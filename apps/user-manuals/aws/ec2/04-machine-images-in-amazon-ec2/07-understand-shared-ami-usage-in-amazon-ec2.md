# Understand shared AMI usage in Amazon EC2

Source: apps/user-manuals/aws/ec2-ug.pdf

---

Setting the Encrypted parameter encrypts the single snapshot for this instance. If you do not specify the KmsKeyId parameter, the default customer managed key is used to encrypt the snapshot copy.
Note You can also copy an image with multiple snapshots and configure the encryption state of each individually.
# Understand shared AMI usage in Amazon EC2 A shared AMI is an AMI that a developer created and made available for others to use. One of the easiest ways to get started with Amazon EC2 is to use a shared AMI that has the components you need and then add custom content. You can also create your own AMIs and share them with others.
You use a shared AMI at your own risk. Amazon can't vouch for the integrity or security of AMIs shared by other Amazon EC2 users. Therefore, you should treat shared AMIs as you would any foreign code that you might consider deploying in your own data center, and perform the appropriate due diligence. We recommend that you get an AMI from a trusted source, such as a verified provider.
## Verified provider In the Amazon EC2 console, public AMIs that are owned by Amazon or a verified Amazon partner are marked Verified provider.
You can also use the describe-images AWS CLI command to identify the public AMIs that come from a verified provider. Public images that are owned by Amazon or a verified partner have an aliased owner, which is either amazon, aws-backup-vault, or aws-marketplace. In the CLI output, these values appear for ImageOwnerAlias. Other users can't alias their AMIs. This enables you to easily find AMIs from Amazon or verified partners.
To become a verified provider, you must register as a seller on the AWS Marketplace. Once registered, you can list your AMI on the AWS Marketplace. For more information, see Getting started as a seller and AMI-based products in the AWS Marketplace Seller Guide.
Shared AMI topics
- Find shared AMIs to use for Amazon EC2 instances

- Prepare to use shared AMIs for Linux
- Control the discovery and use of AMIs in Amazon EC2 with Allowed AMIs
- Make your AMI publicly available for use in Amazon EC2
- Understand block public access for AMIs
- Share an AMI with organizations and organizational units
- Share an AMI with specific AWS accounts
- Cancel having an AMI shared with your AWS account
- Recommendations for creating shared Linux AMIs If you're looking for information about other topics
- For information about creating an AMI, see the section called "Create an Amazon S3-backed AMI" or the section called "Create an AMI".
- For information about building, delivering, and maintaining your applications on the AWS Marketplace, see the AWS Marketplace Documentation.
## Find shared AMIs to use for Amazon EC2 instances You can use the Amazon EC2 console or the command line to find public or private shared AMIs to use with your Amazon EC2 instances.
AMIs are a Regional resource. When you search for a shared AMI (public or private), you must search for it from the same Region from which it is shared. To make an AMI available in a different Region, copy the AMI to the Region, and then share it. For more information, see Copy an Amazon EC2 AMI.
Console The console provides an AMI filter field. You can also scope your searches using the filters provided in the Search field.
To find a shared or AMI
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose AMIs.
3. In the first filter, choose one of the following options:

- Private images – Lists all AMIs that are shared with you.
- Public images – Lists all public AMIs.
4. (Optional) To display only the public images from Amazon, choose the Search field and then, from the menu options, choose Owner alias, then =, and then amazon.
5. (Optional) Add filters to scope your search to AMIs that meet your requirements.
To find a shared public AMI from a verified provider
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose AMI Catalog.
3. Choose Community AMIs.
4. In the Refine results pane, select Verified provider. The Verified provider label indicates that the AMIs are from Amazon or a verified partner.
AWS CLI Use the describe-images command to list AMIs. You can scope the list to the types of AMIs that interest you, as shown in the following examples.
To list all public AMIs The following command lists all public AMIs, including any public AMIs that you own. aws ec2 describe-images --executable-users all To list AMIs with explicit launch permissions The following command lists the AMIs for which you have explicit launch permissions. This list does not include any AMIs that you own. aws ec2 describe-images --executable-users self To list AMIs owned by verified providers The following command lists the AMIs owned by verified providers. Public AMIs owned by verified providers (either Amazon or verified partners) have an aliased owner, which appears as

amazon, aws-backup-vault, or aws-marketplace in the account field. This helps you to easily find AMIs from verified providers. Other users can't alias their AMIs. aws ec2 describe-images \ --owners amazon aws-marketplace \ --query 'Images[*].[ImageId]' \ --output text To list AMIs owned by an account The following command lists the AMIs owned by the specified AWS account. aws ec2 describe-images --owners 123456789012 To scope AMIs using a filter To reduce the number of displayed AMIs, use a filter to list only the types of AMIs that interest you. For example, use the following filter to display only EBS-backed AMIs.
--filters "Name=root-device-type,Values=ebs"
PowerShell Use the Get-EC2Image cmdlet (Tools for Windows PowerShell) to list AMIs. You can scope the list to the types of AMIs that interest you, as shown in the following examples.
To list all public AMIs The following command lists all public AMIs, including any public AMIs that you own.
Get-EC2Image -ExecutableUser all To list AMIs with explicit launch permissions The following command lists the AMIs for which you have explicit launch permissions. This list does not include any AMIs that you own.
Get-EC2Image -ExecutableUser self To list AMIs owned by verified providers

The following command lists the AMIs owned by verified providers. Public AMIs owned by verified providers (either Amazon or verified partners) have an aliased owner, which appears as amazon, aws-backup-vault, or aws-marketplace in the account field. This helps you to easily find AMIs from verified providers. Other users can't alias their AMIs.
Get-EC2Image -Owner amazon aws-marketplace To list AMIs owned by an account The following command lists the AMIs owned by the specified AWS account.
Get-EC2Image -Owner 123456789012 To scope AMIs using a filter To reduce the number of displayed AMIs, use a filter to list only the types of AMIs that interest you. For example, use the following filter to display only EBS-backed AMIs.
-Filter @{Name="root-device-type"; Values="ebs"}
## Prepare to use shared AMIs for Linux Before you use a shared AMI for Linux, take the following steps to confirm that there are no pre- installed credentials that would allow unwanted access to your instance by a third party and no pre-configured remote logging that could transmit sensitive data to a third party. Check the documentation for the Linux distribution used by the AMI for information about improving the security of the system.
To ensure that you don't accidentally lose access to your instance, we recommend that you initiate two SSH sessions and keep the second session open until you've removed credentials that you don't recognize and confirmed that you can still log into your instance using SSH.
1. Identify and disable any unauthorized public SSH keys. The only key in the file should be the key you used to launch the AMI. The following command locates authorized_keys files:
[ec2-user ~]$ sudo find / -name "authorized_keys" -print -exec cat {} \;
2. Disable password-based authentication for the root user. Open the sshd_config file and edit the PermitRootLogin line as follows:

PermitRootLogin without-password Alternatively, you can disable the ability to log into the instance as the root user:
PermitRootLogin No Restart the sshd service.
3. Check whether there are any other users that are able to log in to your instance. Users with superuser privileges are particularly dangerous. Remove or lock the password of any unknown accounts.
4. Check for open ports that you aren't using and running network services listening for incoming connections.
5. To prevent preconfigured remote logging, you should delete the existing configuration file and restart the rsyslog service. For example:
[ec2-user ~]$ sudo rm /etc/rsyslog.conf [ec2-user ~]$ sudo service rsyslog restart
6. Verify that all cron jobs are legitimate.
If you discover a public AMI that you feel presents a security risk, contact the AWS security team.
For more information, see the AWS Security Center.
## Control the discovery and use of AMIs in Amazon EC2 with Allowed AMIs AMIs To control the discovery and use of Amazon Machine Images (AMIs) by users in your AWS account, you can use the Allowed AMIs feature. You specify criteria that AMIs must meet to be visible and available within your account. When the criteria are enabled, users launching instances will only see and have access to AMIs that comply with the specified criteria. For example, you can specify a list of trusted AMI providers as the criteria, and only AMIs from these providers will be visible and available for use.
Before enabling the Allowed AMIs settings, you can enable audit mode to preview which AMIs will or won't be visible and available for use. This lets you refine the criteria as needed to ensure that only the intended AMIs are visible and available to users in your account. Additionally, use the

describe-instance-image-metadata command to find instances that were launched with AMIs that don't meet the specified criteria. This information can guide your decision to either update your launch configurations to use compliant AMIs (for example, specifying a different AMI in a launch template) or adjust your criteria to allow these AMIs.
You specify the Allowed AMIs settings at the account level, either directly in the account or by using a declarative policy. These settings must be configured in each AWS Region where you want to control AMI usage. Using a declarative policy allows you to apply the settings across multiple Regions simultaneously, as well as across multiple accounts simultaneously. When a declarative policy is in use, you can't modify the settings directly within an account. This topic describes how to configure the settings directly within an account. For information about using declarative policies, see Declarative policies in the AWS Organizations User Guide.
Note The Allowed AMIs feature only controls the discovery and use of public AMIs or AMIs shared with your account. It does not restrict the AMIs owned by your account. Regardless of the criteria you set, the AMIs created by your account are always discoverable and usable by users in your account.
Key benefits of Allowed AMIs
- Compliance and security: Users can only discover and use AMIs that meet the specified criteria, reducing the risk of non-compliant AMI usage.
- Efficient management: By reducing the number of allowed AMIs, managing the remaining ones becomes easier and more efficient.
- Centralized account-level implementation: Configure the Allowed AMIs settings at the account level, either directly within the account or through a declarative policy. This provides a centralized and efficient way to control AMI usage across the entire account.
Contents
- How Allowed AMIs works
- Best practices for implementing Allowed AMIs
- Required IAM permissions
- Manage the settings for Allowed AMIs

