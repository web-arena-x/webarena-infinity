# Enhanced networking on Amazon EC2 instances

Source: apps/user-manuals/aws/ec2-ug.pdf

---

instance metrics do not. This can happen when the instance has a short spike in demand for network resources (known as a microburst), but the CloudWatch metrics are not granular enough to reflect these microsecond spikes.
Learn more
- Instance metrics
- Monitor network performance
# Enhanced networking on Amazon EC2 instances Enhanced networking uses single root I/O virtualization (SR-IOV) to provide high-performance networking capabilities on supported instance types. SR-IOV is a method of device virtualization that provides higher I/O performance and lower CPU utilization when compared to traditional virtualized network interfaces. Enhanced networking provides higher bandwidth, higher packet per second (PPS) performance, and consistently lower latency between instances. There is no additional charge for using enhanced networking.
For information about the supported network speed for each instance type, see Amazon EC2 Instance Types.
You can enable enhanced networking using one of the following mechanisms:
Elastic Network Adapter (ENA)
The Elastic Network Adapter (ENA) supports network speeds of up to 100 Gbps for supported instance types.
All Nitro-based instances use ENA for enhanced networking. In addition, the following Xen- based instances use ENA: H1, I3, G3, m4.16xlarge, P2, P3, P3dn, and R4.
For more information, see Enable enhanced networking with ENA on your EC2 instances.
Intel 82599 Virtual Function (VF) interface The Intel 82599 Virtual Function interface supports network speeds of up to 10 Gbps for supported instance types.
The following instance types use the Intel 82599 VF interface for enhanced networking: C3, C4, D2, I2, M4 (excluding m4.16xlarge), and R3.
For more information, see Enhanced networking with the Intel 82599 VF interface.

Contents
- Enable enhanced networking with ENA on your EC2 instances
- Improve network performance between EC2 instances with ENA Express
- Enhanced networking with the Intel 82599 VF interface
- Monitor network performance for ENA settings on your EC2 instance
- Improve network latency for Linux based EC2 instances
- Nitro system considerations for performance tuning
- Optimize network performance on EC2 Windows instances
## Enable enhanced networking with ENA on your EC2 instances Amazon EC2 provides enhanced networking capabilities through the Elastic Network Adapter (ENA). To use enhanced networking, you must use an AMI that includes the required ENA driver or manually install it. Then you can enable ENA support on your instance.
To review release notes or install instructions for an ENA driver, see the tab that matches your instance operating system platform.
Linux You can review the following documentation on GitHub:
- Review ENA Linux kernel driver release notes on GitHub.
- For an overview of the ENA Linux kernel driver that includes install instructions see Linux kernel driver for Elastic Network Adapter (ENA) family on GitHub.
#### Windows You can review the following documentation from the Manage device drivers section of this guide:
- Track ENA Windows driver version releases.
- Install the ENA driver on EC2 Windows instances.
For Nitro-based instances, enhanced networking capabilities vary by the Nitro version that the instance type implements.

To review network specifications for your instance, choose the instance family link for your instance type. If you're not sure which instance family applies, see Naming conventions in the Amazon EC2 Instance Types guide.
- Network specifications for accelerated computing instances
- Network specifications for compute optimized instances
- Network specifications for general purpose instances
- Network specifications for high-performance computing instances
- Network specifications for memory optimized instances
- Network specifications for storage optimized instances Contents
- Prerequisites for enhanced networking with ENA
- Test whether enhanced networking is enabled
- Enable enhanced networking on your instance
- ENA queues
- Troubleshoot the ENA kernel driver on Linux
- Troubleshoot the Elastic Network Adapter Windows driver
### Prerequisites for enhanced networking with ENA To prepare for enhanced networking using the ENA, set up your instance as follows:
- Launch a Nitro-based instance.
- Ensure that the instance has internet connectivity.
- If you have important data on the instance that you want to preserve, you should back that data up now by creating an AMI from your instance. Updating the ENA kernel driver and enabling the enaSupport attribute might render incompatible instances or operating systems unreachable. If you have a recent backup, your data will still be retained if this happens.
- Linux instances – Launch the instance using a supported version of the Linux kernel and a supported distribution, so that ENA enhanced networking is enabled for your instance automatically. For more information, see ENA Linux Kernel Driver Release Notes.
- Windows instances – If the instance is running Windows Server 2008 R2 SP1, ensure that is has the SHA-2 code signing support update.

- Use AWS CloudShell from the AWS Management Console, or install and configure the AWS CLI or the AWS Tools for Windows PowerShell on any computer you choose, preferably your local desktop or laptop. For more information, see Access Amazon EC2 or the AWS CloudShell User Guide. Enhanced networking cannot be managed from the Amazon EC2 console.
### Test whether enhanced networking is enabled You can test whether enhanced networking is enabled in your instances or your AMIs.
Instance attribute Check the value of the enaSupport instance attribute.
AWS CLI Use the describe-instances command. aws ec2 describe-instances \ --instance-ids i-1234567890abcdef0 \ --query "Reservations[].Instances[].EnaSupport"
If enhanced networking is enabled, the output is as follows.
[ true ]
PowerShell Use the Get-EC2Instance cmdlet.
(Get-EC2Instance -InstanceId i-1234567890abcdef0).Instances.EnaSupport If enhanced networking is enabled, the output is as follows.
True Image attribute

Check the value of the enaSupport image attribute.
AWS CLI Use the describe-images command. aws ec2 describe-images \ --image-id ami-0abcdef1234567890 \ --query "Images[].EnaSupport"
If enhanced networking is enabled, the output is as follows.
[ true ]
PowerShell Use the Get-EC2Image cmdlet.
(Get-EC2Image -ImageId ami-0abcdef1234567890).EnaSupport If enhanced networking is enabled, the output is as follows.
True Linux network interface driver Use the following command to verify that the ena kernel driver is being used on a particular interface, substituting the interface name that you want to check. If you are using a single interface (default), this is eth0. If your Linux distribution supports predictable network names, this could be a name like ens5. For more information, expand the section for RHEL, SUSE, and CentOS in Enable enhanced networking on your instance.
In the following example, the ena kernel driver is not loaded, because the listed driver is vif.
[ec2-user ~]$ ethtool -i eth0 driver: vif

version: firmware-version: bus-info: vif-0 supports-statistics: yes supports-test: no supports-eeprom-access: no supports-register-dump: no supports-priv-flags: no In this example, the ena kernel driver is loaded and at the minimum recommended version. This instance has enhanced networking properly configured.
[ec2-user ~]$ ethtool -i eth0 driver: ena version: 1.5.0g firmware-version: expansion-rom-version: bus-info: 0000:00:05.0 supports-statistics: yes supports-test: no supports-eeprom-access: no supports-register-dump: no supports-priv-flags: no
### Enable enhanced networking on your instance The procedure that you use depends on the operating system of the instance.
#### Amazon Linux The AMIs for Amazon Linux include the kernel driver required for enhanced networking with ENA installed and have ENA support enabled. Therefore, if you launch an instance with an HVM version of Amazon Linux on a supported instance type, enhanced networking is already enabled for your instance. For more information, see Test whether enhanced networking is enabled.
#### Ubuntu The latest Ubuntu HVM AMIs include the kernel driver required for enhanced networking with ENA installed and have ENA support enabled. Therefore, if you launch an instance with the latest Ubuntu HVM AMI on a supported instance type, enhanced networking is already enabled for your instance. For more information, see Test whether enhanced networking is enabled.

If you launched your instance using an older AMI and it does not have enhanced networking enabled already, you can install the linux-aws kernel package to get the latest enhanced networking drivers and update the required attribute.
To install the linux-aws kernel package (Ubuntu 16.04 or later)
Ubuntu 16.04 and 18.04 ship with the Ubuntu custom kernel (linux-aws kernel package). To use a different kernel, contact Support.
To install the linux-aws kernel package (Ubuntu Trusty 14.04)
1. Connect to your instance.
2. Update the package cache and packages. ubuntu:~$ sudo apt-get update && sudo apt-get upgrade -y linux-aws Important If during the update process you are prompted to install grub, use /dev/xvda to install grub onto, and then choose to keep the current version of /boot/grub/ menu.lst.
3. [EBS-backed instance] From your local computer, stop the instance using the Amazon EC2 console or one of the following commands: stop-instances (AWS CLI) or Stop-EC2Instance (AWS Tools for Windows PowerShell).
[Instance store-backed instance] You can't stop the instance to modify the attribute. Instead, proceed to this procedure: To enable enhanced networking on Ubuntu (instance store-backed instances).
4. From your local computer, enable the enhanced networking attribute using one of the following commands:
- modify-instance-attribute (AWS CLI) aws ec2 modify-instance-attribute --instance-id i-1234567890abcdef0 --ena-support
- Edit-EC2InstanceAttribute (Tools for Windows PowerShell)
Edit-EC2InstanceAttribute -InstanceId i-1234567890abcdef0 -EnaSupport $true

5. (Optional) Create an AMI from the instance, as described in Create an Amazon EBS-backed AMI. The AMI inherits the enhanced networking enaSupport attribute from the instance.
Therefore, you can use this AMI to launch another instance with enhanced networking enabled by default.
6. From your local computer, start the instance using the Amazon EC2 console or one of the following commands: start-instances (AWS CLI) or Start-EC2Instance (AWS Tools for Windows PowerShell).
To enable enhanced networking on Ubuntu (instance store-backed instances)
Follow the previous procedure until the step where you stop the instance. Create a new AMI as described in Create an Amazon S3-backed AMI, making sure to enable the enhanced networking attribute when you register the AMI.
- register-image (AWS CLI) aws ec2 register-image --ena-support ...
- Register-EC2Image (AWS Tools for Windows PowerShell)
Register-EC2Image -EnaSupport $true ...
#### RHEL, SUSE, CentOS The latest AMIs for Red Hat Enterprise Linux, SUSE Linux Enterprise Server, and CentOS include the kernel driver required for enhanced networking with ENA and have ENA support enabled.
Therefore, if you launch an instance with the latest AMI on a supported instance type, enhanced networking is already enabled for your instance. For more information, see Test whether enhanced networking is enabled.
The following procedure provides the general steps for enabling enhanced networking on a Linux distribution other than Amazon Linux AMI or Ubuntu. For more information, such as detailed syntax for commands, file locations, or package and tool support, see the documentation for your Linux distribution.
To enable enhanced networking on Linux
1. Connect to your instance.

2. Clone the source code for the ena kernel driver on your instance from GitHub at https:// github.com/amzn/amzn-drivers. (SUSE Linux Enterprise Server 12 SP2 and later include ENA 2.02 by default, so you are not required to download and compile the ENA driver. For SUSE Linux Enterprise Server 12 SP2 and later, you should file a request to add the driver version you want to the stock kernel). git clone https://github.com/amzn/amzn-drivers
3. Compile and install the ena kernel driver on your instance. These steps depend on the Linux distribution. For more information about compiling the kernel driver on Red Hat Enterprise Linux, see How do I install the latest ENS driver for enhanced network support on an Amazon EC2 instance that runs RHEL?
4. Run the sudo depmod command to update kernel driver dependencies.
5. Update initramfs on your instance to ensure that the new kernel driver loads at boot time.
For example, if your distribution supports dracut, you can use the following command. dracut -f -v
6. Determine if your system uses predictable network interface names by default. Systems that use systemd or udev versions 197 or greater can rename Ethernet devices and they do not guarantee that a single network interface will be named eth0. This behavior can cause problems connecting to your instance. For more information and to see other configuration options, see Predictable Network Interface Names on the freedesktop.org website. a.
You can check the systemd or udev versions on RPM-based systems with the following command. rpm -qa | grep -e '^systemd-[0-9]\+\|^udev-[0-9]\+' systemd-208-11.el7_0.2.x86_64 In the above Red Hat Enterprise Linux 7 example, the systemd version is 208, so predictable network interface names must be disabled. b.
Disable predictable network interface names by adding the net.ifnames=0 option to the GRUB_CMDLINE_LINUX line in /etc/default/grub. sudo sed -i '/^GRUB\_CMDLINE\_LINUX/s/\"$/\ net\.ifnames\=0\"/' /etc/default/ grub

c.
Rebuild the grub configuration file. sudo grub2-mkconfig -o /boot/grub2/grub.cfg
7. [EBS-backed instance] From your local computer, stop the instance using the Amazon EC2 console or one of the following commands: stop-instances (AWS CLI), Stop-EC2Instance (AWS Tools for Windows PowerShell).
[Instance store-backed instance] You can't stop the instance to modify the attribute. Instead, proceed to this procedure: To enable enhanced networking on Linux (instance store–backed instances).
8. From your local computer, enable the enhanced networking enaSupport attribute using one of the following commands:
- modify-instance-attribute (AWS CLI) aws ec2 modify-instance-attribute --instance-id i-1234567890abcdef0 --ena-support
- Edit-EC2InstanceAttribute (Tools for Windows PowerShell)
Edit-EC2InstanceAttribute -InstanceId i-1234567890abcdef0 -EnaSupport $true
9. (Optional) Create an AMI from the instance, as described in Create an Amazon EBS-backed AMI. The AMI inherits the enhanced networking enaSupport attribute from the instance.
Therefore, you can use this AMI to launch another instance with enhanced networking enabled by default.
If your instance operating system contains an /etc/udev/rules.d/70-persistent- net.rules file, you must delete it before creating the AMI. This file contains the MAC address for the Ethernet adapter of the original instance. If another instance boots with this file, the operating system will be unable to find the device and eth0 might fail, causing boot issues.
This file is regenerated at the next boot cycle, and any instances launched from the AMI create their own version of the file.
10. From your local computer, start the instance using the Amazon EC2 console or one of the following commands: start-instances (AWS CLI) or Start-EC2Instance (AWS Tools for Windows PowerShell).
11. (Optional) Connect to your instance and verify that the kernel driver is installed.

If you are unable to connect to your instance after enabling enhanced networking, see Troubleshoot the ENA kernel driver on Linux.
To enable enhanced networking on Linux (instance store–backed instances)
Follow the previous procedure until the step where you stop the instance. Create a new AMI as described in Create an Amazon S3-backed AMI, making sure to enable the enhanced networking attribute when you register the AMI.
- register-image (AWS CLI) aws ec2 register-image --ena-support ...
- Register-EC2Image (AWS Tools for Windows PowerShell)
Register-EC2Image -EnaSupport ...
#### Ubuntu with DKMS This method is for testing and feedback purposes only. It is not intended for use with production deployments. For production deployments, see Ubuntu.
Important Using DKMS voids the support agreement for your subscription. It should not be used for production deployments.
To enable enhanced networking with ENA on Ubuntu (EBS-backed instances)
1. Follow steps 1 and 2 in Ubuntu.
2. Install the build-essential packages to compile the kernel driver and the dkms package so that your ena kernel driver is rebuilt every time your kernel is updated. ubuntu:~$ sudo apt-get install -y build-essential dkms
3. Clone the source for the ena kernel driver on your instance from GitHub at https:// github.com/amzn/amzn-drivers.

ubuntu:~$ git clone https://github.com/amzn/amzn-drivers
4. Move the amzn-drivers package to the /usr/src/ directory so DKMS can find it and build it for each kernel update. Append the version number (you can find the current version number in the release notes) of the source code to the directory name. For example, version 1.0.0 is shown in the following example. ubuntu:~$ sudo mv amzn-drivers /usr/src/amzn-drivers-1.0.0
5. Create the DKMS configuration file with the following values, substituting your version of ena.
Create the file. ubuntu:~$ sudo touch /usr/src/amzn-drivers-1.0.0/dkms.conf Edit the file and add the following values. ubuntu:~$ sudo vim /usr/src/amzn-drivers-1.0.0/dkms.conf PACKAGE_NAME="ena"
PACKAGE_VERSION="1.0.0"
CLEAN="make -C kernel/linux/ena clean"
MAKE="make -C kernel/linux/ena/ BUILD_KERNEL=${kernelver}"
BUILT_MODULE_NAME[0]="ena"
BUILT_MODULE_LOCATION="kernel/linux/ena"
DEST_MODULE_LOCATION[0]="/updates"
DEST_MODULE_NAME[0]="ena"
AUTOINSTALL="yes"
6. Add, build, and install the ena kernel driver on your instance using DKMS.
Add the kernel driver to DKMS. ubuntu:~$ sudo dkms add -m amzn-drivers -v 1.0.0 Build the kernel driver using the dkms command. ubuntu:~$ sudo dkms build -m amzn-drivers -v 1.0.0 Install the kernel driver using dkms.

ubuntu:~$ sudo dkms install -m amzn-drivers -v 1.0.0
7. Rebuild initramfs so the correct kernel driver is loaded at boot time. ubuntu:~$ sudo update-initramfs -u -k all
8. Verify that the ena kernel driver is installed using the modinfo ena command from Test whether enhanced networking is enabled. ubuntu:~$ modinfo ena filename:    /lib/modules/3.13.0-74-generic/updates/dkms/ena.ko version:  1.0.0 license:  GPL description: Elastic Network Adapter (ENA) author:   Amazon.com, Inc. or its affiliates srcversion:  9693C876C54CA64AE48F0CA alias:    pci:v00001D0Fd0000EC21sv*sd*bc*sc*i* alias:    pci:v00001D0Fd0000EC20sv*sd*bc*sc*i* alias:    pci:v00001D0Fd00001EC2sv*sd*bc*sc*i* alias:    pci:v00001D0Fd00000EC2sv*sd*bc*sc*i* depends: vermagic:    3.13.0-74-generic SMP mod_unload modversions parm:     debug:Debug level (0=none,...,16=all) (int) parm:     push_mode:Descriptor / header push mode (0=automatic,1=disable,3=enable)
    0 - Automatically choose according to device capability (default)
    1 - Don't push anything to device memory 3 - Push descriptors and header buffer to device memory (int) parm:     enable_wd:Enable keepalive watchdog (0=disable,1=enable,default=1) (int) parm:     enable_missing_tx_detection:Enable missing Tx completions. (default=1)
 (int) parm:     numa_node_override_array:Numa node override map (array of int) parm:     numa_node_override:Enable/Disable numa node override (0=disable)
(int)
9. Continue with Step 3 in Ubuntu.

#### Enable enhanced networking on Windows If you launched your instance and it does not have enhanced networking enabled already, you must download and install the required network adapter driver on your instance, and then set the enaSupport instance attribute to activate enhanced networking.
To enable enhanced networking
1. Connect to your instance and log in as the local administrator.
2. [Windows Server 2016 and 2019 only] Run the following EC2Launch PowerShell script to configure the instance after the driver is installed.
PS C:\> C:\ProgramData\Amazon\EC2-Windows\Launch\Scripts\InitializeInstance.ps1 - Schedule
3. From the instance, install the driver as follows: a.
Download the latest driver to the instance. b.
Extract the zip archive. c.
Install the driver by running the install.ps1 PowerShell script.
Note If you get an execution policy error, set the policy to Unrestricted (by default it is set to Restricted or RemoteSigned). In a command line, run Set- ExecutionPolicy -ExecutionPolicy Unrestricted, and then run the install.ps1 PowerShell script again.
4. From your local computer, stop the instance using the Amazon EC2 console or one of the following commands: stop-instances (AWS CLI) or Stop-EC2Instance (AWS Tools for Windows PowerShell).
5. Enable ENA support on your instance as follows: a.
From your local computer, check the EC2 instance ENA support attribute on your instance by running one of the following commands. If the attribute is not enabled, the output will be "[]" or blank. EnaSupport is set to false by default.
- describe-instances (AWS CLI)

aws ec2 describe-instances --instance-ids i-1234567890abcdef0 --query "Reservations[].Instances[].EnaSupport"
- Get-EC2Instance (Tools for Windows PowerShell)
(Get-EC2Instance -InstanceId i-1234567890abcdef0).Instances.EnaSupport b.
To enable ENA support, run one of the following commands:
- modify-instance-attribute (AWS CLI) aws ec2 modify-instance-attribute --instance-id i-1234567890abcdef0 --ena- support
- Edit-EC2InstanceAttribute (AWS Tools for Windows PowerShell)
Edit-EC2InstanceAttribute -InstanceId i-1234567890abcdef0 -EnaSupport $true If you encounter problems when you restart the instance, you can also disable ENA support using one of the following commands:
- modify-instance-attribute (AWS CLI) aws ec2 modify-instance-attribute --instance-id i-1234567890abcdef0 --no-ena- support
- Edit-EC2InstanceAttribute (AWS Tools for Windows PowerShell)
Edit-EC2InstanceAttribute -InstanceId i-1234567890abcdef0 -EnaSupport $false c.
Verify that the attribute has been set to true using describe-instances or Get- EC2Instance as shown previously. You should now see the following output:
[ true ]

