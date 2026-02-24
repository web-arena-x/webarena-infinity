# Amazon EC2 AMI lifecycle

Source: apps/user-manuals/aws/ec2-ug.pdf

---

# Amazon EC2 AMI lifecycle An Amazon Machine Image (AMI) is an image that contains the software configuration required to set up and boot an instance. You must specify an AMI when you launch an instance. You can use AMIs provided by Amazon, or you can create your own AMIs. The AMI must be located in the AWS Region in which you want to launch your instance.
The lifecycle of an AMI includes creating, copying, deprecating, disabling, and deleting (deregistering) the AMI.
Create AMIs. While Amazon provides AMIs that you can use to launch your instances, you can create custom AMIs tailored to your needs. To create a custom AMI, launch an instance from an existing AMI, customize the instance (for example, install software and configure operating system settings), and then create an AMI from the instance. Any instance customizations are saved to the new AMI, so that instances launched from your new AMI include these customizations.
Attestable AMIs. To create an AMI that supports EC2 instance attestation, see Attestable AMIs.
Copy AMIs. You can use an AMI to launch an instance only in the AWS Region in which the AMI is located. If you need to launch instances with the same configuration in multiple Regions, copy the AMI to the other Regions.
Deprecate AMIs. To mark an AMI as superseded or out of date, you can set an immediate or future deprecation date. Deprecated AMIs are hidden from AMI listings, but users and services can continue to use deprecated AMIs if they know the AMI ID.
Disable AMIs. To temporarily prevent an AMI from being used, you can disable it. When an AMI is disabled, it can't be used to launch new instances. However, if you re-enable the AMI, it can be used to launch instances again. Note that disabling an AMI doesn't affect existing instances that have already been launched from it.
Deregister (delete) AMIs. When you no longer need an AMI, you can deregister it, preventing it from being used to launch new instances. If the AMI matches a retention rule, it moves to the Recycle Bin, where it can be restored before its retention period expires, after which it is permanently deleted. If it doesn't match a retention rule, it is permanently deleted immediately.
Note that deregistering an AMI does not affect existing instances that were launched from the AMI.
Automate the AMI lifecycle. You can use Amazon Data Lifecycle Manager to automate the creation, retention, copy, deprecation, and deregistration of Amazon EBS-backed AMIs and their

backing snapshots. You can also use EC2 Image Builder to automate the creation, management, an deployment of customized AMIs. For more information, see Automate backups with Amazon Data Lifecycle Manager in the Amazon EBS User Guide and the EC2 Image Builder User Guide.
Contents
- Create an Amazon EBS-backed AMI
- Create an Amazon S3-backed AMI
- Create an Amazon EC2 AMI using Windows Sysprep
- Copy an Amazon EC2 AMI
- Store and restore an AMI using S3
- Use AMI ancestry to trace the origin of an AMI
- Manage and monitor AMI usage
- Deprecate an Amazon EC2 AMI
- Disable an Amazon EC2 AMI
- Deregister an Amazon EC2 AMI
## Create an Amazon EBS-backed AMI You can create your own Amazon EBS-backed AMI from an Amazon EC2 instance or from a snapshot of the root volume of an Amazon EC2 instance.
To create an Amazon EBS-backed AMI from an instance, start by launching an instance using an existing Amazon EBS-backed AMI. This AMI can be one you obtained from the AWS Marketplace, created using VM Import/Export, or any other AMI that you can access. After customizing the instance to meet your specific requirements, create and register a new AMI. You can then use the new AMI to launch new instances with your customizations.
Note To create an AMI that supports EC2 instance attestation, see Attestable AMIs.
The procedures described below work for Amazon EC2 instances backed by encrypted Amazon Elastic Block Store (Amazon EBS) volumes (including the root volume) as well as for unencrypted volumes.

The AMI creation process is different for Amazon S3-backed AMIs. For more information, see Create an Amazon S3-backed AMI.
Contents
- Overview of AMI creation from an instance
- Create an AMI from an instance
- Create an AMI from a snapshot
### Overview of AMI creation from an instance The following diagram summarizes the process for creating an Amazon EBS-backed AMI from a running EC2 instance: Start with an existing AMI, launch an instance, customize it, create a new AMI from it, and finally launch an instance of your new AMI. The numbers in the diagram match the numbers in the description that follows.
1 – AMI #1: Start with an existing AMI Find an existing AMI that is similar to the AMI that you'd like to create. This can be an AMI you have obtained from the AWS Marketplace, an AMI that you have created using VM Import/ Export, or any other AMI that you can access. You'll customize this AMI for your needs.
In the diagram, EBS root volume snapshot #1 indicates that the AMI is an Amazon EBS-backed AMI and that information about the root volume is stored in this snapshot.
2 – Launch instance from existing AMI The way to configure an AMI is to launch an instance from the AMI on which you'd like to base your new AMI, and then customize the instance (indicated at 3 in the diagram). Then, you'll create a new AMI that includes the customizations (indicated at 4 in the diagram).
3 – EC2 instance #1: Customize the instance Connect to your instance and customize it for your needs. Your new AMI will include these customizations.

You can perform any of the following actions on your instance to customize it:
- Install software and applications
- Copy data
- Reduce start time by deleting temporary files and defragmenting your hard drive
- Attach additional EBS volumes 4 – Create image When you create an AMI from an instance, Amazon EC2 powers down the instance before creating the AMI to ensure that everything on the instance is stopped and in a consistent state during the creation process. If you're confident that your instance is in a consistent state appropriate for AMI creation, you can tell Amazon EC2 not to power down and reboot the instance. Some file systems, such as XFS, can freeze and unfreeze activity, making it safe to create the image without rebooting the instance.
During the AMI-creation process, Amazon EC2 creates snapshots of your instance's root volume and any other EBS volumes attached to your instance. You're charged for the snapshots until you deregister the AMI and delete the snapshots. If any volumes attached to the instance are encrypted, the new AMI only launches successfully on instances that support Amazon EBS encryption.
Depending on the size of the volumes, it can take several minutes for the AMI-creation process to complete (sometimes up to 24 hours). You might find it more efficient to create snapshots of your volumes before creating your AMI. This way, only small, incremental snapshots need to be created when the AMI is created, and the process completes more quickly (the total time for snapshot creation remains the same).
5 – AMI #2: New AMI After the process completes, you have a new AMI and snapshot (snapshot #2) created from the root volume of the instance. If you added instance store volumes or EBS volumes to the instance, in addition to the root volume, the block device mapping for the new AMI contains information for these volumes.
Amazon EC2 automatically registers the AMI for you.
6 – Launch instance from new AMI You can use the new AMI to launch an instance.

7 – EC2 instance #2: New instance When you launch an instance using the new AMI, Amazon EC2 creates a new EBS volume for the instance's root volume using the snapshot. If you added instance store volumes or EBS volumes when you customized the instance, the block device mapping for the new AMI contains information for these volumes, and the block device mappings for instances that you launch from the new AMI automatically contain information for these volumes. The instance store volumes specified in the block device mapping for the new instance are new and don't contain any data from the instance store volumes of the instance you used to create the AMI. The data on EBS volumes persists. For more information, see Block device mappings for volumes on Amazon EC2 instances.
When you create a new instance from an EBS-backed AMI, you should initialize both its root volume and any additional EBS storage before putting it into production. For more information, see Initialize Amazon EBS volumes in the Amazon EBS User Guide.
### Create an AMI from an instance If you have an existing instance, you can create an AMI from this instance.
Console To create an AMI
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Instances.
3. Select the instance from which to create the AMI, and then choose Actions, Image and templates, Create image.
Tip If this option is disabled, your instance isn't an Amazon EBS-backed instance.
4. On the Create image page, specify the following information: a.
For Image name, enter a unique name for the image, up to 127 characters. b.
For Image description, enter an optional description of the image, up to 255 characters.

c.
For Reboot instance, either keep the checkbox selected (the default), or clear it.
- If Reboot instance is selected, when Amazon EC2 creates the new AMI, it reboots the instance so that it can take snapshots of the attached volumes while data is at rest, in order to ensure a consistent state.
- If Reboot instance is cleared, when Amazon EC2 creates the new AMI, it does not shut down and reboot the instance.
Warning If you clear Reboot instance, we can't guarantee the file system integrity of the created image. d.
Instance volumes – You can modify the root volume, and add additional Amazon EBS and instance store volumes, as follows: i.
The root volume is defined in the first row.
- To change the size of the root volume, for Size, enter the required value.
- If you select Delete on termination, when you terminate the instance created from this AMI, the EBS volume is deleted. If you clear Delete on termination, when you terminate the instance, the EBS volume is not deleted. For more information, see Preserve data when an instance is terminated. ii.
To add an EBS volume, choose Add volume (which adds a new row). For Storage type, choose EBS, and fill in the fields in the row. When you launch an instance from your new AMI, additional volumes are automatically attached to the instance.
Empty volumes must be formatted and mounted. Volumes based on a snapshot must be mounted. iii.
To add an instance store volume, see Add instance store volumes to an Amazon EC2 AMI. When you launch an instance from your new AMI, additional volumes are automatically initialized and mounted. These volumes do not contain data from the instance store volumes of the running instance on which you based your AMI. e.
Snapshot destination – If your instance volumes are in a Local Zone that supports EBS local snapshots, choose where to create the AMI's snapshots:

- AWS Region: Create snapshots in the parent Region of the Local Zone of your volumes.
- AWS Local Zone: Create snapshots in the same Local Zone as your volumes.
Note This option appears only in Local Zones that support EBS local snapshots, and only if your instance was created in a Local Zone. If the volume is in a Region, this option does not appear, and the snapshot is automatically created in the same Region as the volume. For more information, see Local snapshots in Local Zones in the Amazon EBS User Guide.
Important All snapshots of the instance's volumes must be in the same location. Verify the location of existing snapshots. If any existing snapshots are in a different location than your selected destination, the AMI creation will fail. f.
Tags – You can tag the AMI and the snapshots with the same tags, or you can tag them with different tags.
- To tag the AMI and the snapshots with the same tags, choose Tag image and snapshots together. The same tags are applied to the AMI and every snapshot that is created.
- To tag the AMI and the snapshots with different tags, choose Tag image and snapshots separately. Different tags are applied to the AMI and the snapshots that are created. However, all the snapshots get the same tags; you can't tag each snapshot with a different tag.
To add a tag, choose Add tag, and enter the key and value for the tag. Repeat for each tag. g.
When you're ready to create your AMI, choose Create image.
5. To view the status of your AMI while it is being created:

a.
In the navigation pane, choose AMIs. b.
Set the filter to Owned by me, and find your AMI in the list.
Initially, the status is pending but should change to available after a few minutes.
6. (Optional) To view the snapshot that was created for the new AMI: a.
Note the ID of your AMI that you located in the previous step. b.
In the navigation pane, choose Snapshots. c.
Set the filter to Owned by me, and then find the snapshot with the new AMI ID in the Description column.
When you launch an instance from this AMI, Amazon EC2 uses this snapshot to create the instance's root volume.
AWS CLI To create an AMI Use the create-image command. aws ec2 create-image \ --instance-id i-1234567890abcdef0 \ --name "my-web-server" \ --description "My web server image" \ --no-reboot PowerShell To create an AMI Use the New-EC2Image cmdlet.
New-EC2Image `
    -InstanceId i-1234567890abcdef0 `
    -Name "my-web-server" `
    -Description "My web server image" `
    -NoReboot $true

### Create an AMI from a snapshot If you have a snapshot of the root volume of an instance, you can create an AMI from this snapshot.
Note In most cases, AMIs for Windows, Red Hat, SUSE, and SQL Server require correct licensing information to be present on the AMI. For more information, see Understand AMI billing information. When creating an AMI from a snapshot, the RegisterImage operation derives the correct billing information from the snapshot's metadata, but this requires the appropriate metadata to be present. To verify if the correct billing information was applied, check the Platform details field on the new AMI. If the field is empty or doesn't match the expected operating system code (for example, Windows, Red Hat, SUSE, or SQL), the AMI creation was unsuccessful, and you should discard the AMI and follow the instructions in Create an AMI from an instance.
Console To create an AMI from a snapshot
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Snapshots.
3. Select the snapshot from which to create the AMI, and then choose Actions, Create image from snapshot.
4. On the Create image from snapshot page, specify the following information: a.
For Image name, enter a descriptive name for the image. b.
For Description, enter a brief description for the image. c.
For Architecture, choose the image architecture. Choose i386 for 32-bit, x86_64 for 64-bit, arm64 for 64-bit ARM, or x86_64 for 64-bit macOS. d.
For Root device name, enter the device name to use for the root volume. For more information, see Device names for volumes on Amazon EC2 instances. e.
For Virtualization type, choose the virtualization type to be used by instances launched from this AMI. For more information, see Virtualization types.

f.
(For paravirtual virtualization only) For Kernel ID, select the operating system kernel for the image. If you're using a snapshot of the root volume of an instance, select the same kernel ID as the original instance. If you're unsure, use the default kernel. g.
(For paravirtual virtualization only) For RAM disk ID, select the RAM disk for the image.
If you select a specific kernel, you may need to select a specific RAM disk with the drivers to support it. h.
For Boot mode, choose the boot mode for the image, or choose Use default so that when an instance is launched with this AMI, it boots with the boot mode supported by the instance type. For more information, see Set the boot mode of an Amazon EC2 AMI. i.
(Optional) Under Block device mappings, customize the root volume and add additional data volumes.
For each volume, you can specify the size, type, performance characteristics, the behavior of delete on termination, and encryption status. For the root volume, the size can't be smaller than the size of the snapshot. For volume type, General Purpose SSD gp3 is the default selection. j.
(Optional) Under Tags, you can add one or more tags to the new AMI. To add a tag, choose Add tag, and enter the key and value for the tag. Repeat for each tag. k.
When you're ready to create your AMI, choose Create image.
5. (Windows, Red Hat, SUSE, and SQL Server only) To verify if the correct billing information was applied, check the Platform details field on the new AMI. If the field is empty or doesn't match the expected operating system code (for example, Windows or Red Hat), the AMI creation was unsuccessful, and you should discard the AMI and follow the instructions in Create an AMI from an instance.
AWS CLI To create an AMI from a snapshot using the AWS CLI Use the register-image command. aws ec2 register-image \ --name my-image \ --root-device-name /dev/xvda \

    --block-device-mappings DeviceName=/dev/ xvda,Ebs={SnapshotId=snap-0db2cf683925d191f} PowerShell To create an AMI from a snapshot using PowerShell Use the Register-EC2Image cmdlet.
