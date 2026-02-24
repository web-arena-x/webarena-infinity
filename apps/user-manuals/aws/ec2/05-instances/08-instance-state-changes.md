# Amazon EC2 instance state changes

Source: apps/user-manuals/aws/ec2-ug.pdf

---

Name Default Adjustable Maximum number of EC2 Instance Connect Endpoints per VPC 1 No Maximum number of EC2 Instance Connect Endpoints per subnet 1 No Maximum number of concurrent connections per EC2 Instance Connect Endpoint 20 No
# Amazon EC2 instance state changes An Amazon EC2 instance transitions through different states from the moment you launch it through to its termination.
The following illustration represents the transitions between instance states.

You can receive notifications when your instances change states. For more information, see the section called "State change events".
## Billing by instance state The following table provides a brief description of each instance state and indicates whether instance usage is billed. Some AWS resources, such as Amazon EBS volumes and Elastic IP addresses, incur charges regardless of the instance's state. For more information, see Avoiding Unexpected Charges in the AWS Billing User Guide.
Instance state Description Instance usage billing pending The instance is preparing to enter the running Not billed

Instance state Description Instance usage billing state. An instance enters the pending state when it is launched or when it is started  after being in the stopped state. running The instance is running and ready for use.
Billed stoppingThe instance is preparing to be stopped.
Not billed Note If you hibernate an instance, you're billed while the instance is in the   stopping state. stopped The instance is shut down and cannot be used. The instance can be started at any  time.
Not billed shutting- down The instance is preparing to be terminated.
Not billed terminate d The instance has been permanently deleted and cannot be started.
Not billed Note Reserved Instances that applied to terminated instances are billed until the end of  their term according to their payment option. For more information,  see Reserved Instances for Amazon EC2 overview

## Pending instances When you launch an instance, it enters the pending state. The instance type that you specified at launch determines the hardware of the host computer for your instance. We use the Amazon Machine Image (AMI) you specified at launch to boot the instance. After the instance is ready for you, it enters the running state. You can connect to your running instance and use it the way that you'd use a computer sitting in front of you.
As soon as your instance transitions to the running state, you're billed for each second, with a one-minute minimum, that you keep the instance running, even if the instance remains idle and you don't connect to it.
## Stopped instances If your instance fails a status check or is not running your applications as expected, and if the root volume of your instance is an Amazon EBS volume, you can stop and start your instance to try to fix the problem.
When you stop your instance, it enters the stopping state, and then the stopped state. You are not charged for usage or data transfer fees for your instance when it is stopped. Charges are incurred for the storage of any Amazon EBS volumes. While your instance is in the stopped state, you can modify certain attributes of the instance, including the instance type.
When you start your instance, it enters the pending state, and the instance is moved to a new host computer (though in some cases, it remains on the current host). When you stop and start your instance, you lose any data on the instance store volumes attached to the previous host computer.
Your instance retains its private IPv4 address, which means that an Elastic IP address associated with the private IPv4 address or network interface remains associated with your instance. If your instance has an IPv6 address, it retains the IPv6 address.
Each time you transition an instance from stopped to running, you are charged per second when the instance is running, with a minimum of one minute per instance start.
For more details about stopping and starting an instance, see Stop and start Amazon EC2 instances.
## Hibernated instances When you hibernate an instance, we signal the operating system to perform hibernation (suspend- to-disk), which saves the contents from the instance memory (RAM) to your Amazon EBS root

volume. We persist the instance's Amazon EBS root volume and any attached Amazon EBS data volumes. When you start your instance, the Amazon EBS root volume is restored to its previous state and the RAM contents are reloaded. Previously attached data volumes are reattached and the instance retains its instance ID.
When you hibernate your instance, it enters the stopping state, and then the stopped state. We don't charge usage for a hibernated instance when it is in the stopped state, but we do charge while it is in the stopping state, unlike when you stop an instance without hibernating it. We don't charge usage for data transfer fees, but we do charge for the storage for any Amazon EBS volumes, including storage for the RAM data.
When you start your hibernated instance, it enters the pending state, and we move the instance to a new host computer (though in some cases, it remains on the current host).
Your instance retains its private IPv4 address, which means that an Elastic IP address associated with the private IPv4 address or network interface is still associated with your instance. If your instance has an IPv6 address, it retains its IPv6 address.
For more information, see Hibernate your Amazon EC2 instance.
## Rebooting instances You can reboot your instance using the Amazon EC2 console, a command line tool, and the Amazon EC2 API. We recommend that you use Amazon EC2 to reboot your instance instead of running the operating system reboot command from your instance.
Rebooting an instance is equivalent to rebooting an operating system. The instance remains on the same host computer and maintains its public DNS name, private IP address, and any data on its instance store volumes. It typically takes a few minutes for the reboot to complete, but the time it takes to reboot depends on the instance configuration.
Rebooting an instance doesn't start a new instance billing period; per second billing continues without a further one-minute minimum charge.
For more information, see Reboot your Amazon EC2 instance.
## Terminated instances When you've decided that you no longer need an instance, you can terminate it. As soon as the status of an instance changes to shutting-down or terminated, you stop incurring charges for that instance.

If you enable termination protection, you can't terminate the instance using the console, CLI, or API.
After you terminate an instance, it remains visible in the console for a short while, and then the entry is automatically deleted. You can also describe a terminated instance using the CLI and API.
Resources (such as tags) are gradually disassociated from the terminated instance, therefore may no longer be visible on the terminated instance after a short while. You can't connect to or recover a terminated instance.
Each Amazon EBS-backed instance supports the InstanceInitiatedShutdownBehavior attribute, which controls whether the instance stops or terminates when you initiate shutdown from within the instance itself (for example, by using the shutdown command on Linux). The default behavior is to stop the instance. You can modify the setting of this attribute while the instance is running or stopped.
Each Amazon EBS volume supports the DeleteOnTermination attribute, which controls whether the volume is deleted or preserved when you terminate the instance it is attached to. The default is to delete the root volume and preserve any other EBS volumes.
For more information, see Terminate Amazon EC2 instances.
## Differences between instance states The following table summarizes the key differences between rebooting, stopping, hibernating, and terminating your instance.
Character istic Reboot Stop/start (Amazon EBS- backed instances only)
Hibernate (Amazon EBS-backed instances only)
Terminate Host computer The instance stays on the same host computer.
We move the instance to a new host computer (though in some cases, it remains on the current host).
We move the instance to a new host computer (though in some cases, it remains on the current host).
None

Character istic Reboot Stop/start (Amazon EBS- backed instances only)
Hibernate (Amazon EBS-backed instances only)
Terminate Private IPv4 address The instance keeps its private IPv4 address.
The instance keeps its private IPv4 address.
The instance keeps its private IPv4 address.
None Public IPv4 address The instance keeps its public IPv4 address.
The instance gets a new public IPv4 address, unless it has a  secondary network interface or a secondary private IPv4 address that  is associated with an Elastic IP address.
The instance gets a new public IPv4 address, unless it has a  secondary network interface or a secondary private IPv4 address that  is associated with an Elastic IP address.
None Elastic IP address (IPv4)
The Elastic IP address remains associated with the instance The Elastic IP address remains associated with the instance The Elastic IP address remains associated with the instance The Elastic IP address is disassoci ated from the instance IPv6 address The instance keeps its IPv6 address The instance keeps its IPv6 address The instance keeps its IPv6 address None Instance store volumes The data is preserved The data is erased The data is erased The data is erased Root volume The volume is preserved The volume is preserved The volume is preserved The volume is deleted by default

Character istic Reboot Stop/start (Amazon EBS- backed instances only)
Hibernate (Amazon EBS-backed instances only)
Terminate RAM (contents of memory)
The RAM is erased The RAM is erased The RAM is saved to a file on the root volume The RAM is erased Billing The instance billing hour doesn't change You stop incurring charges for an instance as soon as its state changes to   stopping.
Each time an instance transitio ns from   stopped to running, we start a new  instan ce billing period, billing a minimum of one minute every time  you start your instance.
You incur charges while the instance is in the stopping state, but stop incurring charges when the instance is in the stopped state. Each time an instance transitions from stopped to running, we start a new instance billing period, billing a minimum of one minute every time you start your  inst ance.
You stop incurring charges for an instance as soon as its state  changes to shutting- down Operating system shutdown commands always terminate an instance with an instance store root volume. You can control whether operating system shutdown commands stop or terminate an instance with an EBS root volume. For more information, see Change instance initiated shutdown behavior.

## Stop and start Amazon EC2 instances You can stop and start your instance if it has an Amazon EBS volume as its root volume. When you stop an instance, it shuts down. When you start an instance, it is typically migrated to a new underlying host computer and assigned a new public IPv4 address.
An instance stop can be user-initiated (where you manually stop the instance) or initiated by AWS (in response to a scheduled stop event when AWS detects irreparable failure of the underlying host for your instance).
For user-initiated stops, we recommend using the Amazon EC2 console, CLI, or API instead of running the operating system stop command from your instance. When using Amazon EC2, if the instance does not cleanly shut down within a few minutes, Amazon EC2 performs a hard shut down. Furthermore, AWS CloudTrail creates an API record of when your instance was stopped.
This topic describes how to perform a user-initiated stop. For information about a stop performed by AWS, see Manage Amazon EC2 instances scheduled to stop or retire.
When you stop an instance, it is not deleted. If you decide that you no longer need an instance, you can terminate it. For more information, see Terminate Amazon EC2 instances. If you want to hibernate an instance to save the contents from the instance memory (RAM), see Hibernate your Amazon EC2 instance. For distinctions between instance lifecycle actions, see Differences between instance states.
Contents
- How EC2 instance stop and start works
- Methods for stopping an instance
- Manually stop and start your instances
- Automatically stop and start your instances
- Find all running and stopped instances
- Find the initial and most recent launch times
- Enable stop protection for your EC2 instances

### How EC2 instance stop and start works When you stop an Amazon EC2 instance, changes are registered at the operating system (OS) level of the instance, some resources are lost, and some resources persist. When you start an instance, changes are registered at the instance level.
Topics
- What happens when you stop an instance
- What happens when you start an instance
- Test application response to stop and start
- Costs related to instance stop and start
#### What happens when you stop an instance The following describes what typically happens when you stop an instance using the default stop method. Note that some aspects might vary depending on which stop method you use.
Changes registered at the OS level
- The API request sends a button press event to the guest.
- Various system services are stopped as a result of the button press event. Graceful OS shutdown is triggered by the ACPI shutdown button press event from the hypervisor.
- ACPI shutdown is initiated.
- The instance shuts down when the graceful OS shutdown process exits. There is no configurable OS shutdown time.
- If the instance OS does not cleanly shut down within a few minutes, a hard shutdown is performed.
- The instance stops running.
- The instance state changes to stopping and then stopped.
- [Auto Scaling] If your instance is in an Auto Scaling group, when the instance is in any Amazon EC2 state other than running, or if its status for the status checks becomes impaired, Amazon EC2 Auto Scaling considers the instance to be unhealthy and replaces it. For more information, see Health checks for instances in an Auto Scaling group in the Amazon EC2 Auto Scaling User Guide.
- [Windows instances] When you stop and start a Windows instance, the launch agent performs tasks on the instance, such as changing the drive letters for any attached Amazon EBS volumes.

For more information about these defaults and how you can change them, see the section called "EC2Launch v2".
Resources lost
- Data stored on the RAM.
- Data stored on the instance store volumes.
- The public IPv4 address that Amazon EC2 automatically assigned to the instance upon launch or start. To retain a public IPv4 address that never changes, you can associate an Elastic IP address with your instance.
Resources that persist
- Any attached Amazon EBS root and data volumes.
- Data stored on the Amazon EBS volumes.
- Any attached network interfaces.
A network interface includes the following resources, which also persist:
- Private IPv4 addresses.
- IPv6 addresses.
- Elastic IP addresses associated with the instance. Note that when the instance is stopped, you are charged for the associated Elastic IP addresses.
The following diagram illustrates what persists and what is lost when an EC2 instance is stopped.
The diagram is divided into three parts: the first part, labeled Running EC2 instance, shows the instance in the running state with its resources. The second part, labeled Stopped EC2 instance, shows the instance in the stopped state with the resources that persist. The third part, labeled Lost, shows the resources that are lost when the instance is stopped.

