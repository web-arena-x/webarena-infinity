# Elastic network interfaces

Source: apps/user-manuals/aws/ec2-ug.pdf

---

The following is example output.
AllocationId    : eipalloc-abcdef01234567890 PtrRecord       : example.com.
PublicIp        : 192.0.2.0 PtrRecordUpdate :
                  Reason :
                  Status : PENDING Value  : example.net.
# Elastic network interfaces An elastic network interface is a logical networking component in a VPC that represents a virtual network card. You can create and configure network interfaces and attach them to instances that you launch in the same Availability Zone. The attributes of a network interface follow it as it's attached or detached from an instance and reattached to another instance. When you move a network interface from one instance to another, network traffic is redirected from the original instance to the new instance.
Note that this AWS resource is referred to as a network interface in the AWS Management Console and the Amazon EC2 API. Therefore, we use "network interface" in this documentation instead of "elastic network interface". The term "network interface" in this documentation always means "elastic network interface".
Network interface attributes A network interface can include the following attributes:
- A primary private IPv4 address from the IPv4 address range of your subnet
- A primary IPv6 address from the IPv6 address range of your subnet
- Secondary private IPv4 addresses from the IPv4 address range of your subnet
- One Elastic IP address (IPv4) for each private IPv4 address
- One public IPv4 address
- Secondary IPv6 addresses
- Security groups
- A MAC address
- A source/destination check flag

- A description Monitoring traffic You can enable a VPC flow log on your network interface to capture information about the traffic going to and from a network interface. After you've created a flow log, you can view and retrieve its data in Amazon CloudWatch Logs. For more information, see VPC Flow Logs in the Amazon VPC User Guide.
Contents
- Network interface concepts
- Network cards
- Maximum IP addresses per network interface
- Create a network interface for your EC2 instance
- Network interface attachments for your EC2 instance
- Manage the IP addresses for your network interface
- Modify network interface attributes
- Multiple network interfaces for your Amazon EC2 instances
- Requester-managed network interfaces
- Prefix delegation for Amazon EC2 network interfaces
- Delete a network interface
## Network interface concepts The following are important concepts to understand as you get started using network interfaces.
Primary network interface Each instance has a default network interface, called the primary network interface. You can't detach a primary network interface from an instance.
Secondary network interfaces You can create and attach secondary network interfaces to your instance. The maximum number of network interfaces varies by instance type. For more information, see Maximum IP addresses per network interface.

IPv4 addresses for network interfaces When you launch an EC2 instance into an IPv4-only or dual stack subnet, the instance receives a primary private IP address from the IPv4 address range of the subnet. You can also specify additional private IPv4 addresses, known as secondary private IPv4 addresses. Unlike primary private IP addresses, secondary private IP addresses can be reassigned from one instance to another.
Public IPv4 addresses for network interfaces All subnets have a modifiable attribute that determines whether network interfaces created in that subnet (and therefore instances launched into that subnet) are assigned a public IPv4 address. For more information, see Subnet settings in the Amazon VPC User Guide. When you launch an instance, the IP address is assigned to the primary network interface. If you specify an existing network interface as the primary network interface when you launch an instance, the public IPv4 address is determined by this network interface.
When you create a network interface, it inherits the public IPv4 addressing attribute from the subnet. If you later modify the public IPv4 addressing attribute of the subnet, the network interface keeps the setting that was in effect when it was created.
We release the public IP address when the instance is stopped, hibernated, or terminated. We assign a new public IP address when you start your stopped or hibernated instance, unless it has a secondary network interface or a secondary private IPv4 address that is associated with an Elastic IP address.
IPv6 addresses for network interfaces If you associate IPv6 CIDR blocks with your VPC and subnet, you can assign IPv6 addresses from the subnet range to a network interface. Each IPv6 address can be assigned to one network interface.
All subnets have a modifiable attribute that determines whether network interfaces created in that subnet (and therefore instances launched into that subnet) are automatically assigned an IPv6 address from the range of the subnet. When you launch an instance, the IPv6 address is assigned to the primary network interface.
Elastic IP addresses for network interfaces You can associate an Elastic IP address with one of the private IPv4 addresses for the network interface. You can associate one Elastic IP address with each private IPv4 address. If you

disassociate an Elastic IP address from a network interface, you can release it or associate it with a different instance.
Termination behavior You can set the termination behavior for a network interface that's attached to an instance. You can specify whether the network interface should be automatically deleted when you terminate the instance to which it's attached.
Source/destination checking You can enable or disable source/destination checks, which ensure that the instance is either the source or the destination of any traffic that it receives. Source/destination checks are enabled by default. You must disable source/destination checks if the instance runs services such as network address translation, routing, or firewalls.
## Requester-managed network interfaces These network interfaces are created and managed by AWS services to enable you to use some resources and services. You can't manage these network interfaces yourself. For more information, see Requester-managed network interfaces.
Prefix delegation A prefix is a reserved private IPv4 or IPv6 CIDR range that you allocate for automatic or manual assignment to network interfaces that are associated with an instance. By using Delegated Prefixes, you can launch services faster by assigning a range of IP addresses as a single prefix.
Managed network interfaces A managed network interface is managed by a service provider, such as Amazon EKS Auto Mode.
You can't directly modify the settings of a managed network interface. Managed network interface are identified by a true value in the Managed field. For more information, see Amazon EC2 managed instances.
## Network cards Most instance types support one network card. Instance types that support multiple network cards provide higher network performance, including bandwidth capabilities above 100 Gbps and improved packet rate performance. When you attach a network interface to an instance that supports multiple network cards, you can select the network card for the network interface. The primary network interface must be assigned to network card index 0.

EFA and EFA-only network interfaces count as a network interface. You can assign only one EFA or EFA-only network interface per network card. The primary network interface can't be an EFA-only network interface.
The following instance types support multiple network cards. For information about the number of network interfaces that an instance type supports, see Maximum IP addresses per network interface.
Instance type Number of network cards c6in.32xlarge 2 c6in.metal 2 c8gb.48xlarge 2 c8gb.metal-48xl 2 c8gn.48xlarge 2 c8gn.metal-48xl 2 dl1.24xlarge 4 g6e.24xlarge 2 g6e.48xlarge 4 g7e.24xlarge 2 g7e.48xlarge 4 hpc6id.32xlarge 2 hpc7a.12xlarge 2 hpc7a.24xlarge 2 hpc7a.48xlarge 2 hpc7a.96xlarge 2

Instance type Number of network cards hpc8a.96xlarge 2 m6idn.32xlarge 2 m6idn.metal 2 m6in.32xlarge 2 m6in.metal 2 m8gb.48xlarge 2 m8gn.48xlarge 2 p4d.24xlarge 4 p4de.24xlarge 4 p5.48xlarge 32 p5e.48xlarge 32 p5en.48xlarge 16 p6-b200.48xlarge 8 p6-b300.48xlarge 17 p6e-gb200.36xlarge 17 r8gb.48xlarge 2 r8gb.metal-48xl 2 r8gn.48xlarge 2 r8gn.metal-48xl 2 r6idn.32xlarge 2

