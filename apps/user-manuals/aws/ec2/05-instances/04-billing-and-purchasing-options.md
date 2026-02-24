# Amazon EC2 billing and purchasing options

Source: apps/user-manuals/aws/ec2-ug.pdf

---

5. On the Change CPU options page, for Nested virtualization, choose one of the following options:
- Enable – Turns on nested virtualization for the instance
- Disable – Turns off nested virtualization for the instance
6. Review your changes, and then choose Change to apply the new CPU options.
AWS CLI To enable nested virtualization on an existing instance First stop the instance, and then use the modify-instance-cpu-options command. aws ec2 modify-instance-cpu-options \ --instance-id i-1234567890abcdef0 \ --core-count 4 \ --threads-per-core 2 \ --nested-virtualization enabled PowerShell To enable nested virtualization on an existing instance First stop the instance, and then use the Edit-EC2InstanceCpuOption command.
Edit-EC2InstanceCpuOption `
    -InstanceId i-1234567890abcdef0 `
    -CoreCount 4 `
    -ThreadsPerCore 2 `
    -NestedVirtualization enabled
# Amazon EC2 billing and purchasing options You can use the following options to optimize your costs for Amazon EC2:
- On-Demand Instances – Pay, by the second, for the instances that you launch.
- Savings Plans – Reduce your Amazon EC2 costs by making a commitment to a consistent amount of usage, in USD per hour, for a term of 1 or 3 years.

- Reserved Instances – Reduce your Amazon EC2 costs by making a commitment to a consistent instance configuration, including instance type and Region, for a term of 1 or 3 years.
- Spot Instances – Request unused EC2 instances, which can reduce your Amazon EC2 costs significantly.
- Dedicated Hosts – Pay for a physical host that is fully dedicated to running your instances, and bring your existing per-socket, per-core, or per-VM software licenses to reduce costs.
- Dedicated Instances – Pay, by the hour, for instances that run on single-tenant hardware.
- Capacity Reservations – Reserve capacity for your EC2 instances in a specific Availability Zone.
If you can't make a commitment to a specific instance configuration, but you can commit to a usage amount, purchase Savings Plans to reduce your On-Demand Instance costs. If you require a capacity reservation, purchase Reserved Instances or Capacity Reservations for a specific Availability Zone. Capacity Blocks can be used to reserve a cluster of GPU instances. Spot Instances are a cost-effective choice if you can be flexible about when your applications run and if they can be interrupted. Dedicated Hosts or Dedicated Instances can help you address compliance requirements and reduce costs by using your existing server-bound software licenses.
For more information, see Amazon EC2 Pricing and Amazon EC2 managed instances.
## Purchasing On-Demand Instances for Amazon EC2 With On-Demand Instances, you pay for compute capacity by the second with no long-term commitments. You have full control over the instance's lifecycle—you decide when to launch, stop, hibernate, start, reboot, or terminate it.
There is no long-term commitment required when you purchase On-Demand Instances. You pay only for the seconds that your On-Demand Instances are in the running state, with a 60-second minimum. The price per second for a running On-Demand Instance is fixed, and is listed on the Amazon EC2 Pricing, On-Demand Pricing page.
We recommend that you use On-Demand Instances for applications with short-term, irregular workloads that cannot be interrupted.
For significant savings over On-Demand Instances, use AWS Savings Plans, Spot Instances, or Reserved Instances for Amazon EC2 overview.
Contents
- On-Demand Instance quotas

- Monitor On-Demand Instance quotas and usage
- Request a quota increase
- Query the prices of On-Demand Instances
### On-Demand Instance quotas There are quotas for the number of running On-Demand Instances per AWS account per Region.
On-Demand Instance quotas are managed in terms of the number of virtual central processing units (vCPUs) that your running On-Demand Instances are using, regardless of the instance type. Each quota type specifies the maximum number of vCPUs for one or more instance families.
Your account includes the following quotas for On-Demand Instances. Instances that are in the pending, stopping, stopped, and hibernated states do not count towards your On-Demand Instance quotas. Capacity Reservations count toward your On-Demand Instance quotas, even if they are unused.
Name Default Adjustable Running On-Demand DL instances 0 Yes Running On-Demand F instances 0 Yes Running On-Demand G and VT instances 0 Yes Running On-Demand HPC instances 0 Yes Running On-Demand High Memory instances 0 Yes Running On-Demand Inf instances 0 Yes Running On-Demand P instances 0 Yes Running On-Demand Standard (A, C, D, H, I, M, R, T, Z) instances 5 Yes Running On-Demand Trn instances 0 Yes Running On-Demand X instances 0 Yes

For information about the different instance families, generations, and sizes, see the Amazon EC2 Instance Types Guide.
You can launch any combination of instance types that meet your changing application needs, as long as the number of vCPUs does not exceed your account quota. For example, with a Standard instance quota of 256 vCPUs, you could launch 32 m5.2xlarge instances (32 x 8 vCPUs) or 16 c5.4xlarge instances (16 x 16 vCPUs). For more information, see EC2 On-Demand Instance limits.
Tasks
- Monitor On-Demand Instance quotas and usage
- Request a quota increase
#### Monitor On-Demand Instance quotas and usage You can view and manage your On-Demand Instance quotas for each Region using the following methods.
To view your current quotas using the Service Quotas console
1. Open the Service Quotas console at https://console.aws.amazon.com/servicequotas/home/ services/ec2/quotas/.
2. From the navigation bar, select a Region.
3. In the filter field, enter On-Demand.
4. The Applied quota value column displays the maximum number of vCPUs for each On- Demand Instance quota type for your account.
To view your current quotas using the AWS Trusted Advisor console Open Service limits page in the AWS Trusted Advisor console.
To configure CloudWatch alarms With Amazon CloudWatch metrics integration, you can monitor your EC2 usage against your quotas. You can also configure alarms to warn about approaching quotas. For more information, see Service Quotas and Amazon CloudWatch alarms in the Service Quotas User Guide.

#### Request a quota increase Even though Amazon EC2 automatically increases your On-Demand Instance quotas based on your usage, you can request a quota increase if necessary. For example, if you intend to launch more instances than your current quota allows, you can request a quota increase by using the Service Quotas console described in Amazon EC2 service quotas.
### Query the prices of On-Demand Instances You can use the Price List Service API or the AWS Price List API to query the prices of On-Demand Instances. For more information, see Using the AWS Price List API in the AWS Billing User Guide.
## Reserved Instances for Amazon EC2 overview Important We recommend Savings Plans over Reserved Instances. Saving Plans are the easiest and most flexible way to save money on your AWS compute costs and offer lower prices (up to 72% off On-Demand pricing), just like Reserved Instances. However, Savings Plans are different to Reserved Instances. With Reserved Instances, you make a commitment to a specific instance configuration, whereas with Savings Plans, you have the flexibility to use the instance configurations that best meet your needs. To use Savings Plans, you make a commitment to a consistent usage amount, measured in USD per hour. For more information, see the AWS Savings Plans User Guide.
Reserved Instances provide you with significant savings on your Amazon EC2 costs compared to On-Demand Instance pricing. Reserved Instances are not physical instances, but rather a billing discount applied to the use of On-Demand Instances in your account. These On-Demand Instances must match certain attributes, such as instance type and Region, in order to benefit from the billing discount.
Reserved Instances topics
- Reserved Instance example scenario
- Key variables that determine Reserved Instance pricing
- Regional and zonal Reserved Instances (scope)
- Types of Reserved Instances (offering classes)
- How Reserved Instance discounts are applied

- Use your Reserved Instances
- How billing works with Reserved Instances
- Buy Reserved Instances for Amazon EC2
- Sell Reserved Instances for Amazon EC2 in the Reserved Instance Marketplace
- Modify Reserved Instances
- Exchange Convertible Reserved Instances
- Reserved Instance quotas
### Reserved Instance example scenario The following diagram shows a basic scenario of purchasing and using Reserved Instances.
In this scenario, you have a running On-Demand Instance (T2) in your account, for which you're currently paying On-Demand rates. You purchase a Reserved Instance that matches the attributes of your running instance, and the billing benefit is immediately applied. Next, you purchase a Reserved Instance for a C4 instance. You do not have any running instances in your account that match the attributes of this Reserved Instance. In the final step, you launch an instance that matches the attributes of the C4 Reserved Instance, and the billing benefit is immediately applied.
### Key variables that determine Reserved Instance pricing The Reserved Instance pricing is determined by the following key variables.
#### Instance attributes A Reserved Instance has four instance attributes that determine its price.

- Instance type: For example, m4.large. This is composed of the instance family (for example, m4) and the instance size (for example, large).
- Region: The Region in which the Reserved Instance is purchased.
- Tenancy: Whether your instance runs on shared (default) or single-tenant (dedicated) hardware.
For more information, see Amazon EC2 Dedicated Instances.
- Platform: The operating system; for example, Windows or Linux/Unix. For more information, see Choosing a platform.
#### Term commitment You can purchase a Reserved Instance for a one-year or three-year commitment, with the three- year commitment offering a bigger discount.
- One-year: A year is defined as 31536000 seconds (365 days).
- Three-year: Three years is defined as 94608000 seconds (1095 days).
Reserved Instances do not renew automatically; when they expire, you can continue using the EC2 instance without interruption, but you are charged On-Demand rates. In the above example, when the Reserved Instances that cover the T2 and C4 instances expire, you go back to paying the On- Demand rates until you terminate the instances or purchase new Reserved Instances that match the instance attributes.
Important After you purchase a Reserved Instance, you cannot cancel your purchase. However, you might be able to modify, exchange, or sell your Reserved Instance if your needs change.
#### Payment options The following payment options are available for Reserved Instances:
- All Upfront: Full payment is made at the start of the term, with no other costs or additional hourly charges incurred for the remainder of the term, regardless of hours used.
- Partial Upfront: A portion of the cost must be paid upfront and the remaining hours in the term are billed at a discounted hourly rate, regardless of whether the Reserved Instance is being used.

- No Upfront: You are billed a discounted hourly rate for every hour within the term, regardless of whether the Reserved Instance is being used. No upfront payment is required.
Note No Upfront Reserved Instances are based on a contractual obligation to pay monthly for the entire term of the reservation. For this reason, a successful billing history is required before you can purchase No Upfront Reserved Instances.
Generally speaking, you can save more money making a higher upfront payment for Reserved Instances. You can also find Reserved Instances offered by third-party sellers at lower prices and shorter term lengths on the Reserved Instance Marketplace. For more information, see Sell Reserved Instances for Amazon EC2 in the Reserved Instance Marketplace.
#### Offering class If your computing needs change, you might be able to modify or exchange your Reserved Instance, depending on the offering class.
- Standard: These provide the most significant discount, but can only be modified. Standard Reserved Instances can't be exchanged.
- Convertible: These provide a lower discount than Standard Reserved Instances, but can be exchanged for another Convertible Reserved Instance with different instance attributes.
Convertible Reserved Instances can also be modified.
For more information, see Types of Reserved Instances (offering classes).
Important After you purchase a Reserved Instance, you cannot cancel your purchase. However, you might be able to modify, exchange, or sell your Reserved Instance if your needs change.
For more information, see the Amazon EC2 Reserved Instances Pricing page.

### Regional and zonal Reserved Instances (scope)
When you purchase a Reserved Instance, you determine the scope of the Reserved Instance. The scope is either regional or zonal.
- Regional: When you purchase a Reserved Instance for a Region, it's referred to as a regional Reserved Instance.
- Zonal: When you purchase a Reserved Instance for a specific Availability Zone, it's referred to as a zonal Reserved Instance.
The scope does not affect the price. You pay the same price for a regional or zonal Reserved Instance. For more information about Reserved Instance pricing, see Key variables that determine Reserved Instance pricing and Amazon EC2 Reserved Instances Pricing.
For more information about how to specify the scope of a Reserved Instance, see RI Attributes, specifically the Availability Zone bullet.
#### Differences between regional and zonal Reserved Instances The following table highlights some key differences between regional Reserved Instances and zonal Reserved Instances:

Regional Reserved Instances Zonal Reserved Instances Ability to reserve capacity A regional Reserved Instance does not  reserve capacity.
A zonal Reserved Instance reserves capacity in the specified Availability  Zone.
Availability Zone flexibility The Reserved Instance discount applies to instance usage in any  Availability Zone in the specified Region.
No Availability Zone flexibili ty—the Reserved Instance discount  applies to instance usage in the specified Availability Zone  only.
#### Instance size flexibility The Reserved Instance discount applies to instance No instance size flexibility —the Reserved Instance

Regional Reserved Instances Zonal Reserved Instances usage within the  instance family, regardless of size.
Only supported on Amazon Linux/Unix Reserved Instances with default  t enancy. For more informati on, see Instance size flexibility determined by normalization factor. discount applies  to instance usage for the specified instance type and size  only.
Queuing a purchase You can queue purchases for regional Reserved  Instances.
You can't queue purchases for zonal Reserved Instances.
For more information and examples, see How Reserved Instance discounts are applied.
### Types of Reserved Instances (offering classes)
The offering class of a Reserved Instance is either Standard or Convertible. A Standard Reserved Instance provides a more significant discount than a Convertible Reserved Instance, but you can't exchange a Standard Reserved Instance. You can exchange Convertible Reserved Instances. You can modify Standard and Convertible Reserved Instances.
The configuration of a Reserved Instance comprises a single instance type, platform, scope, and tenancy over a term. If your computing needs change, you might be able to modify or exchange your Reserved Instance.
#### Differences between Standard and Convertible Reserved Instances The following are the differences between Standard and Convertible Reserved Instances.

Standard Reserved Instance Convertible Reserved Instance
### Modify Reserved Instances Some attributes can be modified. For more informati Some attributes can be modified. For more informati

Standard Reserved Instance Convertible Reserved Instance on, see Modify Reserved Instances. on, see Modify Reserved Instances.
Exchange Reserved Instances Can't be exchanged.
Can be exchanged during the term for another Convertib le Reserved Instance with new  attributes, including instance family, instance type, platform, scope, or tenancy. For more informati on, see Exchange Convertible Reserved Instances.
Sell in the Reserved Instance Marketplace Can be sold in the Reserved Instance Marketplace.
Can't be sold in the Reserved Instance Marketplace.
Buy in the Reserved Instance Marketplace Can be bought in the Reserved Instance Marketpla ce.
Can't be bought in the Reserved Instance Marketpla ce.
### How Reserved Instance discounts are applied Reserved Instances are not physical instances, but rather a billing discount that is applied to the running On-Demand Instances in your account. The On-Demand Instances must match certain specifications of the Reserved Instances in order to benefit from the billing discount.
If you purchase a Reserved Instance and you already have a running On-Demand Instance that matches the specifications of the Reserved Instance, the billing discount is applied immediately and automatically. You do not have to restart your instances. If you do not have an eligible running On-Demand Instance, launch an On-Demand Instance with the same specifications as your Reserved Instance. For more information, see Use your Reserved Instances.
The offering class (Standard or Convertible) of the Reserved Instance does not affect how the billing discount is applied.
Topics

- How zonal Reserved Instances are applied
- How regional Reserved Instances are applied
- Instance size flexibility
- Examples of applying Reserved Instances
#### How zonal Reserved Instances are applied A Reserved Instance that is purchased to reserve capacity in a specific Availability Zone is called a zonal Reserved Instance.
- The Reserved Instance discount applies to matching instance usage in that Availability Zone.
- The attributes (tenancy, platform, Availability Zone, instance type, and instance size) of the running instances must match that of the Reserved Instances.
For example, if you purchase two c4.xlarge default tenancy Linux/Unix Standard Reserved Instances for Availability Zone us-east-1a, then up to two c4.xlarge default tenancy Linux/ Unix instances running in the Availability Zone us-east-1a can benefit from the Reserved Instance discount.
#### How regional Reserved Instances are applied A Reserved Instance that is purchased for a Region is called a regional Reserved Instance, and provides Availability Zone and instance size flexibility.
- The Reserved Instance discount applies to instance usage in any Availability Zone in that Region.
- The Reserved Instance discount applies to instance usage within the instance family, regardless of size—this is known as instance size flexibility.
Instance size flexibility With instance size flexibility, the Reserved Instance discount applies to instance usage for instances that have the same  family. The Reserved Instance is applied from the smallest to the largest instance size within the instance family based on the normalization factor. For an example of how the Reserved Instance discount is applied, see Scenario 2: Reserved Instances in a single account using the normalization factor.

##### Limitations
- Supported: Instance size flexibility is only supported for Regional Reserved Instances.
- Not supported: Instance size flexibility is not supported for the following Reserved Instances:
- Reserved Instances that are purchased for a specific Availability Zone (zonal Reserved Instances)
- Reserved Instances for G4ad, G4dn, G5, G5g, G6, G6e, G6f, Gr6, Gr6f, hpc7a, P5, Inf1, Inf2, u7i-6tb, and u7i-8tb instances
- Reserved Instances for Windows Server, Windows Server with SQL Standard, Windows Server with SQL Server Enterprise, Windows Server with SQL Server Web, RHEL, and SUSE Linux Enterprise Server
- Reserved Instances with dedicated tenancy
##### Instance size flexibility determined by normalization factor Instance size flexibility is determined by the normalization factor of the instance size. The discount applies either fully or partially to running instances of the same instance family, depending on the instance size of the reservation, in any Availability Zone in the Region. The only attributes that must be matched are the instance family, tenancy, and platform.
The following table lists the different sizes within an instance family, and the corresponding normalization factor. This scale is used to apply the discounted rate of Reserved Instances to the normalized usage of the instance family.
Instance size Normalization factor nano 0.25 micro 0.5 small 1 medium 2 large 4 xlarge 8

Instance size Normalization factor 2xlarge 16 3xlarge 24 4xlarge 32 6xlarge 48 8xlarge 64 9xlarge 72 10xlarge 80 12xlarge 96 16xlarge 128 18xlarge 144 24xlarge 192 32xlarge 256 48xlarge 384 56xlarge 448 112xlarge 896 For example, a t2.medium instance has a normalization factor of 2. If you purchase a t2.medium default tenancy Amazon Linux/Unix Reserved Instance in the US East (N. Virginia) and you have two running t2.small instances in your account in that Region, the billing benefit is applied in full to both instances.

Or, if you have one t2.large instance running in your account in the US East (N. Virginia) Region, the billing benefit is applied to 50% of the usage of the instance.
The normalization factor is also applied when modifying Reserved Instances. For more information, see Modify Reserved Instances.
###### Normalization factor for bare metal instances Instance size flexibility also applies to bare metal instances within the instance family. If you have regional Amazon Linux/Unix Reserved Instances with shared tenancy on bare metal instances, you can benefit from the Reserved Instance savings within the same instance family. The opposite is also true: if you have regional Amazon Linux/Unix Reserved Instances with shared tenancy on instances in the same family as a bare metal instance, you can benefit from the Reserved Instance savings on the bare metal instance.
The metal instance size does not have a single normalization factor. A bare metal instance has the same normalization factor as the equivalent virtualized instance size within the same instance family. For example, an i3.metal instance has the same normalization factor as an i3.16xlarge instance.

Instance size Normalization factor a1.metal 32 m5zn.metal  | x2iezn.metal   z1d.metal 96 c6g.metal  |   c6gd.metal  |   i3.metal |   m6g.metal  |   m6gd.metal
|   r6g.metal  |   r6gd.metal  |   x2gd.metal 128 c5n.metal 144 c5.metal |   c5d.metal  |   i3en.metal  |   m5.metal |   m5d.metal  | m5dn.metal  |   m5n.metal  |   r5.metal |   r5b.metal  |   r5d.metal  | r5dn.metal  |   r5n.metal 192 c6i.metal  | c6id.metal  | m6i.metal  | m6id.metal  | r6d.metal
| r6id.metal 256 u-18tb1.metal  | u-24tb1.metal 448 u-6tb1.metal  | u-9tb1.metal  | u-12tb1.metal 896 For example, an i3.metal instance has a normalization factor of 128. If you purchase an i3.metal default tenancy Amazon Linux/Unix Reserved Instance in the US East (N. Virginia), the billing benefit can apply as follows:
- If you have one running i3.16xlarge in your account in that Region, the billing benefit is applied in full to the i3.16xlarge instance (i3.16xlarge normalization factor = 128).
- Or, if you have two running i3.8xlarge instances in your account in that Region, the billing benefit is applied in full to both i3.8xlarge instances (i3.8xlarge normalization factor = 64).
- Or, if you have four running i3.4xlarge instances in your account in that Region, the billing benefit is applied in full to all four i3.4xlarge instances (i3.4xlarge normalization factor = 32).

The opposite is also true. For example, if you purchase two i3.8xlarge default tenancy Amazon Linux/Unix Reserved Instances in the US East (N. Virginia), and you have one running i3.metal instance in that Region, the billing benefit is applied in full to the i3.metal instance.
#### Examples of applying Reserved Instances The following scenarios cover the ways in which Reserved Instances are applied.
- Scenario 1: Reserved Instances in a single account
- Scenario 2: Reserved Instances in a single account using the normalization factor
- Scenario 3: Regional Reserved Instances in linked accounts
- Scenario 4: Zonal Reserved Instances in a linked account
##### Scenario 1: Reserved Instances in a single account You are running the following On-Demand Instances in account A:
- 4 x m3.large Linux, default tenancy instances in Availability Zone us-east-1a
- 2 x m4.xlarge Amazon Linux, default tenancy instances in Availability Zone us-east-1b
- 1 x c4.xlarge Amazon Linux, default tenancy instances in Availability Zone us-east-1c You purchase the following Reserved Instances in account A:
- 4 x m3.large Linux, default tenancy Reserved Instances in Availability Zone us-east-1a (capacity is reserved)
- 4 x m4.large Amazon Linux, default tenancy Reserved Instances in Region us-east-1
- 1 x c4.large Amazon Linux, default tenancy Reserved Instances in Region us-east-1 The Reserved Instance benefits are applied in the following way:
- The discount and capacity reservation of the four m3.large zonal Reserved Instances is used by the four m3.large instances because the attributes (instance size, Region, platform, tenancy) between them match.
- The m4.large regional Reserved Instances provide Availability Zone and instance size flexibility, because they are regional Amazon Linux Reserved Instances with default tenancy.
An m4.large is equivalent to 4 normalized units/hour.

You've purchased four m4.large regional Reserved Instances, and in total, they are equal to 16 normalized units/hour (4x4). Account A has two m4.xlarge instances running, which is equivalent to 16 normalized units/hour (2x8). In this case, the four m4.large regional Reserved Instances provide the full billing benefit to the usage of the two m4.xlarge instances.
- The c4.large regional Reserved Instance in us-east-1 provides Availability Zone and instance size flexibility, because it is a regional Amazon Linux Reserved Instance with default tenancy, and applies to the c4.xlarge instance. A c4.large instance is equivalent to 4 normalized units/ hour and a c4.xlarge is equivalent to 8 normalized units/hour.
In this case, the c4.large regional Reserved Instance provides partial benefit to c4.xlarge usage. This is because the c4.large Reserved Instance is equivalent to 4 normalized units/ hour of usage, but the c4.xlarge instance requires 8 normalized units/hour. Therefore, the c4.large Reserved Instance billing discount applies to 50% of c4.xlarge usage. The remaining c4.xlarge usage is charged at the On-Demand rate.
##### Scenario 2: Reserved Instances in a single account using the normalization factor You are running the following On-Demand Instances in account A:
- 2 x m3.xlarge Amazon Linux, default tenancy instances in Availability Zone us-east-1a
- 2 x m3.large Amazon Linux, default tenancy instances in Availability Zone us-east-1b You purchase the following Reserved Instance in account A:
- 1 x m3.2xlarge Amazon Linux, default tenancy Reserved Instance in Region us-east-1 The Reserved Instance benefits are applied in the following way:
- The m3.2xlarge regional Reserved Instance in us-east-1 provides Availability Zone and instance size flexibility, because it is a regional Amazon Linux Reserved Instance with default tenancy.
It applies first to the m3.large instances and then to the m3.xlarge instances, because it applies from the smallest to the largest instance size within the instance family based on the normalization factor.
An m3.large instance is equivalent to 4 normalized units/hour.
An m3.xlarge instance is equivalent to 8 normalized units/hour.

An m3.2xlarge instance is equivalent to 16 normalized units/hour.
The benefit is applied as follows:
The m3.2xlarge regional Reserved Instance provides full benefit to 2 x m3.large usage, because together these instances account for 8 normalized units/hour. This leaves 8 normalized units/hour to apply to the m3.xlarge instances.
With the remaining 8 normalized units/hour, the m3.2xlarge regional Reserved Instance provides full benefit to 1 x m3.xlarge usage, because each m3.xlarge instance is equivalent to 8 normalized units/hour. The remaining m3.xlarge usage is charged at the On-Demand rate.
##### Scenario 3: Regional Reserved Instances in linked accounts Reserved Instances are first applied to usage within the purchasing account, followed by qualifying usage in any other account in the organization. For more information, see Reserved Instances and consolidated billing. For regional Reserved Instances that offer instance size flexibility, the benefit is applied from the smallest to the largest instance size within the instance family.
You're running the following On-Demand Instances in account A (the purchasing account):
- 2 x m4.xlarge Linux, default tenancy instances in Availability Zone us-east-1a
- 1 x m4.2xlarge Linux, default tenancy instances in Availability Zone us-east-1b
- 2 x c4.xlarge Linux, default tenancy instances in Availability Zone us-east-1a
- 1 x c4.2xlarge Linux, default tenancy instances in Availability Zone us-east-1b Another customer is running the following On-Demand Instances in account B—a linked account:
- 2 x m4.xlarge Linux, default tenancy instances in Availability Zone us-east-1a You purchase the following regional Reserved Instances in account A:
- 4 x m4.xlarge Linux, default tenancy Reserved Instances in Region us-east-1
- 2 x c4.xlarge Linux, default tenancy Reserved Instances in Region us-east-1 The regional Reserved Instance benefits are applied in the following way:

- The discount of the four m4.xlarge Reserved Instances is used by the two m4.xlarge instances and the single m4.2xlarge instance in account A (purchasing account). All three instances match the attributes (instance family, Region, platform, tenancy). The discount is applied to instances in the purchasing account (account A) first, even though account B (linked account) has two m4.xlarge that also match the Reserved Instances. There is no capacity reservation because the Reserved Instances are regional Reserved Instances.
- The discount of the two c4.xlarge Reserved Instances applies to the two c4.xlarge instances, because they are a smaller instance size than the c4.2xlarge instance. There is no capacity reservation because the Reserved Instances are regional Reserved Instances.
##### Scenario 4: Zonal Reserved Instances in a linked account In general, Reserved Instances that are owned by an account are applied first to usage in that account. However, if there are qualifying, unused Reserved Instances for a specific Availability Zone (zonal Reserved Instances) in other accounts in the organization, they are applied to the account before regional Reserved Instances owned by the account. This is done to ensure maximum Reserved Instance utilization and a lower bill. For billing purposes, all the accounts in the organization are treated as one account. The following example might help explain this.
You're running the following On-Demand Instance in account A (the purchasing account):
- 1 x m4.xlarge Linux, default tenancy instance in Availability Zone us-east-1a A customer is running the following On-Demand Instance in linked account B:
- 1 x m4.xlarge Linux, default tenancy instance in Availability Zone us-east-1b You purchase the following regional Reserved Instances in account A:
- 1 x m4.xlarge Linux, default tenancy Reserved Instance in Region us-east-1 A customer also purchases the following zonal Reserved Instances in linked account C:
- 1 x m4.xlarge Linux, default tenancy Reserved Instances in Availability Zone us-east-1a The Reserved Instance benefits are applied in the following way:

- The discount of the m4.xlarge zonal Reserved Instance owned by account C is applied to the m4.xlarge usage in account A.
- The discount of the m4.xlarge regional Reserved Instance owned by account A is applied to the m4.xlarge usage in account B.
- If the regional Reserved Instance owned by account A was first applied to the usage in account A, the zonal Reserved Instance owned by account C remains unused and usage in account B is charged at On-Demand rates.
For more information, see Understanding your reservations in the AWS Cost and Usage Report.
Note Zonal Reserved Instances reserve capacity only for the owning account and cannot be shared with other AWS accounts. If you need to share capacity with other AWS accounts, use Reserve compute capacity with EC2 On-Demand Capacity Reservations.
### Use your Reserved Instances Reserved Instances are automatically applied to running On-Demand Instances provided that the specifications match. If you have no running On-Demand Instances that match the specifications of your Reserved Instance, the Reserved Instance is unused until you launch an instance with the required specifications.
If you're launching an On-Demand Instance to take advantage of the billing benefit of a Reserved Instance, ensure that you specify the following information when you configure your On-Demand Instance:
Platform You must specify an Amazon Machine Image (AMI) that matches the platform (product description) of your Reserved Instance. For example, if you specified Linux/UNIX for your Reserved Instance, you can launch an instance from an Amazon Linux AMI or an Ubuntu AMI.
Instance type If you purchased a zonal Reserved Instance, you must specify the same instance type as your Reserved Instance; for example, t3.large. For more information, see How zonal Reserved Instances are applied.

If you purchased a regional Reserved Instance, you must specify an instance type from the same instance family as the instance type of your Reserved Instance. For example, if you specified t3.xlarge for your Reserved Instance, you must launch your instance from the T3 family, but you can specify any size, for example, t3.medium. For more information, see How regional Reserved Instances are applied.
Availability Zone If you purchased a zonal Reserved Instance for a specific Availability Zone, you must launch the instance into the same Availability Zone.
If you purchased a regional Reserved Instance, you can launch the instance into any Availability Zone in the Region that you specified for the Reserved Instance.
Tenancy The tenancy (dedicated or shared) of the instance must match the tenancy of your Reserved Instance. For more information, see Amazon EC2 Dedicated Instances.
For examples of how Reserved Instances are applied to your running On-Demand Instances, see How Reserved Instance discounts are applied. For more information, see Why aren't my Amazon EC2 Reserved Instances applying to my AWS billing in the way that I expected?
You can use various methods to launch the On-Demand Instances that use your Reserved Instance discount. For information about the different launch methods, see Launch an Amazon EC2 instance. You can also use Amazon EC2 Auto Scaling to launch an instance. For more information, see the Amazon EC2 Auto Scaling User Guide.
### How billing works with Reserved Instances All Reserved Instances provide you with a discount compared to On-Demand pricing. With Reserved Instances, you pay for the entire term regardless of actual use. You can choose to pay for your Reserved Instance upfront, partially upfront, or monthly, depending on the payment option specified for the Reserved Instance.
When Reserved Instances expire, you are charged On-Demand rates for EC2 instance usage. You can queue a Reserved Instance for purchase up to three years in advance. This can help you ensure that you have uninterrupted coverage. For more information, see Queue your purchase.

The AWS Free Tier is available for new AWS accounts. If you are using the AWS Free Tier to run Amazon EC2 instances, and you purchase a Reserved Instance, you are charged the standard pricing. For information, see AWS Free Tier.
Contents
- Usage billing
- Viewing your bill
- Reserved Instances and consolidated billing
- Reserved Instance discount pricing tiers
#### Usage billing Reserved Instances are billed for every clock-hour during the term that you select, regardless of whether an instance is running. Each clock-hour starts on the hour (zero minutes and zero seconds past the hour) of a standard 24-hour clock. For example, 1:00:00 to 1:59:59 is one clock-hour. For more information about instance states, see Amazon EC2 instance state changes.
A Reserved Instance billing benefit can be applied to a running instance on a per-second basis. Per- second billing is available for instances using an open-source Linux distribution, such as Amazon Linux and Ubuntu. Per-hour billing is used for commercial Linux distributions, such as Red Hat Enterprise Linux and SUSE Linux Enterprise Server.
A Reserved Instance billing benefit can apply to a maximum of 3600 seconds (one hour) of instance usage per clock-hour. You can run multiple instances concurrently, but can only receive the benefit of the Reserved Instance discount for a total of 3600 seconds per clock-hour; instance usage that exceeds 3600 seconds in a clock-hour is billed at the On-Demand rate.
For example, if you purchase one m4.xlarge Reserved Instance and run four m4.xlarge instances concurrently for one hour, one instance is charged at one hour of Reserved Instance usage and the other three instances are charged at three hours of On-Demand usage.
However, if you purchase one m4.xlarge Reserved Instance and run four m4.xlarge instances for 15 minutes (900 seconds) each within the same hour, the total running time for the instances is one hour, which results in one hour of Reserved Instance usage and 0 hours of On-Demand usage.

If multiple eligible instances are running concurrently, the Reserved Instance billing benefit is applied to all the instances at the same time up to a maximum of 3600 seconds in a clock-hour; thereafter, On-Demand rates apply.
Cost Explorer on the Billing and Cost Management console enables you to analyze the savings against running On-Demand Instances. The Reserved Instances FAQ includes an example of a list value calculation.
If you close your AWS account, On-Demand billing for your resources stops. However, if you have any Reserved Instances in your account, you continue to receive a bill for these until they expire.
#### Viewing your bill You can find out about the charges and fees to your account by viewing the AWS Billing and Cost Management console.
- The Dashboard displays a spend summary for your account.
- On the Bills page, under Details expand the Elastic Compute Cloud section and the Region to get billing information about your Reserved Instances.
You can view the charges online, or you can download a CSV file.

You can also track your Reserved Instance utilization using the AWS Cost and Usage Report. For more information, see Understanding your reservations.
#### Reserved Instances and consolidated billing The pricing benefits of Reserved Instances are shared when the purchasing account is part of a set of accounts billed under one consolidated billing payer account. The instance usage across all member accounts is aggregated in the payer account every month. This is typically useful for companies in which there are different functional teams or groups; then, the normal Reserved Instance logic is applied to calculate the bill. For more information, see Consolidated billing for AWS Organizations.
If you close the account that purchased the Reserved Instance, the payer account is charged for the Reserved Instance until the Reserved Instance expires. After the closed account is permanently deleted in 90 days, the member accounts no longer benefit from the Reserved Instance billing discount.
Note Zonal Reserved Instances reserve capacity only for the owning account and cannot be shared with other AWS accounts. If you need to share capacity with other AWS accounts, use Reserve compute capacity with EC2 On-Demand Capacity Reservations.
#### Reserved Instance discount pricing tiers If your account qualifies for a discount pricing tier, it automatically receives discounts on upfront and instance usage fees for Reserved Instance purchases that you make within that tier level from that point on. To qualify for a discount, the list value of your Reserved Instances in the Region must be $500,000 USD or more.
The following rules apply:
- Pricing tiers and related discounts apply only to purchases of Amazon EC2 Standard Reserved Instances.
- Pricing tiers do not apply to Reserved Instances for Windows with SQL Server Standard, SQL Server Web, and SQL Server Enterprise.
- Pricing tiers do not apply to Reserved Instances for Linux with SQL Server of any kind.

- Pricing tier discounts only apply to purchases made from AWS. They do not apply to purchases of third-party Reserved Instances.
- Discount pricing tiers are currently not applicable to Convertible Reserved Instance purchases.
Topics
- Calculate Reserved Instance pricing discounts
- Buy with a discount tier
- Crossing pricing tiers
- Consolidated billing for pricing tiers
##### Calculate Reserved Instance pricing discounts You can determine the pricing tier for your account by calculating the list value for all of your Reserved Instances in a Region. Multiply the hourly recurring price for each reservation by the total number of hours for the term and add the undiscounted upfront price (also known as the fixed price) at the time of purchase. Because the list value is based on undiscounted (public) pricing, it is not affected if you qualify for a volume discount or if the price drops after you buy your Reserved Instances.
List value = fixed price + (undiscounted recurring hourly price * hours in term)
For example, for a 1-year Partial Upfront t2.small Reserved Instance, assume the upfront price is $60.00 and the hourly rate is $0.007. This provides a list value of $121.32.
121.32 = 60.00 + (0.007 * 8760)
To view the fixed price values for Reserved Instances using the Amazon EC2 console
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Reserved Instances.
3. To display the Upfront price column, choose settings ( ) in the top-right corner, turn on Upfront price, and choose Confirm.
To view the fixed price values for Reserved Instances using the command line

- describe-reserved-instances (AWS CLI)
- Get-EC2ReservedInstance (AWS Tools for Windows PowerShell)
##### Buy with a discount tier When you buy Reserved Instances, Amazon EC2 automatically applies any discounts to the part of your purchase that falls within a discount pricing tier. You don't need to do anything differently, and you can buy Reserved Instances using any of the Amazon EC2 tools. For more information, see Buy Reserved Instances for Amazon EC2.
After the list value of your active Reserved Instances in a Region crosses into a discount pricing tier, any future purchase of Reserved Instances in that Region are charged at a discounted rate.
If a single purchase of Reserved Instances in a Region takes you over the threshold of a discount tier, then the portion of the purchase that is above the price threshold is charged at the discounted rate. For more information about the temporary Reserved Instance IDs that are created during the purchase process, see Crossing pricing tiers.
If your list value falls below the price point for that discount pricing tier—for example, if some of your Reserved Instances expire—future purchases of Reserved Instances in the Region are not discounted. However, you continue to get the discount applied against any Reserved Instances that were originally purchased within the discount pricing tier.
When you buy Reserved Instances, one of four possible scenarios occurs:
- No discount—Your purchase within a Region is still below the discount threshold.
- Partial discount—Your purchase within a Region crosses the threshold of the first discount tier.
No discount is applied to one or more reservations and the discounted rate is applied to the remaining reservations.
- Full discount—Your entire purchase within a Region falls within one discount tier and is discounted appropriately.
- Two discount rates—Your purchase within a Region crosses from a lower discount tier to a higher discount tier. You are charged two different rates: one or more reservations at the lower discounted rate, and the remaining reservations at the higher discounted rate.

##### Crossing pricing tiers If your purchase crosses into a discounted pricing tier, you see multiple entries for that purchase: one for that part of the purchase charged at the regular price, and another for that part of the purchase charged at the applicable discounted rate.
The Reserved Instance service generates several Reserved Instance IDs because your purchase crossed from an undiscounted tier, or from one discounted tier to another. There is an ID for each set of reservations in a tier. Consequently, the ID returned by your purchase CLI command or API action is different from the actual ID of the new Reserved Instances.
##### Consolidated billing for pricing tiers A consolidated billing account aggregates the list value of member accounts within a Region.
When the list value of all active Reserved Instances for the consolidated billing account reaches a discount pricing tier, any Reserved Instances purchased after this point by any member of the consolidated billing account are charged at the discounted rate (as long as the list value for that consolidated account stays above the discount pricing tier threshold). For more information, see Reserved Instances and consolidated billing.
### Buy Reserved Instances for Amazon EC2 To buy a Reserved Instance for Amazon EC2, you can use the Amazon EC2 console, a command line tool, or an SDK to search for Reserved Instance offerings from AWS and third-party sellers, adjusting your search parameters until you find the exact match that you're looking for.
When you search for Reserved Instances to buy, you receive a quote on the cost of the returned offerings. When you proceed with the purchase, AWS automatically places a limit price on the purchase price. The total cost of your Reserved Instances won't exceed the amount that you were quoted.
If the price rises or changes for any reason, the purchase is not completed. When you are purchasing a third-party seller's Reserved Instance from the Amazon EC2 Reserved Instance Marketplace, if there are offerings similar to your choice but at a lower upfront price, AWS sells you the offerings at the lower upfront price.
Before you confirm your purchase, review the details of the Reserved Instance that you plan to buy, and make sure that all the parameters are accurate. After you purchase a Reserved Instance (either from a third-party seller in the Reserved Instance Marketplace or from AWS), you cannot cancel your purchase. You can queue a purchase for a future date, and cancel the queued purchase before its scheduled time.

To purchase and modify Reserved Instances, ensure that your user has the appropriate permissions, such as the ability to describe Availability Zones. For information, see the section called "Work with Reserved Instances" (API) or the section called "Work with Reserved Instances" (console).
Tasks
- Choosing a platform
- Queue your purchase
- Buy Standard Reserved Instances
- Buy Convertible Reserved Instances
- Buy from the Reserved Instance Marketplace
- Cancel a queued purchase
- Renew a Reserved Instance
#### Choosing a platform Amazon EC2 supports the following platforms for Reserved Instances:
- Linux/UNIX
- Linux with SQL Server Standard
- Linux with SQL Server Web
- Linux with SQL Server Enterprise
- SUSE Linux
- Red Hat Enterprise Linux
- Red Hat Enterprise Linux with HA
- Windows
- Windows with SQL Server Standard
- Windows with SQL Server Web
- Windows with SQL Server Enterprise
#### Considerations
- If you bring your existing subscription (BYOS) for Red Hat Enterprise Linux, SUSE Linux, or Ubuntu Pro, you must choose an offering for the Linux/Unix platform.

- Reserved Instances are not supported on instances running macOS or Ubuntu Pro (EC2 subscription-included, i.e., not BYOS). For saving with On-Demand instance pricing, we recommend that you use macOS and Ubuntu Pro (EC2 subscription-included) instances with Savings Plans. For more information, see Savings Plans User Guide.
To ensure that an instance runs in a specific Reserved Instance, the platform of the Reserved Instance must match the platform of the AMI used to launch the instance. For Linux AMIs, it is important to check whether the AMI platform uses the general value Linux/UNIX or a more specific value like SUSE Linux.
Console To check the AMI platform
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose AMIs.
3. Select the AMI.
4. On the Details tab, note the value of Platform details.
AWS CLI To check the AMI platform Use the describe-images command and check the value of PlatformDetails. aws ec2 describe-images \ --image-id ami-0abcdef1234567890 \ --query Images[*].PlatformDetails The following is example output.
[ "Linux/UNIX"
]
PowerShell To check the AMI platform

Use the Get-EC2Image cmdlet and check the value of PlatformDetails.
Get-EC2Image `
    -ImageId ami-0abcdef1234567890 | `
    Select PlatformDetails The following is example output.
PlatformDetails
--------------- Linux/UNIX
#### Queue your purchase By default, when you purchase a Reserved Instance, the purchase is made immediately.
Alternatively, you can queue your purchases for a future date and time. For example, you can queue a purchase for around the time that an existing Reserved Instance expires. This can help you ensure that you have uninterrupted coverage.
You can queue purchases for regional Reserved Instances, but not zonal Reserved Instances or Reserved Instances from other sellers. You can queue a purchase up to three years in advance. On the scheduled date and time, the purchase is made using the default payment method. After the payment is successful, the billing benefit is applied.
You can set a date for your queued purchases in the Amazon EC2 console, and the purchase is queued until 00:00 UTC on this date. To specify a different time for the queued purchase, use an AWS SDK or command line tool.
You can view your queued purchases in the Amazon EC2 console. The status of a queued purchase is queued. You can cancel a queued purchase any time before its scheduled time. For details, see Cancel a queued purchase.
#### Buy Standard Reserved Instances You can buy Standard Reserved Instances in a specific Availability Zone and get a capacity reservation. Alternatively, you can forego the capacity reservation and purchase a regional Standard Reserved Instance.
After the purchase is complete, if you already have a running instance that matches the specifications of the Reserved Instance, the billing benefit is immediately applied. You do not need

to restart your instances. If you do not have a suitable running instance, launch an instance and ensure that you match the exact criteria that you specified for your Reserved Instance. For more information, see Use your Reserved Instances.
For examples of how Reserved Instances are applied to your running instances, see How Reserved Instance discounts are applied.
Console To buy Standard Reserved Instances
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Reserved Instances, and then choose Purchase Reserved Instances.
3. For Offering class, choose Standard to display Standard Reserved Instances.
4. To purchase a capacity reservation, toggle on Only show offerings that reserve capacity in the top-right corner of the purchase screen. When you toggle on this setting, the Availability Zone field appears.
To purchase a regional Reserved Instance, toggle off this setting. When you toggle off this setting, the Availability Zone field disappears.
5. Select other configurations as needed, and then choose Search.
6. For each Reserved Instance that you want to purchase, enter the desired quantity, and choose Add to cart.
To purchase a Standard Reserved Instance from the Reserved Instance Marketplace, look for 3rd party in the Seller column in the search results. The Term column displays non- standard terms. For more information, see Buy from the Reserved Instance Marketplace.
7. To see a summary of the Reserved Instances that you selected, choose View cart.
8. If Order on is Now, the purchase is completed immediately after you choose Order all. To queue a purchase, choose Now and select a date. You can select a different date for each eligible offering in the cart. The purchase is queued until 00:00 UTC on the selected date.
9. To complete the order, choose Order all.
If, at the time of placing the order, there are offerings similar to your choice but with a lower price, AWS sells you the offerings at the lower price.
10. Choose Close.

The status of your order is listed in the State column. When your order is complete, the State value changes from Payment-pending to Active. When the Reserved Instance is Active, it is ready to use.
If the status goes to Retired, AWS might not have received your payment.
AWS CLI To buy a Standard Reserved Instance
1. Find available Reserved Instances using the describe-reserved-instances-offerings command. Specify standard for the --offering-class option to return only Standard Reserved Instances. You can apply additional criteria to narrow your results. For example, use the following command to purchase a regional t2.large Reserved Instance with a default tenancy for Linux/UNIX for a 1-year term only. aws ec2 describe-reserved-instances-offerings \ --instance-type t2.large \ --offering-class standard \ --product-description "Linux/UNIX" \ --instance-tenancy default \ --filters Name=duration,Values=31536000 \ Name=scope,Values=Region To find Reserved Instances on the Reserved Instance Marketplace only, use the marketplace filter and do not specify a duration in the request, as the term might be shorter than a 1– or 3-year term. aws ec2 describe-reserved-instances-offerings \ --instance-type t2.large \ --offering-class standard \ --product-description "Linux/UNIX" \ --instance-tenancy default \ --filters Name=marketplace,Values=true When you find a Reserved Instance that meets your needs, take note of the offering ID. For example:

"ReservedInstancesOfferingId": "bec624df-a8cc-4aad-a72f-4f8abc34caf2"
2. Use the purchase-reserved-instances-offering command to buy your Reserved Instance.
You must specify the Reserved Instance offering ID you obtained the previous step and you must specify the number of instances for the reservation. aws ec2 purchase-reserved-instances-offering \ --reserved-instances-offering-id bec624df-a8cc-4aad-a72f-4f8abc34caf2 \ --instance-count 1 By default, the purchase is completed immediately. Alternatively, to queue the purchase, add the following option to the previous call.
--purchase-time "2020-12-01T00:00:00Z"
3. Use the describe-reserved-instances command to get the status of your Reserved Instance. aws ec2 describe-reserved-instances \ --reserved-instances-ids b847fa93-e282-4f55-b59a-1342fec06327 \ --query ReservedInstances[].State PowerShell To buy a Standard Reserved Instance
1. Find available Reserved Instances using the Get-EC2ReservedInstancesOffering cmdlet.
Specify standard for the -OfferingClass parameter to return only Standard Reserved Instances. You can apply additional criteria to narrow your results. For example, use the following command to purchase a regional t2.large Reserved Instance with a default tenancy for Linux/UNIX for a 1-year term only.
Get-EC2ReservedInstancesOffering `
    -InstanceType "t2.large" `
    -OfferingClass "standard" `
    -ProductDescription "Linux/UNIX" `
    -InstanceTenancy "default" `
    -Filters @{Name="duration"; Values="31536000"} `
             @{Name="scope"; Values="Region"

To find Reserved Instances on the Reserved Instance Marketplace only, use the marketplace filter and do not specify a duration in the request, as the term might be shorter than a 1– or 3-year term.
Get-EC2ReservedInstancesOffering `
    -InstanceType t2.large `
    -OfferingClass "standard" `
    -ProductDescription "Linux/UNIX" `
    -InstanceTenancy default `
    -Filters @{Name="marketplace"; Values="true"} When you find a Reserved Instance that meets your needs, take note of the offering ID. For example: bec624df-a8cc-4aad-a72f-4f8abc34caf2
2. Use the New-EC2ReservedInstance cmdlet to buy your Reserved Instance. You must specify the Reserved Instance offering ID you obtained the previous step and you must specify the number of instances for the reservation.
New-EC2ReservedInstance `
    -ReservedInstancesOfferingId "bec624df-a8cc-4aad-a72f-4f8abc34caf2" `
    -InstanceCount 1 By default, the purchase is completed immediately. Alternatively, to queue the purchase, add the following parameter to the previous call.
-PurchaseTime "2020-12-01T00:00:00Z"
3. Use the Get-EC2ReservedInstance cmdlet to get the status of your Reserved Instance.
Get-EC2ReservedInstance `
    -ReservedInstancesId b847fa93-e282-4f55-b59a-1342fec06327 | `
    Select State

#### Buy Convertible Reserved Instances You can buy Convertible Reserved Instances in a specific Availability Zone and get a capacity reservation. Alternatively, you can forego the capacity reservation and purchase a regional Convertible Reserved Instance.
If you already have a running instance that matches the specifications of the Reserved Instance, the billing benefit is immediately applied. You do not have to restart your instances. If you do not have a suitable running instance, launch an instance and ensure that you match the same criteria that you specified for your Reserved Instance. For more information, see Use your Reserved Instances.
For examples of how Reserved Instances are applied to your running instances, see How Reserved Instance discounts are applied.
Console To buy Convertible Reserved Instances
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Reserved Instances, and then choose Purchase Reserved Instances.
3. For Offering class, choose Convertible to display Convertible Reserved Instances.
4. To purchase a capacity reservation, toggle on Only show offerings that reserve capacity in the top-right corner of the purchase screen. When you toggle on this setting, the Availability Zone field appears.
To purchase a regional Reserved Instance, toggle off this setting. When you toggle off this setting, the Availability Zone field disappears.
5. Select other configurations as needed and choose Search.
6. For each Convertible Reserved Instance that you want to purchase, enter the quantity, and choose Add to cart.
7. To see a summary of your selection, choose View cart.
8. If Order on is Now, the purchase is completed immediately after you choose Order all. To queue a purchase, choose Now and select a date. You can select a different date for each eligible offering in the cart. The purchase is queued until 00:00 UTC on the selected date.
9. To complete the order, choose Order all.

If, at the time of placing the order, there are offerings similar to your choice but with a lower price, AWS sells you the offerings at the lower price.
10. Choose Close.
The status of your order is listed in the State column. When your order is complete, the State value changes from Payment-pending to Active. When the Reserved Instance is Active, it is ready to use.
If the status goes to Retired, AWS might not have received your payment.
AWS CLI To buy a Convertible Reserved Instance
1. Find available Reserved Instances using the describe-reserved-instances-offerings command. Specify convertible for the --offering-class option to return only Convertible Reserved Instances. You can apply additional criteria to narrow your results. For example, use the following command to purchase a regional t2.large Reserved Instance with a default tenancy for Linux/UNIX. aws ec2 describe-reserved-instances-offerings \ --instance-type t2.large \ --offering-class convertible \ --product-description "Linux/UNIX" \ --instance-tenancy default \ --filters Name=scope,Values=Region When you find a Reserved Instance that meets your needs, take note of the offering ID. For example:
"ReservedInstancesOfferingId": "bec624df-a8cc-4aad-a72f-4f8abc34caf2"
2. Use the purchase-reserved-instances-offering command to buy your Reserved Instance.
You must specify the Reserved Instance offering ID you obtained the previous step and you must specify the number of instances for the reservation. aws ec2 purchase-reserved-instances-offering \ --reserved-instances-offering-id bec624df-a8cc-4aad-a72f-4f8abc34caf2 \

    --instance-count 1 By default, the purchase is completed immediately. Alternatively, to queue the purchase, add the following option to the previous call.
--purchase-time "2020-12-01T00:00:00Z"
3. Use the describe-reserved-instances command to get the status of your Reserved Instance. aws ec2 describe-reserved-instances \ --reserved-instances-ids b847fa93-e282-4f55-b59a-1342fec06327 \ --query ReservedInstances[].State PowerShell To buy a Convertible Reserved Instance
1. Find available Reserved Instances using the Get-EC2ReservedInstancesOffering cmdlet.
Specify convertible for the -OfferingClass parameter to return only Convertible Reserved Instances. You can apply additional criteria to narrow your results. For example, use the following command to purchase a regional t2.large Reserved Instance with a default tenancy for Linux/UNIX.
Get-EC2ReservedInstancesOffering `
    -InstanceType "t2.large" `
    -OfferingClass "convertible" `
    -ProductDescription "Linux/UNIX" `
    -InstanceTenancy "default" `
    -Filters @{Name="scope"; Values="Region"
When you find a Reserved Instance that meets your needs, take note of the offering ID. For example: bec624df-a8cc-4aad-a72f-4f8abc34caf2
2. Use the New-EC2ReservedInstance cmdlet to buy your Reserved Instance. You must specify the Reserved Instance offering ID that you obtained the previous step and you must specify the number of instances for the reservation.

New-EC2ReservedInstance `
    -ReservedInstancesOfferingId "bec624df-a8cc-4aad-a72f-4f8abc34caf2" `
    -InstanceCount 1 By default, the purchase is completed immediately. Alternatively, to queue the purchase, add the following parameter to the previous call.
-PurchaseTime "2020-12-01T00:00:00Z"
3. Use the Get-EC2ReservedInstance cmdlet to get the status of your Reserved Instance.
Get-EC2ReservedInstance `
    -ReservedInstancesId b847fa93-e282-4f55-b59a-1342fec06327 | `
    Select State
#### Buy from the Reserved Instance Marketplace You can purchase Reserved Instances from third-party sellers who own Reserved Instances that they no longer need from the Reserved Instance Marketplace. You can do this using the Amazon EC2 console or a command line tool. The process is similar to purchasing Reserved Instances from AWS. For more information, see Buy Standard Reserved Instances.
There are a few differences between Reserved Instances purchased in the Reserved Instance Marketplace and Reserved Instances purchased directly from AWS:
- Term – Reserved Instances that you purchase from third-party sellers have less than a full standard term remaining. Full standard terms from AWS run for one year or three years.
- Upfront price – Third-party Reserved Instances can be sold at different upfront prices. The usage or recurring fees remain the same as the fees set when the Reserved Instances were originally purchased from AWS.
- Types of Reserved Instances – Only Amazon EC2 Standard Reserved Instances can be purchased from the Reserved Instance Marketplace. Convertible Reserved Instances, Amazon RDS, and Amazon ElastiCache Reserved Instances are not available for purchase on the Reserved Instance Marketplace.
Basic information about you is shared with the seller, for example, your ZIP code and country information.

This information enables sellers to calculate any necessary transaction taxes that they have to remit to the government (such as sales tax or value-added tax) and is provided as a disbursement report. In rare circumstances, AWS might have to provide the seller with your email address, so that they can contact you regarding questions related to the sale (for example, tax questions).
For similar reasons, AWS shares the legal entity name of the seller on the buyer's purchase invoice.
If you need additional information about the seller for tax or related reasons, contact Support.
#### Cancel a queued purchase You can queue a purchase up to three years in advance. You can cancel a queued purchase any time before its scheduled time.
Console To cancel a queued purchase
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Reserved Instances.
3. Select one or more Reserved Instances.
4. Choose Actions, Delete queued Reserved Instances.
5. When prompted for confirmation, choose Delete, and then Close.
AWS CLI To cancel a queued purchase Use the delete-queued-reserved-instances command. aws ec2 delete-queued-reserved-instances \ --reserved-instances-ids b847fa93-e282-4f55-b59a-1342fec06327 PowerShell To cancel a queued purchase Use the Remove-EC2QueuedReservedInstance cmdlet.
Remove-EC2QueuedReservedInstance `
    -ReservedInstancesId b847fa93-e282-4f55-b59a-1342fec06327

#### Renew a Reserved Instance You can renew a Reserved Instance before it is scheduled to expire. Renewing a Reserved Instance queues the purchase of a Reserved Instance with the same configuration until the current Reserved Instance expires.
You must renew a Reserved Instance using the Amazon EC2 console.
To renew a Reserved Instance using a queued purchase
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Reserved Instances.
3. Select the Reserved Instance to renew.
4. Choose Actions, Renew Reserved Instances.
5. To complete the order, choose Order all, and then Close.
### Sell Reserved Instances for Amazon EC2 in the Reserved Instance Marketplace The Amazon EC2 Reserved Instance Marketplace is a platform that facilitates the sale of unused Standard Reserved Instances from AWS customers and third-party sellers. These Reserved Instances can vary in term lengths and pricing options. You might want to sell your Reserved Instances when you no longer need them, such as when you move your instances to a new AWS Region, change to a different instance type, finish projects before the Reserved Instance term expires, your business needs change, or you have excess capacity.
As soon as you list your Reserved Instances in the Reserved Instance Marketplace, they are available for potential buyers to find. All Reserved Instances are grouped according to the duration of the term remaining and the hourly price.
To fulfill a buyer's request to purchase a third-party seller's Reserved Instance via the Reserved Instance Marketplace, AWS first sells the Reserved Instance with the lowest upfront price in the specified grouping. Then, AWS sells the Reserved Instance with the next lowest price, until the buyer's entire order is fulfilled. AWS then processes the transactions and transfers ownership of the Reserved Instances to the buyer.
You own your Reserved Instance until it's sold. After the sale, you've given up the capacity reservation and the discounted recurring fees. If you continue to use your instance, AWS charges you the On-Demand price starting from the time that your Reserved Instance was sold.

If you want to sell your unused Reserved Instances on the Reserved Instance Marketplace, you must meet certain eligibility criteria.
For information about buying Reserved Instances on the Reserved Instance Marketplace, see Buy from the Reserved Instance Marketplace.
Contents
- Restrictions and limitations
- Register as a seller
- Bank account for disbursement
- Tax information
- Price your Reserved Instances
- List your Reserved Instances
- Reserved Instance listing states
- Lifecycle of a listing
- After your Reserved Instance is sold
- Getting paid
- Information shared with the buyer
#### Restrictions and limitations Before you can sell your unused reservations, you must register as a seller in the Reserved Instance Marketplace. For information, see Register as a seller.
The following limitations and restrictions apply when selling Reserved Instances:
- Only Amazon EC2 Standard regional and zonal Reserved Instances can be sold in the Reserved Instance Marketplace.
- Amazon EC2 Convertible Reserved Instances can't be sold in the Reserved Instance Marketplace.
- Reserved Instances for other AWS services, such as Amazon RDS and Amazon ElastiCache, cannot be sold in the Reserved Instance Marketplace.
- There must be at least one month remaining in the term of the Standard Reserved Instance.
- You can't sell a Standard Reserved Instance in a Region that is disabled by default.
- The minimum price allowed in the Reserved Instance Marketplace is $0.00.

- You can sell No Upfront, Partial Upfront, or All Upfront Reserved Instances in the Reserved Instance Marketplace as long as they have been active in your account for at least 30 days.
Additionally, if there is an upfront payment on a Reserved Instance, it can only be sold after AWS has received the upfront payment.
- You can't sell a Reserved Instance in the Reserved Instance Marketplace if you purchased it using a volume discount.
- You cannot modify your listing in the Reserved Instance Marketplace directly. However, you can change your listing by first canceling it and then creating another listing with new parameters.
For information, see Price your Reserved Instances. You can also modify your Reserved Instances before listing them. For information, see Modify Reserved Instances.
- AWS charges a service fee of 12 percent of the total upfront price of each Standard Reserved Instance you sell in the Reserved Instance Marketplace. The upfront price is the price the seller is charging for the Standard Reserved Instance.
- When you register as a seller, the bank you specify must have a US address. For more information, see Additional seller requirements for paid products in the AWS Marketplace Seller Guide.
- Amazon Web Services India Private Limited (AWS India) customers can't register as a seller on EC2 Reserved Instance Marketplace and can't list or sell Reserved Instances in the EC2 Reserved Instance Marketplace, even if they have a US bank account. For more information, see What are the differences between AWS accounts and AWS India accounts?
- If you change your seller of record to Amazon Web Services India Private Limited (AWS India), you'll be deregistered as a seller from the EC2 Reserved Instance Marketplace and all of your existing active listings on the EC2 Reserved Instance Marketplace will be removed. To restore your seller status, you must change your account location to a country other than India and complete the seller registration process again.
#### Register as a seller Note Only the AWS account root user can register an account as a seller.
To sell in the Reserved Instance Marketplace, you must first register as a seller. During registration, you provide the following information:

- Bank information—AWS must have your bank information in order to disburse funds collected when you sell your reservations. The bank you specify must have a US address. For more information, see Bank account for disbursement.
- Tax information—All sellers are required to complete a tax information interview to determine any necessary tax reporting obligations. For more information, see Tax information.
After AWS receives your completed seller registration, you receive an email confirming your registration and informing you that you can get started selling in the Reserved Instance Marketplace.
#### Bank account for disbursement AWS must have your bank information in order to disburse funds collected when you sell your Reserved Instance. The bank you specify must have a US address. For more information, see Additional seller requirements for paid products in the AWS Marketplace Seller Guide.
To register a default bank account for disbursements
1. Open the Reserved Instance Marketplace Seller Registration page and sign in using your AWS credentials.
2. On the Manage Bank Account page, provide the following information about the bank through to receive payment:
- Bank account holder name
- Routing number
- Account number
- Bank account type Note If you are using a corporate bank account, you are prompted to send the information about the bank account via fax (1-206-765-3424).
After registration, the bank account provided is set as the default, pending verification with the bank. It can take up to two weeks to verify a new bank account, during which time you can't receive

disbursements. For an established account, it usually takes about two days for disbursements to complete.
To change the default bank account for disbursement
1. On the Reserved Instance Marketplace Seller Registration page, sign in with the account that you used when you registered.
2. On the Manage Bank Account page, add a new bank account or modify the default bank account as needed.
#### Tax information Your sale of Reserved Instances might be subject to a transaction-based tax, such as sales tax or value-added tax. You should check with your business's tax, legal, finance, or accounting department to determine if transaction-based taxes are applicable. You are responsible for collecting and sending the transaction-based taxes to the appropriate tax authority.
As part of the seller registration process, you must complete a tax interview in the Seller Registration Portal. The interview collects your tax information and populates an IRS form W-9, W-8BEN, or W-8BEN-E, which is used to determine any necessary tax reporting obligations.
The tax information you enter as part of the tax interview might differ depending on whether you operate as an individual or business, and whether you or your business are a US or non-US person or entity. As you fill out the tax interview, keep in mind the following:
- Information provided by AWS, including the information in this topic, does not constitute tax, legal, or other professional advice. To find out how the IRS reporting requirements might affect your business, or if you have other questions, contact your tax, legal, or other professional advisor.
- To fulfill the IRS reporting requirements as efficiently as possible, answer all questions and enter all information requested during the interview.
- Check your answers. Avoid misspellings or entering incorrect tax identification numbers. They can result in an invalidated tax form.
Based on your tax interview responses and IRS reporting thresholds, Amazon might file Form 1099-K. Amazon mails a copy of your Form 1099-K on or before January 31 in the year following the year that your tax account reaches the threshold levels. For example, if your account reaches the threshold in 2018, your Form 1099-K is mailed on or before January 31, 2019.

For more information about IRS requirements and Form 1099-K, see Form 1099-K FAQs on the IRS website.
#### Price your Reserved Instances When setting the price for your Reserved Instances, consider the following:
- Upfront price – The upfront price is the only price that you can specify for the Reserved Instance that you're selling. The upfront price is the one-time price that the buyer pays when they purchase each Reserved Instance.
Because the value of Reserved Instances decreases over time, by default, AWS can set prices to decrease in equal increments month over month. However, you can set different upfront prices based on when your reservation sells. For example, if your Reserved Instance has nine months of its term remaining, you can specify the amount that you would accept if a customer were to purchase that Reserved Instance with nine months remaining. You could set another price with five months remaining, and yet another price with one month remaining.
The minimum allowed price in the Reserved Instance Marketplace is $0.00.
- Limits – The following limits for selling Reserved Instances apply to the lifetime of your AWS account. They are not annual limits and they can't be increased.
- You can sell up to $50,000 in Reserved Instances.
- You can sell up to 5,000 Reserved Instances.
- Can't modify – You cannot modify your listing directly. However, you can change your listing by first canceling it and then creating another listing with new parameters.
- Can cancel – You can cancel your listing at any time, as long as it's in the active state. You cannot cancel the listing if it's already matched or being processed for a sale. If some of the instances in your listing are matched and you cancel the listing, only the remaining unmatched instances are removed from the listing.
#### List your Reserved Instances As a registered seller, you can choose to sell one or more of your Reserved Instances. You can choose to sell all of them in one listing or in portions. In addition, you can list Reserved Instances with any configuration of instance type, platform, and scope.
The console determines a suggested price. It checks for offerings that match your Reserved Instance and matches the one with the lowest price. Otherwise, it calculates a suggested price

based on the cost of the Reserved Instance for its remaining time. If the calculated value is less than $1.01, the suggested price is $1.01.
If you cancel your listing and a portion of that listing has already been sold, the cancellation is not effective on the portion that has been sold. Only the unsold portion of the listing is no longer available in the Reserved Instance Marketplace.
Console To list a Reserved Instance in the Reserved Instance Marketplace
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Reserved Instances.
3. Select the Reserved Instances to list, and choose Actions, Sell Reserved Instances.
4. On the Configure Your Reserved Instance Listing page, set the number of instances to sell and the upfront price for the remaining term in the relevant columns. See how the value of your reservation changes over the remainder of the term by selecting the arrow next to the Months Remaining column.
5. If you are an advanced user and you want to customize the pricing, you can enter different values for the subsequent months. To return to the default linear price drop, choose Reset.
6. Choose Continue when you are finished configuring your listing.
7. Confirm the details of your listing, on the Confirm Your Reserved Instance Listing page and if you're satisfied, choose List Reserved Instance.
To view your listings in the Amazon EC2 console
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Reserved Instances.
3. Select the Reserved Instance that you've listed and choose the My Listings tab near the bottom of the page.
AWS CLI To manage Reserved Instances in the Reserved Instance Marketplace
1. Get a list of your Reserved Instances by using the describe-reserved-instances command.
Note that ID of the Reserved Instance that you want to list.

2. Use the create-reserved-instances-listing command. You must specify the ID of the Reserved Instance, the number of instances, and the pricing schedule.
3. To view your listing, use the describe-reserved-instances-listings command.
4. To cancel your listing, use the cancel-reserved-instances-listing command.
PowerShell To manage Reserved Instances in the Reserved Instance Marketplace
1. Get a list of your Reserved Instances by using the Get-EC2ReservedInstance cmdlet. Note that ID of the Reserved Instance that you want to list.
2. Use the New-EC2ReservedInstancesListing cmdlet. You must specify the ID of the Reserved Instance, the number of instances, and the pricing schedule.
3. To view your listing, use the Get-EC2ReservedInstancesListing cmdlet.
4. To cancel your listing, use the Stop-EC2ReservedInstancesListing cmdlet.
#### Reserved Instance listing states Listing State on the My Listings tab of the Reserved Instances page displays the current status of your listings:
The information displayed by Listing State is about the status of your listing in the Reserved Instance Marketplace. It is different from the status information that is displayed by the State column in the Reserved Instances page. This State information is about your reservation.
- active—The listing is available for purchase.
- canceled—The listing is canceled and isn't available for purchase in the Reserved Instance Marketplace.
- closed—The Reserved Instance is not listed. A Reserved Instance might be closed because the sale of the listing was completed.
#### Lifecycle of a listing When all the instances in your listing are matched and sold, the My Listings tab shows that the Total instance count matches the count listed under Sold. Also, there are no Available instances left for your listing, and its Status is closed.

When only a portion of your listing is sold, AWS retires the Reserved Instances in the listing and creates the number of Reserved Instances equal to the Reserved Instances remaining in the count.
So, the listing ID and the listing that it represents, which now has fewer reservations for sale, is still active.
Any future sales of Reserved Instances in this listing are processed this way. When all the Reserved Instances in the listing are sold, AWS marks the listing as closed.
For example, you create a listing Reserved Instances listing ID 5ec28771-05ff-4b9b- aa31-9e57dexample with a listing count of 5.
The My Listings tab in the Reserved Instance console page displays the listing this way:
Reserved Instance listing ID 5ec28771-05ff-4b9b-aa31-9e57dexample
- Total reservation count = 5
- Sold = 0
- Available = 5
- Status = active A buyer purchases two of the reservations, which leaves a count of three reservations still available for sale. Because of this partial sale, AWS creates a new reservation with a count of three to represent the remaining reservations that are still for sale.
This is how your listing looks in the My Listings tab:
Reserved Instance listing ID 5ec28771-05ff-4b9b-aa31-9e57dexample
- Total reservation count = 5
- Sold = 2
- Available = 3
- Status = active If you cancel your listing and a portion of that listing has already sold, the cancelation is not effective on the portion that has been sold. Only the unsold portion of the listing is no longer available in the Reserved Instance Marketplace.

#### After your Reserved Instance is sold When your Reserved Instance is sold, AWS sends you an email notification. Each day that there is any kind of activity, you receive one email notification capturing all the activities of the day.
Activities can include when you create or sell a listing, or when AWS sends funds to your account.
Console To track the status of a Reserved Instance listing
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation page, choose Reserved Instances.
3. On the My Listings tab, find the value of Listing State. The tab also contains information about the term, listing price, and a breakdown of how many instances in the listing are available, pending, sold, and canceled.
AWS CLI To track the status of a Reserved Instance listing Use the describe-reserved-instances-listings command with the appropriate filter to obtain information about your listings. aws ec2 describe-reserved-instances-listings PowerShell To track the status of a Reserved Instance listing Use the Get-EC2ReservedInstancesListing cmdlet.
Get-EC2ReservedInstancesListing
#### Getting paid As soon as AWS receives funds from the buyer, a message is sent to the registered owner account email for the sold Reserved Instance.
AWS sends an Automated Clearing House (ACH) wire transfer to your specified bank account.
Typically, this transfer occurs between one to three days after your Reserved Instance has been

sold. Disbursements take place once a day. You will receive an email with a disbursement report after the funds are released. Keep in mind that you can't receive disbursements until AWS receives verification from your bank. This can take up to two weeks.
The Reserved Instance that you sold continues to appear when you describe your Reserved Instances.
You receive a cash disbursement for your Reserved Instances through a wire transfer directly into your bank account. AWS charges a service fee of 12 percent of the total upfront price of each Reserved Instance you sell in the Reserved Instance Marketplace.
#### Information shared with the buyer When you sell in the Reserved Instance Marketplace, AWS shares your company's legal name on the buyer's statement in accordance with US regulations. In addition, if the buyer calls Support because the buyer needs to contact you for an invoice or for some other tax-related reason, AWS might need to provide the buyer with your email address so that the buyer can contact you directly.
For similar reasons, the buyer's ZIP code and country information are provided to the seller in the disbursement report. As a seller, you might need this information to accompany any necessary transaction taxes that you remit to the government (such as sales tax and value-added tax).
AWS cannot offer tax advice, but if your tax specialist determines that you need specific additional information, contact Support.
Modify Reserved Instances When your needs change, you can modify your Standard or Convertible Reserved Instances and continue to benefit from the billing benefit. You can modify attributes such as the Availability Zone, instance size (within the same instance family and generation), and scope of your Reserved Instance.
Note You can also exchange a Convertible Reserved Instance for another Convertible Reserved Instance with a different configuration. For more information, see Exchange Convertible Reserved Instances.
You can modify all or a subset of your Reserved Instances. You can separate your original Reserved Instances into two or more new Reserved Instances. For example, if you have a reservation for

10 instances in us-east-1a and decide to move 5 instances to us-east-1b, the modification request results in two new reservations: one for 5 instances in us-east-1a and the other for 5 instances in us-east-1b.
You can also merge two or more Reserved Instances into a single Reserved Instance. For example, if you have four t2.small Reserved Instances of one instance each, you can merge them to create one t2.large Reserved Instance. For more information, see Support for modifying instance sizes.
After modification, the benefit of the Reserved Instances is applied only to instances that match the new parameters. For example, if you change the Availability Zone of a reservation, the capacity reservation and pricing benefits are automatically applied to instance usage in the new Availability Zone. Instances that no longer match the new parameters are charged at the On-Demand rate, unless your account has other applicable reservations.
If your modification request succeeds:
- The modified reservation becomes effective immediately and the pricing benefit is applied to the new instances beginning at the hour of the modification request. For example, if you successfully modify your reservations at 9:15PM, the pricing benefit transfers to your new instance at 9:00PM. You can get the effective date of the modified Reserved Instances by using the describe-reserved-instances command.
- The original reservation is retired. Its end date is the start date of the new reservation, and the end date of the new reservation is the same as the end date of the original Reserved Instance. If you modify a three-year reservation that had 16 months left in its term, the resulting modified reservation is a 16-month reservation with the same end date as the original one.
- The modified reservation lists a $0 fixed price and not the fixed price of the original reservation.
- The fixed price of the modified reservation does not affect the discount pricing tier calculations applied to your account, which are based on the fixed price of the original reservation.
If your modification request fails, your Reserved Instances maintain their original configuration, and are immediately available for another modification request.
There is no fee for modification, and you do not receive any new bills or invoices.
You can modify your reservations as frequently as you like, but you cannot change or cancel a pending modification request after you submit it. After the modification has completed successfully, you can submit another modification request to roll back any changes you made, if needed.

Contents
- Requirements and restrictions for modification
- Support for modifying instance sizes
- Submit modification requests
- Troubleshoot modification requests
#### Requirements and restrictions for modification You can modify these attributes as follows.
Modifiable attribute
#### Supported platforms Limitations and considera tions Change Availability Zones within the same Region Linux and Windows - Change the scope from  Avai lability Zone to Region and vice versa Linux and Windows A zonal Reserved Instance is scoped to an Availability Zone and reserves  capacity in that Availability Zone. If you change the scope from Availability Zone to Region (in other words, from zonal to  regional), you lose the capacity reservation benefit.
A regional Reserved Instance is scoped to a Region.
Your  Reserved Instance discount can apply to instances running in any Availability Zone in that Region. Furthermore, the Reserved  Instance discount applies to instance usage

Modifiable attribute
#### Supported platforms Limitations and considera tions across all sizes in  the selected instance family. If you change the scope from  Region to Availability Zone (in other words, from regional to zonal), you lose Availability Zone flexibility and instance size  flexibility (if applicable).
For more information, see How Reserved Instance discounts are applied.
Change the instance size within the same instance family and generation Linux/UNIX only Instance size flexibility is not available for Reserved Instances on the  other platforms, which include Linux with SQL Server Standard,  Linux with SQL Server Web, Linux with SQL Server Enterprise, Red  Hat Enterprise Linux, SUSE Linux, Windows, Windows with SQL Standard, Windows with SQL Server Enterprise, and Windows with  SQL Server Web.
The reservation must use default tenancy. Some instance  families are not supported, because there are no other sizes  available.
For more information, see Support for modifying instance  sizes Requirements Amazon EC2 processes your modification request if there is sufficient capacity for your new configuration (if applicable), and if the following conditions are met:

- The Reserved Instance cannot be modified before or at the same time that you purchase it
- The Reserved Instance must be active
- There cannot be a pending modification request
- The Reserved Instance is not listed in the Reserved Instance Marketplace
- There must be a match between the instance size footprint of the original reservation and the new configuration. For more information, see Support for modifying instance sizes.
- The original Reserved Instances are all Standard Reserved Instances or all Convertible Reserved Instances, not some of each type
- The original Reserved Instances must expire within the same hour, if they are Standard Reserved Instances
- For modifying instance size, the Reserved Instance must support instance size flexibility. For the list of Reserved Instances that don't support instance size flexibility, see Instance size flexibility.
#### Support for modifying instance sizes You can modify the instance size of a Reserved Instance if the following requirements are met.
Requirements
- The platform is Linux/UNIX.
- You must select another instance size in the same instance family (indicated by a letter, for example, T) and generation (indicated by a number, for example, 2).
For example, you can modify a Reserved Instance from t2.small to t2.large because they're both in the same T2 family and generation. But you can't modify a Reserved Instance from T2 to M2 or from T2 to T3, because in both these examples, the target instance family and generation are not the same as the original Reserved Instance.
- You can modify the instance size of a Reserved Instance only if it supports instance size flexibility. For the list of Reserved Instances that don't support instance size flexibility, see Instance size flexibility.
- You can't modify the instance size of Reserved Instances for t1.micro instances, because t1.micro has only one size.
- The original and new Reserved Instance must have the same instance size footprint.
Contents

- Instance size footprint
- Normalization factors for bare metal instances
##### Instance size footprint Each Reserved Instance has an instance size footprint, which is determined by the normalization factor of the instance size and the number of instances in the reservation. When you modify the instance sizes in an Reserved Instance, the footprint of the new configuration must match that of the original configuration, otherwise the modification request is not processed.
To calculate the instance size footprint of a Reserved Instance, multiply the number of instances by the normalization factor. In the Amazon EC2 console, the normalization factor is measured in units.
The following table describes the normalization factor for the instance sizes in an instance family.
For example, t2.medium has a normalization factor of 2, so a reservation for four t2.medium instances has a footprint of 8 units.
Instance size Normalization factor nano 0.25 micro 0.5 small 1 medium 2 large 4 xlarge 8 2xlarge 16 3xlarge 24 4xlarge 32 6xlarge 48 8xlarge 64

Instance size Normalization factor 9xlarge 72 10xlarge 80 12xlarge 96 16xlarge 128 18xlarge 144 24xlarge 192 32xlarge 256 48xlarge 384 56xlarge 448 112xlarge 896 You can allocate your reservations into different instance sizes across the same instance family as long as the instance size footprint of your reservation remains the same. For example, you can divide a reservation for one t2.large (1 @ 4 units) instance into four t2.small (4 @ 1 unit) instances. Similarly, you can combine a reservation for four t2.small instances into one t2.large instance. However, you cannot change your reservation for two t2.small instances into one t2.large instance because the footprint of the new reservation (4 units) is larger than the footprint of the original reservation (2 units).
In the following example, you have a reservation with two t2.micro instances (1 unit) and a reservation with one t2.small instance (1 unit). If you merge both of these reservations to a single reservation with one t2.medium instance (2 units), the footprint of the new reservation equals the footprint of the combined reservations.

You can also modify a reservation to divide it into two or more reservations. In the following example, you have a reservation with a t2.medium instance (2 units). You can divide the reservation into two reservations, one with two t2.nano instances (.5 units) and the other with three t2.micro instances (1.5 units).
##### Normalization factors for bare metal instances You can modify a reservation with metal instances using other sizes within the same instance family. Similarly, you can modify a reservation with instances other than bare metal instances using the metal size within the same instance family. Generally, a bare metal instance is the same size as the largest available instance size within the same instance family. For example, an i3.metal instance is the same size as an i3.16xlarge instance, so they have the same normalization factor.
The following table describes the normalization factor for the bare metal instance sizes in the instance families that have bare metal instances. The normalization factor for metal instances depends on the instance family, unlike the other instance sizes.

Instance size Normalization factor a1.metal 32 m5zn.metal  | x2iezn.metal   z1d.metal 96 c6g.metal  |   c6gd.metal  |   i3.metal |   m6g.metal  |   m6gd.metal
|   r6g.metal  |   r6gd.metal  |   x2gd.metal 128 c5n.metal 144 c5.metal |   c5d.metal  |   i3en.metal  |   m5.metal |   m5d.metal  | m5dn.metal  |   m5n.metal  |   r5.metal |   r5b.metal  |   r5d.metal  | r5dn.metal  |   r5n.metal 192 c6i.metal  | c6id.metal  | m6i.metal  | m6id.metal  | r6d.metal
| r6id.metal 256 u-18tb1.metal  | u-24tb1.metal 448 u-6tb1.metal  | u-9tb1.metal  | u-12tb1.metal 896 For example, an i3.metal instance has a normalization factor of 128. If you purchase an i3.metal default tenancy Amazon Linux/Unix Reserved Instance, you can divide the reservation as follows:
- An i3.16xlarge is the same size as an i3.metal instance, so its normalization factor is 128 (128/1). The reservation for one i3.metal instance can be modified into one i3.16xlarge instance.
- An i3.8xlarge is half the size of an i3.metal instance, so its normalization factor is 64 (128/2). The reservation for one i3.metal instance can be divided into two i3.8xlarge instances.
- An i3.4xlarge is a quarter the size of an i3.metal instance, so its normalization factor is 32 (128/4). The reservation for one i3.metal instance can be divided into four i3.4xlarge instances.

#### Submit modification requests Before you modify your Reserved Instances, ensure that you have read the applicable restrictions.
Before you modify the instance size, calculate the total instance size footprint of the original reservations that you want to modify and ensure that it matches the total instance size footprint of your new configurations.
Console To modify your Reserved Instances
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. On the Reserved Instances page, select one or more Reserved Instances to modify, and choose Actions, Modify Reserved Instances.
If your Reserved Instances are not in the active state or cannot be modified, Modify Reserved Instances is disabled.
3. The first entry in the modification table displays attributes of the selected Reserved Instances, and at least one target configuration beneath it. The Units column displays the total instance size footprint. Choose Add for each new configuration to add. Modify the attributes as needed for each configuration.
- Scope: Choose whether the configuration applies to an Availability Zone or to the whole Region.
- Availability Zone: Choose the required Availability Zone. Not applicable for regional Reserved Instances.
- Instance type: Select the required instance type. The combined configurations must equal the instance size footprint of your original configurations.
- Count: Specify the number of instances. To split the Reserved Instances into multiple configurations, reduce the count, choose Add, and specify a count for the additional configuration. For example, if you have a single configuration with a count of 10, you can change its count to 6 and add a configuration with a count of 4. This process retires the original Reserved Instance after the new Reserved Instances are activated.
4. Choose Continue.
5. To confirm your modification choices when you finish specifying your target configurations, choose Submit modifications.

6. You can determine the status of your modification request by looking at the State column in the Reserved Instances screen. The following are the possible states.
- active (pending modification) — Transition state for original Reserved Instances
- retired (pending modification) — Transition state for original Reserved Instances while new Reserved Instances are being created
- retired — Reserved Instances successfully modified and replaced
- active — One of the following:
- New Reserved Instances created from a successful modification request
- Original Reserved Instances after a failed modification request AWS CLI To modify your Reserved Instances Use the modify-reserved-instances command. You can provide the configuration details in a JSON file. aws ec2 modify-reserved-instances \ --reserved-instances-ids b847fa93-e282-4f55-b59a-1342f5bd7c02 \ --target-configurations file://configuration.json To get the status of your modification request Use the describe-reserved-instances-modifications command. The status is processing, fulfilled, or failed. aws ec2 describe-reserved-instances-modifications \ --reserved-instances-modification-ids rimod-d3ed4335-b1d3-4de6-ab31-0f13aaf46687 \ --query ReservedInstancesModifications[].Status PowerShell To modify your Reserved Instances Use the Edit-EC2ReservedInstance cmdlet. You can provide the configuration details in an object of type Amazon.EC2.Model.ReservedInstancesConfiguration.

Edit-EC2ReservedInstance `
    -ReservedInstancesId b847fa93-e282-4f55-b59a-1342f5bd7c02 `
    -TargetConfiguration $configuration To get the status of your modification request Use the Get-EC2ReservedInstancesModification cmdlet. The status is processing, fulfilled, or failed.
Get-EC2ReservedInstancesModification `
    -ReservedInstancesModificationId rimod-d3ed4335-b1d3-4de6-ab31-0f13aaf46687 | `
    Select Status
#### Troubleshoot modification requests If the target configuration settings that you requested were unique, you receive a message that your request is being processed. At this point, Amazon EC2 has only determined that the parameters of your modification request are valid. Your modification request can still fail during processing due to unavailable capacity.
In some situations, you might get a message indicating incomplete or failed modification requests instead of a confirmation. Use the information in such messages as a starting point for resubmitting another modification request. Ensure that you have read the applicable restrictions before submitting the request.
Not all selected Reserved Instances can be processed for modification Amazon EC2 identifies and lists the Reserved Instances that cannot be modified. If you receive a message like this, go to the Reserved Instances page in the Amazon EC2 console and check the information for the Reserved Instances.
Error in processing your modification request You submitted one or more Reserved Instances for modification and none of your requests can be processed. Depending on the number of reservations you are modifying, you can get different versions of the message.
Amazon EC2 displays the reasons why your request cannot be processed. For example, you might have specified the same target configuration—a combination of Availability Zone and platform

—for one or more subsets of the Reserved Instances you are modifying. Try submitting the modification requests again, but ensure that the instance details of the reservations match, and that the target configurations for all subsets being modified are unique.
### Exchange Convertible Reserved Instances You can exchange one or more Convertible Reserved Instances for another Convertible Reserved Instance with a different configuration, including instance family, operating system, and tenancy.
There are no limits to how many times you perform an exchange, as long as the new Convertible Reserved Instance is of an equal or higher value than the Convertible Reserved Instances that you are exchanging.
When you exchange your Convertible Reserved Instance, the number of instances for your current reservation is exchanged for a number of instances that cover the equal or higher value of the configuration of the new Convertible Reserved Instance. Amazon EC2 calculates the number of Reserved Instances that you can receive as a result of the exchange.
You can't exchange Standard Reserved Instances, but you can modify them. For more information, see Modify Reserved Instances .
Contents
- Requirements for exchanging Convertible Reserved Instances
- Calculate Convertible Reserved Instances exchanges
- Merge Convertible Reserved Instances
- Exchange a portion of a Convertible Reserved Instance
- Submit exchange requests
#### Requirements for exchanging Convertible Reserved Instances If the following conditions are met, Amazon EC2 processes your exchange request. Your Convertible Reserved Instance must be:
- Active
- Not pending a previous exchange request
- Have at least 24 hours remaining before it expires The following rules apply:

- Convertible Reserved Instances must be exchanged for other Convertible Reserved Instances currently offered by AWS.
- Convertible Reserved Instances are associated with a specific Region, which is fixed for the duration of the reservation's term. You can't exchange a Convertible Reserved Instance for a Convertible Reserved Instance in a different Region.
- To exchange a zonal Convertible Reserved Instance, AWS must have enough capacity for the new instance type in the Region.
- You can exchange one or more Convertible Reserved Instances at a time for one Convertible Reserved Instance only.
- To exchange a portion of a Convertible Reserved Instance, you can modify it into two or more reservations, and then exchange one or more of the reservations for a new Convertible Reserved Instance. For more information, see Exchange a portion of a Convertible Reserved Instance. For more information about modifying your Reserved Instances, see Modify Reserved Instances.
- All Upfront Convertible Reserved Instances can be exchanged for Partial Upfront Convertible Reserved Instances, and vice versa.
Note If the total upfront payment required for the exchange (true-up cost) is less than $0.00, AWS automatically gives you a quantity of instances in the Convertible Reserved Instance that ensures that true-up cost is $0.00 or more.
Note If the total value (upfront price + hourly price * number of remaining hours) of the new Convertible Reserved Instance is less than the total value of the exchanged Convertible Reserved Instance, AWS automatically gives you a quantity of instances in the Convertible Reserved Instance that ensures that the total value is the same or higher than that of the exchanged Convertible Reserved Instance.
- To benefit from better pricing, you can exchange a No Upfront Convertible Reserved Instance for an All Upfront or Partial Upfront Convertible Reserved Instance.
- You can't exchange All Upfront and Partial Upfront Convertible Reserved Instances for No Upfront Convertible Reserved Instances.

- You can exchange a No Upfront Convertible Reserved Instance for another No Upfront Convertible Reserved Instance only if the new Convertible Reserved Instance's hourly price is the same or higher than the exchanged Convertible Reserved Instance's hourly price.
Note If the total value (hourly price * number of remaining hours) of the new Convertible Reserved Instance is less than the total value of the exchanged Convertible Reserved Instance, AWS automatically gives you a quantity of instances in the Convertible Reserved Instance that ensures that the total value is the same or higher than that of the exchanged Convertible Reserved Instance.
- If you exchange multiple Convertible Reserved Instances that have different expiration dates, the expiration date for the new Convertible Reserved Instance is the date that's furthest in the future.
- If you exchange a single Convertible Reserved Instance, it must have the same term (1-year or 3-years) as the new Convertible Reserved Instance. If you merge multiple Convertible Reserved Instances with different term lengths, the new Convertible Reserved Instance has a 3-year term.
For more information, see Merge Convertible Reserved Instances.
- When Amazon EC2 exchanges a Convertible Reserved Instance, it retires the associated reservation, and transfers the end date to the new reservation. After the exchange, Amazon EC2 sets both the end date for the old reservation and the start date for the new reservation equal to the date of the exchange. For example, if you exchange a three-year reservation that had 16 months left in its term, the new reservation is a 16-month reservation with the same end date as the reservation from the Convertible Reserved Instance that you exchanged.
#### Calculate Convertible Reserved Instances exchanges Exchanging Convertible Reserved Instances is free. However, you might be required to pay a true- up cost, which is a prorated upfront cost of the difference between the Convertible Reserved Instances that you had and the new Convertible Reserved Instances that you receive from the exchange.
Each Convertible Reserved Instance has a list value. This list value is compared to the list value of the Convertible Reserved Instances that you want in order to determine how many instance reservations you can receive from the exchange.

For example: You have 1 x $35-list value Convertible Reserved Instance that you want to exchange for a new instance type with a list value of $10.
$35/$10 = 3.5 You can exchange your Convertible Reserved Instance for three $10 Convertible Reserved Instances. It's not possible to purchase half reservations; therefore you must purchase an additional Convertible Reserved Instance to cover the remainder:
3.5 = 3 whole Convertible Reserved Instances + 1 additional Convertible Reserved Instance The fourth Convertible Reserved Instance has the same end date as the other three. If you are exchanging Partial or All Upfront Convertible Reserved Instances, you pay the true-up cost for the fourth reservation. If the remaining upfront cost of your Convertible Reserved Instances is $500, and the new reservation would normally cost $600 on a prorated basis, you are charged $100.
$600 prorated upfront cost of new reservations - $500 remaining upfront cost of old reservations = $100 difference
#### Merge Convertible Reserved Instances If you merge two or more Convertible Reserved Instances, the term of the new Convertible Reserved Instance must be the same as the old Convertible Reserved Instances, or the highest of the Convertible Reserved Instances. The expiration date for the new Convertible Reserved Instance is the expiration date that's furthest in the future.
For example, you have the following Convertible Reserved Instances in your account:
Reserved Instance ID Term Expiration date aaaa1111 1-year 2018-12-31 bbbb2222 1-year 2018-07-31 cccc3333 3-year 2018-06-30 dddd4444 3-year 2019-12-31

- You can merge aaaa1111 and bbbb2222 and exchange them for a 1-year Convertible Reserved Instance. You cannot exchange them for a 3-year Convertible Reserved Instance. The expiration date of the new Convertible Reserved Instance is 2018-12-31.
- You can merge bbbb2222 and cccc3333 and exchange them for a 3-year Convertible Reserved Instance. You cannot exchange them for a 1-year Convertible Reserved Instance. The expiration date of the new Convertible Reserved Instance is 2018-07-31.
- You can merge cccc3333 and dddd4444 and exchange them for a 3-year Convertible Reserved Instance. You cannot exchange them for a 1-year Convertible Reserved Instance. The expiration date of the new Convertible Reserved Instance is 2019-12-31.
#### Exchange a portion of a Convertible Reserved Instance You can use the modification process to split your Convertible Reserved Instance into smaller reservations, and then exchange one or more of the new reservations for a new Convertible Reserved Instance. The following examples demonstrate how you can do this.
Example: Convertible Reserved Instance with multiple instances In this example, you have a t2.micro Convertible Reserved Instance with four instances in the reservation. To exchange two t2.micro instances for an m4.xlarge instance:
1. Modify the t2.micro Convertible Reserved Instance by splitting it into two t2.micro Convertible Reserved Instances with two instances each.
2. Exchange one of the new t2.micro Convertible Reserved Instances for an m4.xlarge Convertible Reserved Instance.
Example: Convertible Reserved Instance with a single instance In this example, you have a t2.large Convertible Reserved Instance. To change it to a smaller t2.medium instance and a m3.medium instance:

1. Modify the t2.large Convertible Reserved Instance by splitting it into two t2.medium Convertible Reserved Instances. A single t2.large instance has the same instance size footprint as two t2.medium instances.
2. Exchange one of the new t2.medium Convertible Reserved Instances for an m3.medium Convertible Reserved Instance.
For more information, see Support for modifying instance sizes and Submit exchange requests.
#### Submit exchange requests You can exchange your Convertible Reserved Instances. Reserved Instances that are exchanged are retired.
Console To exchange Convertible Reserved Instances
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. Choose Reserved Instances, select the Convertible Reserved Instances to exchange, and choose Actions, Exchange Reserved Instance.
3. Select the attributes of the desired configuration, and choose Find offering.
4. Select a new Convertible Reserved Instance. At the bottom of the screen, you can view the number of Reserved Instances that you receive for the exchange, and any additional costs.
5. When you have selected a Convertible Reserved Instance that meets your needs, choose Review.
6. Choose Exchange, and then Close.

AWS CLI To exchange a Convertible Reserved Instance
1. Find a new Convertible Reserved Instance that meets your needs by using the describe- reserved-instances-offerings command.
2. Get a quote for the exchange by using the get-reserved-instances-exchange-quote command. This includes the number of Reserved Instances you get from the exchange, and the true-up cost for the exchange:
3. Perform the exchange by using the accept-reserved-instances-exchange-quote command.
PowerShell To exchange a Convertible Reserved Instance
1. Find a new Convertible Reserved Instance that meets your needs by using the Get- EC2ReservedInstancesOffering cmdlet.
2. Get a quote for the exchange by using the GetEC2-ReservedInstancesExchangeQuote cmdlet. This includes the number of Reserved Instances you get from the exchange, and the true-up cost for the exchange:
3. Perform the exchange by using the Approve-EC2ReservedInstancesExchangeQuote cmdlet
### Reserved Instance quotas You can purchase new Reserved Instances each month. The number of new Reserved Instances that you can purchase each month is determined by your monthly quota, as follows:
Quota description Default quota New regional Reserved Instances 20 per Region per month New zonal Reserved Instances 20 per Availability Zone per month For example, in a Region with three Availability Zones, the default quota is 80 new Reserved Instances per month, calculated as follows:
- 20 regional Reserved Instances for the Region

- Plus 60 zonal Reserved Instances (20 for each of the three Availability Zones)
Instances in the running state count toward your quota. Instances that are in the pending, stopping, stopped, and hibernated states do not count towards your quota.
#### View the number of Reserved Instances you have purchased The number of Reserved Instances that you purchase is indicated by the Instance count field (console) or the InstanceCount parameter (AWS CLI). When you purchase new Reserved Instances, the quota is measured against the total instance count. For example, if you purchase a single Reserved Instance configuration with an instance count of 10, the purchase counts towards your quota as 10, not 1.
You can view how many Reserved Instances you have purchased by using the Amazon EC2 or the AWS CLI.
Console To view the number of Reserved Instances you have purchased
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Reserved Instances.
3. Select a Reserved Instance configuration from the table, and check the Instance count field.
In the following screenshot, the selected line represents a single Reserved Instance configuration for a t3.micro instance type. The Instance count column in the table view and the Instance count field in the detail view (outlined in the screenshot) indicate that there are 10 Reserved Instances for this configuration.

AWS CLI To view the number of Reserved Instances you have purchased Use the  describe-reserved-instances command and specify the ID of the Reserved Instance configuration. aws ec2 describe-reserved-instances \ --reserved-instances-ids a1b2c3d4-5678-90ab-cdef-EXAMPLE11111 \ --output table The following is example output. The InstanceCount field indicates that there are 10 Reserved Instances for this configuration.
-------------------------------------------------------------------
|                    DescribeReservedInstances                    | +-----------------------------------------------------------------+
||                       ReservedInstances                       ||
|+----------------------+----------------------------------------+|
||  CurrencyCode        |  USD                                   ||
||  Duration            |  31536000                              ||
||  End                 |  2023-08-27T13:29:44+00:00             ||
||  FixedPrice          |  59.0                                  ||

||   InstanceCount       |   10                                    ||
||  InstanceTenancy     |  default                               ||
||  InstanceType        |  t3.micro                              ||
||  OfferingClass       |  standard                              ||
||  OfferingType        |  All Upfront                           ||
||  ProductDescription  |  Linux/UNIX                            ||
||  ReservedInstancesId |  a1b2c3d4-5678-90ab-cdef-EXAMPLE11111  ||
||  Scope               |  Region                                ||
||  Start               |  2022-08-27T13:29:45.938000+00:00      ||
||  State               |  active                                ||
||  UsagePrice          |  0.0                                   ||
|+----------------------+----------------------------------------+|
|||                      RecurringCharges                       |||
||+----------------------------------+--------------------------+||
|||  Amount                          |  0.0                     |||
|||  Frequency                       |  Hourly                  |||
||+----------------------------------+--------------------------+|| PowerShell To view the number of Reserved Instances you have purchased Use the  Get-EC2ReservedInstance Cmdlet and specify the ID of the Reserved Instance configuration.
Get-EC2ReservedInstance -ReservedInstancesId a1b2c3d4-5678-90ab-cdef-EXAMPLE11111 The following is example output. The InstanceCount field indicates that there are 10 Reserved Instances for this configuration.
AvailabilityZone    :
CurrencyCode        : USD Duration            : 31536000 End                 : 1/12/2017 8:57:08 PM FixedPrice          : 0 InstanceCount       : 10 InstanceTenancy     : default InstanceType        : t3.medium OfferingClass       : standard OfferingType        : All Upfront ProductDescription  : Windows RecurringCharges    : {}

ReservedInstancesId : a1b2c3d4-5678-90ab-cdef-EXAMPLE11111 Scope               : Region Start               : 10/12/2016 4:00:00 PM State               : active Tags                : {} UsagePrice          : 0
#### Considerations A regional Reserved Instance applies a discount to a running On-Demand Instance. The default On-Demand Instance limit is 20. You cannot exceed your running On-Demand Instance limit by purchasing regional Reserved Instances. For example, if you already have 20 running On-Demand Instances, and you purchase 20 regional Reserved Instances, the 20 regional Reserved Instances are used to apply a discount to the 20 running On-Demand Instances. If you purchase more regional Reserved Instances, you will not be able to launch more instances because you have reached your On-Demand Instance limit.
Before purchasing regional Reserved Instances, make sure your On-Demand Instance limit matches or exceeds the number of regional Reserved Instances you intend to own. If required, make sure you request an increase to your On-Demand Instance limit before purchasing more regional Reserved Instances.
A zonal Reserved Instance—a Reserved Instance that is purchased for a specific Availability Zone —provides a capacity reservation as well as a discount. You can exceed your running On-Demand Instance limit by purchasing zonal Reserved Instances. For example, if you already have 20 running On-Demand Instances, and you purchase 20 zonal Reserved Instances, you can launch a further 20 On-Demand Instances that match the specifications of your zonal Reserved Instances, giving you a total of 40 running instances.
#### View your Reserved Instance quotas and request a quota increase The Amazon EC2 console provides quota information. You can also request an increase in your quotas. For more information, see View your current quotas and Request an increase.
## Spot Instances A Spot Instance is an instance that uses spare EC2 capacity that is available for less than the On-Demand price. Because Spot Instances enable you to request unused EC2 instances at steep discounts, you can lower your Amazon EC2 costs significantly. The hourly price for a Spot Instance

is called a Spot price. The Spot price of each instance type in each Availability Zone is set by Amazon EC2, and is adjusted gradually based on the long-term supply of and demand for Spot Instances. Your Spot Instance runs whenever capacity is available.
Spot Instances are a cost-effective choice if you can be flexible about when your applications run and if your applications can be interrupted. For example, Spot Instances are well-suited for data analysis, batch jobs, background processing, and optional tasks. For more information, see Amazon EC2 Spot Instances.
For a comparison of the different purchasing options for EC2 instances, see Amazon EC2 billing and purchasing options.
### Concepts Before you get started with Spot Instances, you should be familiar with the following concepts:
- Spot capacity pool – A set of unused EC2 instances with the same instance type (for example, m5.large) and Availability Zone.
- Spot price – The current price of a Spot Instance per hour.
- Spot Instance request – Requests a Spot Instance. When capacity is available, Amazon EC2 fulfills your request. A Spot Instance request is either one-time or persistent. Amazon EC2 automatically resubmits a persistent Spot Instance request after the Spot Instance associated with the request is interrupted.
- EC2 instance rebalance recommendation – Amazon EC2 emits an instance rebalance recommendation signal to notify you that a Spot Instance is at an elevated risk of interruption.
This signal provides an opportunity to proactively rebalance your workloads across existing or new Spot Instances without having to wait for the two-minute Spot Instance interruption notice.
- Spot Instance interruption – Amazon EC2 terminates, stops, or hibernates your Spot Instance when Amazon EC2 needs the capacity back. Amazon EC2 provides a Spot Instance interruption notice, which gives the instance a two-minute warning before it is interrupted.
### Differences between Spot Instances and On-Demand Instances The following table lists the key differences between Spot Instances and On-Demand Instances.

Spot Instances On-Demand Instances

Spot Instances On-Demand Instances Launch time Can only be launched immediately if the Spot Instance request is active  and capacity is available.
Can only be launched immediately if you make a manual launch  request and capacity is available.
Available capacity If capacity is not available, the Spot Instance request continues to  automa tically make the launch request until capacity becomes  available.
If capacity is not available when you make a launch request,  you get an insufficient capacity error (ICE).
Hourly price The hourly price for Spot Instances varies based on long-term supply  and demand.
The hourly price for On-Demand Instances is static.
Rebalance recommend ation The signal that Amazon EC2 emits for a running Spot Instance when the instance  is at an elevated risk of interruption.
You determine when an On-Demand Instance is interrupted (stopped, hibernated,  or terminated).
Instance interruption You can stop and start an Amazon EBS-backed Spot Instance. In addition, Amazon EC2 can interrupt an  indivi dual Spot Instance if capacity is no longer available.
You determine when an On-Demand Instance is interrupted (stopped, hibernated, or terminated).
### Pricing and savings You pay the Spot price for Spot Instances, which is set by Amazon EC2 and adjusted gradually based on the long-term supply of and demand for Spot Instances. Your Spot Instances run until you terminate them, capacity is no longer available, or your Amazon EC2 Auto Scaling group terminates them during scale in.
If you or Amazon EC2 interrupts a running Spot Instance, you are charged for the seconds used or the full hour, or you receive no charge, depending on the operating system used and who interrupted the Spot Instance. For more information, see Billing for interrupted Spot Instances.

Spot Instances are not covered by Savings Plans. If you have a Savings Plans, it does not provide additional savings on top of the savings that you already get from using Spot Instances.
Furthermore, your spend on Spot Instances does not apply the commitments in your Compute Savings Plans.
#### View prices To view the current (updated every five minutes) lowest Spot price per AWS Region and instance type, see the Amazon EC2 Spot Instances Pricing page.
To view the Spot price history for the past three months, use the Amazon EC2 console or the describe-spot-price-history command. For more information, see View Spot Instance pricing history.
We independently map Availability Zones to codes for each AWS account. Therefore, you can get different results for the same Availability Zone code (for example, us-west-2a) between different accounts.
#### View savings You can view the savings made from using Spot Instances for a single Spot Fleet or for all Spot Instances. You can view the savings made in the last hour or the last three days, and you can view the average cost per vCPU hour and per memory (GiB) hour. Savings are estimated and may differ from actual savings because they do not include the billing adjustments for your usage. For more information about viewing savings information, see Savings from purchasing Spot Instances.
#### View billing Your bill provides details about your service usage. For more information, see Viewing your bill in the AWS Billing User Guide.
### Best practices for Amazon EC2 Spot Amazon EC2 provides access to spare EC2 compute capacity in the AWS Cloud through Spot Instances at savings of up to 90% compared to On-Demand prices. The only difference between On-Demand Instances and Spot Instances is that Spot Instances can be interrupted by Amazon EC2, with two minutes of notice, if Amazon EC2 needs to reclaim the capacity. To ensure the best experience with Spot Instances, it's important to understand and apply best practices for their use.

Spot Instances are recommended for stateless, fault-tolerant, flexible applications. For example, Spot Instances work well for big data, containerized workloads, CI/CD, stateless web servers, high performance computing (HPC), and rendering workloads.
While running, Spot Instances are exactly the same as On-Demand Instances. However, Spot does not guarantee that you can keep your running instances long enough to finish your workloads.
Spot also does not guarantee that you can get immediate availability of the instances that you are looking for, or that you can always get the aggregate capacity that you requested. Moreover, Spot Instance interruptions and capacity can change over time because Spot Instance availability varies based on supply and demand, and past performance isn't a guarantee of future results.
Spot Instances are not suitable for workloads that are inflexible, stateful, fault-intolerant, or tightly coupled between instance nodes. We do not recommend Spot Instances for workloads that are intolerant of occasional periods when the entire target capacity is not completely available. While following Spot best practices to be flexible about instance types and Availability Zones provides the best chance for high availability, there are no guarantees that capacity will be available, because surges in demand for On-Demand Instances can disrupt workloads on Spot Instances.
We strongly discourage using Spot Instances for these workloads or attempting to fail over to On- Demand Instances to handle interruptions or periods of unavailability. Failing over to On-Demand Instances can inadvertently drive interruptions for your other Spot Instances. In addition if Spot Instances for a combination of instance type and Availability Zone get interrupted, it might become difficult for you to get On-Demand Instances with that same combination.
Regardless of whether you're an experienced Spot user or new to Spot Instances, if you are currently experiencing issues with Spot Instance interruptions or availability, we recommend that you follow these best practices to have the best experience using the Spot service.
Spot best practices
- Prepare individual instances for interruptions
- Be flexible about instance types and Availability Zones
- Use attribute-based instance type selection
- Use Spot placement scores to identify optimal Regions and Availability Zones
- Use EC2 Auto Scaling groups or EC2 Fleet to manage your aggregate capacity
- Use the price and capacity optimized allocation strategy
- Use integrated AWS services to manage your Spot Instances
- Which is the best Spot request method to use?

#### Prepare individual instances for interruptions The best way for you to gracefully handle Spot Instance interruptions is to architect your application to be fault-tolerant. To accomplish this, you can take advantage of EC2 instance rebalance recommendations and Spot Instance interruption notices.
An EC2 Instance rebalance recommendation is a signal that notifies you when a Spot Instance is at an elevated risk of interruption. The signal gives you the opportunity to proactively manage the Spot Instance in advance of the two-minute Spot Instance interruption notice. You can decide to rebalance your workload to new or existing Spot Instances that are not at an elevated risk of interruption. We've made it easy for you to use this signal by using the Capacity Rebalancing feature in Auto Scaling groups and EC2 Fleet.
A Spot Instance interruption notice is a warning that is issued two minutes before Amazon EC2 interrupts a Spot Instance. If your workload is "time-flexible," you can configure your Spot Instances to be stopped or hibernated, instead of being terminated, when they are interrupted.
Amazon EC2 automatically stops or hibernates your Spot Instances on interruption, and automatically resumes the instances when we have available capacity.
We recommend that you create a rule in Amazon EventBridge that captures the rebalance recommendations and interruption notifications, and then triggers a checkpoint for the progress of your workload or gracefully handles the interruption. For more information, see Monitor rebalance recommendation signals. For a detailed example that walks you through how to create and use event rules, see Taking Advantage of Amazon EC2 Spot Instance Interruption Notices.
For more information, see EC2 instance rebalance recommendations and Spot Instance interruptions.
#### Be flexible about instance types and Availability Zones A Spot capacity pool is a set of unused EC2 instances with the same instance type (for example, m5.large) and Availability Zone (for example, us-east-1a). You should be flexible about which instance types you request and in which Availability Zones you can deploy your workload. This gives Spot a better chance to find and allocate your required amount of compute capacity. For example, don't just ask for c5.large if you'd be willing to use larges from the c4, m5, and m4 families.
Depending on your specific needs, you can evaluate which instance types you can be flexible across to fulfill your compute requirements. If a workload can be vertically scaled, you should include larger instance types (more vCPUs and memory) in your requests. If you can only scale horizontally,

you should include older generation instance types because they are less in demand from On- Demand customers.
A good rule of thumb is to be flexible across at least 10 instance types for each workload. In addition, make sure that all Availability Zones are configured for use in your VPC and selected for your workload.
#### Use attribute-based instance type selection With attribute-based instance type selection, you can specify instance attributes—such as vCPUs, memory, and storage—for the workload you want to run. EC2 Auto Scaling or EC2 Fleet will then automatically identify and launch instances that match your specified attributes. This removes the effort required to manually select specific instance types, which requires an in-depth understanding of each instance type's offering.
Moreover, attribute-based instance type selection enables you to automatically use newly released instance types as they become available. This ensures seamless access to an increasingly broad range of Spot Instance capacity.
Attribute-based instance type selection is ideal for workloads and frameworks that can be flexible about the instance types they run on, such as High Performance Computing (HPC) and big data workloads.
For more information, see Create mixed instances group using attribute-based instance type selection in the Amazon EC2 Auto Scaling User Guide and Specify attributes for instance type selection for EC2 Fleet or Spot Fleet in this guide.
#### Use Spot placement scores to identify optimal Regions and Availability Zones Spot Instances are unused EC2 capacity, and this capacity fluctuates based on EC2 supply and demand. As a result, you might not always get the exact Spot capacity that you require in a specific location at a specific time. To mitigate this unpredictability, you can use the Spot placement score feature. This feature provides recommendations for Regions or Availability Zones that are more likely to have sufficient capacity to meet your Spot capacity needs without requiring you to launch Spot Instances in those locations first.
Spot placement score is best used for workloads that can be flexible about the instance types and the Region or Availability Zone they can use. All you need to do is specify the Spot capacity that you need, your instance type requirements, and whether you want a recommendations for Regions or Availability Zones. In return, you receive a score ranging from 1 to 10 for each Region

or Availability Zone, indicating the likelihood of successfully provisioning your requested Spot capacity in that location. A score of 10 indicates that your Spot request is highly likely to succeed.
It's important to note that a Spot placement score is a point-in-time recommendation, because capacity can vary over time. It does not guarantee available capacity or predict the risk of interruption.
You can use the Spot placement score feature in the Amazon EC2 console, AWS CLI, or an SDK. For more information, see Spot placement score.
#### Use EC2 Auto Scaling groups or EC2 Fleet to manage your aggregate capacity Spot enables you to think in terms of aggregate capacity—in units that include vCPUs, memory, storage, or network throughput—rather than thinking in terms of individual instances. Auto Scaling groups and EC2 Fleet enable you to launch and maintain a target capacity, and to automatically request resources to replace any that are disrupted or manually terminated. When you configure an Auto Scaling group or an EC2 Fleet, you need only specify the instance types and target capacity based on your application needs. For more information, see Auto Scaling groups in the Amazon EC2 Auto Scaling User Guide and Create an EC2 Fleet in this user guide.
#### Use the price and capacity optimized allocation strategy Allocation strategies in Auto Scaling groups help you to provision your target capacity without the need to manually look for the Spot capacity pools with spare capacity. We recommend using the price-capacity-optimized strategy because this strategy automatically provisions instances from the most-available Spot capacity pools that also have the lowest possible price. You can also take advantage of the price-capacity-optimized allocation strategy in EC2 Fleet.
Because your Spot Instance capacity is sourced from pools with optimal capacity, this decreases the possibility that your Spot Instances are reclaimed. For more information, see Allocation strategies for multiple instance types in the Amazon EC2 Auto Scaling User Guide and When workloads have a high cost of interruption in this user guide.
#### Use integrated AWS services to manage your Spot Instances Other AWS services integrate with Spot to reduce overall compute costs without the need to manage the individual instances or fleets. We recommend that you consider the following solutions for your applicable workloads: Amazon EMR, Amazon Elastic Container Service, AWS Batch, Amazon Elastic Kubernetes Service, Amazon SageMaker AI, AWS Elastic Beanstalk, and Amazon GameLift Servers. To learn more about Spot best practices with these services, see the Amazon EC2 Spot Instances Workshops Website.

#### Which is the best Spot request method to use?
Use the following table to determine which API to use when requesting Spot Instances.
API When to use?
Use case Should I use this API?
CreateAutoScalingG roup
- You need multiple instances with either a single configuration or a mixed  configurat ion.
- You want to automate the lifecycle managemen t through   a configurable API.
Create an Auto Scaling group that manages the lifecycle of your instances while  mai ntaining the desired number of instances.
Supports horizontal scaling (adding more instances) between specified minimum and  maximum limits.
Yes CreateFleet
- You need multiple instances with either a single configuration or a mixed  configurat ion.
- You want to self- manage your instance lifecycle.
- If you don't need auto scaling, we recommend that you  use an Create a fleet of both On-Demand Instances and Spot Instances in a single request, with multiple launch specifications that vary by instance type, AMI, Availabil ity  Zone, or subnet.
The Spot Instance allocation strategy defaults  to lowest- price  per unit, but you can change it to price-capacity- Yes – in instant mode if you don't need auto scaling

API When to use?
Use case Should I use this API? instant type fleet. optimized , capacity- optimized , or diversified .
RunInstances
- You're already using the RunInstances API to launch On- Demand Instances , and you simply want to  chan ge to launching Spot Instances by changing a single parameter.
- You do not need multiple instances with different instance types.
Launch a specified number of instances using an AMI and one instance type.
No – because RunInstances does not allow mixed instance types in a single  request

API When to use?
Use case Should I use this API?
RequestSpotFleet
- We strongly discourage using the RequestSp otFleet API because it is a legacy API with no planned   investme nt.
- If you want to manage your instance lifecycle , use the  Cre ateFleet API.
- If you don't want to manage your instance lifecycle, use the CreateAut oScalingGroup API.
DO NOT USE.
RequestSpotFleet is legacy API with no planned investment.
No RequestSpotInstanc es
- We strongly discourage using the RequestSp otInstances API because it is a legacy API  with no planned investmen t.
DO NOT USE.
RequestSpotInstances is legacy API with no planned investment.
No

### How Spot Instances work To launch a Spot Instance, either you create a Spot Instance request, or Amazon EC2 creates a Spot Instance request on your behalf. The Spot Instance launches when the Spot Instance request is fulfilled.
You can launch a Spot Instance using several different services. For more information, see Getting Started with Amazon EC2 Spot Instances. In this user guide, we describe the following ways to launch a Spot Instance using EC2:
- You can create a Spot Instance request by using the launch instance wizard in the Amazon EC2 console or the run-instances command. For more information, see Manage your Spot Instances.
- You can create an EC2 Fleet, in which you specify the desired number of Spot Instances. Amazon EC2 creates a Spot Instance request on your behalf for every Spot Instance that is specified in the EC2 Fleet. For more information, see Create an EC2 Fleet.
- You can create a Spot Fleet request, in which you specify the desired number of Spot Instances.
Amazon EC2 creates a Spot Instance request on your behalf for every Spot Instance that is specified in the Spot Fleet request. For more information, see Create a Spot Fleet.
Your Spot Instance launches if there is available capacity. Your Spot Instance runs until you stop or terminate it, or until Amazon EC2 interrupts it (known as a Spot Instance interruption). Amazon EC2 can stop, terminate, or hibernate a Spot Instance when it interrupts it.
When you use Spot Instances, you must be prepared for interruptions. Amazon EC2 can interrupt your Spot Instance when the demand for Spot Instances rises or when the supply of Spot Instances decreases. When Amazon EC2 interrupts a Spot Instance, it provides a Spot Instance interruption notice, which gives the instance a two-minute warning before Amazon EC2 interrupts it. You can't enable termination protection for Spot Instances. For more information, see Spot Instance interruptions.
Contents
- Spot Instance request states
- Launch Spot Instances in a launch group
- Launch Spot Instances in an Availability Zone group
- Launch Spot Instances in a VPC
- Launch burstable performance instances

- Launch on single-tenant hardware
#### Spot Instance request states A Spot Instance request can be in one of the following states:
- open – The request is waiting to be fulfilled.
- active – The request is fulfilled and has an associated Spot Instance.
- failed – The request has one or more bad parameters.
- closed – The Spot Instance was interrupted or terminated.
- disabled – You stopped the Spot Instance.
- cancelled – You canceled the request, or the request expired.
The following illustration represents the transitions between the request states. Notice that the transitions depend on the request type (one-time or persistent).

A one-time Spot Instance request remains active until Amazon EC2 launches the Spot Instance, the request expires, or you cancel the request. If capacity is not available, your Spot Instance is terminated and the Spot Instance request is closed.

A persistent Spot Instance request remains active until it expires or you cancel it, even if the request is fulfilled. If capacity is not available, your Spot Instance is interrupted. After your instance is interrupted, when capacity becomes available again, the Spot Instance is started if stopped or resumed if hibernated. You can stop a Spot Instance and start it again if capacity is available.
If the Spot Instance is terminated (irrespective of whether the Spot Instance is in a stopped or running state), the Spot Instance request is opened again and Amazon EC2 launches a new Spot Instance. For more information, see Stop a Spot Instance, Start a Spot Instance, and Terminate a Spot Instance.
You can track the status of your Spot Instance requests, as well as the status of the Spot Instances launched, through the status. For more information, see Get the status of a Spot Instance request.
#### Launch Spot Instances in a launch group Specify a launch group in your Spot Instance request to tell Amazon EC2 to launch a set of Spot Instances only if it can launch them all. In addition, if the Spot service must terminate one of the instances in a launch group, it must terminate them all. However, if you terminate one or more of the instances in a launch group, Amazon EC2 does not terminate the remaining instances in the launch group.
Although this option can be useful, adding this constraint can decrease the chances that your Spot Instance request is fulfilled and increase the chances that your Spot Instances are terminated. For example, your launch group includes instances in multiple Availability Zones. If capacity in one of these Availability Zones decreases and is no longer available, then Amazon EC2 terminates all instances for the launch group.
If you create another successful Spot Instance request that specifies the same (existing) launch group as an earlier successful request, then the new instances are added to the launch group.
Subsequently, if an instance in this launch group is terminated, all instances in the launch group are terminated, which includes instances launched by the first and second requests.
#### Launch Spot Instances in an Availability Zone group Specify an Availability Zone group in your Spot Instance request to tell Amazon EC2 to launch a set of Spot Instances in the same Availability Zone. Amazon EC2 need not interrupt all instances in an Availability Zone group at the same time. If Amazon EC2 must interrupt one of the instances in an Availability Zone group, the others remain running.
Although this option can be useful, adding this constraint can lower the chances that your Spot Instance request is fulfilled.

If you specify an Availability Zone group but don't specify an Availability Zone in the Spot Instance request, the result depends on the network you specified.
Default VPC Amazon EC2 uses the Availability Zone for the specified subnet. If you don't specify a subnet, it selects an Availability Zone and its default subnet, but not necessarily the lowest-priced zone. If you deleted the default subnet for an Availability Zone, then you must specify a different subnet.
Nondefault VPC Amazon EC2 uses the Availability Zone for the specified subnet.
#### Launch Spot Instances in a VPC You specify a subnet for your Spot Instances the same way that you specify a subnet for your On- Demand Instances.
- [Default VPC] If you want your Spot Instance launched in a specific low-priced Availability Zone, you must specify the corresponding subnet in your Spot Instance request. If you do not specify a subnet, Amazon EC2 selects one for you, and the Availability Zone for this subnet might not have the lowest Spot price.
- [Nondefault VPC] You must specify the subnet for your Spot Instance.
#### Launch burstable performance instances The T instance types are burstable performance instances. If you launch your Spot Instances using a burstable performance instance type, and if you plan to use your burstable performance Spot Instances immediately and for a short duration, with no idle time for accruing CPU credits, we recommend that you launch them in Standard mode to avoid paying higher costs. If you launch burstable performance Spot Instances in Unlimited mode and burst CPU immediately, you'll spend surplus credits for bursting. If you use the instance for a short duration, the instance doesn't have time to accrue CPU credits to pay down the surplus credits, and you are charged for the surplus credits when you terminate the instance.
Unlimited mode is suitable for burstable performance Spot Instances only if the instance runs long enough to accrue CPU credits for bursting. Otherwise, paying for surplus credits makes burstable performance Spot Instances more expensive than using other instances. For more information, see When to use unlimited mode versus fixed CPU.

T2 instances, when configured in Standard mode, get launch credits. T2 instances are the only burstable performance instances that get launch credits. Launch credits are meant to provide a productive initial launch experience for T2 instances by providing sufficient compute resources to configure the instance. Repeated launches of T2 instances to access new launch credits is not permitted. If you require sustained CPU, you can earn credits (by idling over some period), use Unlimited mode for T2 Spot Instances, or use an instance type with dedicated CPU.
#### Launch on single-tenant hardware You can run a Spot Instance on single-tenant hardware. Dedicated Spot Instances are physically isolated from instances that belong to other AWS accounts. For more information, see Amazon EC2 Dedicated Instances and the Amazon EC2 Dedicated Instances.
To run a Dedicated Spot Instance, do one of the following:
- Specify a tenancy of dedicated when you create the Spot Instance request. For more information, see Manage your Spot Instances.
- Request a Spot Instance in a VPC with an instance tenancy of dedicated. For more information, see Launch Dedicated Instances into a VPC with default tenancy. You can't request a Spot Instance with a tenancy of default if you request it in a VPC with an instance tenancy of dedicated.
All instance families support Dedicated Spot Instances except T instances. For each supported instance family, only the largest instance size or metal size supports Dedicated Spot Instances.
### View Spot Instance pricing history Spot Instance prices are set by Amazon EC2 and adjust gradually based on long-term trends in supply and demand for Spot Instance capacity.
When your Spot request is fulfilled, your Spot Instances launch at the current Spot price, not exceeding the On-Demand price. You can view the Spot price history for the last 90 days, filtering by instance type, operating system, and Availability Zone.
For the current Spot Instance prices, see Amazon EC2 Spot Instances Pricing.

Console To view the Spot price history
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Spot Requests.
3. Choose Pricing history.
4. For Graph, choose to compare the price history by Availability Zones or by Instance Types.
- If you choose Availability Zones, then choose the Instance type, operating system (Platform), and Date range for which to view the price history.
- If you choose Instance Types, then choose up to five Instance type(s), the Availability Zone, operating system (Platform), and Date range for which to view the price history.
The following screenshot shows a price comparison for different instance types.
5. Hover (move your pointer) over the graph to display the prices at specific times in the selected date range. The prices are displayed in the information blocks above the graph.
The price displayed in the top row shows the price on a specific date. The price displayed in the second row shows the average price over the selected date range.
6. To display the price per vCPU, toggle on Display normalized prices. To display the price for the instance type, toggle off Display normalized prices.

AWS CLI To view the Spot price history Use the following describe-spot-price-history command. aws ec2 describe-spot-price-history \ --instance-types c6i.xlarge \ --product-descriptions "Linux/UNIX" \ --start-time 2025-04-01T00:00:00 \ --end-time 2025-04-02T00:00:0 PowerShell To view the Spot price history Use the Get-EC2SpotPriceHistory cmdlet.
Get-EC2SpotPriceHistory `
    -InstanceType c6i.xlarge `
    -ProductDescription "Linux/UNIX" `
    -UtcStartTime 2025-04-01T00:00:00 `
    -UtcEndTime 2025-04-02T00:00:0
### Savings from purchasing Spot Instances You can view the usage and savings information for Spot Instances at the per-fleet level, or for all running Spot Instances. At the per-fleet level, the usage and savings information includes all instances launched and terminated by the fleet. You can view this information from the last hour or the last three days.
The following screenshot from the Savings section shows the Spot usage and savings information for a Spot Fleet.

You can view the following usage and savings information:
- Spot Instances – The number of Spot Instances launched and terminated by the Spot Fleet.
When viewing the savings summary, the number represents all your running Spot Instances.
- vCPU-hours – The number of vCPU hours used across all the Spot Instances for the selected time frame.
- Mem(GiB)-hours – The number of GiB hours used across all the Spot Instances for the selected time frame.
- On-Demand total – The total amount you would've paid for the selected time frame had you launched these instances as On-Demand Instances.
- Spot total – The total amount to pay for the selected time frame.
- Savings – The percentage that you are saving by not paying the On-Demand price.
- Average cost per vCPU-hour – The average hourly cost of using the vCPUs across all the Spot Instances for the selected time frame, calculated as follows: Average cost per vCPU-hour = Spot total / vCPU-hours.
- Average cost per mem(GiB)-hour – The average hourly cost of using the GiBs across all the Spot Instances for the selected time frame, calculated as follows: Average cost per mem(GiB)-hour = Spot total / Mem(GiB)-hours.

- Details table – The different instance types (the number of instances per instance type is in parentheses) that comprise the Spot Fleet. When viewing the savings summary, these comprise all your running Spot Instances.
Savings information can only be viewed using the Amazon EC2 console.
To view the savings information for a Spot Fleet
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. On the navigation pane, choose Spot Requests.
3. Select the ID of a Spot Fleet request and scroll to the Savings section.
Alternatively, select the checkbox next to the Spot Fleet request ID and choose the Savings tab.
4. By default, the page displays usage and savings information for the last three days. You can choose last hour or the last three days. For Spot Fleets that were launched less than an hour ago, the page shows the estimated savings for the hour.
To view the savings information for all running Spot Instances
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. On the navigation pane, choose Spot Requests.
3. Choose Savings summary.
### Create a Spot Instance request To use Spot Instances, you create a Spot Instance request that includes the desired number of instances, the instance type, and the Availability Zone. If capacity is available, Amazon EC2 fulfills your request immediately. Otherwise, Amazon EC2 waits until your request can be fulfilled or until you cancel the request.
You can use the launch instance wizard in the Amazon EC2 console or the run-instances command to request a Spot Instance in the same way that you can launch an On-Demand Instance. This method is only recommended for the following reasons:

- You're already using the launch instance wizard or run-instances command to launch On- Demand Instances, and you simply want to change to launching Spot Instances by changing a single parameter.
- You do not need multiple instances with different instance types.
This method is generally not recommended for launching Spot Instances because you can't specify multiple instance types, and you can't launch Spot Instances and On-Demand Instances in the same request. For the preferred methods for launching Spot Instances, which include launching a fleet that includes Spot Instances and On-Demand Instances with multiple instance types, see Which is the best Spot request method to use?
If you request multiple Spot Instances at one time, Amazon EC2 creates separate Spot Instance requests so that you can track the status of each request separately. For more information about tracking Spot Instance requests, see Get the status of a Spot Instance request.
Console To create a Spot Instance request Steps 1–9 are the same steps you'd use to launch an On-Demand Instance. At Step 10, you configure the Spot Instance request.
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation bar at the top of the screen, select a Region.
3. From the Amazon EC2 console dashboard, choose Launch instance.
4. (Optional) Under Name and tags, you can name your instance, and tag the Spot Instance request, the instance, the volumes, and the elastic graphics. For information about tags, see Tag your Amazon EC2 resources. a.
For Name, enter a descriptive name for your instance.
The instance name is a tag, where the key is Name, and the value is the name that you specify. If you don't specify a name, the instance can be identified by its ID, which is automatically generated when you launch the instance. b.
To tag the Spot Instance request, the instance, the volumes, and the elastic graphics, choose Add additional tags. Choose Add tag, and then enter a key and value, and select the resource type to tag. Choose Add tag again for each additional tag to add.

5. Under Application and OS Images (Amazon Machine Image), choose the operating system (OS) for your instance, and then select an AMI. For more information, see Application and OS Images (Amazon Machine Image).
6. Under Instance type, select the instance type that meets your requirements for the hardware configuration and size of your instance. For more information, see Instance type.
7. Under Key pair (login), choose an existing key pair, or choose Create new key pair to create a new one. For more information, see Amazon EC2 key pairs and Amazon EC2 instances.
Important If you choose the Proceed without key pair (Not recommended) option, you won't be able to connect to the instance unless you choose an AMI that is configured to allow users another way to log in.
8. Under Network settings, use the default settings, or choose Edit to configure the network settings as necessary.
Security groups form part of the network settings, and define firewall rules for your instance. These rules specify which incoming network traffic is delivered to your instance.
For more information, see Network settings.
9. The AMI you selected includes one or more volumes of storage, including the root device volume. Under Configure storage, you can specify additional volumes to attach to the instance by choosing Add new volume. For more information, see Configure storage.
10. Under Advanced details, configure the Spot Instance request as follows: a.
Under Purchasing option, select the Request Spot Instances checkbox. b.
You can either keep the default configuration for the Spot Instance request, or choose Customize (at the right) to specify custom settings for your Spot Instance request.
When you choose Customize, the following fields appear. i.
Maximum price: You can request Spot Instances at the Spot price, capped at the On-Demand price, or you can specify the maximum amount you're willing to pay.

Warning If you specify a maximum price, your instances will be interrupted more frequently than if you choose No maximum price.
If you specify a maximum price, it must be more than USD $0.001.
Specifying a value below USD $0.001 will result in a failed launch.
- No maximum price: Your Spot Instance will launch at the current Spot price.
The price will never exceed the On-Demand price. (Recommended)
- Set your maximum price (per instance/hour): You can specify the maximum amount you're willing pay.
- If you specify a maximum price that is less than the current Spot price, your Spot Instance will not launch.
- If you specify a maximum price that is more than the current Spot price, your Spot Instance will launch and be charged at the current Spot price. After your Spot Instance is running, if the Spot price rises above your maximum price, Amazon EC2 interrupts your Spot Instance.
- Regardless of the maximum price you specify, you will always be charged the current Spot price.
To review Spot price trends, see View Spot Instance pricing history. ii.
Request type: The Spot Instance request type that you choose determines what happens if your Spot Instance is interrupted.
- One-time: Amazon EC2 places a one-time request for your Spot Instance. If your Spot Instance is interrupted, the request is not resubmitted.
- Persistent request: Amazon EC2 places a persistent request for your Spot Instance. If your Spot Instance is interrupted, the request is resubmitted to replenish the interrupted Spot Instance.
If you do not specify a value, the default is a one-time request. iii.
Valid to: The expiration date of a persistent Spot Instance request.

This field is not supported for one-time requests. A one-time request remains active until all the instances in the request launch or you cancel the request.
- No request expiry date: The request remains active until you cancel it.
- Set your request expiry date: The persistent request remains active until the date that you specify, or until you cancel it. iv.
Interruption behavior: The behavior that you choose determines what happens when a Spot Instance is interrupted.
- For persistent requests, valid values are Stop and Hibernate. When an instance is stopped, charges for EBS volume storage apply.
Note Spot Instances now use the same hibernation functionality as On- Demand Instances. To enable hibernation, you can either choose Hibernate here, or you can choose Enable from the Stop - Hibernate behavior field, which appears lower down in the launch instance wizard.
For the hibernation prerequisites, see Prerequisites for EC2 instance hibernation.
- For one-time requests, only Terminate is valid.
If you do not specify a value, the default is Terminate, which is not valid for a persistent Spot Instance request. If you keep the default and try to launch a persistent Spot Instance request, you'll get an error.
For more information, see Behavior of Spot Instance interruptions.
11. On the Summary panel, for Number of instances, enter the number of instances to launch.
Note Amazon EC2 creates a separate request for each Spot Instance.
12. On the Summary panel, review the details of your instance, and make any necessary changes. After you submit your Spot Instance request, you can't change the parameters

of the request. You can navigate directly to a section in the launch instance wizard by choosing its link in the Summary panel. For more information, see Summary.
13. When you're ready to launch your instance, choose Launch instance.
If the instance fails to launch or the state immediately goes to terminated instead of running, see Troubleshoot Amazon EC2 instance launch issues.
AWS CLI To create a Spot Instance request using run-instances Use the run-instances command and specify the Spot Instance options in the --instance- market-options parameter as follows.
--instance-market-options file://spot-options.json The following is the data structure to specify in the JSON file. You can also specify ValidUntil and InstanceInterruptionBehavior. If you do not specify a field in the data structure, the default value is used.
The following example creates a persistent request.
{ "MarketType": "spot", "SpotOptions": { "SpotInstanceType": "persistent"
  } } To create a Spot Instance request using request-spot-instances Note We strongly discourage using the request-spot-instances command to request a Spot Instance because it is a legacy API with no planned investment. For more information, see Which is the best Spot request method to use?
Use the request-spot-instances command to create a one-time request.

aws ec2 request-spot-instances \ --instance-count 5 \ --type "one-time" \ --launch-specification file://specification.json Use the request-spot-instances command to create a persistent request. aws ec2 request-spot-instances \ --instance-count 5 \ --type "persistent" \ --launch-specification file://specification.json For example launch specification files to use with these commands, see Spot Instance request example launch specifications. If you download a launch specification file from the Spot Requests console, you must use the request-spot-fleet command instead (the Spot Requests console specifies a Spot Instance request using a Spot Fleet).
PowerShell To create a Spot Instance request Use the New-EC2Instance cmdlet and specify the Spot Instance options using the - InstanceMarketOption parameter.
-InstanceMarketOptions $marketOptions Create the data structure for the Spot Instance options as follows.
$spotOptions = New-Object Amazon.EC2.Model.SpotMarketOptions $spotOptions.SpotInstanceType="persistent"
$marketOptions = New-Object Amazon.EC2.Model.InstanceMarketOptionsRequest $marketOptions.MarketType = "spot"
$marketOptions.SpotOptions = $spotOptions
#### Spot Instance request example launch specifications The following examples show launch configurations that you can use with the request-spot- instances command to create a Spot Instance request. For more information, see Manage your Spot Instances.

Important We strongly discourage using the request-spot-instances command to request a Spot Instance because it is a legacy API with no planned investment. For more information, see Which is the best Spot request method to use?
Examples
- Example 1: Launch Spot Instances
- Example 2: Launch Spot Instances in the specified Availability Zone
- Example 3: Launch Spot Instances in the specified subnet
- Example 4: Launch a Dedicated Spot Instance
##### Example 1: Launch Spot Instances The following example does not include an Availability Zone or subnet. Amazon EC2 selects an Availability Zone for you. Amazon EC2 launches the instances in the default subnet of the selected Availability Zone.
{ "ImageId": "ami-0abcdef1234567890", "KeyName": "my-key-pair", "SecurityGroupIds": [ "sg-1a2b3c4d5e6f7g8h9" ], "InstanceType": "m5.medium", "IamInstanceProfile": { "Arn": "arn:aws:iam::123456789012:instance-profile/my-iam-role"
  } }
##### Example 2: Launch Spot Instances in the specified Availability Zone The following example includes an Availability Zone. Amazon EC2 launches the instances in the default subnet of the specified Availability Zone.
{ "ImageId": "ami-0abcdef1234567890", "KeyName": "my-key-pair", "SecurityGroupIds": [ "sg-1a2b3c4d5e6f7g8h9" ],

  "InstanceType": "m5.medium", "Placement": { "AvailabilityZone": "us-west-2a"
  }, "IamInstanceProfile": { "Arn": "arn:aws:iam::123456789012:instance-profile/my-iam-role"
  } }
##### Example 3: Launch Spot Instances in the specified subnet The following example includes a subnet. Amazon EC2 launches the instances in the specified subnet. If the VPC is a nondefault VPC, the instance does not receive a public IPv4 address by default.
{ "ImageId": "ami-0abcdef1234567890", "SecurityGroupIds": [ "sg-1a2b3c4d5e6f7g8h9" ], "InstanceType": "m5.medium", "SubnetId": "subnet-1a2b3c4d", "IamInstanceProfile": { "Arn": "arn:aws:iam::123456789012:instance-profile/my-iam-role"
  } } To assign a public IPv4 address to an instance in a nondefault VPC, specify the AssociatePublicIpAddress field as shown in the following example. When you specify a network interface, you must include the subnet ID and security group ID using the network interface, rather than using the SubnetId and SecurityGroupIds fields shown in the previous code block.
{ "ImageId": "ami-0abcdef1234567890", "KeyName": "my-key-pair", "InstanceType": "m5.medium", "NetworkInterfaces": [ { "DeviceIndex": 0, "SubnetId": "subnet-1a2b3c4d5e6f7g8h9", "Groups": [ "sg-1a2b3c4d5e6f7g8h9" ], "AssociatePublicIpAddress": true

    } ], "IamInstanceProfile": { "Arn": "arn:aws:iam::123456789012:instance-profile/my-iam-role"
  } }
##### Example 4: Launch a Dedicated Spot Instance The following example requests Spot Instance with a tenancy of dedicated. A Dedicated Spot Instance must be launched in a VPC.
{ "ImageId": "ami-0abcdef1234567890", "KeyName": "my-key-pair", "SecurityGroupIds": [ "sg-1a2b3c4d5e6f7g8h9" ], "InstanceType": "c5.8xlarge", "SubnetId": "subnet-1a2b3c4d5e6f7g8h9", "Placement": { "Tenancy": "dedicated"
  } }
### Get the status of a Spot Instance request To help you track your Spot Instance requests and plan your use of Spot Instances, use the request status provided by Amazon EC2. For example, the request status can provide the reason why your Spot request isn't fulfilled yet, or list the constraints that are preventing the fulfillment of your Spot request.
At each step of the process—also called the Spot request lifecycle—specific events determine successive request states.
The following illustration shows how Spot Instance requests work. Notice that the request type (one-time or persistent) determines whether the request is opened again when Amazon EC2 interrupts a Spot Instance or if you stop a Spot Instance. If the request is persistent, the request is opened again after your Spot Instance is interrupted. If the request is persistent and you stop your Spot Instance, the request only opens after you start your Spot Instance.

Contents
- Get request status information
- Spot request status codes
- EC2 Spot Instance Request Fulfillment event
- State changes for a Spot request
#### Get request status information You can get status information for your Spot Instance request.
Console To get request status information
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Spot Requests and select the Spot request.
3. To check the status, on the Description tab, check the Status field.

AWS CLI To get request status information Use the following describe-spot-instance-requests command. aws ec2 describe-spot-instance-requests --spot-instance-request- ids sir-0e54a519c9EXAMPLE PowerShell To get request status information Use the Get-EC2SpotInstanceRequest cmdlet.
Get-EC2SpotInstanceRequest -SpotInstanceRequestId sir-0e54a519c9EXAMPLE
#### Spot request status codes Spot request status information is composed of a status code, the update time, and a status message. Together, these help you determine the disposition of your Spot request.
The following are the Spot request status codes: az-group-constraint Amazon EC2 cannot launch all the instances you requested in the same Availability Zone. bad-parameters One or more parameters for your Spot request are not valid (for example, the AMI you specified does not exist). The status message indicates which parameter is not valid. canceled-before-fulfillment The user canceled the Spot request before it was fulfilled. capacity-not-available There is not enough capacity available for the instances that you requested. constraint-not-fulfillable The Spot request can't be fulfilled because one or more constraints are not valid (for example, the Availability Zone does not exist). The status message indicates which constraint is not valid.

fulfilled The Spot request is active, and Amazon EC2 is launching your Spot Instances. instance-stopped-by-price Your instance was stopped because the Spot price exceeded your maximum price. instance-stopped-by-user Your instance was stopped because a user stopped the instance or ran the shutdown command from the instance. instance-stopped-no-capacity Your instance was stopped due to EC2 capacity management needs. instance-terminated-by-price Your instance was terminated because the Spot price exceeded your maximum price. If your request is persistent, the process restarts, so your request is pending evaluation. instance-terminated-by-schedule Your Spot Instance was terminated at the end of its scheduled duration. instance-terminated-by-service Your instance was terminated from a stopped state. instance-terminated-by-user or spot-instance-terminated-by-user You terminated a Spot Instance that had been fulfilled, so the request state is closed (unless it's a persistent request) and the instance state is terminated. instance-terminated-launch-group-constraint One or more of the instances in your launch group was terminated, so the launch group constraint is no longer fulfilled. instance-terminated-no-capacity Your instance was terminated due to standard capacity management processes. launch-group-constraint Amazon EC2 cannot launch all the instances that you requested at the same time. All instances in a launch group are started and terminated together.

limit-exceeded The limit on the number of EBS volumes or total volume storage was exceeded. For more information, see Quotas for Amazon EBS in the Amazon EBS User Guide. marked-for-stop The Spot Instance is marked for stopping. marked-for-termination The Spot Instance is marked for termination. not-scheduled-yet The Spot request is not evaluated until the scheduled date. pending-evaluation After you make a Spot Instance request, it goes into the pending-evaluation state while the system evaluates the parameters of your request. pending-fulfillment Amazon EC2 is trying to provision your Spot Instances. placement-group-constraint The Spot request can't be fulfilled yet because a Spot Instance can't be added to the placement group at this time. price-too-low The request can't be fulfilled yet because your maximum price is below the Spot price. In this case, no instance is launched and your request remains open. request-canceled-and-instance-running You canceled the Spot request while the Spot Instances are still running. The request is cancelled, but the instances remain running. schedule-expired The Spot request expired because it was not fulfilled before the specified date. system-error There was an unexpected system error. If this is a recurring issue, please contact AWS Support for assistance.

#### EC2 Spot Instance Request Fulfillment event When a Spot Instance request is fulfilled, Amazon EC2 sends an EC2 Spot Instance Request Fulfillment event to Amazon EventBridge. You can create a rule to take an action whenever this event occurs, such as invoking a Lambda function or notifying an Amazon SNS topic.
The following is example data for this event.
{ "version": "0", "id": "01234567-1234-0123-1234-012345678901", "detail-type": "EC2 Spot Instance Request Fulfillment", "source": "aws.ec2", "account": "123456789012", "time": "yyyy-mm-ddThh:mm:ssZ", "region": "us-east-2", "resources": ["arn:aws:ec2:us-east-2:123456789012:instance/i-1234567890abcdef0"], "detail": { "spot-instance-request-id": "sir-0e54a519c9EXAMPLE", "instance-id": "i-1234567890abcdef0"
    } } For more information, see the Amazon EventBridge User Guide.
#### State changes for a Spot request The following diagram shows you the paths that your Spot request can follow throughout its lifecycle, from submission to termination. Each step is depicted as a node, and the status code for each node describes the status of the Spot request and Spot Instance.

Pending evaluation As soon as you create a Spot Instance request, it goes into the pending-evaluation state unless one or more request parameters are not valid (bad-parameters).

Status code Request state Instance state pending-evaluation open Not applicable bad-parameters closed Not applicable Holding If one or more request constraints are valid but can't be met yet, or if there is not enough capacity, the request goes into a holding state waiting for the constraints to be met. The request options affect the likelihood of the request being fulfilled. For example, if there is no capacity, your request stays in a holding state until there is available capacity. If you specify an Availability Zone group, the request stays in a holding state until the Availability Zone constraint is met.
In the event of an outage of one of the Availability Zones, there is a chance that the spare EC2 capacity available for Spot Instance requests in other Availability Zones can be affected.
Status code Request state Instance state capacity-not-avail able open Not applicable price-too-low open Not applicable not-scheduled-yet open Not applicable launch-group-const raint open Not applicable az-group-constraint open Not applicable placement-group-co nstraint open Not applicable constraint-not-ful fillable open Not applicable

Pending evaluation/fulfillment-terminal Your Spot Instance request can go to a terminal state if you create a request that is valid only during a specific time period and this time period expires before your request reaches the pending fulfillment phase. It might also happen if you cancel the request, or if a system error occurs.
Status code Request state Instance state schedule-expired cancelled Not applicable canceled-before-fu lfillment ¹ cancelled Not applicable bad-parameters failed Not applicable system-error closed Not applicable ¹ If you cancel the request.
Pending fulfillment When the constraints you specified (if any) are met, your Spot request goes into the pending- fulfillment state.
At this point, Amazon EC2 is getting ready to provision the instances that you requested. If the process stops at this point, it is likely to be because it was canceled by the user before a Spot Instance was launched. It might also be because an unexpected system error occurred.
Status code Request state Instance state pending-fulfillment open Not applicable Fulfilled When all the specifications for your Spot Instances are met, your Spot request is fulfilled. Amazon EC2 launches the Spot Instances, which can take a few minutes. If a Spot Instance is hibernated

or stopped when interrupted, it remains in this state until the request can be fulfilled again or the request is canceled.
Status code Request state Instance state fulfilled active pending → running fulfilled active stopped → running If you stop a Spot Instance, your Spot request goes into the marked-for-stop or instance- stopped-by-user state until the Spot Instance can be started again or the request is cancelled.
Status code Request state Instance state marked-for-stop active stopping instance-stopped-by- user ¹ disabled or cancelled  ² stopped ¹ A Spot Instance goes into the instance-stopped-by-user state if you stop the instance or run the shutdown command from the instance. After you've stopped the instance, you can start it again. On restart, the Spot Instance request returns to the pending-evaluation state and then Amazon EC2 launches a new Spot Instance when the constraints are met.
² The Spot request state is disabled if you stop the Spot Instance but do not cancel the request.
The request state is cancelled if your Spot Instance is stopped and the request expires.
Fulfilled-terminal Your Spot Instances continue to run as long as there is available capacity for your instance type, and you don't terminate the instance. If Amazon EC2 must terminate your Spot Instances, the Spot request goes into a terminal state. A request also goes into the terminal state if you cancel the Spot request or terminate the Spot Instances.

Status code Request state Instance state request-canceled-a nd-instance-running cancelled running marked-for-stop active running marked-for-termina tion active running instance-stopped-by- price disabled stopped instance-stopped-by- user disabled stopped instance-stopped-no- capacity disabled stopped instance-terminated- by-price closed (one-time), open (persistent) terminated instance-terminated- by-schedule closed terminated instance-terminated- by-service cancelled terminated instance-terminated- by-user closed or cancelled  ¹ terminated instance-terminated- no-capacity closed (one-time), open (persistent) running † instance-terminated- no-capacity closed (one-time), open (persistent) terminated

Status code Request state Instance state instance-terminate d-launch-group-con straint closed (one-time), open (persistent) terminated ¹ The request state is closed if you terminate the instance but do not cancel the request. The request state is cancelled if you terminate the instance and cancel the request. Even if you terminate a Spot Instance before you cancel its request, there might be a delay before Amazon EC2 detects that your Spot Instance was terminated. In this case, the request state can either be closed or cancelled.
† When Amazon EC2 interrupts a Spot Instance if it needs the capacity back and the instance is configured to terminate on interruption, the status is immediately set to instance-terminated- no-capacity (it is not set to marked-for-termination). However, the instance remains in the running state for 2 minutes to reflect the 2-minute period when the instance receives the Spot Instance interruption notice. After 2 minutes, the instance state is set to terminated.
Interruption experiments You can use AWS Fault Injection Service to initiate a Spot Instance interruption so that you can test how the applications on your Spot Instances respond. If AWS FIS stops a Spot Instance, your Spot request enters the marked-for-stop-by-experiment state and then the instance- stopped-by-experiment state. If AWS FIS terminates a Spot Instance, your Spot request enters the instance-terminated-by-experiment state. For more information, see the section called "Initiate an interruption".
Status code Request state Instance state marked-for-stop-by- experiment active running instance-stopped-by- experiment disabled stopped instance-terminated- by-experiment closed terminated

Persistent requests When your Spot Instances are terminated (either by you or Amazon EC2), if the Spot request is a persistent request, it returns to the pending-evaluation state and then Amazon EC2 can launch a new Spot Instance when the constraints are met.
### Tag Spot Instance requests To help categorize and manage your Spot Instance requests, you can tag them with custom metadata. You can assign a tag to a Spot Instance request when you create it, or afterward. You can assign tags using the Amazon EC2 console or a command line tool.
When you tag a Spot Instance request, the instances and volumes that are launched by the Spot Instance request are not automatically tagged. You need to explicitly tag the instances and volumes launched by the Spot Instance request. You can assign a tag to a Spot Instance and volumes during launch, or afterward.
For more information about how tags work, see Tag your Amazon EC2 resources.
Contents
- Prerequisites
- Tag a new Spot Instance request
- Tag an existing Spot Instance request
- View Spot Instance request tags
#### Prerequisites Grant the user the permission to tag resources. For more information about IAM policies and example policies, see Example: Tag resources.
The IAM policy you create is determined by which method you use for creating a Spot Instance request.
- If you use the launch instance wizard or run-instances to request Spot Instances, see To grant a user the permission to tag resources when using the launch instance wizard or run-instances.
- If you use the request-spot-instances command to request Spot Instances, see To grant a user the permission to tag resources when using request-spot-instances.

To grant a user the permission to tag resources when using the launch instance wizard or run- instances Create a IAM policy that includes the following:
- The ec2:RunInstances action. This grants the user permission to launch an instance.
- For Resource, specify spot-instances-request. This allows users to create Spot Instance requests, which request Spot Instances.
- The ec2:CreateTags action. This grants the user permission to create tags.
- For Resource, specify *. This allows users to tag all resources that are created during instance launch.
JSON { "Version":"2012-10-17", "Statement": [ { "Sid": "AllowLaunchInstances", "Effect": "Allow", "Action": [ "ec2:RunInstances"
            ], "Resource": [ "arn:aws:ec2:us-east-1::image/*", "arn:aws:ec2:us-east-1:*:subnet/*", "arn:aws:ec2:us-east-1:*:network-interface/*", "arn:aws:ec2:us-east-1:*:security-group/*", "arn:aws:ec2:us-east-1:*:key-pair/*", "arn:aws:ec2:us-east-1:*:volume/*", "arn:aws:ec2:us-east-1:*:instance/*", "arn:aws:ec2:us-east-1:*:spot-instances-request/*"
            ]
        }, { "Sid": "TagSpotInstanceRequests", "Effect": "Allow", "Action": "ec2:CreateTags", "Resource": "*"
        }

    ]
} When you use the RunInstances action to create Spot Instance requests and tag the Spot Instance requests on create, you need to be aware of how Amazon EC2 evaluates the spot-instances- request resource in the RunInstances statement it is evaluated in the IAM policy as follows:
- If you don't tag a Spot Instance request on create, Amazon EC2 does not evaluate the spot- instances-request resource in the RunInstances statement.
- If you tag a Spot Instance request on create, Amazon EC2 evaluates the spot-instances- request resource in the RunInstances statement.
Therefore, for the spot-instances-request resource, the following rules apply to the IAM policy:
- If you use RunInstances to create a Spot Instance request and you don't intend to tag the Spot Instance request on create, you don't need to explicitly allow the spot-instances-request resource; the call will succeed.
- If you use RunInstances to create a Spot Instance request and intend to tag the Spot Instance request on create, you must include the spot-instances-request resource in the RunInstances allow statement, otherwise the call will fail.
- If you use RunInstances to create a Spot Instance request and intend to tag the Spot Instance request on create, you must specify the spot-instances-request resource or include a * wildcard in the CreateTags allow statement, otherwise the call will fail.
For example IAM policies, including policies that are not supported for Spot Instance requests, see Work with Spot Instances.
To grant a user the permission to tag resources when using request-spot-instances Create a IAM policy that includes the following:
- The ec2:RequestSpotInstances action. This grants the user permission to create a Spot Instance request.
- The ec2:CreateTags action. This grants the user permission to create tags.

- For Resource, specify spot-instances-request. This allows users to tag only the Spot Instance request.
JSON { "Version":"2012-10-17", "Statement": [ { "Sid": "TagSpotInstanceRequest", "Effect": "Allow", "Action": [ "ec2:RequestSpotInstances", "ec2:CreateTags"
            ], "Resource": "arn:aws:ec2:us-east-1:111122223333:spot-instances- request/*"
        } ]
}
#### Tag a new Spot Instance request In the AWS CLI and PowerShell examples, configure the Spot Instance request as follows:
- For ResourceType, specify spot-instances-request. If you specify another value, the Spot Instance request will fail.
- For Tags, specify the key-value pair. You can specify more than one key-value pair.
Console To tag a new Spot Instance request
1. Follow the Manage your Spot Instances procedure.
2. To add a tag, on the Add Tags page, choose Add Tag, and enter the key and value for the tag. Choose Add another tag for each additional tag.

For each tag, you can tag the Spot Instance request, the Spot Instances, and the volumes with the same tag. To tag all three, ensure that Instances, Volumes, and Spot Instance Requests are selected. To tag only one or two, ensure that the resources you want to tag are selected, and the other resources are cleared.
3. Complete the required fields to create a Spot Instance request, and then choose Launch.
For more information, see Manage your Spot Instances.
AWS CLI To tag a new Spot Instance request Use the request-spot-instances command with the --tag-specification option.
The tag specification adds two tags to the Spot Instance request: Environment=Production and Cost-Center=123. aws ec2 request-spot-instances \ --instance-count 5 \ --type "one-time" \ --launch-specification file://specification.json \ --tag-specification 'ResourceType=spot-instances- request,Tags=[{Key=Environment,Value=Production},{Key=Cost-Center,Value=123}]'
PowerShell To tag a new Spot Instance request Use the Request-EC2SpotInstance cmdlet with the -TagSpecification parameter.
-TagSpecification $tagspec The tag specification is defined as follows. It adds two tags to the Spot Instance request:
Environment=Production and Cost-Center=123.
$tag1 = @{Key="Environment"; Value="Production"} $tag2 = @{Key="Cost-Center"; Value="123"} $tagspec = New-Object Amazon.EC2.Model.TagSpecification $tagspec.ResourceType = "spot-instances-request"
$tagspec.Tags = @($tag1,$tag2)

#### Tag an existing Spot Instance request Console To tag an existing Spot Instance request After you have created a Spot Instance request, you can add tags to the Spot Instance request using the console.
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Spot Requests.
3. Select your Spot Instance request.
4. Choose the Tags tab and choose Create Tag.
To tag an existing Spot Instance using the console After your Spot Instance request has launched your Spot Instance, you can add tags to the instance using the console. For more information, see Add tags using the console.
AWS CLI To tag an existing Spot Instance request or Spot Instance Use the create-tags command to tag existing resources. In the following example, the existing Spot Instance request and the Spot Instance are tagged with purpose=test. aws ec2 create-tags \ --resources sir-0e54a519c9EXAMPLE i-1234567890abcdef0 \ --tags Key=purpose,Value=test PowerShell To tag an existing Spot Instance request or Spot Instance Use the New-EC2Tag cmdlet. The following example adds the tag purpose=test to the existing Spot Instance request and the Spot Instance.
New-EC2Tag `
    -Resource sir-0e54a519c9EXAMPLE, i-1234567890abcdef0 `
    -Tag @{Key="purpose"; Value="test"}

#### View Spot Instance request tags Console To view Spot Instance request tags
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Spot Requests.
3. Select your Spot Instance request and choose the Tags tab.
AWS CLI To describe Spot Instance request tags Use the describe-spot-instance-requests command to view the configuration of the specified Spot Instance request, which includes any tags that were specified for the request. aws ec2 describe-spot-instance-requests \ --spot-instance-request-ids sir-0e54a519c9EXAMPLE \ --query "SpotInstanceRequests[*].Tags"
The following is example output.
[ [ { "Key": "Environment", "Value": "Production"
        }, { "Key": "Department", "Value": "101"
        } ]
]
PowerShell To describe Spot Instance request tags Use the Get-EC2SpotInstanceRequest cmdlet.

(Get-EC2SpotInstanceRequest `
    -SpotInstanceRequestId sir-0e54a519c9EXAMPLE).Tags The following is example output.
Key         Value ---         ----- Environment Production Department  101
### Cancel a Spot Instance request If you no longer want your Spot Instance request, you can cancel it. You can only cancel Spot Instance requests that are open, active, or disabled.
- Your Spot Instance request is open when your request has not yet been fulfilled and no instances have been launched.
- Your Spot Instance request is active when your request has been fulfilled and Spot Instances have launched as a result.
- Your Spot Instance request is disabled when you stop your Spot Instance.
If your Spot Instance request is active and has an associated running Spot Instance, canceling the request does not terminate the instance. For more information about terminating a Spot Instance, see Terminate a Spot Instance.
Console To cancel a Spot Instance request
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Spot Requests.
3. Select the Spot Instance request.
4. Choose Actions, Cancel request.
5. (Optional) If you are finished with the associated Spot Instances, you can terminate them.
In the Cancel Spot request dialog box, select Terminate instances, and then choose Confirm.

AWS CLI To cancel a Spot Instance request Use the following cancel-spot-instance-requests command. aws ec2 cancel-spot-instance-requests --spot-instance-request- ids sir-0e54a519c9EXAMPLE PowerShell To cancel a Spot Instance request Use the Stop-EC2SpotInstanceRequest cmdlet.
Stop-EC2SpotInstanceRequest -SpotInstanceRequestId sir-0e54a519c9EXAMPLE
### Manage your Spot Instances Amazon EC2 launches a Spot Instance when capacity is available. A Spot Instance runs until it is interrupted or you terminate it yourself.
Contents
- Find your Spot Instances
- Find instances launched by a specific request
- Stop a Spot Instance
- Start a Spot Instance
- Terminate a Spot Instance
#### Find your Spot Instances A Spot Instance appears in the Instances page in the console, along with On-Demand Instances.
Use the following procedure to find your Spot Instances.
Console To find your Spot Instances
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.

2. In the navigation pane, choose Instances.
3. To find all Spot Instances, in the search pane, choose Instance lifecycle=spot.
4. To verify that an instance is a Spot Instance, select the instance, choose the Details tab, and check the value of Lifecycle. The value for a Spot Instance is spot and the value for an On- Demand Instance is normal.
AWS CLI To find your Spot Instances Use the following describe-instances command. aws ec2 describe-instances --filters "Name=instance-lifecycle,Values=spot"
To determine whether an instance is a Spot Instance Use the following describe-instances command. aws ec2 describe-instances \ --instance-ids i-1234567890abcdef0 \ --query "Reservations[*].Instances[*].InstanceLifecycle" \ --output text If the output is spot, the instance is a Spot Instance. If there is no output, the instance is an On- Demand Instance.
PowerShell To find your Spot Instances Use the Get-EC2Instance cmdlet.
Get-EC2Instance -Filter @{Name="instance-lifecycle"; Values="spot"} To determine whether an instance is a Spot Instance Use the Get-EC2Instance cmdlet.
(Get-EC2Instance -InstanceId i-1234567890abcdef0).Instances.InstanceLifecycle

If the output is Spot, the instance is a Spot Instance. If there is no output, the instance is an On- Demand Instance.
#### Find instances launched by a specific request Use the following procedure to find the Spot Instances launched from a specific Spot Instance or Spot Fleet request.
Console To find the Spot Instances for a request
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Spot Requests. The list contains both Spot Instance requests and Spot Fleet requests.
3. If a Spot Instance request is fulfilled, Capacity is the ID of the Spot Instance. For a Spot Fleet, Capacity indicates how much of the requested capacity has been fulfilled. To view the IDs of the instances in a Spot Fleet, choose the expand arrow, or select the fleet and choose Instances.
4. For a Spot Fleet, Capacity indicates how much of the requested capacity is fulfilled. To view the IDs of the instances in a Spot Fleet, choose the fleet ID to open its details page and locate the Instances pane.
AWS CLI To find the Spot Instances for a request Use the following describe-spot-instance-requests command. aws ec2 describe-spot-instance-requests \ --spot-instance-request-ids sir-0e54a519c9EXAMPLE \ --query "SpotInstanceRequests[*].{ID:InstanceId}"
The following is example output:
[ { "ID": "i-1234567890abcdef0"

    }, { "ID": "i-0598c7d356eba48d7"
    } ]
PowerShell To find the Spot Instances for a request Use the Get-EC2SpotInstanceRequest cmdlet.
(Get-EC2SpotInstanceRequest -SpotInstanceRequestId sir-0e54a519c9EXAMPLE).InstanceId
#### Stop a Spot Instance If you don't need your Spot Instances now, but you want to restart them later without losing the data persisted in the Amazon EBS volume, you can stop them. The steps for stopping a Spot Instance are similar to the steps for stopping an On-Demand Instance.
Note While a Spot Instance is stopped, you can modify some of its instance attributes, but not the instance type.
We don't charge usage for a stopped Spot Instance, or data transfer fees, but we do charge for the storage for any Amazon EBS volumes.
#### Limitations
- You can only stop a Spot Instance if the Spot Instance was launched from a persistent Spot Instance request.
- You can't stop a Spot Instance if the associated Spot Instance request is cancelled. When the Spot Instance request is cancelled, you can only terminate the Spot Instance.
- You can't stop a Spot Instance if it is part of a fleet or launch group, or Availability Zone group.

Console To stop a Spot Instance
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Instances.
3. Select the Spot Instance. If you didn't save the instance ID of the Spot Instance, see the section called "Find your Spot Instances".
4. Choose Instance state, Stop instance.
5. When prompted for confirmation, choose Stop.
AWS CLI To stop a Spot Instance Use the stop-instances command to manually stop your Spot Instances. aws ec2 stop-instances --instance-ids i-1234567890abcdef0 PowerShell To stop a Spot Instance Use the Stop-EC2Instance cmdlet.
Stop-EC2Instance -InstanceId i-1234567890abcdef0
#### Start a Spot Instance You can start a Spot Instance that you previously stopped.
#### Prerequisites You can only start a Spot Instance if:
- You manually stopped the Spot Instance.
- The Spot Instance is an EBS-backed instance.
- Spot Instance capacity is available.
- The Spot price is lower than your maximum price.

#### Limitations
- You can't start a Spot Instance if it is part of fleet or launch group, or Availability Zone group.
The steps for starting a Spot Instance are similar to the steps for starting an On-Demand Instance.
Console To start a Spot Instance
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Instances.
3. Select the Spot Instance. If you didn't save the instance ID of the Spot Instance, see the section called "Find your Spot Instances".
4. Choose Instance state, Start instance.
AWS CLI To start a Spot Instance Use the start-instances command to manually start your Spot Instances. aws ec2 start-instances --instance-ids i-1234567890abcdef0 PowerShell To start a Spot Instance Use the Start-EC2Instance cmdlet.
Start-EC2Instance -InstanceId i-1234567890abcdef0
#### Terminate a Spot Instance Warning Terminating an instance is permanent and irreversible.

After you terminate an instance, you can no longer connect to it, and it can't be recovered.
All attached Amazon EBS volumes that are configured to be deleted on termination are also permanently deleted and can't be recovered. All data stored on instance store volumes is permanently lost. For more information, see How instance termination works.
Before you terminate an instance, ensure that you have backed up all data that you need to retain after the termination to persistent storage.
If you terminate a running or stopped Spot Instance that was launched by a persistent Spot Instance request, the Spot Instance request transitions to the open state so that a new Spot Instance can be launched. To ensure that no new Spot Instance is launched, you must first cancel the Spot Instance request.
If you cancel an active Spot Instance request that has a running Spot Instance, the running Spot Instance is not automatically terminated; you must manually terminate the Spot Instance.
If you cancel a disabled Spot Instance request that has a stopped Spot Instance, the stopped Spot Instance is automatically terminated by the Amazon EC2 Spot service. There might be a short lag between when you cancel the Spot Instance request and when the Spot service terminates the Spot Instance.
For more information, see Cancel a Spot Instance request.
Console To manually terminate a Spot Instance
1. Before you terminate an instance, verify that you won't lose any data by checking that your Amazon EBS volumes won't be deleted on termination and that you've copied any data that you need from your instance store volumes to persistent storage, such as Amazon EBS or Amazon S3.
2. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
3. In the navigation pane, choose Instances.
4. Select the Spot Instance. If you didn't save the instance ID of the Spot Instance, see the section called "Find your Spot Instances".
5. Choose Instance state, Terminate (delete) instance.
6. Choose Terminate (delete) when prompted for confirmation.

AWS CLI To manually terminate a Spot Instance Use the terminate-instances command to manually terminate your Spot Instances. aws ec2 terminate-instances --instance-ids i-1234567890abcdef0 i-0598c7d356eba48d7 PowerShell To manually terminate a Spot Instance Use the Remove-EC2Instance cmdlet.
Remove-EC2Instance -InstanceId i-1234567890abcdef0
### Spot Instance interruptions You can launch Spot Instances on spare EC2 capacity for steep discounts in exchange for returning them when Amazon EC2 needs the capacity back. When Amazon EC2 reclaims a Spot Instance, we call this event a Spot Instance interruption.
Demand for Spot Instances can vary significantly from moment to moment, and the availability of Spot Instances can also vary significantly depending on how many unused EC2 instances are available. It is always possible that your Spot Instance might be interrupted. The following are the possible reasons that Amazon EC2 might interrupt your Spot Instances:
Capacity Amazon EC2 can interrupt your Spot Instance when it needs it back. EC2 reclaims your instance mainly to repurpose capacity, but it can also occur for other reasons such as host maintenance or hardware decommission.
Price The Spot price is higher than your maximum price.
You can specify the maximum price in your Spot request. However, if you specify a maximum price, your instances will be interrupted more frequently than if you do not specify it.

Constraints If your Spot request includes a constraint such as a launch group or an Availability Zone group, the Spot Instances are terminated as a group when the constraint can no longer be met.
When Amazon EC2 interrupts a Spot Instance, it either terminates, stops, or hibernates the instance, depending on the interruption behavior that you specified when you created the Spot request.
Contents
- Behavior of Spot Instance interruptions
- Prepare for Spot Instance interruptions
- Initiate a Spot Instance interruption
- Spot Instance interruption notices
- Find interrupted Spot Instances
- Determine whether Amazon EC2 terminated a Spot Instance
- Billing for interrupted Spot Instances
#### Behavior of Spot Instance interruptions When you create a Spot request, you can specify the interruption behavior. The following are the possible interruption behaviors:
- Stop
- Hibernate
- Terminate The default behavior is that Amazon EC2 terminates Spot Instances when they are interrupted.
##### Stop interrupted Spot Instances You can specify that Amazon EC2 stops your Spot Instances when they are interrupted. The Spot Instance request type must be persistent. You can't specify a launch group in the Spot Instance request. For EC2 Fleet or Spot Fleet, the request type must be maintain.

#### Considerations
- Only Amazon EC2 can restart an interrupted stopped Spot Instance.
- For a Spot Instance launched by a persistent Spot Instance request: Amazon EC2 restarts the stopped instance when capacity is available in the same Availability Zone and for the same instance type as the stopped instance (the same launch specification must be used).
- While a Spot Instance is stopped, you can modify some of its instance attributes, but not the instance type. If you detach or delete an EBS volume, it is not attached when the Spot Instance is started. If you detach the root volume and Amazon EC2 attempts to start the Spot Instance, the instance will fail to start and Amazon EC2 will terminate the stopped instance.
- You can terminate a Spot Instance while it is stopped.
- If you cancel a Spot Instance request, an EC2 Fleet, or a Spot Fleet, Amazon EC2 terminates any associated Spot Instances that are stopped.
- While an interrupted Spot Instance is stopped, you are charged only for the EBS volumes, which are preserved. With EC2 Fleet and Spot Fleet, if you have many stopped instances, you can exceed the limit on the number of EBS volumes for your account. For more information about how you're charged when a Spot Instance is interrupted, see Billing for interrupted Spot Instances.
- Make sure that you are familiar with the implications of stopping an instance. For information about what happens when an instance is stopped, see Differences between instance states.
##### Hibernate interrupted Spot Instances You can specify that Amazon EC2 hibernates your Spot Instances when they are interrupted. For more information, see Hibernate your Amazon EC2 instance.
Amazon EC2 now offers the same hibernation experience for Spot Instances as is currently available for On-Demand Instances. It offers more extensive support, where the following is now supported for Spot Instance hibernation:
- More supported AMIs
- More supported instance families
- User-initiated hibernation

##### Terminate interrupted Spot Instances When Amazon EC2 interrupts a Spot Instance, it terminates the instance by default, unless you specify a different interruption behavior, such as stop or hibernate. For more information, see Terminate Amazon EC2 instances.
#### Prepare for Spot Instance interruptions Demand for Spot Instances can vary significantly from moment to moment, and the availability of Spot Instances can also vary significantly depending on how many unused EC2 instances are available. It is always possible that your Spot Instance might be interrupted. Therefore, you must ensure that your application is prepared for a Spot Instance interruption.
We recommend that you follow these best practices so that you're prepared for a Spot Instance interruption.
- Create your Spot request using an Auto Scaling group. If your Spot Instances are interrupted, the Auto Scaling group will automatically launch replacement instances. For more information, see Auto Scaling groups with multiple instance types and purchase options in the Amazon EC2 Auto Scaling User Guide.
- Ensure that your instance is ready to go as soon as the request is fulfilled by using an Amazon Machine Image (AMI) that contains the required software configuration. You can also use user data to run commands at startup.
- Data on instance store volumes is lost when the instance is stopped or terminated. Back up any important data on instance store volumes to a more persistent storage, such as Amazon S3, Amazon EBS, or Amazon DynamoDB.
- Store important data regularly in a place that isn't affected if the Spot Instance terminates. For example, you can use Amazon S3, Amazon EBS, or DynamoDB.
- Divide the work into small tasks (using a Grid, Hadoop, or queue-based architecture) or use checkpoints so that you can save your work frequently.
- Amazon EC2 emits a rebalance recommendation signal to the Spot Instance when the instance is at an elevated risk of interruption. You can rely on the rebalance recommendation to proactively manage Spot Instance interruptions without having to wait for the two-minute Spot Instance interruption notice. For more information, see EC2 instance rebalance recommendations.
- Use the two-minute Spot Instance interruption notices to monitor the status of your Spot Instances. For more information, see Spot Instance interruption notices.

- While we make every effort to provide these warnings as soon as possible, it is possible that your Spot Instance is interrupted before the warnings can be made available. Test your application to ensure that it handles an unexpected instance interruption gracefully, even if you are monitoring for rebalance recommendation signals and interruption notices. You can do this by running the application using an On-Demand Instance and then terminating the On-Demand Instance yourself.
- Run a controlled fault injection experiment with AWS Fault Injection Service to test how your application responds when your Spot Instance is interrupted. For more information, see the Tutorial: Test Spot Instance interruptions using AWS FIS in the AWS Fault Injection Service User Guide.
#### Initiate a Spot Instance interruption You can select a Spot Instance request or a Spot Fleet request in the Amazon EC2 console and initiate a Spot Instance interruption so that you can test how the applications on your Spot Instances handle being interrupted. When you initiate a Spot Instance interruption, Amazon EC2 notifies you that your Spot Instance will be interrupted in two minutes, and then, after two minutes, the instance is interrupted.
The underlying service that performs the Spot Instance interruption is AWS Fault Injection Service (AWS FIS). For information about AWS FIS, see AWS Fault Injection Service.
Note Interruption behaviors are terminate, stop, and hibernate. If you set the interruption behavior to hibernate, when you initiate a Spot Instance interruption, the hibernation process will begin immediately.
Initiating a Spot Instance interruption is supported in all AWS Regions except Asia Pacific (Jakarta), Asia Pacific (Osaka), China (Beijing), China (Ningxia), and Middle East (UAE).
Contents
- Initiate a Spot Instance interruption
- Verify the Spot Instance interruption
- Quotas

##### Initiate a Spot Instance interruption You can use the EC2 console to quickly initiate a Spot Instance interruption. When you select a Spot Instance request, you can initiate the interruption of one Spot Instance. When you select a Spot Fleet request, you can initiate the interruption of multiple Spot Instances at once.
For more advanced experiments to test Spot Instance interruptions, you can create your own experiments using the AWS FIS console.
To initiate the interruption of one Spot Instance in a Spot Instance request using the EC2 console
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. From the navigation pane, choose Spot Requests.
3. Select a Spot Instance request, and then choose Actions, Initiate interruption. You can't select multiple Spot Instance requests to initiate an interruption.
4. In the Initiate Spot Instance interruption dialog box, under Service access, either use the default role, or choose an existing role. To choose an existing role, choose Use an existing service role, and then, for IAM role, select the role to use.
5. When you're ready to initiate the Spot Instance interruption, choose Initiate interruption.
To initiate the interruption of one or more Spot Instances in a Spot Fleet request using the EC2 console
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. From the navigation pane, choose Spot Requests.
3. Select a Spot Fleet request, and then choose Actions, Initiate interruption. You can't select multiple Spot Fleet requests to initiate an interruption.
4. In the Specify number of Spot Instances dialog box, for Number of instances to interrupt, enter the number of Spot Instances to interrupt, and then choose Confirm.
Note The number can't exceed the number of Spot Instances in the fleet or your quota for the number of Spot Instances that AWS FIS can interrupt per experiment.

5. In the Initiate Spot Instance interruption dialog box, under Service access, either use the default role, or choose an existing role. To choose an existing role, choose Use an existing service role, and then, for IAM role, select the role to use.
6. When you're ready to initiate the Spot Instance interruption, choose Initiate interruption.
To create more advanced experiments to test Spot Instance interruptions using the AWS FIS console
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. From the navigation pane, choose Spot Requests.
3. Choose Actions, Create advanced experiments.
The AWS FIS console opens. For more information, see Tutorial: Test Spot Instance interruptions using AWS FIS in the AWS Fault Injection Service User Guide.
##### Verify the Spot Instance interruption After you initiate the interruption, the following occurs:
- The Spot Instance receives an instance rebalance recommendation.
- A Spot Instance interruption notice is issued two minutes before AWS FIS interrupts your instance.
- After two minutes, the Spot Instance is interrupted.
- A Spot Instance that was stopped by AWS FIS remains stopped until you restart it.
To verify that the instance was interrupted after you initiated the interruption
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. From the navigation pane, open Spot Requests and Instances in separate browser tabs or windows.
3. For Spot Requests, select the Spot Instance request or Spot Fleet request. The initial status is fulfilled. After the instance is interrupted, the status changes as follows, depending on the interruption behavior:
- terminate – The status changes to instance-terminated-by-experiment.

- stop – The status changes to marked-for-stop-by-experiment and then instance- stopped-by-experiment.
4. For Instances, select the Spot Instance. The initial status is Running. Two minutes after you receive the Spot Instance interruption notice, the status changes as follows, depending on the interruption behavior:
- stop – The status changes to Stopping and then Stopped.
- terminate – The status changes to Shutting-down and then Terminated.
##### Quotas Your AWS account has the following default quota for the number of Spot Instances that AWS FIS can interrupt per experiment.
Name Default Adjustable Description Target SpotInstances for  aws:ec2:send- spot-instance-inte rruptions Each supported Region: 5 Yes The maximum number of Spot Instances that  aws :ec2:send-spot-ins tance-interruptions can target when you identify targets using tags, per experiment.
You can request a quota increase. For more information, see Requesting a quota increase in the Service Quotas User Guide.
To view all the quotas for AWS FIS, open the Service Quotas console. In the navigation pane, choose AWS services and select AWS Fault Injection Service. You can also view all the quotas for AWS Fault Injection Service in the AWS Fault Injection Service User Guide.
#### Spot Instance interruption notices A Spot Instance interruption notice is a warning that is issued two minutes before Amazon EC2 stops or terminates your Spot Instance. If you specify hibernation as the interruption behavior,

you receive an interruption notice, but you do not receive a two-minute warning because the hibernation process begins immediately.
The best way for you to gracefully handle Spot Instance interruptions is to architect your application to be fault-tolerant. To accomplish this, you can take advantage of Spot Instance interruption notices. We recommend that you check for these interruption notices every 5 seconds.
The interruption notices are made available as an EventBridge event and as items in the instance metadata on the Spot Instance. Interruption notices are emitted on a best effort basis.
##### EC2 Spot Instance Interruption Warning event When Amazon EC2 is going to interrupt your Spot Instance, it emits an event two minutes prior to the actual interruption (except for hibernation, which gets the interruption notice, but not two minutes in advance, because hibernation begins immediately). This event can be detected by Amazon EventBridge. For more information about EventBridge events, see the Amazon EventBridge User Guide. For a detailed example that walks you through how to create and use event rules, see Taking Advantage of Amazon EC2 Spot Instance Interruption Notices.
The following is an example of the event for Spot Instance interruption. The possible values for instance-action are hibernate, stop, or terminate.
{ "version": "0", "id": "12345678-1234-1234-1234-123456789012", "detail-type": "EC2 Spot Instance Interruption Warning", "source": "aws.ec2", "account": "123456789012", "time": "yyyy-mm-ddThh:mm:ssZ", "region": "us-east-2", "resources": ["arn:aws:ec2:us-east-2a:instance/i-1234567890abcdef0"], "detail": { "instance-id": "i-1234567890abcdef0", "instance-action": "action"
    } } Note The ARN format of the Spot Instance interruption event is arn:aws:ec2:availability- zone:instance/instance-id. This format differs from the EC2 resource ARN format.

##### instance-action The instance-action item specifies the action and the approximate time, in UTC, when the action will occur.
If your Spot Instance is marked to be stopped or terminated by Amazon EC2, the instance- action item is present in your instance metadata. Otherwise, it is not present. You can retrieve the instance-action using Instance Metadata Service Version 2 (IMDSv2) as follows.
Linux TOKEN=`curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata- token-ttl-seconds: 21600"` \ && curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/ meta-data/spot/instance-action Windows [string]$token = Invoke-RestMethod `
    -Headers @{"X-aws-ec2-metadata-token-ttl-seconds" = "21600"} `
    -Method PUT -Uri http://169.254.169.254/latest/meta-data/spot/instance-action The following example output indicates the time at which this instance will be stopped.
{"action": "stop", "time": "2017-09-18T08:22:00Z"} The following example output indicates the time at which this instance will be terminated.
{"action": "terminate", "time": "2017-09-18T08:22:00Z"} If Amazon EC2 is not preparing to stop or terminate the instance, or if you terminated the instance yourself, instance-action is not present in the instance metadata and you receive an HTTP 404 error when you try to retrieve it.
##### termination-time The termination-time item specifies the approximate time in UTC when the instance will receive the shutdown signal.

Note This item is maintained for backward compatibility; you should use instance-action instead.
If your Spot Instance is marked for termination by Amazon EC2 (either due to a Spot Instance interruption where the interruption behavior is set to terminate, or due to the cancellation of a persistent Spot Instance request), the termination-time item is present in your instance metadata. Otherwise, it is not present. You can retrieve the termination-time using IMDSv2 as follows.
Linux TOKEN=`curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata- token-ttl-seconds: 21600"` if curl -H "X-aws-ec2-metadata-token: $TOKEN" -s http://169.254.169.254/latest/meta- data/spot/termination-time | grep -q .*T.*Z; then echo termination_scheduled; fi Windows [string]$token = Invoke-RestMethod -Headers @{"X-aws-ec2-metadata-token-ttl- seconds" = "21600"} -Method PUT -Uri http://169.254.169.254/latest/meta-data/spot/ termination-time The following is example output.
2015-01-05T18:02:00Z If Amazon EC2 is not preparing to terminate the instance (either because there is no Spot Instance interruption or because your interruption behavior is set to stop or hibernate), or if you terminated the Spot Instance yourself, the termination-time item is either not present in the instance metadata (so you receive an HTTP 404 error) or contains a value that is not a time value.
If Amazon EC2 fails to terminate the instance, the request status is set to fulfilled. The termination-time value remains in the instance metadata with the original approximate time, which is now in the past.

#### Find interrupted Spot Instances When you describe your EC2 instances, the results include your Spot Instances. The instance lifecycle of a Spot Instance is spot. The instance state of a Spot Instance is either stopped or terminated, depending on the interruption behavior that you configured. For a hibernated Spot Instance, the instance state is stopped.
For additional details about the reason for the interruption, check the Spot request status code. For more information, see the section called "Get the status of a Spot Instance request".
Console To find an interrupted Spot Instance
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Instances.
3. Apply the following filter: Instance lifecycle=spot.
4. Apply the Instance state=stopped or Instance state=terminated filter depending on the interruption behavior that you configured.
5. For each Spot Instance, on the Details tab, under Instance details, find State transition message. The following codes indicate that the Spot Instance was interrupted.
- Server.SpotInstanceShutdown
- Server.SpotInstanceTermination AWS CLI To find interrupted Spot Instances Use the describe-instances command with the --filters option. To list only the instance IDs in the output, include the --query option.
If the interruption behavior is to terminate the Spot Instances, use the following example: aws ec2 describe-instances \ --filters Name=instance-lifecycle,Values=spot \ Name=instance-state-name,Values=terminated \ Name=state-reason-code,Values=Server.SpotInstanceTermination \

    --query "Reservations[*].Instances[*].InstanceId"
If the interruption behavior is to stop the Spot Instances, use the following example: aws ec2 describe-instances \ --filters Name=instance-lifecycle,Values=spot \ Name=instance-state-name,Values=stopped \ Name=state-reason-code,Values=Server.SpotInstanceShutdown \ --query "Reservations[*].Instances[*].InstanceId"
PowerShell To find interrupted Spot Instances Use the Get-EC2Instance cmdlet.
If the interruption behavior is to terminate the Spot Instances, use the following example:
(Get-EC2Instance `
    -Filter @{Key="instance-lifecycle"; Values="spot"} `
            @{Key="instance-state-name"; Values="terminated"} `
            @{Key="state-reason-code"; Values="Server.SpotInstanceTermination"}).Instances.InstanceId If the interruption behavior is to stop the Spot Instances, use the following example:
(Get-EC2Instance `
    -Filter @{Key="instance-lifecycle"; Values="spot"} `
            @{Key="instance-state-name"; Values="stopped"} `
            @{Key="state-reason-code"; Values="Server.SpotInstanceTermination"}).Instances.InstanceId
#### Determine whether Amazon EC2 terminated a Spot Instance A Spot Instance runs until Amazon EC2 terminates it in response to a Spot Instance interruption, or until you terminate it yourself. For more information, see the section called "Interruption behavior".
After a Spot Instance is terminated, you can use AWS CloudTrail to see whether Amazon EC2 terminated it. If the CloudTrail log includes a BidEvictedEvent, this indicates that Amazon EC2

terminated the Spot Instance. If instead you see a TerminateInstances event, this indicates that a user terminated the Spot Instance.
Alternatively, if you want to receive notification that Amazon EC2 is going to interrupt your Spot Instance, use Amazon EventBridge to respond to the EC2 Spot Instance Interruption Warning event.
To view BidEvictedEvent events in CloudTrail
1. Open the CloudTrail console at https://console.aws.amazon.com/cloudtrail/.
2. In the navigation pane, choose Event history.
3. From the list of filters, choose Event name, and then in the filter field to the right, enter BidEvictedEvent.
4. (Optional) Select a time range.
5. If the list is not empty, choose BidEvictedEvent from the resulting entry to open its details page. You can find information about the Spot Instance in the Event record pane, including the ID of the Spot Instance. The following is an example of the event record.
{ "eventVersion": "1.05", "userIdentity": { "accountId": "123456789012", "invokedBy": "ec2.amazonaws.com"
    }, "eventTime": "2016-08-16T22:30:00Z", "eventSource": "ec2.amazonaws.com", "userAgent": "ec2.amazonaws.com", "sourceIPAddress": "ec2.amazonaws.com", "eventName": "BidEvictedEvent", "awsRegion": "us-east-2", "eventID": "d27a6096-807b-4bd0-8c20-a33a83375054", "eventType": "AwsServiceEvent", "recipientAccountId": "123456789012", "RequestParameters": null, "ResponseElements": null, "serviceEventDetails": { "instanceIdSet": [ "i-1eb2ac8eEXAMPLE"
        ]
    } }

6. If you did not find an entry for the BidEvictedEvent event, enter TerminateInstances as the event name. For more information about the event record for TerminateInstances, see the section called "Amazon EC2 API event examples".
#### Billing for interrupted Spot Instances When a Spot Instance is interrupted, you're charged for instance and EBS volume usage, and you might incur other charges, as follows.
##### Instance usage Who interrupts the Spot Instance Operating system Interrupted in the first hour Interrupted in any hour after the first hour Windows and Linux (excluding SUSE)
Charged for the seconds used Charged for the seconds used If you stop or terminate the Spot Instance SUSE Charged for the full hour even if you used a partial hour Charged for the full hours used, and charged a full hour for the  interrupted partial hour Windows and Linux (excluding SUSE)
No charge Charged for the seconds used If the Amazon EC2 interrupts the Spot Instance SUSE No charge Charged for the full hours used, but no charge for the  inter rupted partial hour
##### EBS volume usage While an interrupted Spot Instance is stopped, you are charged only for the EBS volumes, which are preserved.

With EC2 Fleet and Spot Fleet, if you have many stopped instances, you can exceed the limit on the number of EBS volumes for your account.
### EC2 instance rebalance recommendations An EC2 instance rebalance recommendation is a signal that notifies you when a Spot Instance is at elevated risk of interruption. The signal can arrive sooner than the two-minute Spot Instance interruption notice, giving you the opportunity to proactively manage the Spot Instance. You can decide to rebalance your workload to new or existing Spot Instances that are not at an elevated risk of interruption.
It is not always possible for Amazon EC2 to send the rebalance recommendation signal before the two-minute Spot Instance interruption notice. Therefore, the rebalance recommendation signal can arrive along with the two-minute interruption notice.
Rebalance recommendations are made available as a EventBridge event and as an item in the instance metadata on the Spot Instance. Events are emitted on a best effort basis.
Note Rebalance recommendations are only supported for Spot Instances that are launched after November 5, 2020 00:00 UTC.
Contents
- Rebalance actions you can take
- Monitor rebalance recommendation signals
- Services that use the rebalance recommendation signal
#### Rebalance actions you can take These are some of the possible rebalancing actions that you can take:
Graceful shutdown When you receive the rebalance recommendation signal for a Spot Instance, you can start your instance shutdown procedures, which might include ensuring that processes are completed before stopping them. For example, you can upload system or application logs to Amazon Simple Storage Service (Amazon S3), you can shut down Amazon SQS workers, or you can

complete deregistration from the Domain Name System (DNS). You can also save your work in external storage and resume it at a later time.
Prevent new work from being scheduled When you receive the rebalance recommendation signal for a Spot Instance, you can prevent new work from being scheduled on the instance, while continuing to use the instance until the scheduled work is completed.
Proactively launch new replacement instances You can configure Auto Scaling groups, EC2 Fleet, or Spot Fleet to automatically launch replacement Spot Instances when a rebalance recommendation signal is emitted. For more information, see Use Capacity Rebalancing to handle Amazon EC2 Spot interruptions in the Amazon EC2 Auto Scaling User Guide, and Use Capacity Rebalancing in EC2 Fleet and Spot Fleet to replace at-risk Spot Instances in this user guide.
#### Monitor rebalance recommendation signals You can monitor the rebalance recommendation signal so that, when it is emitted, you can take the actions that are specified in the preceding section. The rebalance recommendation signal is made available as an event that is sent to Amazon EventBridge (formerly known as Amazon CloudWatch Events) and as instance metadata on the Spot Instance.
Monitor rebalance recommendation signals:
- Use Amazon EventBridge
- Use instance metadata
##### Use Amazon EventBridge When the rebalance recommendation signal is emitted for a Spot Instance, the event for the signal is sent to Amazon EventBridge. If EventBridge detects an event pattern that matches a pattern defined in a rule, EventBridge invokes a target (or targets) specified in the rule.
The following is an example event for the rebalance recommendation signal.
{ "version": "0", "id": "12345678-1234-1234-1234-123456789012", "detail-type": "EC2 Instance Rebalance Recommendation", "source": "aws.ec2",

    "account": "123456789012", "time": "yyyy-mm-ddThh:mm:ssZ", "region": "us-east-2", "resources": ["arn:aws:ec2:us-east-2:123456789012:instance/i-1234567890abcdef0"], "detail": { "instance-id": "i-1234567890abcdef0"
    } } The following fields form the event pattern that is defined in the rule:
"detail-type": "EC2 Instance Rebalance Recommendation"
Identifies that the event is a rebalance recommendation event "source": "aws.ec2"
Identifies that the event is from Amazon EC2
###### Create an EventBridge rule You can write an EventBridge rule and automate what actions to take when the event pattern matches the rule.
The following example creates an EventBridge rule to send an email, text message, or mobile push notification every time Amazon EC2 emits a rebalance recommendation signal. The signal is emitted as an EC2 Instance Rebalance Recommendation event, which triggers the action defined by the rule.
Before creating the EventBridge rule, you must create the Amazon SNS topic for the email, text message, or mobile push notification.
To create an EventBridge rule for a rebalance recommendation event
1. Open the Amazon EventBridge console at https://console.aws.amazon.com/events/.
2. Choose Create rule.
3. For Define rule detail, do the following: a.
Enter a Name for the rule, and, optionally, a description.
A rule can't have the same name as another rule in the same Region and on the same event bus.

b.
For Event bus, choose default. When an AWS service in your account generates an event, it always goes to your account's default event bus. c.
For Rule type, choose Rule with an event pattern. d.
Choose Next.
4. For Build event pattern, do the following: a.
For Event source, choose AWS events or EventBridge partner events. b.
For Event pattern, for this example you'll specify the following event pattern to match the EC2 Instance Rebalance Recommendation event, and then choose Save.
{ "source": ["aws.ec2"], "detail-type": ["EC2 Instance Rebalance Recommendation"]
} To add the event pattern, you can either use a template by choosing Event pattern form, or specify your own pattern by choosing Custom pattern (JSON editor), as follows: i.
To use a template to create the event pattern, do the following:
A.
Choose Event pattern form.
B.
For Event source, choose AWS services.
C.
For AWS Service, choose EC2 Spot Fleet.
D.
For Event type, choose EC2 Instance Rebalance Recommendation.
E.
To customize the template, choose Edit pattern and make your changes to match the example event pattern. ii.
(Alternative) To specify a custom event pattern, do the following:
A.
Choose Custom pattern (JSON editor).
B.
In the Event pattern box, add the event pattern for this example. c.
Choose Next.
5. For Select target(s), do the following: a.
For Target types, choose AWS service. b.
For Select a target, choose SNS topic to send an email, text message, or mobile push notification when the event occurs.

c.
For Topic, choose an existing topic. You first need to create an Amazon SNS topic using the Amazon SNS console. For more information, see Using Amazon SNS for application- to-person (A2P) messaging in the Amazon Simple Notification Service Developer Guide. d.
(Optional) Under Additional settings, you can optionally configure additional settings. For more information, see Creating Amazon EventBridge rules that react to events (step 16) in the Amazon EventBridge User Guide. e.
Choose Next.
6. (Optional) For Tags, you can optionally assign one or more tags to your rule, and then choose Next.
7. For Review and create, do the following: a.
Review the details of the rule and modify them as necessary. b.
Choose Create rule.
For more information, see Amazon EventBridge rules and Amazon EventBridge event patterns in the Amazon EventBridge User Guide
##### Use instance metadata The instance metadata category events/recommendations/rebalance provides the approximate time, in UTC, when the rebalance recommendation signal was emitted for a Spot Instance.
We recommend that you check for rebalance recommendation signals every 5 seconds so that you don't miss an opportunity to act on the rebalance recommendation.
If a Spot Instance receives a rebalance recommendation, the time that the signal was emitted is present in the instance metadata. You can retrieve the time that the signal was emitted as follows.
IMDSv2 Linux Run the following command from your Linux instance.
IMDSv2 TOKEN=`curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata- token-ttl-seconds: 21600"` \

    && curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/ meta-data/events/recommendations/rebalance Windows Run the following cmdlet from your Windows instance [string]$token = Invoke-RestMethod `
    -Headers @{"X-aws-ec2-metadata-token-ttl-seconds" = "21600"} `
    -Method PUT -Uri http://169.254.169.254/latest/api/token Invoke-RestMethod `
    -Headers @{"X-aws-ec2-metadata-token" = $token} `
    -Method GET -Uri http://169.254.169.254/latest/meta-data/events/recommendations/ rebalance IMDSv1 Linux Run the following command from your Linux instance. curl http://169.254.169.254/latest/meta-data/events/recommendations/rebalance Windows Run the following cmdlet from your Windows instance.
Invoke-RestMethod -Uri http://169.254.169.254/latest/meta-data/events/ recommendations/rebalance The following is example output, which indicates the time, in UTC, that the rebalance recommendation signal was emitted for the Spot Instance.
{"noticeTime": "2020-10-27T08:22:00Z"} If the signal has not been emitted for the instance, events/recommendations/rebalance is not present and you receive an HTTP 404 error when you try to retrieve it.

#### Services that use the rebalance recommendation signal Amazon EC2 Auto Scaling, EC2 Fleet, and Spot Fleet use the rebalance recommendation signal to make it easy for you to maintain workload availability by proactively augmenting your fleet with a new Spot Instance before a running instance receives the two-minute Spot Instance interruption notice. You can have these services monitor and respond proactively to changes affecting the availability of your Spot Instances. For more information, see the following:
- Use Capacity Rebalancing to handle Amazon EC2 Spot interruptions in the Amazon EC2 Auto Scaling User Guide
- Use Capacity Rebalancing in EC2 Fleet and Spot Fleet to replace at-risk Spot Instances in the EC2 Fleet and Spot Fleet topic in this user guide
### Spot placement score The Spot placement score feature can recommend an AWS Region or Availability Zone based on your Spot capacity requirements. Spot capacity fluctuates, and you can't be sure that you'll always get the capacity that you need. A Spot placement score indicates how likely it is that a Spot request will succeed in a Region or Availability Zone.
Note A Spot placement score does not provide any guarantees in terms of available capacity or risk of interruption. A Spot placement score serves only as a recommendation.
Use cases You can use the Spot placement score feature for the following:
- To relocate and scale Spot compute capacity in a different Region, as needed, in response to increased capacity needs or decreased available capacity in the current Region.
- To identify the most optimal Availability Zone in which to run single-Availability Zone workloads.
- To simulate future Spot capacity needs so that you can pick an optimal Region for the expansion of your Spot-based workloads.
- To find an optimal combination of instance types to fulfill your Spot capacity needs.
Contents

- Limitations
- Costs
- How Spot placement score works
- Required permissions for Spot placement score
- Calculate the Spot placement score
##### Limitations
- Target capacity limit – Your Spot placement score target capacity limit is based on your recent Spot usage, while accounting for potential usage growth. If you have no recent Spot usage, we provide you with a low default limit aligned with your Spot request limit.
- Request configurations limit – We can limit the number of new request configurations within a 24-hour period if we detect patterns not associated with the intended use of the Spot placement score feature. If you reach the limit, you can retry the request configurations that you've already used, but you can't specify new request configurations until the next 24-hour period.
- Minimum number of instance types – If you specify instance types, you must specify at least three different instance types, otherwise Amazon EC2 will return a low Spot placement score.
Similarly, if you specify instance attributes, they must resolve to at least three different instance types. Instance types are considered different if they have a different name. For example, m5.8xlarge, m5a.8xlarge, and m5.12xlarge are all considered different.
#### Costs There is no additional charge for using the Spot placement score feature.
#### How Spot placement score works When you use the Spot placement score feature, you first specify your compute requirements for your Spot Instances, and then Amazon EC2 returns the top 10 Regions or Availability Zones where your Spot request is likely to succeed. Each Region or Availability Zone is scored on a scale from 1 to 10, with 10 indicating that your Spot request is highly likely to succeed, and 1 indicating that your Spot request is not likely to succeed.
To use the Spot placement score feature, follow these steps:
- Step 1: Specify your Spot requirements
- Step 2: Filter the Spot placement score response

- Step 3: Review the recommendations
- Step 4: Use the recommendations
##### Step 1: Specify your Spot requirements First, you specify your desired target Spot capacity and your compute requirements, as follows:
1. Specify the target Spot capacity, and optionally the target capacity unit.
You can specify your desired target Spot capacity in terms of the number of instances or vCPUs, or in terms of the amount of memory in MiB. To specify the target capacity in number of vCPUs or amount of memory, you must specify the target capacity unit as vcpu or memory-mib.
Otherwise, it defaults to number of instances.
By specifying your target capacity in terms of the number of vCPUs or the amount of memory, you can use these units when counting the total capacity. For example, if you want to use a mix of instances of different sizes, you can specify the target capacity as a total number of vCPUs.
The Spot placement score feature then considers each instance type in the request by its number of vCPUs, and counts the total number of vCPUs rather than the total number of instances when totaling up the target capacity.
For example, say you specify a total target capacity of 30 vCPUs, and your instance type list consists of c5.xlarge (4 vCPUs), m5.2xlarge (8 vCPUs), and r5.large (2 vCPUs). To achieve a total of 30 vCPUs, you could get a mix of 2 c5.xlarge (2*4 vCPUs), 2 m5.2xlarge (2*8 vCPUs), and 3 r5.large (3*2 vCPUs).
2. Specify instance types or instance attributes.
You can either specify the instance types to use, or you can specify the instance attributes that you need for your compute requirements, and then let Amazon EC2 identify the instance types that have those attributes. This is known as attribute-based instance type selection.
You can't specify both instance types and instance attributes in the same Spot placement score request.
If you specify instance types, you must specify at least three different instance types, otherwise Amazon EC2 will return a low Spot placement score. Similarly, if you specify instance attributes, they must resolve to at least three different instance types.

For examples of different ways to specify your Spot requirements, see Example configurations.
##### Step 2: Filter the Spot placement score response Amazon EC2 calculates the Spot placement score for each Region or Availability Zone, and returns either the top 10 Regions or the top 10 Availability Zones where your Spot request is likely to succeed. The default is to return a list of scored Regions. If you plan to launch all of your Spot capacity into a single Availability Zone, then it's useful to request a list of scored Availability Zones.
You can specify a Region filter to narrow down the Regions that will be returned in the response.
You can combine the Region filter and a request for scored Availability Zones. In this way, the scored Availability Zones are confined to the Regions for which you've filtered. To find the highest- scored Availability Zone in a Region, specify only that Region, and the response will return a scored list of all of the Availability Zones in that Region.
##### Step 3: Review the recommendations The Spot placement score for each Region or Availability Zone is calculated based on the target capacity, the composition of the instance types, the historical and current Spot usage trends, and the time of the request. Because Spot capacity is constantly fluctuating, the same Spot placement score request can yield different scores when calculated at different times.
Regions and Availability Zones are scored on a scale from 1 to 10. A score of 10 indicates that your Spot request is highly likely—but not guaranteed—to succeed. A score of 1 indicates that your Spot request is not likely to succeed at all. The same score might be returned for different Regions or Availability Zones.
If low scores are returned, you can edit your compute requirements and recalculate the score. You can also request Spot placement score recommendations for the same compute requirements at different times of the day.
##### Step 4: Use the recommendations A Spot placement score is only relevant if your Spot request has exactly the same configuration as the Spot placement score configuration (target capacity, target capacity unit, and instance types or instance attributes), and is configured to use the capacity-optimized allocation strategy.
Otherwise, the likelihood of getting available Spot capacity will not align with the score.
While a Spot placement score serves as a guideline, and no score guarantees that your Spot request will be fully or partially fulfilled, you can use the following information to get the best results:

- Use the same configuration – The Spot placement score is relevant only if the Spot request configuration (target capacity, target capacity unit, and instance types or instance attributes) in your Auto Scaling group, EC2 Fleet, or Spot Fleet is the same as what you entered to get the Spot placement score.
If you used attribute-based instance type selection in your Spot placement score request, you can use attribute-based instance type selection to configure your Auto Scaling group, EC2 Fleet, or Spot Fleet. For more information, see Create mixed instances group using attribute-based instance type selection and Specify attributes for instance type selection for EC2 Fleet or Spot Fleet.
Note If you specified your target capacity in terms of the number of vCPUs or the amount of memory, and you specified instance types in your Spot placement score configuration, note that you can't currently create this configuration in your Auto Scaling group, EC2 Fleet, or Spot Fleet. Instead, you must manually set the instance weighting by using the WeightedCapacity parameter.
- Use the capacity-optimized allocation strategy – Any score assumes that your fleet request will be configured to use all Availability Zones (for requesting capacity across Regions) or a single Availability Zone (if requesting capacity in one Availability Zone) and the capacity-optimized Spot allocation strategy for your request for Spot capacity to succeed. If you use other allocation strategies, such as lowest-price, the likelihood of getting available Spot capacity will not align with the score.
- Act on a score immediately – The Spot placement score recommendation reflects the available Spot capacity at the time of the request, and the same configuration can yield different scores when calculated at different times due to Spot capacity fluctuations. While a score of 10 means that your Spot capacity request is highly likely—but not guaranteed—to succeed, for best results we recommend that you act on a score immediately. We also recommend that you get a fresh score each time you attempt a capacity request.
#### Required permissions for Spot placement score By default, IAM identities (users, roles, or groups) don't have permission to use the section called "Spot placement score". To allow IAM identities to use Spot placement score, you must create an

IAM policy that grants permission to use the ec2:GetSpotPlacementScores EC2 API action. You then attach the policy to the IAM identities that require this permission.
The following is an example IAM policy that grants permission to use the ec2:GetSpotPlacementScores EC2 API action.
JSON { "Version":"2012-10-17", "Statement": [ { "Effect": "Allow", "Action": "ec2:GetSpotPlacementScores", "Resource": "*"
        } ]
} For information about editing an IAM policy, see Editing IAM policies in the IAM User Guide.
To provide access, add permissions to your users, groups, or roles:
- Users and groups in AWS IAM Identity Center:
Create a permission set. Follow the instructions in Create a permission set in the AWS IAM Identity Center User Guide.
- Users managed in IAM through an identity provider:
Create a role for identity federation. Follow the instructions in Create a role for a third-party identity provider (federation) in the IAM User Guide.
- IAM users:
- Create a role that your user can assume. Follow the instructions in Create a role for an IAM user in the IAM User Guide.
- (Not recommended) Attach a policy directly to a user or add a user to a user group. Follow the instructions in Adding permissions to a user (console) in the IAM User Guide.

#### Calculate the Spot placement score You can calculate a Spot placement score based on target capacity and compute requirements. For more information, see the section called "How Spot placement score works".
Required permissions Ensure that you have the required permissions. For more information, see the section called "Required permissions".
Options
- Calculate using instance attributes
- Calculate using instance types
- Calculate using the AWS CLI Looking for an automated solution? Instead of following the manual steps in this user guide, you can build a Spot placement score tracker dashboard that automatically captures and stores the scores in Amazon CloudWatch. For more information, see Guidance for Building a Spot Placement Score Tracker Dashboard on AWS.
##### Calculate using instance attributes To calculate a Spot placement score by specifying instance attributes
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Spot Requests.
3. Choose the down arrow next to Request Spot Instances and choose Calculate Spot Placement Score.
4. Choose Enter requirements.
5. For Target capacity, enter your desired capacity in terms of the number of instances or vCPUs, or the amount of memory (MiB).
6. For Instance type requirements, to specify your compute requirements and let Amazon EC2 identify the optimal instance types with these requirements, choose Specify instance attributes that match your compute requirements.
7. For vCPUs, enter the desired minimum and maximum number of vCPUs. To specify no limit, select No minimum, No maximum, or both.

8. For Memory (GiB), enter the desired minimum and maximum amount of memory. To specify no limit, select No minimum, No maximum, or both.
9. For CPU architecture, select the required instance architecture.
10. (Optional) For Additional instance attributes, you can optionally specify one or more attributes to express your compute requirements in more detail. Each additional attribute adds a further constraint to your request. You can omit the additional attributes; when omitted, the default values are used. For a description of each attribute and their default values, see get- spot-placement-scores.
11. (Optional) To view the instance types with your specified attributes, expand Preview matching instance types. To exclude instance types from being used in the placement evaluation, select the instances and then choose Exclude selected instance types.
12. Choose Load placement scores, and review the results.
13. (Optional) To display the Spot placement score for specific Regions, for Regions to evaluate, select the Regions to evaluate, and then choose Calculate placement scores.
14. (Optional) To display the Spot placement score for the Availability Zones in the displayed Regions, select the Provide placement scores per Availability Zone checkbox. A list of scored Availability Zones is useful if you want to launch all of your Spot capacity into a single Availability Zone.
15. (Optional) To edit your compute requirements and get a new placement score, choose Edit, make the necessary adjustments, and then choose Calculate placement scores.
##### Calculate using instance types To calculate a Spot placement score by specifying instance types
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Spot Requests.
3. Choose the down arrow next to Request Spot Instances and choose Calculate Spot Placement Score.
4. Choose Enter requirements.
5. For Target capacity, enter your desired capacity in terms of the number of instances or vCPUs, or the amount of memory (MiB).
6. For Instance type requirements, to specify the instance types to use, choose Manually select instance types.

7. Choose Select instance types, select the instance types to use, and then choose Select. To quickly find instance types, you can use the filter bar to filter the instance types by different properties.
8. Choose Load placement scores, and review the results.
9. (Optional) To display the Spot placement score for specific Regions, for Regions to evaluate, select the Regions to evaluate, and then choose Calculate placement scores.
10. (Optional) To display the Spot placement score for the Availability Zones in the displayed Regions, select the Provide placement scores per Availability Zone checkbox. A list of scored Availability Zones is useful if you want to launch all of your Spot capacity into a single Availability Zone.
11. (Optional) To edit the list of instance types and get a new placement score, choose Edit, make the necessary adjustments, and then choose Calculate placement scores.
##### Calculate using the AWS CLI To calculate the Spot placement score
1. (Optional) To generate all of the possible parameters that can be specified for the Spot placement score configuration, use the get-spot-placement-scores command and the -- generate-cli-skeleton parameter. aws ec2 get-spot-placement-scores \ --region us-east-1 \ --generate-cli-skeleton The following is example output.
{ "InstanceTypes": [ ""
    ], "TargetCapacity": 0, "TargetCapacityUnitType": "vcpu", "SingleAvailabilityZone": true, "RegionNames": [ ""
    ], "InstanceRequirementsWithMetadata": {

        "ArchitectureTypes": [ "x86_64_mac"
        ], "VirtualizationTypes": [ "hvm"
        ], "InstanceRequirements": { "VCpuCount": { "Min": 0, "Max": 0 }, "MemoryMiB": { "Min": 0, "Max": 0 }, "CpuManufacturers": [ "amd"
            ], "MemoryGiBPerVCpu": { "Min": 0.0, "Max": 0.0 }, "ExcludedInstanceTypes": [ ""
            ], "InstanceGenerations": [ "previous"
            ], "SpotMaxPricePercentageOverLowestPrice": 0, "OnDemandMaxPricePercentageOverLowestPrice": 0, "BareMetal": "excluded", "BurstablePerformance": "excluded", "RequireHibernateSupport": true, "NetworkInterfaceCount": { "Min": 0, "Max": 0 }, "LocalStorage": "included", "LocalStorageTypes": [ "hdd"
            ], "TotalLocalStorageGB": { "Min": 0.0, "Max": 0.0

            }, "BaselineEbsBandwidthMbps": { "Min": 0, "Max": 0 }, "AcceleratorTypes": [ "fpga"
            ], "AcceleratorCount": { "Min": 0, "Max": 0 }, "AcceleratorManufacturers": [ "amd"
            ], "AcceleratorNames": [ "vu9p"
            ], "AcceleratorTotalMemoryMiB": { "Min": 0, "Max": 0 } } }, "DryRun": true, "MaxResults": 0, "NextToken": ""
}
2. Create a JSON configuration file using the output from the previous step, and configure it as follows: a.
For TargetCapacity, enter your desired Spot capacity in terms of the number of instances or vCPUs, or the amount of memory (MiB). b.
For TargetCapacityUnitType, enter the unit for the target capacity. If you omit this parameter, it defaults to units.
Valid values: units (which translates to number of instances) | vcpu | memory-mib c.
For SingleAvailabilityZone, specify true for a response that returns a list of scored Availability Zones. A list of scored Availability Zones is useful if you want to launch all of your Spot capacity into a single Availability Zone. If you omit this parameter, it defaults to false, and the response returns a list of scored Regions.

d.
(Optional) For RegionNames, specify the Regions to use as a filter. You must specify the Region code, for example, us-east-1.
With a Region filter, the response returns only the Regions that you specify. If you specified true for SingleAvailabilityZone, the response returns only the Availability Zones in the specified Regions. e.
You can include either InstanceTypes or InstanceRequirements, but not both in the same configuration.
Specify one of the following in your JSON configuration:
- To specify a list of instance types, specify the instance types in the InstanceTypes parameter. Specify at least three different instance types. If you specify only one or two instance types, Spot placement score returns a low score. For the list of instance types, see Amazon EC2 Instance Types.
- To specify the instance attributes so that Amazon EC2 will identify the instance types that match those attributes, specify the attributes that are located in the InstanceRequirements structure.
You must provide values for VCpuCount, MemoryMiB, and CpuManufacturers.
You can omit the other attributes; when omitted, the default values are used. For a description of each attribute and their default values, see get-spot-placement-scores.
For example configurations, see Example configurations.
3. To get the Spot placement score for the requirements that you specified in the JSON file, use the get-spot-placement-scores command, and specify the name and path to your JSON file by using the --cli-input-json parameter. aws ec2 get-spot-placement-scores \ --region us-east-1 \ --cli-input-json file://file_name.json Example output if SingleAvailabilityZone is set to false or omitted (if omitted, it defaults to false) – a scored list of Regions is returned.
"SpotPlacementScores": [ {

        "Region": "us-east-1", "Score": 7 }, { "Region": "us-west-1", "Score": 5 }, ...
Example output if SingleAvailabilityZone is set to true – a scored list of Availability Zones is returned.
"SpotPlacementScores": [ { "Region": "us-east-1", "AvailabilityZoneId": "use1-az1", "Score": 8 }, { "Region": "us-east-1", "AvailabilityZoneId": "usw2-az3", "Score": 6 }, ...
###### Example configurations When using the AWS CLI, you can use the following example configurations.
Example configurations
- Example: Specify instance types and target capacity
- Example: Specify instance types, and target capacity in terms of memory
- Example: Specify attributes for attribute-based instance type selection
- Example: Specify attributes for attribute-based instance type selection and return a scored list of Availability Zones

###### Example: Specify instance types and target capacity The following example configuration specifies three different instance types and a target Spot capacity of 500 Spot Instances.
{ "InstanceTypes": [ "m5.4xlarge", "r5.2xlarge", "m4.4xlarge"
    ], "TargetCapacity": 500 }
###### Example: Specify instance types, and target capacity in terms of memory The following example configuration specifies three different instance types and a target Spot capacity of 500,000 MiB of memory, where the number of Spot Instances to launch must provide a total of 500,000 MiB of memory.
{ "InstanceTypes": [ "m5.4xlarge", "r5.2xlarge", "m4.4xlarge"
    ], "TargetCapacity": 500000, "TargetCapacityUnitType": "memory-mib"
}
###### Example: Specify attributes for attribute-based instance type selection The following example configuration is configured for attribute-based instance type selection, and is followed by a text explanation of the example configuration.
{ "TargetCapacity": 5000, "TargetCapacityUnitType": "vcpu", "InstanceRequirementsWithMetadata": { "ArchitectureTypes": ["arm64"], "VirtualizationTypes": ["hvm"],

        "InstanceRequirements": { "VCpuCount": { "Min": 1, "Max": 12 }, "MemoryMiB": { "Min": 512 } } } } InstanceRequirementsWithMetadata To use attribute-based instance type selection, you must include the InstanceRequirementsWithMetadata structure in your configuration, and specify the desired attributes for the Spot Instances.
In the preceding example, the following required instance attributes are specified:
- ArchitectureTypes – The architecture type of the instance types must be arm64.
- VirtualizationTypes – The virtualization type of the instance types must be hvm.
- VCpuCount – The instance types must have a minimum of 1 and a maximum of 12 vCPUs.
- MemoryMiB – The instance types must have a minimum of 512 MiB of memory. By omitting the Max parameter, you are indicating that there is no maximum limit.
Note that there are several other optional attributes that you can specify. For the list of attributes, see get-spot-placement-scores.
TargetCapacityUnitType The TargetCapacityUnitType parameter specifies the unit for the target capacity. In the example, the target capacity is 5000 and the target capacity unit type is vcpu, which together specify a desired target capacity of 5000 vCPUs, where the number of Spot Instances to launch must provide a total of 5000 vCPUs.

###### Example: Specify attributes for attribute-based instance type selection and return a scored list of Availability Zones of Availability Zones The following example configuration is configured for attribute-based instance type selection.
By specifying "SingleAvailabilityZone": true, the response will return a list of scored Availability Zones.
{ "TargetCapacity": 1000, "TargetCapacityUnitType": "vcpu", "SingleAvailabilityZone": true, "InstanceRequirementsWithMetadata": { "ArchitectureTypes": ["arm64"], "VirtualizationTypes": ["hvm"], "InstanceRequirements": { "VCpuCount": { "Min": 1, "Max": 12 }, "MemoryMiB": { "Min": 512 } } } }
### Track your Spot Instance costs using the Spot Instance data feed To help you understand the charges for your Spot Instances, Amazon EC2 provides a data feed that describes your Spot Instance usage and pricing. This data feed is sent to an Amazon S3 bucket that you specify when you subscribe to the data feed.
Data feed files arrive in your bucket typically once an hour. If you don't have a Spot Instance running during a certain hour, you don't receive a data feed file for that hour.
Each hour of Spot Instance usage is typically covered in a single data file. These files are compressed (gzip) before they are delivered to your bucket. Amazon EC2 can write multiple files for a given hour of usage where files are large (for example, when file contents for the hour exceed 50 MB before compression).

Note You can create only one Spot Instance data feed per AWS account.
Spot Instance data feed is supported in all AWS Regions except China (Beijing), China (Ningxia), AWS GovCloud (US), and the Regions that are disabled by default.
Contents
- Data feed file name and format
- Amazon S3 bucket requirements
- Subscribe to your Spot Instance data feed
- View the data in your data feed
- Delete your Spot Instance data feed
#### Data feed file name and format The Spot Instance data feed file name uses the following format (with the date and hour in UTC): bucket-name.s3.amazonaws.com/optional-prefix/aws-account-id.YYYY-MM-DD-HH.n.unique- id.gz For example, if your bucket name is amzn-s3-demo-bucket and your prefix is my-prefix, your file names are similar to the following: amzn-s3-demo-bucket.s3.amazonaws.com/my- prefix/111122223333.2023-12-09-07.001.b959dbc6.gz For more information about bucket names, see Bucket naming rules in the Amazon S3 User Guide.
The Spot Instance data feed files are tab-delimited. Each line in the data file corresponds to one instance hour and contains the fields listed in the following table.
Field Description Timestamp The timestamp used to determine the price charged for this  instance usage.

Field Description UsageType The type of usage and instance type being charged for. For   m1.small Spot Instances, this field is set to   SpotUsage . For all other instance types, this field is set to   SpotUsage: {instance-type}.  For example, SpotUsage :c1.medium .
 Operation The product being charged for. For Linux Spot Instances, this field is set to RunInstances . For Windows Spot Instances, this field  is set to RunInstances:0002 . Spot usage is grouped  according to Availability Zone.
 InstanceID The ID of the Spot Instance that generated this instance usage.
 MyBidID The ID for the Spot Instance request that generated this instance  usage.
 MyMaxPrice The maximum price specified for this Spot request.
 MarketPrice The Spot price at the time specified in the   Timestamp  field.
 Charge The price charged for this instance usage.
 Version The data feed version. The possible version is 1.0.
#### Amazon S3 bucket requirements When you subscribe to the data feed, you must specify an Amazon S3 bucket to store the data feed files.
Before you choose an Amazon S3 bucket for the data feed, consider the following:
- You must have FULL_CONTROL permission to the bucket. If you're the bucket owner, you have this permission by default. Otherwise, the bucket owner must grant your AWS account this permission.

- When you subscribe to a data feed, these permissions are used to update the bucket ACL to give the AWS data feed account FULL_CONTROL permission. The AWS data feed account writes data feed files to the bucket. If your account doesn't have the required permissions, the data feed files cannot be written to the bucket. For more information, see Logs sent to Amazon S3 in the Amazon CloudWatch Logs User Guide.
If you update the ACL and remove the permissions for the AWS data feed account, the data feed files cannot be written to the bucket. You must resubscribe to the data feed to receive the data feed files.
- Each data feed file has its own ACL (separate from the ACL for the bucket). The bucket owner has FULL_CONTROL permission to the data files. The AWS data feed account has read and write permissions.
- If you delete your data feed subscription, Amazon EC2 doesn't remove the read and write permissions for the AWS data feed account on either the bucket or the data files. You must remove these permissions yourself.
- If you encrypt your Amazon S3 bucket using server-side encryption with a AWS KMS key stored in AWS Key Management Service (SSE-KMS), you must use a customer managed key. For more information, see Amazon S3 bucket server-side encryption in the Amazon CloudWatch Logs User Guide.
#### Subscribe to your Spot Instance data feed You can subscribe to your Spot Instance data feed at any time. You can't complete this task using the Amazon EC2 console.
If you get an error that the bucket does not have enough permissions, see the following article for troubleshooting information: Troubleshoot the data feed for Spot Instances.
AWS CLI To subscribe to your data feed Use the create-spot-datafeed-subscription command.
To specify a bucket with a prefix, use the following example: aws ec2 create-spot-datafeed-subscription \ --bucket amzn-s3-demo-bucket \ --prefix my-prefix

To specify a bucket without a prefix, use the following example: aws ec2 create-spot-datafeed-subscription \ --bucket amzn-s3-demo-bucket PowerShell To subscribe to your data feed Use the New-EC2SpotDatafeedSubscription cmdlet.
To specify a bucket with a prefix, use the following example:
New-EC2SpotDatafeedSubscription `
    -Bucket amzn-s3-demo-bucket `
    -Prefix my-prefix To specify a bucket without a prefix, use the following example:
New-EC2SpotDatafeedSubscription `
    -Bucket amzn-s3-demo-bucket
#### View the data in your data feed In the AWS Management Console, open AWS CloudShell. Use the following s3 sync command to get the .gz files from the S3 bucket for your data feed and store them in the folder that you specify. aws s3 sync s3://amzn-s3-demo-bucket ./data-feed To display the contents of a .gz file, change to the folder where you stored the contents of the S3 bucket. cd data-feed Use the ls command to view the names of the files. Use the zcat command with the name of the file to display the contents of the compressed file. The following is an example command. zcat   111122223333.2023-12-09-07.001.b959dbc6.gz

The following is example output.
#Version: 1.0
#Fields: Timestamp UsageType Operation InstanceID MyBidID MyMaxPrice MarketPrice Charge Version 2023-12-09 07:13:47 UTC USE2-SpotUsage:c7a.medium       RunInstances:SV050 i-0c3e0c0b046e050df     sir-pwq6nmfp    0.0510000000 USD        0.0142000000 USD 0.0142000000 USD        1
#### Delete your Spot Instance data feed When you are finished with the Spot Instance data feed, you can delete it.
AWS CLI To delete your data feed Use the delete-spot-datafeed-subscription command. aws ec2 delete-spot-datafeed-subscription PowerShell To delete your data feed Use the Remove-EC2SpotDatafeedSubscription cmdlet.
Remove-EC2SpotDatafeedSubscription
### Service-linked role for Spot Instance requests Amazon EC2 uses service-linked roles for the permissions that it requires to call other AWS services on your behalf. A service-linked role is a unique type of IAM role that is linked directly to an AWS service. Service-linked roles provide a secure way to delegate permissions to AWS services because only the linked service can assume a service-linked role. For more information, see Service-linked roles in the IAM User Guide.
Amazon EC2 uses the service-linked role named AWSServiceRoleForEC2Spot to launch and manage Spot Instances on your behalf.

#### Permissions granted by AWSServiceRoleForEC2Spot Amazon EC2 uses AWSServiceRoleForEC2Spot to complete the following actions:
- ec2:DescribeInstances – Describe Spot Instances
- ec2:StopInstances – Stop Spot Instances
- ec2:StartInstances – Start Spot Instances
#### Create the service-linked role Under most circumstances, you don't need to manually create a service-linked role. Amazon EC2 creates the AWSServiceRoleForEC2Spot service-linked role the first time you request a Spot Instance using the console.
If you had an active Spot Instance request before October 2017, when Amazon EC2 began supporting this service-linked role, Amazon EC2 created the AWSServiceRoleForEC2Spot role in your AWS account. For more information, see A New Role Appeared in My Account in the IAM User Guide.
If you use the AWS CLI or an API to request a Spot Instance, you must first ensure that this role exists.
To create AWSServiceRoleForEC2Spot using the console
1. Open the IAM console at https://console.aws.amazon.com/iam/.
2. In the navigation pane, choose Roles.
3. Choose Create role.
4. On the Select type of trusted entity page, choose EC2, EC2 - Spot Instances, Next:
Permissions.
5. On the next page, choose Next:Review.
6. On the Review page, choose Create role.
To create AWSServiceRoleForEC2Spot using the AWS CLI Use the create-service-linked-role command as follows. aws iam create-service-linked-role --aws-service-name spot.amazonaws.com

If you no longer need to use Spot Instances, we recommend that you delete the AWSServiceRoleForEC2Spot role. After this role is deleted from your account, Amazon EC2 will create the role again if you request Spot Instances.
#### Grant access to customer managed keys for use with encrypted AMIs and EBS snapshots If you specify an encrypted AMI or an encrypted Amazon EBS snapshot for your Spot Instances and you use a customer managed key for encryption, you must grant the AWSServiceRoleForEC2Spot role permission to use the customer managed key so that Amazon EC2 can launch Spot Instances on your behalf. To do this, you must add a grant to the customer managed key, as shown in the following procedure.
When providing permissions, grants are an alternative to key policies. For more information, see Using Grants and Using Key Policies in AWS KMS in the AWS Key Management Service Developer Guide.
To grant the AWSServiceRoleForEC2Spot role permissions to use the customer managed key
- Use the create-grant command to add a grant to the customer managed key and to specify the principal (the AWSServiceRoleForEC2Spot service-linked role) that is given permission to perform the operations that the grant permits. The customer managed key is specified by the key-id parameter and the ARN of the customer managed key. The principal is specified by the grantee-principal parameter and the ARN of the AWSServiceRoleForEC2Spot service- linked role. aws kms create-grant \ --region us-east-1 \ --key-id arn:aws:kms:us- east-1:444455556666:key/1234abcd-12ab-34cd-56ef-1234567890ab \ --grantee-principal arn:aws:iam::111122223333:role/aws-service-role/ spot.amazonaws.com/AWSServiceRoleForEC2Spot \ --operations "Decrypt" "Encrypt" "GenerateDataKey"
 "GenerateDataKeyWithoutPlaintext" "CreateGrant" "DescribeKey" "ReEncryptFrom"
 "ReEncryptTo"
### Spot Instance quotas There are quotas for the number of running Spot Instances and pending Spot Instance requests per AWS account per Region. After a pending Spot Instance request is fulfilled, the request no longer counts towards the quota because the running instance is counted towards the quota.

Spot Instance quotas are managed in terms of the number of virtual central processing units (vCPUs) that your running Spot Instances are either using or will use pending the fulfillment of open Spot Instance requests. If you terminate your Spot Instances but do not cancel the Spot Instance requests, the requests count against your Spot Instance vCPU quota until Amazon EC2 detects the Spot Instance terminations and closes the requests.
We provide the following quota types for Spot Instances.
Name Default Adjustable All DL Spot Instance Requests 0 Yes All F Spot Instance Requests 0 Yes All G and VT Spot Instance Requests 0 Yes All Inf Spot Instance Requests 0 Yes All P Spot Instance Requests 0 Yes All Standard (A, C, D, H, I, M, R, T, Z) Spot Instance Requests 5 Yes All Trn Spot Instance Requests 0 Yes All X Spot Instance Requests 0 Yes Even though Amazon EC2 automatically adjusts your Spot Instance quotas based on your usage, you can request a quota increase if necessary. For example, if you intend to launch more Spot Instances than your current quota allows, you can request a quota increase. You can also request a quota increase if you submit a Spot Instance request and you receive the error Max spot instance count exceeded. To request a quota increase, use the Service Quotas console described in Amazon EC2 service quotas.
You can launch any combination of instance types that meet your changing application needs. For example, with an All Standard Spot Instance Requests quota of 256 vCPUs, you could request 32 m5.2xlarge Spot Instances (32 x 8 vCPUs) or 16 c5.4xlarge Spot Instances (16 x 16 vCPUs).

With Amazon CloudWatch metrics integration, you can monitor EC2 usage against your quotas. You can also configure alarms to warn about approaching quotas. For more information, see Service Quotas and Amazon CloudWatch alarms in the Service Quotas User Guide.
## Amazon EC2 Dedicated Hosts An Amazon EC2 Dedicated Host is a physical server that is fully dedicated for your use. You can optionally choose to share the instance capacity with other AWS accounts. For more information, see Cross-account Amazon EC2 Dedicated Host sharing.
Dedicated Hosts provide visibility and control over instance placement and they support host affinity. This means that you can launch and run instances on specific hosts, and you can ensure that instances run only on specific hosts. For more information, see Amazon EC2 Dedicated Host auto-placement and host affinity.
Dedicated Hosts provide comprehensive Bring Your Own License (BYOL) support. They allow you to use your existing per-socket, per-core, or per-VM software licenses, including Windows Server, SQL Server, SUSE Linux Enterprise Server, Red Hat Enterprise Linux, or other software licenses that are bound to VMs, sockets, or physical cores, subject to your license terms.
If you require your instances to run on dedicated hardware, but you do not need visibility or control over instance placement, and you do not need to use per-socket or per-core software licenses, you can consider using Dedicated Instances instead. Dedicated Instances and Dedicated Hosts can both be used to launch Amazon EC2 instances onto dedicated physical servers. There are no performance, security, or physical differences between Dedicated Instances and instances on Dedicated Hosts. However, there are some key differences between them. The following table highlights some of the key differences between Dedicated Instances and Dedicated Hosts:

Dedicated Host Dedicated Instance Dedicated physical server Physical server with instance capacity fully dedicated to your use.
Physical server that's dedicated to a single customer account.
Instance capacity sharing Can share instance capacity with other accounts.
Not supported
##### Billing Per-host billing Per-instance billing

Dedicated Host Dedicated Instance Visibility of sockets, cores, and host ID Provides visibility of the number of sockets and physical  cores No visibility Host and instance affinity Allows you to consistently deploy your instances to the same  physical server over time Not supported Targeted instance placement Provides additional visibility and control over how instances are placed on a physical server Not supported Automatic instance recovery Supported. For more information, see Amazon EC2 Dedicated Host recovery.
Supported Bring Your Own License (BYOL)
Supported Partial support * Capacity Reservations Not supported Supported
* Microsoft SQL Server with License Mobility through Software Assurance, and Windows Virtual Desktop Access (VDA) licenses can be used with Dedicated Instance.
For more information about Dedicated Instances, see Amazon EC2 Dedicated Instances.
### Dedicated Hosts restrictions Before you allocate Dedicated Hosts, take note of the following limitations and restrictions:
- To run RHEL and SUSE Linux on Dedicated Hosts, you must bring your own AMIs. You can't use the RHEL and SUSE Linux AMIs that are offered by AWS or that are available on AWS Marketplace with Dedicated Hosts. For more information about how to create your own AMI, see Bring your own software licenses to Amazon EC2 Dedicated Hosts.

This restriction does not apply to hosts allocated for high memory instances (u-6tb1.metal, u-9tb1.metal, u-12tb1.metal, u-18tb1.metal, and u-24tb1.metal). RHEL and SUSE Linux AMIs that are offered by AWS or that are available on AWS Marketplace can be used with these hosts.
- There is a limit on the number of running Dedicated Hosts per instance family per AWS account per Region. Quotas apply to running instances only. If your instance is pending, stopping, or stopped, it does not count towards your quota. To view the quotas for your account, or to request a quota increase, use the  Service Quotas console.
- Auto Scaling groups are supported when using a launch template that specifies a host resource group. For more information, see Create a launch template using advanced settings in the Amazon EC2 Auto Scaling User Guide.
- Amazon RDS instances are not supported.
- The AWS Free Usage tier is not available for Dedicated Hosts.
- Instance placement control refers to managing instance launches onto Dedicated Hosts. You can't launch Dedicated Hosts into placement groups.
- If you allocate a host for a virtualized instance type, you can't modify the instance type to a .metal instance type after the host is allocated. For example, if you allocate a host for the m5.large instance type, you can't modify the instance type to m5.metal.
Similarly, if you allocate a host for a .metal instance type, you can't modify the instance type to a virtualized instance type after the host is allocated. For example, if you allocate a host for the m5.metal instance type, you can't modify the instance type to m5.large.
Contents
- Amazon EC2 Dedicated Host pricing and billing
- Amazon EC2 Dedicated Host instance capacity configurations
- Burstable T3 instances on Amazon EC2 Dedicated Hosts
- Bring your own software licenses to Amazon EC2 Dedicated Hosts
- Amazon EC2 Dedicated Host auto-placement and host affinity
- Allocate an Amazon EC2 Dedicated Host for use in your account
- Launch Amazon EC2 instances on an Amazon EC2 Dedicated Host
- Launch Amazon EC2 instances into a host resource group
- Modify the auto-placement setting for an existing Amazon EC2 Dedicated Host

- Modify supported instance types for an existing Amazon EC2 Dedicated Host
- Modify Amazon EC2 Dedicated Host tenancy and affinity for an Amazon EC2 instance
- Release an Amazon EC2 Dedicated Host
- Migrate to Nitro-based Amazon EC2 Dedicated Hosts
- Purchase Dedicated Host Reservations for Dedicated Host billing discounts
- Cross-account Amazon EC2 Dedicated Host sharing
- Amazon EC2 Dedicated Hosts on AWS Outposts
- Amazon EC2 Dedicated Host recovery
- Host maintenance for Amazon EC2 Dedicated Host
- Monitor the state of your Amazon EC2 Dedicated Hosts
- Track Amazon EC2 Dedicated Host configuration changes using AWS Config
### Amazon EC2 Dedicated Host pricing and billing The price for a Dedicated Host varies by payment option.
Payment Options
- On-Demand Dedicated Hosts
- Dedicated Host Reservations
- Savings Plans
- Pricing for Windows Server on Dedicated Hosts
#### On-Demand Dedicated Hosts On-Demand billing is automatically activated when you allocate a Dedicated Host to your account.
The On-Demand price for a Dedicated Host varies by instance family and Region. You pay per second (with a minimum of 60 seconds) for active Dedicated Host, regardless of the quantity or the size of instances that you choose to launch on it. For more information about On-Demand pricing, see Amazon EC2 Dedicated Hosts On-Demand Pricing.
You can release an On-Demand Dedicated Host at any time to stop accruing charges for it. For information about releasing a Dedicated Host, see Release an Amazon EC2 Dedicated Host.

#### Dedicated Host Reservations Dedicated Host Reservations provide a billing discount compared to running On-Demand Dedicated Hosts. Reservations are available in three payment options:
- No Upfront—No Upfront Reservations provide you with a discount on your Dedicated Host usage over a term and do not require an upfront payment. Available in one-year and three-year terms. Only some instance families support the three-year term for No Upfront Reservations.
- Partial Upfront—A portion of the reservation must be paid upfront and the remaining hours in the term are billed at a discounted rate. Available in one-year and three-year terms.
- All Upfront—Provides the lowest effective price. Available in one-year and three-year terms and covers the entire cost of the term upfront, with no additional future charges.
You must have active Dedicated Hosts in your account before you can purchase reservations.
Each reservation can cover one or more hosts that support the same instance family in a single Availability Zone. Reservations are applied to the instance family on the host, not the instance size.
If you have three Dedicated Hosts with different instances sizes (m4.xlarge, m4.medium, and m4.large) you can associate a single m4 reservation with all those Dedicated Hosts. The instance family and Availability Zone of the reservation must match that of the Dedicated Hosts you want to associate it with.
When a reservation is associated with a Dedicated Host, the Dedicated Host can't be released until the reservation's term is over.
For more information about reservation pricing, see Amazon EC2 Dedicated Hosts Pricing.
#### Savings Plans Savings Plans are a flexible pricing model that offers significant savings over On-Demand Instances. With Savings Plans, you make a commitment to a consistent amount of usage, in USD per hour, for a term of one or three years. This provides you with the flexibility to use the Dedicated Hosts that best meet your needs and continue to save money, instead of making a commitment to a specific Dedicated Host. For more information, see the AWS Savings Plans User Guide.

Note Savings Plans are not supported with u-6tb1.metal, u-9tb1.metal, u-12tb1.metal, u-18tb1.metal, and u-24tb1.metal Dedicated Hosts.
#### Pricing for Windows Server on Dedicated Hosts Subject to Microsoft licensing terms, you can bring your existing Windows Server and SQL Server licenses to Dedicated Hosts. There is no additional charge for software usage if you choose to bring your own licenses.
In addition, you can also use Windows Server AMIs provided by Amazon to run the latest versions of Windows Server on Dedicated Hosts. This is common for scenarios where you have existing SQL Server licenses eligible to run on Dedicated Hosts, but need Windows Server to run the SQL Server workload. Windows Server AMIs provided by Amazon are supported on current generation instance types only. For more information, see Amazon EC2 Dedicated Hosts Pricing.
### Amazon EC2 Dedicated Host instance capacity configurations Dedicated Hosts support different configurations (physical cores, sockets, and VCPUs) that allow you to run instances of different families and sizes.
When you allocate a Dedicated Host in your account, you can choose a configuration that supports either a single instance type, or  multiple instance types within the same instance family. The number of instances that you can run on a host depends on the configuration you choose.
Contents
- Single instance type support
- Multiple instance type support
#### Single instance type support You can allocate a Dedicated Host that supports only one instance type. With this configuration, every instance that you launch on the Dedicated Host must be of the same instance type, which you specify when you allocate the host.
For example, you can allocate a host that supports only the m5.4xlarge instance type. In this case, you can run only m5.4xlarge instances on that host.

The number of instances that you can launch onto the host depends on the number of physical cores provided by the host, and the number of cores consumed by the specified instance type. For example, if you allocate a host for m5.4xlarge instances, the host provides 48 physical cores, and each m5.4xlarge instance consumes 8 physical cores. This means that you can launch up to 6 instances on that host (48 physical cores / 8 cores per instance = 6 instances).
#### Multiple instance type support You can allocate a Dedicated Host that supports multiple instance types within the same instance family. This allows you to run different instance types on the same host, as long as they're in the same instance family and the host has sufficient instance capacity.
For example, you can allocate a host that supports different instance types within the R5 instance family. In this case, you can launch certain combinations of R5 instance types, such as r5.large, r5.xlarge, r5.2xlarge, and r5.4xlarge, on that host, within the host's physical core capacity.
The following instance families support Dedicated Hosts with multiple instance type support:
- General purpose: A1 | M5 | M5n | M6i | M7i | T3
- Compute optimized: C5 | C5n | C6i | C7i
- Memory optimized: R5 | R5n | R6i | R7i The number of instances you can run on the host depends on the number of physical cores provided by the host, and the number of cores consumed by each instance type that you run on the host. For example, if you allocate an R5 host, which provides 48 physical cores, and you run two r5.2xlarge instances (4 cores x 2 instances) and three r5.4xlarge instances (8 cores x 3 instances), those instances consume a total of 32 cores, and you might be able to run certain combinations of R5 instances as long as they are within the remaining 16 cores.
However, for each instance family, there is a limit on the number of instances that can be run for each instance type. For example, an R5 Dedicated Host supports a maximum of 2 r5.8xlarge instances, which uses 32 of the physical cores. In this case, additional R5 instances of smaller types can then be used to fill the host to core capacity. For the supported number of instance types for each instance family, see the Dedicated Hosts Configuration Table.
The following table shows example instance type combinations:

Instance family Example instance type combinations R5
- Example 1: 4 x r5.4xlarge  + 4 x   r5.2xlarge
- Example 2: 1 x r5.12xlarge  + 1 x   r5.4xlarg e  + 1 x   r5.2xlarge  + 5 x r5.xlarge   + 2 x r5.large C5
- Example 1: 1 x c5.9xlarge  + 2 x   c5.4xlarge  + 1 x   c5.xlarge
- Example 2: 4 x c5.4xlarge  + 1 x   c5.xlarge  + 2 x   c5.large M5
- Example 1: 4 x m5.4xlarge  + 4 x   m5.2xlarge
- Example 2: 1 x m5.12xlarge  + 1 x   m5.4xlarg e  + 1 x   m5.2xlarge  + 5 x m5.xlarge   + 2 x m5.large
##### Considerations Keep the following in mind when working with Dedicated Hosts that support multiple instance types:
- Using multiple instance types on the same host is possible only within the same instance family.
- When mixing instance types, to maximize host utilization, we recommend launching larger instance types first followed by smaller instance types.
- Depending on the combination and launch order of the instance types on a Dedicated Host, it may not be physically possible to maximize the utilization of the host. When mixing instance types on a host, some capacity might be available on the host but not usable. For example, you might see 16 vCPUs available on an r5n host but may not be able to launch a 4xlarge instance on the host even though r5n.4xlarge runs on 16 vCPUs.

Note If you enable an A1 Dedicated Host for multiple instance types, you can launch only a mix of a1.xlarge and a1.2xlarge instances on that host. If you launch an a1.medium or a1.large instance on that host, you will be restricted to launching only more of that same instance type on the host. A single a1.4xlarge instance consumes all capacity on the host. If you require a host for either a1.medium or a1.large instances, we recommend that you allocate separate hosts for those instance types.
### Burstable T3 instances on Amazon EC2 Dedicated Hosts Dedicated Hosts support burstable performance T3 instances. T3 instances provide a cost-efficient way of using your eligible BYOL license software on dedicated hardware. The smaller vCPU footprint of T3 instances enables you to consolidate your workloads on fewer hosts and maximize your per-core license utilization.
T3 Dedicated Hosts are best suited for running BYOL software with low to moderate CPU utilization. This includes eligible per-socket, per-core, or per-VM software licenses, such as Windows Server, Windows Desktop, SQL Server, SUSE Enterprise Linux Server, Red Hat Enterprise Linux, and Oracle Database. Examples of workloads suited for T3 Dedicated Hosts are small and medium databases, virtual desktops, development and test environments, code repositories, and product prototypes. T3 Dedicated Hosts are not recommended for workloads with sustained high CPU utilization or for workloads that experience correlated CPU bursts simultaneously.
T3 instances on Dedicated Hosts use the same credit model as T3 instances on shared tenancy hardware. However, they support the standard credit mode only; they do not support the unlimited credit mode. In standard mode, T3 instances on Dedicated Hosts earn, spend, and accrue credits in the same way as burstable instances on shared tenancy hardware. They provide a baseline CPU performance with the ability to burst above the baseline level. To burst above the baseline, the instance spends credits that it has accrued in its CPU credit balance. When the accrued credits are depleted, CPU utilization is lowered to the baseline level. For more information about standard mode, see How standard burstable performance instances work.
T3 Dedicated Hosts support all of the features offered by Amazon EC2 Dedicated Hosts, including multiple instance sizes on a single host, Host resource groups, and BYOL.
Supported T3 instance sizes and configurations

T3 Dedicated Hosts run general purpose burstable T3 instances that share CPU resources of the host by providing a baseline CPU performance and the ability to burst to a higher level when needed. This enables T3 Dedicated Hosts, which have 48 cores, to support up to a maximum of 192 instances per host. In order to efficiently utilize the host's resources and to provide the best instance performance, the Amazon EC2 instance placement algorithm automatically calculates the supported number of instances and instance size combinations that can be launched on the host.
T3 Dedicated Hosts support multiple instance types on the same host. All T3 instance sizes are supported on Dedicated Hosts. You can run different combinations of T3 instances up to the CPU limit of the host.
The following table lists the supported instance types, summarizes the performance of each instance type, and indicates the maximum number of instances of each size that can be launched.
Instance type vCPUs Memory (GiB)
Baseline CPU utilization per vCPU Network burst bandwidth (Gbps)
Amazon EBS burst bandwidth (Mbps)
Max number of instances per Dedicated Host t3.nano 2 0.5 5% 5 Up to 2,085 192 t3.micro 2 1 10% 5 Up to 2,085 192 t3.small 2 2 20% 5 Up to 2,085 192 t3.medium 2 4 20% 5 Up to 2,085 192 t3.large 2 8 30% 5 2,780 96 t3.xlarge 4 16 40% 5 2,780 48 t3.2xlarg e 8 32 40% 5 2,780 24 Monitor CPU utilization for T3 Dedicated Hosts You can use the DedicatedHostCPUUtilization Amazon CloudWatch metric to monitor the vCPU utilization of a Dedicated Host. The metric is available in the EC2 namespace and Per-Host- Metrics dimension. For more information, see Dedicated Host metrics.

### Bring your own software licenses to Amazon EC2 Dedicated Hosts Dedicated Hosts allow you to use your existing per-socket, per-core, or per-VM software licenses.
When you bring your own license, you are responsible for managing your own licenses. However, Amazon EC2 has features that help you maintain license compliance, such as instance affinity and targeted placement.
These are the general steps to follow in order to bring your own volume licensed machine image into Amazon EC2.
1. Verify that the license terms controlling the use of your machine images allow usage in a virtualized cloud environment. For more information about Microsoft Licensing, see Amazon Web Services and Microsoft Licensing.
2. After you have verified that your machine image can be used within Amazon EC2, import it using VM Import/Export. For information about how to import your machine image, see the VM Import/Export User Guide.
3. After you import your machine image, you can launch instances from it onto active Dedicated Hosts in your account.
4. When you run these instances, depending on the operating system, you might be required to activate these instances against your own KMS server (for example, Windows Server or Windows SQL Server). You can't activate your imported Windows AMI against the Amazon Windows KMS server.
Note To track how your images are used in AWS, enable host recording in AWS Config. You can use AWS Config to record configuration changes to a Dedicated Host and use the output as a data source for license reporting. For more information, see Track Amazon EC2 Dedicated Host configuration changes using AWS Config.
### Amazon EC2 Dedicated Host auto-placement and host affinity Placement control for Dedicated Hosts happens on both the instance level and host level.

#### Auto-placement Auto-placement is configured at the host level. It allows you to manage whether instances that you launch are launched onto a specific host, or onto any available host that has matching configurations.
When auto-placement is disabled for a Dedicated Host, it accepts only host tenancy instance launches that specify its unique host ID. This is the default setting for new Dedicated Hosts.
When auto-placement is enabled for a Dedicated Host, it accepts any untargeted, host tenancy instance launches that match its instance type configuration.
When launching an instance, you need to configure its tenancy. Launching an instance onto a Dedicated Host without providing a specific HostId enables it to launch on any Dedicated Host that has auto-placement enabled and that matches its instance type.
#### Host affinity Host affinity is configured at the instance level. It establishes a launch relationship between an instance and a Dedicated Host.
When affinity is set to Host, an instance launched onto a specific host always restarts on the same host if stopped. This applies to both targeted and untargeted launches.
When affinity is set to Default, and you stop and restart the instance, it can be restarted on any available host. However, it tries to launch back onto the last Dedicated Host on which it ran (on a best-effort basis).
### Allocate an Amazon EC2 Dedicated Host for use in your account To begin using a Dedicated Host, you must first allocate it in your account. After you allocate the Dedicated Host, the Dedicated Host capacity is made available in your account immediately and you can start launching instances onto the Dedicated Host.
When you allocate a Dedicated Host in your account, you can choose a configuration that supports either a single instance type, or  multiple instance types within the same instance family. The number of instances that you can run on the host depends on the configuration you choose. For more information see Amazon EC2 Dedicated Host instance capacity configurations.

Console To allocate a Dedicated Host
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Dedicated Hosts and then choose Allocate Dedicated Host.
3. For Instance family, choose the instance family for the Dedicated Host.
4. Specify whether the Dedicated Host supports multiple instance sizes within the selected instance family, or a specific instance type only. Do one of the following.
- To configure the Dedicated Host to support multiple instance types in the selected instance family, for Support multiple instance types, choose Enable. Enabling this allows you to launch different instance sizes from the same instance family onto the Dedicated Host. For example, if you choose the m5 instance family and choose this option, you can launch m5.xlarge and m5.4xlarge instances onto the Dedicated Host.
- To configure the Dedicated Host to support a single instance type within the selected instance family, clear Support multiple instance types, and then for Instance type, choose the instance type to support. This allows you to launch a single instance type on the Dedicated Host. For example, if you choose this option and specify m5.4xlarge as the supported instance type, you can launch only m5.4xlarge instances onto the Dedicated Host.
5. For Availability Zone, choose the Availability Zone in which to allocate the Dedicated Host.
6. To allow the Dedicated Host to accept untargeted instance launches that match its instance type, for Instance auto-placement, choose Enable. For more information about auto- placement, see Amazon EC2 Dedicated Host auto-placement and host affinity.
7. To enable host recovery for the Dedicated Host, for Host recovery, choose Enable. For more information, see Amazon EC2 Dedicated Host recovery.
8. For Quantity, enter the number of Dedicated Hosts to allocate.
9. (Optional) Choose Add new tag and enter a tag key and a tag value.
10. Choose Allocate.
AWS CLI To allocate a Dedicated Host

Use the allocate-hosts command. The following example allocates a Dedicated Host that supports multiple instance types from the m5 instance family in the us-east-1a Availability Zone. It also enables host recovery and disables auto-placement. aws ec2 allocate-hosts \ --instance-family "m5" \ --availability-zone "us-east-1a" \ --auto-placement "off" \ --host-recovery "on" \ --quantity 1 The following example allocates a Dedicated Host that supports untargeted instance launches in the specified Availability Zone, enables host recovery, and enables auto-placement. aws ec2 allocate-hosts \ --instance-type "m5.large" \ --availability-zone "eu-west-1a" \ --auto-placement "on" \ --host-recovery "on" \ --quantity 1 PowerShell To allocate a Dedicated Host Use the New-EC2Host cmdlet. The following example allocates a Dedicated Host that supports multiple instance types from the m5 instance family in the us-east-1a Availability Zone. The host also has host recovery enabled and auto-placement disabled.
New-EC2Host `
    -InstanceFamily m5 `
    -AvailabilityZone us-east-1a `
    -AutoPlacement Off `
    -HostRecovery On `
    -Quantity 1 The following example allocates a Dedicated Host that supports untargeted instance launches in the specified Availability Zone and enables host recovery.
New-EC2Host `
    -InstanceType m5.large `

    -AvailabilityZone eu-west-1a `
    -AutoPlacement On `
    -HostRecovery On `
    -Quantity 1
### Launch Amazon EC2 instances on an Amazon EC2 Dedicated Host After you have allocated a Dedicated Host, you can launch instances onto it. You can't launch instances with host tenancy if you do not have active Dedicated Hosts with enough available capacity for the instance type that you are launching.
##### Considerations
- SQL Server, SUSE, and RHEL AMIs provided by Amazon EC2 can't be used with Dedicated Hosts.
- For Dedicated Hosts that support multiple instance sizes, we recommend that you launch the larger instance sizes first, and then fill the remaining instance capacity with the smaller instance sizes as needed.
- Before you launch your instances, take note of the limitations. For more information, see Dedicated Hosts restrictions.
Console To launch an instance onto a specific Dedicated Host from the Dedicated Hosts page
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. Choose Dedicated Hosts in the navigation pane.
3. On the Dedicated Hosts page, select a host and choose Actions, Launch Instance(s) onto host.
4. In the Application and OS Images section, select an AMI from the list.
5. In the Instance type section, select the instance type to launch.
Note If the Dedicated Host supports a single instance type only, the supported instance type is selected by default and can't be changed.
If the Dedicated Host supports multiple instance types, you must select an instance type within the supported instance family based on the available instance capacity

of the Dedicated Host. We recommend that you launch the larger instance sizes first, and then fill the remaining instance capacity with the smaller instance sizes as needed.
6. In the Key pair section, select the key pair to associate with the instance.
7. In the Advanced details section, for Tenancy affinity, choose one of the following:
- Off — Host affinity disabled. The instance launches onto the specified host, but it is not guaranteed to restart on the same Dedicated Host if stopped.
- A Dedicated Host ID — Host affinity enabled. If stopped, the instance always restarts on this specified host if it has capacity. If the host does not have capacity, the instance can't be restarted; you must establish affinity with a different host.
For more information about Affinity, see Amazon EC2 Dedicated Host auto-placement and host affinity.
Note The Tenancy and Host options are pre-configured based on the host that you selected.
8. Configure the remaining instance options as needed. For more information, see Reference for Amazon EC2 instance configuration parameters.
9. Choose Launch instance.
To launch an instance onto a Dedicated Host using the Launch Instance wizard
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Instances, Launch instance.
3. In the Application and OS Images section, select an AMI from the list.
4. In the Instance type section, select the instance type to launch.
5. In the Key pair section, select the key pair to associate with the instance.
6. In the Advanced details section, do the following: a.
For Tenancy, select Dedicated Host. b.
For Target host by, select Host ID.

c.
For Target host ID, select the host onto which to launch the instance. d.
For Tenancy affinity, choose one of the following:
- Off — Host affinity disabled. The instance launches onto the specified host, but it is not guaranteed to restart on the same Dedicated Host if stopped.
- A Dedicated Host ID — Host affinity enabled. If stopped, the instance always restarts on this specified host if it has capacity. If the host does not have capacity, the instance can't be restarted; you must establish affinity with a different host.
For more information about Affinity, see Amazon EC2 Dedicated Host auto-placement and host affinity.
7. Configure the remaining instance options as needed. For more information, see Reference for Amazon EC2 instance configuration parameters.
8. Choose Launch instance.
AWS CLI To launch an instance onto a Dedicated Host Use the run-instances command and specify the instance affinity, tenancy, and host in the -- placement option.
To launch onto a specific Dedicated Host with host affinity (instance always restarts on the same host if stopped):
--placement Affinity=host,Tenancy=host,HostId=h-07879acf49EXAMPLE To launch onto a specific Dedicated Host without host affinity (instance can restart on any available host):
--placement Tenancy=host,HostId=h-07879acf49EXAMPLE To launch onto any available Dedicated Host with auto-placement enabled and matching instance type:
--placement Tenancy=host

PowerShell To launch an instance onto a Dedicated Host Use the New-EC2Instance cmdlet and specify the instance affinity, tenancy, and host in the - Placement parameter.
To launch onto a specific Dedicated Host with host affinity (instance always restarts on the same host if stopped):
-Placement_Affinity host `
-Placement_Tenancy host `
-Placement_HostId h-07879acf49EXAMPLE To launch onto a specific Dedicated Host without host affinity (instance can restart on any available host):
-Placement_Tenancy host `
-Placement_HostId h-07879acf49EXAMPLE To launch onto any available Dedicated Host with auto-placement enabled and matching instance type:
-Placement_Tenancy host
### Launch Amazon EC2 instances into a host resource group Dedicated Hosts are also integrated with AWS License Manager. With License Manager, you can create a host resource group, which is a collection of Dedicated Hosts that are managed as a single entity. When creating a host resource group, you specify the host management preferences, such as auto-allocate and auto-release, for the Dedicated Hosts. This allows you to launch instances onto Dedicated Hosts without manually allocating and managing those hosts. For more information, see  Host Resource Groups in the AWS License Manager User Guide.
When you launch an instance into a host resource group that has a Dedicated Host with available instance capacity, Amazon EC2 launches the instance onto that host. If the host resource group does not have a host with available instance capacity, Amazon EC2 automatically allocates a new host in the host resource group, and then launches the instance onto that host. For more information, see  Host Resource Groups in the AWS License Manager User Guide.

Requirements and limits
- You must associate a core- or socket-based license configuration with the AMI.
- You can't use SQL Server, SUSE, or RHEL AMIs provided by Amazon EC2 with Dedicated Hosts.
- You can't target a specific host by choosing a host ID, and you can't enable instance affinity when launching an instance into a host resource group.
Console To launch an instance into a host resource group
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Instances, Launch instance.
3. In the Application and OS Images section, select an AMI from the list.
4. In the Instance type section, select the instance type to launch.
5. In the Key pair section, select the key pair to associate with the instance.
6. In the Advanced details section, do the following: a.
For Tenancy, select Dedicated Host. b.
For Target host by, select Host resource group. c.
For Tenancy host resource group, select the host resource group into which to launch the instance. d.
For Tenancy affinity, do one of the following:
- Select Off — The instance launches onto the specified host, but it is not guaranteed to restart on the same Dedicated Host if stopped.
- Select the Dedicated Host ID — If stopped, the instance always restarts on this specific host.
For more information about Affinity, see Amazon EC2 Dedicated Host auto-placement and host affinity.
7. Configure the remaining instance options as needed. For more information, see Reference for Amazon EC2 instance configuration parameters.
8. Choose Launch instance.

AWS CLI To launch an instance into a host resource group Use the run-instances command. In the --placement option, omit the tenancy and specify the ARN of the host resource group.
--placement HostResourceGroupArn=arn:aws:resource-groups:us- east-2:123456789012:group/my-resource-group PowerShell To launch an instance into a host resource group Use the New-EC2Instance cmdlet. In the -Placement parameter, omit the tenancy and specify the ARN of the host resource group.
-Placement_HostResourceGroupArn arn:aws:resource-groups:us- east-2:123456789012:group/my-resource-group
### Modify the auto-placement setting for an existing Amazon EC2 Dedicated Host You can modify the auto-placement settings of a Dedicated Host after you have allocated it to your AWS account.
Console To modify the auto-placement of a Dedicated Host
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Dedicated Hosts.
3. Select a host and choose Actions, Modify host.
4. For Instance auto-placement, choose Enable to enable auto-placement, or clear Enable to disable auto-placement. For more information, see Amazon EC2 Dedicated Host auto- placement and host affinity.
5. Choose Save.

AWS CLI To modify the auto-placement of a Dedicated Host Use the modify-hosts command. aws ec2 modify-hosts \ --auto-placement on \ --host-ids h-012a3456b7890cdef PowerShell To modify the auto-placement of a Dedicated Host Use the Edit-EC2Host cmdlet.
Edit-EC2Host `
    -AutoPlacement 1 `
    -HostId h-012a3456b7890cdef
### Modify supported instance types for an existing Amazon EC2 Dedicated Host You can modify a Dedicated Host to change the instance types that it supports. If it currently supports a single instance type, you can modify it to support multiple instance types within that instance family. Similarly, if it currently supports multiple instance types, you can modify it to support a specific instance type only.
To modify a Dedicated Host to support multiple instance types, you must first stop all running instances on the host. The modification takes approximately 10 minutes to complete. The Dedicated Host transitions to the pending state while the modification is in progress. You can't start stopped instances or launch new instances on the Dedicated Host while it is in the pending state.
To modify a Dedicated Host that supports multiple instance types to support only a single instance type, the host must either have no running instances, or the running instances must be of the instance type that you want the host to support. For example, to modify a host that supports multiple instance types in the m5 instance family to support only m5.large instances, the Dedicated Host must either have no running instances, or it must have only m5.large instances running on it.

If you allocate a host for a virtualized instance type, you can't modify the instance type to a .metal instance type after the host is allocated. For example, if you allocate a host for the m5.large instance type, you can't modify the instance type to m5.metal. Similarly, if you allocate a host for a .metal instance type, you can't modify the instance type to a virtualized instance type after the host is allocated. For example, if you allocate a host for the m5.metal instance type, you can't modify the instance type to m5.large.
Console To modify the supported instance types for a Dedicated Host
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the Navigation pane, choose Dedicated Host.
3. Select the Dedicated Host to modify and choose Actions, Modify host.
4. Do one of the following, depending on the current configuration of the Dedicated Host:
- If the Dedicated Host currently supports a specific instance type, Support multiple instance types is not enabled, and Instance type lists the supported instance type. To modify the host to support multiple types in the current instance family, for Support multiple instance types, choose Enable.
You must first stop all instances running on the host before modifying it to support multiple instance types.
- If the Dedicated Host currently supports multiple instance types in an instance family, Enabled is selected for Support multiple instance types. To modify the host to support a specific instance type, for Support multiple instance types, clear Enable, and then for Instance type, select the specific instance type to support.
You can't change the instance family supported by the Dedicated Host.
5. Choose Save.
AWS CLI To modify the supported instance types for a Dedicated Host Use the modify-hosts command.

The following example modifies a Dedicated Host to support multiple instance types within the m5 instance family. aws ec2 modify-hosts \ --instance-family m5 \ --host-ids h-012a3456b7890cdef The following example modifies a Dedicated Host to support m5.xlarge instances only. aws ec2 modify-hosts \ --instance-type m5.xlarge \ --instance-family --host-ids h-012a3456b7890cdef PowerShell To modify the supported instance types for a Dedicated Host Use the Edit-EC2Host cmdlet.
The following example modifies a Dedicated Host to support multiple instance types within the m5 instance family.
Edit-EC2Host `
    -InstanceFamily m5 `
    -HostId h-012a3456b7890cdef The following example modifies a Dedicated Host to support m5.xlarge instances only.
Edit-EC2Host `
    -InstanceType m5.xlarge `
    -HostId h-012a3456b7890cdef
### Modify Amazon EC2 Dedicated Host tenancy and affinity for an Amazon EC2 instance instance You can change the tenancy of an instance after you have launched it. You can also modify the affinity for your instance to target a specific host or allow it to launch on any available dedicated host with matching attributes in your account. To modify either instance tenancy or affinity, the instance must be in the stopped state.

The operating system details of your instance—and whether SQL Server is installed—affect what conversions are supported. For more information about the tenancy conversion paths available to your instance, see Tenancy conversion in the License Manager User Guide.
Note For T3 instances, you must launch the instance on a Dedicated Host to use a tenancy of host. For T3 instances, you can't change the tenancy from host to dedicated or default. Attempting to make one of these unsupported tenancy changes results in an InvalidRequest error code.
Console To modify instance tenancy or affinity
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. Choose Instances, and select the instance to modify.
3. Choose Instance state, Stop.
4. With the instance selected, choose Actions, Instance settings, Modify instance placement.
5. On the Modify instance placement page, configure the following:
- Tenancy—Choose one of the following:
- Run a dedicated hardware instance—Launches the instance as a Dedicated Instance.
For more information, see Amazon EC2 Dedicated Instances.
- Launch the instance on a Dedicated Host—Launches the instance onto a Dedicated Host with configurable affinity.
- Affinity—Choose one of the following:
- This instance can run on any one of my hosts—The instance launches onto any available Dedicated Host in your account that supports its instance type.
- This instance can only run on the selected host—The instance is only able to run on the Dedicated Host selected for Target Host.
- Target Host—Select the Dedicated Host that the instance must run on. If no target host is listed, you might not have available, compatible Dedicated Hosts in your account.
For more information, see Amazon EC2 Dedicated Host auto-placement and host affinity.

6. Choose Save.
AWS CLI To modify instance tenancy or affinity Use the modify-instance-placement command. The following example changes the specified instance's affinity from default to host, and specifies the Dedicated Host that the instance has affinity with. aws ec2 modify-instance-placement \ --instance-id i-1234567890abcdef0 \ --affinity host \ --tenancy host \ --host-id h-012a3456b7890cdef PowerShell To modify instance tenancy or affinity Use the Edit-EC2InstancePlacement cmdlet. The following example changes the specified instance's affinity from default to host, and specifies the Dedicated Host that the instance has affinity with.
Edit-EC2InstancePlacement `
    -InstanceId i-1234567890abcdef0 `
    -Affinity host `
    -Tenancy host `
    -HostId h-012a3456b7890cdef
### Release an Amazon EC2 Dedicated Host If you no longer need Dedicated Host, you can stop the instances running on the host, direct them to launch on a different host, and then release the host.
Any running instances on the Dedicated Host must be stopped before you can release the host.
These instances can be migrated to other Dedicated Hosts in your account so that you can continue to use them. These steps apply only to On-Demand Dedicated Hosts.

Console To release a Dedicated Host
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Dedicated Hosts.
3. On the Dedicated Hosts page, select the Dedicated Host to release.
4. Choose Actions, Release host.
5. To confirm, choose Release.
AWS CLI To release a Dedicated Host Use the release-hosts command. aws ec2 release-hosts --host-ids h-012a3456b7890cdef PowerShell To release a Dedicated Host Use the Remove-EC2Host cmdlet.
Remove-EC2Host -HostId h-012a3456b7890cdef After you release a Dedicated Host, you can't reuse the same host or host ID again, and you are no longer charged On-Demand billing rates for it. The state of the Dedicated Host is changed to released, and you are not able to launch any instances onto that host.
Note If you have recently released Dedicated Hosts, it can take some time for them to stop counting towards your limit. During this time, you might experience LimitExceeded errors when trying to allocate new Dedicated Hosts. If this is the case, try allocating new hosts again after a few minutes.

The instances that were stopped are still available for use and are listed on the Instances page.
They retain their host tenancy setting.
### Migrate to Nitro-based Amazon EC2 Dedicated Hosts The Nitro System is a collection of hardware and software components built by AWS that enable high performance, high availability, and high security. Nitro-based Dedicated Hosts offer improved price performance compared to Xen-based Dedicated Hosts. If you have any Xen-based Dedicated Hosts in your account, we recommend that you migrate your workloads to Nitro-based Dedicated Hosts. For more information, see AWS Nitro System.
To migrate from a Xen-based Dedicated Host to a Nitro-based Dedicated Host, you need to migrate the Xen-based instances on your Dedicated Host to Nitro-based instance types, allocate a new Nitro-based Dedicated Host, and then move your migrated Nitro-based instances to your new Nitro-based Dedicated Host.
This topic provides detailed steps for migrating from Xen-based Dedicated Hosts to Nitro-based Dedicated Hosts.
Migration steps
- Step 1: Identify your Xen-based Dedicated Hosts
- Step 2: Migrate Xen-based instances to Nitro-based instance types
- Step 3: Allocate a Nitro-based Dedicated Host
- Step 4: Move migrated instances to new Nitro-based Dedicated Host
- Step 5: Release unused Xen-based Dedicated Host
#### Step 1: Identify your Xen-based Dedicated Hosts The following Dedicated Hosts are Xen-based and are eligible to be migrated to Nitro-based Dedicated Hosts.
- General purpose: M3 | M4
- Compute optimized: C3 | C4
- Memory optimized: R3 | R4 | X1 | X1e
- Storage optimized: D2 | H1 | I2 | I3
- Accelerated computing: F1 | G3 | P2 | P3

To check if you have Xen-based Dedicated Hosts in your account
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation panel, choose Dedicated Hosts.
3. In the Search field, use the Instance family filter to search for the Xen-based Dedicated Hosts above. For example, Instance family = m3.
#### Step 2: Migrate Xen-based instances to Nitro-based instance types Instances that run on Xen-based Dedicated Hosts are also Xen-based. You must migrate these instances to Nitro-based instance types before you can move them to Nitro-based Dedicated Hosts.
Important Before you begin migrating your instances, we recommend that you back up your data. For more information, see Create multi-volume Amazon EBS snapshots from an Amazon EC2 instance.
To find instances running on your Xen-based Dedicated Hosts
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation panel, choose Dedicated Hosts.
3. Select the Xen-based host you intend to migrate and then select the Running instances tab.
The tab lists all of the instances running of the selected host.
To migrate Linux instances, see Amazon EC2 instance type changes.
To migrate Windows instances, see Migrate an EC2 Windows instance to a Nitro-based instance type.
Note Ensure that you migrate your instances to an instance type that matches the Nitro-based Dedicated Host that you intend to migrate to. For example, if you intend to migrate to a M7i Dedicated Host, ensure that you migrate your instances to an M7i instance type.

#### Step 3: Allocate a Nitro-based Dedicated Host To find supported Nitro-based Dedicated Hosts
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation panel, select Instance Types.
3. Apply the following filters:
- Hypervisor = nitro
- Dedicated Host support = true After you've found a suitable Nitro-based instance type,  allocate a new Dedicated Host.
#### Step 4: Move migrated instances to new Nitro-based Dedicated Host After you have allocated the Nitro-based Dedicated Host and it reaches the available state, you can move the instances that you previously migrated to Nitro-based instance types to the new Dedicated Host.
To move your instances to your new Nitro-based Dedicated Host
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation panel, Instances.
3. Select the instance that you migrated and choose Actions, Instance settings, Modify instance placement.
4. For Target dedicated host, select the new Nitro-based Dedicated Host, and then choose Save.
5. Restart the instance. Select the instance and choose Instance state, Start instance.
#### Step 5: Release unused Xen-based Dedicated Host After you have migrated your workloads from the Xen-based Dedicated Host to the new Nitro- based Dedicated Host, you can release the Xen-based Dedicated Host if you no longer need it.
### Purchase Dedicated Host Reservations for Dedicated Host billing discounts Dedicated Host Reservations provide you with a discount of up to 70 percent compared to On- Demand Dedicated Host pricing. You must have active Dedicated Hosts allocated in your account

before you can purchase Dedicated Host Reservations. For more information, see Dedicated Host Reservations.
Console To purchase reservations
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. Choose Dedicated Hosts, Dedicated Host Reservations, Purchase Dedicated Host Reservation.
3. On the Find offerings screen, do the following: a.
For Instance family, select the instance family of the Dedicated Host for which to purchase the Dedicated Host Reservation. b.
For Payment option, select and configure your preferred payment option.
4. Choose Next.
5. Select the Dedicated Hosts with which to associate the Dedicated Host Reservation, and then choose Next.
6. (Optional) Assign tags to the Dedicated Host Reservation.
7. Review your order and choose Purchase.
AWS CLI To purchase reservations
1. Use the describe-host-reservation-offerings command to list the available offerings that match your needs. The following example lists the offerings that support instances in the m4 instance family and have a one-year term.
The term is specified in seconds. A one-year term includes 31,536,000 seconds, and a three-year term includes 94,608,000 seconds. aws ec2 describe-host-reservation-offerings \ --filter Name=instance-family,Values=m4 \ --max-duration 31536000

The command returns a list of offerings that match your criteria. Note the ID of the offering to purchase.
2. Use the purchase-host-reservation command to purchase the offering and provide the offeringId noted in the previous step. The following example purchases the specified reservation and associates it with a specific Dedicated Host that is already allocated in the AWS account, and it applies a tag with a key of purpose and a value of production. aws ec2 purchase-host-reservation \ --offering-id hro-03f707bf363b6b324 \ --host-id-set h-013abcd2a00cbd123 \ --tag-specifications 'ResourceType=host- reservation,Tags={Key=purpose,Value=production}'
PowerShell To purchase reservations
1. Use the Get-EC2HostReservationOffering cmdlet to list the available offerings that match your needs. The following examples list the offerings that support instances in the m5 instance family and have a one-year term.
The term is specified in seconds. A one-year term includes 31,536,000 seconds, and a three-year term includes 94,608,000 seconds.
$filter = @{Name="instance-family"; Values="m5"} Get-EC2HostReservationOffering `
    -Filter $filter `
    -MaxDuration 31536000 The command returns a list of offerings that match your criteria. Note the ID of the offering to purchase.
2. Use the New-EC2HostReservation cmdlet to purchase the offering and provide the offering ID noted in the previous step. The following example purchases the specified reservation and associates it with a specific Dedicated Host that is already allocated in the AWS account.
New-EC2HostReservation `

    -OfferingId hro-03f707bf363b6b324 `
    -HostIdSet h-013abcd2a00cbd123
### Cross-account Amazon EC2 Dedicated Host sharing Dedicated Host sharing enables Dedicated Host owners to share their Dedicated Hosts with other AWS accounts or within an AWS organization. This enables you to create and manage Dedicated Hosts centrally, and share the Dedicated Host across multiple AWS accounts or within your AWS organization.
In this model, the AWS account that owns the Dedicated Host (owner) shares it with other AWS accounts (consumers). Consumers can launch instances onto Dedicated Hosts that are shared with them in the same way that they would launch instances onto Dedicated Hosts that they allocate in their own account. The owner is responsible for managing the Dedicated Host and the instances that they launch onto it. Owners can't modify instances that consumers launch onto shared Dedicated Hosts. Consumers are responsible for managing the instances that they launch onto Dedicated Hosts shared with them. Consumers can't view or modify instances owned by other consumers or by the Dedicated Host owner, and they can't modify Dedicated Hosts that are shared with them.
A Dedicated Host owner can share a Dedicated Host with:
- Specific AWS accounts inside or outside of its AWS organization
- An organizational unit inside its AWS organization
- Its entire AWS organization Contents
- Prerequisites for sharing Dedicated Hosts
- Limitations for sharing Dedicated Hosts
- Related services
- Share across Availability Zones
- Shared Dedicated Host permissions
- Billing and metering
- Dedicated Host limits
- Host recovery and Dedicated Host sharing

- Share an Amazon EC2 Dedicated Host across AWS accounts
- Unshare a Dedicated Host that is shared with other AWS accounts
- View shared Amazon EC2 Dedicated Hosts in your AWS account
#### Prerequisites for sharing Dedicated Hosts
- To share a Dedicated Host, you must own it in your AWS account. You can't share a Dedicated Host that has been shared with you.
- To share a Dedicated Host with your AWS organization or an organizational unit in your AWS organization, you must enable sharing with AWS Organizations. For more information, see Enable Sharing with AWS Organizations in the AWS RAM User Guide.
#### Limitations for sharing Dedicated Hosts You can't share Dedicated Hosts that have been allocated for the following instance types: u-6tb1.metal, u-9tb1.metal, u-12tb1.metal, u-18tb1.metal, and u-24tb1.metal.
#### Related services
##### AWS Resource Access Manager Dedicated Host sharing integrates with AWS Resource Access Manager (AWS RAM). AWS RAM is a service that enables you to share your AWS resources with any AWS account or through AWS Organizations. With AWS RAM, you share resources that you own by creating a resource share.
A resource share specifies the resources to share, and the consumers with whom to share them.
Consumers can be individual AWS accounts, or organizational units or an entire organization from AWS Organizations.
For more information about AWS RAM, see the AWS RAM User Guide.
#### Share across Availability Zones To ensure that resources are distributed across the Availability Zones for a Region, we independently map Availability Zones to names for each account. This could lead to Availability Zone naming differences across accounts. For example, the Availability Zone us-east-1a for your AWS account might not have the same location as us-east-1a for another AWS account.
To identify the location of your Dedicated Hosts relative to your accounts, you must use the Availability Zone ID (AZ ID). The Availability Zone ID is a unique and consistent identifier for an

Availability Zone across all AWS accounts. For example, use1-az1 is an Availability Zone ID for the us-east-1 Region and it is the same location in every AWS account.
To view the Availability Zone IDs for the Availability Zones in your account
1. Open the AWS RAM console at https://console.aws.amazon.com/ram/home.
2. The Availability Zone IDs for the current Region are displayed in the Your AZ ID panel on the right-hand side of the screen.
#### Shared Dedicated Host permissions
##### Permissions for owners Owners are responsible for managing their shared Dedicated Hosts and the instances that they launch onto them. Owners can view all instances running on the shared Dedicated Host, including those launched by consumers. However, owners can't take any action on running instances that were launched by consumers.
##### Permissions for consumers Consumers are responsible for managing the instances that they launch onto a shared Dedicated Host. Consumers can't modify the shared Dedicated Host in any way, and they can't view or modify instances that were launched by other consumers or the Dedicated Host owner.
#### Billing and metering There are no additional charges for sharing Dedicated Hosts.
Owners are billed for Dedicated Hosts that they share. Consumers are not billed for instances that they launch onto shared Dedicated Hosts.
Dedicated Host Reservations continue to provide billing discounts for shared Dedicated Hosts. Only Dedicated Host owners can purchase Dedicated Host Reservations for shared Dedicated Hosts that they own.
#### Dedicated Host limits Shared Dedicated Hosts count towards the owner's Dedicated Hosts limits only. Consumer's Dedicated Hosts limits are not affected by Dedicated Hosts that have been shared with them.

Similarly, instances that consumers launch onto shared Dedicated Hosts do not count towards their instance limits.
#### Host recovery and Dedicated Host sharing Host recovery recovers instances launched by the Dedicated Host owner and the consumers with whom it has been shared. The replacement Dedicated Host is allocated to the owner's account. It is added to the same resource shares as the original Dedicated Host, and it is shared with the same consumers.
For more information, see Amazon EC2 Dedicated Host recovery.
#### Share an Amazon EC2 Dedicated Host across AWS accounts When an owner shares a Dedicated Host, it enables consumers to launch instances on the host.
Consumers can launch as many instances onto the shared host as its available capacity allows.
Important Note that you are responsible for ensuring that you have appropriate license rights to share any BYOL licenses on your Dedicated Hosts.
If you share a Dedicated Host with auto-placement enabled, keep the following in mind as it could lead to unintended Dedicated Host usage:
- If consumers launch instances with Dedicated Host tenancy and they do not have capacity on a Dedicated Host that they own in their account, the instance is automatically launched onto the shared Dedicated Host.
To share a Dedicated Host, you must add it to a resource share. A resource share is an AWS RAM resource that lets you share your resources across AWS accounts. A resource share specifies the resources to share, and the consumers with whom they are shared. You can add the Dedicated Host to an existing resource, or you can add it to a new resource share.
If you are part of an organization in AWS Organizations and sharing within your organization is enabled, consumers in your organization are automatically granted access to the shared Dedicated Host. Otherwise, consumers receive an invitation to join the resource share and are granted access to the shared Dedicated Host after accepting the invitation.

Note After you share a Dedicated Host, it could take a few minutes for consumers to have access to it.
Console To share a Dedicated Host that you own using the Amazon EC2 console
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Dedicated Hosts.
3. Choose the Dedicated Host to share and choose Actions, Share host.
4. Select the resource share to which to add the Dedicated Host and choose Share host.
It could take a few minutes for consumers to get access to the shared host.
To share a Dedicated Host that you own using the AWS RAM console See Create a resource share in the AWS RAM User Guide.
AWS CLI To share a Dedicated Host that you own Use the create-resource-share command. aws ram create-resource-share \ --name my-resource-share \ --resource-arns arn:aws:ec2:us-east-2:123456789012:dedicated- host/h-07879acf49EXAMPLE PowerShell To share a Dedicated Host that you own Use the New-RAMResourceShare cmdlet.
New-RAMResourceShare `
    -Name my-resource-share `

    -ResourceArn arn:aws:ec2:us-east-2:123456789012:dedicated- host/h-07879acf49EXAMPLE
#### Unshare a Dedicated Host that is shared with other AWS accounts The Dedicated Host owner can unshare a shared Dedicated Host at any time. When you unshare a shared Dedicated Host, the following rules apply:
- Consumers with whom the Dedicated Host was shared can no longer launch new instances onto it.
- Instances owned by consumers that were running on the Dedicated Host at the time of unsharing continue to run but are scheduled for retirement. Consumers receive retirement notifications for the instances and they have two weeks to take action on the notifications. However, if the Dedicated Host is reshared with the consumer within the retirement notice period, the instance retirements are cancelled.
To unshare a shared Dedicated Host that you own, you must remove it from the resource share.
Console To unshare a shared Dedicated Host that you own
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Dedicated Hosts.
3. Choose the Dedicated Host to unshare and choose the Sharing tab.
4. The Sharing tab lists the resource shares to which the Dedicated Host has been added.
Select the resource share from which to remove the Dedicated Host and choose Remove host from resource share.
To unshare a shared Dedicated Host that you own using the AWS RAM console See Update a resource share in the AWS RAM User Guide.
AWS CLI To unshare a shared Dedicated Host that you own Use the disassociate-resource-share command.

aws ram disassociate-resource-share \ --resource-share-arn arn:aws:ram:us-east-2:123456789012:resource-share/7ab63972- b505-7e2a-420d-6f5d3EXAMPLE \ --resource-arns arn:aws:ec2:us-east-2:123456789012:dedicated- host/h-07879acf49EXAMPLE PowerShell To unshare a shared Dedicated Host that you own Use the Disconnect-RAMResourceShare cmdlet.
Disconnect-RAMResourceShare `
    -ResourceShareArn "arn:aws:ram:us-east-2:123456789012:resource-share/7ab63972- b505-7e2a-420d-6f5d3EXAMPLE" `
    -ResourceArn "arn:aws:ec2:us-east-2:123456789012:dedicated- host/h-07879acf49EXAMPLE"
#### View shared Amazon EC2 Dedicated Hosts in your AWS account You can view Dedicated Host that you are sharing with other accounts, and Dedicated Hosts that are shared with you. If you own the Dedicated Host, you can see all of the instances running on the host, including instances launched by consumers. If the Dedicated Host is shared with you, you can see only the instances that you launched onto the shared host, and not those launched by other consumers.
Owners and consumers can identify shared Dedicated Hosts using one of the following methods.
Console To identify a shared Dedicated Host
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Dedicated Hosts. The screen lists Dedicated Hosts that you own and Dedicated Hosts that are shared with you.
3. The Owner column shows the AWS account ID of the Dedicated Host owner.
4. To view the instances running on the hosts, select the Instances tab.

AWS CLI To identify a shared Dedicated Host Use the  describe-hosts command. The command returns the Dedicated Hosts that you own and Dedicated Hosts that are shared with you. The value of Owner is the account ID of the owner of the Dedicated Host. The Instances list describes the instances running on the host. aws ec2 describe-hosts --filter "Name=state,Values=available"
PowerShell To identify a shared Dedicated Host Use the Get-EC2host cmdlet. The cmdlet returns the Dedicated Hosts that you own and Dedicated Hosts that are shared with you. The value of Owner in the response is the account ID of the owner of the Dedicated Host. The Instances list describes the instances running on the host.
Get-EC2Host -Filter @{Name="state"; Values="available"}
### Amazon EC2 Dedicated Hosts on AWS Outposts AWS Outposts is a fully managed service that extends AWS infrastructure, services, APIs, and tools to your premises. By providing local access to AWS managed infrastructure, AWS Outposts enables you to build and run applications on premises using the same programming interfaces as in AWS Regions, while using local compute and storage resources for lower latency and local data processing needs.
An Outpost is a pool of AWS compute and storage capacity deployed at a customer site. AWS operates, monitors, and manages this capacity as part of an AWS Region.
You can allocate Dedicated Hosts on Outposts that you own in your account. This makes it easier for you to bring your existing software licenses and workloads that require a dedicated physical server to AWS Outposts. You can also target specific hardware assets on an Outpost to help minimize latency between your workloads.
Dedicated Hosts allow you to use your eligible software licenses on Amazon EC2, so that you get the flexibility and cost effectiveness of using your own licenses. Other software licenses that are bound to virtual machines, sockets, or physical cores, can also be used on Dedicated Hosts, subject

to their license terms. While Outposts have always been a single-tenant environments that are eligible for BYOL workloads, Dedicated Hosts allows you to limit the needed licenses to a single host as opposed to the entire Outpost deployment.
Additionally, using Dedicated Hosts on an Outpost gives you greater flexibility in instance type deployment, and more granular control over instance placement. You can target a specific host for instance launches and use host affinity to ensure that the instance always runs on that host, or you can use auto-placement to launch an instance onto any available host that has matching configurations and available capacity.
Contents
- Prerequisites
- Supported features
- Considerations
- Allocate an Amazon EC2 Dedicated Host on AWS Outposts
###### Prerequisites You must have an Outpost installed at your site. For more information, see  Create an Outpost and order Outpost capacity in the AWS Outposts User Guide.
#### Supported features
- The following instance families are supported: C5, M5, R5, C5d, M5d, R5d, G4dn, and i3en.
- Dedicated Hosts on Outposts can be configured to support multiple instance sizes. Support for multiple instance sizes is available for the following instance families: C5, M5, R5, C5d, M5d, and R5d. For more information, see Amazon EC2 Dedicated Host instance capacity configurations.
- Dedicated Hosts on Outposts support auto-placement and targeted instance launches. For more information, see Amazon EC2 Dedicated Host auto-placement and host affinity.
- Dedicated Hosts on Outposts support host affinity. For more information, see Amazon EC2 Dedicated Host auto-placement and host affinity.
- Dedicated Hosts on Outposts support sharing with AWS RAM. For more information, see Cross- account Amazon EC2 Dedicated Host sharing.
###### Considerations
- Dedicated Host Reservations are not supported on Outposts.

- Host resource groups and AWS License Manager are not supported on Outposts.
- Dedicated Hosts on Outposts do not support burstable T3 instances.
- Dedicated Hosts on Outposts do not support host recovery.
- Simplified automatic recovery is not supported for instances with Dedicated Host tenancy on Outposts.
#### Allocate an Amazon EC2 Dedicated Host on AWS Outposts You allocate and use Dedicated Hosts on Outposts in the same way that would with Dedicated Hosts in an AWS Region.
Prerequisites Create a subnet on the Outpost. For more information, see Create a subnet in the AWS Outposts User Guide.
To allocate a Dedicated Host on an Outpost, use one of the following methods:
Console To allocate a Dedicated Host on an Outpost using the AWS Outposts console
1. Open the AWS Outposts console at https://console.aws.amazon.com/outposts/.
2. In the navigation pane, choose Outposts. Select the Outpost and then choose Actions, Allocate Dedicated Host.
3. Configure the Dedicated Host as needed. For more information, see Allocate an Amazon EC2 Dedicated Host for use in your account.
Note Availability Zone and Outpost ARN should be pre-populated with the Availability Zone and ARN of the selected Outpost.
4. Choose Allocate.
To allocate a Dedicated Host on an Outpost using the Amazon EC2 console
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.

2. In the navigation pane, choose Dedicated Hosts, and then choose Allocate Dedicated Host.
3. For Availability Zone, select the Availability Zone associated with the Outpost.
4. For Outpost ARN, enter the ARN of the Outpost.
5. To target specific hardware assets on the Outpost, for Target specific hardware assets on Outpost, select Enable. For each hardware asset to target, choose Add asset ID, and then enter the ID of the hardware asset.
Note The value that you specify for Quantity must be equal to the number of asset IDs that you specify. For example, if you specify 3 asset IDs, then Quantity must also be
3. 6.
Configure the remaining Dedicated Host settings as needed. For more information, see Allocate an Amazon EC2 Dedicated Host for use in your account.
7. Choose Allocate.
AWS CLI To allocate a Dedicated Host on an Outpost Use the allocate-hosts command. For --availability-zone, specify the Availability Zone associated with the Outpost. For --outpost-arn, specify the ARN of the Outpost. Optionally, for --asset-ids, specify the IDs of the Outpost hardware assets to target. aws ec2 allocate-hosts \ --availability-zone "us-east-1a" \ --outpost-arn "arn:aws:outposts:us-east-1a:111122223333:outpost/ op-4fe3dc21baEXAMPLE" \ --asset-ids asset_id \ --instance-family "m5" \ --auto-placement "off" \ --quantity 1 PowerShell To allocate a Dedicated Host on an Outpost

Use the New-EC2Host cmdlet. Specify the Availability Zone associated with the Outpost.
Optionally, for -AssetId, specify the IDs of the Outpost hardware assets to target.
New-EC2Host `
    -AvailabilityZone "us-east-1a" `
    -OutpostArn "arn:aws:outposts:us-east-1a:111122223333:outpost/ op-4fe3dc21baEXAMPLE" `
    -AssetId asset_id `
    -InstanceFamily "m5" `
    -AutoPlacement "off" `
    -Quantity 1 To launch an instance onto a Dedicated Host on an Outpost
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Dedicated Hosts. Select the Dedicated Host that you allocated in the previous step and choose Actions, Launch instance onto host.
3. Configure the instance as needed and then launch the instance. For more information, see Launch Amazon EC2 instances on an Amazon EC2 Dedicated Host.
### Amazon EC2 Dedicated Host recovery Dedicated Host auto recovery restarts your instances on to a new replacement host when certain problematic conditions are detected on your Dedicated Host. Host recovery reduces the need for manual intervention and lowers the operational burden if there is an unexpected Dedicated Host failure concerning system power or network connectivity events. Other Dedicated Host issues will require manual intervention to recover from.
Contents
- How Amazon EC2 Dedicated Host recovery works
- Supported instance types
- Pricing
- Manage Amazon EC2 Dedicated Host recovery
- View the host recovery setting for your Amazon EC2 Dedicated Host
- Manually recover instances that are not supported by Amazon EC2 Dedicated Host recovery

#### How Amazon EC2 Dedicated Host recovery works Dedicated Hosts and the host resource groups recovery process use host-level health checks to assess Dedicated Host availability and to detect underlying system failures. The type of Dedicated Host failure determines if Dedicated Host auto recovery is possible. Examples of problems that can cause host-level health checks to fail include:
- Loss of network connectivity
- Loss of system power
- Hardware or software issues on the physical host Important Dedicated Host auto recovery does not occur when the host is scheduled for retirement.
##### Dedicated Host auto recovery When a system power or network connectivity failure is detected on your Dedicated Host, Dedicated Host auto recovery is initiated and Amazon EC2 automatically allocates a replacement Dedicated Host in the same Availability Zone as the original Dedicated Host. The replacement Dedicated Host receives a new host ID, but retains the same attributes as the original Dedicated Host, including:
- Availability Zone
- Instance type
- Tags
- Auto placement settings
- Reservation When the replacement Dedicated Host is allocated, the instances are recovered on to the replacement Dedicated Host. The recovered instances retain the same attributes as the original instances, including:
- Instance ID
- Private IP addresses

- Elastic IP addresses
- EBS volume attachments
- All instance metadata Additionally, the built-in integration with AWS License Manager automates the tracking and management of your licenses.
Note AWS License Manager integration is supported only in Regions in which AWS License Manager is available.
If instances have a host affinity relationship with the impaired Dedicated Host, the recovered instances establish host affinity with the replacement Dedicated Host.
When all of the instances have been recovered on to the replacement Dedicated Host, the impaired Dedicated Host is released, and the replacement Dedicated Host becomes available for use.
When host recovery is initiated, the AWS account owner is notified by email and by an AWS Health Dashboard event. A second notification is sent after the host recovery has been successfully completed.
If you are using AWS License Manager to track your licenses, AWS License Manager allocates new licenses for the replacement Dedicated Host based on the license configuration limits. If the license configuration has hard limits that will be breached as a result of the host recovery, the recovery process is not allowed and you are notified of the host recovery failure through an Amazon SNS notification (if notification settings have been configured for AWS License Manager). If the license configuration has soft limits that will be breached as a result of the host recovery, the recovery is allowed to continue and you are notified of the limit breach through an Amazon SNS notification.
For more information, see Using License Configurations and Settings in License Manager in the AWS License Manager User Guide.
##### Host recovery states When a Dedicated Host failure is detected, the impaired Dedicated Host enters the under- assessment state, and all of the instances enter the impaired state. You can't launch instances on to the impaired Dedicated Host while it is in the under-assessment state.

After the replacement Dedicated Host is allocated, it enters the pending state. It remains in this state until the host recovery process is complete. You can't launch instances on to the replacement Dedicated Host while it is in the pending state. Recovered instances on the replacement Dedicated Host remain in the impaired state during the recovery process.
After the host recovery is complete, the replacement Dedicated Host enters the available state, and the recovered instances return to the running state. You can launch instances on to the replacement Dedicated Host after it enters the available state. The original impaired Dedicated Host is permanently released and it enters the released-permanent-failure state.
If the impaired Dedicated Host has instances that do not support host recovery, such as instances with instance store root volumes, the Dedicated Host is not released. Instead, it is marked for retirement and enters the permanent-failure state.
##### Scenarios without Dedicated Host auto recovery Dedicated Host auto recovery does not occur when the host is scheduled for retirement. You will receive a retirement notification in the AWS Health Dashboard, an Amazon CloudWatch event, and the AWS account owner email address receives a message regarding the Dedicated Host failure.
Follow the remedial steps described in the retirement notification within the specified time period to manually recover the instances on the retiring host.
Stopped instances are not recovered on to the replacement Dedicated Host. If you attempt to start a stopped instance that targets the impaired Dedicated Host, the instance start fails. We recommend that you modify the stopped instance to either target a different Dedicated Host, or to launch on any available Dedicated Host with matching configurations and auto-placement enabled.
Instances with instance storage are not recovered on to the replacement Dedicated Host. As a remedial measure, the impaired Dedicated Host is marked for retirement and you receive a retirement notification after the host recovery is complete. Follow the remedial steps described in the retirement notification within the specified time period to manually recover the remaining instances on the impaired Dedicated Host.
#### Supported instance types Host recovery is supported for the following instance families:
- General purpose: A1 | M3 | M4 | M5 | M5n | M5zn | M6a | M6g | M6i | T3 | Mac1 | Mac2 | Mac2- m1ultra | Mac2-m2 | Mac2-m2pro
- Compute optimized: C3 | C4 | C5 | C5n | C6a | C6g | C6i

- Memory optimized: R3 | R4 | R5 | R5b | R5n | R6g | R6i | U-6tb1 | U-9tb1 | U-12tb1 | U-18tb1 | U-24tb1 | X1 | X1e | X2iezn
- Accelerated computing: Inf1 | G3 | G5g | P2 | P3 To recover instances that are not supported, see Manually recover instances that are not supported by Amazon EC2 Dedicated Host recovery.
Note Dedicated Host auto recovery of supported metal instance types will take longer to detect and recover from than non-metal instance types.
#### Pricing There are no additional charges for using host recovery, but the usual Dedicated Host charges apply. For more information, see  Amazon EC2 Dedicated Hosts Pricing.
As soon as host recovery is initiated, you are no longer billed for the impaired Dedicated Host.
Billing for the replacement Dedicated Host begins only after it enters the available state.
If the impaired Dedicated Host was billed using the On-Demand rate, the replacement Dedicated Host is also billed using the On-Demand rate. If the impaired Dedicated Host had an active Dedicated Host Reservation, it is transferred to the replacement Dedicated Host.
#### Manage Amazon EC2 Dedicated Host recovery Dedicated Host auto recovery restarts your instances on to a new replacement host when certain problematic conditions are detected on your Dedicated Host. You can enable host recovery when you allocate the Dedicated Host or after allocation.
Use the following procedures to enable host recovery when allocating the host.
Console To enable host recovery at allocation When allocating a Dedicated Host using the Amazon EC2 console, for Host recovery, choose Enable. For more information, see Allocate an Amazon EC2 Dedicated Host for use in your account.

AWS CLI To enable host recovery at allocation Use the allocate-hosts command. aws ec2 allocate-hosts \ --instance-type m5.large \ --availability-zone eu-west-1a \ --auto-placement on \ --host-recovery on \ --quantity 1 PowerShell To enable host recovery at allocation Use the New-EC2Host cmdlet.
New-EC2Host `
    -InstanceType m5.large `
    -AvailabilityZone eu-west-1a `
    -AutoPlacement on `
    -HostRecovery on `
    -Quantity 1 Use the following procedures to manage host recovery for a Dedicated Host.
Console To manage host recovery after allocation
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Dedicated Hosts.
3. Select the Dedicated Host.
4. Choose Actions, Modify host.
5. For Host recovery, select or clear Enable.
6. Choose Save.

AWS CLI To enable host recovery after allocation Use the modify-hosts command. aws ec2 modify-hosts \ --host-recovery on \ --host-ids h-012a3456b7890cdef To disable host recovery after allocation Use the modify-hosts command and specify the host-recovery parameter with a value of off. aws ec2 modify-hosts \ --host-recovery off \ --host-ids h-012a3456b7890cdef PowerShell To enable host recovery after allocation Use the Edit-host cmdlet.
Edit-EC2Host `
    -HostRecovery on `
    -HostId h-012a3456b7890cdef To disable host recovery after allocation Use the Edit-EC2Host cmdlet.
Edit-EC2Host `
    -HostRecovery off `
    -HostId h-012a3456b7890cdef
#### View the host recovery setting for your Amazon EC2 Dedicated Host You can view the host recovery configuration for a Dedicated Host at any time.

Console To view the host recovery configuration for a Dedicated Host
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Dedicated Hosts.
3. Select the Dedicated Host, and in the Description tab, review the Host Recovery field.
AWS CLI To view the host recovery configuration for a Dedicated Host Use the describe-hosts command. aws ec2 describe-hosts \ --host-ids h-012a3456b7890cdef \ --query Hosts[].HostRecovery The following is example output. on PowerShell To view the host recovery configuration for a Dedicated Host Use the Get-EC2Host cmdlet.
(Get-EC2Host -HostId h-012a3456b7890cdef).Hosts | Select HostRecovery The following is example output.
HostRecovery
------------ on

#### Manually recover instances that are not supported by Amazon EC2 Dedicated Host recovery Host recovery does not support recovering instances that use instance store volumes. Follow the instructions below to manually recover any of your instances that could not be automatically recovered.
Warning Data on instance store volumes is lost when an instance is stopped, hibernated, or terminated. This includes instance store volumes that are attached to an instance that has an EBS root volume. To protect data from instance store volumes, back it up to persistent storage before the instance is stopped or terminated.
##### Manually recover EBS-backed instances For EBS-backed instances that could not be automatically recovered, we recommend that you manually stop and start the instances to recover them onto a new Dedicated Host. For more information about stopping your instance, and about the changes that occur in your instance configuration when it's stopped, see Stop and start Amazon EC2 instances.
##### Manually recover instances with instance store root volumes For instances with instance store root volumes that could not be automatically recovered, we recommend that you do the following:
1. Launch a replacement instance on a new Dedicated Host from your most recent AMI.
2. Migrate all of the necessary data to the replacement instance.
3. Terminate the original instance on the impaired Dedicated Host.
### Host maintenance for Amazon EC2 Dedicated Host With host maintenance, in the rare event that a Dedicated Host becomes degraded, we automatically migrate instances running on it onto a healthy replacement Dedicated Host.
This helps to minimize the downtime for your workload, and simplify the management of your Dedicated Hosts. Host maintenance is also performed for planned and routine Amazon EC2 maintenance.
Amazon EC2 supports two types of host maintenance:

- Live migration host maintenance — Instances are automatically migrated to the replacement host within 24 hours, without stopping and restarting them.
- Reboot-based host maintenance — Instances are scheduled for instance reboot scheduled events, during which they are automatically stopped and restarted on the replacement host.
Contents
- Host maintenance versus host recovery
- Considerations
- Related services
- Pricing
- How host maintenance works for Amazon EC2 Dedicated Hosts
- Configure the host maintenance setting for an Amazon EC2 Dedicated Host
#### Host maintenance versus host recovery The following table shows the main differences between host recovery and host maintenance.

Host recovery Host maintenance Instance reachability Unreachable Reachable Dedicated Host state under-assessment permanent-failure Host resource group Supported Not supported For more information about host recovery, see Host recovery.
##### Considerations
- Host maintenance is available in all AWS Regions, except the China Regions and AWS GovCloud (US) Regions.
- Host maintenance is not supported in AWS Outposts, AWS Local Zones, and AWS Wavelength Zones.

- Host maintenance can't be turned on or off for hosts already within a host resource group. Hosts added to a host resource group retain their host maintenance setting. For more information, see Host resource groups.
- Host maintenance is not supported with the following instance types, because they have instance store root volumes: C1, C3, D2, I2, M1, M2, M3, R3, and X1.
#### Related services Dedicated Host integrates with AWS License Manager—Tracks licenses across your Amazon EC2 Dedicated Hosts (supported only in Regions in which AWS License Manager is available). For more information, see the AWS License Manager User Guide.
You must have sufficient licenses in your AWS account for your new Dedicated Host. The licenses associated with your degraded host are released when the host is released after the completion of the scheduled event.
#### Pricing There are no additional charges for using host maintenance, but the usual Dedicated Host charges apply. For more information, see  Amazon EC2 Dedicated Hosts Pricing.
As soon as host maintenance is initiated, you are no longer billed for the degraded Dedicated Host.
Billing for the replacement Dedicated Host begins only after it enters the available state.
If the degraded Dedicated Host was billed using the On-Demand rate, the replacement Dedicated Host is also billed using the On-Demand rate. If the degraded Dedicated Host had an active Dedicated Host Reservation, it is transferred to the new Dedicated Host.
#### How host maintenance works for Amazon EC2 Dedicated Hosts When a degradation is detected on a Dedicated Host that is enabled for host maintenance, we automatically allocate a replacement Dedicated Host in your account. The replacement Dedicated Host receives a new host ID, but retains the same attributes as the original Dedicated Host, including:
- Auto placement settings
- Availability Zone
- Dedicated Host Reservation association
- Host affinity

- Host maintenance settings
- Host recovery settings
- Instance type
- Tags After the replacement host has been allocated, we migrate the instances using either live migration host maintenance or reboot-based host maintenance, depending on the instance.
After the degraded host has no more running instances, it is permanently released from your account.
##### Live migration host maintenance Instances that require live migration host maintenance are automatically migrated to the replacement host within 24 hours, without stopping and restarting them. The migrated instances retain their existing attributes, including:
- Instance ID
- Instance metadata
- Amazon EBS volume attachments
- Elastic IP addresses and private IP address
- Memory, CPU, and networking states Some larger instance sizes might experience a slight performance decrease during the migration.
After the instances are automatically migrated to the replacement host, we send you email and AWS Health Dashboard notifications. Notifications include the IDs of the degraded and replacement hosts, information about the instances that were automatically migrated using live migration host maintenance, and information about the remaining instances.
##### Reboot-based host maintenance Instances that require reboot-based host maintenance are scheduled for instance reboot scheduled events for 14 days from the date of the notification. You can continue to access your instances on the degraded Dedicated Host before the scheduled event.
You can reschedule reboot events for a date that is within 7 days of the original event date and time. For more information, see Reschedule a scheduled event for an EC2 instance.

Amazon EC2 automatically reserves capacity on the replacement host for these instances. You can't run instances in this reserved capacity.
The Amazon EC2 console shows the reserved capacity as used capacity. It could appear that the instances are running on both the degraded host and the replacement host. However, the instances will continue to run only on the degraded host until they are stopped or they are migrated into the reserved capacity on the replacement host.
At the date and time of the scheduled event, the instances are automatically stopped and restarted into the reserved capacity on the replacement host. The migrated instances retain their existing attributes, including:
- Instance ID
- Instance metadata
- Amazon EBS volume attachments
- Elastic IP addresses and private IP address However, since the instances are stopped and restarted during the migration, they do not retain their memory, CPU, and networking states.
You can also manually stop and restart these instances at any time before the scheduled event to migrate them to the replacement host or to a different host. You might need to modify your instance's host affinity to restart it on a different host. If you stop an instance before the scheduled event, the reserved capacity on the replacement host is released and becomes available for use.
##### Host maintenance states When a host becomes degraded, it enters the permanent-failure state. You can't launch instances on a Dedicated Host that is in the permanent-failure state.
After the replacement host is allocated, it remains in the pending state until the instances that support live migration host maintenance are automatically migrated from the degraded host, and until the scheduled events are scheduled for the remaining instances. After these tasks are completed, the replacement host enters the available state.
After the replacement host enters the available state, you can use it in the same way that you use any host in your account. However, some instance capacity on the replacement host is reserved for the instances that require reboot-based host migration. You can't launch new instances into this reserved capacity.

When the degraded host has no more running instances, it enters the released, permanent- failure state, and it is permanently released from your account. Note that the host and its resources remain visible in the console for a short time.
##### Automatic migration Some instances can't be automatically migrated to the replacement host.
Instances with EBS-backed root volumes For these instances, we schedule instance stop events for 28 days from the date of the notification.
At the date and time of the scheduled event, the instances are stopped. We recommend that you manually stop on restart the instance on the replacement host or on a different host. You might need to modify your instance's host affinity to restart it on a different host.
Instances with an instance store root volume For these instances, we schedule instance retirement events for 28 days from the date of the notification. At the date and time of the scheduled event, the instances are permanently terminated. We recommend that you manually launch replacement instances on the replacement host and then migrate the required data to the replacement instances before the scheduled event.
The following instances have instance store root volumes: C1, C3, D2, I2, M1, M2, M3, R3, and X1.
You can continue to access your instances on the degraded Dedicated Host before the scheduled event.
#### Configure the host maintenance setting for an Amazon EC2 Dedicated Host Enable host maintenance to ensure that your instances running on a Dedicated Host are automatically recovered onto a new Dedicated Host during a scheduled maintenance event.
If you disable host maintenance, you receive an email notification to evict the degraded host and manually migrate your instances to another host within 28 days. A replacement host is allocated if you have Dedicated Host reservation. After 28 days, the instances running on the degraded host are terminated, and the host is released automatically.
Console To enable host maintenance for your Dedicated Host
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.

2. In the navigation pane, choose Dedicated Hosts.
3. Select the Dedicated Host > Actions > Modify host.
4. Select on in the Host maintenance field.
To disable host maintenance for your Dedicated Host
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Dedicated Hosts.
3. Select the Dedicated Host > Actions > Modify host.
4. Select off in the Host maintenance field.
AWS CLI To enable host maintenance for your Dedicated Host Use the modify-hosts command. aws ec2 modify-hosts \ --host-maintenance on \ --host-ids h-0d123456bbf78910d To disable host maintenance for your Dedicated Host Use the modify-hosts command. aws ec2 modify-hosts \ --host-maintenance off \ --host-ids h-0d123456bbf78910d PowerShell To enable host maintenance for your Dedicated Host Use the Edit-EC2Host cmdlet.
Edit-EC2Host `
    -HostMaintenance on `

    -HostId h-0d123456bbf78910d To disable host maintenance for your Dedicated Host Use the Edit-EC2Host cmdlet.
Edit-EC2Host `
    -HostMaintenance off `
    -HostId h-0d123456bbf78910d
### Monitor the state of your Amazon EC2 Dedicated Hosts Amazon EC2 constantly monitors the state of your Dedicated Hosts. Updates are communicated on the Amazon EC2 console. You can view information about a Dedicated Host using the following methods.
Console To view the state of a Dedicated Host
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Dedicated Hosts.
3. Locate the Dedicated Host in the list and review the value in the State column.
AWS CLI To view the state of a Dedicated Host Use the describe-hosts command. aws ec2 describe-hosts --host-id h-012a3456b7890cdef PowerShell To view the state of a Dedicated Host Use the Get-EC2Host cmdlet.
Get-EC2Host -HostId h-012a3456b7890cdef

The following table explains the possible Dedicated Host states.
State Description available AWS hasn't detected an issue with the Dedicated Host. No maintenan ce or  repairs are scheduled. Instances can be launched onto this Dedicated Host. released The Dedicated Host has been released. The host ID is no longer in use.
 Released hosts can't be reused. under-ass essment AWS is exploring a possible issue with the Dedicated Host. If action must  be taken, you are notified via the AWS Management Console or email. Instances can't be launched onto a Dedicated Host in this state. pending The Dedicated Host can't be used for new instance launches. It is either being  modified to support  multiple instance types, or a host recovery is in  progress. permanent- failure An unrecoverable failure has been detected. You receive an  eviction notice through your instances and by email. Your instances might continue to run. If you stop or terminate all instances on a Dedicated Host with this state, AWS retires the host. AWS does not restart  ins tances in this state. Instances can't be launched onto Dedicated Hosts in  this state. released- permanent- failure AWS permanently releases Dedicated Hosts that have failed and no longer  have running instances on them. The Dedicated Host ID is no longer available for use.
### Track Amazon EC2 Dedicated Host configuration changes using AWS Config You can use AWS Config to record configuration changes for Dedicated Hosts, and for instances that are launched, stopped, or terminated on them. You can then use the information captured by AWS Config as a data source for license reporting.
AWS Config records configuration information for Dedicated Hosts and instances individually, and pairs this information through relationships. There are three reporting conditions:

- AWS Config recording status—When On, AWS Config is recording one or more AWS resource types, which can include Dedicated Hosts and Dedicated Instances. To capture the information required for license reporting, verify that hosts and instances are being recorded with the following fields.
- Host recording status—When Enabled, the configuration information for Dedicated Hosts is recorded.
- Instance recording status—When Enabled, the configuration information for Dedicated Instances is recorded.
If any of these three conditions are disabled, the icon in the Edit Config Recording button is red.
To derive the full benefit of this tool, ensure that all three recording methods are enabled. When all three are enabled, the icon is green. To edit the settings, choose Edit Config Recording. You are directed to the Set up AWS Config page in the AWS Config console, where you can set up AWS Config and start recording for your hosts, instances, and other supported resource types. For more information, see Setting up AWS Config using the Console in the AWS Config Developer Guide.
Note AWS Config records your resources after it discovers them, which might take several minutes.
After AWS Config starts recording configuration changes to your hosts and instances, you can get the configuration history of any host that you have allocated or released and any instance that you have launched, stopped, or terminated. For example, at any point in the configuration history of a Dedicated Host, you can look up how many instances are launched on that host, along with the number of sockets and cores on the host. For any of those instances, you can also look up the ID of its Amazon Machine Image (AMI). You can use this information to report on licensing for your own server-bound software that is licensed per-socket or per-core.
You can view configuration histories in any of the following ways:
- By using the AWS Config console. For each recorded resource, you can view a timeline page, which provides a history of configuration details. To view this page, choose the gray icon in the Config Timeline column of the Dedicated Hosts page. For more information, see Viewing Configuration Details in the AWS Config Console in the AWS Config Developer Guide.

- By running AWS CLI commands. First, you can use the list-discovered-resources command to get a list of all hosts and instances. Then, you can use the get-resource-config-history command to get the configuration details of a host or instance for a specific time interval.
- By using the AWS Config API in your applications. First, you can use the ListDiscoveredResources action to get a list of all hosts and instances. Then, you can use the GetResourceConfigHistory action to get the configuration details of a host or instance for a specific time interval.
For example, to get a list of all of your Dedicated Hosts from AWS Config, run a CLI command such as the following. aws configservice list-discovered-resources --resource-type AWS::EC2::Host To obtain the configuration history of a Dedicated Host from AWS Config, run a CLI command such as the following. aws configservice get-resource-config-history \ --resource-type AWS::EC2::Instance \ --resource-id i-1234567890abcdef0 To manage AWS Config settings using the console
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. On the Dedicated Hosts page, choose Edit Config Recording.
3. In the AWS Config console, follow the steps provided to turn on recording. For more information, see Setting up AWS Config using the Console.
For more information, see Viewing Configuration Details in the AWS Config Console.
To activate AWS Config using the command line or API
- AWS CLI: Viewing Configuration Details (AWS CLI) in the AWS Config Developer Guide.
- Amazon EC2 API: GetResourceConfigHistory.
## Amazon EC2 Dedicated Instances By default, EC2 instances run on shared tenancy hardware. This means that multiple AWS accounts might share the same physical hardware.

Dedicated Instances are EC2 instances that run on hardware that's dedicated to a single AWS account. This means that Dedicated Instances are physically isolated at the host hardware level from instances that belong to other AWS accounts, even if those accounts are linked to a single payer account. However, Dedicated Instances might share hardware with other instances from the same AWS account that are not Dedicated Instances.
Dedicated Instances provide no visibility or control over instance placement, and they do not support host affinity. If you stop and start a Dedicated Instance, it might not run on the same host.
Similarly, you cannot target a specific host on which to launch or run an instance. Additionally, Dedicated Instances provide limited support for Bring Your Own License (BYOL).
If you require visibility and control over instance placement and more comprehensive BYOL support, consider using a Dedicated Host instead. Dedicated Instances and Dedicated Hosts can both be used to launch Amazon EC2 instances onto dedicated physical servers. There are no performance, security, or physical differences between Dedicated Instances and instances on Dedicated Hosts. However, there are some key differences between them. The following table highlights some of the key differences between Dedicated Instances and Dedicated Hosts:

Dedicated Host Dedicated Instance Dedicated physical server Physical server with instance capacity fully dedicated to your use.
Physical server that's dedicated to a single customer account.
Instance capacity sharing Can share instance capacity with other accounts.
Not supported
##### Billing Per-host billing Per-instance billing Visibility of sockets, cores, and host ID Provides visibility of the number of sockets and physical  cores No visibility Host and instance affinity Allows you to consistently deploy your instances to the same  physical server over time Not supported

Dedicated Host Dedicated Instance Targeted instance placement Provides additional visibility and control over how instances are placed on a physical server Not supported Automatic instance recovery Supported. For more information, see Amazon EC2 Dedicated Host recovery.
Supported Bring Your Own License (BYOL)
Supported Partial support * Capacity Reservations Not supported Supported
* Microsoft SQL Server with License Mobility through Software Assurance, and Windows Virtual Desktop Access (VDA) licenses can be used with Dedicated Instance.
For more information, see Amazon EC2 Dedicated Hosts.
Contents
- Dedicated Instance basics
- Supported features
- Dedicated Instances limitations
- Pricing for Dedicated Instances
- Launch Dedicated Instances into a VPC with default tenancy
- Change the tenancy of an EC2 instance
- Change the instance tenancy of a VPC
### Dedicated Instance basics A VPC can have a tenancy of either default or dedicated. By default, your VPCs have default tenancy and instances launched into a default tenancy VPC have default tenancy. To launch Dedicated Instances, do the following:

- Create a VPC with a tenancy of dedicated, so that all instances in the VPC run as Dedicated Instances. For more information, see Launch Dedicated Instances into a VPC with default tenancy.
- Create a VPC with a tenancy of default and manually specify a tenancy of dedicated for the instances to run as Dedicated Instances. For more information, see Launch Dedicated Instances into a VPC with default tenancy.
### Supported features Dedicated Instances support the following features and AWS service integrations:
Features
- Reserved Instances
- Automatic scaling
- Automatic recovery
- Dedicated Spot Instances
- Burstable performance instances
#### Reserved Instances To reserve capacity for your Dedicated Instances, you can purchase Dedicated Reserved Instances or Capacity Reservations. For more information, see Reserved Instances for Amazon EC2 overview and Reserve compute capacity with EC2 On-Demand Capacity Reservations.
When you purchase a Dedicated Reserved Instance, you are purchasing the capacity to launch a Dedicated Instance at a much reduced usage fee; the price break in the usage charge applies only if you launch an instance with dedicated tenancy. When you purchase a Reserved Instance with default tenancy, it applies only to a running instance with default tenancy; it does not apply to a running instance with dedicated tenancy.
You can't use the modification process to change the tenancy of a Reserved Instance after you've purchased it. However, you can exchange a Convertible Reserved Instance for a new Convertible Reserved Instance with a different tenancy.
#### Automatic scaling You can use Amazon EC2 Auto Scaling to launch Dedicated Instances. For more information, see Create a launch template using advanced settings in the Amazon EC2 Auto Scaling User Guide.

#### Automatic recovery You can configure automatic recovery for a Dedicated Instance if it becomes impaired due to an underlying hardware failure or a problem that requires AWS involvement to repair. For more information, see Automatic instance recovery.
#### Dedicated Spot Instances You can run a Dedicated Spot Instance by specifying a tenancy of dedicated when you create a Spot Instance request. For more information, see Launch on single-tenant hardware.
#### Burstable performance instances You can leverage the benefits of running on dedicated tenancy hardware with the section called "Burstable performance instances". T3 Dedicated Instances launch in unlimited mode by default, and they provide a baseline level of CPU performance with the ability to burst to a higher CPU level when required by your workload. The T3 baseline performance and ability to burst are governed by CPU credits. Because of the burstable nature of the T3 instance types, we recommend that you monitor how your T3 instances use the CPU resources of the dedicated hardware for the best performance. T3 Dedicated Instances are intended for customers with diverse workloads that display random CPU behavior, but that ideally have average CPU usage at or below the baseline usages. For more information, see the section called "Key concepts".
Amazon EC2 has systems in place to identify and correct variability in performance. However, it is still possible to experience short-term variability if you launch multiple T3 Dedicated Instances that have correlated CPU usage patterns. For these more demanding or correlated workloads, we recommend using M5 or M5a Dedicated Instances rather than T3 Dedicated Instances.
### Dedicated Instances limitations Keep the following in mind when using Dedicated Instances:
- Some AWS services or their features are not supported with a VPC with the instance tenancy set to dedicated. Refer to the respective service's documentation to confirm if there are any limitations.
- Some instance types can't be launched into a VPC with the instance tenancy set to dedicated.
For more information about supported instance types, see Amazon EC2 Dedicated Instances.
- When you launch a Dedicated Instance backed by Amazon EBS, the EBS volume doesn't run on single-tenant hardware.

### Pricing for Dedicated Instances Pricing for Dedicated Instances is different from pricing for On-Demand Instances. For more information, see the Amazon EC2 Dedicated Instances.
### Launch Dedicated Instances into a VPC with default tenancy When you create a VPC, you have the option of specifying its instance tenancy. If you launch an instance into a VPC that has an instance tenancy of dedicated, it runs as a Dedicated Instance on hardware that's dedicated for your use.
For more information about launching an instance with a tenancy of host, see Launch Amazon EC2 instances on an Amazon EC2 Dedicated Host.
For more information about VPC tenancy options, see Create a VPC in the Amazon VPC User Guide.
Requirements
- Choose a supported instance type. For more information, see Amazon EC2 Dedicated Instances.
Console To launch a Dedicated Instance into a default tenancy VPC
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Instances, Launch instance.
3. In the Application and OS Images section, select an AMI from the list.
4. In the Instance type section, select the instance type to launch.
5. In the Key pair section, select the key pair to associate with the instance.
6. In the Advanced details section, for Tenancy, select Dedicated.
7. Configure the remaining instance options as needed. For more information, see Reference for Amazon EC2 instance configuration parameters.
8. Choose Launch instance.
AWS CLI To set the tenancy option for an instance during launch Use the run-instances command and include Tenancy with the --placement option.

--placement Tenancy=dedicated PowerShell To set the tenancy option for an instance during launch Use the New-EC2Instance cmdlet with the -Placement_Tenancy parameter.
-Placement_Tenancy dedicated
### Change the tenancy of an EC2 instance You can change the tenancy of a stopped instance after launch. The changes that you make take effect the next time the instance starts.
Alternatively, you can change the tenancy of your virtual private cloud (VPC). For more information, see the section called "Change the tenancy of a VPC".
Limitations
- You can't change the tenancy of an instance using the AWS Management Console.
- The instance must be in the stopped state.
- The operating system details of your instance—and whether SQL Server is installed—affect what conversions are supported. For more information about the tenancy conversion paths available to your instance, see Tenancy conversion in the License Manager User Guide.
- For T3 instances, you must launch the instance on a Dedicated Host to use a tenancy of host.
You can't change the tenancy from host to dedicated or default. Attempting to make one of these unsupported tenancy changes results in an InvalidRequest error code.
AWS CLI To modify the tenancy value of an instance Use the  modify-instance-placement command. aws ec2 modify-instance-placement \ --instance-id i-1234567890abcdef0 \ --tenancy dedicated

PowerShell To modify the tenancy value of an instance Use the  Edit-EC2InstancePlacement cmdlet.
Edit-EC2InstancePlacement `
    -InstanceId i-1234567890abcdef0 `
    -Tenancy Dedicated
### Change the instance tenancy of a VPC You can change the instance tenancy of a virtual private cloud (VPC) from dedicated to default after you create it. Modifying the instance tenancy of a VPC does not affect the tenancy of any existing instances in the VPC. The next time that you launch an instance in the VPC, it has a tenancy of default, unless you specify otherwise during instance launch.
Alternatively, you can change the tenancy of specific instances. For more information, see the section called "Change the tenancy of an instance".
Limitations
- You can't change the instance tenancy of a VPC from default to dedicated after it is created.
- You can't modify the instance tenancy of a VPC using the AWS Management Console.
AWS CLI To modify the instance tenancy attribute of a VPC Use the modify-vpc-tenancy command. The only supported tenancy value is default. aws ec2 modify-vpc-tenancy \ --vpc-id vpc-1234567890abcdef0 \ --instance-tenancy default PowerShell To modify the instance tenancy attribute of a VPC Use the Edit-EC2VpcTenancy cmdlet. The only supported tenancy value is Default.

Edit-EC2VpcTenancy `
    -VpcId vpc-1234567890abcdef0 `
    -InstanceTenancy Default
## On-Demand Capacity Reservations and Capacity Blocks for ML Capacity Reservations allow you to reserve compute capacity for Amazon EC2 instances in a specific Availability Zone. There are two types of Capacity Reservations serving different use cases.
Types of Capacity Reservations
- On-Demand Capacity Reservations
- Capacity Blocks for ML The following are some common use cases for On-Demand Capacity Reservations:
- Scaling events – Create On-Demand Capacity Reservations ahead of your business-critical events to ensure that you can scale when you need to.
- Regulatory requirements and disaster recovery – Use On-Demand Capacity Reservations to satisfy regulatory requirements for high availability, and reserve capacity in a different Availability Zone or Region for disaster recovery.
- Sharing unused capacity – Use Interruptible Capacity Reservations to make unused capacity available for other workloads within your account while maintaining control to reclaim it when needed.
The following are some common use cases for Capacity Blocks for ML:
- Machine learning (ML) model training and fine-tuning – Get uninterrupted access to the GPU instances that you reserved to complete ML model training and fine-tuning.
- ML experiments and prototypes – Run experiments and build prototypes that require GPU instances for short durations.
When to use On-Demand Capacity Reservation Use On-Demand Capacity Reservations if you have strict capacity requirements, and your current or future business-critical workloads require capacity assurance. With On-Demand Capacity

Reservations, you can ensure that you'll always have access to the Amazon EC2 capacity you've reserved for as long as you need it.
When to use Capacity Blocks for ML Use Capacity Blocks for ML when you need to ensure that you have uninterrupted access to GPU instances for a defined period of time starting on a future date. Capacity Blocks are ideal for training and fine-tuning ML models, short experimentation runs, and handling temporary surges in inference demand in the future. With Capacity Blocks, you can ensure that you'll have access to GPU resources on a specific date to run your ML workloads.
### Reserve compute capacity with EC2 On-Demand Capacity Reservations Amazon EC2 Capacity Reservations allow you to reserve compute capacity for your Amazon EC2 instances in a specific Availability Zone for any duration. If you have strict capacity requirements for current or future business-critical workloads that require a certain level of long or short-term capacity assurance, we recommend that you create a Capacity Reservation to help ensure that you always have access to Amazon EC2 capacity when you need it, for as long as you need it.
You can create a Capacity Reservation at any time, and you can choose when it starts. You can request a Capacity Reservation for immediate use or you can request a Capacity Reservation for a future date.
- If you request a Capacity Reservation for immediate use, the Capacity Reservation becomes available for use immediately and there is no term commitment. You can modify the Capacity Reservation at any time, and you can cancel it at any time to release the reserved capacity and to stop incurring charges.
- If you request a future-dated Capacity Reservation, you specify the future date at which you need the Capacity Reservation to become available for use. You must also specify a commitment duration for which you commit to keeping the requested capacity in your account after the specified date. At the requested date and time, the Capacity Reservation becomes available for use and the commitment duration starts. During the commitment duration, you can't decrease the instance count or commitment duration below your initial commitment, or cancel the Capacity Reservation. After the commitment duration elapses, you can modify the Capacity Reservation in any way or cancel it if you no longer need it.
Capacity Reservations can only be used by instances that match their attributes. By default, Capacity Reservations automatically match new instances and running instances that have

matching attributes (instance type, platform, Availability Zone, and tenancy). This means that any instance with matching attributes automatically runs in the Capacity Reservation. However, you can also target a Capacity Reservation for specific workloads. This allows you to explicitly control which instances are allowed to run in that reserved capacity. You can also specify that instances will only run in a Capacity Reservation or Capacity Reservation resource group.
Important Future-dated Capacity Reservations are for helping you launch and cover incremental instances, and not to cover existing running instances. If you need to cover existing running instances, use Capacity Reservations that start immediately instead.
All supported Amazon EC2 instances with matching attributes, that is instance type, platform, Availability Zone, and tenancy, are eligible to run in a Capacity Reservation. The Amazon EC2 instance can be launched by you (non-managed instances) or on your behalf by an AWS service (managed instances). This is particularly true for open Capacity Reservations, which automatically match with any running instances that have matching attributes. For example, managed instances launched on your behalf by the following services are eligible to run in Capacity Reservations that you create and manage.
- Amazon EC2 Auto Scaling
- Amazon ECS
- Amazon EKS
- Amazon EMR
- Amazon SageMaker AI
- AWS Batch
- AWS Elastic Beanstalk
- AWS ParallelCluster
- AWS Parallel Computing Service (AWS PCS)
Contents
- Concepts for Amazon EC2 Capacity Reservations
- Differences between Capacity Reservations, Reserved Instances, and Savings Plans
- Supported platforms

- Quotas
- Limitations
- Capacity Reservation pricing and billing
- Create a Capacity Reservation
- View the state of a Capacity Reservation
- Launch instances into an existing Capacity Reservation
- Modify an active Capacity Reservation
- Modify the Capacity Reservation settings of your instance
- Move capacity between Capacity Reservations
- Split off capacity from an existing Capacity Reservation
- Cancel a Capacity Reservation
- Use Capacity Reservations with cluster placement groups
- Capacity Reservation groups
- Capacity Reservations in Local Zones
- Capacity Reservations in Wavelength Zones
- Capacity Reservations on AWS Outposts
- Shared Capacity Reservations
- Capacity Reservation Fleets
- Monitor Capacity Reservations usage with CloudWatch metrics
- Monitor Capacity Reservation underutilization
- Monitor state changes for future-dated Capacity Reservations
- Interruptible Capacity Reservations
#### Concepts for Amazon EC2 Capacity Reservations The following key concepts apply to Capacity Reservations.
Topics
- Start date and time
- End date and time
- Commitment duration
- Future-dated Capacity Reservation assessment

- Capacity Reservation attributes
- Instance matching criteria
##### Start date and time The start date and time defines when the Capacity Reservation becomes available for use. A Capacity Reservation can start immediately, or it can start at a future date.
- If you choose to start a Capacity Reservation immediately, the reserved capacity becomes available for use immediately after you create it, and billing starts as soon as the Capacity Reservation enters the active state. You do not need to enter into any term commitments. You can modify the Capacity Reservation as needed at any time to meet your needs, and you can cancel it at any time to release the capacity and to stop incurring charges.
- If you choose to start a Capacity Reservation at a future date, you specify a future date and time at which you will need the reserved capacity, and a commitment duration, which is the minimum duration for which you commit to keeping the requested Capacity Reservation in your account after it has been provisioned. At the specified future date, the Capacity Reservation becomes available for use and billing starts at that time, once the Capacity Reservation enters the active state. The commit duration starts as soon as the Capacity Reservation is provisioned in your account. During this time, you can't decrease the instance count below the committed instance count, choose an end date that is before the commitment duration, or cancel the Capacity Reservation. However, after the commitment duration lapses, you are free to modify the Capacity Reservation in any way, or cancel it to release the reserved capacity and to stop incurring charges.
##### End date and time The end date and time defines when the Capacity Reservation ends and the reserved capacity is released from your account. You can configure a Capacity Reservation to end automatically at a specific date and time, or you can configure it to stay active indefinitely until you  manually cancel it.
If you configure a Capacity Reservation to end automatically, the Capacity Reservation expires within an hour of the specified time. For example, if you specify 5/31/2019, 13:30:55, the Capacity Reservation is guaranteed to end between 13:30:55 and 14:30:55 on 5/31/2019.
After a reservation ends, the reserved capacity is released from your account and you can no longer target instances to the Capacity Reservation. Instances running in the reserved capacity continue to

run uninterrupted. If instances targeting a Capacity Reservation are stopped, you can't restart them until you remove their Capacity Reservation targeting preference or configure them to target a different Capacity Reservation. For more information, see Modify the Capacity Reservation settings of your instance.
##### Commitment duration The commitment duration applies to future-dated Capacity Reservations only.
The commitment duration is a minimum duration for which you commit to having the future-dated Capacity Reservation in the active state in your account after it has been provisioned. You can keep a future-dated Capacity Reservation for longer than the commitment duration, but not shorter.
The following apply during the commitment duration:
- You can't cancel a Capacity Reservation during the commitment duration.
- You can't decrease the instance count below the committed instance count, but you can increase it.
- You can't configure a Capacity Reservation to automatically end at a date or time that is within the commitment duration. You can extend the end date and time during the commitment period.
Amazon EC2 uses the commitment duration that you specify to assess whether the request can be supported. The minimum commitment duration is 14 days. While assessing a request, Amazon EC2 might determine that it can support a shorter commitment duration. In that case, Amazon EC2 will schedule the future-dated Capacity Reservation with the shorter commitment duration. This means that you are committed to keeping the Capacity Reservation in your account for a shorter period than you initially requested.
##### Future-dated Capacity Reservation assessment When you request a future-dated Capacity Reservation, Amazon EC2 assesses the request to determine whether it can be supported based on capacity availability and the commitment duration you specify. The assessment is typically completed within 5 days. Amazon EC2 considers multiple factors when evaluating a request, including:
- Forecasted capacity supply
- The commitment duration
- How early you request the Capacity Reservation relative to your start date
- The size of your request

You can request a future-dated Capacity Reservation between 5 and 120 days in advance. We recommend that you make the request at least 56 days (8 weeks) in advance to improve our ability to support your request. The minimum commitment duration is 14 days and the minimum instance count is 32 vCPUs.
The Capacity Reservation remains in the assessing state while the request is being assessed.
If the request can be supported, the Capacity Reservation enters the scheduled state and it is scheduled for delivery on the requested date and time. The total instance count remains 0 during while the Capacity Reservation is in the scheduled state. A scheduled Capacity Reservation will become active and available for use at the requested date.
If a request can't be supported, the Capacity Reservation enters the unsupported state.
Unsupported Capacity Reservations are not delivered.
You can cancel a future-dated Capacity Reservation while it is in the assessing state.
For more information, see Create a future-dated Capacity Reservation.
##### Capacity Reservation attributes When you create a Capacity Reservation, you must specify the following attributes:
- Availability Zone
- Instance type
- Platform (operating system type)
- Tenancy (default or dedicated)
Only instances that match these attributes can launch or run in the Capacity Reservation.
##### Instance matching criteria Instance matching criteria, or instance eligibility, determines which instances are allowed to launch and run in the Capacity Reservation. A Capacity Reservation can have one of the following matching criteria:
- Open — The Capacity Reservation automatically matches all instances that have matching attributes (instance type, platform, and Availability Zone). New and existing instances that have matching attributes automatically run in the Capacity Reservation without any additional configuration.

- Targeted — The Capacity Reservation accepts only instances that have matching attributes (instance type, platform, and Availability Zone), and that explicitly target the Capacity Reservation. The instance must specifically target the Capacity Reservation to launch or run in its reserved capacity. This allows you to explicitly control which instances are allowed to run in the reserved capacity and helps you avoid unintentional reserved capacity usage.
When you request a future-dated Capacity Reservation, you can specify only targeted matching criteria. This ensures that the capacity delivered by the Capacity Reservation is incremental, or additional, to any running instances or reserved capacity that you have at the time of delivery.
After the Capacity Reservation becomes active in your account, you can change the instance matching criteria to open if needed. However, keep in mind that any matching instances will automatically run in the Capacity Reservation, which could lead to unintentional capacity usage and prevent you from launching new instances for the full requested instance count.
#### Differences between Capacity Reservations, Reserved Instances, and Savings Plans The following table highlights key differences between Capacity Reservations, Reserved Instances, and Savings Plans:

Capacity Reservati ons Zonal Reserved Instances Regional Reserved Instances Savings Plans Term No commitmen t required for immediate-use Capacity Reservati ons. They can be created, modified, and canceled as needed.
With future-dated Capacity Reservati ons, you specify a commitmen t duration for which you commit to keeping the Requires a fixed one-year or three-year commitment

Capacity Reservati ons Zonal Reserved Instances Regional Reserved Instances Savings Plans capacity in your account. After the  commitment duration elapses, you can cancel the Capacity Reservati on at any  time.
Capacity benefit Capacity reserved in a specific Availabil ity  Zone.
No capacity reserved.
##### Billing discount No billing discount. † Provides a billing discount.
Instance Limits Your On-Demand Instance limits per Region apply.
Default is 20 per Availability Zone.
You can request a limit  increase.
Default is 20 per Region. You can request a limit increase.
No limit.
† You can combine Capacity Reservations with Savings Plans or Regional Reserved Instances to receive a discount.
For more information, see the following:
- Reserved Instances for Amazon EC2 overview
- Savings Plans User Guide Supported platforms You must create the Capacity Reservation with the correct platform to ensure that it properly matches with your instances. Capacity Reservations support the following values for platform:
- Linux/UNIX
- Linux with SQL Server Standard
- Linux with SQL Server Web

- Linux with SQL Server Enterprise
- SUSE Linux
- Red Hat Enterprise Linux
- RHEL with SQL Server Standard
- RHEL with SQL Server Enterprise
- RHEL with SQL Server Web
- RHEL with HA
- RHEL with HA and SQL Server Standard
- RHEL with HA and SQL Server Enterprise
- Ubuntu Pro
- Windows
- Windows with SQL Server
- Windows with SQL Server Web
- Windows with SQL Server Standard
- Windows with SQL Server Enterprise To ensure that an instance runs in a specific Capacity Reservation, the platform of the Capacity Reservation must match the platform of the AMI used to launch the instance. For Linux AMIs, it is important to check whether the AMI platform uses the general value Linux/UNIX or a more specific value like SUSE Linux.
Console To check the AMI platform
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose AMIs.
3. Select the AMI.
4. On the Details tab, note the value of Platform details.
AWS CLI To check the AMI platform

Use the describe-images command and check the value of PlatformDetails. aws ec2 describe-images \ --image-ids ami-0abcdef1234567890 \ --query Images[*].PlatformDetails The following is example output.
[ "Linux/UNIX"
]
PowerShell To check the AMI platform Use the Get-EC2Image cmdlet and check the value of PlatformDetails.
Get-EC2Image `
    -ImageId ami-0abcdef1234567890 | `
    Select PlatformDetails The following is example output.
PlatformDetails
--------------- Linux/UNIX
#### Quotas The number of instances for which you are allowed to reserve capacity is based on your account's On-Demand Instance quota. You can reserve capacity for as many instances as that quota allows, minus the number of instances that are already running.
Capacity Reservations in the assessing, scheduled, pending , active, and delayed state count towards your On-Demand Instance quota.
Limitations Before you create Capacity Reservations, take note of the following limitations and restrictions.

- Active and unused Capacity Reservations count toward your On-Demand Instance limits.
- Capacity Reservations are not transferable from one AWS account to another. However, you can share Capacity Reservations with other AWS accounts. For more information, see Shared Capacity Reservations.
- Zonal Reserved Instance billing discounts do not apply to Capacity Reservations.
- Capacity Reservations can be created in cluster placement groups. Spread and partition placement groups are not supported.
- Capacity Reservations can't be used with Dedicated Hosts. Capacity Reservations can be used with Dedicated Instances.
- [Windows instances] Capacity Reservations can't be used with Bring Your Own License (BYOL).
- [Red Hat instances] Capacity Reservations can be used with Bring Your Own License (BYOL).
- Capacity Reservations do not ensure that a hibernated instance can resume after you try to start it.
- You can request future-dated Capacity Reservations for an instance count with a minimum of 32 vCPUs. For example, if you request a future-dated Capacity Reservation for m5.xlarge instances, you must request at least 8 instances (8 * m5.xlarge = 32 vCPUs).
- You can request future-dated Capacity Reservations for instance types in the following series only: C, G, I, M, R, and T.
#### Capacity Reservation pricing and billing The topics in this section provide an overview of pricing and billing for Capacity Reservations.
Topics
- Pricing
- Billing
- Billing discounts
- Viewing your bill
##### Pricing Capacity Reservations are charged at the equivalent On-Demand rate whether you run instances in reserved capacity or not, including any applicable regional surcharge for Dedicated Instances. If you do not use the reservation, this shows up as unused reservation on your Amazon EC2 bill. When

you run an instance that matches the attributes of a reservation, you just pay for the instance and nothing for the reservation. There are no upfront or additional charges.
For example, if you create a Capacity Reservation for 20 m4.large Linux instances and run 15 m4.large Linux instances in the same Availability Zone, you will be charged for 15 active instances and for 5 unused instances in the reservation.
Billing discounts for Savings Plans and Regional Reserved Instances apply to Capacity Reservations.
For more information, see Billing discounts.
For more information, see Amazon EC2 Pricing.
##### Billing Billing starts as soon as the Capacity Reservation is provisioned in your account, and it continues while the Capacity Reservation remains provisioned in your account. For future-dated Capacity Reservations, this means that billing starts only once the Capacity Reservation is provisioned in your account at the requested future date.
Capacity Reservations are billed at per-second granularity. This means that you are charged for partial hours. For example, if a Capacity Reservation remains provisioned in your account for 24 hours and 15 minutes, you are billed for 24.25 reservation hours.
The following example shows how a Capacity Reservation is billed. The Capacity Reservation is created for one m4.large Linux instance, which has an On-Demand rate of $0.10 per usage hour.
In this example, the Capacity Reservation is provisioned in the account for five hours. The Capacity Reservation is unused for the first hour, so it is billed for one unused hour at the m4.large instance type's standard On-Demand rate. In hours two through five, the Capacity Reservation is occupied by an m4.large instance. During this time, the Capacity Reservation accrues no charges, and the account is instead billed for the m4.large instance occupying it. In the sixth hour, the Capacity Reservation is canceled and the m4.large instance runs normally outside of the reserved capacity. For that hour, it is charged at the On-Demand rate of the m4.large instance type.

##### Billing discounts Billing discounts for Savings Plans and Regional Reserved Instances apply to Capacity Reservations.
AWS automatically applies these discounts to Capacity Reservations that have matching attributes. When a Capacity Reservation is used by an instance, the discount is applied to the instance. Discounts are preferentially applied to instance usage before covering unused Capacity Reservations.
Billing discounts for zonal Reserved Instances do not apply to Capacity Reservations.
For more information, see the following:
- Reserved Instances for Amazon EC2 overview
- Savings Plans User Guide
- Billing and purchase options
##### Viewing your bill You can review the charges and fees to your account on the AWS Billing and Cost Management console.
- The Dashboard displays a spend summary for your account.
- On the Bills page, under Details, expand the Elastic Compute Cloud section and the Region to get billing information about your Capacity Reservations.
You can view the charges online, or you can download a CSV file. For more information, see Capacity Reservation line items.
#### Create a Capacity Reservation You can create a Capacity Reservation at any time to ensure that you have compute capacity available in a specific Availability Zone. A Capacity Reservation can start immediately, or it can start at a future date. The capacity becomes available for use only once the Capacity Reservation enters the active state.
Note If you create a Capacity Reservation with open instance matching criteria, and you have running instances with matching attributes at the time the Capacity Reservation becomes

active, those instances automatically run in the reserved capacity. To avoid this, use targeted instance matching criteria. For more information, see Instance matching criteria.
Your request to create a Capacity Reservation could fail if one of the following is true:
- Amazon EC2 does not have sufficient capacity to fulfill the request. Either try again at a later time, try a different Availability Zone, or try a smaller request. If your application is flexible across instance types and sizes, try different instance attributes.
- The requested quantity exceeds your On-Demand Instance limit for the selected instance family. Increase your On-Demand Instance limit for the instance family and try again. For more information, see On-Demand Instance quotas.
Topics
- Create a Capacity Reservation for immediate use
- Create a future-dated Capacity Reservation
##### Create a Capacity Reservation for immediate use You create a Capacity Reservation for immediate use.
Console To create a Capacity Reservation
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. Choose Capacity Reservations, and then choose Create Capacity Reservation.
3. Configure the following settings in the Instance details section. a.
Instance Type — The instance type for which to reserve capacity. b.
Platform — The operating system for your instances. For more information, see Supported platforms. c.
Availability Zone — The Availability Zone in which to reserve the capacity. d.
Tenancy — The type of tenancy to use for the reserved capacity. Choose Default to reserve capacity on shared hardware, or Dedicated to reserve capacity on hardware that is dedicated to your account.

e.
(Optional) Placement group ARN — The ARN of the cluster placement group in which to create the Capacity Reservation. For more information, see Use Capacity Reservations with cluster placement groups. f.
Total instance count — The number of instances for which to reserve capacity. If you specify a quantity that exceeds your remaining On-Demand Instance quota for the selected instance type, the request fails.
4. Configure the following settings in the Reservation details section: a.
Capacity Reservation starts — Choose Immediately. b.
Capacity Reservation ends — Choose one of the following options:
- Manually — Reserve the capacity until you explicitly cancel it.
- Specific time — Cancel the capacity reservation automatically at the specified date and time. c.
Instance eligibility — Choose one of the following options:
- open — (Default) The Capacity Reservation matches any instance that has matching attributes (instance type, platform, Availability Zone, and tenancy). If you launch an instance with matching attributes, it is placed into the reserved capacity automatically.
- targeted — The Capacity Reservation only accepts instances that have matching attributes (instance type, platform, Availability Zone, and tenancy), and that explicitly target the reservation.
5. Choose Create.
AWS CLI To create a Capacity Reservation Use the create-capacity-reservation command. aws ec2 create-capacity-reservation \ --availability-zone az_name \ --instance-type instance_type \ --instance-count number_of_instances \ --instance-platform operating_system \ --instance-match-criteria open|targeted

PowerShell To create a Capacity Reservation Use the Add-EC2CapacityReservation cmdlet.
Add-EC2CapacityReservation `
    -AvailabilityZone az_name `
    -InstanceType instance_type `
    -InstanceCount number_of_instances `
    -InstancePlatform operating_system `
    -InstanceMatchCriterion open|targeted
##### Create a future-dated Capacity Reservation Request a future-dated Capacity Reservation if you need the reserved capacity to become available at a future date and time.
After you request a future-dated Capacity Reservation, the request undergoes an assessment to determine whether it can be supported. For more information, see Future-dated Capacity Reservation assessment.
#### Considerations
- You can request future-dated Capacity Reservations for instance types in the following series: C, G, I, M, R, and T.
- You can request future-dated Capacity Reservations for an instance count with a minimum of 32 vCPUs. For example, if you request a future-dated Capacity Reservation for m5.xlarge instances, you must request capacity for at least 8 instances (8 * m5.xlarge = 32 vCPUs).
- You can request a future-dated Capacity Reservation between 5 and 120 days in advance.
However, we recommend that you request it at least 56 days (8 weeks) in advance to improve supportability.
- The minimum commitment duration is 14 days.
Console To create a Capacity Reservation
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.

2. Choose Capacity Reservations, and then choose Create Capacity Reservation.
3. Configure the following settings in the Instance details section. a.
Instance Type — The instance type for which to reserve capacity. b.
Platform — The operating system for your instances. For more information, see Supported platforms. c.
Availability Zone — The Availability Zone in which to reserve the capacity. d.
Tenancy — The type of tenancy to use for the reserved capacity. Choose Default to reserve capacity on shared hardware, or Dedicated to reserve capacity on hardware that is dedicated to your account. e.
Total instance count — The number of instances for which to reserve capacity. If you specify a quantity that exceeds your remaining On-Demand Instance quota for the selected instance type, the request fails.
4. Configure the following settings in the Reservation details section: a.
Capacity Reservation starts — Choose At a specific time. b.
Start date — Specify the date and time at which the Capacity Reservation must become available for use. For more information, see Start date and time. c.
Commitment duration — Specify the minimum duration for which you commit keeping the Capacity Reservation after it has been delivered. For more information, see Commitment duration. d.
Capacity Reservation ends — Choose one of the following options:
- When I cancel it — Reserve the capacity until you explicitly cancel it.
- Specific time — Cancel the capacity reservation automatically at the specified date and time.
5. Choose Create.
AWS CLI To create a Capacity Reservation Use the create-capacity-reservation command. aws ec2 create-capacity-reservation \ --availability-zone az_name \

    --instance-type instance_type \ --instance-count number_of_instances \ --instance-platform operating_system \ --instance-match-criteria targeted \ --delivery-preference incremental \ --commitment-duration commitment_in_seconds \ --start-date YYYY-MMDDThh:mm:ss.sssZ PowerShell To create a Capacity Reservation Use the Add-EC2CapacityReservation cmdlet.
Add-EC2CapacityReservation `
    -AvailabilityZone az_name `
    -InstanceType instance_type `
    -InstanceCount number_of_instances `
    -InstancePlatform operating_system `
    -InstanceMatchCriterion targeted `
    -DeliveryPreference incremental `
    -CommitmentDuration commitment_in_seconds `
    -StartDate   YYYY-MMDDThh:mm:ss.sssZ
#### View the state of a Capacity Reservation Amazon EC2 constantly monitors the state of your Capacity Reservations.
Due to the eventual consistency model followed by the Amazon EC2 API, after you create a Capacity Reservation, it can take up to 5 minutes for the state of the Capacity Reservation to reflect that it is active. During this time, the Capacity Reservation might remain in the pending state. However, it might already be available for use, in which case attempts to launch instances into the Capacity Reservation would succeed.
Console To view your Capacity Reservations
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Capacity Reservations.
3. Select the Capacity Reservation.

AWS CLI To describe your Capacity Reservations Use the describe-capacity-reservations command.
For example, the following command describes all Capacity Reservations. aws ec2 describe-capacity-reservations The following is example output.
{ "CapacityReservations": [ { "CapacityReservationId": "cr-1234abcd56EXAMPLE", "EndDateType": "unlimited", "AvailabilityZone": "eu-west-1a", "InstanceMatchCriteria": "open", "Tags": [], "EphemeralStorage": false, "CreateDate": "2019-08-16T09:03:18.000Z", "AvailableInstanceCount": 1, "InstancePlatform": "Linux/UNIX", "TotalInstanceCount": 1, "State": "active", "Tenancy": "default", "EbsOptimized": true, "InstanceType": "a1.medium", "PlacementGroupArn": "arn:aws:ec2:us-east-1:123456789012:placement- group/MyPG"
        }, { "CapacityReservationId": "cr-abcdEXAMPLE9876ef", "EndDateType": "unlimited", "AvailabilityZone": "eu-west-1a", "InstanceMatchCriteria": "open", "Tags": [], "EphemeralStorage": false, "CreateDate": "2019-08-07T11:34:19.000Z", "AvailableInstanceCount": 3, "InstancePlatform": "Linux/UNIX", "TotalInstanceCount": 3,

            "State": "cancelled", "Tenancy": "default", "EbsOptimized": true, "InstanceType": "m5.large"
        } ]
} PowerShell To describe a Capacity Reservation Use the Get-EC2CapacityReservation cmdlet.
Get-EC2CapacityReservation `
    -CapacityReservationId cr-1234abcd56EXAMPLE
##### Capacity Reservation states Capacity Reservations have the following possible states.
State Description active The capacity is available for use. expired The Capacity Reservation expired automatically at the date and time specified in your  reservation request. The reserved capacity is no longer available for  your use. cancelled The Capacity Reservation was canceled. The reserved capacity is no longer available for your use. pending The Capacity Reservation request was successful but the capacity provisioning is  still pending. failed The Capacity Reservation request has failed. A request can fail due to request  parameters that are not valid, capacity constraints, or instance limit  constraints. You can view a failed request for 60 minutes.

State Description scheduled (Future-dated Capacity Reservations only) The future-dated Capacity Reservation  request was approved and the Capacity Reservation is scheduled for delivery on the  requested start date. assessing (Future-dated Capacity Reservations only) Amazon EC2 is assessing your request for a future-dated Capacity Reservation. For more information, see Future-dated Capacity Reservation assessment. delayed (Future-dated Capacity Reservations only) Amazon EC2 encountered a delay in provisioning the requested future-dated Capacity Reservati on. Amazon EC2 is unable  to deliver the requested capacity by the requested start date and  time. unsupported (Future-dated Capacity Reservations only) Amazon EC2 can't support the future-dated Capacity Reservation request due to capacity constraints. You can view  unsupported requests for 30 days. The Capacity Reservation will not be  delivered.
#### Launch instances into an existing Capacity Reservation You can only launch an instance into a Capacity Reservation that:
- Has matching attributes (instance type, platform, Availability Zone, and tenancy)
- Has sufficient available capacity
- Is in the active state When you launch an instance, you can specify whether to launch the instance into any open Capacity Reservation, into a specific Capacity Reservation, or into a group of Capacity Reservations.
Alternatively, you can configure the instance to avoid running in a Capacity Reservation, even if you have an open Capacity Reservation that has matching attributes and available capacity.
Launching an instance into a Capacity Reservation reduces its available capacity by the number of instances launched. For example, if you launch three instances, the available capacity of the Capacity Reservation is reduced by three.

Console To launch instances into an existing Capacity Reservation
1. Follow the procedure to launch an instance, but don't launch the instance until you've completed the following steps to specify the settings for the placement group and Capacity Reservation.
2. Expand Advanced details and do the following: a.
For Placement group, select the cluster placement group in which to launch the instance. b.
For Capacity Reservation, choose one of the following options depending on the configuration of the Capacity Reservation:
- None – Prevents the instances from launching into a Capacity Reservation. The instances run in On-Demand capacity.
- Open – Launches the instances into any Capacity Reservation that has matching attributes and sufficient capacity for the number of instances you selected. If there is no matching Capacity Reservation with sufficient capacity, the instance uses On- Demand capacity.
- Specify Capacity Reservation – Launches the instances into the selected Capacity Reservation. If the selected Capacity Reservation does not have sufficient capacity for the number of instances you selected, the instance launch fails.
- Specify Capacity Reservation resource group – Launches the instances into any Capacity Reservation with matching attributes and available capacity in the selected Capacity Reservation group. If the selected group does not have a Capacity Reservation with matching attributes and available capacity, the instances launch into On-Demand capacity.
- Specify Capacity Reservation only – Launches the instances into a Capacity Reservation. If a Capacity Reservation ID isn't specified, the instances launch into an open Capacity Reservation. If capacity isn't available, the instances fail to launch.
- Specify Capacity Reservation resource group only – Launches the instances into a Capacity Reservation in a Capacity Reservation resource group. If a Capacity Reservation resource group ARN isn't specified, the instances launch into an open Capacity Reservation. If capacity isn't available, the instances fail to launch.

3. In the Summary panel, review your instance configuration, and then choose Launch instance.
AWS CLI To launch an instance into an existing Capacity Reservation Use the run-instances command and specify the --capacity-reservation- specification option.
The following example launches an instance into any open Capacity Reservation with matching attributes and available capacity: aws ec2 run-instances \ --image-id ami-0abcdef1234567890 \ --count 1 \ --instance-type t2.micro \ --key-name my-key-pair \ --subnet-id subnet-0abcdef1234567890 \ --capacity-reservation-specification CapacityReservationPreference=open The following example launches an instance into a targeted Capacity Reservation: aws ec2 run-instances \ --image-id ami-0abcdef1234567890 \ --count 1 \ --instance-type t2.micro \ --key-name my-key-pair \ --subnet-id subnet-0abcdef1234567890 \ --capacity-reservation-specification \ CapacityReservationTarget={CapacityReservationId=cr-1234abcd56EXAMPLE} The following example launches an instance into the specified Capacity Reservation group: aws ec2 run-instances \ --image-id ami-0abcdef1234567890 \ --count 1 \ --instance-type t2.micro \ --key-name my-key-pair \ --subnet-id subnet-0abcdef1234567890 \ --capacity-reservation-specification \

 CapacityReservationTarget={CapacityReservationResourceGroupArn=arn:aws:resource- groups:us-west-2:123456789012:group/my-cr-group} The following example launches an instance into a Capacity Reservation only. Because it does not specify a Capacity Reservation ID, the instance launches in any open Capacity Reservation with matching attributes and available capacity: aws ec2 run-instances \ --image-id ami-0abcdef1234567890 \ --count 1 \ --instance-type t2.micro \ --key-name my-key-pair \ --subnet-id subnet-0abcdef1234567890 \ --capacity-reservation-specification \ CapacityReservationPreference=capacity-reservations-only The following example launches an instance into a specific Capacity Reservation only. If capacity isn't available in the specified Capacity Reservation, the instance fails to launch. aws ec2 run-instances \ --image-id ami-0abcdef1234567890 \ --count 1 \ --instance-type t2.micro \ --key-name my-key-pair \ --subnet-id subnet-0abcdef1234567890 \ --capacity-reservation-specification \ CapacityReservationPreference=capacity-reservations-only \ CapacityReservationTarget={CapacityReservationId=cr-1234abcd56EXAMPLE} PowerShell To launch an instance into an existing Capacity Reservation Use the New-EC2Instance cmdlet.
The following example launches an instance into any open Capacity Reservation with matching attributes and available capacity:
New-EC2Instance `
    -ImageId ami-0abcdef1234567890 `

    -InstanceType t2.micro `
    -KeyName "my-key-pair" `
    -SubnetId subnet-0abcdef1234567890 `
    -CapacityReservationSpecification_CapacityReservationPreference "open"
The following example launches an instance into a targeted Capacity Reservation:
New-EC2Instance `
    -ImageId ami-0abcdef1234567890 `
    -InstanceType t2.micro `
    -KeyName "my-key-pair" `
    -SubnetId subnet-0abcdef1234567890 `
    -CapacityReservationTarget_CapacityReservationId cr-1234abcd56EXAMPLE The following example launches an instance into the specified Capacity Reservation group:
New-EC2Instance `
    -ImageId ami-0abcdef1234567890 `
    -InstanceType t2.micro `
    -KeyName "my-key-pair" `
    -SubnetId subnet-0abcdef1234567890 `
    -CapacityReservationTarget_CapacityReservationResourceGroupArn `
        "arn:aws:resource-groups:us-west-2:123456789012:group/my-cr-group"
The following example launches an instance into a Capacity Reservation only. Because it does not specify a Capacity Reservation ID, the instance launches in any open Capacity Reservation with matching attributes and available capacity:
New-EC2Instance `
    -ImageId ami-0abcdef1234567890 `
    -InstanceType t2.micro `
    -KeyName "my-key-pair" `
    -SubnetId subnet-0abcdef1234567890 `
    -CapacityReservationSpecification_CapacityReservationPreference "capacity- reservations-only"
The following example launches an instance into a specific Capacity Reservation only. If capacity isn't available in the specified Capacity Reservation, the instance fails to launch.
New-EC2Instance `

    -ImageId ami-0abcdef1234567890 `
    -InstanceType t2.micro `
    -KeyName "my-key-pair" `
    -SubnetId subnet-0abcdef1234567890 `
    -CapacityReservationSpecification_CapacityReservationPreference "capacity- reservations-only" `
    -CapacityReservationTarget_CapacityReservationId cr-1234abcd56EXAMPLE
#### Modify an active Capacity Reservation If you have an existing Capacity Reservation which isn't a good fit for the workload that needs the capacity, you can modify the instance quantity, instance eligibility (open or targeted), and end time (At specific time or Manually). If you specify a new instance quantity that exceeds your remaining On-Demand Instance limit for the selected instance type, the update fails.
The allowed modifications depend on the state of the Capacity Reservation:
- assessing or scheduled state — You can modify the tags only.
- pending state — You can't modify the Capacity Reservation in any way.
- active state but still within the commitment duration — You can't decrease the instance count below the committed instance count, or set an end date that is before the committed duration.
All other modifications are allowed.
- active state with no commitment duration or elapsed commitment duration — All modifications are allowed.
- expired, cancelled, unsupported, or failed state — You can't modify the Capacity Reservation in any way.
Considerations
- You can't change the instance type, platform, Availability Zone, or tenancy after creation. If you need to modify any of these attributes, we recommend that you cancel the reservation, and then create a new one with the required attributes.
- If you modify an existing Capacity Reservation by changing the instance eligibility from targeted to open, any running instances that match the attributes of the Capacity Reservation, have the CapacityReservationPreference parameter set to open, and are not yet running in a Capacity Reservation, will automatically use the modified Capacity Reservation.

- To change the instance eligibility, the Capacity Reservation must be completely idle (zero usage) because Amazon EC2 can't modify instance eligibility when instances are running inside the reservation.
Console To modify a Capacity Reservation
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. Choose Capacity Reservations, select the Capacity Reservation to modify, and then choose Edit.
3. Modify the Total capacity, Capacity Reservation ends, or Instance eligibility options as needed, and choose Save.
AWS CLI To modify a Capacity Reservation Use the modify-capacity-reservation command. The following example modifies the specified Capacity Reservation to reserve capacity for eight instances. aws ec2 modify-capacity-reservation \ --capacity-reservation-id cr-1234567890abcdef0 \ --instance-count 8 PowerShell To modify a Capacity Reservation Use the Edit-EC2CapacityReservation cmdlet. The following example modifies the specified Capacity Reservation to reserve capacity for eight instances.
Edit-EC2CapacityReservation `
    -CapacityReservationId cr-1234567890abcdef0 `
    -InstanceCount 8
#### Modify the Capacity Reservation settings of your instance You can modify the following Capacity Reservation settings for a stopped instance at any time:

- Start in any Capacity Reservation that has matching attributes (instance type, platform, Availability Zone, and tenancy) and available capacity.
- Start the instance in a specific Capacity Reservation.
- Start in any Capacity Reservation that has matching attributes and available capacity in a Capacity Reservation group
- Prevent the instance from starting in a Capacity Reservation.
Console To modify instance Capacity Reservation settings
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. Choose Instances and select the instance to modify. Stop the instance if it is not already stopped.
3. Choose Actions, Instance settings, Modify Capacity Reservation Settings.
4. For Capacity Reservation, choose one of the following options:
- Open – Launches the instances into any Capacity Reservation that has matching attributes and sufficient capacity for the number of instances you selected. If there is no matching Capacity Reservation with sufficient capacity, the instance uses On-Demand capacity.
- None – Prevents the instances from launching into a Capacity Reservation. The instances run in On-Demand capacity.
- Specify Capacity Reservation – Launches the instances into the selected Capacity Reservation. If the selected Capacity Reservation does not have sufficient capacity for the number of instances you selected, the instance launch fails.
- Specify Capacity Reservation group – Launches the instances into any Capacity Reservation with matching attributes and available capacity in the selected Capacity Reservation group. If the selected group does not have a Capacity Reservation with matching attributes and available capacity, the instances launch into On-Demand capacity.
- Specify Capacity Reservation only – Launches the instances into a Capacity Reservation.
If a Capacity Reservation ID isn't specified, the instances launch into an open Capacity Reservation. If capacity isn't available, the instances fail to launch.

- Specify Capacity Reservation resource group only – Launches the instances into a Capacity Reservation in a Capacity Reservation resource group. If a Capacity Reservation resource group ARN isn't specified, the instances launch into an open Capacity Reservation. If capacity isn't available, the instances fail to launch.
AWS CLI To modify instance Capacity Reservation settings Use the modify-instance-capacity-reservation-attributes command.
The following example changes the Capacity Reservation preference to none. aws ec2 modify-instance-capacity-reservation-attributes \ --instance-id i-1234567890abcdef0 \ --capacity-reservation-specification CapacityReservationPreference=none The following example the target to a specific Capacity Reservation. aws ec2 modify-instance-capacity-reservation-attributes \ --instance-id i-1234567890abcdef0 \ --capacity-reservation-specification \ CapacityReservationTarget={CapacityReservationId=cr-1234567890abcdef0} The following example changes the target to a specific Capacity Reservation group. aws ec2 modify-instance-capacity-reservation-attributes \ --instance-id i-1234567890abcdef0 \ --capacity-reservation-specification \

 CapacityReservationTarget={CapacityReservationResourceGroupArn=arn:aws:resource- groups:us-west-2:123456789012:group/my-cr-group} The following example changes the Capacity Reservation preference to capacity- reservation-only. Because it doesn't specify a Capacity Reservation, instances launch into any open Capacity Reservation with matching attributes and available capacity. aws ec2 modify-instance-capacity-reservation-attributes \ --instance-id i-1234567890abcdef0 \

    --capacity-reservation-specification CapacityReservationPreference=capacity- reservation-only The following example changes the Capacity Reservation preference to capacity- reservation-only and changes the target to a specific Capacity Reservation. If capacity isn't available in the specified Capacity Reservation, the instances fail to launch. aws ec2 modify-instance-capacity-reservation-attributes \ --instance-id i-1234567890abcdef0 \ --capacity-reservation-specification \ CapacityReservationPreference=capacity-reservation-only \ CapacityReservationTarget={CapacityReservationId=cr-1234567890abcdef0} PowerShell To modify instance Capacity Reservation settings Use the Edit-EC2InstanceCapacityReservationAttribute cmdlet.
The following example changes the Capacity Reservation preference to none.
Edit-EC2InstanceCapacityReservationAttribute `
    -InstanceId i-1234567890abcdef0 `
    -CapacityReservationSpecification_CapacityReservationPreference "none"
The following example the target to a specific Capacity Reservation.
Edit-EC2InstanceCapacityReservationAttribute `
    -InstanceId i-1234567890abcdef0 `
    -CapacityReservationTarget_CapacityReservationId cr-1234567890abcdef0 The following example changes the target to a specific Capacity Reservation group.
Edit-EC2InstanceCapacityReservationAttribute `
    -InstanceId i-1234567890abcdef0 `
    -CapacityReservationTarget_CapacityReservationResourceGroupArn `
        "arn:aws:resource-groups:us-west-2:123456789012:group/my-cr-group"
The following example changes the Capacity Reservation preference to capacity- reservation-only. Because it doesn't specify a Capacity Reservation, instances launch into any open Capacity Reservation with matching attributes and available capacity.

Edit-EC2InstanceCapacityReservationAttribute `
    -InstanceId i-1234567890abcdef0 `
    -CapacityReservationSpecification_CapacityReservationPreference "capacity- reservation-only"
The following example changes the Capacity Reservation preference to capacity- reservation-only and changes the target to a specific Capacity Reservation. If capacity isn't available in the specified Capacity Reservation, the instances fail to launch.
Edit-EC2InstanceCapacityReservationAttribute `
    -InstanceId i-1234567890abcdef0 `
    -CapacityReservationSpecification_CapacityReservationPreference "capacity- reservation-only" `
    -CapacityReservationTarget_CapacityReservationId cr-1234567890abcdef0
#### Move capacity between Capacity Reservations You can move capacity from one Capacity Reservation to another to redistribute your reserved compute resources as needed. For example, if you need additional capacity in a reservation with growing usage, and you have capacity available in another reservation, then you can reallocate that capacity between the two reservations.
##### Prerequisites for moving capacity As a prerequisite, the two Capacity Reservations must meet the following requirements:
- Both reservations must be in the active state.
- Both reservations must be owned by your AWS account. You cannot move capacity between reservations owned by different AWS accounts.
- Both reservations must have the same:
- Instance type
- Platform
- Availability Zone
- Tenancy
- Placement group
- End time

The destination Capacity Reservations instance eligibility (open or targeted), and tags, don't have to match the source reservation. The configuration of both reservations remains the same, except that the source reservation has reduced capacity and the destination reservation has increased capacity.
When you specify the quantity of instances to be moved, by default, any available capacity is moved first, followed by any eligible running instances (the used capacity in your reservation).
For example, if you move 4 instances from a reservation with 5 used instances and 3 available instances, then the 3 available instances and 1 used instance will be moved.
Note When you move used capacity from your reservation by specifying a Quantity to move that's greater than the available capacity, only the instances that were launched with their Capacity Reservation Specification as open will be moved.
Considerations The following considerations apply when moving capacity from one reservation to another:
- The used capacity can only be moved between Capacity Reservations with open instance eligibility that are shared with the same set of accounts.
- When you move used capacity, the eligible instances are randomly selected. You cannot specify which running instances are moved. If a sufficient number of eligible instances are not found to fulfill the move quantity, the move operation will fail.
- If you move all of the capacity from the source reservation, the Capacity Reservation will be automatically canceled.
- Future-dated Capacity Reservations  — You can't move capacity for a future-dated Capacity Reservation during the commitment period.
Note Moving capacity from a Capacity Block isn't supported.

##### Move capacity You can move capacity from a source Capacity Reservation to a destination Capacity Reservation.
Console To move capacity
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the left navigation pane, choose Capacity Reservations.
3. Select an On-Demand Capacity Reservation ID that has capacity to move.
4. Under Actions, Manage capacity, choose Move.
5. On the Move capacity page, under Destination Capacity Reservation, select a reservation from the list.
6. Under Quantity to move, use the slider or type the number of instances to move from the source Capacity Reservation to the destination Capacity Reservation.
7. Review the summary, and when you're ready, choose Move.
AWS CLI To move capacity Use the move-capacity-reservation-instances command. The following example moves 10 instances from the specified source Capacity Reservation to the specified destination Capacity Reservation. aws ec2 move-capacity-reservation-instances \ --source-capacity-reservation-id cr-1234567890abcdef0 \ --destination-capacity-reservation-id cr-021345abcdef56789 \ --instance-count 10 PowerShell To move capacity Use the Move-EC2CapacityReservationInstance cmdlet. The following example moves 10 instances from the specified source Capacity Reservation to the specified destination Capacity Reservation.

Move-EC2CapacityReservationInstance `
    -SourceCapacityReservationId cr-1234567890abcdef0 `
    -DestinationCapacityReservationId cr-021345abcdef56789 `
    -InstanceCount 10
#### Split off capacity from an existing Capacity Reservation You can split off capacity from an existing Capacity Reservation to create a new reservation. By splitting capacity, you allocate a portion of the original reservation to a specific workload or share it with another AWS account. For example, to partially share a Capacity Reservation with another account, you can split off some of the capacity to create a smaller sized Capacity Reservation. The smaller sized Capacity Reservation can then be shared with the other accounts using AWS Resource Access Manager.
When you split capacity from an existing Capacity Reservation, a new Capacity Reservation is automatically created. The existing reservation will be unchanged, except for the reduced total capacity from the number of instances split off. Instances that are running in the existing Capacity Reservation are not affected. You can split the existing reservation into only one new Capacity Reservation.
The new Capacity Reservation will have the same configuration as the existing Capacity Reservation except for tags. By default, the new Capacity Reservation doesn't have any tags. You can specify new tags during the split operation. The new Capacity Reservation can also be modified after it is created, if necessary.
When you specify the quantity of instances to be split, by default, any available capacity is split first, followed by any eligible running instances (the used capacity in your reservation). For example: if you split 4 instances from a Capacity Reservation with 5 used instances and 3 available instances, then the 3 available instances and 1 used instance will be split into a new reservation.
##### Prerequisites for splitting capacity As a prerequisite, your Capacity Reservation must meet the following requirements:
- The source reservation must be in the active state.
- The source reservation must be owned by your AWS account.

Note When you split used capacity from your reservation by specifying a Quantity to split that's greater than the available capacity, only the instances that were launched with their Capacity Reservation Specification as open will be split.
Considerations The following considerations apply when splitting off capacity from one reservation to a new one:
- The used capacity can only be split for Capacity Reservations with "open" instance eligibility that are not shared with any account.
- When you split the used capacity, the eligible instances are randomly selected. You cannot specify which running instances are split. If a sufficient number of eligible instances are not found to fulfill the split quantity, the split operation will fail.
- The maximum quantity of instances to split from an existing reservation is the size of the reservation minus one. For example, if your reservation's total capacity is 5 instances, you can split a maximum of 4 instances into a new reservation.
- Future-dated Capacity Reservations  – You can't split capacity for a future-dated Capacity Reservation during the commitment period.
- Resource groups – If the existing Capacity Reservation belongs to a resource group, the new Capacity Reservation will not be automatically added to the resource group. You can add the new Capacity Reservation to a resource group after it is created, if necessary.
- Sharing – If the existing Capacity Reservation is shared with a consumer account, the new Capacity Reservation will not be automatically shared with the consumer account. You can share the new Capacity Reservation after it is created, if necessary.
- Cluster placement group – If the existing Capacity Reservation is part of a cluster placement group, the new Capacity Reservation will be created in the same cluster placement group.
Note Splitting capacity from a Capacity Block isn't supported.

##### Control access for splitting Capacity Reservations using tags You can use tags to control access to Amazon EC2 resources, including splitting capacity from an existing Capacity Reservation to create a new Capacity Reservation. For more information, see Controlling access to AWS resources using tags in the IAM User Guide.
To control access for splitting a Capacity Reservation using tags, make sure that you specify both resource and request tags in the policy statement because IAM policies are evaluated against both the source Capacity Reservation and the newly created Capacity Reservation.
The following example policy includes the ec2:ResourceTag condition key with the tag Owner=ExampleDepartment1 for the source Capacity Reservation and the ec2:RequestTag condition key with the tag stack=production for the newly created Capacity Reservation.
{ "Statement": [ { "Sid": "AllowSourceCapacityReservation", "Effect": "Allow", "Action": "ec2:CreateCapacityReservationBySplitting", "Resource": "arn:aws:ec2:us-east-1:111122223333:capacity-reservation/ cr-1234567890abcdef0", "Condition": { "StringEquals": { "ec2:ResourceTag/Owner": "ExampleDepartment1"
        } } }, { "Sid": "AllowNewlyCreatedCapacityReservation", "Effect": "Allow", "Action": ["ec2:CreateCapacityReservationBySplitting", "ec2:CreateTags"], "Resource": "arn:aws:ec2:us-east-1:111122223333:capacity-reservation/*", "Condition": { "StringEquals": { "aws:RequestTag/stack": "production"
        } } } ]
}

##### Split off capacity You can split off capacity from an existing Capacity Reservation to create a new Capacity Reservation.
Console To split off capacity
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the left navigation pane, choose Capacity Reservations.
3. Select an On-Demand Capacity Reservation ID that has capacity to split.
4. Under Actions, Manage capacity, choose Split.
5. On the Split Capacity Reservation page, under Quantity to split, use the slider or type the number of instances to split from the current reservation.
6. (Optional) Add tags for the new Capacity Reservation.
7. Review the summary, and when you're ready, choose Split.
AWS CLI To split off capacity Use the create-capacity-reservation-by-splitting command. The following example creates a new Capacity Reservation by splitting off 10 instances from the specified Capacity Reservation. aws ec2 create-capacity-reservation-by-splitting \ --source-capacity-reservation-id cr-1234567890abdef0 \ --instance-count 10 PowerShell To split off capacity Use the New-EC2CapacityReservationBySplitting cmdlet. The following example creates a new Capacity Reservation by splitting off 10 instances from the specified Capacity Reservation.
New-EC2CapacityReservationBySplitting `

    -SourceCapacityReservationId cr-1234567890abdef0 `
    -InstanceCount 10
#### Cancel a Capacity Reservation You can cancel a Capacity Reservation that is in one of the following states:
- assessing
- active and there is no commitment duration or the commitment duration has elapsed. You can't cancel a future-dated Capacity Reservation during the commitment duration.
Note You can't modify or cancel a Capacity Block. For more information, see Capacity Blocks for ML.
If a future-dated Capacity Reservation enters the delayed state, the commitment duration is waived, and you can cancel it as soon as it enters the active state.
When you cancel a Capacity Reservation, the capacity is released immediately, and it is no longer reserved for your use.
You can cancel empty Capacity Reservations and Capacity Reservations that have running instances. If you cancel a Capacity Reservation that has running instances, the instances continue to run normally outside of the capacity reservation at standard On-Demand Instance rates or at a discounted rate if you have a matching Savings Plans or Regional Reserved Instance.
After you cancel a Capacity Reservation, instances that target it can no longer launch. Modify these instances so that they either target a different Capacity Reservation, launch into any open Capacity Reservation with matching attributes and sufficient capacity, or avoid launching into a Capacity Reservation. For more information, see Modify the Capacity Reservation settings of your instance.
Console To cancel a Capacity Reservation
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.

2. Choose Capacity Reservations and select the Capacity Reservation to cancel.
3. Choose Cancel reservation, Cancel reservation.
AWS CLI To cancel a Capacity Reservation Use the cancel-capacity-reservation command. aws ec2 cancel-capacity-reservation \ --capacity-reservation-id cr-1234567890abcdef0 PowerShell To cancel a Capacity Reservation Use the Remove-EC2CapacityReservation cmdlet.
Remove-EC2CapacityReservation `
    -CapacityReservationId cr-1234567890abcdef0
#### Use Capacity Reservations with cluster placement groups You can create Capacity Reservations in a cluster placement group to reserve Amazon EC2 compute capacity for your workloads. Cluster placement groups offer the benefit of low network latency and high network throughput.
Creating a Capacity Reservation in a cluster placement group ensures that you have access to compute capacity in your cluster placement groups when you need it, for as long as you need it.
This is ideal for reserving capacity for high-performance (HPC) workloads that require compute scaling. It allows you to scale your cluster down while ensuring that the capacity remains available for your use so that you can scale back up when needed.
After you create a Capacity Reservation in a cluster placement group, you can share it with other AWS accounts. For more information, see Sharing Capacity Reservations in cluster placement groups.
Topics

- Limitations
- Work with Capacity Reservations in cluster placement groups
- Sharing Capacity Reservations in cluster placement groups Limitations Keep the following in mind when creating Capacity Reservations in cluster placement groups:
- If an existing Capacity Reservation is not in a placement group, you can't modify the Capacity Reservation to reserve capacity in a placement group. To reserve capacity in a placement group, you must create the Capacity Reservation in the placement group.
- After you create a Capacity Reservation in a placement group, you can't modify it to reserve capacity outside of the placement group.
- You can increase your reserved capacity in a placement group by modifying an existing Capacity Reservation in the placement group, or by creating additional Capacity Reservations in the placement group. However, you increase your chances of getting an insufficient capacity error.
- You can share Capacity Reservations only from the cluster placement group that you own. You cannot share Capacity Reservations from a cluster placement group that you do not own.
- You can't delete a cluster placement group that has active Capacity Reservations. You must cancel all Capacity Reservations in the cluster placement group before you can delete it.
##### Work with Capacity Reservations in cluster placement groups To start using Capacity Reservations with cluster placement groups, perform the following steps.
Note If you want to create a Capacity Reservation in an existing cluster placement group, skip Step 1. Then for Steps 2 and 3, specify the ARN of the existing cluster placement group.
Tasks
- Step 1: (Conditional) Create a cluster placement group for use with a Capacity Reservation
- Step 2: Create a Capacity Reservation in a cluster placement group
- Step 3: Launch instances into Capacity Reservations in a cluster placement group

###### Step 1: (Conditional) Create a cluster placement group for use with a Capacity Reservation Perform this step only if you need to create a new cluster placement group. To use an existing cluster placement group, skip this step and then for Steps 2 and 3, use the ARN of that cluster placement group.
Console To create a cluster placement group
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Placement Groups, and then choose Create placement group.
3. For Name, specify a descriptive name for the placement group.
4. For Placement strategy, choose Cluster.
5. Choose Create group.
6. In the Placement groups table, in the Group ARN column, make a note of the ARN of the cluster placement group that you created. You'll need it for the next step.
AWS CLI To create a cluster placement group Use the create-placement-group command. aws ec2 create-placement-group \ --group-name MyPG \ --strategy cluster Make a note of the placement group ARN returned in the output, because you'll need it for the next step.
PowerShell To create a cluster placement group Use the New-EC2PlacementGroup cmdlet.
New-EC2PlacementGroup `
    -GroupName my-placement-group `

    -Strategy "cluster"
Make a note of the placement group ARN returned in the output, because you'll need it for the next step.
###### Step 2: Create a Capacity Reservation in a cluster placement group You create a Capacity Reservation in a cluster placement group in the same way that you create any Capacity Reservation. However, you must also specify the ARN of the cluster placement group in which to create the Capacity Reservation.
Considerations
- The specified cluster placement group must be in the available state. If the cluster placement group is in the pending, deleting, or deleted state, the request fails.
- The Capacity Reservation and the cluster placement group must be in the same Availability Zone.
If the request to create the Capacity Reservation specifies an Availability Zone that is different from that of the cluster placement group, the request fails.
- You can create Capacity Reservations only for instance types that are supported by cluster placement groups. If you specify an unsupported instance type, the request fails.
- If you create an open Capacity Reservation in a cluster placement group and there are existing running instances that have matching attributes (placement group ARN, instance type, Availability Zone, platform, and tenancy), those instances automatically run in the Capacity Reservation.
- Your request to create a Capacity Reservation could fail if one of the following is true:
- Amazon EC2 does not have sufficient capacity to fulfill the request. Either try again at a later time, try a different Availability Zone, or try a smaller capacity. If your workload is flexible across instance types and sizes, try different instance attributes.
- The requested quantity exceeds your On-Demand Instance limit for the selected instance family. Increase your On-Demand Instance limit for the instance family and try again. For more information, see On-Demand Instance quotas.
Console To create a Capacity Reservation
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.

2. Choose Capacity Reservations, and then choose Create Capacity Reservation.
3. On the Create a Capacity Reservation page, specify the instance type, platform, Availability Zone, Tenancy, quantity, and end date as needed.
4. For Placement group, select the ARN of the cluster placement group in which to create the Capacity Reservation.
5. Choose Create.
For more information, see Create a Capacity Reservation.
AWS CLI To create a Capacity Reservation Use the create-capacity-reservation command. For --placement-group-arn, specify the ARN of the cluster placement group in which to create the Capacity Reservation. aws ec2 create-capacity-reservation \ --instance-type instance_type \ --instance-platform platform \ --availability-zone-id az_id \ --instance-count quantity \ --placement-group-arn "placement_group_arn"
PowerShell To create a Capacity Reservation Use the Add-EC2CapacityReservation cmdlet. For -PlacementGroupArn, specify the ARN of the cluster placement group in which to create the Capacity Reservation.
Add-EC2CapacityReservation `
    -InstanceType instance_type `
    -InstancePlatform platform `
    -AvailabilityZoneId az_id `
    -InstanceCount quantity `
    -PlacementGroupArn "placement_group_arn"

###### Step 3: Launch instances into Capacity Reservations in a cluster placement group You can launch an instance into a Capacity Reservation that is in a cluster placement group with one of the following options:
- Specifying the ARN of the cluster placement group in which to launch the instance – When you provide the ARN of a cluster placement group, Amazon EC2 launches the instance into that cluster placement group. You can use one of the following methods:
- Specifying open – You do not have to specify the Capacity Reservation in the instance launch request. If the instance has attributes (placement group ARN, instance type, Availability Zone, platform, and tenancy) that match a Capacity Reservation in the specified placement group, the instance automatically runs in the Capacity Reservation.
- Specifying a Capacity Reservation – If the Capacity Reservation accepts only targeted instance launches, you must specify the target Capacity Reservation in addition to the cluster placement group in the request.
- Specifying a Capacity Reservation group – For more information, see  Using Capacity Reservation in cluster placement groups with a Capacity Reservation group.
- Specifying only a Capacity Reservation group – For more information, see Using Capacity Reservation in cluster placement groups with a Capacity Reservation group.
- Specifying only a Capacity Reservation – You can launch instances into a Capacity Reservation in a cluster placement group.
Note When you launch instances by specifying only a Capacity Reservation or only a Capacity Reservation group, the instances are launched into the Capacity Reservations that are created in the cluster placement group, but the instances are not directly attached to the cluster placement group.
Console To launch instances into an existing Capacity Reservation
1. Follow the procedure to launch an instance, but don't launch the instance until you've completed the following steps to specify the settings for the placement group and Capacity Reservation.

2. Expand Advanced details and do the following: a.
For Placement group, select the cluster placement group in which to launch the instance. b.
For Capacity Reservation, choose one of the following options depending on the configuration of the Capacity Reservation:
- Open – To launch the instances into any open Capacity Reservation in the cluster placement group that has matching attributes and sufficient capacity.
- Target by ID – To launch the instances into a Capacity Reservation that accepts only targeted instance launches.
- Target by group – To launch the instances into any Capacity Reservation with matching attributes and available capacity in the selected Capacity Reservation group.
3. In the Summary panel, review your instance configuration, and then choose Launch instance. For more information, see Launch an EC2 instance using the launch instance wizard in the console.
AWS CLI To launch instances into an existing Capacity Reservation Use the run-instances command. If you need to target a specific Capacity Reservation or a Capacity Reservation group, specify the --capacity-reservation-specification parameter. For --placement, specify the GroupName parameter and then specify the name of the placement group that you created in the previous steps. aws ec2 run-instances \ --image-id ami-0abcdef1234567890 \ --count quantity \ --instance-type instance_type \ --key-name key_pair_name \ --subnet-id subnet-0abcdef1234567890 \ --capacity-reservation-specification CapacityReservationTarget={CapacityReservationId=capacity_reservation_id} \ --placement "GroupName=cluster_placement_group_name"

PowerShell To launch instances into an existing Capacity Reservation Use the New-EC2Instance cmdlet. For -Placement, specify the GroupName parameter and then specify the name of the placement group that you created in the previous steps.
New-EC2Instance `
    -ImageId ami-0abcdef1234567890 `
    -InstanceType instance_type `
    -KeyName key_pair_name `
    -SubnetId subnet-0abcdef1234567890 `
    -CapacityReservationTarget_CapacityReservationId capacity_reservation_id `
    -Placement_GroupName cluster_placement_group_name
##### Sharing Capacity Reservations in cluster placement groups You can share Capacity Reservations in cluster placement groups by either sharing only the Capacity Reservations, or by sharing both the Capacity Reservations and the cluster placement group in which they were created.
By sharing only the Capacity Reservation, you give consumer accounts access to that Capacity Reservation only. Consumer accounts have no visibility or access to the cluster placement group in which the Capacity Reservation is created. This gives you fine-grained control over consumer account access. Consumer accounts can't view any information about the cluster placement group, including its ARN.
When you share the cluster placement group and the Capacity Reservation, the cluster placement group is visible and accessible to consumer accounts. They can launch instances and create their own Capacity Reservations in it.
For more information, see the following resources.
- Launch instances into Capacity Reservations in a cluster placement group
- Shared Capacity Reservations
- Shared placement groups

#### Capacity Reservation groups You can use AWS Resource Groups to create logical collections of Capacity Reservations, called resource groups. A resource group is a logical grouping of AWS resources that are all in the same AWS Region. For more information about resource groups, see What are resource groups? in the AWS Resource Groups User Guide.
You can include Capacity Reservations that you own in your account, and Capacity Reservations that are shared with you by other AWS accounts in a single resource group. You can also include Capacity Reservations that have different attributes (instance type, platform, Availability Zone, and tenancy) in a single resource group.
When you create resource groups for Capacity Reservations, you can target instances to a group of Capacity Reservations instead of an individual Capacity Reservation. Instances that target a group of Capacity Reservations match with any Capacity Reservation in the group that has matching attributes (instance type, platform, Availability Zone, and tenancy) and available capacity. If the group does not have a Capacity Reservation with matching attributes and available capacity, the instances run using On-Demand capacity. If a matching Capacity Reservation is added to the targeted group at a later stage, the instance is automatically matched with and moved into its reserved capacity.
To prevent unintended use of Capacity Reservations in a group, configure the Capacity Reservations in the group to accept only instances that explicitly target the capacity reservation.
To do this, set Instance eligibility to Only instances that specify this reservation when creating the Capacity Reservation using the Amazon EC2 console. When using the AWS CLI, specify -- instance-match-criteria targeted when creating the Capacity Reservation. Doing this ensures that only instances that explicitly target the group, or a Capacity Reservation in the group, can run in the group.
If a Capacity Reservation in a group is canceled or expires while it has running instances, the instances are automatically moved to another Capacity Reservation in the group that has matching attributes and available capacity. If there are no remaining Capacity Reservations in the group that have matching attributes and available capacity, the instances run in On-Demand capacity.
If a matching Capacity Reservation is added to the targeted group at a later stage, the instance is automatically moved into its reserved capacity.
Tasks
- Create a Capacity Reservation group
- Add a Capacity Reservation to a group

- Remove a Capacity Reservation from a group
- Delete a Capacity Reservation group
- Using Capacity Reservation in cluster placement groups with a Capacity Reservation group
##### Create a Capacity Reservation group You can use the following examples to create a resource group for Capacity Reservations with the following request parameters.
- AWS::EC2::CapacityReservationPool – Ensures that the resource group can be targeted for instance launches.
- AWS::ResourceGroups::Generic with allowed-resource-types set to AWS::EC2::CapacityReservation – Ensures that the resource group accepts Capacity Reservations only.
After you create a group, you can add Capacity Reservations to the group.
AWS CLI To create a group for Capacity Reservations Use the create-group AWS CLI command. aws resource-groups create-group \ --name MyCRGroup \ --configuration \ '{"Type": "AWS::EC2::CapacityReservationPool"}' \ '{"Type": "AWS::ResourceGroups::Generic", "Parameters": [{"Name": "allowed- resource-types", "Values": ["AWS::EC2::CapacityReservation"]}]}'
PowerShell To create a group for Capacity Reservations Use the New-RGGroup cmdlet.
New-RGGroup `
    -Name MyCRGroup `
    -Configuration `
        @{"Type"="AWS::EC2::CapacityReserationPool"} `

        @{"Type"="AWS::ResourceGroups::Generic"; "Parameters"=@{"allowed-resource- types"=@{"Values"="AWS::EC2::CapacityReservations"}}}
##### Add a Capacity Reservation to a group If you add a Capacity Reservation that is shared with you to a group, and that Capacity Reservation is unshared, it is automatically removed from the group.
AWS CLI To add a Capacity Reservation to a group Use the group-resources command.
The following example adds two Capacity Reservations to the specified group. aws resource-groups group-resources \ --group MyCRGroup \ --resource-arns \ arn:aws:ec2:sa-east-1:123456789012:capacity-reservation/cr-1234567890abcdef1 \ arn:aws:ec2:sa-east-1:123456789012:capacity-reservation/cr-54321abcdef567890 PowerShell To add a Capacity Reservation to a group Use the Add-RGResource cmdlet.
The following example adds two Capacity Reservations to the specified group.
Add-RGResource `
    -Group MyCRGroup `
    -ResourceArn `
        "arn:aws:ec2:sa-east-1:123456789012:capacity- reservation/cr-1234567890abcdef1", `
        "arn:aws:ec2:sa-east-1:123456789012:capacity- reservation/cr-54321abcdef567890"
##### Remove a Capacity Reservation from a group You can use the following examples to remove a Capacity Reservation from a group.

AWS CLI To remove a Capacity Reservation from a group Use the ungroup-resources command.
The following example removes two Capacity Reservations from the specified group. aws resource-groups ungroup-resources \ --group MyCRGroup \ --resource-arns \ arn:aws:ec2:sa-east-1:123456789012:capacity-reservation/cr-0e154d26a16094dd \ arn:aws:ec2:sa-east-1:123456789012:capacity-reservation/cr-54321abcdef567890 PowerShell To remove a Capacity Reservation from a group Use the Remove-RGResource cmdlet.
The following example removes two Capacity Reservations from the specified group.
Remove-RGResource `
    -Group MyCRGroup `
    -ResourceArn `
        "arn:aws:ec2:sa-east-1:123456789012:capacity- reservation/cr-0e154d26a16094dd", `
        "arn:aws:ec2:sa-east-1:123456789012:capacity- reservation/cr-54321abcdef567890"
##### Delete a Capacity Reservation group You can use the following examples to delete a Capacity Reservation group.
AWS CLI To delete a group Use the delete-group command. aws resource-groups delete-group --group MyCRGroup

PowerShell To delete a group Use the Remove-RGGroup cmdlet.
Remove-RGGroup -GroupName MyCRGroup
##### Using Capacity Reservation in cluster placement groups with a Capacity Reservation group Amazon EC2 provides different launch methods for you to use Capacity Reservations in a cluster placement group with a Capacity Reservation group. You can choose one of the following methods to target a Capacity Reservation group based on your workload requirements:
- Specifying the ARN of the cluster placement group and Capacity Reservation group – This will use any available Capacity Reservation with matching attributes and available capacity in the selected Capacity Reservation group. If the selected group does not have a Capacity Reservation with matching attributes and available capacity, the instances launch into On-Demand capacity.
Note When you launch instances using this method, the instances are placed in the specified cluster placement group.
- Specifying only a Capacity Reservation group – This will use all available capacity within the Capacity Reservation group by specifying only the Capacity Reservation group. While launching instances, capacity is used in the following order:
- Capacity Reservations not associated with any cluster placement group.
- Capacity Reservation in any cluster placement group within the Capacity Reservation group.
- If the group does not have a Capacity Reservation with matching attributes and available capacity, the instances run using On-Demand capacity and they are not placed in any cluster placement group.
Note When you launch instances by specifying only a Capacity Reservation group, the instances are launched into the Capacity Reservations that are created in the cluster

placement group, but the instances are not directly attached to the cluster placement group.
#### Capacity Reservations in Local Zones A Local Zone is an extension of an AWS Region that is geographically close to your users. Resources created in a Local Zone can serve local users with very low-latency communications. For more information, see AWS Local Zones.
You can extend a VPC from its parent AWS Region into a Local Zone by creating a new subnet in that Local Zone. When you create a subnet in a Local Zone, your VPC is extended to that Local Zone. The subnet in the Local Zone operates the same as the other subnets in your VPC.
By using Local Zones, you can place Capacity Reservations in multiple locations that are closer to your users. You create and use Capacity Reservations in Local Zones in the same way that you create and use Capacity Reservations in regular Availability Zones. The same features and instance matching behavior apply. For more information about the pricing models that are supported in Local Zones, see AWS Local Zones FAQs.
Considerations You can't use Capacity Reservation groups in a Local Zone.
To use a Capacity Reservation in a Local Zone
1. Enable the Local Zone for use in your AWS account. For more information, see Getting started with AWS Local Zones in the AWS Local Zones User Guide.
2. Create a Capacity Reservation in the Local Zone. For Availability Zone, choose the Local Zone.
The Local Zone is represented by an AWS Region code followed by an identifier that indicates the location, for example us-west-2-lax-1a. For more information, see Create a Capacity Reservation.
3. Create a subnet in the Local Zone. For Availability Zone, choose the Local Zone. For more information, see Create a subnet in your VPC in the Amazon VPC User Guide.
4. Launch an instance. For Subnet, choose the subnet in the Local Zone (for example subnet-123abc | us-west-2-lax-1a), and for Capacity Reservation, choose the specification (either open or target it by ID) that's required for the Capacity Reservation that you created in the Local Zone. For more information, see Launch instances into an existing Capacity Reservation.

#### Capacity Reservations in Wavelength Zones AWS Wavelength enables developers to build applications that deliver ultra-low latencies to mobile devices and end users. Wavelength deploys standard AWS compute and storage services to the edge of telecommunication carriers' 5G networks. You can extend an Amazon Virtual Private Cloud (VPC) to one or more Wavelength Zones. You can then use AWS resources like Amazon EC2 instances to run applications that require ultra-low latency and a connection to AWS services in the Region. For more information, see AWS Wavelength Zones.
When you create On-Demand Capacity Reservations, you can choose the Wavelength Zone and you can launch instances into a Capacity Reservation in a Wavelength Zone by specifying the subnet associated with the Wavelength Zone. A Wavelength Zone is represented by an AWS Region code followed by an identifier that indicates the location, for example us-east-1-wl1-bos-wlz-1.
Wavelength Zones are not available in every Region. For information about the Regions that support Wavelength Zones, see Available Wavelength Zones in the AWS Wavelength Developer Guide.
Considerations You can't use Capacity Reservation groups in a Wavelength Zone.
To use a Capacity Reservation in a Wavelength Zone
1. Enable the Wavelength Zone for use in your AWS account. For more information, see Get started with AWS Wavelength in the AWS Wavelength Developer Guide.
2. Create a Capacity Reservation in the Wavelength Zone. For Availability Zone, choose the Wavelength. The Wavelength is represented by an AWS Region code followed by an identifier that indicates the location, for example us-east-1-wl1-bos-wlz-1. For more information, see Create a Capacity Reservation.
3. Create a subnet in the Wavelength Zone. For Availability Zone, choose the Wavelength Zone.
For more information, see Create a subnet in your VPC in the Amazon VPC User Guide.
4. Launch an instance. For Subnet, choose the subnet in the Wavelength Zone (for example subnet-123abc | us-east-1-wl1-bos-wlz-1), and for Capacity Reservation, choose the specification (either open or target it by ID) that's required for the Capacity Reservation that you created in the Wavelength. For more information, see Launch instances into an existing Capacity Reservation.

#### Capacity Reservations on AWS Outposts AWS Outposts is a fully managed service that extends AWS infrastructure, services, APIs, and tools to customer premises. By providing local access to AWS managed infrastructure, AWS Outposts enables customers to build and run applications on premises using the same programming interfaces as in AWS Regions, while using local compute and storage resources for lower latency and local data processing needs.
An Outpost is a pool of AWS compute and storage capacity deployed at a customer site. AWS operates, monitors, and manages this capacity as part of an AWS Region.
You can create Capacity Reservations on Outposts that you have created in your account. This allows you to reserve compute capacity on an Outpost at your site. You create and use Capacity Reservations on Outposts in the same way that you create and use Capacity Reservations in regular Availability Zones. The same features and instance matching behavior apply.
You can also share Capacity Reservations on Outposts with other AWS accounts within your organization using AWS Resource Access Manager. For more information about sharing Capacity Reservations, see Shared Capacity Reservations.
Prerequisite You must have an Outpost installed at your site. For more information, see  Create an Outpost and order Outpost capacity in the AWS Outposts User Guide.
Considerations
- You can't use Capacity Reservation groups on an Outpost.
To use a Capacity Reservation on an Outpost
1. Create a subnet on the Outpost. For more information, see Create a subnet in the AWS Outposts User Guide.
2. Create a Capacity Reservation on the Outpost. a.
Open the AWS Outposts console at https://console.aws.amazon.com/outposts/. b.
In the navigation pane, choose Outposts, and then choose Actions, Create Capacity Reservation. c.
Configure the Capacity Reservation as needed and then choose Create. For more information, see Create a Capacity Reservation.

Note The Instance Type drop-down lists only instance types that are supported by the selected Outpost, and the Availability Zone drop-down lists only the Availability Zone with which the selected Outpost is associated.
3. Launch an instance into the Capacity Reservation. For Subnet choose the subnet that you created in Step 1, and for Capacity Reservation, select the Capacity Reservation that you created in Step 2. For more information, see Launch an instance on the Outpost in the AWS Outposts User Guide.
#### Shared Capacity Reservations Capacity Reservation sharing enables Capacity Reservation owners to share their reserved capacity with other AWS accounts or within an AWS organization. This enables you to create and manage Capacity Reservations centrally, and share the reserved capacity across multiple AWS accounts or within your AWS organization.
In this model, the AWS account that owns the Capacity Reservation (owner) shares it with other AWS accounts (consumers). Consumers can launch instances into Capacity Reservations that are shared with them in the same way that they launch instances into Capacity Reservations that they own in their own account. The Capacity Reservation owner is responsible for managing the Capacity Reservation and the instances that they launch into it. Owners cannot modify instances that consumers launch into Capacity Reservations that they have shared. Consumers are responsible for managing the instances that they launch into Capacity Reservations shared with them. Consumers cannot view or modify instances owned by other consumers or by the Capacity Reservation owner.
A Capacity Reservation owner can share a Capacity Reservation with:
- Specific AWS accounts inside or outside of its AWS organization
- An organizational unit inside its AWS organization
- Its entire AWS organization

##### Prerequisites for sharing Capacity Reservations
- To share a Capacity Reservation, you must own it in your AWS account. You cannot share a Capacity Reservation that has been shared with you.
- You can only share Capacity Reservations for shared tenancy instances. You cannot share Capacity Reservations for dedicated tenancy instances.
- Capacity Reservation sharing is not available to new AWS accounts or AWS accounts that have a limited billing history.
- To share a Capacity Reservation with your AWS organization or an organizational unit in your AWS organization, you must enable sharing with AWS Organizations. For more information, see Enable Sharing with AWS Organizations in the AWS RAM User Guide.
- You can share a Capacity Reservation in active or scheduled state. You cannot share Capacity Reservation in other  states , such as assessing or unsupported.
##### Related services Capacity Reservation sharing integrates with AWS Resource Access Manager (AWS RAM). AWS RAM is a service that enables you to share your AWS resources with any AWS account or through AWS Organizations. With AWS RAM, you share resources that you own by creating a resource share.
A resource share specifies the resources to share, and the consumers with whom to share them.
Consumers can be individual AWS accounts, or organizational units or an entire organization from AWS Organizations.
For more information about AWS RAM, see the AWS RAM User Guide.
##### Share across Availability Zones To ensure that resources are distributed across the Availability Zones for a Region, we independently map Availability Zones to names for each account. This could lead to Availability Zone naming differences across accounts. For example, the Availability Zone us-east-1a for your AWS account might not have the same location as us-east-1a for another AWS account.
To identify the location of your Capacity Reservations relative to your accounts, you must use the Availability Zone ID (AZ ID). The AZ ID is a unique and consistent identifier for an Availability Zone across all AWS accounts. For example, use1-az1 is an AZ ID for the us-east-1 Region and it is the same location in every AWS account.

To view the AZ IDs for the Availability Zones in your account
1. Open the AWS RAM console at https://console.aws.amazon.com/ram/home.
2. The AZ IDs for the current Region are displayed in the Your AZ ID panel on the right-hand side of the screen.
##### Share a Capacity Reservation When you share a Capacity Reservation that you own with other AWS accounts, you enable them to launch instances into your reserved capacity. If you share an open Capacity Reservation, keep the following in mind as it could lead to unintended Capacity Reservation usage:
- If consumers have running instances that match the attributes of the Capacity Reservation, have the CapacityReservationPreference parameter set to open, and are not yet running in reserved capacity, they automatically use the shared Capacity Reservation.
- If consumers launch instances that have matching attributes (instance type, platform, Availability Zone, and tenancy) and have the CapacityReservationPreference parameter set to open, they automatically launch into the shared Capacity Reservation.
To share a Capacity Reservation, you must add it to a resource share. A resource share is an AWS RAM resource that lets you share your resources across AWS accounts. A resource share specifies the resources to share, and the consumers with whom they are shared. When you share a Capacity Reservation using the Amazon EC2 console, you add it to an existing resource share. To add the Capacity Reservation to a new resource share, you must create the resource share using the AWS RAM console.
If you are part of an organization in AWS Organizations and sharing within your organization is enabled, consumers in your organization are granted access to the shared Capacity Reservation if the prerequisites for sharing are met. If the Capacity Reservation is shared with external accounts, they receive an invitation to join the resource share and are granted access to the shared Capacity Reservation after accepting the invitation.
Important Before launching instances into a Capacity Reservation that is shared with you, verify that you have access to the shared Capacity Reservation by viewing it in the console or by describing it using the  describe-capacity-reservations AWS CLI command. If you can

view the shared Capacity Reservation in the console or describe it using the AWS CLI, it is available for your use and you can launch instances into it. If you attempt to launch instances into the Capacity Reservation and it is not accessible due to a sharing failure, the instances will launch into On-Demand capacity.
Console To share a Capacity Reservation that you own using the Amazon EC2 console
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Capacity Reservations.
3. Choose the Capacity Reservation to share and choose Actions, Share reservation.
4. Select the resource share to which to add the Capacity Reservation and choose Share Capacity Reservation.
It could take a few minutes for consumers to get access to the shared Capacity Reservation.
To share a Capacity Reservation that you own using the AWS RAM console See Creating a resource share in the AWS RAM User Guide.
AWS CLI To share a Capacity Reservation that you own Use the create-resource-share command. aws ram create-resource-share \ --name my-resource-share \ --resource-arns arn:aws:ec2:us-east-2:123456789012:capacity- reservation/cr-1234abcd56EXAMPLE PowerShell To share a Capacity Reservation that you own Use the New-RAMResourceShare cmdlet.
New-RAMResourceShare `

    -Name my-resource-share `
    -ResourceArn "arn:aws:ec2:us-east-2:123456789012:capacity- reservation/cr-1234abcd56EXAMPLE"
##### Stop sharing a Capacity Reservation The Capacity Reservation owner can stop sharing a Capacity Reservation at any time. The following rules apply:
- Instances owned by consumers that were running in the shared capacity at the time sharing stops continue to run normally outside of the reserved capacity, and the capacity is restored to the Capacity Reservation subject to Amazon EC2 capacity availability.
- Consumers with whom the Capacity Reservation was shared can no longer launch new instances into the reserved capacity.
To stop sharing a Capacity Reservation that you own, you must remove it from the resource share.
Console To stop sharing a Capacity Reservation that you own using the Amazon EC2 console
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Capacity Reservations.
3. Select the Capacity Reservation and choose the Sharing tab.
4. The Sharing tab lists the resource shares to which the Capacity Reservation has been added. Select the resource share from which to remove the Capacity Reservation and choose Remove from resource share.
To stop sharing a Capacity Reservation that you own using the AWS RAM console See Updating a Resource Share in the AWS RAM User Guide.
AWS CLI To stop sharing a Capacity Reservation that you own Use the disassociate-resource-share command. aws ram disassociate-resource-share \

    --resource-share-arn arn:aws:ram:us-east-2:123456789012:resource-share/7ab63972- b505-7e2a-420d-6f5d3EXAMPLE \ --resource-arns arn:aws:ec2:us-east-2:123456789012:capacity- reservation/cr-1234abcd56EXAMPLE PowerShell To stop sharing a Capacity Reservation that you own Use the Disconnect-RAMResourceShare cmdlet.
Disconnect-RAMResourceShare `
    -ResourceShareArn "arn:aws:ram:us-east-2:123456789012:resource-share/7ab63972- b505-7e2a-420d-6f5d3EXAMPLE" `
    -ResourceArn "arn:aws:ec2:us-east-2:123456789012:capacity- reservation/cr-1234abcd56EXAMPLE"
##### Billing assignment for shared Amazon EC2 Capacity Reservations By default, when a Capacity Reservation is shared, the owner is billed for the instances they run in the Capacity Reservation and for any available capacity, also called unused capacity, in the Capacity Reservation; while consumers are billed only for the instances they run in the shared Capacity Reservation.
If needed, the Capacity Reservation owner can assign the billing of any available capacity in the Capacity Reservation to any one of the accounts with which the Capacity Reservation is shared. After billing is assigned to another account, that account becomes the billing owner of any available capacity in the Capacity Reservation. Any charges for available capacity in the Capacity Reservation, from that point onward, are billed to the assigned account instead of the owner's account. The Capacity Reservation owner and the accounts with which the Capacity Reservation is shared continue to be billed for the instances they run in the Capacity Reservation.
Important The Capacity Reservation owner remains the resource owner and they remain responsible for managing the Capacity Reservation. The account to which billing is assigned does not get any additional privileges; they can't cancel, modify, or share the Capacity Reservation in any way.

Topics
- How it works
- Considerations
- Assign billing of a shared EC2 Capacity Reservation to another account
- View billing assignment requests for shared EC2 Capacity Reservations
- Accept or reject billing of a shared EC2 Capacity Reservation
- Cancel or revoke billing assignment requests for shared EC2 Capacity Reservations
- Monitor billing assignment requests for shared Capacity Reservations
###### How it works Only the Capacity Reservation owner can assign billing of a shared Capacity Reservation to another account. Billing can be assigned only to an account with which the Capacity Reservation is shared and that is consolidated under the same AWS Organizations payer account as the Capacity Reservation owner.
To assign billing of the available capacity of a Capacity Reservation to another account, the Capacity Reservation owner must initiate a request to the required account. The specified account receives the request and they must either accept or reject it within 12 hours.
- If they accept, they become the billing owner of any available capacity, also called unused capacity, in the Capacity Reservation. From that point onward, charges for any available capacity in the Capacity Reservation are billed to their account instead of the owner's account. After it is accepted, only the Capacity Reservation owner can revoke billing from the assigned account.
- If they reject, the Capacity Reservation owner remains the billing owner of the available capacity in the Capacity Reservation. Charges for any available capacity in the Capacity Reservation continue to be billed to the owner's account.
- If they do not accept or reject the request within 12 hours, it expires and charges for any available capacity in the Capacity Reservation continue to be billed to owner's account.
For the period that billing is assigned to another account, the Reservation and UnusedBox line items appear in the assigned account's Cost and Usage Report (CUR) instead of the owner's CUR.
The following table shows which line items appear in the CUR for the Capacity Reservation owner and consumer accounts before billing is assigned to another account.

Account CUR line items before billing is assigned Capacity Reservation owner
- Reservation
- BoxUsage *
- UnusedBox Consumer accounts with which the Capacity Reservati on is shared
- BoxUsage * The following table shows which line items appear in the CUR for the Capacity Reservation owner and consumer accounts after billing is assigned to another account.
Account CUR line items after billing is assigned Capacity Reservation owner
- BoxUsage * Consumer account to which billing is assigned
- Reservation
- BoxUsage *
- UnusedBox Other consumer accounts with which the Capacity Reservation is shared
- BoxUsage *

Account CUR line items after billing is assigned Note
- * The BoxUsage line item appears in an account's CUR only if they have running instances in the Capacity Reservation. For more information about the CUR line items, see Monitoring Capacity Reservations.
- Use the Capacity Reservation ARN in the CUR to determine who owns the Capacity Reservation. If the ARN includes your AWS account ID, you are the Capacity Reservation owner. Otherwise, the Capacity Reservation is owned by a different account but billing is assigned to you.
- Cost allocation tags assigned to Capacity Reservation by the owner will not appear in the consumer account's CUR. Cost allocation tags appear in the Capacity Reservation owner's CUR only.
Considerations Keep the following in mind when assigning billing of a shared Capacity Reservation:
- You can't do partial or split billing assignments. Billing of all available capacity of a Capacity Reservation can be assigned to one account at a time.
- The available capacity of a Capacity Reservation can change over time. This will impact billing for the assigned account. For example, available capacity can increase if the Capacity Reservation owner increases the size of the Capacity Reservation, or if other consumer accounts stop or terminate their instances running in the Capacity Reservation.
- Billing can be assigned only to a consumer account that is consolidated under the same AWS Organizations payer account. Billing is automatically revoked from the consumer account if they leave the organization, or if the Capacity Reservation is no longer shared with them.
- Only the Capacity Reservation owner can cancel a pending billing assignment request and revoke billing from an assigned account after the request has been accepted.

###### Assign billing of a shared EC2 Capacity Reservation to another account To assign billing of the available capacity of a shared Capacity Reservation to another account, the Capacity Reservation owner must initiate a request to the required account. In the Amazon EC2 console, this request is called a transfer request.
A Capacity Reservation owner can assign billing of the available capacity of Capacity Reservation to an account only if:
- The Capacity Reservation is already shared with that account.
- The account is consolidated under the same AWS Organizations payer account as the Capacity Reservation owner.
Billing is assigned to the specified account only once they accept the request.
When a Capacity Reservation owner initiates a request, an Amazon EventBridge event is sent to the requested account. For more information, see Monitor billing assignment requests for shared Capacity Reservations.
Console To assign billing of a shared Capacity Reservation
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation panel, select Capacity Reservations and then choose the shared Capacity Reservation.
3. In the Billing of available capacity section, choose Assign billing.
4. In the Assign billing screen, select the consumer account to which to assign billing, and then choose Request.
AWS CLI To assign billing of a shared Capacity Reservation Use the associate-capacity-reservation-billing-owner command. For --capacity- reservation-id, specify the ID of the shared Capacity Reservation. For --unused- reservation-billing-owner-id, specify the ID of the AWS account to which to assign billing.

aws ec2 associate-capacity-reservation-billing-owner \ --capacity-reservation-id cr-01234567890abcdef \ --unused-reservation-billing-owner-id 123456789012 PowerShell To assign billing of a shared Capacity Reservation Use the Register-EC2CapacityReservationBillingOwner cmdlet. For - CapacityReservationId, specify the ID of the shared Capacity Reservation. For - UnusedReservationBillingOwnerId, specify the ID of the AWS account to which to assign billing.
Register-EC2CapacityReservationBillingOwner `
    -CapacityReservationId cr-01234567890abcdef `
    -UnusedReservationBillingOwnerId 123456789012
###### View billing assignment requests for shared EC2 Capacity Reservations A Capacity Reservation owner can view only the most recent billing assignment request that they initiated. And consumer accounts can view only the most recent billing assignment requests sent to them.
Requests can be viewed for 24 hours after they enter the cancelled, expired, or revoked state.
After 24 hours, they can no longer be viewed.
Console (Capacity Reservation owner) To view requests you initiated
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation panel, select Capacity Reservations and then choose the shared Capacity Reservation for which to view requests.
3. The Billing of available capacity section shows the most recent request and its current state.
(Consumer account) To requests sent to you
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.

2. In the navigation panel, select Capacity Reservations.
3. If you have pending requests, the Pending billing assignment requests banner appears at the top of the screen. If the banner does not appear, you do not have pending requests.
To view the requests, choose Review requests in the banner.
AWS CLI (Capacity Reservation owner) To view requests you initiated Use the describe-capacity-reservation-billing-requests command. aws ec2 describe-capacity-reservation-billing-requests \ --role odcr-owner (Consumer account) To view requests sent to you Use the describe-capacity-reservation-billing-requests command. aws ec2 describe-capacity-reservation-billing-requests \ --role unused-reservation-billing-owner PowerShell (Capacity Reservation owner) To view requests you initiated Use the Get-EC2CapacityReservationBillingRequest cmdlet.
Get-EC2CapacityReservationBillingRequest `
    -Role odcr-owner (Consumer account) To view requests sent to you Use the Get-EC2CapacityReservationBillingRequest cmdlet.
Get-EC2CapacityReservationBillingRequest `
    -Role unused-reservation-billing-owner A request can be in one of the following states.

State Description pending The request has not been accepted or rejected, but it has not  yet expired. accepted The request was accepted by the specified account.
Billing of  available capacity of the Capacity Reservation is assigned to the consumer account. rejected The request was rejected by the consumer account. cancelled The request was cancelled by the Capacity Reservation owner while it was in  the pending state. revoked Billing was revoked from the consumer account for one of the  following reasons:
- It was explicitly revoked by the Capacity Reservation owner.
- The Capacity Reservation is no longer shared with the consumer   account.
- The consumer account is no longer part of the  AWS organization.

State Description expired The request expired because the consumer account did not  accept or reject it within 12 hours.
###### Accept or reject billing of a shared EC2 Capacity Reservation If you receive a billing assignment request for a Capacity Reservation that is shared with you, you can either accept or reject it. The request remains in the pending state until it is accepted or rejected.
If you accept the request, it enters the accepted state, and billing of any available, or unused, capacity of that Capacity Reservation is assigned to your account from that point onward. After you accept a request, only the Capacity Reservation owner can revoke billing from your account.
If you reject the request, it enters the rejected state, and billing of the available capacity of the Capacity Reservation remains assigned to the Capacity Reservation owner.
Requests expire if they are not accepted or rejected within 12 hours. If a request expires, billing of any unused capacity of the Capacity Reservation remains assigned to the Capacity Reservation owner.
When a request is accepted or rejected, an Amazon EventBridge event is sent to the Capacity Reservation owner's account. When a request expires, an Amazon EventBridge event is sent to the Capacity Reservation owner and the consumer account. For more information, see Monitor billing assignment requests for shared Capacity Reservations.
Console To accept or reject a request
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation panel, select Capacity Reservations.
3. If you have pending requests, the Pending billing assignment requests banner appears at the top of the screen. If the banner does not appear, you do not have pending requests.
To view the requests, choose Review requests in the banner.

4. Select the request to accept or reject, and then choose either Accept or Reject.
AWS CLI To accept a request Use the accept-capacity-reservation-billing-ownership command. For --capacity- reservation-id, specify the ID of the Capacity Reservation for which to accept the request. aws ec2 accept-capacity-reservation-billing-ownership \ --capacity-reservation-id cr-01234567890abcdef To reject a request Use the reject-capacity-reservation-billing-ownership command. For --capacity- reservation-id, specify the ID of the Capacity Reservation for which to reject the request. aws ec2 reject-capacity-reservation-billing-ownership \ --capacity-reservation-id cr-01234567890abcdef PowerShell To accept a request Use the Approve-EC2CapacityReservationBillingOwnership cmdlet.
Approve-EC2CapacityReservationBillingOwnership `
    -CapacityReservationId cr-01234567890abcdef To reject a request Use the Deny-EC2CapacityReservationBillingOwnership cmdlet.
Deny-EC2CapacityReservationBillingOwnership `
    -CapacityReservationId cr-01234567890abcdef

###### Cancel or revoke billing assignment requests for shared EC2 Capacity Reservations Only the Capacity Reservation owner can cancel a pending billing assignment request. If a pending request is cancelled, it enters the cancelled state and billing of any available, or unused, capacity of the Capacity Reservation remains assigned to Capacity Reservation owner.
After a request is accepted, only the Capacity Reservation owner can revoke billing from the assigned account. If billing is revoked, the request enters the revoked state and billing of any available capacity of the Capacity Reservation is reassigned to Capacity Reservation owner.
When a request is cancelled or revoked, Amazon EventBridge events are sent to the Capacity Reservation owner and specified consumer account. For more information, see Monitor billing assignment requests for shared Capacity Reservations.
Console To cancel or revoke a request
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation panel, select Capacity Reservations and then choose the Capacity Reservation for which to cancel or revoke the request.
3. In the Billing of available capacity section, choose Cancel transfer or Revoke transfer, depending on the current state of the request.
AWS CLI To cancel or revoke a request Use the disassociate-capacity-reservation-billing-owner command. For --unused- reservation-billing-owner-id, specify the ID of the AWS account to which the request was sent. aws ec2 disassociate-capacity-reservation-billing-owner \ --capacity-reservation-id cr-01234567890abcdef \ --unused-reservation-billing-owner-id 123456789012 PowerShell To cancel or revoke a request

Use the Unregister-EC2CapacityReservationBillingOwner cmdlet. For - UnusedReservationBillingOwnerId, specify the ID of the AWS account to which the request was sent.
Unregister-EC2CapacityReservationBillingOwner `
    -CapacityReservationId cr-01234567890abcdef `
    -UnusedReservationBillingOwnerId 123456789012
###### Monitor billing assignment requests for shared Capacity Reservations Amazon EC2 sends Amazon EventBridge events when the state of a billing assignment request changes.
- Events are sent to the Capacity Reservation owner when a request enters the following states: accepted | rejected | expired | revoked.
- Events are sent to the requested consumer account when a request enters the following states: pending | expired | cancelled | revoked.
For more information about Amazon EventBridge, see the  Amazon EventBridge User Guide.
The following is the Amazon EventBridge event pattern.
{ "version":"0", "id":"12345678-1234-1234-1234-123456789012", "detail-type":"On-Demand Capacity Reservation Billing Ownership Request pending| accepted|rejected|cancelled|revoked|expired", "source":"aws.ec2", "account":"account_id", "time":"state_change_timestamp", "region":"region", "resources":[ "arn:aws:ec2:region:cr_owner_account_id:capacity-reservation/cr_id"
   ], "detail":{ "capacity-reservation-id":"cr_id", "updateTime":timestamp, "ownerAccountId":"cr_owner_account_id", "unusedReservationChargesOwnerID":"consumer_account_id", "status":"pending|accepted|rejected|cancelled|revoked|expired",

      "statusMessage":"message } } The following is an example of an event that is sent to the Capacity Reservation owner (222222222222) when a consumer account (111111111111) accepts a billing assignment request for a shared Capacity Reservation (cr-01234567890abcdef).
{ "version":"0", "id":"12345678-1234-1234-1234-123456789012", "detail-type":"On-Demand Capacity Reservation Billing Ownership Request accepted", "source":"aws.ec2", "account":"222222222222", "time":"2024-09-01Thh:59:59Z", "region":"us-east-1", "resources":[ "arn:aws:ec2:us-east-1:222222222222:capacity-reservation/cr-01234567890abcdef"
   ], "detail":{ "capacity-reservation-id":"cr-01234567890abcdef", "updateTime":"2024-08-01Thh:59:59Z", "ownerAccountId":"222222222222", "unusedReservationChargesOwnerID":"111111111111", "status":"accepted", "statusMessage":"billing transfer status message"
   } }
##### Shared Capacity Reservation permissions
###### Permissions for owners Owners are responsible for managing and canceling their shared Capacity Reservations. Owners cannot modify instances running in the shared Capacity Reservation that are owned by other accounts. Owners remain responsible for managing instances that they launch into the shared Capacity Reservation.
###### Permissions for consumers Consumers are responsible for managing their instances that are running the shared Capacity Reservation. Consumers cannot modify the shared Capacity Reservation in any way, and they

cannot view or modify instances that are owned by other consumers or the Capacity Reservation owner. Consumers can only view the total capacity and available capacity in the shared reservation.
##### Billing and metering There are no additional charges for sharing Capacity Reservations.
By default, the Capacity Reservation owner is billed for instances that they run inside the Capacity Reservation and for unused reserved capacity, while consumers are billed for the instances that they run inside the shared Capacity Reservation. However, you can assign billing of the available capacity of a shared Capacity Reservation to a specific consumer account. For more information, see Billing assignment for shared Amazon EC2 Capacity Reservations.
If the Capacity Reservation owner belongs to a different payer account and the Capacity Reservation is covered by a Regional Reserved Instance or a Savings Plan, the Capacity Reservation owner continues to be billed for the Regional Reserved Instance or Savings Plan. In these cases, the Capacity Reservation owner pays for the Regional Reserved Instance or Savings Plan, and consumers are billed for the instances that the run in the shared Capacity Reservation.
##### Instance limits All Capacity Reservation usage counts toward the Capacity Reservation owner's On-Demand Instance limits. This includes:
- Unused reserved capacity
- Usage by instances owned by the Capacity Reservation owner
- Usage by instances owned by consumers Instances launched into the shared capacity by consumers count towards the Capacity Reservation owner's On-Demand Instance limit. Consumers' instance limits are a sum of their own On-Demand Instance limits and the capacity available in the shared Capacity Reservations to which they have access.
#### Capacity Reservation Fleets An On-Demand Capacity Reservation Fleet is a group of Capacity Reservations.
A Capacity Reservation Fleet request contains all of the configuration information that's needed to launch a Capacity Reservation Fleet. Using a single request, you can reserve large amounts of

Amazon EC2 capacity for your workload across multiple instance types, up to a target capacity that you specify.
After you create a Capacity Reservation Fleet, you can manage the Capacity Reservations in the fleet collectively by modifying or canceling the Capacity Reservation Fleet.
Topics
- How Capacity Reservation Fleets work
- Considerations
- Pricing
- Capacity Reservation Fleet concepts and planning
- Create a Capacity Reservation Fleet
- Modify a Capacity Reservation Fleet
- Cancel a Capacity Reservation Fleet
- Example Capacity Reservation Fleet configurations
- Using service-linked roles for Capacity Reservation Fleet
##### How Capacity Reservation Fleets work When you create a Capacity Reservation Fleet, the Fleet attempts to create individual Capacity Reservations to meet the total target capacity that you specified in the Fleet request.
The number of instances for which the Fleet reserves capacity depends on the total target capacity and the instance type weights that you specify. The instance type for which it reserves capacity depends on the allocation strategy and instance type priorities that you use.
If there is insufficient capacity at the time the Fleet is created, and it is unable to immediately meet its total target capacity, the Fleet asynchronously attempts to create Capacity Reservations until it has reserved the requested amount of capacity.
When the Fleet reaches its total target capacity, it attempts to maintain that capacity. If a Capacity Reservation in the Fleet is cancelled, the Fleet automatically creates one or more Capacity Reservations, depending on your Fleet configuration, to replace the lost capacity and to maintain its total target capacity.

The Capacity Reservations in the Fleet can't be managed individually. They must be managed collectively by modifying the Fleet. When you modify a Fleet, the Capacity Reservations in the Fleet are automatically updated to reflect the changes.
Currently, Capacity Reservation Fleets support the open instance matching criteria, and all Capacity Reservations launched by a Fleet automatically use this instance matching criteria. With this criteria, new instances and existing instances that have matching attributes (instance type, platform, Availability Zone, and tenancy) automatically run in the Capacity Reservations created by a Fleet. Capacity Reservation Fleets do not support targeted instance matching criteria.
Considerations Keep the following in mind when working with Capacity Reservation Fleets:
- A Capacity Reservation Fleet can be created, modified, viewed, and cancelled using the AWS CLI and AWS API.
- The Capacity Reservations in a Fleet can't be managed individually. They must be managed collectively by modifying or cancelling the Fleet.
- A Capacity Reservation Fleet can't span across Regions.
- A Capacity Reservation Fleet can't span across Availability Zones.
- Capacity Reservations created by a Capacity Reservation Fleet are automatically tagged with the following AWS generated tag:
- Key — aws:ec2-capacity-reservation-fleet
- Value — fleet_id You can use this tag to identify Capacity Reservations that were created by a Capacity Reservation Fleet.
##### Pricing There are no additional charges for using Capacity Reservation Fleets. You are billed for the individual Capacity Reservations that are created by your Capacity Reservation Fleets. For more information about how Capacity Reservations are billed, see Capacity Reservation pricing and billing.

##### Capacity Reservation Fleet concepts and planning The following information describes how to plan a Capacity Reservation Fleet and describes Capacity Reservation Fleet concepts including total target capacity, allocation strategy, instance type weight, and instance type priority.
Topics
- Plan a Capacity Reservation Fleet
- Total target capacity
- Allocation strategy
- Instance type weight
- Instance type priority
###### Plan a Capacity Reservation Fleet When planning your Capacity Reservation Fleet, we recommend that you do the following:
1. Determine the amount of compute capacity that is needed by your workload.
2. Decide on the instance types and Availability Zones that you want to use.
3. Assign each instance type a priority based on your needs and preferences. For more information, see Instance type priority.
4. Create a capacity weighting system that makes sense for your workload. Assign a weight to each instance type and determine your total target capacity. For more information, see Instance type weight and Total target capacity.
5. Determine whether you need the Capacity Reservation indefinitely or only for a specific period of time.
###### Total target capacity The total target capacity defines the total amount of compute capacity that the Capacity Reservation Fleet reserves. You specify the total target capacity when you create the Capacity Reservation Fleet. After the Fleet has been created, Amazon EC2 automatically creates Capacity Reservations to reserve capacity up to the total target capacity.
The number of instances for which the Capacity Reservation Fleet reserves capacity is determined by the total target capacity and the instance type weight that you specify for each instance type in

the Capacity Reservation Fleet (total target capacity/instance type weight=number of instances).
You can assign a total target capacity based on units that are meaningful to your workload. For example, if your workload requires a certain number of vCPUs, you can assign the total target capacity based on the number of vCPUs required. If your workload requires 2048 vCPUs, specify a total target capacity of 2048 and then assign instance type weights based on the number of vCPUs provided by the instance types in the Fleet. For an example, see Instance type weight.
###### Allocation strategy The allocation strategy for your Capacity Reservation Fleet determines how it fulfills your request for reserved capacity from the instance type specifications in the Capacity Reservation Fleet configuration.
Currently, only the prioritized allocation strategy is supported. With this strategy, the Capacity Reservation Fleet creates Capacity Reservations using the priorities that you have assigned to each of the instance type specifications in the Capacity Reservation Fleet configuration. Lower priority values indicate higher priority for use. For example, say you create a Capacity Reservation Fleet that uses the following instance types and priorities:
- m4.16xlarge — priority = 1
- m5.16xlarge — priority = 3
- m5.24xlarge — priority = 2 The Fleet first attempts to create Capacity Reservations for m4.16xlarge. If Amazon EC2 has insufficient m4.16xlarge capacity, the Fleet attempts to create Capacity Reservations for m5.24xlarge. If Amazon EC2 has insufficient m5.24xlarge capacity, the Fleet creates Capacity Reservations for m5.16xlarge.
###### Instance type weight The instance type weight is a weight that you assign to each instance type in the Capacity Reservation Fleet. The weight determines how many units of capacity each instance of that specific instance type counts toward the Fleet's total target capacity.
You can assign weights based on units that are meaningful to your workload. For example, if your workload requires a certain number of vCPUs, you can assign weights based on the number of

vCPUs provided by each instance type in the Capacity Reservation Fleet. In this case, if you create a Capacity Reservation Fleet using m4.16xlarge and m5.24xlarge instances, you would assign weights that correspond to the number of vCPUs for each instance as follows:
- m4.16xlarge — 64 vCPUs, weight = 64 units
- m5.24xlarge — 96 vCPUs, weight = 96 units The instance type weight determines the number of instances for which the Capacity Reservation Fleet reserves capacity. For example, if a Capacity Reservation Fleet with a total target capacity of 384 units uses the instance types and weights in the preceding example, the Fleet could reserve capacity for 6 m4.16xlarge instances (384 total target capacity/64 instance type weight=6 instances), or 4 m5.24xlarge instances (384 / 96 = 4).
If you do not assign instance type weights, or if you assign an instance type weight of 1, the total target capacity is based purely on instance count. For example, if a Capacity Reservation Fleet with a total target capacity of 384 units uses the instance types in the preceding example, but omits the weights or specifies a weight of 1 for both instance types, the Fleet could reserve capacity for either 384 m4.16xlarge instances or 384 m5.24xlarge instances.
###### Instance type priority The instance type priority is a value that you assign to the instance types in the Fleet. The priorities are used to determine which of the instance types specified for the Fleet should be prioritized for use.
Lower priority values indicate a higher priority for use.
##### Create a Capacity Reservation Fleet When you create a Capacity Reservation Fleet it automatically creates Capacity Reservations for the instance types specified in the Fleet request, up to the specified total target capacity.
The number of instances for which the Capacity Reservation Fleet reserves capacity depends on the total target capacity and instance type weights that you specify in the request. For more information, see Instance type weight and Total target capacity.
When you create the Fleet, you must specify the instance types to use and a priority for each of those instance types. For more information, see Allocation strategy and Instance type priority.

Note The AWSServiceRoleForEC2CapacityReservationFleet service-linked role is automatically created in your account the first time that you create a Capacity Reservation Fleet. For more information, see Using service-linked roles for Capacity Reservation Fleet.
Currently, Capacity Reservation Fleets support the open instance matching criteria only.
AWS CLI To create a Capacity Reservation Fleet Use the create-capacity-reservation-fleet command. aws ec2 create-capacity-reservation-fleet \ --total-target-capacity 24 \ --allocation-strategy prioritized \ --instance-match-criteria open \ --tenancy default \ --end-date 2021-12-31T23:59:59.000Z \ --instance-type-specifications file://instanceTypeSpecification.json The following are the contents of instanceTypeSpecification.json.
[ { "InstanceType": "m5.xlarge", "InstancePlatform": "Linux/UNIX", "Weight": 3.0, "AvailabilityZone":"us-east-1a", "EbsOptimized": true, "Priority" : 1 } ]
The following is example output.
{ "Status": "submitted", "TotalFulfilledCapacity": 0.0,

    "CapacityReservationFleetId": "crf-abcdef01234567890", "TotalTargetCapacity": 24 } PowerShell To create a Capacity Reservation Fleet Use the New-EC2CapacityReservationFleet cmdlet.
New-EC2CapacityReservationFleet `
    -TotalTargetCapacity 24 `
    -AllocationStrategy "prioritized" `
    -InstanceMatchCriterion "open" `
    -Tenancy "default" `
    -EndDate 2021-12-31T23:59:59.000Z `
    -InstanceTypeSpecification $specification The specification is defined as follows.
$specification = New-Object Amazon.EC2.Model.ReservationFleetInstanceSpecification $specification.InstanceType = "m5.xlarge"
$specification.InstancePlatform = "Linux/UNIX"
$specification.Weight = 3.0 $specification.AvailabilityZone = "us-east-1a"
$specification.EbsOptimized = $true $specification.Priority = 1
##### Modify a Capacity Reservation Fleet You can modify the total target capacity and date of a Capacity Reservation Fleet at any time.
When you modify the total target capacity of a Capacity Reservation Fleet, the Fleet automatically creates new Capacity Reservations, or modifies or cancels existing Capacity Reservations in the Fleet to meet the new total target capacity. When you modify the end date for the Fleet, the end dates for all of the individual Capacity Reservations are updated accordingly.
Considerations
- After you modify a Fleet, its status transitions to modifying. You can't attempt additional modifications to a Fleet while it is in the modifying state.

- You can't modify the tenancy, Availability Zone, instance types, instance platforms, priorities, or weights used by a Capacity Reservation Fleet. If you need to change any of these parameters, you might need to cancel the existing Fleet and create a new one with the required parameters.
- You can't specify --end-date and --remove-end-date in the same command.
AWS CLI To modify a Capacity Reservation Fleet Use the modify-capacity-reservation-fleet command.
Example 1: Modify total target capacity aws ec2 modify-capacity-reservation-fleet \ --capacity-reservation-fleet-id crf-01234567890abcedf \ --total-target-capacity 160 Example 2: Modify end date aws ec2 modify-capacity-reservation-fleet \ --capacity-reservation-fleet-id crf-01234567890abcedf \ --end-date 2021-07-04T23:59:59.000Z Example 3: Remove end date aws ec2 modify-capacity-reservation-fleet \ --capacity-reservation-fleet-id crf-01234567890abcedf \ --remove-end-date PowerShell To modify a Capacity Reservation Fleet Use the Edit-EC2CapacityReservationFleet cmdlet.
Example 1: Modify total target capacity Edit-EC2CapacityReservationFleet `
    -CapacityReservationFleetId crf-01234567890abcedf `
    -TotalTargetCapacity 160

Example 2: Modify end date Edit-EC2CapacityReservationFleet `
    -CapacityReservationFleetId crf-01234567890abcedf `
    -EndDate 2021-07-04T23:59:59.000Z Example 3: Remove end date Edit-EC2CapacityReservationFleet `
    -CapacityReservationFleetId crf-01234567890abcedf `
    -RemoveEndDate
##### Cancel a Capacity Reservation Fleet When you no longer need a Capacity Reservation Fleet and the capacity it reserves, you can cancel it. When you cancel a Fleet, its status changes to cancelled and it can no longer create new Capacity Reservations. Additionally, all of the individual Capacity Reservations in the Fleet are canceled. The instances that were previously running in the reserved capacity continue to run normally in the shared capacity.
AWS CLI To cancel a Capacity Reservation Fleet Use the cancel-capacity-reservation-fleets command. aws ec2 cancel-capacity-reservation-fleets \ --capacity-reservation-fleet-ids crf-abcdef01234567890 The following is example output.
{ "SuccessfulFleetCancellations": [ { "CurrentFleetState": "cancelling", "PreviousFleetState": "active", "CapacityReservationFleetId": "crf-abcdef01234567890"
        } ], "FailedFleetCancellations": []

} PowerShell To cancel a Capacity Reservation Fleet Use the Stop-EC2CapacityReservationFleet cmdlet.
Stop-EC2CapacityReservationFleet `
    -CapacityReservationFleetId crf-abcdef01234567890
##### Example Capacity Reservation Fleet configurations The following example creates a Capacity Reservation Fleet that uses two instance types: m5.4xlarge and m5.12xlarge.
It uses a weighting system based on the number of vCPUs provided by the specified instance types.
The total target capacity is 480 vCPUs. The m5.4xlarge provides 16 vCPUs and gets a weight of 16, while the m5.12xlarge provides 48 vCPUs and gets a weight of 48. This weighting system configures the Capacity Reservation Fleet to reserve capacity for either 30 m5.4xlarge instances (480/16=30), or 10 m5.12xlarge instances (480/48=10).
The Fleet is configured to prioritize the m5.12xlarge capacity and gets priority of 1, while the m5.4xlarge gets a lower priority of 2. This means that the fleet will attempt to reserve the m5.12xlarge capacity first, and only attempt to reserve the m5.4xlarge capacity if Amazon EC2 has insufficient m5.12xlarge capacity.
The Fleet reserves the capacity for Windows instances and the reservation automatically expires on October 31, 2021 at 23:59:59 UTC. aws ec2 create-capacity-reservation-fleet \ --total-target-capacity 480 \ --allocation-strategy prioritized \ --instance-match-criteria open \ --tenancy default \ --end-date 2021-10-31T23:59:59.000Z \ --instance-type-specifications file://instanceTypeSpecification.json The following is the contents of instanceTypeSpecification.json.

[ { "InstanceType": "m5.4xlarge", "InstancePlatform":"Windows", "Weight": 16, "AvailabilityZone":"us-east-1a", "EbsOptimized": true, "Priority" : 2 }, { "InstanceType": "m5.12xlarge", "InstancePlatform":"Windows", "Weight": 48, "AvailabilityZone":"us-east-1a", "EbsOptimized": true, "Priority" : 1 } ]
##### Using service-linked roles for Capacity Reservation Fleet On-Demand Capacity Reservation Fleet uses AWS Identity and Access Management (IAM) service- linked roles. A service-linked role is a unique type of IAM role that is linked directly to Capacity Reservation Fleet. Service-linked roles are predefined by Capacity Reservation Fleet and include all the permissions that the service requires to call other AWS services on your behalf.
A service-linked role makes setting up Capacity Reservation Fleet easier because you don't have to manually add the necessary permissions. Capacity Reservation Fleet defines the permissions of its service-linked roles, and unless defined otherwise, only Capacity Reservation Fleet can assume its roles. The defined permissions include the trust policy and the permissions policy, and that permissions policy cannot be attached to any other IAM entity.
You can delete a service-linked role only after first deleting their related resources. This protects your Capacity Reservation Fleet resources because you can't inadvertently remove permission to access the resources.
###### Service-linked role permissions for Capacity Reservation Fleet Capacity Reservation Fleet uses the service-linked role named AWSServiceRoleForEC2CapacityReservationFleet to create, describe, modify, and cancel Capacity Reservations in a Capacity Reservation Fleet on your behalf.

The AWSServiceRoleForEC2CapacityReservationFleet service-linked role trusts the following entity to assume the role:
- capacity-reservation-fleet.amazonaws.com The role uses the AWSEC2CapacityReservationFleetRolePolicy AWS managed policy. For more information, see AWS managed policy: AWSEC2CapacityReservationFleetRolePolicy.
You must configure permissions to allow an IAM entity (such as a user, group, or role) to create, edit, or delete a service-linked role. For more information, see Service-linked role permissions in the IAM User Guide.
###### Create a service-linked role for Capacity Reservation Fleet You don't need to manually create a service-linked role. When you create a Capacity Reservation Fleet using the create-capacity-reservation-fleet AWS CLI command or the CreateCapacityReservationFleet API, the service-linked role is automatically created for you.
If you delete this service-linked role, and then need to create it again, you can use the same process to recreate the role in your account. When you create a Capacity Reservation Fleet, Capacity Reservation Fleet creates the service-linked role for you again.
###### Edit a service-linked role for Capacity Reservation Fleet Capacity Reservation Fleet does not allow you to edit the AWSServiceRoleForEC2CapacityReservationFleet service-linked role. After you create a service- linked role, you cannot change the name of the role because various entities might reference the role. However, you can edit the description of the role using IAM. For more information, see Edit a service-linked role description in the IAM User Guide.
###### Delete a service-linked role for Capacity Reservation Fleet If you no longer need to use a feature or service that requires a service-linked role, we recommend that you delete that role. That way you don't have an unused entity that is not actively monitored or maintained. However, you must delete the resources for your service-linked role before you can manually delete it.

Note If the Capacity Reservation Fleet service is using the role when you try to delete the resources, then the deletion might fail. If that happens, wait for a few minutes and try the operation again.
To delete the AWSServiceRoleForEC2CapacityReservationFleet service-linked role
1. Use the delete-capacity-reservation-fleet AWS CLI command or the DeleteCapacityReservationFleet API to delete the Capacity Reservation Fleets in your account.
2. Use the IAM console, the AWS CLI, or the AWS API to delete the AWSServiceRoleForEC2CapacityReservationFleet service-linked role. For more information, see Delete a service-linked role in the IAM User Guide.
###### Supported Regions for Capacity Reservation Fleet service-linked roles Capacity Reservation Fleet supports using service-linked roles in all of the Regions where the service is available. For more information, see AWS Regions and Endpoints.
#### Monitor Capacity Reservations usage with CloudWatch metrics With CloudWatch metrics, you can efficiently monitor your Capacity Reservations and identify unused capacity by setting CloudWatch alarms to notify you when usage thresholds are met.
This can help you maintain a constant Capacity Reservation volume and achieve a higher level of utilization.
Capacity Reservations send metric data to CloudWatch every five minutes. Metrics are not supported for Capacity Reservations that are active for less than five minutes.
For more information about viewing metrics in the CloudWatch console, see Using Amazon CloudWatch Metrics. For more information about creating alarms, see Creating Amazon CloudWatch Alarms.
Contents
- Capacity Reservation usage metrics
- Capacity Reservation metric dimensions

- View CloudWatch metrics for Capacity Reservations
##### Capacity Reservation usage metrics The AWS/EC2CapacityReservations namespace includes the following usage metrics you can use to monitor and maintain on-demand capacity within thresholds you specify for your reservation.
Metric Description UsedInstanceCount The number of instances that are currently in use.
Unit: Count AvailableInstanceCount The number of instances that are available.
Unit: Count TotalInstanceCount The total number of instances you have reserved.
Unit: Count InstanceUtilization The percentage of reserved capacity instances that are  currently in use.
Unit: Percent
##### Capacity Reservation metric dimensions You can use the following dimensions to refine the metrics listed in the previous table within the selected Region and account.
Dimension Description (No dimension)

Dimension Description This dimension filters the specified metric for all Capacity Reservations.
CapacityReservatio nId This dimension filters the specified metric for the identified Capacity Reservation.
InstanceType This dimension filters the specified metric for the identified instance type.
AvailabilityZone This dimension filters the specified metric for the identified Availability Zone.
InstanceMatchCrite ria This dimension filters the specified metric for the identified instance match criteria (open or   targeted).
InstancePlatform This dimension filters the specified metric data for the  ident ified platform.
Tenancy This dimension filters the specified metric for the identified tenancy.
##### View CloudWatch metrics for Capacity Reservations Metrics are grouped first by the service namespace, and then by the supported dimensions. You can use the following procedures to view the metrics for your Capacity Reservations.
To view Capacity Reservation metrics using the CloudWatch console
1. Open the CloudWatch console at https://console.aws.amazon.com/cloudwatch/.
2. If necessary, change the Region. From the navigation bar, select the Region where your Capacity Reservation resides. For more information, see Regions and Endpoints.
3. In the navigation pane, choose Metrics.

4. For All metrics, choose EC2 Capacity Reservations.
5. Choose from the preceding metric dimensions Across All Capacity Reservations, By Capacity Reservation, By Instance Type, By Availability Zone, By Platform, By Instance Match Criteria or By Tenancy and metrics will be grouped by No dimension, CapacityReservationId, InstanceType, AvailabilityZone, Platform, InstanceMatchCriteria, and Tenancy respectively.
6. To sort the metrics, use the column heading. To graph a metric, select the checkbox next to the metric.
To view Capacity Reservation metrics using the AWS CLI Use the following list-metrics command: aws cloudwatch list-metrics --namespace "AWS/EC2CapacityReservations"
#### Monitor Capacity Reservation underutilization You can monitor Capacity Reservation underutilization using the following:
Topics
- Amazon EventBridge events
- Email and AWS Health Dashboard notifications
##### Amazon EventBridge events AWS Health sends events to Amazon EventBridge when a Capacity Reservation in your account is below 20 percent usage over certain periods. With EventBridge, you can establish rules that trigger programmatic actions in response to such events. For example, you can create a rule that automatically cancels a Capacity Reservation when its utilization drops below 20 percent utilization over a 7-day period.
Events in EventBridge are represented as JSON objects. The fields that are unique to the event are contained in the "detail" section of the JSON object. The "event" field contains the event name.
The "result" field contains the completed status of the action that triggered the event. For more information, see Amazon EventBridge event patterns in the Amazon EventBridge User Guide.
For more information, see the Amazon EventBridge User Guide.

This feature is not supported in AWS GovCloud (US).
###### Events AWS Health sends the following events when capacity usage for a Capacity Reservation is below 20 percent.
- AWS_EC2_ODCR_UNDERUTILIZATION_NOTIFICATION The following is an example of an event that is generated when a newly created Capacity Reservation is below 20 percent capacity usage over a 24-hour period.
{ "version": "0", "id": "b3e00086-f271-12a1-a36c-55e8ddaa130a", "detail-type": "AWS Health Event", "source": "aws.health", "account": "123456789012", "time": "2023-03-10T12:03:38Z", "region": "ap-south-1", "resources": [ "cr-01234567890abcdef"
    ], "detail": { "eventArn": "arn:aws:health:ap-south-1::event/EC2/ AWS_EC2_ODCR_UNDERUTILIZATION_NOTIFICATION/ AWS_EC2_ODCR_UNDERUTILIZATION_NOTIFICATION_cr-01234567890abcdef-6211-4d50-9286-0c9fbc243f04", "service": "EC2", "eventTypeCode": "AWS_EC2_ODCR_UNDERUTILIZATION_NOTIFICATION", "eventTypeCategory": "accountNotification", "startTime": "Fri, 10 Mar 2023 12:03:38 GMT", "endTime": "Fri, 10 Mar 2023 12:03:38 GMT", "eventDescription": [ { "language": "en_US", "latestDescription": "A description of the event will be provided here"
            } ], "affectedEntities": [ { "entityValue": "cr-01234567890abcdef"
            }

        ]
    } }
- AWS_EC2_ODCR_UNDERUTILIZATION_NOTIFICATION_SUMMARY The following is an example of an event that is generated when one or more Capacity Reservation is below 20 percent capacity usage over a 7-day period.
{ "version": "0", "id":"7439d42b-3c7f-ad50-6a88-25e2a70977e2", "detail-type": "AWS Health Event", "source": "aws.health", "account": "123456789012", "time": "2023-03-07T06:06:01Z", "region": "us-east-1", "resources": [ "cr-01234567890abcdef | us-east-1b | t3.medium | Linux/UNIX | 0.0%", "cr-09876543210fedcba | us-east-1a | t3.medium | Linux/UNIX | 0.0%"
    ], "detail": { "eventArn": "arn:aws:health:us-east-1::event/ EC2/AWS_EC2_ODCR_UNDERUTILIZATION_NOTIFICATION_SUMMARY/ AWS_EC2_ODCR_UNDERUTILIZATION_NOTIFICATION_SUMMARY_726c1732-d6f6-4037-b9b8- bec3c2d3ba65", "service": "EC2", "eventTypeCode": "AWS_EC2_ODCR_UNDERUTILIZATION_NOTIFICATION_SUMMARY", "eventTypeCategory": "accountNotification", "startTime": "Tue, 7 Mar 2023 06:06:01 GMT", "endTime": "Tue, 7 Mar 2023 06:06:01 GMT", "eventDescription": [ { "language": "en_US", "latestDescription": "A description of the event will be provided here"
            } ], "affectedEntities": [ { "entityValue": "cr-01234567890abcdef | us-east-1b | t3.medium | Linux/UNIX | 0.0%"
            }, {

                "entityValue": "cr-09876543210fedcba | us-east-1a | t3.medium | Linux/UNIX | 0.0%"
            } ]
    } }
###### Create an EventBridge rule To receive email notifications when your Capacity Reservation utilization drops below 20 percent, create an Amazon SNS topic, and then create an EventBridge rule for the AWS_EC2_ODCR_UNDERUTILIZATION_NOTIFICATION event.
To create the Amazon SNS topic
1. Open the Amazon SNS console at https://console.aws.amazon.com/sns/v3/home.
2. In the navigation pane, choose Topics, and then choose Create topic.
3. For Type, choose Standard.
4. For Name, enter a name for the new topic.
5. Choose Create topic.
6. Choose Create subscription.
7. For Protocol, choose Email, and then for Endpoint, enter the email address that receives the notifications.
8. Choose Create subscription.
9. The email address entered above will receive email message with the following subject line:
AWS Notification - Subscription Confirmation. Follow the directions to confirm your subscription.
To create the EventBridge rule
1. Open the Amazon EventBridge console at https://console.aws.amazon.com/events/.
2. In the navigation pane, choose Rules, and then choose Create rule.
3. For Name, enter a name for the new rule.
4. For Rule type, choose Rule with an event pattern.
5. Choose Next.

6. In the Event pattern, do the following: a.
For Event source, choose AWS services. b.
For AWS service, choose AWS Health. c.
For Event type, choose EC2 ODCR Underutilization Notification.
7. Choose Next.
8. For Target 1, do the following: a.
For Target types, choose AWS service. b.
For Select a target, choose SNS topic. c.
For Topic, choose the topic that you created earlier.
9. Choose Next and then Next again.
10. Choose Create rule.
##### Email and AWS Health Dashboard notifications AWS Health sends the following email and Health Dashboard notifications when capacity utilization for Capacity Reservations in your account drops below 20 percent.
- Individual notifications for each newly created Capacity Reservation that has been below 20 percent utilization over the last 24-hour period.
- A summary notification for all Capacity Reservations that have been below 20 percent utilization over the last 7-day period.
The email notifications and Health Dashboard notifications are sent to the email address associated with the AWS account that owns the Capacity Reservations. The notifications include the following information:
- The ID of the Capacity Reservation.
- The Availability Zone of the Capacity Reservation.
- The average utilization rate for the Capacity Reservation.
- The instance type and platform (operating system) of the Capacity Reservation.
Additionally, when capacity utilization for a Capacity Reservation in your account drops below 20 percent over a 24-hour and 7-day period, AWS Health sends events to EventBridge. With

EventBridge, you can create rules that activate automatic actions, such as sending email notifications or triggering AWS Lambda functions, in response to such events. For more information, see Monitor Capacity Reservation underutilization.
#### Monitor state changes for future-dated Capacity Reservations Amazon EC2 sends an event to Amazon EventBridge when the state of a future-dated Capacity Reservation changes.
The following is example of this event. In this example, the future-dated Capacity Reservation entered the scheduled state. Note the state highlighted in the detail-type field.
{ "version":"0", "id":"12345678-1234-1234-1234-123456789012", "detail-type":"EC2 Capacity Reservation Scheduled", "source":"aws.ec2", "account":"123456789012", "time":"yyyy-mm-ddThh:mm:ssZ", "region":"us-east-1", "resources":[ "arn:aws:ec2:us-east-1:123456789012:capacity-reservation/cr-1234567890abcdefg"
   ], "detail":{ "capacity-reservation-id":"cr-1234567890abcdefg", "state":"scheduled"
   } } The possible values for the detail-type field are:
- Scheduled
- Active
- Delayed
- Unsupported
- Failed
- Expired For more information about these states, see View the state of a Capacity Reservation.

You can create Amazon EventBridge events that monitor for these events and then trigger specific actions when they occur. For more information, see Creating rules that react to events in Amazon EventBridge.
To create a rule that monitors for all state change events, you can use the following event pattern.
{ "source": ["aws.ec2"], "detail-type": [{ "prefix": "EC2 Capacity Reservation"
  }]
} To create a rule that monitors for only specific state changes, you can use the following event pattern.
{ "source": ["aws.ec2"], "detail-type": [{ "prefix": "EC2 Capacity Reservation state"
  }]
} For example, the following event pattern monitors for events that are sent when a future-dated Capacity Reservation enters the active state.
{ "source": ["aws.ec2"], "detail-type": [{ "prefix": "EC2 Capacity Reservation Active"
  }]
}
#### Interruptible Capacity Reservations Interruptible Capacity Reservations help you make unused capacity temporarily available for other workloads within your account. This gives you control to reclaim capacity when needed. When you reclaim capacity, any instances running inside the interruptible reservation are terminated. After creating an interruptible reservation, you can share it with additional AWS accounts or your AWS organization using AWS Resource Access Manager (RAM).

Use interruptible Capacity Reservations when you have unused reserved capacity during off-peak periods, between deployments, or when workloads scale down. If you know another team that could use this capacity, you can make it available by creating an interruptible Capacity Reservation.
When your critical workload needs capacity back, you can reclaim it.
You can use interruptible Capacity Reservations as one of the following:
- Capacity owner – You own the source Capacity Reservation and create the interruptible Capacity Reservation to share unused capacity with other teams while retaining control to reclaim it when needed.
- Capacity consumer – You launch instances into shared interruptible reservations, understanding that your instances may be terminated when the owner reclaims capacity.
Topics
- How it works
- Billing
- Considerations
- Interruptible Capacity Reservations for capacity owners
- Interruptible Capacity Reservations for capacity consumers
- Monitor interruptible Capacity Reservations with EventBridge and CloudTrail
##### How it works To make unused capacity available to other teams, create an interruptible reservation by specifying the number of unused instances you want to share from your source reservation. When you create the interruptible reservation, we transfer these instances from your source reservation to the new interruptible reservation within your account.
We retain the association between the source reservation and the interruptible Capacity Reservation. As a result, when you reclaim your capacity, any running consumer instances are terminated, and the capacity is restored to your original source reservation.
Key features:
- Make unused capacity temporarily available while maintaining control to reclaim it
- Reclaim capacity at any time. For more information, see Reclamation process and tracking

- Share with additional accounts or your AWS organization using AWS Resource Access Manager (RAM)
Billing When you create an interruptible reservation, you're billed for it as an independent new reservation. This splits your billing:
- Source reservation: You're billed for total capacity minus allocated capacity
- Interruptible reservation: You're billed for the allocated capacity For more information about On-Demand Capacity Reservation billing, see Capacity Reservation pricing and billing.
Considerations Before using interruptible Capacity Reservations, review the following limitations and requirements that apply to capacity owners and consumers.
###### Capacity owners
- You cannot directly modify or cancel an interruptible Capacity Reservation. To edit it, update the capacity allocated from the source Capacity Reservation.
- You can only view, launch, tag, share, and assign billing for interruptible reservations.
- You can create only one interruptible allocation per source Capacity Reservation.
###### Capacity consumers
- Interruptible Capacity Reservations are by default targeted Capacity Reservations, so you need to target them in your instance launch.
- You can't add interruptible Capacity Reservations to capacity reservation groups.
- We recommend that you only use interruptible Capacity Reservations for applications that can be interrupted.
- Your instances will be terminated when the owner reclaims capacity - there is no fallback to On- Demand or Spot. For more information, see Interruption experience.

##### Interruptible Capacity Reservations for capacity owners The capacity owner is the account that owns the source Capacity Reservation and creates the interruptible Capacity Reservation to share unused capacity with other teams while retaining control to reclaim it when needed.
This section covers how you (the capacity owner) can create, modify, reclaim, and track an interruptible Capacity Reservation.
Topics
- Creating an interruptible Capacity Reservation
- View your interruptible Capacity Reservation
- Modifying your interruptible Capacity Reservation
- Reclamation process and tracking
- Sharing interruptible reservations
###### Creating an interruptible Capacity Reservation Create an interruptible Capacity Reservation to make unused capacity from your source reservation available for other workloads while maintaining control to reclaim it when needed.
Prerequisites Before creating an interruptible allocation, ensure your source On-Demand Capacity Reservation meets these requirements:
- Your Capacity Reservation must be in active state with no end date set. You can't create allocations from reservations that are pending, expired, cancelled, or have scheduled end dates.
- Your Capacity Reservation must have available capacity for allocation. You can only allocate available instances (also called unused capacity).
- You can create only one interruptible allocation per source Capacity Reservation. If an allocation already exists, you must modify or cancel it before creating a new one.
- You can allocate a maximum of 1000 instances at once to an interruptible Capacity Reservation.
Use can use the console or the AWS CLI to create an interruptible Capacity Reservation.

Console To create an interruptible Capacity Reservation
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. Choose Capacity Reservations.
3. Select your Capacity Reservation.
4. Choose Actions, Create interruptible allocation.
5. For Instances to allocate, enter the number of instances to allocate.
6. (Optional) Add tags.
7. Choose Create interruptible capacity allocation.
AWS CLI To create an interruptible Capacity Reservation Use the create-interruptible-capacity-reservation-allocation command: aws ec2 create-interruptible-capacity-reservation-allocation \ --capacity-reservation-id cr-1234567890abcdef0 \ --instance-count 10
###### View your interruptible Capacity Reservation After creating an interruptible Capacity Reservation, you can view the interruptible reservation in your account or from a specific resource.
###### View all interruptible Capacity Reservations in your account Use the following procedure to view the interruptible Capacity Reservations in your account.
Console To view the interruptible Capacity Reservations in your account
1. Go to the Capacity Reservations page in the console.
2. Look for reservations with Interruptible in the type column.
3. Select the interruptible reservation to view details.

AWS CLI To view the interruptible Capacity Reservations in your account aws ec2 describe-capacity-reservations \ --capacity-reservation-id cr-interruptible-id \ --filters Name=interruptible,Values=true
###### View interruptible Capacity Reservation from a specific source Use the following procedure to view the interruptible Capacity Reservation created from a specific source Capacity Reservation. aws ec2 describe-capacity-reservations \ --capacity-reservation-id cr-source-id In the response, you'll find an interruptibleCapacityAllocations object that contains the interruptible Capacity Reservation ID and allocation details. For information about the response structure, see InterruptibleCapacityAllocation in the Amazon EC2 API Reference.
###### Modifying your interruptible Capacity Reservation Use the following procedures to edit or cancel your interruptible Capacity Reservation.
Note
- When you reduce the allocation, we first reclaim available instances, then running instances, until we meet the requested count. If we can meet the count entirely with available instances, no termination occurs. All modifications to allocated instance count are done through the source Capacity Reservation, not directly on the interruptible Capacity Reservation.
- You can only modify an interruptible Capacity Reservation by a maximum of 1000 instances at once (increase or decrease).
###### Edit your interruptible Capacity Reservation Use the following procedure to edit your interruptible Capacity Reservation.

Console
1. From the source Capacity Reservation details page, choose Actions. Then, Edit interruptible Capacity Reservation.
2. For Instances to allocate, enter the new number:
- Add more capacity to share
- Reclaim capacity to your source Capacity Reservation
3. Choose Update.
AWS CLI aws ec2 update-interruptible-capacity-reservation-allocation \ --capacity-reservation-id cr-1234567890abcdef0 \ --target-instance-count 80
###### Cancel your interruptible Capacity Reservation Use the following procedure to permanently remove the allocation and return all capacity.
Console
1. From the source Capacity Reservation details page, navigate to the interruptible capacity allocation details.
2. Choose Edit interruptible allocation.
3. For Instance count, enter 0.
4. Choose Update.
AWS CLI aws ec2 update-interruptible-capacity-reservation-allocation \ --capacity-reservation-id cr-1234567890abcdef0 \ --target-instance-count 0

###### Reclamation process and tracking When you reclaim capacity:
- Running instances receive a 2-minute interruption warning through EventBridge events.
- After the notice period, running instances in the reclaimed capacity enter a shutting down state and get terminated.
- When terminated, the reclaimed instances become available in your source Capacity Reservation for immediate use.
- Your allocation status changes from updating to active when complete.
Complete reclamation can take a few minutes depending on instance type and shutdown time. For more information about the EventBridge notification you receive when the process is complete, see Reclamation completion.
###### Track reclamation status Monitor reclamation progress by describing your source reservation: aws ec2 describe-capacity-reservations \ --capacity-reservation-id cr-1234567890abcdef0 The response shows these fields within the interruptibleCapacityAllocation object:
- instance-count: Current allocated instances
- target-instance-count: Requested quantity after reclamation
- status: updating during reclamation and active when complete
###### Sharing interruptible reservations You can share interruptible reservations only within your AWS organization using AWS Resource Access Manager (RAM).
Considerations:
- If a consumer account leaves your organization, the interruptible reservation is automatically unshared from that account.
- Any instances running in the unshared reservation are eventually terminated.

- All other sharing functionality works the same as standard Capacity Reservations.
For complete sharing procedures, see Sharing Capacity Reservations.
##### Interruptible Capacity Reservations for capacity consumers The capacity consumer is the account that launches instances into shared interruptible Capacity Reservations, understanding that their instances may be terminated when the owner reclaims capacity.
This section covers how you (the capacity consumer) can launch instances into an interruptible Capacity Reservation and learn about what happens when capacity is reclaimed by the owner.
Topics
- View an interruptible Capacity Reservation
- Launch instances into interruptible reservations
- Interruption experience
###### View an interruptible Capacity Reservation Use the following procedures to view an interruptible Capacity Reservation.
Console To view interruptible Capacity Reservations in your account
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. Choose Capacity Reservations.
3. In the Type column, look for reservations marked as Interruptible.
4. Note the reservation IDs for use in your instance launches.
AWS CLI To find all interruptible Capacity Reservations in your account Use the describe-capacity-reservations command: aws ec2 describe-capacity-reservations \

--filters Name=state,Values=active Look for reservations where Interruptible is set to true in the response.
To filter specifically for interruptible reservations Use the following command: aws ec2 describe-capacity-reservations \ --capacity-reservation-ids cr-example123 \ --query 'CapacityReservations[?Interruptible==`true`]'
Note Interruptible Capacity Reservations are by default targeted Capacity Reservations, so you need to target them specifically in your instance launch. Unlike open reservations, interruptible reservations will not automatically cover matching instances. You must explicitly specify the reservation ID when launching.
###### Launch instances into interruptible reservations Use the following procedure to launch Amazon EC2 instances into interruptible Capacity Reservations within your account.
Note We recommend that you only use interruptible Capacity Reservations for applications that can be interrupted.
Console To launch instances into interruptible Capacity Reservations
1. Open the Amazon Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. From the Amazon EC2 dashboard, choose Launch instance.
3. Configure your instance settings.

4. In Advanced details for Capacity Reservation, choose Launch interruptible instances in your active reservation.
5. Select the interruptible reservation ID and the new instance purchasing option.
6. Choose Launch instance.
AWS CLI aws ec2 run-instances \ --instance-type m5.large \ --count 2 \ --image-id ami-12345678 \ --instance-market-options '{ "MarketType": "interruptible-capacity-reservation"
}' \ --capacity-reservation-specification '{ "CapacityReservationTarget": { "CapacityReservationId": "cr-abcdef1234567890"
    } }'
###### Launch instances with Auto Scaling Groups You can also launch instances into interruptible reservations using Auto Scaling Groups with launch templates. Configure the launch template with the interruptible market type and reservation ID, then create your Auto Scaling Group using that template. For more information, see Interruptible Capacity Reservations with EC2 Auto Scaling.
###### Interruption experience When capacity is reclaimed by the owner, you receive an interruption notice 2 minutes before instance termination. This warning comes through EventBridge events, giving you time to:
- Save your work or checkpoint your applications
- Shut down processes
- Prepare for instance termination The EventBridge event includes details about which instances will be terminated and the exact termination time. For more information, see Instance interruption warning.

##### Monitor interruptible Capacity Reservations with EventBridge and CloudTrail Interruptible Capacity Reservations send EventBridge notifications and CloudTrail events to help you monitor and respond to capacity changes.
Topics
- EventBridge notifications
- CloudTrail events
###### EventBridge notifications You receive two types of EventBridge notifications. For information about how to set up EventBridge notifications, see Creating Amazon EventBridge rules.
###### Instance interruption warning If you're running instances in an interruptible reservation, you receive this notification 2 minutes before your instances are terminated:
{ "version": "0", "id": "12345678-1234-1234-1234-123456789012", "detail-type": "EC2 Capacity Reservation Instance Interruption Warning", "source": "aws.ec2", "account": "[instance owner Account ID]", "time": "[Current time in yyyy-mm-ddThh:mm:ssZ]", "resources": "[instance arn]", "region": "[region]", "detail": { "instance-id": "[instance-id]", "instance-action": "terminate", "instance-termination-time": "yyyy-mm-ddThh:mm:ssZ", "azId": "[availability-zone-id]"
    } }
###### Reclamation completion If you own the source reservation, you receive this notification when capacity reclamation finishes:
{ "version": "0",

    "id": "12345678-1234-1234-1234-123456789012", "detail-type": "EC2 Interruptible Capacity Reservation Allocation Reclamation Completed", "source": "aws.ec2", "account": "[source Capacity Reservation Owner Account ID]", "time": "[Current time in yyyy-mm-ddThh:mm:ssZ]", "region": "us-east-1", "resources": ["source_cr_arn"], "detail": { "sourceCapacityReservationId": "string", "instanceType": "string", "availabilityZoneId": "string", "TotalInstanceCount": "current total count in the source", "ReclaimedInstanceCount": "count of instances added to the source", "targetInstanceCount": "number"
    } }
###### CloudTrail events CloudTrail logs these events for interruptible Capacity Reservations:
- InterruptibleCapacityReservationCreated — When you create an interruptible allocation
- InterruptibleCapacityReservationAllocationUpdated — When you modify the allocation
- InterruptibleCapacityReservationCancelled — When you cancel the allocation
- CapacityReservationModified — When we modify the source reservation for allocation
- InterruptibleCapacityReservationInstancesTerminated — When we terminate instances during reclamation
### Capacity Blocks for ML Capacity Blocks for ML allow you to reserve GPU-based accelerated computing instances on a future date to support your short duration machine learning (ML) workloads. Instances that run inside a Capacity Block are automatically placed close together inside  Amazon EC2 UltraClusters, for low-latency, petabit-scale, non-blocking networking.
You can also use Capacity Blocks to reserve capacity for Amazon EC2 UltraServers. UltraServers connect multiple Amazon EC2 instances within a low-latency, high-bandwidth accelerator

interconnect. You can use UltraServers to handle the most compute and memory intensive AI/ ML workloads in training, fine-tuning, and inference. For more information, see Amazon EC2 UltraServers.
With Capacity Blocks, you can see when GPU instance capacity is available on future dates, and you can schedule a Capacity Block to start at a time that works best for you. When you reserve a Capacity Block, you get predictable capacity assurance for GPU instances while paying only for the amount of time that you need. We recommend Capacity Blocks when you need GPUs to support your ML workloads for days or weeks at a time and don't want to pay for a reservation while your GPU instances aren't in use.
The following are some common use cases for Capacity Blocks.
- ML model training and fine-tuning – Get uninterrupted access to the GPU instances that you reserved to complete ML model training and fine-tuning.
- ML experiments and prototypes – Run experiments and build prototypes that require GPU instances for short durations.
Capacity Blocks are available for select instance types in some AWS Regions. For more information, see Supported instance types and Regions.
You can reserve a Capacity Block with a reservation start time up to eight weeks in the future. Each Capacity Block can have up to 64 instances, and you can have up to 256 instances across Capacity Blocks.
Topics
- Supported instance types and Regions
- Supported platforms
- Considerations
- Related resources
- How Amazon EC2 Capacity Blocks work
- Capacity Blocks pricing and billing
- Find and purchase Capacity Blocks
- Launch instances using Capacity Blocks
- View Capacity Blocks
- Extend Capacity Blocks

- Share Capacity Blocks
- Create a resource group for UltraServer Capacity Blocks
- Monitor Capacity Blocks using EventBridge
- Logging Capacity Blocks API calls with AWS CloudTrail
#### Supported instance types and Regions Instance and UltraServer Capacity Blocks can use be used with the following instance types and AWS regions.
Note Capacity Block sizes of 64 instances are not supported for all instance types in all AWS Regions.
##### Instance Capacity Blocks
- p6-b300.48xlarge
- US West (Oregon) — us-west-2
- p6-b200.48xlarge
- US East (N. Virginia) — us-east-1
- US East (Ohio) — us-east-2
- US West (Oregon) — us-west-2
- p5.4xlarge
- US East (N. Virginia) — us-east-1
- US East (Ohio) — us-east-2
- US West (Oregon) — us-west-2
- Europe (London) — eu-west-2
- Asia Pacific (Mumbai) — ap-south-1
- Asia Pacific (Tokyo) — ap-northeast-1
- Asia Pacific (Sydney) — ap-southeast-2
- South America (São Paulo) — sa-east-1
- p5.48xlarge

- US East (N. Virginia) — us-east-1
- US East (Ohio) — us-east-2
- US West (N. California) — us-west-1
- US West (Oregon) — us-west-2
- Europe (Stockholm) — eu-north-1
- Europe (London) — eu-west-2
- South America (São Paulo) — sa-east-1
- Asia Pacific (Tokyo) — ap-northeast-1
- Asia Pacific (Mumbai) — ap-south-1
- Asia Pacific (Sydney) — ap-southeast-2
- Asia Pacific (Jakarta) — ap-southeast-3
- p5e.48xlarge
- US East (N. Virginia) — us-east-1
- US East (Ohio) — us-east-2
- US West (N. California) — us-west-1
- US West (Oregon) — us-west-2
- Europe (Stockholm) — eu-north-1
- Europe (London) — eu-west-2
- Europe (Spain) — eu-south-2
- South America (São Paulo) — sa-east-1
- Asia Pacific (Tokyo) — ap-northeast-1
- Asia Pacific (Seoul) — ap-northeast-2
- Asia Pacific (Mumbai) — ap-south-1
- Asia Pacific (Jakarta) — ap-southeast-3
- p4d.24xlarge
- US East (N. Virginia) — us-east-1
- US East (Ohio) — us-east-2
- US West (Oregon) — us-west-2
- p4de.24xlarge
- US East (N. Virginia) — us-east-1

- US West (Oregon) — us-west-2
- trn1.32xlarge
- US East (N. Virginia) — us-east-1
- US East (Ohio) — us-east-2
- US West (N. California) — us-west-1
- US West (Oregon) — us-west-2
- Europe (Stockholm) — eu-north-1
- Asia Pacific (Mumbai) — ap-south-1
- Asia Pacific (Sydney) — ap-southeast-2
- Asia Pacific (Melbourne) — ap-southeast-4
- trn2.3xlarge
- Asia Pacific (Melbourne) — ap-southeast-4
- South America (São Paulo) — sa-east-1
- trn2.48xlarge
- US East (Ohio) — us-east-2
##### UltraServer Capacity Blocks
- Trn2
- US East (Ohio) — us-east-2
- P6e-GB200
- Dallas Local Zone (N. Virginia) — us-east-1-dfw-2a Supported platforms Capacity Blocks for ML currently support instances and UltraServers with default tenancy only.
When you use the AWS Management Console to purchase a Capacity Block, the default platform option is Linux/UNIX. When you use the AWS Command Line Interface (AWS CLI) or AWS SDK to purchase a Capacity Block, the following platform options are available:
- Linux/Unix
- Red Hat Enterprise Linux
- RHEL with HA

- SUSE Linux
- Ubuntu Pro Considerations Before you use Capacity Blocks, consider the following details and limitations.
- If we detect impairment impacting an UltraServer Capacity Block, we will notify you but generally will not take action to terminate your instances on the Capacity Block. This is to minimize unintended disruption to your workloads. You can continue using the UltraServer Capacity Block as is after receiving this notification or request remediation by terminating all instances on the capacity block and submitting an AWS support case. After we receive your support case, we will notify you when we have completed remediation and you can relaunch instances onto your UltraServer Capacity Block.
- For P6e-GB200 UltraServer Capacity Blocks, you must terminate your instances at least 60 minutes before the Capacity Block end time.
- To use P6e-GB200 UltraServer Capacity Blocks, you must be opted in to the Dallas Local Zone (N. Virginia) Local Zone.
- Each Capacity Block can have up to 64 instances, and you can have up to 256 instances across Capacity Blocks.
- You can describe Capacity Block offerings that can start in as soon as 30 minutes.
- Capacity Blocks end at 11:30AM Coordinated Universal Time (UTC).
- The termination process for instances running in a Capacity Block begins at 11:00AM Coordinated Universal Time (UTC) on the final day of the reservation.
- Capacity Blocks can be reserved with a start time up to 8 weeks in the future.
- Capacity Block cancellations aren't allowed.
- UltraServer Capacity Blocks can't be shared across AWS accounts or within your AWS Organization.
- Capacity Block can't be moved or split.
- Only UltraServer Capacity Blocks can be used with resource groups. Instance Capacity Blocks can't be used with resource groups. For more information, see Create a resource group for UltraServer Capacity Blocks.
- The total number of instances that can be reserved in Capacity Blocks across all accounts in your AWS Organization can't exceed 256 instances on a particular date.

- To use a Capacity Block, instances must specifically target the reservation ID.
- Instances in a Capacity Block don't count against your On-Demand Instances limits.
- For P5 instances using a custom AMI, ensure that you have the required software and configuration for EFA.
- For Amazon EKS managed node groups, see Create a managed node group with Amazon EC2 Capacity Blocks for ML. For Amazon EKS self-managed node groups, see Use Capacity Blocks for ML with self-managed nodes.
#### Related resources After you create a Capacity Block, you can do the following with the Capacity Block:
- Launch instances into the Capacity Block. For more information, see Launch instances using Capacity Blocks.
- Create an Amazon EC2 Auto Scaling group. For more information, see Use Capacity Blocks for machine learning workloads in the Amazon EC2 Auto Scaling User Guide.
Note If you use Amazon EC2 Auto Scaling or Amazon EKS, you can schedule scaling to run at the start of the Capacity Block reservation. With scheduled scaling, AWS automatically handles retries for you, so you don't need to worry about implementing retry logic to handle transient failures.
- Enhance ML workflows with AWS ParallelCluster. For more information, see Enhancing ML workflows with AWS ParallelCluster and Amazon EC2 Capacity Blocks for ML.
For more information about AWS ParallelCluster, see What is AWS ParallelCluster.
#### How Amazon EC2 Capacity Blocks work You can reserve a Capacity Block with the following specifications:
- Reserve a start time up to 8 weeks in advance
- Set a reservation duration of one to 14 days or a multiple of 7 days, up to 182 days (Examples:
21 days, 28 days)
- Configure up to 64 instances per Capacity Block

- Configure up to 256 instances across multiple Capacity Blocks For Amazon EC2 UltraServers, each UltraServer corresponds to one Capacity Block. You can request multiple UltraServers through a single request.
You can use Capacity Blocks to reserve p6-b200, p5, p5e, p5en, p4d, p4de, trn1, and trn2 instances. You can purchase the following UltraServer types through Capacity Blocks: P6e-GB200 and Trn2 (in preview).
To reserve a Capacity Block, you start by specifying your capacity needs, including the instance type or UltraServer type, the number of instances or UltraServers, amount of time, earliest start date, and latest end date that you need. Then, you can see an available Capacity Block offering that meets your specifications. The Capacity Block offering includes details such as start time, Availability Zone, and reservation price. The price of a Capacity Block offering depends on available supply and demand at the time the offering was delivered. After you reserve a Capacity Block, the price doesn't change. For more information, see Capacity Blocks pricing and billing.
When you purchase a Capacity Block offering, your reservation is created for the date and number of instances that you selected. When your Capacity Block reservation begins, you can target instance launches by specifying the reservation ID in your launch requests.
You can use all the instances you reserved until 30 minutes (for instance types) or 60 minutes (for UltraServer type) before the end time of the Capacity Block. With 30 minutes (for instance types) or 60 minutes (for UltraServer types) left in your Capacity Block reservation, we begin terminating any instances that are running in the Capacity Block. We use this time to clean up your instances before delivering the Capacity Block to the next customer. We emit an event through EventBridge 10 minutes before the termination process begins. For more information, see Monitor Capacity Blocks using EventBridge.
#### Capacity Blocks pricing and billing With Amazon EC2 Capacity Blocks for ML, you pay only for what you reserve. The price of a Capacity Block depends on available supply and demand for Capacity Blocks at the time of purchase. You can view the price of a Capacity Block offering before you reserve it. The price of the Capacity Block is charged up front at the time the reservation is made. When you search for a Capacity Block across a range of dates, we return the lowest-priced Capacity Block offering available. After you've reserved a Capacity Block, the price doesn't change.

When you use a Capacity Block, you pay for the operating system you use when your instances are running. For more information about operating system prices, see Amazon EC2 Capacity Blocks for ML Pricing.
Billing The price of a Capacity Block offering is charged up front. Payment is billed to your AWS account within 5 minutes to 12 hours after you purchase a Capacity Block. While your payment is processing, your Capacity Block reservation resource remains in a state of payment-pending.
If your payment can't be processed at least 5 minutes before your block start time, or within 12 hours (whichever comes first), your Capacity Block is released and the reservation state changes to payment-failed.
After your payment is processed successfully, the Capacity Block resource state changes from payment-pending to scheduled. You receive an invoice that reflects the one-time upfront payment. In the invoice, you can associate the paid amount with the Capacity Block reservation ID.
When your Capacity Block reservation begins, you are billed based only on the operating system you use while your instances are running in the reservation. You can view your usage and associated charges in your anniversary bill for the month of usage in your AWS Cost and Usage Report.
Note Savings Plans and Reserved Instance discounts don't apply to Capacity Blocks.
Viewing your bill You can view your bill in the AWS Billing and Cost Management console. The upfront payment for your Capacity Block appears in the month that you purchased the reservation.
After your reservation begins, your bill shows separate lines for the block reservation used and unused time. You can use these line items to see how much time was used in your reservation. You will see only a usage charge in the line for used time if you use a premium operating system. For more information, see Capacity Blocks pricing and billing. There is no additional charge for unused time.
For more information, see Viewing your bill in the AWS Billing and Cost Management User Guide.

If your Capacity Block starts in a different month then the month you purchased your reservation, the upfront price and reservation usage show up under separate billing months. In your AWS Cost and Usage Report, the Capacity Block reservation ID is listed in the reservation/ReservationARN line item of your upfront fee and the lineitem/ResourceID in your anniversary bill so that you can associate the usage to the corresponding upfront price.
#### Find and purchase Capacity Blocks To reserve a Capacity Block, you first need to find a block of time when capacity is available that matches your needs. To find a Capacity Block that is available to reserve, you specify the following.
- The number of instances that you need
- The duration of time you that you need the instances
- The date range that you need your reservation To search for an available Capacity Block offering, you specify a reservation duration and instance count. You must specify reservation durations in  1-day increments up to 14 days, and in 7-day increments up to 182 days. Each Capacity Block can have up to 64 instances, and you can have up to 256 instances across Capacity Blocks.
When you request a Capacity Block that matches your specifications, we provide the details of up to 3 available blocks. All Capacity Blocks end at 11:30AM UTC, so the blocks starting on the same day will have durations that are the closest match to your desired duration. One block will have a duration that is slightly less than your desired duration, while the other will have a duration slightly greater than your desired duration.
The offering details include the start time of the reservation, the Availability Zone for the reservation, and the price of the reservation. For more information, see Capacity Blocks pricing and billing.
You can purchase the Capacity Block offering you are shown, or you can modify your search criteria to see the other options that are available. There is no predefined expiration time for the offering, but offerings are only available on a first-come, first-served basis.
When you purchase a Capacity Block offering, you get an immediate response confirming that your Capacity Block was reserved. After confirmation, you will see a new Capacity Reservation in your account with a reservation type of capacity-block and a start-date set to the start time of the offering that you purchased. Your Capacity Block reservation is created with a state

of payment-pending. After the upfront payment is successfully processed, the reservation state changes to scheduled. For more information, see Billing.
Note To use P6e-GB200 UltraServer Capacity Blocks, you must be opted in to the Dallas Local Zone (N. Virginia) Local Zone.
Console To find and purchase a Capacity Block
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation bar at the top of the screen, select an AWS Region. This choice is important because Capacity Block sizes of 64 instances are not supported for all instance types in all Regions.
3. In the navigation pane, choose Capacity Reservations, Create Capacity Block.
4. Under Capacity Block types, choose either Instances or  UltraServers.
5. Under Capacity attributes, you can define your Capacity Block search parameters. By default, the platform is Linux. If you want to select a different operating system, use the AWS CLI. For more information, see Supported platforms.
6. Under Total capacity (for Instances) or UltraServer count (for UltraServers), specify the number of instances or UltraServers you want to reserve.
7. Under Duration, enter the number of days or weeks you need the reservation for.
8. Under Date range to search for Capacity Blocks, enter the earliest date that you want your reservation to start.
9. Choose Find Capacity Blocks.
10. If a Capacity Block is available that meets your specifications, you see an offering under Recommended Capacity Blocks. If there are multiple offerings that meet your specifications, the earliest available Capacity Block offering is shown. To view other Capacity Block offerings, adjust your search inputs and choose Find Capacity Blocks again.
11. When you find a Capacity Block offering that you want to purchase, choose Next.
12. (Optional) On the Add tags page, choose Add new tag.

13. The Review and purchase page lists the start and end date, duration, total number of instances, and price.
Note Capacity Blocks can't be canceled after you reserve them.
14. In the popup window Purchase a Capacity Block, type confirm, then choose Purchase.
AWS CLI To find an instance Capacity Block Use the  describe-capacity-block-offerings command.
The following example finds instance Capacity Blocks. aws ec2 describe-capacity-block-offerings \ --instance-type p5.48xlarge \ --instance-count 16 \ --start-date-range 2023-08-14T00:00:00Z \ --end-date-range 2023-10-22-T00:00:00Z \ --capacity-duration-hours 48 The following example finds UltraServer Capacity Blocks. aws ec2 describe-capacity-block-offerings \ --ultraserver-type u-p6e-gb200x72 \ --ultraserver-count 1 \ --start-date-range 2023-08-14T00:00:00Z \ --end-date-range 2023-10-22-T00:00:00Z \ --capacity-duration-hours 48 To purchase a Capacity Block Use the  purchase-capacity-block command with the offering ID of the Capacity Block from the output of the previous example. aws ec2 purchase-capacity-block \ --capacity-block-offering-id cb-0123456789abcdefg \

--instance-platform Linux/UNIX PowerShell To find Capacity Blocks Use the Get-EC2CapacityBlockOffering cmdlet.
The following example finds instance Capacity Blocks.
Get-EC2CapacityBlockOffering `
-InstanceType p5.48xlarge `
-InstanceCount 16 `
-CapacityDurationHour 48 `
-StartDateRange 2023-08-14T00:00:00Z `
-EndDateRange 2023-10-22-T00:00:00Z The following example finds UltraServer Capacity Blocks.
Get-EC2CapacityBlockOffering `
-UltraserverType u-p6e-gb200x72 `
-UltraserverCount   1 `
-CapacityDurationHour 48 `
-StartDateRange 2023-08-14T00:00:00Z `
-EndDateRange 2023-10-22-T00:00:00Z To purchase a Capacity Block Use the New-EC2EC2CapacityBlock cmdlet with the offering ID of the Capacity Block from the output of the previous example.
New-EC2EC2CapacityBlock `
-CapacityBlockOfferingId cb-0123456789abcdefg `
-InstancePlatform Linux/UNIX
#### Launch instances using Capacity Blocks To use your Capacity Block, you must specify the Capacity Block reservation ID when launching instances. Launching an instance into a Capacity Block reduces the available capacity by the

number of instances launched. For example, if your purchased instance capacity is eight instances and you launch four instances, the available capacity is reduced by four.
If you terminate an instance running in the Capacity Block before the reservation ends, you can launch a new instance in its place. When you stop or terminate an instance in a Capacity Block, it takes several minutes to clean up your instance before you can launch another instance to replace it. During this time, your instance will be in a stopping or shutting-down state. After this process is complete, your instance state will change to stopped or terminated. Then, the available capacity in your Capacity Block will update to show another instance available to use.
Requirements
- Your instance can't launch in a subnet in a different Availability Zone from the Availability Zone where your Capacity Block is located.
- Your instance can't launch using an AMI with a different platform than the platform for your Capacity Block.
- To use P6e-GB200 UltraServer Capacity Blocks, you must be opted in to the Dallas Local Zone (N. Virginia) Local Zone.
Console To launch instances into a Capacity Block
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation bar at the top of the screen, select the Region for your Capacity Block reservation.
3. From the Amazon EC2 console dashboard, choose Launch instance.
4. Follow the procedure to launch an instance.
5. Expand Advanced details, and for Purchasing option, choose Capacity Blocks. Then do one of the following:
- To launch the instances into a specific Capacity Block, for Capacity Reservation choose Specify Capacity Reservation, and then select the Capacity Block.
- (UltraServers only) To launch the instances into an UltraServer Capacity Block resource group, for Capacity Reservation choose Specify Capacity Reservation resource group, and then select the resource group.
6. Choose Launch instance.

AWS CLI To launch instances using into a Capacity Block Use the run-instances command with the instance-market-options MarketType option.
The following example launches an instance into a specific Capacity Block. aws ec2 run-instances \ --image-id ami-0abcdef1234567890 \ --count 1 \ --instance-type p5.48xlarge \ --key-name my-key-pair \ --subnet-id subnet-0abcdef1234567890 \ --instance-market-options MarketType='capacity-block' \ --capacity-reservation-specification CapacityReservationTarget={CapacityReservationId=capacity_block_id} The following example launches an instance into an UltraServer Capacity Block resource group. aws ec2 run-instances \ --image-id ami-0abcdef1234567890 \ --count 1 \ --instance-type p6e-gb200.36xlarge \ --key-name my-key-pair \ --subnet-id subnet-0abcdef1234567890 \ --instance-market-options MarketType='capacity-block' \ --capacity-reservation-specification CapacityReservationTarget={CapacityReservationResourceGroupArn=resource_group_arn} PowerShell To launch instances into a Capacity Block Use the New-EC2Instance cmdlet with the -InstanceMarketOption option defined as follows.
$marketoption = New-Object Amazon.EC2.Model.InstanceMarketOptionsRequest $marketoption.MarketType = "capacity-block"
The following example launches an instance into a specific Capacity Block.
New-EC2Instance `

-ImageId ami-0abcdef1234567890 `
-InstanceType p5.48xlarge `
-KeyName "my-key-pair" `
-SubnetId subnet-0abcdef1234567890 `
-InstanceMarketOptions $marketoption `
-CapacityReservationTarget_CapacityReservationId capacity_block_id The following example launches an instance into an UltraServer Capacity Block resource group.
New-EC2Instance `
-ImageId ami-0abcdef1234567890 `
-InstanceType p6e-gb200.36xlarge `
-KeyName "my-key-pair" `
-SubnetId subnet-0abcdef1234567890 `
-InstanceMarketOptions $marketoption `
-CapacityReservationTarget_CapacityReservationResourceGroupArn "resource_group_arn"
Related resources
- To create a launch template targeting a Capacity Block, see the section called "Launch templates".
- To launch instances into a Capacity Block using EC2 Fleet, see Tutorial: Configure your EC2 Fleet to launch instances into Capacity Blocks.
- To set up an EKS managed node group with a Capacity Block, see Create a managed node group with Capacity Blocks for ML in the Amazon EKS User Guide.
- To set up AWS ParallelCluster using a Capacity Block, see ML on AWS ParallelCluster.
#### View Capacity Blocks After you reserve a Capacity Block, you can view the Capacity Block reservation in your AWS account. You can view the start-date and end-date to see when your reservation will begin and end. Before a Capacity Block reservation begins, the available capacity appears as zero. You can see how many instances will be available in your Capacity Block by the tag value for the tag key aws:ec2capacityreservation:incrementalRequestedQuantity.
When a Capacity Block reservation begins, the reservation state changes from scheduled to active. We emit an event through Amazon EventBridge to notify you that the Capacity Block is available to use. For more information, see Monitor Capacity Blocks using EventBridge.

Capacity Blocks have the following states:
- payment-pending – The upfront payment hasn't been processed yet.
- payment-failed—The payment couldn't be processed in the 12 hour time frame. Your Capacity Block was released.
- scheduled – The payment was processed and the Capacity Block reservation hasn't started yet.
- active – The reserved capacity is available for your use.
- expired – The Capacity Block reservation expired automatically at the date and time specified in your reservation request. The reserved capacity is no longer available for your use.
Console To view Capacity Blocks
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Capacity Reservations.
3. On the Capacity Reservations overview page, you see a resource table with details about all of your Capacity Reservation resources. To find your Capacity Blocks reservations, select Capacity Blocks from the dropdown list above Capacity Reservation ID. In the table, you can see information about your Capacity Blocks such as start and end dates, duration, and status.
4. For more details about a Capacity Block, select the reservation ID for the Capacity Block that you want to view. The Capacity Reservation details page displays all the properties of the reservation and the number of instances in use and available in the Capacity Block.
Note Before a Capacity Block reservation begins, the available capacity appears as zero. You can see how many instances will be available when the Capacity Block reservation starts by using the following tag value for the tag key: aws:ec2capacityreservation:incrementalRequestedQuantity.
AWS CLI To view Capacity Blocks

By default, when you use the describe-capacity-reservations command both On-Demand Capacity Reservations and Capacity Block reservations are listed. To view only your Capacity Block reservations, filter for reservations of type capacity-block. aws ec2 describe-capacity-reservations \ --filters Name=reservation-type,Values=capacity-block PowerShell To view Capacity Blocks Use the Get-EC2CapacityReservation cmdlet. By default, both On-Demand Capacity Reservations and Capacity Block reservations are listed. To view only your Capacity Block reservations, filter for reservations of type capacity-block.
Get-EC2CapacityReservation `
    -Filter @{Name="reservation-type"; Values="capacity-block"}
#### Extend Capacity Blocks With Capacity Blocks, you reserve compute capacity for your workloads, ensuring availability and consistency. To accommodate your changing needs, you can extend the duration of your existing Capacity Blocks as required.
To extend a Capacity Block, it must have a status of active or scheduled, and have no extensions that are payment-pending. You can request to extend the duration of your Capacity Block up to a minimum of 1 hour or a maximum of 56 days before it expires. You can extend your Capacity Block by 1-day increments up to 14 days, and 7-day increments up to 182 days (26 weeks) total. When you extend your Capacity Block, its end date will be updated so that your instances can continue to run without disruption.
- There is no limit to the number of extensions you can apply to a Capacity Block
- Your Capacity Reservation ID will remain the same after extending the block
- Capacity Blocks can only be extended if there is sufficient capacity available to support them, which is not guaranteed.

Billing The price of a Capacity Block offering is charged up front. The extension will remain in payment- pending until the bill is paid. If your payment can't be processed within 12 hours, or up to 35 minutes before the Capacity Block is scheduled to end (whichever comes first), your extension is not successful and the status changes to payment-failed. Your Capacity Block reservation will remain active and will be terminated on the original end date.
After your payment is processed successfully, the Capacity Block extension status changes to payment-succeeded and the end date of the Capacity Block reservation will be updated to the new end date. The details of your extension can be viewed in the Capacity Block Extension details section of the console, or by using the describe-capacity-block-extension-history command.
##### Extend your Capacity Block Console To extend a Capacity Block
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Capacity Reservations.
3. On the Capacity Reservations overview page, you see a resource table with details about all of your Capacity Reservations resources. Select the reservation ID for the Capacity Block that you want to extend.
4. From the Actions drop down menu, choose Extend Capacity Block.
5. Under Duration, enter the number of days or weeks you need to extend the reservation for.
6. Choose Find Capacity Block.
7. If a Capacity Block is available that meets your specifications, an offering appears under Recommended Capacity Blocks. To view other Capacity Block offerings, adjust your search inputs and choose Find Capacity Blocks again.
8. When you find a Capacity Block offering that you want to purchase, choose Extend.
9. In the pop-up window Extend Capacity Block, enter confirm, then choose Extend.
AWS CLI To find a Capacity Block extension

Use the describe-capacity-block-extension-offerings command. The following example searches for a 48 hour Capacity Block extension for the specified Reservation. aws ec2 describe-capacity-block-extension-offerings \ --capacity-reservation-id cr-1234567890abcdefg \ --capacity-block-extension-duration-hours 48 To extend a Capacity Block Use the purchase-capacity-block-extension command. Specify the extension offering ID from the output of the previous example. aws ec2 purchase-capacity-block-extension \ --capacity-block-extension-offering-id cbe-0123456789abcdefg \ --capacity-reservation-id cr-1234567890abcdefg PowerShell To find a Capacity Block extension Use the Get-EC2CapacityBlockExtensionOffering cmdlet. The following example searches for a 48 hour Capacity Block extension for the specified Reservation.
Get-EC2CapacityBlockExtensionOffering `
    -CapacityReservationId cr-1234567890abcdefg `
    -CapacityBlockExtensionDurationHour 48 To extend a Capacity Block Use the Invoke-EC2CapacityBlockExtension cmdlet. Specify the extension offering ID from the output of the previous example.
Invoke-EC2CapacityBlockExtension `
    -CapacityBlockExtensionOfferingId cbe-0123456789abcdefg `
    -CapacityReservationId cr-1234567890abcdefg
#### Share Capacity Blocks Capacity Block sharing enables Capacity Block owners to share Amazon EC2 Capacity Blocks with other AWS accounts within an AWS Organization. This allows you to maximize utilization of reserved GPU capacity across different teams and projects to efficiently use the Capacity Blocks.

The AWS account that owns the Capacity Block (owner) can share it with other AWS accounts (consumers). An owner can share a Capacity Block with specific AWS accounts inside their AWS Organization, an organizational unit inside their AWS Organization, or the entire AWS Organization. Consumers can launch instances into Capacity Blocks that are shared with them in the same way that they launch instances into Capacity Blocks they own.
##### Prerequisites for sharing Capacity Blocks Before you can share a Capacity Block, the following conditions must be met:
- You must own the Capacity Block - You cannot share a Capacity Block that has been shared with you.
- The Capacity Block state must be active or scheduled - Capacity Blocks that are in other states, such as expired or payment-pending cannot be shared.
- Sharing within your AWS Organization only - An owner can share a Capacity Block with specific AWS accounts inside their AWS Organization, an organizational unit inside their AWS Organization, or the entire AWS Organization.
- UltraServer Capacity Blocks not supported - You cannot share Capacity Blocks for Amazon EC2 UltraServers.
- Account eligibility - Capacity Block sharing is not available to new AWS accounts or AWS accounts that have a limited billing history.
##### Related services Capacity Block sharing integrates with AWS Resource Access Manager (AWS RAM). AWS RAM is a service that enables you to share your AWS resources with any AWS account or through AWS Organizations. With AWS RAM, you share resources that you own by creating a resource share.
A resource share specifies the resources to share, and the consumers with whom to share them.
Consumers can be individual AWS accounts, or organizational units or an entire organization from AWS Organizations.
For more information about AWS RAM, see the AWS RAM User Guide.

##### Shared Capacity Block permissions
###### Permissions for owners The Capacity Block owner remains responsible for managing the Capacity Block (e.g. extending, sharing), and the instances they launch into it. Owners cannot modify instances that consumers launch into Capacity Blocks they have shared.
###### Permissions for consumers Consumers can launch instances into the shared capacity and are responsible for managing those instances. Consumers cannot view or modify instances owned by other consumers or by the Capacity Block owner. Consumers can also only view the total capacity and available capacity in the shared Capacity Block.
##### Share a Capacity Block To share a Capacity Block, you must add it to a resource share. A resource share is an AWS RAM resource that lets you share your resources across AWS accounts.
If you added your Capacity Block to a resource share that is shared with the entire AWS Organization, consumers in your organization are granted access to the shared Capacity Block.
Console To share a Capacity Block that you own using the Amazon EC2 console
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Capacity Reservations.
3. Select the Capacity Block to share and choose Actions, Share reservation.
4. Select the resource share to which to add the Capacity Block and choose Share Capacity Reservation.
It could take a few minutes for consumers to get access to the shared Capacity Block.
To add a Capacity Block to a new resource share You must first create the resource share using the AWS RAM console. For more information, see Creating a resource share in the AWS RAM User Guide.

AWS CLI To share a Capacity Block that you own Use the create-resource-share and associate-resource-share commands. aws ram create-resource-share \ --name my-resource-share \ --resource-arns arn:aws:ec2:us-east-2:123456789012:capacity- reservation/cr-1234abcd56EXAMPLE aws ram associate-resource-share \ --resource-share-arn arn:aws:ram:us-east-2:123456789012:resource-share/7ab63972- b505-7e2a-420d-6f5d3EXAMPLE \ --resource-arns arn:aws:ec2:us-east-2:123456789012:capacity- reservation/cr-1234abcd56EXAMPLE PowerShell To share a Capacity Block that you own Use the New-RAMResourceShare and Connect-RAMResourceShare cmdlets.
New-RAMResourceShare `
    -Name my-resource-share `
    -ResourceArn "arn:aws:ec2:us-east-2:123456789012:capacity- reservation/cr-1234abcd56EXAMPLE"
Connect-RAMResourceShare `
    -ResourceShareArn "arn:aws:ram:us-east-2:123456789012:resource-share/7ab63972- b505-7e2a-420d-6f5d3EXAMPLE" `
    -ResourceArn "arn:aws:ec2:us-east-2:123456789012:capacity- reservation/cr-1234abcd56EXAMPLE"
Capacity Blocks operate on a first-come, first-served basis for all accounts, regardless of ownership status. When you share a Capacity Block, if a consumer launches instances before the owner, those instances occupy the capacity until the consumer terminates the instances or until 30 minutes before the Capacity Block expires.

##### Stop sharing a Capacity Block You can stop sharing a Capacity Block at any time until 30 minutes before the block expiry date.
What happens when you stop sharing:
- Consumers can no longer launch new instances into the Capacity Block that was unshared.
- Any running instances continue running until 30 minutes before the Capacity Block expiry date, unless terminated by the consumer.
Console To stop sharing a Capacity Block that you own using the Amazon EC2 console
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Capacity Reservations.
3. Select the Capacity Block and choose the Sharing tab.
4. The Sharing tab lists the resource shares to which the Capacity Block has been added.
Select the resource share from which to remove the Capacity Block.
5. Choose Remove from resource share.
AWS CLI To stop sharing a Capacity Block that you own Use the disassociate-resource-share command. aws ram disassociate-resource-share \ --resource-share-arn arn:aws:ram:us-east-2:123456789012:resource-share/7ab63972- b505-7e2a-420d-6f5d3EXAMPLE \ --resource-arns arn:aws:ec2:us-east-2:123456789012:capacity- reservation/cr-1234abcd56EXAMPLE PowerShell To stop sharing a Capacity Block that you own Use the Disconnect-RAMResourceShare cmdlet.
Disconnect-RAMResourceShare `

    -ResourceShareArn "arn:aws:ram:us-east-2:123456789012:resource-share/7ab63972- b505-7e2a-420d-6f5d3EXAMPLE" `
    -ResourceArn "arn:aws:ec2:us-east-2:123456789012:capacity- reservation/cr-1234abcd56EXAMPLE"
##### Monitor shared Capacity Block usage Capacity Block owners can monitor which accounts are using their shared Capacity Blocks and track instance usage per account.
AWS CLI To monitor usage of a Capacity Block Use the get-capacity-reservation-usage command. aws ec2 get-capacity-reservation-usage \ --capacity-reservation-id cr-1234abcd56EXAMPLE This API enables owners to:
- View which accounts are currently using the Capacity Block.
- See the number of instances each account is running.
##### Instance termination notices Owner and consumer accounts that have instances running in the Capacity Block will receive an EventBridge event 40 minutes before the Capacity Block reservation ends, indicating that any instances running in the reservation will begin to terminate in 10 minutes. For more information, see Monitor Capacity Blocks using EventBridge.
##### Capacity Block extensions Capacity Blocks can be extended while they are shared. Only the owner account can extend a shared Capacity Block.
When a Capacity Block is extended, running instances launched by the owner or consumers automatically inherit the new expiry date, and consumers can continue using the shared capacity until the new expiry date without any instance interruption.

##### Pricing and billing Owners are billed for the Capacity Blocks they share and pay upfront for the Capacity Block when they purchase it. Owners also pay for operating system charges for instances they run on the Capacity Block.
Consumers are billed only for the operating system charges for instances they run in the shared Capacity Block. Consumers are not charged for the Capacity Block reservation itself.
#### Create a resource group for UltraServer Capacity Blocks You can use AWS Resource Groups to create logical collections of UltraServer Capacity Blocks.
After you create the resource group, you can add UltraServer Capacity Blocks that you own in your account. After you add the UltraServer Capacity Blocks, you can target instances launches to the resource group instead of the individual Capacity Blocks. Instances that target a resource group match with any UltraServer Capacity Blocks in the group that has matching attributes and available capacity. If the resource group does not have an UltraServer Capacity Block with matching attributes and available capacity, the instance launch fails.
If an UltraServer Capacity Block is removed from a resource group while it has running instances, those instances continue to run in the Capacity Block. If an UltraServer Capacity Block in a group ends while it has running instances, the instances are terminated.
You can't add instance Capacity Blocks to a resource group.
To create a resource group for UltraServer Capacity Blocks, use one of the following methods.
AWS CLI To create a resource group for UltraServer Capacity Blocks Use the create-group AWS CLI command, and for --configuration, specify the following:
{ "Configuration": [ { "Type": "AWS::EC2::CapacityReservationPool", "Parameters": [ { "Name": "instance-type", "Values": [ "instance_type"
          ]

        }, { "Name": "reservation-type", "Values": [ "capacity-block"
          ]
        } ]
    }, { "Type": "AWS::ResourceGroups::Generic", "Parameters": [ { "Name": "allowed-resource-types", "Values": [ "AWS::EC2::CapacityReservation"
          ]
        } ]
    } ]
} PowerShell To create a resource group for UltraServer Capacity Blocks Use the New-RGGroup cmdlet. For -Configuration, specify the following:
{ "Configuration": [ { "Type": "AWS::EC2::CapacityReservationPool", "Parameters": [ { "Name": "instance-type", "Values": [ "instance_type"
          ]
        }, { "Name": "reservation-type", "Values": [ "capacity-block"

          ]
        } ]
    }, { "Type": "AWS::ResourceGroups::Generic", "Parameters": [ { "Name": "allowed-resource-types", "Values": [ "AWS::EC2::CapacityReservation"
          ]
        } ]
    } ]
} After you create a resource group for UltraServer Capacity Block, use one of the following methods to add existing UltraServer Capacity Blocks to it.
AWS CLI To add an UltraServer Capacity Block to a resource group Use the  group-resources command. For --group specify the name of the resource group you created. For --resource-arns, specify the ARNs of the UltraServer Capacity Blocks to add. aws resource-groups group-resources \ --group MyCRGroup \ --resource-arns CapacityReservationArn PowerShell To add an UltraServer Capacity Block to a resource group Use the Add-RGResource cmdlet. For -Group specify the name of the resource group you created. For -ResourceArn , specify the ARNs of the UltraServer Capacity Blocks to add.
The following example adds two Capacity Reservations to the specified group.
Add-RGResource `

-Group MyCRGroup `
-ResourceArn CapacityReservationArn
#### Monitor Capacity Blocks using EventBridge When your Capacity Block reservation starts, Amazon EC2 will emit an event through EventBridge that indicates your capacity is ready to use. Forty minutes before your Capacity Block reservation ends, you receive another EventBridge event that tells you that any instances running in the reservation will begin to terminate in 10 minutes. For more information about EventBridge events, see Amazon EventBridge Events.
The following event structures for events emitted for Capacity Blocks:
Capacity Block Delivered The following example shows an event for Capacity Block Delivered.
{ "customer_event_id": "[Capacity Reservation Id]-delivered", "detail_type": "Capacity Block Reservation Delivered", "source": "aws.ec2", "account": "[Customer Account ID]", "time": "[Current time]", "resources": [ "[ODCR ARN]"
  ], "detail": { "capacity-reservation-id": "[ODCR ID]", "end-date": "[ODCR End Date]"
  } } Capacity Block Expiration Warning The following example shows an event for Capacity Block Expiration Warning.
{ "customer_event_id": "[Capacity Reservation Id]-approaching-expiry", "detail_type": "Capacity Block Reservation Expiration Warning", "source": "aws.ec2", "account": "[Customer Account ID]",

  "time": "[Current time]", "resources": [ "[ODCR ARN]"
  ], "detail": { "capacity-reservation-id": "[ODCR ID]", "end-date": "[ODCR End Date]"
  } } Capacity Reservation Instance Interruption Warning The following example shows an event for EC2 Capacity Reservation Instance Interruption Warning.
{ "version": "0", "id": "12345678-1234-1234-1234-123456789012", "detail_type": "EC2 Capacity Reservation Instance Interruption Warning", "source": "aws.ec2", "account": "[Customer Account ID]", "time": "[Current time]", "region": "[Region]", "resources": [ "[Instance ARN]"
    ], "detail": { "instance-id": "[Instance ID]", "instance-action": "terminate", "instance-termination-time": "[Current time]", "availability-zone-id": "[Availability Zone ID]", "instance-lifecycle": "capacity-block"
    } }
#### Logging Capacity Blocks API calls with AWS CloudTrail Capacity Blocks is integrated with AWS CloudTrail, a service that provides a record of actions taken by a user, role, or an AWS service in Capacity Blocks. CloudTrail captures API calls for Capacity Blocks as events. The calls captured include calls from the Capacity Blocks console and code calls to the Capacity Blocks API operations. If you create a trail, you can enable continuous delivery of CloudTrail events to an Amazon S3 bucket, including events for Capacity Blocks. If you don't

configure a trail, you can still view the most recent events in the CloudTrail console in Event history. Using the information collected by CloudTrail, you can determine the request that was made to Capacity Blocks, the IP address from which the request was made, who made the request, when it was made, and additional details.
To learn more about CloudTrail, see the AWS CloudTrail User Guide.
##### Capacity Blocks information in CloudTrail CloudTrail is enabled on your AWS account when you create the account. When activity occurs in Capacity Blocks, that activity is recorded in a CloudTrail event along with other AWS service events in Event history. You can view, search, and download recent events in your AWS account. For more information, see Viewing events with CloudTrail Event history.
For an ongoing record of events in your AWS account, including events for Capacity Blocks, create a trail. A trail enables CloudTrail to deliver log files to an Amazon S3 bucket. By default, when you create a trail in the console, the trail applies to all AWS Regions. The trail logs events from all Regions in the AWS partition and delivers the log files to the Amazon S3 bucket that you specify.
Additionally, you can configure other AWS services to further analyze and act upon the event data collected in CloudTrail logs. For more information, see the following:
- Overview for creating a trail
- CloudTrail supported services and integrations
- Configuring Amazon SNS notifications for CloudTrail
- Receiving CloudTrail log files from multiple regions and Receiving CloudTrail log files from multiple accounts All Capacity Blocks actions are logged by CloudTrail and are documented in the Amazon EC2 API Reference. For example, calls to the CapacityBlockScheduled, and CapacityBlockActive actions generate entries in the CloudTrail log files.
Every event or log entry contains information about who generated the request. The identity information helps you determine the following:
- Whether the request was made with root or AWS Identity and Access Management (IAM) user credentials.
- Whether the request was made with temporary security credentials for a role or federated user.
- Whether the request was made by another AWS service.

For more information, see the CloudTrail userIdentity element.
##### Understanding Capacity Blocks log file entries A trail is a configuration that enables delivery of events as log files to an Amazon S3 bucket that you specify. CloudTrail log files contain one or more log entries. An event represents a single request from any source and includes information about the requested action, the date and time of the action, request parameters, and so on. CloudTrail log files aren't an ordered stack trace of the public API calls, so they don't appear in any specific order.
The following examples show CloudTrail log entries for:
- TerminateCapacityBlocksInstances
- CapacityBlockPaymentFailed
- CapacityBlockScheduled
- CapacityBlockActive
- CapacityBlockFailed
- CapacityBlockExpired Note Some fields have been redacted from the examples for data privacy.
###### TerminateCapacityBlocksInstances { "eventVersion": "1.05", "userIdentity": { "accountId": "123456789012", "invokedBy": "AWS Internal;"
  }, "eventTime": "2023-10-02T00:06:08Z", "eventSource": "ec2.amazonaws.com", "eventName": "TerminateCapacityBlockInstances", "awsRegion": "us-east-1", "sourceIPAddress": "203.0.113.25", "userAgent": "aws-cli/1.15.61 Python/2.7.10 Darwin/16.7.0 botocore/1.10.60", "requestParameters": null,

  "responseElements": null, "eventID": "a1b2c3d4-EXAMPLE", "readOnly": false, "resources": [ { "accountId": "123456789012", "type": "AWS::EC2::Instance", "ARN": "arn:aws:ec2:us-east-1:123456789012:instance/i-1234567890abcdef0"
    } { "accountId": "123456789012", "type": "AWS::EC2::Instance", "ARN": "arn:aws:ec2:us-east-1:123456789012:instance/i-0598c7d356eba48d7"
    } ], "eventType": "AwsServiceEvent", "recipientAccountId": "123456789012", "serviceEventDetails": { "capacityReservationId": "cr-12345678", } }
###### CapacityBlockPaymentFailed { "eventVersion": "1.05", "userIdentity": { "accountId": "123456789012", "invokedBy": "AWS Internal;"
  }, "eventTime": "2023-10-02T00:06:08Z", "eventSource": "ec2.amazonaws.com", "eventName": "CapacityBlockPaymentFailed", "awsRegion": "us-east-1", "sourceIPAddress": "203.0.113.25", "userAgent": "aws-cli/1.15.61 Python/2.7.10 Darwin/16.7.0 botocore/1.10.60", "requestParameters": null, "responseElements": null, "eventID": "a1b2c3d4-EXAMPLE", "readOnly": false, "resources": [ { "ARN": "arn:aws:ec2:us-east-1:123456789012:capacity-reservation/cr-12345678",

      "accountId": "123456789012", "type": "AWS::EC2::CapacityReservation"
    } ], "eventType": "AwsServiceEvent", "recipientAccountId": "123456789012", "serviceEventDetails": { "capacityReservationId": "cr-12345678", "capacityReservationState": "payment-failed"
      } }
###### CapacityBlockScheduled { "eventVersion": "1.05", "userIdentity": { "accountId": "123456789012", "invokedBy": "AWS Internal;"
  }, "eventTime": "2023-10-02T00:06:08Z", "eventSource": "ec2.amazonaws.com", "eventName": "CapacityBlockScheduled", "awsRegion": "us-east-1", "sourceIPAddress": "203.0.113.25", "userAgent": "aws-cli/1.15.61 Python/2.7.10 Darwin/16.7.0 botocore/1.10.60", "requestParameters": null, "responseElements": null, "eventID": "a1b2c3d4-EXAMPLE", "readOnly": false, "resources": [ { "ARN": "arn:aws:ec2:us-east-1:123456789012:capacity-reservation/cr-12345678", "accountId": "123456789012", "type": "AWS::EC2::CapacityReservation"
    } ], "eventType": "AwsServiceEvent", "recipientAccountId": "123456789012", "serviceEventDetails": { "capacityReservationId": "cr-12345678", "capacityReservationState": "scheduled"
      }

}
###### CapacityBlockActive { "eventVersion": "1.05", "userIdentity": { "accountId": "123456789012", "invokedBy": "AWS Internal;"
  }, "eventTime": "2023-10-02T00:06:08Z", "eventSource": "ec2.amazonaws.com", "eventName": "CapacityBlockActive", "awsRegion": "us-east-1", "sourceIPAddress": "203.0.113.25", "userAgent": "aws-cli/1.15.61 Python/2.7.10 Darwin/16.7.0 botocore/1.10.60", "requestParameters": null, "responseElements": null, "eventID": "a1b2c3d4-EXAMPLE", "readOnly": false, "resources": [ { "ARN": "arn:aws:ec2:us-east-1:123456789012:capacity-reservation/cr-12345678", "accountId": "123456789012", "type": "AWS::EC2::CapacityReservation"
    } ], "eventType": "AwsServiceEvent", "recipientAccountId": "123456789012", "serviceEventDetails": { "capacityReservationId": "cr-12345678", "capacityReservationState": "active"
      } }
###### CapacityBlockFailed { "eventVersion": "1.05", "userIdentity": { "accountId": "123456789012", "invokedBy": "AWS Internal;"
  },

  "eventTime": "2023-10-02T00:06:08Z", "eventSource": "ec2.amazonaws.com", "eventName": "CapacityBlockFailed", "awsRegion": "us-east-1", "sourceIPAddress": "203.0.113.25", "userAgent": "aws-cli/1.15.61 Python/2.7.10 Darwin/16.7.0 botocore/1.10.60", "requestParameters": null, "responseElements": null, "eventID": "a1b2c3d4-EXAMPLE", "readOnly": false, "resources": [ { "ARN": "arn:aws:ec2:us-east-1:123456789012:capacity-reservation/cr-12345678", "accountId": "123456789012", "type": "AWS::EC2::CapacityReservation"
    } ], "eventType": "AwsServiceEvent", "recipientAccountId": "123456789012", "serviceEventDetails": { "capacityReservationId": "cr-12345678", "capacityReservationState": "failed"
      } }
###### CapacityBlockExpired { "eventVersion": "1.05", "userIdentity": { "accountId": "123456789012", "invokedBy": "AWS Internal;"
  }, "eventTime": "2023-10-02T00:06:08Z", "eventSource": "ec2.amazonaws.com", "eventName": "CapacityBlockExpired", "awsRegion": "us-east-1", "sourceIPAddress": "203.0.113.25", "userAgent": "aws-cli/1.15.61 Python/2.7.10 Darwin/16.7.0 botocore/1.10.60", "requestParameters": null, "responseElements": null, "eventID": "a1b2c3d4-EXAMPLE", "readOnly": false,
