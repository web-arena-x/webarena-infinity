# Paid AMIs in the AWS Marketplace for Amazon EC2 instances

Source: apps/user-manuals/aws/ec2-ug.pdf

---

PowerShell To launch an instance using a public parameter Use the New-EC2Instance cmdlet with the -ImageId parameter. This example specifies a Systems Manager public parameter for the image ID to launch an instance using the latest AMI for Windows Server 2022.
-ImageId "resolve:ssm:/aws/service/ami-windows-latest/Windows_Server-2022-English- Full-Base"
For more examples that use Systems Manager parameters, see Query for the latest Amazon Linux AMI IDs Using AWS Systems Manager Parameter Store and Query for the Latest Windows AMI Using AWS Systems Manager Parameter Store.
# Paid AMIs in the AWS Marketplace for Amazon EC2 instances A paid AMI is an AMI that is listed for sale in the AWS Marketplace. The AWS Marketplace is an online store where you can buy software that runs on AWS, including AMIs that you can use to launch your EC2 instance. The AWS Marketplace AMIs are organized into categories, such as Developer Tools, to enable you to find products to suit your requirements. For more information about AWS Marketplace, see the AWS Marketplace website.
You can purchase AMIs in the AWS Marketplace from a third party, including AMIs that come with service contracts from organizations such as Red Hat. You can also create an AMI and sell it in the AWS Marketplace to other Amazon EC2 users. Building a safe, secure, usable AMI for public consumption is a fairly straightforward process, if you follow a few simple guidelines.
For information about how to create and use shared AMIs, see Understand shared AMI usage in Amazon EC2.
Launching an instance from a paid AMI is the same as launching an instance from any other AMI.
No additional parameters are required. The instance is charged according to the rates set by the owner of the AMI, as well as the standard usage fees for the related web services, for example, the hourly rate for running an m5.small instance type in Amazon EC2. Additional taxes might also apply. The owner of the paid AMI can confirm whether a specific instance was launched using that paid AMI.

Important Amazon DevPay is no longer accepting new sellers or products. AWS Marketplace is now the single, unified e-commerce platform for selling software and services through AWS. For information about how to deploy and sell software from AWS Marketplace, see Selling in AWS Marketplace. AWS Marketplace supports AMIs backed by Amazon EBS.
Contents
- Sell your AMI in the AWS Marketplace
- Find a paid AMI
- Purchase a paid AMI in the AWS Marketplace
- Retrieve the AWS Marketplace product code from your instance
- Use paid support for supported AWS Marketplace offerings
- Bills for paid and supported AMIs
- Manage your AWS Marketplace subscriptions
## Sell your AMI in the AWS Marketplace You can sell your AMI using AWS Marketplace. AWS Marketplace offers an organized shopping experience. Additionally, AWS Marketplace also supports AWS features such as Amazon EBS-backed AMIs, Reserved Instances, and Spot Instances.
For information about how to sell your AMI on the AWS Marketplace, see Selling in AWS Marketplace.
## Find a paid AMI A paid AMI is an Amazon Machine Image (AMI) that is available for purchase. A paid AMI also has a product code. You can find AMIs that are available for purchase in the AWS Marketplace.
Console To find a paid AMI
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.

2. In the navigation pane, choose AMIs.
3. Choose Public images for the first filter.
4. Do one of the following:
- If you know the product code, choose Product code, then =, and then enter the product code.
- If you do not know the product code, in the Search bar, specify the following filter:
Owner alias=aws-marketplace. Specify additional filters as needed.
5. Save the ID of the AMI.
AWS CLI To find a paid AMI Use the following describe-images command. aws ec2 describe-images --owners aws-marketplace The output includes a large number of images. You can specify filters to help you determine which AMI you need. After you find an AMI, specify its ID in the following command to get its product code. aws ec2 describe-images \ --image-ids ami-0abcdef1234567890 \ --query Images[*].ProductCodes[].ProductCodeId The following is example output.
[ "cdef1234abc567def8EXAMPLE"
]
If you know the product code, you can filter the results by product code. This example returns the most recent AMI with the specified product code. aws ec2 describe-images \ --filters "Name=product-code,Values=cdef1234abc567def8EXAMPLE" \

    --query "sort_by(Images, &CreationDate)[-1].[ImageId]"
PowerShell To find a paid AMI Use the Get-EC2Image cmdlet.
Get-EC2Image -Owner aws-marketplace The output includes a large number of images. You can specify filters to help you determine which AMI you need. After you find an AMI, specify its ID in the following command to get its product code.
(Get-EC2Image -ImageId ami-0abcdef1234567890).ProductCodes The following is example output.
ProductCodeId             ProductCodeType -------------             --------------- cdef1234abc567def8EXAMPLE marketplace If you know the product code, you can filter the results by product code. This example returns the most recent AMI with the specified product code.
(Get-EC2Image -Owner aws-marketplace -Filter @{"Name"="product- code";"Value"="cdef1234abc567def8EXAMPLE"} | sort CreationDate -Descending | Select- Object -First 1).ImageId
## Purchase a paid AMI in the AWS Marketplace You must sign up for (purchase) a paid AMI before you can launch an Amazon EC2 instance using the AMI.
Typically a seller of a paid AMI presents you with information about the AMI, including its price and a link where you can buy it. When you click the link, you're first asked to log into AWS, and then you can purchase the AMI.

