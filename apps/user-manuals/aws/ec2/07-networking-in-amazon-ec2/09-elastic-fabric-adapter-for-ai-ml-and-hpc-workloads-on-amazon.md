# Elastic Fabric Adapter for AI/ML and HPC workloads on Amazon EC2

Source: apps/user-manuals/aws/ec2-ug.pdf

---

noted, various components must run on CPU 0, and therefore we recommend excluding it from all RSS configurations when sufficient vCPUs are available.
For example, when there are three elastic network interfaces on a 72 vCPU instance with 2 NUMA nodes with hyper-threading enabled, the following commands spread the network load between the two CPUs without overlap and prevent the use of core 0 completely.
Set-NetAdapterRss -Name NIC1 -BaseProcessorGroup 0 -BaseProcessorNumber 2 - MaxProcessorNumber 16 Set-NetAdapterRss -Name NIC2 -BaseProcessorGroup 1 -BaseProcessorNumber 0 - MaxProcessorNumber 14 Set-NetAdapterRss -Name NIC3 -BaseProcessorGroup 1 -BaseProcessorNumber 16 - MaxProcessorNumber 30 Note that these settings are persistent for each network adapter. If an instance is resized to one with a different number of vCPUs, you should reevaluate the RSS configuration for each enabled elastic network interface. The complete Microsoft documentation for the cmdlet can be found here: Set-NetAdapterRss.
Special note for SQL workloads: We also recommend that you review your I/O thread affinity settings along with your elastic network interface RSS configuration to minimize I/O and network contention for the same CPUs. See Server configuration: affinity mask.
# Elastic Fabric Adapter for AI/ML and HPC workloads on Amazon EC2 EC2 An Elastic Fabric Adapter (EFA) is a network device that you can attach to your Amazon EC2 instance to accelerate Artificial Intelligence (AI), Machine Learning (ML), and High Performance Computing (HPC) applications. EFA enables you to achieve the application performance of an on- premises AI/ML or HPC cluster, with the scalability, flexibility, and elasticity provided by the AWS Cloud.
EFA provides lower and more consistent latency and higher throughput than the TCP transport traditionally used in cloud-based HPC systems. It enhances the performance of inter-instance communication that is critical for scaling AI/ML and HPC applications. It is optimized to work on the existing AWS network infrastructure and it can scale depending on application requirements.

EFA integrates with Libfabric 1.7.0 and later, and it supports Nvidia Collective Communications Library (NCCL) for AI and ML applications, and Open MPI 4.1 and later and Intel MPI 2019 Update 5 and later for HPC applications.
EFA supports RDMA (Remote Direct Memory Access) write on most supported instance types that have Nitro version 4 and later. RDMA read is supported on all instances with Nitro version 4 and later. For more information, see Supported instance types.
Contents
- EFA basics
- Supported interfaces and libraries
- Supported instance types
- Supported operating systems
- EFA limitations
- EFA pricing
- Get started with EFA and MPI for HPC workloads on Amazon EC2
- Get started with EFA and NCCL for ML workloads on Amazon EC2
- Maximize network bandwidth on Amazon EC2 instances with multiple network cards
- Create and attach an Elastic Fabric Adapter to an Amazon EC2 instance
- Detach and delete an EFA from an Amazon EC2 instance
- Monitor an Elastic Fabric Adapter on Amazon EC2
- Verify the EFA installer using a checksum
- Elastic Fabric Adapter release notes
## EFA basics An EFA device can be attached to an EC2 instance in two ways:
1. Using a traditional EFA interface, also called EFA with ENA, which creates both an EFA device and an ENA device.
2. Using an EFA-only interface, which creates just the EFA device.
The EFA device provides capabilities like built-in OS-bypass and congestion control through the Scalable Reliable Datagram (SRD) protocol. The EFA device features enable low-latency, reliable

transport functionality that allows EFA interface to provide better application performance for HPC and ML applications on Amazon EC2. While the ENA device offers traditional IP networking.
Traditionally, AI/ML applications use NCCL and HPC applications use the Message Passing Interface (MPI) to interface with the system's network transport. In the AWS cloud, this has meant that applications interface with NCCL or MPI, which then uses the operating system's TCP/IP stack and the ENA device driver to enable network communication between instances.
With a traditional EFA (EFA with ENA) or EFA-only interface, AI/ML applications use NCCL and HPC applications use MPI, to interface directly with the Libfabric API. The Libfabric API bypasses the operating system kernel and communicates directly with the EFA device to put packets on the network. This reduces overhead and enables AI/ML and HPC applications to run more efficiently.
Note Libfabric is a core component of the OpenFabrics Interfaces (OFI) framework, which defines and exports the user-space API of OFI. For more information, see the Libfabric OpenFabrics website.
### Differences between ENA, EFA, and EFA-only network interfaces Amazon EC2 provides two types of network interfaces:

- ENA interfaces provide all of the traditional IP networking and routing features that are required to support IP networking for a VPC. For more information, see Enable enhanced networking with ENA on your EC2 instances.
- EFA (EFA with ENA) interfaces provide both the ENA device for IP networking and the EFA device for low-latency, high-throughput communication.
- EFA-only interfaces support only the EFA device capabilities, without the ENA device for traditional IP networking.
The following table provides a comparison of ENA, EFA, and EFA-only network interfaces.
ENA EFA (EFA with ENA)
EFA-only Supports IP networking functionality Yes Yes No Can be assigned IPv4 or IPv6 addresses Yes Yes No Can be used as primary network interface for instance Yes Yes No Counts towards ENI attachmen t limit for instance Yes Yes Yes Instance type support Supported on all Nitro-based instances types
## Supported instance types Supported instance types

ENA EFA (EFA with ENA)
EFA-only Parameter naming in EC2 APIs interface efa efa-only Field naming in EC2 console No selection EFA with ENA EFA-only
## Supported interfaces and libraries EFAs support the following interfaces and libraries:
- Open MPI 4.1 and later
- Intel MPI 2019 Update 5 and later
- NVIDIA Collective Communications Library (NCCL) 2.4.2 and later
- AWS Neuron SDK version 2.3 and later Supported instance types All of the following instance types support EFA. Additionally, the tables indicate RDMA read and RDMA write support for the instance types.
Nitro v6 Instance type RDMA read support RDMA write support General Purpose m8a.48xlarge Yes Yes m8a.metal-48xl Yes Yes m8azn.24xlarge Yes Yes m8azn.metal-24xl Yes Yes

Instance type RDMA read support RDMA write support m8gb.16xlarge Yes Yes m8gb.24xlarge Yes Yes m8gb.48xlarge Yes Yes m8gn.16xlarge Yes Yes m8gn.24xlarge Yes Yes m8gn.48xlarge Yes Yes m8i.48xlarge Yes Yes m8i.96xlarge Yes Yes m8i.metal-48xl Yes Yes m8i.metal-96xl Yes Yes m8id.48xlarge Yes Yes m8id.96xlarge Yes Yes m8id.metal-48xl Yes Yes m8id.metal-96xl Yes Yes Compute Optimized c8a.48xlarge Yes Yes c8a.metal-48xl Yes Yes c8gb.16xlarge Yes Yes c8gb.24xlarge Yes Yes c8gb.48xlarge Yes Yes c8gb.metal-24xl Yes Yes

Instance type RDMA read support RDMA write support c8gb.metal-48xl Yes Yes c8gn.16xlarge Yes Yes c8gn.24xlarge Yes Yes c8gn.48xlarge Yes Yes c8gn.metal-24xl Yes Yes c8gn.metal-48xl Yes Yes c8i.48xlarge Yes Yes c8i.96xlarge Yes Yes c8i.metal-48xl Yes Yes c8i.metal-96xl Yes Yes c8id.48xlarge Yes Yes c8id.96xlarge Yes Yes c8id.metal-48xl Yes Yes c8id.metal-96xl Yes Yes Memory Optimized r8a.48xlarge Yes Yes r8a.metal-48xl Yes Yes r8gb.16xlarge Yes Yes r8gb.24xlarge Yes Yes r8gb.48xlarge Yes Yes r8gb.metal-24xl Yes Yes

Instance type RDMA read support RDMA write support r8gb.metal-48xl Yes Yes r8gn.16xlarge Yes Yes r8gn.24xlarge Yes Yes r8gn.48xlarge Yes Yes r8gn.metal-24xl Yes Yes r8gn.metal-48xl Yes Yes r8i.48xlarge Yes Yes r8i.96xlarge Yes Yes r8i.metal-48xl Yes Yes r8i.metal-96xl Yes Yes r8id.48xlarge Yes Yes r8id.96xlarge Yes Yes r8id.metal-48xl Yes Yes r8id.metal-96xl Yes Yes x8aedz.24xlarge Yes Yes x8aedz.metal-24xl Yes Yes x8i.48xlarge Yes Yes x8i.64xlarge Yes Yes x8i.96xlarge Yes Yes x8i.metal-48xl Yes Yes x8i.metal-96xl Yes Yes

Instance type RDMA read support RDMA write support Storage Optimized i8ge.48xlarge Yes No i8ge.metal-48xl Yes No Accelerated Computing g7e.8xlarge Yes Yes g7e.12xlarge Yes Yes g7e.24xlarge Yes Yes g7e.48xlarge Yes Yes p6-b200.48xlarge Yes Yes p6-b300.48xlarge Yes Yes High Performance Computing hpc8a.96xlarge Yes Yes Nitro v5 Instance type RDMA read support RDMA write support General Purpose m8g.24xlarge Yes No m8g.48xlarge Yes No m8g.metal-24xl Yes No m8g.metal-48xl Yes No m8gd.24xlarge No No

Instance type RDMA read support RDMA write support m8gd.48xlarge No No m8gd.metal-24xl No No m8gd.metal-48xl No No Compute Optimized c7gn.16xlarge Yes No c7gn.metal Yes No c8g.24xlarge Yes No c8g.48xlarge Yes No c8g.metal-24xl Yes No c8g.metal-48xl Yes No c8gd.24xlarge No No c8gd.48xlarge No No c8gd.metal-24xl No No c8gd.metal-48xl No No Memory Optimized r8g.24xlarge No No r8g.48xlarge No No r8g.metal-24xl No No r8g.metal-48xl No No r8gd.24xlarge No No r8gd.48xlarge No No

Instance type RDMA read support RDMA write support r8gd.metal-24xl No No r8gd.metal-48xl No No x8g.24xlarge No No x8g.48xlarge No No x8g.metal-24xl No No x8g.metal-48xl No No Storage Optimized i7ie.48xlarge Yes No i7ie.metal-48xl Yes No i8g.48xlarge No No Accelerated Computing p5en.48xlarge Yes Yes p6e-gb200.36xlarge Yes Yes trn2.3xlarge Yes Yes trn2.48xlarge Yes Yes trn2u.48xlarge Yes Yes High Performance Computing hpc7g.4xlarge Yes No hpc7g.8xlarge Yes No hpc7g.16xlarge Yes No

Nitro v4 Instance type RDMA read support RDMA write support General Purpose m6a.48xlarge Yes Yes m6a.metal Yes Yes m6i.32xlarge Yes Yes m6i.metal Yes Yes m6id.32xlarge Yes Yes m6id.metal Yes Yes m6idn.32xlarge Yes Yes m6idn.metal Yes Yes m6in.32xlarge Yes Yes m6in.metal Yes Yes m7a.48xlarge Yes No m7a.metal-48xl Yes No m7g.16xlarge Yes No m7g.metal Yes No m7gd.16xlarge Yes No m7gd.metal Yes No m7i.48xlarge Yes No m7i.metal-48xl Yes No Compute Optimized

Instance type RDMA read support RDMA write support c6a.48xlarge Yes Yes c6a.metal Yes Yes c6gn.16xlarge Yes Yes c6i.32xlarge Yes Yes c6i.metal Yes Yes c6id.32xlarge Yes Yes c6id.metal Yes Yes c6in.32xlarge Yes Yes c6in.metal Yes Yes c7a.48xlarge Yes No c7a.metal-48xl Yes No c7g.16xlarge Yes Yes c7g.metal Yes Yes c7gd.16xlarge Yes No c7gd.metal Yes No c7i.48xlarge Yes No c7i.metal-48xl Yes No Memory Optimized r6a.48xlarge Yes Yes r6a.metal Yes Yes r6i.32xlarge Yes Yes

Instance type RDMA read support RDMA write support r6i.metal Yes Yes r6id.32xlarge Yes Yes r6id.metal Yes Yes r6idn.32xlarge Yes Yes r6idn.metal Yes Yes r6in.32xlarge Yes Yes r6in.metal Yes Yes r7a.48xlarge No No r7a.metal-48xl No No r7g.16xlarge No No r7g.metal No No r7gd.16xlarge No No r7gd.metal No No r7i.48xlarge No No r7i.metal-48xl No No r7iz.32xlarge No No r7iz.metal-32xl No No u7i-6tb.112xlarge Yes Yes u7i-8tb.112xlarge Yes Yes u7i-12tb.224xlarge Yes Yes u7in-16tb.224xlarge Yes Yes

Instance type RDMA read support RDMA write support u7in-24tb.224xlarge Yes Yes u7in-32tb.224xlarge Yes Yes u7inh-32tb.480xlarge Yes Yes x2idn.32xlarge Yes Yes x2idn.metal Yes Yes x2iedn.32xlarge Yes Yes x2iedn.metal Yes Yes Storage Optimized i4g.16xlarge Yes Yes i4i.32xlarge Yes Yes i4i.metal Yes Yes i7i.24xlarge Yes No i7i.48xlarge Yes No i7i.metal-48xl Yes No im4gn.16xlarge Yes Yes Accelerated Computing f2.48xlarge Yes Yes g6.8xlarge Yes Yes g6.12xlarge Yes Yes g6.16xlarge Yes Yes g6.24xlarge Yes Yes

Instance type RDMA read support RDMA write support g6.48xlarge Yes Yes g6e.8xlarge Yes Yes g6e.12xlarge Yes Yes g6e.16xlarge Yes Yes g6e.24xlarge Yes Yes g6e.48xlarge Yes Yes gr6.8xlarge Yes Yes p5.4xlarge Yes Yes p5.48xlarge Yes Yes p5e.48xlarge Yes Yes trn1.32xlarge Yes Yes trn1n.32xlarge Yes Yes High Performance Computing hpc6a.48xlarge Yes Yes hpc6id.32xlarge Yes Yes hpc7a.12xlarge Yes No hpc7a.24xlarge Yes No hpc7a.48xlarge Yes No hpc7a.96xlarge Yes No

Nitro v3 Instance type RDMA read support RDMA write support General Purpose m5dn.24xlarge No No m5dn.metal No No m5n.24xlarge No No m5n.metal No No m5zn.12xlarge No No m5zn.metal No No Compute Optimized c5n.9xlarge No No c5n.18xlarge No No c5n.metal No No Memory Optimized r5dn.24xlarge No No r5dn.metal No No r5n.24xlarge No No r5n.metal No No x2iezn.12xlarge No No x2iezn.metal No No Storage Optimized i3en.12xlarge No No

Instance type RDMA read support RDMA write support i3en.24xlarge No No i3en.metal No No Accelerated Computing dl1.24xlarge Yes No dl2q.24xlarge No No g4dn.8xlarge No No g4dn.12xlarge No No g4dn.16xlarge No No g4dn.metal No No g5.8xlarge No No g5.12xlarge No No g5.16xlarge No No g5.24xlarge No No g5.48xlarge No No inf1.24xlarge No No p3dn.24xlarge No No p4d.24xlarge Yes No p4de.24xlarge Yes No vt1.24xlarge No No Previous Generation p3dn.24xlarge No No

To see the available instance types that support EFAs in a specific Region The available instance types vary by Region. To see the available instance types that support EFAs in a Region, use the describe-instance-types command with the --region parameter. Include the --filters parameter to scope the results to the instance types that support EFA and the -- query parameter to scope the output to the value of InstanceType. aws ec2 describe-instance-types \ --region us-east-1  \ --filters Name=network-info.efa-supported,Values=true \ --query "InstanceTypes[*].[InstanceType]"  \ --output text | sort
## Supported operating systems Operating system support differs depending on the processor type. The following table shows the supported operating systems.
Operating system Intel/AMD (x86_64) instance types AWS Graviton (arm64) instance types Amazon Linux 2023 ✓ ✓ Amazon Linux 2 ✓ ✓ RHEL 8 and 9 ✓ ✓ Debian 11, 12, and 13 ✓ ✓ Rocky Linux 8 and 9 ✓ ✓ Ubuntu 22.04 and 24.04 ✓ ✓ SUSE Linux Enterprise 15 SP2 and later ✓ ✓

Operating system Intel/AMD (x86_64) instance types AWS Graviton (arm64) instance types OpenSUSE Leap 15.5 and later ✓

Note Some of the listed operating systems might not be supported with Intel MPI. If you are using Intel MPI, refer to the  Intel MPI documentation to verify support for your operating system.
## EFA limitations EFAs have the following limitations:
- RDMA write is not supported with all instance types. For more information, see Supported instance types.
- EFA traffic1 between P4d/P4de/DL1 instances and other instance types is currently not supported.
- Instance types that support multiple network cards can be configured with one EFA per network card. All other supported instance types support only one EFA per instance.
- c7g.16xlarge, m7g.16xlarge, and r7g.16xlarge Dedicated Instances and Dedicated Hosts are not supported when an EFA is attached.
- EFA traffic1 can't cross Availability Zones or VPCs. This does not apply to normal IP traffic from the ENA device of an EFA interface.
- EFA traffic1 is not routable. Normal IP traffic from the ENA device of an EFA interface remains routable.
- EFA is not supported on AWS Outposts.
- The EFA device of an EFA (EFA with ENA) interface is supported on Windows instances only for AWS Cloud Digital Interface Software Development Kit (AWS CDI SDK) based applications.
If you attach an EFA (EFA with ENA) interface to a Windows instance for non-CDI SDK based applications, it functions as an ENA interface, without the added EFA device capabilities. The

EFA-only interface is not supported by AWS CDI based applications on Windows or Linux. For more information, see the AWS Cloud Digital Interface Software Development Kit (AWS CDI SDK)
User Guide.
1EFA traffic refers to the traffic transmitted through the EFA device of either an EFA (EFA with ENA) or EFA-only interface.
## EFA pricing EFA is available as an optional Amazon EC2 networking feature that you can enable on any supported instance at no additional cost.
## Get started with EFA and MPI for HPC workloads on Amazon EC2 This tutorial helps you to launch an EFA and MPI-enabled instance cluster for HPC workloads.
Note The u7i-12tb.224xlarge, u7in-16tb.224xlarge, u7in-24tb.224xlarge, and u7in-32tb.224xlarge instances can run up to 128 parallel MPI processes with Open MPI or up to 256 parallel MPI processes with Intel MPI.
Tasks
- Step 1: Prepare an EFA-enabled security group
- Step 2: Launch a temporary instance
- Step 3: Install the EFA software
- Step 4: (Optional) Enable Open MPI 5
- Step 5: (Optional) Install Intel MPI
- Step 6: Disable ptrace protection
- Step 7. Confirm installation
- Step 8: Install your HPC application
- Step 9: Create an EFA-enabled AMI
- Step 10: Launch EFA-enabled instances into a cluster placement group

