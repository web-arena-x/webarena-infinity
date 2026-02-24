# Identity and access management for Amazon EC2

Source: apps/user-manuals/aws/ec2-ug.pdf

---

In addition to the AWS global infrastructure, Amazon EC2 offers the following features to support your data resiliency:
- Copying AMIs across Regions
- Copying EBS snapshots across Regions
- Automating EBS-backed AMIs using Amazon Data Lifecycle Manager
- Automating EBS snapshots using Amazon Data Lifecycle Manager
- Maintaining the health and availability of your fleet using Amazon EC2 Auto Scaling
- Distributing incoming traffic across multiple instances in a single Availability Zone or multiple Availability Zones using Elastic Load Balancing
# Compliance validation for Amazon EC2 To learn whether an AWS service is within the scope of specific compliance programs, see AWS services in Scope by Compliance Program and choose the compliance program that you are interested in. For general information, see AWS Compliance Programs.
You can download third-party audit reports using AWS Artifact. For more information, see Downloading Reports in AWS Artifact.
Your compliance responsibility when using AWS services is determined by the sensitivity of your data, your company's compliance objectives, and applicable laws and regulations. For more information about your compliance responsibility when using AWS services, see AWS Security Documentation.
# Identity and access management for Amazon EC2 AWS Identity and Access Management (IAM) is an AWS service that helps an administrator securely control access to AWS resources. IAM administrators control who can be authenticated (signed in) and authorized (have permissions) to use Amazon EC2 resources. IAM is an AWS service that you can use with no additional charge.
Your security credentials identify you to services in AWS and grant you access to AWS resources, such as your Amazon EC2 resources. You can use features of Amazon EC2 and IAM to allow other users, services, and applications to use your Amazon EC2 resources without sharing your security credentials. You can use IAM to control how other users use resources in your AWS account, and

you can use security groups to control access to your Amazon EC2 instances. You can choose to allow full or limited use of your Amazon EC2 resources.
If you are a developer, you can use IAM roles to manage the security credentials needed by the applications that you run on your EC2 instances. After you attach an IAM role to your instance, your applications running on the instance can retrieve the credentials from the Instance Metadata Service (IMDS).
For best practices for securing your AWS resources using IAM, see Security best practices in IAM in the IAM User Guide.
Contents
- Identity-based policies for Amazon EC2
- Example policies to control access the Amazon EC2 API
- Example policies to control access to the Amazon EC2 console
- AWS managed policies for Amazon EC2
- IAM roles for Amazon EC2
## Identity-based policies for Amazon EC2 By default, users don't have permission to create or modify Amazon EC2 resources, or perform tasks using the Amazon EC2 API, Amazon EC2 console, or CLI. To allow users to create or modify resources and perform tasks, you must create IAM policies that grant users permission to use the specific resources and API actions they'll need, and then attach those policies to the users, groups, or IAM roles that require those permissions.
When you attach a policy to a user, group of users, or role it allows or denies the users permission to perform the specified tasks on the specified resources. For more general information about IAM policies, see Policies and permissions in IAM in the IAM User Guide. For more information about managing and creating IAM policies, see Manage IAM policies.
An IAM policy must grant or deny permissions to use one or more Amazon EC2 actions. It must also specify the resources that can be used with the action, which can be all resources, or in some cases, specific resources. The policy can also include conditions that you apply to the resource.
To get started, you can check whether the AWS managed policies for Amazon EC2 meet your needs. Otherwise, you can create your own custom policies. For more information, see the section called "AWS managed policies".

Contents
- Policy syntax
- Actions for Amazon EC2
- Supported resource-level permissions for Amazon EC2 API actions
- Amazon Resource Names (ARNs) for Amazon EC2
- Condition keys for Amazon EC2
- Control access using attribute-based access
- Grant permissions to users, groups, and roles
- Check that users have the required permissions
### Policy syntax An IAM policy is a JSON document that consists of one or more statements. Each statement is structured as follows.
{ "Statement":[{ "Effect":"effect", "Action":"action", "Resource":"arn", "Condition":{ "condition":{ "key":"value"
        } } } ]
} There are various elements that make up a statement:
- Effect: The effect can be Allow or Deny. By default, users don't have permission to use resources and API actions, so all requests are denied. An explicit allow overrides the default. An explicit deny overrides any allows.
- Action: The action is the specific API action for which you are granting or denying permission. To learn about specifying action, see Actions for Amazon EC2.

- Resource: The resource that's affected by the action. Some Amazon EC2 API actions allow you to include specific resources in your policy that can be created or modified by the action. You specify a resource using an Amazon Resource Name (ARN) or using the wildcard (*) to indicate that the statement applies to all resources. For more information, see Supported resource-level permissions for Amazon EC2 API actions.
- Condition: Conditions are optional. They can be used to control when your policy is in effect. For more information about specifying conditions for Amazon EC2, see Condition keys for Amazon EC2.
For more information about policy requirements, see the IAM JSON policy reference in the IAM User Guide. For example IAM policy statements for Amazon EC2, see Example policies to control access the Amazon EC2 API.
### Actions for Amazon EC2 In an IAM policy statement, you can specify any API action from any service that supports IAM.
For Amazon EC2, use the following prefix with the name of the API action: ec2:. For example: ec2:RunInstances and ec2:CreateImage.
To specify multiple actions in a single statement, separate them with commas as follows:
"Action": ["ec2:action1", "ec2:action2"]
You can also specify multiple actions using wildcards. For example, you can specify all actions whose name begins with the word "Describe" as follows:
"Action": "ec2:Describe*"
Note Currently, the Amazon EC2 Describe* API actions do not support resource-level permissions.
For more information about resource-level permissions for Amazon EC2, see Identity-based policies for Amazon EC2.
To specify all Amazon EC2 API actions, use the * wildcard as follows:
"Action": "ec2:*"

For a list of Amazon EC2 actions, see Actions defined by Amazon EC2 in the Service Authorization Reference.
### Supported resource-level permissions for Amazon EC2 API actions Resource-level permissions refers to the ability to specify which resources users are allowed to perform actions on. Amazon EC2 has partial support for resource-level permissions. This means that for certain Amazon EC2 actions, you can control when users are allowed to use those actions based on conditions that have to be fulfilled, or specific resources that users are allowed to use. For example, you can grant users permissions to launch instances, but only of a specific type, and only using a specific AMI.
To specify a resource in an IAM policy statement, use its Amazon Resource Name (ARN). For more information about specifying the ARN value, see Amazon Resource Names (ARNs) for Amazon EC2.
If an API action does not support individual ARNs, you must use a wildcard (*) to specify that all resources can be affected by the action.
To see tables that identify which Amazon EC2 API actions support resource-level permissions, and the ARNs and condition keys that you can use in a policy, see Actions, resources, and condition keys for Amazon EC2.
Keep in mind that you can apply tag-based resource-level permissions in the IAM policies you use for Amazon EC2 API actions. This gives you better control over which resources a user can create, modify, or use. For more information, see Grant permission to tag Amazon EC2 resources during creation.
### Amazon Resource Names (ARNs) for Amazon EC2 Each IAM policy statement applies to the resources that you specify using their ARNs.
An ARN has the following general syntax: arn:aws:[service]:[region]:[account-id]:resourceType/resourcePath service The service (for example, ec2). region The Region for the resource (for example, us-east-1).

account-id The AWS account ID, with no hyphens (for example, 123456789012). resourceType The type of resource (for example, instance). resourcePath A path that identifies the resource. You can use the * wildcard in your paths.
For example, you can indicate a specific instance (i-1234567890abcdef0) in your statement using its ARN as follows.
"Resource": "arn:aws:ec2:us-east-1:123456789012:instance/i-1234567890abcdef0"
You can specify all instances that belong to a specific account by using the * wildcard as follows.
"Resource": "arn:aws:ec2:us-east-1:123456789012:instance/*"
You can also specify all Amazon EC2 resources that belong to a specific account by using the * wildcard as follows.
"Resource": "arn:aws:ec2:us-east-1:123456789012:*"
To specify all resources, or if a specific API action does not support ARNs, use the * wildcard in the Resource element as follows.
"Resource": "*"
Many Amazon EC2 API actions involve multiple resources. For example, AttachVolume attaches an Amazon EBS volume to an instance, so a user must have permissions to use the volume and the instance. To specify multiple resources in a single statement, separate their ARNs with commas, as follows.
"Resource": ["arn1", "arn2"]
For a list of ARNs for Amazon EC2 resources, see Resource types defined by Amazon EC2.

### Condition keys for Amazon EC2 In a policy statement, you can optionally specify conditions that control when it is in effect. Each condition contains one or more key-value pairs. Condition keys are not case-sensitive. We've defined AWS global condition keys, plus additional service-specific condition keys.
For a list of service-specific condition keys for Amazon EC2, see Condition keys for Amazon EC2. Amazon EC2 also implements the AWS global condition keys. For more information, see Information available in all requests in the IAM User Guide.
All Amazon EC2 actions support the aws:RequestedRegion and ec2:Region condition keys. For more information, see Example: Restrict access to a specific Region.
To use a condition key in your IAM policy, use the Condition statement. For example, the following policy grants users permission to add and remove inbound and outbound rules for any security group. It uses the ec2:Vpc condition key to specify that these actions can only be performed on security groups in a specific VPC.
JSON { "Version":"2012-10-17", "Statement":[{ "Effect":"Allow", "Action": [ "ec2:AuthorizeSecurityGroupIngress", "ec2:AuthorizeSecurityGroupEgress", "ec2:RevokeSecurityGroupIngress", "ec2:RevokeSecurityGroupEgress"], "Resource": "arn:aws:ec2:us-east-1:111122223333:security-group/*", "Condition": { "StringEquals": { "ec2:Vpc": "arn:aws:ec2:us-east-1:111122223333:vpc/ vpc-11223344556677889"
        } } } ]
}

If you specify multiple conditions, or multiple keys in a single condition, we evaluate them using a logical AND operation. If you specify a single condition with multiple values for one key, we evaluate the condition using a logical OR operation. For permissions to be granted, all conditions must be met.
You can also use placeholders when you specify conditions. For more information, see IAM policy elements: Variables and tags in the IAM User Guide.
Important Many condition keys are specific to a resource, and some API actions use multiple resources.
If you write a policy with a condition key, use the Resource element of the statement to specify the resource to which the condition key applies. If not, the policy may prevent users from performing the action at all, because the condition check fails for the resources to which the condition key does not apply. If you do not want to specify a resource, or if you've written the Action element of your policy to include multiple API actions, then you must use the ...IfExists condition type to ensure that the condition key is ignored for resources that do not use it. For more information, see ...IfExists Conditions in the IAM User Guide.
Condition keys
- ec2:Attribute condition key
- ec2:ResourceID condition keys
- ec2:SourceInstanceARN condition key
#### ec2:Attribute condition key The ec2:Attribute condition key can be used for conditions that filter access by an attribute of a resource.
This condition key supports only properties that are of a primitive data type (such as strings or integers), or complex AttributeValue objects that contain only a Value property (such as the Description or ImdsSupport objects of the  ModifyImageAttribute API action). The condition key can't be used with complex objects that contain multiple properties, such as the LaunchPermission object of ModifyImageAttribute.

For example, the following policy uses the ec2:Attribute/Description condition key to filter access by the complex Description object of the ModifyImageAttribute API action. The condition key allows only requests that modify an image's description to either Production or Development.
JSON { "Version":"2012-10-17", "Statement": [ { "Effect": "Allow", "Action": "ec2:ModifyImageAttribute", "Resource": "arn:aws:ec2:us-east-1::image/ami-*", "Condition": { "StringEquals": { "ec2:Attribute/Description": [ "Production", "Development"
          ]
        } } } ]
} The following example policy uses the ec2:Attribute condition key to filter access by the primitive Attribute property of the  ModifyImageAttribute API action. The condition key denies all requests that attempt to modify an image's description.
JSON { "Version":"2012-10-17", "Statement": [ { "Effect": "Deny", "Action": "ec2:ModifyImageAttribute", "Resource": "arn:aws:ec2:us-east-1::image/ami-*",

      "Condition": { "StringEquals": { "ec2:Attribute": "Description"
        } } } ]
}
#### ec2:ResourceID condition keys When using the following ec2:ResourceID condition keys with the specified API actions, the condition key value is used to specify the resulting resource that is created by the API action. ec2:ResourceID condition keys can't be used to specify a source resource that is specified in the API request. If you use one of the following ec2:ResourceID condition keys with a specified API, then you must always specify the wildcard (*). If you specify a different value, the condition always resolves to * during runtime. For example, to use the ec2:ImageId condition key with the CopyImage API, then you must specify the condition key as follows:
JSON { "Version":"2012-10-17", "Statement": [ { "Effect": "Allow", "Action": "ec2:CopyImage", "Resource": "arn:aws:ec2:us-east-1::image/ami-*", "Condition": { "StringEquals": { "ec2:ImageID": "*"
        } } } ]
} We recommend that you avoid using these condition keys with these API actions:

- ec2:DhcpOptionsID – CreateDhcpOptions
- ec2:ImageID – CopyImage, CreateImage, ImportImage, and RegisterImage
- ec2:InstanceID – RunInstances and ImportInstance
- ec2:InternetGatewayID – CreateInternetGateway
- ec2:NetworkAclID – CreateNetworkAcl
- ec2:NetworkInterfaceID – CreateNetworkInterface
- ec2:PlacementGroupName – CreatePlacementGroup
- ec2:RouteTableID – CreateRouteTable
- ec2:SecurityGroupID – CreateSecurityGroup
- ec2:SnapshotID – CopySnapshot, CreateSnapshot, CreateSnapshots, and ImportSnapshots
- ec2:SubnetID – CreateSubnet
- ec2:VolumeID – CreateVolume and ImportVolume
- ec2:VpcID – CreateVpc
- ec2:VpcPeeringConnectionID – CreateVpcPeeringConnection To filter access based on specific resource IDs, we recommend that you use the Resource policy element as follows.
JSON { "Version":"2012-10-17", "Statement": [ { "Effect": "Allow", "Action": "ec2:CopyImage", "Resource": "arn:aws:ec2:us-east-1::image/ami-01234567890abcdef"
    } ]
}

#### ec2:SourceInstanceARN condition key Use ec2:SourceInstanceARN to specify the ARN of the instance from which a request is made.
This is an AWS global condition key, which means that you can use it with services other than Amazon EC2. For a policy example, see Example: Allow a specific instance to view resources in other AWS services.
### Control access using attribute-based access When you create an IAM policy that grants users permission to use EC2 resources, you can include tag information in the Condition element of the policy to control access based on tags. This is known as attribute-based access control (ABAC). ABAC provides better control over which resources a user can modify, use, or delete. For more information, see What is ABAC for AWS?
For example, you can create a policy that allows users to terminate an instance, but denies the action if the instance has the tag environment=production. To do this, you use the aws:ResourceTag condition key to allow or deny access to the resource based on the tags that are attached to the resource.
"StringEquals": { "aws:ResourceTag/environment": "production" } To learn whether an Amazon EC2 API action supports controlling access using the aws:ResourceTag condition key, see Actions, resources, and condition keys for Amazon EC2. Note that the Describe actions do not support resource-level permissions, so you must specify them in a separate statement without conditions.
For example IAM policies, see Example policies to control access the Amazon EC2 API.
If you allow or deny users access to resources based on tags, you must consider explicitly denying users the ability to add those tags to or remove them from the same resources. Otherwise, it's possible for a user to circumvent your restrictions and gain access to a resource by modifying its tags.
### Grant permissions to users, groups, and roles To provide access, add permissions to your users, groups, or roles:
- Users and groups in AWS IAM Identity Center:
Create a permission set. Follow the instructions in Create a permission set in the AWS IAM Identity Center User Guide.

- Users managed in IAM through an identity provider:
Create a role for identity federation. Follow the instructions in Create a role for a third-party identity provider (federation) in the IAM User Guide.
- IAM users:
- Create a role that your user can assume. Follow the instructions in Create a role for an IAM user in the IAM User Guide.
- (Not recommended) Attach a policy directly to a user or add a user to a user group. Follow the instructions in Adding permissions to a user (console) in the IAM User Guide.
### Check that users have the required permissions After you've created an IAM policy, we recommend that you check whether it grants users the permissions to use the particular API actions and resources they need before you put the policy into production.
First, create a user for testing purposes, and then attach the IAM policy that you created to the test user. Then, make a request as the test user.
If the Amazon EC2 action that you are testing creates or modifies a resource, you should make the request using the DryRun parameter (or run the AWS CLI command with the --dry-run option). In this case, the call completes the authorization check, but does not complete the operation. For example, you can check whether the user can terminate a particular instance without actually terminating it. If the test user has the required permissions, the request returns DryRunOperation; otherwise, it returns UnauthorizedOperation.
If the policy doesn't grant the user the permissions that you expected, or is overly permissive, you can adjust the policy as needed and retest until you get the desired results.
Important It can take several minutes for policy changes to propagate before they take effect.
Therefore, we recommend that you allow five minutes to pass before you test your policy updates.
If an authorization check fails, the request returns an encoded message with diagnostic information. You can decode the message using the DecodeAuthorizationMessage action.

For more information, see DecodeAuthorizationMessage in the AWS Security Token Service API Reference, and decode-authorization-message.
## Example policies to control access the Amazon EC2 API You can use IAM policies to grant users the permissions required to work with Amazon EC2. For step-by-step directions, see Creating IAM policies in the IAM User Guide.
The following examples show policy statements that you could use to grant users permissions to use Amazon EC2. These policies are designed for requests that are made using the AWS CLI or an AWS SDK. In the following examples, replace each user input placeholder with your own information.
Examples
- Example: Read-only access
- Example: Restrict access to a specific Region
- Work with instances
- Launch instances (RunInstances)
- Work with Spot Instances
- Example: Work with Reserved Instances
- Example: Tag resources
- Example: Work with IAM roles
- Example: Work with route tables
- Example: Allow a specific instance to view resources in other AWS services
- Example: Work with launch templates
- Work with instance metadata
- Work with Amazon EBS volumes and snapshots For example policies for working in the Amazon EC2 console, see Example policies to control access to the Amazon EC2 console.
### Example: Read-only access The following policy grants users permissions to use all Amazon EC2 API actions whose names begin with Describe. The Resource element uses a wildcard to indicate that users can specify all resources with these API actions. The * wildcard is also necessary in cases where the API action does

not support resource-level permissions. For more information about which ARNs you can use with which Amazon EC2 API actions, see Actions, resources, and condition keys for Amazon EC2.
Users don't have permission to perform any actions on the resources (unless another statement grants them permission to do so) because they're denied permission to use API actions by default.
JSON { "Version":"2012-10-17", "Statement": [ { "Effect": "Allow", "Action": "ec2:Describe*", "Resource": "*"
    } ]
}
### Example: Restrict access to a specific Region The following policy denies users permission to use all Amazon EC2 API actions unless the Region is Europe (Frankfurt). It uses the global condition key aws:RequestedRegion, which is supported by all Amazon EC2 API actions.
JSON { "Version":"2012-10-17", "Statement": [ { "Effect": "Deny", "Action": "ec2:*", "Resource": "*", "Condition": { "StringNotEquals": { "aws:RequestedRegion": "eu-central-1"
        } } }

  ]
} Alternatively, you can use the condition key ec2:Region, which is specific to Amazon EC2 and is supported by all Amazon EC2 API actions.
JSON { "Version":"2012-10-17", "Statement": [ { "Effect": "Deny", "Action": "ec2:*", "Resource": "*", "Condition": { "StringNotEquals": { "ec2:Region": "eu-central-1"
        } } } ]
}
### Work with instances Examples
- Example: Describe, launch, stop, start, and terminate all instances
- Example: Describe all instances, and stop, start, and terminate only particular instances
#### Example: Describe, launch, stop, start, and terminate all instances The following policy grants users permissions to use the API actions specified in the Action element. The Resource element uses a * wildcard to indicate that users can specify all resources with these API actions. The * wildcard is also necessary in cases where the API action does not support resource-level permissions. For more information about which ARNs you can use with which Amazon EC2 API actions, see Actions, resources, and condition keys for Amazon EC2.

The users don't have permission to use any other API actions (unless another statement grants them permission to do so) because users are denied permission to use API actions by default.
JSON { "Version":"2012-10-17", "Statement": [ { "Effect": "Allow", "Action": [ "ec2:DescribeInstances", "ec2:DescribeImages", "ec2:DescribeKeyPairs", "ec2:DescribeSecurityGroups", "ec2:DescribeAvailabilityZones", "ec2:RunInstances", "ec2:TerminateInstances", "ec2:StopInstances", "ec2:StartInstances"
      ], "Resource": "*"
    } ]
}
#### Example: Describe all instances, and stop, start, and terminate only particular instances The following policy allows users to describe all instances, to start and stop only instances i-1234567890abcdef0 and i-0598c7d356eba48d7, and to terminate only instances in the us- east-1 Region, with the resource tag "purpose=test".
The first statement uses a * wildcard for the Resource element to indicate that users can specify all resources with the action; in this case, they can list all instances. The * wildcard is also necessary in cases where the API action does not support resource-level permissions (in this case, ec2:DescribeInstances). For more information about which ARNs you can use with which Amazon EC2 API actions, see Actions, resources, and condition keys for Amazon EC2.

The second statement uses resource-level permissions for the StopInstances and StartInstances actions. The specific instances are indicated by their ARNs in the Resource element.
The third statement allows users to terminate all instances in the us-east-1 Region that belong to the specified AWS account, but only where the instance has the tag "purpose=test". The Condition element qualifies when the policy statement is in effect.
JSON { "Version":"2012-10-17", "Statement": [ { "Effect": "Allow", "Action": "ec2:DescribeInstances", "Resource": "*"
   }, { "Effect": "Allow", "Action": [ "ec2:StopInstances", "ec2:StartInstances"
      ], "Resource": [ "arn:aws:ec2:us-east-1:111122223333:instance/i-1234567890abcdef0", "arn:aws:ec2:us-east-1:111122223333:instance/i-0598c7d356eba48d7"
      ]
    }, { "Effect": "Allow", "Action": "ec2:TerminateInstances", "Resource": "arn:aws:ec2:us-east-1:111122223333:instance/*", "Condition": { "StringEquals": { "aws:ResourceTag/purpose": "test"
         } } } ]
}

### Launch instances (RunInstances)
The RunInstances API action launches one or more On-Demand Instances or one or more Spot Instances. RunInstances requires an AMI and creates an instance. Users can specify a key pair and security group in the request. Launching into a VPC requires a subnet, and creates a network interface. Launching from an Amazon EBS-backed AMI creates a volume. Therefore, the user must have permissions to use these Amazon EC2 resources. You can create a policy statement that requires users to specify an optional parameter on RunInstances, or restricts users to particular values for a parameter.
For more information about the resource-level permissions that are required to launch an instance, see Actions, resources, and condition keys for Amazon EC2.
By default, users don't have permissions to describe, start, stop, or terminate the resulting instances. One way to grant the users permission to manage the resulting instances is to create a specific tag for each instance, and then create a statement that enables them to manage instances with that tag. For more information, see Work with instances.
Resources
- AMIs
- Instance types
- Subnets
- EBS volumes
- Tags
- Tags in a launch template
- Elastic GPUs
- Launch templates
#### AMIs The following policy allows users to launch instances using only the specified AMIs, ami-9e1670f7 and ami-45cf5c3c. The users can't launch an instance using other AMIs (unless another statement grants the users permission to do so).

JSON { "Version":"2012-10-17", "Statement": [ { "Effect": "Allow", "Action": "ec2:RunInstances", "Resource": [ "arn:aws:ec2:us-east-1::image/ami-9e1670f7", "arn:aws:ec2:us-east-1::image/ami-45cf5c3c", "arn:aws:ec2:us-east-1:111122223333:instance/*", "arn:aws:ec2:us-east-1:111122223333:volume/*", "arn:aws:ec2:us-east-1:111122223333:key-pair/*", "arn:aws:ec2:us-east-1:111122223333:security-group/*", "arn:aws:ec2:us-east-1:111122223333:subnet/*", "arn:aws:ec2:us-east-1:111122223333:network-interface/*"
      ]
    } ]
} Alternatively, the following policy allows users to launch instances from all AMIs owned by Amazon, or certain trusted and verified partners. The Condition element of the first statement tests whether ec2:Owner is amazon. The users can't launch an instance using other AMIs (unless another statement grants the users permission to do so).
JSON { "Version":"2012-10-17", "Statement": [ { "Effect": "Allow", "Action": "ec2:RunInstances", "Resource": [ "arn:aws:ec2:us-east-1::image/ami-*"
      ], "Condition": { "StringEquals": {

            "ec2:Owner": "amazon"
         } } }, { "Effect": "Allow", "Action": "ec2:RunInstances", "Resource": [ "arn:aws:ec2:us-east-1:111122223333:instance/*", "arn:aws:ec2:us-east-1:111122223333:subnet/*", "arn:aws:ec2:us-east-1:111122223333:volume/*", "arn:aws:ec2:us-east-1:111122223333:network-interface/*", "arn:aws:ec2:us-east-1:111122223333:key-pair/*", "arn:aws:ec2:us-east-1:111122223333:security-group/*"
         ]
      } ]
}
#### Instance types The following policy allows users to launch instances using only the t2.micro or t2.small instance type, which you might do to control costs. The users can't launch larger instances because the Condition element of the first statement tests whether ec2:InstanceType is either t2.micro or t2.small.
JSON { "Version":"2012-10-17", "Statement": [ { "Effect": "Allow", "Action": "ec2:RunInstances", "Resource": [ "arn:aws:ec2:us-east-1:111122223333:instance/*"
      ], "Condition": { "StringEquals": { "ec2:InstanceType": ["t2.micro", "t2.small"]
         }

      } }, { "Effect": "Allow", "Action": "ec2:RunInstances", "Resource": [ "arn:aws:ec2:us-east-1::image/ami-*", "arn:aws:ec2:us-east-1:111122223333:subnet/*", "arn:aws:ec2:us-east-1:111122223333:network-interface/*", "arn:aws:ec2:us-east-1:111122223333:volume/*", "arn:aws:ec2:us-east-1:111122223333:key-pair/*", "arn:aws:ec2:us-east-1:111122223333:security-group/*"
         ]
      } ]
} Alternatively, you can create a policy that denies users permissions to launch any instances except t2.micro and t2.small instance types.
JSON { "Version":"2012-10-17", "Statement": [ { "Effect": "Deny", "Action": "ec2:RunInstances", "Resource": [ "arn:aws:ec2:us-east-1:111122223333:instance/*"
      ], "Condition": { "StringNotEquals": { "ec2:InstanceType": ["t2.micro", "t2.small"]
         } } }, { "Effect": "Allow", "Action": "ec2:RunInstances", "Resource": [

         "arn:aws:ec2:us-east-1::image/ami-*", "arn:aws:ec2:us-east-1:111122223333:network-interface/*", "arn:aws:ec2:us-east-1:111122223333:instance/*", "arn:aws:ec2:us-east-1:111122223333:subnet/*", "arn:aws:ec2:us-east-1:111122223333:volume/*", "arn:aws:ec2:us-east-1:111122223333:key-pair/*", "arn:aws:ec2:us-east-1:111122223333:security-group/*"
         ]
      } ]
}
#### Subnets The following policy allows users to launch instances using only the specified subnet, subnet-12345678. The group can't launch instances into any another subnet (unless another statement grants the users permission to do so).
JSON { "Version":"2012-10-17", "Statement": [ { "Effect": "Allow", "Action": "ec2:RunInstances", "Resource": [ "arn:aws:ec2:us-east-1:111122223333:subnet/subnet-12345678", "arn:aws:ec2:us-east-1:111122223333:network-interface/*", "arn:aws:ec2:us-east-1:111122223333:instance/*", "arn:aws:ec2:us-east-1:111122223333:volume/*", "arn:aws:ec2:us-east-1::image/ami-*", "arn:aws:ec2:us-east-1:111122223333:key-pair/*", "arn:aws:ec2:us-east-1:111122223333:security-group/*"
      ]
    } ]
}

