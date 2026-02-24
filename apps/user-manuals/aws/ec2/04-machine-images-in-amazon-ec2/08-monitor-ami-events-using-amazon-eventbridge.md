# Monitor AMI events using Amazon EventBridge

Source: apps/user-manuals/aws/ec2-ug.pdf

---

find that ~/.bash_history has been re-created and contains all of the commands you ran during your previous session.
Other programs besides bash also write histories to disk, Use caution and remove or exclude unnecessary dot-files and dot-directories.
- Bundling a running instance requires your private key and X.509 certificate. Put these and other credentials in a location that is not bundled (such as the instance store).
# Monitor AMI events using Amazon EventBridge When the state of an Amazon Machine Image (AMI) changes, Amazon EC2 generates an event that is sent to Amazon EventBridge (formerly known as Amazon CloudWatch Events). The events are sent to the default EventBridge event bus in JSON format. You can use Amazon EventBridge to detect and react to these events. You do this by creating rules in EventBridge that trigger an action in response to an event. For example, you can create an EventBridge rule that detects when the AMI creation process has completed and then invokes an Amazon SNS topic to send an email notification to you.
Amazon EC2 generates an EC2 AMI State Change event when an AMI enters any of the following states:
- available
- failed
- deregistered
- disabled Events are generated on a best effort basis.
The following table lists the AMI operations and the states that an AMI can enter. In the table, Yes indicates the states that the AMI can enter when the corresponding operation runs.
AMI operations available failed deregistered disabled CopyImage Yes Yes


CreateImage Yes Yes


AMI operations available failed deregistered disabled CreateRes toreImageTask Yes Yes


DeregisterImage


Yes

DisableImage


Yes EnableImage Yes


RegisterImage Yes Yes


EC2 AMI State Change events
- Event details
- available events
- failed events
- deregistered events
- disabled events
## Event details You can use the following fields in the event to create rules that trigger an action:
"source": "aws.ec2"
Identifies that the event is from Amazon EC2.
"detail-type": "EC2 AMI State Change"
Identifies the event name.
"detail": { "ImageId": "ami-0abcdef1234567890", "State": "available", } Provides the AMI ID and the state of the AMI (available, failed, deregistered, or disabled).
For more information, see the following in the Amazon EventBridge User Guide:

- Amazon EventBridge events
- Amazon EventBridge event patterns
- Amazon EventBridge rules For a tutorial about how to create a Lambda function and an EventBridge rule that runs the Lambda function, see Tutorial: Log the state of an Amazon EC2 instance using EventBridge in the AWS Lambda Developer Guide.
## available events The following is an example of an event that Amazon EC2 generates when the AMI enters the available state following a successful CreateImage, CopyImage, RegisterImage, CreateRestoreImageTask, or EnableImage operation.
"State": "available" indicates that the operation was successful.
{ "version": "0", "id": "example-9f07-51db-246b-d8b8441bcdf0", "detail-type": "EC2 AMI State Change", "source": "aws.ec2", "account": "012345678901", "time": "yyyy-mm-ddThh:mm:ssZ", "region": "us-east-1", "resources": ["arn:aws:ec2:us-east-1::image/ami-0abcdef1234567890"], "detail": { "RequestId": "example-9dcc-40a6-aa77-7ce457d5442b", "ImageId": "ami-0abcdef1234567890", "State": "available", "ErrorMessage": ""
    } }
## failed events The following is an example of an event that Amazon EC2 generates when the AMI enters the failed state following a failed CreateImage, CopyImage, RegisterImage, or CreateRestoreImageTask operation.
The following fields provide pertinent information:

- "State": "failed" – Indicates that the operation failed.
- "ErrorMessage": "" – Provides the reason for the failed operation.
{ "version": "0", "id": "example-9f07-51db-246b-d8b8441bcdf0", "detail-type": "EC2 AMI State Change", "source": "aws.ec2", "account": "012345678901", "time": "yyyy-mm-ddThh:mm:ssZ", "region": "us-east-1", "resources": ["arn:aws:ec2:us-east-1::image/ami-0abcdef1234567890"], "detail": { "RequestId": "example-9dcc-40a6-aa77-7ce457d5442b", "ImageId": "ami-0abcdef1234567890", "State": "failed", "ErrorMessage": "Description of failure"
    } }
## deregistered events The following is an example of an event that Amazon EC2 generates when the AMI enters the deregistered state following a successful DeregisterImage operation. If the operation fails, no event is generated. Any failure is known immediately because DeregisterImage is a synchronous operation.
"State": "deregistered" indicates that the DeregisterImage operation was successful.
{ "version": "0", "id": "example-9f07-51db-246b-d8b8441bcdf0", "detail-type": "EC2 AMI State Change", "source": "aws.ec2", "account": "012345678901", "time": "yyyy-mm-ddThh:mm:ssZ", "region": "us-east-1", "resources": ["arn:aws:ec2:us-east-1::image/ami-0abcdef1234567890"], "detail": { "RequestId": "example-9dcc-40a6-aa77-7ce457d5442b", "ImageId": "ami-0abcdef1234567890",
