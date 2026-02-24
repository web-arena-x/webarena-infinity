# Use instance metadata to manage your EC2 instance

Source: apps/user-manuals/aws/ec2-ug.pdf

---

If the instance's system status check failure persists despite multiple recovery attempts, see Troubleshoot instances with failed status checks for additional guidance.
# Use instance metadata to manage your EC2 instance Instance metadata is data about your instance that you can use to configure or manage the running instance. Instance metadata includes the following:
Instance metadata properties Instance metadata properties are divided into categories, for example, host name, events, and security groups.
Dynamic data Dynamic data is metadata that's generated when the instance is launched, such as an instance identity document. For more information, see Dynamic data categories.
User data You can also use instance metadata to access user data that you specified when you launched your instance. For example, you can specify parameters for configuring your instance, or include a simple script. You can also build generic AMIs and use user data to modify the configuration files supplied at launch time. For example, if you run web servers for various small businesses, they can all use the same generic AMI and retrieve their content from an Amazon S3 bucket that you specify in the user data at launch. To add a new customer at any time, create a bucket for the customer, add their content, and launch your AMI with the unique bucket name provided to your code in the user data. If you launch multiple instances using the same RunInstances call, the user data is available to all instances in that reservation. Each instance that is part of the same reservation has a unique ami-launch-index number, so that you can write code that controls what the instances do. For example, the first host might elect itself as the original node in a cluster. For a detailed AMI launch example, see Identify each instance launched in a single request.
Important Although you can only access instance metadata and user data from within the instance itself, the data is not protected by authentication or cryptographic methods. Anyone who has direct access to the instance, and potentially any software running on the instance,

can view its metadata. Therefore, you should not store sensitive data, such as passwords or long-lived encryption keys, as user data.
Contents
- Instance metadata categories
- Dynamic data categories
- Access instance metadata for an EC2 instance
- Configure the Instance Metadata Service options
- Run commands when you launch an EC2 instance with user data input
- Identify each instance launched in a single request
## Instance metadata categories Instance metadata properties are divided into categories. To retrieve instance metadata properties, you specify the category in the request, and the metadata is returned in the response.
When new categories are released, a new instance metadata build is created with a new version number. In the following table, the Version when category was released column specifies the build version when an instance metadata category was released. To avoid having to update your code every time Amazon EC2 releases a new instance metadata build, use latest instead of the version number in your metadata requests. For more information, see Get the available versions of the instance metadata.
When Amazon EC2 releases a new instance metadata category, the instance metadata for the new category might not be available for existing instances. With Nitro-based instances, you can retrieve instance metadata only for the categories that were available at launch. For instances with the Xen hypervisor, you can stop and then start the instance to update the categories that are available for the instance.
The following table lists the categories of instance metadata. Some of the category names include placeholders for data that is unique to your instance. For example, mac represents the MAC address for the network interface. You must replace the placeholders with actual values when you retrieve the instance metadata.

Category Description Version when category was released ami-id The AMI ID used to launch the instance.
1.0 ami-launch-index If you launch multiple instances using the same   RunInstan ces  call, this value indicates the launch  order for each instance.
The value of the first instance launched is 0.  If you launch instances using Auto Scaling or EC2 fleet, this value is  always 0.
1.0 ami-manifest-path The path to the AMI manifest file in Amazon S3. If you used an  Amazon EBS-backed AMI to launch the instance, the returned result is   unknown.
1.0 ancestor-ami-ids The AMI IDs of any instances that were rebundled to create this AMI.  This value will only exist if the AMI manifest file contained an   ancestor-amis  key.
2007-10-10 autoscaling/target- lifecycle-state Value showing the target Auto Scaling lifecycle state that an Auto Scaling  instance is transitioning to. Present when the instance transitions  to one of the target lifecycle states after March 10, 2022.
Possible  values: Detached
| InService  |   Standby | Terminated  |   Warmed:Hi 2021-07-15

Category Description Version when category was released bernated  | Warmed:Ru nning  |   Warmed:Stopped
| Warmed:Terminated .  See Retrieve the target lifecycle state through instance  metadata in the Amazon EC2 Auto Scaling User Guide. block-device-mapping/ ami The virtual device that contains the root/boot file system.
2007-12-15 block-device-mapping/ ebsN The virtual devices associated with any Amazon EBS volumes.
Amazon EBS volumes  are only available in metadata if they were present at launch time or  when the instance was last started.
The N indicates the index of the Amazon EBS volume (such as ebs1 or   ebs2).
2007-12-15

Category Description Version when category was released block-device-mapping/ ephemeral N The virtual devices for any non- NVMe instance store volumes.
The   N indicates the index of each volume. The  number of instance store volumes in the block device mapping might not  match the actual number of instance store volumes for the instance.
The  instance type determine s the number of instance store volumes that are  available to an instance. If the number of instance store volumes in a block device mapping exceeds the number available to an instance, the  additional instance store volumes are ignored.
2007-12-15 block-device-mapping/ root The virtual devices or partitions associated with the root devices or  partitions on the virtual device, where the root (/ or C:) file system  is associated with the given instance.
2007-12-15 block-device-mapping/ swap The virtual devices associated with swap. Not always  present.
2007-12-15 events/maintenance/ history If there are completed or canceled maintenance events for the instance, contains a JSON string with information about the events.
2018-08-17

Category Description Version when category was released events/maintenance/ scheduled If there are active maintenance events for the instance, contains a JSON string with informati on about the events. For more information, see   View scheduled events that affect your Amazon EC2 instances.
2018-08-17 events/recommendations/ rebalance The approximate time, in UTC, when the EC2 instance rebalance recommendation notification is emitted for the instance. The following is an example of the metadata for this category:
{"noticeTime":  "202 0-11-05T08:22:00Z"} .
This category is available only after the notification is emitted.
For more information, see EC2 instance rebalance recommend ations.
2020-10-27

Category Description Version when category was released hostname If the EC2 instance is using IP- based naming (IPBN), this is the private IPv4 DNS hostname of the instance. If the EC2 instance is using  Resource-based naming (RBN), this is the RBN. In cases where multiple  network interface s are present, this refers to the eth0 device (the  device for which the device number is 0). For more information about  IPBN and RBN, see EC2 instance hostnames and domains.
1.0 iam/info If there is an IAM role associate d with the instance, contains  in formation about the last time the instance profile was updated,  in cluding the instance's LastUpdat ed date, InstanceProfileArn, and InstanceProfileId. Otherwise, not present.
2012-01-12 iam/security-crede ntials/role-name If there is an IAM role associated with the instance,  role-name  is the name of the role, and   role- name  contains the temporary security  credentials associated with the role (for more informati on, see Retrieve security credentia ls from instance metadata).
 Otherwise, not present.
2012-01-12

Category Description Version when category was released identity-credentials/ ec2/info Information about the credentials in   identity-credentials/ ec2/security-credentials /ec2-instance .
2018-05-23 identity-credentia ls/ec2/security-c redentials/ec2-in stance Credentials for the instance identity role that allow on-instan ce  software to identify itself to AWS to support features such as  EC2 Instance Connect and AWS Systems Manager Default Host Management Configura tion. These  credentials have no policies attached, so they have no additional AWS  API permissions beyond identifying the instance to the AWS feature.  For more information, see Instance identity roles for Amazon EC2 instances.
2018-05-23 instance-action Notifies the instance that it should reboot in preparation for  bundlin g. Valid values: none | shutdown
|  bundle-pending .
2008-09-01 instance-id The ID of this instance.
1.0 instance-life-cycle The purchasing option of this instance. For more informati on, see   Amazon EC2 billing and purchasing options.
2019-10-01 instance-type The type of instance. For more information, see Amazon EC2 instance types.
2007-08-29

Category Description Version when category was released ipv6 The IPv6 address of the instance.
In cases where multiple network interfaces are present, this refers to the eth0 device (the device for  which the device number is 0) network interface and the first IPv6  address assigned. If no IPv6 address exists on network interface[0],  this item is not set and results in an HTTP 404 response.
2021-01-03 kernel-id The ID of the kernel launched with this instance, if  applicable.
2008-02-01 local-hostname In cases where multiple network interfaces are present, this refers to the eth0 device (the device for which the device number is 0).
If the  EC2 instance is using IP- based naming (IPBN), this is the private IPv4  DNS hostname of the instance. If the EC2 instance is using  Resource-based naming (RBN), this is the RBN. For more information about  IPBN, RBN, and EC2 instance naming, see EC2 instance hostnames and domains.
2007-01-19

Category Description Version when category was released local-ipv4 The private IPv4 address of the instance. In cases where multiple network interfaces are present, this refers to the eth0 device (the  device for which the device number is 0). If this is an IPv6-only instance, this item is not set and results in an HTTP 404  response.
1.0 mac The instance's media access control (MAC) address. In cases where  multiple network interface s are present, this refers to the eth0 device  (the device for which the device number is 0).
2011-01-01 metrics/vhostmd No longer available.
2011-05-01 network/interfaces/ macs/mac/device-number The unique device number associated with that interface.
The device  number corresponds to the device name; for example, a   device-number  of 2 is for the eth2 device. This  category corresponds to the DeviceInd ex  and   device-index  fields that are used by the Amazon EC2 API and  the EC2 commands for the AWS CLI.
2011-01-01 network/interfaces/ macs/mac/interface-id The ID of the network interface.
2011-01-01

Category Description Version when category was released network/interfaces /macs/mac/ipv4-as sociations/public-ip The private IPv4 addresses that are associated with each public IP  address and assigned to that interface.
2011-01-01 network/interfaces/ macs/mac/ipv6s The IPv6 addresses assigned to the interface.
2016-06-30 network/interfaces/ macs/mac/ipv6-prefix The IPv6 prefix assigned to the network interface.

network/interfaces /macs/mac/local-h ostname The private IPv4 DNS hostname of the instance. In cases where multiple network interfaces are present, this refers to the eth0 device (the device for which the device number is 0). If this is a IPv6-only instance, this is the resource-based name. For more information about IPBN and RBN, see EC2 instance hostnames and domains.
2007-01-19 network/interfaces/ macs/mac/local-ipv4s The private IPv4 addresses associated with the interface.
If this is  an IPv6-only network interface, this item is not set and results in an  HTTP 404 response.
2011-01-01 network/interfaces/ macs/mac/mac The instance's MAC address.
2011-01-01 network/interfaces/ macs/mac/network-card The index of the network card.
Some instance types support multiple  network cards.
2020-11-01

Category Description Version when category was released network/interfaces/ macs/mac/owner-id The ID of the owner of the network interface. In multiple- interface environments, an interface can be attached by a third party, such as  Elastic Load Balancing. Traffic on an interface is always billed to the interface o wner.
2011-01-01 network/interfaces /macs/mac/public- hostname The interface's public DNS (IPv4).
This category is only returned if the enableDnsHostnames attribute is set to   true. For more information, see DNS attributes for your VPC in the Amazon VPC User Guide. If the instance only has a public-IPv6 address and no public-IPv4 address, this item is not set and  results in an HTTP 404 response.
2011-01-01 network/interfaces/ macs/mac/public-ipv4s The public IP address or Elastic IP addresses associated with the interface. There may be multiple IPv4 addresses on an instance.
2011-01-01 network/interfaces/ macs/mac/security- groups Security groups to which the network interface belongs.
2011-01-01 network/interfaces/ macs/mac/security- group-ids The IDs of the security groups to which the network interface b elongs.
2011-01-01

Category Description Version when category was released network/interfaces/ macs/mac/subnet-id The ID of the subnet in which the interface resides.
2011-01-01 network/interfaces/ macs/mac/subnet-ipv4- cidr-block The IPv4 CIDR block of the subnet in which the interface resides.
2011-01-01 network/interfaces/ macs/mac/subnet-ipv6- cidr-blocks The IPv6 CIDR block of the subnet in which the interface resides.
2016-06-30 network/interfaces/ macs/mac/vpc-id The ID of the VPC in which the interface resides.
2011-01-01 network/interfaces/ macs/mac/vpc-ipv4- cidr-block The primary IPv4 CIDR block of the VPC.
2011-01-01 network/interfaces/ macs/mac/vpc-ipv4- cidr-blocks The IPv4 CIDR blocks for the VPC.
2016-06-30 network/interfaces/ macs/mac/vpc-ipv6- cidr-blocks The IPv6 CIDR block of the VPC in which the interface resides.
2016-06-30 placement/availability- zone The Availability Zone in which the instance launched.
2008-02-01 placement/availability- zone-id The static Availability Zone ID in which the instance is launched. T he Availability Zone ID is consisten t across accounts. However, it might be different from the Availability Zone, which can vary by  account.
2019-10-01

Category Description Version when category was released placement/group-name The name of the placement group in which the instance is  launched.
2020-08-24 placement/host-id The ID of the host on which the instance is launched. Applicable only  to Dedicated Hosts.
2020-08-24 placement/partition- number The number of the partition in which the instance is  launched.
2020-08-24 placement/region The AWS Region in which the instance is launched.
2020-08-24 product-codes AWS Marketplace product codes associated with the instance, if any.
2007-03-01 public-hostname The instance's public DNS (IPv4).
This category is only returned if the enableDnsHostnames attribute is set to   true. For more information, see DNS attributes for your VPC in the Amazon VPC User Guide. If the instance only has a public-IPv6 address and no public-IPv4 address, this item is not set and  results in an HTTP 404 response.
2007-01-19 public-ipv4 The public IPv4 address. If an Elastic IP address is associate d with  the instance, the value returned is the Elastic IP address.
2007-01-19

Category Description Version when category was released public-keys/0/openssh- key Public key. Only available if supplied at instance launch  time.
1.0 ramdisk-id The ID of the RAM disk specified at launch time, if  applicable.
2007-10-10 reservation-id The ID of the reservation.
1.0 security-groups The names of the security groups applied to the instance.
After launch, you can change the security groups of the instances.
 Such changes are reflected here and in  network/interfaces/macs /mac/security-groups.
1.0 services/domain The domain for AWS resources for the Region.
2014-02-25 services/partition The partition that the resource is in. For standard AWS Regions, the partition is aws. If you have resources in other  partitions, the partition is   aws-partition name .  For example, the partition for resources in the China (Beijing)
 Region is aws-cn.
2015-10-20

Category Description Version when category was released spot/instance-action The action (hibernate, stop, or terminate) and the approximate time, in UTC, when the action will occur. This item is present only if the Spot Instance has been marked for hibernate, stop, or terminate. For  more information, see instance-action.
2016-11-15 spot/termination-time The approximate time, in UTC, that the operating system for your  Spot Instance will receive the shutdown signal. This item is present and  contains a time value (for example, 2015-01-0 5T18:02:00Z) only if  the Spot Instance has been marked for termination by Amazon EC2. The termination-time item is not set to a time if you terminated the Spot Instance yourself. For more information, see termination- time.
2014-11-05 system The underlying virtualization type (hypervisor) of the instance.
2022-09-24 tags/instance The instance tags associated with the instance. Only available if you explicitly allow access to tags in instance metadata. For more information, see Enable access to tags in instance metadata.
2021-03-23

## Dynamic data categories The following table lists the categories of dynamic data.
Category Description Version when category was released fws/instance- monitoring Value showing whether the customer has enabled detailed one-minute monitoring in CloudWatch. Valid values: enabled | disabled 2009-04-0 4 instance- identity/docume nt JSON containing instance attributes, such as instance- id, private IP  address, etc. See Instance identity documents for Amazon EC2 instances.
2009-04-0 4 instance- identity/pkcs7 Used to verify the document's authenticity and content against the  signature. See Instance identity documents for Amazon EC2 instances.
2009-04-0 4 instance- identity/signat ure Data that can be used by other parties to verify its origin and  authenticity. See Instance identity documents for Amazon EC2 instances.
2009-04-0 4
## Access instance metadata for an EC2 instance You can access EC2 instance metadata from inside of the instance itself or from the EC2 console, API, SDKs, or the AWS CLI. To get the current instance metadata settings for an instance from the console or command line, see Query instance metadata options for existing instances.
You can also modify user data for instances with an EBS root volume. The instance must be in the stopped state. For console directions, see Update the instance user data. For a Linux example that uses the AWS CLI, see modify-instance-attribute. For a Windows example that uses the Tools for Windows PowerShell, see the section called "User data and the Tools for Windows PowerShell".

Note You are not billed for HTTP requests used to retrieve instance metadata and user data.
### Instance metadata access considerations To avoid problems with instance metadata retrieval, consider the following.
Command format The command format is different, depending on whether you use Instance Metadata Service Version 1 (IMDSv1) or Instance Metadata Service Version 2 (IMDSv2). By default, you can use both versions of the Instance Metadata Service. To require the use of IMDSv2, see Use the Instance Metadata Service to access instance metadata.
If IMDSv2 is required, IMDSv1 does not work If you use IMDSv1 and receive no response, it's likely that IMDSv2 is required. To check whether IMDSv2 is required, select the instance to view its details. The IMDSv2 value indicates either Required (you must use IMDSv2) or Optional (you can use either IMDSv2 or IMDSv1).
(IMDSv2) Use /latest/api/token to retrieve the token Issuing PUT requests to any version-specific path, for example /2021-03-23/api/token, results in the metadata service returning 403 Forbidden errors. This behavior is intended.
Metadata version To avoid having to update your code every time Amazon EC2 releases a new instance metadata build, we recommend that you use latest in the path, and not the version number.
IPv6 support To retrieve instance metadata using an IPv6 address, ensure that you enable and use the IPv6 address of the IMDS [fd00:ec2::254] instead of the IPv4 address 169.254.169.254. The instance must be a Nitro-based instance launched in a subnet that supports IPv6.
(Windows) Create custom AMIs using Windows Sysprep To ensure that IMDS works when you launch an instance from a custom Windows AMI, the AMI must be a standardized image created with Windows Sysprep. Otherwise, the IMDS won't work.
For more information, see Create an Amazon EC2 AMI using Windows Sysprep.

