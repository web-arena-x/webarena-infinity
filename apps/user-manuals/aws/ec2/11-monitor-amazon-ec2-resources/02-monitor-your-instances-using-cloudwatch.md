# Monitor your instances using CloudWatch

Source: apps/user-manuals/aws/ec2-ug.pdf

---

    -InstanceEventWindowId iew-0abcdef1234567890 To force-delete an event window Use the Remove-EC2InstanceEventWindow cmdlet.
Remove-EC2InstanceEventWindow `
    -InstanceEventWindowId iew-0abcdef1234567890 `
    -ForceDelete $true
# Monitor your instances using CloudWatch You can monitor your instances using Amazon CloudWatch, which collects and processes raw data from Amazon EC2 into readable, near real-time metrics. These statistics are recorded for a period of 15 months, so that you can access historical information and gain a better perspective on how your web application or service is performing.
By default, Amazon EC2 sends metric data to CloudWatch in 5-minute periods. To send metric data for your instance to CloudWatch in 1-minute periods, you can enable detailed monitoring on the instance. For more information, see Manage detailed monitoring for your EC2 instances.
The Amazon EC2 console displays a series of graphs based on the raw data from Amazon CloudWatch. Depending on your needs, you might prefer to get data for your instances from Amazon CloudWatch instead of the graphs in the console.
For Amazon CloudWatch billing and cost information, see  CloudWatch billing and cost in the Amazon CloudWatch User Guide.
Contents
- Manage CloudWatch alarms for your EC2 instances in the Amazon EC2 console
- Manage detailed monitoring for your EC2 instances
- CloudWatch metrics that are available for your instances
- Install and configure the CloudWatch agent using the Amazon EC2 console to add additional metrics
- Statistics for CloudWatch metrics for your instances
- View the monitoring graphs for your instances
- Create a CloudWatch alarm for an instance

- Create alarms that stop, terminate, reboot, or recover an instance
## Manage CloudWatch alarms for your EC2 instances in the Amazon EC2 console console From the Instances screen in the Amazon EC2 console, you can manage the Amazon CloudWatch alarms for your instances. In the Instances table, the Alarm status column provides two console controls: a control for viewing alarms, and another for creating or editing them. The following screenshot indicates these console controls, numbered 1 (View alarms) and 2 (a + sign for creating or editing an alarm).
### View alarms from the Instances screen You can view each instance's alarms from the Instances screen.
To view an instance's alarm from the Instances screen
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Instances.
3. In the Instances table, for your chosen instance, choose View alarms (numbered 1 in the preceding screenshot).
4. In the Alarm details for i-1234567890abcdef0 window, choose the alarm name to view the alarm in the CloudWatch console.
### Create alarms from the Instances screen You can create an alarm for each instance from the Instances screen.
To create an alarm for an instance from the Instances screen
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.

2. In the navigation pane, choose Instances.
3. In the Instances table, for your chosen instance, choose the plus sign (numbered 2 in the preceding screenshot).
4. In the Manage CloudWatch alarms screen, create your alarm. For more information, see Create a CloudWatch alarm for an instance.
### Edit alarms from the Instances screen You can edit the alarm for an instance from the Instances screen.
To edit an alarm for an instance from the Instances screen
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Instances.
3. In the Instances table, for your chosen instance, choose the plus sign (numbered 2 in the preceding screenshot).
4. In the Manage CloudWatch alarms screen, edit your alarm. For more information, see Edit or delete a CloudWatch alarm in the Amazon CloudWatch User Guide.
## Manage detailed monitoring for your EC2 instances Amazon CloudWatch provides two categories of monitoring: basic monitoring and detailed monitoring. By default, your instance is configured for basic monitoring. You can optionally enable detailed monitoring to help you more quickly identify and act on operational issues. You can enable or turn off detailed monitoring at launch or when the instance is running or stopped.
Enabling detailed monitoring on an instance does not affect the monitoring of its attached EBS volumes. For more information, see Amazon CloudWatch metrics for Amazon EBS.
The following table highlights the differences between basic monitoring and detailed monitoring for your instances.
Monitoring type Description Charges Basic monitorin g Status check metrics are available in 1-minute periods. All other metrics are available in 5-minute periods.
No charge.

Monitoring type Description Charges Detailed monitoring You can get metrics in 1-minute periods, provided you enable detailed monitoring for the instance.
Once you've enabled detailed monitoring, you can aggregate the data across groups of similar instances.
You are charged per metric that Amazon EC2 sends to CloudWatc h. You are not charged for data storage. For more information, see Paid tier on the Amazon CloudWatc h pricing page.
Contents
- Required permissions
- Enable detailed monitoring at launch
- Manage detailed monitoring
### Required permissions To enable detailed monitoring for an instance, your user must have permission to use the MonitorInstances API action. To turn off detailed monitoring for an instance, your user must have permission to use the UnmonitorInstances API action.
### Enable detailed monitoring at launch Use the following procedures to enable detailed monitoring at launch. By default, your instance uses basic monitoring.
Console To enable detailed monitoring when launching an instance When launching an instance using the Amazon EC2 console, under Advanced details, select the Detailed CloudWatch monitoring checkbox.
AWS CLI To enable detailed monitoring when launching an instance Use the run-instances command with the --monitoring option.

--monitoring Enabled=true PowerShell To enable detailed monitoring when launching an instance Use the New-EC2Instance cmdlet with the -Monitoring parameter.
-Monitoring $true
### Manage detailed monitoring Use the following procedures to manage detailed monitoring for a running or stopped instance.
Console To manage detailed monitoring
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Instances.
3. Select the instance.
4. Choose Actions, Monitor and troubleshoot, Manage detailed monitoring.
5. On the Detailed monitoring page, for Detailed monitoring, do one of the following:
- Detailed monitoring – Select Enable.
- Basic monitoring – Clear Enable.
6. Choose Confirm.
AWS CLI To enable detailed monitoring Use the following monitor-instances command. aws ec2 monitor-instances --instance-ids i-1234567890abcdef0 To disable detailed monitoring Use the unmonitor-instances command.

aws ec2 unmonitor-instances --instance-ids i-1234567890abcdef0 PowerShell To enable detailed monitoring Use the Start-EC2InstanceMonitoring cmdlet.
Start-EC2InstanceMonitoring -InstanceId i-1234567890abcdef0 To disable detailed monitoring Use the Stop-EC2InstanceMonitoring cmdlet.
Stop-EC2InstanceMonitoring -InstanceId i-1234567890abcdef0
## CloudWatch metrics that are available for your instances Amazon EC2 sends metrics to Amazon CloudWatch. You can use the AWS Management Console, the AWS CLI, or an API to list the metrics that Amazon EC2 sends to CloudWatch. By default, each data point covers the 5 minutes that follow the start time of activity for the instance. If you've enabled detailed monitoring, each data point covers the next minute of activity from the start time. Note that for the Minimum, Maximum, and Average statistics, the minimum granularity for the metrics that EC2 provides is 1 minute.
For information about how to view the available metrics using the AWS Management Console or the AWS CLI, see View available metrics in the Amazon CloudWatch User Guide.
For information about getting the statistics for these metrics, see Statistics for CloudWatch metrics for your instances.
Contents
- Instance metrics
- Accelerator metrics
- CPU credit metrics
- Dedicated Host metrics
- Amazon EBS metrics for Nitro-based instances

