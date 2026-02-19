#!/usr/bin/env bash
# Terminate pipeline EC2 instances.
# Does NOT delete VPC/SQS/IAM — those are cheap to keep for next run.
#
# Usage:
#   bash infra/setup/teardown.sh                       # terminate all mm instances
#   bash infra/setup/teardown.sh --keep-generators     # keep env-generator instances
#   bash infra/setup/teardown.sh --clean-generators    # keep + clean generators (implies --keep-generators)
#   bash infra/setup/teardown.sh --purge-queues        # also purge SQS queues
#   bash infra/setup/teardown.sh --all                 # also delete VPC, SQS, IAM role
#
# Flags can be combined: --clean-generators --purge-queues
# SSH key: defaults to ~/.ssh/mirror-mirror.pem, override with --ssh-key=/path/to/key

set -euo pipefail

REGION="${AWS_REGION:-us-east-1}"
SSH_KEY="${SSH_KEY:-$HOME/.ssh/mirror-mirror.pem}"
KEEP_GENERATORS=false
CLEAN_GENERATORS=false
PURGE_QUEUES=false
DELETE_ALL=false

for arg in "$@"; do
  case "$arg" in
    --keep-generators)  KEEP_GENERATORS=true ;;
    --clean-generators) CLEAN_GENERATORS=true; KEEP_GENERATORS=true ;;
    --purge-queues)     PURGE_QUEUES=true ;;
    --all)              DELETE_ALL=true ;;
    --ssh-key=*)        SSH_KEY="${arg#*=}" ;;
    *) echo "Unknown flag: $arg"; exit 1 ;;
  esac
done

echo "=== Terminating mirror-mirror EC2 instances ==="

if $KEEP_GENERATORS; then
  echo "  (keeping env-generator instances)"
  # Get all mm instances
  ALL_IDS=$(aws ec2 describe-instances \
    --filters "Name=tag:Project,Values=mirror-mirror" "Name=instance-state-name,Values=pending,running,stopping,stopped" \
    --query 'Reservations[].Instances[].InstanceId' \
    --output text --region "$REGION")
  # Get generator instances to exclude
  GEN_IDS=$(aws ec2 describe-instances \
    --filters "Name=tag:Project,Values=mirror-mirror" "Name=tag:Role,Values=env-generator" "Name=instance-state-name,Values=pending,running,stopping,stopped" \
    --query 'Reservations[].Instances[].InstanceId' \
    --output text --region "$REGION")
  # Subtract generators from all
  INSTANCE_IDS=""
  for id in $ALL_IDS; do
    skip=false
    for gen in $GEN_IDS; do
      [ "$id" = "$gen" ] && skip=true && break
    done
    $skip || INSTANCE_IDS="$INSTANCE_IDS $id"
  done
  INSTANCE_IDS=$(echo "$INSTANCE_IDS" | xargs)  # trim whitespace
  if [ -n "$GEN_IDS" ]; then
    echo "  Keeping generators: $GEN_IDS"
  fi
else
  INSTANCE_IDS=$(aws ec2 describe-instances \
    --filters "Name=tag:Project,Values=mirror-mirror" "Name=instance-state-name,Values=pending,running,stopping,stopped" \
    --query 'Reservations[].Instances[].InstanceId' \
    --output text --region "$REGION")
fi

if [ -n "$INSTANCE_IDS" ]; then
  echo "  Terminating: $INSTANCE_IDS"
  aws ec2 terminate-instances --instance-ids $INSTANCE_IDS --region "$REGION" > /dev/null
  echo "  Waiting for termination..."
  aws ec2 wait instance-terminated --instance-ids $INSTANCE_IDS --region "$REGION"
  echo "  Terminated."
else
  echo "  No instances to terminate."
fi