Instance type Number of network cards r6idn.metal 2 r6in.32xlarge 2 r6in.metal 2 trn1.32xlarge 8 trn1n.32xlarge 16 trn2.48xlarge 16 trn2u.48xlarge 16 u7in-16tb.224xlarge 2 u7in-24tb.224xlarge 2 u7in-32tb.224xlarge 2 u7inh-32tb.480xlarge 2
## Maximum IP addresses per network interface Each instance type supports a maximum number of network interfaces, maximum number of private IPv4 addresses per network interface, and maximum number of IPv6 addresses per network interface. The limit for IPv6 addresses is separate from the limit for private IPv4 addresses per network interface. Note that all instance types support IPv6 addressing except for the following:
C1, M1, M2, M3, and T1.
Available network interfaces The Amazon EC2 Instance Types Guide provides the information about the network interfaces available for each instance type. For more information, see the following:
- Network specifications – General purpose
- Network specifications – Compute optimized
- Network specifications – Memory optimized

- Network specifications – Storage optimized
- Network specifications – Accelerated computing
- Network specifications – High-performance computing
- Network specifications – Previous generation Console To retrieve the maximum network interfaces
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Instance Types.
3. Add a filter to specify the instance type (Instance type=c5.12xlarge) or instance family (Instance family=c5).
4. (Optional) Click the Preferences icon and then turn on Maximum number of network interfaces. This column indicates the maximum number of network interfaces for each instance type.
5. (Optional) Select the instance type. On the Networking tab, find Maximum number of network interfaces.
AWS CLI To retrieve the maximum network interfaces You can use the describe-instance-types command to display information about an instance type, such as its supported network interfaces and IP addresses per interface. The following example displays this information for all C5 instances. aws ec2 describe-instance-types \ --filters "Name=instance-type,Values=c5.*" \ --query "InstanceTypes[].{ \ Type: InstanceType, \ MaxENI: NetworkInfo.MaximumNetworkInterfaces, \ IPv4addr: NetworkInfo.Ipv4AddressesPerInterface}" \ --output table The following is example output.
---------------------------------------

|        DescribeInstanceTypes        | +----------+----------+---------------+
| IPv4addr | MaxENI   |     Type      | +----------+----------+---------------+
|  30      |  8       |  c5.4xlarge   |
|  50      |  15      |  c5.24xlarge  |
|  15      |  4       |  c5.xlarge    |
|  30      |  8       |  c5.12xlarge  |
|  10      |  3       |  c5.large     |
|  15      |  4       |  c5.2xlarge   |
|  50      |  15      |  c5.metal     |
|  30      |  8       |  c5.9xlarge   |
|  50      |  15      |  c5.18xlarge  | +----------+----------+---------------+ PowerShell To retrieve the maximum network interfaces You can use the Get-EC2InstanceType PowerShell command to display information about an instance type, such as its supported network interfaces and IP addresses per interface. The following example displays this information for all C5 instances.
Get-EC2InstanceType -Filter @{Name="instance-type"; Values="c5.*"} | `
Select-Object `
    @{Name='Ipv4AddressesPerInterface'; Expression={($_.Networkinfo.Ipv4AddressesPerInterface)}}, @{Name='MaximumNetworkInterfaces'; Expression={($_.Networkinfo.MaximumNetworkInterfaces)}}, InstanceType | `
Format-Table -AutoSize The following is example output.
Ipv4AddressesPerInterface MaximumNetworkInterfaces InstanceType ------------------------- ------------------------ ------------ 30                        8 c5.4xlarge 15                        4 c5.xlarge 30                        8 c5.12xlarge 50                       15 c5.24xlarge 30                        8 c5.9xlarge 50                       15 c5.metal 15                        4 c5.2xlarge

                       10                        3 c5.large 50                       15 c5.18xlarge
## Create a network interface for your EC2 instance You can create a network interface for use by your EC2 instances. When you create a network interface, you specify the subnet for which it is created. You can't move a network interface to another subnet after it's created. You must attach a network interface to an instance in the same Availability Zone. You can detach a secondary network interface from an instance and then attach it to a different instance in the same Availability Zone. You can't detach a primary network interface from an instance. For more information, see the section called "Network interface attachments".
Console To create a network interface
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Network Interfaces.
3. Choose Create network interface.
4. (Optional) For Description, enter a descriptive name.
5. For Subnet, select a subnet. The options available in the subsequent steps change depending on the type of subnet you select (IPv4-only, IPv6-only, or dual-stack (IPv4 and IPv6)).
6. For Interface type, choose one of the following:
- ENA: A high-performance network interface designed to handle high throughput and packet-per-second rates for TCP/IP protocols while minimizing CPU usage. This is the default value. For more information about ENA, see Elastic Network Adapter.
- EFA with ENA: A network interface that supports both ENA and EFA devices for traditional TCP/IP based transport along with SRD based transport. If you choose EFA with ENA, the instance you are attaching it to must support EFA. For more information about EFA, see Elastic Fabric Adapter.
- EFA-only: A high-performance network interface designed to handle high throughput, low latency inter-node communication for SRD based transport while bypassing the operating system stack. If you choose this option, the instance you are attaching it to

must support EFA. EFA-only network interfaces do not support IP addresses. For more information about EFA, see Elastic Fabric Adapter.
7. For Private IPv4 address, do one of the following:
- Choose Auto-assign to allow Amazon EC2 to select an IPv4 address from the subnet.
- Choose Custom and enter an IPv4 address that you select from the subnet.
8. (Subnets with IPv6 addresses only) For IPv6 address, do one of the following:
- Choose None if you do not want to assign an IPv6 address to the network interface.
- Choose Auto-assign to allow Amazon EC2 to select an IPv6 address from the subnet.
- Choose Custom and enter an IPv6 address that you select from the subnet.
9. (Optional) If you're creating a network interface in a dual-stack or IPv6-only subnet, you have the option to Assign Primary IPv6 IP. This assigns a primary IPv6 global unicast address (GUA) to the network interface. Assigning a primary IPv6 address enables you to avoid disrupting traffic to instances or ENIs. Choose Enable if the instance that this ENI will be attached to relies on its IPv6 address not changing. AWS will automatically assign an IPv6 address associated with the ENI attached to your instance to be the primary IPv6 address. Once you enable an IPv6 GUA address to be a primary IPv6, you can't disable it.
When you enable an IPv6 GUA address to be a primary IPv6, the first IPv6 GUA will be made the primary IPv6 address until the instance is terminated or the network interface is detached. If you have multiple IPv6 addresses associated with an ENI attached to your instance and you enable a primary IPv6 address, the first IPv6 GUA address associated with the ENI becomes the primary IPv6 address.
10. (Optional) To create an Elastic Fabric Adapter, choose Elastic Fabric Adapter, Enable.
11. (Optional) Under Advanced settings, you can optionally set IP prefix delegation. For more information, see Prefix delegation.
- Auto-assign — AWS chooses the prefix from the IPv4 or IPv6 CIDR blocks for the subnet, and assigns it to the network interface.
- Custom — You specify the prefix from the IPv4 or IPv6 CIDR blocks for the subnet, and AWS verifies that the prefix is not already assigned to other resources before assigning it to the network interface.
12. (Optional) Under Advanced settings, for Idle connection tracking timeout, modify the default idle connection timeouts. For more information, see Idle connection tracking timeout.

- TCP established timeout: Timeout (in seconds) for idle TCP connections in an established state.
- Min: 60 seconds
- Max: 432000 seconds
- Default: 350 seconds for Nitrov6 instance types, excluding P6e-GB200. And 432000 seconds for other instance types, including P6e-GB200.
- Recommended: Less than 432000 seconds
- UDP timeout: Timeout (in seconds) for idle UDP flows that have seen traffic only in a single direction or a single request-response transaction.
- Min: 30 seconds
- Max: 60 seconds
- Default: 30 seconds
- UDP stream timeout: Timeout (in seconds) for idle UDP flows classified as streams which have seen more than one request-response transaction.
- Min: 60 seconds
- Max: 180 seconds
- Default: 180 seconds
13. For Security groups, select one or more security groups.
14. (Optional) For each tag, choose Add new tag and enter a tag key and an optional tag value.
15. Choose Create network interface.
AWS CLI Example 1: To create a network interface with IP addresses chosen by Amazon EC2 Use the following create-network-interface command. This example creates a network interface with a public IPv4 address and an IPv6 address chosen by Amazon EC2. aws ec2 create-network-interface \ --subnet-id subnet-0abcdef1234567890 \ --description "my dual-stack network interface" \ --ipv6-address-count 1 \ --groups sg-1234567890abcdef0

Example 2: To create a network interface with specific IP addresses Use the following create-network-interface command. aws ec2 create-network-interface \ --subnet-id subnet-0abcdef1234567890 \ --description "my dual-stack network interface" \ --private-ip-address 10.251.50.12 \ --ipv6-addresses 2001:db8::1234:5678:1.2.3.4 \ --groups sg-1234567890abcdef0 Example 3: To create a network interface with a count of secondary IP addresses Use the following create-network-interface command. In this example, Amazon EC2 chooses both the primary IP address and the secondary IP addresses. aws ec2 create-network-interface \ --subnet-id subnet-0abcdef1234567890 \ --description "my network interface" \ --secondary-private-ip-address-count 2 \ --groups sg-1234567890abcdef0 Example 4: To create a network interface with a specific secondary IP address Use the following create-network-interface command. This example specifies a primary IP address and a secondary IP address. aws ec2 create-network-interface \ --subnet-id subnet-0abcdef1234567890 \ --description "my network interface" \ --private-ip-addresses PrivateIpAddress=10.0.1.30,Primary=true \ PrivateIpAddress=10.0.1.31,Primary=false --groups sg-1234567890abcdef0 PowerShell Example 1: To create a network interface with IP addresses chosen by Amazon EC2 Use the New-EC2NetworkInterface cmdlet. This example creates a network interface with a public IPv4 address and an IPv6 address chosen by Amazon EC2.
New-EC2NetworkInterface `

    -SubnetId subnet-0abcdef1234567890 `
    -Description "my dual-stack network interface" `
    -Ipv6AddresCount 1 `
    -Group sg-1234567890abcdef0 Example 2: To create a network interface with specific IP addresses Use the New-EC2NetworkInterface cmdlet.
New-EC2NetworkInterface `
    -SubnetId subnet-0abcdef1234567890 `
    -Description "my dual-stack network interface" `
    -PrivateIpAddress 10.251.50.12 `
    -Ipv6Address $ipv6addr `
    -Group sg-1234567890abcdef0 Define the IPv6 addresses as follows.
