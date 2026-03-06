#!/usr/bin/env bash
# Run pipeline in batches: launch N environments at a time, wait for all
# to finish, tear down, then launch the next batch.
#
# Prerequisites: same as launch.sh (GITHUB_TOKEN, KEY_PAIR_NAME, etc.)
#
# Usage:
#   bash infra/setup/run_batches.sh --manifest infra/env_manifest.jsonl --batch-size 3 --model gemini
#   bash infra/setup/run_batches.sh --manifest infra/env_manifest.jsonl --batch-size 3 --ami ami-0abc123
#
# All extra flags are forwarded to launch.sh (--ami, --model, --workers, etc.)

set -euo pipefail

MANIFEST=""
BATCH_SIZE=3
POLL_INTERVAL=120  # seconds between completion checks
LAUNCH_ARGS=()

# --- Parse arguments ---
while [[ $# -gt 0 ]]; do
  case "$1" in
    --manifest)      MANIFEST="$2";      shift 2 ;;
    --batch-size)    BATCH_SIZE="$2";     shift 2 ;;
    --poll-interval) POLL_INTERVAL="$2";  shift 2 ;;
    *)               LAUNCH_ARGS+=("$1"); shift ;;
  esac
done

if [ -z "$MANIFEST" ]; then
  echo "ERROR: --manifest is required"
  echo "Usage: bash infra/setup/run_batches.sh --manifest FILE --batch-size N [launch.sh flags...]"
  exit 1
fi

if [ ! -f "$MANIFEST" ]; then
  echo "ERROR: Manifest not found: $MANIFEST"
  exit 1
fi

# --- Read all environments ---
ALL_ENVS=()
while IFS= read -r line; do
  [ -z "$line" ] && continue
  ALL_ENVS+=("$line")
