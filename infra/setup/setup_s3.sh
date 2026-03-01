#!/usr/bin/env bash
# One-time S3 bucket setup for results hosting.
#
# Creates an S3 bucket with static website hosting enabled and a public-read
# policy so report.html files are directly browsable.  Also attaches an inline
# IAM policy to the mirror-mirror-ec2 role so EC2 instances can upload.
#
# Usage:
#   bash infra/setup/setup_s3.sh
#   bash infra/setup/setup_s3.sh --bucket my-custom-bucket --region us-west-2

set -euo pipefail

# --- Defaults ---
BUCKET="${MM_S3_BUCKET:-mirror-mirror-results}"
REGION="${AWS_REGION:-us-east-1}"
ROLE_NAME="mirror-mirror-ec2"

# --- Parse arguments ---
while [[ $# -gt 0 ]]; do
  case "$1" in
    --bucket) BUCKET="$2"; shift 2 ;;
    --region) REGION="$2"; shift 2 ;;
    --role)   ROLE_NAME="$2"; shift 2 ;;
    *)
      echo "Unknown argument: $1"
      echo "Usage: bash infra/setup/setup_s3.sh [--bucket NAME] [--region REGION] [--role ROLE]"
      exit 1
      ;;
  esac
done

echo "=== S3 Results Bucket Setup ==="
echo "  Bucket: $BUCKET"
echo "  Region: $REGION"
echo "  IAM Role: $ROLE_NAME"
echo ""

# --- Create bucket ---
if aws s3api head-bucket --bucket "$BUCKET" 2>/dev/null; then
  echo "Bucket already exists: $BUCKET"
else
  echo "Creating bucket: $BUCKET"
  if [ "$REGION" = "us-east-1" ]; then
    aws s3api create-bucket --bucket "$BUCKET" --region "$REGION"
  else
    aws s3api create-bucket --bucket "$BUCKET" --region "$REGION" \
      --create-bucket-configuration LocationConstraint="$REGION"
  fi
  echo "  Created."
fi

# --- Enable static website hosting ---
echo "Enabling static website hosting..."
aws s3 website "s3://$BUCKET/" --index-document index.html --region "$REGION"
echo "  Website endpoint: http://$BUCKET.s3-website-$REGION.amazonaws.com/"

# --- Disable block public access ---
echo "Disabling block public access..."
aws s3api put-public-access-block --bucket "$BUCKET" \
  --public-access-block-configuration \
  "BlockPublicAcls=false,IgnorePublicAcls=false,BlockPublicPolicy=false,RestrictPublicBuckets=false" \
  --region "$REGION"

# --- Set public-read bucket policy ---
echo "Setting public-read bucket policy..."
POLICY=$(cat <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "PublicReadGetObject",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::$BUCKET/*"
    }
  ]
}
EOF
)
aws s3api put-bucket-policy --bucket "$BUCKET" --policy "$POLICY" --region "$REGION"
echo "  Public-read policy applied."

# --- Attach IAM policy to EC2 role ---
echo "Attaching S3 upload policy to IAM role: $ROLE_NAME"
S3_POLICY=$(cat <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "MirrorMirrorResultsUpload",
      "Effect": "Allow",
      "Action": [
        "s3:PutObject",
        "s3:GetObject",
        "s3:ListBucket"
      ],
      "Resource": [
        "arn:aws:s3:::$BUCKET",
        "arn:aws:s3:::$BUCKET/*"
      ]
    }
  ]
}
EOF
)
aws iam put-role-policy \
  --role-name "$ROLE_NAME" \
  --policy-name "mirror-mirror-s3-results" \
  --policy-document "$S3_POLICY" 2>/dev/null || {
    echo "  WARNING: Could not attach policy to role '$ROLE_NAME'."
    echo "  The role may not exist yet. It will be created by launch.sh."
    echo "  Re-run this script after launch.sh, or the policy will be"
    echo "  attached by launch.sh itself."
  }

echo ""
echo "=== Setup Complete ==="
echo "  Website URL: http://$BUCKET.s3-website-$REGION.amazonaws.com/"
echo ""
echo "Test with:"
echo "  aws s3 cp some-file.html s3://$BUCKET/test/report.html"
echo "  open http://$BUCKET.s3-website-$REGION.amazonaws.com/test/report.html"