$ipv6addr = New-Object Amazon.EC2.Model.InstanceIpv6Address $ipv6addr1.Ipv6Address = "2001:db8::1234:5678:1.2.3.4"
Example 3: To create a network interface with a count of secondary IP addresses Use the New-EC2NetworkInterface cmdlet. In this example, Amazon EC2 chooses both the primary IP address and the secondary IP addresses.
New-EC2NetworkInterface `
    -SubnetId subnet-0abcdef1234567890 `
    -Description "my network interface" `
    -SecondaryPrivateIpAddressCount 2 `
    -Group sg-1234567890abcdef0 Example 4: To create a network interface with a specific secondary IP address Use the New-EC2NetworkInterface cmdlet. This example specifies a primary IP address and a secondary IP address.
New-EC2NetworkInterface `
    -SubnetId subnet-0abcdef1234567890 `
    -Description "my network interface" `
    -PrivateIpAddresses @($primary, $secondary) `

    -Group sg-1234567890abcdef0 Define the secondary addresses as follows.
$primary = New-Object Amazon.EC2.Model.PrivateIpAddressSpecification $primary.PrivateIpAddress = "10.0.1.30"
$primary.Primary = $true $secondary = New-Object Amazon.EC2.Model.PrivateIpAddressSpecification $secondary.PrivateIpAddress = "10.0.1.31"
$secondary.Primary = $false
## Network interface attachments for your EC2 instance You can create network interfaces to be used by your EC2 instances as primary or secondary network interfaces. You must attach a network interface to an EC2 instance if it is in the same Availability Zone as the network interface. The instance type of an instance determines how many network interfaces you can attach to the instance. For more information, see the section called "IP addresses per network interface".
### Considerations
- You can attach a network interface to an instance when it's running (hot attach), when it's stopped (warm attach), or when the instance is being launched (cold attach).
- You can detach secondary network interfaces when the instance is running or stopped. However, you can't detach the primary network interface.
- You can detach a secondary network interface from one instance and attach it to another instance.
- When launching an instance using the CLI, API, or an SDK, you can specify the primary network interface and additional network interfaces. Note that you can't enable the auto-assignment of public IPv4 addresses if you add a secondary network interface during launch.
- Launching an Amazon Linux or Windows Server instance with multiple network interfaces automatically configures interfaces, private IPv4 addresses, and route tables on the operating system of the instance.
- A warm or hot attach of an additional network interface might require you to manually bring up the second interface, configure the private IPv4 address, and modify the route table accordingly.
Instances running Amazon Linux or Windows Server automatically recognize the warm or hot attach and configure themselves.

- You can't attach another network interface to an instance (for example, a NIC teaming configuration) to increase or double the network bandwidth to or from the dual-homed instance.
- If you attach multiple network interfaces from the same subnet to an instance, you might encounter networking issues such as asymmetric routing. If possible, add a secondary private IPv4 address on the primary network interface instead.
- For EC2 instances in an IPv6-only subnet, if you attach a secondary network interface, the private DNS hostname of the secondary network interface resolves to the primary IPv6 address for the primary network interface.
- [Windows instances] – If you add multiple network interfaces to an instance, you must configure the network interfaces to use static routing.
### Attach a network interface You can attach a network interface to any instance in the same Availability Zone as the network interface, using either the Instances or Network Interfaces page of the Amazon EC2 console.
Alternatively, you can specify existing network interfaces when you launch instances.
If the public IPv4 address on your instance is released, it does not receive a new one if there is more than one network interface attached to the instance. For more information about the behavior of public IPv4 addresses, see Public IPv4 addresses.
Console To attach a network interface using the Instances page
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Instances.
3. Select the checkbox for the instance.
4. Choose Actions, Networking, Attach network interface.
5. Choose a VPC. The network interface can reside in the same VPC as your instance or in a different VPC that you own, as long as the network interface is in the same Availability Zone as the instance. This enables you to create multi-homed instances across VPCs with different networking and security configurations.
6. Select a network interface. If the instance supports multiple network cards, you can choose a network card.
7. Choose Attach.

