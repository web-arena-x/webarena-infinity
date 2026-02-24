# Instance store temporary block storage for EC2 instances

Source: apps/user-manuals/aws/ec2-ug.pdf

---

# Instance store temporary block storage for EC2 instances An instance store provides temporary block-level storage for your EC2 instance. This storage is provided by disks that are physically attached to the host computer. Instance store is ideal for temporary storage of information that changes frequently, such as buffers, caches, scratch data, and other temporary content. It can also be used to store temporary data that you replicate across a fleet of instances, such as a load-balanced pool of web servers.
An instance store consists of one or more instance store volumes exposed as block devices. The size of an instance store as well as the number of devices available varies by instance type and instance size. For example, not every instance type provides instance store volumes. For more information, see Instance store volume limits for EC2 instances.
The virtual devices for instance store volumes are given virtual device names in order from ephemeral0 to ephemeral23. For example, with an instance type that supports one instance store volume, the virtual device name of the one volume is ephemeral0. With an instance type that supports four instance store volumes, the virtual device names of the four volumes are as follows: ephemeral0, ephemeral1, ephemeral2 and ephemeral3.
Instance store pricing There is no additional charge to use the instance store volumes provided for your instance. Instance store volumes are included as part of the usage cost of the instance.

Contents
- Data persistence for Amazon EC2 instance store volumes
- Instance store volume limits for EC2 instances
- SSD instance store volumes for EC2 instances
- Add instance store volumes to an EC2 instance
- Enable instance store swap volume for M1 and C1 EC2 instances
- Initialize instance store volumes on EC2 instances
- Detailed performance statistics for Amazon EC2 instance store volumes
## Data persistence for Amazon EC2 instance store volumes Instance store volumes are attached only at instance launch. You can't attach instance store volumes after launch. You can't detach an instance store volume from one instance and attach it to a different instance.
An instance store volume exists only during the lifetime of the instance to which it is attached. You can't configure an instance store volume to persist beyond the lifetime of its associated instance.
The data on an instance store volume persists even if the instance is rebooted. However, the data does not persist if the instance is stopped, hibernated, or terminated. When the instance is stopped, hibernated, or terminated, every block of the instance store volume is cryptographically erased.
Therefore, do not rely on instance store volumes for valuable, long-term data. If you need to retain the data stored on an instance store volume beyond the lifetime of the instance, you need to manually copy that data to more persistent storage, such as an Amazon EBS volume, an Amazon S3 bucket, or an Amazon EFS file system.
There are some events that can result in your data not persisting throughout the lifetime of the instance. The following table indicates whether data on instance store volumes is persisted during specific events, for both virtualized and bare metal instances.
Event What happens to your data?
User-initiated instance lifecycle events The instance is rebooted The data persists

Event What happens to your data?
The instance is stopped The data does not persist The instance is hibernated The data does not persist The instance is terminated The data does not persist The instance type is changed The data does not persist * An EBS-backed AMI is created from the instance The data does not persist in the created AMI ** An Amazon S3-backed AMI is created from the instance (Linux instances)
The data persists in the AMI bundle uploaded to Amazon S3 *** User-initiated OS events A shutdown is initiated The data does not persist † A restart is initiated The data persists AWS scheduled events Instance stop The data does not persist Instance reboot The data persists System reboot The data persists Instance retirement The data does not persist Unplanned events Simplified automatic recovery The data does not persist CloudWatch action based recovery The data does not persist The underlying disk fails The data on the failed disk does not persist Power failure The data persists upon reboot

* If the new instance type supports instance store, the instance gets the number of instance store volumes supported by the new instance type, but the data does not transfer to the new instance. If the new instance type does not support instance store, the instance does not get the instance store volumes.
** The data is not included in the EBS-backed AMI, and it is not included on instance store volumes attached to instances launched from that AMI.
*** The data is included in the AMI bundle that is uploaded to Amazon S3. When you launch an instance from that AMI, the instance gets the instance store volumes bundled in the AMI with the data they contained at the time the AMI was created.
† Termination protection and stop protection do not protect instances against instance stops or terminations as a result of shutdowns initiated through the operating system on the instance. Data stored on instance store volumes does not persist in both instance stop and termination events.
## Instance store volume limits for EC2 instances The number, size, and type of instance store volumes are determined by the instance type. Some instance types, such as M6, C6, and R6, do not support instance store volumes, while other instance types, such as M5d, C6gd, and R6gd, do support instance store volumes. You can't attach more instance store volumes to an instance than is supported by its instance type. For the instance types that do support instance store volumes, the number and size of the instance store volumes vary by instance size. For example, m5d.large supports 1 x 75 GB instance store volume, while m5d.24xlarge supports 4 x 900 GB instance store volumes.
For instance types with NVMe instance store volumes, all of the supported instance store volumes are automatically attached to the instance at launch. For instance types with non-NVMe instance store volumes, such as C1, C3, M1, M2, M3, R3, D2, H1, I2, X1, and X1e, you must manually specify the block device mappings for the instance store volumes that you want to attach at launch. Then, after the instance has launched, you must  format and mount the attached instance store volumes before you can use them. You can't attach an instance store volume after you launch the instance.
Some instance types use NVMe or SATA-based solid state drives (SSD), while others use SATA- based hard disk drives (HDD). SSDs deliver high random I/O performance with very low latency, but you don't need the data to persist when the instance terminates or you can take advantage of fault-tolerant architectures. For more information, see SSD instance store volumes for EC2 instances.

