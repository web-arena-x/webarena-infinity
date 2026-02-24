# Automatic instance recovery

Source: apps/user-manuals/aws/ec2-ug.pdf

---

Transfer your data to an EBS volume, take a snapshot of the volume, and then create AMI from the snapshot. You can launch a replacement instance from your new AMI. For more information, see Convert your Amazon S3-backed AMI to an EBS-backed AMI.
# Automatic instance recovery Important This section describes how to proactively configure recovery mechanisms on an EC2 instance. These recovery mechanisms are designed to restore instance availability when AWS detects an underlying hardware or software issue that causes a system status check to fail. If you are currently experiencing problems accessing your instance, see Troubleshoot EC2 instances.
If AWS detects that an instance is unavailable due to an underlying hardware or software issue, there are two mechanisms that can automatically restore instance availability—simplified automatic recovery and Amazon CloudWatch action based recovery. Restoring instance availability is also known as instance recovery.
During the instance recovery process, AWS will attempt to move your instance from the host with the underlying hardware or software issue to a different host. If successful, the instance recovery process will appear to the instance as an unplanned reboot. You can verify if instance recovery occurred.
If the recovery process is unsuccessful, the instance might continue running on the host with the underlying hardware or software issue. In this case, manual intervention is required. If the instance becomes unreachable or the system status check continues to fail, we recommend that you manually stop and start the instance. When you start an instance, it is typically migrated to a new underlying host computer. However, unlike automatic instance recovery, where the instance retains its public IPv4 address, a restarted instance receives a new public IPv4 address unless it has an Elastic IP address.
To benefit from the automatic recovery mechanisms, they must be configured in advance on an instance before a system status check fails. By default, simplified automatic recovery is enabled during instance launch. You can optionally configure Amazon CloudWatch action based recovery after launch. Having one of these mechanisms configured makes your instance more resilient.

Simplified automatic recovery and Amazon CloudWatch action based recovery are only available on supported instances. For more information, see Requirements for enabling simplified automatic recovery and Requirements for enabling CloudWatch action based recovery.
Warning When AWS recovers your instance due to an underlying hardware or software issue, be aware of the following consequences: data stored in volatile memory (RAM) will be lost and the operating system's uptime will start over from zero. Furthermore, with CloudWatch action based recovery, data on instance store volumes will also be lost. To help protect against data loss, we recommend that you regularly create backups of valuable data. For more information about backup and recovery best practices for EC2 instances, see Best practices for Amazon EC2.
Automatic instance recovery mechanisms are designed for individual instances. For guidance on building a resilient system, see Build a resilient system.
Topics
- Key concepts of automatic instance recovery
- Differences between simplified automatic recovery and CloudWatch action based recovery
- Build a resilient system
- Verify if automatic instance recovery occurred
- Configure simplified automatic recovery on an Amazon EC2 instance
- Configure CloudWatch action based recovery on an EC2 instance
## Key concepts of automatic instance recovery Automatic instance recovery is an Amazon EC2 feature that automatically restores instance availability when underlying hardware or software failures occur, enhancing the resilience and reliability of your EC2 instances.
The following are key concepts of automatic instance recovery:
Configuration options Two mechanisms can be configured to support automatic instance recovery:

- Simplified automatic recovery: Enabled by default on supported instances.
- CloudWatch action based recovery: Requires manual configuration on supported instances.
System status checks System status checks automatically monitor the AWS infrastructure on which your EC2 instance runs.
- If a system status check fails, AWS initiates automatic instance recovery, which attempts to migrate the affected instance to different hardware.
- A failed system status check indicates a problem with the host's hardware or software, and not a problem with the instance itself. Automatic instance recovery can recover an instance that fails a system status check. However, automatic instance recovery does not operate if only the instance status check fails.
- For the differences between instance and system status checks, see Types of status checks.
Examples of underlying hardware or software problems Hardware or software issues that can cause a system status check to fail include loss of network connectivity, loss of system power, software issues on the physical host, and hardware issues on the physical host that impact network reachability.
Characteristics of recovered instances A recovered instance is identical to the original instance, except for the elements that are lost.
Preserved elements:
- Instance ID
- Public, private, and Elastic IP addresses
- Instance metadata
- Placement group
- Attached EBS volumes
- Availability Zone Lost elements:
- Data stored in volatile memory (RAM)
- Data stored on instance store volumes (applicable to CloudWatch action based recovery only)
- Operating system uptime resets to zero

