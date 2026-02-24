# Configure your Amazon EC2 Windows instance

Source: apps/user-manuals/aws/ec2-ug.pdf

---

To unsubscribe from Amazon EC2 Windows driver notification
1. Open the Amazon SNS console at https://console.aws.amazon.com/sns/v3/home.
2. In the navigation pane, choose Subscriptions.
3. Select the checkbox for the subscription and then choose Actions, Delete subscriptions. When prompted for confirmation, choose Delete.
To subscribe to EC2 notifications using the AWS CLI To subscribe to EC2 notifications with the AWS CLI, use the following command. aws sns subscribe --topic-arn arn:aws:sns:us-east-1:801119661308:ec2-windows-drivers -- protocol email --notification-endpoint YourUserName@YourDomainName.ext To subscribe to EC2 notifications using AWS Tools for Windows PowerShell To subscribe to EC2 notifications with AWS Tools for Windows PowerShell, use the following command.
Connect-SNSNotification -TopicArn 'arn:aws:sns:us-east-1:801119661308:ec2-windows- drivers' -Protocol email -Region us-east-1 -Endpoint 'YourUserName@YourDomainName.ext'
# Configure your Amazon EC2 Windows instance After you've launched a Windows instance, you can log in as an administrator to perform additional configuration for Windows features and system settings. EC2 Windows troubleshooting utilities can help you troubleshoot issues on your instance.
You can configure Windows launch agents and other Windows-specific features as follows.
Windows launch agents Each AWS Windows AMI (and many other AMIs that are available on the AWS Marketplace) includes a Windows launch agent that's pre-configured with default settings. Launch agents perform tasks during instance startup and run if an instance is stopped and later started, or restarted.

EC2 Fast Launch for Windows Every Amazon EC2 Windows instance must go through the standard Windows operating system (OS) launch steps, which include several reboots, and often take 15 minutes or longer to complete. Amazon EC2 Windows Server AMIs that have the EC2 Fast Launch feature enabled complete some of those steps and reboots in advance to reduce the time it takes to launch an instance.
## Windows-specific system settings The following list includes some system settings that apply only for Windows operating systems:
## Change the Windows Administrator password for your Amazon EC2 instance When you connect to a Windows instance, you must specify a user account and password that has permission to access the instance. The first time that you connect to an instance, you must use the Administrator account and provide the default password. When you connect to an instance the first time, we recommend that you change the Administrator password from its default value.
Add Windows System components Windows Server operating systems include many optional components. Including all optional components in each AWS Windows Server AMI is not practical. Instead, we provide installation media EBS snapshots that have the necessary files to configure or install components on your Windows instance.
Install WSL on Windows Windows Subsystem for Linux (WSL) is a free download that you can install on your Windows instance. By installing WSL, you can run native Linux command line tools directly on your Windows instance and use the Linux tools for scripting, alongside your traditional Windows desktop. You can easily swap between Linux and Windows on a single Windows instance, which you might find useful in a development environment.
## AWS device drivers for Windows instances You can update the AWS device drivers for your Windows instances. For more information, see the section called "Manage device drivers".

The following table summarizes the supported drivers for Nitro-based instances by Windows version.
Version Storage driver Enhanced networking driver Windows Server 2025 AWS NVMe latest version ENA latest version Windows Server 2022 AWS NVMe latest version ENA latest version Windows Server 2019 AWS NVMe latest version ENA latest version Windows Server 2016 AWS NVMe latest version ENA latest version Windows Server 2012 R2 AWS NVMe version 1.5.1 ENA version 2.6.0 Windows Server 2008 R2 AWS NVMe version 1.3.2 ENA version 2.2.3 The following table summarizes the supported drivers for Xen-based instances by Windows version.
Version Storage driver Enhanced networking driver Windows Server 2022 AWS PV latest version
- ENA latest version 1
- Intel VF 2
- AWS PV latest version 3 Windows Server 2019 AWS PV latest version
- ENA latest version 1
- Intel VF 2
- AWS PV latest version 3 Windows Server 2016 AWS PV latest version
- ENA latest version 1
- Intel VF 2
- AWS PV latest version 3 Windows Server 2012 R2 AWS PV version 8.4.3
- ENA version 2.6.0 1

Version Storage driver Enhanced networking driver
- Intel VF 2
- AWS PV version 8.4.3 3 Windows Server 2008 R2 AWS PV version 8.3.5
- ENA version 2.2.3 1
- Intel VF 2
- AWS PV version 8.3.5 3 1 For instance types G3, H1, I3, m4.16xlarge, P2, P3, P3dn, and R4.
2 For instance types C3, C4, D2, I2, M4 (excluding m4.16xlarge), and R3.
3 For instance types C1, M1, M2, M3, T1, T2, X1, and X1e.
## Windows launch agents on Amazon EC2 Windows instances Each AWS Windows AMI includes a Windows launch agent that's pre-configured with default settings. Launch agents perform tasks during instance startup and run if an instance is stopped and later started, or restarted. For information about a specific agent, see the detail pages in the following list.
For more information about AWS Windows AMIs, see the AWS Windows AMI reference.
- Use the EC2Launch v2 agent to perform tasks during EC2 Windows instance launch
- Use the EC2Launch v1 agent to perform tasks during EC2 Windows instance launch
- Use the EC2Config service to perform tasks during EC2 legacy Windows operating system instance launch Content
- Compare Amazon EC2 launch agents
- Configure DNS Suffix for EC2 Windows launch agents
- Subscribe to EC2 Windows launch agent notifications
- Windows Service administration for EC2Launch v2 and EC2Config agents

### Compare Amazon EC2 launch agents The following table shows the major functional differences between EC2Config, EC2Launch v1, and EC2Launch v2.
Feature EC2Config EC2Launch v1 EC2Launch v2 Run as Windows Service PowerShell Scripts Windows Service Supports Legacy OS only Windows Server versions:
- 2016
- 2019 (LTSC and SAC)
Windows Server versions:
- 2016
- 2019 (LTSC and SAC)
- 2022
- 2025 Configuration file XML JSON JSON/YAML Set Administrator username No No Yes Compressed user data No No Yes Local user data baked on AMI No No Yes, configurable Task configuration in user data No No Yes Configurable
###### wallpaper No No Yes Customize task run order No No Yes Configurable tasks 15 9 20 at launch

Feature EC2Config EC2Launch v1 EC2Launch v2 Supports Windows Event Viewer Yes No Yes Number of Event Viewer event types 2 0 30 Note EC2Config documentation is provided for historical reference only. The operating system versions it runs on are no longer supported by Microsoft. We strongly recommend that you upgrade to the latest launch service.
### Configure DNS Suffix for EC2 Windows launch agents With Amazon EC2 launch agents, you can configure a list of DNS suffixes that Windows instances use for domain name resolution. The launch agents override the standard Windows settings in the System\CurrentControlSet\Services\Tcpip\Parameters\SearchList registry key by adding the following values to the DNS suffix search list:
- The domain of the instance
- The suffixes that result from devolution of the instance domain
- NV domain
- The domains specified by each network interface cards All launch agents support DNS suffix configuration. For more information, see your specific launch agent version:
- For information about the setDnsSuffix task and how to configure DNS suffixes in EC2Launch v2, see setDnsSuffix .
- For information about DNS suffix list setup and how to enable or disable devolution for EC2Launch v1, see Configure the EC2Launch v1 agent on your Windows instance.
- For information about DNS suffix list setup and how to enable or disable devolution for EC2Config, see EC2Config settings files.

Domain name devolution Domain name devolution is an Active Directory behavior that allows computers in a child domain to access resources in the parent domain without using a fully qualified domain name. By default, domain name devolution continues until there are only two nodes left in the domain name progression.
Launch agents perform devolution on the domain name if the instance is connected to a domain, and add the results to the DNS suffix search list that's maintained in the System \CurrentControlSet\Services\Tcpip\Parameters\SearchList registry key. The agents use the settings from the following registry keys, to determine the devolution behavior.
- System\CurrentControlSet\Services\Tcpip\Parameters \UseDomainNameDevolution
- When not set, disables devolution
- When set to 1, enables devolution (default)
- When set to 0, disables devolution
- System\CurrentControlSet\Services\Dnscache\Parameters \DomainNameDevolutionLevel
- When not set, use level of 2 (default)
- When set to 3 or greater, use value to set level When you disable devolution or change your devolution settings to a higher level, the System \CurrentControlSet\Services\Tcpip\Parameters\SearchList registry key stil contains the suffixes that were added previously. They are not automatically removed. You can manually update the list, or you can clear the list and let your agent run through the process to set up the new list.
Note To clear the DNS suffix list from the registry, you can run the following command.
PS C:\> Invoke-CimMethod -ClassName Win32_NetworkAdapterConfiguration - MethodName "SetDNSSuffixSearchOrder" -Arguments @{ DNSDomainSuffixSearchOrder = $null } | Out-Null

Devolution examples The following examples show domain name progression through the devolution process. corp.example.com
- Progresses to example.com locale.region.corp.example.com
1. Progresses to region.corp.example.com
2. Progresses to corp.example.com
3. Progresses to example.com locale.region.corp.example.com with a setting of DomainNameDevolutionLevel=3
1. Progresses to region.corp.example.com
2. Progresses to corp.example.com. The progression stops here, due to the level setting.
### Subscribe to EC2 Windows launch agent notifications Amazon SNS can notify you when new versions of the EC2 launch agents are released. Use the following procedure to subscribe to these notifications.
Subscribe to EC2Config notifications
1. Open the Amazon SNS console at https://console.aws.amazon.com/sns/v3/home.
2. In the navigation bar, change the Region to US East (N. Virginia), if necessary. You must select this Region because the SNS notifications that you are subscribing to were created in this Region.
3. In the navigation pane, choose Subscriptions.
4. Choose Create subscription.
5. In the Create subscription dialog box, do the following: a.
For Topic ARN, use the following Amazon Resource Name (ARN) that matches the agent you want to receive notifications for:

- EC2Launch v2: arn:aws:sns:us-east-1:309726204594:amazon-ec2launch-v2
- EC2Launch or EC2Config: arn:aws:sns:us-east-1:801119661308:ec2-windows-ec2config b.
For Protocol, choose Email. c.
For Endpoint, enter the email address where you want to receive the notifications. d.
Choose Create subscription.
6. You'll receive a email asking you to confirm your subscription. Open the email and follow the directions to complete your subscription.
Whenever a new version of the launch agent is released, we send notifications to subscribers. If you no longer want to receive these notifications, use the following procedure to unsubscribe.
Unsubscribe from launch agent notifications
1. Open the Amazon SNS console.
2. In the navigation pane, choose Subscriptions.
3. Select the subscription and then choose Actions, Delete subscriptions. When prompted for confirmation, choose Delete.
### Windows Service administration for EC2Launch v2 and EC2Config agents If you've logged into your instance as a user with administrative rights, you can manage the EC2Launch v2 and EC2Config launch agents just as you would any other Windows service.
EC2Launch v1 is a set of PowerShell scripts that is managed via scheduled task by default. This section covers service administration for EC2Launch v2 and EC2Config.
To apply updated settings to your instance, you can stop and restart the EC2Launch v2 agent or the EC2Config service launch agent from the Microsoft Management Console (MMC) interface for Services. Similarly, when you install a new version of the launch agent, you must stop the agent first, then restart it when the installation is complete.

Note You must open the MMC Services interface as an administrator to select these actions. To do this, you can select Run as administrator from the context menu. Alternatively, to open the interface using your keyboard, follow these steps:
1. Using the Tab key or arrow keys, select the Services menu item from the Administrative Tools menu.
2. Use the following keyboard combination to open as an administrator: Ctrl + Shift + Enter.
The following procedures list steps to stop and start the launch agent on your instance.
Stop the launch agent
1. Launch and connect to your Windows instance.
2. Select Administrative Tools from the Windows Start menu.
3. Open the Services console as an administrator, as described at the beginning of this section.
4. In the list of services, select the agent that's running on your instance (EC2Launch or EC2Config), then choose Stop from the Action menu. Alternatively, you can use the context menu to stop the agent.
Restart the launch agent
1. Launch and connect to your Windows instance.
2. Select Administrative Tools from the Windows Start menu.
3. Open the Services console as an administrator, as described at the beginning of this section.
4. In the list of services, select the agent that's running on your instance (EC2Launch or EC2Config), then choose Start or Restart from the Action menu. Alternatively, you can use the context menu to restart the agent.
If you don't need to update the configuration settings, create your own AMI, or use AWS Systems Manager, you can delete or uninstall the launch agent.

Delete Deleting a service removes its registry subkey.
Uninstall Uninstalling a service removes the files, the registry subkey, and any shortcuts to the service.
Delete the launch agent
1. Launch and connect to your Windows instance.
2. Start a Windows Command Prompt window.
3. Run one of the following commands to delete the launch agent.
- Run the following command to delete the EC2Launch or EC2Launch v2: sc delete ec2launch
- Run the following command to delete the EC2Config service: sc delete ec2config Uninstall the launch agent
1. Launch and connect to your Windows instance.
2. Choose Windows System, then Control Panel from the Windows Start menu.
3. Choose Programs and Features to open the list of programs that are installed on your instance.
4. Select your launch agent from the list (Amazon EC2Launch or EC2ConfigService), then choose Uninstall from the File menu. Alternatively, you can use the context menu.
Note You can see what launch agent version is installed in the Version column.

### Use the EC2Launch v2 agent to perform tasks during EC2 Windows instance launch launch All supported instances of Amazon EC2 that are launched from AWS Windows Server 2022 and Windows Server 2025 AMIs include the EC2Launch v2 launch agent (EC2Launch.exe) by default.
We also provide Windows Server 2016 and 2019 AMIs with EC2Launch v2 installed as the default launch agent. These AMIs are provided in addition to the Windows Server 2016 and 2019 AMIs that include EC2Launch v1. You can search for Windows AMIs that include EC2Launch v2 by default by entering the following prefix in your search from the AMIs page in the Amazon EC2 console:
EC2LaunchV2-Windows_Server-*.
To compare launch agent version features, see Compare Amazon EC2 launch agents.
EC2Launch v2 performs tasks during instance startup and runs if an instance is stopped and later started, or restarted. EC2Launch v2 can also perform tasks on demand. Some of these tasks are automatically enabled, while others must be enabled manually. The EC2Launch v2 service supports all EC2Config and EC2Launch features.
This service uses a configuration file to control its operation. You can update the configuration file using either a graphical tool or by directly editing it as a single .yml file (agent-config.yml). For more information about file locations, see EC2Launch v2 directory structure.
EC2Launch v2 publishes Windows event logs to help you troubleshoot errors and set triggers. For more information, see Windows event logs.
Supported OS versions The EC2Launch v2 agent supports the following Windows Server operating system (OS) versions:
- Windows Server 2025
- Windows Server 2022
- Windows Server 2019 (Long-Term Servicing Channel and Semi-Annual Channel)
- Windows Server 2016 Tasks that run by default The EC2Launch v2 agent runs the following tasks one time only by default during the initial instance launch. Tasks are organized according to the order in which they run within their launch stage.

Boot stage
- extendRootPartition PreReady stage
- activateWindows
- setDnsSuffix
- setAdminAccount
- setWallpaper PostReady stage
- startSsm
#### EC2Launch v2 concepts The following concepts are useful to understand when considering EC2Launch v2. agent-config agent-config is a file that is located in the configuration folder for EC2Launch v2. It includes configuration for the boot, network, PreReady, and PostReady stages. This file is used to specify the instance configuration for tasks that should run when the AMI is either booted for the first time or for subsequent times.
By default, the EC2Launch v2 installation installs an agent-config file that includes recommended configurations that are used in standard Amazon Windows AMIs. You can update the configuration file to alter the default boot experience for your AMI that EC2Launch v2 specifies. For more information about file locations, see EC2Launch v2 directory structure.
Frequency Task frequency determines when tasks should run, depending on the boot context. Most tasks have only one allowed frequency. You can specify a frequency for executeScript tasks.
You will see the following frequencies in the EC2Launch v2 task configuration.
- Once – The task runs once, when the AMI has booted for the first time (finished Sysprep).

- Always – The task runs every time that the launch agent runs. The launch agent runs when:
- an instance starts or restarts
- the EC2Launch service runs
- EC2Launch.exe run is invoked Stage A stage is a logical grouping of tasks that the EC2Launch v2 agent runs. Some tasks can run only in a specific stage. Others can run in multiple stages. When using agent-config.yml, you must specify a list of stages, and a list of tasks to run within each stage.
The service runs stages in the following order:
Stage 1: Boot Stage 2: Network Stage 3: PreReady Windows is ready After the PreReady stage completes, the service sends the Windows is ready message to the Amazon EC2 console.
Stage 4: PostReady User data runs during the PostReady stage. Some script versions run before the agent- config.yml file PostReady stage, and some run after, as follows:
Before agent-config.yml
- YAML user data version 1.1
- XML user data After agent-config.yml
- YAML user data version 1.0 (legacy version for backwards compatibility)
For example stages and tasks, see Example: agent-config.yml.
When you use user data, you must specify a list of tasks for the launch agent to run. The stage is implied. For example tasks, see Example: user data.

EC2Launch v2 runs the list of tasks in the order that you specify in agent-config.yml and in user data. Stages run sequentially. The next stage starts after the previous stage completes.
Tasks also run sequentially.
Task You can invoke a task to perform an action on an instance. You can configure tasks in the agent-config.yml file or through user data. For a list of available tasks for EC2Launch v2, see EC2Launch v2 tasks. For task configuration schema and details, see EC2Launch v2 task configuration.
User data User data is data that is configurable when you launch an instance. You can update user data to dynamically change how custom AMIs or quickstart AMIs are configured. EC2Launch v2 supports 60 kB user data input length. User data includes only the UserData stage, and therefore runs after the agent-config file. You can enter user data when you launch an instance using the launch instance wizard, or you can modify user data from the EC2 console.
For more information about working with user data, see How Amazon EC2 handles user data for Windows instances.
#### EC2Launch v2 task overview EC2Launch v2 can perform the following tasks at each boot:
- Set up new and optionally customized wallpaper that renders information about the instance.
- Set the attributes for the administrator account that is created on the local machine.
- Add DNS suffixes to the list of search suffixes. Only suffixes that do not already exist are added to the list.
- Set drive letters for any additional volumes and extend them to use available space.
- Write files from the configuration to the disk.
- Run scripts specified in the EC2Launch v2 config file or from user-data. Scripts from user- data can be plain text or zipped and provided as a base64 format.
- Run a program with given arguments.
- Set the computer name.
- Send instance information to the Amazon EC2 console.
- Send the RDP certificate thumbprint to the Amazon EC2 console.

- Dynamically extend the operating system partition to include any unpartitioned space.
- Run user data. For more information about specifying user data, see EC2Launch v2 task configuration.
- Set non-persistent static routes to reach the metadata service and AWS KMS servers.
- Set non-boot partitions to mbr or gpt.
- Start the Systems Manager service following Sysprep.
- Optimize ENA settings.
- Enable OpenSSH for later Windows versions.
- Enable Jumbo Frames.
- Set Sysprep to run with EC2Launch v2.
- Publish Windows event logs.
#### EC2Launch v2 directory structure EC2Launch v2 should be installed in the following directories:
- Service binaries: %ProgramFiles%\Amazon\EC2Launch
- Service data (settings, log files, and state files): %ProgramData%\Amazon\EC2Launch Note By default, Windows hides files and folders under C:\ProgramData. To view EC2Launch v2 directories and files, you must either enter the path in Windows Explorer or change the folder properties to show hidden files and folders.
The %ProgramFiles%\Amazon\EC2Launch directory contains binaries and supporting libraries.
It includes the following subdirectories:
- settings
- EC2LaunchSettingsUI.exe – user interface for modifying the agent-config.yml file
- YamlDotNet.dll – DLL for supporting some operations in the user interface
- tools
- ebsnvme-id.exe – tool for examining the metadata of the EBS volumes on the instance