6. From your local computer, start the instance using the Amazon EC2 console or one of the following commands: start-instances (AWS CLI) or Start-EC2Instance (AWS Tools for Windows PowerShell).
7. On the instance, validate that the ENA driver is installed and enabled as follows: a.
Right-click the network icon and choose Open Network and Sharing Center. b.
Choose the Ethernet adapter (for example, Ethernet 2). c.
Choose Details. For Network Connection Details, check that Description is Amazon Elastic Network Adapter.
8. (Optional) Create an AMI from the instance. The AMI inherits the enaSupport attribute from the instance. Therefore, you can use this AMI to launch another instance with ENA enabled by default.
### ENA queues ENA queues are allocated to network interfaces with default static limits based on the instance type and size. On supported instance types, you can dynamically allocate these queues across Elastic Network Interfaces (ENIs). While the total queue count per instance depends on its type and size, you can configure multiple ENIs with ENA queues until you meet the maximum queue count for the ENI and the instance.
Flexible ENA queue allocation optimizes resource distribution, enabling maximum vCPU utilization.
High network performance workloads typically require multiple ENA queues. You can fine-tune network performance and packets per second (PPS) by adjusting queue counts according to your specific workload needs. For example, network-intensive applications may require more queues compared to CPU-intensive applications.
Topics
- Supported instances
- Modify the number of queues
#### Supported instances The following instances support dynamic allocation of multiple ENA queues.

##### General purpose Instance type Default ENA queues per interface Maximum ENA queues per interface Maximum ENA queues per instance M6i m6i.large 2 2 6 m6i.xlarge 4 4 16 m6i.2xlarge 8 8 32 m6i.4xlarge 8 16 64 m6i.8xlarge 8 32 64 m6i.12xlarge 8 32 64 m6i.16xlarge 8 32 120 m6i.24xlarge 8 32 120 m6i.32xlarge 8 32 120 M6id m6id.large 2 2 6 m6id.xlarge 4 4 16 m6id.2xlarge 8 8 32 m6id.4xlarge 8 16 64 m6id.8xlarge 8 32 64 m6id.12xlarge 8 32 64 m6id.16xlarge 8 32 120

Instance type Default ENA queues per interface Maximum ENA queues per interface Maximum ENA queues per instance m6id.24xlarge 8 32 120 m6id.32xlarge 8 32 120 M6idn m6idn.large 2 2 6 m6idn.xlarge 4 4 16 m6idn.2xlarge 8 8 32 m6idn.4xlarge 8 16 64 m6idn.8xlarge 16 32 128 m6idn.12xlarge 16 32 128 m6idn.16xlarge 16 32 240 m6idn.24xlarge 32 32 480 m6idn.32xlarge 32 32 512 * M6in m6in.large 2 2 6 m6in.xlarge 4 4 16 m6in.2xlarge 8 8 32 m6in.4xlarge 8 16 64 m6in.8xlarge 16 32 128 m6in.12xlarge 16 32 128

Instance type Default ENA queues per interface Maximum ENA queues per interface Maximum ENA queues per instance m6in.16xlarge 16 32 240 m6in.24xlarge 32 32 480 m6in.32xlarge 32 32 512 * M8a m8a.medium 1 1 3 m8a.large 2 2 6 m8a.xlarge 4 4 16 m8a.2xlarge 8 8 32 m8a.4xlarge 8 16 64 m8a.8xlarge 8 32 128 m8a.12xlarge 16 64 192 m8a.16xlarge 16 64 256 m8a.24xlarge 16 128 384 m8a.48xlarge 32 128 768 m8a.metal-24xl 16 128 384 m8a.metal-48xl 32 128 768 M8azn m8azn.medium 1 1 3 m8azn.large 2 2 8

Instance type Default ENA queues per interface Maximum ENA queues per interface Maximum ENA queues per instance m8azn.xlarge 4 4 16 m8azn.3xlarge 4 16 48 m8azn.6xlarge 8 32 96 m8azn.12xlarge 8 64 192 m8azn.24xlarge 16 128 384 m8azn.metal-12xl 8 64 192 m8azn.metal-24xl 16 128 384 M8gb m8gb.medium 1 1 2 m8gb.large 2 2 6 m8gb.xlarge 4 4 16 m8gb.2xlarge 8 8 32 m8gb.4xlarge 8 16 64 m8gb.8xlarge 8 32 128 m8gb.12xlarge 16 64 192 m8gb.16xlarge 16 64 256 m8gb.24xlarge 16 128 384 m8gb.48xlarge 32 128 768 * M8gn

Instance type Default ENA queues per interface Maximum ENA queues per interface Maximum ENA queues per instance m8gn.medium 1 1 2 m8gn.large 2 2 6 m8gn.xlarge 4 4 16 m8gn.2xlarge 8 8 32 m8gn.4xlarge 8 16 64 m8gn.8xlarge 8 32 128 m8gn.12xlarge 16 64 192 m8gn.16xlarge 16 64 256 m8gn.24xlarge 16 128 384 m8gn.48xlarge 32 128 768 * M8i m8i.large 2 2 6 m8i.xlarge 4 4 16 m8i.2xlarge 8 8 32 m8i.4xlarge 8 16 64 m8i.8xlarge 8 32 128 m8i.12xlarge 16 64 192 m8i.16xlarge 16 64 256 m8i.24xlarge 16 128 384

Instance type Default ENA queues per interface Maximum ENA queues per interface Maximum ENA queues per instance m8i.32xlarge 16 128 512 m8i.48xlarge 32 128 768 m8i.96xlarge 32 128 1536 m8i.metal-48xl 32 128 768 m8i.metal-96xl 32 128 1536 M8id m8id.large 2 2 6 m8id.xlarge 4 4 16 m8id.2xlarge 8 8 32 m8id.4xlarge 8 16 64 m8id.8xlarge 8 32 128 m8id.12xlarge 16 64 192 m8id.16xlarge 16 64 256 m8id.24xlarge 16 128 384 m8id.32xlarge 16 128 512 m8id.48xlarge 32 128 768 m8id.96xlarge 32 128 1536 m8id.metal-48xl 32 128 768 m8id.metal-96xl 32 128 1536

Instance type Default ENA queues per interface Maximum ENA queues per interface Maximum ENA queues per instance M8i-flex m8i-flex.large 1 1 3 m8i-flex.xlarge 2 2 8 m8i-flex.2xlarge 4 4 16 m8i-flex.4xlarge 4 8 32 m8i-flex.8xlarge 4 16 64 m8i-flex.12xlarge 8 32 96 m8i-flex.16xlarge 8 32 128 Note
* These instance types feature multiple network cards. Other instance types feature a single network card. For more information, see Network cards.
##### Compute optimized Instance type Default ENA queues per interface Maximum ENA queues per interface Maximum ENA queues per instance C6i c6i.large 2 2 6 c6i.xlarge 4 4 16 c6i.2xlarge 8 8 32

Instance type Default ENA queues per interface Maximum ENA queues per interface Maximum ENA queues per instance c6i.4xlarge 8 16 64 c6i.8xlarge 8 32 64 c6i.12xlarge 8 32 64 c6i.16xlarge 8 32 120 c6i.24xlarge 8 32 120 c6i.32xlarge 8 32 120 C6id c6id.large 2 2 6 c6id.xlarge 4 4 16 c6id.2xlarge 8 8 32 c6id.4xlarge 8 16 64 c6id.8xlarge 8 32 64 c6id.12xlarge 8 32 64 c6id.16xlarge 8 32 120 c6id.24xlarge 8 32 120 c6id.32xlarge 8 32 120 C6in c6in.large 2 2 6 c6in.xlarge 4 4 16

Instance type Default ENA queues per interface Maximum ENA queues per interface Maximum ENA queues per instance c6in.2xlarge 8 8 32 c6in.4xlarge 8 16 64 c6in.8xlarge 16 32 128 c6in.12xlarge 16 32 128 c6in.16xlarge 16 32 240 c6in.24xlarge 32 32 480 c6in.32xlarge 32 32 512 * C8a c8a.medium 1 1 3 c8a.large 2 2 6 c8a.xlarge 4 4 16 c8a.2xlarge 8 8 32 c8a.4xlarge 8 16 64 c8a.8xlarge 8 32 128 c8a.12xlarge 16 64 192 c8a.16xlarge 16 64 256 c8a.24xlarge 16 128 384 c8a.48xlarge 32 128 768 c8a.metal-24xl 16 128 384

Instance type Default ENA queues per interface Maximum ENA queues per interface Maximum ENA queues per instance c8a.metal-48xl 32 128 768 C8gb c8gb.medium 1 1 2 c8gb.large 2 2 6 c8gb.xlarge 4 4 16 c8gb.2xlarge 8 8 32 c8gb.4xlarge 8 16 64 c8gb.8xlarge 8 32 128 c8gb.12xlarge 16 64 192 c8gb.16xlarge 16 64 256 c8gb.24xlarge 16 128 384 c8gb.48xlarge 32 128 768 * c8gb.metal-24xl 32 128 768 c8gb.metal-48xl 32 128 768 * C8gn c8gn.medium 1 1 2 c8gn.large 2 2 6 c8gn.xlarge 4 4 16 c8gn.2xlarge 8 8 32

Instance type Default ENA queues per interface Maximum ENA queues per interface Maximum ENA queues per instance c8gn.4xlarge 8 16 64 c8gn.8xlarge 8 32 128 c8gn.12xlarge 16 64 192 c8gn.16xlarge 16 64 256 c8gn.24xlarge 16 128 384 c8gn.48xlarge 32 128 768 * c8gn.metal-24xl 32 128 768 c8gn.metal-48xl 32 128 768 * C8i c8i.large 2 2 6 c8i.xlarge 4 4 16 c8i.2xlarge 8 8 32 c8i.4xlarge 8 16 64 c8i.8xlarge 8 32 128 c8i.12xlarge 16 64 192 c8i.16xlarge 16 64 256 c8i.24xlarge 16 128 384 c8i.32xlarge 16 128 512 c8i.48xlarge 32 128 768

Instance type Default ENA queues per interface Maximum ENA queues per interface Maximum ENA queues per instance c8i.96xlarge 32 128 1536 c8i.metal-48xl 32 128 768 c8i.metal-96xl 32 128 1536 C8id c8id.large 2 2 6 c8id.xlarge 4 4 16 c8id.2xlarge 8 8 32 c8id.4xlarge 8 16 64 c8id.8xlarge 8 32 128 c8id.12xlarge 16 64 192 c8id.16xlarge 16 64 256 c8id.24xlarge 16 128 384 c8id.32xlarge 16 128 512 c8id.48xlarge 32 128 768 c8id.96xlarge 32 128 1536 c8id.metal-48xl 32 128 768 c8id.metal-96xl 32 128 1536 C8i-flex c8i-flex.large 1 1 3

Instance type Default ENA queues per interface Maximum ENA queues per interface Maximum ENA queues per instance c8i-flex.xlarge 2 2 8 c8i-flex.2xlarge 4 4 16 c8i-flex.4xlarge 4 8 32 c8i-flex.8xlarge 4 16 64 c8i-flex.12xlarge 8 32 96 c8i-flex.16xlarge 8 32 128 Note
* These instance types feature multiple network cards. Other instance types feature a single network card. For more information, see Network cards.
##### Memory optimized Instance type Default ENA queues per interface Maximum ENA queues per interface Maximum ENA queues per instance R6i r6i.large 2 2 6 r6i.xlarge 4 4 16 r6i.2xlarge 8 8 32 r6i.4xlarge 8 16 64 r6i.8xlarge 8 32 64

Instance type Default ENA queues per interface Maximum ENA queues per interface Maximum ENA queues per instance r6i.12xlarge 8 32 64 r6i.16xlarge 8 32 120 r6i.24xlarge 8 32 120 r6i.32xlarge 8 32 120 R6id r6id.large 2 2 6 r6id.xlarge 4 4 16 r6id.2xlarge 8 8 32 r6id.4xlarge 8 16 64 r6id.8xlarge 8 32 64 r6id.12xlarge 8 32 64 r6id.16xlarge 8 32 120 r6id.24xlarge 8 32 120 r6id.32xlarge 8 32 120 R6idn r6idn.large 2 2 6 r6idn.xlarge 4 4 16 r6idn.2xlarge 8 8 32 r6idn.4xlarge 8 16 64

Instance type Default ENA queues per interface Maximum ENA queues per interface Maximum ENA queues per instance r6idn.8xlarge 16 32 128 r6idn.12xlarge 16 32 128 r6idn.16xlarge 16 32 240 r6idn.24xlarge 32 32 480 r6idn.32xlarge 32 32 512 * R6in r6in.large 2 2 6 r6in.xlarge 4 4 16 r6in.2xlarge 8 8 32 r6in.4xlarge 8 16 64 r6in.8xlarge 16 32 128 r6in.12xlarge 16 32 128 r6in.16xlarge 16 32 240 r6in.24xlarge 32 32 480 r6in.32xlarge 32 32 512 * R8a r8a.medium 1 1 3 r8a.large 2 2 6 r8a.xlarge 4 4 16

Instance type Default ENA queues per interface Maximum ENA queues per interface Maximum ENA queues per instance r8a.2xlarge 8 8 32 r8a.4xlarge 8 16 64 r8a.8xlarge 8 32 128 r8a.12xlarge 16 64 192 r8a.16xlarge 16 64 256 r8a.24xlarge 16 128 384 r8a.48xlarge 32 128 768 r8a.metal-24xl 16 128 384 r8a.metal-48xl 32 128 768 R8gb r8gb.medium 1 1 2 r8gb.large 2 2 6 r8gb.xlarge 4 4 16 r8gb.2xlarge 8 8 32 r8gb.4xlarge 8 16 64 r8gb.8xlarge 8 32 128 r8gb.12xlarge 16 64 192 r8gb.16xlarge 16 64 256 r8gb.24xlarge 16 128 384

Instance type Default ENA queues per interface Maximum ENA queues per interface Maximum ENA queues per instance r8gb.48xlarge 32 128 768 * r8gb.metal-24xl 32 128 768 r8gb.metal-48xl 32 128 768 * R8gn r8gn.medium 1 1 2 r8gn.large 2 2 6 r8gn.xlarge 4 4 16 r8gn.2xlarge 8 8 32 r8gn.4xlarge 8 16 64 r8gn.8xlarge 8 32 128 r8gn.12xlarge 16 64 192 r8gn.16xlarge 16 64 256 r8gn.24xlarge 16 128 384 r8gn.48xlarge 32 128 768 * r8gn.metal-24xl 32 128 768 r8gn.metal-48xl 32 128 768 * R8i r8i.large 2 2 6 r8i.xlarge 4 4 16

Instance type Default ENA queues per interface Maximum ENA queues per interface Maximum ENA queues per instance r8i.2xlarge 8 8 32 r8i.4xlarge 8 16 64 r8i.8xlarge 8 32 128 r8i.12xlarge 16 64 192 r8i.16xlarge 16 64 256 r8i.24xlarge 16 128 384 r8i.32xlarge 16 128 512 r8i.48xlarge 32 128 768 r8i.96xlarge 32 128 1536 r8i.metal-48xl 32 128 768 r8i.metal-96xl 32 128 1536 R8id r8id.large 2 2 6 r8id.xlarge 4 4 16 r8id.2xlarge 8 8 32 r8id.4xlarge 8 16 64 r8id.8xlarge 8 32 128 r8id.12xlarge 16 64 192 r8id.16xlarge 16 64 256

Instance type Default ENA queues per interface Maximum ENA queues per interface Maximum ENA queues per instance r8id.24xlarge 16 128 384 r8id.32xlarge 16 128 512 r8id.48xlarge 32 128 768 r8id.96xlarge 32 128 1536 r8id.metal-48xl 32 128 768 r8id.metal-96xl 32 128 1536 R8i-flex r8i-flex.large 1 1 3 r8i-flex.xlarge 2 2 8 r8i-flex.2xlarge 4 4 16 r8i-flex.4xlarge 4 8 32 r8i-flex.8xlarge 4 16 64 r8i-flex.12xlarge 8 32 96 r8i-flex.16xlarge 8 32 128 X8aedz x8aedz.large 2 2 8 x8aedz.xlarge 4 4 16 x8aedz.3xlarge 4 16 48 x8aedz.6xlarge 8 32 96

Instance type Default ENA queues per interface Maximum ENA queues per interface Maximum ENA queues per instance x8aedz.12xlarge 8 64 192 x8aedz.24xlarge 16 128 384 x8aedz.metal-12xl 8 64 192 x8aedz.metal-24xl 16 128 384 X8i x8i.large 2 2 6 x8i.xlarge 4 4 16 x8i.2xlarge 8 8 32 x8i.4xlarge 8 16 64 x8i.8xlarge 8 32 128 x8i.12xlarge 16 64 192 x8i.16xlarge 16 64 256 x8i.24xlarge 16 128 384 x8i.32xlarge 16 128 512 x8i.48xlarge 32 128 768 x8i.64xlarge 32 128 1024 x8i.96xlarge 32 128 1536 x8i.metal-48xl 32 128 768 x8i.metal-96xl 32 128 1536

Note
* These instance types feature multiple network cards. Other instance types feature a single network card. For more information, see Network cards.
#### Modify the number of queues You can modify the number of ENA queues using AWS Management Console or AWS CLI. In the AWS Management Console, the ENA queues configuration is available under each Network interface setting.
To modify the number of ENA queues using the AWS CLI, use either one of the following commands. Before modifying the queue count, use the following command to check your current queue count. aws ec2 describe-instances --instance-id i-1234567890abcdef0 Note
- Your instance must be stopped before modifying the number of ENA queues.
- The value for ENA queues must be a power of 2, such as, 1, 2, 4, 8, 16, 32, etc.
- The number of queues allocated to any single ENI cannot exceed the number of vCPUs available on your instance. attach-network-interface In the following example, 32 ENA queues are configured on an ENI. aws ec2 attach-network-interface \ --network-interface-id eni-001aa1bb223cdd4e4 \ --instance-id i-1234567890abcdef0 \ --device-index 1 \ --ena-queue-count 32 run-instances In the following example, 2 ENA queues each are configured on 3 ENIs.

aws ec2 run-instances \ --image-id ami-12ab3c30 \ --instance-type c6i.large \ --min-count 1 \ --max-count 1 \ --network-interfaces \ "[{\"DeviceIndex\":0,\"SubnetId\":\"subnet-123456789012a345a\",\"EnaQueueCount \":2}, {\"DeviceIndex\":1,\"SubnetId\":\"subnet-123456789012a345a\",\"EnaQueueCount \":2}, {\"DeviceIndex\":2,\"SubnetId\":\"subnet-123456789012a345a\",\"EnaQueueCount \":2}]" modify-network-interface-attribute In the following example, 32 ENA queues are configured on an ENI. aws ec2 modify-network-interface-attribute \ --network-interface-id eni-1234567890abcdef0 \ --attachment AttachmentId=eni-attach-12345678,EnaQueueCount=32 In the following example, the ENA count is reset to the default value. aws ec2 modify-network-interface-attribute \ --network-interface-id eni-1234567890abcdef0 \ --attachment AttachmentId=eni-attach-12345678,DefaultEnaQueueCount=true
### Troubleshoot the ENA kernel driver on Linux The Elastic Network Adapter (ENA) is designed to improve operating system health and reduce the chances of long-term disruption because of unexpected hardware behavior and or failures. The ENA architecture keeps device or driver failures as transparent to the system as possible. This topic provides troubleshooting information for ENA.
If you are unable to connect to your instance, start with the Troubleshoot connectivity issues section.
If you experience performance degradation after migrating to a sixth generation instance type, see the article What do I need to do before I migrate my EC2 instance to a sixth generation instance to make sure that I get maximum network performance?