$block = @{SnapshotId=snap-0db2cf683925d191f} Register-EC2Image `
    -Name my-image `
    -RootDeviceName /dev/xvda `
    -BlockDeviceMapping @{DeviceName="/dev/xvda";Ebs=$block}
## Create an Amazon S3-backed AMI The AMI that you specify when you launch your instance determines the type of root volume.
To create an Amazon S3-backed Linux AMI, start from an instance that you've launched from an existing Amazon S3-backed Linux AMI. After you've customized the instance to suit your needs, bundle the volume and register a new AMI, which you can use to launch new instances with these customizations.
You can't create an Amazon S3-backed Windows AMI because Windows AMIs don't support instance store for the root volume.
Important Only the following instance types support an instance store volume as the root volume and require an Amazon S3-backed AMI: C1, C3, D2, I2, M1, M2, M3, R3, and X1.
The AMI creation process is different for Amazon EBS-backed AMIs. For more information, see Create an Amazon EBS-backed AMI.
Contents
- Overview of AMI creation
- Prerequisites

- Create an AMI from an Amazon Linux instance
- Set up the Amazon EC2 AMI tools
- Amazon EC2 AMI tools reference
- Convert your Amazon S3-backed AMI to an EBS-backed AMI
### Overview of AMI creation The following diagram summarizes the process of creating an AMI from an instance with an instance store root volume.
First, launch an instance from an AMI that's similar to the AMI that you'd like to create. You can connect to your instance and customize it. When the instance is set up the way you want it, you can bundle it. It takes several minutes for the bundling process to complete. After the process completes, you have a bundle, which consists of an image manifest (image.manifest.xml) and files (image.part.xx) that contain a template for the root volume. Next you upload the bundle to your Amazon S3 bucket and then register your AMI.
Note To upload objects to an S3 bucket for your Amazon S3-backed Linux AMI, ACLs must be enabled for the bucket. Otherwise, Amazon EC2 will not be able to set ACLs on the objects to upload. If your destination bucket uses the bucket owner enforced setting for S3 Object Ownership, this won't work because ACLs are disabled. For more information, see Controlling ownership of objects and disabling ACLs for your bucket.

When you launch an instance using the new AMI, we create the root volume for the instance using the bundle that you uploaded to Amazon S3. The storage space used by the bundle in Amazon S3 incurs charges to your account until you delete it. For more information, see Deregister an Amazon EC2 AMI.
If you add instance store volumes to your instance in addition to the root volume, the block device mapping for the new AMI contains information for these volumes, and the block device mappings for instances that you launch from the new AMI automatically contain information for these volumes. For more information, see Block device mappings for volumes on Amazon EC2 instances.
### Prerequisites Before you can create an AMI, you must complete the following tasks:
- Install the AMI tools. For more information, see Set up the Amazon EC2 AMI tools.
- Install the AWS CLI. For more information, see Getting started with the AWS CLI.
- Ensure that you have an S3 bucket for the bundle, and that your bucket has ACLs enabled. For more information on configuring ACLs, see Configuring ACLs.
- To create an S3 bucket using the AWS Management Console, open the Amazon S3 console at https://console.aws.amazon.com/s3/ and choose Create Bucket.
- To create an S3 bucket with the AWS CLI, you can use the mb command. If your installed version of the AMI tools is 1.5.18 or later, you can also use the ec2-upload-bundle command to create the S3 bucket. For more information, see ec2-upload-bundle.
- Ensure that the files in your bundle aren't encrypted in the S3 bucket. If you require encryption for your AMI, you can use an EBS-backed AMI instead. For more information, see Use encryption with EBS-backed AMIs.
- Ensure that you have your AWS account ID. For more information, see View AWS account identifiers in the AWS Account Management Reference Guide.
- Ensure that you have credentials to use the AWS CLI. For more information, see Authentication and access credentials for the AWS CLI in the AWS Command Line Interface User Guide.
- Ensure that you have an X.509 certificate and corresponding private key.
- If you need to create an X.509 certificate, see Manage signing certificates. The X.509 certificate and private key are used to encrypt and decrypt your AMI.
- [China (Beijing)] Use the $EC2_AMITOOL_HOME/etc/ec2/amitools/cert-ec2-cn- north-1.pem certificate.

- [AWS GovCloud (US-West)] Use the $EC2_AMITOOL_HOME/etc/ec2/amitools/cert-ec2- gov.pem certificate.
- Connect to your instance and customize it. For example, you can install software and applications, copy data, delete temporary files, and modify the Linux configuration.
### Create an AMI from an Amazon Linux instance The following procedures describe how to create an AMI from an instance with an instance store root volume running Amazon Linux 1. They might not work for instances running other Linux distributions.
To prepare to use the AMI tools (HVM instances only)
1. The AMI tools require GRUB Legacy to boot properly. Use the following command to install GRUB:
[ec2-user ~]$ sudo yum install -y grub
2. Install the partition management packages with the following command:
[ec2-user ~]$ sudo yum install -y gdisk kpartx parted To create an AMI from an Amazon Linux instance with an instance store root volume This procedure assumes that you have satisfied the prerequisites in Prerequisites.
In the following commands, replace each user input placeholder with your own information.
1. Upload your credentials to your instance. We use these credentials to ensure that only you and Amazon EC2 can access your AMI. a.
Create a temporary directory on your instance for your credentials as follows:
[ec2-user ~]$ mkdir /tmp/cert This enables you to exclude your credentials from the created image. b.
Copy your X.509 certificate and corresponding private key from your computer to the / tmp/cert directory on your instance using a secure copy tool such as scp. The -i my-

private-key.pem option in the following scp command is the private key you use to connect to your instance with SSH, not the X.509 private key. For example: you@your_computer:~ $ scp -i my-private-key.pem / path/to/pk-HKZYKTAIG2ECMXYIBH3HXV4ZBEXAMPLE.pem / path/to/cert-HKZYKTAIG2ECMXYIBH3HXV4ZBEXAMPLE.pem ec2- user@ec2-203-0-113-25.compute-1.amazonaws.com:/tmp/cert/ pk-HKZYKTAIG2ECMXYIBH3HXV4ZBEXAMPLE.pem  100%  717     0.7KB/s   00:00 cert-HKZYKTAIG2ECMXYIBH3HXV4ZBEXAMPLE.pem  100%  685     0.7KB/s   00:00 Alternatively, because these are plain text files, you can open the certificate and key in a text editor and copy their contents into new files in /tmp/cert.
2. Prepare the bundle to upload to Amazon S3 by running the ec2-bundle-vol command from inside your instance. Be sure to specify the -e option to exclude the directory where your credentials are stored. By default, the bundle process excludes files that might contain sensitive information. These files include *.sw, *.swo, *.swp, *.pem, *.priv, *id_rsa*, *id_dsa* *.gpg, *.jks, */.ssh/authorized_keys, and */.bash_history. To include all of these files, use the --no-filter option. To include some of these files, use the -- include option.
Important By default, the AMI bundling process creates a compressed, encrypted collection of files in the /tmp directory that represents your root volume. If you do not have enough free disk space in /tmp to store the bundle, you need to specify a different location for the bundle to be stored with the -d /path/to/bundle/storage option. Some instances have ephemeral storage mounted at /mnt or /media/ephemeral0 that you can use, or you can also create, attach, and mount a new Amazon EBS) volume to store the bundle. For more information, see Create an Amazon EBS volume in the Amazon EBS User Guide. a.
You must run the ec2-bundle-vol command as root. For most commands, you can use sudo to gain elevated permissions, but in this case, you should run sudo -E su to keep your environment variables.

[ec2-user ~]$ sudo -E su Note that bash prompt now identifies you as the root user, and that the dollar sign has been replaced by a hash tag, signalling that you are in a root shell:
[root ec2-user]# b.
To create the AMI bundle, run the ec2-bundle-vol command as follows:
[root ec2-user]# ec2-bundle-vol -k /tmp/cert/pk- HKZYKTAIG2ECMXYIBH3HXV4ZBEXAMPLE.pem -c /tmp/cert/cert- HKZYKTAIG2ECMXYIBH3HXV4ZBEXAMPLE.pem -u 123456789012 -r x86_64 -e /tmp/cert -- partition gpt Note For the China (Beijing) and AWS GovCloud (US-West) Regions, use the --ec2cert parameter and specify the certificates as per the prerequisites.
It can take a few minutes to create the image. When this command completes, your /tmp (or non-default) directory contains the bundle (image.manifest.xml, plus multiple image.part.xx files). c.
Exit from the root shell.
[root ec2-user]# exit
3. (Optional) To add more instance store volumes, edit the block device mappings in the image.manifest.xml file for your AMI. For more information, see Block device mappings for volumes on Amazon EC2 instances. a.
Create a backup of your image.manifest.xml file.
[ec2-user ~]$ sudo cp /tmp/image.manifest.xml /tmp/image.manifest.xml.bak b.
Reformat the image.manifest.xml file so that it is easier to read and edit.

[ec2-user ~]$ sudo xmllint --format /tmp/image.manifest.xml.bak > /tmp/ image.manifest.xml c.
Edit the block device mappings in image.manifest.xml with a text editor. The example below shows a new entry for the ephemeral1 instance store volume.
Note For a list of excluded files, see ec2-bundle-vol.
    <block_device_mapping>
      <mapping>
        <virtual>ami</virtual>
        <device>sda</device>
      </mapping>
      <mapping>
        <virtual>ephemeral0</virtual>
        <device>sdb</device>
      </mapping>
      <mapping>
        <virtual>ephemeral1</virtual>
        <device>sdc</device>
      </mapping>
      <mapping>
        <virtual>root</virtual>
        <device>/dev/sda1</device>
      </mapping>
    </block_device_mapping> d.
Save the image.manifest.xml file and exit your text editor.
4. To upload your bundle to Amazon S3, run the ec2-upload-bundle command as follows.
[ec2-user ~]$ ec2-upload-bundle -b amzn-s3-demo-bucket/bundle_folder/bundle_name - m /tmp/image.manifest.xml -a your_access_key_id -s your_secret_access_key

Important To register your AMI in a Region other than US East (N. Virginia), you must specify both the target Region with the --region option and a bucket path that already exists in the target Region or a unique bucket path that can be created in the target Region.
5. (Optional) After the bundle is uploaded to Amazon S3, you can remove the bundle from the / tmp directory on the instance using the following rm command:
[ec2-user ~]$ sudo rm /tmp/image.manifest.xml /tmp/image.part.* /tmp/image Important If you specified a path with the -d /path/to/bundle/storage option in Step 2, use that path instead of /tmp.
6. To register your AMI, run the register-image command as follows.
[ec2-user ~]$ aws ec2 register-image --image-location amzn-s3-demo- bucket/bundle_folder/bundle_name/image.manifest.xml --name AMI_name -- virtualization-type hvm Important If you previously specified a Region for the ec2-upload-bundle command, specify that Region again for this command.
### Set up the Amazon EC2 AMI tools You can use the AMI tools to create and manage Amazon S3-backed Linux AMIs. To use the tools, you must install them on your Linux instance. The AMI tools are available as both an RPM and as a .zip file for Linux distributions that don't support RPM.
To set up the AMI tools using the RPM
1. Install Ruby using the package manager for your Linux distribution, such as yum. For example:

[ec2-user ~]$ sudo yum install -y ruby
2. Download the RPM file using a tool such as wget or curl. For example:
[ec2-user ~]$ wget https://s3.amazonaws.com/ec2-downloads/ec2-ami-tools.noarch.rpm
3. Verify the RPM file's signature using the following command:
[ec2-user ~]$ rpm -K ec2-ami-tools.noarch.rpm The command above should indicate that the file's SHA1 and MD5 hashes are OK. If the command indicates that the hashes are NOT OK, use the following command to view the file's Header SHA1 and MD5 hashes:
[ec2-user ~]$ rpm -Kv ec2-ami-tools.noarch.rpm Then, compare your file's Header SHA1 and MD5 hashes with the following verified AMI tools hashes to confirm the file's authenticity:
- Header SHA1: a1f662d6f25f69871104e6a62187fa4df508f880
- MD5: 9faff05258064e2f7909b66142de6782 If your file's Header SHA1 and MD5 hashes match the verified AMI tools hashes, continue to the next step.
4. Install the RPM using the following command:
[ec2-user ~]$ sudo yum install ec2-ami-tools.noarch.rpm
5. Verify your AMI tools installation using the ec2-ami-tools-version command.
[ec2-user ~]$ ec2-ami-tools-version

Note If you receive a load error such as "cannot load such file -- ec2/amitools/version (LoadError)", complete the next step to add the location of your AMI tools installation to your RUBYLIB path.
6. (Optional) If you received an error in the previous step, add the location of your AMI tools installation to your RUBYLIB path. a.
Run the following command to determine the paths to add.
[ec2-user ~]$ rpm -qil ec2-ami-tools | grep ec2/amitools/version /usr/lib/ruby/site_ruby/ec2/amitools/version.rb /usr/lib64/ruby/site_ruby/ec2/amitools/version.rb In the above example, the missing file from the previous load error is located at /usr/ lib/ruby/site_ruby and /usr/lib64/ruby/site_ruby. b.
Add the locations from the previous step to your RUBYLIB path.
[ec2-user ~]$ export RUBYLIB=$RUBYLIB:/usr/lib/ruby/site_ruby:/usr/lib64/ruby/ site_ruby c.
Verify your AMI tools installation using the ec2-ami-tools-version command.
[ec2-user ~]$ ec2-ami-tools-version To set up the AMI tools using the .zip file
1. Install Ruby and unzip using the package manager for your Linux distribution, such as apt-get.
For example:
[ec2-user ~]$ sudo apt-get update -y && sudo apt-get install -y ruby unzip
2. Download the .zip file using a tool such as wget or curl. For example:
[ec2-user ~]$ wget https://s3.amazonaws.com/ec2-downloads/ec2-ami-tools.zip
3. Unzip the files into a suitable installation directory, such as /usr/local/ec2.

[ec2-user ~]$ sudo mkdir -p /usr/local/ec2 $ sudo unzip ec2-ami-tools.zip -d /usr/local/ec2 Notice that the .zip file contains a folder ec2-ami-tools-x.x.x, where x.x.x is the version number of the tools (for example, ec2-ami-tools-1.5.7).
4. Set the EC2_AMITOOL_HOME environment variable to the installation directory for the tools.
For example:
[ec2-user ~]$ export EC2_AMITOOL_HOME=/usr/local/ec2/ec2-ami-tools-x.x.x
5. Add the tools to your PATH environment variable. For example:
[ec2-user ~]$ export PATH=$EC2_AMITOOL_HOME/bin:$PATH
6. You can verify your AMI tools installation using the ec2-ami-tools-version command.
[ec2-user ~]$ ec2-ami-tools-version
#### Manage signing certificates Certain commands in the AMI tools require a signing certificate (also known as X.509 certificate).
You must create the certificate and then upload it to AWS. For example, you can use a third-party tool such as OpenSSL to create the certificate.
To create a signing certificate
1. Install and configure OpenSSL.
2. Create a private key using the openssl genrsa command and save the output to a .pem file.
We recommend that you create a 2048- or 4096-bit RSA key. openssl genrsa 2048 > private-key.pem
3. Generate a certificate using the openssl req command. openssl req -new -x509 -nodes -sha256 -days 365 -key private-key.pem -outform PEM - out certificate.pem

To upload the certificate to AWS, use the upload-signing-certificate command. aws iam upload-signing-certificate --user-name user-name --certificate-body file://path/to/certificate.pem To list the certificates for a user, use the list-signing-certificates command: aws iam list-signing-certificates --user-name user-name To disable or re-enable a signing certificate for a user, use the update-signing-certificate command.
The following command disables the certificate: aws iam update-signing-certificate --certificate-id OFHPLP4ZULTHYPMSYEX7O4BEXAMPLE -- status Inactive --user-name user-name To delete a certificate, use the delete-signing-certificate command: aws iam delete-signing-certificate --user-name user-name --certificate- id OFHPLP4ZULTHYPMSYEX7O4BEXAMPLE
### Amazon EC2 AMI tools reference You can use the AMI tools commands to create and manage Amazon S3-backed Linux AMIs. To set up the tools, see Set up the Amazon EC2 AMI tools.
For information about your access keys, see Managing access keys for IAM users in the IAM User Guide.
Commands
- ec2-ami-tools-version
- ec2-bundle-image
- ec2-bundle-vol
- ec2-delete-bundle
- ec2-download-bundle
- ec2-migrate-manifest
- ec2-unbundle
- ec2-upload-bundle

- Common options for AMI tools
#### ec2-ami-tools-version
##### Description Describes the version of the AMI tools.
##### Syntax ec2-ami-tools-version
##### Output The version information.
##### Example This example command displays the version information for the AMI tools that you're using.
[ec2-user ~]$ ec2-ami-tools-version 1.5.2 20071010
#### ec2-bundle-image
##### Description Creates an Amazon S3-backed Linux AMI from an operating system image created in a loopback file.
##### Syntax ec2-bundle-image -c path -k path -u account -i path [-d path] [--ec2cert path] [-r architecture] [--productcodes code1,code2,...] [-B mapping] [-p prefix]
##### Options -c, --cert path The user's PEM encoded RSA public key certificate file.

Required: Yes -k, --privatekey path The path to a PEM-encoded RSA key file. You'll need to specify this key to unbundle this bundle, so keep it in a safe place. Note that the key doesn't have to be registered to your AWS account.
Required: Yes -u, --user  account The user's AWS account ID, without dashes.
Required: Yes -i, --image path The path to the image to bundle.
Required: Yes -d, --destination path The directory in which to create the bundle.
Default: /tmp Required: No --ec2cert path The path to the Amazon EC2 X.509 public key certificate used to encrypt the image manifest.
The us-gov-west-1 and cn-north-1 Regions use a non-default public key certificate and the path to that certificate must be specified with this option. The path to the certificate varies based on the installation method of the AMI tools. For Amazon Linux, the certificates are located at /opt/aws/amitools/ec2/etc/ec2/amitools/. If you installed the AMI tools from the RPM or ZIP file in Set up the Amazon EC2 AMI tools, the certificates are located at $EC2_AMITOOL_HOME/etc/ec2/amitools/.
Required: Only for the us-gov-west-1 and cn-north-1 Regions.
-r, --arch architecture Image architecture. If you don't provide the architecture on the command line, you'll be prompted for it when bundling starts.

Valid values: i386 | x86_64 Required: No --productcodes code1,code2,...
Product codes to attach to the image at registration time, separated by commas.
Required: No -B, --block-device-mapping mapping Defines how block devices are exposed to an instance of this AMI if its instance type supports the specified device.
Specify a comma-separated list of key-value pairs, where each key is a virtual name and each value is the corresponding device name. Virtual names include the following:
- ami—The root file system device, as seen by the instance
- root—The root file system device, as seen by the kernel
- swap—The swap device, as seen by the instance
- ephemeralN—The Nth instance store volume Required: No -p, --prefix prefix The filename prefix for bundled AMI files.
Default: The name of the image file. For example, if the image path is /var/spool/my- image/version-2/debian.img, then the default prefix is debian.img.
Required: No --kernel kernel_id Deprecated. Use register-image to set the kernel.
Required: No --ramdisk ramdisk_id Deprecated. Use register-image to set the RAM disk if required.

Required: No
##### Output Status messages describing the stages and status of the bundling process.
##### Example This example creates a bundled AMI from an operating system image that was created in a loopback file.
[ec2-user ~]$ ec2-bundle-image -k pk-HKZYKTAIG2ECMXYIBH3HXV4ZBEXAMPLE.pem -c cert- HKZYKTAIG2ECMXYIBH3HXV4ZBEXAMPLE.pem -u 111122223333 -i image.img -d bundled/ -r x86_64 Please specify a value for arch [i386]:
Bundling image file...
Splitting bundled/image.gz.crypt...
Created image.part.00 Created image.part.01 Created image.part.02 Created image.part.03 Created image.part.04 Created image.part.05 Created image.part.06 Created image.part.07 Created image.part.08 Created image.part.09 Created image.part.10 Created image.part.11 Created image.part.12 Created image.part.13 Created image.part.14 Generating digests for each part...
Digests generated.
Creating bundle manifest... ec2-bundle-image complete.
#### ec2-bundle-vol
##### Description Creates an Amazon S3-backed Linux AMI by compressing, encrypting, and signing a copy of the root volume for the instance.

Amazon EC2 attempts to inherit product codes, kernel settings, RAM disk settings, and block device mappings from the instance.
By default, the bundle process excludes files that might contain sensitive information. These files include *.sw, *.swo, *.swp, *.pem, *.priv, *id_rsa*, *id_dsa* *.gpg, *.jks, */.ssh/ authorized_keys, and */.bash_history. To include all of these files, use the --no-filter option. To include some of these files, use the --include option.
For more information, see Create an Amazon S3-backed AMI.
##### Syntax ec2-bundle-vol -c path -k path -u account [-d path] [--ec2cert path] [- r architecture] [--productcodes code1,code2,...] [-B mapping] [--all] [-e directory1,directory2,...] [-i file1,file2,...] [--no-filter] [-p prefix]
[-s size] [--[no-]inherit] [-v volume] [-P type] [-S script] [--fstab path]
[--generate-fstab] [--grub-config path]
##### Options -c, --cert path The user's PEM encoded RSA public key certificate file.
Required: Yes -k, --privatekey  path The path to the user's PEM-encoded RSA key file.
Required: Yes -u, --user account The user's AWS account ID, without dashes.
Required: Yes -d, --destination destination The directory in which to create the bundle.
Default: /tmp

Required: No --ec2cert path The path to the Amazon EC2 X.509 public key certificate used to encrypt the image manifest.
The us-gov-west-1 and cn-north-1 Regions use a non-default public key certificate and the path to that certificate must be specified with this option. The path to the certificate varies based on the installation method of the AMI tools. For Amazon Linux, the certificates are located at /opt/aws/amitools/ec2/etc/ec2/amitools/. If you installed the AMI tools from the RPM or ZIP file in Set up the Amazon EC2 AMI tools, the certificates are located at $EC2_AMITOOL_HOME/etc/ec2/amitools/.
Required: Only for the us-gov-west-1 and cn-north-1 Regions.
-r, --arch  architecture The image architecture. If you don't provide this on the command line, you'll be prompted to provide it when the bundling starts.
Valid values: i386 | x86_64 Required: No --productcodes code1,code2,...
Product codes to attach to the image at registration time, separated by commas.
Required: No -B, --block-device-mapping mapping Defines how block devices are exposed to an instance of this AMI if its instance type supports the specified device.
Specify a comma-separated list of key-value pairs, where each key is a virtual name and each value is the corresponding device name. Virtual names include the following:
- ami—The root file system device, as seen by the instance
- root—The root file system device, as seen by the kernel
- swap—The swap device, as seen by the instance
- ephemeralN—The Nth instance store volume Required: No

-a, --all Bundle all directories, including those on remotely mounted file systems.
Required: No -e, --exclude  directory1,directory2,...
A list of absolute directory paths and files to exclude from the bundle operation. This parameter overrides the --all option. When exclude is specified, the directories and subdirectories listed with the parameter will not be bundled with the volume.
Required: No -i, --include  file1,file2,...
A list of files to include in the bundle operation. The specified files would otherwise be excluded from the AMI because they might contain sensitive information.
Required: No --no-filter If specified, we won't exclude files from the AMI because they might contain sensitive information.
Required: No -p, --prefix  prefix The file name prefix for bundled AMI files.
Default: image Required: No -s, --size size The size, in MB (1024 * 1024 bytes), of the image file to create. The maximum size is 10240 MB.
Default: 10240 Required: No --[no-]inherit Indicates whether the image should inherit the instance's metadata (the default is to inherit).
Bundling fails if you enable --inherit but the instance metadata is not accessible.

Required: No -v, --volume  volume The absolute path to the mounted volume from which to create the bundle.
Default: The root directory (/)
Required: No -P, --partition type Indicates whether the disk image should use a partition table. If you don't specify a partition table type, the default is the type used on the parent block device of the volume, if applicable, otherwise the default is gpt.
Valid values: mbr | gpt | none Required: No -S, --script script A customization script to be run right before bundling. The script must expect a single argument, the mount point of the volume.
Required: No --fstab path The path to the fstab to bundle into the image. If this is not specified, Amazon EC2 bundles / etc/fstab.
Required: No --generate-fstab Bundles the volume using an Amazon EC2-provided fstab.
Required: No --grub-config The path to an alternate grub configuration file to bundle into the image. By default, ec2- bundle-vol expects either /boot/grub/menu.lst or /boot/grub/grub.conf to exist on

the cloned image. This option allows you to specify a path to an alternative grub configuration file, which will then be copied over the defaults (if present).
Required: No --kernel kernel_id Deprecated. Use register-image to set the kernel.
Required: No --ramdiskramdisk_id Deprecated. Use register-image to set the RAM disk if required.
Required: No
##### Output Status messages describing the stages and status of the bundling.
##### Example This example creates a bundled AMI by compressing, encrypting and signing a snapshot of the local machine's root file system.
[ec2-user ~]$ ec2-bundle-vol -d /mnt -k pk-HKZYKTAIG2ECMXYIBH3HXV4ZBEXAMPLE.pem -c cert-HKZYKTAIG2ECMXYIBH3HXV4ZBEXAMPLE.pem -u 111122223333 -r x86_64 Copying / into the image file /mnt/image...
  Excluding: sys dev/shm proc dev/pts proc/sys/fs/binfmt_misc dev media mnt proc sys tmp/image mnt/img-mnt 1+0 records in 1+0 records out

  mke2fs 1.38 (30-Jun-2005) warning: 256 blocks unused.
  Splitting /mnt/image.gz.crypt...
  Created image.part.00 Created image.part.01 Created image.part.02 Created image.part.03 ...
  Created image.part.22 Created image.part.23 Generating digests for each part...
  Digests generated.
  Creating bundle manifest...
  Bundle Volume complete.
#### ec2-delete-bundle
##### Description Deletes the specified bundle from Amazon S3 storage. After you delete a bundle, you can't launch instances from the corresponding AMI.
##### Syntax ec2-delete-bundle -b bucket -a access_key_id -s secret_access_key [-t token] [--url url] [--region region] [--sigv version] [-m path] [-p prefix]
[--clear] [--retry] [-y]
##### Options -b, --bucket bucket The name of the Amazon S3 bucket containing the bundled AMI, followed by an optional '/'- delimited path prefix Required: Yes -a, --access-key access_key_id The AWS access key ID.
Required: Yes

-s, --secret-key secret_access_key The AWS secret access key.
Required: Yes -t, --delegation-token token The delegation token to pass along to the AWS request. For more information, see Temporary security credentials in the IAM User Guide.
Required: Only when you are using temporary security credentials.
Default: The value of the AWS_DELEGATION_TOKEN environment variable (if set).
--regionregion The Region to use in the request signature.
Default: us-east-1 Required: Required if using signature version 4 --sigvversion The signature version to use when signing the request.
Valid values: 2 | 4 Default: 4 Required: No -m, --manifestpath The path to the manifest file.
Required: You must specify --prefix or --manifest.
-p, --prefix prefix The bundled AMI filename prefix. Provide the entire prefix. For example, if the prefix is image.img, use -p image.img and not -p image.
Required: You must specify --prefix or --manifest.

--clear Deletes the Amazon S3 bucket if it's empty after deleting the specified bundle.
Required: No --retry Automatically retries on all Amazon S3 errors, up to five times per operation.
Required: No -y, --yes Automatically assumes the answer to all prompts is yes.
Required: No
##### Output Amazon EC2 displays status messages indicating the stages and status of the delete process.
##### Example This example deletes a bundle from Amazon S3.
[ec2-user ~]$ ec2-delete-bundle -b amzn-s3-demo-bucket -a your_access_key_id - s your_secret_access_key Deleting files: amzn-s3-demo-bucket/image.manifest.xml amzn-s3-demo-bucket/image.part.00 amzn-s3-demo-bucket/image.part.01 amzn-s3-demo-bucket/image.part.02 amzn-s3-demo-bucket/image.part.03 amzn-s3-demo-bucket/image.part.04 amzn-s3-demo-bucket/image.part.05 amzn-s3-demo-bucket/image.part.06 Continue? [y/n] y Deleted amzn-s3-demo-bucket/image.manifest.xml Deleted amzn-s3-demo-bucket/image.part.00 Deleted amzn-s3-demo-bucket/image.part.01 Deleted amzn-s3-demo-bucket/image.part.02

Deleted amzn-s3-demo-bucket/image.part.03 Deleted amzn-s3-demo-bucket/image.part.04 Deleted amzn-s3-demo-bucket/image.part.05 Deleted amzn-s3-demo-bucket/image.part.06 ec2-delete-bundle complete.
#### ec2-download-bundle
##### Description Downloads the specified Amazon S3-backed Linux AMIs from Amazon S3 storage.
##### Syntax ec2-download-bundle -b bucket -a access_key_id -s secret_access_key -k path [--url url] [--region region] [--sigv version] [-m file] [-p prefix] [-d directory] [--retry]
##### Options -b, --bucket bucket The name of the Amazon S3 bucket where the bundle is located, followed by an optional '/'- delimited path prefix.
Required: Yes -a, --access-key access_key_id The AWS access key ID.
Required: Yes -s, --secret-key secret_access_key The AWS secret access key.
Required: Yes -k, --privatekey path The private key used to decrypt the manifest.
Required: Yes

--url url The Amazon S3 service URL.
Default: https://s3.amazonaws.com/ Required: No --region region The Region to use in the request signature.
Default: us-east-1 Required: Required if using signature version 4 --sigv version The signature version to use when signing the request.
Valid values: 2 | 4 Default: 4 Required: No -m, --manifest file The name of the manifest file (without the path). We recommend that you specify either the manifest (-m) or a prefix (-p).
Required: No -p, --prefix  prefix The filename prefix for the bundled AMI files.
Default: image Required: No -d, --directory  directory The directory where the downloaded bundle is saved. The directory must exist.
Default: The current working directory.
Required: No

--retry Automatically retries on all Amazon S3 errors, up to five times per operation.
Required: No
##### Output Status messages indicating the various stages of the download process are displayed.
##### Example This example creates the bundled directory (using the Linux mkdir command) and downloads the bundle from the amzn-s3-demo-bucket Amazon S3 bucket.
[ec2-user ~]$ mkdir bundled [ec2-user ~]$ ec2-download-bundle -b amzn-s3-demo-bucket/bundles/bundle_name -m image.manifest.xml -a your_access_key_id -s your_secret_access_key -k pk- HKZYKTAIG2ECMXYIBH3HXV4ZBEXAMPLE.pem -d mybundle Downloading manifest image.manifest.xml from amzn-s3-demo-bucket to mybundle/ image.manifest.xml ...
Downloading part image.part.00 from amzn-s3-demo-bucket/bundles/bundle_name to mybundle/image.part.00 ...
Downloaded image.part.00 from amzn-s3-demo-bucket Downloading part image.part.01 from amzn-s3-demo-bucket/bundles/bundle_name to mybundle/image.part.01 ...
Downloaded image.part.01 from amzn-s3-demo-bucket Downloading part image.part.02 from amzn-s3-demo-bucket/bundles/bundle_name to mybundle/image.part.02 ...
Downloaded image.part.02 from amzn-s3-demo-bucket Downloading part image.part.03 from amzn-s3-demo-bucket/bundles/bundle_name to mybundle/image.part.03 ...
Downloaded image.part.03 from amzn-s3-demo-bucket Downloading part image.part.04 from amzn-s3-demo-bucket/bundles/bundle_name to mybundle/image.part.04 ...
Downloaded image.part.04 from amzn-s3-demo-bucket Downloading part image.part.05 from amzn-s3-demo-bucket/bundles/bundle_name to mybundle/image.part.05 ...
Downloaded image.part.05 from amzn-s3-demo-bucket Downloading part image.part.06 from amzn-s3-demo-bucket/bundles/bundle_name to mybundle/image.part.06 ...
Downloaded image.part.06 from amzn-s3-demo-bucket

#### ec2-migrate-manifest
##### Description Modifies an Amazon S3-backed Linux AMI (for example, its certificate, kernel, and RAM disk) so that it supports a different Region.
##### Syntax ec2-migrate-manifest -c path -k path -m path {(-a access_key_id - s secret_access_key --region region) | (--no-mapping)} [--ec2cert ec2_cert_path] [--kernel kernel-id] [--ramdisk ramdisk_id]
##### Options -c, --cert path The user's PEM encoded RSA public key certificate file.
Required: Yes -k, --privatekey path The path to the user's PEM-encoded RSA key file.
Required: Yes --manifest path The path to the manifest file.
Required: Yes -a, --access-key access_key_id The AWS access key ID.
Required: Required if using automatic mapping.
-s, --secret-key  secret_access_key The AWS secret access key.
Required: Required if using automatic mapping.
--region region The Region to look up in the mapping file.

Required: Required if using automatic mapping.
--no-mapping Disables automatic mapping of kernels and RAM disks.
During migration, Amazon EC2 replaces the kernel and RAM disk in the manifest file with a kernel and RAM disk designed for the destination region. Unless the --no-mapping parameter is given, ec2-migrate-bundle might use the DescribeRegions and DescribeImages operations to perform automated mappings.
Required: Required if you're not providing the -a, -s, and --region options used for automatic mapping.
--ec2cert path The path to the Amazon EC2 X.509 public key certificate used to encrypt the image manifest.
The us-gov-west-1 and cn-north-1 Regions use a non-default public key certificate and the path to that certificate must be specified with this option. The path to the certificate varies based on the installation method of the AMI tools. For Amazon Linux, the certificates are located at /opt/aws/amitools/ec2/etc/ec2/amitools/. If you installed the AMI tools from the ZIP file in Set up the Amazon EC2 AMI tools, the certificates are located at $EC2_AMITOOL_HOME/etc/ec2/amitools/.
Required: Only for the us-gov-west-1 and cn-north-1 Regions.
--kernel kernel_id The ID of the kernel to select.
Important We recommend that you use PV-GRUB instead of kernels and RAM disks. For more information, see User provided kernels in the Amazon Linux 2 User Guide.
Required: No --ramdisk ramdisk_id The ID of the RAM disk to select.

Important We recommend that you use PV-GRUB instead of kernels and RAM disks. For more information, see User provided kernels in the Amazon Linux 2 User Guide.
Required: No
##### Output Status messages describing the stages and status of the bundling process.
##### Example This example copies the AMI specified in the my-ami.manifest.xml manifest from the US to the EU.
[ec2-user ~]$ ec2-migrate-manifest --manifest my-ami.manifest.xml --cert cert-HKZYKTAIG2ECMXYIBH3HXV4ZBZQ55CLO.pem --privatekey pk- HKZYKTAIG2ECMXYIBH3HXV4ZBZQ55CLO.pem --region eu-west-1 Backing up manifest...
Successfully migrated my-ami.manifest.xml It is now suitable for use in eu-west-1.
#### ec2-unbundle
##### Description Re-creates the bundle from an Amazon S3-backed Linux AMI.
##### Syntax ec2-unbundle -k path -m path [-s source_directory] [-d destination_directory]
##### Options -k, --privatekey path The path to your PEM-encoded RSA key file.
Required: Yes

-m, --manifest path The path to the manifest file.
Required: Yes -s, --source source_directory The directory containing the bundle.
Default: The current directory.
Required: No -d, --destination destination_directory The directory in which to unbundle the AMI. The destination directory must exist.
Default: The current directory.
Required: No
##### Example This Linux and UNIX example unbundles the AMI specified in the image.manifest.xml file.
[ec2-user ~]$ mkdir unbundled $ ec2-unbundle -m mybundle/image.manifest.xml -k pk- HKZYKTAIG2ECMXYIBH3HXV4ZBEXAMPLE.pem -s mybundle -d unbundled $ ls -l unbundled total 1025008 -rw-r--r-- 1 root root 1048578048 Aug 25 23:46 image.img
##### Output Status messages indicating the various stages of the unbundling process are displayed.
#### ec2-upload-bundle
##### Description Uploads the bundle for an Amazon S3-backed Linux AMI to Amazon S3 and sets the appropriate access control lists (ACLs) on the uploaded objects. For more information, see Create an Amazon S3-backed AMI.

Note To upload objects to an S3 bucket for your Amazon S3-backed Linux AMI, ACLs must be enabled for the bucket. Otherwise, Amazon EC2 will not be able to set ACLs on the objects to upload. If your destination bucket uses the bucket owner enforced setting for S3 Object Ownership, this won't work because ACLs are disabled. For more information, see Controlling ownership of objects and disabling ACLs for your bucket.
##### Syntax ec2-upload-bundle -b bucket -a access_key_id -s secret_access_key [-t token] -m path [--url url] [--region region] [--sigv version] [--acl acl]
[-d directory] [--part part] [--retry] [--skipmanifest]
##### Options -b, --bucket bucket The name of the Amazon S3 bucket in which to store the bundle, followed by an optional '/'- delimited path prefix. If the bucket doesn't exist, it's created if the bucket name is available.
Additionally, if the bucket doesn't exist and the AMI tools version is 1.5.18 or later, this command sets the ACLs for the bucket.
Required: Yes -a, --access-key access_key_id Your AWS access key ID.
Required: Yes -s, --secret-key secret_access_key Your AWS secret access key.
Required: Yes -t, --delegation-token token The delegation token to pass along to the AWS request. For more information, see Temporary security credentials in the IAM User Guide.

Required: Only when you are using temporary security credentials.
Default: The value of the AWS_DELEGATION_TOKEN environment variable (if set).
-m, --manifest path The path to the manifest file. The manifest file is created during the bundling process and can be found in the directory containing the bundle.
Required: Yes --url url Deprecated. Use the --region option instead unless your bucket is constrained to the EU location (and not eu-west-1). The --location flag is the only way to target that specific location restraint.
The Amazon S3 endpoint service URL.
Default: https://s3.amazonaws.com/ Required: No --region region The Region to use in the request signature for the destination S3 bucket.
- If the bucket doesn't exist and you don't specify a Region, the tool creates the bucket without a location constraint (in us-east-1).
- If the bucket doesn't exist and you specify a Region, the tool creates the bucket in the specified Region.
- If the bucket exists and you don't specify a Region, the tool uses the bucket's location.
- If the bucket exists and you specify us-east-1 as the Region, the tool uses the bucket's actual location without any error message, any existing matching files are over-written.
- If the bucket exists and you specify a Region (other than us-east-1) that doesn't match the bucket's actual location, the tool exits with an error.
If your bucket is constrained to the EU location (and not eu-west-1), use the --location flag instead. The --location flag is the only way to target that specific location restraint.
Default: us-east-1

Required: Required if using signature version 4 --sigv version The signature version to use when signing the request.
Valid values: 2 | 4 Default: 4 Required: No --acl acl The access control list policy of the bundled image.
Valid values: public-read | aws-exec-read Default: aws-exec-read Required: No -d, --directory directory The directory containing the bundled AMI parts.
Default: The directory containing the manifest file (see the -m option).
Required: No --part part Starts uploading the specified part and all subsequent parts. For example, --part 04.
Required: No --retry Automatically retries on all Amazon S3 errors, up to five times per operation.
Required: No --skipmanifest Does not upload the manifest.

Required: No --location location Deprecated. Use the --region option instead, unless your bucket is constrained to the EU location (and not eu-west-1). The --location flag is the only way to target that specific location restraint.
The location constraint of the destination Amazon S3 bucket. If the bucket exists and you specify a location that doesn't match the bucket's actual location, the tool exits with an error.
If the bucket exists and you don't specify a location, the tool uses the bucket's location. If the bucket doesn't exist and you specify a location, the tool creates the bucket in the specified location. If the bucket doesn't exist and you don't specify a location, the tool creates the bucket without a location constraint (in us-east-1).
Default: If --region is specified, the location is set to that specified Region. If --region is not specified, the location defaults to us-east-1.
Required: No
##### Output Amazon EC2 displays status messages that indicate the stages and status of the upload process.
##### Example This example uploads the bundle specified by the image.manifest.xml manifest.
[ec2-user ~]$ ec2-upload-bundle -b amzn-s3-demo-bucket/bundles/bundle_name -m image.manifest.xml -a your_access_key_id -s your_secret_access_key Creating bucket...
Uploading bundled image parts to the S3 bucket amzn-s3-demo-bucket ...
Uploaded image.part.00 Uploaded image.part.01 Uploaded image.part.02 Uploaded image.part.03 Uploaded image.part.04 Uploaded image.part.05 Uploaded image.part.06 Uploaded image.part.07 Uploaded image.part.08

Uploaded image.part.09 Uploaded image.part.10 Uploaded image.part.11 Uploaded image.part.12 Uploaded image.part.13 Uploaded image.part.14 Uploading manifest ...
Uploaded manifest.
Bundle upload completed.
#### Common options for AMI tools Most of the AMI tools accept the following optional parameters.
--help, -h Displays the help message.
--version Displays the version and copyright notice.
--manual Displays the manual entry.
--batch Runs in batch mode, suppressing interactive prompts.
--debug Displays information that can be useful when troubleshooting problems.
### Convert your Amazon S3-backed AMI to an EBS-backed AMI You can convert an Amazon S3-backed Linux AMI that you own to an Amazon EBS-backed Linux AMI.
Important You can't convert an AMI that you don't own.

To convert an Amazon S3-backed AMI to an Amazon EBS-backed AMI
1. Launch an Amazon Linux instance from an Amazon EBS-backed AMI. For more information, see Launch an EC2 instance using the launch instance wizard in the console. Amazon Linux instances have the AWS CLI and AMI tools pre-installed.
2. Upload the X.509 private key that you used to bundle your Amazon S3-backed AMI to your instance. We use this key to ensure that only you and Amazon EC2 can access your AMI. a.
Create a temporary directory on your instance for your X.509 private key as follows:
[ec2-user ~]$ mkdir /tmp/cert b.
Copy your X.509 private key from your computer to the /tmp/cert directory on your instance, using a secure copy tool such as scp. The my-private-key parameter in the following command is the private key you use to connect to your instance with SSH. For example: you@your_computer:~ $ scp -i my-private-key.pem / path/to/pk-HKZYKTAIG2ECMXYIBH3HXV4ZBEXAMPLE.pem ec2- user@ec2-203-0-113-25.compute-1.amazonaws.com:/tmp/cert/ pk-HKZYKTAIG2ECMXYIBH3HXV4ZBEXAMPLE.pem  100%  717     0.7KB/s   00:00
3. Configure your environment variables to use the AWS CLI. For more information, see Environment variables. a.
(Recommended) Set environment variables for your AWS access key, secret key, and session token.
[ec2-user ~]$ export AWS_ACCESS_KEY_ID=your_access_key_id [ec2-user ~]$ export AWS_SECRET_ACCESS_KEY=your_secret_access_key [ec2-user ~]$ export AWS_SESSION_TOKEN=your_session_token b.
Set environment variables for your AWS access key, and secret key.
[ec2-user ~]$ export AWS_ACCESS_KEY_ID=your_access_key_id [ec2-user ~]$ export AWS_SECRET_ACCESS_KEY=your_secret_access_key
4. Prepare an Amazon Elastic Block Store (Amazon EBS) volume for your new AMI. a.
Create an empty EBS volume in the same Availability Zone as your instance using the create-volume command. Note the volume ID in the command output.

Important This EBS volume must be the same size or larger than the original instance store root volume. aws ec2 create-volume \ --size 10 \ --region us-west-2 \ --availability-zone us-west-2b b.
Attach the volume to your Amazon EBS-backed instance using the attach-volume command. aws ec2 attach-volume \ --volume-id vol-01234567890abcdef \ --instance-id i-1234567890abcdef0 \ --region us-west-2
5. Create a folder for your bundle.
[ec2-user ~]$ mkdir /tmp/bundle
6. Download the bundle for your instance store-based AMI to /tmp/bundle using the ec2- download-bundle command.
[ec2-user ~]$ ec2-download-bundle -b amzn-s3-demo-bucket/bundle_folder/bundle_name -m image.manifest.xml -a $AWS_ACCESS_KEY_ID -s $AWS_SECRET_ACCESS_KEY -- privatekey /path/to/pk-HKZYKTAIG2ECMXYIBH3HXV4ZBEXAMPLE.pem -d /tmp/bundle
7. Reconstitute the image file from the bundle using the ec2-unbundle command. a.
Change directories to the bundle folder.
[ec2-user ~]$ cd /tmp/bundle/ b.
Run the ec2-unbundle command.

[ec2-user bundle]$ ec2-unbundle -m image.manifest.xml --privatekey /path/to/pk- HKZYKTAIG2ECMXYIBH3HXV4ZBEXAMPLE.pem
8. Copy the files from the unbundled image to the new EBS volume.
[ec2-user bundle]$ sudo dd if=/tmp/bundle/image of=/dev/sdb bs=1M
9. Probe the volume for any new partitions that were unbundled.
[ec2-user bundle]$ sudo partprobe /dev/sdb1
10. List the block devices to find the device name to mount.
[ec2-user bundle]$ lsblk NAME         MAJ:MIN RM SIZE RO TYPE MOUNTPOINT /dev/sda    202:0    0   8G  0 disk
##/dev/sda1 202:1    0   8G  0 part / /dev/sdb    202:80   0  10G  0 disk
##/dev/sdb1 202:81   0  10G  0 part In this example, the partition to mount is /dev/sdb1, but your device name will likely be different. If your volume is not partitioned, then the device to mount will be similar to /dev/ sdb (without a device partition trailing digit).
11. Create a mount point for the new EBS volume and mount the volume.
[ec2-user bundle]$ sudo mkdir /mnt/ebs [ec2-user bundle]$ sudo mount /dev/sdb1 /mnt/ebs
12. Open the /etc/fstab file on the EBS volume with your favorite text editor (such as vim or nano) and remove any entries for instance store (ephemeral) volumes. Because the EBS volume is mounted on /mnt/ebs, the fstab file is located at /mnt/ebs/etc/fstab.
[ec2-user bundle]$ sudo nano /mnt/ebs/etc/fstab
# LABEL=/     /           ext4    defaults,noatime  1   1 tmpfs       /dev/shm    tmpfs   defaults        0   0 devpts      /dev/pts    devpts  gid=5,mode=620  0   0 sysfs       /sys        sysfs   defaults        0   0 proc        /proc       proc    defaults        0   0

/dev/sdb        /media/ephemeral0       auto    defaults,comment=cloudconfig    0 2 In this example, the last line should be removed.
13. Unmount the volume and detach it from the instance.
[ec2-user bundle]$ sudo umount /mnt/ebs [ec2-user bundle]$ aws ec2 detach-volume --volume-id vol-01234567890abcdef -- region us-west-2
14. Create an AMI from the new EBS volume as follows. a.
Create a snapshot of the new EBS volume.
[ec2-user bundle]$ aws ec2 create-snapshot --region us-west-2 --description "your_snapshot_description" --volume-id vol-01234567890abcdef b.
Check to see that your snapshot is complete.
[ec2-user bundle]$ aws ec2 describe-snapshots --region us-west-2 --snapshot- id snap-0abcdef1234567890 c.
Identify the processor architecture, virtualization type, and the kernel image (aki) used on the original AMI with the describe-images command. You need the AMI ID of the original Amazon S3-backed AMI for this step.
[ec2-user bundle]$ aws ec2 describe-images --region us-west-2 --image- id ami-0abcdef1234567890 --output text IMAGES x86_64 amazon/amzn-ami-pv-2013.09.2.x86_64-s3 ami-8ef297be amazon available public machine aki-fc8f11cc instance-store paravirtual xen In this example, the architecture is x86_64 and the kernel image ID is aki-fc8f11cc.
Use these values in the following step. If the output of the above command also lists an ari ID, take note of that as well. d.
Register your new AMI with the snapshot ID of your new EBS volume and the values from the previous step. If the previous command output listed an ari ID, include that in the following command with --ramdisk-id ari_id.
[ec2-user bundle]$ aws ec2 register-image --region us-west-2 -- name your_new_ami_name --block-device-mappings DeviceName=device-

name,Ebs={SnapshotId=snap-0abcdef1234567890} --virtualization-type paravirtual --architecture x86_64 --kernel-id aki-fc8f11cc --root-device-name device-name
15. (Optional) After you have tested that you can launch an instance from your new AMI, you can delete the EBS volume that you created for this procedure. aws ec2 delete-volume --volume-id vol-01234567890abcdef
## Create an Amazon EC2 AMI using Windows Sysprep The Microsoft System Preparation (Windows Sysprep) tool creates a generalized version of the operating system, with instance-specific system configuration removed before it captures a new image.
We recommend that you use EC2 Image Builder to automate the creation, management, and deployment of customized, secure, and up-to-date "golden" server images that are pre-installed and preconfigured with software and settings.
You can also use Windows Sysprep to create a standardized AMI using the Windows launch agents:
EC2Launch v2, EC2Launch, and EC2Config.
Important Do not use Windows Sysprep to create an instance backup. Windows Sysprep removes system-specific information; removing this information might have unintended consequences for an instance backup.
To troubleshoot Windows Sysprep, see Troubleshoot Sysprep issues with Amazon EC2 Windows instances.
Contents
- Windows Sysprep phases
- Before you begin
- Create an AMI using Windows Sysprep with EC2Launch v2
- Create an AMI using Windows Sysprep with EC2Launch
- Create an AMI using Windows Sysprep with EC2Config

### Windows Sysprep phases Windows Sysprep runs through the following phases:
- Generalize: The Sysprep tool removes image-specific information and configurations. For example, Windows Sysprep removes the security identifier (SID), the computer name, the event logs, and specific drivers, to name a few. After this phase is completed, the operating system (OS) is ready to create an AMI.
Note When you run Windows Sysprep with the Windows launch agents, the system prevents drivers from being removed because PersistAllDeviceInstalls is set to true by default.
- Specialize: Plug and Play scans the computer and installs drivers for any detected devices. The Sysprep tool generates OS requirements, like the computer name and SID. Optionally, you can run commands in this phase.
- Out-of-Box Experience (OOBE): The system runs an abbreviated version of Windows Setup and asks you to enter information such as system language, time zone, and registered organization.
When you run Windows Sysprep with Windows launch agents, the answer file automates this phase.
### Before you begin
- Before performing Windows Sysprep, we recommend that you remove all local user accounts and all account profiles other than a single administrator account under which Windows Sysprep will be run. If you perform Windows Sysprep with additional accounts and profiles, unexpected behavior could result, including loss of profile data or failure to complete Windows Sysprep.
- Learn more about Sysprep Overview.
- Learn which Sysprep Support for Server Roles.
### Create an AMI using Windows Sysprep with EC2Launch v2 When you create an image from an instance with the EC2Launch v2 agent installed, EC2Launch v2 performs specific tasks as the image is prepared. This includes working with Windows Sysprep. For more information, see the section called "Windows Sysprep phases".

Contents
- Windows Sysprep actions
- Post Sysprep
- Run Windows Sysprep with EC2Launch v2
#### Windows Sysprep actions Windows Sysprep and EC2Launch v2 perform the following actions when preparing an image.
1. When you choose Shutdown with Sysprep in the EC2Launch settings dialog box, the system runs the ec2launch sysprep command.
2. EC2Launch v2 edits the content of the unattend.xml file by reading the registry value at HKEY_USERS\.DEFAULT\Control Panel\International\LocaleName. This file is located in the following directory: C:\ProgramData\Amazon\EC2Launch\sysprep.
3. The system run the BeforeSysprep.cmd. This command creates a registry key as follows: reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 1 /f The registry key disables RDP connections until they are re-enabled. Disabling RDP connections is a necessary security measure because, during the first boot session after Windows Sysprep has run, there is a short period of time where RDP allows connections and the Administrator password is blank.
4. The EC2Launch v2 service calls Windows Sysprep by running the following command: sysprep.exe /oobe /generalize /shutdown /unattend: "C:\ProgramData\Amazon\EC2Launch \sysprep\unattend.xml"
##### Generalize phase
- EC2Launch v2 removes image-specific information and configurations, such as the computer name and the SID. If the instance is a member of a domain, it is removed from the domain. The unattend.xml answer file includes the following settings that affect this phase:
- PersistAllDeviceInstalls: This setting prevents Windows Setup from removing and reconfiguring devices, which speeds up the image preparation process because Amazon AMIs require certain drivers to run and re-detection of those drivers would take time.

- DoNotCleanUpNonPresentDevices: This setting retains Plug and Play information for devices that are not currently present.
- Windows Sysprep shuts down the OS as it prepares to create the AMI. The system either launches a new instance or starts the original instance.
##### Specialize phase The system generates OS-specific requirements, such as a computer name and an SID. The system also performs the following actions based on configurations that you specify in the unattend.xml answer file.
- CopyProfile: Windows Sysprep can be configured to delete all user profiles, including the built- in Administrator profile. This setting retains the built-in Administrator account so that any customizations you make to that account are carried over to the new image. The default value is True.
CopyProfile replaces the default profile with the existing local administrator profile. All accounts that you log in to after running Windows Sysprep receive a copy of that profile and its contents at first login.
If you don't have specific user-profile customizations that you want to carry over to the new image, then change this setting to False. Windows Sysprep will remove all user profiles (this saves time and disk space).
- TimeZone: The time zone is set to Coordinate Universal Time (UTC) by default.
- Synchronous command with order 1: The system runs the following command, which enables the administrator account and specifies the password requirement: net user Administrator /ACTIVE:YES /LOGONPASSWORDCHG:NO /EXPIRES:NEVER / PASSWORDREQ:YES
- Synchronous command with order 2: The system scrambles the administrator password. This security measure is designed to prevent the instance from being accessible after Windows Sysprep completes if you did not configure the setAdminAccount task.
The system runs the following command from your local launch agent directory (C:\Program Files\Amazon\EC2Launch\).

EC2Launch.exe internal randomize-password --username Administrator
- To enable remote desktop connections, the system sets the Terminal Server fDenyTSConnections registry key to false.
##### OOBE phase
1. The system specifies the following configurations using the EC2Launch v2 answer file:
- <InputLocale>en-US</InputLocale>
- <SystemLocale>en-US</SystemLocale>
- <UILanguage>en-US</UILanguage>
- <UserLocale>en-US</UserLocale>
- <HideEULAPage>true</HideEULAPage>
- <HideWirelessSetupInOOBE>true</HideWirelessSetupInOOBE>
- <ProtectYourPC>3</ProtectYourPC>
- <BluetoothTaskbarIconEnabled>false</BluetoothTaskbarIconEnabled>
- <TimeZone>UTC</TimeZone>
- <RegisteredOrganization>Amazon.com</RegisteredOrganization>
- <RegisteredOwner>EC2</RegisteredOwner>
Note During the generalize and specialize phases, EC2Launch v2 monitors the status of the OS. If EC2Launch v2 detects that the OS is in a Sysprep phase, then it publishes the following message to the system log:
Windows is being configured. SysprepState=IMAGE_STATE_UNDEPLOYABLE
2. The system runs EC2Launch v2.
#### Post Sysprep After Windows Sysprep completes, EC2Launch v2 sends the following message to the console output:

Windows sysprep configuration complete.
EC2Launch v2 then performs the following actions:
1. Reads the content of the agent-config.yml file and runs configured tasks.
2. Executes all tasks in the preReady stage.
3. After it is finished, sends a Windows is ready message to the instance system logs.
4. Executes all tasks in the PostReady stage.
For more information about EC2Launch v2 , see Use the EC2Launch v2 agent to perform tasks during EC2 Windows instance launch.
#### Run Windows Sysprep with EC2Launch v2 Use the following procedure to create a standardized AMI using Windows Sysprep with EC2Launch v2.
1. In the Amazon EC2 console, locate an AMI that you want to duplicate.
2. Launch and connect to your Windows instance.
3. Customize settings a.
From the Windows Start menu, search for and choose Amazon EC2Launch settings. For more information about the options and settings in the Amazon EC2Launch settings dialog box, see Configure EC2Launch v2 settings for Windows instances. b.
If you've made changes, choose Save before you shut down.
4. Choose Shutdown with Sysprep or Shutdown without Sysprep.
When you are asked to confirm that you want to run Windows Sysprep and shut down the instance, click Yes. EC2Launch v2 runs Windows Sysprep. Next, you are logged off the instance, and the instance shuts down. If you check the Instances page in the Amazon EC2 console, the instance state changes from Running to Stopping to Stopped. At this point, it's safe to create an AMI from this instance.
You can manually invoke the Windows Sysprep tool from the command line using the following command:

"%programfiles%\amazon\ec2launch\ec2launch.exe" sysprep --shutdown=true
### Create an AMI using Windows Sysprep with EC2Launch When you create an image from an instance with the EC2Launch agent installed, EC2Launch performs specific tasks as the image is prepared. This includes working with Windows Sysprep. For more information, see the section called "Windows Sysprep phases".
EC2Launch offers a default answer file and batch files for Windows Sysprep that automate and secure the image-preparation process on your AMI. Modifying these files is optional. These files are located in the following directory by default: C:\ProgramData\Amazon\EC2-Windows\Launch \Sysprep.
Important Do not use Windows Sysprep to create an instance backup. Windows Sysprep removes system-specific information. If you remove this information there might be unintended consequences for an instance backup.
Contents
- EC2Launch answer and batch files for Windows Sysprep
- Run Windows Sysprep with EC2Launch
- Update metadata/KMS routes for Server 2016 and later when launching a custom AMI
#### EC2Launch answer and batch files for Windows Sysprep The EC2Launch answer file and batch files for Windows Sysprep include the following:
Unattend.xml This is the default answer file. If you run SysprepInstance.ps1 or choose ShutdownWithSysprep in the user interface, the system reads the setting from this file.
BeforeSysprep.cmd Customize this batch file to run commands before EC2Launch runs Windows Sysprep.

SysprepSpecialize.cmd Customize this batch file to run commands during the Windows Sysprep specialize phase.
#### Run Windows Sysprep with EC2Launch On the full installation of Windows Server 2016 and later (with a desktop experience), you can run Windows Sysprep with EC2Launch manually or by using the EC2 Launch Settings application.
To run Windows Sysprep using the EC2Launch Settings application
1. In the Amazon EC2 console, locate or create a Windows Server 2016 or later AMI.
2. Launch a Windows instance from the AMI.
3. Connect to your Windows instance and customize it.
4. Search for and run the EC2LaunchSettings application. It is located in the following directory by default: C:\ProgramData\Amazon\EC2-Windows\Launch\Settings.

5. Select or clear options as needed. These settings are stored in the LaunchConfig.json file.
6. For Administrator Password, do one of the following:

- Choose Random. EC2Launch generates a password and encrypts it using the user's key. The system disables this setting after the instance is launched so that this password persists if the instance is rebooted or stopped and started.
- Choose Specify and type a password that meets the system requirements. The password is stored in LaunchConfig.json as clear text and is deleted after Windows Sysprep sets the administrator password. If you shut down now, the password is set immediately. EC2Launch encrypts the password using the user's key.
- Choose DoNothing and specify a password in the unattend.xml file. If you don't specify a password in unattend.xml, the administrator account is disabled.
7. Choose Shutdown with Sysprep.
To manually run Windows Sysprep using EC2Launch
1. In the Amazon EC2 console locate or create a Windows Server 2016 or later Datacenter edition AMI that you want to duplicate.
2. Launch and connect to your Windows instance.
3. Customize the instance.
4. Specify settings in the LaunchConfig.json file. This file is located in the C:\ProgramData \Amazon\EC2-Windows\Launch\Config directory by default.
For adminPasswordType, specify one of the following values:
Random EC2Launch generates a password and encrypts it using the user's key. The system disables this setting after the instance is launched so that this password persists if the instance is rebooted or stopped and started.
Specify EC2Launch uses the password you specify in adminPassword. If the password does not meet the system requirements, EC2Lauch generates a random password instead. The password is stored in LaunchConfig.json as clear text and is deleted after Windows Sysprep sets the administrator password. EC2Launch encrypts the password using the user's key.

DoNothing EC2Launch uses the password you specify in the unattend.xml file. If you don't specify a password in unattend.xml, the administrator account is disabled.
5. (Optional) Specify settings in unattend.xml and other configuration files. If plan to attend to the installation, then you don't need to make changes in these files. The files are located in the following directory by default: C:\ProgramData\Amazon\EC2-Windows\Launch \Sysprep.
6. In Windows PowerShell, run ./InitializeInstance.ps1 -Schedule. The script is located in the following directory, by default: C:\ProgramData\Amazon\EC2-Windows\Launch \Scripts. This script schedules the instance to initialize during the next boot. You must run this script before you run the SysprepInstance.ps1 script in the next step.
7. In Windows PowerShell, run ./SysprepInstance.ps1. The script is located in the following directory by default: C:\ProgramData\Amazon\EC2-Windows\Launch\Scripts.
You are logged off the instance and the instance shuts down. If you check the Instances page in the Amazon EC2 console, the instance state changes from Running to Stopping, and then to Stopped. At this point, it is safe to create an AMI from this instance.
#### Update metadata/KMS routes for Server 2016 and later when launching a custom AMI To update metadata/KMS routes for Server 2016 and later when launching a custom AMI, do one of the following:
- Run the EC2LaunchSettings GUI (C:\ProgramData\Amazon\EC2-Windows\Launch\Settings \Ec2LaunchSettings.exe) and select the option to shut down with Windows Sysprep.
- Run EC2LaunchSettings and shut down without Windows Sysprep before creating the AMI. This sets the EC2 Launch Initialize tasks to run at the next boot, which will set routes based on the subnet for the instance.
- Manually reschedule EC2 Launch initialize tasks before creating an AMI from PowerShell.
Important Take note of the default password reset behavior before rescheduling tasks.
- To update the routes on a running instance that is experiencing Windows activation or communication with instance metadata failures, see "Unable to activate Windows".

### Create an AMI using Windows Sysprep with EC2Config When you create an image from an instance with the EC2Config service installed, EC2Config performs specific tasks as the image is prepared. This includes working with Windows Sysprep. For more information, see the section called "Windows Sysprep phases".
Contents
- Windows Sysprep actions
- Post Sysprep
- Run Windows Sysprep with the EC2Config service
#### Windows Sysprep actions Windows Sysprep and the EC2Config service perform the following actions when preparing an image.
1. When you choose Shutdown with Sysprep in the EC2 Service Properties dialog box, the system runs the ec2config.exe -sysprep command.
2. The EC2Config service reads the content of the BundleConfig.xml file. This file is located in the following directory, by default: C:\Program Files\Amazon\Ec2ConfigService \Settings.
The BundleConfig.xml file includes the following settings. You can change these settings:
- AutoSysprep: Indicates whether to use Windows Sysprep automatically. You do not need to change this value if you are running Windows Sysprep from the EC2 Service Properties dialog box. The default value is No.
- SetRDPCertificate: Sets a self-signed certificate for the Remote Desktop server. This enables you to securely use the Remote Desktop Protocol (RDP) to connect to the instance. Change the value to Yes if new instances should use a certificate. This setting is not used with Windows Server 2012 instances because these operating systems can generate their own certificates.
The default value is No.
- SetPasswordAfterSysprep: Sets a random password on a newly launched instance, encrypts it with the user launch key, and outputs the encrypted password to the console. Change the value to No if new instances should not be set to a random encrypted password. The default value is Yes.

- PreSysprepRunCmd: The location of the command to run. The command is located in the following directory, by default: C:\Program Files\Amazon\Ec2ConfigService \Scripts\BeforeSysprep.cmd
3. The system runs BeforeSysprep.cmd. This command creates a registry key as follows: reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 1 /f The registry key disables RDP connections until they are re-enabled. Disabling RDP connections is a necessary security measure because, during the first boot session after Windows Sysprep has run, there is a short period of time where RDP allows connections and the Administrator password is blank.
4. The EC2Config service calls Windows Sysprep by running the following command: sysprep.exe /unattend: "C:\Program Files\Amazon\Ec2ConfigService\sysprep2008.xml" / oobe /generalize /shutdown
##### Generalize phase
- The tool removes image-specific information and configurations such as the computer name and the SID. If the instance is a member of a domain, it is removed from the domain. The sysprep2008.xml answer file includes the following settings that affect this phase:
- PersistAllDeviceInstalls: This setting prevents Windows Setup from removing and reconfiguring devices, which speeds up the image preparation process because Amazon AMIs require certain drivers to run and re-detection of those drivers would take time.
- DoNotCleanUpNonPresentDevices: This setting retains Plug and Play information for devices that are not currently present.
- Windows Sysprep shuts down the OS as it prepares to create the AMI. The system either launches a new instance or starts the original instance.
##### Specialize phase The system generates OS specific requirements such as a computer name and a SID. The system also performs the following actions based on configurations that you specify in the sysprep2008.xml answer file.

- CopyProfile: Windows Sysprep can be configured to delete all user profiles, including the built- in Administrator profile. This setting retains the built-in Administrator account so that any customizations you made to that account are carried over to the new image. The default value is True.
CopyProfile replaces the default profile with the existing local administrator profile. All accounts logged into after running Windows Sysprep will receive a copy of that profile and its contents at first login.
If you don't have specific user-profile customizations that you want to carry over to the new image then change this setting to False. Windows Sysprep will remove all user profiles; this saves time and disk space.
- TimeZone: The time zone is set to Coordinate Universal Time (UTC) by default.
- Synchronous command with order 1: The system runs the following command that enables the administrator account and specifies the password requirement. net user Administrator /ACTIVE:YES /LOGONPASSWORDCHG:NO /EXPIRES:NEVER / PASSWORDREQ:YES
- Synchronous command with order 2: The system scrambles the administrator password. This security measure is designed to prevent the instance from being accessible after Windows Sysprep completes if you did not enable the ec2setpassword setting.
C:\Program Files\Amazon\Ec2ConfigService\ScramblePassword.exe" -u Administrator
- Synchronous command with order 3: The system runs the following command:
C:\Program Files\Amazon\Ec2ConfigService\Scripts\SysprepSpecializePhase.cmd This command adds the following registry key, which re-enables RDP: reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 0 /f
##### OOBE phase
1. Using the EC2Config service answer file, the system specifies the following configurations:
- <InputLocale>en-US</InputLocale>
- <SystemLocale>en-US</SystemLocale>

- <UILanguage>en-US</UILanguage>
- <UserLocale>en-US</UserLocale>
- <HideEULAPage>true</HideEULAPage>
- <HideWirelessSetupInOOBE>true</HideWirelessSetupInOOBE>
- <NetworkLocation>Other</NetworkLocation>
- <ProtectYourPC>3</ProtectYourPC>
- <BluetoothTaskbarIconEnabled>false</BluetoothTaskbarIconEnabled>
- <TimeZone>UTC</TimeZone>
- <RegisteredOrganization>Amazon.com</RegisteredOrganization>
- <RegisteredOwner>Amazon</RegisteredOwner>
Note During the generalize and specialize phases the EC2Config service monitors the status of the OS. If EC2Config detects that the OS is in a Sysprep phase, then it publishes the following message to the system log:
EC2ConfigMonitorState: 0 Windows is being configured.
SysprepState=IMAGE_STATE_UNDEPLOYABLE
2. After the OOBE phase completes, the system runs SetupComplete.cmd from the following location: C:\Windows\Setup\Scripts\SetupComplete.cmd. In Amazon public AMIs before April 2015 this file was empty and ran nothing on the image. In public AMIs dated after April 2015, the file includes the following value: call "C:\Program Files\Amazon\Ec2ConfigService \Scripts\PostSysprep.cmd".
3. The system runs PostSysprep.cmd, which performs the following operations:
- Sets the local Administrator password to not expire. If the password expired, Administrators might not be able to log on.
- Sets the MSSQLServer machine name (if installed) so that the name will be in sync with the AMI.
#### Post Sysprep After Windows Sysprep completes, the EC2Config services sends the following message to the console output:

Windows sysprep configuration complete.
   Message: Sysprep Start Message: Sysprep End EC2Config then performs the following actions:
1. Reads the content of the config.xml file and lists all enabled plug-ins.
2. Executes all "Before Windows is ready" plug-ins at the same time.
- Ec2SetPassword
- Ec2SetComputerName
- Ec2InitializeDrives
- Ec2EventLog
- Ec2ConfigureRDP
- Ec2OutputRDPCert
- Ec2SetDriveLetter
- Ec2WindowsActivate
- Ec2DynamicBootVolumeSize
3. After it is finished, sends a "Windows is ready" message to the instance system logs.
4. Runs all "After Windows is ready" plug-ins at the same time.
- Amazon CloudWatch Logs
- UserData
- AWS Systems Manager (Systems Manager)
For more information about Windows plug-ins, see Use the EC2Config service to perform tasks during EC2 legacy Windows operating system instance launch.
#### Run Windows Sysprep with the EC2Config service Use the following procedure to create a standardized AMI using Windows Sysprep and the EC2Config service.
1. In the Amazon EC2 console, locate or create an AMI that you want to duplicate.
2. Launch and connect to your Windows instance.
3. Customize it.

4. Specify configuration settings in the EC2Config service answer file:
C:\Program Files\Amazon\Ec2ConfigService\sysprep2008.xml
5. From the Windows Start menu, choose All Programs, and then choose EC2ConfigService Settings.
6. Choose the Image tab in the Ec2 Service Properties dialog box. For more information about the options and settings in the Ec2 Service Properties dialog box, see Ec2 Service Properties.
7. Select an option for the Administrator password, and then select Shutdown with Sysprep or Shutdown without Sysprep. EC2Config edits the settings files based on the password option that you selected.
- Random: EC2Config generates a password, encrypts it with user's key, and displays the encrypted password to the console. We disable this setting after the first launch so that this password persists if the instance is rebooted or stopped and started.
- Specify: The password is stored in the Windows Sysprep answer file in unencrypted form (clear text). When Windows Sysprep runs next, it sets the Administrator password. If you shut down now, the password is set immediately. When the service starts again, the Administrator password is removed. It's important to remember this password, as you can't retrieve it later.
- Keep Existing: The existing password for the Administrator account doesn't change when Windows Sysprep is run or EC2Config is restarted. It's important to remember this password, as you can't retrieve it later.
8. Choose OK.
When you are asked to confirm that you want to run Windows Sysprep and shut down the instance, click Yes. You'll notice that EC2Config runs Windows Sysprep. Next, you are logged off the instance, and the instance is shut down. If you check the Instances page in the Amazon EC2 console, the instance state changes from Running to Stopping, and then finally to Stopped. At this point, it's safe to create an AMI from this instance.
You can manually invoke the Windows Sysprep tool from the command line using the following command:
"%programfiles%\amazon\ec2configservice\"ec2config.exe -sysprep""

Note The double quotation marks in the command are not required if your CMD shell is already in the C:\Program Files\Amazon\EC2ConfigService\ directory.
However, you must be very careful that the XML file options specified in the Ec2ConfigService \Settings folder are correct; otherwise, you might not be able to connect to the instance.
For more information about the settings files, see EC2Config settings files. For an example of configuring and then running Windows Sysprep from the command line, see Ec2ConfigService \Scripts\InstallUpdates.ps1.
## Copy an Amazon EC2 AMI When you need a consistent Amazon EC2 instance configuration across multiple Regions, you can use a single Amazon Machine Image (AMI) as your template to launch all the instances. However, AMIs are Region-specific resources—to launch an instance in a specific AWS Region, the AMI must be located in that Region. Therefore, to use the same AMI in multiple Regions, you must copy it from the source Region to each target Region.
The method you use to copy an AMI depends on whether you're copying across Regions within the same partition or across different partitions:
- Cross-Region copying – Copy AMIs across Regions within the same partition, for example, across the Regions within the commercial partition. This copy method is described in this topic.
- Cross-partition copying – Copy AMIs from one partition to another partition, for example, from the commercial partition to the AWS GovCloud (US) partition. For information about this copy method, see Store and restore an AMI.
- Cross-account copying – Create a copy of an AMI that another AWS account has shared with your AWS account. This copy method is described in this topic.
The time taken to complete the copy operation for cross-Region and cross-account AMI copying is on a best-effort basis. If you need control over the completion time, you can specify a completion window ranging from 15 minutes to 48 hours, ensuring your AMI is copied within your required timeframe. Additional charges apply for time-based AMI copy operations. For more information, see Time-based copies in the Amazon EBS User Guide.
Contents

- Considerations
- Costs
- Grant permissions to copy Amazon EC2 AMIs
- Copy an AMI
- Stop a pending AMI copy operation
- How Amazon EC2 AMI copy works
### Considerations
- Permission to copy AMIs – You can use IAM policies to grant or deny users permission to copy AMIs. Starting October 28, 2024, you can specify resource-level permissions for the CopyImage action on the source AMI. Resource-level permissions for the new AMI are available as before.
- Launch permissions and Amazon S3 bucket permissions – AWS does not copy launch permissions or Amazon S3 bucket permissions from the source AMI to the new AMI. After the copy operation is complete, you can apply launch permissions and Amazon S3 bucket permissions to the new AMI.
- Tags – You can only copy user-defined AMI tags that you attached to the source AMI. System tags (prefixed with aws:) and user-defined tags that are attached by other AWS accounts will not be copied. When copying an AMI, you can attach new tags to the new AMI and its backing snapshots.
- Quotas for time-based AMI copies – After you reach your cumulative snapshot copy throughput quota, subsequent time-based AMI copy requests fail. For more information, see Quotas for time- based copies in the Amazon EBS User Guide.
- Supported source-destination copies – The location of the source AMI determines whether you can copy it and the allowed destinations for the new AMI:
- If the source AMI is in a Region, you can copy it within that Region, to another Region, to an Outpost associated with that Region, or to a Local Zone in that Region.
- If the source AMI is in a Local Zone, you can copy it within that Local Zone, to the parent Region of that Local Zone, or to certain other Local Zones with the same parent Region.
- If the source AMI is on an Outpost, you can't copy it.
- CLI parameters for source and destination – When using the CLI, the following parameters are supported for specifying the source location of the AMI to copy and the destination of the new AMI. Note that the copy operation must be initiated in the destination Region; if you omit the

--region parameter, the destination assumes the default Region configured in your AWS CLI settings.
Source to destination Source parameter Destination parameter Region to Region --source-region --region Region to Outpost --source-region --destination-outp ost-arn  (the ARN of the Outpost)
Region to Local Zone --source-region Must be the parent Region of the Local Zone.
--destination-avai lability-zone (the name of the Local Zone) or --destination-avai lability-zone-id (the ID of  the Local Zone)
Local Zone to Region --source-region Must be the parent Region of the Local Zone.
The source Local Zone is assumed from the location of the  specified source AMI ID.
--region Must be the parent Region of the Local Zone.
Local Zone to Local Zone --source-region Must be the parent Region  o f the Local Zone.
The source Local Zone is assumed from the location of the specified source AMI  ID.
--destination-avai lability-zone (the name of the Local Zone) or --destination-avai lability-zone-id (the ID of  the Local Zone)

### Costs There is no charge for copying an AMI when no completion time is specified. However, additional charges apply for time-based AMI copy operations. For more information, see Time-based copies in the Amazon EBS User Guide.
Standard storage and data transfer rates apply. If you copy an EBS-backed AMI, you will incur charges for the storage of any additional EBS snapshots.
### Grant permissions to copy Amazon EC2 AMIs To copy an EBS-backed or Amazon S3-backed AMI, you need the following IAM permissions:
- ec2:CopyImage – To copy the AMI. For EBS-backed AMIs, it also grants permission to copy the AMI's backing snapshots.
- ec2:CreateTags – To tag the target AMI. For EBS-backed AMIs, it also grants permission to tag the target AMI's backing snapshots.
If you're copying an instance stored-backed AMI, you need the following additional IAM permissions:
- s3:CreateBucket – To create the S3 bucket in the target Region for the new AMI
- s3:PutBucketOwnershipControls – To enable ACLs for the newly created S3 bucket so that objects can be written with the aws-exec-read canned ACL
- s3:GetBucketAcl – To read the ACLs for the source bucket
- s3:ListAllMyBuckets – To find an existing S3 bucket for AMIs in the target Region
- s3:GetObject – To read the objects in the source bucket
- s3:PutObject – To write the objects in the target bucket
- s3:PutObjectAcl – To write the permissions for the new objects in the target bucket Note Starting October 28, 2024, you can specify resource-level permissions for the CopyImage action on the source AMI. Resource-level permissions for the target AMI are available as before. For more information, see CopyImage in the table under Actions defined by Amazon EC2 in the Service Authorization Reference.

#### Example IAM policy for copying an EBS-backed AMI and tagging the target AMI and snapshots The following example policy grants you permission to copy any EBS-backed AMI and tag the target AMI and its backing snapshots.
Note Starting October 28, 2024, you can specify snapshots in the Resource element. For more information, see CopyImage in the table under Actions defined by Amazon EC2 in the Service Authorization Reference.
JSON { "Version":"2012-10-17", "Statement": [{ "Sid": "PermissionToCopyAllImages", "Effect": "Allow", "Action": [ "ec2:CopyImage", "ec2:CreateTags"
        ], "Resource": [ "arn:aws:ec2:*::image/*", "arn:aws:ec2:*::snapshot/*"
        ]
    }]
}
#### Example IAM policy for copying an EBS-backed AMI but denying tagging the new snapshots The ec2:CopySnapshot permission is automatically granted when you get the ec2:CopyImage permission. Permission to tag the new backing snapshots can be explicitly denied, overriding the Allow effect for the ec2:CreateTags action.
The following example policy grants you permission to copy any EBS-backed AMI, but denies you from tagging the new backing snapshots of the target AMI.

JSON { "Version":"2012-10-17", "Statement": [{ "Effect": "Allow", "Action": [ "ec2:CopyImage", "ec2:CreateTags"
            ], "Resource": [ "arn:aws:ec2:*::image/*", "arn:aws:ec2:*::snapshot/*"
            ]
        }, { "Effect": "Deny", "Action": "ec2:CreateTags", "Resource": "arn:aws:ec2:::snapshot/*"
        } ]
}
#### Example IAM policy for copying an Amazon S3-backed AMI and tagging the target AMI The following example policy grants you permission to copy any Amazon S3-backed AMI in the specified source bucket to the specified Region, and tag the target AMI.
JSON { "Version":"2012-10-17", "Statement": [{ "Sid": "PermissionToCopyAllImages", "Effect": "Allow", "Action": [ "ec2:CopyImage", "ec2:CreateTags"
            ], "Resource": "arn:aws:ec2:*::image/*"
        },

        { "Effect": "Allow", "Action": "s3:ListAllMyBuckets", "Resource": [ "arn:aws:s3:::*"
            ]
        }, { "Effect": "Allow", "Action": "s3:GetObject", "Resource": [ "arn:aws:s3:::amzn-s3-demo-source-bucket/*"
            ]
        }, { "Effect": "Allow", "Action": [ "s3:CreateBucket", "s3:GetBucketAcl", "s3:PutObjectAcl", "s3:PutObject"
            ], "Resource": [ "arn:aws:s3:::amis-for-111122223333-in-us-east-2-hash"
            ]
        } ]
} To find the Amazon Resource Name (ARN) of the AMI source bucket, open the Amazon EC2 console at https://console.aws.amazon.com/ec2/, in the navigation pane choose AMIs, and locate the bucket name in the Source column.
Note The s3:CreateBucket permission is only needed the first time that you copy an Amazon S3-backed AMI to an individual Region. After that, the Amazon S3 bucket that is already created in the Region is used to store all future AMIs that you copy to that Region.

### Copy an AMI You can copy an AMI that you own or an AMI that was shared with you from another account. For the supported source and destination combinations, see Considerations.
Console To copy an AMI
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. From the console navigation bar, select the Region that contains the AMI.
3. In the navigation pane, choose AMIs to display the list of AMIs available to you in the Region.
4. If you don't see the AMI you want to copy, choose a different filter. You can filter by AMIs Owned by me, Private images, Public images, and Disabled images.
5. Select the AMI to copy, and then choose Actions, Copy AMI.
6. On the Copy Amazon Machine Image (AMI) page, specify the following information: a.
AMI copy name: A name for the new AMI. You can include the operating system information in the name because Amazon EC2 does not provide this information when displaying details about the AMI. b.
AMI copy description: By default, the description includes information about the source AMI so that you can distinguish a copy from its original. You can change this description as needed. c.
Destination Region: The Region in which to copy the AMI. For more information, see Cross-Region copying and Cross-account copying. d.
Copy tags: Select this checkbox to include your user-defined AMI tags when copying the AMI. System tags (prefixed with aws:) and user-defined tags that are attached by other AWS accounts will not be copied. e.
Time-based copy: You can specify whether the copy operation completes within a specific timeframe or on a best-effort basis, as follows:
- To complete the copy within a specific timeframe:
- Select Enable time-based copy.

- For Completion duration, enter the number of minutes (in 15-minute increments) allowed for the copy operation. The completion duration applies to all snapshots associated with the AMI.
For more information, see Time-based copies in the Amazon EBS User Guide.
- To complete the copy on a best-effort basis:
- Leave Enable time-based copy unselected. f.
(EBS-backed AMIs only) Encrypt EBS snapshots of AMI copy: Select this checkbox to encrypt the target snapshots, or to re-encrypt them using a different key. If encryption by default is enabled, the Encrypt EBS snapshots of AMI copy checkbox is selected and cannot be cleared. For more information, see Encryption and copying. g.
(EBS-backed AMIs only) KMS key: The KMS key to used to encrypt the target snapshots. h.
Tags: You can tag the new AMI and the new snapshots with the same tags, or you can tag them with different tags.
- To tag the new AMI and the new snapshots with the same tags, choose Tag image and snapshots together. The same tags are applied to the new AMI and every snapshot that is created.
- To tag the new AMI and the new snapshots with different tags, choose Tag image and snapshots separately. Different tags are applied to the new AMI and the snapshots that are created. Note, however, that all the new snapshots that are created get the same tags; you can't tag each new snapshot with a different tag.
To add a tag, choose Add tag, and enter the key and value for the tag. Repeat for each tag. i.
When you're ready to copy the AMI, choose Copy AMI.
The initial status of the new AMI is Pending. The AMI copy operation is complete when the status is Available.
AWS CLI To copy an AMI from one Region to another Region

Use the copy-image command. You must specify both the source and destination Regions.
You specify the source Region using the --source-region parameter. You can specify the destination Region using the --region parameter (or omit this parameter to assume the default Region configured in your AWS CLI settings). aws ec2 copy-image \ --source-image-id ami-0abcdef1234567890 \ --source-region us-west-2 \ --name my-ami \ --region us-east-1 When you encrypt a target snapshot during AMI copy, you must specify these additional parameters: --encrypted and --kms-key-id.
To copy an AMI from a Region to a Local Zone Use the copy-image command. You must specify both the source and destination. You specify the source Region using the --source-region parameter. You specify the destination Local Zone using the --destination-availability-zone parameter (you can use -- destination-availability-zone-id instead). Note that you can only copy an AMI from a Region to a Local Zone within that same Region. aws ec2 copy-image \ --source-image-id ami-0abcdef1234567890 \ --source-region cn-north-1 \ --destination-availability-zone cn-north-1-pkx-1a \ --name my-ami \ --region cn-north-1 To copy an AMI from a Local Zone to a Region Use the copy-image command. You must specify both the source and destination. You specify the source Region using the --source-region parameter. You specify the destination Region using the --region parameter (or omit this parameter to assume the default Region configured in your AWS CLI settings). The source Local Zone is assumed from the location of the specified source AMI ID. Note that you can only copy an AMI from a Local Zone to its parent Region. aws ec2 copy-image \

    --source-image-id ami-0abcdef1234567890 \ --source-region cn-north-1 \ --name my-ami \ --region cn-north-1 To copy an AMI from one Local Zone to another Local Zone Use the copy-image command. You must specify both the source and destination. You specify the source Region of the Local Zone using the --source-region parameter. You specify the destination Local Zone using the --destination-availability-zone parameter (you can use --destination-availability-zone-id instead). The source Local Zone is assumed from the location of the specified source AMI ID. You specify the parent Region of the destination Local Zone using the --region parameter (or omit this parameter to assume the default Region configured in your AWS CLI settings). aws ec2 copy-image \ --source-image-id ami-0abcdef1234567890 \ --source-region cn-north-1 \ --destination-availability-zone cn-north-1-pkx-1a \ --name my-ami \ --region cn-north-1 PowerShell To copy an AMI from one Region to another Region Use the Copy-EC2Image cmdlet. You must specify both the source and destination Regions.
You specify the source Region using the -SourceRegion parameter. You can specify the destination Region using the -Region parameter or the Set-AWSDefaultRegion cmdlet.
Copy-EC2Image `
    -SourceImageId ami-0abcdef1234567890 `
    -SourceRegion us-west-2 `
    -Name my-ami `
    -Region us-east-1 When you encrypt a target snapshot during AMI copy, you must specify these additional parameters: -Encrypted and -KmsKeyId.
To copy an AMI from a Region to a Local Zone

Use the Copy-EC2Image cmdlet. You must specify both the source and destination. You specify the source Region using the -SourceRegion parameter. You specify the destination Local Zone using the -DestinationAvailabilityZone parameter (you can use - DestinationAvailabilityZoneId instead). Note that you can only copy an AMI from a Region to a Local Zone within that same Region.
Copy-EC2Image `
    -SourceImageId ami-0abcdef1234567890 `
    -SourceRegion cn-north-1 `
    -DestinationAvailabilityZone cn-north-1-pkx-1a `
    -Name my-ami `
    -Region cn-north-1 To copy an AMI from a Local Zone to a Region Use the Copy-EC2Image cmdlet. You must specify both the source and destination. You specify the source Region using the -SourceRegion parameter. You specify the destination Region using the -Region parameter or the Set-AWSDefaultRegion cmdlet. The source Local Zone is assumed from the location of the specified source AMI ID. Note that you can only copy an AMI from a Local Zone to its parent Region.
