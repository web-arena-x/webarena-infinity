# Find an AMI that meets the requirements for your EC2 instance

Source: apps/user-manuals/aws/ec2-ug.pdf

---

Characteristic HVM PV access to the native hardware platform, and HVM virtualiz ation provides this access.
For more information, see Enhanced networking on Amazon EC2 instances.
How to find Verify that the virtualization type of the AMI is set to hvm, using the console or the describe-images command.
Verify that the virtualization type of the AMI is set to paravirtual , using the console or the describe- images command.
PV on HVM Paravirtual guests traditionally performed better with storage and network operations than HVM guests because they could leverage special drivers for I/O that avoided the overhead of emulating network and disk hardware, whereas HVM guests had to translate these instructions to emulated hardware. Now PV drivers are available for HVM guests, so operating systems that cannot be ported to run in a paravirtualized environment can still see performance advantages in storage and network I/O by using them. With these PV on HVM drivers, HVM guests can get the same, or better, performance than paravirtual guests.
# Find an AMI that meets the requirements for your EC2 instance An AMI includes the components and applications, such as the operating system and type of root volume, required to launch an instance. To launch an instance, you must find an AMI that meets your needs.
When selecting an AMI, consider the following requirements you might have for the instances that you want to launch:
- The AWS Region of the AMI as AMI IDs are unique to each Region.
- The operating system (for example, Linux or Windows).
- The architecture (for example, 32-bit, 64-bit, or 64-bit ARM).

- The root volume type (for example, Amazon EBS or instance store).
- The provider (for example, Amazon Web Services).
- Additional software (for example, SQL Server).
Console You can select from the list of AMIs when you use the launch instance wizard, or you can search all available AMIs using the Images page.
To find a Quick Start AMI using the launch instance wizard
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. From the navigation bar, select the Region in which to launch your instances. You can select any Region that's available to you, regardless of your location. AMI IDs are unique to each AWS Region.
3. From the console dashboard, choose Launch instance.
4. Under Application and OS Images (Amazon Machine Image), choose Quick Start, choose the operating system (OS) for your instance, and then, from Amazon Machine Image (AMI), select from one of the commonly used AMIs in the list. If you don't see the AMI that you want to use, choose Browse more AMIs to browse the full AMI catalog. For more information, see Application and OS Images (Amazon Machine Image).
To find an AMI using the AMIs page
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. From the navigation bar, select the Region in which to launch your instances. You can select any Region that's available to you, regardless of your location. AMI IDs are unique to each AWS Region.
3. In the navigation pane, choose AMIs.
4. (Optional) Use the filter and search options to scope the list of displayed AMIs to see only the AMIs that match your criteria.
For example, to list all AMIs provided by AWS, choose Public images. Then use the search options to further scope the list of displayed AMIs. Choose the Search bar and, from the menu, choose Owner alias, then the = operator, and then the value amazon. To find AMIs that match a specific platform, for example Linux or Windows, choose the Search bar

again to choose Platform, then the = operator, and then the operating system from the list provided.
5. (Optional) Choose the Preferences icon to select which image attributes to display, such as the root volume type. Alternatively, you can select an AMI from the list and view its properties on the Details tab.
6. Before you select an AMI, it's important that you check whether it's backed by instance store or by Amazon EBS and that you are aware of the effects of this difference. For more information, see Root volume type.
7. To launch an instance from this AMI, select it and then choose Launch instance from image. For more information about launching an instance using the console, see Launch an EC2 instance using the launch instance wizard in the console. If you're not ready to launch the instance now, make note of the AMI ID for later.
AWS CLI Use the describe-images command to find an AMI that meets your requirements. By default, this command returns all AMIs that are public, that you own, and that are shared with you.
To find an AMI owned by Amazon Use the describe-images command with the --owners option. aws ec2 describe-images --owners amazon To find a Windows AMI Add the following filter to display only Windows AMIs.
--filters "Name=platform,Values=windows"
To find an EBS-backed AMI Add the following filter to display only AMIs backed by Amazon EBS.
--filters "Name=root-device-type,Values=ebs"

