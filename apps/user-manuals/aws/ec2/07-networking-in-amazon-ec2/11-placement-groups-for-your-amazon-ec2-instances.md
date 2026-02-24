# Placement groups for your Amazon EC2 instances

Source: apps/user-manuals/aws/ec2-ug.pdf

---

    --filters Name=instance-type,Values=p5en.48xlarge The following is example output.
{ "CapacityReservations": [ { "CapacityReservationId": "cr-2222222222example", "CapacityBlockId": "null", "State": "active", "InstanceType": "p5en.48xlarge", "NetworkNodes": [ "nn-1111111111example", "nn-2222222222example"
            ], "AvailabilityZone": "us-east-1a"
        } ], "NextToken": "SomeEncryptedToken"
} PowerShell To describe the topology of Capacity Reservations with a specific instance type Use the Get-EC2CapacityReservationTopology cmdlet.
Get-EC2CapacityReservationTopology `
    -Filter @{Name="instance-type"; Values="p5en.48xlarge"}
# Placement groups for your Amazon EC2 instances To meet the needs of your workload, you can launch a group of interdependent EC2 instances into a placement group to influence their placement.
Depending on the type of workload, you can create a placement group using one of the following placement strategies:
- Cluster – Packs instances close together inside an Availability Zone. This strategy enables workloads to achieve the low-latency network performance necessary for tightly-coupled node- to-node communication that is typical of high-performance computing (HPC) applications.

- Partition – Spreads your instances across logical partitions such that groups of instances in one partition do not share the underlying hardware with groups of instances in different partitions.
This strategy is typically used by large distributed and replicated workloads, such as Hadoop, Cassandra, and Kafka.
- Spread – Strictly places a small group of instances across distinct underlying hardware to reduce correlated failures.
Placement groups are optional. If you don't launch your instances into a placement group, EC2 tries to place the instances in such a way that all of your instances are spread out across the underlying hardware to minimize correlated failures.
Pricing There is no charge for creating a placement group.
### Rules and limitations Before you use placement groups, be aware of the following rules:
- An instance can be placed in one placement group at a time; you can't place an instance in multiple placement groups.
- You can't merge placement groups.
- On-Demand Capacity Reservations and zonal Reserved Instances allow you to reserve capacity for EC2 instances in Availability Zones. When you launch an instance, if the instance attributes match those specified by an On-Demand Capacity Reservation or a zonal Reserved Instance, then the reserved capacity is automatically used by the instance. This is also true if you launch the instance into a placement group.
- You can't launch Dedicated Hosts in placement groups.
- You can't launch a Spot Instance that is configured to stop or hibernate on interruption in a placement group.
Contents
- Placement strategies for your placement groups
- Create a placement group for your EC2 instances
- Change the placement for an EC2 instance
- Delete a placement group

- Shared placement groups
- Placement groups on AWS Outposts
## Placement strategies for your placement groups You can create a placement group for your EC2 instances using one of the following placement strategies.
Placement strategies
- Cluster placement groups
- Partition placement groups
- Spread placement groups
### Cluster placement groups A cluster placement group is a logical grouping of instances within a single Availability Zone.
Instances are not isolated to a single rack. A cluster placement group can span peered virtual private networks (VPCs) in the same Region. Instances in the same cluster placement group enjoy a higher per-flow throughput limit for TCP/IP traffic and are placed in the same high-bisection bandwidth segment of the network.
The following image shows instances that are placed into a cluster placement group.
Cluster placement groups are recommended for applications that benefit from low network latency, high network throughput, or both. They are also recommended when the majority of the network traffic is between the instances in the group. To provide the lowest latency and the

highest packet-per-second network performance for your placement group, choose an instance type that supports enhanced networking. For more information, see Enhanced Networking.
We recommend that you launch your instances in the following way:
- Use a single launch request to launch the number of instances that you need in the placement group.
- Use the same instance type for all instances in the placement group.
If you try to add more instances to the placement group later, or if you try to launch more than one instance type in the placement group, you increase your chances of getting an insufficient capacity error.
If you stop an instance in a placement group and then start it again, it still runs in the placement group. However, the start fails if there isn't enough capacity for the instance.
If you receive a capacity error when launching an instance in a placement group that already has running instances, stop and start all of the instances in the placement group, and try the launch again. Starting the instances may migrate them to hardware that has capacity for all of the requested instances.
Rules and limitations The following rules apply to cluster placement groups:
- The following instance types are supported:
- Current generation instances, except for burstable performance instances (for example, T2), Mac1 instances, and M7i-flex instances.
- The following previous generation instances: A1, C3, C4, I2, M4, R3, and R4.
- A cluster placement group can't span multiple Availability Zones.
- The maximum network throughput speed of traffic between two instances in a cluster placement group is limited by the slower of the two instances. For applications with high-throughput requirements, choose an instance type with network connectivity that meets your requirements.
- For instances that are enabled for enhanced networking, the following rules apply:
- Instances within a cluster placement group can use up to 10 Gbps for single-flow traffic.
Instances that are not within a cluster placement group can use up to 5 Gbps for single-flow traffic.

- Traffic to and from Amazon S3 buckets within the same Region over the public IP address space or through a VPC endpoint can use all available instance aggregate bandwidth.
- You can launch multiple instance types into a cluster placement group. However, this reduces the likelihood that the required capacity will be available for your launch to succeed. We recommend using the same instance type for all instances in a cluster placement group.
- We recommend that you reserve capacity explicitly in the cluster placement group by creating an On-Demand Capacity Reservation in the cluster placement group. Note that you can't reserve capacity using zonal Reserved Instances, as they can't reserve capacity explicitly in a placement group.
- Network traffic to the internet and over an Direct Connect connection to on-premises resources is limited to 5 Gbps for cluster placement groups.
### Partition placement groups Partition placement groups help reduce the likelihood of correlated hardware failures for your application. When using partition placement groups, Amazon EC2 divides each group into logical segments called partitions. Amazon EC2 ensures that each partition within a placement group has its own set of racks. Each rack has its own network and power source. No two partitions within a placement group share the same racks, allowing you to isolate the impact of hardware failure within your application.
The following image is a simple visual representation of a partition placement group in a single Availability Zone. It shows instances that are placed into a partition placement group with three partitions—Partition 1, Partition 2, and Partition 3. Each partition comprises multiple instances.
The instances in a partition do not share racks with the instances in the other partitions, allowing you to contain the impact of a single hardware failure to only the associated partition.

Partition placement groups can be used to deploy large distributed and replicated workloads, such as HDFS, HBase, and Cassandra, across distinct racks. When you launch instances into a partition placement group, Amazon EC2 tries to distribute the instances evenly across the number of partitions that you specify. You can also launch instances into a specific partition to have more control over where the instances are placed.
A partition placement group can have partitions in multiple Availability Zones in the same Region.
A partition placement group can have a maximum of seven partitions per Availability Zone. The number of instances that can be launched into a partition placement group is limited only by the limits of your account.
In addition, partition placement groups offer visibility into the partitions — you can see which instances are in which partitions. You can share this information with topology-aware applications, such as HDFS, HBase, and Cassandra. These applications use this information to make intelligent data replication decisions for increasing data availability and durability.
If you start or launch an instance in a partition placement group and there is insufficient unique hardware to fulfill the request, the request fails. Amazon EC2 makes more distinct hardware available over time, so you can try your request again later.
Rules and limitations The following rules apply to partition placement groups:
- A partition placement group supports a maximum of seven partitions per Availability Zone. The number of instances that you can launch in a partition placement group is limited only by your account limits.
- When instances are launched into a partition placement group, Amazon EC2 tries to evenly distribute the instances across all partitions. Amazon EC2 doesn't guarantee an even distribution of instances across all partitions.
- A partition placement group with Dedicated Instances can have a maximum of two partitions.
- Capacity Reservations do not reserve capacity in a partition placement group.
### Spread placement groups A spread placement group is a group of instances that are each placed on distinct hardware.
Spread placement groups are recommended for applications that have a small number of critical instances that should be kept separate from each other. Launching instances in a spread level

placement group reduces the risk of simultaneous failures that might occur when instances share the same equipment. Spread level placement groups provide access to distinct hardware, and are therefore suitable for mixing instance types or launching instances over time.
If you start or launch an instance in a spread placement group and there is insufficient unique hardware to fulfill the request, the request fails. Amazon EC2 makes more distinct hardware available over time, so you can try your request again later. Placement groups can spread instances across racks or hosts. Rack level spread placement groups can be used in AWS Regions and on AWS Outposts. Host level spread placement groups can be used with AWS Outposts only.
Rack level spread placement groups The following image shows seven instances in a single Availability Zone that are placed into a spread placement group. The seven instances are placed on seven different racks, each rack has its own network and power source.
A rack level spread placement group can span multiple Availability Zones in the same Region. In a Region, a rack level spread placement group can have a maximum of seven running instances per Availability Zone per group. With Outposts, a rack level spread placement group can hold as many instances as you have racks in your Outpost deployment.
Host level spread placement groups Host level spread placement groups are only available with AWS Outposts. A host spread level placement group can hold as many instances as you have hosts in your Outpost deployment. For more information, see the section called "Placement groups on AWS Outposts".
Rules and limitations The following rules apply to spread placement groups:

- A rack spread placement group supports a maximum of seven running instances per Availability Zone. For example, in a Region with three Availability Zones, you can run a total of 21 instances in the group, with seven instances in each Availability Zone. If you try to start an eighth instance in the same Availability Zone and in the same spread placement group, the instance will not launch. If you need more than seven instances in an Availability Zone, we recommend that you use multiple spread placement groups. Using multiple spread placement groups does not provide guarantees about the spread of instances between groups, but it does help ensure the spread for each group, thus limiting the impact from certain classes of failures.
- Spread placement groups are not supported for Dedicated Instances.
- Host level spread placement groups are only supported for placement groups on AWS Outposts.
A host level spread placement group can hold as many instances as you have hosts in your Outpost deployment.
- In a Region, a rack level spread placement group can have a maximum of seven running instances per Availability Zone per group. With AWS Outposts, a rack level spread placement group can hold as many instances as you have racks in your Outpost deployment.
- Capacity Reservations do not reserve capacity in a spread placement group.
## Create a placement group for your EC2 instances You can use a placement group to control the placement of instances relative to each other. After you create a placement group, you can launch instances in the placement group.
Limitation You can create a maximum of 500 placement groups per Region.
Console To create a placement group
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Placement Groups.
3. Choose Create placement group.
4. Specify a name for the group.
5. Choose the placement strategy for the group: Cluster, Spread, or Partition.
If you chose Spread, you must choose the spread level: Rack or Host.

If you chose Partition, you must enter the number of partitions for the group.
6. (Optional) To add a tag, choose Add new tag, and then enter a key and value.
7. Choose Create group.
AWS CLI Use the create-placement-group command.
To create a cluster placement group The following example creates a placement group that uses the cluster placement strategy, and it applies a tag with a key of purpose and a value of production. aws ec2 create-placement-group \ --group-name my-cluster \ --strategy cluster \ --tag-specifications 'ResourceType=placement- group,Tags={Key=purpose,Value=production}'
To create a partition placement group The following example creates a placement group that uses the partition placement strategy, and specifies the five partitions using the --partition-count parameter. aws ec2 create-placement-group \ --group-name HDFS-Group-A \ --strategy partition \ --partition-count 5 PowerShell Use the New-EC2PlacementGroup cmdlet.
To create a cluster placement group The following example creates a cluster placement group.
New-EC2PlacementGroup `
    -GroupName my-placement-group `

    -Strategy cluster To create a partition placement group The following example creates a partition placement group.
New-EC2PlacementGroup `
    -GroupName my-placement-group `
    -Strategy partition `
    -PartitionCount 5
