# EC2 instance hostnames and domains

Source: apps/user-manuals/aws/ec2-ug.pdf

---

7. Choose OK, Close.
# EC2 instance hostnames and domains Understanding EC2 instance hostnames and domains is important for effectively managing and accessing your Amazon EC2 instances. Each EC2 instance can have different types of hostnames - private and public - that serve different purposes and follow specific naming conventions.
This topic explains the structure of EC2 instance hostnames, how they're constructed, and the different hostname types available. You'll learn how to view and modify hostname settings, understand when to use each type, and learn best practices for hostname management in your AWS environment.
Contents
- Understanding EC2 instance hostnames and domains
- Hostname types

## Understanding EC2 instance hostnames and domains A EC2 instance address is made up of different components. The following is an example of an EC2 instance address that uses the private IPv4 address of the instance:
   IP address         Domain name
   #--------# #------------------------# ip-10-24-34-0.us-west-2.compute.internal
#-----------# Hostname
#--------------------------------------# Fully qualified domain name (FQDN)
Where:
- IP address: The primary IPv4 address of the primary network interface associated with an instance.
- Hostname: The local name of a specific EC2 instance (used by the operating system and for local network identification)
- Domain name: The part of the FQDN that AWS provides
- Fully qualified domain name (FQDN): The complete address that includes both the hostname and the domain name. This is the full, globally unique identifier used to reach your instance across networks.
Depending on the hostname type you choose for the instance or primary network interface attached to the instance, the hostname and domain name formats will be different from the example above. This section explains the hostname type options.
## Hostname types AWS provides two types of hostnames: private and public. The following table compares the key differences between private and public hostnames, including how they resolve, how they're configured, and when to use each type.
### Private hostnames
### Public hostnames DNS resolution Private hostnames enable private FQDNs that are not accessible Public hostnames enable public FQDNs that are accessible from the

Private hostnames Public hostnames from the public internet. Private hostnames only allow requests to resolve to private IPv4 and IPv6 GUA addresses within the VPC. public internet. Public hostnames enable requests to resolve to private IPv4 and IPv6 GUA within the VPC and public IPs from the internet (split-horizon DNS).
Configuration Private hostnames are configured at the instance level.
Public hostnames are configured at the network interface level.
When to use
- For hostnames that resolve only within your VPC, for internal communication
- To keep your internal naming scheme private
- To simplify internal resource management without external DNS considerations
- To access instances over both IPv4 and IPv6 from the internet
- To enable smooth migration from IPv4 to IPv6 environments Contents
- Public hostnames
- Private hostnames Public hostnames You can use public hostnames to access EC2 instances using hostnames that resolve to the public IPv4 or IPv6 address of the instance and ease your transition to IPv6.
Public hostnames allow you to:
- Access your EC2 instances over both IPv4 and IPv6, giving you more flexibility in how you connect to your resources.
- Migrate from IPv4 to IPv6 environments at your own pace. You can, for example, decouple your database and application migrations, reducing complexity and risk.

- Use multiple hostname options (IPv4-only, IPv6-only, and dual-stack) that automatically resolve to the appropriate IP addresses.
- Benefit from improved security with split-horizon DNS, which resolves hostnames to private IP addresses when queried from within your VPC.
Contents
- Public hostname types and when to use them
- View public hostnames
- Modify public hostnames types
#### Public hostname types and when to use them To use public hostnames, you have to modify an existing network interface. This section describes the three public hostname type options and helps you decide which to use:
- Dual-stack - IP based name
- This is the best option if you are migrating or planning to migrate from IPv4 to IPv6. This option allows for connectivity over both IPv4 and IPv6, giving flexibility to clients that may be using either protocol and enables clients to keep the same hostname throughout the migration to IPv6.
- Requests from within the VPC resolve to both the private IPv4 address and the IPv6 Global Unicast Address (GUA) of the network interface. Requests from the internet resolve to both the public IPv4 and the IPv6 GUA address of the network interface.
- Example
- When you choose this option, a dual-stack FQDN will be generated for this network interface. This is an example of the FQDN that will be generated:
- f5lnz-0khrm-nt2u3-gyqqt-nbdl5-q3cdpO.ap-southeast-2.ip.aws
- Where:
- f5lnz-0khrm-nt2u3-gyqqt-nbdl5-q3cdpO is the hostname that is a base36 representation of the primary public IPv6 address (f5lnz-0khrm-nt2u3-gyqqt-nbdl5) on the network interface along with a base36 representation of the primary public IPv4 address (q3cdpO) on the network interface.