- AWSAcpiSpcrReader.exe – tool for determining the correct COM port to use
- EC2LaunchEventMessage.dll – DLL for supporting the Windows event logging for EC2Launch
- service
- EC2LaunchService.exe – Windows service executable that is launched when the launch agent runs as a service
- EC2AgentTelemetry.dll – DLL for supporting EC2 agent telemetry
- EC2Launch.exe – main EC2Launch executable
- EC2LaunchAgentAttribution.txt – attribution for code used within EC2 Launch The %ProgramData%\Amazon\EC2Launch directory contains the following subdirectories. All of the data produced by the service, including logs, configuration, and state, is stored in this directory.
- config – Configuration The service configuration file is stored in this directory as agent-config.yml. This file can be updated to modify, add, or remove default tasks run by the service. Permission to create files in this directory is restricted to the administrator account to prevent privilege escalation.
- log – Instance logs Logs for the service (agent.log), console (console.log), performance (bench.log), errors (err.log), and telemetry (telemetry.log are stored in this directory. Log files are appended to on subsequent executions of the service.
- state – Service state data The state that the service uses to determine which tasks should run is stored here. There is a .run-once file that indicates whether the service has already run after Sysprep (so tasks with a frequency of once will be skipped on the next run). This subdirectory includes a state.json and previous-state.json to track the status of each task.
- sysprep – Sysprep This directory contains files that are used to determine which operations to perform by Sysprep when it creates a customized Windows AMI that can be reused.
- wallpaper – Wallpaper This wallpaper images is stored in this directory.

#### Telemetry Telemetry is additional information that helps AWS to better understand your requirements, diagnose issues, and deliver features to improve your experience with AWS services.
EC2Launch v2 version 2.1.592 and later collect telemetry, such as usage metrics and errors. This data is collected from the Amazon EC2 instance on which EC2Launch v2 runs. This includes all Windows AMIs owned by AWS.
The following types of telemetry are collected by EC2Launch v2:
- Usage information — agent commands, install method, and scheduled run frequency.
- Errors and diagnostic information — agent installation error codes, run error codes, and error call stacks.
Examples of collected data from version 2.0.592 through 2.1.1:
2025/07/18 22:38:52Z: EC2LaunchTelemetry: IsTelemetryEnabled=true 2025/07/18 22:38:52Z: EC2LaunchTelemetry: AgentOsArch=windows_amd64 2025/07/18 22:38:52Z: EC2LaunchTelemetry: IsAgentScheduledPerBoot=true 2025/07/18 22:38:52Z: EC2LaunchTelemetry: AgentCommandErrorCode=0 2025/07/18 22:38:52Z: EC2LaunchTelemetry: AdminPasswordTypeCode=0 2025/07/18 22:38:52Z: EC2LaunchTelemetry: IpConflictDetectionCode=0 2025/07/18 22:38:52Z: EC2LaunchTelemetry: AgentErrorLocation=addroutes.go:49 Starting with version 2.2.63, EC2 Agent telemetry data is formatted as a JSON object:
{"type":"EC2AgentTelemetry","agentId":"WindowsLaunchAgentV2" ... } Telemetry is enabled by default. You can disable telemetry collection at any time.
Disable telemetry on an instance To disable telemetry for a single instance, you can either set a system environment variable, or use the MSI to modify the installation.
To disable telemetry by setting a system environment variable, run the following command as an administrator. setx /M EC2LAUNCH_TELEMETRY 0

To disable telemetry using the MSI, run the following command after you download the MSI. msiexec /i ".\AmazonEC2Launch.msi" Remove="Telemetry" /q More topics for EC2Launch v2
- Install the latest version of EC2Launch v2
- Configure EC2Launch v2 settings for Windows instances
- Task definitions for EC2Launch v2 startup tasks
- Troubleshoot issues with the EC2Launch v2 agent
- EC2Launch v2 version histories
#### Install the latest version of EC2Launch v2 You can use one of the following methods to install the EC2Launch v2 agent on your EC2 instance:
- Download the agent from Amazon S3 and install with Windows PowerShell. For download URLs, see EC2Launch v2 downloads on Amazon S3.
- Install with SSM Distributor.
- Install from an EC2 Image Builder component when you create a custom image.
- Launch your instance from an AMI that has EC2Launch v2 pre-installed.
Warning AmazonEC2Launch.msi uninstalls previous versions of the EC2 launch services, such as EC2Launch (v1) and EC2Config.
For install steps, select the tab that matches your preferred method.
PowerShell To install the latest version of EC2Launch v2 agent with Windows PowerShell, follow these steps.
1. Create your local directory.

New-Item -Path "$env:USERPROFILE\Desktop\EC2Launchv2" -ItemType Directory
2. Set the URL for your download location. Run the following command with the Amazon S3 URL you'll use. For download URLs, see EC2Launch v2 downloads on Amazon S3 $Url = "Amazon S3 URL/AmazonEC2Launch.msi"
3. Use the following compound command to download the agent and run the install $DownloadFile = "$env:USERPROFILE\Desktop\EC2Launchv2\" + $(Split-Path -Path $Url -Leaf)
Invoke-WebRequest -Uri $Url -OutFile $DownloadFile msiexec /i "$DownloadFile"
Note If you receive an error when downloading the file, and you are using Windows Server 2016 or earlier, TLS 1.2 might need to be enabled for your PowerShell terminal. You can enable TLS 1.2 for the current PowerShell session with the following command and then try again:
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
4. The msiexec command installs EC2Launch v2 in the following location on Windows Server instances: %ProgramFiles%\Amazon\EC2Launch. To verify that the install ran, you can check the local file system on your instance.
AWS Systems Manager Distributor To configure automatic updates for EC2Launch v2 with AWS Systems Manager Quick Setup, see
##### Automatically install and update EC2Launch v2 with AWS Systems Manager Distributor Quick Setup You can also perform a one-time install of the AWSEC2Launch-Agent package from AWS Systems Manager Distributor. For instructions on how to install a package from Systems Manager Distributor, see Install or update packages in the AWS Systems Manager User Guide.

EC2 Image Builder component You can install the ec2launch-v2-windows component when you build a custom image with EC2 Image Builder. For instructions on how to build a custom image with EC2 Image Builder, see Create an image pipeline using the EC2 Image Builder console wizard in the EC2 Image Builder User Guide.
AMI EC2Launch v2 is preinstalled by default on AMIs for the Windows Server 2022 and above operating systems:
- Windows_Server-version-English-Full-Base
- Windows_Server-version-English-Core-Base
- Windows_Server-version-English-Core-EKS_Optimized
- Windows Server version AMIs with all other languages
- Windows Server version AMIs with SQL installed EC2Launch v2 is also preinstalled on the following Windows Server AMIs. You can find these AMIs from the Amazon EC2 console, or by using the following search prefix: EC2LaunchV2- in the AWS CLI.
- EC2LaunchV2-Windows_Server-2019-English-Core-Base
- EC2LaunchV2-Windows_Server-2019-English-Full-Base
- EC2LaunchV2-Windows_Server-2016-English-Core-Base
- EC2LaunchV2-Windows_Server-2016-English-Full-Base Automatically install and update EC2Launch v2 with AWS Systems Manager Distributor Quick Setup With AWS Systems Manager Distributor Quick Setup, you can set up automatic updates for EC2Launch v2. The following process sets up a Systems Manager Association on your instance that automatically updates the EC2Launch v2 agent at a frequency that you specify. The Association that the Distributor Quick Setup creates can include instances within an AWS account and Region, or instances within an AWS Organization. For more information about setting up an organization, see Tutorial: Creating and configuring an organization in the AWS Organizations User Guide.

Before you begin, make sure that your instances meet all of the prerequisites.
###### Prerequisites To set up automatic updates with Distributor Quick Setup, your instances must meet the following prerequisites.
- You have at least one running instance that supports EC2Launch v2. See supported operating systems for EC2Launch v2.
- You've performed the Systems Manager set-up tasks on your instances. For more information, see Setting up Systems Manager in the AWS Systems Manager User Guide.
- EC2Launch v2 must be the only launch agent installed on your instance. If you have more than one launch agent installed, your Distributor Quick Setup configuration will fail. Before you configure EC2Launch v2 with a Distributor Quick Setup, uninstall EC2Config or EC2Launch v1 launch agents, if they exist.
###### Configure Distributor Quick Setup for EC2Launch v2 To create a configuration for EC2Launch v2 with Distributor Quick Setup, use the following settings when you complete the steps for Distributor package deployment:
- Software packages: Amazon EC2Launch v2 agent.
- Update frequency: Select a frequency from the list.
- Targets: Choose from the available deployment options.
To check the status of your configuration, navigate to the Systems Manager Quick Setup Configurations tab in the AWS Management Console.
1. Open the AWS Systems Manager console at https://console.aws.amazon.com/systems- manager/.
2. In the navigation pane, choose Quick Setup.
3. In the Configurations tab, select the row that's associated with the configuration that you created. The Configurations tab lists your configurations, and includes a summary of key details, such as Region, Deployment status, and Association status.

Note The association name for every EC2Launch v2 Distributor configuration begins with the following prefix: AWS-QuickSetup-Distributor-EC2Launch-Agent-.
4. To view details, select the configuration and choose View details.
For more information and troubleshooting steps, see Troubleshooting Quick Setup results in the AWS Systems Manager User Guide.
##### EC2Launch v2 downloads on Amazon S3 To install the latest version of EC2Launch v2, download the installer from the following location:
- https://s3.amazonaws.com/amazon-ec2launch-v2/windows/amd64/latest/ AmazonEC2Launch.msi
##### Configure install options When you install or upgrade EC2Launch v2, you can configure installation options with the EC2Launch v2 install dialog or with the msiexec command in a command line shell.
The first time the EC2Launch v2 installer runs on an instance, it initializes launch agent settings on your instance as follows:
- It creates the local path and writes the launch agent file to it. This is sometimes referred to as a clean install.
- It creates the EC2LAUNCH_TELEMETRY environment variable if it doesn't already exist, and sets it based on your configuration.
For configuration details, select the tab that matches the configuration method that you'll use.
Amazon EC2Launch Setup dialog When you install or upgrade EC2Launch v2, you can configure the following installation options through the EC2Launch v2 install dialog.

Basic Install options Send Telemetry When you include this feature in the setup dialog, the installer sets the EC2LAUNCH_TELEMETRY environment variable to a value of 1. If you disable Send Telemetry, the installer sets the environment variable to a value of 0.
When the EC2Launch v2 agent runs, it reads the EC2LAUNCH_TELEMETRY environment variable to determine whether to upload telemetry data. If the value equals 1, it uploads the data. Otherwise, it doesn't upload.
Default configuration The default configuration for EC2Launch v2 is to overwrite the local launch agent if it exists already. The first time you run an install on an instance, the default configuration performs a clean install. If you disable the default configuration on the initial install, the installation fails.
If you run the install again on the instance, you can disable the default configuration to perform an upgrade that doesn't replace the %ProgramData%/Amazon/EC2Launch/ config/agent-config.yml file.
Example: Upgrade EC2Launch v2 with telemetry The following example shows the EC2Launch v2 setup dialog configured to upgrade the current installation and enable telemetry. This configuration performs an install without replacing the agent configuration file, and sets the EC2LAUNCH_TELEMETRY environment variable to a value of 1.

Command line When you install or upgrade EC2Launch v2, you can configure the following installation options with the msiexec command in a command line shell.
ADDLOCAL parameter values Basic (required)
Install the launch agent. If this value is not present in the ADDLOCAL parameter, the installation ends.
Clean When you include the Clean value in the ADDLOCAL parameter, the installer writes the agent configuration file to the following location: %ProgramData%/Amazon/EC2Launch/ config/agent-config.yml. If the agent configuration file already exists, it overwrites the file.
When you leave the Clean value out of the ADDLOCAL parameter, the installer performs an upgrade that doesn't replace the agent configuration file.

#### Telemetry When you include the Telemetry value in the ADDLOCAL parameter, the installer sets the EC2LAUNCH_TELEMETRY environment variable to a value of 1.
When you leave the Telemetry value out of the ADDLOCAL parameter, the installer sets the environment variable to a value of 0.
When the EC2Launch v2 agent runs, it reads the EC2LAUNCH_TELEMETRY environment variable to determine whether to upload telemetry data. If the value equals 1, it uploads the data. Otherwise, it doesn't upload.
Example: install EC2Launch v2 with telemetry & msiexec /i "C:\Users\Administrator\Desktop\EC2Launchv2\AmazonEC2Launch.msi"
 ADDLOCAL="Basic,Clean,Telemetry" /q
##### Verify the EC2Launch v2 version Use one of the following procedures to verify the version of EC2Launch v2 that is installed on your instances.
PowerShell Verify the installed version of EC2Launch v2 with Windows PowerShell, as follows.
1. Launch an instance from your AMI and connect to it.
2. Run the following command in PowerShell to verify the installed version of EC2Launch v2:
& "C:\Program Files\Amazon\EC2Launch\EC2Launch.exe" version Windows Control Panel Verify the installed version of EC2Launch v2 in the Windows Control Panel, as follows.
1. Launch an instance from your AMI and connect to it.
2. Open the Windows Control Panel and choose Programs and Features.

3. Look for Amazon EC2Launch in the list of installed programs. Its version number appears in the Version column.
To view the latest updates for the AWS Windows AMIs, see Windows AMI version history in the AWS Windows AMI Reference.
For the latest version of EC2Launch v2, see EC2Launch v2 version history.
You can receive notifications when new versions of the EC2Launch v2 service are released. For more information, see Subscribe to EC2 Windows launch agent notifications.
#### Configure EC2Launch v2 settings for Windows instances This section contains information about how to configure settings for EC2Launch v2.
Topics include:
- Change settings using the EC2Launch v2 settings dialog box
- Configure EC2Launch v2 using the CLI
- EC2Launch v2 task configuration
- EC2Launch v2 exit codes and reboots
- EC2Launch v2 and Sysprep
##### Change settings using the EC2Launch v2 settings dialog box The following procedure describes how to use the EC2Launch v2 settings dialog box to enable or disable settings.
Note If you improperly configure custom tasks in the agent-config.yml file, and you attempt to open the Amazon EC2Launch settings dialog box, you will receive an error. For example schema, see Example: agent-config.yml.
1. Launch and connect to your Windows instance.
2. From the Start menu, choose All Programs, and then navigate to EC2Launch settings. Before you choose Shutdown with Sysprep or Shutdown without Sysprep, make sure that you save any changes that you want to apply when you run the shutdown.


3. On the General tab of the EC2Launch settings dialog box, you can enable or disable the following settings. a.
Set Computer Name If this setting is enabled (it is disabled by default), the current host name is compared to the desired host name at each boot. If the host names do not match, the host name is reset, and the system then optionally reboots to pick up the new host name. If a custom host name is not specified, it is generated using the hexadecimal-formatted private IPv4 address, for example, ip-AC1F4E6. To prevent your existing host name from being modified, do not enable this setting. b.
Extend Boot Volume This setting dynamically extends Disk 0/Volume 0 to include any unpartitioned space.
This can be useful when the instance is booted from a root volume that has a custom size. c.
Set Administrator Account When enabled, you can set the username and password attributes for the administrator account that is created on your local machine. If this feature is not enabled, an administrator account is not created on the system following Sysprep. Provide a password in adminPassword only if adminPasswordtype is Specify.
The password types are defined as follows: i.
Random EC2Launch generates a password and encrypts it using the user's key. The system disables this setting after the instance is launched so that this password persists if the instance is rebooted or stopped and started. ii.
Specify EC2Launch uses the password that you specify in adminPassword. If the password does not meet the system requirements, EC2Launch generates a random password instead. The password is stored in agent-config.yml as clear text and is deleted after Sysprep sets the administrator password. EC2Launch encrypts the password using the user's key. iii.
Do not set

EC2Launch uses the password that you specify in the unattend.xml file. If you don't specify a password in unattend.xml, the administrator account is disabled. d.
Start SSM Service When selected, the Systems Manager service is enabled to start following Sysprep.
EC2Launch v2 performs all of the tasks described earlier, and the SSM Agent processes requests for Systems Manager capabilities, such as Run Command and State Manager.
You can use Run Command to upgrade your existing instances to use the latest version of the EC2Launch v2 service and SSM Agent. For more information, see Update SSM Agent using Run Command in the AWS Systems Manager User Guide. e.
Optimize ENA When selected, ENA settings are configured to ensure that ENA Receive Side Scaling and Receive Queue Depth settings are optimized for AWS. For more information, see Configure Receive side scaling CPU affinity. f.
Enable SSH This setting enables OpenSSH for later Windows versions to allow for remote system administration. g.
Enable Jumbo Frames Select to enable Jumbo Frames. Jumbo Frames can have unintended effects on your network communications, so ensure you understand how Jumbo Frames will impact your system before enabling. For more information about Jumbo Frames, see Jumbo frames (9001 MTU). h.
Prepare for Imaging Select whether you want your EC2 instance to shut down with or without Sysprep. When you want to run Sysprep with EC2Launch v2, choose Shutdown with Sysprep.
4. On the DNS Suffix tab, you can select whether you want to add a DNS suffix list for DNS resolution of servers running in EC2, without providing the fully qualified domain name. DNS suffixes can contain the variables $REGION and $AZ. Only suffixes that do not already exist will be added to the list.

5. On the Wallpaper tab, you can configure your instance wallpaper with a background image, and specify instance details for the wallpaper to display. Amazon EC2 generates the details each time you log in.
You can configure your wallpaper with the following controls.
- Display instance details on wallpaper – This checkbox activates or deactivates instance detail display on the wallpaper.
- Image path (.jpg) – Specify the path to the image to use as the wallpaper background.
- Select attributes to display on wallpaper – Select the check boxes for the instance details that you want to appear on the wallpaper. Clear the check boxes for previously selected instance details that you want to remove from the wallpaper.
- Display Instance Tags on wallpaper – Select one of the following settings to display instance tags on the wallpaper:
- None – Don't display any instance tags on the wallpaper.
- Show all – Display all instance tags on the wallpaper.
- Show filtered – Display specified instance tags on the wallpaper. When you select this setting, you can add instance tags that you want to display on your wallpaper in the Instance tag filter box.

Note You must enable tags in metadata to show tags on the wallpaper. For more information about instance tags and metadata, see View tags for your EC2 instances using instance metadata.


6. On the Volumes tab, select whether you want to initialize the volumes that are attached to the instance. Enabling sets drive letters for any additional volumes and extends them to use available space. If you select All, all of the storage volumes are initialized. If you select Devices, only devices that are specified in the list are initialized. You must enter the device for each device to be initialized. Use the devices listed on the EC2 console, for example, xvdb or /dev/ nvme0n1. The dropdown list displays the storage volumes that are attached to the instance. To enter a device that is not attached to the instance, enter it in the text field.
Name, Letter, and Partition are optional fields. If no value is specified for Partition, storage volumes larger than 2 TB are initialized with the gpt partition type, and those smaller than 2 TB are initialized with the mbr partition type. If devices are configured, and a non-NTFS device either contains a partition table, or the first 4 KB of the disk contain data, then the disk is skipped and the action logged.


##### Configure EC2Launch v2 using the CLI You can use the Command Line Interface (CLI) to configure your EC2Launch settings and manage the service. The following section contains descriptions and usage information for the CLI commands that you can use to manage EC2Launch v2.
Commands
- collect-logs
- get-agent-config
- list-volumes
- reset
- run
- status
- sysprep
- validate
- version
- wallpaper
###### collect-logs Collects log files for EC2Launch, zips the files, and places them in a specified directory.
Example ec2launch collect-logs -o C:\Mylogs.zip Usage ec2launch collect-logs [flags]
Flags -h, --help help for collect-logs -o, --output string

path to zipped output log files
###### get-agent-config Prints agent-config.yml in the format specified (JSON or YAML). If no format is specified, agent-config.yml is printed in the format previously specified.
Example ec2launch get-agent-config -f json Usage ec2launch get-agent-config [flags]
Flags -h, --help help for get-agent-config -f, --format string output format of agent-config file: json, yaml
###### list-volumes Lists all of the storage volumes attached to the instance, including ephemeral and EBS volumes.
Example ec2launch list-volumes Usage ec2launch list-volumes Flags -h, --help help for list-volumes

###### reset The main goal of this task is to reset the agent for the next time that it runs. To do that, the reset command deletes all of the agent state data for EC2Launch v2 from the local EC2Launch directory (see EC2Launch v2 directory structure). Reset optionally deletes the service and Sysprep logs.
Script behavior depends on what mode the agent runs the scripts in – inline, or detached.
Inline (default)
The EC2Launch v2 agent runs scripts one at a time (detach: false). This is the default setting.
Note When your inline script issues a reset or sysprep command, it runs immediately and resets the agent. The current task finishes, then the agent shuts down without running any further tasks.
For example, if the task that issues the command would have been followed by a startSsm task (included by default after user data runs), the task doesn't run and the Systems Manager service never starts.
Detached The EC2Launch v2 agent runs scripts concurrently with other tasks (detach: true).
Note When your detached script issues a reset or sysprep command, those commands wait for the agent to finish before they run. Tasks after the executeScript will still run.
Example ec2launch reset -c Usage ec2launch reset [flags]

Flags -c, --clean cleans instance logs before reset -h, --help help for reset
###### run Runs EC2Launch v2.
Example ec2launch run Usage ec2launch run [flags]
Flags -h, --help help for run
###### status Gets the status of the EC2Launch v2 agent. Optionally blocks the process until the agent is finished. The process exit code determines the agent state:
- 0 –the agent ran and was successful.
- 1 – the agent ran and failed.
- 2 – the agent is still running.
- 3 – the agent is in an unknown state. The agent state is not running or stopped.
- 4 – an error occurred when attempting to retrieve the agent state.
- 5 – the agent is not running and the status of the last known run is unknown. This could mean one of the following:

- both the state.json and previous-state.json are deleted.
- the previous-state.json is corrupted.
This is the agent state after running the reset command.
Example: ec2launch status -b Usage ec2launch status [flags]
Flags -b,--block blocks the process until the agent finishes running -h,--help help for status
###### sysprep The main goal of this task is to reset the agent for the next time that it runs. To do that, the sysprep command resets the agent state, updates the unattend.xml file, disables RDP, and runs Sysprep.
Script behavior depends on what mode the agent runs the scripts in – inline, or detached.
Inline (default)
The EC2Launch v2 agent runs scripts one at a time (detach: false). This is the default setting.
Note When your inline script issues a reset or sysprep command, it runs immediately and resets the agent. The current task finishes, then the agent shuts down without running any further tasks.

For example, if the task that issues the command would have been followed by a startSsm task (included by default after user data runs), the task doesn't run and the Systems Manager service never starts.
Detached The EC2Launch v2 agent runs scripts concurrently with other tasks (detach: true).
Note When your detached script issues a reset or sysprep command, those commands wait for the agent to finish before they run. Tasks after the executeScript will still run.
Example: ec2launch sysprep Usage ec2launch sysprep [flags]
Flags -c,--clean cleans instance logs before sysprep -h,--help help for Sysprep -s,--shutdown shuts down the instance after sysprep
###### validate Validates the agent-config file C:\ProgramData\Amazon\EC2Launch\config\agent- config.yml.

Example ec2launch validate Usage ec2launch validate [flags]
Flags -h , --help help for validate
###### version Gets the executable version.
Example ec2launch version Usage ec2launch version [flags]
Flags -h, --help help for version wallpaper Sets new wallpaper to the wallpaper path that is provided (.jpg file), and displays the selected instance details.
###### Syntax ec2launch wallpaper ^

--path="C:\ProgramData\Amazon\EC2Launch\wallpaper\Ec2Wallpaper.jpg" ^ --all-tags ^ -- attributes=hostName,instanceId,privateIpAddress,publicIpAddress,ipv6Address,instanceSize,availa
###### Inputs Parameters --allowed-tags [tag-name-1, tag-name-n]
(Optional) Base64 encoded JSON array of instance tag names to display on the wallpaper. You can use this tag or the --all-tags, but not both.
--attributes attribute-string-1, attribute-string-n (Optional) A comma-separated list of wallpaper attribute strings to apply settings to the wallpaper.
[--path | -p] path-string (Required) Specifies the wallpaper background image file path.
Flags --all-tags (Optional) Displays all of the instance tags on the wallpaper. You can use this tag or the -- allowed-tags, but not both.
[--help | -h]
Displays help for the wallpaper command.
##### EC2Launch v2 task configuration This section includes the configuration schema, tasks, details, and examples for agent- config.yml and user data.
Tasks and examples
- Schema: agent-config.yml

- Configure EC2Launch v2 user data scripts that run during launch or reboot
###### Schema: agent-config.yml The structure of the agent-config.yml file is shown below. Note that a task cannot be repeated in the same stage. For task properties, see the task descriptions that follow.
###### Document structure: agent-config.yml JSON { "version": "1.1", "config": [ { "stage": "string", "tasks": [ { "task": "string", "inputs": { ...
     } }, ...
   ]
  }, ...
 ]
} YAML version: 1.1 config:
- stage: string tasks:
  - task: string inputs:
   ...
  ...
...

###### Example: agent-config.yml The following example shows settings for the agent-config.yml configuration file. version: 1.1 config:
- stage: boot tasks:
  - task: extendRootPartition
- stage: preReady tasks:
  - task: activateWindows inputs: activation: type: amazon
  - task: setDnsSuffix inputs: suffixes:
      - $REGION.ec2-utilities.amazonaws.com
  - task: setAdminAccount inputs: password: type: random
  - task: setWallpaper inputs: path: C:\ProgramData\Amazon\EC2Launch\wallpaper\Ec2Wallpaper.jpg attributes:
      - hostName
      - instanceId
      - privateIpAddress
      - publicIpAddress
      - instanceSize
      - availabilityZone
      - architecture
- stage: postReady tasks:
  - task: startSsm
###### Configure EC2Launch v2 user data scripts that run during launch or reboot The following JSON and YAML examples show the document structure for user data. Amazon EC2 parses each task named in the tasks array that you specify in the document. Each task has its own

set of properties and requirements. For details, see the Task definitions for EC2Launch v2 startup tasks.
Note A task must only appear once in the user data tasks array.
###### Document structure: user data JSON { "version": "1.1", "tasks": [ { "task": "string", "inputs": { ...
   }, }, ...
 ]
} YAML version: 1.1 tasks:
- task: string inputs:
    ...
...
###### Example: user data For more information about user data, see How Amazon EC2 handles user data for Windows instances.
The following YAML document example shows a PowerShell script that EC2Launch v2 runs as user data to create a file.

version: 1.1 tasks:
- task: executeScript inputs:
  - frequency: always type: powershell runAs: localSystem content: |- New-Item -Path 'C:\PowerShellTest.txt' -ItemType File You can use an XML format for the user data that's compatible with previous versions of the launch agent. EC2Launch v2 runs the script as an executeScript task in the UserData stage.
To conform with EC2Launch v1 and EC2Config behavior, the user data script runs as an attached/ inline process by default.
You can add optional tags to customize how your script runs. For example, to run the user data script when the instance reboots in addition to one time when the instance launches, you can use the following tag:
<persist>true</persist>
Example:
<powershell>
  $file = $env:SystemRoot + "\Temp" + (Get-Date).ToString("MM-dd-yy-hh-mm")
  New-Item $file -ItemType file </powershell>
<persist>true</persist>
You can specify one or more PowerShell arguments with the <powershellArguments> tag. If no arguments are passed, EC2Launch v2 adds the following argument by default: - ExecutionPolicy Unrestricted.
Example:
<powershell>
  $file = $env:SystemRoot + "\Temp" + (Get-Date).ToString("MM-dd-yy-hh-mm")
  New-Item $file -ItemType file </powershell>
<powershellArguments>-ExecutionPolicy Unrestricted -NoProfile -NonInteractive</ powershellArguments>

To run an XML user data script as a detached process, add the following tag to your user data.
<detach>true</detach>
Example:
<powershell>
  $file = $env:SystemRoot + "\Temp" + (Get-Date).ToString("MM-dd-yy-hh-mm")
  New-Item $file -ItemType file </powershell>
<detach>true</detach>
Note The detach tag is not supported on previous launch agents.
###### Change log: user data The following table lists changes for user data, and cross-references them to the EC2Launch v2 agent version that applies.
User data version Details Introduced in 1.1
- User data tasks run before the   PostReady  stage in the agent config   file.
- Runs user data before starting the Systems Manager Agent (same behavior as EC2Launch v1 and  EC2Config).* EC2Launch v2 version 2.0.1245 1.0
- Will be deprecated.
- User data tasks run after the   PostReady  stage in the agent config   file. This is not backwards compatible with  E C2Launch v1.
- EC2Launch v2 version 2.0.0

User data version Details Introduced in Impacted by a race condition between Systems Manager Agent start and user data tasks.
* When used with the default agent-config.yml file.
##### EC2Launch v2 exit codes and reboots You can use EC2Launch v2 to define how exit codes are handled by your scripts. By default, the exit code of the last command that is run in a script is reported as the exit code for the entire script. For example, if a script includes three commands and the first command fails but the following ones succeed, the run status is reported as success because the final command succeeded.
If you want a script to reboot an instance, then you must specify exit 3010 in your script, even when the reboot is the last step in your script. exit 3010 instructs EC2Launch v2 to reboot the instance and call the script again until it returns an exit code that is not 3010, or until the maximum reboot count has been reached. EC2Launch v2 permits a maximum of 5 reboots per task. If you attempt to reboot an instance from a script by using a different mechanism, such as Restart-Computer, then the script run status will be inconsistent. For example, it may get stuck in a restart loop or not perform the restart.
If you are using an XML user data format that is compatible with older agents, the user data may run more times than you intend it to. For more information, see Service runs user data more than once in the Troubleshooting section.
##### EC2Launch v2 and Sysprep The EC2Launch v2 service runs Sysprep, a Microsoft tool that enables you to create a customized Windows AMI that can be reused. When EC2Launch v2 calls Sysprep, it uses the files in %ProgramData%\Amazon\EC2Launch to determine which operations to perform. You can edit these files indirectly using the EC2Launch settings dialog box, or directly using a YAML editor or a text editor. However, there are some advanced settings that aren't available in the EC2Launch settings dialog box, so you must edit those entries directly.
If you create an AMI from an instance after updating its settings, the new settings are applied to any instance that's launched from the new AMI. For information about creating an AMI, see Create an Amazon EBS-backed AMI.

#### Task definitions for EC2Launch v2 startup tasks Each task that EC2Launch v2 runs during launch or startup has its own set of properties and requirements. Task details include settings for how often a task runs – once, or always, what stage of the agent boot process it runs in, syntax, and YAML document examples. For more information, review the task details shown in this reference.
EC2Launch v2 Tasks
- activateWindows
- enableJumboFrames
- enableOpenSsh
- executeProgram
- executeScript
- extendRootPartition
- initializeVolume
- optimizeEna
- setAdminAccount
- setDnsSuffix
- setHostName
- setWallpaper
- startSsm
- sysprep
- writeFile
##### activateWindows Activates Windows against a set of AWS KMS servers. Activation is skipped if the instance is detected as Bring-Your-Own-License (BYOL).
Frequency — once AllowedStages — [PreReady]
Inputs — activation: (map)

type: (string) activation type to use, set to amazon Example task: activateWindows inputs: activation: type: amazon
##### enableJumboFrames Enables Jumbo Frames, which increase the maximum transmission unit (MTU) of the network adapter. For more information, see Jumbo frames (9001 MTU).
Frequency — always AllowedStages — [PostReady, UserData]
Inputs — none Example task: enableJumboFrames
##### enableOpenSsh Enables Windows OpenSSH and adds the public key for the instance to the authorized keys folder.
Frequency — once AllowedStages — [PreReady, UserData]
Inputs — none Example The following example shows how to enable OpenSSH on an instance, and to add the public key for the instance to the authorized keys folder. This configuration works only on instances running Windows Server 2019 and later versions. task: enableOpenSsh

##### executeProgram Runs a program with optional arguments and a specified frequency.
Stages: You can run the executeProgram task during the PreReady, PostReady, and UserData stages.
Frequency: configurable, see Inputs.
Inputs This section contains one or more programs for the executeProgram task to run (inputs). Each input can include the following configurable settings: frequency (string)
(Required) Specify exactly one of the following values:
- once
- always path (string)
(Required) The file path for the executable to run. arguments (list of strings)
(Optional) A comma separated list of arguments to provide to the program as input. runAs (string)
(Required) Must be set to localSystem Output All of the tasks write logfile entries to the agent.log file. Additional output from the executeProgram task is stored separately in a dynamically named folder, as follows:
%LocalAppData%\Temp\EC2Launch#########\outputfilename.tmp The exact path to the output files is included in the agent.log file, for example:
Program file is created at: C:\Windows\system32\config\systemprofile\AppData\Local \Temp\EC2Launch123456789\ExecuteProgramInputs.tmp Output file is created at: C:\Windows\system32\config\systemprofile\AppData\Local \Temp\EC2Launch123456789\Output.tmp

