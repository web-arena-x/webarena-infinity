# Upgrade an EC2 Windows instance to a newer version of Windows Server

Source: apps/user-manuals/aws/ec2-ug.pdf

---

# Upgrade an EC2 Windows instance to a newer version of Windows Server Windows Server If it's time to upgrade the Windows Server operating system on your EC2 Windows instance from an earlier version, you can use one of the following methods.
In-place upgrade An in-place upgrade operates on an existing instance. Only the operating system files are affected during this process, while your settings, server roles, and data are left intact.
Migration (also known as a side-by-side upgrade)
A migration involves capturing settings, configurations, and data, and porting these to a newer operating system on a fresh EC2 Windows instance. You can launch your instance from a public or private Windows AMI that you subscribe to from the AWS Marketplace, or an AMI that's shared with you. You can also create a custom AMI with EC2 Image Builder. See the Image Builder User Guide for more information.
Note AWS provides a set of publicly available Amazon Machine Images (AMIs) for Windows Server versions that run on EC2 instances. These AMIs are updated on a monthly basis.
For information about the latest Windows AMIs, see the AWS Windows AMI Reference.
Microsoft has traditionally recommended migrating to a newer version of Windows Server instead of upgrading in place. Migrating can result in fewer upgrade errors or issues, but can take longer than an in-place upgrade because of the need to provision a new instance, plan for and port applications, and adjust configuration settings on the new instance. An in-place upgrade can be faster, but software incompatibilities can produce errors.
Contents
- Perform an in-place upgrade on your EC2 Windows instance
- Use Automation runbooks to upgrade an EC2 Windows instance
- Migrate an EC2 Windows instance to a Nitro-based instance type
- Troubleshoot an operating system upgrade on an EC2 Windows instance

## Perform an in-place upgrade on your EC2 Windows instance Before you perform an in-place upgrade, you must determine which network drivers the instance is running. PV network drivers enable you to access your instance using Remote Desktop. Instances use either AWS PV, Intel Network Adapter, or the Enhanced Networking drivers. For more information, see Paravirtual drivers for Windows instances.
### Before you begin an in-place upgrade Complete the following tasks and note the following important details before you begin your in- place upgrade.
- Read the Microsoft documentation to understand the upgrade requirements, known issues, and restrictions. Also review the official instructions for upgrading.
- Upgrade Options for Windows Server 2012
- Upgrade Options for Windows Server 2012 R2
- Upgrade and conversion options for Windows Server 2016 and above
- Windows Server Upgrades
- We recommend performing an operating system upgrade on instances with at least 2 vCPUs and 4GB of RAM. If needed, you can change the instance to a larger size of the same type (t2.small to t2.large, for example), perform the upgrade, and then resize it back to the original size. If you are required to retain the instance size, you can monitor the progress using the instance console screenshot. For more information, see Amazon EC2 instance type changes.
- Verify that the root volume on your Windows instance has enough free disk space. The Windows Setup process might not warn you of insufficient disk space. For information about how much disk space is required to upgrade a specific operating system, see the Microsoft documentation.
If the volume does not have enough space, it can be expanded. For more information, see Amazon EBS Elastic Volumes in the Amazon EBS User Guide.
- Determine your upgrade path. You must upgrade the operating system to the same architecture.
For example, you must upgrade a 32-bit system to a 32-bit system. Windows Server 2008 R2 and later are 64-bit only.
- Disable antivirus and anti-spyware software and firewalls. These types of software can conflict with the upgrade process. Re-enable antivirus and anti-spyware software and firewalls after the upgrade completes.
- Update to the latest drivers as described in Migrate an EC2 Windows instance to a Nitro-based instance type.

- The Upgrade Helper Service only supports instances running Citrix PV drivers. If the instance is running Red Hat drivers, you must manually upgrade those drivers first.
### Upgrade an instance in-place with AWS PV, Intel Network Adapter, or the Enhanced Networking drivers Enhanced Networking drivers Use the following procedure to upgrade a Windows Server instance using the AWS PV, Intel Network Adapter, or the Enhanced Networking network drivers.
To perform the in-place upgrade
1. Create an AMI of the system you plan to upgrade for either backup or testing purposes. You can then perform the upgrade on the copy to simulate a test environment. If the upgrade completes, you can switch traffic to this instance with little downtime. If the upgrade fails, you can revert to the backup. For more information, see Create an Amazon EBS-backed AMI.
2. Ensure that your Windows Server instance is using the latest network drivers. a.
To update your AWS PV driver, see Upgrade PV drivers on EC2 Windows instances. b.
To update your ENA driver, see Install the ENA driver on EC2 Windows instances. c.
To update your Intel drivers, see Enhanced networking with the Intel 82599 VF interface
3. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
4. In the navigation pane, choose Instances. Locate the instance. Make a note of the instance ID and Availability Zone for the instance. You need this information later in this procedure.
5. If you are upgrading from Windows Server 2012 or 2012 R2 to Windows Server 2016 or later, perform the following on your instance before you proceed. a.
Uninstall the EC2Config service. For more information, see Windows Service administration for EC2Launch v2 and EC2Config agents. b.
Install EC2Launch v1 or the EC2Launch v2 agent. For more information, see Use the EC2Launch v1 agent to perform tasks during EC2 Windows instance launch and Use the EC2Launch v2 agent to perform tasks during EC2 Windows instance launch. c.
Install the AWS Systems Manager SSM Agent. For more information, see  Manually install SSM Agent on Amazon EC2 for Windows Server in the AWS Systems Manager User Guide.
6. Create a new volume from a Windows Server installation media snapshot. a.
In the left navigation pane, under Elastic Block Store, choose Snapshots.

