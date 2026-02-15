#!/usr/bin/env bash
# Monitor pipeline progress from your local machine.
# Polls SQS queue depths and EC2 instance status every 30 seconds.
#
# Prerequisites:
#   source /tmp/mirror-mirror-infra.env
#
# Usage:
#   bash infra/setup/monitor_pipeline.sh             # continuous monitoring
#   bash infra/setup/monitor_pipeline.sh --once       # single snapshot

set -euo pipefail

REGION="${AWS_REGION:-us-east-1}"
ONCE="${1:-}"

for var in GENERATE_QUEUE_URL EVAL_QUEUE_URL EVAL_DONE_QUEUE_URL PIPELINE_DONE_QUEUE_URL; do
  if [ -z "${!var:-}" ]; then
    echo "ERROR: $var not set. Run: source /tmp/mirror-mirror-infra.env"
    exit 1
  fi
done

queue_depth() {
  local url="$1"
  local name="$2"
  local attrs
  attrs=$(aws sqs get-queue-attributes --queue-url "$url" \
    --attribute-names ApproximateNumberOfMessages ApproximateNumberOfMessagesNotVisible \
    --query 'Attributes' --output json --region "$REGION" 2>/dev/null)
  local visible=$(echo "$attrs" | python3 -c "import sys,json; print(json.load(sys.stdin).get('ApproximateNumberOfMessages','?'))")
  local inflight=$(echo "$attrs" | python3 -c "import sys,json; print(json.load(sys.stdin).get('ApproximateNumberOfMessagesNotVisible','?'))")
  printf "  %-20s  queued: %-4s  in-flight: %-4s\n" "$name" "$visible" "$inflight"
}

instance_status() {
  echo "  EC2 Instances:"
  aws ec2 describe-instances \
    --filters "Name=tag:Project,Values=mirror-mirror" "Name=instance-state-name,Values=pending,running,stopping" \
    --query 'Reservations[].Instances[].{Id:InstanceId,Type:InstanceType,State:State.Name,Name:Tags[?Key==`Name`].Value|[0],Role:Tags[?Key==`Role`].Value|[0]}' \
    --output table --region "$REGION" 2>/dev/null || echo "  (no instances found)"
}

snapshot() {
  clear
  echo "=== Mirror-Mirror Pipeline Monitor ==="
  echo "  $(date)"
  echo ""
  echo "  SQS Queues:"
  queue_depth "$GENERATE_QUEUE_URL" "generate"
  queue_depth "$EVAL_QUEUE_URL" "eval"
  queue_depth "$EVAL_DONE_QUEUE_URL" "eval-done"
  queue_depth "$PIPELINE_DONE_QUEUE_URL" "pipeline-done"
  echo ""
  instance_status
  echo ""
  echo "  (Ctrl+C to stop)"
}

if [ "$ONCE" = "--once" ]; then
  snapshot
else
  while true; do
    snapshot
    sleep 30
  done
fi
