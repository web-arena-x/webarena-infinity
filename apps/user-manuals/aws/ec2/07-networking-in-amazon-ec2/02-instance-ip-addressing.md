# Amazon EC2 instance IP addressing

Source: apps/user-manuals/aws/ec2-ug.pdf

---

For more information, see Get started with Outposts racks or Get started with Outposts servers.
### Volumes on an Outposts rack If your Outposts compute capacity is on an Outpost rack, you can create EBS volumes in the Outpost subnet that you created. When you create the volume, specify the Amazon Resource Name (ARN) of the Outpost.
The following create-volume command creates an empty 50 GB volume on the specified Outpost. aws ec2 create-volume --availability-zone us-east-2a --outpost-arn arn:aws:outposts:us- east-2:123456789012:outpost/op-03e6fecad652a6138 --size 50 You can dynamically modify the size of your Amazon EBS gp2 volumes without detaching them.
For more information about modifying a volume without detaching it, see Request modifications to your EBS volumes in the Amazon EBS User Guide.
We recommend that you limit the root volume for an instance on an Outpost rack to 30 GiB or smaller. You can specify data volumes in the block device mapping of the AMI or the instance to provide additional storage. To trim unused blocks from the boot volume, see How to Build Sparse EBS Volumes in the AWS Partner Network Blog.
We recommend that you increase the NVMe timeout for the root volume. For more information, see I/O operation timeout in the Amazon EBS User Guide.
### Volumes on an Outposts server Instances on Outposts servers provide instance store volumes but do not support EBS volumes.
Choose an Amazon EBS-backed AMI with only a single EBS snapshot. Choose an instance size with enough instance storage to meet the needs of your application. For more information, see Instance store volume limits.
# Amazon EC2 instance IP addressing Amazon EC2 and Amazon VPC support both the IPv4 and IPv6 addressing protocols. By default, Amazon VPC uses the IPv4 addressing protocol; you can't disable this behavior. When you create a VPC, you must specify an IPv4 CIDR block (a range of private IPv4 addresses). You can optionally assign an IPv6 CIDR block to your VPC and assign IPv6 addresses from that block to instances in your subnets.

When you launch an EC2 instance, you specify a VPC and a subnet. The instance receives a private IPv4 address from the CIDR range of the subnet. You can optionally configure your instances with public IPv4 addresses and IPv6 addresses. If EC2 instances in different VPCs communicate using public IP addresses, the traffic stays in the AWS private global network and does not traverse the public internet.
Contents
- Private IPv4 addresses
- Public IPv4 addresses
- Public IPv4 address optimization
- IPv6 addresses
- Multiple IP addresses
- EC2 instance hostnames
- Link-local addresses
- Manage the IPv4 addresses for your EC2 instances
- Manage the IPv6 addresses for your EC2 instances
- Secondary IP addresses for your EC2 instances
- Configure secondary private IPv4 addresses for Windows instances
## Private IPv4 addresses A private IPv4 address is an IP address that's not reachable over the Internet. You can use private IPv4 addresses for communication between instances in the same VPC. For more information about the standards and specifications of private IPv4 addresses, see RFC 1918. We allocate private IPv4 addresses to instances using DHCP.
Note You can create a VPC with a publicly routable CIDR block that falls outside of the private IPv4 address ranges specified in RFC 1918. However, for the purposes of this documentation, we refer to private IPv4 addresses (or 'private IP addresses') as the IP addresses that are within the IPv4 CIDR range of your VPC.
VPC subnets can be one of the following types:

- IPv4-only subnets – You can only create resources in these subnets with IPv4 addresses assigned to them.
- IPv6-only subnets – You can only create resources in these subnets with IPv6 addresses assigned to them.
- IPv4 and IPv6 subnets – You can create resources in these subnets with either IPv4 or IPv6 addresses assigned to them.
When you launch an EC2 instance into an IPv4-only or dual stack (IPv4 and IPv6) subnet, the instance receives a primary private IP address from the IPv4 address range of the subnet. For more information, see IP addressing in the Amazon VPC User Guide. If you don't specify a primary private IP address when you launch the instance, we select an available IP address in the subnet's IPv4 range for you. Each instance has a default network interface (index 0) that is assigned the primary private IPv4 address. You can also specify additional private IPv4 addresses, known as secondary private IPv4 addresses. Unlike primary private IP addresses, secondary private IP addresses can be reassigned from one instance to another. For more information, see Multiple IP addresses.
A private IPv4 address, regardless of whether it is a primary or secondary address, remains associated with the network interface when the instance is stopped and started, or hibernated and started, and is released when the instance is terminated.
## Public IPv4 addresses A public IP address is an IPv4 address that's reachable from the Internet. You can use public addresses for communication between your instances and the Internet.
When you launch an instance in a default VPC, we assign it a public IP address by default. When you launch an instance into a nondefault VPC, the subnet has an attribute that determines whether instances launched into that subnet receive a public IP address from the public IPv4 address pool.
By default, we don't assign a public IP address to instances launched in a nondefault subnet.
You can control whether your instance receives a public IP address as follows:
- Modify the public IP addressing attribute of your subnet. For more information, see Modify the public IPv4 addressing attribute for your subnet in the Amazon VPC User Guide.
- Enable or disable the public IP addressing feature during launch. This overrides the subnet's public IP addressing attribute. For more information, see Assign a public IPv4 address at launch.
- Unassign a public IP address from your instance after launch. For more information, see the section called "Manage IP addresses".