Copy-EC2Image `
    -SourceImageId ami-0abcdef1234567890 `
    -SourceRegion cn-north-1 `
    -Name my-ami `
    -Region cn-north-1 To copy an AMI from one Local Zone to another Local Zone Use the Copy-EC2Image cmdlet. You must specify both the source and destination. You specify the source Region of the Local Zone using the -SourceRegion parameter. You specify the destination Local Zone using the -DestinationAvailabilityZone parameter (you can use -DestinationAvailabilityZoneId instead). The source Local Zone is assumed from the location of the specified source AMI ID. You specify the parent Region of the destination Local Zone using the -Region parameter or the Set-AWSDefaultRegion cmdlet.
Copy-EC2Image `
    -SourceImageId ami-0abcdef1234567890 `
    -SourceRegion cn-north-1 `
    -DestinationAvailabilityZone cn-north-1-pkx-1a `

    -Name my-ami `
    -Region cn-north-1
### Stop a pending AMI copy operation You can stop a pending AMI copy using the following procedures.
Console To stop an AMI copy operation
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. From the navigation bar, select the destination Region from the Region selector.
3. In the navigation pane, choose AMIs.
4. Select the AMI to stop copying, and then choose Actions, Deregister AMI.
5. When asked for confirmation, choose Deregister AMI.
AWS CLI To stop an AMI copy operation Use the deregister-image command. aws ec2 deregister-image --image-id ami-0abcdef1234567890 PowerShell To stop an AMI copy operation using Use the Unregister-EC2Image cmdlet.
Unregister-EC2Image -ImageId ami-0abcdef1234567890
### How Amazon EC2 AMI copy works Copying a source AMI results in an identical but distinct new AMI that we also refer to as the target AMI. The target AMI has its own unique AMI ID. You can change or deregister the source AMI with no effect on the target AMI. The reverse is also true.

With an EBS-backed AMI, each of its backing snapshots is copied to an identical but distinct target snapshot. If you copy an AMI to a new Region, the snapshots are complete (non-incremental) copies. If you encrypt unencrypted backing snapshots or encrypt them to a new KMS key, the snapshots are complete (non-incremental) copies. Subsequent copy operations of an AMI result in incremental copies of the backing snapshots.
Contents
- Cross-Region copying
- Cross-account copying
- Time-based AMI copy operations
- Encryption and copying
#### Cross-Region copying Copying an AMI across geographically diverse Regions provides the following benefits:
- Consistent global deployment: Copying an AMI from one Region to another enables you to launch consistent instances in different Regions based on the same AMI.
- Scalability: You can more easily design and build global applications that meet the needs of your users, regardless of their location.
- Performance: You can increase performance by distributing your application, as well as locating critical components of your application in closer proximity to your users. You can also take advantage of Region-specific features, such as instance types or other AWS services.
- High availability: You can design and deploy applications across AWS Regions, to increase availability.
The following diagram shows the relationship between a source AMI and two copied AMIs in different Regions, as well as the EC2 instances launched from each. When you launch an instance from an AMI, it resides in the same Region where the AMI resides. If you make changes to the source AMI and want those changes to be reflected in the AMIs in the target Regions, you must recopy the source AMI to the target Regions.

When you first copy an Amazon S3-backed AMI to a Region, we create an Amazon S3 bucket for the AMIs copied to that Region. All Amazon S3-backed AMIs that you copy to that Region are stored in this bucket. The bucket names have the following format: amis-for-account- in-region-hash. For example: amis-for-123456789012-in-us-east-2-yhjmxvp6.
Prerequisite Prior to copying an AMI, you must ensure that the contents of the source AMI are updated to support running in a different Region. For example, you should update any database connection strings or similar application configuration data to point to the appropriate resources. Otherwise, instances launched from the new AMI in the destination Region might still use the resources from the source Region, which can impact performance and cost.
### Limitations
- Destination Regions are limited to 300 concurrent AMI copy operations. This also applies to time- based AMI copy operations.
- You can't copy a paravirtual (PV) AMI to a Region that does not support PV AMIs. For more information, see Virtualization types.
#### Cross-account copying If an AMI from another AWS account is shared with your AWS account, you can copy the shared AMI. This is known as cross-account copying. The AMI that is shared with you is the source AMI.

When you copy the source AMI, you create a new AMI. The new AMI is often referred to as the target AMI.
AMI costs
- For a shared AMI, the account of the shared AMI is charged for the storage in the Region.
- If you copy an AMI that is shared with your account, you are the owner of the target AMI in your account.
- The owner of the source AMI is charged standard Amazon EBS or Amazon S3 transfer fees.
- You are charged for the storage of the target AMI in the destination Region.
Resource permissions To copy an AMI that was shared with you from another account, the owner of the source AMI must grant you read permissions for the storage that backs the AMI, not just for the AMI itself. The storage is either the associated EBS snapshot (for an Amazon EBS-backed AMI) or an associated S3 bucket (for an Amazon S3-backed AMI). If the shared AMI has encrypted snapshots, the owner must share the key or keys with you. For more information about granting resource permissions, for EBS snapshots, see Share an Amazon EBS snapshot with other AWS accounts in the Amazon EBS User Guide, and for S3 buckets, see Identity and access management for Amazon S3 in the Amazon S3 User Guide.
Note Tags that are attached to the source AMI are not copied across accounts to the target AMI.
#### Time-based AMI copy operations When you initiate a time-based AMI copy operation for an EBS-backed AMI with a single associated snapshot, it behaves in the same way as an individual time-based snapshot copy operation, and the same throughput limitations apply.
When you initiate a time-based AMI copy operation for an EBS-backed AMI with a multiple associated snapshots, it behaves in the same way as concurrent time-based snapshot copy operations, and the same throughput limitations apply. Each associated snapshot results in a separate snapshot copy request, each of which contributes to your cumulative snapshot copy throughput quota. The completion duration that you specify applies to each associated snapshot.

For more information, see  Time-based copies in the Amazon EBS User Guide.
#### Encryption and copying The following table shows encryption support for various AMI-copying scenarios. While it is possible to copy an unencrypted snapshot to yield an encrypted snapshot, you cannot copy an encrypted snapshot to yield an unencrypted one.
Scenario Description Supported 1 Unencrypted to unencrypted Yes 2 Encrypted to encrypted Yes 3 Unencrypted to encrypted Yes 4 Encrypted to unencrypted No Note Encrypting during the CopyImage action applies only to Amazon EBS-backed AMIs.
Because an Amazon S3-backed AMI does not use snapshots, you can't use copying to change its encryption status.
When you copy an AMI without specifying encryption parameters, the backing snapshot is copied with its original encryption status by default. Therefore, if the source AMI is backed by an unencrypted snapshot, the resulting target snapshot will also be unencrypted. Similarly, if the source AMI's snapshot is encrypted, the resulting target snapshot will also be encrypted by the same AWS KMS key. For AMIs backed by multiple snapshots, each target snapshot preserves the encryption state of its corresponding source snapshot.
To change the encryption state of the target backing snapshots during an AMI copy, you can specify encryption parameters. The following example shows a non-default case, where encryption parameters are specified with the CopyImage action to change the target AMI's encryption state.
Copy an unencrypted source AMI to an encrypted target AMI

In this scenario, an AMI backed by an unencrypted root snapshot is copied to an AMI with an encrypted root snapshot. The CopyImage action is invoked with two encryption parameters, including a customer managed key. As a result, the encryption status of the root snapshot changes, so that the target AMI is backed by a root snapshot containing the same data as the source snapshot, but encrypted using the specified key. You incur storage costs for the snapshots in both AMIs, as well as charges for any instances you launch from either AMI.
Note Enabling encryption by default has the same effect as setting the Encrypted parameter to true for all snapshots in the AMI.
Setting the Encrypted parameter encrypts the single snapshot for this instance. If you do not specify the KmsKeyId parameter, the default customer managed key is used to encrypt the snapshot copy.
For more information about copying AMIs with encrypted snapshots, see Use encryption with EBS- backed AMIs.
## Store and restore an AMI using S3 You can store an Amazon Machine Image (AMI) in an Amazon S3 bucket, copy the AMI to another S3 bucket, and then restore it from the S3 bucket. By storing and restoring an AMI using S3 buckets, you can copy AMIs from one AWS partition to another, for example, from the main

commercial partition to the AWS GovCloud (US) partition. You can also make archival copies of AMIs by storing them in an S3 bucket.
The supported APIs for storing and restoring an AMI using S3 are CreateStoreImageTask, DescribeStoreImageTasks, and CreateRestoreImageTask.
CopyImage is the recommended API to use for copying AMIs within an AWS partition. However, CopyImage can't copy an AMI to another partition.
For information about the AWS partitions, see partition on the Amazon Resource Names (ARNs) page in the IAM User Guide.
Warning Ensure that you comply with all applicable laws and business requirements when moving data between AWS partitions or AWS Regions, including, but not limited to, any applicable government regulations and data residency requirements.
Contents
- Use cases
- Limitations
- Costs
- How AMI store and restore works
- Create a store image task
### Use cases Use the store and restore APIs to do the following:
- Copy an AMI between AWS partitions
- Make archival copies of AMIs
#### Copy an AMI between AWS partitions By storing and restoring an AMI using S3 buckets, you can copy an AMI from one AWS partition to another, or from one AWS Region to another. In the following example, you copy an AMI from the

main commercial partition to the AWS GovCloud (US) partition, specifically from the us-east-2 Region to the us-gov-east-1 Region.
To copy an AMI from one partition to another, follow these steps:
- Store the AMI in an S3 bucket in the current Region by using CreateStoreImageTask. In this example, the S3 bucket is located in us-east-2.
- Monitor the progress of the store task by using DescribeStoreImageTasks. The object becomes visible in the S3 bucket when the task is completed.
- Copy the stored AMI object to an S3 bucket in the target partition using a procedure of your choice. In this example, the S3 bucket is located in us-gov-east-1.
Note Because you need different AWS credentials for each partition, you can't copy an S3 object directly from one partition to another. The process for copying an S3 object across partitions is outside the scope of this documentation. We provide the following copy processes as examples, but you must use the copy process that meets your security requirements.
- To copy one AMI across partitions, the copy process could be as straightforward as the following: Download the object from the source bucket to an intermediate host (for example, an EC2 instance or a laptop), and then upload the object from the intermediate host to the target bucket. For each stage of the process, use the AWS credentials for the partition.
- For more sustained usage, consider developing an application that manages the copies, potentially using S3 multipart downloads and uploads.
- Restore the AMI from the S3 bucket in the target partition by using CreateRestoreImageTask. In this example, the S3 bucket is located in us-gov-east-1.
- Monitor the progress of the restore task by describing the AMI to check when its state becomes available. You can also monitor the progress percentages of the snapshots that make up the restored AMI by describing the snapshots.
#### Make archival copies of AMIs You can make archival copies of AMIs by storing them in an S3 bucket. The AMI is packed into a single object in S3, and all of the AMI metadata (excluding sharing information) is preserved

as part of the stored AMI. The AMI data is compressed as part of the storage process. AMIs that contain data that can easily be compressed will result in smaller objects in S3. To reduce costs, you can use less expensive S3 storage tiers. For more information, see Amazon S3 Storage Classes and Amazon S3 pricing Limitations
- To store an AMI, your AWS account must either own the AMI and its snapshots, or the AMI and its snapshots must be shared directly with your account. You can't store an AMI if it is only publicly shared.
- Only EBS-backed AMIs can be stored using these APIs.
- Paravirtual (PV) AMIs are not supported.
- The size of an AMI (before compression) that can be stored is limited to 5,000 GB.
- Quota on store image requests: 1,200 GB of storage work (snapshot data) in progress.
- Quota on restore image requests: 600 GB of restore work (snapshot data) in progress.
- For the duration of the store task, the snapshots must not be deleted and the IAM principal doing the store must have access to the snapshots, otherwise the store process will fail.
- You can't create multiple copies of an AMI in the same S3 bucket.
- An AMI that is stored in an S3 bucket can't be restored with its original AMI ID. You can mitigate this by using AMI aliasing.
- Currently the store and restore APIs are only supported by using the AWS Command Line Interface, AWS SDKs, and Amazon EC2 API. You can't store and restore an AMI using the Amazon EC2 console.
### Costs When you store and restore AMIs using S3, you are charged for the services that are used by the store and restore APIs, and for data transfer. The APIs use S3 and the EBS Direct API (used internally by these APIs to access the snapshot data). For more information, see Amazon S3 pricing and Amazon EBS pricing.
### How AMI store and restore works To store and restore an AMI using S3, you use the following APIs:
- CreateStoreImageTask – Stores the AMI in an S3 bucket

- DescribeStoreImageTasks – Provides the progress of the AMI store task
- CreateRestoreImageTask – Restores the AMI from an S3 bucket How the APIs work
- CreateStoreImageTask
- DescribeStoreImageTasks
- CreateRestoreImageTask
- File paths
#### CreateStoreImageTask The CreateStoreImageTask API stores an AMI as a single object in an S3 bucket.
The API creates a task that reads all of the data from the AMI and its snapshots, and then uses an S3 multipart upload to store the data in an S3 object. The API takes all of the components of the AMI, including most of the non-Region-specific AMI metadata, and all the EBS snapshots contained in the AMI, and packs them into a single object in S3. The data is compressed as part of the upload process to reduce the amount of space used in S3, so the object in S3 might be smaller than the sum of the sizes of the snapshots in the AMI.
If there are AMI and snapshot tags visible to the account calling this API, they are preserved.
The object in S3 has the same ID as the AMI, but with a .bin extension. The following data is also stored as S3 metadata tags on the S3 object: AMI name, AMI description, AMI registration date, AMI owner account, and a timestamp for the store operation.
The time it takes to complete the task depends on the size of the AMI. It also depends on how many other tasks are in progress because tasks are queued. You can track the progress of the task by calling the DescribeStoreImageTasks API.
The sum of the sizes of all the AMIs in progress is limited to 1,200 GB of EBS snapshot data per account. Further task creation will be rejected until the tasks in progress are less than the limit.
For example, if an AMI with 200 GB of snapshot data and another AMI with 400 GB of snapshot data are currently being stored, another request will be accepted, because the total in progress is 600 GB, which is less than the limit. But if a single AMI with 1,200 GB of snapshot data is currently being stored, further tasks are rejected until the task is completed.

#### DescribeStoreImageTasks The DescribeStoreImageTasks API describes the progress of the AMI store tasks. You can describe tasks for specified AMIs. If you don't specify AMIs, you get a paginated list of all of the store image tasks that have been processed in the last 31 days.
For each AMI task, the response indicates if the task is InProgress, Completed, or Failed. For tasks InProgress, the response shows an estimated progress as a percentage.
Tasks are listed in reverse chronological order.
Currently, only tasks from the previous month can be viewed.
#### CreateRestoreImageTask The CreateRestoreImageTask API starts a task that restores an AMI from an S3 object that was previously created by using a CreateStoreImageTask request.
The restore task can be performed in the same or a different Region in which the store task was performed.
The S3 bucket from which the AMI object will be restored must be in the same Region in which the restore task is requested. The AMI will be restored in this Region.
The AMI is restored with its metadata, such as the name, description, and block device mappings corresponding to the values of the stored AMI. The name must be unique for AMIs in the Region for this account. If you do not provide a name, the new AMI gets the same name as the original AMI.
The AMI gets a new AMI ID that is generated at the time of the restore process.
The time it takes to complete the AMI restoration task depends on the size of the AMI. It also depends on how many other tasks are in progress because tasks are queued. You can view the progress of the task by describing the AMI (describe-images) or its EBS snapshots (describe- snapshots). If the task fails, the AMI and snapshots are moved to a failed state.
The sum of the sizes of all of the AMIs in progress is limited to 600 GB (based on the size after restoration) of EBS snapshot data per account. Further task creation will be rejected until the tasks in progress are less than the limit.
#### File paths You can use file paths when storing and restoring AMIs, in the following way:

- When storing an AMI in S3, the file path can be added to the bucket name. Internally, the system separates the path from the bucket name, and then adds the path to the object key that is generated to store the AMI. The full object path is shown in the response from the API call.
- When restoring the AMI, because an object key parameter is available, the path can be added to the beginning of the object key value.
Example: Bucket name with appended file path When you store the AMI, specify the file path after the bucket name. amzn-s3-demo-bucket/path1/path2 The following is the resulting object key. path1/path2/ami-0abcdef1234567890.bin When you restore the AMI, you specify both the bucket name and the object key. For examples, see the section called "Create a store image task".
### Create a store image task When you store an AMI in an S3 bucket, a store image task is created. You can use the store image task to monitor the progress and outcome of the process.
Contents
- Securing your AMIs
- Permissions for storing and restoring AMIs using S3
- Create a store image task
- Create a restore image task
#### Securing your AMIs It is important to ensure that the S3 bucket is configured with sufficient security to secure the content of the AMI and that the security is maintained for as long as the AMI objects remain in the bucket. If this can't be done, use of these APIs is not recommended. Ensure that public access to the S3 bucket is not allowed. We recommend enabling Server-side encryption for the S3 buckets in which you store the AMIs, although it's not required.

For information about how to set the appropriate security settings for your S3 buckets, review the following security topics:
- Blocking public access to your Amazon S3 storage
- Setting default server-side encryption behavior for Amazon S3 buckets
- What S3 bucket policy can I use to comply with the AWS Config rule s3-bucket-ssl-requests-only?
- Enabling Amazon S3 server access logging When the AMI snapshots are copied to the S3 object, the data is then copied over TLS connections.
You can store AMIs with encrypted snapshots, but the snapshots are decrypted as part of the store process.
#### Permissions for storing and restoring AMIs using S3 If your IAM principals will store or restore AMIs using Amazon S3, you need to grant them the required permissions.
The following example policy includes all of the actions that are required to allow an IAM principal to carry out the store and restore tasks.
You can also create IAM policies that grant principals access to specific resources only. For more example policies, see  Access management for AWS resources in the IAM User Guide.
Note If the snapshots that make up the AMI are encrypted, or if your account is enabled for encryption by default, your IAM principal must have permission to use the KMS key.
JSON { "Version":"2012-10-17", "Statement": [ { "Effect": "Allow", "Action": [ "s3:DeleteObject",

                "s3:GetObject", "s3:ListBucket", "s3:PutObject", "s3:PutObjectTagging", "s3:AbortMultipartUpload", "ebs:CompleteSnapshot", "ebs:GetSnapshotBlock", "ebs:ListChangedBlocks", "ebs:ListSnapshotBlocks", "ebs:PutSnapshotBlock", "ebs:StartSnapshot", "ec2:CreateStoreImageTask", "ec2:DescribeStoreImageTasks", "ec2:CreateRestoreImageTask", "ec2:GetEbsEncryptionByDefault", "ec2:DescribeTags", "ec2:CreateTags"
            ], "Resource": "*"
        } ]
}
#### Create a store image task To store an AMI in an S3 bucket, start by creating a store image task. The time it takes to complete the task depends on the size of the AMI. You can track the progress of the task until it either succeeds or fails.
AWS CLI To create the store image task Use the create-store-image-task command. aws ec2 create-store-image-task \ --image-id ami-0abcdef1234567890 \ --bucket amzn-s3-demo-bucket The following is example output.
{

  "ObjectKey": "ami-0abcdef1234567890.bin"
} To describe the progress of the store image task Use the describe-store-image-tasks command. aws ec2 describe-store-image-tasks \ --image-ids ami-0abcdef1234567890 \ --query StoreImageTaskResults[].StoreTaskState \ --output text The following is example output.
InProgress PowerShell To create the store image task Use the New-EC2StoreImageTask cmdlet.
New-EC2StoreImageTask `
    -ImageId ami-0abcdef1234567890 `
    -Bucket amzn-s3-demo-bucket The following is example output.
ObjectKey         : ami-0abcdef1234567890.bin To describe the progress of the store image task Use the Get-EC2StoreImageTask cmdlet.
(Get-EC2StoreImageTask -ImageId ami-0abcdef1234567890).StoreTaskState The following is example output.
InProgress

#### Create a restore image task You must specify a name for the restored AMI. The name must be unique for AMIs in the Region for this account. The restored AMI gets a new AMI ID.
AWS CLI To create a restore image task Use the create-restore-image-task command. aws ec2 create-restore-image-task \ --object-key ami-0abcdef1234567890.bin \ --bucket amzn-s3-demo-bucket \ --name "my-restored-ami"
The following is example output.
{ "ImageId": "ami-1234567890abcdef0"
} PowerShell To create a restore image task Use the New-EC2RestoreImageTask cmdlet.
New-EC2RestoreImageTask `
    -ObjectKey ami-0abcdef1234567890.bin `
    -Bucket amzn-s3-demo-bucket `
    -Name "my-restored-ami"