PowerShell Use the Get-EC2Image cmdlet to find an AMI that meets your requirements. By default, this cmdlet returns all AMIs that are public, that you own, or that are shared with you.
To find an AMI owned by Amazon Use the Get-EC2Image command with the -Owner parameter.
Get-EC2Image -Owner amazon To find a Windows AMI Add the following filter to display only Windows AMIs.
-Filter @{Name="platform"; Values="windows"} For additional examples, see Find an Amazon Machine Image Using Windows PowerShell in the AWS Tools for PowerShell User Guide.
Related resources For more information about AMIs for a specific operating system, see the following:
- Amazon Linux 2023 – AL2023 on Amazon EC2 in the Amazon Linux 2023 User Guide
- Ubuntu – Amazon EC2 AMI Locator on the Canonical Ubuntu website
- RHEL – Red Hat Enterprise Linux Images (AMI) Available on Amazon Web Services (AWS) on the Red Hat website
- Windows Server – AWS Windows AMI reference For information about AMIs that you can subscribe to on the AWS Marketplace see Paid AMIs in the AWS Marketplace for Amazon EC2 instances.
For information about using Systems Manager to help your users find the latest AMI that they should use when launching an instance, see the following:
- Reference AMIs using Systems Manager parameters
- Reference the latest AMIs using Systems Manager public parameters

## Reference AMIs using Systems Manager parameters When you launch an instance using the EC2 launch instance wizard in the Amazon EC2 console, you can either select an AMI from the list, or you can select an AWS Systems Manager parameter that points to an AMI ID (described in this section). If you use automation code to launch your instances, you can specify the Systems Manager parameter instead of the AMI ID.
A Systems Manager parameter is a customer-defined key-value pair that you can create in Systems Manager Parameter Store. The Parameter Store provides a central store to externalize your application configuration values. For more information, see AWS Systems Manager Parameter Store in the AWS Systems Manager User Guide.
When you create a parameter that points to an AMI ID, make sure that you specify the data type as aws:ec2:image. Specifying this data type ensures that when the parameter is created or modified, the parameter value is validated as an AMI ID. For more information, see Native parameter support for Amazon Machine Image IDs in the AWS Systems Manager User Guide.
Contents
- Use cases
- Permissions
- Limitations
- Launch an instance using a Systems Manager parameter
### Use cases When you use Systems Manager parameters to point to AMI IDs, it is easier for your users to select the correct AMI when launching instances. Systems Manager parameters can also simplify the maintenance of automation code.
Easier for users If you require instances to be launched using a specific AMI, and the AMI is regularly updated, we recommend that you require your users to select a Systems Manager parameter to find the AMI.
Requiring your users to select a Systems Manager parameter ensures that the latest AMI is used to launch instances.
For example, every month in your organization you might create a new version of your AMI that has the latest operating system and application patches. You also require your users to launch

instances using the latest version of your AMI. To ensure that your users use the latest version, you can create a Systems Manager parameter (for example, golden-ami) that points to the correct AMI ID. Each time a new version of the AMI is created, you update the AMI ID value in the parameter so that it always points to the latest AMI. Your users don't have to know about the periodic updates to the AMI because they continue to select the same Systems Manager parameter each time. Using a Systems Manager parameter for your AMI makes it easier for them to select the correct AMI for an instance launch.
Simplify automation code maintenance If you use automation code to launch your instances, you can specify the Systems Manager parameter instead of the AMI ID. If a new version of the AMI is created, you can change the AMI ID value in the parameter so that it points to the latest AMI. The automation code that references the parameter doesn't have to be modified each time a new version of the AMI is created. This simplifies the maintenance of the automation and helps to drive down deployment costs.
Note Running instances are not affected when you change the AMI ID pointed to by the Systems Manager parameter.
### Permissions If you use Systems Manager parameters that point to AMI IDs in the launch instance wizard, you must add the following permissions to your IAM policy:
- ssm:DescribeParameters – Grants permission to view and select Systems Manager parameters.
- ssm:GetParameters – Grants permission to retrieve the values of the Systems Manager parameters.
You can also restrict access to specific Systems Manager parameters. For more information and example IAM policies, see Example: Use the EC2 launch instance wizard.
### Limitations AMIs and Systems Manager parameters are Region specific. To use the same Systems Manager parameter name across Regions, create a Systems Manager parameter in each Region with the

