#!/usr/bin/env bash
# Launch the full pipeline: controller + env generators + agent testers.
# Run from your local machine after vpc_and_sg.sh and seed_branches.sh.
#
# Prerequisites:
#   source /tmp/mirror-mirror-infra.env   (from vpc_and_sg.sh)
#   Set these env vars:
#     ANTHROPIC_API_KEY    — for Claude Code (env generation)
#     GOOGLE_API_KEY       — for Gemini (agent evaluation)
#     GITHUB_TOKEN         — for git push/pull on EC2 instances
#     KEY_PAIR_NAME        — your EC2 key pair name (for SSH if needed)
#
# Usage:
#   bash infra/setup/launch_pipeline.sh              # N=5 default (1 gen + 1 tester)
#   bash infra/setup/launch_pipeline.sh 20           # N=20 (2 gen + 1 tester)
#   bash infra/setup/launch_pipeline.sh 100          # N=100 (10 gen + 5 testers)

set -euo pipefail

TOTAL_ENVS="${1:-5}"
REGION="${AWS_REGION:-us-east-1}"
REPO_URL="https://github.com/shuyanzhou/mirror-mirror.git"

# --- Validate required env vars ---
for var in PRIV_SUBNET SG_ENV SG_AGENT SG_CTRL PUB_SUBNET \
           GENERATE_QUEUE_URL EVAL_QUEUE_URL EVAL_DONE_QUEUE_URL PIPELINE_DONE_QUEUE_URL \
           ANTHROPIC_API_KEY GOOGLE_API_KEY GITHUB_TOKEN KEY_PAIR_NAME; do
  if [ -z "${!var:-}" ]; then
    echo "ERROR: $var is not set"
    echo "Run: source /tmp/mirror-mirror-infra.env"
    echo "And set: ANTHROPIC_API_KEY, GOOGLE_API_KEY, GITHUB_TOKEN, KEY_PAIR_NAME"
    exit 1
  fi
done

# --- Calculate instance counts ---
ENVS_PER_GEN=10
NUM_GENERATORS=$(( (TOTAL_ENVS + ENVS_PER_GEN - 1) / ENVS_PER_GEN ))
NUM_TESTERS=$(( (NUM_GENERATORS + 1) / 2 ))
[ "$NUM_TESTERS" -lt 1 ] && NUM_TESTERS=1

echo "=== Pipeline Launch Plan ==="
echo "  Environments:    $TOTAL_ENVS"
echo "  Env generators:  $NUM_GENERATORS  (m5.xlarge)"
echo "  Agent testers:   $NUM_TESTERS  (c5.4xlarge)"
echo "  Controller:      1  (t3.medium)"
echo "  Region:          $REGION"
echo ""

# --- Find latest Amazon Linux 2023 AMI ---
AL2023_AMI=$(aws ec2 describe-images \
  --owners amazon \
  --filters "Name=name,Values=al2023-ami-2023*-x86_64" "Name=state,Values=available" \
  --query 'Images | sort_by(@, &CreationDate) | [-1].ImageId' \
  --output text --region "$REGION")
echo "  Base AMI: $AL2023_AMI"
echo ""

# --- IAM role for SQS access ---
# Create instance profile if it doesn't exist
ROLE_NAME="mirror-mirror-ec2"
if ! aws iam get-role --role-name "$ROLE_NAME" --region "$REGION" 2>/dev/null; then
  echo "Creating IAM role: $ROLE_NAME"
  aws iam create-role --role-name "$ROLE_NAME" \
    --assume-role-policy-document '{
      "Version": "2012-10-17",
      "Statement": [{"Effect": "Allow", "Principal": {"Service": "ec2.amazonaws.com"}, "Action": "sts:AssumeRole"}]
    }' --region "$REGION" > /dev/null
  aws iam attach-role-policy --role-name "$ROLE_NAME" \
    --policy-arn arn:aws:iam::aws:policy/AmazonSQSFullAccess --region "$REGION"
  aws iam create-instance-profile --instance-profile-name "$ROLE_NAME" --region "$REGION" > /dev/null
  aws iam add-role-to-instance-profile --instance-profile-name "$ROLE_NAME" --role-name "$ROLE_NAME" --region "$REGION"
  echo "  Waiting for IAM propagation..."
  sleep 10
fi

# --- Common user-data header ---
read -r -d '' USERDATA_COMMON << 'COMMON_EOF' || true
#!/bin/bash
set -euo pipefail
exec > /var/log/mirror-mirror-setup.log 2>&1

export HOME=/home/ec2-user
cd $HOME