To attach a network interface using the Network Interfaces page
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Network Interfaces.
3. Select the checkbox for the network interface.
4. Choose Actions, Attach.
5. Choose an instance. If the instance supports multiple network cards, you can choose a network card.
6. Choose Attach.
AWS CLI To attach a network interface Use the following attach-network-interface command. aws ec2 attach-network-interface \ --network-interface-id eni-1234567890abcdef0 \ --instance-id i-1234567890abcdef0 \ --device-index 1 PowerShell To attach a network interface Use the Add-EC2NetworkInterface cmdlet.
Add-EC2NetworkInterface `
    -NetworkInterfaceId eni-1234567890abcdef0 `
    -InstanceId i-1234567890abcdef0 `
    -DeviceIndex 1
### Detach a network interface You can detach a secondary network interface that is attached to an EC2 instance at any time, using either the Instances or Network Interfaces page of the Amazon EC2 console.
If you try to detach a network interface that is attached to a resource from another service, such as an Elastic Load Balancing load balancer, a Lambda function, a WorkSpace, or a NAT gateway, you

get an error that you do not have permission to access the resource. To find which service created the resource attached to a network interface, check the description of the network interface. If you delete the resource, then its network interface is deleted.
Console To detach a network interface using the Instances page
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Instances.
3. Select the checkbox for the instance. Check the Network interfaces section of the Networking tab to verify that the network interface is attached to an instance as a secondary network interface.
4. Choose Actions, Networking, Detach network interface.
5. Select the network interface and choose Detach.
To detach a network interface using the Network Interfaces page
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Network Interfaces.
3. Select the checkbox for the network interface. Check the Instance details section of the Details tab to verify that the network interface is attached to an instance as a secondary network interface.
4. Choose Actions, Detach.
5. When prompted for confirmation, choose Detach.
6. If the network interface fails to detach from the instance, choose Force detachment, Enable and then try again. We recommend that force detachment only as a last resort.
Forcing a detachment can prevent you from attaching a different network interface on the same index until you restart the instance. It can also prevent the instance metadata from reflecting that the network interface was detached until you restart the instance.
AWS CLI To detach a network interface Use the following detach-network-interface command.

aws ec2 detach-network-interface --attachment-id eni-attach-016c93267131892c9 PowerShell To detach a network interface Use the Dismount-EC2NetworkInterface cmdlet.
Dismount-EC2NetworkInterface -AttachmentId eni-attach-016c93267131892c9
## Manage the IP addresses for your network interface You can manage the following IP addresses for your network interfaces:
- Elastic IP addresses (one per private IPv4 address)
- IPv4 addresses
- IPv6 addresses Console To manage the IP addresses of a network interface
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Network Interfaces.
3. Select the checkbox for the network interface.
4. To manage the IPv4 and IPv6 addresses, do the following: a.
Choose Actions, Manage IP addresses. b.
Expand the network interface. c.
For IPv4 addresses, edit the IP addresses as needed. To assign an additional IPv4 address, choose Assign new IP address and then specify an IPv4 address from the subnet range or let AWS choose one for you. d.
(Dual stack or IPv6 only) For IPv6 addresses, edit the IP addresses as needed. To assign an additional IPv6 address, choose Assign new IP address and then specify an IPv6 address from the subnet range or let AWS choose one for you.

e.
To assign or unassign a public IPv4 address to a network interface, choose Auto-assign public IP. You can enable or disable this for any network interface, but it only affects the primary network interface. f.
(Dual stack or IPv6-only) For Assign primary IPv6 IP, choose Enable to assign a primary IPv6 address. The first GUA associated with the network interface is chosen as the primary IPv6 address. After you assign a primary IPv6 address, you can't change it.
This address is the primary IPv6 address until the instance is terminated or the network interface is detached. g.
Choose Save.
5. To associate an Elastic IP address, do the following: a.
Choose Actions, Associate address. b.
For Elastic IP address, select the Elastic IP address. c.
For Private IPv4 address, select the private IPv4 address to associate with the Elastic IP address. d.
(Optional) Choose Allow the Elastic IP address to be reassociated if the network interface is currently associated with another instance or network interface. e.
Choose Associate.
6. To disassociate an Elastic IP address, do the following: a.
Choose Actions, Disassociate address. b.
For Public IP address, select the Elastic IP address. c.
Choose Disassociate.
AWS CLI To manage the IPv4 addresses Use the following assign-private-ip-addresses command to assign an IPv4 address. aws ec2 assign-private-ip-addresses \ --network-interface-id eni-1234567890abcdef0 \ --private-ip-addresses 10.0.0.82 Use the following unassign-private-ip-addresses command to unassign an IPv4 address.

aws ec2 unassign-private-ip-addresses \ --network-interface-id eni-1234567890abcdef0 \ --private-ip-addresses 10.0.0.82 To manage the IPv6 addresses Use the following assign-ipv6-addresses command to assign an IPv6 address. aws ec2 assign-ipv6-addresses \ --network-interface-id eni-1234567890abcdef0 \ --ipv6-addresses 2001:db8:1234:1a00:9691:9503:25ad:1761 Use the following unassign-ipv6-addresses command to unassign an IPv6 address. aws ec2 unassign-ipv6-addresses \ --network-interface-id eni-1234567890abcdef0 \ --ipv6-addresses 2001:db8:1234:1a00:9691:9503:25ad:1761 To manage the Elastic IP address for the primary private IPv4 address Use the following associate-address command to associate an Elastic IP address with the primary private IPv4 address. aws ec2 associate-address \ --allocation-id eipalloc-0b263919b6EXAMPLE \ --network-interface-id eni-1234567890abcdef0 Use the following disassociate-address command to disassociate an Elastic IP address from the primary private IPv4 address. aws ec2 disassociate-address --association-id eipassoc-2bebb745a1EXAMPLE PowerShell To manage the IPv4 addresses Use the Register-EC2PrivateIpAddress cmdlet to assign an IPv4 address.
Register-EC2PrivateIpAddress `
    -NetworkInterfaceId eni-1234567890abcdef0 `
    -PrivateIpAddress 10.0.0.82

Use the Unregister-EC2PrivateIpAddress cmdlet to unassign an IPv4 address.
Unregister-EC2PrivateIpAddress `
    -NetworkInterfaceId eni-1234567890abcdef0 `
    -PrivateIpAddress 10.0.0.82 To manage the IPv6 addresses Use the Register-EC2Ipv6AddressList cmdlet to assign an IPv6 address.
Register-EC2Ipv6AddressList `
    -NetworkInterfaceId eni-1234567890abcdef0 `
    -Ipv6Address 2001:db8:1234:1a00:9691:9503:25ad:1761 Use the Unregister-EC2Ipv6AddressList cmdlet to unassign an IPv6 address.
Unregister-EC2Ipv6AddressList `
    -NetworkInterfaceId eni-1234567890abcdef0 `
    -Ipv6Address 2001:db8:1234:1a00:9691:9503:25ad:1761 To manage the Elastic IP address for the primary private IPv4 address Use the Register-EC2Address cmdlet to associate an Elastic IP address with the primary private IPv4 address.
Register-EC2Address `
    -NetworkInterfaceId eni-1234567890abcdef0 `
    -AllocationId eipalloc-0b263919b6EXAMPLE Use the Unregister-EC2Address cmdlet to disassociate an Elastic IP address from the primary private IPv4 address.
Unregister-EC2Address -AssociationId eipassoc-2bebb745a1EXAMPLE
## Modify network interface attributes You can change the following network interface attributes:
- Description

- Security groups
- Delete on termination
- Source/destination check
- Idle connection tracking timeout Considerations You can't change the attributes of a requester-managed network interface.
Console To modify network interface attributes
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Network Interfaces.
3. Select the checkbox for the network interface.
4. To change the description, do the following a.
Choose Actions, Change description. b.
For Description, enter a description. c.
Choose Save.
5. To change the security groups, do the following: a.
Choose Actions, Change security groups. b.
For Associated security groups, add and remove security groups as needed. The security group and network interface must be created for the same VPC. c.
Choose Save.
6. To change the termination behavior, do the following: a.
Choose Actions, Change termination behavior. b.
Select or clear Delete on termination, Enable. c.
Choose Save.
7. To change source/destination checking, do the following: a.
Choose Actions, Change source/dest check. b.
Select or clear Source/destination check, Enable.

c.
Choose Save.
8. To change idle connection tracking timeouts, do the following: a.
Choose Actions, Modify idle connection tracking timeout. b.
Modify timeout values as needed. For more information, see Idle connection tracking timeout.
- TCP established timeout: Timeout (in seconds) for idle TCP connections in an established state.
- Min: 60 seconds
- Max: 432000 seconds
- Default: 350 seconds for Nitrov6 instance types, excluding P6e-GB200. And 432000 seconds for other instance types, including P6e-GB200.
- Recommended: Less than 432000 seconds
- UDP timeout: Timeout (in seconds) for idle UDP flows that have seen traffic only in a single direction or a single request-response transaction.
- Min: 30 seconds
- Max: 60 seconds
- Default: 30 seconds
- UDP stream timeout: Timeout (in seconds) for idle UDP flows classified as streams which have seen more than one request-response transaction.
- Min: 60 seconds
- Max: 180 seconds
- Default: 180 seconds c.
Choose Save.
AWS CLI Example: To modify the description Use the following modify-network-interface-attribute command. aws ec2 modify-network-interface-attribute \ --network-interface-id eni-1234567890abcdef0 \ --description "my updated description"

Example: To modify the security groups Use the following modify-network-interface-attribute command. aws ec2 modify-network-interface-attribute \ --network-interface-id eni-1234567890abcdef0 \ --groups sg-1234567890abcdef0 Example: To modify the termination behavior Use the following modify-network-interface-attribute command. aws ec2 modify-network-interface-attribute \ --network-interface-id eni-1234567890abcdef0 \ --attachment AttachmentId=eni-attach-43348162abEXAMPLE,DeleteOnTermination=false Example: To enable source/destination checking Use the following modify-network-interface-attribute command. aws ec2 modify-network-interface-attribute \ --network-interface-id eni-1234567890abcdef0 \ --source-dest-check Example: To modify idle connection tracking timout Use the following modify-network-interface-attribute command. For more information, see Idle connection tracking timeout. aws ec2 modify-network-interface-attribute \ --network-interface-id eni-1234567890abcdef0 \ --connection-tracking-specification TcpEstablishedTimeout=172800,UdpStreamTimeout=90,UdpTimeout=60 PowerShell Example: To modify the description Use the Edit-EC2NetworkInterfaceAttribute cmdlet.
Edit-EC2NetworkInterfaceAttribute `
    -NetworkInterfaceId eni-1234567890abcdef0 `

    -Description "my updated description"
Example: To modify the security groups Use the Edit-EC2NetworkInterfaceAttribute cmdlet.
Edit-EC2NetworkInterfaceAttribute `
    -NetworkInterfaceId eni-1234567890abcdef0 `
    -Group sg-1234567890abcdef0 Example: To modify the termination behavior Use the Edit-EC2NetworkInterfaceAttribute cmdlet.
Edit-EC2NetworkInterfaceAttribute `
    -NetworkInterfaceId eni-1234567890abcdef0 `
    -Attachment_AttachmentId eni-attach-43348162abEXAMPLE `
    -Attachment_DeleteOnTermination $false Example: To enable source/destination checking Use the Edit-EC2NetworkInterfaceAttribute cmdlet.
