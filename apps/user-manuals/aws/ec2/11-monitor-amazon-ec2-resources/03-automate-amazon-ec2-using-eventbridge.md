# Automate Amazon EC2 using EventBridge

Source: apps/user-manuals/aws/ec2-ug.pdf

---

Setting Value 7 5 Minutes
# Automate Amazon EC2 using EventBridge You can use Amazon EventBridge to automate your AWS services and respond automatically to system events, such as application availability issues or resource changes. Events from AWS services are delivered to EventBridge in near real time. You can create rules to indicate which events you're interested in, and the actions to take when an event matches a rule. The actions that can be automatically triggered include the following:
- Invoke an AWS Lambda function
- Invoke Amazon EC2 Run Command
- Relay the event to Amazon Kinesis Data Streams
- Activate an AWS Step Functions state machine
- Notify an Amazon SNS topic
- Notify an Amazon SQS queue The following are examples of how you can use EventBridge with Amazon EC2:
- Activate a Lambda function whenever an instance enters the running state.
- Notify an Amazon SNS topic when an Amazon EBS volume is created or modified.
- Send a command to one or more Amazon EC2 instances using Amazon EC2 Run Command whenever a certain event in another AWS service occurs.
For more information, see the Amazon EventBridge User Guide.
## Amazon EC2 event types Amazon EC2 supports the following event types:
- EC2 AMI State Change
- EC2 Fast Launch State-change Notification
