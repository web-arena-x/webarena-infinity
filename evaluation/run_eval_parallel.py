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

    # Multi-run: repeat full task set 3 times
    python evaluation/run_eval_parallel.py --model gemini --repetitions 3 --workers 4

    # Multi-run cascading: run all, retry failures, retry remaining failures
    python evaluation/run_eval_parallel.py --model gemini --repetitions 3 --failed-only --workers 4
"""

import argparse
import asyncio
import json
import os
import shutil
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
    "gemini": lambda: ChatGoogle(model="gemini-3-flash-preview"),
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


# ---------------------------------------------------------------------------
# Multi-run helpers
# ---------------------------------------------------------------------------


def merge_repetition_results(
    run_dirs: list[Path],
    merged_dir: Path,
    model: str,
    timestamp: str,
    use_vision: bool,
    num_workers: int,
):
    """Merge results from multiple repetitions into success/ and fail/ folders.

    A task is considered successful if it passed in ANY repetition.
    For success: copies the first passing run's task directory.
    For fail: copies the last run's task directory.
    """
    merged_dir.mkdir(parents=True, exist_ok=True)
    success_dir = merged_dir / "success"
    fail_dir = merged_dir / "fail"
    success_dir.mkdir(exist_ok=True)
    fail_dir.mkdir(exist_ok=True)

    # Collect all per-task results across runs, keyed by task_id
    # Each entry: list of (run_dir, result_dict) in run order
    task_runs: dict[str, list[tuple[Path, dict]]] = {}
    for run_dir in run_dirs:
        results_file = run_dir / "results.json"
        if not results_file.exists():
            continue
        with open(results_file) as f:
            data = json.load(f)
        for task_result in data["tasks"]:
            tid = task_result["task_id"]
            task_runs.setdefault(tid, []).append((run_dir, task_result))

    merged_results = []
    for tid, runs in sorted(task_runs.items()):
        # Check if any run passed
        passing = [(rd, r) for rd, r in runs if r["passed"]]
        if passing:
            # Use first passing result
            src_run_dir, best_result = passing[0]
            dest = success_dir / tid
        else:
            # Use last failing result
            src_run_dir, best_result = runs[-1]
            dest = fail_dir / tid

        # Copy the task directory (screenshots, history, result.json, etc.)
        src_task_dir = src_run_dir / tid
        if src_task_dir.exists():
            shutil.copytree(src_task_dir, dest, dirs_exist_ok=True)
        else:
            # No task dir (shouldn't happen), just write result.json
            dest.mkdir(parents=True, exist_ok=True)
            with open(dest / "result.json", "w") as f:
                json.dump(best_result, f, indent=2)

        # Tag with which run the result came from
        best_result["source_run"] = src_run_dir.name
        merged_results.append(best_result)

    merged_results.sort(key=lambda r: r["task_id"])

    # Aggregate stats
    total = len(merged_results)
    passed = sum(1 for r in merged_results if r["passed"])
    by_diff: dict[str, dict] = {}
    for r in merged_results:
        d = r.get("difficulty", "")
        if d:
            by_diff.setdefault(d, {"total": 0, "passed": 0})
            by_diff[d]["total"] += 1
            if r["passed"]:
                by_diff[d]["passed"] += 1

    aggregate = {
        "model": model,
        "timestamp": timestamp,
        "use_vision": use_vision,
        "workers": num_workers,
        "repetitions": len(run_dirs),
        "source_runs": [rd.name for rd in run_dirs],
        "total": total,
        "passed": passed,
        "pass_rate": round(passed / total * 100, 1) if total else 0,
        "by_difficulty": by_diff,
        "tasks": merged_results,
    }
    with open(merged_dir / "results.json", "w") as f:
        json.dump(aggregate, f, indent=2)

    # Generate report in merged dir (report.py reads task dirs relative to run_dir)
    # We need to generate report pointing at the merged structure. Since tasks live
    # under success/ and fail/ (not directly under merged_dir), we generate the report
    # manually using the merged results.
    from report import generate_report
    report_path = generate_report(merged_results, model, timestamp, merged_dir)

    return aggregate, report_path


def find_incomplete_tasks(
    run_dir: Path, expected_tasks: list[dict]
) -> tuple[list[dict], list[dict]]:
    """Analyze a partial run dir. Returns (remaining_tasks, completed_results).

    - A task is complete if run_dir/task_id/result.json exists
    - Incomplete task dirs (dir exists, no result.json) are deleted
    """
    completed_results: list[dict] = []
    remaining_tasks: list[dict] = []

    for task in expected_tasks:
        task_id = task["id"]
        task_dir = run_dir / task_id
        result_file = task_dir / "result.json"

        if result_file.exists():
            # Task completed — load its result
            with open(result_file) as f:
                completed_results.append(json.load(f))
        else:
            # Task not completed — needs to be re-run
            if task_dir.exists():
                # Partial dir (agent was mid-execution) — clean up
                shutil.rmtree(task_dir)
            remaining_tasks.append(task)

    return remaining_tasks, completed_results


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
        try:
            await agent.setup(server_url)
        except Exception as setup_err:
            print(f"  {tag} {RED}Browser setup failed: {setup_err}{RESET}")
            return
        print(f"  {tag} ready on :{port}")

        while True:
            try:
                task = task_queue.get_nowait()
            except asyncio.QueueEmpty:
                break

            task_id = task["id"]
            diff = task.get("difficulty", "")
            dc = DIFF_COLOR.get(diff, "")
            task_dir = run_dir / task_id
            task_dir.mkdir(parents=True, exist_ok=True)

            needs_restart = False
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
                # If the agent reported errors, the browser may be degraded
                if result.get("errors"):
                    err_text = " ".join(str(e) for e in result["errors"])
                    if any(k in err_text for k in ("INSUFFICIENT_RESOURCES", "Timeout", "CDP", "consecutive failures")):
                        needs_restart = True
            except asyncio.TimeoutError:
                print(f"  {tag} {BOLD}{task_id}{RESET} {dc}{diff}{RESET}  {BG_YELLOW}{WHITE}{BOLD} TIME {RESET}")
                result = {
                    "task_id": task_id,
                    "difficulty": task.get("difficulty", ""),
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
                needs_restart = True
            except Exception as e:
                print(f"  {tag} {BOLD}{task_id}{RESET} {dc}{diff}{RESET}  {BG_RED}{WHITE}{BOLD} ERR  {RESET} {DIM}{e}{RESET}")
                result = {
                    "task_id": task_id,
                    "difficulty": task.get("difficulty", ""),
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
                needs_restart = True

            async with results_lock:
                results.append(result)

            # Restart browser if the previous task left it in a bad state
            if needs_restart and not task_queue.empty():
                print(f"  {tag} {YELLOW}Restarting browser session after error...{RESET}")
                try:
                    await agent.restart_session()
                    print(f"  {tag} {GREEN}Browser restarted OK{RESET}")
                except Exception as restart_err:
                    print(f"  {tag} {RED}Browser restart failed: {restart_err}{RESET}")
                    break

    finally:
        await agent.teardown()
        if server_proc:
            stop_server(server_proc)


async def run_single_eval(
    tasks: list[dict],
    args,
    run_dir: Path,
    web_app_dir: str,
    run_label: str = "",
    prior_results: list[dict] | None = None,
) -> tuple[list[dict], dict]:
    """Execute a single evaluation run. Returns (results, aggregate)."""
    num_workers = min(args.workers, len(tasks))
    port_hi = args.base_port + num_workers - 1

    timestamp = run_dir.name.split("_", 1)[-1] if "_" in run_dir.name else ""

    # Header
    resuming = prior_results is not None
    header_label = "  Resuming Evaluation" if resuming else "  Parallel Evaluation"
    print(f"\n{BOLD}{CYAN}{'=' * 60}{RESET}")
    print(f"{BOLD}{CYAN}{header_label}{run_label}{RESET}")
    print(f"{BOLD}{CYAN}{'=' * 60}{RESET}")
    print(f"  {DIM}Model:{RESET}   {BOLD}{args.model}{RESET}")
    print(f"  {DIM}Suite:{RESET}   {BOLD}{args.task_suite}{RESET}")
    print(f"  {DIM}Tasks:{RESET}   {BOLD}{len(tasks)}{RESET}" + (f" {DIM}({len(prior_results)} already done){RESET}" if resuming else ""))
    print(f"  {DIM}Workers:{RESET} {BOLD}{num_workers}{RESET}")
    print(f"  {DIM}Env:{RESET}     {BOLD}{args.env_host}:{args.base_port}-{port_hi}{RESET}")
    print(f"  {DIM}Vision:{RESET}  {BOLD}{'on' if args.use_vision else 'off'}{RESET}")
    print(f"  {DIM}Output:{RESET}  {run_dir}")
    print(f"{CYAN}{'─' * 60}{RESET}\n")

    # Build task queue
    task_queue: asyncio.Queue = asyncio.Queue()
    for t in tasks:
        await task_queue.put(t)

    results: list[dict] = list(prior_results) if prior_results else []
    results_lock = asyncio.Lock()

    # Launch workers with staggered startup to avoid overwhelming the system
    # when multiple Chromium instances start simultaneously.
    async def staggered_worker(i, startup_delay):
        if startup_delay > 0:
            await asyncio.sleep(startup_delay)
        await worker(
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

    STAGGER_DELAY = 5  # seconds between each worker launch
    worker_coros = [
        staggered_worker(i, i * STAGGER_DELAY)
        for i in range(num_workers)
    ]
    await asyncio.gather(*worker_coros)

    if not results:
        return [], {}

    # Sort results by task_id for consistent ordering
    results.sort(key=lambda r: r["task_id"])

    # Aggregate
    total = len(results)
    passed = sum(1 for r in results if r["passed"])
    by_diff: dict[str, dict] = {}
    for r in results:
        d = r.get("difficulty", "")
        if d:
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
    print(f"  {BOLD}Results{run_label}: {pct_color}{passed}/{total} passed ({pct}%){RESET}")
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

    return results, aggregate


async def main():
    parser = argparse.ArgumentParser(
        description="Parallel evaluation runner with worker pool"
    )
    parser.add_argument("--model", choices=MODELS.keys(), default="gpt")
    parser.add_argument("--task-id", default=None, help="Run one or more tasks, comma-separated (e.g. task_e1 or task_3,task_4,task_6)")
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
    parser.add_argument("--task-suite", default="tasks",
                        help="Task suite name, e.g. 'tasks' or 'tasks-function-test' (loads <name>.json)")
    # Multi-run arguments
    parser.add_argument("--repetitions", type=int, default=1,
                        help="Number of times to repeat the evaluation (default: 1). "
                             "Runs cascade: run 1 executes all selected tasks, run 2 "
                             "retries only failures from run 1, and so on.")
    parser.add_argument("--failed-only", action="store_true",
                        help="Cascading mode: run 2+ retries only tasks that failed "
                             "in the previous run. Without this flag, every run "
                             "executes the full task set.")
    parser.add_argument("--resume-dir", default=None,
                        help="Resume a partial evaluation into this existing directory. "
                             "Detects completed tasks and only re-runs the remainder.")
    args = parser.parse_args()

    web_app_dir = str(Path(args.web_app).resolve())
    output_dir = args.output_dir or os.path.join(web_app_dir, "results")

    # Load and filter tasks
    all_tasks = load_tasks(web_app_dir, task_suite=args.task_suite)
    tasks = filter_tasks(all_tasks, task_id=args.task_id, difficulty=args.difficulty)
    if not tasks:
        print(f"{RED}No tasks matched.{RESET}")
        sys.exit(1)

    # Single run (original behavior)
    if args.repetitions <= 1:
        if args.resume_dir:
            run_dir = Path(args.resume_dir)
            remaining, prior = find_incomplete_tasks(run_dir, tasks)
            if not remaining:
                print(f"{GREEN}All tasks already completed in {run_dir}{RESET}")
                return
            results, _ = await run_single_eval(
                remaining, args, run_dir, web_app_dir, prior_results=prior,
            )
        else:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            suite_tag = f"_{args.task_suite}" if args.task_suite != "tasks" else ""
            run_dir = Path(output_dir) / f"{args.model}_{timestamp}{suite_tag}_parallel"
            run_dir.mkdir(parents=True, exist_ok=True)
            results, _ = await run_single_eval(tasks, args, run_dir, web_app_dir)

        if not results:
            print(f"{RED}No tasks completed.{RESET}")
            sys.exit(1)
        return

    # Multi-run mode
    #
    # --failed-only (cascading):
    #   Run 1: all selected tasks
    #   Run 2: only tasks that failed in run 1
    #   Run 3: only tasks that failed in run 2  …stops early if all pass
    #
    # Without --failed-only (full repeat):
    #   Every run executes the full task set
    #
    # Directory layout:
    #   parent_dir/
    #   ├── run1/   run2/   run3/   ...
    #   ├── merged/  (success/ + fail/)
    #   ├── results.json   (merged — top-level)
    #   └── report.html
    num_workers = min(args.workers, len(tasks))

    if args.resume_dir:
        parent_dir = Path(args.resume_dir)
        # Extract timestamp from dir name (format: {model}_{timestamp}_{suite}_parallel)
        parts = parent_dir.name.split("_", 1)
        timestamp = parts[1] if len(parts) > 1 else datetime.now().strftime("%Y%m%d_%H%M%S")
    else:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        suite_tag = f"_{args.task_suite}" if args.task_suite != "tasks" else ""
        parent_dir = Path(output_dir) / f"{args.model}_{timestamp}{suite_tag}_parallel"
    parent_dir.mkdir(parents=True, exist_ok=True)

    mode_label = "cascading (failed-only)" if args.failed_only else "full repeat"
    resume_label = " (resuming)" if args.resume_dir else ""
    print(f"\n{BOLD}{MAGENTA}{'=' * 60}{RESET}")
    print(f"{BOLD}{MAGENTA}  Multi-Run Evaluation: {args.repetitions} rounds ({mode_label}){resume_label}{RESET}")
    print(f"  {DIM}Output:{RESET}  {parent_dir}")
    print(f"{BOLD}{MAGENTA}{'=' * 60}{RESET}")

    run_dirs: list[Path] = []
    current_tasks = tasks
    all_tasks_by_id = {t["id"]: t for t in tasks}

    for rep in range(1, args.repetitions + 1):
        if args.failed_only and not current_tasks:
            print(f"\n{GREEN}All tasks passed — stopping early after {rep - 1} runs.{RESET}")
            break

        run_dir = parent_dir / f"run{rep}"
        run_dirs.append(run_dir)

        # Resume logic: check state of each runN/ directory
        run_results_file = run_dir / "results.json"
        if args.resume_dir and run_results_file.exists():
            # Run is complete — load results and cascade failures
            print(f"\n{GREEN}Run {rep}: already complete — loading results{RESET}")
            with open(run_results_file) as f:
                saved = json.load(f)
            results = saved.get("tasks", [])

            if args.failed_only:
                failed_ids = {r["task_id"] for r in results if not r["passed"]}
                current_tasks = [all_tasks_by_id[tid] for tid in failed_ids if tid in all_tasks_by_id]
            continue

        if args.resume_dir and run_dir.exists():
            # Partial run — find what's done and resume the rest
            remaining, prior = find_incomplete_tasks(run_dir, current_tasks)
            if not remaining:
                # All tasks done but results.json wasn't written — run will regenerate it
                print(f"\n{GREEN}Run {rep}: all tasks done, regenerating results.json{RESET}")
                results, _ = await run_single_eval(
                    [], args, run_dir, web_app_dir,
                    run_label=f" (run {rep}/{args.repetitions}, 0 tasks)",
                    prior_results=prior,
                )
            else:
                results, _ = await run_single_eval(
                    remaining, args, run_dir, web_app_dir,
                    run_label=f" (run {rep}/{args.repetitions}, {len(remaining)} remaining of {len(current_tasks)} tasks)",
                    prior_results=prior,
                )
        else:
            # Fresh run
            run_dir.mkdir(parents=True, exist_ok=True)
            results, _ = await run_single_eval(
                current_tasks, args, run_dir, web_app_dir,
                run_label=f" (run {rep}/{args.repetitions}, {len(current_tasks)} tasks)",
            )

        if not results:
            print(f"{YELLOW}Run {rep}: no tasks completed, skipping.{RESET}")
            continue

        if args.failed_only:
            # Narrow to only the tasks that still failed for the next round
            failed_ids = {r["task_id"] for r in results if not r["passed"]}
            current_tasks = [all_tasks_by_id[tid] for tid in failed_ids if tid in all_tasks_by_id]

            passed_this_round = sum(1 for r in results if r["passed"])
            if passed_this_round > 0 and failed_ids:
                print(f"  {MAGENTA}→ {len(failed_ids)} still failing, will retry in next round{RESET}")

    if not run_dirs:
        print(f"{RED}No runs completed.{RESET}")
        sys.exit(1)

    # Merge results across all runs into parent/merged/
    merged_dir = parent_dir / "merged"
    print(f"\n{BOLD}{MAGENTA}{'=' * 60}{RESET}")
    print(f"{BOLD}{MAGENTA}  Merging {len(run_dirs)} runs → merged/{RESET}")
    print(f"{BOLD}{MAGENTA}{'=' * 60}{RESET}")

    aggregate, report_path = merge_repetition_results(
        run_dirs=run_dirs,
        merged_dir=merged_dir,
        model=args.model,
        timestamp=timestamp,
        use_vision=args.use_vision,
        num_workers=num_workers,
    )

    # Copy merged results.json + report.html to parent for find_latest_results
    shutil.copy2(merged_dir / "results.json", parent_dir / "results.json")
    shutil.copy2(merged_dir / "report.html", parent_dir / "report.html")

    # Final merged summary
    passed = aggregate["passed"]
    total = aggregate["total"]
    pct = aggregate["pass_rate"]
    by_diff = aggregate["by_difficulty"]
    pct_color = GREEN if pct >= 50 else RED

    print(f"\n{BOLD}{MAGENTA}{'=' * 60}{RESET}")
    print(f"  {BOLD}Merged Results ({len(run_dirs)} runs): {pct_color}{passed}/{total} passed ({pct}%){RESET}")
    print()
    for d in ["easy", "medium", "hard"]:
        if d in by_diff:
            info = by_diff[d]
            dc = DIFF_COLOR.get(d, "")
            ratio_color = GREEN if info["passed"] == info["total"] else (YELLOW if info["passed"] > 0 else RED)
            print(f"    {dc}{d.capitalize():8s}{RESET} {ratio_color}{info['passed']}/{info['total']}{RESET}")
    print()
    print(f"  {DIM}Output:{RESET}   {parent_dir}")
    print(f"  {DIM}Success:{RESET}  {GREEN}{merged_dir / 'success'}{RESET}")
    print(f"  {DIM}Fail:{RESET}     {RED}{merged_dir / 'fail'}{RESET}")
    print(f"  {DIM}Report:{RESET}   {MAGENTA}{parent_dir / 'report.html'}{RESET}")
    print(f"{MAGENTA}{'=' * 60}{RESET}\n")


if __name__ == "__main__":
    asyncio.run(main())
