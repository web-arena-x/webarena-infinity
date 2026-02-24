# Store instance launch parameters in Amazon EC2 launch templates

Source: apps/user-manuals/aws/ec2-ug.pdf

---

  "resources": [ { "ARN": "arn:aws:ec2:us-east-1:123456789012:capacity-reservation/cr-12345678", "accountId": "123456789012", "type": "AWS::EC2::CapacityReservation"
    } ], "eventType": "AwsServiceEvent", "recipientAccountId": "123456789012", "serviceEventDetails": { "capacityReservationId": "cr-12345678", "capacityReservationState": "expired"
      } }
# Store instance launch parameters in Amazon EC2 launch templates templates You can use an Amazon EC2 launch template to store instance launch parameters so that you don't have to specify them every time you launch an Amazon EC2 instance. For example, you can create a launch template that stores the AMI ID, instance type, and network settings that you typically use to launch instances. When you launch an instance using the Amazon EC2 console, an AWS SDK, or a command line tool, you can specify the launch template instead of entering the parameters again.
For each launch template, you can create one or more numbered launch template versions.
Each version can have different launch parameters. When you launch an instance from a launch template, you can use any version of the launch template. If you don't specify a version, the default version is used. You can set any version of the launch template as the default version—by default, it's the first version of the launch template.
The following diagram shows a launch template with three versions. The first version specifies the instance type, AMI ID, subnet, and key pair to use to launch the instance. The second version is based on the first version and also specifies a security group for the instance. The third version uses different values for some of the parameters. Version 2 is set as the default version. If you launched an instance from this launch template, the launch parameters from version 2 would be used if no other version were specified.

Contents
- Restrictions for Amazon EC2 launch templates
- IAM permissions required for Amazon EC2 launch templates
- Use Amazon EC2 launch templates to control launching Amazon EC2 instances
- Create an Amazon EC2 launch template
- Modify a launch template (manage launch template versions)
- Delete a launch template or a launch template version
## Restrictions for Amazon EC2 launch templates The following restrictions apply to launch templates and launch template versions:
- Quotas – To view the quotas for your launch templates and launch template versions, open the Service Quotas console or use the  list-service-quotas AWS CLI command. Each AWS account can have up to a maximum of 5,000 launch templates per Region and up to 10,000 versions per launch template. Your accounts might have different quotas based on their age and usage history.
- Parameters are optional – Launch template parameters are optional. However, you must ensure that your instance launch request includes all required parameters. For example, if your launch template does not include an AMI ID, you must specify an AMI ID when launching an instance with this launch template.
- Parameters not validated – Launch template parameters are not fully validated when you create the launch template. If you specify incorrect values or use unsupported parameter combinations, instances will fail to launch using this launch template. To avoid issues, make sure to specify

correct values and use supported parameter combinations. For example, to launch an instance in a placement group, you must specify a supported instance type.
- Tags – You can tag a launch template, but you can't tag a launch template version.
- Immutable – Launch templates are immutable. To modify a launch template, you must create a new version of the launch template.
- Version numbers – Launch template versions are numbered in the order in which they are created. When you create a launch template version, you can't specify the version number yourself.
## IAM permissions required for Amazon EC2 launch templates You can use IAM permissions to control whether users can list, view, create, or delete launch templates or launch template versions.
Important You can't use resource-level permissions to restrict the resources that users can specify in a launch template when they create a launch template or launch template version.
Therefore, make sure that only trusted administrators are granted permission to create launch templates and launch template versions.
You must grant anyone that will use a launch template the permissions required to create and access the resources that are specified in the launch template. For example:
- To launch an instance from a shared private Amazon Machine Image (AMI), the user must have launch permission for the AMI.
- To create EBS volumes with tags from existing snapshots, the user must have read access to the snapshots, and permissions to create and tag volumes.
Contents
- ec2:CreateLaunchTemplate
- ec2:DescribeLaunchTemplates
- ec2:DescribeLaunchTemplateVersions
- ec2:DeleteLaunchTemplate

- Control versioning permissions
- Control access to tags on launch templates
### ec2:CreateLaunchTemplate To create a launch template in the console or by using the APIs, the principal must have the ec2:CreateLaunchTemplate permission in an IAM policy. Whenever possible, use tags to help you control access to the launch templates in your account.
For example, the following IAM policy statement gives the principal permission to create launch templates only if the template uses the specified tag (purpose=testing).
{ "Sid": "IAMPolicyForCreatingTaggedLaunchTemplates", "Action": "ec2:CreateLaunchTemplate", "Effect": "Allow", "Resource": "*", "Condition": { "StringEquals": { "aws:ResourceTag/purpose": "testing"
        } } } Principals who create launch templates might need some related permissions, such as:
- ec2:CreateTags – To add tags to the launch template during the CreateLaunchTemplate operation, the CreateLaunchTemplate caller must have the ec2:CreateTags permission in an IAM policy.
- ec2:RunInstances – To launch EC2 instances from the launch template that they created, the principal must also have the ec2:RunInstances permission in an IAM policy.
For resource-creating actions that apply tags, users must have the ec2:CreateTags permission.
The following IAM policy statement uses the ec2:CreateAction condition key to allow users to create tags only in the context of CreateLaunchTemplate. Users cannot tag existing launch templates or any other resources. For more information, see Grant permission to tag Amazon EC2 resources during creation.
{

    "Sid": "IAMPolicyForTaggingLaunchTemplatesOnCreation", "Action": "ec2:CreateTags", "Effect": "Allow", "Resource": "arn:aws:ec2:us-east-1:111122223333:launch-template/*", "Condition": { "StringEquals": { "ec2:CreateAction": "CreateLaunchTemplate"
        } } } The IAM user who creates a launch template doesn't automatically have permission to use the launch template that they created. Like any other principal, the launch template creator needs to get permission through an IAM policy. If an IAM user wants to launch an EC2 instance from a launch template, they must have the ec2:RunInstances permission. When granting these permissions, you can specify that users can only use launch templates with specific tags or specific IDs. You can also control the AMI and other resources that anyone using launch templates can reference and use when launching instances by specifying resource-level permissions for the RunInstances call. For example policies, see Launch templates.
### ec2:DescribeLaunchTemplates To list and view launch templates in the account, the principal must have the ec2:DescribeLaunchTemplates permission in an IAM policy. Because Describe actions do not support resource-level permissions, you must specify them without conditions and the value of the resource element in the policy must be "*".
For example, the following IAM policy statement gives the principal permission to list and view all launch templates in the account.
{ "Sid": "IAMPolicyForDescribingLaunchTemplates", "Action": "ec2:DescribeLaunchTemplates", "Effect": "Allow", "Resource": "*"
}

### ec2:DescribeLaunchTemplateVersions Principals who list and view launch templates should also have the ec2:DescribeLaunchTemplateVersions permission to retrieve the entire set of attributes that make up the launch templates.
To list and view launch template versions in the account, the principal must have the ec2:DescribeLaunchTemplateVersions permission in an IAM policy. Because Describe actions do not support resource-level permissions, you must specify them without conditions and the value of the resource element in the policy must be "*".
For example, the following IAM policy statement gives the principal permission to list and view all launch template versions in the account.
{ "Sid": "IAMPolicyForDescribingLaunchTemplateVersions", "Effect": "Allow", "Action": "ec2:DescribeLaunchTemplateVersions", "Resource": "*"
}
### ec2:DeleteLaunchTemplate Important Use caution when giving principals permission to delete a resource. Deleting a launch template might cause a failure in an AWS resource that relies on the launch template.
To delete a launch template, the principal must have the ec2:DeleteLaunchTemplate permission in an IAM policy. Whenever possible, use tag-based condition keys to limit the permissions.
For example, the following IAM policy statement gives the principal permission to delete launch templates only if the template has the specified tag (purpose=testing).
{ "Sid": "IAMPolicyForDeletingLaunchTemplates", "Action": "ec2:DeleteLaunchTemplate", "Effect": "Allow", "Resource": "*",

    "Condition": { "StringEquals": { "aws:ResourceTag/purpose": "testing"
        } } } Alternatively, you can use ARNs to identify the launch template that the IAM policy applies to.
A launch template has the following ARN.
"Resource": "arn:aws:ec2:us-east-1:111122223333:launch-template/lt-09477bcd97b0d310e"
You can specify multiple ARNs by enclosing them in a list, or you can specify a Resource value of "*" without the Condition element to allow the principal to delete any launch template in the account.
### Control versioning permissions For trusted administrators, you can grant access for creating and deleting versions of a launch template, and for changing the default version of a launch template, by using IAM policies similar to the following examples.
Important Be cautious when giving principals permission to create launch template versions or modify launch templates.
- When you create a launch template version, you affect any AWS resources that allow Amazon EC2 to launch instances on your behalf with the Latest version.
- When you modify a launch template, you can change which version is the Default and therefore affect any AWS resources that allow Amazon EC2 to launch instances on your behalf with this modified version.
You also need to be cautious in how you handle AWS resources that interact with the Latest or Default launch template version, such as EC2 Fleet and Spot Fleet. When a different launch template version is used for Latest or Default, Amazon EC2 does not re-check user permissions for actions to be completed when launching new instances to fulfil the fleet's target capacity because there is no user interaction with the AWS

resource. By granting a user permission to call the CreateLaunchTemplateVersion and ModifyLaunchTemplate APIs, the user is effectively also granted the iam:PassRole permission if they point the fleet to a different launch template version that contains an instance profile (a container for an IAM role). It means that a user can potentially update a launch template to pass an IAM role to an instance even if they don't have the iam:PassRole permission. You can manage this risk by being careful when granting permissions to who can create and manage launch template versions.
#### ec2:CreateLaunchTemplateVersion To create a new version of a launch template, the principal must have the ec2:CreateLaunchTemplateVersion permission for the launch template in an IAM policy.
For example, the following IAM policy statement gives the principal permission to create launch template versions only if the version uses the specified tag (environment=production).
Alternatively, you can specify one or multiple launch template ARNs, or you can specify a Resource value of "*" without the Condition element to allow the principal to create versions of any launch template in the account.
{ "Sid": "IAMPolicyForCreatingLaunchTemplateVersions", "Action": "ec2:CreateLaunchTemplateVersion", "Effect": "Allow", "Resource": "*", "Condition": { "StringEquals": { "aws:ResourceTag/environment": "production"
        } } }
