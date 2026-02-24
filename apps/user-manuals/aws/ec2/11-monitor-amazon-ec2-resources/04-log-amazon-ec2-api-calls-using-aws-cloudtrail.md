# Log Amazon EC2 API calls using AWS CloudTrail

Source: apps/user-manuals/aws/ec2-ug.pdf

---

- EC2 Fleet Error
- EC2 Fleet Information
- EC2 Fleet Instance Change
- EC2 Fleet Spot Instance Request Change
- EC2 Fleet State Change
- EC2 Instance Rebalance Recommendation
- EC2 Instance State-change Notification
- EC2 Spot Fleet Error
- EC2 Spot Fleet Information
- EC2 Spot Fleet Instance Change
- EC2 Spot Fleet Spot Instance Request Change
- EC2 Spot Fleet State Change
- EC2 Spot Instance Interruption Warning
- EC2 Spot Instance Request Fulfillment
- EC2 ODCR Underutilization Notification For information about the event types supported by Amazon EBS, see Amazon EventBridge for Amazon EBS.
# Log Amazon EC2 API calls using AWS CloudTrail The Amazon EC2 API is integrated with AWS CloudTrail, a service that provides a record of actions taken by a user, role, or an AWS service. CloudTrail captures all Amazon EC2 API calls as events. The calls captured include calls made by the console. Using the information collected by CloudTrail, you can determine the request that was made to the Amazon EC2 API, the IP address from which the request was made, and when it was made.
Every event or log entry contains information about who generated the request. The identity information helps you determine the following:
- Whether the request was made with root user or user credentials.
- Whether the request was made on behalf of an IAM Identity Center user.
- Whether the request was made with temporary security credentials for a role or federated user.

- Whether the request was made by another AWS service.
CloudTrail is active in your AWS account when you create the account and you automatically have access to the CloudTrail Event history. The CloudTrail Event history provides a viewable, searchable, downloadable, and immutable record of the past 90 days of recorded management events in an AWS Region. For more information, see Working with CloudTrail Event history in the AWS CloudTrail User Guide. There are no CloudTrail charges for viewing the Event history.
For an ongoing record of events in your AWS account past 90 days, create a trail or a CloudTrail Lake event data store.
CloudTrail trails A trail enables CloudTrail to deliver log files to an Amazon S3 bucket. All trails created using the AWS Management Console are multi-Region. You can create a single-Region or a multi-Region trail by using the AWS CLI. Creating a multi-Region trail is recommended because you capture activity in all AWS Regions in your account. If you create a single-Region trail, you can view only the events logged in the trail's AWS Region. For more information about trails, see Creating a trail for your AWS account and Creating a trail for an organization in the AWS CloudTrail User Guide.
You can deliver one copy of your ongoing management events to your Amazon S3 bucket at no charge from CloudTrail by creating a trail, however, there are Amazon S3 storage charges. For more information about CloudTrail pricing, see AWS CloudTrail Pricing. For information about Amazon S3 pricing, see Amazon S3 Pricing.
CloudTrail Lake event data stores CloudTrail Lake lets you run SQL-based queries on your events. CloudTrail Lake converts existing events in row-based JSON format to  Apache ORC format. ORC is a columnar storage format that is optimized for fast retrieval of data. Events are aggregated into event data stores, which are immutable collections of events based on criteria that you select by applying advanced event selectors. The selectors that you apply to an event data store control which events persist and are available for you to query. For more information about CloudTrail Lake, see Working with AWS CloudTrail Lake in the AWS CloudTrail User Guide.
CloudTrail Lake event data stores and queries incur costs. When you create an event data store, you choose the pricing option you want to use for the event data store. The pricing option determines the cost for ingesting and storing events, and the default and maximum