b.
From the filter bar, choose Public snapshots. c.
In the search bar, specify the following filters:
- Choose Owner Alias, then =, then amazon.
- Choose Description, and then start typing Windows. Select the Windows filter that matches the system architecture and language preference you're upgrading to. For example, choose Windows 2019 English Installation Media to upgrade to Windows Server 2019. d.
Select the checkbox next to the snapshot that matches the system architecture and language preference you're upgrading to, and then choose Actions, Create volume from snapshot. e.
On the Create volume page, choose the Availability Zone that matches your Windows instance, and then choose Create volume.
7. In the Successfully created volume vol-1234567890example banner at the top of the page, choose the ID of the volume that you just created.
8. Choose Actions, Attach volume.
9. On the Attach volume page, for Instance, select the instance ID of your Windows instance, and then choose Attach volume.
10. Make the new volume available for use by following the steps at Make an Amazon EBS volume available for use.
Important Do not initialize the disk because doing so will delete the existing data.
11. In Windows PowerShell, switch to the new volume drive. Begin the upgrade by opening the installation media volume you attached to the instance. a.
If you are upgrading to Windows Server 2016 or later, run the following:
.\setup.exe /auto upgrade /dynamicupdate disable Note Running the setup.exe with the /dynamicupdate option set to disabled prevents Windows from installing updates during the Windows Server upgrade process, as

installing updates during the upgrade can cause failures. You can install updates with Windows Update after the upgrade completes.
If you are upgrading to an earlier version of Windows Server, run the following:
Sources\setup.exe b.
For Select the operating system you want to install, select the full installation option for your Windows Server instance, and choose Next. c.
For Which type of installation do you want?, choose Upgrade. d.
Complete the wizard.
Windows Server Setup copies and processes files. After several minutes, your Remote Desktop session closes. The time it takes to upgrade depends on the number of applications and server roles running on your Windows Server instance. The upgrade process could take as little as 40 minutes or several hours. The instance may fail one or more status checks during the upgrade process. When the upgrade completes, all status checks pass. You can check the system log for console output or use Amazon CloudWatch metrics for disk and CPU activity to determine whether the upgrade is progressing.
Note If upgrading to Windows Server 2019, after the upgrade is complete you can change the desktop background manually to remove the previous operating system name if desired.
If the instance has not passed all status checks after several hours, see Troubleshoot an operating system upgrade on an EC2 Windows instance.
### Post upgrade tasks
1. Log in to the instance to initiate an upgrade for the .NET Framework and reboot the system when prompted.
2. If you haven't already done so in a prior step, install the EC2Launch v1 or EC2Launch v2 agent.
For more information, see Use the EC2Launch v1 agent to perform tasks during EC2 Windows

instance launch and Use the EC2Launch v2 agent to perform tasks during EC2 Windows instance launch.
3. If you upgraded to Windows Server 2012 R2, we recommend that you upgrade the PV drivers to AWS PV drivers. If you upgraded on a Nitro-based instance, we recommend that you install or upgrade the NVME and ENA drivers. For more information, see AWS NVMe drivers or Enable enhanced networking on Windows.
4. Re-enable antivirus and anti-spyware software and firewalls.
## Use Automation runbooks to upgrade an EC2 Windows instance You can perform an automated upgrade of your Windows and SQL Server instances on AWS with AWS Systems Manager Automation runbooks.
Contents
- Related services
- Execution options
- Upgrade Windows Server
- Upgrade SQL Server
### Related services The following AWS services are used in the automated upgrade process:
- AWS Systems Manager. AWS Systems Manager is a powerful, unified interface for centrally managing your AWS resources. For more information, see the AWS Systems Manager User Guide.
- AWS Systems Manager Agent (SSM Agent) is Amazon software that can be installed and configured on an Amazon EC2 instance, an on-premises server, or a virtual machine (VM). SSM Agent makes it possible for Systems Manager to update, manage, and configure these resources.
The agent processes requests from the Systems Manager service in the AWS Cloud, and then runs them as specified in the request. For more information, see Working with SSM Agent in the AWS Systems Manager User Guide.
- AWS Systems Manager SSM runbooks. An SSM runbook defines the actions that Systems Manager performs on your managed instances. SSM runbooks use JavaScript Object Notation (JSON) or YAML, and they include steps and parameters that you specify. This topic uses two