### How Allowed AMIs works To control which AMIs can be discovered and used in your account, you define a set of criteria against which to evaluate the AMIs. The criteria are made up of one or more ImageCriterion as shown in the following diagram. An explanation follows the diagram.
The configuration has three levels:
- 1 – Parameter values
- Multi-value parameters:
- ImageProviders
- ImageNames
- MarketplaceProductCodes An AMI can match any values within a parameter to be allowed.
Example: ImageProviders = amazon OR account 111122223333 OR account 444455556666 (The evaluation logic for parameter values is not shown in the diagram.)
- Single-value parameters:
- CreationDateCondition
- DeprecationTimeCondition
- 2 – ImageCriterion
- Groups multiple parameters with AND logic.

- An AMI must match all parameters within an ImageCriterion to be allowed.
- Example: ImageProviders = amazon AND CreationDateCondition = 300 days or less
- 3 – ImageCriteria
- Groups multiple ImageCriterion with OR logic.
- An AMI can match any ImageCriterion to be allowed.
- Forms the complete configuration against which AMIs are evaluated.
Topics
- Allowed AMIs parameters
- Allowed AMIs configuration
- How criteria are evaluated
- Limits
- Allowed AMIs operations
#### Allowed AMIs parameters The following parameters can be configured to create ImageCriterion:
ImageProviders The AMI providers whose AMIs are allowed.
Valid values are aliases that are defined by AWS, and AWS account IDs, as follows:
- amazon – An alias that identifies AMIs created by Amazon or verified providers
- aws-marketplace – An alias that identifies AMIs created by verified providers in the AWS Marketplace
- aws-backup-vault – An alias that identifies backup AMIs that reside in logically air-gapped AWS Backup vault accounts. If you use the AWS Backup logically air-gapped vault feature, ensure this alias is included as an AMI provider.
- AWS account IDs – One or more 12-digit AWS account IDs
- none – Indicates that only AMIs created by your account can be discovered and used. Public or shared AMIs can't be discovered and used. When specified, no other criteria can be specified.

ImageNames The names of allowed AMIs, using exact matches or wildcards (? or *).
MarketplaceProductCodes The AWS Marketplace product codes for allowed AMIs.
CreationDateCondition The maximum age for allowed AMIs.
DeprecationTimeCondition The maximum period since deprecation for allowed AMIs.
For the valid values and constraints for each criterion, see ImageCriterionRequest in the Amazon EC2 API Reference.
#### Allowed AMIs configuration The core configuration for Allowed AMIs is the ImageCriteria configuration that defines the criteria for allowed AMIs. The following JSON structure shows the parameters that can be specified:
{ "State": "enabled" | "disabled" | "audit-mode", "ImageCriteria" : [ { "ImageProviders": ["string",...], "MarketplaceProductCodes": ["string",...], "ImageNames":["string",...], "CreationDateCondition" : { "MaximumDaysSinceCreated": integer }, "DeprecationTimeCondition" : { "MaximumDaysSinceDeprecated": integer } }, ...
}

##### ImageCriteria example The following ImageCriteria example configures four ImageCriterion. An AMI is allowed if it matches any one of these ImageCriterion. For information about how the criteria are evaluated, see How criteria are evaluated.
{ "ImageCriteria": [ // ImageCriterion 1: Allow AWS Marketplace AMIs with product code "abcdefg1234567890"
        { "MarketplaceProductCodes": [ "abcdefg1234567890"
            ]
        }, // ImageCriterion 2: Allow AMIs from providers whose accounts are // "123456789012" OR "123456789013" AND AMI age is less than 300 days { "ImageProviders": [ "123456789012", "123456789013"
            ], "CreationDateCondition": { "MaximumDaysSinceCreated": 300 } }, // ImageCriterion 3: Allow AMIs from provider whose account is "123456789014"
        // AND with names following the pattern "golden-ami-*"
        { "ImageProviders": [ "123456789014"
            ], "ImageNames": [ "golden-ami-*"
            ]
        }, // ImageCriterion 4: Allow AMIs from Amazon or verified providers // AND which aren't deprecated { "ImageProviders": [ "amazon"
            ], "DeprecationTimeCondition": {

                "MaximumDaysSinceDeprecated": 0 } } ]
}
#### How criteria are evaluated The following table explains the evaluation rules that determine if an AMI is allowed, showing how the AND or OR operator is applied at each level:
Evaluation level Operator Requirement to be an Allowed AMI Parameter values for ImageProviders , ImageNames , and MarketplaceProduct Codes OR AMI must match at least one value in each parameter list ImageCriterion AND AMI must match all parameters in each ImageCriterion ImageCriteria OR AMI must match any one of the ImageCriterion Using the preceding evaluation rules, let's see how to apply them to the ImageCriteria example:
- ImageCriterion 1: Allows AMIs that have the AWS Marketplace product code abcdefg1234567890 OR
- ImageCriterion 2: Allows AMIs that meet both of these criteria:
- Owned by either account 123456789012 OR 123456789013
- AND
- Created within the last 300 days

OR
- ImageCriterion 3: Allows AMIs that meet both of these criteria:
- Owned by account 123456789014
- AND
- Named with the pattern golden-ami-* OR
- ImageCriterion 4: Allows AMIs that meet both of these criteria:
- Published by Amazon or verified providers (specified by the amazon alias)
- AND
- Not deprecated (maximum days since deprecation is 0)
#### Limits The ImageCriteria can include up to:
- 10 ImageCriterion Each ImageCriterion can include up to:
- 200 values for ImageProviders
- 50 values for ImageNames
- 50 values for MarketplaceProductCodes Example of limits Using the preceding ImageCriteria example:
- There are 4 ImageCriterion. Up to 6 more can be added to the request to reach the limit of
10. - In the first ImageCriterion, there is 1 value for MarketplaceProductCodes. Up to 49 more can be added to this ImageCriterion to reach the limit of 50.
- In the second ImageCriterion, there are 2 values for ImageProviders. Up to 198 more can be added to this ImageCriterion to reach the limit of 200.

- In the third ImageCriterion, there is 1 value for ImageNames. Up to 49 more can be added to this ImageCriterion to reach the limit of 50.
#### Allowed AMIs operations The Allowed AMIs feature has three operational states for managing the image criteria: enabled, disabled, and audit mode. These allow you to enable or disable the image criteria, or review them as needed.
Enabled When Allowed AMIs is enabled:
- The ImageCriteria are applied.
- Only allowed AMIs are discoverable in the EC2 console and by APIs that use images (for example, that describe, copy, store, or perform other actions that use images).
- Instances can only be launched using allowed AMIs.
Disabled When Allowed AMIs is disabled:
- The ImageCriteria are not applied.
- No restrictions are placed on AMI discoverability or usage.
Audit mode In audit mode:
- The ImageCriteria are applied, but no restrictions are placed on AMI discoverability or usage.
- In the EC2 console, for each AMI, the Allowed image field displays either Yes or No to indicate whether the AMI will be discoverable and available to users in the account when Allowed AMIs is enabled.
- In the command line, the response for the describe-image operation includes "ImageAllowed": true or "ImageAllowed": false to indicate whether the AMI will be discoverable and available to users in the account when Allowed AMIs is enabled.
- In the EC2 console, the AMI Catalog displays Not allowed next to AMIs that won't be discoverable or available to users in the account when Allowed AMIs is enabled.

### Best practices for implementing Allowed AMIs When implementing Allowed AMIs, consider these best practices to ensure a smooth transition and minimize potential disruptions to your AWS environment.
1. Enable audit mode Begin by enabling Allowed AMIs in audit mode. This state allows you to see which AMIs would be affected by your criteria without actually restricting access, providing a risk-free evaluation period.
2. Set Allowed AMIs criteria Carefully establish which AMI providers align with your organization's security policies, compliance requirements, and operational needs.
Note When using AWS managed services, such as Amazon ECS, Amazon EKS, or AWS Lambda Managed Instances, we recommend specifying the amazon alias to allow AMIs created by AWS. These services depend on Amazon-published AMIs to launch instances.
Be cautious when setting CreationDateCondition restrictions for any AMIs. Setting overly restrictive date conditions (for example, AMIs must be less than 5 days old) can cause instance launch failures if the AMIs, whether from AWS or other providers, are not updated within your specified time frame.
We recommend pairing ImageNames with ImageProviders for better control and specificity. Using ImageNames alone might not uniquely identify an AMI.
3. Check for impact on expected business processes You can use the console or the CLI to identify any instances that were launched with AMIs that don't meet the specified criteria. This information can guide your decision to either update your launch configurations to use compliant AMIs (for example, specifying a different AMI in a launch template) or adjust your criteria to allow these AMIs.
Console: Use the ec2-instance-launched-with-allowed-ami AWS Config rule to check if running or stopped instances were launched with AMIs that meet your Allowed AMIs criteria. The rule is NON_COMPLIANT if an AMI doesn't meet the Allowed AMIs criteria, and COMPLIANT if it does.
The rule only operates when the Allowed AMIs setting is set to enabled or audit mode.

