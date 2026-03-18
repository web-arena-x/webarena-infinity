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
# Rate-limit retry helpers
# ---------------------------------------------------------------------------

def _is_rate_limit(exc: Exception) -> bool:
    """Return True if the exception indicates a rate-limit / quota error."""
    s = str(exc).lower()
    return "429" in s or "resource_exhausted" in s or ("rate" in s and "limit" in s)


async def _async_retry_api_call(fn, *, max_retries: int = 3, base_delay: float = 5.0):
    """Call *fn()* with exponential backoff on rate-limit errors.

    *fn()* may be a sync callable (run in a thread) or return a coroutine.
    Uses ``asyncio.sleep`` so that ``asyncio.wait_for`` can cancel retries.

    Defaults: 3 retries with backoff 5 / 10 / 20 s (35 s worst-case).
    """
    for attempt in range(max_retries + 1):
        try:
            result = fn()
            if asyncio.iscoroutine(result):
                result = await result
            return result
        except Exception as e:
            if _is_rate_limit(e) and attempt < max_retries:
                delay = base_delay * (2 ** attempt)
                await asyncio.sleep(delay)
                continue
            raise


async def _async_retry_step_api_call(fn, *, max_retries: int = 1, base_delay: float = 3.0):
    """Retry *fn()* on ANY transient error, with short backoff.

    Wraps the outer API call for a single step.  Rate-limit errors are
    already handled by the inner ``_async_retry_api_call``, so this catches
    transient server errors (500, timeout, network blip).

    Uses ``asyncio.sleep`` so that ``asyncio.wait_for`` can cancel retries.

    Defaults: 1 retry after 3 s (single quick retry for network blips).

    Returns ``(result, None)`` on success, or ``(None, error_string)``
    after exhausting retries.
    """
    last_error = None
    for attempt in range(max_retries + 1):
        try:
            result = fn()
            if asyncio.iscoroutine(result):
                result = await result
            return result, None
        except Exception as e:
            last_error = e
            if attempt < max_retries:
                delay = base_delay * (2 ** attempt)
                await asyncio.sleep(delay)
    return None, f"API error after {max_retries + 1} attempts: {last_error}"


# ---------------------------------------------------------------------------
# Step result — returned by _parse_response hooks
# ---------------------------------------------------------------------------


class StepResult:
    """Parsed LLM response for one agent step."""

    __slots__ = ("actions", "text", "is_done", "action_descriptions", "raw")

    def __init__(
        self,
        *,
        actions: list[dict],
        text: str = "",
        is_done: bool = False,
        action_descriptions: list[str] | None = None,
        raw: object = None,
    ):
        self.actions = actions
        self.text = text
        self.is_done = is_done
        self.action_descriptions = action_descriptions or []
        self.raw = raw  # opaque — subclass stores whatever _execute_step needs


# ---------------------------------------------------------------------------
# Shared Playwright infrastructure (template-method base class)
# ---------------------------------------------------------------------------