Systems Manager SSM runbooks for automation. For more information, see AWS Systems Manager Automation runbook reference in the AWS Systems Manager User Guide.
### Execution options When you select Automation on the Systems Manager console, select Execute. After you select an Automation document, you are then prompted to choose an automation execution option. You choose from the following options. In the steps for the paths provided later in this topic, we use the Simple execution option.
Simple execution Choose this option if you want to update a single instance but do not want to go through each automation step to audit the results. This option is explained in further detail in the upgrade steps that follow.
Rate control Choose this option if you want to apply the upgrade to more than one instance. You define the following settings.
- Parameter This setting, which is also set in Multi-Account and Region settings, defines how your automation branches out.
- Targets Select the target to which you want to apply the automation. This setting is also set in Multi- Account and Region settings.
- Parameter Values Use the values defined in the automation document parameters.
- Resource Group In AWS, a resource is an entity you can work with. Examples include Amazon EC2 instances, AWS CloudFormation stacks, or Amazon S3 buckets. If you work with multiple resources, it might be useful to manage them as a group as opposed to moving from one AWS service to another for every task. In some cases, you may want to manage large numbers of related resources, such as

EC2 instances that make up an application layer. In this case, you will likely need to perform bulk actions on these resources at one time.
- Tags Tags help you categorize your AWS resources in different ways, for example, by purpose, owner, or environment. This categorization is useful when you have many resources of the same type.
You can quickly identify a specific resource using the assigned tags.
- Rate Control Rate Control is also set in Multi-Account and Region settings. When you set the rate control parameters, you define how many of your fleet to apply the automation to, either by target count or by percentage of the fleet.
Multi-Account and Region In addition to the parameters specified under Rate Control that are also used in the Multi-Account and Region settings, there are two additional settings:
- Accounts and organizational units (OUs)
Specify multiple accounts on which you want to run the automation.
- AWS Regions Specify multiple AWS Regions where you want to run the automation.
Manual execution This option is similar to Simple execution, but allows you to step through each automation step and audit the results.
### Upgrade Windows Server The AWSEC2-CloneInstanceAndUpgradeWindows runbook creates an Amazon Machine Image (AMI) from a Windows Server instance in your account and upgrades this AMI to a supported version of your choice. This multi-step process can take up to two hours to complete.
There are two AMIs included in the automated upgrade process:

- Current running instance. The first AMI is the current running instance, which is not upgraded.
This AMI is used to launch another instance to run the in-place upgrade. When the process is complete, this AMI is deleted from your account, unless you specifically request to keep the original instance. This setting is handled by the parameter KeepPreUpgradeImageBackUp (default value is false, which means the AMI is deleted by default).
- Upgraded AMI. This AMI is the outcome of the automation process.
The final result is one AMI, which is the upgraded instance of the AMI.
When the upgrade is complete, you can test your application functionality by launching the new AMI in your Amazon VPC. After testing, and before you perform another upgrade, schedule application downtime before completely switching to the upgraded instance.
#### Prerequisites In order to automate your Windows Server upgrade with the AWS Systems Manager Automation document, you must perform the following tasks:
- Create an IAM role with the specified IAM policies to allow Systems Manager to perform automation tasks on your Amazon EC2 instances and verify that you meet the prerequisites to use Systems Manager. For more information, see Creating a role to delegate permissions to an AWS service in the AWS Identity and Access Management User Guide.
- Select the option for how you want the automation to be run. The options for execution are Simple execution, Rate control, Multi-account and Region, and Manual execution. For more information about these options, see Execution options.
- Verify that SSM Agent is installed on your instance. For more information see Installing and configuring SSM Agent on Amazon EC2 instances for Windows Server.
- Windows PowerShell 3.0 or later must be installed on your instance.
- For instances that are joined to a Microsoft Active Directory domain, we recommend specifying a SubnetId that does not have connectivity to your domain controllers to help avoid hostname conflicts.
- The instance subnet must have outbound connectivity to the internet, which provides access to AWS services such as Amazon S3 and access to download patches from Microsoft. This requirement is met if either the subnet is a public subnet and the instance has a public IP address, or if the subnet is a private subnet with a route that sends internet traffic to a public NAT device.