Edit-EC2NetworkInterfaceAttribute `
    -NetworkInterfaceId eni-1234567890abcdef0 `
    -SourceDestCheck $true Example: To modify idle connection tracking timeouts Use the Edit-EC2NetworkInterfaceAttribute cmdlet. For more information, see Idle connection tracking timeout.
Edit-EC2NetworkInterfaceAttribute `
    -NetworkInterfaceId eni-1234567890abcdef0 `
    -ConnectionTrackingSpecification_TcpEstablishedTimeout 172800 `
    -ConnectionTrackingSpecification_UdpStreamTimeout 90 `
    -ConnectionTrackingSpecification_UdpTimeout 60
## Multiple network interfaces for your Amazon EC2 instances Attaching multiple network interfaces to an instance is useful when you need the following:

- A management network.
- Network and security appliances.
- Dual-homed instances with workloads in different subnets or VPCs.
- A low-budget, high-availability solution.
### Management network The following overview describes a management network created using multiple network interfaces.
Criteria
- The primary network interface on the instance (for example, eth0) handles public traffic.
- The secondary network interface on the instance (for example, eth1) handles backend management traffic. It's connected to a separate subnet that has more restrictive access controls, and is located within the same Availability Zone as the primary network interface.
Settings
- The primary network interface, which may or may not be behind a load balancer, has an associated security group that allows access to the server from the internet. For example, allow TCP port 80 and 443 from 0.0.0.0/0 or from the load balancer.
- The secondary network interface has an associated security group that allows SSH access only, initiated from one of the following locations:
- An allowed range of IP addresses, either within the VPC, or from the internet.
- A private subnet within the same Availability Zone as the primary network interface.
- A virtual private gateway.
Note To ensure failover capabilities, consider using a secondary private IPv4 for incoming traffic on a network interface. In the event of an instance failure, you can move the interface and/ or secondary private IPv4 address to a standby instance.

