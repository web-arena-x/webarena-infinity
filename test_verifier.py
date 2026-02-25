#!/usr/bin/env python3
"""
Interactive verifier testing tool.

Usage:
    python3 test_verifier.py <app_dir> [task_id]

Example:
    python3 test_verifier.py apps/gitlab-org-management
    python3 test_verifier.py apps/linear task_e1
    python3 test_verifier.py ./apps/gitlab-org-management task_m3 --port 9000

If no task_id is given, lists all available tasks and prompts for selection.
Each round: resets state → waits for you to perform the task in the browser → you press Enter → runs the verifier.
Type 'q' to quit or pick a different task.
"""

import argparse
import importlib.util
import json
import subprocess
import sys
import time
import webbrowser
from pathlib import Path

import requests


def load_tasks(app_dir):
    with open(Path(app_dir) / "tasks.json") as f:
        return json.load(f)


def load_verifier(app_dir, verify_path):
    full_path = str(Path(app_dir) / verify_path)
    spec = importlib.util.spec_from_file_location("verifier", full_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.verify


def reset_and_wait(server_url):
    """Reset state to seed data on the server and notify the browser."""
    resp = requests.post(f"{server_url}/api/reset")
    if resp.status_code != 200:
        print(f"  [!] Reset failed: {resp.status_code}")
        return False

    data = resp.json()
    if not data.get("seed_restored"):
        print("  [!] No seed state captured yet. Load the app in a browser first.")
        return False

    # Brief pause to let the browser process the SSE reset event
    time.sleep(0.5)
    return True


def pick_task(tasks):
    """Display task list and let user pick one."""
    print("\nAvailable tasks:")
    print("-" * 80)
    for t in tasks:
        print(f"  {t['id']:10s}  [{t['difficulty']:6s}]  {t['instruction'][:55]}...")
    print("-" * 80)
    while True:
        choice = input("\nEnter task ID (e.g. task_e1) or 'q' to quit: ").strip()
        if choice == "q":
            return None
        match = next((t for t in tasks if t["id"] == choice), None)
        if match:
            return match
        print(f"  Unknown task '{choice}'. Try again.")


def run_loop(task, tasks, app_dir, server_url):
    """Run reset-perform-verify loop for a task."""
    verify_fn = load_verifier(app_dir, task["verify"])
    attempt = 0

    while True:
        attempt += 1
        print(f"\n{'='*70}")
        print(f"Task:       {task['id']} [{task['difficulty']}]")
        print(f"Instruction: {task['instruction']}")
        print(f"Attempt:    #{attempt}")
        print(f"{'='*70}")

        print("\n  Resetting state...", end=" ", flush=True)
        if not reset_and_wait(server_url):
            return
        print("done.")
        print("\n  >>> Perform the task in your browser now. <<<")

        cmd = (
            input(
                "\n  Press Enter when done, 'r' to re-reset, 's' to switch task, 'q' to quit: "
            )
            .strip()
            .lower()
        )
        if cmd == "q":
            return "quit"
        if cmd == "s":
            return "switch"
        if cmd == "r":
            attempt -= 1
            continue

        # Run verifier
        print("\n  Running verifier...", end=" ", flush=True)
        try:
            passed, message = verify_fn(server_url)
        except Exception as e:
            passed, message = False, f"Verifier error: {e}"

        if passed:
            print("PASSED")
            print(f"  {message}")
        else:
            print("FAILED")
            print(f"  {message}")

        cmd = (
            input("\n  Press Enter to retry, 's' to switch task, 'q' to quit: ")
            .strip()
            .lower()
        )
        if cmd == "q":
            return "quit"
        if cmd == "s":
            return "switch"


def _run_web_mode(app_dir, port, server_url):
    """Start the app server with --test-mode and open the browser."""
    print(f"Starting server with test panel on port {port}...")
    proc = subprocess.Popen(
        [sys.executable, "server.py", "--port", str(port), "--test-mode"],
        cwd=str(app_dir),
    )
    # Poll until server is ready
    deadline = time.time() + 15
    ready = False
    while time.time() < deadline:
        try:
            r = requests.get(f"{server_url}/", timeout=2)
            if r.status_code == 200:
                ready = True
                break
        except requests.ConnectionError:
            pass
        time.sleep(0.5)

    if not ready:
        print("Error: server did not start in time.")
        proc.terminate()
        sys.exit(1)

    print(f"Server ready at {server_url}")
    print("Opening browser... Press Ctrl+C to stop.\n")
    webbrowser.open(server_url)

    try:
        proc.wait()
    except KeyboardInterrupt:
        print("\nShutting down server...")
        proc.terminate()
        try:
            proc.wait(timeout=5)
        except subprocess.TimeoutExpired:
            proc.kill()
    print("Done.")


def main():
    parser = argparse.ArgumentParser(
        description="Interactive verifier testing tool for human spot-checking."
    )
    parser.add_argument(
        "app_dir",
        help="Path to the web app directory (e.g. apps/gitlab-org-management, apps/linear)",
    )
    parser.add_argument(
        "task_id", nargs="?", default=None, help="Task ID to test (e.g. task_e1)"
    )
    parser.add_argument(
        "--port", type=int, default=8080, help="Server port (default: 8080)"
    )
    parser.add_argument(
        "--web",
        action="store_true",
        help="Start server with in-browser test panel and open in browser",
    )
    args = parser.parse_args()

    app_dir = Path(args.app_dir).resolve()
    if not (app_dir / "tasks.json").exists():
        print(f"Error: {app_dir / 'tasks.json'} not found.")
        sys.exit(1)

    server_url = f"http://localhost:{args.port}"

    if args.web:
        _run_web_mode(app_dir, args.port, server_url)
        return

    tasks = load_tasks(app_dir)

    # If task_id provided, jump straight to it
    if args.task_id:
        task = next((t for t in tasks if t["id"] == args.task_id), None)
        if not task:
            print(
                f"Unknown task '{args.task_id}'. Available: {', '.join(t['id'] for t in tasks)}"
            )
            sys.exit(1)
    else:
        task = pick_task(tasks)
        if not task:
            return

    while True:
        result = run_loop(task, tasks, app_dir, server_url)
        if result == "quit" or result is None:
            break
        if result == "switch":
            task = pick_task(tasks)
            if not task:
                break

    print("\nDone.")


if __name__ == "__main__":
    main()