## Change the placement for an EC2 instance You can change the placement group for an instance as follows:
- Add an instance to a placement group
- Move an instance from one placement group to another
- Remove an instance from a placement group Requirement Before you can change the placement group for an instance, the instance must be in the stopped state.
Console To change the instance placement
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Instances.
3. Select the instance.
4. Choose Actions, Instance settings, Modify instance placement.
5. For Placement group, do one of the following:
- To add the instance to a placement group, choose the placement group.
- To move the instance from one placement group to another, choose the placement group.

- To remove the instance from the placement group, choose None.
6. Choose Save.
AWS CLI To move an instance to a placement group Use the following modify-instance-placement command. aws ec2 modify-instance-placement \ --instance-id i-0123a456700123456 \ --group-name MySpreadGroup To remove an instance from a placement group Use the following modify-instance-placement command. When you specify an empty string for the placement group name, this removes the instance from its current placement group. aws ec2 modify-instance-placement \ --instance-id i-0123a456700123456 \ --group-name ""
PowerShell To move an instance to a placement group Use the Edit-EC2InstancePlacement cmdlet with the name of the placement group.
Edit-EC2InstancePlacement `
    -InstanceId i-0123a456700123456 `
    -GroupName MySpreadGroup To remove an instance from a placement group Use the Edit-EC2InstancePlacement cmdlet with an empty string for the name of the placement group.