The data on NVMe instance store volumes and some HDD instance store volumes is encrypted at rest. For more information, see Data protection in Amazon EC2.
### Available instance store volumes The Amazon EC2 Instance Types Guide provides the quantity, size, type, and performance optimizations of instance store volumes available on each supported instance type. For more information, see the following:
- Instance store specifications – General purpose
- Instance store specifications – Compute optimized
- Instance store specifications – Memory optimized
- Instance store specifications – Storage optimized
- Instance store specifications – Accelerated computing
- Instance store specifications – High-performance computing
- Instance store specifications – Previous generation Console To retrieve instance store volume information
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Instance Types.
3. Add the filter Local instance storage = true. The Storage column indicates the total size of the instance storage for the instance type.
4. (Optional) Click the Preferences icon and then turn on Storage disk count. This column indicates the number of instance store volumes.
5. (Optional) Add filters to further scope to specific instance types of interest.
AWS CLI To retrieve instance store volume information Use the describe-instance-types command. The following example displays the total size of the instance storage for each instance type in the R6i instance families with instance store volumes. aws ec2 describe-instance-types \

    --filters "Name=instance-type,Values=r6i*" "Name=instance-storage- supported,Values=true" \ --query "InstanceTypes[].[InstanceType, InstanceStorageInfo.TotalSizeInGB]" \ --output table The following is example output.
----------------------------
|  DescribeInstanceTypes   | +----------------+---------+
|  r6id.16xlarge  |  3800  |
|  r6idn.16xlarge |  3800  |
|  r6idn.8xlarge  |  1900  |
|  r6id.2xlarge   |  474   |
|  r6idn.xlarge   |  237   |
|  r6id.12xlarge  |  2850  |
|  r6idn.2xlarge  |  474   |
|  r6id.xlarge    |  237   |
|  r6idn.24xlarge |  5700  |
|  r6id.4xlarge   |  950   |
|  r6id.32xlarge  |  7600  |
|  r6id.24xlarge  |  5700  |
|  r6idn.large    |  118   |
|  r6idn.4xlarge  |  950   |
|  r6id.large     |  118   |
|  r6id.8xlarge   |  1900  |
|  r6idn.32xlarge |  7600  |
|  r6idn.metal    |  7600  |
|  r6id.metal     |  7600  |
|  r6idn.12xlarge |  2850  | +----------------+--------+ To get complete instance storage details for an instance type Use the describe-instance-types command. aws ec2 describe-instance-types \ --filters "Name=instance-type,Values=r6id.16xlarge" \ --query "InstanceTypes[].InstanceStorageInfo"
The example output shows that this instance type has two 1900 GB NVMe SSD volumes, for a total of 3800 GB of instance storage.

[ { "TotalSizeInGB": 3800, "Disks": [ { "SizeInGB": 1900, "Count": 2, "Type": "ssd"
            } ], "NvmeSupport": "required", "EncryptionSupport": "required"
    } ]
PowerShell To retrieve instance store volume information Use the Get-EC2InstanceType cmdlet. The following example displays the total size of the instance storage for each instance type in the R6i instance families with instance store volumes.
(Get-EC2InstanceType -Filter @{Name="instance-type"; Values="r6i*"},@{Name="instance-storage-supported"; Values="true"})
 | Format-Table @{Name="InstanceType";Expression={$_.InstanceType}}, @{Name="TotalSize";Expression={$_.InstanceStorageInfo.TotalSizeInGB}} The following is example output.
InstanceType   TotalSize ------------   --------- r6idn.16xlarge      3800 r6id.16xlarge       3800 r6id.xlarge          237 r6idn.8xlarge       1900 r6idn.2xlarge        474 r6id.12xlarge       2850 r6idn.xlarge         237 r6id.2xlarge         474 r6id.4xlarge         950 r6idn.24xlarge      5700 r6id.32xlarge       7600 r6id.24xlarge       5700