If you are able to connect to your instance, you can gather diagnostic information by using the failure detection and recovery mechanisms that are covered in the later sections of this topic.
Contents
- Troubleshoot connectivity issues
- Keep-alive mechanism
- Register read timeout
- Statistics
- Driver error logs in syslog
- Sub-optimal configuration notifications
#### Troubleshoot connectivity issues If you lose connectivity while enabling enhanced networking, the ena module might be incompatible with your instance's current running kernel. This can happen if you install the module for a specific kernel version (without dkms, or with an improperly configured dkms.conf file) and then your instance kernel is updated. If the instance kernel that is loaded at boot time does not have the ena module properly installed, your instance will not recognize the network adapter and your instance becomes unreachable.
If you enable enhanced networking for a PV instance or AMI, this can also make your instance unreachable.
If your instance becomes unreachable after enabling enhanced networking with ENA, you can disable the enaSupport attribute for your instance and it will fall back to the stock network adapter.
To disable enhanced networking with ENA (EBS-backed instances)
1. From your local computer, stop the instance by using the Amazon EC2 console, the stop- instances command (AWS CLI), or the Stop-EC2Instance cmdlet (AWS Tools for PowerShell).
2. From your local computer, disable the enhanced networking attribute by using the modify-instance-attribute command with the --no-ena-support option or the Edit- EC2InstanceAttribute cmdlet with the -EnaSupport $false parameter.
3. From your local computer, start the instance using the Amazon EC2 console, the start- instances command, or the Start-EC2Instance cmdlet.

4. (Optional) Connect to your instance and try reinstalling the ena module with your current kernel version by following the steps in Enable enhanced networking with ENA on your EC2 instances.
To disable enhanced networking with ENA (instance store-backed instances)
1. Create a new AMI as described in Create an Amazon S3-backed AMI.
2. When you register the AMI, be sure to include the --no-ena-support option in the stop- instances command (AWS CLI) or the -EnaSupport $false parameter in the Register- EC2Image cmdlet.
#### Keep-alive mechanism The ENA device posts keep-alive events at a fixed rate (usually once every second). The ENA driver implements a watchdog mechanism, which checks for the presence of these keep-alive messages.
If a message or messages are present, the watchdog is rearmed, otherwise the driver concludes that the device experienced a failure and then does the following:
- Dumps its current statistics to syslog
- Resets the ENA device
- Resets the ENA driver state The above reset procedure may result in some traffic loss for a short period of time (TCP connections should be able to recover), but should not otherwise affect the user.
The ENA device may also indirectly request a device reset procedure, by not sending a keep- alive notification, for example, if the ENA device reaches an unknown state after loading an irrecoverable configuration.
The following is an example of the reset procedure:
[18509.800135] ena 0000:00:07.0 eth1: Keep alive watchdog timeout. // The watchdog process initiates a reset [18509.815244] ena 0000:00:07.0 eth1: Trigger reset is on [18509.825589] ena 0000:00:07.0 eth1: tx_timeout: 0 // The driver logs the current statistics [18509.834253] ena 0000:00:07.0 eth1: io_suspend: 0

[18509.842674] ena 0000:00:07.0 eth1: io_resume: 0 [18509.850275] ena 0000:00:07.0 eth1: wd_expired: 1 [18509.857855] ena 0000:00:07.0 eth1: interface_up: 1 [18509.865415] ena 0000:00:07.0 eth1: interface_down: 0 [18509.873468] ena 0000:00:07.0 eth1: admin_q_pause: 0 [18509.881075] ena 0000:00:07.0 eth1: queue_0_tx_cnt: 0 [18509.888629] ena 0000:00:07.0 eth1: queue_0_tx_bytes: 0 [18509.895286] ena 0000:00:07.0 eth1: queue_0_tx_queue_stop: 0 .......
........
[18511.280972] ena 0000:00:07.0 eth1: free uncompleted tx skb qid 3 idx 0x7 // At the end of the down process, the driver discards incomplete packets.
[18511.420112] [ENA_COM: ena_com_validate_version] ena device version: 0.10 //The driver begins its up process [18511.420119] [ENA_COM: ena_com_validate_version] ena controller version: 0.0.1 implementation version 1 [18511.420127] [ENA_COM: ena_com_admin_init] ena_defs : Version:[b9692e8] Build date [Wed Apr  6 09:54:21 IDT 2016]
[18512.252108] ena 0000:00:07.0: Device watchdog is Enabled [18512.674877] ena 0000:00:07.0: irq 46 for MSI/MSI-X [18512.674933] ena 0000:00:07.0: irq 47 for MSI/MSI-X [18512.674990] ena 0000:00:07.0: irq 48 for MSI/MSI-X [18512.675037] ena 0000:00:07.0: irq 49 for MSI/MSI-X [18512.675085] ena 0000:00:07.0: irq 50 for MSI/MSI-X [18512.675141] ena 0000:00:07.0: irq 51 for MSI/MSI-X [18512.675188] ena 0000:00:07.0: irq 52 for MSI/MSI-X [18512.675233] ena 0000:00:07.0: irq 53 for MSI/MSI-X [18512.675279] ena 0000:00:07.0: irq 54 for MSI/MSI-X [18512.772641] [ENA_COM: ena_com_set_hash_function] Feature 10 isn't supported [18512.772647] [ENA_COM: ena_com_set_hash_ctrl] Feature 18 isn't supported [18512.775945] ena 0000:00:07.0: Device reset completed successfully // The reset process is complete
#### Register read timeout The ENA architecture suggests a limited usage of memory mapped I/O (MMIO) read operations.
MMIO registers are accessed by the ENA device driver only during its initialization procedure.
If the driver logs (available in dmesg output) indicate failures of read operations, this may be caused by an incompatible or incorrectly compiled driver, a busy hardware device, or hardware failure.

Intermittent log entries that indicate failures on read operations should not be considered an issue; the driver will retry them in this case. However, a sequence of log entries containing read failures indicate a driver or hardware problem.
Below is an example of driver log entry indicating a read operation failure due to a timeout:
[ 47.113698] [ENA_COM: ena_com_reg_bar_read32] reading reg failed for timeout. expected: req id[1] offset[88] actual: req id[57006] offset[0]
[ 47.333715] [ENA_COM: ena_com_reg_bar_read32] reading reg failed for timeout. expected: req id[2] offset[8] actual: req id[57007] offset[0]
[ 47.346221] [ENA_COM: ena_com_dev_reset] Reg read32 timeout occurred
#### Statistics If you experience insufficient network performance or latency issues, you should retrieve the device statistics and examine them. These statistics can be obtained using ethtool as follows.
[ec2-user ~]$ ethtool -S ethN NIC statistics: tx_timeout: 0 suspend: 0 resume: 0 wd_expired: 0 interface_up: 1 interface_down: 0 admin_q_pause: 0 bw_in_allowance_exceeded: 0 bw_out_allowance_exceeded: 0 pps_allowance_exceeded: 0 conntrack_allowance_available: 450878 conntrack_allowance_exceeded: 0 linklocal_allowance_exceeded: 0 queue_0_tx_cnt: 4329 queue_0_tx_bytes: 1075749 queue_0_tx_queue_stop: 0 ...
The following command output parameters are described below: tx_timeout: N The number of times that the Netdev watchdog was activated.

suspend: N The number of times the driver performed a suspend operation. resume: N The number of times the driver performed a resume operation. wd_expired: N The number of times that the driver did not receive the keep-alive event in the preceding three seconds. interface_up: N The number of times that the ENA interface was brought up. interface_down: N The number of times that the ENA interface was brought down. admin_q_pause: N The number of times the admin queue was not found in a running state. bw_in_allowance_exceeded: N The number of packets queued or dropped because the inbound aggregate bandwidth exceeded the maximum for the instance. bw_out_allowance_exceeded: N The number of packets queued or dropped because the outbound aggregate bandwidth exceeded the maximum for the instance. pps_allowance_exceeded: N The number of packets queued or dropped because the bidirectional PPS exceeded the maximum for the instance. * conntrack_allowance_available: N The number of tracked connections that can be established by the instance before hitting the Connections Tracked allowance of that instance type. Only available for Nitro-based instances.
Not supported with FreeBSD instances or DPDK environments.

conntrack_allowance_exceeded: N The number of packets dropped because connection tracking exceeded the maximum for the instance and new connections could not be established. This can result in packet loss for traffic to or from the instance. linklocal_allowance_exceeded: N The number of packets dropped because the PPS of the traffic to local proxy services exceeded the maximum for the network interface. This impacts traffic to the Amazon DNS service, the Instance Metadata Service, and the Amazon Time Sync Service, but does not impact traffic to custom DNS resolvers. queue_N_tx_cnt: N The number of transmitted packets for this queue. queue_N_tx_bytes: N The number of transmitted bytes for this queue. queue_N_tx_queue_stop: N The number of times that queue N was full and stopped. queue_N_tx_queue_wakeup: N The number of times that queue N resumed after being stopped. queue_N_tx_dma_mapping_err: N Direct memory access error count. If this value is not 0, it indicates low system resources. queue_N_tx_linearize: N The number of times SKB linearization was attempted for this queue. queue_N_tx_linearize_failed: N The number of times SKB linearization failed for this queue. queue_N_tx_napi_comp: N The number of times the napi handler called napi_complete for this queue. queue_N_tx_tx_poll: N The number of times the napi handler was scheduled for this queue.

queue_N_tx_doorbells: N The number of transmission doorbells for this queue. queue_N_tx_prepare_ctx_err: N The number of times ena_com_prepare_tx failed for this queue. queue_N_tx_bad_req_id: N Invalid req_id for this queue. The valid req_id is zero, minus the queue_size, minus 1. queue_N_tx_llq_buffer_copy: N The number of packets whose headers size are larger than llq entry for this queue. queue_N_tx_missed_tx: N The number of packets that were left uncompleted for this queue. queue_N_tx_unmask_interrupt: N The number of times the tx interrupt was unmasked for this queue. queue_N_rx_cnt: N The number of received packets for this queue. queue_N_rx_bytes: N The number of received bytes for this queue. queue_N_rx_rx_copybreak_pkt: N The number of times the rx queue received a packet that is less than the rx_copybreak packet size for this queue. queue_N_rx_csum_good: N The number of times the rx queue received a packet where the checksum was checked and was correct for this queue. queue_N_rx_refil_partial: N The number of times the driver did not succeed in refilling the empty portion of the rx queue with the buffers for this queue. If this value is not zero, it indicates low memory resources. queue_N_rx_bad_csum: N The number of times the rx queue had a bad checksum for this queue (only if rx checksum offload is supported).

queue_N_rx_page_alloc_fail: N The number of time that page allocation failed for this queue. If this value is not zero, it indicates low memory resources. queue_N_rx_skb_alloc_fail: N The number of time that SKB allocation failed for this queue. If this value is not zero, it indicates low system resources. queue_N_rx_dma_mapping_err: N Direct memory access error count. If this value is not 0, it indicates low system resources. queue_N_rx_bad_desc_num: N Too many buffers per packet. If this value is not 0, it indicates the use of very small buffers. queue_N_rx_bad_req_id: N The req_id for this queue is not valid. The valid req_id is from [0, queue_size - 1 ]. queue_N_rx_empty_rx_ring: N The number of times the rx queue was empty for this queue. queue_N_rx_csum_unchecked: N The number of times the rx queue received a packet whose checksum wasn't checked for this queue. queue_N_rx_xdp_aborted: N The number of times that an XDP packet was classified as XDP_ABORT. queue_N_rx_xdp_drop: N The number of times that an XDP packet was classified as XDP_DROP. queue_N_rx_xdp_pass: N The number of times that an XDP packet was classified as XDP_PASS. queue_N_rx_xdp_tx: N The number of times that an XDP packet was classified as XDP_TX. queue_N_rx_xdp_invalid: N The number of times that the XDP return code for the packet was not valid.

queue_N_rx_xdp_redirect: N The number of times that an XDP packet was classified as XDP_REDIRECT. queue_N_xdp_tx_cnt: N The number of transmitted packets for this queue. queue_N_xdp_tx_bytes: N The number of transmitted bytes for this queue. queue_N_xdp_tx_queue_stop: N The number of times that this queue was full and stopped. queue_N_xdp_tx_queue_wakeup: N The number of times that this queue resumed after being stopped. queue_N_xdp_tx_dma_mapping_err: N Direct memory access error count. If this value is not 0, it indicates low system resources. queue_N_xdp_tx_linearize: N The number of times XDP buffer linearization was attempted for this queue. queue_N_xdp_tx_linearize_failed: N The number of times XDP buffer linearization failed for this queue. queue_N_xdp_tx_napi_comp: N The number of times the napi handler called napi_complete for this queue. queue_N_xdp_tx_tx_poll: N The number of times the napi handler was scheduled for this queue. queue_N_xdp_tx_doorbells: N The number of transmission doorbells for this queue. queue_N_xdp_tx_prepare_ctx_err: N The number of times ena_com_prepare_tx failed for this queue. This value should always be zero; if not, see the driver logs.

queue_N_xdp_tx_bad_req_id: N The req_id for this queue is not valid. The valid req_id is from [0, queue_size - 1 ]. queue_N_xdp_tx_llq_buffer_copy: N The number of packets that had their headers copied using llq buffer copy for this queue. queue_N_xdp_tx_missed_tx: N The number of times a tx queue entry missed a completion timeout for this queue. queue_N_xdp_tx_unmask_interrupt: N The number of times the tx interrupt was unmasked for this queue. ena_admin_q_aborted_cmd: N The number of admin commands that were aborted. This usually happens during the auto- recovery procedure. ena_admin_q_submitted_cmd: N The number of admin queue doorbells. ena_admin_q_completed_cmd: N The number of admin queue completions. ena_admin_q_out_of_space: N The number of times that the driver tried to submit new admin command, but the queue was full. ena_admin_q_no_completion: N The number of times that the driver did not get an admin completion for a command.
#### Driver error logs in syslog The ENA driver writes log messages to syslog during system boot. You can examine these logs to look for errors if you are experiencing issues. Below is an example of information logged by the ENA driver in syslog during system boot, along with some annotations for select messages.
Jun  3 22:37:46 ip-172-31-2-186 kernel: [  478.416939] [ENA_COM: ena_com_validate_version] ena device version: 0.10

Jun  3 22:37:46 ip-172-31-2-186 kernel: [  478.420915] [ENA_COM: ena_com_validate_version] ena controller version: 0.0.1 implementation version 1 Jun  3 22:37:46 ip-172-31-2-186 kernel: [  479.256831] ena 0000:00:03.0: Device watchdog is Enabled Jun  3 22:37:46 ip-172-31-2-186 kernel: [  479.672947] ena 0000:00:03.0: creating 8 io queues. queue size: 1024 Jun  3 22:37:46 ip-172-31-2-186 kernel: [  479.680885] [ENA_COM: ena_com_init_interrupt_moderation] Feature 20 isn't supported   // Interrupt moderation is not supported by the device Jun  3 22:37:46 ip-172-31-2-186 kernel: [  479.691609] [ENA_COM: ena_com_get_feature_ex] Feature 10 isn't supported // RSS HASH function configuration is not supported by the device Jun  3 22:37:46 ip-172-31-2-186 kernel: [  479.694583] [ENA_COM: ena_com_get_feature_ex] Feature 18 isn't supported //RSS HASH input source configuration is not supported by the device Jun  3 22:37:46 ip-172-31-2-186 kernel: [  479.697433] [ENA_COM: ena_com_set_host_attributes] Set host attribute isn't supported Jun  3 22:37:46 ip-172-31-2-186 kernel: [  479.701064] ena 0000:00:03.0 (unnamed net_device) (uninitialized): Cannot set host attributes Jun  3 22:37:46 ip-172-31-2-186 kernel: [  479.704917] ena 0000:00:03.0: Elastic Network Adapter (ENA) found at mem f3000000, mac addr 02:8a:3c:1e:13:b5 Queues 8 Jun  3 22:37:46 ip-172-31-2-186 kernel: [  480.805037] EXT4-fs (xvda1): re-mounted.
 Opts: (null)
Jun  3 22:37:46 ip-172-31-2-186 kernel: [  481.025842] NET: Registered protocol family 10 Which errors can I ignore?
The following warnings that may appear in your system's error logs can be ignored for the Elastic Network Adapter:
Set host attribute isn't supported Host attributes are not supported for this device. failed to alloc buffer for rx queue This is a recoverable error, and it indicates that there may have been a memory pressure issue when the error was thrown.
Feature X isn't supported The referenced feature is not supported by the Elastic Network Adapter. Possible values for X include:

- 10: RSS Hash function configuration is not supported for this device.
- 12: RSS Indirection table configuration is not supported for this device.
- 18: RSS Hash Input configuration is not supported for this device.
- 20: Interrupt moderation is not supported for this device.
- 27: The Elastic Network Adapter driver does not support polling the Ethernet capabilities from snmpd.
Failed to config AENQ The Elastic Network Adapter does not support AENQ configuration.
Trying to set unsupported AENQ events This error indicates an attempt to set an AENQ events group that is not supported by the Elastic Network Adapter.
#### Sub-optimal configuration notifications The ENA device detects sub-optimal configuration settings in the driver that you can change. The device notifies the ENA driver and logs a warning to the console. The following example shows the format of the warning message.
Sub-optimal configuration notification code: 1. Refer to AWS ENA documentation for additional details and mitigation options.
The following list shows notification code details and recommended actions for sub-optimal configuration findings.
- Code 1: ENA Express with wide LLQ configuration is not recommended ENA Express ENI is configured with wide LLQ. This configuration is sub-optimal and could impact performance for ENA Express. We recommend that you disable wide LLQ settings when you use ENA Express ENIs as follows. sudo rmmod ena && sudo modprobe ena force_large_llq_header=0 For more information about optimal configuration for ENA Express, see Improve network performance between EC2 instances with ENA Express.
- Code 2: ENA Express ENI with sub-optimal Tx queue depth is not recommended

ENA Express ENI is configured with sub-optimal Tx queue depth. This configuration could impact performance for ENA Express. We recommend that you enlarge all Tx queues to the maximum value for the network interface when you use ENA Express ENIs as follows.
You can run the following ethtool commands to adjust LLQ size. To learn more about how to control, query, and enable wide-LLQ, see the Large Low-Latency Queue (Large LLQ) topic of the Linux kernel driver for ENA documentation in the Amazon Drivers GitHub repository. ethtool -g interface Set your Tx queues to the maximum depth: ethtool -G interface tx depth For more information about optimal configuration for ENA Express, see Improve network performance between EC2 instances with ENA Express.
- Code 3: ENA with regular LLQ size and Tx packet traffic exceeds the maximum header supported size By default, ENA LLQ supports Tx packet header size up to 96 bytes. If the packet header size is larger than 96 bytes, the packet is dropped. To mitigate this issue, we recommend that you enable wide-LLQ, which increases the supported Tx packet header size to a maximum of 224 bytes.
However, when you enable wide-LLQ, the maximum Tx ring size is reduced from 1000 to 512 entries. Wide-LLQ is enabled by default for all Nitro v4 and later instance types.
- Nitro v4 instance types have a default maximum wide-LLQ Tx ring size of 512 entries, which can't be changed.
- Nitro v5 instance types have a default wide-LLQ Tx ring size of 512 entries, which you can increase up to 1000 entries.
You can run the following ethtool commands to adjust LLQ size. To learn more about how to control, query, and enable wide-LLQ, see the Large Low-Latency Queue (Large LLQ) topic of the Linux kernel driver for ENA documentation in the Amazon Drivers GitHub repository.
Find the maximum depth for your Tx queues:

ethtool -g interface Set your Tx queues to the maximum depth: ethtool -G interface tx depth
### Troubleshoot the Elastic Network Adapter Windows driver The Elastic Network Adapter (ENA) is designed to improve operating system health and to reduce unexpected hardware behavior or failures that can disrupt the operation of your Windows instance.
The ENA architecture keeps device or driver failures as transparent to the operating system as possible.
#### Collect diagnostic information on the instance The steps to open Windows operating system (OS) tools vary, depending on what version of the OS is installed on your instance. In the following sections, we use the Run dialog to open the tools, which works the same across all OS versions. However, you can access these tools using any method that you prefer.
Access the Run dialog
- Using the Windows logo key combination: Windows + R
- Using the search bar:
- Enter run in the search bar.
- Select the Run application from the search results.
Some steps require the context menu to access properties or context-sensitive actions. There are several ways to do this, depending on your OS version and hardware.
Access the context menu
- Using your mouse: right-click an item to bring up its context menu.
- Using your keyboard:
- Depending on your OS version, use Shift + F10, or Ctrl + Shift + F10.