Edit-EC2InstancePlacement `
    -InstanceId i-0123a456700123456 `

    -GroupName ""
## Delete a placement group If you need to replace a placement group or no longer need one, you can delete it. Before you can delete a placement group, it must contain no instances. You can terminate the instances, move them to another placement group, or remove them from the placement group.
Console To delete a placement group
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Placement Groups.
3. Select the placement group and choose Actions, Delete.
4. When prompted for confirmation, enter Delete and then choose Delete.
AWS CLI To delete a placement group Use the delete-placement-group command. aws ec2 delete-placement-group --group-name my-cluster PowerShell To delete a placement group Use the Remove-EC2PlacementGroup cmdlet.
Remove-EC2PlacementGroup -GroupName my-cluster
## Shared placement groups Placement group sharing allows you to influence the placement of interdependent instances that are owned by separate AWS accounts. An owner can share a placement group across multiple AWS

accounts or within their organization. A participant can launch instances in a placement group that is shared with their account.
A placement group owner can share a placement group with:
- Specific AWS accounts inside or outside of its organization
- An organizational unit inside its organization
- Its entire organization You can use VPC peering to connect instances owned by separate AWS accounts and get the full latency benefits offered by shared cluster placement groups.
Contents
- Rules and limitations
- Required permissions
- Sharing across Availability Zones
- Placement group sharing
- Placement group unsharing Rules and limitations The following rules and limitations apply when you share a placement group or when a placement group is shared with you.
- To share a placement group, you must own it in your AWS account. You can't share a placement group that has been shared with you.
- When you share a partition or spread placement group, the placement group limits do not change. A shared partition placement group supports a maximum of seven partitions per Availability Zone, and a shared spread placement group supports a maximum of seven running instances per Availability Zone.
- To share a placement group with your organization or an organizational unit in your organization, you must enable sharing with AWS Organizations. For more information, see Sharing your AWS resources.
- When using the AWS Management Console to launch an instance, you can select any placement groups that were shared with you. When using the AWS CLI to launch an instance, you must