The following is example output.
ImageId         : ami-1234567890abcdef0

## Use AMI ancestry to trace the origin of an AMI AMI ancestry helps you trace the origin of an AMI by returning the IDs and Regions of all its ancestor AMIs. When you create or copy an AMI, the new AMI retains the ID and Region of its source (parent) AMI. This enables you to track the chain of AMIs back to the root AMI.
Key benefits Using AMI ancestry helps you:
- Track AMI derivatives to ensure compliance with internal policies.
- Identify potentially vulnerable AMIs when a security issue is found in an ancestor AMI.
- Maintain visibility of AMI origins across multiple Regions.
Topics
- How AMI ancestry works
- Considerations
- View AMI ancestry
- Identify the source AMI
### How AMI ancestry works AMI ancestry identifies the parent AMI that was used to create the specified AMI, the parent's parent, and so on, up to the root AMI. Here's how it works:
- Each AMI displays the ID and Region of its source (parent) AMI.
- Starting with your selected AMI, the list of ancestry entries displays each parent AMI in sequence.
- The list of ancestry entries traces back until it reaches the root AMI. The root AMI is one of the following:
- A public AMI from a verified provider (identified by its owner alias, which is either amazon or aws-marketplace).
- An AMI with no recorded ancestor. For example, when using RegisterImage to create an AMI directly from a set of snapshots, there is no source AMI to track, unlike when creating an AMI from an instance.
- An AMI whose source AMI is from a different partition.

