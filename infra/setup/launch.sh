#!/usr/bin/env bash
# Simplified EC2 launcher for the self-contained pipeline.
#
# Each environment runs on one EC2 instance (no SQS, no cross-machine
# coordination).  For N environments, launch N independent instances.
#
# Prerequisites:
#   Set these env vars (or source .env):
#     GITHUB_TOKEN       — for git clone/push on EC2 instances
#     KEY_PAIR_NAME      — your EC2 key pair name
#     GOOGLE_API_KEY     — for Gemini eval agent (optional if using --model gpt)
#     OPENAI_API_KEY     — for GPT eval agent (optional if using --model gemini)
#
# Usage:
#   bash infra/setup/launch.sh --manifest infra/env_manifest.jsonl --model gemini
#   bash infra/setup/launch.sh --manifest infra/env_manifest.jsonl --ami ami-0abc123 --model gemini
#   bash infra/setup/launch.sh --manifest infra/env_manifest.jsonl --instance-type m5.2xlarge --key-pair my-key
#   bash infra/setup/launch.sh --manifest infra/env_manifest.jsonl --model gpt --workers 8 --repetitions 5

set -euo pipefail

# --- Load .env if present ---
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
set -a && source "$REPO_ROOT/.env" && set +a

# --- Defaults ---
MANIFEST="infra/env_manifest.jsonl"
INSTANCE_TYPE="m5.4xlarge"
KEY_PAIR="${KEY_PAIR_NAME:-}"
MODEL="gemini"
WORKERS="8"
REPETITIONS="3"
MAX_ITERATIONS="3"
REGION="${AWS_REGION:-us-east-1}"
SG_ID=""
SUBNET_ID=""
CUSTOM_AMI=""
LAUNCH_FILE="/tmp/mirror-mirror-launch.env"

# --- Parse arguments ---
while [[ $# -gt 0 ]]; do
  case "$1" in
    --manifest)       MANIFEST="$2";       shift 2 ;;
    --instance-type)  INSTANCE_TYPE="$2";  shift 2 ;;
    --key-pair)       KEY_PAIR="$2";       shift 2 ;;
    --model)          MODEL="$2";          shift 2 ;;
    --workers)        WORKERS="$2";        shift 2 ;;
    --repetitions)    REPETITIONS="$2";    shift 2 ;;
    --max-iterations) MAX_ITERATIONS="$2"; shift 2 ;;
    --region)         REGION="$2";         shift 2 ;;
    --security-group) SG_ID="$2";          shift 2 ;;
    --subnet)         SUBNET_ID="$2";      shift 2 ;;
    --ami)            CUSTOM_AMI="$2";     shift 2 ;;
    --launch-file)    LAUNCH_FILE="$2";    shift 2 ;;
    *)
      echo "Unknown argument: $1"
      echo "Usage: bash infra/setup/launch.sh --manifest FILE [OPTIONS]"
      exit 1
      ;;
  esac
done

# --- Validate ---
for var in GITHUB_TOKEN KEY_PAIR; do
  val="${!var:-}"
  if [ -z "$val" ]; then
    echo "ERROR: $var is not set."
    echo ""
    echo "Required env vars:"
    echo "  GITHUB_TOKEN     — for git clone/push"
    echo "  KEY_PAIR_NAME    — EC2 key pair (or pass --key-pair)"
    echo ""
    echo "Optional (depending on --model):"
    echo "  GOOGLE_API_KEY   — for Gemini agent"
    echo "  OPENAI_API_KEY   — for GPT agent"
    exit 1
  fi
done

if [ ! -f "$MANIFEST" ]; then
  echo "ERROR: Manifest file not found: $MANIFEST"
  exit 1
fi

# --- Read manifest ---
ENVS=()
while IFS= read -r line; do
  [ -z "$line" ] && continue
  ENVS+=("$line")