- Status check metrics
- Traffic mirroring metrics
- Auto Scaling group metrics
- Amazon EC2 metric dimensions
- Amazon EC2 usage metrics
### Instance metrics The AWS/EC2 namespace includes the following instance metrics.
Metric Description Unit Meaningful statistics CPUUtiliz ation The percentage of physical CPU time that Amazon EC2 uses to run the EC2 instance, which includes time spent to run both the user code and the Amazon EC2 code.
At a very high level, CPUUtilization  is the sum of guest CPUUtilization  and hypervisor CPUUtilization .
Tools in your operating system can show a different percentage than CloudWatch due to factors such as legacy device simulation, configuration of non-legacy devices, interrupt -heavy workloads, live migration, and live update.
Percent
- Average
- Minimum
- Maximum DiskReadO ps Completed read operations from all instance store volumes available to the instance in a specified period of time.
To calculate the average I/O operations per second (IOPS) for the period, divide the total operations in the period by the number of seconds in that period.
Count
- Sum
- Average
- Minimum
- Maximum

Metric Description Unit Meaningful statistics If there are no instance store volumes, either the value is 0 or the metric is not reported.
DiskWrite Ops Completed write operations to all instance store volumes available to the instance in a specified period of time.
To calculate the average I/O operations per second (IOPS) for the period, divide the total operations in the period by the number of seconds in that period.
If there are no instance store volumes, either the value is 0 or the metric is not reported.
Count
- Sum
- Average
- Minimum
- Maximum

Metric Description Unit Meaningful statistics DiskReadB ytes Bytes read from all instance store volumes available to the instance.
This metric is used to determine the volume of the data the application reads from the hard disk of the instance. This can be used to determine the speed of the application.
The number reported is the number of bytes received during the period. If you are using basic (5-minute) monitoring, you can divide this number by 300 to find Bytes/ second. If you have detailed (1-minute) monitoring, divide it by 60. You can also use the CloudWatch metric math function DIFF_TIME  to find the bytes per second.
For example, if you have graphed DiskReadB ytes  in CloudWatch as m1, the metric math formula m1/(DIFF_TIME(m1)) returns the metric in bytes/second. For more informati on about DIFF_TIME  and other metric math functions, see Use metric math in the Amazon CloudWatch User Guide.
If there are no instance store volumes, either the value is 0 or the metric is not reported.
Bytes
- Sum
- Average
- Minimum
- Maximum

Metric Description Unit Meaningful statistics DiskWrite Bytes Bytes written to all instance store volumes available to the instance.
This metric is used to determine the volume of the data the application writes onto the hard disk of the instance. This can be used to determine the speed of the application.
The number reported is the number of bytes received during the period. If you are using basic (5-minute) monitoring, you can divide this number by 300 to find Bytes/ second. If you have detailed (1-minute) monitoring, divide it by 60. You can also use the CloudWatch metric math function DIFF_TIME  to find the bytes per second.
For example, if you have graphed DiskWrite Bytes  in CloudWatch as m1, the metric math formula m1/(DIFF_TIME(m1)) returns the metric in bytes/second. For more informati on about DIFF_TIME  and other metric math functions, see Use metric math in the Amazon CloudWatch User Guide.
If there are no instance store volumes, either the value is 0 or the metric is not reported.
Bytes
- Sum
- Average
- Minimum
- Maximum

Metric Description Unit Meaningful statistics MetadataN oToken The number of times the Instance Metadata Service (IMDS) was successfully accessed using a method that does not use a token.
This metric is used to determine if there are any processes accessing instance metadata that are using Instance Metadata Service Version 1 (IMDSv1), which does not use a token. If all requests use token-backed sessions, i.e., Instance Metadata Service Version 2 (IMDSv2), the value is 0. For more information, see Transition to using  Instance Metadata Service Version 2.
Nitro instances:
None Xen instances : Count
- Sum
- Percentiles MetadataN oTokenRej ected The number of times an IMDSv1 call was attempted after IMDSv1 was disabled.
If this metric appears, it indicates that an IMDSv1 call was attempted and rejected. You can either re-enable IMDSv1 or make sure all of your calls use IMDSv2. For more informati on, see Transition to using  Instance Metadata Service Version 2.
Nitro instances:
None Xen instances : Count
- Sum
- Percentiles

Metric Description Unit Meaningful statistics NetworkIn The number of bytes received by the instance on all network interfaces. This metric identifie s the volume of incoming network traffic to a single instance.
The number reported is the number of bytes received during the period. If you are using basic (5-minute) monitoring and the statistic is Sum, you can divide this number by 300 to find Bytes/second. If you have detailed (1- minute) monitoring and the statistic is Sum, divide it by 60.
Bytes
- Sum
- Average
- Minimum
- Maximum NetworkOu t The number of bytes sent out by the instance on all network interfaces. This metric identifie s the volume of outgoing network traffic from a single instance.
The number reported is the number of bytes sent during the period. If you are using basic (5-minute) monitoring and the statistic is Sum, you can divide this number by 300 to find Bytes/second. If you have detailed (1-minute ) monitoring and the statistic is Sum, divide it by 60.
Bytes
- Sum
- Average
- Minimum
- Maximum

Metric Description Unit Meaningful statistics NetworkPa cketsIn The number of packets received by the instance on all network interfaces. This metric identifies the volume of incoming traffic in terms of the number of packets on a single instance.
This metric is available for basic monitorin g only (5-minute periods). To calculate the number of packets per second (PPS) your instance received for the 5 minutes, divide the Sum statistic value by 300.
Count
- Sum
- Average
- Minimum
- Maximum NetworkPa cketsOut The number of packets sent out by the instance on all network interfaces. This metric identifies the volume of outgoing traffic in terms of the number of packets on a single instance.
This metric is available for basic monitorin g only (5-minute periods). To calculate the number of packets per second (PPS) your instance sent for the 5 minutes, divide the Sum statistic value by 300.
Count
- Sum
- Average
- Minimum
- Maximum
### Accelerator metrics The AWS/EC2 namespace includes the following accelerator metric for your accelerated computing instances. Only supported on a subset of accelerated computing instance types.

Metric Description Unit Meaningful statistics GPUPowerU tilizatio n Active power usage as a percentage of maximum active power.
Percent
- Average
- Minimum
- Maximum
### CPU credit metrics The AWS/EC2 namespace includes the following CPU credit metrics for your burstable performance instances.
Metric Description Unit Meaningful statistics CPUCredit Usage The number of CPU credits spent by the instance for CPU utilization. One CPU credit equals one vCPU running at 100% utilization for one minute or an equivalent combination of vCPUs, utilization, and time (for example, one vCPU running at 50% utilization for two minutes or two vCPUs running at 25% utilizati on for two minutes).
CPU credit metrics are available at a 5-minute frequency only. If you specify a period greater than five minutes, use the Sum statistic instead of the Average statistic.
Credits (vCPU-min utes)
- Sum
- Average
- Minimum
- Maximum CPUCredit Balance The number of earned CPU credits that an instance has accrued since it was launched or started. For T2 Standard, the CPUCredit Balance  also includes the number of launch credits that have been accrued.
Credits (vCPU-min utes)
- Sum
- Average
- Minimum
- Maximum