r6idn.large          118 r6id.large           118 r6idn.4xlarge        950 r6id.8xlarge        1900 r6id.metal          7600 r6idn.32xlarge      7600 r6idn.metal         7600 r6idn.12xlarge      2850 To get complete instance storage details for an instance type Use the Get-EC2InstanceType cmdlet. The output is converted to JSON format.
(Get-EC2InstanceType -Filter @{Name="instance-type"; Values="r6id.16xlarge"}).InstanceStorageInfo | ConvertTo-Json The example output shows that this instance type has two 1900 GB NVMe SSD volumes, for a total of 3800 GB of instance storage.
{ "Disks": [ { "Count": 2, "SizeInGB": 1900, "Type": "ssd"
    } ], "EncryptionSupport": { "Value": "required"
  }, "NvmeSupport": { "Value": "required"
  }, "TotalSizeInGB": 3800 }
## SSD instance store volumes for EC2 instances Like other instance store volumes, you must map the SSD instance store volumes for your instance when you launch it. The data on an SSD instance volume persists only for the life of its associated instance. For more information, see Add instance store volumes to an EC2 instance.

### NVMe SSD volumes Some instances offer non-volatile memory express (NVMe) solid state drives (SSD) instance store volumes. For more information about the type of instance store volume supported by each instance type, see Instance store volume limits for EC2 instances.
The data on NVMe instance storage is encrypted using an XTS-AES-256 block cipher implemented in a hardware module on the instance. The encryption keys are generated using the hardware module and are unique to each NVMe instance storage device. All encryption keys are destroyed when the instance is stopped or terminated and cannot be recovered. You cannot disable this encryption and you cannot provide your own encryption key.
#### Linux instances To access NVMe volumes, the NVMe drivers must be installed. The following AMIs meet this requirement:
- AL2023
- Amazon Linux 2
- Amazon Linux AMI 2018.03 and later
- Ubuntu 14.04 or later with linux-aws kernel Note AWS Graviton-based instance types require Ubuntu 18.04 or later with linux-aws kernel
- Red Hat Enterprise Linux 7.4 or later
- SUSE Linux Enterprise Server 12 SP2 or later
- CentOS 7.4.1708 or later
- FreeBSD 11.1 or later
- Debian GNU/Linux 9 or later
- Bottlerocket After you connect to your instance, you can list the NVMe devices using the lspci command. The following is example output for an i3.8xlarge instance, which supports four NVMe devices.

[ec2-user ~]$ lspci 00:00.0 Host bridge: Intel Corporation 440FX - 82441FX PMC [Natoma] (rev 02)
00:01.0 ISA bridge: Intel Corporation 82371SB PIIX3 ISA [Natoma/Triton II]
00:01.1 IDE interface: Intel Corporation 82371SB PIIX3 IDE [Natoma/Triton II]
00:01.3 Bridge: Intel Corporation 82371AB/EB/MB PIIX4 ACPI (rev 01)
00:02.0 VGA compatible controller: Cirrus Logic GD 5446 00:03.0 Ethernet controller: Device 1d0f:ec20 00:17.0 Non-Volatile memory controller: Device 1d0f:cd01 00:18.0 Non-Volatile memory controller: Device 1d0f:cd01 00:19.0 Non-Volatile memory controller: Device 1d0f:cd01 00:1a.0 Non-Volatile memory controller: Device 1d0f:cd01 00:1f.0 Unassigned class [ff80]: XenSource, Inc. Xen Platform Device (rev 01)
If you are using a supported operating system but you do not see the NVMe devices, verify that the NVMe module is loaded using the following command.
- Amazon Linux, Amazon Linux 2, Ubuntu 14/16, Red Hat Enterprise Linux, SUSE Linux Enterprise Server, CentOS 7 $ lsmod | grep nvme nvme          48813  0
- Ubuntu 18 $ cat /lib/modules/$(uname -r)/modules.builtin | grep nvme s/nvme/host/nvme-core.ko kernel/drivers/nvme/host/nvme.ko kernel/drivers/nvmem/nvmem_core.ko The NVMe volumes are compliant with the NVMe 1.0e specification. You can use the NVMe commands with your NVMe volumes. With Amazon Linux, you can install the nvme-cli package from the repo using the yum install command. With other supported versions of Linux, you can download the nvme-cli package if it's not available in the image.
#### Windows instances The latest AWS Windows AMIs for the following operating systems contain the AWS NVMe drivers used to interact with SSD instance store volumes that are exposed as NVMe block devices for better performance:

- Windows Server 2025
- Windows Server 2022
- Windows Server 2019
- Windows Server 2016
- Windows Server 2012 R2 After you connect to your instance, you can verify that you see the NVMe volumes in Disk Manager.
On the taskbar, open the context (right-click) menu for the Windows logo and choose Disk Management.
The AWS Windows AMIs provided by Amazon include the AWS NVMe driver. If you are not using the latest AWS Windows AMIs, you can install the current AWS NVMe driver.
### Non-NVMe SSD volumes The following instances support instance store volumes that use non-NVMe SSDs to deliver high random I/O performance: C3, I2, M3, R3, and X1. For more information about the instance store volumes supported by each instance type, see Instance store volume limits for EC2 instances.
### SSD-based instance store volume I/O performance As you fill the SSD-based instance store volumes for your instance, the number of write IOPS that you can achieve decreases. This is due to the extra work the SSD controller must do to find available space, rewrite existing data, and erase unused space so that it can be rewritten. This process of garbage collection results in internal write amplification to the SSD, expressed as the ratio of SSD write operations to user write operations. This decrease in performance is even larger if the write operations are not in multiples of 4,096 bytes or not aligned to a 4,096-byte boundary.
If you write a smaller amount of bytes or bytes that are not aligned, the SSD controller must read the surrounding data and store the result in a new location. This pattern results in significantly increased write amplification, increased latency, and dramatically reduced I/O performance.
SSD controllers can use several strategies to reduce the impact of write amplification. One such strategy is to reserve space in the SSD instance storage so that the controller can more efficiently manage the space available for write operations. This is called over-provisioning. The SSD-based instance store volumes provided to an instance do not have any space reserved for over-provisioning. To reduce write amplification, we recommend that you leave 10 percent of the volume unpartitioned so that the SSD controller can use it for over-provisioning. This decreases the storage that you can use, but increases performance even if the disk is close to full capacity.

For instance store volumes that support TRIM, you can use the TRIM command to notify the SSD controller whenever you no longer need data that you have written. This provides the controller with more free space, which can reduce write amplification and increase performance. For more information, see Instance store volume TRIM support.
### Instance store volume TRIM support Some instance types support SSD volumes with TRIM. For more information, see Instance store volume limits for EC2 instances.
Note (Windows instances only) Instances running Windows Server 2012 R2 support TRIM as of AWS PV Driver version 7.3.0. Instances running earlier versions of Windows Server do not support TRIM.
Instance store volumes that support TRIM are fully trimmed before they are allocated to your instance. These volumes are not formatted with a file system when an instance launches, so you must format them before they can be mounted and used. For faster access to these volumes, you should skip the TRIM operation when you format them.
(Windows instances) To temporarily disable TRIM support during initial formatting, use the fsutil behavior set DisableDeleteNotify 1 command. After formatting is complete, re-enable TRIM support by using fsutil behavior set DisableDeleteNotify 0.
With instance store volumes that support TRIM, you can use the TRIM command to notify the SSD controller when you no longer need data that you've written. This provides the controller with more free space, which can reduce write amplification and increase performance. On Linux instances, use the fstrim command to enable periodic TRIM. On Windows instances, use the fsutil behavior set DisableDeleteNotify 0 command to ensure TRIM support is enabled during normal operation.
## Add instance store volumes to an EC2 instance For instance types with NVMe instance store volumes, all of the supported instance store volumes are automatically attached to the instance at launch. They are automatically enumerated and assigned a device name on instance launch.

For instance types with non-NVMe instance store volumes, such as C1, C3, M1, M2, M3, R3, D2, H1, I2, X1, and X1e, you must manually specify the block device mappings for the instance store volumes that you want to attach at launch. Block device mappings can be specified in the instance launch request or in the AMI used to launch the instance. The block device mapping includes a device name and the volume that it maps to. For more information, see Block device mappings for volumes on Amazon EC2 instances Important Instance store volumes can be attached to an instance only when you launch it. You can't attach instance store volumes to an instance after you've launched it.
After you launch an instance, you must ensure that the instance store volumes for your instance are formatted and mounted before you can use them. The instance store root volume is mounted automatically.
Consideration for root volumes A block device mapping always specifies the root volume for the instance. The root volume is always mounted automatically.
Linux instances – The root volume is either an Amazon EBS volume or an instance store volume.
For instances with an instance store volume for the root volume, the size of this volume varies by AMI, but the maximum size is 10 GB. For more information, see Root volume type.
Windows instances – The root volume must be an Amazon EBS volume. Instance store is not supported for the root volume.
Contents
- Add instance store volumes to an Amazon EC2 AMI
- Add instance store volumes to an EC2 instance during launch
- Make instance store volume available for use on an EC2 instance
### Add instance store volumes to an Amazon EC2 AMI You can create an AMI with a block device mapping that includes instance store volumes.