### Network and security appliances Some network and security appliances, such as load balancers, network address translation (NAT) servers, and proxy servers prefer to be configured with multiple network interfaces. You can create and attach secondary network interfaces to instances that are running these types of applications and configure the additional interfaces with their own public and private IP addresses, security groups, and source/destination checking.

### Dual-homed instances with workloads in different subnets You can place a network interface on each of your web servers that connects to a mid-tier network where an application server resides. The application server can also be dual-homed to a backend network (subnet) where the database server resides. Instead of routing network packets through the dual-homed instances, each dual-homed instance receives and processes requests on the front end, initiates a connection to the backend, and then sends requests to the servers on the backend network.
### Dual-homed instances with workloads in different VPCs in the same account You can launch an EC2 instance in one VPC and attach a secondary ENI from a different VPC, as long as the network interface is in the same Availability Zone as the instance. This enables you to create multi-homed instances across VPCs with different networking and security configurations.
You can't create multi-homed instances across VPCs in different AWS accounts.
You can use dual-homed instances across VPCs in the following use cases:
- Overcome CIDR overlaps between two VPCs that can't be peered together: You can leverage a secondary CIDR in a VPC and allow an instance to communicate across two non-overlapping IP ranges.
- Connect multiple VPCs within a single account: Enable communication between individual resources that would normally be separated by VPC boundaries.
### Low-budget, high-availability solution If one of your instances serving a particular function fails, its network interface can be attached to a replacement or hot standby instance pre-configured for the same role in order to rapidly recover the service. For example, you can use a network interface as your primary or secondary network interface to a critical service such as a database instance or a NAT instance. If the instance fails, you (or more likely, the code running on your behalf) can attach the network interface to a hot standby instance. Because the interface maintains its private IP addresses, Elastic IP addresses, and MAC address, network traffic begins flowing to the standby instance as soon as you attach the network interface to the replacement instance. Users experience a brief loss of connectivity between the time the instance fails and the time that the network interface is attached to the standby instance, but no changes to the route table or your DNS server are required.

Requester-managed network interfaces A requester-managed network interface is a network interface that an AWS service creates in your VPC on your behalf. The network interface is associated with a resource for another service, such as a DB instance from Amazon RDS, a NAT gateway, or an interface VPC endpoint from AWS PrivateLink.
Considerations
- You can view the requester-managed network interfaces in your account. You can add or remove tags, but you can't change other properties of a requester-managed network interface.
- You can't detach a requester-managed network interface.
- When you delete the resource associated with a requester-managed network interface, the AWS service detaches the network interface and deletes it. If the service detached a network interface but didn't delete it, you can delete the detached network interface.
Console To view requester-managed network interfaces
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Network & Security, Network Interfaces.
3. Select the ID of the network interface to open its details page.
4. The following are the key fields that you can use to determine the purpose of the network interface:
- Description: A description provided by the AWS service that created the interface. For example, "VPC Endpoint Interface vpce 089f2123488812123".
- Requester-managed: Indicates whether the network interface is managed by AWS.
- Requester ID: The alias or AWS account ID of the principal or service that created the network interface. If you created the network interface, this is your AWS account ID.
Otherwise, another principal or service created it.
AWS CLI To view requester-managed network interfaces

Use the describe-network-interfaces command as follows. aws ec2 describe-network-interfaces \ --filters "Name=requester-managed,Values=true" \ --query "NetworkInterfaces[*].[Description, InterfaceType]" \ --output table The following is example output that shows the key fields that you can use to determine the purpose of the network interface: Description and InterfaceType.
-------------------------------------------------------------------------------
|                          DescribeNetworkInterfaces                          | +---------------------------------------------------+-------------------------+
|  VPC Endpoint Interface: vpce-0f00567fa8477a1e6   |  interface              |
|  VPC Endpoint Interface vpce-0d8ddce4be80e4474    |  interface              |
|  VPC Endpoint Interface vpce-078221a1e27d1ea5b    |  vpc_endpoint           |
|  Resource Gateway Interface rgw-0bba03f3d56060135 |  interface              |
|  VPC Endpoint Interface: vpce-0cc199f605eaeace7   |  interface              |
|  VPC Endpoint Interface vpce-019b90d6f16d4f958    |  interface              | +---------------------------------------------------+-------------------------+ PowerShell To view requester-managed network interfaces Use the Get-EC2NetworkInterface cmdlet as follows.
Get-EC2NetworkInterface -Filter @{Name="requester-managed"; Values="true"} | Select Description, InterfaceType The following is example output that shows the key fields that you can use to determine the purpose of a network interface: Description and InterfaceType.
Description                                      InterfaceType -----------                                      ------------- VPC Endpoint Interface: vpce-0f00567fa8477a1e6   interface VPC Endpoint Interface vpce-0d8ddce4be80e4474    interface VPC Endpoint Interface vpce-078221a1e27d1ea5b    vpc_endpoint Resource Gateway Interface rgw-0bba03f3d56060135 interface VPC Endpoint Interface: vpce-0cc199f605eaeace7   interface VPC Endpoint Interface vpce-019b90d6f16d4f958    interface

## Prefix delegation for Amazon EC2 network interfaces You can assign a private IPv4 or IPv6 CIDR range, either automatically or manually, to your network interfaces. By assigning prefixes, you scale and simplify the management of applications, including container and networking applications that require multiple IP addresses on an instance. For more information about IPv4 and IPv6 addresses, see Amazon EC2 instance IP addressing.
The following assignment options are available:
- Automatic assignment — AWS chooses the prefix and assigns it to your network interface. If the subnet for the network interface has a subnet CIDR reservation of type prefix, we select the prefixes from the subnet CIDR reservation. Otherwise, we select them from the subnet CIDR range.
- Manual assignment — You specify the prefix and AWS verifies that it is not already assigned to other resources before assigning it to your network interface.
Assigning prefixes has the following benefits:
- Increased IP addresses on a network interface — When you use a prefix, you assign a block of IP addresses as opposed to individual IP addresses. This increases the number of IP addresses for a network interface.
- Simplified VPC management for containers — In container applications, each container requires a unique IP address. Assigning prefixes to your instance simplifies the management of your VPCs, as you can launch and terminate containers without having to call Amazon EC2 APIs for individual IP assignments.
Contents
- Basics
- Considerations
- Manage prefixes for your network interfaces
- Assign prefixes during network interface creation
- Assign prefixes to an existing network interface
- Remove prefixes from your network interfaces

### Basics
- You can assign a prefix to new or existing network interfaces.
- To use prefixes, you assign a prefix to your network interface, attach the network interface to your instance, and then configure your operating system.
- When you choose the option to specify a prefix, the prefix must meet the following requirements:
- The IPv4 prefix that you can specify is /28.
- The IPv6 prefix that you can specify is /80.
- The prefix is in the subnet CIDR of the network interface, and does not overlap with other prefixes or IP addresses assigned to existing resources in the subnet.
- You can assign a prefix to the primary or secondary network interface.
- You can assign an Elastic IP address to a network interface that has a prefix assigned to it.
- You can also assign an Elastic IP address to the IP address part of the assigned prefix.
- We resolve the private DNS host name of an instance to the primary private IPv4 address.
- We assign each private IPv4 address for a network interface, including those from prefixes, using the following format:
- us-east-1 Region ip-private-ipv4-address.ec2.internal
- All other Regions ip-private-ipv4-address.region.compute.internal Considerations Take the following into consideration when you use prefixes:
- Network interfaces with prefixes are supported with Nitro-based instances.
- Prefixes for network interfaces must use IPv6 addresses or private IPv4 addresses.
- The maximum number of IP addresses that you can assign to a network interface depends on the instance type. Each prefix that you assign to a network interface counts as one IP address.
For example, a c5.large instance has a limit of 10 IPv4 addresses per network interface. Each

