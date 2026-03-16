"""Vision-based agents that use coordinate-based actions via Playwright.

These agents bypass the browser-use library entirely.  They manage their own
Playwright browser, capture screenshots, send them to an LLM API, parse
coordinate-based actions from the response, and execute them via Playwright's
low-level mouse/keyboard APIs.

Built-in implementations:
  - GeminiComputerUseAgent: Google Gemini computer-use function-calling API.
  - ClaudeComputerUseAgent: Anthropic Claude computer-use beta API.
  - KimiVisionAgent: Moonshot Kimi K2.5 with pyautogui-style code output.
"""

from __future__ import annotations

import asyncio
import base64
import json
import os
import re
import time
from pathlib import Path

import requests

from agents import AgentResult


# ---------------------------------------------------------------------------
# Shared Playwright infrastructure
# ---------------------------------------------------------------------------


class VisionAgentBase:
    """Base class for vision-based agents with shared Playwright management.

    Subclasses must implement ``_run_agent_loop`` — the API-specific agentic
    loop that takes screenshots, calls an LLM, and returns actions.
    """

    def __init__(
        self,
        *,
        viewport_width: int = 1440,
        viewport_height: int = 900,
        max_steps: int = 50,
        timeout: int = 300,
        headless: bool = True,
    ):
        self.viewport_width = viewport_width
        self.viewport_height = viewport_height
        self.max_steps = max_steps
        self.timeout = timeout
        self.headless = headless
        self._playwright = None
        self._browser = None
        self._page = None
        self._server_url: str | None = None

    # -- lifecycle -----------------------------------------------------------

    async def _launch_browser(self) -> None:
        from playwright.async_api import async_playwright

        self._playwright = await async_playwright().start()
        self._browser = await self._playwright.chromium.launch(
            headless=self.headless,
            args=[
                "--disable-gpu",
                "--disable-software-rasterizer",
                "--disable-extensions",
                "--no-sandbox",
                "--disable-dev-shm-usage",
            ],
        )
        self._page = await self._browser.new_page(
            viewport={"width": self.viewport_width, "height": self.viewport_height},
        )

    async def _close_browser(self) -> None:
        if self._page:
            try:
                await self._page.close()
            except Exception:
                pass
            self._page = None
        if self._browser:
            try:
                await self._browser.close()
            except Exception:
                pass
            self._browser = None
        if self._playwright:
            try:
                await self._playwright.stop()
            except Exception:
                pass
            self._playwright = None

    async def setup(self, server_url: str) -> None:
        self._server_url = server_url
        await self._launch_browser()
        await self._page.goto(server_url, wait_until="load")

        # Poll for seed state (same pattern as BrowserUseAgent)
        for _ in range(10):
            await asyncio.sleep(1.0)
            try:
                resp = requests.get(f"{server_url}/api/state", timeout=2)
                if resp.status_code == 200:
                    break
            except requests.RequestException:
                pass
        else:
            raise RuntimeError(
                "Seed state not captured after first load. "
                "GET /api/state never returned 200 within 10s"
            )

    async def restart_session(self) -> None:
        await self._close_browser()
        await self._launch_browser()
        if self._server_url:
            await self._page.goto(self._server_url, wait_until="load")
            await asyncio.sleep(2)

    async def teardown(self) -> None:
        await self._close_browser()

    # -- shared helpers ------------------------------------------------------

    async def take_screenshot(self) -> bytes:
        return await self._page.screenshot(type="png")

    async def execute_action(self, action: dict) -> None:
        """Execute a single parsed action dict via Playwright.

        Supported action types (all coordinates in CSS pixels):
          click(x, y, button="left")
          double_click(x, y)
          type(x, y, text, clear=False, press_enter=False)
          scroll(x, y, direction, amount=3)
          key(keys)  — e.g. "Control+c"
          hover(x, y)
          drag(x, y, dest_x, dest_y)
          navigate(url)
          go_back()
          wait(seconds)
        """
        kind = action.get("type", "")
        page = self._page

        if kind == "click":
            await page.mouse.click(
                action["x"], action["y"],
                button=action.get("button", "left"),
            )
        elif kind == "double_click":
            await page.mouse.dblclick(action["x"], action["y"])
        elif kind == "type":
            x, y = action.get("x"), action.get("y")
            if x is not None and y is not None:
                await page.mouse.click(x, y)
                await asyncio.sleep(0.1)
            if action.get("clear"):
                await page.keyboard.press("Control+a")
                await page.keyboard.press("Backspace")
                await asyncio.sleep(0.05)
            text = action.get("text", "")
            await page.keyboard.type(text, delay=20)
            if action.get("press_enter"):
                await page.keyboard.press("Enter")
        elif kind == "scroll":
            x = action.get("x", self.viewport_width // 2)
            y = action.get("y", self.viewport_height // 2)
            direction = action.get("direction", "down")
            amount = action.get("amount", 3)
            # Playwright scroll uses delta pixels; 100px per unit
            delta = amount * 100
            if direction == "up":
                delta = -delta
            elif direction == "left":
                await page.mouse.move(x, y)
                await page.evaluate(f"window.scrollBy(-{delta}, 0)")
                return
            elif direction == "right":
                await page.mouse.move(x, y)
                await page.evaluate(f"window.scrollBy({delta}, 0)")
                return
            await page.mouse.move(x, y)
            await page.mouse.wheel(0, delta)
        elif kind == "key":
            keys = action.get("keys", "")
            await page.keyboard.press(keys)
        elif kind == "hover":
            await page.mouse.move(action["x"], action["y"])
        elif kind == "drag":
            await page.mouse.move(action["x"], action["y"])
            await page.mouse.down()
            await page.mouse.move(action["dest_x"], action["dest_y"], steps=10)
            await page.mouse.up()
        elif kind == "navigate":
            await page.goto(action["url"], wait_until="load")
        elif kind == "go_back":
            await page.go_back()
        elif kind == "wait":
            await asyncio.sleep(action.get("seconds", 5))

        # Brief settle after action
        await asyncio.sleep(0.3)

    async def run(self, task: str, server_url: str, task_dir: Path) -> AgentResult:
        """Run a single task.  Delegates to subclass ``_run_agent_loop``."""
        task_dir.mkdir(parents=True, exist_ok=True)
        screenshots_dir = task_dir / "screenshots"
        screenshots_dir.mkdir(exist_ok=True)

        t0 = time.time()
        timed_out = False
        steps = 0
        is_done = False
        final_result = None
        errors: list[str] = []
        history: list[dict] = []

        try:
            result_data = await asyncio.wait_for(
                self._run_agent_loop(
                    task=task,
                    server_url=server_url,
                    task_dir=task_dir,
                    screenshots_dir=screenshots_dir,
                ),
                timeout=self.timeout,
            )
            steps = result_data.get("steps", 0)
            is_done = result_data.get("is_done", False)
            final_result = result_data.get("final_result")
            errors = result_data.get("errors", [])
            history = result_data.get("history", [])
        except asyncio.TimeoutError:
            timed_out = True
            errors.append(f"Timeout after {self.timeout}s")

        elapsed = time.time() - t0

        # Save history (may be partial on timeout)
        with open(task_dir / "history.json", "w") as f:
            json.dump({"history": history, "format": "vision_agent"}, f, indent=2)

        if timed_out:
            raise asyncio.TimeoutError()

        return AgentResult(
            elapsed=round(elapsed, 1),
            steps=steps,
            is_done=is_done,
            final_result=final_result,
            errors=errors,
        )

    async def _run_agent_loop(
        self,
        task: str,
        server_url: str,
        task_dir: Path,
        screenshots_dir: Path,
    ) -> dict:
        """Subclasses implement this.  Returns dict with keys:
        steps, is_done, final_result, errors, history."""
        raise NotImplementedError


# ---------------------------------------------------------------------------
# Gemini Computer Use Agent
# ---------------------------------------------------------------------------


class GeminiComputerUseAgent(VisionAgentBase):
    """Agent using Google Gemini's computer-use function-calling API.

    Requires the ``google-genai`` package and a ``GOOGLE_API_KEY`` env var.
    Coordinates use a normalized 0-999 grid; recommended viewport 1440x900.
    """

    MODEL = "gemini-2.5-computer-use-preview-10-2025"

    def __init__(self, *, max_steps: int = 50, timeout: int = 300, headless: bool = True, **_kw):
        super().__init__(
            viewport_width=1440,
            viewport_height=900,
            max_steps=max_steps,
            timeout=timeout,
            headless=headless,
        )
        self._client = None

    def _get_client(self):
        if self._client is None:
            from google import genai
            self._client = genai.Client()
        return self._client

    # -- coordinate conversion -----------------------------------------------

    def _norm_to_pixel(self, x_norm: float, y_norm: float) -> tuple[int, int]:
        """Convert Gemini's 0-999 normalized coords to pixel coords."""
        px = int(x_norm / 1000 * self.viewport_width)
        py = int(y_norm / 1000 * self.viewport_height)
        return px, py

    # -- action parsing ------------------------------------------------------

    def _parse_gemini_action(self, fc) -> dict | None:
        """Convert a Gemini function_call to an internal action dict."""
        name = fc.name
        args = dict(fc.args) if fc.args else {}

        if name == "click_at":
            px, py = self._norm_to_pixel(args["x"], args["y"])
            return {"type": "click", "x": px, "y": py}
        elif name == "type_text_at":
            px, py = self._norm_to_pixel(args["x"], args["y"])
            return {
                "type": "type", "x": px, "y": py,
                "text": args.get("text", ""),
                "press_enter": args.get("press_enter", False),
                "clear": args.get("clear_before_typing", False),
            }
        elif name == "scroll_document":
            return {
                "type": "scroll",
                "x": self.viewport_width // 2,
                "y": self.viewport_height // 2,
                "direction": args.get("direction", "down"),
                "amount": 3,
            }
        elif name == "scroll_at":
            px, py = self._norm_to_pixel(args["x"], args["y"])
            magnitude = args.get("magnitude", 500)
            return {
                "type": "scroll", "x": px, "y": py,
                "direction": args.get("direction", "down"),
                "amount": max(1, int(magnitude / 100)),
            }
        elif name == "hover_at":
            px, py = self._norm_to_pixel(args["x"], args["y"])
            return {"type": "hover", "x": px, "y": py}
        elif name == "key_combination":
            keys = args.get("keys", "")
            # Gemini uses "Control+C" style — Playwright expects the same
            return {"type": "key", "keys": keys}
        elif name == "navigate":
            return {"type": "navigate", "url": args.get("url", "")}
        elif name == "go_back":
            return {"type": "go_back"}
        elif name == "go_forward":
            return {"type": "key", "keys": "Alt+ArrowRight"}
        elif name == "wait_5_seconds":
            return {"type": "wait", "seconds": 5}
        elif name == "drag_and_drop":
            sx, sy = self._norm_to_pixel(args["x"], args["y"])
            dx, dy = self._norm_to_pixel(args["destination_x"], args["destination_y"])
            return {"type": "drag", "x": sx, "y": sy, "dest_x": dx, "dest_y": dy}
        elif name in ("search", "open_web_browser"):
            return None  # no-op in our context
        return None

    # -- agent loop ----------------------------------------------------------

    async def _run_agent_loop(
        self,
        task: str,
        server_url: str,
        task_dir: Path,
        screenshots_dir: Path,
    ) -> dict:
        from google import genai
        from google.genai import types

        client = self._get_client()

        config = types.GenerateContentConfig(
            tools=[types.Tool(
                computer_use=types.ComputerUse(
                    environment=types.Environment.ENVIRONMENT_BROWSER,
                ),
            )],
        )

        contents = []
        history: list[dict] = []
        errors: list[str] = []
        is_done = False
        final_result = None

        for step in range(self.max_steps):
            # Take screenshot BEFORE deciding action (what the model sees)
            screenshot = await self.take_screenshot()
            ss_path = screenshots_dir / f"step_{step}.png"
            ss_path.write_bytes(screenshot)

            # Build contents for this turn
            if step == 0:
                contents = [
                    types.Content(
                        role="user",
                        parts=[
                            types.Part(text=(
                                f"You are interacting with a web application at {server_url}. "
                                f"Your task: {task}"
                            )),
                            types.Part.from_bytes(data=screenshot, mime_type="image/png"),
                        ],
                    ),
                ]
            else:
                # Send function responses from previous step + new screenshot
                contents.append(
                    types.Content(role="user", parts=self._pending_response_parts + [
                        types.Part.from_bytes(data=screenshot, mime_type="image/png"),
                    ]),
                )

            try:
                response = client.models.generate_content(
                    model=self.MODEL,
                    contents=contents,
                    config=config,
                )
            except Exception as e:
                errors.append(f"API error at step {step}: {e}")
                break

            if not response.candidates:
                errors.append(f"Empty response at step {step} (likely safety-blocked)")
                break

            candidate = response.candidates[0]
            contents.append(candidate.content)

            # Extract text and function calls
            step_text = ""
            function_calls = []
            for part in candidate.content.parts:
                if hasattr(part, "text") and part.text:
                    step_text += part.text
                if hasattr(part, "function_call") and part.function_call:
                    function_calls.append(part.function_call)

            if not function_calls:
                # Model is done — no more actions
                is_done = True
                final_result = step_text
                history.append({
                    "model_output": {
                        "current_state": {"thought": step_text},
                        "action": [],
                    },
                    "result": [{"extracted_content": "Task completed (no more actions)"}],
                })
                break

            # Execute each function call
            actions_taken = []
            parsed_actions = []
            self._pending_response_parts = []
            for fc in function_calls:
                action = self._parse_gemini_action(fc)
                action_desc = f"{fc.name}({dict(fc.args) if fc.args else {}})"
                actions_taken.append(action_desc)
                if action:
                    parsed_actions.append(action)

                if action:
                    try:
                        await self.execute_action(action)
                    except Exception as e:
                        errors.append(f"Action error at step {step}: {e}")

                fr_fields = {"url": self._page.url}
                if fc.args and "safety_decision" in fc.args:
                    fr_fields["safety_acknowledgement"] = "true"
                self._pending_response_parts.append(
                    types.Part.from_function_response(
                        name=fc.name,
                        response=fr_fields,
                    )
                )

            # Record step in history — step_{step}.png is what model saw
            history.append({
                "model_output": {
                    "current_state": {"thought": step_text},
                    "action": [{a: ""} for a in actions_taken],
                },
                "result": [{"extracted_content": "; ".join(actions_taken)}],
                "coordinates": parsed_actions,
            })


        return {
            "steps": len(history),
            "is_done": is_done,
            "final_result": final_result,
            "errors": errors,
            "history": history,
        }


# ---------------------------------------------------------------------------
# Claude Computer Use Agent
# ---------------------------------------------------------------------------


class ClaudeComputerUseAgent(VisionAgentBase):
    """Agent using Anthropic Claude's computer-use beta API.

    Requires the ``anthropic`` package and an ``ANTHROPIC_API_KEY`` env var.
    Uses absolute pixel coordinates matching the configured display size.
    """

    MODEL = "claude-sonnet-4-6"
    TOOL_VERSION = "computer_20251124"
    BETA_FLAG = "computer-use-2025-11-24"

    def __init__(self, *, max_steps: int = 50, timeout: int = 300, headless: bool = True, **_kw):
        super().__init__(
            viewport_width=1280,
            viewport_height=800,
            max_steps=max_steps,
            timeout=timeout,
            headless=headless,
        )
        self._client = None

    def _get_client(self):
        if self._client is None:
            import anthropic
            self._client = anthropic.Anthropic()
        return self._client

    # -- action parsing ------------------------------------------------------

    @staticmethod
    def _parse_claude_action(tool_input: dict) -> dict | None:
        """Convert Claude computer-use tool input to an internal action dict."""
        action = tool_input.get("action", "")
        coord = tool_input.get("coordinate")  # [x, y]

        if action == "screenshot":
            return None  # We handle screenshots ourselves
        elif action == "left_click" and coord:
            return {"type": "click", "x": coord[0], "y": coord[1]}
        elif action == "right_click" and coord:
            return {"type": "click", "x": coord[0], "y": coord[1], "button": "right"}
        elif action == "middle_click" and coord:
            return {"type": "click", "x": coord[0], "y": coord[1], "button": "middle"}
        elif action == "double_click" and coord:
            return {"type": "double_click", "x": coord[0], "y": coord[1]}
        elif action == "triple_click" and coord:
            return {"type": "double_click", "x": coord[0], "y": coord[1]}  # approximate
        elif action == "type":
            return {"type": "type", "text": tool_input.get("text", "")}
        elif action == "key":
            keys = tool_input.get("text", "")
            # Claude uses "ctrl+a" style — Playwright expects "Control+a"
            key_map = {"ctrl": "Control", "alt": "Alt", "shift": "Shift",
                       "super": "Meta", "return": "Enter", "space": " ",
                       "tab": "Tab", "escape": "Escape", "backspace": "Backspace",
                       "delete": "Delete"}
            parts = keys.split("+")
            mapped = [key_map.get(p.lower().strip(), p) for p in parts]
            return {"type": "key", "keys": "+".join(mapped)}
        elif action == "mouse_move" and coord:
            return {"type": "hover", "x": coord[0], "y": coord[1]}
        elif action == "scroll" and coord:
            direction = tool_input.get("scroll_direction", "down")
            amount = tool_input.get("scroll_amount", 3)
            return {
                "type": "scroll", "x": coord[0], "y": coord[1],
                "direction": direction, "amount": amount,
            }
        elif action == "left_click_drag" and coord:
            end = tool_input.get("end_coordinate", coord)
            return {
                "type": "drag",
                "x": coord[0], "y": coord[1],
                "dest_x": end[0], "dest_y": end[1],
            }
        elif action == "wait":
            duration = tool_input.get("duration", 5)
            return {"type": "wait", "seconds": duration}
        return None

    # -- agent loop ----------------------------------------------------------

    async def _run_agent_loop(
        self,
        task: str,
        server_url: str,
        task_dir: Path,
        screenshots_dir: Path,
    ) -> dict:
        import anthropic

        client = self._get_client()

        tools = [
            {
                "type": self.TOOL_VERSION,
                "name": "computer",
                "display_width_px": self.viewport_width,
                "display_height_px": self.viewport_height,
            },
        ]

        messages = []
        history: list[dict] = []
        errors: list[str] = []
        is_done = False
        final_result = None

        for step in range(self.max_steps):
            # Take screenshot BEFORE deciding action (what the model sees)
            screenshot = await self.take_screenshot()
            ss_path = screenshots_dir / f"step_{step}.png"
            ss_path.write_bytes(screenshot)
            b64_screenshot = base64.b64encode(screenshot).decode()

            if step == 0:
                messages = [
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                "text": (
                                    f"You are interacting with a web application at {server_url}. "
                                    f"Your task: {task}"
                                ),
                            },
                            {
                                "type": "image",
                                "source": {
                                    "type": "base64",
                                    "media_type": "image/png",
                                    "data": b64_screenshot,
                                },
                            },
                        ],
                    },
                ]
            else:
                # Send tool results from previous step with new screenshot
                self._pending_tool_results[-1]["content"] = [
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": "image/png",
                            "data": b64_screenshot,
                        },
                    },
                ]
                messages.append({"role": "user", "content": self._pending_tool_results})

            try:
                response = client.beta.messages.create(
                    model=self.MODEL,
                    max_tokens=4096,
                    tools=tools,
                    messages=messages,
                    betas=[self.BETA_FLAG],
                )
            except Exception as e:
                errors.append(f"API error at step {step}: {e}")
                break

            # Process response content blocks
            response_content = response.content
            messages.append({"role": "assistant", "content": response_content})

            # Extract text and tool_use blocks
            step_text = ""
            tool_uses = []
            for block in response_content:
                if hasattr(block, "text"):
                    step_text += block.text
                if block.type == "tool_use":
                    tool_uses.append(block)

            # If no tool calls, Claude is done
            if not tool_uses:
                is_done = True
                final_result = step_text
                history.append({
                    "model_output": {
                        "current_state": {"thought": step_text},
                        "action": [],
                    },
                    "result": [{"extracted_content": "Task completed (no more actions)"}],
                })
                break

            # Execute each tool use
            parsed_actions = []
            actions_taken = []
            self._pending_tool_results = []

            for tu in tool_uses:
                if tu.name != "computer":
                    self._pending_tool_results.append({
                        "type": "tool_result",
                        "tool_use_id": tu.id,
                        "content": "Unknown tool",
                        "is_error": True,
                    })
                    continue

                tool_input = tu.input
                action_name = tool_input.get("action", "")

                # Handle screenshot action — just take a fresh screenshot
                if action_name == "screenshot":
                    actions_taken.append("screenshot")
                    self._pending_tool_results.append({
                        "type": "tool_result",
                        "tool_use_id": tu.id,
                        "content": [],  # will be filled with screenshot next iteration
                    })
                    continue

                # Parse and execute action
                action = self._parse_claude_action(tool_input)
                action_desc = f"{action_name}({tool_input})"
                actions_taken.append(action_desc)

                if action:
                    parsed_actions.append(action)
                    try:
                        await self.execute_action(action)
                    except Exception as e:
                        errors.append(f"Action error at step {step}: {e}")

                self._pending_tool_results.append({
                    "type": "tool_result",
                    "tool_use_id": tu.id,
                    "content": [],  # will be filled with screenshot next iteration
                })

            # Record step in history — step_{step}.png is what model saw
            history.append({
                "model_output": {
                    "current_state": {"thought": step_text},
                    "action": [{a: ""} for a in actions_taken],
                },
                "result": [{"extracted_content": "; ".join(actions_taken)}],
                "coordinates": parsed_actions,
            })

            # If stop_reason is not tool_use, Claude is done
            if response.stop_reason != "tool_use":
                is_done = True
                final_result = step_text
                break


        return {
            "steps": len(history),
            "is_done": is_done,
            "final_result": final_result,
            "errors": errors,
            "history": history,
        }