Metric Description Unit Meaningful statistics Credits are accrued in the credit balance after they are earned, and removed from the credit balance when they are spent. The credit balance has a maximum limit, determined by the instance size. After the limit is reached, any new credits that are earned are discarded . For T2 Standard, launch credits do not count towards the limit.
The credits in the CPUCreditBalance  are available for the instance to spend to burst beyond its baseline CPU utilization.
When an instance is running, credits in the CPUCreditBalance  do not expire. When a T3 or T3a instance stops, the CPUCredit Balance  value persists for seven days.
Thereafter, all accrued credits are lost. When a T2 instance stops, the CPUCreditBalance value does not persist, and all accrued credits are lost.
CPU credit metrics are available at a 5-minute frequency only.

Metric Description Unit Meaningful statistics CPUSurplu sCreditBa lance The number of surplus credits that have been spent by an unlimited  instance when its CPUCreditBalance  value is zero.
The CPUSurplusCreditBalance value is paid down by earned CPU credits. If the number of surplus credits exceeds the maximum number of credits that the instance can earn in a 24-hour period, the spent surplus credits above the maximum incur an additiona l charge.
CPU credit metrics are available at a 5-minute frequency only.
Credits (vCPU-min utes)
- Sum
- Average
- Minimum
- Maximum CPUSurplu sCreditsC harged The number of spent surplus credits that are not paid down by earned CPU credits, and which thus incur an additional charge.
Spent surplus credits are charged when any of the following occurs:
- The spent surplus credits exceed the maximum number of credits that the instance can earn in a 24-hour period. Spent surplus credits above the maximum are charged at the end of the hour.
- The instance is stopped or terminated.
- The instance is switched from unlimited to standard.
CPU credit metrics are available at a 5-minute frequency only.
Credits (vCPU-min utes)
- Sum
- Average
- Minimum
- Maximum

### Dedicated Host metrics The AWS/EC2 namespace includes the following metrics for T3 Dedicated Hosts.
Metric Description Unit Meaningful statistics Dedicated HostCPUUt ilization The percentage of allocated compute capacity that is currently in use by the instances running on the Dedicated Host.
Percent
- Sum
- Average
- Minimum
- Maximum
### Amazon EBS metrics for Nitro-based instances The AWS/EC2 namespace includes additional Amazon EBS metrics for volumes that are attached to Nitro-based instances that are not bare metal instances.
Metric Description Unit Meaningful statistics InstanceE BSIOPSExc eededChec k Reports whether an application attempted to drive IOPS that exceeds the maximum EBS IOPS limits for the instance within the last minute. This metric can be either 0 (IOPS not exceeded) or 1 (IOPS exceeded).
None
- Sum
- Average
- Minimum
- Maximum InstanceE BSThrough putExceed edCheck Reports whether an application attempted to drive throughput that exceeds the maximum EBS throughput limits for the instance within the last minute. This metric can be either 0 (throughput not exceeded) or 1 (throughput exceeded).
None
- Sum
- Average
- Minimum
- Maximum EBSReadOp s Completed read operations from all Amazon EBS volumes attached to the instance in a specified period of time.
Count
- Sum
- Average
- Minimum

Metric Description Unit Meaningful statistics To calculate the average read I/O operations per second (Read IOPS) for the period, divide the total operations in the period by the number of seconds in that period. If you are using basic (5-minute) monitoring, you can divide this number by 300 to calculate the Read IOPS. If you have detailed (1-minute ) monitoring, divide it by 60. You can also use the CloudWatch metric math function DIFF_TIME  to find the operations per second. For example, if you have graphed EBSReadOps  in CloudWatch as m1, the metric math formula m1/(DIFF_TIME(m1)) returns the metric in operations/second. For more information about DIFF_TIME  and other metric math functions, see Use metric math in the Amazon CloudWatch User Guide.
- Maximum

Metric Description Unit Meaningful statistics EBSWriteO ps Completed write operations to all EBS volumes attached to the instance in a specified period of time.
To calculate the average write I/O operation s per second (Write IOPS) for the period, divide the total operations in the period by the number of seconds in that period. If you are using basic (5-minute) monitoring, you can divide this number by 300 to calculate the Write IOPS. If you have detailed (1-minute ) monitoring, divide it by 60. You can also use the CloudWatch metric math function DIFF_TIME  to find the operations per second. For example, if you have graphed EBSWriteOps  in CloudWatch as m1, the metric math formula m1/(DIFF_TIME(m1)) returns the metric in operations/second. For more information about DIFF_TIME  and other metric math functions, see Use metric math in the Amazon CloudWatch User Guide.
Count
- Sum
- Average
- Minimum
- Maximum

Metric Description Unit Meaningful statistics EBSReadBy tes Bytes read from all EBS volumes attached to the instance in a specified period of time.
The number reported is the number of bytes read during the period. If you are using basic (5-minute) monitoring, you can divide this number by 300 to find Read Bytes/ second. If you have detailed (1-minute) monitoring, divide it by 60. You can also use the CloudWatch metric math function DIFF_TIME  to find the bytes per second.
For example, if you have graphed EBSReadBy tes  in CloudWatch as m1, the metric math formula m1/(DIFF_TIME(m1)) returns the metric in bytes/second. For more informati on about DIFF_TIME  and other metric math functions, see Use metric math in the Amazon CloudWatch User Guide.
Bytes
- Sum
- Average
- Minimum
- Maximum

Metric Description Unit Meaningful statistics EBSWriteB ytes Bytes written to all EBS volumes attached to the instance in a specified period of time.
The number reported is the number of bytes written during the period. If you are using basic (5-minute) monitoring, you can divide this number by 300 to find Write Bytes/ second. If you have detailed (1-minute) monitoring, divide it by 60. You can also use the CloudWatch metric math function DIFF_TIME  to find the bytes per second.
For example, if you have graphed EBSWriteB ytes  in CloudWatch as m1, the metric math formula m1/(DIFF_TIME(m1)) returns the metric in bytes/second. For more informati on about DIFF_TIME  and other metric math functions, see Use metric math in the Amazon CloudWatch User Guide.
Bytes
- Sum
- Average
- Minimum
- Maximum EBSIOBala nce% Provides information about the percentage of I/O credits remaining in the burst bucket. This metric is available for basic monitoring only.
This metric is available only for some *.4xlarge  instance sizes and smaller that burst to their maximum performance for only 30 minutes at least once every 24 hours.
The Sum statistic is not applicable to this metric.
Percent
- Minimum
- Maximum

Metric Description Unit Meaningful statistics EBSByteBa lance% Provides information about the percentag e of throughput credits remaining in the burst bucket. This metric is available for basic monitoring only.
This metric is available only for some *.4xlarge  instance sizes and smaller that burst to their maximum performance for only 30 minutes at least once every 24 hours.
The Sum statistic is not applicable to this metric.
Percent
- Minimum
- Maximum For information about the metrics provided for your EBS volumes, see Metrics for Amazon EBS volumes in the Amazon EBS User Guide. For information about the metrics provided for your EC2 Fleets and Spot Fleets, see Monitor your EC2 Fleet or Spot Fleet using CloudWatch.
### Status check metrics By default, status check metrics are available at a 1-minute frequency at no charge. For a newly- launched instance, status check metric data is only available after the instance has completed the initialization state (within a few minutes of the instance entering the running state). For more information about EC2 status checks, see Status checks for Amazon EC2 instances.
The AWS/EC2 namespace includes the following status check metrics.
Metric Description Unit Meaningful statistics StatusChe ckFailed Reports whether the instance has passed all status checks in the last minute.
This metric can be either 0 (passed) or 1 (failed).
Count
- Average
- Minimum
- Maximum

