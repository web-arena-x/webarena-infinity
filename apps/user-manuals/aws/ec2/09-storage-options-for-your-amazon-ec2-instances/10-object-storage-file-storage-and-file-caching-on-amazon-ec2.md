# Object storage, file storage, and file caching on Amazon EC2

Source: apps/user-manuals/aws/ec2-ug.pdf

---

Windows Server version AwsVssComponents version AWSEC2- Vs sInstallA ndSnapsho t version name AWSEC2- Cr eateVssSn apshot version name Windows Server 2008 R2 1.3.1.0 not supported 2008R2
# Object storage, file storage, and file caching on Amazon EC2 Cloud file storage is a method for storing data in the cloud that provides servers and applications access to data through shared file systems. This compatibility makes cloud file storage ideal for workloads that rely on shared file systems and provides simple integration without code changes.
There are many file storage solutions that exist, ranging from a single node file server on a compute instance using block storage as the underpinnings with no scalability or few redundancies to protect the data, to a do-it-yourself clustered solution, to a fully-managed solution. The following content introduces some of the storage services provided by AWS for use with Amazon EC2 instances.
Contents
- Use Amazon S3 with Amazon EC2 instances
- Use Amazon EFS with Amazon EC2 Linux instances
- Use Amazon FSx with Amazon EC2 instances
- Use Amazon File Cache with Amazon EC2 instances
## Use Amazon S3 with Amazon EC2 instances Amazon Simple Storage Service (Amazon S3) is an object storage service that offers industry- leading scalability, data availability, security, and performance. You can use Amazon S3 to store and retrieve any amount of data for a range of use cases, such as data lakes, websites, backups, and big data analytics, from an Amazon EC2 instance or from anywhere over the internet. For more information, see What is Amazon S3?

Objects are the fundamental entities stored in Amazon S3. Every object stored in Amazon S3 is contained in a bucket. Buckets organize the Amazon S3 namespace at the highest level and identify the account responsible for that storage. Amazon S3 buckets are similar to internet domain names. Objects stored in the buckets have a unique key value and are retrieved using a URL. For example, if an object with a key value /photos/mygarden.jpg is stored in the amzn- s3-demo-bucket1 bucket, then it is addressable using the URL https://amzn-s3-demo- bucket1.s3.amazonaws.com/photos/mygarden.jpg. For more information, see  How Amazon S3 works.
### Usage examples Given the benefits of Amazon S3 for storage, you might decide to use this service to store files and data sets for use with EC2 instances. There are several ways to move data to and from Amazon S3 to your instances. In addition to the examples discussed below, there are a variety of tools that people have written that you can use to access your data in Amazon S3 from your computer or your instance.
If you have permission, you can copy a file to or from Amazon S3 and your instance using one of the following methods. wget Note This method works for public objects only. If the object is not public, you receive an ERROR 403: Forbidden message. If you receive this error, you must use either the Amazon S3 console, AWS CLI, AWS API, AWS SDK, or AWS Tools for Windows PowerShell, and you must have the required permissions. For more information, see Identity and access management for Amazon S3 and  Downloading an object in the Amazon S3 User Guide.
The wget utility is an HTTP and FTP client that allows you to download public objects from Amazon S3. It is installed by default in Amazon Linux and most other distributions, and available for download on Windows. To download an Amazon S3 object, use the following command, substituting the URL of the object to download.
[ec2-user ~]$ wget https://amzn-s3-demo-bucket.s3.amazonaws.com/path-to-file