- If you have the context key on your keyboard (three horizontal lines in a box), select the item you want and then press the context key.
If you can connect to your instance, use the following techniques to gather diagnostic information for troubleshooting.
##### Check ENA device status To check the status of your ENA Windows driver using the Windows Device Manager, follow these steps:
1. Open the Run dialog using one of the methods described in the preceding section.
2. To open the Windows Device Manager, enter devmgmt.msc in the Run box.
3. Choose OK. This opens the Device Manager window.
4. Select the arrow to the left of Network adapters to expand the list.
5. Choose the name, or open the context menu for the Amazon Elastic Network Adapter, and then choose Properties. This opens the Amazon Elastic Network Adapter Properties dialog.
6. Verify that the message in the General tab says "This device is working properly."
##### Investigate driver event messages To review ENA Windows driver event logs using the Windows Event Viewer, follow these steps:
1. Open the Run dialog using one of the methods described in the preceding section.
2. To open the Windows Event Viewer, enter eventvwr.msc in the Run box.
3. Choose OK. This opens the Event Viewer window.
4. Expand the Windows Logs menu, and then choose System.
5. Under Actions, in the top-right panel, choose Filter Current Log. This displays the filtering dialog.
6. In the Event sources box, enter ena. This limits results to events that were generated by the ENA Windows driver.
7. Choose OK. This shows filtered event log results in the detail sections of the window.
8. To drill down into the details, select an event message from the list.
The following example shows an ENA driver event in the Windows Event Viewer system events list:

###### Event message summary The following table shows event messages that the ENA Windows driver generates.
Input Event ID ENA driver event description Type 5001 Hardware is out of resources Error 5002 Adapter has detected a hardware error Error 5005 Adapter has timed out on NDIS operation that did not complete in a timely  manner Error 5032 Adapter has failed to reset the device Error 5200 Adapter has been initialized Informational 5201 Adapter has been halted Informational 5202 Adapter has been paused Informational

Event ID ENA driver event description Type 5203 Adapter has been restarted Informational 5204 Adapter has been shut down Informational 5205 Adapter has been reset Error 5206 Adapter has been surprise removed Error 5208 Adapter initialization routine has failed Error 5210 Adapter has encountered and successfully recovered an internal issue Error
##### Review performance metrics The ENA Windows driver publishes network performance metrics from the instances where metrics are enabled. You can view and enable metrics on the instance using the native Performance Monitor application. For more information about the metrics that the ENA Windows driver produces, see Monitor network performance for ENA settings on your EC2 instance.
On instances where ENA metrics are enabled, and the Amazon CloudWatch agent is installed, CloudWatch collects the metrics that are associated with the counters in Windows Performance Monitor, as well as some advanced metrics for ENA. These metrics are collected in addition to the metrics enabled by default on EC2 instances. For more information about the metrics, see Metrics collected by the CloudWatch agent in the Amazon CloudWatch User Guide.
Note Performance metrics are available for ENA driver versions 2.4.0 and later (also for version 2.2.3). ENA driver version 2.2.4 was rolled back due to potential performance degradation on the sixth generation EC2 instances. We recommend that you upgrade to the current version of the driver to ensure that you have the latest updates.

Some of the ways that you can use performance metrics include:
- Troubleshoot instance performance issues.
- Choose the right instance size for a workload.
- Proactively plan scaling activities.
- Benchmark applications to determine if they maximize the performance available on an instance.
Refresh rate By default, the driver refreshes metrics using a 1-second interval. However, the application that retrieves the metrics might use a different interval for polling. You can change the refresh interval in Device Manager, using the advanced properties for the driver.
To change the metrics refresh interval for the ENA Windows driver, follow these steps:
1. Open the Run dialog using one of the methods described in the preceding section.
2. To open the Windows Device Manager, enter devmgmt.msc in the Run box.
3. Choose OK. This opens the Device Manager window.
4. Select the arrow to the left of Network adapters to expand the list.
5. Choose the name, or open the context menu for the Amazon Elastic Network Adapter, and then choose Properties. This opens the Amazon Elastic Network Adapter Properties dialog.
6. Open the Advanced tab in the pop-up window.
7. From the Property list, choose Metrics Refresh Interval to change the value.
8. When you are done, choose OK.
#### Investigate sub-optimal configuration notifications The ENA device detects sub-optimal configuration settings in the driver that you can change. The device notifies the ENA driver and logs an event notification. To review sub-optimal events in the Windows Event Viewer
1. Open the Run dialog using one of the methods described in the preceding section.
2. To open the Windows Event Viewer, enter eventvwr.msc in the Run box.
3. Choose OK. This opens the Event Viewer window.
4. Expand the Windows Logs menu, and then choose System.

5. Under Actions, in the top-right panel, choose Filter Current Log. This displays the filtering dialog.
6. In the Event sources box, enter ena. This limits results to events that were generated by the ENA Windows driver.
7. Choose OK. This shows filtered event log results in the detail sections of the window.
Events with ID 59000 notify you of sub-optimal configuration findings. Right-click an event and choose Event Properties to open a detailed view, or select Preview Pane from the View menu to see the same detail.
Open the Details tab to see the event code. In the Binary Data: In words section, the last word is the code.

The following list shows notification code details and recommended actions for sub-optimal configuration findings.
- Code 1: ENA Express with wide LLQ configuration is not recommended

ENA Express ENI is configured with wide LLQ. This configuration is sub-optimal and could impact performance for ENA Express. We recommend that you disable wide LLQ settings when you use ENA Express ENIs as follows.
1. To open the Windows Device Manager, enter devmgmt.msc in the Run box.
2. Choose OK. This opens the Device Manager window.
3. Select the arrow to the left of Network adapters to expand the list.
4. Open the device properties for the Amazon Elastic Network Adapter.
5. From there, open the Advanced tab to make your changes.
6. Select the LLQ Header Size Policy property, and set its value to Normal (128 Bytes).
7. Choose OK to save your changes.
- Code 2: ENA Express ENI with sub-optimal Tx queue depth is not recommended ENA Express ENI is configured with sub-optimal Tx queue depth. This configuration could impact performance for ENA Express. We recommend that you enlarge all Tx queues to the maximum value for the network interface when you use ENA Express ENIs as follows.
Follow these steps to enlarge the Tx queues to the maximum depth:
1. To open the Windows Device Manager, enter devmgmt.msc in the Run box.
2. Choose OK. This opens the Device Manager window.
3. Select the arrow to the left of Network adapters to expand the list.
4. Open the device properties for the Amazon Elastic Network Adapter.
5. From there, open the Advanced tab to make your changes.
6. Select the Transmit Buffers property, and set its value to the maximum supported.
7. Choose OK to save your changes.
#### ENA adapter reset The reset process starts when the ENA Windows driver detects an error on an adapter, and marks the adapter as unhealthy. The driver cannot reset itself, so it depends on the operating system to check the adapter health status, and call the reset handle for the ENA Windows driver. The reset process might result in a brief period of time where traffic loss occurs. However, TCP connections should be able to recover.

The ENA adapter might also indirectly request a device reset procedure, by failing to send a keep- alive notification. For example, if the ENA adapter reaches an unknown state after loading an irrecoverable configuration, it might stop sending keep-alive notifications.
Common causes for ENA adapter reset
- Keep-alive messages are missing The ENA adapter posts keep-alive events at a fixed rate (usually once every second). The ENA Windows driver implements a watchdog mechanism, which periodically checks for the presence of these keep-alive messages. If it detects one or more new messages since the last time it checked, it records a successful outcome. Otherwise, the driver concludes that the device experienced a failure, and initiates a reset sequence.
- Packets are stuck in transmit queues The ENA adapter verifies that packets are flowing through the transmit queues as expected. The ENA Windows driver detects if packets are getting stuck, and initiates a reset sequence if they are.
- Read timeout for Memory Mapped I/O (MMIO) registers To limit memory mapped I/O (MMIO) read operations, the ENA Windows driver accesses MMIO registers only during initialization and reset processes. If the driver detects a timeout, it takes one of the following actions, depending on what process was running:
- If a timeout is detected during initialization, it fails the flow, which results in the driver displaying a yellow exclamation mark by the ENA adapter in Windows Device Manager.
- If a timeout is detected during reset, it fails the flow. The OS then initiates a surprise removal of the ENA adapter, and recovers it by stopping and starting the adapter that was removed.
For more information about surprise removal of a network interface card (NIC), see Handling the Surprise Removal of a NIC in the Microsoft Windows Hardware Developer documentation.
#### Troubleshooting scenarios The following scenarios can help you troubleshoot issues that you might experience with the ENA Windows driver. We recommend that you start with upgrading your ENA driver, if you don't have the latest version. To find the latest driver for your Windows OS version, see Track ENA Windows driver version releases.

##### Unexpected ENA driver version installed
###### Description After you go through the steps to install a specific version of the ENA driver, the Windows Device Manager shows that Windows installed a different version of the ENA driver.
###### Cause When you run the install for a driver package, Windows ranks all of the driver packages that are valid for the given device in the local Driver Store before it begins. Then it selects the package with the lowest rank value as the best match. This can be different from the package that you intended to install. For more information about the device driver package selection process, see How Windows selects a driver package for a device on the Microsoft documentation website.
###### Solution To ensure that Windows installs your chosen driver package version, you can remove lower ranked driver packages from the Driver Store with the PnPUtil command line tool.
Follow these steps to update the ENA driver:
1. Connect to your instance and log in as the local administrator.
2. Open the Device Manager properties window, as described in the Check ENA device status section. This opens the General tab of the Amazon Elastic Network Adapter Properties window.
3. Open the Driver tab.
4. Choose Update Driver. This opens the Update Driver Software – Amazon Elastic Network Adapter dialog box. a.
On the How do you want to search for driver software? page, choose Browse my computer for driver software. b.
On the Browse for driver software on your computer page, choose Let me pick from a list of device drivers on my computer, located below the search bar. c.
On the Select the device driver you want to install for this hardware page, choose Have Disk.... d.
In the Install from Disk window, choose Browse..., next to the file location from the dropdown list.

e.
Navigate to the location where you downloaded the target ENA driver package. Select the file named ena.inf and choose Open. f.
To start the install, choose OK, and then choose Next.
5. If the installer doesn't automatically reboot your instance, run the Restart-Computer PowerShell cmdlet.
PS C:\> Restart-Computer
##### Device warning for ENA driver
###### Description The ENA adapter icon in the Device Manager Network adapters section displays a warning sign (a yellow triangle with an exclamation mark inside).
The following example shows an ENA adapter with the warning icon in Windows Device Manager:
###### Cause This device warning is commonly caused by environment issues, which might require more research, and often require a process of elimination to determine the underlying cause. For a full list of device errors, see Device Manager Error Messages in the Microsoft documentation.
###### Solution The solution for this device warning depends on the root cause. The process of elimination described here includes a few basic steps to help identify and resolve the most common issues that might have a simple solution. Additional root cause analysis is required when these steps do not resolve the issue.
Follow these steps to help identify and resolve common issues:
1. Stop and start the device Open the Device Manager properties window, as described in the Check ENA device status section. This opens the General tab of the Amazon Elastic Network Adapter Properties window, where the Device status displays the error code and a short message.

a.
Open the Driver tab. b.
Choose Disable Device, and respond Yes to the warning message that displays. c.
Choose Enable Device.
2. Stop and start the EC2 instance If the adapter still shows the warning icon in Device Manager, the next step is to stop and start the EC2 instance. This relaunches the instance on different hardware in most cases.
3. Investigate possible instance resource issue If you have stopped and started your EC2 instance, and the problem persists, this might indicate a resource issue on your instance, such as insufficient memory.
##### Connection timeout with adapter reset (error codes 5007, 5205)
###### Description The Windows Event Viewer shows adapter timeout and reset events occurring in combination for ENA adapters. Messages resemble the following examples:
- Event ID 5007: Amazon Elastic Network Adapter : Timed out during an operation.
- Event ID 5205: Amazon Elastic Network Adapter : Adapter reset has been started.
Adapter resets cause minimal traffic disruption. Even when there are multiple resets, it would be unusual for them to cause any severe network disruption.
###### Cause This sequence of events indicates that the ENA Windows driver initiated a reset for an ENA adapter that was unresponsive. However, the mechanism that the device driver uses to detect this issue is subject to false positives resulting from CPU 0 starvation.
###### Solution If this combination of errors happens frequently, check your resource allocations to see where adjustments might be helpful.
1. Open the Run dialog using one of the methods described in the preceding section.

2. To open the Windows Resource Monitor, enter resmon in the Run box.
3. Choose OK. This opens the Resource Monitor window.
4. Open the CPU tab. Per-CPU usage graphs are shown along the right side of the Resource Monitor window.
5. Check the usage levels for CPU 0 to see if they are too high.
We recommend that you configure RSS to exclude CPU 0 for the ENA adapter on larger instance types (more than 16 vCPU). For smaller instance types, configuring RSS might improve the experience, but due to the lower number of available cores, testing is necessary to ensure that constraining CPU cores does not negatively impact performance.
Use the Set-NetAdapterRss command to configure RSS for your ENA adapter, as shown in the following example.
Set-NetAdapterRss -name (Get-NetAdapter | Where-Object {$_.InterfaceDescription -like "*Elastic*"}).Name -Baseprocessorgroup 0 -BaseProcessorNumber 1
##### Migrating to a sixth generation instance infrastructure impacts performance or attachment
###### Description If you migrate to a sixth generation EC2 instance, you might experience reduced performance or ENA attachment failures if you haven't updated your ENA Windows driver version.
###### Cause The sixth generation EC2 instance types require the following minimum version of the ENA Windows driver, based on the instance operating system (OS).
Minimum version Windows Server version ENA driver version Windows Server 2008 R2 2.2.3 or 2.4.0 Windows Server 2012 and later 2.2.3 and later

Windows Server version ENA driver version Windows Workstation 2.2.3 and later
###### Solution Before you upgrade to a sixth generation EC2 instance, make sure that the AMI you launch from has compatible drivers based on the instance OS as shown in the previous table. For more information, see What do I need to do before migrating my EC2 instance to a sixth generation instance to make sure that I get maximum network performance? in the AWS re:Post Knowledge Center.
##### Suboptimal performance for the elastic network interface
###### Description The ENA interface is not performing as expected.
###### Cause Root cause analysis for performance issues is a process of elimination. There are too many variables involved to name a common cause.
###### Solution The first step in your root cause analysis is to review the diagnostic information for the instance that is not performing as expected, to determine if there are errors that might be causing the issue.
For more information, see the Collect diagnostic information on the instance section.
You might need to modify the default operating system configuration to achieve maximum network performance on instances with enhanced networking. Some optimizations, such as turning on checksum offloading and enabling RSS, are configured by default in official Windows AMIs.
For other optimizations that you can apply to the ENA adapter, see the performance adjustments shown in ENA adapter performance adjustments.
We recommend that you proceed with caution, and limit device property adjustments to those that are listed in this section, or to specific changes that are recommended by the AWS support team.
To change ENA adapter properties, follow these steps:

1. Open the Run dialog using one of the methods described in the preceding section.
2. To open the Windows Device Manager, enter devmgmt.msc in the Run box.
3. Choose OK. This opens the Device Manager window.
4. Select the arrow to the left of Network adapters to expand the list.
5. Choose the name, or open the context menu for the Amazon Elastic Network Adapter, and then choose Properties. This opens the Amazon Elastic Network Adapter Properties dialog.
6. To make your changes, open the Advanced tab.
7. When you're done, choose OK to save your changes.
The following example shows an ENA adapter property in the Windows Device Manager:
###### ENA adapter performance adjustments The following table includes properties that can be adjusted to improve performance for the ENA interface.

Input Property Description Default value Adjustment Receive Buffers Controls the number of entries in the software receive queues.
1024 Can be increased up to a maximum of
8192. Receive Side Scaling (RSS)
Enables the efficient distribution of network receive processing  acros s multiple CPUs in multiprocessor systems.
Enabled You can spread the load across multiple processors. To learn more,  see Optimize network performan ce on EC2 Windows instances.
Maximum Number of RSS Queues Sets the maximum number of RSS queues allowed when RSS  is enabled.
32 The number of RSS queues is determined during driver initializ ation,  and includes the following limitations (among others):
- RSS queue limit set by this property
- Instance limits (vCPU count)
- Hardware generation limits (up to 8 RSS queues in ENAv1,

Property Description Default value Adjustment and up to 32 RSS queues   in ENAv2)
You can set the value from 1-32, depending on your instance and  hardw are generation limits.
To learn more,  see Optimize network performance on EC2 Windows instances.
Jumbo packet Enables the use of jumbo ethernet frames (more than 1500 bytes  of payload).
Disabled (this limits payload to 1500 bytes or less)
Value can be set up to 9015, which translates to 9001 bytes of  payload.
This is the maximum payload for jumbo ethernet frames. See Considerations for using jumbo ethernet frames.
###### Considerations for using jumbo ethernet frames Jumbo frames allow more than 1500 bytes of data by increasing the payload size per packet, which increases the percentage of the packet that is not packet overhead. Fewer packets are needed to send the same amount of usable data. However, traffic is limited to a maximum MTU of 1500 in the following cases:
- Traffic outside of a given AWS Region for EC2 Classic.
- Traffic outside of a single VPC.

- Traffic over an inter-Region VPC peering connection.
- Traffic over VPN connections.
- Traffic over an internet gateway.
Note Packets over 1500 bytes are fragmented. If you have the Don't Fragment flag set in the IP header, these packets are dropped.
Jumbo frames should be used with caution for internet-bound traffic, or any traffic that leaves a VPC. Packets are fragmented by intermediate systems, which slows down this traffic. To use jumbo frames inside of a VPC without impacting outbound traffic that's leaving the VPC, try one of the following options:
- Configure the MTU size by route.
- Use multiple network interfaces with different MTU sizes and different routes.
Recommended use cases for jumbo frames Jumbo frames can be useful for traffic inside of and between VPCs. We recommend using jumbo frames for the following use cases:
- For instances that are collocated inside of a cluster placement group, jumbo frames help to achieve the maximum network throughput possible. For more information, see Placement groups for your Amazon EC2 instances.
- You can use jumbo frames for traffic between your VPCs and your on-premises networks over Direct Connect. For more information about using Direct Connect, and verifying jumbo frame capability, see MTU for private virtual interfaces or transit virtual interfaces in the Direct Connect User Guide.
- For more information about supported MTU sizes for transit gateways, see Quotas for your transit gateways in the Amazon VPC Transit Gateways.

## Improve network performance between EC2 instances with ENA Express Express ENA Express is powered by AWS Scalable Reliable Datagram (SRD) technology. SRD is a high performance network transport protocol that uses dynamic routing to increase throughput and minimize tail latency. With ENA Express, you can communicate between two EC2 instances in the same Availability Zone.
Benefits of ENA Express
- Increases the maximum bandwidth a single flow can use from 5 Gbps up to 25 Gbps within the Availability Zone, up to the aggregate instance limit.
- Reduces tail latency of network traffic between EC2 instances, especially during periods of high network load.
- Detects and avoids congested network paths.
- Handles some tasks directly in the network layer, such as packet reordering on the receiving end, and most retransmits that are needed. This frees up the application layer for other work.
Note
- If your application sends or receives a high volume of packets per second, and needs to optimize for latency most of the time, especially during periods when there is no congestion on the network, Enhanced networking might be a better fit for your network.
- ENA Express traffic can't be sent in a Local Zone.
After you've enabled ENA Express for the network interface attachment on an instance, the sending instance initiates communication with the receiving instance, and SRD detects if ENA Express is operating on both the sending instance and the receiving instance. If ENA Express is operating, the communication can use SRD transmission. If ENA Express is not operating, the communication falls back to standard ENA transmission.
During periods of time when network traffic is light, you might notice a slight increase in packet latency (tens of microseconds) when the packet uses ENA Express. During those times, applications that prioritize specific network performance characteristics can benefit from ENA Express as follows:

- Processes can benefit from increased maximum single flow bandwidth from 5 Gbps up to 25 Gbps within the same Availability Zone, up to the aggregate instance limit. For example, if a specific instance type supports up to 12.5 Gbps, the single flow bandwidth is also limited to 12.5 Gbps.
- Longer running processes should experience reduced tail latency during periods of network congestion.
- Processes can benefit from a smoother and more standard distribution for network response times.
Topics
- How ENA Express works
- Supported instance types for ENA Express
- Prerequisites for Linux instances
- Tune performance for ENA Express settings on Linux instances
- Review ENA Express settings for your EC2 instance
- Configure ENA Express settings for your EC2 instance
### How ENA Express works ENA Express is powered by AWS Scalable Reliable Datagram (SRD) technology. It distributes packets for each network flow across different AWS network paths, and dynamically adjusts distribution when it detects signs of congestion. It also manages packet reordering on the receiving end.
To ensure that ENA Express can manage network traffic as intended, sending and receiving instances and the communication between them must meet all of the following requirements:
- Both sending and receiving instance types are supported. See the Supported instance types for ENA Express table for more information.
- Both sending and receiving instances must have ENA Express configured. If there are differences in the configuration, you can run into situations where traffic defaults to standard ENA transmission. The following scenario shows what can happen.
Scenario: Differences in configuration

Instance ENA Express Enabled UDP uses ENA Express Instance 1 Yes Yes Instance 2 Yes No In this case, TCP traffic between the two instances can use ENA Express, as both instances have enabled it. However, since one of the instances does not use ENA Express for UDP traffic, communication between these two instances over UDP uses standard ENA transmission.
- The sending and receiving instances must run in the same Availability Zone.
- The network path between the instances must not include middleware boxes. ENA Express doesn't currently support middleware boxes.
- (Linux instances only) To utilize full bandwidth potential, use driver version 2.2.9 or higher.
- (Linux instances only) To produce metrics, use driver version 2.8 or higher.
If any requirement is unmet, the instances use the standard TCP/UDP protocol but without SRD to communicate.
To ensure that your instance network driver is configured for optimum performance, review the recommended best practices for ENA drivers. These best practices apply to ENA Express, as well.
For more information, see the ENA Linux Driver Best Practices and Performance Optimization Guide on the GitHub website.
Note Amazon EC2 refers to the relationship between an instance and a network interface that's attached to it as an attachment. ENA Express settings apply to the attachment. If the network interface is detached from the instance, the attachment no longer exists, and the ENA Express settings that applied to it are no longer in force. The same is true when an instance is terminated, even if the network interface remains.
After you've enabled ENA Express for the network interface attachments on both the sending instance and the receiving instance, you can use ENA Express metrics to help ensure that your

instances take full advantage of the performance improvements that SRD technology provides. For more information about ENA Express metrics, see Metrics for ENA Express.
### Supported instance types for ENA Express The following instance types support ENA Express.
General purpose Instance type Architecture m6a.12xlarge x86_64 m6a.16xlarge x86_64 m6a.24xlarge x86_64 m6a.32xlarge x86_64 m6a.48xlarge x86_64 m6a.metal x86_64 m6i.8xlarge x86_64 m6i.12xlarge x86_64 m6i.16xlarge x86_64 m6i.24xlarge x86_64 m6i.32xlarge x86_64 m6i.metal x86_64 m6id.8xlarge x86_64 m6id.12xlarge x86_64 m6id.16xlarge x86_64 m6id.24xlarge x86_64

Instance type Architecture m6id.32xlarge x86_64 m6id.metal x86_64 m6idn.8xlarge x86_64 m6idn.12xlarge x86_64 m6idn.16xlarge x86_64 m6idn.24xlarge x86_64 m6idn.32xlarge x86_64 m6idn.metal x86_64 m6in.8xlarge x86_64 m6in.12xlarge x86_64 m6in.16xlarge x86_64 m6in.24xlarge x86_64 m6in.32xlarge x86_64 m6in.metal x86_64 m7a.12xlarge x86_64 m7a.16xlarge x86_64 m7a.24xlarge x86_64 m7a.32xlarge x86_64 m7a.48xlarge x86_64 m7a.metal-48xl x86_64

Instance type Architecture m7g.12xlarge arm64 m7g.16xlarge arm64 m7g.metal arm64 m7gd.12xlarge arm64 m7gd.16xlarge arm64 m7gd.metal arm64 m7i.12xlarge x86_64 m7i.16xlarge x86_64 m7i.24xlarge x86_64 m7i.48xlarge x86_64 m7i.metal-24xl x86_64 m7i.metal-48xl x86_64 m8a.16xlarge x86_64 m8a.24xlarge x86_64 m8a.48xlarge x86_64 m8a.metal-24xl x86_64 m8a.metal-48xl x86_64 m8azn.12xlarge x86_64 m8azn.24xlarge x86_64 m8azn.metal-12xl x86_64

Instance type Architecture m8azn.metal-24xl x86_64 m8g.12xlarge arm64 m8g.16xlarge arm64 m8g.24xlarge arm64 m8g.48xlarge arm64 m8g.metal-24xl arm64 m8g.metal-48xl arm64 m8gb.8xlarge arm64 m8gb.12xlarge arm64 m8gb.16xlarge arm64 m8gb.24xlarge arm64 m8gb.48xlarge arm64 m8gd.12xlarge arm64 m8gd.16xlarge arm64 m8gd.24xlarge arm64 m8gd.48xlarge arm64 m8gd.metal-24xl arm64 m8gd.metal-48xl arm64 m8gn.8xlarge arm64 m8gn.12xlarge arm64

Instance type Architecture m8gn.16xlarge arm64 m8gn.24xlarge arm64 m8gn.48xlarge arm64 m8i.24xlarge x86_64 m8i.32xlarge x86_64 m8i.48xlarge x86_64 m8i.96xlarge x86_64 m8i.metal-48xl x86_64 m8i.metal-96xl x86_64 m8id.24xlarge x86_64 m8id.32xlarge x86_64 m8id.48xlarge x86_64 m8id.96xlarge x86_64 m8id.metal-48xl x86_64 m8id.metal-96xl x86_64 Compute optimized Instance type Architecture c6a.12xlarge x86_64 c6a.16xlarge x86_64

Instance type Architecture c6a.24xlarge x86_64 c6a.32xlarge x86_64 c6a.48xlarge x86_64 c6a.metal x86_64 c6gn.4xlarge arm64 c6gn.8xlarge arm64 c6gn.12xlarge arm64 c6gn.16xlarge arm64 c6i.8xlarge x86_64 c6i.12xlarge x86_64 c6i.16xlarge x86_64 c6i.24xlarge x86_64 c6i.32xlarge x86_64 c6i.metal x86_64 c6id.8xlarge x86_64 c6id.12xlarge x86_64 c6id.16xlarge x86_64 c6id.24xlarge x86_64 c6id.32xlarge x86_64 c6id.metal x86_64

Instance type Architecture c6in.8xlarge x86_64 c6in.12xlarge x86_64 c6in.16xlarge x86_64 c6in.24xlarge x86_64 c6in.32xlarge x86_64 c6in.metal x86_64 c7a.12xlarge x86_64 c7a.16xlarge x86_64 c7a.24xlarge x86_64 c7a.32xlarge x86_64 c7a.48xlarge x86_64 c7a.metal-48xl x86_64 c7g.12xlarge arm64 c7g.16xlarge arm64 c7g.metal arm64 c7gd.12xlarge arm64 c7gd.16xlarge arm64 c7gd.metal arm64 c7gn.4xlarge arm64 c7gn.8xlarge arm64

Instance type Architecture c7gn.12xlarge arm64 c7gn.16xlarge arm64 c7gn.metal arm64 c7i.12xlarge x86_64 c7i.16xlarge x86_64 c7i.24xlarge x86_64 c7i.48xlarge x86_64 c7i.metal-24xl x86_64 c7i.metal-48xl x86_64 c8a.16xlarge x86_64 c8a.24xlarge x86_64 c8a.48xlarge x86_64 c8a.metal-24xl x86_64 c8a.metal-48xl x86_64 c8g.12xlarge arm64 c8g.16xlarge arm64 c8g.24xlarge arm64 c8g.48xlarge arm64 c8g.metal-24xl arm64 c8g.metal-48xl arm64

Instance type Architecture c8gb.8xlarge arm64 c8gb.12xlarge arm64 c8gb.16xlarge arm64 c8gb.24xlarge arm64 c8gb.48xlarge arm64 c8gb.metal-24xl arm64 c8gb.metal-48xl arm64 c8gd.12xlarge arm64 c8gd.16xlarge arm64 c8gd.24xlarge arm64 c8gd.48xlarge arm64 c8gd.metal-24xl arm64 c8gd.metal-48xl arm64 c8gn.8xlarge arm64 c8gn.12xlarge arm64 c8gn.16xlarge arm64 c8gn.24xlarge arm64 c8gn.48xlarge arm64 c8gn.metal-24xl arm64 c8gn.metal-48xl arm64

Instance type Architecture c8i.24xlarge x86_64 c8i.32xlarge x86_64 c8i.48xlarge x86_64 c8i.96xlarge x86_64 c8i.metal-48xl x86_64 c8i.metal-96xl x86_64 c8id.24xlarge x86_64 c8id.32xlarge x86_64 c8id.48xlarge x86_64 c8id.96xlarge x86_64 c8id.metal-48xl x86_64 c8id.metal-96xl x86_64 Memory optimized Instance type Architecture r6a.12xlarge x86_64 r6a.16xlarge x86_64 r6a.24xlarge x86_64 r6a.32xlarge x86_64 r6a.48xlarge x86_64

Instance type Architecture r6a.metal x86_64 r6i.8xlarge x86_64 r6i.12xlarge x86_64 r6i.16xlarge x86_64 r6i.24xlarge x86_64 r6i.32xlarge x86_64 r6i.metal x86_64 r6id.8xlarge x86_64 r6id.12xlarge x86_64 r6id.16xlarge x86_64 r6id.24xlarge x86_64 r6id.32xlarge x86_64 r6id.metal x86_64 r6idn.8xlarge x86_64 r6idn.12xlarge x86_64 r6idn.16xlarge x86_64 r6idn.24xlarge x86_64 r6idn.32xlarge x86_64 r6idn.metal x86_64 r6in.8xlarge x86_64

Instance type Architecture r6in.12xlarge x86_64 r6in.16xlarge x86_64 r6in.24xlarge x86_64 r6in.32xlarge x86_64 r6in.metal x86_64 r7a.12xlarge x86_64 r7a.16xlarge x86_64 r7a.24xlarge x86_64 r7a.32xlarge x86_64 r7a.48xlarge x86_64 r7a.metal-48xl x86_64 r7g.12xlarge arm64 r7g.16xlarge arm64 r7g.metal arm64 r7gd.12xlarge arm64 r7gd.16xlarge arm64 r7gd.metal arm64 r7i.12xlarge x86_64 r7i.16xlarge x86_64 r7i.24xlarge x86_64

Instance type Architecture r7i.48xlarge x86_64 r7i.metal-24xl x86_64 r7i.metal-48xl x86_64 r7iz.8xlarge x86_64 r7iz.12xlarge x86_64 r7iz.16xlarge x86_64 r7iz.32xlarge x86_64 r7iz.metal-16xl x86_64 r7iz.metal-32xl x86_64 r8a.16xlarge x86_64 r8a.24xlarge x86_64 r8a.48xlarge x86_64 r8a.metal-24xl x86_64 r8a.metal-48xl x86_64 r8g.12xlarge arm64 r8g.16xlarge arm64 r8g.24xlarge arm64 r8g.48xlarge arm64 r8g.metal-24xl arm64 r8g.metal-48xl arm64

Instance type Architecture r8gb.8xlarge arm64 r8gb.12xlarge arm64 r8gb.16xlarge arm64 r8gb.24xlarge arm64 r8gb.48xlarge arm64 r8gb.metal-24xl arm64 r8gb.metal-48xl arm64 r8gd.12xlarge arm64 r8gd.16xlarge arm64 r8gd.24xlarge arm64 r8gd.48xlarge arm64 r8gd.metal-24xl arm64 r8gd.metal-48xl arm64 r8gn.8xlarge arm64 r8gn.12xlarge arm64 r8gn.16xlarge arm64 r8gn.24xlarge arm64 r8gn.48xlarge arm64 r8gn.metal-24xl arm64 r8gn.metal-48xl arm64

Instance type Architecture r8i.24xlarge x86_64 r8i.32xlarge x86_64 r8i.48xlarge x86_64 r8i.96xlarge x86_64 r8i.metal-48xl x86_64 r8i.metal-96xl x86_64 r8id.24xlarge x86_64 r8id.32xlarge x86_64 r8id.48xlarge x86_64 r8id.96xlarge x86_64 r8id.metal-48xl x86_64 r8id.metal-96xl x86_64 u7i-6tb.112xlarge x86_64 u7i-8tb.112xlarge x86_64 u7i-12tb.224xlarge x86_64 u7in-16tb.224xlarge x86_64 u7in-24tb.224xlarge x86_64 u7in-32tb.224xlarge x86_64 u7inh-32tb.480xlarge x86_64 x2idn.16xlarge x86_64

Instance type Architecture x2idn.24xlarge x86_64 x2idn.32xlarge x86_64 x2idn.metal x86_64 x2iedn.8xlarge x86_64 x2iedn.16xlarge x86_64 x2iedn.24xlarge x86_64 x2iedn.32xlarge x86_64 x2iedn.metal x86_64 x8g.12xlarge arm64 x8g.16xlarge arm64 x8g.24xlarge arm64 x8g.48xlarge arm64 x8g.metal-24xl arm64 x8g.metal-48xl arm64 x8aedz.24xlarge x86_64 x8aedz.metal-24xl x86_64 x8i.24xlarge x86_64 x8i.32xlarge x86_64 x8i.48xlarge x86_64 x8i.64xlarge x86_64

Instance type Architecture x8i.96xlarge x86_64 x8i.metal-48xl x86_64 x8i.metal-96xl x86_64 Accelerated computing Instance type Architecture g6.48xlarge x86_64 g6e.12xlarge x86_64 g6e.24xlarge x86_64 g6e.48xlarge x86_64 g7e.12xlarge x86_64 g7e.24xlarge x86_64 g7e.48xlarge x86_64 p5.4xlarge x86_64 p5.48xlarge x86_64 p5e.48xlarge x86_64 p5en.48xlarge x86_64 p6-b200.48xlarge x86_64 p6-b300.48xlarge x86_64

Storage optimized Instance type Architecture i4g.4xlarge arm64 i4g.8xlarge arm64 i4g.16xlarge arm64 i4i.8xlarge x86_64 i4i.12xlarge x86_64 i4i.16xlarge x86_64 i4i.24xlarge x86_64 i4i.32xlarge x86_64 i4i.metal x86_64 i7i.12xlarge x86_64 i7i.16xlarge x86_64 i7i.24xlarge x86_64 i7i.48xlarge x86_64 i7i.metal-24xl x86_64 i7i.metal-48xl x86_64 i7ie.12xlarge x86_64 i7ie.18xlarge x86_64 i7ie.24xlarge x86_64 i7ie.48xlarge x86_64

Instance type Architecture i7ie.metal-24xl x86_64 i7ie.metal-48xl x86_64 i8g.12xlarge arm64 i8g.16xlarge arm64 i8g.24xlarge arm64 i8g.48xlarge arm64 i8g.metal-24xl arm64 i8ge.12xlarge arm64 i8ge.18xlarge arm64 i8ge.24xlarge arm64 i8ge.48xlarge arm64 i8ge.metal-24xl arm64 i8ge.metal-48xl arm64 im4gn.4xlarge arm64 im4gn.8xlarge arm64 im4gn.16xlarge arm64
### Prerequisites for Linux instances To ensure that ENA Express can operate effectively, update the settings for your Linux instance as follows.
- If your instance uses jumbo frames, run the following command to set your maximum transmission unit (MTU) to 8900.

[ec2-user ~]$ sudo ip link set dev eth0 mtu 8900
- Increase the receiver (Rx) ring size, as follows:
[ec2-user ~]$ ethtool -G device rx 8192
- To maximize ENA Express bandwidth, configure your TCP queue limits as follows:
1. Set the TCP small queue limit to 1MB or higher. This increases the amount of data that's queued for transmission on a socket. sudo sh -c 'echo 1048576 > /proc/sys/net/ipv4/tcp_limit_output_bytes'
2. Disable byte queue limits on the eth device if they're enabled for your Linux distribution.
This increases data queued for transmission for the device queue. sudo sh -c 'for txq in /sys/class/net/eth0/queues/tx-*; do echo max > ${txq}/ byte_queue_limits/limit_min; done'
Note The ENA driver for the Amazon Linux distribution disables byte queue limits by default.
### Tune performance for ENA Express settings on Linux instances To check your Linux instance configuration for optimal ENA Express performance, you can run the following script that's available on the Amazon GitHub repository: https://github.com/amzn/amzn-ec2-ena-utilities/blob/main/ena-express/check-ena-express- settings.sh The script runs a series of tests and suggests both recommended and required configuration changes.

### Review ENA Express settings for your EC2 instance You can verify the ENA Express settings by instance or by network interface. To update the ENA Express settings, see the section called "Configure instance settings".
Console To view ENA Express settings for a network interface
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the left navigation pane, choose Network interfaces.
3. Select a network interface to see the details for that instance. You can choose the Network interface ID link to open the detail page, or you can select the checkbox on the left side of the list to view details in the detail pane at the bottom of the page.
4. In the Network interface attachment section on the Details tab or detail page, review settings for ENA Express and ENA Express UDP.
To view ENA Express settings for an instance
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the left navigation pane, choose Instances.
3. Select an instance to see the details for that instance. You can choose the Instance ID link to open the detail page, or you can select the checkbox on the left side of the list to view details in the detail pane at the bottom of the page.
4. In the Network interfaces section on the Networking tab, scroll right to review settings for ENA Express and ENA Express UDP.
AWS CLI To get the ENA Express settings for an instance Use the describe-instances command. This command example returns a list of ENA Express configurations for the network interfaces attached to each of the running instances that are specified by the --instance-ids parameter. aws ec2 describe-instances \ --instance-ids i-1234567890abcdef0 i-0598c7d356eba48d7 \

    --query 'Reservations[*].Instances[*].[InstanceId, NetworkInterfaces[*].Attachment.EnaSrdSpecification]'
The following is example output.
[ [ [ "i-1234567890abcdef0", [ { "EnaSrdEnabled": true, "EnaSrdUdpSpecification": { "EnaSrdUdpEnabled": false } } ]
        ]
    ], [ [ "i-0598c7d356eba48d7", [ { "EnaSrdEnabled": true, "EnaSrdUdpSpecification": { "EnaSrdUdpEnabled": false } } ]
        ]
    ]
]
To get the ENA Express settings for a network interface Use the describe-network-interfaces command. aws ec2 describe-network-interfaces \ --network-interface-ids eni-1234567890abcdef0 \ --query NetworkInterfaces[].[NetworkInterfaceId,Attachment.EnaSrdSpecification]
The following is example output.

[ [ "eni-1234567890abcdef0", { "EnaSrdEnabled": true, "EnaSrdUdpSpecification": { "EnaSrdUdpEnabled": false } } ]
]
PowerShell To get the ENA Express settings for a network interface Use the Get-EC2NetworkInterface cmdlet.
Get-EC2NetworkInterface `
    -NetworkInterfaceId eni-1234567890abcdef0 | `