Error file is created at: C:\Windows\system32\config\systemprofile\AppData\Local \Temp\EC2Launch123456789\Err.tmp Output files for the executeProgram task ExecuteProgramInputs.tmp Contains the path for the executable, and all of the input parameters that the executeProgram task passes to it when it runs.
Output.tmp Contains runtime output from the program that the executeProgram task runs.
Err.tmp Contains runtime error messages from the program that the executeProgram task runs.
Examples The following examples show how to run an executable file from a local directory on an instance with the executeProgram task.
Example 1: Setup executable with one argument This example shows an executeProgram task that runs a setup executable in quiet mode. task: executeProgram inputs:
    - frequency: always path: C:\Users\Administrator\Desktop\setup.exe arguments: ['-quiet']
Example 2: VLC executable with two arguments This example shows an executeProgram task that runs a VLC executable file with two arguments passed as input parameters. task: executeProgram inputs:
    - frequency: always path: C:\vlc-3.0.11-win64.exe arguments: ['/L=1033','/S'] runAs: localSystem

##### executeScript Runs a script with optional arguments and a specified frequency. Script behavior depends on what mode the agent runs the scripts in – inline, or detached.
Inline (default)
The EC2Launch v2 agent runs scripts one at a time (detach: false). This is the default setting.
Note When your inline script issues a reset or sysprep command, it runs immediately and resets the agent. The current task finishes, then the agent shuts down without running any further tasks.
For example, if the task that issues the command would have been followed by a startSsm task (included by default after user data runs), the task doesn't run and the Systems Manager service never starts.
Detached The EC2Launch v2 agent runs scripts concurrently with other tasks (detach: true).
Note When your detached script issues a reset or sysprep command, those commands wait for the agent to finish before they run. Tasks after the executeScript will still run.
Stages: You can run the executeScript task during the PreReady, PostReady, and UserData stages.
Frequency: configurable, see Inputs.
Inputs This section contains one or more scripts for the executeScript task to run (inputs). Each input can include the following configurable settings:

frequency (string)
(Required) Specify exactly one of the following values:
- once
- always type (string)
(Required) Specify exactly one of the following values:
- batch
- powershell arguments (list of strings)
(Optional) A list of string arguments to pass to the shell (not to the PowerShell script). This parameter isn't supported for type: batch. If no arguments are passed, EC2Launch v2 adds the following argument by default: -ExecutionPolicy Unrestricted. content (string)
(Required) Script content. runAs (string)
(Required) Specify exactly one of the following values:
- admin
- localSystem detach (Boolean)
(Optional) The EC2Launch v2 agent defaults to run scripts one at a time (detach: false).
To run the script concurrently with other tasks, set the value to true (detach: true).
Note Script exit codes (including 3010) have no effect when detach is set to true.
Output All of the tasks write logfile entries to the agent.log file. Additional output from script that the executeScript task runs is stored separately in a dynamically named folder, as follows:

%LocalAppData%\Temp\EC2Launch#########\outputfilename.ext The exact path to the output files is included in the agent.log file, for example:
Program file is created at: C:\Windows\system32\config\systemprofile\AppData\Local \Temp\EC2Launch123456789\UserScript.ps1 Output file is created at: C:\Windows\system32\config\systemprofile\AppData\Local \Temp\EC2Launch123456789\Output.tmp Error file is created at: C:\Windows\system32\config\systemprofile\AppData\Local \Temp\EC2Launch123456789\Err.tmp Output files for the executeScript task UserScript.ext Contains the script that the executeScript task ran. The file extension depends on the type of script you specified in the type parameter for the executeScript task, as follows:
- If the type is batch, then the file extension is .bat.
- If the type is powershell, then the file extension is .ps1.
Output.tmp Contains runtime output from the script that the executeScript task runs.
Err.tmp Contains runtime error messages from the script that the executeScript task runs.
Examples The following examples show how to run an inline script with the executeScript task.
Example 1: Hello world output text file This example shows an executeScript task that runs a PowerShell script to create a "Hello world" text file on the C: drive. task: executeScript inputs:
    - frequency: always type: powershell runAs: admin content: |- New-Item -Path 'C:\PowerShellTest.txt' -ItemType File

        Set-Content 'C:\PowerShellTest.txt' "Hello world"
Example 2: Run two scripts This example shows that the executeScript task can run more than one script, and the script type doesn't necessarily need to match.
The first script (type: powershell) writes a summary of the processes that are currently running on the instance to a text file located on the C: drive.
The second script (batch) writes the system information to the Output.tmp file. task: executeScript inputs:
    - frequency: always type: powershell runAs: localSystem content: | Get-Process | Out-File -FilePath C:\Process.txt
    - frequency: always type: batch runAs: localSystem content: | systeminfo Example 3: Idempotent system configuration with reboots This example shows an executeScript task that runs an idempotent script to perform the following system configuration with a reboot between each step:
- Rename the computer.
- Join the computer to the domain.
- Enable Telnet.
The script ensures that each operation runs one time only. This prevents a reboot loop and makes the script idempotent. task: executeScript inputs:
    - frequency: always type: powershell runAs: localSystem

      content: |- $name = $env:ComputerName if ($name -ne $desiredName) { Rename-Computer -NewName $desiredName exit 3010 } $domain = Get-ADDomain if ($domain -ne $desiredDomain)
        { Add-Computer -DomainName $desiredDomain exit 3010 } $telnet = Get-WindowsFeature -Name Telnet-Client if (-not $telnet.Installed)
        { Install-WindowsFeature -Name "Telnet-Client" exit 3010 }
##### extendRootPartition Extends the root volume to use all of the available space on the disk.
Frequency — once AllowedStages — [Boot]
Inputs — none Example task: extendRootPartition
##### initializeVolume Initializes empty volumes that are attached to the instance so that they're activated and partitioned. The launch agent skips initialization if it detects that the volume is not empty. A volume is considered empty if the first 4 KiB of the volume are empty, or if the volume doesn't have a Windows-recognizable drive layout.
The letter input parameter is always applied when this task runs, regardless of whether the drive is already initialized.

The initializeVolume task performs the following actions.
- Set disk attributes offline and readonly to false.
- Create a partition. If no partition type is specified in the partition input parameter, the following defaults apply:
- If the disk size is smaller than 2 TB, set the partition type to mbr.
- If the disk size is 2 TB or larger, set the partition type to gpt.
- Format the volume as NTFS.
- Set the volume label as follows:
- Use the value of the name input parameter, if specified.
- If the volume is ephemeral, and no name was specified, set the volume label to Temporary Storage Z.
- If the volume is ephemeral (SSD or HDD – not Amazon EBS), create an Important.txt file at the root of the volume with the following content:
This is an 'Instance Store' disk and is provided at no additional charge.
*This disk offers increased performance since it is local to the host *The number of Instance Store disks available to an instance vary by instance type *DATA ON THIS DRIVE WILL BE LOST IN CASES OF IMPAIRMENT OR STOPPING THE INSTANCE.
 PLEASE ENSURE THAT ANY IMPORTANT DATA IS BACKED UP FREQUENTLY For more information, please refer to: Instance store temporary block storage for EC2 instances.
- Set the drive letter to the value specified in the letter input parameter.
Stages: You can run the initializeVolume task during the PostReady and UserData stages.
Frequency: always.
Inputs You can configure runtime parameters as follows: devices (list of maps)
(Conditional) Configuration for each device that the launch agent initializes. This is required if the initialize input parameter is set to devices.

- device (string, required) – Identifies the device during instance creation. For example, xvdb, xvdf, or \dev\nvme0n1.
- letter (string, optional) – One character. The drive letter to assign.
- name (string, optional) – The volume name to assign.
- partition (string, optional) – Specify one of the following values for the type of partition to create, or let the launch agent default based on volume size:
- mbr
- gpt initialize (string)
(Required) Specify exactly one of the following values:
- all
- devices Examples The following examples show sample input configurations for the initializeVolume task.
Example 1: Initialize two volumes on an instance This example shows an initializeVolume task that initializes two secondary volumes on an instance. The device named DataVolume2 in the example is ephemeral. task: initializeVolume inputs: initialize: devices devices:
  - device: xvdb name: DataVolume1 letter: D partition: mbr
  - device: /dev/nvme0n1 name: DataVolume2 letter: E partition: gpt Example 2: Initialize EBS volumes attached to an instance

This example shows an initializeVolume task that initializes all empty EBS volumes that are attached to the instance. task: initializeVolume inputs: initialize: all
##### optimizeEna Optimizes ENA settings based on the current instance type; might reboot the instance.
Frequency — always AllowedStages — [PostReady, UserData]
Inputs — none Example task: optimizeEna
##### setAdminAccount Sets attributes for the default administrator account that is created on the local machine.
Frequency — once AllowedStages — [PreReady]
Inputs — name: (string) name of the administrator account password: (map) type: (string) strategy to set the password, either as static, random, or doNothing data: (string) stores data if the type field is static Example task: setAdminAccount

inputs: name: Administrator password: type: random
##### setDnsSuffix Adds DNS suffixes to the list of search suffixes. Only suffixes that do not already exist are added to the list. For more information about how launch agents set DNS suffixes, see Configure DNS Suffix for EC2 Windows launch agents.
Frequency — always AllowedStages — [PreReady]
Inputs — suffixes: (list of strings) list of one or more valid DNS suffixes; valid substitution variables are $REGION and $AZ Example task: setDnsSuffix inputs: suffixes:
  - $REGION.ec2-utilities.amazonaws.com
##### setHostName Sets the hostname of the computer to a custom string or, if hostName is not specified, the private IPv4 address.
Frequency — always AllowedStages — [PostReady, UserData]
Inputs — hostName: (string) optional host name, which must be formatted as follows.
- Must be 15 characters or less

- Must contain only alphanumeric (a-z, A-Z, 0-9) and hyphen (-) characters.
- Must not consist entirely of numerical characters. reboot: (boolean) denotes whether a reboot is permitted when the hostname is changed Example task: setHostName inputs: reboot: true
##### setWallpaper Creates the setwallpaper.lnk shortcut file in the startup folder of each existing user except for Default User. This shortcut file runs when the user logs in for the first time after instance boot.
It sets up the instance with a custom wallpaper that displays the instance attributes.
The shortcut file path is:
$env:SystemDrive/Users/<user>/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/ Startup/setwallpaper.lnk Note When you remove the setWallpaper task, it does not delete this shortcut file. For more information, see setWallpaper task is not enabled but the wallpaper resets at reboot.
Stages: You can configure wallpaper during the PreReady and UserData stages.
Frequency: always Wallpaper configuration You can use the following settings to configure your wallpaper.
Inputs Input parameters that you provide, and attributes that you can set to configure your wallpaper:

path (string)
(Required) The filename path of the local .jpg format image file to use for your wallpaper image. attributes (list of strings)
(Optional) You can add one or more of the following attributes to your wallpaper:
- architecture
- availabilityZone
- hostName
- instanceId
- instanceSize
- privateIpAddress
- publicIpAddress
- ipv6Address instanceTags (Optional) You can use exactly one of the following options for this setting.
- AllTags (string) – Add all instance tags to your wallpaper. instanceTags: AllTags
- instanceTags (list of strings) – Specify a list of instance tag names to add to your wallpaper. For example: instanceTags:
  - Tag 1
  - Tag 2 Example The following example shows wallpaper configuration inputs that set the file path for the wallpaper background image, along with instance tags named Tag 1 and Tag 2, and attributes that include the host name, instance ID, and private and public IP addresses for the instance. task: setWallpaper

inputs: path: C:\ProgramData\Amazon\EC2Launch\wallpaper\Ec2Wallpaper.jpg attributes:
  - hostName
  - instanceId
  - privateIpAddress
  - publicIpAddress instanceTags:
  - Tag 1
  - Tag 2 Note You must enable tags in metadata to show tags on the wallpaper. For more information about instance tags and metadata, see View tags for your EC2 instances using instance metadata.
##### startSsm Starts the Systems Manager (SSM) service following Sysprep.
Frequency — always AllowedStages — [PostReady, UserData]
Inputs — none Example task: startSsm
##### sysprep Resets the service state, updates unattend.xml, disables RDP, and runs Sysprep. This task runs only after all other tasks are completed.
Frequency — once AllowedStages — [UserData]
Inputs —

clean: (boolean) cleans instance logs before running Sysprep shutdown: (boolean) shuts down the instance after running Sysprep Example task: sysprep inputs: clean: true shutdown: true
##### writeFile Writes a file to a destination.
Frequency — see Inputs AllowedStages — [PostReady, UserData]
Inputs — frequency: (string) one of once or always destination: (string) path to which to write the content content: (string) text to write to the destination Example task: writeFile inputs:
  - frequency: once destination: C:\Users\Administrator\Desktop\booted.txt content: Windows Has Booted
#### Troubleshoot issues with the EC2Launch v2 agent This section shows common troubleshooting scenarios for EC2Launch v2, information about viewing Windows event logs, and console log output and messages.
Troubleshooting topics
- Common troubleshooting scenarios

- Windows event logs
- EC2Launch v2 console log output
##### Common troubleshooting scenarios This section shows common troubleshooting scenarios and steps for resolution.
Scenarios
- Service fails to set the wallpaper
- Service fails to run user data
- Service runs a task only one time
- Service fails to run a task
- Service runs user data more than once
- Scheduled tasks from EC2Launch v1 fail to run after migration to EC2Launch v2
- Service initializes an EBS volume that is not empty
- setWallpaper task is not enabled but the wallpaper resets at reboot
- Service stuck in running status
- Invalid agent-config.yml prevents opening EC2Launch v2 settings dialog box
- task:executeScript should be unique and only invoked once
###### Service fails to set the wallpaper Resolution
1. Check that %AppData%\Roaming\Microsoft\Windows\Start Menu\Programs\Startup \setwallpaper.lnk exists.
2. Check %ProgramData%\Amazon\EC2Launch\log\agent.log to see if any errors occurred.
###### Service fails to run user data Possible cause: Service may have failed before running user data.
Resolution
1. Check %ProgramData%\Amazon\EC2Launch\state\previous-state.json.

2. See if boot, network, preReady, and postReadyLocalData have all been marked as success.
3. If one of the stages failed, check %ProgramData%\Amazon\EC2Launch\log\agent.log for specific errors.
###### Service runs a task only one time Resolution
1. Check the frequency of the task.
2. If the service already ran after Sysprep, and the task frequency is set to once, the task will not run again.
3. Set the frequency of the task to always if you want it to run the task every time EC2Launch v2 runs.
###### Service fails to run a task Resolution
1. Check the latest entries in %ProgramData%\Amazon\EC2Launch\log\agent.log.
2. If no errors occurred, try running the service manually from "%ProgramFiles%\Amazon \EC2Launch\EC2Launch.exe" run to see if the tasks succeed.
###### Service runs user data more than once Resolution User data is handled differently between EC2Launch v1 and EC2Launch v2. EC2Launch v1 runs user data as a scheduled task on the instance when persist is set to true. If persist is set to false, the task is not scheduled even when it exits with a reboot or is interrupted while running.
EC2Launch v2 runs user data as an agent task and tracks its run state. If user data issues a computer restart or if user data was interrupted while running, the run state persists as pending and the user data will run again at the next instance boot. If you want to prevent the user data script from running more than once, make the script idempotent.
The following example idempotent script sets the computer name and joins a domain.

<powershell>
  $name = $env:computername if ($name -ne $desiredName) { Rename-Computer -NewName $desiredName } $domain = Get-ADDomain if ($domain -ne $desiredDomain)
  { Add-Computer -DomainName $desiredDomain } $telnet = Get-WindowsFeature -Name Telnet-Client if (-not $telnet.Installed)
  { Install-WindowsFeature -Name "Telnet-Client"
  } </powershell>
<persist>false</persist>
###### Scheduled tasks from EC2Launch v1 fail to run after migration to EC2Launch v2 Resolution The migration tool does not detect any scheduled tasks linked to EC2Launch v1 scripts; therefore, it does not automatically set up those tasks in EC2Launch v2. To configure these tasks, edit the agent-config.yml file, or use the EC2Launch v2 settings dialog box. For example, if an instance has a scheduled task that runs InitializeDisks.ps1, then after you run the migration tool, you must specify the volumes you want to initialize in the EC2Launch v2 settings dialog box. See Step 6 of the procedure to Change settings using the EC2Launch v2 settings dialog box.
###### Service initializes an EBS volume that is not empty Resolution Before it initializes a volume, EC2Launch v2 attempts to detect whether it is empty. If a volume is not empty, it skips the initialization. Any volumes that are detected as not empty are not initialized.
A volume is considered empty if the first 4 KiB of a volume are empty, or if a volume does not have a Windows-recognizable drive layout. A volume that was initialized and formatted on a Linux system does not have a Windows-recognizable drive layout, for example MBR or GPT. Therefore, it will be considered as empty and initialized. If you want to preserve this data, do not rely on EC2Launch v2 empty drive detection. Instead, specify volumes that you would like to initialize in the EC2Launch v2 settings dialog box (see step 6) or in the agent-config.yml.

###### setWallpaper task is not enabled but the wallpaper resets at reboot The setWallpaper task creates the setwallpaper.lnk shortcut file in the startup folder of each existing user. This shortcut file runs when the user logs in for the first time after instance boot. It sets up the instance with a custom wallpaper that displays the instance attributes.
Removing the setWallpaper task does not delete this shortcut file. You must manually delete this file or delete it using a script.
The shortcut path is:
$env:SystemDrive/Users/<user>/AppData/Roaming/Microsoft/Windows/Start Menu/ Programs/Startup/setwallpaper.lnk Resolution Manually delete this file, or delete it using a script.
Example PowerShell script to delete shortcut file foreach ($userDir in (Get-ChildItem "C:\Users" -Force -Directory).FullName)
{ $startupPath = Join-Path $userDir -ChildPath "AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup" if (Test-Path $startupPath)
 { $wallpaperSetupPath = Join-Path $startupPath -ChildPath "setwallpaper.lnk" if (Test-Path $wallpaperSetupPath)
  { Remove-Item $wallpaperSetupPath -Force -Confirm:$false } } }
###### Service stuck in running status
###### Description EC2Launch v2 is blocked, with log messages (agent.log) similar to the following:
2022-02-24 08:08:58 Info:
 *****************************************************************************************

2022-02-24 08:08:58 Info: EC2Launch Service starting 2022-02-24 08:08:58 Info: Windows event custom log exists: Amazon EC2Launch 2022-02-24 08:08:58 Info: ACPI SPCR table not supported. Bailing Out 2022-02-24 08:08:58 Info: Serial port is in use. Waiting for Serial Port...
2022-02-24 08:09:00 Info: ACPI SPCR table not supported. Use default console port.
2022-02-24 08:09:02 Info: ACPI SPCR table not supported. Use default console port.
2022-02-24 08:09:04 Info: ACPI SPCR table not supported. Use default console port.
2022-02-24 08:09:06 Info: ACPI SPCR table not supported. Use default console port.
Possible cause SAC is enabled and using the serial port. For more information, see Use SAC to troubleshoot your Windows instance.
Resolution Try the following steps to resolve this issue:
- Disable the service that is using the serial port.
- If you want the service to continue to use the serial port, write custom scripts to perform launch agent tasks and invoke them as scheduled tasks.
###### Invalid agent-config.yml prevents opening EC2Launch v2 settings dialog box
###### Description EC2Launch v2 settings attempts to parse the agent-config.yml file before it opens the dialog box. If the YAML configuration file does not follow the supported schema, the dialog box will show the following error:
Unable to parse configuration file agent-config.yml. Review configuration file. Exiting application.
Resolution
1. Verify that the configuration file follows the supported schema.
2. If you want to start from scratch, copy the default configuration file into agent-config.yml.
You can use the example agent-config.yml provided in the Task Configuration section.
3. You can also start over by deleting agent-config.yml. EC2Launch v2 settings generates an empty configuration file.

###### task:executeScript should be unique and only invoked once
###### Description A task cannot be repeated in the same stage.
Resolution Some tasks must be input as an array, such as executeScript and executeProgram. For an example of how to write the script as an array, see executeScript.
##### Windows event logs EC2Launch v2 publishes Windows event logs for important events, such as service starting, Windows is ready, and task success and failure. Event identifiers uniquely identify a particular event. Each event contains stage, task, and level information, and a description. You can set triggers for specific events using the event identifier.
Event IDs provide information about an event and uniquely identify some events. The least significant digit of an event ID indicates the severity of an event.
Event Least significant digit Success . . .0 Informational . . .1 Warning . . .2 Error . . .3 Service-related events that are generated when the service starts or stops include a single digit event identifier.
Event Single digit identifier Success 0 Informational 1

Event Single digit identifier Warning 2 Error 3 The event messages for EC2LaunchService.exe events begin with Service:. The event messages for EC2Launch.exe events do not begin with Service:.
Four digit event IDs include information about the stage, task, and severity of an event.
Topics
- Event ID format
- Event ID examples
- Windows event log schema
###### Event ID format The following table shows the format of an EC2Launch v2 event identifier.
3 2 1 0 S T L The letters and numbers in the table represent the following event type and definitions.
Event type Definition S (Stage)
0 - Service-level message 1 - Boot 2 - Network 3 - PreReady

Event type Definition 5 - Windows is Ready 6 - PostReady 7 - User Data T (Task)
The tasks represented by the corresponding two values are  different for each stage.
To view the complete list of  events, see Windows   Event log schema.
L (Level of the event)
0 - Success 1 - Informational 2 - Warning 3 - Error
###### Event ID examples The following are example event IDs.
- 5000 - Windows is ready to use
- 3010 - Activate windows task in PreReady stage was successful
- 6013 - Set wallpaper task in PostReady Local Data stage encountered an error
###### Windows event log schema MessageId/Event Id Event message . . .0 Success . . .1 Informational

MessageId/Event Id Event message . . .2 Warning . . .3 Error x EC2Launch service-level logs 0 EC2Launch service exited successfu lly 1 EC2Launch service informational logs 2 EC2Launch service warning logs 3 EC2Launch service error logs 10 Replace state.json with  prev ious-state.json 100 Serial Port 200 Sysprep 300 PrimaryNic 400 Metadata x000 Stage (1 digit), Task (2 digits), Status (1  digit)
 1000 Boot 1010 Boot - extend_root_partition 2000 Network 2010 Network - add_routes 3000 PreReady

MessageId/Event Id Event message 3010 PreReady - activate_windows 3020 PreReady - install_egpu_manager 3030 PreReady - set_monitor_on 3040 PreReady - set_hibernation 3050 PreReady - set_admin_account 3060 PreReady - set_dns_suffix 3070 PreReady - set_wallpaper 3080 PreReady - set_update_schedule 3090 PreReady - output_log 3100 PreReady - enable_open_ssh 5000 Windows is Ready to use 6000 PostReadyLocalData 7000 PostReadyUserData 6010/7010 PostReadyLocal/UserData - set_wallpaper 6020/7020 PostReadyLocal/UserData - set_update_schedule 6030/7030 PostReadyLocal/UserData - set_hostname 6040/7040 PostReadyLocal/UserData - execute_program

MessageId/Event Id Event message 6050/7050 PostReadyLocal/UserData - execute_script 6060/7060 PostReadyLocal/UserData - manage_package 6070/7070 PostReadyLocal/UserData - initialize_volume 6080/7080 PostReadyLocal/UserData - write_file 6090/7090 PostReadyLocal/UserData - start_ssm 7100 PostReadyUserData - enable_op en_ssh 6110/7110 PostReadyLocal/UserData - enable_jumbo_frames
##### EC2Launch v2 console log output This section contains sample console log output for EC2Launch v2 and lists all of the EC2Launch v2 console log error messages to help you to troubleshoot issues. For more information about instance console output and how to access it, see the section called "Instance console output".
Outputs
- EC2Launch v2 console log output
- EC2Launch v2 console log messages
###### EC2Launch v2 console log output The following is sample console log output for EC2Launch v2. Some values in this example are substituted with representative text surrounded by curly braces.

2025/07/22 21:26:53Z: Windows sysprep configuration complete.
2025/07/22 21:26:53Z: Message: Waiting for access to metadata...
2025/07/22 21:26:53Z: Message: Meta-data is now available.
2025/07/22 21:26:53Z: AMI Origin Version: 2024.12.13 2025/07/22 21:26:53Z: AMI Origin Name: Windows_Server-2022-English-Full-Base 2025/07/22 21:26:53Z: OS: Microsoft Windows NT 10.0.20348 2025/07/22 21:26:53Z: OsVersion: 10.0 2025/07/22 21:26:53Z: OsProductName: Windows Server 2022 Datacenter 2025/07/22 21:26:53Z: OsBuildLabEx: 20348.1.amd64fre.fe_release.210507-1500 2025/07/22 21:26:53Z: OsCurrentBuild: 20348 2025/07/22 21:26:53Z: OsReleaseId: 2009 2025/07/22 21:26:53Z: Language: en-US 2025/07/22 21:26:53Z: TimeZone: UTC 2025/07/22 21:26:53Z: Offset: UTC +0000 2025/07/22 21:26:53Z: Launch: EC2 Launch v2.2.63 2025/07/22 21:26:53Z: AMI-ID: ami-1234567890abcdef1 2025/07/22 21:26:53Z: Instance-ID: i-1234567890abcdef0 2025/07/22 21:26:54Z: Instance Type: t3.xlarge 2025/07/22 21:26:54Z: Driver: AWS NVMe Driver v1.6.0.35 2025/07/22 21:26:54Z: SubComponent: 1.6.0.35; EnableSCSIPersistentReservations: 0 2025/07/22 21:26:54Z: Driver: AWS PV Driver Package v8.5.0 2025/07/22 21:26:55Z: Driver: Amazon Elastic Network Adapter v2.8.0.0 2025/07/22 21:26:55Z: HOSTNAME: EC2AMAZ-9FJG5CC 2025/07/22 21:26:55Z: RDPCERTIFICATE-SUBJECTNAME: {certificate subject name} 2025/07/22 21:26:55Z: RDPCERTIFICATE-THUMBPRINT: {thumbprint hash} 2025/07/22 21:26:56Z: SSM: Amazon SSM Agent v3.3.2746.0 2025/07/22 21:26:57Z: User data format: no_user_data 2025/07/22 21:26:57Z: EC2LaunchTelemetry: IsTelemetryEnabled=true 2025/07/22 21:26:57Z: EC2LaunchTelemetry: AgentOsArch=windows_amd64 2025/07/22 21:26:57Z: EC2LaunchTelemetry: IsAgentScheduledPerBoot=true 2025/07/22 21:26:57Z: EC2LaunchTelemetry: AgentCommandErrorCode=1 2025/07/22 21:26:57Z: EC2LaunchTelemetry: AdminPasswordTypeCode=0 2025/07/22 21:26:57Z: EC2LaunchTelemetry: AgentErrorLocation=execute_windows.go:410 2025/07/22 21:26:57Z: EC2LaunchTelemetry: IpConflictDetectionCode=0 2025/07/22 21:26:57Z: Message: Windows is Ready to use {"type":"EC2AgentTelemetry","agentId":"WindowsLaunchAgentV2", ...} {"type":"EC2AgentTelemetry","agentId":"WindowsLaunchAgentV2", ...}
###### EC2Launch v2 console log messages The following is a list of all of the EC2Launch v2 console log messages.

