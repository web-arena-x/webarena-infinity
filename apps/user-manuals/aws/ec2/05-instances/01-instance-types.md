# Amazon EC2 instance types

Source: apps/user-manuals/aws/ec2-ug.pdf

---

- Automatic instance recovery
- Use instance metadata to manage your EC2 instance
- Detect whether a host is an EC2 instance
- Instance identity documents for Amazon EC2 instances
- STIG compliance for your EC2 instance
- Precision clock and time synchronization on your EC2 instance
- EC2 Capacity Manager
- Manage device drivers for your EC2 instance
- Configure your Amazon EC2 Windows instance
- Upgrade an EC2 Windows instance to a newer version of Windows Server
- Tutorial: Connect an Amazon EC2 instance to an Amazon RDS database
# Amazon EC2 instance types When you launch an instance, the instance type that you specify determines the hardware of the host computer used for your instance. Each instance type offers different compute, memory, and storage capabilities, and is grouped in an instance family based on these capabilities. Select an instance type based on the requirements of the application or software that you plan to run on your instance. For more information about features and use cases, see Amazon EC2 Instance Types.
Amazon EC2 dedicates some resources of the host computer, such as CPU, memory, and instance storage, to a particular instance. Amazon EC2 shares other resources of the host computer, such as the network and the disk subsystem, among instances. If each instance on a host computer tries to use as much of one of these shared resources as possible, each receives an equal share of that resource. However, when a resource is underused, an instance can consume a higher share of that resource while it's available.
Each instance type provides higher or lower minimum performance from a shared resource. For example, instance types with high I/O performance have a larger allocation of shared resources.
Allocating a larger share of shared resources also reduces the variance of I/O performance. For most applications, moderate I/O performance is more than enough. However, for applications that require greater or more consistent I/O performance, consider an instance type with higher I/O performance.
Contents

- Available instance types
- Hardware specifications
- Hypervisor type
- AMI virtualization types
- Processors
- Find an Amazon EC2 instance type
- Get recommendations from EC2 instance type finder
- Get EC2 instance recommendations from Compute Optimizer
- Amazon EC2 instance type changes
- Burstable performance instances
- Performance acceleration with GPU instances
- Amazon EC2 Mac instances
- Amazon EBS-optimized instance types
- CPU options for Amazon EC2 instances
- AMD SEV-SNP for Amazon EC2 instances
- Processor state control for Amazon EC2 Linux instances
## Available instance types Amazon EC2 provides a wide selection of instance types optimized to fit different use cases.
Instance types comprise varying combinations of CPU, memory, storage, and networking capacity and give you the flexibility to choose the appropriate mix of resources for your applications. Each instance type includes one or more instance sizes, allowing you to scale your resources to the requirements of your target workload.
Instance type naming conventions Names are based on instance family, generation, processor family, capabilities, and size. For more information, see Naming conventions in the Amazon EC2 Instance Types Guide.
Find an instance type To determine which instance types meet your requirements, such as supported Regions, compute resources, or storage resources, see Find an Amazon EC2 instance type and Amazon EC2 instance type specifications in the Amazon EC2 Instance Types Guide.

## Hardware specifications For detailed instance type specifications, see Specifications in the Amazon EC2 Instance Types Guide. For pricing information, see Amazon EC2 On-Demand Pricing.
To determine which instance type best meets your needs, we recommend that you launch an instance and use your own benchmark application. Because you pay by the instance second, it's convenient and inexpensive to test multiple instance types before making a decision. If your needs change, even after you make a decision, you can change the instance type later. For more information, see Amazon EC2 instance type changes.
## Hypervisor type Amazon EC2 supports the following hypervisors: Xen and Nitro.
Nitro-based instances
- General purpose: M5 | M5a | M5ad | M5d | M5dn | M5n | M5zn | M6a | M6g | M6gd | M6i | M6id
| M6idn | M6in | M7a | M7g | M7gd | M7i | M7i-flex | M8a | M8azn | M8g | M8gb | M8gd | M8gn | M8i | M8id | M8i-flex | T3 | T3a | T4g
- Compute optimized: C5 | C5a | C5ad | C5d | C5n | C6a | C6g | C6gd | C6gn | C6i | C6id | C6in | C7a
| C7g | C7gd | C7gn | C7i | C7i-flex | C8a | C8g | C8gb | C8gd | C8gn | C8i | C8id | C8i-flex
- Memory optimized: R5 | R5a | R5ad | R5b | R5d | R5dn | R5n | R6a | R6g | R6gd | R6i | R6id | R6idn | R6in | R7a | R7g | R7gd | R7i | R7iz | R8a | R8g | R8gb | R8gd | R8gn | R8i | R8id | R8i- flex | U-3tb1 | U-6tb1 | U-9tb1 | U-12tb1 | U-18tb1 | U-24tb1 | U7i-6tb | U7i-8tb | U7i-12tb | U7in-16tb | U7in-24tb | U7in-32tb | U7inh-32tb | X2gd | X2idn | X2iedn | X2iezn | X8g | X8aedz | X8i | z1d
- Storage optimized: D3 | D3en | I3en | I4g | I4i | I7i | I7ie | I8g | I8ge | Im4gn | Is4gen
- Accelerated computing: DL1 | DL2q | F2 | G4ad | G4dn | G5 | G5g | G6 | G6e | G6f | Gr6 | Gr6f | G7e | Inf1 | Inf2 | P4d | P4de | P5 | P5e | P5en | P6-B200 | P6-B300 | P6e-GB200 | Trn1 | Trn1n | Trn2 | Trn2u | VT1
- High-performance computing: Hpc6a | Hpc6id | Hpc7a | Hpc7g | Hpc8a
- Previous generation: A1 | P3dn For more information about the supported versions of Nitro hypervisor, see Network feature support in the Amazon EC2 Instance Types Guide.

Xen-based instances
- General purpose: M1 | M2 | M3 | M4 | T1 | T2
- Compute optimized: C1 | C3 | C4
- Memory optimized: R3 | R4 | X1 | X1e
- Storage optimized: D2 | H1 | I2 | I3
- Accelerated computing: F1 | G3 | P2 | P3
## AMI virtualization types The virtualization type of your instance is determined by the AMI that you use to launch it. Current generation instance types support hardware virtual machine (HVM) only. Some previous generation instance types support paravirtual (PV) and some AWS Regions support PV instances. For more information, see Virtualization types.
For best performance, we recommend that you use an HVM AMI. In addition, HVM AMIs are required to take advantage of enhanced networking. HVM virtualization uses hardware-assist technology provided by the AWS platform. With HVM virtualization, the guest VM runs as if it were on a native hardware platform, except that it still uses PV network and storage drivers for improved performance.
## Processors EC2 instances support a variety of processors.
Processors
- Intel processors
- AMD processors
- AWS Graviton processors
- AWS Trainium
- AWS Inferentia
### Intel processors Amazon EC2 instances that run on Intel processors might include the following processor features. Not all instances that run on Intel processors support all of these processor features. For

information about which features are available for each instance type, see Amazon EC2 Instance types.
- Intel AES New Instructions (AES-NI) — Intel AES-NI encryption instruction set improves upon the original Advanced Encryption Standard (AES) algorithm to provide faster data protection and greater security. All current generation EC2 instances support this processor feature.
- Intel Advanced Vector Extensions (Intel AVX, Intel AVX2, and Intel AVX-512) — Intel AVX and Intel AVX2 are 256-bit, and Intel AVX-512 is a 512-bit instruction set extension designed for applications that are Floating Point (FP) intensive. Intel AVX instructions improve performance for applications like image and audio/video processing, scientific simulations, financial analytics, and 3D modeling and analysis. These features are only available on instances launched with HVM AMIs.
- Intel Turbo Boost Technology — Intel Turbo Boost Technology processors automatically run cores faster than the base operating frequency.
- Intel Deep Learning Boost (Intel DL Boost) — Accelerates AI deep learning use cases. The 2nd Gen Intel Xeon Scalable processors extend Intel AVX-512 with a new Vector Neural Network Instruction (VNNI/INT8) that significantly increases deep learning inference performance over previous generation Intel Xeon Scalable processors (with FP32) for image recognition/ segmentation, object detection, speech recognition, language translation, recommendation systems, reinforcement learning, and more. VNNI may not be compatible with all Linux distributions.
The following instances support VNNI: M5n, R5n, M5dn, M5zn, R5b, R5dn, D3, D3en, and C6i. C5 and C5d instances support VNNI for only 12xlarge, 24xlarge, and metal instances.
Confusion can result from industry naming conventions for 64-bit CPUs. Chip manufacturer Advanced Micro Devices (AMD) introduced the first commercially successful 64-bit architecture based on the Intel x86 instruction set. Consequently, the architecture is widely referred to as AMD64 regardless of the chip manufacturer. Windows and several Linux distributions follow this practice. This explains why the internal system information on an instance running Ubuntu or Windows displays the CPU architecture as AMD64 even though the instances are running on Intel hardware.
### AMD processors Amazon EC2 instances that run on AMD EPYC processors can help you optimize both cost and performance for your workloads. These instances might support the following processor

features. Not all instances that run on AMD processors support all of these processor features. For information about which features are available for each instance type, see Amazon EC2 Instance types.
- AMD Secure Memory Encryption (SME)
- AMD Transparent Single Key Memory Encryption (TSME)
- AMD Advanced Vector Extensions (AVX)
- AMD Secure Encrypted Virtualization-Secure Nested Paging (SEV-SNP)
- Vector Neural Network Instructions (VNNI)
- BFloat16
### AWS Graviton processors AWS Graviton is a family of processors designed to deliver the best price performance for your workloads running on Amazon EC2 instances.
For more information, see Getting started with Graviton.
### AWS Trainium Instances powered by AWS Trainium are purpose built for high-performance, cost-effective deep learning training. You can use these instances to train natural language processing, computer vision, and recommender models used across a broad set of applications, such as speech recognition, recommendation, fraud detection, and image and video classification. Use your existing workflows in popular ML frameworks, such as PyTorch and TensorFlow.
### AWS Inferentia Instances powered by AWS Inferentia are designed to accelerate machine learning. They provide high performance and low latency machine learning inference. These instances are optimized for deploying deep learning (DL) models for applications, such as natural language processing, object detection and classification, content personalization and filtering, and speech recognition.
There are a variety of ways that you can get started:
- Use SageMaker AI, a fully-managed service that is the easiest way to get started with machine learning models. For more information, see Get Started with SageMaker AI in the Amazon SageMaker AI Developer Guide.

- Launch an Inf1 or Inf2 instance using the Deep Learning AMI. For more information, see AWS Inferentia with DLAMI in the AWS Deep Learning AMIs Developer Guide.
- Launch an Inf1 or Inf2 instance using your own AMI and install the AWS Neuron SDK, which enables you to compile, run, and profile deep learning models for AWS Inferentia.
- Launch a container instance using an Inf1 or Inf2 instance and an Amazon ECS-optimized AMI.
For more information, see Amazon Linux 2 (Inferentia) AMIs in the Amazon Elastic Container Service Developer Guide.
- Create an Amazon EKS cluster with nodes running Inf1 instances. For more information, see Inferentia support in the Amazon EKS User Guide.
## Find an Amazon EC2 instance type Before you can launch an instance, you must select an instance type to use. The instance type that you choose might depend on the resources that your workload requires, such as compute, memory, or storage resources. It can be beneficial to identify several instance types that might suit your workload and evaluate their performance in a test environment. There is no substitute for measuring the performance of your application under load.
You can get suggestions and guidance for EC2 instance types using the EC2 instance type finder.
For more information, see the section called "EC2 instance type finder".
If you already have running EC2 instances, you can use AWS Compute Optimizer to get recommendations about the instance types that you should use to improve performance, save money, or both. For more information, see the section called "Compute Optimizer recommendations".
Tasks
- Find an instance type using the console
- Describe an instance type using the AWS CLI
- Find an instance type using the AWS CLI
- Find an instance type using the Tools for PowerShell
### Find an instance type using the console You can find an instance type that meets your needs using the Amazon EC2 console.

To find an instance type using the console
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. From the navigation bar, select the Region in which to launch your instances. You can select any Region that's available to you, regardless of your location.
3. In the navigation pane, choose Instance Types.
4. (Optional) Choose the preferences (gear) icon to select which instance type attributes to display, such as On-Demand Linux pricing, and then choose Confirm. Alternatively, select the name of an instance type to open its details page and view all attributes available through the console. The console does not display all the attributes available through the API or the command line.
5. Use the instance type attributes to filter the list of displayed instance types to only the instance types that meet your needs. For example, you can filter on the following attributes:
- Availability zones – The name of the Availability Zone, Local Zone, or Wavelength Zone. For more information, see the section called "Regions and Zones".
- vCPUs or Cores – The number of vCPUs or cores.
- Memory (GiB) – The memory size, in GiB.
- Network performance – The network performance, in Gigabits.
- Local instance storage – Indicates whether the instance type has local instance storage (true | false).
6. (Optional) To see a side-by-side comparison, select the checkbox for multiple instance types.
The comparison is displayed at the bottom of the screen.
7. (Optional) To save the list of instance types to a comma-separated values (.csv) file for further review, choose Actions, Download list CSV. The file includes all instance types that match the filters you set.
8. (Optional) To launch instances using an instance type that meet your needs, select the checkbox for the instance type and choose Actions, Launch instance. For more information, see Launch an EC2 instance using the launch instance wizard in the console.
### Describe an instance type using the AWS CLI You can use the describe-instance-types command to describe a specific instance type.
To fully describe an instance type

The following command displays all available details for the specified instance type. The output is lengthy, so it is omitted here. aws ec2 describe-instance-types \ --instance-types t2.micro \ --region us-east-2 The describe an instance type and filter the output The following command displays the networking details for the specified instance type. aws ec2 describe-instance-types \ --instance-types t2.micro \ --region us-east-2 \ --query "InstanceTypes[].NetworkInfo"
The following is example output.
[ { "NetworkPerformance": "Low to Moderate", "MaximumNetworkInterfaces": 2, "MaximumNetworkCards": 1, "DefaultNetworkCardIndex": 0, "NetworkCards": [ { "NetworkCardIndex": 0, "NetworkPerformance": "Low to Moderate", "MaximumNetworkInterfaces": 2, "BaselineBandwidthInGbps": 0.064, "PeakBandwidthInGbps": 1.024 } ], "Ipv4AddressesPerInterface": 2, "Ipv6AddressesPerInterface": 2, "Ipv6Supported": true, "EnaSupport": "unsupported", "EfaSupported": false, "EncryptionInTransitSupported": false, "EnaSrdSupported": false } ]

The following command displays the available memory for the specified instance type. aws ec2 describe-instance-types \ --instance-types t2.micro \ --region us-east-2 \ --query "InstanceTypes[].MemoryInfo"
The following is example output.
[ { "SizeInMiB": 1024 } ]
### Find an instance type using the AWS CLI You can use the describe-instance-types and describe-instance-type-offerings commands to find the instance types that meet your needs.
Examples
- Example 1: Find an instance type by Availability Zone
- Example 2: Find an instance type by available memory size
- Example 3: Find an instance type by available instance storage
- Example 4: Find an instance type that supports hibernation
#### Example 1: Find an instance type by Availability Zone The following example displays only the instance types offered in the specified Availability Zone. aws ec2 describe-instance-type-offerings \ --location-type "availability-zone" \ --filters "Name=location,Values=us-east-2a" \ --region us-east-2 \ --query "InstanceTypeOfferings[*].[InstanceType]" --output text | sort The output is a list of instance types, sorted alphabetically. The following is the start of the output only.

a1.2xlarge a1.4xlarge a1.large a1.medium a1.metal a1.xlarge c4.2xlarge ...
#### Example 2: Find an instance type by available memory size The following example displays only current generation instance types with 64 GiB (65536 MiB) of memory. aws ec2 describe-instance-types \ --filters "Name=current-generation,Values=true" "Name=memory-info.size-in- mib,Values=65536" \ --region us-east-2 \ --query "InstanceTypes[*].[InstanceType]" --output text | sort The output is a list of instance types, sorted alphabetically. The following is the start of the output only. c5a.8xlarge c5ad.8xlarge c6a.8xlarge c6g.8xlarge c6gd.8xlarge c6gn.8xlarge c6i.8xlarge c6id.8xlarge c6in.8xlarge ...
#### Example 3: Find an instance type by available instance storage The following example displays the total size of instance storage for all R7 instances with instance store volumes. aws ec2 describe-instance-types \

    --filters "Name=instance-type,Values=r7*" "Name=instance-storage- supported,Values=true" \ --region us-east-2 \ --query "InstanceTypes[].[InstanceType, InstanceStorageInfo.TotalSizeInGB]" \ --output table The following is example output.
---------------------------
|  DescribeInstanceTypes  | +----------------+--------+
|  r7gd.xlarge   |  237   |
|  r7gd.8xlarge  |  1900  |
|  r7gd.16xlarge |  3800  |
|  r7gd.medium   |  59    |
|  r7gd.4xlarge  |  950   |
|  r7gd.2xlarge  |  474   |
|  r7gd.metal    |  3800  |
|  r7gd.large    |  118   |
|  r7gd.12xlarge |  2850  | +----------------+--------+
#### Example 4: Find an instance type that supports hibernation The following example displays the instance types that support hibernation. aws ec2 describe-instance-types \ --filters "Name=hibernation-supported,Values=true" \ --region us-east-2 \ --query "InstanceTypes[*].[InstanceType]" \ --output text | sort The output is a list of instance types, sorted alphabetically. The following is the start of the output only. c4.2xlarge c4.4xlarge c4.8xlarge c4.large c4.xlarge c5.12xlarge c5.18xlarge

c5.2xlarge c5.4xlarge c5.9xlarge ...
### Find an instance type using the Tools for PowerShell You can use the Get-EC2InstanceType and Get-EC2InstanceTypeOffering cmdlets to find the instance types that meet your needs.
Examples
- Find an instance type by Availability Zone
- Find an instance type by available memory size
- Find an instance type by available instance storage
- Find an instance type that supports hibernation
#### Find an instance type by Availability Zone The following example displays only the instance types offered in the specified Availability Zone.
(Get-EC2InstanceTypeOffering `
    -LocationType "availability-zone" `
    -Region us-east-2 `
    -Filter @{Name="location"; Values="us-east-2a"}).InstanceType | Sort-Object `
#### Find an instance type by available memory size The following example displays only current generation instance types with 64 GiB (65536 MiB) of memory.
(Get-EC2InstanceType `
    -Filter @{Name="current-generation"; Values="true"}, @{Name="memory-info.size-in-mib"; Values="65536"}).InstanceType | Sort- Object
#### Find an instance type by available instance storage The following example displays the total size of instance storage for all R7 instances with instance store volumes.

Get-EC2InstanceType `
    -Filter @{Name="instance-type"; Values="r7*"}, @{Name="instance-storage-supported"; Values="true"} | `
     Select InstanceType, @{Name="TotalSizeInGB"; Expression={($_.InstanceStorageInfo.TotalSizeInGB)}} The following is example output.
InstanceType  TotalSizeInGB ------------  ------------- r7gd.8xlarge           1900 r7gd.16xlarge          3800 r7gd.xlarge             237 r7gd.4xlarge            950 r7gd.medium              59 r7gd.2xlarge            474 r7gd.large              118 r7gd.metal             3800 r7gd.12xlarge          2850
#### Find an instance type that supports hibernation The following example displays the instance types that support hibernation.
(Get-EC2InstanceType `
    -Filter @{Name="hibernation-supported"; Values="true"}).InstanceType | Sort-Object
## Get recommendations from EC2 instance type finder EC2 instance type finder considers your use case, workload type, CPU manufacturer preference, and how you prioritize price and performance, as well as additional parameters that you can specify. It then uses this data to provide suggestions and guidance for Amazon EC2 instance types that are best suited to your new workloads.
With so many instance types available, finding the right instance types for your workload can be time-consuming and complex. By using the EC2 instance type finder, you can remain up to date with the latest instance types and achieve the best price-performance for your workloads.
You can get suggestions and guidance for EC2 instance types using the Amazon EC2 console. You can also go directly to Amazon Q to ask for instance type advice. For more information, see the Amazon Q Developer User Guide.

If you're looking for instance type recommendations for an existing workload, use AWS Compute Optimizer. For more information, see Get EC2 instance recommendations from Compute Optimizer.
### Use the EC2 instance type finder In the Amazon EC2 console, you can get instance type suggestions from the EC2 instance type finder in the launch instance wizard, when creating a launch template, or on the Instance types page.
Use the following instructions to get suggestions and guidance for EC2 instance types using the EC2 instance type finder in the Amazon EC2 console. To view an animation of the steps, see View an animation: Get instance type suggestions using the EC2 instance type finder.
To get instance type suggestions using the EC2 instance type finder
1. Start your process using any of the following:
- Follow the procedure to launch an instance. Next to Instance type, choose the Get advice link.
- Follow the procedure to create a launch template. Next to Instance type, choose the Get advice link.
- In the navigation pane, choose Instance Types, and then choose the Instance type finder button.
2. In the Get advice on instance type selection screen, do the following: a.
Specify your instance type requirements by selecting options for Workload type, Use case, Priority, and CPU manufacturers. b.
(Optional) To specify more detailed requirements for your workload, do the following: i.
Expand Advanced parameters. ii.
To add a parameter, select a parameter, choose Add, and specify a value for the parameter. Repeat for each additional parameter that you want to add. To indicate no minimum or maximum value, leave the field empty. iii.
To remove a parameter after adding it, choose the X next to the parameter. c.
Choose Get instance type advice.
Amazon EC2 provides you with suggestions for instance families matching your specified requirements.

3. To view the details of each instance type within the suggested instance families, choose View recommended instance family details.
4. Select an instance type that meets your requirements, and then choose Actions, Launch instance or Actions, Create launch template.
Alternatively, if you started the process in the launch instance wizard or the launch template page, and you prefer to go back to your original flow, make note of the instance type you'd like to use. Then, in the launch instance wizard or launch template, for Instance type, choose the instance type, and complete the procedure to launch an instance or create a launch template.
#### View an animation: Get instance type suggestions using the EC2 instance type finder
## Get EC2 instance recommendations from Compute Optimizer AWS Compute Optimizer provides Amazon EC2 recommendations to help you improve performance, save money, or both. You can use these recommendations to decide whether to change to a new instance type.
To make recommendations, Compute Optimizer analyzes your existing instance specifications and utilization metrics. The compiled data is then used to recommend which Amazon EC2 instance

types are best able to handle the existing workload. Recommendations are returned along with per-hour instance pricing. For more information, see Amazon EC2 instance metrics in the AWS Compute Optimizer User Guide.
Contents
- Requirements
- Finding classifications
- View recommendations
- Considerations for evaluating recommendations
### Requirements To get recommendations from Compute Optimizer, you must first opt in to Compute Optimizer.
For more information, see Getting started with AWS Compute Optimizer in the AWS Compute Optimizer User Guide.
Compute Optimizer generates recommendations for some instance types, but not all instance types. If you're using an unsupported instance type, Compute Optimizer will not generate recommendations. For the list of supported instance types, see Amazon EC2 instance requirements in the AWS Compute Optimizer User Guide.
### Finding classifications Compute Optimizer classifies its findings for EC2 instances as follows:
- Under-provisioned – An EC2 instance is considered under-provisioned when at least one specification of your instance, such as CPU, memory, or network, does not meet the performance requirements of your workload. Under-provisioned EC2 instances might lead to poor application performance.
- Over-provisioned – An EC2 instance is considered over-provisioned when at least one specification of your instance, such as CPU, memory, or network, can be sized down while still meeting the performance requirements of your workload, and when no specification is under- provisioned. Over-provisioned EC2 instances might lead to unnecessary infrastructure cost.
- Optimized – An EC2 instance is considered optimized when all specifications of your instance, such as CPU, memory, and network, meet the performance requirements of your workload, and the instance is not over-provisioned. An optimized EC2 instance runs your workloads with

optimal performance and infrastructure cost. For optimized instances, Compute Optimizer might sometimes recommend a new generation instance type.
- None – There are no recommendations for this instance. This might occur if you've been opted in to Compute Optimizer for less than 12 hours, or when the instance has been running for less than 30 hours, or when the instance type is not supported by Compute Optimizer.
### View recommendations After you opt in to Compute Optimizer, you can view the findings that Compute Optimizer generates for your EC2 instances in the Amazon EC2 console. You can then access the Compute Optimizer console to view the recommendations. If you recently opted in, findings might not be reflected in the EC2 console for up to 12 hours.
To view recommendations for an instance using the Amazon EC2 console
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Instances.
3. Choose the instance ID to open the instance detail page.
4. On the instance detail page, in the top summary section, locate AWS Compute Optimizer finding. If there is a finding, we display the finding classification and a link to view the details.
Otherwise, we display No recommendations available for this instance.
5. If there is a finding, choose View detail. This opens the Recommendations for EC2 instances page in the Compute Optimizer console. The current instance type is labeled Current. There are also up to three instance type recommendations, labeled Option 1, Option 2, and Option
3. This page also shows recent CloudWatch metric data for the instance.
To view recommendations for all instances in all Regions You can view recommendations for all of your Amazon EC2 instances in all Regions using the Compute Optimizer console. For more information, see Viewing EC2 instances recommendations and Viewing EC2 instance details in the AWS Compute Optimizer User Guide.
### Considerations for evaluating recommendations When you receive a recommendation, you must decide whether to act on it. Before changing an instance type, consider the following:

- The recommendations don't forecast your usage. Recommendations are based on your historical usage over the most recent 14-day time period. Be sure to choose an instance type that is expected to meet your future resource needs.
- Focus on the graphed metrics to determine whether actual usage is lower than instance capacity.
You can also view metric data (average, peak, percentile) in CloudWatch to further evaluate your EC2 instance recommendations. For example, notice how CPU percentage metrics change during the day and whether there are peaks that need to be accommodated. For more information, see Viewing Available Metrics in the Amazon CloudWatch User Guide.
- Compute Optimizer might supply recommendations for burstable performance instances, which are T3, T3a, and T2 instances. If you periodically burst above the baseline, make sure that you can continue to do so based on the vCPUs of the new instance type. For more information, see Key concepts for burstable performance instances.
- If you've purchased a Reserved Instance, your On-Demand Instance might be billed as a Reserved Instance. Before you change your current instance type, first evaluate the impact on Reserved Instance utilization and coverage.
- Consider conversions to newer generation instances, where possible.
- When migrating to a different instance family, make sure the current instance type and the new instance type are compatible, for example, in terms of virtualization, architecture, or network type. For more information, see Compatibility for changing the instance type.
- Finally, consider the performance risk rating that's provided for each recommendation.
Performance risk indicates the amount of effort you might need to spend in order to validate whether the recommended instance type meets the performance requirements of your workload. We also recommend rigorous load and performance testing before and after making any changes.
## Amazon EC2 instance type changes As your needs change, you might find that your instance is over-utilized (the instance type is too small) or under-utilized (the instance type is too large). If this is the case, you can resize your instance by changing its instance type. For example, if your t2.micro instance is too small for its workload, you can increase its size by changing it to a bigger T2 instance type, such as t2.large.
Or you can change it to another instance type, such as m5.large. You might also want to change from a previous generation to a current generation instance type to take advantage of some features, such as support for IPv6.

If you want a recommendation for an instance type that is best able to handle your existing workload, you can use AWS Compute Optimizer. For more information, see Get EC2 instance recommendations from Compute Optimizer.
When you change the instance type, you'll start paying the rate of the new instance type. For the on-demand rates of all instance types, see Amazon EC2 On-Demand Pricing.
To add additional storage to your instance without changing the instance type, add an EBS volume to the instance. For more information, see Attach an Amazon EBS volume to an instance in the Amazon EBS User Guide.
### Which instructions to follow?
There are different instructions for changing the instance type. The instructions to use depend on the instance's root volume, and whether the instance type is compatible with the instance's current configuration. For information about how compatibility is determined, see Compatibility for changing the instance type.
Use the following table to determine which instructions to follow.
Root volume Compatibility Use these instructions EBS Compatible Change the instance type EBS Not compatible Migrate to a new instance type Instance store Not applicable Migrate to a new instance type
### Compatibility for changing the instance type You can change the instance type only if the instance's current configuration is compatible with the instance type that you want. If the instance type that you want is not compatible with the instance's current configuration, you must launch a new instance with a configuration that is compatible with the instance type, and then migrate your application to the new instance.
Compatibility is determined through the following:

Virtualization type Linux AMIs use one of two types of virtualization: paravirtual (PV) or hardware virtual machine (HVM). If an instance was launched from a PV AMI, you can't change to an instance type that is HVM only. For more information, see Virtualization types. To check the virtualization type of your instance, check the Virtualization value on the details pane of the Instances screen in the Amazon EC2 console.
Architecture AMIs are specific to the architecture of the processor, so you must select an instance type with the same processor architecture as the current instance type. For example:
- If the current instance type has a processor based on the Arm architecture, you are limited to the instance types that support a processor based on the Arm architecture, such as C6g and M6g.
- The following instance types are the only instance types that support 32-bit AMIs: t2.nano, t2.micro, t2.small, t2.medium, c3.large, t1.micro, m1.small, m1.medium, and c1.medium. If you are changing the instance type of a 32-bit instance, you are limited to these instance types.
Network adapters If you switch from a driver for one network adapter to another, the network adapter settings are reset when the operating system creates the new adapter. To reconfigure the settings, you might need access to a local account with administrator permissions. The following are examples of moving from one network adapter to another:
- AWS PV (T2 instances) to Intel 82599 VF (M4 instances)
- Intel 82599 VF (most M4 instances) to ENA (M5 instances)
- ENA (M5 instances) to high-bandwidth ENA (M5n instances)
Enhanced networking Instance types that support enhanced networking require the necessary drivers installed. For example, Nitro-based instances require EBS-backed AMIs with the Elastic Network Adapter (ENA) drivers installed. To change from an instance type that does not support enhanced networking to an instance type that supports enhanced networking, you must install the ENA drivers or ixgbevf drivers on the instance, as appropriate.

Note When you resize an instance with ENA Express enabled, the new instance type must also support ENA Express. For a list of instance types that support ENA Express, see Supported instance types for ENA Express.
To change from an instance type that supports ENA Express to an instance type that does not support it, ensure that ENA Express is not currently enabled before you resize the instance.
NVMe EBS volumes are exposed as NVMe block devices on Nitro-based instances. If you change from an instance type that does not support NVMe to an instance type that supports NVMe, you must first install the NVMe drivers on your instance. Also, the device names for devices that you specify in the block device mapping are renamed using NVMe device names (/dev/ nvme[0-26]n1).
[Linux instances] Therefore, to mount file systems at boot time using /etc/fstab, you must use UUID/Label instead of device names.
Volume limit The maximum number of Amazon EBS volumes that you can attach to an instance depends on the instance type and instance size. For more information, see Amazon EBS volume limits for Amazon EC2 instances.
You can only change to an instance type or instance size that supports the same number or a larger number of volumes than is currently attached to the instance. If you change to an instance type or instance size that does not support the number of currently attached volumes, the request fails. For example, if you change from an m7i.4xlarge instance with 32 attached volumes to an m6i.4xlarge, which supports a maximum of 27 volumes, the request fails.
NitroTPM If you launched the instance using an AMI with NitroTPM enabled and an instance type that supports NitroTPM, the instance launches with NitroTPM enabled. You can only change to an instance type that also supports NitroTPM.

### Change the instance type for your Amazon EC2 instance Use the following instructions to change the instance type of an Amazon EBS-backed instance if the instance type that you need is compatible with the current configuration of your instance. For more information, see the section called "Compatibility".
### Considerations
- You must stop your instance before you can change its instance type. Ensure that you plan for downtime while your instance is stopped. Stopping the instance and changing its instance type might take a few minutes, and restarting your instance might take a variable amount of time depending on your application's startup scripts. For more information, see Stop and start Amazon EC2 instances.
- When you stop and start an instance, we move the instance to new hardware. If your instance has a public IPv4 address, that is not an Elastic IP, we release the address and give your instance a new public IPv4 address. For more information on IP address behavior throughout the lifecycle of an instance, see Differences between instance states.
- You can't change the instance type of a Spot Instance.
- [Windows instances] We recommend that you update the AWS PV driver package before changing the instance type. For more information, see the section called "Upgrade PV drivers".
- If your instance is in an Auto Scaling group, the Amazon EC2 Auto Scaling service marks the stopped instance as unhealthy, and might terminate it and launch a replacement instance. To prevent this, you can suspend the scaling processes for the group while you're changing the instance type. For more information, see Suspending and resuming a process for an Auto Scaling group in the Amazon EC2 Auto Scaling User Guide.
- When you change the instance type of an instance with NVMe instance store volumes, the updated instance might have additional instance store volumes, because all NVMe instance store volumes are available even if they are not specified in the AMI or instance block device mapping. Otherwise, the updated instance has the same number of instance store volumes that you specified when you launched the original instance.
- The maximum number of Amazon EBS volumes that you can attach to an instance depends on the instance type and instance size. You can't change to an instance type or instance size that does not support the number of volumes that are already attached to your instance. For more information, see Amazon EBS volume limits for Amazon EC2 instances.
- [Linux instances] You can use the AWSSupport-MigrateXenToNitroLinux runbook to migrate compatible Linux instances from a Xen instance type to a Nitro instance type. For more

information, see AWSSupport-MigrateXenToNitroLinux runbook in the AWS Systems Manager Automation runbook reference.
- [Windows instances] For additional guidance on migrating compatible Windows instances from a Xen instance type to a Nitro instance type, see Migrate to latest generation instance types.
To change the instance type of an Amazon EBS-backed instance
1. (Optional) If the new instance type requires drivers that are not installed on the existing instance, you must connect to your instance and install the drivers first. For more information, see Compatibility for changing the instance type.
2. [Windows instances] If you configured your Windows instance to use static IP addressing and you change from an instance type that doesn't support enhanced networking to an instance type that does support enhanced networking, you might get a warning about a potential IP address conflict when you reconfigure static IP addressing. To prevent this, enable DHCP on the network interface for your instance before you change the instance type. From your instance, open the Network and Sharing Center, open Internet Protocol Version 4 (TCP/ IPv4) Properties for the network interface, and choose Obtain an IP address automatically.
Change the instance type and reconfigure static IP addressing on the network interface.
3. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
4. In the navigation pane, choose Instances.
5. Select the instance and choose Instance state, Stop instance. When prompted for confirmation, choose Stop. It can take a few minutes for the instance to stop.
6. With the instance still selected, choose Actions, Instance settings, Change instance type. This option is grayed out if the instance state is not stopped.
7. On the Change instance type page, do the following: a.
For Instance type, select the instance type that you want.
If the instance type is not in the list, then it's not compatible with the configuration of your instance. Instead, use the following instructions: Migrate to a new instance type by launching a new EC2 instance. b.
(Optional) If the instance type that you selected supports EBS optimization, select EBS-optimized to enable EBS optimization, or deselect EBS-optimized to disable EBS optimization.

If the instance type that you selected is EBS optimized by default, EBS-optimized is selected and you can't deselect it. c.
(Optional) Configure vCPU options on the new instance type.
When you change the instance type of an existing instance, Amazon EC2 applies the CPU option settings from the existing instance to the new instance, if possible. If the new instance type doesn't support those settings, the CPU options are reset to None. This option uses the default number of vCPUs for the new instance type.
If the instance type that you selected supports vCPU configuration, select Specify CPU options in the Advanced details panel to configure vCPUs for your new instance type. d.
Choose Change to accept the new settings.
8. To start the instance, select the instance and choose Instance state, Start instance. It can take a few minutes for the instance to enter the running state. If your instance won't start, see Troubleshoot changing the instance type.
9. [Windows instances] If your instance runs Windows Server 2016 or Windows Server 2019 with EC2Launch v1, connect to your Windows instance and run the following EC2Launch PowerShell script to configure the instance after the instance type is changed.
Important The administrator password will reset when you enable the initialize instance EC2 Launch script. You can modify the configuration file to disable the administrator password reset by specifying it in the settings for the initialization tasks. For steps on how to disable password reset, see Configure initialization tasks (EC2Launch) or Change settings (EC2Launch v2).
PS C:\> C:\ProgramData\Amazon\EC2-Windows\Launch\Scripts\InitializeInstance.ps1 - Schedule
### Migrate to a new instance type by launching a new EC2 instance You can change the instance type of an EC2 instance only if it is an EBS-backed instance with a configuration that is compatible with the new instance type that you want. Otherwise, if the

configuration or your instance is not compatible with the new instance type, or it is an instance store-based instance, you must launch a replacement instance that is compatible with the instance type that you want. For more information about how compatibility is determined, see Compatibility for changing the instance type.
Overview of the migration process
- Back up the data on the original instance.
- Launch a new instance with a configuration that is compatible with the new instance type that you want, attaching any EBS volumes that were attached to your original instance.
- Install your application on your new instance.
- Restore any data.
- If the original instance has an Elastic IP address, you must associate it with your new instance to ensure that your users can continue to use your application without interruption.
To migrate an instance to a new instance
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. Back up any data that you still need as follows:
- Connect to your instance and copy the data on your instance store volumes to persistent storage.
- Create snapshots of your EBS volumes so that you can create new volumes with the same data, or detach the volumes from the original instance so that you can attach them to the new instance.
3. In the navigation pane, choose Instances.
4. Choose Launch instances. When you configure the instance, do the following: a.
Select an AMI that supports the instance type that you want. For example, you must select an AMI that supports the processor type of the new instance type. Also, current generation instance types require an HVM AMI. b.
Select the new instance type that you want. If the instance type that you want isn't available, then it's not compatible with the configuration of the AMI that you selected. c.
If you want to allow the same traffic to reach the new instance, select the same VPC and security group that are used with the original instance.

d.
When you're done configuring your new instance, complete the steps to select a key pair and launch your instance. It can take a few minutes for the instance to enter the running state.
5. If you backed up data to an EBS snapshot, create a volume from the snapshot and then attach the volume to the new instance.
To move an EBS volume from the original instance to the new instance, detach the volume from the original instance and then attach the volume to the new instance.
6. Install your application and any required software on the new instance.
7. Restore any data that you backed up from the instance store volumes of the original instance.
8. If the original instance has an Elastic IP address, assign it to the new instance as follows: a.
In the navigation pane, choose Elastic IPs. b.
Select the Elastic IP address that is associated with the original instance and choose Actions, Disassociate Elastic IP address. When prompted for confirmation, choose Disassociate. c.
With the Elastic IP address still selected, choose Actions, Associate Elastic IP address. d.
For Resource type, choose Instance. e.
For Instance, choose the new instance. f.
(Optional) For Private IP address, specify a private IP address with which to associate the Elastic IP address. g.
Choose Associate.
9. (Optional) You can terminate the original instance if it's no longer needed. Select the instance, verify that you are about to terminate the original instance and not the new instance (for example, check the name or launch time), and then choose Instance state, Terminate instance.
### Troubleshoot changing the instance type Use the following information to help diagnose and fix issues that you might encounter when changing the instance type.

#### Instance won't start after changing instance type Possible cause: Requirements for new instance type not met If your instance won't boot, it is possible that one of the requirements for the new instance type was not met. For more information, see Why is my Linux instance not booting after I changed its type?
Possible cause: AMI does not support instance type If you use the EC2 console to change the instance type, only the instance types that are supported by the selected AMI are available. However, if you use the AWS CLI to launch an instance, you can specify an incompatible AMI and instance type. If the AMI and instance type are incompatible, the instance can't start. For more information, see Compatibility for changing the instance type.
Possible cause: Instance is in cluster placement group If your instance is in a cluster placement group and, after changing the instance type, the instance fails to start, try the following:
1. Stop all the instances in the cluster placement group.
2. Change the instance type of the affected instance.
3. Start all the instances in the cluster placement group.
#### Application or website not reachable from the internet after changing instance type Possible cause: Public IPv4 address is released When you change the instance type, you must first stop the instance. When you stop an instance, we release the public IPv4 address and give your instance a new public IPv4 address.
To retain the public IPv4 address between instance stops and starts, we recommend that you use an Elastic IP address, at no extra cost provided your instance is running. For more information, see Elastic IP addresses.
## Burstable performance instances Many general purpose workloads are on average not busy, and do not require a high level of sustained CPU performance. The following graph illustrates the CPU utilization for many common workloads that customers run in the AWS Cloud today.

These low-to-moderate CPU utilization workloads lead to wastage of CPU cycles and, as a result, you pay for more than you use. To overcome this, you can leverage the low-cost burstable general purpose instances, which are the T instances.
The T instance family provides a baseline CPU performance with the ability to burst above the baseline at any time for as long as required. The baseline CPU is defined to meet the needs of the majority of general purpose workloads, including large-scale micro-services, web servers, small and medium databases, data logging, code repositories, virtual desktops, development and test environments, and business-critical applications. The T instances offer a balance of compute, memory, and network resources, and provide you with the most cost-effective way to run a broad spectrum of general purpose applications that have a low-to-moderate CPU usage. They can save you up to 15% in costs when compared to M instances, and can lead to even more cost savings with smaller, more economical instance sizes, offering as low as 2 vCPUs and 0.5 GiB of memory.
The smaller T instance sizes, such as nano, micro, small, and medium, are well suited for workloads that need a small amount of memory and do not expect high CPU usage.

Note This topic describes burstable CPU. For information about burstable network performance, see Amazon EC2 instance network bandwidth.
### EC2 burstable instance types The EC2 burstable instances consist of T4g, T3a, and T3 instance types, and the previous generation T2 instance types.
The T4g instance types are the latest generation of burstable instances. They provide the best price for performance, and provide you with the lowest cost of all the EC2 instance types. The T4g instance types are powered by Arm-based AWS Graviton2 processors with extensive ecosystem support from operating systems vendors, independent software vendors, and popular AWS services and applications.
The following table summarizes the key differences between the burstable instance types.
Type Description Processor family Latest generation T4g Lowest cost EC2 instance type with up to 40% higher price/ performance and 20% lower costs vs T3 AWS Graviton2 processors with Arm Neoverse N1 cores T3a Lowest cost x86-based instances with 10% lower costs vs T3 instances AMD 1st gen EPYC processors T3 Best peak price/performance for x86 workloads with up to 30% lower price/performance vs previous generation T2 instances Intel Xeon Scalable (Skylake, Cascade Lake processors)
Previous generation

Type Description Processor family T2 Previous generation burstable instances Intel Xeon processors For information about instance pricing and additional specifications, see Amazon EC2 Pricing and Amazon EC2 Instance Types. For information about burstable network performance, see Amazon EC2 instance network bandwidth.
If your created your AWS account before July 15, 2025 and it's less than 12 months old, you can use a t2.micro instance for free (or a t3.micro instance in Regions where t2.micro is unavailable) within certain usage limits. If you created your AWS account on or after July 15, 2025, you can use t3.micro, t3.small, t4g.micro, t4g.small instance types for 6 months or until your credits are used up. For more information, see AWS Free Tier.
Supported purchasing options for T instances
- On-Demand Instances
- Reserved Instances
- Dedicated Instances (T3 only)
- Dedicated Hosts (T3 only, in standard mode only)
- Spot Instances For more information, see Amazon EC2 billing and purchasing options.
Contents
- Best practices
- Key concepts for burstable performance instances
- Unlimited mode for burstable performance instances
- Standard mode for burstable performance instances
- Configure burstable performance instances
- Monitor CPU credits for burstable instances

### Best practices Follow these best practices to get the maximum benefit from burstable performance instances.
- Ensure that the instance size you choose passes the minimum memory requirements of your operating system and applications. Operating systems with graphical user interfaces that consume significant memory and CPU resources (for example, Windows) might require a t3.micro or larger instance size for many use cases. As the memory and CPU requirements of your workload grow over time, you have the flexibility with the T instances to scale to larger instance sizes of the same instance type, or to select another instance type.
- Enable AWS Compute Optimizer for your account and review the Compute Optimizer recommendations for your workload. Compute Optimizer can help assess whether instances should be upsized to improve performance or downsized for cost savings. Compute Optimizer may also recommend a different instance type based on your scenario. For more information, see Viewing EC2 instance recommendations in the AWS Compute Optimizer User Guide.
### Key concepts for burstable performance instances Traditional Amazon EC2 instance types provide fixed CPU resources, while burstable performance instances provide a baseline level of CPU utilization with the ability to burst CPU utilization above the baseline level. This ensures that you pay only for baseline CPU plus any additional burst CPU usage resulting in lower compute costs. The baseline utilization and ability to burst are governed by CPU credits. Burstable performance instances are the only instance types that use credits for CPU usage.
Each burstable performance instance continuously earns credits when it stays below the CPU baseline, and continuously spends credits when it bursts above the baseline. The amount of credits earned or spent depends on the CPU utilization of the instance:
- If the CPU utilization is below baseline, then credits earned are greater than credits spent.
- If the CPU utilization is equal to baseline, then credits earned are equal to credits spent.
- If the CPU utilization is higher than baseline, then credits spent are higher than credits earned.
When the credits earned are greater than credits spent, then the difference is called accrued credits, which can be used later to burst above baseline CPU utilization. Similarly, when the credits spent are more than credits earned, then the instance behavior depends on the credit configuration mode—Standard mode or Unlimited mode.

In Standard mode, when credits spent are more than credits earned, the instance uses the accrued credits to burst above baseline CPU utilization. If there are no accrued credits remaining, then the instance gradually comes down to baseline CPU utilization and cannot burst above baseline until it accrues more credits.
In Unlimited mode, if the instance bursts above baseline CPU utilization, then the instance first uses the accrued credits to burst. If there are no accrued credits remaining, then the instance spends surplus credits to burst. When its CPU utilization falls below the baseline, it uses the CPU credits that it earns to pay down the surplus credits that it spent earlier. The ability to earn CPU credits to pay down surplus credits enables Amazon EC2 to average the CPU utilization of an instance over a 24-hour period. If the average CPU usage over a 24-hour period exceeds the baseline, the instance is billed for the additional usage at a flat additional rate per vCPU-hour.
Contents
- Key concepts and definitions
- Earn CPU credits
- CPU credit earn rate
- CPU credit accrual limit
- Accrued CPU credits life span
- Baseline utilization
#### Key concepts and definitions The following key concepts and definitions are applicable to burstable performance instances.
CPU utilization CPU utilization is the percentage of allocated EC2 compute units that are currently in use on the instance. This metric measures the percentage of allocated CPU cycles that are being utilized on an instance. The CPU Utilization CloudWatch metric shows CPU usage per instance and not CPU usage per core. The baseline CPU specification of an instance is also based on the CPU usage per instance. To measure CPU utilization using the AWS Management Console or the AWS CLI, see Get statistics for a specific instance.
CPU credit A unit of vCPU-time.

Examples:
1 CPU credit = 1 vCPU * 100% utilization * 1 minute.
1 CPU credit = 1 vCPU * 50% utilization * 2 minutes 1 CPU credit = 2 vCPU * 25% utilization * 2 minutes
#### Baseline utilization The baseline utilization is the level at which the CPU can be utilized for a net credit balance of zero, when the number of CPU credits being earned matches the number of CPU credits being used. Baseline utilization is also known as the baseline. Baseline utilization is expressed as a percentage of vCPU utilization, which is calculated as follows: Baseline utilization % = (number of credits earned/number of vCPUs)/60 minutes.
For the baseline utilization of each burstable performance instance type, see the credit table.
Earned credits Credits earned continuously by an instance when it is running.
Number of credits earned per hour = % baseline utilization * number of vCPUs * 60 minutes Example:
A t3.nano with 2 vCPUs and a baseline utilization of 5% earns 6 credits per hour, calculated as follows:
2 vCPUs * 5% baseline * 60 minutes = 6 credits per hour Spent or used credits Credits used continuously by an instance when it is running.
CPU credits spent per minute = Number of vCPUs * CPU utilization * 1 minute Accrued credits Unspent CPU credits when an instance uses fewer credits than is required for baseline utilization. In other words, accrued credits = (Earned credits – Used credits) below baseline.
Example:

If a t3.nano is running at 2% CPU utilization, which is below its baseline of 5% for an hour, the accrued credits is calculated as follows:
Accrued CPU credits = (Earned credits per hour – Used credits per hour) = 6 – 2 vCPUs * 2% CPU utilization * 60 minutes = 6 – 2.4 = 3.6 accrued credits per hour Credit accrual limit Depends on the instance size but in general is equal to the number of maximum credits earned in 24 hours.
Example:
For t3.nano, the credit accrual limit = 24 * 6 = 144 credits
##### Launch credits Only applicable for T2 instances configured for Standard mode. Launch credits are a limited number of CPU credits that are allocated to a new T2 instance so that, when launched in Standard mode, it can burst above the baseline.
Surplus credits Credits that are spent by an instance after it depletes its accrued credit balance. The surplus credits are designed for burstable instances to sustain high performance for an extended period of time, and are only used in Unlimited mode. The surplus credits balance is used to determine how many credits were used by the instance for bursting in Unlimited mode.
Standard mode Credit configuration mode, which allows an instance to burst above the baseline by spending credits it has accrued in its credit balance.
Unlimited mode Credit configuration mode, which allows an instance to burst above the baseline by sustaining high CPU utilization for any period of time whenever required. The hourly instance price automatically covers all CPU usage spikes if the average CPU utilization of the instance is at or below the baseline over a rolling 24-hour period or the instance lifetime, whichever is shorter.
If the instance runs at higher CPU utilization for a prolonged period, it can do so for a flat additional rate per vCPU-hour.
The following table summarizes the key credit differences between the burstable instance types.

Type Type of CPU credits supported Credit configuration modes Accrued CPU credits lifespan between instance starts and stops Latest generation T4g Earned credits, Accrued credits, Spent credits, Surplus credits (Unlimited mode only)
Standard, Unlimited (default)
7 days (credits persist for 7 days after an instance stops)
T3a Earned credits, Accrued credits, Spent credits, Surplus credits (Unlimited mode only)
Standard, Unlimited (default)
7 days (credits persist for 7 days after an instance stops)
T3 Earned credits, Accrued credits, Spent credits, Surplus credits (Unlimited mode only)
Standard, Unlimited (default)
7 days (credits persist for 7 days after an instance stops)
Previous generation T2 Earned credits, Accrued credits, Spent credits, Launch credits (Standard mode only), Surplus credits (Unlimited mode only)
Standard (default), Unlimited 0 days (credits are lost when an instance stops)

Note Unlimited mode is not supported for T3 instances that are launched on a Dedicated Host.
#### Earn CPU credits Each burstable performance instance continuously earns (at a millisecond-level resolution) a set rate of CPU credits per hour, depending on the instance size. The accounting process for whether credits are accrued or spent also happens at a millisecond-level resolution, so you don't have to worry about overspending CPU credits; a short burst of CPU uses a small fraction of a CPU credit.
If a burstable performance instance uses fewer CPU resources than is required for baseline utilization (such as when it is idle), the unspent CPU credits are accrued in the CPU credit balance. If a burstable performance instance needs to burst above the baseline utilization level, it spends the accrued credits. The more credits that a burstable performance instance has accrued, the more time it can burst beyond its baseline when more CPU utilization is needed.
The following table lists the burstable performance instance types, the rate at which CPU credits are earned per hour, the maximum number of earned CPU credits that an instance can accrue, the number of vCPUs per instance, and the baseline utilization as a percentage of a full core (using a single vCPU).
Instance type CPU credits earned per hour Maximum earned credits that can be accrued* vCPUs*** Baseline utilizati on per vCPU T2 t2.nano 3 72 1 5% t2.micro 6 144 1 10% t2.small 12 288 1 20% t2.medium 24 576 2 20%** t2.large 36 864 2 30%** t2.xlarge 54 1296 4 22.5%**

Instance type CPU credits earned per hour Maximum earned credits that can be accrued* vCPUs*** Baseline utilizati on per vCPU t2.2xlarge 81.6 1958.4 8 17%** T3 t3.nano 6 144 2 5%** t3.micro 12 288 2 10%** t3.small 24 576 2 20%** t3.medium 24 576 2 20%** t3.large 36 864 2 30%** t3.xlarge 96 2304 4 40%** t3.2xlarge 192 4608 8 40%** T3a t3a.nano 6 144 2 5%** t3a.micro 12 288 2 10%** t3a.small 24 576 2 20%** t3a.medium 24 576 2 20%** t3a.large 36 864 2 30%** t3a.xlarge 96 2304 4 40%** t3a.2xlar ge 192 4608 8 40%** T4g


Instance type CPU credits earned per hour Maximum earned credits that can be accrued* vCPUs*** Baseline utilizati on per vCPU t4g.nano 6 144 2 5%** t4g.micro 12 288 2 10%** t4g.small 24 576 2 20%** t4g.medium 24 576 2 20%** t4g.large 36 864 2 30%** t4g.xlarge 96 2304 4 40%** t4g.2xlar ge 192 4608 8 40%**
* The number of credits that can be accrued is equivalent to the number of credits that can be earned in a 24-hour period.
** The percentage baseline utilization in the table is per vCPU. In CloudWatch, CPU utilizati on is shown per vCPU. For example, the CPU utilization for a t3.large instance operating at the baseline level is shown as 30% in CloudWatch CPU metrics. For information about how to calculate the baseline utilization, see Baseline utilization.
*** Each vCPU is a thread of either an Intel Xeon core or an AMD EPYC core, except for T2 and T4g instances.
#### CPU credit earn rate The number of CPU credits earned per hour is determined by the instance size. For example, a t3.nano earns six credits per hour, while a t3.small earns 24 credits per hour. The preceding table lists the credit earn rate for all instances.

#### CPU credit accrual limit While earned credits never expire on a running instance, there is a limit to the number of earned credits that an instance can accrue. The limit is determined by the CPU credit balance limit. After the limit is reached, any new credits that are earned are discarded, as indicated by the following image. The full bucket indicates the CPU credit balance limit, and the spillover indicates the newly earned credits that exceed the limit.
The CPU credit balance limit differs for each instance size. For example, a t3.micro instance can accrue a maximum of 288 earned CPU credits in the CPU credit balance. The preceding table lists the maximum number of earned credits that each instance can accrue.
T2 Standard instances also earn launch credits. Launch credits do not count towards the CPU credit balance limit. If a T2 instance has not spent its launch credits, and remains idle over a 24-hour period while accruing earned credits, its CPU credit balance appears as over the limit. For more information, see Launch credits.
T4g, T3a, and T3 instances do not earn launch credits. These instances launch as unlimited by default, and therefore can burst immediately upon start without any launch credits. T3 instances launched on a Dedicated Host launch as standard by default; unlimited mode is not supported for T3 instances on a Dedicated Host.

#### Accrued CPU credits life span CPU credits on a running instance do not expire.
For T2, the CPU credit balance does not persist between instance stops and starts. If you stop a T2 instance, the instance loses all its accrued credits.
For T4g, T3a, and T3, the CPU credit balance persists for seven days after an instance stops and the credits are lost thereafter. If you start the instance within seven days, no credits are lost.
For more information, see CPUCreditBalance in the CloudWatch metrics table.
Baseline utilization The baseline utilization is the level at which the CPU can be utilized for a net credit balance of zero, when the number of CPU credits being earned matches the number of CPU credits being used.
Baseline utilization is also known as the baseline.
Baseline utilization is expressed as a percentage of vCPU utilization, which is calculated as follows:
(number of credits earned/number of vCPUs)/60 minutes = % baseline utilization For example, a t3.nano instance, with 2 vCPUs, earns 6 credits per hour, resulting in a baseline utilization of 5% , which is calculated as follows:
(6 credits earned/2 vCPUs)/60 minutes = 5% baseline utilization A t3.large instance, with 2 vCPUs, earns 36 credits per hour, resulting in a baseline utilization of 30% ((36/2)/60).
The following graph provides an example of a t3.large with an average CPU utilization below the baseline.

### Unlimited mode for burstable performance instances A burstable performance instance configured as unlimited can sustain high CPU utilization for any period of time whenever required. The hourly instance price automatically covers all CPU usage spikes if the average CPU utilization of the instance is at or below the baseline over a rolling 24- hour period or the instance lifetime, whichever is shorter.
For the vast majority of general-purpose workloads, instances configured as unlimited provide ample performance without any additional charges. If the instance runs at higher CPU utilization for a prolonged period, it can do so for a flat additional rate per vCPU-hour. For information about pricing, see Amazon EC2 pricing and T2/T3/T4 Unlimited Mode Pricing.
If your created your AWS account before July 15, 2025 and you use a t2.micro or t3.micro instance under the AWS Free Tier offer and use it in unlimited mode, charges might apply if your average utilization over a rolling 24-hour period exceeds the baseline utilization of the instance.
T4g, T3a, and T3 instances launch as unlimited by default (unless you change the default). If the average CPU usage over a 24-hour period exceeds the baseline, you incur charges for surplus credits. If you launch Spot Instances as unlimited and plan to use them immediately and for a short duration, with no idle time for accruing CPU credits, you incur charges for surplus credits. We recommend that you launch your Spot Instances in standard mode to avoid paying higher costs.

For more information, see Surplus credits can incur charges and Launch burstable performance instances.
Note T3 instances launched on a Dedicated Host launch as standard by default; unlimited mode is not supported for T3 instances on a Dedicated Host.
Contents
- Unlimited mode concepts for burstable instances
- How Unlimited burstable performance instances work
- When to use unlimited mode versus fixed CPU
- Surplus credits can incur charges
- How much does unlimited burstable performance cost?
- No launch credits for T2 Unlimited instances
- Enable unlimited mode
- What happens to credits when switching between Unlimited and Standard
- Monitor credit usage
- Unlimited mode examples for burstable instances
- Example 1: Explain credit use with T3 Unlimited
- Example 2: Explain credit use with T2 Unlimited
#### Unlimited mode concepts for burstable instances The unlimited mode is a credit configuration option for burstable performance instances. It can be enabled or disabled at any time for a running or stopped instance. You can set unlimited as the default credit option at the account level per AWS Region, per burstable performance instance family, so that all new burstable performance instances in the account launch using the default credit option.
##### How Unlimited burstable performance instances work If a burstable performance instance configured as unlimited depletes its CPU credit balance, it can spend surplus credits to burst beyond the baseline. When its CPU utilization falls below the

baseline, it uses the CPU credits that it earns to pay down the surplus credits that it spent earlier.
The ability to earn CPU credits to pay down surplus credits enables Amazon EC2 to average the CPU utilization of an instance over a 24-hour period. If the average CPU usage over a 24-hour period exceeds the baseline, the instance is billed for the additional usage at a flat additional rate per vCPU-hour.
The following graph shows the CPU usage of a t3.large. The baseline CPU utilization for a t3.large is 30%. If the instance runs at 30% CPU utilization or less on average over a 24-hour period, there is no additional charge because the cost is already covered by the instance hourly price. However, if the instance runs at 40% CPU utilization on average over a 24-hour period, as shown in the graph, the instance is billed for the additional 10% CPU usage at a flat additional rate per vCPU-hour.
For more information about the baseline utilization per vCPU for each instance type and how many credits each instance type earns, see the credit table.
##### When to use unlimited mode versus fixed CPU When determining whether you should use a burstable performance instance in unlimited mode, such as T3, or a fixed performance instance, such as M5, you need to determine the breakeven CPU usage. The breakeven CPU usage for a burstable performance instance is the point at which a burstable performance instance costs the same as a fixed performance instance. The breakeven CPU usage helps you determine the following:
- If the average CPU usage over a 24-hour period is at or below the breakeven CPU usage, use a burstable performance instance in unlimited mode so that you can benefit from the lower

price of a burstable performance instance while getting the same performance as a fixed performance instance.
- If the average CPU usage over a 24-hour period is above the breakeven CPU usage, the burstable performance instance will cost more than the equivalently-sized fixed performance instance. If a T3 instance continuously bursts at 100% CPU, you end up paying approximately 1.5 times the price of an equivalently-sized M5 instance.
The following graph shows the breakeven CPU usage point where a t3.large costs the same as an m5.large. The breakeven CPU usage point for a t3.large is 42.5%. If the average CPU usage is at 42.5%, the cost of running the t3.large is the same as an m5.large, and is more expensive if the average CPU usage is above 42.5%. If the workload needs less than 42.5% average CPU usage, you can benefit from the lower price of the t3.large while getting the same performance as an m5.large.
The following table shows how to calculate the breakeven CPU usage threshold so that you can determine when it's less expensive to use a burstable performance instance in unlimited mode or a fixed performance instance. The columns in the table are labeled A through K.

Instance type vCPUs T3 price*/ hour M5 price*/ hour Price differenc e T3 baseline utilizati on per vCPU (%)
Charge per vCPU hour for surplus credits Charge per vCPU minute Additiona l burst minutes available per vCPU Additiona l CPU % available Breakeven CPU % A B C D E = D - C F G H = G / 60 I = E / H J = (I /
60) / B K = F + J t3.large 2 $0.0835 $0.096 $0.0125 30% $0.05 $0.000833 15 12.5% 42.5%
* Price is based on us-east-1 and Linux OS.
The table provides the following information:
- Column A shows the instance type, t3.large.
- Column B shows the number of vCPUs for the t3.large.
- Column C shows the price of a t3.large per hour.
- Column D shows the price of an m5.large per hour.
- Column E shows the price difference between the t3.large and the m5.large.
- Column F shows the baseline utilization per vCPU of the t3.large, which is 30%. At the baseline, the hourly cost of the instance covers the cost of the CPU usage.
- Column G shows the flat additional rate per vCPU-hour that an instance is charged if it bursts at 100% CPU after it has depleted its earned credits.
- Column H shows the flat additional rate per vCPU-minute that an instance is charged if it bursts at 100% CPU after it has depleted its earned credits.
- Column I shows the number of additional minutes that the t3.large can burst per hour at 100% CPU while paying the same price per hour as an m5.large.

- Column J shows the additional CPU usage (in %) over baseline that the instance can burst while paying the same price per hour as an m5.large.
- Column K shows the breakeven CPU usage (in %) that the t3.large can burst without paying more than the m5.large. Anything above this, and the t3.large costs more than the m5.large.
The following table shows the breakeven CPU usage (in %) for T3 instance types compared to the similarly-sized M5 instance types.
T3 instance type Breakeven CPU usage (in %) for T3 compared to M5 t3.large 42.5% t3.xlarge 52.5% t3.2xlarge 52.5%
##### Surplus credits can incur charges If the average CPU utilization of an instance is at or below the baseline, the instance incurs no additional charges. Because an instance earns a maximum number of credits in a 24-hour period (for example, a t3.micro instance can earn a maximum of 288 credits in a 24-hour period), it can spend surplus credits up to that maximum without being charged.
However, if CPU utilization stays above the baseline, the instance cannot earn enough credits to pay down the surplus credits that it has spent. The surplus credits that are not paid down are charged at a flat additional rate per vCPU-hour. For information about the rate, see  T2/T3/T4g Unlimited Mode Pricing.
Surplus credits that were spent earlier are charged when any of the following occurs:
- The spent surplus credits exceed the maximum number of credits the instance can earn in a 24- hour period. Spent surplus credits above the maximum are charged at the end of the hour.
- The instance is stopped or terminated.
- The instance is switched from unlimited to standard.

Spent surplus credits are tracked by the CloudWatch metric CPUSurplusCreditBalance. Surplus credits that are charged are tracked by the CloudWatch metric CPUSurplusCreditsCharged. For more information, see Additional CloudWatch metrics for burstable performance instances.
##### How much does unlimited burstable performance cost?
If you use surplus credits and they're not paid down by earned credits (see Surplus credits can incur charges), you pay a flat additional rate per vCPU-hour for the surplus credits. The rate is listed in the T2/T3/T4g Unlimited Mode Pricing section on the Amazon EC2 On-Demand Pricing page.
##### No launch credits for T2 Unlimited instances T2 Standard instances receive launch credits, but T2 Unlimited instances do not. A T2 Unlimited instance can burst beyond the baseline at any time with no additional charge, as long as its average CPU utilization is at or below the baseline over a rolling 24-hour window or its lifetime, whichever is shorter. As such, T2 Unlimited instances do not require launch credits to achieve high performance immediately after launch.
If a T2 instance is switched from standard to unlimited, any accrued launch credits are removed from the CPUCreditBalance before the remaining CPUCreditBalance is carried over.
T4g, T3a, and T3 instances never receive launch credits because they launch in Unlimited mode by default, and therefore can burst immediately upon start. The Unlimited mode credit configuration enables T4g, T3a, and T3 instances to use as much CPU as needed to burst beyond the baseline and for as long as needed.
##### Enable unlimited mode You can switch from unlimited to standard, and from standard to unlimited, at any time on a running or stopped instance. For more information, see Configure the credit specification at launch and Manage the credit specification of a burstable performance instance.
You can set unlimited as the default credit option at the account level per AWS Region, per burstable performance instance family, so that all new burstable performance instances in the account launch using the default credit option. For more information, see Manage the default credit specification for an account.
You can check whether your burstable performance instance is configured as unlimited or standard using the Amazon EC2 console or the AWS CLI. For more information, see Configure burstable performance instances.

##### What happens to credits when switching between Unlimited and Standard CPUCreditBalance is a CloudWatch metric that tracks the number of credits accrued by an instance. CPUSurplusCreditBalance is a CloudWatch metric that tracks the number of surplus credits spent by an instance.
When you change an instance configured as unlimited to standard, the following occurs:
- The CPUCreditBalance value remains unchanged and is carried over.
- The CPUSurplusCreditBalance value is immediately charged.
When a standard instance is switched to unlimited, the following occurs:
- The CPUCreditBalance value containing accrued earned credits is carried over.
- For T2 Standard instances, any launch credits are removed from the CPUCreditBalance value, and the remaining CPUCreditBalance value containing accrued earned credits is carried over.
##### Monitor credit usage To see if your instance is spending more credits than the baseline provides, you can use CloudWatch metrics to track usage, and you can set up hourly alarms to be notified of credit usage.
For more information, see Monitor CPU credits for burstable instances.
#### Unlimited mode examples for burstable instances The following examples explain credit use for instances that are configured as unlimited.
Examples
- Example 1: Explain credit use with T3 Unlimited
- Example 2: Explain credit use with T2 Unlimited
##### Example 1: Explain credit use with T3 Unlimited In this example, you see the CPU utilization of a t3.nano instance launched as unlimited, and how it spends earned and surplus credits to sustain CPU utilization.
A t3.nano instance earns 144 CPU credits over a rolling 24-hour period, which it can redeem for 144 minutes of vCPU use. When it depletes its CPU credit balance (represented by the CloudWatch metric CPUCreditBalance), it can spend surplus CPU credits—that it has not yet earned—to burst

for as long as it needs. Because a t3.nano instance earns a maximum of 144 credits in a 24-hour period, it can spend surplus credits up to that maximum without being charged immediately. If it spends more than 144 CPU credits, it is charged for the difference at the end of the hour.
The intent of the example, illustrated by the following graph, is to show how an instance can burst using surplus credits even after it depletes its CPUCreditBalance. The following workflow references the numbered points on the graph:
P1 – At 0 hours on the graph, the instance is launched as unlimited and immediately begins to earn credits. The instance remains idle from the time it is launched—CPU utilization is 0%—and no credits are spent. All unspent credits are accrued in the credit balance. For the first 24 hours, CPUCreditUsage is at 0, and the CPUCreditBalance value reaches its maximum of 144.
P2 – For the next 12 hours, CPU utilization is at 2.5%, which is below the 5% baseline. The instance earns more credits than it spends, but the CPUCreditBalance value cannot exceed its maximum of 144 credits.
P3 – For the next 24 hours, CPU utilization is at 7% (above the baseline), which requires a spend of 57.6 credits. The instance spends more credits than it earns, and the CPUCreditBalance value reduces to 86.4 credits.
P4 – For the next 12 hours, CPU utilization decreases to 2.5% (below the baseline), which requires a spend of 36 credits. In the same time, the instance earns 72 credits. The instance earns more credits than it spends, and the CPUCreditBalance value increases to 122 credits.
P5 – For the next 5 hours, the instance bursts at 100% CPU utilization, and spends a total of 570 credits to sustain the burst. About an hour into this period, the instance depletes its entire CPUCreditBalance of 122 credits, and starts to spend surplus credits to sustain the high CPU utilization, totaling 448 surplus credits in this period (570-122=448). When the CPUSurplusCreditBalance value reaches 144 CPU credits (the maximum a t3.nano instance can earn in a 24-hour period), any surplus credits spent thereafter cannot be offset by earned credits. The surplus credits spent thereafter amounts to 304 credits (448-144=304), which results in a small additional charge at the end of the hour for 304 credits.
P6 – For the next 13 hours, CPU utilization is at 5% (the baseline). The instance earns as many credits as it spends, with no excess to pay down the CPUSurplusCreditBalance. The CPUSurplusCreditBalance value remains at 144 credits.
P7 – For the last 24 hours in this example, the instance is idle and CPU utilization is 0%. During this time, the instance earns 144 credits, which it uses to pay down the CPUSurplusCreditBalance.

##### Example 2: Explain credit use with T2 Unlimited In this example, you see the CPU utilization of a t2.nano instance launched as unlimited, and how it spends earned and surplus credits to sustain CPU utilization.
A t2.nano instance earns 72 CPU credits over a rolling 24-hour period, which it can redeem for 72 minutes of vCPU use. When it depletes its CPU credit balance (represented by the CloudWatch metric CPUCreditBalance), it can spend surplus CPU credits—that it has not yet earned—to burst for as long as it needs. Because a t2.nano instance earns a maximum of 72 credits in a 24-hour period, it can spend surplus credits up to that maximum without being charged immediately. If it spends more than 72 CPU credits, it is charged for the difference at the end of the hour.
The intent of the example, illustrated by the following graph, is to show how an instance can burst using surplus credits even after it depletes its CPUCreditBalance. You can assume that, at the start of the time line in the graph, the instance has an accrued credit balance equal to the maximum number of credits it can earn in 24 hours. The following workflow references the numbered points on the graph:
1 – In the first 10 minutes, CPUCreditUsage is at 0, and the CPUCreditBalance value remains at its maximum of 72.
2 – At 23:40, as CPU utilization increases, the instance spends CPU credits and the CPUCreditBalance value decreases.

3 – At around 00:47, the instance depletes its entire CPUCreditBalance, and starts to spend surplus credits to sustain high CPU utilization.
4 – Surplus credits are spent until 01:55, when the CPUSurplusCreditBalance value reaches 72 CPU credits. This is equal to the maximum a t2.nano instance can earn in a 24-hour period.
Any surplus credits spent thereafter cannot be offset by earned credits within the 24-hour period, which results in a small additional charge at the end of the hour.
5 – The instance continues to spend surplus credits until around 02:20. At this time, CPU utilization falls below the baseline, and the instance starts to earn credits at 3 credits per hour (or 0.25 credits every 5 minutes), which it uses to pay down the CPUSurplusCreditBalance. After the CPUSurplusCreditBalance value reduces to 0, the instance starts to accrue earned credits in its CPUCreditBalance at 0.25 credits every 5 minutes.
Calculating the bill (Linux instance)
Surplus credits cost $0.05 per vCPU-hour. The instance spent approximately 25 surplus credits between 01:55 and 02:20, which is equivalent to 0.42 vCPU-hours. Additional charges for this instance are 0.42 vCPU-hours x $0.05/vCPU-hour = $0.021, rounded to $0.02. Here is the month- end bill for this T2 Unlimited instance:

Calculating the bill (Windows instance)
Surplus credits cost $0.096 per vCPU-hour. The instance spent approximately 25 surplus credits between 01:55 and 02:20, which is equivalent to 0.42 vCPU-hours. Additional charges for this instance are 0.42 vCPU-hours x $0.096/vCPU-hour = $0.04032, rounded to $0.04. Here is the month-end bill for this T2 Unlimited instance:
You can set billing alerts to be notified every hour of any accruing charges, and take action if required.
### Standard mode for burstable performance instances A burstable performance instance configured as standard is suited to workloads with an average CPU utilization that is consistently below the baseline CPU utilization of the instance. To burst above the baseline, the instance spends credits that it has accrued in its CPU credit balance. If the instance is running low on accrued credits, CPU utilization is gradually lowered to the baseline level, so that the instance does not experience a sharp performance drop-off when its accrued CPU credit balance is depleted. For more information, see Key concepts for burstable performance instances.
Contents
- Standard mode concepts for burstable instances
- How standard burstable performance instances work
- Launch credits

- Launch credit limits
- Differences between launch credits and earned credits
- Standard mode examples for burstable instances
- Example 1: Explain credit use with T3 Standard
- Example 2: Explain credit use with T2 Standard
- Period 1: 1 – 24 hours
- Period 2: 25 – 36 hours
- Period 3: 37 – 61 hours
- Period 4: 62 – 72 hours
- Period 5: 73 – 75 hours
- Period 6: 76 – 90 hours
- Period 7: 91 – 96 hours
#### Standard mode concepts for burstable instances The standard mode is a configuration option for burstable performance instances. It can be enabled or disabled at any time for a running or stopped instance. You can set standard as the default credit option at the account level per AWS Region, per burstable performance instance family, so that all new burstable performance instances in the account launch using the default credit option.
##### How standard burstable performance instances work When a burstable performance instance configured as standard is in a running state, it continuously earns (at a millisecond-level resolution) a set rate of earned credits per hour. For T2 Standard, when the instance is stopped, it loses all its accrued credits, and its credit balance is reset to zero. When it is restarted, it receives a new set of launch credits, and begins to accrue earned credits. For T4g, T3a, and T3 Standard instances, the CPU credit balance persists for seven days after the instance stops and the credits are lost thereafter. If you start the instance within seven days, no credits are lost.
T2 Standard instances receive two types of CPU credits: earned credits and launch credits. When a T2 Standard instance is in a running state, it continuously earns (at a millisecond-level resolution) a set rate of earned credits per hour. At start, it has not yet earned credits for a good startup experience; therefore, to provide a good startup experience, it receives launch credits at start, which it spends first while it accrues earned credits.

T4g, T3a, and T3 instances do not receive launch credits because they support Unlimited mode.
The Unlimited mode credit configuration enables T4g, T3a, and T3 instances to use as much CPU as needed to burst beyond baseline and for as long as needed.
Launch credits T2 Standard instances get 30 launch credits per vCPU at launch or start, and T1 Standard instances get 15 launch credits. For example, a t2.micro instance has one vCPU and gets 30 launch credits, while a t2.xlarge instance has four vCPUs and gets 120 launch credits. Launch credits are designed to provide a good startup experience to allow instances to burst immediately after launch before they have accrued earned credits.
Launch credits are spent first, before earned credits. Unspent launch credits are accrued in the CPU credit balance, but do not count towards the CPU credit balance limit. For example, a t2.micro instance has a CPU credit balance limit of 144 earned credits. If it is launched and remains idle for 24 hours, its CPU credit balance reaches 174 (30 launch credits + 144 earned credits), which is over the limit. However, after the instance spends the 30 launch credits, the credit balance cannot exceed 144. For more information about the CPU credit balance limit for each instance size, see the credit table.
The following table lists the initial CPU credit allocation received at launch or start, and the number of vCPUs.
Instance type Launch credits vCPUs t1.micro 15 1 t2.nano 30 1 t2.micro 30 1 t2.small 30 1 t2.medium 60 2 t2.large 60 2 t2.xlarge 120 4 t2.2xlarge 240 8

##### Launch credit limits There is a limit to the number of times T2 Standard instances can receive launch credits. The default limit is 100 launches or starts of all T2 Standard instances combined per account, per Region, per rolling 24-hour period. For example, the limit is reached when one instance is stopped and started 100 times within a 24-hour period, or when 100 instances are launched within a 24- hour period, or other combinations that equate to 100 starts. New accounts may have a lower limit, which increases over time based on your usage.
Tip To ensure that your workloads always get the performance they need, switch to Unlimited mode for burstable performance instances or consider using a larger instance size.
##### Differences between launch credits and earned credits The following table lists the differences between launch credits and earned credits.
Launch credits Earned credits Credit earn rate T2 Standard instances get 30 launch credits per vCPU at launch or start.
If a T2 instance is switched from unlimited  to standard, it does not get launch credits at the time of switching.
Each T2 instance continuously earns (at a millisecond-level resolution) a set rate of CPU credits per hour, depending on the instance size. For more information about the number of CPU credits earned per instance size, see the credit table.
Credit earn limit The limit for receiving launch credits is 100 launches or starts of all T2 Standard instances combined per account, per Region, per rolling 24- hour period. New accounts may have a lower limit, which increases over time based on your usage.
A T2 instance cannot accrue more credits than the CPU credit balance limit. If the CPU credit balance has reached its limit, any credits that are earned after the limit is reached are discarded. Launch credits do not count towards the limit. For more information about the CPU credit

Launch credits Earned credits balance limit for each T2 instance size, see the credit table.
Credit use Launch credits are spent first, before earned credits.
Earned credits are spent only after all launch credits are spent.
Credit expiration When a T2 Standard instance is running, launch credits do not expire.
When a T2 Standard instance stops or is switched to T2 Unlimited, all launch credits are lost.
When a T2 instance is running, earned credits that have accrued do not expire. When the T2 instance stops, all accrued earned credits are lost.
The number of accrued launch credits and accrued earned credits is tracked by the CloudWatch metric CPUCreditBalance. For more information, see CPUCreditBalance in the CloudWatch metrics table.
#### Standard mode examples for burstable instances The following examples explain credit use when instances are configured as standard.
Examples
- Example 1: Explain credit use with T3 Standard
- Example 2: Explain credit use with T2 Standard
##### Example 1: Explain credit use with T3 Standard In this example, you see how a t3.nano instance launched as standard earns, accrues, and spends earned credits. You see how the credit balance reflects the accrued earned credits.
A running t3.nano instance earns 144 credits every 24 hours. Its credit balance limit is 144 earned credits. After the limit is reached, new credits that are earned are discarded. For more information about the number of credits that can be earned and accrued, see the credit table.
You might launch a T3 Standard instance and use it immediately. Or, you might launch a T3 Standard instance and leave it idle for a few days before running applications on it. Whether an instance is used or remains idle determines if credits are spent or accrued. If an instance remains

idle for 24 hours from the time it is launched, the credit balance reaches it limit, which is the maximum number of earned credits that can be accrued.
This example describes an instance that remains idle for 24 hours from the time it is launched, and walks you through seven periods of time over a 96-hour period, showing the rate at which credits are earned, accrued, spent, and discarded, and the value of the credit balance at the end of each period.
The following workflow references the numbered points on the graph:
P1 – At 0 hours on the graph, the instance is launched as standard and immediately begins to earn credits. The instance remains idle from the time it is launched—CPU utilization is 0%—and no credits are spent. All unspent credits are accrued in the credit balance. For the first 24 hours, CPUCreditUsage is at 0, and the CPUCreditBalance value reaches its maximum of 144.
P2 – For the next 12 hours, CPU utilization is at 2.5%, which is below the 5% baseline. The instance earns more credits than it spends, but the CPUCreditBalance value cannot exceed its maximum of 144 credits. Any credits that are earned in excess of the limit are discarded.
P3 – For the next 24 hours, CPU utilization is at 7% (above the baseline), which requires a spend of 57.6 credits. The instance spends more credits than it earns, and the CPUCreditBalance value reduces to 86.4 credits.
P4 – For the next 12 hours, CPU utilization decreases to 2.5% (below the baseline), which requires a spend of 36 credits. In the same time, the instance earns 72 credits. The instance earns more credits than it spends, and the CPUCreditBalance value increases to 122 credits.
P5 – For the next two hours, the instance bursts at 60% CPU utilization, and depletes its entire CPUCreditBalance value of 122 credits. At the end of this period, with the CPUCreditBalance at zero, CPU utilization is forced to drop to the baseline utilization level of 5%. At the baseline, the instance earns as many credits as it spends.
P6 – For the next 14 hours, CPU utilization is at 5% (the baseline). The instance earns as many credits as it spends. The CPUCreditBalance value remains at 0.
P7 – For the last 24 hours in this example, the instance is idle and CPU utilization is 0%. During this time, the instance earns 144 credits, which it accrues in its CPUCreditBalance.

##### Example 2: Explain credit use with T2 Standard In this example, you see how a t2.nano instance launched as standard earns, accrues, and spends launch and earned credits. You see how the credit balance reflects not only accrued earned credits, but also accrued launch credits.
A t2.nano instance gets 30 launch credits when it is launched, and earns 72 credits every 24 hours. Its credit balance limit is 72 earned credits; launch credits do not count towards the limit.
After the limit is reached, new credits that are earned are discarded. For more information about the number of credits that can be earned and accrued, see the credit table. For more information about limits, see Launch credit limits.
You might launch a T2 Standard instance and use it immediately. Or, you might launch a T2 Standard instance and leave it idle for a few days before running applications on it. Whether an instance is used or remains idle determines if credits are spent or accrued. If an instance remains idle for 24 hours from the time it is launched, the credit balance appears to exceed its limit because the balance reflects both accrued earned credits and accrued launch credits. However, after CPU is used, the launch credits are spent first. Thereafter, the limit always reflects the maximum number of earned credits that can be accrued.
This example describes an instance that remains idle for 24 hours from the time it is launched, and walks you through seven periods of time over a 96-hour period, showing the rate at which credits are earned, accrued, spent, and discarded, and the value of the credit balance at the end of each period.

###### Period 1: 1 – 24 hours At 0 hours on the graph, the T2 instance is launched as standard and immediately gets 30 launch credits. It earns credits while in the running state. The instance remains idle from the time it is launched—CPU utilization is 0%—and no credits are spent. All unspent credits are accrued in the credit balance. At approximately 14 hours after launch, the credit balance is 72 (30 launch credits + 42 earned credits), which is equivalent to what the instance can earn in 24 hours. At 24 hours after launch, the credit balance exceeds 72 credits because the unspent launch credits are accrued in the credit balance—the credit balance is 102 credits: 30 launch credits + 72 earned credits.
Credit Spend Rate 0 credits per 24 hours (0% CPU utilization)
Credit Earn Rate 72 credits per 24 hours Credit Discard Rate 0 credits per 24 hours Credit Balance 102 credits (30 launch credits + 72 earned credits)
Conclusion If there is no CPU utilization after launch, the instance accrues more credits than what it can earn in 24 hours (30 launch credits + 72 earned credits = 102 credits).
In a real-world scenario, an EC2 instance consumes a small number of credits while launching and running, which prevents the balance from reaching the maximum theoretical value in this example.

###### Period 2: 25 – 36 hours For the next 12 hours, the instance continues to remain idle and earn credits, but the credit balance does not increase. It plateaus at 102 credits (30 launch credits + 72 earned credits). The credit balance has reached its limit of 72 accrued earned credits, so newly earned credits are discarded.
Credit Spend Rate 0 credits per 24 hours (0% CPU utilization)
Credit Earn Rate 72 credits per 24 hours (3 credits per hour)
Credit Discard Rate 72 credits per 24 hours (100% of credit earn rate)
Credit Balance 102 credits (30 launch credits + 72 earned credits)—balance is unchanged Conclusion An instance constantly earns credits, but it cannot accrue more earned credits if the credit balance has reached its limit. After the limit is reached, newly earned credits are discarded. Launch credits do not count towards the credit balance limit. If the balance includes accrued launch credits, the balance appears to be over the limit.

###### Period 3: 37 – 61 hours For the next 25 hours, the instance uses 2% CPU, which requires 30 credits. In the same period, it earns 75 credits, but the credit balance decreases. The balance decreases because the accrued launch credits are spent first, while newly earned credits are discarded because the credit balance is already at its limit of 72 earned credits.
Credit Spend Rate 28.8 credits per 24 hours (1.2 credits per hour, 2% CPU utilization, 40% of credit earn rate)— 30 credits over 25 hours Credit Earn Rate 72 credits per 24 hours Credit Discard Rate 72 credits per 24 hours (100% of credit earn rate)
Credit Balance 72 credits (30 launch credits were spent; 72 earned credits remain unspent)
Conclusion An instance spends launch credits first, before spending earned credits. Launch credits do not count towards the credit limit. After the launch credits are spent, the balance can never go higher than what can be earned in 24 hours. Furthermore, while an instance is running, it cannot get more launch credits.

###### Period 4: 62 – 72 hours For the next 11 hours, the instance uses 2% CPU, which requires 13.2 credits. This is the same CPU utilization as in the previous period, but the balance does not decrease. It stays at 72 credits.
The balance does not decrease because the credit earn rate is higher than the credit spend rate. In the time that the instance spends 13.2 credits, it also earns 33 credits. However, the balance limit is 72 credits, so any earned credits that exceed the limit are discarded. The balance plateaus at 72 credits, which is different from the plateau of 102 credits during Period 2, because there are no accrued launch credits.
Credit Spend Rate 28.8 credits per 24 hours (1.2 credits per hour, 2% CPU utilization, 40% of credit earn rate)— 13.2 credits over 11 hours Credit Earn Rate 72 credits per 24 hours Credit Discard Rate 43.2 credits per 24 hours (60% of credit earn rate)
Credit Balance 72 credits (0 launch credits, 72 earned credits)
—balance is at its limit Conclusion

After launch credits are spent, the credit balance limit is determined by the number of credits that an instance can earn in 24 hours. If the instance earns more credits than it spends, newly earned credits over the limit are discarded.
###### Period 5: 73 – 75 hours For the next three hours, the instance bursts at 20% CPU utilization, which requires 36 credits. The instance earns nine credits in the same three hours, which results in a net balance decrease of 27 credits. At the end of three hours, the credit balance is 45 accrued earned credits.
Credit Spend Rate 288 credits per 24 hours (12 credits per hour, 20% CPU utilization, 400% of credit earn rate)
—36 credits over 3 hours Credit Earn Rate 72 credits per 24 hours (9 credits over 3 hours)
Credit Discard Rate 0 credits per 24 hours Credit Balance 45 credits (previous balance (72) - spent credits (36) + earned credits (9))—balance decreases at a rate of 216 credits per 24 hours (spend rate 288/24 + earn rate 72/24 = balance decrease rate 216/24)
Conclusion

If an instance spends more credits than it earns, its credit balance decreases.
###### Period 6: 76 – 90 hours For the next 15 hours, the instance uses 2% CPU, which requires 18 credits. This is the same CPU utilization as in Periods 3 and 4. However, the balance increases in this period, whereas it decreased in Period 3 and plateaued in Period 4.
In Period 3, the accrued launch credits were spent, and any earned credits that exceeded the credit limit were discarded, resulting in a decrease in the credit balance. In Period 4, the instance spent fewer credits than it earned. Any earned credits that exceeded the limit were discarded, so the balance plateaued at its maximum of 72 credits.
In this period, there are no accrued launch credits, and the number of accrued earned credits in the balance is below the limit. No earned credits are discarded. Furthermore, the instance earns more credits than it spends, resulting in an increase in the credit balance.
Credit Spend Rate 28.8 credits per 24 hours (1.2 credits per hour, 2% CPU utilization, 40% of credit earn rate)— 18 credits over 15 hours Credit Earn Rate 72 credits per 24 hours (45 credits over 15 hours)
Credit Discard Rate 0 credits per 24 hours

Credit Balance 72 credits (balance increases at a rate of 43.2 credits per 24 hours—change rate = spend rate 28.8/24 + earn rate 72/24)
Conclusion If an instance spends fewer credits than it earns, its credit balance increases.
###### Period 7: 91 – 96 hours For the next six hours, the instance remains idle—CPU utilization is 0%—and no credits are spent.
This is the same CPU utilization as in Period 2, but the balance does not plateau at 102 credits—it plateaus at 72 credits, which is the credit balance limit for the instance.
In Period 2, the credit balance included 30 accrued launch credits. The launch credits were spent in Period 3. A running instance cannot get more launch credits. After its credit balance limit is reached, any earned credits that exceed the limit are discarded.
Credit Spend Rate 0 credits per 24 hours (0% CPU utilization)
Credit Earn Rate 72 credits per 24 hours Credit Discard Rate 72 credits per 24 hours (100% of credit earn rate)
Credit Balance 72 credits (0 launch credits, 72 earned credits)

Conclusion An instance constantly earns credits, but cannot accrue more earned credits if the credit balance limit has been reached. After the limit is reached, newly earned credits are discarded. The credit balance limit is determined by the number of credits that an instance can earn in 24 hours. For more information about credit balance limits, see the credit table.
### Configure burstable performance instances The steps for launching, monitoring, and modifying burstable performance instances (T instances) are similar. The key difference is the default credit specification when they launch.
Each T instance family comes with the following default credit specification:
- T4g, T3a, and T3 instances launch as unlimited
- T3 instances on a Dedicated Host can only launch as standard
- T2 instances launch as standard You can change the default credit specification for the account.
Tasks
- Configure the credit specification at launch
- Configure an Auto Scaling group to set the credit specification as unlimited
- Manage the credit specification of a burstable performance instance
- Manage the default credit specification for an account
#### Configure the credit specification at launch You can launch your T instances with a credit specification of unlimited or standard.
The following procedures describe how to use the EC2 console or the AWS CLI. For information about using an Auto Scaling group, see Configure an Auto Scaling group to set the credit specification as unlimited.
Console To configure the credit specification of an instance at launch
1. Follow the procedure to launch an instance.

2. Under Instance type, select a T instance type.
3. Expand Advanced details. For Credit specification, select a credit specification.
4. In the Summary panel, review your instance configuration, and then choose Launch instance.
AWS CLI To set the credit specification of an instance at launch Use the run-instances command with the --credit-specification option.
--credit-specification CpuCredits=unlimited PowerShell To set the credit specification of an instance at launch Use the New-EC2Instance cmdlet with the -CreditSpecification_CpuCredit parameter.
-CreditSpecification_CpuCredit unlimited
#### Configure an Auto Scaling group to set the credit specification as unlimited When T instances are launched or started, they require CPU credits for a good bootstrapping experience. If you use an Auto Scaling group to launch your instances, we recommend that you configure your instances as unlimited. If you do, the instances use surplus credits when they are automatically launched or restarted by the Auto Scaling group. Using surplus credits prevents performance restrictions.
##### Create a launch template You must use a launch template for launching instances as unlimited in an Auto Scaling group. A launch configuration does not support launching instances as unlimited.
Console To create a launch template that sets the credit specification
1. Follow the Create a launch template using advanced settings procedure in the Amazon EC2 Auto Scaling User Guide.

2. In Launch template contents, for Instance type, choose an instance size.
3. To launch instances as unlimited in an Auto Scaling group, under Advanced details, for Credit specification, choose Unlimited.
4. When you've finished defining the launch template parameters, choose Create launch template.
AWS CLI To create a launch template that sets the credit specification Use the create-launch-template command. aws ec2 create-launch-template \ --launch-template-name my-launch-template \ --version-description FirstVersion \ --launch-template-data CreditSpecification={CpuCredits=unlimited} PowerShell To create a launch template that sets the credit specification Use the New-EC2LaunchTemplate cmdlet. Define the credit specification for the launch template data as follows.
$creditSpec = New-Object Amazon.EC2.Model.CreditSpecificationRequest $creditSpec.CpuCredits = "unlimited"
$launchTemplateData = New-Object Amazon.EC2.Model.RequestLaunchTemplateData $launchTemplateData.CreditSpecification = $creditSpec

##### Associate an Auto Scaling group with a launch template To associate the launch template with an Auto Scaling group, create the Auto Scaling group using the launch template, or add the launch template to an existing Auto Scaling group.
Console To create an Auto Scaling group using a launch template
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.

2. On the navigation bar at the top of the screen, select the same Region that you used when you created the launch template.
3. In the navigation pane, choose Auto Scaling Groups, Create Auto Scaling group.
4. Choose Launch Template, select your launch template, and then choose Next Step.
5. Complete the fields for the Auto Scaling group. When you've finished reviewing your configuration settings on the Review page, choose Create Auto Scaling group. For more information, see Creating an Auto Scaling Group Using a Launch Template in the Amazon EC2 Auto Scaling User Guide.
To add a launch template to an existing Auto Scaling group
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. On the navigation bar at the top of the screen, select the same Region that you used when you created the launch template.
3. In the navigation pane, choose Auto Scaling Groups.
4. From the Auto Scaling group list, select an Auto Scaling group, and choose Actions, Edit.
5. On the Details tab, for Launch Template, choose a launch template, and then choose Save.
AWS CLI To create an Auto Scaling group using a launch template Use the create-auto-scaling-group command and specify the --launch-template parameter.
To add a launch template to an existing Auto Scaling group Use the update-auto-scaling-group command and specify the --launch-template parameter.
PowerShell To create an Auto Scaling group using a launch template Use the New-ASAutoScalingGroup cmdlet and specify the - LaunchTemplate_LaunchTemplateId or -LaunchTemplate_LaunchTemplateName parameter.
To add a launch template to an existing Auto Scaling group

Use the Update-ASAutoScalingGroup cmdlet and specify the - LaunchTemplate_LaunchTemplateId or -LaunchTemplate_LaunchTemplateName parameter.
#### Manage the credit specification of a burstable performance instance You can switch the credit specification of a running or stopped T instance at any time between unlimited and standard.
Note that in unlimited mode, an instance can spend surplus credits, which might incur an additional charge. For more information, see Surplus credits can incur charges.
Console To manage the credit specification of an instance
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the left navigation pane, choose Instances.
3. (Optional) Select an instance. On its Details tab, find Credit specification. The value is either unlimited or standard.
4. (Optional) To modify the credit specification for multiple instances at the same time, select them all.
5. Choose Actions, Instance settings, Change credit specification. This option is enabled only if you selected a T instance.
6. For Unlimited mode, select or clear the checkbox next to each instance ID.
AWS CLI To get the credit specification of an instance Use the describe-instance-credit-specifications command. If you do not specify an instance ID, all instances with the credit specification of unlimited are returned. The output would also include instances that were previously configured with the unlimited credit specification. For example, if you resize a T3 instance to an M4 instance, while it is configured as unlimited, Amazon EC2 returns the M4 instance. aws ec2 describe-instance-credit-specifications \

    --instance-id i-1234567890abcdef0 \ --query InstanceCreditSpecifications[].CpuCredits \ --output text The following is example output. unlimited To set the credit specification of an instance Use the modify-instance-credit-specification command. aws ec2 modify-instance-credit-specification \ --region us-east-1 \ --instance-credit-specification "InstanceId=i-1234567890abcdef0,CpuCredits=unlimited"
PowerShell To get the credit specification of an instance Use the Get-EC2CreditSpecification cmdlet.
(Get-EC2CreditSpecification `
    -InstanceId i-1234567890abcdef0).CpuCredits The following is example output. unlimited To set the credit specification of an instance Use the Edit-EC2InstanceCreditSpecification cmdlet.
Edit-EC2InstanceCreditSpecification `
    -Region us-east-1 `
    -InstanceCreditSpecification @({InstanceId="i-1234567890abcdef0"
 CpuCredits="unlimited"})

#### Manage the default credit specification for an account Each T instance family comes with a default credit specification. You can change the default credit specification for each T instance family at the account level per AWS Region. The valid values for the default credit specification are unlimited and standard.
If you use the launch instance wizard in the EC2 console to launch instances, the value you select for the credit specification overrides the account-level default credit specification. If you use the AWS CLI to launch instances, all new T instances in the account launch using the default credit specification. The credit specification for existing running or stopped instances is not affected.
Consideration The default credit specification for an instance family can be modified only once in a rolling 5- minute period, and up to four times in a rolling 24-hour period.
Console To manage the default credit specification
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. To change the AWS Region, use the Region selector in the upper-right corner of the page.
3. On the left navigation pane, choose EC2 Dashboard.
4. From Account attributes, choose Default credit specification.
5. Choose Manage.
6. For each instance family, choose Unlimited or Standard, and then choose Update.
AWS CLI To get the default credit specification Use the get-default-credit-specification command. aws ec2 get-default-credit-specification \ --region us-east-1 \ --instance-family t2 \ --query InstanceFamilyCreditSpecifications[].CpuCredits \ --output text

The following is example output. standard To set the default credit specification Use the modify-default-credit-specification command. The following example sets the value to unlimited. aws ec2 modify-default-credit-specification \ --region us-east-1 \ --instance-family t2 \ --cpu-credits unlimited PowerShell To get the default credit specification Use the Get-EC2DefaultCreditSpecification cmdlet.
(Get-EC2DefaultCreditSpecification `
    -Region us-east-1 `
    -InstanceFamily t2).CpuCredits The following is example output. standard To set the default credit specification Use the Edit-EC2DefaultCreditSpecification cmdlet. The following example sets the value to unlimited.
Edit-EC2DefaultCreditSpecification `
    -Region us-east-1 `
    -InstanceFamily t2 `
    -CpuCredit unlimited

### Monitor CPU credits for burstable instances EC2 sends metrics to Amazon CloudWatch. You can see the CPU credit metrics in the Amazon EC2 per-instance metrics of the CloudWatch console or by using the AWS CLI to list the metrics for each instance. For more information, see CloudWatch metrics that are available for your instances.
Contents
- Additional CloudWatch metrics for burstable performance instances
- Calculate CPU credit usage
#### Additional CloudWatch metrics for burstable performance instances Burstable performance instances have these additional CloudWatch metrics, which are updated every five minutes:
- CPUCreditUsage – The number of CPU credits spent during the measurement period.
- CPUCreditBalance – The number of CPU credits that an instance has accrued. This balance is depleted when the CPU bursts and CPU credits are spent more quickly than they are earned.
- CPUSurplusCreditBalance – The number of surplus CPU credits spent to sustain CPU utilization when the CPUCreditBalance value is zero.
- CPUSurplusCreditsCharged – The number of surplus CPU credits exceeding the maximum number of CPU credits that can be earned in a 24-hour period, and thus attracting an additional charge.
The last two metrics apply only to instances configured as unlimited.
The following table describes the CloudWatch metrics for burstable performance instances. For more information, see CloudWatch metrics that are available for your instances.
Metric Description CPUCreditUsage The number of CPU credits spent by the instance for CPU utilization. One CPU credit equals one vCPU running at 100% utilization for one minute or an equivalent combination of vCPUs, utilization, and time (for example, one vCPU running at 50% utilization for two minutes or two vCPUs running at 25% utilization for two minutes).

Metric Description CPU credit metrics are available at a five-minute frequency only. If you specify a period greater than five minutes, use the Sum statistic instead of the Average statistic.
Units: Credits (vCPU-minutes)
CPUCreditBalance The number of earned CPU credits that an instance has accrued since it was launched or started. For T2 Standard, the CPUCreditBalance  also includes the number of launch credits that have been accrued.
Credits are accrued in the credit balance after they are earned, and removed from the credit balance when they are spent.
The credit balance has a maximum limit, determined by the instance size. After the limit is reached, any new credits that are earned are discarded. For T2 Standard, launch credits do not count towards the limit.
The credits in the CPUCreditBalance  are available for the instance to spend to burst beyond its baseline CPU utilization.
When an instance is running, credits in the CPUCredit Balance  do not expire. When a T4g, T3a or T3 instance stops, the CPUCreditBalance  value persists for seven days.
Thereafter, all accrued credits are lost. When a T2 instance stops, the CPUCreditBalance  value does not persist, and all accrued credits are lost.
CPU credit metrics are available at a five-minute frequency only.
Units: Credits (vCPU-minutes)

Metric Description CPUSurplusCreditBa lance The number of surplus credits that have been spent by an unlimited  instance when its CPUCreditBalance  value is zero.
The CPUSurplusCreditBalance value is paid down by earned CPU credits. If the number of surplus credits exceeds the maximum number of credits that the instance can earn in a 24-hour period, the spent surplus credits above the maximum incur an additional charge.
Units: Credits (vCPU-minutes)
CPUSurplusCreditsC harged The number of spent surplus credits that are not paid down by earned CPU credits, and which thus incur an additional charge.
Spent surplus credits are charged when any of the following occurs:
- The spent surplus credits exceed the maximum number of credits that the instance can earn in a 24-hour period. Spent surplus credits above the maximum are charged at the end of the hour.
- The instance is stopped or terminated.
- The instance is switched from unlimited  to standard.
Units: Credits (vCPU-minutes)
#### Calculate CPU credit usage The CPU credit usage of instances is calculated using the instance CloudWatch metrics described in the preceding table.
Amazon EC2 sends the metrics to CloudWatch every five minutes. A reference to the prior value of a metric at any point in time implies the previous value of the metric, sent five minutes ago.

##### Calculate CPU credit usage for Standard instances
- The CPU credit balance increases if CPU utilization is below the baseline, when the credits spent are less than the credits earned in the prior five-minute interval.
- The CPU credit balance decreases if CPU utilization is above the baseline, when the credits spent are more than the credits earned in the prior five-minute interval.
Mathematically, this is captured by the following equation:
Example CPUCreditBalance = prior CPUCreditBalance + [Credits earned per hour * (5/60) - CPUCreditUsage]
The size of the instance determines the number of credits that the instance can earn per hour and the number of earned credits that it can accrue in the credit balance. For information about the number of credits earned per hour, and the credit balance limit for each instance size, see the credit table.
Example This example uses a t3.nano instance. To calculate the CPUCreditBalance value of the instance, use the preceding equation as follows:
- CPUCreditBalance – The current credit balance to calculate.
- prior CPUCreditBalance – The credit balance five minutes ago. In this example, the instance had accrued two credits.
- Credits earned per hour – A t3.nano instance earns six credits per hour.
- 5/60 – Represents the five-minute interval between CloudWatch metric publication. Multiply the credits earned per hour by 5/60 (five minutes) to get the number of credits that the instance earned in the past five minutes. A t3.nano instance earns 0.5 credits every five minutes.
- CPUCreditUsage – How many credits the instance spent in the past five minutes. In this example, the instance spent one credit in the past five minutes.
Using these values, you can calculate the CPUCreditBalance value:

Example CPUCreditBalance = 2 + [0.5 - 1] = 1.5
##### Calculate CPU credit usage for Unlimited instances When a burstable performance instance needs to burst above the baseline, it always spends accrued credits before spending surplus credits. When it depletes its accrued CPU credit balance, it can spend surplus credits to burst CPU for as long as it needs. When CPU utilization falls below the baseline, surplus credits are always paid down before the instance accrues earned credits.
We use the term Adjusted balance in the following equations to reflect the activity that occurs in this five-minute interval. We use this value to arrive at the values for the CPUCreditBalance and CPUSurplusCreditBalance CloudWatch metrics.
Example Adjusted balance = [prior CPUCreditBalance - prior CPUSurplusCreditBalance] + [Credits earned per hour * (5/60) - CPUCreditUsage]
A value of 0 for Adjusted balance indicates that the instance spent all its earned credits for bursting, and no surplus credits were spent. As a result, both CPUCreditBalance and CPUSurplusCreditBalance are set to 0.
A positive Adjusted balance value indicates that the instance accrued earned credits, and previous surplus credits, if any, were paid down. As a result, the Adjusted balance value is assigned to CPUCreditBalance, and the CPUSurplusCreditBalance is set to 0. The instance size determines the maximum number of credits that it can accrue.
Example CPUCreditBalance = min [max earned credit balance, Adjusted balance]
CPUSurplusCreditBalance = 0 A negative Adjusted balance value indicates that the instance spent all its earned credits that it accrued and, in addition, also spent surplus credits for bursting. As a result, the Adjusted balance value is assigned to CPUSurplusCreditBalance and CPUCreditBalance is set to 0.
Again, the instance size determines the maximum number of credits that it can accrue.

Example CPUSurplusCreditBalance = min [max earned credit balance, -Adjusted balance]
CPUCreditBalance = 0 If the surplus credits spent exceed the maximum credits that the instance can accrue, the surplus credit balance is set to the maximum, as shown in the preceding equation. The remaining surplus credits are charged as represented by the CPUSurplusCreditsCharged metric.
Example CPUSurplusCreditsCharged = max [-Adjusted balance - max earned credit balance, 0]
Finally, when the instance terminates, any surplus credits tracked by the CPUSurplusCreditBalance are charged. If the instance is switched from unlimited to standard, any remaining CPUSurplusCreditBalance is also charged.
## Performance acceleration with GPU instances GPU-based instances provide access to NVIDIA GPUs with thousands of compute cores. You can use these instances to accelerate scientific, engineering, and rendering applications by leveraging the CUDA or Open Computing Language (OpenCL) parallel computing frameworks. You can also use them for graphics applications, including game streaming, 3-D application streaming, and other graphics workloads.
Before you can activate or optimize a GPU-based instance, you must install the appropriate drivers, as follows:
- To install NVIDIA drivers on an instance with an attached NVIDIA GPU, such as a P3 or G4dn instance, see NVIDIA drivers.
- To install AMD drivers on an instance with an attached AMD GPU, such as a G4ad instance, see AMD drivers.
Contents
- Activate NVIDIA GRID Virtual Applications on your Amazon EC2 GPU-based instances
- Optimize GPU settings on Amazon EC2 instances
- Set up Dual 4K displays on G4ad Linux instances
- Get started with GPU accelerated instances

### Activate NVIDIA GRID Virtual Applications on your Amazon EC2 GPU-based instances instances To activate the GRID Virtual Applications on GPU-based instances that have NVIDIA GPUs (NVIDIA GRID Virtual Workstation is enabled by default), you must define the product type for the driver.
The process that you use depends on the operating system of your instance.
#### Linux instances To activate GRID Virtual Applications on your Linux instances
1. Create the /etc/nvidia/gridd.conf file from the provided template file.
[ec2-user ~]$ sudo cp /etc/nvidia/gridd.conf.template /etc/nvidia/gridd.conf
2. Open the /etc/nvidia/gridd.conf file in your favorite text editor.
3. Find the FeatureType line, and set it equal to 0. Then add a line with IgnoreSP=TRUE.
FeatureType=0 IgnoreSP=TRUE
4. Save the file and exit.
5. Reboot the instance to pick up the new configuration.
[ec2-user ~]$ sudo reboot
#### Windows instances To activate GRID Virtual Applications on your Windows instances
1. Run regedit.exe to open the registry editor.
2. Navigate to HKEY_LOCAL_MACHINE\SOFTWARE\NVIDIA Corporation\Global \GridLicensing.
3. Open the context (right-click) menu on the right pane and choose New, DWORD.
4. For Name, enter FeatureType and type Enter.
5. Open the context (right-click) menu on FeatureType and choose Modify.
6. For Value data, enter 0 for NVIDIA GRID Virtual Applications and choose OK.
7. Open the context (right-click) menu on the right pane and choose New, DWORD.

8. For Name, enter IgnoreSP and type Enter.
9. Open the context (right-click) menu on IgnoreSP and choose Modify.
10. For Value data, type 1 and choose OK.
11. Close the registry editor.
### Optimize GPU settings on Amazon EC2 instances There are several GPU setting optimizations that you can perform to achieve the best performance on NVIDIA GPU instances. With some of these instance types, the NVIDIA driver uses an autoboost feature, which varies the GPU clock speeds. By disabling autoboost and setting the GPU clock speeds to their maximum frequency, you can consistently achieve the maximum performance with your GPU instances.
#### Optimize GPU settings on Linux
1. Configure the GPU settings to be persistent. This command can take several minutes to run.
[ec2-user ~]$ sudo nvidia-persistenced
2. [G3, and P2 instances only] Disable the autoboost feature for all GPUs on the instance.
[ec2-user ~]$ sudo nvidia-smi --auto-boost-default=0
3. Set all GPU clock speeds to their maximum frequency. Use the memory and graphics clock speeds specified in the following commands.
Some versions of the NVIDIA driver do not support setting the application clock speed, and display the error "Setting applications clocks is not supported for GPU...", which you can ignore.
- G3 instances:
[ec2-user ~]$ sudo nvidia-smi -ac 2505,1177
- G4dn instances:
[ec2-user ~]$ sudo nvidia-smi -ac 5001,1590
- G5 instances:

[ec2-user ~]$ sudo nvidia-smi -ac 6250,1710
- G6, G6f, Gr6, and Gr6f instances:
[ec2-user ~]$ sudo nvidia-smi -ac 6251,2040
- G6e instances:
[ec2-user ~]$ sudo nvidia-smi -ac 9001,2520
- G7e instances:
[ec2-user ~]$ sudo nvidia-smi -ac 12481,2430
- P2 instances:
[ec2-user ~]$ sudo nvidia-smi -ac 2505,875
- P3 and P3dn instances:
[ec2-user ~]$ sudo nvidia-smi -ac 877,1530
- P4d instances:
[ec2-user ~]$ sudo nvidia-smi -ac 1215,1410
- P4de instances:
[ec2-user ~]$ sudo nvidia-smi -ac 1593,1410
- P5 instances:
[ec2-user ~]$ sudo nvidia-smi -ac 2619,1980
- P5e and P5en instances:
[ec2-user ~]$ sudo nvidia-smi -ac 3201,1980
- P6-B200 instances:

[ec2-user ~]$ sudo nvidia-smi -ac 3996,1965
- P6-B300 instances:
[ec2-user ~]$ sudo nvidia-smi -ac 3996,2032
#### Optimize GPU settings on Windows
1. Open a PowerShell window and navigate to the NVIDIA installation folder.
PS C:\> cd "C:\Windows\System32\DriverStore\FileRepository\nvgridsw_aws.inf_*\"
2. [G3, and P2 instances only] Disable the autoboost feature for all GPUs on the instance.
PS C:\> .\nvidia-smi --auto-boost-default=0
3. Set all GPU clock speeds to their maximum frequency. Use the memory and graphics clock speeds specified in the following commands.
Some versions of the NVIDIA driver do not support setting the application clock speed, and display the error "Setting applications clocks is not supported for GPU...", which you can ignore.
- G3 instances:
PS C:\> .\nvidia-smi -ac "2505,1177"
- G4dn instances:
PS C:\> .\nvidia-smi -ac "5001,1590"
- G5 instances:
PS C:\> .\nvidia-smi -ac "6250,1710"
- G6, G6f, Gr6, and Gr6f instances:
PS C:\> .\nvidia-smi -ac "6251,2040"

- G6e instances:
PS C:\> .\nvidia-smi -ac "9001,2520"
- P2 instances:
PS C:\> .\nvidia-smi -ac "2505,875"
- P3 and P3dn instances:
PS C:\> .\nvidia-smi -ac "877,1530"
### Set up Dual 4K displays on G4ad Linux instances After you launch a G4ad instance, you can set up dual 4K displays.
To install the AMD drivers and configure dual screens
1. Connect to your Linux instance to get the PCI Bus address of the GPU you want to target for dual 4K (2x4k): lspci -vv | grep -i amd You will get output similar to the following:
00:1e.0 Display controller: Advanced Micro Devices, Inc. [*AMD*/ATI] Device 7362 (rev c3)
Subsystem: Advanced Micro Devices, Inc. [AMD/ATI] Device 0a34
2. Note the PCI bus address is 00:1e.0 in the above output. Create a file named /etc/ modprobe.d/amdgpu.conf and add: options amdgpu virtual_display=0000:00:1e.0,2
3. To install the AMD drivers on Linux, see AMD drivers for your EC2 instance. If you already have the AMD GPU driver installed, you will need to rebuild the amdgpu kernel modules through dkms.
4. Use the below xorg.conf file to define the dual (2x4K) screen topology and save the file in /etc/ X11/xorg.conf:

~$ cat /etc/X11/xorg.conf Section "ServerLayout"
    Identifier     "Layout0"
    Screen          0 "Screen0"
    Screen        1 "Screen1"
    InputDevice     "Keyboard0" "CoreKeyboard"
    InputDevice     "Mouse0" "CorePointer"
    Option          "Xinerama" "1"
EndSection Section "Files"
    ModulePath "/opt/amdgpu/lib64/xorg/modules/drivers"
    ModulePath "/opt/amdgpu/lib/xorg/modules"
    ModulePath "/opt/amdgpu-pro/lib/xorg/modules/extensions"
    ModulePath "/opt/amdgpu-pro/lib64/xorg/modules/extensions"
    ModulePath "/usr/lib64/xorg/modules"
    ModulePath "/usr/lib/xorg/modules"
EndSection Section "InputDevice"
    # generated from default Identifier     "Mouse0"
    Driver         "mouse"
    Option         "Protocol" "auto"
    Option         "Device" "/dev/psaux"
    Option         "Emulate3Buttons" "no"
    Option         "ZAxisMapping" "4 5"
EndSection Section "InputDevice"
    # generated from default Identifier     "Keyboard0"
    Driver         "kbd"
EndSection Section "Monitor"
    Identifier     "Virtual"
    VendorName     "Unknown"
    ModelName      "Unknown"
    Option         "Primary" "true"
EndSection Section "Monitor"
    Identifier     "Virtual-1"
    VendorName     "Unknown"
    ModelName      "Unknown"

    Option         "RightOf" "Virtual"
EndSection Section "Device"
    Identifier     "Device0"
    Driver         "amdgpu"
    VendorName     "AMD"
    BoardName      "Radeon MxGPU V520"
    BusID          "PCI:0:30:0"
EndSection Section "Device"
    Identifier     "Device1"
    Driver         "amdgpu"
    VendorName     "AMD"
    BoardName      "Radeon MxGPU V520"
    BusID          "PCI:0:30:0"
EndSection Section "Extensions"
    Option         "DPMS" "Disable"
EndSection Section "Screen"
    Identifier     "Screen0"
    Device         "Device0"
    Monitor        "Virtual"
    DefaultDepth   24 Option         "AllowEmptyInitialConfiguration" "True"
    SubSection "Display"
        Virtual    3840 2160 Depth      32 EndSubSection EndSection Section "Screen"
    Identifier     "Screen1"
    Device         "Device1"
    Monitor        "Virtual"
    DefaultDepth   24 Option         "AllowEmptyInitialConfiguration" "True"
    SubSection "Display"
        Virtual    3840 2160 Depth      32

    EndSubSection EndSection
5. Set up DCV by following the instructions in setting up an interactive desktop.
6. After the DCV set up is complete, reboot.
7. Confirm that the driver is functional: dmesg | grep amdgpu The response should look like the following:
Initialized amdgpu
8. You should see in the output for DISPLAY=:0 xrandr -q that you have 2 virtual displays connected:
~$ DISPLAY=:0 xrandr -q Screen 0: minimum 320 x 200, current 3840 x 1080, maximum 16384 x 16384 Virtual connected primary 1920x1080+0+0 (normal left inverted right x axis y axis)
 0mm x 0mm 4096x3112  60.00 3656x2664  59.99 4096x2160  60.00 3840x2160  60.00 1920x1200  59.95 1920x1080  60.00 1600x1200  59.95 1680x1050  60.00 1400x1050  60.00 1280x1024  59.95 1440x900 59.99 1280x960 59.99 1280x854 59.95 1280x800 59.96 1280x720 59.97 1152x768 59.95 1024x768 60.00 59.95 800x600  60.32 59.96 56.25 848x480  60.00 59.94 720x480  59.94 640x480  59.94 59.94

Virtual-1 connected 1920x1080+1920+0 (normal left inverted right x axis y axis) 0mm x 0mm 4096x3112  60.00 3656x2664  59.99 4096x2160  60.00 3840x2160  60.00 1920x1200  59.95 1920x1080  60.00 1600x1200  59.95 1680x1050  60.00 1400x1050  60.00 1280x1024  59.95 1440x900 59.99 1280x960 59.99 1280x854 59.95 1280x800 59.96 1280x720 59.97 1152x768 59.95 1024x768 60.00 59.95 800x600  60.32 59.96 56.25 848x480  60.00 59.94 720x480  59.94 640x480  59.94 59.94
9. When you connect into DCV, change the resolution to 2x4K, confirming the dual monitor support is registered by DCV.
#### Set up an interactive desktop for Linux After you confirm that your Linux instance has the AMD GPU driver installed and amdgpu is in use, you can install an interactive desktop manager. We recommend the MATE desktop environment for the best compatibility and performance.
Prerequisite Open a text editor and save the following as a file named xorg.conf. You'll need this file on your instance.
Section "ServerLayout"

Identifier     "Layout0"
Screen          0 "Screen0"
InputDevice     "Keyboard0" "CoreKeyboard"
InputDevice     "Mouse0" "CorePointer"
EndSection Section "Files"
ModulePath "/opt/amdgpu/lib64/xorg/modules/drivers"
ModulePath "/opt/amdgpu/lib/xorg/modules"
ModulePath "/opt/amdgpu-pro/lib/xorg/modules/extensions"
ModulePath "/opt/amdgpu-pro/lib64/xorg/modules/extensions"
ModulePath "/usr/lib64/xorg/modules"
ModulePath "/usr/lib/xorg/modules"
EndSection Section "InputDevice"
# generated from default Identifier     "Mouse0"
Driver         "mouse"
Option         "Protocol" "auto"
Option         "Device" "/dev/psaux"
Option         "Emulate3Buttons" "no"
Option         "ZAxisMapping" "4 5"
EndSection Section "InputDevice"
# generated from default Identifier     "Keyboard0"
Driver         "kbd"
EndSection Section "Monitor"
Identifier     "Monitor0"
VendorName     "Unknown"
ModelName      "Unknown"
EndSection Section "Device"
Identifier     "Device0"
Driver         "amdgpu"
VendorName     "AMD"
BoardName      "Radeon MxGPU V520"
BusID          "PCI:0:30:0"
EndSection Section "Extensions"
Option         "DPMS" "Disable"
EndSection Section "Screen"
Identifier     "Screen0"

Device         "Device0"
Monitor        "Monitor0"
DefaultDepth   24 Option         "AllowEmptyInitialConfiguration" "True"
SubSection "Display"
    Virtual    3840 2160 Depth      32 EndSubSection EndSection To set up an interactive desktop on Amazon Linux 2
1. Install the EPEL repository.
[ec2-user ~]$ sudo amazon-linux-extras install epel -y
2. Install the MATE desktop.
[ec2-user ~]$ sudo amazon-linux-extras install mate-desktop1.x -y [ec2-user ~]$ sudo yum groupinstall "MATE Desktop" -y [ec2-user ~]$ sudo systemctl disable firewalld
3. Copy the xorg.conf file to /etc/X11/xorg.conf.
4. Reboot the instance.
[ec2-user ~]$ sudo reboot
5. (Optional) Install the Amazon DCV server to use Amazon DCV as a high-performance display protocol, and then connect to a Amazon DCV session using your preferred client.
To set up an interactive desktop on Ubuntu
1. Install the MATE desktop.
$ sudo apt install xorg-dev ubuntu-mate-desktop -y $ sudo apt purge ifupdown -y
2. Copy the xorg.conf file to /etc/X11/xorg.conf.
3. Reboot the instance.

$ sudo reboot
4. Install the AMF encoder for the appropriate version of Ubuntu.
$ sudo apt install ./amdgpu-pro-20.20-*/amf-amdgpu-pro_20.20-*_amd64.deb
5. (Optional) Install the Amazon DCV server to use Amazon DCV as a high-performance display protocol, and then connect to a Amazon DCV session using your preferred client.
6. After the DCV installation give the DCV User video permissions:
$ sudo usermod -aG video dcv To set up an interactive desktop on CentOS
1. Install the EPEL repository.
$ sudo yum update -y $ sudo yum install epel-release -y
2. Install the MATE desktop.
$ sudo yum groupinstall "MATE Desktop" -y $ sudo systemctl disable firewalld
3. Copy the xorg.conf file to /etc/X11/xorg.conf.
4. Reboot the instance.
$ sudo reboot
5. (Optional) Install the Amazon DCV server to use Amazon DCV as a high-performance display protocol, and then connect to a Amazon DCV session using your preferred client.
### Get started with GPU accelerated instances The latest generation of GPU accelerated instance types, such as those shown in the following list deliver the highest performance capabilities for deep learning and high performance computing (HPC) applications. Select the instance type link to learn more about its capabilities.

- P6 family
- P6 family
- P5 family For a complete list of instance type specifications for accelerated instance types, see Accelerated computing in the Amazon EC2 Instance Types reference.
Software configuration The easiest way to get started with the latest generation GPU accelerated instance types is to launch an instance from an AWS Deep Learning AMI that's preconfigured with all of the required software. For the latest AWS Deep Learning AMIs for use with GPU accelerated instance types, see P6 Supported DLAMI in the AWS Deep Learning AMIs Developer Guide.
If you need to build a custom AMI to launch instances that host deep learning or HPC applications, we recommend that you install the following minimum software versions on top of your base image.
Instance type NVIDIA driver CUDA NVIDIA GDRCopy EFA installer NCCL EFA K8s ¹ G7e 575 12.9 2.5 1.45.0 2.28.3 0.5.10 P5 530 12.1 2.3 1.24.1 2.18.3 0.4.4 P5.4xlarge 530 12.1 2.3 1.43.1 ² 2.18.3 0.4.4 P5e 550 12.1 2.3 1.24.1 2.18.3 0.5.5 P5en 550 12.1 2.3 1.24.1 2.18.3 0.5.6 P6-B200 570 12.8 2.5 1.41.0 2.26.2-1 0.5.10 P6e- GB200 570 12.8 2.5 1.41.0 2.26.2-1 0.5.10 P6-B300 580 13.0 2.5 1.44.0 2.28.3 0.5.10

¹ The EFA K8s column contains the minimum recommended version for aws-efa-k8s-device- plugin.
² There is compatibility issue that affects P5.4xlarge instances when GPU-to-GPU communication uses Elastic Fabric Adapter (EFA) and the NVIDIA Collective Communications Library (NCCL). To mitigate the issue, set the environment variable FI_HMEM_DISABLE_P2P to 1, and ensure that you install EFA version 1.43.1 or newer.
Note If you use version 1.41.0 of the EFA installer, the aws-ofi-nccl plugin comes with it.
For earlier versions of the EFA installer, use aws-ofi-nccl plugin version 1.7.2-aws or later.
We also recommend that you configure the instance to not use deeper C-states. For more information, see High performance and low latency by limiting deeper C-states in the Amazon Linux 2 User Guide. The latest AWS Deep Learning Base GPU AMIs are preconfigured to not use deeper C-states.
For networking and Elastic Fabric Adapter (EFA) configuration see Maximize network bandwidth on Amazon EC2 instances with multiple network cards.
## Amazon EC2 Mac instances EC2 Mac instances are ideal for developing, building, testing, and signing applications for Apple platforms, such as iPhone, iPad, Mac, Vision Pro, Apple Watch, Apple TV, and Safari. You can connect to your Mac instance using SSH or Apple Remote Desktop (ARD).
Note The unit of billing is the dedicated host. The instances running on that host have no additional charge.
Amazon EC2 Mac instances natively support the macOS operating system.

- EC2 x86 Mac instances (mac1.metal) are built on 2018 Mac mini hardware powered by 3.2 GHz Intel eighth-generation (Coffee Lake) Core i7 processors, 6 physical and 12 logical cores, and 32 GiB of memory.
- EC2 M1 Mac instances (mac2.metal) are built on 2020 Mac mini hardware powered by Apple silicon M1 processor, 8 CPU cores, 8 GPU cores, 16 GiB of memory, and the 16-core Apple Neural Engine.
- EC2 M1 Ultra Mac instances (mac2-m1ultra.metal) are built on 2022 Mac Studio hardware powered by Apple silicon M1 Ultra processor, 20 CPU cores, 64 GPU cores, 128 GiB of memory, and the 32-core Apple Neural Engine.
- EC2 M2 Mac instances (mac2-m2.metal) are built on 2023 Mac mini hardware powered by Apple silicon M2 processor, 8 CPU cores, 10 GPU cores, 24 GiB of memory, and the 16-core Apple Neural Engine.
- EC2 M2 Pro Mac instances (mac2-m2pro.metal) are built on 2023 Mac mini hardware powered by Apple silicon M2 Pro processor, 12 CPU cores, 19 GPU cores, 32 GiB of memory, and the 16- core Apple Neural Engine.
- EC2 M4 Mac instances (mac-m4.metal) are built on 2024 Mac mini hardware powered by Apple silicon M4 processor, 10 CPU cores, 10 GPU cores, 24 GiB of memory, and the 16-core Apple Neural Engine.
- EC2 M4 Pro Mac Mac instances (mac-m4pro.metal) are built on 2024 Mac mini hardware powered by Apple silicon M4 Pro processor, 14 CPU cores, 20 GPU cores, 48 GiB of memory, and the 16-core Apple Neural Engine.
Amazon EC2 Mac Dedicated Hosts support Dedicated Host auto recovery and reboot-based host maintenance.
Contents
- Considerations
- Instance readiness
- EC2 macOS AMIs
- EC2 macOS Init
- Amazon EC2 System Monitor for macOS
- Related resources
- Launch a Mac instance using the AWS Management Console or the AWS CLI

- Connect to your Mac instance using SSH or a GUI
- Update the operating system and software on Amazon EC2 Mac instances
- Increase the size of an EBS volume on your Mac instance
- Stop or terminate your Amazon EC2 Mac instance
- Configure System Integrity Protection for Amazon EC2 Mac instances
- Find supported macOS versions for your Amazon EC2 Mac Dedicated Host
- Subscribe to macOS AMI notifications
- Retrieve macOS AMI IDs using AWS Systems Manager Parameter Store API
- Amazon EC2 macOS AMIs release notes
#### Considerations The following considerations apply to Mac instances:
- Mac instances are available only as bare metal instances on Dedicated Hosts, with a minimum allocation period of 24 hours before you can release the Dedicated Host. You can launch one Mac instance per Dedicated Host. You can share the Dedicated Host with the AWS accounts or organizational units within your AWS organization, or the entire AWS organization.
- Mac instances are available in different AWS Regions. For a list of Mac instance availability in each of the AWS Regions, see Amazon EC2 instance types by Region.
- Mac instances are available only as On-Demand Instances. They are not available as Spot Instances or Reserved Instances. You can save money on Mac instances by purchasing a Savings Plan.
- The compatibility of different Mac instance types with specific macOS Amazon Machine Images (AMIs) varies. For more information, see Amazon EC2 macOS AMIs release notes.
- EBS hotplug is supported.
- AWS does not manage or support the internal SSD on the Apple hardware. We strongly recommend that you use Amazon EBS volumes instead. EBS volumes provide the same elasticity, availability, and durability benefits on Mac instances as they do on any other EC2 instance.
- We recommend using an Amazon EBS volume with 10,000 IOPS and 400 MiB/s throughput with Mac instances for optimal performance. For more information, see Amazon EBS volume types in the Amazon EBS User Guide.
- Mac instances support Amazon EC2 Auto Scaling.

- On x86 Mac instances, automatic software updates are disabled. We recommend that you apply updates and test them on your instance before you put the instance into production. For more information, see Update the operating system and software on Amazon EC2 Mac instances.
- When you stop or terminate a Mac instance, a scrubbing workflow is performed on the Dedicated Host. For more information, see Stop or terminate your Amazon EC2 Mac instance.
- Important Apple Intelligence features are not available when booting Mac hardware from an external volume. As EC2 Mac instances boot from external EBS volumes by default, they do not support Apple Intelligence features.
- Warning Do not use FileVault. If you enable FileVault, the host fails to boot because the partitions are locked. If data encryption is required, use Amazon EBS encryption to avoid boot issues and performance impact. With Amazon EBS encryption, encryption operations occur on the host servers, ensuring the security of both data-at-rest and data-in-transit between the instances and their attached EBS storage. For more information, see Amazon EBS encryption in the Amazon EBS User Guide.
### Instance readiness After you launch a Mac instance, you'll need to wait until the instance is ready before you can connect to it. For an AWS vended AMI with a x86 Mac instance or a Apple silicon Mac instance, the launch time can range from approximately 6 minutes to 20 minutes. Depending on the chosen Amazon EBS volume sizes, the inclusion of additional scripts to user data, or additional loaded software on a custom macOS AMI, the launch time might increase.
You can use a small shell script, like the one below, to poll the describe-instance-status API to know when the instance is ready to be connected to. In the following command, replace the example instance ID with your own. for i in $(seq 1 200); do aws ec2 describe-instance-status --instance- ids=i-1234567890abcdef0 \ --query='InstanceStatuses[0].InstanceStatus.Status'; sleep 5; done;

### EC2 macOS AMIs Amazon EC2 macOS is designed to provide a stable, secure, and high-performance environment for developer workloads running on Amazon EC2 Mac instances. EC2 macOS AMIs includes packages that enable easy integration with AWS, such as launch configuration tools and popular AWS libraries and tools.
For more information about EC2 macOS AMIs, see Amazon EC2 macOS AMIs release notes.
AWS provides updated EC2 macOS AMIs on a regular basis that include updates to packages owned by AWS and the latest fully-tested macOS version. Additionally, AWS provides updated AMIs with the latest minor version updates or major version updates as soon as they can be fully tested and vetted. If you do not need to preserve data or customizations to your Mac instances, you can get the latest updates by launching a new instance using the current AMI and then terminating the previous instance. Otherwise, you can choose which updates to apply to your Mac instances.
For information about how to subscribe to macOS AMI notifications, see Subscribe to macOS AMI notifications.
### EC2 macOS Init EC2 macOS Init is used to initialize EC2 Mac instances at launch. It uses priority groups to run logical groups of tasks at the same time.
The launchd plist file is /Library/LaunchDaemons/com.amazon.ec2.macos-init.plist.
The files for EC2 macOS Init are located in /usr/local/aws/ec2-macos-init.
For more information, see https://github.com/aws/ec2-macos-init.
### Amazon EC2 System Monitor for macOS Amazon EC2 System Monitor for macOS provides CPU utilization metrics to Amazon CloudWatch. It sends these metrics to CloudWatch over a custom serial device in 1-minute periods. You can enable or disable this agent as follows. It is enabled by default. sudo setup-ec2monitoring [enable | disable]

Note Amazon EC2 System Monitor for macOS is not currently supported on Apple silicon Mac instances.
### Related resources For information about pricing, see Pricing.
For more information about Mac instances, see Amazon EC2 Mac Instances.
For more information about hardware specifications and network performance of Mac instances, see General purpose instances.
### Launch a Mac instance using the AWS Management Console or the AWS CLI EC2 Mac instances require a Dedicated Host. You first need to allocate a host to your account, and then launch the instance onto the host.
You can launch a Mac instance using the AWS Management Console or the AWS CLI.
#### Launch a Mac instance using the console To launch a Mac instance onto a Dedicated Host
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. Allocate the Dedicated Host, as follows: a.
In the navigation pane, choose Dedicated Hosts. b.
Choose Allocate Dedicated Host and then do the following: i.
For Instance family, choose a Mac Instance family. If the instance family doesn't appear in the list, it's not supported in the currently selected Region. ii.
For Instance type, choose the instance type based on the selected instance family chosen. iii.
For Availability Zone, choose the Availability Zone for the Dedicated Host. iv.
For Quantity, keep 1. v.
Choose Allocate.

3. Launch the instance on the host, as follows: a.
Select the Dedicated Host that you created and then do the following: i.
Choose Actions, Launch instance(s) onto host. ii.
Under Application and OS Images (Amazon Machine Image), select a macOS AMI. iii.
Under Instance type, select the Mac instance type. iv.
Under Advanced details, verify that Tenancy, Tenancy host by, and Tenancy host ID are preconfigured based on the Dedicated Host you created. Update Tenancy affinity as needed. v.
Complete the wizard, specifying EBS volumes, security groups, and key pairs as needed. vi.
In the Summary panel, choose Launch instance. b.
A confirmation page lets you know that your instance is launching. Choose View all instances to close the confirmation page and return to the console. The initial state of an instance is pending. The instance is ready when its state changes to running and it passes status checks.
#### Launch a Mac instance using the AWS CLI Allocate the Dedicated Host Use the following allocate-hosts command to allocate a Dedicated Host for your Mac instance, replacing the instance-type with a valid mac instance type, and the region and availability-zone with the appropriate ones for your environment. aws ec2 allocate-hosts --region us-east-1 --instance-type mac1.metal --availability- zone us-east-1b --auto-placement "on" --quantity 1 Launch the instance on the host Use the following run-instances command to launch a Mac instance, again replacing the instance-type with a valid mac instance type, and the region and availability-zone with the ones used previously. aws ec2 run-instances --region us-east-1 --instance-type mac1.metal --placement Tenancy=host --image-id ami_id --key-name my-key-pair

The initial state of an instance is pending. The instance is ready when its state changes to running and it passes status checks. Use the following describe-instance-status command to display status information for your instance. aws ec2 describe-instance-status --instance-ids i-017f8354e2dc69c4f The following is example output for an instance that is running and has passed status checks.
{ "InstanceStatuses": [ { "AvailabilityZone": "us-east-1b", "InstanceId": "i-017f8354e2dc69c4f", "InstanceState": { "Code": 16, "Name": "running"
            }, "InstanceStatus": { "Details": [ { "Name": "reachability", "Status": "passed"
                    } ], "Status": "ok"
            }, "SystemStatus": { "Details": [ { "Name": "reachability", "Status": "passed"
                    } ], "Status": "ok"
            } } ]
}
### Connect to your Mac instance using SSH or a GUI You can connect to your Mac instance using SSH or a graphical user interface (GUI).

Multiple users can access the OS simultaneously. Typically there is a 1:1 user:GUI session, due to the built-in Screen Sharing service on port 5900. Using SSH within macOS supports multiple sessions up until the "Max Sessions" limit in the sshd_config file.
#### Connect to your instance using SSH Amazon EC2 Mac instances do not allow remote root SSH by default. The ec2-user account is configured to log in remotely using SSH. The ec2-user account also has sudo privileges. After you connect to your instance, you can add other users.
To support connecting to your instance using SSH, launch the instance using a key pair and a security group that allows SSH access, and ensure that the instance has internet connectivity. You provide the .pem file for the key pair when you connect to the instance.
Use the following procedure to connect to your Mac instance using an SSH client. If you receive an error while attempting to connect to your instance, see Troubleshoot issues connecting to your Amazon EC2 Linux instance.
To connect to your instance using SSH
1. Verify that your local computer has an SSH client installed by entering ssh at the command line. If your computer doesn't recognize the command, search for an SSH client for your operating system and install it.
2. Get the public DNS name of your instance. Using the Amazon EC2 console, you can find the public DNS name on both the Details and the Networking tabs. Using the AWS CLI, you can find the public DNS name using the describe-instances command.
3. Locate the .pem file for the key pair that you specified when you launched the instance.
4. Connect to your instance using the following ssh command, specifying the public DNS name of the instance and the .pem file. ssh -i /path/key-pair-name.pem ec2-user@instance-public-dns-name Password authentication is disabled to prevent brute-force password attacks. Before you make changes to the SSH configuration, open /usr/local/aws/ec2-macos-init/init.toml and set secureSSHDConfig to false.

#### Connect to your instance's graphical user interface (GUI)
Use the following procedure to connect to your instance's GUI using VNC, Apple Remote Desktop (ARD), or the Apple Screen Sharing application (included with macOS).
Note macOS 10.14 and later only allows control if Screen Sharing is enabled through System Preferences.
To connect to your instance using ARD client or VNC client
1. Verify that your local computer has an ARD client or a VNC client that supports ARD installed.
On macOS, you can leverage the built-in Screen Sharing application. Otherwise, search for ARD for your operating system and install it.
2. From your local computer, connect to your instance using SSH.
3. Set up a password for the ec2-user account using the passwd command as follows.
[ec2-user ~]$ sudo passwd ec2-user
4. Install and start macOS Screen Sharing using the following command.
[ec2-user ~]$ sudo launchctl enable system/com.apple.screensharing sudo launchctl load -w /System/Library/LaunchDaemons/com.apple.screensharing.plist
5. Disconnect from your instance by typing exit and pressing Enter.
6. From your computer, connect to your instance using the following ssh command. In addition to the options shown in the previous section, use the -L option to enable port forwarding and forward all traffic on local port 5900 to the ARD server on the instance. ssh -L 5900:localhost:5900 -i /path/key-pair-name.pem ec2-user@instance-public-dns- name
7. From your local computer, use the ARD client or VNC client that supports ARD to connect to localhost:5900. For example, use the Screen Sharing application on macOS as follows: a.
Open Finder and select Go. b.
Select Connect to Server.

c.
In the Server Address field, enter vnc://localhost:5900. d.
Log in as prompted, using ec2-user as the username and the password that you created for the ec2-user account.
#### Modify macOS screen resolution on Mac instances After you connect to your EC2 Mac instance using ARD or a VNC client that supports ARD, you can modify the screen resolution of your macOS environment using any of the publicly available macOS tools or utilities, such as displayplacer.
To modify the screen resolution using displayplacer
1. Install displayplacer.
[ec2-user ~]$ brew tap jakehilborn/jakehilborn && brew install displayplacer
2. Show the current screen information and possible screen resolutions.
[ec2-user ~]$ displayplacer list
3. Apply the desired screen resolution.
[ec2-user ~]$ displayplacer "id:<screenID> res:<width>x<height> origin:(0,0) degree:0"
For example:
RES="2560x1600" displayplacer "id:69784AF1-CD7D-B79B-E5D4-60D937407F68 res:${RES} scaling:off origin:(0,0) degree:0"

### Update the operating system and software on Amazon EC2 Mac instances The following topic explains how to update the operating system and software on Apple silicon Mac instances (Mac2, Mac2-m1ultra, Mac2-m2, Mac2-m2pro, Mac-m4, and Mac-m4pro) and x86 Mac instances (Mac1).

Warning Installation of beta or preview macOS versions is only available on Apple silicon Mac instances. Amazon EC2 doesn't qualify beta or preview macOS versions and doesn't ensure instances will remain functional after an update to a pre-production macOS version.
Attempting to install beta or preview macOS versions on Amazon EC2 x86 Mac instances will lead to degradation of your Amazon EC2 Mac Dedicated Host when you stop or terminate your instances, and will prevent you from starting or launching a new instance on that host.
Note If you perform an in-place macOS update before AWS releases an official AMI, the update applies to the selected host only. If you have other hosts, or if you launch new hosts, you must perform the same update process on those hosts as well. Each macOS version requires a minimum firmware version on the underlying Apple Mac hardware. The in- place update only updates the firmware on the selected host and doesn't transfer to other existing or new hosts. To check which macOS versions are compatible with your Amazon EC2 Mac Dedicated Host, see  Find supported macOS versions for your Amazon EC2 Mac Dedicated Host.
#### Update software on Apple silicon Mac instances
##### Prerequisites Due to an update in the network driver configuration, ENA driver version 1.0.2 isn't compatible with macOS 13.3 and later. If you want to install any beta, preview, or production macOS version 13.3 or later and have not installed the latest ENA driver, use the following procedure to install a new version of the driver.
To install a new version of the ENA driver
1. In a Terminal window, connect to your Apple silicon Mac instance using SSH.
2. Update Homebrew and download the ENA application into the Applications file using the following command.

[ec2-user ~]$ brew update [ec2-user ~]$ brew install amazon-ena-ethernet-dext
3. Disconnect from your instance by typing exit and pressing return.
4. Use the VNC client to activate the ENA application. a.
Setup the VNC client using Connect to your instance's graphical user interface (GUI). b.
Once you have connected to your instance using the Screen Sharing application, go to the Applications folder and open the ENA application. c.
Choose Activate d.
To confirm the driver was activated correctly, run the following command in the Terminal window. The output of the command shows that the old driver is in the terminating state and the new driver is in the activated state. systemextensionsctl list; e.
After you restart the instance, only the new driver will be present.
##### Perform the software update On Apple silicon Mac instances, you must complete several steps to perform an in-place operating system update. This includes delegating ownership of the Amazon EBS root volume to the EBS root volume administrative user. You can choose to do this either automatically using an Amazon EC2 API, or you can do it manually by running the commands on your instance.
Automated volume ownership delegation (Recommended)
### Considerations
- It can take between 30 and 90 minutes for the volume ownership delegation task to complete. During this time, the instance is unreachable.
- The following macOS versions are supported:
- Mac2 | Mac2-m1ultra — macOS Ventura (version 13.0 or later)
- Mac2-m2 | Mac2-m2pro — macOS Ventura (version 13.2 or later)
- Mac-m4 | Mac-m4pro — macOS Sequoia (version 15.6 or later)

- Instances must have only one bootable volume, and each attached volume can have only one additional admin user.
Step 1: Set a password and enable the secure token for the EBS root volume administrative user You must set a password and enable the secure token for the Amazon EBS root volume administrative user (ec2-user).
Note The password and secure token are set the first time you connect to an Apple silicon Mac instance using the GUI. If you previously  connected to the instance using the GUI, you do not need to perform these steps.
1. Connect to the instance using SSH.
2. Set the password for the ec2-user user.
$ sudo /usr/bin/dscl . -passwd /Users/ec2-user
3. Enable the secure token for the ec2-user user. For -oldPassword, specify the same password from the previous step. For -newPassword, specify a different password. The following command assumes that you have your old and new passwords saved in .txt files.
$ sysadminctl -oldPassword `cat old_password.txt` -newPassword `cat new_password.txt`
4. Verify that the secure token is enabled.
$ sysadminctl -secureTokenStatus ec2-user Step 2: Delegate ownership of the Amazon EBS root volume to the EBS root volume administrative user To delegate ownership, you must create a volume ownership delegation task.

1. Use the  create-delegate-mac-volume-ownership-task command to create the task. For --instance-id, specify the ID of the instance. For --mac-credentials, specify the following credentials:
- Internal disk administrative user
- Username — Only the default administrative user (aws-managed-user) is supported and it is used by default. You can't specify a different administrative user.
- Password — If you did not change the default password for aws-managed-user, specify the default password, which is blank. Otherwise, specify your password.
- Amazon EBS root volume administrative user
- Username — If you did not change the default administrative user, specify ec2-user.
Otherwise, specify the username for your administrative user.
- Password — Specify the password that you set for root volume admin user in Step 1 above. aws ec2 create-delegate-mac-volume-ownership-task \ --instance-id i-1234567890abcdef0 \ --mac-credentials file://mac-credentials.json The following is the contents of the mac-credentials.json file referenced in the preceding examples.
{ "internalDiskPassword":"internal-disk-admin_password", "rootVolumeUsername":"root-volume-admin_username", "rootVolumepassword":"root-volume-admin_password"
}
2. Wait for the volume ownership delegation task to complete and for the instance to return to a healthy state. Use the  describe-mac-modification-tasks command. For --mac- modification-task-id, specify the ID of the volume ownership delegation task from the previous step. aws ec2 describe-mac-modification-tasks \ --mac-modification-task-id task-id
3. After the volume ownership delegation task completes, continue to Step 3.

Step 3: Update the software After you have delegated ownership of the Amazon EBS root volume, follow the steps described in Update software on x86 Mac instances (below) to update the software.
Manual volume ownership delegation As you work through this procedure, you create two passwords. One password is for the Amazon EBS root volume administrative user (ec2-user), and the other password is for the internal disk administrative user (aws-managed-user). Remember these passwords since you will use them as you work through the procedure.
Note With this procedure on macOS Big Sur, you can only perform minor updates such as updating from macOS Big Sur 11.7.3 to macOS Big Sur 11.7.4. For macOS Monterey or above, you can perform major software updates.
To access the internal disk
1. From your local computer, in the Terminal, connect to your Apple silicon Mac instance using SSH with the following command. For more information, see Connect to your instance using SSH. ssh -i /path/key-pair-name.pem ec2-user@instance-public-dns-name
2. Install and start macOS Screen Sharing using the following command.
[ec2-user ~]$ sudo launchctl enable system/com.apple.screensharing sudo launchctl load -w /System/Library/LaunchDaemons/ com.apple.screensharing.plist
3. Set a password for ec2-user with the following command. Remember the password as you will use it later.
[ec2-user ~]$ sudo /usr/bin/dscl . -passwd /Users/ec2-user
4. Disconnect from the instance by typing exit and pressing return.
5. From your local computer, in the Terminal, reconnect to your instance with an SSH tunnel to the VNC port using the following command.

ssh -i /path/key-pair-name.pem -L 5900:localhost:5900 ec2-user@instance-public- dns-name Note Do not exit this SSH session until the following VNC connection and GUI steps are completed. When the instance is restarted, the connection will close automatically.
6. From your local computer, connect to localhost:5900 using the following steps: a.
Open Finder and select Go. b.
Select Connect to Server. c.
In the Server Address field, enter vnc://localhost:5900.
7. In the macOS window, connect to the remote session of the Apple silicon Mac instance as ec2-user with the password you created in Step 3.
8. Access the internal disk, named InternalDisk, using one of the following options. a.
For macOS Ventura or above: Open System Settings, select General in the left pane, then Startup Disk at the lower right of the pane. b.
For macOS Monterey or below: Open System Preferences, select Startup Disk, then unlock the pane by choosing the lock icon in the lower left of the window.
Troubleshooting tip If you need to mount the internal disk, run the following command in the Terminal.
APFSVolumeName="InternalDisk" ; SSDContainer=$(diskutil list | grep "Physical Store disk0" -B 3 | grep "/dev/disk" | awk {'print $1'} ) ; diskutil apfs addVolume $SSDContainer APFS $APFSVolumeName
9. Choose the internal disk, named InternalDisk, and select Restart. Select Restart again when prompted.

Important If the internal disk is named Macintosh HD instead of InternalDisk, your instance needs to be stopped and restarted so the dedicated host can be updated. For more information, see Stop or terminate your Amazon EC2 Mac instance.
Use the following procedure to delegate ownership to the administrative user. When you reconnect to your instance with SSH, you boot from the internal disk using the special administrative user (aws-managed-user). The initial password for aws-managed-user is blank, so you need to overwrite it on your first connection. Then, you need to repeat the steps to install and start macOS Screen Sharing since the boot volume has changed.
To delegate ownership to the administrator on an Amazon EBS volume
1. From your local computer, in the Terminal, connect to your Apple silicon Mac instance using the following command. ssh -i /path/key-pair-name.pem aws-managed-user@instance-public-dns-name
2. When you receive the warning WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!, use one of the following commands to resolve this issue. a.
Clear out the known hosts using the following command. Then, repeat the previous step. rm ~/.ssh/known_hosts b.
Add the following to the SSH command in the previous step.
-o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no
3. Set the password for aws-managed-user with the following command. The aws- managed-user initial password is blank, so you need to overwrite it on your first connection. a.
[aws-managed-user ~]$ sudo /usr/bin/dscl . -passwd /Users/aws-managed- user password

b.
When you receive the prompt, Permission denied. Please enter user's old password:, press enter.
Troubleshooting tip If you get the error passwd: DS error: eDSAuthFailed, use the following command.
[aws-managed-user ~]$ sudo passwd aws-managed-user
4. Install and start macOS Screen Sharing using the following command.
[aws-managed-user ~]$ sudo launchctl enable system/com.apple.screensharing sudo launchctl load -w /System/Library/LaunchDaemons/ com.apple.screensharing.plist
5. Disconnect from the instance by typing exit and pressing return.
6. From your local computer, in the Terminal, reconnect to your instance with an SSH tunnel to the VNC port using the following command. ssh -i /path/key-pair-name.pem -L 5900:localhost:5900 aws-managed-user@instance- public-dns-name
7. From your local computer, connect to localhost:5900 using the following steps: a.
Open Finder and select Go. b.
Select Connect to Server. c.
In the Server Address field, enter vnc://localhost:5900.
8. In the macOS window, connect to the remote session of the Apple silicon Mac instance as aws-managed-user with the password you created in Step 3.
Note When prompted to sign in with your Apple ID, select Set Up Later.
9. Access the Amazon EBS volume using one of the following options.

a.
For macOS Ventura or later: Open System Settings, select General in the left pane, then Startup Disk at the lower right of the pane. b.
For macOS Monterey or earlier: Open System Preferences, select Startup Disk, then unlock the pane using the lock icon in the lower left of the window.
Note Until the reboot takes place, when prompted for an administrator password, use the password you set above for aws-managed-user. This password might be different from the one you set for ec2-user or the default administrator account on your instance. The following instructions specify when to use your instance's administrator password.
10. Select the Amazon EBS volume (the volume not named InternalDisk in the Startup Disk window) and choose Restart.
Note If you have multiple bootable Amazon EBS volumes attached to your Apple silicon Mac instance, be sure to use a unique name for each volume.
11. Confirm the restart, then choose Authorize Users when prompted.
12. On the Authorize user on this volume pane, verify that the administrative user (ec2-user by default) is selected, then select Authorize.
13. Enter the ec2-user password you created in Step 3 of the previous procedure, then select Continue.
14. Enter the password for the special administrative user (aws-managed-user) when prompted.
15. From your local computer, in the Terminal, reconnect to your instance using SSH with username ec2-user.
Troubleshooting tip If you get the warning WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!, run the following command and reconnect to your instance using SSH.

rm ~/.ssh/known_hosts
16. To perform the software update, use the commands under Update software on x86 Mac instances.
#### Update software on x86 Mac instances On x86 Mac instances, you can install operating system updates from Apple using the softwareupdate command.
To install operating system updates from Apple on x86 Mac instances
1. List the packages with available updates using the following command.
[ec2-user ~]$ softwareupdate --list
2. Install all updates or only specific updates. To install specific updates, use the following command.
[ec2-user ~]$ sudo softwareupdate --install label To install all updates instead, use the following command.
[ec2-user ~]$ sudo softwareupdate --install --all --restart System administrators can use AWS Systems Manager to roll out pre-approved operating system updates on x86 Mac instances. For more information, see the AWS Systems Manager User Guide.
You can use Homebrew to install updates to packages in the EC2 macOS AMIs, so that you have the latest version of these packages on your instances. You can also use Homebrew to install and run common macOS applications on Amazon EC2 macOS. For more information, see the Homebrew Documentation.
To install updates using Homebrew
1. Update Homebrew using the following command.

[ec2-user ~]$ brew update
2. List the packages with available updates using the following command.
[ec2-user ~]$ brew outdated
3. Install all updates or only specific updates. To install specific updates, use the following command.
[ec2-user ~]$ brew upgrade package name To install all updates instead, use the following command.
[ec2-user ~]$ brew upgrade
### Increase the size of an EBS volume on your Mac instance You can increase the size of your Amazon EBS volumes on your Mac instance. For more information, see Amazon EBS Elastic Volumes in the Amazon EBS User Guide.
After you increase the size of the volume, you must increase the size of your APFS container as follows.
Make increased disk space available for use
1. Determine if a restart is required. If you resized an existing EBS volume on a running Mac instance, you must reboot the instance to make the new size available. If disk space modification was done during launch time, a reboot will not be required.
View current status of disk sizes:
[ec2-user ~]$  diskutil list external physical /dev/disk0 (external, physical):
   #:                       TYPE NAME                    SIZE       IDENTIFIER 0:                 GUID_partition_scheme            *322.1 GB     disk0 1:                 EFI EFI                           209.7 MB     disk0s1 2:                 Apple_APFS Container disk2        321.9 GB     disk0s2
2. Copy and paste the following command.

[ec2-user ~]$ PDISK=$(diskutil list physical external | head -n1 | cut -d" " -f1)
APFSCONT=$(diskutil list physical external | grep "Apple_APFS" | tr -s " " | cut - d" " -f8) yes | sudo diskutil repairDisk $PDISK
3. Copy and paste the following command.
[ec2-user ~]$ sudo diskutil apfs resizeContainer $APFSCONT 0
### Stop or terminate your Amazon EC2 Mac instance When you stop a Mac instance, the instance remains in the stopping state for about 15 minutes before it enters the stopped state.
When you stop or terminate a Mac instance, Amazon EC2 performs a scrubbing workflow on the underlying Dedicated Host to erase the internal SSD, to clear the persistent NVRAM variables, and to update to the latest device firmware. This ensures that Mac instances provide the same security and data privacy as other EC2 Nitro instances. It also allows you to run the latest macOS AMIs.
During the scrubbing workflow, the Dedicated Host temporarily enters the pending state. On x86 Mac instances, the scrubbing workflow might take up to 50 minutes to complete. On Apple silicon Mac instances, the scrubbing workflow might take up to 110 minutes to complete. Additionally, on x86 Mac instances, if the device firmware needs to be updated, the scrubbing workflow might take up to 3 hours to complete.
You can't start the stopped Mac instance or launch a new Mac instance until after the scrubbing workflow completes, at which point the Dedicated Host enters the available state.
Metering and billing is paused when the Dedicated Host enters the pending state. You are not charged for the duration of the scrubbing workflow.
#### Release the Dedicated Host for your Mac instance When you are finished with your Mac instance, you can release the Dedicated Host. Before you can release the Dedicated Host, you must stop or terminate the Mac instance. You cannot release the host until the allocation period exceeds the 24-hour minimum.
To release the Dedicated Host
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.

2. In the navigation pane, choose Instances.
3. Select the instance and choose Instance state, then choose either Stop instance or Terminate instance.
4. In the navigation pane, choose Dedicated Hosts.
5. Select the Dedicated Host and choose Actions, Release host.
6. When prompted for confirmation, choose Release.
### Configure System Integrity Protection for Amazon EC2 Mac instances You can configure System Integrity Protection (SIP) settings for x86 Mac instances and Apple silicon Mac instances. SIP is a critical macOS security feature that helps to prevent unauthorized code execution and system-level modifications. For more information, see About System Integrity Protection.
You can either enable or disable SIP completely, or you can selectively enable or disable specific SIP settings. It is recommended that you disable SIP only temporarily to perform necessary tasks, and then reenable it as soon as possible. Leaving SIP disabled could leave your instance vulnerable to malicious code.
SIP configuration is supported in all AWS Regions where Amazon EC2 Mac instances are supported.
Topics
- Considerations
- Default SIP configurations
- Check your SIP configuration
- Prerequisites for Apple silicon Mac instances
- Configure SIP settings
- Check SIP configuration task status Considerations
- The following Amazon EC2 Mac instance types and macOS versions are supported:
- Mac1 | Mac2 | Mac2-m1ultra — macOS Ventura (version 13.0 or later)
- Mac2-m2 | Mac2-m2pro — macOS Ventura (version 13.2 or later)

- Mac-m4 | Mac-m4pro — macOS Sequoia (version 15.6 or later)
Note Beta and preview versions of macOS are not supported.
- You can specify a custom SIP configuration to selectively enable or disable individual SIP settings. If you implement a custom configuration, connect to the instance and verify the settings to ensure that your requirements are properly implemented and functioning as intended.
SIP configurations might change with macOS updates. We recommend that you review custom SIP settings after any macOS version upgrade to ensure continued compatibility and proper functionality of your security configurations.
- For x86 Mac instances, SIP settings are applied at the instance level. Any root volume attached to the instance will automatically inherit the configured SIP settings.
For Apple silicon Mac instances, SIP settings are applied at the volume level. Root volumes attached to the instance do not inherit the SIP settings. If you attach another root volume, you must reconfigure the SIP settings to the required state.
- It can take up to 90 mins for SIP configuration tasks to complete. The instance remains unreachable while the SIP configuration task in progress.
- SIP configurations do not transfer to snapshots or AMIs that you subsequently create from the instance.
- Apple silicon Mac instances must have only one bootable volume, and each attached volume can have only one additional admin user.
#### Default SIP configurations The following table lists the default SIP configuration for x86 Mac instances and Apple silicon Mac instances.

Apple silicon Mac instances x86 Mac instances Apple Internal Enabled Disabled Filesystem Protections Enabled Disabled

Apple silicon Mac instances x86 Mac instances Base System Enabled Enabled Debugging Restrictions Enabled Enabled Dtrace Restrictions Enabled Enabled Kext Signing Enabled Enabled Nvram Protections Enabled Enabled
#### Check your SIP configuration We recommend that you check your SIP configuration before and after making changes to ensure that it is configured as expected.
To check the SIP configuration for an Amazon EC2 Mac instance Connect to the instance using SSH, and then run the following command at the command line.
$ csrutil status The following is example output.
System Integrity Protection status: enabled.
Configuration:
    Apple Internal: enabled Kext Signing: disabled Filesystem Protections: enabled Debugging Restrictions: enabled DTrace Restrictions: enabled NVRAM Protections: enabled BaseSystem Verification: disabled
#### Prerequisites for Apple silicon Mac instances Before you can configure the SIP settings for Apple silicon Mac instances, you must set a password and enable the secure token for the Amazon EBS root volume administrative user (ec2-user).

Note The password and secure token are set the first time you connect to an Apple silicon Mac instance using the GUI. If you previously  connected to the instance using the GUI, or if you are using an x86 Mac instance, you do not need to perform these steps.
To set a password and enable the secure token for the EBS root volume administrative user
1. Connect to the instance using SSH.
2. Set the password for the ec2-user user.
$ sudo /usr/bin/dscl . -passwd /Users/ec2-user
3. Enable the secure token for the ec2-user user. For -oldPassword, specify the same password from the previous step. For -newPassword, specify a different password. The following command assumes that you have your old and new passwords saved in .txt files.
$ sysadminctl -oldPassword `cat old_password.txt` -newPassword `cat new_password.txt`
4. Verify that the secure token is enabled.
$ sysadminctl -secureTokenStatus ec2-user
#### Configure SIP settings When you configure the SIP settings for your instance, you can either enable or disable all SIP settings, or you can specify a custom configuration that selectively enables or disables specific SIP settings.
Note If you implement a custom configuration,  connect to the instance and verify the settings to ensure that your requirements are properly implemented and functioning as intended.

SIP configurations might change with macOS updates. We recommend that you review custom SIP settings after any macOS version upgrade to ensure continued compatibility and proper functionality of your security configurations.
To configure the SIP settings for your instance, you must create a SIP configuration task. The SIP configuration task specifies the SIP settings for your instance.
When you create a SIP configuration for an Apple silicon Mac instance, you must specify the following credentials:
- Internal disk administrative user
- Username — Only the default administrative user (aws-managed-user) is supported and it is used by default. You can't specify a different administrative user.
- Password — If you did not change the default password for aws-managed-user, specify the default password, which is blank. Otherwise, specify your password.
- Amazon EBS root volume administrative user
- Username — If you did not change the default administrative user, specify ec2-user.
Otherwise, specify the username for your administrative user.
- Password — You must always specify the password.
Use the following methods to create a SIP configuration task.
Console To create a SIP configuration task using the console
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation panel, choose Instances and then select the Amazon EC2 Mac instance.
3. In the Security tab, choose Modify Mac, Modify System Integrity Protection.
4. To enable all SIP settings, select Enable SIP. To disable all SIP settings, clear Enable SIP.
5. To specify a custom configuration that selectively enables or disables specific SIP settings, select Specify a custom SIP configuration, and then select the SIP settings to enable, or clear the SIP settings to disable.
6. Specify the credentials for the root volume user and internal disk owner.
7. Choose Create SIP modification task.

AWS CLI To create a SIP configuration task using the AWS CLI Use the  create-mac-system-integrity-protection-modification-task command.
Enable or disable all SIP settings To completely enable or disable all SIP settings, use only the --mac-system-integrity- protection-status parameter.
The following example command enables all SIP settings. aws ec2 create-mac-system-integrity-protection-modification-task \ --instance-id i-0abcdef9876543210 \ --mac-system-integrity-protection-status enabled \ --mac-credentials file://mac-credentials.json Specify a custom SIP configuration To specify a custom SIP configuration that selectively enables or disable specific SIP settings, specify the --mac-system-integrity-protection-status and --mac-system- integrity-protection-configuration parameters. In this case, use mac-system- integrity-protection-status to specify the overall SIP status, and use mac-system- integrity-protection-configuration to selectively enable or disable individual SIP settings.
The following example command creates a SIP configuration task to enable all SIP settings, except NvramProtections and FilesystemProtections. aws ec2 create-mac-system-integrity-protection-modification-task \ --instance-id i-0abcdef9876543210 \ --mac-system-integrity-protection-status enabled \ --mac-system-integrity-protection-configuration "NvramProtections=disabled, FilesystemProtections=disabled" \ --mac-credentials file://mac-credentials.json The following example command creates a SIP configuration task to disable all SIP settings, except DtraceRestrictions. aws ec2 create-mac-system-integrity-protection-modification-task \

--instance-id i-0abcdef9876543210 \ --mac-system-integrity-protection-status disabled \ --mac-system-integrity-protection-configuration "DtraceRestrictions=enabled" \ --mac-credentials file://mac-credentials.json Contents of the mac-credentials.json file The following is the contents of the mac-credentials.json file referenced in the preceding examples.
{ "internalDiskPassword":"internal-disk-admin_password", "rootVolumeUsername":"root-volume-admin_username", "rootVolumepassword":"root-volume-admin_password"
}
#### Check SIP configuration task status Use one of the following methods to check the state of SIP configuration tasks.
Console To view SIP configuration tasks using the console
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation panel, choose Instances and then select the Amazon EC2 Mac instance.
3. In the Security tab, scroll down to the Mac modification tasks section.
AWS CLI To check the state of SIP configuration tasks using the AWS CLI Use the  describe-mac-modification-tasks command.
### Find supported macOS versions for your Amazon EC2 Mac Dedicated Host You can view the latest macOS versions supported by your Amazon EC2 Mac Dedicated Host. With this functionality, you can validate whether your Dedicated Host can support instance launches with your preferred macOS versions.

Each macOS version requires a minimum firmware version on the underlying Apple Mac to successfully boot. The Apple Mac firmware version can become outdated if an allocated Mac Dedicated Host has remained idle for an extended period of time or if it has a long running instance on it.
To ensure supportability for the latest macOS versions, you can stop or terminate instances on your allocated Mac Dedicated Host. This triggers the host scrubbing workflow and updates the firmware on the underlying Apple Mac to support the latest macOS versions. A Dedicated Host with a long running instance will automatically be updated when you stop or terminate a running instance.
For more information about the scrubbing workflow, see Stop or terminate your Amazon EC2 Mac instance.
For more information about launching Mac instances, see Launch a Mac instance using the AWS Management Console or the AWS CLI.
You can view information about the latest macOS versions supported on your allocated Dedicated Host using the Amazon EC2 console or the AWS CLI.
Console To view Dedicated Host firmware information using the console
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Dedicated Hosts.
3. On the Dedicated Hosts details page, under Latest supported macOS versions, you can see the latest macOS versions that the host can support.
AWS CLI To view Dedicated Host firmware information using the AWS CLI Use the describe-mac-hosts command, replacing region with the appropriate AWS Region.
$ aws ec2 describe-mac-hosts --region us-east-1 { "MacHosts": [ { "HostId": "h-07879acf49EXAMPLE", "MacOSLatestSupportedVersions": [

                  "14.3", "13.6.4", "12.7.3"
              ]
          } ]
  }
### Subscribe to macOS AMI notifications To be notified when new AMIs are released or when bridgeOS has been updated, subscribe for notifications using Amazon SNS.
For more information about EC2 macOS AMIs, see Amazon EC2 macOS AMIs release notes.
To subscribe to macOS AMI notifications
1. Open the Amazon SNS console at https://console.aws.amazon.com/sns/v3/home.
2. In the navigation bar, change the Region to US East (N. Virginia), if necessary. You must use this Region because the SNS notifications that you are subscribing to were created in this Region.
3. In the navigation pane, choose Subscriptions.
4. Choose Create subscription.
5. For the Create subscription dialog box, do the following: a.
For Topic ARN, copy and paste one of the following Amazon Resource Names (ARNs):
- arn:aws:sns:us-east-1:898855652048:amazon-ec2-macos-ami-updates
- arn:aws:sns:us-east-1:898855652048:amazon-ec2-bridgeos-updates b.
For Protocol, choose one of the following:
- Email:
For Endpoint, type an email address that you can use to receive the notifications. After you create your subscription you'll receive a confirmation message with the subject line AWS Notification - Subscription Confirmation. Open the email and choose Confirm subscription to complete your subscription
- SMS:

For Endpoint, type a phone number that you can use to receive the notifications.
- AWS Lambda, Amazon SQS, Amazon Data Firehose (Notifications come in JSON format):
For Endpoint, enter the ARN for the Lambda function, SQS queue, or Firehose stream you can use to receive the notifications. c.
Choose Create subscription.
Whenever macOS AMIs are released, we send notifications to the subscribers of the amazon- ec2-macos-ami-updates topic. Whenever bridgeOS is updated, we send notifications to the subscribers of the amazon-ec2-bridgeos-updates topic. If you no longer want to receive these notifications, use the following procedure to unsubscribe.
To unsubscribe from macOS AMI notifications
1. Open the Amazon SNS console at https://console.aws.amazon.com/sns/v3/home.
2. In the navigation bar, change the Region to US East (N. Virginia), if necessary. You must use this Region because the SNS notifications were created in this Region.
3. In the navigation pane, choose Subscriptions.
4. Select the subscriptions and then choose Actions, Delete subscriptions When prompted for confirmation, choose Delete.
### Retrieve macOS AMI IDs using AWS Systems Manager Parameter Store API You must specify an AMI when you launch an instance. An AMI is specific to an AWS Region, operating system, and processor architecture. You can view all of the macOS AMIs in an AWS Region and retrieve the latest macOS AMI by querying the AWS Systems Manager Parameter Store API. Using these public parameters, you don't need to manually look up macOS AMI IDs. Public parameters are available for both x86 and ARM64 macOS AMIs, and can be integrated with your existing AWS CloudFormation templates.
Required permissions To perform this action, the IAM principal must have permissions to call the ssm:GetParameter API action.
To view a list of all macOS AMIs in the current AWS Region using the AWS CLI

Use the following get-parameters-by-path command to view a list of all macOS AMIs in the current Region. aws ssm get-parameters-by-path --path /aws/service/ec2-macos --recursive --query "Parameters[].Name"
To retrieve the AMI ID of the latest major macOS AMI using the AWS CLI Use the following get-parameter command with the sub-parameter image_id. In the following example, replace sonoma with a macOS supported major version, x86_64_mac with the processor, and region-code with a supported AWS Region for which you want the latest macOS AMI ID. aws ssm get-parameter --name /aws/service/ec2-macos/sonoma/x86_64_mac/latest/image_id --region region-code For more information, see Calling AMI public parameters for macOS in the AWS Systems Manager User Guide.
### Amazon EC2 macOS AMIs release notes The following information provides details about the packages included by default in the EC2 macOS AMIs and summarizes the changes for each EC2 macOS AMI release.
For information about how to subscribe to macOS AMI notifications, see Subscribe to macOS AMI notifications.
Mac instances can run one of the following operating systems:
- macOS Mojave (version 10.14) (x86 Mac instances only)
- macOS Catalina (version 10.15) (x86 Mac instances only)
- macOS Big Sur (version 11) (x86 and M1 Mac instances)
- macOS Monterey (version 12) (x86 and M1 Mac instances)
- macOS Ventura (version 13) (all Mac instances, M2 and M2 Pro Mac instances support macOS Ventura version 13.2 or later)
- macOS Sonoma (version 14) (all Mac instances)
- macOS Sequoia (version 15) (all Mac instances)

Note M4 and M4 Pro Mac instances support macOS Sequoia version 15.6 or later.
#### Approve Local Network Privacy policies for macOS Sequoia macOS Sequoia (version 15) has a new Local Network Privacy feature that impacts users of local IP- based services, including Amazon EC2 Instance Metadata Service (IMDS).
Important To make sure that you have uninterrupted access to local IP-based services, use the following steps to approve the Local Network Privacy policies.
To approve Local Network Privacy policies
1. Connect to your instance's graphical user interface (GUI).
2. Follow the prompts on the screen to approve the Local Network Privacy policies.
3. After you have approved the policies, create an AMI of your EC2 Mac instance. For more information, see Create an Amazon EBS-backed AMI.
Any EC2 Mac instances that are launched from the newly created AMI will retain the Local Network Privacy permissions.
#### Default packages included in Amazon EC2 macOS AMIs The following table describes packages that are included by default in the EC2 macOS AMIs.
Packages Release notes EC2 macOS Init https://github.com/aws/ec2-macos-init/tags EC2 macOS Utils https://github.com/aws/ec2-macos-utils/tags Amazon SSM Agent https://github.com/aws/amazon-ssm-agent/r eleases

Packages Release notes AWS Command Line Interface (AWS CLI) version 2 https://raw.githubusercontent.com/aws/aws- cli/v2/CHANGELOG.rst Command Line Tools for Xcode https://developer.apple.com/documentation/ xcode-release-notes Homebrew https://github.com/Homebrew/brew/releases EC2 Instance Connect https://github.com/aws/aws-ec2-instance-co nnect-config/releases Safari https://developer.apple.com/documentation/ safari-release-notes
#### Amazon EC2 macOS AMI updates The following table describes changes included in the EC2 macOS AMI releases. Note that some changes apply to all EC2 macOS AMIs, whereas others apply to only a subset of these AMIs.
##### EC2 macOS AMI updates Release Changes 2025.12.26 All AMIs
- Updated awscli to 2.32.19
- Updated Homebrew to 5.0.6 Release of macOS Sonoma 14.8.3
- Security content of macOS Sonoma 14.8.3
- Updated Safari to 26.2
- Security content of Safari 26.2

Release Changes Release of macOS Sequoia 15.7.3
- Security content of macOS Sequoia 15.7.3
- Updated Safari to 26.2
- Security content of Safari 26.2
- Updated Command Line Tools to 26.2 Release of macOS Tahoe 26.2
- Security content of macOS Tahoe 26.2
- Updated Command Line Tools to 26.2

Release Changes 2025.12.17 All AMIs
- Updated awscli to 2.32.16
- Updated Homebrew to 5.0.5 Release of macOS Sonoma 14.8.2
- Security content of macOS Sonoma 14.8.2
- Updated Safari to 26.1
- Security content of Safari 26.1 Release of macOS Sequoia 15.7.2
- Security content of macOS Sequoia 15.7.2
- Updated Safari to 26.1
- Security content of Safari 26.1
- Updated Command Line Tools to 26.1 Release of macOS Tahoe 26.1
- Security content of macOS Tahoe 26.1
- Updated Command Line Tools to 26.1

Release Changes 2025.11.18 All AMIs
- Updated awscli to 2.31.35
- Updated ec2-macos-init  to 1.5.13
- Updated ec2-macos-utils  to 1.0.7
- Updated Homebrew to 5.0.1 Release of macOS Sonoma 14.8.1
- Security content of macOS Sonoma 14.8.1
- Updated Safari to 26.0.1
- Security content of Safari 26.0.1 Release of macOS Sequoia 15.7.1
- Security content of macOS Sequoia 15.7.1
- Updated Safari to 26.0.1
- Security content of Safari 18.6
- Updated Command Line Tools to 26.0 Release of macOS Tahoe 26.0.1
- Security content of macOS Tahoe 26.0.1
- Updated Command Line Tools to 26.0

Release Changes 2025.09.04 All AMIs
- Updated awscli to 2.28.19
- Updated Homebrew to 4.6.7 Release of macOS Ventura 13.7.8
- Security content of macOS Ventura 13.7.8 Release of macOS Sonoma 14.7.8
- Security content of macOS Sonoma 14.7.8 Release of macOS Sequoia 15.6.1
- Security content of macOS Sequoia 15.6.1

Release Changes 2025.08.05 All AMIs
- Updated awscli to 2.28.0
- Updated Homebrew to 4.5.13 Release of macOS Ventura 13.7.7
- Security content of macOS Ventura 13.7.7
- Updated Safari to 18.6
- Security content of Safari 18.6 Release of macOS Sonoma 14.7.7
- Security content of macOS Sonoma 14.7.7
- Updated Safari to 18.6
- Security content of Safari 18.6 Release of macOS Sequoia 15.6
- Security content of macOS Sequoia 15.6
- Updated AWS ENA Ethernet to 2.0.0

Release Changes 2025.06.27 All AMIs
- Updated awscli to 2.27.40
- Updated Homebrew to 4.5.7
- Migrated x86_64 images to AWS ENA Ethernet dext Release of macOS Ventura 13.7.6
- Security content of macOS Ventura 13.7.6
- Updated Safari to 18.5
- Security content of Safari 18.5 Release of macOS Sonoma 14.7.6
- Security content of macOS Sonoma 14.7.6
- Updated Safari to 18.5
- Security content of Safari 18.5 Release of macOS Sequoia 15.5
- Security content of macOS Sequoia 15.5
- Updated Command Line Tools to 16.4
- Updated AWS ENA Ethernet to 1.0.9

Release Changes 2025.05.21 All AMIs
- Updated awscli to 2.27.7
- Updated ec2-macos-init  to 1.5.11
- Updated ec2-macos-utils  to 1.0.5
- Updated Homebrew to 4.5.1 Release of macOS Ventura 13.7.5
- Security content of macOS Ventura 13.7.5
- Updated Safari to 18.4
- Security content of Safari 18.4 Release of macOS Sonoma 14.7.5
- Security content of macOS Sonoma 14.7.5
- Updated Safari to 18.4
- Security content of Safari 18.4 Release of macOS Sequoia 15.4.1
- Security content of macOS Sequoia 15.4.1
- Updated Command Line Tools to 16.3

Release Changes 2025.05.05 All AMIs
- Updated awscli to 2.27.1
- Updated ec2-macos-init  to 1.5.11
- Updated ec2-macos-system-monitor to 1.3.1
- Updated ec2-macos-utils  to 1.0.5
- Updated Homebrew to 4.4.32 Release of macOS Ventura 13.7.5
- Security content of macOS Ventura 13.7.5
- Updated Safari to 18.4
- Security content of Safari 18.4 Release of macOS Sonoma 14.7.5
- Security content of macOS Sonoma 14.7.5
- Updated Safari to 18.4
- Security content of Safari 18.4 Release of macOS Sequoia 15.4.1
- Security content of macOS Sequoia 15.4.1

Release Changes 2025.03.18 All AMIs
- Updated awscli to 2.24.2
- Updated Homebrew to 4.4.20 Release of macOS Sequoia 15.3.1
- Security content of macOS Sequoia 15.3.1 Release of macOS Sonoma 14.7.4
- Security content of macOS Sonoma 14.7.4
- Updated Safari to 18.3 Release of macOS Ventura 13.7.4
- Security content of macOS Ventura 13.7.4
- Updated Safari to 18.3

Release Changes 2025.01.24 All AMIs
- Updated awscli to 2.22.33
- Updated Homebrew to 4.4.15 Release of macOS Sequoia 15.2
- Security content of macOS Sequoia 15.2
- Updated Command Line Tools to 16.2 Release of macOS Sonoma 14.7.2
- Security content of macOS Sonoma 14.7.2
- Updated Safari to 18.2
- Updated Command Line Tools to 16.2 Release of macOS Ventura 13.7.2
- Security content of macOS Ventura 13.7.2
- Updated Safari to 18.2

Release Changes 2024.12.20 All AMIs
- Updated Homebrew to 4.4.8
- Updated aws-cli to 2.22.5
- Updated amazon-ssm-agent  to 3.3.987.0 Release of macOS Sequoia 15.1.1
- Security content of macOS Sequoia 15.1.1 Release of macOS Sonoma 14.7.1
- Security content of macOS Sonoma 14.7.1
- Updated Safari to 18.1.1 Release of macOS Ventura 13.7.1
- Security content of macOS Ventura 13.7.1
- Updated Safari to 18.1.1

Release Changes 2024.10.28 All AMIs
- Updated Homebrew to 4.4.2
- Updated aws-cli to 2.18.13
- Updated amazon-ssm-agent  to 3.3.987.0
- Updated ec2-macos-init  to 1.5.10
- Updated ec2-macos-utils  to 1.0.4 Release of macOS Sequoia 15.0
- Security content of macOS Sequoia 15 Release of macOS Sonoma 14.7
- Security content of macOS Sonoma 14.7.
- Updated Command Line Tools to 16.0
- Updated Safari to 18.0.1
- Security content of Safari 18 Release of macOS Ventura 13.7
- Security content of macOS Ventura 13.7
- Updated Safari to 18.0.1
- Security content of Safari 18

Release Changes 2024.08.20 All AMIs
- Updated Homebrew to 4.3.14
- Updated aws-cli to 2.17.29 Release of macOS Sonoma 14.6.1
- No published CVE entries.
Release of macOS Ventura 13.6.9
- No published CVE entries.
- Updated Safari to 17.6
- Security content of Safari 17.6 Release of macOS Monterey 12.7.6
- Security content of macOS Monterey 12.7.6
- Updated Safari to 17.6
- Security content of Safari 17.6

Release Changes 2024.06.07 All AMIs
- Updated Homebrew to 4.3.1-1
- Updated aws-cli to 2.15.56
- Updated amazon-ssm-agent  to 3.3.380.0-1 Release of macOS Sonoma 14.5
- Security content of macOS Sonoma 14.5 Release of macOS Ventura 13.6.7
- Security content of macOS Ventura 13.6.7
- Updated Safari to 17.5
- Security content of Safari 17.5 Release of macOS Monterey 12.7.5
- Security content of macOS Monterey 12.7.5
- Updated Safari to 17.5
- Security content of Safari 17.5

Release Changes 2024.04.12 All AMIs
- Updated Homebrew to 4.2.16-1
- Updated aws-cli to 2.15.36 Release of macOS Sonoma 14.4.1
- Security content of macOS Sonoma 14.4.1 Release of macOS Ventura 13.6.6
- Security content of macOS Ventura 13.6.6
- Updated Safari to 17.4.1
- Security content of Safari 17.4.1 For macOS Monterey
- Updated Safari to 17.4.1
- Security content of Safari 17.4.1
## Amazon EBS-optimized instance types Amazon EBS–optimized instances use an optimized configuration stack and provide additional, dedicated bandwidth for Amazon EBS I/O. This optimization provides the best performance for your EBS volumes by minimizing contention between Amazon EBS I/O and other traffic from your instance.
When attached to an EBS–optimized instance, General Purpose SSD (gp2 and gp3) volumes are designed to deliver at least 90 percent of their provisioned IOPS performance 99 percent of the time in a given year, and Provisioned IOPS SSD (io1 and io2) volumes are designed to deliver at least 90 percent of their provisioned IOPS performance 99.9 percent of the time in a given year. Throughput Optimized HDD (st1) and Cold HDD (sc1) deliver at least 90 percent of their expected throughput performance 99 percent of the time in a given year. Non-compliant periods

are approximately uniformly distributed, targeting 99 percent of expected total throughput each hour. For more information, see Amazon EBS volume types in the Amazon EBS User Guide.
Some instance types are EBS-optimized by default, and there is no need to enable it and no effect if you attempt to disable it. Other instance types optionally support EBS optimization and you can enable it during or after launch for an  additional hourly fee. Some instance types do not support EBS optimization.
For detailed instance type specifications and features, see the Amazon EC2 Instance Types Guide.
Considerations
- An instance's EBS performance is bounded by the instance type's performance limits, or the aggregated performance of its attached volumes, whichever is smaller. To achieve maximum EBS performance, an instance must have attached volumes that provide a combined performance equal to or greater than the maximum instance performance. For example, to achieve 80,000 IOPS for r6i.16xlarge, the instance must have at least 5 gp2 volumes provisioned with 16,000 IOPS each (5 volumes x 16,000 IOPS = 80,000 IOPS), or it can have 1 gp3 volume provisioned with 80,000 IOPS. We recommend that you choose an instance type that provides more dedicated Amazon EBS throughput than your application needs; otherwise, the connection between Amazon EBS and Amazon EC2 can become a performance bottleneck.
- The maximum number of Amazon EBS volumes that you can attach to an instance depends on the instance type and instance size. For more information, see Amazon EBS volume limits for Amazon EC2 instances.
- The maximum IOPS and throughput limits are interdependent. Depending on your I/O size, you might reach one limit before the other, which can affect overall performance. For optimal results, consider both limits when planning your workload.
### EBS-optimized by default The following instance types are EBS–optimized by default. There is no need to enable EBS optimization and no effect if you disable EBS optimization.
Instances
- General purpose
- Compute optimized
- Memory optimized

- Storage optimized
- Accelerated computing
- High-performance computing
#### General purpose Note M8a, M8g, M8gd, M8i, M8id, M8i-flex instance types support configurable bandwidth weightings. With these instance types, you can optimize an instance's bandwidth for either networking performance or Amazon EBS performance. The following table shows the default Amazon EBS bandwidth performance for these instance types. For more information, see EC2 instance bandwidth weighting configuration.
Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) a1.medium 1 300 3500 37.50 437.50 2500 20000 a1.large 1 525 3500 65.62 437.50 4000 20000 a1.xlarge 1 800 3500 100.00 437.50 6000 20000 a1.2xlarge 1 1750 3500 218.75 437.50 10000 20000 a1.4xlarge 2 3500 437.5 20000 a1.metal 2 3500 437.5 20000 m4.large 2 450 56.25 3600

Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) m4.xlarge 2 750 93.75 6000 m4.2xlarg e 2 1000 125.0 8000 m4.4xlarg e 2 2000 250.0 16000 m4.10xlar ge 2 4000 500.0 32000 m4.16xlar ge 2 10000 1250.0 65000 m5.large 1 650 4750 81.25 593.75 3600 18750 m5.xlarge 1 1150 4750 143.75 593.75 6000 18750 m5.2xlarg e 1 2300 4750 287.50 593.75 12000 18750 m5.4xlarg e 2 4750 593.75 18750 m5.8xlarg e 2 6800 850.0 30000 m5.12xlar ge 2 9500 1187.5 40000

Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) m5.16xlar ge 2 13600 1700.0 60000 m5.24xlar ge 2 19000 2375.0 80000 m5.metal 2 19000 2375.0 80000 m5a.large 1 650 2880 81.25 360.00 3600 16000 m5a.xlarg e 1 1085 2880 135.62 360.00 6000 16000 m5a.2xlar ge 1 1580 2880 197.50 360.00 8333 16000 m5a.4xlar ge 2 2880 360.0 16000 m5a.8xlar ge 2 4750 593.75 20000 m5a.12xla rge 2 6780 847.5 30000 m5a.16xla rge 2 9500 1187.5 40000 m5a.24xla rge 2 13750 1718.75 60000

Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) m5ad.larg e 1 650 2880 81.25 360.00 3600 16000 m5ad.xlar ge 1 1085 2880 135.62 360.00 6000 16000 m5ad.2xla rge 1 1580 2880 197.50 360.00 8333 16000 m5ad.4xla rge 2 2880 360.0 16000 m5ad.8xla rge 2 4750 593.75 20000 m5ad.12xl arge 2 6780 847.5 30000 m5ad.16xl arge 2 9500 1187.5 40000 m5ad.24xl arge 2 13750 1718.75 60000 m5d.large 1 650 4750 81.25 593.75 3600 18750 m5d.xlarg e 1 1150 4750 143.75 593.75 6000 18750 m5d.2xlar ge 1 2300 4750 287.50 593.75 12000 18750

Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) m5d.4xlar ge 2 4750 593.75 18750 m5d.8xlar ge 2 6800 850.0 30000 m5d.12xla rge 2 9500 1187.5 40000 m5d.16xla rge 2 13600 1700.0 60000 m5d.24xla rge 2 19000 2375.0 80000 m5d.metal 2 19000 2375.0 80000 m5dn.larg e 1 650 4750 81.25 593.75 3600 18750 m5dn.xlar ge 1 1150 4750 143.75 593.75 6000 18750 m5dn.2xla rge 1 2300 4750 287.50 593.75 12000 18750 m5dn.4xla rge 2 4750 593.75 18750 m5dn.8xla rge 2 6800 850.0 30000

Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) m5dn.12xl arge 2 9500 1187.5 40000 m5dn.16xl arge 2 13600 1700.0 60000 m5dn.24xl arge 2 19000 2375.0 80000 m5dn.meta l 2 19000 2375.0 80000 m5n.large 1 650 4750 81.25 593.75 3600 18750 m5n.xlarg e 1 1150 4750 143.75 593.75 6000 18750 m5n.2xlar ge 1 2300 4750 287.50 593.75 12000 18750 m5n.4xlar ge 2 4750 593.75 18750 m5n.8xlar ge 2 6800 850.0 30000 m5n.12xla rge 2 9500 1187.5 40000 m5n.16xla rge 2 13600 1700.0 60000

Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) m5n.24xla rge 2 19000 2375.0 80000 m5n.metal 2 19000 2375.0 80000 m5zn.larg e 1 800 3170 100.00 396.25 3333 13333 m5zn.xlar ge 1 1564 3170 195.50 396.25 6667 13333 m5zn.2xla rge 2 3170 396.25 13333 m5zn.3xla rge 2 4750 593.75 20000 m5zn.6xla rge 2 9500 1187.5 40000 m5zn.12xl arge 2 19000 2375.0 80000 m5zn.meta l 2 19000 2375.0 80000 m6a.large 1 650 10000 81.25 1250.00 3600 40000 m6a.xlarg e 1 1250 10000 156.25 1250.00 6000 40000

Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) m6a.2xlar ge 1 2500 10000 312.50 1250.00 12000 40000 m6a.4xlar ge 1 5000 10000 625.00 1250.00 20000 40000 m6a.8xlar ge 2 10000 1250.0 40000 m6a.12xla rge 2 15000 1875.0 60000 m6a.16xla rge 2 20000 2500.0 80000 m6a.24xla rge 2 30000 3750.0 120000 m6a.32xla rge 2 40000 5000.0 160000 m6a.48xla rge 2 40000 5000.0 240000 m6a.metal 2 40000 5000.0 240000 m6g.mediu m 1 315 4750 39.38 593.75 2500 20000 m6g.large 1 630 4750 78.75 593.75 3600 20000

Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) m6g.xlarg e 1 1188 4750 148.50 593.75 6000 20000 m6g.2xlar ge 1 2375 4750 296.88 593.75 12000 20000 m6g.4xlar ge 2 4750 593.75 20000 m6g.8xlar ge 2 9500 1187.5 40000 m6g.12xla rge 2 14250 1781.25 50000 m6g.16xla rge 2 19000 2375.0 80000 m6g.metal 2 19000 2375.0 80000 m6gd.medi um 1 315 4750 39.38 593.75 2500 20000 m6gd.larg e 1 630 4750 78.75 593.75 3600 20000 m6gd.xlar ge 1 1188 4750 148.50 593.75 6000 20000 m6gd.2xla rge 1 2375 4750 296.88 593.75 12000 20000

Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) m6gd.4xla rge 2 4750 593.75 20000 m6gd.8xla rge 2 9500 1187.5 40000 m6gd.12xl arge 2 14250 1781.25 50000 m6gd.16xl arge 2 19000 2375.0 80000 m6gd.meta l 2 19000 2375.0 80000 m6i.large 1 650 10000 81.25 1250.00 3600 40000 m6i.xlarge 1 1250 10000 156.25 1250.00 6000 40000 m6i.2xlar ge 1 2500 10000 312.50 1250.00 12000 40000 m6i.4xlar ge 1 5000 10000 625.00 1250.00 20000 40000 m6i.8xlar ge 2 10000 1250.0 40000 m6i.12xla rge 2 15000 1875.0 60000

Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) m6i.16xla rge 2 20000 2500.0 80000 m6i.24xla rge 2 30000 3750.0 120000 m6i.32xla rge 2 40000 5000.0 160000 m6i.metal 2 40000 5000.0 160000 m6id.large 1 650 10000 81.25 1250.00 3600 40000 m6id.xlar ge 1 1250 10000 156.25 1250.00 6000 40000 m6id.2xla rge 1 2500 10000 312.50 1250.00 12000 40000 m6id.4xla rge 1 5000 10000 625.00 1250.00 20000 40000 m6id.8xla rge 2 10000 1250.0 40000 m6id.12xl arge 2 15000 1875.0 60000 m6id.16xl arge 2 20000 2500.0 80000

Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) m6id.24xl arge 2 30000 3750.0 120000 m6id.32xl arge 2 40000 5000.0 160000 m6id.meta l 2 40000 5000.0 160000 m6idn.lar ge 1 1562 25000 195.31 3125.00 6250 100000 m6idn.xla rge 1 3125 25000 390.62 3125.00 12500 100000 m6idn.2xl arge 1 6250 25000 781.25 3125.00 25000 100000 m6idn.4xl arge 1 12500 25000 1562.50 3125.00 50000 100000 m6idn.8xl arge 2 25000 3125.0 100000 m6idn.12x large 2 37500 4687.5 150000 m6idn.16x large 2 50000 6250.0 200000 m6idn.24x large 2 75000 9375.0 300000

Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) m6idn.32x large 2 100000 12500.0 400000 m6idn.met al 2 100000 12500.0 400000 m6in.large 1 1562 25000 195.31 3125.00 6250 100000 m6in.xlar ge 1 3125 25000 390.62 3125.00 12500 100000 m6in.2xla rge 1 6250 25000 781.25 3125.00 25000 100000 m6in.4xla rge 1 12500 25000 1562.50 3125.00 50000 100000 m6in.8xla rge 2 25000 3125.0 100000 m6in.12xl arge 2 37500 4687.5 150000 m6in.16xl arge 2 50000 6250.0 200000 m6in.24xl arge 2 75000 9375.0 300000 m6in.32xl arge 2 100000 12500.0 400000

Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) m6in.meta l 2 100000 12500.0 400000 m7a.mediu m 1 325 10000 40.62 1250.00 2500 40000 m7a.large 1 650 10000 81.25 1250.00 3600 40000 m7a.xlarg e 1 1250 10000 156.25 1250.00 6000 40000 m7a.2xlar ge 1 2500 10000 312.50 1250.00 12000 40000 m7a.4xlar ge 1 5000 10000 625.00 1250.00 20000 40000 m7a.8xlar ge 2 10000 1250.0 40000 m7a.12xla rge 2 15000 1875.0 60000 m7a.16xla rge 2 20000 2500.0 80000 m7a.24xla rge 2 30000 3750.0 120000 m7a.32xla rge 2 40000 5000.0 160000

Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) m7a.48xla rge 2 40000 5000.0 240000 m7a.metal -48xl 2 40000 5000.0 240000 m7g.mediu m 1 315 10000 39.38 1250.00 2500 40000 m7g.large 1 630 10000 78.75 1250.00 3600 40000 m7g.xlarg e 1 1250 10000 156.25 1250.00 6000 40000 m7g.2xlar ge 1 2500 10000 312.50 1250.00 12000 40000 m7g.4xlar ge 1 5000 10000 625.00 1250.00 20000 40000 m7g.8xlar ge 2 10000 1250.0 40000 m7g.12xla rge 2 15000 1875.0 60000 m7g.16xla rge 2 20000 2500.0 80000 m7g.metal 2 20000 2500.0 80000

Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) m7gd.medi um 1 315 10000 39.38 1250.00 2500 40000 m7gd.larg e 1 630 10000 78.75 1250.00 3600 40000 m7gd.xlar ge 1 1250 10000 156.25 1250.00 6000 40000 m7gd.2xla rge 1 2500 10000 312.50 1250.00 12000 40000 m7gd.4xla rge 1 5000 10000 625.00 1250.00 20000 40000 m7gd.8xla rge 2 10000 1250.0 40000 m7gd.12xl arge 2 15000 1875.0 60000 m7gd.16xl arge 2 20000 2500.0 80000 m7gd.meta l 2 20000 2500.0 80000 m7i.large 1 650 10000 81.25 1250.00 3600 40000 m7i.xlarge 1 1250 10000 156.25 1250.00 6000 40000

Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) m7i.2xlar ge 1 2500 10000 312.50 1250.00 12000 40000 m7i.4xlar ge 1 5000 10000 625.00 1250.00 20000 40000 m7i.8xlar ge 2 10000 1250.0 40000 m7i.12xla rge 2 15000 1875.0 60000 m7i.16xla rge 2 20000 2500.0 80000 m7i.24xla rge 2 30000 3750.0 120000 m7i.48xla rge 2 40000 5000.0 240000 m7i.metal -24xl 2 30000 3750.0 120000 m7i.metal -48xl 2 40000 5000.0 240000 m7i-flex. large 1 312 10000 39.06 1250.00 2500 40000 m7i-flex. xlarge 1 625 10000 78.12 1250.00 3600 40000

Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) m7i-flex.
2xlarge 1 1250 10000 156.25 1250.00 6000 40000 m7i-flex.
4xlarge 1 2500 10000 312.50 1250.00 12000 40000 m7i-flex.
8xlarge 1 5000 10000 625.00 1250.00 20000 40000 m7i-flex.
12xlarge 1 7500 15000 937.50 1875.00 30000 60000 m7i-flex.
16xlarge 1 10000 20000 1250.00 2500.00 40000 80000 m8a.mediu m 1 325 10000 40.62 1250.00 2500 40000 m8a.large 1 650 10000 81.25 1250.00 3600 40000 m8a.xlarg e 1 1250 10000 156.25 1250.00 6000 40000 m8a.2xlar ge 1 2500 10000 312.50 1250.00 12000 40000 m8a.4xlar ge 1 5000 10000 625.00 1250.00 20000 40000 m8a.8xlar ge 2 10000 1250.0 40000

Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) m8a.12xla rge 2 15000 1875.0 60000 m8a.16xla rge 2 20000 2500.0 80000 m8a.24xla rge 2 30000 3750.0 120000 m8a.48xla rge 2 60000 7500.0 240000 m8a.metal -24xl 2 30000 3750.0 120000 m8a.metal -48xl 2 60000 7500.0 240000 m8azn.med ium 1 625 15000 78.12 1875.00 2500 60000 m8azn.lar ge 1 1250 15000 156.25 1875.00 5000 60000 m8azn.xla rge 1 2500 15000 312.50 1875.00 10000 60000 m8azn.3xl arge 1 7500 15000 937.50 1875.00 30000 60000 m8azn.6xl arge 2 15000 1875.0 60000

Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) m8azn.12x large 2 30000 3750.0 120000 m8azn.24x large 2 60000 7500.0 240000 m8azn.met al-12xl 2 30000 3750.0 120000 m8azn.met al-24xl 2 60000 7500.0 240000 m8g.mediu m 1 315 10000 39.38 1250.00 2500 40000 m8g.large 1 630 10000 78.75 1250.00 3600 40000 m8g.xlarg e 1 1250 10000 156.25 1250.00 6000 40000 m8g.2xlar ge 1 2500 10000 312.50 1250.00 12000 40000 m8g.4xlar ge 1 5000 10000 625.00 1250.00 20000 40000 m8g.8xlar ge 2 10000 1250.0 40000 m8g.12xla rge 2 15000 1875.0 60000

Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) m8g.16xla rge 2 20000 2500.0 80000 m8g.24xla rge 2 30000 3750.0 120000 m8g.48xla rge 2 40000 5000.0 240000 m8g.metal -24xl 2 30000 3750.0 120000 m8g.metal -48xl 2 40000 5000.0 240000 m8gb.medi um 1 1562 25000 195.31 3125.00 7500 120000 m8gb.larg e 1 3125 25000 390.62 3125.00 15000 120000 m8gb.xlar ge 1 6250 25000 781.25 3125.00 30000 120000 m8gb.2xla rge 1 12500 25000 1562.50 3125.00 60000 120000 m8gb.4xla rge 2 25000 3125.0 120000 m8gb.8xla rge 2 50000 6250.0 240000

Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) m8gb.12xl arge 2 75000 9375.0 360000 m8gb.16xl arge 2 100000 12500.0 480000 m8gb.24xl arge 2 150000 18750.0 720000 m8gb.48xl arge 2 300000 37500.0 1440000 m8gd.medi um 1 315 10000 39.38 1250.00 2500 40000 m8gd.larg e 1 630 10000 78.75 1250.00 3600 40000 m8gd.xlar ge 1 1250 10000 156.25 1250.00 6000 40000 m8gd.2xla rge 1 2500 10000 312.50 1250.00 12000 40000 m8gd.4xla rge 1 5000 10000 625.00 1250.00 20000 40000 m8gd.8xla rge 2 10000 1250.0 40000 m8gd.12xl arge 2 15000 1875.0 60000

Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) m8gd.16xl arge 2 20000 2500.0 80000 m8gd.24xl arge 2 30000 3750.0 120000 m8gd.48xl arge 2 40000 5000.0 240000 m8gd.meta l-24xl 2 30000 3750.0 120000 m8gd.meta l-48xl 2 40000 5000.0 240000 m8gn.medi um 1 760 10000 95.00 1250.00 2500 40000 m8gn.larg e 1 1250 10000 156.25 1250.00 5000 40000 m8gn.xlar ge 1 2500 10000 312.50 1250.00 10000 40000 m8gn.2xla rge 1 5000 10000 625.00 1250.00 20000 40000 m8gn.4xla rge 2 10000 1250.0 40000 m8gn.8xla rge 2 20000 2500.0 80000

Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) m8gn.12xl arge 2 30000 3750.0 120000 m8gn.16xl arge 2 40000 5000.0 160000 m8gn.24xl arge 2 60000 7500.0 240000 m8gn.48xl arge 2 60000 7500.0 240000 m8i.large 1 650 10000 81.25 1250.00 3600 40000 m8i.xlarge 1 1250 10000 156.25 1250.00 6000 40000 m8i.2xlar ge 1 2500 10000 312.50 1250.00 12000 40000 m8i.4xlar ge 1 5000 10000 625.00 1250.00 20000 40000 m8i.8xlar ge 2 10000 1250.0 40000 m8i.12xla rge 2 15000 1875.0 60000 m8i.16xla rge 2 20000 2500.0 80000

Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) m8i.24xla rge 2 30000 3750.0 120000 m8i.32xla rge 2 40000 5000.0 160000 m8i.48xla rge 2 60000 7500.0 240000 m8i.96xla rge 2 80000 10000.0 480000 m8i.metal -48xl 2 60000 7500.0 240000 m8i.metal -96xl 2 80000 10000.0 480000 m8id.large 1 650 10000 81.25 1250.00 3600 40000 m8id.xlar ge 1 1250 10000 156.25 1250.00 6000 40000 m8id.2xla rge 1 2500 10000 312.50 1250.00 12000 40000 m8id.4xla rge 1 5000 10000 625.00 1250.00 20000 40000 m8id.8xla rge 2 10000 1250.0 40000

Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) m8id.12xl arge 2 15000 1875.0 60000 m8id.16xl arge 2 20000 2500.0 80000 m8id.24xl arge 2 30000 3750.0 120000 m8id.32xl arge 2 40000 5000.0 160000 m8id.48xl arge 2 60000 7500.0 240000 m8id.96xl arge 2 80000 10000.0 480000 m8id.meta l-48xl 2 60000 7500.0 240000 m8id.meta l-96xl 2 80000 10000.0 480000 m8i-flex. large 1 315 10000 39.38 1250.00 2500 40000 m8i-flex. xlarge 1 630 10000 78.75 1250.00 3600 40000 m8i-flex.
2xlarge 1 1250 10000 156.25 1250.00 6000 40000

Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) m8i-flex.
4xlarge 1 2500 10000 312.50 1250.00 12000 40000 m8i-flex.
8xlarge 1 5000 10000 625.00 1250.00 20000 40000 m8i-flex.
12xlarge 1 7500 15000 937.50 1875.00 30000 60000 m8i-flex.
16xlarge 1 10000 20000 1250.00 2500.00 40000 80000 mac1.meta l 2 14000 1750.0 80000 mac2.meta l 2 10000 1250.0 55000 mac2- m1ul tra.metal 2 10000 1250.0 55000 mac2- m2.metal 2 8000 1000.0 55000 mac2- m2pr o.metal 2 8000 1000.0 55000 mac- m4.metal 2 8000 1000.0 55000

Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) mac- m4pro .metal 2 8000 1000.0 55000 t3.nano 1 43 2085 5.38 260.62 250 11800 t3.micro 1 87 2085 10.88 260.62 500 11800 t3.small 1 174 2085 21.75 260.62 1000 11800 t3.medium 1 347 2085 43.38 260.62 2000 11800 t3.large 1 695 2780 86.88 347.50 4000 15700 t3.xlarge 1 695 2780 86.88 347.50 4000 15700 t3.2xlarge 1 695 2780 86.88 347.50 4000 15700 t3a.nano 1 45 2085 5.62 260.62 250 11800 t3a.micro 1 90 2085 11.25 260.62 500 11800 t3a.small 1 175 2085 21.88 260.62 1000 11800 t3a.mediu m 1 350 2085 43.75 260.62 2000 11800 t3a.large 1 695 2780 86.88 347.50 4000 15700 t3a.xlarge 1 695 2780 86.88 347.50 4000 15700

Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) t3a.2xlarge 1 695 2780 86.88 347.50 4000 15700 t4g.nano 1 43 2085 5.38 260.62 250 11800 t4g.micro 1 87 2085 10.88 260.62 500 11800 t4g.small 1 174 2085 21.75 260.62 1000 11800 t4g.mediu m 1 347 2085 43.38 260.62 2000 11800 t4g.large 1 695 2780 86.88 347.50 4000 15700 t4g.xlarge 1 695 2780 86.88 347.50 4000 15700 t4g.2xlar ge 1 695 2780 86.88 347.50 4000 15700 1 These instances can sustain the maximum performance for 30 minutes at least once every 24 hours, after which they revert to their baseline performance.
2 These instances can sustain their stated performance indefinitely. If your workload requires sustained maximum performance for longer than 30 minutes, use one of these instances.
#### Compute optimized Note C8a, C8g, C8gd, C8i, C8id, C8i-flex instance types support configurable bandwidth weightings. With these instance types, you can optimize an instance's bandwidth for either networking performance or Amazon EBS performance. The following table shows

the default Amazon EBS bandwidth performance for these instance types. For more information, see EC2 instance bandwidth weighting configuration.
Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) c4.large 2 500 62.5 4000 c4.xlarge 2 750 93.75 6000 c4.2xlarge 2 1000 125.0 8000 c4.4xlarge 2 2000 250.0 16000 c4.8xlarge 2 4000 500.0 32000 c5.large 1 650 4750 81.25 593.75 4000 20000 c5.xlarge 1 1150 4750 143.75 593.75 6000 20000 c5.2xlarge 1 2300 4750 287.50 593.75 10000 20000 c5.4xlarge 2 4750 593.75 20000 c5.9xlarge 2 9500 1187.5 40000 c5.12xlar ge 2 9500 1187.5 40000

Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) c5.18xlar ge 2 19000 2375.0 80000 c5.24xlar ge 2 19000 2375.0 80000 c5.metal 2 19000 2375.0 80000 c5a.large 1 200 3170 25.00 396.25 800 13300 c5a.xlarge 1 400 3170 50.00 396.25 1600 13300 c5a.2xlar ge 1 800 3170 100.00 396.25 3200 13300 c5a.4xlar ge 1 1580 3170 197.50 396.25 6600 13300 c5a.8xlar ge 2 3170 396.25 13300 c5a.12xla rge 2 4750 593.75 20000 c5a.16xla rge 2 6300 787.5 26700 c5a.24xla rge 2 9500 1187.5 40000 c5ad.large 1 200 3170 25.00 396.25 800 13300

Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) c5ad.xlar ge 1 400 3170 50.00 396.25 1600 13300 c5ad.2xla rge 1 800 3170 100.00 396.25 3200 13300 c5ad.4xla rge 1 1580 3170 197.50 396.25 6600 13300 c5ad.8xla rge 2 3170 396.25 13300 c5ad.12xl arge 2 4750 593.75 20000 c5ad.16xl arge 2 6300 787.5 26700 c5ad.24xl arge 2 9500 1187.5 40000 c5d.large 1 650 4750 81.25 593.75 4000 20000 c5d.xlarge 1 1150 4750 143.75 593.75 6000 20000 c5d.2xlar ge 1 2300 4750 287.50 593.75 10000 20000 c5d.4xlar ge 2 4750 593.75 20000

Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) c5d.9xlar ge 2 9500 1187.5 40000 c5d.12xla rge 2 9500 1187.5 40000 c5d.18xla rge 2 19000 2375.0 80000 c5d.24xla rge 2 19000 2375.0 80000 c5d.metal 2 19000 2375.0 80000 c5n.large 1 650 4750 81.25 593.75 4000 20000 c5n.xlarge 1 1150 4750 143.75 593.75 6000 20000 c5n.2xlar ge 1 2300 4750 287.50 593.75 10000 20000 c5n.4xlar ge 2 4750 593.75 20000 c5n.9xlar ge 2 9500 1187.5 40000 c5n.18xla rge 2 19000 2375.0 80000

Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) c5n.metal 2 19000 2375.0 80000 c6a.large 1 650 10000 81.25 1250.00 3600 40000 c6a.xlarge 1 1250 10000 156.25 1250.00 6000 40000 c6a.2xlar ge 1 2500 10000 312.50 1250.00 12000 40000 c6a.4xlar ge 1 5000 10000 625.00 1250.00 20000 40000 c6a.8xlar ge 2 10000 1250.0 40000 c6a.12xla rge 2 15000 1875.0 60000 c6a.16xla rge 2 20000 2500.0 80000 c6a.24xla rge 2 30000 3750.0 120000 c6a.32xla rge 2 40000 5000.0 160000 c6a.48xla rge 2 40000 5000.0 240000

Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) c6a.metal 2 40000 5000.0 240000 c6g.mediu m 1 315 4750 39.38 593.75 2500 20000 c6g.large 1 630 4750 78.75 593.75 3600 20000 c6g.xlarge 1 1188 4750 148.50 593.75 6000 20000 c6g.2xlar ge 1 2375 4750 296.88 593.75 12000 20000 c6g.4xlar ge 2 4750 593.75 20000 c6g.8xlar ge 2 9500 1187.5 40000 c6g.12xla rge 2 14250 1781.25 50000 c6g.16xla rge 2 19000 2375.0 80000 c6g.metal 2 19000 2375.0 80000 c6gd.medi um 1 315 4750 39.38 593.75 2500 20000

Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) c6gd.large 1 630 4750 78.75 593.75 3600 20000 c6gd.xlar ge 1 1188 4750 148.50 593.75 6000 20000 c6gd.2xla rge 1 2375 4750 296.88 593.75 12000 20000 c6gd.4xla rge 2 4750 593.75 20000 c6gd.8xla rge 2 9500 1187.5 40000 c6gd.12xl arge 2 14250 1781.25 50000 c6gd.16xl arge 2 19000 2375.0 80000 c6gd.meta l 2 19000 2375.0 80000 c6gn.medi um 1 760 9500 95.00 1187.50 2500 40000 c6gn.large 1 1235 9500 154.38 1187.50 5000 40000 c6gn.xlar ge 1 2375 9500 296.88 1187.50 10000 40000

Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) c6gn.2xla rge 1 4750 9500 593.75 1187.50 20000 40000 c6gn.4xla rge 2 9500 1187.5 40000 c6gn.8xla rge 2 19000 2375.0 80000 c6gn.12xl arge 2 28500 3562.5 120000 c6gn.16xl arge 2 38000 4750.0 160000 c6i.large 1 650 10000 81.25 1250.00 3600 40000 c6i.xlarge 1 1250 10000 156.25 1250.00 6000 40000 c6i.2xlarge 1 2500 10000 312.50 1250.00 12000 40000 c6i.4xlarge 1 5000 10000 625.00 1250.00 20000 40000 c6i.8xlarge 2 10000 1250.0 40000 c6i.12xla rge 2 15000 1875.0 60000 c6i.16xla rge 2 20000 2500.0 80000

Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) c6i.24xla rge 2 30000 3750.0 120000 c6i.32xla rge 2 40000 5000.0 160000 c6i.metal 2 40000 5000.0 160000 c6id.large 1 650 10000 81.25 1250.00 3600 40000 c6id.xlarge 1 1250 10000 156.25 1250.00 6000 40000 c6id.2xla rge 1 2500 10000 312.50 1250.00 12000 40000 c6id.4xla rge 1 5000 10000 625.00 1250.00 20000 40000 c6id.8xla rge 2 10000 1250.0 40000 c6id.12xl arge 2 15000 1875.0 60000 c6id.16xl arge 2 20000 2500.0 80000 c6id.24xl arge 2 30000 3750.0 120000 c6id.32xl arge 2 40000 5000.0 160000

Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) c6id.meta l 2 40000 5000.0 160000 c6in.large 1 1562 25000 195.31 3125.00 6250 100000 c6in.xlarge 1 3125 25000 390.62 3125.00 12500 100000 c6in.2xla rge 1 6250 25000 781.25 3125.00 25000 100000 c6in.4xla rge 1 12500 25000 1562.50 3125.00 50000 100000 c6in.8xla rge 2 25000 3125.0 100000 c6in.12xl arge 2 37500 4687.5 150000 c6in.16xl arge 2 50000 6250.0 200000 c6in.24xl arge 2 75000 9375.0 300000 c6in.32xl arge 2 100000 12500.0 400000 c6in.meta l 2 100000 12500.0 400000

Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) c7a.mediu m 1 325 10000 40.62 1250.00 2500 40000 c7a.large 1 650 10000 81.25 1250.00 3600 40000 c7a.xlarge 1 1250 10000 156.25 1250.00 6000 40000 c7a.2xlar ge 1 2500 10000 312.50 1250.00 12000 40000 c7a.4xlar ge 1 5000 10000 625.00 1250.00 20000 40000 c7a.8xlar ge 2 10000 1250.0 40000 c7a.12xla rge 2 15000 1875.0 60000 c7a.16xla rge 2 20000 2500.0 80000 c7a.24xla rge 2 30000 3750.0 120000 c7a.32xla rge 2 40000 5000.0 160000 c7a.48xla rge 2 40000 5000.0 240000

Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) c7a.metal -48xl 2 40000 5000.0 240000 c7g.mediu m 1 315 10000 39.38 1250.00 2500 40000 c7g.large 1 630 10000 78.75 1250.00 3600 40000 c7g.xlarge 1 1250 10000 156.25 1250.00 6000 40000 c7g.2xlar ge 1 2500 10000 312.50 1250.00 12000 40000 c7g.4xlar ge 1 5000 10000 625.00 1250.00 20000 40000 c7g.8xlar ge 2 10000 1250.0 40000 c7g.12xla rge 2 15000 1875.0 60000 c7g.16xla rge 2 20000 2500.0 80000 c7g.metal 2 20000 2500.0 80000 c7gd.medi um 1 315 10000 39.38 1250.00 2500 40000

Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) c7gd.large 1 630 10000 78.75 1250.00 3600 40000 c7gd.xlar ge 1 1250 10000 156.25 1250.00 6000 40000 c7gd.2xla rge 1 2500 10000 312.50 1250.00 12000 40000 c7gd.4xla rge 1 5000 10000 625.00 1250.00 20000 40000 c7gd.8xla rge 2 10000 1250.0 40000 c7gd.12xl arge 2 15000 1875.0 60000 c7gd.16xl arge 2 20000 2500.0 80000 c7gd.meta l 2 20000 2500.0 80000 c7gn.medi um 1 521 10000 65.12 1250.00 2083 40000 c7gn.large 1 1042 10000 130.25 1250.00 4167 40000 c7gn.xlar ge 1 2083 10000 260.38 1250.00 8333 40000

Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) c7gn.2xla rge 1 4167 10000 520.88 1250.00 16667 40000 c7gn.4xla rge 1 8333 10000 1041.62 1250.00 33333 40000 c7gn.8xla rge 1 16667 20000 2083.38 2500.00 66667 80000 c7gn.12xl arge 1 25000 30000 3125.00 3750.00 100000 120000 c7gn.16xl arge 1 33333 40000 4166.62 5000.00 133333 160000 c7gn.meta l 1 33333 40000 4166.62 5000.00 133333 160000 c7i.large 1 650 10000 81.25 1250.00 3600 40000 c7i.xlarge 1 1250 10000 156.25 1250.00 6000 40000 c7i.2xlarge 1 2500 10000 312.50 1250.00 12000 40000 c7i.4xlarge 1 5000 10000 625.00 1250.00 20000 40000 c7i.8xlarge 2 10000 1250.0 40000 c7i.12xla rge 2 15000 1875.0 60000

Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) c7i.16xla rge 2 20000 2500.0 80000 c7i.24xla rge 2 30000 3750.0 120000 c7i.48xla rge 2 40000 5000.0 240000 c7i.metal -24xl 2 30000 3750.0 120000 c7i.metal -48xl 2 40000 5000.0 240000 c7i-flex. large 1 312 10000 39.06 1250.00 2500 40000 c7i-flex. xlarge 1 625 10000 78.12 1250.00 3600 40000 c7i-flex.
2xlarge 1 1250 10000 156.25 1250.00 6000 40000 c7i-flex.
4xlarge 1 2500 10000 312.50 1250.00 12000 40000 c7i-flex.
8xlarge 1 5000 10000 625.00 1250.00 20000 40000 c7i-flex.
12xlarge 1 7500 15000 937.50 1875.00 30000 60000

Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) c7i-flex.
16xlarge 1 10000 20000 1250.00 2500.00 40000 80000 c8a.mediu m 1 325 10000 40.62 1250.00 2500 40000 c8a.large 1 650 10000 81.25 1250.00 3600 40000 c8a.xlarge 1 1250 10000 156.25 1250.00 6000 40000 c8a.2xlar ge 1 2500 10000 312.50 1250.00 12000 40000 c8a.4xlar ge 1 5000 10000 625.00 1250.00 20000 40000 c8a.8xlar ge 2 10000 1250.0 40000 c8a.12xla rge 2 15000 1875.0 60000 c8a.16xla rge 2 20000 2500.0 80000 c8a.24xla rge 2 30000 3750.0 120000 c8a.48xla rge 2 60000 7500.0 240000

Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) c8a.metal -24xl 2 30000 3750.0 120000 c8a.metal -48xl 2 60000 7500.0 240000 c8g.mediu m 1 315 10000 39.38 1250.00 2500 40000 c8g.large 1 630 10000 78.75 1250.00 3600 40000 c8g.xlarge 1 1250 10000 156.25 1250.00 6000 40000 c8g.2xlar ge 1 2500 10000 312.50 1250.00 12000 40000 c8g.4xlar ge 1 5000 10000 625.00 1250.00 20000 40000 c8g.8xlar ge 2 10000 1250.0 40000 c8g.12xla rge 2 15000 1875.0 60000 c8g.16xla rge 2 20000 2500.0 80000 c8g.24xla rge 2 30000 3750.0 120000

Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) c8g.48xla rge 2 40000 5000.0 240000 c8g.metal -24xl 2 30000 3750.0 120000 c8g.metal -48xl 2 40000 5000.0 240000 c8gb.medi um 1 1562 25000 195.31 3125.00 7500 120000 c8gb.large 1 3125 25000 390.62 3125.00 15000 120000 c8gb.xlar ge 1 6250 25000 781.25 3125.00 30000 120000 c8gb.2xla rge 1 12500 25000 1562.50 3125.00 60000 120000 c8gb.4xla rge 2 25000 3125.0 120000 c8gb.8xla rge 2 50000 6250.0 240000 c8gb.12xl arge 2 75000 9375.0 360000 c8gb.16xl arge 2 100000 12500.0 480000

Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) c8gb.24xl arge 2 150000 18750.0 720000 c8gb.48xl arge 2 300000 37500.0 1440000 c8gb.meta l-24xl 2 150000 18750.0 720000 c8gb.meta l-48xl 2 300000 37500.0 1440000 c8gd.medi um 1 315 10000 39.38 1250.00 2500 40000 c8gd.large 1 630 10000 78.75 1250.00 3600 40000 c8gd.xlar ge 1 1250 10000 156.25 1250.00 6000 40000 c8gd.2xla rge 1 2500 10000 312.50 1250.00 12000 40000 c8gd.4xla rge 1 5000 10000 625.00 1250.00 20000 40000 c8gd.8xla rge 2 10000 1250.0 40000 c8gd.12xl arge 2 15000 1875.0 60000

Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) c8gd.16xl arge 2 20000 2500.0 80000 c8gd.24xl arge 2 30000 3750.0 120000 c8gd.48xl arge 2 40000 5000.0 240000 c8gd.meta l-24xl 2 30000 3750.0 120000 c8gd.meta l-48xl 2 40000 5000.0 240000 c8gn.medi um 1 760 10000 95.00 1250.00 2500 40000 c8gn.large 1 1250 10000 156.25 1250.00 5000 40000 c8gn.xlar ge 1 2500 10000 312.50 1250.00 10000 40000 c8gn.2xla rge 1 5000 10000 625.00 1250.00 20000 40000 c8gn.4xla rge 2 10000 1250.0 40000 c8gn.8xla rge 2 20000 2500.0 80000

Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) c8gn.12xl arge 2 30000 3750.0 120000 c8gn.16xl arge 2 40000 5000.0 160000 c8gn.24xl arge 2 60000 7500.0 240000 c8gn.48xl arge 2 60000 7500.0 240000 c8gn.meta l-24xl 2 60000 7500.0 240000 c8gn.meta l-48xl 2 60000 7500.0 240000 c8i.large 1 650 10000 81.25 1250.00 3600 40000 c8i.xlarge 1 1250 10000 156.25 1250.00 6000 40000 c8i.2xlarge 1 2500 10000 312.50 1250.00 12000 40000 c8i.4xlarge 1 5000 10000 625.00 1250.00 20000 40000 c8i.8xlarge 2 10000 1250.0 40000 c8i.12xla rge 2 15000 1875.0 60000

Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) c8i.16xla rge 2 20000 2500.0 80000 c8i.24xla rge 2 30000 3750.0 120000 c8i.32xla rge 2 40000 5000.0 160000 c8i.48xla rge 2 60000 7500.0 240000 c8i.96xla rge 2 80000 10000.0 480000 c8i.metal -48xl 2 60000 7500.0 240000 c8i.metal -96xl 2 80000 10000.0 480000 c8id.large 1 650 10000 81.25 1250.00 3600 40000 c8id.xlarge 1 1250 10000 156.25 1250.00 6000 40000 c8id.2xla rge 1 2500 10000 312.50 1250.00 12000 40000 c8id.4xla rge 1 5000 10000 625.00 1250.00 20000 40000

Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) c8id.8xla rge 2 10000 1250.0 40000 c8id.12xl arge 2 15000 1875.0 60000 c8id.16xl arge 2 20000 2500.0 80000 c8id.24xl arge 2 30000 3750.0 120000 c8id.32xl arge 2 40000 5000.0 160000 c8id.48xl arge 2 60000 7500.0 240000 c8id.96xl arge 2 80000 10000.0 480000 c8id.meta l-48xl 2 60000 7500.0 240000 c8id.meta l-96xl 2 80000 10000.0 480000 c8i-flex. large 1 315 10000 39.38 1250.00 2500 40000 c8i-flex. xlarge 1 630 10000 78.75 1250.00 3600 40000

Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) c8i-flex.
2xlarge 1 1250 10000 156.25 1250.00 6000 40000 c8i-flex.
4xlarge 1 2500 10000 312.50 1250.00 12000 40000 c8i-flex.
8xlarge 1 5000 10000 625.00 1250.00 20000 40000 c8i-flex.
12xlarge 1 7500 15000 937.50 1875.00 30000 60000 c8i-flex.
16xlarge 1 10000 20000 1250.00 2500.00 40000 80000 1 These instances can sustain the maximum performance for 30 minutes at least once every 24 hours, after which they revert to their baseline performance.
2 These instances can sustain their stated performance indefinitely. If your workload requires sustained maximum performance for longer than 30 minutes, use one of these instances.
#### Memory optimized Note
- R8a, R8g, R8gd, R8i, R8id, R8i-flex, X8g, X8aedz, X8i instance types support configurable bandwidth weightings. With these instance types, you can optimize an instance's bandwidth for either networking performance or Amazon EBS performance. The following table shows the default Amazon EBS bandwidth performance for these instance types. For more information, see EC2 instance bandwidth weighting configuration.

- For maximum IOPS performance with U7i instances, we recommend that you use io2 BlockExpress volumes.
Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) r4.large 2 425 53.125 3000 r4.xlarge 2 850 106.25 6000 r4.2xlarge 2 1700 212.5 12000 r4.4xlarge 2 3500 437.5 18750 r4.8xlarge 2 7000 875.0 37500 r4.16xlar ge 2 14000 1750.0 75000 r5.large 1 650 4750 81.25 593.75 3600 18750 r5.xlarge 1 1150 4750 143.75 593.75 6000 18750 r5.2xlarge 1 2300 4750 287.50 593.75 12000 18750 r5.4xlarge 2 4750 593.75 18750 r5.8xlarge 2 6800 850.0 30000

Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) r5.12xlar ge 2 9500 1187.5 40000 r5.16xlar ge 2 13600 1700.0 60000 r5.24xlar ge 2 19000 2375.0 80000 r5.metal 2 19000 2375.0 80000 r5a.large 1 650 2880 81.25 360.00 3600 16000 r5a.xlarge 1 1085 2880 135.62 360.00 6000 16000 r5a.2xlarge 1 1580 2880 197.50 360.00 8333 16000 r5a.4xlarge 2 2880 360.0 16000 r5a.8xlarge 2 4750 593.75 20000 r5a.12xla rge 2 6780 847.5 30000 r5a.16xla rge 2 9500 1187.5 40000 r5a.24xla rge 2 13570 1696.25 60000

Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) r5ad.large 1 650 2880 81.25 360.00 3600 16000 r5ad.xlarge 1 1085 2880 135.62 360.00 6000 16000 r5ad.2xla rge 1 1580 2880 197.50 360.00 8333 16000 r5ad.4xla rge 2 2880 360.0 16000 r5ad.8xla rge 2 4750 593.75 20000 r5ad.12xl arge 2 6780 847.5 30000 r5ad.16xl arge 2 9500 1187.5 40000 r5ad.24xl arge 2 13570 1696.25 60000 r5b.large 1 1250 10000 156.25 1250.00 5417 43333 r5b.xlarge 1 2500 10000 312.50 1250.00 10833 43333 r5b.2xlar ge 1 5000 10000 625.00 1250.00 21667 43333

Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) r5b.4xlar ge 2 10000 1250.0 43333 r5b.8xlar ge 2 20000 2500.0 86667 r5b.12xla rge 2 30000 3750.0 130000 r5b.16xla rge 2 40000 5000.0 173333 r5b.24xla rge 2 60000 7500.0 260000 r5b.metal 2 60000 7500.0 260000 r5d.large 1 650 4750 81.25 593.75 3600 18750 r5d.xlarge 1 1150 4750 143.75 593.75 6000 18750 r5d.2xlar ge 1 2300 4750 287.50 593.75 12000 18750 r5d.4xlar ge 2 4750 593.75 18750 r5d.8xlar ge 2 6800 850.0 30000 r5d.12xla rge 2 9500 1187.5 40000

Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) r5d.16xla rge 2 13600 1700.0 60000 r5d.24xla rge 2 19000 2375.0 80000 r5d.metal 2 19000 2375.0 80000 r5dn.large 1 650 4750 81.25 593.75 3600 18750 r5dn.xlar ge 1 1150 4750 143.75 593.75 6000 18750 r5dn.2xla rge 1 2300 4750 287.50 593.75 12000 18750 r5dn.4xla rge 2 4750 593.75 18750 r5dn.8xla rge 2 6800 850.0 30000 r5dn.12xl arge 2 9500 1187.5 40000 r5dn.16xl arge 2 13600 1700.0 60000 r5dn.24xl arge 2 19000 2375.0 80000

Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) r5dn.meta l 2 19000 2375.0 80000 r5n.large 1 650 4750 81.25 593.75 3600 18750 r5n.xlarge 1 1150 4750 143.75 593.75 6000 18750 r5n.2xlar ge 1 2300 4750 287.50 593.75 12000 18750 r5n.4xlar ge 2 4750 593.75 18750 r5n.8xlar ge 2 6800 850.0 30000 r5n.12xla rge 2 9500 1187.5 40000 r5n.16xla rge 2 13600 1700.0 60000 r5n.24xla rge 2 19000 2375.0 80000 r5n.metal 2 19000 2375.0 80000 r6a.large 1 650 10000 81.25 1250.00 3600 40000 r6a.xlarge 1 1250 10000 156.25 1250.00 6000 40000

Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) r6a.2xlarge 1 2500 10000 312.50 1250.00 12000 40000 r6a.4xlarge 1 5000 10000 625.00 1250.00 20000 40000 r6a.8xlarge 2 10000 1250.0 40000 r6a.12xla rge 2 15000 1875.0 60000 r6a.16xla rge 2 20000 2500.0 80000 r6a.24xla rge 2 30000 3750.0 120000 r6a.32xla rge 2 40000 5000.0 160000 r6a.48xla rge 2 40000 5000.0 240000 r6a.metal 2 40000 5000.0 240000 r6g.mediu m 1 315 4750 39.38 593.75 2500 20000 r6g.large 1 630 4750 78.75 593.75 3600 20000 r6g.xlarge 1 1188 4750 148.50 593.75 6000 20000

Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) r6g.2xlar ge 1 2375 4750 296.88 593.75 12000 20000 r6g.4xlar ge 2 4750 593.75 20000 r6g.8xlar ge 2 9500 1187.5 40000 r6g.12xla rge 2 14250 1781.25 50000 r6g.16xla rge 2 19000 2375.0 80000 r6g.metal 2 19000 2375.0 80000 r6gd.medi um 1 315 4750 39.38 593.75 2500 20000 r6gd.large 1 630 4750 78.75 593.75 3600 20000 r6gd.xlar ge 1 1188 4750 148.50 593.75 6000 20000 r6gd.2xla rge 1 2375 4750 296.88 593.75 12000 20000 r6gd.4xla rge 2 4750 593.75 20000

Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) r6gd.8xla rge 2 9500 1187.5 40000 r6gd.12xl arge 2 14250 1781.25 50000 r6gd.16xl arge 2 19000 2375.0 80000 r6gd.meta l 2 19000 2375.0 80000 r6i.large 1 650 10000 81.25 1250.00 3600 40000 r6i.xlarge 1 1250 10000 156.25 1250.00 6000 40000 r6i.2xlarge 1 2500 10000 312.50 1250.00 12000 40000 r6i.4xlarge 1 5000 10000 625.00 1250.00 20000 40000 r6i.8xlarge 2 10000 1250.0 40000 r6i.12xla rge 2 15000 1875.0 60000 r6i.16xla rge 2 20000 2500.0 80000 r6i.24xla rge 2 30000 3750.0 120000

Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) r6i.32xla rge 2 40000 5000.0 160000 r6i.metal 2 40000 5000.0 160000 r6id.large 1 650 10000 81.25 1250.00 3600 40000 r6id.xlarge 1 1250 10000 156.25 1250.00 6000 40000 r6id.2xla rge 1 2500 10000 312.50 1250.00 12000 40000 r6id.4xla rge 1 5000 10000 625.00 1250.00 20000 40000 r6id.8xla rge 2 10000 1250.0 40000 r6id.12xl arge 2 15000 1875.0 60000 r6id.16xl arge 2 20000 2500.0 80000 r6id.24xl arge 2 30000 3750.0 120000 r6id.32xl arge 2 40000 5000.0 160000 r6id.metal 2 40000 5000.0 160000

Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) r6idn.large 1 1562 25000 195.31 3125.00 6250 100000 r6idn.xla rge 1 3125 25000 390.62 3125.00 12500 100000 r6idn.2xl arge 1 6250 25000 781.25 3125.00 25000 100000 r6idn.4xl arge 1 12500 25000 1562.50 3125.00 50000 100000 r6idn.8xl arge 2 25000 3125.0 100000 r6idn.12x large 2 37500 4687.5 150000 r6idn.16x large 2 50000 6250.0 200000 r6idn.24x large 2 75000 9375.0 300000 r6idn.32x large 2 100000 12500.0 400000 r6idn.met al 2 100000 12500.0 400000 r6in.large 1 1562 25000 195.31 3125.00 6250 100000

Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) r6in.xlarge 1 3125 25000 390.62 3125.00 12500 100000 r6in.2xla rge 1 6250 25000 781.25 3125.00 25000 100000 r6in.4xla rge 1 12500 25000 1562.50 3125.00 50000 100000 r6in.8xla rge 2 25000 3125.0 100000 r6in.12xl arge 2 37500 4687.5 150000 r6in.16xl arge 2 50000 6250.0 200000 r6in.24xl arge 2 75000 9375.0 300000 r6in.32xl arge 2 100000 12500.0 400000 r6in.metal 2 100000 12500.0 400000 r7a.mediu m 1 325 10000 40.62 1250.00 2500 40000 r7a.large 1 650 10000 81.25 1250.00 3600 40000

Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) r7a.xlarge 1 1250 10000 156.25 1250.00 6000 40000 r7a.2xlarge 1 2500 10000 312.50 1250.00 12000 40000 r7a.4xlarge 1 5000 10000 625.00 1250.00 20000 40000 r7a.8xlarge 2 10000 1250.0 40000 r7a.12xla rge 2 15000 1875.0 60000 r7a.16xla rge 2 20000 2500.0 80000 r7a.24xla rge 2 30000 3750.0 120000 r7a.32xla rge 2 40000 5000.0 160000 r7a.48xla rge 2 40000 5000.0 240000 r7a.metal -48xl 2 40000 5000.0 240000 r7g.mediu m 1 315 10000 39.38 1250.00 2500 40000

Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) r7g.large 1 630 10000 78.75 1250.00 3600 40000 r7g.xlarge 1 1250 10000 156.25 1250.00 6000 40000 r7g.2xlar ge 1 2500 10000 312.50 1250.00 12000 40000 r7g.4xlar ge 1 5000 10000 625.00 1250.00 20000 40000 r7g.8xlar ge 2 10000 1250.0 40000 r7g.12xla rge 2 15000 1875.0 60000 r7g.16xla rge 2 20000 2500.0 80000 r7g.metal 2 20000 2500.0 80000 r7gd.medi um 1 315 10000 39.38 1250.00 2500 40000 r7gd.large 1 630 10000 78.75 1250.00 3600 40000 r7gd.xlar ge 1 1250 10000 156.25 1250.00 6000 40000 r7gd.2xla rge 1 2500 10000 312.50 1250.00 12000 40000

Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) r7gd.4xla rge 1 5000 10000 625.00 1250.00 20000 40000 r7gd.8xla rge 2 10000 1250.0 40000 r7gd.12xl arge 2 15000 1875.0 60000 r7gd.16xl arge 2 20000 2500.0 80000 r7gd.meta l 2 20000 2500.0 80000 r7i.large 1 650 10000 81.25 1250.00 3600 40000 r7i.xlarge 1 1250 10000 156.25 1250.00 6000 40000 r7i.2xlarge 1 2500 10000 312.50 1250.00 12000 40000 r7i.4xlarge 1 5000 10000 625.00 1250.00 20000 40000 r7i.8xlarge 2 10000 1250.0 40000 r7i.12xla rge 2 15000 1875.0 60000 r7i.16xla rge 2 20000 2500.0 80000

Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) r7i.24xla rge 2 30000 3750.0 120000 r7i.48xla rge 2 40000 5000.0 240000 r7i.metal -24xl 2 30000 3750.0 120000 r7i.metal -48xl 2 40000 5000.0 240000 r7iz.large 1 792 10000 99.00 1250.00 3600 40000 r7iz.xlarge 1 1584 10000 198.00 1250.00 6667 40000 r7iz.2xla rge 1 3168 10000 396.00 1250.00 13333 40000 r7iz.4xla rge 1 5000 10000 625.00 1250.00 20000 40000 r7iz.8xla rge 2 10000 1250.0 40000 r7iz.12xl arge 2 19000 2375.0 76000 r7iz.16xl arge 2 20000 2500.0 80000

Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) r7iz.32xl arge 2 40000 5000.0 160000 r7iz.meta l-16xl 2 20000 2500.0 80000 r7iz.meta l-32xl 2 40000 5000.0 160000 r8a.mediu m 1 325 10000 40.62 1250.00 2500 40000 r8a.large 1 650 10000 81.25 1250.00 3600 40000 r8a.xlarge 1 1250 10000 156.25 1250.00 6000 40000 r8a.2xlarge 1 2500 10000 312.50 1250.00 12000 40000 r8a.4xlarge 1 5000 10000 625.00 1250.00 20000 40000 r8a.8xlarge 2 10000 1250.0 40000 r8a.12xla rge 2 15000 1875.0 60000 r8a.16xla rge 2 20000 2500.0 80000

Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) r8a.24xla rge 2 30000 3750.0 120000 r8a.48xla rge 2 60000 7500.0 240000 r8a.metal -24xl 2 30000 3750.0 120000 r8a.metal -48xl 2 60000 7500.0 240000 r8g.mediu m 1 315 10000 39.38 1250.00 2500 40000 r8g.large 1 630 10000 78.75 1250.00 3600 40000 r8g.xlarge 1 1250 10000 156.25 1250.00 6000 40000 r8g.2xlar ge 1 2500 10000 312.50 1250.00 12000 40000 r8g.4xlar ge 1 5000 10000 625.00 1250.00 20000 40000 r8g.8xlar ge 2 10000 1250.0 40000 r8g.12xla rge 2 15000 1875.0 60000

Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) r8g.16xla rge 2 20000 2500.0 80000 r8g.24xla rge 2 30000 3750.0 120000 r8g.48xla rge 2 40000 5000.0 240000 r8g.metal -24xl 2 30000 3750.0 120000 r8g.metal -48xl 2 40000 5000.0 240000 r8gb.medi um 1 1562 25000 195.31 3125.00 7500 120000 r8gb.large 1 3125 25000 390.62 3125.00 15000 120000 r8gb.xlar ge 1 6250 25000 781.25 3125.00 30000 120000 r8gb.2xla rge 1 12500 25000 1562.50 3125.00 60000 120000 r8gb.4xla rge 2 25000 3125.0 120000 r8gb.8xla rge 2 50000 6250.0 240000

Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) r8gb.12xl arge 2 75000 9375.0 360000 r8gb.16xl arge 2 100000 12500.0 480000 r8gb.24xl arge 2 150000 18750.0 720000 r8gb.48xl arge 2 300000 37500.0 1440000 r8gb.meta l-24xl 2 150000 18750.0 720000 r8gb.meta l-48xl 2 300000 37500.0 1440000 r8gd.medi um 1 315 10000 39.38 1250.00 2500 40000 r8gd.large 1 630 10000 78.75 1250.00 3600 40000 r8gd.xlar ge 1 1250 10000 156.25 1250.00 6000 40000 r8gd.2xla rge 1 2500 10000 312.50 1250.00 12000 40000 r8gd.4xla rge 1 5000 10000 625.00 1250.00 20000 40000

Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) r8gd.8xla rge 2 10000 1250.0 40000 r8gd.12xl arge 2 15000 1875.0 60000 r8gd.16xl arge 2 20000 2500.0 80000 r8gd.24xl arge 2 30000 3750.0 120000 r8gd.48xl arge 2 40000 5000.0 240000 r8gd.meta l-24xl 2 30000 3750.0 120000 r8gd.meta l-48xl 2 40000 5000.0 240000 r8gn.medi um 1 760 10000 95.00 1250.00 2500 40000 r8gn.large 1 1250 10000 156.25 1250.00 5000 40000 r8gn.xlar ge 1 2500 10000 312.50 1250.00 10000 40000 r8gn.2xla rge 1 5000 10000 625.00 1250.00 20000 40000

Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) r8gn.4xla rge 2 10000 1250.0 40000 r8gn.8xla rge 2 20000 2500.0 80000 r8gn.12xl arge 2 30000 3750.0 120000 r8gn.16xl arge 2 40000 5000.0 160000 r8gn.24xl arge 2 60000 7500.0 240000 r8gn.48xl arge 2 60000 7500.0 240000 r8gn.meta l-24xl 2 60000 7500.0 240000 r8gn.meta l-48xl 2 60000 7500.0 240000 r8i.large 1 650 10000 81.25 1250.00 3600 40000 r8i.xlarge 1 1250 10000 156.25 1250.00 6000 40000 r8i.2xlarge 1 2500 10000 312.50 1250.00 12000 40000 r8i.4xlarge 1 5000 10000 625.00 1250.00 20000 40000

Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) r8i.8xlarge 2 10000 1250.0 40000 r8i.12xla rge 2 15000 1875.0 60000 r8i.16xla rge 2 20000 2500.0 80000 r8i.24xla rge 2 30000 3750.0 120000 r8i.32xla rge 2 40000 5000.0 160000 r8i.48xla rge 2 60000 7500.0 240000 r8i.96xla rge 2 80000 10000.0 480000 r8i.metal -48xl 2 60000 7500.0 240000 r8i.metal -96xl 2 80000 10000.0 480000 r8id.large 1 650 10000 81.25 1250.00 3600 40000 r8id.xlarge 1 1250 10000 156.25 1250.00 6000 40000

Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) r8id.2xla rge 1 2500 10000 312.50 1250.00 12000 40000 r8id.4xla rge 1 5000 10000 625.00 1250.00 20000 40000 r8id.8xla rge 2 10000 1250.0 40000 r8id.12xl arge 2 15000 1875.0 60000 r8id.16xl arge 2 20000 2500.0 80000 r8id.24xl arge 2 30000 3750.0 120000 r8id.32xl arge 2 40000 5000.0 160000 r8id.48xl arge 2 60000 7500.0 240000 r8id.96xl arge 2 80000 10000.0 480000 r8id.meta l-48xl 2 60000 7500.0 240000 r8id.meta l-96xl 2 80000 10000.0 480000

Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) r8i-flex. large 1 315 10000 39.38 1250.00 2500 40000 r8i-flex. xlarge 1 630 10000 78.75 1250.00 3600 40000 r8i-flex.
2xlarge 1 1250 10000 156.25 1250.00 6000 40000 r8i-flex.
4xlarge 1 2500 10000 312.50 1250.00 12000 40000 r8i-flex.
8xlarge 1 5000 10000 625.00 1250.00 20000 40000 r8i-flex.
12xlarge 1 7500 15000 937.50 1875.00 30000 60000 r8i-flex.
16xlarge 1 10000 20000 1250.00 2500.00 40000 80000 u-3tb1.56 xlarge 2 19000 2375.0 80000 u-6tb1.56 xlarge 2 38000 4750.0 160000 u-6tb1.11 2xlarge 2 38000 4750.0 160000 u-6tb1.me tal 2 38000 4750.0 160000

Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) u-9tb1.11 2xlarge 2 38000 4750.0 160000 u-9tb1.me tal 2 38000 4750.0 160000 u-12tb1.1 12xlarge 2 38000 4750.0 160000 u-12tb1.m etal 2 38000 4750.0 160000 u-18tb1.1 12xlarge 2 38000 4750.0 160000 u-18tb1.m etal 2 38000 4750.0 160000 u-24tb1.1 12xlarge 2 38000 4750.0 160000 u-24tb1.m etal 2 38000 4750.0 160000 u7i-6tb.1 12xlarge 2 100000 12500.0 560000 u7i-8tb.1 12xlarge 2 100000 12500.0 560000 u7i-12tb.
224xlarge 2 100000 12500.0 560000

Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) u7in-16tb .224xlarge 2 100000 12500.0 560000 u7in-24tb .224xlarge 2 100000 12500.0 560000 u7in-32tb .224xlarge 2 100000 12500.0 560000 u7inh-32t b.480xlar ge 2 160000 20000.0 840000 x1.16xlar ge 2 7000 875.0 40000 x1.32xlar ge 2 14000 1750.0 80000 x1e.xlarge 2 500 62.5 3700 x1e.2xlar ge 2 1000 125.0 7400 x1e.4xlar ge 2 1750 218.75 10000 x1e.8xlar ge 2 3500 437.5 20000

Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) x1e.16xla rge 2 7000 875.0 40000 x1e.32xla rge 2 14000 1750.0 80000 x2gd.medi um 1 315 4750 39.38 593.75 2500 20000 x2gd.large 1 630 4750 78.75 593.75 3600 20000 x2gd.xlar ge 1 1188 4750 148.50 593.75 6000 20000 x2gd.2xla rge 1 2375 4750 296.88 593.75 12000 20000 x2gd.4xla rge 2 4750 593.75 20000 x2gd.8xla rge 2 9500 1187.5 40000 x2gd.12xl arge 2 14250 1781.25 60000 x2gd.16xl arge 2 19000 2375.0 80000 x2gd.meta l 2 19000 2375.0 80000

Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) x2idn.16x large 2 40000 5000.0 173333 x2idn.24x large 2 60000 7500.0 260000 x2idn.32x large 2 80000 10000.0 260000 x2idn.met al 2 80000 10000.0 260000 x2iedn.xl arge 1 2500 20000 312.50 2500.00 8125 65000 x2iedn.2x large 1 5000 20000 625.00 2500.00 16250 65000 x2iedn.4x large 1 10000 20000 1250.00 2500.00 32500 65000 x2iedn.8x large 2 20000 2500.0 65000 x2iedn.16 xlarge 2 40000 5000.0 130000 x2iedn.24 xlarge 2 60000 7500.0 195000 x2iedn.32 xlarge 2 80000 10000.0 260000

Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) x2iedn.me tal 2 80000 10000.0 260000 x2iezn.2x large 2 3170 396.25 13333 x2iezn.4x large 2 4750 593.75 20000 x2iezn.6x large 2 9500 1187.5 40000 x2iezn.8x large 2 12000 1500.0 55000 x2iezn.12 xlarge 2 19000 2375.0 80000 x2iezn.me tal 2 19000 2375.0 80000 x8g.mediu m 1 315 10000 39.38 1250.00 2500 40000 x8g.large 1 630 10000 78.75 1250.00 3600 40000 x8g.xlarge 1 1250 10000 156.25 1250.00 6000 40000 x8g.2xlar ge 1 2500 10000 312.50 1250.00 12000 40000

Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) x8g.4xlar ge 1 5000 10000 625.00 1250.00 20000 40000 x8g.8xlar ge 2 10000 1250.0 40000 x8g.12xla rge 2 15000 1875.0 60000 x8g.16xla rge 2 20000 2500.0 80000 x8g.24xla rge 2 30000 3750.0 120000 x8g.48xla rge 2 40000 5000.0 240000 x8g.metal -24xl 2 30000 3750.0 120000 x8g.metal -48xl 2 40000 5000.0 240000 x8aedz.la rge 1 1250 15000 156.25 1875.00 5000 60000 x8aedz.xl arge 1 2500 15000 312.50 1875.00 10000 60000 x8aedz.3x large 1 7500 15000 937.50 1875.00 30000 60000

Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) x8aedz.6x large 2 15000 1875.0 60000 x8aedz.12 xlarge 2 30000 3750.0 120000 x8aedz.24 xlarge 2 60000 7500.0 240000 x8aedz.me tal-12xl 2 30000 3750.0 120000 x8aedz.me tal-24xl 2 60000 7500.0 240000 x8i.large 1 650 10000 81.25 1250.00 3600 40000 x8i.xlarge 1 1250 10000 156.25 1250.00 6000 40000 x8i.2xlarge 1 2500 10000 312.50 1250.00 12000 40000 x8i.4xlarge 1 5000 10000 625.00 1250.00 20000 40000 x8i.8xlarge 2 10000 1250.0 40000 x8i.12xla rge 2 15000 1875.0 60000 x8i.16xla rge 2 20000 2500.0 80000

Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) x8i.24xla rge 2 30000 3750.0 120000 x8i.32xla rge 2 40000 5000.0 160000 x8i.48xla rge 2 60000 7500.0 240000 x8i.64xla rge 2 70000 8750.0 320000 x8i.96xla rge 2 80000 10000.0 480000 x8i.metal -48xl 2 60000 7500.0 240000 x8i.metal -96xl 2 80000 10000.0 480000 z1d.large 1 800 3170 100.00 396.25 3333 13333 z1d.xlarge 1 1580 3170 197.50 396.25 6667 13333 z1d.2xlar ge 2 3170 396.25 13333 z1d.3xlar ge 2 4750 593.75 20000

Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) z1d.6xlar ge 2 9500 1187.5 40000 z1d.12xla rge 2 19000 2375.0 80000 z1d.metal 2 19000 2375.0 80000 1 These instances can sustain the maximum performance for 30 minutes at least once every 24 hours, after which they revert to their baseline performance.
2 These instances can sustain their stated performance indefinitely. If your workload requires sustained maximum performance for longer than 30 minutes, use one of these instances.
#### Storage optimized Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) d2.xlarge 2 750 93.75 6000 d2.2xlarge 2 1000 125.0 8000 d2.4xlarge 2 2000 250.0 16000

Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) d2.8xlarge 2 4000 500.0 32000 d3.xlarge 1 850 2800 106.25 350.00 5000 15000 d3.2xlarge 1 1700 2800 212.50 350.00 10000 15000 d3.4xlarge 2 2800 350.0 15000 d3.8xlarge 2 5000 625.0 30000 d3en.xlar ge 1 850 2800 106.25 350.00 5000 15000 d3en.2xla rge 1 1700 2800 212.50 350.00 10000 15000 d3en.4xla rge 2 2800 350.0 15000 d3en.6xla rge 2 4000 500.0 25000 d3en.8xla rge 2 5000 625.0 30000 d3en.12xl arge 2 7000 875.0 40000

Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) h1.2xlarge 2 1750 218.75 12000 h1.4xlarge 2 3500 437.5 20000 h1.8xlarge 2 7000 875.0 40000 h1.16xlar ge 2 14000 1750.0 80000 i3.large 2 425 53.125 3000 i3.xlarge 2 850 106.25 6000 i3.2xlarge 2 1700 212.5 12000 i3.4xlarge 2 3500 437.5 16000 i3.8xlarge 2 7000 875.0 32500 i3.16xlarge 2 14000 1750.0 65000 i3.metal 2 19000 2375.0 80000 i3en.large 1 576 4750 72.10 593.75 3000 20000

Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) i3en.xlarge 1 1153 4750 144.20 593.75 6000 20000 i3en.2xla rge 1 2307 4750 288.39 593.75 12000 20000 i3en.3xla rge 1 3800 4750 475.00 593.75 15000 20000 i3en.6xla rge 2 4750 593.75 20000 i3en.12xl arge 2 9500 1187.5 40000 i3en.24xl arge 2 19000 2375.0 80000 i3en.meta l 2 19000 2375.0 80000 i4g.large 1 625 10000 78.12 1250.00 2500 40000 i4g.xlarge 1 1250 10000 156.25 1250.00 5000 40000 i4g.2xlarge 1 2500 10000 312.50 1250.00 10000 40000 i4g.4xlarge 1 5000 10000 625.00 1250.00 20000 40000 i4g.8xlarge 2 10000 1250.0 40000

Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) i4g.16xla rge 2 20000 2500.0 80000 i4i.large 1 625 10000 78.12 1250.00 2500 40000 i4i.xlarge 1 1250 10000 156.25 1250.00 5000 40000 i4i.2xlarge 1 2500 10000 312.50 1250.00 10000 40000 i4i.4xlarge 1 5000 10000 625.00 1250.00 20000 40000 i4i.8xlarge 2 10000 1250.0 40000 i4i.12xla rge 2 15000 1875.0 60000 i4i.16xla rge 2 20000 2500.0 80000 i4i.24xla rge 2 30000 3750.0 120000 i4i.32xla rge 2 40000 5000.0 160000 i4i.metal 2 40000 5000.0 160000 i7i.large 1 625 10000 78.12 1250.00 2500 40000 i7i.xlarge 1 1250 10000 156.25 1250.00 5000 40000

Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) i7i.2xlarge 1 2500 10000 312.50 1250.00 10000 40000 i7i.4xlarge 1 5000 10000 625.00 1250.00 20000 40000 i7i.8xlarge 2 10000 1250.0 40000 i7i.12xla rge 2 15000 1875.0 60000 i7i.16xla rge 2 20000 2500.0 80000 i7i.24xla rge 2 30000 3750.0 120000 i7i.48xla rge 2 60000 7500.0 240000 i7i.metal -24xl 2 30000 3750.0 120000 i7i.metal -48xl 2 60000 7500.0 240000 i7ie.large 1 625 10000 78.12 1250.00 2500 40000 i7ie.xlarge 1 1250 10000 156.25 1250.00 5000 40000

Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) i7ie.2xla rge 1 2500 10000 312.50 1250.00 10000 40000 i7ie.3xla rge 1 3750 10000 468.75 1250.00 15000 40000 i7ie.6xla rge 1 7500 10000 937.50 1250.00 30000 40000 i7ie.12xl arge 2 15000 1875.0 60000 i7ie.18xl arge 2 22500 2812.5 90000 i7ie.24xl arge 2 30000 3750.0 120000 i7ie.48xl arge 2 60000 7500.0 240000 i7ie.meta l-24xl 2 30000 3750.0 120000 i7ie.meta l-48xl 2 60000 7500.0 240000 i8g.large 1 625 10000 78.12 1250.00 2500 40000 i8g.xlarge 1 1250 10000 156.25 1250.00 5000 40000 i8g.2xlarge 1 2500 10000 312.50 1250.00 10000 40000

Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) i8g.4xlarge 1 5000 10000 625.00 1250.00 20000 40000 i8g.8xlarge 2 10000 1250.0 40000 i8g.12xla rge 2 15000 1875.0 60000 i8g.16xla rge 2 20000 2500.0 80000 i8g.24xla rge 2 30000 3750.0 120000 i8g.48xla rge 2 60000 7500.0 240000 i8g.metal -24xl 2 30000 3750.0 120000 i8ge.large 1 625 10000 78.12 1250.00 2500 40000 i8ge.xlarge 1 1250 10000 156.25 1250.00 5000 40000 i8ge.2xla rge 1 2500 10000 312.50 1250.00 10000 40000 i8ge.3xla rge 1 3750 10000 468.75 1250.00 15000 40000

Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) i8ge.6xla rge 1 7500 10000 937.50 1250.00 30000 40000 i8ge.12xl arge 2 15000 1875.0 60000 i8ge.18xl arge 2 22500 2812.5 90000 i8ge.24xl arge 2 30000 3750.0 120000 i8ge.48xl arge 2 60000 7500.0 240000 i8ge.meta l-24xl 2 30000 3750.0 120000 i8ge.meta l-48xl 2 60000 7500.0 240000 im4gn.lar ge 1 1250 10000 156.25 1250.00 5000 40000 im4gn.xla rge 1 2500 10000 312.50 1250.00 10000 40000 im4gn.2xl arge 1 5000 10000 625.00 1250.00 20000 40000 im4gn.4xl arge 2 10000 1250.0 40000

Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) im4gn.8xl arge 2 20000 2500.0 80000 im4gn.16x large 2 40000 5000.0 160000 is4gen.me dium 1 625 10000 78.12 1250.00 2500 40000 is4gen.la rge 1 1250 10000 156.25 1250.00 5000 40000 is4gen.xl arge 1 2500 10000 312.50 1250.00 10000 40000 is4gen.2x large 1 5000 10000 625.00 1250.00 20000 40000 is4gen.4x large 2 10000 1250.0 40000 is4gen.8x large 2 20000 2500.0 80000 1 These instances can sustain the maximum performance for 30 minutes at least once every 24 hours, after which they revert to their baseline performance.
2 These instances can sustain their stated performance indefinitely. If your workload requires sustained maximum performance for longer than 30 minutes, use one of these instances.

#### Accelerated computing Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) dl1.24xla rge 2 19000 2375.0 80000 dl2q.24xl arge 2 19000 2375.0 80000 f1.2xlarge 2 1700 212.5 12000 f1.4xlarge 2 3500 437.5 44000 f1.16xlar ge 2 14000 1750.0 75000 f2.6xlarge 2 7500 937.5 30000 f2.12xlar ge 2 15000 1875.0 60000 f2.48xlar ge 2 60000 7500.0 240000 g3.4xlarge 2 3500 437.5 20000 g3.8xlarge 2 7000 875.0 40000

Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) g3.16xlar ge 2 14000 1750.0 80000 g4ad.xlar ge 1 400 3170 50.00 396.25 1700 13333 g4ad.2xla rge 1 800 3170 100.00 396.25 3400 13333 g4ad.4xla rge 1 1580 3170 197.50 396.25 6700 13333 g4ad.8xla rge 2 3170 396.25 13333 g4ad.16xl arge 2 6300 787.5 26667 g4dn.xlar ge 1 950 3500 118.75 437.50 3000 20000 g4dn.2xla rge 1 1150 3500 143.75 437.50 6000 20000 g4dn.4xla rge 2 4750 593.75 20000 g4dn.8xla rge 2 9500 1187.5 40000 g4dn.12xl arge 2 9500 1187.5 40000

Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) g4dn.16xl arge 2 9500 1187.5 40000 g4dn.meta l 2 19000 2375.0 80000 g5.xlarge 1 700 3500 87.50 437.50 3000 15000 g5.2xlarge 1 850 3500 106.25 437.50 3500 15000 g5.4xlarge 2 4750 593.75 20000 g5.8xlarge 2 16000 2000.0 65000 g5.12xlar ge 2 16000 2000.0 65000 g5.16xlar ge 2 16000 2000.0 65000 g5.24xlar ge 2 19000 2375.0 80000 g5.48xlar ge 2 19000 2375.0 80000 g5g.xlarge 1 1188 4750 148.50 593.75 6000 20000

Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) g5g.2xlar ge 1 2375 4750 296.88 593.75 12000 20000 g5g.4xlar ge 2 4750 593.75 20000 g5g.8xlar ge 2 9500 1187.5 40000 g5g.16xla rge 2 19000 2375.0 80000 g5g.metal 2 19000 2375.0 80000 g6.xlarge 1 1000 5000 125.00 625.00 4000 20000 g6.2xlarge 1 2000 5000 250.00 625.00 8000 20000 g6.4xlarge 2 8000 1000.0 32000 g6.8xlarge 2 16000 2000.0 64000 g6.12xlar ge 2 20000 2500.0 80000 g6.16xlar ge 2 20000 2500.0 80000

Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) g6.24xlar ge 2 30000 3750.0 120000 g6.48xlar ge 2 60000 7500.0 240000 g6e.xlarge 1 1000 5000 125.00 625.00 4000 20000 g6e.2xlar ge 1 2000 5000 250.00 625.00 8000 20000 g6e.4xlar ge 2 8000 1000.0 32000 g6e.8xlar ge 2 16000 2000.0 64000 g6e.12xla rge 2 20000 2500.0 80000 g6e.16xla rge 2 20000 2500.0 80000 g6e.24xla rge 2 30000 3750.0 120000 g6e.48xla rge 2 60000 7500.0 240000 g6f.large 1 936 5000 117.00 625.00 3750 20000

Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) g6f.xlarge 1 1000 5000 125.00 625.00 4000 20000 g6f.2xlarge 1 2000 5000 250.00 625.00 8000 20000 g6f.4xlarge 2 6000 750.0 24000 gr6.4xlar ge 2 8000 1000.0 32000 gr6.8xlar ge 2 16000 2000.0 64000 gr6f.4xla rge 2 8000 1000.0 32000 g7e.2xlar ge 1 2000 5000 250.00 625.00 8000 20000 g7e.4xlar ge 2 8000 1000.0 32000 g7e.8xlar ge 2 16000 2000.0 64000 g7e.12xla rge 2 25000 3125.0 100000 g7e.24xla rge 2 50000 6250.0 200000

Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) g7e.48xla rge 2 100000 12500.0 400000 inf1.xlarge 1 1190 4750 148.75 593.75 4000 20000 inf1.2xla rge 1 1190 4750 148.75 593.75 6000 20000 inf1.6xla rge 2 4750 593.75 20000 inf1.24xl arge 2 19000 2375.0 80000 inf2.xlarge 1 1250 10000 156.25 1250.00 6000 40000 inf2.8xla rge 2 10000 1250.0 40000 inf2.24xl arge 2 30000 3750.0 120000 inf2.48xl arge 2 60000 7500.0 240000 p3.2xlarge 2 1750 218.75 10000 p3.8xlarge 2 7000 875.0 40000

Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) p3.16xlar ge 2 14000 1750.0 80000 p3dn.24xl arge 2 19000 2375.0 80000 p4d.24xla rge 2 19000 2375.0 80000 p4de.24xl arge 2 19000 2375.0 80000 p5.4xlarge 2 10000 1250.0 32500 p5.48xlar ge 2 80000 10000.0 260000 p5e.48xla rge 2 80000 10000.0 260000 p5en.48xl arge 2 100000 12500.0 400000 p6-b200.4 8xlarge 2 100000 12500.0 400000 p6-b300.4 8xlarge 2 100000 12500.0 400000 p6e-gb200 .36xlarge 2 60000 7500.0 240000

Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) trn1.2xla rge 1 5000 20000 625.00 2500.00 16250 65000 trn1.32xl arge 2 80000 10000.0 260000 trn1n.32x large 2 80000 10000.0 260000 trn2.3xla rge 2 5000 625.0 16250 trn2.48xl arge 2 80000 10000.0 260000 trn2u.48x large 2 80000 10000.0 260000 vt1.3xlarge 1 2375 4750 296.88 593.75 10000 20000 vt1.6xlarge 2 4750 593.75 20000 vt1.24xla rge 2 19000 2375.0 80000 1 These instances can sustain the maximum performance for 30 minutes at least once every 24 hours, after which they revert to their baseline performance.
2 These instances can sustain their stated performance indefinitely. If your workload requires sustained maximum performance for longer than 30 minutes, use one of these instances.

#### High-performance computing Instance size Baseline bandwidth (Mbps)
Maximum bandwidth (Mbps)
Baseline throughpu t (MB/s, 128 KiB I/ O)
Maximum throughpu t (MB/s, 128 KiB I/ O)
Baseline IOPS (16 KiB I/O)
Maximum IOPS (16 KiB I/O) hpc6a.48x large 1 87 2085 10.88 260.62 500 11000 hpc6id.32 xlarge 1 87 2085 10.88 260.62 500 11000 hpc7a.12x large 1 87 2085 10.88 260.62 500 11000 hpc7a.24x large 1 87 2085 10.88 260.62 500 11000 hpc7a.48x large 1 87 2085 10.88 260.62 500 11000 hpc7a.96x large 1 87 2085 10.88 260.62 500 11000 hpc7g.4xl arge 1 87 2085 10.88 260.62 500 11000 hpc7g.8xl arge 1 87 2085 10.88 260.62 500 11000 hpc7g.16x large 1 87 2085 10.88 260.62 500 11000 hpc8a.96x large 1 87 2085 10.88 260.62 500 11000

1 These instances can sustain the maximum performance for 30 minutes at least once every 24 hours, after which they revert to their baseline performance.
2 These instances can sustain their stated performance indefinitely. If your workload requires sustained maximum performance for longer than 30 minutes, use one of these instances.
### EBS optimization supported The following instance types support EBS optimization but EBS optimization is not enabled by default. You must enable EBS optimization, at an additional hourly fee, during or after launch to achieve the level of EBS performance described.
Instance size Maximum bandwidth (Mbps)
Maximum throughpu t (MB/s, 128 KiB I/O)
Maximum IOPS (16 KiB I/O) c1.xlarge 1000 125.0 8000 c3.xlarge 500 62.5 4000 c3.2xlarge 1000 125.0 8000 c3.4xlarge 2000 250.0 16000 i2.xlarge 500 62.5 4000 i2.2xlarge 1000 125.0 8000 i2.4xlarge 2000 250.0 16000 m1.large 500 62.5 4000 m1.xlarge 1000 125.0 8000 m2.2xlarge 500 62.5 4000 m2.4xlarge 1000 125.0 8000 m3.xlarge 500 62.5 4000 m3.2xlarge 1000 125.0 8000

Instance size Maximum bandwidth (Mbps)
Maximum throughpu t (MB/s, 128 KiB I/O)
Maximum IOPS (16 KiB I/O) r3.xlarge 500 62.5 4000 r3.2xlarge 1000 125.0 8000 r3.4xlarge 2000 250.0 16000 Note The i2.8xlarge, c3.8xlarge, and r3.8xlarge instances do not have dedicated EBS bandwidth and therefore do not offer EBS optimization. On these instances, network traffic and Amazon EBS traffic share the same 10-gigabit network interface.
### Get the maximum Amazon EBS optimized performance An instance's EBS performance is bounded by the instance type's performance limits, or the aggregated performance of its attached volumes, whichever is smaller. To achieve maximum EBS performance, an instance must have attached volumes that provide a combined performance equal to or greater than the maximum instance performance. For example, to achieve 80,000 IOPS for r6i.16xlarge, the instance must have at least 5 gp2 volumes provisioned with 16,000 IOPS each (5 volumes x 16,000 IOPS = 80,000 IOPS), or it can have 1 gp3 volume provisioned with 80,000 IOPS. We recommend that you choose an instance type that provides more dedicated Amazon EBS throughput than your application needs; otherwise, the connection between Amazon EBS and Amazon EC2 can become a performance bottleneck.
Important When using configurable bandwidth weightings, the EBS bandwidth limits for your instance might change. For instances with the VPC-1 weighting configuration, which increases networking bandwidth, you might experience lower than expected IOPS for EBS volumes due to reaching the EBS bandwidth limit before the IOPS limit. This is particularly noticeable with larger I/O sizes. Always test your specific workload to ensure it meets your performance requirements with your selected bandwidth weighting. For more information, see EC2 instance bandwidth weighting configuration.

You can use the EBSIOBalance% and EBSByteBalance% metrics to help you determine whether your instances are sized correctly. You can view these metrics in the CloudWatch console and set an alarm that is triggered based on a threshold you specify. These metrics are expressed as a percentage. Instances with a consistently low balance percentage are candidates to size up.
Instances where the balance percentage never drops below 100% are candidates for downsizing.
For more information, see Monitor your instances using CloudWatch.
The high memory instances are designed to run large in-memory databases, including production deployments of the SAP HANA in-memory database, in the cloud. To maximize EBS performance, use high memory instances with an even number of io1 or io2 volumes with identical provisioned performance. For example, for IOPS heavy workloads, use four io1 or io2 volumes with 40,000 provisioned IOPS to get the maximum 160,000 instance IOPS. Similarly, for throughput heavy workloads, use six io1 or io2 volumes with 48,000 provisioned IOPS to get the maximum 4,750 MB/s throughput. For additional recommendations, see Storage Configuration for SAP HANA.
Considerations
- G4dn, I3en, Inf1, M5a, M5ad, R5a, R5ad, T3, T3a, and Z1d instances launched after February 26, 2020 provide the maximum EBS optimized performance. To get the maximum performance from an instance launched before February 26, 2020, stop and start it.
- C5, C5d, C5n, M5, M5d, M5n, M5dn, R5, R5d, R5n, R5dn, and P3dn instances launched after December 3, 2019 provide the maximum EBS optimized performance. To get the maximum performance from an instance launched before December 3, 2019, stop and start it.
- u-6tb1.metal, u-9tb1.metal, and u-12tb1.metal instances launched after March 12, 2020 provide the maximum EBS optimized performance. Instances of these types launched before March 12, 2020 might provide lower performance. To get the maximum performance from an instance launched before March 12, 2020, contact your account team to upgrade the instance at no additional cost.
### Find EBS-optimized EC2 instance types You can view the instances types that support EBS optimization in each Region.
Console To find instance types that are EBS-optimized by default
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.

2. In the navigation pane, choose Instance Types.
3. Add the filter EBS optimization support = default.
4. (Optional) Click the Preferences icon and then turn on the relevant columns, such as EBS Maximum IOPS and EBS Baseline IOPS.
5. (Optional) Add filters to further scope to specific instance types of interest.
AWS CLI To find instance types that are EBS-optimized by default Use the following  describe-instance-types command. aws ec2 describe-instance-types \ --filters Name=ebs-info.ebs-optimized-support,Values=default  \ --query 'InstanceTypes[].{InstanceType:InstanceType, "MaxBandwidth(Mb/s)":EbsInfo.EbsOptimizedInfo.MaximumBandwidthInMbps, MaxIOPS:EbsInfo.EbsOptimizedInfo.MaximumIops, "MaxThroughput(MB/ s)":EbsInfo.EbsOptimizedInfo.MaximumThroughputInMBps}' \ --output=table To find instance types that optionally support EBS optimization Use the following describe-instance-types command. aws ec2 describe-instance-types \ --filters Name=ebs-info.ebs-optimized-support,Values=supported \ --query 'InstanceTypes[].{InstanceType:InstanceType, "MaxBandwidth(Mb/s)":EbsInfo.EbsOptimizedInfo.MaximumBandwidthInMbps, MaxIOPS:EbsInfo.EbsOptimizedInfo.MaximumIops, "MaxThroughput(MB/ s)":EbsInfo.EbsOptimizedInfo.MaximumThroughputInMBps}' \ --output=table The following is example output for eu-west-1.
--------------------------------------------------------------------------
|                         DescribeInstanceTypes                          | +--------------+----------------------+----------+-----------------------+
| InstanceType | MaxBandwidth(Mb/s)   | MaxIOPS  |  MaxThroughput(MB/s)  | +--------------+----------------------+----------+-----------------------+

|  i2.2xlarge  |  1000                |  8000    |  125.0                |
|  m2.4xlarge  |  1000                |  8000    |  125.0                |
|  m2.2xlarge  |  500                 |  4000    |  62.5                 |
|  c1.xlarge   |  1000                |  8000    |  125.0                |
|  i2.xlarge   |  500                 |  4000    |  62.5                 |
|  m3.xlarge   |  500                 |  4000    |  62.5                 |
|  m1.xlarge   |  1000                |  8000    |  125.0                |
|  r3.4xlarge  |  2000                |  16000   |  250.0                |
|  r3.2xlarge  |  1000                |  8000    |  125.0                |
|  c3.xlarge   |  500                 |  4000    |  62.5                 |
|  m3.2xlarge  |  1000                |  8000    |  125.0                |
|  r3.xlarge   |  500                 |  4000    |  62.5                 |
|  i2.4xlarge  |  2000                |  16000   |  250.0                |
|  c3.4xlarge  |  2000                |  16000   |  250.0                |
|  c3.2xlarge  |  1000                |  8000    |  125.0                |
|  m1.large    |  500                 |  4000    |  62.5                 | +--------------+----------------------+----------+-----------------------+ PowerShell To find instance types that are EBS-optimized by default Use the Get-EC2InstanceType cmdlet.
Get-EC2InstanceType `
    -Filter @{Name="ebs-info.ebs-optimized-support"; Values="default"} | `
    Select InstanceType, `
        @{Name="MaxBandwidth(Mb/s)"; Expression={($_.EbsInfo.EbsOptimizedInfo.MaximumBandwidthInMbps)}}, `
        @{Name="MaxIOPS"; Expression={($_.EbsInfo.EbsOptimizedInfo.MaximumIops)}}, `
        @{Name="MaxThroughput (MB/s)"; Expression={($_.EbsInfo.EbsOptimizedInfo.MaximumThroughputInMBps)}} To find instance types that optionally support EBS optimization Use the Get-EC2InstanceType cmdlet.
Get-EC2InstanceType `
    -Filter @{Name="ebs-info.ebs-optimized-support"; Values="supported"} | `
    Select InstanceType, `
        @{Name="MaxBandwidth(Mb/s)"; Expression={($_.EbsInfo.EbsOptimizedInfo.MaximumBandwidthInMbps)}}, `
        @{Name="MaxIOPS"; Expression={($_.EbsInfo.EbsOptimizedInfo.MaximumIops)}}, `

        @{Name="MaxThroughput (MB/s)"; Expression={($_.EbsInfo.EbsOptimizedInfo.MaximumThroughputInMBps)}} The following is example output for eu-west-1.
InstanceType MaxBandwidth(Mb/s) MaxIOPS MaxThroughput (MB/s)
------------ ------------------ ------- -------------------- m2.4xlarge                 1000    8000              125.000 i2.2xlarge                 1000    8000              125.000 c1.xlarge                  1000    8000              125.000 m2.2xlarge                  500    4000               62.500 r3.2xlarge                 1000    8000              125.000 m3.xlarge                   500    4000               62.500 r3.4xlarge                 2000   16000              250.000 m1.xlarge                  1000    8000              125.000 i2.xlarge                   500    4000               62.500 c3.xlarge                   500    4000               62.500 c3.4xlarge                 2000   16000              250.000 c3.2xlarge                 1000    8000              125.000 i2.4xlarge                 2000   16000              250.000 r3.xlarge                   500    4000               62.500 m3.2xlarge                 1000    8000              125.000 m1.large                    500    4000               62.500
### Enable EBS optimization for an Amazon EC2 instance You can manually enable EBS optimization only for previous generation instances types that optionally support EBS optimization. If you enable EBS optimization for these instance types, there is additional hourly fee Prerequisites
- Verify that the instance type requires that you enable EBS optimization. For more information, see EBS optimization supported.
- To you enable EBS optimization after launch, you must stop the instance.
Warning When you stop an instance, the data on any instance store volumes is erased. To keep data from instance store volumes, be sure to back it up to persistent storage.

Console To enable Amazon EBS optimization during launch In the Launch instances wizard, select the required instance type. Expand the Advanced details section, then for EBS-optimized instance, select Enable.
If the selected instance type does not support Amazon EBS optimization, the drop-down is disabled. If the instance type is Amazon EBS-optimized by default, Enable is already selected.
To enable Amazon EBS optimization after launch
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Instances, and select the instance.
3. Stop the instance. Choose Actions, Instance state, Stop instance.
4. With the instance still selected, choose Actions, Instance settings, Change instance type.
5. Select EBS-optimized and then choose Apply.
If the instance type is Amazon EBS-optimized by default, or if it does not support Amazon EBS optimization, the checkbox is disabled.
6. Restart the instance. Choose Instance state, Start instance.
AWS CLI To enable Amazon EBS optimization during launch Use the run-instances command with the --ebs-optimized option.
To enable Amazon EBS optimization after launch
1. If the instance is running, stop it by using the stop-instances command. aws ec2 stop-instances --instance-ids i-1234567890abcdef0
2. Enable EBS optimization by using the modify-instance-attribute command with the -- ebs-optimized option. aws ec2 modify-instance-attribute \ --instance-id i-1234567890abcdef0 \

    --ebs-optimized PowerShell To enable Amazon EBS optimization during launch Use the New-EC2Instance cmdlet with the -EbsOptimized option.
To enable Amazon EBS optimization after launch
1. If the instance is running, stop it by using the Stop-EC2Instance cmdlet.
Stop-EC2Instance -InstanceId i-1234567890abcdef0
2. Enable EBS optimization by using the Edit-EC2InstanceAttribute cmdlet with the - EbsOptimized option.
Edit-EC2InstanceAttribute `
    -InstanceId i-1234567890abcdef0 `
    -EbsOptimized $true
## CPU options for Amazon EC2 instances Many Amazon EC2 instances support simultaneous multithreading (SMT), which enables multiple threads to run concurrently on a single CPU core. Each thread is represented as a virtual CPU (vCPU) on the instance. An instance has a default number of CPU cores, which varies according to instance type. For example, an m5.xlarge instance type has two CPU cores and two threads per core by default—four vCPUs in total.
In most cases, there is an Amazon EC2 instance type that has a combination of memory and number of vCPUs to suit your workloads. However, to optimize your instance for specific workloads or business needs, you can specify the following CPU options during and after instance launch:
- Number of CPU cores: You can customize the number of CPU cores for the instance. You might do this to potentially optimize the licensing costs of your software with an instance that has sufficient amounts of RAM for memory-intensive workloads but fewer CPU cores.
- Threads per core: You can disable SMT by specifying a single thread per CPU core. You might do this for certain workloads, such as high performance computing (HPC) workloads.

Considerations
- You can't modify the number of threads per core for T2, C7a, M7a, R7a, and Apple silicon Mac instances, and instances based on the AWS Graviton processor.
- The number of instances that you can run is based on the default vCPUs for the instance types used. How we calculate the vCPUs consumed by an instance is not affected by changing its CPU options.
### Pricing There is no additional charge for specifying CPU options. For EC2 instances that are launched from license-included Windows and SQL Server AMIs, you can customize the CPU options to take advantage of the EC2 Optimize CPUs feature to pay licensing fees based on the number of vCPUs that are configured for your instance. For other EC2 instances, you're charged the same as instances that are launched with the default CPU options.
Contents
- Rules for specifying CPU options for an Amazon EC2 instance
- Supported CPU options for Amazon EC2 instance types
- Specify CPU options for an Amazon EC2 instance
- View CPU threads and cores for an Amazon EC2 instance
- Optimize CPUs for License-Included instances
### Rules for specifying CPU options for an Amazon EC2 instance To specify the CPU options for your instance, be aware of the following rules:
- You can't specify CPU options for bare metal instances.
- You can specify CPU options both during and after instance launch.
- To configure CPU options, you must specify both the number of CPU cores and threads per core in the request. For example requests, see Specify CPU options for an Amazon EC2 instance.
- The number of vCPUs for the instance is the number of CPU cores multiplied by the threads per core. To specify a custom number of vCPUs, you must specify a valid number of CPU cores and threads per core for the instance type. You cannot exceed the default number of vCPUs for the instance. For more information, see Supported CPU options for Amazon EC2 instance types.

- To disable simultaneous multithreading (SMT), also referred to as hyper-threading, specify one thread per core.
- In the console, when you change the instance type of an existing instance, Amazon EC2 applies the CPU option settings from the existing instance to the new instance, if possible. If the new instance type doesn't support those settings, the CPU options are reset to Use default CPU options. This option uses the default number of vCPUs for the new instance type.
To update settings for the new instance, select Specify CPU options under Advanced details in the Change instance type view.
- The specified CPU options persist after you stop, start, or reboot an instance.
- If you use Reserved Instances, discounts may not be applied when you configure Optimize CPUs for instances launched from license-included Windows AMIs in the same payer account.
We recommend that you use Savings Plans to reduce vCPU-based licensing costs and provide comparable savings on your compute costs.
- To save on licensing costs for instances launched from Windows and SQL Server license-included AMIs, you must configure a minimum of four vCPUs. If you configure fewer than four vCPUs, default billing is applied.
- Optimize CPUs for License-Included instances is not supported on T3 instance types.
### Supported CPU options for Amazon EC2 instance types The following tables list the instance types that support specifying CPU options.
Contents
- General purpose instances
- Compute optimized instances
- Memory optimized instances
- Storage optimized instances
- Accelerated computing instances
- High-performance computing instances

#### General purpose instances Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core m2.xlarge 2 2 1 1, 2 1 m2.2xlarg e 4 4 1 1, 2, 3, 4 1 m2.4xlarg e 8 8 1 1, 2, 3, 4, 5, 6, 7, 8 1 m3.large 2 1 2 1 1, 2 m3.xlarge 4 2 2 1, 2 1, 2 m3.2xlarg e 8 4 2 1, 2, 3, 4 1, 2 m4.large 2 1 2 1 1, 2 m4.xlarge 4 2 2 1, 2 1, 2 m4.2xlarg e 8 4 2 1, 2, 3, 4 1, 2 m4.4xlarg e 16 8 2 1, 2, 3, 4, 5, 6, 7, 8 1, 2 m4.10xlar ge 40 20 2 2, 4, 6, 8, 10, 12, 14, 16, 18, 20 1, 2 m4.16xlar ge 64 32 2 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core 24, 26, 28, 30, 32 m5.large 2 1 2 1 1, 2 m5.xlarge 4 2 2 2 1, 2 m5.2xlarg e 8 4 2 2, 4 1, 2 m5.4xlarg e 16 8 2 2, 4, 6, 8 1, 2 m5.8xlarg e 32 16 2 2, 4, 6, 8, 10, 12, 14, 16 1, 2 m5.12xlar ge 48 24 2 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24 1, 2 m5.16xlar ge 64 32 2 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32 1, 2 m5.24xlar ge 96 48 2 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core m5a.large 2 1 2 1 1, 2 m5a.xlarg e 4 2 2 2 1, 2 m5a.2xlar ge 8 4 2 2, 4 1, 2 m5a.4xlar ge 16 8 2 2, 4, 6, 8 1, 2 m5a.8xlar ge 32 16 2 4, 6, 8, 10, 12, 14, 16 1, 2 m5a.12xla rge 48 24 2 6, 12, 18, 24 1, 2 m5a.16xla rge 64 32 2 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32 1, 2 m5a.24xla rge 96 48 2 12, 18, 24, 36, 48 1, 2 m5ad.larg e 2 1 2 1 1, 2 m5ad.xlar ge 4 2 2 2 1, 2 m5ad.2xla rge 8 4 2 2, 4 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core m5ad.4xla rge 16 8 2 2, 4, 6, 8 1, 2 m5ad.8xla rge 32 16 2 4, 6, 8, 10, 12, 14, 16 1, 2 m5ad.12xl arge 48 24 2 6, 12, 18, 24 1, 2 m5ad.16xl arge 64 32 2 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32 1, 2 m5ad.24xl arge 96 48 2 12, 18, 24, 36, 48 1, 2 m5d.large 2 1 2 1 1, 2 m5d.xlarg e 4 2 2 2 1, 2 m5d.2xlar ge 8 4 2 2, 4 1, 2 m5d.4xlar ge 16 8 2 2, 4, 6, 8 1, 2 m5d.8xlar ge 32 16 2 2, 4, 6, 8, 10, 12, 14, 16 1, 2 m5d.12xla rge 48 24 2 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core m5d.16xla rge 64 32 2 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32 1, 2 m5d.24xla rge 96 48 2 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48 1, 2 m5dn.larg e 2 1 2 1 1, 2 m5dn.xlar ge 4 2 2 1, 2 1, 2 m5dn.2xla rge 8 4 2 2, 4 1, 2 m5dn.4xla rge 16 8 2 2, 4, 6, 8 1, 2 m5dn.8xla rge 32 16 2 2, 4, 6, 8, 10, 12, 14, 16 1, 2 m5dn.12xl arge 48 24 2 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core m5dn.16xl arge 64 32 2 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32 1, 2 m5dn.24xl arge 96 48 2 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48 1, 2 m5n.large 2 1 2 1 1, 2 m5n.xlarg e 4 2 2 1, 2 1, 2 m5n.2xlar ge 8 4 2 2, 4 1, 2 m5n.4xlar ge 16 8 2 2, 4, 6, 8 1, 2 m5n.8xlar ge 32 16 2 2, 4, 6, 8, 10, 12, 14, 16 1, 2 m5n.12xla rge 48 24 2 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core m5n.16xla rge 64 32 2 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32 1, 2 m5n.24xla rge 96 48 2 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48 1, 2 m5zn.larg e 2 1 2 1 1, 2 m5zn.xlar ge 4 2 2 1, 2 1, 2 m5zn.2xla rge 8 4 2 2, 4 1, 2 m5zn.3xla rge 12 6 2 2, 4, 6 1, 2 m5zn.6xla rge 24 12 2 2, 4, 6, 8, 10, 12 1, 2 m5zn.12xl arge 48 24 2 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core m6a.large 2 1 2 1 1, 2 m6a.xlarg e 4 2 2 1, 2 1, 2 m6a.2xlar ge 8 4 2 1, 2, 3, 4 1, 2 m6a.4xlar ge 16 8 2 1, 2, 3, 4, 5, 6, 7, 8 1, 2 m6a.8xlar ge 32 16 2 4, 6, 8, 10, 12, 14, 16 1, 2 m6a.12xla rge 48 24 2 1, 2, 3, 4, 5, 6, 7, 8, 16, 24 1, 2 m6a.16xla rge 64 32 2 4, 6, 8, 10, 12, 14, 16, 32 1, 2 m6a.24xla rge 96 48 2 4, 6, 8, 10, 12, 14, 16, 32, 48 1, 2 m6a.32xla rge 128 64 2 8, 12, 16, 20, 24, 28, 32, 64 1, 2 m6a.48xla rge 192 96 2 8, 12, 16, 20, 24, 28, 32, 64, 96 1, 2 m6g.large 2 2 1 1, 2 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core m6g.xlarg e 4 4 1 1, 2, 3, 4 1 m6g.2xlar ge 8 8 1 1, 2, 3, 4, 5, 6, 7, 8 1 m6g.4xlar ge 16 16 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 1 m6g.8xlar ge 32 32 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core m6g.12xla rge 48 48 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core m6g.16xla rge 64 64 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64 1 m6gd.larg e 2 2 1 1, 2 1 m6gd.xlar ge 4 4 1 1, 2, 3, 4 1 m6gd.2xla rge 8 8 1 1, 2, 3, 4, 5, 6, 7, 8 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core m6gd.4xla rge 16 16 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 1 m6gd.8xla rge 32 32 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32 1 m6gd.12xl arge 48 48 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core m6gd.16xl arge 64 64 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64 1 m6i.large 2 1 2 1 1, 2 m6i.xlarg e 4 2 2 1, 2 1, 2 m6i.2xlar ge 8 4 2 2, 4 1, 2 m6i.4xlar ge 16 8 2 2, 4, 6, 8 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core m6i.8xlar ge 32 16 2 2, 4, 6, 8, 10, 12, 14, 16 1, 2 m6i.12xla rge 48 24 2 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24 1, 2 m6i.16xla rge 64 32 2 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32 1, 2 m6i.24xla rge 96 48 2 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48 1, 2 m6i.32xla rge 128 64 2 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core m6id.larg e 2 1 2 1 1, 2 m6id.xlar ge 4 2 2 1, 2 1, 2 m6id.2xla rge 8 4 2 2, 4 1, 2 m6id.4xla rge 16 8 2 2, 4, 6, 8 1, 2 m6id.8xla rge 32 16 2 2, 4, 6, 8, 10, 12, 14, 16 1, 2 m6id.12xl arge 48 24 2 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24 1, 2 m6id.16xl arge 64 32 2 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32 1, 2 m6id.24xl arge 96 48 2 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core m6id.32xl arge 128 64 2 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64 1, 2 m6idn.lar ge 2 1 2 1 1, 2 m6idn.xla rge 4 2 2 1, 2 1, 2 m6idn.2xl arge 8 4 2 1, 2, 3, 4 1, 2 m6idn.4xl arge 16 8 2 1, 2, 3, 4, 5, 6, 7, 8 1, 2 m6idn.8xl arge 32 16 2 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core m6idn.12x large 48 24 2 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24 1, 2 m6idn.16x large 64 32 2 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32 1, 2 m6idn.24x large 96 48 2 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core m6idn.32x large 128 64 2 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64 1, 2 m6in.larg e 2 1 2 1 1, 2 m6in.xlar ge 4 2 2 1, 2 1, 2 m6in.2xla rge 8 4 2 1, 2, 3, 4 1, 2 m6in.4xla rge 16 8 2 1, 2, 3, 4, 5, 6, 7, 8 1, 2 m6in.8xla rge 32 16 2 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core m6in.12xl arge 48 24 2 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24 1, 2 m6in.16xl arge 64 32 2 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32 1, 2 m6in.24xl arge 96 48 2 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core m6in.32xl arge 128 64 2 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64 1, 2 m7a.large 2 2 1 1, 2 1 m7a.xlarg e 4 4 1 1, 2, 3, 4 1 m7a.2xlar ge 8 8 1 1, 2, 3, 4, 5, 6, 7, 8 1 m7a.4xlar ge 16 16 1 1, 2, 4, 6, 8, 10, 12, 14, 16 1 m7a.8xlar ge 32 32 1 1, 2, 3, 4, 8, 12, 16, 20, 24, 28, 32 1 m7a.12xla rge 48 48 1 1, 2, 3, 4, 5, 6, 12, 18, 24, 30, 36, 42, 48 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core m7a.16xla rge 64 64 1 1, 2, 3, 4, 5, 6, 7, 8, 16, 24, 32, 40, 48, 56, 64 1 m7a.24xla rge 96 96 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36, 48, 60, 72, 84, 96 1 m7a.32xla rge 128 128 1 4, 6, 8, 10, 12, 14, 16, 32, 48, 64, 80, 96, 112, 128 1 m7a.48xla rge 192 192 1 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 48, 72, 96, 120, 144, 168, 192 1 m7g.large 2 2 1 1, 2 1 m7g.xlarg e 4 4 1 1, 2, 3, 4 1 m7g.2xlar ge 8 8 1 1, 2, 3, 4, 5, 6, 7, 8 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core m7g.4xlar ge 16 16 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 1 m7g.8xlar ge 32 32 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32 1 m7g.12xla rge 48 48 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core m7g.16xla rge 64 64 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64 1 m7gd.larg e 2 2 1 1, 2 1 m7gd.xlar ge 4 4 1 1, 2, 3, 4 1 m7gd.2xla rge 8 8 1 1, 2, 3, 4, 5, 6, 7, 8 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core m7gd.4xla rge 16 16 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 1 m7gd.8xla rge 32 32 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32 1 m7gd.12xl arge 48 48 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core m7gd.16xl arge 64 64 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64 1 m7i.large 2 1 2 1 1, 2 m7i.xlarg e 4 2 2 1, 2 1, 2 m7i.2xlar ge 8 4 2 1, 2, 3, 4 1, 2 m7i.4xlar ge 16 8 2 1, 2, 3, 4, 5, 6, 7, 8 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core m7i.8xlar ge 32 16 2 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 1, 2 m7i.12xla rge 48 24 2 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24 1, 2 m7i.16xla rge 64 32 2 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core m7i.24xla rge 96 48 2 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48 1, 2 m7i.48xla rge 192 96 2 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core m7i-flex. large 2 1 2 1 1, 2 m7i-flex. xlarge 4 2 2 1, 2 1, 2 m7i-flex.
2xlarge 8 4 2 1, 2, 3, 4 1, 2 m7i-flex.
4xlarge 16 8 2 1, 2, 3, 4, 5, 6, 7, 8 1, 2 m7i-flex.
8xlarge 32 16 2 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 1, 2 m7i-flex.
12xlarge 48 24 2 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core m7i-flex.
16xlarge 64 32 2 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32 1, 2 m8a.mediu m 1 1 1 1 1 m8a.large 2 2 1 1, 2 1 m8a.xlarg e 4 4 1 1, 2, 3, 4 1 m8a.2xlar ge 8 8 1 1, 2, 3, 4, 5, 6, 7, 8 1 m8a.4xlar ge 16 16 1 1, 2, 4, 6, 8, 10, 12, 14, 16 1 m8a.8xlar ge 32 32 1 1, 2, 3, 4, 8, 12, 16, 20, 24, 28, 32 1 m8a.12xla rge 48 48 1 1, 2, 3, 4, 5, 6, 12, 18, 24, 30, 36, 42, 48 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core m8a.16xla rge 64 64 1 1, 2, 3, 4, 5, 6, 7, 8, 16, 24, 32, 40, 48, 56, 64 1 m8a.24xla rge 96 96 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36, 48, 60, 72, 84, 96 1 m8a.48xla rge 192 192 1 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 48, 72, 96, 120, 144, 168, 192 1 m8azn.med ium 1 1 1 1 1 m8azn.lar ge 2 2 1 1, 2 1 m8azn.xla rge 4 4 1 1, 2, 3, 4 1 m8azn.3xl arge 12 12 1 1, 2, 4, 6, 8, 10, 12 1 m8azn.6xl arge 24 24 1 1, 2, 3, 4, 8, 12, 16, 20, 24 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core m8azn.12x large 48 48 1 1, 2, 3, 4, 5, 6, 7, 8, 16, 24, 32, 40, 48 1 m8azn.24x large 96 96 1 4, 6, 8, 10, 12, 14, 16, 32, 48, 64, 80, 96 1 m8g.large 2 2 1 1, 2 1 m8g.xlarg e 4 4 1 1, 2, 3, 4 1 m8g.2xlar ge 8 8 1 1, 2, 3, 4, 5, 6, 7, 8 1 m8g.4xlar ge 16 16 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 1 m8g.8xlar ge 32 32 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core m8g.12xla rge 48 48 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core m8g.16xla rge 64 64 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core m8g.24xla rge 96 96 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core m8g.48xla rge 192 192 1 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100, 102, 104, 106, 108, 110, 112, 114, 116, 118, 120, 122, 124, 126, 128, 130, 132, 134, 136, 138, 140, 142, 144, 146, 148, 150, 152, 154, 156, 158, 160, 162, 164, 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core 166, 168, 170, 172, 174, 176, 178, 180, 182, 184, 186, 188, 190, 192 m8gb.larg e 2 2 1 1, 2 1 m8gb.xlar ge 4 4 1 1, 2, 3, 4 1 m8gb.2xla rge 8 8 1 1, 2, 3, 4, 5, 6, 7, 8 1 m8gb.4xla rge 16 16 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 1 m8gb.8xla rge 32 32 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core m8gb.12xl arge 48 48 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core m8gb.16xl arge 64 64 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core m8gb.24xl arge 96 96 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core m8gb.48xl arge 192 192 1 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100, 102, 104, 106, 108, 110, 112, 114, 116, 118, 120, 122, 124, 126, 128, 130, 132, 134, 136, 138, 140, 142, 144, 146, 148, 150, 152, 154, 156, 158, 160, 162, 164, 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core 166, 168, 170, 172, 174, 176, 178, 180, 182, 184, 186, 188, 190, 192 m8gd.larg e 2 2 1 1, 2 1 m8gd.xlar ge 4 4 1 1, 2, 3, 4 1 m8gd.2xla rge 8 8 1 1, 2, 3, 4, 5, 6, 7, 8 1 m8gd.4xla rge 16 16 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 1 m8gd.8xla rge 32 32 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core m8gd.12xl arge 48 48 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core m8gd.16xl arge 64 64 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core m8gd.24xl arge 96 96 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core m8gd.48xl arge 192 192 1 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100, 102, 104, 106, 108, 110, 112, 114, 116, 118, 120, 122, 124, 126, 128, 130, 132, 134, 136, 138, 140, 142, 144, 146, 148, 150, 152, 154, 156, 158, 160, 162, 164, 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core 166, 168, 170, 172, 174, 176, 178, 180, 182, 184, 186, 188, 190, 192 m8gn.larg e 2 2 1 1, 2 1 m8gn.xlar ge 4 4 1 1, 2, 3, 4 1 m8gn.2xla rge 8 8 1 1, 2, 3, 4, 5, 6, 7, 8 1 m8gn.4xla rge 16 16 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 1 m8gn.8xla rge 32 32 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core m8gn.12xl arge 48 48 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core m8gn.16xl arge 64 64 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core m8gn.24xl arge 96 96 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core m8gn.48xl arge 192 192 1 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100, 102, 104, 106, 108, 110, 112, 114, 116, 118, 120, 122, 124, 126, 128, 130, 132, 134, 136, 138, 140, 142, 144, 146, 148, 150, 152, 154, 156, 158, 160, 162, 164, 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core 166, 168, 170, 172, 174, 176, 178, 180, 182, 184, 186, 188, 190, 192 m8i.large 2 1 2 1 1, 2 m8i.xlarg e 4 2 2 1, 2 1, 2 m8i.2xlar ge 8 4 2 1, 2, 3, 4 1, 2 m8i.4xlar ge 16 8 2 1, 2, 3, 4, 5, 6, 7, 8 1, 2 m8i.8xlar ge 32 16 2 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 1, 2 m8i.12xla rge 48 24 2 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core m8i.16xla rge 64 32 2 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32 1, 2 m8i.24xla rge 96 48 2 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48 1, 2 m8i.32xla rge 128 64 2 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core m8i.48xla rge 192 96 2 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96 1, 2 m8i.96xla rge 384 192 2 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96, 102, 108, 114, 120, 126, 132, 138, 144, 150, 156, 162, 168, 174, 180, 186, 192 1, 2 m8id.larg e 2 1 2 1 1, 2 m8id.xlar ge 4 2 2 1, 2 1, 2 m8id.2xla rge 8 4 2 1, 2, 3, 4 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core m8id.4xla rge 16 8 2 1, 2, 3, 4, 5, 6, 7, 8 1, 2 m8id.8xla rge 32 16 2 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 1, 2 m8id.12xl arge 48 24 2 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24 1, 2 m8id.16xl arge 64 32 2 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core m8id.24xl arge 96 48 2 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48 1, 2 m8id.32xl arge 128 64 2 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64 1, 2 m8id.48xl arge 192 96 2 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core m8id.96xl arge 384 192 2 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96, 102, 108, 114, 120, 126, 132, 138, 144, 150, 156, 162, 168, 174, 180, 186, 192 1, 2 m8i-flex. large 2 1 2 1 1, 2 m8i-flex. xlarge 4 2 2 1, 2 1, 2 m8i-flex.
2xlarge 8 4 2 1, 2, 3, 4 1, 2 m8i-flex.
4xlarge 16 8 2 1, 2, 3, 4, 5, 6, 7, 8 1, 2 m8i-flex.
8xlarge 32 16 2 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core m8i-flex.
12xlarge 48 24 2 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24 1, 2 m8i-flex.
16xlarge 64 32 2 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32 1, 2 t3.nano 2 1 2 1 1, 2 t3.micro 2 1 2 1 1, 2 t3.small 2 1 2 1 1, 2 t3.medium 2 1 2 1 1, 2 t3.large 2 1 2 1 1, 2 t3.xlarge 4 2 2 2 1, 2 t3.2xlarg e 8 4 2 2, 4 1, 2 t3a.nano 2 1 2 1 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core t3a.micro 2 1 2 1 1, 2 t3a.small 2 1 2 1 1, 2 t3a.mediu m 2 1 2 1 1, 2 t3a.large 2 1 2 1 1, 2 t3a.xlarg e 4 2 2 2 1, 2 t3a.2xlar ge 8 4 2 2, 4 1, 2 t4g.nano 2 2 1 1, 2 1 t4g.micro 2 2 1 1, 2 1 t4g.small 2 2 1 1, 2 1 t4g.mediu m 2 2 1 1, 2 1 t4g.large 2 2 1 1, 2 1 t4g.xlarg e 4 4 1 1, 2, 3, 4 1 t4g.2xlar ge 8 8 1 1, 2, 3, 4, 5, 6, 7, 8 1

#### Compute optimized instances Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core c3.large 2 1 2 1 1, 2 c3.xlarge 4 2 2 1, 2 1, 2 c3.2xlarg e 8 4 2 1, 2, 3, 4 1, 2 c3.4xlarg e 16 8 2 1, 2, 3, 4, 5, 6, 7, 8 1, 2 c3.8xlarg e 32 16 2 2, 4, 6, 8, 10, 12, 14, 16 1, 2 c4.large 2 1 2 1 1, 2 c4.xlarge 4 2 2 1, 2 1, 2 c4.2xlarg e 8 4 2 1, 2, 3, 4 1, 2 c4.4xlarg e 16 8 2 1, 2, 3, 4, 5, 6, 7, 8 1, 2 c4.8xlarg e 36 18 2 2, 4, 6, 8, 10, 12, 14, 16, 18 1, 2 c5.large 2 1 2 1 1, 2 c5.xlarge 4 2 2 2 1, 2 c5.2xlarg e 8 4 2 2, 4 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core c5.4xlarg e 16 8 2 2, 4, 6, 8 1, 2 c5.9xlarg e 36 18 2 2, 4, 6, 8, 10, 12, 14, 16, 18 1, 2 c5.12xlar ge 48 24 2 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24 1, 2 c5.18xlar ge 72 36 2 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36 1, 2 c5.24xlar ge 96 48 2 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48 1, 2 c5a.large 2 1 2 1 1, 2 c5a.xlarg e 4 2 2 1, 2 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core c5a.2xlar ge 8 4 2 1, 2, 3, 4 1, 2 c5a.4xlar ge 16 8 2 1, 2, 3, 4, 8 1, 2 c5a.8xlar ge 32 16 2 1, 2, 3, 4, 8, 12, 16 1, 2 c5a.12xla rge 48 24 2 1, 2, 3, 4, 8, 12, 16, 20, 24 1, 2 c5a.16xla rge 64 32 2 1, 2, 3, 4, 8, 12, 16, 20, 24, 28, 32 1, 2 c5a.24xla rge 96 48 2 1, 2, 3, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48 1, 2 c5ad.larg e 2 1 2 1 1, 2 c5ad.xlar ge 4 2 2 1, 2 1, 2 c5ad.2xla rge 8 4 2 1, 2, 3, 4 1, 2 c5ad.4xla rge 16 8 2 1, 2, 3, 4, 8 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core c5ad.8xla rge 32 16 2 1, 2, 3, 4, 8, 12, 16 1, 2 c5ad.12xl arge 48 24 2 1, 2, 3, 4, 8, 12, 16, 20, 24 1, 2 c5ad.16xl arge 64 32 2 1, 2, 3, 4, 8, 12, 16, 20, 24, 28, 32 1, 2 c5ad.24xl arge 96 48 2 1, 2, 3, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48 1, 2 c5d.large 2 1 2 1 1, 2 c5d.xlarg e 4 2 2 2 1, 2 c5d.2xlar ge 8 4 2 2, 4 1, 2 c5d.4xlar ge 16 8 2 2, 4, 6, 8 1, 2 c5d.9xlar ge 36 18 2 2, 4, 6, 8, 10, 12, 14, 16, 18 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core c5d.12xla rge 48 24 2 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24 1, 2 c5d.18xla rge 72 36 2 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36 1, 2 c5d.24xla rge 96 48 2 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48 1, 2 c5n.large 2 1 2 1 1, 2 c5n.xlarg e 4 2 2 2 1, 2 c5n.2xlar ge 8 4 2 2, 4 1, 2 c5n.4xlar ge 16 8 2 2, 4, 6, 8 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core c5n.9xlar ge 36 18 2 2, 4, 6, 8, 10, 12, 14, 16, 18 1, 2 c5n.18xla rge 72 36 2 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36 1, 2 c6a.large 2 1 2 1 1, 2 c6a.xlarg e 4 2 2 1, 2 1, 2 c6a.2xlar ge 8 4 2 1, 2, 3, 4 1, 2 c6a.4xlar ge 16 8 2 1, 2, 3, 4, 5, 6, 7, 8 1, 2 c6a.8xlar ge 32 16 2 4, 6, 8, 10, 12, 14, 16 1, 2 c6a.12xla rge 48 24 2 1, 2, 3, 4, 5, 6, 7, 8, 16, 24 1, 2 c6a.16xla rge 64 32 2 4, 6, 8, 10, 12, 14, 16, 32 1, 2 c6a.24xla rge 96 48 2 4, 6, 8, 10, 12, 14, 16, 32, 48 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core c6a.32xla rge 128 64 2 8, 12, 16, 20, 24, 28, 32, 64 1, 2 c6a.48xla rge 192 96 2 8, 12, 16, 20, 24, 28, 32, 64, 96 1, 2 c6g.large 2 2 1 1, 2 1 c6g.xlarg e 4 4 1 1, 2, 3, 4 1 c6g.2xlar ge 8 8 1 1, 2, 3, 4, 5, 6, 7, 8 1 c6g.4xlar ge 16 16 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 1 c6g.8xlar ge 32 32 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core c6g.12xla rge 48 48 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core c6g.16xla rge 64 64 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64 1 c6gd.larg e 2 2 1 1, 2 1 c6gd.xlar ge 4 4 1 1, 2, 3, 4 1 c6gd.2xla rge 8 8 1 1, 2, 3, 4, 5, 6, 7, 8 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core c6gd.4xla rge 16 16 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 1 c6gd.8xla rge 32 32 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32 1 c6gd.12xl arge 48 48 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core c6gd.16xl arge 64 64 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64 1 c6gn.medi um 1 1 1 1 1 c6gn.larg e 2 2 1 1, 2 1 c6gn.xlar ge 4 4 1 1, 2, 3, 4 1 c6gn.2xla rge 8 8 1 1, 2, 3, 4, 5, 6, 7, 8 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core c6gn.4xla rge 16 16 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 1 c6gn.8xla rge 32 32 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32 1 c6gn.12xl arge 48 48 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core c6gn.16xl arge 64 64 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64 1 c6i.large 2 1 2 1 1, 2 c6i.xlarg e 4 2 2 1, 2 1, 2 c6i.2xlar ge 8 4 2 2, 4 1, 2 c6i.4xlar ge 16 8 2 2, 4, 6, 8 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core c6i.8xlar ge 32 16 2 2, 4, 6, 8, 10, 12, 14, 16 1, 2 c6i.12xla rge 48 24 2 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24 1, 2 c6i.16xla rge 64 32 2 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32 1, 2 c6i.24xla rge 96 48 2 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48 1, 2 c6i.32xla rge 128 64 2 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core c6id.larg e 2 1 2 1 1, 2 c6id.xlar ge 4 2 2 1, 2 1, 2 c6id.2xla rge 8 4 2 2, 4 1, 2 c6id.4xla rge 16 8 2 2, 4, 6, 8 1, 2 c6id.8xla rge 32 16 2 2, 4, 6, 8, 10, 12, 14, 16 1, 2 c6id.12xl arge 48 24 2 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24 1, 2 c6id.16xl arge 64 32 2 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32 1, 2 c6id.24xl arge 96 48 2 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core c6id.32xl arge 128 64 2 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64 1, 2 c6in.larg e 2 1 2 1 1, 2 c6in.xlar ge 4 2 2 1, 2 1, 2 c6in.2xla rge 8 4 2 1, 2, 3, 4 1, 2 c6in.4xla rge 16 8 2 1, 2, 3, 4, 5, 6, 7, 8 1, 2 c6in.8xla rge 32 16 2 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core c6in.12xl arge 48 24 2 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24 1, 2 c6in.16xl arge 64 32 2 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32 1, 2 c6in.24xl arge 96 48 2 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core c6in.32xl arge 128 64 2 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64 1, 2 c7a.large 2 2 1 1, 2 1 c7a.xlarg e 4 4 1 1, 2, 3, 4 1 c7a.2xlar ge 8 8 1 1, 2, 3, 4, 5, 6, 7, 8 1 c7a.4xlar ge 16 16 1 1, 2, 4, 6, 8, 10, 12, 14, 16 1 c7a.8xlar ge 32 32 1 1, 2, 3, 4, 8, 12, 16, 20, 24, 28, 32 1 c7a.12xla rge 48 48 1 1, 2, 3, 4, 5, 6, 12, 18, 24, 30, 36, 42, 48 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core c7a.16xla rge 64 64 1 1, 2, 3, 4, 5, 6, 7, 8, 16, 24, 32, 40, 48, 56, 64 1 c7a.24xla rge 96 96 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36, 48, 60, 72, 84, 96 1 c7a.32xla rge 128 128 1 4, 6, 8, 10, 12, 14, 16, 32, 48, 64, 80, 96, 112, 128 1 c7a.48xla rge 192 192 1 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 48, 72, 96, 120, 144, 168, 192 1 c7g.large 2 2 1 1, 2 1 c7g.xlarg e 4 4 1 1, 2, 3, 4 1 c7g.2xlar ge 8 8 1 1, 2, 3, 4, 5, 6, 7, 8 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core c7g.4xlar ge 16 16 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 1 c7g.8xlar ge 32 32 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32 1 c7g.12xla rge 48 48 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core c7g.16xla rge 64 64 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64 1 c7gd.larg e 2 2 1 1, 2 1 c7gd.xlar ge 4 4 1 1, 2, 3, 4 1 c7gd.2xla rge 8 8 1 1, 2, 3, 4, 5, 6, 7, 8 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core c7gd.4xla rge 16 16 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 1 c7gd.8xla rge 32 32 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32 1 c7gd.12xl arge 48 48 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core c7gd.16xl arge 64 64 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64 1 c7gn.larg e 2 2 1 1, 2 1 c7gn.xlar ge 4 4 1 1, 2, 3, 4 1 c7gn.2xla rge 8 8 1 1, 2, 3, 4, 5, 6, 7, 8 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core c7gn.4xla rge 16 16 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 1 c7gn.8xla rge 32 32 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32 1 c7gn.12xl arge 48 48 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core c7gn.16xl arge 64 64 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64 1 c7i.large 2 1 2 1 1, 2 c7i.xlarg e 4 2 2 1, 2 1, 2 c7i.2xlar ge 8 4 2 1, 2, 3, 4 1, 2 c7i.4xlar ge 16 8 2 1, 2, 3, 4, 5, 6, 7, 8 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core c7i.8xlar ge 32 16 2 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 1, 2 c7i.12xla rge 48 24 2 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24 1, 2 c7i.16xla rge 64 32 2 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core c7i.24xla rge 96 48 2 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48 1, 2 c7i.48xla rge 192 96 2 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core c7i-flex. large 2 1 2 1 1, 2 c7i-flex. xlarge 4 2 2 1, 2 1, 2 c7i-flex.
2xlarge 8 4 2 1, 2, 3, 4 1, 2 c7i-flex.
4xlarge 16 8 2 1, 2, 3, 4, 5, 6, 7, 8 1, 2 c7i-flex.
8xlarge 32 16 2 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 1, 2 c7i-flex.
12xlarge 48 24 2 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core c7i-flex.
16xlarge 64 32 2 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32 1, 2 c8a.mediu m 1 1 1 1 1 c8a.large 2 2 1 1, 2 1 c8a.xlarg e 4 4 1 1, 2, 3, 4 1 c8a.2xlar ge 8 8 1 1, 2, 3, 4, 5, 6, 7, 8 1 c8a.4xlar ge 16 16 1 1, 2, 4, 6, 8, 10, 12, 14, 16 1 c8a.8xlar ge 32 32 1 1, 2, 3, 4, 8, 12, 16, 20, 24, 28, 32 1 c8a.12xla rge 48 48 1 1, 2, 3, 4, 5, 6, 12, 18, 24, 30, 36, 42, 48 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core c8a.16xla rge 64 64 1 1, 2, 3, 4, 5, 6, 7, 8, 16, 24, 32, 40, 48, 56, 64 1 c8a.24xla rge 96 96 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36, 48, 60, 72, 84, 96 1 c8a.48xla rge 192 192 1 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 48, 72, 96, 120, 144, 168, 192 1 c8g.large 2 2 1 1, 2 1 c8g.xlarg e 4 4 1 1, 2, 3, 4 1 c8g.2xlar ge 8 8 1 1, 2, 3, 4, 5, 6, 7, 8 1 c8g.4xlar ge 16 16 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core c8g.8xlar ge 32 32 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32 1 c8g.12xla rge 48 48 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core c8g.16xla rge 64 64 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core c8g.24xla rge 96 96 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core c8g.48xla rge 192 192 1 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100, 102, 104, 106, 108, 110, 112, 114, 116, 118, 120, 122, 124, 126, 128, 130, 132, 134, 136, 138, 140, 142, 144, 146, 148, 150, 152, 154, 156, 158, 160, 162, 164, 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core 166, 168, 170, 172, 174, 176, 178, 180, 182, 184, 186, 188, 190, 192 c8gb.larg e 2 2 1 1, 2 1 c8gb.xlar ge 4 4 1 1, 2, 3, 4 1 c8gb.2xla rge 8 8 1 1, 2, 3, 4, 5, 6, 7, 8 1 c8gb.4xla rge 16 16 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 1 c8gb.8xla rge 32 32 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core c8gb.12xl arge 48 48 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core c8gb.16xl arge 64 64 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core c8gb.24xl arge 96 96 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core c8gb.48xl arge 192 192 1 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100, 102, 104, 106, 108, 110, 112, 114, 116, 118, 120, 122, 124, 126, 128, 130, 132, 134, 136, 138, 140, 142, 144, 146, 148, 150, 152, 154, 156, 158, 160, 162, 164, 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core 166, 168, 170, 172, 174, 176, 178, 180, 182, 184, 186, 188, 190, 192 c8gd.larg e 2 2 1 1, 2 1 c8gd.xlar ge 4 4 1 1, 2, 3, 4 1 c8gd.2xla rge 8 8 1 1, 2, 3, 4, 5, 6, 7, 8 1 c8gd.4xla rge 16 16 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 1 c8gd.8xla rge 32 32 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core c8gd.12xl arge 48 48 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core c8gd.16xl arge 64 64 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core c8gd.24xl arge 96 96 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core c8gd.48xl arge 192 192 1 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100, 102, 104, 106, 108, 110, 112, 114, 116, 118, 120, 122, 124, 126, 128, 130, 132, 134, 136, 138, 140, 142, 144, 146, 148, 150, 152, 154, 156, 158, 160, 162, 164, 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core 166, 168, 170, 172, 174, 176, 178, 180, 182, 184, 186, 188, 190, 192 c8gn.larg e 2 2 1 1, 2 1 c8gn.xlar ge 4 4 1 1, 2, 3, 4 1 c8gn.2xla rge 8 8 1 1, 2, 3, 4, 5, 6, 7, 8 1 c8gn.4xla rge 16 16 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 1 c8gn.8xla rge 32 32 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core c8gn.12xl arge 48 48 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core c8gn.16xl arge 64 64 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core c8gn.24xl arge 96 96 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core c8gn.48xl arge 192 192 1 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100, 102, 104, 106, 108, 110, 112, 114, 116, 118, 120, 122, 124, 126, 128, 130, 132, 134, 136, 138, 140, 142, 144, 146, 148, 150, 152, 154, 156, 158, 160, 162, 164, 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core 166, 168, 170, 172, 174, 176, 178, 180, 182, 184, 186, 188, 190, 192 c8i.large 2 1 2 1 1, 2 c8i.xlarg e 4 2 2 1, 2 1, 2 c8i.2xlar ge 8 4 2 1, 2, 3, 4 1, 2 c8i.4xlar ge 16 8 2 1, 2, 3, 4, 5, 6, 7, 8 1, 2 c8i.8xlar ge 32 16 2 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 1, 2 c8i.12xla rge 48 24 2 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core c8i.16xla rge 64 32 2 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32 1, 2 c8i.24xla rge 96 48 2 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48 1, 2 c8i.32xla rge 128 64 2 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core c8i.48xla rge 192 96 2 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96 1, 2 c8i.96xla rge 384 192 2 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96, 102, 108, 114, 120, 126, 132, 138, 144, 150, 156, 162, 168, 174, 180, 186, 192 1, 2 c8id.larg e 2 1 2 1 1, 2 c8id.xlar ge 4 2 2 1, 2 1, 2 c8id.2xla rge 8 4 2 1, 2, 3, 4 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core c8id.4xla rge 16 8 2 1, 2, 3, 4, 5, 6, 7, 8 1, 2 c8id.8xla rge 32 16 2 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 1, 2 c8id.12xl arge 48 24 2 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24 1, 2 c8id.16xl arge 64 32 2 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core c8id.24xl arge 96 48 2 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48 1, 2 c8id.32xl arge 128 64 2 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64 1, 2 c8id.48xl arge 192 96 2 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core c8id.96xl arge 384 192 2 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96, 102, 108, 114, 120, 126, 132, 138, 144, 150, 156, 162, 168, 174, 180, 186, 192 1, 2 c8i-flex. large 2 1 2 1 1, 2 c8i-flex. xlarge 4 2 2 1, 2 1, 2 c8i-flex.
2xlarge 8 4 2 1, 2, 3, 4 1, 2 c8i-flex.
4xlarge 16 8 2 1, 2, 3, 4, 5, 6, 7, 8 1, 2 c8i-flex.
8xlarge 32 16 2 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core c8i-flex.
12xlarge 48 24 2 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24 1, 2 c8i-flex.
16xlarge 64 32 2 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32 1, 2
#### Memory optimized instances Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core r3.large 2 1 2 1 1, 2 r3.xlarge 4 2 2 1, 2 1, 2 r3.2xlarg e 8 4 2 1, 2, 3, 4 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core r3.4xlarg e 16 8 2 1, 2, 3, 4, 5, 6, 7, 8 1, 2 r3.8xlarg e 32 16 2 2, 4, 6, 8, 10, 12, 14, 16 1, 2 r4.large 2 1 2 1 1, 2 r4.xlarge 4 2 2 1, 2 1, 2 r4.2xlarg e 8 4 2 1, 2, 3, 4 1, 2 r4.4xlarg e 16 8 2 1, 2, 3, 4, 5, 6, 7, 8 1, 2 r4.8xlarg e 32 16 2 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 1, 2 r4.16xlar ge 64 32 2 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32 1, 2 r5.large 2 1 2 1 1, 2 r5.xlarge 4 2 2 2 1, 2 r5.2xlarg e 8 4 2 2, 4 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core r5.4xlarg e 16 8 2 2, 4, 6, 8 1, 2 r5.8xlarg e 32 16 2 2, 4, 6, 8, 10, 12, 14, 16 1, 2 r5.12xlar ge 48 24 2 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24 1, 2 r5.16xlar ge 64 32 2 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32 1, 2 r5.24xlar ge 96 48 2 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48 1, 2 r5a.large 2 1 2 1 1, 2 r5a.xlarg e 4 2 2 2 1, 2 r5a.2xlar ge 8 4 2 2, 4 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core r5a.4xlar ge 16 8 2 2, 4, 6, 8 1, 2 r5a.8xlar ge 32 16 2 4, 6, 8, 10, 12, 14, 16 1, 2 r5a.12xla rge 48 24 2 6, 12, 18, 24 1, 2 r5a.16xla rge 64 32 2 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32 1, 2 r5a.24xla rge 96 48 2 12, 18, 24, 36, 48 1, 2 r5ad.larg e 2 1 2 1 1, 2 r5ad.xlar ge 4 2 2 2 1, 2 r5ad.2xla rge 8 4 2 2, 4 1, 2 r5ad.4xla rge 16 8 2 2, 4, 6, 8 1, 2 r5ad.8xla rge 32 16 2 4, 6, 8, 10, 12, 14, 16 1, 2 r5ad.12xl arge 48 24 2 6, 12, 18, 24 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core r5ad.16xl arge 64 32 2 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32 1, 2 r5ad.24xl arge 96 48 2 12, 18, 24, 36, 48 1, 2 r5b.large 2 1 2 1 1, 2 r5b.xlarg e 4 2 2 1, 2 1, 2 r5b.2xlar ge 8 4 2 2, 4 1, 2 r5b.4xlar ge 16 8 2 2, 4, 6, 8 1, 2 r5b.8xlar ge 32 16 2 2, 4, 6, 8, 10, 12, 14, 16 1, 2 r5b.12xla rge 48 24 2 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24 1, 2 r5b.16xla rge 64 32 2 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core r5b.24xla rge 96 48 2 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48 1, 2 r5d.large 2 1 2 1 1, 2 r5d.xlarg e 4 2 2 2 1, 2 r5d.2xlar ge 8 4 2 2, 4 1, 2 r5d.4xlar ge 16 8 2 2, 4, 6, 8 1, 2 r5d.8xlar ge 32 16 2 2, 4, 6, 8, 10, 12, 14, 16 1, 2 r5d.12xla rge 48 24 2 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24 1, 2 r5d.16xla rge 64 32 2 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core r5d.24xla rge 96 48 2 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48 1, 2 r5dn.larg e 2 1 2 1 1, 2 r5dn.xlar ge 4 2 2 1, 2 1, 2 r5dn.2xla rge 8 4 2 2, 4 1, 2 r5dn.4xla rge 16 8 2 2, 4, 6, 8 1, 2 r5dn.8xla rge 32 16 2 2, 4, 6, 8, 10, 12, 14, 16 1, 2 r5dn.12xl arge 48 24 2 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24 1, 2 r5dn.16xl arge 64 32 2 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core r5dn.24xl arge 96 48 2 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48 1, 2 r5n.large 2 1 2 1 1, 2 r5n.xlarg e 4 2 2 1, 2 1, 2 r5n.2xlar ge 8 4 2 2, 4 1, 2 r5n.4xlar ge 16 8 2 2, 4, 6, 8 1, 2 r5n.8xlar ge 32 16 2 2, 4, 6, 8, 10, 12, 14, 16 1, 2 r5n.12xla rge 48 24 2 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24 1, 2 r5n.16xla rge 64 32 2 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core r5n.24xla rge 96 48 2 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48 1, 2 r6a.large 2 1 2 1 1, 2 r6a.xlarg e 4 2 2 1, 2 1, 2 r6a.2xlar ge 8 4 2 1, 2, 3, 4 1, 2 r6a.4xlar ge 16 8 2 1, 2, 3, 4, 5, 6, 7, 8 1, 2 r6a.8xlar ge 32 16 2 4, 6, 8, 10, 12, 14, 16 1, 2 r6a.12xla rge 48 24 2 1, 2, 3, 4, 5, 6, 7, 8, 16, 24 1, 2 r6a.16xla rge 64 32 2 4, 6, 8, 10, 12, 14, 16, 32 1, 2 r6a.24xla rge 96 48 2 4, 6, 8, 10, 12, 14, 16, 32, 48 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core r6a.32xla rge 128 64 2 8, 12, 16, 20, 24, 28, 32, 64 1, 2 r6a.48xla rge 192 96 2 8, 12, 16, 20, 24, 28, 32, 64, 96 1, 2 r6g.large 2 2 1 1, 2 1 r6g.xlarg e 4 4 1 1, 2, 3, 4 1 r6g.2xlar ge 8 8 1 1, 2, 3, 4, 5, 6, 7, 8 1 r6g.4xlar ge 16 16 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 1 r6g.8xlar ge 32 32 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core r6g.12xla rge 48 48 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core r6g.16xla rge 64 64 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64 1 r6gd.larg e 2 2 1 1, 2 1 r6gd.xlar ge 4 4 1 1, 2, 3, 4 1 r6gd.2xla rge 8 8 1 1, 2, 3, 4, 5, 6, 7, 8 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core r6gd.4xla rge 16 16 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 1 r6gd.8xla rge 32 32 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32 1 r6gd.12xl arge 48 48 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core r6gd.16xl arge 64 64 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64 1 r6i.large 2 1 2 1 1, 2 r6i.xlarg e 4 2 2 1, 2 1, 2 r6i.2xlar ge 8 4 2 2, 4 1, 2 r6i.4xlar ge 16 8 2 2, 4, 6, 8 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core r6i.8xlar ge 32 16 2 2, 4, 6, 8, 10, 12, 14, 16 1, 2 r6i.12xla rge 48 24 2 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24 1, 2 r6i.16xla rge 64 32 2 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32 1, 2 r6i.24xla rge 96 48 2 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48 1, 2 r6i.32xla rge 128 64 2 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core r6id.larg e 2 1 2 1 1, 2 r6id.xlar ge 4 2 2 1, 2 1, 2 r6id.2xla rge 8 4 2 2, 4 1, 2 r6id.4xla rge 16 8 2 2, 4, 6, 8 1, 2 r6id.8xla rge 32 16 2 2, 4, 6, 8, 10, 12, 14, 16 1, 2 r6id.12xl arge 48 24 2 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24 1, 2 r6id.16xl arge 64 32 2 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32 1, 2 r6id.24xl arge 96 48 2 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core r6id.32xl arge 128 64 2 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64 1, 2 r6idn.lar ge 2 1 2 1 1, 2 r6idn.xla rge 4 2 2 1, 2 1, 2 r6idn.2xl arge 8 4 2 1, 2, 3, 4 1, 2 r6idn.4xl arge 16 8 2 1, 2, 3, 4, 5, 6, 7, 8 1, 2 r6idn.8xl arge 32 16 2 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core r6idn.12x large 48 24 2 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24 1, 2 r6idn.16x large 64 32 2 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32 1, 2 r6idn.24x large 96 48 2 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core r6idn.32x large 128 64 2 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64 1, 2 r6in.larg e 2 1 2 1 1, 2 r6in.xlar ge 4 2 2 1, 2 1, 2 r6in.2xla rge 8 4 2 1, 2, 3, 4 1, 2 r6in.4xla rge 16 8 2 1, 2, 3, 4, 5, 6, 7, 8 1, 2 r6in.8xla rge 32 16 2 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core r6in.12xl arge 48 24 2 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24 1, 2 r6in.16xl arge 64 32 2 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32 1, 2 r6in.24xl arge 96 48 2 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core r6in.32xl arge 128 64 2 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64 1, 2 r7a.large 2 2 1 1, 2 1 r7a.xlarg e 4 4 1 1, 2, 3, 4 1 r7a.2xlar ge 8 8 1 1, 2, 3, 4, 5, 6, 7, 8 1 r7a.4xlar ge 16 16 1 1, 2, 4, 6, 8, 10, 12, 14, 16 1 r7a.8xlar ge 32 32 1 1, 2, 3, 4, 8, 12, 16, 20, 24, 28, 32 1 r7a.12xla rge 48 48 1 1, 2, 3, 4, 5, 6, 12, 18, 24, 30, 36, 42, 48 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core r7a.16xla rge 64 64 1 1, 2, 3, 4, 5, 6, 7, 8, 16, 24, 32, 40, 48, 56, 64 1 r7a.24xla rge 96 96 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36, 48, 60, 72, 84, 96 1 r7a.32xla rge 128 128 1 4, 6, 8, 10, 12, 14, 16, 32, 48, 64, 80, 96, 112, 128 1 r7a.48xla rge 192 192 1 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 48, 72, 96, 120, 144, 168, 192 1 r7g.large 2 2 1 1, 2 1 r7g.xlarg e 4 4 1 1, 2, 3, 4 1 r7g.2xlar ge 8 8 1 1, 2, 3, 4, 5, 6, 7, 8 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core r7g.4xlar ge 16 16 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 1 r7g.8xlar ge 32 32 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32 1 r7g.12xla rge 48 48 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core r7g.16xla rge 64 64 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64 1 r7gd.larg e 2 2 1 1, 2 1 r7gd.xlar ge 4 4 1 1, 2, 3, 4 1 r7gd.2xla rge 8 8 1 1, 2, 3, 4, 5, 6, 7, 8 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core r7gd.4xla rge 16 16 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 1 r7gd.8xla rge 32 32 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32 1 r7gd.12xl arge 48 48 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core r7gd.16xl arge 64 64 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64 1 r7i.large 2 1 2 1 1, 2 r7i.xlarg e 4 2 2 1, 2 1, 2 r7i.2xlar ge 8 4 2 1, 2, 3, 4 1, 2 r7i.4xlar ge 16 8 2 1, 2, 3, 4, 5, 6, 7, 8 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core r7i.8xlar ge 32 16 2 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 1, 2 r7i.12xla rge 48 24 2 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24 1, 2 r7i.16xla rge 64 32 2 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core r7i.24xla rge 96 48 2 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48 1, 2 r7i.48xla rge 192 96 2 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core r7iz.larg e 2 1 2 1 1, 2 r7iz.xlar ge 4 2 2 1, 2 1, 2 r7iz.2xla rge 8 4 2 1, 2, 3, 4 1, 2 r7iz.4xla rge 16 8 2 1, 2, 3, 4, 5, 6, 7, 8 1, 2 r7iz.8xla rge 32 16 2 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 1, 2 r7iz.12xl arge 48 24 2 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core r7iz.16xl arge 64 32 2 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32 1, 2 r7iz.32xl arge 128 64 2 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64 1, 2 r8a.mediu m 1 1 1 1 1 r8a.large 2 2 1 1, 2 1 r8a.xlarg e 4 4 1 1, 2, 3, 4 1 r8a.2xlar ge 8 8 1 1, 2, 3, 4, 5, 6, 7, 8 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core r8a.4xlar ge 16 16 1 1, 2, 4, 6, 8, 10, 12, 14, 16 1 r8a.8xlar ge 32 32 1 1, 2, 3, 4, 8, 12, 16, 20, 24, 28, 32 1 r8a.12xla rge 48 48 1 1, 2, 3, 4, 5, 6, 12, 18, 24, 30, 36, 42, 48 1 r8a.16xla rge 64 64 1 1, 2, 3, 4, 5, 6, 7, 8, 16, 24, 32, 40, 48, 56, 64 1 r8a.24xla rge 96 96 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36, 48, 60, 72, 84, 96 1 r8a.48xla rge 192 192 1 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 48, 72, 96, 120, 144, 168, 192 1 r8g.large 2 2 1 1, 2 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core r8g.xlarg e 4 4 1 1, 2, 3, 4 1 r8g.2xlar ge 8 8 1 1, 2, 3, 4, 5, 6, 7, 8 1 r8g.4xlar ge 16 16 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 1 r8g.8xlar ge 32 32 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core r8g.12xla rge 48 48 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core r8g.16xla rge 64 64 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core r8g.24xla rge 96 96 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core r8g.48xla rge 192 192 1 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100, 102, 104, 106, 108, 110, 112, 114, 116, 118, 120, 122, 124, 126, 128, 130, 132, 134, 136, 138, 140, 142, 144, 146, 148, 150, 152, 154, 156, 158, 160, 162, 164, 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core 166, 168, 170, 172, 174, 176, 178, 180, 182, 184, 186, 188, 190, 192 r8gb.larg e 2 2 1 1, 2 1 r8gb.xlar ge 4 4 1 1, 2, 3, 4 1 r8gb.2xla rge 8 8 1 1, 2, 3, 4, 5, 6, 7, 8 1 r8gb.4xla rge 16 16 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 1 r8gb.8xla rge 32 32 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core r8gb.12xl arge 48 48 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core r8gb.16xl arge 64 64 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core r8gb.24xl arge 96 96 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core r8gb.48xl arge 192 192 1 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100, 102, 104, 106, 108, 110, 112, 114, 116, 118, 120, 122, 124, 126, 128, 130, 132, 134, 136, 138, 140, 142, 144, 146, 148, 150, 152, 154, 156, 158, 160, 162, 164, 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core 166, 168, 170, 172, 174, 176, 178, 180, 182, 184, 186, 188, 190, 192 r8gd.larg e 2 2 1 1, 2 1 r8gd.xlar ge 4 4 1 1, 2, 3, 4 1 r8gd.2xla rge 8 8 1 1, 2, 3, 4, 5, 6, 7, 8 1 r8gd.4xla rge 16 16 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 1 r8gd.8xla rge 32 32 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core r8gd.12xl arge 48 48 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core r8gd.16xl arge 64 64 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core r8gd.24xl arge 96 96 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core r8gd.48xl arge 192 192 1 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100, 102, 104, 106, 108, 110, 112, 114, 116, 118, 120, 122, 124, 126, 128, 130, 132, 134, 136, 138, 140, 142, 144, 146, 148, 150, 152, 154, 156, 158, 160, 162, 164, 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core 166, 168, 170, 172, 174, 176, 178, 180, 182, 184, 186, 188, 190, 192 r8gn.larg e 2 2 1 1, 2 1 r8gn.xlar ge 4 4 1 1, 2, 3, 4 1 r8gn.2xla rge 8 8 1 1, 2, 3, 4, 5, 6, 7, 8 1 r8gn.4xla rge 16 16 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 1 r8gn.8xla rge 32 32 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core r8gn.12xl arge 48 48 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core r8gn.16xl arge 64 64 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core r8gn.24xl arge 96 96 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core r8gn.48xl arge 192 192 1 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100, 102, 104, 106, 108, 110, 112, 114, 116, 118, 120, 122, 124, 126, 128, 130, 132, 134, 136, 138, 140, 142, 144, 146, 148, 150, 152, 154, 156, 158, 160, 162, 164, 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core 166, 168, 170, 172, 174, 176, 178, 180, 182, 184, 186, 188, 190, 192 r8i.large 2 1 2 1 1, 2 r8i.xlarg e 4 2 2 1, 2 1, 2 r8i.2xlar ge 8 4 2 1, 2, 3, 4 1, 2 r8i.4xlar ge 16 8 2 1, 2, 3, 4, 5, 6, 7, 8 1, 2 r8i.8xlar ge 32 16 2 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 1, 2 r8i.12xla rge 48 24 2 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core r8i.16xla rge 64 32 2 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32 1, 2 r8i.24xla rge 96 48 2 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48 1, 2 r8i.32xla rge 128 64 2 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core r8i.48xla rge 192 96 2 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96 1, 2 r8i.96xla rge 384 192 2 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96, 102, 108, 114, 120, 126, 132, 138, 144, 150, 156, 162, 168, 174, 180, 186, 192 1, 2 r8id.larg e 2 1 2 1 1, 2 r8id.xlar ge 4 2 2 1, 2 1, 2 r8id.2xla rge 8 4 2 1, 2, 3, 4 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core r8id.4xla rge 16 8 2 1, 2, 3, 4, 5, 6, 7, 8 1, 2 r8id.8xla rge 32 16 2 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 1, 2 r8id.12xl arge 48 24 2 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24 1, 2 r8id.16xl arge 64 32 2 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core r8id.24xl arge 96 48 2 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48 1, 2 r8id.32xl arge 128 64 2 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64 1, 2 r8id.48xl arge 192 96 2 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core r8id.96xl arge 384 192 2 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96, 102, 108, 114, 120, 126, 132, 138, 144, 150, 156, 162, 168, 174, 180, 186, 192 1, 2 r8i-flex. large 2 1 2 1 1, 2 r8i-flex. xlarge 4 2 2 1, 2 1, 2 r8i-flex.
2xlarge 8 4 2 1, 2, 3, 4 1, 2 r8i-flex.
4xlarge 16 8 2 1, 2, 3, 4, 5, 6, 7, 8 1, 2 r8i-flex.
8xlarge 32 16 2 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core r8i-flex.
12xlarge 48 24 2 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24 1, 2 r8i-flex.
16xlarge 64 32 2 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32 1, 2 u-3tb1.56 xlarge 224 112 2 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76, 80, 84, 88, 92, 96, 100, 104, 108, 112 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core u-6tb1.56 xlarge 224 224 1 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 128, 136, 144, 152, 160, 168, 176, 184, 192, 200, 208, 216, 224 1 u-6tb1.11 2xlarge 448 224 2 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 128, 136, 144, 152, 160, 168, 176, 184, 192, 200, 208, 216, 224 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core u-9tb1.11 2xlarge 448 224 2 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 128, 136, 144, 152, 160, 168, 176, 184, 192, 200, 208, 216, 224 1, 2 u-12tb1.1 12xlarge 448 224 2 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 128, 136, 144, 152, 160, 168, 176, 184, 192, 200, 208, 216, 224 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core u-18tb1.1 12xlarge 448 224 2 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 128, 136, 144, 152, 160, 168, 176, 184, 192, 200, 208, 216, 224 1, 2 u-24tb1.1 12xlarge 448 224 2 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 128, 136, 144, 152, 160, 168, 176, 184, 192, 200, 208, 216, 224 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core u7i-6tb.1 12xlarge 448 224 2 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76, 80, 84, 88, 92, 96, 100, 104, 108, 112, 116, 120, 124, 128, 132, 136, 140, 144, 148, 152, 156, 160, 164, 168, 172, 176, 180, 184, 188, 192, 196, 200, 204, 208, 212, 216, 220, 224 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core u7i-8tb.1 12xlarge 448 224 2 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76, 80, 84, 88, 92, 96, 100, 104, 108, 112, 116, 120, 124, 128, 132, 136, 140, 144, 148, 152, 156, 160, 164, 168, 172, 176, 180, 184, 188, 192, 196, 200, 204, 208, 212, 216, 220, 224 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core u7i-12tb.
224xlarge 896 448 2 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 128, 136, 144, 152, 160, 168, 176, 184, 192, 200, 208, 216, 224, 232, 240, 248, 256, 264, 272, 280, 288, 296, 304, 312, 320, 328, 336, 344, 352, 360, 368, 376, 384, 392, 400, 408, 416, 424, 432, 440, 448 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core u7in-16tb .224xlarg e 896 448 2 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 128, 136, 144, 152, 160, 168, 176, 184, 192, 200, 208, 216, 224, 232, 240, 248, 256, 264, 272, 280, 288, 296, 304, 312, 320, 328, 336, 344, 352, 360, 368, 376, 384, 392, 400, 408, 416, 424, 432, 440, 448 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core u7in-24tb .224xlarg e 896 448 2 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 128, 136, 144, 152, 160, 168, 176, 184, 192, 200, 208, 216, 224, 232, 240, 248, 256, 264, 272, 280, 288, 296, 304, 312, 320, 328, 336, 344, 352, 360, 368, 376, 384, 392, 400, 408, 416, 424, 432, 440, 448 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core u7in-32tb .224xlarg e 896 448 2 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 128, 136, 144, 152, 160, 168, 176, 184, 192, 200, 208, 216, 224, 232, 240, 248, 256, 264, 272, 280, 288, 296, 304, 312, 320, 328, 336, 344, 352, 360, 368, 376, 384, 392, 400, 408, 416, 424, 432, 440, 448 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core u7inh-32t b.480xlar ge 1920 960 2 32, 48, 64, 80, 96, 112, 128, 144, 160, 176, 192, 208, 224, 240, 256, 272, 288, 304, 320, 336, 352, 368, 384, 400, 416, 432, 448, 464, 480, 496, 512, 528, 544, 560, 576, 592, 608, 624, 640, 656, 672, 688, 704, 720, 736, 752, 768, 784, 800, 816, 832, 848, 864, 880, 896, 912, 928, 944, 960 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core x1.16xlar ge 64 32 2 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32 1, 2 x1.32xlar ge 128 64 2 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64 1, 2 x1e.xlarg e 4 2 2 1, 2 1, 2 x1e.2xlar ge 8 4 2 1, 2, 3, 4 1, 2 x1e.4xlar ge 16 8 2 1, 2, 3, 4, 5, 6, 7, 8 1, 2 x1e.8xlar ge 32 16 2 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 1, 2 x1e.16xla rge 64 32 2 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core x1e.32xla rge 128 64 2 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64 1, 2 x2gd.larg e 2 2 1 1, 2 1 x2gd.xlar ge 4 4 1 1, 2, 3, 4 1 x2gd.2xla rge 8 8 1 1, 2, 3, 4, 5, 6, 7, 8 1 x2gd.4xla rge 16 16 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 1 x2gd.8xla rge 32 32 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core x2gd.12xl arge 48 48 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core x2gd.16xl arge 64 64 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64 1 x2idn.16x large 64 32 2 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core x2idn.24x large 96 48 2 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48 1, 2 x2idn.32x large 128 64 2 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64 1, 2 x2iedn.xl arge 4 2 2 1, 2 1, 2 x2iedn.2x large 8 4 2 2, 4 1, 2 x2iedn.4x large 16 8 2 2, 4, 6, 8 1, 2 x2iedn.8x large 32 16 2 2, 4, 6, 8, 10, 12, 14, 16 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core x2iedn.16 xlarge 64 32 2 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32 1, 2 x2iedn.24 xlarge 96 48 2 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48 1, 2 x2iedn.32 xlarge 128 64 2 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64 1, 2 x2iezn.2x large 8 4 2 2, 4 1, 2 x2iezn.4x large 16 8 2 2, 4, 6, 8 1, 2 x2iezn.6x large 24 12 2 2, 4, 6, 8, 10, 12 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core x2iezn.8x large 32 16 2 2, 4, 6, 8, 10, 12, 14, 16 1, 2 x2iezn.12 xlarge 48 24 2 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24 1, 2 x8g.large 2 2 1 1, 2 1 x8g.xlarg e 4 4 1 1, 2, 3, 4 1 x8g.2xlar ge 8 8 1 1, 2, 3, 4, 5, 6, 7, 8 1 x8g.4xlar ge 16 16 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 1 x8g.8xlar ge 32 32 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core x8g.12xla rge 48 48 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core x8g.16xla rge 64 64 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core x8g.24xla rge 96 96 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core x8g.48xla rge 192 192 1 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100, 102, 104, 106, 108, 110, 112, 114, 116, 118, 120, 122, 124, 126, 128, 130, 132, 134, 136, 138, 140, 142, 144, 146, 148, 150, 152, 154, 156, 158, 160, 162, 164, 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core 166, 168, 170, 172, 174, 176, 178, 180, 182, 184, 186, 188, 190, 192 x8aedz.la rge 2 2 1 1, 2 1 x8aedz.xl arge 4 4 1 1, 2, 3, 4 1 x8aedz.3x large 12 12 1 1, 2, 4, 6, 8, 10, 12 1 x8aedz.6x large 24 24 1 1, 2, 3, 4, 8, 12, 16, 20, 24 1 x8aedz.12 xlarge 48 48 1 1, 2, 3, 4, 5, 6, 7, 8, 16, 24, 32, 40, 48 1 x8aedz.24 xlarge 96 96 1 4, 6, 8, 10, 12, 14, 16, 32, 48, 64, 80, 96 1 x8i.large 2 1 2 1 1, 2 x8i.xlarg e 4 2 2 1, 2 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core x8i.2xlar ge 8 4 2 1, 2, 3, 4 1, 2 x8i.4xlar ge 16 8 2 1, 2, 3, 4, 5, 6, 7, 8 1, 2 x8i.8xlar ge 32 16 2 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 1, 2 x8i.12xla rge 48 24 2 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24 1, 2 x8i.16xla rge 64 32 2 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core x8i.24xla rge 96 48 2 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48 1, 2 x8i.32xla rge 128 64 2 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64 1, 2 x8i.48xla rge 192 96 2 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core x8i.64xla rge 256 128 2 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76, 80, 84, 88, 92, 96, 100, 104, 108, 112, 116, 120, 124, 128 1, 2 x8i.96xla rge 384 192 2 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96, 102, 108, 114, 120, 126, 132, 138, 144, 150, 156, 162, 168, 174, 180, 186, 192 1, 2 z1d.large 2 1 2 1 1, 2 z1d.xlarg e 4 2 2 1, 2 1, 2 z1d.2xlar ge 8 4 2 2, 4 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core z1d.3xlar ge 12 6 2 2, 4, 6 1, 2 z1d.6xlar ge 24 12 2 2, 4, 6, 8, 10, 12 1, 2 z1d.12xla rge 48 24 2 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24 1, 2
#### Storage optimized instances Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core d2.xlarge 4 2 2 1, 2 1, 2 d2.2xlarg e 8 4 2 1, 2, 3, 4 1, 2 d2.4xlarg e 16 8 2 1, 2, 3, 4, 5, 6, 7, 8 1, 2 d2.8xlarg e 36 18 2 2, 4, 6, 8, 10, 12, 14, 16, 18 1, 2 d3.xlarge 4 2 2 1, 2 1, 2 d3.2xlarg e 8 4 2 2, 4 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core d3.4xlarg e 16 8 2 2, 4, 6, 8 1, 2 d3.8xlarg e 32 16 2 2, 4, 6, 8, 10, 12, 14, 16 1, 2 d3en.xlar ge 4 2 2 1, 2 1, 2 d3en.2xla rge 8 4 2 2, 4 1, 2 d3en.4xla rge 16 8 2 2, 4, 6, 8 1, 2 d3en.6xla rge 24 12 2 2, 4, 6, 8, 10, 12 1, 2 d3en.8xla rge 32 16 2 2, 4, 6, 8, 10, 12, 14, 16 1, 2 d3en.12xl arge 48 24 2 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24 1, 2 h1.2xlarg e 8 4 2 1, 2, 3, 4 1, 2 h1.4xlarg e 16 8 2 1, 2, 3, 4, 5, 6, 7, 8 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core h1.8xlarg e 32 16 2 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 1, 2 h1.16xlar ge 64 32 2 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32 1, 2 i2.xlarge 4 2 2 1, 2 1, 2 i2.2xlarg e 8 4 2 1, 2, 3, 4 1, 2 i2.4xlarg e 16 8 2 1, 2, 3, 4, 5, 6, 7, 8 1, 2 i2.8xlarg e 32 16 2 2, 4, 6, 8, 10, 12, 14, 16 1, 2 i3.large 2 1 2 1 1, 2 i3.xlarge 4 2 2 1, 2 1, 2 i3.2xlarg e 8 4 2 1, 2, 3, 4 1, 2 i3.4xlarg e 16 8 2 1, 2, 3, 4, 5, 6, 7, 8 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core i3.8xlarg e 32 16 2 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 1, 2 i3.16xlar ge 64 32 2 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32 1, 2 i3en.larg e 2 1 2 1 1, 2 i3en.xlar ge 4 2 2 1, 2 1, 2 i3en.2xla rge 8 4 2 2, 4 1, 2 i3en.3xla rge 12 6 2 2, 4, 6 1, 2 i3en.6xla rge 24 12 2 2, 4, 6, 8, 10, 12 1, 2 i3en.12xl arge 48 24 2 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core i3en.24xl arge 96 48 2 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48 1, 2 i4g.large 2 2 1 1, 2 1 i4g.xlarg e 4 4 1 1, 2, 3, 4 1 i4g.2xlar ge 8 8 1 1, 2, 3, 4, 5, 6, 7, 8 1 i4g.4xlar ge 16 16 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 1 i4g.8xlar ge 32 32 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core i4g.16xla rge 64 64 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64 1 i4i.large 2 1 2 1 1, 2 i4i.xlarg e 4 2 2 1, 2 1, 2 i4i.2xlar ge 8 4 2 1, 2, 3, 4 1, 2 i4i.4xlar ge 16 8 2 1, 2, 3, 4, 5, 6, 7, 8 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core i4i.8xlar ge 32 16 2 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 1, 2 i4i.12xla rge 48 24 2 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24 1, 2 i4i.16xla rge 64 32 2 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32 1, 2 i4i.24xla rge 96 48 2 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core i4i.32xla rge 128 64 2 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64 1, 2 i7i.large 2 1 2 1 1, 2 i7i.xlarg e 4 2 2 1, 2 1, 2 i7i.2xlar ge 8 4 2 1, 2, 3, 4 1, 2 i7i.4xlar ge 16 8 2 1, 2, 3, 4, 5, 6, 7, 8 1, 2 i7i.8xlar ge 32 16 2 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 1, 2 i7i.12xla rge 48 24 2 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core i7i.16xla rge 64 32 2 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32 1, 2 i7i.24xla rge 96 48 2 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core i7i.48xla rge 192 96 2 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96 1, 2 i7ie.larg e 2 1 2 1 1, 2 i7ie.xlar ge 4 2 2 1, 2 1, 2 i7ie.2xla rge 8 4 2 1, 2, 3, 4 1, 2 i7ie.3xla rge 12 6 2 1, 2, 3, 4, 5, 6 1, 2 i7ie.6xla rge 24 12 2 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core i7ie.12xl arge 48 24 2 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24 1, 2 i7ie.18xl arge 72 36 2 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core i7ie.24xl arge 96 48 2 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48 1, 2 i7ie.48xl arge 192 96 2 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core i8g.large 2 2 1 1, 2 1 i8g.xlarg e 4 4 1 1, 2, 3, 4 1 i8g.2xlar ge 8 8 1 1, 2, 3, 4, 5, 6, 7, 8 1 i8g.4xlar ge 16 16 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 1 i8g.8xlar ge 32 32 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core i8g.12xla rge 48 48 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core i8g.16xla rge 64 64 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core i8g.24xla rge 96 96 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core i8g.48xla rge 192 192 1 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100, 102, 104, 106, 108, 110, 112, 114, 116, 118, 120, 122, 124, 126, 128, 130, 132, 134, 136, 138, 140, 142, 144, 146, 148, 150, 152, 154, 156, 158, 160, 162, 164, 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core 166, 168, 170, 172, 174, 176, 178, 180, 182, 184, 186, 188, 190, 192 i8ge.larg e 2 2 1 1, 2 1 i8ge.xlar ge 4 4 1 1, 2, 3, 4 1 i8ge.2xla rge 8 8 1 1, 2, 3, 4, 5, 6, 7, 8 1 i8ge.3xla rge 12 12 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 1 i8ge.6xla rge 24 24 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core i8ge.12xl arge 48 48 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core i8ge.18xl arge 72 72 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core i8ge.24xl arge 96 96 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core i8ge.48xl arge 192 192 1 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100, 102, 104, 106, 108, 110, 112, 114, 116, 118, 120, 122, 124, 126, 128, 130, 132, 134, 136, 138, 140, 142, 144, 146, 148, 150, 152, 154, 156, 158, 160, 162, 164, 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core 166, 168, 170, 172, 174, 176, 178, 180, 182, 184, 186, 188, 190, 192 im4gn.lar ge 2 2 1 1, 2 1 im4gn.xla rge 4 4 1 1, 2, 3, 4 1 im4gn.2xl arge 8 8 1 1, 2, 3, 4, 5, 6, 7, 8 1 im4gn.4xl arge 16 16 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 1 im4gn.8xl arge 32 32 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core im4gn.16x large 64 64 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64 1 is4gen.me dium 1 1 1 1 1 is4gen.la rge 2 2 1 1, 2 1 is4gen.xl arge 4 4 1 1, 2, 3, 4 1 is4gen.2x large 8 8 1 1, 2, 3, 4, 5, 6, 7, 8 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core is4gen.4x large 16 16 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 1 is4gen.8x large 32 32 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32 1
#### Accelerated computing instances Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core dl1.24xla rge 96 48 2 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core dl2q.24xl arge 96 48 2 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48 1, 2 f1.2xlarg e 8 4 2 1, 2, 3, 4 1, 2 f1.4xlarg e 16 8 2 1, 2, 3, 4, 5, 6, 7, 8 1, 2 f1.16xlar ge 64 32 2 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32 1, 2 f2.6xlarg e 24 12 2 1, 2, 3, 6, 9, 12 1, 2 f2.12xlar ge 48 24 2 1, 2, 3, 6, 9, 12, 15, 18, 21, 24 1, 2 f2.48xlar ge 192 96 2 4, 6, 8, 10, 12, 24, 36, 48, 60, 72, 84, 96 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core g3.4xlarg e 16 8 2 1, 2, 3, 4, 5, 6, 7, 8 1, 2 g3.8xlarg e 32 16 2 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 1, 2 g3.16xlar ge 64 32 2 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32 1, 2 g4ad.xlar ge 4 2 2 2 1, 2 g4ad.2xla rge 8 4 2 2, 4 1, 2 g4ad.4xla rge 16 8 2 2, 4, 8 1, 2 g4ad.8xla rge 32 16 2 2, 4, 8, 16 1, 2 g4ad.16xl arge 64 32 2 2, 4, 8, 16, 32 1, 2 g4dn.xlar ge 4 2 2 2 1, 2 g4dn.2xla rge 8 4 2 2, 4 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core g4dn.4xla rge 16 8 2 2, 4, 6, 8 1, 2 g4dn.8xla rge 32 16 2 2, 4, 6, 8, 10, 12, 14, 16 1, 2 g4dn.12xl arge 48 24 2 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24 1, 2 g4dn.16xl arge 64 32 2 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32 1, 2 g5g.xlarg e 4 4 1 1, 2, 3, 4 1 g5g.2xlar ge 8 8 1 1, 2, 3, 4, 5, 6, 7, 8 1 g5g.4xlar ge 16 16 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core g5g.8xlar ge 32 32 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32 1 g5g.16xla rge 64 64 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64 1 g6.xlarge 4 2 2 1, 2 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core g6.2xlarg e 8 4 2 1, 2, 3, 4 1, 2 g6.4xlarg e 16 8 2 1, 2, 3, 4, 5, 6, 7, 8 1, 2 g6.8xlarg e 32 16 2 1, 2, 4, 6, 8, 10, 12, 14, 16 1, 2 g6.12xlar ge 48 24 2 1, 2, 3, 6, 9, 12, 15, 18, 21, 24 1, 2 g6.16xlar ge 64 32 2 1, 2, 3, 4, 8, 12, 16, 20, 24, 28, 32 1, 2 g6.24xlar ge 96 48 2 1, 2, 3, 4, 5, 6, 12, 18, 24, 30, 36, 42, 48 1, 2 g6.48xlar ge 192 96 2 4, 6, 8, 10, 12, 24, 36, 48, 60, 72, 84, 96 1, 2 g6e.xlarg e 4 2 2 1, 2 1, 2 g6e.2xlar ge 8 4 2 1, 2, 3, 4 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core g6e.4xlar ge 16 8 2 1, 2, 3, 4, 5, 6, 7, 8 1, 2 g6e.8xlar ge 32 16 2 2, 4, 6, 8, 10, 12, 14, 16 1, 2 g6e.12xla rge 48 24 2 3, 6, 9, 12, 15, 18, 21, 24 1, 2 g6e.16xla rge 64 32 2 4, 8, 12, 16, 20, 24, 28, 32 1, 2 g6e.24xla rge 96 48 2 6, 12, 18, 24, 30, 36, 42, 48 1, 2 g6e.48xla rge 192 96 2 12, 24, 36, 48, 60, 72, 84, 96 1, 2 g6f.large 2 1 2 1 1, 2 g6f.xlarg e 4 2 2 1, 2 1, 2 g6f.2xlar ge 8 4 2 1, 2, 3, 4 1, 2 g6f.4xlar ge 16 8 2 1, 2, 3, 4, 5, 6, 7, 8 1, 2 gr6.4xlar ge 16 8 2 1, 2, 3, 4, 5, 6, 7, 8 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core gr6.8xlar ge 32 16 2 1, 2, 4, 6, 8, 10, 12, 14, 16 1, 2 gr6f.4xla rge 16 8 2 1, 2, 3, 4, 5, 6, 7, 8 1, 2 g7e.2xlar ge 8 4 2 1, 2, 3, 4 1, 2 g7e.4xlar ge 16 8 2 1, 2, 3, 4, 5, 6, 7, 8 1, 2 g7e.8xlar ge 32 16 2 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 1, 2 g7e.12xla rge 48 24 2 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core g7e.24xla rge 96 48 2 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48 1, 2 g7e.48xla rge 192 96 2 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core inf1.xlar ge 4 2 2 2 1, 2 inf1.2xla rge 8 4 2 2, 4 1, 2 inf1.6xla rge 24 12 2 2, 4, 6, 8, 10, 12 1, 2 inf1.24xl arge 96 48 2 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48 1, 2 inf2.xlar ge 4 2 2 1, 2 1, 2 inf2.8xla rge 32 16 2 4, 6, 8, 10, 12, 14, 16 1, 2 inf2.24xl arge 96 48 2 4, 6, 8, 10, 12, 14, 16, 32, 48 1, 2 inf2.48xl arge 192 96 2 4, 8, 12, 16, 20, 24, 28, 32, 64, 96 1, 2 p3.2xlarg e 8 4 2 1, 2, 3, 4 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core p3.8xlarg e 32 16 2 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 1, 2 p3.16xlar ge 64 32 2 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32 1, 2 p3dn.24xl arge 96 48 2 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48 1, 2 p4d.24xla rge 96 48 2 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core p4de.24xl arge 96 48 2 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48 1, 2 p5.4xlarg e 16 8 2 1, 2, 3, 4, 5, 6, 7, 8 1, 2 p5.48xlar ge 192 96 2 12, 24, 36, 48, 60, 72, 84, 96 1, 2 p5e.48xla rge 192 96 2 12, 24, 36, 48, 60, 72, 84, 96 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core p5en.48xl arge 192 96 2 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core p6-b200.4 8xlarge 192 96 2 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core p6-b300.4 8xlarge 192 96 2 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core p6e-gb200 .36xlarge 144 144 1 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 1

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144 trn1.2xla rge 8 4 2 2, 4 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core trn1.32xl arge 128 64 2 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64 1, 2 trn1n.32x large 128 64 2 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64 1, 2 trn2.3xla rge 12 6 2 1, 2, 3, 4, 5, 6 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core trn2.48xl arge 192 96 2 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96 1, 2

Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core trn2u.48x large 192 96 2 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96 1, 2 vt1.3xlar ge 12 6 2 6 1, 2 vt1.6xlar ge 24 12 2 6, 12 1, 2 vt1.24xla rge 96 48 2 6, 12, 48 1, 2

#### High-performance computing instances Instance type Default vCPUs Default CPU cores Default threads per core Valid CPU cores Valid threads per core hpc6id.32 xlarge 64 64 1 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64 1 hpc8a.96x large 192 192 1 24, 48, 72, 96, 120, 144, 168, 192 1
### Specify CPU options for an Amazon EC2 instance You can specify CPU options during or after instance launch.
Tasks
- Disable simultaneous multithreading
- Specify a custom number of vCPUs at launch
- Specify a custom number of vCPUs in a launch template
- Change CPU options for your EC2 instance
#### Disable simultaneous multithreading To disable simultaneous multithreading (SMT), also known as hyper-threading, specify 1 thread per core.

Console To disable SMT during instance launch
1. Follow the Launch an EC2 instance using the launch instance wizard in the console procedure and configure your instance as needed.
2. Expand Advanced details, and select the Specify CPU options checkbox.
3. For Core count, choose the number of required CPU cores. In this example, to specify the default CPU core count for an r5.4xlarge instance, choose 8.
4. To disable SMT, for Threads per core, choose 1.
5. In the Summary panel, review your instance configuration, and then choose Launch instance. For more information, see Launch an EC2 instance using the launch instance wizard in the console.
AWS CLI To disable SMT during instance launch Use the run-instances AWS CLI command and specify a value of 1 for ThreadsPerCore for the --cpu-options parameter. For CoreCount, specify the number of CPU cores. In this example, to specify the default CPU core count for an r7i.4xlarge instance, specify a value of 8. aws ec2 run-instances \ --image-id ami-0abcdef1234567890 \ --instance-type r7i.4xlarge \ --cpu-options "CoreCount=8,ThreadsPerCore=1" \ --key-name my-key-pair PowerShell To disable SMT during instance launch Use the New-EC2Instance command and specify a value of 1 for ThreadsPerCore for the - CpuOptions parameter. For CoreCount, specify the number of CPU cores. In this example, to specify the default CPU core count for an r7i.4xlarge instance, specify a value of 8.
New-EC2Instance `
    -ImageId 'ami-0abcdef1234567890' `
    -InstanceType 'r7i.4xlarge' `
    -CpuOptions @{CoreCount=8; ThreadsPerCore=1} `

    -KeyName 'my-key-pair'
Note To disable SMT for an existing instance, follow the process shown in Change CPU options for your EC2 instance, and change the number of threads that run per core to 1.
#### Specify a custom number of vCPUs at launch You can customize the number of CPU cores and threads per core when you launch an instance from the EC2 console or AWS CLI. The examples in this section use an r5.4xlarge instance type, which has the following default settings:
- CPU cores: 8
- Threads per core: 2 Instances launch with the maximum number of vCPUs available for the instance type by default.
For this instance type, that's 16 total vCPUs (8 cores running 2 threads each). For more information about this instance type, see Memory optimized instances.
The following example launches an r5.4xlarge instance with 4 vCPUs.
Console To specify a custom number of vCPUs during instance launch
1. Follow the Launch an EC2 instance using the launch instance wizard in the console procedure and configure your instance as needed.
2. Expand Advanced details, and select the Specify CPU options checkbox.
3. To get 4 vCPUs, specify 2 CPU cores and 2 threads per core, as follows:
- For Core count, choose 2.
- For Threads per core, choose 2.
4. In the Summary panel, review your instance configuration, and then choose Launch instance. For more information, see Launch an EC2 instance using the launch instance wizard in the console.

AWS CLI To specify a custom number of vCPUs during instance launch Use the run-instances AWS CLI command and specify the number of CPU cores and number of threads in the --cpu-options parameter. You can specify 2 CPU cores and 2 threads per core to get 4 vCPUs. aws ec2 run-instances \ --image-id ami-0abcdef1234567890 \ --instance-type r7i.4xlarge \ --cpu-options "CoreCount=2,ThreadsPerCore=2" \ --key-name my-key-pair Alternatively, specify 4 CPU cores and 1 thread per core (disable SMT) to get 4 vCPUs: aws ec2 run-instances \ --image-id ami-0abcdef1234567890 \ --instance-type r7i.4xlarge \ --cpu-options "CoreCount=4,ThreadsPerCore=1" \ --key-name my-key-pair PowerShell To specify a custom number of vCPUs during instance launch Use the New-EC2Instance command and specify the number of CPU cores and number of threads in the -CpuOptions parameter. You can specify 2 CPU cores and 2 threads per core to get 4 vCPUs.
New-EC2Instance `
    -ImageId 'ami-0abcdef1234567890' `
    -InstanceType 'r7i.4xlarge' `
    -CpuOptions @{CoreCount=2; ThreadsPerCore=2} `
    -KeyName 'my-key-pair'
Alternatively, specify 4 CPU cores and 1 thread per core (disable SMT) to get 4 vCPUs:
New-EC2Instance `
    -ImageId 'ami-0abcdef1234567890' `
    -InstanceType 'r7i.4xlarge' `

    -CpuOptions @{CoreCount=4; ThreadsPerCore=1} `
    -KeyName 'my-key-pair'
#### Specify a custom number of vCPUs in a launch template You can customize the number of CPU cores and threads per core for the instance in a launch template. The examples in this section use an r5.4xlarge instance type, which has the following default settings:
- CPU cores: 8
- Threads per core: 2 Instances launch with the maximum number of vCPUs available for the instance type by default.
For this instance type, that's 16 total vCPUs (8 cores running 2 threads each). For more information about this instance type, see Memory optimized instances.
The following example creates a launch template that specifies the configuration for an r5.4xlarge instance with 4 vCPUs.
Console To specify a custom number of vCPUs in a launch template
1. Follow the Create a launch template by specifying parameters procedure and configure your launch template as needed.
2. Expand Advanced details, and select the Specify CPU options checkbox.
3. To get 4 vCPUs, specify 2 CPU cores and 2 threads per core, as follows:
- For Core count, choose 2.
- For Threads per core, choose 2.
4. In the Summary panel, review your instance configuration, and then choose Create launch template. For more information, see Store instance launch parameters in Amazon EC2 launch templates.
AWS CLI To specify a custom number of vCPUs in a launch template

Use the create-launch-template AWS CLI command and specify the number of CPU cores and number of threads in the CpuOptions parameter. You can specify 2 CPU cores and 2 threads per core to get 4 vCPUs. aws ec2 create-launch-template \ --launch-template-name TemplateForCPUOptions \ --version-description CPUOptionsVersion1 \ --launch-template-data file://template-data.json The following is an example JSON file that contains the launch template data, which includes the CPU options, for the instance configuration for this example.
{ "NetworkInterfaces": [{ "AssociatePublicIpAddress": true, "DeviceIndex": 0, "Ipv6AddressCount": 1, "SubnetId": "subnet-0abcdef1234567890"
    }], "ImageId": "ami-0abcdef1234567890", "InstanceType": "r5.4xlarge", "TagSpecifications": [{ "ResourceType": "instance", "Tags": [{ "Key":"Name", "Value":"webserver"
        }]
    }], "CpuOptions": { "CoreCount":2, "ThreadsPerCore":2 } } Alternatively, specify 4 CPU cores and 1 thread per core (disable SMT) to get 4 vCPUs:
{ "NetworkInterfaces": [{ "AssociatePublicIpAddress": true, "DeviceIndex": 0, "Ipv6AddressCount": 1, "SubnetId": "subnet-0abcdef1234567890"

    }], "ImageId": "ami-0abcdef1234567890", "InstanceType": "r5.4xlarge", "TagSpecifications": [{ "ResourceType": "instance", "Tags": [{ "Key":"Name", "Value":"webserver"
        }]
    }], "CpuOptions": { "CoreCount":4, "ThreadsPerCore":1 } } PowerShell To specify a custom number of vCPUs in a launch template Use the New-EC2LaunchTemplate.
New-EC2LaunchTemplate `
    -LaunchTemplateName 'TemplateForCPUOptions' `
    -VersionDescription 'CPUOptionsVersion1' `
    -LaunchTemplateData (Get-Content -Path 'template-data.json' | ConvertFrom-Json)
#### Change CPU options for your EC2 instance As your needs change over time, you might want to change the configuration of CPU options for an existing instance. Each thread that runs on your instance is known as a virtual CPU (vCPU). You can change the number of vCPUs that run for an existing instance in the Amazon EC2 console, AWS CLI, API, or SDKs. The instance state must be Stopped before you can make this change.
To view console or command line steps, select the tab that matches your environment. For API request and response information, see ModifyInstanceCpuOptions in the Amazon EC2 API Reference.
Console Follow this procedure to change the number of active vCPUs for your instance from the AWS Management Console.

1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the left navigation pane, choose Instances. This opens the list of instances that are defined for the current AWS Region.
3. Select the instance from the Instances list. Alternatively, you can select the instance link to open the instance detail page.
4. If the instance is running, you must stop it before you proceed. Choose Stop instance from the Instance state menu.
5. To change the vCPU configuration, choose Change CPU options from Instance settings in the Actions menu. This opens the Change CPU options page.
6. Choose one of the following CPU options to change the configuration for your instance.
Use default CPU options This option resets your instance to the default number of vCPUs for the instance type.
The default is to run all threads for all CPU cores.
Specify CPU options This option enables configuration of the number of vCPUs that are running on your instance.
7. If you chose Specify CPU options, the Active vCPUs fields are displayed.
- Use the first selector to configure the number of threads for each CPU core. To disable simultaneous multithreading, choose 1.
- Use the second selector to configure the number of CPUs that run on your instance.
The following fields dynamically update as you make changes to the CPU option selectors.
- Active vCPUs: The number of CPU cores multiplied by the threads per core, based on the selections that you made. For example, if you selected 2 threads and 4 cores, that would equal 8 vCPUs.
- Total vCPUs: The maximum number of vCPUs for the instance type. For example, for an m6i.4xlarge instance type, this is 16 vCPUs (8 cores running 2 threads each).
8. To apply your updates, choose Change.

AWS CLI Follow this procedure to change the number of active vCPUs for your instance from the AWS CLI.
Use the modify-instance-cpu-options command and specify the number of CPU cores that run in the --core-count parameter, and the number of threads that run per core in the -- threads-per-core parameter.
The following examples show two possible configurations on an m6i.4xlarge instance type to run 8 vCPUs on the specified instance. The default for this instance type is 16 vCPUs (8 cores running 2 threads each).
Example 1: Run 4 CPU cores with 2 threads per core, for a total of 8 vCPU. aws ec2 modify-instance-cpu-options \ --instance-id i-1234567890abcdef0 \ --core-count=4 \ --threads-per-core=2 Example 2: Disable simultaneous multi-threading by changing the number of threads that run per core to 1. The resulting configuration also runs a total of 8 vCPUs (8 CPU cores with 1 thread per core). aws ec2 modify-instance-cpu-options \ --instance-id 1234567890abcdef0 \ --core-count=8 \ --threads-per-core=1 PowerShell To change the number of active vCPUs for an instance Use the Edit-EC2InstanceCpuOption cmdlet and specify the number of CPU cores that run in the -CoreCount parameter, and the number of threads that run per core in the ThreadsPerCore parameter.
Example 1: Run 4 CPU cores with 2 threads per core, for a total of 8 vCPU.
Edit-EC2InstanceCpuOption `
    -InstanceId 'i-1234567890abcdef0' `

    -CoreCount 4 `
    -ThreadsPerCore 2 Example 2: Disable simultaneous multi-threading by changing the number of threads that run per core to 1. The resulting configuration also runs a total of 8 vCPUs (8 CPU cores with 1 thread per core).
Edit-EC2InstanceCpuOption `
    -InstanceId 'i-1234567890abcdef0' `
    -CoreCount 8 `
    -ThreadsPerCore 1
### View CPU threads and cores for an Amazon EC2 instance You can view the CPU options for an existing instance by describing the instance.
Console To view the CPU options for an instance
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the left navigation pane, choose Instances and select the instance.
3. On the Details tab, under Host and placement group, find Number of vCPUs.
AWS CLI To view the CPU options for an instance Use the describe-instances command. aws ec2 describe-instances \ --instance-ids i-1234567890abcdef0 \ --query Reservations[].Instances[].CpuOptions The following is example output. The CoreCount field indicates the number of cores for the instance. The ThreadsPerCore field indicates the number of threads per core.
[ {

        "CoreCount": 24, "ThreadsPerCore": 2 }, ]
PowerShell To view the CPU options for an instance Use the Get-EC2Instance cmdlet.
(Get-EC2Instance `
    -InstanceId 'i-1234567890abcdef0').Instances.CpuOptions The following is example output.
AmdSevSnp CoreCount ThreadsPerCore --------- --------- -------------- 24        2 Alternatively, to view CPU information, you can connect to your instance and use one of the following system tools:
- Windows Task Manager on your Windows instance
- The lscpu command on your Linux instance You can use AWS Config to record, assess, audit, and evaluate configuration changes for instances, including terminated instances. For more information, see Getting Started with AWS Config in the AWS Config Developer Guide.
### Optimize CPUs for License-Included instances Workloads such as Microsoft SQL Server often require high levels of memory and IOPS but a low vCPU count. AWS provides a broad set of instance types that can cover most of your infrastructure needs. However, to reduce vCPU-based licensing costs for Windows and Microsoft SQL Server, you can customize the number of vCPUs running on your EC2 instance while maintaining the same memory and IOPS. To configure CPU options on your instance and save on vCPU-based licensing costs for both license-included and Bring-Your-Own-License (BYOL) workloads, use the Optimize CPUs feature.

For more information, see this blog post about best practices to optimize CPUs for SQL Server workloads.
#### Supported license types Optimize CPUs supports billing based on the number of active CPUs for the following types of license configurations for instances launched from a license-included AMI. For more information about license types, see AMI billing information fields.
License-included AMI instance billing Licenses included Usage operation Price per vCPU hour Windows Server RunInstances:0002 $0.046 Windows Server with SQL Server Enterprise RunInstances:0102 $0.421 Windows Server with SQL Server Standard RunInstances:0006 $0.166 Windows Server with SQL Server Web RunInstances:0202 $0.063
#### Supported purchasing options Optimize CPUs supports the following purchasing options for license included instances:
- On-Demand
- Savings Plans Warning If you use Reserved Instances, discounts may not be applied when you configure Optimize CPUs for license included instances in the same payer account. We recommend that you

use Savings Plans to reduce vCPU-based licensing costs and provide comparable savings on your compute costs.
Accounts that used both Optimize CPUs and Reserved Instances for Windows and SQL Server on the same instance type before October 15, 2025, were added to an opt-out list to maintain their current billing experience. To take advantage of Optimize CPU license savings, contact the AWS Support Center to be removed from the opt-out list.
#### How Optimize CPUs works to save on licensing fees The following examples help to illustrate the cost savings that are possible when you configure your CPU usage.
Example 1: Default billing This example shows an r7i.8xlarge instance launched from a license- included Windows and SQL Server Enterprise AMI that ran for 100 hours with the default CPU configuration of 32 vCPUs for the instance type (3200 vCPU hours).
The bill shows one line item with a combined rate that includes both usage and licensing fees.
Example 2: Optimize CPUs billing This example shows an r7i.8xlarge instance launched from a license-included Windows and SQL Server Enterprise AMI. To save on license fees, the number of CPUs that are active was reduced to 16 vCPUs. Then the instance ran for 100 hours with the new configuration.
The bill shows the following two line items.
Billing description: Elastic Compute Cloud The first line item shows the baseline cost of the Windows and SQL Server instance that ran for 100 hours ($211.68).
Billing description: Amazon EC2 Optimize CPU License Included Third Party Fees The second line item covers licensing fees based on the number of vCPUs that were active for the billing period ($673.60).

Example 3: Optimize CPUs billing with Savings Plans This example shows an r7i.8xlarge instance launched from a license-included Windows and SQL Server Enterprise AMI. To save on license fees, the number of CPUs that are active was reduced to 16 vCPUs. Then the instance ran for 100 hours with the new configuration.
A one year No Upfront Compute Savings Plan with a $1.60/hour (rounded) commitment provides further cost savings that reduce the baseline cost of the Windows and SQL Server instance. The Savings Plan commitment covers the full 100 hour usage of the r7i.8xlarge instance for a Savings Plans rate of $1.53362/hour.
The bill shows the following line items.
Billing description: Savings Plans for Compute usage The first line item shows the Savings Plan commitment for the full 100 hour usage ($160.00).
Billing description: Elastic Compute Cloud The second line item contains two entries. The first entry shows what the baseline cost of the Windows and SQL Server instance that ran for 100 hours would have been without the Savings Plan ($211.68). The second entry shows that the full baseline cost was covered by the Compute Savings Plan (-$211.68), which yields a net cost of zero for this line item.
Billing description: Amazon EC2 Optimize CPU License Included Third Party Fees The third line item covers licensing fees based on the number of vCPUs that were active for the billing period ($673.60).

## AMD SEV-SNP for Amazon EC2 instances AMD Secure Encrypted Virtualization-Secure Nested Paging (AMD SEV-SNP) is a CPU feature that provides the following properties:
- Attestation – AMD SEV-SNP enables you to retrieve a signed attestation report that contains a cryptographic measure that can be used to validate the instance's state and identity, and that it is running on genuine AMD hardware. For more information, see Attest an Amazon EC2 instance with AMD SEV-SNP.
- Memory encryption – Starting with AMD EPYC (Milan), AWS Graviton2, and Intel Xeon Scalable (Ice Lake) processors, instance memory is always encrypted. Instances that are enabled for AMD SEV-SNP use an instance-specific key for their memory encryption.
Contents
- Concepts and terminology
- Requirements
- Considerations
- Pricing
- Find EC2 instance types that support AMD SEV-SNP
- Enable AMD SEV-SNP for an EC2 instance
- Attest an Amazon EC2 instance with AMD SEV-SNP

### Concepts and terminology Before you begin using AMD SEV-SNP, ensure that you are familiar with the following concepts and terminology.
AMD SEV-SNP attestation report The AMD SEV-SNP attestation report is a document that an instance can request from the CPU.
The AMD SEV-SNP attestation report can be used to validate the state and identity of an instance, and to verify that it is running in a sanctioned AMD environment. The report includes a launch measurement, which is a cryptographic hash of the initial boot state of an instance, including its initial instance memory contents and initial state of the vCPUs. The AMD SEV-SNP attestation report is signed with a VLEK signature that chains back to an AMD root of trust.
VLEK The Versioned Loaded Endorsement Key (VLEK) is a versioned signing key that is certified by AMD and used by the AMD CPU to sign the AMD SEV-SNP attestation reports. VLEK signatures can be validated using certificates provided by AMD.
OVMF binary The Open Virtual Machine Firmware (OVMF) is the early-boot code that is used to provide a UEFI environment for the instance. The early-boot code is run before the code in the AMI is booted.
The OVMF also finds and runs the boot loader provided in the AMI. For more information, see the OVMF repository.
### Requirements To use AMD SEV-SNP, you must do the following:
- Use one of the following supported instance types:
- General purpose: m6a.large | m6a.xlarge | m6a.2xlarge | m6a.4xlarge | m6a.8xlarge
- Compute optimized: c6a.large | c6a.xlarge | c6a.2xlarge | c6a.4xlarge | c6a.8xlarge | c6a.12xlarge | c6a.16xlarge
- Memory optimized: r6a.large | r6a.xlarge | r6a.2xlarge | r6a.4xlarge
- Launch your instance in a supported AWS Region. Currently, only US East (Ohio) and Europe (Ireland) are supported.

- Use an AMI with uefi or uefi-preferred boot mode and an operating system that supports AMD SEV-SNP. For more information about AMD SEV-SNP support on your operating system, refer to the respective operating system's documentation. For AWS, AMD SEV-SNP is supported on AL2023, RHEL 9.3, SLES 15 SP4, and Ubuntu 23.04 and later.
Considerations You can only enable AMD SEV-SNP when you launch an instance. When AMD SEV-SNP is enabled for your instance launch, the following rules apply.
- After it is enabled, AMD SEV-SNP can't be disabled. It remains enabled throughout the instance lifecycle.
- You can only change the instance type to another instance type that supports AMD SEV-SNP.
- Hibernation and Nitro Enclaves aren't supported.
- Dedicated Hosts aren't supported.
- If the underlying host for your instance is scheduled for maintenance, you'll receive a scheduled event notification 14 days before the event. You must manually stop or restart your instance to move it to a new host.
Pricing When you launch an Amazon EC2 instance with AMD SEV-SNP enabled, you are charged an additional hourly usage fee that is equivalent to 10 percent of the On-Demand hourly rate of the selected instance type.
This AMD SEV-SNP usage fee is a separate charge to your Amazon EC2 instance usage. Reserved Instances, Savings Plans, and operating system usage don't impact this fee.
If you configure a Spot Instance to launch with AMD SEV-SNP enabled, you are charged an additional hourly usage fee that is equivalent to 10 percent of the On-Demand hourly rate of the selected instance type. If the allocation strategy uses price as an input, Spot Fleet does not include this additional fee; only the Spot price is used.
### Find EC2 instance types that support AMD SEV-SNP You can find instance types that support AMD SEV-SNP. The Amazon EC2 console does not display this information for an instance type.

AWS CLI To find the instance types that support AMD SEV-SNP Use the following describe-instance-types command. aws ec2 describe-instance-types \ --filters Name=processor-info.supported-features,Values=amd-sev-snp \ --query 'InstanceTypes[*].[InstanceType]' \ --output text | sort The following is example output. c6a.12xlarge c6a.16xlarge c6a.2xlarge c6a.4xlarge c6a.8xlarge c6a.large c6a.xlarge m6a.2xlarge m6a.4xlarge m6a.8xlarge m6a.large m6a.xlarge r6a.2xlarge r6a.4xlarge r6a.large r6a.xlarge PowerShell To find the instance types that support AMD SEV-SNP Use the Get-EC2InstanceType cmdlet.
(Get-EC2InstanceType `
    -Filter @{Name="processor-info.supported-features"; Values="amd-sev- snp"}).InstanceType.Value | Sort-Object The following is example output.

c6a.12xlarge c6a.16xlarge c6a.2xlarge c6a.4xlarge c6a.8xlarge c6a.large c6a.xlarge m6a.2xlarge m6a.4xlarge m6a.8xlarge m6a.large m6a.xlarge r6a.2xlarge r6a.4xlarge r6a.large r6a.xlarge
### Enable AMD SEV-SNP for an EC2 instance You can launch an instance with AMD SEV-SNP enabled. You can't enable AMD SEV-SNP after launch.
#### Launch an instance with AMD SEV-SNP enabled You can't enable AMD SEV-SNP using the Amazon EC2 console.
AWS CLI To launch an instance with AMD SEV-SNP enabled Use the run-instances command with the --cpu-options option. For additional requirements, see AMD SEV-SNP requirements.
--cpu-options AmdSevSnp=enabled PowerShell To launch an instance with AMD SEV-SNP enabled Use the New-EC2Instance cmdlet with the -CpuOption parameter.

-CpuOption @{AmdSevSnp="enabled"}
#### Check if an EC2 instance is enabled for AMD SEV-SNP You can find instances that are enabled for AMD SEV-SNP. The Amazon EC2 console does not display this information.
AWS CLI To check whether AMD SEV-SNP is enabled for an instance Use the describe-instances command. aws ec2 describe-instances \ --instance-ids i-1234567890abcdef0 \ --query Reservations[].Instances[].CpuOptions The following is example output. If AmdSevSnp is not present in CpuOptions, then AMD SEV- SNP is disabled.
[ { "AmdSevSnp": "enabled", "CoreCount": 1, "ThreadsPerCore": 2 } ]
PowerShell To check whether AMD SEV-SNP is enabled for an instance Use the Get-EC2Instance cmdlet.
(Get-EC2Instance `
    -InstanceId i-1234567890abcdef0).Instances.CpuOptions The following is example output. If the value of AmdSevSnp is not present, then AMD SEV-SNP is disabled.

AmdSevSnp CoreCount ThreadsPerCore --------- --------- -------------- enabled   1         2 AWS CloudTrail In the AWS CloudTrail event for the instance launch request, the following property indicates that AMD SEV-SNP is enabled for the instance.
"cpuOptions": {"AmdSevSnp": "enabled"}
### Attest an Amazon EC2 instance with AMD SEV-SNP Attestation is a process that allows your instance to prove its state and identity. After you enable AMD SEV-SNP for your instance, you can request an AMD SEV-SNP attestation report from the underlying processor. The AMD SEV-SNP attestation report contains a cryptographic hash, called the launch measurement, of the initial guest memory contents and initial vCPU state. The attestation report is signed with a VLEK signature that chains back to an AMD root of trust. You can use the launch measurement included in the attestation report to validate that the instance is running in a genuine AMD environment and to validate the initial boot code that was used to launch the instance.
Prerequisite Launch an instance that is enabled for AMD SEV-SNP. For more information, see Enable AMD SEV- SNP for an EC2 instance.
Steps
- Step 1: Get the attestation report
- Step 2: Validate the attestation report signature
#### Step 1: Get the attestation report In this step, you install and build the snpguest utility, and then use it to request the AMD SEV- SNP attestation report and certificates.
1. Connect to your instance.

2. Run the following commands to build the snpguest utility from the snpguest repository.
$ git clone https://github.com/virtee/snpguest.git $ cd snpguest $ cargo build -r $ cd target/release
3. Generate a request for the attestation report. The utility requests the attestation report from the host, and writes it to a binary file with the provided request data.
The following example creates a random request string, and uses it as the request file (request-file.txt). When the command returns the attestation report it's stored in the file path that you specify (report.bin). In this case, the utility stores the report in the current directory.
$ ./snpguest report report.bin request-file.txt --random
4. Request the certificates from host memory, and store them as PEM files. The following example stores the files in the same directory as the snpguest utility. If certificates already exist in the specified directory, those certificates are overwritten.
$ ./snpguest certificates PEM ./
#### Step 2: Validate the attestation report signature The attestation report is signed with a certificate, called the Versioned Loaded Endorsement Key (VLEK), which is issued by AMD for AWS. In this step, you can validate that the VLEK certificate is issued by AMD, and that the attestation report is signed by that VLEK certificate.
1. Download the VLEK root of trust certificates from the official AMD website to the current directory.
$ sudo curl --proto '=https' --tlsv1.2 -sSf https://kdsintf.amd.com/vlek/v1/Milan/ cert_chain -o ./cert_chain.pem
2. Use openssl to validate that the VLEK certificate is signed by the AMD root of trust certificates.
$ sudo openssl verify --CAfile ./cert_chain.pem vlek.pem

The following is example output. vlek.pem: OK
3. Use the snpguest utility to validate that the attestation report is signed by the VLEK certificate.
$ ./snpguest verify attestation ./ report.bin The following is example output.
Reported TCB Boot Loader from certificate matches the attestation report.
Reported TCB TEE from certificate matches the attestation report.
Reported TCB SNP from certificate matches the attestation report.
Reported TCB Microcode from certificate matches the attestation report.
VEK signed the Attestation Report!
## Processor state control for Amazon EC2 Linux instances C-states control the sleep levels that a core can enter when it is idle. C-states are numbered starting with C0 (the shallowest state where the core is totally awake and executing instructions) and go to C6 (the deepest idle state where a core is powered off).
P-states control the desired performance (in CPU frequency) from a core. P-states are numbered starting from P0 (the highest performance setting where the core is allowed to use Intel Turbo Boost Technology to increase frequency if possible), and they go from P1 (the P-state that requests the maximum baseline frequency) to P15 (the lowest possible frequency).
Note AWS Graviton processors have built-in power saving modes and operate at a fixed frequency. Therefore, they do not provide the ability for the operating system to control C- states and P-states.

C-states and P-states The following instance types provide the ability for an operating system to control C-states and P- states:
- General purpose: m4.10xlarge | m4.16xlarge
- Compute optimized: c4.8xlarge
- Memory optimized: r4.8xlarge | r4.16xlarge | x1.16xlarge | x1.32xlarge | x1e.8xlarge | x1e.16xlarge | x1e.32xlarge
- Storage optimized: d2.8xlarge | i3.8xlarge | i3.16xlarge | h1.8xlarge | h1.16xlarge
- Accelerated computing: f1.16xlarge | g3.16xlarge | p2.16xlarge | p3.16xlarge
- Bare metal: All bare metal instances with Intel and AMD processors C-states only The following instance types provide the ability for an operating system to control C-states:
- General purpose: m5.12xlarge | m5.24xlarge | m5d.12xlarge | m5d.24xlarge | m5n.12xlarge | m5n.24xlarge | m5dn.12xlarge | m5dn.24xlarge | m5zn.6xlarge
| m5zn.12xlarge | m6a.24xlarge | m6a.48xlarge | m6i.16xlarge | m6i.32xlarge | m6id.16xlarge | m6id.32xlarge | m6idn.16xlarge | m6in.16xlarge | m6in.32xlarge
| m7a.medium | m7a.large | m7a.xlarge | m7a.2xlarge | m7a.4xlarge | m7a.8xlarge
| m7a.12xlarge | m7a.16xlarge | m7a.24xlarge | m7a.32xlarge | m7a.48xlarge | m7i.large | m7i.xlarge | m7i.2xlarge |  m7i.4xlarge | m7i.8xlarge | m7i.12xlarge
| m7i.16xlarge | m7i.24xlarge | m7i.48xlarge | m8a.medium | m8a.large | m8a.xlarge
| m8a.2xlarge | m8a.4xlarge | m8a.8xlarge | m8a.12xlarge | m8a.16xlarge | m8a.24xlarge | m8a.48xlarge | m8azn.medium | m8azn.large | m8azn.xlarge | m8azn.3xlarge | m8azn.6xlarge | m8azn.12xlarge | m8azn.24xlarge | m8i.large
| m8i.xlarge | m8i.2xlarge | m8i.4xlarge | m8i.8xlarge | m8i.12xlarge | m8i.16xlarge | m8i.24xlarge | m8i.32xlarge | m8i.48xlarge | m8i.96xlarge
| m8id.large | m8id.xlarge | m8id.2xlarge | m8id.4xlarge | m8id.8xlarge | m8id.12xlarge | m8id.16xlarge | m8id.24xlarge | m8id.32xlarge | m8id.48xlarge | m8id.96xlarge
- Compute optimized: c5.9xlarge | c5.12xlarge | c5.18xlarge | c5.24xlarge | c5a.24xlarge | c5ad.24xlarge | c5d.9xlarge | c5d.12xlarge | c5d.18xlarge
| c5d.24xlarge | c5n.9xlarge | c5n.18xlarge | c6a.24xlarge | c6a.32xlarge |

c6a.48xlarge | c6i.16xlarge | c6i.32xlarge | c6id.24xlarge | c6id.32xlarge | c6in.32xlarge | c7a.medium | c7a.large | c7a.xlarge | c7a.2xlarge | c7a.4xlarge
| c7a.8xlarge | c7a.12xlarge | c7a.16xlarge | c7a.24xlarge | c7a.32xlarge | c7a.48xlarge | c7i.large | c7i.xlarge | c7i.2xlarge | c7i.4xlarge | c7i.8xlarge
| c7i.12xlarge | c7i.16xlarge | c7i.24xlarge | c7i.48xlarge | c8a.medium | c8a.large | c8a.xlarge | c8a.2xlarge | c8a.4xlarge | c8a.8xlarge | c8a.12xlarge | c8a.16xlarge | c8a.24xlarge | c8a.48xlarge | c8i.large | c8i.xlarge | c8i.2xlarge
| c8i.4xlarge | c8i.8xlarge | c8i.12xlarge | c8i.16xlarge | c8i.24xlarge
| c8i.32xlarge | c8i.48xlarge | c8i.96xlarge | c8id.large | c8id.xlarge | c8id.2xlarge | c8id.4xlarge | c8id.8xlarge | c8id.12xlarge | c8id.16xlarge
| c8id.24xlarge | c8id.32xlarge | c8id.48xlarge | c8id.96xlarge x8i.large
| x8i.xlarge | x8i.2xlarge | x8i.4xlarge | x8i.8xlarge | x8i.12xlarge | x8i.16xlarge | x8i.24xlarge | x8i.32xlarge | x8i.48xlarge | x8i.48xlarge | x8i.96xlarge
- Memory optimized: r5.12xlarge | r5.24xlarge | r5b.12xlarge | r5d.12xlarge | r5d.24xlarge | r5n.12xlarge | r5n.24xlarge | r5dn.12xlarge | r5dn.24xlarge
| r6a.24xlarge | r6a.48xlarge | r6i.16xlarge | r6i.32xlarge | r6id.16xlarge
| r6id.32xlarge | r6in.16xlarge | r6in.32xlarge | r7a.medium | r7a.large
| r7a.xlarge | r7a.2xlarge | r7a.4xlarge | r7a.8xlarge | r7a.12xlarge | r7a.16xlarge | r7a.24xlarge | r7a.32xlarge | r7a.48xlarge | r7i.large
| r7i.xlarge | r7i.2xlarge | r7i.4xlarge | r7i.8xlarge | r7i.12xlarge | r7i.16xlarge | r7i.24xlarge | r7i.48xlarge | r7iz.large | r7iz.xlarge | r7iz.2xlarge | r7iz.4xlarge | r7iz.8xlarge | r7iz.12xlarge | r7iz.16xlarge
| r7iz.32xlarge | r8a.medium | r8a.large | r8a.xlarge | r8a.2xlarge | r8a.4xlarge | r8a.8xlarge | r8a.12xlarge | r8a.16xlarge | r8a.24xlarge | r8a.48xlarge | r8i.large | r8i.xlarge | r8i.2xlarge | r8i.4xlarge | r8i.8xlarge
| r8i.12xlarge | r8i.16xlarge | r8i.24xlarge | r8i.32xlarge | r8i.48xlarge
| r8i.96xlarge | r8id.large | r8id.xlarge | r8id.2xlarge | r8id.4xlarge | r8id.8xlarge | r8id.12xlarge | r8id.16xlarge | r8id.24xlarge | r8id.32xlarge
| r8id.48xlarge | r8id.96xlarge | u-3tb1.56xlarge | u-6tb1.56xlarge | u-6tb1.112xlarge | u-9tb1.112xlarge | u-12tb1.112xlarge | u-18tb1.112xlarge | u-24tb1.112xlarge | u7i-6tb.112xlarge | u7i-8tb.112xlarge | u7i-12tb.224xlarge
| u7in-16tb.224xlarge | u7in-24tb.224xlarge |  u7in-32tb.224xlarge | u7inh-32tb.480xlarge | x2idn.32xlarge | x2iedn.16xlarge | x2iedn.32xlarge
| x2iezn.12xlarge | x8aedz.large | x8aedz.xlarge | x8aedz.3xlarge | x8aedz.6xlarge | x8aedz.12xlarge | x8aedz.24xlarge | z1d.6xlarge | z1d.12xlarge