### Purchase a paid AMI using the console You can purchase a paid AMI by using the Amazon EC2 launch wizard. For more information, see Launch an Amazon EC2 instance from an AWS Marketplace AMI.
### Subscribe to a product using AWS Marketplace To use the AWS Marketplace, you must have an AWS account. To launch instances from AWS Marketplace products, you must be signed up to use the Amazon EC2 service, and you must be subscribed to the product from which to launch the instance. You can use one of the following methods to subscribe to products in the AWS Marketplace:
- AWS Marketplace website: You can launch preconfigured software quickly with the 1-Click deployment feature. For more information, see AMI-based products in AWS Marketplace.
- Amazon EC2 launch wizard: You can search for an AMI and launch an instance directly from the wizard. For more information, see Launch an Amazon EC2 instance from an AWS Marketplace AMI.
## Retrieve the AWS Marketplace product code from your instance You can retrieve the AWS Marketplace product code for your instance using its instance metadata.
If the instance has a product code, Amazon EC2 returns it. For more information about retrieving metadata, see Access instance metadata for an EC2 instance.
IMDSv2 Linux Run the following command from your Linux instance.
TOKEN=`curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata- token-ttl-seconds: 21600"` \ && curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/ meta-data/product-codes Windows Run the following cmdlets from your Windows instance.

[string]$token = Invoke-RestMethod -Headers @{"X-aws-ec2-metadata-token-ttl-seconds"
 = "21600"} `
    -Method PUT -Uri http://169.254.169.254/latest/api/token Invoke-RestMethod -Headers @{"X-aws-ec2-metadata-token" = $token} `
    -Method GET -Uri http://169.254.169.254/latest/meta-data/product-codes IMDSv1 Linux Run the following command from your Linux instance. curl http://169.254.169.254/latest/meta-data/product-codes Windows Run the following command from your Windows instance.
Invoke-RestMethod -Uri http://169.254.169.254/latest/meta-data/product-codes
## Use paid support for supported AWS Marketplace offerings Amazon EC2 also enables developers to offer support for software (or derived AMIs). Developers can create support products that you can sign up to use. During sign-up for the support product, the developer gives you a product code, which you must then associate with your own AMI. This enables the developer to confirm that your instance is eligible for support. It also ensures that when you run instances of the product, you are charged according to the terms for the product specified by the developer.
Limitations
- After you set the product code attribute, it can't be changed or removed.
- You can't use a support product with Reserved Instances. You always pay the price that's specified by the seller of the support product.
AWS CLI To associate a product code with your AMI

Use the modify-image-attribute command. aws ec2 modify-image-attribute \ --image-id ami-0abcdef1234567890 \ --product-codes "cdef1234abc567def8EXAMPLE"
PowerShell To associate a product code with your AMI Use the Edit-EC2ImageAttribute cmdlet.
Edit-EC2ImageAttribute `
    -ImageId ami-0abcdef1234567890 `
    -ProductCode "cdef1234abc567def8EXAMPLE"
## Bills for paid and supported AMIs At the end of each month, you receive an email with the amount your credit card has been charged for using any paid or supported AMIs during the month. This bill is separate from your regular Amazon EC2 bill. For more information, see Paying for products in the AWS Marketplace Buyer Guide.
## Manage your AWS Marketplace subscriptions On the AWS Marketplace website, you can check your subscription details, view the vendor's usage instructions, manage your subscriptions, and more.
### Check subscription details To check your subscription details
1. Log in to the AWS Marketplace.
2. Choose Your Marketplace Account.
3. Choose Manage your software subscriptions.
4. All your current subscriptions are listed. Choose  Usage Instructions to view specific instructions for using the product, for example, a username for connecting to your running instance.

### Cancel subscription Note
- Canceling a subscription does not terminate the instances launched with that AMI.
We'll continue to bill you for your running instances until they're terminated. You must terminate all instances launched with the AMI in order to stop billing for the subscription.
- After you've canceled your subscription, you are no longer able to launch any instances from that AMI. To use that AMI again, you need to resubscribe to it, either on the AWS Marketplace website, or through the launch wizard in the Amazon EC2 console.
To cancel an AWS Marketplace subscription
1. To stop billing for the subscription, ensure that you have terminated any instances running from the subscription.
Warning Terminating an instance is permanent and irreversible.
After you terminate an instance, you can no longer connect to it, and it can't be recovered. All attached Amazon EBS volumes that are configured to be deleted on termination are also permanently deleted and can't be recovered. All data stored on instance store volumes is permanently lost. For more information, see How instance termination works.
Before you terminate an instance, ensure that you have backed up all data that you need to retain after the termination to persistent storage. a.
Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/. b.
In the navigation pane, choose Instances. c.
Select the instance, and then choose Instance state, Terminate (delete) instance. d.
Choose Terminate (delete) when prompted for confirmation.
2. Log in to the AWS Marketplace, and choose Your Marketplace Account, then Manage your software subscriptions.
3. Choose Cancel subscription. You are prompted to confirm your cancellation.
