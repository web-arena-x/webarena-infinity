#!/usr/bin/env bash
# Launch the full pipeline: controller + env generators + agent testers.
# Run from your local machine after vpc_and_sg.sh and seed_branches.sh.
#
# Env generators are launched in the PUBLIC subnet so you can SSH in to
# run `claude login`.  They do NOT auto-start the worker — you must SSH
# into each one, run `claude login`, then start the worker manually:
#   cd ~/mirror-mirror && nohup python infra/env_worker.py > /tmp/mirror-mirror-logs/env-worker.log 2>&1 &
#
# Controller and agent testers auto-start their workers via user-data.
#
# Prerequisites:
#   source /tmp/mirror-mirror-infra.env   (from vpc_and_sg.sh)
#   Set these env vars (or source .env):
#     GOOGLE_API_KEY       — for Gemini (agent evaluation)
#     GITHUB_TOKEN         — for git push/pull on EC2 instances
#     KEY_PAIR_NAME        — your EC2 key pair name
#
# Usage:
#   bash infra/setup/launch_pipeline.sh              # N=5 default (1 gen + 1 tester)
#   bash infra/setup/launch_pipeline.sh 20           # N=20 (2 gen + 1 tester)
#   bash infra/setup/launch_pipeline.sh 100          # N=100 (10 gen + 5 testers)

set -euo pipefail

TOTAL_ENVS="${1:-5}"
REGION="${AWS_REGION:-us-east-1}"

# --- Validate required env vars ---
for var in PRIV_SUBNET SG_ENV SG_AGENT SG_CTRL PUB_SUBNET \
           GENERATE_QUEUE_URL EVAL_QUEUE_URL EVAL_DONE_QUEUE_URL PIPELINE_DONE_QUEUE_URL \
           GOOGLE_API_KEY GITHUB_TOKEN KEY_PAIR_NAME; do
  if [ -z "${!var:-}" ]; then
    echo "ERROR: $var is not set"
    echo ""
    echo "Run these first:"
    echo "  source /tmp/mirror-mirror-infra.env"
    echo "  set -a && source .env && set +a"
    exit 1
  fi
done

# --- Calculate instance counts ---
ENVS_PER_GEN=10
NUM_GENERATORS=$(( (TOTAL_ENVS + ENVS_PER_GEN - 1) / ENVS_PER_GEN ))
NUM_TESTERS=$(( (NUM_GENERATORS + 1) / 2 ))
[ "$NUM_TESTERS" -lt 1 ] && NUM_TESTERS=1

# --- Find latest Amazon Linux 2023 AMI ---
AL2023_AMI=$(aws ec2 describe-images \
  --owners amazon \
  --filters "Name=name,Values=al2023-ami-2023*-x86_64" "Name=state,Values=available" \
  --query 'Images | sort_by(@, &CreationDate) | [-1].ImageId' \
  --output text --region "$REGION")

echo "=== Pipeline Launch Plan ==="
echo "  Environments:    $TOTAL_ENVS"
echo "  Env generators:  $NUM_GENERATORS  (m5.xlarge)"
echo "  Agent testers:   $NUM_TESTERS  (c5.4xlarge)"
echo "  Controller:      1  (t3.medium)"
echo "  Region:          $REGION"
echo "  Base AMI:        $AL2023_AMI"
echo ""

# --- IAM role for SQS access ---
ROLE_NAME="mirror-mirror-ec2"
if ! aws iam get-role --role-name "$ROLE_NAME" 2>/dev/null; then
  echo "Creating IAM role: $ROLE_NAME"
  aws iam create-role --role-name "$ROLE_NAME" \
    --assume-role-policy-document '{
      "Version": "2012-10-17",
      "Statement": [{"Effect": "Allow", "Principal": {"Service": "ec2.amazonaws.com"}, "Action": "sts:AssumeRole"}]
    }' > /dev/null
  aws iam attach-role-policy --role-name "$ROLE_NAME" \
    --policy-arn arn:aws:iam::aws:policy/AmazonSQSFullAccess
  aws iam create-instance-profile --instance-profile-name "$ROLE_NAME" > /dev/null
  aws iam add-role-to-instance-profile --instance-profile-name "$ROLE_NAME" --role-name "$ROLE_NAME"
  echo "  Waiting for IAM propagation..."
  sleep 10
fi

# --- Common user-data header (shared by all instance types) ---
read -r -d '' USERDATA_COMMON << 'COMMON_EOF' || true
#!/bin/bash
set -uo pipefail   # no -e: don't abort on individual command failures
exec > /var/log/mirror-mirror-setup.log 2>&1