done < "$MANIFEST"
NUM_ENVS=${#ENVS[@]}

if [ "$NUM_ENVS" -eq 0 ]; then
  echo "ERROR: No environments found in $MANIFEST"
  exit 1
fi

echo "=== Pipeline Launch Plan ==="
echo "  Environments:    $NUM_ENVS"
echo "  Instance type:   $INSTANCE_TYPE"
echo "  Model:           $MODEL"
echo "  Workers/inst:    $WORKERS"
echo "  Repetitions:     $REPETITIONS"
echo "  Max iterations:  $MAX_ITERATIONS"
echo "  Region:          $REGION"
echo ""

# --- Resolve AMI ---
if [ -n "$CUSTOM_AMI" ]; then
  LAUNCH_AMI="$CUSTOM_AMI"
  echo "  Custom AMI:      $LAUNCH_AMI (pre-built base)"
else
  LAUNCH_AMI=$(aws ec2 describe-images \
    --owners amazon \
    --filters "Name=name,Values=al2023-ami-2023*-x86_64" "Name=state,Values=available" \
    --query 'Images | sort_by(@, &CreationDate) | [-1].ImageId' \
    --output text --region "$REGION")
  echo "  Base AMI:        $LAUNCH_AMI (Amazon Linux 2023 — full setup)"
fi

# --- Security group (create simple one if not provided) ---
if [ -z "$SG_ID" ]; then
  # Get default VPC
  VPC_ID=$(aws ec2 describe-vpcs --filters "Name=isDefault,Values=true" \
    --query 'Vpcs[0].VpcId' --output text --region "$REGION" 2>/dev/null || true)

  if [ -z "$VPC_ID" ] || [ "$VPC_ID" = "None" ]; then
    echo "No default VPC found. Provide --security-group and --subnet manually."
    exit 1
  fi

  # Check if security group already exists
  SG_ID=$(aws ec2 describe-security-groups \
    --filters "Name=group-name,Values=mm-pipeline" "Name=vpc-id,Values=$VPC_ID" \
    --query 'SecurityGroups[0].GroupId' --output text --region "$REGION" 2>/dev/null || true)

  if [ -z "$SG_ID" ] || [ "$SG_ID" = "None" ]; then
    echo "Creating security group: mm-pipeline"
    SG_ID=$(aws ec2 create-security-group \
      --group-name mm-pipeline \
      --description "Mirror-Mirror pipeline (SSH only)" \
      --vpc-id "$VPC_ID" \
      --query 'GroupId' --output text --region "$REGION")
    aws ec2 authorize-security-group-ingress \
      --group-id "$SG_ID" \
      --protocol tcp --port 22 --cidr 0.0.0.0/0 \
      --region "$REGION" > /dev/null
    echo "  Created: $SG_ID (SSH from anywhere + all outbound)"
  else
    echo "  Reusing security group: $SG_ID"
  fi
fi

# --- Subnet (use default VPC public subnet if not provided) ---
if [ -z "$SUBNET_ID" ]; then
  VPC_ID=$(aws ec2 describe-security-groups --group-ids "$SG_ID" \
    --query 'SecurityGroups[0].VpcId' --output text --region "$REGION")
  SUBNET_ID=$(aws ec2 describe-subnets \
    --filters "Name=vpc-id,Values=$VPC_ID" "Name=default-for-az,Values=true" \
    --query 'Subnets[0].SubnetId' --output text --region "$REGION")
  echo "  Subnet:          $SUBNET_ID"
fi

# --- Pre-create git branches ---
echo ""
echo "=== Pre-creating git branches ==="
for entry in "${ENVS[@]}"; do
  env_id=$(echo "$entry" | python3 -c "import sys,json; print(json.load(sys.stdin)['env_id'])")

  # Check if branch already exists on remote
  if git ls-remote --heads origin "$env_id" | grep -q "$env_id"; then
    echo "  Branch exists: $env_id"
  else
    git branch "$env_id" 2>/dev/null || true
    git push origin "$env_id" 2>/dev/null || true
    echo "  Created branch: $env_id"
  fi
done

# --- IAM role (create if needed) ---
ROLE_NAME="mirror-mirror-ec2"
PROFILE_EXISTS=$(aws iam get-instance-profile --instance-profile-name "$ROLE_NAME" \
  --query 'InstanceProfile.InstanceProfileName' --output text 2>/dev/null || true)

if [ -z "$PROFILE_EXISTS" ] || [ "$PROFILE_EXISTS" = "None" ]; then
  echo ""
  echo "Creating IAM role: $ROLE_NAME"
  aws iam create-role --role-name "$ROLE_NAME" \
    --assume-role-policy-document '{
      "Version": "2012-10-17",
      "Statement": [{"Effect": "Allow", "Principal": {"Service": "ec2.amazonaws.com"}, "Action": "sts:AssumeRole"}]
    }' > /dev/null 2>&1 || true
  aws iam create-instance-profile --instance-profile-name "$ROLE_NAME" > /dev/null 2>&1 || true
  aws iam add-role-to-instance-profile --instance-profile-name "$ROLE_NAME" --role-name "$ROLE_NAME" 2>/dev/null || true
  echo "  Waiting for IAM propagation..."
  sleep 10