- The 50th AMI in the list. The maximum number of AMIs in an ancestry list is 50.
### Considerations
- The ID and Region of the source AMI are only available for AMIs created using CreateImage, CopyImage, or CreateRestoreImageTask.
- For AMIs created using CreateImage (creates an AMI from an instance), the source AMI ID is the ID of the AMI used to launch the instance.
- The source AMI information is not available for:
- AMIs created using RegisterImage because they were created from snapshots.
- For some older AMIs.
- The source AMI information is preserved when:
- AMIs are copied across Regions.
- Source AMIs are deregistered (deleted).
- You don't have access to the source AMIs.
- Each ancestry list is limited to 50 AMIs.
### View AMI ancestry You can view an AMI's ancestry using the following methods.
Console To view the ancestry of an AMI
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose AMIs.
3. Select an AMI and choose the AMI ancestry tab.
4. The AMI ancestry entries table lists all the AMIs in the ancestry list.
- AMI ID – The identifier of each AMI in the ancestry list. The first entry in the table is the selected AMI, followed by its ancestors.
- Source AMI ID – The ID of the AMI from which the AMI in the AMI ID column was created.
A dash (-) indicates the end of the AMI ancestry list.
- Source AMI Region – The AWS Region where the source AMI is located.

- Ancestry level – The position in the ancestry list, where:
- 0 (input AMI) indicates the selected AMI whose ancestry you want to know.
- Increasing numbers show older ancestors.
- n (original AMI) indicates the root AMI, with the number indicating how far back the ancestry list goes.
- Creation date – When the AMI was created, in UTC format.
- Owner alias – The alias of the AMI owner (for example, amazon). A dash (-) indicates that the AMI has no owner alias.
AWS CLI To view the ancestry of an AMI Use the get-image-ancestry command and specify the AMI ID. aws ec2 get-image-ancestry \ --image-id ami-1111111111EXAMPLE \ --region us-east-1 The following is example output. The output lists AMIs in ancestry order: the first entry is the specified (input) AMI, followed by its parent, parent's parent, and so on, and ends with the root AMI.
{ "ImageAncestryEntries": [ { "CreationDate": "2025-01-17T18:37:50.000Z", "ImageId": "ami-1111111111EXAMPLE", // Input AMI "SourceImageId": "ami-2222222222EXAMPLE", "SourceImageRegion": "us-east-1"
        }, { "CreationDate": "2025-01-17T18:37:50.000Z", "ImageId": "ami-2222222222EXAMPLE", // Parent AMI "SourceImageId": "ami-3333333333EXAMPLE", "SourceImageRegion": "us-east-1"
        }, ...

        { "CreationDate": "2025-01-17T18:37:50.000Z", "ImageId": "ami-8888888888EXAMPLE", // Root AMI "ImageOwnerAlias": "aws-marketplace", "SourceImageId": "ami-9999999999EXAMPLE", "SourceImageRegion": "us-east-2"
        } ]
} PowerShell To view the ancestry of an AMI Use the Get-EC2ImageAncestry cmdlet.
Get-EC2ImageAncestry -ImageId ami-1111111111EXAMPLE The following is example output. The output lists AMIs in ancestry order: the first entry is the specified (input) AMI, followed by its parent, parent's parent, and so on, and ends with the root AMI.
ImageAncestryEntries : { @{ CreationDate = "2025-01-17T18:37:50.000Z"
        ImageId = "ami-1111111111EXAMPLE"    # Input AMI SourceImageId = "ami-2222222222EXAMPLE"
        SourceImageRegion = "us-east-1"
    }, @{ CreationDate = "2025-01-17T18:37:50.000Z"
        ImageId = "ami-2222222222EXAMPLE"    # Parent AMI SourceImageId = "ami-3333333333EXAMPLE"
        SourceImageRegion = "us-east-1"
    }, ...
    @{ CreationDate = "2025-01-17T18:37:50.000Z"
        ImageId = "ami-8888888888EXAMPLE"    # Root AMI ImageOwnerAlias = "aws-marketplace"
        SourceImageId = "ami-9999999999EXAMPLE"
        SourceImageRegion = "us-east-2"

    } }