network interface for this instance has a primary IPv4 address. If a network interface has no secondary IPv4 addresses, you can assign up to 9 prefixes to the network interface. For each additional IPv4 address that you assign to a network interface, you can assign one less prefix to the network interface. For more information, see Maximum IP addresses per network interface.
- Prefixes are included in source/destination checks.
- You must configure your operating system to work with network interfaces with prefixes. Note the following:
- Some Amazon Linux AMIs contain additional scripts installed by AWS, known as ec2-net- utils. These scripts optionally automate the configuration of your network interfaces. They are for use only on Amazon Linux.
- For containers, you can use a Container Network Interface (CNI) for the Kubernetes plug-in, or dockerd if you use Docker to manage your containers.
### Manage prefixes for your network interfaces When you assign prefixes to a network interface, you can choose whether to let us automatically assign the prefixes or you can specify custom prefixes. If you let us automatically assign prefixes and the subnet for the network interface has a subnet CIDR reservation of type prefix, we select the prefixes from the subnet CIDR reservation. Otherwise, we select them from the subnet CIDR range.
Tasks
- Assign prefixes during network interface creation
- Assign prefixes to an existing network interface
- Remove prefixes from your network interfaces
#### Assign prefixes during network interface creation You can assign automatic or custom prefixes when you create a network interface.
Console To assign automatic prefixes during network interface creation
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Network Interfaces.

3. Choose Create network interface.
4. Enter a description for the network interface, select the subnet in which to create the network interface, and configure the private IPv4 and IPv6 addresses.
5. Expand Advanced settings.
6. For IPv4 prefix delegation do one of the following:
- To automatically assign an IPv4 prefix, choose Auto-assign. For Number of IPv4 prefixes, enter the number of prefixes to assign.
- To assign a specific IPv4 prefix, choose Custom. Choose Add new prefix and enter the prefix.
7. For IPv6 prefix delegation do one of the following:
- To automatically assign an IPv6 prefix, choose Auto-assign. For Number of IPv6 prefixes, enter the number of prefixes to assign.
- To assign a specific IPv6 prefix, choose Custom. Choose Add new prefix and enter the prefix.
Note IPv6 prefix delegation appears only if the selected subnet is enabled for IPv6.
8. Select the security groups to associate with the network interface and assign resource tags if needed.
9. Choose Create network interface.
AWS CLI To assign automatic IPv4 prefixes during network interface creation Use the create-network-interface command and set --ipv4-prefix-count to the number of IPv4 prefixes for AWS to assign. In the following example, AWS assigns one IPv4 prefix. aws ec2 create-network-interface \ --subnet-id subnet-047cfed18eEXAMPLE \ --description "IPv4 automatic example" \ --ipv4-prefix-count 1 To assign specific IPv4 prefixes during network interface creation

Use the create-network-interface command and set --ipv4-prefixes to the prefixes.
AWS selects IPv4 addresses from this range. In the following example, the prefix CIDR is 10.0.0.208/28. aws ec2 create-network-interface \ --subnet-id subnet-047cfed18eEXAMPLE \ --description "IPv4 manual example" \ --ipv4-prefixes Ipv4Prefix=10.0.0.208/28 To assign automatic IPv6 prefixes during network interface creation Use the create-network-interface command and set --ipv6-prefix-count to the number of IPv6 prefixes for AWS to assign. In the following example, AWS assigns one IPv6 prefix. aws ec2 create-network-interface \ --subnet-id subnet-047cfed18eEXAMPLE \ --description "IPv6 automatic example" \ --ipv6-prefix-count 1 To assign specific IPv6 prefixes during network interface creation Use the create-network-interface command and set --ipv6-prefixes to the prefixes.
AWS selects IPv6 addresses from this range. In the following example, the prefix CIDR is 2600:1f13:fc2:a700:1768::/80. aws ec2 create-network-interface \ --subnet-id subnet-047cfed18eEXAMPLE \ --description "IPv6 manual example" \ --ipv6-prefixes Ipv6Prefix=2600:1f13:fc2:a700:1768::/80 PowerShell To assign automatic IPv4 prefixes during network interface creation Use the New-EC2NetworkInterface cmdlet and set Ipv4PrefixCount to the number of IPv4 prefixes for AWS to assign. In the following example, AWS assigns one IPv4 prefix.
New-EC2NetworkInterface `
    -SubnetId 'subnet-047cfed18eEXAMPLE' `
    -Description 'IPv4 automatic example' `
    -Ipv4PrefixCount 1

To assign specific IPv4 prefixes during network interface creation Use the New-EC2NetworkInterface cmdlet and set Ipv4Prefix to the prefixes. AWS selects IPv4 addresses from this range. In the following example, the prefix CIDR is 10.0.0.208/28.
Import-Module AWS.Tools.EC2 New-EC2NetworkInterface `
    -SubnetId 'subnet-047cfed18eEXAMPLE' `
    -Description 'IPv4 manual example' `
    -Ipv4Prefix (New-Object `
        -TypeName Amazon.EC2.Model.Ipv4PrefixSpecificationRequest `
        -Property @{Ipv4Prefix = '10.0.0.208/28'})
To assign automatic IPv6 prefixes during network interface creation Use the New-EC2NetworkInterface cmdlet and set Ipv6PrefixCount to the number of IPv6 prefixes for AWS to assign. In the following example, AWS assigns one IPv6 prefix.
New-EC2NetworkInterface `
    -SubnetId 'subnet-047cfed18eEXAMPLE' `
    -Description 'IPv6 automatic example' `
    -Ipv6PrefixCount 1 To assign specific IPv6 prefixes during network interface creation Use the New-EC2NetworkInterface cmdlet and set Ipv6Prefixes to the prefixes. AWS selects IPv6 addresses from this range. In the following example, the prefix CIDR is 2600:1f13:fc2:a700:1768::/80.
Import-Module AWS.Tools.EC2 New-EC2NetworkInterface `
    -SubnetId 'subnet-047cfed18eEXAMPLE' `
    -Description 'IPv6 manual example' `
    -Ipv6Prefix (New-Object `
        -TypeName Amazon.EC2.Model.Ipv6PrefixSpecificationRequest `
        -Property @{Ipv6Prefix = '2600:1f13:fc2:a700:1768::/80'})
#### Assign prefixes to an existing network interface You can assign automatic or custom prefixes to an existing network interface.

