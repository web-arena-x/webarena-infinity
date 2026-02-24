# Access Amazon EC2 using an interface VPC endpoint

Source: apps/user-manuals/aws/ec2-ug.pdf

---

Important You must first reboot the instance to finish applying the policy settings required to enable Credential Guard.
To verify Credential Guard is running
1. Connect to your instance using the Remote Desktop Protocol (RDP). For more information, see the section called "Connect using an RDP client".
2. Within the RDP session to your instance, open the Start menu and search for cmd to start a command prompt.
3. Open System Information by running the following command: msinfo32.exe
4. The Microsoft System Information tool lists the details for VBS configuration. Next to Virtualization-based security Services, confirm that Credential Guard appears as Running.
The following image displays VBS is running as described previously:
# Access Amazon EC2 using an interface VPC endpoint You can improve the security posture of your VPC by creating a private connection between resources in your VPC and the Amazon EC2 API. You can access the Amazon EC2 API as if it were in your VPC, without the use of an internet gateway, NAT device, VPN connection, or Direct Connect connection. EC2 instances in your VPC don't need public IP addresses to access the Amazon EC2 API.
For more information, see Access AWS services through AWS PrivateLink in the AWS PrivateLink Guide.
Contents
- Create an interface VPC endpoint
- Create an endpoint policy

## Create an interface VPC endpoint Create an interface endpoint for Amazon EC2 using the following service name:
- com.amazonaws.region.ec2 — Creates an endpoint for the Amazon EC2 API actions.
For more information, see Access an AWS service using an interface VPC endpoint in the AWS PrivateLink Guide.
## Create an endpoint policy An endpoint policy is an IAM resource that you can attach to your interface endpoint. The default endpoint policy allows full access to the Amazon EC2 API through the interface endpoint. To control the access allowed to the Amazon EC2 API from your VPC, attach a custom endpoint policy to the interface endpoint.
An endpoint policy specifies the following information:
- The principals that can perform actions.
- The actions that can be performed.
- The resource on which the actions can be performed.
Important When a non-default policy is applied to an interface VPC endpoint for Amazon EC2, certain failed API requests, such as those failing from RequestLimitExceeded, might not be logged to AWS CloudTrail or Amazon CloudWatch.
For more information, see  Control access to services using endpoint policies in the AWS PrivateLink Guide.
The following example shows a VPC endpoint policy that denies permission to create unencrypted volumes or to launch instances with unencrypted volumes. The example policy also grants permission to perform all other Amazon EC2 actions.

JSON { "Version":"2012-10-17", "Statement": [ { "Action": "ec2:*", "Effect": "Allow", "Resource": "*", "Principal": "*"
    }, { "Action": [ "ec2:CreateVolume"
        ], "Effect": "Deny", "Resource": "*", "Principal": "*", "Condition": { "Bool": { "ec2:Encrypted": "false"
            } } }, { "Action": [ "ec2:RunInstances"
        ], "Effect": "Deny", "Resource": "*", "Principal": "*", "Condition": { "Bool": { "ec2:Encrypted": "false"
            } } }]
}