In a container environment, consider reconfiguration or increasing the hop limit to 2 The AWS SDKs use IMDSv2 calls by default. If the IMDSv2 call receives no response, some AWS SDKs retry the call and, if still unsuccessful, use IMDSv1. This can result in a delay, especially in a container environment. For those AWS SDKs that require IMDSv2, if the hop limit is 1 in a container environment, the call might not receive a response at all because going to the container is considered an additional network hop.
To mitigate these issues in a container environment, consider changing the configuration to pass settings (such as the AWS Region) directly to the container, or consider increasing the hop limit to 2. For information about the hop limit impact, see Add defense in depth against open firewalls, reverse proxies, and SSRF vulnerabilities with enhancements to the EC2 Instance Metadata Service. For information about changing the hop limit, see Change the PUT response hop limit.
Packets per second (PPS) limit There is a 1024 packet per second (PPS) limit to services that use link-local addresses. This limit includes the aggregate of Route 53 Resolver DNS Queries, Instance Metadata Service (IMDS) requests, Amazon Time Service Network Time Protocol (NTP) requests, and Windows Licensing Service (for Microsoft Windows based instances) requests.
Additional considerations for user data access
- User data is treated as opaque data: what you specify is what you get back upon retrieval. It is up to the instance to interpret and act on user data.
- User data must be base64-encoded. Depending on the tool or SDK that you're using, the base64- encoding might be performed for you. For example:
- The Amazon EC2 console can perform the base64-encoding for you or accept base64-encoded input.
- AWS CLI version 2 performs base64-encoding of binary parameters for you by default. AWS CLI version 1 performs the base64-encoding of the --user-data parameter for you.
- The AWS SDK for Python (Boto3) performs base64-encoding of the UserData parameter for you.
- User data is limited to 16 KB, in raw form, before it is base64-encoded. The size of a string of length n after base64-encoding is ceil(n/3)*4.

- User data must be base64-decoded when you retrieve it. If you retrieve the data using instance metadata or the console, it's decoded for you automatically.
- If you stop an instance, modify its user data, and start the instance, the updated user data is not run automatically when you start the instance. With Windows instances, you can configure settings so that updated user data scripts are run one time when you start the instance or every time you reboot or start the instance.
- User data is an instance attribute. If you create an AMI from an instance, the instance user data is not included in the AMI.
### Access instance metadata from within an EC2 instance Because your instance metadata is available from your running instance, you do not need to use the Amazon EC2 console or the AWS CLI. This can be helpful when you're writing scripts to run from your instance. For example, you can access the local IP address of your instance from instance metadata to manage a connection to an external application.
All of the following are considered instance metadata, but they are accessed in different ways.
Select the tab that represents the type of instance metadata you want to access to see more information.
Metadata Instance metadata properties are divided into categories. For a description of each instance metadata category, see Instance metadata categories.
To access instance metadata properties from within a running instance, get the data from the following IPv4 or IPv6 URIs. These IP addresses are link-local addresses and are valid only from the instance. For more information, see Link-local addresses.
IPv4 http://169.254.169.254/latest/meta-data/ IPv6 http://[fd00:ec2::254]/latest/meta-data/

Dynamic data To retrieve dynamic data from within a running instance, use one of the following URIs.
IPv4 http://169.254.169.254/latest/dynamic/ IPv6 http://[fd00:ec2::254]/latest/dynamic/ Examples: Access with cURL The following examples use cURL to retrieve the high-level instance identity categories.
IMDSv2 [ec2-user ~]$ TOKEN=`curl -X PUT "http://169.254.169.254/latest/api/token" -H "X- aws-ec2-metadata-token-ttl-seconds: 21600"` \ && curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/dynamic/ instance-identity/ rsa2048 pkcs7 document signature dsa2048 IMDSv1 [ec2-user ~]$ curl http://169.254.169.254/latest/dynamic/instance-identity/ rsa2048 pkcs7 document signature dsa2048 Examples: Access with PowerShell The following examples use PowerShell to retrieve the high-level instance identity categories.
IMDSv2

PS C:\> [string]$token = Invoke-RestMethod -Headers @{"X-aws-ec2-metadata-token-ttl- seconds" = "21600"} -Method PUT -Uri http://169.254.169.254/latest/api/token PS C:\> Invoke-RestMethod -Headers @{"X-aws-ec2-metadata-token" = $token} -Method GET -Uri http://169.254.169.254/latest/dynamic/instance-identity/ document rsa2048 pkcs7 signature IMDSv1 PS C:\> Invoke-RestMethod -uri http://169.254.169.254/latest/dynamic/instance- identity/ document rsa2048 pkcs7 signature For more information about dynamic data and examples of how to retrieve it, see Instance identity documents for Amazon EC2 instances.
User data To retrieve user data from an instance, use one of the following URIs. To retrieve user data using the IPv6 address, you must enable it, and the instance must be a Nitro-based instance in a subnet that supports IPv6.
IPv4 http://169.254.169.254/latest/user-data IPv6 http://[fd00:ec2::254]/latest/user-data A request for user data returns the data as it is (content type application/octet-stream). If the instance does not have any user data, the request returns 404 - Not Found.
Examples: Access with cURL to retrieve comma-separated text

The following examples use cURL to retrieve user data that was specified as comma-separated text.
IMDSv2 TOKEN=`curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata- token-ttl-seconds: 21600"` \ && curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/user- data 1234,john,reboot,true | 4512,richard, | 173,,, IMDSv1 curl http://169.254.169.254/latest/user-data 1234,john,reboot,true | 4512,richard, | 173,,, Examples: Access with PowerShell to retrieve comma-separated text The following examples use PowerShell to retrieve user data that was specified as comma- separated text.
IMDSv2 [string]$token = Invoke-RestMethod -Headers @{"X-aws-ec2-metadata-token-ttl-seconds"
 = "21600"} -Method PUT -Uri http://169.254.169.254/latest/api/token Invoke-RestMethod -Headers @{"X-aws-ec2-metadata-token" = $token} -Method GET -Uri http://169.254.169.254/latest/user-data 1234,john,reboot,true | 4512,richard, | 173,,, IMDSv1 Invoke-RestMethod -Headers @{"X-aws-ec2-metadata-token" = Invoke-RestMethod -Headers @{"X-aws-ec2-metadata-token-ttl-seconds" = "21600"} `
-Method PUT -Uri http://169.254.169.254/latest/api/token} -Method GET -uri http://169.254.169.254/latest/user-data 1234,john,reboot,true | 4512,richard, | 173,,, Examples: Access with cURL to retrieve a script The following examples use cURL to retrieve user data that was specified as a script.

IMDSv2 TOKEN=`curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata- token-ttl-seconds: 21600"` \ && curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/user- data
#!/bin/bash yum update -y service httpd start chkconfig httpd on IMDSv1 curl http://169.254.169.254/latest/user-data
#!/bin/bash yum update -y service httpd start chkconfig httpd on Examples: Access with PowerShell to retrieve a script The following examples use PowerShell to retrieve user data that was specified as a script.
IMDSv2 [string]$token = Invoke-RestMethod -Headers @{"X-aws-ec2-metadata-token-ttl-seconds"
 = "21600"} -Method PUT -Uri http://169.254.169.254/latest/api/token Invoke-RestMethod -Headers @{"X-aws-ec2-metadata-token" = $token} -Method GET -Uri http://169.254.169.254/latest/user-data <powershell>
$file = $env:SystemRoot + "\Temp\" + (Get-Date).ToString("MM-dd-yy-hh-mm")
New-Item $file -ItemType file </powershell>
<persist>true</persist>
IMDSv1 Invoke-RestMethod -uri http://169.254.169.254/latest/user-data <powershell>
$file = $env:SystemRoot + "\Temp\" + (Get-Date).ToString("MM-dd-yy-hh-mm")
New-Item $file -ItemType file

</powershell>
<persist>true</persist>
### Query instance metadata options for existing instances You can query the instance metadata options for your existing instances.
Console To query the instance metadata options for an existing instance
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Instances.
3. Select your instance and check the following fields:
- IMDSv2 – The value is either Required or Optional.
- Allow tags in instance metadata – The value is either Enabled or Disabled.
4. With your instance selected, choose Actions, Instance settings, Modify instance metadata options.
The dialog box displays whether the instance metadata service is enabled or disabled for the selected instance.
AWS CLI To query the instance metadata options for an existing instance Use the describe-instances command. aws ec2 describe-instances \ --instance-id i-1234567898abcdef0 \ --query 'Reservations[].Instances[].MetadataOptions'
PowerShell To query the instance metadata options for an existing instance using the Tools for PowerShell Use the Get-EC2Instance Cmdlet.

