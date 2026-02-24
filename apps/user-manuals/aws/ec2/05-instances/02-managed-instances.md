# Amazon EC2 managed instances

Source: apps/user-manuals/aws/ec2-ug.pdf

---

- Storage optimized: d3en.12xlarge | dl1.24xlarge | i3en.12xlarge | i3en.24xlarge | i4i.16xlarge | i7i.large | i7i.xlarge | i7i.2xlarge | i7i.4xlarge | i7i.8xlarge
| i7i.12xlarge | i7i.16xlarge | i7i.24xlarge | i7i.48xlarge | i7ie.large | i7ie.xlarge | i7ie.2xlarge | i7ie.3xlarge | i7ie.6xlarge | i7ie.12xlarge | i7ie.18xlarge | i7ie.24xlarge | i7ie.48xlarge | r5b.12xlarge | r5b.24xlarge
- Accelerated computing: dl1.24xlarge | f2.6xlarge | f2.12xlarge | f2.48xlarge
| g5.24xlarge | g5.48xlarge | g6.24xlarge | g6.48xlarge | g6e.12xlarge | g6e.24xlarge | g6e.48xlarge | g7e.2xlarge | g7e.4xlarge | g7e.8xlarge | g7e.12xlarge | g7e.24xlarge | g7e.48xlarge | inf1.24xlarge | p3dn.24xlarge
| p4d.24xlarge | p4de.24xlarge | p5.48xlarge | p5e.48xlarge | p5en.48xlarge
| p6-b200.48xlarge | p6-b300.48xlarge | trn1.32xlarge | trn2.3xlarge | trn2.48xlarge | trn2a.3xlarge | trn2a.48xlarge | trn2n.3xlarge | trn2n.48xlarge | trn2p.48xlarge | trn2u.48xlarge | vt1.24xlarge
- High-performance computing: hpc7a.12xlarge | hpc7a.24xlarge | hpc7a.48xlarge | hpc7a.96xlarge | hpc8a.96xlarge You might want to change the C-state or P-state settings to increase processor performance consistency, reduce latency, or tune your instance for a specific workload. The default C-state and P-state settings provide maximum performance, which is optimal for most workloads. However, if your application would benefit from reduced latency at the cost of higher single- or dual-core frequencies, or from consistent performance at lower frequencies as opposed to bursty Turbo Boost frequencies, consider experimenting with the C-state or P-state settings that are available to these instances.
For information about different processor configurations and how to monitor the effects of your configuration for Amazon Linux, see Processor state control for Amazon EC2 Amazon Linux instance in the Amazon Linux 2 User Guide. These procedures were written for, and apply to Amazon Linux; however, they might also work for other Linux distributions with a Linux kernel of 3.9 or newer. For more information about other Linux distributions and processor state control, see your system-specific documentation.
# Amazon EC2 managed instances An Amazon EC2 managed instance is an EC2 instance that is provisioned and managed by a designated service provider, such as Amazon EKS through EKS Auto Mode. Managed instances

provide a simplified way for running compute workloads on Amazon EC2 by allowing you to delegate operational control of the instance to a service provider.
Delegated control is the only change introduced for managed instances. The technical specifications and billing remain the same as non-managed EC2 instances. Because managed instances allow you to delegate control to the service provider, you can benefit from the service provider's operational expertise and best practices. When an instance is managed, the service provider is responsible for tasks such as provisioning the instance, configuring software, scaling capacity, handling instance failures and replacements, and terminating the instance.
You can't directly modify the settings of a managed instance or terminate it. The service and specific operations are determined by the agreement between you and the service provider.
However, you can add, modify, or remove tags from your managed instances, allowing you to categorize them within your AWS environment.
Contents
- Billing for managed instances
- Identify managed instances
- Get started with managed instances
## Billing for managed instances An Amazon EC2 managed instance incurs the same base charge as a non-managed Amazon EC2 instance, plus a separate fee for the service provider. This additional fee is charged by the service provider managing your instance and is billed separately. It covers the cost of services provided for operating and maintaining your managed instance.
All Amazon EC2 purchasing options are available for managed instances, including On-Demand Instances, Reserved Instances, Spot Instances, and Savings Plans. By sourcing your compute directly from EC2 and then providing it to your service provider, you benefit from any existing Reserved Instances or Savings Plans applied to your account, ensuring that you're using the most cost- effective compute capacity available.
For example, when using Amazon EKS Auto Mode, you pay the standard EC2 instance rate for the underlying instances, plus an additional charge from Amazon EKS for managing the instances on your behalf. If you then decide to sign up for a Savings Plans, the EC2 instance rate is reduced by the Savings Plans, while the additional charge from Amazon EKS remains unchanged.

## Identify managed instances Managed instances are identified by a true value in the Managed field. The service provider is identified in the Operator field (in the console) or Principal field (in the CLI).
Use the following procedures to identify managed instances.
Console To identify a managed instance
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Instances.
3. Select the instance you want to check.
4. On the Details tab (if you selected the checkbox) or in the summary area (if you selected the instance ID), find the Managed field.
- A value of true indicates a managed instance.
- A value of false indicates a non-managed instance.
5. If Managed is set to true, the Operator field displays a value identifying the service provider responsible for managing the instance. For example, a value of eks.amazonaws.com identifies Amazon EKS as the service provider.
AWS CLI To identify a managed instance Use the describe-instances command and specify the instance ID. aws ec2 describe-instances \ --instance-ids i-1234567890abcdef0 \ --query Reservations[].Instances[].Operator The following is example output. If Managed is true, the instance is a managed instance and a Principal is included. The principal is the service provider that manages the instance. For example, a value of eks.amazonaws.com identifies Amazon EKS as the service provider.
[

    { "Managed": true, "Principal": "eks.amazonaws.com"
    } ]
To find your managed instances Use the describe-instances command and specify the operator.managed filter with a value of true. The --query option displays only the IDs of the managed instances. aws ec2 describe-instances \ --filters "Name=operator.managed,Values=true" \ --query Reservations[*].Instances[].InstanceId PowerShell To identify a managed instance Use the Get-EC2Instance cmdlet.
(Get-EC2Instance -InstanceId i-1234567890abcdef0).Instances.Operator The following is example output.
Managed Principal ------- --------- True    eks.amazonaws.com To find your managed instances Use the Get-EC2Instance cmdlet. This example displays only the IDs of the managed instances.
(Get-EC2Instance -Filter @{Name="operator.managed"; Values="true"}).Instances.InstanceId
## Get started with managed instances For guidance on using managed instances, see Automate cluster infrastructure with EKS Auto Mode in the Amazon EKS User Guide.