- Step 11: Terminate the temporary instance
- Step 12: Enable passwordless SSH
### Step 1: Prepare an EFA-enabled security group An EFA requires a security group that allows all inbound and outbound traffic to and from the security group itself. The following procedure creates a security group that allows all inbound and outbound traffic to and from itself, and that allows inbound SSH traffic from any IPv4 address for SSH connectivity.
Important This security group is intended for testing purposes only. For your production environments, we recommend that you create an inbound SSH rule that allows traffic only from the IP address from which you are connecting, such as the IP address of your computer, or a range of IP addresses in your local network.
For other scenarios, see Security group rules for different use cases.
To create an EFA-enabled security group
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Security Groups and then choose Create security group.
3. In the Create security group window, do the following: a.
For Security group name, enter a descriptive name for the security group, such as EFA- enabled security group. b.
(Optional) For Description, enter a brief description of the security group. c.
For VPC, select the VPC into which you intend to launch your EFA-enabled instances. d.
Choose Create security group.
4. Select the security group that you created, and on the Details tab, copy the Security group ID.
5. With the security group still selected, choose Actions, Edit inbound rules, and then do the following: a.
Choose Add rule.

b.
For Type, choose All traffic. c.
For Source type, choose Custom and paste the security group ID that you copied into the field. d.
Choose Add rule. e.
For Type, choose SSH. f.
For Source type, choose Anywhere-IPv4. g.
Choose Save rules.
6. With the security group still selected, choose Actions, Edit outbound rules, and then do the following: a.
Choose Add rule. b.
For Type, choose All traffic. c.
For Destination type, choose Custom and paste the security group ID that you copied into the field. d.
Choose Save rules.
### Step 2: Launch a temporary instance Launch a temporary instance that you can use to install and configure the EFA software components. You use this instance to create an EFA-enabled AMI from which you can launch your EFA-enabled instances.
To launch a temporary instance
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Instances, and then choose Launch Instances to open the new launch instance wizard.
3. (Optional) In the Name and tags section, provide a name for the instance, such as EFA- instance. The name is assigned to the instance as a resource tag (Name=EFA-instance).
4. In the Application and OS Images section, select an AMI for one of the supported operating systems.
5. In the Instance type section, select a supported instance type.
6. In the Key pair section, select the key pair to use for the instance.
7. In the Network settings section, choose Edit, and then do the following:

a.
For Subnet, choose the subnet in which to launch the instance. If you do not select a subnet, you can't enable the instance for EFA. b.
For Firewall (security groups), choose Select existing security group, and then select the security group that you created in the previous step. c.
Expand the Advanced network configuration section.
For Network interface 1, select Network card index = 0, Device index = 0, and Interface type = EFA with ENA.
(Optional) If you are using a multi-card instance type, such as p4d.24xlarge or p5.48xlarge, for each additional network interface required, choose Add network interface, for Network card index select the next unused index, and then select Device index = 1 and Interface type = EFA with ENA or EFA-only.
8. In the Storage section, configure the volumes as needed.
9. In the Summary panel on the right, choose Launch instance.
Note Consider requiring the use of IMDSv2 for the temporary instance as well as the AMI that you will create in Step 9 unless you have already set IMDSv2 as the default for the account.
For more information about IMDSv2 configuration steps, see Configure instance metadata options for new instances.
### Step 3: Install the EFA software Install the EFA-enabled kernel, EFA drivers, Libfabric, and Open MPI stack that is required to support EFA on your temporary instance.
The steps differ depending on whether you intend to use EFA with Open MPI, with Intel MPI, or with Open MPI and Intel MPI.
Note Some operating systems might not be supported with Intel MPI. If you are using Intel MPI, refer to the  Intel MPI documentation to verify support for your operating system.

To install the EFA software
1. Connect to the instance you launched. For more information, see Connect to your Linux instance using SSH.
2. To ensure that all of your software packages are up to date, perform a quick software update on your instance. This process may take a few minutes.
- Amazon Linux 2023, Amazon Linux 2, RHEL 8/9, Rocky Linux 8/9 $ sudo yum update -y
- Ubuntu and Debian $ sudo apt-get update && sudo apt-get upgrade -y
- SUSE Linux Enterprise $ sudo zypper update -y
3. Reboot the instance and reconnect to it.
4. Download the EFA software installation files. The software installation files are packaged into a compressed tarball (.tar.gz) file. To download the latest stable version, use the following command.
You can also get the latest version by replacing the version number with latest in the preceding command.
$ curl -O https://efa-installer.amazonaws.com/aws-efa-installer-1.47.0.tar.gz
5. (Optional) Verify the authenticity and integrity of the EFA tarball (.tar.gz) file.
We recommend that you do this to verify the identity of the software publisher and to check that the file has not been altered or corrupted since it was published. If you do not want to verify the tarball file, skip this step.
Note Alternatively, if you prefer to verify the tarball file by using an MD5 or SHA256 checksum instead, see Verify the EFA installer using a checksum.

a.
Download the public GPG key and import it into your keyring.
$ wget https://efa-installer.amazonaws.com/aws-efa-installer.key && gpg -- import aws-efa-installer.key The command should return a key value. Make a note of the key value, because you need it in the next step. b.
Verify the GPG key's fingerprint. Run the following command and specify the key value from the previous step.
$ gpg --fingerprint key_value The command should return a fingerprint that is identical to 4E90 91BC BB97 A96B 26B1 5E59 A054 80B1 DD2D 3CCC. If the fingerprint does not match, don't run the EFA installation script, and contact Support. c.
Download the signature file and verify the signature of the EFA tarball file.
$ wget https://efa-installer.amazonaws.com/aws-efa-installer-1.47.0.tar.gz.sig && gpg --verify ./aws-efa-installer-1.47.0.tar.gz.sig The following shows example output. gpg: Signature made Wed 29 Jul 2020 12:50:13 AM UTC using RSA key ID DD2D3CCC gpg: Good signature from "Amazon EC2 EFA <ec2-efa-maintainers@amazon.com>" gpg: WARNING: This key is not certified with a trusted signature! gpg:          There is no indication that the signature belongs to the owner.
Primary key fingerprint: 4E90 91BC BB97 A96B 26B1  5E59 A054 80B1 DD2D 3CCC If the result includes Good signature, and the fingerprint matches the fingerprint returned in the previous step, proceed to the next step. If not, don't run the EFA installation script, and contact Support.
6. Extract the files from the compressed .tar.gz file and navigate into the extracted directory.
$ tar -xf aws-efa-installer-1.47.0.tar.gz && cd aws-efa-installer
7. Install the EFA software. Do one of the following depending on your use case.

Note EFA does not support NVIDIA GPUDirect with SUSE Linux. If you are using SUSE Linux, you must additionally specify the --skip-kmod option to prevent kmod installation. By default, SUSE Linux does not allow out-of-tree kernel modules.
Open MPI and Intel MPI If you intend to use EFA with Open MPI and Intel MPI, you must install the EFA software with Libfabric and Open MPI, and you  must complete Step 5: Install Intel MPI.
To install the EFA software with Libfabric and Open MPI, run the following command.
Note From EFA 1.30.0, both Open MPI 4.1 and Open MPI 5 are installed by default. You can optionally specify the version of Open MPI that you want to install. To install only Open MPI 4.1, include --mpi=openmpi4. To install only Open MPI 5, include --mpi=openmpi5. To install both, omit the --mpi option.
$ sudo ./efa_installer.sh -y Libfabric is installed to /opt/amazon/efa. Open MPI 4.1 is installed to /opt/amazon/ openmpi. Open MPI 5 is installed to /opt/amazon/openmpi5.
Open MPI only If you intend to use EFA with Open MPI only, you must install the EFA software with Libfabric and Open MPI, and you can skip Step 5: Install Intel MPI. To install the EFA software with Libfabric and Open MPI, run the following command.
Note From EFA 1.30.0, both Open MPI 4.1 and Open MPI 5 are installed by default. You can optionally specify the version of Open MPI that you want to install. To install

only Open MPI 4.1, include --mpi=openmpi4. To install only Open MPI 5, include --mpi=openmpi5. To install both, omit the --mpi option.
$ sudo ./efa_installer.sh -y Libfabric is installed to /opt/amazon/efa. Open MPI 4.1 is installed to /opt/amazon/ openmpi. Open MPI 5 is installed to /opt/amazon/openmpi5.
Intel MPI only If you intend to use EFA with Intel MPI only, you can install the EFA software without Libfabric and Open MPI. In this case, Intel MPI uses its embedded Libfabric. If you choose to do this, you must complete Step 5: Install Intel MPI.
To install the EFA software without Libfabric and Open MPI, run the following command.
$ sudo ./efa_installer.sh -y --minimal
8. If the EFA installer prompts you to reboot the instance, do so and then reconnect to the instance. Otherwise, log out of the instance and then log back in to complete the installation.
9. Delete the uncompressed tarball and the tarball itself. Otherwise, these will be included in the EFA-enabled AMI that you create, increasing its size.
### Step 4: (Optional) Enable Open MPI 5 Note Perform this step only if you intend to use Open MPI 5.
From EFA 1.30.0, both Open MPI 4.1 and Open MPI 5 are installed by default. Alternatively, you can choose to install only Open MPI 4.1 or Open MPI 5.
If you chose to install Open MPI 5 in Step 3: Install the EFA software, and you intend to use it, you must perform the following steps to enable it.

To enable Open MPI 5
1. Add Open MPI 5 to the PATH environment variable.
$ module load openmpi5
2. Verify that Open MPI 5 is enabled for use.
$ which mpicc The command should return the Open MPI 5 installation directory - /opt/amazon/ openmpi5.
3. (Optional) To ensure that Open MPI 5 is added to PATH environment variable each time the instance starts, do the following: bash shell Add module load openmpi5 to /home/username/.bashrc and / home/username/.bash_profile. csh and tcsh shells Add module load openmpi5 to /home/username/.cshrc.
If you need to remove Open MPI 5 from the PATH environment variable, run the following command and remove the command from the shell startup scripts.
$ module unload openmpi5
### Step 5: (Optional) Install Intel MPI Important Perform this step only if you intend to use Intel MPI. If you intend to only use Open MPI, skip this step.
Intel MPI requires an additional installation and environment variable configuration.
Prerequisite

Ensure that the user performing the following steps has sudo permissions.
To install Intel MPI
1. To download the Intel MPI installation script, do the following a.
Visit the Intel website. b.
In the Intel MPI Library section of the webpage, choose the link for the Intel MPI Library for Linux Offline installer.
2. Run the installation script that you downloaded in the previous step.
$ sudo bash installation_script_name.sh
3. In the installer, choose Accept & install.
4. Read the Intel Improvement Program, choose the appropriate option, and then choose Begin Installation.
5. When the installation completes, choose Close.
6. By default, Intel MPI uses its embedded (internal) Libfabric. You can configure Intel MPI to use the Libfabric that ships with the EFA installer instead. Typically, the EFA installer ships with a later version of Libfabric than Intel MPI. In some cases, the Libfabric that ships with the EFA installer is more performant than that of Intel MPI. To configure Intel MPI to use the Libfabric that ships with the EFA installer, do one of the following depending on your shell. bash shells Add the following statement to /home/username/.bashrc and / home/username/.bash_profile. export I_MPI_OFI_LIBRARY_INTERNAL=0 csh and tcsh shells Add the following statement to /home/username/.cshrc. setenv I_MPI_OFI_LIBRARY_INTERNAL 0
7. Add the following source command to your shell script to source the vars.sh script from the installation directory to set up the compiler environment each time the instance starts. Do one of the following depending on your shell.

