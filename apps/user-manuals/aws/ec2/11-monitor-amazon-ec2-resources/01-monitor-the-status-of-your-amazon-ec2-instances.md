# Monitor the status of your Amazon EC2 instances

Source: apps/user-manuals/aws/ec2-ug.pdf

---

a number of time periods. The action is a notification sent to an Amazon Simple Notification Service (Amazon SNS) topic or Amazon EC2 Auto Scaling policy. Alarms invoke actions for sustained state changes only. CloudWatch alarms will not invoke actions simply because they are in a particular state; the state must have changed and been maintained for a specified number of periods. For more information, see Monitor your instances using CloudWatch.
- Amazon EventBridge events – Automate your AWS services and respond automatically to system events. Events from AWS services are delivered to EventBridge in near real time, and you can specify automated actions to take when an event matches a rule you write. For more information, see the section called "Automate using EventBridge".
- AWS CloudTrail logs – Capture detailed information about the calls made to the Amazon EC2 API and stores them as log files in Amazon S3. You can use CloudTrail logs to determine which calls were made, the source IP address for the call, who made the call, and when the call was made. For more information, see the section called "Log API calls using CloudTrail".
- CloudWatch agent – Collect logs and system-level metrics from both hosts and guests on your EC2 instances and on-premises servers. For more information, see Collecting Metrics and Logs from Amazon EC2 Instances and On-Premises Servers with the CloudWatch Agent in the Amazon CloudWatch User Guide.
# Monitor the status of your Amazon EC2 instances You can monitor the status of your instances by viewing status checks and scheduled events for your instances.
A status check gives you the information that results from automated checks performed by Amazon EC2. These automated checks detect whether specific issues are affecting your instances.
The status check information, together with the data provided by Amazon CloudWatch, gives you detailed operational visibility into each of your instances.
You can also see the status of specific events that are scheduled for your instances. The status of events provides information about upcoming activities that are planned for your instances, such as rebooting or retirement. They also provide the scheduled start and end time of each event.
Contents
- Status checks for Amazon EC2 instances
- State change events for Amazon EC2 instances
- Scheduled events for Amazon EC2 instances

## Status checks for Amazon EC2 instances With instance status monitoring, you can quickly determine whether Amazon EC2 has detected any problems that might prevent your instances from running applications. Amazon EC2 performs automated checks on every running EC2 instance to identify hardware and software issues. You can view the results of these status checks to identify specific and detectable problems. The event status data augments the information that Amazon EC2 already provides about the state of each instance (such as pending, running, stopping) and the utilization metrics that Amazon CloudWatch monitors (CPU utilization, network traffic, and disk activity).
Status checks are performed every minute, returning a pass or a fail status. If all checks pass, the overall status of the instance is OK. If one or more checks fail, the overall status is impaired. Status checks are built into Amazon EC2, so they cannot be disabled or deleted.
When a status check fails, the corresponding CloudWatch metric for status checks is incremented.
For more information, see Status check metrics. You can use these metrics to create CloudWatch alarms that are triggered based on the result of the status checks. For example, you can create an alarm to warn you if status checks fail on a specific instance. For more information, see Create CloudWatch alarms for Amazon EC2 instances that fail status checks.
You can also create an Amazon CloudWatch alarm that monitors an Amazon EC2 instance and automatically recovers the instance if it becomes impaired due to an underlying issue. For more information, see Automatic instance recovery.
Contents
- Types of status checks
- View status checks for Amazon EC2 instances
- Create CloudWatch alarms for Amazon EC2 instances that fail status checks
### Types of status checks There are three types of status checks.
- System status checks
- Instance status checks
- Attached EBS status checks

#### System status checks System status checks monitor the AWS systems on which your instance runs. These checks detect underlying problems with your instance that require AWS involvement to repair. When a system status check fails, you can choose to wait for AWS to fix the issue, or you can resolve it yourself.
For instances backed by Amazon EBS, you can stop and start the instance yourself, which in most cases results in the instance being migrated to a new host. For instances backed by instance store (supported only for Linux instances), you can terminate and replace the instance. Note that instance store volumes are ephemeral and all data is lost when the instance is stopped.
The following are examples of problems that can cause system status checks to fail:
- Loss of network connectivity
- Loss of system power
- Software issues on the physical host
- Hardware issues on the physical host that impact network reachability If a system status check fails, we increment the StatusCheckFailed_System metric.
Bare metal instances If you perform a restart from the operating system on a bare metal instance, the system status check might temporarily return a fail status. When the instance becomes available, the system status check should return a pass status.
#### Instance status checks Instance status checks monitor the software and network connectivity of your individual instance.
Amazon EC2 checks the health of the instance by sending an address resolution protocol (ARP) request to the network interface (NIC). These checks detect problems that require your involvement to repair. When an instance status check fails, you typically must address the problem yourself (for example, by rebooting the instance or by making instance configuration changes).
Note Recent Linux distributions that use systemd-networkd for network configuration might report on health checks differently from earlier distributions. During the boot process, this type of network can start earlier and potentially finish before other startup tasks that can

also affect instance health. Status checks that depend on network availability can report a healthy status before other tasks complete.
The following are examples of problems that can cause instance status checks to fail:
- Failed system status checks
- Incorrect networking or startup configuration
- Exhausted memory
- Corrupted file system
- Incompatible kernel
- During a reboot, an instance status check reports a failure until the instance becomes available again.
If an instance status check fails, we increment the StatusCheckFailed_Instance metric.
Bare metal instances If you perform a restart from the operating system on a bare metal instance, the instance status check might temporarily return a fail status. When the instance becomes available, the instance status check should return a pass status.
#### Attached EBS status checks Attached EBS status checks monitor if the Amazon EBS volumes attached to an instance are reachable and able to complete I/O operations. The StatusCheckFailed_AttachedEBS metric is a binary value that indicates impairment if one or more of the EBS volumes attached to the instance are unable to complete I/O operations. These status checks detect underlying issues with the compute or Amazon EBS infrastructure. When the attached EBS status check metric fails, you can either wait for AWS to resolve the issue, or you can take actions, such as replacing the affected volumes or stopping and restarting the instance.
The following are examples of issues that can cause attached EBS status checks to fail:
- Hardware or software issues on the storage subsystems underlying the EBS volumes
- Hardware issues on the physical host that impact reachability of the EBS volumes
- Connectivity issues between the instance and EBS volumes

You can use the StatusCheckFailed_AttachedEBS metric to help improve the resilience of your workload. You can use this metric to create Amazon CloudWatch alarms that are triggered based on the result of the status check. For example, you could fail over to a secondary instance or Availability Zone when you detect a prolonged impact. Alternatively, you can monitor the I/O performance of each attached volume using EBS CloudWatch metrics to detect and replace the impaired volume. If your workload is not driving I/O to any EBS volumes attached to your instance, and the EBS status check indicates an impairment, you can stop and start the instance to move it to a new host. This can resolve underlying host issues that are impacting the reachability of the EBS volumes. For more information, see Amazon CloudWatch metrics for Amazon EBS.
You can also configure your Amazon EC2 Auto Scaling groups to detect attached EBS status check failures, and then replace the affected instance with a new one. For more information, see  Monitor and replace Auto Scaling instances with impaired Amazon EBS volumes in the Amazon EC2 Auto Scaling User Guide.
Note The attached EBS status check metric is available only for Nitro instances.
### View status checks for Amazon EC2 instances If your instance has a failed status check, you typically must address the problem yourself (for example, by rebooting the instance or by making instance configuration changes). To troubleshoot system or instance status check failures yourself, see Troubleshoot Amazon EC2 Linux instances with failed status checks.
Console To view status checks
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Instances.
3. On the Instances page, the Status check column lists the operational status of each instance.
4. To view the status of a specific instance, select the instance, and then choose the Status and alarms tab.

