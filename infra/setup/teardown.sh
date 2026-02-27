#!/usr/bin/env bash
# Terminate pipeline EC2 instances and optionally release Elastic IPs.
#
# Finds all instances tagged Project=mirror-mirror and terminates them.
#
# Usage:
#   bash infra/setup/teardown.sh                   # terminate instances (keep EIPs + SG)
#   bash infra/setup/teardown.sh --release-eips    # also release Elastic IPs
#   bash infra/setup/teardown.sh --all             # terminate + release EIPs + delete SG + IAM role

set -euo pipefail

REGION="${AWS_REGION:-us-east-1}"
RELEASE_EIPS=false
DELETE_ALL=false

for arg in "$@"; do
  case "$arg" in
    --release-eips) RELEASE_EIPS=true ;;
    --all)          DELETE_ALL=true; RELEASE_EIPS=true ;;
    *) echo "Unknown flag: $arg"; exit 1 ;;
  esac
done

# --- Terminate instances ---
echo "=== Terminating mirror-mirror EC2 instances ==="
INSTANCE_IDS=$(aws ec2 describe-instances \
  --filters "Name=tag:Project,Values=mirror-mirror" "Name=instance-state-name,Values=pending,running,stopping,stopped" \
  --query 'Reservations[].Instances[].InstanceId' \
  --output text --region "$REGION")

if [ -n "$INSTANCE_IDS" ]; then
  # Show what we're terminating
  for id in $INSTANCE_IDS; do
    ENV_ID=$(aws ec2 describe-instances --instance-ids "$id" \
      --query 'Reservations[0].Instances[0].Tags[?Key==`EnvId`].Value | [0]' --output text --region "$REGION")
    STATE=$(aws ec2 describe-instances --instance-ids "$id" \
      --query 'Reservations[0].Instances[0].State.Name' --output text --region "$REGION")
    echo "  $id  ${ENV_ID:-unknown}  ($STATE)"
  done

  echo "  Terminating..."
  aws ec2 terminate-instances --instance-ids $INSTANCE_IDS --region "$REGION" > /dev/null
  echo "  Waiting for termination..."
  aws ec2 wait instance-terminated --instance-ids $INSTANCE_IDS --region "$REGION"
  echo "  Done."
else
  echo "  No instances found."
fi

# --- Release Elastic IPs ---
if $RELEASE_EIPS; then
  echo ""
  echo "=== Releasing Elastic IPs ==="
  EIP_IDS=$(aws ec2 describe-addresses \
    --filters "Name=tag:Project,Values=mirror-mirror" \
    --query 'Addresses[].AllocationId' --output text --region "$REGION")
  if [ -n "$EIP_IDS" ]; then
    for eip in $EIP_IDS; do
      IP=$(aws ec2 describe-addresses --allocation-ids "$eip" \
        --query 'Addresses[0].PublicIp' --output text --region "$REGION")
      aws ec2 release-address --allocation-id "$eip" --region "$REGION" 2>/dev/null && \
        echo "  Released: $IP ($eip)" || echo "  Failed to release: $eip"
    done
  else
    echo "  No Elastic IPs found."
  fi
fi

# --- Full cleanup ---
if $DELETE_ALL; then
  echo ""
  echo "=== Deleting security group ==="
  SG_ID=$(aws ec2 describe-security-groups \
    --filters "Name=group-name,Values=mm-pipeline" \
    --query 'SecurityGroups[0].GroupId' --output text --region "$REGION" 2>/dev/null || true)
  if [ -n "$SG_ID" ] && [ "$SG_ID" != "None" ]; then
    aws ec2 delete-security-group --group-id "$SG_ID" --region "$REGION" 2>/dev/null && \
      echo "  Deleted: $SG_ID" || echo "  Failed (may have dependencies): $SG_ID"
  else
    echo "  No mm-pipeline security group found."
  fi

  echo ""
  echo "=== Deleting IAM role ==="
  ROLE_NAME="mirror-mirror-ec2"
  aws iam remove-role-from-instance-profile --instance-profile-name "$ROLE_NAME" --role-name "$ROLE_NAME" 2>/dev/null || true
  aws iam delete-instance-profile --instance-profile-name "$ROLE_NAME" 2>/dev/null || true
  aws iam detach-role-policy --role-name "$ROLE_NAME" --policy-arn arn:aws:iam::aws:policy/AmazonSQSFullAccess 2>/dev/null || true
  aws iam delete-role --role-name "$ROLE_NAME" 2>/dev/null && echo "  Deleted role: $ROLE_NAME" || echo "  No role found."
fi

if ! $DELETE_ALL; then
  echo ""
  echo "Security group and IAM role preserved (re-use on next run)."
  echo "To delete everything: bash infra/setup/teardown.sh --all"
fi

echo ""
echo "=== Teardown complete ==="
