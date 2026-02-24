# Track your Free Tier usage for Amazon EC2

Source: apps/user-manuals/aws/ec2-ug.pdf

---

Feedback You can provide feedback on automatically generated insights on detected problems by designating them useful or not useful. Your feedback on the insights, along with your application diagnostics (metric anomalies and log exceptions), are used to improve the future detection of similar problems.
For more information, see the CloudWatch Application Insights documentation in the Amazon CloudWatch User Guide.
# Track your Free Tier usage for Amazon EC2 When you create your AWS account, you can get started with Amazon EC2 for free using the AWS Free Tier. Your Free Tier benefits are different depending on whether you created your account before July 15, 2025, or on or after July 15, 2025. For more information, see Explore AWS services with AWS Free Tier in the AWS Billing User Guide.
## Free Tier benefits before and after July 15, 2025 The following table compares your Free Tier benefits based on your AWS account creation date:
Free Tier benefit Account created before July 15, 2025 Account created on or after July 15, 2025 Instance types marked Free tier eligible t2.micro, t3.micro t3.micro, t3.small, t4g.micro , t4g.small , c7i-flex.large , m7i- flex.large Amazon EBS volume types marked Free tier eligible standard, st1, sc1, gp2, and gp3 standard, st1, sc1, gp2, and gp3 AMIs marked Free tier eligible Check for AMIs marked Free tier eligible.
Check for AMIs marked Free tier eligible.
Usage limit Restricted to usage limits, after which you are billed pay-as-you-go rates.
Receive USD $100 sign-up credit and earn up to $100 in additional credits.

Free Tier benefit Account created before July 15, 2025 Account created on or after July 15, 2025 Free Tier duration Your Free Tier lasts for 12 months from the date you create your account. During this time, if you exceed your Free Tier usage limits, you are billed pay-as-you-go rates.
Your Free Tier lasts for 6 months from the date you created your account, or when your credits are used up, whichever happens first. You can't exceed your Free Tier limits.
To list the instance types that are free tier eligible Use the describe-instance-types command with the free-tier-eligible filter. aws ec2 describe-instance-types \ --filters Name=free-tier-eligible,Values=true \ --query "InstanceTypes[*].[InstanceType]" \ --output text | sort To list the AMIs that are free tier eligible Use the describe-images command with the free-tier-eligible filter. aws ec2 describe-images \ --filters Name=free-tier-eligible,Values=true \ --query "Images[*].[ImageId]" \ --output text | sort
## Track Free Tier usage for accounts created before July 15, 2025 Note This section only applies to Free Tier users who created AWS accounts before July 15,
2025. If you created your account on or after July 15, 2025, see Tracking your AWS Free Tier usage in the AWS Billing User Guide.

If you created your account before July 15, 2025, you can use Amazon EC2 without incurring charges if you've been an AWS customer for less than 12 months and you stay within the AWS Free Tier usage limits. It's important to track your Free Tier usage to avoid billing surprises. If you exceed the Free Tier limits, you'll incur standard pay-as-go charges. For more information, see AWS Free Tier.
Note If you've been an AWS customer for more than 12 months, you're no longer eligible for Free Tier usage and you won't see the EC2 Free Tier box that is described in the following procedure.
To track your Free Tier usage
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose EC2 Dashboard.
3. Find the EC2 Free Tier box (at top right).

4. In the EC2 Free Tier box, check your Free Tier usage, as follows:
- Under EC2 Free Tier offers in use, take note of the warnings:
- End of month forecast – This warns that you will incur charges this month if you continue with your current usage pattern.
- Exceeds Free Tier – This warns that you've exceeded your Free Tier limits and you're already incurring charges.
