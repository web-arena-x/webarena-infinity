# Block device mappings for volumes on Amazon EC2 instances

Source: apps/user-manuals/aws/ec2-ug.pdf

---

information, see Windows launch agents on Amazon EC2 Windows instances, and How volumes are attached and mapped for Amazon EC2 Windows instances.
- (Linux instances) Depending on the block device driver of the kernel, the device could be attached with a different name than you specified. For example, if you specify a device name of /dev/sdh, your device could be renamed /dev/xvdh or /dev/hdh. In most cases, the trailing letter remains the same. In some versions of Red Hat Enterprise Linux (and its variants, such as CentOS), the trailing letter could change (/dev/sda could become /dev/xvde). In these cases, the trailing letter of each device name is incremented the same number of times. For example, if /dev/sdb is renamed /dev/xvdf, then /dev/sdc is renamed /dev/xvdg. Amazon Linux creates a symbolic link for the name you specified to the renamed device. Other operating systems could behave differently.
- (Linux instances) HVM AMIs do not support the use of trailing numbers on device names, except for /dev/sda1, which is reserved for the root volume, and /dev/sda2. While using /dev/sda2 is possible, we do not recommend using this device mapping with HVM instances.
- (Linux instances) When using PV AMIs, you cannot attach volumes that share the same device letters both with and without trailing digits. For example, if you attach a volume as /dev/sdc and another volume as /dev/sdc1, only /dev/sdc is visible to the instance. To use trailing digits in device names, you must use trailing digits on all device names that share the same base letters (such as /dev/sdc1, /dev/sdc2, /dev/sdc3).
- (Linux instances) Some custom kernels might have restrictions that limit use to /dev/sd[f- p] or /dev/sd[f-p][1-6]. If you're having trouble using /dev/sd[q-z] or /dev/sd[q-z]
[1-6], try switching to /dev/sd[f-p] or /dev/sd[f-p][1-6].
Before you specify the device name that you've selected, verify that it is available. Otherwise, you'll get an error that the device name is already in use. To view the disk devices and their mount points, use the lsblk command (Linux instances), or the Disk Management utility or the diskpart command (Windows instances).
# Block device mappings for volumes on Amazon EC2 instances Each instance that you launch has an associated root volume, which is either an Amazon EBS volume or an instance store volume. You can use block device mappings to specify additional EBS volumes or instance store volumes to attach to an instance when it's launched. You can also attach additional EBS volumes to a running instance. However, the only way to attach instance store

volumes to an instance is to use block device mappings to attach the volumes as the instance is launched.
Contents
- Block device mapping concepts
- Add block device mappings to an AMI
- Add block device mappings to Amazon EC2 instance
## Block device mapping concepts A block device is a storage device that moves data in sequences of bytes or bits (blocks). These devices support random access and generally use buffered I/O. Examples include hard disks, CD- ROM drives, and flash drives. A block device can be physically attached to a computer or accessed remotely as if it were physically attached to the computer.
Amazon EC2 supports two types of block devices:
- Instance store volumes (virtual devices whose underlying hardware is physically attached to the host computer for the instance)
- EBS volumes (remote storage devices)
A block device mapping defines the block devices (instance store volumes and EBS volumes) to attach to an instance. You can specify a block device mapping as part of creating an AMI so that the mapping is used by all instances launched from the AMI. Alternatively, you can specify a block device mapping when you launch an instance, so this mapping overrides the one specified in the AMI from which you launched the instance. Note that all NVMe instance store volumes supported by an instance type are automatically enumerated and assigned a device name on instance launch; including them in your block device mapping has no effect.
Contents
- Block device mapping entries
- Block device mapping instance store caveats
- Example block device mapping
- How devices are made available in the operating system