Alternatively, you could create a policy that denies users permissions to launch an instance into any other subnet. The statement does this by denying permission to create a network interface, except where subnet subnet-12345678 is specified. This denial overrides any other policies that are created to allow launching instances into other subnets.
JSON { "Version":"2012-10-17", "Statement": [ { "Effect": "Deny", "Action": "ec2:RunInstances", "Resource": [ "arn:aws:ec2:us-east-1:111122223333:network-interface/*"
      ], "Condition": { "ArnNotEquals": { "ec2:Subnet": "arn:aws:ec2:us-east-1:111122223333:subnet/ subnet-12345678"
         } } }, { "Effect": "Allow", "Action": "ec2:RunInstances", "Resource": [ "arn:aws:ec2:us-east-1::image/ami-*", "arn:aws:ec2:us-east-1:111122223333:network-interface/*", "arn:aws:ec2:us-east-1:111122223333:instance/*", "arn:aws:ec2:us-east-1:111122223333:subnet/*", "arn:aws:ec2:us-east-1:111122223333:volume/*", "arn:aws:ec2:us-east-1:111122223333:key-pair/*", "arn:aws:ec2:us-east-1:111122223333:security-group/*"
         ]
      } ]
}

#### EBS volumes The following policy allows users to launch instances only if the EBS volumes for the instance are encrypted. The user must launch an instance from an AMI that was created with encrypted snapshots, to ensure that the root volume is encrypted. Any additional volume that the user attaches to the instance during launch must also be encrypted.
JSON { "Version":"2012-10-17", "Statement": [ { "Effect": "Allow", "Action": "ec2:RunInstances", "Resource": [ "arn:aws:ec2:*:*:volume/*"
            ], "Condition": { "Bool": { "ec2:Encrypted": "true"
                } } }, { "Effect": "Allow", "Action": "ec2:RunInstances", "Resource": [ "arn:aws:ec2:*::image/ami-*", "arn:aws:ec2:*:*:network-interface/*", "arn:aws:ec2:*:*:instance/*", "arn:aws:ec2:*:*:subnet/*", "arn:aws:ec2:*:*:key-pair/*", "arn:aws:ec2:*:*:security-group/*"
            ]
        } ]
}

#### Tags Tag instances on creation The following policy allows users to launch instances and tag the instances during creation. For resource-creating actions that apply tags, users must have permissions to use the CreateTags action. The second statement uses the ec2:CreateAction condition key to allow users to create tags only in the context of RunInstances, and only for instances. Users cannot tag existing resources, and users cannot tag volumes using the RunInstances request.
For more information, see Grant permission to tag Amazon EC2 resources during creation.
JSON { "Version":"2012-10-17", "Statement": [ { "Effect": "Allow", "Action": [ "ec2:RunInstances"
      ], "Resource": "*"
    }, { "Effect": "Allow", "Action": [ "ec2:CreateTags"
      ], "Resource": "arn:aws:ec2:us-east-1:111122223333:instance/*", "Condition": { "StringEquals": { "ec2:CreateAction" : "RunInstances"
          } } } ]
} Tag instances and volumes on creation with specific tags

The following policy includes the aws:RequestTag condition key that requires users to tag any instances and volumes that are created by RunInstances with the tags environment=production and purpose=webserver. If users don't pass these specific tags, or if they don't specify tags at all, the request fails.
JSON { "Version":"2012-10-17", "Statement": [ { "Effect": "Allow", "Action": [ "ec2:RunInstances"
      ], "Resource": [ "arn:aws:ec2:us-east-1::image/*", "arn:aws:ec2:us-east-1:111122223333:subnet/*", "arn:aws:ec2:us-east-1:111122223333:network-interface/*", "arn:aws:ec2:us-east-1:111122223333:security-group/*", "arn:aws:ec2:us-east-1:111122223333:key-pair/*"
      ]
    }, { "Effect": "Allow", "Action": [ "ec2:RunInstances"
      ], "Resource": [ "arn:aws:ec2:us-east-1:111122223333:volume/*", "arn:aws:ec2:us-east-1:111122223333:instance/*"
      ], "Condition": { "StringEquals": { "aws:RequestTag/environment": "production" , "aws:RequestTag/purpose": "webserver"
          } } }, { "Effect": "Allow", "Action": [

         "ec2:CreateTags"
      ], "Resource": "arn:aws:ec2:us-east-1:111122223333:*/*", "Condition": { "StringEquals": { "ec2:CreateAction" : "RunInstances"
          } } } ]
} Tag instances and volumes on creation with at least one specific tag The following policy uses the ForAnyValue modifier on the aws:TagKeys condition to indicate that at least one tag must be specified in the request, and it must contain the key environment or webserver. The tag must be applied to both instances and volumes. Any tag values can be specified in the request.
JSON { "Version":"2012-10-17", "Statement": [ { "Effect": "Allow", "Action": [ "ec2:RunInstances"
      ], "Resource": [ "arn:aws:ec2:us-east-1::image/*", "arn:aws:ec2:us-east-1:111122223333:subnet/*", "arn:aws:ec2:us-east-1:111122223333:network-interface/*", "arn:aws:ec2:us-east-1:111122223333:security-group/*", "arn:aws:ec2:us-east-1:111122223333:key-pair/*"
      ]
    }, { "Effect": "Allow", "Action": [ "ec2:RunInstances"

      ], "Resource": [ "arn:aws:ec2:us-east-1:111122223333:volume/*", "arn:aws:ec2:us-east-1:111122223333:instance/*"
      ], "Condition": { "ForAnyValue:StringEquals": { "aws:TagKeys": ["environment","webserver"]
          } } }, { "Effect": "Allow", "Action": [ "ec2:CreateTags"
      ], "Resource": "arn:aws:ec2:us-east-1:111122223333:*/*", "Condition": { "StringEquals": { "ec2:CreateAction" : "RunInstances"
          } } } ]
} If instances are tagged on creation, they must be tagged with a specific tag In the following policy, users do not have to specify tags in the request, but if they do, the tag must be purpose=test. No other tags are allowed. Users can apply the tags to any taggable resource in the RunInstances request.
JSON { "Version":"2012-10-17", "Statement": [ { "Effect": "Allow", "Action": [ "ec2:RunInstances"

      ], "Resource": "*"
    }, { "Effect": "Allow", "Action": [ "ec2:CreateTags"
      ], "Resource": "arn:aws:ec2:us-east-1:111122223333:*/*", "Condition": { "StringEquals": { "aws:RequestTag/purpose": "test", "ec2:CreateAction" : "RunInstances"
          }, "ForAllValues:StringEquals": { "aws:TagKeys": "purpose"
          } } } ]
} To disallow anyone called tag on create for RunInstances JSON { "Version":"2012-10-17", "Statement": [ { "Sid": "AllowRun", "Effect": "Allow", "Action": [ "ec2:RunInstances"
            ], "Resource": [ "arn:aws:ec2:us-east-1::image/*", "arn:aws:ec2:us-east-1:*:subnet/*", "arn:aws:ec2:us-east-1:*:network-interface/*", "arn:aws:ec2:us-east-1:*:security-group/*", "arn:aws:ec2:us-east-1:*:key-pair/*",

                "arn:aws:ec2:us-east-1:*:volume/*", "arn:aws:ec2:us-east-1:*:instance/*", "arn:aws:ec2:us-east-1:*:spot-instances-request/*"
            ]
        }, { "Effect": "Deny", "Action": "ec2:CreateTags", "Resource": "*"
        } ]
} Only allow specific tags for spot-instances-request. Surprise inconsistency number 2 comes into play here. Under normal circumstances, specifying no tags will result in Unauthenticated. In the case of spot-instances-request, this policy will not be evaluated if there are no spot-instances- request tags, so a non-tag Spot on Run request will succeed.
#### Tags in a launch template In the following example, users can launch instances, but only if they use a specific launch template (lt-09477bcd97b0d310e). The ec2:IsLaunchTemplateResource condition key prevents users from overriding any of the resources specified in the launch template. The second part of the statement allows users to tag instances on creation—this part of the statement is necessary if tags are specified for the instance in the launch template.
JSON { "Version":"2012-10-17", "Statement": [ { "Effect": "Allow", "Action": "ec2:RunInstances", "Resource": "*", "Condition": { "ArnLike": { "ec2:LaunchTemplate": "arn:aws:ec2:us-east-1:111122223333:launch- template/lt-09477bcd97b0d310e"
          }, "Bool": {

             "ec2:IsLaunchTemplateResource": "true"
          } } }, { "Effect": "Allow", "Action": [ "ec2:CreateTags"
      ], "Resource": "arn:aws:ec2:us-east-1:111122223333:instance/*", "Condition": { "StringEquals": { "ec2:CreateAction" : "RunInstances"
          } } } ]
}
#### Elastic GPUs In the following policy, users can launch an instance and specify an elastic GPU to attach to the instance. Users can launch instances in any Region, but they can only attach an elastic GPU during a launch in the us-east-2 Region.
The ec2:ElasticGpuType condition key ensures that instances use either the eg1.medium or eg1.large elastic GPU type.
JSON { "Version":"2012-10-17", "Statement": [ { "Effect": "Allow", "Action": [ "ec2:RunInstances"
            ], "Resource": [ "arn:aws:ec2:*:111122223333:elastic-gpu/*"
            ],

            "Condition": { "StringEquals": { "ec2:Region": "us-east-2", "ec2:ElasticGpuType": [ "eg1.medium", "eg1.large"
                    ]
                } } }, { "Effect": "Allow", "Action": "ec2:RunInstances", "Resource": [ "arn:aws:ec2:*::image/ami-*", "arn:aws:ec2:*:111122223333:network-interface/*", "arn:aws:ec2:*:111122223333:instance/*", "arn:aws:ec2:*:111122223333:subnet/*", "arn:aws:ec2:*:111122223333:volume/*", "arn:aws:ec2:*:111122223333:key-pair/*", "arn:aws:ec2:*:111122223333:security-group/*"
            ]
        } ]
}
#### Launch templates In the following example, users can launch instances, but only if they use a specific launch template (lt-09477bcd97b0d310e). Users can override any parameters in the launch template by specifying the parameters in the RunInstances action.
JSON { "Version":"2012-10-17", "Statement": [ { "Effect": "Allow", "Action": "ec2:RunInstances", "Resource": "*",

      "Condition": { "ArnLike": { "ec2:LaunchTemplate": "arn:aws:ec2:us-east-1:111122223333:launch- template/lt-09477bcd97b0d310e"
          } } } ]
} In this example, users can launch instances only if they use a launch template. The policy uses the ec2:IsLaunchTemplateResource condition key to prevent users from overriding any pre- existing ARNs in the launch template.
JSON { "Version":"2012-10-17", "Statement": [ { "Effect": "Allow", "Action": "ec2:RunInstances", "Resource": "*", "Condition": { "ArnLike": { "ec2:LaunchTemplate": "arn:aws:ec2:us-east-1:111122223333:launch- template/*"
          }, "Bool": { "ec2:IsLaunchTemplateResource": "true"
          } } } ]
} The following example policy allows user to launch instances, but only if they use a launch template. Users cannot override the subnet and network interface parameters in the request; these parameters can only be specified in the launch template. The first part of the statement uses the

NotResource element to allow all other resources except subnets and network interfaces. The second part of the statement allows the subnet and network interface resources, but only if they are sourced from the launch template.
JSON { "Version":"2012-10-17", "Statement": [ { "Effect": "Allow", "Action": "ec2:RunInstances", "NotResource": ["arn:aws:ec2:us-east-1:111122223333:subnet/*", "arn:aws:ec2:us-east-1:111122223333:network-interface/*" ], "Condition": { "ArnLike": { "ec2:LaunchTemplate": "arn:aws:ec2:us-east-1:111122223333:launch- template/*"
          } } }, { "Effect": "Allow", "Action": "ec2:RunInstances", "Resource": ["arn:aws:ec2:us-east-1:111122223333:subnet/*", "arn:aws:ec2:us-east-1:111122223333:network-interface/*" ], "Condition": { "ArnLike": { "ec2:LaunchTemplate": "arn:aws:ec2:us-east-1:111122223333:launch- template/*"
          }, "Bool": { "ec2:IsLaunchTemplateResource": "true"
          } } } ]
}