For information about what happens when you stop a Mac instance, see Stop or terminate your Amazon EC2 Mac instance.
#### What happens when you start an instance
- In most cases, the instance is migrated to a new underlying host computer (though in some cases, such as when an instance is allocated to a host in a Dedicated Host configuration, it remains on the current host).
- The associated EBS volumes and network interfaces are reattached to the instance.
- Amazon EC2 assigns a new public IPv4 address to the instance if the instance is configured to receive a public IPv4 address, unless it has a secondary network interface or a secondary private IPv4 address that is associated with an Elastic IP address.
- If you stop an instance in a placement group and then start it again, it still runs in the placement group. However, the start fails if there isn't enough capacity for the instance. If you receive a capacity error when starting an instance in a placement group that already has running instances, stop all the instances in the placement group and start them all again. Starting the instances may migrate them to hardware that has capacity for all of the requested instances.

#### Test application response to stop and start You can use AWS Fault Injection Service to test how your application responds when your instance is stopped and started. For more information, see the AWS Fault Injection Service User Guide.
#### Costs related to instance stop and start The following costs are associated with stopping and starting an instance.
Stopping – As soon as the state of an instance changes to shutting-down or terminated, charges are no longer incurred for the instance. You are not charged for usage or data transfer fees for a stopped instance. Charges are incurred to store Amazon EBS storage volumes.
Starting – Each time you start a stopped instance, you are charged for a minimum of one minute of usage. After one minute, you are charged for only the seconds you use. For example, if you run an instance for 20 seconds and then stop it, you are charged for a minute of usage. If you run an instance for 3 minutes and 40 seconds, you are charged for 3 minutes and 40 seconds of usage.
### Methods for stopping an instance There are four ways to perform a user-initiated stop: default stop, stop with skip OS shutdown, force stop, and force stop with skip OS shutdown. The following table compares the key differences between the stop methods:
Stop method Key purpose Use case CLI command Default stop Normal instance shutdown with attempted graceful OS shutdown.
Typical instance stop. aws ec2 stop- instances \ --instance- id i-1234567 890abcdef0 Stop with skip OS shutdown Bypasses the graceful OS shutdown when stopping an instance.
When bypassing graceful OS shutdown is required. aws ec2 stop- instances \ --instance- id i-1234567 890abcdef0 \

Stop method Key purpose Use case CLI command --skip-os- shutdown Force stop Handles stuck instances.
Attempts a default stop first; if instance fails to stop, then forcibly stops the instance.
When instance is stuck in stopping state. aws ec2 stop- instances \ --instance- id i-1234567 890abcdef0 \ --force Force stop with skip OS shutdown Force stops and bypasses the graceful OS shutdown when stopping an  instance.
When force stop and bypassing graceful OS shutdown is required. aws ec2 stop- instances \ --instance- id i-1234567 890abcdef0 \ --force \ --skip-os- shutdown For instructions on how to use each method, see the following:
- Stop an instance with a graceful OS shutdown
- Stop an instance and bypass the graceful OS shutdown
- Force stop an instance Stop methods:
- Default stop
- Stop with skip OS shutdown
- Force stop
- Force stop with skip OS shutdown

The following sections provide more detailed information about the four different user-initiated stop methods.
#### Default stop The default stop method is the standard way to stop an instance. When you issue the StopInstances command, the instance transitions from the running state, to stopping, and finally to stopped, as illustrated by the following diagram:
Purpose: Normal instance shutdown with attempted graceful OS shutdown.
Data impact: Preserves data on the EBS root volume and data volumes. Loses data on the instance store volume.
When to use: First stop attempt for typical stops.
Note If you've already attempted a stop with skip OS shutdown, a subsequent default stop attempt during the same state transition session will not perform a graceful OS shutdown.
Bypassing the graceful OS shutdown is irreversible for the instance's current session.
#### Stop with skip OS shutdown When bypassing the graceful OS shutdown is required, the stop with skip OS shutdown method can be used to stop an instance and bypass the graceful OS shutdown, as illustrated by the following diagram:

Warning Bypassing the graceful OS shutdown might result in data loss or corruption (for example, memory contents not flushed to disk or loss of in-flight IOs) or skipped shutdown scripts.
Purpose: Bypass the graceful OS shutdown when stopping an instance.
Data impact: Might result in data loss or corruption. Contents of memory might not be flushed to disk and in-flight IOs might be lost. Might skip shutdown scripts.
When to use: When bypassing the graceful OS shutdown is required. If used while a default stop with graceful OS shutdown is in progress, the graceful OS shutdown will be bypassed.
Note Bypassing the graceful OS shutdown is irreversible for the instance's current state transition session. A subsequent default stop attempt during this session will not attempt a graceful OS shutdown.
#### Force stop The force stop method is used to handle instances that are stuck in the stopping state. An instance typically becomes stuck due to an underlying hardware issue (indicated by a failed system status check).
The force stop method first attempts a default stop. If the instance remains stuck in the stopping state, the force parameter forcibly shuts down the instance and transitions the instance to the stopped state, as indicated by the following diagram:
Purpose: Handles instances stuck in the stopping state. Attempts a default stop first. If the instance fails to stop, then forcibly shuts down the instance.

Data impact: Attempts a default stop first, but if force stop goes ahead, then might cause data loss or corruption. In rare cases, results in post-stop writes to EBS volumes or other shared resources.
When to use: Second stop attempt when an instance remains stuck after a default stop. For more information, see Troubleshoot Amazon EC2 instance stop issues.
#### Force stop with skip OS shutdown When force stopping and bypassing the graceful OS shutdown is required, the force stop with skip OS shutdown method can be used to bring an instance to the stopped state, as illustrated in the following diagram:
Purpose: Combines force stop with bypassing a graceful OS shutdown when stopping an instance.
Data impact: Skip OS shutdown might result in data loss or corruption. Contents of memory might not be flushed to disk and in-flight IOs might be lost. Might skip shutdown scripts. If force stop goes ahead, then might cause additional data loss or corruption. In rare cases, results in post-stop writes to the EBS volumes or other shared resources.
When to use: When you want to be sure that your instance will stop and you want to bypass the graceful OS shutdown. If used while a default stop with graceful OS shutdown is in progress, the graceful OS shutdown will be bypassed.
### Manually stop and start your instances You can stop and start your Amazon EBS-backed instances (instances with EBS root volumes). You can't stop and start instances with an instance store root volume.
When using the default method to stop an instance, a graceful operating system (OS) shutdown is attempted. You can bypass the graceful OS shutdown; however, this might risk data integrity.

Warning When you stop an instance, the data on any instance store volumes is erased. Before you stop an instance, verify that you've copied any data that you need from the instance store volumes to persistent storage, such as Amazon EBS or Amazon S3.
[Linux instances] Using the OS halt command from an instance does not initiate a shutdown. If you use the halt command, the instance does not terminate; instead, it places the CPU into HLT, which suspends CPU operation. The instance remains running.
You can initiate a shutdown using the OS shutdown or poweroff commands. When you use an OS command, the instance stops by default. You can change this behavior. For more information, see Change instance initiated shutdown behavior.
Note If you stopped an Amazon EBS-backed instance and it appears "stuck" in the stopping state, you can forcibly stop it. For more information, see Troubleshoot Amazon EC2 instance stop issues.
Stop and start methods
- Stop an instance with a graceful OS shutdown
- Stop an instance and bypass the graceful OS shutdown
- Start an instance
#### Stop an instance with a graceful OS shutdown You can stop an instance using the default stop method, which includes an attempt at a graceful OS shutdown. For more information, see Default stop.
Console To stop an instance using the default stop method
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.

2. In the left navigation pane, choose Instances, and then select the instance.
3. Choose Instance state, Stop instance. If this option is disabled, either the instance is already stopped or its root volume is an instance store volume.
4. When prompted for confirmation, choose Stop. It can take a few minutes for the instance to stop.
AWS CLI To stop an instance using the default stop method Use the stop-instances command. aws ec2 stop-instances --instance-ids i-1234567890abcdef0 PowerShell To stop an instance using the default stop method Use the Stop-EC2Instance cmdlet Stop-EC2Instance -InstanceId i-1234567890abcdef0
#### Stop an instance and bypass the graceful OS shutdown You can bypass the graceful OS shutdown when stopping an instance. For more information, see Stop with skip OS shutdown.
Warning Bypassing the graceful OS shutdown might result in data loss or corruption (for example, memory contents not flushed to disk or loss of in-flight IOs) or skipped shutdown scripts.
Console To stop an instance and bypass the graceful OS shutdown
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.

2. In the navigation pane, choose Instances and select the instance.
3. Choose Instance state, Stop instance.
4. Under Skip OS shutdown, select the Skip OS shutdown checkbox. If you don't see this option in the console, it's not yet available in the console in the current Region. You can, however, access this feature using the AWS CLI or SDK, or try another Region in the console.
5. Choose Stop.
AWS CLI To stop an instance and bypass the graceful OS shutdown Use the stop-instances command with --skip-os-shutdown. aws ec2 stop-instances \ --instance-ids i-1234567890abcdef0 \ --skip-os-shutdown PowerShell To stop an instance and bypass the graceful OS shutdown Use the Stop-EC2Instance cmdlet with -SkipOsShutdown $true.
Stop-EC2Instance `
    -InstanceId i-1234567890abcdef0 `
    -SkipOsShutdown $true
#### Start an instance You can start a stopped instance.
Console To start an instance
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the left navigation pane, choose Instances.
3. Select the instance, and choose Instance state, Start instance.

It can take a few minutes for the instance to enter the running state.
AWS CLI To start an instance Use the start-instances command. aws ec2 start-instances --instance-ids i-1234567890abcdef0 PowerShell To start an instance Use the Start-EC2Instance cmdlet.
Start-EC2Instance -InstanceId i-1234567890abcdef0
### Automatically stop and start your instances You can automate stopping and starting instances with the following services:
Instance Scheduler on AWS You can use Instance Scheduler on AWS to automate the starting and stopping of EC2 instances. For more information, see How do I use Instance Scheduler with CloudFormation to schedule EC2 instances? Note that additional charges apply.
AWS Lambda and an Amazon EventBridge rule You can use Lambda and an EventBridge rule to stop and start your instances on a schedule. For more information, see How do I use Lambda to stop and start Amazon EC2 instances at regular intervals?
Amazon EC2 Auto Scaling To ensure you have the correct number of Amazon EC2 instances available to handle the load for an application, create Auto Scaling groups. Amazon EC2 Auto Scaling ensures that your application always has the right capacity to handle the traffic demand, and saves costs by launching instances only when they are needed. Note that Amazon EC2 Auto Scaling

terminates, rather than stops, unneeded instances. To set up Auto Scaling groups, see Get started with Amazon EC2 Auto Scaling.
### Find all running and stopped instances You can find all of your running and stopped instances across all AWS Regions on a single page using Amazon EC2 Global View. This capability is especially useful for taking inventory and finding forgotten instances. For information about how to use Global View, see View resources across Regions using AWS Global View.
Alternatively, you can run a command or cmdlet in each Region where you have instances.
AWS CLI To get the number of EC2 instances in a Region Use the following describe-instances command to count the instances in the current Region.
You must run this command in each Region where you have instances. aws ec2 describe-instances \ --region us-east-2 \ --query "length(Reservations[].Instances[])"
The following is example output.
27 To get summary info about your EC2 instances in a Region Use the following describe-instances command. You must run this command in each Region where you have instances. aws ec2 describe-instances \ --region us-east-2 \ --query "Reservations[].Instances[].[InstanceId,InstanceType,PrivateIpAddress]"
 \ --output table The following is example output.