If you launch an instance that supports non-NVMe instance store volumes using an AMI that specifies instance store volume block device mappings, the instance includes the instance store volumes. If the number of instance store volume block device mappings in the AMI exceeds the number of instance store volumes available to the instance, the additional instance store volume block device mappings are ignored.
If you launch an instance that supports NVMe instance store volumes using an AMI that specifies instance store volume block device mappings, the instance store volume block device mappings are ignored. Instances that support NVMe instance store volumes get all of their supported instance store volumes, regardless of the block device mappings specified in the instance launch request and the AMI. The device mapping of these volumes depends on the order in which the operating system enumerates the volumes.
Considerations
- The number of available instance store volumes depends on the instance type. For more information, see the section called "Available instance store volumes".
- You must specify a device name for each block device. For more information, see Device names for volumes on Amazon EC2 instances.
- When you launch an instance, you can omit non-NVMe instance store volumes specified in the AMI block device mapping or add instance store volumes.
- For M3 instances, specify instance store volumes in the block device mapping of the instance, not the AMI. Amazon EC2 might ignore instance store volume block device mappings in the AMI.
Console To add instance store volumes to an Amazon EBS-backed AMI
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Instances and select the instance.
3. Choose Actions, Image and templates, Create image.
4. On the Create image page, enter a meaningful name and description for your image.
5. For each instance store volume to add, choose Add volume, from Volume type select an instance store volume, and from Device select a device name.
6. Choose Create image.

AWS CLI To add instance store volumes to an AMI Use the create-image command with the --block-device-mappings option to specify a block device mapping for an EBS-backed AMI. Use the register-image command with the -- block-device-mappings option to specify a block device mapping for an iAmazon S3- backed AMI.
--block-device-mappings file://mapping.json The following block device mapping adds two instance store volumes.
[ { "DeviceName": "/dev/sdc", "VirtualName": "ephemeral0"
    }, { "DeviceName": "/dev/sdd", "VirtualName": "ephemeral1"
    } ]
PowerShell To add instance store volumes to an AMI Use the New-EC2Image cmdlet with the -BlockDeviceMapping parameter to specify a block device mapping for an EBS-backed AMI. Use the Register-EC2Image cmdlet with the - BlockDeviceMapping parameter to specify a block device mapping for an Amazon S3-backed AMI.
-BlockDeviceMapping $bdm The following block device mapping adds two instance store volumes.
$bdm = @()
$sdc = New-Object -TypeName Amazon.EC2.Model.BlockDeviceMapping $sdc.DeviceName = "/dev/sdc"

$sdc.VirtualName = "ephemeral0"
$bdm += $sdc $sdd = New-Object -TypeName Amazon.EC2.Model.BlockDeviceMapping $sdd.DeviceName = "/dev/sdd"
$sdd.VirtualName = "ephemeral1"
$bdm += $sdd
### Add instance store volumes to an EC2 instance during launch When you launch an instance type with non-NVMe instance store volumes, such as C1, C3, M1, M2, M3, R3, D2, H1, I2, X1, and X1e, you must specify the block device mappings for the instance store volumes that you want to attach at launch. The block device mappings must be specified in the instance launch request or in the AMI used to launch the instance.
If the AMI includes block device mappings for the instance store volumes, you do not need to specify block device mappings in the instance launch request, unless you need more instance store volumes than is included in the AMI.
If the AMI does not include block device mappings for instance store volumes, then you must specify the block device mappings in the instance launch request.
For instance types with NVMe instance store volumes, all of the supported instance store volumes are automatically attached to the instance at launch.
Considerations
- The number of available instance store volumes depends on the instance type. For more information, see the section called "Available instance store volumes".
- You must specify a device name for each block device. For more information, see Device names for volumes on Amazon EC2 instances.
- For M3 instances, you might receive instance store volumes even if you do not specify them in the block device mapping for the instance.
Console To specify a block device mapping in an instance launch request
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.

2. From the dashboard, choose Launch instance.
3. In the Application and OS Images section, select the AMI to use.
4. In the Configure storage section, the Instance store volumes section lists the instance store volumes that can be attached to the instance.
5. For each instance store volume to attach, for Device name, select the device name to use.
6. Configure the remaining instance settings as needed, and then choose Launch instance.
AWS CLI To specify a block device mapping in an instance launch request Use the run-instances command with the --block-device-mappings option.
--block-device-mappings file://mapping.json The following block device mapping adds two instance store volumes.
[ { "DeviceName": "/dev/sdc", "VirtualName": "ephemeral0"
    }, { "DeviceName": "/dev/sdd", "VirtualName": "ephemeral1"
    } ]
PowerShell To specify a block device mapping in an instance launch request Use the New-EC2Instance cmdlet with the -BlockDeviceMapping option.
-BlockDeviceMapping $bdm The following block device mapping adds two instance store volumes.
$bdm = @()