Metric Description Unit Meaningful statistics By default, this metric is available at a 1- minute frequency at no charge.
StatusChe ckFailed_ Instance Reports whether the instance has passed the instance status check in the last minute.
This metric can be either 0 (passed) or 1 (failed).
By default, this metric is available at a 1- minute frequency at no charge.
Count
- Average
- Minimum
- Maximum StatusChe ckFailed_ System Reports whether the instance has passed the system status check in the last minute.
This metric can be either 0 (passed) or 1 (failed).
By default, this metric is available at a 1- minute frequency at no charge.
Count
- Average
- Minimum
- Maximum StatusChe ckFailed_ AttachedE BS Reports whether the instance has passed the attached EBS status check in the last minute.
This metric can be either 0 (passed) or 1 (failed).
By default, this metric is available at a 1- minute frequency at no charge.
Count
- Average
- Minimum
- Maximum The AWS/EBS namespace includes the following status check metric.

Metric Description Unit Meaningful statistics VolumeSta lledIOChe ck Note: For Nitro instances only. Not published for volumes attached to Amazon ECS and AWS Fargate tasks.
Reports whether a volume has passed or failed a stalled IO check in the last minute. This metric can be either 0 (passed) or 1 (failed).
None
- Average
- Minimum
- Maximum
### Traffic mirroring metrics The AWS/EC2 namespace includes metrics for mirrored traffic. For more information, see Monitor mirrored traffic using Amazon CloudWatch in the Amazon VPC Traffic Mirroring Guide.
### Auto Scaling group metrics The AWS/AutoScaling namespace includes metrics for Auto Scaling groups. For more information, see Monitor CloudWatch metrics for your Auto Scaling groups and instances in the Amazon EC2 Auto Scaling User Guide.
### Amazon EC2 metric dimensions You can use the following dimensions to refine the metrics listed in the previous tables.
Dimension Description AutoScalingGroupName This dimension filters the data you request for all instances in a specified capacity group. An Auto Scaling group is a collectio n of instances you define if you're using Auto Scaling. This dimension is available only for Amazon EC2 metrics when the instances are in such an Auto Scaling group. Available for instances with Detailed or Basic Monitoring enabled.
ImageId This dimension filters the data you request for all instances running this Amazon EC2 Amazon Machine Image (AMI).
Available for instances with Detailed Monitoring enabled.

Dimension Description InstanceId This dimension filters the data you request for the identified instance only. This helps you pinpoint an exact instance from which to monitor data.
InstanceType This dimension filters the data you request for all instances running with this specified instance type. This helps you categorize your data by the type of instance running. For example, you might compare data from an m1.small instance and an m1.large instance to determine which has the better business value for your application. Available for instances with Detailed Monitoring enabled.
### Amazon EC2 usage metrics You can use CloudWatch usage metrics to provide visibility into your account's usage of resources.
Use these metrics to visualize your current service usage on CloudWatch graphs and dashboards.
Amazon EC2 usage metrics correspond to AWS service quotas. You can configure alarms that alert you when your usage approaches a service quota. For more information about CloudWatch integration with service quotas, see AWS usage metrics in the Amazon CloudWatch User Guide.
Amazon EC2 publishes the following metrics in the AWS/Usage namespace.
Metric Description ResourceCount The number of the specified resources running in your account.
The resources are defined by the dimensions associated with the metric.
The most useful statistic for this metric is MAXIMUM, which represents the maximum number of resources used during the 1-minute period.
The following dimensions are used to refine the usage metrics that are published by Amazon EC2.

Dimension Description Service The name of the AWS service containing the resource. For Amazon EC2 usage metrics, the value for this dimension is EC2.
Type The type of entity that is being reported. Currently, the only valid value for Amazon EC2 usage metrics is Resource.
Resource The type of resource that is running. Currently, the only valid value for Amazon EC2 usage metrics is vCPU, which returns information on instances that are running.
Class The class of resource being tracked. For Amazon EC2 usage metrics with vCPU as the value of the Resource dimension, the valid values are Standard/OnDemand , F/OnDemand , G/ OnDemand , Inf/OnDemand , P/OnDemand , and X/OnDeman d .
The values for this dimension define the first letter of the instance types that are reported by the metric. For example, Standard/OnDemand  returns information about all running instances with types that start with A, C, D, H, I, M, R, T, and Z, and G/OnDemand  returns information about all running instances with types that start with G.
## Install and configure the CloudWatch agent using the Amazon EC2 console to add additional metrics console to add additional metrics Installing and configuring the CloudWatch agent using the Amazon EC2 console is in beta for Amazon EC2 and is subject to change.
By default, Amazon CloudWatch provides basic metrics, such as CPUUtilization and NetworkIn, for monitoring your Amazon EC2 instances. To collect additional metrics, you can install the CloudWatch agent on your EC2 instances, and then configure the agent to emit selected

metrics. Instead of manually installing and configuring the CloudWatch agent on every EC2 instance, you can use the Amazon EC2 console to do this for you.
You can use the Amazon EC2 console to install the CloudWatch agent on your instances and configure the agent to emit selected metrics.
Alternatively, to complete this process manually, see Installing the CloudWatch agent in the Amazon CloudWatch User Guide. For more information about the CloudWatch agent, see Collect metrics, logs, and traces using the CloudWatch agent.
Contents
- Prerequisites
- How it works
- Costs
- Install and configure the CloudWatch agent
### Prerequisites To use Amazon EC2 to install and configure the CloudWatch agent, you must meet the user and instance prerequisites described in this section.
Tip This feature is not available in all AWS Regions. If the menu item described in the installation procedure on this page does not exist in the Amazon EC2 console and you are flexible about where your instances run, try another Region. Otherwise, you can use the manual directions in the Amazon CloudWatch User Guide to install and configure the agent.
User prerequisites To use this feature, your IAM console user or role must have the permissions required for using Amazon EC2 and the following IAM permissions:
JSON {

    "Version":"2012-10-17", "Statement": [ { "Effect": "Allow", "Action": [ "ssm:GetParameter", "ssm:PutParameter"
            ], "Resource": "arn:aws:ssm:*:*:parameter/EC2-Custom-Metrics-*"
        }, { "Effect": "Allow", "Action": [ "ssm:SendCommand", "ssm:ListCommandInvocations", "ssm:DescribeInstanceInformation"
            ], "Resource": [ "*"
            ]
        }, { "Effect": "Allow", "Action": [ "iam:GetInstanceProfile", "iam:SimulatePrincipalPolicy"
            ], "Resource": "*"
        } ]
} Instance prerequisites
- Instance state: running
- Supported operating system: Linux
- AWS Systems Manager Agent (SSM Agent): Installed. Two notes about SSM Agent:
- SSM Agent is preinstalled on some Amazon Machine Images (AMIs) provided by AWS and trusted third-parties. For information about the supported AMIs and the instructions for installing SSM Agent, see Amazon Machine Images (AMIs) with SSM Agent preinstalled in the AWS Systems Manager User Guide.

