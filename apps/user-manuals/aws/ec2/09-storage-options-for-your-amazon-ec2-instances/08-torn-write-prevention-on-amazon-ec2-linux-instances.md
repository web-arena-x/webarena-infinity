# Torn write prevention on Amazon EC2 Linux instances

Source: apps/user-manuals/aws/ec2-ug.pdf

---

Location Device name Bus Number 0, Target ID 20, LUN 0 xvdu Bus Number 0, Target ID 21, LUN 0 xvdv Bus Number 0, Target ID 22, LUN 0 xvdw Bus Number 0, Target ID 23, LUN 0 xvdx Bus Number 0, Target ID 24, LUN 0 xvdy Bus Number 0, Target ID 25, LUN 0 xvdz
# Torn write prevention on Amazon EC2 Linux instances Note Torn write prevention is supported with Linux instances only.
Torn write prevention is a block storage feature designed by AWS to improve the performance of your I/O-intensive relational database workloads and reduce latency without negatively impacting data resiliency. Relational databases that use InnoDB or XtraDB as the database engine, such as MySQL and MariaDB, will benefit from torn write prevention.
Typically, relational databases that use pages larger than the power fail atomicity of the storage device use data logging mechanisms to protect against torn writes. MariaDB and MySQL use a doublewrite buffer file to log data before writing it to data tables. In the event of incomplete or torn writes, as a result of operating system crashes or power loss during write transactions, the database can recover the data from the doublewrite buffer. The additional I/O overhead associated with writing to the doublewrite buffer impacts database performance and application latency, and it reduces the number transactions that can be processed per second. For more information about doublewrite buffer, see the  MariaDB and  MySQL documentation.
With torn write prevention, data is written to storage in all-or-nothing write transactions, which eliminates the need for using the doublewrite buffer. This prevents partial, or torn, data from being written to storage in the event of operating system crashes or power loss during write transactions.

The number of transactions processed per second can be increased by up to 30 percent, and write latency can be decreased by up to 50 percent, without compromising the resiliency of your workloads.
Pricing There are no additional costs for using torn write prevention.
Contents
- Block sizes for torn write prevention on Amazon EC2
- Requirements for using torn write prevention on Amazon EC2
- Check Amazon EC2 instance support for torn write prevention
- Configure your workload on Amazon EC2 for torn write prevention
## Block sizes for torn write prevention on Amazon EC2 Torn write prevention supports write operations for 4 KiB, 8 KiB, and 16 KiB blocks of data. The data block start logical block address (LBA) must be aligned to the respective block boundary size of 4 KiB, 8 KiB, or 16 KiB. For example, for 16 KiB write operations, the data block start LBA must be aligned to a block boundary size of 16 KiB.
The following table shows support across storage and instance types.

4 KiB blocks 8 KiB blocks 16 KiB blocks Instance store volumes All NVMe instance store volumes attached to current generation I- family instances.
I4i, Im4gn, Is4gen, I7i, I7ie, I8g, and I8ge instances supported by AWS Nitro SSD.
Amazon EBS volumes All Amazon EBS volumes attached to Nitro-based instances.
To confirm whether your instance and volume support torn write prevention, query to check if the instance supports torn write prevention and other details, like supported block and boundary sizes.
For more information, see Check Amazon EC2 instance support for torn write prevention.

## Requirements for using torn write prevention on Amazon EC2 For torn write prevention to work properly, an I/O operation must meet size, alignment, and boundary requirements, as specified in the NTWPU, NTWGU, NTWBU fields. You must configure your operating system to ensure that the specific storage subsystem (file system, LVM, RAID, etc) does not modify I/O properties down the storage stack, including block merges, splits, or block address relocation, before being submitted to the device.
Torn write prevent has been tested with the following configuration:
- An instance type and storage type that supports the required block size.
- Amazon Linux 2 with kernel version 5.10 or later.
- ext4 with bigalloc enabled and a cluster size of 16 KiB, and the most recent ext4 utilities (e2fsprogs 1.46.5 or later).
- O_DIRECT file access mode to bypass Linux kernel buffer cache.
Note You do not need to disable I/O merging for MySQL and MariaDB workloads.
## Check Amazon EC2 instance support for torn write prevention To confirm whether your instance and volume supports torn write prevention, and to view the NVMe namespace vendor specific data that contains torn write prevention information, use the following command.
$ sudo nvme id-ns -v device_name Note The command returns the vendor-specific information in hex with ASCII interpretation. You might need to build a tool, similar to ebsnvme-id, into your applications that can read and parse the output.

For example, the following command returns the NVMe namespace vendor specific data that contains torn write prevention information for /dev/nvme1n1.
$ sudo nvme id-ns -v /dev/nvme1n1 If your instance and volume support torn write prevention, it returns the following AWS torn write prevention information in the NVMe namespace vendor specific data.
Note The bytes in the following table represent the offset in bytes from the beginning of the NVMe namespace vendor specific data.
Bytes Description 0:31 The name of the device attachment mount point, for example /dev/ xvda . You provide this during volume attachment request and it can be used by the Amazon EC2 instance to create a symlink to the NVMe block device(nvmeXn1).
32:63 The volume ID. For example, vol01234567890abcdef . This field can be used to map the NVMe device to the attached volume.
64:255 Reserved for future use.
256:257 Namespace Torn Write Prevention Unit size (NTWPU). This field indicates the namespace specific size of the write operation guarantee d to be written atomically to the NVM during a power failure or error condition. This field is specified in logical blocks represented in zero based values.
258:259 Namespace Torn Write Prevention Granularity size (NTWPG). This field indicates the namespace specific size increments below NTWPU of the write operation guaranteed to be written atomically to the NVM during a power failure or error condition. That is, size should be NTWPG * n <= NTWPU where n is positive integer. The write operation LBA offset

Bytes Description also must be aligned to this field. This field is specified in logical blocks represented in zero based values.
260:263 Namespace Torn Write Prevention Boundary size (NTWPB). This field indicates the atomic boundary size for this namespace for the NTWPU value. Writes to this namespace that cross atomic boundaries are not guaranteed to be written atomically to the NVM during a power failure or error condition. A value of 0h indicates that there are no atomic boundaries for power fail or error conditions. All other values specify a size in terms of logical blocks using the same encoding as the NTWPU field.
## Configure your workload on Amazon EC2 for torn write prevention Torn write prevention is enabled by default on supported instance types with supported volumes.
You do not need to enabled any additional settings to enable your volume or instance for torn write prevention.
Note There is no performance impact on workloads that do not support torn write prevention.
You do not need to make any changes for these workloads.
Workloads that do support torn write prevention, but are not configured to use it, continue to use the doublewrite buffer and do not receive any performance benefits.
To configure your MySQL or MariaDB software stack to disable the doublewrite buffer and use torn write prevention, complete the following steps:
1. Configure your volume to use ext4 file system with the BigAlloc option and set the cluster size to 4 KiB, 8 KiB, or 16 KiB. Using BigAlloc with a cluster size of 4 KiB, 8 KiB, or 16 KiB ensures that the file system allocates files that align with the respective boundary.
$  mkfs.ext4 -O bigalloc -C 4096|8192|16384 device_name