export HOME=/home/ec2-user
cd $HOME

# System packages
dnf update -y
dnf install -y git gcc gcc-c++ make openssl-devel bzip2-devel \
  libffi-devel zlib-devel readline-devel sqlite-devel

# Python via uv
su - ec2-user -c 'curl -LsSf https://astral.sh/uv/install.sh | sh'
su - ec2-user -c 'export PATH="$HOME/.local/bin:$PATH" && uv python install 3.12'

# Create venv
su - ec2-user -c 'export PATH="$HOME/.local/bin:$PATH" && uv venv $HOME/venv --python 3.12'
echo 'export PATH="$HOME/venv/bin:$HOME/.local/bin:$PATH"' >> /home/ec2-user/.bashrc

# Node.js 20
curl -fsSL https://rpm.nodesource.com/setup_20.x | bash -
dnf install -y nodejs

# Git config
su - ec2-user -c 'git config --global user.email "mirror-mirror-bot@example.com"'
su - ec2-user -c 'git config --global user.name "mirror-mirror-bot"'

mkdir -p /tmp/mirror-mirror-logs
chown ec2-user:ec2-user /tmp/mirror-mirror-logs
COMMON_EOF

# --- Env Generator user-data (installs everything but does NOT start worker) ---
gen_userdata() {
  cat <<EOF
${USERDATA_COMMON}

# Claude Code CLI
npm install -g @anthropic-ai/claude-code

# Python deps
su - ec2-user -c 'export PATH="\$HOME/.local/bin:\$PATH" && VIRTUAL_ENV=\$HOME/venv uv pip install requests python-dotenv boto3'

# Clone repo
su - ec2-user -c 'git clone https://${GITHUB_TOKEN}@github.com/shuyanzhou/mirror-mirror.git /home/ec2-user/mirror-mirror'

# Write env vars
cat >> /home/ec2-user/.bashrc <<ENVVARS
export GITHUB_TOKEN="${GITHUB_TOKEN}"
export AWS_REGION="${REGION}"
export GENERATE_QUEUE_URL="${GENERATE_QUEUE_URL}"
export EVAL_QUEUE_URL="${EVAL_QUEUE_URL}"
export EVAL_DONE_QUEUE_URL="${EVAL_DONE_QUEUE_URL}"
export PIPELINE_DONE_QUEUE_URL="${PIPELINE_DONE_QUEUE_URL}"
export TOTAL_ENVS="${TOTAL_ENVS}"
ENVVARS

# Signal setup complete
touch /home/ec2-user/.setup-complete
echo "Setup complete. SSH in to run: claude login"
echo "Then start the worker with:"
echo "  cd ~/mirror-mirror && nohup python infra/env_worker.py > /tmp/mirror-mirror-logs/env-worker.log 2>&1 &"
EOF
}

# --- Agent Tester user-data ---
agent_userdata() {
  cat <<EOF
${USERDATA_COMMON}

# Chromium dependencies
dnf install -y alsa-lib atk at-spi2-atk cups-libs libdrm mesa-libgbm \
  pango libXcomposite libXdamage libXrandr libxkbcommon nss nspr

# Write env vars first (so they're available even if later steps fail)
cat >> /home/ec2-user/.bashrc <<ENVVARS
export GOOGLE_API_KEY="${GOOGLE_API_KEY}"
export GITHUB_TOKEN="${GITHUB_TOKEN}"
export AWS_REGION="${REGION}"
export EVAL_QUEUE_URL="${EVAL_QUEUE_URL}"
export EVAL_DONE_QUEUE_URL="${EVAL_DONE_QUEUE_URL}"
ENVVARS

# Python deps (playwright must be explicit — browser-use alone doesn't install the CLI)
su - ec2-user -c 'export PATH="\$HOME/.local/bin:\$PATH" && VIRTUAL_ENV=\$HOME/venv uv pip install playwright "browser-use>=0.11.9" requests python-dotenv boto3'

# Playwright + Chromium (install-deps needs sudo for system packages)
su - ec2-user -c '\$HOME/venv/bin/python -m playwright install chromium'
\$HOME/venv/bin/python -m playwright install-deps || dnf install -y alsa-lib nss nspr atk cups-libs mesa-libgbm pango libXcomposite libXdamage libXrandr

# Clone repo
su - ec2-user -c 'git clone https://${GITHUB_TOKEN}@github.com/shuyanzhou/mirror-mirror.git /home/ec2-user/mirror-mirror'

# Start agent worker
su - ec2-user -c 'cd /home/ec2-user/mirror-mirror && nohup python infra/agent_worker.py --workers 8 > /tmp/mirror-mirror-logs/agent-worker.log 2>&1 &'
echo "Agent worker started"
EOF
}