- This Automation works with instances running Windows Server 2008 R2, Windows Server 2012 R2, Windows Server 2016, and Windows Server 2019.
- Verify that the instance has 20 GB of free disk space in the boot disk.
- If the instance does not use a Windows license provided by AWS, then specify an Amazon EBS snapshot ID that includes Windows Server 2012 R2 installation media. To do this:
1. Verify that the Amazon EC2 instance is running Windows Server 2012 or later.
2. Create a 6 GB Amazon EBS volume in the same Availability Zone where the instance is running. Attach the volume to the instance. Mount it, for example, as drive D.
3. Right-click the ISO and mount it to an instance as, for example, drive E.
4. Copy the content of the ISO from drive E:\ to drive D:\
5. Create an Amazon EBS snapshot of the 6 GB volume created in step 2 above.
#### Windows Server upgrade limitations This automation doesn't support upgrading Windows domain controllers, clusters, or Windows desktop operating systems. In addition, this automation doesn't support Amazon EC2 instances for Windows Server with the following roles installed:
- Remote Desktop Session Host (RDSH)
- Remote Desktop Connection Broker (RDCB)
- Remote Desktop Virtualization Host (RDVH)
- Remote Desktop Web Access (RDWA)
#### Steps to perform an automated upgrade of Windows Server Follow these steps to upgrade your Windows Server instance using the AWSEC2- CloneInstanceAndUpgradeWindows automation runbook.
1. Open Systems Manager from the AWS Management Console.
2. From the left navigation pane, under Change Management, choose Automation.
3. Choose Execute automation.
4. Search for the automation document called AWSEC2-CloneInstanceAndUpgradeWindows.
5. When the document name appears, select it. When you select it, the document details appear.

6. Choose Execute automation to input the parameters for this document. Leave Simple execution selected at the top of the page.
7. Enter the requested parameters based on the following guidance.
- InstanceID Type: String (Required) The instance running Windows Server 2008 R2, 2012 R2, 2016, or 2019 with the SSM agent installed.
- InstanceProfile.
Type: String (Required) The IAM instance profile. This is the IAM role used to perform the Systems Manager automation against the Amazon EC2 instance and AWS AMIs. For more information, see Configure EC2 instance permissions in the AWS Systems Manager User Guide.
- TargetWindowsVersion Type: String (Required) Select the target Windows version.
- SubnetId Type: String (Required) This is the subnet for the upgrade process and where your source EC2 instance resides. Verify that the subnet has outbound connectivity to AWS services, including Amazon S3, and also to Microsoft (in order to download patches).
- KeepPreUpgradedBackUp Type: String (Optional) If this parameter is set to true, the automation retains the image created from the instance. The default setting is false.
- RebootInstanceBeforeTakingImage Type: String

(Optional) The default is false (no reboot). If this parameter is set to true, Systems Manager reboots the instance before creating an AMI for the upgrade.
8. After you have entered the parameters, choose Execute. When the automation begins, you can monitor the execution progress.
9. When the automation completes, you will see the AMI ID. You can launch the AMI to verify that the Windows OS is upgraded.
Note It is not necessary for the automation to run all of the steps. The steps are conditional based on the behavior of the automation and instance. Systems Manager might skip some steps that are not required.
Additionally, some steps may time out. Systems Manager attempts to upgrade and install all of the latest patches. Sometimes, however, patches time out based on a definable timeout setting for the given step. When this happens, the Systems Manager automation continues to the next step to ensure that the internal OS is upgraded to the target Windows Server version.
10. After the automation completes, you can launch an Amazon EC2 instance using the AMI ID to review your upgrade. For more information about how to create an Amazon EC2 instance from an AWS AMI, see  How do I launch an EC2 instance from a custom AMI?
### Upgrade SQL Server The AWSEC2-CloneInstanceAndUpgradeSQLServer script creates an AMI from an Amazon EC2 instance running SQL Server in your account, and then upgrades the AMI to a later version of SQL Server. This multi-step process can take up to two hours to complete.
In this workflow, the automation creates an AMI from the instance and then launches the new AMI in the subnet you provide. The automation then performs an in-place upgrade of SQL Server.
After the upgrade is complete, the automation creates a new AMI before terminating the upgraded instance.
There are two AMIs included in the automated upgrade process:
- Current running instance. The first AMI is the current running instance, which is not upgraded.
This AMI is used to launch another instance to run the in-place upgrade. When the process is