Select-Object `
    Association, NetworkInterfaceId, OwnerId, @{Name = 'AttachTime'; Expression = { $_.Attachment.AttachTime } }, @{Name = 'AttachmentId'; Expression = { $_.Attachment.AttachmentId } }, @{Name = 'DeleteOnTermination'; Expression = { $_.Attachment.DeleteOnTermination } }, @{Name = 'NetworkCardIndex'; Expression = { $_.Attachment.NetworkCardIndex } }, @{Name = 'InstanceId'; Expression = { $_.Attachment.InstanceId } }, @{Name = 'InstanceOwnerId'; Expression = { $_.Attachment.InstanceOwnerId } }, @{Name = 'Status'; Expression = { $_.Attachment.Status } }, @{Name = 'EnaSrdEnabled'; Expression = { $_.Attachment.EnaSrdSpecification.EnaSrdEnabled } }, @{Name = 'EnaSrdUdpEnabled'; Expression = { $_.Attachment.EnaSrdSpecification.EnaSrdUdpSpecification.EnaSrdUdpEnabled } } The following is example output.
Association         :
NetworkInterfaceId  : eni-0d1234e5f6a78901b OwnerId             : 111122223333

AttachTime          : 6/11/2022 1:13:11 AM AttachmentId        : eni-attach-0d1234e5f6a78901b DeleteOnTermination : True NetworkCardIndex    : 0 InstanceId          : i-1234567890abcdef0 InstanceOwnerId     : 111122223333 Status              : attached EnaSrdEnabled       : True EnaSrdUdpEnabled    : False
### Configure ENA Express settings for your EC2 instance You can configure ENA Express for supported EC2 instance types without needing to install any additional software. For more information, see the section called "Supported instance types for ENA Express".
Console To manage ENA Express for a network interface
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the left navigation pane, choose Network interfaces.
3. Select a network interface that is attached to an instance. You can choose the Network interface ID link to open the detail page, or you can select the checkbox on the left side of the list.
4. Choose Manage ENA Express from the Action menu at the top right side of the page. This opens the Manage ENA Express dialog, with the selected network interface ID and current settings displayed.
If the network interface you selected is not attached to an instance, this action does not appear in the menu.
5. To use ENA Express, select the Enable checkbox.
6. When ENA Express is enabled, you can configure UDP settings. To use ENA Express UDP, select the Enable checkbox.
7. To save your settings, choose Save.

To manage ENA Express for an instance
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the left navigation pane, choose Instances.
3. Select the instance that you want to manage. You can choose the Instance ID to open the detail page, or you can select the checkbox on the left side of the list.
4. Select the Network interface to configure for your instance.
5. Choose Manage ENA Express from the Action menu at the top right side of the page.
6. To configure ENA Express for a network interface that's attached to your instance, select it from the Network interface list.
7. To use ENA Express for the selected network interface attachment, select the Enable checkbox.
8. When ENA Express is enabled, you can configure UDP settings. To use ENA Express UDP, select the Enable checkbox.
9. To save your settings, choose Save.
To configure ENA Express when you attach a network interface
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the left navigation pane, choose Network interfaces.
3. Select a network interface that is not attached to an instance (Status is Available). You can choose the Network interface ID link to open the detail page, or you can select the checkbox on the left side of the list.
4. Select the Instance that you'll attach to.
5. To use ENA Express after you attach the network interface to the instance, select the Enable checkbox.
6. When ENA Express is enabled, you can configure UDP settings. To use ENA Express UDP, select the Enable checkbox.
7. To attach the network interface to the instance and save your ENA Express settings, choose Attach.
AWS CLI To configure ENA Express when you attach a network interface

Use the attach-network-interface command, as shown in the following examples.
Example 1: Use ENA Express for TCP traffic, but not UDP traffic This example configures EnaSrdEnabled as true, and allows EnaSrdUdpEnabled to default to false. aws ec2 attach-network-interface \ --network-interface-id eni-1234567890abcdef0 \ --instance-id i-1234567890abcdef0 \ --device-index 1 \ --ena-srd-specification 'EnaSrdEnabled=true'
Example 2: Use ENA Express for both TCP traffic and UDP traffic This example configures both EnaSrdEnabled and EnaSrdUdpEnabled as true. aws ec2 attach-network-interface \ --network-interface-id eni-1234567890abcdef0 \ --instance-id i-1234567890abcdef0 \ --device-index 1 \ --ena-srd-specification 'EnaSrdEnabled=true,EnaSrdUdpSpecification={EnaSrdUdpEnabled=true}'
To update ENA Express settings for a network interface attachment Use the modify-network-interface-attribute command as shown in the following examples.
Example 1: Use ENA Express for TCP traffic, but not UDP traffic This example configures EnaSrdEnabled as true, and allows EnaSrdUdpEnabled to default to false if it has never been set previously. aws ec2 modify-network-interface-attribute \ --network-interface-id eni-1234567890abcdef0 \ --ena-srd-specification 'EnaSrdEnabled=true'
Example 2: Use ENA Express for both TCP traffic and UDP traffic This example configures both EnaSrdEnabled and EnaSrdUdpEnabled as true. aws ec2 modify-network-interface-attribute \

    --network-interface-id eni-1234567890abcdef0 \ --ena-srd-specification 'EnaSrdEnabled=true,EnaSrdUdpSpecification={EnaSrdUdpEnabled=true}'
Example 3: Stop using ENA Express for UDP traffic This example configures EnaSrdUdpEnabled as false. aws ec2 modify-network-interface-attribute \ --network-interface-id eni-1234567890abcdef0 \ --ena-srd-specification 'EnaSrdUdpSpecification={EnaSrdUdpEnabled=false}'
PowerShell To configure ENA Express when you attach a network interface Use the Add-EC2NetworkInterface cmdlet as shown in the following examples.
Example 1: Use ENA Express for TCP traffic, but not UDP traffic This example configures EnaSrdEnabled as true, and allows EnaSrdUdpEnabled to default to false.
Add-EC2NetworkInterface `
    -NetworkInterfaceId eni-1234567890abcdef0 `
    -InstanceId i-1234567890abcdef0 `
    -DeviceIndex 1 `
    -EnaSrdSpecification_EnaSrdEnabled $true Example 2: Use ENA Express for both TCP traffic and UDP traffic This example configures both EnaSrdEnabled and EnaSrdUdpEnabled as true.
Add-EC2NetworkInterface `
    -NetworkInterfaceId eni-1234567890abcdef0 `
    -InstanceId i-1234567890abcdef0 `
    -DeviceIndex 1 `
    -EnaSrdSpecification_EnaSrdEnabled $true `
    -EnaSrdUdpSpecification_EnaSrdUdpEnabled $true To configure ENA Express settings for your network interface attachment

Use the Edit-EC2NetworkInterfaceAttribute cmdlet as shown in the following examples.
Example 1: Use ENA Express for TCP traffic, but not UDP traffic This example configures EnaSrdEnabled as true, and allows EnaSrdUdpEnabled to default to false if it has never been set previously.
Edit-EC2NetworkInterfaceAttribute `
    -NetworkInterfaceId eni-1234567890abcdef0 `
    -EnaSrdSpecification_EnaSrdEnabled $true ; Get-EC2NetworkInterface -NetworkInterfaceId eni-0123f4567890a1b23 | `
Select-Object `
    NetworkInterfaceId, @{Name = 'EnaSrdEnabled'; Expression = { $_.Attachment.EnaSrdSpecification.EnaSrdEnabled }}, @{Name = 'EnaSrdUdpEnabled'; Expression = { $_.Attachment.EnaSrdSpecification.EnaSrdUdpSpecification.EnaSrdUdpEnabled }} | `
Format-List Example 2: Use ENA Express for both TCP traffic and UDP traffic This example configures both EnaSrdEnabled and EnaSrdUdpEnabled as true.
Edit-EC2NetworkInterfaceAttribute `
    -NetworkInterfaceId eni-1234567890abcdef0 `
    -EnaSrdSpecification_EnaSrdEnabled $true `
    -EnaSrdSpecification_EnaSrdUdpSpecification_EnaSrdUdpEnabled $true ; Get-EC2NetworkInterface -NetworkInterfaceId eni-1234567890abcdef0 | `
Select-Object `
    NetworkInterfaceId, @{Name = 'EnaSrdEnabled'; Expression = { $_.Attachment.EnaSrdSpecification.EnaSrdEnabled }}, @{Name = 'EnaSrdUdpEnabled'; Expression = { $_.Attachment.EnaSrdSpecification.EnaSrdUdpSpecification.EnaSrdUdpEnabled }} | `
Format-List Example 3: Stop using ENA Express for UDP traffic This example configures EnaSrdUdpEnabled as false.
Edit-EC2NetworkInterfaceAttribute `
    -NetworkInterfaceId eni-0123f4567890a1b23 `

    -EnaSrdSpecification_EnaSrdUdpSpecification_EnaSrdUdpEnabled $false ; Get-EC2NetworkInterface -NetworkInterfaceId eni-0123f4567890a1b23 | `
Select-Object `
    NetworkInterfaceId, @{Name = 'EnaSrdEnabled'; Expression = { $_.Attachment.EnaSrdSpecification.EnaSrdEnabled }}, @{Name = 'EnaSrdUdpEnabled'; Expression = { $_.Attachment.EnaSrdSpecification.EnaSrdUdpSpecification.EnaSrdUdpEnabled }} | `
Format-List
#### Configure ENA Express at launch You can use one of the following methods to configure ENA Express directly when you launch an instance. The specified links refer you to the AWS Management Console instructions for these methods.
- Launch instance wizard – You can configure ENA Express at launch with the launch instance wizard. For more information, see Advanced network configuration in the Network settings for the launch instance wizard.
- Launch template – You can configure ENA Express at launch when you use a launch template.
For more information, see the Create an Amazon EC2 launch template page, then expand the Network settings section and review the Advanced network configuration.
## Enhanced networking with the Intel 82599 VF interface For Xen-based instances, the Intel 82599 Virtual Function (VF) interface provides enhanced networking capabilities. The interface uses the Intel ixgbevf driver.
The following tabs show how to verify the network adapter driver that's installed for your instance operating system.
Linux Linux network interface driver Use the following command to verify that the module is being used on a particular interface, substituting the interface name that you want to check. If you are using a single interface (default), this is eth0. If the operating system supports predictable network names, this could be a name like ens5.

In the following example, the ixgbevf module is not loaded, because the listed driver is vif.
[ec2-user ~]$ ethtool -i eth0 driver: vif version: firmware-version: bus-info: vif-0 supports-statistics: yes supports-test: no supports-eeprom-access: no supports-register-dump: no supports-priv-flags: no In this example, the ixgbevf module is loaded. This instance has enhanced networking properly configured.
[ec2-user ~]$ ethtool -i eth0 driver: ixgbevf version: 4.0.3 firmware-version: N/A bus-info: 0000:00:03.0 supports-statistics: yes supports-test: yes supports-eeprom-access: no supports-register-dump: yes supports-priv-flags: no Windows Windows network adapter To verify that the driver is installed, connect to your instance and open Device Manager. You should see Intel(R) 82599 Virtual Function listed under Network adapters.
Contents
- Prepare your instance for enhanced networking
- Test whether enhanced networking is enabled
- Enable enhanced networking on your instance
- Troubleshoot connectivity issues

### Prepare your instance for enhanced networking To prepare for enhanced networking using the Intel 82599 VF interface, set up your instance as follows:
- Verify that the instance type is one of the following: C3, C4, D2, I2, M4 (excluding m4.16xlarge), and R3.
- Ensure that the instance has internet connectivity.
- If you have important data on the instance that you want to preserve, you should back that data up now by creating an AMI from your instance. Updating kernels and kernel modules, as well as enabling the sriovNetSupport attribute, might render incompatible instances or operating systems unreachable. If you have a recent backup, your data will still be retained if this happens.
- Linux instances – Launch the instance from an HVM AMI using Linux kernel version of 2.6.32 or later. The latest Amazon Linux HVM AMIs have the modules required for enhanced networking installed and have the required attributes set. Therefore, if you launch an Amazon EBS–backed, enhanced networking–supported instance using a current Amazon Linux HVM AMI, enhanced networking is already enabled for your instance.
Warning Enhanced networking is supported only for HVM instances. Enabling enhanced networking with a PV instance can make it unreachable. Setting this attribute without the proper module or module version can also make your instance unreachable.
- Windows instances – Launch the instance from a 64-bit HVM AMI. You can't enable enhanced networking on Windows Server 2008. Enhanced networking is already enabled for Windows Server 2012 R2 and Windows Server 2016 and later AMIs. Windows Server 2012 R2 includes Intel driver 1.0.15.3 and we recommend that you upgrade that driver to the latest version using the Pnputil.exe utility.
- Use AWS CloudShell from the AWS Management Console, or install and configure the AWS CLI or the AWS Tools for Windows PowerShell on any computer you choose, preferably your local desktop or laptop. For more information, see Access Amazon EC2 or the AWS CloudShell User Guide. Enhanced networking cannot be managed from the Amazon EC2 console.
### Test whether enhanced networking is enabled Verify that the sriovNetSupport attribute is set on the instance or the image.

AWS CLI To check the instance attribute (sriovNetSupport)
Use the following describe-instance-attribute command. If the attribute is set, the value is simple. aws ec2 describe-instance-attribute \ --instance-id i-1234567890abcdef0 \ --attribute sriovNetSupport To check the image attribute (sriovNetSupport)
Use the following describe-images command. If the attribute is set, the value is simple. aws ec2 describe-images \ --image-id ami-0abcdef1234567890 \ --query "Images[].SriovNetSupport"
PowerShell To check the instance attribute (sriovNetSupport)
Use the Get-EC2InstanceAttribute cmdlet. If the attribute is set, the value is simple.
Get-EC2InstanceAttribute `
    -InstanceId i-1234567890abcdef0 `
    -Attribute sriovNetSupport To check the image attribute (sriovNetSupport)
Use the following describe-images command. If the attribute is set, the value is simple.
(Get-EC2Image -ImageId ami-0abcdef1234567890).SriovNetSupport
### Enable enhanced networking on your instance The procedure that you use depends on the operating system of the instance.

Warning There is no way to disable the enhanced networking attribute after you've enabled it.
#### Amazon Linux The latest Amazon Linux HVM AMIs have the ixgbevf module required for enhanced networking installed and have the required sriovNetSupport attribute set. Therefore, if you launch an instance type using a current Amazon Linux HVM AMI, enhanced networking is already enabled for your instance. For more information, see Test whether enhanced networking is enabled.
If you launched your instance using an older Amazon Linux AMI and it does not have enhanced networking enabled already, use the following procedure to enable enhanced networking.
To enable enhanced networking
1. Connect to your instance.
2. From the instance, run the following command to update your instance with the newest kernel and kernel modules, including ixgbevf:
[ec2-user ~]$ sudo yum update
3. From your local computer, reboot your instance using the Amazon EC2 console or one of the following commands: reboot-instances (AWS CLI) or Restart-EC2Instance (AWS Tools for Windows PowerShell).
4. Connect to your instance again and verify that the ixgbevf module is installed and at the minimum recommended version using the modinfo ixgbevf command from Test whether enhanced networking is enabled.
5. [EBS-backed instance] From your local computer, stop the instance using the Amazon EC2 console or one of the following commands: stop-instances (AWS CLI) or Stop-EC2Instance (AWS Tools for Windows PowerShell).
[Instance store-backed instance] You can't stop the instance to modify the attribute. Instead, skip to the next procedure.
6. From your local computer, enable the enhanced networking attribute using one of the following commands:

AWS CLI Use the modify-instance-attribute command as follows. aws ec2 modify-instance-attribute \ --instance-id i-1234567890abcdef0 \ --sriov-net-support simple PowerShell Use the Edit-EC2InstanceAttribute cmdlet as follows.
Edit-EC2InstanceAttribute `
    -InstanceId i-1234567890abcdef0 `
    -SriovNetSupport "simple"
7. (Optional) Create an AMI from the instance, as described in Create an Amazon EBS-backed AMI. The AMI inherits the enhanced networking attribute from the instance. Therefore, you can use this AMI to launch another instance with enhanced networking enabled by default.
8. From your local computer, start the instance using the Amazon EC2 console or one of the following commands: start-instances (AWS CLI) or Start-EC2Instance (AWS Tools for Windows PowerShell).
9. Connect to your instance and verify that the ixgbevf module is installed and loaded on your network interface using the ethtool -i ethn command from Test whether enhanced networking is enabled.
To enable enhanced networking (instance store-backed instances)
Follow the previous procedure until the step where you stop the instance. Create a new AMI as described in Create an Amazon S3-backed AMI, making sure to enable the enhanced networking attribute when you register the AMI.
AWS CLI Use the register-image command as follows. aws ec2 register-image --sriov-net-support simple ...

PowerShell Use Register-EC2Image as follows.
Register-EC2Image -SriovNetSupport "simple" ...
#### Ubuntu Before you begin, check if enhanced networking is already enabled on your instance.
The Quick Start Ubuntu HVM AMIs include the necessary drivers for enhanced networking. If you have a version of ixgbevf earlier than 2.16.4, you can install the linux-aws kernel package to get the latest enhanced networking drivers.
The following procedure provides the general steps for compiling the ixgbevf module on an Ubuntu instance.
To install the linux-aws kernel package
1. Connect to your instance.
2. Update the package cache and packages. ubuntu:~$ sudo apt-get update && sudo apt-get upgrade -y linux-aws Important If during the update process, you are prompted to install grub, use /dev/xvda to install grub, and then choose to keep the current version of /boot/grub/menu.lst.
#### Other Linux distributions Before you begin, check if enhanced networking is already enabled on your instance. The latest Quick Start HVM AMIs include the necessary drivers for enhanced networking, therefore you do not need to perform additional steps.
The following procedure provides the general steps if you need to enable enhanced networking with the Intel 82599 VF interface on a Linux distribution other than Amazon Linux or Ubuntu.

For more information, such as detailed syntax for commands, file locations, or package and tool support, see the specific documentation for your Linux distribution.
To enable enhanced networking on Linux
1. Connect to your instance.
2. Download the source for the ixgbevf module on your instance from Sourceforge at https:// sourceforge.net/projects/e1000/files/ixgbevf%20stable/.
Versions of ixgbevf earlier than 2.16.4, including version 2.14.2, do not build properly on some Linux distributions, including certain versions of Ubuntu.
3. Compile and install the ixgbevf module on your instance.
Warning If you compile the ixgbevf module for your current kernel and then upgrade your kernel without rebuilding the driver for the new kernel, your system might revert to the distribution-specific ixgbevf module at the next reboot. This could make your system unreachable if the distribution-specific version is incompatible with enhanced networking.
4. Run the sudo depmod command to update module dependencies.
5. Update initramfs on your instance to ensure that the new module loads at boot time.
6. Determine if your system uses predictable network interface names by default. Systems that use systemd or udev versions 197 or greater can rename Ethernet devices and they do not guarantee that a single network interface will be named eth0. This behavior can cause problems connecting to your instance. For more information and to see other configuration options, see Predictable Network Interface Names on the freedesktop.org website. a.
You can check the systemd or udev versions on RPM-based systems with the following command:
[ec2-user ~]$ rpm -qa | grep -e '^systemd-[0-9]\+\|^udev-[0-9]\+' systemd-208-11.el7_0.2.x86_64 In the above Red Hat Enterprise Linux 7 example, the systemd version is 208, so predictable network interface names must be disabled.

b.
Disable predictable network interface names by adding the net.ifnames=0 option to the GRUB_CMDLINE_LINUX line in /etc/default/grub.
[ec2-user ~]$ sudo sed -i '/^GRUB\_CMDLINE\_LINUX/s/\"$/\ net\.ifnames\=0\"/' / etc/default/grub c.
Rebuild the grub configuration file.
[ec2-user ~]$ sudo grub2-mkconfig -o /boot/grub2/grub.cfg
7. [EBS-backed instance] From your local computer, stop the instance using the Amazon EC2 console or one of the following commands: stop-instances (AWS CLI) or Stop-EC2Instance (AWS Tools for Windows PowerShell).
[Instance store-backed instance] You can't stop the instance to modify the attribute. Instead, skip to the next procedure.
8. From your local computer, enable the enhanced networking attribute using one of the following commands:
AWS CLI Use the modify-instance-attribute command as follows. aws ec2 modify-instance-attribute \ --instance-id i-1234567890abcdef0 -\ -sriov-net-support simple PowerShell Use the Edit-EC2InstanceAttribute cmdlet as follows.
Edit-EC2InstanceAttribute `
    -InstanceId i-1234567890abcdef0 `
    -SriovNetSupport "simple"
