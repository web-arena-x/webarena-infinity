# Amazon Machine Images in Amazon EC2

Source: apps/user-manuals/aws/ec2-ug.pdf

---

# Amazon Machine Images in Amazon EC2 An Amazon Machine Image (AMI) is an image that provides the software that is required to set up and boot an Amazon EC2 instance. Each AMI also contains a block device mapping that specifies the block devices to attach to the instances that you launch. You must specify an AMI when you launch an instance. The AMI must be compatible with the instance type that you chose for your instance. You can use an AMI provided by AWS, a public AMI, an AMI that someone else shared with you, or an AMI that you purchased from the AWS Marketplace.
An AMI is specific to the following:
- Region
- Operating system
- Processor architecture
- Root volume type
- Virtualization type You can launch multiple instances from a single AMI when you require multiple instances with the same configuration. You can use different AMIs to launch instances when you require instances

You can create an AMI from your Amazon EC2 instances and then use it to launch instances with the same configuration. You can copy an AMI to another AWS Region, and then use it to launch instances in that Region. You can also share an AMI that you created with other accounts so that they can launch instances with the same configuration. You can sell your AMI using the AWS Marketplace.
Contents
- AMI types and characteristics in Amazon EC2
- Find an AMI that meets the requirements for your EC2 instance
- Paid AMIs in the AWS Marketplace for Amazon EC2 instances
- Amazon EC2 AMI lifecycle
- Instance launch behavior with Amazon EC2 boot modes
- Use encryption with EBS-backed AMIs
- Understand shared AMI usage in Amazon EC2
- Monitor AMI events using Amazon EventBridge
- Understand AMI billing information