Error EC2Launch service is stopping. {error message} Stopped service error details:
- Error setting up EC2Launch agent folders
- See instance logs for detail
- Error stopping service
- Error initializing service Windows sysprep configuration complete Invalid administrator username: {invalid username} Invalid administrator password Username: {username} Password: <Password>{encrypted password}</Password>
The following message is an information block that contains AMI details:
AMI Origin Version: {amiVersion} AMI Origin Name: {amiName} Microsoft Windows NT {currentVersion}.{currentBuildNumber} OsVersion: {currentVersion} OsProductName: {productName} OsBuildLabEx: {buildLabEx} OsCurrentBuild: {currentBuild} OsReleaseId: {releaseId} Language: {language} TimeZone: {timeZone} Offset: UTC {offset} Launch agent: EC2Launch {BuildVersion} AMI-ID: {amiId} Instance-ID: {instanceId} Instance Type: {instanceType} HOSTNAME: {computer name} RDPCERTIFICATE-SUBJECTNAME: {certificate subject name} RDPCERTIFICATE-THUMBPRINT: {thumbprint hash} SqlServerBilling: {sql billing}

SqlServerInstall: {sql patch leve, edition type} Driver: AWS NVMe Driver {version} Driver: Inbox NVMe Driver {version} Driver: AWS PV Driver Package {version} Microsoft-Hyper-V is installed.
Unable to get service status for vmms Microsoft-Hyper-V is {status} SSM: Amazon SSM Agent {version} AWS VSS Version: {version} Windows sysprep configuration complete.
Windows is being configured. 'SysprepState is {state}'
Windows is still being configured. 'SysprepState is {state}'
Windows is Ready to use Waiting for access to metadata...
Meta-data is now available.
Metadata is not available for this instance.
Timed out waiting for access to metadata.
User data format: {format} EC2Launch v2 telemetry messages include the launch telemetry property values. Starting with version 2.2.63, EC2 agent telemetry data is formatted as a JSON object.
EC2LaunchTelemetry: {telemetry property} {"type":"EC2AgentTelemetry","agentId":"WindowsLaunchAgentV2" ... }
#### EC2Launch v2 version histories Version histories
- EC2Launch v2 version history
##### EC2Launch v2 version history To ensure that you have the latest launch agent installed, see Install the latest version of EC2Launch v2. You can receive notifications when new versions of the EC2Launch v2 agent are released. For more information, see Subscribe to EC2 Windows launch agent notifications.
The following table describes the released versions of EC2Launch v2.

Version Details Release date 2.3.108
- Added IPv6 address display to wallpaper. For Memory and Network attributes, consult   AWS Documentation.
December 29, 2025 2.3.56
- Fixed an issue where preconfigured persistent network routes  were not handled properly by EC2Launch v2.
November 4, 2025 2.3.5
- Improved primary network interface detection using  IMDS when adding routes.
September 15, 2025 2.2.63
- Updated launch agent to improve Telemetry.
July 29, 2025 2.1.1
- Added full support for IPv6.
May 14, 2025 2.0.2107
- Enhanced route addition to handle scenarios when IPv4 or IPv6 addresses are not available on the interface.
March 27, 2025 2.0.2081
- Fixed an issue where RDP certificate information was not properly retrieved or validated. Added functionality to automatically start the Remote Desktop Services if  needed.
- Adjusted EC2Launch v2 service permissions to fix an issue that  occurs when querying the service status.
February 4, 2025 2.0.2046
- Updated the wallpaper path in the   agent-config.yml file to use the  default operating system wallpaper path.
- Added telemetry to monitor the locations where agent  er rors occurred.
- Updated agent log messaging.
October 3, 2024

Version Details Release date 2.0.1981
- Updated EC2Launch.exe  CLI command  error messages for non-Administrator users.
August 6, 2024 2.0.1948
- Added telemetry to monitor usage of admin password options.
- Modified EC2Launch permissions.
July 1, 2024 2.0.1924
- Updated the EC2Launch Settings UI.
- Updated the wallpaper CLI command.
- Updated the EC2Launch installer.
June 10, 2024 2.0.1914
- Add routes with unspecified gateway addresses  (0.0.0.0 for IPv4 or :: for  IPv6).
- Always add both IPv4 and IPv6 routes.
- Fixed an issue where the Administrator   username was added to the   agent-config.yml  file when it  wasn't specified.
- Modified EC2Launch v2 permissions.
June 5, 2024

Version Details Release date 2.0.1881
- Added an encrypted password option to   setAdminA ccount  task.
- Added CLI command to encrypt static password in  agent- config.yml.
- Fixed an issue where XML user data doesn't add PowerShell arguments when it runs with Administrator permissions. For more details, see How Amazon EC2 handles user data for Windows instances.
- Adjusted PowerShell arguments for the   executeScript task and user data scripts  when they run with LocalSyst em  permissions.  When arguments are empty, the agent uses the following  default value: -ExecutionPolicy Unrestricted .
- Prevented printing duplicate driver versions to the  console log.
May 8, 2024 2.0.1815
- Adjusted error handling to fail on critical setup issues  before sysprep.
- Fixed an issue where wallpaper and hostname tasks could  us e an incorrect IP address on instances with multiple IP  addre sses assigned to the primary network interface.
- Wallpaper and hostname tasks changed to get private IP from IMDS first, then fail back to WMI if IMDS is  disabled.
- Fixed an issue with the initializeVolume  task  where sc1 volumes failed to initialize due to a  transient error.
March 6, 2024

Version Details Release date 2.0.1739
- Fixed an issue that prevented exit codes from being  ca ptured by executeScript  tasks that were run  as the Windows Administrator user.
January 17, 2024 2.0.1702
- Restricted Telemetry.log  permissions  to read-exec ute  only for standard users.
- Configured the EC2Launch Windows service to restart on start-up failure.
- Made add-routes  failures actionable by  logging route.exe   stderr output.
- Fixed an issue that occurs when route metrics are outside  of the range [1, 9999].
- Added wallpaper support to several new instance   types.
- Fixed an issue caused by user data scripts that run as the Windows Administrator user and send output to   stderr.
January 4, 2024

Version Details Release date 2.0.1643
- Updated the ebsnvme-id.exe  tool to  version 1.1.0.7.
- Fixed an issue with receive side scaling (RSS) and receive queue depth settings on metal instance types that begin with  'metal-*', such as metal-48x1.
- Removed telemetry event that reports on XML userdata commands that block the agent.
- Updated setDnsSuffix  task to limit domain  n ame devolution based on registry entry:   HKEY_LOCA L_MACHINE\System\CurrentControlSet\S ervices\Dnscache\Parameters\DomainNa meDevolutionLevel .
- Added a public task and CLI that adds network  routes.
- Note – This is the  last version to officially support Windows Server  2012.
- Note – This is the  last version to officially support 32-bit operating  systems.
October 4, 2023 2.0.1580
- Changed the way that the launch agent handles errors when you modify log file permissions.
- Added a timeout for connecting to the serial port. The  time out allows the launch agent to continue running if the  serial port is in use.
September 5, 2023

Version Details Release date 2.0.1521
- Deprecated the —block flag of the   EC2Launch.exe   reset and sysprep  commands.
- Updated EC2Launch.exe  to detect and  handle the reset and   sysprep commands that are used in  inline executeSc ript  tasks. Those commands   cause the agent to stop running after the   executeScript  task runs them.
- Updated XML userdata scripts to run inline by  default.
- Enable XML userdata scripts to run detached with the new detach tag. For more details, see User data scripts.
- Made the following changes to the agent log.
- Updated agent log messages.
- Removed executeScript  content and  output from the agent log.
- Removed executeProgram  arguments and  output from the agent log.
- Made the following changes to the console log.
- Added   EnableSCSIPersistentReservations

 value to the console log.
July 3, 2023

Version Details Release date 2.0.1303
- Added additional error handling and log lines when adding network routes.
- Allowed executeScript  and   executeProgram  tasks in the PreReady   stage.
- Updated executeProgram  task to generate   output files similar to the output from the executeScript  task. For more information, see executeProgram.
- Added telemetry to monitor usage of blocking agent  co mmands in XML user data.
May 3, 2023 2.0.1245
- Improved visibility into crashes by logging crash call  stacks in clear text.
- Added the EventLog service as a startup dependency to fix  a crash when the Amazon EC2Launch service starts up faster  t han the EventLog service.
- Made XML user data run before PostReady stage from the agent config file (like EC2Launch v1 and EC2Config).
- Added YAML user data version 1.1 to make user data run before PostReady stage from the agent config file (YAML user  data version 1.0 runs after PostReady stage from the agent  config file).
March 8, 2023

Version Details Release date 2.0.1173
- Adds an optional feature to display instance tags on  wallp aper. For more information, see setWallpaper .
- Adds error handling when the security group for Elastic Graphics is not properly set up.
- Fixes a timeout when the Instance Metadata Service is not enabled.
February 6, 2023 2.0.1121
- Fixes an issue where a 404 error is printed to the  wallpaper when no public IPv4 address is assigned.
- Fixes an issue where the volume's file system is formatted  as RAW instead of NTFS when its  device's drive letter is set to D.
- Fixes an issue where NVMe SSD volumes are incorrectly identified as EBS volumes.
- Fixes an error when activating Windows when IMDS is  disab led.
January 4, 2023

Version Details Release date 2.0.1082
- Fixes an issue where the setWallpaper :   privateIp Address  field is blank when IMDS  is disabled.
- Fixes an issue with setting the hostname to the private  IPv4 address when IMDS is disabled.
- Fixes an issue with initializing volumes on Windows Server  2
012. - Fixes an issue with setting jumbo frames.
- Fixes an error when no SSH key is specified at instance launch.
- Fixes an error on Windows Server 2012 when Windows does not have a 'ReleaseId' registry key.
December 7, 2022 2.0.1011
- Fixes logic for finding network adapter when PnPDeviceID  is empty.
November 11, 2022 2.0.1009
- Uses PCI segment information to select the console  port.
November 8, 2022 2.0.982
- Adds retry logic to get RDP information.
- Fixes errors during volume initialization on   d2.8xlarge instances.
- Fixes issue where an incorrect network adapter can be  selec ted after a reboot.
- Removes false alarm error message when ACPI SPCR is unavailable.
October 31, 2022

Version Details Release date 2.0.863
- Updates IMDS wait logic to make only IMDSv2  requests.
- Adds logic to assign drive letter to volumes that are  already initialized but not mounted.
- Prints a more specific error message when key pair type is not supported.
- Fixes 3010 reboot code bug.
- Adds check for invalid base64-encoded user data.
July 6, 2022 2.0.698
- Fixes typo in log output when executing scripts.
January 30, 2022 2.0.674
- Telemetry uploads the enabled/disabled privacy  control.
- Fixes index out of bounds bug.
- Removes wallpaper shortcuts during   sysprep.
November 15, 2021 2.0.651
- Adds logic to uninstall legacy agents during EC2Launch v2 installation.
- Fixes list-volume  CLI issue when root volume  is not listed as volume 0.
October 7, 2021 2.0.592
- Fixes bug to correctly report stage status.
- Removes false alarm error messages when log files are  clos ed.
- Adds telemetry.
August 31, 2021

Version Details Release date 2.0.548
- Adds leading zeros for hex IP hostname.
- Fixes file permissions for enableOpenSsh   task.
- Fixes sysprep command crash.
August 4, 2021 2.0.470
- Fixes bug in network stage to wait for DHCP to assign an  IP to the instance.
- Fixes bug with setDnsSuffix  when   SearchList registry key does not  exist.
- Fixes bug in DNS devolution logic in   setDnsSuffix .
- Adds network routes after intermediate reboots.
- Allows initializeVolume  to re-letter existing   volumes.
- Removes extra information from version subcommand.
July 20, 2021 2.0.285
- Adds option to run user scripts in a detached   process.
- Legacy userdata (XML userdata) now runs in a detached process, which is similar behavior to the prior launch  agent.
- Adds CLI flag to the sysprep and   reset commands, which allows them to block  until the service stops.
- Restricts the config folder permissions.
March 8, 2021

Version Details Release date 2.0.207
- Adds optional hostName field to   setHostName  task.
- Fixes reboot bug. Reboot tasks executeScript   and executeProgram  will be marked as running.
- Adds more return codes to the status command.
- Adds bootstrap service to fix startup issue when running  on t2.nano instance type.
- Fixes clean installation mode to remove files not tracked  by installer.
February 2, 2021 2.0.160
- Fixes validate command to detect invalid  stage name.
- Adds w32tm resync command in   addroutes  task.
- Fixes issue with changing DNS suffix search order.
- Adds check conditions to better report invalid user  data.
December 4, 2020 2.0.153 Adds Sysprep functionality in UserData.
November 3, 2020

Version Details Release date 2.0.146
- Fixes issue with RootExtend on non-English AMIs.
- Grants users group write permission to log files.
- Creates MS Reserved partition for GPT volumes.
- Adds list-volumes command and volume dropdown in Amazon  EC2Launch settings.
- Adds get-agent-config command for printing   agent-co nfig.yml file in yaml or json format.
- Erases static password if no public key detected.
October 6, 2020 2.0.124
- Adds option to display OS version on wallpaper.
- Initializes encrypted EBS volumes.
- Adds routes for VPCs with no local DNS name.
September 10, 2020 2.0.104
- Creates DNS suffix search list if it does not exist.
- Skips Hibernation if not requested.
August 12, 2020 2.0.0 Initial release.
June 30, 2020
### Use the EC2Launch v1 agent to perform tasks during EC2 Windows instance launch launch Amazon managed AMIs for Windows Server 2016 and 2019 include a set of Windows Powershell scripts called EC2Launch. EC2Launch performs tasks during the initial instance boot. For information about the EC2Launch versions that are included in AWS Windows AMIs, see the AWS Windows AMI Reference.

Note The latest launch agent for Windows Server 2016 and later operating system versions is EC2Launch v2, which replaces both EC2Config and EC2Launch, and comes pre-installed on AWS Windows Server 2016 and 2019 AMIs with names that begin with EC2LaunchV2- Windows_Server-*. You can also manually install and configure the agent on Windows Server 2016 and 2019. For more information, see Install EC2Launch v2.
To use EC2Launch with IMDSv2, the version must be 1.3.2002730 or later.
You can use the following Windows PowerShell command to verify the installed version of EC2Launch.
Test-ModuleManifest -Path "C:\ProgramData\Amazon\EC2-Windows\Launch\Module \Ec2Launch.psd1" | Select Version
#### EC2Launch tasks EC2Launch performs the following tasks by default during the initial instance boot:
- Sets up new wallpaper that renders information about the instance.
- Sets the computer name to the private IPv4 address of the instance.
- Sends instance information to the Amazon EC2 console.
- Sends the RDP certificate thumbprint to the EC2 console.
- Sets a random password for the administrator account.
- Adds DNS suffixes.
- Dynamically extends the operating system partition to include any unpartitioned space.
- Executes user data (if specified). For more information about specifying user data, see Run commands when you launch an EC2 instance with user data input.
- Sets persistent static routes to reach the metadata service and AWS KMS servers.
Important If a custom AMI is created from this instance, these routes are captured as part of the OS configuration and any new instances launched from the AMI will retain the same routes,

regardless of subnet placement. In order to update the routes, see Update metadata/ KMS routes for Server 2016 and later when launching a custom AMI.
The following tasks help to maintain backward compatibility with the EC2Config service. You can also configure EC2Launch to perform these tasks during startup:
- Initialize secondary EBS volumes.
- Send Windows Event logs to the EC2 console logs.
- Send the Windows is ready to use message to the EC2 console.
#### EC2Launch directory structure EC2Launch is installed by default on Windows Server 2016 and later AMIs in the root directory C:
\ProgramData\Amazon\EC2-Windows\Launch.
Note By default, Windows hides files and folders under C:\ProgramData. To view EC2Launch directories and files, you must either type the path in Windows Explorer or change the folder properties to show hidden files and folders.
The Launch directory contains the following subdirectories.
- Scripts — Contains the PowerShell scripts that make up EC2Launch.
- Module — Contains the module for building scripts related to Amazon EC2.
- Config — Contains script configuration files that you can customize.
- Sysprep — Contains Sysprep resources.
- Settings — Contains an application for the Sysprep graphical user interface.
- Library — Contains shared libraries for EC2 launch agents.
- Log — Contains subdirectories for scripts and the log files that are generated by the scripts.

Telemetry Telemetry is additional information that helps AWS to better understand your requirements, diagnose issues, and deliver features to improve your experience with AWS services.
EC2Launch version 1.3.2003498 and later collect telemetry, such as usage metrics and errors.
This data is collected from the Amazon EC2 instance on which EC2Launch runs. This includes all Windows AMIs owned by AWS.
The following types of telemetry are collected by EC2Launch:
- Usage information — agent commands, install method, and scheduled run frequency.
- Errors and diagnostic information — agent installation and run error codes.
Examples of collected data:
2021/07/15 21:44:12Z: EC2LaunchTelemetry: IsAgentScheduledPerBoot=true 2021/07/15 21:44:12Z: EC2LaunchTelemetry: IsUserDataScheduledPerBoot=true 2021/07/15 21:44:12Z: EC2LaunchTelemetry: AgentCommandCode=1 2021/07/15 21:44:12Z: EC2LaunchTelemetry: AgentCommandErrorCode=5 2021/07/15 21:44:12Z: EC2LaunchTelemetry: AgentInstallCode=2 2021/07/15 21:44:12Z: EC2LaunchTelemetry: AgentInstallErrorCode=0 Telemetry is enabled by default. You can disable telemetry collection at any time. If telemetry is enabled, EC2Launch sends telemetry data without additional customer notifications.
Your choice to enable or disable telemetry is collected.
You can opt in or out of telemetry collection. Your selection to opt in or out of telemetry is collected to ensure that we adhere to your telemetry option.
Telemetry visibility When telemetry is enabled, it appears in the Amazon EC2 console output as follows:
2021/07/15 21:44:12Z: Telemetry: <Data>
Disable telemetry on an instance To disable telemetry by setting a system environment variable, run the following command as an administrator:

setx /M EC2LAUNCH_TELEMETRY 0 To disable telemetry during installation, run install.ps1 as follows:
. .\install.ps1 -EnableTelemetry:$false More topics for EC2Launch
- Install the latest version of EC2Launch
- Configure the EC2Launch v1 agent on your Windows instance
- EC2Launch version history
#### Install the latest version of EC2Launch Use the following procedure to download and install the latest version of EC2Launch on your instances.
To download and install the latest version of EC2Launch
1. If you have already installed and configured EC2Launch on an instance, make a backup of the EC2Launch configuration file. The installation process does not preserve changes in this file. By default, the file is located in the C:\ProgramData\Amazon\EC2-Windows\Launch\Config directory.
2. Download EC2-Windows-Launch.zip to a directory on the instance.
3. Download install.ps1 to the same directory where you downloaded EC2-Windows- Launch.zip.
4. Run install.ps1
5. If you made a backup of the EC2Launch configuration file, copy it to the C:\ProgramData \Amazon\EC2-Windows\Launch\Config directory.
To download and install the latest version of EC2Launch using PowerShell If you have already installed and configured EC2Launch on an instance, make a backup of the EC2Launch configuration file. The installation process does not preserve changes in this file. By default, the file is located in the C:\ProgramData\Amazon\EC2-Windows\Launch\Config directory.

To install the latest version of EC2Launch using PowerShell, run the following commands from a PowerShell window as an administrator: mkdir $env:USERPROFILE\Desktop\EC2Launch $Url = "https://s3.amazonaws.com/ec2-downloads-windows/EC2Launch/latest/EC2-Windows- Launch.zip"
$DownloadZipFile = "$env:USERPROFILE\Desktop\EC2Launch\" + $(Split-Path -Path $Url - Leaf)
Invoke-WebRequest -Uri $Url -OutFile $DownloadZipFile $Url = "https://s3.amazonaws.com/ec2-downloads-windows/EC2Launch/latest/install.ps1"
$DownloadZipFile = "$env:USERPROFILE\Desktop\EC2Launch\" + $(Split-Path -Path $Url - Leaf)
Invoke-WebRequest -Uri $Url -OutFile $DownloadZipFile & $env:USERPROFILE\Desktop\EC2Launch\install.ps1 Note If you receive an error when downloading the file, and you are using Windows Server 2016, TLS 1.2 might need to be enabled for your PowerShell terminal. You can enable TLS 1.2 for the current PowerShell session with the following command and then try again:
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12 Verify the installation by checking the launch agent. Run the following commands from a PowerShell window as an administrator:
Import-Module C:\ProgramData\Amazon\EC2-Windows\Launch\Module\Ec2Launch.psm1 Import-LocalizedData -BaseDirectory C:\ProgramData\Amazon\EC2-Windows\Launch\Module\ - FileName 'Ec2Launch.psd1' -BindingVariable moduleManifest $moduleManifest.Get_Item('ModuleVersion')
#### Configure the EC2Launch v1 agent on your Windows instance After your instance has been initialized the first time, you can configure EC2Launch to run again and perform different start-up tasks.
Tasks
- Configure initialization tasks

- Schedule EC2Launch to run on every boot
- Initialize drives and map drive letters
- Send Windows event logs to the EC2 console
- Send Windows is ready message after a successful boot
##### Configure initialization tasks Specify settings in the LaunchConfig.json file to enable or disable the following initialization tasks:
- Set the computer name to the instance private IPv4 address.
- Set the monitor to always stay on.
- Set up new wallpaper.
- Add DNS suffix list.
Note This adds a DNS suffix lookup for the following domain and configures other standard suffixes. For more information about how launch agents set DNS suffixes, see Configure DNS Suffix for EC2 Windows launch agents. region.ec2-utilities.amazonaws.com
- Extend the boot volume size.
- Set the administrator password.
To configure initialization settings
1. On the instance to configure, open the following file in a text editor: C:\ProgramData \Amazon\EC2-Windows\Launch\Config\LaunchConfig.json.
2. Update the following settings as needed and save your changes. Provide a password in adminPassword only if adminPasswordtype is Specify.
{ "setComputerName": false,

 "setMonitorAlwaysOn": true, "setWallpaper": true, "addDnsSuffixList": true, "extendBootVolumeSize": true, "handleUserData": true, "adminPasswordType": "Random | Specify | DoNothing", "adminPassword": "password that adheres to your security policy (optional)"
} The password types are defined as follows:
Random EC2Launch generates a password and encrypts it using the user's key. The system disables this setting after the instance is launched so that this password persists if the instance is rebooted or stopped and started.
Specify EC2Launch uses the password you specify in adminPassword. If the password does not meet the system requirements, EC2Launch generates a random password instead. The password is stored in LaunchConfig.json as clear text and is deleted after Sysprep sets the administrator password. EC2Launch encrypts the password using the user's key.
DoNothing EC2Launch uses the password you specify in the unattend.xml file. If you don't specify a password in unattend.xml, the administrator account is disabled.
3. In Windows PowerShell, run the following command to schedule the script to run as a Windows Scheduled Task. The script runs one time during the next boot and then disables these tasks from running again.
C:\ProgramData\Amazon\EC2-Windows\Launch\Scripts\InitializeInstance.ps1 -Schedule
##### Schedule EC2Launch to run on every boot You can schedule EC2Launch to run on every boot instead of only the initial boot.
To enable EC2Launch to run on every boot:
1. Open Windows PowerShell and run the following command:

C:\ProgramData\Amazon\EC2-Windows\Launch\Scripts\InitializeInstance.ps1 - SchedulePerBoot
2. Or, run the executable with the following command:
C:\ProgramData\Amazon\EC2-Windows\Launch\Settings\Ec2LaunchSettings.exe Then select Run EC2Launch on every boot. You can specify that your EC2 instance Shutdown without Sysprep or Shutdown with Sysprep.
Note When you enable EC2Launch to run on every boot, the following happens the next time EC2Launch runs:
- If AdminPasswordType is still set to Random, EC2Launch will generate a new password at the next boot. After that boot, AdminPasswordType is automatically set to DoNothing to prevent EC2Launch from generating new passwords on subsequent boots.
To prevent EC2Launch from generating a new password on the first boot, manually set AdminPasswordType to DoNothing before you reboot.
- HandleUserData will be set back to false unless the user data has persist set to true. For more information, see the section called "User data scripts".
##### Initialize drives and map drive letters Specify settings in the DriveLetterMappingConfig.json file to map drive letters to volumes on your EC2 instance. The script initializes drives that are not already initialized and partitioned.
For more information about getting volume details in Windows, see Get-Volume in the Microsoft documentation.
To map drive letters to volumes
1. Open the C:\ProgramData\Amazon\EC2-Windows\Launch\Config \DriveLetterMappingConfig.json file in a text editor.
2. Specify the following volume settings and save your changes:

{ "driveLetterMapping": [ { "volumeName": "sample volume", "driveLetter": "H"
  } ]
}
3. Open Windows PowerShell and use the following command to run the EC2Launch script that initializes the disks:
C:\ProgramData\Amazon\EC2-Windows\Launch\Scripts\InitializeDisks.ps1 To initialize the disks each time the instance boots, add the -Schedule flag as follows:
C:\ProgramData\Amazon\EC2-Windows\Launch\Scripts\InitializeDisks.ps1 -Schedule
##### Send Windows event logs to the EC2 console Specify settings in the EventLogConfig.json file to send Windows Event logs to EC2 console logs.
To configure settings to send Windows Event logs
1. On the instance, open the C:\ProgramData\Amazon\EC2-Windows\Launch\Config \EventLogConfig.json file in a text editor.
2. Configure the following log settings and save your changes:
{ "events": [ { "logName": "System", "source": "An event source (optional)", "level": "Error | Warning | Information", "numEntries": 3 } ]
}