Monitoring system status checks with CloudWatch The StatusCheckFailed_System metric in CloudWatch indicates whether a system status check passed or failed.
Metric values:
- 0 – The system status check passed.
- 1 – The system status check failed.
Events in Health Dashboard During automatic instance recovery attempts, AWS sends events to your Health Dashboard based on the configured recovery mechanism and its outcome:
- Simplified automatic recovery
- Success event: AWS_EC2_SIMPLIFIED_AUTO_RECOVERY_SUCCESS
- Failure event: AWS_EC2_SIMPLIFIED_AUTO_RECOVERY_FAILURE
- CloudWatch action based recovery
- Success event: AWS_EC2_INSTANCE_AUTO_RECOVERY_SUCCESS
- Failure event: AWS_EC2_INSTANCE_AUTO_RECOVERY_FAILURE
## Differences between simplified automatic recovery and CloudWatch action based recovery action based recovery The following table compares the key differences between simplified automatic recovery and CloudWatch action based recovery.
Comparison point Simplified automatic recovery CloudWatch action based recovery Configuration Enabled by default on supported instances Requires manual configura tion of CloudWatch alarms and actions Flexibility Fixed recovery behavior managed by AWS Customizable actions and conditions

Comparison point Simplified automatic recovery CloudWatch action based recovery Notification Basic notifications through Health Dashboard Customizable notifications through SNS Metal instance size Excluded Included Instance store volumes attached at launch Not supported for instances that attach instance store volumes at launch Supported on selected instance types. Note that data on instance store volumes is lost during instance recovery.
Recovery time Standard recovery attempt Faster recovery attempts than simplified automatic recovery Host problem resolves during migration Migration might be canceled and the instance stays on the original host Migration continues to a new host Cost No additional cost Might incur CloudWatch charges
## Build a resilient system While simplified automatic recovery and CloudWatch action based recovery are effective for maintaining individual instance availability, AWS recommends implementing a high-availability architecture that allows failover of traffic to healthy instances.
To achieve this, consider using AWS services such as Elastic Load Balancing (which distributes incoming traffic across multiple EC2 instances) and Amazon EC2 Auto Scaling (which automatically adjusts the number of instances based on demand and health).
For more information about building a resilient, fault-tolerant system with EC2 instances, see the following resources:
- Back to Basics: Designing for Failure with EC2 on the AWS YouTube channel

- Disaster Recovery (DR) Architecture on AWS, Part I: Strategies for Recovery in the Cloud on the AWS Architecture Blog site
- Application Load Balancers User Guide
- Amazon EC2 Auto Scaling User Guide
- REL11-BP02 Fail over to healthy resources in the Reliability Pillar AWS Well-Architected Framework
## Verify if automatic instance recovery occurred If your instance appears to have been offline and then unexpectedly rebooted, it might have undergone automatic instance recovery in response to an underlying hardware or software issue.
You can verify this by checking for automatic instance recovery events in your Health Dashboard.
You can also check whether an underlying hardware or software issue was detected for your instance by checking the StatusCheckFailed_System Amazon CloudWatch metric.
### Check for events in Health Dashboard When an automatic instance recovery attempt occurs, AWS sends events to your Health Dashboard.
The specific event depends on the configured recovery mechanism and whether the attempt succeeded or failed.
To check for automatic instance recovery events in the Health Dashboard
1. Open the Health Dashboard at https://phd.aws.amazon.com/phd/home#/.
2. Look for the events associated with automatic instance recovery. The presence of these events can confirm whether an attempt at automatic instance recovery occurred and its outcome.
- Simplified automatic recovery
- Success event: AWS_EC2_SIMPLIFIED_AUTO_RECOVERY_SUCCESS
- Failure event: AWS_EC2_SIMPLIFIED_AUTO_RECOVERY_FAILURE
- CloudWatch action based recovery
- Success event: AWS_EC2_INSTANCE_AUTO_RECOVERY_SUCCESS
- Failure event: AWS_EC2_INSTANCE_AUTO_RECOVERY_FAILURE

### Monitor system status checks with CloudWatch You can verify if an underlying hardware or software issue was detected for your instance by checking the StatusCheckFailed_System metric in CloudWatch. The metric value indicates whether a system status check passed (no hardware or software issue) or failed (hardware or software issue).
To verify if an underlying hardware or software issue was detected
1. Open the CloudWatch console Metrics page at https://console.aws.amazon.com/cloudwatch/ home?#metricsV2.
2. Verify that you're in the same Region as your EC2 instance.
3. Paste the following metric in the Metrics search field, and press Enter.
StatusCheckFailed_System
4. Choose EC2 > Per-Instance Metrics.
5. In the table, select the check box next to the instance that you want to check.
6. Change the query period to the time that you suspect the recovery event occurred.
7. Choose the Graphed metrics tab, and for StatusCheckFailed_System, do the following: a.
For Statistic, choose either Average, Maximum, or Minimum. b.
For Period, choose 1 minute.
8. Check the value for StatusCheckFailed_System.
- Value of 0: The system status check passed, indicating no underlying hardware or software issue.
- Value of 1: The system status check failed, indicating an underlying hardware or software issue.
For more information, see Automatic instance recovery.