retention period for the event data store. For more information about CloudTrail pricing, see AWS CloudTrail Pricing.
## Amazon EC2 API management events in CloudTrail Management events provide information about management operations that are performed on resources in your AWS account. These are also known as control plane operations. By default, CloudTrail logs management events.
All Amazon EC2 API actions are logged as management events. For a list of the API actions that are logged to CloudTrail, see the Amazon EC2 API Reference. For example, calls to the RunInstances, DescribeInstances, and StopInstances actions are logged as management events.
## Amazon EC2 API event examples An event represents a single request from any source and includes information about the requested API operation, the date and time of the operation, request parameters, and so on. CloudTrail log files aren't an ordered stack trace of the public API calls, so events don't appear in any specific order.
The following log file record shows that a user terminated an instance.
{ "Records":[ { "eventVersion":"1.03", "userIdentity":{ "type":"Root", "principalId":"123456789012", "arn":"arn:aws:iam::123456789012:root", "accountId":"123456789012", "accessKeyId":"AKIAIOSFODNN7EXAMPLE", "userName":"user"
         }, "eventTime":"2016-05-20T08:27:45Z", "eventSource":"ec2.amazonaws.com", "eventName":"TerminateInstances", "awsRegion":"us-west-2", "sourceIPAddress":"198.51.100.1", "userAgent":"aws-cli/1.10.10 Python/2.7.9 Windows/7botocore/1.4.1", "requestParameters":{

            "instancesSet":{ "items":[{ "instanceId":"i-1a2b3c4d"
               }]
            } }, "responseElements":{ "instancesSet":{ "items":[{ "instanceId":"i-1a2b3c4d", "currentState":{ "code":32, "name":"shutting-down"
                  }, "previousState":{ "code":16, "name":"running"
                  } }]
            } }, "requestID":"be112233-1ba5-4ae0-8e2b-1c302EXAMPLE", "eventID":"6e12345-2a4e-417c-aa78-7594fEXAMPLE", "eventType":"AwsApiCall", "recipientAccountId":"123456789012"
     } ]
} For information about CloudTrail record contents, see CloudTrail record contents in the AWS CloudTrail User Guide.
## Audit connections made using EC2 Instance Connect You can use AWS CloudTrail to audit the users that connect to your instances using EC2 Instance Connect.
To audit SSH activity via EC2 Instance Connect using the AWS CloudTrail console
1. Open the CloudTrail console at https://console.aws.amazon.com/cloudtrail/.
2. Verify that you are in the correct Region.
3. In the navigation pane, choose Event history.

4. For Filter, choose Event source, ec2-instance-connect.amazonaws.com.
5. (Optional) For Time range, select a time range.
6. Choose the Refresh events icon.
7. The page displays the events that correspond to the SendSSHPublicKey API calls. Expand an event using the arrow to view additional details, such as the user name and AWS access key that was used to make the SSH connection, and the source IP address.
8. To display the full event information in JSON format, choose View event. The requestParameters field contains the destination instance ID, OS username, and public key that were used to make the SSH connection.
{ "eventVersion": "1.05", "userIdentity": { "type": "IAMUser", "principalId": "ABCDEFGONGNOMOOCB6XYTQEXAMPLE", "arn": "arn:aws:iam::1234567890120:user/IAM-friendly-name", "accountId": "123456789012", "accessKeyId": "ABCDEFGUKZHNAW4OSN2AEXAMPLE", "userName": "IAM-friendly-name", "sessionContext": { "attributes": { "mfaAuthenticated": "false", "creationDate": "2018-09-21T21:37:58Z"} } }, "eventTime": "2018-09-21T21:38:00Z", "eventSource": "ec2-instance-connect.amazonaws.com", "eventName": "SendSSHPublicKey ", "awsRegion": "us-west-2", "sourceIPAddress": "123.456.789.012", "userAgent": "aws-cli/1.15.61 Python/2.7.10 Darwin/16.7.0 botocore/1.10.60", "requestParameters": { "instanceId": "i-0123456789EXAMPLE", "osUser": "ec2-user", "SSHKey": { "publicKey": "ssh-rsa ABCDEFGHIJKLMNO01234567890EXAMPLE"
        } }, "responseElements": null, "requestID": "1a2s3d4f-bde6-11e8-a892-f7ec64543add", "eventID": "1a2w3d4r5-a88f-4e28-b3bf-30161f75be34",