The following example allows users to launch instances only if they use a launch template, and only if the launch template has the tag Purpose=Webservers. Users cannot override any of the launch template parameters in the RunInstances action.
JSON { "Version":"2012-10-17", "Statement": [ { "Effect": "Allow", "Action": "ec2:RunInstances", "NotResource": "arn:aws:ec2:us-east-1:111122223333:launch-template/*", "Condition": { "ArnLike": { "ec2:LaunchTemplate": "arn:aws:ec2:us-east-1:111122223333:launch- template/*"
          }, "Bool": { "ec2:IsLaunchTemplateResource": "true"
          } } }, { "Effect": "Allow", "Action": "ec2:RunInstances", "Resource": "arn:aws:ec2:us-east-1:111122223333:launch-template/*", "Condition": { "StringEquals": { "aws:ResourceTag/Purpose": "Webservers"
        } } } ]
}
### Work with Spot Instances You can use the RunInstances action to create Spot Instance requests, and tag the Spot Instance requests on create. The resource to specify for RunInstances is spot-instances-request.

The spot-instances-request resource is evaluated in the IAM policy as follows:
- If you don't tag a Spot Instance request on create, Amazon EC2 does not evaluate the spot- instances-request resource in the RunInstances statement.
- If you tag a Spot Instance request on create, Amazon EC2 evaluates the spot-instances- request resource in the RunInstances statement.
Therefore, for the spot-instances-request resource, the following rules apply to the IAM policy:
- If you use RunInstances to create a Spot Instance request and you don't intend to tag the Spot Instance request on create, you don't need to explicitly allow the spot-instances-request resource; the call will succeed.
- If you use RunInstances to create a Spot Instance request and intend to tag the Spot Instance request on create, you must include the spot-instances-request resource in the RunInstances allow statement, otherwise the call will fail.
- If you use RunInstances to create a Spot Instance request and intend to tag the Spot Instance request on create, you must specify the spot-instances-request resource or * wildcard in the CreateTags allow statement, otherwise the call will fail.
You can request Spot Instances using RunInstances or RequestSpotInstances. The following example IAM policies apply only when requesting Spot Instances using RunInstances.
Example: Request Spot Instances using RunInstances The following policy allows users to request Spot Instances by using the RunInstances action. The spot-instances-request resource, which is created by RunInstances, requests Spot Instances.
Note To use RunInstances to create Spot Instance requests, you can omit spot-instances- request from the Resource list if you do not intend to tag the Spot Instance requests on create. This is because Amazon EC2 does not evaluate the spot-instances-request resource in the RunInstances statement if the Spot Instance request is not tagged on create.

JSON { "Version":"2012-10-17", "Statement": [ { "Sid": "AllowRun", "Effect": "Allow", "Action": [ "ec2:RunInstances"
            ], "Resource": [ "arn:aws:ec2:us-east-1::image/*", "arn:aws:ec2:us-east-1:*:subnet/*", "arn:aws:ec2:us-east-1:*:network-interface/*", "arn:aws:ec2:us-east-1:*:security-group/*", "arn:aws:ec2:us-east-1:*:key-pair/*", "arn:aws:ec2:us-east-1:*:volume/*", "arn:aws:ec2:us-east-1:*:instance/*", "arn:aws:ec2:us-east-1:*:spot-instances-request/*"
            ]
        } ]
} Warning NOT SUPPORTED – Example: Deny users permission to request Spot Instances using RunInstances The following policy is not supported for the spot-instances-request resource.
The following policy is meant to give users the permission to launch On-Demand Instances, but deny users the permission to request Spot Instances. The spot-instances- request resource, which is created by RunInstances, is the resource that requests Spot Instances. The second statement is meant to deny the RunInstances action for the spot- instances-request resource. However, this condition is not supported because Amazon EC2 does not evaluate the spot-instances-request resource in the RunInstances statement if the Spot Instance request is not tagged on create.

JSON { "Version":"2012-10-17", "Statement": [ { "Sid": "AllowRun", "Effect": "Allow", "Action": [ "ec2:RunInstances"
            ], "Resource": [ "arn:aws:ec2:us-east-1::image/*", "arn:aws:ec2:us-east-1:*:subnet/*", "arn:aws:ec2:us-east-1:*:network-interface/*", "arn:aws:ec2:us-east-1:*:security-group/*", "arn:aws:ec2:us-east-1:*:key-pair/*", "arn:aws:ec2:us-east-1:*:volume/*", "arn:aws:ec2:us-east-1:*:instance/*"
            ]
        }, { "Sid": "DenySpotInstancesRequestsNOTSUPPORTEDDONOTUSE", "Effect": "Deny", "Action": "ec2:RunInstances", "Resource": "arn:aws:ec2:us-east-1:*:spot-instances-request/*"
        } ]
} Example: Tag Spot Instance requests on create The following policy allows users to tag all resources that are created during instance launch.
The first statement allows RunInstances to create the listed resources. The spot-instances- request resource, which is created by RunInstances, is the resource that requests Spot Instances.
The second statement provides a * wildcard to allow all resources to be tagged when they are created at instance launch.

Note If you tag a Spot Instance request on create, Amazon EC2 evaluates the spot-instances- request resource in the RunInstances statement. Therefore, you must explicitly allow the spot-instances-request resource for the RunInstances action, otherwise the call will fail.
JSON { "Version":"2012-10-17", "Statement": [ { "Sid": "AllowRun", "Effect": "Allow", "Action": [ "ec2:RunInstances"
            ], "Resource": [ "arn:aws:ec2:us-east-1::image/*", "arn:aws:ec2:us-east-1:*:subnet/*", "arn:aws:ec2:us-east-1:*:network-interface/*", "arn:aws:ec2:us-east-1:*:security-group/*", "arn:aws:ec2:us-east-1:*:key-pair/*", "arn:aws:ec2:us-east-1:*:volume/*", "arn:aws:ec2:us-east-1:*:instance/*", "arn:aws:ec2:us-east-1:*:spot-instances-request/*"
            ]
        }, { "Sid": "TagResources", "Effect": "Allow", "Action": "ec2:CreateTags", "Resource": "*"
        } ]
} Example: Deny tag on create for Spot Instance requests

The following policy denies users the permission to tag the resources that are created during instance launch.
The first statement allows RunInstances to create the listed resources. The spot-instances- request resource, which is created by RunInstances, is the resource that requests Spot Instances.
The second statement provides a * wildcard to deny all resources being tagged when they are created at instance launch. If spot-instances-request or any other resource is tagged on create, the RunInstances call will fail.
JSON { "Version":"2012-10-17", "Statement": [ { "Sid": "AllowRun", "Effect": "Allow", "Action": [ "ec2:RunInstances"
            ], "Resource": [ "arn:aws:ec2:us-east-1::image/*", "arn:aws:ec2:us-east-1:*:subnet/*", "arn:aws:ec2:us-east-1:*:network-interface/*", "arn:aws:ec2:us-east-1:*:security-group/*", "arn:aws:ec2:us-east-1:*:key-pair/*", "arn:aws:ec2:us-east-1:*:volume/*", "arn:aws:ec2:us-east-1:*:instance/*", "arn:aws:ec2:us-east-1:*:spot-instances-request/*"
            ]
        }, { "Sid": "DenyTagResources", "Effect": "Deny", "Action": "ec2:CreateTags", "Resource": "*"
        } ]
}

Warning NOT SUPPORTED – Example: Allow creating a Spot Instance request only if it is assigned a specific tag The following policy is not supported for the spot-instances-request resource.
The following policy is meant to grant RunInstances the permission to create a Spot Instance request only if the request is tagged with a specific tag.
The first statement allows RunInstances to create the listed resources.
The second statement is meant to grant users the permission to create a Spot Instance request only if the request has the tag environment=production. If this condition is applied to other resources created by RunInstances, specifying no tags results in an Unauthenticated error. However, if no tags are specified for the Spot Instance request, Amazon EC2 does not evaluate the spot-instances-request resource in the RunInstances statement, which results in non-tagged Spot Instance requests being created by RunInstances.
Note that specifying another tag other than environment=production results in an Unauthenticated error, because if a user tags a Spot Instance request, Amazon EC2 evaluates the spot-instances-request resource in the RunInstances statement.
JSON { "Version":"2012-10-17", "Statement": [ { "Sid": "AllowRun", "Effect": "Allow", "Action": [ "ec2:RunInstances"
            ], "Resource": [ "arn:aws:ec2:us-east-1::image/*", "arn:aws:ec2:us-east-1:*:subnet/*", "arn:aws:ec2:us-east-1:*:network-interface/*", "arn:aws:ec2:us-east-1:*:security-group/*", "arn:aws:ec2:us-east-1:*:key-pair/*", "arn:aws:ec2:us-east-1:*:volume/*", "arn:aws:ec2:us-east-1:*:instance/*"
            ]

        }, { "Sid":
 "RequestSpotInstancesOnlyIfTagIsEnvironmentProductionNOTSUPPORTEDDONOTUSE", "Effect": "Allow", "Action": "ec2:RunInstances", "Resource": "arn:aws:ec2:us-east-1:*:spot-instances-request/ *", "Condition": { "StringEquals": { "aws:RequestTag/environment": "production"
                } } }, { "Sid": "TagResources", "Effect": "Allow", "Action": "ec2:CreateTags", "Resource": "*"
        } ]
} Example: Deny creating a Spot Instance request if it is assigned a specific tag The following policy denies RunInstances the permission to create a Spot Instance request if the request is tagged with environment=production.
The first statement allows RunInstances to create the listed resources.
The second statement denies users the permission to create a Spot Instance request if the request has the tag environment=production. Specifying environment=production as a tag results in an Unauthenticated error. Specifying other tags or specifying no tags will result in the creation of a Spot Instance request.
JSON { "Version":"2012-10-17",

    "Statement": [ { "Sid": "AllowRun", "Effect": "Allow", "Action": [ "ec2:RunInstances"
            ], "Resource": [ "arn:aws:ec2:us-east-1::image/*", "arn:aws:ec2:us-east-1:*:subnet/*", "arn:aws:ec2:us-east-1:*:network-interface/*", "arn:aws:ec2:us-east-1:*:security-group/*", "arn:aws:ec2:us-east-1:*:key-pair/*", "arn:aws:ec2:us-east-1:*:volume/*", "arn:aws:ec2:us-east-1:*:instance/*", "arn:aws:ec2:us-east-1:*:spot-instances-request/*"
            ]
        }, { "Sid": "DenySpotInstancesRequests", "Effect": "Deny", "Action": "ec2:RunInstances", "Resource": "arn:aws:ec2:us-east-1:*:spot-instances-request/*", "Condition": { "StringEquals": { "aws:RequestTag/environment": "production"
                } } }, { "Sid": "TagResources", "Effect": "Allow", "Action": "ec2:CreateTags", "Resource": "*"
        } ]
}
### Example: Work with Reserved Instances The following policy gives users permission to view, modify, and purchase Reserved Instances in your account.

It is not possible to set resource-level permissions for individual Reserved Instances. This policy means that users have access to all the Reserved Instances in the account.
The Resource element uses a * wildcard to indicate that users can specify all resources with the action; in this case, they can list and modify all Reserved Instances in the account. They can also purchase Reserved Instances using the account credentials. The * wildcard is also necessary in cases where the API action does not support resource-level permissions.
JSON { "Version":"2012-10-17", "Statement": [ { "Effect": "Allow", "Action": [ "ec2:DescribeReservedInstances", "ec2:ModifyReservedInstances", "ec2:PurchaseReservedInstancesOffering", "ec2:DescribeAvailabilityZones", "ec2:DescribeReservedInstancesOfferings"
      ], "Resource": "*"
    } ]
} To allow users to view and modify the Reserved Instances in your account, but not purchase new Reserved Instances.
JSON { "Version":"2012-10-17", "Statement": [ { "Effect": "Allow", "Action": [ "ec2:DescribeReservedInstances", "ec2:ModifyReservedInstances",

        "ec2:DescribeAvailabilityZones"
      ], "Resource": "*"
    } ]
}
### Example: Tag resources The following policy allows users to use the CreateTags action to apply tags to an instance only if the tag contains the keyenvironment and the value production. No other tags are allowed and the user cannot tag any other resource types.
JSON { "Version":"2012-10-17", "Statement": [ { "Effect": "Allow", "Action": [ "ec2:CreateTags"
            ], "Resource": "arn:aws:ec2:us-east-1:111122223333:instance/*", "Condition": { "StringEquals": { "aws:RequestTag/environment": "production"
                } } } ]
} The following policy allows users to tag any taggable resource that already has a tag with a key of owner and a value of the username. In addition, users must specify a tag with a key of anycompany:environment-type and a value of either test or prod in the request. Users can specify additional tags in the request.

