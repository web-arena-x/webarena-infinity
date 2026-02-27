#!/usr/bin/env python3
"""Post-pipeline result aggregation.

Pulls all env branches, collects results.json from each, and produces a
cross-environment summary with per-difficulty breakdowns.

Usage:
    python infra/collect_results.py                        # all 100 envs
    python infra/collect_results.py --total-envs 5         # small test
    python infra/collect_results.py --output summary.json  # custom output path
"""

from __future__ import annotations

import argparse
import json
import logging
import os
import subprocess
import sys
from datetime import datetime
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_DIR = str(SCRIPT_DIR.parent)
APPS_DIR = str(SCRIPT_DIR.parent / "apps")
GIT_REMOTE = "origin"
BRANCH_PREFIX = ""

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [collect] %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger(__name__)


def git(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["git", *args], cwd=REPO_DIR, capture_output=True, text=True, check=True
    )


def collect_env_results(env_id: str) -> dict | None:
    """Checkout the env branch and find the latest results.json."""
    branch = f"{BRANCH_PREFIX}{env_id.removeprefix(BRANCH_PREFIX)}"
    try:
        git("fetch", GIT_REMOTE, branch)
        git("checkout", branch)
        git("reset", "--hard", f"{GIT_REMOTE}/{branch}")
    except subprocess.CalledProcessError:
        log.warning("Could not checkout branch %s", branch)
        return None

    results_dir = os.path.join(APPS_DIR, env_id, "results")
    if not os.path.isdir(results_dir):
        log.warning("No results/ directory for %s", env_id)
        return None

    # Find all results.json files (one per eval run)
    all_results = []
    for root, dirs, files in os.walk(results_dir):
        for f in files:
            if f == "results.json":
                path = os.path.join(root, f)
                try:
                    with open(path) as fh:
                        data = json.load(fh)
                        data["_source_path"] = path
                        all_results.append(data)
                except (json.JSONDecodeError, OSError) as e:
                    log.warning("Failed to read %s: %s", path, e)

    if not all_results:
        log.warning("No results.json found for %s", env_id)
        return None

    # Return the latest run (by timestamp field)
    all_results.sort(key=lambda r: r.get("timestamp", ""), reverse=True)
    latest = all_results[0]
    latest["env_id"] = env_id
    latest["branch"] = branch
    latest["total_eval_runs"] = len(all_results)
    return latest


def aggregate(env_results: list[dict]) -> dict:
    """Compute cross-environment summary statistics."""
    total_envs = len(env_results)
    total_tasks = sum(r.get("total", 0) for r in env_results)
    total_passed = sum(r.get("passed", 0) for r in env_results)

    pass_rates = [r.get("pass_rate", 0) for r in env_results]
    avg_pass_rate = sum(pass_rates) / len(pass_rates) if pass_rates else 0

    # Per-difficulty aggregation across all envs
    by_difficulty: dict[str, dict] = {}
    for r in env_results:
        for diff, info in r.get("by_difficulty", {}).items():
            by_difficulty.setdefault(diff, {"total": 0, "passed": 0})
            by_difficulty[diff]["total"] += info.get("total", 0)
            by_difficulty[diff]["passed"] += info.get("passed", 0)

    for diff, info in by_difficulty.items():
        info["pass_rate"] = round(
            info["passed"] / info["total"] * 100, 1
        ) if info["total"] else 0

    # Distribution of pass rates
    buckets = {"0-25%": 0, "25-50%": 0, "50-75%": 0, "75-100%": 0}
    for pr in pass_rates:
        if pr < 25:
            buckets["0-25%"] += 1
        elif pr < 50:
            buckets["25-50%"] += 1
        elif pr < 75:
            buckets["50-75%"] += 1
        else:
            buckets["75-100%"] += 1

    return {
        "timestamp": datetime.now().isoformat(),
        "total_environments": total_envs,
        "total_tasks": total_tasks,
        "total_passed": total_passed,
        "overall_pass_rate": round(total_passed / total_tasks * 100, 1) if total_tasks else 0,
        "avg_env_pass_rate": round(avg_pass_rate, 1),
        "min_pass_rate": round(min(pass_rates), 1) if pass_rates else 0,
        "max_pass_rate": round(max(pass_rates), 1) if pass_rates else 0,
        "by_difficulty": by_difficulty,
        "pass_rate_distribution": buckets,
        "environments": [
            {
                "env_id": r["env_id"],
                "pass_rate": r.get("pass_rate", 0),
                "total": r.get("total", 0),
                "passed": r.get("passed", 0),
                "model": r.get("model", "unknown"),
                "total_eval_runs": r.get("total_eval_runs", 0),
            }
            for r in sorted(env_results, key=lambda r: r["env_id"])
        ],
    }


def load_manifest(path: str) -> list[str]:
    """Read env_ids from the JSONL manifest."""
    env_ids = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line:
                env_ids.append(json.loads(line)["env_id"])
    return env_ids


def main() -> None:
    parser = argparse.ArgumentParser(description="Collect and aggregate results across all environments")
    parser.add_argument("--manifest", default=os.path.join(REPO_DIR, "infra", "env_manifest.jsonl"),
                        help="Path to env_manifest.jsonl")
    parser.add_argument("--output", default=None, help="Output JSON path (default: auto-generated)")
    args = parser.parse_args()

    env_ids = load_manifest(args.manifest)
    log.info("Collecting results from %d environments", len(env_ids))

    # Stash any local changes before switching branches
    git("stash")

    env_results = []
    failed_envs = []
    for i, env_id in enumerate(env_ids, 1):
        log.info("Collecting %s (%d/%d)", env_id, i, len(env_ids))
        result = collect_env_results(env_id)
        if result:
            env_results.append(result)
        else:
            failed_envs.append(env_id)

    # Return to main branch
    git("checkout", "main")
    try:
        git("stash", "pop")
    except subprocess.CalledProcessError:
        pass  # no stash to pop

    if not env_results:
        log.error("No results collected from any environment")
        sys.exit(1)

    summary = aggregate(env_results)

    output_path = args.output or f"evaluation/results/cross_env_summary_{datetime.now():%Y%m%d_%H%M%S}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(summary, f, indent=2)

    # Console summary
    log.info("=" * 60)
    log.info("Cross-environment summary:")
    log.info("  Environments collected: %d / %d", len(env_results), len(env_ids))
    if failed_envs:
        log.info("  Failed to collect: %s", ", ".join(failed_envs[:10]))
    log.info("  Total tasks: %d", summary["total_tasks"])
    log.info("  Overall pass rate: %.1f%%", summary["overall_pass_rate"])
    log.info("  Avg env pass rate: %.1f%%", summary["avg_env_pass_rate"])
    log.info("  Range: %.1f%% - %.1f%%", summary["min_pass_rate"], summary["max_pass_rate"])
    for diff in ["easy", "medium", "hard"]:
        if diff in summary["by_difficulty"]:
            info = summary["by_difficulty"][diff]
            log.info("    %s: %d/%d (%.1f%%)", diff, info["passed"], info["total"], info["pass_rate"])
    log.info("  Pass rate distribution: %s", summary["pass_rate_distribution"])
    log.info("  Written to: %s", output_path)
    log.info("=" * 60)


if __name__ == "__main__":
    main()
