# Network maximum transmission unit (MTU) for your EC2 instance

Source: apps/user-manuals/aws/ec2-ug.pdf

---

Considerations
- A rack level spread placement group can hold as many instances as you have racks in your Outpost deployment.
- A host level spread placement group can hold as many instances as you have hosts in your Outpost deployment.
Prerequisite You must have an Outpost installed at your site. For more information, see Create an Outpost and order Outpost capacity in the AWS Outposts User Guide.
To use a placement group on an Outpost
1. Create a subnet on the Outpost. For more information, see Create a subnet in the AWS Outposts User Guide.
2. Create a placement group in the associated Region of the Outpost. If you create a placement group with a spread strategy, you can choose host or rack level spread to determine how the group will spread instances across the underlying hardware on your Outpost. For more information, see the section called "Create a placement group".
3. Launch an instance into the placement group. For Subnet choose the subnet that you created in Step 1, and for Placement group name, select the placement group that you created in Step 2. For more information, see Launch an instance on the Outpost in the AWS Outposts User Guide.
# Network maximum transmission unit (MTU) for your EC2 instance instance The maximum transmission unit (MTU) of a network connection is the size, in bytes, of the largest permissible packet that can be passed over the connection. The larger the MTU of a connection, the more data that can be passed in a single packet. Ethernet frames consist of the packet, or the actual data you are sending, and the network overhead information that surrounds it.
Ethernet frames can come in different formats, and the most common format is the standard Ethernet v2 frame format. It supports 1500 MTU, which is the largest Ethernet packet size supported over most of the internet. The maximum supported MTU for an instance depends on its instance type.

All EC2 instance types support 1500 MTU.
Contents
- Jumbo frames (9001 MTU)
- Path MTU Discovery
- Set the MTU for your Amazon EC2 instances
- Troubleshoot
## Jumbo frames (9001 MTU)
With jumbo frames, you can increase the payload size per packet, thereby increasing the percentage of the packet that is not packet overhead. With jumbo frames, fewer packets are needed to send the same amount of usable data. However, certain types of traffic are subject to the following maximum payloads:
MTU limit 1500 bytes
- Traffic over an internet gateway
- Traffic over VPN connections
- Traffic between AWS Regions, unless a transit gateway is used MTU limit 8500 bytes
- Traffic over an inter-region VPC peering connection If packets are over their MTU limit, they are fragmented, or they are dropped if the Don't Fragment flag is set in the IP header.
Jumbo frames should be used with caution for internet-bound traffic or any traffic that leaves a VPC. Packets are fragmented by intermediate systems, which slows down this traffic. To use jumbo frames inside a VPC and not slow traffic that's bound for outside the VPC, you can configure the MTU size by route, or use multiple elastic network interfaces with different MTU sizes and different routes.
For instances that are collocated inside a cluster placement group, jumbo frames help to achieve the maximum network throughput possible, and they are recommended in this case. For more information, see Placement groups for your Amazon EC2 instances.

You can use jumbo frames for traffic between your VPCs and your on-premises networks over Direct Connect. For more information, and for how to verify Jumbo Frame capability, see MTU for private virtual interfaces or transit virtual interfaces in the Direct Connect User Guide.
All current generation instance types support jumbo frames. The following previous generation instance types support jumbo frames: A1, C3, I2, M3, and R3.
Related resources
- For NAT gateways, see NAT gateway basics  in the Amazon VPC User Guide.
- For transit gateways, see Maximum transmission unit in the Amazon VPC Transit Gateways User Guide.
- For Local Zones, see Considerations in the AWS Local Zones User Guide.
- For AWS Wavelength, see Maximum transmission unit in the AWS Wavelength User Guide.
- For Outposts see Service link maximum transmission unit requirements in the AWS Outposts User Guide.
## Path MTU Discovery Path MTU Discovery (PMTUD) is used to determine the path MTU between two devices. The path MTU is the maximum packet size that's supported on the path between the originating host and the receiving host. When there is a difference in the MTU size in the network between two hosts, PMTUD enables the receiving host to respond to the originating host with an ICMP message. This ICMP message instructs the originating host to use the lowest MTU size along the network path and to resend the request. Without this negotiation, packet drop can occur because the request is too large for the receiving host to accept.
For IPv4, when a host sends a packet that's larger than the MTU of the receiving host or that's larger than the MTU of a device along the path, the receiving host or device drops the packet, and then returns the following ICMP message: Destination Unreachable: Fragmentation Needed and Don't Fragment was Set (Type 3, Code 4). This instructs the transmitting host to split the payload into multiple smaller packets, and then retransmit them.
The IPv6 protocol does not support fragmentation in the network. When a host sends a packet that's larger than the MTU of the receiving host or that's larger than the MTU of a device along the path, the receiving host or device drops the packet, and then returns the following ICMP message:
ICMPv6 Packet Too Big (PTB) (Type 2). This instructs the transmitting host to split the payload into multiple smaller packets, and then retransmit them.