3. In Windows PowerShell, run the following command so that the system schedules the script to run as a Windows Scheduled Task each time the instance boots.
C:\ProgramData\Amazon\EC2-Windows\Launch\Scripts\SendEventLogs.ps1 -Schedule The logs can take three minutes or more to appear in the EC2 console logs.
##### Send Windows is ready message after a successful boot The EC2Config service sent the "Windows is ready" message to the EC2 console after every boot.
EC2Launch sends this message only after the initial boot. For backwards compatibility with the EC2Config service, you can schedule EC2Launch to send this message after every boot. On the instance, open Windows PowerShell and run the following command. The system schedules the script to run as a Windows Scheduled Task.
C:\ProgramData\Amazon\EC2-Windows\Launch\Scripts\SendWindowsIsReady.ps1 -Schedule
#### EC2Launch version history Important Beginning January 1, 2025, only the last two versions are supported. When a new version is released, the oldest previously supported version will automatically be marked private and will no longer be available for download.
To download and install the latest version of EC2Launch, see Install the latest version of EC2Launch.
You can receive notifications when new versions of the EC2Launch agent are released. For more information, see Subscribe to EC2 Windows launch agent notifications.
The following EC2Launch agent versions are supported and are available for download.
Version Details Release date 1.4.183
- Updated installer logic to prevent unsupported installation on Windows Server 2022.
4 February 2026

Version Details Release date
- Updated to print EC2WinUtil driver version to instance console log.
1.4.6
- Updated agent log messaging.
13 October 2025 The following prior versions of EC2Launch are no longer available for download.
Version Details Release date 1.3.2005119
- Fixed an issue where Invoke-Userdata  would  fail when called without any parameters.
11 February 2025 1.3.2005065
- Fixed an issue where RDP certificate information was not properly retrieved or validated. Added functionality to automatically start the Remote Desktop Services if  needed.
22 October 2024 1.3.2005008
- Updated Set-Wallpaper  to fall back to a solid  color background if the default wallpaper image is not  found.
6 August 2024 1.3.2004959
- Updated installer logic to prevent unsupported  installation on Windows Server 2025 or later.
2 July 2024 1.3.2004891
- Fixed an issue where HandleUserData  was not  set to false as expected.
- Added an Encrypted  password option to   LaunchCon fig.json .
- Changed Settings UI behavior to encrypt the  user specified password by default.
- 31 May 2024

Version Details Release date Added SetAdminPasswordConfig.ps1 to  convert the Specify password option to the   Encrypted  password option in the agent  configuration file.
1.3.2004617
- Fixed an error when setting the wallpaper.
15 January 2024 1.3.2004592
- Updated access permissions set by install.ps1 for %ProgramData%\Amazon\EC2-Windows\Launch .
- Restricted EC2Launch folder/file access to read-execute  only for standard user accounts.
- Changed the agent to stop waiting for the Instance Metadata Service (IMDS) to initialize if IMDS is not enabled for the instance.
- Added a five minute timeout when waiting for the IMDS to initialize.
- Changed the agent to write telemetry to the instance console log before the Windows is Ready message instead of after.
- Added wallpaper support to several new instance   types.
For more information about access permissions and user account  permissions of EC2Launch directories, see the section called "EC2Launch directory structure".
2 January 2024 1.3.2004491
- Added telemetry to monitor usage of the Specify   admin password option.
9 November 2023

Version Details Release date 1.3.2004462
- Added flush after every write to the serial  console.
18 October 2023 1.3.2004438
- Limit domain name devolution based on registry entry:
  HKEY_LOCAL_MACHINE\System\CurrentCon trolSet\Services\Dnscache\Parameters \DomainNameDevolutionLevel .
- Limited UserdataExecution.log permissions to Administrators  only.
- Added error messages in the Windows Event Log when log initialization fails.
4 October 2023 1.3.2004256
- Added EnableSCSIPersistentReservations value to console log.
- Added retry capability for   Get-ConsolePort.
7 July 2023 1.3.2004052
- Fixed an error that occurred when no SSH key is specified  at instance launch.
- Updated to retry starting the AmazonSSMAgent Windows service on failure.
- Updated to fail SysprepInstance.ps1 if BeforeSysprep.cmd fails with a non-zero exit code.
8 March 2023 1.3.2003975
- Fixed issue impacting Packer AMI builds where   SysprepIn stance.ps1 returns a   $LastErrorCode  of 1.
24 December 2022

Version Details Release date 1.3.2003961
- Fixed issue where explicitly specified administrator  pas swords are overwritten with a random password on  fast- launched instances.
- Fixed issue where SSM Agent fails to start on smaller instance types.
- Fixed an issue where the instance console log contains RDPCERTIFICATE-THUMBPRINT:   0000000 0000000000000000 instead of a valid RDP  certificate thumbprint value.
6 December 2022 1.3.2003923
- Fixes logic for finding network adapter when PnPDeviceID  is empty.
9 November 2022 1.3.2003919
- Updated Get-ConsolePort to use PCI segment  information.
- Fixed issue where an incorrect network adapter can be  selec ted after reboot.
- Fixed start-SSM-Agent timeout logic.
- Fixed backwards compatibility for Send-AdminCredentials function alias.
8 November 2022 1.3.2003857
- Prioritizes adapters with a default gateway when the  prim ary network adapter is selected.
- Extended in-memory password encryption.
3 October 2022

Version Details Release date 1.3.2003824
- Fixed error during setComputerName .
- Added logic to skip Windows activation when a BYOL billing code is detected.
- Added in-memory password encryption.
- Fixed error during volume initialization on   m6id.4xlarge .
30 August 2022 1.3.2003691
- Updated IMDS wait logic to make only IMDSv2  requests.
- Fixed bug impacting eGPU installation.
21 June 2022 1.3.2003639
- Added network-adapter wait logic to prevent use before  i nitialization.
- Fixed minor issues.
10 May 2022 1.3.2003498
- Added telemetry.
- Added shortcut to Settings UI.
- Formatted PowerShell scripts.
- Fixed issue with shutdown occurring before  BeforeSysp rep.cmd completes.
31 January 2022 1.3.2003411 Changed password generation logic to exclude passwords with low  complexity.
04 August 2021 1.3.2003364 Updated Install-EgpuManager with IMDSv2 support.
07 June 2021

Version Details Release date 1.3.2003312
- Added log lines before and after   setMonitorAlwaysOn setting.
- Added AWS Nitro Enclaves package version to console  log.
04 May 2021 1.3.2003284 Improved permission model by updating location for storing user data  to LocalAppData .
23 March 2021 1.3.2003236
- Updated method for setting user password in   Set-Admin Account  and   Randomize-LocalAdminPassword .
- FixedInitializeDisks  to check whether disk is  set to read only before setting it to writable.
11 February 2021 1.3.2003210 Localization fix for install.ps1 .
7 January 2021 1.3.2003205 Security fix for install.ps1  to update permissions on   %ProgramData%AmazonEC2-WindowsLaunch ModuleScripts directory.
28 December 2020 1.3.2003189 Added w32tm resync after adding routes.
4 December 2020 1.3.2003155 Updated instance type information.
25 August 2020 1.3.2003150 Added OsCurrentBuild  and OsReleaseId  to  console output .
22 April 2020 1.3.2003040 Fixed IMDS version 1 fallback logic.
7 April 2020 1.3.2002730 Added support for IMDS V2.
3 March 2020

Version Details Release date 1.3.2002240 Fixed minor issues.
31 October 2019 1.3.2001660 Fixed automatic login issue for users without password after first  time executing Sysprep.
2 July 2019 1.3.2001360 Fixed minor issues.
27 March 2019 1.3.2001220 All PowerShell scripts signed.
28 February 2019 1.3.2001200 Fixed issue with InitializeDisks.ps1 where running the script on a node in a Windows Server Failover Cluster would format drives on remote  nodes whose drive letter matched the local drive letter.
27 February 2019 1.3.2001160 Fixed missing wallpaper in Windows 2019.
22 February 2019 1.3.2001040
- Added plugin for setting the monitor to never turn off to  fix ACPI issues.
- SQL Server edition and version written to console.
21 January 2019 1.3.2000930 Fix for adding routes to metadata on ipv6-enabled ENIs.
2 January 2019 1.3.2000760
- Added default configuration for RSS and Receive Queue  se ttings for ENA devices.
- Disabled hibernation during Sysprep.
5 December 2018

Version Details Release date 1.3.2000630
- Added route 169.254.169.253/32 for DNS server.
- Added filter of setting Admin user.
- Improvements made to instance hibernation.
- Added option to schedule EC2Launch to run on every  boot.
9 November 2018 1.3.20004 30.0
- Added route 169.254.169.123/32 to AMZN time  service.
- Added route 169.254.169.249/32 to GRID license  service.
- Added timeout of 25 seconds when attempting to start  Sy stems Manager.
19 September 2018 1.3.200039.0
- Fixed improper drive lettering for EBS NVME  volumes.
- Added additional logging for NVME driver versions.
15 August 2018 1.3.2000080 Fixed minor issues.

1.3.610 Fixed issue with redirecting output and errors to files from user  data.

1.3.590
- Added missing instances types in the wallpaper.
- Fixed an issue with drive letter mapping and disk  installation .


Version Details Release date 1.3.580
- Fixed Get-Metadata  to use the default system  proxy settings for web requests.
- Added a special case for NVMe in disk  initialization.
- Fixed minor issues.

1.3.550 Added a -NoShutdown  option to enable Sysprep with no shutdown.

1.3.540 Fixed minor issues.

1.3.530 Fixed minor issues.

1.3.521 Fixed minor issues.

1.3.0
- Fixed a hexadecimal length issue for computer name  cha nge.
- Fixed a possible reboot loop for computer name  change.
- Fixed an issue in wallpaper setup.

1.2.0
- Update to display information about installed operating system (OS) in EC2 system log.
- Update to display EC2Launch and SSM Agent version in EC2 system log.
- Fixed minor issues.


Version Details Release date 1.1.2
- Update to display ENA driver information in EC2 system  log.
- Update to exclude Hyper-V from primary NIC filter  logic.
- Added AWS KMS server and port into registry key for KMS activation.
- Improved wallpaper setup for multiple users.
- Update to clear routes from persistent store.
- Update to remove the z from availability zone in DNS  suffix list.
- Update to address an issue with the  <runAsLocalSystem> tag in user data.

1.1.1 Initial release.

### Use the EC2Config service to perform tasks during EC2 legacy Windows operating system instance launch system instance launch Note EC2Config has reached the end of support. The operating system versions that it runs on are no longer supported by Microsoft. We strongly recommend that you upgrade to the latest launch agent.
The latest launch agent for Windows Server 2022 and later operating system versions is EC2Launch v2, which replaces both EC2Config and EC2Launch, and comes pre-installed on AWS Windows Server 2022 and 2025 AMIs. You can also manually install and configure the agent on Windows Server 2016 and 2019. For more information, see Install EC2Launch v2.

