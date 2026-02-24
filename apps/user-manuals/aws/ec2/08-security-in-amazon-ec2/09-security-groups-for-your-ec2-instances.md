# Amazon EC2 security groups for your EC2 instances

Source: apps/user-manuals/aws/ec2-ug.pdf

---

openssl pkcs8 -in path_to_private_key -inform PEM -outform DER -topk8 -nocrypt | openssl sha1 -c (Linux instances) For ED25519 key pairs: ssh-keygen -l -f path_to_private_key
- (RSA key pairs only) If you imported the public key to Amazon EC2 You can follow this procedure regardless of how you created the key pair, for example, by using a third-party tool or by generating a new public key from an existing private key created using Amazon EC2 Use the OpenSSL tools to generate the fingerprint as shown in the following example. openssl rsa -in path_to_private_key -pubout -outform DER | openssl md5 -c
- If you created an OpenSSH key pair using OpenSSH 7.8 or later and imported the public key to Amazon EC2 Use ssh-keygen to generate the fingerprint as shown in the following examples.
For RSA key pairs: ssh-keygen -ef path_to_private_key -m PEM | openssl rsa -RSAPublicKey_in -outform DER
 | openssl md5 -c (Linux instances) For ED25519 key pairs: ssh-keygen -l -f path_to_private_key
# Amazon EC2 security groups for your EC2 instances A security group acts as a virtual firewall for your EC2 instances to control incoming and outgoing traffic. Inbound rules control the incoming traffic to your instance, and outbound rules control the outgoing traffic from your instance. When you launch an instance, you can specify one or more security groups. If you don't specify a security group, Amazon EC2 uses the default security group for the VPC. After you launch an instance, you can change its security groups.

Security is a shared responsibility between AWS and you. For more information, see Security in Amazon EC2. AWS provides security groups as one of the tools for securing your instances, and you need to configure them to meet your security needs. If you have requirements that aren't fully met by security groups, you can maintain your own firewall on any of your instances in addition to using security groups.
Pricing There is no additional charge for using security groups.
Contents
- Overview
- Create a security group for your Amazon EC2 instance
- Change the security groups for your Amazon EC2 instance
- Delete an Amazon EC2 security group
- Amazon EC2 security group connection tracking
- Security group rules for different use cases
## Overview You can associate each instance with multiple security groups, and you can associate each security group with multiple instances. You add rules to each security group that allow traffic to or from its associated instances. You can modify the rules for a security group at any time. New and modified rules are automatically applied to all instances that are associated with the security group. When Amazon EC2 decides whether to allow traffic to reach an instance, it evaluates all rules from all security groups that are associated with the instance. For more information, see Security group rules in the Amazon VPC User Guide.
The following diagram shows a VPC with a subnet, an internet gateway, and a security group.
The subnet contains EC2 instances. The security group is associated with the instances. The only traffic that reaches the instance is the traffic allowed by the security group rules. For example, if the security group contains a rule that allows SSH traffic from your network, then you can connect to your instance from your computer using SSH. If the security group contains a rule that allows all traffic from the resources associated with it, then each instance can receive any traffic sent from the other instances.

Security groups are stateful—if you send a request from your instance, the response traffic for that request is allowed to flow in regardless of inbound security group rules. Also, responses to allowed inbound traffic are allowed to flow out, regardless of outbound rules. For more information, see Connection tracking.
## Create a security group for your Amazon EC2 instance Security groups act as a firewall for associated instances, controlling both inbound and outbound traffic at the instance level. You can add rules to a security group that enable you to connect to your instance using SSH (Linux instances) or RDP (Windows instances). You can also add rules that allow client traffic, for example, HTTP and HTTPS traffic destined to a web server.
You can associate a security group with an instance when you launch the instance. When you add or remove rules from associated security groups, those changes are automatically applied to all instances to which you've associated the security group.
After you launch an instance, you can associate additional security groups. For more information, see Change the security groups for your Amazon EC2 instance.
You can add inbound and outbound security group rules when you create a security group or you can add them later on. For more information, see Configure security group rules. For examples of rules that you can add to a security group, see Security group rules for different use cases.