$sdc = New-Object -TypeName Amazon.EC2.Model.BlockDeviceMapping $sdc.DeviceName = "/dev/sdc"
$sdc.VirtualName = "ephemeral0"
$bdm += $sdc $sdd = New-Object -TypeName Amazon.EC2.Model.BlockDeviceMapping $sdd.DeviceName = "/dev/sdd"
$sdd.VirtualName = "ephemeral1"
$bdm += $sdd
### Make instance store volume available for use on an EC2 instance After you launch an instance with attached instance store volumes, you must mount the volumes before you can access them.
#### Linux instances You can format volumes with the file system of your choice after you launch your instance.
To make an instance store volume available on Linux
1. Connect to the instance using an SSH client. For more information, see Connect to your Linux instance using SSH.
2. Use the df -h command to view the volumes that are formatted and mounted.
$ df -h Filesystem      Size  Used Avail Use% Mounted on devtmpfs        3.8G   72K  3.8G   1% /dev tmpfs           3.8G     0  3.8G   0% /dev/shm /dev/nvme0n1p1  7.9G  1.2G  6.6G  15% /
3. Use the lsblk to view any volumes that were mapped at launch but not formatted and mounted.
$ lsblk NAME          MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT nvme0n1       259:1    0    8G  0 disk
##nvme0n1p1   259:2    0    8G  0 part /
##nvme0n1p128 259:3    0    1M  0 part nvme1n1       259:0    0 69.9G  0 disk

4. To format and mount an instance store volume that was mapped only, do the following: a.
Create a file system on the device using the mkfs command.
$ sudo mkfs -t xfs /dev/nvme1n1 b.
Create a directory on which to mount the device using the mkdir command.
$ sudo mkdir /data c.
Mount the device on the newly created directory using the mount command.
$ sudo mount /dev/nvme1n1 /data
#### Windows instances For Windows instances, we reformat the instance store volumes with the NTFS file system.
You can view the instance store volumes using Windows Disk Management. For more information, see List non-NVMe disks.
To manually mount an instance store volume
1. Choose Start, enter Computer Management, and then press Enter.
2. In left-hand panel, choose Disk Management.
3. If you are prompted to initialize the volume, choose the volume to initialize, select the required partition type depending on your use case, and then choose OK.
4. In the list of volumes, right-click the volume to mount, and then choose New Simple Volume.
5. On the wizard, choose Next.
6. On the Specify Volume Size screen, choose Next to use the maximum volume size.
Alternatively, choose a volume size that is between the minimum and maximum disk space.
7. On the Assign a Drive Letter or Path screen, do one of the following, and choose Next.
- To mount the volume with a drive letter, choose Assign the following drive letter and then choose the drive letter to use.
- To mount the volume as a folder, choose Mount in the following empty NTFS folder and then choose Browse to create or select the folder to use.

- To mount the volume without a drive letter or path, choose Do not assign a drive letter or drive path.
8. On the Format Partition screen, specify whether or not to format the volume. If you choose to format the volume, choose the required file system and unit size, and specify a volume label.
9. Choose Next, Finish.
## Enable instance store swap volume for M1 and C1 EC2 instances Note This topic applies to c1.medium and m1.small Linux instances only.
The c1.medium and m1.small instance types have a limited amount of physical memory.
Therefore, they are given a 900 MiB swap volume at launch time to act as virtual memory, or swap space, for the Linux system. Swap space in Linux can be used when a system requires more memory than it has been physically allocated. When swap space is enabled, Linux systems can swap infrequently used memory pages from physical memory to swap space (either a dedicated partition or a swap file in an existing file system) and free up that space for memory pages that require high-speed access.
Note
- Using swap space for memory paging is not as fast or efficient as using RAM. If your workload is regularly paging memory into swap space, you should consider migrating to a larger instance type with more RAM. For more information, see Amazon EC2 instance type changes.
- Although the Linux kernel sees this swap space as a partition on the root volume, it is actually a separate instance store volume, regardless of your root volume type.
Amazon Linux automatically enables and uses this swap space, but your AMI may require some additional steps to recognize and use this swap space. To see if your instance is using swap space, you can use the swapon -s command.
[ec2-user ~]$ swapon -s

Filename                                Type            Size    Used    Priority /dev/xvda3                              partition       917500  0       -1 The above instance has a 900 MiB swap volume attached and enabled. If you don't see a swap volume listed with this command, you may need to enable swap space for the device. Check your available disks using the lsblk command.
[ec2-user ~]$ lsblk NAME  MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT xvda1 202:1    0    8G  0 disk / xvda3 202:3    0  896M  0 disk Here, the swap volume xvda3 is available to the instance, but it is not enabled (notice that the MOUNTPOINT field is empty). You can enable the swap volume with the swapon command.
Note You must prepend /dev/ to the device name listed by lsblk. Your device may be named differently, such as sda3, sde3, or xvde3. Use the device name for your system in the command below.
[ec2-user ~]$ sudo swapon /dev/xvda3 Now the swap space should show up in lsblk and swapon -s output.
[ec2-user ~]$ lsblk NAME  MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT xvda1 202:1    0    8G  0 disk / xvda3 202:3    0  896M  0 disk [SWAP]
[ec2-user ~]$ swapon -s Filename                                Type            Size    Used    Priority /dev/xvda3                              partition       917500  0       -1 You also need to edit your /etc/fstab file so that this swap space is automatically enabled at every system boot.
[ec2-user ~]$ sudo vim /etc/fstab

