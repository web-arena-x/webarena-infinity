#!/usr/bin/env python3
"""Environment generator worker — runs on m5.xlarge Env Generator instances.

Runs PARALLEL_WORKERS concurrent workers, each with its own git worktree and
port range. Each worker independently polls SQS for jobs and processes them.

Usage:
    python infra/env_worker.py                         # 5 parallel workers (default)
    python infra/env_worker.py --parallel 3             # 3 parallel workers
    python infra/env_worker.py --parallel 1             # sequential (legacy mode)
    python infra/env_worker.py --dry-run                # log actions without executing
"""

from __future__ import annotations

import argparse
import json
import logging
import multiprocessing
import os
import shlex
import signal
import subprocess
import sys
import time

sys.path.insert(0, os.path.dirname(__file__))

from config import (
    BASE_PORT,
    BRANCH_PREFIX,
    EVAL_DONE_QUEUE_URL,
    EVAL_QUEUE_URL,
    GENERATE_QUEUE_URL,
    GIT_REMOTE,
    LOG_DIR,
    MAX_ITERATIONS,
    PARALLEL_WORKERS,
    PIPELINE_DONE_QUEUE_URL,
    REFERENCE_APP,
    REPO_DIR,
    SERVERS_PER_ENV,
    SQS_VISIBILITY_TIMEOUT,
    WORKTREE_DIR,
)
from sqs_utils import delete_message, receive_message, release_message, send_message

# ---------------------------------------------------------------------------
# Prompt templates (loaded from infra/prompts/*.md)
# ---------------------------------------------------------------------------
PROMPTS_DIR = os.path.join(os.path.dirname(__file__), "prompts")


def load_prompt(name: str, **kwargs: str) -> str:
    """Load a prompt template from infra/prompts/{name}.md and fill placeholders."""
    path = os.path.join(PROMPTS_DIR, f"{name}.md")
    with open(path) as f:
        template = f.read().strip()
    return template.format(**kwargs)


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [env-worker] %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger(__name__)

# Graceful shutdown
_shutdown = False


def _handle_signal(signum, frame):
    global _shutdown
    log.info("Received signal %s, shutting down workers", signum)
    _shutdown = True


# ---------------------------------------------------------------------------
# Git helpers (worktree-aware)
# ---------------------------------------------------------------------------

# File-based lock for git operations on the main repo — git doesn't handle
# concurrency.  A file lock works across fork/spawn and auto-releases if the
# holder crashes.
import fcntl

_GIT_LOCK_PATH = os.path.join(REPO_DIR, ".git", "mirror-mirror.lock")


class _GitLock:
    """Context manager using fcntl file locking."""

    def __enter__(self):
        self._fd = open(_GIT_LOCK_PATH, "w")
        fcntl.flock(self._fd, fcntl.LOCK_EX)
        return self

    def __exit__(self, *exc):
        fcntl.flock(self._fd, fcntl.LOCK_UN)
        self._fd.close()


_git_lock = _GitLock()


def git(*args: str, cwd: str = REPO_DIR) -> subprocess.CompletedProcess:
    cmd = ["git", *args]
    result = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    if result.returncode != 0:
        log.error(
            "git %s failed (rc=%d): %s",
            " ".join(args),
            result.returncode,
            result.stderr.strip(),
        )
        result.check_returncode()
    return result


def setup_worktree(worker_id: int, env_id: str) -> str:
    """Create or reset a git worktree for this worker+env.

    Returns the worktree path.
    """
    worktree_path = os.path.join(WORKTREE_DIR, f"worker-{worker_id}")
    branch = f"{BRANCH_PREFIX}{env_id.removeprefix(BRANCH_PREFIX)}"

    with _git_lock:
        # Clean stale worktree entries
        git("worktree", "prune")

        # Fetch the branch
        git("fetch", GIT_REMOTE, branch)

        if os.path.isdir(worktree_path):
            # Remove existing worktree and re-create for the new branch
            git("worktree", "remove", "--force", worktree_path)

        git("worktree", "add", worktree_path, branch)
        git("reset", "--hard", f"{GIT_REMOTE}/{branch}", cwd=worktree_path)

    return worktree_path