CLI: Run the describe-instance-image-metadata command and filter the response to identify any instances that were launched with AMIs that don't meet the specified criteria.
For the console and CLI instructions, see Find instances launched from AMIs that aren't allowed.
4. Enable Allowed AMIs Once you've confirmed that the criteria will not adversely affect expected business processes, enable Allowed AMIs.
5. Monitor instance launches Continue to monitor instance launches from AMIs across your applications and the AWS managed services you use, such as Amazon EMR, Amazon ECR, Amazon EKS, and AWS Elastic Beanstalk. Check for any unexpected issues and make necessary adjustments to the Allowed AMIs criteria.
6. Pilot new AMIs To test third-party AMIs that do not comply with your current Allowed AMIs settings, AWS recommends the following approaches:
- Use a separate AWS account: Create an account with no access to your business-critical resources. Ensure that the Allowed AMIs setting is not enabled in this account, or that the AMIs you want to test are explicitly allowed, so that you can test them.
- Test in another AWS Region: Use a Region where the third-party AMIs are available, but where you have not yet enabled the Allowed AMIs settings.
These approaches help ensure your business-critical resources remain secure while you test new AMIs.
### Required IAM permissions To use the Allowed AMIs feature, you need the following IAM permissions:
- GetAllowedImagesSettings
- EnableAllowedImagesSettings
- DisableAllowedImagesSettings
- ReplaceImageCriteriaInAllowedImagesSettings

### Manage the settings for Allowed AMIs You can manage the settings for Allowed AMIs. These settings are per Region per account.
Tasks
- Enable Allowed AMIs
- Set the Allowed AMIs criteria
- Disable Allowed AMIs
- Get the Allowed AMIs criteria
- Find AMIs that are allowed
- Find instances launched from AMIs that aren't allowed
#### Enable Allowed AMIs You can enable Allowed AMIs and specify Allowed AMIs criteria. We recommend that you begin in audit mode, which shows you which AMIs would be affected by the criteria without actually restricting access.
Console To enable Allowed AMIs
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Dashboard.
3. Under Account attributes (top right), choose Allowed AMIs.
4. On the Allowed AMIs tab, choose Manage.
5. For Allowed AMIs settings, choose Audit mode or Enabled. We recommend that you begin in audit mode, test the criteria, and then return to this step to enable Allowed AMIs.
6. (Optional) For AMI criteria, enter the criteria in JSON format.
7. Choose Update.
AWS CLI To enable Allowed AMIs Use the enable-allowed-images-settings command.

aws ec2 enable-allowed-images-settings --allowed-images-settings-state enabled To enable audit mode instead, specify audit-mode instead of enabled. aws ec2 enable-allowed-images-settings --allowed-images-settings-state audit-mode PowerShell To enable Allowed AMIs Use the Enable-EC2AllowedImagesSetting cmdlet.
Enable-EC2AllowedImagesSetting -AllowedImagesSettingsState enabled To enable audit mode instead, specify audit-mode instead of enabled.
Enable-EC2AllowedImagesSetting -AllowedImagesSettingsState audit-mode
#### Set the Allowed AMIs criteria After you enable Allowed AMIs, you can set or replace the Allowed AMIs criteria.
For the correct configuration and valid values, see Allowed AMIs configuration and Allowed AMIs parameters.
Console To set the Allowed AMIs criteria
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Dashboard.
3. Under Account attributes (top right), choose Allowed AMIs.
4. On the Allowed AMIs tab, choose Manage.
5. For AMI criteria, enter the criteria in JSON format.
6. Choose Update.

AWS CLI To set the Allowed AMIs criteria Use the replace-image-criteria-in-allowed-images-settings command and specify the JSON file that contains the Allowed AMIs criteria. aws ec2 replace-image-criteria-in-allowed-images-settings --cli-input-json file://file_name.json PowerShell To set the Allowed AMIs criteria Use the Set-EC2ImageCriteriaInAllowedImagesSetting cmdlet and specify the JSON file that contains the Allowed AMIs criteria.
$imageCriteria = Get-Content -Path .\file_name.json | ConvertFrom-Json Set-EC2ImageCriteriaInAllowedImagesSetting -ImageCriterion $imageCriteria
#### Disable Allowed AMIs You can disable Allowed AMIs as follows.
Console To disable Allowed AMIs
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Dashboard.
3. Under Account attributes (top right), choose Allowed AMIs.
4. On the Allowed AMIs tab, choose Manage.
5. For Allowed AMIs settings, choose Disabled.
6. Choose Update.
AWS CLI To disable Allowed AMIs Use the disable-allowed-images-settings command.

aws ec2 disable-allowed-images-settings PowerShell To disable Allowed AMIs Use the Disable-EC2AllowedImagesSetting cmdlet.
Disable-EC2AllowedImagesSetting
#### Get the Allowed AMIs criteria You can get the current state of the Allowed AMIs setting and the Allowed AMIs criteria.
Console To get the Allowed AMIs state and criteria
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Dashboard.
3. Under Account attributes (top right), choose Allowed AMIs.
4. On the Allowed AMIs tab, Allowed AMIs settings is set to Enabled, Disabled, or Audit mode.
5. If the state of Allowed AMIs is either Enabled or Audit mode, AMI criteria, displays the AMI criteria in JSON format.
AWS CLI To get the Allowed AMIs state and criteria Use the get-allowed-images-settings command. aws ec2 get-allowed-images-settings In the following example output, the state is audit-mode and the image criteria are set in the account.
{

    "State": "audit-mode", "ImageCriteria": [ { "MarketplaceProductCodes": [ "abcdefg1234567890"
            ]
        }, { "ImageProviders": [ "123456789012", "123456789013"
            ], "CreationDateCondition": { "MaximumDaysSinceCreated": 300 } }, { "ImageProviders": [ "123456789014"
            ], "ImageNames": [ "golden-ami-*"
            ]
        }, { "ImageProviders": [ "amazon"
            ], "DeprecationTimeCondition": { "MaximumDaysSinceDeprecated": 0 } } ], "ManagedBy": "account"
} PowerShell To get the Allowed AMIs state and criteria Use the Get-EC2AllowedImagesSetting cmdlet.
Get-EC2AllowedImagesSetting | Select-Object `
    State, `

    ManagedBy, `
    @{Name='ImageProviders'; Expression={($_.ImageCriteria.ImageProviders)}}, `
    @{Name='MarketplaceProductCodes'; Expression={($_.ImageCriteria.MarketplaceProductCodes)}}, `
    @{Name='ImageNames'; Expression={($_.ImageCriteria.ImageNames)}}, `
    @{Name='MaximumDaysSinceCreated'; Expression={($_.ImageCriteria.CreationDateCondition.MaximumDaysSinceCreated)}}, `
    @{Name='MaximumDaysSinceDeprecated'; Expression={($_.ImageCriteria.DeprecationTimeCondition.MaximumDaysSinceDeprecated)}} In the following example output, the state is audit-mode and the image criteria are set in the account.
State      : audit-mode ManagedBy  : account ImageProviders            : {123456789012, 123456789013, 123456789014, amazon} MarketplaceProductCodes   : {abcdefg1234567890} ImageNames                : {golden-ami-*} MaximumDaysSinceCreated  : 300 MaximumDaysSinceDeprecated: 0
#### Find AMIs that are allowed You can find the AMIs that are allowed or not allowed by the current Allowed AMIs criteria.
Note Allowed AMIs must be in audit mode.
Console To check whether an AMI meets the Allowed AMIs criteria
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose AMIs.
3. Select the AMI.
4. On the Details tab (if you selected the checkbox) or in the summary area (if you selected the AMI ID), find the Allowed image field.

- Yes – The AMI meets the Allowed AMIs criteria. This AMI will be available to users in your account after you enable Allowed AMIs.
- No – The AMI does not meet the Allowed AMIs criteria.
5. In the navigation pane, choose AMI Catalog.
An AMI marked Not allowed indicates an AMI that does not meet the Allowed AMIs criteria.
This AMI won't be visible or available to users in your account when Allowed AMIs is enabled.
AWS CLI To check whether an AMI meets the Allowed AMIs criteria Use the describe-images command. aws ec2 describe-images \ --image-id ami-0abcdef1234567890 \ --query Images[].ImageAllowed \ --output text The following is example output.
True To find AMIs that meet the Allowed AMIs criteria Use the describe-images command. aws ec2 describe-images \ --filters "Name=image-allowed,Values=true" \ --max-items 10 \ --query Images[].ImageId The following is example output. ami-000eaaa8be2fd162a ami-000f82db25e50de8e ami-000fc21eb34c7a9a6

ami-0010b876f1287d7be ami-0010b929226fe8eba ami-0010957836340aead ami-00112c992a47ba871 ami-00111759e194abcc1 ami-001112565ffcafa5e ami-0011e45aaee9fba88 PowerShell To check whether an AMI meets the Allowed AMIs criteria Use the Get-EC2Image cmdlet.
(Get-EC2Image -ImageId ami-0abcdef1234567890).ImageAllowed The following is example output.
True To find AMIs that meet the Allowed AMIs criteria Use the Get-EC2Image cmdlet.
Get-EC2Image `
    -Filter @{Name="image-allows";Values="true"} `
    -MaxResult 10 | `
    Select ImageId The following is example output. ami-000eaaa8be2fd162a ami-000f82db25e50de8e ami-000fc21eb34c7a9a6 ami-0010b876f1287d7be ami-0010b929226fe8eba ami-0010957836340aead ami-00112c992a47ba871 ami-00111759e194abcc1 ami-001112565ffcafa5e