fi

# --- Attach S3 results upload policy to EC2 role ---
S3_BUCKET="${MM_S3_BUCKET:-mirror-mirror-results}"
echo "Attaching S3 results policy to $ROLE_NAME (bucket: $S3_BUCKET)"
aws iam put-role-policy \
  --role-name "$ROLE_NAME" \
  --policy-name "mirror-mirror-s3-results" \
  --policy-document "{
    \"Version\": \"2012-10-17\",
    \"Statement\": [{
      \"Sid\": \"MirrorMirrorResultsUpload\",
      \"Effect\": \"Allow\",
      \"Action\": [\"s3:PutObject\", \"s3:GetObject\", \"s3:ListBucket\"],
      \"Resource\": [\"arn:aws:s3:::${S3_BUCKET}\", \"arn:aws:s3:::${S3_BUCKET}/*\"]
    }]
  }" 2>/dev/null || echo "  WARNING: Could not attach S3 policy (role may not exist yet)"

# --- Build user-data ---
# Env-specific setup shared by both modes (clone repo, .claudeignore, env vars)
build_env_setup() {
  local env_id="$1"
  local docs_path="$2"

  cat <<ENVSETUP_EOF

# Clone repo and checkout branch (retry up to 3 times for transient network errors)
for attempt in 1 2 3; do
  su - ec2-user -c 'git clone --branch ${env_id} https://${GITHUB_TOKEN}@github.com/shuyanzhou/mirror-mirror.git /home/ec2-user/mirror-mirror' && break
  echo "Clone attempt \$attempt failed, retrying in 10s..."
  rm -rf /home/ec2-user/mirror-mirror
  sleep 10
done

if [ ! -d /home/ec2-user/mirror-mirror/.git ]; then
  echo "FATAL: git clone failed after 3 attempts"
  exit 1
fi

# Generate .claudeignore (local only — never committed)
# Hides other apps and irrelevant product docs so Claude stays focused.
REPO=/home/ec2-user/mirror-mirror
REFERENCE_APP="gitlab-org-management"
PRODUCT=\$(echo "${docs_path}" | cut -d'/' -f3)

{
  echo "# Auto-generated — local only, not committed"
  echo "# Hides irrelevant apps and docs for env: ${env_id}"
  echo ""
  echo "# Other apps (keep reference + this env)"
  for app_dir in \$REPO/apps/*/; do
    app_name=\$(basename "\$app_dir")
    [ "\$app_name" = "\$REFERENCE_APP" ] && continue
    [ "\$app_name" = "user-manuals" ] && continue
    [ "\$app_name" = "${env_id}" ] && continue
    echo "apps/\$app_name/"
  done
  echo ""
  echo "# Other product docs (keep \$PRODUCT)"
  for product_dir in \$REPO/apps/user-manuals/*/; do
    pname=\$(basename "\$product_dir")
    [ "\$pname" = "\$PRODUCT" ] && continue
    echo "apps/user-manuals/\$pname/"
  done
} > \$REPO/.claudeignore

# Tell git to ignore .claudeignore itself (never track it)
echo ".claudeignore" >> \$REPO/.git/info/exclude
chown ec2-user:ec2-user \$REPO/.claudeignore

# Write env vars
cat >> /home/ec2-user/.bashrc <<ENVVARS
export GITHUB_TOKEN="${GITHUB_TOKEN}"
export GOOGLE_API_KEY="${GOOGLE_API_KEY:-}"
export OPENAI_API_KEY="${OPENAI_API_KEY:-}"
export MM_S3_BUCKET="${S3_BUCKET}"
ENVVARS

# Create logs directory
mkdir -p /tmp/mirror-mirror-logs
chown ec2-user:ec2-user /tmp/mirror-mirror-logs

# Signal setup complete
touch /home/ec2-user/.setup-complete
echo ""
echo "======================================"
echo "Setup complete for: ${env_id}"
echo "======================================"
ENVSETUP_EOF
}