- f5lnz-0khrm-nt2u3-gyqqt-nbdl5 is resolved by the Amazon DNS resolver to the IPv6 GUA address FFFF:1407:4:f000:81d:2689:1066:4489. This is the first IPv6 GUA assigned to the network interface.
- q3cdpO is resolved to the IPv4 address of 52.54.55.56. This is the public IPv4 address attached to the primary network interface.
- ap-southeast-2 is the Region of the subnet that the network interface is in.
- ip.aws is the domain provided by AWS.
- IPv6 - IP based name
- This is a good option if you have already migrated to IPv6 and require connectivity only over IPv6.
- Requests from within the VPC or from the internet resolve to the IPv6 GUA of the network interface.
- Example
- When you choose this option, a FQDN will be generated for this network interface. This is an example of the FQDN that will be generated:
- f5lnz-0khrm-nt2u3-gyqqt-nbdl5.ap-southeast-2.ip.aws
- Where:
- f5lnz-0khrm-nt2u3-gyqqt-nbdl5 is a hostname that is a base36 representation of the primary public IPv6 address on the network interface.
- f5lnz-0khrm-nt2u3-gyqqt-nbdl5 is resolved by the Amazon DNS resolver to the IPv6 GUA address FFFF:1407:4:f000:81d:2689:1066:4489. This is the first IPv6 GUA assigned to the network interface.
- ap-southeast-2 is the Region of the subnet that the network interface is in.
- ip.aws is the domain provided by AWS.
- IPv4 - IP based name
- This is a good option if the instance using this network interface need to maintain IPv4 access during the transition to IPv6 or if applications or systems running on the instance only support IPv4. This is the best option if you only need to maintain IPv4 connectivity and your workloads don't require IPv6 support. For example, if you are migrating to IPv6, you may decide to keep some applications on IPv4 while others move to IPv6.
- Requests from within the VPC resolve to the private primary IPv4 address of the network interface. Requests from the internet resolve to the public IPv4 address of the network interface.

- Example
- If you choose this option, an IPv4-enabled public hostname will be generated for this network interface. This is an example of the DNS name that will be generated:
- ec2-52-54-55-66.ap-southeast-2.compute.amazonaws.com
- Where:
- ec2-52-54-55-66 is a hostname that is a base36 representation of the primary public IPv4 address of a network interface.
- ec2-52-54-55-66 resolves to the IPv4 address of 52.54.55.56. This is the public IPv4 address attached to the primary network interface.
- ap-southeast-2 is the Region of the subnet that the network interface is in.
- ip.aws is the domain provided by AWS.
Important In the examples above, you can see that IP addresses are used to generate the hostname. If you change the primary private IPv4 address or the first IPv6 GUA assigned to the network interface, the portion of the hostname that translates to the IP address will change and the previously-generated public hostname will no longer be valid. In addition, changing the primary IPv4 public address forces a downstream refresh of Instance Metadata Service (IMDS) in the Amazon EC2 User Guide, so the EC2 instance IMDS metadata is automatically updated.
#### View public hostnames If the VPC that the network interface is in does not have both EnableDnsHostnames and EnableDnsSupport enabled, there is no hostname type defined or generated.
Console You can view the public hostnames for an instance or primary network interface.
To view the hostname type and DNS names of an instance
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Instances.

3. Select the checkbox for the instance.
4. On the Network tab, under Hostname and DNS, find the following:
- Public hostname type
- Public DNS
- IPv4-only IP based name
- IPv6-only - IP based name
- Dualstack - IP based name To view the hostname type and DNS names of a network interface
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Network Interfaces.
3. In the search field, enter the ID of the instance. Select the ID of the network interface to open its details page.
4. Under Hostname and DNS, find the following:
- Public hostname type
- Public DNS name
- Public IPv4 DNS name
- Public IPv6 DNS name
- Public Dualstack DNS name AWS CLI To view the hostname type and DNS names of a network interface Use the describe-network-interfaces command. aws ec2 describe-network-interfaces \ --network-interface-id eni-1234567890abcdef0 \ --query NetworkInterfaces[].PublicIpDnsNameOptions The following is example output. Because the hostname type is public-dual-stack-dns- name, the DNS hostname is the same as PublicDualStackDnsName.