Windows AMIs for Windows Server versions prior to Windows Server 2016 include an optional service, the EC2Config service (EC2Config.exe). EC2Config starts when the instance boots and performs tasks during startup and each time you stop or start the instance. EC2Config can also perform tasks on demand. Some of these tasks are automatically enabled, while others must be enabled manually. Although optional, this service provides access to advanced features that aren't otherwise available. This service runs in the LocalSystem account.
The EC2Config service runs Sysprep, a Microsoft tool that enables you to create a customized Windows AMI that can be reused. When EC2Config calls Sysprep, it uses the files in %ProgramFiles%\Amazon\EC2ConfigService\Settings to determine which operations to perform. You can edit these files indirectly using the EC2 Service Properties system dialog, or directly using an XML editor or a text editor. However, there are some advanced settings that aren't available in the Ec2 Service Properties system dialog, so you must edit those entries directly.
If you create an AMI from an instance after updating its settings, the new settings are applied to any instance that's launched from the new AMI. For information about creating an AMI, see Create an Amazon EBS-backed AMI.
EC2Config uses settings files to control its operation. You can update these settings files using either a graphical tool or by directly editing XML files. The service binaries and additional files are contained in the %ProgramFiles%\Amazon\EC2ConfigService directory.
Contents
- EC2Config and AWS Systems Manager
- EC2Config tasks
- EC2Config settings files
- Install the latest version of EC2Config
- Configure .NET proxy settings for the EC2Config service
- Set EC2Config service properties from the system dialog on your EC2 Windows instance
- Troubleshoot issues with the EC2Config launch agent
- EC2Config version history
#### EC2Config and AWS Systems Manager The EC2Config service processes Systems Manager requests on instances created from AMIs for versions of Windows Server prior to Windows Server 2016 that were published before November
2016. Instances created from AMIs for versions of Windows Server prior to Windows Server 2016 that were published after November 2016 include the EC2Config service and SSM Agent. EC2Config performs all of the tasks described earlier, and SSM Agent processes requests for Systems Manager capabilities like Run Command and State Manager.
You can use Run Command to upgrade your existing instances to use to the latest version of the EC2Config service and SSM Agent. For more information, see Update SSM Agent using Run Command in the AWS Systems Manager User Guide.
#### EC2Config tasks EC2Config runs initial startup tasks when the instance is first started and then disables them. To run these tasks again, you must explicitly enable them prior to shutting down the instance, or by running Sysprep manually. These tasks are as follows:
- Set a random, encrypted password for the administrator account.
- Generate and install the host certificate used for Remote Desktop Connection.
- Dynamically extend the operating system partition to include any unpartitioned space.
- Execute the specified user data (and Cloud-Init, if it's installed). For more information about specifying user data, see Run commands when you launch an EC2 instance with user data input.
EC2Config performs the following tasks every time the instance starts:
- Change the host name to match the private IP address in Hex notation (this task is disabled by default and must be enabled in order to run at instance start).
- Configure the key management server (AWS KMS), check for Windows activation status, and activate Windows as necessary.
- Mount all Amazon EBS volumes and instance store volumes, and map volume names to drive letters.
- Write event log entries to the console to help with troubleshooting (this task is disabled by default and must be enabled in order to run at instance start).
- Write to the console that Windows is ready.
- Add a custom route to the primary network adapter to enable the following IP addresses when a single NIC or multiple NICs are attached: 169.254.169.250, 169.254.169.251, and 169.254.169.254. These addresses are used by Windows Activation and when you access instance metadata.

Note If the Windows OS is configured to use IPv4, these IPv4 link-local addresses can be used.
If the Windows OS has the IPv4 network protocol stack disabled and uses IPv6 instead, add [fd00:ec2::250] in place of 169.254.169.250 and 169.254.169.251. Then add [fd00:ec2::254] in place of 169.254.169.254.
EC2Config performs the following task every time a user logs in:
- Display wallpaper information to the desktop background.
While the instance is running, you can request that EC2Config perform the following task on demand:
- Run Sysprep and shut down the instance so that you can create an AMI from it. For more information, see Create an Amazon EC2 AMI using Windows Sysprep.
#### EC2Config settings files The settings files control the operation of the EC2Config service. These files are located in the C:
\Program Files\Amazon\Ec2ConfigService\Settings directory:
- ActivationSettings.xml—Controls product activation using a key management server (AWS KMS).
- AWS.EC2.Windows.CloudWatch.json—Controls which performance counters to send to CloudWatch and which logs to send to CloudWatch Logs.
- BundleConfig.xml—Controls how EC2Config prepares an instance store-backed instance for AMI creation.
- Config.xml—Controls the primary settings.
- DriveLetterConfig.xml—Controls drive letter mappings.
- EventLogConfig.xml—Controls the event log information that's displayed on the console while the instance is booting.
- WallpaperSettings.xml—Controls the information that's displayed on the desktop background.

ActivationSettings.xml This file contains settings that control product activation. When Windows boots, the EC2Config service checks whether Windows is already activated. If Windows is not already activated, it attempts to activate Windows by searching for the specified AWS KMS server.
- SetAutodiscover—Indicates whether to detect a AWS KMS automatically.
- TargetKMSServer—Stores the private IP address of a AWS KMS. The AWS KMS must be in the same Region as your instance.
- DiscoverFromZone—Discovers the AWS KMS server from the specified DNS zone.
- ReadFromUserData—Gets the AWS KMS server from UserData.
- LegacySearchZones—Discovers the AWS KMS server from the specified DNS zone.
- DoActivate—Attempts activation using the specified settings in the section. This value can be true or false.
- LogResultToConsole—Displays the result to the console.
BundleConfig.xml This file contains settings that control how EC2Config prepares an instance for AMI creation.
- AutoSysprep—Indicates whether to use Sysprep automatically. Change the value to Yes to use Sysprep.
- SetRDPCertificate—Sets a self-signed certificate to the Remote Desktop server. This enables you to securely RDP into the instances. Change the value to Yes if the new instances should have the certificate.
This setting is not used for instances with operating system versions prior to Windows Server 2016, because they can generate their own certificates.
- SetPasswordAfterSysprep—Sets a random password on a newly launched instance, encrypts it with the user launch key, and outputs the encrypted password to the console. Change the value of this setting to No if the new instances should not be set to a random encrypted password.
Config.xml Plug-ins

- Ec2SetPassword—Generates a random encrypted password each time you launch an instance.
This feature is disabled by default after the first launch so that reboots of this instance don't change a password set by the user. Change this setting to Enabled to continue to generate passwords each time you launch an instance.
This setting is important if you are planning to create an AMI from your instance.
- Ec2SetComputerName—Sets the host name of the instance to a unique name based on the IP address of the instance and reboots the instance. To set your own host name, or prevent your existing host name from being modified, you must disable this setting.
- Ec2InitializeDrives—Initializes and formats all volumes during startup. This feature is enabled by default.
- Ec2EventLog—Displays event log entries in the console. By default, the three most recent error entries from the system event log are displayed. To specify the event log entries to display, edit the EventLogConfig.xml file located in the EC2ConfigService\Settings directory. For information about the settings in this file, see Eventlog Key.
- Ec2ConfigureRDP—Sets up a self-signed certificate on the instance, so users can securely access the instance using Remote Desktop. This setting is not used for instances with operating system versions prior to Windows Server 2016, because they can generate their own certificates.
- Ec2OutputRDPCert—Displays the Remote Desktop certificate information to the console so that the user can verify it against the thumbprint.
- Ec2SetDriveLetter—Sets the drive letters of the mounted volumes based on user- defined settings. By default, when an Amazon EBS volume is attached to an instance, it can be mounted using the drive letter on the instance. To specify your drive letter mappings, edit the DriveLetterConfig.xml file located in the EC2ConfigService\Settings directory.
- Ec2WindowsActivate—The plug-in handles Windows activation. It checks to see if Windows is activated. If not, it updates the AWS KMS client settings, and then activates Windows.
To modify the AWS KMS settings, edit the ActivationSettings.xml file located in the EC2ConfigService\Settings directory.
- Ec2DynamicBootVolumeSize—Extends Disk 0/Volume 0 to include any unpartitioned space.
- Ec2HandleUserData—Creates and runs scripts created by the user on the first launch of an instance after Sysprep is run. Commands wrapped in script tags are saved to a batch file, and commands wrapped in PowerShell tags are saved to a .ps1 file (corresponds to the User Data checkbox on the Ec2 Service Properties system dialog).

- Ec2ElasticGpuSetup—Installs the Elastic GPU software package if the instance is associated with an elastic GPU.
- Ec2FeatureLogging—Sends Windows feature installation and corresponding service status to the console. Supported only for the Microsoft Hyper-V feature and corresponding vmms service.
Global Settings
- ManageShutdown—Ensures that instances launched from Amazon S3-backed AMIs do not terminate while running Sysprep.
- SetDnsSuffixList—Sets the DNS suffix of the network adapter for Amazon EC2. This allows DNS resolution of servers running in Amazon EC2 without providing the fully qualified domain name.
Note This adds a DNS suffix lookup for the following domain and configures other standard suffixes. For more information about how launch agents set DNS suffixes, see Configure DNS Suffix for EC2 Windows launch agents. region.ec2-utilities.amazonaws.com
- WaitForMetaDataAvailable—Ensures that the EC2Config service will wait for metadata to be accessible and the network available before continuing with the boot. This check ensures that EC2Config can obtain information from metadata for activation and other plug-ins.
- ShouldAddRoutes—Adds a custom route to the primary network adapter to enable the following IP addresses when multiple NICs are attached: 169.254.169.250, 169.254.169.251, and 169.254.169.254. These addresses are used by Windows Activation and when you access instance metadata.
- RemoveCredentialsfromSyspreponStartup—Removes the administrator password from Sysprep.xml the next time the service starts. To ensure that this password persists, edit this setting.
DriveLetterConfig.xml This file contains settings that control drive letter mappings. By default, a volume can be mapped to any available drive letter. You can mount a volume to a particular drive letter as follows.

<?xml version="1.0" standalone="yes"?>
<DriveLetterMapping>
  <Mapping>
    <VolumeName></VolumeName>
    <DriveLetter></DriveLetter>
  </Mapping>
  . . .
  <Mapping>
    <VolumeName></VolumeName>
    <DriveLetter></DriveLetter>
  </Mapping>
</DriveLetterMapping>
- VolumeName—The volume label. For example, My Volume. To specify a mapping for an instance storage volume, use the label Temporary Storage X, where X is a number from 0 to 25.
- DriveLetter—The drive letter. For example, M:. The mapping fails if the drive letter is already in use.
EventLogConfig.xml This file contains settings that control the event log information that's displayed on the console while the instance is booting. By default, we display the three most recent error entries from the System event log.
- Category—The event log key to monitor.
- ErrorType—The event type (for example, Error, Warning, Information.)
- NumEntries—The number of events stored for this category.
- LastMessageTime—To prevent the same message from being pushed repeatedly, the service updates this value every time it pushes a message.
- AppName—The event source or application that logged the event.
WallpaperSettings.xml This file contains settings that control the information that's displayed on the desktop background.
The following information is displayed by default.
- Hostname—Displays the computer name.

- Instance ID—Displays the ID of the instance.
- Public IP Address—Displays the public IP address of the instance.
- Private IP Address—Displays the private IP address of the instance.
- Availability Zone—Displays the Availability Zone in which the instance is running.
- Instance Size—Displays the type of instance.
- Architecture—Displays the setting of the PROCESSOR_ARCHITECTURE environment variable.
You can remove any of the information that's displayed by default by deleting its entry. You can add additional instance metadata to display as follows.
<WallpaperInformation>
  <name>display_name</name>
  <source>metadata</source>
  <identifier>meta-data/path</identifier>
</WallpaperInformation>
You can add additional System environment variables to display as follows.
<WallpaperInformation>
  <name>display_name</name>
  <source>EnvironmentVariable</source>
  <identifier>variable-name</identifier>
</WallpaperInformation>
InitializeDrivesSettings.xml This file contains settings that control how EC2Config initializes drives.
By default, EC2Config initialize drives that were not brought online with the operating system. You can customize the plugin as follows.
<InitializeDrivesSettings>
    <SettingsGroup>setting</SettingsGroup>
</InitializeDrivesSettings>
Use a settings group to specify how you want to initialize drives:

FormatWithTRIM Enables the TRIM command when formatting drives. After a drive has been formatted and initialized, the system restores TRIM configuration.
Starting with EC2Config version 3.18, the TRIM command is disabled during the disk format operation by default. This improves formatting times. Use this setting to enable TRIM during the disk format operation for EC2Config version 3.18 and later.
FormatWithoutTRIM Disables the TRIM command when formatting drives and improves formatting times in Windows. After a drive has been formatted and initialized, the system restores TRIM configuration.
DisableInitializeDrives Disables formatting for new drives. Use this setting to initialize drives manually.
#### Install the latest version of EC2Config Note The latest launch agent for Windows Server 2022 and later operating system versions is EC2Launch v2, which replaces both EC2Config and EC2Launch. EC2Launch v2 comes pre- installed on AWS Windows Server 2022 and 2025 AMIs. You can also manually install and configure the agent on Windows Server 2016 and 2019. For more information, see Install EC2Launch v2.
For information about how to receive notifications for EC2Config updates, see Subscribe to EC2 Windows launch agent notifications. For information about the changes in each version, see the EC2Config version history.
##### Before you begin
- Verify that you have .NET framework 3.5 SP1 or greater.
- By default, Setup replaces your settings files with default settings files during installation and restarts the EC2Config service when the installation is completed. If you changed EC2Config service settings, copy the config.xml file from the %Program Files%\Amazon

\Ec2ConfigService\Settings directory. After you update the EC2Config service, you can restore this file to retain your configuration changes.
##### Verify the EC2Config version Use the following procedure to verify the version of EC2Config that is installed on your instances.
To verify the installed version of EC2Config
1. Launch an instance from your AMI and connect to it.
2. In Control Panel, select Programs and Features.
3. In the list of installed programs, look for Ec2ConfigService. Its version number appears in the Version column.
##### Update EC2Config Use the following procedure to download and install the latest version of EC2Config on your instances.
To download and install the latest version of EC2Config
1. Download and unzip the EC2Config installer.
2. Run EC2Install.exe. For a complete list of options, run EC2Install with the /? option.
By default, setup displays prompts. To run the command with no prompts, use the /quiet option.
Important To keep the custom settings from the config.xml file that you saved, run EC2Install with the /norestart option, restore your settings, and then restart the EC2Config service manually.
3. If you are running EC2Config version 4.0 or later, you must restart SSM Agent on the instance from the Microsoft Services snap-in.

Note The updated EC2Config version information will not appear in the instance System Log or Trusted Advisor check until you reboot or stop and start your instance.
To download and install the latest version of EC2Config using PowerShell To download, unzip, and install the latest version of EC2Config using PowerShell, run the following commands from a PowerShell window:
$Url = "https://s3.amazonaws.com/ec2-downloads-windows/EC2Config/EC2Install.zip"
$DownloadZipFile = "$env:USERPROFILE\Desktop\" + $(Split-Path -Path $Url -Leaf)
$ExtractPath = "$env:USERPROFILE\Desktop\"
Invoke-WebRequest -Uri $Url -OutFile $DownloadZipFile $ExtractShell = New-Object -ComObject Shell.Application $ExtractFiles = $ExtractShell.Namespace($DownloadZipFile).Items()
$ExtractShell.NameSpace($ExtractPath).CopyHere($ExtractFiles)
Start-Process $ExtractPath Start-Process `
    -FilePath $env:USERPROFILE\Desktop\EC2Install.exe `
    -ArgumentList "/S"
Note If you receive an error when downloading the file, and you are using Windows Server 2016 or earlier, TLS 1.2 might need to be enabled for your PowerShell terminal. You can enable TLS 1.2 for the current PowerShell session with the following command and then try again:
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12 Verify the installation by checking C:\Program Files\Amazon\ for the Ec2ConfigService directory.
#### Configure .NET proxy settings for the EC2Config service You can configure the EC2Config service to communicate through a proxy using one of the following methods: the AWS SDK for .NET, the system.net element, or Microsoft Group Policy

and Internet Explorer. Using the AWS SDK for .NET is the preferred method because you can specify sign-in credentials.
Methods
- Configure proxy settings using the AWS SDK for .NET (Preferred)
- Configure proxy settings using the system.net element
- Configure proxy settings using Microsoft Group Policy and Microsoft Internet Explorer
##### Configure proxy settings using the AWS SDK for .NET (Preferred)
You can configure proxy settings for the EC2Config service by specifying the proxy element in the Ec2Config.exe.config file. For more information, see Configuration Files Reference for AWS SDK for .NET.
To specify the proxy element in Ec2Config.exe.config
1. Edit the Ec2Config.exe.config file on an instance where you want the EC2Config service to communicate through a proxy. By default, the file is located in the following directory:
%ProgramFiles%\Amazon\Ec2ConfigService.
2. Add the following aws element to the configSections. Do not add this to any existing sectionGroups.
For EC2Config versions 3.17 or earlier <configSections>
   <section name="aws" type="Amazon.AWSSection, AWSSDK"/>
</configSections>
For EC2Config versions 3.18 or later <configSections>
     <section name="aws" type="Amazon.AWSSection, AWSSDK.Core"/>
</configSections>
3. Add the following aws element to the Ec2Config.exe.config file.
<aws>
   <proxy host="string value"

     port="string value" username="string value" password="string value" />
</aws>
4. Save your changes.
##### Configure proxy settings using the system.net element You can specify proxy settings in a system.net element in the Ec2Config.exe.config file. For more information, see defaultProxy element (network settings).
To specify the system.net element in Ec2Config.exe.config
1. Edit the Ec2Config.exe.config file on an instance where you want the EC2Config service to communicate through a proxy. By default, the file is located in the following directory:
%ProgramFiles%\Amazon\Ec2ConfigService.
2. Add a defaultProxy entry to system.net. For more information, see defaultProxy element (network settings).
For example, the following configuration routes all traffic to use the proxy that is currently configured for Internet Explorer, with the exception of the metadata and licensing traffic, which will bypass the proxy.
<defaultProxy>
    <proxy usesystemdefault="true" />
    <bypasslist>
        <add address="169.254.169.250" />
        <add address="169.254.169.251" />
        <add address="169.254.169.254" />
        <add address="[fd00:ec2::250]" />
        <add address="[fd00:ec2::254]" />
    </bypasslist>
</defaultProxy>
3. Save your changes.

##### Configure proxy settings using Microsoft Group Policy and Microsoft Internet Explorer The EC2Config service runs under the Local System user account. You can specify instance-wide proxy settings for this account in Internet Explorer after you change Group Policy settings on the instance.
To configure proxy settings using Group Policy and Internet Explorer
1. On an instance where you want the EC2Config service to communicate through a proxy, open a Command prompt as an Administrator, type gpedit.msc, and press Enter.
2. In the Local Group Policy Editor, under Local Computer Policy, choose Computer Configuration, Administrative Templates, Windows Components, Internet Explorer.
3. In the right-pane, choose Make proxy settings per-machine (rather than per-user) and then choose Edit policy setting.
4. Choose Enabled, and then choose Apply.
5. Open Internet Explorer, and then choose the Tools button.
6. Choose Internet Option, and then choose the Connections tab.
7. Choose LAN settings.
8. Under Proxy server, choose the Use a proxy server for your LAN option.
9. Specify address and port information and then choose OK.
#### Set EC2Config service properties from the system dialog on your EC2 Windows instance The following procedure describes how to use the EC2 Service Properties system dialog to enable or disable settings.
1. Launch and connect to your Windows instance.
2. From the Start menu, click All Programs, and then click EC2ConfigService Settings.

3. On the General tab of the EC2 Service Properties system dialog, you can enable or disable the following settings.
Set Computer Name If this setting is enabled (it is disabled by default), the host name is compared to the current internal IP address at each boot; if the host name and internal IP address do not match, the host name is reset to contain the internal IP address and then the system reboots to pick up the new host name. To set your own host name, or to prevent your existing host name from being modified, do not enable this setting.

User Data User data execution enables you to specify scripts in the instance metadata. By default, these scripts are run during the initial launch. You can also configure them to run the next time you reboot or start the instance, or every time you reboot or start the instance.
If you have a large script, we recommend that you use user data to download the script, and then run it.
For more information, see User data execution.
Event Log Use this setting to display event log entries on the console during boot for easy monitoring and debugging.
Click Settings to specify filters for the log entries sent to the console. The default filter sends the three most recent error entries from the system event log to the console.
Wallpaper Information Use this setting to display system information on the desktop background. The following is an example of the information displayed on the desktop background.
The information displayed on the desktop background is controlled by the settings file EC2ConfigService\Settings\WallpaperSettings.xml.
Enable Hibernation Use this setting to allow EC2 to signal the operating system to perform hibernation.
4. Click the Storage tab. You can enable or disable the following settings.

Root Volume This setting dynamically extends Disk 0/Volume 0 to include any unpartitioned space. This can be useful when the instance is booted from a root volume that has a custom size.
Initialize Drives This setting formats and mounts all volumes attached to the instance during start.
Drive Letter Mapping The system maps the volumes attached to an instance to drive letters. For Amazon EBS volumes, the default is to assign drive letters going from D: to Z:. For instance store

volumes, the default depends on the driver. AWS PV drivers and Citrix PV drivers assign instance store volumes drive letters going from Z: to A:. Red Hat drivers assign instance store volumes drive letters going from D: to Z:.
To choose the drive letters for your volumes, click Mappings. In the DriveLetterSetting dialog box, specify the Volume Name and Drive Letter values for each volume, click Apply, and then click OK. We recommend that you select drive letters that avoid conflicts with drive letters that are likely to be in use, such as drive letters in the middle of the alphabet.
After you specify a drive letter mapping and attach a volume with same label as one of the volume names that you specified, EC2Config automatically assigns your specified drive letter to that volume. However, the drive letter mapping fails if the drive letter is already in use. Note that EC2Config doesn't change the drive letters of volumes that were already mounted when you specified the drive letter mapping.
5. To save your settings and continue working on them later, click OK to close the EC2 Service Properties system dialog. If you have finished customizing your instance and want to create an AMI from that instance, see Create an Amazon EC2 AMI using Windows Sysprep.
#### Troubleshoot issues with the EC2Config launch agent The following information can help you troubleshoot issues with the EC2Config service.
##### Update EC2Config on an unreachable instance Use the following procedure to update the EC2Config service on a Windows Server instance that is inaccessible using Remote Desktop.

To update EC2Config on an Amazon EBS-backed Windows instance that you can't connect to
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Instances.
3. Locate the affected instance. Select the instance and choose Instance state, and then choose Stop instance.
Warning When you stop an instance, the data on any instance store volumes is erased. To keep data from instance store volumes, be sure to back it up to persistent storage.
4. Choose Launch instances and create a temporary t2.micro instance in the same Availability Zone as the affected instance. Use a different AMI than the one that you used to launch the affected instance.
Important If you do not create the instance in the same Availability Zone as the affected instance you will not be able to attach the root volume of the affected instance to the new instance.
5. In the EC2 console, choose Volumes.
6. Locate the root volume of the affected instance. Detach the volume and then attach the volume to the temporary instance that you created earlier. Attach it with the default device name (xvdf).
7. Use Remote Desktop to connect to the temporary instance, and then use the Disk Management utility to make the volume available for use.
8. Download the latest version of the EC2Config service. Extract the files from the .zip file to the Temp directory on the drive you attached.
9. On the temporary instance, open the Run dialog box, type regedit, and press Enter.
10. Choose HKEY_LOCAL_MACHINE. From the File menu, choose Load Hive. Choose the drive and then navigate to and open the following file: Windows\System32\config\SOFTWARE. When prompted, specify a key name.

11. Select the key you just loaded and navigate to Microsoft\Windows\CurrentVersion.
Choose the RunOnce key. If this key doesn't exist, choose CurrentVersion from the context (right-click) menu, choose New and then choose Key. Name the key RunOnce.
12. From the context (right-click) menu choose the RunOnce key, choose New and then choose String Value. Enter Ec2Install as the name and C:\Temp\Ec2Install.exe /quiet as the data.
13. Choose the HKEY_LOCAL_MACHINE\specified key name\Microsoft\Windows NT \CurrentVersion\Winlogon key. From the context (right-click) menu choose New, and then choose String Value. Enter AutoAdminLogon as the name and 1 as the value data.
14. Choose the HKEY_LOCAL_MACHINE\specified key name\Microsoft\Windows NT \CurrentVersion\Winlogon> key. From the context (right-click) menu choose New, and then choose String Value. Enter DefaultUserName as the name and Administrator as the value data.
15. Choose the HKEY_LOCAL_MACHINE\specified key name\Microsoft\Windows NT \CurrentVersion\Winlogon key. From the context (right-click) menu choose New, and then choose String Value. Type DefaultPassword as the name and enter a password in the value data.
16. In the Registry Editor navigation pane, choose the temporary key that you created when you first opened Registry Editor.
17. From the File menu, choose Unload Hive.
18. In Disk Management Utility, choose the drive you attached earlier, open the context (right- click) menu, and choose Offline.
19. In the Amazon EC2 console, detach the affected volume from the temporary instance and reattach it to your instance with the device name /dev/sda1. You must specify this device name to designate the volume as a root volume.
20. Stop and start Amazon EC2 instances the instance.
21. After the instance starts, check the system log and verify that you see the message Windows is ready to use.
22. Open Registry Editor and choose HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon. Delete the String Value keys you created earlier:
AutoAdminLogon, DefaultUserName, and DefaultPassword.
23. Delete or stop the temporary instance you created in this procedure.

#### EC2Config version history The following table describes the released versions of EC2Config. For information about the updates for SSM Agent, see Systems Manager SSM Agent Release Notes.
Important EC2Config has reached the end of support. Only the latest version of the EC2Config agent is available for download. Prior versions are marked as private.
Version Details Release date 4.9.5777
- Fixed issue where RSS configuration was set incorrectly for some  instance types.
- New version of SSM Agent 3.3.484.0 .
17 June 2024 4.9.5554
- Limit domain name devolution based on registry entry:
  HKEY_LOCAL_MACHINE\System\CurrentCon trolSet\Services\Dnscache\Parameters \DomainNameDevolutionLevel .
- New version of SSM Agent 3.2.1630.0 .
4 October 2023 4.9.5467
- Added retry capability for discovering console port.
- New version of SSM Agent 3.1.2282.0 .
1 August 2023 4.9.5288
- Updated AWS Core SDK to version 3.7.103.23 .
- Fixed issue where the AWS-UpdateEC2Config SSM document fails  to update EC2Config  on instances enabled with only IMDSv2.
- New version of SSM Agent 3.1.2144.0 .
8 March 2023

Version Details Release date 4.9.5231
- New version of SSM Agent 3.1.1927.0.
14 February 2023 4.9.5103
- Fixed issue where ephemeral volumes are incorrectly identified on r5d and i4i instance   families.
- New version of SSM Agent 3.1.1856.0.
5 December 2022 4.9.5064
- Updated to use PCI segment information to select the console port.
- Signed PowerShell scripts and added copyright headers.
- Fixed primary network adapter selection logic.
- New version of SSM Agent 3.1.1732.0.
16 November 2022 4.9.4588
- Updated IMDS wait logic to make only IMDSv2 requests.
- Added libec2launch.dll launch-agent shared library.
- New version of SSM Agent 3.1.1188.0.
31 May 2022 4.9.4556
- Added wait logic to ensure full initialization of NIC before use.
- New version of Log4Net 2.0.14.0 picks up security   patch.
- New version of SSM Agent 3.1.1045.0 picks up security patch.
1 March 2022 4.9.4536
- Fixed issue where userdata crashes when the Temp folder is missing.
- New version of SSM Agent 3.1.804.0.
31 January 2022

Version Details Release date 4.9.4508
- Fixed issue to correctly compute diskpart script path.
- New version of SSM Agent 3.1.338.0.
6 October 2021 4.9.4500
- Updated Install-EgpuManagerConfig with IMDS v2 support.
- Updated web links to use https.
- New version of SSM Agent 3.1.282.0 7 September 2021 4.9.4419
- Fixed IMDS version 1 fallback logic
- Updated all usage of Windows temp directory to EC2Config temp directory
- New version of SSM Agent 3.0.1124.0 2 June 2021 4.9.4381
- Added support for SSM document schema version 2.2 in EC2ConfigUpdater
- Added AWS Nitro Enclaves package version to console log
- New version of SSM Agent 3.0.529.0 4 May 2021 4.9.4326
- Removed all links in the settings UI
- This is the last EC2Config version that supports Windows Server 2008.
3 March 2021

Version Details Release date 4.9.4279
- Fixed security issue related to Ec2ConfigMonitor scheduled task
- Fixed drive letter mapping issue and incorrect ephemeral disk count
- Added OsCurrentBuild  and OsReleaseId  to console output
- New version of SSM Agent 2.3.871.0 11 December 2020 4.9.4222
- Fixed IMDS version 1 fallback logic
- New version of SSM Agent 2.3.842.0 7 April 2020 4.9.4122
- Added support for IMDS v2
- New version of SSM Agent 2.3.814.0 4 March 2020 4.9.3865
- Fixed issue detecting COM port for Windows Server 2008 R2 on metal instances
- New version of SSM Agent 2.3.722.0 31 October 2019 4.9.3519
- New version of SSM Agent 2.3.634.0 18 June 2019 4.9.3429
- New version of SSM Agent 2.3.542.0 25 April 2019 4.9.3289
- New version of SSM Agent 2.3.444.0 11 February 2019 4.9.3270
- Added plugin for setting the monitor to never turn off to fix ACPI issues
- SQL Server edition and version written to console
- New version of SSM Agent 2.3.415.0 22 January 2019 4.9.3230
- Drive Letter Mapping description updated to better align to functionality
- New version of SSM Agent 2.3.372.0 10 January 2019

Version Details Release date 4.9.3160
- Increased wait time for primary NIC
- Added default configuration for RSS and Receive Queue settings for ENA devices
- Disabled hibernation during Sysprep
- New version of SSM Agent 2.3.344.0
- Upgraded AWS SDK to 3.3.29.13 15 December 2018 4.9.3067
- Improvements made to instance hibernation
- New version of SSM Agent 2.3.235.0 8 November 2018 4.9.3034
- Added route 169.254.169.253/32 for DNS server
- New version of SSM Agent 2.3.193.0 24 October 2018 4.9.2986
- Added signing for all EC2Config related binaries
- New version of SSM Agent 2.3.136.0 11 October 2018 4.9.2953 New version of SSM Agent (2.3.117.0)
2 October 2018 4.9.2926 New version of SSM Agent (2.3.68.0)
18 September 2018 4.9.2905
- New version of SSM Agent (2.3.50.0)
- Added route 169.254.169.123/32 to AMZN time service
- Added route 169.254.169.249/32 to GRID license service
- Fixed an issue causing EBS NVMe volumes to be marked as ephemeral 17 September 2018 4.9.2854 New version of SSM Agent (2.3.13.0)
17 August 2018 4.9.2831 New version of SSM Agent (2.2.916.0)
7 August 2018

Version Details Release date 4.9.2818 New version of SSM Agent (2.2.902.0)
31 July 2018 4.9.2756 New version of SSM Agent (2.2.800.0)
27 June 2018 4.9.2688 New version of SSM Agent (2.2.607.0)
25 May 2018 4.9.2660 New version of SSM Agent (2.2.546.0)
11 May 2018 4.9.2644 New version of SSM Agent (2.2.493.0)
26 April 2018 4.9.2586 New version of SSM Agent (2.2.392.0)
28 March 2018 4.9.2565
- New version of SSM Agent (2.2.355.0)
- Fixed an issue on M5 and C5 instances (unable to find PV drivers)
- Add console logging for instance type, newest PV drivers, and NVMe drivers 13 March 2018 4.9.2549 New version of SSM Agent (2.2.325.0)
8 March 2018 4.9.2461 New version of SSM Agent (2.2.257.0)
15 February 2018 4.9.2439 New version of SSM Agent (2.2.191.0)
6 February 2018 4.9.2400 New version of SSM Agent (2.2.160.0)
16 January 2018

Version Details Release date 4.9.2327
- New version of SSM Agent (2.2.120.0)
- Added COM port discovery on Amazon EC2 bare metal instances
- Added Hyper-V status logging on Amazon EC2 bare metal instances 2 January 2018 4.9.2294 New version of SSM Agent (2.2.103.0)
4 December 2017 4.9.2262 New version of SSM Agent (2.2.93.0)
15 November 2017 4.9.2246 New version of SSM Agent (2.2.82.0)
11 November 2017 4.9.2218 New version of SSM Agent (2.2.64.0)
29 October 2017 4.9.2212 New version of SSM Agent (2.2.58.0)
23 October 2017 4.9.2203 New version of SSM Agent (2.2.45.0)
19 October 2017 4.9.2188 New version of SSM Agent (2.2.30.0)
10 October 2017 4.9.2180
- New version of SSM Agent (2.2.24.0)
- Added the Elastic GPU plugin for GPU instances 5 October 2017 4.9.2143 New version of SSM Agent (2.2.16.0)
1 October 2017 4.9.2140 New version of SSM Agent (2.1.10.0)

4.9.2130 New version of SSM Agent (2.1.4.0)


Version Details Release date 4.9.2106 New version of SSM Agent (2.0.952.0)

4.9.2061 New version of SSM Agent (2.0.922.0)

4.9.2047 New version of SSM Agent (2.0.913.0)

4.9.2031 New version of SSM Agent (2.0.902.0)

4.9.2016
- New version of SSM Agent (2.0.879.0)
- Fixed the CloudWatch Logs directory path for Windows Server 2003

4.9.1981
- New version of SSM Agent (2.0.847.0)
- Fixed the issue with important.txt  being  generated in EBS volumes.

4.9.1964 New version of SSM Agent (2.0.842.0)

4.9.1951
- New version of SSM Agent (2.0.834.0)
- Fixed the issue with drive letter not being mapped from Z: for ephemeral drives.

4.9.1925
- New version of SSM Agent (2.0.822.0)
- [Bug] This version is not a valid update target from  SSM Agent v4.9.1775.

4.9.1900 New version of SSM Agent (2.0.805.0)


Version Details Release date 4.9.1876
- New version of SSM Agent (2.0.796.0)
- Fixed an issue with output/error redirection for admin  us erdata execution.

4.9.1863
- New version of SSM Agent (2.0.790.0)
- Fixed problems with attaching multiple EBS volumes to an Amazon EC2 instance.
- Improved CloudWatch to take a configuration path, keeping the  backwards compatibility.

4.9.1791 New version of SSM Agent (2.0.767.0)

4.9.1775 New version of SSM Agent (2.0.761.0)

4.9.1752 New version of SSM Agent (2.0.755.0)

4.9.1711 New version of SSM Agent (2.0.730.0)

4.8.1676 New version of SSM Agent (2.0.716.0)

4.7.1631 New version of SSM Agent (2.0.682.0)

4.6.1579
- New version of SSM Agent (2.0.672.0)
- Fixed agent update issue with v4.3, v4.4, and v4.5

4.5.1534 New version of SSM Agent (2.0.645.1)

4.4.1503 New version of SSM Agent (2.0.633.0)

4.3.1472 New version of SSM Agent (2.0.617.1)

4.2.1442 New version of SSM Agent (2.0.599.0)


Version Details Release date 4.1.1378 New version of SSM Agent (2.0.558.0)

4.0.1343
- Run Command, State Manager, the CloudWatch agent, and domain join  support have been moved into another agent called SSM Agent.  SSM Agent will be installed as part of the EC2Config  upgrade. For more information, see EC2Config and AWS Systems Manager.
- If you have a proxy set up in EC2Config, you will need to update your proxy settings for SSM Agent before upgrading.
 If you do not update the proxy settings, you will not be  able to use Run Command to manage your instances. To avoid this, see the following information before updating to the newer version: Installing  and Configuring SSM Agent on Windows Instances in the   AWS Systems Manager User Guide.
- If you previously enabled CloudWatch integration on your instances by using a local configuration file  (AWS.EC2.W indows.CloudWatch.json ), you will need to  confi gure the file to work with SSM Agent.

3.19.1153
- Re-enabled activation plugin for instances with old AWS KMS configuration. Skip  activation for BYOL users.
- Change default TRIM behavior to be disabled during disk  for mat operation and added FormatWithTRIM for overriding InitializeDisks plugin with userdata.

3.18.1118
- Fix to reliably add routes to the primary network  adapter.
- Updates to improve support for AWS services.


Version Details Release date 3.17.1032
- Fixes duplicate system logs appearing when filters set to same category.
- Fixes to prevent from hanging during disk  initialization.

3.16.930 Added support to log "Window is Ready to use" event to Windows  Event Log on start.

3.15.880 Fix to allow uploading Systems Manager Run Command output to S3 bucket names with  '.' character.

3.14.786 Added support to override InitializeDisks plugin settings. For example: To speed up SSD disk initialize, you can temporarily disable TRIM by specifying this in userdata:
<InitializeDrivesSettings><SettingsGroup>FormatWithout TRIM</SettingsGroup></InitializeDrivesSettings

3.13.727 Systems Manager Run Command - Fixes to process commands reliably after windows  reboot.

3.12.649
- Fix to gracefully handle reboot when running  commands/ scripts.
- Fix to reliably cancel running commands.
- Add support for (optionally) uploading MSI logs to S3 when installing applications via Systems Manager Run Command.


Version Details Release date 3.11.521
- Fixes to enable RDP thumbprint generation for Windows Server  2003.
- Fixes to include timezone and UTC offset in the EC2Config log lines.
- Systems Manager support to run Run Command commands in parallel.
- Roll back previous change to bring partitioned disks  online.

3.10.442
- Fix Systems Manager configuration failures   when installing MSI applications.
- Fix to reliably bring storage disks online.
- Updates to improve support for AWS services.

3.9.359
- Fix in post Sysprep script to leave the configuration of  windo ws update in a default state.
- Fix the password generation plugin to improve the  reliability in getting GPO password policy settings.
- Restrict EC2Config/SSM log folder permissions to the local Administrators group.
- Updates to improve support for AWS services.


Version Details Release date 3.8.294
- Fixed an issue with CloudWatch that prevented logs from getting uploaded when not on primary drive.
- Improved the disk initialization process by adding retry  lo gic.
- Added improved error handling when the SetPassword plugin  occasionally failed during AMI creation.
- Updates to improve support for AWS services.

3.7.308
- Improvements to the ec2config-cli utility for config  testing and troubleshooting within instance.
- Avoid adding static routes for AWS KMS and meta-data service  on an OpenVPN adapter.
- Fixed an issue where user-data execution was not honoring the "persist" tag.
- Improved error handling when logging to the EC2 console is not available.
- Updates to improve support for AWS services.

3.6.269
- Windows activation reliability fix to first use link local  ad dress 169.254.0.250/251 for activating windows via  AWS KMS
- Improved proxy handling for Systems Manager, Windows Activation and  Domain Join scenarios
- Fixed an issue where duplicate lines of user accounts were added to the Sysprep answer file


Version Details Release date 3.5.228
- Addressed a scenario where the CloudWatch plugin may consume excessive CPU and memory reading Windows Event  Logs
- Added a link to the CloudWatch configuration documenta tion  in the EC2Config Settings UI

3.4.212
- Fixes to EC2Config when used in combination with  VM- Import.
- Fixed service naming issue in the WiX installer.

3.3.174
- Improved exception handling for Systems Manager and domain join  failures.
- Change to support Systems Manager SSM schema versionin g.
- Fixed formatting ephemeral disks on Win2K3.
- Change to support configuring disk size greater than  2TB.
- Reduced virtual memory usage by setting GC mode to  defau lt.
- Support for downloading artifacts from UNC path in aws:psModule  and aws:application  plugin.
- Improved logging for Windows activation plugin.


Version Details Release date 3.2.97
- Performance improvements by delay loading Systems Manager SSM  assemblies.
- Improved exception handling for malformed  sysprep 2008.xml.
- Command line support for Systems Manager "Apply" configuration.
- Change to support domain join when there is a pending computer rename.
- Support for optional parameters in the aws:appli cations   plugin.
- Support for command array in aws:psModule  plugin.

3.0.54
- Enable support for Systems Manager.
- Automatically domain join EC2 Windows instances to an AWS  directory via Systems Manager.
- Configure and upload CloudWatch logs/metrics via  Systems Manager.
- Install PowerShell modules via Systems Manager.
- Install MSI applications via Systems Manager.


Version Details Release date 2.4.233
- Added scheduled task to recover EC2Config from service startup failures.
- Improvements to the Console log error messages.
- Updates to improve support for AWS services.

2.3.313
- Fixed an issue with large memory consumption in some cases  when the CloudWatch Logs feature is enabled.
- Fixed an upgrade bug so that ec2config versions lower than 2.1.19 can now upgrade to latest.
- Updated COM port opening exception to be more friendly and  useful in logs.
- Ec2configServiceSettings UI disabled resizing and fixed  the attribution and version display placement in UI.

2.2.12
- Handled NullPointerException while querying a registry key for determining Windows Sysprep state which returned null occasionally.
- Freed up unmanaged resources in finally block.

2.2.11 Fixed a issue in CloudWatch plugin for handling empty log lines.

2.2.10
- Removed configuring CloudWatch Logs settings through UI.
- Enable users to define CloudWatch Logs settings in %ProgramFiles%\Amazon\Ec2ConfigService \Settings\AWS.EC2.Windows.CloudWatch.json

 file to allow future enhancements.


Version Details Release date 2.2.9 Fixed unhandled exception and added logging.

2.2.8
- Fixes Windows OS version check in EC2Config Installer to support Windows Server 2003 SP1 and later.
- Fixes null value handling when reading registry keys  related to updating Sysprep config files.

2.2.7
- Added support for EC2Config to run during Sysprep execution for Windows 2008 and greater.
- Improved exception handling and logging for better  d iagnostics

2.2.6
- Reduced the load on the instance and on CloudWatch Logs when  uploading log events.
- Addressed an upgrade issue where the CloudWatch Logs plug-in did  not always stay enabled

2.2.5
- Added support to upload logs to CloudWatch Log Service.
- Fixed a race condition issue in Ec2OutputRDPCert  plug-in
- Changed EC2Config Service recovery option to Restart from TakeNoAction
- Added more exception information when EC2Config  Crashes

2.2.4
- Fixed a typo in PostSysprep.cmd
- Fixed the bug which EC2Config does not pin itself onto  start menu for OS2012+


Version Details Release date 2.2.3
- Added option to install EC2Config without service starting immediately upon install. To use, run 'Ec2Install.exe  s tart=false' from the command prompt
- Added parameter in wallpaper plugin to control  adding/re moving wallpaper. To use, run 'Ec2WallpaperInfo.exe  set' or 'Ec2WallpaperInfo.exe revert' from the command  prompt
- Added checking for RealTimeIsUniversal key, output  i ncorrect settings of the RealTimeIsUniveral registry key to the Console
- Removed EC2Config dependency on Windows temp folder
- Removed UserData execution dependency on .Net 3.5

2.2.2
- Added check to service stop behavior to check that  res ources are being released
- Fixed issue with long execution times when joined to  domai n

2.2.1
- Updated Installer to allow upgrades from older  versions
- Fixed Ec2WallpaperInfo bug in .Net4.5 only  environment
- Fixed intermittent driver detection bug
- Added silent install option. Execute Ec2Install.exe with  the '- q' option. eg: 'Ec2Install.exe -q'

2.2.0
- Added support for .Net4 and .Net4.5 only  environments
- Updated Installer


Version Details Release date 2.1.19
- Added ephemeral disk labeling support when using Intel  ne twork driver (eg. C3 instance Type). For more information, see Enhanced networking on Amazon EC2 instances.
- Added AMI Origin Version and AMI Origin Name support to the console output
- Made changes to the Console Output for consistent  format ting/parsing
- Updated Help File

2.1.18
- Added EC2Config WMI Object for Completion notification  (- Namespace root\Amazon -Class EC2_ConfigService)
- Improved Performance of Startup WMI query with large Event  Logs; could cause prolonged high CPU during initial execution

2.1.17
- Fixed UserData execution issue with Standard Output and Standard Error buffer filling
- Fixed incorrect RDP thumbprint sometimes appearing in Console Output for >= w2k8 OS
- Console Output now contains 'RDPCERTIFICATE-Su bjectName:'  for Windows 2008+, which contains the machine name  value
- Added D:\ to Drive Letter Mapping dropdown
- Moved Help button to top right and changed  look/feel
- Added Feedback survey link to top right


Version Details Release date 2.1.16
- General Tab includes link to EC2Config download page for new Versions
- Desktop Wallpaper overlay now stored in Users Local  Ap pdata folder instead of My Documents to support MyDoc  re direction
- MSSQLServer name sync'd with system in Post-Sysprep script  (2008+)
- Reordered Application Folder (moved files to Plugin  d irectory and removed duplicate files)
- Changed System Log Output (Console):
- *Moved to a date, name, value format for easier parsing (Please start migrating dependencies to new format)
- *Added 'Ec2SetPassword' plugin status
- *Added Sysprep Start and End times
- Fixed issue of Ephemeral Disks not being labeled as  'Temp orary Storage' for non-english Operating Systems
- Fixed EC2Config Uninstall failure after running  Sysprep


Version Details Release date 2.1.15
- Optimized requests to the Metadata service
- Metadata now bypass Proxy Settings
- Ephemeral Disks labeled as 'Temporary Storage' and  Impo rtant.txt placed on volume when found (Citrix PV drivers only). For more information, see Upgrade PV drivers on EC2 Windows instances.
- Ephemeral Disks assigned drive letters from Z to A (Citrix  PV drivers only) - assignment can be overwritten using Drive  Le tter Mapping plugin with Volume labels 'Temporary Storage X' where x is a number 0-25)
- UserData now runs immediately following 'Windows is Ready'

