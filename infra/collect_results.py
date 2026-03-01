#!/usr/bin/env python3
"""Post-pipeline result aggregation via S3.

Enumerates results stored in S3, downloads each results.json, aggregates
cross-environment statistics, generates a browsable index.html dashboard,
and uploads both to the bucket root.

Usage:
    python infra/collect_results.py --s3-bucket mirror-mirror-results
    python infra/collect_results.py --s3-bucket mirror-mirror-results --output summary.json
"""

from __future__ import annotations

import argparse
import json
import logging
import os
import subprocess
import sys
import tempfile
from datetime import datetime
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_DIR = str(SCRIPT_DIR.parent)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [collect] %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger(__name__)


def get_region() -> str:
    """Return the AWS region."""
    region = os.environ.get("AWS_REGION") or os.environ.get("AWS_DEFAULT_REGION")
    if region:
        return region
    try:
        result = subprocess.run(
            ["aws", "configure", "get", "region"],
            capture_output=True, text=True, check=True,
        )
        return result.stdout.strip() or "us-east-1"
    except (subprocess.CalledProcessError, FileNotFoundError):
        return "us-east-1"


def s3_list_env_ids(bucket: str) -> list[str]:
    """List top-level prefixes (env_ids) in the bucket."""
    cmd = [
        "aws", "s3", "ls", f"s3://{bucket}/",
        "--region", get_region(),
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    except subprocess.CalledProcessError as e:
        log.error("Failed to list bucket: %s", e)
        return []

    env_ids = []
    for line in result.stdout.strip().splitlines():
        # s3 ls output for prefixes: "                           PRE env_id/"
        line = line.strip()
        if line.startswith("PRE ") and line.endswith("/"):
            env_id = line[4:].rstrip("/")
            # Skip files like index.html or summary.json (no PRE prefix for objects)
            if env_id:
                env_ids.append(env_id)
    return env_ids


def s3_list_results_jsons(bucket: str, env_id: str) -> list[str]:
    """List all results.json S3 keys under an env_id prefix."""
    cmd = [
        "aws", "s3", "ls", f"s3://{bucket}/{env_id}/",
        "--recursive", "--region", get_region(),
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    except subprocess.CalledProcessError:
        return []

    keys = []
    for line in result.stdout.strip().splitlines():
        # Format: "2024-01-01 12:00:00    1234 env_id/run_dir/results.json"
        parts = line.strip().split()
        if len(parts) >= 4:
            key = parts[-1]
            if key.endswith("/results.json"):
                keys.append(key)
    return keys


def s3_download_json(bucket: str, key: str) -> dict | None:
    """Download a JSON file from S3 and return parsed contents."""
    with tempfile.NamedTemporaryFile(suffix=".json", delete=True) as tmp:
        cmd = [
            "aws", "s3", "cp",
            f"s3://{bucket}/{key}", tmp.name,
            "--region", get_region(),
        ]
        try:
            subprocess.run(cmd, capture_output=True, text=True, check=True)
            with open(tmp.name) as f:
                return json.load(f)
        except (subprocess.CalledProcessError, json.JSONDecodeError, OSError) as e:
            log.warning("Failed to download %s: %s", key, e)
            return None


def collect_env_results(bucket: str, env_id: str) -> dict | None:
    """Download all results.json for an env and return the latest."""
    keys = s3_list_results_jsons(bucket, env_id)
    if not keys:
        log.warning("No results.json found for %s", env_id)
        return None

    all_results = []
    for key in keys:
        data = s3_download_json(bucket, key)
        if data:
            data["_source_key"] = key
            all_results.append(data)

    if not all_results:
        log.warning("No valid results.json for %s", env_id)
        return None

    # Return the latest run (by timestamp field)
    all_results.sort(key=lambda r: r.get("timestamp", ""), reverse=True)
    latest = all_results[0]
    latest["env_id"] = env_id
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


def generate_index_html(summary: dict, bucket: str) -> str:
    """Generate a static index.html dashboard from the summary."""
    region = get_region()
    base_url = f"http://{bucket}.s3-website-{region}.amazonaws.com"

    env_rows = []
    for env in summary["environments"]:
        env_id = env["env_id"]
        pass_rate = env["pass_rate"]
        total = env["total"]
        passed = env["passed"]
        model = env["model"]
        runs = env["total_eval_runs"]

        # Color based on pass rate
        if pass_rate >= 75:
            badge_class = "badge-green"
        elif pass_rate >= 50:
            badge_class = "badge-yellow"
        else:
            badge_class = "badge-red"

        env_rows.append(
            f'<tr>'
            f'<td><a href="{base_url}/{env_id}/">{env_id}</a></td>'
            f'<td>{model}</td>'
            f'<td>{passed}/{total}</td>'
            f'<td><span class="badge {badge_class}">{pass_rate:.1f}%</span></td>'
            f'<td>{runs}</td>'
            f'</tr>'
        )

    # Difficulty breakdown
    diff_rows = []
    for diff in ["easy", "medium", "hard"]:
        if diff in summary.get("by_difficulty", {}):
            info = summary["by_difficulty"][diff]
            diff_rows.append(
                f'<tr>'
                f'<td style="text-transform:capitalize">{diff}</td>'
                f'<td>{info["passed"]}/{info["total"]}</td>'
                f'<td>{info["pass_rate"]:.1f}%</td>'
                f'</tr>'
            )

    timestamp = summary.get("timestamp", "")

    return f"""\
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Mirror-Mirror Results</title>
<style>
  body {{
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    max-width: 960px; margin: 0 auto; padding: 40px 20px; background: #f8f9fa;
    color: #1a1a2e;
  }}
  h1 {{ margin-bottom: 4px; }}
  .subtitle {{ color: #666; margin-bottom: 24px; }}
  .stats {{
    display: flex; gap: 16px; margin-bottom: 24px; flex-wrap: wrap;
  }}
  .stat-card {{
    background: #fff; border-radius: 8px; padding: 16px 24px;
    box-shadow: 0 1px 3px rgba(0,0,0,.1); min-width: 140px;
  }}
  .stat-card .label {{ color: #666; font-size: .85em; margin-bottom: 4px; }}
  .stat-card .value {{ font-size: 1.5em; font-weight: 700; }}
  table {{
    width: 100%; border-collapse: collapse; background: #fff;
    border-radius: 8px; overflow: hidden;
    box-shadow: 0 1px 3px rgba(0,0,0,.1); margin-bottom: 24px;
  }}
  th, td {{ padding: 12px 16px; text-align: left; border-bottom: 1px solid #eee; }}
  th {{ background: #1a1a2e; color: #fff; }}
  tr:hover {{ background: #f1f3f5; }}
  a {{ color: #0066cc; text-decoration: none; }}
  a:hover {{ text-decoration: underline; }}
  .badge {{
    padding: 3px 10px; border-radius: 12px; font-size: .85em; font-weight: 600;
  }}
  .badge-green {{ background: #e8f5e9; color: #2e7d32; }}
  .badge-yellow {{ background: #fff8e1; color: #f57f17; }}
  .badge-red {{ background: #ffebee; color: #c62828; }}
  .section {{ margin-top: 32px; }}
  .section h2 {{ margin-bottom: 12px; }}
</style>
</head>
<body>
<h1>Mirror-Mirror Results</h1>
<p class="subtitle">Updated: {timestamp} &mdash; {summary["total_environments"]} environments</p>

<div class="stats">
  <div class="stat-card">
    <div class="label">Overall Pass Rate</div>
    <div class="value">{summary["overall_pass_rate"]:.1f}%</div>
  </div>
  <div class="stat-card">
    <div class="label">Total Tasks</div>
    <div class="value">{summary["total_tasks"]}</div>
  </div>
  <div class="stat-card">
    <div class="label">Passed</div>
    <div class="value">{summary["total_passed"]}</div>
  </div>
  <div class="stat-card">
    <div class="label">Avg Env Rate</div>
    <div class="value">{summary["avg_env_pass_rate"]:.1f}%</div>
  </div>
</div>

<div class="section">
  <h2>By Difficulty</h2>
  <table>
    <tr><th>Difficulty</th><th>Passed/Total</th><th>Rate</th></tr>
    {"".join(diff_rows)}
  </table>
</div>

<div class="section">
  <h2>Environments</h2>
  <table>
    <tr><th>Environment</th><th>Model</th><th>Passed/Total</th><th>Pass Rate</th><th>Runs</th></tr>
    {"".join(env_rows)}
  </table>
</div>
</body>
</html>"""


def s3_upload_file(local_path: str, bucket: str, key: str) -> bool:
    """Upload a local file to S3."""
    cmd = [
        "aws", "s3", "cp", local_path,
        f"s3://{bucket}/{key}",
        "--region", get_region(),
    ]
    # Set content type for HTML
    if key.endswith(".html"):
        cmd.extend(["--content-type", "text/html"])
    try:
        subprocess.run(cmd, capture_output=True, text=True, check=True)
        return True
    except subprocess.CalledProcessError as e:
        log.error("Failed to upload %s: %s", key, e)
        return False


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Collect and aggregate results from S3 across all environments"
    )
    parser.add_argument(
        "--s3-bucket",
        default=os.environ.get("MM_S3_BUCKET", "mirror-mirror-results"),
        help="S3 bucket name (default: MM_S3_BUCKET or mirror-mirror-results)",
    )
    parser.add_argument(
        "--output", default=None,
        help="Output JSON path (default: auto-generated)",
    )
    parser.add_argument(
        "--env-ids", nargs="*", default=None,
        help="Specific env IDs to collect (default: all found in bucket)",
    )
    args = parser.parse_args()

    # Discover environments from S3
    if args.env_ids:
        env_ids = args.env_ids
    else:
        log.info("Listing environments in s3://%s/ ...", args.s3_bucket)
        env_ids = s3_list_env_ids(args.s3_bucket)

    if not env_ids:
        log.error("No environments found in bucket %s", args.s3_bucket)
        sys.exit(1)

    log.info("Collecting results from %d environments", len(env_ids))

    env_results = []
    failed_envs = []
    for i, env_id in enumerate(env_ids, 1):
        log.info("Collecting %s (%d/%d)", env_id, i, len(env_ids))
        result = collect_env_results(args.s3_bucket, env_id)
        if result:
            env_results.append(result)
        else:
            failed_envs.append(env_id)

    if not env_results:
        log.error("No results collected from any environment")
        sys.exit(1)

    summary = aggregate(env_results)

    # Write summary locally
    output_path = args.output or f"evaluation/results/cross_env_summary_{datetime.now():%Y%m%d_%H%M%S}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(summary, f, indent=2)

    # Upload summary.json and index.html to bucket root
    log.info("Uploading summary.json to s3://%s/summary.json", args.s3_bucket)
    s3_upload_file(output_path, args.s3_bucket, "summary.json")

    log.info("Generating and uploading index.html dashboard")
    index_html = generate_index_html(summary, args.s3_bucket)
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".html", delete=True
    ) as tmp:
        tmp.write(index_html)
        tmp.flush()
        s3_upload_file(tmp.name, args.s3_bucket, "index.html")

    region = get_region()
    dashboard_url = f"http://{args.s3_bucket}.s3-website-{region}.amazonaws.com/"

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
    log.info("  Dashboard: %s", dashboard_url)
    log.info("=" * 60)


if __name__ == "__main__":
    main()
