# Create an inventory of your EC2 instances

Source: apps/user-manuals/aws/ec2-ug.pdf

---

## Capacity Reservations Code Description Units region-Reservat ion :instance- type The reserved instance time for Capacity Reservations.
Hours region-UnusedBo x :instance-type The unused reserved instance time for Capacity Reservations.
Hours region-Dedicate dRes :instance- type The reserved instance time for Dedicated Capacity Reservations.
Hours region-UnusedDe d :instance-type The unused reserved instance time for Dedicated Capacity Reservations.
Hours
# Create an inventory of your EC2 instances Amazon EC2 provides on-demand, scalable computing capacity. An EC2 instance is a virtual server that runs in the AWS network.
The following table describes the key characteristics of an EC2 instance. A system administrator can use the guidance provided in this guide to get information about these characteristics and use it to configure functionally equivalent servers that run on premises or in the network of another Cloud Provider.
Characteristic Description
## Geographic location Amazon EC2 is hosted in all AWS Regions world-wide. You select locations for your instances that put them close to your customers. You can launch instances in multiple locations.

Characteristic Description
## Hardware specifications Amazon EC2 provides a wide selection of instance types, optimized for different use cases. The instance types that you select for your instances determine their compute, memory, networking, and storage resources.
## Images An Amazon Machine Image (AMI) includes the software to install on your instance at launch.
This includes the operating system, software packages, and custom configurations.
## IP addresses and DNS hostnames Instances receive private IP addresses and a private DNS hostname. If you configure a public IP address for an instance, it also receives a public DNS hostname.
## Security group rules The security group rules associated with your instances determines which inbound traffic and outbound traffic is allowed.
## User data User data is made available to instances at launch. It consists of shell scripts (Linux) or PowerShell scripts (Windows).
Geographic location Amazon EC2 is available in every AWS Region world-wide. Each Region is a separate geographic area. You can lower network latency when you select Regions for your servers that are close to the majority of your users.
You can use Amazon EC2 Global View to list your Amazon EC2 instances across all Regions.
With the AWS Management Console and the API, you must list the instances for each Region individually.
Why this matters

After you determine where your instances are located, you can decide whether to deploy functionally equivalent servers in the same locations or different locations, depending on your needs.
To get a summary of your EC2 instances across all Regions
1. Open the Amazon EC2 Global View console at https://console.aws.amazon.com/ ec2globalview/home.
2. On the Region explorer tab, under Summary, check the resource count for Instances, which includes the number of instances and the number of Regions. Click the underlined text to see how the instance count is spread across Regions.
3. On the Global search tab, select the client filter Resource type = Instance. You can filter the results further by specifying a Region or a tag.
To get the number of EC2 instances in a Region using the AWS CLI Use the following describe-instances command to count the instances in the specified Region. You must run this command in each Region where you have instances. aws ec2 describe-instances \ --region us-east-2 \ --query "length(Reservations[*].Instances[])"
The following is example output.
27 To get a list of the instance IDs instead of the count of instances, use the following --query parameter instead.
--query "Reservations[*].Instances[].InstanceId"
Hardware specifications The instance type that you specify for an EC2 instance determines the compute, memory, storage, and networking resources that are available to it. Each instance family offers a different balance of compute, memory, network, and storage resources. For more information, see the Amazon EC2 Instance Types Guide.

Why these matter After you determine the hardware specifications for your instances, you can decide the minimum specifications required for functionally equivalent servers.
To get a summary of the instance types used by your instances Use the following describe-instances command. The sed command removes lines with brackets and empty lines. You must run this command in each Region where you have instances. aws ec2 describe-instances \ --query "Reservations[*].Instances[].InstanceType" | sed 's/[][]//g;/^$/d' | sort | uniq -c | sort -nr The following is example output.
  20    "c6i.4xlarge", 5    "t2.micro", 2    "g6e.2xlarge", To get information about specific instance types Use the following describe-instance-types command to describe the instance types. The --query parameter includes only the specified fields in the output. These are the basic characteristics. You can include any additional fields that you need, or you can refer to Amazon EC2 instance type specifications in the Amazon EC2 Instance Types Guide. aws ec2 describe-instance-types \ --instance-types c6i.4xlarge t2.micro g6e.2xlarge \ --query "InstanceTypes[*].