5. To review the CloudWatch metrics for status checks, on the Status and alarms tab, expand Metrics to see the graphs for the following metrics:
- Status check failed for system
- Status check failed for instance
- Status check failed for attached EBS For more information, see the section called "Status check metrics".
AWS CLI To view status checks Use the describe-instance-status command.
Example: Get the status of all running instances aws ec2 describe-instance-status Example: Get the status of all instances aws ec2 describe-instance-status --include-all-instances Example: Get the status of a single running instance aws ec2 describe-instance-status --instance-ids i-1234567890abcdef0 Example: Get all instances with a status of impaired aws ec2 describe-instance-status \ --filters Name=instance-status.status,Values=impaired PowerShell To view status checks Use the Get-EC2InstanceStatus command.
Example: Get the status of all running instances

Get-EC2InstanceStatus Example: Get the status of all instances Get-EC2InstanceStatus -IncludeAllInstance $true Example: Get the status of a single running instance Get-EC2InstanceStatus -InstanceId i-1234567890abcdef0 Example: Get all instances with a status of impaired Get-EC2InstanceStatus \ -Filter @{Name="instance-status.status"; Values="impaired"}
### Create CloudWatch alarms for Amazon EC2 instances that fail status checks You can use the status check metrics to create CloudWatch alarms to notify you when an instance has a failed status check.
Status checks and status check alarms can temporarily enter an insufficient data state if there are missing metric data points. Although rare, this can happen when there is an interruption in the metric reporting systems, even when an instance is healthy. We recommend that you treat this state as missing data instead of a status check failure or alarm breach. This is especially important when taking stop, terminate, reboot, or recover actions on the instance in response.
Console This example configures an alarm that sends a notification when an instance fails a status check. You can optionally stop, terminate, or recover the instance.
To create a status check alarm
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Instances.
3. Select the instance, choose the Status Checks tab, and choose Actions, Create status check alarm.

4. On the Manage CloudWatch alarms page, under Add or edit alarm, choose Create an alarm.
5. For Alarm notification, turn the toggle on to configure Amazon Simple Notification Service (Amazon SNS) notifications. Select an existing Amazon SNS topic or enter a name to create a new topic.
If you add an email address to the list of recipients or create a new topic, Amazon SNS sends a confirmation email to each new address. Each recipient must choose the confirmation link in the email. Only confirmed addresses receive alert notifications.
6. For Alarm action, turn the toggle on to specify an action to take when the alarm is triggered. Select the action.
7. For Alarm thresholds, specify the metric and criteria for the alarm.
You can leave the default settings for Group samples by (Average) and Type of data to sample (Status check failed:either), or you can change them to suit your needs.
For Consecutive period, set the number of periods to evaluate and, in Period, enter the evaluation period duration before triggering the alarm and sending an email.
8. (Optional) For Sample metric data, choose Add to dashboard.
9. Choose Create.
If you need to change an instance status alarm, you can edit it.
To edit a status check alarm
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Instances.
3. Select the instance and choose Actions, Monitoring, Manage CloudWatch alarms.
4. On the Manage CloudWatch alarms page, under Add or edit alarm, choose Edit an alarm.
5. For Search for alarm, choose the alarm.
6. When you are finished making changes, choose Update.

AWS CLI In the following example, the alarm publishes a notification to an SNS topic when the instance fails either the instance check or system status check for at least two consecutive periods. The CloudWatch metric used is StatusCheckFailed.
To create a status check alarm
1. Select an existing SNS topic or create a new one. For more information, see Accessing Amazon SNS in the AWS CLI in the AWS Command Line Interface User Guide.
2. Use the following list-metrics command to view the available Amazon CloudWatch metrics for Amazon EC2. aws cloudwatch list-metrics --namespace AWS/EC2
3. Use the following put-metric-alarm command to create the alarm. aws cloudwatch put-metric-alarm \ --alarm-name StatusCheckFailed-Alarm-for-i-1234567890abcdef0 \ --metric-name StatusCheckFailed \ --namespace AWS/EC2 \ --statistic Maximum \ --dimensions Name=InstanceId,Value=i-1234567890abcdef0 \ --unit Count \ --period 300 \ --evaluation-periods 2 \ --threshold 1 \ --comparison-operator GreaterThanOrEqualToThreshold \ --alarm-actions arn:aws:sns:us-west-2:111122223333:my-sns-topic The period is the time frame, in seconds, in which Amazon CloudWatch metrics are collected. This example uses 300, which is 60 seconds multiplied by 5 minutes. The evaluation period is the number of consecutive periods for which the value of the metric must be compared to the threshold. This example uses 2. The alarm actions are the actions to perform when this alarm is triggered.
PowerShell To create a status check alarm