9. (Optional) Create an AMI from the instance, as described in Create an Amazon EBS-backed AMI. The AMI inherits the enhanced networking attribute from the instance. Therefore, you can use this AMI to launch another instance with enhanced networking enabled by default.

If your instance operating system contains an /etc/udev/rules.d/70-persistent- net.rules file, you must delete it before creating the AMI. This file contains the MAC address for the Ethernet adapter of the original instance. If another instance boots with this file, the operating system will be unable to find the device and eth0 might fail, causing boot issues.
This file is regenerated at the next boot cycle, and any instances launched from the AMI create their own version of the file.
10. From your local computer, start the instance using the Amazon EC2 console or one of the following commands: start-instances (AWS CLI) or Start-EC2Instance (AWS Tools for Windows PowerShell).
11. (Optional) Connect to your instance and verify that the module is installed.
To enable enhanced networking (instance store–backed instances)
Follow the previous procedure until the step where you stop the instance. Create a new AMI as described in Create an Amazon S3-backed AMI, making sure to enable the enhanced networking attribute when you register the AMI.
AWS CLI Use the register-image command as follows. aws ec2 register-image --sriov-net-support simple ...
PowerShell Use Register-EC2Image as follows.
Register-EC2Image -SriovNetSupport "simple" ...
Windows If you launched your instance and it does not have enhanced networking enabled already, you must download and install the required network adapter driver on your instance, and then set the sriovNetSupport instance attribute to activate enhanced networking. You can only enable this attribute on supported instance types. For more information, see Enhanced networking on Amazon EC2 instances.

Important To view the latest driver updates in the Windows AMIs, see Windows AMI version history in the AWS Windows AMI Reference.
To enable enhanced networking
1. Connect to your instance and log in as the local administrator.
2. [Windows Server 2016 and later] Run the following EC2 Launch PowerShell script to configure the instance after the driver is installed.
PS C:\> C:\ProgramData\Amazon\EC2-Windows\Launch\Scripts\InitializeInstance.ps1 - Schedule Important The administrator password will reset when you enable the initialize instance EC2 Launch script. You can modify the configuration file to disable the administrator password reset by specifying it in the settings for the initialization tasks.
3. From the instance, download the Intel network adapter driver for your operating system:
- Windows Server 2022 Visit the  download page and download Wired_driver_version_x64.zip.
- Windows Server 2019 including for Server version 1809 and later* Visit the  download page and download Wired_driver_version_x64.zip.
- Windows Server 2016 including for Server version 1803 and earlier* Visit the  download page and download Wired_driver_version_x64.zip.
- Windows Server 2012 R2 Visit the  download page and download Wired_driver_version_x64.zip.
- Windows Server 2012 Visit the  download page and download Wired_driver_version_x64.zip.

- Windows Server 2008 R2 Visit the  download page and download PROWinx64Legacy.exe.
*Server versions 1803 and earlier as well as 1809 and later are not specifically addressed on the Intel Drivers and Software pages.
4. Install the Intel network adapter driver for your operating system.
- Windows Server 2008 R2
1. In the Downloads folder, locate the PROWinx64Legacy.exe file and rename it to PROWinx64Legacy.zip.
2. Extract the contents of the PROWinx64Legacy.zip file.
3. Open the command line, navigate to the extracted folder, and run the following command to use the pnputil utility to add and install the INF file in the driver store.
C:\> pnputil -a PROXGB\Winx64\NDIS62\vxn62x64.inf
- Windows Server 2022, Windows Server 2019, Windows Server 2016, Windows Server 2012 R2, and Windows Server 2012
1. In the Downloads folder, extract the contents of the Wired_driver_version_x64.zip file.
2. Open the command line, navigate to the extracted folder, and run one of the following commands to use the pnputil utility to add and install the INF file in the driver store.
- Windows Server 2022 pnputil -i -a PROXGB\Winx64\NDIS68\vxn68x64.inf
- Windows Server 2019 pnputil -i -a PROXGB\Winx64\NDIS68\vxn68x64.inf
- Windows Server 2016 pnputil -i -a PROXGB\Winx64\NDIS65\vxn65x64.inf
- Windows Server 2012 R2

pnputil -i -a PROXGB\Winx64\NDIS64\vxn64x64.inf
- Windows Server 2012 pnputil -i -a PROXGB\Winx64\NDIS63\vxn63x64.inf
5. From your local computer, enable the enhanced networking attribute using one of the following commands:
AWS CLI Use the modify-instance-attribute command as follows. aws ec2 modify-instance-attribute \ --instance-id i-1234567890abcdef0 \ --sriov-net-support simple PowerShell Use the Edit-EC2InstanceAttribute cmdlet as follows.
Edit-EC2InstanceAttribute `
    -InstanceId i-1234567890abcdef0 `
    -SriovNetSupport "simple"
6. (Optional) Create an AMI from the instance, as described in Create an Amazon EBS-backed AMI. The AMI inherits the enhanced networking attribute from the instance. Therefore, you can use this AMI to launch another instance with enhanced networking enabled by default.
7. From your local computer, start the instance using the Amazon EC2 console or one of the following commands: start-instances (AWS CLI) or Start-EC2Instance (AWS Tools for Windows PowerShell).
### Troubleshoot connectivity issues If you lose connectivity while enabling enhanced networking, the ixgbevf module might be incompatible with the kernel. Try installing the version of the ixgbevf module included with the distribution of Linux for your instance.

If you enable enhanced networking for a PV instance or AMI, this can make your instance unreachable.
For more information, see How do I turn on and configure enhanced networking on my EC2 instances?
## Monitor network performance for ENA settings on your EC2 instance The Elastic Network Adapter (ENA) driver publishes network performance metrics from the instances where they are enabled. You can use these metrics to troubleshoot instance performance issues, choose the right instance size for a workload, plan scaling activities proactively, and benchmark applications to determine whether they maximize the performance available on an instance.
Amazon EC2 defines network maximums at the instance level to ensure a high-quality networking experience, including consistent network performance across instance sizes. AWS provides maximums for the following for each instance:
- Bandwidth capability – Each EC2 instance has a maximum bandwidth for aggregate inbound and outbound traffic, based on instance type and size. Some instances use a network I/O credit mechanism to allocate network bandwidth based on average bandwidth utilization. Amazon EC2 also has maximum bandwidth for traffic to Direct Connect and the internet. For more information, see Amazon EC2 instance network bandwidth.
- Packet-per-second (PPS) performance – Each EC2 instance has a maximum PPS performance, based on instance type and size.
- Connections tracked – The security group tracks each connection established to ensure that return packets are delivered as expected. There is a maximum number of connections that can be tracked per instance. For more information, see Amazon EC2 security group connection tracking
- Link-local service access – Amazon EC2 provides a maximum PPS per network interface for traffic to local proxy services such as the Amazon DNS service, the Instance Metadata Service, and the Amazon Time Sync Service.
When the network traffic for an instance exceeds a maximum, AWS shapes the traffic that exceeds the maximum by queueing and then dropping network packets. You can monitor when traffic exceeds a maximum using the network performance metrics. These metrics inform you, in real time, of impact to network traffic and possible network performance issues.
Contents

- Requirements
- Metrics for the ENA driver
- View the network performance metrics for your instance
- Metrics for ENA Express
- Network performance metrics with the DPDK driver for ENA
- Metrics on instances running FreeBSD
### Requirements
#### Linux instances
- Install ENA driver version 2.2.10 or later. To verify the installed version, use the ethtool command. In the following example, the version meets the minimum requirement.
[ec2-user ~]$ ethtool -i eth0 | grep version version: 2.2.10 To upgrade your ENA driver, see Enhanced networking.
- To import these metrics to Amazon CloudWatch, install the CloudWatch agent. For more information, see Collect network performance metrics in the Amazon CloudWatch User Guide.
- To support the conntrack_allowance_available metric, install ENA driver version 2.8.1 or later.
- To override the egress fragment PPS limit of 1024, install ENA driver version 2.13.3 or later.
#### Windows instances
- Install ENA driver version 2.2.2 or later. To verify the installed version, use Device Manager as follows.
1. Open Device Manager by running devmgmt.msc.
2. Expand Network Adapters.
3. Choose Amazon Elastic Network Adapter, Properties.
4. On the Driver tab, locate Driver Version.
To upgrade your ENA driver, see Enhanced networking.

- To import these metrics to Amazon CloudWatch, install the CloudWatch agent. For more information, see Collect advanced network metrics in the Amazon CloudWatch User Guide.
### Metrics for the ENA driver The ENA driver delivers the following metrics to the instance in real time. They provide the cumulative number of packets queued or dropped on each network interface since the last driver reset.
Metric Description Supported on bw_in_allowance_ex ceeded The number of packets queued or dropped because the inbound aggregate bandwidth exceeded the maximum for the instance.
All instance types bw_out_allowance_e xceeded The number of packets queued or dropped because the outbound aggregate bandwidth exceeded the maximum for the instance.
All instance types conntrack_allowanc e_exceeded The number of packets dropped because connection tracking exceeded the maximum for the instance and new connections could not be established. This can result in packet loss for traffic to or from the instance.
All instance types conntrack_allowanc e_available The number of tracked connections that can be established by the instance before hitting the Connectio ns Tracked allowance of that instance type.
Nitro-based instances only

Metric Description Supported on linklocal_allowanc e_exceeded The number of packets dropped because the PPS of the traffic to local proxy services exceeded the maximum for the network interface. This impacts traffic to the Amazon DNS service, the Instance Metadata Service, and the Amazon Time Sync Service, but does not impact traffic to custom DNS resolvers.
All instance types pps_allowance_exce eded The number of packets queued or dropped because the bidirectional PPS exceeded the maximum for the instance. * All instance types
* Depending on the fragment proxy mode setting for ENA Linux driver v2.13.3 or later, this limit can also include egress fragment drops that exceed 1024 PPS for the network interface. If fragment proxy mode is enabled for the Linux driver, egress fragment drops bypass the 1024 PPS limit that usually applies and are counted within standard PPS allowances. Fragment proxy mode is disabled by default.
### View the network performance metrics for your instance The procedure that you use depends on the operating system of the instance.
Linux instances You can publish metrics to your favorite tools to visualize the metric data. For example, you can publish the metrics to Amazon CloudWatch using the CloudWatch agent. The agent enables you to select individual metrics and control publication.
You can also use the ethtool to retrieve the metrics for each network interface, such as eth0, as follows.
[ec2-user ~]$ ethtool -S eth0

     bw_in_allowance_exceeded: 0 bw_out_allowance_exceeded: 0 pps_allowance_exceeded: 0 conntrack_allowance_exceeded: 0 linklocal_allowance_exceeded: 0 conntrack_allowance_available: 136812 Windows instances You can view the metrics using any consumer of Windows performance counters. The data can be parsed according to the EnaPerfCounters manifest. This is an XML file that defines the performance counter provider and its countersets.
To install the manifest If you launched the instance using an AMI that contains ENA driver 2.2.2 or later, or used the install script in the driver package for ENA driver 2.2.2, the manifest is already installed. To install the manifest manually, use the following steps:
1. Remove the existing manifest using the following command: unlodctr /m:EnaPerfCounters.man
2. Copy the manifest file EnaPerfCounters.man from the driver installation package to %SystemRoot%\System32\drivers.
3. Install the new manifest using the following command: lodctr /m:EnaPerfCounters.man To view metrics using Performance Monitor
1. Open Performance Monitor.
2. Press Ctrl+N to add new counters.
3. Choose ENA Packets Shaping from the list.
4. Select the instances to monitor and choose Add.
5. Choose OK.

### Metrics for ENA Express ENA Express is powered by AWS Scalable Reliable Datagram (SRD) technology. SRD is a high performance network transport protocol that uses dynamic routing to increase throughput and minimize tail latency. If you've enabled ENA Express for the network interface attachments on both the sending instance and receiving instance, you can use ENA Express metrics to help ensure that your instances take full advantage of the performance improvements that SRD technology provides. For example:
- Evaluate your resources to ensure that they have sufficient capacity to establish more SRD connections.
- Identify where there are potential issues that prevent eligible outgoing packets from using SRD.
- Calculate the percentage of outgoing traffic that uses SRD for the instance.
- Calculate the percentage of incoming traffic that uses SRD for the instance.
Note To produce metrics, use driver version 2.8 or higher.
To see a list of metrics for your Linux instance that's filtered for ENA Express, run the following ethtool command for your network interface (shown here as eth0). Take note of the value of the ena_srd_mode metric.
[ec2-user ~]$ ethtool -S eth0 | grep ena_srd NIC statistics: ena_srd_mode: 1 ena_srd_tx_pkts: 0 ena_srd_eligible_tx_pkts: 0 ena_srd_rx_pkts: 0 ena_srd_resource_utilization: 0 The following metrics are available for all instances that have ENA Express enabled. ena_srd_mode Describes which ENA Express features are enabled. Values are as follows:
- 0 = ENA Express off, UDP off

- 1 = ENA Express on, UDP off
- 2 = ENA Express off, UDP on Note This only happens when ENA Express was originally enabled, and UDP was configured to use it. The prior value is retained for UDP traffic.
- 3 = ENA Express on, UDP on ena_srd_eligible_tx_pkts The number of network as follows:
- Both sending and receiving instance types are supported. See the Supported instance types for ENA Express table for more information.
- Both sending and receiving instances must have ENA Express configured.
- The sending and receiving instances must run in the same Availability Zone.
- The network path between the instances must not include middleware boxes. ENA Express doesn't currently support middleware boxes.
Note The ENA Express eligibility metric covers source and destination requirements, and the network between the two endpoints. Eligible packets can still be disqualified after they've already been counted. For example, if an eligible packet is over the maximum transmission unit (MTU) limit, it falls back to standard ENA transmission, though the packet is still reflected as eligible in the counter. ena_srd_tx_pkts The number of SRD packets transmitted within a given time period. ena_srd_rx_pkts The number of SRD packets received within a given time period. ena_srd_resource_utilization The percentage of the maximum allowed memory utilization for concurrent SRD connections that the instance has consumed.

To confirm if packet transmission is using SRD, you can compare the number of eligible packets (ena_srd_eligible_tx_pkts metric) to the number of SRD packets transmitted (ena_srd_tx_pkts metric) during a given time period.
Egress traffic (outgoing packets)
To ensure that your egress traffic uses SRD as expected, compare the number of SRD eligible packets (ena_srd_eligible_tx_pkts) with the number of SRD packets sent (ena_srd_tx_pkts) over a given time period.
Significant differences between the number of eligible packets and the number of SRD packets sent are often caused by resource utilization issues. When the network card attached to the instance has used up its maximum resources, or if packets are over the MTU limit, eligible packets are not able to transmit via SRD, and must fall back to standard ENA transmission. Packets can also fall into this gap during live migrations or live server updates. Additional troubleshooting is required to determine the root cause.
Note You can ignore occasional minor differences between the number of eligible packets and the number of SRD packets. This can happen when your instance establishes a connection to another instance for SRD traffic, for example.
To find out what percentage of your total egress traffic over a given time period uses SRD, compare the number of SRD packets sent (ena_srd_tx_pkts) to the total number of packets sent for the instance (NetworkPacketOut) during that time.
Ingress traffic (incoming packets)
To find out what percentage of your ingress traffic uses SRD, compare the number of SRD packets received (ena_srd_rx_pkts) over a given time period to the total number of packets received for the instance (NetworkPacketIn) during that time.
Resource utilization Resource utilization is based on the number of concurrent SRD connections a single instance can hold at a given time. The resource utilization metric (ena_srd_resource_utilization) keeps track of your current utilization for the instance. As utilization approaches 100%, you can expect to see performance issues. ENA Express falls back from SRD to standard ENA transmission, and the

possibility of dropped packets increases. High resource utilization is a sign that it's time to scale the instance out to improve network performance.
Note When the network traffic for an instance exceeds a maximum, AWS shapes the traffic that exceeds the maximum by queueing and then dropping network packets.
Persistence Egress and ingress metrics accrue while ENA Express is enabled for the instance. Metrics stop accruing if ENA Express is deactivated, but persist as long as the instance is still running. Metrics reset if the instance reboots or is terminated, or if the network interface is detached from the instance.
### Network performance metrics with the DPDK driver for ENA The ENA driver version 2.2.0 and later supports network metrics reporting. DPDK 20.11 includes the ENA driver 2.2.0 and is the first DPDK version to support this feature.
DPDK driver v25.03 or later supports fragment proxy mode. If fragment proxy mode is enabled for the DPDK driver, egress fragment drops bypass the 1024 PPS limit that usually applies and are counted within standard PPS allowances. Fragment proxy mode is disabled by default.
You can use an example application to view DPDK statistics. To start an interactive version of the example application, run the following command.
./app/dpdk-testpmd -- -i Within this interactive session, you can enter a command to retrieve extended statistics for a port.
The following example command retrieves the statistics for port 0. show port xstats 0 The following is an example of an interactive session with the DPDK example application.
[root@ip-192.0.2.0 build]# ./app/dpdk-testpmd -- -i EAL: Detected 4 lcore(s)
        EAL: Detected 1 NUMA nodes EAL: Multi-process socket /var/run/dpdk/rte/mp_socket

        EAL: Selected IOVA mode 'PA'
        EAL: Probing VFIO support...
        EAL:   Invalid NUMA socket, default to 0 EAL:   Invalid NUMA socket, default to 0 EAL: Probe PCI driver: net_ena (1d0f:ec20) device: 0000:00:06.0 (socket 0)
        EAL: No legacy callbacks, legacy socket not created Interactive-mode selected

        Port 0: link state change event testpmd: create a new mbuf pool <mb_pool_0>: n=171456, size=2176, socket=0 testpmd: preferred mempool ops selected: ring_mp_mc

        Warning! port-topology=paired and odd forward ports number, the last port will pair with itself.

        Configuring Port 0 (socket 0)
        Port 0: 02:C7:17:A2:60:B1 Checking link statuses...
        Done Error during enabling promiscuous mode for port 0: Operation not supported - ignore testpmd> show port xstats 0
        ###### NIC extended statistics for port 0 rx_good_packets: 0 tx_good_packets: 0 rx_good_bytes: 0 tx_good_bytes: 0 rx_missed_errors: 0 rx_errors: 0 tx_errors: 0 rx_mbuf_allocation_errors: 0 rx_q0_packets: 0 rx_q0_bytes: 0 rx_q0_errors: 0 tx_q0_packets: 0 tx_q0_bytes: 0 wd_expired: 0 dev_start: 1 dev_stop: 0 tx_drops: 0 bw_in_allowance_exceeded: 0 bw_out_allowance_exceeded: 0

        pps_allowance_exceeded: 0 conntrack_allowance_exceeded: 0 linklocal_allowance_exceeded: 0 rx_q0_cnt: 0 rx_q0_bytes: 0 rx_q0_refill_partial: 0 rx_q0_bad_csum: 0 rx_q0_mbuf_alloc_fail: 0 rx_q0_bad_desc_num: 0 rx_q0_bad_req_id: 0 tx_q0_cnt: 0 tx_q0_bytes: 0 tx_q0_prepare_ctx_err: 0 tx_q0_linearize: 0 tx_q0_linearize_failed: 0 tx_q0_tx_poll: 0 tx_q0_doorbells: 0 tx_q0_bad_req_id: 0 tx_q0_available_desc: 1023 testpmd>
For more information about the example application and using it to retrieve extended statistics. see Testpmd Application User Guide in the DPDK documentation.
### Metrics on instances running FreeBSD Starting with version 2.3.0, the ENA FreeBSD driver supports collecting network performance metrics on instances running FreeBSD. To enable the collection of FreeBSD metrics, enter the following command and set interval to a value between 1 and 3600. This specifies how often, in seconds, to collect FreeBSD metrics. sysctl dev.ena.network_interface.eni_metrics.sample_interval=interval For example, the following command sets the driver to collect FreeBSD metrics on network interface 1 every 10 seconds: sysctl dev.ena.1.eni_metrics.sample_interval=10 To turn off the collection of FreeBSD metrics, you can run the preceding command and specify 0 as the interval.

