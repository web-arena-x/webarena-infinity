# Device names for volumes on Amazon EC2 instances

Source: apps/user-manuals/aws/ec2-ug.pdf

---

The following is example output.
Succeeded Alternatively, specify the instance-id filter to filter the results by instance.
PS C:\> Get-EC2ReplaceRootVolumeTask -Filters @{Name = 'instance-id'; Values = 'i-1234567890abcdef0'} | Format-Table
# Device names for volumes on Amazon EC2 instances When you attach a volume to your instance, you include a device name for the volume. This device name is used by Amazon EC2. The block device driver for the instance assigns the actual volume name when mounting the volume, and the name assigned can be different from the name that Amazon EC2 uses.
The number of volumes that your instance can support is determined by the operating system. For more information, see Amazon EBS volume limits for Amazon EC2 instances.
Contents
- Available device names
- Device name considerations
## Available device names
### Linux instances There are two types of virtualization available for Linux instances: paravirtual (PV) and hardware virtual machine (HVM). The virtualization type of an instance is determined by the AMI used to launch the instance. All instance types support HVM AMIs. Some previous generation instance types support PV AMIs. Be sure to note the virtualization type of your AMI because the recommended and available device names that you can use depend on the virtualization type of your instance. For more information, see Virtualization types.
The following table lists the available device names that you can specify in a block device mapping or when attaching an EBS volume.

Virtualization type Available Reserved for root volume Recommend ed for EBS data volumes Instance store volumes Paravirtual /dev/sd[a-z]
/dev/sd[a-z]
[1-15]
/dev/hd[a-z]
/dev/hd[a-z]
[1-15]
/dev/sda1 /dev/sd[f-p]
/dev/sd[f-p]
[1-6]
/dev/sd[b-e]
HVM /dev/sd[a-z]
/dev/xvd[a-c][a- z]
/dev/xvdd[a-x]
Differs by AMI /dev/sda1 or / dev/xvda /dev/sd[b-z]
/dev/xvdb[b-z]
* /dev/sd[b-e]
/dev/sd[b-h]
(h1.16xlarge)
/dev/sd[b-y]
(d2.8xlarge)
/dev/sd[b-i]
(i2.8xlarge)
**
* The device names that you specify for NVMe EBS volumes in a block device mapping are renamed using NVMe device names (/dev/nvme[0-26]n1). The block device driver can assign NVMe device names in a different order than you specified for the volumes in the block device mapping.
** NVMe instance store volumes are automatically enumerated and assigned an NVMe device name.
### Windows instances AWS Windows AMIs use one of the following sets of drivers to permit access to virtualized hardware:
- AWS PV: Paravirtual drivers for Windows instances
- AWS NVMe: AWS NVMe drivers

Device names for Nitro based instances The following table lists the available device names that you can specify in a block device mapping or when attaching an EBS volume to a Nitro based instance.
Driver type Available Reserved for root volume Recommended for EBS volumes Instance store volumes AWS NVMe xvd[a-z] xvd[a-c][a-z] xvdd[a-x]
/dev/sda1 /dev/sda1 xvd[b-z] xvdb[b-z]
*
* NVMe instance store volumes are automatically enumerated and are assigned a Windows drive letter.
Device names for Xen based instances The following table lists the available device names that you can specify in a block device mapping or when attaching an EBS volume to a Xen based instance.
Driver type Available Reserved for root volume Recommended for EBS volumes Instance store volumes AWS PV xvd[b-z] xvd[b-c][a-z]
/dev/sda1 /dev/sd[b-e]
/dev/sda1 xvd[f-z] xvdc[a-x] xvd[a-e]
Citrix PV (no longer supported) xvd[b-z] xvd[b-c][a-z]
/dev/sda1 /dev/sda1 xvd[f-z] xvdc[a-x] xvd[a-e]

Driver type Available Reserved for root volume Recommended for EBS volumes Instance store volumes /dev/sd[b-e]
Red Hat PV (no longer supported) xvd[a-z] xvd[b-c][a-z]
/dev/sda1 /dev/sd[b-e]
/dev/sda1 xvd[f-p] xvdc[a-x] xvd[a-e]
For more information about instance store volumes, see Instance store temporary block storage for EC2 instances. For more information about NVMe EBS volumes (Nitro-based instances), including how to identify the EBS device, see Amazon EBS and NVMe in the Amazon EBS User Guide.
## Device name considerations Keep the following in mind when selecting a device name:
- The ending portion of device names that you use shouldn't overlap as it can cause issues when you start your instance. For example, avoid using combinations such as /dev/xvdf and xvdf for volumes attached to the same instance.
- Although you can attach your EBS volumes using the device names used to attach instance store volumes, we strongly recommend that you don't because the behavior can be unpredictable.
- The number of NVMe instance store volumes for an instance depends on the size of the instance.
NVMe instance store volumes are automatically enumerated and assigned an NVMe device name (Linux instances) or a Windows drive letter (Windows instances).
- (Windows instances) AWS Windows AMIs come with additional software that prepares an instance when it first boots up. This is either the EC2Config service (Windows AMIs prior to Windows Server 2016) or EC2Launch (Windows Server 2016 and later). After the devices have been mapped to drives, they are initialized and mounted. The root drive is initialized and mounted as C:\. By default, when an EBS volume is attached to a Windows instance, it can show up as any drive letter on the instance. You can change the settings to set the drive letters of the volumes per your specifications. For instance store volumes, the default depends on the driver.
AWS PV drivers and Citrix PV drivers assign instance store volumes drive letters going from Z: to A:. Red Hat drivers assign instance store volumes drive letters going from D: to Z:. For more