JSON { "Version":"2012-10-17", "Statement": [ { "Effect": "Allow", "Action": [ "ec2:CreateTags"
            ], "Resource": "arn:aws:ec2:us-east-1:111122223333:*/*", "Condition": { "StringEquals": { "aws:RequestTag/anycompany:environment-type":
 ["test","prod"], "aws:ResourceTag/owner": "${aws:username}"
                } } } ]
} You can create an IAM policy that allows users to delete specific tags for a resource. For example, the following policy allows users to delete tags for a volume if the tag keys specified in the request are environment or cost-center. Any value can be specified for the tag but the tag key must match either of the specified keys.
Note If you delete a resource, all tags associated with the resource are also deleted. Users do not need permissions to use the ec2:DeleteTags action to delete a resource that has tags; they only need permissions to perform the deleting action.
JSON { "Version":"2012-10-17", "Statement": [

       { "Effect": "Allow", "Action": "ec2:DeleteTags", "Resource": "arn:aws:ec2:us-east-1:111122223333:volume/*", "Condition": { "ForAllValues:StringEquals": { "aws:TagKeys": ["environment","cost-center"]
        } } } ]
} This policy allows users to delete only the environment=prod tag on any resource, and only if the resource is already tagged with a key of owner and a value of the username. Users can't delete any other tags for a resource.
JSON { "Version":"2012-10-17", "Statement": [ { "Effect": "Allow", "Action": [ "ec2:DeleteTags"
      ], "Resource": "arn:aws:ec2:us-east-1:111122223333:*/*", "Condition": { "StringEquals": { "aws:RequestTag/environment": "prod", "aws:ResourceTag/owner": "${aws:username}"
        }, "ForAllValues:StringEquals": { "aws:TagKeys": ["environment"]
        } } } ]
}

### Example: Work with IAM roles The following policy allows users to attach, replace, and detach an IAM role to instances that have the tag department=test. Replacing or detaching an IAM role requires an association ID, therefore the policy also grants users permission to use the ec2:DescribeIamInstanceProfileAssociations action.
Users must have permission to use the iam:PassRole action in order to pass the role to the instance.
JSON { "Version":"2012-10-17", "Statement": [ { "Effect": "Allow", "Action": [ "ec2:AssociateIamInstanceProfile", "ec2:ReplaceIamInstanceProfileAssociation", "ec2:DisassociateIamInstanceProfile"
      ], "Resource": "arn:aws:ec2:us-east-1:111122223333:instance/*", "Condition": { "StringEquals": { "aws:ResourceTag/department":"test"
        } } }, { "Effect": "Allow", "Action": "ec2:DescribeIamInstanceProfileAssociations", "Resource": "*"
    }, { "Effect": "Allow", "Action": "iam:PassRole", "Resource": "arn:aws:iam::111122223333:role/DevTeam*"
    } ]
}

The following policy allows users to attach or replace an IAM role for any instance. Users can only attach or replace IAM roles with names that begin with TestRole-. For the iam:PassRole action, ensure that you specify the name of the IAM role and not the instance profile (if the names are different). For more information, see Instance profiles.
JSON { "Version":"2012-10-17", "Statement": [ { "Effect": "Allow", "Action": [ "ec2:AssociateIamInstanceProfile", "ec2:ReplaceIamInstanceProfileAssociation"
            ], "Resource": "*"
        }, { "Effect": "Allow", "Action": "ec2:DescribeIamInstanceProfileAssociations", "Resource": "*"
        }, { "Effect": "Allow", "Action": "iam:PassRole", "Resource": "arn:aws:iam::111122223333:role/TestRole-*"
        } ]
}
### Example: Work with route tables The following policy allows users to add, remove, and replace routes for route tables that are associated with VPC vpc-ec43eb89 only. To specify a VPC for the ec2:Vpc condition key, you must specify the full ARN of the VPC.

JSON { "Version":"2012-10-17", "Statement": [ { "Effect": "Allow", "Action": [ "ec2:DeleteRoute", "ec2:CreateRoute", "ec2:ReplaceRoute"
            ], "Resource": [ "arn:aws:ec2:us-east-1:111122223333:route-table/*"
            ], "Condition": { "StringEquals": { "ec2:Vpc": "arn:aws:ec2:us-east-1:111122223333:vpc/vpc- ec43eb89"
                } } } ]
}
### Example: Allow a specific instance to view resources in other AWS services The following is an example of a policy that you might attach to an IAM role. The policy allows an instance to view resources in various AWS services. It uses the ec2:SourceInstanceARN global condition key to specify that the instance from which the request is made must be instance i-093452212644b0dd6. If the same IAM role is associated with another instance, the other instance cannot perform any of these actions.
JSON { "Version":"2012-10-17", "Statement": [ { "Effect": "Allow",

            "Action": [ "ec2:DescribeVolumes", "s3:ListAllMyBuckets", "dynamodb:ListTables", "rds:DescribeDBInstances"
            ], "Resource": [ "*"
            ], "Condition": { "ArnEquals": { "ec2:SourceInstanceARN": "arn:aws:ec2:us- east-1:111122223333:instance/i-093452212644b0dd6"
                } } } ]
}
### Example: Work with launch templates The following policy allows users to create a launch template version and modify a launch template, but only for a specific launch template (lt-09477bcd97b0d3abc). Users cannot work with other launch templates.
JSON { "Version":"2012-10-17", "Statement": [ { "Action": [ "ec2:CreateLaunchTemplateVersion", "ec2:ModifyLaunchTemplate"
      ], "Effect": "Allow", "Resource": "arn:aws:ec2:us-east-1:111122223333:launch-template/ lt-09477bcd97b0d3abc"
    } ]
}

The following policy allows users to delete any launch template and launch template version, provided that the launch template has the tag Purpose=Testing.
JSON { "Version":"2012-10-17", "Statement": [ { "Action": [ "ec2:DeleteLaunchTemplate", "ec2:DeleteLaunchTemplateVersions"
      ], "Effect": "Allow", "Resource": "arn:aws:ec2:us-east-1:111122223333:launch-template/*", "Condition": { "StringEquals": { "aws:ResourceTag/Purpose": "Testing"
        } } } ]
}
### Work with instance metadata The following policies ensure that users can only retrieve instance metadata using Instance Metadata Service Version 2 (IMDSv2). You can combine the following four policies into one policy with four statements. When combined as one policy, you can use the policy as a service control policy (SCP). It can work equally well as a deny policy that you apply to an existing IAM policy (taking away and limiting existing permission), or as an SCP that is applied globally across an account, an organizational unit (OU), or an entire organization.
Note The following RunInstances metadata options policies must be used in conjunction with a policy that gives the principal permissions to launch an instance with RunInstances. If the principal does not also have RunInstances permissions, it will not be able to launch

an instance. For more information, see the policies in Work with instances and Launch instances (RunInstances).
Important If you use Auto Scaling groups and you need to require the use of IMDSv2 on all new instances, your Auto Scaling groups must use launch templates.
When an Auto Scaling group uses a launch template, the ec2:RunInstances permissions of the IAM principal are checked when a new Auto Scaling group is created. They are also checked when an existing Auto Scaling group is updated to use a new launch template or a new version of a launch template.
Restrictions on the use of IMDSv1 on IAM principals for RunInstances are only checked when an Auto Scaling group that is using a launch template, is created or updated. For an Auto Scaling group that is configured to use the Latest or Default launch template, the permissions are not checked when a new version of the launch template is created.
For permissions to be checked, you must configure the Auto Scaling group to use a specific version of the launch template.
To enforce the use of IMDSv2 on instances launched by Auto Scaling groups, the following additional steps are required:
1. Disable the use of launch configurations for all accounts in your organization by using either service control policies (SCPs) or IAM permissions boundaries for new principals that are created. For existing IAM principals with Auto Scaling group permissions, update their associated policies with this condition key. To disable the use of launch configurations, create or modify the relevant SCP, permissions boundary, or IAM policy with the "autoscaling:LaunchConfigurationName" condition key with the value specified as null.
2. For new launch templates, configure the instance metadata options in the launch template. For existing launch templates, create a new version of the launch template and configure the instance metadata options in the new version.
3. In the policy that gives any principal the permission to use a launch template, restrict association of $latest and $default by specifying "autoscaling:LaunchTemplateVersionSpecified": "true". By restricting the use to a specific version of a launch template, you can ensure that new instances will be launched using the version in which the instance metadata options are configured. For

more information, see LaunchTemplateSpecification in the Amazon EC2 Auto Scaling API Reference, specifically the Version parameter.
4. For an Auto Scaling group that uses a launch configuration, replace the launch configuration with a launch template. For more information, see Migrate your Auto Scaling groups to launch templates in the Amazon EC2 Auto Scaling User Guide.
5. For an Auto Scaling group that uses a launch template, make sure that it uses a new launch template with the instance metadata options configured, or uses a new version of the current launch template with the instance metadata options configured. For more information, see update-auto-scaling-group.
Examples
- Require the use of IMDSv2
- Deny opt-out of IMDSv2
- Specify maximum hop limit
- Limit who can modify the instance metadata options
- Require role credentials to be retrieved from IMDSv2
#### Require the use of IMDSv2 The following policy specifies that you can't call the RunInstances API unless the instance is also opted in to require the use of IMDSv2 (indicated by "ec2:MetadataHttpTokens":
"required"). If you do not specify that the instance requires IMDSv2, you get an UnauthorizedOperation error when you call the RunInstances API.
JSON { "Version":"2012-10-17", "Statement": [ { "Sid": "RequireImdsV2", "Effect": "Deny", "Action": "ec2:RunInstances", "Resource": "arn:aws:ec2:*:*:instance/*", "Condition": {

                "StringNotEquals": { "ec2:MetadataHttpTokens": "required"
                } } } ]
}
#### Deny opt-out of IMDSv2 The following policy specifies that you cannot call the ModifyInstanceMetadataOptions API and allow the option of IMDSv1 or IMDSv2. If you call the ModifyInstanceMetadataOptions API, the HttpTokens attribute must be set to required.
JSON { "Version":"2012-10-17", "Statement": [{ "Sid": "DenyIMDSv1HttpTokensModification", "Effect": "Deny", "Action": "ec2:ModifyInstanceMetadataOptions", "Resource": "arn:aws:ec2:*:*:instance/*", "Condition": { "StringNotEquals": { "ec2:Attribute/HttpTokens": "required"
            }, "Null": { "ec2:Attribute/HttpTokens": false } } }]
}
#### Specify maximum hop limit The following policy specifies that you can't call the RunInstances API unless you also specify a hop limit, and the hop limit can't be more than 3. If you fail to do that, you get an UnauthorizedOperation error when you call the RunInstances API.

JSON { "Version":"2012-10-17", "Statement": [ { "Sid": "MaxImdsHopLimit", "Effect": "Deny", "Action": "ec2:RunInstances", "Resource": "arn:aws:ec2:*:*:instance/*", "Condition": { "NumericGreaterThan": { "ec2:MetadataHttpPutResponseHopLimit": "3"
                } } } ]
}
#### Limit who can modify the instance metadata options The following policy permits only users with the role ec2-imds-admins to make changes to the instance metadata options. If any principal other than the ec2-imds-admins role tries to call the ModifyInstanceMetadataOptions API, it will get an UnauthorizedOperation error. This statement could be used to control the use of the ModifyInstanceMetadataOptions API; there are currently no fine-grained access controls (conditions) for the ModifyInstanceMetadataOptions API.
#### Require role credentials to be retrieved from IMDSv2 The following policy specifies that if this policy is applied to a role, and the role is assumed by the EC2 service and the resulting credentials are used to sign a request, then the request must be signed by EC2 role credentials retrieved from IMDSv2. Otherwise, all of its API calls will get an UnauthorizedOperation error. This statement/policy can be applied generally because, if the request is not signed by EC2 role credentials, it has no effect.
JSON { "Version":"2012-10-17",

    "Statement": [ { "Sid": "RequireAllEc2RolesToUseV2", "Effect": "Deny", "Action": "*", "Resource": "*", "Condition": { "NumericLessThan": { "ec2:RoleDelivery": "2.0"
                } } } ]
}
### Work with Amazon EBS volumes and snapshots For example policies for working with Amazon EBS volumes and snapshots, see Identity-based policy examples for Amazon EBS.
## Example policies to control access to the Amazon EC2 console You can use IAM policies to grant users the permissions required to work with Amazon EC2. For step-by-step directions, see Creating IAM policies in the IAM User Guide.
The console uses additional API actions for its features, so these policies may not work as expected.
For example, a user that has permission to use only the DescribeVolumes API action will encounter errors when trying to view volumes in the console. This section demonstrates policies that enable users to work with specific parts of the console. For additional information about creating policies for the Amazon EC2 console, see the following AWS Security Blog post: Granting Users Permission to Work in the Amazon EC2 Console.
The following examples show policy statements that you could use to grant users permissions to use Amazon EC2. Replace each user input placeholder with your own information. These policies are designed for requests that are made using the AWS Management Console. The Amazon EC2 console might call multiple API actions to display a single resource, and it might not be obvious until the user attempts a task and the console displays an error. For more information, see the following AWS Security Blog post: Granting Users Permission to Work in the Amazon EC2 Console.