Append the following line to your /etc/fstab file (using the swap device name for your system):
/dev/xvda3       none    swap    sw  0       0 To use an instance store volume as swap space Any instance store volume can be used as swap space. For example, the m3.medium instance type includes a 4 GB SSD instance store volume that is appropriate for swap space. If your instance store volume is much larger (for example, 350 GB), you may consider partitioning the volume with a smaller swap partition of 4-8 GB and the rest for a data volume.
Note This procedure applies only to instance types that support instance storage. For a list of supported instance types, see Instance store volume limits for EC2 instances.
1. List the block devices attached to your instance to get the device name for your instance store volume.
[ec2-user ~]$ lsblk -p NAME       MAJ:MIN RM SIZE RO TYPE MOUNTPOINT /dev/xvdb  202:16   0   4G  0 disk /media/ephemeral0 /dev/xvda1 202:1    0   8G  0 disk / In this example, the instance store volume is /dev/xvdb. Because this is an Amazon Linux instance, the instance store volume is formatted and mounted at /media/ephemeral0; not all Linux operating systems do this automatically.
2. (Optional) If your instance store volume is mounted (it lists a MOUNTPOINT in the lsblk command output), unmount it with the following command.
[ec2-user ~]$ sudo umount /dev/xvdb
3. Set up a Linux swap area on the device with the mkswap command.
[ec2-user ~]$ sudo mkswap /dev/xvdb mkswap: /dev/xvdb: warning: wiping old ext3 signature.
Setting up swapspace version 1, size = 4188668 KiB no label, UUID=b4f63d28-67ed-46f0-b5e5-6928319e620b

4. Enable the new swap space.
[ec2-user ~]$ sudo swapon /dev/xvdb
5. Verify that the new swap space is being used.
[ec2-user ~]$ swapon -s Filename    Type  Size Used Priority /dev/xvdb                               partition 4188668 0 -1
6. Edit your /etc/fstab file so that this swap space is automatically enabled at every system boot.
[ec2-user ~]$ sudo vim /etc/fstab If your /etc/fstab file has an entry for /dev/xvdb (or /dev/sdb) change it to match the line below; if it does not have an entry for this device, append the following line to your /etc/ fstab file (using the swap device name for your system):
/dev/xvdb       none    swap    sw  0       0 Important Instance store volume data is lost when an instance is stopped or hibernated; this includes the instance store swap space formatting created in Step 3. If you stop and restart an instance that has been configured to use instance store swap space, you must repeat Step 1 through Step 5 on the new instance store volume.
## Initialize instance store volumes on EC2 instances Because of the way that Amazon EC2 virtualizes disks, the first write to any location on some instance store volumes performs more slowly than subsequent writes. For most applications, amortizing this cost over the lifetime of the instance is acceptable. However, if you require high disk performance, we recommend that you initialize your drives by writing once to every drive location before production use.

Note Instance types with direct-attached solid state drives (SSD) and TRIM support provide maximum performance at launch time, without initialization. For information about the instance store for each instance type, see Instance store volume limits for EC2 instances.
If you require greater flexibility in latency or throughput, we recommend using Amazon EBS.
To initialize the instance store volumes, use the following dd commands, depending on the store to initialize (for example, /dev/sdb or /dev/nvme1n1).
Note Make sure to unmount the drive before performing this command.
Initialization can take a long time (about 8 hours for an extra large instance).
To initialize the instance store volumes, use the following commands on the m1.large, m1.xlarge, c1.xlarge, m2.xlarge, m2.2xlarge, and m2.4xlarge instance types: dd if=/dev/zero of=/dev/sdb bs=1M dd if=/dev/zero of=/dev/sdc bs=1M dd if=/dev/zero of=/dev/sdd bs=1M dd if=/dev/zero of=/dev/sde bs=1M To perform initialization on all instance store volumes at the same time, use the following command: dd if=/dev/zero bs=1M|tee /dev/sdb|tee /dev/sdc|tee /dev/sde > /dev/sdd Configuring drives for RAID initializes them by writing to every drive location. When configuring software-based RAID, make sure to change the minimum reconstruction speed: echo $((30*1024)) > /proc/sys/dev/raid/speed_limit_min