#### ec2:DeleteLaunchTemplateVersion Important As always, you should exercise caution when giving principals permission to delete a resource. Deleting a launch template version might cause a failure in an AWS resource that relies on the launch template version.

To delete a launch template version, the principal must have the ec2:DeleteLaunchTemplateVersion permission for the launch template in an IAM policy.
For example, the following IAM policy statement gives the principal permission to delete launch template versions only if the version uses the specified tag (environment=production).
Alternatively, you can specify one or multiple launch template ARNs, or you can specify a Resource value of "*" without the Condition element to allow the principal to delete versions of any launch template in the account.
{ "Sid": "IAMPolicyForDeletingLaunchTemplateVersions", "Action": "ec2:DeleteLaunchTemplateVersion", "Effect": "Allow", "Resource": "*", "Condition": { "StringEquals": { "aws:ResourceTag/environment": "production"
        } } }
#### ec2:ModifyLaunchTemplate To change the Default version that is associated with a launch template, the principal must have the ec2:ModifyLaunchTemplate permission for the launch template in an IAM policy.
For example, the following IAM policy statement gives the principal permission to modify launch templates only if the launch template uses the specified tag (environment=production).
Alternatively, you can specify one or multiple launch template ARNs, or you can specify a Resource value of "*" without the Condition element to allow the principal to modify any launch template in the account.
{ "Sid": "IAMPolicyForModifyingLaunchTemplates", "Action": "ec2:ModifyLaunchTemplate", "Effect": "Allow", "Resource": "*", "Condition": { "StringEquals": { "aws:ResourceTag/environment": "production"
        }

    } }
### Control access to tags on launch templates You can use condition keys to limit tagging permissions when the resource is a launch template.
For example, the following IAM policy allows removing only the tag with the temporary key from launch templates in the specified account and Region.
{ "Sid": "IAMPolicyForDeletingTagsOnLaunchTemplates", "Action": "ec2:DeleteTags", "Effect": "Allow", "Resource": "arn:aws:ec2:us-east-1:111122223333:launch-template/*", "Condition": { "ForAllValues:StringEquals": { "aws:TagKeys": ["temporary"]
        } } } For more information about conditions keys that you can use to control the tag keys and values that can be applied to Amazon EC2 resources, see Control access to specific tags.
## Use Amazon EC2 launch templates to control launching Amazon EC2 instances instances You can control the configuration of your Amazon EC2 instances by specifying that users can only launch instances if they use a launch template, and that they can only use a specific launch template. You can also control who can create, modify, describe, and delete launch templates and launch template versions.
### Use launch templates to control launch parameters A launch template can contain all or some of the parameters to configure an instance at launch.
However, when you launch an instance using a launch template, you can override parameters that are specified in the launch template. Or, you can specify additional parameters that are not in the launch template.

Note You can't remove launch template parameters during launch (for example, you can't specify a null value for the parameter). To remove a parameter, create a new version of the launch template without the parameter and use that version to launch the instance.
To launch instances, users must have permission to use the ec2:RunInstances action. Users must also have permissions to create or use the resources that are created or associated with the instance. You can use resource-level permissions for the ec2:RunInstances action to control the launch parameters that users can specify. Alternatively, you can grant users permissions to launch an instance using a launch template. This enables you to manage launch parameters in a launch template rather than in an IAM policy, and to use a launch template as an authorization vehicle for launching instances. For example, you can specify that users can only launch instances using a launch template, and that they can only use a specific launch template. You can also control the launch parameters that users can override in the launch template. For example policies, see Launch templates.
### Control the use of launch templates By default, users do not have permissions to work with launch templates. You can create a policy that grants users permissions to create, modify, describe, and delete launch templates and launch template versions. You can also apply resource-level permissions to some launch template actions to control a user's ability to use specific resources for those actions. For more information, see the following example policies: Example: Work with launch templates.
Take care when granting users permissions to use the ec2:CreateLaunchTemplate and ec2:CreateLaunchTemplateVersion actions. You can't use resource-level permissions to control which resources users can specify in the launch template. To restrict the resources that are used to launch an instance, ensure that you grant permissions to create launch templates and launch template versions only to appropriate administrators.
### Important security concerns when using launch templates with EC2 Fleet or Spot Fleet Fleet To use launch templates, you must grant your users permissions to create, modify, describe, and delete launch templates and launch template versions. You can control who can create launch templates and launch template versions by controlling access