done < "$MANIFEST"
TOTAL=${#ALL_ENVS[@]}

if [ "$TOTAL" -eq 0 ]; then
  echo "ERROR: No environments in $MANIFEST"
  exit 1
fi

NUM_BATCHES=$(( (TOTAL + BATCH_SIZE - 1) / BATCH_SIZE ))
echo "=== Batch Run Plan ==="
echo "  Total environments: $TOTAL"
echo "  Batch size:         $BATCH_SIZE"
echo "  Number of batches:  $NUM_BATCHES"
echo "  Poll interval:      ${POLL_INTERVAL}s"
echo "  Extra launch args:  ${LAUNCH_ARGS[*]:-none}"
echo ""

KEY_PAIR="${KEY_PAIR_NAME:-}"
REGION="${AWS_REGION:-us-east-1}"

# --- Check if all pipelines in current batch are done ---
# Reports status of every instance and returns 0 only when none are still running.
check_batch_done() {
  local launch_file="$1"
  source "$launch_file"
  local any_running=0

  for INST_ID in $INSTANCE_IDS; do
    INFO=$(aws ec2 describe-instances --instance-ids "$INST_ID" \
      --query 'Reservations[0].Instances[0].[PublicIpAddress,State.Name,Tags[?Key==`EnvId`].Value|[0]]' \
      --output text --region "$REGION" 2>/dev/null)
    IP=$(echo "$INFO" | awk '{print $1}')
    STATE=$(echo "$INFO" | awk '{print $2}')
    ENV_ID=$(echo "$INFO" | awk '{print $3}')

    # Instance not running — treat as done (terminated/stopped)
    if [ "$STATE" != "running" ]; then
      echo "    $ENV_ID: instance $STATE"
      continue
    fi

    if [ "$IP" = "None" ] || [ -z "$IP" ]; then
      echo "    $ENV_ID: no public IP"
      any_running=1
      continue
    fi

    # Check if pipeline process is still running
    PIPELINE_RUNNING=$(ssh -i "$HOME/.ssh/${KEY_PAIR}.pem" \
      -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -o ConnectTimeout=5 -o BatchMode=yes \
      "ec2-user@${IP}" \
      'pgrep -f "infra/pipeline[.]py" > /dev/null 2>&1 && echo yes || echo no' \
      2>/dev/null || echo "unreachable")

    if [ "$PIPELINE_RUNNING" = "yes" ]; then
      STATUS=$(ssh -i "$HOME/.ssh/${KEY_PAIR}.pem" \
        -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -o ConnectTimeout=5 -o BatchMode=yes \
        "ec2-user@${IP}" \
        'grep -E "(Phase|pass rate|complete|iteration)" /tmp/mirror-mirror-logs/pipeline.log 2>/dev/null | tail -1 | sed "s/^[0-9-]* [0-9:]* \[pipeline\] //"' \
        2>/dev/null || echo "unknown")
      echo "    $ENV_ID: running — $STATUS"
      any_running=1
    elif [ "$PIPELINE_RUNNING" = "unreachable" ]; then
      echo "    $ENV_ID: SSH unreachable"
      any_running=1
    else
      # Pipeline not running — check if it completed successfully or crashed
      OUTCOME=$(ssh -i "$HOME/.ssh/${KEY_PAIR}.pem" \
        -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -o ConnectTimeout=5 -o BatchMode=yes \
        "ec2-user@${IP}" \
        'grep -c "Pipeline complete for:" /tmp/mirror-mirror-logs/pipeline.log 2>/dev/null || echo 0' \
        2>/dev/null || echo "0")

      if [ "$OUTCOME" = "0" ]; then
        FAIL_MSG=$(ssh -i "$HOME/.ssh/${KEY_PAIR}.pem" \
          -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -o ConnectTimeout=5 -o BatchMode=yes \
          "ec2-user@${IP}" \
          'grep -E "FAILED|Error|Traceback" /tmp/mirror-mirror-logs/pipeline.log 2>/dev/null | tail -1 | sed "s/^[0-9-]* [0-9:]* \[pipeline\] //"' \
          2>/dev/null || echo "unknown error")
        echo "    $ENV_ID: CRASHED — ${FAIL_MSG:-(no log)}"
        BATCH_HAD_FAILURES=1
      else
        echo "    $ENV_ID: done"
      fi
    fi
  done

  return $any_running
}

# --- Run batches ---
for (( batch=0; batch<NUM_BATCHES; batch++ )); do
  start=$(( batch * BATCH_SIZE ))
  end=$(( start + BATCH_SIZE ))
  if [ "$end" -gt "$TOTAL" ]; then
    end=$TOTAL
  fi
  batch_num=$(( batch + 1 ))
  batch_count=$(( end - start ))

  echo "==========================================="
  echo "=== Batch $batch_num / $NUM_BATCHES ($batch_count environments) ==="
  echo "==========================================="
  echo ""

  # Write temp manifest for this batch
  BATCH_MANIFEST=$(mktemp /tmp/mm-batch-XXXXXX)
  for (( i=start; i<end; i++ )); do
    echo "${ALL_ENVS[$i]}" >> "$BATCH_MANIFEST"
  done

  echo "Environments in this batch:"
  while IFS= read -r line; do
    env_id=$(echo "$line" | python3 -c "import sys,json; print(json.load(sys.stdin)['env_id'])")
    echo "  - $env_id"
  done < "$BATCH_MANIFEST"
  echo ""

  # Launch this batch (unique launch file per batch)
  LAUNCH_FILE="/tmp/mirror-mirror-launch-batch${batch_num}.env"
  bash infra/setup/launch.sh --manifest "$BATCH_MANIFEST" --launch-file "$LAUNCH_FILE" "${LAUNCH_ARGS[@]}"

  # Wait for all pipelines to complete
  echo ""
  echo "=== Waiting for batch $batch_num to complete (polling every ${POLL_INTERVAL}s) ==="
  echo ""

  BATCH_HAD_FAILURES=0
  while true; do
    BATCH_HAD_FAILURES=0
    if check_batch_done "$LAUNCH_FILE"; then
      echo ""
      if [ "$BATCH_HAD_FAILURES" -gt 0 ]; then
        echo "  Batch $batch_num finished (some pipelines FAILED — check logs above)"
      else
        echo "  Batch $batch_num complete!"
      fi
      break
    fi
    echo "  --- sleeping ${POLL_INTERVAL}s ($(date -u +%H:%M:%S)) ---"
    sleep "$POLL_INTERVAL"
  done

  # # Tear down this batch (keep EIPs released, keep SG/IAM for reuse)
  # echo ""
  # echo "=== Tearing down batch $batch_num ==="
  # bash infra/setup/teardown.sh --release-eips

  # # Cleanup temp files
  # rm -f "$BATCH_MANIFEST"
  # rm -f "$LAUNCH_FILE"
# 
  echo ""
  if [ "$batch_num" -lt "$NUM_BATCHES" ]; then
    echo "Moving to next batch..."
    echo ""
  fi
done

echo "==========================================="
echo "=== All $NUM_BATCHES batches complete! ==="
echo "==========================================="