Use the Write-CWMetricAlarm cmdlet as follows to publish notifications to an SNS topic when the instance fails status checks for at least two consecutive periods.
Write-CWMetricAlarm `
    -AlarmName "StatusCheckFailed-Alarm-for-i-1234567890abcdef0" `
    -MetricName "StatusCheckFailed" `
    -Namespace "AWS/EC2" `
    -Statistic "Maximum" `
    -Dimension @{Name="InstanceId"; Values="i-1234567890abcdef0"} `
    -Unit "Count" `
    -Period 300 `
    -EvaluationPeriod 2 `
    -Threshold 1 `
    -ComparisonOperator "GreaterThanOrEqualToThreshold" `
    -AlarmAction "arn:aws:sns:us-west-2:111122223333:my-sns-topic"
The period is the time frame, in seconds, in which Amazon CloudWatch metrics are collected.
This example uses 300, which is 60 seconds multiplied by 5 minutes. The evaluation period is the number of consecutive periods for which the value of the metric must be compared to the threshold. This example uses 2. The alarm actions are the actions to perform when this alarm is triggered.
## State change events for Amazon EC2 instances Amazon EC2 sends an EC2 Instance State-change Notification event to Amazon EventBridge when the state of an instance changes.
The following is example data for this event. In this example, the instance entered the pending state.
{ "id":"7bf73129-1428-4cd3-a780-95db273d1602", "detail-type":"EC2 Instance State-change Notification", "source":"aws.ec2", "account":"123456789012", "time":"2021-11-11T21:29:54Z", "region":"us-east-1", "resources":[ "arn:aws:ec2:us-east-1:123456789012:instance/i-1234567890abcdef0"
   ],

   "detail":{ "instance-id":"i-1234567890abcdef0", "state":"pending"
   } } The possible values for state are:
- pending
- running
- stopping
- stopped
- shutting-down
- terminated When you launch or start an instance, it enters the pending state and then the running state.
When you stop an instance, it enters the stopping state and then the stopped state. When you terminate an instance, it enters the shutting-down state and then the terminated state. For more information, see Amazon EC2 instance state changes.
### Create an alarm that sends an email when an Amazon EC2 instance changes state To receive email notifications when your instance changes state, create an Amazon SNS topic and then create an EventBridge rule for the EC2 Instance State-change Notification event.
To create an SNS topic
1. Open the Amazon SNS console at https://console.aws.amazon.com/sns/v3/home.
2. In the navigation pane, choose Topics.
3. Choose Create topic.
4. For Type, choose Standard.
5. For Name, enter a name for your topic.
6. Choose Create topic.
7. Choose Create subscription.
8. For Protocol, choose Email.

9. For Endpoint, enter the email address that receives the notifications.
10. Choose Create subscription.
11. You'll receive an email message with the following subject line: AWS Notification - Subscription Confirmation. Follow the directions to confirm your subscription.
To create an EventBridge rule
1. Open the Amazon EventBridge console at https://console.aws.amazon.com/events/.
2. Choose Create rule.
3. For Name, enter a name for your rule.
4. For Rule type, choose Rule with an event pattern.
5. Choose Next.
6. For Event pattern, do the following: a.
For Event source, choose AWS services. b.
For AWS service, choose EC2. c.
For Event type, choose EC2 Instance State-change Notification. d.
By default, we send notifications for any state change for any instance. If you prefer, you can select specific states or specific instances.
7. Choose Next.
8. Specify a target as follows: a.
For Target types, choose AWS service. b.
For Select a target, choose SNS topic. c.
For Topic, choose the SNS topic that you created in the previous procedure.
9. Choose Next.
10. (Optional) Add tags to your rule.
11. Choose Next.
12. Choose Create rule.
13. To test your rule, initiate a state change. For example, start a stopped instance, stop a running instance, or launch an instance. You'll receive email messages with the following subject line:
AWS Notification Message. The body of the email contains the event data.

## Scheduled events for Amazon EC2 instances To ensure infrastructure reliability and performance, AWS can schedule events to reboot, stop, and retire your instances. These events do not occur frequently.
If one of your instances will be affected by a scheduled event, AWS notifies you in advance by email, using the email address that's associated with your AWS account. The email provides details about the event, such as the start and end dates. Depending on the event type, you might be able to take action to control the timing of the event. AWS also sends an AWS Health event, which you can monitor and manage by using Amazon EventBridge. For more information, see Monitoring events in AWS Health with Amazon EventBridge.
Scheduled events are managed by AWS. You can't schedule events for your instances. However, you can:
- View scheduled events for your instances.
- Customize scheduled event notifications to include or remove tags from the email notification.
- Reschedule certain scheduled events.
- Create custom event windows for scheduled events.
- Take action when an instance is scheduled to reboot, stop, or retire.
To ensure that you receive notifications of scheduled events, verify your contact information on the Account page.
Note When an instance is affected by a scheduled event, and it is part of an Auto Scaling group, Amazon EC2 Auto Scaling eventually replaces it as part of its health checks, with no further action necessary on your part. For more information about the health checks performed by Amazon EC2 Auto Scaling, see Health checks for instances in an Auto Scaling group in the Amazon EC2 Auto Scaling User Guide.
### Types of scheduled events Amazon EC2 can create the following types of scheduled events for your instances, where the event occurs at a scheduled time:

Event type Event code Event action Instance stop instance-stop At the scheduled time, the instance is stopped.
When you start it again, it's migrated to a new host.
Applies only to instances with an Amazon EBS root volume.
Instance retirement instance-retirement At the scheduled time, the instance is stopped if it has an Amazon EBS root volume, or terminated if it has an instance store root volume.
Instance reboot instance-reboot At the scheduled time, the instance is rebooted. The instance stays on the host, and during the reboot, the host undergoes maintenance.
This is known as an in-place reboot.
System reboot system-reboot At the scheduled time, the instance is rebooted and migrated to a new host.
This is known as a reboot migration.
System maintenance system-maintenance At the scheduled time, the instance might be temporari ly affected by network maintenance or power maintenance.

### Determine the event type You can check what type of event is scheduled for your instance.
Console To determine the event type
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Events.
3. In the table, the event code appears in the Event type column.
4. To filter the table to show only the events for instances, in the search field choose Resource type: instance from the filter list.
AWS CLI To determine the event type for an instance Use the describe-instance-status command. If the instance has an associated scheduled event, the output provides information about the scheduled event. aws ec2 describe-instance-status \ --instance-id i-1234567890abcdef0 \ --query InstanceStatuses[].Events The following is example output. The scheduled event code is system-reboot.
[ "Events": [ { "InstanceEventId": "instance-event-0d59937288b749b32", "Code": "system-reboot", "Description": "The instance is scheduled for a reboot", "NotAfter": "2020-03-14T22:00:00.000Z", "NotBefore": "2020-03-14T20:00:00.000Z", "NotBeforeDeadline": "2020-04-05T11:00:00.000Z"
        } ]
]

PowerShell To determine the event type for an instance Use the Get-EC2InstanceStatus cmdlet. If the instance has an associated scheduled event, the output provides information about the scheduled event.
(Get-EC2InstanceStatus `
    -InstanceId i-1234567890abcdef0).Events The following is example output. The scheduled event code is system-reboot.
Code              : system-reboot Description       : The instance is scheduled for a reboot InstanceEventId   : instance-event-0d59937288b749b32 NotAfter          : 2020-03-14T22:00:00.000Z NotBefore         : 2020-03-14T20:00:00.000Z NotBeforeDeadline : 2020-04-05T11:00:00.000Z Contents
- Manage Amazon EC2 instances scheduled to stop or retire
- Manage Amazon EC2 instances scheduled for reboot
- Manage Amazon EC2 instances scheduled for maintenance
- View scheduled events that affect your Amazon EC2 instances
- Customize scheduled event notifications for your EC2 instances
- Reschedule a scheduled event for an EC2 instance
- Create custom event windows for scheduled events that affect your Amazon EC2 instances
### Manage Amazon EC2 instances scheduled to stop or retire When AWS detects irreparable failure of the underlying host for your instance, it schedules the instance to either stop or terminate, depending on the instance's root volume type.
- If the instance has an Amazon EBS root volume, the instance is scheduled to stop.
- If the instance has an instance store root volume, the instance is scheduled to terminate.

For more information, see Instance retirement.
Important Any data stored on instance store volumes is lost when an instance is stopped, hibernated, or terminated. This includes instance store volumes that are attached to an instance that has an EBS root volume. Be sure to save data from your instance store volumes that you might need later before the instance is stopped, hibernated, or terminated.
#### Actions you can take Actions you can take for instances with an EBS root volume When you receive a scheduled instance-stop event notification, you can take one of the following actions:
- Wait for scheduled stop: You can wait for the instance to stop within its scheduled maintenance window.
- Perform manual stop and start: You can stop and start the instance yourself at a time that suits you, which migrates it to a new host. This is not the same as rebooting the instance. For more information, see Stop and start Amazon EC2 instances.
- Automate stop and start: You can automate an immediate stop and start in response to a scheduled instance-stop event. For more information, see Running operations on EC2 instances automatically in response to events in AWS Health in the AWS Health User Guide.
Actions you can take for instances with an instance store root volume When you receive a scheduled system-retirement event notification, and you want to retain your data, you can take the following actions:
1. Launch a replacement instance from your most recent AMI.
2. Migrate all necessary data to the replacement instance before the instance is scheduled to terminate.
3. Terminate the original instance, or wait for it to terminate as scheduled.
For more information about the actions you can take, see Instance retirement.