to the ec2:CreateLaunchTemplate and ec2:CreateLaunchTemplateVersion actions. You can also control who can modify launch templates by controlling access to the ec2:ModifyLaunchTemplate action.
Important If an EC2 Fleet or Spot Fleet is configured to use the Latest or Default launch template version, the fleet is not aware if Latest or Default are later changed to point to a different launch template version. When a different launch template version is used for Latest or Default, Amazon EC2 does not re-check permissions for actions to be completed when launching new instances to fulfil the fleet's target capacity. This is an important consideration when granting permissions to who can create and manage launch template versions, particularly the ec2:ModifyLaunchTemplate action that allows a user to change the Default launch template version.
By granting a user permission to use the EC2 actions for the launch template APIs, the user is effectively also granted the iam:PassRole permission if they create or update an EC2 Fleet or Spot Fleet to point to a different launch template version that contains an instance profile (a container for an IAM role). It means that a user can potentially update a launch template to pass an IAM role to an instance even if they don't have the iam:PassRole permission. For more information and an example IAM policy, see Using an IAM role to grant permissions to applications running on Amazon EC2 instances in the IAM User Guide.
For more information, see Control the use of launch templates and Example: Work with launch templates.
## Create an Amazon EC2 launch template You can create an Amazon EC2 launch template by specifying your own values for the instance configuration parameters, or by getting the values from an existing launch template or Amazon EC2 instance.
You don't need to specify a value for every parameter in the launch template; you need only specify one instance configuration parameter to create a launch template. To indicate parameters that you choose not to specify, select Don't include in launch template when using the console.
When using a command line tool, don't include the parameters to indicate that you're choosing not to specify them in the launch template.

If you want to specify an AMI in the launch template, you can either select an AMI, or specify a Systems Manager parameter that will point to an AMI on instance launch.
When an instance is launched with a launch template, the values that are specified in the launch template are used to configure the corresponding instance parameters. If a value isn't specified in the launch template, then the default value for the corresponding instance parameter is used.
Tasks
- Create a launch template by specifying parameters
- Create a launch template from an existing launch template
- Create a launch template from an instance
- Use a Systems Manager parameter instead of an AMI ID
### Create a launch template by specifying parameters To create a launch template, you must specify the launch template name and at least one instance configuration parameter.
For a description of each parameter, see Reference for Amazon EC2 instance configuration parameters.
Console To create a launch template
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Launch Templates, and then choose Create launch template.
3. Under Launch template name and description, do the following: a.
For Launch template name, enter a descriptive name for the launch template. b.
For Template version description, provide a brief description of this version of the launch template. c.
To tag the launch template on creation, expand Template tags, choose Add new tag, and then enter a tag key and value pair. Choose Add new tag again for each additional tag to add.

Note To tag the resources that are created when an instance is launched, you must specify the tags under Resource tags. For more information, see Step 9 in this procedure.
4. Under Application and OS Images (Amazon Machine Image), you can either keep Don't include in launch template selected, or choose the operating system (OS) for the instance, and then choose an AMI. Alternatively, you can specify a Systems Manager parameter instead of specifying an AMI. For more information, see Use a Systems Manager parameter instead of an AMI ID.
An AMI is a template that contains the operating system and software required to launch an instance.
5. Under Instance type, you can either keep Don't include in launch template selected, or select an instance type, or specify instance attributes and let Amazon EC2 identify the instance types with those attributes.
Note Specifying instance attributes is supported only when the launch template is used by Auto Scaling groups, EC2 Fleet, and Spot Fleet to launch instances. For more information, see Create mixed instances group using attribute-based instance type selection and Specify attributes for instance type selection for EC2 Fleet or Spot Fleet.
If you plan to use the launch template in the launch instance wizard or with the RunInstances API, you can't specify instance type attributes.
The instance type determines the hardware configuration (CPU, memory, storage, and networking capacity) and size of the host computer used for an instance.
If you're not sure which instance type to choose, you can do the following:
- Choose Compare instance types to compare different instance types by the following attributes: number of vCPUs, architecture, amount of memory (GiB), amount of storage (GB), storage type, and network performance.

