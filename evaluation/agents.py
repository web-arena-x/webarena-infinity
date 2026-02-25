"""Pluggable agent interface and built-in implementations.

AgentRunner is the protocol every agent must satisfy.  The evaluation harness
only calls this interface — it never touches browser-use (or any other library)
directly.

Built-in implementations:
  - BrowserUseAgent: wraps the browser-use library.
"""

from __future__ import annotations

import asyncio
import shutil
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Protocol, runtime_checkable

import requests


# ---------------------------------------------------------------------------
# Data
# ---------------------------------------------------------------------------


@dataclass
class AgentResult:
    """Result returned by an agent after running a single task."""

    elapsed: float
    steps: int
    is_done: bool
    final_result: str | None
    errors: list[str] = field(default_factory=list)


# ---------------------------------------------------------------------------
# Protocol
# ---------------------------------------------------------------------------


@runtime_checkable
class AgentRunner(Protocol):
    """Interface that every agent implementation must satisfy."""

    async def setup(self, server_url: str) -> None:
        """One-time setup before running tasks (e.g. start browser, seed state)."""
        ...

    async def run(self, task: str, server_url: str, task_dir: Path) -> AgentResult:
        """Execute a single task.  Save trajectory artifacts to *task_dir*."""
        ...

    async def teardown(self) -> None:
        """Release resources (e.g. close browser)."""
        ...


# ---------------------------------------------------------------------------
# browser-use implementation
# ---------------------------------------------------------------------------


class BrowserUseAgent:
    """AgentRunner backed by the *browser-use* library."""

    def __init__(
        self,
        llm,
        *,
        use_vision: bool = False,
        max_steps: int = 50,
        timeout: int = 300,
        headless: bool = True,
    ):
        self.llm = llm
        self.use_vision = use_vision
        self.max_steps = max_steps
        self.timeout = timeout
        self.headless = headless
        self._session = None  # lazily created in setup()

    # -- lifecycle -----------------------------------------------------------

    async def setup(self, server_url: str) -> None:
        """Start a persistent browser session and capture the seed state."""
        from browser_use import BrowserSession

        self._session = BrowserSession(
            headless=self.headless, keep_alive=True
        )
        await self._session.start()

        page = await self._session.get_current_page()
        await page.goto(server_url)

        # Poll for the browser JS to push state via PUT /api/state
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

    async def run(self, task: str, server_url: str, task_dir: Path) -> AgentResult:
        """Run a single task using the browser-use Agent."""
        from browser_use import Agent

        instruction = (
            f"You are interacting with a web application at {server_url}. "
            f"Your task: {task}"
        )

        agent = Agent(
            task=instruction,
            llm=self.llm,
            browser_session=self._session,
            use_vision=self.use_vision,
            save_conversation_path=str(task_dir / "conversations"),
            max_steps=self.max_steps,
        )

        t0 = time.time()
        history = await asyncio.wait_for(agent.run(), timeout=self.timeout)
        elapsed = time.time() - t0

        # Save trajectory
        history.save_to_file(task_dir / "history.json")
        screenshots_dst = task_dir / "screenshots"
        for step_idx, path_str in enumerate(history.screenshot_paths()):
            if path_str and Path(path_str).exists():
                screenshots_dst.mkdir(parents=True, exist_ok=True)
                shutil.copy2(path_str, screenshots_dst / f"step_{step_idx}.png")

        return AgentResult(
            elapsed=round(elapsed, 1),
            steps=len(history.history),
            is_done=history.is_done(),
            final_result=history.final_result(),
            errors=history.errors(),
        )

    async def teardown(self) -> None:
        if self._session:
            try:
                await self._session.kill()
            except Exception:
                pass
            self._session = None