Considerations
- New security groups start with only an outbound rule that allows all traffic to leave the resource.
You must add rules to enable any inbound traffic or to restrict the outbound traffic.
- When configuring a source for a rule that allows SSH or RDP access to your instances, do not allow access from anywhere, because it would allow this access to your instance from all IP addresses on the internet. This is acceptable for a short time in a test environment, but it is unsafe for production environments.
- If there is more than one rule for a specific port, Amazon EC2 applies the most permissive rule. For example, if you have a rule that allows access to TCP port 22 (SSH) from IP address 203.0.113.1, and another rule that allows access to TCP port 22 from anywhere, then everyone has access to TCP port 22.
- You can associate multiple security groups with an instance. Therefore, an instance can have hundreds of rules that apply. This might cause problems when you access the instance. We recommend that you condense your rules as much as possible.
- When you specify a security group as the source or destination for a rule, the rule affects all instances that are associated with the security group. Incoming traffic is allowed based on the private IP addresses of the instances that are associated with the source security group (and not the public IP or Elastic IP addresses). For more information about IP addresses, see Amazon EC2 instance IP addressing.
- Amazon EC2 blocks traffic on port 25 by default. For more information, see Restriction on email sent using port 25.
Console To create a security group
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Security Groups.
3. Choose Create security group.
4. Enter a descriptive name and brief description for the security group. You can't change the name and description of a security group after it is created.
5. For VPC, choose the VPC in which you'll run your Amazon EC2 instances.