2.1.14 Desktop wallpaper fixes

2.1.13
- Desktop wallpaper will display hostname by default
- Removed dependency on Windows Time service
- Route added in cases where multiple IPs are assigned to a single interface

2.1.11
- Changes made to Ec2Activation Plugin
- -Verifies Activation status every 30 days
- -If Grace Period has 90 days remaining (out of 180),  re attempts activation


Version Details Release date 2.1.10
- Desktop wallpaper overlay no longer persists with Sysprep or Shutdown without Sysprep
- Userdata option to run on every service start with  <pe rsist>true</persist>
- Changed location and name of /DisableWinUpdate.cmd to  / Scripts/PostSysprep.cmd
- Administrator password set to not expire by default in  /Scri pts/PostSysprep.cmd
- Uninstall will remove EC2Config PostSysprep script from  c:\ windows\setup\script\CommandComplete.cmd
- Add Route supports custom interface metrics

2.1.9 UserData Execution no longer limited to 3851 Characters


Version Details Release date 2.1.7
- OS Version and language identifier written to  console
- EC2Config version written to console
- PV driver version written to console
- Detection of Bug Check and output to the console on next boot when found
- Option added to config.xml to persist Sysprep  credentials
- Add Route Retry logic in cases of ENI being unavailable at start
- User Data execution PID written to console
- Minimum generated password length retrieved from  GPO
- Set service start to retry 3 attempts
- Added S3_DownloadFile.ps1 and S3_Upload file.ps1 examples   to /Scripts folder


Version Details Release date 2.1.6
- Version information added to General tab
- Renamed the Bundle tab to Image
- Simplified the process of specifying passwords and moved the password-related UI from the General tab to the Image tab
- Renamed the Disk Settings tab to Storage
- Added a Support tab with common tools for  troubleshooti ng
- Windows Server 2003 sysprep.ini  set to extend OS partition by  default
- Added the private IP address to the wallpaper
- Private IP address displayed on wallpaper
- Added retry logic for Console output
- Fixed Com port exception for metadata accessibility --  cause d EC2Config to terminate before console output is  displayed
- Checks for activation status on every boot -- activates as necessary
- Fixed issue of relative paths -- caused when manually executing wallpaper shortcut from startup folder; pointing to Administrator/logs
- Fixed default background color for Windows Server 2003 user  (other than Administrator)


Version Details Release date 2.1.2
- Console timestamps in UTC (Zulu)
- Removed appearance of hyperlink on Sysprep tab
- Addition of feature to dynamically expand Root Volume on first boot for Windows 2008+
- When Set-Password is enabled, now automatically enables EC2Config to set the password
- EC2Config checks activation status prior to running  Sysprep (presents warning if not activated)
- Windows Server 2003 Sysprep.xml  now defaults to UTC timezone   instead of Pacific
- Randomized Activation Servers
- Renamed Drive Mapping tab to Disk Settings
- Moved Initialize Drives UI items from General to the Disk  Set tings tab
- Help button now points to HTML help file
- Updated HTML help file with changes
- Updated 'Note' text for Drive Letter Mappings
- Added InstallUpdates.ps1 to /Scripts folder for automating Patches and cleanup prior to Sysprep


Version Details Release date 2.1.0
- Desktop wallpaper displays instance information by default upon first logon (not disconnect/reconnect)
- PowerShell can be run from the userdata by  surrounding the code with  <powershell></powershell>

## Use EC2 Fast Launch for your Windows instances When you configure a Windows Server AMI for EC2 Fast Launch, Amazon EC2 creates a set of pre- provisioned snapshots to use for faster launching, as follows.
1. Amazon EC2 launches a set of temporary t3 instances, based on your settings.
2. As each temporary instance completes the standard launch steps, Amazon EC2 creates a pre- provisioned snapshot of the instance. It stores the snapshot in your Amazon S3 bucket.
3. When the snapshot is ready, Amazon EC2 terminates the associated t3 instance to keep resource costs as low as possible.
4. The next time Amazon EC2 launches an instance from the EC2 Fast Launch enabled AMI, it uses one of the snapshots to significantly reduce the time it takes to launch.
Amazon EC2 automatically replenishes the snapshots you have on hand as it uses them to launch instances from the EC2 Fast Launch enabled AMI.
Any account that has access to an AMI with EC2 Fast Launch enabled can benefit from reduced launch times. When the AMI owner grants access for you to launch instances, the pre-provisioned snapshots come from the AMI owner's account.
If an AMI that supports EC2 Fast Launch is shared with you, you can enable or disable faster launching on the shared AMI yourself. If you enable a shared AMI for EC2 Fast Launch, Amazon EC2 creates the pre-provisioned snapshots directly in your account. If you deplete the snapshots in your account, you can still use snapshots from the AMI owner's account.

Note EC2 Fast Launch deletes pre-provisioned snapshots as soon as they're consumed by a launch to minimize storage costs and prevent reuse. However, if the deleted snapshots match a retention rule, Recycle Bin automatically retains them. We recommend that you review the scope of your Recycle Bin retention rules so that this doesn't happen. For more information, see Recycle Bin in the Amazon EBS User Guide.
This feature is not the same as EBS fast snapshot restore. You must explicitly enable EBS fast snapshot restore on a per-snapshot basis, and it has its own associated costs.
The following video demonstrates how to configure your Windows AMI for faster launching with a quick overview of the related key terms and their definitions: Launching EC2 Windows instances up to 65% faster on AWS.
Resource costs There is no service charge to configure Windows AMIs for EC2 Fast Launch. However, standard pricing applies for any underlying AWS resources that Amazon EC2 uses. To learn more about associated resource costs and how to manage them, see Manage costs for EC2 Fast Launch underlying resources.
Contents
- Key terms
- EC2 Fast Launch prerequisites for Windows
- Configure EC2 Fast Launch settings for your Amazon EC2 Windows Server AMI
- View AMIs with EC2 Fast Launch enabled
- Manage costs for EC2 Fast Launch underlying resources
- Monitor EC2 Fast Launch
- Service-linked role for EC2 Fast Launch
- Troubleshoot Windows EC2 Fast Launch
### Key terms The EC2 Fast Launch feature uses the following key terms:

Pre-provisioned snapshot A snapshot of an instance that was launched from a Windows AMI with EC2 Fast Launch enabled, and that has completed the following Windows launch steps, rebooting as required.
- Sysprep specialize
- Windows Out of Box Experience (OOBE)
When these steps are complete, EC2 Fast Launch stops the instance, and creates a snapshot that is later used for faster launching from the AMI, based on your configuration.
Launch frequency Controls the number of pre-provisioned snapshots that Amazon EC2 can launch within the specified timeframe. When you enable EC2 Fast Launch for your AMI, Amazon EC2 creates the initial set of pre-provisioned snapshots in the background. For example, if the launch frequency is set to five launches per hour, which is the default, then EC2 Fast Launch creates an initial set of five pre-provisioned snapshots.
When Amazon EC2 launches an instance from an AMI with EC2 Fast Launch enabled, it uses one of the pre-provisioned snapshots to reduce the launch time. As snapshots are used, they are automatically replenished, up to the number specified by the launch frequency.
If you expect a spike in the number of instances that are launched from your AMI – during a special event, for example – you can increase the launch frequency in advance to cover the additional instances that you'll need. When your launch rate returns to normal, you can adjust the frequency back down.
When you experience a higher number of launches than anticipated, you might use up all the pre-provisioned snapshots that you have available. This doesn't cause any launches to fail.
However, it can result in some instances going through the standard launch process, until snapshots can be replenished.
Target resource count The number of pre-provisioned snapshots to keep on hand for an Amazon EC2 Windows Server AMI with EC2 Fast Launch enabled.
Max parallel launches Controls how many instances Amazon EC2 can launch at the same time to create the pre- provisioned snapshots for EC2 Fast Launch. If your target resource count is higher than the maximum parallel launches that you've configured, then Amazon EC2 launches the number of

instances specified by Max parallel launches to start creating the snapshots. As those instances complete the process, Amazon EC2 takes the snapshot and stops the instance. Then it continues to launch more instances until the total number of snapshots available has reached the target resource count. The value for Max parallel launches must be 6 or greater.
### EC2 Fast Launch prerequisites for Windows Before you set up EC2 Fast Launch, verify that you've met the following prerequisites that are required to create snapshots for the AMIs in your AWS account:
- If you provide a custom launch template when you configure EC2 Fast Launch, the service uses the VPC and other configuration settings that you've defined in the launch template. For more information, see Use a launch template when you set up EC2 Fast Launch.
- If you don't use a custom launch template to configure your settings, you must attach the EC2FastLaunchFullAccess policy to your current IAM role before you enable EC2 Fast Launch.
Then the service automatically creates an CloudFormation stack with the following resources in your AWS account.
- A virtual private cloud (VPC)
- Private subnets across multiple Availability Zones
- A launch template configured with Instance Metadata Service Version 2 (IMDSv2)
- A security group with no inbound or outbound rules
- Private EC2 Fast Launch AMIs must support user data script execution.
- To configure EC2 Fast Launch for an AMI, you must create the AMI using Sysprep with the shutdown option. The EC2 Fast Launch feature doesn't currently support AMIs that were created from a running instance.
To create an AMI using Sysprep, see Create an Amazon EC2 AMI using Windows Sysprep.
- To enable EC2 Fast Launch for an encrypted AMI that uses a customer managed key for encryption, you must grant the service-linked role for EC2 Fast Launch permission to use the CMK. For more information, see the section called "Access to customer managed keys".
- The default quota for Max parallel launches across all AMIs in an AWS account is 40 per Region.
You can request a Service Quotas increase for your account, as follows.
1. Open the Service Quotas console at https://console.aws.amazon.com/servicequotas/.
2. In the navigation pane, choose AWS services.

3. In the search bar, enter EC2 Fast Launch, and select the result.
4. Select the link for Parallel instance launches to open the service quota detail page.
5. Choose Request increase at account level.
For more information, see Requesting a quota increase in the Service Quotas User Guide.
### Configure EC2 Fast Launch settings for your Amazon EC2 Windows Server AMI You can configure EC2 Fast Launch for Windows AMIs that you own, or AMIs that are shared with you from the AWS Management Console, API, SDKs, CloudFormation, or AWS Command Line Interface (AWS CLI). Before you configure EC2 Fast Launch, verify that your AMI meets all of the prerequisites that are required to create the pre-provisioned snapshots. For more information, see EC2 Fast Launch prerequisites for Windows.
When you enable faster launching for Windows instances, Amazon EC2 checks to make sure that you have the required permissions to launch instances from the specified AMI and Launch Template (if provided), including permissions for encrypted AMIs. To prevent errors during the instance launch process, the service validates your permissions before EC2 Fast Launch is enabled. If you don't have the required permissions, the service returns an error, and does not enable EC2 Fast Launch.
EC2 Fast Launch integrates with EC2 Image Builder to help you create custom images with EC2 Fast Launch enabled. For more information, see Create distribution settings for a Windows AMI with EC2 Fast Launch enabled (AWS CLI) in the EC2 Image Builder User Guide.
#### Enable EC2 Fast Launch Before changing these settings, make sure that your AMI, and the Region that you run in meet all EC2 Fast Launch prerequisites for Windows.
Console To enable EC2 Fast Launch
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, under Images, choose AMIs.
3. Choose the AMI to update by selecting the check box next to the Name.

4. From the Actions menu above the list of AMIs, choose Configure fast launch. This opens the Configure fast launch page, where you configure the settings for EC2 Fast Launch.
5. To start using pre-provisioned snapshots to launch instances from your Windows AMI faster, select the Enable fast launch for Windows checkbox.
6. From the Set anticipated launch frequency drop-down list, choose a value to specify the number of snapshots that are created and maintained to cover your expected instance launch volume.
7. When you're done making changes, choose Save changes.
Note If you need to use a launch template to specify a VPC, or to configure metadata settings for IMDSv2, see Use a launch template when you set up EC2 Fast Launch.
AWS CLI To enable EC2 Fast Launch Use the following enable-fast-launch command to enable EC2 Fast Launch for the specified AMI, launching six parallel instances for pre-provisioning. aws ec2 enable-fast-launch \ --image-id ami-0abcdef1234567890  \ --max-parallel-launches 6 \ --resource-type snapshot The following is example output.
{ "ImageId": "ami-0abcdef1234567890", "ResourceType": "snapshot", "SnapshotConfiguration": { "TargetResourceCount": 10 }, "LaunchTemplate": {}, "MaxParallelLaunches": 6, "OwnerId": "0123456789123",

 "State": "enabling", "StateTransitionReason": "Client.UserInitiated", "StateTransitionTime": "2022-01-27T22:16:03.199000+00:00"
} PowerShell To enable EC2 Fast Launch Use the Enable-EC2FastLaunch cmdlet to enable EC2 Fast Launch for the specified AMI, launching six parallel instances for pre-provisioning.
Enable-EC2FastLaunch `
 -ImageId ami-0abcdef1234567890 `
 -MaxParallelLaunch 6 `
 -Region us-west-2 `
 -ResourceType snapshot The following is example output.
ImageId               : ami-0abcdef1234567890 LaunchTemplate        :
 MaxParallelLaunches   : 6 OwnerId               : 0123456789123 ResourceType          : snapshot SnapshotConfiguration : Amazon.EC2.Model.FastLaunchSnapshotConfigurationResponse State                 : enabling StateTransitionReason : Client.UserInitiated StateTransitionTime   : 2/25/2022 12:24:11 PM
#### Disable EC2 Fast Launch Before changing these settings, make sure that your AMI, and the Region that you run in meet all EC2 Fast Launch prerequisites for Windows.
Console To disable EC2 Fast Launch
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, under Images, choose AMIs.

3. Choose the AMI to update by selecting the check box next to the Name.
4. From the Actions menu above the list of AMIs, choose Configure fast launch. This opens the Configure fast launch page, where you configure the settings for EC2 Fast Launch.
5. Clear the Enable fast launch for Windows checkbox to disable EC2 Fast Launch and to remove pre-provisioned snapshots. This results in the AMI using the standard launch process for each instance, going forward.
Note When you disable Windows image optimization, any existing pre-provisioned snapshots are automatically deleted. This step must be completed before you can start using the feature again.
6. When you're done making changes, choose Save changes.
AWS CLI To disable EC2 Fast Launch Use the following disable-fast-launch command to disable EC2 Fast Launch on the specified AMI, and clean up existing pre-provisioned snapshots. aws ec2 disable-fast-launch --image-id ami-01234567890abcedf The following is example output.
{ "ImageId": "ami-01234567890abcedf", "ResourceType": "snapshot", "SnapshotConfiguration": {}, "LaunchTemplate": { "LaunchTemplateId": "lt-01234567890abcedf", "LaunchTemplateName": "EC2FastLaunchDefaultResourceCreation- a8c6215d-94e6-441b-9272-dbd1f87b07e2", "Version": "1"
    }, "MaxParallelLaunches": 6, "OwnerId": "0123456789123", "State": "disabling",

    "StateTransitionReason": "Client.UserInitiated", "StateTransitionTime": "2022-01-27T22:47:29.265000+00:00"
} PowerShell To disable EC2 Fast Launch Use the Disable-EC2FastLaunch cmdlet to disable EC2 Fast Launch on the specified AMI, and clean up existing pre-provisioned snapshots.
Disable-EC2FastLaunch -ImageId ami-0abcdef1234567890 The following is example output.
ImageId               : ami-0abcdef1234567890 LaunchTemplate        :
 Amazon.EC2.Model.FastLaunchLaunchTemplateSpecificationResponse MaxParallelLaunches   : 6 OwnerId               : 0123456789123 ResourceType          : snapshot SnapshotConfiguration :
 State                 : disabling StateTransitionReason : Client.UserInitiated StateTransitionTime   : 2/25/2022 1:10:08 PM
#### Use a launch template when you set up EC2 Fast Launch With a launch template, you can configure a set of launch parameters that Amazon EC2 uses each time it launches an instance from that template. You can specify such things as an AMI to use for your base image, instance types, storage, network settings, and more.
Launch templates are optional, except for the following specific cases, where you must use a launch template for your Windows AMI when you configure faster launching:
- You must use a launch template to specify an existing VPC for your Windows AMI. This doesn't apply if you use the default VPC for your AWS account.
- If your account includes a policy that enforces IMDSv2 for Amazon EC2 instances, you must create a launch template that specifies the metadata configuration to enforce IMDSv2.

Use the launch template that includes your metadata configuration from the EC2 console, or when you run the enable-fast-launch command in the AWS CLI, or call the EnableFastLaunch API action.
Amazon EC2 EC2 Fast Launch doesn't support the following configuration when you use a launch template. If you use a launch template for EC2 Fast Launch, you must not specify any of the following:
- User data scripts
- Termination protection
- Disabled metadata
- Spot option
- Shutdown behavior that terminates the instance
- Resource tags for network interface, elastic graphic, or spot instance requests
##### Specify a VPC Step 1: Create a launch template Create a launch template that specifies the following details for your Windows instances:
- The VPC subnet.
- An instance type of t3.xlarge.
For more information, see Create an Amazon EC2 launch template.
Step 2: Specify the launch template for your EC2 Fast Launch AMI Console To specify the launch template for EC2 Fast Launch
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, under Images, choose AMIs.
3. Choose the AMI to update by selecting the check box next to the Name.

4. From the Actions menu above the list of AMIs, choose Configure fast launch. This opens the Configure fast launch page, where you configure the settings for EC2 Fast Launch.
5. The Launch template box performs a filtered search that finds launch templates in your account in the current Region that match the text you've entered. Specify all or part of the launch template name or ID in the box to show a list of matching launch templates. For example, if you enter fast in the box, Amazon EC2 finds all of the launch templates in your account in the current Region that have "fast" in the name.
To create a new launch template, you can choose Create launch template.
6. When you select a launch template, Amazon EC2 shows the default version for that template in the Source template version box. To specify a different version, highlight the default version to replace it, and enter the version number you want in the box.
7. When you're done making changes, choose Save changes.
AWS CLI To specify the launch template for EC2 Fast Launch Use the enable-fast-launch command with the --launch-template option, specifying either the name or the ID of the launch template.
--launch-template LaunchTemplateName=my-launch-template PowerShell To specify the launch template for EC2 Fast Launch Use the Enable-EC2FastLaunch cmdlet with the -LaunchTemplate_LaunchTemplateId or - LaunchTemplate_LaunchTemplateName parameter.
-LaunchTemplate_LaunchTemplateName my-launch-template For more information about EC2 launch templates, see Store instance launch parameters in Amazon EC2 launch templates.

### View AMIs with EC2 Fast Launch enabled You can use the describe-fast-launch-images command in the AWS CLI, or the Get- EC2FastLaunchImage Tools for PowerShell Cmdlet to get details for AMIs that have EC2 Fast Launch enabled.
Amazon EC2 provides the following details for each Windows AMI that is returned in the results:
- The image ID for an AMI with EC2 Fast Launch enabled.
- The resource type that is used for pre-provisioning the associated Windows AMI. Supported value: snapshot.
- The snapshot configuration, which is a group of parameters that configure pre-provisioning for the associated Windows AMI using snapshots.
- Launch template information, including the ID, name, and version of the launch template that the associated AMI uses when it launches Window instances from pre-provisioned snapshots.
- The maximum number of instances that can be launched at the same time for creating resources.
- The owner ID for the associated AMI. This is not populated for AMIs that are shared with you.
- The current state of EC2 Fast Launch for the associated AMI. Supported values include: enabling | enabling-failed | enabled | enabled-failed | disabling | disabling-failed.
Note You can also see the current state displayed in the Manage image optimization page in the EC2 console, as Image optimization state.
- The reason that EC2 Fast Launch for the associated AMI changed to the current state.
- The time that EC2 Fast Launch for the associated AMI changed to the current state.
AWS CLI To find AMIs configured for EC2 Fast Launch Use the following describe-fast-launch-images command to describe the details for each of the AMIs in the account that are configured for EC2 Fast Launch. In this example, only one AMI in the account is configured for EC2 Fast Launch.

aws ec2 describe-fast-launch-images The following is example output.
{ "FastLaunchImages": [ { "ImageId": "ami-01234567890abcedf", "ResourceType": "snapshot", "SnapshotConfiguration": {}, "LaunchTemplate": { "LaunchTemplateId": "lt-01234567890abcedf", "LaunchTemplateName": "EC2FastLaunchDefaultResourceCreation- a8c6215d-94e6-441b-9272-dbd1f87b07e2", "Version": "1"
            }, "MaxParallelLaunches": 6, "OwnerId": "0123456789123", "State": "enabled", "StateTransitionReason": "Client.UserInitiated", "StateTransitionTime": "2022-01-27T22:20:06.552000+00:00"
        } ]
} PowerShell To find AMIs configured for EC2 Fast Launch Use the following Get-EC2FastLaunchImage cmdlet to describe the details for each of the AMIs in the account that are configured for EC2 Fast Launch. In this example, only one AMI in the account is configured for EC2 Fast Launch.
Get-EC2FastLaunchImage -ImageId ami-0abcdef1234567890 The following is example output.
ImageId               : ami-0abcdef1234567890 LaunchTemplate        :
 Amazon.EC2.Model.FastLaunchLaunchTemplateSpecificationResponse MaxParallelLaunches   : 6

OwnerId               : 012345678912 ResourceType          : snapshot SnapshotConfiguration :
State                 : enabled StateTransitionReason : Client.UserInitiated StateTransitionTime   : 2/25/2022 12:54:43 PM
### Manage costs for EC2 Fast Launch underlying resources There is no service charge to configure Windows AMIs for EC2 Fast Launch. However, when you enable EC2 Fast Launch for an Amazon EC2 Windows AMI, standard pricing applies for underlying AWS resources that Amazon EC2 uses to prepare and store the pre-provisioned snapshots. You can configure cost allocation tags to help you track and manage the costs that are associated with EC2 Fast Launch resources. For more information about how to configure cost allocation tags, see Track EC2 Fast Launch costs on your bill.
The following example demonstrates how the costs associated with EC2 Fast Launch snapshots costs might be allocated.
Example scenario: The AtoZ Example company has a Windows AMI with a 50 GiB EBS root volume.
They enable EC2 Fast Launch for their AMI, and set the target resource count to five. Over the course of a month, using EC2 Fast Launch for their AMI costs them around $5.00, and the cost breakdown is as follows:
1. When AtoZ Example enables EC2 Fast Launch, Amazon EC2 launches five small instances. Each instance runs through the Sysprep and OOBE Windows launch steps, rebooting as required.
This takes several minutes for each instance (time can vary, based on how busy that Region or Availability Zone (AZ) is, and on the size of the AMI).
Costs
- Instance runtime costs (or minimum runtime, if applicable): five instances
- Volume costs: five EBS root volumes
2. When the pre-provisioning process completes, Amazon EC2 takes a snapshot of the instance, which it stores in Amazon S3. Snapshots are typically stored for 4–8 hours before they are consumed by a launch. In this case, the cost is roughly $0.02 to $0.05 per snapshot.
Costs
- Snapshot storage (Amazon S3): five snapshots