A public IP address is assigned to your instance from Amazon's pool of public IPv4 addresses, and is not associated with your AWS account. When a public IP address is disassociated from your instance, it is released back into the public IPv4 address pool, and you cannot reuse it.
We release the public IP address from your instance and assign a new one in the following cases:
- We release the public IP address when the instance is stopped, hibernated, or terminated. We assign a new public IP address when you start your stopped or hibernated instance.
- We release the public IP address when you associate an Elastic IP address with the instance. We assign a new public IP address when you disassociate the Elastic IP address from your instance.
- If we release the public IP address of your instance and it has a secondary network interface, we do not assign a new public IP address.
- If we release the public IP address of your instance and it has a secondary private IP address that is associated with an Elastic IP address, we do not assign a new public IP address.
If you require a persistent public IP address that can be associated to and from instances as you require, use an Elastic IP address instead.
If you use dynamic DNS to map an existing DNS name to a new instance's public IP address, it might take up to 24 hours for the IP address to propagate through the Internet. As a result, new instances might not receive traffic while terminated instances continue to receive requests. To solve this problem, use an Elastic IP address. You can allocate your own Elastic IP address, and associate it with your instance. For more information, see Elastic IP addresses.
If you are using Amazon VPC IP Address Manager (IPAM), you can get a contiguous block of public IPv4 addresses from AWS and use it to allocate Elastic IP addresses to AWS resources. Using contiguous IPv4 address blocks can significantly reduce management overhead for security access control lists and simplify IP address allocation and tracking for enterprises scaling on AWS. For more information, see Allocate sequential Elastic IP addresses from an IPAM pool in the Amazon VPC IPAM User Guide.
Considerations
- AWS charges for all public IPv4 addresses, including public IPv4 addresses associated with running instances and Elastic IP addresses. For more information, see the Public IPv4 Address tab on the Amazon VPC pricing page.
- Instances that access other instances through their public NAT IP address are charged for regional or Internet data transfer, depending on whether the instances are in the same Region.

## Public IPv4 address optimization AWS charges for all public IPv4 addresses, including public IPv4 addresses associated with running instances and Elastic IP addresses. For more information, see the Public IPv4 Address tab on the Amazon VPC pricing page.
The following list contains actions you can take to optimize the number of public IPv4 addresses you use:
- Use an elastic load balancer to load balance traffic to your EC2 instances and disable Auto-assign public IP on the primary ENI assigned to the instances. Load balancers use a single public IPv4 address, so this reduces your public IPv4 address count. You may also want consolidate existing load balancers to further reduce the public IPv4 address count.
- If the only reason for using a NAT gateway is to SSH into an EC2 instance in a private subnet for maintenance or emergencies, consider using EC2 Instance Connect Endpoint instead. With EC2 Instance Connect Endpoint, you can connect to an instance from the internet without requiring the instance to have a public IPv4 address.
- If your EC2 instances are in a public subnet with public IP addresses allocated to them, consider moving the instances to a private subnet, removing the public IP addresses, and using a public NAT gateway to allow access to and from your EC2 instances. There are cost considerations for using NAT gateways. Use this calculation method to decide if NAT gateways are cost effective.
You can get the Number of public IPv4 addresses required for this calculation by creating an AWS Billing Cost and Usage Report.
NAT gateway per hour + NAT gateway public IPs + NAT gateway transfer / Existing public IP cost Where:
- NAT gateway per hour = $0.045 * 730 hours in a month * Number of Availability Zones the NAT gateways are in
- NAT gateway public IPs = $0.005 * 730 hours in a month * Number of IPs associated with your NAT gateways
- NAT gateway transfer = $0.045 * Number of GBs that will go through the NAT gateway in a month
- Existing public IP cost = $0.005 * 730 hours in a month * Number of public IPv4 addresses