6. (Optional) To add inbound rules, choose Inbound rules. For each rule, choose Add rule and specify the protocol, port, and source. For example, to allow SSH traffic, choose SSH for Type and specify the public IPv4 address of your computer or network for Source.
7. (Optional) To add outbound rules, choose Outbound rules. For each rule, choose Add rule and specify the protocol, port, and destination. Otherwise, you can keep the default rule, which allows all outbound traffic.
8. (Optional) To add a tag, choose Add new tag and enter the tag key and value.
9. Choose Create security group.
AWS CLI To create a security group Use the following create-security-group command. aws ec2 create-security-group \ --group-name my-security-group \ --description "my security group" \ --vpc-id vpc-1234567890abcdef0 For examples that add rules, see the section called "Configure security group rules".
PowerShell To create a security group Use the New-EC2SecurityGroup cmdlet.
New-EC2SecurityGroup `
    -GroupName my-security-group `
    -Description "my security group" `
    -VpcId vpc-1234567890abcdef0 For examples that add rules, see the section called "Configure security group rules".
## Change the security groups for your Amazon EC2 instance You can specify security groups for your Amazon EC2 instances when you launch them. After you launch an instance, you can add or remove security groups. You can also add, remove, or edit security group rules for associated security groups at any time.

Security groups are associated with network interfaces. Adding or removing security groups changes the security groups associated with the primary network interface. You can also change the security groups associated with any secondary network interfaces. For more information, see Modify network interface attributes.
Tasks
- Add or remove security groups
- Configure security group rules
### Add or remove security groups After you launch an instance, you can add or remove security groups from the list of associated security groups. When you associate multiple security groups with an instance, the rules from each security group are effectively aggregated to create one set of rules. Amazon EC2 uses this set of rules to determine whether to allow traffic.
Requirements
- The instance must be in the running or stopped state.
Console To change the security groups for an instance
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Instances.
3. Select your instance, and then choose Actions, Security, Change security groups.
4. For Associated security groups, select a security group from the list and choose Add security group.
To remove an already associated security group, choose Remove for that security group.
5. Choose Save.
AWS CLI To change the security groups for an instance Use the following modify-instance-attribute command.

aws ec2 modify-instance-attribute \ --instance-id i-1234567890abcdef0 \ --groups sg-1234567890abcdef0 PowerShell To change the security groups for an instance Use the Edit-EC2InstanceAttribute cmdlet.
Edit-EC2InstanceAttribute `
    -InstanceId i-1234567890abcdef0 `
    -Group sg-1234567890abcdef0
### Configure security group rules After you create a security group, you can add, update, and delete its security group rules. When you add, update, or delete a rule, the change is automatically applied to the resources that are associated with the security group.
For examples of rules that you can add to a security group, see Security group rules for different use cases.
Required permissions Before you begin, ensure that you have the required permissions. For more information, see Example: Work with security groups.
Protocols and ports
- With the console, when you select a predefined type, Protocol and Port range are specified for you. To enter a port range, you must select one of the following custom types: Custom TCP or Custom UDP.
- With the AWS CLI, you can add a single rule with a single port using the --protocol and -- port options. To add multiple rules, or a rule with a port range, use the --ip-permissions option instead.

Sources and destinations
- With the console, you can specify the following as sources for inbound rules or destinations for outbound rules:
- Custom – An IPv4 CIDR block, an IPv6 CIDR block, a security group, or a prefix list.
- Anywhere-IPv4 – The 0.0.0.0/0 IPv4 CIDR block.
- Anywhere-IPv6 – The ::/0 IPv6 CIDR block.
- My IP – The public IPv4 address of your local computer.
- With the AWS CLI, you can specify an IPv4 CIDR block using the --cidr option or a security group using the --source-group option. To specify a prefix list or an IPv6 CIDR block, use the --ip-permissions option.
Warning If you add inbound rules for ports 22 (SSH) or 3389 (RDP), we strongly recommend that you authorize only the specific IP address or range of addresses that need access to your instances. If you choose Anywhere-IPv4, you allow traffic from all IPv4 addresses to access your instances using the specified protocol. If you choose Anywhere-IPv6, you allow traffic from all IPv6 addresses to access your instances using the specified protocol.
Console To configure security group rules
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Security Groups.
3. Select the security group.
4. To edit the inbound rules, choose Edit inbound rules from Actions or the Inbound rules tab. a.
To add a rule, choose Add rule and enter the type, protocol, port, and source for the rule.
If the type is TCP or UDP, you must enter the port range to allow. For custom ICMP, you must choose the ICMP type name from Protocol, and, if applicable, the code name

from Port range. For any other type, the protocol and port range are configured for you. b.
To update a rule, change its protocol, description, and source as needed. However, you can't change the source type. For example, if the source is an IPv4 CIDR block, you can't specify an IPv6 CIDR block, a prefix list, or a security group. c.
To delete a rule, choose its Delete button.
5. To edit the outbound rules, choose Edit outbound rules from Actions or the Outbound rules tab. a.
To add a rule, choose Add rule and enter the type, protocol, port, and destination for the rule. You can also enter an optional description.
If the type is TCP or UDP, you must enter the port range to allow. For custom ICMP, you must choose the ICMP type name from Protocol, and, if applicable, the code name from Port range. For any other type, the protocol and port range are configured for you. b.
To update a rule, change its protocol, description, and source as needed. However, you can't change the source type. For example, if the source is an IPv4 CIDR block, you can't specify an IPv6 CIDR block, a prefix list, or a security group. c.
To delete a rule, choose its Delete button.
6. Choose Save rules.
AWS CLI To add security group rules Use the authorize-security-group-ingress command to add inbound rules. The following example allows inbound SSH traffic from the CIDR blocks in the specified prefix list. aws ec2 authorize-security-group-ingress \ --group-id sg-1234567890abcdef0 \ --ip-permissions 'IpProtocol=tcp,FromPort=22,ToPort=22,PrefixListIds=[{PrefixListId=pl- f8a6439156EXAMPLE}]'
Use the authorize-security-group-egress command to add outbound rules. The following example allows outbound TCP traffic on port 80 to instances with the specified security group.

aws ec2 authorize-security-group-egress \ --group-id sg-1234567890abcdef0 \ --ip-permissions 'IpProtocol=tcp,FromPort=80,ToPort=80,UserIdGroupPairs=[{GroupId=sg-0aad1c26bb6EXAMPLE}]'
To remove security group rules Use the following revoke-security-group-ingress command to remove an inbound rule. aws ec2 revoke-security-group-egress \ --group id sg-1234567890abcdef0 \ --security-group-rule-ids sgr-09ed298024EXAMPLE Use the following revoke-security-group-egress command to remove an outbound rule. aws ec2 revoke-security-group-ingress \ --group id sg-1234567890abcdef0 \ --security-group-rule-ids sgr-0352250c1aEXAMPLE To modify security group rules Use the modify-security-group-rules command. The following example changes the IPv4 CIDR block of the specified security group rule. aws ec2 modify-security-group-rules \ --group id sg-1234567890abcdef0 \ --security-group-rules 'SecurityGroupRuleId=sgr-09ed298024EXAMPLE,SecurityGroupRule={IpProtocol=tcp,FromPort=80,To PowerShell To add security group rules Use the Grant-EC2SecurityGroupIngress cmdlet to add inbound rules. The following example allows inbound SSH traffic from the CIDR blocks in the specified prefix list.
$plid = New-Object -TypeName Amazon.EC2.Model.PrefixListId $plid.Id = "pl-f8a6439156EXAMPLE"
Grant-EC2SecurityGroupIngress `
    -GroupId sg-1234567890abcdef0 `

    -IpPermission @{IpProtocol="tcp"; FromPort=22; ToPort=22; PrefixListIds=$plid} Use the Grant-EC2SecurityGroupEgress cmdlet to add outbound rules. The following example allows outbound TCP traffic on port 80 to instances with the specified security group.
$uigp = New-Object -TypeName Amazon.EC2.Model.UserIdGroupPair $uigp.GroupId = "sg-0aad1c26bb6EXAMPLE"
Grant-EC2SecurityGroupEgress `
    -GroupId sg-1234567890abcdef0 `
    -IpPermission @{IpProtocol="tcp"; FromPort=80; ToPort=80; UserIdGroupPairs= $uigp} To remove security group rules Use the Revoke-EC2SecurityGroupIngress cmdlet to remove inbound rules.
Revoke-EC2SecurityGroupIngress `
    -GroupId sg-1234567890abcdef0 `
    -SecurityGroupRuleId sgr-09ed298024EXAMPLE Use the Revoke-EC2SecurityGroupEgress cmdlet to remove outbound rules.
Revoke-EC2SecurityGroupEgress `
    -GroupId sg-1234567890abcdef0 `
    -SecurityGroupRuleId sgr-0352250c1aEXAMPLE To modify security group rules Use the Edit-EC2SecurityGroupRule cmdlet. The following example changes the IPv4 CIDR block of the specified security group rule.
$sgrr = New-Object -TypeName Amazon.EC2.Model.SecurityGroupRuleRequest $sgrr.IpProtocol = "tcp"
$sgrr.FromPort = 80 $sgrr.ToPort = 80 $sgrr.CidrIpv4 = "0.0.0.0/0"
$sgr = New-Object -TypeName Amazon.EC2.Model.SecurityGroupRuleUpdate $sgr.SecurityGroupRuleId = "sgr-09ed298024EXAMPLE"
$sgr.SecurityGroupRule = $sgrr Edit-EC2SecurityGroupRule  `
    -GroupId sg-1234567890abcdef0 `

    -SecurityGroupRule $sgr
## Delete an Amazon EC2 security group When you are finished with a security group that you created for use with your Amazon EC2 instances, you can delete it.
Requirements
- The security group can't be associated with an instance or network interface.
- The security group can't be referenced by a rule in another security group.
Console To delete a security group
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. (Optional) To verify that your security group is not associated with an instance, do the following: a.
In the navigation pane, choose Security Groups. b.
Copy the ID of the security group to delete. c.
In the navigation pane, choose Instances. d.
In the search bar, add Security group IDs equals filter and paste the ID of the security group. If there are no results, then the security group is not associated with an instance. Otherwise, you must disassociate the security group before you can delete it.
3. In the navigation pane, choose Security Groups.
4. Select the security group and choose Actions, Delete security groups.
5. If you selected more than one security group, you are prompted for confirmation. If some of the security groups can't be deleted, we display the status of each security group, which indicates whether it will be deleted. To confirm deletion, enter Delete.
6. Choose Delete.
AWS CLI To delete a security group

Use the following delete-security-group command. aws ec2 delete-security-group --group-id sg-1234567890abcdef0 PowerShell To delete a security group Use the Remove-EC2SecurityGroup cmdlet.
Remove-EC2SecurityGroup -GroupId sg-1234567890abcdef0
## Amazon EC2 security group connection tracking Your security groups use connection tracking to track information about traffic to and from the instance. Rules are applied based on the connection state of the traffic to determine if the traffic is allowed or denied. With this approach, security groups are stateful. This means that responses to inbound traffic are allowed to flow out of the instance regardless of outbound security group rules, and vice versa.
As an example, suppose that you initiate a command such as netcat or similar to your instances from your home computer, and your inbound security group rules allow ICMP traffic. Information about the connection (including the port information) is tracked. Response traffic from the instance for the command is not tracked as a new request, but rather as an established connection, and is allowed to flow out of the instance, even if your outbound security group rules restrict outbound ICMP traffic.
For protocols other than TCP, UDP, or ICMP, only the IP address and protocol number is tracked.
If your instance sends traffic to another host, and the host sends the same type of traffic to your instance within 600 seconds, the security group for your instance accepts it regardless of inbound security group rules. The security group accepts it because it's regarded as response traffic for the original traffic.
When you change a security group rule, its tracked connections are not immediately interrupted.
The security group continues to allow packets until existing connections time out. To ensure that traffic is immediately interrupted, or that all traffic is subject to firewall rules regardless of the tracking state, you can use a network ACL for your subnet. Network ACLs are stateless and therefore do not automatically allow response traffic. Adding a network ACL that blocks traffic

in either direction breaks existing connections. For more information, see Network ACLs in the Amazon VPC User Guide.
Note Security groups have no effect on DNS traffic to or from the Route 53 Resolver, sometimes referred to as the 'VPC+2 IP address' (see What is Amazon Route 53 Resolver? in the Amazon Route 53 Developer Guide), or the 'AmazonProvidedDNS' (see Work with DHCP option sets in the Amazon Virtual Private Cloud User Guide). If you wish to filter DNS requests through the Route 53 Resolver, you can enable Route 53 Resolver DNS Firewall (see Route 53 Resolver DNS Firewall in the Amazon Route 53 Developer Guide).
### Untracked connections Not all flows of traffic are tracked. If a security group rule permits TCP or UDP flows for all traffic (0.0.0.0/0 or ::/0) and there is a corresponding rule in the other direction that permits all response traffic (0.0.0.0/0 or ::/0) for any port (0-65535), then that flow of traffic is not tracked, unless it is part of an automatically tracked connection. The response traffic for an untracked flow is allowed based on the inbound or outbound rule that permits the response traffic, not based on tracking information.
An untracked flow of traffic is immediately interrupted if the rule that enables the flow is removed or modified. For example, if you have an open (0.0.0.0/0) outbound rule, and you remove a rule that allows all (0.0.0.0/0) inbound SSH (TCP port 22) traffic to the instance (or modify it such that the connection would no longer be permitted), your existing SSH connections to the instance are immediately dropped. The connection was not previously being tracked, so the change will break the connection. On the other hand, if you have a narrower inbound rule that initially allows an SSH connection (meaning that the connection was tracked), but change that rule to no longer allow new connections from the address of the current SSH client, the existing SSH connection is not interrupted because it is tracked.
### Automatically tracked connections Connections made through the following are automatically tracked, even if the security group configuration does not otherwise require tracking:
- Egress-only internet gateways

- Global Accelerator accelerators
- NAT gateways
- Network Firewall firewall endpoints
- Network Load Balancers
- AWS PrivateLink (interface VPC endpoints)
- AWS Lambda (Hyperplane elastic network interfaces)
- DynamoDB gateway endpoints – Each connection to DynamoDB consumes 2 conntrack entries.
### Connection tracking allowances Amazon EC2 defines the maximum number of connections that can be tracked per instance.
After the maximum is reached, any packets that are sent or received are dropped because a new connection cannot be established. When this happens, applications that send and receive packets cannot communicate properly. Use the conntrack_allowance_available network performance metric to determine the number of tracked connections still available for that instance type.
To determine whether packets were dropped because the network traffic for your instance exceeded the maximum number of connections that can be tracked, use the conntrack_allowance_exceeded network performance metric. For more information, see Monitor network performance for ENA settings on your EC2 instance.
With Elastic Load Balancing, if you exceed the maximum number of connections that can be tracked per instance, we recommend that you scale either the number of instances registered with the load balancer or the size of the instances registered with the load balancer.
### Connection tracking best practices Asymmetric routing, where traffic comes into an instance through one network interface and leaves through a different network interface, can reduce the peak performance that an instance can achieve if flows are tracked.
To maintain peak performance and optimize connection management when connection tracking is enabled for your security groups, we recommend the following configuration:
- Avoid asymmetric routing topologies, if possible.

- Instead of using security groups for filtering, use network ACLs.
- If you must use security groups with connection tracking, configure the shortest idle connection tracking timeout possible. For more details on idle connection tracking timeout, see the following section.
- For long-lived connections, configure TCP keep alives to be sent at intervals of less than 5 minutes to ensure connections stay open and maintain their tracked state. This helps prevent connections from being dropped due to idle timeout and reduces the overhead of connection re- establishment, especially in cases where connection timeouts may be reduced due to minimal activity.
For more information about performance tuning on the Nitro system, see Nitro system considerations for performance tuning.
### Idle connection tracking timeout The security group tracks each connection established to ensure that return packets are delivered as expected. There is a maximum number of connections that can be tracked per instance.
Connections that remain idle can lead to connection tracking exhaustion and cause connections not to be tracked and packets to be dropped. You can set the timeout for idle connection tracking on an Elastic network interface.
Note This feature is available only with Nitro-based instances.
There are three configurable timeouts:
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
- Default: 180 seconds You may want to modify the default timeouts for any of the following cases:
- If you are monitoring tracked connections using Amazon EC2 network performance metrics, the conntrack_allowance_exceeded and conntrack_allowance_available metrics enable you to monitor dropped packets and tracked connection utilization to proactively manage EC2 instance capacity with scale up or out actions to help meet network connections demand before dropping packets.
If you are observing conntrack_allowance_exceeded drops on your EC2 instances, you may benefit from setting a lower TCP established timeout to account for stale TCP/UDP sessions resulting from improper clients or network middle boxes.
- Typically, load balancers or firewalls have TCP Established idle timeout in the range of 60 to 90 minutes. If you are running workloads that are expected to handle a very high number of connections (greater than 100k) from appliances like network firewalls, configuring a similar timeout on an EC2 network interface is advised.
- If you are running a workload that utilizes an asymmetric routing topology, we recommend that you configure a TCP Established idle timeout of 60 seconds.
- If you are running workloads with high numbers of connections like DNS, SIP, SNMP, Syslog, Radius and other services that primarily use UDP to serve requests, setting the 'UDP-stream' timeout to 60s provides higher scale/performance for existing capacity and to prevent gray failures.
- For TCP/UDP connections through Network Load Balancers, all connections are tracked. Idle timeout value for TCP flows is 350secs and UDP flows is 120 secs, and varies from interface level timeout values. You may want to configure timeouts at the network interface level to allow for more flexibility for timeout than the defaults for the load balancer.
You have the option to configure the connection tracking timeouts when you do the following:

- Create a network interface
- Modify network interface attributes
- Launch an EC2 instance
- Create an EC2 instance launch template
### Example In the following example, the security group has inbound rules that allow TCP and ICMP traffic, and outbound rules that allow all outbound traffic.
Inbound Protocol type Port number Source TCP 22 (SSH)
203.0.113.1/32 TCP 80 (HTTP)
0.0.0.0/0 TCP 80 (HTTP)
::/0 ICMP All 0.0.0.0/0 Outbound Protocol type Port number Destination All All 0.0.0.0/0 All All ::/0 With a direct network connection to the instance or network interface, the tracking behavior is as follows:
- Inbound and outbound TCP traffic on port 22 (SSH) is tracked, because the inbound rule allows traffic from 203.0.113.1/32 only, and not all IP addresses (0.0.0.0/0).
- Inbound and outbound TCP traffic on port 80 (HTTP) is not tracked, because the inbound and outbound rules allow traffic from all IP addresses.

- ICMP traffic is always tracked.
If you remove the outbound rule for IPv4 traffic, all inbound and outbound IPv4 traffic is tracked, including traffic on port 80 (HTTP). The same applies for IPv6 traffic if you remove the outbound rule for IPv6 traffic.
## Security group rules for different use cases You can create a security group and add rules that reflect the role of the instance that's associated with the security group. For example, an instance that's configured as a web server needs security group rules that allow inbound HTTP and HTTPS access. Likewise, a database instance needs rules that allow access for the type of database, such as access over port 3306 for MySQL.
The following are examples of the kinds of rules that you can add to security groups for specific kinds of access.
Examples
- Web server rules
- Database server rules
- Rules to connect to instances from your computer
- Rules to connect to instances from an instance with the same security group
- Rules for ping/ICMP
- DNS server rules
- Amazon EFS rules
- Elastic Load Balancing rules For instructions, see Create a security group and the section called "Configure security group rules".
### Web server rules The following inbound rules allow HTTP and HTTPS access from any IP address. If your VPC is enabled for IPv6, you can add rules to control inbound HTTP and HTTPS traffic from IPv6 addresses.

Protocol type Protocol number Port Source IP Notes TCP 6 80 (HTTP)
0.0.0.0/0 Allows inbound HTTP access from any IPv4 address TCP 6 443 (HTTPS)
0.0.0.0/0 Allows inbound HTTPS access from any IPv4 address TCP 6 80 (HTTP)
::/0 Allows inbound HTTP access from any IPv6  address TCP 6 443 (HTTPS)
::/0 Allows inbound HTTPS access from any IPv6  address
### Database server rules The following inbound rules are examples of rules you might add for database access, depending on what type of database you're running on your instance. For more information about Amazon RDS instances, see the Amazon RDS User Guide.
For the source IP, specify one of the following:
- A specific IP address or range of IP addresses (in CIDR block notation) in your local network
- A security group ID for a group of instances that access the database Protocol type Protocol number Port Notes TCP 6 1433 (MS SQL)
The default port to access a Microsoft SQL Server database, for  example, on an Amazon RDS instance TCP 6 3306 (MYSQL/ Aurora)
The default port to access a MySQL or Aurora database, for  example, on an Amazon RDS instance

Protocol type Protocol number Port Notes TCP 6 5439 (Redshift)
The default port to access an Amazon Redshift cluster database.
TCP 6 5432 (PostgreS QL)
The default port to access a PostgreSQL database, for example, on  an Amazon RDS instance TCP 6 1521 (Oracle)
The default port to access an Oracle database, for example, on an Amazon RDS instance You can optionally restrict outbound traffic from your database servers. For example, you might want to allow access to the internet for software updates, but restrict all other kinds of traffic. You must first remove the default outbound rule that allows all outbound traffic.
Protocol type Protocol number Port Destination IP Notes TCP 6 80 (HTTP)
0.0.0.0/0 Allows outbound HTTP access to any IPv4 address TCP 6 443 (HTTPS)
0.0.0.0/0 Allows outbound HTTPS access to any IPv4 address TCP 6 80 (HTTP)
::/0 (IPv6-enabled VPC only)
Allows outbound HTTP access to any  IPv6 address TCP 6 443 (HTTPS)
::/0 (IPv6-enabled VPC only)
Allows outbound HTTPS access to any  IPv6 address

### Rules to connect to instances from your computer To connect to your instance, your security group must have inbound rules that allow SSH access (for Linux instances) or RDP access (for Windows instances).
Protocol type Protocol number Port Source IP TCP 6 22 (SSH)
The public IPv4 address of your computer, or a range of IP addresses in your local  network. If your VPC is enabled for IPv6 and your instance has an  IPv6 address, you can enter an IPv6 address or range.
TCP 6 3389 (RDP)
The public IPv4 address of your computer, or a range of IP addresses in your local  network. If your VPC is enabled for IPv6 and your instance has an  IPv6 address, you can enter an IPv6 address or range.
### Rules to connect to instances from an instance with the same security group To allow instances that are associated with the same security group to communicate with each other, you must explicitly add rules for this.
Note If you configure routes to forward the traffic between two instances in different subnets through a middlebox appliance, you must ensure that the security groups for both instances allow traffic to flow between the instances. The security group for each instance must reference the private IP address of the other instance, or the CIDR range of the subnet that contains the other instance, as the source. If you reference the security group of the other instance as the source, this does not allow traffic to flow between the instances.

The following table describes the inbound rule for a security group that enables associated instances to communicate with each other. The rule allows all types of traffic.
Protocol type Protocol number Ports Source IP -1 (All)
-1 (All)
-1 (All)
The ID of the security group, or the CIDR range of the subnet that contains  the other instance (see note).
### Rules for ping/ICMP The ping command is a type of ICMP traffic. To ping your instance, you must add one of the following inbound ICMP rules.
Type Protocol Source Custom ICMP - IPv4 Echo request The public IPv4 address of your computer, a specific IPv4 address, or an IPv4 or IPv6 address from anywhere.
All ICMP - IPv4 IPv4 ICMP (1)
The public IPv4 address of your computer, a specific IPv4 address, or an IPv4 or IPv6 address from anywhere.

To use the ping6 command to ping the IPv6 address for your instance, you must add the following inbound ICMPv6 rule.
Type Protocol Source All ICMP - IPv6 IPv6 ICMP (58)
The IPv6 address of your computer, a specific IPv4 address, or an IPv4 or IPv6 address from anywhere.
### DNS server rules If you've set up your EC2 instance as a DNS server, you must ensure that TCP and UDP traffic can reach your DNS server over port 53.
For the source IP, specify one of the following:
- An IP address or range of IP addresses (in CIDR block notation) in a network
- The ID of a security group for the set of instances in your network that require access to the DNS server Protocol type Protocol number Port TCP 6 53 UDP 17 53
### Amazon EFS rules If you're using an Amazon EFS file system with your Amazon EC2 instances, the security group that you associate with your Amazon EFS mount targets must allow traffic over the NFS protocol.

Protocol type Protocol number Ports Source IP Notes TCP 6 2049 (NFS)
The ID of the security group Allows inbound NFS access from resources (including the mount  tar get) associated with this security group To mount an Amazon EFS file system on your Amazon EC2 instance, you must connect to your instance. Therefore, the security group associated with your instance must have rules that allow inbound SSH from your local computer or local network.
Protocol type Protocol number Ports Source IP Notes TCP 6 22 (SSH)
The IP address range of your local computer, or the range of IP addresses (in CIDR block notation) for your network.
Allows inbound SSH access from your local computer.
### Elastic Load Balancing rules If you register your EC2 instances with a load balancer, the security group associated with your load balancer must allow communication with the instances. For more information, see the following in the Elastic Load Balancing documentation.
- Security groups for your Application Load Balancer
- Security groups for your Network Load Balancer
- Configure security groups for your Classic Load Balancer
