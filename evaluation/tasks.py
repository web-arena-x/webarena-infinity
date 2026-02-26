"""Task loading, filtering, verification, and single-task execution."""

import importlib.util
import json
import time
from pathlib import Path

import requests

from agents import AgentResult

TASK_TIMEOUT = 300  # seconds per task wall-clock limit


def load_tasks(web_app_dir: str, task_suite: str = "tasks") -> list[dict]:
    with open(Path(web_app_dir) / f"{task_suite}.json") as f:
        return json.load(f)


def filter_tasks(
    tasks: list[dict],
    task_id: str | None = None,
    difficulty: str | None = None,
) -> list[dict]:
    if task_id:
        return [t for t in tasks if t["id"] == task_id]
    if difficulty:
        return [t for t in tasks if t["difficulty"] == difficulty]
    return tasks


def load_verifier(web_app_dir: str, verify_path: str):
    full_path = str(Path(web_app_dir) / verify_path)
    spec = importlib.util.spec_from_file_location("verifier", full_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.verify


def reset_state(server_url: str):
    resp = requests.post(f"{server_url}/api/reset")
    resp.raise_for_status()
    time.sleep(0.5)


async def run_task(
    task: dict,
    agent_runner,
    server_url: str,
    web_app_dir: str,
    task_dir: Path,
) -> dict:
    """Reset state, run the agent, verify, return result dict."""
    task_id = task["id"]

    # 1. Reset
    reset_state(server_url)

    # 2. Run agent
    result: AgentResult = await agent_runner.run(
        task=task["instruction"],
        server_url=server_url,
        task_dir=task_dir,
    )

    # 3. Verify
    try:
        verify_fn = load_verifier(web_app_dir, task["verify"])
        passed, verifier_message = verify_fn(server_url)
    except Exception as e:
        passed, verifier_message = False, f"Verifier exception: {e}"

    task_result = {
        "task_id": task_id,
        "difficulty": task["difficulty"],
        "instruction": task["instruction"],
        "passed": passed,
        "verifier_message": verifier_message,
        "elapsed": result.elapsed,
        "steps": result.steps,
        "is_done": result.is_done,
        "final_result": result.final_result,
        "errors": result.errors,
    }

    with open(task_dir / "result.json", "w") as f:
        json.dump(task_result, f, indent=2)

    return task_result