## Configure simplified automatic recovery on an Amazon EC2 instance Important This section describes how to proactively configure recovery mechanisms on an EC2 instance. These recovery mechanisms are designed to restore instance availability when AWS detects an underlying hardware or software issue that causes a system status check to fail. If you are currently experiencing problems accessing your instance, see Troubleshoot EC2 instances.
If AWS detects that an instance is unavailable due to an underlying hardware or software issue, simplified automatic recovery can automatically restore instance availability by moving the instance from the host with the underlying issue to a different host.
If simplified automatic recovery occurs, AWS sends one of the following events to your AWS Health Dashboard, depending on the outcome:
- Success event: AWS_EC2_SIMPLIFIED_AUTO_RECOVERY_SUCCESS
- Failure event: AWS_EC2_SIMPLIFIED_AUTO_RECOVERY_FAILURE To be notified of these events, you can configure notifications. For more information, see Creating your first notification configuration in AWS User Notifications in the AWS User Notifications User Guide. You can also use Amazon EventBridge rules to monitor simplified automatic recovery events.
Simplified automatic recovery is enabled by default on all supported instances during instance launch. However, it can only operate if an instance is in the running state, there are no service events listed in the AWS Health Dashboard, and there is available capacity for the instance type. In some situations, such as significant outages, capacity constraints might cause recovery attempts to fail. For more information, see the section called "Troubleshoot simplified automatic recovery failures".
You can disable simplified automatic recovery during or after launch, and re-enable it later if required.

Warning When AWS recovers your instance due to an underlying hardware or software issue, be aware of the following consequences: data stored in volatile memory (RAM) will be lost and the operating system's uptime will start over from zero. To help protect against data loss, we recommend that you regularly create backups of valuable data. For more information about backup and recovery best practices for EC2 instances, see Best practices for Amazon EC2.
Automatic instance recovery mechanisms are designed for individual instances. For guidance on building a resilient system, see Build a resilient system.
Contents
- Requirements for enabling simplified automatic recovery
- Configure simplified automatic recovery
- Troubleshoot simplified automatic recovery failures
### Requirements for enabling simplified automatic recovery Simplified automatic recovery can be enabled on instances that meet the following criteria:
Instance types
- General purpose: A1, M3, M4, M5, M5a, M5n, M5zn, M6a, M6g, M6i, M6in, M7a, M7g, M7i, M7i-flex, M8a, M8azn, M8g, M8gb, M8gn, M8i, M8i-flex, T1, T2, T3, T3a, T4g
- Compute optimized: C3, C4, C5, C5a, C5n, C6a, C6g, C6gn, C6i, C6in, C7a, C7g, C7gn, C7i, C7i-flex, C8a, C8g, C8gb, C8gn, C8i, C8i-flex
- Memory optimized: R3, R4, R5, R5a, R5b, R5n, R6a, R6g, R6i, R6in, R7a, R7g, R7i, R7iz, R8a, R8g, R8gb, R8gn, R8i, R8i-flex, U-3tb1, U-6tb1, U-9tb1, U-12tb1, U-18tb1, U-24tb1, U7i-6tb, U7i-8tb, U7i-12tb, U7in-16tb, U7in-24tb, U7in-32tb, U7inh-32tb, X1, X1e, X2iezn, X8g, X8i
- Accelerated computing: G3, G5g, Inf1, P3, VT1
- High-performance computing: Hpc6a, Hpc7a, Hpc7g, Hpc8a Tenancy
- Shared
- Dedicated Instance

For more information, see Amazon EC2 Dedicated Instances.
Limitations Simplified automatic recovery is not supported for instances with the following characteristics:
- Instance size: metal instances
- Tenancy: Dedicated Host. For Dedicated Hosts, use Dedicated Host Auto Recovery instead.
- Storage: Instances with instance store volumes
- Networking: Instances using an Elastic Fabric Adapter
- Auto Scaling: Instances that are part of an Auto Scaling group
- Maintenance: Instances currently undergoing a scheduled maintenance event
### Configure simplified automatic recovery Simplified automatic recovery is enabled by default when you launch a supported instance. You can set the automatic recovery behavior to disabled during or after launching the instance.
The default configuration doesn't enable simplified automatic recovery for an unsupported instance.
Console To disable simplified automatic recovery at launch
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Instances, and then choose Launch instance.
3. In the Advanced details section, for Instance auto-recovery, choose Disabled.
4. Configure the remaining instance launch settings as needed and then launch the instance.
To disable simplified automatic recovery after launch
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Instances.
3. Select the instance, and then choose Actions, Instance settings, Change auto-recovery behavior.