bash shells Add the following statement to /home/username/.bashrc and / home/username/.bash_profile. source /opt/intel/oneapi/mpi/latest/env/vars.sh csh and tcsh shells Add the following statement to /home/username/.cshrc. source /opt/intel/oneapi/mpi/latest/env/vars.csh
8. By default, if EFA is not available due to a misconfiguration, Intel MPI defaults to the TCP/IP network stack, which might result in slower application performance. You can prevent this by setting I_MPI_OFI_PROVIDER to efa. This causes Intel MPI to fail with the following error if EFA is not available:
Abort (XXXXXX) on node 0 (rank 0 in comm 0): Fatal error in PMPI_Init: OtherMPI error, MPIR_Init_thread (XXX)........:
MPID_Init (XXXX)..............:
MPIDI_OFI_mpi_init_hook (XXXX): open_fabric (XXXX)............: find_provider (XXXX)..........:
OFI fi_getinfo() failed (ofi_init.c:2684:find_provider:
Do one of the following depending on your shell. bash shells Add the following statement to /home/username/.bashrc and / home/username/.bash_profile. export I_MPI_OFI_PROVIDER=efa csh and tcsh shells Add the following statement to /home/username/.cshrc.

setenv I_MPI_OFI_PROVIDER efa
9. By default, Intel MPI doesn't print debugging information. You can specify different verbosity levels to control the debugging information. Possible values (in order of the amount of detail they provide) are: 0 (default), 1, 2, 3, 4, 5. Level 1 and higher prints the libfabric version and libfabric provider. Use libfabric version to check whether Intel MPI is using the internal Libfabric or the Libfabric that ships with the EFA installer. If it's using the internal Libfabric, the version is suffixed with impi. Use libfabric provider to check with Intel MPI is using EFA or the TCP/IP network. If it's using EFA, the value is efa. If it's using TCP/IP, the value is tcp;ofi_rxm.
To enable debugging information, do one of the following depending on your shell. bash shells Add the following statement to /home/username/.bashrc and / home/username/.bash_profile. export I_MPI_DEBUG=value csh and tcsh shells Add the following statement to /home/username/.cshrc. setenv I_MPI_DEBUG value
10. By default, Intel MPI uses the operating system's shared memory (shm) for intra-node communication, and it uses Libfabric (ofi) only for inter-node communication. Generally, this configuration provides the best performance. However, in some cases the Intel MPI shm fabric can cause certain applications to hang indefinitely.
To resolve this issue, you can force Intel MPI to use Libfabric for both intra-node and inter- node communication. To do this, do one of the following depending on your shell. bash shells Add the following statement to /home/username/.bashrc and / home/username/.bash_profile.

export I_MPI_FABRICS=ofi csh and tcsh shells Add the following statement to /home/username/.cshrc. setenv I_MPI_FABRICS ofi Note The EFA Libfabric provider uses the operating system's shared memory for intra- node communication. This means that setting I_MPI_FABRICS to ofi yields similar performance to the default shm:ofi configuration.
11. Log out of the instance and then log back in.
If you no longer want to use Intel MPI, remove the environment variables from the shell startup scripts.
### Step 6: Disable ptrace protection To improve your HPC application's performance, Libfabric uses the instance's local memory for interprocess communications when the processes are running on the same instance.
The shared memory feature uses Cross Memory Attach (CMA), which is not supported with ptrace protection. If you are using a Linux distribution that has ptrace protection enabled by default, such as Ubuntu, you must disable it. If your Linux distribution does not have ptrace protection enabled by default, skip this step.
To disable ptrace protection Do one of the following:
- To temporarily disable ptrace protection for testing purposes, run the following command.
$ sudo sysctl -w kernel.yama.ptrace_scope=0

- To permanently disable ptrace protection, add kernel.yama.ptrace_scope = 0 to /etc/ sysctl.d/10-ptrace.conf and reboot the instance.
### Step 7. Confirm installation To confirm successful installation
1. To confirm that MPI was successfully installed, run the following command:
$ which mpicc
- For Open MPI, the returned path should include /opt/amazon/
- For Intel MPI, the returned path should include /opt/intel/. If you do not get the expected output, ensure that you have sourced the Intel MPI vars.sh script.
2. To confirm that the EFA software components and Libfabric were successfully installed, run the following command.
$ fi_info -p efa -t FI_EP_RDM The command should return information about the Libfabric EFA interfaces. The following example shows the command output. provider: efa fabric: EFA-fe80::94:3dff:fe89:1b70 domain: efa_0-rdm version: 2.0 type: FI_EP_RDM protocol: FI_PROTO_EFA
### Step 8: Install your HPC application Install the HPC application on the temporary instance. The installation procedure varies depending on the specific HPC application. For more information, see Manage software on your AL2 instance in the Amazon Linux 2 User Guide.

Note Refer to your HPC application's documentation for installation instructions.
### Step 9: Create an EFA-enabled AMI After you have installed the required software components, you create an AMI that you can reuse to launch your EFA-enabled instances.
To create an AMI from your temporary instance
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Instances.
3. Select the temporary instance that you created and choose Actions, Image, Create image.
4. For Create image, do the following: a.
For Image name, enter a descriptive name for the AMI. b.
(Optional) For Image description, enter a brief description of the purpose of the AMI. c.
Choose Create image.
5. In the navigation pane, choose AMIs.
6. Locate the AMI tht you created in the list. Wait for the status to change from pending to available before continuing to the next step.
### Step 10: Launch EFA-enabled instances into a cluster placement group Launch your EFA-enabled instances into a cluster placement group using the EFA-enabled AMI that you created in Step 7, and the EFA-enabled security group that you created in Step 1.
Note
- It is not an absolute requirement to launch your EFA-enabled instances into a cluster placement group. However, we do recommend running your EFA-enabled instances in a cluster placement group as it launches the instances into a low-latency group in a single Availability Zone.

- To ensure that capacity is available as you scale your cluster's instances, you can create a Capacity Reservation for your cluster placement group. For more information, see Use Capacity Reservations with cluster placement groups.
To launch an instance
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Instances, and then choose Launch Instances to open the new launch instance wizard.
3. (Optional) In the Name and tags section, provide a name for the instance, such as EFA- instance. The name is assigned to the instance as a resource tag (Name=EFA-instance).
4. In the Application and OS Images section, choose My AMIs, and then select the AMI that you created in the previous step.
5. In the Instance type section, select a supported instance type.
6. In the Key pair section, select the key pair to use for the instance.
7. In the Network settings section, choose Edit, and then do the following: a.
For Subnet, choose the subnet in which to launch the instance. If you do not select a subnet, you can't enable the instance for EFA. b.
For Firewall (security groups), choose Select existing security group, and then select the security group that you created in the previous step. c.
Expand the Advanced network configuration section.
For Network interface 1, select Network card index = 0, Device index = 0, and Interface type = EFA with ENA.
(Optional) If you are using a multi-card instance type, such as p4d.24xlarge or p5.48xlarge, for each additional network interface required, choose Add network interface, for Network card index select the next unused index, and then select Device index = 1 and Interface type = EFA with ENA or EFA-only.
8. (Optional) In the Storage section, configure the volumes as needed.
9. In the Advanced details section, for Placement group name, select the cluster placement group into which to launch the instances. If you need to create a new cluster placement group, choose Create new placement group.

10. In the Summary panel on the right, for Number of instances, enter the number of EFA- enabled instances that you want to launch, and then choose Launch instance.
### Step 11: Terminate the temporary instance At this point, you no longer need the instance that you launched in Step 2. You can terminate the instance to stop incurring charges for it.
To terminate the temporary instance
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Instances.
3. Select the temporary instance that you created and then choose Actions, Instance state, Terminate (delete) instance.
4. When prompted for confirmation, choose Terminate (delete).
### Step 12: Enable passwordless SSH To enable your applications to run across all of the instances in your cluster, you must enable passwordless SSH access from the leader node to the member nodes. The leader node is the instance from which you run your applications. The remaining instances in the cluster are the member nodes.
To enable passwordless SSH between the instances in the cluster
1. Select one instance in the cluster as the leader node, and connect to it.
2. Disable strictHostKeyChecking and enable ForwardAgent on the leader node. Open ~/.ssh/config using your preferred text editor and add the following.
Host * ForwardAgent yes Host * StrictHostKeyChecking no
3. Generate an RSA key pair.
$ ssh-keygen -t rsa -N "" -f ~/.ssh/id_rsa

The key pair is created in the $HOME/.ssh/ directory.
4. Change the permissions of the private key on the leader node.
$ chmod 600 ~/.ssh/id_rsa chmod 600 ~/.ssh/config
5. Open ~/.ssh/id_rsa.pub using your preferred text editor and copy the key.
6. For each member node in the cluster, do the following: a.
Connect to the instance. b.
Open ~/.ssh/authorized_keys using your preferred text editor and add the public key that you copied earlier.
7. To test that the passwordless SSH is functioning as expected, connect to your leader node and run the following command.
$ ssh member_node_private_ip You should connect to the member node without being prompted for a key or password.
## Get started with EFA and NCCL for ML workloads on Amazon EC2 The NVIDIA Collective Communications Library (NCCL) is a library of standard collective communication routines for multiple GPUs across a single node or multiple nodes. NCCL can be used together with EFA, Libfabric, and MPI to support various machine learning workloads. For more information, see the NCCL website.
Requirements
- Only accelerated computing P series instance types are supported. For more information, see Amazon EC2 accelerated computing instances.
- Only Amazon Linux 2023, Amazon Linux 2, Ubuntu 24.04, and Ubuntu 22.04 base AMIs are supported.
- Only NCCL 2.4.2 and later is supported with EFA.
For more information about running machine learning workloads with EFA and NCCL using an AWS Deep Learning AMIs, see  Using EFA on the DLAMI in the AWS Deep Learning AMIs Developer Guide.

Steps
- Step 1: Prepare an EFA-enabled security group
- Step 2: Launch a temporary instance
- Step 3: Install Nvidia GPU drivers, Nvidia CUDA toolkit, and cuDNN
- Step 4: Install GDRCopy
- Step 5: Install the EFA software
- Step 6: Install NCCL
- Step 7: Install the NCCL tests
- Step 8: Test your EFA and NCCL configuration
- Step 9: Install your machine learning applications
- Step 10: Create an EFA and NCCL-enabled AMI
- Step 11: Terminate the temporary instance
- Step 12: Launch EFA and NCCL-enabled instances into a cluster placement group
- Step 13: Enable passwordless SSH
### Step 1: Prepare an EFA-enabled security group An EFA requires a security group that allows all inbound and outbound traffic to and from the security group itself. The following procedure creates a security group that allows all inbound and outbound traffic to and from itself, and that allows inbound SSH traffic from any IPv4 address for SSH connectivity.
Important This security group is intended for testing purposes only. For your production environments, we recommend that you create an inbound SSH rule that allows traffic only from the IP address from which you are connecting, such as the IP address of your computer, or a range of IP addresses in your local network.
For other scenarios, see Security group rules for different use cases.
To create an EFA-enabled security group
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.

2. In the navigation pane, choose Security Groups and then choose Create security group.
3. In the Create security group window, do the following: a.
For Security group name, enter a descriptive name for the security group, such as EFA- enabled security group. b.
(Optional) For Description, enter a brief description of the security group. c.
For VPC, select the VPC into which you intend to launch your EFA-enabled instances. d.
Choose Create security group.
4. Select the security group that you created, and on the Details tab, copy the Security group ID.
5. With the security group still selected, choose Actions, Edit inbound rules, and then do the following: a.
Choose Add rule. b.
For Type, choose All traffic. c.
For Source type, choose Custom and paste the security group ID that you copied into the field. d.
Choose Add rule. e.
For Type, choose SSH. f.
For Source type, choose Anywhere-IPv4. g.
Choose Save rules.
6. With the security group still selected, choose Actions, Edit outbound rules, and then do the following: a.
Choose Add rule. b.
For Type, choose All traffic. c.
For Destination type, choose Custom and paste the security group ID that you copied into the field. d.
Choose Save rules.
### Step 2: Launch a temporary instance Launch a temporary instance that you can use to install and configure the EFA software components. You use this instance to create an EFA-enabled AMI from which you can launch your EFA-enabled instances.

To launch a temporary instance
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Instances, and then choose Launch Instances to open the new launch instance wizard.
3. (Optional) In the Name and tags section, provide a name for the instance, such as EFA- instance. The name is assigned to the instance as a resource tag (Name=EFA-instance).
4. In the Application and OS Images section, select an AMI for one of the supported operating systems.
5. In the Instance type section, select a supported instance type.
6. In the Key pair section, select the key pair to use for the instance.
7. In the Network settings section, choose Edit, and then do the following: a.
For Subnet, choose the subnet in which to launch the instance. If you do not select a subnet, you can't enable the instance for EFA. b.
For Firewall (security groups), choose Select existing security group, and then select the security group that you created in the previous step. c.
Expand the Advanced network configuration section.
For Network interface 1, select Network card index = 0, Device index = 0, and Interface type = EFA with ENA.
(Optional) If you are using a multi-card instance type, such as p4d.24xlarge or p5.48xlarge, for each additional network interface required, choose Add network interface, for Network card index select the next unused index, and then select Device index = 1 and Interface type = EFA with ENA or EFA-only.
8. In the Storage section, configure the volumes as needed.
Note You must provision an additional 10 to 20 GiB of storage for the Nvidia CUDA Toolkit.
If you do not provision enough storage, you will receive an insufficient disk space error when attempting to install the Nvidia drivers and CUDA toolkit.
9. In the Summary panel on the right, choose Launch instance.

### Step 3: Install Nvidia GPU drivers, Nvidia CUDA toolkit, and cuDNN Amazon Linux 2023 and Amazon Linux 2 To install the Nvidia GPU drivers, Nvidia CUDA toolkit, and cuDNN
1. To ensure that all of your software packages are up to date, perform a quick software update on your instance.
$ sudo yum upgrade -y && sudo reboot After the instance has rebooted, reconnect to it.
2. Install the utilities that are needed to install the Nvidia GPU drivers and the Nvidia CUDA toolkit.
$ sudo yum groupinstall 'Development Tools' -y
3. Disable the nouveau open source drivers. a.
Install the required utilities and the kernel headers package for the version of the kernel that you are currently running.
$ sudo yum install -y wget kernel-devel-$(uname -r) kernel-headers-$(uname - r) b.
Add nouveau to the /etc/modprobe.d/blacklist.conf deny list file.
$ cat << EOF | sudo tee --append /etc/modprobe.d/blacklist.conf blacklist vga16fb blacklist nouveau blacklist rivafb blacklist nvidiafb blacklist rivatv EOF c.
Append GRUB_CMDLINE_LINUX="rdblacklist=nouveau" to the grub file and rebuild the Grub configuration.
$ echo 'GRUB_CMDLINE_LINUX="rdblacklist=nouveau"' | sudo tee -a /etc/ default/grub \

&& sudo grub2-mkconfig -o /boot/grub2/grub.cfg
4. Reboot the instance and reconnect to it.
5. Prepare the required repositories a.
Enable the EPEL repository and set the distribution to rhel7.
$ sudo amazon-linux-extras install epel \ && distribution='rhel7' b.
Set up the CUDA network repository and update the repository cache.
$ ARCH=$( /bin/arch ) \ && sudo yum-config-manager --add-repo http://developer.download.nvidia.com/ compute/cuda/repos/$distribution/${ARCH}/cuda-$distribution.repo \ && sudo yum clean expire-cache c.
(Kernel version 5.10 only) Perform these steps only if you are using Amazon Linux 2 with kernel version 5.10. If you are using Amazon Linux 2 with kernel version 4.12, skip these steps. To check your kernel version, run uname -r. i.
Create the Nvidia driver configuration file named /etc/dkms/nvidia.conf.
$ sudo mkdir -p /etc/dkms \ && echo "MAKE[0]=\"'make' -j2 module SYSSRC=\${kernel_source_dir} IGNORE_XEN_PRESENCE=1 IGNORE_PREEMPT_RT_PRESENCE=1 IGNORE_CC_MISMATCH=1 CC=/usr/bin/gcc10-gcc\"" | sudo tee /etc/dkms/nvidia.conf ii.
(p4d.24xlarge and p5.48xlarge only) Copy the Nvidia driver configuration file.
$ sudo cp /etc/dkms/nvidia.conf /etc/dkms/nvidia-open.conf
6. Install the Nvidia GPU drivers, NVIDIA CUDA toolkit, and cuDNN.
$ sudo yum clean all \ && sudo yum -y install nvidia-driver-latest-dkms \ && sudo yum -y install cuda-drivers-fabricmanager cuda libcudnn8-devel
7. Reboot the instance and reconnect to it.

8. (p4d.24xlarge and p5.48xlarge only) Start the Nvidia Fabric Manager service, and ensure that it starts automatically when the instance starts. Nvidia Fabric Manager is required for NV Switch Management.
$ sudo systemctl enable nvidia-fabricmanager && sudo systemctl start nvidia- fabricmanager
9. Ensure that the CUDA paths are set each time that the instance starts.
- For bash shells, add the following statements to /home/username/.bashrc and / home/username/.bash_profile. export PATH=/usr/local/cuda/bin:$PATH export LD_LIBRARY_PATH=/usr/local/cuda/lib64:/usr/local/cuda/extras/CUPTI/ lib64:$LD_LIBRARY_PATH
- For tcsh shells, add the following statements to /home/username/.cshrc. setenv PATH=/usr/local/cuda/bin:$PATH setenv LD_LIBRARY_PATH=/usr/local/cuda/lib64:/usr/local/cuda/extras/CUPTI/ lib64:$LD_LIBRARY_PATH
10. To confirm that the Nvidia GPU drivers are functional, run the following command.
$ nvidia-smi -q | head The command should return information about the Nvidia GPUs, Nvidia GPU drivers, and Nvidia CUDA toolkit.
Ubuntu 24.04 and Ubuntu 22.04 To install the Nvidia GPU drivers, Nvidia CUDA toolkit, and cuDNN
1. To ensure that all of your software packages are up to date, perform a quick software update on your instance.
$ sudo apt-get update && sudo apt-get upgrade -y
2. Install the utilities that are needed to install the Nvidia GPU drivers and the Nvidia CUDA toolkit.

$ sudo apt-get update && sudo apt-get install build-essential -y
3. To use the Nvidia GPU driver, you must first disable the nouveau open source drivers. a.
Install the required utilities and the kernel headers package for the version of the kernel that you are currently running.
$ sudo apt-get install -y gcc make linux-headers-$(uname -r) b.
Add nouveau to the /etc/modprobe.d/blacklist.conf deny list file.
$ cat << EOF | sudo tee --append /etc/modprobe.d/blacklist.conf blacklist vga16fb blacklist nouveau blacklist rivafb blacklist nvidiafb blacklist rivatv EOF c.
Open /etc/default/grub using your preferred text editor and add the following.
GRUB_CMDLINE_LINUX="rdblacklist=nouveau" d.
Rebuild the Grub configuration.
$ sudo update-grub
4. Reboot the instance and reconnect to it.
5. Add the CUDA repository and install the Nvidia GPU drivers, NVIDIA CUDA toolkit, and cuDNN.
- p3dn.24xlarge $ sudo apt-key adv --fetch-keys http://developer.download.nvidia.com/compute/ machine-learning/repos/ubuntu2004/x86_64/7fa2af80.pub \ && wget -O /tmp/deeplearning.deb http://developer.download.nvidia.com/compute/ machine-learning/repos/ubuntu2004/x86_64/nvidia-machine-learning-repo- ubuntu2004_1.0.0-1_amd64.deb \ && sudo dpkg -i /tmp/deeplearning.deb \ && wget -O /tmp/cuda.pin https://developer.download.nvidia.com/compute/cuda/ repos/ubuntu2004/x86_64/cuda-ubuntu2004.pin \

&& sudo mv /tmp/cuda.pin /etc/apt/preferences.d/cuda-repository-pin-600 \ && sudo apt-key adv --fetch-keys https://developer.download.nvidia.com/ compute/cuda/repos/ubuntu2004/x86_64/3bf863cc.pub \ && sudo add-apt-repository 'deb http://developer.download.nvidia.com/compute/ cuda/repos/ubuntu2004/x86_64/ /' \ && sudo apt update \ && sudo apt install nvidia-dkms-535 \ && sudo apt install -o Dpkg::Options::='--force-overwrite' cuda-drivers-535 cuda-toolkit-12-3 libcudnn8 libcudnn8-dev -y
- p4d.24xlarge and p5.48xlarge $ sudo apt-key adv --fetch-keys http://developer.download.nvidia.com/compute/ machine-learning/repos/ubuntu2004/x86_64/7fa2af80.pub \ && wget -O /tmp/deeplearning.deb http://developer.download.nvidia.com/compute/ machine-learning/repos/ubuntu2004/x86_64/nvidia-machine-learning-repo- ubuntu2004_1.0.0-1_amd64.deb \ && sudo dpkg -i /tmp/deeplearning.deb \ && wget -O /tmp/cuda.pin https://developer.download.nvidia.com/compute/cuda/ repos/ubuntu2004/x86_64/cuda-ubuntu2004.pin \ && sudo mv /tmp/cuda.pin /etc/apt/preferences.d/cuda-repository-pin-600 \ && sudo apt-key adv --fetch-keys https://developer.download.nvidia.com/ compute/cuda/repos/ubuntu2004/x86_64/3bf863cc.pub \ && sudo add-apt-repository 'deb http://developer.download.nvidia.com/compute/ cuda/repos/ubuntu2004/x86_64/ /' \ && sudo apt update \ && sudo apt install nvidia-kernel-open-535 \ && sudo apt install -o Dpkg::Options::='--force-overwrite' cuda-drivers-535 cuda-toolkit-12-3 libcudnn8 libcudnn8-dev -y
6. Reboot the instance and reconnect to it.
7. (p4d.24xlarge and p5.48xlarge only) Install the Nvidia Fabric Manager. a.
You must install the version of the Nvidia Fabric Manager that matches the version of the Nvidia kernel module that you installed in the previous step.
Run the following command to determine the version of the Nvidia kernel module.
$ cat /proc/driver/nvidia/version | grep "Kernel Module"
The following is example output.

NVRM version: NVIDIA UNIX x86_64 Kernel Module   450.42.01  Tue Jun 15 21:26:37 UTC 2021 In the example above, major version 450 of the kernel module was installed. This means that you need to install Nvidia Fabric Manager version 450. b.
Install the Nvidia Fabric Manager. Run the following command and specify the major version identified in the previous step.
$ sudo apt install -o Dpkg::Options::='--force-overwrite' nvidia- fabricmanager-major_version_number For example, if major version 450 of the kernel module was installed, use the following command to install the matching version of Nvidia Fabric Manager.
$ sudo apt install -o Dpkg::Options::='--force-overwrite' nvidia- fabricmanager-450 c.
Start the service, and ensure that it starts automatically when the instance starts.
Nvidia Fabric Manager is required for NV Switch Management.
$ sudo systemctl start nvidia-fabricmanager && sudo systemctl enable nvidia- fabricmanager
8. Ensure that the CUDA paths are set each time that the instance starts.
- For bash shells, add the following statements to /home/username/.bashrc and / home/username/.bash_profile. export PATH=/usr/local/cuda/bin:$PATH export LD_LIBRARY_PATH=/usr/local/cuda/lib64:/usr/local/cuda/extras/CUPTI/ lib64:$LD_LIBRARY_PATH
- For tcsh shells, add the following statements to /home/username/.cshrc. setenv PATH=/usr/local/cuda/bin:$PATH setenv LD_LIBRARY_PATH=/usr/local/cuda/lib64:/usr/local/cuda/extras/CUPTI/ lib64:$LD_LIBRARY_PATH
9. To confirm that the Nvidia GPU drivers are functional, run the following command.

$ nvidia-smi -q | head The command should return information about the Nvidia GPUs, Nvidia GPU drivers, and Nvidia CUDA toolkit.
### Step 4: Install GDRCopy Install GDRCopy to improve the performance of Libfabric. For more information about GDRCopy, see the GDRCopy repository.
Amazon Linux 2023 and Amazon Linux 2 To install GDRCopy
1. Install the required dependencies.
$ sudo yum -y install dkms rpm-build make check check-devel subunit subunit- devel
2. Download and extract the GDRCopy package.
$ wget https://github.com/NVIDIA/gdrcopy/archive/refs/tags/v2.4.tar.gz \ && tar xf v2.4.tar.gz ; cd gdrcopy-2.4/packages
3. Build the GDRCopy RPM package.
$ CUDA=/usr/local/cuda ./build-rpm-packages.sh
4. Install the GDRCopy RPM package.
$ sudo rpm -Uvh gdrcopy-kmod-2.4-1dkms.noarch*.rpm \ && sudo rpm -Uvh gdrcopy-2.4-1.x86_64*.rpm \ && sudo rpm -Uvh gdrcopy-devel-2.4-1.noarch*.rpm Ubuntu 24.04 and Ubuntu 22.04 To install GDRCopy
1. Install the required dependencies.

$ sudo apt -y install build-essential devscripts debhelper check libsubunit-dev fakeroot pkg-config dkms
2. Download and extract the GDRCopy package.
$ wget https://github.com/NVIDIA/gdrcopy/archive/refs/tags/v2.4.tar.gz \ && tar xf v2.4.tar.gz \ && cd gdrcopy-2.4/packages
3. Build the GDRCopy RPM package.
$ CUDA=/usr/local/cuda ./build-deb-packages.sh
4. Install the GDRCopy RPM package.
$ sudo dpkg -i gdrdrv-dkms_2.4-1_amd64.*.deb \ && sudo dpkg -i libgdrapi_2.4-1_amd64.*.deb \ && sudo dpkg -i gdrcopy-tests_2.4-1_amd64.*.deb \ && sudo dpkg -i gdrcopy_2.4-1_amd64.*.deb
### Step 5: Install the EFA software Install the EFA-enabled kernel, EFA drivers, Libfabric, aws-ofi-nccl plugin, and Open MPI stack that is required to support EFA on your instance.
To install the EFA software
1. Connect to the instance you launched. For more information, see Connect to your Linux instance using SSH.
2. Download the EFA software installation files. The software installation files are packaged into a compressed tarball (.tar.gz) file. To download the latest stable version, use the following command.
You can also get the latest version by replacing the version number with latest in the preceding command.
$ curl -O https://efa-installer.amazonaws.com/aws-efa-installer-1.47.0.tar.gz
3. (Optional) Verify the authenticity and integrity of the EFA tarball (.tar.gz) file.

We recommend that you do this to verify the identity of the software publisher and to check that the file has not been altered or corrupted since it was published. If you do not want to verify the tarball file, skip this step.
Note Alternatively, if you prefer to verify the tarball file by using an MD5 or SHA256 checksum instead, see Verify the EFA installer using a checksum. a.
Download the public GPG key and import it into your keyring.
$ wget https://efa-installer.amazonaws.com/aws-efa-installer.key && gpg -- import aws-efa-installer.key The command should return a key value. Make a note of the key value, because you need it in the next step. b.
Verify the GPG key's fingerprint. Run the following command and specify the key value from the previous step.
$ gpg --fingerprint key_value The command should return a fingerprint that is identical to 4E90 91BC BB97 A96B 26B1 5E59 A054 80B1 DD2D 3CCC. If the fingerprint does not match, don't run the EFA installation script, and contact Support. c.
Download the signature file and verify the signature of the EFA tarball file.
$ wget https://efa-installer.amazonaws.com/aws-efa-installer-1.47.0.tar.gz.sig && gpg --verify ./aws-efa-installer-1.47.0.tar.gz.sig The following shows example output. gpg: Signature made Wed 29 Jul 2020 12:50:13 AM UTC using RSA key ID DD2D3CCC gpg: Good signature from "Amazon EC2 EFA <ec2-efa-maintainers@amazon.com>" gpg: WARNING: This key is not certified with a trusted signature! gpg:          There is no indication that the signature belongs to the owner.

Primary key fingerprint: 4E90 91BC BB97 A96B 26B1  5E59 A054 80B1 DD2D 3CCC If the result includes Good signature, and the fingerprint matches the fingerprint returned in the previous step, proceed to the next step. If not, don't run the EFA installation script, and contact Support.
4. Extract the files from the compressed .tar.gz file and navigate into the extracted directory.
$ tar -xf aws-efa-installer-1.47.0.tar.gz && cd aws-efa-installer
5. Run the EFA software installation script.
Note From EFA 1.30.0, both Open MPI 4.1 and Open MPI 5 are installed by default. Unless you need Open MPI 5, we recommend that you install only Open MPI 4.1. The following command installs Open MPI 4.1 only. If you want to install Open MPI 4.1 and Open MPI 5, remove --mpi=openmpi4.
$ sudo ./efa_installer.sh -y --mpi=openmpi4 Libfabric is installed in the /opt/amazon/efa directory. The aws-ofi-nccl plugin is installed in the /opt/amazon/ofi-nccl directory. Open MPI is installed in the /opt/amazon/ openmpi directory.
6. If the EFA installer prompts you to reboot the instance, do so and then reconnect to the instance. Otherwise, log out of the instance and then log back in to complete the installation.
7. Confirm that the EFA software components were successfully installed.
$ fi_info -p efa -t FI_EP_RDM The command should return information about the Libfabric EFA interfaces. The following example shows the command output.
- p3dn.24xlarge with single network interface provider: efa fabric: EFA-fe80::94:3dff:fe89:1b70

domain: efa_0-rdm version: 2.0 type: FI_EP_RDM protocol: FI_PROTO_EFA
- p4d.24xlarge and p5.48xlarge with multiple network interfaces provider: efa fabric: EFA-fe80::c6e:8fff:fef6:e7ff domain: efa_0-rdm version: 111.0 type: FI_EP_RDM protocol: FI_PROTO_EFA provider: efa fabric: EFA-fe80::c34:3eff:feb2:3c35 domain: efa_1-rdm version: 111.0 type: FI_EP_RDM protocol: FI_PROTO_EFA provider: efa fabric: EFA-fe80::c0f:7bff:fe68:a775 domain: efa_2-rdm version: 111.0 type: FI_EP_RDM protocol: FI_PROTO_EFA provider: efa fabric: EFA-fe80::ca7:b0ff:fea6:5e99 domain: efa_3-rdm version: 111.0 type: FI_EP_RDM protocol: FI_PROTO_EFA
### Step 6: Install NCCL Install NCCL. For more information about NCCL, see the NCCL repository.
To install NCCL
1. Navigate to the /opt directory.
$ cd /opt

2. Clone the official NCCL repository to the instance and navigate into the local cloned repository.
$ sudo git clone https://github.com/NVIDIA/nccl.git -b v2.23.4-1 && cd nccl
3. Build and install NCCL and specify the CUDA installation directory.
$ sudo make -j src.build CUDA_HOME=/usr/local/cuda
### Step 7: Install the NCCL tests Install the NCCL tests. The NCCL tests enable you to confirm that NCCL is properly installed and that it is operating as expected. For more information about the NCCL tests, see the nccl-tests repository.
To install the NCCL tests
1. Navigate to your home directory.
$ cd $HOME
2. Clone the official nccl-tests repository to the instance and navigate into the local cloned repository.
$ git clone https://github.com/NVIDIA/nccl-tests.git && cd nccl-tests
3. Add the Libfabric directory to the LD_LIBRARY_PATH variable.
- Amazon Linux 2023 and Amazon Linux 2 $ export LD_LIBRARY_PATH=/opt/amazon/efa/lib64:$LD_LIBRARY_PATH
- Ubuntu 24.04 and Ubuntu 22.04 $ export LD_LIBRARY_PATH=/opt/amazon/efa/lib:$LD_LIBRARY_PATH
4. Install the NCCL tests and specify the MPI, NCCL, and CUDA installation directories.
$ make MPI=1 MPI_HOME=/opt/amazon/openmpi NCCL_HOME=/opt/nccl/build CUDA_HOME=/usr/ local/cuda

### Step 8: Test your EFA and NCCL configuration Run a test to ensure that your temporary instance is properly configured for EFA and NCCL.
To test your EFA and NCCL configuration
1. Create a host file that specifies the hosts on which to run the tests. The following command creates a host file named my-hosts that includes a reference to the instance itself.
IMDSv2 [ec2-user ~]$ TOKEN=`curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600"` \ && curl -H "X-aws-ec2-metadata-token: $TOKEN" -v http://169.254.169.254/latest/ meta-data/local-ipv4 >> my-hosts IMDSv1 [ec2-user ~]$ curl http://169.254.169.254/latest/meta-data/local-ipv4 >> my- hosts
2. Run the test and specify the host file (--hostfile) and the number of GPUs to use (-n). The following command runs the all_reduce_perf test on 8 GPUs on the instance itself, and specifies the following environment variables.
- FI_EFA_USE_DEVICE_RDMA=1—(p4d.24xlarge only) uses the device's RDMA functionality for one-sided and two-sided transfer.
- NCCL_DEBUG=INFO—enables detailed debugging output. You can also specify VERSION to print only the NCCL version at the start of the test, or WARN to receive only error messages.
For more information about the NCCL test arguments, see the NCCL Tests README in the official nccl-tests repository.
- p3dn.24xlarge $ /opt/amazon/openmpi/bin/mpirun \ -x LD_LIBRARY_PATH=/opt/nccl/build/lib:/usr/local/cuda/lib64:/opt/amazon/efa/ lib:/opt/amazon/openmpi/lib:/opt/amazon/ofi-nccl/lib:$LD_LIBRARY_PATH \ -x NCCL_DEBUG=INFO \ --hostfile my-hosts -n 8 -N 8 \

--mca pml ^cm --mca btl tcp,self --mca btl_tcp_if_exclude lo,docker0 --bind-to none \ $HOME/nccl-tests/build/all_reduce_perf -b 8 -e 1G -f 2 -g 1 -c 1 -n 100
- p4d.24xlarge and p5.48xlarge $ /opt/amazon/openmpi/bin/mpirun \ -x FI_EFA_USE_DEVICE_RDMA=1 \ -x LD_LIBRARY_PATH=/opt/nccl/build/lib:/usr/local/cuda/lib64:/opt/amazon/efa/ lib:/opt/amazon/openmpi/lib:/opt/amazon/ofi-nccl/lib:$LD_LIBRARY_PATH \ -x NCCL_DEBUG=INFO \ --hostfile my-hosts -n 8 -N 8 \ --mca pml ^cm --mca btl tcp,self --mca btl_tcp_if_exclude lo,docker0 --bind-to none \ $HOME/nccl-tests/build/all_reduce_perf -b 8 -e 1G -f 2 -g 1 -c 1 -n 100
3. You can confirm that EFA is active as the underlying provider for NCCL when the NCCL_DEBUG log is printed. ip-192-168-2-54:14:14 [0] NCCL INFO NET/OFI Selected Provider is efa* The following additional information is displayed when using a p4d.24xlarge instance. ip-192-168-2-54:14:14 [0] NCCL INFO NET/OFI Running on P4d platform, Setting NCCL_TOPO_FILE environment variable to /home/ec2-user/install/plugin/share/aws- ofi-nccl/xml/p4d-24xl-topo.xml
### Step 9: Install your machine learning applications Install the machine learning applications on the temporary instance. The installation procedure varies depending on the specific machine learning application. For more information about installing software on your Linux instance, see Manage software on your Amazon Linux 2 instance.
Note Refer to your machine learning application's documentation for installation instructions.

### Step 10: Create an EFA and NCCL-enabled AMI After you have installed the required software components, you create an AMI that you can reuse to launch your EFA-enabled instances.
To create an AMI from your temporary instance
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Instances.
3. Select the temporary instance that you created and choose Actions, Image, Create image.
4. For Create image, do the following: a.
For Image name, enter a descriptive name for the AMI. b.
(Optional) For Image description, enter a brief description of the purpose of the AMI. c.
Choose Create image.
5. In the navigation pane, choose AMIs.
6. Locate the AMI tht you created in the list. Wait for the status to change from pending to available before continuing to the next step.
### Step 11: Terminate the temporary instance At this point, you no longer need the temporary instance that you launched. You can terminate the instance to stop incurring charges for it.
To terminate the temporary instance
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Instances.
3. Select the temporary instance that you created and then choose Actions, Instance state, Terminate instance.
4. When prompted for confirmation, choose Terminate.
### Step 12: Launch EFA and NCCL-enabled instances into a cluster placement group Launch your EFA and NCCL-enabled instances into a cluster placement group using the EFA- enabled AMI and the EFA-enabled security group that you created earlier.

Note
- It is not an absolute requirement to launch your EFA-enabled instances into a cluster placement group. However, we do recommend running your EFA-enabled instances in a cluster placement group as it launches the instances into a low-latency group in a single Availability Zone.
- To ensure that capacity is available as you scale your cluster's instances, you can create a Capacity Reservation for your cluster placement group. For more information, see Use Capacity Reservations with cluster placement groups.
New console To launch a temporary instance
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Instances, and then choose Launch Instances to open the new launch instance wizard.
3. (Optional) In the Name and tags section, provide a name for the instance, such as EFA- instance. The name is assigned to the instance as a resource tag (Name=EFA-instance).
4. In the Application and OS Images section, choose My AMIs, and then select the AMI that you created in the previous step.
5. In the Instance type section, select either p3dn.24xlarge or p4d.24xlarge.
6. In the Key pair section, select the key pair to use for the instance.
7. In the Network settings section, choose Edit, and then do the following: a.
For Subnet, choose the subnet in which to launch the instance. If you do not select a subnet, you can't enable the instance for EFA. b.
For Firewall (security groups), choose Select existing security group, and then select the security group that you created in the previous step. c.
Expand the Advanced network configuration section.
For Network interface 1, select Network card index = 0, Device index = 0, and Interface type = EFA with ENA.

(Optional) If you are using a multi-card instance type, such as p4d.24xlarge or p5.48xlarge, for each additional network interface required, choose Add network interface, for Network card index select the next unused index, and then select Device index = 1 and Interface type = EFA eith ENA or EFA-only.
8. (Optional) In the Storage section, configure the volumes as needed.
9. In the Advanced details section, for Placement group name, select the cluster placement group into which to launch the instance. If you need to create a new cluster placement group, choose Create new placement group.
10. In the Summary panel on the right, for Number of instances, enter the number of EFA- enabled instances that you want to launch, and then choose Launch instance.
Old console To launch your EFA and NCCL-enabled instances into a cluster placement group
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. Choose Launch Instance.
3. On the Choose an AMI page, choose My AMIs, find the AMI that you created earlier, and then choose Select.
4. On the Choose an Instance Type page, select p3dn.24xlarge and then choose Next:
Configure Instance Details.
5. On the Configure Instance Details page, do the following: a.
For Number of instances, enter the number of EFA and NCCL-enabled instances that you want to launch. b.
For Network and Subnet, select the VPC and subnet into which to launch the instances. c.
For Placement group, select Add instance to placement group. d.
For Placement group name, select Add to a new placement group, and then enter a descriptive name for the placement group. Then for Placement group strategy, select cluster. e.
For EFA, choose Enable. f.
In the Network Interfaces section, for device eth0, choose New network interface.
You can optionally specify a primary IPv4 address and one or more secondary IPv4

addresses. If you are launching the instance into a subnet that has an associated IPv6 CIDR block, you can optionally specify a primary IPv6 address and one or more secondary IPv6 addresses. g.
Choose Next: Add Storage.
6. On the Add Storage page, specify the volumes to attach to the instances in addition to the volumes specified by the AMI (such as the root device volume). Then choose Next: Add Tags.
7. On the Add Tags page, specify tags for the instances, such as a user-friendly name, and then choose Next: Configure Security Group.
8. On the Configure Security Group page, for Assign a security group, select Select an existing security group, and then select the security group that you created earlier.
9. Choose Review and Launch.
10. On the Review Instance Launch page, review the settings, and then choose Launch to choose a key pair and to launch your instances.
### Step 13: Enable passwordless SSH To enable your applications to run across all of the instances in your cluster, you must enable passwordless SSH access from the leader node to the member nodes. The leader node is the instance from which you run your applications. The remaining instances in the cluster are the member nodes.
To enable passwordless SSH between the instances in the cluster
1. Select one instance in the cluster as the leader node, and connect to it.
2. Disable strictHostKeyChecking and enable ForwardAgent on the leader node. Open ~/.ssh/config using your preferred text editor and add the following.
Host * ForwardAgent yes Host * StrictHostKeyChecking no
3. Generate an RSA key pair.
$ ssh-keygen -t rsa -N "" -f ~/.ssh/id_rsa

The key pair is created in the $HOME/.ssh/ directory.
4. Change the permissions of the private key on the leader node.
$ chmod 600 ~/.ssh/id_rsa chmod 600 ~/.ssh/config
5. Open ~/.ssh/id_rsa.pub using your preferred text editor and copy the key.
6. For each member node in the cluster, do the following: a.
Connect to the instance. b.
Open ~/.ssh/authorized_keys using your preferred text editor and add the public key that you copied earlier.
7. To test that the passwordless SSH is functioning as expected, connect to your leader node and run the following command.
$ ssh member_node_private_ip You should connect to the member node without being prompted for a key or password.
## Maximize network bandwidth on Amazon EC2 instances with multiple network cards network cards Many instances types that support EFA also have multiple network cards. For more information, see Network cards. If you plan to use EFA with one of these instance types, we recommend the following basic configuration:
- For the primary network interface (network card index 0, device index 0), create an EFA (EFA with ENA) interface. You can't use an EFA-only network interface as the primary network interface.
- For each additional network interface, use the next unused network card index, device index 1, and either an EFA (EFA with ENA) or EFA-only network interface, depending on your usecase, such as ENA bandwidth requirements or IP address space. For example use cases, see EFA configuration for a P5 and P5e instances.

Note P5 instances require network interfaces to be configured in a specific manner to enable maximum network bandwidth. For more information, see EFA configuration for a P5 and P5e instances.
The following examples show how to launch an instance based on these recommendations.
Instance launch To specify EFAs during instance launch using the launch instance wizard
1. In the Network settings section, choose Edit.
2. Expand Advanced network configuration.
3. For the primary network interface (Network interface 1), select Network card index = 0, Device index = 0, and Interface type = EFA with ENA.
4. For each additional network interface required, choose Add network interface. For Network card index select the next unused index, and then select Device index = 1, and Interface type = EFA with ENA or EFA-only.
To specify EFAs during instance launch using the run-instances command For --network-interfaces, specify the required number of network interfaces. For the primary network interface, specify NetworkCardIndex=0, DeviceIndex=0, and InterfaceType=efa. For any additional network interfaces, for NetworkCardIndex specify the next unused index, DeviceIndex=1, and InterfaceType=efa or efa-only.
The following example command snippet shows a request with 32 EFA devices and one ENA device.
$ aws ec2 run-instances \ --instance-type p5.48xlarge \ --count 1 \ --key-name key_pair_name \ --image-id ami-0abcdef1234567890 \ --network-interfaces "NetworkCardIndex=0,DeviceIndex=0,Groups=security_group_id,SubnetId=subnet_id,InterfaceType \

"NetworkCardIndex=1,DeviceIndex=1,Groups=security_group_id,SubnetId=subnet_id,InterfaceType= or efa-only" \ "NetworkCardIndex=2,DeviceIndex=1,Groups=security_group_id,SubnetId=subnet_id,InterfaceType= or efa-only" \ "NetworkCardIndex=3,DeviceIndex=1,Groups=security_group_id,SubnetId=subnet_id,InterfaceType= or efa-only" \ "NetworkCardIndex=4,DeviceIndex=1,Groups=security_group_id,SubnetId=subnet_id,InterfaceType= or efa-only" \ "NetworkCardIndex=5,DeviceIndex=1,Groups=security_group_id,SubnetId=subnet_id,InterfaceType= or efa-only" \ "NetworkCardIndex=6,DeviceIndex=1,Groups=security_group_id,SubnetId=subnet_id,InterfaceType= or efa-only" \ "NetworkCardIndex=7,DeviceIndex=1,Groups=security_group_id,SubnetId=subnet_id,InterfaceType= or efa-only" \ "NetworkCardIndex=8,DeviceIndex=1,Groups=security_group_id,SubnetId=subnet_id,InterfaceType= or efa-only" \ "NetworkCardIndex=9,DeviceIndex=1,Groups=security_group_id,SubnetId=subnet_id,InterfaceType= or efa-only" \ "NetworkCardIndex=10,DeviceIndex=1,Groups=security_group_id,SubnetId=subnet_id,InterfaceType or efa-only" \ "NetworkCardIndex=11,DeviceIndex=1,Groups=security_group_id,SubnetId=subnet_id,InterfaceType or efa-only" \ "NetworkCardIndex=12,DeviceIndex=1,Groups=security_group_id,SubnetId=subnet_id,InterfaceType or efa-only" \ "NetworkCardIndex=13,DeviceIndex=1,Groups=security_group_id,SubnetId=subnet_id,InterfaceType or efa-only" \ "NetworkCardIndex=14,DeviceIndex=1,Groups=security_group_id,SubnetId=subnet_id,InterfaceType or efa-only" \ "NetworkCardIndex=15,DeviceIndex=1,Groups=security_group_id,SubnetId=subnet_id,InterfaceType or efa-only" \ "NetworkCardIndex=16,DeviceIndex=1,Groups=security_group_id,SubnetId=subnet_id,InterfaceType or efa-only" \ "NetworkCardIndex=17,DeviceIndex=1,Groups=security_group_id,SubnetId=subnet_id,InterfaceType or efa-only" \ "NetworkCardIndex=18,DeviceIndex=1,Groups=security_group_id,SubnetId=subnet_id,InterfaceType or efa-only" \ "NetworkCardIndex=19,DeviceIndex=1,Groups=security_group_id,SubnetId=subnet_id,InterfaceType or efa-only" \ "NetworkCardIndex=20,DeviceIndex=1,Groups=security_group_id,SubnetId=subnet_id,InterfaceType or efa-only" \ "NetworkCardIndex=21,DeviceIndex=1,Groups=security_group_id,SubnetId=subnet_id,InterfaceType or efa-only" \ "NetworkCardIndex=22,DeviceIndex=1,Groups=security_group_id,SubnetId=subnet_id,InterfaceType or efa-only" \

"NetworkCardIndex=23,DeviceIndex=1,Groups=security_group_id,SubnetId=subnet_id,InterfaceType or efa-only" \ "NetworkCardIndex=24,DeviceIndex=1,Groups=security_group_id,SubnetId=subnet_id,InterfaceType or efa-only" \ "NetworkCardIndex=25,DeviceIndex=1,Groups=security_group_id,SubnetId=subnet_id,InterfaceType or efa-only" \ "NetworkCardIndex=26,DeviceIndex=1,Groups=security_group_id,SubnetId=subnet_id,InterfaceType or efa-only" \ "NetworkCardIndex=27,DeviceIndex=1,Groups=security_group_id,SubnetId=subnet_id,InterfaceType or efa-only" \ "NetworkCardIndex=28,DeviceIndex=1,Groups=security_group_id,SubnetId=subnet_id,InterfaceType or efa-only" \ "NetworkCardIndex=29,DeviceIndex=1,Groups=security_group_id,SubnetId=subnet_id,InterfaceType or efa-only" \ "NetworkCardIndex=30,DeviceIndex=1,Groups=security_group_id,SubnetId=subnet_id,InterfaceType or efa-only" \ "NetworkCardIndex=31,DeviceIndex=1,Groups=security_group_id,SubnetId=subnet_id,InterfaceType or efa-only"
...
Launch templates To add EFAs to a launch template using the Amazon EC2 console
1. In the Network settings section, expand Advanced network configuration.
2. To add the primary network interface (Network interface 1), choose Add network interface and then select Network card index = 0, Device index = 0, and Interface type = EFA with ENA.
3. To add additional network interfaces, choose Add network interface. For Network card index, select the next unused index, and then select Device index = 1, and Interface type = EFA with ENA or EFA-only.
To add EFAs to a launch template using the create-launch-template command For NetworkInterfaces, specify the required number of network interfaces. For the primary network interface, specify NetworkCardIndex=0, DeviceIndex=0, and InterfaceType=efa. For any additional network interfaces, for NetworkCardIndex specify the next unused index, DeviceIndex=1, and InterfaceType=efa or efa-only.
The following snippet shows an example with 3 network interfaces out of the possible 32 network interfaces.

"NetworkInterfaces":[ { "NetworkCardIndex":0, "DeviceIndex":0, "InterfaceType": "efa", "AssociatePublicIpAddress":false, "Groups":[ "security_group_id"
  ], "DeleteOnTermination":true }, { "NetworkCardIndex": 1, "DeviceIndex": 1, "InterfaceType": "efa or efa-only", "AssociatePublicIpAddress":false, "Groups":[ "security_group_id"
  ], "DeleteOnTermination":true }, { "NetworkCardIndex": 2, "DeviceIndex": 1, "InterfaceType": "efa or efa-only", "AssociatePublicIpAddress":false, "Groups":[ "security_group_id"
  ], "DeleteOnTermination":true }, { "NetworkCardIndex": 3, "DeviceIndex": 1, "InterfaceType": "efa or efa-only", "AssociatePublicIpAddress":false, "Groups":[ "security_group_id"
  ], "DeleteOnTermination":true } ...

### EFA configuration for a P5 and P5e instances p5.48xlarge and p5e.48xlarge instances support 32 network cards and have a total network bandwidth capacity of 3,200 Gbps, of which up to 800 Gbps can be utilized for IP network traffic.
Because EFA and IP network traffic share the same underlying resources, bandwidth used by one will reduce the bandwidth that is available to the other. This means that you can distribute the network bandwidth between EFA traffic and IP traffic in any combination, as long as the total bandwidth does not exceed 3,200 Gbps and IP bandwidth does not exceed 800 Gbps. For example, if you use 400 Gbps for IP bandwidth, you can achieve up to 2,800 Gbps of EFA bandwidth at the same time.
Use case 1: Save IP addresses and avoid potential Linux IP issues This configuration provides up to 3200 Gbps of EFA networking bandwidth and up to 100 Gbps of IP networking bandwidth with one private IP address. This configuration also helps to avoid potential Linux IP issues, such as disallowed auto-assignment of public IP addresses and IP routing challenges (hostname to IP address mapping issues and source IP address mismatches), that can arise if an instance has multiple network interfaces.
- For the primary network interface (network card index 0, device index 0), use an EFA (EFA with ENA) network interface.
- For the remaining network interfaces (network card indexes 1-31, device index 1), use EFA-only network interfaces.
Use case 2: Maximum EFA and IP network bandwidth This configuration provides up to 3200 Gbps of EFA networking bandwidth and up to 800 Gbps of IP networking bandwidth with 8 private IP address. You can't auto-assign public IP addresses with this configuration. However, you can attach an Elastic IP address to the primary network interface (network card index 0, device index 0) after launch for internet connectivity.
- For the primary network interface (network card index 0, device index 0), use an EFA (EFA with ENA) network interface.
- For the remaining interfaces, do the following:
- Specify EFA-only network interfaces on network card indexes 1, 2, and 3, and use device index
1. - Specify one EFA (EFA with ENA) network interface and three EFA-only network interfaces in each of the following network card index subsets, and use device index 1 for all of them:

- [4,5,6,7]
- [8,9,10,11]
- [12,13,14,15]
- [16,17,18,19]
- [20,21,22,23]
- [24,25,26,27]
- [28,29,30,31]
The following example illustrates this configuration:
$ aws --region $REGION ec2 run-instances \ --instance-type p5.48xlarge \ --count 1 \ --key-name key_pair_name \ --image-id ami_id \ --network-interfaces "NetworkCardIndex=0,DeviceIndex=0,Groups=security_group_id,SubnetId=subnet_id,InterfaceType=ef \ "NetworkCardIndex=1,DeviceIndex=1,Groups=security_group_id,SubnetId=subnet_id,InterfaceType=efa only" \ "NetworkCardIndex=2,DeviceIndex=1,Groups=security_group_id,SubnetId=subnet_id,InterfaceType=efa only" \ "NetworkCardIndex=3,DeviceIndex=1,Groups=security_group_id,SubnetId=subnet_id,InterfaceType=efa only" \ "NetworkCardIndex=4,DeviceIndex=1,Groups=security_group_id,SubnetId=subnet_id,InterfaceType=efa \ "NetworkCardIndex=5,DeviceIndex=1,Groups=security_group_id,SubnetId=subnet_id,InterfaceType=efa only" \ "NetworkCardIndex=6,DeviceIndex=1,Groups=security_group_id,SubnetId=subnet_id,InterfaceType=efa only" \ "NetworkCardIndex=7,DeviceIndex=1,Groups=security_group_id,SubnetId=subnet_id,InterfaceType=efa only" \ "NetworkCardIndex=8,DeviceIndex=1,Groups=security_group_id,SubnetId=subnet_id,InterfaceType=efa \ "NetworkCardIndex=9,DeviceIndex=1,Groups=security_group_id,SubnetId=subnet_id,InterfaceType=efa only" \ "NetworkCardIndex=10,DeviceIndex=1,Groups=security_group_id,SubnetId=subnet_id,InterfaceType=ef only" \ "NetworkCardIndex=11,DeviceIndex=1,Groups=security_group_id,SubnetId=subnet_id,InterfaceType=ef only" \

"NetworkCardIndex=12,DeviceIndex=1,Groups=security_group_id,SubnetId=subnet_id,InterfaceType=ef \ "NetworkCardIndex=13,DeviceIndex=1,Groups=security_group_id,SubnetId=subnet_id,InterfaceType=ef only" \ "NetworkCardIndex=14,DeviceIndex=1,Groups=security_group_id,SubnetId=subnet_id,InterfaceType=ef only" \ "NetworkCardIndex=15,DeviceIndex=1,Groups=security_group_id,SubnetId=subnet_id,InterfaceType=ef only" \ "NetworkCardIndex=16,DeviceIndex=1,Groups=security_group_id,SubnetId=subnet_id,InterfaceType=ef \ "NetworkCardIndex=17,DeviceIndex=1,Groups=security_group_id,SubnetId=subnet_id,InterfaceType=ef only" \ "NetworkCardIndex=18,DeviceIndex=1,Groups=security_group_id,SubnetId=subnet_id,InterfaceType=ef only" \ "NetworkCardIndex=19,DeviceIndex=1,Groups=security_group_id,SubnetId=subnet_id,InterfaceType=ef only" \ "NetworkCardIndex=20,DeviceIndex=1,Groups=security_group_id,SubnetId=subnet_id,InterfaceType=ef \ "NetworkCardIndex=21,DeviceIndex=1,Groups=security_group_id,SubnetId=subnet_id,InterfaceType=ef only" \ "NetworkCardIndex=22,DeviceIndex=1,Groups=security_group_id,SubnetId=subnet_id,InterfaceType=ef only" \ "NetworkCardIndex=23,DeviceIndex=1,Groups=security_group_id,SubnetId=subnet_id,InterfaceType=ef only" \ "NetworkCardIndex=24,DeviceIndex=1,Groups=security_group_id,SubnetId=subnet_id,InterfaceType=ef \ "NetworkCardIndex=25,DeviceIndex=1,Groups=security_group_id,SubnetId=subnet_id,InterfaceType=ef only" \ "NetworkCardIndex=26,DeviceIndex=1,Groups=security_group_id,SubnetId=subnet_id,InterfaceType=ef only" \ "NetworkCardIndex=27,DeviceIndex=1,Groups=security_group_id,SubnetId=subnet_id,InterfaceType=ef only" \ "NetworkCardIndex=28,DeviceIndex=1,Groups=security_group_id,SubnetId=subnet_id,InterfaceType=ef \ "NetworkCardIndex=29,DeviceIndex=1,Groups=security_group_id,SubnetId=subnet_id,InterfaceType=ef only" \ "NetworkCardIndex=30,DeviceIndex=1,Groups=security_group_id,SubnetId=subnet_id,InterfaceType=ef only" \ "NetworkCardIndex=31,DeviceIndex=1,Groups=security_group_id,SubnetId=subnet_id,InterfaceType=ef only"
...

### EFA configuration for a P6-B200 instances P6-B200 instances have a total network bandwidth capacity of 3,200 Gbps, of which up to 1600 Gbps can be utilized for ENA. They have 8 GPUs and 8 network cards, where each network card supports up to 400 Gbps EFA bandwidth and 200 Gbps ENA bandwidth. Since EFA and ENA traffic share the same underlying resources, bandwidth used by one will reduce the bandwidth that is available to the other.
Use case 1: Save IP addresses This configuration consumes at least one private IP address per instance and supports up to 3200 Gbps of EFA bandwidth and 200 Gbps of ENA bandwidth.
- For the primary network interface (network card index 0, device index 0), use an EFA (EFA with ENA) network interface.
- For the remaining 7 network cards (network card indexes 1-7, device index 1), use EFA-only network interfaces.
Use case 2: Maximum EFA and ENA bandwidth This configuration consumes at least 8 private IP address per instance and supports up to 3200 Gbps of EFA bandwidth and 1600 Gbps of ENA bandwidth.
- For the primary network interface (network card index 0, device index 0) and the remaining 7 network cards (network card indexes 1-7, device index 1), use EFA (EFA with ENA) network interfaces.
### EFA configuration for a P6e-GB200 instances P6e-GB200 instances can be configured with up to 17 network cards. The following image shows the physical network interface card (NIC) layout for P6e-GB200 instances, along with the mapping of network card indexes (NCIs).

The primary NCI (index 0) supports up to 100 Gbps of ENA bandwidth. NCIs with the following indexes support EFA-only network interfaces and 400 Gbps EFA bandwidth: [1, 3, 5, 7, 9, 11, 13, 15]. NCIs with the following indexes support up to 200 Gbps ENA or EFA bandwidth: [2, 4, 6, 8, 10, 12, 14, 16].
The NCIs in the following groups share an underlying physical NIC on the host:
- [1 and 2]
- [3 and 4]
- [5 and 6]
- [7 and 8]
- [9 and 10]
- [11 and 12]
- [13 and 14]
- [15 and 16]
Each physical NIC supports up 400 Gbps of bandwidth. Because the NCIs in these groups share the same underlying physical NIC, bandwidth used by one will reduce the bandwidth that is available

to the other. For example, if NCI 2 uses 200 Gbps of ENA bandwidth, NCI 1 can use up to 200 Gbps of EFA bandwidth at the same time.
Each underlying GPU on the host can send traffic directly over the following pairs of NCIs:
- [1 and 3]
- [5 and 7]
- [9 and 11]
- [13 and 15]
Each GPU supports up to 400 Gbps of EFA bandwidth. Because the network cards in these groups share the same GPU, bandwidth used by one will reduce the bandwidth that is available to the other. For example, if NCI 1 uses 200 Gbps of EFA bandwidth, NCI 3 can use up to 200 Gbps of EFA bandwidth at the same time. Therefore, to achieve maximum EFA performance, we recommend that you do one of the following to achieve a total of 1,600 Gbps EFA bandwidth:
- Add an EFA-only network interface to only one NCI in each group to achieve 400 Gbps per network interface (4 EFA network interfaces x 400 Gbps).
- Add an EFA-only network interface to each NCI in each group to achieve 200 Gbps per network interface (8 EFA network interfaces x 200 Gbps).
For example, the following configuration provides up to 1,600 Gbps of EFA bandwidth using a single EFA-only network interface in each NCI group, and up to 100 Gbps of ENA networking bandwidth using only the primary NCI (index 0).
- For the primary NCI (network card index 0, device index 0), use an ENA network interface.
- Add EFA-only network interfaces to the following:
- NCI 1, device index 0
- NCI 5, device index 0
- NCI 9, device index 0
- NCI 13, device index 0
### EFA configuration for a P6-B300 instances P6-B300 instances have a total network bandwidth capacity of up to 6400 Gbps for EFA traffic, and up to 3870 Gbps for ENA traffic. They have 8 GPUs and 17 network cards, where the primary

network card supports only an ENA network interface with up to 350 Gbps of bandwidth. The secondary network cards support up to 400 Gbps EFA and up to 220 Gbps of ENA bandwidth. Since EFA and ENA traffic share the same underlying resources, bandwidth used by one will reduce the bandwidth that is available to the other.
Use case 1: Save IP addresses This configuration consumes at least one private IP address per instance and supports up to 6400 Gbps of EFA bandwidth and up to 350 Gbps of ENA bandwidth.
- For the primary network interface (network card index 0, device index 0), use an ENA network interface.
- For the remaining network cards (network card indexes 1-16, device index 1), use EFA-only network interfaces.
--network-interfaces \ "NetworkCardIndex=0,DeviceIndex=0,Groups=security_group_id,SubnetId=subnet_id,InterfaceType=int \ "NetworkCardIndex=1,DeviceIndex=0,Groups=security_group_id,SubnetId=subnet_id,InterfaceType=efa only" \ "NetworkCardIndex=2,DeviceIndex=0,Groups=security_group_id,SubnetId=subnet_id,InterfaceType=efa only" \ "NetworkCardIndex=3,DeviceIndex=0,Groups=security_group_id,SubnetId=subnet_id,InterfaceType=efa only" \ "NetworkCardIndex=4,DeviceIndex=0,Groups=security_group_id,SubnetId=subnet_id,InterfaceType=efa only" \ "NetworkCardIndex=5,DeviceIndex=0,Groups=security_group_id,SubnetId=subnet_id,InterfaceType=efa only" \

"NetworkCardIndex=6,DeviceIndex=0,Groups=security_group_id,SubnetId=subnet_id,InterfaceType=efa only" \ "NetworkCardIndex=7,DeviceIndex=0,Groups=security_group_id,SubnetId=subnet_id,InterfaceType=efa only" \ "NetworkCardIndex=8,DeviceIndex=0,Groups=security_group_id,SubnetId=subnet_id,InterfaceType=efa only" \ "NetworkCardIndex=9,DeviceIndex=0,Groups=security_group_id,SubnetId=subnet_id,InterfaceType=efa only" \ "NetworkCardIndex=10,DeviceIndex=0,Groups=security_group_id,SubnetId=subnet_id,InterfaceType=ef only" \ "NetworkCardIndex=11,DeviceIndex=0,Groups=security_group_id,SubnetId=subnet_id,InterfaceType=ef only" \ "NetworkCardIndex=12,DeviceIndex=0,Groups=security_group_id,SubnetId=subnet_id,InterfaceType=ef only" \ "NetworkCardIndex=13,DeviceIndex=0,Groups=security_group_id,SubnetId=subnet_id,InterfaceType=ef only" \ "NetworkCardIndex=14,DeviceIndex=0,Groups=security_group_id,SubnetId=subnet_id,InterfaceType=ef only" \ "NetworkCardIndex=15,DeviceIndex=0,Groups=security_group_id,SubnetId=subnet_id,InterfaceType=ef only" \ "NetworkCardIndex=16,DeviceIndex=0,Groups=security_group_id,SubnetId=subnet_id,InterfaceType=ef only Use case 2: Maximum EFA and ENA bandwidth This configuration consumes at least 17 private IP address per instance and supports up to 6400 Gbps of EFA bandwidth and up to 3870 Gbps of ENA bandwidth.
- For the primary network interface (network card index 0, device index 0) use an ENA network interface.
- For the remaining network cards, create an EFA-only interface (network card indexes 1-16 device index 1) and an ENA interface network card indexes 1-16 device index 2).
--network-interfaces \ "NetworkCardIndex=0,DeviceIndex=0,Groups=security_group_id,SubnetId=subnet_id,InterfaceType=int \ "NetworkCardIndex=1,DeviceIndex=0,Groups=security_group_id,SubnetId=subnet_id,InterfaceType=efa only" \ "NetworkCardIndex=2,DeviceIndex=0,Groups=security_group_id,SubnetId=subnet_id,InterfaceType=efa only" \

"NetworkCardIndex=3,DeviceIndex=0,Groups=security_group_id,SubnetId=subnet_id,InterfaceType=efa only" \ "NetworkCardIndex=4,DeviceIndex=0,Groups=security_group_id,SubnetId=subnet_id,InterfaceType=efa only" \ "NetworkCardIndex=5,DeviceIndex=0,Groups=security_group_id,SubnetId=subnet_id,InterfaceType=efa only" \ "NetworkCardIndex=6,DeviceIndex=0,Groups=security_group_id,SubnetId=subnet_id,InterfaceType=efa only" \ "NetworkCardIndex=7,DeviceIndex=0,Groups=security_group_id,SubnetId=subnet_id,InterfaceType=efa only" \ "NetworkCardIndex=8,DeviceIndex=0,Groups=security_group_id,SubnetId=subnet_id,InterfaceType=efa only" \ "NetworkCardIndex=9,DeviceIndex=0,Groups=security_group_id,SubnetId=subnet_id,InterfaceType=efa only" \ "NetworkCardIndex=10,DeviceIndex=0,Groups=security_group_id,SubnetId=subnet_id,InterfaceType=ef only" \ "NetworkCardIndex=11,DeviceIndex=0,Groups=security_group_id,SubnetId=subnet_id,InterfaceType=ef only" \ "NetworkCardIndex=12,DeviceIndex=0,Groups=security_group_id,SubnetId=subnet_id,InterfaceType=ef only" \ "NetworkCardIndex=13,DeviceIndex=0,Groups=security_group_id,SubnetId=subnet_id,InterfaceType=ef only" \ "NetworkCardIndex=14,DeviceIndex=0,Groups=security_group_id,SubnetId=subnet_id,InterfaceType=ef only" \ "NetworkCardIndex=15,DeviceIndex=0,Groups=security_group_id,SubnetId=subnet_id,InterfaceType=ef only" \ "NetworkCardIndex=16,DeviceIndex=0,Groups=security_group_id,SubnetId=subnet_id,InterfaceType=ef only" \ "NetworkCardIndex=1,DeviceIndex=1,Groups=security_group_id,SubnetId=subnet_id,InterfaceType=ena \ "NetworkCardIndex=2,DeviceIndex=1,Groups=security_group_id,SubnetId=subnet_id,InterfaceType=ena \ "NetworkCardIndex=3,DeviceIndex=1,Groups=security_group_id,SubnetId=subnet_id,InterfaceType=ena \ "NetworkCardIndex=4,DeviceIndex=1,Groups=security_group_id,SubnetId=subnet_id,InterfaceType=ena \ "NetworkCardIndex=5,DeviceIndex=1,Groups=security_group_id,SubnetId=subnet_id,InterfaceType=ena \ "NetworkCardIndex=6,DeviceIndex=1,Groups=security_group_id,SubnetId=subnet_id,InterfaceType=ena \ "NetworkCardIndex=7,DeviceIndex=1,Groups=security_group_id,SubnetId=subnet_id,InterfaceType=ena \ "NetworkCardIndex=8,DeviceIndex=1,Groups=security_group_id,SubnetId=subnet_id,InterfaceType=ena \

"NetworkCardIndex=9,DeviceIndex=1,Groups=security_group_id,SubnetId=subnet_id,InterfaceType=ena \ "NetworkCardIndex=10,DeviceIndex=1,Groups=security_group_id,SubnetId=subnet_id,InterfaceType=en \ "NetworkCardIndex=11,DeviceIndex=1,Groups=security_group_id,SubnetId=subnet_id,InterfaceType=en \ "NetworkCardIndex=12,DeviceIndex=1,Groups=security_group_id,SubnetId=subnet_id,InterfaceType=en \ "NetworkCardIndex=13,DeviceIndex=1,Groups=security_group_id,SubnetId=subnet_id,InterfaceType=en \ "NetworkCardIndex=14,DeviceIndex=1,Groups=security_group_id,SubnetId=subnet_id,InterfaceType=en \ "NetworkCardIndex=15,DeviceIndex=1,Groups=security_group_id,SubnetId=subnet_id,InterfaceType=en \ "NetworkCardIndex=16,DeviceIndex=1,Groups=security_group_id,SubnetId=subnet_id,InterfaceType=en
## Create and attach an Elastic Fabric Adapter to an Amazon EC2 instance You can create an EFA and attach it to an Amazon EC2 instance much like any other elastic network interface in Amazon EC2. However, unlike elastic network interfaces, EFAs can't be attached to or detached from an instance in a running state.
Considerations
- You can change the security group that is associated with an EFA. To enable OS-bypass functionality, the EFA must be a member of a security group that allows all inbound and outbound traffic to and from the security group itself. For more information, see Step 1: Prepare an EFA-enabled security group.
You change the security group that is associated with an EFA in the same way that you change the security group that is associated with an elastic network interface. For more information, see the section called "Modify network interface attributes".
- You assign an Elastic IP (IPv4) and IPv6 address to an EFA (EFA with ENA) network interface in the same way that you assign an IP address to an elastic network interface. For more information, see Managing IP addresses.
You can't assign an IP address to an EFA-only network interface.
Tasks
- Create an EFA

- Attach an EFA to a stopped instance
- Attach an EFA when launching an instance
- Add an EFA to a launch template
### Create an EFA You can create an EFA in a subnet in a VPC. You can't move the EFA to another subnet after it's created, and you can only attach it to stopped instances in the same Availability Zone.
Console To create an EFA (EFA with ENA or ENA-only) network interface
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Network Interfaces and then choose Create network interface.
3. For Description, enter a descriptive name for the EFA.
4. For Subnet, select the subnet in which to create the EFA.
5. Interface type, choose one of the following options:
- EFA with ENA — To create a network interface that supports both ENA and EFA devices.
- EFA-only — To create a network interface with an EFA device only.
6. (For EFA with ENA only) Configure the IP address and prefix assignment for the network interface. The type of IP addresses and prefixes you can assign depend on the selected subnet. For IPv4-only subnets, you can assign IPv4 IP addresses and prefixes only. For IPv6- only subnets, you can assign IPv6 IP addresses and prefixes only. For dual-stack subnets, you can assign both IPv4 and IPv6 IP addresses and prefixes.
Note You can't assign IP addresses to an EFA-only network interface. a.
For Private IPv4 address and/or IPv6 address, choose Auto-assign to have Amazon EC2 automatically assign an IP address from the selected subnet, or choose Custom to manually specify the IP address to assign.

b.
If you assign an IPv6 address, you can optionally enable Assign primary IPv6 IP. Doing this assigns a primary IPv6 global unicast address (GUA) to the network interface.
Assigning a primary IPv6 address enables you to avoid disrupting traffic to instances or ENIs. For more information, see IPv6 addresses. c.
For IPv4 prefix delegation and/or IPv6 prefix delegation, choose Auto-assign to have Amazon EC2 automatically assign a prefix from the subnet's CIDR block, or choose Custom to manually specify a prefix from the subnet's CIDR block. If you specify a prefix, AWS verifies that it is not already assigned to another resource. For more information, see Prefix delegation for Amazon EC2 network interfaces d.
(Optional) Configure the Idle connection tracking timeout settings. For more information, see Idle connection tracking timeout
- TCP established timeout — The timeout period, in seconds, for idle TCP connections in an established state. Min: 60 seconds. Max: 432000 seconds (5 days). Default:
432000 seconds. Recommended: Less than 432000 seconds.
- UDP timeout — The timeout period, in seconds, for idle UDP flows that have seen traffic only in a single direction or a single request-response transaction. Min: 30 seconds. Max: 60 seconds. Default: 30 seconds.
- UDP stream timeout — The timeout period, in seconds, for idle UDP flows classified as streams that have seen more than one request-response transaction. Min: 60 seconds. Max: 180 seconds (3 minutes). Default: 180 seconds.
7. For Security groups, select one or more security groups.
8. Choose Create network interface.
AWS CLI To create an EFA Use the create-network-interface command. For --interface-type, specify efa for an EFA network interface or efa-only for an EFA-only network interface. aws ec2 create-network-interface \ --subnet-id subnet-0abcdef1234567890 \ --interface-type efa \ --description "my efa"


PowerShell To create an EFA Use the New-EC2NetworkInterface cmdlet. For -InterfaceType, specify efa for an EFA network interface or efa-only for an EFA-only network interface New-EC2NetworkInterface `
    -SubnetId subnet-0abcdef1234567890 `
    -InterfaceType efa `
    -Description "my efa"
### Attach an EFA to a stopped instance You can attach an EFA to any supported instance that is in the stopped state. You cannot attach an EFA to an instance that is in the running state. For more information about the supported instance types, see Supported instance types.
You attach an EFA to an instance in the same way that you attach a network interface to an instance. For more information, see Attach a network interface.
### Attach an EFA when launching an instance AWS CLI To attach an existing EFA when launching an instance Use the run-instances command with the --network-interfaces option. For the primary network interface, specify an EFA network interface and NetworkCardIndex=0, DeviceIndex=0. To attach multiple EFA network interfaces, see Maximize network bandwidth.
--network-interfaces "NetworkCardIndex=0, \ DeviceIndex=0, \ NetworkInterfaceId=eni-1234567890abcdef0, \ Groups=sg-1234567890abcdef0, \ SubnetId=subnet-0abcdef1234567890"
To attach a new EFA when launching an instance

Use the run-instances command with the --network-interfaces option. For the primary network interface, use NetworkCardIndex=0, DeviceIndex=0, and InterfaceType=efa. If you are attaching multiple EFA network interfaces, see Maximize network bandwidth.
--network-interfaces "NetworkCardIndex=0, \ DeviceIndex=0, \ InterfaceType=efa, \ Groups=sg-1234567890abcdef0, \ SubnetId=subnet-0abcdef1234567890"
PowerShell To attach an existing EFA when launching an instance Use the New-EC2Instance cmdlet with the -NetworkInterfaces parameter.
-NetworkInterface $networkInterface Define the network interface as follows.
$networkInterface = New-Object Amazon.EC2.Model.InstanceNetworkInterfaceSpecification $networkInterface.DeviceIndex = 0 $networkInterface.NetworkInterfaceId = "eni-1234567890abcdef0"
$networkInterface.Groups = @("sg-1234567890abcdef0")
$networkInterface.SubnetId = "subnet-0abcdef1234567890"
To attach a new EFA when launching an instance Use the New-EC2Instance cmdlet with the -NetworkInterfaces parameter.
-NetworkInterface $networkInterface Define the network interface as follows.
$networkInterface = New-Object Amazon.EC2.Model.InstanceNetworkInterfaceSpecification $networkInterface.DeviceIndex = 0 $networkInterface.InterfaceType = "efa"
$networkInterface.Groups = @("sg-1234567890abcdef0")

$networkInterface.SubnetId = "subnet-0abcdef1234567890"
### Add an EFA to a launch template You can create a launch template that contains the configuration information needed to launch EFA-enabled instances. You can specify both EFA and EFA-only network interfaces in the launch template. To create an EFA-enabled launch template, create a new launch template and specify a supported instance type, your EFA-enabled AMI, and an EFA-enabled security group. For NetworkInterfaces, specify the EFA network interfaces to attach. For the primary network interface, use NetworkCardIndex=0, DeviceIndex=0, and InterfaceType=efa. If you are attaching multiple EFA network interfaces, see Maximize network bandwidth on Amazon EC2 instances with multiple network cards.
You can leverage launch templates to launch EFA-enabled instances with other AWS services, such as AWS Batch or AWS ParallelCluster.
For more information about creating launch templates, see Create an Amazon EC2 launch template.
## Detach and delete an EFA from an Amazon EC2 instance You can detach an EFA from an Amazon EC2 instance and delete it in the same way as any other elastic network interface in Amazon EC2.
### Detach an EFA To detach an EFA from an instance, you must first stop the instance. You cannot detach an EFA from an instance that is in the running state.
You detach an EFA from an instance in the same way that you detach an elastic network interface from an instance. For more information, see Detach a network interface.
### Delete an EFA To delete an EFA, you must first detach it from the instance. You cannot delete an EFA while it is attached to an instance.
You delete EFAs in the same way that you delete elastic network interfaces. For more information, see Delete a network interface.

## Monitor an Elastic Fabric Adapter on Amazon EC2 You can use the following features to monitor the performance of your Elastic Fabric Adapters.
Topics
- EFA driver metrics for an Amazon EC2 instance
- Amazon VPC flow logs
- Amazon CloudWatch
### EFA driver metrics for an Amazon EC2 instance The Elastic Fabric Adapter (EFA) driver publishes multiple metrics from the instances that have EFA interfaces attached, in real time. You can use these metrics to troubleshoot application performance and networking issues, choose the right cluster size for a workload, plan scaling activities proactively, and benchmark applications to determine whether they maximize the EFA performance available on an instance.
Topics
- Available EFA driver metrics
- Retrieve EFA driver metrics for your instance
#### Available EFA driver metrics The EFA driver publishes the following metrics to the instance in real time. They provide the cumulative number of errors, connection events, and packets or bytes sent, received, retransmitted, or dropped by the attached EFA devices since instance launch or the last driver reset.
Metric Description Supported instance types tx_bytes The number of bytes transmitted.
Unit: bytes All instance types that support EFA rx_bytes The number of bytes received.
Unit: bytes All instance types that support EFA

Metric Description Supported instance types tx_pkts The number of packets transmitted.
Unit: count All instance types that support EFA rx_pkts The number of packets received.
Unit: count All instance types that support EFA rx_drops The number of packets that were received and then dropped.
Unit: count All instance types that support EFA send_byte s The number of bytes sent using send operations.
Unit: bytes All instance types that support EFA recv_byte s The number of bytes received by send operations.
Unit: bytes All instance types that support EFA send_wrs The number of packets sent using send operations.
Unit: count All instance types that support EFA recv_wrs The number of packets received by send operations.
Unit: count All instance types that support EFA

Metric Description Supported instance types rdma_writ e_wrs The number of completed rdma write operations.
Unit: count All instance types that support EFA rdma_read _wrs The number of completed rdma read operations.
Unit: count All instance types that support EFA rdma_writ e_bytes The number of bytes written to it by other instances using rdma write operations.
Unit: bytes All instance types that support EFA rdma_read _bytes The number of bytes received using rdma read operations.
Unit: bytes All instance types that support EFA rdma_writ e_wr_err The number of rdma write operations that had local or remote errors.
Unit: count All instance types that support EFA rdma_read _wr_err The number of rdma read operations that had local or remote errors.
Unit: count All instance types that support EFA

Metric Description Supported instance types rdma_read _resp_byt es The number of bytes sent in response to rdma read operations.
Unit: bytes All instance types that support EFA rdma_writ e_recv_by tes The number of bytes received by rdma write operations.
Unit: bytes All instance types that support EFA retrans_b ytes The number of EFA SRD bytes retransmitted.
Unit: count Nitro v4 and later instance types that support EFA retrans_p kts The number of EFA SRD packets retransmitted.
Unit: bytes Nitro v4 and later instance types that support EFA retrans_t imeout_ev ents The number of times EFA SRD traffic timed out and resulted in a network path change.
Unit: count Nitro v4 and later instance types that support EFA impaired_ remote_co nn_events The number of times EFA SRD connections entered an impaired state, resulting in a reduced throughput rate limit.
Unit: count Nitro v4 and later instance types that support EFA

Metric Description Supported instance types unrespons ive_remot e_events The number of times an EFA SRD remote connection was unresponsive.
Unit: count Nitro v4 and later instance types that support EFA For more information about the instance types that support EFA, see Supported instance types.
#### Retrieve EFA driver metrics for your instance You can use the rdma-tool command line tool to retrieve the metrics for all EFA interfaces attached to an instance as follows:
$ rdma -p statistic show link rdmap0s31/1 tx_bytes 0 tx_pkts 0 rx_bytes 0 rx_pkts 0 rx_drops 0 send_bytes 0 send_wrs 0 recv_bytes 0 recv_wrs 0 rdma_read_wrs 0 rdma_read_bytes 0 rdma_read_wr_err 0 rdma_read_resp_bytes 0 rdma_write_wrs 0 rdma_write_bytes 0 rdma_write_wr_err 0 retrans_bytes 0 retrans_pkts 0 retrans_timeout_events 0 unresponsive_remote_events 0 impaired_remote_conn_events 0 Alternatively, you can retrieve the metrics for each EFA interface attached to an instance from the sys files using the following command.

$ more /sys/class/infiniband/device_number/ports/port_number/hw_counters/* | cat For example $ more /sys/class/infiniband/rdmap0s31/ports/1/hw_counters/* | cat ::::::::::::::
/sys/class/infiniband/rdmap0s31/ports/1/hw_counters/lifespan ::::::::::::::
12 ::::::::::::::
/sys/class/infiniband/rdmap0s31/ports/1/hw_counters/rdma_read_bytes ::::::::::::::
0 ::::::::::::::
/sys/class/infiniband/rdmap0s31/ports/1/hw_counters/rdma_read_resp_bytes ::::::::::::::
0 ::::::::::::::
/sys/class/infiniband/rdmap0s31/ports/1/hw_counters/rdma_read_wr_err ::::::::::::::
0 ::::::::::::::
/sys/class/infiniband/rdmap0s31/ports/1/hw_counters/rdma_read_wrs ::::::::::::::
0 ::::::::::::::
/sys/class/infiniband/rdmap0s31/ports/1/hw_counters/rdma_write_bytes ::::::::::::::
0 ::::::::::::::
/sys/class/infiniband/rdmap0s31/ports/1/hw_counters/rdma_write_recv_bytes ::::::::::::::
0 ::::::::::::::
/sys/class/infiniband/rdmap0s31/ports/1/hw_counters/rdma_write_wr_err ::::::::::::::
0 ::::::::::::::
/sys/class/infiniband/rdmap0s31/ports/1/hw_counters/rdma_write_wrs ::::::::::::::
0 ::::::::::::::
/sys/class/infiniband/rdmap0s31/ports/1/hw_counters/recv_bytes

::::::::::::::
0 ::::::::::::::
/sys/class/infiniband/rdmap0s31/ports/1/hw_counters/recv_wrs ::::::::::::::
0 ::::::::::::::
/sys/class/infiniband/rdmap0s31/ports/1/hw_counters/rx_bytes ::::::::::::::
0 ::::::::::::::
/sys/class/infiniband/rdmap0s31/ports/1/hw_counters/rx_drops ::::::::::::::
0 ::::::::::::::
/sys/class/infiniband/rdmap0s31/ports/1/hw_counters/rx_pkts ::::::::::::::
0 ::::::::::::::
/sys/class/infiniband/rdmap0s31/ports/1/hw_counters/send_bytes ::::::::::::::
0 ::::::::::::::
/sys/class/infiniband/rdmap0s31/ports/1/hw_counters/send_wrs ::::::::::::::
0 ::::::::::::::
/sys/class/infiniband/rdmap0s31/ports/1/hw_counters/tx_bytes ::::::::::::::
0 ::::::::::::::
/sys/class/infiniband/rdmap0s31/ports/1/hw_counters/tx_pkts ::::::::::::::
0 ::::::::::::::
/sys/class/infiniband/rdmap0s31/ports/1/hw_counters/retrans_bytes ::::::::::::::
0 /sys/class/infiniband/rdmap0s31/ports/1/hw_counters/retrans_pkts ::::::::::::::
0 /sys/class/infiniband/rdmap0s31/ports/1/hw_counters/retrans_timeout_events ::::::::::::::
0

/sys/class/infiniband/rdmap0s31/ports/1/hw_counters/unresponsive_remote_events ::::::::::::::
0 /sys/class/infiniband/rdmap0s31/ports/1/hw_counters/impaired_remote_conn_events ::::::::::::::
0
### Amazon VPC flow logs You can create an Amazon VPC Flow Log to capture information about the traffic going to and from an EFA. Flow log data can be published to Amazon CloudWatch Logs and Amazon S3. After you create a flow log, you can retrieve and view its data in the chosen destination. For more information, see VPC Flow Logs in the Amazon VPC User Guide.
You create a flow log for an EFA in the same way that you create a flow log for an elastic network interface. For more information, see Create a flow log in the Amazon VPC User Guide.
In the flow log entries, EFA traffic is identified by the srcAddress and destAddress, which are both formatted as MAC addresses, as shown in the following example. version accountId  eniId         srcAddress        destAddress       sourcePort destPort protocol packets bytes start      end        action log-status 2       3794735123 eni-10000001 01:23:45:67:89:ab 05:23:45:67:89:ab -          -
 -        9       5689  1521232534 1524512343 ACCEPT OK
### Amazon CloudWatch If you are using EFA in an Amazon EKS cluster, you can monitor your EFAs using CloudWatch Container Insights. Amazon CloudWatch Container Insights supports all of the EFA driver metrics, except: retrans_bytes, retrans_pkts, retrans_timeout_events, unresponsive_remote_events, and impaired_remote_conn_events.
For more information, see  Amazon EKS and Kubernetes Container Insights metrics in the Amazon CloudWatch User Guide.
## Verify the EFA installer using a checksum You can optionally verify the EFA tarball (.tar.gz file) using an MD5 or SHA256 checksum. We recommend that you do this to verify the identity of the software publisher and to check that the application has not been altered or corrupted since it was published.

To verify the tarball Use the md5sum utility for the MD5 checksum, or the sha256sum utility for the SHA256 checksum, and specify the tarball filename. You must run the command from the directory in which you saved the tarball file.
- MD5 $  md5sum tarball_filename.tar.gz
- SHA256 $  sha256sum tarball_filename.tar.gz The commands should return a checksum value in the following format. checksum_value tarball_filename.tar.gz Compare the checksum value returned by the command with the checksum value provided in the table below. If the checksums match, then it is safe to run the installation script. If the checksums do not match, do not run the installation script, and contact Support.
For example, the following command verifies the EFA 1.9.4 tarball using the SHA256 checksum.
$  sha256sum aws-efa-installer-1.9.4.tar.gz Example output:
1009b5182693490d908ef0ed2c1dd4f813cc310a5d2062ce9619c4c12b5a7f14 aws-efa- installer-1.9.4.tar.gz The following table lists the checksums for recent versions of EFA.
Version Checksums EFA 1.47.0 MD5: c81d4caf24dabc04a6e48185906 20f5f

Version Checksums SHA256: 2df4201e046833c7dc 8160907bee7f52b76ff80ed1473 76a2d0ed8a0dd66b2db EFA 1.46.0 MD5:a88bbd9b71624d7ca401b54bc2fc0c19 SHA256: 8302bd7849afb95c90 3a875d7dcb6f85b3d7629e9a8b6 7d020031cfc6f4d0ee1 EFA 1.45.1 MD5:91c3c87e16bbcaca1513252c38b771bb SHA256: 9aeb20c645135b6039 cc08986d8f14e63280f7839e882 a74df5e83627ffeaa17 EFA 1.45.0 MD5:800aeddfa9d9c5f139a7b8f7c4fec627 SHA256: 25ba26a0877fe33173 90dc126aad2f23e27fc461cf0b9 40004f032cb342fa539 EFA 1.44.0 MD5:d024f6bebe080db42745103b84ca7c43 SHA256: f129a5b44a49d593d2 47e55a59eb9bcb57121566e1c2e 42b832a4e794fa83d8a EFA 1.43.3 MD5: 4dbc6eeecc516760253c10cbedb 6319d SHA256: 6c470ebce254c71653 47b5048895ac2996c8856727164 2297f4c597738300652

Version Checksums EFA 1.43.2 MD5: 7287b25a07c9747c0d4001e8fc5 f59b2 SHA256: de15c5bdbc83b952af bde876110830c604ad0796680e5 157c05f7c1979a41069 EFA 1.43.1 MD5: 7cfafc8debaea51dd4966fa0b2b ba673 SHA256:54211eda0c193138ee8ed09b5fb 41c41fc76fe0a77935fa4ec8d989466342740 EFA 1.43.0 MD5: f2b3dd7dc8670b541f7c23fd58e 5e503 SHA256: 786df3458c499237be 33bb8e50ffd4da7c18c20e25438 0ffc80fb90833d8cc73 EFA 1.42.0 MD5: 94b2b1db09da1dde08ec049db1f 24370 SHA256: 4114fe612905ee0508 3ae5cb391a00a012510f3abfecc 642d86c9a5ae4be9008 EFA 1.41.0 MD5: 086181c3ee3f8da512fc6e1c795 e8936 SHA256: 3506354cdfbe31ff55 2fe75f5d0d9bb7efd29cf79bd99 457347d29c751c38f9f

Version Checksums EFA 1.40.0 MD5: f3ec6f73fbeaccba08232750758 1157c SHA256: 30491b0fe7c3470d44 39594538855c981b05fa69862d7 4f8c05eb9b97912368a EFA 1.39.0 MD5: c223d5954a85a7fbcd248c942b8 66e43 SHA256: 2cbc028c03064633bb 990782b47c36156637769e2f487 04417a9c700a7a32101 EFA 1.38.1 MD5: f112569e828ab65187777f794ba b542c SHA256: 83923374afd388b1cf cf4b3a21a2b1ba7cf46a01a587f 7b519b8386cb95e4f81 EFA 1.38.0 MD5: 43a2a446b33a2506f40853d5505 9f1ea SHA256: 4f436954f35ad53754 b4d005fd8d0be63de3b4184de41 a695b504bdce0fecb22 EFA 1.37.0 MD5: 6328070192bae920eca45797ad4 c1db1 SHA256: 2584fc3c8bb99f29b3 285e275747ff09d67c18e162c2a 652e36c976b72154bfb

Version Checksums EFA 1.36.0 MD5: 1bec83180fbffb23452ab6469ca 21dfa SHA256: de183f333cfb58aeb7 908a67bf9106985ba3ccb7f8638 b851d2a0d8dbfacaec4 EFA 1.35.0 MD5: 252f03c978dca5f8e8d9f34e488 b256e SHA256: 432b6ad4368ba0cd8b 902729d14a908a97be7a3dcc523 9422ea994a47f35a5e1 EFA 1.34.0 MD5: 5cd4b28d27a31677c16139b54c9 acb45 SHA256: bd68839e741b0afd3e c2e37d50603803cfa7a279c120f 0a736cc57c2ff2d7fdc EFA 1.33.0 MD5: e2f61fccbcaa11e2ccfddd36605 22276 SHA256: 0372877b87c6a7337b b7791d255e1053b907d030489fb 2c3732ba70069185fce EFA 1.32.0 MD5: db8d65cc028d8d08b5a9f2d8888 1c1b1 SHA256: 5f7233760be57f6fee 6de8c09acbfbf59238de848e060 48dc54d156ef578fc66

Version Checksums EFA 1.31.0 MD5: 856352f12bef2ccbadcd75e35aa 52aaf SHA256: 943325bd37902a4300 ac9e5715163537d56ecb4e7b87b 37827c3e547aa1897bf EFA 1.30.0 MD5: 31f48e1a47fe93ede8ebd273fb7 47358 SHA256: 876ab9403e07a0c3c9 1a1a34685a52eced890ae052df9 4857f6081c5f6c78a0a EFA 1.29.1 MD5: e1872ca815d752c1d7c2b5c175e 52a16 SHA256: 178b263b8c25845b63 dc93b25bcdff5870df5204ec509 af26f43e8d283488744 EFA 1.29.0 MD5: 39d06a002154d94cd982ed34813 3f385 SHA256: 836655f87015547e73 3e7d9f7c760e4e24697f8bbc261 bb5f3560abd4206bc36 EFA 1.28.0 MD5: 9dc13b7446665822605e66febe0 74035 SHA256: 2e625d2d6d3e073b51 78e8e861891273d896b66d03cb1 a32244fd56789f1c435

Version Checksums EFA 1.27.0 MD5: 98bfb515ea3e8d93f554020f383 7fa15 SHA256: 1d49a97b0bf8d964d9 1652a79ac851f2550e33a5bf9d0 cf86ec9357ff6579aa3 EFA 1.26.1 MD5: 884e74671fdef4725501f7cd2d4 51d0c SHA256: c616994c924f54ebfa bfab32b7fe8ac56947fae00a0ff 453d975e298d174fc96 EFA 1.26.0 MD5: f8839f12ff2e3b9ba09ae8a82b3 0e663 SHA256: bc1abc1f76e97d204d 3755d2a9ca307fc423e51c63141 f798c2f15be3715aa11 EFA 1.25.1 MD5: 6d876b894547847a45bb8854d44 31f18 SHA256: d2abc553d22b89a4ce 92882052c1fa6de450d3a801fe0 05da718b7d4b9602b06 EFA 1.25.0 MD5: 1993836ca749596051da04694ea 0d00c SHA256: 98b7b26ce031a2d6a9 3de2297cc71b03af64719486636 9ca53b60d82d45ad342

Version Checksums EFA 1.24.1 MD5: 211b249f39d53086f3cb0c07665 f4e6f SHA256: 120cfeec233af09556 23ac7133b674143329f9561a9a8 193e473060f596aec62 EFA 1.24.0 MD5: 7afe0187951e2dd2c9cc4b572e6 2f924 SHA256: 878623f819a0d9099d 76ecd41cf4f569d4c3aac0c9bb7 ba9536347c50b6bf88e EFA 1.23.1 MD5: 22491e114b6ee7160a8290145dc a0c28 SHA256: 5ca848d8e0ff4d1571 cd443c36f8d27c8cdf2a0c97e90 68ebf000c303fc40797 EFA 1.23.0 MD5: 38a6d7c1861f5038dba4e441ca7 683ca SHA256: 555d497a60f22e3857 fdeb3dfc53aa86d05926023c68c 916d15d2dc3df6525bd EFA 1.22.1 MD5: 600c0ad7cdbc06e8e846cb763f9 2901b SHA256: f90f3d5f59c031b9a9 64466b5401e86fd0429272408f6 c207c3f9048254e9665

Version Checksums EFA 1.22.0 MD5: 8f100c93dc8ab519c2aeb5dab89 e98f8 SHA256: f329e7d54a86a03ea5 1da6ea9a5b68fb354fbae4a57a0 2f9592e21fce431dc3a EFA 1.21.0 MD5: 959ccc3a4347461909ec02ed3ba 7c372 SHA256: c64e6ca34ccfc3ebe8 e82d08899ae8442b3ef552541cf 5429c43d11a04333050 EFA 1.20.0 MD5: 7ebfbb8e85f1b94709df4ab3db4 7913b SHA256: aeefd2681ffd5c4c63 1d1502867db5b831621d6eb85b6 1fe3ec80df983d1dcf0 EFA 1.19.0 MD5: 2fd45324953347ec5518da7e3fe fa0ec SHA256: 99b77821b9e72c8dea 015cc92c96193e8db307deee05b 91a58094cc331f16709 EFA 1.18.0 MD5: fc2571a72f5d3c7b7b576ce2de3 8d91e SHA256: acb18a0808aedb9a5e 485f1469225b9ac97f21db9af78 e4cd6939700debe1cb6

Version Checksums EFA 1.17.3 MD5: 0517df4a190356ab55923514717 4cafd SHA256: 5130998b0d2883bbae 189b21ab215ecbc1b01ae023165 9a9b4a17b0a33ebc6ca EFA 1.17.2 MD5: a329dedab53c4832df218a24449 f4c9a SHA256: bca1fdde8b32b00346 e175e597ffab32a09a08ee9ab13 6875fb38283cc4cd099 EFA 1.17.1 MD5: 733ae2cfc9d14b52017eaf0a2ab 6b0ff SHA256: f29322640a88ae9279 805993cb836276ea24062382084 8463ca686c8ce02136f EFA 1.17.0 MD5: d430fc841563c11c3805c5f82a4 746b1 SHA256: 75ab0cee4fb6bd3888 9dce313183f5d3a83bd233e0a6e f6205d8352821ea901d EFA 1.16.0 MD5: 399548d3b0d2e812d74dd67937b 696b4 SHA256: cecec36495a1bc6fdc 82f97761a541e4fb6c9a3cbf3cf cb145acf25ea5dbd45b

Version Checksums EFA 1.15.2 MD5: 955fea580d5170b05823d51acde 7ca21 SHA256: 84df4fbc1b3741b6c0 73176287789a601a589313accc8 e6653434e8d4c20bd49 EFA 1.15.1 MD5: c4610267039f72bbe4e35d7bf53 519bc SHA256: be871781a1b9a15fca 342a9d169219260069942a8bda7 a8ad06d4baeb5e2efd7 EFA 1.15.0 MD5: 9861694e1cc00d884fadac07d22 898be SHA256: b329862dd5729d2d09 8d0507fb486bf859d7c70ce18b6 1c302982234a3a5c88f EFA 1.14.1 MD5: 50ba56397d359e57872fde1f74d 4168a SHA256: c7b1b48e86fe4b3eaa 4299d3600930919c4fe6d88cc6e 2c7e4a408a3f16452c7 EFA 1.14.0 MD5: 40805e7fd842c36ececb9fd7f92 1b1ae SHA256: 662d62c12de85116df 33780d40e0533ef7dad92709f4f 613907475a7a1b60a97

Version Checksums EFA 1.13.0 MD5: c91d16556f4fd53becadbb34582 8221e SHA256: ad6705eb23a3fce44a f3afc0f7643091595653a723ad0 374084f4f2b715192e1 EFA 1.12.3 MD5: 818aee81f097918cfaebd724edd ea678 SHA256: 2c225321824788b8ca 3fbc118207b944cdb096b847e1e 0d1d853ef2f0d727172 EFA 1.12.2 MD5: 956bb1fc5ae0d6f0f87d2e481d4 9fccf SHA256: 083a868a2c212a5a4f cf3e4d732b685ce39cceb3ca7e5 d50d0b74e7788d06259 EFA 1.12.1 MD5: f5bfe52779df435188b0a2874d0 633ea SHA256: 5665795c2b4f09d5f3 f767506d4d4c429695b36d4a17e 5758b27f033aee58900 EFA 1.12.0 MD5: d6c6b49fafb39b770297e1cc44f e68a6 SHA256: 28256c57e9ecc0b077 8b41c1f777a9982b4e8eae78234 3dfe1246079933dca59

Version Checksums EFA 1.11.2 MD5: 2376cf18d1353a4551e35c33d26 9c404 SHA256: a25786f98a3628f7f5 4f7f74ee2b39bc6734ea9374720 507d37d3e8bf8ee1371 EFA 1.11.1 MD5: 026b0d9a0a48780cc7406bd5199 7b1c0 SHA256: 6cb04baf5ffc58ddf3 19e956b5461289199c8dd805fe2 16f8f9ab8d102f6d02a EFA 1.11.0 MD5: 7d9058e010ad65bf2e14259214a 36949 SHA256: 7891f6d45ae33e8221 89511c4ea1d14c9d54d000f6696 f97be54e915ce2c9dfa EFA 1.10.1 MD5: 78521d3d668be22976f46c6fecc 7b730 SHA256: 61564582de7320b21d e319f532c3a677d26cc46785378 eb3b95c636506b9bcb4 EFA 1.10.0 MD5: 46f73f5a7afe41b4bb918c81888 fefa9 SHA256: 136612f96f2a085a7d 98296da0afb6fa807b38142e2fc 0c548fa986c41186282

Version Checksums EFA 1.9.5 MD5: 95edb8a209c18ba8d250409846e b6ef4 SHA256: a4343308d7ea4dc943 ccc21bcebed913e8868e59bfb2a c93599c61a7c87d7d25 EFA 1.9.4 MD5: f26dd5c350422c1a985e35947fa 5aa28 SHA256: 1009b5182693490d90 8ef0ed2c1dd4f813cc310a5d206 2ce9619c4c12b5a7f14 EFA 1.9.3 MD5: 95755765a097802d3e6d5018d1a 5d3d6 SHA256: 46ce732d6f3fcc9edf 6a6e9f9df0ad136054328e24675 567f7029edab90c68f1 EFA 1.8.4 MD5: 85d594c41e831afc6c930526314 0457e SHA256: 0d974655a09b213d78 59e658965e56dc4f23a0eee2dc4 4bb41b6d039cc5bab45
## Elastic Fabric Adapter release notes The following table describes the version history and changelog for the Elastic Fabric Adapter software.

Version Changes Release date 1.47.0
- Upgrade to   libfabric 2.4.0amzn1.0
- Refactor peer management: move  endpoint→ peer hashmap to AV level
- Add packet entry generation counter to prevent ABA problem
- Implement blocking CQ read support (fi_cq_sread) with wait objects
- Fix double-free in eager/mulreq/longread RTM packet processing
- Fix MR registration IBV access flags based on device RDMA capabilities
- Disable FI_OPT_EFA_SENDRECV_IN_ORDER_ALIGNED _128_BYTES (returns -FI_EOPNOTSUPP)
- Optimize packet entry to fit in two x86 cache lines (128 bytes)
- Always succeed efa_rdm_srx_start and slide recv window on RTM/RTA errors
- Unlink RX packet entries before releasing during endpoint cleanup
- Upgrade to   libnccl-ofi 1.18.0
- P6-B300 support: added custom tuner decisions for P6- B300
- Improved performance of PAT on P6-B200 by reducing channel count for smaller message sizes January 29, 2026

Version Changes Release date
- Changed protocol defaults, default to RDMA protocol on Trn1 and default to SENDRECV protocol on g7e.8xlarge
- Dynamic platform selection: added feature to enable AWS optimizations at runtime based on presence of AWS NICs.
This allows a single plugin binary to be used for both AWS and non-AWS platforms. AWS optimizations can still be disabled at compile-time.
- Fixed support for non-FI_MR_VIRT_ADDR providers in RDMA protocol
- Improved NIC PCIe link speed and width reporting to NCCL
- Redesigned threading model to support multi-threaded applications without requiring a separate Libfabric domain for each thread.
- Fixed support for FI_MR_ENDPOINT providers (supports SENDRECV protocol only) by cleaning up resources in correct order
- Upgrade to  rdma-core 61.0
- Use single threaded CQ if Thread Domain was provided
- Verify QP number on CQE processes
- Upgrade to  efa driver 3.0.0
- Improve admin error handling
- Check for QP number correctness on completion poll
- Remove unconditional backport of best page size finding
- Print errno strings for error pointers

Version Changes Release date
- Simplify the code in CQ creation flows
- Backport upstream changes in CQ with umem creation flow
- Adjust DKMS configuration for new DKMS versions
- Upgrade to  Open MPI 5.0.9amzn1
- Bugfix: Set domain threading level based on MPI thread support
- Bugfix: Request FI_COMPLETION flag to ensure completio ns are generated for all data transfer events
- Share domains between BTL and MTL to reduce the total number of domains created to fix resource exhaustion on systems with high core counts 1.46.0
- Add Support for Debian 13
- Upgrade to   efa-nv-peermem 1.2.3
- Fix build errors and warnings with new kernels and DKMS
- Upgrade to   libfabric 2.3.1amzn4.0
- Enable data path direct for efa-rdm protocol path
- Enable ROCr HMEM support
- New FI_OPT_EFA_USE_UNSOLICITED_WRITE_RECV option to disable unsolicited write recv
- Optimize connection establishment time
- Add libnccl-ofi on RHEL 9, Rocky Linux 9, and Debian 13 December 12, 2025

Version Changes Release date 1.45.1
- Upgrade to   libfabric 2.3.1amzn3.0
- Fix bug that truncated cq_data to 2 bytes while provider advertised support for 4 bytes November 26, 2025

Version Changes Release date 1.45.0
- Upgrade to   rdma-core 60.amzn0
- Extend DV query CQ to return doorbell
- Upgrade to   libfabric 2.3.1amzn2.0
- Support FI_RX_CQ_DATA mode for efa-direct
- Optimize WQE post in data path direct path
- Fix the race condition in cntr progress
- Improve the logging for warning messages
- Handles RMA completion correctly for removed peers
- Evict AH entries from implicit AV when AH limit is reached
- Upgrade to libnccl-ofi 1.17.2
- Fixed a crash with NCCL v2.28.x when Libfabric initializ ation failed
- Added support for g7e instance family
- Fixed an issue where NCCL could erroneously attempt to use a GPUDirect RDMA path on platforms that support DMA-BUF
- Fixed shutdown ordering issue on NICs that require per- endpoint memory registration (Cray Slingshot)
November 17, 2025

Version Changes Release date 1.44.0
- Upgrade to   rdma-core 59.amzn0
- Add support to bind QPs and CQs to thread domains
- Add support to allocate a parent domain
- Add support to allocate thread domains
- Add direct verbs query QP and CQ
- Add option to create CQ with external memory`
- Fix CQ poll after QP destroy
- Upgrade to   libfabric 2.3.1amzn1.0
- Upgrade to   Open MPI 5.0.8amzn1
- Functionality enhancements
- Bug fixes
- Upgrade to libnccl-ofi 1.17.1
- Supports NCCL v2.28.3-1 while maintaining backward compatibility with NCCL v2.17.1 and later.
- Building with platform-aws requires Libfabric v1.22.0am zn4.0 or greater. Tested with versions up  to Libfabric v2.3.1amzn1.0.
- Fixes to support compatibility across CUDA12 and CUDA13.
October 29, 2025

Version Changes Release date 1.43.3
- Upgrade to   efa driver 2.17.3
- Support P2P with NVIDIA 580 drivers
- Adjust MR registration for 6.17 and on kernels October 01, 2025 1.43.2
- Upgrade to   libnccl-ofi 1.16.3
- Supports NCCL v2.27.7-1 while maintaining backward compatibility with  NCCL v2.17.1 and later.
- Building with platform-aws requires Libfabric v1.22.0am zn4.0 or greater.  Tested with versions up to Libfabric 2.1.0amzn5.0.
- Enable domain-per-thread by default on all Amazon EC2 instance types for improved performance for some applications where NCCL creates multiple proxy threads August 15, 2025 1.43.1
- Upgrade to   libnccl-ofi 1.16.2
- Supports NCCL v2.27.6-1 while maintaining backward compatibility with  NCCL v2.17.1 and later.
- Building with platform-aws requires Libfabric v1.22.0am zn4.0 or greater.  Tested with versions up to Libfabric 2.1.0amzn4.0.
- Added a new platform configuration to support using the OFI NCCL plugin on the Amazon EC2 p5.4xlarge instance type
- Upgrade to libfabric  2.1.0amzn5.0 July 31, 2025

Version Changes Release date 1.43.0
- Upgrade to   libnccl-ofi 1.16.1
- Supports NCCL v2.27.6-1 while maintaining backward compatibility with NCCL v2.17.1 and later.
- Building with platform-aws requires Libfabric v1.22.0am zn4.0 or greater.  Tested with versions up to Libfabric 2.1.0amzn3.
- Update the PCI link speed format reported in the topology file to match kernel 5.7+
- Added SKIP_NICS_WITHOUT_ACCEL_AT_SAME_PCI_LEVEL to skip libfabric nics that do not have an accelerator at the same pci level
- Upgrade to   efa driver 2.17.2
- Upgrade to   efa-nv-peermem 1.2.2
- Upgrade to libfabric  2.1.0amzn4.0
- Upgrade to rdma-core 58.amzn0
- Fix work request index double use
- Add WQE length to post_send tracepoint
- Enable optimizations for Graviton platforms
- Deprecate support for Ubuntu 20.04 July 25, 2025

Version Changes Release date 1.42.0
- Upgrade to efa driver 2.15.3
- Upgrade to efa-nv-peermem 1.2.1
- Upgrade to rdma-core 57.amzn1
- Fix work request index double use
- Upgrade to libfabric 2.1.0amzn3.0
- Upgrade to libnccl-ofi 1.15.0
- Supports NCCL 2.26.6-1 while maintaining backward compatibility with (NCCL v2.17.1 and later.
- Building with platform-aws requires Libfabric v1.22.0am zn4.0 or greater. Tested with versions up to Libfabric 2.1.0amzn3.
- Build system and platform support
- Added Amazon EC2 P6-B200 platform support
- Changed default plugin library name to libnccl-net- ofi.so, and by default create symlink from libnccl-net- ofi.so to libnccl-net.so to maintain backward compatibi lity. This allows users to set NCCL_NET_PLUGIN=of i to force NCCL to use the OFI plugin for communica tion. Specifying --disable-nccl-net-symlink to configure will skip the symlink, allowing multiple plugins to be installed in the same container.
- Tuning and performance improvements
- Added tuner support on P6-B200 for AllReduce, AllGather, and ReduceScatter regions for 0x0 and 0x7 bitmask
- Updated default latency for P5en and P6-B200 platforms based on empirical results and analysis June 6, 2025

Version Changes Release date
- Update to use NCCL v10 API with trafficClass parameter support for future traffic prioritization
- Migrated plugin code base from C to C++
- Added support for jobs where the number of NICs per GPU is different across systems. See the OFI_NCCL_ FORCE_NUM_RAILS runtime environment variable documentation for more information.
1.41.0
- Upgrade to rdma-core 57.amzn0 May 16, 2025 1.40.0
- Upgrade to libfabric 2.1.0amzn2.0
- Upgrade to rdma-core 56.0
- Upgrade to efa-config 1.18.
- Deprecate support for Debian 10
- Upgrade to libnccl-ofi 1.14.2
- Enable CUDA support in Libfabric on ARM for Ubuntu and Amazon Linux 2023
- Add libnccl-ofi on ARM for Ubuntu and Amazon Linux 2023 May 2, 2025 1.39.0
- Upgrade to libfabric 2.1.0
- Upgrade to Open MPI 5.0.6
- Upgrade to libnccl-ofi 1.14.1
- Upgrade to efa driver 2.15.0 April 16, 2025 1.38.1
- Update to Libfabric 1.22.0amzn5.0 March 3, 2025 1.38.0
- Add libnccl-ofi 1.13.2-1 January 8, 2025 1.37.0
- Upgrade to libfabric 1.22.0amzn4.0
- Upgrade to rdma-core 54.amzn0 November 18, 2024

Version Changes Release date 1.36.0
- Add support for Debian 12
- Distribute efa_test.sh  as a utility script at /opt/amaz on/efa/bin
- Upgrade to efa driver 2.13.0
- Upgrade to libfabric 1.22.0amzn3.0
- Upgrade to rdma-core 54.0
- Upgrade to open mpi 4.1.7 November 7, 2024 1.35.0
- Upgrade to Open MPI 5.0.5
- Upgrade to PRRTE 3.0.6 and rename the RPM package to prrte-aws
- Rename the OpenPMIx RPM package to pmix-aws
- Configure build options for dpkg and RPM builds
- Upgrade to Libfabric 1.22.0amzn2.0
- Upgrade to efa driver 2.12.1 October 14, 2024 1.34.0
- Drop support for CentOS 7 and RHEL 7
- Ingest Libfabric 1.22.0amzn1.0
- Update efa-config package to 1.17 August 6, 2024 1.33.0
- Upgrade to efa driver 2.10.0
- Upgrade to rdma-core 52.0
- Upgrade to PRRTE 3.0.5
- Upgrade to Open MPI 5.0.3
- Add support for Ubuntu 24.04 LTS
- Remove OpenPMIx, PRRTE and Open MPI HTML documenta tion. Users should refer to the official website.
- Drop support for openSUSE 15.4 or older June 20, 2024

Version Changes Release date 1.32.0
- Upgrade to efa driver 2.8.0
- Upgrade to efa-nv-peermem driver 1.1.1
- Upgrade efa-config package to 1.16
- Upgrade efa-profile package to 1.7
- Upgrade to rdma-core 50.0
- Upgrade to libfabric 1.21.0amzn1.0
- Enhance efa_test.sh  with fi_pingpong  port selection
- Install newer rdma-core from system when required April 18, 2024 1.31.0
- Upgrade to OpenPMIx 4.2.8
- Upgrade to PRRTE 3.0.3
- Upgrade to Open MPI 5.0.2, and convert MCA components to DSO.
- Upgrade to Libfabric 1.20.1amzn1.0 March 7, 2024 1.30.0
- Include OpenPMIx 4.2.7, installed at /opt/amazon/pmix by default
- Include PRRTE 3.0.2, installed at /opt/amazon/prrte  by default
- Include Open MPI 5.0.0, installed at /opt/amazon/ openmpi5  by default
- Update efa-profile to 1.6 December 2023 1.29.1
- Ingest libfabric 1.19.0amzn4.0 December 2023 1.29.0
- Ingest efa kernel driver 2.6.0
- Ingest libfabric 1.19.0amzn3.0 November 2023 1.28.0
- Upgrade Open MPI to 4.1.6
- Ingest libfabric 1.19.0amzn2.0 October 2023

Version Changes Release date 1.27.0
- Add Libfabric 1.19.0amzn1.0  to installer
- Enable GCC builtin atomics for Open MPI 4 September 2023 1.26.1
- efa_test.sh : fix infinite retry bug September 2023 1.26.0
- Add support for RHEL 9
- Fix debug build on multiple distributions
- Ingest libfabric 1.18.2amzn1.0
- efa_test.sh : Add retry for fi_pingpong September 2023 1.25.1
- Ingest libfabric 1.18.1amzn1.0
- Update timeouts in EFA installer scripts September 2023 1.25.0
- Add support for Amazon Linux 2023
- Bugfix in post-installation test July 2023 1.24.1
- Upgrade libfabric to 1.18.1
- Upgrade efa driver to 2.5.0 July 2023 1.24.0
- Ingest rdma-core 46.0
- Ingest efa driver 2.4.1
- Support Debian 11 June 2023 1.23.1
- Ingest libfabric 1.18.0amzn2.0 June 2023 1.23.0
- Add support for Debian 10
- Drop support for Ubuntu 18.04 LTS
- Upgrade efa-config package to 1.14
- Ingest libfabric 1.18.0amzn1.0 May 2023 1.22.1
- Upgrade libfabric to 1.17.1 March 2023

Version Changes Release date 1.22.0
- Upgrade Open MPI to 4.1.5
- Upgrade libfabric to 1.17.0
- Upgrade efa-config package to 1.13 February 2023 1.21.0
- Add support for Rocky Linux 9 OS
- Ingest efa driver 2.1.1
- Ingest libfabric 1.16.1amzn3.0
- Upgrade efa-config package to 1.12 December 2022 1.20.0
- Add support for Rocky Linux 8 OS.
- Ingest efa driver 2.1.0.
- Ingest rdma-core 43.0.
- Ingest libfabric 1.16.1amzn1.0 November 2022 1.19.0
- Ingest libfabric 1.16.0
- Build Open MPI with --enable-orterun-prefix-by- default October 2022 1.18.0
- Add support for Ubuntu22.04 August 2022 1.17.3
- Update libfabric to 1.16.0~amzn4.0 . The ~ indicates it is a pre-release version of libfabric 1.16.0.
- Extend post-installation pingpong test timeout to 20 seconds August 2022 1.17.2
- Update libfabric to 1.16.0~amzn3.0 . The ~ indicates it is a pre-release version of libfabric 1.16.0.
July 2022 1.17.1
- Update libfabric to 1.16.0~amzn2.0 . The ~ indicates it is a pre-release version of libfabric 1.16.0.
- Disable the experimental net provider when building libfabric July 2022

Version Changes Release date 1.17.0
- Update rdma-core  to v41.0
- Update Open MPI to 4.1.4
- Update libfabric to 1.16.0~amzn1.0 . The ~ indicates it is a pre-release version of libfabric 1.16.0.
July 2022 1.16.0
- Update libfabric to 1.15.1amzn1.0 , contains neuron library name change
- Upgrade efa-config to 1.10
- Exclude opx and rxd providers in the libfabric build June 2022 1.15.2
- Update libfabric to 1.14.1 May 2022 1.15.1
- Update libfabric to 1.14.0amzn1.0 March 2022 1.15.0
- Fix a bug that cause installation fail on Open SuSE 15.3
- Drop support of Open SuSE 15.2 (as Open SuSE 15.2 reached end of life)
- Drop Support of CentOS 8 (as CentOS 8 reached end of life)
- Update libfabric to 1.14.0
- Update efa kernel driver to 1.16.0
- Update rdma-core  to v39.0
- Update Open MPI to version 4.1.2.
Feburary 2022 1.14.1
- Update libfabric to 1.13.2amzn1.0 .
October 2021

Version Changes Release date 1.14.0
- Ingest efa kernel driver 1.14.2.
- Make -g, --enable-gdr  in efa_installer.sh  as a no-op option as the latest efa kernel driver enables GDR support by default.
- Ingest rdma-core v37.0.
- Ingest libfabric 1.13.2.
- Add packages list and compare RPM/DEB to list during installation to prevent unknown package installations.
- Add sleep in installer script to wait for udev rule to apply after EFA driver reload.
October 2021 1.13.0
- Update rdma-core  to v35.0.
- Update libfabric  to v1.13.0amzn1.0.
- Add EFA support for CentOS/RHEL 8 on Gravition2 platform.
- Add version comparison logic in installer script to skip the local package installation when there is one installed in system with higher version.
August 2021 1.12.3
- Update EFA kernel module to 1.13.0.
- Update efa-config package to version 1.9. Improve the calculation of huge page reservation to handle large defaulted huge page size.
July 2021 1.12.2
- Update EFA kernel module to 1.12.3.
- Build Open MPI debian packages with --with-li bevent=external and --with-hwloc=external .
- Bump Open MPI rpm build ID to 2 to fix backward compatibi lity issue of HWLOC on CentOS 8.
- Remove the installation of kernel-devel and kernel-source packages on SLES15SP2 and openSUSE 15.2.
June 2021 1.12.1
- Update Libfabric to version 1.11.2amzon1.1.
- Update EFA kernel module to version 1.12.1.
May 2021

Version Changes Release date 1.12.0
- Update Open MPI to version 4.1.1.
- Update Libfabric to version 1.11.2amzn1.0.
- Build rdma-core for Amazon Linux 2 using the same packaging configuration as the AL2 rdma-core.
- Do not force -Wl,--enable-new-dtags when building Open MPI RPMs.
- Build Open MPI with system libraries for hwloc and libevent.
- Update EFA kernel module to version 1.12.0
- Update efa-config package to version 1.8. Improve the calculation of huge page reservation for long-lived instances.
- Update efa-profile package to version 1.5. Remove the open mpi collective tuning file that worked as a workaround to fix Open MPI 4.1.0 hang on P4d.
- Update rdma-core  to v32.1.
- Drop support for Amazon Linux 1 and Ubuntu 16.04.
May 2021 1.11.2
- Fix Open MPI hang when using Open MPI on P4d by changing the default algorithm used to implement MPI_BARRIER via a configuration file.
- Disable use of builtin atomics in Open MPI on ARM via -- disable-builtin-atomics to work around compiler issue.
February 2021 1.11.1
- Update Open MPI to version 4.1.0.
- Update efa-config package to version 1.7. Improve calculati on of huge page reservation count.
- Update efa-profile package to version 1.3. Removes unneeded collectives decision file now that Open MPI 4.1.0 is used.
December 2020

Version Changes Release date 1.11.0
- Add support for Gravition2 platform.
- Update rdma-core  to version 31.2amzn.
- Update Libfabric to version 1.11.1amzn1.0.
- Update efa-config to version 1.6.
- Update efa-profile to version 1.2.
December 2020 1.10.1
- Add support for CentOS / RHEL 8.
- Add support for Ubuntu 20.04.
- Add support for SUSE Linux Enterprise 15.
November 2020 1.10.0
- Add GPUDirect RDMA support for P4d platform. Use -- enable-gdr  installer option to instal GDR-aware kernel module and userspace.
- Update EFA kernel module to version 1.10.2.
- Update rdma-core  to version 31.amzn0.
- Update Libfabric to version 1.11.1.
- Update Open MPI to version 4.0.5.
- Update efa-config to version 1.5.
- Update efa-profile to version 1.1. Includes improved Open MPI collectives decision file.
October 2020 1.9.5
- Update efa-config to version 1.4. Fixes bug in Open MPI collective decision file.
September 2020 1.9.4
- Update Open MPI to version 4.0.3.
- Update Libfabric to version 1.10.1amazon1.1.
- Update rdma-core  to version 28.amzn0.
July 2020

Version Changes Release date 1.9.3
- Update EFA kernel module to version 1.6.0.
- Update rdma-core  to version 28.amzn0.
- Update Libfabric to version 1.10.1amzn1.1.
- Update efa-config to version 1.3. Adds collectives tuning file for Open MPI.
- Skip dkms installation if it is already installed.
- Fix --skip-kmod  installation mode to actually work.
June 2020 1.8.4
- Move configuration files into efa-config and efa-profile packages so that they are tracked by the operating system package manager.
- Update Open MPI to version 4.0.3.
April 2020 1.8.3
- Update EFA kernel module to version 1.5.1.
- Distributed DKMS on some platforms rather than relying on EPEL repositories for added installation reliability.
- On RHEL 7, install RPMs built on CentOS 7 instead of RPMs built on Amazon Linux 2.
February 2020 1.8.2
- Revert rdma-core  to version 25 due to a mismatch in device naming between kernel module and rdma-core .
January 2020 1.8.1
- Update Libfabric to version 1.9.0amzn1.1.
January 2020 1.8.0
- Update rdma-core  to version 27.0.
- Update EFA kernel module to version 1.5.0.
- Update Libfabric to version 1.9.0amzn1.0.
- Add option --minimal  to install just the EFA kernel module and rdma-core .
December 2019 1.7.1
- Update Libfabric to version 1.8.1amzn1.3.
December 2019

Version Changes Release date 1.7.0
- Add Libfabric module file.
- Update Libfabric to version 1.8.1amzn1.1.
November 2019 1.6.2
- Update Open MPI to version 1.6.2.
October 2019 1.6.1
- Update Libfabric to version 1.8.1amzn1.0.
- Update Open MPI to version 4.0.1.
- Update rdma-core  to version 26.0.
October 2019 1.5.4
- Update EFA kernel module to version 1.4.1.
September 2019 1.5.3
- Update EFA kernel module to version 1.3.1.
- Avoid installing kernel-devel  or linux-headers packages unless installing the kernel driver.
September 2019 1.5.1
- Only configure huge pages when EFA device is present.
August 2019 1.5.0
- Update Libfabric to version 1.8.0amzn1.1.
- Update rmda-core  to version 25.0.
August 2019 1.4.1
- Add Libfabric and Open MPI library paths (/opt/amazon/ efa/lib64  and /opt/amazon/efa/openmpi/lib ) to /etc/ld.so.conf.d/efa.conf to ensure the Open MPI and Libfabric shared libraries are properly located.
July 2019 1.4.0
- Update EFA kernel module to version 1.3.0.
- Update Libfabric to version 1.8.0amzn1.0
- First release to support Intel MPI 2019 Update 4.
July 2019