### Manage Amazon EC2 instances scheduled for reboot When AWS must perform tasks such as installing updates or maintaining the underlying host, it can schedule an instance reboot. During the scheduled reboot, the instance either stays on the same host, or migrates to a different host, depending on the event, as follows:
- instance-reboot event
- During the reboot, the instance remains on the host. This is known as an in-place reboot.
- The current host undergoes maintenance.
- Typically completes in seconds.
- system-reboot event
- During the reboot, the instance is migrated to a new host. This is known as a reboot migration.
- Typically completes in minutes.
To check what type of event is scheduled for your instance, see Determine the event type.
#### Actions you can take When you receive a scheduled instance-reboot or system-reboot event notification, you can take one of the following actions:
- Wait for scheduled reboot: You can wait for the instance reboot to occur within its scheduled maintenance window.
- Reschedule the reboot: You can reschedule the instance reboot to a date and time that suits you.
- Perform a user-initiated reboot: You can manually reboot the instance yourself at a time that suits you. However, the outcome depends on the event:
- instance-reboot event – Your instance remains on the current hardware (in-place reboot), no host maintenance takes place, and the event stays open.
- system-reboot event
- If reboot migration is enabled on your instance, a user-initiated reboot attempts to migrate your instance to new hardware. If successful, the event is cleared. If unsuccessful, an in-place reboot occurs and the event remains scheduled.
- If reboot migration is disabled on your instance, a user-initiated reboot keeps the instance on the same hardware (in-place reboot), no host maintenance takes place, and the event

remains scheduled. When the scheduled event eventually takes place, AWS will move your instance to new hardware (reboot migration).
After AWS reboots your instance The following applies after AWS reboots your instance:
- The scheduled event is cleared.
- The event description is updated.
- For an instance-reboot event:
- Maintenance of the underlying host is complete.
- For a system-reboot event:
- The instance moves to a new host.
- The instance retains its IP address and DNS name.
- Any data on local instance store volumes is preserved.
- You can use your instance after it has fully booted.
Alternative options If you can't reschedule the reboot event or enable reboot migration for a user-initiated reboot, but want to maintain normal operation during the scheduled maintenance window, you can do the following:
- For an instance with an EBS root volume
- Manually stop and start the instance to migrate it to a new host. This is not the same as manually rebooting the instance, where the instance stays on the same host.
- Optionally, automate an immediate instance stop and start in response to the scheduled reboot event. For more information, see Running operations on EC2 instances automatically in response to events in AWS Health in the AWS Health User Guide.
Important The data on instance store volumes is lost when an instance is stopped. For more information, see Stop and start Amazon EC2 instances.
- For an instance with an instance store root volume

1. Launch a replacement instance from your most recent AMI.
2. Migrate all necessary data to the replacement instance before the scheduled maintenance window.
3. Terminate the original instance.
#### Enable or disable reboot migration When an instance is scheduled for a system-reboot event, you can reboot it before the event.
The outcome of a user-initiated reboot depends on the instance's reboot migration setting:
- Enabled – A user-initiated reboot attempts to migrate your instance to new hardware (reboot migration). If successful, the event is cleared. If unsuccessful, an in-place reboot occurs and the event remains scheduled. Note that even when enabled, reboot migration can only occur if your instance meets the reboot migration requirements.
- Disabled – A user-initiated reboot keeps the instance on the same hardware (in-place reboot), no host maintenance takes place, and the event remains scheduled. When the scheduled event eventually takes place, AWS will move your instance to new hardware (reboot migration).
A reboot with migration takes longer than an in-place reboot:
- In-place reboot: Approximately 30 seconds
- Reboot with migration: Several minutes Note Instances that receive a system-reboot event notification are enabled for user-initiated reboot migration by default.
##### Requirements for enabling reboot migration Reboot migration can be enabled on instances that meet the following criteria:
Instance types Not all instance types support enabling reboot migration. You can view the instance types that support enabling reboot migration.

Console To view the instance types that support enabling reboot migration
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the left navigation pane, choose Instance Types.
3. In the filter bar, enter Reboot Migration support: supported. As you enter the characters and the filter name appears, you can select it.
The Instance types table displays all the instance types that support enabling reboot migration.
AWS CLI To view the instance types that support enabling reboot migration Use the describe-instance-types command with the reboot-migration-support filter. aws ec2 describe-instance-types \ --filters Name=reboot-migration-support,Values=supported \ --query "InstanceTypes[*].[InstanceType]" \ --output text | sort PowerShell To view the instance types that support enabling reboot migration Use the Get-EC2InstanceType cmdlet with the reboot-migration-support filter.
Get-EC2InstanceType `
    -Filter @{Name="reboot-migration-support";Values="true"} | `
    Select InstanceType | Sort-Object InstanceType Tenancy
- Shared
- Dedicated Instance For more information, see Amazon EC2 Dedicated Instances.
Limitations

Reboot migration is not supported for instances with the following characteristics:
- Platform: Instances running natively on the Xen hypervisor
- Instance size: metal instances
- Tenancy: Dedicated Host. For Dedicated Hosts, use Dedicated Host Auto Recovery instead.
- Storage: Instances with instance store volumes
- Networking: Instances using an Elastic Fabric Adapter
- Auto Scaling: Instances that are part of an Auto Scaling group
##### Steps for enabling or disabling reboot migration When an instance receives a system-reboot event, it is enabled for reboot migration by default.
You can disable reboot migration so that during a user-initiated reboot, the instance stays on the same hardware (in-place reboot).
The default configuration doesn't enable reboot migration for an unsupported instance. For more information, see Requirements for enabling reboot migration.
You can disable or enable reboot migration on a running or stopped instance.
AWS CLI To disable reboot migration Use the modify-instance-maintenance-options command and set the --reboot-migration parameter to disabled. aws ec2 modify-instance-maintenance-options \ --instance-id i-0abcdef1234567890 \ --reboot-migration disabled To enable reboot migration Use the modify-instance-maintenance-options command and set the --reboot-migration parameter to default. aws ec2 modify-instance-maintenance-options \

    --instance-id i-0abcdef1234567890 \ --reboot-migration default PowerShell To disable reboot migration Use the Edit-EC2InstanceMaintenanceOption cmdlet.
Edit-EC2InstanceMaintenanceOption `
    -InstanceId  `
    -RebootMigration Disabled To enable reboot migration Use the Edit-EC2InstanceMaintenanceOption cmdlet.
Edit-EC2InstanceMaintenanceOption `
    -InstanceId i-1234567890abcdef0 `
    -RebootMigration Enabled
### Manage Amazon EC2 instances scheduled for maintenance When AWS must maintain the underlying host for an instance, it schedules the instance for maintenance. There are two types of maintenance events: network maintenance and power maintenance.
- During network maintenance, scheduled instances lose network connectivity for a brief period of time. Normal network connectivity to your instance is restored after maintenance is complete.
- During power maintenance, scheduled instances are taken offline for a brief period, and then rebooted. When a reboot is performed, all of your instance's configuration settings are retained.
After your instance has rebooted (this normally takes a few minutes), verify that your application is working as expected. At this point, your instance should no longer have a scheduled event associated with it, or if it does, the description of the scheduled event begins with [Completed].
It sometimes takes up to 1 hour for the instance status description to refresh. Completed maintenance events are displayed on the Amazon EC2 console dashboard for up to a week.