If the total is less than 1, NAT gateways are cheaper than public IPv4 addresses.
- Use AWS PrivateLink to connect privately to AWS services or services hosted by other AWS accounts rather than using public IPv4 addresses and internet gateways.
- Bring your own IP address range (BYOIP) to AWS and use the range for public IPv4 addresses rather than using Amazon-owned public IPv4 addresses.
- Turn off auto-assign public IPv4 address for instances launched into subnets. This option is generally disabled by default for VPCs when you create a subnet, but you should check your existing subnets to ensure it's disabled.
- If you have EC2 instances that do not need public IPv4 addresses,  check that the network interfaces attached to your instances have Auto-assign public IP disabled.
- Configure accelerator endpoints in AWS Global Accelerator for EC2 instances in private subnets to enable internet traffic to flow directly to the endpoints in your VPCs without requiring public IP addresses. You can also bring your own addresses to AWS Global Accelerator and use your own IPv4 addresses for your accelerator's static IP addresses.
## IPv6 addresses IPv6 addresses are globally unique and can be configured to remain private or reachable over the Internet. Both public and private IPv6 addressing is available in AWS:
- Private IPv6: AWS considers private IPv6 addresses those that are not advertised and cannot be advertised on the Internet from AWS.
- Public IPv6: AWS considers public IPv6 addresses those that are advertised on the Internet from AWS.
For more information about public and private IPv6 addresses, see IPv6 addresses in the Amazon VPC User Guide.
All instance types support IPv6 addresses except for the following: C1, M1, M2, M3, and T1.
Your EC2 instances receive an IPv6 address if an IPv6 CIDR block is associated with your VPC and subnet, and if one of the following is true:
- Your subnet is configured to automatically assign an IPv6 address to an instance during launch.
For more information, see Modify the IP addressing attributes of your subnet.

- You assign an IPv6 address to your instance during launch.
- You assign an IPv6 address to the primary network interface of your instance after launch.
- You assign an IPv6 address to a network interface in the same subnet, and attach the network interface to your instance after launch.
When your instance receives an IPv6 address during launch, the address is associated with the primary network interface (index 0) of the instance. You can manage the IPv6 addresses for your instances primary network interface as follows:
- Assign and unassign IPv6 addresses from the network interface. The number of IPv6 addresses you can assign to a network interface and the number of network interfaces you can attach to an instance varies per instance type. For more information, see Maximum IP addresses per network interface.
- Enable a primary IPv6 address. A primary IPv6 address enables you to avoid disrupting traffic to instances or ENIs. For more information, see Create a network interface for your EC2 instance or Manage the IP addresses for your network interface.
An IPv6 address persists when you stop and start, or hibernate and start, your instance, and is released when you terminate your instance. You cannot reassign an IPv6 address while it's assigned to another network interface—you must first unassign it.
You can control whether instances are reachable via their IPv6 addresses by controlling the routing for your subnet or by using security group and network ACL rules. For more information, see Internetwork traffic privacy in the Amazon VPC User Guide.
For more information about reserved IPv6 address ranges, see IANA IPv6 Special-Purpose Address Registry and RFC4291.
## Multiple IP addresses You can specify multiple private IPv4 and IPv6 addresses for your instances. The number of network interfaces and private IPv4 and IPv6 addresses that you can specify for an instance depends on the instance type. For more information, see Maximum IP addresses per network interface.

Use cases
- Host multiple websites on a single server by using multiple SSL certificates on a single server and associating each certificate with a specific IP address.
- Operate network appliances, such as firewalls or load balancers, that have multiple IP addresses for each network interface.
- Redirect internal traffic to a standby instance in case your instance fails, by reassigning the secondary IP address to the standby instance.
How multiple IP addresses work
- You can assign a secondary private IPv4 address to any network interface.
- You can assign multiple IPv6 addresses to a network interface that's in a subnet that has an associated IPv6 CIDR block.
- You must choose a secondary IPv4 address from the IPv4 CIDR block range of the subnet for the network interface.
- You must choose IPv6 addresses from the IPv6 CIDR block range of the subnet for the network interface.
- You associate security groups with network interfaces, not individual IP addresses. Therefore, each IP address you specify in a network interface is subject to the security group of its network interface.
- Multiple IP addresses can be assigned and unassigned to network interfaces attached to running or stopped instances.
- Secondary private IPv4 addresses that are assigned to a network interface can be reassigned to another one if you explicitly allow it.
- An IPv6 address cannot be reassigned to another network interface; you must first unassign the IPv6 address from the existing network interface.
- When assigning multiple IP addresses to a network interface using the command line tools or API, the entire operation fails if one of the IP addresses can't be assigned.
- Primary private IPv4 addresses, secondary private IPv4 addresses, Elastic IP addresses, and IPv6 addresses remain with a secondary network interface when it is detached from an instance or attached to an instance.
- Although you can't detach the primary network interface from an instance, you can reassign the secondary private IPv4 address of the primary network interface to another network interface.

For more information, see the section called "Secondary IP addresses".
## EC2 instance hostnames When you create an EC2 instance, AWS creates a hostname for that instance. For more information on the types of hostnames and how they're provisioned by AWS, see EC2 instance hostnames and domains. Amazon provides a DNS server that resolves Amazon-provided hostnames to IPv4 and IPv6 addresses. The Amazon DNS server is located at the base of your VPC network range plus two.
For more information, see DNS attributes for your VPC in the Amazon VPC User Guide.
## Link-local addresses Link-local addresses are well-known, non-routable IP addresses. Amazon EC2 uses addresses from the link-local address space to provide services that are accessible only from an EC2 instance. These services do not run on the instance, they run on the underlying host. When you access the link- local addresses for these services, you're communicating with either the Xen hypervisor or the Nitro controller.
Link-local address ranges
- IPv4 – 169.254.0.0/16 (169.254.0.0 to 169.254.255.255)
- IPv6 – fe80::/10 Services that you access using link-local addresses
- Instance Metadata Service
- Amazon Route 53 Resolver (also known as the Amazon DNS server)
- Amazon Time Sync Service
- AWS KMS servers
## Manage the IPv4 addresses for your EC2 instances You can assign a public IPv4 address to your instance when you launch it. You can view the IPv4 addresses for your instance in the console through either the Instances page or the Network Interfaces page.
Tasks
- Assign a public IPv4 address at launch