complete, this AMI is deleted from your account, unless you specifically request to keep the original instance. This setting is handled by the parameter KeepPreUpgradeImageBackUp (default value is false, which means the AMI is deleted by default).
- Upgraded AMI. This AMI is the outcome of the automation process.
The final result is one AMI, which is the upgraded instance of the AMI.
When the upgrade is complete, you can test your application functionality by launching the new AMI in your Amazon VPC. After testing, and before you perform another upgrade, schedule application downtime before completely switching to the upgraded instance.
#### Prerequisites In order to automate your SQL Server upgrade with the AWS Systems Manager Automation document, you must perform the following tasks:
- Create an IAM role with the specified IAM policies to allow Systems Manager to perform automation tasks on your Amazon EC2 instances and verify that you meet the prerequisites to use Systems Manager. For more information, see Creating a role to delegate permissions to an AWS service in the AWS Identity and Access Management User Guide.
- Select the option for how you want the automation to be run. The options for execution are Simple execution, Rate control, Multi-account and Region, and Manual execution. For more information about these options, see Execution options.
- The Amazon EC2 instance must use Windows Server 2008 R2 or later and SQL Server 2008 or later.
- Verify that SSM Agent is installed on your instance. For more information, see Working with SSM Agent on Amazon EC2 instances for Windows Server.
- Verify that the instance has enough free disk space:
- If you are upgrading from Windows Server 2008 R2 to 2012 R2, or from Windows Server 2012 R2 to a later operating system, verify that you have 20 GB of free disk space in the instance boot disk.
- If you are upgrading from Windows Server 2008 R2 to 2016 or later, verify that the instance has 40 GB of free disk space in the instance boot disk.
- For instances that use a Bring Your Own License (BYOL) SQL Server version, the following additional prerequisites apply:

- Provide an Amazon EBS snapshot ID that includes the target SQL Server installation media. To do this:
1. Verify that the Amazon EC2 instance is running Windows Server 2008 R2 or later.
2. Create a 6 GB Amazon EBS volume in the same Availability Zone where the instance is running. Attach the volume to the instance. Mount it, for example, as drive D.
3. Right-click the ISO and mount it to an instance as, for example, drive E.
4. Copy the content of the ISO from drive E:\ to drive D:\
5. Create an Amazon EBS snapshot of the 6 GB volume created in step 2.
#### SQL Server automated upgrade limitations The following limitations apply when using the AWSEC2-CloneInstanceAndUpgradeSQLServer runbook to perform an automated upgrade:
- The upgrade can be performed on only a SQL Server using Windows authentication.
- Verify that no security patch updates are pending on the instances. Open Control Panel, then choose Check for updates.
- SQL Server deployments in HA and mirroring mode are not supported.
#### Steps to perform an automated upgrade of SQL Server Follow these steps to upgrade your SQL Server using the AWSEC2- CloneInstanceAndUpgradeSQLServer automation runbook.
1. If you haven't already, download the SQL Server 2016 .iso file and mount it to the source server.
2. After the .iso file is mounted, copy all of the component files and place them on any volume of your choice.
3. Take an Amazon EBS snapshot of the volume and copy the snapshot ID onto a clipboard for later use. For more information, see Create Amazon EBS snapshots in the Amazon EBS User Guide.
4. Attach the instance profile to the Amazon EC2 source instance. This allows Systems Manager to communicate with the EC2 instance and run commands on it after it is added to the AWS Systems Manager service. For this example, we named the role SSM-EC2-Profile-Role with the AmazonSSMManagedInstanceCore  policy attached to the role.

5. In the AWS Systems Manager console, in the left navigation pane, choose Managed Instances.
Verify that your EC2 instance is in the list of managed instance. If you don't see your instance after a few minutes, see Where Are My Instances? in the AWS Systems Manager User Guide.
6. In the left navigation pane, under Change Management choose Automation.
7. Choose Execute automation.
8. Search for the automation document called AWSEC2- CloneInstanceAndUpgradeSQLServer.
9. Choose the AWSEC2-CloneInstanceAndUpgradeSQLServer SSM document, and then choose Next.
10. Ensure that the Simple execution option is selected.
11. Enter the requested parameters based on the following guidance.
- InstanceId Type: String (Required) The instance running SQL Server 2008 R2 (or later).
- IamInstanceProfile Type: String (Required) The IAM instance profile.
- SQLServerSnapshotId Type: String (Required) The Snapshot ID for the target SQL Server installation media. This parameter is not required for SQL Server license-included instances.
- SubnetId Type: String (Required) This is the subnet for the upgrade process and where your source EC2 instance resides. Verify that the subnet has outbound connectivity to AWS services, including Amazon S3, and also to Microsoft (in order to download patches).
- KeepPreUpgradedBackUp Type: String