- Choose Get advice to get guidance and suggestions for instance types from the EC2 instance type finder. For more information, see Get recommendations from EC2 instance type finder.
Note Depending on when you created your account, you might be eligible to use Amazon EC2 under the Free Tier.
If your created your AWS account before July 15, 2025 and it's less than 12 months old, you can use Amazon EC2 under the Free Tier by selecting the t2.micro instance type, or the t3.micro instance type in Regions where t2.micro is unavailable. Be aware that when you launch a t3.micro instance, it defaults to Unlimited mode, which might incur additional charges based on CPU usage. If an instance type can be used under the Free Tier, it is labeled Free tier eligible.
If you created your AWS account on or after July 15, 2025, you can use t3.micro, t3.small, t4g.micro, t4g.small, c7i-flex.large, and m7i-flex.large instance types for 6 months or until your credits are used up.
For more information, see Free Tier benefits before and after July 15, 2025.
6. Under Key pair (login), for Key pair name, either keep Don't include in launch template selected, or choose an existing key pair, or create a new one.
7. Under Network settings, you can either keep Dont include in launch template selected, or you can specify values for the various network settings.
8. Under Configure storage, if you specified an AMI in the launch template, the AMI includes one or more volumes of storage, including the root volume (Volume 1 (AMI Root). You can optionally specify additional volumes to attach to the instance. To add a new volume, choose Add new volume.
9. Under Resource tags, to tag the resources that are created when an instance is launched, choose Add tag, and then enter a tag key and value pair. For Resource types, specify the resources to tag on creation. You can specify the same tag for all the resources, or specify different tags for different resources. Choose Add tag again for each additional tag to add.
You can specify tags for the following resources that are created when a launch template is used:
- Instances

- Volumes
- Elastic graphics
- Spot Instance requests
- Network interfaces Note To tag the launch template itself, you must specify the tags under Template tags.
For more information, see Step 3 in this procedure.
10. For Advanced details, expand the section to view the fields and optionally specify any additional parameters for your instance.
11. Use the Summary panel to review your launch template configuration. You can navigate to any section by choosing its link and then make any necessary changes.
12. When you're ready to create your launch template, choose Create launch template.
AWS CLI To create a launch template Use the create-launch-template command. aws ec2 create-launch-template \ --launch-template-name TemplateForWebServer \ --version-description WebVersion1 \ --tag-specifications 'ResourceType=launch- template,Tags=[{Key=purpose,Value=production}]' \ --launch-template-data file://template-data.json The following is example JSON that specifies the launch template data for the instance configuration. Save the JSON to a file and include it in the --launch-template-data parameter as shown in the example command.
{ "NetworkInterfaces": [{ "AssociatePublicIpAddress": true, "DeviceIndex": 0,

        "Ipv6AddressCount": 1, "SubnetId": "subnet-0abcdef1234567890"
    }], "ImageId": "ami-0abcdef1234567890", "InstanceType": "r5.4xlarge", "TagSpecifications": [{ "ResourceType": "instance", "Tags": [{ "Key":"Name", "Value":"webserver"
        }]
    }], "CpuOptions": { "CoreCount":4, "ThreadsPerCore":2 } } The following is example output.
{ "LaunchTemplate": { "LatestVersionNumber": 1, "LaunchTemplateId": "lt-01238c059e3466abc", "LaunchTemplateName": "TemplateForWebServer", "DefaultVersionNumber": 1, "CreatedBy": "arn:aws:iam::123456789012:root", "CreateTime": "2017-11-27T09:13:24.000Z"
    } } PowerShell To create a launch template Use the New-EC2LaunchTemplate cmdlet.
$launchTemplateData = [Amazon.EC2.Model.RequestLaunchTemplateData]@{ ImageId = 'ami-0abcdef1234567890'
    InstanceType = 'r5.4xlarge'
    NetworkInterfaces = @(

 [Amazon.EC2.Model.LaunchTemplateInstanceNetworkInterfaceSpecificationRequest]@{

            AssociatePublicIpAddress = $true DeviceIndex = 0 Ipv6AddressCount = 1 SubnetId = 'subnet-0abcdef1234567890'
        } )
    TagSpecifications = @( [Amazon.EC2.Model.LaunchTemplateTagSpecificationRequest]@{ ResourceType = 'instance'
            Tags = [Amazon.EC2.Model.Tag]@{ Key = 'Name'
                Value = 'webserver'
            } } )
    CpuOptions = [Amazon.EC2.Model.LaunchTemplateCpuOptionsRequest]@{ CoreCount = 4 ThreadsPerCore = 2 } } $tagSpecificationData = [Amazon.EC2.Model.TagSpecification]@{ ResourceType = 'launch-template'
    Tags = [Amazon.EC2.Model.Tag]@{ Key = 'purpose'
        Value = 'production'
    } } New-EC2LaunchTemplate -LaunchTemplateName 'TemplateForWebServer' `
    -VersionDescription 'WebVersion1' `
    -LaunchTemplateData $launchTemplateData `
    -TagSpecification $tagSpecificationData The following is example output.
CreatedBy            : arn:aws:iam::123456789012:root CreateTime           : 9/19/2023 16:57:55 DefaultVersionNumber : 1 LatestVersionNumber  : 1 LaunchTemplateId     : lt-01238c059eEXAMPLE LaunchTemplateName   : TemplateForWebServer Tags                 : {purpose}

### Create a launch template from an existing launch template You can clone an existing launch template and then adjust the parameters to create a new launch template. However, you can only do this when using the Amazon EC2 console. The AWS CLI does not support cloning a template. For a description of each parameter, see Reference for Amazon EC2 instance configuration parameters.
Console To create a launch template from an existing launch template
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Launch Templates, and then choose Create launch template.
3. For Launch template name, enter a descriptive name for the launch template.
4. For Template version description, provide a brief description of this version of the launch template.
5. To tag the launch template on creation, expand Template tags, choose Add new tag, and then enter a tag key and value pair.
6. Expand Source template, and for Launch template name choose a launch template on which to base the new launch template.
7. For Source template version, choose the launch template version on which to base the new launch template.
8. Adjust any launch parameters as required, and then choose Create launch template.
### Create a launch template from an instance You can clone the parameters of an existing Amazon EC2 instance and then adjust the parameters to create a launch template. For a description of each parameter, see Reference for Amazon EC2 instance configuration parameters.
Console To create a launch template from an instance
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Instances.

3. Select the instance, and choose Actions, Image and templates, Create template from instance.
4. Provide a name, description, and tags, and adjust the launch parameters as required.
Note When you create a launch template from an instance, the instance's network interface IDs and IP addresses are not included in the template.
5. Choose Create launch template.
AWS CLI You can use the AWS CLI to create a launch template from an existing instance by first getting the launch template data from an instance, and then creating a launch template using the launch template data.
To get launch template data from an instance
- Use the get-launch-template-data command and specify the instance ID. You can use the output as a base to create a new launch template or launch template version. By default, the output includes a top-level LaunchTemplateData object, which cannot be specified in your launch template data. Use the --query option to exclude this object. aws ec2 get-launch-template-data \ --instance-id i-0123d646e8048babc \ --query "LaunchTemplateData"
The following is example output.
    { "Monitoring": {}, "ImageId": "ami-8c1be5f6", "BlockDeviceMappings": [ { "DeviceName": "/dev/xvda", "Ebs": { "DeleteOnTermination": true } }

        ], "EbsOptimized": false, "Placement": { "Tenancy": "default", "GroupName": "", "AvailabilityZone": "us-east-1a"
        }, "InstanceType": "t2.micro", "NetworkInterfaces": [ { "Description": "", "NetworkInterfaceId": "eni-35306abc", "PrivateIpAddresses": [ { "Primary": true, "PrivateIpAddress": "10.0.0.72"
                    } ], "SubnetId": "subnet-7b16de0c", "Groups": [ "sg-7c227019"
                ], "Ipv6Addresses": [ { "Ipv6Address": "2001:db8:1234:1a00::123"
                    } ], "PrivateIpAddress": "10.0.0.72"
            } ]
    } You can write the output directly to a file, for example: aws ec2 get-launch-template-data \ --instance-id i-0123d646e8048babc \ --query "LaunchTemplateData" >> instance-data.json

To create a launch template using launch template data
- Use the create-launch-template command to create a launch template using the output from the previous procedure. For more information about creating a launch template using the AWS CLI, see Create a launch template by specifying parameters.
### Use a Systems Manager parameter instead of an AMI ID Instead of specifying an AMI ID in your launch templates, you can specify an AWS Systems Manager parameter. If the AMI ID changes, you can update the AMI ID in one place by updating the Systems Manager parameter in the Systems Manager Parameter Store. Parameters can also be shared with other AWS accounts. You can centrally store and manage AMI parameters in one account and share them with every other account that needs to reference them. By using a Systems Manager parameter, all your launch templates can be updated in a single action.
A Systems Manager parameter is a user-defined key-value pair that you create in the AWS Systems Manager Parameter Store. The Parameter Store provides a central place to store your application configuration values.
In the following diagram, the golden-ami parameter is first mapped to the original AMI ami- aabbccddeeffgghhi in the Parameter Store. In the launch template, the value for the AMI ID is golden-ami. When an instance is launched using this launch template, the AMI ID resolves to ami-aabbccddeeffgghhi. Later, the AMI is updated resulting in a new AMI ID. In the Parameter Store, the golden-ami parameter is mapped to the new ami-00112233445566778. The launch template remains unchanged. When an instance is launched using this launch template, the AMI ID resolves to the new ami-00112233445566778.

#### Systems Manager parameter format for AMI IDs Launch templates require that user-defined Systems Manager parameters adhere to the following format when used in place of an AMI ID:
- Parameter type: String
- Parameter data type: aws:ec2:image – This ensures that Parameter Store validates that the value you enter is in the proper format for an AMI ID.
For more information about creating a valid parameter for an AMI ID, see Creating Systems Manager parameters in the AWS Systems Manager User Guide.
#### Systems Manager parameter format in launch templates To use a Systems Manager parameter in place of an AMI ID in a launch template, you must use one of the following formats when specifying the parameter in the launch template:
To reference a public parameter:
- resolve:ssm:public-parameter To reference a parameter stored in the same account:
- resolve:ssm:parameter-name
- resolve:ssm:parameter-name:version-number – The version number itself is a default label
- resolve:ssm:parameter-name:label To reference a parameter shared from another AWS account:
- resolve:ssm:parameter-ARN
- resolve:ssm:parameter-ARN:version-number
- resolve:ssm:parameter-ARN:label Parameter versions

Systems Manager parameters are versioned resources. When you update a parameter, you create new, successive versions of the parameter. Systems Manager supports parameter labels that you can map to specific versions of a parameter.
For example, the golden-ami parameter can have three versions: 1, 2, and 3. You can create a parameter label beta that maps to version 2, and a parameter label prod that maps to version 3.
In a launch template, you can specify version 3 of the golden-ami parameter by using either of the following formats:
- resolve:ssm:golden-ami:3
- resolve:ssm:golden-ami:prod Specifying the version or label is optional. If a version or label is not specified, the latest version of the parameter is used.
#### Specify a Systems Manager parameter in a launch template You can specify a Systems Manager parameter in a launch template instead of an AMI ID when you create a launch template or a new version of a launch template.
Console To specify a Systems Manager parameter in a launch template
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Launch Templates, and then choose Create launch template.
3. For Launch template name, enter a descriptive name for the launch template.
4. Under Application and OS Images (Amazon Machine Image), choose Browse more AMIs.
5. Choose the arrow button to the right of the search bar, and then choose Specify custom value/Systems Manager parameter.
6. In the Specify custom value or Systems Manager parameter dialog box, do the following: a.
For AMI ID or Systems Manager parameter string, enter the Systems Manager parameter name using one of the following formats:
To reference a public parameter:

- resolve:ssm:public-parameter To reference a parameter stored in the same account:
- resolve:ssm:parameter-name
- resolve:ssm:parameter-name:version-number
- resolve:ssm:parameter-name:label To reference a parameter shared from another AWS account:
- resolve:ssm:parameter-ARN
- resolve:ssm:parameter-ARN:version-number
- resolve:ssm:parameter-ARN:label b.
Choose Save.
7. Specify any other launch template parameters as needed, and then choose Create launch template.
For more information, see Create a launch template by specifying parameters.
AWS CLI To specify a Systems Manager parameter in a launch template
- Use the create-launch-template command to create the launch template. To specify the AMI to use, enter the Systems Manager parameter name using one of the following formats:
To reference a public parameter:
- resolve:ssm:public-parameter To reference a parameter stored in the same account:
- resolve:ssm:parameter-name
- resolve:ssm:parameter-name:version-number
- resolve:ssm:parameter-name:label

To reference a parameter shared from another AWS account:
- resolve:ssm:parameter-ARN
- resolve:ssm:parameter-ARN:version-number
- resolve:ssm:parameter-ARN:label The following example creates a launch template that specifies the following:
- A name for the launch template (TemplateForWebServer)
- A tag for the launch template (purpose=production)
- The data for the instance configuration, specified in a JSON file:
- The AMI to use (resolve:ssm:golden-ami)
- The instance type to launch (m5.4xlarge)
- A tag for the instance (Name=webserver) aws ec2 create-launch-template \ --launch-template-name TemplateForWebServer \ --tag-specifications 'ResourceType=launch- template,Tags=[{Key=purpose,Value=production}]' \ --launch-template-data file://template-data.json The following is an example JSON file that contains the launch template data for the instance configuration. The value for ImageId is the Systems Manager parameter name, entered in the required format resolve:ssm:golden-ami.
{"LaunchTemplateData": { "ImageId": "resolve:ssm:golden-ami", "InstanceType": "m5.4xlarge", "TagSpecifications": [{ "ResourceType": "instance", "Tags": [{ "Key":"Name", "Value":"webserver"
        }]
    }]
  }

}
#### Verify that a launch template gets the correct AMI ID To resolve the Systems Manager parameter to the actual AMI ID Use the describe-launch-template-versions command and include the --resolve-alias parameter. aws ec2 describe-launch-template-versions \ --launch-template-name my-launch-template \ --versions $Default \ --resolve-alias The response includes the AMI ID for ImageId. In this example, when an instance is launched using this launch template, the AMI ID resolves to ami-0ac394d6a3example.
{ "LaunchTemplateVersions": [ { "LaunchTemplateId": "lt-089c023a30example", "LaunchTemplateName": "my-launch-template", "VersionNumber": 1, "CreateTime": "2022-12-28T19:52:27.000Z", "CreatedBy": "arn:aws:iam::123456789012:user/Bob", "DefaultVersion": true, "LaunchTemplateData": { "ImageId": "ami-0ac394d6a3example", "InstanceType": "t3.micro", } } ]
}
#### Related resources For more information about working with Systems Manager parameters, see the following reference materials in the Systems Manager documentation.
- For information about how to look up the AMI public parameters supported by Amazon EC2, see Calling AMI public parameters.

- For information about sharing parameters with other AWS accounts or through AWS Organizations, see Working with shared parameters.
- For information about monitoring whether your parameters are created successfully, see Native parameter support for Amazon Machine Image IDs.
#### Limitations
- Only EC2 Fleets of type instant support using a launch template that has a Systems Manager parameter specified in place of an AMI ID.
- EC2 Fleets of type maintain and request, and Spot Fleets do not support using a launch template that has a Systems Manager parameter specified in place of an AMI ID. For EC2 Fleets of type maintain and request, and for Spot Fleets, if you specify an AMI in the launch template, you must specify the AMI ID.
- If you use attribute-based instance selection in your EC2 Fleet, you can't specify a Systems Manager parameter in place of an AMI ID. When using attribute-based instance selection, you must specify the AMI ID.
- Amazon EC2 Auto Scaling provides other restrictions. For more information, see Use AWS Systems Manager parameters instead of AMI IDs in launch templates in the Amazon EC2 Auto Scaling User Guide.
## Modify a launch template (manage launch template versions)
Launch templates are immutable; after you create a launch template, you can't modify it. Instead, you can create a new version of the launch template that includes any changes you require.
You can create different versions of a launch template, set the default version, describe a launch template version, and delete versions you no longer need.
Tasks
- Create a launch template version
- Set the default launch template version
- Describe a launch template version

### Create a launch template version When you create a launch template version, you can specify new launch parameters or use an existing version as the base for the new version. For a description of each parameter, see Reference for Amazon EC2 instance configuration parameters.
Console To create a launch template version
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Launch Templates.
3. Select a launch template, and then choose Actions, Modify template (Create new version).
4. For Template version description, enter a description for this version of the launch template.
5. (Optional) Expand Source template and select a version of the launch template to use as a base for the new launch template version. The new launch template version inherits the launch parameters from this launch template version.
6. Modify the launch parameters as required.
7. Choose Create launch template.
AWS CLI To create a launch template version Use the create-launch-template-version command. You can specify a source version on which to base the new version. The new version inherits the launch parameters from this version, and you can override parameters using --launch-template-data. The following example creates a new version based on version 1 of the launch template and specifies a different AMI ID. aws ec2 create-launch-template-version \ --launch-template-id lt-0abcd290751193123 \ --version-description WebVersion2 \ --source-version 1 \ --launch-template-data "ImageId=ami-0abcdef1234567890"
PowerShell To create a launch template version

Use the New-EC2LaunchTemplateVersion Cmdlet. You can specify a source version on which to base the new version. The new version inherits the launch parameters from this version, and you can override parameters using LaunchTemplateData. The following example creates a new version based on version 1 of the launch template and specifies a different AMI ID.
New-EC2LaunchTemplateVersion `
    -LaunchTemplateId lt-0abcd290751193123 `
    -VersionDescription WebVersion2 `
    -SourceVersion 1 `
    -LaunchTemplateData ( New-Object `
            -TypeName Amazon.EC2.Model.RequestLaunchTemplateData `
            -Property @{ImageId = 'ami-0abcdef1234567890'} )
### Set the default launch template version You can set the default version for the launch template. When you launch an instance from a launch template and do not specify a version, the instance is launched using the parameters of the default version.
Console To set the default launch template version
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Launch Templates.
3. Select the launch template and choose Actions, Set default version.
4. For Template version, select the version number to set as the default version and choose Set as default version.
AWS CLI To set the default launch template version Use the modify-launch-template command. aws ec2 modify-launch-template \

    --launch-template-id lt-0abcd290751193123 \ --default-version 2 PowerShell To set the default launch template version Use the Edit-EC2LaunchTemplate cmdlet.
Edit-EC2LaunchTemplate `
    -LaunchTemplateId lt-0abcd290751193123 `
    -DefaultVersion 2
### Describe a launch template version Using the console, you can view all the versions of the selected launch template, or get a list of the launch templates whose latest or default version matches a specific version number. Using the AWS CLI, you can describe all versions, individual versions, or a range of versions of a specified launch template. You can also describe all the latest versions or all the default versions of all the launch templates in your account.
Console To describe a launch template version
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Launch Templates.
3. You can view a version of a specific launch template, or get a list of the launch templates whose latest or default version matches a specific version number.
- To view a version of a launch template: Select the launch template. On the Versions tab, from Version, select a version to view its details.
- To get a list of all the launch templates whose latest version matches a specific version number: From the search bar, choose Latest version, and then choose a version number.
- To get a list of all the launch templates whose default version matches a specific version number: From the search bar, choose Default version, and then choose a version number.

AWS CLI To describe a launch template version Use the describe-launch-template-versions command and specify the version numbers. In the following example, versions 1 and 3 are specified. aws ec2 describe-launch-template-versions \ --launch-template-id lt-0abcd290751193123 \ --versions 1 3 To describe the latest and default launch template versions in your account Use the describe-launch-template-versions command and specify $Latest, $Default, or both. You must omit the launch template ID and name in the call. You can't specify version numbers. aws ec2 describe-launch-template-versions \ --versions "$Latest,$Default"
PowerShell To describe a launch template version Use the Get-EC2TemplateVersion Cmdlet and specify the version numbers. In the following example, versions 1 and 3 are specified.
Get-EC2TemplateVersion `
    -LaunchTemplateId lt-0abcd290751193123 `
    -Version 1,3 To describe the latest and default launch template versions in your account Use the Get-EC2TemplateVersion Cmdlet and specify $Latest, $Default, or both. You must omit the launch template ID and name in the call. You can't specify version numbers.
Get-EC2TemplateVersion `
    -Version '$Latest','$Default'

## Delete a launch template or a launch template version If you no longer require a launch template, you can delete it. Deleting a launch template deletes all of its versions. If you only want to delete a specific version of a launch template, you can do so while retaining the other versions of the launch template.
Deleting a launch template or launch template version doesn't affect any instances that you've launched from the launch template.
### Delete a launch template and all of its versions If you no longer require a launch template, including all of its versions, you can delete the launch template. Deleting a launch template deletes all of its versions.
Console To delete a launch template and all its versions
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Launch Templates.
3. Select the launch template and choose Actions, Delete template.
4. Enter Delete to confirm deletion, and then choose Delete.
AWS CLI To delete a launch template and all its versions Use the delete-launch-template command and specify the launch template. aws ec2 delete-launch-template --launch-template-id lt-01238c059e3466abc PowerShell To delete a launch template and all its versions Use the Remove-EC2LaunchTemplate (AWS Tools for PowerShell) command and specify the launch template. If -Force is omitted, PowerShell prompts for a confirmation.
Remove-EC2LaunchTemplate -LaunchTemplateId lt-0123456789example -Force

### Delete a launch template version If you no longer require a launch template version, you can delete it.
Considerations
- You can't replace the version number after you delete it.
- You can't delete the default version of the launch template; you must first assign a different version as the default. If the default version is the only version for the launch template, you must delete the entire launch template.
- When using the console, you can delete one launch template version at a time. When using the AWS CLI, you can delete up to 200 launch template versions in a single request. To delete more than 200 versions in a single request, you can delete the launch template, which also deletes all of its versions.
Console To delete a launch template version
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Launch Templates.
3. Select the launch template and choose Actions, Delete template version.
4. Select the version to delete and choose Delete.
AWS CLI To delete a launch template version Use the delete-launch-template-versions command and specify the version numbers to delete.
You can specify up to 200 launch template versions to delete in a single request. aws ec2 delete-launch-template-versions \ --launch-template-id lt-0abcd290751193123 \ --versions 1 PowerShell To delete a launch template version