Console To assign automatic prefixes to an existing network interface
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Network Interfaces.
3. Select the network interface to which to assign the prefixes, and choose Actions, Manage prefixes.
4. For IPv4 prefix delegation do one of the following:
- To automatically assign an IPv4 prefix, choose Auto-assign. For Number of IPv4 prefixes, enter the number of prefixes to assign.
- To assign a specific IPv4 prefix, choose Custom. Choose Add new prefix and enter the prefix.
5. For IPv6 prefix delegation do one of the following:
- To automatically assign an IPv6 prefix, choose Auto-assign. For Number of IPv6 prefixes, enter the number of prefixes to assign.
- To assign a specific IPv6 prefix, choose Custom. Choose Add new prefix and enter the prefix.
Note IPv6 prefix delegation appears only if the selected subnet is enabled for IPv6.
6. Choose Save.
AWS CLI Use the assign-ipv6-addresses command to assign IPv6 prefixes and the assign-private-ip- addresses command to assign IPv4 prefixes to existing network interfaces.
To assign automatic IPv4 prefixes to an existing network interface Use the assign-private-ip-addresses command and set --ipv4-prefix-count to the number of IPv4 prefixes for AWS to assign. In the following example, AWS assigns one IPv4 prefix. aws ec2 assign-private-ip-addresses \ --network-interface-id eni-081fbb4095EXAMPLE \

    --ipv4-prefix-count 1 To assign specific IPv4 prefixes to an existing network interface Use the assign-private-ip-addresses command and set --ipv4-prefixes to the prefix.
AWS selects IPv4 addresses from this range. In the following example, the prefix CIDR is 10.0.0.208/28. aws ec2 assign-private-ip-addresses \ --network-interface-id eni-081fbb4095EXAMPLE \ --ipv4-prefixes 10.0.0.208/28 To assign automatic IPv6 prefixes to an existing network interface Use the assign-ipv6-addresses command and set --ipv6-prefix-count to the number of IPv6 prefixes for AWS to assign. In the following example, AWS assigns one IPv6 prefix. aws ec2 assign-ipv6-addresses \ --network-interface-id eni-00d577338cEXAMPLE \ --ipv6-prefix-count 1 To assign specific IPv6 prefixes to an existing network interface Use the assign-ipv6-addresses command and set --ipv6-prefixes to the prefix.
AWS selects IPv6 addresses from this range. In the following example, the prefix CIDR is 2600:1f13:fc2:a700:18bb::/80. aws ec2 assign-ipv6-addresses \ --network-interface-id eni-00d577338cEXAMPLE \ --ipv6-prefixes 2600:1f13:fc2:a700:18bb::/80 PowerShell To assign automatic IPv4 prefixes to an existing network interface Use the Register-EC2PrivateIpAddress cmdlet and set Ipv4PrefixCount to the number of IPv4 prefixes for AWS to assign. In the following example, AWS assigns one IPv4 prefix.
Register-EC2PrivateIpAddress `
    -NetworkInterfaceId 'eni-00d577338cEXAMPLE' `

    -Ipv4PrefixCount 1 To assign specific IPv4 prefixes to an existing network interface Use the Register-EC2PrivateIpAddress cmdlet and set Ipv4Prefix to the prefix. AWS selects IPv4 addresses from this range. In the following example, the prefix CIDR is 10.0.0.208/28.
Register-EC2PrivateIpAddress `
    -NetworkInterfaceId 'eni-00d577338cEXAMPLE' `
    -Ipv4Prefix '10.0.0.208/28'
To assign automatic IPv6 prefixes to an existing network interface Use the Register-EC2Ipv6AddressList cmdlet and set Ipv6PrefixCount to the number of IPv4 prefixes for AWS to assign. In the following example, AWS assigns one IPv6 prefix.
Register-EC2Ipv6AddressList `
    -NetworkInterfaceId 'eni-00d577338cEXAMPLE' `
    -Ipv6PrefixCount 1 To assign specific IPv6 prefixes to an existing network interface Use the Register-EC2Ipv6AddressList cmdlet and set Ipv6Prefix to the prefix. AWS selects IPv6 addresses from this range. In the following example, the prefix CIDR is 2600:1f13:fc2:a700:18bb::/80.
Register-EC2Ipv6AddressList `
    -NetworkInterfaceId 'eni-00d577338cEXAMPLE' `
    -Ipv6Prefix '2600:1f13:fc2:a700:18bb::/80'
#### Remove prefixes from your network interfaces You can remove prefixes from an existing network interface.
Console To remove the prefixes from a network interface
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Network Interfaces.

3. Select the network interface.
4. Choose Actions, Manage prefixes.
5. For IPv4 prefix delegation, to remove specific prefixes, choose Unassign next to the prefixes to remove. To remove all prefixes, choose Do not assign.
6. For IPv6 prefix delegation, to remove specific prefixes, choose Unassign next to the prefixes to remove. To remove all prefixes, choose Do not assign.
Note IPv6 prefix delegation appears only if the selected subnet is enabled for IPv6.
7. Choose Save.
AWS CLI You can use the unassign-ipv6-addresses command to remove IPv6 prefixes and the unassign- private-ip-addresses commands to remove IPv4 prefixes from your existing network interfaces.
To remove IPv4 prefixes from a network interface Use the unassign-private-ip-addresses command and set --ipv4-prefix to the prefix CIDR to remove. aws ec2 unassign-private-ip-addresses \ --network-interface-id eni-081fbb4095EXAMPLE \ --ipv4-prefixes 10.0.0.176/28 To remove IPv6 prefixes from a network interface Use the unassign-ipv6-addresses command and set --ipv6-prefix to the prefix CIDR to remove. aws ec2 unassign-ipv6-addresses \ --network-interface-id eni-00d577338cEXAMPLE \ --ipv6-prefix 2600:1f13:fc2:a700:18bb::/80 PowerShell To remove IPv4 prefixes from a network interface

Use the Unregister-EC2PrivateIpAddress cmdlet and set Ipv4Prefix to the prefix CIDR to remove.
Unregister-EC2PrivateIpAddress `
    -NetworkInterfaceId 'eni-00d577338cEXAMPLE' `
    -Ipv4Prefix '10.0.0.208/28'
To remove IPv6 prefixes from a network interface Use the Unregister-EC2Ipv6AddressList cmdlet and set Ipv6Prefix to the prefix CIDR to remove.
Unregister-EC2Ipv6AddressList `
    -NetworkInterfaceId 'eni-00d577338cEXAMPLE' `
    -Ipv6Prefix '2600:1f13:fc2:a700:18bb::/80'
## Delete a network interface Deleting a network interface releases all attributes associated with the interface and releases any private IP addresses or Elastic IP addresses to be used by another instance.
You can't delete a network interface that is in use. First, you must detach the network interface.
Console To delete a network interface
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Network Interfaces.
3. Select the checkbox for the network interface, and then choose Actions, Delete.
4. When prompted for confirmation, choose Delete.
AWS CLI To delete a network interface Use the following delete-network-interface command. aws ec2 delete-network-interface --network-interface-id eni-1234567890abcdef0
