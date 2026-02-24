# Application consistent Windows VSS based Amazon EBS snapshots

Source: apps/user-manuals/aws/ec2-ug.pdf

---

Note For MySQL and MariaDB, you must use -C 16384 to match the database page size.
Setting allocation granularity to a value other than a multiple of the page size can result in allocations that might be mismatched with torn write prevention boundaries of the storage device.
For example:
$  mkfs.ext4 -O bigalloc -C 16384 /dev/nvme1n1
2. Configure InnoDB to use the 0_DIRECT flushing method and turn off InnoDB doublewrite. Use your preferred text editor to open /etc/my.cnf, and update the innodb_flush_method and innodb_doublewrite parameters as follows: innodb_flush_method=O_DIRECT innodb_doublewrite=0 Important If you are using Logical Volume Manager (LVM) or other storage virtualization layer, make sure that the starting offsets of the volumes are aligned on 16 KiB multiples. This is relative to the underlying NVMe storage to account for the metadata headers and superblocks used by the storage virtualization layer. If you add an offset to the LVM physical volume, it can cause misalignment between the file system allocations and the NVMe device's offsets, which would invalidate torn write prevention. For more information, see -- dataalignmentoffset in the Linux manual page.
# Application consistent Windows VSS based Amazon EBS snapshots snapshots You can take application-consistent snapshots of all Amazon EBS volumes attached to your Amazon EC2 Windows instances using AWS Systems Manager Run Command. The snapshot

process uses the Windows Volume Shadow Copy Service (VSS) to take EBS volume level backups of VSS-aware applications. The snapshots include data from pending transactions between these applications and the disk. You don't have to shut down your instances or disconnect them when you need to back up all attached volumes.
There is no additional cost to use VSS based EBS snapshots. You only pay for EBS snapshots created by the backup process. For more information, see How am I billed for my Amazon EBS snapshots?
Note Application consistent Windows VSS based snapshots are supported with Windows instances only.
Contents
- What is VSS?
- How the VSS based Amazon EBS snapshot solution works
- Prerequisites to create Windows VSS based EBS snapshots
- Create VSS based EBS snapshots for your EC2 Windows instance
- Troubleshoot Windows VSS based EBS snapshots
- Use the AWS VSS solution to restore data for your instance
- AWS VSS solution version history
## What is VSS?
Volume Shadow Copy Service (VSS) is a backup and recovery technology included in Microsoft Windows. It can create backup copies, or snapshots, of computer files or volumes while they are in use. For more information, see  Volume Shadow Copy Service.
To create an application-consistent snapshot, the following software components are involved.
- VSS service — Part of the Windows operating system
- VSS requester — The software that requests the creation of shadow copies
- VSS writer — Typically provided as part of an application, such as SQL Server, to ensure a consistent data set to back up

- VSS provider — The component that creates the shadow copies of the underlying volumes The Windows VSS based Amazon EBS snapshot solution consists of multiple Systems Manager (SSM) Run Command documents that facilitate backup creation, and a  Systems Manager Distributor package, called AwsVssComponents, that includes an EC2 VSS requester and an EC2 VSS provider. The AwsVssComponents package must be installed on EC2 Windows instances to take application-consistent snapshots of EBS volumes. The following diagram illustrates the relationship between these software components.
## How the VSS based Amazon EBS snapshot solution works The process for taking application-consistent, VSS based EBS snapshot scripts consists of the following steps.
1. Complete the Prerequisites to create Windows VSS based EBS snapshots.
2. Enter parameters for the AWSEC2-VssInstallAndSnapshot SSM document and run this document by using Run Command. For more information, see Run the AWSEC2- VssInstallAndSnapshot command document (recommended).
3. The Windows VSS service on your instance coordinates all ongoing I/O operations for running applications.

4. The system flushes all I/O buffers and temporarily pauses all I/O operations. The pause lasts, at most, ten seconds.
5. During the pause, the system creates snapshots of all volumes attached to the instance.
6. The pause is lifted and I/O resumes operation.
7. The system adds all newly-created snapshots to the list of EBS snapshots. The system tags all VSS based EBS snapshots successfully created by this process with AppConsistent:true.
8. If you need to restore from a snapshot, you can use the standard EBS process of creating a volume from a snapshot, or you can restore all volumes to an instance by using a sample script, as described in Use the AWS VSS solution to restore data for your instance.
## Prerequisites to create Windows VSS based EBS snapshots You can create VSS based EBS snapshots with Systems Manager Run Command, AWS Backup, or Amazon Data Lifecycle Manager. The following prerequisites apply for all solutions.
### System requirements Ensure that your EC2 Windows instance meets all of the system requirements to create VSS based snapshots, including supported versions of the Windows operating system, .NET framework, PowerShell, AWS Tools for Windows PowerShell, and the AWS Systems Manager Agent.
IAM permissions The IAM role that's attached to your Amazon EC2 Windows instance must have permission to create application-consistent snapshots with VSS. To grant the necessary permissions, you can attach the AWSEC2VssSnapshotPolicy managed policy to your instance profile.
VSS components To create application-consistent snapshots on Windows operating systems, the AwsVssComponents package must be installed on the instance. The package contains an on- instance EC2 VSS Agent that functions as the VSS requester, and an EC2 VSS provider for EBS volumes.

System requirements Install the Systems Manager Agent VSS is orchestrated by the Systems Manager Agent using PowerShell. Ensure that you have installed SSM Agent version 3.0.502.0 or later on your EC2 instance. If you are already using an older version of the SSM Agent, update it using Run Command. For more information, see  Setting up Systems Manager for Amazon EC2 instances and Working with SSM Agent on Amazon EC2 instances for Windows Server in the AWS Systems Manager User Guide.
Amazon EC2 Windows instance requirements VSS based EBS snapshots are supported for instances running Windows Server 2016 and later.
.NET Framework version The AwsVssComponents package requires .NET Framework version 4.6 or later. Windows operating system versions prior to Windows Server 2016 default to an earlier version of the .NET Framework. If your instance uses an earlier version of the .NET Framework, you must install version 4.6 or later using Windows Update.
AWS Tools for Windows PowerShell version Ensure that your instance is running AWS Tools for Windows PowerShell version 3.3.48.0 or later. To check your version, run the following command in the PowerShell terminal on the instance.
C:\> Get-AWSPowerShellVersion If you need to update AWS Tools for Windows PowerShell on your instance, see  Installing the AWS Tools for Windows PowerShell in the AWS Tools for PowerShell User Guide.
Windows PowerShell version Ensure that your instance is running Windows PowerShell major version 3, 4, or 5. To check your version, run the following command in a PowerShell terminal on the instance.
C:\> $PSVersionTable.PSVersion PowerShell language mode Ensure that your instance has the PowerShell language mode set to FullLanguage. For more information, see  about_Language_Modes in the Microsoft documentation.