---------------------------------------------------------
|                   DescribeInstances                   | +---------------------+---------------+-----------------+
|  i-0e3e777f4362f1bf7|  t2.micro     |  10.0.12.9      |
|  i-09453945dcf1529e9|  t2.micro     |  10.0.143.213   |
|  i-08fd74f3f1595fdbd|  m7i.4xlarge  |  10.0.1.103     | +---------------------+---------------+-----------------+ PowerShell To get the number of EC2 instances in a Region Use the Get-EC2Instance cmdlet.
(Get-EC2Instance -Region us-east-2).Instances.Length The following is example output.
27 To get summary info about your EC2 instances in a Region Use the Get-EC2Instance cmdlet. You must run this command in each Region where you have instances.
(Get-EC2Instance).Instances | Select InstanceId, InstanceType, PrivateIpAddress The following is example output.
InstanceId          InstanceType PrivateIpAddress ----------          ------------ ---------------- i-0e3e777f4362f1bf7 t2.micro     10.0.12.9 i-09453945dcf1529e9 t2.micro     10.0.143.213 i-08fd74f3f1595fdbd m7i.4xlarge  10.0.1.103
### Find the initial and most recent launch times When you describe an instance, the launch time for the instance is its most recent launch time.
After you stop and start an instance, the launch time reflects the new instance start time. To find