### Block device mapping entries When you create a block device mapping, you specify the following information for each block device that you need to attach to the instance:
- The device name used within Amazon EC2. The block device driver for the instance assigns the actual volume name when mounting the volume. The name assigned can be different from the name that Amazon EC2 recommends. For more information, see Device names for volumes on Amazon EC2 instances.
For Instance store volumes, you also specify the following information:
- The virtual device: ephemeral[0-23]. Note that the number and size of available instance store volumes for your instance varies by instance type.
For NVMe instance store volumes, the following information also applies:
- These volumes are automatically enumerated and assigned a device name; including them in your block device mapping has no effect.
For EBS volumes, you also specify the following information:
- The ID of the snapshot to use to create the block device (snap-xxxxxxxx). This value is optional as long as you specify a volume size. You can't specify the ID of an archived snapshot.
- The size of the volume, in GiB. The specified size must be greater than or equal to the size of the specified snapshot.
- Whether to delete the volume on instance termination (true or false). The default value is true for the root volume and false for attached volumes. When you create an AMI, its block device mapping inherits this setting from the instance. When you launch an instance, it inherits this setting from the AMI.
- The volume type, which can be gp2 and gp3 for General Purpose SSD, io1 and io2 for Provisioned IOPS SSD, st1 for Throughput Optimized HDD, sc1 for Cold HDD, or standard for Magnetic.
- The number of input/output operations per second (IOPS) that the volume supports. (Used only with io1 and io2 volumes.)

- Some instance types support more than one EBS card. You can select the EBS card for the volume to be attached to by specifying the EBS card index. For more information, see EBS cards.
### Block device mapping instance store caveats There are several caveats to consider when launching instances with AMIs that have instance store volumes in their block device mappings.
- Some instance types include more instance store volumes than others, and some instance types contain no instance store volumes at all. If your instance type supports one instance store volume, and your AMI has mappings for two instance store volumes, then the instance launches with one instance store volume.
- Instance store volumes can only be mapped at launch time. You cannot stop an instance without instance store volumes (such as the t2.micro), change the instance to a type that supports instance store volumes, and then restart the instance with instance store volumes. However, you can create an AMI from the instance and launch it on an instance type that supports instance store volumes, and map those instance store volumes to the instance.
- If you launch an instance with instance store volumes mapped, and then stop the instance and change it to an instance type with fewer instance store volumes and restart it, the instance store volume mappings from the initial launch still show up in the instance metadata. However, only the maximum number of supported instance store volumes for that instance type are available to the instance.
Note When an instance is stopped, all data on the instance store volumes is lost.
- Depending on instance store capacity at launch time, M3 instances may ignore AMI instance store block device mappings at launch unless they are specified at launch. You should specify instance store block device mappings at launch time, even if the AMI you are launching has the instance store volumes mapped in the AMI, to ensure that the instance store volumes are available when the instance launches.

### Example block device mapping This figure shows an example block device mapping for an EBS-backed instance. It maps /dev/sdb to ephemeral0 and maps two EBS volumes, one to /dev/sdh and the other to /dev/sdj. It also shows the EBS volume that is the root volume, /dev/sda1.
Note that this example block device mapping is used in the example commands and APIs in this topic. You can find example commands and APIs that create block device mappings in Specify a block device mapping for an AMI and Update the block device mapping when launching an instance.
### How devices are made available in the operating system Device names like /dev/sdh and xvdh are used by Amazon EC2 to describe block devices. The block device mapping is used by Amazon EC2 to specify the block devices to attach to an EC2 instance. After a block device is attached to an instance, it must be mounted by the operating system before you can access the storage device. When a block device is detached from an instance, it is unmounted by the operating system and you can no longer access the storage device.
Linux instances – The device names specified in the block device mapping are mapped to their corresponding block devices when the instance first boots. The instance type determines which instance store volumes are formatted and mounted by default. You can mount additional instance store volumes at launch, as long as you don't exceed the number of instance store volumes