(Get-EC2Instance `
    -InstanceId i-1234567898abcdef0).Instances.MetadataOptions
### Responses and error messages All instance metadata is returned as text (HTTP content type text/plain).
A request for a specific metadata resource returns the appropriate value, or a 404 - Not Found HTTP error code if the resource is not available.
A request for a general metadata resource (the URI ends with a /) returns a list of available resources, or a 404 - Not Found HTTP error code if there is no such resource. The list items are on separate lines, terminated by line feeds (ASCII 10).
If an IMDSv1 request receives no response, it's likely that IMDSv2 is required.
For requests made using IMDSv2, the following HTTP error codes can be returned:
- 400 - Missing or Invalid Parameters – The PUT request is not valid.
- 401 - Unauthorized – The GET request uses an invalid token. The recommended action is to generate a new token.
- 403 - Forbidden – The request is not allowed or the IMDS is turned off.
- 404 - Not Found – The resource is not available or there is no such resource.
- 503 – The request could not be completed. Retry the request.
If the IMDS returns an error, curl prints the error message in the output and returns a success status code. The error message is stored in the TOKEN variable, which causes curl commands that use the token to fail. If you call curl with the -f option, it returns an error status code in the event of an HTTP server error. If you enable error handling, the shell can catch the error and stop the script.
### Query throttling We throttle queries to the IMDS on a per-instance basis, and we place limits on the number of simultaneous connections from an instance to the IMDS.
If you're using the IMDS to retrieve AWS security credentials, avoid querying for credentials during every transaction or concurrently from a high number of threads or processes, as this might lead to

throttling. Instead, we recommend that you cache the credentials until they start approaching their expiry time. For more information about IAM role and security credentials associated with the role, see Retrieve security credentials from instance metadata.
If you are throttled while accessing the IMDS, retry your query with an exponential backoff strategy.
### Use the Instance Metadata Service to access instance metadata You can access instance metadata from a running instance using one of the following methods:
- Instance Metadata Service Version 2 (IMDSv2) – a session-oriented method For examples, see Examples for IMDSv2.
- Instance Metadata Service Version 1 (IMDSv1) – a request/response method For examples, see Examples for IMDSv1.
By default, you can use either IMDSv1 or IMDSv2, or both.
You can configure the Instance Metadata Service (IMDS) on each instance to only accept IMDSv2 calls, which will cause IMDSv1 calls to fail. For information about how to configure your instance to use IMDSv2, see Configure the Instance Metadata Service options.
The PUT or GET headers are unique to IMDSv2. If these headers are present in the request, then the request is intended for IMDSv2. If no headers are present, it is assumed the request is intended for IMDSv1.
For an extensive review of IMDSv2, see Add defense in depth against open firewalls, reverse proxies, and SSRF vulnerabilities with enhancements to the EC2 Instance Metadata Service.
Topics
- How Instance Metadata Service Version 2 works
- Use a supported AWS SDK
- Examples for IMDSv2
- Examples for IMDSv1

#### How Instance Metadata Service Version 2 works IMDSv2 uses session-oriented requests. With session-oriented requests, you create a session token that defines the session duration, which can be a minimum of one second and a maximum of six hours. During the specified duration, you can use the same session token for subsequent requests.
After the specified duration expires, you must create a new session token to use for future requests.
Note The examples in this section use the IPv4 address of the Instance Metadata Service (IMDS):
169.254.169.254. If you are retrieving instance metadata for EC2 instances over the IPv6 address, ensure that you enable and use the IPv6 address instead: [fd00:ec2::254]. The IPv6 address of the IMDS is compatible with IMDSv2 commands. The IPv6 address is only accessible on Nitro-based instances in an IPv6-supported subnet (dual stack or IPv6 only).
The following examples use a shell script and IMDSv2 to retrieve the top-level instance metadata items. Each example:
- Creates a session token lasting six hours (21,600 seconds) using the PUT request
- Stores the session token header in a variable named TOKEN (Linux instances) or token (Windows instances)
- Requests the top-level metadata items using the token
##### Linux example You can run two separate commands, or combine them.
Separate commands First, generate a token using the following command.
[ec2-user ~]$ TOKEN=`curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws- ec2-metadata-token-ttl-seconds: 21600"`
Then, use the token to generate top-level metadata items using the following command.
[ec2-user ~]$ curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/ meta-data/

Combined commands You can store the token and combine the commands. The following example combines the above two commands and stores the session token header in a variable named TOKEN.
Note If there is an error in creating the token, instead of a valid token, an error message is stored in the variable, and the command will not work.
[ec2-user ~]$ TOKEN=`curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws- ec2-metadata-token-ttl-seconds: 21600"` \ && curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/ After you've created a token, you can reuse it until it expires. In the following example command, which gets the ID of the AMI used to launch the instance, the token that is stored in $TOKEN in the previous example is reused.
[ec2-user ~]$ curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/ meta-data/ami-id
##### Windows example PS C:\> [string]$token = Invoke-RestMethod -Headers @{"X-aws-ec2-metadata-token-ttl- seconds" = "21600"} -Method PUT -Uri http://169.254.169.254/latest/api/token PS C:\> Invoke-RestMethod -Headers @{"X-aws-ec2-metadata-token" = $token} -Method GET - Uri http://169.254.169.254/latest/meta-data/ After you've created a token, you can reuse it until it expires. In the following example command, which gets the ID of the AMI used to launch the instance, the token that is stored in $token in the previous example is reused.
PS C:\> Invoke-RestMethod -Headers @{"X-aws-ec2-metadata-token" = $token} `
 -Method GET -uri http://169.254.169.254/latest/meta-data/ami-id When you use IMDSv2 to request instance metadata, the request must include the following:

1. Use a PUT request to initiate a session to the instance metadata service. The PUT request returns a token that must be included in subsequent GET requests to the instance metadata service. The token is required to access metadata using IMDSv2.
2. Include the token in all GET requests to the IMDS. When token usage is set to required, requests without a valid token or with an expired token receive a 401 - Unauthorized HTTP error code.
- The token is an instance-specific key. The token is not valid on other EC2 instances and will be rejected if you attempt to use it outside of the instance on which it was generated.
- The PUT request must include a header that specifies the time to live (TTL) for the token, in seconds, up to a maximum of six hours (21,600 seconds). The token represents a logical session. The TTL specifies the length of time that the token is valid and, therefore, the duration of the session.
- After a token expires, to continue accessing instance metadata, you must create a new session using another PUT.
- You can choose to reuse a token or create a new token with every request. For a small number of requests, it might be easier to generate and immediately use a token each time you need to access the IMDS. But for efficiency, you can specify a longer duration for the token and reuse it rather than having to write a PUT request every time you need to request instance metadata.
There is no practical limit on the number of concurrent tokens, each representing its own session. IMDSv2 is, however, still constrained by normal IMDS connection and throttling limits.
For more information, see Query throttling.
HTTP GET and HEAD methods are allowed in IMDSv2 instance metadata requests. PUT requests are rejected if they contain an X-Forwarded-For header.
By default, the response to PUT requests has a response hop limit (time to live) of 1 at the IP protocol level. If you need a bigger hop limit, you can adjust it by using the modify-instance- metadata-options AWS CLI command. For example, you might need a bigger hop limit for backward compatibility with container services running on the instance. For more information, see Modify instance metadata options for existing instances.
#### Use a supported AWS SDK To use IMDSv2, your EC2 instances must use an AWS SDK version that supports using IMDSv2. The latest versions of all the AWS SDKs support using IMDSv2.

Important We recommend that you to stay up to date with SDK releases to keep up with the latest features, security updates, and underlying dependencies. Continued use of an unsupported SDK version is not recommended and is done at your discretion. For more information, see the AWS SDKs and Tools maintenance policy in the AWS SDKs and Tools Reference Guide.
The following are the minimum versions that support using IMDSv2:
- AWS CLI – 1.16.289
- AWS Tools for Windows PowerShell – 4.0.1.0
- AWS SDK for .NET – 3.3.634.1
- AWS SDK for C++ – 1.7.229
- AWS SDK for Go – 1.25.38
- AWS SDK for Go v2 – 0.19.0
- AWS SDK for Java – 1.11.678
- AWS SDK for Java 2.x – 2.10.21
- AWS SDK for JavaScript in Node.js – 2.722.0
- AWS SDK for Kotlin – 1.1.4
- AWS SDK for PHP – 3.147.7
- AWS SDK for Python (Botocore) – 1.13.25
- AWS SDK for Python (Boto3) – 1.12.6
- AWS SDK for Ruby – 3.79.0
#### Examples for IMDSv2 Run the following examples on your Amazon EC2 instance to retrieve the instance metadata for IMDSv2.
On Windows instances, you can use Windows PowerShell or you can install cURL or wget. If you install a third-party tool on a Windows instance, ensure that you read the accompanying documentation carefully, as the calls and the output might be different from what is described here.

Examples
- Get the available versions of the instance metadata
- Get the top-level metadata items
- Get the values for metadata items
- Get the list of available public keys
- Show the formats in which public key 0 is available
- Get public key 0 (in the OpenSSH key format)
- Get the subnet ID for an instance
- Get the instance tags for an instance
##### Get the available versions of the instance metadata This example gets the available versions of the instance metadata. Each version refers to an instance metadata build when new instance metadata categories were released. The instance metadata build versions do not correlate with the Amazon EC2 API versions. The earlier versions are available to you in case you have scripts that rely on the structure and information present in a previous version. cURL [ec2-user ~]$ TOKEN=`curl -X PUT "http://169.254.169.254/latest/api/token" -H "X- aws-ec2-metadata-token-ttl-seconds: 21600"` \ && curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/ 1.0 2007-01-19 2007-03-01 2007-08-29 2007-10-10 2007-12-15 2008-02-01 2008-09-01 2009-04-04 2011-01-01 2011-05-01 2012-01-12 2014-02-25 2014-11-05 2015-10-20 2016-04-19

... latest PowerShell PS C:\> [string]$token = Invoke-RestMethod -Headers @{"X-aws-ec2-metadata-token-ttl- seconds" = "21600"} -Method PUT -Uri http://169.254.169.254/latest/api/token PS C:\> Invoke-RestMethod -Headers @{"X-aws-ec2-metadata-token" = $token} -Method GET -Uri http://169.254.169.254/ 1.0 2007-01-19 2007-03-01 2007-08-29 2007-10-10 2007-12-15 2008-02-01 2008-09-01 2009-04-04 2011-01-01 2011-05-01 2012-01-12 2014-02-25 2014-11-05 2015-10-20 2016-04-19 ... latest
##### Get the top-level metadata items This example gets the top-level metadata items. For more information about the items in the response, see Instance metadata categories.
Note that tags are included in this output only if you've allowed access. For more information, see the section called "Enable access to tags in instance metadata". cURL [ec2-user ~]$ TOKEN=`curl -X PUT "http://169.254.169.254/latest/api/token" -H "X- aws-ec2-metadata-token-ttl-seconds: 21600"` \

&& curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta- data/ ami-id ami-launch-index ami-manifest-path block-device-mapping/ events/ hostname iam/ instance-action instance-id instance-life-cycle instance-type local-hostname local-ipv4 mac metrics/ network/ placement/ profile public-hostname public-ipv4 public-keys/ reservation-id security-groups services/ tags/ PowerShell PS C:\> [string]$token = Invoke-RestMethod -Headers @{"X-aws-ec2-metadata-token-ttl- seconds" = "21600"} -Method PUT -Uri http://169.254.169.254/latest/api/token PS C:\> Invoke-RestMethod -Headers @{"X-aws-ec2-metadata-token" = $token} -Method GET -Uri http://169.254.169.254/latest/meta-data/ ami-id ami-launch-index ami-manifest-path block-device-mapping/ hostname iam/ instance-action instance-id

instance-life-cycle instance-type local-hostname local-ipv4 mac metrics/ network/ placement/ profile public-hostname public-ipv4 public-keys/ reservation-id security-groups services/ tags/
##### Get the values for metadata items These examples get the values of some of the top-level metadata items that were obtained in the preceding example. These requests use the stored token that was created using the command in the previous example. The token must not be expired. cURL [ec2-user ~]$ curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/ latest/meta-data/ami-id ami-0abcdef1234567890 [ec2-user ~]$ curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/ latest/meta-data/reservation-id r-0efghijk987654321 [ec2-user ~]$ curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/ latest/meta-data/local-hostname ip-10-251-50-12.ec2.internal [ec2-user ~]$ curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/ latest/meta-data/public-hostname ec2-203-0-113-25.compute-1.amazonaws.com

PowerShell PS C:\> Invoke-RestMethod -Headers @{"X-aws-ec2-metadata-token" = $token} -Method GET -Uri http://169.254.169.254/latest/meta-data/ami-id ami-0abcdef1234567890 PS C:\> Invoke-RestMethod -Headers @{"X-aws-ec2-metadata-token" = $token} -Method GET -Uri http://169.254.169.254/latest/meta-data/reservation-id r-0efghijk987654321 PS C:\> Invoke-RestMethod -Headers @{"X-aws-ec2-metadata-token" = $token} -Method GET -Uri http://169.254.169.254/latest/meta-data/local-hostname ip-10-251-50-12.ec2.internal PS C:\> Invoke-RestMethod -Headers @{"X-aws-ec2-metadata-token" = $token} -Method GET -Uri http://169.254.169.254/latest/meta-data/public-hostname ec2-203-0-113-25.compute-1.amazonaws.com
##### Get the list of available public keys This example gets the list of available public keys. cURL [ec2-user ~]$ TOKEN=`curl -X PUT "http://169.254.169.254/latest/api/token" -H "X- aws-ec2-metadata-token-ttl-seconds: 21600"` \ && curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta- data/public-keys/ 0=my-public-key PowerShell PS C:\> [string]$token = Invoke-RestMethod -Headers @{"X-aws-ec2-metadata-token-ttl- seconds" = "21600"} -Method PUT -Uri http://169.254.169.254/latest/api/token PS C:\> Invoke-RestMethod -Headers @{"X-aws-ec2-metadata-token" = $token} -Method GET -Uri http://169.254.169.254/latest/meta-data/public-keys/ 0=my-public-key

##### Show the formats in which public key 0 is available This example shows the formats in which public key 0 is available. cURL [ec2-user ~]$ TOKEN=`curl -X PUT "http://169.254.169.254/latest/api/token" -H "X- aws-ec2-metadata-token-ttl-seconds: 21600"` \ && curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta- data/public-keys/0/ openssh-key PowerShell PS C:\> [string]$token = Invoke-RestMethod -Headers @{"X-aws-ec2-metadata-token-ttl- seconds" = "21600"} -Method PUT -Uri http://169.254.169.254/latest/api/token PS C:\> Invoke-RestMethod -Headers @{"X-aws-ec2-metadata-token" = $token} -Method GET -Uri http://169.254.169.254/latest/meta-data/public-keys/0/openssh-key openssh-key
##### Get public key 0 (in the OpenSSH key format)
This example gets public key 0 (in the OpenSSH key format). cURL [ec2-user ~]$ TOKEN=`curl -X PUT "http://169.254.169.254/latest/api/token" -H "X- aws-ec2-metadata-token-ttl-seconds: 21600"` \ && curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta- data/public-keys/0/openssh-key ssh-rsa MIICiTCCAfICCQD6m7oRw0uXOjANBgkqhkiG9w0BAQUFADCBiDELMAkGA1UEBhMC VVMxCzAJBgNVBAgTAldBMRAwDgYDVQQHEwdTZWF0dGxlMQ8wDQYDVQQKEwZBbWF6 b24xFDASBgNVBAsTC0lBTSBDb25zb2xlMRIwEAYDVQQDEwlUZXN0Q2lsYWMxHzAd BgkqhkiG9w0BCQEWEG5vb25lQGFtYXpvbi5jb20wHhcNMTEwNDI1MjA0NTIxWhcN MTIwNDI0MjA0NTIxWjCBiDELMAkGA1UEBhMCVVMxCzAJBgNVBAgTAldBMRAwDgYD VQQHEwdTZWF0dGxlMQ8wDQYDVQQKEwZBbWF6b24xFDASBgNVBAsTC0lBTSBDb25z b2xlMRIwEAYDVQQDEwlUZXN0Q2lsYWMxHzAdBgkqhkiG9w0BCQEWEG5vb25lQGFt YXpvbi5jb20wgZ8wDQYJKoZIhvcNAQEBBQADgY0AMIGJAoGBAMaK0dn+a4GmWIWJ 21uUSfwfEvySWtC2XADZ4nB+BLYgVIk60CpiwsZ3G93vUEIO3IyNoH/f0wYK8m9T

rDHudUZg3qX4waLG5M43q7Wgc/MbQITxOUSQv7c7ugFFDzQGBzZswY6786m86gpE Ibb3OhjZnzcvQAaRHhdlQWIMm2nrAgMBAAEwDQYJKoZIhvcNAQEFBQADgYEAtCu4 nUhVVxYUntneD9+h8Mg9q6q+auNKyExzyLwaxlAoo7TJHidbtS4J5iNmZgXL0Fkb FFBjvSfpJIlJ00zbhNYS5f6GuoEDmFJl0ZxBHjJnyp378OD8uTs7fLvjx79LjSTb NYiytVbZPQUQ5Yaxu2jXnimvw3rrszlaEXAMPLE my-public-key PowerShell PS C:\> [string]$token = Invoke-RestMethod -Headers @{"X-aws-ec2-metadata-token-ttl- seconds" = "21600"} -Method PUT -Uri http://169.254.169.254/latest/api/token PS C:\> Invoke-RestMethod -Headers @{"X-aws-ec2-metadata-token" = $token} -Method GET -Uri http://169.254.169.254/latest/meta-data/public-keys/0/openssh-key ssh-rsa MIICiTCCAfICCQD6m7oRw0uXOjANBgkqhkiG9w0BAQUFADCBiDELMAkGA1UEBhMC VVMxCzAJBgNVBAgTAldBMRAwDgYDVQQHEwdTZWF0dGxlMQ8wDQYDVQQKEwZBbWF6 b24xFDASBgNVBAsTC0lBTSBDb25zb2xlMRIwEAYDVQQDEwlUZXN0Q2lsYWMxHzAd BgkqhkiG9w0BCQEWEG5vb25lQGFtYXpvbi5jb20wHhcNMTEwNDI1MjA0NTIxWhcN MTIwNDI0MjA0NTIxWjCBiDELMAkGA1UEBhMCVVMxCzAJBgNVBAgTAldBMRAwDgYD VQQHEwdTZWF0dGxlMQ8wDQYDVQQKEwZBbWF6b24xFDASBgNVBAsTC0lBTSBDb25z b2xlMRIwEAYDVQQDEwlUZXN0Q2lsYWMxHzAdBgkqhkiG9w0BCQEWEG5vb25lQGFt YXpvbi5jb20wgZ8wDQYJKoZIhvcNAQEBBQADgY0AMIGJAoGBAMaK0dn+a4GmWIWJ 21uUSfwfEvySWtC2XADZ4nB+BLYgVIk60CpiwsZ3G93vUEIO3IyNoH/f0wYK8m9T rDHudUZg3qX4waLG5M43q7Wgc/MbQITxOUSQv7c7ugFFDzQGBzZswY6786m86gpE Ibb3OhjZnzcvQAaRHhdlQWIMm2nrAgMBAAEwDQYJKoZIhvcNAQEFBQADgYEAtCu4 nUhVVxYUntneD9+h8Mg9q6q+auNKyExzyLwaxlAoo7TJHidbtS4J5iNmZgXL0Fkb FFBjvSfpJIlJ00zbhNYS5f6GuoEDmFJl0ZxBHjJnyp378OD8uTs7fLvjx79LjSTb NYiytVbZPQUQ5Yaxu2jXnimvw3rrszlaEXAMPLE my-public-key
##### Get the subnet ID for an instance This example gets the subnet ID for an instance. cURL [ec2-user ~]$ TOKEN=`curl -X PUT "http://169.254.169.254/latest/api/token" -H "X- aws-ec2-metadata-token-ttl-seconds: 21600"` \ && curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta- data/network/interfaces/macs/02:29:96:8f:6a:2d/subnet-id subnet-be9b61d7

PowerShell PS C:\> [string]$token = Invoke-RestMethod -Headers @{"X-aws-ec2-metadata-token-ttl- seconds" = "21600"} -Method PUT -Uri http://169.254.169.254/latest/api/token PS C:\> Invoke-RestMethod -Headers @{"X-aws-ec2-metadata-token" = $token} - Method GET -Uri http://169.254.169.254/latest/meta-data/network/interfaces/ macs/02:29:96:8f:6a:2d/subnet-id subnet-be9b61d7
##### Get the instance tags for an instance If access to instance tags in the instance metadata is turned on, you can get the tags for a instance from instance metadata. For more information, see Retrieve tags from instance metadata.
#### Examples for IMDSv1 Run the following examples on your Amazon EC2 instance to retrieve the instance metadata for IMDSv1.
On Windows instances, you can use Windows PowerShell or you can install cURL or wget. If you install a third-party tool on a Windows instance, ensure that you read the accompanying documentation carefully, as the calls and the output might be different from what is described here.
Examples
- Get the available versions of the instance metadata
- Get the top-level metadata items
- Get the values for metadata items
- Get the list of available public keys
- Show the formats in which public key 0 is available
- Get public key 0 (in the OpenSSH key format)
- Get the subnet ID for an instance
- Get the instance tags for an instance

##### Get the available versions of the instance metadata This example gets the available versions of the instance metadata. Each version refers to an instance metadata build when new instance metadata categories were released. The instance metadata build versions do not correlate with the Amazon EC2 API versions. The earlier versions are available to you in case you have scripts that rely on the structure and information present in a previous version. cURL [ec2-user ~]$ curl http://169.254.169.254/ 1.0 2007-01-19 2007-03-01 2007-08-29 2007-10-10 2007-12-15 2008-02-01 2008-09-01 2009-04-04 2011-01-01 2011-05-01 2012-01-12 2014-02-25 2014-11-05 2015-10-20 2016-04-19 ... latest PowerShell PS C:\> Invoke-RestMethod -uri http://169.254.169.254/ 1.0 2007-01-19 2007-03-01 2007-08-29 2007-10-10 2007-12-15 2008-02-01 2008-09-01 2009-04-04 2011-01-01

2011-05-01 2012-01-12 2014-02-25 2014-11-05 2015-10-20 2016-04-19 ... latest
##### Get the top-level metadata items This example gets the top-level metadata items. For more information about the items in the response, see Instance metadata categories.
Note that tags are included in this output only if you've allowed access. For more information, see the section called "Enable access to tags in instance metadata". cURL [ec2-user ~]$ curl http://169.254.169.254/latest/meta-data/ ami-id ami-launch-index ami-manifest-path block-device-mapping/ events/ hostname iam/ instance-action instance-id instance-type local-hostname local-ipv4 mac metrics/ network/ placement/ profile public-hostname public-ipv4 public-keys/ reservation-id security-groups

services/ tags/ PowerShell PS C:\> Invoke-RestMethod -uri http://169.254.169.254/latest/meta-data/ ami-id ami-launch-index ami-manifest-path block-device-mapping/ hostname iam/ instance-action instance-id instance-type local-hostname local-ipv4 mac metrics/ network/ placement/ profile public-hostname public-ipv4 public-keys/ reservation-id security-groups services/ tags/
##### Get the values for metadata items These examples get the values of some of the top-level metadata items that were obtained in the previous example. cURL [ec2-user ~]$ curl http://169.254.169.254/latest/meta-data/ami-id ami-0abcdef1234567890 [ec2-user ~]$ curl http://169.254.169.254/latest/meta-data/reservation-id

r-0efghijk987654321 [ec2-user ~]$ curl http://169.254.169.254/latest/meta-data/local-hostname ip-10-251-50-12.ec2.internal [ec2-user ~]$ curl http://169.254.169.254/latest/meta-data/public-hostname ec2-203-0-113-25.compute-1.amazonaws.com PowerShell PS C:\> Invoke-RestMethod -uri http://169.254.169.254/latest/meta-data/ami-id ami-0abcdef1234567890 PS C:\> Invoke-RestMethod -uri http://169.254.169.254/latest/meta-data/reservation- id r-0efghijk987654321 PS C:\> Invoke-RestMethod -uri http://169.254.169.254/latest/meta-data/local- hostname ip-10-251-50-12.ec2.internal PS C:\> Invoke-RestMethod -uri http://169.254.169.254/latest/meta-data/public- hostname ec2-203-0-113-25.compute-1.amazonaws.com
##### Get the list of available public keys This example gets the list of available public keys. cURL [ec2-user ~]$ curl http://169.254.169.254/latest/meta-data/public-keys/ 0=my-public-key PowerShell PS C:\> Invoke-RestMethod -uri http://169.254.169.254/latest/meta-data/public- keys/ 0=my-public-key

##### Show the formats in which public key 0 is available This example shows the formats in which public key 0 is available. cURL [ec2-user ~]$ curl http://169.254.169.254/latest/meta-data/public-keys/0/ openssh-key PowerShell PS C:\> Invoke-RestMethod -uri http://169.254.169.254/latest/meta-data/public- keys/0/openssh-key openssh-key
##### Get public key 0 (in the OpenSSH key format)
This example gets public key 0 (in the OpenSSH key format). cURL [ec2-user ~]$ curl http://169.254.169.254/latest/meta-data/public-keys/0/openssh-key ssh-rsa MIICiTCCAfICCQD6m7oRw0uXOjANBgkqhkiG9w0BAQUFADCBiDELMAkGA1UEBhMC VVMxCzAJBgNVBAgTAldBMRAwDgYDVQQHEwdTZWF0dGxlMQ8wDQYDVQQKEwZBbWF6 b24xFDASBgNVBAsTC0lBTSBDb25zb2xlMRIwEAYDVQQDEwlUZXN0Q2lsYWMxHzAd BgkqhkiG9w0BCQEWEG5vb25lQGFtYXpvbi5jb20wHhcNMTEwNDI1MjA0NTIxWhcN MTIwNDI0MjA0NTIxWjCBiDELMAkGA1UEBhMCVVMxCzAJBgNVBAgTAldBMRAwDgYD VQQHEwdTZWF0dGxlMQ8wDQYDVQQKEwZBbWF6b24xFDASBgNVBAsTC0lBTSBDb25z b2xlMRIwEAYDVQQDEwlUZXN0Q2lsYWMxHzAdBgkqhkiG9w0BCQEWEG5vb25lQGFt YXpvbi5jb20wgZ8wDQYJKoZIhvcNAQEBBQADgY0AMIGJAoGBAMaK0dn+a4GmWIWJ 21uUSfwfEvySWtC2XADZ4nB+BLYgVIk60CpiwsZ3G93vUEIO3IyNoH/f0wYK8m9T rDHudUZg3qX4waLG5M43q7Wgc/MbQITxOUSQv7c7ugFFDzQGBzZswY6786m86gpE Ibb3OhjZnzcvQAaRHhdlQWIMm2nrAgMBAAEwDQYJKoZIhvcNAQEFBQADgYEAtCu4 nUhVVxYUntneD9+h8Mg9q6q+auNKyExzyLwaxlAoo7TJHidbtS4J5iNmZgXL0Fkb FFBjvSfpJIlJ00zbhNYS5f6GuoEDmFJl0ZxBHjJnyp378OD8uTs7fLvjx79LjSTb NYiytVbZPQUQ5Yaxu2jXnimvw3rrszlaEXAMPLE my-public-key PowerShell PS C:\> Invoke-RestMethod -uri http://169.254.169.254/latest/meta-data/public- keys/0/openssh-key

ssh-rsa MIICiTCCAfICCQD6m7oRw0uXOjANBgkqhkiG9w0BAQUFADCBiDELMAkGA1UEBhMC VVMxCzAJBgNVBAgTAldBMRAwDgYDVQQHEwdTZWF0dGxlMQ8wDQYDVQQKEwZBbWF6 b24xFDASBgNVBAsTC0lBTSBDb25zb2xlMRIwEAYDVQQDEwlUZXN0Q2lsYWMxHzAd BgkqhkiG9w0BCQEWEG5vb25lQGFtYXpvbi5jb20wHhcNMTEwNDI1MjA0NTIxWhcN MTIwNDI0MjA0NTIxWjCBiDELMAkGA1UEBhMCVVMxCzAJBgNVBAgTAldBMRAwDgYD VQQHEwdTZWF0dGxlMQ8wDQYDVQQKEwZBbWF6b24xFDASBgNVBAsTC0lBTSBDb25z b2xlMRIwEAYDVQQDEwlUZXN0Q2lsYWMxHzAdBgkqhkiG9w0BCQEWEG5vb25lQGFt YXpvbi5jb20wgZ8wDQYJKoZIhvcNAQEBBQADgY0AMIGJAoGBAMaK0dn+a4GmWIWJ 21uUSfwfEvySWtC2XADZ4nB+BLYgVIk60CpiwsZ3G93vUEIO3IyNoH/f0wYK8m9T rDHudUZg3qX4waLG5M43q7Wgc/MbQITxOUSQv7c7ugFFDzQGBzZswY6786m86gpE Ibb3OhjZnzcvQAaRHhdlQWIMm2nrAgMBAAEwDQYJKoZIhvcNAQEFBQADgYEAtCu4 nUhVVxYUntneD9+h8Mg9q6q+auNKyExzyLwaxlAoo7TJHidbtS4J5iNmZgXL0Fkb FFBjvSfpJIlJ00zbhNYS5f6GuoEDmFJl0ZxBHjJnyp378OD8uTs7fLvjx79LjSTb NYiytVbZPQUQ5Yaxu2jXnimvw3rrszlaEXAMPLE my-public-key
##### Get the subnet ID for an instance This example gets the subnet ID for an instance. cURL [ec2-user ~]$ curl http://169.254.169.254/latest/meta-data/network/interfaces/ macs/02:29:96:8f:6a:2d/subnet-id subnet-be9b61d7 PowerShell PS C:\> Invoke-RestMethod -uri http://169.254.169.254/latest/meta-data/network/ interfaces/macs/02:29:96:8f:6a:2d/subnet-id subnet-be9b61d7
##### Get the instance tags for an instance If access to instance tags in the instance metadata is turned on, you can get the tags for a instance from instance metadata. For more information, see Retrieve tags from instance metadata.
### Transition to using Instance Metadata Service Version 2 If you want to configure your instances to only accept Instance Metadata Service Version 2 (IMDSv2) calls, we recommend that you use the following tools and transition path.

Topics
- Tools for transitioning to IMDSv2
- Recommended path to requiring IMDSv2
#### Tools for transitioning to IMDSv2 The following tools can help you identify, monitor, and manage the transition of your software from IMDSv1 to IMDSv2. For the instructions on how to use these tools, see Recommended path to requiring IMDSv2.
AWS software The latest versions of the AWS CLI and AWS SDKs support IMDSv2. To use IMDSv2, update your EC2 instances to use the latest versions. For the minimum AWS SDK versions that support IMDSv2, see Use a supported AWS SDK.
All Amazon Linux 2 and Amazon Linux 2023 software packages support IMDSv2. Amazon Linux 2023 disables IMDSv1 by default.
IMDS Packet Analyzer IMDS Packet Analyzer is an open-source tool that identifies and logs IMDSv1 calls during your instance's boot phase and runtime operations. By analyzing these logs, you can precisely identify the software making IMDSv1 calls on your instances and determine what needs to be updated to support IMDSv2 only on your instances. You can run IMDS Packet Analyzer from a command line or install it as a service. For more information, see AWS ImdsPacketAnalyzer on GitHub.
CloudWatch CloudWatch provides the following two metrics for monitoring your instances:
MetadataNoToken – IMDSv2 uses token-backed sessions, while IMDSv1 does not. The MetadataNoToken metric tracks the number of calls to the Instance Metadata Service (IMDS) that are using IMDSv1. By tracking this metric to zero, you can determine if and when all of your software has been upgraded to use IMDSv2.
MetadataNoTokenRejected – After you've disabled IMDSv1, you can use the MetadataNoTokenRejected metric to track the number of times an IMDSv1 call was

attempted and rejected. By tracking this metric, you can ascertain whether your software needs to be updated to use IMDSv2.
For more information, see Instance metrics.
Launch APIs New instances: Use the RunInstances API to launch new instances that require the use of IMDSv2. For more information, see Configure instance metadata options for new instances.
Existing instances: Use the ModifyInstanceMetadataOptions API to require the use of IMDSv2 on existing instances. For more information, see Modify instance metadata options for existing instances.
New instances launched by Auto Scaling groups: To require the use of IMDSv2 on all new instances launched by Auto Scaling groups, your Auto Scaling groups can use either a launch template or a launch configuration. When you create a launch template or create a launch configuration, you must configure the MetadataOptions parameters to require the use of IMDSv2. The Auto Scaling group launches new instances using the new launch template or launch configuration, but existing instances are not affected.
Existing instances in an Auto Scaling group: Use the ModifyInstanceMetadataOptions API to require the use of IMDSv2 on existing instances, or terminate the instances and the Auto Scaling group will launch new replacement instances with the instance metadata options settings that are defined in the new launch template or launch configuration.
AMIs AMIs configured with the ImdsSupport parameter set to v2.0 will launch instances that require IMDSv2 by default. Amazon Linux 2023 is configured with ImdsSupport = v2.0.
New AMIs: Use the register-image CLI command to set the ImdsSupport parameter to v2.0 when creating a new AMI.
Existing AMIs: Use the modify-image-attribute CLI command to set the ImdsSupport parameter to v2.0 when modifying an existing AMI.
For more information, see Configure the AMI.
IAM policies and SCPs You can use an IAM policy or AWS Organizations service control policy (SCP) to control users as follows:

- Can't launch an instance using the RunInstances API unless the instance is configured to use IMDSv2.
- Can't modify a running instance using the ModifyInstanceMetadataOptions API to re-enable IMDSv1.
The IAM policy or SCP must contain the following IAM condition keys:
- ec2:MetadataHttpEndpoint
- ec2:MetadataHttpPutResponseHopLimit
- ec2:MetadataHttpTokens If a parameter in the API or CLI call doesn't match the state specified in the policy that contains the condition key, the API or CLI call fails with an UnauthorizedOperation response.
Furthermore, you can choose an additional layer of protection to enforce the change from IMDSv1 to IMDSv2. At the access management layer with respect to the APIs called via EC2 Role credentials, you can use a condition key in either IAM policies or AWS Organizations service control policies (SCPs). Specifically, by using the condition key ec2:RoleDelivery with a value of 2.0 in your IAM policies, API calls made with EC2 Role credentials obtained from IMDSv1 will receive an UnauthorizedOperation response. The same thing can be achieved more broadly with that condition required by an SCP. This ensures that credentials delivered via IMDSv1 cannot actually be used to call APIs because any API calls not matching the specified condition will receive an UnauthorizedOperation error.
For example IAM policies, see Work with instance metadata. For more information on SCPs, see Service control policies in the AWS Organizations User Guide.
Declarative Policies Use Declarative Policies (a feature of AWS Organizations) to centrally set and enforce IMDSv2 as the default IMDS version across your organization. For an example policy, see the Instance Metadata Defaults tab in the Supported declarative policies section in the AWS Organizations User Guide.
#### Recommended path to requiring IMDSv2 Using the above tools, we recommend the following path for transitioning to IMDSv2:
- Step 1: Identify instances with IMDSv2=optional and audit IMDSv1 usage
- Step 2: Update software to IMDSv2

- Step 3: Require IMDSv2 on instances
- Step 4: Set IMDSv2=required as the default
- Step 5: Enforce instances to require IMDSv2
##### Step 1: Identify instances with IMDSv2=optional and audit IMDSv1 usage To assess your IMDSv2 migration scope, identify instances that are configured to allow either IMDSv1 or IMDSv2, and audit IMDSv1 calls.
1. Identify instances that are configured to allow either IMDSv1 or IMDSv2:
Amazon EC2 console
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Instances.
3. To see only the instances that are configured to allow IMDSv1 or IMDSv2, add the filter IMDSv2 = optional.
4. Alternatively, to see whether IMDSv2 is optional or required for all instances, open the Preferences window (gear icon), toggle on IMDSv2, and choose Confirm. This adds the IMDSv2 column to the Instances table.
AWS CLI Use the describe-instances command and filter by metadata-options.http-tokens = optional, as follows: aws ec2 describe-instances --filters "Name=metadata-options.http- tokens,Values=optional" --query "Reservations[*].Instances[*].[InstanceId]" -- output text
2. Audit IMDSv1 calls on each instance:
Use the CloudWatch metric MetadataNoToken. This metric shows the number of IMDSv1 calls to the IMDS on your instances. For more information, see Instance metrics.
3. Identify software on your instances making IMDSv1 calls:
Use the open source IMDS Packet Analyzer to identify and log IMDSv1 calls during your instance's boot phase and runtime operations. Use this information to identify the software to

update to get your instances ready to use IMDSv2 only. You can run IMDS Packet Analyzer from a command line or install it as a service.
##### Step 2: Update software to IMDSv2 Update all SDKs, CLIs, and software that use Role credentials on your instances to IMDSv2- compatible versions. For more information about updating the CLI, see Installing or updating to the latest version of the AWS CLI in the AWS Command Line Interface User Guide.
##### Step 3: Require IMDSv2 on instances After confirming zero IMDSv1 calls through the MetadataNoToken metric, configure your existing instances to require IMDSv2. Also, configure all new instances to require IMDSv2. In other words, disable IMDSv1 on all existing and new instances.
1. Configure existing instances to require IMDSv2:
Amazon EC2 console
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Instances.
3. Select your instance.
4. Choose Actions, Instance settings, Modify instance metadata options.
5. For IMDSv2, choose Required.
6. Choose Save.
AWS CLI Use the modify-instance-metadata-options CLI command to specify that only IMDSv2 is to be used.
Note You can modify this setting on running instances. The change takes effect immediately without needing an instance restart.

For more information, see Require the use of IMDSv2.
2. Monitor for issues after disabling IMDSv1:
1. Track the number of times an IMDSv1 call was attempted and rejected with the MetadataNoTokenRejected CloudWatch metric.
2. If the MetadataNoTokenRejected metric records IMDSv1 calls on an instance that is experiencing software issues, this indicates that the software requires updating to use IMDSv2.
3. Configure new instances to require IMDSv2:
Amazon EC2 console
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. Follow the steps to launch an instance.
3. Expand Advanced details, and for Metadata version, choose V2 only (token required).
4. In the Summary panel, review your instance configuration, and then choose Launch instance.
For more information, see Configure the instance at launch.
AWS CLI AWS CLI: Use the run-instances command and specify that IMDSv2 is required.
##### Step 4: Set IMDSv2=required as the default You can set IMDSv2=required as the default configuration at either the account or organization level. This ensures that all newly launched instances are automatically configured to require IMDSv2.
1. Set account-level default:
Amazon EC2 console
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. On the EC2 Dashboard, under Account attributes, choose Data protection and security.

3. Under IMDS defaults, choose Manage.
4. For Instance metadata service , choose Enabled.
5. For Metadata version, choose to V2 only (token required).
6. Choose Update.
AWS CLI Use the modify-instance-metadata-defaults CLI command and specify --http-tokens required and --http-put-response-hop-limit 2.
For more information, see Set IMDSv2 as the default for the account.
2. Alternatively, set organization-level default using a Declarative Policy:
Use a Declarative Policy to set the organization default for IMDSv2 to required. For an example policy, see the Instance Metadata Defaults tab in the Supported declarative policies section in the AWS Organizations User Guide.
##### Step 5: Enforce instances to require IMDSv2 Use the following IAM or SCP condition keys to enforce IMDSv2 usage:
- ec2:MetadataHttpTokens
- ec2:MetadataHttpPutResponseHopLimit
- ec2:MetadataHttpEndpoint These condition keys control the use of the RunInstances and the ModifyInstanceMetadataOptions APIs and corresponding CLIs. If a policy is created, and a parameter in the API call does not match the state specified in the policy using the condition key, the API or CLI call fails with an UnauthorizedOperation response.
For example IAM policies, see Work with instance metadata.
### Limit access to the Instance Metadata Service You can consider using local firewall rules to disable access from some or all processes to the Instance Metadata Service (IMDS).

For Nitro-based instances, the IMDS can be reached from your own network when a network appliance within your VPC, such as a virtual router, forwards packets to the IMDS address, and the default source/destination check on the instance is disabled. To prevent a source from outside your VPC reaching the IMDS, we recommend that you modify the configuration of the network appliance to drop packets with the destination IPv4 address of the IMDS 169.254.169.254 and, if you enabled the IPv6 endpoint, the IPv6 address of the IMDS [fd00:ec2::254].
#### Limit IMDS access for Linux instances Using iptables to limit access The following example uses Linux iptables and its owner module to prevent the Apache webserver (based on its default installation user ID of apache) from accessing 169.254.169.254. It uses a deny rule to reject all instance metadata requests (whether IMDSv1 or IMDSv2) from any process running as that user.
$ sudo iptables --append OUTPUT --proto tcp --destination 169.254.169.254 --match owner --uid-owner apache --jump REJECT Or, you can consider only allowing access to particular users or groups, by using allow rules. Allow rules might be easier to manage from a security perspective, because they require you to make a decision about what software needs access to instance metadata. If you use allow rules, it's less likely you will accidentally allow software to access the metadata service (that you did not intend to have access) if you later change the software or configuration on an instance. You can also combine group usage with allow rules, so that you can add and remove users from a permitted group without needing to change the firewall rule.
The following example prevents access to the IMDS by all processes, except for processes running in the user account trustworthy-user.
$ sudo iptables --append OUTPUT --proto tcp --destination 169.254.169.254 --match owner ! --uid-owner trustworthy-user --jump REJECT Note
- To use local firewall rules, you need to adapt the preceding example commands to suit your needs.
- By default, iptables rules are not persistent across system reboots. They can be made to be persistent by using OS features, not described here.

- The iptables owner module only matches group membership if the group is the primary group of a given local user. Other groups are not matched.
Using PF or IPFW to limit access If you are using FreeBSD or OpenBSD, you can also consider using PF or IPFW. The following examples limit access to the IMDS to just the root user.
PF $ block out inet proto tcp from any to 169.254.169.254 $ pass out inet proto tcp from any to 169.254.169.254 user root IPFW $ allow tcp from any to 169.254.169.254 uid root $ deny tcp from any to 169.254.169.254 Note The order of the PF and IPFW commands matter. PF defaults to last matching rule and IPFW defaults to first matching rule.
#### Limit IMDS access for Windows instances Using Windows firewall to limit access The following PowerShell example uses the built-in Windows firewall to prevent the Internet Information Server webserver (based on its default installation user ID of NT AUTHORITY\IUSR) from accessing 169.254.169.254. It uses a deny rule to reject all instance metadata requests (whether IMDSv1 or IMDSv2) from any process running as that user.
PS C:\> $blockPrincipal = New-Object -TypeName System.Security.Principal.NTAccount ("NT AUTHORITY\IUSR")

PS C:\> $BlockPrincipalSID = $blockPrincipal.Translate([System.Security.Principal.SecurityIdentifier]).Value PS C:\> $BlockPrincipalSDDL = "D:(A;;CC;;;$BlockPrincipalSID)"
PS C:\> New-NetFirewallRule -DisplayName "Block metadata service from IIS" -Action block -Direction out `
-Protocol TCP -RemoteAddress 169.254.169.254 -LocalUser $BlockPrincipalSDDL Or, you can consider only allowing access to particular users or groups, by using allow rules. Allow rules might be easier to manage from a security perspective, because they require you to make a decision about what software needs access to instance metadata. If you use allow rules, it's less likely you will accidentally allow software to access the metadata service (that you did not intend to have access) if you later change the software or configuration on an instance. You can also combine group usage with allow rules, so that you can add and remove users from a permitted group without needing to change the firewall rule.
The following example prevents access to instance metadata by all processes running as an OS group specified in the variable blockPrincipal (in this example, the Windows group Everyone), except for processes specified in exceptionPrincipal (in this example, a group called trustworthy-users). You must specify both deny and allow principals because Windows Firewall, unlike the ! --uid-owner trustworthy-user rule in Linux iptables, does not provide a shortcut mechanism to allow only a particular principal (user or group) by denying all the others.
PS C:\> $blockPrincipal = New-Object -TypeName System.Security.Principal.NTAccount ("Everyone")
PS C:\> $BlockPrincipalSID = $blockPrincipal.Translate([System.Security.Principal.SecurityIdentifier]).Value PS C:\> $exceptionPrincipal = New-Object -TypeName System.Security.Principal.NTAccount ("trustworthy-users")
PS C:\> $ExceptionPrincipalSID = $exceptionPrincipal.Translate([System.Security.Principal.SecurityIdentifier]).Value PS C:\> $PrincipalSDDL = "O:LSD:(D;;CC;;;$ExceptionPrincipalSID)(A;;CC;;; $BlockPrincipalSID)"
PS C:\> New-NetFirewallRule -DisplayName "Block metadata service for $($blockPrincipal.Value), exception: $($exceptionPrincipal.Value)" -Action block - Direction out `
-Protocol TCP -RemoteAddress 169.254.169.254 -LocalUser $PrincipalSDDL

Note To use local firewall rules, you need to adapt the preceding example commands to suit your needs.
Using netsh rules to limit access You can consider blocking all software using netsh rules, but those are much less flexible.
C:\> netsh advfirewall firewall add rule name="Block metadata service altogether" dir=out protocol=TCP remoteip=169.254.169.254 action=block Note
- To use local firewall rules, you need to adapt the preceding example commands to suit your needs.
- netsh rules must be set from an elevated command prompt, and can't be set to deny or allow particular principals.
## Configure the Instance Metadata Service options The Instance Metadata Service (IMDS) runs locally on every EC2 instance. The instance metadata options refer to a set of configurations that control the accessibility and behavior of the IMDS on an EC2 instance.
You can configure the following instance metadata options on each instance:
Instance metadata service (IMDS): enabled | disabled You can enable or disable the IMDS on an instance. When disabled, you or any code won't be able to access the instance metadata on the instance.
The IMDS has two endpoints on an instance: IPv4 (169.254.169.254) and IPv6 ([fd00:ec2::254]). When you enable the IMDS, the IPv4 endpoint is automatically enabled. If you want to enable the IPv6 endpoint, you need to do so explicitly.

IMDS IPv6 endpoint: enabled | disabled You can explicitly enable the IPv6 IMDS endpoint on an instance. When the IPv6 endpoint is enabled, the IPv4 endpoint remains enabled. The IPv6 endpoint is only supported on Nitro- based instances in IPv6-supported subnets (dual stack or IPv6 only).
Metadata version: IMDSv1 or IMDSv2 (token optional) | IMDSv2 only (token required)
When requesting instance metadata, IMDSv2 calls require a token. IMDSv1 calls do not require a token. You can configure an instance to allow either IMDSv1 or IMDSv2 calls (where a token is optional), or to only allow IMDSv2 calls (where a token is required).
Metadata response hop limit: 1–64 The hop limit is the number of network hops that the PUT response is allowed to make. You can set the hop limit to a minimum of 1 and a maximum of 64. In a container environment, a hop limit of 1 can cause issues. For information about how to mitigate these issues, see the information about container environments under Instance metadata access considerations.
Access to tags in instance metadata: enabled | disabled You can enable or disable access to the instance's tags from an instance's metadata. For more information, see View tags for your EC2 instances using instance metadata.
To view an instance's current configuration, see Query instance metadata options for existing instances.
### Where to configure instance metadata options Instance metadata options can be configured at different levels, as follows:
- Account – You can set default values for the instance metadata options at the account level for each AWS Region. When an instance is launched, the instance metadata options are automatically set to the account-level values. You can change these values at launch. Account- level default values do not affect existing instances.
- AMI – You can set the imds-support parameter to v2.0 when you register or modify an AMI.
When an instance is launched with this AMI, the instance metadata version is automatically set to IMDSv2 and the hop limit is set to 2.

- Instance – You can change all the instance metadata options on an instance at launch, overriding the default settings. You can also change the instance metadata options after launch on a running or stopped instance. Note that changes may be restricted by an IAM or SCP policy.
For more information, see Configure instance metadata options for new instances and Modify instance metadata options for existing instances.
### Order of precedence for instance metadata options The value for each instance metadata option is determined at instance launch, following a hierarchical order of precedence. The hierarchy, with the highest precedence at the top, is as follows:
- Precedence 1: Instance configuration at launch – Values can be specified either in the launch template or in the instance configuration. Any values specified here override values specified at the account level or in the AMI.
- Precedence 2: Account settings – If a value is not specified at instance launch, then it is determined by the account-level settings (which are set for each AWS Region). Account-level settings either include a value for each metadata option, or indicate no preference at all.
- Precedence 3: AMI configuration – If a value is not specified at instance launch or at the account level, then it is determined by the AMI configuration. This applies only to HttpTokens and HttpPutResponseHopLimit.
Each metadata option is evaluated separately. The instance can be configured with a mix of direct instance configuration, account-level defaults, and the configuration from the AMI.
You can change the value of any metadata option after launch on a running or stopped instance, unless changes are restricted by an IAM or SCP policy.
Determine values for metadata options – Example 1 In this example, an EC2 instance is launched into a Region where the HttpPutResponseHopLimit is set to 1 at the account level. The specified AMI has ImdsSupport set to v2.0. No metadata options are specified directly on the instance at launch. The instance is launched with the following metadata options:
"MetadataOptions": { ...

    "HttpTokens": "required", "HttpPutResponseHopLimit": 1, ...
These values were determined as follows:
- No metadata options specified at launch: During the launch of the instance, specific values for the metadata options were not provided either in the instance launch parameters or in the launch template.
- Account settings take next precedence: In the absence of specific values specified at launch, the settings at the account level within the Region take precedence. This means that the default values configured at the account level are applied. In this case, the HttpPutResponseHopLimit was set to 1.
- AMI settings take last precedence: In the absence of a specific value specified at launch or at the account level for HttpTokens (the instance metadata version), the AMI setting is applied. In this case, the AMI setting ImdsSupport: v2.0 determined that HttpTokens was set to required. Note that while the AMI setting ImdsSupport: v2.0 is designed to set HttpPutResponseHopLimit: 2, it was overridden by the account-level setting HttpPutResponseHopLimit: 1, which has higher precedence.
Determine values for metadata options – Example 2 In this example, the EC2 instance is launched with the same settings as in the previous Example 1, but with HttpTokens set to optional directly on the instance at launch. The instance is launched with the following metadata options:
"MetadataOptions": { ...
    "HttpTokens": "optional", "HttpPutResponseHopLimit": 1, ...
The value for HttpPutResponseHopLimit is determined in the same way as in Example 1.
However, the value for HttpTokens is determined as follows: Metadata options configured on the instance at launch take first precedence. Even though the AMI was configured with ImdsSupport: v2.0 (in other words, HttpTokens is set to required), the value specified on the instance at launch (HttpTokens set to optional) took precedence.

#### Set the instance metadata version When an instance is launched, the value for the instance metadata version is either IMDSv1 or IMDSv2 (token optional) or IMDSv2 only (token required).
At instance launch, you can either manually specify the value for the metadata version, or use the default value. If you manually specify the value, it overrides any defaults. If you opt not to manually specify the value, it will be determined by a combination of default settings, as outlined in the following table.
The table shows how the metadata version for an instance at launch (indicated by Resulting instance configuration in column 4) is determined by the settings at the different levels of configuration. The order of precedence is from left to right, where the first column takes the highest precedence, as follows:
- Column 1: Launch parameter – Represents the setting on the instance that you manually specify at launch.
- Column 2: Account level default – Represents the setting for the account.
- Column 3: AMI default – Represents the setting on the AMI.
Launch parameter Account level default AMI default Resulting instance configuration V2 only (token required)
No preference V2 only V2 only V2 only (token required)
V2 only V2 only V2 only V2 only (token required)
V1 or V2 V2 only V2 only V1 or V2 (token optional)
No preference V2 only V1 or V2 V1 or V2 (token optional)
V2 only V2 only V1 or V2

Launch parameter Account level default AMI default Resulting instance configuration V1 or V2 (token optional)
V1 or V2 V2 only V1 or V2 Not set No preference V2 only V2 only Not set V2 only V2 only V2 only Not set V1 or V2 V2 only V1 or V2 V2 only (token required)
No preference null V2 only V2 only (token required)
V2 only null V2 only V2 only (token required)
V1 or V2 null V2 only V1 or V2 (token optional)
No preference null V1 or V2 V1 or V2 (token optional)
V2 only null V1 or V2 V1 or V2 (token optional)
V1 or V2 null V1 or V2 Not set No preference null V1 or V2 Not set V2 only null V2 only Not set V1 or V2 null V1 or V2
### Use IAM condition keys to restrict instance metadata options You can use IAM condition keys in an IAM policy or SCP as follows:

- Allow an instance to launch only if it's configured to require the use of IMDSv2
- Restrict the number of allowed hops
- Turn off access to instance metadata Tasks
- Configure instance metadata options for new instances
- Modify instance metadata options for existing instances Note You should proceed cautiously and conduct careful testing before making any changes.
Take note of the following:
- If you enforce the use of IMDSv2, applications or agents that use IMDSv1 for instance metadata access will break.
- If you turn off all access to instance metadata, applications or agents that rely on instance metadata access to function will break.
- For IMDSv2, you must use /latest/api/token when retrieving the token.
- (Windows only) If your PowerShell version is earlier than 4.0, you must update to Windows Management Framework 4.0 to require the use of IMDSv2.
### Configure instance metadata options for new instances You can configure the following instance metadata options for new instances.
Options
- Require the use of IMDSv2
- Enable the IMDS IPv4 and IPv6 endpoints
- Turn off access to instance metadata
- Allow access to tags in instance metadata

Note The settings for these options are configured at the account level, either directly in the account or by using a declarative policy. They must be configured in each AWS Region where you want to configure instance metadata options. Using a declarative policy allows you to apply the settings across multiple Regions simultaneously, as well as across multiple accounts simultaneously. When a declarative policy is in use, you can't modify the settings directly within an account. This topic describes how to configure the settings directly within an account. For information about using declarative policies, see Declarative policies in the AWS Organizations User Guide.
#### Require the use of IMDSv2 You can use the following methods to require the use of IMDSv2 on your new instances.
To require IMDSv2
- Set IMDSv2 as the default for the account
- Configure the instance at launch
- Configure the AMI
- Use an IAM policy
##### Set IMDSv2 as the default for the account You can set the default version for the instance metadata service (IMDS) at the account level for each AWS Region. This means that when you launch a new instance, the instance metadata version is automatically set to the account-level default. However, you can manually override the value at launch or after launch. For more information about how the account-level settings and manual overrides affect an instance, see Order of precedence for instance metadata options.
Note Setting the account-level default does not reset existing instances. For example, if you set the account-level default to IMDSv2, any existing instances that are set to IMDSv1 are not affected. If you want to change the value on existing instances, you must manually change the value on the instances themselves.

You can set the account default for the instance metadata version to IMDSv2 so that all new instances in the account launch with IMDSv2 required, and IMDSv1 will be disabled. With this account default, when you launch an instance, the following are the default values for the instance:
- Console: Metadata version is set to V2 only (token required) and Metadata response hop limit is set to 2.
- AWS CLI: HttpTokens is set to required and HttpPutResponseHopLimit is set to 2.
Note Before setting the account default to IMDSv2, ensure that your instances do not depend on IMDSv1. For more information, see Recommended path to requiring IMDSv2.
Console To set IMDSv2 as the default for the account for the specified Region
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. To change the AWS Region, use the Region selector in the upper-right corner of the page.
3. In the navigation pane, choose EC2 Dashboard.
4. Under Account attributes, choose Data protection and security.
5. Next to IMDS defaults, choose Manage.
6. On the Manage IMDS defaults page, do the following: a.
For Instance metadata service, choose Enabled. b.
For Metadata version, choose V2 only (token required). c.
For Metadata response hop limit, specify 2 if your instances will host containers.
Otherwise, select No preference. When no preference is specified, at launch, the value defaults to 2 if the AMI has the setting ImdsSupport: v2.0; otherwise it defaults to
1. d.
Choose Update.
AWS CLI To set IMDSv2 as the default for the account for the specified Region

Use the modify-instance-metadata-defaults command and specify the Region in which to modify the IMDS account level settings. Include --http-tokens set to required and -- http-put-response-hop-limit set to 2 if your instances will host containers. Otherwise, specify -1 to indicate no preference. When -1 (no preference) is specified, at launch, the value defaults to 2 if the AMI has the setting ImdsSupport: v2.0; otherwise it defaults to 1. aws ec2 modify-instance-metadata-defaults \ --region us-east-1 \ --http-tokens required \ --http-put-response-hop-limit 2 The following is example output.
{ "Return": true } To view the default account settings for the instance metadata options for the specified Region Use the get-instance-metadata-defaults command and specify the Region. aws ec2 get-instance-metadata-defaults --region us-east-1 The following is example output.
{ "AccountLevel": { "HttpTokens": "required", "HttpPutResponseHopLimit": 2 }, "ManagedBy": "account"
} The ManagedBy field indicates the entity that configured the settings. In this example, account indicates that the settings were configured directly in the account. A value of declarative-policy would mean the settings were configured by a declarative policy. For more information, see Declarative policies in the AWS Organizations User Guide.
To set IMDSv2 as the default for the account for all Regions

Use the modify-instance-metadata-defaults command to modify the IMDS account level settings for all Regions. Include --http-tokens set to required and --http-put- response-hop-limit set to 2 if your instances will host containers. Otherwise, specify -1 to indicate no preference. When -1 (no preference) is specified, at launch, the value defaults to 2 if the AMI has the setting ImdsSupport: v2.0; otherwise it defaults to 1. echo -e "Region          \t Modified" ; \ echo -e "--------------  \t ---------" ; \ for region in $( aws ec2 describe-regions \ --region us-east-1 \ --query "Regions[*].[RegionName]" \ --output text ); do (output=$( aws ec2 modify-instance-metadata-defaults \ --region $region \ --http-tokens required \ --http-put-response-hop-limit 2 \ --output text) echo -e "$region        \t $output"
    ); done The following is example output.
Region                   Modified --------------           --------- ap-south-1               True eu-north-1               True eu-west-3                True ...
To view the default account settings for the instance metadata options for all Regions Use the get-instance-metadata-defaults command. echo -e "Region   \t Level          Hops    HttpTokens" ; \ echo -e "-------------- \t ------------   ----    ----------" ; \ for region in $( aws ec2 describe-regions \ --region us-east-1 \

        --query "Regions[*].[RegionName]" \ --output text ); do (output=$( aws ec2 get-instance-metadata-defaults \ --region $region \ --output text) echo -e "$region \t $output"
    ); done The following is example output.
Region           Level          Hops    HttpTokens --------------   ------------   ----    ---------- ap-south-1       ACCOUNTLEVEL   2       required eu-north-1       ACCOUNTLEVEL   2       required eu-west-3        ACCOUNTLEVEL   2       required ...
PowerShell To set IMDSv2 as the default for the account for the specified Region Use the Edit-EC2InstanceMetadataDefault command and specify the Region in which to modify the IMDS account level settings. Include -HttpToken set to required and - HttpPutResponseHopLimit set to 2 if your instances will host containers. Otherwise, specify -1 to indicate no preference. When -1 (no preference) is specified, at launch, the value defaults to 2 if the AMI has the setting ImdsSupport: v2.0; otherwise it defaults to 1.
Edit-EC2InstanceMetadataDefault `
    -Region us-east-1 `
    -HttpToken required `
    -HttpPutResponseHopLimit 2 The following is example output.
True To view the default account settings for the instance metadata options for the specified Region

Use the Get-EC2InstanceMetadataDefault command and specify the Region.
Get-EC2InstanceMetadataDefault -Region us-east-1 | Format-List The following is example output.
HttpEndpoint            :
HttpPutResponseHopLimit : 2 HttpTokens              : required InstanceMetadataTags    :
To set IMDSv2 as the default for the account for all Regions Use the Edit-EC2InstanceMetadataDefault Cmdlet to modify the IMDS account level settings for all Regions. Include -HttpToken set to required and -HttpPutResponseHopLimit set to 2 if your instances will host containers. Otherwise, specify -1 to indicate no preference. When -1 (no preference) is specified, at launch, the value defaults to 2 if the AMI has the setting ImdsSupport: v2.0; otherwise it defaults to 1.
(Get-EC2Region).RegionName | `
    ForEach-Object { [PSCustomObject]@{ Region   = $_ Modified = (Edit-EC2InstanceMetadataDefault `
                -Region $_ `
                -HttpToken required `
                -HttpPutResponseHopLimit 2)
    } } | `
Format-Table Region, Modified -AutoSize Expected output Region         Modified ------         -------- ap-south-1         True eu-north-1         True eu-west-3          True ...
To view the default account settings for the instance metadata options for all Regions

Use the Get-EC2InstanceMetadataDefault Cmdlet.
(Get-EC2Region).RegionName | `
    ForEach-Object { [PSCustomObject]@{ Region = $_ HttpPutResponseHopLimit = (Get-EC2InstanceMetadataDefault -Region $_).HttpPutResponseHopLimit HttpTokens              = (Get-EC2InstanceMetadataDefault -Region $_).HttpTokens } } | `
Format-Table -AutoSize Example output Region         HttpPutResponseHopLimit HttpTokens ------         ----------------------- ---------- ap-south-1                           2 required eu-north-1                           2 required eu-west-3                            2 required ...
##### Configure the instance at launch When you launch an instance, you can configure the instance to require the use of IMDSv2 by configuring the following fields:
- Amazon EC2 console: Set Metadata version to V2 only (token required).
- AWS CLI: Set HttpTokens to required.
When you specify that IMDSv2 is required, you must also enable the Instance Metadata Service (IMDS) endpoint by setting Metadata accessible to Enabled (console) or HttpEndpoint to enabled (AWS CLI).
In a container environment, when IMDSv2 is required, we recommend setting the hop limit to 2.
For more information, see Instance metadata access considerations.

Console To require the use of IMDSv2 on a new instance
- When launching a new instance in the Amazon EC2 console, expand Advanced details, and do the following:
- For Metadata accessible, choose Enabled.
- For Metadata version, choose V2 only (token required).
- (Container environment) For Metadata response hop limit, choose 2.
For more information, see Advanced details.
AWS CLI To require the use of IMDSv2 on a new instance The following run-instances example launches a c6i.large instance with --metadata- options set to HttpTokens=required. When you specify a value for HttpTokens, you must also set HttpEndpoint to enabled. Because the secure token header is set to required for metadata retrieval requests, this requires the instance to use IMDSv2 when requesting instance metadata.
In a container environment, when IMDSv2 is required, we recommend setting the hop limit to 2 with HttpPutResponseHopLimit=2. aws ec2 run-instances \ --image-id ami-0abcdef1234567890 \ --instance-type c6i.large \ ...
    --metadata-options "HttpEndpoint=enabled,HttpTokens=required,HttpPutResponseHopLimit=2"
PowerShell To require the use of IMDSv2 on a new instance The following New-EC2Instance Cmdlet example launches a c6i.large instance with MetadataOptions_HttpEndpoint set to enabled and the MetadataOptions_HttpTokens parameter to required. When you specify a value for

HttpTokens, you must also set HttpEndpoint to enabled. Because the secure token header is set to required for metadata retrieval requests, this requires the instance to use IMDSv2 when requesting instance metadata.
New-EC2Instance `
    -ImageId ami-0abcdef1234567890 `
    -InstanceType c6i.large `
    -MetadataOptions_HttpEndpoint enabled `
    -MetadataOptions_HttpTokens required CloudFormation To specify the metadata options for an instance using CloudFormation, see the AWS::EC2::LaunchTemplate MetadataOptions property in the AWS CloudFormation User Guide.
##### Configure the AMI When you register a new AMI or modify an existing AMI, you can set the imds-support parameter to v2.0. Instances launched from this AMI will have Metadata version set to V2 only (token required) (console) or HttpTokens set to required (AWS CLI). With these settings, the instance requires that IMDSv2 is used when requesting instance metadata.
Note that when you set imds-support to v2.0, instances launched from this AMI will also have Metadata response hop limit (console) or http-put-response-hop-limit (AWS CLI) set to 2.
Important Do not use this parameter unless your AMI software supports IMDSv2. After you set the value to v2.0, you can't undo it. The only way to "reset" your AMI is to create a new AMI from the underlying snapshot.
To configure a new AMI for IMDSv2 Use one of the following methods to configure a new AMI for IMDSv2.
AWS CLI The following register-image example registers an AMI using the specified snapshot of an EBS root volume as device /dev/xvda. Specify v2.0 for the imds-support parameter so that

instances launched from this AMI will require that IMDSv2 is used when requesting instance metadata. aws ec2 register-image \ --name my-image \ --root-device-name /dev/xvda \ --block-device-mappings DeviceName=/dev/ xvda,Ebs={SnapshotId=snap-0123456789example} \ --architecture x86_64 \ --imds-support v2.0 PowerShell The following Register-EC2Image Cmdlet example registers an AMI using the specified snapshot of an EBS root volume as device /dev/xvda. Specify v2.0 for the ImdsSupport parameter so that instances launched from this AMI will require that IMDSv2 is used when requesting instance metadata.
Register-EC2Image `
    -Name 'my-image' `
    -RootDeviceName /dev/xvda `
    -BlockDeviceMapping  ( New-Object `
        -TypeName Amazon.EC2.Model.BlockDeviceMapping `
        -Property @{ DeviceName = '/dev/xvda'; EBS        = (New-Object -TypeName Amazon.EC2.Model.EbsBlockDevice -Property @{ SnapshotId = 'snap-0123456789example'
                VolumeType = 'gp3'
                } )
        }  ) `
    -Architecture X86_64 `
    -ImdsSupport v2.0 To configure an existing AMI for IMDSv2 Use one of the following methods to configure an existing AMI for IMDSv2.