- Assign a private IPv4 address at launch
- View the primary IPv4 address
- View the IPv4 addresses using instance metadata
### Assign a public IPv4 address at launch Each subnet has an attribute that determines whether instances launched into that subnet are assigned a public IP address. By default, nondefault subnets have this attribute set to false, and default subnets have this attribute set to true. When you launch an instance, a public IPv4 addressing feature is also available for you to control whether your instance is assigned a public IPv4 address; you can override the default behavior of the subnet's IP addressing attribute. The public IPv4 address is assigned from Amazon's pool of public IPv4 addresses, and is assigned to the network interface with the device index of 0. This feature depends on certain conditions at the time you launch your instance.
Considerations
- You can unassign the public IP address from your instance after launch by managing the IP addresses associated with a network interface. For more information about public IPv4 addresses, see Public IPv4 addresses.
- You can't auto-assign a public IP address if you specify more than one network interface.
Additionally, you cannot override the subnet setting using the auto-assign public IP feature if you specify an existing network interface for device index 0.
- Whether you assign a public IP address to your instance during launch or not, you can associate an Elastic IP address with your instance after it's launched. For more information, see Elastic IP addresses. You can also modify your subnet's public IPv4 addressing behavior. For more information, see Modify the public IPv4 addressing attribute for your subnet.
Console To assign a public IPv4 address at launch Follow the procedure to launch an instance, and when you configure Network Settings, choose the option to Auto-assign Public IP.
AWS CLI To assign a public IPv4 address at launch

Use the run-instances command with the --associate-public-ip-address option.
--associate-public-ip-address PowerShell To assign a public IPv4 address at launch Use the New-EC2Instance cmdlet with the -AssociatePublicIp parameter.
-AssociatePublicIp $true
### Assign a private IPv4 address at launch You can specify a private IPv4 address from the IPv4 address range of the subnet, or let Amazon EC2 chose one for you. This address is assigned to the primary network interface.
To assign IPv4 addresses after launch, see the section called "Assign secondary IP addresses to an instance".
Console To assign a private IPv4 address at launch Follow the procedure to launch an instance. When you configure Network Settings, expand Advanced network configuration and enter a value for Primary IP.
AWS CLI To assign a private IPv4 address at launch Use the run-instances command with the --private-ip-address option.
--private-ip-addresses 10.251.50.12 To let Amazon EC2 choose the IP address, omit this option.
PowerShell To assign a private IPv4 address at launch

Use the New-EC2Instance cmdlet with the -PrivateIpAddress parameter.
-PrivateIpAddress 10.251.50.12 To let Amazon EC2 choose the IP address, omit this parameter.
### View the primary IPv4 address The public IPv4 address is displayed as a property of the network interface in the console, but it's mapped to the primary private IPv4 address through NAT. Therefore, if you inspect the properties of your network interface on your instance, for example, through ifconfig (Linux) or ipconfig (Windows), the public IPv4 address is not displayed.
Console To view the IPv4 addresses for an instance
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Instances.
3. Select the instance.
4. On the Networking tab, find Public IPv4 address and Private IPv4 addresses.
5. (Optional) The Networking tab also contains the network interfaces and Elastic IP addresses for the instance.
AWS CLI To view the primary IPv4 address for an instance Use the describe-instances command. aws ec2 describe-instances \ --instance-ids i-1234567890abcdef0 \ --query "Reservations[].Instances[].PrivateIpAddress" \ --output text The following is example output.
10.251.50.12