# System packages
dnf update -y
dnf install -y git gcc gcc-c++ make openssl-devel bzip2-devel \
  libffi-devel zlib-devel readline-devel sqlite-devel

# Python via uv
su - ec2-user -c 'curl -LsSf https://astral.sh/uv/install.sh | sh'
export PATH="/home/ec2-user/.local/bin:$PATH"
su - ec2-user -c 'export PATH="$HOME/.local/bin:$PATH" && uv python install 3.12'

# Node.js 20
curl -fsSL https://rpm.nodesource.com/setup_20.x | bash -
dnf install -y nodejs

# Git config
su - ec2-user -c 'git config --global user.email "mirror-mirror-bot@example.com"'
su - ec2-user -c 'git config --global user.name "mirror-mirror-bot"'
COMMON_EOF

# --- Env Generator user-data ---
gen_userdata() {
  cat <<EOF
${USERDATA_COMMON}

# Claude Code CLI
npm install -g @anthropic-ai/claude-code

# Python deps
su - ec2-user -c 'export PATH="\$HOME/.local/bin:\$PATH" && uv pip install --system requests python-dotenv boto3'

# Clone repo
su - ec2-user -c 'git clone https://${GITHUB_TOKEN}@github.com/shuyanzhou/mirror-mirror.git /home/ec2-user/mirror-mirror'

# Write env vars
cat >> /home/ec2-user/.bashrc <<ENVVARS
export ANTHROPIC_API_KEY="${ANTHROPIC_API_KEY}"
export GITHUB_TOKEN="${GITHUB_TOKEN}"
export AWS_REGION="${REGION}"
export GENERATE_QUEUE_URL="${GENERATE_QUEUE_URL}"
export EVAL_QUEUE_URL="${EVAL_QUEUE_URL}"
export EVAL_DONE_QUEUE_URL="${EVAL_DONE_QUEUE_URL}"
export PIPELINE_DONE_QUEUE_URL="${PIPELINE_DONE_QUEUE_URL}"
export TOTAL_ENVS="${TOTAL_ENVS}"
ENVVARS

# Start env worker
su - ec2-user -c 'cd /home/ec2-user/mirror-mirror && nohup python infra/env_worker.py > /tmp/mirror-mirror-logs/env-worker.log 2>&1 &'
echo "Env worker started"
EOF
}

# --- Agent Tester user-data ---
agent_userdata() {
  cat <<EOF
${USERDATA_COMMON}

# Chromium dependencies
dnf install -y alsa-lib atk at-spi2-atk cups-libs libdrm mesa-libgbm \
  pango libXcomposite libXdamage libXrandr libxkbcommon nss nspr

# Python deps
su - ec2-user -c 'export PATH="\$HOME/.local/bin:\$PATH" && uv pip install --system "browser-use>=0.11.9" requests python-dotenv boto3'

# Playwright + Chromium
su - ec2-user -c 'export PATH="\$HOME/.local/bin:\$PATH" && python -m playwright install chromium && python -m playwright install-deps'

# Clone repo
su - ec2-user -c 'git clone https://${GITHUB_TOKEN}@github.com/shuyanzhou/mirror-mirror.git /home/ec2-user/mirror-mirror'

# Write env vars
cat >> /home/ec2-user/.bashrc <<ENVVARS
export GOOGLE_API_KEY="${GOOGLE_API_KEY}"
export ANTHROPIC_API_KEY="${ANTHROPIC_API_KEY:-}"
export GITHUB_TOKEN="${GITHUB_TOKEN}"
export AWS_REGION="${REGION}"
export EVAL_QUEUE_URL="${EVAL_QUEUE_URL}"
export EVAL_DONE_QUEUE_URL="${EVAL_DONE_QUEUE_URL}"
ENVVARS

# Start agent worker
su - ec2-user -c 'cd /home/ec2-user/mirror-mirror && nohup python infra/agent_worker.py --workers 8 > /tmp/mirror-mirror-logs/agent-worker.log 2>&1 &'
echo "Agent worker started"
EOF
}