### Identify the source AMI If you only need to identify the immediate parent (source) AMI used to create an AMI, you can use the following methods.
Console To identify the source AMI used to create the selected AMI
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose AMIs.
3. Select the AMI to view its details.
The source AMI information appears in the following fields: Source AMI ID and Source AMI Region AWS CLI To identify the source AMI used to create the specified AMI Use the describe-images command. aws ec2 describe-images \ --region us-east-1 \ --image-ids ami-0abcdef1234567890 \ --query "Images[].{ID:SourceImageId,Region:SourceImageRegion}"
The following is example output.
[ { "ID": "ami-0abcdef1234567890", "Region": "us-west-2"
    } }

PowerShell To identify the source AMI used to create the specified AMI Use the Get-EC2Image cmdlet.
Get-EC2Image -ImageId ami-0abcdef1234567890 | Select SourceImageId, SourceImageRegion The following is example output.
SourceImageId           SourceImageRegion -------------           ----------------- ami-0abcdef1234567890 us-west-2
## Manage and monitor AMI usage AWS provides several features to help you manage and monitor your AMI usage effectively. You can track which accounts are using your shared AMIs, identify when your AMIs were last used, and discover which resources in your AWS account are referencing specific AMIs.
The following table provides an overview of the features for managing and monitoring AMI usage:
Feature Use case Key benefits AMI usage reports Gain visibility into which AWS accounts are using your AMIs and how much each AMI is being used.
- Identify the AWS accounts and resource types referencing your AMIs so that you can  safely deregister or disable AMIs.
- Identify unused AMIs for deregistration to reduce storage costs.
- Identify your most used AMIs.

Feature Use case Key benefits Last used tracking Check when your AMI was last used.
- Identify unused AMIs so that you can safely deregister AMIs.
- Identify unused AMIs for deregistration to reduce storage costs.
AMI reference check Ensure your AWS resources are using the latest compliant AMIs.
- Audit the use of AMIs in your account.
- Check where specific AMIs are being referenced.
- Maintain compliance by updating your resources to reference the latest  AMIs.
Topics
- View your AMI usage
- Check when an Amazon EC2 AMI was last used
- Identify your resources referencing specified AMIs
### View your AMI usage If you share your Amazon Machine Images (AMIs) with other AWS accounts—whether with specific AWS accounts, organizations, organizational units (OUs), or publicly—you can see how these AMIs are used by creating AMI usage reports. The reports provide visibility into:
- Which AWS accounts are using your AMIs in EC2 instances or launch templates
- How many EC2 instances or launch templates are referencing each AMI

AMI usage reports help you manage your AMIs more effectively by helping you:
- Identify the AWS accounts and resource types referencing your AMIs so that you can safely deregister or disable AMIs.
- Identify unused AMIs for deregistration to reduce storage costs.
- Identify your most used AMIs.
Contents
- How AMI usage reports work
- Create an AMI usage report
- View AMI usage reports
- Delete an AMI usage report
- Report quotas
#### How AMI usage reports work When you create an AMI usage report, you specify:
- The AMI to report on.
- The AWS accounts to check (specific accounts or all accounts).
- The resource types to check (EC2 instances, launch templates, or both).
- For launch templates, the number of versions to check (defaults to the 20 most recent versions).
Amazon EC2 creates a separate report for each AMI. Each report provides:
- A list of the AWS accounts using the AMI.
- A count of the resources referencing the AMI by resource type per account. Note that for launch templates, if an AMI is referenced in multiple versions of a launch template, the count is only 1.
Important When you generate an AMI usage report, it might not contain the most recent activity.
Instance activity from the past 24 hours and launch template activity from the past few days might not appear in the report.