ami-0011e45aaee9fba88
#### Find instances launched from AMIs that aren't allowed You can identify the instances that were launched using an AMI that does not meet the Allowed AMIs criteria.
Console To check whether an instance was launched using an AMI that isn't allowed
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Instances.
3. Select the instance.
4. On the Details tab, under Instance details, find Allowed image.
- Yes – The AMI meets the Allowed AMIs criteria.
- No – The AMI does not meet the Allowed AMIs criteria.
AWS CLI To find instances launched using AMIs that aren't allowed Use the describe-instance-image-metadata command with the image-allowed filter. aws ec2 describe-instance-image-metadata \ --filters "Name=image-allowed,Values=false" \ --query "InstanceImageMetadata[*].[InstanceId,ImageMetadata.ImageId]" \ --output table The following is example output.
--------------------------------------------------
|          DescribeInstanceImageMetadata         | +----------------------+-------------------------+
|  i-08fd74f3f1595fdbd |  ami-09245d5773578a1d6  |
|  i-0b1bf24fd4f297ab9 |  ami-07cccf2bd80ed467f  |
|  i-026a2eb590b4f7234 |  ami-0c0ec0a3a3a4c34c0  |

|  i-006a6a4e8870c828f |  ami-0a70b9d193ae8a799  |
|  i-0781e91cfeca3179d |  ami-00c257e12d6828491  |
|  i-02b631e2a6ae7c2d9 |  ami-0bfddf4206f1fa7b9  | +----------------------+-------------------------+ PowerShell To find instances launched using AMIs that aren't allowed Use the Get-EC2InstanceImageMetadata cmdlet.
Get-EC2InstanceImageMetadata `
    -Filter @{Name="image-allowed";Values="false"} | `
    Select InstanceId, @{Name='ImageId'; Expression={($_.ImageMetadata.ImageId)}} The following is example output.
InstanceId          ImageId ----------          ------- i-08fd74f3f1595fdbd ami-09245d5773578a1d6 i-0b1bf24fd4f297ab9 ami-07cccf2bd80ed467f i-026a2eb590b4f7234 ami-0c0ec0a3a3a4c34c0 i-006a6a4e8870c828f ami-0a70b9d193ae8a799 i-0781e91cfeca3179d ami-00c257e12d6828491 i-02b631e2a6ae7c2d9 ami-0bfddf4206f1fa7b9 AWS Config You can add the ec2-instance-launched-with-allowed-ami AWS Config rule, configure it for your requirements, and then use it to evaluate your instances.
For more information, see Adding AWS Config rules and ec2-instance-launched-with-allowed- ami in the AWS Config Developer Guide.
## Make your AMI publicly available for use in Amazon EC2 You can make your AMI publicly available by sharing it with all AWS accounts.
If you want to prevent the public sharing of your AMIs, you can enable block public access for AMIs.
This blocks any attempts to make an AMI public, helping to prevent unauthorized access and

potential misuse of AMI data. Note that enabling block public access does not affect your AMIs that are already publicly available; they remain publicly available. For more information, see Understand block public access for AMIs.
To allow only specific accounts to use your AMI to launch instances, see Share an AMI with specific AWS accounts.
Contents
- Considerations
- Share an AMI with all AWS accounts (share publicly)
### Considerations Consider the following before making an AMI public.
- Ownership – To make an AMI public, your AWS account must own the AMI.
- Region – AMIs are a Regional resource. When you share an AMI, it is available only in the Region from which you shared it. To make an AMI available in a different Region, copy the AMI to the Region and then share it. For more information, see Copy an Amazon EC2 AMI.
- Block public access – To publicly share an AMI, block public access for AMIs must be disabled in each Region in which the AMI will be publicly shared. After you've publicly shared the AMI, you can re-enable block public access for AMIs to prevent further public sharing of your AMIs.
- Some AMIs can't be made public – If your AMI includes one of the following components, you can't make it public (but you can share the AMI with specific AWS accounts):
- Encrypted volumes
- Snapshots of encrypted volumes
- Product codes
- Avoid exposing sensitive data – To avoid exposing sensitive data when you share an AMI, read the security considerations in Recommendations for creating shared Linux AMIs and follow the recommended actions.
- Usage – When you share an AMI, users can only launch instances from the AMI. They can't delete, share, or modify it. However, after they have launched an instance using your AMI, they can then create an AMI from the instance they launched.
- Automatic deprecation – By default, the deprecation date of all public AMIs is set to two years from the AMI creation date. You can set the deprecation date to earlier than two years. To cancel

the deprecation date, or to move the deprecation to a later date, you must make the AMI private by only sharing it with specific AWS accounts.
- Remove obsolete AMIs – After a public AMI reaches its deprecation date, if no new instances were launched from the AMI for six or more months, AWS eventually removes the public sharing property so that obsolete AMIs don't appear in the public AMI lists.
- Billing – You are not billed when your AMI is used by other AWS accounts to launch instances.
The accounts that launch instances using the AMI are billed for the instances that they launch.
### Share an AMI with all AWS accounts (share publicly)
After you make an AMI public, it is available in Community AMIs in the console, which you can access from the AMI Catalog in the left navigator in the EC2 console or when launching an instance using the console. Note that it can take a short while for an AMI to appear in Community AMIs after you make it public.
Console To make an AMI public
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose AMIs.
3. Select your AMI from the list, and then choose Actions, Edit AMI permissions.
4. Under AMI availability, choose Public.
5. Choose Save changes.
AWS CLI Each AMI has a launchPermission property that controls which AWS accounts, besides the owner's, are allowed to use that AMI to launch instances. By modifying the launchPermission property of an AMI, you can make the AMI public (which grants launch permissions to all AWS accounts), or share it with only the AWS accounts that you specify.
You can add or remove account IDs from the list of accounts that have launch permissions for an AMI. To make the AMI public, specify the all group. You can specify both public and explicit launch permissions.

To make an AMI public
1. Use the modify-image-attribute command as follows to add the all group to the launchPermission list for the specified AMI. aws ec2 modify-image-attribute \ --image-id ami-0abcdef1234567890 \ --launch-permission "Add=[{Group=all}]"
2. To verify the launch permissions of the AMI, use the describe-image-attribute command. aws ec2 describe-image-attribute \ --image-id ami-0abcdef1234567890 \ --attribute launchPermission
3. (Optional) To make the AMI private again, remove the all group from its launch permissions. Note that the owner of the AMI always has launch permissions and is therefore unaffected by this command. aws ec2 modify-image-attribute \ --image-id ami-0abcdef1234567890 \ --launch-permission "Remove=[{Group=all}]"
PowerShell Each AMI has a launchPermission property that controls which AWS accounts, besides the owner's, are allowed to use that AMI to launch instances. By modifying the launchPermission property of an AMI, you can make the AMI public (which grants launch permissions to all AWS accounts), or share it with only the AWS accounts that you specify.
You can add or remove account IDs from the list of accounts that have launch permissions for an AMI. To make the AMI public, specify the all group. You can specify both public and explicit launch permissions.
To make an AMI public
1. Use the Edit-EC2ImageAttribute command as follows to add the all group to the launchPermission list for the specified AMI.
Edit-EC2ImageAttribute `

    -ImageId ami-0abcdef1234567890 `
    -Attribute launchPermission `
    -OperationType add `
    -UserGroup all
2. To verify the launch permissions of the AMI, use the following Get-EC2ImageAttribute command.
Get-EC2ImageAttribute `
    -ImageId ami-0abcdef1234567890 `
    -Attribute launchPermission
3. (Optional) To make the AMI private again, remove the all group from its launch permissions. Note that the owner of the AMI always has launch permissions and is therefore unaffected by this command.
Edit-EC2ImageAttribute `
    -ImageId ami-0abcdef1234567890 `
    -Attribute launchPermission `
    -OperationType remove `
    -UserGroup all
