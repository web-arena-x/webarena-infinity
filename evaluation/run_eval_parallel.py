#!/usr/bin/env python3
"""
Parallel evaluation runner with worker pool.

Each worker gets a dedicated environment instance (server port) and pulls
tasks from a shared queue.  Supports local servers (auto-started per worker)
or remote env hosts (pre-running servers).

Usage:
    # Local — 4 workers, auto-starts servers on ports 8001-8004
    python evaluation/run_eval_parallel.py --model gpt --workers 4

    # Remote env host — agents connect to pre-running servers
    python evaluation/run_eval_parallel.py --model gpt --workers 8 \\
        --env-host ec2-host --base-port 8001

    # Filter tasks
    python evaluation/run_eval_parallel.py --model claude --difficulty easy --workers 2
"""

import argparse
import asyncio
import json
import os
import sys
from datetime import datetime
from pathlib import Path

# Ensure sibling modules are importable when run as `python evaluation/run_eval_parallel.py`
sys.path.insert(0, str(Path(__file__).resolve().parent))

from dotenv import load_dotenv

from browser_use.llm.anthropic.chat import ChatAnthropic
from browser_use.llm.google.chat import ChatGoogle
from browser_use.llm.openai.chat import ChatOpenAI

from agents import BrowserUseAgent
from report import generate_report
from server import start_server, stop_server, wait_for_server
from tasks import (
    TASK_TIMEOUT,
    filter_tasks,
    load_tasks,
    run_task,
)

load_dotenv()

MODELS = {
    "gpt": lambda: ChatOpenAI(model="gpt-4o"),
    "gemini": lambda: ChatGoogle(model="gemini-2.0-flash"),
    "claude": lambda: ChatAnthropic(model="claude-sonnet-4-5-20250929"),
}

# --- ANSI colors ---
BOLD = "\033[1m"
DIM = "\033[2m"
RESET = "\033[0m"
GREEN = "\033[32m"
RED = "\033[31m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
MAGENTA = "\033[35m"
WHITE = "\033[97m"
BG_GREEN = "\033[42m"
BG_RED = "\033[41m"
BG_YELLOW = "\033[43m"

DIFF_COLOR = {"easy": GREEN, "medium": YELLOW, "hard": RED}


async def worker(
    worker_id: int,
    task_queue: asyncio.Queue,
    results: list,
    results_lock: asyncio.Lock,
    *,
    model_factory,
    web_app_dir: str,
    run_dir: Path,
    env_host: str,
    port: int,
    use_vision: bool,
    max_steps: int,
):
    """A single evaluation worker.

    Manages its own server (if local) and agent.  Pulls tasks from the shared
    queue until it is empty.
    """
    server_proc = None
    is_local = env_host in ("localhost", "127.0.0.1")
    server_url = f"http://{env_host}:{port}"
    tag = f"{DIM}[W{worker_id}]{RESET}"

    # Start local server if needed
    if is_local:
        server_proc = start_server(web_app_dir, port)
        if not wait_for_server(port, host=env_host):
            if server_proc:
                stop_server(server_proc)
            print(f"  {tag} {RED}Server failed to start on port {port}{RESET}")
            return

    llm = model_factory()
    agent = BrowserUseAgent(
        llm,
        use_vision=use_vision,
        max_steps=max_steps,
        timeout=TASK_TIMEOUT,
    )

    try:
        await agent.setup(server_url)
        print(f"  {tag} ready on :{port}")

        while True:
            try:
                task = task_queue.get_nowait()
            except asyncio.QueueEmpty:
                break

            task_id = task["id"]
            diff = task["difficulty"]
            dc = DIFF_COLOR.get(diff, "")
            task_dir = run_dir / task_id
            task_dir.mkdir(parents=True, exist_ok=True)

            try:
                result = await run_task(
                    task=task,
                    agent_runner=agent,
                    server_url=server_url,
                    web_app_dir=web_app_dir,
                    task_dir=task_dir,
                )
                status_badge = (
                    f"{BG_GREEN}{WHITE}{BOLD} PASS {RESET}"
                    if result["passed"]
                    else f"{BG_RED}{WHITE}{BOLD} FAIL {RESET}"
                )
                print(
                    f"  {tag} {BOLD}{task_id}{RESET} {dc}{diff}{RESET}  "
                    f"{status_badge} {DIM}{result['elapsed']}s  {result['steps']} steps{RESET}"
                )
            except asyncio.TimeoutError:
                print(f"  {tag} {BOLD}{task_id}{RESET} {dc}{diff}{RESET}  {BG_YELLOW}{WHITE}{BOLD} TIME {RESET}")
                result = {
                    "task_id": task_id,
                    "difficulty": task["difficulty"],
                    "instruction": task["instruction"],
                    "passed": False,
                    "verifier_message": f"Timed out after {TASK_TIMEOUT}s",
                    "elapsed": TASK_TIMEOUT,
                    "steps": -1,
                    "is_done": False,
                    "final_result": None,
                    "errors": [f"Timeout after {TASK_TIMEOUT}s"],
                }
                with open(task_dir / "result.json", "w") as f:
                    json.dump(result, f, indent=2)
            except Exception as e:
                print(f"  {tag} {BOLD}{task_id}{RESET} {dc}{diff}{RESET}  {BG_RED}{WHITE}{BOLD} ERR  {RESET} {DIM}{e}{RESET}")
                result = {
                    "task_id": task_id,
                    "difficulty": task["difficulty"],
                    "instruction": task["instruction"],
                    "passed": False,
                    "verifier_message": f"Agent crashed: {e}",
                    "elapsed": 0,
                    "steps": -1,
                    "is_done": False,
                    "final_result": None,
                    "errors": [str(e)],
                }
                with open(task_dir / "result.json", "w") as f:
                    json.dump(result, f, indent=2)

            async with results_lock:
                results.append(result)

    finally:
        await agent.teardown()
        if server_proc:
            stop_server(server_proc)