AWS CLI The following modify-image-attribute example modifies an existing AMI for IMDSv2 only.
Specify v2.0 for the imds-support parameter so that instances launched from this AMI will require that IMDSv2 is used when requesting instance metadata. aws ec2 modify-image-attribute \ --image-id ami-0abcdef1234567890 \ --imds-support v2.0 PowerShell The following Edit-EC2ImageAttribute Cmdlet example modifies an existing AMI for IMDSv2 only. Specify v2.0 for the imds-support parameter so that instances launched from this AMI will require that IMDSv2 is used when requesting instance metadata.
Edit-EC2ImageAttribute `
    -ImageId ami-0abcdef1234567890 `
     -ImdsSupport 'v2.0'
##### Use an IAM policy You can create an IAM policy that prevents users from launching new instances unless they require IMDSv2 on the new instance.
To enforce the use of IMDSv2 on all new instances by using an IAM policy To ensure that users can only launch instances that require the use of IMDSv2 when requesting instance metadata, you can specify that the condition to require IMDSv2 must be met before an instance can be launched. For the example IAM policy, see Work with instance metadata.
#### Enable the IMDS IPv4 and IPv6 endpoints The IMDS has two endpoints on an instance: IPv4 (169.254.169.254) and IPv6 ([fd00:ec2::254]). When you enable the IMDS, the IPv4 endpoint is automatically enabled.
The IPv6 endpoint remains disabled even if you launch an instance into an IPv6-only subnet. To enable the IPv6 endpoint, you need to do so explicitly. When you enable the IPv6 endpoint, the IPv4 endpoint remains enabled.
You can enable the IPv6 endpoint at instance launch or after.