# ---------------------------------------------------------------------------
# Kimi K2.5 Vision Agent
# ---------------------------------------------------------------------------


_KIMI_SYSTEM_PROMPT = """
You are a GUI agent. You are given an instruction, a screenshot of the screen and your previous interactions with the computer. You need to perform a series of actions to complete the task.

For each step, provide your response in this format:
## Thought
{thought}
## Action:
{action}
## Code:
{code}

In the code section, the code should be either pyautogui code or one of the following functions wrapped in the code block:
- {"name": "computer.wait", "description": "Make the computer wait for 20 seconds for installation, running code, etc.", "parameters": {"type": "object", "properties": {}, "required": []}}
- {"name": "computer.terminate", "description": "Terminate the current task and report its completion status", "parameters": {"type": "object", "properties": {"status": {"type": "string", "enum": ["success", "failure"], "description": "The status of the task"}, "answer": {"type": "string", "description": "The answer of the task"}}, "required": ["status"]}}
""".strip()

_KIMI_INSTRUCTION_TEMPLATE = (
    "# Task Instruction:\n{instruction}\n\n"
    "Please generate the next move according to the screenshot, "
    "task instruction and previous steps (if provided).\n"
)

_KIMI_STEP_TEMPLATE = "# Step {step_num}:\n"