PowerShell To view the primary IPv4 address for an instance Use the Get-EC2Instance cmdlet.
(Get-EC2Instance `
    -InstanceId i-1234567890abcdef0).Instances.PrivateIpAddress The following is example output.
10.251.50.12
### View the IPv4 addresses using instance metadata You can get the IPv4 addresses for your instance by retrieving instance metadata. For more information, see Use instance metadata to manage your EC2 instance.
To view the IPv4 addresses using instance metadata
1. Connect to your instance. For more information, see Connect to your EC2 instance.
2. Run one of the following commands.
IMDSv2 Linux Run the following command from your Linux instance.
TOKEN=`curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2- metadata-token-ttl-seconds: 21600"` \ && curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/ meta-data/local-ipv4 Windows Run the following command from your Windows instance.
[string]$token = Invoke-RestMethod -Headers @{"X-aws-ec2-metadata-token-ttl- seconds" = "21600"} `

    -Method PUT -Uri http://169.254.169.254/latest/api/token Invoke-RestMethod -Headers @{"X-aws-ec2-metadata-token" = $token} `
    -Method GET -Uri http://169.254.169.254/latest/meta-data/local-ipv4 IMDSv1 Linux Run the following command from your Linux instance. curl http://169.254.169.254/latest/meta-data/local-ipv4 Windows Run the following command from your Windows instance.
Invoke-RestMethod http://169.254.169.254/latest/meta-data/local-ipv4
3. Use one of the following commands to access the public IP address. If there is an Elastic IP address associated with the instance, the command returns the Elastic IP address.
IMDSv2 Linux Run the following command from your Linux instance.
[ec2-user ~]$ TOKEN=`curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600"` \ && curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/ meta-data/public-ipv4 Windows Run the following command from your Windows instance.
[string]$token = Invoke-RestMethod -Headers @{"X-aws-ec2-metadata-token-ttl- seconds" = "21600"} `
    -Method PUT -Uri http://169.254.169.254/latest/api/token

Invoke-RestMethod -Headers @{"X-aws-ec2-metadata-token" = $token} `
    -Method GET -Uri http://169.254.169.254/latest/meta-data/public-ipv4 IMDSv1 Linux Run the following command from your Linux instance. curl http://169.254.169.254/latest/meta-data/public-ipv4 Windows Run the following command from your Windows instance.
Invoke-RestMethod http://169.254.169.254/latest/meta-data/public-ipv4
## Manage the IPv6 addresses for your EC2 instances If your VPC and subnet have IPv6 CIDR blocks associated with them, you can assign an IPv6 address to your instance during or after launch. You can access the IPv6 addresses for your instances in the console on either the Instances page or the Network Interfaces page. The following tasks configure IP addresses for your instances. To configure IP addresses for your network interfaces instead, see the section called "Manage IP addresses".
Tasks
- Assign an IPv6 address to an instance
- View the IPv6 addresses for an instance
- View IPv6 addresses using instance metadata
- Unassign an IPv6 address from an instance
### Assign an IPv6 address to an instance You can specify an IPv6 address from the IPv6 address range of the subnet, or let Amazon EC2 choose one for you. This address is assigned to the primary network interface. Note that the following instance types do not support IPv6 addresses: C1, M1, M2, M3, and T1.

Console To assign an IPv6 address at launch Follow the procedure to launch an instance. When you configure Network Settings, choose the option to Auto-assign IPv6 IP. If you don't see this option, the selected subnet does not have an associated IPv6 CIDR block.
To assign an IPv6 address after launch
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Instances.
3. Select your instance, and choose Actions, Networking, Manage IP addresses.
4. Expand the network interface. Under IPv6 addresses, choose Assign new IP address.
5. Enter an IPv6 address from the range of the subnet, or leave the field blank to let Amazon EC2 choose the IPv6 address for you. If you don't see this option, the instance subnet does not have an associated IPv6 CIDR block.
6. Choose Save.
AWS CLI To assign an IPv6 address at launch Use the run-instances command with the --ipv6-addresses option. The following example assigns two IPv6 addresses.
--ipv6-addresses Ipv6Address=2001:db8::1234:5678:1.2.3.4 Ipv6Address=2001:db8::1234:5678:5.6.7.8 To let Amazon EC2 choose the IPv6 addresses, use the --ipv6-address-count option instead. The following example assigns two IPv6 addresses.
--ipv6-address-count 2 To assign an IPv6 address after launch Use the assign-ipv6-addresses command. The following example assigns two IPv6 addresses.

aws ec2 assign-ipv6-addresses \ --network-interface-id eni-1234567890abcdef0 \ --ipv6-addresses 2001:db8::1234:5678:1.2.3.4 2001:db8::1234:5678:5.6.7.8 To let Amazon EC2 choose the IPv6 addresses, use the --ipv6-address-count option instead. The following example assigns two IPv6 addresses. aws ec2 assign-ipv6-addresses \ --network-interface-id eni-1234567890abcdef0 \ --ipv6-address-count 2 PowerShell To assign an IPv6 address at launch Use the New-EC2Instance cmdlet with the -Ipv6Address parameter. The following example assigns two IPv6 addresses.
-Ipv6Address $ipv6addr1,$ipv6addr2 Define the IPv6 addresses as follows.
$ipv6addr1 = New-Object Amazon.EC2.Model.InstanceIpv6Address $ipv6addr1.Ipv6Address = "2001:db8::1234:5678:1.2.3.4"
$ipv6addr2 = New-Object Amazon.EC2.Model.InstanceIpv6Address $ipv6addr2.Ipv6Address = "2001:db8::1234:5678:5.6.7.8"
To let Amazon EC2 choose the IPv6 addresses, use the -Ipv6AddressCount parameter instead. The following example assigns two IPv6 addresses.
-Ipv6AddressCount 2 To assign an IPv6 address after launch Use the Register-EC2Ipv6AddressList cmdlet. The following example assigns two IPv6 addresses.
Register-EC2Ipv6AddressList `

    -NetworkInterfaceId eni-1234567890abcdef0 `
    -Ipv6Address "2001:db8::1234:5678:1.2.3.4","2001:db8::1234:5678:5.6.7.8"
To let Amazon EC2 choose the IPv6 addresses, use the -Ipv6AddressCount parameter instead. The following example assigns two IPv6 addresses.
Register-EC2Ipv6AddressList `
    -NetworkInterfaceId eni-1234567890abcdef0 `
    -Ipv6AddressCount 2
### View the IPv6 addresses for an instance You can view the IPv6 addresses for your instances.
Console To view the IPv6 addresses for an instance
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Instances.
3. Select the instance.
4. On the Networking tab, locate IPv6 addresses.
AWS CLI To view the IPv6 address for an instance Use the describe-instances command. aws ec2 describe-instances \ --instance-ids i-1234567890abcdef0 \ --query "Reservations[*].Instances[].Ipv6Address" \ --output text The following is example output.
2001:db8::1234:5678:1.2.3.4

PowerShell To view the IPv6 address for an instance Use the Get-EC2Instance cmdlet.
(Get-EC2Instance `
    -InstanceId i-1234567890abcdef0).Instances.Ipv6Address The following is example output.
2001:db8::1234:5678:1.2.3.4
### View IPv6 addresses using instance metadata After you connect to your instance, you can retrieve the IPv6 addresses using instance metadata.
First, you must get the MAC address of the instance from http://169.254.169.254/latest/ meta-data/network/interfaces/macs/.
IMDSv2 Linux Run the following command from your Linux instance.
TOKEN=`curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata- token-ttl-seconds: 21600"` \ && curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta- data/network/interfaces/macs/mac-address/ipv6s Windows Run the following cmdlets from your Windows instance.
[string]$token = Invoke-RestMethod -Headers @{"X-aws-ec2-metadata-token-ttl-seconds"
 = "21600"} `
    -Method PUT -Uri http://169.254.169.254/latest/api/token Invoke-RestMethod -Headers @{"X-aws-ec2-metadata-token" = $token} `

    -Method GET -Uri http://169.254.169.254/latest/meta-data/network/interfaces/ macs/mac-address/ipv6s IMDSv1 Linux Run the following command from your Linux instance. curl http://169.254.169.254/latest/meta-data/network/interfaces/macs/mac-address/ ipv6s Windows Run the following cmdlet from your Windows instance.
Invoke-RestMethod -Uri http://169.254.169.254/latest/meta-data/network/interfaces/ macs/mac-address/ipv6s
### Unassign an IPv6 address from an instance You can unassign an IPv6 address from an instance at any time.
Console To unassign an IPv6 address from an instance
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Instances.
3. Select your instance, and choose Actions, Networking, Manage IP addresses.
4. Expand the network interface. Under IPv6 addresses, choose Unassign next to the IPv6 address.
5. Choose Save.
AWS CLI To unassign an IPv6 address from an instance Use the unassign-ipv6-addresses command.

aws ec2 unassign-ipv6-addresses \ --network-interface-id eni-1234567890abcdef0 \ --ipv6-addresses 2001:db8::1234:5678:1.2.3.4 PowerShell To unassign an IPv6 address from an instance Use the Unregister-EC2Ipv6AddressList cmdlet.
Unregister-EC2Ipv6AddressList `
    -NetworkInterfaceId eni-1234567890abcdef0 `
    -Ipv6Address 2001:db8::1234:5678:1.2.3.4
## Secondary IP addresses for your EC2 instances The first IPv4 address assigned to a network interface is known as the primary IP address.
Secondary IP addresses are additional IPv4 address assigned to a network interface. For more information, see the section called "Multiple IP addresses".
You can also assign multiple IPv6 addresses to an instance. For more information, see the section called "IPv6 addresses".
Tasks
- Assign secondary IP addresses to an instance
- Configure the operating system to use secondary IP addresses
- Unassign a secondary IP address from an instance
### Assign secondary IP addresses to an instance You can assign secondary IP addresses to the network interface for an instance as you launch the instance, or after the instance is running.
Console To assign a secondary IP address at launch
1. Follow the procedure to launch an instance. When you configure Network Settings, expand Advanced network configuration.

2. For Secondary IP, choose Automatically assign and enter the number of IP addresses for Amazon EC2 to assign. Alternatively, choose Manually assign and enter the IPv4 addresses.
3. Complete the remaining steps to launch the instance.
To assign a secondary IP address after launch
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Instances.
3. Select your instance, and choose Actions, Networking, Manage IP addresses.
4. Expand the network interface.
5. To add an IPv4 address, under IPv4 addresses, choose Assign new IP address. Enter an IPv4 address from the range of the subnet, or leave the field blank to let Amazon EC2 choose one for you.
6. Choose Save.
AWS CLI To assign a secondary IP address at launch Use the run-instances command with the --secondary-private-ip-addresses option.
--secondary-private-ip-addresses 10.251.50.12 To let Amazon EC2 choose the IP address, use the --secondary-private-ip-address- count option instead. The following example assigns one secondary IP address.
--secondary-private-ip-address-count 1 Alternatively, you can create a network interface. For more information, see the section called "Create a network interface".
To assign a secondary IP address after launch Use the assign-private-ip-addresses command with the --private-ip-addresses option. aws ec2 assign-private-ip-addresses \ --network-interface-ids eni-1234567890abcdef0 \

    --private-ip-addresses 10.251.50.12 To let Amazon EC2 choose the IPv4 address, use the --secondary-private-ip-address- count parameter instead. The following example assigns one IPv4 address. aws ec2 assign-private-ip-addresses \ --network-interface-ids eni-1234567890abcdef0 \ --secondary-private-ip-address-count 1 PowerShell To assign a secondary IP address at launch You must create a network interface. For more information, see the section called "Create a network interface".
To assign a secondary IP address after launch Use the Register-EC2PrivateIpAddress cmdlet with the -PrivateIpAddress parameter.
Register-EC2PrivateIpAddress `
    -NetworkInterfaceId eni-1234567890abcdef0 `
    -PrivateIpAddress 10.251.50.12 To let Amazon EC2 choose the IPv4 addresses, use the -SecondaryPrivateIpAddressCount parameter instead. The following example assigns one IPv4 address.
Register-EC2PrivateIpAddress `
    -NetworkInterfaceId eni-1234567890abcdef0 `
    -SecondaryPrivateIpAddressCount 1
### Configure the operating system to use secondary IP addresses After you assign a secondary IP address to your instance, you must configure the operating system on your instance to recognize the additional private IPv4 address.
Linux instances
- If you are using Amazon Linux, the ec2-net-utils package can take care of this step for you. It configures additional network interfaces that you attach while the instance is running, refreshes

secondary IPv4 addresses during DHCP lease renewal, and updates the related routing rules.
You can immediately refresh the list of interfaces by using one of the following commands, depending on your system: sudo systemctl restart systemd-networkd (AL2023) or sudo service network restart (Amazon Linux 2). You can view the up-to-date list using the following command: ip addr li. If you require manual control over your network configuration, you can remove the ec2-net-utils package. For more information, see Configure your network interface using ec2-net-utils.
- If you are using another Linux distribution, see the documentation for your Linux distribution.
Search for information about configuring additional network interfaces and secondary IPv4 addresses. If the instance has two or more interfaces on the same subnet, search for information about using routing rules to work around asymmetric routing.
Windows instances For more information, see Configure secondary private IPv4 addresses for Windows instances.
### Unassign a secondary IP address from an instance If you no longer require a secondary IP address, you can unassign it from the instance or the network interface. When a secondary private IPv4 address is unassigned from a network interface, the Elastic IP address (if it exists) is also disassociated.
Console To unassign a secondary private IPv4 address from an instance
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Instances.
3. Select an instance, choose Actions, Networking, Manage IP addresses.
4. Expand the network interface. For IPv4 addresses, choose Unassign for the IPv4 address to unassign.
5. Choose Save.
AWS CLI To unassign a secondary private IP address Use the unassign-private-ip-addresses command.

aws ec2 unassign-private-ip-addresses \ --network-interface eni-1234567890abcdef0\ --private-ip-addresses 10.251.50.12 PowerShell To unassign a secondary private IP address Use the Unregister-EC2PrivateIpAddress cmdlet.
Unregister-EC2PrivateIpAddress `
    -NetworkInterface eni-1234567890abcdef0 `
    -PrivateIpAddress 10.251.50.12
## Configure secondary private IPv4 addresses for Windows instances You can specify multiple private IPv4 addresses for your instances. After you assign a secondary private IPv4 address to an instance, you must configure the operating system on the instance to recognize the secondary private IPv4 address.
Note These instructions are based on Windows Server 2022. The implementation of these steps might vary based on the operating system of the Windows instance.
Tasks
- Prerequisites
- Step 1: Configure static IP addressing in your instance
- Step 2: Configure a secondary private IP address for your instance
- Step 3: Configure applications to Use the secondary private IP address
### Prerequisites
- Assign the secondary private IPv4 address to the network interface for the instance. You can assign the secondary private IPv4 address when you launch the instance, or after the instance is running. For more information, see Assign secondary IP addresses to an instance.

### Step 1: Configure static IP addressing in your instance To enable your Windows instance to use multiple IP addresses, you must configure your instance to use static IP addressing rather than a DHCP server.
Important When you configure static IP addressing in your instance, the IP address must match exactly what is shown in the console, CLI, or API. If you enter these IP addresses incorrectly, the instance could become unreachable.
To configure static IP addressing on a Windows instance
1. Connect to your instance.
2. Find the IP address, subnet mask, and default gateway addresses for the instance by performing the following steps:
- Run the following command in PowerShell: ipconfig /all Review the output and note the IPv4 Address, Subnet Mask, Default Gateway, and DNS Servers values for the network interface. Your output should resemble the following example:
...
Ethernet adapter Ethernet 4:
   Connection-specific DNS Suffix  . : us-west-2.compute.internal Description . . . . . . . . . . . : Amazon Elastic Network Adapter #2 Physical Address. . . . . . . . . : 02-9C-3B-FC-8E-67 DHCP Enabled. . . . . . . . . . . : Yes Autoconfiguration Enabled . . . . : Yes Link-local IPv6 Address . . . . . : fe80::f4d1:a773:5afa:cd1%7(Preferred)
   IPv4 Address. . . . . . . . . . . : 10.200.0.128(Preferred)
   Subnet Mask . . . . . . . . . . . : 255.255.255.0 Lease Obtained. . . . . . . . . . : Monday, April 8, 2024 12:19:29 PM Lease Expires . . . . . . . . . . : Monday, April 8, 2024 4:49:30 PM

   Default Gateway . . . . . . . . . : 10.200.0.1 DHCP Server . . . . . . . . . . . : 10.200.0.1 DHCPv6 IAID . . . . . . . . . . . : 151166011 DHCPv6 Client DUID. . . . . . . . : 00-01-00-01-2D-67-AC-FC-12-34-9A-BE-A5- E7 DNS Servers . . . . . . . . . . . : 10.200.0.2 NetBIOS over Tcpip. . . . . . . . : Enabled
3. Open the Network and Sharing Center by running the following command in PowerShell:
& $env:SystemRoot\system32\control.exe ncpa.cpl
4. Open the context (right-click) menu for the network interface (Local Area Connection or Ethernet) and choose Properties.
5. Choose Internet Protocol Version 4 (TCP/IPv4), Properties.
6. In the Internet Protocol Version 4 (TCP/IPv4) Properties dialog box, choose Use the following IP address, enter the following values, and then choose OK.
Field Value IP address The IPv4 address obtained in step 2 above.
Subnet mask The subnet mask obtained in step 2 above.
Default gateway The default gateway address obtained in step 2 above.
Preferred DNS server The DNS server obtained in step 2 above.
Alternate DNS server The alternate DNS server obtained in step 2 above. If an alternate DNS server was not listed, leave  this field blank.
Important If you set the IP address to any value other than the current IP address, you will lose connectivity to the instance.

You will lose RDP connectivity to the Windows instance for a few seconds while the instance converts from using DHCP to static addressing. The instance retains the same IP address information as before, but now this information is static and not managed by DHCP.
### Step 2: Configure a secondary private IP address for your instance After you have set up static IP addressing on your Windows instance, you are ready to prepare a second private IP address.
To configure a secondary IP address
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.

2. In the navigation pane, choose Instances and select your instance.
3. On the Networking, note the secondary IP address.
4. Connect to your instance.
5. On your Windows instance, choose Start, Control Panel.
6. Choose Network and Internet, Network and Sharing Center.
7. Select the network interface (Local Area Connection or Ethernet) and choose Properties.
8. On the Local Area Connection Properties page, choose Internet Protocol Version 4 (TCP/ IPv4), Properties, Advanced.
9. Choose Add.
10. In the TCP/IP Address dialog box, type the secondary private IP address for IP address. For Subnet mask, type the same subnet mask that you entered for the primary private IP address in Step 1: Configure static IP addressing in your instance, and then choose Add.
11. Verify the IP address settings and choose OK.

12. Choose OK, Close.
13. To confirm that the secondary IP address has been added to the operating system, run the ipconfig /all command in PowerShell. Your output should resemble the following:
Ethernet adapter Ethernet 4:
   Connection-specific DNS Suffix  . :
   Description . . . . . . . . . . . : Amazon Elastic Network Adapter #2 Physical Address. . . . . . . . . : 02-9C-3B-FC-8E-67 DHCP Enabled. . . . . . . . . . . : No Autoconfiguration Enabled . . . . : Yes Link-local IPv6 Address . . . . . : fe80::f4d1:a773:5afa:cd1%7(Preferred)
   IPv4 Address. . . . . . . . . . . : 10.200.0.128(Preferred)

   Subnet Mask . . . . . . . . . . . : 255.255.255.0 IPv4 Address. . . . . . . . . . . : 10.200.0.129(Preferred)
   Subnet Mask . . . . . . . . . . . : 255.255.255.0 Default Gateway . . . . . . . . . : 10.200.0.1 DHCPv6 IAID . . . . . . . . . . . : 151166011 DHCPv6 Client DUID. . . . . . . . : 00-01-00-01-2D-67-AC-FC-12-34-9A-BE-A5-E7 DNS Servers . . . . . . . . . . . : 10.200.0.2 NetBIOS over Tcpip. . . . . . . . : Enabled
### Step 3: Configure applications to Use the secondary private IP address You can configure any applications to use the secondary private IP address. For example, if your instance is running a website on IIS, you can configure IIS to use the secondary private IP address.
To configure IIS to use the secondary private IP address
1. Connect to your instance.
2. Open Internet Information Services (IIS) Manager.
3. In the Connections pane, expand Sites.
4. Open the context (right-click) menu for your website and choose Edit Bindings.
5. In the Site Bindings dialog box, for Type, choose http, Edit.
6. In the Edit Site Binding dialog box, for IP address, select the secondary private IP address. (By default, each website accepts HTTP requests from all IP addresses.)