available for your instance type. For more information, see Instance store temporary block storage for EC2 instances. The block device driver for the instance determines which devices are used when the volumes are formatted and mounted.
Windows instances – The device names specified in the block device mapping are mapped to their corresponding block devices when the instance first boots, and then the Ec2Config service initializes and mounts the drives. The root volume is mounted as C:\. The instance store volumes are mounted as Z:\, Y:\, and so on. When an EBS volume is mounted, it can be mounted using any available drive letter. However, you can configure how drive letters are assigned to EBS volumes; for more information, see the section called "Windows launch agents".
## Add block device mappings to an AMI Each AMI has a block device mapping that specifies the block devices to attach to an instance when it is launched from the AMI. To add more block devices to an AMI, you must create your own AMI.
Contents
- Specify a block device mapping for an AMI
- View the EBS volumes in an AMI block device mapping
### Specify a block device mapping for an AMI There are two ways to specify volumes in addition to the root volume when you create an AMI. If you've already attached volumes to a running instance before you create an AMI from the instance, the block device mapping for the AMI includes those same volumes. For EBS volumes, the existing data is saved to a new snapshot, and it's this new snapshot that's specified in the block device mapping. For instance store volumes, the data is not preserved.
For an EBS-backed AMI, you can add EBS volumes and instance store volumes using a block device mapping. For an Amazon S3-backed AMI, you can add instance store volumes only by modifying the block device mapping entries in the image manifest file when registering the image.
Note For M3 instances, you must specify instance store volumes in the block device mapping for the instance when you launch it. When you launch an M3 instance, instance store volumes specified in the block device mapping for the AMI may be ignored if they are not specified as part of the instance block device mapping.

Console To add volumes to an AMI
1. Open the Amazon EC2 console.
2. In the navigation pane, choose Instances.
3. Select an instance and choose Actions, Image and templates, Create image.
4. Enter a name and a description for the image.
5. The instance volumes appear under Instance volumes. To add another volume, choose Add volume.
6. For Volume type, choose the volume type. For Device choose the device name. For an EBS volume, you can specify additional details, such as a snapshot, volume size, volume type, IOPS, and encryption state.
7. Choose Create image.
AWS CLI To add volumes to an AMI Use the create-image command to specify a block device mapping for an EBS-backed AMI. Use the register-image command to specify a block device mapping for an Amazon S3-backed AMI.
Specify the block device mapping using the --block-device-mappings parameter. You can specified arguments encoded in JSON directly on the command line or by referencing a JSON file, as shown here.
--block-device-mappings file://mapping.json To add an instance store volume, use the following mapping. Note that NVMe instance store volumes are added automatically.
{ "DeviceName": "device_name", "VirtualName": "ephemeral0"
} To add an empty 100 GiB volume, use the following mapping.

{ "DeviceName": "device_name", "Ebs": { "VolumeSize": 100 } } To add an EBS volume based on a snapshot, use the following mapping.
{ "DeviceName": "device_name", "Ebs": { "SnapshotId": "snap-1234567890abcdef0"
    } } To omit a mapping for a device, use the following mapping.
{ "DeviceName": "device_name", "NoDevice": ""
} PowerShell Use the New-EC2Image cmdlet to specify a block device mapping for an EBS-backed AMI. Use the Register-EC2Image cmdlet to specify a block device mapping for an Amazon S3-backed AMI.
Add the -BlockDeviceMapping option, specifying the updates in bdm:
-BlockDeviceMapping $bdm The following mapping adds a volume based on a snapshot.
$ebd = New-Object -TypeName Amazon.EC2.Model.EbsBlockDevice $ebd.SnapshotId = "snap-1234567890abcdef0"
$bdm = New-Object -TypeName Amazon.EC2.Model.BlockDeviceMapping $bdm.DeviceName = "device_name"
$bdm.Ebs = $ebd