[InstanceType,VCpuInfo.DefaultVCpus,MemoryInfo.SizeInMiB,NetworkInfo.NetworkPerformance]"
 \ --output table The following is example output. The columns are instance type, vCPUs, memory (GiB), and network bandwidth (Gbps).
------------------------------------------------------
|                DescribeInstanceTypes               | +--------------+-----+--------+----------------------+

|  t2.micro    |  1  |  1024  |  Low to Moderate     |
|  c6i.4xlarge |  16 |  32768 |  Up to 12.5 Gigabit  |
|  g6e.2xlarge |  8  |  65536 |  Up to 20 Gigabit    | +--------------+-----+--------+----------------------+ Images An Amazon Machine Image (AMI) provides the software that's installed on your instance at launch, such as the operating system, services, development tools, and applications. You can export an AMI to other formats for use with other servers.
Why these matter After you determine the AMIs for your instances, you can plan the images required for functionally equivalent servers. It might be possible to export your AMIs to a format that you can use elsewhere. Alternatively, you might need to connect to an instance that you launched from each AMI, confirm what's installed and how it's configured, and ensure that you have a copy of everything that you need.
To get the AMIs for your instances Use the following describe-instances command. The sed command removes lines with brackets and empty lines. You must run this command in each Region where you have instances. aws ec2 describe-instances \ --query "Reservations[*].Instances[].ImageId" | sed 's/[][]//g;/^$/d' | sort | uniq -c | sort -nr The following is example output.
20     "ami-0a70b9d193ae8a79", 5     "ami-07d9cf938edb0739b", 2     "ami-09245d5773578a1d6", To get information about specific AMIs Use the following describe-images command. The --query parameter includes only the specified fields in the output. You can include any additional fields that you need. aws ec2 describe-images \

    --image-id ami-0a70b9d193ae8a79 ami-07d9cf938edb0739b ami-09245d5773578a1d6 \ --query "Images[*].
{ID:ImageId,CreateDate:CreationDate,Name:Name,Description:Description}"
The following is example output.
[ { "ID": "ami-0a70b9d193ae8a799", "CreateDate": "2025-03-01T02:22:41.000Z", "Name": "web-server-3.1", "Description": "Image for web servers"
    }, { "ID": "ami-07d9cf938edb0739b", "CreateDate": "2025-02-01T23:59:03.000Z", "Name": "awesome-application-11.5", "Description": "Image for Awesome Application"
    }, { "ID": "ami-09245d5773578a1d6", "CreateDate": "2025-01-31T02:22:41.000Z", "Name": "monitoring-4.2", "Description": "Monitoring software"
    } ]
To create a VM file from an AMI Use the export-image command. The supported image formats are VHD (compatible with Citrix Xen and Microsoft Hyper-V), VMDK (compatible with VMware ESX and VMware vSphere), and raw format (compatible with KVM and Xen hypervisors). For information about the requirements and limitations of VM Import/Export, see VM Import/Export requirements.
IP addresses and DNS hostnames Your users connect to your EC2 instances over the internet using their public DNS hostnames.
The public DNS hostname of an EC2 instance resolves to its public IP address. EC2 instances can communicate with each other using their private IP addresses.
Why these matter

IP addresses allow devices to communicate with each other over a local network or the internet. By noting the IP addresses and DNS names of your instances, you can help to ensure that functionally equivalent servers can communicate with the same clients or devices as your instances. For example, you can update your load balancer configuration or the DNS records that you created for your DNS provider.
To get the IP addresses and DNS hostnames for your instances Use the following describe-instances command. You must run this command in each Region where you have instances. The --query parameter includes only the specified fields in the output. You can include any additional fields that you need. aws ec2 describe-instances \ --query "Reservations[*].Instances[].[InstanceId,PrivateIpAddress,PublicDnsName]" \ --output table The following is example output. The columns are instance ID, private IPv4 address, and public IPv4 DNS name.
----------------------------------------------------------------------------------------
|                                   DescribeInstances
 | +---------------------+------------+--------------------------------------------------- +
| i-0bac57d7472c89bac | 10.0.2.139 | ec2-192-0-2-142.us-east-2.compute.amazonaws.com
 |
| i-0fa8b7678975a3fff | 10.0.14.85 | ec2-198-51-100-56.us-east-2.compute.amazonaws.com
 | ...
  ...