_KIMI_HISTORY_TEMPLATE = "## Thought:\n{thought}\n\n## Action:\n{action}\n"


class KimiVisionAgent(VisionAgentBase):
    """Agent using Moonshot Kimi K2.5's vision API with pyautogui-style output.

    Uses the OpenAI SDK pointed at Moonshot's OpenAI-compatible endpoint.
    Requires ``openai`` package and a ``KIMI_API_KEY`` env var.
    Uses relative coordinates (0-1) mapped to a 1920x1080 viewport.
    """

    MODEL = "kimi-k2.5"
    BASE_URL = "https://api.moonshot.ai/v1"

    def __init__(self, *, max_steps: int = 50, timeout: int = 300, headless: bool = True, **_kw):
        super().__init__(
            viewport_width=1920,
            viewport_height=1080,
            max_steps=max_steps,
            timeout=timeout,
            headless=headless,
        )
        self._client = None

    def _get_client(self):
        if self._client is None:
            from openai import OpenAI
            api_key = os.environ.get("KIMI_API_KEY", "")
            if not api_key:
                raise RuntimeError("KIMI_API_KEY environment variable not set")
            self._client = OpenAI(api_key=api_key, base_url=self.BASE_URL)
        return self._client

    # -- API call ------------------------------------------------------------

    def _call_api(self, messages: list[dict]) -> dict:
        client = self._get_client()

        for attempt in range(5):
            try:
                response = client.chat.completions.create(
                    model=self.MODEL,
                    messages=messages,
                    max_tokens=4096,
                    top_p=0.95,
                    temperature=1,
                )
                choice = response.choices[0]
                if choice.finish_reason == "stop":
                    msg = choice.message
                    return {
                        "content": msg.content or "",
                        "reasoning_content": getattr(msg, "reasoning_content", "") or "",
                    }
                if attempt < 4:
                    time.sleep(5)
                    continue
                raise RuntimeError("Kimi API did not finish properly")
            except Exception as e:
                if attempt < 4 and "timeout" in str(e).lower():
                    time.sleep(5)
                    continue
                if attempt >= 4:
                    raise
                time.sleep(5)

        raise RuntimeError("Kimi API max retries exceeded")

    # -- response parsing ----------------------------------------------------

    @staticmethod
    def _parse_response(response: dict) -> tuple[str, str, list[dict]]:
        """Parse Kimi response into (thought, action_desc, actions).

        Returns parsed action dicts ready for execute_action().
        """
        content = response.get("content", "").strip()
        reasoning = response.get("reasoning_content", "")

        # Extract thought
        thought_match = re.search(
            r"##\s*Thought\s*:?\s*\n(.*?)(?=##\s*Action|$)",
            content, re.DOTALL,
        )
        thought = thought_match.group(1).strip() if thought_match else reasoning or ""

        # Extract action description
        action_match = re.search(
            r"##\s*Action\s*:?\s*\n(.*?)(?=##\s*Code|$)",
            content, re.DOTALL,
        )
        action_desc = action_match.group(1).strip() if action_match else ""

        # Extract code block
        code_blocks = re.findall(
            r"```(?:python|code)?\s*(.*?)\s*```",
            content, re.DOTALL | re.IGNORECASE,
        )
        if not code_blocks:
            return thought, action_desc, []

        code = code_blocks[-1].strip()

        # Check for special commands
        if "computer.wait" in code.lower():
            return thought, action_desc, [{"type": "wait", "seconds": 5}]
        if "computer.terminate" in code.lower():
            status = "done" if "success" in code.lower() else "fail"
            return thought, action_desc, [{"type": "_terminate", "status": status}]

        # Parse pyautogui calls into action dicts
        actions = KimiVisionAgent._parse_pyautogui_code(code)
        return thought, action_desc, actions

    @staticmethod
    def _parse_pyautogui_code(code: str) -> list[dict]:
        """Parse pyautogui function calls from code string into action dicts.

        Handles: click, doubleClick, rightClick, moveTo, typewrite/write,
        hotkey, press, scroll, dragTo.  Coordinates are treated as relative
        (0-1) and converted to absolute later.
        """
        actions = []

        # Match pyautogui.xxx(...) calls
        for match in re.finditer(r"pyautogui\.(\w+)\((.*?)\)", code, re.DOTALL):
            func_name = match.group(1)
            args_str = match.group(2).strip()

            # Simple arg parser: extract positional and keyword args
            parsed = _parse_args_simple(args_str)

            if func_name in ("click", "leftClick"):
                x, y = _get_xy(parsed)
                actions.append({"type": "click", "x": x, "y": y})
            elif func_name == "rightClick":
                x, y = _get_xy(parsed)
                actions.append({"type": "click", "x": x, "y": y, "button": "right"})
            elif func_name == "doubleClick":
                x, y = _get_xy(parsed)
                actions.append({"type": "double_click", "x": x, "y": y})
            elif func_name == "moveTo":
                x, y = _get_xy(parsed)
                actions.append({"type": "hover", "x": x, "y": y})
            elif func_name in ("typewrite", "write"):
                text = parsed.get(0, parsed.get("text", ""))
                if isinstance(text, str):
                    text = text.strip("'\"")
                actions.append({"type": "type", "text": str(text)})
            elif func_name == "hotkey":
                # hotkey('ctrl', 'a') → "Control+a"
                keys = [str(parsed.get(i, "")).strip("'\"") for i in range(10) if i in parsed]
                key_map = {"ctrl": "Control", "alt": "Alt", "shift": "Shift",
                           "enter": "Enter", "return": "Enter", "tab": "Tab",
                           "delete": "Delete", "backspace": "Backspace",
                           "escape": "Escape", "esc": "Escape"}
                mapped = [key_map.get(k.lower(), k) for k in keys if k]
                if mapped:
                    actions.append({"type": "key", "keys": "+".join(mapped)})
            elif func_name == "press":
                key = str(parsed.get(0, parsed.get("key", ""))).strip("'\"")
                key_map = {"enter": "Enter", "return": "Enter", "tab": "Tab",
                           "escape": "Escape", "esc": "Escape", "backspace": "Backspace",
                           "delete": "Delete", "space": " ", "up": "ArrowUp",
                           "down": "ArrowDown", "left": "ArrowLeft", "right": "ArrowRight"}
                actions.append({"type": "key", "keys": key_map.get(key.lower(), key)})
            elif func_name == "scroll":
                amount = int(float(parsed.get(0, parsed.get("clicks", 3))))
                direction = "down" if amount < 0 else "up"
                x = parsed.get("x", parsed.get(1))
                y = parsed.get("y", parsed.get(2))
                action = {
                    "type": "scroll",
                    "direction": direction,
                    "amount": abs(amount),
                }
                if x is not None and y is not None:
                    action["x"] = float(x)
                    action["y"] = float(y)
                actions.append(action)
            elif func_name == "dragTo":
                x, y = _get_xy(parsed)
                actions.append({"type": "drag", "x": 0, "y": 0, "dest_x": x, "dest_y": y})

        # Handle time.sleep calls
        for match in re.finditer(r"time\.sleep\((\d+(?:\.\d+)?)\)", code):
            actions.append({"type": "wait", "seconds": float(match.group(1))})

        return actions

    def _convert_relative_coords(self, actions: list[dict]) -> list[dict]:
        """Convert relative (0-1) coordinates to absolute pixel coords."""
        for action in actions:
            for key in ("x", "dest_x"):
                if key in action:
                    v = float(action[key])
                    if v <= 1.0:
                        action[key] = int(round(v * self.viewport_width))
                    else:
                        action[key] = int(round(v))
            for key in ("y", "dest_y"):
                if key in action:
                    v = float(action[key])
                    if v <= 1.0:
                        action[key] = int(round(v * self.viewport_height))
                    else:
                        action[key] = int(round(v))
        return actions

    # -- agent loop ----------------------------------------------------------

    async def _run_agent_loop(
        self,
        task: str,
        server_url: str,
        task_dir: Path,
        screenshots_dir: Path,
    ) -> dict:
        history: list[dict] = []
        errors: list[str] = []
        is_done = False
        final_result = None
        max_image_history = 3

        # Track observations and cots for history replay (OSWorld pattern)
        observations: list[bytes] = []
        cots: list[dict] = []

        instruction_prompt = _KIMI_INSTRUCTION_TEMPLATE.format(instruction=task)

        for step in range(self.max_steps):
            # Take screenshot
            screenshot = await self.take_screenshot()
            ss_path = screenshots_dir / f"step_{step}.png"
            ss_path.write_bytes(screenshot)
            b64_screenshot = base64.b64encode(screenshot).decode()

            # Build messages from scratch each turn (OSWorld pattern):
            # system → [old history text-only] → [recent history with images] → current screenshot
            messages: list[dict] = [
                {"role": "system", "content": _KIMI_SYSTEM_PROMPT},
            ]

            # Replay history as alternating user/assistant messages
            for i in range(len(cots)):
                if i > len(cots) - max_image_history:
                    # Recent steps: include screenshot image
                    messages.append({
                        "role": "user",
                        "content": [
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": f"data:image/png;base64,{base64.b64encode(observations[i]).decode()}",
                                },
                            },
                        ],
                    })
                    messages.append({
                        "role": "assistant",
                        "content": (
                            _KIMI_STEP_TEMPLATE.format(step_num=i + 1)
                            + _KIMI_HISTORY_TEMPLATE.format(
                                thought=cots[i].get("thought", ""),
                                action=cots[i].get("action", ""),
                            )
                        ),
                    })
                elif i == len(cots) - max_image_history:
                    # Batch older steps as text-only in one assistant message
                    old_texts = []
                    for j in range(i + 1):
                        old_texts.append(
                            _KIMI_STEP_TEMPLATE.format(step_num=j + 1)
                            + _KIMI_HISTORY_TEMPLATE.format(
                                thought=cots[j].get("thought", ""),
                                action=cots[j].get("action", ""),
                            )
                        )
                    messages.append({
                        "role": "assistant",
                        "content": "\n".join(old_texts),
                    })

            # Current observation + instruction
            user_content: list[dict] = [
                {
                    "type": "image_url",
                    "image_url": {"url": f"data:image/png;base64,{b64_screenshot}"},
                },
                {
                    "type": "text",
                    "text": instruction_prompt,
                },
            ]
            messages.append({"role": "user", "content": user_content})

            # Call API
            try:
                response = self._call_api(messages)
            except Exception as e:
                errors.append(f"API error at step {step}: {e}")
                break

            # Parse response
            thought, action_desc, actions = self._parse_response(response)

            if not actions:
                errors.append(f"No actions parsed at step {step}")
                break

            # Check for termination
            if any(a.get("type") == "_terminate" for a in actions):
                is_done = True
                status = next(
                    (a["status"] for a in actions if a.get("type") == "_terminate"),
                    "done",
                )
                final_result = f"Agent terminated with status: {status}"
                history.append({
                    "model_output": {
                        "current_state": {"thought": thought},
                        "action": [{action_desc: ""}],
                    },
                    "result": [{"extracted_content": final_result}],
                })
                break

            # Convert coordinates and execute
            actions = self._convert_relative_coords(actions)
            for action in actions:
                try:
                    await self.execute_action(action)
                except Exception as e:
                    errors.append(f"Action error at step {step}: {e}")

            # Store for history replay
            observations.append(screenshot)
            cots.append({"thought": thought, "action": action_desc})

            # Record step with coordinate data for report visualization
            history.append({
                "model_output": {
                    "current_state": {"thought": thought},
                    "action": [{action_desc: ""}] if action_desc else [{"code": str(actions)}],
                },
                "result": [{"extracted_content": action_desc or str(actions)}],
                "coordinates": actions,
            })

        return {
            "steps": len(history),
            "is_done": is_done,
            "final_result": final_result,
            "errors": errors,
            "history": history,
        }