## Understand block public access for AMIs To prevent the public sharing of your AMIs, you can enable block public access for AMIs at the account level.
When block public access is enabled, any attempt to make an AMI public is automatically blocked.
However, if you already have public AMIs, they remain publicly available.
To publicly share AMIs, you must disable block public access. When you're done sharing, it's best practice to re-enable block public access to prevent any unintended public sharing of your AMIs.
Note This setting is configured at the account level, either directly in the account or by using a declarative policy. It must be configured in each AWS Region where you want to prevent the public sharing of your AMIs. Using a declarative policy allows you to apply the setting across multiple Regions simultaneously, as well as across multiple accounts simultaneously. When a declarative policy is in use, you can't modify the setting directly

within an account. This topic describes how to configure the setting directly within an account. For information about using declarative policies, see Declarative policies in the AWS Organizations User Guide.
You can restrict IAM permissions to an administrator user so that only they can enable or disable block public access for AMIs.
Topics
- Default settings
- Manage the block public access setting for AMIs
### Default settings The Block public access for AMIs setting is either enabled or disabled by default depending on whether your account is new or existing, and whether you have public AMIs. The following table lists the default settings:
AWS account Block public access for AMIs default setting New accounts Enabled Existing accounts with no public AMIs ¹ Enabled Existing accounts with one or more public AMIs Disabled ¹ If your account had one or more public AMIs on or after July 15, 2023, Block public access for AMIs is disabled by default for your account, even if you subsequently made all the AMIs private.
### Manage the block public access setting for AMIs You can manage the block public access setting for your AMIs to control whether they can be publicly shared. You can enable, disable, or view the current block public access state for your AMIs using the Amazon EC2 console or the AWS CLI.

#### View the block public access state for AMIs To see whether the public sharing of your AMIs is blocked in your account, you can view the state for block public access for AMIs. You must view the state in each AWS Region in which you want to see whether the public sharing of your AMIs is blocked.
Required permissions To get the current block public access setting for AMIs, you must have the GetImageBlockPublicAccessState IAM permission.
Console To view the block public access state for AMIs in the specified Region
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. From the navigation bar (at the top of the screen), select the Region in which to view the block public access state for AMIs.
3. If the dashboard is not displayed, in the navigation pane, choose EC2 Dashboard.
4. Under Account attributes, choose Data protection and security.
5. Under Block public access for AMIs, check the Public access field. The value is either New public sharing blocked or New public sharing allowed.
AWS CLI To get the block public access state for AMIs Use the  get-image-block-public-access-state command. The value is either block-new- sharing or unblocked.
Example: For a specific Region aws ec2 get-image-block-public-access-state --region us-east-1 The ManagedBy field indicates the entity that configured the setting. In this example, account indicates that the setting was configured directly in the account. A value of declarative- policy would mean the setting was configured by a declarative policy. For more information, see Declarative policies in the AWS Organizations User Guide.

{ "ImageBlockPublicAccessState": "block-new-sharing", "ManagedBy": "account"
} Example: For all Regions in your account echo -e "Region   \t Public Access State" ; \ echo -e "-------------- \t ----------------------" ; \ for region in $( aws ec2 describe-regions \ --region us-east-1 \ --query "Regions[*].[RegionName]" \ --output text ); do (output=$( aws ec2 get-image-block-public-access-state \ --region $region \ --output text) echo -e "$region \t $output"
    ); done The following is example output.
Region           Public Access State --------------   ---------------------- ap-south-1       block-new-sharing eu-north-1       unblocked eu-west-3        block-new-sharing ...
PowerShell To get the block public access state for AMIs Use the Get-EC2ImageBlockPublicAccessState cmdlet. The value is either block-new-sharing or unblocked.
Example: For a specific Region Get-EC2ImageBlockPublicAccessState -Region us-east-1

The following is example output. block-new-sharing Example: For all Regions in your account (Get-EC2Region).RegionName | `
    ForEach-Object { [PSCustomObject]@{ Region   = $_ PublicAccessState = (Get-EC2ImageBlockPublicAccessState -Region $_)
        } } | `
Format-Table -AutoSize The following is example output.
Region         PublicAccessState ------         ----------------- ap-south-1     block-new-sharing eu-north-1     block-new-sharing eu-west-3      block-new-sharing ...
#### Enable block public access for AMIs To prevent the public sharing of your AMIs, enable block public access for AMIs at the account level.
You must enable block public access for AMIs in each AWS Region in which you want to prevent the public sharing of your AMIs. If you already have public AMIs, they will remain publicly available.
Required permissions To enable the block public access setting for AMIs, you must have the EnableImageBlockPublicAccess IAM permission.
### Considerations
- It can take up to 10 minutes to configure this setting. During this time, if you describe the public access state, the response is unblocked. When the configuration is completed, the response is block-new-sharing.

Console To enable block public access for AMIs in the specified Region
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. From the navigation bar (at the top of the screen), select the Region in which to enable block public access for AMIs.
3. If the dashboard is not displayed, in the navigation pane, choose EC2 Dashboard.
4. Under Account attributes, choose Data protection and security.
5. Under Block public access for AMIs, choose Manage.
6. Select the Block new public sharing checkbox, and then choose Update.
AWS CLI To enable block public access for AMIs Use the enable-image-block-public-access command.
Example: For a specific Region aws ec2 enable-image-block-public-access \ --region us-east-1 \ --image-block-public-access-state block-new-sharing The following is example output.
{ "ImageBlockPublicAccessState": "block-new-sharing"
} Example: For all Regions in your account echo -e "Region   \t Public Access State" ; \ echo -e "-------------- \t ----------------------" ; \ for region in $( aws ec2 describe-regions \ --region us-east-1 \ --query "Regions[*].[RegionName]" \ --output text

    ); do (output=$( aws ec2 enable-image-block-public-access \ --region $region \ --image-block-public-access-state block-new-sharing \ --output text) echo -e "$region \t $output"
    ); done The following is example output.
Region           Public Access State --------------   ---------------------- ap-south-1       block-new-sharing eu-north-1       block-new-sharing eu-west-3        block-new-sharing ...
PowerShell To enable block public access for AMIs Use the Enable-EC2ImageBlockPublicAccess command.
Example: For a specific Region Enable-EC2ImageBlockPublicAccess `
    -Region us-east-1 `
    -ImageBlockPublicAccessState block-new-sharing The following is example output.
Value
----- block-new-sharing Example: For all Regions in your account (Get-EC2Region).RegionName | `
    ForEach-Object { [PSCustomObject]@{

        Region            = $_ PublicAccessState = ( Enable-EC2ImageBlockPublicAccess `
         -Region $_ `
         -ImageBlockPublicAccessState block-new-sharing)
    } } | `
Format-Table -AutoSize The following is example output.
Region         PublicAccessState ------         ----------------- ap-south-1     block-new-sharing eu-north-1     block-new-sharing eu-west-3      block-new-sharing ...
#### Disable block public access for AMIs To allow the users in your account to publicly share your AMIs, disable block public access at the account level. You must disable block public access for AMIs in each AWS Region in which you want to allow the public sharing of your AMIs.
Required permissions To disable the block public access setting for AMIs, you must have the DisableImageBlockPublicAccess IAM permission.
### Considerations
- It can take up to 10 minutes to configure this setting. During this time, if you describe the public access state, the response is block-new-sharing. When the configuration is completed, the response is unblocked.
Console To disable block public access for AMIs in the specified Region
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.

2. From the navigation bar (at the top of the screen), select the Region in which to disable block public access for AMIs.
3. If the dashboard is not displayed, in the navigation pane, choose EC2 Dashboard.
4. Under Account attributes, choose Data protection and security.
5. Under Block public access for AMIs, choose Manage.
6. Clear the Block new public sharing checkbox, and then choose Update.
7. Enter confirm when prompted for confirmation, and then choose Allow public sharing.
AWS CLI To disable block public access for AMIs Use the disable-image-block-public-access command.
Example: For a specific Region aws ec2 disable-image-block-public-access --region us-east-1 The following is example output.
{ "ImageBlockPublicAccessState": "unblocked"
} Example: For all Regions in your account echo -e "Region   \t Public Access State" ; \ echo -e "-------------- \t ----------------------" ; \ for region in $( aws ec2 describe-regions \ --region us-east-1 \ --query "Regions[*].[RegionName]" \ --output text ); do (output=$( aws ec2 disable-image-block-public-access \ --region $region \ --output text)

        echo -e "$region \t $output"
    ); done The following is example output.
Region           Public Access State --------------   ---------------------- ap-south-1       unblocked eu-north-1       unblocked eu-west-3        unblocked ...
PowerShell To disable block public access for AMIs Use the Disable-EC2ImageBlockPublicAccess cmdlet.
Example: For a specific Region Disable-EC2ImageBlockPublicAccess -Region us-east-1 The following is example output.
Value
----- unblocked Example: For all Regions in your account (Get-EC2Region).RegionName | `
    ForEach-Object { [PSCustomObject]@{ Region            = $_ PublicAccessState = (Disable-EC2ImageBlockPublicAccess -Region $_)
    } } | `
Format-Table -AutoSize