- If you experience issues with the SSM Agent, see Troubleshooting SSM Agent in the AWS Systems Manager User Guide.
- IAM permissions for the instance: The following AWS managed policies must be added to an IAM role that is attached to the instance:
- AmazonSSMManagedInstanceCore – Enables an instance to use Systems Manager to install and configure the CloudWatch agent.
- CloudWatchAgentServerPolicy – Enables an instance to use the CloudWatch agent to write data to CloudWatch.
For information about how to add IAM permissions to your instance, see Use instance profiles in the IAM User Guide.
### How it works Before you can use the Amazon EC2 console to install and configure the CloudWatch agent, you must make sure that your IAM user or role, and the instances on which you want to add metrics, meet certain prerequisites. Then, you can use the Amazon EC2 console to install and configure the CloudWatch agent on your selected instances.
First meet the prerequisites
- You need the required IAM permissions – Before you get started, make sure that your console user or role has the required IAM permissions to use this feature.
- Instances – To use the feature, your EC2 instances must be Linux instances, have the SSM Agent installed, have the required IAM permissions, and be running.
Then you can use the feature
1. Select your instances – In the Amazon EC2 console, you select the instances on which to install and configure the CloudWatch agent. You then start the process by choosing Configure CloudWatch agent.
2. Validate SSM Agent – Amazon EC2 checks that the SSM Agent is installed and started on each instance. Any instances that fail this check are excluded from the process. The SSM Agent is used for performing actions on the instance during this process.
3. Validate IAM permissions – Amazon EC2 checks that each instance has the required IAM permissions for this process. Any instances that fail this check are excluded from the process.

The IAM permissions enable the CloudWatch agent to collect metrics from the instance and integrate with AWS Systems Manager to use the SSM Agent.
4. Validate CloudWatch agent – Amazon EC2 checks that the CloudWatch agent is installed and running on each instance. If any instances fail this check, Amazon EC2 offers to install and start the CloudWatch agent for you. The CloudWatch agent will collect the selected metrics on each instance once this process is completed.
5. Select metric configuration – You select the metrics for the CloudWatch agent to emit from your instances. Once selected, Amazon EC2 stores a configuration file in Parameter Store, where it remains until the process is completed. Amazon EC2 will delete the configuration file from Parameter Store unless the process is interrupted. Note that if you don't select a metric, but you previously added it to your instance, it will be removed from your instance when this process is completed.
6. Update CloudWatch agent configuration – Amazon EC2 sends the metric configuration to the CloudWatch agent. This is the last step in the process. If it succeeds, your instances can emit data for the selected metrics and Amazon EC2 deletes the configuration file from Parameter Store.
### Costs Additional metrics that you add during this process are billed as custom metrics. For more information about CloudWatch metrics pricing, see Amazon CloudWatch Pricing.
### Install and configure the CloudWatch agent You can use the Amazon EC2 console to install and configure the CloudWatch agent to add additional metrics.
Note Every time you perform this procedure, you overwrite the existing CloudWatch agent configuration. If you don't select a metric that was selected previously, it will be removed from the instance.
To install and configure the CloudWatch agent using the Amazon EC2 console
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Instances.

3. Select the instances on which to install and configure the CloudWatch agent.
4. Choose Actions, Monitor and troubleshoot, Configure CloudWatch agent.
5. For each step in the process, read the console text, and then choose Next.
6. To complete the process, in the final step, choose Complete.
To update the agent configuration created by the Amazon EC2 console You can manually customize the configuration that the EC2 console created. For more information, see Manually create or edit the CloudWatch agent configuration file in the Amazon CloudWatch User Guide.
## Statistics for CloudWatch metrics for your instances You can get statistics for the CloudWatch metrics for your instances. Statistics are metric data aggregations over specified periods of time. CloudWatch provides statistics based on the metric data points provided by your custom data or provided by other services in AWS to CloudWatch.
Aggregations are made using the namespace, metric name, dimensions, and the data point unit of measure, within the time period you specify. The following table describes the available statistics.
Statistic Description Minimum The lowest value observed during the specified period. You can use this value to determine low volumes of activity for your application.
Maximum The highest value observed during the specified period. You can use this value to determine high volumes of activity for your application.
Sum All values submitted for the matching metric added together. This statistic can be useful for determining the total volume of a metric.
Average The value of Sum / SampleCount  during the specified period. By comparing this statistic with the Minimum and Maximum, you can determine the full scope of a metric and how close the average use is to the Minimum and Maximum. This comparison helps you to know when to increase or decrease your resources as needed.
SampleCou nt The count (number) of data points used for the statistical calculation.

Statistic Description pNN.NN The value of the specified percentile. You can specify any percentile, using up to two decimal places (for example, p95.45).
Contents
- Get statistics for a specific instance
- Aggregate statistics across instances
- Aggregate statistics by Auto Scaling group
- Aggregate statistics by AMI
### Get statistics for a specific instance You can use the AWS Management Console or the AWS CLI to get statistics for a specific instance.
The following examples show you how to use the AWS Management Console or the AWS CLI to determine the maximum CPU utilization of a specific EC2 instance.
Requirements
- You must have the ID of the instance. You can get the instance ID using the AWS Management Console or the describe-instances command.
- By default, basic monitoring is enabled, but you can enable detailed monitoring. For more information, see Manage detailed monitoring for your EC2 instances.
To display the CPU utilization for a specific instance (console)
1. Open the CloudWatch console at https://console.aws.amazon.com/cloudwatch/.
2. In the navigation pane, choose Metrics.
3. Choose the EC2 metric namespace.
4. Choose the Per-Instance Metrics dimension.
5. In the search field, enter CPUUtilization and press Enter. Choose the row for the specific instance, which displays a graph for the CPUUtilization metric for the instance. To name the graph, choose the pencil icon. To change the time range, select one of the predefined values or choose custom.

6. To change the statistic or the period for the metric, choose the Graphed metrics tab. Choose the column heading or an individual value, and then choose a different value.
To get the CPU utilization for a specific instance (AWS CLI)

Use the following get-metric-statistics command to get the CPUUtilization metric for the specified instance, using the specified period and time interval: aws cloudwatch get-metric-statistics --namespace AWS/EC2 --metric-name CPUUtilization --period 3600 \ --statistics Maximum --dimensions Name=InstanceId,Value=i-1234567890abcdef0 \ --start-time 2022-10-18T23:18:00 --end-time 2022-10-19T23:18:00 The following is example output. Each value represents the maximum CPU utilization percentage for a single EC2 instance.
{ "Datapoints": [ { "Timestamp": "2022-10-19T00:18:00Z", "Maximum": 0.33000000000000002, "Unit": "Percent"
        }, { "Timestamp": "2022-10-19T03:18:00Z", "Maximum": 99.670000000000002, "Unit": "Percent"
        }, { "Timestamp": "2022-10-19T07:18:00Z", "Maximum": 0.34000000000000002, "Unit": "Percent"
        }, { "Timestamp": "2022-10-19T12:18:00Z", "Maximum": 0.34000000000000002, "Unit": "Percent"
        } ], "Label": "CPUUtilization"
}
### Aggregate statistics across instances Aggregate statistics are available for instances that have detailed monitoring enabled. Instances that use basic monitoring are not included in the aggregates. Before you can get statistics

aggregated across instances, you must enable detailed monitoring (at an additional charge), which provides data in 1-minute periods.
Note that Amazon CloudWatch cannot aggregate data across AWS Regions. Metrics are completely separate between Regions.
This example shows you how to use detailed monitoring to get the average CPU usage for your EC2 instances. Because no dimension is specified, CloudWatch returns statistics for all dimensions in the AWS/EC2 namespace.
Important This technique for retrieving all dimensions across an AWS namespace does not work for custom namespaces that you publish to Amazon CloudWatch. With custom namespaces, you must specify the complete set of dimensions that are associated with any given data point to retrieve statistics that include the data point.
To display average CPU utilization across your instances (console)
1. Open the CloudWatch console at https://console.aws.amazon.com/cloudwatch/.
2. In the navigation pane, choose Metrics.
3. Choose the EC2 namespace and then choose Across All Instances.
4. Choose the row that contains CPUUtilization, which displays a graph for the metric for all your EC2 instances. To name the graph, choose the pencil icon. To change the time range, select one of the predefined values or choose custom.