async def main():
    parser = argparse.ArgumentParser(
        description="Parallel evaluation runner with worker pool"
    )
    parser.add_argument("--model", choices=MODELS.keys(), default="gpt")
    parser.add_argument("--task-id", default=None, help="Run a single task (e.g. task_e1)")
    parser.add_argument("--difficulty", choices=["easy", "medium", "hard"], default=None)
    parser.add_argument("--max-steps", type=int, default=50)
    parser.add_argument("--use-vision", action="store_true", help="Enable vision for the agent")
    parser.add_argument("--workers", type=int, default=4, help="Number of parallel workers")
    parser.add_argument("--base-port", type=int, default=8001, help="First port for env instances")
    parser.add_argument(
        "--env-host",
        default="localhost",
        help="Hostname of environment servers (localhost = auto-start)",
    )
    parser.add_argument("--output-dir", default=None,
                        help="Results directory (default: <web-app>/results)")
    parser.add_argument("--web-app", default="apps/gitlab-org-management")
    args = parser.parse_args()

    web_app_dir = str(Path(args.web_app).resolve())
    output_dir = args.output_dir or os.path.join(web_app_dir, "results")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    run_dir = Path(output_dir) / f"{args.model}_{timestamp}_parallel"
    run_dir.mkdir(parents=True, exist_ok=True)

    # Load and filter tasks
    all_tasks = load_tasks(web_app_dir)
    tasks = filter_tasks(all_tasks, task_id=args.task_id, difficulty=args.difficulty)
    if not tasks:
        print(f"{RED}No tasks matched.{RESET}")
        sys.exit(1)

    num_workers = min(args.workers, len(tasks))
    port_hi = args.base_port + num_workers - 1

    # Header
    print(f"\n{BOLD}{CYAN}{'=' * 60}{RESET}")
    print(f"{BOLD}{CYAN}  Parallel Evaluation{RESET}")
    print(f"{BOLD}{CYAN}{'=' * 60}{RESET}")
    print(f"  {DIM}Model:{RESET}   {BOLD}{args.model}{RESET}")
    print(f"  {DIM}Tasks:{RESET}   {BOLD}{len(tasks)}{RESET}")
    print(f"  {DIM}Workers:{RESET} {BOLD}{num_workers}{RESET}")
    print(f"  {DIM}Env:{RESET}     {BOLD}{args.env_host}:{args.base_port}-{port_hi}{RESET}")
    print(f"  {DIM}Vision:{RESET}  {BOLD}{'on' if args.use_vision else 'off'}{RESET}")
    print(f"  {DIM}Output:{RESET}  {run_dir}")
    print(f"{CYAN}{'─' * 60}{RESET}\n")

    # Build task queue
    task_queue: asyncio.Queue = asyncio.Queue()
    for t in tasks:
        await task_queue.put(t)

    results: list[dict] = []
    results_lock = asyncio.Lock()

    # Launch workers concurrently
    worker_coros = [
        worker(
            worker_id=i,
            task_queue=task_queue,
            results=results,
            results_lock=results_lock,
            model_factory=MODELS[args.model],
            web_app_dir=web_app_dir,
            run_dir=run_dir,
            env_host=args.env_host,
            port=args.base_port + i,
            use_vision=args.use_vision,
            max_steps=args.max_steps,
        )
        for i in range(num_workers)
    ]
    await asyncio.gather(*worker_coros)

    if not results:
        print(f"{RED}No tasks completed.{RESET}")
        sys.exit(1)

    # Sort results by task_id for consistent ordering
    results.sort(key=lambda r: r["task_id"])

    # Aggregate
    total = len(results)
    passed = sum(1 for r in results if r["passed"])
    by_diff: dict[str, dict] = {}
    for r in results:
        d = r["difficulty"]
        by_diff.setdefault(d, {"total": 0, "passed": 0})
        by_diff[d]["total"] += 1
        if r["passed"]:
            by_diff[d]["passed"] += 1

    aggregate = {
        "model": args.model,
        "timestamp": timestamp,
        "use_vision": args.use_vision,
        "workers": num_workers,
        "total": total,
        "passed": passed,
        "pass_rate": round(passed / total * 100, 1) if total else 0,
        "by_difficulty": by_diff,
        "tasks": results,
    }
    with open(run_dir / "results.json", "w") as f:
        json.dump(aggregate, f, indent=2)

    # HTML report
    report_path = generate_report(results, args.model, timestamp, run_dir)

    # Console summary
    pct = aggregate["pass_rate"]
    pct_color = GREEN if pct >= 50 else RED
    print(f"\n{BOLD}{CYAN}{'=' * 60}{RESET}")
    print(f"  {BOLD}Results: {pct_color}{passed}/{total} passed ({pct}%){RESET}")
    print()
    for d in ["easy", "medium", "hard"]:
        if d in by_diff:
            info = by_diff[d]
            dc = DIFF_COLOR.get(d, "")
            ratio_color = GREEN if info["passed"] == info["total"] else (YELLOW if info["passed"] > 0 else RED)
            print(f"    {dc}{d.capitalize():8s}{RESET} {ratio_color}{info['passed']}/{info['total']}{RESET}")
    print()
    print(f"  {DIM}Report:{RESET} {MAGENTA}{report_path}{RESET}")
    print(f"{CYAN}{'=' * 60}{RESET}\n")


if __name__ == "__main__":
    asyncio.run(main())
