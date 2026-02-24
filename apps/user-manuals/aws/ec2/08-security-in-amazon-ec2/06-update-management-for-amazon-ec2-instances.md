# Update management for Amazon EC2 instances

Source: apps/user-manuals/aws/ec2-ug.pdf

---

- AWS Security Token Service (AWS STS) – Instance identity role credentials can be used with the AWS STS GetCallerIdentity action.
- AWS Systems Manager – When using Default Host Management Configuration, AWS Systems Manager uses the identity provided by the instance identity role to register EC2 instances. After identifying your instance, Systems Manager can pass your AWSSystemsManagerDefaultEC2InstanceManagementRole IAM role to your instance.
Instance identity roles can't be used with other AWS services or features because they do not have an integration with instance identity roles.
#### Instance identity role ARN The instance identity role ARN takes the following format: arn:aws-partition:iam::account-number:assumed-role/aws:ec2-instance/instance-id For example: arn:aws:iam::0123456789012:assumed-role/aws:ec2-instance/i-1234567890abcdef0 For more information about ARNs, see Amazon Resource Names (ARNs) in the IAM User Guide.
# Update management for Amazon EC2 instances We recommend that you regularly patch, update, and secure the operating system and applications on your EC2 instances. You can use AWS Systems Manager Patch Manager to automate the process of installing security-related updates for both the operating system and applications.
For EC2 instances in an Auto Scaling group, you can use the AWS-PatchAsgInstance runbook to help avoid instances that are undergoing patching from being replaced. Alternatively, you can use any automatic update services or recommended processes for installing updates that are provided by the application vendor.
Resources
- AL2023 – Updating AL2023 in the Amazon Linux 2023 User Guide
- AL2 – Manage software on your Amazon Linux 2 instance in the Amazon Linux 2 User Guide