build_userdata() {
  local env_id="$1"
  local docs_path="$2"

  if [ -n "$CUSTOM_AMI" ]; then
    # Pre-built AMI: only env-specific setup needed (pipeline started via SSH)
    cat <<HEADER_EOF
#!/bin/bash
set -uo pipefail
exec > /var/log/mirror-mirror-setup.log 2>&1

export HOME=/home/ec2-user
cd \$HOME

# Clear stale sentinel from AMI so start_pipelines.sh waits for this
# user-data to finish (clone, env vars, etc.) before starting the pipeline.
rm -f /home/ec2-user/.setup-complete
HEADER_EOF
    build_env_setup "$env_id" "$docs_path"
  else
    # Fresh instance: full setup
    cat <<HEADER_EOF
#!/bin/bash
set -uo pipefail
exec > /var/log/mirror-mirror-setup.log 2>&1

export HOME=/home/ec2-user
cd \$HOME

# System packages
dnf update -y
dnf install -y git gcc gcc-c++ make openssl-devel bzip2-devel \\
  libffi-devel zlib-devel readline-devel sqlite-devel tmux

# Chromium dependencies
dnf install -y alsa-lib atk at-spi2-atk cups-libs libdrm mesa-libgbm \\
  pango libXcomposite libXdamage libXrandr libxkbcommon nss nspr

# Python via uv
su - ec2-user -c 'curl -LsSf https://astral.sh/uv/install.sh | sh'
su - ec2-user -c 'export PATH="\$HOME/.local/bin:\$PATH" && uv python install 3.12'

# Create venv
su - ec2-user -c 'export PATH="\$HOME/.local/bin:\$PATH" && uv venv \$HOME/venv --python 3.12'
echo 'export PATH="\$HOME/venv/bin:\$HOME/.local/bin:\$PATH"' >> /home/ec2-user/.bashrc

# Node.js 20
curl -fsSL https://rpm.nodesource.com/setup_20.x | bash -
dnf install -y nodejs

# Claude Code CLI
npm install -g @anthropic-ai/claude-code

# Python deps
su - ec2-user -c 'export PATH="\$HOME/.local/bin:\$PATH" && VIRTUAL_ENV=\$HOME/venv uv pip install playwright "browser-use>=0.11.9" requests python-dotenv'

# Playwright + Chromium
su - ec2-user -c '\$HOME/venv/bin/python -m playwright install chromium'
\$HOME/venv/bin/python -m playwright install-deps || true

# Git config
su - ec2-user -c 'git config --global user.email "mirror-mirror-bot@example.com"'
su - ec2-user -c 'git config --global user.name "mirror-mirror-bot"'
HEADER_EOF
    build_env_setup "$env_id" "$docs_path"

    # Fresh instances need manual claude login before pipeline can run
    cat <<NOTE_EOF

echo ""
echo "NOTE: This is a fresh instance. You must also run:"
echo "  1. claude login"
echo "  2. claude plugins install frontend-design"
echo "  3. Start pipeline:"
echo "     cd ~/mirror-mirror && nohup \\\$HOME/venv/bin/python infra/pipeline.py \\\\"
echo "       --app-name ${env_id} --docs-path ${docs_path} \\\\"
echo "       --model ${MODEL} --workers ${WORKERS} --repetitions ${REPETITIONS} \\\\"
echo "       --max-iterations ${MAX_ITERATIONS} --branch ${env_id} \\\\"
echo "       --push --s3-bucket \\\$MM_S3_BUCKET \\\\"
echo "       > /tmp/mirror-mirror-logs/pipeline.log 2>&1 &"
NOTE_EOF
  fi
}