the initial launch time for an instance, even after stopping and starting it, view the time at which the primary network interface was attached to the instance.
Console To find the most recent launch time Select the instance and find Launch time under Instance details on the Details tab.
To find the initial launch time Select the instance and find the primary network interface (device index is 0) under Network interfaces on the Networking tab.
AWS CLI To find the initial and most recent launch times Use the following describe-instances command to display both the initial launch time and the most recent launch time for the specified instance. aws ec2 describe-instances \ --instance-id i-1234567890abcdef0 \ --query 'Reservations[].Instances[].
{InstanceID:InstanceId,InitialLaunch:NetworkInterfaces[0].Attachment.AttachTime,LastLaunch:L The following is example output.
[ { "InstanceID": "i-1234567890abcdef0", "InitialLaunch": "2024-04-19T00:47:08+00:00", "LastLaunch": "2024-05-27T06:24:06+00:00"
    } ]
PowerShell To find the most recent launch time Use the Get-EC2Instance cmdlet.

(Get-EC2Instance -InstanceId i-1234567890abcdef0).Instances.LaunchTime The following is example output.
Monday, May 27, 2024 6:24:06 AM To find the initial launch time Use the Get-EC2Instance cmdlet.
(Get-EC2Instance - InstanceId i-1234567890abcdef0).Instances.NetworkInterfaces.Attachment.AttachTime The following is example output.
Friday, April 19, 2024 12:47:08 AM
### Enable stop protection for your EC2 instances To prevent an instance from being accidentally stopped, you can enable stop protection for the instance. Stop protection also protects your instance from accidental termination.
The DisableApiStop attribute of the Amazon EC2 ModifyInstanceAttribute API controls whether the instance can be stopped by using the Amazon EC2 console, the AWS CLI, or the Amazon EC2 API. You can set the value of this attribute when you launch the instance, while the instance is running, or while the instance is stopped.
#### Considerations
- Enabling stop protection does not prevent you from accidentally stopping an instance by initiating a shutdown from the instance using an operating system command such as shutdown or poweroff.
- Enabling stop protection does not prevent AWS from stopping the instance when there is a scheduled event to stop the instance.
- Enabling stop protection does not prevent Amazon EC2 Auto Scaling from terminating an instance when the instance is unhealthy or during scale-in events. You can control whether an Auto Scaling group can terminate a particular instance when scaling in by using instance scale-in protection.

- Stop protection not only prevents your instance from being accidentally stopped, but also from accidental termination when using the console, AWS CLI, or API. However, it does not automatically set the DisableApiTermination attribute. Note that when the DisableApiStop attribute is set to false, the DisableApiTermination attribute setting determines whether the instance can be terminated using the console, AWS CLI, or API. For more information see Terminate Amazon EC2 instances.
- You can't enable stop protection for an instance with an instance store root volume.
- You can't enable stop protection for Spot Instances.
- The Amazon EC2 API follows an eventual consistency model when you enable or disable stop protection. This means that the result of running commands to set the stop protection attribute might not be immediately visible to all subsequent commands you run. For more information, see Eventual consistency in the Amazon EC2 Developer Guide.
Stop protection tasks
- Enable stop protection for an instance at launch
- Enable stop protection for a running or stopped instance
- Disable stop protection for a running or stopped instance
#### Enable stop protection for an instance at launch You can enable stop protection for an instance when launching the instance.
Console To enable stop protection for an instance at launch
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. On the dashboard, choose Launch instance.
3. Configure your instance in the new launch instance wizard.
4. In the wizard, enable stop protection by choosing Enable for Stop protection under Advanced details.
AWS CLI To enable stop protection for an instance at launch

Use the run-instances command to launch the instance. Add the following parameter.
--disable-api-stop PowerShell To enable stop protection for an instance at launch Use the New-EC2Instance cmdlet to launch the instance. Add the following parameter.
-DisableApiStop $true
#### Enable stop protection for a running or stopped instance You can enable stop protection for an instance while the instance is running or stopped.
Console To enable stop protection for an instance
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the left navigation pane, choose Instances.
3. Select the instance, and then choose Actions>Instance settings>Change stop protection.
4. Select the Enable checkbox, and then choose Save.
AWS CLI To enable stop protection for an instance Use the modify-instance-attribute command. aws ec2 modify-instance-attribute \ --instance-id i-1234567890abcdef0 \ --disable-api-stop PowerShell To enable stop protection for an instance

Use the Edit-EC2InstanceAttribute cmdlet.
Edit-EC2InstanceAttribute `
    -InstanceId i-1234567890abcdef0 `
    -DisableApiStop $true
#### Disable stop protection for a running or stopped instance You can disable stop protection for a running or stopped instance using one of the following methods.
Console To disable stop protection for a running or stopped instance
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the left navigation pane, choose Instances.
3. Select the instance, and then choose Actions, Instance settings, Change stop protection.
4. Clear the Enable checkbox, and then choose Save.
AWS CLI To disable stop protection for a running or stopped instance Use the modify-instance-attribute command. aws ec2 modify-instance-attribute \ --instance-id i-1234567890abcdef0 \ --no-disable-api-stop PowerShell To disable stop protection for an instance Use the Edit-EC2InstanceAttribute cmdlet.
Edit-EC2InstanceAttribute `
    -InstanceId i-1234567890abcdef0 `
    -DisableApiStop $false

## Hibernate your Amazon EC2 instance When you hibernate an instance, Amazon EC2 signals the operating system to perform hibernation (suspend-to-disk). Hibernation saves the contents from the instance memory (RAM) to your Amazon Elastic Block Store (Amazon EBS) root volume. Amazon EC2 persists the instance's EBS root volume and any attached EBS data volumes. When your instance is started:
- The EBS root volume is restored to its previous state
- The RAM contents are reloaded
- The processes that were previously running on the instance are resumed
- Previously attached data volumes are reattached and the instance retains its instance ID You can hibernate an instance only if it's enabled for hibernation and it meets the hibernation prerequisites.
If an instance or application takes a long time to bootstrap and build a memory footprint in order to become fully productive, you can use hibernation to pre-warm the instance. To pre-warm the instance, you:
1. Launch it with hibernation enabled.
2. Bring it to a desired state.
3. Hibernate it so that it's ready to be resumed to the desired state whenever needed.
You're not charged for instance usage for a hibernated instance when it is in the stopped state or for data transfer when the contents of the RAM are transferred to the EBS root volume. You are charged for storage of any EBS volumes, including storage for the RAM contents.
If you no longer need an instance, you can terminate it at any time, including when it is in a stopped (hibernated) state. For more information, see Terminate Amazon EC2 instances.
Contents
- How Amazon EC2 instance hibernation works
- Prerequisites for EC2 instance hibernation
- Configure a Linux AMI to support hibernation
- Enable hibernation for an Amazon EC2 instance

- Disable KASLR on an instance (Ubuntu only)
- Hibernate an Amazon EC2 instance
- Start a hibernated Amazon EC2 instance
- Troubleshoot Amazon EC2 instance hibernation
### How Amazon EC2 instance hibernation works The following diagram shows a basic overview of the hibernation process for EC2 instances.
#### What happens when you hibernate an instance When you hibernate an instance, the following happens:
- The instance moves to the stopping state. Amazon EC2 signals the operating system to perform hibernation (suspend-to-disk). The hibernation freezes all of the processes, saves the contents of the RAM to the EBS root volume, and then performs a regular shutdown.
- After the shutdown is complete, the instance moves to the stopped state.
- Any EBS volumes remain attached to the instance, and their data persists, including the saved contents of the RAM.
- Any Amazon EC2 instance store volumes remain attached to the instance, but the data on the instance store volumes is lost.
- In most cases, the instance is migrated to a new underlying host computer when it's started. This is also what happens when you stop and start an instance.
- When the instance is started, the instance boots up and the operating system reads in the contents of the RAM from the EBS root volume, before unfreezing processes to resume its state.
- The instance retains its private IPv4 addresses and any IPv6 addresses. When the instance is started, the instance continues to retain its private IPv4 addresses and any IPv6 addresses.

- Amazon EC2 releases the public IPv4 address. When the instance is started, Amazon EC2 assigns a new public IPv4 address to the instance.
- The instance retains its associated Elastic IP addresses. You're charged for any Elastic IP addresses that are associated with a hibernated instance.
For information about how hibernation differs from reboot, stop, and terminate, see Differences between instance states.
#### Limitations
- When you hibernate an instance, the data on any instance store volumes is lost.
- (Linux instances) You can't hibernate a Linux instance that has more than 150 GiB of RAM.
- (Windows instances) You can't hibernate a Windows instance that has more than 16 GiB of RAM.
- While your instance is hibernated, you can't modify it. This is different to a stopped instance that isn't hibernated, where you can modify certain attributes, such as the instance type or size.
- If you create a snapshot or AMI from an instance that is hibernated or has hibernation enabled, you might not be able to connect to a new instance that is launched from the AMI or from an AMI that was created from the snapshot.
- (Spot Instances only) If Amazon EC2 hibernates your Spot Instance, only Amazon EC2 can resume your instance. If you hibernate your Spot Instance (user-initiated hibernation), you can resume your instance. A hibernated Spot Instance can only be resumed if capacity is available and the Spot price is less than or equal to your specified maximum price.
- You can't hibernate an instance that is in an Auto Scaling group or used by Amazon ECS. If your instance is in an Auto Scaling group and you try to hibernate it, the Amazon EC2 Auto Scaling service marks the stopped instance as unhealthy, and might terminate it and launch a replacement instance. For more information, see Health checks for instances in an Auto Scaling group in the Amazon EC2 Auto Scaling User Guide.
- You can't hibernate an instance that is configured to boot in UEFI mode with UEFI Secure Boot enabled.
- If you hibernate an instance that was launched into a Capacity Reservation, the Capacity Reservation does not ensure that the hibernated instance can resume after you try to start it.
- You can't hibernate an instance that uses a kernel below 5.10 if Federal Information Processing Standard (FIPS) mode is enabled.
- We do not support keeping an instance hibernated for more than 60 days. To keep the instance for longer than 60 days, you must start the hibernated instance, stop the instance, and start it.

- We constantly update our platform with upgrades and security patches, which can conflict with existing hibernated instances. We notify you about critical updates that require a start for hibernated instances so that we can perform a shutdown or a reboot to apply the necessary upgrades and security patches.
#### Considerations for hibernating a Spot Instance
- If you hibernate your Spot Instance, you can restart it provided capacity is available and the Spot price is less than or equal to your specified maximum price.
- If Amazon EC2 hibernates your Spot Instance:
- Only Amazon EC2 can resume your instance.
- Amazon EC2 resumes the hibernated Spot Instance when capacity becomes available with a Spot price that is less than or equal to your specified maximum price.
- Before Amazon EC2 hibernates your Spot Instance, you'll receive an interruption notice two minutes before hibernation starts.
For more information, see Spot Instance interruptions.
### Prerequisites for EC2 instance hibernation You can enable hibernation support for an On-Demand Instance or a Spot Instance when you launch it. You can't enable hibernation on an existing instance, whether it is running or stopped.
For more information, see Enable instance hibernation.
Requirements to hibernate an instance
- AWS Regions
- AMIs
- Instance families
- Instance RAM size
- Root volume type
- Root volume size
- Root volume encryption
- EBS volume type
- Spot Instance requests

#### AWS Regions You can use hibernation with instances in all AWS Regions.
#### AMIs You must use an HVM AMI that supports hibernation. The following AMIs support hibernation:
##### Linux AMIs AMIs for Intel and AMD instance types
- AL2023 AMI released 2023.09.20 or later ¹
- Amazon Linux 2 AMI released 2019.08.29 or later
- Amazon Linux AMI 2018.03 released 2018.11.16 or later
- CentOS version 8 AMI ² (Additional configuration is required)
- Fedora version 34 or later AMI ² (Additional configuration is required)
- Red Hat Enterprise Linux (RHEL) 9 AMI ² (Additional configuration is required)
- Red Hat Enterprise Linux (RHEL) 8 AMI ² (Additional configuration is required)
- Ubuntu 22.04.2 LTS (Jammy Jellyfish) AMI released with serial number 20230303 or later ³
- Ubuntu 20.04 LTS (Focal Fossa) AMI released with serial number 20210820 or later ³
- Ubuntu 18.04 LTS (Bionic Beaver) AMI released with serial number 20190722.1 or later ³ ⁵
- Ubuntu 16.04 LTS (Xenial Xerus) AMI ³ ⁴ ⁵ (Additional configuration is required)
AMIs for Graviton instance types
- AL2023 AMI (64-bit Arm) released 2024.07.01 or later ¹
- Amazon Linux 2 AMI (64-bit Arm) released 2024.06.20 or later
- Ubuntu 22.04.2 LTS (64-bit Arm) (Jammy Jellyfish) AMI released with serial number 20240701 or later ³
- Ubuntu 20.04 LTS (64-bit Arm) (Focal Fossa) AMI released with serial number 20240701 or later ³

¹ For AL2023 minimal AMI, additional configuration is required.

² For CentOS, Fedora, and Red Hat Enterprise Linux, hibernation is supported on Nitro-based instances only.
³ We recommend disabling KASLR on instances with Ubuntu 22.04.2 LTS (Jammy Jellyfish), Ubuntu 20.04 LTS (Focal Fossa), Ubuntu 18.04 LTS (Bionic Beaver), and Ubuntu 16.04 LTS (Xenial Xerus).
For more information, see Disable KASLR on an instance (Ubuntu only).
⁴ For the Ubuntu 16.04 LTS (Xenial Xerus) AMI, hibernation is not supported on t3.nano instance types. No patch will be made available because Ubuntu (Xenial Xerus) ended support in April
2021. If you want to use t3.nano instance types, we recommend that you upgrade to the Ubuntu 22.04.2 LTS (Jammy Jellyfish), Ubuntu 20.04 LTS (Focal Fossa) AMI, or the Ubuntu 18.04 LTS (Bionic Beaver) AMI.
⁵ Support for Ubuntu 18.04 LTS (Bionic Beaver) and Ubuntu 16.04 LTS (Xenial Xerus) has reached end of life.
To configure your own AMI to support hibernation, see Configure a Linux AMI to support hibernation.
Support for other versions of Ubuntu and other operating systems is coming soon.
##### Windows AMIs
- Windows Server 2022 AMI released 2023.09.13 or later
- Windows Server 2019 AMI released 2019.09.11 or later
- Windows Server 2016 AMI released 2019.09.11 or later
- Windows Server 2012 R2 AMI released 2019.09.11 or later
- Windows Server 2012 AMI released 2019.09.11 or later
#### Instance families You must use an instance family that supports hibernation. However, bare metal instances are not supported.
- General purpose: M3, M4, M5, M5a, M5ad, M5d, M6a, M6g, M6gd, M6i, M6id, M6idn, M6in, M7a, M7g, M7gd, M7i, M7i-flex, M8a, M8azn, M8g, M8gb, M8gd, M8gn, M8i, M8i-flex, T2, T3, T3a, T4g
- Compute optimized: C3, C4, C5, C5d, C6a, C6g, C6gd, C6gn, C6i, C6id, C6in, C7a, C7g, C7gd, C7gn, C7i, C7i-flex, C8a, C8g, C8gb, C8gd, C8gn, C8i, C8i-flex

- Memory optimized: R3, R4, R5, R5a, R5ad, R5d, R6a, R6g, R6gd, R6idn, R6in, R7a, R7g, R7gd, R7i, R7iz, R8a, R8g, R8gb, R8gd, R8gn, R8i, R8i-flex, X2gd, X8aedz, X8i
- Storage optimized: I3, I3en, I4g, I7i, I7ie, I8g, I8ge, Im4gn, Is4gen Console To get the instance types that support hibernation
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Instance Types.
3. Add the filter On-Demand Hibernation support = true.
4. (Optional) Add filters to further scope to specific instance types of interest.
AWS CLI To get the instance types that support hibernation Use the describe-instance-types command. Note that the available instance types vary by Region. aws ec2 describe-instance-types \ --filters Name=hibernation-supported,Values=true \ --query "InstanceTypes[*].[InstanceType]" \ --output text | sort PowerShell To get the instance types that support hibernation Use the Get-EC2InstanceType cmdlet. Note that the available instance types vary by Region.
(Get-EC2InstanceType `
    -Filter @{Name="hibernation-supported"; Values="true"}).InstanceType | Sort- Object
#### Instance RAM size Linux instances – Must be less than 150 GiB.

Windows instances – Must be less than or equal to 16 GiB. For hibernating a T3 or T3a Windows instance, we recommend at least 1 GiB of RAM.
#### Root volume type The root volume must be an EBS volume, not an instance store volume.
#### Root volume size The root volume must be large enough to store the RAM contents and accommodate your expected usage, for example, OS or applications. If you enable hibernation, space is allocated on the root volume at launch to store the RAM.
#### Root volume encryption The root volume must be encrypted to ensure the protection of sensitive content that is in memory at the time of hibernation. When RAM data is moved to the EBS root volume, it is always encrypted. Encryption of the root volume is enforced at instance launch.
Use one of the following three options to ensure that the root volume is an encrypted EBS volume:
- EBS encryption by default – You can enable EBS encryption by default to ensure that all new EBS volumes created in your AWS account are encrypted. This way, you can enable hibernation for your instances without specifying encryption intent at instance launch. For more information, see Enable encryption by default.
- EBS "single-step" encryption – You can launch encrypted EBS-backed EC2 instances from an unencrypted AMI and also enable hibernation at the same time. For more information, see Use encryption with EBS-backed AMIs.
- Encrypted AMI – You can enable EBS encryption by using an encrypted AMI to launch your instance. If your AMI does not have an encrypted root snapshot, you can copy it to a new AMI and request encryption. For more information, see Encrypt an unencrypted image during copy and Copy an AMI.
#### EBS volume type The EBS volumes must use one of the following EBS volume types:
- General Purpose SSD (gp2 and gp3)
- Provisioned IOPS SSD (io1 and io2)

If you choose a Provisioned IOPS SSD volume type, you must provision the EBS volume with the appropriate IOPS to achieve optimum performance for hibernation. For more information, see Amazon EBS volume types in the Amazon EBS User Guide.
#### Spot Instance requests For Spot Instances, the following requirements apply:
- The Spot Instance request type must be persistent.
- You can't specify a launch group in the Spot Instance request.
### Configure a Linux AMI to support hibernation The following Linux AMIs can support hibernating an Amazon EC2 instance, provided you complete the additional configuration steps described in this section.
Additional configuration required for:
- AL2023 minimal AMI released 2023.09.20 or later
- Amazon Linux 2 minimal AMI released 2019.08.29 or later
- Amazon Linux 2 released before 2019.08.29
- Amazon Linux released before 2018.11.16
- CentOS version 8 or later
- Fedora version 34 or later
- Red Hat Enterprise Linux version 8 or 9
- Ubuntu 20.04 LTS (Focal Fossa) released before serial number 20210820
- Ubuntu 18.04 (Bionic Beaver) released before serial number 20190722.1
- Ubuntu 16.04 (Xenial Xerus)
For the Linux and Windows AMIs that support hibernation and for which no additional configuration is required, see AMIs.
For more information, see Update instance software on your Amazon Linux 2 instance.

#### AL2023 minimal AMI released 2023.09.20 or later To configure an AL2023 minimal AMI released 2023.09.20 or later to support hibernation
1. Install the ec2-hibinit-agent package from the repositories.
[ec2-user ~]$ sudo dnf install ec2-hibinit-agent
2. Restart the service.
[ec2-user ~]$ sudo systemctl start hibinit-agent
#### Amazon Linux 2 minimal AMI released 2019.08.29 or later To configure an Amazon Linux 2 minimal AMI released 2019.08.29 or later to support hibernation
1. Install the ec2-hibinit-agent package from the repositories.
[ec2-user ~]$ sudo yum install ec2-hibinit-agent
2. Restart the service.
[ec2-user ~]$ sudo systemctl start hibinit-agent
#### Amazon Linux 2 released before 2019.08.29 To configure an Amazon Linux 2 AMI released before 2019.08.29 to support hibernation
1. Update the kernel to 4.14.138-114.102 or later.
[ec2-user ~]$ sudo yum update kernel
2. Install the ec2-hibinit-agent package from the repositories.
[ec2-user ~]$ sudo yum install ec2-hibinit-agent
3. Reboot the instance.

[ec2-user ~]$ sudo reboot
4. Confirm that the kernel version is updated to 4.14.138-114.102 or later.
[ec2-user ~]$ uname -a
5. Stop the instance and create an AMI. For more information, see Create an Amazon EBS-backed AMI.
#### Amazon Linux released before 2018.11.16 To configure an Amazon Linux AMI released before 2018.11.16 to support hibernation
1. Update the kernel to 4.14.77-70.59 or later.
[ec2-user ~]$ sudo yum update kernel
2. Install the ec2-hibinit-agent package from the repositories.
[ec2-user ~]$ sudo yum install ec2-hibinit-agent
3. Reboot the instance.
[ec2-user ~]$ sudo reboot
4. Confirm that the kernel version is updated to 4.14.77-70.59 or greater.
[ec2-user ~]$ uname -a
5. Stop the instance and create an AMI. For more information, see Create an Amazon EBS-backed AMI.
#### CentOS version 8 or later To configure a CentOS version 8 or later AMI to support hibernation
1. Update the kernel to 4.18.0-305.7.1.el8_4.x86_64 or later.
[ec2-user ~]$ sudo yum update kernel

2. Install the Fedora Extra Packages for Enterprise Linux (EPEL) repository.
[ec2-user ~]$ sudo yum install https://dl.fedoraproject.org/pub/epel/epel-release- latest-8.noarch.rpm
3. Install the ec2-hibinit-agent package from the repositories.
[ec2-user ~]$ sudo yum install ec2-hibinit-agent
4. Enable the hibernate agent to start on boot.
[ec2-user ~]$ sudo systemctl enable hibinit-agent.service
5. Reboot the instance.
[ec2-user ~]$ sudo reboot
6. Confirm that the kernel version is updated to 4.18.0-305.7.1.el8_4.x86_64 or later.
[ec2-user ~]$ uname -a
#### Fedora version 34 or later To configure a Fedora version 34 or later AMI to support hibernation
1. Update the kernel to 5.12.10-300.fc34.x86_64 or later.
[ec2-user ~]$ sudo yum update kernel
2. Install the ec2-hibinit-agent package from the repositories.
[ec2-user ~]$ sudo dnf install ec2-hibinit-agent
3. Enable the hibernate agent to start on boot.
[ec2-user ~]$ sudo systemctl enable hibinit-agent.service
4. Reboot the instance.
[ec2-user ~]$ sudo reboot

5. Confirm that the kernel version is updated to 5.12.10-300.fc34.x86_64 or later.
[ec2-user ~]$ uname -a
#### Red Hat Enterprise Linux version 8 or 9 To configure a Red Hat Enterprise Linux 8 or 9 AMI to support hibernation
1. Update the kernel to 4.18.0-305.7.1.el8_4.x86_64 or later.
[ec2-user ~]$ sudo yum update kernel
2. Install the Fedora Extra Packages for Enterprise Linux (EPEL) repository.
RHEL version 8:
[ec2-user ~]$ sudo yum install https://dl.fedoraproject.org/pub/epel/epel-release- latest-8.noarch.rpm RHEL version 9:
[ec2-user ~]$ sudo yum install https://dl.fedoraproject.org/pub/epel/epel-release- latest-9.noarch.rpm
3. Install the ec2-hibinit-agent package from the repositories.
[ec2-user ~]$ sudo yum install ec2-hibinit-agent
4. Enable the hibernate agent to start on boot.
[ec2-user ~]$ sudo systemctl enable hibinit-agent.service
5. Reboot the instance.
[ec2-user ~]$ sudo reboot
6. Confirm that the kernel version is updated to 4.18.0-305.7.1.el8_4.x86_64 or later.
[ec2-user ~]$ uname -a

#### Ubuntu 20.04 LTS (Focal Fossa) released before serial number 20210820 To configure an Ubuntu 20.04 LTS (Focal Fossa) AMI released before serial number 20210820 to support hibernation
1. Update the linux-aws-kernel to 5.8.0-1038.40 or later, and grub2 to 2.04-1ubuntu26.13 or later.
[ec2-user ~]$ sudo apt update [ec2-user ~]$ sudo apt dist-upgrade
2. Reboot the instance.
[ec2-user ~]$ sudo reboot
3. Confirm that the kernel version is updated to 5.8.0-1038.40 or later.
[ec2-user ~]$ uname -a
4. Confirm that the grub2 version is updated to 2.04-1ubuntu26.13 or later.
[ec2-user ~]$ dpkg --list | grep grub2-common
#### Ubuntu 18.04 (Bionic Beaver) released before serial number 20190722.1 To configure an Ubuntu 18.04 LTS AMI released before serial number 20190722.1 to support hibernation
1. Update the kernel to 4.15.0-1044 or later.
[ec2-user ~]$ sudo apt update [ec2-user ~]$ sudo apt dist-upgrade
2. Install the ec2-hibinit-agent package from the repositories.
[ec2-user ~]$ sudo apt install ec2-hibinit-agent
3. Reboot the instance.
[ec2-user ~]$ sudo reboot

4. Confirm that the kernel version is updated to 4.15.0-1044 or later.
[ec2-user ~]$ uname -a
#### Ubuntu 16.04 (Xenial Xerus)
To configure Ubuntu 16.04 LTS to support hibernation, you need to install the linux-aws-hwe kernel package version 4.15.0-1058-aws or later and the ec2-hibinit-agent.
Important The linux-aws-hwe kernel package is supported by Canonical. The standard support for Ubuntu 16.04 LTS ended in April 2021, and the package no longer receives regular updates.
However, it will receive additional security updates until the Extended Security Maintenance support ends in 2024. For more information, see Amazon EC2 Hibernation for Ubuntu 16.04 LTS now available on the Canonical Ubuntu Blog.
We recommend that you upgrade to the Ubuntu 20.04 LTS (Focal Fossa) AMI or the Ubuntu 18.04 LTS (Bionic Beaver) AMI.
To configure an Ubuntu 16.04 LTS AMI to support hibernation
1. Update the kernel to 4.15.0-1058-aws or later.
[ec2-user ~]$ sudo apt update [ec2-user ~]$ sudo apt install linux-aws-hwe
2. Install the ec2-hibinit-agent package from the repositories.
[ec2-user ~]$ sudo apt install ec2-hibinit-agent
3. Reboot the instance.
[ec2-user ~]$ sudo reboot
4. Confirm that the kernel version is updated to 4.15.0-1058-aws or later.
[ec2-user ~]$ uname -a

### Enable hibernation for an Amazon EC2 instance To hibernate an instance, you must first enable it for hibernation while launching the instance.
Important You can't enable or disable hibernation for an instance after you launch it.
Tasks
- Enable hibernation for On-Demand Instances
- Enable hibernation for Spot Instances
- View if an instance is enabled for hibernation
#### Enable hibernation for On-Demand Instances You can enable hibernation for your On-Demand Instances.
Console To enable hibernation for an On-Demand Instance
1. Follow the procedure to launch an instance, but don't launch the instance until you've completed the following steps to enable hibernation.
2. To enable hibernation, configure the following fields in the launch instance wizard: a.
Under Application and OS Images (Amazon Machine Image), select an AMI that supports hibernation. For more information, see AMIs. b.
Under Instance type, select a supported instance type. For more information, see Instance families. c.
Under Configure storage, choose Advanced (at the right), and specify the following information for the root volume:
- For Size (GiB), enter the EBS root volume size. The volume must be large enough to store the RAM contents and accommodate your expected usage.
- For Volume type, select a supported EBS volume type: General Purpose SSD (gp2 and gp3) or Provisioned IOPS SSD (io1 and io2).

- For Encrypted, choose Yes. If you enabled encryption by default in this AWS Region, Yes is selected.
- For KMS key, select the encryption key for the volume. If you enabled encryption by default in this AWS Region, the default encryption key is selected.
For more information about the prerequisites for the root volume, see Prerequisites for EC2 instance hibernation. d.
Expand Advanced details, and for Stop - Hibernate behavior, choose Enable.
3. In the Summary panel, review your instance configuration, and then choose Launch instance. For more information, see Launch an EC2 instance using the launch instance wizard in the console.
AWS CLI To enable hibernation for an On-Demand Instance Use the run-instances command to launch an instance. Specify the EBS root volume parameters using the --block-device-mappings file://mapping.json parameter, and enable hibernation using the --hibernation-options Configured=true parameter. aws ec2 run-instances \ --image-id ami-0abcdef1234567890 \ --instance-type m5.large \ --block-device-mappings file://mapping.json \ --hibernation-options Configured=true \ --count 1 \ --key-name MyKeyPair Specify the following in mapping.json.
[ { "DeviceName": "/dev/xvda", "Ebs": { "VolumeSize": 30, "VolumeType": "gp2", "Encrypted": true } }

]
The value for DeviceName must match the root device name that's associated with the AMI. To find the root device name, use the describe-images command. aws ec2 describe-images --image-id ami-0abcdef1234567890 If you enabled encryption by default in this AWS Region, you can omit "Encrypted": true.
PowerShell To enable hibernation for an On-Demand Instance Use the New-EC2Instance command to launch an instance. Specify the EBS root volume by first defining the block device mapping, and then adding it to the command using the -BlockDeviceMappings parameter. Enable hibernation using the - HibernationOptions_Configured $true parameter.
$ebs_encrypt = New-Object Amazon.EC2.Model.BlockDeviceMapping $ebs_encrypt.DeviceName = "/dev/xvda"
$ebs_encrypt.Ebs = New-Object Amazon.EC2.Model.EbsBlockDevice $ebs_encrypt.Ebs.VolumeSize = 30 $ebs_encrypt.Ebs.VolumeType = "gp2"
$ebs_encrypt.Ebs.Encrypted = $true New-EC2Instance `
    -ImageId ami-0abcdef1234567890 `
    -InstanceType m5.large `
    -BlockDeviceMappings $ebs_encrypt `
    -HibernationOptions_Configured $true `
    -MinCount 1 `
    -MaxCount 1 `
    -KeyName MyKeyPair The value for DeviceName must match the root device name associated with the AMI. To find the root device name, use the Get-EC2Image command.
Get-EC2Image -ImageId ami-0abcdef1234567890 If you enabled encryption by default in this AWS Region, you can omit Encrypted = $true from the block device mapping.

#### Enable hibernation for Spot Instances You can enable hibernation for your Spot Instances. For more information about hibernating a Spot Instance on interruption, see Spot Instance interruptions.
Console To enable hibernation for a Spot Instance
1. Follow the procedure to request a Spot Instance using the launch instance wizard, but don't launch the instance until you've completed the following steps to enable hibernation.
2. To enable hibernation, configure the following fields in the launch instance wizard: a.
Under Application and OS Images (Amazon Machine Image), select an AMI that supports hibernation. For more information, see AMIs. b.
Under Instance type, select a supported instance type. For more information, see Instance families. c.
Under Configure storage, choose Advanced (at the right), and specify the following information for the root volume:
- For Size (GiB), enter the EBS root volume size. The volume must be large enough to store the RAM contents and accommodate your expected usage.
- For Volume type, select a supported EBS volume type: General Purpose SSD (gp2 and gp3) or Provisioned IOPS SSD (io1 and io2).
- For Encrypted, choose Yes. If you enabled encryption by default in this AWS Region, Yes is selected.
- For KMS key, select the encryption key for the volume. If you enabled encryption by default in this AWS Region, the default encryption key is selected.
For more information about the prerequisites for the root volume, see Prerequisites for EC2 instance hibernation. d.
Expand Advanced details, and, in addition to the fields for configuring a Spot Instance, do the following: i.
For Request type, choose Persistent.

ii.
For Interruption behavior, choose Hibernate. Alternatively, for Stop - Hibernate behavior, choose Enable. Both fields enable hibernation on your Spot Instance.
You need only configure one of them.
3. In the Summary panel, review your instance configuration, and then choose Launch instance. For more information, see Launch an EC2 instance using the launch instance wizard in the console.
AWS CLI To enable hibernation for a Spot Instance Use the run-instances command to request a Spot Instance. Specify the EBS root volume parameters using the --block-device-mappings file://mapping.json parameter, and enable hibernation using the --hibernation-options Configured=true parameter. The Spot request type (SpotInstanceType) must be persistent. aws ec2 run-instances \ --image-id ami-0abcdef1234567890 \ --instance-type c4.xlarge \ --block-device-mappings file://mapping.json \ --hibernation-options Configured=true \ --count 1 \ --key-name MyKeyPair --instance-market-options { "MarketType":"spot", "SpotOptions":{ "MaxPrice":"1", "SpotInstanceType":"persistent"
            } } Specify the EBS root volume parameters in mapping.json as follows.