After you enable collecting FreeBSD metrics, you can retrieve the latest set of collected metrics by running the following command. sysctl dev.ena.network_interface.eni_metrics
## Improve network latency for Linux based EC2 instances Network latency is the amount of time it takes for a packet of data to travel from its source to its destination. Applications that send data across the network depend on timely responses to provide a positive user experience. High network latency can lead to various issues, such as the following:
- Slow load times for web pages
- Video stream lag
- Difficulty accessing online resources This section outlines steps that you can take to improve the network latency on Amazon EC2 instances that run on Linux. To achieve optimal latency, follow these steps to configure your instance, kernel, and ENA driver settings. For additional configuration guidance, see the ENA Linux Driver Best Practices and Performance Optimization Guide on GitHub.
Note Steps and settings may vary slightly, depending on your specific network hardware, the AMI that you launched your instance from, and your application use case. Before you make any changes, thoroughly test and monitor your network performance to ensure that you're getting the desired results.
### Reduce the number of network hops for data packets Each hop that a data packet takes as it moves from router to router increases network latency.
Typically, traffic must take multiple hops to reach your destination. There are two ways to reduce network hops for your Amazon EC2 instances, as follows:
- Cluster placement group – When you specify a cluster placement group, Amazon EC2 launches instances that are in close proximity to each other, physically within the same Availability Zone (AZ) with tighter packing. The physical proximity of the instances in the group allows them

to take advantage of high-speed connectivity, resulting in low latency and high single flow throughput.
- Dedicated Host – A Dedicated Host is a physical server that's dedicated for your use.
With a Dedicated Host, you can launch your instances to run on the same physical server.
Communication between instances that run on the same Dedicated Host can happen without extra network hops.
### How Linux kernel configuration affects latency Linux kernel configuration can increase or decrease network latency. To achieve your latency optimization goals, it's important to fine-tune the Linux kernel configuration according to the specific requirements of your workload.
There are many configuration options for the Linux kernel that might help decrease network latency. The most impactful options are as follows.
- Enable busy poll mode – Busy poll mode reduces latency on the network receive path. When you enable busy poll mode, the socket layer code can directly poll the receive queue of a network device. The downside of busy polling is higher CPU usage in the host that comes from polling for new data in a tight loop. There are two global settings that control the number of microseconds to wait for packets for all interfaces.

busy_read A low latency busy poll timeout for socket reads. This controls the number of microseconds to wait for the socket layer to read packets on the device queue. To enable the feature globally with the sysctl command, the Linux Kernel organization recommends a value of 50 microseconds. For more information, see busy_read in the Linux kernel user's and administrator's guide.
[ec2-user ~]$ sudo sysctl -w net.core.busy_read=50 busy_poll A low latency busy poll timeout for poll and select. This controls the number of microseconds to wait for events. The recommended value is between 50-100 microseconds, depending

on the number of sockets you're polling. The more sockets you add, the higher the number should be.
[ec2-user ~]$ sudo sysctl -w net.core.busy_poll=50
- Configure CPU power states (C-states) – C-states control the sleep levels that a core may enter when it's inactive. You might want to control C-states to tune your system for latency versus performance. In deeper C-states, the CPU is essentially "asleep" and can't respond to requests until it wakes up and transitions back to an active state. Putting cores to sleep takes time, and although a sleeping core allows more headroom for another core to boost to a higher frequency, it takes time for that sleeping core to wake back up and perform work.
For example, if a core that's assigned to handle network packet interrupts is asleep, there might be a delay in servicing that interrupt. You can configure the system so that it doesn't use deeper C-states. However, while this configuration reduces the processor reaction latency, it also reduces the headroom available to other cores for Turbo Boost.
To reduce the processor reaction latency, you can limit deeper C-states. For more information, see High performance and low latency by limiting deeper C-states in the Amazon Linux 2 User Guide.
### Interrupt moderation The ENA network driver enables communication between an instance and a network. The driver processes network packets and passes them on to the network stack or to the Nitro card. When a network packet comes in, the Nitro card generates an interrupt for the CPU to notify the software of an event.
Interrupt An interrupt is a signal that a device or application sends to the processor. The interrupt tells the processor that an event has occurred or a condition has been met that requires immediate attention. Interrupts can handle time-sensitive tasks such as receiving data from a network interface, handling hardware events, or servicing requests from other devices.
Interrupt moderation Interrupt moderation is a technique that reduces the number of interrupts a device generates by aggregating or delaying them. The purpose of interrupt moderation is to improve system performance by reducing the overhead associated with handling a large number of interrupts.

Too many interrupts increase CPU usage, impacting the throughput adversely, while too few interrupts increase the latency.
Dynamic interrupt moderation Dynamic interrupt moderation is an enhanced form of interrupt moderation that dynamically adjusts the interrupt rate based on the current system load and traffic patterns. It aims to strike a balance between reducing interrupt overhead and packets per second, or bandwidth.
Note Dynamic interrupt moderation is enabled by default in some AMIs (but can be enabled or disabled in all AMIs).
To minimize network latency, it might be necessary to disable interrupt moderation. However, this can also increase the overhead of interrupt processing. It's important to find the right balance between reducing latency and minimizing overhead. ethtool commands can help you configure interrupt moderation. By default, rx-usecs is set to 20, and tx-usecs is set to 64.
To get the current interrupt modification configuration, use the following command.
[ec2-user ~]$ ethtool -c interface | egrep "rx-usecs:|tx-usecs:|Adaptive RX"
Adaptive RX: on  TX: off rx-usecs: 20 tx-usecs: 64 To disable interrupt modification and dynamic interrupt moderation, use the following command.
[ec2-user ~]$ sudo ethtool -C interface adaptive-rx off rx-usecs 0 tx-usecs 0
## Nitro system considerations for performance tuning The Nitro System is a collection of hardware and software components built by AWS that enable high performance, high availability, and high security. The Nitro System provides bare metal-like capabilities that eliminate virtualization overhead and support workloads that require full access to host hardware. For more detailed information, see AWS Nitro System.
All current generation EC2 instance types perform network packet processing on EC2 Nitro Cards. This topic covers high level packet handling on the Nitro card, common aspects of network

architecture and configuration that impact packet handling performance, and what actions you can take to achieve peak performance for your Nitro based instances.
Nitro Cards handle all input and output (I/O) interfaces, such as those needed for Virtual Private Clouds (VPCs). For all of the components that send or receive information over the network, the Nitro cards act as a self-contained computing device for I/O traffic that's physically separate from the system main board on which customer workloads run.
### Network packet flow on Nitro cards EC2 instances built on the Nitro system have hardware acceleration capabilities that enable faster packet processing, as measured by packets per second (PPS) throughput rates. When a Nitro card performs the initial evaluation for a new flow, it saves information that's the same for all packets in the flow, such as security groups, access control lists, and route table entries. When it processes additional packets for the same flow, it can use the saved information to reduce overhead for those packets.
Your connection rate is measured by the connections per second (CPS) metric. Each new connection requires additional processing overhead that must be factored into workload capability estimates.
It's important to consider both the CPS and PPS metrics when you design your workloads.
How a connection is established When a connection is established between a Nitro based instance and another endpoint, the Nitro card evaluates the full flow for the first packet that's sent or received between the two endpoints.
For subsequent packets of the same flow, full reevaluation is usually not necessary. However, there are exceptions. For more information about the exceptions, see Packets that don't use hardware acceleration.
The following properties define the two endpoints and the packet flow between them. These five properties together are known as a 5-tuple flow.
- Source IP
- Source port
- Destination IP
- Destination port
- Communication protocol

The direction of the packet flow is known as ingress (inbound) and egress (outbound). The following high level descriptions summarize end to end network packet flow.
- Ingress – When a Nitro card handles an inbound network packet, it evaluates the packet against stateful firewall rules and access control lists. It tracks the connection, meters it, and performs other actions as applicable. Then it forwards the packet to its destination on the host CPU.
- Egress – When a Nitro card handles an outbound network packet, it looks up the remote interface destination, evaluates various VPC functions, applies rate limits, and performs other actions that apply. Then it forwards the packet to its next hop destination on the network.
### Design your network for optimal performance To take advantage of your Nitro system's performance capabilities, you must understand what your network processing needs are and how those needs affect the workload for your Nitro resources.
Then you can design for optimal performance for your network landscape. Your infrastructure settings and application workload design and configuration can impact both the packet processing and connection rates. For example, if your application has a high rate of connection establishment, such as a DNS service, firewall, or virtual router, it will have less opportunity to take advantage of the hardware acceleration that only occurs after the connection is established.
You can configure application and infrastructure settings to streamline workloads and improve network performance. However, not all packets are eligible for acceleration. The Nitro system uses the full network flow for new connections and for packets that aren't eligible for acceleration.
The remainder of this section will focus on application and infrastructure design considerations to help ensure that packets flow within the accelerated path as much as possible.
#### Network design considerations for the Nitro system When you configure network traffic for your instance, there are many aspects to consider that can affect PPS performance. After a flow is established, the majority of packets that regularly come in or go out are eligible for acceleration. However, exceptions exist to ensure that infrastructure designs and packet flows continue to meet protocol standards.
To get the best performance from your Nitro card, you should carefully consider the pros and cons of the following configuration details for your infrastructure and applications.

##### Infrastructure considerations Your infrastructure configuration can affect your packet flow and processing efficiency. The following list includes some important considerations.
Network interface configuration with asymmetry Security groups use connection tracking to track information about traffic that flows to and from the instance. Asymmetric routing, where traffic comes into an instance through one network interface and leaves through a different network interface, can reduce the peak performance that an instance can achieve if flows are tracked. For more information about security group connection tracking, untracked connections, and automatically tracked connections, see Amazon EC2 security group connection tracking.
Network drivers Network drivers are updated and released on a regular basis. If your drivers are out of date, that can significantly impair performance. Keep your drivers up to date to ensure that you have the latest patches and can take advantage of performance improvements, such as the accelerated path feature that's only available for the latest generation of drivers. Earlier drivers don't support the accelerated path feature.
To take advantage of the accelerated path feature, we recommend that you install the latest ENA driver on your instances.
Linux instances – ENA Linux driver 2.2.9 or later. To install or update the ENA Linux driver from the Amazon Drivers GitHub repository, see the Driver compilation section of the readme file.
Windows instances – ENA Windows driver 2.0.0 or later. To install or update the ENA Windows driver, see Install the ENA driver on EC2 Windows instances.
Distance between endpoints A connection between two instances in the same Availability Zone can process more packets per second than a connection across Regions as a result of TCP windowing at the application layer, which determines how much data can be in flight at any given time. Long distances between instances increase latency and decrease the number of packets that the endpoints can process.
Byte queue limit (BQL)
BQL is a feature that limits the number of bytes passed to the Nitro card to reduce queuing.
BQL is disabled by default in ENA drivers, in Amazon Linux operating systems, and in most Linux distributions. If BQL and the fragment proxy override are both enabled, it can result in

performance limitations by restricting the number of bytes passed to Nitro before all fragments are processed.
##### Application design considerations There are aspects of application design and configuration that can affect your processing efficiency.
The following list includes some important considerations.
Packet size Larger packet sizes can increase throughput for the data that an instance can send and receive on the network. Amazon EC2 supports jumbo frames of 9001 bytes, however other services may enforce different limits. Smaller packet sizes can increase the packet process rate, but this can reduce the maximum achieved bandwidth when the number of packets exceed PPS allowances.
If the size of a packet exceeds the Maximum Transmission Unit (MTU) of a network hop, a router along the path might fragment it. The resulting packet fragments are considered exceptions, and are normally processed at the standard rate (not accelerated). This can cause variations in your performance. However, you can override the standard behavior for outbound fragmented packets with the fragment proxy mode setting. For more information, see Maximize network performance on your Nitro system. We recommended that you evaluate your topology when you configure MTU.
Protocol trade-offs Reliable protocols like TCP have more overhead than unreliable protocols like UDP. The lower overhead and simplified network processing for the UDP transport protocol can result in a higher PPS rate, but at the expense of reliable packet delivery. If reliable packet delivery isn't critical for your application, UDP might be a good option.
Micro-bursting Micro-bursting occurs when traffic exceeds allowances during brief periods of time rather than being evenly distributed. This typically happens on a microsecond scale.
For example, say that you have an instance that can send up to 10 Gbps, and your application sends the full 10 Gb in half a second. This micro-burst exceeds the allowance during the first half second and leaves nothing for the remainder of the second. Even though you sent 10Gb in the 1 second timeframe, allowances in the first half second can result in packets being queued or dropped.

You can use a network scheduler such as Linux Traffic Control to help pace your throughput and avoid causing queued or dropped packets as a result of micro-bursting.
Number of flows A single flow is limited to 5 Gbps unless it's inside of a cluster placement group that supports up to 10 Gbps, or if it uses ENA Express, which supports up to 25 Gbps.
Similarly, a Nitro card can process more packets across multiple flows as opposed to using a single flow. To achieve the peak packet processing rate per instance, we recommend at least 100 flows on instances with 100 Gbps or higher aggregate bandwidth. As aggregate bandwidth capabilities increase, the number of flows needed to achieve peak processing rates also increases. Benchmarking will help you determine what configuration you need to achieve peak rates on your network.
Elastic Network Adapter (ENA) queues ENA (Elastic Network Adapter) uses multiple receive (Rx) and transmit (Tx) queues (ENA queues) to improve network performance and scalability on EC2 instances. These queues efficiently manage network traffic by load-balancing sent and received data across available queues.
For more information, see the section called "ENA queues".
Feature process overhead Features like Traffic Mirroring and ENA Express can add more processing overhead, which can reduce absolute packet processing performance. You can limit feature use or disable features to increase packet processing rates.
Connection tracking to maintain state Your security groups use connection tracking to store information about traffic to and from the instance. Connection tracking applies rules against each individual flow of network traffic to determine if the traffic is allowed or denied. The Nitro card uses flow tracking to maintain state for the flow. As more security group rules are applied, more work is required to evaluate the flow.
Note Not all network traffic flows are tracked. If a security group rule is configured with Untracked connections, no additional work is required except for connections that are

automatically tracked to ensure symmetric routing when there are multiple valid reply paths.
##### Packets that don't use hardware acceleration Not all packets can take advantage of hardware acceleration. Handling these exceptions involves some processing overhead which is necessary to ensure the health of your network flows. Network flows must reliably meet protocol standards, conform to changes in the VPC design, and route packets only to allowed destinations. However, the overhead reduces your performance.
Packet fragments As mentioned under Application considerations, packet fragments that result from packets that exceed network MTU are normally handled as exceptions, and can't take advantage of hardware acceleration. However, you can bypass egress fragment limitations with the fragment proxy mode, depending on your driver version. For more information, see actions you can take in the Maximize network performance on your Nitro system section.
Idle connections When a connection has no activity for a while, even if the connection hasn't reached its timeout limit, the system can de-prioritize it. Then, if data comes in after the connection is de- prioritized, the system needs to handle it as an exception in order to reconnect.
To manage your connections, you can use connection tracking timeouts to close idle connections. You can also use TCP keepalives to keep idle connections open. For more information, see Idle connection tracking timeout.
VPC mutation Updates to security groups, route tables, and access control lists all need to be reevaluated in the processing path to ensure that route entries and security group rules still apply as expected.
ICMP flows Internet Control Message Protocol (ICMP) is a network layer protocol that network devices use to diagnose network communication issues. These packets always use the full flow.
Asymmetric L2 flows NitroV3 and earlier platforms do not use hardware acceleration for traffic between two ENIs in the same subnet where one ENI is using the default gateway router and the other

is not. NitroV4 and later platforms utilize hardware acceleration in this scenario. For better performance on NitroV3 or earlier platforms, ensure that either the default gateway router used matches between both ENIs, or those ENIs are in different subnets.
### Maximize network performance on your Nitro system You can maximize your network performance on Nitro system by adjusting network settings.
Topics
- Considerations
- Tune PPS performance
- Configure ENA queue allocation
- Monitor performance on Linux instances Considerations Before you make any design decisions or adjust any network settings on your instance, we recommend that you take the following steps to help ensure that you have the best outcome:
1. Understand the pros and cons of the actions that you can take to improve performance by reviewing Network design considerations for the Nitro system.
For more considerations and best practices for your instance configuration on Linux, see ENA Linux Driver Best Practices and Performance Optimization Guide on GitHub.
2. Benchmark your workloads with peak active flow count to determine a baseline for your application performance. With a performance baseline, you can test variations in your settings or application design to understand which considerations will have the most impact, especially if you plan to scale up or scale out.
#### Tune PPS performance The following list contains actions that you can take to tune your PPS performance, depending on your system needs.
- Reduce the physical distance between two instances. When sending and receiving instances are located in same Availability Zone or use cluster placement groups, you can reduce the number of hops a packet needs to take to travel from one endpoint to another.

- Use Untracked connections.
- Use the UDP protocol for network traffic.
- For EC2 instances with aggregate bandwidth of 100 Gbps or more, distribute the workload over 100 or more individual flows to spread the work evenly across the Nitro card.
- To overcome the egress fragment PPS limit on EC2 instances, you can enable fragment proxy mode (depending on your driver version). This setting allows fragmented packets to be evaluated in the processing path, thereby overcoming the egress PPS limit of 1024. When loading the driver, run one of the following commands to enable or disable fragment proxy mode:
Enable fragment proxy mode sudo insmod ena.ko enable_frag_bypass=1 Disable fragment proxy mode sudo insmod ena.ko enable_frag_bypass=0
#### Configure ENA queue allocation On supported instance types, you can dynamically allocate these queues across Elastic Network Interfaces (ENIs). Flexible ENA queue allocation optimizes resource distribution, enabling maximum vCPU utilization. High network performance workloads typically require multiple ENA queues. For more information, see ENA queues.
#### Monitor performance on Linux instances You can use Ethtool metrics on Linux instances to monitor instance networking performance indicators such as bandwidth, packet rate, and connection tracking. For more information, see Monitor network performance for ENA settings on your EC2 instance.
## Optimize network performance on EC2 Windows instances To achieve the maximum network performance on your Windows instances with enhanced networking, you might need to modify the default operating system configuration. We recommend the following configuration changes for applications that require high network performance. Other optimizations (such as turning on checksum offloading and enabling RSS, for example) are already configured on official Windows AMIs.

Note TCP chimney offloading should be disabled in most use cases, and has been deprecated as of Windows Server 2016.
In addition to these operating system optimizations, you should also consider the maximum transmission unit (MTU) of your network traffic, and adjust according to your workload and network architecture. For more information, see Network maximum transmission unit (MTU) for your EC2 instance.
AWS regularly measures average round trip latencies between instances launched in a cluster placement group of 50us and tail latencies of 200us at the 99.9 percentile. If your applications require consistently low latencies, we recommend using the latest version of the ENA drivers on fixed performance instances built on the Nitro System.
### Configure Receive side scaling CPU affinity Receive side scaling (RSS) is used to distribute network traffic CPU load across multiple processors.
By default, the official Amazon Windows AMIs are configured with RSS enabled. ENA elastic network interfaces provide up to eight RSS queues. By defining CPU affinity for RSS queues, as well as for other system processes, it is possible to spread the CPU load out over multi-core systems, enabling more network traffic to be processed. On instance types with more than 16 vCPUs, we recommend that you use the Set-NetAdapterRSS PowerShell cmdlet, which manually excludes the boot processor (logical processor 0 and 1 when hyper-threading is enabled) from the RSS configuration for all elastic network interfaces, in order to prevent contention with various system components.
Windows is hyper-thread aware and ensures that the RSS queues of a single network interface card (NIC) are always placed on different physical cores. Therefore, unless hyper-threading is disabled, in order to completely prevent contention with other NICs, spread the RSS configuration of each NIC among a range of 16 logical processors. The Set-NetAdapterRss cmdlet allows you to define the per-NIC range of valid logical processors by defining the values of BaseProcessorGroup, BaseProcessorNumber, MaxProcessingGroup, MaxProcessorNumber, and NumaNode (optional). If there are not enough physical cores to completely eliminate inter-NIC contention, minimize the overlapping ranges or reduce the number of logical processors in the elastic network interface ranges depending on the expected workload of the interface (in other words, a low volume administrative network interface may not need as many RSS queues assigned). Also, as previously
