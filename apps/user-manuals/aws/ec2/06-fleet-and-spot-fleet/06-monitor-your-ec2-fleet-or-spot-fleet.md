# Monitor your EC2 Fleet or Spot Fleet

Source: apps/user-manuals/aws/ec2-ug.pdf

---

5. Select the scheduled action and choose Actions, Edit.
6. Make the needed changes and choose Submit.
To delete a scheduled action
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Spot Requests.
3. Select your Spot Fleet request.
4. Choose the Scheduled Scaling tab near the bottom of the screen. If you selected the link for your Spot Fleet, there is no tab; instead, scroll down to the Scheduled Scaling section.
5. Select the scheduled action and choose Actions, Delete.
6. When prompted for confirmation, choose Delete.
To manage scheduled scaling using the AWS CLI Use the following commands:
- put-scheduled-action
- describe-scheduled-actions
- delete-scheduled-action
# Monitor your EC2 Fleet or Spot Fleet Effective monitoring of your EC2 Fleet or Spot Fleet is essential for maintaining optimal performance and ensuring reliability. There are various tools to help you achieve this, including Amazon CloudWatch and Amazon EventBridge, which are covered in this topic.
With CloudWatch, you can collect and track metrics, set alarms, and automatically react to changes in your fleet's status.
With EventBridge, you can monitor and respond programmatically to events emitted by your fleet.
By defining rules in EventBridge, you can automate responses to specific fleet events, such as instance termination or fleet state changes, improving your operational efficiency.
Topics

- Monitor your EC2 Fleet or Spot Fleet using CloudWatch
- Monitor and programmatically respond to the events emitted by your EC2 Fleet or Spot Fleet using Amazon EventBridge
## Monitor your EC2 Fleet or Spot Fleet using CloudWatch You can monitor your EC2 Fleet or Spot Fleet using the Amazon CloudWatch metrics described in this section.
Important To ensure accuracy, we recommend that you enable detailed monitoring when using these metrics. For more information, see Manage detailed monitoring for your EC2 instances.
For more information about using CloudWatch, see Monitor your instances using CloudWatch.
### EC2 Fleet and Spot Fleet metrics The AWS/EC2Spot namespace includes the following metrics for your fleet, plus the CloudWatch metrics for the Spot Instances in your fleet. For more information, see Instance metrics.
Metric Description AvailableInstanceP oolsCount The Spot capacity pools specified in the fleet request.
Units: Count BidsSubmittedForCa pacity The capacity for which Amazon EC2 has submitted fleet requests.
Units: Count EligibleInstancePo olCount The Spot capacity pools specified in the fleet request where Amazon EC2 can fulfill requests. Amazon EC2 does not fulfill requests in pools where the maximum price you're willing to pay for Spot Instances is less than the Spot price or the Spot price is greater than the price for On-Demand Instances.

Metric Description Units: Count FulfilledCapacity The capacity that Amazon EC2 has fulfilled.
Units: Count MaxPercentCapacity Allocation The maximum value of PercentCapacityAllocation across all fleet pools specified in the fleet request.
Units: Percent PendingCapacity The difference between TargetCapacity  and FulfilledCapacity .
Units: Count PercentCapacityAll ocation The capacity allocated for the Spot capacity pool for the specified dimensions. To get the maximum value recorded across all Spot capacity pools, use MaxPercentCapacity Allocation .
Units: Percent TargetCapacity The target capacity of the fleet request.
Units: Count TerminatingCapacity The capacity that is being terminated because the provision ed capacity is greater than the target capacity.
Units: Count If the unit of measure for a metric is Count, the most useful statistic is Average.
### EC2 Fleet and Spot Fleet dimensions To filter the data for your fleet, use the following dimensions.

