# Understand AMI billing information

Source: apps/user-manuals/aws/ec2-ug.pdf

---

        "State": "deregistered", "ErrorMessage": ""
    } }
## disabled events The following is an example of an event that Amazon EC2 generates when the AMI enters the disabled state following a successful DisableImage operation. If the operation fails, no event is generated. Any failure is known immediately because DisableImage is a synchronous operation.
"State": "disabled" indicates that the DisableImage operation was successful.
{ "version": "0", "id": "example-9f07-51db-246b-d8b8441bcdf0", "detail-type": "EC2 AMI State Change", "source": "aws.ec2", "account": "012345678901", "time": "yyyy-mm-ddThh:mm:ssZ", "region": "us-east-1", "resources": ["arn:aws:ec2:us-east-1::image/ami-0abcdef1234567890"], "detail": { "RequestId": "example-9dcc-40a6-aa77-7ce457d5442b", "ImageId": "ami-0abcdef1234567890", "State": "disabled", "ErrorMessage": ""
    } }
# Understand AMI billing information There are many Amazon Machine Images (AMIs) to choose from when launching your instances, and they support a variety of operating system platforms and features. To understand how the AMI you choose when launching your instance affects the bottom line on your AWS bill, you can research the associated operating system platform and billing information. Do this before you launch any On-Demand or Spot Instances, or purchase a Reserved Instance.
Here are two examples of how researching your AMI in advance can help you choose the AMI that best suits your needs:

- For Spot Instances, you can use the AMI Platform details to confirm that the AMI is supported for Spot Instances.
- When purchasing a Reserved Instance, you can make sure that you select the operating system platform (Platform) that maps to the AMI Platform details.
For more information about instance pricing, see Amazon EC2 pricing.
Contents
- AMI billing information fields
- Finding AMI billing and usage details
- Verify AMI charges on your bill
## AMI billing information fields The following fields provide billing information associated with an AMI:
Platform details The platform details associated with the billing code of the AMI. For example, Red Hat Enterprise Linux.
Usage operation The operation of the Amazon EC2 instance and the billing code that is associated with the AMI.
For example, RunInstances:0010. Usage operation corresponds to the lineitem/Operation column on your AWS Cost and Usage Report (CUR) and in the AWS Price List API.
You can view these fields on the Instances or AMIs page in the Amazon EC2 console, or in the response that is returned by the describe-images or Get-EC2Image command.
### Sample data: usage operation by platform The following table lists some of the platform details and usage operation values that can be displayed on the Instances or AMIs pages in the Amazon EC2 console, or in the response that is returned by the describe-images or Get-EC2Image command.
Platform details Usage operation 2

Platform details Usage operation 2 Linux/UNIX RunInstances Red Hat BYOL Linux RunInstances:00g0 3 Red Hat Enterprise Linux RunInstances:0010 Red Hat Enterprise Linux with HA RunInstances:1010 Red Hat Enterprise Linux with SQL Server Standard and HA RunInstances:1014 Red Hat Enterprise Linux with SQL Server Enterprise and HA RunInstances:1110 Red Hat Enterprise Linux with SQL Server Standard RunInstances:0014 Red Hat Enterprise Linux with SQL Server Web RunInstances:0210 Red Hat Enterprise Linux with SQL Server Enterprise RunInstances:0110 SQL Server Enterprise RunInstances:0100 SQL Server Standard RunInstances:0004 SQL Server Web RunInstances:0200 SUSE Linux RunInstances:000g Ubuntu Pro RunInstances:0g00 Windows RunInstances:0002

Platform details Usage operation 2 Windows BYOL RunInstances:0800 Windows with SQL Server Enterprise 1 RunInstances:0102 Windows with SQL Server Standard 1 RunInstances:0006 Windows with SQL Server Web 1 RunInstances:0202 1 If two software licenses are associated with an AMI, the Platform details field shows both.
2 If you are running Spot Instances, the lineitem/Operation on your AWS Cost and Usage Report might be different from the Usage operation value that is listed here. For example, if lineitem/ Operation displays RunInstances:0010:SV006, it means that Amazon EC2 is running Red Hat Enterprise Linux Spot Instance-hour in US East (N. Virginia) in Zone 6.
3 This appears as RunInstances (Linux/UNIX) in your usage reports.
## Finding AMI billing and usage details The following properties can help you verify AMI charges on your bill:
- Platform details
- Usage operation
- AMI ID Console To find the AMI billing information for an AMI
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose AMIs.
3. Select the AMI.
4. On the Details tab, find Platform details and Usage operation.

To find the AMI billing information for an instance
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Instances.
3. Select the instance.
4. On the Details tab, expand Instance details and find Platform details and Usage operation.
AWS CLI To find the AMI billing information for an AMI Use the describe-images command. aws ec2 describe-images \ --image-ids ami-0abcdef1234567890 \ --query "Images[].
{PlatformDetails:PlatformDetails,UsageOperation:UsageOperation}"
The following is example output for a Linux AMI.
[ { "PlatformDetails": "Linux/UNIX", "UsageOperation": "RunInstances"
    } ]
To find the AMI billing information for an instance Use the describe-instances command. aws ec2 describe-instances \ --instance-ids i-1234567890abcdef0 \ --query "Reservations[].Instances[].
{PlatformDetails:PlatformDetails,UsageOperation:UsageOperation}"
The following is example output for a Windows instance.
[

    { "PlatformDetails": "Windows", "UsageOperation": "RunInstances:0002"
    } ]
PowerShell To find the AMI billing information for an AMI Use the Get-EC2Image cmdlet.
Get-EC2Image `
    -ImageId ami-0abcdef1234567890 | `
    Format-List PlatformDetails, UsageOperation The following is example output for a Linux AMI.
PlatformDetails : Linux/UNIX UsageOperation  : RunInstances To find the AMI billing information for an instance Use the Get-EC2Instance cmdlet.
(Get-EC2Instance `
    -InstanceId i-1234567890abcdef0).Instances | `
    Format-List PlatformDetails, UsageOperation The following is example output for a Windows instance.
PlatformDetails : Windows UsageOperation  : RunInstances:0002
## Verify AMI charges on your bill To ensure that you're not incurring unplanned costs, you can verify that the billing information for an instance in your AWS Cost and Usage Report (CUR) matches the billing information that's associated with the AMI that you used to launch the instance.