Connections made through some components, like NAT gateways and load balancers, are automatically tracked. This means that security group tracking is automatically enabled for your outbound connection attempts. If connections are automatically tracked or if your security group rules allow inbound ICMP traffic, you can receive PMTUD responses.
Note that ICMP traffic can be blocked even if the traffic is allowed at the security group level, such as if you have a network access control list entry that denies ICMP traffic to the subnet.
Important Path MTU Discovery does not guarantee that jumbo frames will not be dropped by some routers. An internet gateway in your VPC will forward packets up to 1500 bytes only. 1500 MTU packets are recommended for internet traffic.
For MTU rules over NAT gateways, see Maximum transmission unit (MTU) in the Amazon VPC User Guide. For MTU rules over Transit gateways, see Maximum transmission unit (MTU) in the AWS Transit Gateway User Guide.
## Set the MTU for your Amazon EC2 instances The maximum transmission unit (MTU) of a network connection is the size, in bytes, of the largest permissible packet that can be passed over the connection. All Amazon EC2 instances support standard frames (1500 MTU) and all current generation instance types support jumbo frames (9001 MTU).
You can view the MTU for your Amazon EC2 instances, view the path MTU between your instance and another host, and configure your instances to use either standard or jumbo frames.
Tasks
- Check the path MTU between two hosts
- Check the MTU for your instance
- Set the MTU for your instance

### Check the path MTU between two hosts You can check the path MTU between your EC2 instance and another host. You can specify a DNS name or an IP address as the destination. If the destination is another EC2 instance, verify that its security group allows inbound UDP traffic.
The procedure that you use depends on the operating system of the instance.
#### Linux instances Run the tracepath command on your instance to check the path MTU between your EC2 instance and the specified destination. This command is part of the iputils package, which is available by default in many Linux distributions.
This example checks the path MTU between the EC2 instance and amazon.com.
[ec2-user ~]$ tracepath amazon.com In this example output, the path MTU is 1500.
 1?: [LOCALHOST]     pmtu 9001 1:  ip-172-31-16-1.us-west-1.compute.internal (172.31.16.1)   0.187ms pmtu 1500 1:  no reply 2:  no reply 3:  no reply 4:  100.64.16.241 (100.64.16.241)                          0.574ms 5:  72.21.222.221 (72.21.222.221)                         84.447ms asymm 21 6:  205.251.229.97 (205.251.229.97)                       79.970ms asymm 19 7:  72.21.222.194 (72.21.222.194)                         96.546ms asymm 16 8:  72.21.222.239 (72.21.222.239)                         79.244ms asymm 15 9:  205.251.225.73 (205.251.225.73)                       91.867ms asymm 16 ...
31:  no reply Too many hops: pmtu 1500 Resume: pmtu 1500
#### Windows instances To check path MTU using mturoute
1. Download mturoute.exe to your EC2 instance from https://elifulkerson.com/projects/ mturoute.php.

2. Open a Command Prompt window and change to the directory where you downloaded mturoute.exe.
3. Use the following command to check the path MTU between your EC2 instance and the specified destination. This example checks the path MTU between the EC2 instance and www.elifulkerson.com.
.\mturoute.exe www.elifulkerson.com In this example output, the path MTU is 1500.
* ICMP Fragmentation is not permitted. *
* Speed optimization is enabled. *
* Maximum payload is 10000 bytes. *
+ ICMP payload of 1472 bytes succeeded.
- ICMP payload of 1473 bytes is too big.
Path MTU: 1500 bytes.
### Check the MTU for your instance You can check the MTU value for your instance. Some instances are configured to use jumbo frames, and others are configured to use standard frame sizes.
The procedure that you use depends on the operating system of the instance.
#### Linux instances To check the MTU setting on a Linux instance Run the following ip command on your EC2 instance. If the primary network interface is not eth0, replace eth0 with your network interface.
[ec2-user ~]$ ip link show eth0 In this example output, mtu 9001 indicates that the instance uses jumbo frames.
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 9001 qdisc pfifo_fast state UP mode DEFAULT group default qlen 1000 link/ether 02:90:c0:b7:9e:d1 brd ff:ff:ff:ff:ff:ff