Amazon EC2 automatically deletes a report 30 days after creation. You can download reports from the EC2 console to retain locally.
#### Create an AMI usage report To view how your AMI is being used, you must first create an AMI usage report, specifying the accounts and resource types to report on. Once the report is created, you can view the contents of the report. You can also download the report from the EC2 console.
Console To create an AMI usage report
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose AMIs.
3. Select an AMI and choose Actions, AMI usage, View my AMI usage.
4. On the Create my AMI usage report page, do the following: a.
For Resource types, select one or more resource types to report on. b.
For Account IDs, do one of the following:
- Choose Specify accounts IDs and then choose Add account ID for each account to report on.
- Choose Include all accounts to report on all accounts. c.
Choose Create my AMI usage report.
5. On the AMI page, choose the My AMI usage tab.
6. Choose a report ID to view its details.
AWS CLI To create an AMI usage report for a list of accounts Use the create-image-usage-report command with the following required parameters:
- --image-id – The ID of the AMI to report on.
- --resource-types – The types of resources to check. In the following example, the resource types to check are EC2 instances and launch templates. In addition, the number of launch template versions to check is also specified (version-depth=100).

To report on specific accounts, use the --account-ids parameter to specify the ID of each account to report on. aws ec2 create-image-usage-report \ --image-id ami-0abcdef1234567890 \ --account-ids 111122223333 444455556666 123456789012 \ --resource-types ResourceType=ec2:Instance \ 'ResourceType=ec2:LaunchTemplate,ResourceTypeOptions=[{OptionName=version- depth,OptionValues=100}]'
To create an AMI usage report of all accounts To report on all accounts using the specified AMI, use the same command but omit the -- account-ids parameter. aws ec2 create-image-usage-report \ --image-id ami-0abcdef1234567890 \ --resource-types ResourceType=ec2:Instance \ 'ResourceType=ec2:LaunchTemplate,ResourceTypeOptions=[{OptionName=version- depth,OptionValues=100}]'
The following is example output.
{ "ReportId": "amiur-00b877d192f6b02d0"
} To monitor the report creation status Use the describe-image-usage-reports command and specify the report ID. aws ec2 describe-image-usage-reports --report-ids amiur-00b877d192f6b02d0 The following is example output. The initial value of the State field is pending. To be able to view the report entries, the state must be available.
{ "ImageUsageReports": [ { "ImageId": "ami-0e9ae3dc21c2b3a64",

            "ReportId": "amiur-abcae3dc21c2b3999", "ResourceTypes": [ {"ResourceType": "ec2:Instance"} ], "State": "pending", "CreationTime": "2025-09-29T13:27:12.322000+00:00", "ExpirationTime": "2025-10-28T13:27:12.322000+00:00"
        } ]
} PowerShell To create an AMI usage report for a list of accounts Use the New-EC2ImageUsageReport cmdlet with the following required parameters:
- -ImageId – The ID of the AMI to report on.
- -ResourceType – The types of resources to check. In the following example, the resource types to check are EC2 instances and launch templates. In addition, the number of launch template versions to check is also specified ('version-depth' = 100).
To report on specific accounts, use the -AccountId parameter to specify the ID of each account to report on.
New-EC2ImageUsageReport `
    -ImageId ami-0abcdef1234567890 `
    -AccountId 111122223333 444455556666 123456789012 `
    -ResourceType @( @{ResourceType = 'ec2:Instance'}, @{ResourceType = 'ec2:LaunchTemplate'ResourceTypeOptions = @{'version-depth'
 = 100} })
To create an AMI usage report of all accounts To report on all accounts using the specified AMI, use the same command but omit the - AccountId parameter.
New-EC2ImageUsageReport `

    -ImageId ami-0abcdef1234567890 `
    -ResourceType @( @{ResourceType = 'ec2:Instance'}, @{ResourceType = 'ec2:LaunchTemplate'ResourceTypeOptions = @{'version-depth'
 = 100} })
The following is example output.
ReportId
-------- amiur-00b877d192f6b02d0 To monitor the report creation status Use the Get-EC2ImageUsageReport command and specify the report ID.
Get-EC2ImageUsageReport -ReportId amiur-00b877d192f6b02d0 The following is example output. The initial value of the State field is pending. To be able to view the report entries, the state must be available.
ImageUsageReports
----------------- {@{ImageId=ami-0e9ae3dc21c2b3a64; ReportId=amiur-abcae3dc21c2b3999; ResourceTypes=System.Object[]; State=pending; CreationTime=2025-09-29; ExpirationTime=2025-10-28}}
#### View AMI usage reports You can view all the usage reports you've created for an AMI in the past 30 days. Amazon EC2 automatically deletes a report 30 days after creation.
For each report, you can see the AWS accounts that are using the AMI, and for each account, a count of the resources referencing the AMI by resource type. You can also see when the report creation was initiated. This information is only available when the report is in the Complete (console) or available (AWS CLI) state.

Important When you generate an AMI usage report, it might not contain the most recent activity.
Instance activity from the past 24 hours and launch template activity from the past few days might not appear in the report.
Console To view an AMI usage report
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose AMIs.
3. Select an AMI.
4. Choose the My usage reports tab.
The report list shows:
- All reports generated in the past 30 days for the selected AMI.
- For each report, the Report initiated time column shows the date the report was created.
5. Choose the ID of a report to view its contents.
6. To go back to the My usage reports tab on the AMI details page, choose View all reports for this AMI.
AWS CLI To list all the AMI usage reports for the specified AMI Use the describe-image-usage-reports command and specify the ID of the AMI to get a list of its reports. aws ec2 describe-image-usage-reports --image-ids ami-0abcdef1234567890 The following is example output. Each report ID is listed along with the resource types that were scanned and the report creation and expiration dates. You can use this information to identify the reports whose entries you want to view.

{ "ImageUsageReports": [ { "ImageId": "ami-0abcdef1234567890", "ReportId": "amiur-1111111111111111", "ResourceTypes": [ { "ResourceType": "ec2:Instance"
        } ], "State": "available", "CreationTime": "2025-09-29T13:27:12.322000+00:00", "ExpirationTime": "2025-10-28T13:27:12.322000+00:00", "Tags": []
    }, { "ImageId": "ami-0abcdef1234567890", "ReportId": "amiur-22222222222222222", "ResourceTypes": [ { "ResourceType": "ec2:Instance"
        }, { "ResourceType": "ec2:LaunchTemplate"
        } ], "State": "available", "CreationTime": "2025-10-01T13:27:12.322000+00:00", "ExpirationTime": "2025-10-30T13:27:12.322000+00:00", "Tags": []
    } ], "NextToken": "opaque"
} To view the contents of an AMI usage report for the specified AMI Use the describe-image-usage-report-entries command and specify the ID of the AMI. The response returns all the reports for the specified AMI, showing the accounts that have used the AMI and their resource counts. aws ec2 describe-image-usage-report-entries --image-ids ami-0abcdef1234567890

The following is example output.
{ "ImageUsageReportEntries": [ { "ImageId": "ami-0abcdef1234567890", "ResourceType": "ec2:Instance", "AccountId": "123412341234", "UsageCount": 15, "ReportCreationTime": "2025-09-29T13:27:12.322000+00:00", "ReportId": "amiur-1111111111111111"
    }, { "ImageId": "ami-0abcdef1234567890", "ResourceType": "ec2:Instance", "AccountId": "123412341234", "UsageCount": 2, "ReportCreationTime": "2025-10-01T13:27:12.322000+00:00", "ReportId": "amiur-22222222222222222"
    }, { "ImageId": "ami-0abcdef1234567890", "ResourceType": "ec2:Instance", "AccountId": "001100110011", "UsageCount": 39, "ReportCreationTime": "2025-10-01T13:27:12.322000+00:00", "ReportId": "amiur-22222222222222222"
    } ], "NextToken": "opaque"
} To view the contents of an AMI usage report for the specified report Use the describe-image-usage-report-entries command and specify the ID of the report. The response returns all the entries for the specified report, showing the accounts that have used the AMI and their resource counts. aws ec2 describe-image-usage-report-entries --report-ids amiur-11111111111111111 The following is example output.

{ "ImageUsageReportEntries": [ { "ImageId": "ami-0abcdef1234567890", "ResourceType": "ec2:Instance", "AccountId": "123412341234", "UsageCount": 15, "ReportCreationTime": "2025-09-29T13:27:12.322000+00:00", "ReportId": "amiur-11111111111111111"
    }, { "ImageId": "ami-0abcdef1234567890", "ResourceType": "ec2:LaunchTemplate", "AccountId": "123412341234", "UsageCount": 4, "ReportCreationTime": "2025-09-29T13:27:12.322000+00:00", "ReportId": "amiur-11111111111111111"
    }, { "ImageId": "ami-0abcdef1234567890", "ResourceType": "ec2:LaunchTemplate", "AccountId": "001100110011", "UsageCount": 2, "ReportCreationTime": "2025-09-29T13:27:12.322000+00:00", "ReportId": "amiur-11111111111111111"
    } ], "NextToken": "opaque"
} PowerShell To list all the AMI usage reports for the specified AMI Use the Get-EC2ImageUsageReport cmdlet and specify the ID of the AMI to get a list of its reports.
Get-EC2ImageUsageReport -ImageId ami-0abcdef1234567890 The following is example output. Each report ID is listed along with the resource types that were scanned and the report creation and expiration dates. You can use this information to identify the reports whose entries you want to view.

@{ ImageUsageReports = @( @{ ImageId = "ami-0abcdef1234567890"
            ReportId = "amiur-1111111111111111"
            ResourceTypes = @( @{ ResourceType = "ec2:Instance"
                } )
            State = "available"
            CreationTime = "2025-09-29T13:27:12.322000+00:00"
            ExpirationTime = "2025-10-28T13:27:12.322000+00:00"
        }, @{ ImageId = "ami-0abcdef1234567890"
            ReportId = "amiur-22222222222222222"
            ResourceTypes = @( @{ ResourceType = "ec2:Instance"
                } )
            State = "available"
            CreationTime = "2025-09-30T13:27:12.322000+00:00"
            ExpirationTime = "2025-10-29T13:27:12.322000+00:00"
        }, @{ ImageId = "ami-0abcdef1234567890"
            ReportId = "amiur-33333333333333333"
            ResourceTypes = @( @{ ResourceType = "ec2:Instance"
                } )
            State = "available"
            CreationTime = "2025-10-01T13:27:12.322000+00:00"
            ExpirationTime = "2025-10-30T13:27:12.322000+00:00"
        } )
    NextToken = "opaque"
} To view the contents of an AMI usage report for the specified AMI

Use the Get-EC2ImageUsageReportEntry cmdlet and specify the ID of the AMI. The response returns all the reports for the specified AMI, showing the accounts that have used the AMI and their resource counts.
Get-EC2ImageUsageReportEntry -ImageId ami-0abcdef1234567890 The following is example output.
ImageUsageReportEntries : {@{ ImageId = "ami-0abcdef1234567890"
    ResourceType = "ec2:Instance"
    AccountId = "123412341234"
    UsageCount = 15 ReportCreationTime = "2025-09-29T13:27:12.322000+00:00"
    ReportId = "amiur-1111111111111111"
    }, @{ ImageId = "ami-0abcdef1234567890"
    ResourceType = "ec2:Instance"
    AccountId = "123412341234"
    UsageCount = 7 ReportCreationTime = "2025-09-30T13:27:12.322000+00:00"
    ReportId = "amiur-22222222222222222"
    }...} NextToken : opaque To view the contents of an AMI usage report for the specified report Use the Get-EC2ImageUsageReportEntry cmdlet and specify the ID of the report. The response returns all the entries for the specified report, showing the accounts that have used the AMI and their resource counts.
Get-EC2ImageUsageReportEntry -ReportId amiur-11111111111111111 The following is example output.
ImageUsageReportEntries : {@{ ImageId = "ami-0abcdef1234567890"
    ResourceType = "ec2:Instance"
    AccountId = "123412341234"
    UsageCount = 15 ReportCreationTime = "2025-09-29T13:27:12.322000+00:00"

    ReportId = "amiur-11111111111111111"
    }, @{ ImageId = "ami-0abcdef1234567890"
    ResourceType = "ec2:LaunchTemplate"
    AccountId = "123412341234"
    UsageCount = 4 ReportCreationTime = "2025-09-29T13:27:12.322000+00:00"
    ReportId = "amiur-11111111111111111"
    }, @{ ImageId = "ami-0abcdef1234567890"
    ResourceType = "ec2:LaunchTemplate"
    AccountId = "************"
    UsageCount = 2 ReportCreationTime = "2025-09-29T13:27:12.322000+00:00"
    ReportId = "amiur-11111111111111111"
    }} NextToken : opaque
#### Delete an AMI usage report Amazon EC2 automatically deletes a report 30 days after it was created. You can delete it manually before that time.
Console To delete an AMI usage report
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose AMIs.
3. Select an AMI.
4. Choose the My AMI usage tab.
5. Choose the option button next to the report to delete, and then choose Delete.
AWS CLI To delete an AMI usage report Use the delete-image-usage-report command and specify the ID of the report. aws ec2 delete-image-usage-report --report-id amiur-0123456789abcdefg

PowerShell To delete an AMI usage report Use the Remove-EC2ImageUsageReport cmdlet and specify the ID of the report.
Remove-EC2ImageUsageReport -ReportId amiur-0123456789abcdefg
#### Report quotas The following quotas apply to creating AMI usage reports. The quotas apply per AWS Region.
Description Quota In-progress (pending) AMI usage reports per AWS account 2,000 In-progress (pending) AMI usage reports per AMI 1
### Check when an Amazon EC2 AMI was last used Amazon EC2 automatically tracks the date and time when an AMI was last used to launch an instance. If you have an AMI that has not been used to launch an instance in a long time, consider whether the AMI is a good candidate for deregistration or deprecation.
### Considerations
- When an AMI is used to launch an instance, there is a 24-hour delay before that usage is reported.
- You must be the owner of the AMI to get the last launched time.
- AMI usage data is available starting April 2017.
Console To view the last launched time of an AMI
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.

2. In the left navigation pane, choose AMIs.
3. From the filter bar, choose Owned by me.
4. Select the checkbox for the AMI.
5. On the Details tab, find Last launched time.
AWS CLI To view the last launched time by describing the AMI Use the describe-images command. If LastLaunchedTime is not present in the output, verify that you own the AMI. aws ec2 describe-images \ --image-id ami-0abcdef1234567890 \ --query Images[].LastLaunchedTime \ --output text The following is example output.
2025-02-17T20:22:19Z To view the last launched time attribute of an AMI Use the describe-image-attribute command. You must be the owner of the specified AMI. aws ec2 describe-image-attribute \ --image-id ami-0abcdef1234567890 \ --attribute lastLaunchedTime \ --query LastLaunchedTime.Value \ --output text The following is example output.
2025-02-17T20:22:19Z PowerShell To view the last launched time by describing the AMI

Use the Get-EC2Image cmdlet. If LastLaunchedTime is not present in the output, verify that you own the AMI.
(Get-EC2Image -ImageId ami-0abcdef1234567890).LastLaunchedTime The following is example output.
2025-02-17T20:22:19Z To view the last launched time attribute of an AMI Use the Get-EC2ImageAttribute cmdlet. You must be the owner of the specified AMI.
(Get-EC2ImageAttribute `
    -ImageId ami-0abcdef1234567890 `
    -Attribute LastLaunchedTime).LastLaunchedTime The following is example output.
2025-02-17T20:22:19Z
### Identify your resources referencing specified AMIs You can identify your AWS resources that reference specified Amazon Machine Images (AMIs), regardless of whether the AMIs are public or private, or who owns them. This visibility helps you ensure your resources use the latest compliant AMIs.
Key benefits Checking AMI references helps you:
- Audit the use of AMIs in your account.
- Check where specific AMIs are being referenced.
- Maintain compliance by updating your resources to reference the latest AMIs.

Topics
- Supported resources

- How AMI reference checks work
- Required IAM permissions
- Steps for checking AMI references
#### Supported resources AMI references can be checked in:
- EC2 instances
- Launch templates
- SSM parameters
- Image Builder image recipes
- Image Builder container recipes
#### How AMI reference checks work Basic operation When you run an AMI reference check, you:
- Specify which AMIs to check.
- Choose which resource types to scan.
- Receive a list of your resources that reference the specified AMIs.
Resource type selection In the console, you select the resource types to scan.
In the CLI, you specify resource types to scan using one or both of the following CLI parameters:
- IncludeAllResourceTypes: Scans all supported resource types.
- ResourceTypes: Scans your specified resource types.
Response scoping You can scope the response for EC2 instances and launch templates by customizing the ResourceTypeOptions values using the ResourceTypes parameter. The console and

IncludeAllResourceTypes parameter both use default option values. When ResourceTypes and IncludeAllResourceTypes are used together, the ResourceTypes option values take precedence over the defaults.
The following are the default values:
Resource type Scoping option (OptionName )
Purpose Default values for OptionValue  and console EC2 instances state-name Filter by instance state pending, running, shutting-down , terminated , stopping, stopped (all states)
Launch templates version-depth Specify the number of launch template versions to check (starting from the most recent version)
10 (most recent versions)
#### Required IAM permissions To use the DescribeImageReferences API to identify your resources that are referencing specified AMIs, you need the following IAM permissions to describe the resources:
- ec2:DescribeInstances
- ec2:DescribeLaunchTemplates
- ec2:DescribeLaunchTemplateVersions
- ssm:DescribeParameters
- ssm:GetParameters
- imagebuilder:ListImageRecipes
- imagebuilder:ListContainerRecipes
- imagebuilder:GetContainerRecipe

Example IAM policy for using the DescribeImageReferences API The following example policy grants you the permissions to use the DescribeImageReferences API, which includes the permissions to describe EC2 instances, launch templates, Systems Manager parameters, Image Builder image recipes, and Image Builder container recipes.
JSON { "Version":"2012-10-17", "Statement": [ { "Effect": "Allow", "Action": "ec2:DescribeImageReferences", "Resource": "*"
  }, { "Effect": "Allow", "Action": [ "ec2:DescribeInstances", "ec2:DescribeLaunchTemplates", "ec2:DescribeLaunchTemplateVersions", "ssm:DescribeParameters", "ssm:GetParameters", "imagebuilder:ListImageRecipes", "imagebuilder:ListContainerRecipes", "imagebuilder:GetContainerRecipe"
   ], "Resource": "*", "Condition": { "ForAnyValue:StringEquals": { "aws:CalledVia": [ "ec2-images.amazonaws.com"
     ]
    } } } ]
}

Important We strongly recommend using the AWS managed policy AmazonEC2ImageReferencesAccessPolicy instead of creating the policy yourself.
Creating a custom IAM policy that provides only the required permissions requires time and expertise, and will require updates as new resource types become available.
The AmazonEC2ImageReferencesAccessPolicy managed policy:
- Grants all the permissions needed to use the DescribeImageReferences API (these include the permissions to describe EC2 instances, launch templates, Systems Manager parameters, and Image Builder container and image recipes).
- Automatically supports new resource types as they become available (especially important when using the IncludeAllResourceTypes parameter).
You can attach the AmazonEC2ImageReferencesAccessPolicy policy to your IAM identities (users, groups, and roles).
To view the permissions included in this policy, see AmazonEC2ImageReferencesAccessPolicy in the AWS Managed Policy Reference.
#### Steps for checking AMI references Use the following procedures to identify which of your AWS resources are referencing specified AMIs.
Console To identify resources referencing specified AMIs
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose AMIs.
3. Select one or more AMIs to check for references.
4. Choose Actions, AMI usage, View referenced resources.
5. On the View resources referencing selected AMIs page: a.
For Resource types, select one or more resource types. b.
Choose View resources.

6. The Resources referencing selected AMIs section appears. The list displays the resources referencing the specified AMIs. Each row provides the following information:
- AMI ID – The ID of the referenced AMI.
- Resource type – The resource type of the resource referencing the AMI.
- Resource ID – The ID of the resource referencing the AMI.
AWS CLI To check AMI references for specific resource types Use the describe-image-references command with the --resource-types parameter. The following example checks EC2 instances (scoping by instance state), launch templates (scoping to the 20 most recent launch template versions), and other specific resource types. aws ec2 describe-image-references \ --image-ids ami-0abcdef1234567890 ami-1234567890abcdef0 \ --resource-types \ 'ResourceType=ec2:Instance,ResourceTypeOptions=[{OptionName=state- name,OptionValues=[running,pending]}]' \ 'ResourceType=ec2:LaunchTemplate,ResourceTypeOptions=[{OptionName=version- depth,OptionValues=[20]}]' \ 'ResourceType=ssm:Parameter' \ 'ResourceType=imagebuilder:ImageRecipe' \ 'ResourceType=imagebuilder:ContainerRecipe'
The following is example output.
{ "ImageReferences": [ { "ImageId": "ami-0abcdef1234567890", "ResourceType": "ec2:Instance", "Arn": "arn:aws:ec2:us-east-1:123456789012:instance/i-1234567890abcdef0"
        }, { "ImageId": "ami-1234567890abcdef0", "ResourceType": "ec2:LaunchTemplate", "Arn": "arn:aws:ec2:us-east-1:123456789012:launch-template/ lt-1234567890abcdef0"
        }

    ]
} To check AMI references for all the supported resource types Use the describe-image-references command with the --include-all-resource-types parameter. aws ec2 describe-image-references \ --image-ids ami-0abcdef1234567890 ami-1234567890abcdef0 \ --include-all-resource-types To check AMI references for all supported resource types and specific options Use the describe-image-references command with both the --include-all-resource- types and --resource-types parameters. This example checks all resource types while scoping the response for EC2 instances to running or pending instances. aws ec2 describe-image-references \ --image-ids ami-0abcdef1234567890 ami-1234567890abcdef0 \ --include-all-resource-types \ --resource-types 'ResourceType=ec2:Instance,ResourceTypeOptions=[{OptionName=state- name,OptionValues=[running,pending]}]'
PowerShell To check AMI references for specific resource types Use the Get-EC2ImageReference cmdlet with the -ResourceType parameter. The following example checks EC2 instances (scoping by instance state), launch templates (scoping to the 20 most recent launch template versions), and other specific resource types.
Get-EC2ImageReference `
    -ImageId 'ami-0abcdef1234567890', 'ami-1234567890abcdef0' `
    -ResourceType @( @{ ResourceType = 'ec2:Instance'
            ResourceTypeOptions = @( @{ OptionName = 'state-name'
                    OptionValues = @('running', 'pending')

                } )
        }, @{ ResourceType = 'ec2:LaunchTemplate'
            ResourceTypeOptions = @( @{ OptionName = 'version-depth'
                    OptionValues = @('20')
                } )
        }, @{ ResourceType = 'ssm:Parameter'
        }, @{ ResourceType = 'imagebuilder:ImageRecipe'
        }, @{ ResourceType = 'imagebuilder:ContainerRecipe'
        } )
To check AMI references for all the supported resource types Use the Get-EC2ImageReference cmdlet with the -IncludeAllResourceTypes parameter.
Get-EC2ImageReference `
    -ImageId 'ami-0abcdef1234567890', 'ami-1234567890abcdef0' `
    -IncludeAllResourceTypes To check AMI references for all supported resource types and specific options Use the Get-EC2ImageReference cmdlet with both the -IncludeAllResourceTypes and - ResourceType parameters. This example checks all resource types while scoping the response for EC2 instances to running or pending instances.
Get-EC2ImageReference `
    -ImageId 'ami-0abcdef1234567890', 'ami-1234567890abcdef0' `
    -IncludeAllResourceTypes `
    -ResourceType @( @{

            ResourceType = 'ec2:Instance'
            ResourceTypeOptions = @( @{ OptionName = 'state-name'
                    OptionValues = @('running', 'pending')
                } )
        } )