PowerShell You can use the AWS Tools for Windows PowerShell to move objects to and from Amazon S3.
Use the Copy-S3Object cmdlet to copy an Amazon S3 object to your Windows instance as follows.
Copy-S3Object `
    -BucketName amzn-s3-demo-bucket `
    -Key path-to-file `
    -LocalFile my_copied_file.ext Alternatively, you can open the Amazon S3 console by using a web browser on the Windows instance.
AWS CLI You can use the AWS Command Line Interface (AWS CLI) to download restricted items from Amazon S3 and also to upload items. For more information, such as how to install and configure the tools, see the AWS Command Line Interface detail page.
The aws s3 cp command is similar to the Unix cp command. You can copy files from Amazon S3 to your instance, copy files from your instance to Amazon S3, and copy files from one Amazon S3 location to another.
Use the following command to copy an object from Amazon S3 to your instance. aws s3 cp s3://amzn-s3-demo-bucket/my_folder/my_file.ext my_copied_file.ext Use the following command to copy an object from your instance back into Amazon S3. aws s3 cp my_copied_file.ext s3://amzn-s3-demo-bucket/my_folder/my_file.ext The aws s3 sync command can synchronize an entire Amazon S3 bucket to a local directory location. This can be helpful for downloading a data set and keeping the local copy up-to-date with the remote set. If you have the proper permissions on the Amazon S3 bucket, you can push your local directory back up to the cloud when you are finished by reversing the source and destination locations in the command.
Use the following command to download an entire Amazon S3 bucket to a local directory on your instance.

aws s3 sync s3://amzn-s3-demo-source-bucket local_directory Amazon S3 API If you are a developer, you can use an API to access data in Amazon S3. You can use this API to help develop your application and integrate it with other APIs and SDKs. For more information, see Code examples for Amazon S3 using AWS SDKs in the Amazon Simple Storage Service API Reference.
## Use Amazon EFS with Amazon EC2 Linux instances Note Amazon EFS is not supported on Windows instances.
Amazon EFS provides scalable file storage for use with Amazon EC2. You can use an EFS file system as a common data source for workloads and applications running on multiple instances. For more information, see the Amazon Elastic File System product page.
This tutorial shows you how to create and attach an Amazon EFS file system using the Amazon EFS Quick Create wizard during instance launch. For a tutorial on how to create a file system using the Amazon EFS console, see Getting started with Amazon Elastic File System in the Amazon Elastic File System User Guide.
Note When you create an EFS file system using EFS Quick Create, the file system is created with the following service recommended settings:
- Automatic backups enabled.
- Manage mount targets in the selected VPC.
- General Purpose performance mode.
- Bursting throughput mode.
- Encryption of data at rest enabled using your default key for Amazon EFS (aws/ elasticfilesystem).

- Amazon EFS lifecycle management enabled with a 30-day policy.
Tasks
- Create an EFS file system using Amazon EFS Quick Create
- Test the EFS file system
- Delete the EFS file system
### Create an EFS file system using Amazon EFS Quick Create You can create an EFS file system and mount it to your instance when you launch your instance using the Amazon EFS Quick Create feature of the Amazon EC2 launch instance wizard.
To create an EFS file system using Amazon EFS Quick Create
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. Choose Launch instance.
3. (Optional) Under Name and tags, for Name, enter a name to identify your instance.
4. Under Application and OS Images (Amazon Machine Image), choose a Linux operating system, and then for Amazon Machine Image (AMI), select a Linux AMI.
5. Under Instance type, for Instance type, select an instance type or keep the default.
6. Under Key pair (login), for Key pair name, choose an existing key pair or create a new one.
7. Under Network settings, choose Edit (at right), and then for Subnet, select a subnet.
Note You must select a subnet before you can add an EFS file system.
8. Under Configure storage, choose Edit (at bottom right), and then do the following: a.
For File systems, ensure that EFS is selected, and then choose Create new shared file system. b.
For File system name enter a name for the Amazon EFS file system, and then choose Create file system. c.
For Mount point, specify a custom mount point or keep the default.

d.
To enable access to the file system, select Automatically create and attach security groups. By selecting this checkbox, the following security groups will be automatically created and attached to the instance and the mount targets of the file system:
- Instance security group – Includes an outbound rule that allows traffic over the NFS 2049port, but includes no inbound rules.
- File system mount targets security group – Includes an inbound rule that allows traffic over the NFS 2049 port from the instance security group (described above), and an outbound rule that allows traffic over the NFS 2049 port.
Note Alternatively, you can manually create and attach the security groups. If you want to manually create and attach the security groups, clear Automatically create and attach the required security groups. e.
To automatically mount the shared file system when the instance launches, select Automatically mount shared file system by attaching required user data script. To view the user data that is automatically generated, expand Advanced details, and scroll down to User data.
Note If you added user data before selecting this checkbox, the original user data is overwritten by the automatically generated user data.
9. Configure any other instance configuration settings as needed.
10. In the Summary panel, review your instance configuration, and then choose Launch instance.
For more information, see Launch an EC2 instance using the launch instance wizard in the console.
### Test the EFS file system You can connect to your instance and verify that the file system is mounted to the directory that you specified (for example, /mnt/efs).

To verify that the file system is mounted
1. Connect to your instance. For more information, see Connect to your Linux instance using SSH.
2. From the terminal window for the instance, run the df -T command to verify that the EFS file system is mounted.
$ df -T Filesystem     Type              1K-blocks    Used          Available Use% Mounted on /dev/xvda1     ext4                8123812 1949800            6073764  25% / devtmpfs       devtmpfs            4078468      56            4078412   1% /dev tmpfs          tmpfs               4089312       0            4089312   0% /dev/shm efs-dns        nfs4       9007199254740992       0   9007199254740992   0% /mnt/efs Note that the name of the file system, shown in the example output as efs-dns, has the following form. file-system-id.efs.aws-region.amazonaws.com:/
3. (Optional) Create a file in the file system from the instance, and then verify that you can view the file from another instance. a.
From the instance, run the following command to create the file.
$ sudo touch /mnt/efs/test-file.txt b.
From the other instance, run the following command to view the file.
$ ls /mnt/efs test-file.txt
### Delete the EFS file system If you no longer need your file system, you can delete it.
To delete the file system
1. Open the Amazon Elastic File System console at https://console.aws.amazon.com/efs/.
2. Select the file system to delete.

3. Choose Actions, Delete file system.
4. When prompted for confirmation, enter the file system ID and choose Delete file system.
## Use Amazon FSx with Amazon EC2 instances The Amazon FSx family of services makes it easy to launch, run, and scale shared storage powered by popular commercial and open-source file systems. You can use the new launch instance wizard to automatically attach the following types of Amazon FSx file systems to your Amazon EC2 instances at launch:
- Amazon FSx for NetApp ONTAP provides fully managed shared storage in the AWS Cloud with the popular data access and management capabilities of NetApp ONTAP.
- Amazon FSx for OpenZFS provides fully managed cost-effective shared storage powered by the popular OpenZFS file system.
Note
- This functionality is available in the new launch instance wizard only. For more information, see Launch an EC2 instance using the launch instance wizard in the console
- Amazon FSx for Windows File Server and Amazon FSx for Lustre file systems can't be mounted at launch. You must mount these file systems manually after launch.
You can choose to mount an existing file system that you created previously, or you can create a new file system to mount to an instance at launch.
Topics
- Security groups and user data script
- Mount an Amazon FSx file system at launch
### Security groups and user data script When you mount an Amazon FSx file system to an instance using the launch instance wizard, you can choose whether to automatically create and attach the security groups needed to enable

access to the file system, and whether to automatically include the user data scripts needed to mount the file system and make it available for use.
Topics
- Security groups
- User data script
#### Security groups If you choose to automatically create the security groups that are needed to enable access to the file system, the launch instance wizard creates and attaches two security groups - one security group is attached to the instance, and the other is attached to the file system. For more information about the security group requirements, see FSx for ONTAP file system access control with Amazon VPC and FSx for OpenZFS file system access control with Amazon VPC.
We add the tag Name=instance-sg-1 to the security group that is created and attached to the instance. The value in the tag is automatically incremented each time the launch instance wizard creates a security group for Amazon FSx file systems.
The security group includes the following output rules, but no inbound rules.
Outbound rules Protocol type Port number Destination UDP 111 file system security group UDP 20001 - 20003 file system security group UDP 4049 file system security group UDP 2049 file system security group UDP 635 file system security group UDP 4045 - 4046 file system security group TCP 4049 file system security group TCP 635 file system security group

Protocol type Port number Destination TCP 2049 file system security group TCP 111 file system security group TCP 4045 - 4046 file system security group TCP 20001 - 20003 file system security group All All file system security group The security group that is created and attached to the file system is tagged with Name=fsx-sg-1.
The value in the tag is automatically incremented each time the launch instance wizard creates a security group for Amazon FSx file systems.
The security group includes the following rules.
Inbound rules Protocol type Port number Source UDP 2049 instance security group UDP 20001 - 20003 instance security group UDP 4049 instance security group UDP 111 instance security group UDP 635 instance security group UDP 4045 - 4046 instance security group TCP 4045 - 4046 instance security group TCP 635 instance security group TCP 2049 instance security group TCP 4049 instance security group

Protocol type Port number Source TCP 20001 - 20003 instance security group TCP 111 instance security group Outbound rules Protocol type Port number Destination All All 0.0.0.0/0
#### User data script If you choose to automatically attach user data scripts, the launch instance wizard adds the following user data to the instance. This script installs the necessary packages, mounts the file system, and updates your instance settings so that the file system will automatically re-mount whenever the instance restarts.
#cloud-config package_update: true package_upgrade: true runcmd:
- yum install -y nfs-utils
- apt-get -y install nfs-common
- svm_id_1=svm_id
- file_system_id_1=file_system_id
- vol_path_1=/vol1
- fsx_mount_point_1=/mnt/fsx/fs1
- mkdir -p "${fsx_mount_point_1}"
- if [ -z "$svm_id_1" ]; then printf "\n${file_system_id_1}.fsx.eu- north-1.amazonaws.com:/${vol_path_1} ${fsx_mount_point_1} nfs4 nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2,noresvport,_netdev 0 0\n" >> /etc/fstab; else printf "\n${svm_id_1}.${file_system_id_1}.fsx.eu- north-1.amazonaws.com:/${vol_path_1} ${fsx_mount_point_1} nfs4 nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2,noresvport,_netdev 0 0\n" >> /etc/fstab; fi
- retryCnt=15; waitTime=30; while true; do mount -a -t nfs4 defaults; if [ $? = 0 ] || [ $retryCnt -lt 1 ]; then echo File system mounted successfully; break; fi; echo File system not available, retrying to mount.; ((retryCnt--)); sleep $waitTime; done;

### Mount an Amazon FSx file system at launch To mount a new or existing Amazon FSx file system at launch
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Instances and then choose Launch instance to open the launch instance wizard.
3. In the Application and OS Images section, select the AMI to use.
4. In the Instance type section, select the instance type.
5. In the Key pair section, select an existing key pair or create a new one.
6. In the Network settings section, do the following: a.
Choose Edit. b.
If you want to mount an existing file system, for Subnet, choose the file system's preferred subnet. We recommend that you launch the instance into the same Availability Zone as the file system's preferred subnet to optimize performance.
If you want to create a new file system to mount to an instance, for Subnet, choose the subnet into which to launch the instance.
Important You must select a subnet to enable the Amazon FSx functionality in the new launch instance wizard. If you do not select a subnet, you will not be able to mount an existing file system or create a new one.
7. In the Storage section, do the following: a.
Configure the volumes as needed. b.
Expand the File systems section and select FSx. c.
Choose Add shared file system. d.
For File system, select the file system to mount.

Note The list displays all Amazon FSx for NetApp ONTAP and Amazon FSx for OpenZFS file systems in your account in the selected Region. e.
To automatically create and attach the security groups needed to enable access to the file system, select Automatically create and attach security groups. If you prefer to create the security groups manually, clear the checkbox. For more information, see Security groups. f.
To automatically attach the user data scripts needed to mount the file system, select Automatically mount shared file system by attaching required user data script. If you prefer to provide the user data scripts manually, clear the checkbox. For more information, see User data script.
8. In the Advanced section, configure the additional instance settings as needed.
9. Choose Launch.
## Use Amazon File Cache with Amazon EC2 instances Amazon File Cache provides a fully managed, high-speed cache on AWS that makes it easier to process file data, regardless of where the data is stored. Amazon File Cache serves as a temporary, high-performance storage location for data that's stored in on-premises file systems, AWS file systems, and Amazon Simple Storage Service (Amazon S3) buckets. You can use this capability to make dispersed datasets available to file-based applications on AWS with a unified view, and at high speeds—sub-millisecond latencies and high throughput. For more information, see the Amazon File Cache User Guide.
Amazon File Cache works with the most popular Linux AMIs, and is compatible with x86-based instance types and Graviton instance types. You can access your cache from your Amazon EC2 instances using the open-source Lustre client. You can mount your cache and then work with the files and directories in your cache using standard Linux commands. Amazon EC2 instances can access your cache from other Availability Zones within the same virtual private cloud (VPC), provided that your network configuration allows access across subnets within the VPC. You can also create a cache in a shared VPC.
To get started, see  Getting started with Amazon File Cache in the Amazon File Cache User Guide.