same name (for example, golden-ami). In each Region, point the Systems Manager parameter to an AMI in that Region.
Parameter names are case-sensitive. Backslashes for the parameter name are only necessary when the parameter is part of a hierarchy, for example, /amis/production/golden-ami. You can omit the backslash if the parameter is not part of a hierarchy.
### Launch an instance using a Systems Manager parameter When you launch an instance, instead of specifying an AMI ID, you can specify a Systems Manager parameter that points to an AMI ID.
To specify the parameter programmatically, use the following syntax, where resolve:ssm is the standard prefix and parameter-name is the unique parameter name. resolve:ssm:parameter-name Systems Manager parameters have version support. Each iteration of a parameter is assigned a unique version number. You can reference the version of the parameter as follows, where version is the unique version number. By default, the latest version of the parameter is used when no version is specified. resolve:ssm:parameter-name:version To launch an instance using a public parameter provided by AWS, see Reference the latest AMIs using Systems Manager public parameters.
Console To find an AMI using a Systems Manager parameter
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. From the navigation bar, select the Region in which to launch your instances. You can select any Region that's available to you, regardless of your location.
3. From the console dashboard, choose Launch instance.
4. Under Application and OS Images (Amazon Machine Image), choose Browse more AMIs.
5. Choose the arrow button to the right of the search bar, and then choose Search by Systems Manager parameter.

6. For Systems Manager parameter, select a parameter. The corresponding AMI ID appears below Currently resolves to.
7. Choose Search. The AMIs that match the AMI ID appear in the list.
8. Select the AMI from the list, and choose Select.
For more information about launching an instance using the launch instance wizard, see Launch an EC2 instance using the launch instance wizard in the console.
AWS CLI To launch an instance using a Systems Manager parameter Use the run-instances command with the --image-id option. This example uses a Systems Manager parameter named golden-ami, which specifies an AMI ID.
--image-id resolve:ssm:/golden-ami You can create versions of a Systems Manager parameter. The following example specifies version 2 of the golden-ami parameter.
--image-id resolve:ssm:/golden-ami:2 PowerShell To launch an instance using a Systems Manager parameter Use the New-EC2Instance cmdlet with the -ImageId parameter. This example uses a Systems Manager parameter named golden-ami, which specifies an AMI ID.
-ImageId "resolve:ssm:/golden-ami"
You can create versions of a Systems Manager parameter. The following example specifies version 2 of the golden-ami parameter.
-ImageId "resolve:ssm:/golden-ami:2"

## Reference the latest AMIs using Systems Manager public parameters AWS Systems Manager provides public parameters for public AMIs maintained by AWS. You can use the public parameters when launching instances to ensure that you're using the latest AMIs.
For example, the public parameter /aws/service/ami-amazon-linux-latest/al2023-ami- kernel-default-arm64 is available in all Regions and always points to the latest version of the Amazon Linux 2023 AMI for arm64 architecture in a given Region.
The public parameters are available from the following paths:
- Linux – /aws/service/ami-amazon-linux-latest
- Windows – /aws/service/ami-windows-latest For more information, see Working with public parameters in the AWS Systems Manager User Guide.
### List the Amazon Linux AMIs AWS CLI To list the Linux AMIs in the current AWS Region Use the following get-parameters-by-path command. The value for the --path parameter is specific to Linux AMIs. aws ssm get-parameters-by-path \ --path /aws/service/ami-amazon-linux-latest \ --query "Parameters[].Name"
PowerShell To list the Linux AMIs in the current AWS Region Use the Get-SSMParametersByPath cmdlet.
Get-SSMParametersByPath `
    -Path "/aws/service/ami-amazon-linux-latest" | `
    Sort-Object Name | Format-Table Name

### List the Windows AMIs AWS CLI To list the Windows AMIs in the current AWS Region Use the following get-parameters-by-path command. The value for the --path parameter is specific to Windows AMIs. aws ssm get-parameters-by-path \ --path /aws/service/ami-windows-latest \ --query "Parameters[].Name"
PowerShell To list the Windows AMIs in the current AWS Region Use the Get-SSMParametersByPath cmdlet.
Get-SSMParametersByPath `
    -Path "/aws/service/ami-windows-latest" | `
    Sort-Object Name | Format-Table Name
### Launch an instance using a public parameter To specify the public parameter when launching an instance, use the following syntax: resolve:ssm:public-parameter, where resolve:ssm is the standard prefix and public- parameter is the path and name of the public parameter.
AWS CLI To launch an instance using a public parameter Use the run-instances command with the --image-id option. This example specifies a Systems Manager public parameter for the image ID to launch an instance using the latest Amazon Linux 2023 AMI --image-id resolve:ssm:/aws/service/ami-amazon-linux-latest/al2023-ami-kernel- default-x86_64
