# Virtual private clouds for your EC2 instances

Source: apps/user-manuals/aws/ec2-ug.pdf

---

Use the following command to enable jumbo frames.
Set-NetAdapterAdvancedProperty -Name "Ethernet" -RegistryKeyword "*JumboPacket" - RegistryValue 9014 Use the following command to disable jumbo frames.
Set-NetAdapterAdvancedProperty -Name "Ethernet" -RegistryKeyword "*JumboPacket" - RegistryValue 1514 AWS PV driver You can change the MTU using the netsh command on your instance. You can't change the MTU using Device Manager.
Use the following command to enable jumbo frames. netsh interface ipv4 set subinterface "Ethernet" mtu=9001 Use the following command to disable jumbo frames. netsh interface ipv4 set subinterface "Ethernet" mtu=1500
## Troubleshoot If you experience connectivity issues between your EC2 instance and an Amazon Redshift cluster when using jumbo frames, see Queries appear to hang and sometimes fail to reach the cluster in the Amazon Redshift Management Guide.
# Virtual private clouds for your EC2 instances Amazon Virtual Private Cloud (Amazon VPC) enables you to define a virtual network in your own logically isolated area within the AWS cloud, known as a virtual private cloud or VPC. You can create AWS resources, such as Amazon EC2 instances, into the subnets of your VPC. Your VPC closely resembles a traditional network that you might operate in your own data center, with the benefits of using scalable infrastructure from AWS. You can configure your VPC; you can select its IP address

range, create subnets, and configure route tables, network gateways, and security settings. You can connect instances in your VPC to the internet or to your own data center.
Contents
- Your default VPCs
- Nondefault VPCs
- Internet access
- Shared subnets
- IPv6-only subnets
## Your default VPCs When you create your AWS account, we create a default VPC in each Region. A default VPC is a VPC that is already configured and ready for you to use. For example, there is a default subnet for each Availability Zone in each default VPC, an internet gateway attached to the VPC, and there's a route in the main route table that sends all traffic (0.0.0.0/0) to the internet gateway. You can modify the configuration of your default VPCs as needed. For example, you can add subnets and route tables.

## Nondefault VPCs Instead of using a default VPC for your resources, you can create your own VPC, as described in Create a VPC in the Amazon VPC User Guide.
Here are some things to consider when creating a VPC for your EC2 instances.
- You can use the default suggestion for the IPv4 CIDR block or enter the CIDR block required by your application or network.
- To ensure high availability, create subnets in multiple Availability Zones.
- If your instances must be accessible from the internet, do one of the following:

- If your instances can be in a public subnet, add public subnets. Keep both DNS options enabled. You can optionally add private subnets now or later on.
- If your instances must be in a private subnet, add only private subnets. You can add a NAT gateway to provide internet access to instances in the private subnets. If your instances send or receive a significant volume of traffic across Availability Zones, create a NAT gateway in each Availability Zone. Otherwise, you can create a NAT gateway in just one of the Availability Zones and launch instances that send or receive cross-zone traffic in the same Availability Zone as the NAT gateway.
## Internet access Instances launched into a default subnet in a default VPC have access to the internet, as default VPCs are configured to assign public IP addresses and DNS hostnames, and the main route table is configured with a route to an internet gateway attached to the VPC.
For instances that you launch in nondefault subnets and VPCs, you can use one of the following options to ensure that the instances that you launch in these subnets have access to the internet:
- Configure an internet gateway. For more information, see Connect to the internet using an internet gateway in the Amazon VPC User Guide.
- Configure a public NAT gateway. For more information, see Access the internet from a private subnet in the Amazon VPC User Guide.
## Shared subnets When launching EC2 instances into shared VPC subnets, note the following:
- Participants can run instances in a shared subnet by specifying the ID of the shared subnet.
Participants must own any network interfaces that they specify.
- Participants can start, stop, terminate, and describe instances that they've created in a shared subnet. Participants can't start, stop, terminate, or describe instances that the VPC owner created in the shared subnet.
- VPC owners can't start, stop, terminate, or describe instances created by participants in a shared subnet.
- Participants can connect to an instance in a shared subnet using EC2 Instance Connect Endpoint. The participant must create the EC2 Instance Connect Endpoint in the shared subnet.