### Use an IAM managed policy to grant permissions for VSS based snapshots The AWSEC2VssSnapshotPolicy managed policy enables Systems Manager to perform the following actions on your Windows instance:
- Create and tag EBS snapshots
- Create and tag Amazon Machine Images (AMIs)
- Attach metadata, such as the device ID, to the default snapshot tags that VSS creates.
This topic covers permission details for the VSS managed policy, and how to attach it to your EC2 instance profile IAM role.
Contents
- AWSEC2VssSnapshotPolicy managed policy details
- Attach the VSS snapshot managed policy to your instance profile role
#### AWSEC2VssSnapshotPolicy managed policy details An AWS managed policy is a standalone policy that Amazon provides for AWS customers. AWS managed policies are designed to grant permissions for common use cases. You can't change the permissions that are defined in AWS managed policies. However, you can copy the policy and use it as a baseline for a customer managed policy that is specific to your use case.
For more information about AWS managed policies, see AWS managed policies in the IAM User Guide.
To use the AWSEC2VssSnapshotPolicy managed policy, you can attach it to the IAM role that's attached to your EC2 Windows Instances. This policy enables the EC2 VSS solution to create and add tags to Amazon Machine Images (AMIs) and EBS Snapshots. To attach the policy, see Attach the VSS snapshot managed policy to your instance profile role.
##### Permissions granted by AWSEC2VssSnapshotPolicy The AWSEC2VssSnapshotPolicy policy includes the following Amazon EC2 permissions to allow Amazon EC2 to create and manage VSS snapshots on your behalf. You can attach this managed policy to the IAM instance profile role that you use for your EC2 Windows instances.
- ec2:CreateTags – Add tags to EBS snapshots and AMIs to help identify and categorize the resources.