# --- AWS CLI v1 vs v2 compatibility ---
# CLI v1 requires manual base64 encoding of --user-data; CLI v2 auto-encodes.
if aws --version 2>&1 | grep -q "^aws-cli/1\."; then
  maybe_base64() { base64; }
else
  maybe_base64() { cat; }
fi

# --- Launch instances ---
echo ""
echo "=== Launching $NUM_ENVS instance(s) ==="
INSTANCE_IDS=""
EIP_ALLOC_IDS=""

for entry in "${ENVS[@]}"; do
  env_id=$(echo "$entry" | python3 -c "import sys,json; print(json.load(sys.stdin)['env_id'])")
  docs_path=$(echo "$entry" | python3 -c "import sys,json; print(json.load(sys.stdin)['docs_path'])")

  INST_ID=$(aws ec2 run-instances \
    --image-id "$LAUNCH_AMI" \
    --instance-type "$INSTANCE_TYPE" \
    --key-name "$KEY_PAIR" \
    --subnet-id "$SUBNET_ID" \
    --security-group-ids "$SG_ID" \
    --iam-instance-profile Name="$ROLE_NAME" \
    --block-device-mappings '[{"DeviceName":"/dev/xvda","Ebs":{"VolumeSize":50}}]' \
    --user-data "$(build_userdata "$env_id" "$docs_path" | maybe_base64)" \
    --tag-specifications "ResourceType=instance,Tags=[{Key=Name,Value=mm-pipeline-${env_id}},{Key=Project,Value=mirror-mirror},{Key=Role,Value=pipeline},{Key=EnvId,Value=${env_id}}]" \
    --query 'Instances[0].InstanceId' --output text --region "$REGION")

  echo "  $env_id → $INST_ID"
  INSTANCE_IDS="$INSTANCE_IDS $INST_ID"
done

# --- Allocate Elastic IPs and associate ---
echo ""
echo "=== Allocating Elastic IPs ==="
echo "  Waiting for instances to enter running state..."
for INST_ID in $INSTANCE_IDS; do
  aws ec2 wait instance-running --instance-ids "$INST_ID" --region "$REGION"
done