[ { "DnsHostnameType": "public-dual-stack-dns-name", "PublicIpv4DnsName": "ec2-52-54-55-66.ap- southeast-2.compute.amazonaws.com", "PublicIpv6DnsName": "f5lnz-0khrm-nt2u3-gyqqt-nbdl5.ap- southeast-2.ip.aws", "PublicDualStackDnsName": "f5lnz-0khrm-nt2u3-gyqqt-nbdl5-q3cdpO.ap- southeast-2.ip.aws"
     } ]
PowerShell To view the hostname type and DNS names of a network interface Use the Get-EC2NetworkInterface cmdlet.
(Get-EC2NetworkInterface `
    -NetworkInterfaceId eni-1234567890abcdef0).PublicIpDnsNameOptions The following is example output. Because the hostname type is public-dual-stack-dns- name, the DNS hostname is the same as PublicDualStackDnsName.
DnsHostnameType        : public-dual-stack-dns-name PublicDualStackDnsName : f5lnz-0khrm-nt2u3-gyqqt-nbdl5-q3cdpO.ap-southeast-2.ip.aws PublicIpv4DnsName      : ec2-52-54-55-66.ap-southeast-2.compute.amazonaws.com PublicIpv6DnsName      : f5lnz-0khrm-nt2u3-gyqqt-nbdl5.ap-southeast-2.ip.aws
#### Modify public hostnames types The public hostname type options depend on the IP addresses associated with the network interface:
- If the network interface has only a public IPv4 address, the hostname type must be IPv4 - IP based name.
- If the network interface has only an IPv6 address, the hostname type must be IPv6 - IP based name.
- If the network interface has both a public IPv4 address and an IPv6 address, the hostname type can be Dual-stack - IP based name.

Prerequisites
- The network interface must have an associated public IPv4 address or an IPv6 address.
- The VPC that the network interface is in must have EnableDnsHostnames and EnableDnsSupport enabled. See View and update DNS attributes for your VPC in the Amazon VPC User Guide.
Console To modify the public hostname type
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Network Interfaces.
3. In the search field, enter the ID of the instance. Select the checkbox for the network interface.
Alternatively, from the instance detail page, choose the Networking tab and select the ID of the network interface for device index 0.
4. Choose Actions, Modify public hostname type.
5. Choose an option:
- Dual-stack - IP based name: A dual-stack public hostname for a network interface.
Requests from within the VPC resolve to both the private IPv4 address and the IPv6 Global Unicast Address of the network interface. Requests from the internet resolve to both the public IPv4 and the IPv6 GUA address of the network interface.
- IPv4 - IP based name: An IPv4-enabled public hostname for a network interface.
Requests from within the VPC resolve to the private primary IPv4 address of the network interface. Requests from the internet resolve to the public IPv4 address of the network interface.
- IPv6 - IP based name: An IPv6-enabled public hostname for a network interface.
Requests from within the VPC or from the internet resolve to the IPv6 GUA of the network interface.
6. Choose Modify.
AWS CLI To modify the public hostname type

Use the  modify-public-ip-dns-name-options command. aws ec2 modify-public-ip-dns-name-options \ --network-interface-id eni-1234567890abcdef0 \ --hostname-type public-dual-stack-dns-name The following is example output.
{ "Successful": true } PowerShell To modify the public hostname type Use the Edit-EC2PublicIpDnsNameOption cmdlet.
Edit-EC2PublicIpDnsNameOption `
    -NetworkInterfaceId eni-1234567890abcdef0 `
    -HostNameType public-dual-stack-dns-name Private hostnames This section describes the Amazon EC2 instance private hostnames available when you launch instances into your VPC subnets.
The private hostname distinguishes the EC2 instances on your network. You may use the private hostname of an instance if, for example, you want to run scripts to communicate with some or all of the instances on your network.
Contents
- Private hostname types
- Where to find resource names and IP names
- Choosing between resource names and IP names
- Change resource based naming options for Amazon EC2

#### Private hostname types There are two private hostname types for the guest OS hostname when EC2 instances are launched in a VPC:
- IP name: The legacy naming scheme where, when you launch an instance, the private IPv4 address of the instance is included in the hostname of the instance. The IP name exists for the life of the EC2 instance. When used as the Private DNS hostname, it will only return the private IPv4 address (A record).
- Resource name: When you launch an instance, the EC2 instance ID is included in the hostname of the instance. The resource name exists for the life of the EC2 instance. When used as the Private DNS hostname, it can return both the private IPv4 address (A record) and/or the IPv6 Global Unicast Address (AAAA record).
The EC2 instance guest OS hostname type depends on the subnet settings:
- If the instance is launched into an IPv4-only subnet, you can select either IP name or resource name.
- If the instance is launched into a dual-stack (IPv4+IPv6) subnet, you can select either IP name or resource name.
- If the instance is launched into an IPv6-only subnet, resource name is used automatically.
Contents
- IP name
- Resource name
- The difference between IP name and Resource name
##### IP name When you launch an EC2 instance with the Hostname type of IP name, the guest OS hostname is configured to use the private IPv4 address.
- Format for an instance in us-east-1: private-ipv4-address.ec2.internal
- Example: ip-10-24-34-0.ec2.internal
- Format for an instance in any other AWS Region: private-ipv4- address.region.compute.internal

- Example: ip-10-24-34-0.us-west-2.compute.internal
##### Resource name When you launch EC2 instances in IPv6-only subnets, the Hostname type of Resource name is selected by default. When you launch an instance in IPv4-only or dual-stack (IPv4+IPv6) subnets, Resource name is an option that you can select. After you launch an instance, you can manage the hostname configuration. For more information, see Change resource based naming options for Amazon EC2.
When you launch an EC2 instance with a Hostname type of Resource name, the guest OS hostname is configured to use the EC2 instance ID.
- Format for an instance in us-east-1: ec2-instance-id.ec2.internal
- Example: i-0123456789abcdef.ec2.internal
- Format for an instance in any other AWS Region: ec2-instance- id.region.compute.internal
- Example: i-0123456789abcdef.us-west-2.compute.internal
##### The difference between IP name and Resource name DNS queries for both IP names and resource names coexist to ensure backward compatibility and to allow you to migrate from IP based-naming for hostnames to resource-based naming. For private DNS hostnames based on IP names, you cannot configure whether a DNS A record query for the instance is responded to or not. DNS A record queries are always responded to irrespective of the guest OS hostname settings. In contrast, for private DNS hostnames based on resource name, you can configure whether DNS A and/or DNS AAAA queries for the instance are responded to or not. You configure the response behavior when you launch an instance or modify a subnet. For more information, see Change resource based naming options for Amazon EC2.
#### Where to find resource names and IP names You can see the hostname types, resource name and IP name, in the Amazon EC2 console.
Contents
- When creating an EC2 instance
- When viewing the details of an existing EC2 instance

##### When creating an EC2 instance When you create an EC2 instance, depending on which type of subnet you select, Hostname type of Resource name might be available or it might be selected and not be modifiable. This section explains the scenarios in which you see the hostname types resource name and IP name.
###### Scenario 1 You create an EC2 instance in the wizard (see Launch an EC2 instance using the launch instance wizard in the console) and, when you configure the details, you choose a subnet that you configured to be IPv6-only.
In this case, the Hostname type of Resource name is selected automatically and is not modifiable.
DNS Hostname options of Enable IP name IPv4 (A record) DNS requests and Enable resource- based IPv4 (A record) DNS requests are deselected automatically and are not modifiable. Enable resource-based IPv6 (AAAA record) DNS requests is selected by default but is modifiable. If selected, DNS requests to the resource name will resolve to the IPv6 address (AAAA record) of this EC2 instance.
###### Scenario 2 You create an EC2 instance in the wizard (see Launch an EC2 instance using the launch instance wizard in the console) and, when you configure the details, you choose a subnet configured with an IPv4 CIDR block or both an IPv4 and IPv6 CIDR block ("dual stack").
In this case, Enable IP name IPv4 (A record) DNS requests is selected automatically and can't be changed. This means that requests to the IP name will resolve to the IPv4 address (A record) of this EC2 instance.
The options default to the configurations of the subnet, but you can modify the options for this instance depending on the subnet settings:
- Hostname type: Determines whether you want the guest OS hostname of the EC2 instance to be the resource name or IP name. The default value is IP name.
- Enable resource-based IPv4 (A record) DNS requests: Determines whether requests to your resource name resolve to the private IPv4 address (A record) of this EC2 instance. This option is not selected by default.
- Enable resource-based IPv6 (AAAA record) DNS requests: Determines whether requests to your resource name resolve to the IPv6 GUA address (AAAA record) of this EC2 instance. This option is not selected by default.

##### When viewing the details of an existing EC2 instance You can see the hostname values for an existing EC2 instance in the Details tab for the EC2 instance:
- Hostname type: The hostname in IP name or resource name format.
- Private IP DNS name (IPv4 only): The IP name that will always resolve to the private IPv4 address of the instance.
- Private resource DNS name: The resource name that resolves to the DNS records selected for this instance.
- Answer private resource DNS name: The resource name resolves to IPv4 (A), IPv6 (AAAA) or IPv4 and IPv6 (A and AAAA) DNS records.
In addition, if you connect to your EC2 instance directly over SSH and enter the hostname command, you'll see the hostname in either the IP name or resource name format.
#### Choosing between resource names and IP names When you launch an EC2 instance (see Launch an EC2 instance using the launch instance wizard in the console), if you choose a Hostname type of Resource name, the EC2 instance launches with a hostname in the resource name format. In such cases, the DNS record for this EC2 instance can also point to the resource name. This gives you the flexibility to choose whether that hostname resolves to the IPv4 address, the IPv6 address, or both the IPv4 and IPv6 address of the instance. If you plan to use IPv6 in the future or if you are using dual-stack subnets today, it's best to use a Hostname type of Resource name so that you change DNS resolution for the hostnames of your instances without making any changes to the DNS records themselves. The resource name allows you to add and remove IPv4 and IPv6 DNS resolution on an EC2 instance.
If instead you choose a Hostname type of IP name, and use it as the DNS hostname, it can only resolve to the IPv4 address of the instance. It will not resolve to the IPv6 address of the instance even if the instance has both an IPv4 address and an IPv6 address associated with it.
#### Change resource based naming options for Amazon EC2 You can change the hostname type and DNS hostname configurations for subnets, which affects all subsequent instance launches in that subject, or you can change them for an EC2 instances after you launch it.

Resource based naming options
- Hostname type: Determines the default setting for the guest OS hostname of EC2 instances launched in the subnet. This is either the resource name or IP name.
- Enable DNS hostname IPv4 (A record) requests: Determines whether DNS requests/queries to the resource name resolve to the private IPv4 address (A record) of the EC2 instance.
- Enable DNS hostname IPv6 (AAAA record) requests: Determines whether DNS requests/queries to the resource name resolve to the IPv6 address (AAAA record) of the EC2 instance.
##### Subnets Changing the subnet settings doesn't change the configuration of EC2 instances that are already launched in the subnet.
Console To modify the options for a subnet Open the Amazon VPC console and select the subnet. Choose Actions, Edit subnet settings.
Modify the settings as needed and then save your changes.
AWS CLI To modify the options for a subnet Use the modify-subnet-attribute command. aws ec2 modify-subnet-attribute \ --subnet-id subnet-0abcdef1234567890 \ --private-dns-hostname-type-on-launch resource-name \ --enable-resource-name-dns-a-record-on-launch \ --enable-resource-name-dns-aaaa-record-on-launch PowerShell To modify the options for a subnet Use the Edit-EC2SubnetAttribute cmdlet.
Edit-EC2SubnetAttribute `

    -SubnetId subnet-0abcdef1234567890 `
    -PrivateDnsHostnameTypeOnLaunch ResourceName `
    -EnableResourceNameDnsAAAARecordOnLaunch $true `
    -EnableResourceNameDnsARecordOnLaunch $true
##### EC2 instances Considerations
- To change the hostname type, you must first stop the instance. There is no need to stop an instance to change the other two options.
- Because you can't stop an instance with an instance store root volume, you can only configure the hostname type and DNS hostname options at instance launch. Only the following instance types support instance store root volumes: C1, C3, D2, I2, M1, M2, M3, R3, and X1.
Console To modify the hostname type and DNS hostname options for an instance
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. If you're going to change the Use resource based naming as guest OS hostname setting, first stop the EC2 instance. Otherwise, skip this step.
To stop the instance, select the instance and choose Instance state, Stop instance.
3. Select the instance and choose Actions, Instance settings, Change resource based naming options.
- Use resource based naming as guest OS hostname: Determines whether you want the guest OS hostname of the EC2 instance to be the resource name or IP name.
- Answer DNS hostname IPv4 (A record) requests: Determines whether DNS requests/ queries to your resource name resolve to the private IPv4 address of this EC2 instance.
- Answer DNS hostname IPv6 (AAAA record) requests: Determines whether DNS requests/queries to your resource name resolve to the IPv6 address (AAAA record) of this EC2 instance.
4. Choose Save.
5. If you stopped the instance, start it again.