#### Actions you can take Actions you can take for instances with an EBS root volume When you receive a system-maintenance event notification, you can take one of the following actions:
- Wait for scheduled maintenance: You can wait for the maintenance to occur as scheduled.
- Perform manual stop and stop: You can stop and start the instance, which migrates it to a new host. This is not the same as rebooting the instance. For more information, see Stop and start Amazon EC2 instances.
- Automate stop and start: You can automate an immediate stop and start in response to a scheduled maintenance event. For more information, see Running operations on EC2 instances automatically in response to events in AWS Health in the AWS Health User Guide.
Actions you can take for instances with an instance store root volume When you receive a system-maintenance event notification, you can take one of the following actions:
- Wait for scheduled maintenance: You can wait for the maintenance to occur as scheduled.
- Launch a replacement instance: If you want to maintain normal operation during the scheduled maintenance window:
1. Launch a replacement instance from your most recent AMI.
2. Migrate all necessary data to the replacement instance before the scheduled maintenance window.
3. Terminate the original instance.
### View scheduled events that affect your Amazon EC2 instances In addition to receiving notification of scheduled events in email, you can check for scheduled events.
Console To view scheduled events for your instances
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.

2. The dashboard displays any resources with an associated event under Scheduled events.
3. For more detail, choose Events in the navigation pane. Any resources with an associated event are displayed. You can filter by characteristics such as event type, resource type, and Availability Zone.
AWS CLI To view scheduled events for your instances Use the describe-instance-status command. aws ec2 describe-instance-status \ --instance-id i-1234567890abcdef0 \ --query "InstanceStatuses[].Events"
The following example output shows a reboot event.
[ "Events": [ { "InstanceEventId": "instance-event-0d59937288b749b32", "Code": "system-reboot", "Description": "The instance is scheduled for a reboot",

            "NotAfter": "2019-03-15T22:00:00.000Z", "NotBefore": "2019-03-14T20:00:00.000Z", "NotBeforeDeadline": "2019-04-05T11:00:00.000Z"
         } ]
]
The following example output shows an instance retirement event.
[ "Events": [ { "InstanceEventId": "instance-event-0e439355b779n26",

            "Code": "instance-stop", "Description": "The instance is running on degraded hardware", "NotBefore": "2015-05-23T00:00:00.000Z"
        } ]
]
PowerShell To view scheduled events for your instances Use the following Get-EC2InstanceStatus command.
(Get-EC2InstanceStatus -InstanceId i-1234567890abcdef0).Events The following example output shows an instance retirement event.
Code         : instance-stop Description  : The instance is running on degraded hardware NotBefore    : 5/23/2015 12:00:00 AM Instance metadata To view scheduled events for your instances using instance metadata You can retrieve information about active maintenance events for your instances from the instance metadata by using Instance Metadata Service Version 2 or Instance Metadata Service Version 1.

IMDSv2 [ec2-user ~]$ TOKEN=`curl -X PUT "http://169.254.169.254/latest/api/token" -H "X- aws-ec2-metadata-token-ttl-seconds: 21600"` \ && curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta- data/events/maintenance/scheduled IMDSv1 [ec2-user ~]$ curl http://169.254.169.254/latest/meta-data/events/maintenance/ scheduled The following is example output with information about a scheduled system reboot event, in JSON format.
[ { "NotBefore" : "21 Jan 2019 09:00:43 GMT", "Code" : "system-reboot", "Description" : "scheduled reboot", "EventId" : "instance-event-0d59937288b749b32", "NotAfter" : "21 Jan 2019 09:17:23 GMT", "State" : "active"
  } ]
To view event history about completed or canceled events for your instances using instance metadata You can retrieve information about completed or canceled events for your instances from instance metadata by using Instance Metadata Service Version 2 or Instance Metadata Service Version 1.
IMDSv2 [ec2-user ~]$ TOKEN=`curl -X PUT "http://169.254.169.254/latest/api/token" -H "X- aws-ec2-metadata-token-ttl-seconds: 21600"` \ && curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta- data/events/maintenance/history

IMDSv1 [ec2-user ~]$ curl http://169.254.169.254/latest/meta-data/events/maintenance/ history The following is example output with information about a system reboot event that was canceled, and a system reboot event that was completed, in JSON format.
[ { "NotBefore" : "21 Jan 2019 09:00:43 GMT", "Code" : "system-reboot", "Description" : "[Canceled] scheduled reboot", "EventId" : "instance-event-0d59937288b749b32", "NotAfter" : "21 Jan 2019 09:17:23 GMT", "State" : "canceled"
  }, { "NotBefore" : "29 Jan 2019 09:00:43 GMT", "Code" : "system-reboot", "Description" : "[Completed] scheduled reboot", "EventId" : "instance-event-0d59937288b749b32", "NotAfter" : "29 Jan 2019 09:17:23 GMT", "State" : "completed"
  } ]
AWS Health You can use the AWS Health Dashboard to learn about events that can affect your instance. The Health Dashboard organizes issues in three groups: open issues, scheduled changes, and other notifications. The scheduled changes group contains items that are ongoing or upcoming.
For more information, see Getting started with your AWS Health Dashboard in the AWS Health User Guide.
### Customize scheduled event notifications for your EC2 instances You can customize scheduled event notifications to include tags in the email notification. This makes it easier to identify the affected resource (instances or Dedicated Hosts) and to prioritize actions for the upcoming event.

When you customize event notifications to include tags, you can choose to include:
- All of the tags that are associated with the affected resource
- Only specific tags that are associated with the affected resource For example, suppose that you assign application, costcenter, project, and owner tags to all of your instances. You can choose to include all of the tags in event notifications. Alternatively, if you'd like to see only the owner and project tags in event notifications, then you can choose to include only those tags.
After you select the tags to include, the event notifications will include the resource ID (instance ID or Dedicated Host ID) and the tag key and value pairs that are associated with the affected resource.
Tasks
- Include tags in event notifications
- Remove tags from event notifications
- View the tags to be included in event notifications
#### Include tags in event notifications The tags that you choose to include apply to all resources (instances and Dedicated Hosts) in the selected Region. To customize event notifications in other Regions, first select the required Region and then perform the following steps.
Console To include tags in event notifications
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Events.
3. Choose Actions, Manage event notifications.
4. Turn on Include tags in event notifications.
5. Do one of the following, depending on the tags that you want to include in event notifications:
- To include all tags associated with the affected instance or Dedicated Host, select Include all tags.

- To select the tags to include, select Choose the tags to include and then select or enter the tag keys.
6. Choose Save.
AWS CLI To include all tags in event notifications Use the register-instance-event-notification-attributes command and set the IncludeAllTagsOfInstance parameter to true. aws ec2 register-instance-event-notification-attributes \ --instance-tag-attribute "IncludeAllTagsOfInstance=true"
To include specific tags in event notifications Use the register-instance-event-notification-attributes command and specify the tags to include by using the InstanceTagKeys parameter. aws ec2 register-instance-event-notification-attributes \ --instance-tag-attribute 'InstanceTagKeys=["tag_key_1", "tag_key_2", "tag_key_3"]'
PowerShell To include all tags in event notifications Use the Register-EC2InstanceEventNotificationAttribute cmdlet.
Register-EC2InstanceEventNotificationAttribute `
    -InstanceTagAttribute_IncludeAllTagsOfInstance $true To include specific tags in event notifications Use the Register-EC2InstanceEventNotificationAttribute cmdlet.
Register-EC2InstanceEventNotificationAttribute `
    -InstanceTagAttribute_InstanceTagKey tag_key_1, tag_key_2, tag_key_3