(Optional) If this parameter is set to true, the automation retains the image created from the instance. The default setting is false.
- RebootInstanceBeforeTakingImage Type: String (Optional) The default is false (no reboot). If this parameter is set to true, Systems Manager reboots the instance before creating an AMI for the upgrade.
- TargetSQLVersion Type: String (Optional) The target SQL Server version. The default is 2016.
12. After you have entered the parameters, choose Execute. When the automation begins, you can monitor the execution progress.
13. When Execution status shows Success, expand Outputs to view the AMI information. You can use the AMI ID to launch your SQL Server instance for the VPC of your choice.
14. Open the Amazon EC2 console. In the left navigation pane, choose AMIs. You should see the new AMI.
15. To verify that the new SQL Server version has been successfully installed, choose the new AMI and choose Launch.
16. Choose the type of instance that you want for the AMI, the VPC and subnet that you want to deploy to, and the storage that you want to use. Because you're launching the new instance from an AMI, the volumes are presented to you as an option to include within the new EC2 instance you are launching. You can remove any of these volumes, or you can add volumes.
17. Add a tag to help you identify your instance.
18. Add the security group or groups to the instance.
19. Choose Launch Instance.
20. Choose the tag name for the instance and select Connect under the Actions dropdown.
21. Verify that the new SQL Server version is the database engine on the new instance.

## Migrate an EC2 Windows instance to a Nitro-based instance type The AWS Windows AMIs are configured with the default settings used by the Microsoft installation media, with some customizations. The customizations include drivers and configurations that support Nitro-based instances, such as M5 and C5.
When migrating from Xen-based instances to Nitro-based instances, including bare metal instances, we recommend that you follow the steps in this topic in the following cases:
- If you are launching instances from custom Windows AMIs
- If you are launching instances from Windows AMIs provided by Amazon that were created before August 2018 Alternatively, you can use the AWSSupport-UpgradeWindowsAWSDrivers automation document to automate the procedures described in Part 1, Part 2, and Part 3. If you choose to use the automated procedure, see (Alternative) Upgrade the AWS PV, ENA, and NVMe drivers using AWS Systems Manager, and then continue with Part 4 and Part 5.
For more information, see Amazon EC2 Update — Additional Instance Types, Nitro System, and CPU Options.
Note The following migration procedures can be performed on Windows Server version 2016 and later. Earlier operating system versions that have reached end of life are not tested, and might not be compatible with the latest instance types.
To migrate Linux instances, see the section called "Instance type changes".
Contents
- Part 1: Install and upgrade AWS PV drivers
- Part 2: Install and upgrade ENA
- Part 3: Upgrade AWS NVMe drivers
- Part 4: Update EC2Config and EC2Launch
- Part 5: Install the serial port driver for bare metal instances
- Part 6: Update power management settings

- Part 7: Update Intel chipset drivers for new instance types
- (Alternative) Upgrade the AWS PV, ENA, and NVMe drivers using AWS Systems Manager Before you begin This procedure assumes that you have a Xen-based instance, such as an M4 or C4, and you are migrating to a Nitro-based instance.
You must use PowerShell version 3.0 or later to successfully perform the upgrade.
Note When migrating, the static IP or custom DNS network settings on the existing network interface card may be lost as the instance will default to a new Enhanced Networking Adapter device.
Before following the steps in this procedure, we recommend that you create a backup of the instance. From the EC2 console, choose the instance that requires the migration, open the context (right-click) menu, and choose Instance State, Stop.
Warning When you stop an instance, the data on any instance store volumes is erased. To preserve data on instance store volumes, ensure that you back up the data to persistent storage.
Open the context (right-click) menu for the instance in the EC2 console, choose Image, and then choose Create Image.
Note Parts 4 and 5 of these instructions can be completed after you migrate or change the instance type. However, we recommend that you complete them before you migrate, especially if you are migrating to a bare metal instance type.

### Part 1: Install and upgrade AWS PV drivers Though AWS PV drivers are not used in the Nitro system, you should still upgrade them if you are on previous versions of either Citrix PV or AWS PV. The latest AWS PV drivers resolve bugs in previous versions of the drivers that may appear while you are on a Nitro system, or if you need to migrate back to a Xen-based instance. As a best practice, we recommend always updating to the latest drivers for Windows instances on AWS.
Use the following procedure to perform an in-place upgrade of AWS PV drivers, or to upgrade from Citrix PV drivers to AWS PV drivers on Windows Server 2008 R2, Windows Server 2012, Windows Server 2012 R2, Windows Server 2016, or Windows Server 2019. For more information, see Upgrade PV drivers on EC2 Windows instances.
To upgrade a Domain Controller, see Upgrade a domain controller (AWS PV upgrade).
To perform an upgrade of or to AWS PV drivers
1. Connect to the instance using Remote Desktop and prepare the instance for upgrade. Take all non-system disks offline before you perform the upgrade. If you are performing an in-place update of AWS PV drivers, this step is not required. Set non-essential services to Manual start- up in the Services console.
2. Download the latest driver package to the instance.
3. Extract the contents of the folder and run AWSPVDriverSetup.msi.
After running the MSI, the instance automatically reboots and upgrades the driver. The instance may not be available for up to 15 minutes.
After the upgrade is complete and the instance passes both health checks in the Amazon EC2 console, connect to the instance using Remote Desktop and verify that the new driver was installed. In Device Manager, under Storage Controllers, locate AWS PV Storage Host Adapter.
Verify that the driver version is the same as the latest version listed in the Driver Version History table. For more information, see AWS PV driver package history.
### Part 2: Install and upgrade ENA Upgrade to the latest Elastic Network Adapter driver to ensure that all network features are supported. If you launched your instance and it does not have enhanced networking already enabled, you must download and install the required network adapter driver on your instance.