4. Choose Off, and then choose Save.
To enable simplified automatic recovery after launch
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Instances.
3. Select the instance, and then choose Actions, Instance settings, Change auto-recovery behavior.
4. Choose Default (On), and then choose Save.
AWS CLI To disable simplified automatic recovery at launch Use the run-instances command with the --maintenance-options option.
--maintenance-options AutoRecovery=Disabled To disable simplified automatic recovery after launch Use the modify-instance-maintenance-options command. aws ec2 modify-instance-maintenance-options \ --instance-id i-1234567890abcdef0 \ --auto-recovery disabled To enable simplified automatic recovery after launch Use the modify-instance-maintenance-options command. aws ec2 modify-instance-maintenance-options \ --instance-id i-1234567890abcdef0 \ --auto-recovery default PowerShell To disable simplified automatic recovery at launch Use the New-EC2Instance cmdlet.

-MaintenanceOptions_AutoRecovery Disabled To disable simplified automatic recovery after launch Use the Edit-EC2InstanceMaintenanceOption cmdlet.
Edit-EC2InstanceMaintenanceOption `
    -InstanceId i-1234567890abcdef0 `
    -AutoRecovery Disabled To enable simplified automatic recovery after launch Use the Edit-EC2InstanceMaintenanceOption cmdlet.
Edit-EC2InstanceMaintenanceOption `
    -InstanceId i-1234567890abcdef0 `
    -AutoRecovery Enabled
### Troubleshoot simplified automatic recovery failures If simplified automatic recovery fails to recover your instance, consider the following issues:
- AWS service events are running Simplified automatic recovery does not operate during service events in the AWS Health Dashboard. You might not receive recovery failure notifications for such events. For the latest service availability information, see the Service health status page.
- Insufficient capacity There is temporarily insufficient replacement hardware to migrate the instance.
- Maximum daily recovery attempts reached The instance has reached the maximum daily allowance for recovery attempts. Your instance might subsequently be retired if automatic recovery fails and a hardware degradation is determined to be the root cause of the original failed system status check.
If the instance's system status check failure persists despite multiple recovery attempts, see Troubleshoot instances with failed status checks for additional guidance.

## Configure CloudWatch action based recovery on an EC2 instance Important This section describes how to proactively configure recovery mechanisms on an EC2 instance. These recovery mechanisms are designed to restore instance availability when AWS detects an underlying hardware or software issue that causes a system status check to fail. If you are currently experiencing problems accessing your instance, see Troubleshoot EC2 instances.
If AWS detects that an instance is unavailable due to an underlying hardware or software issue, CloudWatch action based recovery can automatically restore instance availability by moving the instance from the host with the underlying issue to a different host.
If CloudWatch action based recovery occurs, AWS sends one of the following events to your AWS Health Dashboard, depending on the outcome:
- Success event: AWS_EC2_INSTANCE_AUTO_RECOVERY_SUCCESS
- Failure event: AWS_EC2_INSTANCE_AUTO_RECOVERY_FAILURE You can configure CloudWatch action based recovery to add recovery actions to Amazon CloudWatch alarms. CloudWatch action based recovery works with the StatusCheckFailed_System metric. CloudWatch action based recovery provides to-the- minute recovery response time granularity and Amazon Simple Notification Service (Amazon SNS) notifications of recovery actions and outcomes. These configuration options allow for faster recovery attempts with more granular control over the system status check failure event response compared to simplified automatic recovery. For more information about available CloudWatch options, see Status checks for your instances.
However, CloudWatch action based recovery can only operate if an instance is in the running state, there are no service events listed in the AWS Health Dashboard, and there is available capacity for the instance type. In some situations, such as significant outages, capacity constraints might cause recovery attempts to fail. For more information, see the section called "Troubleshoot".