#### Remove tags from event notifications You can remove tags from event notifications.
Console To remove tags from event notifications
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Events.
3. Choose Actions, Manage event notifications.
4. To remove all tags from event notifications, turn off Include tags in event notifications.
5. To remove specific tags from event notifications, choose the X) for the corresponding tag keys.
6. Choose Save.
AWS CLI To remove all tags from event notifications Use the deregister-instance-event-notification-attributes command and set the IncludeAllTagsOfInstance parameter to false. aws ec2 deregister-instance-event-notification-attributes \ --instance-tag-attribute "IncludeAllTagsOfInstance=false"
To remove a tag from event notifications Use the deregister-instance-event-notification-attributes command and specify the tags to remove by using the InstanceTagKeys parameter. aws ec2 deregister-instance-event-notification-attributes \ --instance-tag-attribute 'InstanceTagKeys=["tag_key_3"]'
PowerShell To remove all tags from event notifications Use the Unregister-EC2InstanceEventNotificationAttribute cmdlet.

Unregister-EC2InstanceEventNotificationAttribute `
    -InstanceTagAttribute_IncludeAllTagsOfInstance $false To remove a tag from event notifications Use the Unregister-EC2InstanceEventNotificationAttribute cmdlet.
Unregister-EC2InstanceEventNotificationAttribute `
    -InstanceTagAttribute_InstanceTagKey tag_key_3
#### View the tags to be included in event notifications You can view the tags that are to be included in event notifications.
Console To view the tags that are to be included in event notifications
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Events.
3. Choose Actions, Manage event notifications.
AWS CLI To view the tags to be included in event notifications Use the describe-instance-event-notification-attributes command. aws ec2 describe-instance-event-notification-attributes PowerShell To view the tags to be included in event notifications Use the Get-EC2InstanceEventNotificationAttribute cmdlet.
Get-EC2InstanceEventNotificationAttribute

### Reschedule a scheduled event for an EC2 instance You can reschedule an event so that it occurs at a specific date and time that suits you. After you reschedule an event, it might take a minute or two before the the updated date is displayed.
Limitations
- Only events with an event deadline date can be rescheduled. The event can be rescheduled up to the event deadline date. The event deadline date is indicated in the Deadline column (console) and the NotBeforeDeadline field (AWS CLI).
- Only events that have not yet started can be rescheduled. The start time is indicated in the Start time column (console) and the NotBefore field (AWS CLI). Events that are scheduled to start in the next 5 minutes can't be rescheduled.
- The new event start time must be at least 60 minutes from the current time.
- If you reschedule multiple events using the console, the event deadline date is determined by the event with the earliest event deadline date.
Console To reschedule an event
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Events.
3. Choose Resource type: instance from the filter list.
4. Select one or more instances, and then choose Actions, Schedule event.
Only events that have an event deadline date, indicated by a value for Deadline, can be rescheduled. If one of the selected events does not have a deadline date, Actions, Schedule event is disabled.
5. For New start time, enter a new date and time for the event. The new date and time must occur before the Event deadline.
6. Choose Save.
It might take a minute or two for the updated event start time to be reflected in the console.

AWS CLI To reschedule an event Use the modify-instance-event-start-time command. aws ec2 modify-instance-event-start-time \ --instance-id i-1234567890abcdef0 \ --instance-event-id instance-event-0d59937288b749b32 \ --not-before 2020-03-25T10:00:00.000 PowerShell To reschedule an event Use the Edit-EC2InstanceEventStartTime cmdlet.
Edit-EC2InstanceEventStartTime `
    -InstanceId i-1234567890abcdef0 `
    -InstanceEventId instance-event-0d59937288b749b32 `
    -NotBefore 2020-03-25T10:00:00.000
### Create custom event windows for scheduled events that affect your Amazon EC2 instances instances You can define custom event windows that recur weekly for scheduled events that reboot, stop, or terminate your Amazon EC2 instances. You can associate one or more instances with an event window. If a scheduled event for those instances is planned, AWS will schedule the events within the associated event window.
You can use event windows to maximize workload availability by specifying event windows that occur during off-peak periods for your workload. You can also align the event windows with your internal maintenance schedules.
You define an event window by specifying a set of time ranges. The minimum time range is 2 hours. The combined time ranges must total at least 4 hours.
You can associate one or more instances with an event window by using either instance IDs or instance tags. You can also associate Dedicated Hosts with an event window by using the host ID.

Warning Event windows are applicable only for scheduled events that stop, reboot, or terminate instances.
Event windows are not applicable for:
- Expedited scheduled events and network maintenance events.
- Unscheduled maintenance such as automatic instance recovery and unplanned reboots.
Work with event windows
- Considerations
- Create an event window
- Associate a target with an event window
- Disassociate a target from an event window
- Modify an event window
- Delete an event window
#### Considerations
- All event window times are in UTC.
- An event window can contain multiple time ranges. While each individual range must be at least 2 hours, the total duration across all ranges must be at least 4 hours.
- Only one target type (instance ID, Dedicated Host ID, or instance tag) can be associated with an event window.
- A target (instance ID, Dedicated Host ID, or instance tag) can only be associated with one event window.
- A maximum of 100 instance IDs, or 50 Dedicated Host IDs, or 50 instance tags can be associated with an event window. The instance tags can be associated with any number of instances.
- A maximum of 200 event windows can be created per AWS Region.
- Multiple instances that are associated with event windows can potentially have scheduled events occur at the same time.
- If AWS has already scheduled an event, modifying an event window won't change the time of the scheduled event. If the event has a deadline date, you can reschedule the event.

- You can stop and start an instance before the scheduled event. This migrates the instance to a new host and clears the event.
#### Create an event window You can create one or more event windows. For each event window, you specify one or more blocks of time. For example, you can create an event window with blocks of time that occur every day at 4 AM for 2 hours. Or you can create an event window with blocks of time that occur on Sundays from 2 AM to 4 AM and on Wednesdays from 3 AM to 5 AM.
Event windows recur weekly until you delete them.
Console To create an event window
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Events.
3. Choose Actions, Manage event windows.
4. Choose Create instance event window.
5. For Event window name, enter a descriptive name for the event window.
6. For Event window schedule, choose to specify the blocks of time in the event window by using the cron schedule builder or by specifying time ranges.
- If you choose Cron schedule builder, specify the following:
1. For Days (UTC), specify the days of the week on which the event window occurs.
2. For Start time (UTC), specify the time when the event window begins.
3. For Duration, specify the duration of the blocks of time in the event window. The minimum duration per block of time is 2 hours. The minimum duration of the event window must equal or exceed 4 hours in total. All times are in UTC.
- If you choose Time ranges, choose Add new time range and specify the start day and time and the end day and time. Repeat for each time range. The minimum duration per time range is 2 hours. The minimum duration for all time ranges combined must equal or exceed 4 hours in total.
7. (Optional) For Target details, associate one or more instances with the event window. Use instance IDs or instance tags to associate instances. Use host IDs to associate Dedicated

Hosts. When these targets are scheduled for maintenance, the event will occur during this event window.
Note that you can create the event window without associating a target with the window.
Later, you can modify the window to associate one or more targets.
8. (Optional) For Event window tags, choose Add tag, and enter the key and value for the tag. Repeat for each tag.
9. Choose Create event window.
AWS CLI To create an event window with a time range Use the create-instance-event-window command. aws ec2 create-instance-event-window \ --time-range StartWeekDay=monday,StartHour=2,EndWeekDay=wednesday,EndHour=8 \ --tag-specifications "ResourceType=instance-event- window,Tags=[{Key=K1,Value=V1}]" \ --name myEventWindowName The following is example output.
{ "InstanceEventWindow": { "InstanceEventWindowId": "iew-0abcdef1234567890", "TimeRanges": [ { "StartWeekDay": "monday", "StartHour": 2, "EndWeekDay": "wednesday", "EndHour": 8 } ], "Name": "myEventWindowName", "State": "creating", "Tags": [ { "Key": "K1", "Value": "V1"
            }

        ]
    } } To create an event window with a cron expression Use the create-instance-event-window command. aws ec2 create-instance-event-window \ --cron-expression "* 21-23 * * 2,3" \ --tag-specifications "ResourceType=instance-event- window,Tags=[{Key=K1,Value=V1}]" \ --name myEventWindowName The following is example output.
{ "InstanceEventWindow": { "InstanceEventWindowId": "iew-0abcdef1234567890", "Name": "myEventWindowName", "CronExpression": "* 21-23 * * 2,3", "State": "creating", "Tags": [ { "Key": "K1", "Value": "V1"
            } ]
    } } PowerShell To create an event window with a time range Use the New-EC2InstanceEventWindow cmdlet.
$timeRange = New-Object Amazon.EC2.Model.InstanceEventWindowTimeRangeRequest $timeRange.StartWeekDay = "monday"
$timeRange.EndWeekDay = "wednesday"
$timeRange.StartHour = 2 $timeRange.EndHour = 8

$tag = @{Key="key1"; Value="value1"} $tagspec = New-Object Amazon.EC2.Model.TagSpecification $tagspec.ResourceType = "instance-event-window"
$tagspec.Tags.Add($tag)
New-EC2InstanceEventWindow `
    -Name my-event-window `
    -TagSpecification $tagspec `
    -TimeRange @($timeRange)