5. To change the statistic or the period for the metric, choose the Graphed metrics tab. Choose the column heading or an individual value, and then choose a different value.
To get average CPU utilization across your instances (AWS CLI)
Use the get-metric-statistics command as follows to get the average of the CPUUtilization metric across your instances. aws cloudwatch get-metric-statistics \ --namespace AWS/EC2 \ --metric-name CPUUtilization \ --period 3600  --statistics "Average" "SampleCount" \ --start-time 2022-10-11T23:18:00 \ --end-time 2022-10-12T23:18:00 The following is example output:

{ "Datapoints": [ { "SampleCount": 238.0, "Timestamp": "2022-10-12T07:18:00Z", "Average": 0.038235294117647062, "Unit": "Percent"
        }, { "SampleCount": 240.0, "Timestamp": "2022-10-12T09:18:00Z", "Average": 0.16670833333333332, "Unit": "Percent"
        }, { "SampleCount": 238.0, "Timestamp": "2022-10-11T23:18:00Z", "Average": 0.041596638655462197, "Unit": "Percent"
        } ], "Label": "CPUUtilization"
}
### Aggregate statistics by Auto Scaling group You can aggregate statistics for the EC2 instances in an Auto Scaling group. Note that Amazon CloudWatch cannot aggregate data across AWS Regions. Metrics are completely separate between Regions.
This example shows you how to retrieve the total bytes written to disk for one Auto Scaling group.
The total is computed for 1-minute periods for a 24-hour interval across all EC2 instances in the specified Auto Scaling group.
To display DiskWriteBytes for the instances in an Auto Scaling group (console)
1. Open the CloudWatch console at https://console.aws.amazon.com/cloudwatch/.
2. In the navigation pane, choose Metrics.
3. Choose the EC2 namespace and then choose By Auto Scaling Group.
4. Choose the row for the DiskWriteBytes metric and the specific Auto Scaling group, which displays a graph for the metric for the instances in the Auto Scaling group. To name the graph,

choose the pencil icon. To change the time range, select one of the predefined values or choose custom.
5. To change the statistic or the period for the metric, choose the Graphed metrics tab. Choose the column heading or an individual value, and then choose a different value.
To display DiskWriteBytes for the instances in an Auto Scaling group (AWS CLI)
Use the get-metric-statistics command as follows. aws cloudwatch get-metric-statistics --namespace AWS/EC2 --metric-name DiskWriteBytes --period 360 \ --statistics "Sum" "SampleCount" --dimensions Name=AutoScalingGroupName,Value=my-asg -- start-time 2022-10-16T23:18:00 --end-time 2022-10-18T23:18:00 The following is example output:
{ "Datapoints": [ { "SampleCount": 18.0, "Timestamp": "2022-10-19T21:36:00Z", "Sum": 0.0, "Unit": "Bytes"
        }, { "SampleCount": 5.0, "Timestamp": "2022-10-19T21:42:00Z", "Sum": 0.0, "Unit": "Bytes"
        } ], "Label": "DiskWriteBytes"
}
### Aggregate statistics by AMI You can aggregate statistics by AMI for your instances that have detailed monitoring enabled.
Instances that use basic monitoring are not included in the aggregates. Before you can get statistics aggregated across instances, you must enable detailed monitoring (at an additional charge), which provides data in 1-minute periods.

Note that Amazon CloudWatch cannot aggregate data across AWS Regions. Metrics are completely separate between Regions.
This example shows you how to determine average CPU utilization for all instances that use a specific Amazon Machine Image (AMI). The average is over 60-second time intervals for a one-day period.
To display the average CPU utilization by AMI (console)
1. Open the CloudWatch console at https://console.aws.amazon.com/cloudwatch/.
2. In the navigation pane, choose Metrics.
3. Choose the EC2 namespace and then choose By Image (AMI) Id.
4. Choose the row for the CPUUtilization metric and the specific AMI, which displays a graph for the metric for the specified AMI. To name the graph, choose the pencil icon. To change the time range, select one of the predefined values or choose custom.
5. To change the statistic or the period for the metric, choose the Graphed metrics tab. Choose the column heading or an individual value, and then choose a different value.
To get the average CPU utilization for an image ID (AWS CLI)
Use the get-metric-statistics command as follows. aws cloudwatch get-metric-statistics --namespace AWS/EC2 --metric-name CPUUtilization --period 3600 \ --statistics Average --dimensions Name=ImageId,Value=ami-3c47a355 --start- time 2022-10-10T00:00:00 --end-time 2022-10-11T00:00:00 The following is example output. Each value represents an average CPU utilization percentage for the EC2 instances running the specified AMI.
{ "Datapoints": [ { "Timestamp": "2022-10-10T07:00:00Z", "Average": 0.041000000000000009, "Unit": "Percent"
        }, {

            "Timestamp": "2022-10-10T14:00:00Z", "Average": 0.079579831932773085, "Unit": "Percent"
        }, { "Timestamp": "2022-10-10T06:00:00Z", "Average": 0.036000000000000011, "Unit": "Percent"
        } ], "Label": "CPUUtilization"
}
## View the monitoring graphs for your instances After you launch an instance, you can open the Amazon EC2 console and view the monitoring graphs for the instance on the Monitoring tab. Each graph is based on one of the available Amazon EC2 metrics.
The following graphs are available:
- Average CPU Utilization (Percent)
- Average Disk Reads (Bytes)
- Average Disk Writes (Bytes)
- Maximum Network In (Bytes)
- Maximum Network Out (Bytes)
- Summary Disk Read Operations (Count)
- Summary Disk Write Operations (Count)
- Summary Status (Any)
- Summary Status Instance (Count)
- Summary Status System (Count)
For more information about the metrics and the data they provide to the graphs, see CloudWatch metrics that are available for your instances.
Graph metrics using the CloudWatch console

You can also use the CloudWatch console to graph metric data generated by Amazon EC2 and other AWS services. For more information, see Graphing metrics in the Amazon CloudWatch User Guide.
## Create a CloudWatch alarm for an instance You can create a CloudWatch alarm that monitors CloudWatch metrics for one of your instances.
CloudWatch will automatically send you a notification when the metric reaches a threshold you specify. You can create a CloudWatch alarm using the Amazon EC2 console, or using the more advanced options provided by the CloudWatch console.
To create an alarm using the CloudWatch console For examples, see Creating Amazon CloudWatch Alarms in the Amazon CloudWatch User Guide.
To create an alarm using the Amazon EC2 console
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Instances.
3. Select the instance and choose Actions, Monitor and troubleshoot, Manage CloudWatch alarms.
4. On the Manage CloudWatch alarms detail page, under Add or edit alarm, select Create an alarm.
5. For Alarm notification, choose whether to configure Amazon Simple Notification Service (Amazon SNS) notifications. Enter an existing Amazon SNS topic or enter a name to create a new topic.
6. For Alarm action, choose whether to specify an action to take when the alarm is triggered.
Choose an action from the list.
7. For Alarm thresholds, select the metric and criteria for the alarm. For example, to create an alarm that is triggered when CPU utilization reaches 80% for a 5 minute period, do the following: a.
Keep the default setting for Group samples by (Average) and Type of data to sample (CPU utilization). b.
Choose >= for Alarm when and enter 0.80 for Percent. c.
Enter 1 for Consecutive period and select 5 minutes for Period.
8. (Optional) For Sample metric data, choose Add to dashboard.