Examples
- Example: Read-only access
- Example: Use the EC2 launch instance wizard
- Example: Work with security groups
- Example: Work with Elastic IP addresses
- Example: Work with Reserved Instances To help you work out which API actions are required to perform tasks in the console, you can use a service that logs calls, such as AWS CloudTrail. If your policy does not grant permission to create or modify a specific resource, the console displays an encoded message with diagnostic information.
You can decode the message using the DecodeAuthorizationMessage API action for AWS STS, or the decode-authorization-message command in the AWS CLI.
### Example: Read-only access To allow users to view all resources in the Amazon EC2 console, you can use the same policy as the following example: Example: Read-only access. Users cannot perform any actions on those resources or create new resources, unless another statement grants them permission to do so.
View instances, AMIs, and snapshots Alternatively, you can provide read-only access to a subset of resources. To do this, replace the * wildcard in the ec2:Describe API action with specific ec2:Describe actions for each resource.
The following policy allows users to view all instances, AMIs, and snapshots in the Amazon EC2 console. The ec2:DescribeTags action allows users to view public AMIs. The console requires the tagging information to display public AMIs; however, you can remove this action to allow users to view only private AMIs.
JSON { "Version":"2012-10-17", "Statement": [{ "Effect": "Allow", "Action": [ "ec2:DescribeInstances", "ec2:DescribeImages", "ec2:DescribeTags",

         "ec2:DescribeSnapshots"
      ], "Resource": "*"
   } ]
} Note The Amazon EC2 ec2:Describe* API actions do not support resource-level permissions, so you cannot control which individual resources users can view in the console. Therefore, the * wildcard is necessary in the Resource element of the above statement. For more information about which ARNs you can use with which Amazon EC2 API actions, see Actions, resources, and condition keys for Amazon EC2.
View instances and CloudWatch metrics The following policy allows users to view instances in the Amazon EC2 console, as well as CloudWatch alarms and metrics in the Monitoring tab of the Instances page.
The Amazon EC2 console uses the CloudWatch API to display the alarms and metrics, so you must grant users permission to use the cloudwatch:DescribeAlarms, cloudwatch:DescribeAlarmsForMetric, cloudwatch:ListMetrics, cloudwatch:GetMetricStatistics, and cloudwatch:GetMetricData actions.
JSON { "Version":"2012-10-17", "Statement": [{ "Effect": "Allow", "Action": [ "ec2:DescribeInstances", "ec2:DescribeInstanceTypes", "cloudwatch:DescribeAlarms", "cloudwatch:DescribeAlarmsForMetric", "cloudwatch:ListMetrics", "cloudwatch:GetMetricStatistics", "cloudwatch:GetMetricData"

      ], "Resource": "*"
   } ]
}
### Example: Use the EC2 launch instance wizard The Amazon EC2 launch instance wizard is a screen with options to configure and launch an instance. Your policy must include permission to use the API actions that allow users to work with the wizard's options. If your policy does not include permission to use those actions, some items in the wizard cannot load properly, and users cannot complete a launch.
Basic launch instance wizard access To complete a launch successfully, users must be given permission to use the ec2:RunInstances API action, and at least the following API actions:
- ec2:DescribeImages: To view and select an AMI.
- ec2:DescribeInstanceTypes: To view and select an instance type.
- ec2:DescribeVpcs: To view the available network options.
- ec2:DescribeSubnets: To view all available subnets for the chosen VPC.
- ec2:DescribeSecurityGroups or ec2:CreateSecurityGroup: To view and select an existing security group, or to create a new one.
- ec2:DescribeKeyPairs or ec2:CreateKeyPair: To select an existing key pair, or to create a new one.
- ec2:AuthorizeSecurityGroupIngress: To add inbound rules.
JSON { "Version":"2012-10-17", "Statement": [ { "Effect": "Allow", "Action": [ "ec2:DescribeInstances",

                "ec2:DescribeImages", "ec2:DescribeInstanceTypes", "ec2:DescribeKeyPairs", "ec2:DescribeVpcs", "ec2:DescribeSubnets", "ec2:DescribeSecurityGroups", "ec2:CreateSecurityGroup", "ec2:AuthorizeSecurityGroupIngress", "ec2:CreateKeyPair"
            ], "Resource": "*"
        }, { "Effect": "Allow", "Action": "ec2:RunInstances", "Resource": "*"
        } ]
} You can add API actions to your policy to provide more options for users, for example:
- ec2:DescribeAvailabilityZones: To view and select a specific Availability Zone.
- ec2:DescribeNetworkInterfaces: To view and select existing network interfaces for the selected subnet.
- To add outbound rules to VPC security groups, users must be granted permission to use the ec2:AuthorizeSecurityGroupEgress API action. To modify or delete existing rules, users must be granted permission to use the relevant ec2:RevokeSecurityGroup* API action.
- ec2:CreateTags: To tag the resources that are created by RunInstances. For more information, see Grant permission to tag Amazon EC2 resources during creation. If users do not have permission to use this action and they attempt to apply tags on the tagging page of the launch instance wizard, the launch fails.
Important Specifying a Name while launching an instance creates a tag and requires the ec2:CreateTags action. Be careful about granting users permission to use the ec2:CreateTags action, because doing so limits your ability to use the aws:ResourceTag condition key to restrict their use of other resources. If you grant

users permission to use the ec2:CreateTags action, they can change a resource's tag in order to bypass those restrictions. For more information, see Control access using attribute-based access.
- To use Systems Manager parameters when selecting an AMI, you must add ssm:DescribeParameters and ssm:GetParameters to your policy. ssm:DescribeParameters grants your users the permission to view and select Systems Manager parameters. ssm:GetParameters grants your users the permission to get the values of the Systems Manager parameters. You can also restrict access to specific Systems Manager parameters. For more information, see Restrict access to specific Systems Manager parameters later in this section.
Currently, the Amazon EC2 Describe* API actions do not support resource-level permissions, so you cannot restrict which individual resources users can view in the launch instance wizard.
However, you can apply resource-level permissions on the ec2:RunInstances API action to restrict which resources users can use to launch an instance. The launch fails if users select options that they are not authorized to use.
Restrict access to a specific instance type, subnet, and Region The following policy allows users to launch t2.micro instances using AMIs owned by Amazon, and only into a specific subnet (subnet-1a2b3c4d). Users can only launch in the specified Region.
If users select a different Region, or select a different instance type, AMI, or subnet in the launch instance wizard, the launch fails.
The first statement grants users permission to view the options in the launch instance wizard or to create new ones, as explained in the example above. The second statement grants users permission to use the network interface, volume, key pair, security group, and subnet resources for the ec2:RunInstances action, which are required to launch an instance into a VPC. For more information about using the ec2:RunInstances action, see Launch instances (RunInstances).
The third and fourth statements grant users permission to use the instance and AMI resources respectively, but only if the instance is a t2.micro instance, and only if the AMI is owned by Amazon, or certain trusted and verified partners.
JSON { "Version":"2012-10-17",

   "Statement": [{ "Effect": "Allow", "Action": [ "ec2:DescribeInstances", "ec2:DescribeImages", "ec2:DescribeInstanceTypes", "ec2:DescribeKeyPairs", "ec2:CreateKeyPair", "ec2:DescribeVpcs", "ec2:DescribeSubnets", "ec2:DescribeSecurityGroups", "ec2:CreateSecurityGroup", "ec2:AuthorizeSecurityGroupIngress"
   ], "Resource": "*"
   }, { "Effect": "Allow", "Action":"ec2:RunInstances", "Resource": [ "arn:aws:ec2:us-east-2:111122223333:network-interface/*", "arn:aws:ec2:us-east-2:111122223333:volume/*", "arn:aws:ec2:us-east-2:111122223333:key-pair/*", "arn:aws:ec2:us-east-2:111122223333:security-group/*", "arn:aws:ec2:us-east-2:111122223333:subnet/subnet-1a2b3c4d"
      ]
   }, { "Effect": "Allow", "Action": "ec2:RunInstances", "Resource": [ "arn:aws:ec2:us-east-2:111122223333:instance/*"
      ], "Condition": { "StringEquals": { "ec2:InstanceType": "t2.micro"
         } } }, { "Effect": "Allow", "Action": "ec2:RunInstances", "Resource": [ "arn:aws:ec2:us-east-2::image/ami-*"
      ],

      "Condition": { "StringEquals": { "ec2:Owner": "amazon"
         } } } ]
} Restrict access to specific Systems Manager parameters The following policy grants access to use Systems Manager parameters with a specific name.
The first statement grants users the permission to view Systems Manager parameters when selecting an AMI in the launch instance wizard. The second statement grants users the permission to only use parameters that are named prod-*.
JSON { "Version":"2012-10-17", "Statement": [{ "Effect": "Allow", "Action": [ "ssm:DescribeParameters"
      ], "Resource": "*"
   }, { "Effect": "Allow", "Action": [ "ssm:GetParameters"
      ], "Resource": "arn:aws:ssm:us-east-2:123456123456:parameter/prod-*"
   } ]
}

### Example: Work with security groups View security groups and add and remove rules The following policy grants users permission to view security groups in the Amazon EC2 console, to add and remove inbound and outbound rules, and to list and modify rule descriptions for existing security groups that have the tag Department=Test.
In the first statement, the ec2:DescribeTags action allows users to view tags in the console, which makes it easier for users to identify the security groups that they are allowed to modify.
JSON { "Version":"2012-10-17", "Statement": [{ "Effect": "Allow", "Action": [ "ec2:DescribeSecurityGroups", "ec2:DescribeSecurityGroupRules", "ec2:DescribeTags"
      ], "Resource": "*"
    }, { "Effect": "Allow", "Action": [ "ec2:AuthorizeSecurityGroupIngress", "ec2:RevokeSecurityGroupIngress", "ec2:AuthorizeSecurityGroupEgress", "ec2:RevokeSecurityGroupEgress", "ec2:ModifySecurityGroupRules", "ec2:UpdateSecurityGroupRuleDescriptionsIngress", "ec2:UpdateSecurityGroupRuleDescriptionsEgress"
      ], "Resource": [ "arn:aws:ec2:us-east-2:111122223333:security-group/*"
      ], "Condition": { "StringEquals": { "aws:ResourceTag/Department": "Test"
         }

      } }, { "Effect": "Allow", "Action": [ "ec2:ModifySecurityGroupRules"
      ], "Resource": [ "arn:aws:ec2:us-east-2:111122223333:security-group-rule/*"
      ]
   } ]} Work with the Create Security Group dialog box You can create a policy that allows users to work with the Create Security Group dialog box in the Amazon EC2 console. To use this dialog box, users must be granted permission to use at the least the following API actions:
- ec2:CreateSecurityGroup: To create a new security group.
- ec2:DescribeVpcs: To view a list of existing VPCs in the VPC list.
With these permissions, users can create a new security group successfully, but they cannot add any rules to it. To work with rules in the Create Security Group dialog box, you can add the following API actions to your policy:
- ec2:AuthorizeSecurityGroupIngress: To add inbound rules.
- ec2:AuthorizeSecurityGroupEgress: To add outbound rules to VPC security groups.
- ec2:RevokeSecurityGroupIngress: To modify or delete existing inbound rules. This is useful to allow users to use the Copy to new feature in the console. This feature opens the Create Security Group dialog box and populates it with the same rules as the security group that was selected.
- ec2:RevokeSecurityGroupEgress: To modify or delete outbound rules for VPC security groups. This is useful to allow users to modify or delete the default outbound rule that allows all outbound traffic.
- ec2:DeleteSecurityGroup: To cater for when invalid rules cannot be saved. The console first creates the security group, and then adds the specified rules. If the rules are invalid, the action

fails, and the console attempts to delete the security group. The user remains in the Create Security Group dialog box so that they can correct the invalid rule and try to create the security group again. This API action is not required, but if a user is not granted permission to use it and attempts to create a security group with invalid rules, the security group is created without any rules, and the user must add them afterward.
- ec2:UpdateSecurityGroupRuleDescriptionsIngress: To add or update descriptions of ingress (inbound) security group rules.
- ec2:UpdateSecurityGroupRuleDescriptionsEgress: To add or update descriptions of egress (outbound) security group rules.
- ec2:ModifySecurityGroupRules: To modify security group rules.
- ec2:DescribeSecurityGroupRules: To list security group rules.
The following policy grants users permission to use the Create Security Group dialog box, and to create inbound and outbound rules for security groups that are associated with a specific VPC (vpc-1a2b3c4d). Users can create security groups for a VPC, but they cannot add any rules to them. Similarly, users cannot add any rules to any existing security group that's not associated with VPC vpc-1a2b3c4d. Users are also granted permission to view all security groups in the console.
This makes it easier for users to identify the security groups to which they can add inbound rules.
This policy also grants users permission to delete security groups that are associated with VPC vpc-1a2b3c4d.
JSON { "Version":"2012-10-17", "Statement": [{ "Effect": "Allow", "Action": [ "ec2:DescribeSecurityGroups", "ec2:CreateSecurityGroup", "ec2:DescribeVpcs"
      ], "Resource": "*"
    }, { "Effect": "Allow", "Action": [ "ec2:DeleteSecurityGroup",

        "ec2:AuthorizeSecurityGroupIngress", "ec2:AuthorizeSecurityGroupEgress"
      ], "Resource": "arn:aws:ec2:us-east-2:111122223333:security-group/*", "Condition":{ "ArnEquals": { "ec2:Vpc": "arn:aws:ec2:us-east-2:111122223333:vpc/vpc-1a2b3c4d"
         } } } ]
}
### Example: Work with Elastic IP addresses To allow users to view Elastic IP addresses in the Amazon EC2 console, you must grant users permission to use the ec2:DescribeAddresses action.
To allow users to work with Elastic IP addresses, you can add the following actions to your policy.
- ec2:AllocateAddress: To allocate an Elastic IP address.
- ec2:ReleaseAddress: To release an Elastic IP address.
- ec2:AssociateAddress: To associate an Elastic IP address with an instance or a network interface.
- ec2:DescribeNetworkInterfaces and ec2:DescribeInstances: To work with the Associate address screen. The screen displays the available instances or network interfaces to which you can associate an Elastic IP address.
- ec2:DisassociateAddress: To disassociate an Elastic IP address from an instance or a network interface.
The following policy allows users to view, allocate, and associate Elastic IP addresses with instances. Users cannot associate Elastic IP addresses with network interfaces, disassociate Elastic IP addresses, or release them.
JSON { "Version":"2012-10-17",

    "Statement": [ { "Effect": "Allow", "Action": [ "ec2:DescribeAddresses", "ec2:AllocateAddress", "ec2:DescribeInstances", "ec2:AssociateAddress"
            ], "Resource": "*"
        } ]
}
### Example: Work with Reserved Instances The following policy allows users to view and modify Reserved Instances in your account, as well as purchase new Reserved Instances in the AWS Management Console.
This policy allows users to view all the Reserved Instances, as well as On-Demand Instances, in the account. It's not possible to set resource-level permissions for individual Reserved Instances.
JSON { "Version":"2012-10-17", "Statement": [{ "Effect": "Allow", "Action": [ "ec2:DescribeReservedInstances", "ec2:ModifyReservedInstances", "ec2:PurchaseReservedInstancesOffering", "ec2:DescribeInstances", "ec2:DescribeInstanceTypes", "ec2:DescribeAvailabilityZones", "ec2:DescribeReservedInstancesOfferings"
      ], "Resource": "*"
   } ]
}