# ---------------------------------------------------------------------------
# Utilities
# ---------------------------------------------------------------------------


def _parse_args_simple(args_str: str) -> dict:
    """Parse a Python function call's arguments into a dict.

    Positional args get integer keys (0, 1, 2, ...).
    Keyword args get string keys.
    """
    result: dict = {}
    if not args_str.strip():
        return result

    # Split by commas, respecting strings and parens
    parts = []
    depth = 0
    current = []
    in_str = None
    for ch in args_str:
        if ch in ('"', "'") and not in_str:
            in_str = ch
        elif ch == in_str:
            in_str = None
        elif not in_str:
            if ch == "(":
                depth += 1
            elif ch == ")":
                depth -= 1
            elif ch == "," and depth == 0:
                parts.append("".join(current).strip())
                current = []
                continue
        current.append(ch)
    if current:
        parts.append("".join(current).strip())

    pos_idx = 0
    for part in parts:
        if "=" in part and not part.startswith(("'", '"')):
            key, _, val = part.partition("=")
            key = key.strip()
            val = val.strip().strip("'\"")
            try:
                result[key] = float(val) if "." in val else int(val)
            except ValueError:
                result[key] = val
        else:
            val = part.strip().strip("'\"")
            try:
                result[pos_idx] = float(val) if "." in val else int(val)
            except ValueError:
                result[pos_idx] = val
            pos_idx += 1

    return result


def _get_xy(parsed: dict) -> tuple[float, float]:
    """Extract x, y from parsed args (positional or keyword)."""
    x = parsed.get("x", parsed.get(0, 0))
    y = parsed.get("y", parsed.get(1, 0))
    return float(x), float(y)


def _prune_image_messages(messages: list[dict], max_images: int) -> None:
    """Remove image data from older messages to control context size.

    Keeps the system message and the last ``max_images`` user messages
    with images intact; strips image_url entries from older messages.
    """
    # Find indices of user messages with images
    image_indices = []
    for i, msg in enumerate(messages):
        if msg.get("role") == "user" and isinstance(msg.get("content"), list):
            if any(p.get("type") == "image_url" for p in msg["content"]):
                image_indices.append(i)

    # Remove images from all but the last N
    to_strip = image_indices[:-max_images] if len(image_indices) > max_images else []
    for idx in to_strip:
        msg = messages[idx]
        msg["content"] = [
            p for p in msg["content"] if p.get("type") != "image_url"
        ]
        # If only text remains and it's a single item, simplify
        if len(msg["content"]) == 1 and msg["content"][0].get("type") == "text":
            msg["content"] = msg["content"][0]["text"]