The following is example output.
AssociationTarget     :
CronExpression        :
InstanceEventWindowId : iew-0abcdef1234567890 Name                  : my-event-window State                 : creating Tags                  : {key1} TimeRanges            : {Amazon.EC2.Model.InstanceEventWindowTimeRange} To create an event window with a cron expression Use the New-EC2InstanceEventWindow cmdlet.
$tag = @{Key="key1"; Value="value1"} $tagspec = New-Object Amazon.EC2.Model.TagSpecification $tagspec.ResourceType = "instance-event-window"
$tagspec.Tags.Add($tag)
New-EC2InstanceEventWindow `
    -Name my-event-window `
    -TagSpecification $tagspec`
    -CronExpression "* 21-23 * * 2,3"
The following is example output.
AssociationTarget     :
CronExpression        : * 21-23 * * 2,3 InstanceEventWindowId : iew-0abcdef1234567890 Name                  : my-event-window State                 : creating Tags                  : {key1} TimeRanges            : {}

#### Associate a target with an event window After you create an event window, you can associate targets with the event window. You can associate only one type of target with an event window. You can specify instance IDs, Dedicated Host IDs, or instance tags.
Console To associate targets with an event window
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Events.
3. Select the event window to modify.
4. Choose Actions, Modify instance event window.
AWS CLI To associate instance tags with an event window Use the associate-instance-event-window command. aws ec2 associate-instance-event-window \ --instance-event-window-id iew-0abcdef1234567890 \ --association-target "InstanceTags=[{Key=k2,Value=v2},{Key=k1,Value=v1}]"
The following is example output.
{ "InstanceEventWindow": { "InstanceEventWindowId": "iew-0abcdef1234567890", "Name": "myEventWindowName", "CronExpression": "* 21-23 * * 2,3", "AssociationTarget": { "InstanceIds": [], "Tags": [ { "Key": "k2", "Value": "v2"
                }, { "Key": "k1",

                    "Value": "v1"
                } ], "DedicatedHostIds": []
        }, "State": "creating"
    } } To associate instance IDs with an event window Use the associate-instance-event-window command. aws ec2 associate-instance-event-window \ --instance-event-window-id iew-0abcdef1234567890 \ --association-target "InstanceIds=i-1234567890abcdef0,i-0598c7d356eba48d7"
The following is example output.
{ "InstanceEventWindow": { "InstanceEventWindowId": "iew-0abcdef1234567890", "Name": "myEventWindowName", "CronExpression": "* 21-23 * * 2,3", "AssociationTarget": { "InstanceIds": [ "i-1234567890abcdef0", "i-0598c7d356eba48d7"
            ], "Tags": [], "DedicatedHostIds": []
        }, "State": "creating"
    } } To associate a Dedicated Host with an event window Use the associate-instance-event-window command. aws ec2 associate-instance-event-window \ --instance-event-window-id iew-0abcdef1234567890 \

    --association-target "DedicatedHostIds=h-029fa35a02b99801d"
The following is example output.
{ "InstanceEventWindow": { "InstanceEventWindowId": "iew-0abcdef1234567890", "Name": "myEventWindowName", "CronExpression": "* 21-23 * * 2,3", "AssociationTarget": { "InstanceIds": [], "Tags": [], "DedicatedHostIds": [ "h-029fa35a02b99801d"
            ]
        }, "State": "creating"
    } } PowerShell To associate instance tags with an event window Use the Register-EC2InstanceEventWindow cmdlet.
$tag1 = @{Key="key1"; Value="value1"} $tag2 = @{Key="key2"; Value="value2"} Register-EC2InstanceEventWindow `
    -InstanceEventWindowId iew-0abcdef1234567890 `
    -AssociationTarget_InstanceTag @($tag1,$tag2)
To associate instance IDs with an event window Use the Register-EC2InstanceEventWindow cmdlet.
Register-EC2InstanceEventWindow `
    -InstanceEventWindowId iew-0abcdef1234567890 `
    -AssociationTarget_InstanceId i-1234567890abcdef0, i-0598c7d356eba48d7 To associate a Dedicated Host with an event window Use the Register-EC2InstanceEventWindow cmdlet.

Register-EC2InstanceEventWindow `
    -InstanceEventWindowId iew-0abcdef1234567890 `
    -AssociationTarget_DedicatedHostId h-029fa35a02b99801d
#### Disassociate a target from an event window Console To disassociate targets with an event window
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Events.
3. Select the event window to modify.
4. Choose Actions, Modify instance event window.
AWS CLI To disassociate instance tags from an event window Use the disassociate-instance-event-window command. aws ec2 disassociate-instance-event-window \ --instance-event-window-id iew-0abcdef1234567890 \ --association-target "InstanceTags=[{Key=k2,Value=v2},{Key=k1,Value=v1}]"
The following is example output.
{ "InstanceEventWindow": { "InstanceEventWindowId": "iew-0abcdef1234567890", "Name": "myEventWindowName", "CronExpression": "* 21-23 * * 2,3", "AssociationTarget": { "InstanceIds": [], "Tags": [], "DedicatedHostIds": []
        }, "State": "creating"
    }

} To disassociate instance IDs from an event window Use the disassociate-instance-event-window command. aws ec2 disassociate-instance-event-window \ --instance-event-window-id iew-0abcdef1234567890 \ --association-target "InstanceIds=i-1234567890abcdef0,i-0598c7d356eba48d7"
The following is example output.
{ "InstanceEventWindow": { "InstanceEventWindowId": "iew-0abcdef1234567890", "Name": "myEventWindowName", "CronExpression": "* 21-23 * * 2,3", "AssociationTarget": { "InstanceIds": [], "Tags": [], "DedicatedHostIds": []
        }, "State": "creating"
    } } To disassociate a Dedicated Host from an event window Use the disassociate-instance-event-window command. aws ec2 disassociate-instance-event-window \ --instance-event-window-id iew-0abcdef1234567890 \ --association-target DedicatedHostIds=h-029fa35a02b99801d The following is example output.
{ "InstanceEventWindow": { "InstanceEventWindowId": "iew-0abcdef1234567890", "Name": "myEventWindowName", "CronExpression": "* 21-23 * * 2,3", "AssociationTarget": {

            "InstanceIds": [], "Tags": [], "DedicatedHostIds": []
        }, "State": "creating"
    } } PowerShell To disassociate instance tags from an event window Use the Unregister-EC2InstanceEventWindow cmdlet.
$tag1 = @{Key="key1"; Value="value1"} $tag2 = @{Key="key2"; Value="value2"} Unregister-EC2InstanceEventWindow `
    -InstanceEventWindowId iew-0abcdef1234567890 `
    -AssociationTarget_InstanceTag @($tag1, $tag2)
To disassociate instance IDs from an event window Use the Unregister-EC2InstanceEventWindow cmdlet.
Unregister-EC2InstanceEventWindow `
    -InstanceEventWindowId iew-0abcdef1234567890 `
    -AssociationTarget_InstanceId i-1234567890abcdef0, i-0598c7d356eba48d7 To disassociate a Dedicated Host from an event window Use the Unregister-EC2InstanceEventWindow cmdlet.
Unregister-EC2InstanceEventWindow `
    -InstanceEventWindowId iew-0abcdef1234567890 `
    -AssociationTarget_DedicatedHostId h-029fa35a02b99801d
#### Modify an event window You can modify all of the fields of an event window except its ID. For example, when daylight savings begin, you might want to modify the event window schedule. For existing event windows, you might want to add or remove targets.

You can modify either a time range or a cron expression when modifying the event window, but not both.
Console To modify an event window
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Events.
3. Choose Actions, Manage event windows.
4. Select the event window to modify, and then choose Actions, Modify instance event window.
5. Modify the fields in the event window, and then choose Modify event window.
AWS CLI To modify the time range of an event window Use the modify-instance-event-window command. aws ec2 modify-instance-event-window --instance-event-window-id iew-0abcdef1234567890 \ --time-range StartWeekDay=monday,StartHour=2,EndWeekDay=wednesday,EndHour=8 The following is example output.
{ "InstanceEventWindow": { "InstanceEventWindowId": "iew-0abcdef1234567890", "TimeRanges": [ { "StartWeekDay": "monday", "StartHour": 2, "EndWeekDay": "wednesday", "EndHour": 8 } ], "Name": "myEventWindowName", "AssociationTarget": {

            "InstanceIds": [ "i-0abcdef1234567890", "i-0be35f9acb8ba01f0"
            ], "Tags": [], "DedicatedHostIds": []
        }, "State": "creating", "Tags": [ { "Key": "K1", "Value": "V1"
            } ]
    } } To modify a set of time ranges for an event window Use the modify-instance-event-window command. aws ec2 modify-instance-event-window --instance-event-window-id iew-0abcdef1234567890 \ --time-range '[{"StartWeekDay": "monday", "StartHour": 2, "EndWeekDay":
 "wednesday", "EndHour": 8}, {"StartWeekDay": "thursday", "StartHour": 2, "EndWeekDay": "friday", "EndHour": 8}]'
The following is example output.
{ "InstanceEventWindow": { "InstanceEventWindowId": "iew-0abcdef1234567890", "TimeRanges": [ { "StartWeekDay": "monday", "StartHour": 2, "EndWeekDay": "wednesday", "EndHour": 8 }, { "StartWeekDay": "thursday", "StartHour": 2,

                "EndWeekDay": "friday", "EndHour": 8 } ], "Name": "myEventWindowName", "AssociationTarget": { "InstanceIds": [ "i-0abcdef1234567890", "i-0be35f9acb8ba01f0"
            ], "Tags": [], "DedicatedHostIds": []
        }, "State": "creating", "Tags": [ { "Key": "K1", "Value": "V1"
            } ]
    } } To modify the cron expression of an event window Use the modify-instance-event-window command. aws ec2 modify-instance-event-window --instance-event-window-id iew-0abcdef1234567890 \ --cron-expression "* 21-23 * * 2,3"
The following is example output.
{ "InstanceEventWindow": { "InstanceEventWindowId": "iew-0abcdef1234567890", "Name": "myEventWindowName", "CronExpression": "* 21-23 * * 2,3", "AssociationTarget": { "InstanceIds": [ "i-0abcdef1234567890", "i-0be35f9acb8ba01f0"
            ],

            "Tags": [], "DedicatedHostIds": []
        }, "State": "creating", "Tags": [ { "Key": "K1", "Value": "V1"
            } ]
    } } PowerShell To modify the time range of an event window Use the Edit-EC2InstanceEventWindow cmdlet.
$timeRange1 = New-Object Amazon.EC2.Model.InstanceEventWindowTimeRangeRequest $timeRange1.StartWeekDay = "monday"
$timeRange1.EndWeekDay = "wednesday"
$timeRange1.StartHour = 2 $timeRange1.EndHour = 8 $timeRange2 = New-Object Amazon.EC2.Model.InstanceEventWindowTimeRangeRequest $timeRange2.StartWeekDay = "thursday"
$timeRange2.EndWeekDay = "friday"
$timeRange2.StartHour = 1 $timeRange2.EndHour = 6 Edit-EC2InstanceEventWindow `
    -InstanceEventWindowId iew-0abcdef1234567890 `
    -TimeRange @($timeRange1, $timeRange2)
To modify the cron expression of an event window Use the Edit-EC2InstanceEventWindow cmdlet.
Edit-EC2InstanceEventWindow `
    -InstanceEventWindowId iew-0abcdef1234567890 `
    -CronExpression "* 21-23 * * 2,3"

#### Delete an event window You can delete one event window at a time.
Console To delete an event window
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Events.
3. Choose Actions, Manage event windows.
4. Select the event window to delete, and then choose Actions, Delete instance event window.
5. When prompted, enter delete, and then choose Delete.
AWS CLI To delete an event window Use the delete-instance-event-window command and specify the event window to delete. aws ec2 delete-instance-event-window \ --instance-event-window-id iew-0abcdef1234567890 To force-delete an event window Use the --force-delete parameter if the event window is currently associated with targets. aws ec2 delete-instance-event-window \ --instance-event-window-id iew-0abcdef1234567890 \ --force-delete PowerShell To delete an event window Use the Remove-EC2InstanceEventWindow cmdlet.
Remove-EC2InstanceEventWindow `