specify a shared placement group by ID, not by name. You can use the name of a placement group only if you're the owner of the shared placement group.
- You are responsible for managing the instances owned by you in a shared placement group.
- You can't view or modify instances and capacity reservations that are associated with a shared placement group but not owned by you.
- The Amazon Resource Name (ARN) of a placement group contains the ID of the account that owns the placement group. You can use the account ID portion of a placement group ARN to identify the owner of a placement group that is shared with you.
### Required permissions To share a placement group, users must have permissions for following actions:
- ec2:PutResourcePolicy
- ec2:DeleteResourcePolicy
### Sharing across Availability Zones To ensure that resources are distributed across the Availability Zones for a Region, we independently map Availability Zones to names for each account. This could lead to Availability Zone naming differences across accounts. For example, the Availability Zone us-east-1a for your AWS account might not have the same location as us-east-1a for another AWS account.
To specify the location of your Dedicated Hosts relative to your accounts, you must use the Availability Zone ID (AZ ID). The AZ ID is a unique and consistent identifier for an Availability Zone across all AWS accounts. For example, use1-az1 is an Availability Zone ID for the us-east-1 Region and it is the same location in every AWS account. For more information, see AZ IDs.
### Placement group sharing To share a placement group, you must add it to a resource share. A resource share is an AWS RAM resource that lets you share your resources across AWS accounts. A resource share specifies the resources to share, and the consumers with whom they are shared.
If you are part of an organization in AWS Organizations sharing within your organization is enabled, consumers in your organization are granted access to the shared placement group.

If the placement group is shared with an AWS account outside of your organization, the AWS account owner will receive an invitation to join the resource share. They can access the shared placement group after accepting the invitation.
You can share a placement group across AWS accounts using AWS Resource Access Manager. For more information, see Creating a resource share in the AWS RAM User Guide.
### Placement group unsharing The placement group owner can unshare a shared placement group at any time. When you unshare a shared placement group, the following changes occur:
- The AWS accounts with which a placement group was shared are no longer able to launch instances or reserve capacity.
- Any instances running in a shared placement group are disassociated from the placement group, but they continue to run in your AWS account.
- Any capacity reservations in a shared placement group are disassociated from the placement group, but remain available to you in your AWS account.
For more information, see Deleting a resource share in the AWS RAM User Guide.
## Placement groups on AWS Outposts AWS Outposts is a fully managed service that extends AWS infrastructure, services, APIs, and tools to customer premises. By providing local access to AWS managed infrastructure, AWS Outposts enables customers to build and run applications on premises using the same programming interfaces as in AWS Regions, while using local compute and storage resources for lower latency and local data processing needs.
An Outpost is a pool of AWS compute and storage capacity deployed at a customer site. AWS operates, monitors, and manages this capacity as part of an AWS Region.
You can create placement groups on Outposts that you have created in your account. This allows you to spread out instances across underlying hardware on an Outpost at your site. You create and use placement groups on Outposts in the same way that you create and use placement groups in regular Availability Zones. When you create a placement group with a spread strategy on an Outpost, you can choose to have the placement group spread instances across hosts or racks.
Spreading instances across hosts allows you to use a spread strategy with a single rack Outpost.
