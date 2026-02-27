#!/usr/bin/env python3
"""Self-contained single-environment pipeline orchestrator.

Runs the full generate → function-task eval → real-task eval pipeline for
one environment on a single machine.  No SQS, no cross-machine coordination.
For N environments, launch N instances each running this script independently.

Usage:
    # Full pipeline from scratch
    python infra/pipeline.py \\
        --app-name linear-account-settings \\
        --docs-path apps/user-manuals/linear/02-account \\
        --model gemini --workers 4 --repetitions 3

    # Resume with existing app (skip generation)
    python infra/pipeline.py \\
        --app-name gmail \\
        --docs-path apps/user-manuals/gmail/ \\
        --skip-generation --model gemini --workers 2 --repetitions 1

    # Skip function tasks, only do real tasks
    python infra/pipeline.py \\
        --app-name gmail \\
        --docs-path apps/user-manuals/gmail/ \\
        --skip-generation --skip-function-tasks --model gemini
"""

from __future__ import annotations

import argparse
import json
import logging
import os
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_DIR = SCRIPT_DIR.parent
PROMPTS_DIR = SCRIPT_DIR / "prompts"

# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------


def setup_logging(app_name: str) -> logging.Logger:
    """Configure logging to both console and file."""
    log_dir = REPO_DIR / "logs" / app_name
    log_dir.mkdir(parents=True, exist_ok=True)

    logger = logging.getLogger("pipeline")
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s [pipeline] %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Console handler
    console = logging.StreamHandler()
    console.setFormatter(formatter)
    logger.addHandler(console)

    # File handler — combined pipeline log
    file_handler = logging.FileHandler(log_dir / "pipeline.log")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger


log: logging.Logger  # set in main()

# ---------------------------------------------------------------------------
# Prompt template loading
# ---------------------------------------------------------------------------


def load_prompt(name: str, **kwargs: str) -> str:
    """Load a prompt template from infra/prompts/{name}.md and fill placeholders."""
    path = PROMPTS_DIR / f"{name}.md"
    with open(path) as f:
        template = f.read().strip()
    return template.format(**kwargs)


# ---------------------------------------------------------------------------
# Claude CLI invocation
# ---------------------------------------------------------------------------


def run_claude(
    prompt_name: str,
    cwd: str | Path,
    timeout: int = 3600,
    retries: int = 1,
    **template_vars: str,
) -> tuple[int, str, str]:
    """Load prompt template, invoke ``claude --print --dangerously-skip-permissions --permission-mode plan``.

    Returns (returncode, stdout, stderr).
    """
    prompt = load_prompt(prompt_name, **template_vars)
    cwd = str(cwd)

    # Ensure log directory exists
    app_name = Path(cwd).name
    step_log_dir = REPO_DIR / "logs" / app_name
    step_log_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_path = step_log_dir / f"{prompt_name}_{timestamp}.log"

    cmd = [
        "claude",
        "--print",
        "--dangerously-skip-permissions",
        "--permission-mode", "plan",
        "--verbose",
        prompt,
    ]

    for attempt in range(1, retries + 2):
        log.info(
            "Running claude (prompt=%s, cwd=%s, attempt=%d)",
            prompt_name,
            cwd,
            attempt,
        )
        try:
            result = subprocess.run(
                cmd, cwd=cwd, capture_output=True, text=True, timeout=timeout
            )
        except subprocess.TimeoutExpired:
            log.error("Claude timed out after %ds (prompt=%s)", timeout, prompt_name)
            with open(log_path, "w") as f:
                f.write(f"TIMEOUT after {timeout}s\n")
            if attempt <= retries:
                log.info("Retrying...")
                continue
            return (1, "", f"Timeout after {timeout}s")

        # Save output to log file
        with open(log_path, "w") as f:
            f.write(result.stdout)
            if result.stderr:
                f.write("\n--- stderr ---\n")
                f.write(result.stderr)

        if result.returncode != 0:
            log.error(
                "Claude failed (rc=%d, prompt=%s): %s",
                result.returncode,
                prompt_name,
                result.stderr[-500:] if result.stderr else "(no stderr)",
            )
            if attempt <= retries:
                log.info("Retrying...")
                continue

        return (result.returncode, result.stdout, result.stderr)

    # Should not reach here, but just in case
    return (1, "", "All retries exhausted")


# ---------------------------------------------------------------------------
# Evaluation
# ---------------------------------------------------------------------------


def run_eval(
    app_dir: str | Path,
    task_suite: str,
    model: str,
    workers: int,
    repetitions: int,
) -> Path | None:
    """Run evaluation/run_eval_parallel.py as a subprocess.

    Returns the path to the results directory, or None on failure.
    """
    app_dir = Path(app_dir).resolve()
    cmd = [
        sys.executable,
        str(REPO_DIR / "evaluation" / "run_eval_parallel.py"),
        "--web-app", str(app_dir),
        "--task-suite", task_suite,
        "--model", model,
        "--workers", str(workers),
        "--repetitions", str(repetitions),
        "--failed-only",
    ]

    log.info("Running eval: %s", " ".join(cmd))
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=7200)

    # Save eval output to log
    app_name = app_dir.name
    step_log_dir = REPO_DIR / "logs" / app_name
    step_log_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_path = step_log_dir / f"eval_{task_suite}_{timestamp}.log"
    with open(log_path, "w") as f:
        f.write(result.stdout)
        if result.stderr:
            f.write("\n--- stderr ---\n")
            f.write(result.stderr)

    if result.returncode != 0:
        log.error("Eval failed (rc=%d): %s", result.returncode, result.stderr[-500:])
        return None

    # Find the latest results directory
    return find_latest_results(app_dir, task_suite)


def find_latest_results(app_dir: str | Path, task_suite: str) -> Path | None:
    """Find the latest results directory for the given task suite."""
    results_dir = Path(app_dir) / "results"
    if not results_dir.is_dir():
        return None

    suite_tag = f"_{task_suite}" if task_suite != "tasks" else ""

    # Find directories matching the pattern: {model}_{timestamp}{suite_tag}_parallel
    candidates = []
    for d in results_dir.iterdir():
        if d.is_dir() and suite_tag in d.name:
            candidates.append(d)

    if not candidates:
        # Fall back to any directory (in case suite_tag matching fails)
        candidates = [d for d in results_dir.iterdir() if d.is_dir()]

    if not candidates:
        return None

    # Sort by modification time, return most recent
    candidates.sort(key=lambda p: p.stat().st_mtime, reverse=True)
    return candidates[0]


def parse_results(results_dir: Path | None) -> dict:
    """Parse results.json from a results directory.

    Returns dict with keys: pass_rate, passed, total, tasks.
    """
    if results_dir is None:
        return {"pass_rate": 0, "passed": 0, "total": 0, "tasks": {}}

    results_file = results_dir / "results.json"
    if not results_file.exists():
        log.warning("No results.json in %s", results_dir)
        return {"pass_rate": 0, "passed": 0, "total": 0, "tasks": {}}

    with open(results_file) as f:
        data = json.load(f)

    return {
        "pass_rate": data.get("pass_rate", 0),
        "passed": data.get("passed", 0),
        "total": data.get("total", 0),
        "tasks": data.get("tasks", {}),
    }


# ---------------------------------------------------------------------------
# Sanity check
# ---------------------------------------------------------------------------


def run_sanity_check(app_dir: str | Path, variant: str) -> tuple[bool, str]:
    """Run sanity_check_{variant}.py (or sanity_check.py) in app_dir.

    Returns (passed, output).
    """
    app_dir = Path(app_dir)

    # Try variant-specific first, then fall back to generic
    script_name = f"sanity_check_{variant}.py"
    script = app_dir / script_name
    if not script.exists():
        script = app_dir / "sanity_check.py"
        if not script.exists():
            log.warning("No sanity check script found in %s", app_dir)
            return (True, "No sanity check script found — skipping")

    log.info("Running sanity check: %s", script.name)
    try:
        result = subprocess.run(
            [sys.executable, str(script), "--workers", "4"],
            cwd=str(app_dir),
            capture_output=True,
            text=True,
            timeout=300,
        )
    except subprocess.TimeoutExpired:
        return (False, "Sanity check timed out after 300s")

    output = result.stdout
    if result.stderr:
        output += "\n" + result.stderr

    if result.returncode != 0:
        log.warning("Sanity check failed:\n%s", output[-1000:])
        return (False, output)

    log.info("Sanity check passed")
    return (True, output)


# ---------------------------------------------------------------------------
# Git helpers
# ---------------------------------------------------------------------------


def git(*args: str, cwd: str | Path | None = None) -> subprocess.CompletedProcess:
    """Run a git command."""
    cmd = ["git", *args]
    result = subprocess.run(
        cmd, cwd=str(cwd or REPO_DIR), capture_output=True, text=True
    )
    if result.returncode != 0:
        log.error(
            "git %s failed (rc=%d): %s",
            " ".join(args),
            result.returncode,
            result.stderr.strip(),
        )
    return result


def detect_changes(app_dir: str | Path) -> bool:
    """Check if there are uncommitted changes in the app directory."""
    result = subprocess.run(
        ["git", "diff", "--quiet", str(app_dir)],
        cwd=str(REPO_DIR),
        capture_output=True,
    )
    # Also check for untracked files
    untracked = subprocess.run(
        ["git", "ls-files", "--others", "--exclude-standard", str(app_dir)],
        cwd=str(REPO_DIR),
        capture_output=True,
        text=True,
    )
    has_diff = result.returncode != 0
    has_untracked = bool(untracked.stdout.strip())
    return has_diff or has_untracked


def commit_checkpoint(app_dir: str | Path, message: str) -> None:
    """Stage app dir changes and commit with message."""
    app_dir = Path(app_dir)
    git("add", str(app_dir))

    # Check if there's anything staged
    result = subprocess.run(
        ["git", "diff", "--cached", "--quiet"],
        cwd=str(REPO_DIR),
        capture_output=True,
    )
    if result.returncode == 0:
        log.info("No changes to commit")
        return

    git("commit", "-m", message)
    log.info("Committed: %s", message)


def setup_branch(branch: str | None) -> None:
    """Create and/or checkout the specified branch."""
    if branch is None:
        return

    # Check if branch exists locally
    result = git("rev-parse", "--verify", branch)
    if result.returncode != 0:
        # Branch doesn't exist — create it
        git("checkout", "-b", branch)
        log.info("Created and checked out branch: %s", branch)
    else:
        git("checkout", branch)
        log.info("Checked out existing branch: %s", branch)


def git_push() -> None:
    """Push current branch to remote."""
    # Get current branch name
    result = git("rev-parse", "--abbrev-ref", "HEAD")
    branch = result.stdout.strip()
    log.info("Pushing branch %s to origin", branch)
    git("push", "-u", "origin", branch)


# ---------------------------------------------------------------------------
# Main pipeline
# ---------------------------------------------------------------------------


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Self-contained single-environment pipeline orchestrator"
    )
    parser.add_argument(
        "--app-name",
        required=True,
        help="Name for the app (becomes apps/{name}/)",
    )
    parser.add_argument(
        "--docs-path",
        required=True,
        help="Path to source documentation",
    )
    parser.add_argument(
        "--model",
        default="gemini",
        choices=["gemini", "gpt", "claude"],
        help="Eval agent model (default: gemini)",
    )
    parser.add_argument(
        "--workers",
        type=int,
        default=8,
        help="Parallel eval workers (default: 8)",
    )
    parser.add_argument(
        "--repetitions",
        type=int,
        default=3,
        help="Eval repetitions per iteration (default: 3)",
    )
    parser.add_argument(
        "--max-iterations",
        type=int,
        default=5,
        help="Max eval-audit loops per phase (default: 5)",
    )
    parser.add_argument(
        "--skip-generation",
        action="store_true",
        help="Skip app generation (resume from existing app)",
    )
    parser.add_argument(
        "--skip-function-tasks",
        action="store_true",
        help="Skip function task phase entirely",
    )
    parser.add_argument(
        "--skip-real-tasks",
        action="store_true",
        help="Skip real task phase entirely",
    )
    parser.add_argument(
        "--branch",
        default=None,
        help="Git branch to work on (created if needed; defaults to current branch)",
    )
    parser.add_argument(
        "--push",
        action="store_true",
        help="Push branch to remote after completion",
    )
    args = parser.parse_args()

    # Set up logging
    global log
    log = setup_logging(args.app_name)

    app_dir = REPO_DIR / "apps" / args.app_name
    max_iterations = args.max_iterations

    log.info("=" * 60)
    log.info("Pipeline starting for: %s", args.app_name)
    log.info("  docs-path:       %s", args.docs_path)
    log.info("  model:           %s", args.model)
    log.info("  workers:         %d", args.workers)
    log.info("  repetitions:     %d", args.repetitions)
    log.info("  max-iterations:  %d", max_iterations)
    log.info("  skip-generation: %s", args.skip_generation)
    log.info("  skip-func-tasks: %s", args.skip_function_tasks)
    log.info("  skip-real-tasks: %s", args.skip_real_tasks)
    log.info("  branch:          %s", args.branch or "(current)")
    log.info("  push:            %s", args.push)
    log.info("=" * 60)

    # Set up branch if specified
    if args.branch:
        setup_branch(args.branch)

    # ── Phase 1: Generate App ──────────────────────────────────────────

    if not args.skip_generation:
        log.info("Phase 1: Generating web app")
        app_dir.mkdir(parents=True, exist_ok=True)

        rc, stdout, stderr = run_claude(
            "generate-app",
            cwd=REPO_DIR,
            timeout=3600,
            docs_source=args.docs_path,
        )
        if rc != 0:
            log.error("Phase 1 FAILED: app generation returned rc=%d", rc)
            sys.exit(1)

        commit_checkpoint(app_dir, f"Generate app: {args.app_name}")
        log.info("Phase 1 complete: app generated")
    else:
        log.info("Phase 1: Skipped (--skip-generation)")
        if not app_dir.is_dir():
            log.error("App directory does not exist: %s", app_dir)
            sys.exit(1)

    # ── Phase 2: Function Tasks ────────────────────────────────────────

    if not args.skip_function_tasks:
        log.info("Phase 2: Function task evaluation")

        # 2a: Generate function tasks (once)
        log.info("Phase 2a: Generating function tasks")
        rc, stdout, stderr = run_claude(
            "generate-function-tests",
            cwd=REPO_DIR,
            timeout=3600,
            **{"app-name": args.app_name},
        )
        if rc != 0:
            log.error("Phase 2a FAILED: function task generation returned rc=%d", rc)
            sys.exit(1)

        ok, output = run_sanity_check(app_dir, "function")
        if not ok:
            log.info("Sanity check failed after function task generation — fixing")
            run_claude(
                "fix-sanity-check",
                cwd=REPO_DIR,
                timeout=1800,
                output=output[-3000:],
                variant="function",
                **{"app-name": args.app_name},
            )

        commit_checkpoint(app_dir, f"Generate function tasks: {args.app_name}")

        # 2b: Eval → Audit loop
        for iteration in range(1, max_iterations + 1):
            log.info(
                "Phase 2b: Function task iteration %d/%d",
                iteration,
                max_iterations,
            )

            results_dir = run_eval(
                app_dir, "function-tasks", args.model, args.workers, args.repetitions
            )
            results = parse_results(results_dir)
            log.info(
                "Function task pass rate: %.1f%% (%d/%d)",
                results["pass_rate"],
                results["passed"],
                results["total"],
            )

            if results["pass_rate"] == 100:
                log.info("All function tasks passed!")
                break

            if results_dir is None:
                log.warning("No results directory — skipping audit")
                break

            log.info("Running audit on function task failures")
            run_claude(
                "audit-function-tests",
                cwd=REPO_DIR,
                timeout=3600,
                evaluation_result_path=str(results_dir),
            )

            if not detect_changes(app_dir):
                log.info(
                    "Audit made no changes — remaining failures are agent-side"
                )
                break

            # Re-check sanity after audit changes
            ok, output = run_sanity_check(app_dir, "function")
            commit_checkpoint(
                app_dir,
                f"Function task audit iter {iteration}: {args.app_name}",
            )

        log.info("Phase 2 complete")
    else:
        log.info("Phase 2: Skipped (--skip-function-tasks)")

    # ── Phase 3: Real Tasks ────────────────────────────────────────────

    if not args.skip_real_tasks:
        log.info("Phase 3: Real task evaluation")

        # 3a: Generate real tasks (once)
        log.info("Phase 3a: Generating real tasks")
        rc, stdout, stderr = run_claude(
            "generate-real-tasks",
            cwd=REPO_DIR,
            timeout=3600,
            **{"app-name": args.app_name},
        )
        if rc != 0:
            log.error("Phase 3a FAILED: real task generation returned rc=%d", rc)
            sys.exit(1)

        ok, output = run_sanity_check(app_dir, "real")
        if not ok:
            log.info("Sanity check failed after real task generation — fixing")
            run_claude(
                "fix-sanity-check",
                cwd=REPO_DIR,
                timeout=1800,
                output=output[-3000:],
                variant="real",
                **{"app-name": args.app_name},
            )

        commit_checkpoint(app_dir, f"Generate real tasks: {args.app_name}")

        # 3b: Eval → Audit loop
        for iteration in range(1, max_iterations + 1):
            log.info(
                "Phase 3b: Real task iteration %d/%d",
                iteration,
                max_iterations,
            )

            results_dir = run_eval(
                app_dir, "tasks", args.model, args.workers, args.repetitions
            )
            results = parse_results(results_dir)
            log.info(
                "Real task pass rate: %.1f%% (%d/%d)",
                results["pass_rate"],
                results["passed"],
                results["total"],
            )

            if results["pass_rate"] == 100:
                log.info("All real tasks passed!")
                break

            if results_dir is None:
                log.warning("No results directory — skipping audit")
                break

            log.info("Running audit on real task failures")
            run_claude(
                "audit-real-tasks",
                cwd=REPO_DIR,
                timeout=3600,
                evaluation_result_path=str(results_dir),
            )

            if not detect_changes(app_dir):
                log.info(
                    "Audit made no changes — remaining failures are agent-side"
                )
                break

            # Re-check sanity after audit changes
            ok, output = run_sanity_check(app_dir, "real")
            commit_checkpoint(
                app_dir,
                f"Real task audit iter {iteration}: {args.app_name}",
            )

        log.info("Phase 3 complete")
    else:
        log.info("Phase 3: Skipped (--skip-real-tasks)")

    # ── Done ───────────────────────────────────────────────────────────

    if args.push:
        git_push()

    log.info("=" * 60)
    log.info("Pipeline complete for: %s", args.app_name)
    log.info("=" * 60)


if __name__ == "__main__":
    main()