#### Windows instances The procedure that you use depends on the driver on your instance.
ENA driver Version 2.1.0 and later To get the MTU value, use the following Get-NetAdapterAdvancedProperty command on your EC2 instance. Use the wildcard (asterisk) to get all Ethernet names. Check the output for the interface name *JumboPacket. A value of 9015 indicates that Jumbo frames are enabled.
Jumbo frames are disabled by default.
Get-NetAdapterAdvancedProperty -Name "Ethernet*"
Version 1.5 and earlier To get the MTU value, use the following Get-NetAdapterAdvancedProperty command on your EC2 instance. Check the output for the interface name MTU. A value of 9001 indicates that Jumbo frames are enabled. Jumbo frames are disabled by default.
Get-NetAdapterAdvancedProperty -Name "Ethernet"
Intel SRIOV 82599 driver To get the MTU value, use the following Get-NetAdapterAdvancedProperty command on your EC2 instance. Check the entry for the interface name *JumboPacket. A value of 9014 indicates that Jumbo frames are enabled. (Note that the MTU size includes the header and the payload.)
Jumbo frames are disabled by default.
Get-NetAdapterAdvancedProperty -Name "Ethernet"
AWS PV driver To get the MTU value, use the following command on your EC2 instance. The name of the interface can vary. In the output, look for an entry with the name "Ethernet," "Ethernet 2," or "Local Area Connection". You'll need the interface name to enable or disable jumbo frames. A value of 9001 indicates that Jumbo frames are enabled. netsh interface ipv4 show subinterface

### Set the MTU for your instance You might want to use jumbo frames for network traffic within your VPC and standard frames for internet traffic. Whatever your use case, we recommend that you verify that your instance behaves as expected.
The procedure that you use depends on the operating system of the instance.
#### Linux instances To set the MTU value on a Linux instance
1. Run the following ip command on your instance. It sets the desired MTU value to 1500, but you could use 9001 instead. If the primary network interface is not eth0, replace eth0 with the actual network interface.
[ec2-user ~]$ sudo ip link set dev eth0 mtu 1500
2. (Optional) To persist your network MTU setting after a reboot, modify the following configuration files, based on your operating system type.
- Amazon Linux 2023 – Modify the [Link] section of the config file. The default config file is /usr/lib/systemd/network/80-ec2.network, or you can update any custom config file created in /run/systemd/network/, where the file name is priority-interface.network. For more information, see Networking service in the Amazon Linux documentation.
MTUBytes=1500
- Amazon Linux 2 – Add the following line to the /etc/sysconfig/network-scripts/ ifcfg-eth0 file:
MTU=1500 Add the following line to the /etc/dhcp/dhclient.conf file: request subnet-mask, broadcast-address, time-offset, routers, domain-name, domain-search, domain-name-servers, host-name, nis-domain, nis-servers, ntp- servers;

- Other Linux distributions – Consult their specific documentation.
3. (Optional) Reboot your instance and verify that the MTU setting is correct.
#### Windows instances The procedure that you use depends on the driver on your instance.
ENA driver You can change the MTU using Device Manager or the Set-NetAdapterAdvancedProperty command on your instance.
Version 2.1.0 and later Use the following command to enable jumbo frames.
Set-NetAdapterAdvancedProperty -Name "Ethernet" -RegistryKeyword "*JumboPacket" - RegistryValue 9015 Use the following command to disable jumbo frames.
Set-NetAdapterAdvancedProperty -Name "Ethernet" -RegistryKeyword "*JumboPacket" - RegistryValue 1514 Version 1.5 and earlier Use the following command to enable jumbo frames.
Set-NetAdapterAdvancedProperty -Name "Ethernet" -RegistryKeyword "MTU" - RegistryValue 9001 Use the following command to disable jumbo frames.
Set-NetAdapterAdvancedProperty -Name "Ethernet" -RegistryKeyword "MTU" - RegistryValue 1500 Intel SRIOV 82599 driver You can change the MTU using Device Manager or the Set-NetAdapterAdvancedProperty command on your instance.