3. After Amazon EC2 takes the snapshot, it stops the instance. At that point, the instance is no longer accruing costs. However EBS volume costs continue to accrue.
Costs
- EBS volumes: costs continue for the associated EBS root volumes.
Note The costs shown here are for demonstration purposes only. Your costs will vary, depending on your AMI configuration and pricing plan.
#### Track EC2 Fast Launch costs on your bill Cost allocation tags can help you organize your AWS bill to reflect the costs associated with EC2 Fast Launch. You can use the following tag that Amazon EC2 adds to the resources it creates when it prepares and stores pre-provisioned snapshots for EC2 Fast Launch:
Tag key: CreatedBy, Value: EC2 Fast Launch After you activate the tag in the Billing and Cost Management console, and set up your detailed billing report, the user:CreatedBy column appears on the report. The column includes values from all services. However, if you download the CSV file, you can import the data into a spreadsheet, and filter for EC2 Fast Launch in the value. This information also appears in the AWS Cost and Usage Report when the tag is activated.
Step 1: Activate user-defined cost allocation tags To include resource tags in your cost reports, you must first activate the tag in the Billing and Cost Management console. For more information, see Activating User-Defined Cost Allocation Tags in the AWS Billing and Cost Management User Guide.
Note Activation can take up to 24 hours.
Step 2: Set up a cost report

If you already have a cost report set up, a column for your tag appears the next time the report runs after activation is complete. To set up cost reports for the first time, choose one of the following.
- See Setting up a monthly cost allocation report in the AWS Billing and Cost Management User Guide.
- See Creating Cost and Usage Reports in the AWS Cost and Usage Report User Guide.
Note It can take up to 24 hours for AWS to start delivering reports to your S3 bucket.
You can configure EC2 Fast Launch for Windows AMIs that you own, or AMIs that are shared with you from the Amazon EC2 console, API, SDKs, CloudFormation, or ec2 commands in the AWS CLI.
The following sections cover configuration steps for the Amazon EC2 console and AWS CLI.
You can also create custom Windows AMIs that are configured for EC2 Fast Launch with EC2 Image Builder. For more information, see Create distribution settings for a Windows AMI with EC2 Fast Launch enabled (AWS CLI).
### Monitor EC2 Fast Launch This section covers how to monitor the Amazon EC2 Windows Server AMIs in your account that have EC2 Fast Launch enabled.
#### Monitor EC2 Fast Launch state changes with EventBridge When the state changes for a Windows AMI with EC2 Fast Launch enabled, Amazon EC2 generates an EC2 Fast Launch State-change Notification event. Then Amazon EC2 sends the state change event to Amazon EventBridge (formerly known as Amazon CloudWatch Events).
You can create EventBridge rules that trigger one or more actions in response to the state change event. For example, you can create an EventBridge rule that detects when EC2 Fast Launch is enabled and performs the following actions:
- Sends a message to an Amazon SNS topic that notifies its subscribers.
- Invokes a Lambda function that performs some action.
- Sends the state change data to Amazon Data Firehose for analytics.

For more information, see Creating Amazon EventBridge rules that react to events in the Amazon EventBridge User Guide.
State change events The EC2 Fast Launch feature emits JSON formatted state change events on a best-effort basis.
Amazon EC2 sends the events to EventBridge in near real time. This section describes the event fields and shows an example of the event format.
EC2 Fast Launch State-change Notification imageId Identifies the AMI with the EC2 Fast Launch state change. resourceType The type of resource to use for pre-provisioning. Supported value: snapshot. The default value is snapshot. state The current state of the EC2 Fast Launch feature for the specified AMI. Valid values include the following:
- enabling – You've enabled the EC2 Fast Launch feature for the AMI, and Amazon EC2 has started creating snapshots for the pre-provisioning process.
- enabling-failed – Something went wrong that caused the pre-provisioning process to fail the first time that you enabled the EC2 Fast Launch for an AMI. This can happen anytime during the pre-provisioning process.
- enabled – The EC2 Fast Launch feature is enabled. The state changes to enabled as soon as Amazon EC2 creates the first pre-provisioned snapshot for a newly enabled EC2 Fast Launch AMI. If the AMI was already enabled and goes through pre-provisioning again, the state change happens right away.
- enabled-failed – This state applies only if this is not the first time your EC2 Fast Launch AMI goes through the pre-provisioning process. This can happen if the EC2 Fast Launch feature is disabled and then later enabled again, or if there is a configuration change or other error after pre-provisioning is completed for the first time.
- disabling – The AMI owner has turned off the EC2 Fast Launch feature for the AMI, and Amazon EC2 has started the clean up process.

- disabled – The EC2 Fast Launch feature is disabled. The state changes to disabled as soon as Amazon EC2 completes the clean up process.
- disabling-failed – Something went wrong that caused the clean up process to fail. This means that some pre-provisioned snapshots may still remain in the account. stateTransitionReason The reason that the state changed for the EC2 Fast Launch AMI.
Note All fields in this event message are required.
The following example shows a newly enabled EC2 Fast Launch AMI that has launched the first instance to start the pre-provisioning process. At this point, the state is enabling. After Amazon EC2 creates the first pre-provisioned snapshot, the state changes to enabled.
{ "version": "0", "id": "01234567-0123-0123-0123-012345678901", "detail-type": "EC2 Fast Launch State-change Notification", "source": "aws.ec2", "account": "123456789012", "time": "2022-08-31T20:30:12Z", "region": "us-east-1", "resources": [ "arn:aws:ec2:us-east-1:123456789012:image/ami-123456789012"
 ], "detail": { "imageId": "ami-123456789012", "resourceType": "snapshot", "state": "enabling", "stateTransitionReason": "Client.UserInitiated"
 } }

#### Monitor EC2 Fast Launch metrics with CloudWatch Amazon EC2 AMIs with EC2 Fast Launch enabled send metrics to Amazon CloudWatch. You can use the AWS Management Console, the AWS CLI, or an API to list the metrics that EC2 Fast Launch sends to CloudWatch. The AWS/EC2 namespace includes the following EC2 Fast Launch metrics:
Metric Description NumberOfAvailableFastLaunchSnapshots The number of pre-provisioned snapshots available per EC2 Fast Launch enabled AMI.
NumberOfInstancesFastLaunched The number of instances per EC2 Fast Launch enabled AMI that were launched from pre- provisioned snapshots.
NumberOfInstancesNotFastLaunched The number of instances per EC2 Fast Launch enabled AMI that resulted in a cold boot due to the lack of available pre-provisioned snapshots at launch time.
FastLaunchSnapshotUsedToRefillStartTime The timestamp when Amazon EC2 launched a new image from a EC2 Fast Launch enabled AMI to create another snapshot after an existing snapshot was used.
FastLaunchSnapshotCreationTime Measures the time it took for Amazon EC2 to launch an instance and create a snapshot for a EC2 Fast Launch enabled AMI.
### Service-linked role for EC2 Fast Launch Amazon EC2 uses service-linked roles for the permissions that it requires to call other AWS services on your behalf. A service-linked role is a unique type of IAM role that is linked directly to an AWS service. Service-linked roles provide a secure way to delegate permissions to AWS services because only the linked service can assume a service-linked role. For more information about how Amazon EC2 uses IAM roles, including service-linked roles, see IAM roles for Amazon EC2.

Amazon EC2 uses the service-linked role named AWSServiceRoleForEC2FastLaunch to create and manage a set of pre-provisioned snapshots that reduce the time it takes to launch instances from your Windows AMI.
#### Permissions granted by AWSServiceRoleForEC2FastLaunch The AWSServiceRoleForEC2FastLaunch service-linked role trusts the following service to assume the role:
- ec2fastlaunch.amazonaws.com Amazon EC2 uses the EC2FastLaunchServiceRolePolicy managed policy to complete the following actions:
- AWS CloudFormation – Allow EC2 Fast Launch to get a description of associated CloudFormation stacks.
- Amazon CloudWatch – Post metric data associated with EC2 Fast Launch to the Amazon EC2 namespace.
- Amazon EC2 – Access is granted for EC2 Fast Launch to perform the following actions:
- Launch instances from an Amazon EC2 Windows Server AMI with EC2 Fast Launch enabled, in order to perform provisioning steps. Additionally specify resource pattern that allows ec2:RunInstances for an AMI that's associated with License Manager.
- Stop and terminate an instance that was launched by EC2 Fast Launch after it creates the pre- provisioned snapshot.
- Describe image and instance type resources used to launch instances from an Amazon EC2 Windows Server AMI with EC2 Fast Launch enabled and create snapshots from them.
- Describe launch template resources and launch instances from a launch template.
- Describe instances, instance attributes and instance status, volumes and volume attributes.
- Describe network interfaces.
- Delete resources that EC2 Fast Launch created, including snapshots, launch templates, volumes and network interfaces.
- Tag resources that EC2 Fast Launch creates to launch and pre-provision, Windows instances, and create snapshots for the final launch process to consume.
- Amazon EventBridge – Includes access to create EventBridge event rules and retrieve details about or delete rules that it created. EC2 Fast Launch may also get a list of target services that

receive EC2 Fast Launch events that are forwarded based on event rules, and add target services to or remove them from event rules that it created.
- IAM – Allows EC2 Fast Launch to create the EC2FastLaunchServiceRolePolicy service- linked role, to get and use instance profiles whose name contains ec2fastlaunch, and to launch instances on your behalf using the instance profile from your launch template.
- AWS KMS – Includes access to create grants and list grants that were created by EC2 Fast Launch that can be retired. Also to describe or use keys for the purpose of encrypting or decrypting volumes attached to instances that EC2 Fast Launch creates, and to generate data keys that are not plaintext.
To view the permissions for this policy, see EC2FastLaunchServiceRolePolicy in the AWS Managed Policy Reference.
For more information about using managed policies for Amazon EC2, see AWS managed policies for Amazon EC2.
#### Create a service-linked role You don't need to create this service-linked role manually. When you start using EC2 Fast Launch for your AMI, Amazon EC2 creates the service-linked role for you, if it doesn't already exist.
If the service-linked role is deleted from your account, you can enable EC2 Fast Launch for another Windows AMI to re-create the role in your account. Alternatively, you can disable EC2 Fast Launch for your current AMI, and then enable it again. However, disabling the feature results in your AMI using the standard launch process for all new instances while Amazon EC2 removes all of your pre- provisioned snapshots. After all of the pre-provisioned snapshots are gone, you can enable using EC2 Fast Launch for your AMI again.
#### Access to customer managed keys To enable EC2 Fast Launch for an encrypted AMI that uses a customer managed key for encryption, you must grant the AWSServiceRoleForEC2FastLaunch role permission to use the CMK. To do this, call the create-grant command. For --grantee-principal, specify the ARN for the AWSServiceRoleForEC2FastLaunch role in your account. For --operations, specify CreateGrant. aws kms create-grant \ --key-id arn:aws:kms:us- east-1:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab \

    --grantee-principal arn:aws:iam::111122223333:role/AWSServiceRoleForEC2FastLaunch \ --operations CreateGrant
#### Edit a service-linked role Amazon EC2 does not allow you to edit the AWSServiceRoleForEC2FastLaunch service-linked role.
After you create a service-linked role, you can't change the name of the role, because various entities might reference the role. However, you can edit the description of the role by using IAM.
For more information, see Editing a service-linked role in the IAM User Guide.
#### Delete a service-linked role You can delete a service-linked role only after first deleting all of the related resources. This protects the Amazon EC2 resources that are associated with your Amazon EC2 Windows Server AMI with EC2 Fast Launch enabled, because you can't inadvertently remove permission to access the resources.
Use the IAM console, the AWS CLI, or the AWS API to delete the AWSServiceRoleForEC2FastLaunch service-linked role. For more information, see Delete a service- linked role in the IAM User Guide.
#### Supported Regions Amazon EC2 supports the EC2 Fast Launch service-linked role in all of the Regions where the Amazon EC2 service is available.
### Troubleshoot Windows EC2 Fast Launch
#### Troubleshooting scenarios The following scenarios can help you diagnose and fix common issues that you might encounter when you try to enable EC2 Fast Launch.
##### Unable to stop instance for snapshot creation Description When you enable EC2 Fast Launch, the service launches a set of instances that are used to create the pre-provisioned snapshots. Each instance is given 30 minutes to complete the process. If any of the instances complete successfully, then the service sets the Fast Launch status for the AMI to Enabled. However, if an instance fails to complete the process in the allotted time, and none of the other instances have completed the process, the service terminates all of the instances and sets

the Fast Launch status for the AMI to enabling_failed and the Fast Launch status reason to the following:
Unable to stop instance ID=i-1234567890abcdef0 for snapshot creation.
###### Cause Most often, this is caused by trying to enable EC2 Fast Launch for a Windows AMI that was created from a running instance, or an AMI that doesn't meet all of the EC2 Fast Launch prerequisites.
###### Solution Ensure that the AMI you use meets all EC2 Fast Launch prerequisites.
To configure EC2 Fast Launch for an AMI, you must create the AMI using Sysprep with the shutdown option. For more information, see Create an Amazon EC2 AMI using Windows Sysprep.
##### You've reached your VPC limit Description If you don't use a launch template to specify an existing VPC, and don't have a default VPC defined for your account, the service automatically creates an CloudFormation stack that includes a VPC and other resources, as described in EC2 Fast Launch prerequisites.
###### Cause You've reached the maximum number of VPCs that are allowed in your AWS account for the Region, and you have not specified an existing VPC for EC2 Fast Launch to use. This causes the process to fail.
###### Solution You can address this issue with either of the following options:
- You can request a quota increase
- You can provide a launch template that specifies an existing VPC To request an increase to the number of VPCs that your account can define per Region, follow these steps:
1. Open the Service Quotas console at https://console.aws.amazon.com/servicequotas/.

2. In the Service Console Dashboard, choose Amazon Virtual Private Cloud (Amazon VPC). This opens the VPC service quotas.
3. Filter on VPCs per Region to go directly to the quota.
4. Select VPCs per Region, and choose Request increase at account level.
If you have an urgent quota request, or if your quota increase request is denied, contact Support for assistance. For more information, see Requesting a quota increase in the Service Quotas User Guide.
##### Insufficient permissions to enable EC2 Fast Launch Description When you enable EC2 Fast Launch for the first time without specifying a Launch Template, EC2 Fast Launch creates a service-owned CloudFormation stack with service default resources. However, the CloudFormation templates will fail to deploy if your IAM principal (role or user) lacks the necessary permissions.
The log message might look something like the following:
Can't enable EC2 Fast Launch. The IAM credentials that you are using do not have sufficient permissions. Attach EC2FastLaunchFullAccess in the IAM console.
###### Cause Your IAM user or role lacks the necessary permissions to enable EC2 Fast Launch.
###### Solution Verify that your IAM principal (user or role) that enables EC2 Fast Launch has the EC2FastLaunchFullAccess policy attached. This AWS managed policy grants full access to all EC2 Fast Launch resources. To view the permissions for this policy, see the EC2FastLaunchFullAccess policy in the AWS Managed Policy Reference.
Change the Windows Administrator password for your Amazon EC2 instance If you launch your instance from an AWS Windows AMI, the launch agents that are pre-installed set the default password as follows:

- For Windows Server 2022 and later, EC2Launch v2 generates the default password.
- For Windows Server 2016 and 2019, the EC2Launch agent generates the default password.
- For Windows Server 2012 R2 and earlier, the EC2Config service generates the default password.
Note For Windows Server 2016 and later AMIs, Password never expires is disabled for the local administrator. For AMI versions prior to Windows Server 2016, Password never expires is enabled for the local administrator.
### Change the Administrator password after connecting When you connect to an instance the first time, we recommend that you change the Administrator password from its default value. Use the following procedure to change the Administrator password for a Windows instance.
Important Store the new password in a safe place. You won't be able to retrieve the new password using the Amazon EC2 console. The console can only retrieve the default password. If you attempt to connect to the instance using the default password after changing it, you'll get a "Your credentials did not work" error.
To change the local Administrator password
1. Connect to the instance and open a command prompt.
2. Run the following command. If your new password includes special characters, enclose the password in double quotes. net user Administrator "new_password"
3. Store the new password in a safe place.

### Change a lost or expired password If you lose your password or it expires, you can generate a new password. For password reset procedures, see Reset the Windows administrator password for an Amazon EC2 Windows instance.
## Add optional Windows Server components to Amazon EC2 Windows instances instances To access and install the optional components, you must find the correct EBS snapshot for your version of Windows Server, create a volume from the snapshot, and attach the volume to your instance.
Before you begin Use the AWS Management Console or a command line tool to get the instance ID and Availability Zone of your instance. You must create your EBS volume in the same Availability Zone as your instance.
Use one of the following procedures to add Windows Server components to your instance.
Console To add Windows components to your instance
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Snapshots.
3. From the Filter bar, choose Public snapshots.
4. Add the Owner Alias filter and choose amazon.
5. Add the Description filter and enter Windows.
6. Press Enter
7. Select the snapshot that matches your system architecture and language preference. For example, select Windows 2019 English Installation Media if your instance is running Windows Server 2019.
8. Choose Actions, Create volume from snapshot.
9. For Availability Zone, select the Availability Zone that matches your Windows instance.
Choose Add tag and enter Name for the tag key and a descriptive name for the tag value.
Choose Create volume.

10. In the Successfully created volume message (green banner), choose the volume that you just created.
11. Choose Actions, Attach volume.
12. From Instance, select the instance ID.
13. For Device name, enter the name of the device for the attachment. If you need help with the device name, see Device names for volumes on Amazon EC2 instances.
14. Choose Attach volume.
15. Connect to your instance and make the volume available. For more information, see Make an Amazon EBS volume available for use in the Amazon EBS User Guide.
Important Do not initialize the volume.
16. Open Control Panel, Programs and Features. Choose Turn Windows features on or off.
If you are prompted for installation media, specify the EBS volume with the installation media.
17. (Optional) When you are finished with the installation media, you can detach the volume.
After you detach the volume, you can delete it.
AWS CLI To add Windows components to your instance
1. Use the describe-snapshots command with the owner-ids parameter and description filter to get a list of the available installation media snapshots. aws ec2 describe-snapshots \ --owner-ids amazon \ --filters Name=description,Values=Windows*
2. In the output, note the ID of the snapshot that matches your system architecture and language preference. For example:
{ "Snapshots": [ ...
        {

            "OwnerAlias": "amazon", "Description": "Windows 2019 English Installation Media", "Encrypted": false, "VolumeId": "vol-be5eafcb", "State": "completed", "VolumeSize": 6, "Progress": "100%", "StartTime": "2019-10-25T20:00:47.000Z", "SnapshotId": "snap-22da283e", "OwnerId": "123456789012"
        }, ...
   ]
}
3. Use the create-volume command to create a volume from the snapshot. Specify the same Availability Zone as your instance. aws ec2 create-volume \ --snapshot-id snap-0abcdef1234567890 \ --volume-type gp2 \ --availability-zone us-east-1a
4. In the output, note the volume ID.
{ "AvailabilityZone": "us-east-1a", "Encrypted": false, "VolumeType": "gp2", "VolumeId": "vol-01234567890abcdef", "State": "creating", "Iops": 100, "SnapshotId": "snap-0abcdef1234567890", "CreateTime": "2017-04-18T10:33:10.940Z", "Size": 6 }
5. Use the attach-volume command to attach the volume to your instance. aws ec2 attach-volume \ --volume-id vol-0c98b37f30bcbc290 \ --instance-id i-01474ef662b89480 \

    --device xvdg
6. Connect to your instance and make the volume available. For more information, see Make an Amazon EBS volume available for use in the Amazon EBS User Guide.
Important Do not initialize the volume.
7. Open Control Panel, Programs and Features. Choose Turn Windows features on or off.
If you are prompted for installation media, specify the EBS volume with the installation media.
8. (Optional) When you are finished with the installation media, use the detach-volume command to detach the volume from your instance. After you detach the volume, you can use the delete-volume command to delete the volume.
PowerShell To add Windows components to your instance
1. Use the Get-EC2Snapshot cmdlet with the Owner and description filters to get a list of the available installation media snapshots.
Get-EC2Snapshot `
    -Owner amazon `
    -Filter @{ Name="description"; Values="Windows*" }
2. In the output, note the ID of the snapshot that matches your system architecture and language preference. For example:
...
DataEncryptionKeyId :
Description         : Windows 2019 English Installation Media Encrypted           : False KmsKeyId            :
OwnerAlias          : amazon OwnerId             : 123456789012 Progress            : 100% SnapshotId          : snap-0abcdef1234567890 StartTime           : 10/25/2019 8:00:47 PM

State               : completed StateMessage        :
Tags                : {} VolumeId            : vol-01234567890abcdef VolumeSize          : 6 ...
3. Use the New-EC2Volume cmdlet to create a volume from the snapshot. Specify the same Availability Zone as your instance.
New-EC2Volume `
    -AvailabilityZone us-east-1a `
    -VolumeType gp2 `
    -SnapshotId snap-0abcdef1234567890
4. In the output, note the volume ID.
Attachments      : {} AvailabilityZone : us-east-1a CreateTime       : 4/18/2017 10:50:25 AM Encrypted        : False Iops             : 100 KmsKeyId         :
Size             : 6 SnapshotId       : snap-0abcdef1234567890 State            : creating Tags             : {} VolumeId         : vol-01234567890abcdef VolumeType       : gp2
5. Use the Add-EC2Volume cmdlet to attach the volume to your instance.
Add-EC2Volume `
    -InstanceId i-1234567890abcdef0 `
    -VolumeId vol-01234567890abcdef `
    -Device xvdh
6. Connect to your instance and make the volume available. For more information, see Make an Amazon EBS volume available for use in the Amazon EBS User Guide.

Important Do not initialize the volume.
7. Open Control Panel, Programs and Features. Choose Turn Windows features on or off.
If you are prompted for installation media, specify the EBS volume with the installation media.
8. (Optional) When you are finished with the installation media, use the Dismount-EC2Volume cmdlet to detach the volume from your instance. After you detach the volume, you can use the Remove-EC2Volume cmdlet to delete the volume.
## Install Windows Subsystem for Linux on your EC2 Windows instance The Windows Subsystem for Linux (WSL) is a feature of Microsoft Windows. By installing WSL on your EC2 Windows instance, you can run native Linux tools directly on your Windows instance.
There are two versions of Windows Subsystem for Linux (WSL): WSL 1 and WSL 2. For more information, see Windows Subsystem for Linux Documentation on the Microsoft website.
Requirements
- The operating system must be Windows Server 2019 or later.
- You can only install WSL 1 on virtualized Windows instances (the instance size is not .metal or does not support nested virtualization).
- You can install either WSL 1 or WSL 2 on instances that support nested virtualization and have the NestedVirtualization CPU Option enabled.
- You can install either WSL 1 or WSL 2 on bare metal instances (the instance size is .metal). Bare metal instances provide the required support for nested virtualization by default.
For more information about nested virtualization for EC2, see Use nested virtualization to run hypervisors in Amazon EC2 instances.

### Install WSL on your Windows instance To install WSL 1
1. Install WSL. The process that you'll use depends on the version of Windows Server running on the instance.
- Windows Server 2022 and later - Run the following standard installation command on your EC2 instance. wsl --install --enable-wsl1 --no-launch
- Windows Server 2019 - Enable WSL and then install WSL as described in Install WSL on previous versions of Windows Server on the Microsoft website.
2. Restart your EC2 instance. shutdown -r -t 20
3. To configure WSL to use WSL 1, run the following command on your instance. This step is required for virtualized instances (the instance size is not .metal or not configured for nested virtualization). wsl --set-default-version 1
4. Install the default distribution. wsl --install To install WSL 2 (.metal or instances with nested virtualization enabled)
Run the following standard installation command on your EC2 instance. By default, WSL 2 is installed. wsl --install
## EC2 Windows troubleshooting utilities The EC2WinUtil driver provides the following types of troubleshooting support for your Windows instance.

Crash call stacks EC2WinUtil collects basic crash information from your instance and writes it out to the serial console. The following list includes some of the key details that the utility writes to the console.
- Identification of the module that generated the fault.
- The Windows error code associated with the event.
- A stack trace of the most recent calls.
With these details, you can perform initial root cause analysis and determine if further analysis is needed. Output to the serial console also enables AWS to track crash trends for Amazon EC2 drivers, and diagnose large scale crash events.
Note EC2WinUtil doesn't collect any customer data in its crash call stacks.
Hibernate/resume stability EC2WinUtil tracks the virtualization settings of the instance across hibernate/resume cycles.
This helps to improve the long-term stability of instances that have enabled hibernation.
For driver release notes, see EC2 Windows Utility Driver version history
### EC2 Windows Utility Driver version history The following table shows which EC2WinUtil drivers run on each version of Windows Server on Amazon EC2. Earlier versions of the operating system use the driver that's preinstalled on AWS Windows Server AMIs that the instance launched from. AMIs that are shared with you or that you subscribe to through AWS Marketplace don't have the driver preinstalled.
Windows Server version EC2WinUtil driver version Windows Server 2025 latest version Windows Server 2022 latest version Windows Server 2019 latest version

Windows Server version EC2WinUtil driver version Windows Server 2016 latest version Note Prior to driver version 3.0.0, the EC2WinUtil driver was not available to download for manual installation. Earlier versions were only available as preinstalled drivers for AWS Windows AMIs.
The following table describes the released versions of the EC2WinUtil driver.
Package version Driver version Details Release date 3.1.0 3.1.0 Improved power management event handling.
Feb 4, 2026 3.0.0 3.0.0 Modernized the driver for Windows 10 and added support for installation as a primitive driver.
June 13, 2024 2.0.0 2.0.0 Added support for output on MMIO serial ports for metal instance types. Also improved crash parsing and updated the output format.
August 23, 2018 1.0.1 1.0.1 Changed the driver name to EC2WinUtil  due to a namespace conflict with Amazon Inspector. Several bug fixes are included.
March 1, 2018 1.0.0 1.0.0 Initial release. The driver was initially called AwsAgent.
November 28, 2017