[ { "DeviceName": "/dev/xvda", "Ebs": { "VolumeSize": 30, "VolumeType": "gp2",

            "Encrypted": true } } ]
The value for DeviceName must match the root device name that's associated with the AMI. To find the root device name, use the describe-images command. aws ec2 describe-images --image-id ami-0abcdef1234567890 If you enabled encryption by default in this AWS Region, you can omit "Encrypted": true.
PowerShell To enable hibernation for a Spot Instance Use the New-EC2Instance command to request a Spot Instance. Specify the EBS root volume by first defining the block device mapping, and then adding it to the command using the -BlockDeviceMappings parameter. Enable hibernation using the - HibernationOptions_Configured $true parameter.
$ebs_encrypt = New-Object Amazon.EC2.Model.BlockDeviceMapping $ebs_encrypt.DeviceName = "/dev/xvda"
$ebs_encrypt.Ebs = New-Object Amazon.EC2.Model.EbsBlockDevice $ebs_encrypt.Ebs.VolumeSize = 30 $ebs_encrypt.Ebs.VolumeType = "gp2"
$ebs_encrypt.Ebs.Encrypted = $true New-EC2Instance `
    -ImageId ami-0abcdef1234567890 `
    -InstanceType m5.large `
    -BlockDeviceMappings $ebs_encrypt `
    -HibernationOptions_Configured $true `
    -MinCount 1 `
    -MaxCount 1 `
    -KeyName MyKeyPair `
    -InstanceMarketOption @( MarketType = spot; SpotOptions @{ MaxPrice = 1; SpotInstanceType = persistent} )