## Detailed performance statistics for Amazon EC2 instance store volumes Amazon EC2 provides real-time, high-resolution performance statistics for NVMe instance store volumes attached to Nitro-based Amazon EC2 instances. These statistics are presented as aggregated counters that are retained for the duration of the instance's lifetime. The statistics provide details about the cumulative number of operations, bytes sent and received, time spent on read and write I/O operations, and histograms for read and write I/O operations. While these statistics maintain consistency with Amazon EBS detailed performance statistics, they also include detailed latency histograms broken down by I/O size, which can provide more granular insights into your storage performance patterns. This enhanced visibility enables you to precisely identify which specific I/O sizes are experiencing latency issues, allowing you to optimize application performance and troubleshoot issues more effectively.
You can collect these statistics at a granularity of up to 1 second intervals. If requests are made more frequently than 1 second intervals, the NVMe driver might queue the requests, along with other admin commands, to be processed at a later time.
Considerations
- The statistics are supported only for NVMe instance store volumes attached to Nitro-based instances.
- The counters are not persistent across instance stops and restarts.
- The statistics are available at no additional cost.
### Statistics The NVMe block device vends the following statistics:
Statistic name Full name Type Description total_rea d_ops Total read operations Counter The total number of completed read operation s. total_wri te_ops Total write operation s Counter The total number of completed write operations.

Statistic name Full name Type Description total_rea d_bytes Total read bytes Counter The total number of read bytes transferred. total_wri te_bytes Total write bytes Counter The total number of write bytes transferred. total_rea d_time Total read time Counter The total time spent, in microseconds, by all completed read operations. total_wri te_time Total write time Counter The total time spent, in microseconds, by all completed write operations. instance_ store_vol ume_perfo rmance_ex ceeded_io ps Total time demand exceeded volume's maximum IOPS Counter The total time, in microseconds, that IOPS requests exceeded the volume's maximum IOPS. Any value above 0 indicates that your workload demanded more IOPS than the volume could deliver. Ideally, the increment al count of this metric, between two snapshot times, should be minimal. instance_ store_vol ume_perfo rmance_ex ceeded_tp Total time demand exceeded volume's maximum throughpu t Counter The total time, in microseconds, that throughput requests exceeded the volume's maximum throughput. Any value above 0 indicates that your workload demanded more throughput than the volume could deliver.
Ideally, the incremental count of this metric, between two snapshot times, should be minimal. volume_qu eue_lengt h Volume queue length Point in time The number of read and write operations waiting to be completed.

Statistic name Full name Type Description read_io_l atency_hi stogram Read I/O histogram Histogram * The number of read operations completed within each latency bin, in microseconds. write_io_ latency_h istogram Write I/O histogram Histogram * The number of write operations completed within each latency bin, in microseconds.
Note
* Histogram statistics represent only I/O operations that have completed successfully.
Stalled or impaired I/O operations are not included, but will be evident in the volume_queue_length statistics, which is presented as a point-in-time statistic.
### Accessing the statistics The statistics must be accessed directly from the instance to which the instance store volumes is attached. You can access the statistics using one of the following methods.
#### Linux instances Amazon CloudWatch You can configure the Amazon CloudWatch agent to collect the statistics from your instance and make them available as custom metrics in CloudWatch. You can then use the metrics in CloudWatch to analyze I/O patterns, track performance trends, create custom dashboards, and set up automated alarms based on performance thresholds.
For more information about configuring the CloudWatch agent, see  Collect Amazon EC2 instance store volume metrics. nvme-cli tool To access the statistics
1. Connect to the instance to which the volume is attached.

2. Amazon Linux 2023 AMIs released after September 15, 2025 include the latest version of the nvme-cli tool. If you are using an older Amazon Linux AMI, update the nvme-cli tool. sudo yum install nvme-cli
3. Run the following command and specify the device name for the volume. sudo nvme amzn stats /dev/nvme0n1 The statistics also provide detailed latency histograms broken down by I/O size. To view statistics broken down by I/O size, include the --details option. For example: sudo nvme amzn stats --details /dev/nvme0n1 You can get more information about how to use the tool by specifying the --help option. For example: sudo nvme amzn stats --help
#### Windows instances nvme_amzn.exe tool To access the statistics
1. Connect to the instance to which the volume is attached.
2. Make sure that you're using AWSNVMe driver version 1.7.0 or later. For more information about updating the AWSNVMe driver, see AWS NVMe drivers.
3. Get the disk number for the volume. For more information, see Map NVMe disks on Amazon EC2 Windows instance to volumes.
4. Run the following command as Administrator and specify the disk number for the volume.
.\nvme_amzn.exe stats disk_number