Warning When AWS recovers your instance due to an underlying hardware or software issue, be aware of the following consequences: data stored in volatile memory (RAM) and on instance store volumes will be lost, and the operating system's uptime will start over from zero. To help protect against data loss, we recommend that you regularly create backups of valuable data. For more information about backup and recovery best practices for EC2 instances, see Best practices for Amazon EC2.
Automatic instance recovery mechanisms are designed for individual instances. For guidance on building a resilient system, see Build a resilient system.
Contents
- Requirements for enabling CloudWatch action based recovery
- Configure CloudWatch action based recovery
- Troubleshoot CloudWatch action based recovery failures
### Requirements for enabling CloudWatch action based recovery CloudWatch action based recovery can be enabled on instances that meet the following criteria:
Instance types
- General purpose: A1, M3, M4, M5, M5a, M5n, M5zn, M6a, M6g, M6i, M6in, M7a, M7g, M7i, M7i-flex, M8a, M8azn, M8g, M8gb, M8gn, M8i, M8i-flex, T1, T2, T3, T3a, T4g
- Compute optimized: C3, C4, C5, C5a, C5n, C6a, C6g, C6gn, C6i, C6in, C7a, C7g, C7gn, C7i, C7i-flex, C8a, C8g, C8gb, C8gn, C8i, C8i-flex
- Memory optimized: R3, R4, R5, R5a, R5b, R5n, R6a, R6g, R6i, R6in, R7a, R7g, R7i, R7iz, R8a, R8g, R8gb, R8gn, R8i, R8i-flex, U-3tb1, U-6tb1, U-9tb1, U-12tb1, U-18tb1, U-24tb1, U7i-6tb, U7i-8tb, U7i-12tb, U7in-16tb, U7in-24tb, U7in-32tb, U7inh-32tb, X1, X1e, X2idn, X2iedn, X2iezn, X8g, X8i
- Accelerated computing: G3, G5g, Inf1, P3, VT1
- High-performance computing: Hpc6a, Hpc7a, Hpc7g, Hpc8a
- Metal instances: Any of the above instance types with the metal instance size.
- If instance store volumes are added at launch: Then only the following instance types are supported: M3, C3, R3, X1, X1e, X2idn, X2iedn

Tenancy
- Shared
- Dedicated Instance For more information, see Amazon EC2 Dedicated Instances.
Limitations CloudWatch action based recovery is not supported for instances with the following characteristics:
- Tenancy: Dedicated Host. For Dedicated Hosts, use Dedicated Host Auto Recovery instead.
- Networking: Instances using an Elastic Fabric Adapter
- Auto Scaling: Instances that are part of an Auto Scaling group
- Maintenance: Instances currently undergoing a scheduled maintenance event
#### Find a supported instance type You can view the instance types that support CloudWatch action based recovery.
Console To view the instance types that support CloudWatch action based recovery
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the left navigation pane, choose Instance Types.
3. In the filter bar, add the filter Auto Recovery support = true. The Instance types table displays all the instance types that support CloudWatch action based recovery.
4. (Optional) Add filters to further scope to specific instance types of interest.
AWS CLI To view the instance types that support CloudWatch action based recovery Use the describe-instance-types command with the auto-recovery-supported filter. aws ec2 describe-instance-types \ --filters Name=auto-recovery-supported,Values=true \ --query "InstanceTypes[*].[InstanceType]" \

    --output text | sort PowerShell To view the instance types that support CloudWatch action based recovery Use the Get-EC2InstanceType cmdlet with the auto-recovery-supported filter.
Get-EC2InstanceType `
    -Filter @{Name="auto-recovery-supported";Values="true"} | `
    Select InstanceType | Sort-Object InstanceType
### Configure CloudWatch action based recovery To configure CloudWatch action based recovery for an EC2 instance, create a CloudWatch alarm that monitors the StatusCheckFailed_System metric for the specified instance. Set the alarm to trigger when the metric value is 1, indicating a failed system status check. Configure the alarm action to automatically recover the instance when triggered.
You can configure the alarm using either the Amazon EC2 console or the CloudWatch console.
For the instructions, see Add recover actions to Amazon CloudWatch alarms in this user guide, or Adding recover actions to Amazon CloudWatch alarms in the Amazon CloudWatch User Guide.
### Troubleshoot CloudWatch action based recovery failures If CloudWatch action based recovery fails to recover your instance, consider the following issues:
- AWS service events are running CloudWatch action based recovery does not operate during service events in the AWS Health Dashboard. You might not receive recovery failure notifications for such events. For the latest service availability information, see the Service health status page.
- Insufficient capacity There is temporarily insufficient replacement hardware to migrate the instance.
- Maximum daily recovery attempts reached The instance has reached the maximum daily allowance for recovery attempts. Your instance might subsequently be retired if automatic recovery fails and a hardware degradation is determined to be the root cause of the original failed system status check.