The following is example output.
Region         PublicAccessState ------         ----------------- ap-south-1     unblocked eu-north-1     unblocked eu-west-3      unblocked ...
## Share an AMI with organizations and organizational units AWS Organizations is an account management service that enables you to consolidate multiple AWS accounts into an organization that you create and centrally manage. You can share an AMI with an organization or an organizational unit (OU) that you have created, in addition to sharing it with specific accounts.
An organization is an entity that you create to consolidate and centrally manage your AWS accounts. You can organize the accounts in a hierarchical, tree-like structure, with a root at the top and organizational units nested under the organization root. Each account can be added directly to the root, or placed in one of the OUs in the hierarchy. For more information, see AWS Organizations terminology and concepts in the AWS Organizations User Guide.
When you share an AMI with an organization or an OU, all of the children accounts gain access to the AMI. For example, in the following diagram, the AMI is shared with a top-level OU (indicated by the arrow at the number 1). All of the OUs and accounts that are nested underneath that top- level OU (indicated by the dotted line at number 2) also have access to the AMI. The accounts in the organization and OU outside the dotted line (indicated by the number 3) do not have access to the AMI because they are not children of the OU that the AMI is shared with.

Topics
- Considerations
- Get the ARN of an organization or organizational unit
- Allow organizations and OUs to use a KMS key
- Manage AMI sharing with an organization or OU Considerations Consider the following when sharing AMIs with specific organizations or organizational units.
- Ownership – To share an AMI, your AWS account must own the AMI.
- Sharing limits – The AMI owner can share an AMI with any organization or OU, including organizations and OUs that they're not a member of.
For the maximum number of entities to which an AMI can be shared within a Region, see the Amazon EC2 service quotas.

- Tags – You can't share user-defined tags (tags that you attach to an AMI). When you share an AMI, your user-defined tags are not available to any AWS account in an organization or OU with which the AMI is shared.
- ARN format – When you specify an organization or OU in a command, make sure to use the correct ARN format. You'll get an error if you specify only the ID, for example, if you specify only o-123example or ou-1234-5example.
Correct ARN formats:
- Organization ARN: arn:aws:organizations::111122223333:organization/organization-id
- OU ARN: arn:aws:organizations::111122223333:ou/organization-id/ou-id Where:
- 111122223333 is an example of the 12-digit account ID for the management account. If you don't know the management account number, you can describe the organization or the organizational unit to get the ARN, which includes the management account number. For more information, see Get the ARN of an organization or organizational unit.
- organization-id is the organization ID, for example, o-123example.
- ou-id is the organizational unit ID, for example, ou-1234-5example.
For more information about the format of ARNs, see Amazon Resource Names (ARNs) in the IAM User Guide.
- Encryption and keys – You can share AMIs that are backed by unencrypted and encrypted snapshots.
- The encrypted snapshots must be encrypted with a customer managed key. You can't share AMIs that are backed by snapshots that are encrypted with the default AWS managed key.
- If you share an AMI that is backed by encrypted snapshots, you must allow the organizations or OUs to use the customer managed keys that were used to encrypt the snapshots. For more information, see Allow organizations and OUs to use a KMS key.
- Region – AMIs are a Regional resource. When you share an AMI, it is available only in the Region from which you shared it. To make an AMI available in a different Region, copy the AMI to the Region and then share it. For more information, see Copy an Amazon EC2 AMI.
- Usage – When you share an AMI, users can only launch instances from the AMI. They can't delete, share, or modify it. However, after they have launched an instance using your AMI, they can then create an AMI from the instance they launched.

- Billing – You are not billed when your AMI is used by other AWS accounts to launch instances.
The accounts that launch instances using the AMI are billed for the instances that they launch.
### Get the ARN of an organization or organizational unit The organization and the organizational unit ARNs contain the 12-digit management account number. If you don't know the management account number, you can describe the organization and the organizational unit to get the ARN for each. In the following examples, 123456789012 is the account ID of the management account.
Required permissions Before you can get the ARNs, you must have the permission to describe organizations and organizational units. The following policy provides the necessary permission.
JSON { "Version":"2012-10-17", "Statement": [ { "Effect": "Allow", "Action": [ "organizations:Describe*"
            ], "Resource": "*"
        } ]
} AWS CLI To get the ARN of an organization Use the describe-organization command. Add the --query option to return only the organization ARN. aws organizations describe-organization --query 'Organization.Arn'

The following is example output.
"arn:aws:organizations::123456789012:organization/o-1234567abc"
To get the ARN of an organizational unit Use the describe-organizational-unit command. Use the --query parameter to return only the organizational unit ARN. aws organizations describe-organizational-unit \ --organizational-unit-id ou-a123-b4567890 \ --query 'OrganizationalUnit.Arn'
The following is example output.
"arn:aws:organizations::123456789012:ou/o-1234567abc/ou-a123-b4567890"
PowerShell To get the ARN of an organization Use the Get-ORGOrganization cmdlet.
(Get-ORGOrganization).Arn The following is example output. arn:aws:organizations::123456789012:organization/o-1234567abc To get the ARN of an organizational unit Use the Get-ORGOrganizationalUnit cmdlet.
(Get-ORGOrganizationalUnit -OrganizationalUnitId "ou-a123-b4567890").Arn The following is example output. arn:aws:organizations::123456789012:ou/o-1234567abc/ou-a123-b4567890

### Allow organizations and OUs to use a KMS key If you share an AMI that is backed by encrypted snapshots, you must also allow the organizations or organizational units (OUs) to use the KMS keys that were used to encrypt the snapshots.
Note The encrypted snapshots must be encrypted with a customer managed key. You can't share AMIs that are backed by snapshots that are encrypted with the default AWS managed key.
To control access to the KMS key, in the key policy you can use the aws:PrincipalOrgID and aws:PrincipalOrgPaths condition keys to allow only specific principals permission to the specified actions. A principal can be a user, IAM role, federated user, or AWS account root user.
The condition keys are used as follows:
- aws:PrincipalOrgID – Allows any principal belonging to the organization represented by the specified ID.
- aws:PrincipalOrgPaths – Allows any principal belonging to the OUs represented by the specified paths.
To give an organization (including the OUs and accounts that belong to it) permission to use a KMS key, add the following statement to the key policy.
{ "Sid": "Allow access for organization root", "Effect": "Allow", "Principal": "*", "Action": [ "kms:Describe*", "kms:List*", "kms:Get*", "kms:Encrypt", "kms:Decrypt", "kms:ReEncrypt*", "kms:GenerateDataKey*", "kms:CreateGrant"
    ], "Resource": "*",

    "Condition": { "StringEquals": { "aws:PrincipalOrgID": "o-123example"
        } } } To give specific OUs (and the accounts that belong to it) permission to use a KMS key, you can use a policy similar to the following example.
{ "Sid": "Allow access for specific OUs and their descendants", "Effect": "Allow", "Principal": "*", "Action": [ "kms:Describe*", "kms:List*", "kms:Get*", "kms:Encrypt", "kms:Decrypt", "kms:ReEncrypt*", "kms:GenerateDataKey*", "kms:CreateGrant"
        ], "Resource": "*", "Condition": { "StringEquals": { "aws:PrincipalOrgID": "o-123example"
            }, "ForAnyValue:StringLike": { "aws:PrincipalOrgPaths": [ "o-123example/r-ab12/ou-ab12-33333333/*", "o-123example/r-ab12/ou-ab12-22222222/*"
                ]
            } } } For more example condition statements, see aws:PrincipalOrgID and aws:PrincipalOrgPaths in the IAM User Guide.
For information about cross-account access, see Allowing users in other accounts to use a KMS key in the AWS Key Management Service Developer Guide.

### Manage AMI sharing with an organization or OU You can manage AMI sharing with organizations and organization units (OU) to control whether they can launch Amazon EC2 instances.
#### View the organizations and OUs with which an AMI is shared You can find the organizations and OUs with which you've shared your AMI.
Console To check with which organizations and OUs you've shared your AMI
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose AMIs.
3. Select your AMI in the list, choose the Permissions tab, and scroll down to Shared organizations/OUs.
To find AMIs that are shared with you, see Find shared AMIs to use for Amazon EC2 instances.
AWS CLI To check with which organizations and OUs you've shared your AMI Use the describe-image-attribute command with the launchPermission attribute. aws ec2 describe-image-attribute \ --image-id ami-0abcdef1234567890 \ --attribute launchPermission The following is an example response.
{ "ImageId": "ami-0abcdef1234567890", "LaunchPermissions": [ { "OrganizationalUnitArn": "arn:aws:organizations::111122223333:ou/ o-123example/ou-1234-5example"
        }

    ]
} PowerShell To check with which organizations and OUs you've shared your AMI Use the Get-EC2ImageAttribute cmdlet.
Get-EC2ImageAttribute `
    -ImageId ami-0abcdef1234567890 `
    -Attribute launchPermission