9. Choose Create.
You can edit your CloudWatch alarm settings from the Amazon EC2 console or the CloudWatch console. If you want to delete your alarm, you can do so from the CloudWatch console. For more information, see Edit or delete a CloudWatch alarm in the Amazon CloudWatch User Guide.
## Create alarms that stop, terminate, reboot, or recover an instance Using Amazon CloudWatch alarm actions, you can create alarms that automatically stop, terminate, reboot, or recover your instances. You can use the stop or terminate actions to help you save money when you no longer need an instance to be running. You can use the reboot and recover actions to automatically reboot those instances or recover them onto new hardware if a system impairment occurs.
Note For Amazon CloudWatch alarms billing and pricing information, see  CloudWatch billing and cost in the Amazon CloudWatch User Guide.
The AWSServiceRoleForCloudWatchEvents service-linked role enables AWS to perform alarm actions on your behalf. The first time you create an alarm in the AWS Management Console, the AWS CLI, or the IAM API, CloudWatch creates the service-linked role for you.
There are a number of scenarios in which you might want to automatically stop or terminate your instance. For example, you might have instances dedicated to batch payroll processing jobs or scientific computing tasks that run for a period of time and then complete their work. Rather than letting those instances sit idle (and accrue charges), you can stop or terminate them, which can help you to save money. The main difference between using the stop and the terminate alarm actions is that you can easily start a stopped instance if you need to run it again later, and you can keep the same instance ID and root volume. However, you cannot start a terminated instance.
Instead, you must launch a new instance. When an instance is stopped or terminated, data on instance store volumes is lost.
You can add the stop, terminate, reboot, or recover actions to any alarm that is set on an Amazon EC2 per-instance metric, including basic and detailed monitoring metrics provided by Amazon CloudWatch (in the AWS/EC2 namespace), as well as any custom metrics that include the InstanceId dimension, as long as its value refers to a valid running Amazon EC2 instance.

Important Status check alarms can temporarily enter the INSUFFICIENT_DATA state if there are missing metric data points. Although rare, this can happen when there is an interruption in the metric reporting systems, even when an instance is healthy. We recommend that you treat the INSUFFICIENT_DATA state as missing data instead of an alarm breach, especially when configuring the alarm to stop, terminate, reboot, or recover an instance.
Console support You can create alarms using the Amazon EC2 console or the CloudWatch console. The procedures in this documentation use the Amazon EC2 console. For procedures that use the CloudWatch console, see Create alarms that stop, terminate, reboot, or recover an instance in the Amazon CloudWatch User Guide.
Permissions You must have the iam:CreateServiceLinkedRole to create or modify an alarm that performs EC2 alarm actions. A service role is an IAM role that a service assumes to perform actions on your behalf. An IAM administrator can create, modify, and delete a service role from within IAM. For more information, see Create a role to delegate permissions to an AWS service in the IAM User Guide.
Contents
- Add stop actions to Amazon CloudWatch alarms
- Add terminate actions to Amazon CloudWatch alarms
- Add reboot actions to Amazon CloudWatch alarms
- Add recover actions to Amazon CloudWatch alarms
- Amazon CloudWatch alarm action scenarios
### Add stop actions to Amazon CloudWatch alarms You can create an alarm that stops an Amazon EC2 instance when a certain threshold has been met. For example, you may run development or test instances and occasionally forget to shut them off. You can create an alarm that is triggered when the average CPU utilization percentage has been lower than 10 percent for 24 hours, signaling that it is idle and no longer in use. You can

adjust the threshold, duration, and period to suit your needs, plus you can add an Amazon Simple Notification Service (Amazon SNS) notification so that you receive an email when the alarm is triggered.
Instances that use an Amazon EBS volume as the root volume can be stopped or terminated, whereas instances that use the instance store as the root volume can only be terminated. Data on instance store volumes is lost when the instance is terminated or stopped.
To create an alarm to stop an idle instance (Amazon EC2 console)
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Instances.
3. Select the instance and choose Actions, Monitor and troubleshoot, Manage CloudWatch alarms.
Alternatively, you can choose the plus sign ( ) in the Alarm status column.
4. On the Manage CloudWatch alarms page, do the following: a.
Choose Create an alarm. b.
To receive an email when the alarm is triggered, for Alarm notification, choose an existing Amazon SNS topic. You first need to create an Amazon SNS topic using the Amazon SNS console. For more information, see Using Amazon SNS for application-to-person (A2P) messaging in the Amazon Simple Notification Service Developer Guide. c.
Toggle on Alarm action, and choose Stop. d.
For Group samples by and Type of data to sample, choose a statistic and a metric. In this example, choose Average and CPU utilization. e.
For Alarm When and Percent, specify the metric threshold. In this example, specify <= and 10 percent. f.
For Consecutive period and Period, specify the evaluation period for the alarm. In this example, specify 1 consecutive period of 5 Minutes. g.
Amazon CloudWatch automatically creates an alarm name for you. To change the name, for Alarm name, enter a new name. Alarm names must contain only ASCII characters.

Note You can adjust the alarm configuration based on your own requirements before creating the alarm, or you can edit them later. This includes the metric, threshold, duration, action, and notification settings. However, after you create an alarm, you cannot edit its name later. h.
Choose Create.
### Add terminate actions to Amazon CloudWatch alarms You can create an alarm that terminates an EC2 instance automatically when a certain threshold has been met (as long as termination protection is not enabled for the instance). For example, you might want to terminate an instance when it has completed its work, and you don't need the instance again. If you might want to use the instance later, you should stop the instance instead of terminating it. Data on instance store volumes is lost when the instance is terminated. For information about enabling and disabling termination protection for an instance, see Change instance termination protection.
To create an alarm to terminate an idle instance (Amazon EC2 console)
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Instances.
3. Select the instance and choose Actions, Monitor and troubleshoot, Manage CloudWatch alarms.
Alternatively, you can choose the plus sign ( ) in the Alarm status column.
4. On the Manage CloudWatch alarms page, do the following: a.
Choose Create an alarm. b.
To receive an email when the alarm is triggered, for Alarm notification, choose an existing Amazon SNS topic. You first need to create an Amazon SNS topic using the Amazon SNS console. For more information, see Using Amazon SNS for application-to-person (A2P) messaging in the Amazon Simple Notification Service Developer Guide.