| i-08fd74f3f1595fdbd | 10.0.1.241 | ec2-203.0.113.13.us-east-2.compute.amazonaws.com
 | +---------------------+------------+--------------------------------------------------- + Security group rules A security group acts as a virtual firewall. After you associate a security group with an EC2 instance, its rules allow inbound and outbound traffic for the EC2 instance over specific ports and protocols.
Why these matter

After you determine the inbound traffic allowed to reach your server and the outbound traffic allowed to leave your server, you can plan the firewall rules needed for functionally equivalent servers.
To get the security groups for your instances Use the following describe-instances command. The sed command removes lines with brackets and empty lines. You must run this command in each Region where you have instances. aws ec2 describe-instances \ --query "Reservations[*].Instances[].SecurityGroups[].GroupId" | sed 's/[][]//g;/^ $/d' | sort | uniq -c | sort -nr The following is example output.
27     "sg-01dd3383691d02f42", 10     "sg-08c77cc910c0b3b2c", 2     "sg-00f4e409629f1a42d", To get the inbound rules for a security group Use the following describe-security-group-rules command to display the rules for the specified security group where IsEgress is false. aws ec2 describe-security-group-rules \ --filters Name=group-id,Values=sg-01dd3383691d02f42 \ --query 'SecurityGroupRules[?IsEgress==`false`]'
The following is example output. The first rule is the default inbound rule, which allows inbound traffic from all resources that are assigned to this security group. The other rule allows SSH traffic from the IP addresses in the specified prefix list. To describe the CIDR blocks in a prefix list, use the describe-prefix-lists command.
[ { "SecurityGroupRuleId": "sgr-06c8b42574a91db1b", "GroupId": "sg-01dd3383691d02f42", "GroupOwnerId": "123456789012", "IsEgress": false, "IpProtocol": "-1", "FromPort": -1,

        "ToPort": -1, "ReferencedGroupInfo": { "GroupId": "sg-01dd3383691d02f42", "UserId": "123456789012"
        }, "Tags": [], "SecurityGroupRuleArn": "arn:aws:ec2:us-west-2:123456789012:security-group- rule/sgr-06c8b42574a91db1b"
    }, { "SecurityGroupRuleId": "sgr-0886a5d46afcd1758", "GroupId": "sg-01dd3383691d02f42", "GroupOwnerId": "123456789012", "IsEgress": false, "IpProtocol": "tcp", "FromPort": 22, "ToPort": 22, "PrefixListId": "pl-f8a6439125e7bf465", "Tags": [], "SecurityGroupRuleArn": "arn:aws:ec2:us-east-2:123456789012:security-group- rule/sgr-0886a5d46afcd1758"
    } ]
To get the outbound rules for a security group Use the following describe-security-group-rules command to display the rules for the specified security group where IsEgress is true. aws ec2 describe-security-group-rules \ --filters Name=group-id,Values=sg-01dd3383691d02f42 \ --query 'SecurityGroupRules[?IsEgress==`true`]'
The following is example output. It contains only the default outbound rule, which allows all outbound IPv4 traffic.
[ { "SecurityGroupRuleId": "sgr-048f09a719247dce7", "GroupId": "sg-01dd3383691d02f42", "GroupOwnerId": "123456789012", "IsEgress": true,

        "IpProtocol": "-1", "FromPort": -1, "ToPort": -1, "CidrIpv4": "0.0.0.0/0", "Tags": [], "SecurityGroupRuleArn": "arn:aws:ec2:us-east-2:123456789012:security-group- rule/sgr-048f09a719247dce7"
    } ]
User data When you launch an EC2 instance, you can pass a shell script to the instance using user data. Note that user data is base64 encoded, so you need to decode the user data to read the script.
Why this matters If you're running commands at launch as part of setting up your instances, you might need to perform the same tasks when setting up functionally equivalent servers.
To view the decoded user data for an instance Use the following describe-instance-attribute command. The base64 command decodes the user data. aws ec2 describe-instance-attribute \ --instance-id i-1234567890abcdef0 \ --attribute userData \ --output text \ --query "UserData.Value" | base64 --decode The following is example output.
#!/bin/bash yum update -y service httpd start chkconfig httpd on
## Related resources The following are additional characteristics of EC2 instances:

- Key pairs
- Storage
- Tags You can verify whether you're using the following to launch EC2 instances or distribute traffic between your EC2 instances:
- Auto Scaling groups
- EC2 Fleet
- Elastic Load Balancing
