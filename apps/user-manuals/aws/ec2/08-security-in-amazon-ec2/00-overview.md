# Security in Amazon EC2

Source: apps/user-manuals/aws/ec2-ug.pdf

---

# Security in Amazon EC2 Cloud security at AWS is the highest priority. As an AWS customer, you benefit from a data center and network architecture that are built to meet the requirements of the most security-sensitive organizations.
Security is a shared responsibility between AWS and you. The shared responsibility model describes this as security of the cloud and security in the cloud:
- Security of the cloud – AWS is responsible for protecting the infrastructure that runs AWS services in the AWS Cloud. AWS also provides you with services that you can use securely. Third- party auditors regularly test and verify the effectiveness of our security as part of the AWS Compliance Programs. To learn about the compliance programs that apply to Amazon EC2, see AWS Services in Scope by Compliance Program.
- Security in the cloud – Your responsibility includes the following areas:
- Controlling network access to your instances, for example, through configuring your VPC and security groups. For more information, see Controlling network traffic.
- Managing the credentials used to connect to your instances.
- Managing the guest operating system and software deployed to the guest operating system, including updates and security patches. For more information, see Update management for Amazon EC2 instances.
- Configuring the IAM roles that are attached to the instance and the permissions associated with those roles. For more information, see IAM roles for Amazon EC2.
This documentation helps you understand how to apply the shared responsibility model when using Amazon EC2. It shows you how to configure Amazon EC2 to meet your security and compliance objectives. You also learn how to use other AWS services that help you to monitor and secure your Amazon EC2 resources.
Contents
- Data protection in Amazon EC2
- Infrastructure security in Amazon EC2
- Resilience in Amazon EC2
- Compliance validation for Amazon EC2