#### Share an AMI with an organization or OU You can share an AMI with an organization or OU.
Note You do not need to share the Amazon EBS snapshots that an AMI references in order to share the AMI. Only the AMI itself needs to be shared, and the system automatically provides the instance with access to the referenced EBS snapshots for the launch. However, you do need to share the KMS keys used to encrypt snapshots that the AMI references. For more information, see Allow organizations and OUs to use a KMS key.
Console To share an AMI with an organization or an OU
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose AMIs.
3. Select your AMI in the list, and then choose Actions, Edit AMI permissions.
4. Under AMI availability, choose Private.
5. Next to Shared organizations/OUs, choose Add organization/OU ARN.
6. For Organization/OU ARN, enter the organization ARN or OU ARN with which you want to share the AMI, and then choose Share AMI. Note that you must specify the full ARN, not just the ID.

To share this AMI with multiple organizations or OUs, repeat this step until you have added all of the required organizations or OUs.
7. Choose Save changes when you're done.
8. (Optional) To view the organizations or OUs with which you have shared the AMI, select the AMI in the list, choose the Permissions tab, and scroll down to Shared organizations/ OUs. To find AMIs that are shared with you, see Find shared AMIs to use for Amazon EC2 instances.
AWS CLI To share an AMI with an organization Use the modify-image-attribute command to grant launch permissions for the specified AMI to the specified organization. aws ec2 modify-image-attribute \ --image-id ami-0abcdef1234567890 \ --launch-permission "Add=[{OrganizationArn=arn:aws:organizations::123456789012:organization/ o-123example}]"
To share an AMI with an OU The modify-image-attribute command grants launch permissions for the specified AMI to the specified OU. Note that you must specify the full ARN, not just the ID. aws ec2 modify-image-attribute \ --image-id ami-0abcdef1234567890 \ --launch-permission "Add=[{OrganizationalUnitArn=arn:aws:organizations::123456789012:ou/o-123example/ ou-1234-5example}]"
PowerShell Use the Edit-EC2ImageAttribute command (Tools for Windows PowerShell) to share an AMI as shown in the following examples.
To share an AMI with an organization or an OU

The following command grants launch permissions for the specified AMI to the specified organization.
Edit-EC2ImageAttribute `
    -ImageId ami-0abcdef1234567890 `
    -Attribute launchPermission `
    -OperationType add `
    -OrganizationArn "arn:aws:organizations::123456789012:organization/o-123example"
To stop sharing an AMI with an organization or OU The following command removes launch permissions for the specified AMI from the specified organization:
Edit-EC2ImageAttribute `
    -ImageId ami-0abcdef1234567890 `
    -Attribute launchPermission `
    -OperationType remove `
    -OrganizationArn "arn:aws:organizations::123456789012:organization/o-123example"
To stop sharing an AMI with all organizations, OUs, and AWS accounts The following command removes all public and explicit launch permissions from the specified AMI. Note that the owner of the AMI always has launch permissions and is therefore unaffected by this command.
Reset-EC2ImageAttribute `
    -ImageId ami-0abcdef1234567890 `
    -Attribute launchPermission
#### Stop sharing an AMI with an organization or OU You can stop sharing an AMI with an organization or OU.
Note You can't stop sharing an AMI with a specific account if it's in an organization or OU with which an AMI is shared. If you try to stop sharing the AMI by removing launch permissions

for the account, Amazon EC2 returns a success message. However, the AMI continues to be shared with the account.
Console To stop sharing an AMI with an organization or OU
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose AMIs.
3. Select your AMI in the list, and then choose Actions, Edit AMI permissions.
4. Under Shared organizations/OUs, select the organizations or OUs with which you want to stop sharing the AMI, and then choose Remove selected.
5. Choose Save changes when you're done.
6. (Optional) To confirm that you have stopped sharing the AMI with the organizations or OUs, select the AMI in the list, choose the Permissions tab, and scroll down to Shared organizations/OUs.
AWS CLI To stop sharing an AMI with an organization or OU Use the modify-image-attribute command. This example removes launch permissions for the specified AMI from the specified organization. aws ec2 modify-image-attribute \ --image-id ami-0abcdef1234567890 \ --launch-permission "Remove=[{OrganizationArn=arn:aws:organizations::123456789012:organization/ o-123example}]"
To stop sharing an AMI with all organizations, OUs, and AWS accounts Use the reset-image-attribute command. This example removes all public and explicit launch permissions from the specified AMI. Note that the owner of the AMI always has launch permissions and is therefore unaffected by this command. aws ec2 reset-image-attribute \

    --image-id ami-0abcdef1234567890 \ --attribute launchPermission PowerShell To stop sharing an AMI with an organization or OU Use the Edit-EC2ImageAttribute cmdlet. This example removes launch permissions for the specified AMI from the specified organization.
Edit-EC2ImageAttribute `
    -ImageId ami-0abcdef1234567890 `
    -Attribute launchPermission `
    -OperationType remove `
    -OrganizationArn "arn:aws:organizations::123456789012:organization/o-123example"
To stop sharing an AMI with all organizations, OUs, and AWS accounts Use the Reset-EC2ImageAttribute cmdlet. This example removes all public and explicit launch permissions from the specified AMI. Note that the owner of the AMI always has launch permissions and is therefore unaffected by this command.
Reset-EC2ImageAttribute `
    -ImageId ami-0abcdef1234567890 `
    -Attribute LaunchPermission
## Share an AMI with specific AWS accounts You can share an AMI with specific AWS accounts without making the AMI public. All you need are the AWS account IDs.
An AWS account ID is a 12-digit number, such as 012345678901, that uniquely identifies an AWS account. For more information, see View AWS account identifiers in the AWS Account Management Reference Guide.
Considerations Consider the following when sharing AMIs with specific AWS accounts.
- Ownership – To share an AMI, your AWS account must own the AMI.

- Sharing limits – For the maximum number of entities to which an AMI can be shared within a Region, see the Amazon EC2 service quotas.
- Tags – You can't share user-defined tags (tags that you attach to an AMI). When you share an AMI, your user-defined tags are not available to any AWS account that the AMI is shared with.
- Snapshots – You do not need to share the Amazon EBS snapshots that an AMI references in order to share the AMI. You can share only the AMI itself; the system provides the instance access to the referenced EBS snapshots for the launch. However, you must share any KMS keys used to encrypt snapshots that an AMI references. For more information, see Share an Amazon EBS snapshot in the Amazon EBS User Guide.
- Encryption and keys – You can share AMIs that are backed by unencrypted and encrypted snapshots.
- The encrypted snapshots must be encrypted with a KMS key. You can't share AMIs that are backed by snapshots that are encrypted with the default AWS managed key.
- If you share an AMI that is backed by encrypted snapshots, you must allow the AWS accounts to use the KMS keys that were used to encrypt the snapshots. For more information, see Allow organizations and OUs to use a KMS key. To set up the key policy that you need to launch Auto Scaling instances when you use a customer managed key for encryption, see Required AWS KMS key policy for use with encrypted volumes in the Amazon EC2 Auto Scaling User Guide.
- Region – AMIs are a Regional resource. When you share an AMI, it is only available in that Region.
To make an AMI available in a different Region, copy the AMI to the Region and then share it. For more information, see Copy an Amazon EC2 AMI.
- Usage – When you share an AMI, users can only launch instances from the AMI. They can't delete, share, or modify it. However, after they have launched an instance using your AMI, they can then create an AMI from their instance.
- Copying shared AMIs – If users in another account want to copy a shared AMI, you must grant them read permissions for the storage that backs the AMI. For more information, see Cross- account copying.
- Billing – You are not billed when your AMI is used by other AWS accounts to launch instances.
The accounts that launch instances using the AMI are billed for the instances that they launch.
Console To grant explicit launch permissions
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.

2. In the navigation pane, choose AMIs.
3. Select your AMI in the list, and then choose Actions, Edit AMI permissions.
4. Choose Private.
5. Under Shared accounts, choose Add account ID.
6. For AWS account ID, enter the AWS account ID with which you want to share the AMI, and then choose Share AMI.
To share this AMI with multiple accounts, repeat Steps 5 and 6 until you have added all the required account IDs.
7. Choose Save changes when you are done.
8. (Optional) To view the AWS account IDs with which you have shared the AMI, select the AMI in the list, and choose the Permissions tab. To find AMIs that are shared with you, see Find shared AMIs to use for Amazon EC2 instances.
AWS CLI Use the modify-image-attribute command to share an AMI as shown in the following examples.
To grant explicit launch permissions The following example grants launch permissions for the specified AMI to the specified AWS account. aws ec2 modify-image-attribute \ --image-id ami-0abcdef1234567890 \ --launch-permission "Add=[{UserId=123456789012}]"
To remove launch permissions for an account The following example removes launch permissions for the specified AMI from the specified AWS account. aws ec2 modify-image-attribute \ --image-id ami-0abcdef1234567890 \ --launch-permission "Remove=[{UserId=123456789012}]"
To remove all launch permissions

The following example removes all public and explicit launch permissions from the specified AMI. Note that the owner of the AMI always has launch permissions and is therefore unaffected by this command. aws ec2 reset-image-attribute \ --image-id ami-0abcdef1234567890 \ --attribute launchPermission PowerShell Use the Edit-EC2ImageAttribute command (Tools for Windows PowerShell) to share an AMI as shown in the following examples.
To grant explicit launch permissions The following example grants launch permissions for the specified AMI to the specified AWS account.
Edit-EC2ImageAttribute `
    -ImageId ami-0abcdef1234567890 `
    -Attribute launchPermission `
    -OperationType add `
    -UserId "123456789012"
