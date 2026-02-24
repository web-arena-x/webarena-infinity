#!/usr/bin/env python3
"""
Evaluation harness for browser-use agent on GitLab org management tasks.

Orchestrates: server lifecycle -> task loop (reset -> agent -> verify) ->
trajectory storage -> HTML report.

Usage:
    python evaluation/run_eval.py --model gemini --task-id task_e1
    python evaluation/run_eval.py --model gemini --difficulty easy
    python evaluation/run_eval.py --model gpt --use-vision
"""

import argparse
import asyncio
import json
import os
import signal
import sys
from datetime import datetime
from pathlib import Path

# Ensure sibling modules are importable when run as `python evaluation/run_eval.py`
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

# --- ANSI colors (no dependencies) ---
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


async def main():
    parser = argparse.ArgumentParser(
        description="Evaluation harness for browser-use agent"
    )
    parser.add_argument("--model", choices=MODELS.keys(), default="gpt")
    parser.add_argument(
        "--task-id", default=None, help="Run a single task (e.g. task_e1)"
    )
    parser.add_argument(
        "--difficulty", choices=["easy", "medium", "hard"], default=None
    )
    parser.add_argument("--max-steps", type=int, default=50)
    parser.add_argument(
        "--use-vision", action="store_true", help="Enable vision for the agent"
    )
    parser.add_argument("--port", type=int, default=8000)
    parser.add_argument("--output-dir", default=None,
                        help="Results directory (default: <web-app>/results)")
    parser.add_argument("--web-app", default="apps/gitlab-org-management")
    args = parser.parse_args()

    web_app_dir = str(Path(args.web_app).resolve())
    output_dir = args.output_dir or os.path.join(web_app_dir, "results")
    server_url = f"http://localhost:{args.port}"
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    run_dir = Path(output_dir) / f"{args.model}_{timestamp}"
    run_dir.mkdir(parents=True, exist_ok=True)

    # Load and filter tasks
    all_tasks = load_tasks(web_app_dir)
    tasks = filter_tasks(all_tasks, task_id=args.task_id, difficulty=args.difficulty)
    if not tasks:
        print(f"{RED}No tasks matched (task-id={args.task_id}, difficulty={args.difficulty}){RESET}")
        sys.exit(1)

    # Header
    print(f"\n{BOLD}{CYAN}{'=' * 60}{RESET}")
    print(f"{BOLD}{CYAN}  Evaluation Harness{RESET}")
    print(f"{BOLD}{CYAN}{'=' * 60}{RESET}")
    print(f"  {DIM}Model:{RESET}  {BOLD}{args.model}{RESET}")
    print(f"  {DIM}Tasks:{RESET}  {BOLD}{len(tasks)}{RESET}")
    print(f"  {DIM}Vision:{RESET} {BOLD}{'on' if args.use_vision else 'off'}{RESET}")
    print(f"  {DIM}Output:{RESET} {run_dir}")
    print(f"{CYAN}{'─' * 60}{RESET}\n")

    # Start server
    print(f"  {DIM}Starting server on port {args.port}...{RESET}", end=" ", flush=True)
    server_proc = start_server(web_app_dir, args.port)
    if not wait_for_server(args.port):
        stop_server(server_proc)
        print(f"{RED}FAILED{RESET}")
        print(f"{RED}ERROR: Server failed to start within timeout.{RESET}")
        sys.exit(1)
    print(f"{GREEN}ready{RESET}")

    results: list[dict] = []
    interrupted = False

    def on_sigint(sig, frame):
        nonlocal interrupted
        interrupted = True
        print(f"\n\n{YELLOW}Interrupted! Generating report for completed tasks...{RESET}")

    original_sigint = signal.getsignal(signal.SIGINT)
    signal.signal(signal.SIGINT, on_sigint)

    try:
        llm = MODELS[args.model]()
        agent = BrowserUseAgent(
            llm,
            use_vision=args.use_vision,
            max_steps=args.max_steps,
            timeout=TASK_TIMEOUT,
        )

        # Seed first load
        print(f"  {DIM}Capturing seed state...{RESET}", end=" ", flush=True)
        await agent.setup(server_url)
        print(f"{GREEN}done{RESET}\n")

        total = len(tasks)
        for idx, task in enumerate(tasks, 1):
            if interrupted:
                break

            task_id = task["id"]
            task_dir = run_dir / task_id
            task_dir.mkdir(parents=True, exist_ok=True)

            diff = task["difficulty"]
            dc = DIFF_COLOR.get(diff, "")
            counter = f"{DIM}[{idx}/{total}]{RESET}"
            print(f"  {counter} {BOLD}{task_id}{RESET} {dc}{diff}{RESET}", end="  ", flush=True)

            try:
                result = await run_task(
                    task=task,
                    agent_runner=agent,
                    server_url=server_url,
                    web_app_dir=web_app_dir,
                    task_dir=task_dir,
                )
                if result["passed"]:
                    print(f"{BG_GREEN}{WHITE}{BOLD} PASS {RESET} {DIM}{result['elapsed']}s  {result['steps']} steps{RESET}")
                else:
                    print(f"{BG_RED}{WHITE}{BOLD} FAIL {RESET} {DIM}{result['elapsed']}s  {result['steps']} steps{RESET}")
                results.append(result)
            except asyncio.TimeoutError:
                print(f"{BG_YELLOW}{WHITE}{BOLD} TIME {RESET} {DIM}{TASK_TIMEOUT}s{RESET}")
                result = {
                    "task_id": task_id,
                    "difficulty": task["difficulty"],
                    "instruction": task["instruction"],
                    "passed": False,
                    "verifier_message": f"Task timed out after {TASK_TIMEOUT}s",
                    "elapsed": TASK_TIMEOUT,
                    "steps": -1,
                    "is_done": False,
                    "final_result": None,
                    "errors": [f"Timeout after {TASK_TIMEOUT}s"],
                }
                with open(task_dir / "result.json", "w") as f:
                    json.dump(result, f, indent=2)
                results.append(result)
            except Exception as e:
                print(f"{BG_RED}{WHITE}{BOLD} ERR  {RESET} {DIM}{e}{RESET}")
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
                results.append(result)

        # Close browser
        await agent.teardown()

    finally:
        signal.signal(signal.SIGINT, original_sigint)
        stop_server(server_proc)

    if not results:
        print(f"{RED}No tasks completed.{RESET}")
        sys.exit(1)

    # Aggregate results
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