The ec2:DescribeAvailabilityZones action is necessary to ensure that the Amazon EC2 console can display information about the Availability Zones in which you can purchase Reserved Instances. The ec2:DescribeInstances action is not required, but ensures that the user can view the instances in the account and purchase reservations to match the correct specifications.
You can adjust the API actions to limit user access, for example removing ec2:DescribeInstances and ec2:DescribeAvailabilityZones means the user has read- only access.
## AWS managed policies for Amazon EC2 To add permissions to users, groups, and roles, it is easier to use AWS managed policies than to write policies yourself. It takes time and expertise to create IAM customer managed policies that provide your team with only the permissions they need. To get started quickly, you can use our AWS managed policies. These policies cover common use cases and are available in your AWS account. For more information about AWS managed policies, see AWS managed policies in the IAM User Guide.
AWS services maintain and update AWS managed policies. You can't change the permissions in AWS managed policies. Services occasionally add additional permissions to an AWS managed policy to support new features. This type of update affects all identities (users, groups, and roles) where the policy is attached. Services are most likely to update an AWS managed policy when a new feature is launched or when new operations become available. Services do not remove permissions from an AWS managed policy, so policy updates won't break your existing permissions.
Additionally, AWS supports managed policies for job functions that span multiple services. For example, the ReadOnlyAccess AWS managed policy provides read-only access to all AWS services and resources. When a service launches a new feature, AWS adds read-only permissions for new operations and resources. For a list and descriptions of job function policies, see AWS managed policies for job functions in the IAM User Guide.
### AWS managed policy: AmazonEC2FullAccess You can attach the AmazonEC2FullAccess policy to your IAM identities. This policy grants permissions that allow full access to Amazon EC2.
To view the permissions for this policy, see AmazonEC2FullAccess in the AWS Managed Policy Reference.

### AWS managed policy: AmazonEC2ReadOnlyAccess You can attach the AmazonEC2ReadOnlyAccess policy to your IAM identities. This policy grants permissions that allow read-only access to Amazon EC2.
To view the permissions for this policy, see AmazonEC2ReadOnlyAccess in the AWS Managed Policy Reference.
### AWS managed policy: AmazonEC2ImageReferencesAccessPolicy You can attach the AmazonEC2ImageReferencesAccessPolicy policy to your IAM identities.
This policy grants the permissions needed to use the EC2 DescribeImageReferences API, including permission to view EC2 instances, launch templates, Systems Manager parameters, and Image Builder recipes. The policy supports the IncludeAllResourceTypes flag and will continue to work when AWS adds support for new resource types, removing the need for future policy updates.
To view the permissions for this policy, see AmazonEC2ImageReferencesAccessPolicy in the AWS Managed Policy Reference.
### AWS managed policy: AWSEC2CapacityReservationFleetRolePolicy This policy is attached to the service-linked role named AWSServiceRoleForEC2CapacityReservationFleet to allow the service to create, modify, and cancel Capacity Reservations in a Capacity Reservation Fleet on your behalf. For more information, see Using service-linked roles for Capacity Reservation Fleet.
To view the permissions for this policy, see AWSEC2CapacityReservationFleetRolePolicy in the AWS Managed Policy Reference.
### AWS managed policy: AWSEC2FleetServiceRolePolicy This policy is attached to the service-linked role named AWSServiceRoleForEC2Fleet to allow EC2 Fleet to request, launch, terminate, and tag instances on your behalf. For more information, see Service-linked role for EC2 Fleet.
To view the permissions for this policy, see AWSEC2FleetServiceRolePolicy in the AWS Managed Policy Reference.

### AWS managed policy: AWSEC2SpotFleetServiceRolePolicy This policy is attached to the service-linked role named AWSServiceRoleForEC2SpotFleet to allow Spot Fleet to launch and manage instances on your behalf. For more information, see Service- linked role for Spot Fleet.
To view the permissions for this policy, see AWSEC2SpotFleetServiceRolePolicy in the AWS Managed Policy Reference.
### AWS managed policy: AWSEC2SpotServiceRolePolicy This policy is attached to the service-linked role named AWSServiceRoleForEC2Spot to allow Amazon EC2 to launch and manage Spot Instances on your behalf. For more information, see Service-linked role for Spot Instance requests.
To view the permissions for this policy, see AWSEC2SpotServiceRolePolicy in the AWS Managed Policy Reference.
### AWS managed policy: AWSEC2VssSnapshotPolicy You can attach this managed policy to the IAM instance profile role that you use for your Amazon EC2 Windows instances. The policy grants permissions to allow Amazon EC2 to create and manage VSS snapshots on your behalf.
To view the permissions for this policy, see AWSEC2VssSnapshotPolicy in the AWS Managed Policy Reference.
### AWS managed policy: DeclarativePoliciesEC2Report This policy is attached to the service-linked role named AWSServiceRoleForDeclarativePoliciesEC2Report to provide access to read-only APIs needed to generate the account status report for declarative policies.
To view the permissions for this policy, see DeclarativePoliciesEC2Report in the AWS Managed Policy Reference.
### AWS managed policy: EC2FastLaunchFullAccess You can attach the EC2FastLaunchFullAccess policy to your instance profile or other IAM role.
This policy grants full access to EC2 Fast Launch actions, and targeted permissions as follows.

Permissions details
- EC2 Fast Launch – Administrative access is granted, so that the role can enable or disable EC2 Fast Launch, and describe EC2 Fast Launch images.
- Amazon EC2 – Access is granted for Amazon EC2 RunInstances, CreateTags, Describe, and Create and Modify Launch Template operations. Access is also granted to create network and security group resources, authorize ingress rules, and delete resources that EC2 Fast Launch created.
- IAM – Access is granted to get and use instance profiles whose name contains ec2fastlaunch to create the EC2FastLaunchServiceRolePolicy service-linked role.
- CloudFormation – Access is granted for EC2 Fast Launch to describe and create CloudFormation stacks, and to delete stacks that it created.
To view the permissions for this policy, see EC2FastLaunchFullAccess in the AWS Managed Policy Reference.
### AWS managed policy: AWSEC2CapacityManagerServiceRolePolicy This policy is attached to the service-linked role named AWSServiceRoleForEC2CapacityManager to allow EC2 Capacity Manager to manage capacity resources and integrate with AWS Organizations on your behalf. For more information, see Service-linked roles for EC2 Capacity Manager.
To view the permissions for this policy, see AWSEC2CapacityManagerServiceRolePolicy in the AWS Managed Policy Reference.
### AWS managed policy: EC2FastLaunchServiceRolePolicy This policy is attached to the service-linked role named AWSServiceRoleForEC2FastLaunch to allow Amazon EC2 to create and manage a set of pre-provisioned snapshots that reduce the time it takes to launch instances from your EC2 Fast Launch-enabled AMI. For more information, see the section called "Service-linked role".
To view the permissions for this policy, see EC2FastLaunchServiceRolePolicy in the AWS Managed Policy Reference.

### AWS managed policy: Ec2InstanceConnect You can attach the Ec2InstanceConnect policy to your IAM identities. This policy grants permissions that allows customers to call EC2 Instance Connect to publish ephemeral keys to their EC2 instances and connect via ssh or the EC2 Instance Connect CLI.
To view the permissions for this policy, see Ec2InstanceConnect in the AWS Managed Policy Reference.
### AWS managed policy: Ec2InstanceConnectEndpoint This policy is attached to a service-linked role named AWSServiceRoleForEC2InstanceConnect to allow EC2 Instance Connect Endpoint to perform actions on your behalf. For more information, see Service-linked role for EC2 Instance Connect Endpoint.
To view the permissions for this policy, see Ec2InstanceConnectEndpoint in the AWS Managed Policy Reference. For a description of the updates to this policy, see Amazon EC2 updates to AWS managed policies.
### Amazon EC2 updates to AWS managed policies View details about updates to AWS managed policies for Amazon EC2 since this service began tracking these changes.
Change Description Date AWSEC2CapacityMana gerServiceRolePolicy –  New policy Amazon EC2 added this policy to allow you to manage capacity resources and integrate with AWS Organizat ions on your behalf.
October 15, 2025 AmazonEC2ImageRefe rencesAccessPolicy –  New policy Amazon EC2 added this policy to provide permissio n to scan all resources types supported by  the EC2 DescribeImageReferences API.
August 26, 2025 Ec2InstanceConnectEndpoint – Updated  policy To support the modification of existing Instance Connect July 31, 2025

Change Description Date Endpoints, Amazon EC2 updated this  policy to add permissions to assign and unassign IPv6 addresses and modify security groups on network interfaces created by EC2 Instance Connect Endpoint. Amazon EC2 also updated this policy to replace the Null condition operator with the StringLike condition operator.
EC2FastLaunchServiceRolePol icy –  Updated policy To help prevent orphaned resources, Amazon EC2 updated this policy to add permission to describe volumes, volume attribute s and network interfaces, and to delete volumes and network interfaces that EC2 Fast Launch created.
July 17, 2025 EC2FastLaunchFullAccess – Updated policy Amazon EC2 updated this policy to include Create and Modify Launch Template operations, to create network and security group resources , authorize ingress rules, and delete resources that EC2 Fast Launch created. It can additionally describe and create CloudFormation stacks, and delete stacks that EC2 Fast Launch created.
May 14, 2025

Change Description Date EC2FastLaunchServiceRolePol icy –  Updated policy Amazon EC2 updated this policy to add Amazon EventBridge access to create and manage event rules for EC2 Fast Launch. Additiona lly, EC2 Fast Launch can now describe CloudFormation stacks, launch an instance f rom an AMI that's associate d with AWS License Manager, get a list of AWS KMS grants it created that can be retired, and delete launch templates that it created.
May 14, 2025 AWSEC2CapacityRese rvationFleetRolePolicy – Updated permissions Amazon EC2 updated the AWSEC2CapacityRese rvationFleetRolePo licy  managed policy to use the  ArnLike condition operator instead of the StringLike  condition operator.
March 03, 2025 AmazonEC2ReadOnlyAccess –  Added permissions Amazon EC2 added a permission that allows you to retrieve security groups using the GetSecurityGroupsF orVpc  operation.
December 27, 2024

Change Description Date EC2FastLaunchFullAccess – New policy Amazon EC2 added this policy to perform API actions related to the EC2 Fast Launch feature from an instance. The policy can be attached to the instance profile for an instance that's launched from a EC2 Fast Launch enabled AMI.
May 14, 2024 AWSEC2VssSnapshotPolicy – New policy Amazon EC2 added the AWSEC2VssSnapshotP olicy  policy that  contai ns permissions to create and add tags to Amazon Machine Images  (AMIs) and EBS snapshots.
March 28, 2024 Ec2InstanceConnectEndpoint – New  policy Amazon EC2 added the Ec2InstanceConnect Endpoint  policy. This policy is attached  to the AWSServiceRoleForE C2InstanceConnect service-l inked  role, to allow Amazon EC2 to perform actions on your behalf when you  create an EC2 Instance Connect Endpoint.
January 24, 2023

Change Description Date EC2FastLaunchServiceRolePol icy –  New policy Amazon EC2 added the EC2 Fast Launch feature to enable Windows AMIs to launch instances faster by creating a set of pre-provisioned snapshots.
November 26, 2021 Amazon EC2 started tracking changes Amazon EC2 started tracking changes to its AWS managed policies March 1, 2021
## IAM roles for Amazon EC2 Applications must sign their API requests with AWS credentials. Therefore, if you are an application developer, you need a strategy for managing credentials for your applications that run on EC2 instances. For example, you can securely distribute your AWS credentials to the instances, enabling the applications on those instances to use your credentials to sign requests, while protecting your credentials from other users. However, it's challenging to securely distribute credentials to each instance, especially those that AWS creates on your behalf, such as Spot Instances or instances in Auto Scaling groups. You must also be able to update the credentials on each instance when you rotate your AWS credentials.
We designed IAM roles so that your applications can securely make API requests from your instances, without requiring you to manage the security credentials that the applications use.
Instead of creating and distributing your AWS credentials, you can delegate permission to make API requests using IAM roles as follows:
1. Create an IAM role.
2. Define which accounts or AWS services can assume the role.
3. Define which API actions and resources the application can use after assuming the role.
4. Specify the role when you launch your instance, or attach the role to an existing instance.
5. Have the application retrieve a set of temporary credentials and use them.