Then, set the enaSupport instance attribute to activate enhanced networking. You can only enable this attribute on supported instance types and only if the ENA driver is installed. For more information, see Enable enhanced networking with ENA on your EC2 instances.
1. Download the latest driver to the instance. If you need a previous version of the driver, see ENA Windows driver version history.
2. Extract the zip archive.
3. Install the driver by running the install.ps1 PowerShell script from the extracted folder.
Note To avoid installation errors, run the install.ps1 script as an administrator.
4. Check if your AMI has enaSupport activated. If not, continue by following the documentation at Enable enhanced networking with ENA on your EC2 instances.
### Part 3: Upgrade AWS NVMe drivers AWS NVMe drivers are used to interact with Amazon EBS and SSD instance store volumes that are exposed as NVMe block devices in the Nitro system for better performance.
Important The following instructions are modified specifically for when you install or upgrade AWS NVMe on a Xen-based instance with the intention to migrate the instance to a Nitro-based instance.
1. Download the latest driver package to the instance.
If you need a previous version of the driver, see NVMe Windows driver releases for supported versions.
2. Extract the zip archive.
3. Install the driver as described in Readme.txt.
4. Open a PowerShell session and run the following command:
PS C:\> start rundll32.exe sppnp.dll,Sysprep_Generalize_Pnp -wait

Note To apply the command, you must run the PowerShell session as an administrator.
PowerShell (x86) versions will result in an error.
This command only runs sysprep on the device drivers. It does not run the full sysprep preparation.
5. For Windows Server 2008 R2 and Windows Server 2012, shut down the instance, change the instance type and start the instance, then proceed to Part 4. If you start the instance again on a Xen-based instance type before migrating to a Nitro-based instance type, it will not boot.
For other supported Windows AMIs, you can change the instance type anytime after the device sysprep.
### Part 4: Update EC2Config and EC2Launch For Windows instances, the latest EC2Config and EC2Launch utilities provide additional functionality and information when running on the Nitro system, including on EC2 Bare Metal.
By default, the EC2Config service is included in AMIs prior to Windows Server 2016. EC2Launch replaces EC2Config on Windows Server 2016 and later AMIs.
When the EC2Config and EC2Launch services are updated, new Windows AMIs from AWS include the latest version of the service. However, you must update your own Windows AMIs and instances with the latest version of EC2Config and EC2Launch.
To install or update EC2Config
1. Download and unzip the  EC2Config Installer.
2. Run EC2Install.exe. For a complete list of options, run EC2Install with the /? option.
By default, setup displays prompts. To run the command with no prompts, use the /quiet option.
For more information, see Install the latest version of EC2Config.
To install or update EC2Launch
1. If you have already installed and configured EC2Launch on an instance, make a backup of the EC2Launch configuration file. The installation process does not preserve changes in this file. By

default, the file is located in the C:\ProgramData\Amazon\EC2-Windows\Launch\Config directory.
2. Download EC2-Windows-Launch.zip to a directory on the instance.
3. Download install.ps1 to the same directory where you downloaded EC2-Windows- Launch.zip.
4. Run install.ps1.
Note To avoid installation errors, run the install.ps1 script as an administrator.
5. If you made a backup of the EC2Launch configuration file, copy it to the C:\ProgramData \Amazon\EC2-Windows\Launch\Config directory.
For more information, see Use the EC2Launch v1 agent to perform tasks during EC2 Windows instance launch.
### Part 5: Install the serial port driver for bare metal instances The i3.metal instance type uses a PCI-based serial device rather than an I/O port-based serial device. The latest Windows AMIs automatically use the PCI-based serial device and have the serial port driver installed. If you are not using an instance launched from an Amazon-provided Windows AMI dated 2018.04.11 or later, you must install the Serial Port Driver to enable the serial device for EC2 features such as Password Generation and Console Output. The latest EC2Config and EC2Launch utilities also support i3.metal and provide additional functionality. Follow the steps in Part 4, if you have not yet done so.
To install the serial port driver
1. Download the serial driver package to the instance.
2. Extract the contents of the folder, open the context (right-click) menu for aws_ser.INF, and choose install.
3. Choose Okay.