c.
Toggle on Alarm action, and choose Terminate. d.
For Group samples by and Type of data to sample, choose a statistic and a metric. In this example, choose Average and CPU utilization. e.
For Alarm When and Percent, specify the metric threshold. In this example, specify => and 10 percent. f.
For Consecutive period and Period, specify the evaluation period for the alarm. In this example, specify 24 consecutive periods of 1 Hour. g.
Amazon CloudWatch automatically creates an alarm name for you. To change the name, for Alarm name, enter a new name. Alarm names must contain only ASCII characters.
Note You can adjust the alarm configuration based on your own requirements before creating the alarm, or you can edit them later. This includes the metric, threshold, duration, action, and notification settings. However, after you create an alarm, you cannot edit its name later. h.
Choose Create.
### Add reboot actions to Amazon CloudWatch alarms You can create an Amazon CloudWatch alarm that monitors an Amazon EC2 instance and automatically reboots the instance. The reboot alarm action is recommended for Instance Health Check failures (as opposed to the recover alarm action, which is suited for System Health Check failures). An instance reboot is equivalent to an operating system reboot. In most cases, it takes only a few minutes to reboot your instance. When you reboot an instance, it remains on the same physical host, so your instance keeps its public DNS name, private IP address, and any data on its instance store volumes.
Rebooting an instance doesn't start a new instance billing period (with a minimum one-minute charge), unlike stopping and restarting your instance. Data on instance store volumes is retained when the instance is rebooted. The instance store volumes must be re-mounted into the filesystem after a reboot. For more information, see Reboot your Amazon EC2 instance.

Important To avoid a race condition between the reboot and recover actions, avoid setting the same number of evaluation periods for a reboot alarm and a recover alarm. We recommend that you set reboot alarms to three evaluation periods of one minute each. For more information, see Evaluating an alarm in the Amazon CloudWatch User Guide.
To create an alarm to reboot an instance (Amazon EC2 console)
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Instances.
3. Select the instance and choose Actions, Monitor and troubleshoot, Manage CloudWatch alarms.
Alternatively, you can choose the plus sign ( ) in the Alarm status column.
4. On the Manage CloudWatch alarms page, do the following: a.
Choose Create an alarm. b.
To receive an email when the alarm is triggered, for Alarm notification, choose an existing Amazon SNS topic. You first need to create an Amazon SNS topic using the Amazon SNS console. For more information, see Using Amazon SNS for application-to-person (A2P) messaging in the Amazon Simple Notification Service Developer Guide. c.
Toggle on Alarm action, and choose Reboot. d.
For Group samples by and Type of data to sample, choose a statistic and a metric. In this example, choose Average and Status check failed: instance. e.
For Consecutive period and Period, specify the evaluation period for the alarm. In this example, enter 3 consecutive periods of 1 Minute. If 1 Minute is disabled, you must enable detailed monitoring, or you can choose 5 Minutes instead. f.
Amazon CloudWatch automatically creates an alarm name for you. To change the name, for Alarm name, enter a new name. Alarm names must contain only ASCII characters. g.
Choose Create.

### Add recover actions to Amazon CloudWatch alarms You can create an Amazon CloudWatch alarm that monitors an Amazon EC2 instance. If the instance becomes impaired due to an underlying hardware failure or a problem that requires AWS involvement to repair, you can automatically recover the instance. Terminated instances cannot be recovered. A recovered instance is identical to the original instance, including the instance ID, private IP addresses, Elastic IP addresses, and all instance metadata.
CloudWatch prevents you from adding a recovery action to an alarm that is on an instance which does not support recovery actions.
When the StatusCheckFailed_System alarm is triggered, and the recover action is initiated, you are notified by the Amazon SNS topic that you chose when you created the alarm and associated the recover action. During instance recovery, the instance is migrated during an instance reboot, and any data that is in-memory is lost. When the process is complete, information is published to the SNS topic you've configured for the alarm. Anyone who is subscribed to this SNS topic receives an email notification that includes the status of the recovery attempt and any further instructions. You notice an instance reboot on the recovered instance.
Note The recover action can be used only with StatusCheckFailed_System, not with StatusCheckFailed_Instance.
The following problems can cause system status checks to fail:
- Loss of network connectivity
- Loss of system power
- Software issues on the physical host
- Hardware issues on the physical host that impact network reachability The recover action is supported only on instances that meet certain characteristics. For more information, see Automatic instance recovery.
If your instance has a public IP address, it retains the public IP address after recovery.

Important To avoid a race condition between the reboot and recover actions, avoid setting the same number of evaluation periods for a reboot alarm and a recover alarm. We recommend that you set recover alarms to two evaluation periods of one minute each. For more information, see Evaluating an alarm in the Amazon CloudWatch User Guide.
To create an alarm to recover an instance (Amazon EC2 console)
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Instances.
3. Select the instance and choose Actions, Monitor and troubleshoot, Manage CloudWatch alarms.
Alternatively, you can choose the plus sign ( ) in the Alarm status column.
4. On the Manage CloudWatch alarms page, do the following: a.
Choose Create an alarm. b.
To receive an email when the alarm is triggered, for Alarm notification, choose an existing Amazon SNS topic. You first need to create an Amazon SNS topic using the Amazon SNS console. For more information, see Using Amazon SNS for application-to-person (A2P) messaging in the Amazon Simple Notification Service Developer Guide.
Note Users must subscribe to the specified SNS topic to receive email notifications when the alarm is triggered. The AWS account root user always receives email notifications when automatic instance recovery actions occur, even if an SNS topic is not specified or the root user is not subscribed to the specified SNS topic. c.
Toggle on Alarm action, and choose Recover. d.
For Group samples by and Type of data to sample, choose a statistic and a metric. In this example, choose Average and Status check failed: system.

e.
For Consecutive period and Period, specify the evaluation period for the alarm. In this example, enter 2 consecutive periods of 1 Minute. If 1 Minute is disabled, you must enable detailed monitoring, or you can choose 5 Minutes instead. f.
Amazon CloudWatch automatically creates an alarm name for you. To change the name, for Alarm name, enter a new name. Alarm names must contain only ASCII characters. g.
Choose Create.
### Amazon CloudWatch alarm action scenarios You can use the Amazon EC2 console to create alarm actions that stop or terminate an Amazon EC2 instance when certain conditions are met. In the following screen capture of the console page where you set the alarm actions, we've numbered the settings. We've also numbered the settings in the scenarios that follow, to help you create the appropriate actions.

#### Scenario 1: Stop idle development and test instances Create an alarm that stops an instance used for software development or testing when it has been idle for at least an hour.
Setting Value 1 Stop

Setting Value 2 Maximum 3 CPU Utilization 4 <= 5 10% 6 1 7 1 Hour
#### Scenario 2: Stop idle instances Create an alarm that stops an instance and sends an email when the instance has been idle for 24 hours.
Setting Value 1 Stop and email 2 Average 3 CPU Utilization 4 <= 5 5% 6 24 7 1 Hour
#### Scenario 3: Send email about web servers with unusually high traffic Create an alarm that sends email when an instance exceeds 10 GB of outbound network traffic per day.

Setting Value 1 Email 2 Sum 3 Network Out 4
>
5 10 GB 6 24 7 1 Hour
#### Scenario 4: Stop web servers with unusually high traffic Create an alarm that stops an instance and send a text message (SMS) if outbound traffic exceeds 1 GB per hour.
Setting Value 1 Stop and send SMS 2 Sum 3 Network Out 4
>
5 1 GB 6 1 7 1 Hour

#### Scenario 5: Stop an impaired instance Create an alarm that stops an instance that fails three consecutive status checks (performed at 5- minute intervals).
Setting Value 1 Stop 2 Average 3 Status Check Failed: System 4 - 5 - 6 1 7 15 Minutes
#### Scenario 6: Terminate instances when batch processing jobs are complete Create an alarm that terminates an instance that runs batch jobs when it is no longer sending results data.
Setting Value 1 Terminate 2 Maximum 3 Network Out 4 <= 5 100,000 bytes 6 1