class VisionAgentBase:
    """Base class for vision-based agents with shared Playwright management.

    Subclasses implement four hooks:

      _init_conversation  — set up client & conversation state
      _prepare_step       — build messages for this turn
      _call_llm_inner     — make the API call (rate-limit retry inside)
      _parse_response     — parse raw response → StepResult

    Optionally override:
      _execute_step       — execute actions + build API feedback
      _on_step_done       — post-action bookkeeping
    """

    def __init__(
        self,
        *,
        viewport_width: int = 1440,
        viewport_height: int = 900,
        max_steps: int = 50,
        timeout: int = 300,
        headless: bool = True,
        max_consecutive_failures: int = 5,
    ):
        self.viewport_width = viewport_width
        self.viewport_height = viewport_height
        self.max_steps = max_steps
        self.timeout = timeout
        self.headless = headless
        self.max_consecutive_failures = max_consecutive_failures
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
        # Auto-dismiss JS dialogs (alert, confirm, prompt, beforeunload)
        self._page.on("dialog", lambda d: asyncio.ensure_future(self._dismiss_dialog(d)))

    @staticmethod
    async def _dismiss_dialog(dialog) -> None:
        try:
            await dialog.accept()
        except Exception:
            pass

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

    async def _check_browser_health(self) -> bool:
        """Return True if the browser is alive; attempt restart if not."""
        try:
            await asyncio.wait_for(self._page.evaluate("1+1"), timeout=3.0)
            return True
        except Exception:
            pass
        # Browser appears dead — attempt restart
        try:
            await self._close_browser()
            await self._launch_browser()
            if self._server_url:
                await self._page.goto(self._server_url, wait_until="load")
                await asyncio.sleep(2)
            return True
        except Exception:
            return False

    async def execute_action(self, action: dict) -> None:
        """Execute a single parsed action dict via Playwright.

        Supported action types (all coordinates in CSS pixels):
          click(x, y, button="left")
          double_click(x, y)
          input(x, y, text, clear=False, press_enter=False)
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
        elif kind == "input":
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

    # -- template-method agent loop -----------------------------------------

    async def run(self, task: str, server_url: str, task_dir: Path) -> AgentResult:
        """Run a single task.  Delegates to subclass hooks."""
        task_dir.mkdir(parents=True, exist_ok=True)
        screenshots_dir = task_dir / "screenshots"
        screenshots_dir.mkdir(exist_ok=True)

        # Shared state that _run_agent_loop appends to, so we can
        # recover partial progress even if the loop is cancelled by timeout.
        self._live_history: list[dict] = []
        self._live_errors: list[str] = []

        t0 = time.time()
        timed_out = False
        steps = 0
        is_done = False
        final_result = None

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
            self._live_errors = result_data.get("errors", self._live_errors)
            self._live_history = result_data.get("history", self._live_history)
        except asyncio.TimeoutError:
            timed_out = True
            # Recover partial progress from shared state
            steps = len(self._live_history)
            self._live_errors.append(f"Timeout after {self.timeout}s")

        elapsed = time.time() - t0

        # Save history (may be partial on timeout)
        with open(task_dir / "history.json", "w") as f:
            json.dump({"history": self._live_history, "format": "vision_agent"}, f, indent=2)

        if timed_out:
            raise asyncio.TimeoutError()

        return AgentResult(
            elapsed=round(elapsed, 1),
            steps=steps,
            is_done=is_done,
            final_result=final_result,
            errors=self._live_errors,
        )

    async def _run_agent_loop(
        self,
        task: str,
        server_url: str,
        task_dir: Path,
        screenshots_dir: Path,
    ) -> dict:
        """Template-method loop.  All robustness lives here; subclasses
        provide API-specific hooks."""
        history = self._live_history
        errors = self._live_errors
        is_done = False
        final_result = None
        consecutive_failures = 0
        empty_output_count = 0

        self._init_conversation(task, server_url)

        for step in range(self.max_steps):
            # --- consecutive failure budget ---
            if consecutive_failures >= self.max_consecutive_failures:
                errors.append(
                    f"Stopping after {consecutive_failures} consecutive failures"
                )
                break

            # --- browser health check ---
            if not await self._check_browser_health():
                errors.append(
                    f"Browser died at step {step} and could not be restarted"
                )
                break

            # --- screenshot ---
            screenshot = await self.take_screenshot()
            ss_path = screenshots_dir / f"step_{step}.png"
            ss_path.write_bytes(screenshot)

            # --- subclass: build messages ---
            self._prepare_step(step, screenshot)

            # --- LLM call with step-level retry ---
            response, api_err = await _async_retry_step_api_call(
                lambda: self._call_llm_inner()
            )
            if api_err:
                errors.append(f"Step {step}: {api_err}")
                consecutive_failures += 1
                self._on_api_error()
                continue

            # --- subclass: parse response ---
            result = self._parse_response(response)

            # --- empty output handling ---
            # Only treat as truly empty if the model returned NO function
            # calls / tool uses at all.  If it returned calls we couldn't
            # parse (or that map to no-ops like open_web_browser), we must
            # still call _execute_step so the protocol-required responses
            # (e.g. Gemini function_response) are sent back.
            if not result.actions and not result.is_done and not result.action_descriptions:
                empty_output_count += 1
                if empty_output_count >= 3:
                    is_done = True
                    final_result = result.text
                    history.append(self._make_step_record(result))
                    break
                consecutive_failures += 1
                continue

            # --- clean termination without actions ---
            if result.is_done and not result.actions:
                is_done = True
                final_result = result.text
                history.append(self._make_step_record(result))
                break

            # --- successful output — reset failure counters ---
            consecutive_failures = 0
            empty_output_count = 0

            # --- record step in history BEFORE executing (survives timeout) ---
            step_record = self._make_step_record(result)
            history.append(step_record)

            # --- subclass: execute actions + build API feedback ---
            await self._execute_step(step, result)

            # --- subclass: post-action bookkeeping ---
            self._on_step_done(step, result, screenshot)

            # --- post-action termination (e.g. Claude stop_reason) ---
            if result.is_done:
                is_done = True
                final_result = result.text
                break

        return {
            "steps": len(history),
            "is_done": is_done,
            "final_result": final_result,
            "errors": errors,
            "history": history,
        }

    # -- hooks (subclasses must override first four) -------------------------

    def _init_conversation(self, task: str, server_url: str) -> None:
        """Set up LLM client and initial conversation state."""
        raise NotImplementedError

    def _prepare_step(self, step: int, screenshot: bytes) -> None:
        """Build / update messages for this turn."""
        raise NotImplementedError

    async def _call_llm_inner(self):
        """Make the LLM API call.  Should include rate-limit retry
        (``_async_retry_api_call``).  Returns the raw API response object."""
        raise NotImplementedError

    def _parse_response(self, response) -> StepResult:
        """Parse raw LLM response into a ``StepResult``.  Also update
        conversation state with the response (e.g. append to messages)."""
        raise NotImplementedError

    def _on_api_error(self) -> None:
        """Clean up conversation state after an API error (no-op default)."""

    async def _execute_step(self, step: int, result: StepResult) -> None:
        """Execute actions.  Default iterates ``result.actions``.
        Override to also build API feedback (e.g. Gemini function responses)."""
        for action in result.actions:
            try:
                await self.execute_action(action)
            except Exception as e:
                self._live_errors.append(f"Action error at step {step}: {e}")

    def _make_step_record(self, result: StepResult) -> dict:
        """Build a history record for one step."""
        return {
            "thought": result.text,
            "actions": result.actions,
        }

    def _on_step_done(self, step: int, result: StepResult, screenshot: bytes) -> None:
        """Post-action bookkeeping (e.g. Kimi's observation/cot lists)."""


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
                "type": "input", "x": px, "y": py,
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

    # -- hooks ---------------------------------------------------------------

    def _init_conversation(self, task: str, server_url: str) -> None:
        from google.genai import types
        self._gemini_config = types.GenerateContentConfig(
            tools=[types.Tool(
                computer_use=types.ComputerUse(
                    environment=types.Environment.ENVIRONMENT_BROWSER,
                ),
            )],
        )
        self._contents: list = []
        self._pending_response_parts: list = []
        self._task = task
        self._server_url_task = server_url

    def _prepare_step(self, step: int, screenshot: bytes) -> None:
        from google.genai import types
        if step == 0 or not self._pending_response_parts:
            # Fresh conversation (first step, or recovery after error/reset)
            self._contents = [
                types.Content(
                    role="user",
                    parts=[
                        types.Part(text=(
                            f"You are interacting with a web application at {self._server_url_task}. "
                            f"Your task: {self._task}"
                        )),
                        types.Part.from_bytes(data=screenshot, mime_type="image/png"),
                    ],
                ),
            ]
        else:
            parts = list(self._pending_response_parts) + [
                types.Part.from_bytes(data=screenshot, mime_type="image/png"),
            ]
            self._contents.append(types.Content(role="user", parts=parts))

    async def _call_llm_inner(self):
        client = self._get_client()
        return await _async_retry_api_call(lambda: asyncio.to_thread(
            client.models.generate_content,
            model=self.MODEL,
            contents=self._contents,
            config=self._gemini_config,
        ))

    def _parse_response(self, response) -> StepResult:
        if not response.candidates:
            # Safety-blocked — conversation is now in a broken state
            # (the user turn we just sent is dangling).  Reset so the
            # next _prepare_step starts fresh.
            self._contents = []
            self._pending_response_parts = []
            return StepResult(actions=[], text="(empty response — likely safety-blocked)")

        candidate = response.candidates[0]
        self._contents.append(candidate.content)

        step_text = ""
        function_calls = []
        for part in candidate.content.parts:
            if hasattr(part, "text") and part.text:
                step_text += part.text
            if hasattr(part, "function_call") and part.function_call:
                function_calls.append(part.function_call)

        if not function_calls:
            # Model is done — clear pending state so the conversation
            # doesn't carry stale function_response parts.
            self._pending_response_parts = []
            return StepResult(actions=[], text=step_text, is_done=True)

        parsed_actions = []
        descs = []
        raw_pairs = []  # (function_call, action_or_none)
        for fc in function_calls:
            action = self._parse_gemini_action(fc)
            desc = f"{fc.name}({dict(fc.args) if fc.args else {}})"
            descs.append(desc)
            raw_pairs.append((fc, action))
            if action:
                parsed_actions.append(action)

        return StepResult(
            actions=parsed_actions,
            text=step_text,
            action_descriptions=descs,
            raw=raw_pairs,
        )

    def _on_api_error(self) -> None:
        self._contents = []
        self._pending_response_parts = []

    async def _execute_step(self, step: int, result: StepResult) -> None:
        from google.genai import types
        self._pending_response_parts = []
        for fc, action in result.raw:
            if action:
                try:
                    await self.execute_action(action)
                except Exception as e:
                    self._live_errors.append(f"Action error at step {step}: {e}")

            fr_fields = {"url": self._page.url}
            if fc.args and "safety_decision" in fc.args:
                fr_fields["safety_acknowledgement"] = "true"
            self._pending_response_parts.append(
                types.Part.from_function_response(
                    name=fc.name,
                    response=fr_fields,
                )
            )


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
            return {"type": "input", "text": tool_input.get("text", "")}
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

    # -- hooks ---------------------------------------------------------------

    def _init_conversation(self, task: str, server_url: str) -> None:
        self._claude_tools = [
            {
                "type": self.TOOL_VERSION,
                "name": "computer",
                "display_width_px": self.viewport_width,
                "display_height_px": self.viewport_height,
            },
        ]
        self._messages: list[dict] = []
        self._pending_tool_results: list[dict] = []
        self._task = task
        self._server_url_task = server_url

    def _prepare_step(self, step: int, screenshot: bytes) -> None:
        b64 = base64.b64encode(screenshot).decode()
        if step == 0 or not self._pending_tool_results:
            self._messages = [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": (
                                f"You are interacting with a web application at {self._server_url_task}. "
                                f"Your task: {self._task}"
                            ),
                        },
                        {
                            "type": "image",
                            "source": {
                                "type": "base64",
                                "media_type": "image/png",
                                "data": b64,
                            },
                        },
                    ],
                },
            ]
        else:
            # Attach screenshot to last tool result
            self._pending_tool_results[-1]["content"] = [
                {
                    "type": "image",
                    "source": {
                        "type": "base64",
                        "media_type": "image/png",
                        "data": b64,
                    },
                },
            ]
            self._messages.append({"role": "user", "content": list(self._pending_tool_results)})

    async def _call_llm_inner(self):
        client = self._get_client()
        return await _async_retry_api_call(lambda: asyncio.to_thread(
            client.beta.messages.create,
            model=self.MODEL,
            max_tokens=4096,
            tools=self._claude_tools,
            messages=self._messages,
            betas=[self.BETA_FLAG],
        ))

    def _parse_response(self, response) -> StepResult:
        response_content = response.content
        self._messages.append({"role": "assistant", "content": response_content})

        step_text = ""
        tool_uses = []
        for block in response_content:
            if hasattr(block, "text"):
                step_text += block.text
            if block.type == "tool_use":
                tool_uses.append(block)

        if not tool_uses:
            # end_turn without tool calls → definitely done
            return StepResult(
                actions=[],
                text=step_text,
                is_done=(response.stop_reason == "end_turn"),
            )

        parsed_actions = []
        descs = []
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

            if action_name == "screenshot":
                descs.append("screenshot")
                self._pending_tool_results.append({
                    "type": "tool_result",
                    "tool_use_id": tu.id,
                    "content": [],
                })
                continue

            action = self._parse_claude_action(tool_input)
            desc = f"{action_name}({tool_input})"
            descs.append(desc)
            if action:
                parsed_actions.append(action)

            self._pending_tool_results.append({
                "type": "tool_result",
                "tool_use_id": tu.id,
                "content": [],
            })

        return StepResult(
            actions=parsed_actions,
            text=step_text,
            is_done=(response.stop_reason != "tool_use"),
            action_descriptions=descs,
        )



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

    def __init__(self, *, max_steps: int = 50, timeout: int = 500, headless: bool = True, **_kw):
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

    async def _call_api(self, messages: list[dict]) -> dict:
        client = self._get_client()

        for attempt in range(3):
            try:
                response = await asyncio.to_thread(
                    client.chat.completions.create,
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
                if attempt < 2:
                    await asyncio.sleep(3)
                    continue
                raise RuntimeError("Kimi API did not finish properly")
            except Exception as e:
                if attempt < 2 and "timeout" in str(e).lower():
                    await asyncio.sleep(3)
                    continue
                if attempt >= 2:
                    raise
                await asyncio.sleep(3)

        raise RuntimeError("Kimi API max retries exceeded")

    # -- response parsing ----------------------------------------------------

    @staticmethod
    def _parse_kimi_response(response: dict) -> tuple[str, str, list[dict]]:
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

    # Parameter order for pyautogui functions (from official docs / OSWorld ref)
    _PYAUTOGUI_PARAMS: dict[str, list[str]] = {
        "click":       ["x", "y", "clicks", "interval", "button", "duration", "pause"],
        "leftClick":   ["x", "y", "duration", "tween", "pause"],
        "rightClick":  ["x", "y", "duration", "tween", "pause"],
        "middleClick": ["x", "y", "duration", "tween", "pause"],
        "doubleClick": ["x", "y", "interval", "button", "duration", "pause"],
        "tripleClick": ["x", "y", "interval", "button", "duration", "pause"],
        "moveTo":      ["x", "y", "duration", "tween", "pause"],
        "dragTo":      ["x", "y", "duration", "button", "mouseDownUp", "pause"],
        "scroll":      ["clicks", "x", "y", "pause"],
        "typewrite":   ["message", "interval", "pause"],
        "write":       ["message", "interval", "pause"],
        "press":       ["keys", "presses", "interval", "pause"],
        "hotkey":      [],  # variadic positional
    }

    _KEY_MAP: dict[str, str] = {
        "ctrl": "Control", "alt": "Alt", "shift": "Shift",
        "enter": "Enter", "return": "Enter", "tab": "Tab",
        "delete": "Delete", "backspace": "Backspace",
        "escape": "Escape", "esc": "Escape", "space": " ",
        "up": "ArrowUp", "down": "ArrowDown",
        "left": "ArrowLeft", "right": "ArrowRight",
        "super": "Meta",
    }

    @staticmethod
    def _parse_pyautogui_code(code: str) -> list[dict]:
        """Parse pyautogui calls from *code* into action dicts.

        Uses ``ast.parse`` (same approach as the OSWorld reference) for
        robust handling of keyword args, triple-quoted strings, etc.
        """
        import ast as _ast

        actions: list[dict] = []
        params_map = KimiVisionAgent._PYAUTOGUI_PARAMS
        key_map = KimiVisionAgent._KEY_MAP

        # Match pyautogui.xxx(...) calls — grab the full call for ast
        for match in re.finditer(r"(pyautogui\.(\w+)\([^)]*\))", code, re.DOTALL):
            full_call = match.group(1)
            func_name = match.group(2)

            # Parse with ast for robust arg extraction
            try:
                tree = _ast.parse(full_call.replace("pyautogui.", "_pag_.", 1))
                call_node = tree.body[0].value
                positional = [_ast.literal_eval(a) for a in call_node.args]
                keywords = {
                    kw.arg: _ast.literal_eval(kw.value)
                    for kw in call_node.keywords
                    if kw.arg is not None
                }
            except Exception:
                continue  # skip unparseable calls

            # Merge positional args using the known parameter order
            param_names = params_map.get(func_name, [])
            args: dict = {}
            for i, val in enumerate(positional):
                if func_name == "hotkey":
                    args[i] = val  # variadic — keep numeric keys
                elif i < len(param_names):
                    args[param_names[i]] = val
            args.update(keywords)

            # --- map to action dicts ---
            if func_name in ("click", "leftClick"):
                x, y = float(args.get("x", 0)), float(args.get("y", 0))
                a: dict = {"type": "click", "x": x, "y": y}
                if args.get("button"):
                    a["button"] = str(args["button"])
                actions.append(a)
            elif func_name == "rightClick":
                actions.append({"type": "click", "x": float(args.get("x", 0)),
                                "y": float(args.get("y", 0)), "button": "right"})
            elif func_name == "middleClick":
                actions.append({"type": "click", "x": float(args.get("x", 0)),
                                "y": float(args.get("y", 0)), "button": "middle"})
            elif func_name in ("doubleClick", "tripleClick"):
                actions.append({"type": "double_click", "x": float(args.get("x", 0)),
                                "y": float(args.get("y", 0))})
            elif func_name == "moveTo":
                actions.append({"type": "hover", "x": float(args.get("x", 0)),
                                "y": float(args.get("y", 0))})
            elif func_name in ("typewrite", "write"):
                text = str(args.get("message", ""))
                actions.append({"type": "input", "text": text})
            elif func_name == "hotkey":
                keys = [str(args[i]) for i in sorted(k for k in args if isinstance(k, int))]
                mapped = [key_map.get(k.lower(), k) for k in keys if k]
                if mapped:
                    actions.append({"type": "key", "keys": "+".join(mapped)})
            elif func_name == "press":
                key = str(args.get("keys", args.get(0, "")))
                actions.append({"type": "key", "keys": key_map.get(key.lower(), key)})
            elif func_name == "scroll":
                amount = int(float(args.get("clicks", 3)))
                direction = "down" if amount < 0 else "up"
                a = {"type": "scroll", "direction": direction, "amount": abs(amount)}
                if "x" in args and "y" in args:
                    a["x"] = float(args["x"])
                    a["y"] = float(args["y"])
                actions.append(a)
            elif func_name == "dragTo":
                actions.append({"type": "drag", "x": 0, "y": 0,
                                "dest_x": float(args.get("x", 0)),
                                "dest_y": float(args.get("y", 0))})

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

    # -- hooks ---------------------------------------------------------------

    def _init_conversation(self, task: str, server_url: str) -> None:
        self._instruction_prompt = _KIMI_INSTRUCTION_TEMPLATE.format(instruction=task)
        self._observations: list[bytes] = []
        self._cots: list[dict] = []
        self._max_image_history = 3
        self._current_messages: list[dict] = []

    def _prepare_step(self, step: int, screenshot: bytes) -> None:
        b64 = base64.b64encode(screenshot).decode()
        cots = self._cots
        observations = self._observations
        mih = self._max_image_history

        # Build messages from scratch each turn (OSWorld pattern)
        messages: list[dict] = [
            {"role": "system", "content": _KIMI_SYSTEM_PROMPT},
        ]

        for i in range(len(cots)):
            if i > len(cots) - mih:
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
            elif i == len(cots) - mih:
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

        messages.append({
            "role": "user",
            "content": [
                {
                    "type": "image_url",
                    "image_url": {"url": f"data:image/png;base64,{b64}"},
                },
                {
                    "type": "text",
                    "text": self._instruction_prompt,
                },
            ],
        })

        self._current_messages = messages

    async def _call_llm_inner(self):
        return await _async_retry_api_call(lambda: self._call_api(self._current_messages))

    def _parse_response(self, response) -> StepResult:
        full_content = response.get("content", "").strip()
        thought, action_desc, actions = self._parse_kimi_response(response)

        if not actions:
            return StepResult(actions=[], text=full_content or thought)

        # Check for termination
        if any(a.get("type") == "_terminate" for a in actions):
            status = next(
                (a["status"] for a in actions if a.get("type") == "_terminate"),
                "done",
            )
            return StepResult(
                actions=[{"type": "terminate", "status": status}],
                text=full_content or thought,
                is_done=True,
            )

        # Convert coordinates before returning
        actions = self._convert_relative_coords(actions)

        return StepResult(
            actions=actions,
            text=full_content or thought,
            raw={"thought": thought, "action_desc": action_desc},
        )

    def _on_step_done(self, step: int, result: StepResult, screenshot: bytes) -> None:
        raw = result.raw or {}
        self._observations.append(screenshot)
        self._cots.append({
            "thought": raw.get("thought", result.text),
            "action": raw.get("action_desc", ""),
        })


# ---------------------------------------------------------------------------
# Qwen 3.5 VL Agent
# ---------------------------------------------------------------------------


# System prompt adapted from the OSWorld reference implementation.
_QWEN_TOOLS_DEF = json.dumps({
    "type": "function",
    "function": {
        "name": "computer_use",
        "description": "Use a mouse and keyboard to interact with a web application.",
        "parameters": {
            "type": "object",
            "required": ["action"],
            "properties": {
                "action": {
                    "type": "string",
                    "enum": [
                        "key", "type", "mouse_move",
                        "left_click", "left_click_drag",
                        "right_click", "middle_click",
                        "double_click", "triple_click",
                        "scroll", "wait", "terminate",
                    ],
                },
                "keys": {"type": "array", "description": "Required only by action=key."},
                "text": {"type": "string", "description": "Required by action=type."},
                "coordinate": {"type": "array", "description": "(x, y) pixel coordinate."},
                "pixels": {"type": "number", "description": "Scroll amount in pixels."},
                "time": {"type": "number", "description": "Seconds to wait."},
                "status": {
                    "type": "string",
                    "description": "Task status for terminate.",
                    "enum": ["success", "failure"],
                },
            },
        },
    },
})

_QWEN_SYSTEM_PROMPT = (
    "You are a multi-purpose intelligent assistant. Based on my requests, "
    "you can use tools to help me complete various tasks.\n\n"
    "# Tools\n\n"
    "You have access to the following functions:\n\n"
    "<tools>\n" + _QWEN_TOOLS_DEF + "\n</tools>\n\n"
    "If you choose to call a function ONLY reply in the following format with NO suffix:\n\n"
    "<tool_call>\n"
    "<function=example_function_name>\n"
    "<parameter=example_parameter_1>\n"
    "value_1\n"
    "</parameter>\n"
    "<parameter=example_parameter_2>\n"
    "This is the value for the second parameter\n"
    "that can span\n"
    "multiple lines\n"
    "</parameter>\n"
    "</function>\n"
    "</tool_call>\n\n"
    "<IMPORTANT>\n"
    "Reminder:\n"
    "- Function calls MUST follow the specified format: an inner "
    "<function=...></function> block must be nested within "
    "<tool_call></tool_call> XML tags\n"
    "- Required parameters MUST be specified\n"
    "- You may provide optional reasoning for your function call in "
    "natural language BEFORE the function call, but NOT after\n"
    "</IMPORTANT>\n\n"
    "# Response format\n\n"
    "Response format for every step:\n"
    "1) Action: a short imperative describing what to do in the UI.\n"
    "2) A single <tool_call>...</tool_call> block.\n\n"
    "Rules:\n"
    "- Output exactly in the order: Action, <tool_call>.\n"
    "- Be brief: one sentence for Action.\n"
    "- Do not output anything else outside those parts.\n"
    "- If finishing, use action=terminate in the tool call.\n"
    "- The screen's resolution is 1000x1000."
)

_QWEN_COLLAPSED_TEXT = "This screenshot has been collapsed."


class Qwen35VLAgent(VisionAgentBase):
    """Agent using Qwen 3.5 VL via an OpenAI-compatible API.

    Uses XML tool-call output format with 0-999 normalised coordinates.
    Requires ``openai`` package and ``QWEN_API_KEY`` / ``QWEN_BASE_URL``
    environment variables.
    """

    MODEL = "qwen3.5-plus"
    BASE_URL = "https://dashscope-intl.aliyuncs.com/compatible-mode/v1"

    def __init__(
        self,
        *,
        max_steps: int = 50,
        timeout: int = 500,
        headless: bool = True,
        model: str | None = None,
        image_max: int = 20,
        fold_size: int = 10,
        history_n: int = 100,
        **_kw,
    ):
        super().__init__(
            viewport_width=1920,
            viewport_height=1080,
            max_steps=max_steps,
            timeout=timeout,
            headless=headless,
        )
        if model:
            self.MODEL = model
        self._client = None
        self._image_max = image_max
        self._fold_size = fold_size
        self._history_n = history_n

    def _get_client(self):
        if self._client is None:
            from openai import OpenAI
            api_key = os.environ.get("DASHSCOPE_API_KEY", "")
            if not api_key:
                raise RuntimeError("DASHSCOPE_API_KEY environment variable not set")
            self._client = OpenAI(api_key=api_key, base_url=self.BASE_URL)
        return self._client

    # -- coordinate conversion -----------------------------------------------

    def _qwen_to_pixel(self, x: float, y: float) -> tuple[int, int]:
        """Convert Qwen's 0-999 normalised coords to viewport pixels."""
        px = int(x * self.viewport_width / 999)
        py = int(y * self.viewport_height / 999)
        return px, py

    # -- XML tool-call parsing -----------------------------------------------

    @staticmethod
    def _parse_xml_tool_call(xml: str) -> dict | None:
        """Parse a ``<function=computer_use>`` XML block into a param dict."""
        func_match = re.search(r"<function=([^>]+)>", xml)
        if not func_match or func_match.group(1) != "computer_use":
            return None
        params: dict = {}
        for m in re.finditer(
            r"<parameter=([^>]+)>\s*(.*?)\s*</parameter>", xml, re.DOTALL
        ):
            name, value = m.group(1), m.group(2).strip()
            if value.startswith("[") or value.startswith("{"):
                try:
                    params[name] = json.loads(value)
                    continue
                except json.JSONDecodeError:
                    pass
            params[name] = value
        return params

    def _tool_params_to_actions(self, params: dict) -> list[dict]:
        """Convert parsed XML tool-call params into action dicts."""
        action = params.get("action", "")
        coord = None
        raw_coord = params.get("coordinate")
        if isinstance(raw_coord, str):
            try:
                raw_coord = json.loads(raw_coord)
            except json.JSONDecodeError:
                raw_coord = None
        if isinstance(raw_coord, list) and len(raw_coord) >= 2:
            coord = self._qwen_to_pixel(float(raw_coord[0]), float(raw_coord[1]))

        actions: list[dict] = []

        if action == "left_click":
            if coord:
                actions.append({"type": "click", "x": coord[0], "y": coord[1]})
        elif action == "right_click":
            if coord:
                actions.append({"type": "click", "x": coord[0], "y": coord[1], "button": "right"})
        elif action == "middle_click":
            if coord:
                actions.append({"type": "click", "x": coord[0], "y": coord[1], "button": "middle"})
        elif action in ("double_click", "triple_click"):
            if coord:
                actions.append({"type": "double_click", "x": coord[0], "y": coord[1]})
        elif action == "mouse_move":
            if coord:
                actions.append({"type": "hover", "x": coord[0], "y": coord[1]})
        elif action == "left_click_drag":
            if coord:
                actions.append({"type": "drag", "x": 0, "y": 0,
                                "dest_x": coord[0], "dest_y": coord[1]})
        elif action == "type":
            text = params.get("text", "")
            actions.append({"type": "input", "text": str(text)})
        elif action == "key":
            raw_keys = params.get("keys", [])
            if isinstance(raw_keys, str):
                try:
                    raw_keys = json.loads(raw_keys)
                except json.JSONDecodeError:
                    raw_keys = [raw_keys]
            if isinstance(raw_keys, list):
                keys = [str(k).strip() for k in raw_keys]
            else:
                keys = [str(raw_keys).strip()]
            if len(keys) > 1:
                actions.append({"type": "key", "keys": "+".join(keys)})
            elif keys:
                actions.append({"type": "key", "keys": keys[0]})
        elif action in ("scroll", "hscroll"):
            pixels = 0
            try:
                pixels = int(float(params.get("pixels", 0)))
            except (ValueError, TypeError):
                pass
            direction = "down" if pixels < 0 else "up"
            a: dict = {"type": "scroll", "direction": direction,
                       "amount": max(1, abs(pixels) // 100)}
            if coord:
                a["x"] = coord[0]
                a["y"] = coord[1]
            actions.append(a)
        elif action == "wait":
            secs = 5
            try:
                secs = int(float(params.get("time", 5)))
            except (ValueError, TypeError):
                pass
            actions.append({"type": "wait", "seconds": secs})
        elif action == "terminate":
            status = params.get("status", "success")
            actions.append({"type": "terminate", "status": status})

        return actions

    # -- hooks ---------------------------------------------------------------

    def _init_conversation(self, task: str, server_url: str) -> None:
        self._task = task
        self._server_url_task = server_url
        self._screenshots_b64: list[str] = []
        self._responses: list[str] = []
        self._action_summaries: list[str] = []
        self._folded_prefix_k = 0
        self._current_messages: list[dict] = []

    def _prepare_step(self, step: int, screenshot: bytes) -> None:
        b64 = base64.b64encode(screenshot).decode()
        self._screenshots_b64.append(b64)
        total = len(self._screenshots_b64)

        # Update folding state (same logic as reference)
        while (total - self._folded_prefix_k) > self._image_max:
            self._folded_prefix_k += self._fold_size
        if self._folded_prefix_k > total:
            self._folded_prefix_k = total

        # Truncate history to last history_n steps (matching reference)
        start_step = max(1, total - self._history_n)

        # Build "previous actions" summary for older steps not in message window
        prev = [
            f"Step {i + 1}: {self._action_summaries[i]}"
            for i in range(min(step, len(self._action_summaries)))
        ]
        prev_str = "\n".join(prev) if prev else "None"

        instruction_prompt = (
            f"\nPlease generate the next move according to the UI screenshot, "
            f"instruction and previous actions.\n\n"
            f"Instruction: You are interacting with a web application at "
            f"{self._server_url_task}. {self._task}\n\n"
            f"Previous actions:\n{prev_str}"
        )

        messages: list[dict] = [
            {"role": "system", "content": [{"type": "text", "text": _QWEN_SYSTEM_PROMPT}]},
        ]

        for s in range(start_step, total + 1):
            is_first = (s == start_step)
            is_collapsed = (s <= self._folded_prefix_k)

            if is_collapsed:
                if is_first:
                    user_content = [{"type": "text", "text": instruction_prompt}]
                else:
                    user_content = [
                        {"type": "text", "text": "<tool_response>\n"},
                        {"type": "text", "text": _QWEN_COLLAPSED_TEXT},
                        {"type": "text", "text": "\n</tool_response>"},
                    ]
            else:
                img_url = f"data:image/png;base64,{self._screenshots_b64[s - 1]}"
                if is_first:
                    user_content = [
                        {"type": "image_url", "image_url": {"url": img_url}},
                        {"type": "text", "text": instruction_prompt},
                    ]
                else:
                    user_content = [
                        {"type": "text", "text": "<tool_response>\n"},
                        {"type": "image_url", "image_url": {"url": img_url}},
                        {"type": "text", "text": "\n</tool_response>"},
                    ]

            messages.append({"role": "user", "content": user_content})

            # Add assistant response for past steps (not the current one)
            if s <= total - 1 and (s - 1) < len(self._responses):
                messages.append({
                    "role": "assistant",
                    "content": [{"type": "text", "text": self._responses[s - 1]}],
                })

        self._current_messages = messages

    async def _call_api(self, messages: list[dict]) -> dict:
        client = self._get_client()

        for attempt in range(3):
            try:
                response = await asyncio.to_thread(
                    client.chat.completions.create,
                    model=self.MODEL,
                    messages=messages,
                    max_tokens=32768,
                    top_p=0.9,
                    temperature=0.0,
                )
                choice = response.choices[0]
                if choice.finish_reason == "stop":
                    msg = choice.message
                    return {
                        "content": msg.content or "",
                    }
                if attempt < 2:
                    await asyncio.sleep(3)
                    continue
                raise RuntimeError("Qwen API did not finish properly")
            except Exception as e:
                if attempt < 2 and "timeout" in str(e).lower():
                    await asyncio.sleep(3)
                    continue
                if attempt >= 2:
                    raise
                await asyncio.sleep(3)

        raise RuntimeError("Qwen API max retries exceeded")

    async def _call_llm_inner(self):
        return await _async_retry_api_call(lambda: self._call_api(self._current_messages))

    def _parse_response(self, response) -> StepResult:
        # Extract text content from response
        content = response.get("content", "")
        if isinstance(content, list):
            content = "".join(
                p.get("text", "") if isinstance(p, dict) else getattr(p, "text", "")
                for p in content
            )

        # Store raw response for history replay
        self._responses.append(content)

        # Parse XML tool calls
        all_actions: list[dict] = []
        for tc_match in re.finditer(
            r"<tool_call>(.*?)</tool_call>", content, re.DOTALL
        ):
            params = self._parse_xml_tool_call(tc_match.group(1))
            if params:
                all_actions.extend(self._tool_params_to_actions(params))

        # Extract action summary line
        summary = ""
        for line in content.split("\n"):
            stripped = line.strip()
            if stripped.lower().startswith("action:"):
                summary = stripped.split("Action:", 1)[-1].strip()
                break
        self._action_summaries.append(summary or "action")

        if not all_actions:
            return StepResult(actions=[], text=content)

        # Check for termination
        if any(a.get("type") == "terminate" for a in all_actions):
            status = next(
                (a["status"] for a in all_actions if a.get("type") == "terminate"),
                "success",
            )
            return StepResult(
                actions=[{"type": "terminate", "status": status}],
                text=content,
                is_done=True,
            )

        # Filter out wait-only (not a real termination but not executable either)
        return StepResult(actions=all_actions, text=content)


# ---------------------------------------------------------------------------
# Utilities
# ---------------------------------------------------------------------------


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