Requirements for enabling the IPv6 endpoint
- The selected instance type is a Nitro-based instance.
- The selected subnet supports IPv6, where the subnet is either dual stack or IPv6 only.
Use any of the following methods to launch an instance with the IMDS IPv6 endpoint enabled.
Console To enable the IMDS IPv6 endpoint at instance launch
- Launch the instance in the Amazon EC2 console with the following specified under Advanced details:
- For Metadata IPv6 endpoint, choose Enabled.
For more information, see Advanced details.
AWS CLI To enable the IMDS IPv6 endpoint at instance launch The following run-instances example launches a c6i.large instance with the IPv6 endpoint enabled for the IMDS. To enable the IPv6 endpoint, for the --metadata-options parameter, specify HttpProtocolIpv6=enabled. When you specify a value for HttpProtocolIpv6, you must also set HttpEndpoint to enabled. aws ec2 run-instances \ --image-id ami-0abcdef1234567890 \ --instance-type c6i.large \ ...
     --metadata-options "HttpEndpoint=enabled,HttpProtocolIpv6=enabled"
PowerShell To enable the IMDS IPv6 endpoint at instance launch The following New-EC2Instance Cmdlet example launches a c6i.large instance with the IPv6 endpoint enabled for the IMDS. To enable the IPv6 endpoint, specify MetadataOptions_HttpProtocolIpv6 as enabled. When you