for INST_ID in $INSTANCE_IDS; do
  ENV_ID=$(aws ec2 describe-instances --instance-ids "$INST_ID" \
    --query 'Reservations[0].Instances[0].Tags[?Key==`EnvId`].Value | [0]' --output text --region "$REGION")

  # Allocate an Elastic IP
  EIP_JSON=$(aws ec2 allocate-address --domain vpc \
    --tag-specifications "ResourceType=elastic-ip,Tags=[{Key=Name,Value=mm-eip-${ENV_ID}},{Key=Project,Value=mirror-mirror},{Key=EnvId,Value=${ENV_ID}}]" \
    --region "$REGION")
  ALLOC_ID=$(echo "$EIP_JSON" | python3 -c "import sys,json; print(json.load(sys.stdin)['AllocationId'])")
  EIP=$(echo "$EIP_JSON" | python3 -c "import sys,json; print(json.load(sys.stdin)['PublicIp'])")

  # Associate with instance
  aws ec2 associate-address --instance-id "$INST_ID" --allocation-id "$ALLOC_ID" \
    --region "$REGION" > /dev/null

  echo "  $ENV_ID → $EIP (eip: $ALLOC_ID)"
  EIP_ALLOC_IDS="$EIP_ALLOC_IDS $ALLOC_ID"
done

# --- Save launch info ---
cat > "$LAUNCH_FILE" <<EOF
# Generated by launch.sh — $(date -u +%Y-%m-%dT%H:%M:%SZ)
INSTANCE_IDS="$INSTANCE_IDS"
EIP_ALLOC_IDS="$EIP_ALLOC_IDS"
NUM_ENVS=$NUM_ENVS
MODEL=$MODEL
WORKERS=$WORKERS
REPETITIONS=$REPETITIONS
MAX_ITERATIONS=$MAX_ITERATIONS
KEY_PAIR=$KEY_PAIR
REGION=$REGION
EOF

echo "" >> "$LAUNCH_FILE"
echo "# Per-instance details (env_id|instance_id|elastic_ip|eip_alloc_id)" >> "$LAUNCH_FILE"

# --- Record per-instance details ---
echo ""

for INST_ID in $INSTANCE_IDS; do
  IP=$(aws ec2 describe-instances --instance-ids "$INST_ID" \
    --query 'Reservations[0].Instances[0].PublicIpAddress' --output text --region "$REGION")
  ENV_ID=$(aws ec2 describe-instances --instance-ids "$INST_ID" \
    --query 'Reservations[0].Instances[0].Tags[?Key==`EnvId`].Value | [0]' --output text --region "$REGION")
  ALLOC_ID=$(aws ec2 describe-addresses --filters "Name=instance-id,Values=$INST_ID" \
    --query 'Addresses[0].AllocationId' --output text --region "$REGION")

  echo "# ${ENV_ID}|${INST_ID}|${IP}|${ALLOC_ID}" >> "$LAUNCH_FILE"
  echo "  $ENV_ID → $IP"
done

echo ""
echo "Instance info saved to: $LAUNCH_FILE"

# --- For AMI mode: poll + start pipelines via SSH ---
if [ -n "$CUSTOM_AMI" ]; then
  echo ""
  bash infra/setup/start_pipelines.sh --manifest "$MANIFEST" --launch-file "$LAUNCH_FILE"
else
  echo ""
  echo "=== ACTION REQUIRED ==="
  echo "SSH into each instance, run 'claude login', install plugins, then start the pipeline:"
  echo ""
  for INST_ID in $INSTANCE_IDS; do
    IP=$(aws ec2 describe-instances --instance-ids "$INST_ID" \
      --query 'Reservations[0].Instances[0].PublicIpAddress' --output text --region "$REGION")
    echo "  ssh -i ~/.ssh/${KEY_PAIR}.pem ec2-user@${IP}"
    echo "    # Wait for setup: tail -f /var/log/mirror-mirror-setup.log"
    echo "    # Then: claude login && claude plugins install frontend-design"
    echo "    # Then: start pipeline (command shown at end of setup log)"
    echo ""
  done
fi

echo ""
echo "NOTE: Elastic IPs are stable across stop/start cycles."
echo "      To release them during teardown, run:"
echo "        bash infra/setup/teardown.sh --release-eips"
echo ""
echo "Monitor progress:"
echo "  bash infra/setup/monitor.sh"
echo ""
echo "Tear down:"
echo "  bash infra/setup/teardown.sh"