Dimensions Description AvailabilityZone Filter the data by Availability Zone.
FleetRequestId Filter the data by fleet request.
InstanceType Filter the data by instance type.
### View the CloudWatch metrics for your EC2 Fleet or Spot Fleet You can view the CloudWatch metrics for your fleet using the Amazon CloudWatch console. These metrics are displayed as monitoring graphs. These graphs show data points if the fleet is active.
Metrics are grouped first by namespace, and then by the various combinations of dimensions within each namespace. For example, you can view all fleet metrics or fleet metrics groups by fleet request ID, instance type, or Availability Zone.
To view fleet metrics
1. Open the CloudWatch console at https://console.aws.amazon.com/cloudwatch/.
2. In the navigation pane, expand Metrics, and choose All metrics.
3. Choose the EC2 Spot namespace.
Note If the EC2 Spot namespace is not displayed, there are two reasons for this. Either you have never used EC2 Fleet or Spot Fleet in the Region—only the AWS services that you're using send metrics to Amazon CloudWatch. Or, if you have used EC2 Fleet or Spot Fleet in the Region, but not for the past two weeks, the namespace does not appear.
4. To filter the metrics by dimension, choose one of the following:
- Fleet Request Metrics – Group by fleet request
- By Availability Zone – Group by fleet request and Availability Zone
- By Instance Type – Group by fleet request and instance type

- By Availability Zone/Instance Type – Group by fleet request, Availability Zone, and instance type
5. To view the data for a metric, select the checkbox next to the metric.
## Monitor and programmatically respond to the events emitted by your EC2 Fleet or Spot Fleet using Amazon EventBridge EC2 Fleet or Spot Fleet using Amazon EventBridge When the state of an EC2 Fleet or Spot Fleet changes, it emits a notification. The notification is made available as an event that is sent to Amazon EventBridge (formerly known as Amazon CloudWatch Events). Events are emitted on a best effort basis.
You can use Amazon EventBridge to create rules that trigger programmatic actions in response to an event. For example, you can create two EventBridge rules: one triggered when a fleet state changes, and another triggered when an instance in the fleet is terminated. In this example, you can configure the first rule so that, if the fleet state changes, the rule invokes an SNS topic, sending an email notification to you. You can configure the second rule so that, if an instance in the fleet is terminated, the rule invokes a Lambda function to launch a new instance.
Note Only fleets of type maintain and request emit events. Fleets of type instant do not emit events because they submit synchronous one-time requests, and the state of the fleet is known immediately in the response. To use Amazon EventBridge to monitor fleet events, the request type must be maintain or request.
For instructions on how to describe a fleet's event history, see Describe the event history for your EC2 Fleet.
Topics
- Create Amazon EventBridge rules to monitor EC2 Fleet or Spot Fleet events
- EC2 Fleet event types
- Spot Fleet event types

### Create Amazon EventBridge rules to monitor EC2 Fleet or Spot Fleet events When a state change notification is emitted for an EC2 Fleet or Spot Fleet, it is sent as an event to Amazon EventBridge as a JSON file. If EventBridge detects an event pattern that matches a pattern defined in a rule, EventBridge invokes the target (or targets) specified in the rule.
You can write EventBridge rules to automate actions based on matching event patterns.
The following fields in the event form the event pattern that is defined in the rule:
"source": "aws.ec2fleet"
Identifies that the event is from EC2 Fleet.
"detail-type": "EC2 Fleet State Change"
Identifies the event type.
"detail": { "sub-type": "submitted" } Identifies the event sub-type.
For the list of EC2 Fleet and Spot Fleet events and example event data, see EC2 Fleet event types and Spot Fleet event types.
Examples
- Create an EventBridge rule to send a notification
- Create an EventBridge rule to trigger a Lambda function
#### Create an EventBridge rule to send a notification The following example creates an EventBridge rule to send an email, text message, or mobile push notification every time that Amazon EC2 emits an EC2 Fleet state change notification. The signal in this example is emitted as an EC2 Fleet State Change event, which triggers the action defined by the rule.
Prerequisite Before creating the EventBridge rule, you must create the Amazon SNS topic for the email, text message, or mobile push notification.