- ec2:DescribeInstanceAttribute – Retrieve the EBS volumes and corresponding block device mappings that are attached to the target instance.
- ec2:CreateSnapshots – Create snapshots of EBS volumes.
- ec2:CreateImage – Create an AMI from a running EC2 instance.
- ec2:DescribeImages – Retrieve the information for EC2 AMIs and snapshots.
- ec2:DescribeSnapshots – Determine the create time and status of snapshots to verify application consistency.
Note To view permission details for this policy, see AWSEC2VssSnapshotPolicy in the AWS Managed Policy Reference.
##### Streamline permissions for specific use cases - advanced The AWSEC2VssSnapshotPolicy managed policy includes permissions for all of the ways that you can create VSS based snapshots. You can create a custom policy that includes only the permissions that you need.
Use case: Create AMI, Use case: Use AWS Backup service If you exclusively use the CreateAmi option, or if you create VSS based snapshots only through the AWS Backup service, then you can streamline the policy statements as follows.
- Omit policy statements identified by the following statement IDs (SIDs):
- CreateSnapshotsWithTag
- CreateSnapshotsAccessInstance
- CreateSnapshotsAccessVolume
- Adjust the CreateTagsOnResourceCreation statement as follows:
- Remove arn:aws:ec2:*:*:snapshot/* from the resources.
- Remove CreateSnapshots from the ec2:CreateAction condition.
- Adjust the CreateTagsAfterResourceCreation statement to remove arn:aws:ec2:*:*:snapshot/* from the resources.

- Adjust the DescribeImagesAndSnapshots statement to remove ec2:DescribeSnapshots from the statement action.
Use case: Snapshot only If you don't use the CreateAmi option, then you can streamline the policy statements as follows.
- Omit policy statements identified by the following statement IDs (SIDs):
- CreateImageAccessInstance
- CreateImageWithTag
- Adjust the CreateTagsOnResourceCreation statement as follows:
- Remove arn:aws:ec2:*:*:image/* from the resources.
- Remove CreateImage from the ec2:CreateAction condition.
- Adjust the CreateTagsAfterResourceCreation statement to remove arn:aws:ec2:*:*:image/* from the resources.
- Adjust the DescribeImagesAndSnapshots statement to remove ec2:DescribeImages from the statement action.
Note To ensure that your customized policy performs as expected, we recommend that you regularly review and incorporate updates to the managed policy.
#### Attach the VSS snapshot managed policy to your instance profile role To grant permissions for VSS based snapshots for your EC2 Windows instance, you can attach the AWSEC2VssSnapshotPolicy managed policy to your instance profile role as follows. It's important to ensure that your instance meets all System requirements.
Note To use the managed policy, your instance must have the AwsVssComponents package version 2.3.1 or later installed. For version history, see AwsVssComponents package versions.

1. Open the IAM console at https://console.aws.amazon.com/iam/.
2. In the navigation pane, choose Roles to see a list of IAM roles that you have access to.
3. Select the Role name link for the role that's attached to your instance. This opens the role detail page.
4. To attach the managed policy, choose Add permissions, located in the upper right corner of the list panel. Then select Attach policies from the dropdown list.
5. To streamline results, enter the policy name in the search bar (AWSEC2VssSnapshotPolicy).
6. Select the checkbox next to the name of the policy to attach, and choose Add permissions.
### Manage VSS components package for Windows VSS based EBS snapshots Before you create VSS based EBS snapshots, ensure that you have the latest version of the VSS components package installed on your Windows instance. There are several ways that you can install the AwsVssComponents package onto an existing instance, as follows:
- (Recommended) Run the AWSEC2-VssInstallAndSnapshot command document (recommended).
This automatically installs or updates if needed every time it runs.
- Manually install the VSS components on an EC2 Windows instance.
- Update the VSS components package on your EC2 Windows instance.
You can also create an AMI with EC2 Image Builder that uses the aws-vss-components-windows managed component to install the AwsVssComponents package for the image. The managed component uses AWS Systems Manager Distributor to install the package. After Image Builder creates the image, every instance that you launch from the associated AMI will have the VSS package installed on it. For more information about how you can create an AMI with the VSS package installed, see Distributor package managed components for Windows in the EC2 Image Builder User Guide.
Contents
- Manually install the VSS components on an EC2 Windows instance
- Update the VSS components package on your EC2 Windows instance

#### Manually install the VSS components on an EC2 Windows instance Your EC2 Windows instance must have VSS components installed before you can create application-consistent snapshots with Systems Manager. If you don't run the AWSEC2- VssInstallAndSnapshot command document to automatically install or update the package every time you create application-consistent snapshots, you must manually install the package.
You must also install manually if you plan to use one of the following methods to create application-consistent snapshots from your EC2 instance.
- Create VSS snapshots using AWS Backup
- Create VSS snapshots using Amazon Data Lifecycle Manager If you need to perform a manual install, we recommend that you use the latest AWS VSS component package to improve the reliability and performance of application-consistent snapshots on your EC2 Windows instances.
Note To automatically install or update the AwsVssComponents package whenever you create application-consistent snapshots, we recommend that you use Systems Manager to run the AWSEC2-VssInstallAndSnapshot document. For more information, see Run the AWSEC2-VssInstallAndSnapshot command document (recommended).
To install the VSS components on an Amazon EC2 Windows instance, follow the steps for your preferred environment.
Console To install the VSS components using SSM Distributor
1. Open the AWS Systems Manager console at https://console.aws.amazon.com/systems- manager/.
2. In the navigation pane, choose Run Command.
3. Choose Run command.
4. For Command document, choose the button next to AWS-ConfigureAWSPackage.
5. For Command parameters, do the following:

a.
Verify that Action is set to Install. b.
For Name, enter AwsVssComponents. c.
For Version, enter a version or leave the field empty so that Systems Manager installs the latest version.
6. For Targets, identify the instances on which you want to run this operation by specifying tags or selecting instances manually.
Note If you choose to select instances manually, and an instance you expect to see is not included in the list, see Where Are My Instances? in the AWS Systems Manager User Guide for troubleshooting tips.
7. For Other parameters:
- (Optional) For Comment, type information about this command.
- For Timeout (seconds), specify the number of seconds for the system to wait before failing the overall command execution.
8. (Optional) For Rate control:
- For Concurrency, specify either a number or a percentage of instances on which to run the command at the same time.
Note If you selected targets by choosing Amazon EC2 tags, and you are not certain how many instances use the selected tags, then limit the number of instances that can run the document at the same time by specifying a percentage.
- For Error threshold, specify when to stop running the command on other instances after it fails on either a number or a percentage of instances. For example, if you specify three errors, then Systems Manager stops sending the command when the fourth error is received. Instances still processing the command might also send errors.
9. (Optional) For Output options section, if you want to save the command output to a file, select the box next to Enable writing to an S3 bucket. Specify the bucket and (optional) prefix (folder) names.

Note The S3 permissions that grant the ability to write the data to an S3 bucket are those of the instance profile assigned to the instance, not those of the user performing this task. For more information, see Configure EC2 instance permissions in the AWS Systems Manager User Guide.
10. (Optional) Specify options for SNS notifications.
For information about configuring Amazon SNS notifications for Run Command, see Configuring Amazon SNS Notifications for AWS Systems Manager.
11. Choose Run.
AWS CLI Use the following procedure to download and install the AwsVssComponents package on your instances by using Run Command from the AWS CLI. The package installs two components: a VSS requester and a VSS provider. The system copies these components to a directory on the instance, and then registers the provider DLL as a VSS provider.
To install the VSS package Run the following command to download and install the required VSS components for Systems Manager. aws ssm send-command \ --document-name "AWS-ConfigureAWSPackage" \ --instance-ids "i-1234567890abcdef0" \ --parameters '{"action":["Install"],"name":["AwsVssComponents"]}'
PowerShell Use the following procedure to download and install the AwsVssComponents package on your instances by using Run Command from the Tools for Windows PowerShell. The package installs two components: a VSS requester and a VSS provider. The system copies these components to a directory on the instance, and then registers the provider DLL as a VSS provider.
To install the VSS package

Run the following command to download and install the required VSS components for Systems Manager.
Send-SSMCommand `
    -DocumentName "AWS-ConfigureAWSPackage" `
    -InstanceId "i-1234567890abcdef0" `
    -Parameter @{'action'='Install';'name'='AwsVssComponents'}
##### Verify the signature on AWS VSS components Use the following procedure to verify the signature on the AwsVssComponents package.
1. Connect to your Windows instance. For more information, see Connect to your Windows instance using RDP.
2. Navigate to C:\Program Files\Amazon\AwsVssComponents.
3. Open the context (right-click) menu for ec2-vss-agent.exe, and then choose Properties.
4. Navigate to the Digital Signatures tab and verify that the name of the signer is Amazon Web Services Inc.
5. Use the preceding steps to verify the signature on Ec2VssInstaller and Ec2VssProvider.dll.
#### Update the VSS components package on your EC2 Windows instance We recommend that you keep the VSS components updated with the latest recommended version.
There are several different ways that you can update components when a new version of the AwsVssComponents package is released.
Update methods
- You can repeat the steps described in Manually install the VSS components on an EC2 Windows instance when a new version of the AWS VSS components is released.
- You can configure a Systems Manager State Manager association to automatically download and install new or updated VSS components when the AwsVssComponents package becomes available.
- You can automatically install or update the AwsVssComponents package whenever you create application-consistent snapshots, when you use Systems Manager to run the AWSEC2- VssInstallAndSnapshot document.

Note We recommend that you use Systems Manager to run the AWSEC2- VssInstallAndSnapshot command document, which automatically installs or updates the AwsVssComponents package before it creates the application-consistent snapshots.
For more information, see Run the AWSEC2-VssInstallAndSnapshot command document (recommended).
To create a Systems Manager State Manager association, follow the steps for your preferred environment.
Console When you create a Systems Manager State Manager association, there are two options for updating the AwsVssComponents package, as follows:
Uninstall and reinstall This method downloads and installs the package with no additional prerequisites.
In-place update This performs an in-place update for the package, and has the following prerequisites:
- The SSM Agent version that's installed on the instance must be version 3.3.808.0 or later. For more information, see Working with SSM Agent on EC2 instances for Windows Server in the AWS Systems Manager User Guide.
- If specified, the AwsVssComponents package version must be version 2.5.0 or later.
Earlier versions don't support in-place update.
Note if your instance doesn't meet these prerequisites, in-place update will fail. Use the Uninstall and reinstall option instead.
To create a State Manager association
1. Open the AWS Systems Manager console at https://console.aws.amazon.com/systems- manager/.

2. In the navigation pane, choose State Manager.
Or, if the Systems Manager homepage opens first, open the navigation pane and then choose State Manager.
3. Choose Create association.
4. In the Name field, enter a descriptive name.
5. In the Document list, choose AWS-ConfigureAWSPackage.
6. In the Parameters section, choose Install from the Action list.
7. For Installation type, choose either Uninstall and reinstall or In-place update.
8. In the Name field, enter AwsVssComponents. You can keep the Version and Additional Arguments fields empty.
9. In the Targets section, choose an option.
Note If you choose to target instances by using tags, and you specify tags that map to Linux instances, the association succeeds on the Windows instance but fails on the Linux instances. The overall status of the association shows Failed.
10. In the Specify schedule section, choose an option.
11. In the Advanced options section, for Compliance severity, choose a severity level for the association. For more information, see Learn about association compliance. For Change Calendars, select a preconfigured change calendar. For more information, see about AWS Systems Manager Change Calendar.
12. For Rate control, do the following:
- For Concurrency, specify either a number or a percentage of managed nodes on which to run the command at the same time.
- For Error threshold, specify when to stop running the command on other managed nodes after it fails on either a number or a percentage of nodes.
13. (Optional) For Output options, to save the command output to a file, select Enable writing output to S3. Enter the bucket and prefix (folder) names in the boxes.
14. Choose Create association, and then choose Close. The system attempts to create the association on the instances and immediately apply the state.

Note If EC2 instances for Windows Server show a status of Failed, verify that the SSM Agent is running on the instance, and verify that the instance is configured with an AWS Identity and Access Management (IAM) role for Systems Manager. For more information, see  Setting up AWS Systems Manager.
AWS CLI Use the create-association command to update a Distributor package on a schedule without taking the associated application offline. Only new or updated files in the package are replaced.
To create a State Manager association Run the following command to create an association. The value of --name, the document name, is always AWS-ConfigureAWSPackage. The following command uses the key InstanceIds to specify target instances. aws ssm create-association \ --name "AWS-ConfigureAWSPackage" \ --parameters action=Install,installationType="Uninstall and reinstall",name=AwsVssComponents \ --targets Key=InstanceIds,Values=i-1234567890abcdef0,i-000011112222abcde PowerShell To create a State Manager association Use the New-SSMAssociation cmdlet.
New-SSMAssociation `
    -Name "AWS-ConfigureAWSPackage" `
    -Parameter  @{ "action" = "Install"
        "installationType" = "Uninstall and reinstall"
        "name" = "AwsVssComponents"
    } `
    -Target @{ "Key" = "InstanceIds"
        "Values" = @("i-1234567890abcdef0", "i-000011112222abcde")

    }
## Create VSS based EBS snapshots for your EC2 Windows instance After you've met all of the Prerequisites to create Windows VSS based EBS snapshots, you can use any of the following methods to create VSS based snapshots from your EC2 instance.
AWS Systems Manager command documents Use Systems Manager command documents to create VSS based snapshots.
To automate backups, you can create an AWS Systems Manager maintenance window task that uses the AWSEC2-VssInstallAndSnapshot command document. For more information, see Working with Maintenance Windows (Console) in the AWS Systems Manager User Guide.
AWS Backup You can create a VSS backup when using AWS Backup by enabling VSS in the console or CLI. For more information, see Creating Windows VSS backups in the AWS Backup Developer Guide.
Note AWS Backup doesn't automatically install the AwsVssComponents package on your instance. You must perform a manual install on your instance. For more information, see Manually install the VSS components on an EC2 Windows instance.
Amazon Data Lifecycle Manager You can create VSS snapshots using Amazon Data Lifecycle Manager by enabling pre and post scripts in your snapshot lifecycle policies. For more information, see Automating application- consistent snapshots in the Amazon EBS User Guide.
Note Amazon Data Lifecycle Manager doesn't automatically install the AwsVssComponents package on your instance. You must perform a manual install on your instance. For more information, see Manually install the VSS components on an EC2 Windows instance.

### Use Systems Manager command documents to create VSS based snapshots You can use AWS Systems Manager command documents to create VSS based snapshots. The following content introduces the command documents that are available, and the runtime parameters that the documents use to create your snapshots.
Before you use any of the Systems Manager command documents, ensure that you've met all Prerequisites to create Windows VSS based EBS snapshots.
Topics
- Parameters for Systems Manager VSS snapshot documents
- Run Systems Manager VSS snapshot command documents
#### Parameters for Systems Manager VSS snapshot documents The Systems Manager documents that create VSS snapshots all use the following parameters, except where noted:
AmiName (string, optional)
If the CreateAmi option is set to True, specify the name of the AMI that the backup creates. description (string, optional)
Specify a description for the snapshots or image that this process creates.
CollectDiagnosticLogs (string, optional)
To collect more information during snapshot and AMI creation steps, set this parameter to "True". The default value for this parameter is "False". Consolidated diagnostic logs are saved as a .zip format archive at the following location on your instance:
C:\ProgramData\Amazon\AwsVss\Logs\timestamp.zip CopyOnly (string, optional)
If you use the native SQL Server backup in addition to AWS VSS, performing a Copy-only backup prevents AWS VSS from breaking the native differential backup chain. To perform a Copy-only backup operation, set this parameter to True.
The default value for this parameter is False, which causes AWS VSS to perform a full backup operation.

CreateAmi (string, optional)
To create a VSS based Amazon Machine Image (AMI) to back up your instance, set this parameter to True. The default value for this parameter is False, which backs up your instance with an EBS snapshot instead.
For more information about creating an AMI from an instance, see Create an Amazon EBS- backed AMI. executionTimeout (string, optional)
Specify the maximum time in seconds to run the snapshot creation process on the instance, or to create an AMI from the instance. Increasing this timeout allows the command to wait longer for VSS to start its freeze and complete tagging of the resources it creates. This timeout only applies to the snapshot or AMI creation steps. The initial step to install or update the AwsVssComponents package is not included in the timeout.
ExcludeBootVolume (string, optional)
This setting excludes boot volumes from the backup process if you create snapshots. To exclude boot volumes from your snapshots, set ExcludeBootVolume to True, and CreateAmi to False.
If you create an AMI for your backup, this parameter should be set to False. The default value for this parameter is False.
NoWriters (string, optional)
To exclude application VSS writers from the snapshot process, set this parameter to True.
Excluding application VSS writers can help you resolve conflicts with third-party VSS backup components. The default value for this parameter is False.
If SaveVssMetadata is True, this parameter must be set to False.
SaveVssMetadata (string, optional)
To save VSS metadata files during every snapshot, set this parameter to True. The default value is False. These files help provide insights into which components or writers were included in a backup operation, and the associated files and volumes for each snapshot. The metadata files are used when restoring a SQL database using VSS restore solution. For more information on how to restore a SQL database from VSS snapshots, see Use an automation runbook to restore your database from AWS VSS solution snapshots.
Metadata files have the associated snapshot set id in their names. You can find them at the following location on your instance:

C:\ProgramData\Amazon\AwsVss\VssMetadata\ Warning
- Saving VSS metadata files requires AwsVssComponents package version 2.4.0 or later. If your instance has an earlier version installed, setting SaveVssMetadata to True causes the snapshot creation to fail.
- The NoWriters and SaveVssMetadata parameters are mutually exclusive. If both are set to True then snapshot creation fails. tags (string, optional)
We recommend that you tag your snapshots and images to help you locate and manage your resources, for example, to restore volumes from a list of snapshots. The system adds the Name key, with a blank value where you can specify the name that you want to apply to your output snapshots or images.
If you want to specify additional tags, separate tags with a semicolon in between. For example, Key=Environment,Value=Test;Key=User,Value=TestUser1.
Note Tag keys and values must only contain alphanumeric characters and the following special characters: () ./\-"'@_+:={}.
By default, the system adds the following reserved tags for VSS based snapshots and images.
- Device – For VSS based snapshots, this is the device name of the EBS volume that the snapshot captures.
- AppConsistent – This tag indicates the successful creation of a VSS based snapshot or AMI.
- AwsVssConfig – This identifies snapshots and AMIs that are created with VSS enabled. The tag includes meta information such as the AwsVssComponents version, and the Snapshot Set ID.

Warning Specifying any of these reserved tags in your parameter list will cause an error.
VssVersion (string, optional)
For the AWSEC2-VssInstallAndSnapshot document only, you can specify the VssVersion parameter to install a specific version of AwsVssComponents package on your instance. Leave this parameter blank to install the recommended default version.
If the specified version of the AwsVssComponents package is already installed, the script skips the install step and moves on to the backup step. For a list of AwsVssComponents package versions and operating support, see AWS VSS solution version history.
#### Run Systems Manager VSS snapshot command documents You can create VSS based EBS snapshots with AWS Systems Manager command documents as follows.
##### Run the AWSEC2-VssInstallAndSnapshot command document (recommended)
When you use AWS Systems Manager to run the AWSEC2-VssInstallAndSnapshot document, the script runs the following steps.
1. The script first installs or updates the AwsVssComponents package on your instance, depending on whether it's already installed.
2. The script creates the application-consistent snapshots after the first step completes.
To run the AWSEC2-VssInstallAndSnapshot document, follow the steps for your preferred environment.
Console Create VSS based EBS snapshots from the console
1. Open the AWS Systems Manager console at https://console.aws.amazon.com/systems- manager/.

2. Select Run Command from the navigation pane. This shows a list of commands that are currently running in your account, if applicable.
3. Choose Run command. This opens a list of command documents that you have access to.
4. Select AWSEC2-VssInstallAndSnapshot from the list of command documents. To streamline results, you can enter all or part of the document name. You can also filter by the owner, by platform types, or by tags.
When you select a command document, details populate below the list.
5. Select Default version at runtime from the Document version list.
6. Configure the Command parameters to define how AWSEC2-VssInstallAndSnapshot will install the AwsVssComponents package and back up with VSS snapshots or an AMI.
For parameter details, see Parameters for Systems Manager VSS snapshot documents.
7. For Target selection, specify tags or select instances manually to identify the instances on which to run this operation.
Note If you select instances manually, and an instance you expect to see is not included in the list, see Where Are My Instances? for troubleshooting tips.
8. For additional parameters to define Systems Manager Run Command behavior such as Rate control, enter values as described in Running commands from the console.
9. Choose Run.
If successful, the command populates the list of EBS snapshots with the new snapshots.
You can locate these snapshots in the list of EBS snapshots by searching for the tags you specified, or by searching for AppConsistent. If the command execution failed, view the Systems Manager command output for details about why the execution failed.
If the command successfully completed, but a specific volume backup failed, you can troubleshoot the failure in the list of EBS volumes.
AWS CLI You can run the following commands in the AWS CLI to create VSS based EBS snapshots and get the status of your snapshot creation.
Create VSS based EBS snapshots

Run the following command to create VSS based EBS snapshots. To create the snapshots, you must identify the instances with the --instance-ids parameter. For more information about other parameters that you can use, see Parameters for Systems Manager VSS snapshot documents. aws ssm send-command \ --document-name "AWSEC2-VssInstallAndSnapshot" \ --instance-ids "i-01234567890abcdef" \ --parameters '{"ExcludeBootVolume":["False"],"description":["Description"],"tags":
["Key=key_name,Value=tag_value"],"VssVersion":[""]}'
If successful, the command document populates the list of EBS snapshots with the new snapshots. You can locate these snapshots in the list of EBS snapshots by searching for the tags you specified, or by searching for AppConsistent. If the command execution failed, view the command output for details about why the execution failed.
Get command status To get the current status of the snapshots, run the following command using the command ID returned from send-command. aws ssm get-command-invocation --instance-ids "i-01234567890abcdef" \ --command-id "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111" \ --plugin-name "CreateVssSnapshot"
PowerShell Run the following commands with AWS Tools for Windows PowerShell to create VSS based EBS snapshots and get the current runtime status for the creation of your output. Specify parameters described in the prior list to modify the behavior of the snapshot process.
Create VSS based EBS snapshots with Tools for Windows PowerShell Run the following command to create VSS based EBS snapshots or AMIs.
Send-SSMCommand -DocumentName "AWSEC2-VssInstallAndSnapshot" -InstanceId "i-01234567890abcdef" -Parameter @{'ExcludeBootVolume'='False';'description'='a_description'
 ;'tags'='Key=key_name,Value=tag_value';'VssVersion'=''}

Get command status To get the current status of the snapshots, run the following command using the command ID returned from Send-SSMCommand.
Get-SSMCommandInvocationDetail -InstanceId "i-01234567890abcdef" -CommandId "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111" -PluginName "CreateVssSnapshot"
If successful, the command populates the list of EBS snapshots with the new snapshots. You can locate these snapshots in the list of EBS snapshots by searching for the tags you specified, or by searching for AppConsistent. If the command execution failed, view the command output for details about why the execution failed.
##### Run the AWSEC2-CreateVssSnapshot command document To run the AWSEC2-CreateVssSnapshot document, follow the steps for your preferred environment.
Console Create VSS based EBS snapshots from the console
1. Open the AWS Systems Manager console at https://console.aws.amazon.com/systems- manager/.
2. Select Run Command from the navigation pane. This shows a list of commands that are currently running in your account, if applicable.
3. Choose Run command. This opens a list of command documents that you have access to.
4. Select AWSEC2-CreateVssSnapshot from the list of command documents. To streamline results, you can enter all or part of the document name. You can also filter by the owner, by platform types, or by tags.
When you select a command document, details populate below the list.
5. Select Default version at runtime from the Document version list.
6. Configure the Command parameters to define how AWSEC2-CreateVssSnapshot will back up with VSS snapshots or an AMI. For parameter details, see Parameters for Systems Manager VSS snapshot documents.
7. For Target selection, specify tags or select instances manually to identify the instances on which to run this operation.

Note If you select instances manually, and an instance you expect to see is not included in the list, see Where Are My Instances? for troubleshooting tips.
8. For additional parameters to define Systems Manager Run Command behavior such as Rate control, enter values as described in Running commands from the console.
9. Choose Run.
If successful, the command populates the list of EBS snapshots with the new snapshots.
You can locate these snapshots in the list of EBS snapshots by searching for the tags you specified, or by searching for AppConsistent. If the command execution failed, view the Systems Manager command output for details about why the execution failed.
If the command successfully completed, but a specific volume backup failed, you can troubleshoot the failure in the list of EBS volumes.
AWS CLI You can run the following command in the AWS CLI to create VSS based EBS snapshots.
Create VSS based EBS snapshots Run the following command to create VSS based EBS snapshots. To create the snapshots, you must identify the instances with the --instance-ids parameter. For more information about other parameters that you can use, see Parameters for Systems Manager VSS snapshot documents. aws ssm send-command \ --document-name "AWSEC2-CreateVssSnapshot" \ --instance-ids "i-01234567890abcdef" \ --parameters '{"ExcludeBootVolume":["False"],"description":["Description"],"tags":
["Key=key_name,Value=tag_value"]}'
If successful, the command document populates the list of EBS snapshots with the new snapshots. You can locate these snapshots in the list of EBS snapshots by searching for the tags you specified, or by searching for AppConsistent. If the command execution failed, view the command output for details about why the execution failed.

PowerShell Run the following command with AWS Tools for Windows PowerShell to create VSS based EBS snapshots.
Create VSS based EBS snapshots with Tools for Windows PowerShell Run the following command to create VSS based EBS snapshots. To create the snapshots, you must identify the instances with the InstanceId parameter. You can specify more than one instance to create snapshots for. For more information about other parameters that you can use, see Parameters for Systems Manager VSS snapshot documents.
Send-SSMCommand -DocumentName AWSEC2-CreateVssSnapshot -InstanceId "i-01234567890abcdef" -Parameter @{'ExcludeBootVolume'='False';'description'='a_description'
 ;'tags'='Key=key_name,Value=tag_value'} If successful, the command populates the list of EBS snapshots with the new snapshots. You can locate these snapshots in the list of EBS snapshots by searching for the tags you specified, or by searching for AppConsistent. If the command execution failed, view the command output for details about why the execution failed. If the command successfully completed, but a specific volume backup failed, you can troubleshoot the failure in the list of EBS snapshots.
##### Run command documents for a Windows Failover Cluster with shared EBS storage You can use any of the command line procedures described in the previous section to create a VSS based snapshot. The command document (AWSEC2-VssInstallAndSnapshot or AWSEC2- CreateVssSnapshot) must run on the primary node in your cluster. The document will fail on the secondary nodes as they don't have access to the shared disks. If your primary and secondary change dynamically, you can run the AWS Systems Manager Run Command document on multiple nodes with the expectation that the command will succeed on the primary node and fail on secondary nodes.
Note To automate backups, you can create an AWS Systems Manager maintenance window task that uses the AWSEC2-VssInstallAndSnapshot document. For more information, see Working with Maintenance Windows (Console) in the AWS Systems Manager User Guide.

## Troubleshoot Windows VSS based EBS snapshots Before you try any other troubleshooting steps, we recommend that you verify the following details.
- Ensure that you've met all Prerequisites to create Windows VSS based EBS snapshots.
- Verify that you're using the latest Windows OS version support of the AwsVssComponents package for your operating system. The issue that you've observed might have been addressed in newer versions.
Topics
- Check log files
- Collect additional diagnostic logs
- Use VSS on instances with proxy configured
- Error: Thaw pipe connection timed out, error on thaw, timeout waiting for VSS Freeze, or other timeout errors
- Error: Cannot invoke method. Method invocation is supported only on core types in this language mode
### Check log files If you experience problems or receive error messages when you create VSS based EBS snapshots, you can view the command output in the Systems Manager console.
For Systems Manager documents that create VSS snapshots, you can set the CollectDiagnosticLogs parameter to "True" at runtime. When the CollectDiagnosticLogs parameter is set to "True", VSS collects additional logs to aid in debugging. For more information, see Collect additional diagnostic logs.
If you collect diagnostic logs, the Systems Manager document stores them on your instance at the following location: C:\ProgramData\Amazon\AwsVss\Logs\timestamp.zip. The default for the CollectDiagnosticLogs parameter is "False".
Note For additional debugging help, you can send the .zip file to Support.

The following additional logs are available, whether you collect diagnostic logs or not:
- %ProgramData%\Amazon\SSM\InstanceData\InstanceID\document\orchestration \SSMCommandID\awsrunPowerShellScript\runPowerShellScript\stdout
- %ProgramData%\Amazon\SSM\InstanceData\InstanceID\document\orchestration \SSMCommandID\awsrunPowerShellScript\runPowerShellScript\stderr You can also open the Event Viewer Windows application and choose Windows Logs, Application to view additional logs. To see events specifically from the EC2 Windows VSS Provider and the Volume Shadow Copy Service, filter by Source on the terms Ec2VssSoftwareProvider and VSS.
If you're using Systems Manager with VPC endpoints, and the Systems Manager send-command API action (Run Command in the console) failed, verify that you configured the following endpoint correctly: com.amazonaws.region.ec2.
Without the Amazon EC2 endpoint defined, the call to enumerate attached EBS volumes fails, which causes the Systems Manager command to fail. For more information about setting up VPC endpoints with Systems Manager, see Create a Virtual Private Cloud Endpoint in the AWS Systems Manager User Guide.
### Collect additional diagnostic logs To collect additional diagnostic logs when you use the Systems Manager send command to run the VSS snapshot document, set the CollectDiagnosticLogs input parameter to "True" at runtime. We recommend that you set this parameter to "True" when you troubleshoot.
To see a command line example, select one of the following tabs.
AWS CLI The following example runs the AWSEC2-CreateVssSnapshot Systems Manager document in the AWS CLI: aws ssm send-command \ --document-name "AWSEC2-CreateVssSnapshot" \ --instance-ids "i-1234567890abcdef0" \ --parameters '{"description":["Example - create diagnostic logs at runtime."],"tags":["Key=tag_name,Value=tag_value"],"CollectDiagnosticLogs":
["True"]}'

PowerShell The following example runs the AWSEC2-CreateVssSnapshot Systems Manager document in PowerShell:
Send-SSMCommand `
    -DocumentName "AWSEC2-CreateVssSnapshot" `
    -InstanceId "i-1234567890abcdef0" `
    -Parameter @{'description'='Example - create diagnostic logs at runtime.';'tags'='Key=tag_name,Value=tag_value';'CollectDiagnosticLogs'='True'}
### Use VSS on instances with proxy configured If you experience problems when creating VSS based EBS snapshots on instances that use a proxy to reach EC2 endpoints, verify the following settings on your instance:
- Verify that the proxy is configured so that the EC2 service endpoints in the instance's Region and IMDS are reachable by AWS Tools for Windows PowerShell running as SYSTEM.
- To support using the system configured WinHTTP proxy, make sure that you've installed the latest AwsVssComponents version on your instance. For more information about configuring WinHTTP proxy, see Netsh Commands for Windows Hypertext Transfer Protocol (WINHTTP) on the Microsoft website.
### Error: Thaw pipe connection timed out, error on thaw, timeout waiting for VSS Freeze, or other timeout errors Freeze, or other timeout errors The EC2 Windows VSS Provider might time out due to activity or services on the instance preventing VSS based snapshots from proceeding in a timely manner. The Windows VSS Framework provides a non-configurable 10-second window during which communication to the file system is paused. During this time, AWSEC2-CreateVssSnapshot snapshots your volumes.
The following issues can cause the EC2 Windows VSS Provider to run into time limits during a snapshot:
- Excessive I/O to a volume
- Slow responsiveness of the EC2 API on the instance
- Fragmented volumes

- Incompatibility with some antivirus software
- Issues with a VSS Application writer
- When Module Logging is enabled for a large number of PowerShell modules, that can cause PowerShell scripts to run slowly Most timeout issues that occur when you run the AWSEC2-CreateVssSnapshot command document are related to the workload on the instance being too high at the time of the backup.
The following actions can help you take a successful snapshot:
- Retry the AWSEC2-CreateVssSnapshot command to see if the snapshot attempt is successful.
If retrying succeeds in some cases, reducing the instance load might make snapshots more successful.
- Wait a while for the workload on the instance to decrease, and retry the AWSEC2- CreateVssSnapshot command. Alternatively, you can attempt snapshots when the instance is known to be under low stress.
- Attempt VSS snapshots when the antivirus software on the system is turned off. If this resolves the issue, refer to the antivirus software instructions and configure it to allow VSS snapshots.
- If there is a high volume of Amazon EC2 API calls in your account within the same Region where you're running a snapshot, API throttling might delay snapshot operations. To reduce throttling impact, use the latest AwsVssComponents package. This package utilizes the EC2 CreateSnapshots API action to reduce the number of mutating actions like per-volume snapshot creation and tagging.
- If you have multiple AWSEC2-CreateVssSnapshot command scripts running at the same time, you can take the following steps to reduce concurrency issues.
- Consider scheduling snapshots during periods of lower API activity.
- If you use Run Command in the Systems Manager console (or SendCommand in the API) to run the command script, you can use Systems Manager rate controls to reduce concurrency.
You can also use Systems Manager rate controls to reduce concurrency for services like AWS Backup that use Systems Manager to run the command script.
- Run the command vssadmin list writers in a shell and see if it reports any errors in the Last error field for any writers on the system. If any writers report a time out error, consider retrying snapshots when the instance is under less load.

- When you use smaller instance types like t2 | t3 | t3a.nano or t2 | t3 | t3a.micro, timeouts due to memory and CPU constraints can occur. The following actions might help reduce timeout issues.
- Try closing memory or CPU intensive applications before taking snapshots.
- Try taking snapshots during periods of lower instance activity.
### Error: Cannot invoke method. Method invocation is supported only on core types in this language mode in this language mode You will encounter this error when the PowerShell language mode is not set to FullLanguage.
The AWSEC2-CreateVssSnapshot SSM document requires PowerShell to be configured to FullLanguage mode.
To verify the language mode, run the following command on the instance in a PowerShell console:
$ExecutionContext.SessionState.LanguageMode For more information about language modes, see about_Language_Modes in the Microsoft documentation.
## Use the AWS VSS solution to restore data for your instance You can restore EBS volumes for a Windows instance from VSS based snapshots created by the AWS VSS solution. If your AWS VSS solution snapshots contain backups of a Microsoft SQL Server database, you can restore the database using the AWSEC2- RestoreSqlServerDatabaseWithVss AWS Systems Manager Automation runbook.
The database restore runbook automates the entire restore process, including creating volumes from the snapshots and attaching them to the instance. The automation leverages VSS technology to restore the database, allowing you to restore without stopping your SQL Server application or disconnecting any active connections.
For detailed instructions on how to use the Microsoft SQL Server database runbook, see Restore from VSS based snapshots in the Microsoft SQL Server on Amazon EC2 User Guide.

### Customize a script to restore EBS volumes from AWS VSS solution snapshots You can use the RestoreVssSnapshotSampleScript.ps1 script as a model to create your own custom script that restores EBS volumes from AWS VSS solution snapshots. The sample script performs the following tasks:
- Stops an instance
- Removes all existing drives from the instance (except the boot volume, if it was excluded)
- Creates new volumes from the snapshots
- Attaches the volumes to the instance by using the device ID tag on the snapshot
- Restarts the instance Important The following script detaches all volumes attached to an instance, and then creates new volumes from a snapshot. Make sure that you have properly backed-up the instance. The old volumes are not deleted. If you want, you can edit the script to delete the old volumes.
To restore volumes from VSS based EBS snapshots
1. Download the RestoreVssSnapshotSampleScript.zip file and extract the file contents.
2. Open RestoreVssSnapshotSampleScript.ps1 in a text editor and edit the sample call at the bottom of the script with a valid EC2 instance ID and EBS snapshot ID, and then run the script from PowerShell.
## AWS VSS solution version history This page includes release notes by version for the AWS VSS component package, as well as component and script version requirements for each supported version of Windows Server.
Topics
- AwsVssComponents package versions
- Windows OS version support

### AwsVssComponents package versions The following table describes the released versions of the AWS VSS component package.
Version Details Release date Downloada ble 2.5.1 Fixed a case where SQL database restoration could fail when the target  database parameter is specified.
March 13, 2025 Yes 2.5.0
- Added the capability to read VSS metadata files and restore a Microsoft SQL Server  database on the instance. For more information, see Restore from VSS based snapshots in the Microsoft SQL Server on Amazon EC2 User  Guide.
- Added support for the in-place update option when installing or upgrading the   AwsVssComponents package.
January 17, 2025 Yes 2.4.0 Added the capability to save VSS metadata files on snapshot creation.  To enable this feature, see SaveVssMetadata in Parameters for Systems Manager VSS snapshot documents.
October 7, 2024 Yes 2.3.3 Updated the VSS agent to ensure that the Ec2VssProvider  is used  during snapshot creation.
June 25, 2024 Yes 2.3.2 Fixed a case where VSS provider registration is not removed on uninstallation.
May 9, 2024 Yes 2.3.1 Added new default tag AwsVssConfig  to identify snapshots and  AMIs created by AWS VSS.
March 7, 2024 Yes

Version Details Release date Downloada ble 2.2.1
- Added support for using the DescribeI nstanceAttribute API.
- Bug fixes and reliability improvements.
- Deprecated support for Windows Server 2012 and 2012 R2. AWS VSS components version   2.2.1 installation on Windows Server 2012 and 2012 R2 will fail. AWS VSS components version 2.1.0 is the last version to support Windows Server 2012 and 2012  R2.
January 18, 2024 Yes 2.1.0 Added support for using the CreateSnapshots API.
November 6, 2023 Yes 2.0.1 Added support for using the WinHTTP proxy settings.
October 26, 2023 No 2.0.0 Added capability to the AWS VSS component to create snapshots and AMIs, which enables compatibi lity with PowerShell  module logging, script block logging, and transcription features.
April 28, 2023 No 1.3.2.0 Fixed a case where installation failure is not reported correctly.
May 10, 2022 No

Version Details Release date Downloada ble 1.3.1.0
- Fixed snapshots failing on domain controllers in relation   to an NTDS VSS writer logging error.
- Fixed VSS agent error when uninstalling version 1.0 VSS  provider.
February 6, 2020 Yes 1.3.00
- Improved logging by reducing unwanted verbosity.
- Fixed regionalization issues during installation.
- Fixed return codes for some provider registration error  conditions.
- Fixed various installation issues.
March 19, 2019 No 1.2.00
- Added command line parameters -nw  (no-writers) and -copy (copy-only) to  agent.
- Fixed EventLog errors caused by improper memory allocation  calls.
November 15, 2018 No 1.1 Fixed AWS VSS components that were being used incorrectly as the default  Windows Backup and Restore provider.
December 12, 2017 No 1.0 Initial release.
November 20, 2017 No

### Windows OS version support The following table shows which AWS VSS solution versions you should run on each version of Windows Server on Amazon EC2.
Windows Server version AwsVssComponents version AWSEC2- Vs sInstallA ndSnapsho t version name AWSEC2- Cr eateVssSn apshot version name Windows Server 2025 default default default Windows Server 2022 default default default Windows Server 2019 default default default Windows Server 2016 default default default Windows Server 2012 R2 2.1.0 not supported 2012R2 Windows Server 2012 2.1.0 not supported 2012R2