## Deprecate an Amazon EC2 AMI You can deprecate an AMI to indicate that it is out of date and should not be used. You can also specify a future deprecation date for an AMI, indicating when the AMI will be out of date.
For example, you might deprecate an AMI that is no longer actively maintained, or you might deprecate an AMI that has been superseded by a newer version. By default, deprecated AMIs do not appear in AMI listings, preventing new users from using out-of-date AMIs. However, existing users and launch services, such as launch templates and Auto Scaling groups, can continue to use a deprecated AMI by specifying its ID. To delete the AMI so that users and services cannot use it, you must deregister it.
After an AMI is deprecated:
- For AMI users, the deprecated AMI does not appear in DescribeImages API calls unless you specify its ID or specify that deprecated AMIs must appear. AMI owners continue to see deprecated AMIs in DescribeImages API calls.
- For AMI users, the deprecated AMI is not available to select via the EC2 console. For example, a deprecated AMI does not appear in the AMI catalog in the launch instance wizard. AMI owners continue to see deprecated AMIs in the EC2 console.
- For AMI users, if you know the ID of a deprecated AMI, you can continue to launch instances using the deprecated AMI by using the API, CLI, or the SDKs.
- Launch services, such as launch templates and Auto Scaling groups, can continue to reference deprecated AMIs.
- EC2 instances that were launched using an AMI that is subsequently deprecated are not affected, and can be stopped, started, and rebooted.
You can deprecate both private and public AMIs.

Contents
- Costs
- Considerations
- Deprecate an AMI
- Describe deprecated AMIs
- Cancel AMI deprecation
### Costs When you deprecate an AMI, the AMI is not deleted. The AMI owner continues to pay for the AMI's snapshots. To stop paying for the snapshots, the AMI owner must delete the AMI by deregistering it.
### Considerations
- To deprecate an AMI, you must be the owner of the AMI.
- AMIs that have not been used recently to launch an instance might be good candidates for deprecation or deregistering. For more information, see the section called "Check when an AMI was last used".
- You can create Amazon Data Lifecycle Manager EBS-backed AMI policies to automate the deprecation of EBS-backed AMIs. For more information, see Create AMI lifecycle policies.
- By default, the deprecation date of all public AMIs is set to two years from the AMI creation date.
You can set the deprecation date to earlier than two years. To cancel the deprecation date, or to move the deprecation to a later date, you must make the AMI private by only sharing it with specific AWS accounts.
### Deprecate an AMI You can deprecate an AMI on a specific date and time. You must be the owner of the AMI.
The upper limit for the deprecation date is 10 years from now, except for public AMIs, where the upper limit is 2 years from the creation date. You can't specify a date in the past.

Console To deprecate an AMI on a specific date
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the left navigator, choose AMIs.
3. From the filter bar, choose Owned by me.
4. Select the AMI, and then choose Actions, Manage AMI Deprecation. You can select multiple AMIs to set the same deprecation date of several AMIs at once.
5. Select the Enable checkbox, and then enter the deprecation date and time.
6. Choose Save.
AWS CLI To deprecate an AMI on a specific date Use the enable-image-deprecation command. If you specify a value for seconds, Amazon EC2 rounds the seconds to the nearest minute. aws ec2 enable-image-deprecation \ --image-id ami-0abcdef1234567890 \ --deprecate-at "2025-04-15T13:17:12.000Z"
PowerShell To deprecate an AMI on a specific date Use the Enable-EC2ImageDeprecation cmdlet. If you specify a value for seconds, Amazon EC2 rounds the seconds to the nearest minute.
Enable-EC2ImageDeprecation `
    -ImageId ami-0abcdef1234567890 `
    -DeprecateAt 2025-04-15T13:17:12.000Z
### Describe deprecated AMIs You can view the deprecation date and time of an AMI, and filter AMIs by deprecation date.

Console To view the deprecation date of an AMI
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the left navigator, choose AMIs, and then select the AMI.
3. Check the Deprecation time field (if you selected the checkbox next to the AMI, it's located on the Details tab). The field shows the deprecation date and time of the AMI. If the field is empty, the AMI is not deprecated.
To filter AMIs by deprecation date
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the left navigator, choose AMIs.
3. From the filter bar, choose Owned by me or Private images (private images include AMIs that are shared with you as well as owned by you).
4. In the Search bar, enter Deprecation time (as you enter the letters, the Deprecation time filter appears), and then choose an operator and a date and time.
AWS CLI When you describe all AMIs, the results depend on whether you are an AMI user or the AMI owner.
- AMI user – By default, when you describe all AMIs, deprecated AMIs that are shared with you but not owned by you are excluded. To include deprecated AMIs in the results, specify the -- include-deprecated option.
- AMI owner – When you describe all AMIs, all AMIs that you own, including deprecated AMIs, are included. You can't exclude deprecated AMIs that you own by using the --no-include- deprecated option.
To include deprecated AMIs when describing all AMIs for an account Use the following describe-images command. aws ec2 describe-images --owners 123456789012 \

    --include-deprecated To describe the deprecated AMIs for your account Use the following describe-images command. aws ec2 describe-images \ --owners self \ --query "Images[?DeprecationTime!=null].ImageId" \ --output text The following is example output. ami-0abcdef1234567890 To describe the deprecation date of an AMI Use the following describe-images command. If DeprecationTime is not present in the output, the AMI is not deprecated or set to deprecate at a future date. aws ec2 describe-images \ --image-ids ami-0abcdef1234567890 \ --query Images[].DeprecationTime \ --output text The following is example output.
2025-05-01T00:00:00.000Z PowerShell To list the deprecated AMIs for your account Use the Get-EC2Image cmdlet.
(Get-EC2Image -Owner self | Where-Object {$_.DeprecationTime -ne $null}).ImageId The following is example output. ami-0abcdef1234567890

To describe the deprecation date of an AMI Use the Get-EC2Image cmdlet. If DeprecationTime is not present in the output, the AMI is not deprecated or set to deprecate at a future date.
(Get-EC2Image -ImageId ami-0abcdef1234567890).DeprecationTime The following is example output.
2025-05-01T00:00:00.000Z
### Cancel AMI deprecation You can cancel the deprecation of an AMI, which removes the deprecation date and time. You must be the AMI owner to perform this procedure.
Console To cancel the deprecation of an AMI
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the left navigator, choose AMIs.
3. From the filter bar, choose Owned by me.
4. Select the AMI, and then choose Actions, Manage AMI Deprecation. You can select multiple AMIs to cancel the deprecation of several AMIs at once.
5. Clear the Enable checkbox, and then choose Save.
AWS CLI To cancel the deprecation of an AMI Use the following disable-image-deprecation command. aws ec2 disable-image-deprecation --image-id ami-0abcdef1234567890 PowerShell To cancel the deprecation of an AMI

Use the Disable-EC2ImageDeprecation cmdlet.
Disable-EC2ImageDeprecation -ImageId ami-0abcdef1234567890
## Disable an Amazon EC2 AMI You can disable an AMI to prevent it from being used for instance launches. You can't launch new instances from a disabled AMI. You can re-enable a disabled AMI so that it can be used again for instance launches.
You can disable both private and public AMIs.
To reduce storage costs for disabled EBS-backed AMIs that are rarely used, but which need to be retained long term, you can archive their associated snapshots. For more information, see Archive Amazon EBS snapshots in the Amazon EBS User Guide.
Contents
- How AMI disable works
- Costs
- Prerequisites
- Required IAM permissions
- Disable an AMI
- Describe disabled AMIs
- Re-enable a disabled AMI
### How AMI disable works Warning Disabling an AMI removes all its launch permissions.
When an AMI is disabled:
- The AMI's state changes to disabled.

- A disabled AMI can't be shared. If an AMI was public or previously shared, it is made private. If an AMI was shared with an AWS account, organization, or Organizational Unit, they lose access to the disabled AMI.
- A disabled AMI does not appear in DescribeImages API calls by default.
- A disabled AMI does not appear under the Owned by me console filter. To find disabled AMIs, use the Disabled images console filter.
- A disabled AMI is not available to select for instance launches in the EC2 console. For example, a disabled AMI does not appear in the AMI catalog in the launch instance wizard or when creating a launch template.
- Launch services, such as launch templates and Auto Scaling groups, can continue to reference disabled AMIs. Subsequent instance launches from a disabled AMI will fail, so we recommend updating launch templates and Auto Scaling groups to reference available AMIs only.
- EC2 instances that were previously launched using an AMI that is subsequently disabled are not affected, and can be stopped, started, and rebooted.
- You can't delete snapshots associated with disabled AMIs. Attempting to delete an associated snapshot results in the snapshot is currently in use error.
When an AMI is re-enabled:
- The AMI's state changes to available, and it can be used to launch instances.
- The AMI can be shared.
- AWS accounts, organizations, and Organizational Units that lost access to the AMI when it was disabled do not regain access automatically, but the AMI can be shared with them again.
### Costs When you disable an AMI, the AMI is not deleted. If the AMI is an EBS-backed AMI, you continue to pay for the AMI's EBS snapshots. If you want to keep the AMI, you might be able to reduce your storage costs by archiving the snapshots. For more information, see Archive Amazon EBS snapshots in the Amazon EBS User Guide. If you don't want to keep the AMI and its snapshots, you must deregister the AMI and delete the snapshots. For more information, see Deregister an AMI.
### Prerequisites To disable or re-enable an AMI, you must be the owner of the AMI.

### Required IAM permissions To disable and re-enable an AMI, you must have the following IAM permissions:
- ec2:DisableImage
- ec2:EnableImage
### Disable an AMI You can disable an AMI by using the EC2 console or the AWS Command Line Interface (AWS CLI).
You must be the AMI owner to perform this procedure.
Console To disable an AMI
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the left navigation pane, choose AMIs.
3. From the filter bar, choose Owned by me.
4. Select the AMI, and then choose Actions, Disable AMI. You can select multiple AMIs to disable at once.
5. In the Disable AMI window, choose Disable AMI.
AWS CLI To disable an AMI Use the following disable-image command. aws ec2 disable-image --image-id ami-0abcdef1234567890 PowerShell To disable an AMI Use the Disable-EC2Image cmdlet.
Disable-EC2Image -ImageId ami-0abcdef1234567890

### Describe disabled AMIs You can view disabled AMIs in the EC2 console and by using the AWS CLI.
You must be the AMI owner to view disabled AMIs. Because disabled AMIs are made private, you can't view disabled AMIs if you're not the owner.
Console To view disabled AMIs
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the left navigation pane, choose AMIs.
3. From the filter bar, choose Disabled images.
AWS CLI By default, when you describe all AMIs, the disabled AMIs are not included in the results. To include disabled AMIs in the results, specify the --include-disabled option. The State field for an AMI is disabled if the AMI is disabled.
To include disabled AMIs when describing all AMIs for an account Use the following describe-images command. aws ec2 describe-images \ --owners 123456789012 \ --include-disabled To list the disabled AMIs for your account

Use the following describe-images command. aws ec2 describe-images \ --owners self \ --include-disabled \ --filters Name=state,Values=disabled \ --query Images[].ImageId \ --output text The following is example output. ami-0abcdef1234567890 To describe the status of an AMI Use the following describe-images command. If DeprecationTime is not present in the output, the AMI is not deprecated or set to deprecate at a future date. aws ec2 describe-images \ --image-ids ami-0abcdef1234567890 \ --query Images[].State \ --output text The following is example output. disabled PowerShell By default, when you describe all AMIs, the disabled AMIs are not included in the results. To include disabled AMIs in the results, specify the -IncludeDisabled parameter. The State field for an AMI is disabled if the AMI is disabled.
To list the disabled AMIs for your account Use the Get-EC2Image cmdlet.
(Get-EC2Image `
    -Owner self `
    -IncludeDisabled $true | Where-Object {$_.State -eq "disabled"}).ImageId

The following is example output. ami-0abcdef1234567890 To describe the status of an AMI Use the Get-EC2Image cmdlet.
(Get-EC2Image -ImageId ami-0abcdef1234567890).State.Value The following is example output. disabled
### Re-enable a disabled AMI You can re-enable a disabled AMI. You must be the AMI owner to perform this procedure.
Console To re-enable a disabled AMI
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the left navigation pane, choose AMIs.
3. From the filter bar, choose Disabled images.
4. Select the AMI, and then choose Actions, Enable AMI. You can select multiple AMIs to re- enable several AMIs at once.
5. In the Enable AMI window, choose Enable.
AWS CLI To re-enable a disabled AMI Use the following enable-image command. aws ec2 enable-image --image-id ami-0abcdef1234567890

PowerShell To re-enable a disabled AMI Use the Enable-EC2Image cmdlet.
Enable-EC2Image -ImageId ami-0abcdef1234567890
## Deregister an Amazon EC2 AMI When you deregister an AMI, Amazon EC2 permanently deletes it. After you deregister an AMI, you can't use it to launch new instances. You might consider deregistering an AMI when you have finished using it.
To protect against accidental or malicious deregistering of an AMI, you can turn on deregistration protection. If you accidentally deregister an EBS-backed AMI, you can use the Recycle Bin to restore it only if you restore it within the allowed time period before it is permanently deleted.
When deregistering an AMI, you can optionally delete its associated snapshots at the same time.
However, if a snapshot is associated with multiple AMIs, it won't be deleted even if specified for deletion, although the AMI will still be deregistered. Any snapshots not deleted will continue to incur storage costs.
Deregistering an AMI has no effect on any instances that were launched from the AMI. You can continue to use these instances. By default, deregistering an AMI also has no effect on any snapshots that were created during the AMI creation process. You'll continue to incur usage costs for these instances and storage costs for the snapshots. Therefore, to avoid incurring unnecessary costs, we recommend that you terminate any instances and delete any snapshots that you do not need. You can delete the snapshots either automatically during deregistration or manually after deregistration. For more information, see Avoid costs from unused resources.
For instances launched from an AMI that is subsequently deregistered, you can still view some high-level information about the AMI by using the describe-instance-image-metadata AWS CLI command. For more information, see describe-instance-image-metadata.
Contents
- Considerations
- Deregister an AMI
- Avoid costs from unused resources

- Protect an Amazon EC2 AMI from deregistration Considerations
- You can't deregister an AMI that is not owned by your account.
- You can't use Amazon EC2 to deregister an AMI that is managed by the AWS Backup service.
Instead, use AWS Backup to delete the corresponding recovery points in the backup vault. For more information, see Deleting backups in the AWS Backup Developer Guide.
### Deregister an AMI You can deregister EBS-backed AMIs and Amazon S3-backed AMIs. For EBS-backed AMIs, you can optionally delete the associated snapshots at the same time. However, if a snapshot is associated with other AMIs, it will not be deleted even if specified for deletion.
Console To deregister an AMI
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose AMIs.
3. From the filter bar, choose Owned by me to list your available AMIs, or choose Disabled images to list your disabled AMIs.
4. Select the AMI to deregister.
5. Choose Actions, Deregister AMI.
6. (Optional) To delete the associated snapshots during deregistration, select the Delete associated snapshots checkbox.
Note If a snapshot is associated with other AMIs, it is not deleted, even if the checkbox is selected.
7. Choose Deregister AMI.
It might take a few minutes before the console removes the AMI from the list. Choose Refresh to refresh the status.

AWS CLI To deregister an AMI Use the following deregister-image command. aws ec2 deregister-image --image-id ami-0abcdef1234567890 To deregister an AMI and delete its associated snapshots Use the following deregister-image command and specify the --delete-associated- snapshots parameter. Note that if a snapshot is associated with other AMIs, it is not deleted, even if you specify this parameter. aws ec2 deregister-image \ --image-id ami-0abcdef1234567890 \ --delete-associated-snapshots PowerShell To deregister an AMI Use the Unregister-EC2Image cmdlet.
Unregister-EC2Image -ImageId ami-0abcdef1234567890 To deregister an AMI and delete its associated snapshots Use the Unregister-EC2Image cmdlet and specify the -DeleteAssociatedSnapshots parameter. Note that if a snapshot is associated with other AMIs, it is not deleted, even if you specify this parameter.
Unregister-EC2Image `
    -ImageId ami-0abcdef1234567890 `
    -DeleteAssociatedSnapshots
### Avoid costs from unused resources Deregistering an AMI doesn't, by default, delete all of the resources that are associated with the AMI. These resources include the snapshots for EBS-backed AMIs and the files in Amazon S3

for Amazon S3-backed AMIs. When you deregister an AMI, you also don't terminate or stop any instances launched from the AMI.
You will continue to incur costs for storing the snapshots and files, and you will incur costs for any running instances.
To avoid incurring these types of unnecessary costs, we recommend deleting any resources that you don't need.
EBS-backed AMIs
- Delete the associated snapshots while deregistering the AMI. For more information, see Deregister an AMI.
- If you deregister an AMI without deleting its associated snaphots, you can manually delete the snapshots. The snapshot of the instance root volume created during AMI creation has the following description format:
Created by CreateImage(i-1234567890abcdef0) for ami-0abcdef1234567890
- If you no longer need the instances that were launched from the AMI, you can stop or terminate them. To list the instances, filter by the ID of the AMI.
Amazon S3-backed AMIs
- Delete the bundle in Amazon S3 by using the ec2-delete-bundle (AMI tools) command.
- If the Amazon S3 bucket is empty after you delete the bundle, and you have no further use for that bucket, you can delete the bucket.
- If you no longer need the instances that were launched from the AMI, you can terminate them.
To list the instances, filter by the ID of the AMI.
### Protect an Amazon EC2 AMI from deregistration You can turn on deregistration protection on an AMI to prevent accidental or malicious deletion.
When you turn on deregistration protection, the AMI can't be deregistered by any user, regardless of their IAM permissions. If you want to deregister the AMI, you must first turn off the deregistration protection on it.
When you turn on deregistration protection on an AMI, you have the option to include a 24-hour cooldown period. This cooldown period is the time during which deregistration protection remains

in effect after you turn it off. During this cooldown period, the AMI can't be deregistered. When the cooldown period ends, the AMI can be deregistered.
Deregistration protection is turned off by default on all existing and new AMIs.
#### Turn on deregistration protection Use the following procedures to turn on deregistration protection.
Console To turn on deregistration protection
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose AMIs.
3. From the filter bar, choose Owned by me to list your available AMIs, or choose Disabled images to list your disabled AMIs.
4. Select the AMI on which you want to turn on deregistration protection, and then choose Actions, Manage AMI deregistration protection.
5. In the Manage AMI deregistration protection dialog box, you can turn on deregistration protection with or without a cooldown period. Choose one of the following options:
- Enable with a 24-hour cooldown period – With a cooldown period, the AMI can't be deregistered for 24 hours when deregistration protection is turned off.
- Enable without cooldown – Without a cooldown period, the AMI can be deregistered immediately when deregistration protection is turned off.
6. Choose Save.
AWS CLI To turn on deregistration protection Use the enable-image-deregistration-protection command. To enable the optional cooldown period, include the --with-cooldown option. aws ec2 enable-image-deregistration-protection \ --image-id ami-0abcdef1234567890 \ --with-cooldown

PowerShell To turn on deregistration protection Use the Enable-EC2ImageDeregistrationProtection cmdlet. To enable the optional cooldown period, set the -WithCooldown parameter to true.
Enable-EC2ImageDeregistrationProtection `
    -ImageId ami-0abcdef1234567890 `
    -WithCooldown $true
#### Turn off deregistration protection Use the following procedures to turn off deregistration protection.
If you chose to include a 24-hour cooldown period when you turned on deregistration protection for the AMI, then, when you turn off deregistration protection, you won't immediately be able to deregister the AMI. The cooldown period is the 24-hour time period during which deregistration protection remains in effect even after you turn it off. During this cooldown period, the AMI can't be deregistered. After the cooldown period ends, the AMI can be deregistered.
Console To turn off deregistration protection
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose AMIs.
3. From the filter bar, choose Owned by me to list your available AMIs, or choose Disabled images to list your disabled AMIs.
4. Select the AMI to turn off deregistration protection, and then choose Actions, Manage AMI deregistration protection.
5. In the Manage AMI deregistration protection dialog box, choose Disable.
6. Choose Save.
AWS CLI To turn off deregistration protection
