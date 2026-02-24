# Troubleshoot Amazon EC2 instance launch issues

Source: apps/user-manuals/aws/ec2-ug.pdf

---

Troubleshoot issues with Amazon EC2 instances The following procedures and tips can help you troubleshoot issues with your Amazon EC2 instances.
Issues
- Troubleshoot Amazon EC2 instance launch issues
- Troubleshoot Amazon EC2 instance stop issues
- Troubleshoot Amazon EC2 instance termination issues
- Troubleshoot an unreachable Amazon EC2 instance
- Troubleshoot issues connecting to your Amazon EC2 Linux instance
- Troubleshoot Amazon EC2 Linux instances with failed status checks
- Troubleshoot an Amazon EC2 Linux instance booting from wrong volume
- Troubleshoot issues connecting to your Amazon EC2 Windows instance
- Troubleshoot Amazon EC2 Windows instance start issues
- Troubleshoot issues with Amazon EC2 Windows instances
- Reset the Windows administrator password for an Amazon EC2 Windows instance
- Troubleshoot Sysprep issues with Amazon EC2 Windows instances
- Troubleshoot impaired Amazon EC2 Linux instance using EC2Rescue
- Troubleshoot impaired Amazon EC2 Windows instance using EC2Rescue
- EC2 Serial Console for instances
- Send a diagnostic interrupt to debug an unreachable Amazon EC2 instance
# Troubleshoot Amazon EC2 instance launch issues The following are troubleshooting tips to help you solve issues when launching an Amazon EC2 instance.
Launch Issues
- Invalid device name
- Instance limit exceeded
- Insufficient instance capacity

- The requested configuration is currently not supported. Please check the documentation for supported configurations.
- Instance terminates immediately
- Insufficient permissions
- High CPU usage shortly after Windows starts (Windows instances only)
## Invalid device name
### Description You get the Invalid device name device_name error when you try to launch a new instance.
### Cause If you get this error when you try to launch an instance, the device name specified for one or more volumes in the request has an invalid device name. Possible causes include:
- The device name might be in use by the selected AMI.
- The device name might be reserved for root volumes.
- The device name might be used for another volume in the request.
- The device name might not be valid for the operating system.
### Solution To resolve the issue:
- Ensure that the device name is not used in the AMI that you selected. Run the following command to view the device names used by the AMI. aws ec2 describe-images --image-id ami-0abcdef1234567890 --query 'Images[*].BlockDeviceMappings[].DeviceName'
- Ensure that you are not using a device name that is reserved for root volumes. For more information, see Available device names.
- Ensure that each volume specified in your request has a unique device name.
- Ensure that the device names that you specified are in the correct format. For more information, see Available device names.

## Instance limit exceeded
### Description You get the InstanceLimitExceeded error when you try to launch a new instance or restart a stopped instance.
### Cause If you get an InstanceLimitExceeded error when you try to launch a new instance or restart a stopped instance, you have reached the limit on the number of instances that you can launch in a Region. When you create your AWS account, we set default limits on the number of instances you can run on a per-Region basis.
### Solution You can request an instance limit increase on a per-region basis. For more information, see Amazon EC2 service quotas.
## Insufficient instance capacity
### Description You get the InsufficientInstanceCapacity error when you try to launch a new instance or restart a stopped instance.
### Cause If you get this error when you try to launch an instance or restart a stopped instance, AWS does not currently have enough available On-Demand capacity to fulfill your request.
### Solution To resolve the issue, try the following:
- Wait a few minutes and then submit your request again; capacity can shift frequently.
- Submit a new request with a reduced number of instances. For example, if you're making a single request to launch 15 instances, try making 3 requests for 5 instances, or 15 requests for 1 instance instead.
- If you're launching an instance, submit a new request without specifying an Availability Zone.

- If you're launching an instance, submit a new request using a different instance type (which you can resize at a later stage). For more information, see Amazon EC2 instance type changes.
- If you are launching instances into a cluster placement group, you can get an insufficient capacity error.
## The requested configuration is currently not supported. Please check the documentation for supported configurations. the documentation for supported configurations.
### Description You get the Unsupported error when you try to launch a new instance because the instance configuration is not supported.
### Cause The error message provides additional details. For example, an instance type or instance purchasing option might not be supported in the specified Region or Availability Zone.
### Solution Try a different instance configuration. To search for an instance type that meets your requirements, see Find an Amazon EC2 instance type.
## Instance terminates immediately
### Description Your instance goes from the pending state to the terminated state.
### Cause The following are a few reasons why an instance might immediately terminate:
- You've exceeded your EBS volume limits. For more information, see Amazon EBS volume limits for Amazon EC2 instances.
- An EBS snapshot is corrupted.
- The root EBS volume is encrypted and you do not have permissions to access the KMS key for decryption.
The requested configuration is currently not supported. Please check the documentation for supported

- A snapshot specified in the block device mapping for the AMI is encrypted and you do not have permissions to access the KMS key for decryption or you do not have access to the KMS key to encrypt the restored volumes.
- The Amazon S3-backed AMI that you used to launch the instance is missing a required part (an image.part.xx file).
For more information, get the termination reason using one of the following methods.
To get the termination reason using the Amazon EC2 console
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Instances, and select the instance.
3. On the first tab, find the reason next to State transition reason.
To get the termination reason using the AWS CLI
1. Use the describe-instances command and specify the instance ID. aws ec2 describe-instances --instance-id i-1234567890abcdef0
2. Review the JSON response returned by the command and note the values in the StateReason response element.
The following code block shows an example of a StateReason response element.
"StateReason": { "Message": "Client.VolumeLimitExceeded: Volume limit exceeded", "Code": "Server.InternalError"
}, To get the termination reason using AWS CloudTrail For more information, see Viewing events with CloudTrail event history in the AWS CloudTrail User Guide.
### Solution Depending on the termination reason, take one of the following actions:

- Client.VolumeLimitExceeded: Volume limit exceeded — Delete unused volumes. You can submit a request to increase your volume limit.
- Client.InternalError: Client error on launch — Ensure that you have the permissions required to access the AWS KMS keys used to decrypt and encrypt volumes. For more information, see Using key policies in AWS KMS in the AWS Key Management Service Developer Guide.
## Insufficient permissions
### Description You get the "errorMessage": "You are not authorized to perform this operation." error when you try to launch a new instance, and the launch fails.
### Cause If you get this error when you try to launch an instance, you don't have the required IAM permissions to launch the instance.
Possible missing permissions include:
- ec2:RunInstances
- iam:PassRole Other permissions might also be missing. For the list of permissions required to launch an instance, see the example IAM policies under Example: Use the EC2 launch instance wizard and Launch instances (RunInstances).
### Solution To resolve the issue:
- If you are making requests as an IAM user, verify that you have the following permissions:
- ec2:RunInstances with a wildcard resource ("*")
- iam:PassRole with the resource matching the role ARN (for example, arn:aws:iam::999999999999:role/ExampleRoleName)
- If you don't have the preceding permissions, edit the IAM policy associated with the IAM role or user to add the missing required permissions.