For example, you can use IAM roles to grant permissions to applications running on your instances that need to use a bucket in Amazon S3. You can specify permissions for IAM roles by creating a policy in JSON format. These are similar to the policies that you create for users. If you change a role, the change is propagated to all instances.
Note Amazon EC2 IAM role credentials are not subject to maximum session durations configured in the role. For more information, see Methods to assume a role in the IAM User Guide.
When creating IAM roles, associate least privilege IAM policies that restrict access to the specific API calls the application requires. For Windows-to-Windows communication, use well-defined and well-documented Windows groups and roles to grant application-level access between Windows instances. Groups and roles allow customers to define least privilege application and NTFS folder- level permissions to limit access to application-specific requirements.
You can only attach one IAM role to an instance, but you can attach the same role to many instances. For more information about creating and using IAM roles, see Roles in the IAM User Guide.
You can apply resource-level permissions to your IAM policies to control the users' ability to attach, replace, or detach IAM roles for an instance. For more information, see Supported resource-level permissions for Amazon EC2 API actions and the following example: Example: Work with IAM roles.
Contents
- Instance profiles
- Permissions for your use case
- Retrieve security credentials from instance metadata
- Grant permissions to attach an IAM role to an instance
- Attach an IAM role to an instance
- Instance identity roles for Amazon EC2 instances
### Instance profiles Amazon EC2 uses an instance profile as a container for an IAM role. When you create an IAM role using the IAM console, the console creates an instance profile automatically and gives it the same

name as the role to which it corresponds. If you use the Amazon EC2 console to launch an instance with an IAM role or to attach an IAM role to an instance, you choose the role based on a list of instance profile names.
If you use the AWS CLI, API, or an AWS SDK to create a role, you create the role and instance profile as separate actions, with potentially different names. If you then use the AWS CLI, API, or an AWS SDK to launch an instance with an IAM role or to attach an IAM role to an instance, specify the instance profile name.
An instance profile can contain only one IAM role. You can include an IAM role in multiple instance profiles.
To update permissions for an instance, replace its instance profile. We do not recommend removing a role from an instance profile, because there is a delay of up to one hour before this change takes effect.
For more information, see Use instance profiles in the IAM User Guide.
### Permissions for your use case When you first create an IAM role for your applications, you might sometimes grant permissions beyond what is required. Before launching your application in your production environment, you can generate an IAM policy that is based on the access activity for an IAM role. IAM Access Analyzer reviews your AWS CloudTrail logs and generates a policy template that contains the permissions that have been used by the role in your specified date range. You can use the template to create a managed policy with fine-grained permissions and then attach it to the IAM role. That way, you grant only the permissions that the role needs to interact with AWS resources for your specific use case. This helps you adhere to the best practice of granting least privilege. For more information, see IAM Access Analyzer policy generation in the IAM User Guide.
### Retrieve security credentials from instance metadata An application on the instance retrieves the security credentials provided by the role from the instance metadata item iam/security-credentials/role-name. The application is granted the permissions for the actions and resources that you've defined for the role through the security credentials associated with the role. These security credentials are temporary and we rotate them automatically. We make new credentials available at least five minutes before the expiration of the old credentials.

For more information about instance metadata, see Use instance metadata to manage your EC2 instance.
Warning If you use services that use instance metadata with IAM roles, ensure that you don't expose your credentials when the services make HTTP calls on your behalf. The types of services that could expose your credentials include HTTP proxies, HTML/CSS validator services, and XML processors that support XML inclusion.
For your Amazon EC2 workloads, we recommend that you retrieve session credentials using the method described below. These credentials should enable your workload to make AWS API requests, without needing to use sts:AssumeRole to assume the same role that is already associated with the instance. Unless you need to pass session tags for attribute-based access control (ABAC) or pass a session policy to further restrict permissions of the role, such role assumption calls are unnecessary as they create a new set of the same temporary role session credentials.
If your workload uses a role to assume itself, you must create a trust policy that explicitly allows that role to assume itself. If you do not create the trust policy, you get an AccessDenied error. For more information, see  Update a role trust policy in the IAM User Guide.
IMDSv2 Linux Run the following command from your Linux instance to retrieve the security credentials for an IAM role.
TOKEN=`curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata- token-ttl-seconds: 21600"` \ && curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/ meta-data/iam/security-credentials/role-name Windows Run the following cmdlet from your Windows instance to retrieve the security credentials for an IAM role.

[string]$token = Invoke-RestMethod `
    -Headers @{"X-aws-ec2-metadata-token-ttl-seconds" = "21600"} `
    -Method PUT -Uri http://169.254.169.254/latest/api/token Invoke-RestMethod `
    -Headers @{"X-aws-ec2-metadata-token" = $token} `
    -Method GET -Uri http://169.254.169.254/latest/meta-data/iam/security- credentials/role-name IMDSv1 Linux Run the following command from your Linux instance to retrieve the security credentials for an IAM role. curl http://169.254.169.254/latest/meta-data/iam/security-credentials/role-name Windows Run the following cmdlet from your Windows instance to retrieve the security credentials for an IAM role.
Invoke-RestMethod -uri http://169.254.169.254/latest/meta-data/iam/security- credentials/role-name The following is example output. If you are not able to retrieve the security credentials, see I can't access the temporary security credentials on my EC2 instance in the IAM User Guide.
{ "Code" : "Success", "LastUpdated" : "2012-04-26T16:39:16Z", "Type" : "AWS-HMAC", "AccessKeyId" : "ASIAIOSFODNN7EXAMPLE", "SecretAccessKey" : "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY", "Token" : "token", "Expiration" : "2017-05-17T15:09:54Z"
}

For applications, AWS CLI, and Tools for Windows PowerShell commands that run on the instance, you do not have to explicitly get the temporary security credentials—the AWS SDKs, AWS CLI, and Tools for Windows PowerShell automatically get the credentials from the EC2 instance metadata service and use them. To make a call outside of the instance using temporary security credentials (for example, to test IAM policies), you must provide the access key, secret key, and the session token. For more information, see Using Temporary Security Credentials to Request Access to AWS Resources in the IAM User Guide.
### Grant permissions to attach an IAM role to an instance The identities in your AWS account, such as IAM users, must have specific permissions to launch an Amazon EC2 instance with an IAM role, attach an IAM role to an instance, replace the IAM role for an instance, or detach an IAM role from an instance. You must grant permission to use the following API actions as required:
- iam:PassRole
- ec2:AssociateIamInstanceProfile
- ec2:DisassociateIamInstanceProfile
- ec2:ReplaceIamInstanceProfileAssociation Note If you specify the resource for iam:PassRole as *, this would grant access to pass any of your IAM roles to an instance. To follow the best practice of least privilege, specify the ARNs of specific IAM roles with iam:PassRole, as shown in the example policy below.
Example policy for programmatic access The following IAM policy grants permissions to launch instances with an IAM role, attach an IAM role to an instance, or replace the IAM role for an instance using the AWS CLI or the Amazon EC2 API.
JSON { "Version":"2012-10-17",

  "Statement": [ { "Effect": "Allow", "Action": [ "ec2:RunInstances", "ec2:AssociateIamInstanceProfile", "ec2:DisassociateIamInstanceProfile", "ec2:ReplaceIamInstanceProfileAssociation"
      ], "Resource": "*"
    }, { "Effect": "Allow", "Action": "iam:PassRole", "Resource": "arn:aws:iam::123456789012:role/DevTeam*"
    } ]
} Additional requirement for console access To grant permissions to complete the same tasks using the Amazon EC2 console, you must also include the iam:ListInstanceProfiles API action.
### Attach an IAM role to an instance You can create an IAM role and attach it to an instance during or after launch. You can also replace or detach IAM roles.
To attach an IAM role to an instance at launch using the Amazon EC2 console, expand Advanced details. For IAM instance profile, select the IAM role.
Note If you created your IAM role using the IAM console, the instance profile was created for you and given the same name as the role. If you created your IAM role using the AWS CLI, API, or an AWS SDK, you might have given your instance profile a different name than the role.
You can attach an IAM role to an instance that is running or stopped. If the instance already has an IAM role attached, you must replace it with the new IAM role.

Console To attach an IAM role to an instance
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Instances.
3. Select the instance.
4. Choose Actions, Security, Modify IAM role.
5. For IAM role, select the IAM instance profile.
6. Choose Update IAM role.
AWS CLI To attach an IAM role to an instance Use the associate-iam-instance-profile command to attach the IAM role to the instance. When you specify the instance profile, you can use either the Amazon Resource Name (ARN) of the instance profile, or you can use its name. aws ec2 associate-iam-instance-profile \ --instance-id i-1234567890abcdef0 \ --iam-instance-profile Name="TestRole-1"
PowerShell To attach an IAM role to an instance Use the Register-EC2IamInstanceProfile cmdlet.
Register-EC2IamInstanceProfile `
    -InstanceId i-1234567890abcdef0 `
    -IamInstanceProfile_Name TestRole-1 To replace the IAM role on an instance that already has an attached IAM role, the instance must be running. You can do this if you want to change the IAM role for an instance without detaching the existing one first. For example, you can do this to ensure that API actions performed by applications running on the instance are not interrupted.

Console To replace an IAM role for an instance
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Instances.
3. Select the instance.
4. Choose Actions, Security, Modify IAM role.
5. For IAM role, select the IAM instance profile.
6. Choose Update IAM role.
AWS CLI To replace an IAM role for an instance
1. If required, use the describe-iam-instance-profile-associations command to get the association ID. aws ec2 describe-iam-instance-profile-associations \ --filters Name=instance-id,Values=i-1234567890abcdef0 \ --query IamInstanceProfileAssociations.AssociationId
2. Use the replace-iam-instance-profile-association command. Specify the association ID for the existing instance profile and the ARN or name of the new instance profile. aws ec2 replace-iam-instance-profile-association \ --association-id iip-assoc-0044d817db6c0a4ba \ --iam-instance-profile Name="TestRole-2"
PowerShell To replace an IAM role for an instance
1. If required, use the Get-EC2IamInstanceProfileAssociation cmdlet to get the association ID.
(Get-EC2IamInstanceProfileAssociation -Filter @{Name="instance-id"; Values="i-0636508011d8e966a"}).AssociationId

2. Use the Set-EC2IamInstanceProfileAssociation cmdlet. Specify the association ID for the existing instance profile and the ARN or name of the new instance profile.
Set-EC2IamInstanceProfileAssociation `
    -AssociationId iip-assoc-0044d817db6c0a4ba `
    -IamInstanceProfile_Name TestRole-2 You can detach an IAM role from an instance that is running or stopped.
Console To detach an IAM role from an instance
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Instances.
3. Select the instance.
4. Choose Actions, Security, Modify IAM role.
5. For IAM role, choose No IAM Role.
6. Choose Update IAM role.
7. When promoted for confirmation, enter Detach, and then choose Detach.
AWS CLI To detach an IAM role from an instance
1. If required, use describe-iam-instance-profile-associations to get the association ID for the IAM instance profile to detach. aws ec2 describe-iam-instance-profile-associations \ --filters Name=instance-id,Values=i-1234567890abcdef0 \ --query IamInstanceProfileAssociations.AssociationId
2. Use the disassociate-iam-instance-profile command. aws ec2 disassociate-iam-instance-profile --association-id iip- assoc-0044d817db6c0a4ba

PowerShell To detach an IAM role from an instance
1. If required, use Get-EC2IamInstanceProfileAssociation to get the association ID for the IAM instance profile to detach.
(Get-EC2IamInstanceProfileAssociation -Filter @{Name="instance-id"; Values="i-0636508011d8e966a"}).AssociationId
2. Use the Unregister-EC2IamInstanceProfile cmdlet.
Unregister-EC2IamInstanceProfile -AssociationId iip-assoc-0044d817db6c0a4ba
### Instance identity roles for Amazon EC2 instances Each Amazon EC2 instance that you launch has an instance identity role that represents its identity.
An instance identity role is a type of IAM role. AWS services and features that are integrated to use the instance identity role can use it to identify the instance to the service.
The instance identity role credentials are accessible from the Instance Metadata Service (IMDS) at /identity-credentials/ec2/security-credentials/ec2-instance. The credentials consist of an AWS temporary access key pair and a session token. They are used to sign AWS Sigv4 requests to the AWS services that use the instance identity role. The credentials are present in the instance metadata regardless of whether a service or feature that makes use of instance identity roles is enabled on the instance.
Instance identity roles are automatically created when an instance is launched, have no role-trust policy document, and are not subject to any identity or resource policy.
#### Supported services The following AWS services use the instance identity role:
- Amazon EC2 – EC2 Instance Connect uses the instance identity role to update the host keys for a Linux instance.
- Amazon GuardDuty – GuardDuty Runtime Monitoring uses the instance identity role to allow the runtime agent to send security telemetry to the GuardDuty VPC endpoint.