# --- Controller user-data ---
controller_userdata() {
  cat <<EOF
${USERDATA_COMMON}

# Python deps
su - ec2-user -c 'export PATH="\$HOME/.local/bin:\$PATH" && uv pip install --system boto3'

# Clone repo
su - ec2-user -c 'git clone https://${GITHUB_TOKEN}@github.com/shuyanzhou/mirror-mirror.git /home/ec2-user/mirror-mirror'

# Write env vars
cat >> /home/ec2-user/.bashrc <<ENVVARS
export AWS_REGION="${REGION}"
export GENERATE_QUEUE_URL="${GENERATE_QUEUE_URL}"
export PIPELINE_DONE_QUEUE_URL="${PIPELINE_DONE_QUEUE_URL}"
export TOTAL_ENVS="${TOTAL_ENVS}"
ENVVARS

# Start orchestrator
su - ec2-user -c 'cd /home/ec2-user/mirror-mirror && nohup python infra/orchestrator.py --manifest infra/env_manifest.jsonl > /tmp/mirror-mirror-logs/orchestrator.log 2>&1 &'
echo "Orchestrator started"
EOF
}

# --- Launch instances ---
echo "=== Launching Controller ==="
CTRL_ID=$(aws ec2 run-instances \
  --image-id "$AL2023_AMI" \
  --instance-type t3.medium \
  --key-name "$KEY_PAIR_NAME" \
  --subnet-id "$PUB_SUBNET" \
  --security-group-ids "$SG_CTRL" \
  --iam-instance-profile Name="$ROLE_NAME" \
  --user-data "$(controller_userdata | base64)" \
  --tag-specifications "ResourceType=instance,Tags=[{Key=Name,Value=mm-controller},{Key=Project,Value=mirror-mirror},{Key=Role,Value=controller}]" \
  --query 'Instances[0].InstanceId' --output text --region "$REGION")
echo "  Controller: $CTRL_ID"

INSTANCE_IDS="$CTRL_ID"

echo "=== Launching $NUM_GENERATORS Env Generator(s) ==="
for i in $(seq 1 "$NUM_GENERATORS"); do
  GEN_ID=$(aws ec2 run-instances \
    --image-id "$AL2023_AMI" \
    --instance-type m5.xlarge \
    --key-name "$KEY_PAIR_NAME" \
    --subnet-id "$PRIV_SUBNET" \
    --security-group-ids "$SG_ENV" \
    --iam-instance-profile Name="$ROLE_NAME" \
    --user-data "$(gen_userdata | base64)" \
    --block-device-mappings '[{"DeviceName":"/dev/xvda","Ebs":{"VolumeSize":30}}]' \
    --tag-specifications "ResourceType=instance,Tags=[{Key=Name,Value=mm-env-gen-$i},{Key=Project,Value=mirror-mirror},{Key=Role,Value=env-generator}]" \
    --query 'Instances[0].InstanceId' --output text --region "$REGION")
  echo "  Env Generator $i: $GEN_ID"
  INSTANCE_IDS="$INSTANCE_IDS $GEN_ID"
done

echo "=== Launching $NUM_TESTERS Agent Tester(s) ==="
for i in $(seq 1 "$NUM_TESTERS"); do
  AGENT_ID=$(aws ec2 run-instances \
    --image-id "$AL2023_AMI" \
    --instance-type c5.4xlarge \
    --key-name "$KEY_PAIR_NAME" \
    --subnet-id "$PRIV_SUBNET" \
    --security-group-ids "$SG_AGENT" \
    --iam-instance-profile Name="$ROLE_NAME" \
    --block-device-mappings '[{"DeviceName":"/dev/xvda","Ebs":{"VolumeSize":40}}]' \
    --user-data "$(agent_userdata | base64)" \
    --tag-specifications "ResourceType=instance,Tags=[{Key=Name,Value=mm-agent-$i},{Key=Project,Value=mirror-mirror},{Key=Role,Value=agent-tester}]" \
    --query 'Instances[0].InstanceId' --output text --region "$REGION")
  echo "  Agent Tester $i: $AGENT_ID"
  INSTANCE_IDS="$INSTANCE_IDS $AGENT_ID"
done

# --- Save instance info ---
LAUNCH_FILE="/tmp/mirror-mirror-instances.env"
cat > "$LAUNCH_FILE" <<EOF
# Generated by launch_pipeline.sh — $(date -u +%Y-%m-%dT%H:%M:%SZ)
INSTANCE_IDS="$INSTANCE_IDS"
CTRL_ID=$CTRL_ID
TOTAL_ENVS=$TOTAL_ENVS
NUM_GENERATORS=$NUM_GENERATORS
NUM_TESTERS=$NUM_TESTERS
EOF
echo ""
echo "=== All instances launched ==="
echo "Instance IDs saved to $LAUNCH_FILE"
echo ""
echo "Instances are installing dependencies (~5-10 min). Monitor:"
echo "  bash infra/setup/monitor_pipeline.sh"
echo ""
echo "To tear down everything when done:"
echo "  bash infra/setup/teardown.sh"