### Part 6: Update power management settings The following update to power management settings sets displays to never turn off, which allows for graceful OS shutdowns on the Nitro system. All Windows AMIs provided by Amazon as of 2018.11.28 already have this default configuration.
1. Open a command prompt or PowerShell session.
2. Run the following commands: powercfg /setacvalueindex 381b4222-f694-41f0-9685-ff5bb260df2e 7516b95f- f776-4464-8c53-06167f40cc99 3c0bc021-c8a8-4e07-a973-6b14cbcb2b7e 0 powercfg /setacvalueindex 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c 7516b95f- f776-4464-8c53-06167f40cc99 3c0bc021-c8a8-4e07-a973-6b14cbcb2b7e 0 powercfg /setacvalueindex a1841308-3541-4fab-bc81-f71556f20b4a 7516b95f- f776-4464-8c53-06167f40cc99 3c0bc021-c8a8-4e07-a973-6b14cbcb2b7e 0
### Part 7: Update Intel chipset drivers for new instance types The u-6tb1.metal, u-9tb1.metal, and u-12tb1.metal instance types use hardware that requires chipset drivers that were not previously installed on Windows AMIs. If you are not using an instance launched from an Amazon-provided Windows AMI dated 2018.11.19 or later, you must install the drivers using the Intel Chipset INF Utility.
To install the chipset drivers
1. Chipset INF Utility to the instance.
2. Extract the files.
3. Run SetupChipset.exe.
4. Accept the Intel software license agreement and install the chipset drivers.
5. Reboot the instance.
### (Alternative) Upgrade the AWS PV, ENA, and NVMe drivers using AWS Systems Manager Manager The AWSSupport-UpgradeWindowsAWSDrivers automation document automates the steps described in Part 1, Part 2, and Part 3. This method can also repair an instance where the driver upgrades have failed.

The AWSSupport-UpgradeWindowsAWSDrivers automation document upgrades or repairs storage and network AWS drivers on the specified EC2 instance. The document attempts to install the latest versions of AWS drivers online by calling the AWS Systems Manager Agent (SSM Agent).
If SSM Agent is not contactable, the document can perform an offline installation of the AWS drivers if explicitly requested.
Note This procedure will fail on a domain controller. To update drivers on a domain controller, see Upgrade a domain controller (AWS PV upgrade).
To automatically upgrade the AWS PV, ENA, and NVMe drivers using AWS Systems Manager
1. Open the Systems Manager console at https://console.aws.amazon.com/systems-manager.
2. Choose Automation, Execute Automation.
3. Search for and then select the AWSSupport-UpgradeWindowsAWSDrivers automation document, and then choose Execute automation.
4. In the Input Parameters section, configure the following options:
Instance ID Enter the unique ID of the instance to upgrade.
AllowOffline (Optional) Choose one of the following options:
- True — Choose this option to perform an offline installation. The instance is stopped and restarted during the upgrade process.
Warning When you stop an instance, the data on any instance store volumes is erased. To preserve data on instance store volumes, ensure that you back up the data to persistent storage.
- False — (Default) To perform an online installation, leave this option selected. The instance is restarted during the upgrade process.

Important Online and offline upgrades create an AMI before attempting the upgrade operations. The AMI persists after the automation completes. Secure your access to the AMI, or delete it if it is no longer needed.
SubnetId (Optional) Enter one of the following values:
- SelectedInstanceSubnet — (Default) The upgrade process launches the helper instance into the same subnet as the instance that is to be upgraded. The subnet must allow communication to the Systems Manager endpoints (ssm.*).
- CreateNewVPC — The upgrade process launches the helper instance into a new VPC. Use this option if you're not sure whether the target instance's subnet allows communication to the ssm.* endpoints. Your user must have permission to create a VPC.
- A specific subnet ID — Specify the ID of a specific subnet into which to launch the helper instance. The subnet must be in the same Availability Zone as the instance that is to be upgraded, and it must allow communication with the ssm.* endpoints.
5. Choose Execute.
6. Allow the upgrade to complete. It could take up to 10 minutes to complete an online upgrade, and up to 25 minutes to complete an offline upgrade.
## Troubleshoot an operating system upgrade on an EC2 Windows instance instance AWS provides upgrade support for issues or problems with the Upgrade Helper Service, an AWS utility that helps you perform in-place upgrades involving Citrix PV drivers.
After the upgrade, the instance might temporarily experience higher than average CPU utilization while the .NET Runtime Optimization service optimizes the .NET framework. This is expected behavior.
If the instance has not passed all status checks after several hours, check the following.