The following mapping adds an empty 100 GB volume.
$ebd = New-Object -TypeName Amazon.EC2.Model.EbsBlockDevice $ebd.VolumeSize = 100 $bdm = New-Object -TypeName Amazon.EC2.Model.BlockDeviceMapping $bdm.DeviceName = "device_name"
$bdm.Ebs = $ebd
### View the EBS volumes in an AMI block device mapping You can easily enumerate the EBS volumes in the block device mapping for an AMI.
Console To view the EBS volumes for an AMI
1. Open the Amazon EC2 console.
2. In the navigation pane, choose AMIs.
3. Choose EBS images from the Filter list to get a list of EBS-backed AMIs.
4. Select the desired AMI, and look at the Details tab. At a minimum, the following information is available for the root volume (where the term root device is equivalent to root volume):
- Root Device Type (ebs)
- Root Device Name (for example, /dev/sda1)
- Block Devices (for example, /dev/sda1=snap-1234567890abcdef0:8:true)
If the AMI was created with additional EBS volumes using a block device mapping, the Block Devices field displays the mapping for those additional volumes as well. (This screen doesn't display instance store volumes.)
AWS CLI To view the EBS volumes for an AMI Use the describe-images command. aws ec2 describe-images \

    --image-ids ami-0abcdef1234567890 \ --query Image[0].BlockDeviceMappings PowerShell To view the EBS volumes for an AMI Use the Get-EC2Image cmdlet.
(Get-EC2Image -ImageId ami-0abcdef1234567890).BlockDeviceMappings
## Add block device mappings to Amazon EC2 instance By default, an instance that you launch includes any storage devices specified in the block device mapping of the AMI from which you launched the instance. You can specify changes to the block device mapping for an instance when you launch it, and these updates overwrite or merge with the block device mapping of the AMI.
Limitations
- For the root volume, you can only modify the following: volume size, volume type, and the Delete on Termination flag.
- When you modify an EBS volume, you can't decrease its size. Therefore, you must specify a snapshot whose size is equal to or greater than the size of the snapshot specified in the block device mapping of the AMI.
Tasks
- Update the block device mapping when launching an instance
- Update the block device mapping of a running instance
- View the EBS volumes in an instance block device mapping
- View the instance block device mapping for instance store volumes
### Update the block device mapping when launching an instance You can add EBS volumes and instance store volumes to an instance when you launch it. Note that updating the block device mapping for an instance doesn't make a permanent change to the block device mapping of the AMI from which it was launched.

Console To update the volumes for an instance at launch
1. Follow the procedure to launch an instance, but don't launch the instance until you've completed the following steps to update the volumes.
2. (Optional) To add a volume, choose Configure storage, Add new volume. Select the volume size and volume type.
3. (Optional) To suppress a volume that was specified by the block device mapping of the AMI, choose Configure storage, Remove.
4. (Optional) To modify the configuration of an EBS volume, on the Configure storage pane, choose Advanced. Expand the information for the volume, and make whatever changes you need.
5. In the Summary panel, review your instance configuration, and then choose Launch instance. For more information, see Launch an EC2 instance using the launch instance wizard in the console.
AWS CLI To update the volumes for an instance at launch Use the run-instances command with the --block-device-mappings option.
--block-device-mappings file://mapping.json For example, suppose that an AMI block device mapping specifies the following:
- /dev/xvda - EBS root volume
- /dev/sdh - EBS volume created from snap-1234567890abcdef0
- /dev/sdj - Empty EBS volume with a size of 100
- /dev/sdb - Instance store volume ephemeral0 Suppose that the following is the instance block device mapping in mapping.json.
[ {

        "DeviceName": "/dev/xvda", "Ebs": { "VolumeSize": 100 } }, { "DeviceName": "/dev/sdj", "NoDevice": ""
    }, { "DeviceName": "/dev/sdh", "Ebs": { "VolumeSize": 300 } }, { "DeviceName": "/dev/sdc", "VirtualName": "ephemeral1"
    } ]
The instance block device mapping does the following:
- Overrides the size of the root volume, /dev/xvda, increasing it to 100 GiB.
- Prevents /dev/sdj from attaching to the instance.
- Overrides the size of /dev/sdh, increasing it to 300 GiB. Notice that you don't need to specify the snapshot ID again.
- Adds an ephemeral volume, /dev/sdc. If the instance type doesn't support multiple instance store volumes, this has no effect. If the instance type supports NVMe instance store volumes, they are automatically enumerated and included in the instance block device mapping and can't be overridden.
PowerShell To update the volumes for an instance at launch Use the -BlockDeviceMapping parameter with the New-EC2Instance cmdlet with the - BlockDeviceMapping parameter.
-BlockDeviceMapping $bdm

Suppose that the following is the instance block device mapping in $bdm.
$bdm = @()
$root = New-Object -TypeName Amazon.EC2.Model.BlockDeviceMapping $root.DeviceName = "/dev/xvda"
$ebs1 = New-Object -TypeName Amazon.EC2.Model.EbsBlockDevice $ebs1.VolumeSize = 100 $root.Ebs = $ebs1 $bdm += $root $sdj = New-Object -TypeName Amazon.EC2.Model.BlockDeviceMapping $sdj.DeviceName = "/dev/sdj"
$sdj.NoDevice = ""
$bdm += $sdj $sdh = New-Object -TypeName Amazon.EC2.Model.BlockDeviceMapping $sdh.DeviceName = "/dev/sdh"
$ebs2 = New-Object -TypeName Amazon.EC2.Model.EbsBlockDevice $ebs2.VolumeSize = 300 $sdh.Ebs = $ebs2 $bdm += $sdh $sdc = New-Object -TypeName Amazon.EC2.Model.BlockDeviceMapping $sdc.DeviceName = "/dev/sdc"
$sdc.VirtualName = "ephemeral1"
$bdm += $sdc The instance block device mapping does the following:
- Overrides the size of the root volume, /dev/xvda, increasing it to 100 GiB.
- Prevents /dev/sdj from attaching to the instance.
- Overrides the size of /dev/sdh, increasing it to 300 GiB. Notice that you don't need to specify the snapshot ID again.
- Adds an ephemeral volume, /dev/sdc. If the instance type doesn't support multiple instance store volumes, this has no effect. If the instance type supports NVMe instance store volumes, they are automatically enumerated and included in the instance block device mapping and can't be overridden.

### Update the block device mapping of a running instance You do not need to stop the instance before changing this attribute.
AWS CLI To update the block device mapping of a running instance Use the modify-instance-attribute command.
Add the --block-device-mappings option:
--block-device-mappings file://mapping.json In mapping.json, specify the updates. For example, the following update changes the root volume to persist.
[ { "DeviceName": "/dev/sda1", "Ebs": { "DeleteOnTermination": false } } ]
PowerShell To update the block device mapping of a running instance Use the Edit-EC2InstanceAttribute cmdlet.
Add the -BlockDeviceMapping option:
-BlockDeviceMapping $bdm In bdm, specify the updates. For example, the following update changes the root volume to persist.
$ebd = New-Object -TypeName Amazon.EC2.Model.EbsBlockDevice

$ebd.DeleteOnTermination = false $bdm = New-Object -TypeName Amazon.EC2.Model.BlockDeviceMapping $bdm.DeviceName = "/dev/sda1"
$bdm.Ebs = $ebd
### View the EBS volumes in an instance block device mapping You can easily enumerate the EBS volumes mapped to an instance.
Console To view the EBS volumes for an instance
1. Open the Amazon EC2 console.
2. In the navigation pane, choose Instances.
3. Select the instance and look at the details displayed in the Storage tab. At a minimum, the following information is available for the root volume (where the term root device is equivalent to root volume):
- Root device type (for example, EBS)
- Root device name (for example, /dev/xvda)
- Block devices (for example, /dev/xvda, /dev/sdf, and /dev/sdj)
If the instance was launched with additional EBS volumes using a block device mapping, they appear under Block devices. Any instance store volumes do not appear on this tab.
4. To display additional information about an EBS volume, choose its volume ID to go to the volume page.
AWS CLI To view the EBS volumes for an instance Use the describe-instances command. aws ec2 describe-instances \ --instance-ids i-1234567890abcdef0 \ --query Reservations[*].Instances[0].BlockDeviceMappings

PowerShell To view the EBS volumes for an instance Use the Get-EC2Instance cmdlet.
(Get-EC2Instance -InstanceId i-0bac57d7472c89bac).Instances.BlockDeviceMappings
### View the instance block device mapping for instance store volumes The instance type determines the number and type of instance store volumes that are available to the instance. If the number of instance store volumes in a block device mapping exceeds the number of instance store volumes available to an instance, the additional volumes are ignored. To view the instance store volumes for your instance, run the lsblk command (Linux instances) or open Windows Disk Management (Windows instances). To learn how many instance store volumes are supported by each instance type, see  Amazon EC2 instance type specifications.
When you view the block device mapping for your instance, you can see only the EBS volumes, not the instance store volumes. The method you use to view the instance store volumes for your instance depends on the volume type.
#### NVMe instance store volumes
##### Linux instances You can use the NVMe command line package, nvme-cli, to query the NVMe instance store volumes in the block device mapping. Download and install the package on your instance, and then run the following command.
[ec2-user ~]$ sudo nvme list The following is example output for an instance. The text in the Model column indicates whether the volume is an EBS volume or an instance store volume. In this example, both /dev/nvme1n1 and /dev/nvme2n1 are instance store volumes.
Node             SN                   Model Namespace

---------------- -------------------- ----------------------------------------
 --------- /dev/nvme0n1     vol06afc3f8715b7a597 Amazon Elastic Block Store               1

/dev/nvme1n1     AWS2C1436F5159EB6614 Amazon EC2 NVMe Instance Storage         1

/dev/nvme2n1     AWSB1F4FF0C0A6C281EA Amazon EC2 NVMe Instance Storage         1 ...
##### Windows instances You can use Disk Management or PowerShell to list both EBS and instance store NVMe volumes.
For more information, see the section called "Map NVME disks to volumes".
#### HDD or SSD instance store volumes You can use instance metadata to query the HDD or SSD instance store volumes in the block device mapping. NVMe instance store volumes are not included.
The base URI for all requests for instance metadata is http://169.254.169.254/latest/. For more information, see Use instance metadata to manage your EC2 instance.
##### Linux instances First, connect to your running instance. From the instance, use this query to get its block device mapping.
IMDSv2 [ec2-user ~]$ TOKEN=`curl -X PUT "http://169.254.169.254/latest/api/token" -H "X- aws-ec2-metadata-token-ttl-seconds: 21600"` \ && curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta- data/block-device-mapping/ IMDSv1 [ec2-user ~]$ curl http://169.254.169.254/latest/meta-data/block-device-mapping/ The response includes the names of the block devices for the instance. For example, the output for an instance store–backed m1.small instance looks like this.

ami ephemeral0 root swap The ami device is the root volume as seen by the instance. The instance store volumes are named ephemeral[0-23]. The swap device is for the page file. If you've also mapped EBS volumes, they appear as ebs1, ebs2, and so on.
To get details about an individual block device in the block device mapping, append its name to the previous query, as shown here.
IMDSv2 [ec2-user ~]$ TOKEN=`curl -X PUT "http://169.254.169.254/latest/api/token" -H "X- aws-ec2-metadata-token-ttl-seconds: 21600"` \ && curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta- data/block-device-mapping/ephemeral0 IMDSv1 [ec2-user ~]$ curl http://169.254.169.254/latest/meta-data/block-device-mapping/ ephemeral0
##### Windows instances First, connect to your running instance. From the instance, use this query to get its block device mapping.
PS C:\> Invoke-RestMethod -uri http://169.254.169.254/latest/meta-data/block-device- mapping/ The response includes the names of the block devices for the instance. For example, the output for an instance store–backed m1.small instance looks like this. ami ephemeral0 root