def remove_worktree(worker_id: int) -> None:
    """Clean up a worker's worktree."""
    worktree_path = os.path.join(WORKTREE_DIR, f"worker-{worker_id}")
    if os.path.isdir(worktree_path):
        with _git_lock:
            try:
                git("worktree", "remove", "--force", worktree_path)
            except subprocess.CalledProcessError:
                pass


def commit_and_push(worktree_path: str, env_id: str, message: str) -> None:
    branch = f"{BRANCH_PREFIX}{env_id.removeprefix(BRANCH_PREFIX)}"
    apps_dir = os.path.join(worktree_path, "apps", env_id)
    git("add", apps_dir, cwd=worktree_path)
    result = subprocess.run(
        ["git", "diff", "--cached", "--quiet"],
        cwd=worktree_path,
        capture_output=True,
    )
    if result.returncode == 0:
        log.info("[%s] No changes to commit", env_id)
        return
    git("commit", "-m", message, cwd=worktree_path)
    git("push", GIT_REMOTE, branch, cwd=worktree_path)


# ---------------------------------------------------------------------------
# Server management (port-range aware)
# ---------------------------------------------------------------------------


def start_servers(app_dir: str, worker_id: int) -> list[subprocess.Popen]:
    """Start SERVERS_PER_ENV servers on this worker's port range."""
    import requests

    port_base = BASE_PORT + (worker_id * SERVERS_PER_ENV)
    procs = []
    for i in range(SERVERS_PER_ENV):
        port = port_base + i
        proc = subprocess.Popen(
            [sys.executable, "server.py", "--port", str(port)],
            cwd=app_dir,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        procs.append(proc)

    # Wait for all servers to be ready
    for i, proc in enumerate(procs):
        port = port_base + i
        url = f"http://localhost:{port}/"
        deadline = time.time() + 15
        while time.time() < deadline:
            try:
                r = requests.get(url, timeout=2)
                if r.status_code == 200:
                    break
            except requests.ConnectionError:
                pass
            time.sleep(0.5)
        else:
            log.warning("Server on :%d did not become ready in time", port)

    log.info(
        "Started %d servers on :%d-:%d",
        SERVERS_PER_ENV,
        port_base,
        port_base + SERVERS_PER_ENV - 1,
    )
    return procs


def stop_servers(procs: list[subprocess.Popen]) -> None:
    for proc in procs:
        if proc.poll() is None:
            proc.terminate()
    for proc in procs:
        try:
            proc.wait(timeout=5)
        except subprocess.TimeoutExpired:
            proc.kill()
            proc.wait()


# ---------------------------------------------------------------------------
# Claude Code invocation
# ---------------------------------------------------------------------------


LIVE_LOG_DIR = os.path.join(LOG_DIR, "live")


def run_claude_code(
    prompt: str, app_dir: str, worker_id: int = 0, timeout: int = 3600
) -> subprocess.CompletedProcess:
    """Run claude --print inside a tmux session for PTY + live observability.

    Claude requires a TTY to produce output.  We run it inside a named tmux
    session so that (a) it gets a real PTY and (b) the user can
    ``tmux attach -t claude-W<id>`` to watch progress live.

    Output is also tee'd to a log file for post-hoc inspection.
    A marker file signals completion so we can poll for it.
    """
    log_path = os.path.join(LIVE_LOG_DIR, f"env-W{worker_id}-claude.log")
    done_path = os.path.join(LIVE_LOG_DIR, f"env-W{worker_id}-done")
    rc_path = os.path.join(LIVE_LOG_DIR, f"env-W{worker_id}-rc")
    os.makedirs(os.path.dirname(log_path), exist_ok=True)

    # Clean up markers from previous run
    for p in (done_path, rc_path, log_path):
        if os.path.exists(p):
            os.remove(p)

    session_name = f"claude-W{worker_id}"

    # Kill any leftover tmux session with this name
    subprocess.run(["tmux", "kill-session", "-t", session_name],
                   capture_output=True)

    # Build the command to run inside tmux.
    # Tee output to log, write exit code to rc file, touch done marker.
    inner = (
        f"claude --print --dangerously-skip-permissions {shlex.quote(prompt)}"
        f" 2>&1 | tee {shlex.quote(log_path)}"
        f"; echo ${{PIPESTATUS[0]}} > {shlex.quote(rc_path)}"
        f"; touch {shlex.quote(done_path)}"
    )

    # Launch tmux session (detached)
    subprocess.run(
        ["tmux", "new-session", "-d", "-s", session_name, "-c", app_dir,
         "bash", "-c", inner],
        check=True,
    )
    log.info("[W%d] tmux session '%s' started — attach with: tmux attach -t %s",
             worker_id, session_name, session_name)

    # Poll for completion
    deadline = time.time() + timeout
    while time.time() < deadline:
        if os.path.exists(done_path):
            break
        time.sleep(5)
    else:
        # Timeout — kill the session
        subprocess.run(["tmux", "kill-session", "-t", session_name],
                       capture_output=True)
        return subprocess.CompletedProcess(
            args=inner, returncode=1,
            stdout="", stderr="Timeout after %ds" % timeout,
        )

    # Read output and exit code
    stdout = ""
    if os.path.exists(log_path):
        with open(log_path) as f:
            stdout = f.read()
    returncode = 0
    if os.path.exists(rc_path):
        try:
            returncode = int(open(rc_path).read().strip())
        except (ValueError, OSError):
            returncode = 1

    return subprocess.CompletedProcess(
        args=inner, returncode=returncode,
        stdout=stdout, stderr="",
    )


def generate_environment(env_id: str, docs_source: str, worktree_path: str, worker_id: int = 0) -> bool:
    app_dir = os.path.join(worktree_path, "apps", env_id)
    os.makedirs(app_dir, exist_ok=True)

    prompt = load_prompt(
        "generate",
        reference_app=REFERENCE_APP,
        worktree_path=worktree_path,
        docs_source=docs_source,
    )

    result = run_claude_code(prompt, app_dir, worker_id=worker_id)
    if result.returncode != 0:
        log.error("[%s] Claude Code failed: %s", env_id, result.stderr[-500:])
        return False

    log.info("[%s] Generation complete", env_id)
    return True


def run_sanity_check(env_id: str, worktree_path: str) -> bool:
    app_dir = os.path.join(worktree_path, "apps", env_id)
    sanity_script = os.path.join(app_dir, "sanity_check.py")

    if not os.path.exists(sanity_script):
        log.error("[%s] sanity_check.py not found", env_id)
        return False

    result = subprocess.run(
        [sys.executable, sanity_script, "--workers", "4"],
        cwd=app_dir,
        capture_output=True,
        text=True,
        timeout=300,
    )
    if result.returncode != 0:
        log.warning("[%s] Sanity check failed:\n%s", env_id, result.stdout[-1000:])
        return False

    log.info("[%s] Sanity check passed", env_id)
    return True


# ---------------------------------------------------------------------------
# Audit
# ---------------------------------------------------------------------------


def run_audit(env_id: str, iteration: int, worktree_path: str, worker_id: int = 0) -> bool:
    app_dir = os.path.join(worktree_path, "apps", env_id)
    results_dir = os.path.join(app_dir, "results")

    if not os.path.isdir(results_dir):
        return False

    # Find the latest run subdirectory (e.g., gemini_20260216_003903_parallel/)
    run_dirs = sorted(
        [
            d
            for d in os.listdir(results_dir)
            if os.path.isdir(os.path.join(results_dir, d))
        ],
        reverse=True,
    )
    if not run_dirs:
        return False

    latest_run_dir = os.path.join(results_dir, run_dirs[0])

    prompt = load_prompt(
        "audit",
        results_dir=latest_run_dir,
        worktree_path=worktree_path,
        iteration=str(iteration),
        max_iterations=str(MAX_ITERATIONS),
    )

    result = run_claude_code(prompt, app_dir, worker_id=worker_id)
    if result.returncode != 0:
        log.error("[%s] Audit failed: %s", env_id, result.stderr[-500:])
        return False

    changes_made = "CHANGES_MADE" in result.stdout
    if changes_made:
        log.info("[%s] Audit revision (iter %d)", env_id, iteration)
        if not run_sanity_check(env_id, worktree_path):
            log.error("[%s] Sanity check failed after audit", env_id)
            return False
        commit_and_push(
            worktree_path, env_id, f"Audit revision iteration {iteration} for {env_id}"
        )
    else:
        log.info("[%s] Audit: no changes needed", env_id)

    return changes_made


# ---------------------------------------------------------------------------
# Wait for eval-done signal
# ---------------------------------------------------------------------------


def wait_for_eval_done(env_id: str, iteration: int) -> dict | None:
    deadline = time.time() + 7200
    while time.time() < deadline:
        if _shutdown:
            return None
        result = receive_message(EVAL_DONE_QUEUE_URL, visibility_timeout=60)
        if result is None:
            continue
        body, receipt = result
        if body.get("env_id") == env_id and body.get("iteration") == iteration:
            delete_message(EVAL_DONE_QUEUE_URL, receipt)
            return body
        # Not for this worker — release immediately so the right worker can grab it
        release_message(EVAL_DONE_QUEUE_URL, receipt)
    log.error("[%s] Timed out waiting for eval-done iter %d", env_id, iteration)
    return None


# ---------------------------------------------------------------------------
# Get private IP
# ---------------------------------------------------------------------------


def get_private_ip() -> str:
    try:
        import requests

        token_resp = requests.put(
            "http://169.254.169.254/latest/api/token",
            headers={"X-aws-ec2-metadata-token-ttl-seconds": "21600"},
            timeout=2,
        )
        ip_resp = requests.get(
            "http://169.254.169.254/latest/meta-data/local-ipv4",
            headers={"X-aws-ec2-metadata-token": token_resp.text},
            timeout=2,
        )
        return ip_resp.text.strip()
    except Exception:
        return "localhost"


# ---------------------------------------------------------------------------
# Process a single environment (full lifecycle)
# ---------------------------------------------------------------------------


def process_env(
    worker_id: int, env_id: str, docs_source: str, start_iteration: int = 1
) -> None:
    """Run the full generate → eval → audit loop for one environment."""
    tag = f"[W{worker_id}:{env_id}]"
    log.info("%s Starting (source=%s, iter=%d)", tag, docs_source, start_iteration)

    port_base = BASE_PORT + (worker_id * SERVERS_PER_ENV)
    my_ip = get_private_ip()

    # Set up worktree for this env
    worktree_path = setup_worktree(worker_id, env_id)

    try:
        # Generate (only on first iteration)
        if start_iteration == 1:
            if not generate_environment(env_id, docs_source, worktree_path, worker_id=worker_id):
                log.error("%s Generation failed", tag)
                send_message(
                    PIPELINE_DONE_QUEUE_URL,
                    {
                        "env_id": env_id,
                        "final_iteration": 0,
                        "pass_rate": 0,
                        "status": "generation_failed",
                    },
                )
                return

            if not run_sanity_check(env_id, worktree_path):
                log.error("%s Sanity check failed", tag)
                send_message(
                    PIPELINE_DONE_QUEUE_URL,
                    {
                        "env_id": env_id,
                        "final_iteration": 0,
                        "pass_rate": 0,
                        "status": "sanity_check_failed",
                    },
                )
                return

            commit_and_push(worktree_path, env_id, f"Initial generation for {env_id}")

        app_dir = os.path.join(worktree_path, "apps", env_id)
        pass_rate = 0.0
        iteration = start_iteration

        for iteration in range(start_iteration, MAX_ITERATIONS + 1):
            if _shutdown:
                log.info("%s Shutdown requested at iter %d", tag, iteration)
                return

            log.info("%s Iteration %d/%d", tag, iteration, MAX_ITERATIONS)

            # Start servers on this worker's port range
            server_procs = start_servers(app_dir, worker_id)

            try:
                # Request eval
                send_message(
                    EVAL_QUEUE_URL,
                    {
                        "env_id": env_id,
                        "iteration": iteration,
                        "branch": f"{BRANCH_PREFIX}{env_id.removeprefix(BRANCH_PREFIX)}",
                        "env_host": my_ip,
                        "base_port": port_base,
                    },
                )

                # Wait for eval completion
                eval_result = wait_for_eval_done(env_id, iteration)
                if eval_result is None:
                    log.error("%s Eval timeout at iter %d", tag, iteration)
                    break
            finally:
                stop_servers(server_procs)

            # Pull results
            branch = f"{BRANCH_PREFIX}{env_id.removeprefix(BRANCH_PREFIX)}"
            git("pull", GIT_REMOTE, branch, cwd=worktree_path)

            pass_rate = eval_result.get("pass_rate", 0)
            log.info("%s Iter %d pass_rate=%.1f%%", tag, iteration, pass_rate)

            # Audit
            if iteration < MAX_ITERATIONS:
                if not run_audit(env_id, iteration, worktree_path, worker_id=worker_id):
                    log.info("%s No changes needed, done at iter %d", tag, iteration)
                    break
            else:
                run_audit(env_id, iteration, worktree_path, worker_id=worker_id)

        # Signal completion
        send_message(
            PIPELINE_DONE_QUEUE_URL,
            {
                "env_id": env_id,
                "final_iteration": iteration,
                "pass_rate": pass_rate,
                "status": "complete",
            },
        )
        log.info("%s Complete (iter=%d, pass_rate=%.1f%%)", tag, iteration, pass_rate)

    finally:
        remove_worktree(worker_id)


# ---------------------------------------------------------------------------
# Worker process: polls SQS and processes envs
# ---------------------------------------------------------------------------


def worker_loop(worker_id: int, dry_run: bool = False) -> None:
    """One worker process: polls SQS, processes envs sequentially."""
    tag = f"[W{worker_id}]"
    log.info(
        "%s Started (ports %d-%d)",
        tag,
        BASE_PORT + worker_id * SERVERS_PER_ENV,
        BASE_PORT + (worker_id + 1) * SERVERS_PER_ENV - 1,
    )

    while not _shutdown:
        result = receive_message(
            GENERATE_QUEUE_URL,
            visibility_timeout=SQS_VISIBILITY_TIMEOUT,
        )
        if result is None:
            continue

        body, receipt = result
        env_id = body["env_id"]
        docs_source = body["docs_source"]
        start_iteration = body.get("iteration", 1)

        log.info("%s Picked up: %s (source=%s)", tag, env_id, docs_source)

        try:
            if not dry_run:
                process_env(worker_id, env_id, docs_source, start_iteration)
            else:
                log.info("%s [dry-run] Would process %s", tag, env_id)
        except Exception:
            log.exception("%s Error processing %s", tag, env_id)
        finally:
            delete_message(GENERATE_QUEUE_URL, receipt)

    log.info("%s Exiting", tag)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> None:
    parser = argparse.ArgumentParser(description="Env generator worker daemon")
    parser.add_argument(
        "--parallel",
        type=int,
        default=PARALLEL_WORKERS,
        help="Number of parallel workers per instance (default: %(default)s)",
    )
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    os.makedirs(LOG_DIR, exist_ok=True)
    os.makedirs(WORKTREE_DIR, exist_ok=True)

    for url_name, url_val in [
        ("GENERATE_QUEUE_URL", GENERATE_QUEUE_URL),
        ("EVAL_QUEUE_URL", EVAL_QUEUE_URL),
        ("EVAL_DONE_QUEUE_URL", EVAL_DONE_QUEUE_URL),
        ("PIPELINE_DONE_QUEUE_URL", PIPELINE_DONE_QUEUE_URL),
    ]:
        if not url_val:
            log.error("Missing env var: %s", url_name)
            sys.exit(1)

    num_workers = args.parallel
    log.info(
        "Env worker starting %d parallel workers (pid=%d)", num_workers, os.getpid()
    )
    log.info(
        "Port range: %d-%d", BASE_PORT, BASE_PORT + num_workers * SERVERS_PER_ENV - 1
    )

    # Register signal handlers in main process
    signal.signal(signal.SIGTERM, _handle_signal)
    signal.signal(signal.SIGINT, _handle_signal)

    if num_workers == 1:
        # Single worker — run in main process
        worker_loop(0, dry_run=args.dry_run)
    else:
        # Spawn parallel worker processes
        processes = []
        for i in range(num_workers):
            p = multiprocessing.Process(
                target=worker_loop,
                args=(i, args.dry_run),
                name=f"env-worker-{i}",
            )
            p.start()
            processes.append(p)
            log.info("Spawned worker %d (pid=%d)", i, p.pid)

        # Wait for all workers to finish
        try:
            for p in processes:
                p.join()
        except KeyboardInterrupt:
            log.info("Interrupt received, stopping workers...")
            _shutdown = True
            for p in processes:
                p.terminate()
            for p in processes:
                p.join(timeout=30)

    log.info("All workers exited")


if __name__ == "__main__":
    main()
