# AMI types and characteristics in Amazon EC2

Source: apps/user-manuals/aws/ec2-ug.pdf

---

# AMI types and characteristics in Amazon EC2 When you launch an instance, the AMI that you choose must be compatible with the instance type that you choose. You can select an AMI to use based on the following characteristics:
- Region
- Operating system
- Processor architecture
- Launch permissions
- Root volume type
- Virtualization types
## Launch permissions Launch permissions determine who can use an AMI to launch instances. You can think of launch permissions as sharing an AMI—when you grant launch permissions, you're sharing the AMI with other users. Only the owner of an AMI can determine its availability by specifying launch permissions. Launch permissions fall into the following categories.
Launch permission Description public The owner grants launch permissions to all AWS accounts. explicit The owner grants launch permissions to specific AWS accounts, organizat ions,  or organizational units (OUs). implicit The owner has implicit launch permissions for an AMI.
Amazon and the Amazon EC2 community provide a large selection of public AMIs. For more information, see Understand shared AMI usage in Amazon EC2. Developers can charge for their AMIs. For more information, see Paid AMIs in the AWS Marketplace for Amazon EC2 instances.
## Root volume type All AMIs are categorized as either backed by Amazon EBS or backed by Amazon S3.

- Amazon EBS-backed AMI – The root volume for an instance launched from the AMI is an Amazon Elastic Block Store (Amazon EBS) volume created from an Amazon EBS snapshot. Supported for both Linux and Windows AMIs.
- Amazon S3-backed AMI – The root volume for an instance launched from the AMI is an instance store volume created from a template stored in Amazon S3. Supported for Linux AMIs only.
Windows AMIs do not support instance store for the root volume.
For more information, see Root volumes for your Amazon EC2 instances.
Note Amazon S3-backed AMIs are considered end of life and are not recommended for new usage. They are only supported on the following older instance types: C1, C3, D2, I2, M1, M2, M3, R3, and X1.
The following table summarizes the important differences when using the two types of AMIs.
Characteristic Amazon EBS-backed AMI Amazon S3-backed AMI Root volume EBS volume Instance store volume Boot time for an instance Usually less than 1 minute Usually less than 5 minutes Data persistence By default, the root volume is deleted when the instance terminates.* Data on any  other EBS volumes persists after instance termination by  default.
Data on any instance store volumes persists only during the life of the  instance.
Stopped state Can be in a stopped state. Even when the instance is stopped and not running, the root  volume is persisted in Amazon EBS.
Cannot be in a stopped state; instances are running or terminated.
Modifications

Characteristic Amazon EBS-backed AMI Amazon S3-backed AMI The instance type, kernel, RAM disk, and user data can be changed while the  instance is stopped.
Instance attributes are fixed for the life of an instance.
Charges You're charged for instance usage, EBS volume usage, and storing your AMI as an EBS  snaps hot.
You're charged for instance usage and storing your AMI in Amazon S3.
AMI creation/bundling Uses a single command/call Requires installation and use of AMI tools
* By default, EBS root volumes have the DeleteOnTermination flag set to true. For information about how to change this flag so that the volume persists after termination, see Keep an Amazon EBS root volume after an Amazon EC2 instance terminates.
** Supported with io2 EBS Block Express only. For more information, see Provisioned IOPS SSD Block Express volumes in the Amazon EBS User Guide.
## Identify the root volume type determined by your AMI The AMI that you use to launch an EC2 instance determines the type of the root volume. The root volume of an EC2 instance is either an EBS volume or an instance store volume.
Nitro-based instances support only EBS root volumes. The following previous generation instance types are the only instance types that support instance store root volumes: C1, C3, D2, I2, M1, M2, M3, R3, and X1.
Console To identify the root volume type determined by an AMI
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose AMIs, and select the AMI.
3. On the Details tab, check the value of Root device type as follows:

- ebs – Instances launched from this AMI will get an EBS root volume
- instance store – Instances launched from this AMI will get an instance store root volume.
AWS CLI To identify the root volume type determined by an AMI Use the describe-images command. aws ec2 describe-images \ --image-ids ami-0abcdef1234567890 \ --query Images[].RootDeviceType The following is example output. ebs PowerShell To identify the root volume type determined by an AMI Use the Get-EC2Image cmdlet.
(Get-EC2Image `
    -ImageId ami-0abcdef1234567890).RootDeviceType.Value The following is example output. ebs
## Virtualization types Amazon Machine Images use one of two types of virtualization: paravirtual (PV) or hardware virtual machine (HVM). The main differences between PV and HVM AMIs are the way in which they boot and whether they can take advantage of special hardware extensions (CPU, network, and storage) for better performance. Windows AMIs are HVM AMIs.
The following table compares HVM and PV AMIs.

Characteristic HVM PV Description HVM AMIs are presented with a fully virtualized set of hardware and boot by executing the master boot record of the root block device of your image. This virtualization type provides the ability to run an operating system directly on top of a virtual machine without any modification, as if it were run on the bare-metal hardware.
The Amazon EC2 host system emulates some or all of the underlying hardware that is presented to the guest.
PV AMIs boot with a special boot loader called PV- GRUB, which starts the boot cycle and then chain loads the kernel specified in the menu.lst file on your image.
Paravirtual guests can run on host hardware that does not have explicit support for virtualization. For more information about PV-GRUB and its use in Amazon EC2, see User provided kernels.
Supported instance types All current generation instance types support HVM AMIs.
The following previous generation instance types support PV AMIs: C1, C3, M1, M3, M2, and T1. Current generation instance types do not support PV AMIs.
Support for hardware extensions HVM guests can take advantage of hardware extensions that provide fast access to the underlyin g hardware on the host system. They are required to use enhanced networkin g and GPU processing. To pass through instructions to specialized network and GPU devices, the OS must have No, they can't take advantage of special hardware extension s such as enhanced networkin g or GPU processing.
