#!/usr/bin/env python3
"""Upload one app's results to S3.

Uses ``aws s3 sync`` (subprocess) so there is no boto3 dependency.

Usage:
    python infra/upload_results.py --app-dir apps/linear --env-id linear
    python infra/upload_results.py --app-dir apps/linear --env-id linear --s3-bucket my-bucket
"""

from __future__ import annotations

import argparse
import logging
import os
import subprocess
import sys
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [upload] %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger(__name__)


def get_region() -> str:
    """Return the AWS region, preferring env var, falling back to CLI config."""
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


def upload_results(app_dir: str | Path, bucket: str, env_id: str) -> bool:
    """Sync ``<app_dir>/results/`` to ``s3://<bucket>/<env_id>/``.

    Returns True on success, False on failure.
    """
    app_dir = Path(app_dir)
    results_dir = app_dir / "results"

    if not results_dir.is_dir():
        log.warning("No results directory at %s — nothing to upload", results_dir)
        return False

    s3_dest = f"s3://{bucket}/{env_id}/"
    region = get_region()
    website_url = f"http://{bucket}.s3-website-{region}.amazonaws.com/{env_id}/"

    log.info("Uploading results: %s -> %s", results_dir, s3_dest)

    cmd = [
        "aws", "s3", "sync",
        str(results_dir),
        s3_dest,
        "--size-only",
        "--region", region,
    ]

    try:
        subprocess.run(cmd, check=True, text=True)
    except subprocess.CalledProcessError as e:
        log.error("S3 upload failed: %s", e)
        return False

    # Log URLs for each report.html found
    for root, _dirs, files in os.walk(results_dir):
        for f in files:
            if f == "report.html":
                rel = os.path.relpath(os.path.join(root, f), results_dir)
                url = f"{website_url}{rel}"
                log.info("  Report viewable at: %s", url)

    log.info("Upload complete. Browse results at: %s", website_url)
    return True


def main() -> None:
    parser = argparse.ArgumentParser(description="Upload app results to S3")
    parser.add_argument(
        "--app-dir", required=True,
        help="Path to the app directory (e.g. apps/linear)",
    )
    parser.add_argument(
        "--env-id", required=True,
        help="Environment ID (used as S3 prefix)",
    )
    parser.add_argument(
        "--s3-bucket",
        default=os.environ.get("MM_S3_BUCKET", "mirror-mirror-results"),
        help="S3 bucket name (default: MM_S3_BUCKET or mirror-mirror-results)",
    )
    args = parser.parse_args()

    success = upload_results(args.app_dir, args.s3_bucket, args.env_id)
    if not success:
        sys.exit(1)


if __name__ == "__main__":
    main()