To create an EventBridge rule to send a notification when an EC2 Fleet state changes
1. Open the Amazon EventBridge console at https://console.aws.amazon.com/events/.
2. Choose Create rule.
3. For Define rule detail, do the following: a.
Enter a Name for the rule, and, optionally, a description.
A rule can't have the same name as another rule in the same Region and on the same event bus. b.
For Event bus, choose default. When an AWS service in your account generates an event, it always goes to your account's default event bus. c.
For Rule type, choose Rule with an event pattern. d.
Choose Next.
4. For Build event pattern, do the following: a.
For Event source, choose AWS events or EventBridge partner events. b.
For Event pattern, for this example you'll specify the following event pattern to match the EC2 Fleet Instance Change event.
{ "source": ["aws.ec2fleet"], "detail-type": ["EC2 Fleet Instance Change"]
} To add the event pattern, you can either use a template by choosing Event pattern form, or specify your own pattern by choosing Custom pattern (JSON editor), as follows: i.
To use a template to create the event pattern, do the following:
A.
Choose Event pattern form.
B.
For Event source, choose AWS services.
C.
For AWS Service, choose EC2 Fleet.
D.
For Event type, choose EC2 Fleet Instance Change.
E.
To customize the template, choose Edit pattern and make your changes to match the example event pattern. ii.
(Alternative) To specify a custom event pattern, do the following:

A.
Choose Custom pattern (JSON editor).
B.
In the Event pattern box, add the event pattern for this example. c.
Choose Next.
5. For Select target(s), do the following: a.
For Target types, choose AWS service. b.
For Select a target, choose SNS topic to send an email, text message, or mobile push notification when the event occurs. c.
For Topic, choose an existing topic. You first need to create an Amazon SNS topic using the Amazon SNS console. For more information, see Using Amazon SNS for application- to-person (A2P) messaging in the Amazon Simple Notification Service Developer Guide. d.
(Optional) Under Additional settings, you can optionally configure additional settings. For more information, see Creating Amazon EventBridge rules that react to events (step 16) in the Amazon EventBridge User Guide. e.
Choose Next.
6. (Optional) For Tags, you can optionally assign one or more tags to your rule, and then choose Next.
7. For Review and create, do the following: a.
Review the details of the rule and modify them as necessary. b.
Choose Create rule.
For more information, see Amazon EventBridge rules and Amazon EventBridge event patterns in the Amazon EventBridge User Guide
#### Create an EventBridge rule to trigger a Lambda function The following example creates an EventBridge rule to trigger a Lambda function every time that Amazon EC2 emits an EC2 Fleet instance change notification for when an instance is launched.
The signal in this example is emitted as an EC2 Fleet Instance Change event, sub-type launched, which triggers the action defined by the rule.
Before creating the EventBridge rule, you must create the Lambda function.