The value for DeviceName must match the root device name associated with the AMI. To find the root device name, use the Get-EC2Image command.
Get-EC2Image -ImageId ami-0abcdef1234567890 If you enabled encryption by default in this AWS Region, you can omit Encrypted = $true from the block device mapping.
#### View if an instance is enabled for hibernation You can check whether an instance is enabled for hibernation.
Console To view if an instance is enabled for hibernation
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Instances.
3. Select the instance and, on the Details tab, in the Instance details section, inspect Stop- hibernate behavior. Enabled indicates that the instance is enabled for hibernation.
AWS CLI To view if an instance is enabled for hibernation Use the describe-instances command and specify the --filters "Name=hibernation- options.configured,Values=true" parameter to filter instances that are enabled for hibernation. aws ec2 describe-instances \ --filters "Name=hibernation-options.configured,Values=true"
The following field in the output indicates that the instance is enabled for hibernation.
"HibernationOptions": { "Configured": true }

PowerShell To view if an instance is enabled for hibernation Use the Get-EC2Instance cmdlet and filter instances that are enabled for hibernation.
(Get-EC2Instance `
    -Filter @{Name="hibernation-options.configured"; Values="true"}).Instances
### Disable KASLR on an instance (Ubuntu only)
To run hibernation on a newly launched instance with Ubuntu 16.04 LTS (Xenial Xerus), Ubuntu 18.04 LTS (Bionic Beaver) released with serial number 20190722.1 or later, or Ubuntu 20.04 LTS (Focal Fossa) released with serial number 20210820 or later, we recommend disabling KASLR (Kernel Address Space Layout Randomization). On Ubuntu 16.04 LTS, Ubuntu 18.04 LTS, or Ubuntu 20.04 LTS, KASLR is enabled by default.
KASLR is a standard Linux kernel security feature that helps to mitigate exposure to and ramifications of yet-undiscovered memory access vulnerabilities by randomizing the base address value of the kernel. With KASLR enabled, there is a possibility that the instance might not resume after it has been hibernated.
To learn more about KASLR, see Ubuntu Features.
To disable KASLR on an instance launched with Ubuntu
1. Connect to your instance using SSH. For more information, see Connect to your Linux instance using SSH.
2. Open the /etc/default/grub.d/50-cloudimg-settings.cfg file in your editor of choice. Edit the GRUB_CMDLINE_LINUX_DEFAULT line to append the nokaslr option to its end, as shown in the following example.
GRUB_CMDLINE_LINUX_DEFAULT="console=tty1 console=ttyS0 nvme_core.io_timeout=4294967295 nokaslr"
3. Save the file and exit your editor.
4. Run the following command to rebuild the grub configuration. sudo update-grub

5. Reboot the instance. sudo reboot
6. Run the following command to confirm that nokaslr has been added. cat /proc/cmdline The output of the command should include the nokaslr option.
### Hibernate an Amazon EC2 instance You can initiate hibernation on an On-Demand Instance or Spot Instance if the instance is an EBS- backed instance, is enabled for hibernation, and meets the hibernation prerequisites. If an instance cannot hibernate successfully, a normal shutdown occurs.
Console To hibernate an instance
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Instances.
3. Select an instance, and choose Instance state, Hibernate instance. If Hibernate instance is disabled, the instance is already hibernated or stopped, or it can't be hibernated. For more information, see Prerequisites for EC2 instance hibernation.
4. When prompted for confirmation, choose Hibernate. It can take a few minutes for the instance to hibernate. The instance state first changes to Stopping, and then changes to Stopped when the instance has hibernated.
AWS CLI To hibernate an instance Use the stop-instances command and specify the --hibernate parameter. aws ec2 stop-instances \ --instance-ids i-1234567890abcdef0 \ --hibernate

PowerShell To hibernate an instance Use the Stop-EC2Instance cmdlet.
Stop-EC2Instance `
    -InstanceId i-1234567890abcdef0 `
    -Hibernate $true You can check whether hibernation was initiated on an instance.
Console To view if hibernation was initiated on an instance
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Instances.
3. Select the instance and, on the Details tab, in the Instance details section, check the value for State transition message.
Client.UserInitiatedHibernate: User initiated hibernate indicates that you initiated hibernation on the On-Demand Instance or Spot Instance.
AWS CLI To view if hibernation was initiated on an instance Use the describe-instances command and specify the state-reason-code filter to see the instances on which hibernation was initiated. aws ec2 describe-instances \ --filters "Name=state-reason-code,Values=Client.UserInitiatedHibernate"
The following field in the output indicates that hibernation was initiated on the On-Demand Instance or Spot Instance.
"StateReason": { "Code": "Client.UserInitiatedHibernate"

} PowerShell To view if hibernation was initiated on an instance Use the Get-EC2Instance cmdlet and specify the state-reason-code filter to see the instances on which hibernation was initiated.
Get-EC2Instance `
    -Filter @{Name="state-reason-code";Value="Client.UserInitiatedHibernate"}
### Start a hibernated Amazon EC2 instance Start a hibernated instance by starting it in the same way that you would start a stopped instance.
For Spot Instances, if Amazon EC2 hibernated the instance, then only Amazon EC2 can resume it.
You can only resume a hibernated Spot Instance if you hibernated it. Spot Instances can only be resumed if capacity is available and the Spot price is less than or equal to your specified maximum price.
Console To start a hibernated instance
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Instances.
3. Select a hibernated instance, and choose Instance state, Start instance. It can take a few minutes for the instance to enter the running state. During this time, the instance status checks show the instance in a failed state until the instance has started.
AWS CLI To start a hibernated instance Use the start-instances command. aws ec2 start-instances --instance-ids i-1234567890abcdef0

PowerShell To start a hibernated instance Use the Start-EC2Instance cmdlet.
Start-EC2Instance -InstanceId i-1234567890abcdef0
### Troubleshoot Amazon EC2 instance hibernation Use this information to help diagnose and fix issues that you might encounter when hibernating an instance.
Hibernation issues
- Can't hibernate immediately after launch
- Takes too long to transition from stopping to stopped, and memory state not restored after start
- Instance "stuck" in the stopping state
- Can't start Spot Instance immediately after hibernate
- Resume Spot Instances failed
#### Can't hibernate immediately after launch If you try to hibernate an instance too quickly after you've launched it, you get an error.
You must wait for about two minutes for Linux instances and about five minutes for Windows instances after launch before hibernating.
#### Takes too long to transition from stopping to stopped, and memory state not restored after start start If it takes a long time for your hibernating instance to transition from the stopping state to stopped, and if the memory state is not restored after you start, this could indicate that hibernation was not properly configured.
Linux instances Check the instance system log and look for messages that are related to hibernation. To access the system log, connect to the instance or use the get-console-output command. Find the log lines

from the hibinit-agent. If the log lines indicate a failure or the log lines are missing, there was most likely a failure configuring hibernation at launch.
For example, the following message indicates that the instance root volume is not large enough: hibinit-agent: Insufficient disk space. Cannot create setup for hibernation. Please allocate a larger root device.
If the last log line from the hibinit-agent is hibinit-agent: Running: swapoff /swap, hibernation was successfully configured.
If you do not see any logs from these processes, your AMI might not support hibernation. For information about supported AMIs, see Prerequisites for EC2 instance hibernation. If you used your own Linux AMI, make sure that you followed the instructions for Configure a Linux AMI to support hibernation.
Windows Server 2016 and later Check the EC2 launch log and look for messages that are related to hibernation. To access the EC2 launch log, connect to the instance and open the C:\ProgramData\Amazon\EC2-Windows \Launch\Log\Ec2Launch.log file in a text editor. If you're using EC2Launch v2, open C:
\ProgramData\Amazon\EC2Launch\log\agent.log.
Note By default, Windows hides files and folders under C:\ProgramData. To view EC2 Launch directories and files, enter the path in Windows Explorer or change the folder properties to show hidden files and folders.
Find the log lines for hibernation. If the log lines indicate a failure or the log lines are missing, there was most likely a failure configuring hibernation at launch.
For example, the following message indicates that hibernation failed to configure: Message:
Failed to enable hibernation. If the error message includes decimal ASCII values, you can convert the ASCII values to plain text in order to read the full error message.
If the log line contains HibernationEnabled: true, hibernation was successfully configured.
Windows Server 2012 R2 and earlier

Check the EC2 config log and look for messages that are related to hibernation. To access the EC2 config log, connect to the instance and open the C:\Program Files\Amazon \Ec2ConfigService\Logs\Ec2ConfigLog.txt file in a text editor. Find the log lines for SetHibernateOnSleep. If the log lines indicate a failure or the log lines are missing, there was most likely a failure configuring hibernation at launch.
For example, the following message indicates that the instance root volume is not large enough:
SetHibernateOnSleep: Failed to enable hibernation: Hibernation failed with the following error: There is not enough space on the disk.
If the log line is SetHibernateOnSleep: HibernationEnabled: true, hibernation was successfully configured.
Windows instance size If you're using a T3 or T3a Windows instance with less than 1 GiB of RAM, try increasing the size of the instance to one that has at least 1 GiB of RAM.
#### Instance "stuck" in the stopping state If you hibernated your instance and it appears "stuck" in the stopping state, you can forcibly stop it. For more information, see Troubleshoot Amazon EC2 instance stop issues.
#### Can't start Spot Instance immediately after hibernate If you try to start a Spot Instance within two minutes of hibernating it, you might get the following error:
You failed to start the Spot Instance because the associated Spot Instance request is not in an appropriate state to support start.
Wait for about two minutes for Linux instances and about five minutes for Windows instances and then retry starting the instance.
#### Resume Spot Instances failed If your Spot Instance was hibernated successfully but failed to resume, and instead rebooted (a fresh restart where the hibernated state is not retained), it might be because the user data contained the following script:
/usr/bin/enable-ec2-spot-hibernation

Remove this script from the User data field in the launch template, and then request a new Spot Instance.
Note that even if the instance failed to resume, without the hibernated state preserved, the instance can still be started in the same way as starting from the stopped state.
## Reboot your Amazon EC2 instance An instance reboot is equivalent to an operating system reboot. In most cases, it takes only a few minutes to reboot your instance.
When you reboot an instance, it keeps the following:
- Public DNS name (IPv4)
- Private IPv4 address
- Public IPv4 address
- IPv6 address (if applicable)
- Any data on its instance store volumes Rebooting an instance doesn't start a new instance billing period, unlike stopping and starting an instance (which starts a new billing period with a one-minute minimum charge).
An instance reboot can be user-initiated (where you manually reboot the instance) or initiated by AWS (for automatic instance recovery, or in response to a scheduled reboot event for necessary maintenance, such as to apply updates that require a reboot).
For user-initiated reboots, we recommend using the Amazon EC2 console, CLI, or API instead of running the operating system reboot command from your instance. When using Amazon EC2, if the instance does not cleanly shut down within a few minutes, Amazon EC2 performs a hard reboot.
Furthermore, AWS CloudTrail creates an API record of when your instance was rebooted.
This topic describes how to perform a user-initiated reboot. For information about reboots performed by AWS, see Automatic instance recovery and Manage Amazon EC2 instances scheduled for reboot.
Important If updates are installing on your instance, we recommend that you do not reboot or shut down your instance using the Amazon EC2 console or the command line until all the

updates are installed. When you use the Amazon EC2 console or the command line to reboot or shut down your instance, there is a risk that your instance will be hard rebooted.
A hard reboot while updates are being installed could throw your instance into an unstable state.
Console To reboot an instance
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Instances.
3. Select the instance and choose Instance state, Reboot instance.
4. Choose Reboot when prompted for confirmation.
The instance remains in the running state.
AWS CLI To reboot an instance Use the reboot-instances command. aws ec2 reboot-instances --instance-ids i-1234567890abcdef0 PowerShell To reboot an instance Use the Restart-EC2Instance cmdlet.
Restart-EC2Instance -InstanceId i-1234567890abcdef0 To run a controlled fault injection experiment You can use AWS Fault Injection Service to test how your application responds when your instance is rebooted. For more information, see the AWS Fault Injection Service User Guide.

## Terminate Amazon EC2 instances Warning Terminating an instance is permanent and irreversible.
After you terminate an instance, you can no longer connect to it, and it can't be recovered.
All attached Amazon EBS volumes that are configured to be deleted on termination are also permanently deleted and can't be recovered. All data stored on instance store volumes is permanently lost. For more information, see How instance termination works.
Before you terminate an instance, ensure that you have backed up all data that you need to retain after the termination to persistent storage.
You can delete your instance when you no longer need it. This is referred to as terminating your instance. As soon as the state of an instance changes to shutting-down or terminated, you stop incurring charges for that instance.
You can't connect to or start an instance after you've terminated it. However, you can launch new instances using the same AMI.
If you'd rather stop or hibernate your instance, see Stop and start Amazon EC2 instances or Hibernate your Amazon EC2 instance. For more information, see Differences between instance states.
Contents
- How instance termination works
- Methods for terminating an instance
- Terminate an instance with a graceful OS shutdown
- Terminate an instance and bypass the graceful OS shutdown
- Troubleshoot instance termination
- Change instance termination protection
- Change instance initiated shutdown behavior
- Preserve data when an instance is terminated

### How instance termination works When you terminate an instance, changes are registered at the operating system (OS) level of the instance, some resources are lost, and some resources persist.
The following diagram shows what is lost and what persists when an Amazon EC2 instance is terminated. When an instance terminates, the data on any instance store volumes and the data stored in the instance RAM is erased. Any Elastic IP addresses associated with the instance are detached. For Amazon EBS root volumes and data volumes, the outcome depends on the Delete on termination setting of each volume.

Considerations
- Data persistence
- Instance store volumes: All data is permanently deleted when the instance terminates.
- EBS root volume:
- When attached at launch, deleted by default when the instance terminates.
- When attached after launch, persists by default when the instance terminates.
- EBS data volumes:
- When attached at launch using the console: Persists by default when the instance terminates.
- When attached at launch using the CLI: Deleted by default when the instance terminates.
- When attached after launch using the console or CLI: Persists by default when the instance terminates.
Note Any volumes that are not deleted on instance termination continue to incur charges. You can change the setting so that a volume is deleted or persists on instance termination. For more information, see Preserve data when an instance is terminated.
- Protection against accidental termination
- To prevent an instance from being accidentally terminated by someone, enable termination protection.
- To control whether an instance stops or terminates when shutdown is initiated from the instance, change the instance initiated shutdown behavior.
- Shutdown scripts – If you run a script on instance termination, your instance might have an abnormal termination because we have no way of ensuring that shutdown scripts run. Amazon EC2 attempts to cleanly shut down an instance and run any system shutdown scripts; however, certain events (such as hardware failure) may prevent these system shutdown scripts from running.
- Bare metal instances – x86 bare metal instances don't support cooperative shutdown.

#### What happens when you terminate an instance Changes registered at the OS level
- The API request sends a button press event to the guest.
- Various system services are stopped as a result of the button press event. Graceful shutdown of the system is provided by systemd (Linux) or the System process (Windows). Graceful shutdown is triggered by the ACPI shutdown button press event from the hypervisor.
- ACPI shutdown is initiated.
- The instance shuts down after the graceful shutdown process exits. There is no configurable OS shutdown time. The instance remains visible in the console for a short time, then the entry is automatically deleted.
Resources lost
- Data stored on the instance store volumes.
- EBS root volume if the DeleteOnTermination attribute is set to true.
- EBS data volumes (attached at launch or after) if the DeleteOnTermination attribute is set to true.
Resources that persist
- EBS root volume if the DeleteOnTermination attribute is set to false.
- EBS data volumes (attached at launch or after) if the DeleteOnTermination attribute is set to false.
#### Test application response to instance termination You can use AWS Fault Injection Service to test how your application responds when your instance is terminated. For more information, see the AWS Fault Injection Service User Guide.
### Methods for terminating an instance Warning Terminating an instance is permanent and irreversible.

After you terminate an instance, you can no longer connect to it, and it can't be recovered.
All attached Amazon EBS volumes that are configured to be deleted on termination are also permanently deleted and can't be recovered. All data stored on instance store volumes is permanently lost. For more information, see How instance termination works.
Before you terminate an instance, ensure that you have backed up all data that you need to retain after the termination to persistent storage.
There are four ways to perform a user-initiated instance termination: default terminate, terminate with skip OS shutdown, force terminate, and force terminate with skip OS shutdown. The following table compares the key differences between the termination methods:
Note You can't terminate an instance if termination protection is turned on. For more information, see Change instance termination protection.
Terminati on method Key purpose Use case CLI command Default terminate Normal instance shutdown with attempted graceful OS shutdown.
Typical instance termination. aws ec2 terminate- instances \ --instance- id i-1234567 890abcdef0 Terminate with skip OS shutdown Bypasses the graceful OS shutdown when terminating an instance.
When bypassing graceful OS shutdown is required. aws ec2 terminate- instances \ --instance- id i-1234567 890abcdef0 \

Terminati on method Key purpose Use case CLI command --skip-os- shutdown Force terminate Handles stuck instances.
Attempts a default terminati on first; if  instance fails to terminate, then forcibly terminates the  instance.
When instance is stuck in shutting-down  state. aws ec2 terminate- instances \ --instance- id i-1234567 890abcdef0 \ --force Force terminate with skip OS shutdown Force terminates and bypasses the graceful OS shutdown when terminating an  instance.
When force termination and bypassing graceful OS shutdown is  required. aws ec2 terminate- instances \ --instance- id i-1234567 890abcdef0 \ --force \ --skip-os- shutdown For instructions on how to use each method, see the following:
- Terminate an instance with a graceful OS shutdown
- Terminate an instance and bypass the graceful OS shutdown
- Force terminate an instance
### Terminate an instance with a graceful OS shutdown You can terminate an instance using the default terminate method, which includes an attempt at a graceful OS shutdown. For more information, see Methods for terminating an instance.

Console To terminate an instance using the default terminate method
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Instances.
3. Select the instance, and choose Instance state, Terminate (delete) instance.
4. Choose Terminate (delete) when prompted for confirmation.
5. After you terminate an instance, it remains visible for a short while, with a state of terminated.
If termination fails or if a terminated instance is visible for more than a few hours, see Terminated instance still displayed.
AWS CLI To terminate an instance using the default terminate method Use the terminate-instances command. aws ec2 terminate-instances --instance-ids i-1234567890abcdef0 PowerShell To terminate an instance using the default terminate method Use the Remove-EC2Instance cmdlet.
Remove-EC2Instance -InstanceId i-1234567890abcdef0
### Terminate an instance and bypass the graceful OS shutdown You can bypass the graceful OS shutdown when terminating an instance. For more information, see Methods for terminating an instance.

Console To terminate an instance and bypass the graceful OS shutdown
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Instances.
3. Select the instance, and choose Instance state, Terminate (delete) instance.
4. Under Skip OS shutdown, select the Skip OS shutdown checkbox. If you don't see this option in the console, it's not yet available in the console in the current Region. You can, however, access this feature using the AWS CLI or SDK, or try another Region in the console.
5. Choose Terminate (delete).
6. After you terminate an instance, it remains visible for a short while, with a state of terminated.
If termination fails or if a terminated instance is visible for more than a few hours, see Terminated instance still displayed.
AWS CLI To terminate an instance and bypass the graceful OS shutdown Use the terminate-instances command with --skip-os-shutdown.. aws ec2 terminate-instances \ --instance-ids i-1234567890abcdef0 \ --skip-os-shutdown PowerShell To terminate an instance and bypass the graceful OS shutdown Use the Remove-EC2Instance cmdlet with -SkipOsShutdown $true..
Remove-EC2Instance `
    -InstanceId i-1234567890abcdef0 `
    -SkipOsShutdown $true

### Troubleshoot instance termination The requester must have permission to call ec2:TerminateInstances. For more information, see Example policies to work with instances.
If you terminate your instance and another instance starts, most likely you have configured automatic scaling through a feature like EC2 Fleet or Amazon EC2 Auto Scaling. For more information, see Instances automatically launched or terminated.
Note You can't terminate an instance if termination protection is turned on. For more information, see Change instance termination protection.
If your instance is in the shutting-down state for longer than usual, you can attempt to force terminate it. If it remains in the shutting-down state, it should be cleaned up (terminated) by automated processes within the Amazon EC2 service. For more information, see Delayed instance termination.
### Change instance termination protection To prevent your instance from being accidentally terminated using the Amazon EC2 API, whether you call TerminateInstances directly or using another interface such as the Amazon EC2 console, enable termination protection for the instance. The DisableApiTermination attribute controls whether the instance can be terminated. By default, termination protection is disabled for your instance. You can set the value of this attribute when you launch an instance, or while the instance is running or stopped.
The DisableApiTermination attribute doesn't prevent you from terminating an instance by initiating shutdown from the instance (for example, by using an operating system command for system shutdown) when the InstanceInitiatedShutdownBehavior attribute is set to terminate. For more information, see Change instance initiated shutdown behavior.
Considerations
- Enabling termination protection does not prevent AWS from terminating the instance when there is a scheduled event to terminate the instance.
- Enabling termination protection does not prevent Amazon EC2 Auto Scaling from terminating an instance when the instance is unhealthy or during scale-in events. You can control whether

an Auto Scaling group can terminate a particular instance when scaling using instance scale-in protection. You can control whether an Auto Scaling group can terminate unhealthy instances by suspending the ReplaceUnhealthy scaling process.
- You can't enable termination protection for Spot Instances.
Console To enable termination protection for an instance at launch
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. On the dashboard, choose Launch instance.
3. Expand Advanced details. For Termination protection, select Enable.
4. When you are finishing specifying the details for your instance, choose Launch instance.
To change termination protection for an instance
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, select Instances.
3. Select the instance.
4. Choose Actions, Instance settings, Change termination protection.
5. For Termination protection select or clear Enable.
6. Choose Save.
AWS CLI To enable termination protection for an instance Use the modify-instance-attribute command. aws ec2 modify-instance-attribute \ --instance-id i-1234567890abcdef0 \ --disable-api-termination To disable termination protection for an instance Use the modify-instance-attribute command.

aws ec2 modify-instance-attribute \ --instance-id i-1234567890abcdef0 \ --no-disable-api-termination PowerShell To enable termination protection for an instance Use the Edit-EC2InstanceAttribute cmdlet.
Edit-EC2InstanceAttribute `
    -InstanceId i-1234567890abcdef0 `
    -DisableApiTermination $true To disable termination protection for an instance Use the Edit-EC2InstanceAttribute cmdlet.
Edit-EC2InstanceAttribute `
    -InstanceId i-1234567890abcdef0 `
    -DisableApiTermination $false
#### Terminate multiple instances with termination protection If you terminate multiple instances across multiple Availability Zones in the same request, and one or more of the specified instances are enabled for termination protection, the request fails with the following results:
- The specified instances that are in the same Availability Zone as the protected instance are not terminated.
- The specified instances that are in different Availability Zones, where no other specified instances are protected, are successfully terminated.
Example Suppose that you have the following four instances across two Availability Zones.

Instance Availability Zone Terminate protection Instance 1 Disabled Instance 2 AZ A Disabled Instance 3 Enabled Instance 4 AZ B Disabled If you attempt to terminate all of these instances in the same request, the request reports failure with the following results:
- Instance 1 and Instance 2 are successfully terminated because neither instance is enabled for termination protection.
- Instance 3 and Instance 4 fail to terminate because Instance 3 is enabled for termination protection.
### Change instance initiated shutdown behavior Warning Terminating an instance is permanent and irreversible.
After you terminate an instance, you can no longer connect to it, and it can't be recovered.
All attached Amazon EBS volumes that are configured to be deleted on termination are also permanently deleted and can't be recovered. All data stored on instance store volumes is permanently lost. For more information, see How instance termination works.
Before you terminate an instance, ensure that you have backed up all data that you need to retain after the termination to persistent storage.
By default, when you initiate a shutdown from an Amazon EBS backed instance (using a command such as shutdown or poweroff), the instance stops. You can change this behavior so that the instance terminates instead by changing the InstanceInitiatedShutdownBehavior attribute for the instance. You can change this attribute while the instance is running or stopped.

The halt command doesn't initiate a shutdown. If used, the instance doesn't terminate; instead, it places the CPU into HLT and the instance continues to run.
Note The InstanceInitiatedShutdownBehavior attribute only applies when you perform a shutdown from the operating system of the instance itself. It doesn't apply when you stop an instance using the StopInstances API or the Amazon EC2 console.
Console To change the instance initiated shutdown behavior
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Instances.
3. Select the instance.
4. Choose Actions, Instance settings, Change shutdown behavior.
Shutdown behavior displays the current behavior.
5. To change the behavior, for Shutdown behavior, choose Stop or Terminate.
6. Choose Save.
AWS CLI To change the instance initiated shutdown behavior Use the modify-instance-attribute command. aws ec2 modify-instance-attribute \ --instance-id i-1234567890abcdef0 \ --instance-initiated-shutdown-behavior terminate PowerShell To change the instance initiated shutdown behavior Use the Edit-EC2InstanceAttribute cmdlet.
Edit-EC2InstanceAttribute `

    -InstanceId i-1234567890abcdef0 `
    -InstanceInitiatedShutdownBehavior terminate
### Preserve data when an instance is terminated When an Amazon EC2 instance is terminated, you can preserve the data on your instance store volumes or Amazon EBS volumes. This topic explains how to ensure your data persists beyond instance termination.
#### How instance termination affects root and data volumes Instance store volumes When an instance is terminated, the instance store volumes are automatically deleted and the data is lost. To preserve this data beyond the lifetime of the instance, before terminating the instance, manually copy the data to persistent storage, such as an Amazon EBS volume, an Amazon S3 bucket, or an Amazon EFS file system. For more information, see Storage options for your Amazon EC2 instances.
Amazon EBS volumes When an instance is terminated, the EBS volumes are either deleted or preserved, depending on the value of the DeleteOnTermination attribute for each volume:
- Yes (console) / true (CLI) – The volume is deleted when the instance is terminated.
- No (console) / false (CLI) – The volume is preserved when the instance is terminated. Preserved volumes continue to incur charges.
Note After an instance terminates, you can take a snapshot of the preserved volume or attach it to another instance. To avoid incurring charges, you must delete the volume.
#### Default deletion behavior for EBS volumes The default DeleteOnTermination value differs depending on the volume type, whether the volume was attached at launch or after, and the method (console or CLI) used to attach the volume:

Volume type Attached when Method for attaching Default behavior on instance termination Root volume At launch Console or CLI Delete Root volume After launch Console or CLI Preserve Data volume At launch Console Preserve Data volume At launch CLI Delete Data volume After launch Console and CLI Preserve
#### Check volume persistence settings The default value at launch for an EBS volume is determined by the DeleteOnTermination attribute set on the AMI. You can change the value at instance launch, overriding the AMI setting.
We recommend that you verify the default setting for the DeleteOnTermination attribute after you launch an instance.
To check if an Amazon EBS volume will be deleted on instance termination
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Instances.
3. Select the instance.
4. Choose the Storage tab.
5. Under Block devices, scroll right to check the Delete on termination column.
- If Yes, the volume is deleted when the instance is terminated.
- If No, the volume is not be deleted when the instance is terminated. Any volumes not deleted continue to incur charges.
#### Change the root volume to persist at launch You can change the DeleteOnTermination attribute of an EBS root volume when you launch an instance. You can also use the following procedure for a data volume.

Console To change the root volume of an instance to persist at launch
1. Follow the procedure to launch an instance, but don't launch the instance until you've completed the following steps to change the root volume to persist.
2. On the Configure storage pane, choose Advanced.
3. Under EBS volumes, expand the root volume information.
4. For Delete on termination, choose No.
5. In the Summary panel, review your instance configuration, and then choose Launch instance. For more information, see Launch an EC2 instance using the launch instance wizard in the console.
AWS CLI To change the root volume of an instance to persist at launch Use the run-instances command to change the value of DeleteOnTermination in the block device mapping.
Add the --block-device-mappings option:
--block-device-mappings file://mapping.json In mapping.json, specify the device name, for example /dev/sda1 or /dev/xvda, and for DeleteOnTermination, specify false.
[ { "DeviceName": "device_name", "Ebs": { "DeleteOnTermination": false } } ]
PowerShell To change the root volume of an instance to persist at launch

Use the New-EC2Instance cmdlet to change the value of DeleteOnTermination in the block device mapping.
Add the -BlockDeviceMapping option:
-BlockDeviceMapping $bdm In bdm, specify the device name, for example /dev/sda1 or /dev/xvda, and for DeleteOnTermination, specify false.
$ebd = New-Object -TypeName Amazon.EC2.Model.EbsBlockDevice $ebd.DeleteOnTermination = false $bdm = New-Object -TypeName Amazon.EC2.Model.BlockDeviceMapping $bdm.DeviceName = "/dev/sda1"
$bdm.Ebs = $ebd
#### Change the root volume of a running instance to persist You can change the EBS root volume of a running instance to persist. You can also use the following procedure for a data volume.
AWS CLI To change the root volume to persist Use the modify-instance-attribute command. aws ec2 modify-instance-attribute \ --instance-id i-1234567890abcdef0  \ --block-device-mappings file://mapping.json In mapping.json, specify the device name, for example /dev/sda1 or /dev/xvda, and for -- DeleteOnTermination, specify false.
[ { "DeviceName": "device_name", "Ebs": { "DeleteOnTermination": false } }

]
PowerShell To change the root volume to persist Use the Edit-EC2InstanceAttribute cmdlet.
Add the -BlockDeviceMapping option:
-BlockDeviceMapping $bdm In bdm, specify the device name, for example /dev/sda1 or /dev/xvda, and for DeleteOnTermination, specify false.
$ebd = New-Object -TypeName Amazon.EC2.Model.EbsBlockDevice $ebd.DeleteOnTermination = false $bdm = New-Object -TypeName Amazon.EC2.Model.BlockDeviceMapping $bdm.DeviceName = "/dev/sda1"
$bdm.Ebs = $ebd
## Instance retirement An instance is scheduled to be retired when AWS detects irreparable failure of the underlying hardware that hosts the instance. The instance root volume type determines the behavior of instance retirement:
- If your instance root volume is an Amazon EBS volume, the instance is stopped, and you can start it again at any time. Starting the stopped instance migrates it to new hardware.
- If your instance root volume is an instance store volume, the instance is terminated, and can't be used again.
For more information about the types of instance events, see Scheduled events for Amazon EC2 instances.
Contents
- Identify instances scheduled for retirement
- Actions to take for EBS-backed instances scheduled for retirement

- Actions to take for instance-store backed instances scheduled for retirement
### Identify instances scheduled for retirement If your instance is scheduled for retirement, you receive an email prior to the event with the instance ID and retirement date. You can also check for instances that are scheduled for retirement.
Important If an instance is scheduled for retirement, we recommend that you take action as soon as possible, because the instance might already be unreachable. For more information, see Check if your instance is reachable.
Options to identify instances scheduled for retirement
- Monitor the email for the account contacts
- Check your instances
#### Monitor the email for the account contacts If an instance is scheduled for retirement, the primary contact for the account and the operations contact receive an email prior to the event. This email includes the instance ID and scheduled retirement date. For more information, see Update the primary contact for your AWS account and Update the alternate contacts for your AWS account in the AWS Account Management Reference Guide.
#### Check your instances If you use an email account that you do not check regularly, you might miss an instance retirement notification. You can check whether any of your instances are scheduled for retirement at any time.
Console To identify instances scheduled for retirement
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose EC2 Dashboard. Under Scheduled events, you can see the events that are associated with your Amazon EC2 instances and volumes, organized by Region.

3. If you have an instance with a scheduled event listed, select its link below the Region name to go to the Events page.
4. The Events page lists all resources that have events associated with them. To view instances that are scheduled for retirement, select Instance resources from the first filter list, and then Instance stop or retirement from the second filter list.
5. If the filter results show that an instance is scheduled for retirement, select it, and note the date and time in the Start time field in the details pane. This is your instance retirement date.
AWS CLI To find instances scheduled for retirement Use the following describe-instance-status command. Repeat in each Region where you have running instances. aws ec2 describe-instance-status --filters Name=event.code,Values=instance- retirement PowerShell To find instances scheduled for retirement Use the Get-EC2InstanceStatus cmdlet. Repeat in each Region where you have running instances.
Get-EC2InstanceStatus -Filter @{Name="event.code"; Values="instance-retirement"}

### Actions to take for EBS-backed instances scheduled for retirement To preserve the data on your retiring instance, you can perform one of the following actions. It's important that you take this action before the instance retirement date to prevent unforeseen downtime and data loss.
For Linux instances, if you are not sure whether your instance is backed by EBS or instance store, see Root volumes for your Amazon EC2 instances.
Check if your instance is reachable When you are notified that your instance is scheduled for retirement, we recommend that you take the following action as soon as possible:
- Check if your instance is reachable by either connecting to or pinging your instance.
- If your instance is reachable, you should plan to stop/start your instance at an appropriate time before the scheduled retirement date, when the impact is minimal. For more information about stopping and starting your instance, and what to expect when your instance is stopped, such as the effect on public, private, and Elastic IP addresses that are associated with your instance, see Stop and start Amazon EC2 instances. Note that data on instance store volumes is lost when you stop and start your instance.
- If your instance is unreachable, you should take immediate action and perform a stop/start to recover your instance.
- Alternatively, if you want to terminate your instance, plan to do so as soon as possible so that you stop incurring charges for the instance.
Create a backup of your instance Create an EBS-backed AMI from your instance so that you have a backup. To ensure data integrity, stop the instance before you create the AMI. You can wait for the scheduled retirement date when the instance is stopped, or stop the instance yourself before the retirement date. You can start the instance again at any time. For more information, see Create an Amazon EBS-backed AMI.
Launch a replacement instance After you create an AMI from your instance, you can use the AMI to launch a replacement instance.
From the Amazon EC2 console, select your new AMI and then choose Launch instance from AMI. Configure the parameters for your instance and then choose Launch instance. For more

information about each field, see Launch an EC2 instance using the launch instance wizard in the console.
### Actions to take for instance-store backed instances scheduled for retirement To preserve the data on your retiring instance, you can perform one of the following actions. It's important that you take this action before the instance retirement date to prevent unforeseen downtime and data loss.
Warning If your instance has an instance store root volume and it passes its retirement date, it is terminated and you cannot recover the instance or any data that was stored on it.
Regardless of the root volume type of your instance, the data on instance store volumes is lost when the instance is retired, even if the volumes are attached to an instance with an EBS root volume.
Check if your instance is reachable When you are notified that your instance is scheduled for retirement, we recommend that you take the following action as soon as possible:
- Check if your instance is reachable by either connecting to or pinging your instance.
- If your instance is unreachable, there is likely very little that can be done to recover your instance. For more information, see Troubleshoot an unreachable Amazon EC2 instance. AWS will terminate your instance on the scheduled retirement date, so, for an unreachable instance, you can immediately terminate the instance yourself.
Launch a replacement instance Create an Amazon S3-backed AMI from your instance using the AMI tools, as described in Create an Amazon S3-backed AMI. From the Amazon EC2 console, select your new AMI and then choose Launch instance from AMI. Configure the parameters for your instance and then choose Launch instance. For more information about each field, see Launch an EC2 instance using the launch instance wizard in the console.
Convert your instance to an EBS-backed instance