# Clean generator instances (remove worktrees, pull latest, kill workers)
if $CLEAN_GENERATORS; then
  echo ""
  echo "=== Cleaning env-generator instances ==="
  GEN_IPS=$(aws ec2 describe-instances \
    --filters "Name=tag:Project,Values=mirror-mirror" "Name=tag:Role,Values=env-generator" "Name=instance-state-name,Values=running" \
    --query 'Reservations[].Instances[].PublicIpAddress' \
    --output text --region "$REGION")
  for ip in $GEN_IPS; do
    echo "  Cleaning $ip ..."
    ssh -i "$SSH_KEY" -o StrictHostKeyChecking=no -o ConnectTimeout=10 "ec2-user@$ip" bash -s <<'REMOTE_SCRIPT' 2>&1 | sed 's/^/    /'
# Kill any running worker processes
pkill -f 'env_worker.py' 2>/dev/null && echo "Killed env_worker" || echo "No env_worker running"
pkill -f 'claude.*--print' 2>/dev/null && echo "Killed claude processes" || echo "No claude processes"
# Clean worktrees
cd ~/mirror-mirror
for wt in ~/mirror-mirror-workers/worker-*; do
  [ -d "$wt" ] && git worktree remove --force "$wt" 2>/dev/null
done
git worktree prune
rm -rf ~/mirror-mirror-workers/*
# Pull latest
git checkout main 2>/dev/null
git fetch origin
git reset --hard origin/main
echo "Git: $(git log --oneline -1)"
echo "Worktrees: $(git worktree list | wc -l) (main only)"
echo "Workers dir: $(ls ~/mirror-mirror-workers/ 2>/dev/null | wc -w) items"
REMOTE_SCRIPT
    echo "  Done: $ip"
  done
fi

# Purge SQS queues (clear messages but keep queues)
if $PURGE_QUEUES; then
  echo ""
  echo "=== Purging SQS queues ==="
  for var in GENERATE_QUEUE_URL EVAL_QUEUE_URL EVAL_DONE_QUEUE_URL PIPELINE_DONE_QUEUE_URL; do
    url="${!var:-}"
    if [ -n "$url" ]; then
      aws sqs purge-queue --queue-url "$url" --region "$REGION" 2>/dev/null && \
        echo "  Purged: $var" || echo "  Skip (not found): $var"
    fi
  done
fi

if ! $DELETE_ALL; then
  echo ""
  echo "VPC, SQS queues, and IAM role preserved (re-use on next run)."
  echo "To delete everything: bash infra/setup/teardown.sh --all"
  exit 0
fi

echo ""
echo "=== Deleting SQS queues ==="
for var in GENERATE_QUEUE_URL EVAL_QUEUE_URL EVAL_DONE_QUEUE_URL PIPELINE_DONE_QUEUE_URL; do
  url="${!var:-}"
  if [ -n "$url" ]; then
    aws sqs delete-queue --queue-url "$url" --region "$REGION" 2>/dev/null && \
      echo "  Deleted: $url" || echo "  Skip (not found): $url"
  fi
done

echo ""
echo "=== Deleting IAM role ==="
ROLE_NAME="mirror-mirror-ec2"
aws iam remove-role-from-instance-profile --instance-profile-name "$ROLE_NAME" --role-name "$ROLE_NAME" --region "$REGION" 2>/dev/null || true
aws iam delete-instance-profile --instance-profile-name "$ROLE_NAME" --region "$REGION" 2>/dev/null || true
aws iam detach-role-policy --role-name "$ROLE_NAME" --policy-arn arn:aws:iam::aws:policy/AmazonSQSFullAccess --region "$REGION" 2>/dev/null || true
aws iam delete-role --role-name "$ROLE_NAME" --region "$REGION" 2>/dev/null && echo "  Deleted role: $ROLE_NAME" || true

echo ""
echo "=== Deleting VPC resources ==="
VPC_ID="${VPC_ID:-}"
if [ -z "$VPC_ID" ]; then
  VPC_ID=$(aws ec2 describe-vpcs \
    --filters "Name=tag:Project,Values=mirror-mirror" \
    --query 'Vpcs[0].VpcId' --output text --region "$REGION" 2>/dev/null)
fi

if [ -n "$VPC_ID" ] && [ "$VPC_ID" != "None" ]; then
  echo "  VPC: $VPC_ID"

  # Delete NAT gateway
  NAT_IDS=$(aws ec2 describe-nat-gateways \
    --filter "Name=vpc-id,Values=$VPC_ID" "Name=state,Values=available" \
    --query 'NatGateways[].NatGatewayId' --output text --region "$REGION")
  for nat in $NAT_IDS; do
    aws ec2 delete-nat-gateway --nat-gateway-id "$nat" --region "$REGION" > /dev/null
    echo "  Deleting NAT gateway: $nat (takes ~2 min)"
  done
  [ -n "$NAT_IDS" ] && sleep 120  # wait for NAT deletion

  # Release EIPs
  EIP_IDS=$(aws ec2 describe-addresses \
    --filters "Name=tag:Project,Values=mirror-mirror" \
    --query 'Addresses[].AllocationId' --output text --region "$REGION")
  for eip in $EIP_IDS; do
    aws ec2 release-address --allocation-id "$eip" --region "$REGION" 2>/dev/null && echo "  Released EIP: $eip"
  done

  # Delete security groups (non-default)
  SG_IDS=$(aws ec2 describe-security-groups \
    --filters "Name=vpc-id,Values=$VPC_ID" \
    --query 'SecurityGroups[?GroupName!=`default`].GroupId' --output text --region "$REGION")
  for sg in $SG_IDS; do
    aws ec2 delete-security-group --group-id "$sg" --region "$REGION" 2>/dev/null && echo "  Deleted SG: $sg"
  done

  # Delete subnets
  SUBNET_IDS=$(aws ec2 describe-subnets \
    --filters "Name=vpc-id,Values=$VPC_ID" \
    --query 'Subnets[].SubnetId' --output text --region "$REGION")
  for sub in $SUBNET_IDS; do
    aws ec2 delete-subnet --subnet-id "$sub" --region "$REGION" 2>/dev/null && echo "  Deleted subnet: $sub"
  done

  # Detach and delete IGW
  IGW_IDS=$(aws ec2 describe-internet-gateways \
    --filters "Name=attachment.vpc-id,Values=$VPC_ID" \
    --query 'InternetGateways[].InternetGatewayId' --output text --region "$REGION")
  for igw in $IGW_IDS; do
    aws ec2 detach-internet-gateway --internet-gateway-id "$igw" --vpc-id "$VPC_ID" --region "$REGION"
    aws ec2 delete-internet-gateway --internet-gateway-id "$igw" --region "$REGION" && echo "  Deleted IGW: $igw"
  done

  # Delete route tables (non-main)
  RT_IDS=$(aws ec2 describe-route-tables \
    --filters "Name=vpc-id,Values=$VPC_ID" \
    --query 'RouteTables[?Associations[0].Main!=`true`].RouteTableId' --output text --region "$REGION")
  for rt in $RT_IDS; do
    # Disassociate first
    ASSOC_IDS=$(aws ec2 describe-route-tables --route-table-ids "$rt" \
      --query 'RouteTables[0].Associations[].RouteTableAssociationId' --output text --region "$REGION")
    for assoc in $ASSOC_IDS; do
      aws ec2 disassociate-route-table --association-id "$assoc" --region "$REGION" 2>/dev/null
    done
    aws ec2 delete-route-table --route-table-id "$rt" --region "$REGION" 2>/dev/null && echo "  Deleted RT: $rt"
  done

  # Delete VPC
  aws ec2 delete-vpc --vpc-id "$VPC_ID" --region "$REGION" && echo "  Deleted VPC: $VPC_ID"
else
  echo "  No VPC found."
fi

echo ""
echo "=== Teardown complete ==="