To create the Lambda function to use in the EventBridge rule
1. Open the AWS Lambda console at https://console.aws.amazon.com/lambda/.
2. Choose Create function.
3. Enter a name for your function, configure the code, and then choose Create function.
For more information, see Create your first Lambda function in the AWS Lambda Developer Guide.
To create an EventBridge rule to trigger a Lambda function when an instance in an EC2 Fleet changes state
1. Open the Amazon EventBridge console at https://console.aws.amazon.com/events/.
2. Choose Create rule.
3. For Define rule detail, do the following: a.
Enter a Name for the rule, and, optionally, a description.
A rule can't have the same name as another rule in the same Region and on the same event bus. b.
For Event bus, choose default. When an AWS service in your account generates an event, it always goes to your account's default event bus. c.
For Rule type, choose Rule with an event pattern. d.
Choose Next.
4. For Build event pattern, do the following: a.
For Event source, choose AWS events or EventBridge partner events. b.
For Event pattern, for this example you'll specify the following event pattern to match the EC2 Fleet Instance Change event and launched sub-type.
{ "source": ["aws.ec2fleet"], "detail-type": ["EC2 Fleet Instance Change"], "detail": { "sub-type": ["launched"]
}

To add the event pattern, you can either use a template by choosing Event pattern form, or specify your own pattern by choosing Custom pattern (JSON editor), as follows: i.
To use a template to create the event pattern, do the following:
A.
Choose Event pattern form.
B.
For Event source, choose AWS services.
C.
For AWS Service, choose EC2 Fleet.
D.
For Event type, choose EC2 Fleet Instance Change.
E.
Choose Edit pattern, and add "detail": {"sub-type": ["launched"] to match the example event pattern. For proper JSON format, insert a comma (,) after the preceding square bracket (]). ii.
(Alternative) To specify a custom event pattern, do the following:
A.
Choose Custom pattern (JSON editor).
B.
In the Event pattern box, add the event pattern for this example. c.
Choose Next.
5. For Select target(s), do the following: a.
For Target types, choose AWS service. b.
For Select a target, choose SNS topic to send an email, text message, or mobile push notification when the event occurs. c.
For Topic, choose Lambda function, and for Function, choose the function that you created to respond when the event occurs. d.
(Optional) Under Additional settings, you can optionally configure additional settings. For more information, see Creating Amazon EventBridge rules that react to events (step 16) in the Amazon EventBridge User Guide. e.
Choose Next.
6. (Optional) For Tags, you can optionally assign one or more tags to your rule, and then choose Next.
7. For Review and create, do the following: a.
Review the details of the rule and modify them as necessary. b.
Choose Create rule.

For a tutorial on how to create a Lambda function and an EventBridge rule that runs the Lambda function, see Tutorial: Log the State of an Amazon EC2 Instance Using EventBridge in the AWS Lambda Developer Guide.
### EC2 Fleet event types There are five EC2 Fleet event types. For each event type, there are several sub-types.
Event types
- EC2 Fleet State Change
- EC2 Fleet Spot Instance Request Change
- EC2 Fleet Instance Change
- EC2 Fleet Information
- EC2 Fleet Error
#### EC2 Fleet State Change EC2 Fleet sends an EC2 Fleet State Change event to Amazon EventBridge when an EC2 Fleet changes state.
The following is example data for this event.
{ "version": "0", "id": "715ed6b3-b8fc-27fe-fad6-528c7b8bf8a2", "detail-type": "EC2 Fleet State Change", "source": "aws.ec2fleet", "account": "123456789012", "time": "2020-11-09T09:00:20Z", "region": "us-east-1", "resources": [ "arn:aws:ec2:us-east-1:123456789012:fleet/fleet-598fb973-87b7-422d- be4d-6b0809bfff0a"
    ], "detail": { "sub-type": "active"
    } } The possible values for sub-type are:

active The EC2 Fleet request has been validated and Amazon EC2 is attempting to maintain the target number of running instances. deleted The EC2 Fleet request is deleted and has no running instances. The EC2 Fleet will be deleted two days after its instances are terminated. deleted_running The EC2 Fleet request is deleted and does not launch additional instances. Its existing instances continue to run until they are interrupted or terminated. The request remains in this state until all instances are interrupted or terminated. deleted_terminating The EC2 Fleet request is deleted and its instances are terminating. The request remains in this state until all instances are terminated. expired The EC2 Fleet request has expired. If the request was created with TerminateInstancesWithExpiration set, a subsequent terminated event indicates that the instances are terminated. modify_in_progress The EC2 Fleet request is being modified. The request remains in this state until the modification is fully processed. modify_succeeded The EC2 Fleet request was modified. submitted The EC2 Fleet request is being evaluated and Amazon EC2 is preparing to launch the target number of instances. progress The EC2 Fleet request is in the process of being fulfilled.

#### EC2 Fleet Spot Instance Request Change EC2 Fleet sends an EC2 Fleet Spot Instance Request Change event to Amazon EventBridge when a Spot Instance request in the fleet changes state.
The following is example data for this event.
{ "version": "0", "id": "19331f74-bf4b-a3dd-0f1b-ddb1422032b9", "detail-type": "EC2 Fleet Spot Instance Request Change", "source": "aws.ec2fleet", "account": "123456789012", "time": "2020-11-09T09:00:05Z", "region": "us-east-1", "resources": [ "arn:aws:ec2:us-east-1:123456789012:fleet/ fleet-83fd4e48-552a-40ef-9532-82a3acca5f10"
    ], "detail": { "spot-instance-request-id": "sir-rmqske6h", "description": "SpotInstanceRequestId sir-rmqske6h, PreviousState: cancelled_running", "sub-type": "cancelled"
    } } The possible values for sub-type are: active The Spot Instance request is fulfilled and has an associated Spot Instance. cancelled You cancelled the Spot Instance request, or the Spot Instance request expired. disabled You stopped the Spot Instance. submitted The Spot Instance request is submitted.

#### EC2 Fleet Instance Change EC2 Fleet sends an EC2 Fleet Instance Change event to Amazon EventBridge when an instance in the fleet changes state.
The following is example data for this event.
{ "version": "0", "id": "542ce428-c8f1-0608-c015-e8ed6522c5bc", "detail-type": "EC2 Fleet Instance Change", "source": "aws.ec2fleet", "account": "123456789012", "time": "2020-11-09T09:00:23Z", "region": "us-east-1", "resources": [ "arn:aws:ec2:us-east-1:123456789012:fleet/fleet-598fb973-87b7-422d- be4d-6b0809bfff0a"
    ], "detail": { "instance-id": "i-0c594155dd5ff1829", "description": "{\"instanceType\":\"c5.large\",\"image\":\"ami-6057e21a\", \"productDescription\":\"Linux/UNIX\",\"availabilityZone\":\"us-east-1d\"}", "sub-type": "launched"
    } } The possible values for sub-type are: launched A new instance was launched. terminated The instance was terminated. termination_notified An instance termination notification was sent when a Spot Instance was terminated by Amazon EC2 during scale-down, when the target capacity of the fleet was modified down, for example, from a target capacity of 4 to a target capacity of 3.

#### EC2 Fleet Information EC2 Fleet sends an EC2 Fleet Information event to Amazon EventBridge when there is an error during fulfillment. The information event does not block the fleet from attempting to fulfil its target capacity.
The following is example data for this event.
{ "version": "0", "id": "76529817-d605-4571-7224-d36cc1b2c0c4", "detail-type": "EC2 Fleet Information", "source": "aws.ec2fleet", "account": "123456789012", "time": "2020-11-09T08:17:07Z", "region": "us-east-1", "resources": [ "arn:aws:ec2:us-east-1:123456789012:fleet/fleet-8becf5fe- bb9e-415d-8f54-3fa5a8628b91"
    ], "detail": { "description": "c4.xlarge, ami-0947d2ba12ee1ff75, Linux/UNIX, us-east-1a, Spot price in either SpotFleetRequestConfigData or SpotFleetLaunchSpecification or LaunchTemplate or LaunchTemplateOverrides is less than Spot market price $0.0619", "sub-type": "launchSpecUnusable"
    } } The possible values for sub-type are: fleetProgressHalted The price in every launch specification is not valid because it is below the Spot price (all the launch specifications have produced launchSpecUnusable events). A launch specification might become valid if the Spot price changes. launchSpecTemporarilyBlacklisted The configuration is not valid and several attempts to launch instances have failed. For more information, see the description of the event. launchSpecUnusable The price in a launch specification is not valid because it is below the Spot price.

registerWithLoadBalancersFailed An attempt to register instances with load balancers failed. For more information, see the description of the event.
#### EC2 Fleet Error EC2 Fleet sends an EC2 Fleet Error event to Amazon EventBridge when there is an error during fulfillment. The error event blocks the fleet from attempting to fulfil its target capacity.
The following is example data for this event.
{ "version": "0", "id": "69849a22-6d0f-d4ce-602b-b47c1c98240e", "detail-type": "EC2 Fleet Error", "source": "aws.ec2fleet", "account": "123456789012", "time": "2020-10-07T01:44:24Z", "region": "us-east-1", "resources": [ "arn:aws:ec2:us-east-1:123456789012:fleet/fleet-9bb19bc6-60d3-4fd2-ae47- d33e68eafa08"
    ], "detail": { "description": "m3.large, ami-00068cd7555f543d5, Linux/UNIX: IPv6 is not supported for the instance type 'm3.large'. ", "sub-type": "spotFleetRequestConfigurationInvalid"
    } } The possible values for sub-type are: iamFleetRoleInvalid The EC2 Fleet does not have the required permissions to either launch or terminate an instance. allLaunchSpecsTemporarilyBlacklisted None of the configurations are valid, and several attempts to launch instances have failed. For more information, see the description of the event.

spotInstanceCountLimitExceeded You've reached the limit on the number of Spot Instances that you can launch. spotFleetRequestConfigurationInvalid The configuration is not valid. For more information, see the description of the event.
### Spot Fleet event types There are five Spot Fleet event types. For each event type, there are several sub-types.
Event types
- EC2 Spot Fleet State Change
- EC2 Spot Fleet Spot Instance Request Change
- EC2 Spot Fleet Instance Change
- EC2 Spot Fleet Information
- EC2 Spot Fleet Error
#### EC2 Spot Fleet State Change Spot Fleet sends an EC2 Spot Fleet State Change event to Amazon EventBridge when a Spot Fleet changes state.
The following is example data for this event.
{ "version": "0", "id": "d1af1091-6cc3-2e24-203a-3b870e455d5b", "detail-type": "EC2 Spot Fleet State Change", "source": "aws.ec2spotfleet", "account": "123456789012", "time": "2020-11-09T08:57:06Z", "region": "us-east-1", "resources": [ "arn:aws:ec2:us-east-1:123456789012:spot-fleet-request/sfr-4b6d274d-0cea-4b2c- b3be-9dc627ad1f55"
    ], "detail": { "sub-type": "submitted"

    } } The possible values for sub-type are: active The Spot Fleet request has been validated and Amazon EC2 is attempting to maintain the target number of running instances. cancelled The Spot Fleet request is canceled and has no running instances. The Spot Fleet will be deleted two days after its instances are terminated. cancelled_running The Spot Fleet request is canceled and does not launch additional instances. Its existing instances continue to run until they are interrupted or terminated. The request remains in this state until all instances are interrupted or terminated. cancelled_terminating The Spot Fleet request is canceled and its instances are terminating. The request remains in this state until all instances are terminated. expired The Spot Fleet request has expired. If the request was created with TerminateInstancesWithExpiration set, a subsequent terminated event indicates that the instances are terminated. modify_in_progress The Spot Fleet request is being modified. The request remains in this state until the modification is fully processed. modify_succeeded The Spot Fleet request was modified. submitted The Spot Fleet request is being evaluated and Amazon EC2 is preparing to launch the target number of instances.

progress The Spot Fleet request is in the process of being fulfilled.
#### EC2 Spot Fleet Spot Instance Request Change Spot Fleet sends an EC2 Spot Fleet Spot Instance Request Change event to Amazon EventBridge when a Spot Instance request in the fleet changes state.
The following is example data for this event.
{ "version": "0", "id": "cd141ef0-14af-d670-a71d-fe46e9971bd2", "detail-type": "EC2 Spot Fleet Spot Instance Request Change", "source": "aws.ec2spotfleet", "account": "123456789012", "time": "2020-11-09T08:53:21Z", "region": "us-east-1", "resources": [ "arn:aws:ec2:us-east-1:123456789012:spot-fleet-request/sfr- a98d2133-941a-47dc-8b03-0f94c6852ad1"
    ], "detail": { "spot-instance-request-id": "sir-a2w9gc5h", "description": "SpotInstanceRequestId sir-a2w9gc5h, PreviousState: cancelled_running", "sub-type": "cancelled"
    } } The possible values for sub-type are: active The Spot Instance request is fulfilled and has an associated Spot Instance. cancelled You cancelled the Spot Instance request, or the Spot Instance request expired. disabled You stopped the Spot Instance.

submitted The Spot Instance request is submitted.
#### EC2 Spot Fleet Instance Change Spot Fleet sends an EC2 Spot Fleet Instance Change event to Amazon EventBridge when an instance in the fleet changes state.
The following is example data for this event.
{ "version": "0", "id": "11591686-5bd7-bbaa-eb40-d46529c2710f", "detail-type": "EC2 Spot Fleet Instance Change", "source": "aws.ec2spotfleet", "account": "123456789012", "time": "2020-11-09T07:25:02Z", "region": "us-east-1", "resources": [ "arn:aws:ec2:us-east-1:123456789012:spot-fleet-request/sfr-c8a764a4-bedc-4b62- af9c-0095e6e3ba61"
    ], "detail": { "instance-id": "i-08b90df1e09c30c9b", "description": "{\"instanceType\":\"r4.2xlarge\",\"image\":
\"ami-032930428bf1abbff\",\"productDescription\":\"Linux/UNIX\",\"availabilityZone\":
\"us-east-1a\"}", "sub-type": "launched"
    } } The possible values for sub-type are: launched A new instance was launched. terminated The instance was terminated.

termination_notified An instance termination notification was sent when a Spot Instance was terminated by Amazon EC2 during scale-down, when the target capacity of the fleet was modified down, for example, from a target capacity of 4 to a target capacity of 3.
#### EC2 Spot Fleet Information Spot Fleet sends an EC2 Spot Fleet Information event to Amazon EventBridge when there is an error during fulfillment. The information event does not block the fleet from attempting to fulfil its target capacity.
The following is example data for this event.
{ "version": "0", "id": "73a60f70-3409-a66c-635c-7f66c5f5b669", "detail-type": "EC2 Spot Fleet Information", "source": "aws.ec2spotfleet", "account": "123456789012", "time": "2020-11-08T20:56:12Z", "region": "us-east-1", "resources": [ "arn:aws:ec2:us-east-1:123456789012:spot-fleet-request/sfr-2531ea06- af18-4647-8757-7d69c94971b1"
    ], "detail": { "description": "r3.8xlarge, ami-032930428bf1abbff, Linux/UNIX, us-east-1a, Spot bid price is less than Spot market price $0.5291", "sub-type": "launchSpecUnusable"
    } } The possible values for sub-type are: fleetProgressHalted The price in every launch specification is not valid because it is below the Spot price (all the launch specifications have produced launchSpecUnusable events). A launch specification might become valid if the Spot price changes.

launchSpecTemporarilyBlacklisted The configuration is not valid and several attempts to launch instances have failed. For more information, see the description of the event. launchSpecUnusable The price in a launch specification is not valid because it is below the Spot price. registerWithLoadBalancersFailed An attempt to register instances with load balancers failed. For more information, see the description of the event.
#### EC2 Spot Fleet Error Spot Fleet sends an EC2 Spot Fleet Error event to Amazon EventBridge when there is an error during fulfillment. The error event blocks the fleet from attempting to fulfil its target capacity.
The following is example data for this event.
{ "version": "0", "id": "10adc4e7-675c-643e-125c-5bfa1b1ba5d2", "detail-type": "EC2 Spot Fleet Error", "source": "aws.ec2spotfleet", "account": "123456789012", "time": "2020-11-09T06:56:07Z", "region": "us-east-1", "resources": [ "arn:aws:ec2:us-east-1:123456789012:spot-fleet-request/ sfr-38725d30-25f1-4f30-83ce-2907c56dba17"
    ], "detail": { "description": "r4.2xlarge, ami-032930428bf1abbff, Linux/UNIX: The associatePublicIPAddress parameter can only be specified for the network interface with DeviceIndex 0. ", "sub-type": "spotFleetRequestConfigurationInvalid"
    } } The possible values for sub-type are:
