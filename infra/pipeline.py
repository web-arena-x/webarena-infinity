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

    # Resume after a crash (picks up from saved state)
    python infra/pipeline.py \\
        --app-name gitlab-plan-and-track \\
        --docs-path apps/user-manuals/gitlab/plan-and-track/ \\
        --model gemini --workers 8 --resume
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
    resume: bool = False,
    task_id_filter: str | None = None,
) -> Path | None:
    """Run evaluation/run_eval_parallel.py as a subprocess.

    Args:
        task_id_filter: Optional comma-separated task IDs to evaluate
            (passed as --task-id to the eval runner).

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

    if task_id_filter:
        cmd.extend(["--task-id", task_id_filter])

    # If resuming, check for a partial results directory to resume into
    if resume:
        partial_dir = find_partial_results(app_dir, task_suite)
        if partial_dir:
            cmd.extend(["--resume-dir", str(partial_dir)])
            log.info("Found partial results dir to resume: %s", partial_dir)

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


def find_partial_results(app_dir: str | Path, task_suite: str) -> Path | None:
    """Find a results dir that has runN/ subdirs but no top-level results.json (partial eval)."""
    results_dir = Path(app_dir) / "results"
    if not results_dir.is_dir():
        return None

    suite_tag = f"_{task_suite}" if task_suite != "tasks" else ""

    candidates = []
    for d in results_dir.iterdir():
        if not d.is_dir() or suite_tag not in d.name:
            continue
        # Must lack a top-level results.json (incomplete eval)
        if (d / "results.json").exists():
            continue
        # Must have at least one runN/ subdir to be a multi-run eval
        has_run_dir = any(
            sub.is_dir() and sub.name.startswith("run") for sub in d.iterdir()
        )
        if has_run_dir:
            candidates.append(d)

    if not candidates:
        return None

    # Return most recent by modification time
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
# Pipeline state persistence (for --resume)
# ---------------------------------------------------------------------------

PHASE_ORDER = {
    "phase_1": 1,
    "phase_2a": 2,
    "phase_2b": 3,
    "phase_3a": 4,
    "phase_3b": 5,
    "phase_4a": 6,
    "phase_4b": 7,
    "done": 8,
}


def _state_file_path(app_name: str) -> Path:
    """Return path to the pipeline state file for an app."""
    return REPO_DIR / "logs" / app_name / "pipeline_state.json"


def save_state(
    app_name: str,
    step: str,
    iteration: int = 0,
    args: argparse.Namespace | None = None,
) -> None:
    """Write current pipeline state to disk.

    Called BEFORE each major operation so that on crash + resume, we know
    exactly where to pick up.
    """
    result = git("rev-parse", "HEAD")
    last_good_commit = result.stdout.strip()

    state = {
        "step": step,
        "iteration": iteration,
        "last_good_commit": last_good_commit,
        "app_name": app_name,
        "timestamp": datetime.now().isoformat(timespec="seconds"),
    }
    if args is not None:
        state["pipeline_args"] = {
            "model": args.model,
            "workers": args.workers,
            "repetitions": args.repetitions,
            "max_iterations": args.max_iterations,
            "docs_path": args.docs_path,
            "hardening_rounds": getattr(args, "hardening_rounds", 3),
            "tasks_per_round": getattr(args, "tasks_per_round", 20),
            "target_pass_rate": getattr(args, "target_pass_rate", None),
        }

    path = _state_file_path(app_name)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        json.dump(state, f, indent=2)
    log.info("Saved pipeline state: step=%s, iteration=%d", step, iteration)


def load_state(app_name: str) -> dict | None:
    """Read pipeline state from disk. Returns None if missing or corrupt."""
    path = _state_file_path(app_name)
    if not path.exists():
        return None
    try:
        with open(path) as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError) as e:
        log.warning("Could not load state file %s: %s", path, e)
        return None


def clear_state(app_name: str) -> None:
    """Delete the state file on successful completion."""
    path = _state_file_path(app_name)
    if path.exists():
        path.unlink()
        log.info("Cleared pipeline state file")


# ---------------------------------------------------------------------------
# Task hardening helpers
# ---------------------------------------------------------------------------


def load_task_ids(tasks_file: Path) -> set[str]:
    """Read tasks.json and return the set of task IDs."""
    if not tasks_file.exists():
        return set()
    with open(tasks_file) as f:
        tasks = json.load(f)
    return {t["id"] for t in tasks}


def get_new_task_ids(tasks_file: Path, known_ids: set[str]) -> set[str]:
    """Return task IDs in tasks_file that are not in known_ids."""
    current_ids = load_task_ids(tasks_file)
    return current_ids - known_ids


def build_hardening_analysis(
    results_dir: Path | None, tasks_file: Path
) -> str:
    """Build a text summary of evaluation results for the hardening prompt.

    Reads results.json for per-task metrics, computes per-difficulty pass rates,
    and identifies easy wins vs hard failures. Includes the results_dir path so
    Claude can read history.json files for behavioral analysis.
    """
    if results_dir is None:
        return "No previous evaluation results available."

    results_file = results_dir / "results.json"
    if not results_file.exists():
        return "No results.json found in the latest results directory."

    with open(results_file) as f:
        data = json.load(f)

    lines = []
    lines.append(f"Overall pass rate: {data.get('pass_rate', 0)}%")
    lines.append(f"Total tasks: {data.get('total', 0)}, Passed: {data.get('passed', 0)}")
    lines.append("")

    # Per-difficulty breakdown
    by_diff = data.get("by_difficulty", {})
    if by_diff:
        lines.append("Per-difficulty pass rates:")
        for diff in ["easy", "medium", "hard"]:
            if diff in by_diff:
                info = by_diff[diff]
                total = info["total"]
                passed = info["passed"]
                pct = round(passed / total * 100, 1) if total else 0
                lines.append(f"  {diff}: {passed}/{total} ({pct}%)")
        lines.append("")

    # Per-task details
    task_results = data.get("tasks", [])
    if task_results:
        easy_wins = []
        hard_fails = []
        for t in task_results:
            tid = t.get("task_id", "")
            passed = t.get("passed", False)
            steps = t.get("steps", -1)
            elapsed = t.get("elapsed", 0)
            diff = t.get("difficulty", "")
            if passed and steps > 0 and steps <= 10:
                easy_wins.append(f"  {tid} ({diff}): {steps} steps, {elapsed}s")
            elif not passed:
                msg = t.get("verifier_message", "")[:80]
                hard_fails.append(f"  {tid} ({diff}): {msg}")

        if easy_wins:
            lines.append("Easy wins (passed in <=10 steps — agent found these trivial):")
            lines.extend(easy_wins[:20])
            lines.append("")

        if hard_fails:
            lines.append("Failures (agent could not solve these):")
            lines.extend(hard_fails[:30])
            lines.append("")

    lines.append(f"Results directory (read history.json files here): {results_dir}")
    return "\n".join(lines)


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
    parser.add_argument(
        "--resume",
        action="store_true",
        help="Resume from last saved pipeline state (reads logs/{app}/pipeline_state.json)",
    )
    parser.add_argument(
        "--skip-hardening",
        action="store_true",
        help="Skip Phase 4 (task hardening) entirely",
    )
    parser.add_argument(
        "--hardening-rounds",
        type=int,
        default=3,
        help="Number of hardening rounds (default: 3)",
    )
    parser.add_argument(
        "--tasks-per-round",
        type=int,
        default=20,
        help="Number of new tasks to generate per hardening round (default: 20)",
    )
    parser.add_argument(
        "--target-pass-rate",
        type=float,
        default=None,
        help="Optional: stop hardening if overall pass rate drops to this %% (default: disabled)",
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
    log.info("  skip-hardening:  %s", args.skip_hardening)
    log.info("  hardening-rounds:%d", args.hardening_rounds)
    log.info("  tasks-per-round: %d", args.tasks_per_round)
    log.info("  target-pass-rate:%s", args.target_pass_rate or "disabled")
    log.info("  branch:          %s", args.branch or "(current)")
    log.info("  push:            %s", args.push)
    log.info("  resume:          %s", args.resume)
    log.info("=" * 60)

    # Set up branch if specified
    if args.branch:
        setup_branch(args.branch)

    # ── Resume handling ───────────────────────────────────────────────

    resume_phase: str | None = None
    resume_iter: int = 0

    if args.resume:
        state = load_state(args.app_name)
        if state is None:
            log.error("--resume specified but no state file found for %s", args.app_name)
            sys.exit(1)

        resume_phase = state["step"]
        resume_iter = state.get("iteration", 0)
        log.info(
            "Resuming from step=%s, iteration=%d (last_good_commit=%s)",
            resume_phase,
            resume_iter,
            state.get("last_good_commit", "unknown"),
        )

        # Warn if pipeline args differ from original run
        saved_args = state.get("pipeline_args", {})
        for key in ("model", "workers", "repetitions"):
            saved_val = saved_args.get(key)
            current_val = getattr(args, key, None)
            if saved_val is not None and saved_val != current_val:
                log.warning(
                    "Arg mismatch: saved %s=%s, current %s=%s",
                    key, saved_val, key, current_val,
                )

        # Discard any partial changes from the crashed run
        log.info("Resetting working tree to HEAD")
        git("reset", "--hard", "HEAD")

    def should_run(phase: str) -> bool:
        """Return True if this phase should run given resume state."""
        if resume_phase is None:
            return True
        return PHASE_ORDER.get(phase, 0) >= PHASE_ORDER.get(resume_phase, 0)

    # ── Phase 1: Generate App ──────────────────────────────────────────

    if not args.skip_generation and should_run("phase_1"):
        log.info("Phase 1: Generating web app")
        save_state(args.app_name, "phase_1", args=args)
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
        if args.skip_generation:
            log.info("Phase 1: Skipped (--skip-generation)")
        else:
            log.info("Phase 1: Skipped (resuming past this phase)")
        if not app_dir.is_dir():
            log.error("App directory does not exist: %s", app_dir)
            sys.exit(1)

    # ── Phase 2: Function Tasks ────────────────────────────────────────

    if not args.skip_function_tasks:
        log.info("Phase 2: Function task evaluation")

        # 2a: Generate function tasks (once)
        if should_run("phase_2a"):
            log.info("Phase 2a: Generating function tasks")
            save_state(args.app_name, "phase_2a", args=args)
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
        else:
            log.info("Phase 2a: Skipped (resuming past this phase)")

        # 2b: Eval → Audit loop
        if should_run("phase_2b"):
            start_iter = resume_iter if resume_phase == "phase_2b" else 1
            for iteration in range(start_iter, max_iterations + 1):
                log.info(
                    "Phase 2b: Function task iteration %d/%d",
                    iteration,
                    max_iterations,
                )
                save_state(args.app_name, "phase_2b", iteration=iteration, args=args)

                results_dir = run_eval(
                    app_dir, "function-tasks", args.model, args.workers, args.repetitions,
                    resume=(args.resume and iteration == start_iter),
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
        if should_run("phase_3a"):
            log.info("Phase 3a: Generating real tasks")
            save_state(args.app_name, "phase_3a", args=args)
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
        else:
            log.info("Phase 3a: Skipped (resuming past this phase)")

        # 3b: Eval → Audit loop
        if should_run("phase_3b"):
            start_iter = resume_iter if resume_phase == "phase_3b" else 1
            for iteration in range(start_iter, max_iterations + 1):
                log.info(
                    "Phase 3b: Real task iteration %d/%d",
                    iteration,
                    max_iterations,
                )
                save_state(args.app_name, "phase_3b", iteration=iteration, args=args)

                results_dir = run_eval(
                    app_dir, "tasks", args.model, args.workers, args.repetitions,
                    resume=(args.resume and iteration == start_iter),
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

    # ── Phase 4: Task Hardening ───────────────────────────────────────

    if not args.skip_hardening:
        log.info("Phase 4: Task hardening (%d rounds)", args.hardening_rounds)

        # Determine starting round on resume
        hardening_start_round = 1
        hardening_start_audit_iter = 1
        if resume_phase in ("phase_4a", "phase_4b"):
            # iteration is encoded as round * 100 + audit_iter
            hardening_start_round = max(1, resume_iter // 100)
            hardening_start_audit_iter = resume_iter % 100 or 1

        for round_num in range(hardening_start_round, args.hardening_rounds + 1):
            log.info(
                "Phase 4: Hardening round %d/%d",
                round_num,
                args.hardening_rounds,
            )

            # --- 4a: Analyze + Generate ---
            skip_4a = (
                resume_phase == "phase_4b"
                and round_num == hardening_start_round
            )
            if not skip_4a:
                save_state(
                    args.app_name, "phase_4a",
                    iteration=round_num * 100, args=args,
                )

                # Snapshot current task IDs before generation
                known_ids = load_task_ids(app_dir / "tasks.json")

                # Get latest results for context
                results_dir = find_latest_results(app_dir, "tasks")
                analysis = build_hardening_analysis(
                    results_dir, app_dir / "tasks.json"
                )

                rc, stdout, stderr = run_claude(
                    "harden-tasks",
                    cwd=REPO_DIR,
                    timeout=3600,
                    hardening_analysis=analysis,
                    results_path=str(results_dir) if results_dir else "none",
                    round_number=str(round_num),
                    tasks_per_round=str(args.tasks_per_round),
                    **{"app-name": args.app_name},
                )
                if rc != 0:
                    log.error(
                        "Phase 4a FAILED: task hardening generation returned rc=%d",
                        rc,
                    )
                    break

                # Identify newly added task IDs
                new_ids = get_new_task_ids(app_dir / "tasks.json", known_ids)
                if not new_ids:
                    log.info("No new tasks generated — stopping hardening")
                    break

                log.info("Generated %d new tasks: %s", len(new_ids), sorted(new_ids))

                # Sanity check
                ok, output = run_sanity_check(app_dir, "real")
                if not ok:
                    log.info("Sanity check failed after hardening generation — fixing")
                    run_claude(
                        "fix-sanity-check",
                        cwd=REPO_DIR,
                        timeout=1800,
                        output=output[-3000:],
                        variant="real",
                        **{"app-name": args.app_name},
                    )
                    ok2, _ = run_sanity_check(app_dir, "real")
                    if not ok2:
                        log.error(
                            "Sanity check still failing after fix — reverting round %d",
                            round_num,
                        )
                        git("checkout", "--", str(app_dir))
                        break

                commit_checkpoint(
                    app_dir,
                    f"Hardening round {round_num}: {args.app_name}",
                )
            else:
                # Resuming into phase_4b — recompute new_ids from last commit
                log.info(
                    "Phase 4a: Skipped (resuming into phase_4b, round %d)",
                    round_num,
                )
                # We need the known_ids from before this round's generation.
                # Since 4a already committed, all current IDs are "known" from
                # git's perspective, but we need the new ones for eval filtering.
                # Read the commit message to find what was added, or just eval
                # all tasks in this round.  Safest: re-read and eval all tasks.
                new_ids = None  # Will skip task_id_filter → eval all tasks

            # --- 4b: Eval-Audit loop (new tasks only) ---
            task_id_filter = (
                ",".join(sorted(new_ids)) if new_ids else None
            )
            start_iter = (
                hardening_start_audit_iter
                if resume_phase == "phase_4b" and round_num == hardening_start_round
                else 1
            )

            for iteration in range(start_iter, max_iterations + 1):
                log.info(
                    "Phase 4b: Round %d, audit iteration %d/%d",
                    round_num,
                    iteration,
                    max_iterations,
                )
                save_state(
                    args.app_name, "phase_4b",
                    iteration=round_num * 100 + iteration, args=args,
                )

                results_dir = run_eval(
                    app_dir, "tasks", args.model, args.workers,
                    args.repetitions,
                    resume=(args.resume and iteration == start_iter
                            and round_num == hardening_start_round),
                    task_id_filter=task_id_filter,
                )
                results = parse_results(results_dir)
                log.info(
                    "Hardening round %d eval: %.1f%% (%d/%d)",
                    round_num,
                    results["pass_rate"],
                    results["passed"],
                    results["total"],
                )

                if results["pass_rate"] == 100:
                    log.info("All new tasks pass — moving to next round")
                    break

                if results_dir is None:
                    log.warning("No results directory — skipping audit")
                    break

                log.info("Running audit on hardening round %d failures", round_num)
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
                    f"Hardening round {round_num} audit iter {iteration}: {args.app_name}",
                )

            # Optional: check overall pass rate with full suite eval
            if args.target_pass_rate is not None:
                log.info("Running full suite eval to check overall pass rate")
                full_results_dir = run_eval(
                    app_dir, "tasks", args.model, args.workers,
                    args.repetitions,
                )
                full_results = parse_results(full_results_dir)
                log.info(
                    "Full suite pass rate: %.1f%%", full_results["pass_rate"]
                )
                if full_results["pass_rate"] <= args.target_pass_rate:
                    log.info(
                        "Target pass rate reached (%.1f%% <= %.1f%%) — stopping hardening",
                        full_results["pass_rate"],
                        args.target_pass_rate,
                    )
                    break

        log.info("Phase 4 complete")
    else:
        log.info("Phase 4: Skipped (--skip-hardening)")

    # ── Done ───────────────────────────────────────────────────────────

    save_state(args.app_name, "done", args=args)
    clear_state(args.app_name)

    if args.push:
        git_push()

    log.info("=" * 60)
    log.info("Pipeline complete for: %s", args.app_name)
    log.info("=" * 60)


if __name__ == "__main__":
    main()