To remove launch permissions for an account The following example removes launch permissions for the specified AMI from the specified AWS account.
Edit-EC2ImageAttribute `
    -ImageId ami-0abcdef1234567890 `
    -Attribute launchPermission -OperationType remove `
    -UserId "123456789012"
To remove all launch permissions The following exaple removes all public and explicit launch permissions from the specified AMI.
Note that the owner of the AMI always has launch permissions and is therefore unaffected by this command.
Reset-EC2ImageAttribute `

    -ImageId ami-0abcdef1234567890 `
    -Attribute launchPermission
## Cancel having an AMI shared with your AWS account An Amazon Machine Image (AMI) can be shared with specific AWS accounts by adding the accounts to the AMI's launch permissions. If an AMI has been shared with your AWS account and you no longer want it shared with your account, you can remove your account from the AMI's launch permissions. You do this by running the cancel-image-launch-permission AWS CLI command. When running this command, your AWS account is removed from the launch permissions for the specified AMI. To find the AMIs that are shared with your AWS account, see Find shared AMIs to use for Amazon EC2 instances.
You might cancel having an AMI shared with your account, for example, to reduce the likelihood of launching an instance with an unused or deprecated AMI that was shared with you. When you cancel having an AMI shared with your account, it no longer appears in any AMI lists in the EC2 console or in the output for describe-images.
Topics
- Limitations
- Cancel having an AMI shared with your account
### Limitations
- You can remove your account from the launch permissions of an AMI that is shared with your AWS account only. You can't use cancel-image-launch-permission to remove your account from the launch permissions of an AMI shared with an organization or organizational unit (OU) or to remove access to public AMIs.
- You can't permanently remove your account from the launch permissions of an AMI. An AMI owner can share an AMI with your account again.
- AMIs are a Regional resource. When running cancel-image-launch-permission, you must specify the Region in which the AMI is located. Either specify the Region in the command, or use the AWS_DEFAULT_REGION environment variable.
- Only the AWS CLI and SDKs support removing your account from the launch permissions of an AMI. The EC2 console does not currently support this action.

### Cancel having an AMI shared with your account Note After you cancel having an AMI shared with your account, you can't undo it. To regain access to the AMI, the AMI owner must share it with your account.
AWS CLI To cancel having an AMI shared with your account Use the cancel-image-launch-permission command. aws ec2 cancel-image-launch-permission \ --image-id ami-0abcdef1234567890 \ --region us-east-1 PowerShell To cancel having an AMI shared with your account Use the Stop-EC2ImageLaunchPermission cmdlet.
Stop-EC2ImageLaunchPermission `
    -ImageId ami-0abcdef1234567890 `
    -Region us-east-1
## Recommendations for creating shared Linux AMIs Use the following guidelines to reduce the attack surface and improve the reliability of the AMIs you create.
Important No list of security guidelines can be exhaustive. Build your shared AMIs carefully and take time to consider where you might expose sensitive data.
Contents

- Disable password-based remote logins for the root user
- Disable local root access
- Remove SSH host key pairs
- Install public key credentials
- Disable sshd DNS checks (optional)
- Remove sensitive data If you are building AMIs for AWS Marketplace, see Best practices for building AMIs in the AWS Marketplace Seller Guide for guidelines, policies, and best practices.
### Disable password-based remote logins for the root user Using a fixed root password for a public AMI is a security risk that can quickly become known. Even relying on users to change the password after the first login opens a small window of opportunity for potential abuse.
To solve this problem, disable password-based remote logins for the root user.
To disable password-based remote logins for the root user
1. Open the /etc/ssh/sshd_config file with a text editor and locate the following line:
#PermitRootLogin yes
2. Change the line to:
PermitRootLogin without-password The location of this configuration file might differ for your distribution, or if you are not running OpenSSH. If this is the case, consult the relevant documentation.
### Disable local root access When you work with shared AMIs, a best practice is to disable direct root logins. To do this, log into your running instance and issue the following command:
[ec2-user ~]$ sudo passwd -l root

Note This command does not impact the use of sudo.
### Remove SSH host key pairs If you plan to share an AMI derived from a public AMI, remove the existing SSH host key pairs located in /etc/ssh. This forces SSH to generate new unique SSH key pairs when someone launches an instance using your AMI, improving security and reducing the likelihood of "man-in- the-middle" attacks.
Remove all of the following key files that are present on your system.
- ssh_host_dsa_key
- ssh_host_dsa_key.pub
- ssh_host_key
- ssh_host_key.pub
- ssh_host_rsa_key
- ssh_host_rsa_key.pub
- ssh_host_ecdsa_key
- ssh_host_ecdsa_key.pub
- ssh_host_ed25519_key
- ssh_host_ed25519_key.pub You can securely remove all of these files with the following command.
[ec2-user ~]$ sudo shred -u /etc/ssh/*_key /etc/ssh/*_key.pub Warning Secure deletion utilities such as shred might not remove all copies of a file from your storage media. Hidden copies of files may be created by journalling file systems (including Amazon Linux default ext4), snapshots, backups, RAID, and temporary caching. For more information, see the shred documentation.

Important If you forget to remove the existing SSH host key pairs from your public AMI, our routine auditing process notifies you and all customers running instances of your AMI of the potential security risk. After a short grace period, we mark the AMI private.
### Install public key credentials After configuring the AMI to prevent logging in using a password, you must make sure users can log in using another mechanism.
Amazon EC2 allows users to specify a public-private key pair name when launching an instance.
When a valid key pair name is provided to the RunInstances API call (or through the command line API tools), the public key (the portion of the key pair that Amazon EC2 retains on the server after a call to CreateKeyPair or ImportKeyPair) is made available to the instance through an HTTP query against the instance metadata.
To log in through SSH, your AMI must retrieve the key value at boot and append it to / root/.ssh/authorized_keys (or the equivalent for any other user account on the AMI). Users can launch instances of your AMI with a key pair and log in without requiring a root password.
Many distributions, including Amazon Linux and Ubuntu, use the cloud-init package to inject public key credentials for a configured user. If your distribution does not support cloud-init, you can add the following code to a system start-up script (such as /etc/rc.local) to pull in the public key you specified at launch for the root user.
Note In the following example, the IP address http://169.254.169.254/ is a link-local address and is valid only from the instance.
IMDSv2 if [ ! -d /root/.ssh ] ; then mkdir -p /root/.ssh chmod 700 /root/.ssh fi
# Fetch public key using HTTP

TOKEN=`curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata- token-ttl-seconds: 21600"` \ && curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta- data/public-keys/0/openssh-key > /tmp/my-key if [ $? -eq 0 ] ; then cat /tmp/my-key >> /root/.ssh/authorized_keys chmod 700 /root/.ssh/authorized_keys rm /tmp/my-key fi IMDSv1 if [ ! -d /root/.ssh ] ; then mkdir -p /root/.ssh chmod 700 /root/.ssh fi
# Fetch public key using HTTP curl http://169.254.169.254/latest/meta-data/public-keys/0/openssh-key > /tmp/my-key if [ $? -eq 0 ] ; then cat /tmp/my-key >> /root/.ssh/authorized_keys chmod 700 /root/.ssh/authorized_keys rm /tmp/my-key fi This can be applied to any user; you do not need to restrict it to the root user.
Note Rebundling an instance based on this AMI includes the key with which it was launched. To prevent the key's inclusion, you must clear out (or delete) the authorized_keys file or exclude this file from rebundling.
### Disable sshd DNS checks (optional)
Disabling sshd DNS checks slightly weakens your sshd security. However, if DNS resolution fails, SSH logins still work. If you do not disable sshd checks, DNS resolution failures prevent all logins.
To disable sshd DNS checks
1. Open the /etc/ssh/sshd_config file with a text editor and locate the following line:

#UseDNS yes
2. Change the line to:
UseDNS no Note The location of this configuration file can differ for your distribution or if you are not running OpenSSH. If this is the case, consult the relevant documentation.
### Remove sensitive data We recommend against storing sensitive data or software on any AMI that you share. Users who launch a shared AMI might be able to rebundle it and register it as their own. Follow these guidelines to help you to avoid some easily overlooked security risks:
- We recommend using the --exclude directory option on ec2-bundle-vol to skip any directories and subdirectories that contain secret information that you would not like to include in your bundle. In particular, exclude all user-owned SSH public/private key pairs and SSH authorized_keys files when bundling the image. The Amazon public AMIs store these in /root/.ssh for the root user, and /home/user_name/.ssh/ for regular users. For more information, see ec2-bundle-vol.
- Always delete the shell history before bundling. If you attempt more than one bundle upload in the same AMI, the shell history contains your access key. The following example should be the last command you run before bundling from within the instance.
[ec2-user ~]$ shred -u ~/.*history Warning The limitations of shred described in the warning above apply here as well.
Be aware that bash writes the history of the current session to the disk on exit. If you log out of your instance after deleting ~/.bash_history, and then log back in, you will