specify a value for MetadataOptions_HttpProtocolIpv6, you must also set MetadataOptions_HttpEndpoint to enabled.
New-EC2Instance `
    -ImageId ami-0abcdef1234567890 `
    -InstanceType c6i.large `
    -MetadataOptions_HttpEndpoint enabled `
    -MetadataOptions_HttpProtocolIpv6 enabled
#### Turn off access to instance metadata You can turn off access to the instance metadata by disabling the IMDS when you launch an instance. You can turn on access later by re-enabling the IMDS. For more information, see Turn on access to instance metadata.
Important You can choose to disable the IMDS at launch or after launch. If you disable the IMDS at launch, the following might not work:
- You might not have SSH access to your instance. The public-keys/0/openssh-key, which is your instance's public SSH key, will not be accessible because the key is normally provided and accessed from EC2 instance metadata.
- EC2 user data will not be available and will not run at instance start. EC2 user data is hosted on the IMDS. If you disable the IMDS, you effectively turn off access to user data.
To access this functionality, you can re-enable the IMDS after launch.
Console To turn off access to instance metadata at launch
- Launch the instance in the Amazon EC2 console with the following specified under Advanced details:
- For Metadata accessible, choose Disabled.

For more information, see Advanced details.
AWS CLI To turn off access to instance metadata at launch at launch Launch the instance with --metadata-options set to HttpEndpoint=disabled. aws ec2 run-instances \ --image-id ami-0abcdef1234567890 \ --instance-type c6i.large \ ...
     --metadata-options "HttpEndpoint=disabled"
PowerShell To turn off access to instance metadata at launch at launch The following New-EC2Instance Cmdlet example launches an instance with MetadataOptions_HttpEndpoint set to disabled.
New-EC2Instance `
    -ImageId ami-0abcdef1234567890 `
    -InstanceType c6i.large `
    -MetadataOptions_HttpEndpoint disabled CloudFormation To specify the metadata options for an instance using CloudFormation, see the AWS::EC2::LaunchTemplate MetadataOptions property in the CloudFormation User Guide.
#### Allow access to tags in instance metadata By default, instance tags are not accessible in the instance metadata. For each instance, you must explicitly allow access. If access is allowed, instance tag keys must comply with specific character restrictions, otherwise the instance launch will fail. For more information, see Enable access to tags in instance metadata.
### Modify instance metadata options for existing instances You can modify the instance metadata options for existing instances.

You can also create an IAM policy that prevents users from modifying the instance metadata options on existing instances. To control which users can modify the instance metadata options, specify a policy that prevents all users other than users with a specified role to use the ModifyInstanceMetadataOptions API. For the example IAM policy, see Work with instance metadata.
Note If a declarative policy was used to configure the instance metadata options, you can't modify them directly within the account. For more information, see Declarative policies in the AWS Organizations User Guide.
#### Require the use of IMDSv2 Use one of the following methods to modify the instance metadata options on an existing instance to require that IMDSv2 is used when requesting instance metadata. When IMDSv2 is required, IMDSv1 cannot be used.
Note Before requiring that IMDSv2 is used, ensure that the instance isn't making IMDSv1 calls.
The MetadataNoToken CloudWatch metric tracks IMDSv1 calls. When MetadataNoToken records zero IMDSv1 usage for an instance, the instance is then ready to require IMDSv2.
Console To require the use of IMDSv2 on an existing instance
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Instances.
3. Select your instance.
4. Choose Actions, Instance settings, Modify instance metadata options.
5. In the Modify instance metadata options dialog box, do the following: a.
For Instance metadata service, select Enable. b.
For IMDSv2, choose Required.

c.
Choose Save.
AWS CLI To require the use of IMDSv2 on an existing instance Use the modify-instance-metadata-options CLI command and set the http-tokens parameter to required. When you specify a value for http-tokens, you must also set http-endpoint to enabled. aws ec2 modify-instance-metadata-options \ --instance-id i-1234567890abcdef0 \ --http-tokens required \ --http-endpoint enabled PowerShell To require the use of IMDSv2 on an existing instance Use the Edit-EC2InstanceMetadataOption Cmdlet and set the HttpTokens parameter to required. When you specify a value for HttpTokens, you must also set HttpEndpoint to enabled.
(Edit-EC2InstanceMetadataOption `
    -InstanceId i-1234567890abcdef0 `
    -HttpTokens required `
    -HttpEndpoint enabled).InstanceMetadataOptions
#### Restore the use of IMDSv1 When IMDSv2 is required, IMDSv1 will not work when requesting instance metadata. When IMDSv2 is optional, then both IMDSv2 and IMDSv1 will work. Therefore, to restore IMDSv1, make IMDSv2 optional by using one of the following methods.
Console To restore the use of IMDSv1 on an instance
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.

2. In the navigation pane, choose Instances.
3. Select your instance.
4. Choose Actions, Instance settings, Modify instance metadata options.
5. In the Modify instance metadata options dialog box, do the following: a.
For Instance metadata service, make sure that Enable is selected. b.
For IMDSv2, choose Optional. c.
Choose Save.
AWS CLI To restore the use of IMDSv1 on an instance You can use the modify-instance-metadata-options CLI command with http-tokens set to optional to restore the use of IMDSv1 when requesting instance metadata. aws ec2 modify-instance-metadata-options \ --instance-id i-1234567890abcdef0 \ --http-tokens optional \ --http-endpoint enabled PowerShell To restore the use of IMDSv1 on an instance You can use the Edit-EC2InstanceMetadataOption Cmdlet with HttpTokens set to optional to restore the use of IMDSv1 when requesting instance metadata.
(Edit-EC2InstanceMetadataOption `
    -InstanceId i-1234567890abcdef0 `
    -HttpTokens optional `
    -HttpEndpoint enabled).InstanceMetadataOptions
#### Change the PUT response hop limit For existing instances, you can change the settings of the PUT response hop limit.
Currently only the AWS CLI and AWS SDKs support changing the PUT response hop limit.

AWS CLI To change the PUT response hop limit Use the modify-instance-metadata-options CLI command and set the http-put-response- hop-limit parameter to the required number of hops. In the following example, the hop limit is set to 3. Note that when specifying a value for http-put-response-hop-limit, you must also set http-endpoint to enabled. aws ec2 modify-instance-metadata-options \ --instance-id i-1234567890abcdef0 \ --http-put-response-hop-limit 3 \ --http-endpoint enabled PowerShell To change the PUT response hop limit Use the Edit-EC2InstanceMetadataOption Cmdlet and set the HttpPutResponseHopLimit parameter to the required number of hops. In the following example, the hop limit is set to
3. Note that when specifying a value for HttpPutResponseHopLimit, you must also set HttpEndpoint to enabled.
(Edit-EC2InstanceMetadataOption `
    -InstanceId i-1234567890abcdef0 `
    -HttpPutResponseHopLimit 3 `
    -HttpEndpoint enabled).InstanceMetadataOptions
#### Enable the IMDS IPv4 and IPv6 endpoints The IMDS has two endpoints on an instance: IPv4 (169.254.169.254) and IPv6 ([fd00:ec2::254]). When you enable the IMDS, the IPv4 endpoint is automatically enabled.
The IPv6 endpoint remains disabled even if you launch an instance into an IPv6-only subnet. To enable the IPv6 endpoint, you need to do so explicitly. When you enable the IPv6 endpoint, the IPv4 endpoint remains enabled.
You can enable the IPv6 endpoint at instance launch or after.
Requirements for enabling the IPv6 endpoint
- The selected instance type is a Nitro-based instance.