# --- Controller user-data ---
controller_userdata() {
  cat <<EOF
${USERDATA_COMMON}

# Write env vars first
cat >> /home/ec2-user/.bashrc <<ENVVARS
export AWS_REGION="${REGION}"
export GENERATE_QUEUE_URL="${GENERATE_QUEUE_URL}"
export PIPELINE_DONE_QUEUE_URL="${PIPELINE_DONE_QUEUE_URL}"
export TOTAL_ENVS="${TOTAL_ENVS}"
ENVVARS

# Python deps
su - ec2-user -c 'export PATH="\$HOME/.local/bin:\$PATH" && VIRTUAL_ENV=\$HOME/venv uv pip install boto3'

# Clone repo
su - ec2-user -c 'git clone https://${GITHUB_TOKEN}@github.com/shuyanzhou/mirror-mirror.git /home/ec2-user/mirror-mirror'

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

# Env generators go in PUBLIC subnet (need SSH for claude login)
echo "=== Launching $NUM_GENERATORS Env Generator(s) ==="
GEN_IDS=""
for i in $(seq 1 "$NUM_GENERATORS"); do
  GEN_ID=$(aws ec2 run-instances \
    --image-id "$AL2023_AMI" \
    --instance-type m5.xlarge \
    --key-name "$KEY_PAIR_NAME" \
    --subnet-id "$PUB_SUBNET" \
    --security-group-ids "$SG_ENV" "$SG_CTRL" \
    --iam-instance-profile Name="$ROLE_NAME" \
    --user-data "$(gen_userdata | base64)" \
    --block-device-mappings '[{"DeviceName":"/dev/xvda","Ebs":{"VolumeSize":30}}]' \
    --tag-specifications "ResourceType=instance,Tags=[{Key=Name,Value=mm-env-gen-$i},{Key=Project,Value=mirror-mirror},{Key=Role,Value=env-generator}]" \
    --query 'Instances[0].InstanceId' --output text --region "$REGION")
  echo "  Env Generator $i: $GEN_ID"
  INSTANCE_IDS="$INSTANCE_IDS $GEN_ID"
  GEN_IDS="$GEN_IDS $GEN_ID"
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

# --- Wait for env generators to get public IPs ---
echo ""
echo "=== Waiting for env generator IPs ==="
sleep 5
for gen_id in $GEN_IDS; do
  GEN_IP=$(aws ec2 describe-instances --instance-ids "$gen_id" \
    --query 'Reservations[0].Instances[0].PublicIpAddress' --output text --region "$REGION")
  echo "  $gen_id → $GEN_IP"
done

# --- Save instance info ---
LAUNCH_FILE="/tmp/mirror-mirror-instances.env"
cat > "$LAUNCH_FILE" <<EOF
# Generated by launch_pipeline.sh — $(date -u +%Y-%m-%dT%H:%M:%SZ)
INSTANCE_IDS="$INSTANCE_IDS"
CTRL_ID=$CTRL_ID
GEN_IDS="$GEN_IDS"
TOTAL_ENVS=$TOTAL_ENVS
NUM_GENERATORS=$NUM_GENERATORS
NUM_TESTERS=$NUM_TESTERS
EOF
echo ""
echo "=== All instances launched ==="
echo "Instance IDs saved to $LAUNCH_FILE"
echo ""
echo "=== ACTION REQUIRED ==="
echo "SSH into each env generator and run 'claude login', then start the worker:"
echo ""
for gen_id in $GEN_IDS; do
  GEN_IP=$(aws ec2 describe-instances --instance-ids "$gen_id" \
    --query 'Reservations[0].Instances[0].PublicIpAddress' --output text --region "$REGION")
  echo "  ssh -i ~/.ssh/${KEY_PAIR_NAME}.pem ec2-user@${GEN_IP}"
  echo "    # Wait for setup: tail -f /var/log/mirror-mirror-setup.log"
  echo "    # Then: claude login"
  echo "    # Then: claude plugins install frontend-design"
  echo "    # Then: cd ~/mirror-mirror && nohup python infra/env_worker.py > /tmp/mirror-mirror-logs/env-worker.log 2>&1 &"
  echo ""
done
echo "Controller and agent testers will auto-start once setup completes (~5-10 min)."
echo ""
echo "Monitor:"
echo "  bash infra/setup/monitor_pipeline.sh"
echo ""
echo "Tear down:"
echo "  bash infra/setup/teardown.sh"