- The selected subnet supports IPv6, where the subnet is either dual stack or IPv6 only.
Currently only the AWS CLI and AWS SDKs support enabling the IMDS IPv6 endpoint after instance launch.
AWS CLI To enable the IMDS IPv6 endpoint for your instance Use the modify-instance-metadata-options CLI command and set the http-protocol-ipv6 parameter to enabled. Note that when specifying a value for http-protocol-ipv6, you must also set http-endpoint to enabled. aws ec2 modify-instance-metadata-options \ --instance-id i-1234567890abcdef0 \ --http-protocol-ipv6 enabled \ --http-endpoint enabled PowerShell To enable the IMDS IPv6 endpoint for your instance Use the Edit-EC2InstanceMetadataOption Cmdlet and set the HttpProtocolIpv6 parameter to enabled. Note that when specifying a value for HttpProtocolIpv6, you must also set HttpEndpoint to enabled.
(Edit-EC2InstanceMetadataOption `
    -InstanceId i-1234567890abcdef0 `
    -HttpProtocolIpv6 enabled `
    -HttpEndpoint enabled).InstanceMetadataOptions
#### Turn on access to instance metadata You can turn on access to instance metadata by enabling the HTTP endpoint of the IMDS on your instance, regardless of which version of the IMDS you are using. You can reverse this change at any time by disabling the HTTP endpoint.
Use one of the following methods to turn on access to instance metadata on an instance.

Console To turn on access to instance metadata
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Instances.
3. Select your instance.
4. Choose Actions, Instance settings, Modify instance metadata options.
5. In the Modify instance metadata options dialog box, do the following: a.
For Instance metadata service, select Enable. b.
Choose Save.
AWS CLI To turn on access to instance metadata Use the modify-instance-metadata-options CLI command and set the http-endpoint parameter to enabled. aws ec2 modify-instance-metadata-options \ --instance-id i-1234567890abcdef0 \ --http-endpoint enabled PowerShell To turn on access to instance metadata Use the Edit-EC2InstanceMetadataOption Cmdlet and set the HttpEndpoint parameter to enabled.
(Edit-EC2InstanceMetadataOption `
    -InstanceId i-1234567890abcdef0 `
    -HttpEndpoint enabled).InstanceMetadataOptions

#### Turn off access to instance metadata You can turn off access to instance metadata by disabling the HTTP endpoint of the IMDS on your instance, regardless of which version of the IMDS you are using. You can reverse this change at any time by enabling the HTTP endpoint.
Use one of the following methods to turn off access to instance metadata on an instance.
Console To turn off access to instance metadata
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Instances.
3. Select your instance.
4. Choose Actions, Instance settings, Modify instance metadata options.
5. In the Modify instance metadata options dialog box, do the following: a.
For Instance metadata service, clear Enable. b.
Choose Save.
AWS CLI To turn off access to instance metadata Use the modify-instance-metadata-options CLI command and set the http-endpoint parameter to disabled. aws ec2 modify-instance-metadata-options \ --instance-id i-1234567890abcdef0 \ --http-endpoint disabled PowerShell To turn off access to instance metadata Use the Edit-EC2InstanceMetadataOption Cmdlet and set the HttpEndpoint parameter to disabled.

(Edit-EC2InstanceMetadataOption `
    -InstanceId i-1234567890abcdef0 `
    -HttpEndpoint disabled).InstanceMetadataOptions
#### Allow access to tags in instance metadata You can allow access to tags in the instance metadata on a running or stopped instance. For each instance, you must explicitly allow access. If access is allowed, instance tag keys must comply with specific character restrictions, otherwise you get an error. For more information, see Enable access to tags in instance metadata.
## Run commands when you launch an EC2 instance with user data input When you launch an Amazon EC2 instance, you can pass user data to the instance that is used to perform automated configuration tasks, or to run scripts after the instance starts.
If you're interested in more complex automation scenarios, you might consider CloudFormation.
For more information, see Deploying applications on Amazon EC2 with CloudFormation in the AWS CloudFormation User Guide.
On Linux instances, you can pass two types of user data to Amazon EC2: shell scripts and cloud- init directives. You can also pass this data into the launch instance wizard as plain text, as a file (this is useful for launching instances with the command line tools), or as base64-encoded text (for API calls).
On Windows instances, the launch agents handle your user data scripts.
Considerations
- User data is treated as opaque data: what you give is what you get back. It is up to the instance to interpret it.
- User data must be base64-encoded. The Amazon EC2 console can perform the base64-encoding for your or accept base64-encoded input. If you retrieve the user data using instance metadata or the console, it's base64-decoded for you automatically.
- User data is limited to 16 KB, in raw form, before it is base64-encoded. The size of a string of length n after base64-encoding is ceil(n/3)*4.
- User data is an instance attribute. If you create an AMI from an instance, the instance user data is not included in the AMI.

### User data in the AWS Management Console You can specify instance user data when you launch the instance. If the root volume of the instance is an EBS volume, you can also stop the instance and update its user data.
#### Specify instance user data at launch with the Launch Wizard You can specify user data when you launch an instance with the Launch Wizard in the EC2 console.
To specify user data on launch, follow the procedure for launching an instance. The User data field is located in the Advanced details section of the launch instance wizard. Enter your PowerShell script in the User data field, and then complete the instance launch procedure.
In the following screenshot of the User data field, the example script creates a file in the Windows temporary folder, using the current date and time in the file name. When you include <persist>true</persist>, the script is run every time you reboot or start the instance. If you leave the User data has already been base64 encoded checkbox empty, the Amazon EC2 console performs the base64 encoding for you.

For more information, see Specify instance user data at launch with the Launch Wizard. For a Linux example that uses the AWS CLI, see the section called "User data and the AWS CLI". For a Windows example that uses the Tools for Windows PowerShell, see the section called "User data and the Tools for Windows PowerShell".
#### View and update the instance user data You can view the instance user data for any instance, and you can update the instance user data for a stopped instance.
To update the user data for an instance using the console
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Instances.
3. Select the instance and choose Actions, Instance state, Stop instance.
Warning When you stop an instance, the data on any instance store volumes is erased. To keep data from instance store volumes, be sure to back it up to persistent storage.
4. When prompted for confirmation, choose Stop. It can take a few minutes for the instance to stop.
5. With the instance still selected, choose Actions, Instance settings, Edit user data. You can't change the user data if the instance is running, but you can view it.
6. In the Edit user data dialog box, update the user data, and then choose Save. To run user data scripts every time you reboot or start the instance, add <persist>true</persist>, as shown in the following example:

7. Start the instance. If you enabled user data execution for subsequent reboots or starts, the updated user data scripts are run as part of the instance start process.
### How Amazon EC2 handles user data for Linux instances The following examples use user data to run commands that set up a LAMP server when the instance launches. In each example, the following tasks are performed:
- The distribution software packages are updated.

- The web server, php, and mariadb packages are installed.
- The httpd service is started and turned on.
- The user ec2-user is added to the apache group.
- The appropriate ownership and file permissions are set for the web directory and the files contained within it.
- A simple web page is created to test the web server and PHP engine.
Contents
- Prerequisites
- User data and shell scripts
- Update the instance user data
- User data and cloud-init directives
- User data and the AWS CLI
- Combine shell scripts and cloud-init directives
#### Prerequisites The examples in this topic assume the following:
- Your instance has a public DNS name that is reachable from the internet.
- The security group associated with your instance is configured to allow SSH (port 22) traffic so that you can connect to the instance to view the output log files.
- Your instance is launched using an Amazon Linux AMI. The commands and directives might not work for other Linux distributions. For more information about other distributions, such as their support for cloud-init, see documentation for the specific distribution.
#### User data and shell scripts If you are familiar with shell scripting, this is the easiest and most complete way to send instructions to an instance at launch. Adding these tasks at boot time adds to the amount of time it takes to boot the instance. You should allow a few minutes of extra time for the tasks to complete before you test that the user script has finished successfully.

Important By default, user data scripts and cloud-init directives run only during the boot cycle when you first launch an instance. You can update your configuration to ensure that your user data scripts and cloud-init directives run every time you restart your instance. For more information, see How can I utilize user data to automatically run a script with every restart of my Amazon EC2 Linux instance? in the AWS Knowledge Center.
User data shell scripts must start with the #! characters and the path to the interpreter you want to read the script (commonly /bin/bash). For an introduction on shell scripting, see the Bash Reference Manual on the GNU Operating System website.
Scripts entered as user data are run as the root user, so do not use the sudo command in the script.
Remember that any files you create will be owned by the root user; if you need a non-root user to have file access, you should modify the permissions accordingly in the script. Also, because the script is not run interactively, you cannot include commands that require user feedback (such as yum update without the -y flag).
If you use an AWS API, including the AWS CLI, in a user data script, you must use an instance profile when launching the instance. An instance profile provides the appropriate AWS credentials required by the user data script to issue the API call. For more information, see Use instance profiles in the IAM User Guide. The permissions you assign to the IAM role depend on which services you are calling with the API. For more information, see IAM roles for Amazon EC2.
The cloud-init output log file captures console output so it is easy to debug your scripts following a launch if the instance does not behave the way you intended. To view the log file, connect to the instance and open /var/log/cloud-init-output.log.
When a user data script is processed, it is copied to and run from /var/lib/cloud/ instances/instance-id/. The script is not deleted after it is run. Be sure to delete the user data scripts from /var/lib/cloud/instances/instance-id/ before you create an AMI from the instance. Otherwise, the script will exist in this directory on any instance launched from the AMI.
#### Update the instance user data To update the instance user data, you must first stop the instance. If the instance is running, you can view the user data but you cannot modify it.

Warning When you stop an instance, the data on any instance store volumes is erased. To keep data from instance store volumes, be sure to back it up to persistent storage.
To modify instance user data
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Instances.
3. Select the instance and choose Instance state, Stop instance. If this option is disabled, either the instance is already stopped or its root volume is an instance store volume.
4. When prompted for confirmation, choose Stop. It can take a few minutes for the instance to stop.
5. With the instance still selected, choose Actions, Instance settings, Edit user data.
6. Modify the user data as needed, and then choose Save.
7. Start the instance. The new user data is visible on your instance after you start it; however, user data scripts are not run.
#### User data and cloud-init directives The cloud-init package configures specific aspects of a new Amazon Linux instance when it is launched; most notably, it configures the .ssh/authorized_keys file for the ec2-user so you can log in with your own private key. For more information about the configuration tasks that the cloud-init package performs for Amazon Linux instances, see the following documentation:
- Amazon Linux 2023 – Customized cloud-init
- Amazon Linux 2 – Using cloud-init on Amazon Linux 2 The cloud-init user directives can be passed to an instance at launch the same way that a script is passed, although the syntax is different. For more information about cloud-init, see https:// cloudinit.readthedocs.org/en/latest/index.html.

Important By default, user data scripts and cloud-init directives run only during the boot cycle when you first launch an instance. You can update your configuration to ensure that your user data scripts and cloud-init directives run every time you restart your instance. For more information, see How can I utilize user data to automatically run a script with every restart of my Amazon EC2 Linux instance? in the AWS Knowledge Center.
Adding these tasks at boot time adds to the amount of time it takes to boot an instance. You should allow a few minutes of extra time for the tasks to complete before you test that your user data directives have completed.
To pass cloud-init directives to an Amazon Linux instance
1. Follow the procedure for launching an instance. The User data field is located in the Advanced details section of the launch instance wizard. Enter your cloud-init directive text in the User data field, and then complete the instance launch procedure.
In the examples below, the directives create and configure a web server on Amazon Linux. The
#cloud-config line at the top is required in order to identify the commands as cloud-init directives.
AL2023
#cloud-config package_update: true package_upgrade: all

packages:
- httpd
- mariadb105-server
- php8.1
- php8.1-mysqlnd runcmd:
- systemctl start httpd
- systemctl enable httpd
- [ sh, -c, "usermod -a -G apache ec2-user" ]
- [ sh, -c, "chown -R ec2-user:apache /var/www" ]
- chmod 2775 /var/www

- [ find, /var/www, -type, d, -exec, chmod, 2775, {}, \; ]
- [ find, /var/www, -type, f, -exec, chmod, 0664, {}, \; ]
- [ sh, -c, 'echo "<?php phpinfo(); ?>" > /var/www/html/phpinfo.php' ]
AL2
#cloud-config package_update: true package_upgrade: all

packages:
- httpd
- mariadb-server

runcmd:
- [ sh, -c, "amazon-linux-extras install -y lamp-mariadb10.2-php7.2 php7.2" ]
- systemctl start httpd
- systemctl enable httpd
- [ sh, -c, "usermod -a -G apache ec2-user" ]
- [ sh, -c, "chown -R ec2-user:apache /var/www" ]
- chmod 2775 /var/www
- [ find, /var/www, -type, d, -exec, chmod, 2775, {}, \; ]
- [ find, /var/www, -type, f, -exec, chmod, 0664, {}, \; ]
- [ sh, -c, 'echo "<?php phpinfo(); ?>" > /var/www/html/phpinfo.php' ]
2. Allow enough time for the instance to launch and run the directives in your user data, and then check to see that your directives have completed the tasks you intended.
For this example, in a web browser, enter the URL of the PHP test file the directives created.
This URL is the public DNS address of your instance followed by a forward slash and the file name. http://my.public.dns.amazonaws.com/phpinfo.php You should see the PHP information page. If you are unable to see the PHP information page, check that the security group you are using contains a rule to allow HTTP (port 80) traffic. For more information, see Configure security group rules.
3. (Optional) If your directives did not accomplish the tasks you were expecting them to, or if you just want to verify that your directives completed without errors, connect to the instance, examine the output log file (/var/log/cloud-init-output.log), and look for error

messages in the output. For additional debugging information, you can add the following line to your directives: output : { all : '| tee -a /var/log/cloud-init-output.log' } This directive sends runcmd output to /var/log/cloud-init-output.log.
#### User data and the AWS CLI You can use the AWS CLI to specify, modify, and view the user data for your instance. For information about viewing user data from your instance using instance metadata, see Access instance metadata for an EC2 instance.
On Windows, you can use the AWS Tools for Windows PowerShell instead of using the AWS CLI. For more information, see User data and the Tools for Windows PowerShell .
Example: Specify user data at launch To specify user data when you launch your instance, use the run-instances command with the -- user-data parameter. With run-instances, the AWS CLI performs base64 encoding of the user data for you.
The following example shows how to specify a script as a string on the command line: aws ec2 run-instances --image-id ami-abcd1234 --count 1 --instance-type m3.medium \ --key-name my-key-pair --subnet-id subnet-abcd1234 --security-group-ids sg-abcd1234 \ --user-data echo user data The following example shows how to specify a script using a text file. Be sure to use the file:// prefix to specify the file. aws ec2 run-instances --image-id ami-abcd1234 --count 1 --instance-type m3.medium \ --key-name my-key-pair --subnet-id subnet-abcd1234 --security-group-ids sg-abcd1234 \ --user-data file://my_script.txt The following is an example text file with a shell script.
#!/bin/bash

yum update -y service httpd start chkconfig httpd on Example: Modify the user data of a stopped instance You can modify the user data of a stopped instance using the modify-instance-attribute command.
With modify-instance-attribute, the AWS CLI does not perform base64 encoding of the user data for you.
- On a Linux computer, use the base64 command to encode the user data. base64 my_script.txt >my_script_base64.txt
- On a Windows computer, use the certutil command to encode the user data. Before you can use this file with the AWS CLI, you must remove the first (BEGIN CERTIFICATE) and last (END CERTIFICATE) lines. certutil -encode my_script.txt my_script_base64.txt notepad my_script_base64.txt Use the --attribute and --value parameters to use the encoded text file to specify the user data. Be sure to use the file:// prefix to specify the file. aws ec2 modify-instance-attribute --instance-id i-1234567890abcdef0 --attribute userData --value file://my_script_base64.txt Example: Clear the user data of a stopped instance To delete the existing user data, use the modify-instance-attribute command as follows: aws ec2 modify-instance-attribute --instance-id i-1234567890abcdef0 --user-data Value= Example: View user data To retrieve the user data for an instance, use the describe-instance-attribute command. With describe-instance-attribute, the AWS CLI does not perform base64 decoding of the user data for you.

aws ec2 describe-instance-attribute --instance-id i-1234567890abcdef0 --attribute userData The following is example output with the user data base64 encoded.
{ "UserData": { "Value":
 "IyEvYmluL2Jhc2gKeXVtIHVwZGF0ZSAteQpzZXJ2aWNlIGh0dHBkIHN0YXJ0CmNoa2NvbmZpZyBodHRwZCBvbg=="
    }, "InstanceId": "i-1234567890abcdef0"
}
- On a Linux computer , use the --query option to get the encoded user data and the base64 command to decode it. aws ec2 describe-instance-attribute --instance-id i-1234567890abcdef0 --attribute userData --output text --query "UserData.Value" | base64 --decode
- On a Windows computer, use the --query option to get the coded user data and the certutil command to decode it. Note that the encoded output is stored in a file and the decoded output is stored in another file. aws ec2 describe-instance-attribute --instance-id i-1234567890abcdef0 --attribute userData --output text --query "UserData.Value" >my_output.txt certutil -decode my_output.txt my_output_decoded.txt type my_output_decoded.txt The following is example output.
#!/bin/bash yum update -y service httpd start chkconfig httpd on

#### Combine shell scripts and cloud-init directives By default, you can include only one content type in user data at a time. However, you can use the text/cloud-config and text/x-shellscript content-types in a mime-multi part file to include both a shell script and cloud-init directives in your user data.
The following shows the mime-multi part format.
Content-Type: multipart/mixed; boundary="//"
MIME-Version: 1.0

--// Content-Type: text/cloud-config; charset="us-ascii"
MIME-Version: 1.0 Content-Transfer-Encoding: 7bit Content-Disposition: attachment; filename="cloud-config.txt"

#cloud-config cloud-init directives

--// Content-Type: text/x-shellscript; charset="us-ascii"
MIME-Version: 1.0 Content-Transfer-Encoding: 7bit Content-Disposition: attachment; filename="userdata.txt"

#!/bin/bash shell script commands --//-- For example, the following user data includes cloud-init directives and a bash shell script.
The cloud-init directives creates a file (/test-cloudinit/cloud-init.txt), and writes Created by cloud-init to that file. The bash shell script creates a file (/test-userscript/ userscript.txt) and writes Created by bash shell script to that file.
Content-Type: multipart/mixed; boundary="//"
MIME-Version: 1.0

--// Content-Type: text/cloud-config; charset="us-ascii"
MIME-Version: 1.0 Content-Transfer-Encoding: 7bit

Content-Disposition: attachment; filename="cloud-config.txt"

#cloud-config runcmd:
- [ mkdir, /test-cloudinit ] write_files:
- path: /test-cloudinit/cloud-init.txt content: Created by cloud-init

--// Content-Type: text/x-shellscript; charset="us-ascii"
MIME-Version: 1.0 Content-Transfer-Encoding: 7bit Content-Disposition: attachment; filename="userdata.txt"

#!/bin/bash mkdir test-userscript touch /test-userscript/userscript.txt echo "Created by bash shell script" >> /test-userscript/userscript.txt --//--
### How Amazon EC2 handles user data for Windows instances On Windows instances, the launch agent performs the tasks related to user data. For more information, see the following:
- EC2Launch v2
- EC2Launch
- EC2Config service For examples of the assembly of a UserData property in a CloudFormation template, see Base64 Encoded UserData Property and Base64 Encoded UserData Property with AccessKey and SecretKey.
For an example of running commands on an instance within an Auto Scaling group that works with lifecycle hooks, see Tutorial: Configure user data to retrieve the target lifecycle state through instance metadata in the Amazon EC2 Auto Scaling User Guide.
Contents
- User data scripts
- Compressed user data

- User data execution
- User data and the Tools for Windows PowerShell
#### User data scripts For EC2Config or EC2Launch to run scripts, you must enclose the script within a special tag when you add it to user data. The tag that you use depends on whether the commands run in a Command Prompt window (batch commands) or use Windows PowerShell.
If you specify both a batch script and a Windows PowerShell script, the batch script runs first and the Windows PowerShell script runs next, regardless of the order in which they appear in the instance user data.
If you use an AWS API, including the AWS CLI, in a user data script, you must use an instance profile when launching the instance. An instance profile provides the appropriate AWS credentials required by the user data script to make the API call. For more information, see Instance profiles.
The permissions you assign to the IAM role depend on which services you are calling with the API.
For more information, see IAM roles for Amazon EC2.
Script type
- Syntax for batch scripts
- Syntax for Windows PowerShell scripts
- Syntax for YAML configuration scripts
- Base64 encoding
##### Syntax for batch scripts Specify a batch script using the script tag. Separate the commands using line breaks as shown in the following example.
<script> echo Current date and time >> %SystemRoot%\Temp\test.log echo %DATE% %TIME% >> %SystemRoot%\Temp\test.log </script>
By default, user data scripts run one time when you launch the instance. To run the user data scripts every time you reboot or start the instance, add <persist>true</persist> to the user data.

<script> echo Current date and time >> %SystemRoot%\Temp\test.log echo %DATE% %TIME% >> %SystemRoot%\Temp\test.log </script>
<persist>true</persist>
EC2Launch v2 agent To run an XML user data script as a detached process with the EC2Launch v2 executeScript task in the UserData stage, add <detach>true</detach> to the user data.
Note The detach tag is not supported by previous launch agents.
<script> echo Current date and time >> %SystemRoot%\Temp\test.log echo %DATE% %TIME% >> %SystemRoot%\Temp\test.log </script>
<detach>true</detach>
##### Syntax for Windows PowerShell scripts The AWS Windows AMIs include the AWS Tools for Windows PowerShell, so you can specify these cmdlets in user data. If you associate an IAM role with your instance, you don't need to specify credentials to the cmdlets, as applications that run on the instance use the role's credentials to access AWS resources (for example, Amazon S3 buckets).
Specify a Windows PowerShell script using the <powershell> tag. Separate the commands using line breaks. The <powershell> tag is case-sensitive.
For example:
<powershell>
    $file = $env:SystemRoot + "\Temp\" + (Get-Date).ToString("MM-dd-yy-hh-mm")
    New-Item $file -ItemType file </powershell>

By default, the user data scripts run one time when you launch the instance. To run the user data scripts every time you reboot or start the instance, add <persist>true</persist> to the user data.
<powershell>
    $file = $env:SystemRoot + "\Temp\" + (Get-Date).ToString("MM-dd-yy-hh-mm")
    New-Item $file -ItemType file </powershell>
<persist>true</persist>
You can specify one or more PowerShell arguments with the <powershellArguments> tag. If no arguments are passed, EC2Launch and EC2Launch v2 add the following argument by default: - ExecutionPolicy Unrestricted.
Example:
<powershell>
    $file = $env:SystemRoot + "\Temp" + (Get-Date).ToString("MM-dd-yy-hh-mm")
    New-Item $file -ItemType file </powershell>
<powershellArguments>-ExecutionPolicy Unrestricted -NoProfile -NonInteractive</ powershellArguments>
EC2Launch v2 agent To run an XML user data script as a detached process with the EC2Launch v2 executeScript task in the UserData stage, add <detach>true</detach> to the user data.
Note The detach tag is not supported by previous launch agents.
<powershell>
    $file = $env:SystemRoot + "\Temp\" + (Get-Date).ToString("MM-dd-yy-hh-mm")
    New-Item $file -ItemType file </powershell>
<detach>true</detach>

##### Syntax for YAML configuration scripts If you are using EC2Launch v2 to run scripts, you can use the YAML format. To view configuration tasks, details, and examples for EC2Launch v2, see EC2Launch v2 task configuration.
Specify a YAML script with the executeScript task.
Example YAML syntax to run a PowerShell script version: 1.0 tasks:
- task: executeScript inputs:
  - frequency: always type: powershell runAs: localSystem content: |- $file = $env:SystemRoot + "\Temp\" + (Get-Date).ToString("MM-dd-yy-hh-mm")
      New-Item $file -ItemType file Example YAML syntax to run a batch script version: 1.1 tasks:
- task: executeScript inputs:
  - frequency: always type: batch runAs: localSystem content: |- echo Current date and time >> %SystemRoot%\Temp\test.log echo %DATE% %TIME% >> %SystemRoot%\Temp\test.log
##### Base64 encoding If you're using the Amazon EC2 API or a tool that does not perform base64 encoding of the user data, you must encode the user data yourself. If not, an error is logged about being unable to find script or powershell tags to run. The following is an example that encodes using Windows PowerShell.
$UserData = [System.Convert]::ToBase64String([System.Text.Encoding]::ASCII.GetBytes($Script))

The following is an example that decodes using PowerShell.
$Script = [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String($UserData))
For more information about base64 encoding, see https://www.ietf.org/rfc/rfc4648.txt.
#### Compressed user data EC2Launch v2 supports zipped user data as a method to submit user data that's larger than the 16 KB limit imposed by IMDS. To use this feature, compress your user data script into a .zip archive and pass it to your EC2 instance. When EC2Launch v2 detects compressed user data, it automatically unzips the compressed user data script and runs it.
As with standard user data, if you're using the Amazon EC2 API or a tool that does not perform base64 encoding of the user data, you must encode the compressed user data yourself. For more information about the user data size limit and base64 encoding, see Access instance metadata for an EC2 instance.
#### User data execution By default, all AWS Windows AMIs have user data execution enabled for the initial launch. You can specify that user data scripts are run the next time the instance reboots or restarts. Alternatively, you can specify that user data scripts are run every time the instance reboots or restarts.
Note User data is not enabled to run by default after the initial launch. To enable user data to run when you reboot or start the instance, see Run scripts during subsequent reboots or starts.
User data scripts are run from the local administrator account when a random password is generated. Otherwise, user data scripts are run from the System account.
##### Instance launch scripts Scripts in the instance user data are run during the initial launch of the instance. If the persist tag is found, user data execution is enabled for subsequent reboots or starts. The log files for EC2Launch v2, EC2Launch, and EC2Config contain the output from the standard output and standard error streams.

EC2Launch v2 The log file for EC2Launch v2 is C:\ProgramData\Amazon\EC2Launch\log\agent.log.
Note The C:\ProgramData folder might be hidden. To view the folder, you must show hidden files and folders.
The following information is logged when the user data is run:
- Info: Converting user-data to yaml format – If the user data was provided in XML format
- Info: Initialize user-data state – The start of user data execution
- Info: Frequency is: always – If the user data task is running on every boot
- Info: Frequency is: once – If the user data task is running just once
- Stage: postReadyUserData execution completed – The end of user data execution EC2Launch The log file for EC2Launch is C:\ProgramData\Amazon\EC2-Windows\Launch\Log \UserdataExecution.log.
The C:\ProgramData folder might be hidden. To view the folder, you must show hidden files and folders.
The following information is logged when the user data is run:
- Userdata execution begins – The start of user data execution
- <persist> tag was provided: true – If the persist tag is found
- Running userdata on every boot – If the persist tag is found
- <powershell> tag was provided.. running powershell content – If the powershell tag is found
- <script> tag was provided.. running script content – If the script tag is found
- Message: The output from user scripts – If user data scripts are run, their output is logged

EC2Config The log file for EC2Config is C:\Program Files\Amazon\Ec2ConfigService\Logs \Ec2Config.log. The following information is logged when the user data is run:
- Ec2HandleUserData: Message: Start running user scripts – The start of user data execution
- Ec2HandleUserData: Message: Re-enabled userdata execution – If the persist tag is found
- Ec2HandleUserData: Message: Could not find <persist> and </persist> – If the persist tag is not found
- Ec2HandleUserData: Message: The output from user scripts – If user data scripts are run, their output is logged
##### Run scripts during subsequent reboots or starts When you update instance user data, the updated user data content is automatically reflected in the instance metadata the next time you reboot or start the instance. However, depending on the installed launch agent, additional configuration may be required to configure user data scripts to run on subsequent reboots or starts.
If you choose the Shutdown with Sysprep option, user data scripts run the next time the instance starts or reboots, even if you did not enable user data execution for subsequent reboots or starts.
For instructions to enable user data execution, select the tab that matches your launch agent.
EC2Launch v2 Unlike EC2Launch v1, EC2Launch v2 evaluates the user data task on every boot. It is not necessary to manually schedule the user data task. The user data runs based on the included frequency or persist options.
For XML user data scripts To run user data scripts on every boot, add the <persist>true</persist> flag to the user data. If the persist flag is not included, the user data script only runs on the initial boot.
For YAML user data
- To run a task in user data on the initial boot, set the task frequency to once.

- To run a task in user data on every boot, set the task frequency to always.
EC2Launch
1. Connect to your Windows instance.
2. Open a PowerShell command window and run one of the following commands:
Run once To run user data once on the next boot, use the -Schedule flag.
C:\ProgramData\Amazon\EC2-Windows\Launch\Scripts\InitializeInstance.ps1 - Schedule Run on all subsequent boots To run user data on all subsequent boots, use the -SchedulePerBoot flag.
C:\ProgramData\Amazon\EC2-Windows\Launch\Scripts\InitializeInstance.ps1 - SchedulePerBoot
3. Disconnect from your Windows instance. To run updated scripts the next time the instance is started, stop the instance and update the user data.
EC2Config
1. Connect to your Windows instance.
2. Open C:\Program Files\Amazon\Ec2ConfigService \Ec2ConfigServiceSetting.exe.
3. For User Data, select Enable UserData execution for next service start.
4. Disconnect from your Windows instance. To run updated scripts the next time the instance is started, stop the instance and update the user data.
#### User data and the Tools for Windows PowerShell You can use the Tools for Windows PowerShell to specify, modify, and view the user data for your instance. For information about viewing user data from your instance using instance metadata, see

Access instance metadata for an EC2 instance. For information about user data and the AWS CLI, see User data and the AWS CLI.
Example: Specify instance user data at launch Create a text file with the instance user data. To run user data scripts every time you reboot or start the instance, add <persist>true</persist>, as shown in the following example.
<powershell>
    $file = $env:SystemRoot + "\Temp\" + (Get-Date).ToString("MM-dd-yy-hh-mm")
    New-Item $file -ItemType file </powershell>
<persist>true</persist>
To specify instance user data when you launch your instance, use the New-EC2Instance command.
This command does not perform base64 encoding of the user data for you. Use the following commands to encode the user data in a text file named script.txt.
PS C:\> $Script = Get-Content -Raw script.txt PS C:\> $UserData = [System.Convert]::ToBase64String([System.Text.Encoding]::ASCII.GetBytes($Script))
Use the -UserData parameter to pass the user data to the New-EC2Instance command.
PS C:\> New-EC2Instance -ImageId ami-abcd1234 -MinCount 1 -MaxCount 1 - InstanceType m3.medium \ -KeyName my-key-pair -SubnetId subnet-12345678 -SecurityGroupIds sg-1a2b3c4d \ -UserData $UserData Example: Update instance user data for a stopped instance You can modify the user data of a stopped instance using the Edit-EC2InstanceAttribute command.
Create a text file with the new script. Use the following commands to encode the user data in the text file named new-script.txt.
PS C:\> $NewScript = Get-Content -Raw new-script.txt PS C:\> $NewUserData = [System.Convert]::ToBase64String([System.Text.Encoding]::ASCII.GetBytes($NewScript))

Use the -UserData and -Value parameters to specify the user data.
PS C:\> Edit-EC2InstanceAttribute -InstanceId i-1234567890abcdef0 -Attribute userData - Value $NewUserData Example: View instance user data To retrieve the user data for an instance, use the Get-EC2InstanceAttribute command.
PS C:\> (Get-EC2InstanceAttribute -InstanceId i-1234567890abcdef0 -Attribute userData).UserData The following is example output. Note that the user data is encoded.
PHBvd2Vyc2hlbGw +DQpSZW5hbWUtQ29tcHV0ZXIgLU5ld05hbWUgdXNlci1kYXRhLXRlc3QNCjwvcG93ZXJzaGVsbD4= Use the following commands to store the encoded user data in a variable and then decode it.
PS C:\> $UserData_encoded = (Get-EC2InstanceAttribute -InstanceId i-1234567890abcdef0 - Attribute userData).UserData PS C:
\> [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String($UserData_encoded)
The following is example output.
<powershell>
    $file = $env:SystemRoot + "\Temp\" + (Get-Date).ToString("MM-dd-yy-hh-mm")
    New-Item $file -ItemType file </powershell>
<persist>true</persist>
Example: Rename the instance to match the tag value You can use the Get-EC2Tag command to read the tag value, rename the instance on first boot to match the tag value, and reboot. To run this command successfully, you must have a role with ec2:DescribeTags permissions attached to the instance because tag information is retrieved by the API call. For more information on settings permissions by using IAM roles, see Attach an IAM role to an instance.

IMDSv2 <powershell>
    [string]$token = Invoke-RestMethod -Headers @{"X-aws-ec2-metadata-token-ttl- seconds" = "21600"} -Method PUT -Uri 'http://169.254.169.254/latest/api/token' - UseBasicParsing $instanceId = Invoke-RestMethod -Headers @{"X-aws-ec2-metadata-token" = $token} -Method GET -Uri 'http://169.254.169.254/latest/meta-data/instance-id' - UseBasicParsing $nameValue = (Get-EC2Tag -Filter @{Name="resource-id";Value= $instanceid},@{Name="key";Value="Name"}).Value $pattern = "^(?![0-9]{1,15}$)[a-zA-Z0-9-]{1,15}$"
 #Verify Name Value satisfies best practices for Windows hostnames If ($nameValue -match $pattern)
     {Try {Rename-Computer -NewName $nameValue -Restart -ErrorAction Stop} Catch {$ErrorMessage = $_.Exception.Message Write-Output "Rename failed: $ErrorMessage"}} Else {Throw "Provided name not a valid hostname. Please ensure Name value is between 1 and 15 characters in length and contains only alphanumeric or hyphen characters"} </powershell>
IMDSv1 <powershell>
 $instanceId = (Invoke-WebRequest http://169.254.169.254/latest/meta-data/instance- id -UseBasicParsing).content $nameValue = (Get-EC2Tag -Filter @{Name="resource-id";Value= $instanceid},@{Name="key";Value="Name"}).Value $pattern = "^(?![0-9]{1,15}$)[a-zA-Z0-9-]{1,15}$"
 #Verify Name Value satisfies best practices for Windows hostnames If ($nameValue -match $pattern)
     {Try {Rename-Computer -NewName $nameValue -Restart -ErrorAction Stop} Catch {$ErrorMessage = $_.Exception.Message Write-Output "Rename failed: $ErrorMessage"}} Else {Throw "Provided name not a valid hostname. Please ensure Name value is between 1 and 15 characters in length and contains only alphanumeric or hyphen characters"} </powershell>

You can also rename the instance using tags in instance metadata, if your instance is configured to access tags from the instance metadata. For more information, see View tags for your EC2 instances using instance metadata.
IMDSv2 <powershell>
    [string]$token = Invoke-RestMethod -Headers @{"X-aws-ec2-metadata-token-ttl- seconds" = "21600"} -Method PUT -Uri 'http://169.254.169.254/latest/api/token' - UseBasicParsing $nameValue = Invoke-RestMethod -Headers @{"X-aws-ec2-metadata-token" = $token} -Method GET -Uri 'http://169.254.169.254/latest/meta-data/tags/instance/Name' - UseBasicParsing $pattern = "^(?![0-9]{1,15}$)[a-zA-Z0-9-]{1,15}$"
 #Verify Name Value satisfies best practices for Windows hostnames If ($nameValue -match $pattern)
     {Try {Rename-Computer -NewName $nameValue -Restart -ErrorAction Stop} Catch {$ErrorMessage = $_.Exception.Message Write-Output "Rename failed: $ErrorMessage"}} Else {Throw "Provided name not a valid hostname. Please ensure Name value is between 1 and 15 characters in length and contains only alphanumeric or hyphen characters"} </powershell>
IMDSv1 <powershell>
 $nameValue = Get-EC2InstanceMetadata -Path /tags/instance/Name $pattern = "^(?![0-9]{1,15}$)[a-zA-Z0-9-]{1,15}$"
 #Verify Name Value satisfies best practices for Windows hostnames If ($nameValue -match $pattern)
     {Try {Rename-Computer -NewName $nameValue -Restart -ErrorAction Stop} Catch {$ErrorMessage = $_.Exception.Message Write-Output "Rename failed: $ErrorMessage"}} Else {Throw "Provided name not a valid hostname. Please ensure Name value is between 1 and 15 characters in length and contains only alphanumeric or hyphen characters"} </powershell>

## Identify each instance launched in a single request This example demonstrates how you can use both user data and instance metadata to configure your Amazon EC2 instances.
Note The examples in this section use the IPv4 address of the IMDS: 169.254.169.254. If you are retrieving instance metadata for EC2 instances over the IPv6 address, ensure that you enable and use the IPv6 address instead: [fd00:ec2::254]. The IPv6 address of the IMDS is compatible with IMDSv2 commands. The IPv6 address is only accessible on Nitro-based instances in IPv6-supported subnets (dual stack or IPv6 only).
Alice wants to launch four instances of her favorite database AMI, with the first acting as the original instance and the remaining three acting as replicas. When she launches them, she wants to add user data about the replication strategy for each replica. She is aware that this data will be available to all four instances, so she needs to structure the user data in a way that allows each instance to recognize which parts are applicable to it. She can do this using the ami-launch- index instance metadata value, which will be unique for each instance. If she starts more than one instance at the same time, the ami-launch-index indicates the order in which the instances were launched. The value of the first instance launched is 0.
Here is the user data that Alice has constructed. replicate-every=1min | replicate-every=5min | replicate-every=10min The replicate-every=1min data defines the first replica's configuration, replicate- every=5min defines the second replica's configuration, and so on. Alice decides to provide this data as an ASCII string with a pipe symbol (|) delimiting the data for the separate instances.
Alice launches four instances using the run-instances command, specifying the user data. aws ec2 run-instances \ --image-id ami-0abcdef1234567890 \ --count 4 \ --instance-type t2.micro \ --user-data "replicate-every=1min | replicate-every=5min | replicate-every=10min"

After they're launched, all instances have a copy of the user data and the common metadata shown here:
- AMI ID: ami-0abcdef1234567890
- Reservation ID: r-1234567890abcabc0
- Public keys: none
- Security group name: default
- Instance type: t2.micro However, each instance has unique metadata, as shown in the following tables.
Metadata Value instance-id i-1234567890abcdef0 ami-launch-index 0 public-hostname ec2-203-0-113-25.compute-1.amazonaws.com public-ipv4 67.202.51.223 local-hostname ip-10-251-50-12.ec2.internal local-ipv4 10.251.50.35 Metadata Value instance-id i-0598c7d356eba48d7 ami-launch-index 1 public-hostname ec2-67-202-51-224.compute-1.amazonaws.com public-ipv4 67.202.51.224 local-hostname ip-10-251-50-36.ec2.internal local-ipv4 10.251.50.36

Metadata Value instance-id i-0ee992212549ce0e7 ami-launch-index 2 public-hostname ec2-67-202-51-225.compute-1.amazonaws.com public-ipv4 67.202.51.225 local-hostname ip-10-251-50-37.ec2.internal local-ipv4 10.251.50.37 Metadata Value instance-id i-1234567890abcdef0 ami-launch-index 3 public-hostname ec2-67-202-51-226.compute-1.amazonaws.com public-ipv4 67.202.51.226 local-hostname ip-10-251-50-38.ec2.internal local-ipv4 10.251.50.38 Alice can use the ami-launch-index value to determine which portion of the user data is applicable to a particular instance.
1. She connects to one of the instances, and retrieves the ami-launch-index for that instance to ensure it is one of the replicas:
IMDSv2 [ec2-user ~]$ TOKEN=`curl -X PUT "http://169.254.169.254/latest/meta-data/api/ token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600"` \

&& curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta- data/ami-launch-index 2 For the following steps, the IMDSv2 requests use the stored token from the preceding IMDSv2 command, assuming the token has not expired.
IMDSv1 [ec2-user ~]$ curl http://169.254.169.254/latest/meta-data/ami-launch-index 2
2. She saves the ami-launch-index as a variable.
IMDSv2 [ec2-user ~]$ ami_launch_index=`curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/ami-launch-index`
IMDSv1 [ec2-user ~]$ ami_launch_index=`curl http://169.254.169.254/latest/meta-data/ami- launch-index`
3. She saves the user data as a variable.
IMDSv2 [ec2-user ~]$ user_data=`curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/user-data`
IMDSv1 [ec2-user ~]$ user_data=`curl http://169.254.169.254/latest/user-data`
4. Finally, Alice uses the cut command to extract the portion of the user data that is applicable to that instance.
IMDSv2 [ec2-user ~]$ echo $user_data | cut -d"|" -f"$ami_launch_index" replicate-every=5min
