# Work with Spot Fleet

Source: apps/user-manuals/aws/ec2-ug.pdf

---

# Work with Spot Fleet To start using a Spot Fleet, create a request that includes the total target capacity for Spot Instances, an optional On-Demand portion, and either manually specify an AMI and a key pair, or specify a launch template that includes the configuration for the instances in the fleet. You can optionally specify additional parameters, or let the fleet use default values. You can also tag the fleet request, and its instances and volumes, when you create the fleet.
The fleet launches On-Demand Instances when there is available capacity, and launches Spot Instances when your maximum price exceeds the Spot price and capacity is available.
Once your fleet is launched, you can describe the fleet request, the instances in the fleet, and any fleet events. You can also assign additional tags as needed.
If you need to change any fleet parameters, such as the total target capacity, you can modify the fleet, provided it was configured to maintain capacity. You can't modify the capacity of a one-time request after it's been submitted.
The fleet request remains active until it expires or you cancel (delete) it. When you cancel the fleet request, you can either terminate the instances or leave them running. If you choose to leave them running, the On-Demand Instances run until you terminate them, and the Spot Instances run until they're interrupted or you terminate them.
Topics
- Spot Fleet request states
- Spot Fleet permissions
- Create a Spot Fleet
- Tag a new or existing Spot Fleet request and the instances and volumes it launches
- Describe a Spot Fleet request, its instances, and event history
- Modify a Spot Fleet request
- Cancel (delete) a Spot Fleet request
- Understand automatic scaling for Spot Fleet
## Spot Fleet request states A Spot Fleet request can be one of various states, with each state indicating a different stage of the request's lifecycle and its management of instances.

A Spot Fleet request can be in one of the following states: submitted The Spot Fleet request is being evaluated and Amazon EC2 is preparing to launch the target number of instances. If a request would exceed your Spot Fleet quotas, it is canceled immediately. active The Spot Fleet has been validated and Amazon EC2 is attempting to maintain the target number of running Spot Instances. The request remains in this state until it is modified or canceled. modifying The Spot Fleet request is being modified. The request remains in this state until the modification is fully processed or the request is canceled. Only a maintain fleet type can be modified. This state does not apply to a one-time request fleet type. cancelled_running The Spot Fleet is canceled (deleted) and does not launch additional Spot Instances. Its existing instances continue to run until they are interrupted or terminated manually. The request remains in this state until all instances are interrupted or terminated. cancelled_terminating The Spot Fleet is canceled (deleted) and its instances are terminating. The request remains in this state until all instances are terminated. cancelled The Spot Fleet is canceled (deleted) and has no running instances. The request is deleted two days after its instances are terminated.
## Spot Fleet permissions If your users will create or manage a Spot Fleet, you need to grant them the required permissions.
If you use the Amazon EC2 console to create a Spot Fleet, it creates two service-linked roles named AWSServiceRoleForEC2SpotFleet and AWSServiceRoleForEC2Spot, and a role named aws-ec2-spot-fleet-tagging-role that grant the Spot Fleet the permissions to request,

launch, terminate, and tag resources on your behalf. If you use the AWS CLI or an API, you must ensure that these roles exist.
Use the following instructions to grant the required permissions and create the roles.
Permissions and roles
- Grant permission to users for Spot Fleet
- Service-linked role for Spot Fleet
- Service-linked role for Spot Instances
- IAM role for tagging a Spot Fleet
### Grant permission to users for Spot Fleet If your users will create or manage a Spot Fleet, be sure to grant them the required permissions.
To create a policy for Spot Fleet
1. Open the IAM console at https://console.aws.amazon.com/iam/.
2. In the navigation pane, choose Policies, Create policy.
3. On the Create policy page, choose JSON, and replace the text with the following.
JSON { "Version":"2012-10-17", "Statement": [ { "Effect": "Allow", "Action": [ "ec2:RunInstances", "ec2:CreateTags", "ec2:RequestSpotFleet", "ec2:ModifySpotFleetRequest", "ec2:CancelSpotFleetRequests", "ec2:DescribeSpotFleetRequests", "ec2:DescribeSpotFleetInstances", "ec2:DescribeSpotFleetRequestHistory"
            ], "Resource": "*"

        }, { "Effect": "Allow", "Action": "iam:PassRole", "Resource": "arn:aws:iam::*:role/aws-ec2-spot-fleet-tagging-role"
        }, { "Effect": "Allow", "Action": [ "iam:CreateServiceLinkedRole", "iam:ListRoles", "iam:ListInstanceProfiles"
            ], "Resource": "*"
        } ]
} The preceding example policy grants a user the permissions required for most Spot Fleet use cases. To limit the user to specific API actions, specify only those API actions instead.
Required EC2 and IAM APIs The following APIs must be included in the policy:
- ec2:RunInstances – Required to launch instances in a Spot Fleet
- ec2:CreateTags – Required to tag the Spot Fleet request, instances, or volumes
- iam:PassRole – Required to specify the Spot Fleet role
- iam:CreateServiceLinkedRole – Required to create the service-linked role
- iam:ListRoles – Required to enumerate existing IAM roles
- iam:ListInstanceProfiles – Required to enumerate existing instance profiles Important If you specify a role for the IAM instance profile in the launch specification or launch template, you must grant the user the permission to pass the role to the service. To do this, in the IAM policy include "arn:aws:iam::*:role/IamInstanceProfile-

role" as a resource for the iam:PassRole action. For more information, see Granting a user permissions to pass a role to an AWS service in the IAM User Guide.
Spot Fleet APIs Add the following Spot Fleet API actions to your policy, as needed:
- ec2:RequestSpotFleet
- ec2:ModifySpotFleetRequest
- ec2:CancelSpotFleetRequests
- ec2:DescribeSpotFleetRequests
- ec2:DescribeSpotFleetInstances
- ec2:DescribeSpotFleetRequestHistory Optional IAM APIs (Optional) To enable a user to create roles or instance profiles using the IAM console, you must add the following actions to the policy:
- iam:AddRoleToInstanceProfile
- iam:AttachRolePolicy
- iam:CreateInstanceProfile
- iam:CreateRole
- iam:GetRole
- iam:ListPolicies
4. Choose Review policy.
5. On the Review policy page, enter a policy name and description, and choose Create policy.
6. To provide access, add permissions to your users, groups, or roles:
- Users and groups in AWS IAM Identity Center:
Create a permission set. Follow the instructions in Create a permission set in the AWS IAM Identity Center User Guide.
- Users managed in IAM through an identity provider:

Create a role for identity federation. Follow the instructions in Create a role for a third-party identity provider (federation) in the IAM User Guide.
- IAM users:
- Create a role that your user can assume. Follow the instructions in Create a role for an IAM user in the IAM User Guide.
- (Not recommended) Attach a policy directly to a user or add a user to a user group. Follow the instructions in Adding permissions to a user (console) in the IAM User Guide.
### Service-linked role for Spot Fleet Amazon EC2 uses service-linked roles for the permissions that it requires to call other AWS services on your behalf. A service-linked role is a unique type of IAM role that is linked directly to an AWS service. Service-linked roles provide a secure way to delegate permissions to AWS services because only the linked service can assume a service-linked role. For more information, see Service-linked roles in the IAM User Guide.
Amazon EC2 uses the service-linked role named AWSServiceRoleForEC2SpotFleet to launch and manage instances on your behalf.
Important If you specify an encrypted AMI or an encrypted Amazon EBS snapshot in your Spot Fleet, you must grant the AWSServiceRoleForEC2SpotFleet role permission to use the CMK so that Amazon EC2 can launch instances on your behalf. For more information, see Grant access to CMKs for use with encrypted AMIs and EBS snapshots.
#### Permissions granted by AWSServiceRoleForEC2SpotFleet The AWSServiceRoleForEC2SpotFleet role grants the Spot Fleet permission to request, launch, terminate, and tag instances on your behalf. Amazon EC2 uses this service-linked role to complete the following actions:
- ec2:RequestSpotInstances - Request Spot Instances
- ec2:RunInstances - Launch instances
- ec2:TerminateInstances - Terminate instances

- ec2:DescribeImages - Describe Amazon Machine Images (AMIs) for the instances
- ec2:DescribeInstanceStatus - Describe the status of the instances
- ec2:DescribeSubnets - Describe the subnets for the instances
- ec2:CreateTags - Add tags to the Spot Fleet request, instances, and volumes
- elasticloadbalancing:RegisterInstancesWithLoadBalancer - Add the specified instances to the specified load balancer
- elasticloadbalancing:RegisterTargets - Register the specified targets with the specified target group
#### Create the service-linked role Under most circumstances, you don't need to manually create a service-linked role. Amazon EC2 creates the AWSServiceRoleForEC2SpotFleet service-linked role the first time you create a Spot Fleet using the console.
If you had an active Spot Fleet request before October 2017, when Amazon EC2 began supporting this service-linked role, Amazon EC2 created the AWSServiceRoleForEC2SpotFleet role in your AWS account. For more information, see A new role appeared in my AWS account in the IAM User Guide.
If you use the AWS CLI or an API to create a Spot Fleet, you must first ensure that this role exists.
To create the AWSServiceRoleForEC2SpotFleet role for Spot Fleet using the console
1. Open the IAM console at https://console.aws.amazon.com/iam/.
2. In the navigation pane, choose Roles.
3. Choose Create role.
4. On the Select trusted entity page, do the following: a.
For Trusted entity type, choose AWS service. b.
Under Use case, for Service or use case, choose EC2. c.
For Use case, choose EC2 - Spot Fleet.

Note The EC2 - Spot Fleet use case will automatically create a policy with the required IAM permissions and will suggest AWSEC2SpotFleetServiceRolePolicy as the role name. d.
Choose Next.
5. On the Add permissions page, choose Next.
6. On the Name, review, and create page, choose Create role.
To create the AWSServiceRoleForEC2SpotFleet role for Spot Fleet using the AWS CLI Use the create-service-linked-role command as follows. aws iam create-service-linked-role --aws-service-name spotfleet.amazonaws.com If you no longer need to use Spot Fleet, we recommend that you delete the AWSServiceRoleForEC2SpotFleet role. After this role is deleted from your account, Amazon EC2 will create the role again if you request a Spot Fleet using the console. For more information, see Deleting a service-linked role in the IAM User Guide.
#### Grant access to CMKs for use with encrypted AMIs and EBS snapshots If you specify an encrypted AMI or an encrypted Amazon EBS snapshot in your Spot Fleet request and you use a customer managed key for encryption, you must grant the AWSServiceRoleForEC2SpotFleet role permission to use the CMK so that Amazon EC2 can launch instances on your behalf. To do this, you must add a grant to the CMK, as shown in the following procedure.
When providing permissions, grants are an alternative to key policies. For more information, see Using Grants and Using Key Policies in AWS KMS in the AWS Key Management Service Developer Guide.
To grant the AWSServiceRoleForEC2SpotFleet role permissions to use the CMK
- Use the create-grant command to add a grant to the CMK and to specify the principal (the AWSServiceRoleForEC2SpotFleet service-linked role) that is given permission to perform the

operations that the grant permits. The CMK is specified by the key-id parameter and the ARN of the CMK. The principal is specified by the grantee-principal parameter and the ARN of the AWSServiceRoleForEC2SpotFleet service-linked role. aws kms create-grant \ --region us-east-1 \ --key-id arn:aws:kms:us- east-1:444455556666:key/1234abcd-12ab-34cd-56ef-1234567890ab \ --grantee-principal arn:aws:iam::111122223333:role/aws-service-role/ spotfleet.amazonaws.com/AWSServiceRoleForEC2SpotFleet \ --operations "Decrypt" "Encrypt" "GenerateDataKey"
 "GenerateDataKeyWithoutPlaintext" "CreateGrant" "DescribeKey" "ReEncryptFrom"
 "ReEncryptTo"
### Service-linked role for Spot Instances Amazon EC2 uses the service-linked role named AWSServiceRoleForEC2Spot to launch and manage Spot Instances on your behalf. For more information, see Service-linked role for Spot Instance requests.
### IAM role for tagging a Spot Fleet The aws-ec2-spot-fleet-tagging-role IAM role grants the Spot Fleet permission to tag the Spot Fleet request, instances, and volumes. For more information, see Tag a new or existing Spot Fleet request and the instances and volumes it launches.
Important If you choose to tag instances in the fleet and you also choose to maintain target capacity (the Spot Fleet request is of type maintain), the differences in the permissions that are set for the user and the IamFleetRole might lead to inconsistent tagging behavior of instances in the fleet. If the IamFleetRole does not include the CreateTags permission, some of the instances launched by the fleet might not be tagged. While we are working to fix this inconsistency, to ensure that all instances launched by the fleet are tagged, we recommend that you use the aws-ec2-spot-fleet-tagging- role role for the IamFleetRole. Alternatively, to use an existing role, attach the AmazonEC2SpotFleetTaggingRole AWS Managed Policy to the existing role. Otherwise, you need to manually add the CreateTags permission to your existing policy.

To create the IAM role for tagging a Spot Fleet
1. Open the IAM console at https://console.aws.amazon.com/iam/.
2. In the navigation pane, choose Roles.
3. Choose Create role.
4. On the Select trusted entity page, under Trusted entity type, choose AWS service.
5. Under Use case, from Use cases for other AWS services, choose EC2, and then choose EC2 - Spot Fleet Tagging.
6. Choose Next.
7. On the Add permissions page, choose Next.
8. On the Name, review, and create page, for Role name, enter a name for the role (for example, aws-ec2-spot-fleet-tagging-role).
9. Review the information on the page, and then choose Create role.
#### Cross-service confused deputy prevention The confused deputy problem is a security issue where an entity that doesn't have permission to perform an action can coerce a more-privileged entity to perform the action. We recommend that you use the aws:SourceArn and aws:SourceAccount global condition context keys in the aws-ec2-spot-fleet-tagging-role trust policy to limit the permissions that Spot Fleet gives another service to the resource.
To add the aws:SourceArn and aws:SourceAccount condition keys to the aws-ec2-spot- fleet-tagging-role trust policy
1. Open the IAM console at https://console.aws.amazon.com/iam/.
2. In the navigation pane, choose Roles.
3. Find the aws-ec2-spot-fleet-tagging-role that you created previously and choose the link (not the checkbox).
4. Under Summary, choose the Trust relationships tab, and then choose Edit trust policy.
5. In the JSON statement, add a Condition element containing your aws:SourceAccount and aws:SourceArn global condition context keys to prevent the confused deputy problem, as follows:
"Condition": {

      "ArnLike": { "aws:SourceArn": "arn:aws:ec2:us-east-1:111122223333:spot-fleet-request/ sfr-*"
      }, "StringEquals": { "aws:SourceAccount": "111122223333"
      } Note If the aws:SourceArn value contains the account ID and you use both global condition context keys, the aws:SourceAccount value and the account in the aws:SourceArn value must use the same account ID when used in the same policy statement.
The final trust policy will be as follows:
JSON { "Version":"2012-10-17", "Statement": { "Sid": "ConfusedDeputyPreventionExamplePolicy", "Effect": "Allow", "Principal": { "Service": "spotfleet.amazonaws.com"
    }, "Action": "sts:AssumeRole", "Condition": { "ArnLike": { "aws:SourceArn": "arn:aws:ec2:us-east-1:111122223333:spot-fleet- request/sfr-*"
      }, "StringEquals": { "aws:SourceAccount": "111122223333"
      } } } }

6. Choose Update policy.
The following table provides potential values for aws:SourceArn to limit the scope of the your aws-ec2-spot-fleet-tagging-role in varying degrees of specificity.
API operation Called service Scope aws:SourceArn RequestSpotFleet AWS STS (AssumeRole )
Limit the AssumeRol e  capability on aws-ec2-spot- fleet-tagging- role  to  spot-f leet-requests in the specified account. arn:aws:e c2:*: 123456789 012 :spot-fle et-request/ sfr-* RequestSpotFleet AWS STS (AssumeRole )
Limit the AssumeRol e  capability on aws-ec2-spot- fleet-tagging- role  to  spot-f leet-requests in the specified account and specified  Region.
Note that this role will not be usable in other  Regions. arn:aws:e c2: us-east-1 :123456789 012 :spot-fle et-request/ sfr-* RequestSpotFleet AWS STS (AssumeRole )
Limit the AssumeRol e  capability on   aws-ec2-s pot-fleet- tagging-role to only actions  a ffecting the fleet sfr-11111111-1111- 1111-1111 -111111111111. arn:aws:e c2: us-east-1 :123456789 012 :spot-fle et-request/ sfr-11111111- 1111-1111 -1111-111 111111111

API operation Called service Scope aws:SourceArn Note that this role may not be usable for other Spot Fleets.  A lso, this role cannot be used to launch any new Spot Fleets  th rough request-spot- fleet.
## Create a Spot Fleet Using the AWS Management Console, you can quickly create a Spot Fleet request by choosing only an AMI and your desired total target capacity. Amazon EC2 will configure a fleet that best meets your needs and follows Spot best practices. Alternatively, you can modify any of the default settings.
If you want to include On-Demand Instances in your fleet, you must specify a launch template in your request and specify you desired On-Demand capacity.
The fleet launches On-Demand Instances when capacity is available, and launches Spot Instances when your maximum price exceeds the Spot price and capacity is available.
If your fleet includes Spot Instances and is of type maintain, Amazon EC2 will attempt to maintain your fleet target capacity when your Spot Instances are interrupted.
Required permissions For more information, see the section called "Spot Fleet permissions".
Tasks
- Quickly create a Spot Fleet request
- Create a Spot Fleet request using defined parameters
- Create a Spot Fleet that replaces unhealthy Spot Instances

### Quickly create a Spot Fleet request Follow these steps to quickly create a Spot Fleet request using the Amazon EC2 console.
To create a Spot Fleet request using the recommended settings
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Spot Requests.
3. If you are new to Spot, you see a welcome page; choose Get started. Otherwise, choose Create Spot Fleet Request.
4. Under Launch parameters, choose Manually configure launch parameters.
5. For AMI, choose an AMI.
6. Under Target capacity, for Total target capacity, specify the number of units to request. For the type of unit, you can choose Instances, vCPUs, or Memory (GiB).
7. Under Your fleet request at a glance, review your fleet configuration, and choose Launch.
### Create a Spot Fleet request using defined parameters You can create a Spot Fleet by using parameters that you define.
Console To create a Spot Fleet request using defined parameters
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Spot Requests.
3. If you are new to Spot, you see a welcome page; choose Get started. Otherwise, choose Create Spot Fleet Request.
4. For Launch parameters, you can either manually configure the launch parameters or you can use a launch template, as follows: a.
[Manually configure] To define the launch parameters in the Amazon EC2 console, choose Manually configure launch parameters, and then do the following: i.
For AMI, choose one of the basic AMIs provided by AWS, or choose Search for AMI to use an AMI from our user community, the AWS Marketplace, or one of your own.

Note If an AMI specified in the launch parameters is deregistered or disabled, no new instances can be launched from the AMI. For fleets that are set to maintain target capacity, the target capacity will not be maintained. ii.
(Optional) For Key pair name, choose an existing key pair or create a new one.
[Existing key pair] Choose the key pair.
[New key pair] Choose Create new key pair to go the Key pairs page. When you are done, return to the Spot Requests page and refresh the list. iii.
(Optional) Expand Additional launch parameters, and do the following:
A.
(Optional) To enable Amazon EBS optimization, for EBS-optimized, select Launch EBS-optimized instances.
B.
(Optional) To add temporary block-level storage for your instances, for Instance store, choose Attach at launch.
C.
(Optional) To add storage, choose Add new volume, and specify additional instance store volumes or Amazon EBS volumes, depending on the instance type.
D.
(Optional) By default, basic monitoring is enabled for your instances. To enable detailed monitoring, for Monitoring, select Enable CloudWatch detailed monitoring.
E.
(Optional) To run a Dedicated Spot Instance, for Tenancy, choose Dedicated - run a dedicated instance.
F.
(Optional) For Security groups, choose one or more security groups or create a new one.
[Existing security group] Choose one or more security groups.
[New security group] Choose Create new security group to go the Security Groups page. When you are done, return to the Spot Requests and refresh the list.
G.
(Optional) To make your instances reachable from the internet, for Auto- assign IPv4 Public IP, choose Enable.

H.
(Optional) To launch your Spot Instances with an IAM role, for IAM instance profile, choose the role.
I.
(Optional) To run a start-up script, copy it to User data.
J.
(Optional) To add a tag, choose Create tag and enter the key and value for the tag, and choose Create. Repeat for each tag.
For each tag, to tag the instances and the Spot Fleet request with the same tag, ensure that both Instances and Fleet are selected. To tag only the instances launched by the fleet, clear Fleet. To tag only the Spot Fleet request, clear Instances. b.
[Launch template] To use a configuration you created in a launch template, choose Use a launch template, and for Launch template, choose a launch template.
Note If you want On-Demand capacity in your Spot Fleet, you must specify a launch template.
5. For Additional request details, do the following: a.
Review the additional request details. To make changes, clear Apply defaults. b.
(Optional) For IAM fleet role, you can use the default role or choose a different role. To use the default role after changing the role, choose Use default role. c.
(Optional) To create a request that is valid only during a specific time period, edit Request valid from and Request valid until. d.
(Optional) By default, Amazon EC2 terminates your Spot Instances when the Spot Fleet request expires. To keep them running after your request expires, clear Terminate the instances when the request expires. e.
(Optional) To register your Spot Instances with a load balancer, choose Receive traffic from one or more load balancers and choose one or more Classic Load Balancers or target groups.
6. For Target capacity, do the following: a.
For Total target capacity, specify the number of units to request. For the type of unit, you can choose Instances, vCPUs, or Memory (MiB). To specify a target capacity of 0 so that you can add capacity later, you must first select Maintain target capacity.

b.
(Optional) For Include On-Demand base capacity, specify the number of On-Demand units to request. The number must be less than the Total target capacity. Amazon EC2 calculates the difference, and allocates the difference to Spot units to request.
Important To specify optional On-Demand capacity, you must first choose a launch template. c.
(Optional) By default, Amazon EC2 terminates Spot Instances when they are interrupted. To maintain the target capacity, select Maintain target capacity. You can then specify that Amazon EC2 terminates, stops, or hibernates Spot Instances when they are interrupted. To do so, choose the corresponding option from Interruption behavior.
Note If an AMI specified in the launch parameters is deregistered or disabled, no new instances can be launched from the AMI. In this case, for fleets that are set to maintain target capacity, the target capacity will not be maintained. d.
(Optional) To allow Spot Fleet to launch a replacement Spot Instance when an instance rebalance notification is emitted for an existing Spot Instance in the fleet, select Capacity rebalance, and then choose an instance replacement strategy. If you choose Launch before terminate, specify the delay (in seconds) before Amazon EC2 terminates the old instances. For more information, see Use Capacity Rebalancing in EC2 Fleet and Spot Fleet to replace at-risk Spot Instances. e.
(Optional) To control the amount you pay per hour for all the Spot Instances in your fleet, select Set maximum cost for Spot Instances and then enter the maximum total amount you're willing to pay per hour. When the maximum total amount is reached, Spot Fleet stops launching Spot Instances even if it hasn't met the target capacity. For more information, see Set a spending limit for your EC2 Fleet or Spot Fleet.
7. For Network, do the following: a.
For Network, choose an existing VPC or create a new one.
[Existing VPC] Choose the VPC.

[New VPC] Choose Create new VPC to go the Amazon VPC console. When you're done, return to this screen and refresh the list. b.
(Optional) For Availability Zone, let Amazon EC2 choose the Availability Zones for your Spot Instances, or specify one or more Availability Zones.
If you have more than one subnet in an Availability Zone, choose the appropriate subnet from Subnet. To add subnets, choose Create new subnet to go to the Amazon VPC console. When you are done, return to this screen and refresh the list.
8. For Instance type requirements, you can either specify instance attributes and let Amazon EC2 identify the optimal instance types with these attributes, or you can specify a list of instances. For more information, see Specify attributes for instance type selection for EC2 Fleet or Spot Fleet. a.
If you choose Specify instance attributes that match your compute requirements, specify your instance attributes as follows: i.
For vCPUs, enter the desired minimum and maximum number of vCPUs. To specify no limit, select No minimum or No maximum, or both. ii.
For Memory (GiB), enter the desired minimum and maximum amount of memory.
To specify no limit, select No minimum or No maximum, or both. iii.
(Optional) For Additional instance attribute, you can optionally specify one or more attributes to express your compute requirements in more detail. Each additional attribute adds a further constraint to your request. You can omit the additional attributes; when omitted, the default values are used. For a description of each attribute and their default values, see get-spot-placement-scores. iv.
(Optional) To view the instance types with your specified attributes, expand Preview matching instance types. To exclude instance types from being used in your request, select the instances and then choose Exclude selected instance types. b.
If you choose Manually select instance types, Spot Fleet provides a default list of instance types. To select more instance types, choose Add instance types, select the instance types to use in your request, and choose Select. To delete instance types, select the instance types and choose Delete.

9. For Allocation strategy, choose a Spot allocation strategy and an On-Demand allocation strategy that meets your needs. For more information, see Use allocation strategies to determine how EC2 Fleet or Spot Fleet fulfills Spot and On-Demand capacity.
10. For Your fleet request at a glance, review your fleet configuration, and make any adjustments if necessary.
11. (Optional) To download a copy of the launch configuration for use with the AWS CLI, choose JSON config.
12. When you're ready to launch your Spot Fleet, choose Launch.
The Spot Fleet request type is fleet. When the request is fulfilled, requests of type instance are added, where the state is active and the status is fulfilled.
AWS CLI To create a Spot Fleet request Use the request-spot-fleet command. aws ec2 request-spot-fleet --spot-fleet-request-config file://config.json For example configuration files, see Example CLI configurations Spot Fleet.
PowerShell To create a Spot Fleet request Use the Request-EC2SpotFleet cmdlet. The following example launches Spot Instances in a capacity-optimized fleet.
Request-EC2SpotFleet `
    -SpotFleetRequestConfig_TargetCapacity 50 `
    -SpotFleetRequestConfig_AllocationStrategy "CapacityOptimized" `
    -SpotFleetRequestConfig_IamFleetRole "arn:aws:iam::123456789012:role/my-spot- fleet-role" `
    -SpotFleetRequestConfig_LaunchTemplateConfig @($launchConfig)
Define the launch configuration as follows, setting the launch template and override properties that you need. For example configurations, see Example CLI configurations Spot Fleet.
$lcSpec = Amazon.EC2.Model.FleetLaunchTemplateSpecification

# To do - Set FleetLaunchTemplateSpecification properties $lcOverrides = New-Object Amazon.EC2.Model.LaunchTemplateOverrides
# To do - Set LaunchTemplateOverrides properties $launchConfig = New-Object Amazon.EC2.Model.LaunchTemplateConfig $launchConfig.LaunchTemplateSpecification $lcSpec $launchConfig.Overrides @($lcOverrides)
### Create a Spot Fleet that replaces unhealthy Spot Instances Spot Fleet checks the health status of the Spot Instances in the fleet every two minutes. The health status of an instance is either healthy or unhealthy.
Spot Fleet determines the health status of an instance by using the status checks provided by Amazon EC2. An instance is determined as unhealthy when the status of either the instance status check or the system status check is impaired for three consecutive health checks. For more information, see Status checks for Amazon EC2 instances.
You can configure your fleet to replace unhealthy Spot Instances. After enabling health check replacement, a Spot Instance is replaced when it is reported as unhealthy. The fleet could go below its target capacity for up to a few minutes while an unhealthy Spot Instance is being replaced.
Requirements
- Health check replacement is supported only for Spot Fleets that maintain a target capacity (fleets of type maintain), not for one-time Spot Fleets (fleets of type request).
- Health check replacement is supported only for Spot Instances. This feature is not supported for On-Demand Instances.
- You can configure your Spot Fleet to replace unhealthy instances only when you create it.
- Users can use health check replacement only if they have permission to call the ec2:DescribeInstanceStatus action.
Console To configure a Spot Fleet to replace unhealthy Spot Instances
1. Follow the steps for creating a Spot Fleet in Create a Spot Fleet request using defined parameters.

2. To configure the fleet to replace unhealthy Spot Instances, expand Additional launch parameters, and under Health check, select Replace unhealthy instances. To enable this option, you must first choose Maintain target capacity.
AWS CLI To configure a Spot Fleet to replace unhealthy Spot Instances Use the request-spot-fleet command with the ReplaceUnhealthyInstances property of SpotFleetRequestConfig.
{ "SpotFleetRequestConfig": { "AllocationStrategy": "lowestPrice", "IamFleetRole": "arn:aws:iam::123456789012:role/aws-ec2-spot-fleet-tagging- role", "TargetCapacity": 10, "ReplaceUnhealthyInstances": true } } PowerShell To configure a Spot Fleet request to replace unhealthy Spot Instances Use the Request-EC2SpotFleet cmdlet with the - SpotFleetRequestConfig_ReplaceUnhealthyInstance parameter.
-SpotFleetRequestConfig_ReplaceUnhealthyInstance $true
## Tag a new or existing Spot Fleet request and the instances and volumes it launches it launches To help categorize and manage your Spot Fleet requests and the instances and volumes that it launches, you can tag them with custom metadata. You can assign a tag to a Spot Fleet request when you create it, or afterward. Similarly, you can assign a tag to the instances and volumes when they're launched by the fleet, or afterward.

When you tag a fleet request, the instances and volumes that are launched by the fleet are not automatically tagged. You need to explicitly tag the instances and volumes launched by the fleet.
You can choose to assign tags to only the fleet request, or to only the instances launched by the fleet, or to only the volumes attached to the instances launched by the fleet, or to all of them.
Note You can only tag volumes that are attached to On-Demand Instances. You can't tag volumes that are attached to Spot Instances.
You can assign tags using the Amazon EC2 console or a command line tool.
For more information about how tags work, see Tag your Amazon EC2 resources.
Contents
- Prerequisite
- Tag a new Spot Fleet and the instances and volumes that it launches
- Tag an existing Spot Fleet
- View Spot Fleet request tags
### Prerequisite Grant the user the permission to tag resources. For more information, see Example: Tag resources.
To grant a user the permission to tag resources Create an IAM policy that includes the following:
- The ec2:CreateTags action. This grants the user permission to create tags.
- The ec2:RequestSpotFleet action. This grants the user permission to create a Spot Fleet request.
- For Resource, you must specify "*". This allows users to tag all resource types.
JSON {

    "Version":"2012-10-17", "Statement": [ { "Sid": "TagSpotFleetRequest", "Effect": "Allow", "Action": [ "ec2:CreateTags", "ec2:RequestSpotFleet"
            ], "Resource": "*"
        } ]
} Important We currently do not support resource-level permissions for the spot-fleet-request resource. If you specify spot-fleet-request as a resource, you will get an unauthorized exception when you try to tag the fleet. The following example illustrates how not to set the policy.
{ "Effect": "Allow", "Action": [ "ec2:CreateTags", "ec2:RequestSpotFleet"
    ], "Resource": "arn:aws:ec2:us-east-1:111122223333:spot-fleet-request/*"
} To provide access, add permissions to your users, groups, or roles:
- Users and groups in AWS IAM Identity Center:
Create a permission set. Follow the instructions in Create a permission set in the AWS IAM Identity Center User Guide.
- Users managed in IAM through an identity provider:

Create a role for identity federation. Follow the instructions in Create a role for a third-party identity provider (federation) in the IAM User Guide.
- IAM users:
- Create a role that your user can assume. Follow the instructions in Create a role for an IAM user in the IAM User Guide.
- (Not recommended) Attach a policy directly to a user or add a user to a user group. Follow the instructions in Adding permissions to a user (console) in the IAM User Guide.
### Tag a new Spot Fleet and the instances and volumes that it launches To tag a new Spot Fleet request and the instances and volumes that it launches using the console
1. Follow the Create a Spot Fleet request using defined parameters procedure.
2. The way you add a tag depends on whether you manually configured the fleet or used a launch template.
- If you manually configured the fleet, do the following:
To add a tag, expand Additional launch parameters, choose Create tag, and enter the key and value for the tag. Repeat for each tag.
For each tag, you can tag the Spot Fleet request and the instances with the same tag. To tag both, ensure that both Instances and Fleet are selected. To tag only the Spot Fleet request, clear Instances. To tag only the instances launched by the fleet, clear Fleet.
Note When you manually configure a fleet, there is no option to tag volumes. Volume tags are only supported for volumes that are attached to On-Demand Instances. When you manually configure a fleet, you can't specify On-Demand Instances.
- If you used a launch template, do the following:
To add a tag to the fleet request, under Tags, choose Create Tag, and enter the key and value for the tag. Repeat for each tag.

To tag the resources in your fleet, you must specify tags in the launch template.
To tag a new Spot Fleet request and the instances and volumes that it launches using the AWS CLI To tag a Spot Fleet request when you create it, and to tag the instances and volumes when they are launched by the fleet, configure the Spot Fleet request configuration as follows:
Spot Fleet request tags:
- Specify the tags for the Spot Fleet request in SpotFleetRequestConfig.
- For ResourceType, specify spot-fleet-request. If you specify another value, the fleet request will fail.
- For Tags, specify the key-value pair. You can specify more than one key-value pair.
Instance tags:
- Specify the tags for the instances in LaunchSpecifications.
- For ResourceType, specify instance. If you specify another value, the fleet request will fail.
- For Tags, specify the key-value pair. You can specify more than one key-value pair.
Alternatively, you can specify the tags for the instance in the launch template that is referenced in the Spot Fleet request.
Volume tags:
- Specify the tags for the volumes in the launch template that is referenced in the Spot Fleet request. Volume tagging in LaunchSpecifications is not supported.
In the following example, the Spot Fleet request is tagged with two tags: Key=Environment and Value=Production, and Key=Cost-Center and Value=123. The instances that are launched by the fleet are tagged with one tag (which is the same as one of the tags for the Spot Fleet request):
Key=Cost-Center and Value=123.
{ "SpotFleetRequestConfig": {

        "AllocationStrategy": "priceCapacityOptimized", "ExcessCapacityTerminationPolicy": "default", "IamFleetRole": "arn:aws:iam::111122223333:role/aws-ec2-spot-fleet-tagging- role", "LaunchSpecifications": [ { "ImageId": "ami-0123456789EXAMPLE", "InstanceType": "c4.large", "TagSpecifications": [ { "ResourceType": "instance", "Tags": [ { "Key": "Cost-Center", "Value": "123"
                            } ]
                    } ]
            } ], "SpotPrice": "5", "TargetCapacity": 2, "TerminateInstancesWithExpiration": true, "Type": "maintain", "ReplaceUnhealthyInstances": true, "InstanceInterruptionBehavior": "terminate", "InstancePoolsToUseCount": 1, "TagSpecifications": [ { "ResourceType": "spot-fleet-request", "Tags": [ { "Key": "Environment", "Value":"Production"
                    }, { "Key": "Cost-Center", "Value":"123"
                    } ]
            } ]
    }

} To tag instances launched by a Spot Fleet using the AWS CLI To tag instances when they are launched by the fleet, you can either specify the tags in the launch template that is referenced in the Spot Fleet request, or you can specify the tags in the Spot Fleet request configuration as follows:
- Specify the tags for the instances in LaunchSpecifications.
- For ResourceType, specify instance. If you specify another value, the fleet request will fail.
- For Tags, specify the key-value pair. You can specify more than one key-value pair.
In the following example, the instances that are launched by the fleet are tagged with one tag:
Key=Cost-Center and Value=123.
{ "SpotFleetRequestConfig": { "AllocationStrategy": "priceCapacityOptimized", "ExcessCapacityTerminationPolicy": "default", "IamFleetRole": "arn:aws:iam::111122223333:role/aws-ec2-spot-fleet-tagging- role", "LaunchSpecifications": [ { "ImageId": "ami-0123456789EXAMPLE", "InstanceType": "c4.large", "TagSpecifications": [ { "ResourceType": "instance", "Tags": [ { "Key": "Cost-Center", "Value": "123"
                            } ]
                    } ]
            } ], "SpotPrice": "5", "TargetCapacity": 2, "TerminateInstancesWithExpiration": true,

        "Type": "maintain", "ReplaceUnhealthyInstances": true, "InstanceInterruptionBehavior": "terminate", "InstancePoolsToUseCount": 1 } } To tag volumes attached to On-Demand Instances launched by a Spot Fleet using the AWS CLI To tag volumes when they are created by the fleet, you must specify the tags in the launch template that is referenced in the Spot Fleet request.
Note Volume tags are only supported for volumes that are attached to On-Demand Instances.
You can't tag volumes that are attached to Spot Instances.
Volume tagging in LaunchSpecifications is not supported.
### Tag an existing Spot Fleet To tag an existing Spot Fleet request using the console After you create a Spot Fleet request, you can add tags to the fleet request using the console.
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Spot Requests.
3. Select your Spot Fleet request.
4. Choose the Tags tab and choose Create Tag.
To tag an existing Spot Fleet request using the AWS CLI You can use the create-tags command to tag existing resources. In the following example, the existing Spot Fleet request is tagged with Key=purpose and Value=test. aws ec2 create-tags \ --resources sfr-11112222-3333-4444-5555-66666EXAMPLE \ --tags Key=purpose,Value=test

### View Spot Fleet request tags To view Spot Fleet request tags using the console
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Spot Requests.
3. Select your Spot Fleet request and choose the Tags tab.
To describe Spot Fleet request tags Use the describe-tags command to view the tags for the specified resource. In the following example, you describe the tags for the specified Spot Fleet request. aws ec2 describe-tags \ --filters "Name=resource-id,Values=sfr-11112222-3333-4444-5555-66666EXAMPLE"
{ "Tags": [ { "Key": "Environment", "ResourceId": "sfr-11112222-3333-4444-5555-66666EXAMPLE", "ResourceType": "spot-fleet-request", "Value": "Production"
        }, { "Key": "Another key", "ResourceId": "sfr-11112222-3333-4444-5555-66666EXAMPLE", "ResourceType": "spot-fleet-request", "Value": "Another value"
        } ]
} You can also view the tags of a Spot Fleet request by describing the Spot Fleet request.
Use the describe-spot-fleet-requests command to view the configuration of the specified Spot Fleet request, which includes any tags that were specified for the fleet request. aws ec2 describe-spot-fleet-requests \

    --spot-fleet-request-ids sfr-11112222-3333-4444-5555-66666EXAMPLE { "SpotFleetRequestConfigs": [ { "ActivityStatus": "fulfilled", "CreateTime": "2020-02-13T02:49:19.709Z", "SpotFleetRequestConfig": { "AllocationStrategy": "capacityOptimized", "OnDemandAllocationStrategy": "lowestPrice", "ExcessCapacityTerminationPolicy": "Default", "FulfilledCapacity": 2.0, "OnDemandFulfilledCapacity": 0.0, "IamFleetRole": "arn:aws:iam::111122223333:role/aws-ec2-spot-fleet- tagging-role", "LaunchSpecifications": [ { "ImageId": "ami-0123456789EXAMPLE", "InstanceType": "c4.large"
                    } ], "TargetCapacity": 2, "OnDemandTargetCapacity": 0, "Type": "maintain", "ReplaceUnhealthyInstances": false, "InstanceInterruptionBehavior": "terminate"
            }, "SpotFleetRequestId": "sfr-11112222-3333-4444-5555-66666EXAMPLE", "SpotFleetRequestState": "active", "Tags": [ { "Key": "Environment", "Value": "Production"
                }, { "Key": "Another key", "Value": "Another value"
                } ]
        } ]
}

## Describe a Spot Fleet request, its instances, and event history You can describe your Spot Fleet configuration, the instances in your Spot Fleet, and the event history of your Spot Fleet.
Console To describe your Spot Fleet
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Spot Requests.
3. Select your Spot Fleet request. The ID begins with sfr-. To see the configuration details, choose Description.
4. To list the Spot Instances for the Spot Fleet, choose Instances.
5. To view the history for the Spot Fleet, choose History.
AWS CLI To describe your Spot Fleet request Use the describe-spot-fleet-requests command. aws ec2 describe-spot-fleet-requests \ --spot-fleet-request-ids sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE To describe the running instances for the specified Spot Fleet request Use the describe-spot-fleet-instances command. aws ec2 describe-spot-fleet-instances \ --spot-fleet-request-id sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE To describe the event history for the specified Spot Fleet request Use the describe-spot-fleet-request-history command. aws ec2 describe-spot-fleet-request-history \ --spot-fleet-request-id sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE \ --start-time 2024-05-18T00:00:00Z

PowerShell To describe your Spot Fleet request Use the Get-EC2SpotFleetRequest cmdlet.
Get-EC2SpotFleetRequest To describe the running instances for the specified Spot Fleet request Use the Get-EC2SpotFleetInstance cmdlet.
Get-EC2SpotFleetInstance `
    -SpotFleetRequestId "sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE"
To describe the event history for the specified Spot Fleet request Use the Get-EC2SpotFleetRequestHistory cmdlet.
Get-EC2SpotFleetRequestHistory `
    -SpotFleetRequestId "sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE" `
    -UtcStartTime 2024-05-18T00:00:00Z
## Modify a Spot Fleet request You can modify an active Spot Fleet request to complete the following tasks:
- Increase the total target capacity and On-Demand portion
- Decrease the total target capacity and On-Demand portion When you increase the total target capacity, the Spot Fleet launches additional Spot Instances according to the allocation strategy for its Spot Fleet request. When you increase the On-Demand portion, the Spot Fleet launches additional On-Demand Instances.
When you decrease the total target capacity, the Spot Fleet cancels any open requests that exceed the new target capacity. You can request that the Spot Fleet terminate Spot Instances until the size of the fleet reaches the new target capacity. If the allocation strategy is diversified, the Spot Fleet terminates instances across the pools. Alternatively, you can request that the Spot Fleet

keep the fleet at its current size, but not replace any Spot Instances that are interrupted or that you terminate manually.
### Considerations
- You can't modify a one-time Spot Fleet request. You can only modify a Spot Fleet request if you selected Maintain target capacity when you created the Spot Fleet request.
- When a Spot Fleet terminates an instance because the target capacity was decreased, the instance receives a Spot Instance interruption notice.
Console To modify a Spot Fleet request
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Spot Requests.
3. Select your Spot Fleet request.
4. Choose Actions, Modify target capacity.
5. In Modify target capacity, do the following: a.
Enter the new target capacity and On-Demand portion. b.
(Optional) If you are decreasing the target capacity but want to keep the fleet at its current size, clear Terminate instances. c.
Choose Submit.
AWS CLI To modify a Spot Fleet request Use the modify-spot-fleet-request command to update the target capacity of the specified Spot Fleet request. aws ec2 modify-spot-fleet-request \ --spot-fleet-request-id sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE \ --target-capacity 20 You can modify the previous command as follows to decrease the target capacity of the specified Spot Fleet without terminating any Spot Instances as a result.

aws ec2 modify-spot-fleet-request \ --spot-fleet-request-id sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE \ --target-capacity 10 \ --excess-capacity-termination-policy NoTermination PowerShell To modify a Spot Fleet request Use the Edit-EC2SpotFleetRequest cmdlet to update the target capacity of the specified Spot Fleet request.
Edit-EC2SpotFleetRequest `
    -SpotFleetRequestId "sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE" `
    -TargetCapacity 20 You can modify the previous command as follows to decrease the target capacity of the specified Spot Fleet without terminating any Spot Instances as a result.
Edit-EC2SpotFleetRequest `
    -SpotFleetRequestId "sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE" `
    -TargetCapacity 20 `
    -ExcessCapacityTerminationPolicy "NoTermination"
## Cancel (delete) a Spot Fleet request If you no longer require a Spot Fleet, you can cancel the Spot Fleet request, which deletes the request. After you cancel a fleet request, all Spot requests associated with the fleet are also canceled, so that no new Spot Instances are launched.
When you cancel a Spot Fleet request, you must also specify if you want to terminate all of its instances. These include both On-Demand Instances and Spot Instances.
Warning Terminating an instance is permanent and irreversible.
After you terminate an instance, you can no longer connect to it, and it can't be recovered.
All attached Amazon EBS volumes that are configured to be deleted on termination are

also permanently deleted and can't be recovered. All data stored on instance store volumes is permanently lost. For more information, see How instance termination works.
Before you terminate an instance, ensure that you have backed up all data that you need to retain after the termination to persistent storage.
If you specify that the instances must be terminated when the fleet request is canceled, the fleet request enters the cancelled_terminating state. Otherwise, it enters the cancelled_running state, and the instances continue to run until they are interrupted or you terminate them manually.
Restrictions
- You can cancel up to 100 fleets in a single request. If you exceed the specified number, no fleets are canceled.
Console To cancel (delete) a Spot Fleet request
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Spot Requests.
3. Select your Spot Fleet request.
4. Choose Actions, Cancel request.
5. In the Cancel Spot request dialog box, do the following: a.
To terminate the associated instances at the same time as canceling the Spot Fleet request, leave the Terminate instances checkbox selected. To cancel the Spot Fleet request without terminating the associated instances, clear the Terminate instances checkbox. b.
Choose Confirm.
AWS CLI To cancel (delete) a Spot Fleet request and terminate its instances Use the cancel-spot-fleet-requests command with the --terminate-instances option.

aws ec2 cancel-spot-fleet-requests \ --spot-fleet-request-ids sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE \ --terminate-instances The following is example output.
{ "SuccessfulFleetRequests": [ { "SpotFleetRequestId": "sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE", "CurrentSpotFleetRequestState": "cancelled_terminating", "PreviousSpotFleetRequestState": "active"
        } ], "UnsuccessfulFleetRequests": []
} To cancel (delete) a Spot Fleet request without terminating its instances Modify the previous example by using the --no-terminate-instances option instead. aws ec2 cancel-spot-fleet-requests \ --spot-fleet-request-ids sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE \ --no-terminate-instances The following is example output.
{ "SuccessfulFleetRequests": [ { "SpotFleetRequestId": "sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE", "CurrentSpotFleetRequestState": "cancelled_running", "PreviousSpotFleetRequestState": "active"
        } ], "UnsuccessfulFleetRequests": []
} PowerShell To cancel (delete) a Spot Fleet request and terminate its instances

Use the Stop-EC2SpotFleetRequest cmdlet with the -TerminateInstance parameter.
Stop-EC2SpotFleetRequest `
    -SpotFleetRequestId "sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE" `
    -TerminateInstance $true To cancel (delete) a Spot Fleet request without terminating its instances Modify the previous example by changing the value of the -TerminateInstance parameter.
Stop-EC2SpotFleetRequest `
    -SpotFleetRequestId "sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE" `
    -TerminateInstance $false
## Understand automatic scaling for Spot Fleet Automatic scaling enables your Spot Fleet to increase or decrease its target capacity based on demand. With automatic scaling, a Spot Fleet can either launch instances (scale out) or terminate instances (scale in) within a specified range, in response to one or more scaling policies.
Automatic scaling for Spot Fleet is made possible by a combination of the Amazon EC2, Amazon CloudWatch, and Application Auto Scaling APIs. Spot Fleet requests are created with Amazon EC2, alarms are created with CloudWatch, and scaling policies are created with Application Auto Scaling.
Types of automatic scaling Spot Fleet supports the following types of automatic scaling:
- Target tracking scaling – Increase or decrease the current capacity of the fleet by targeting a value for a specific metric. This is similar to the way that your thermostat maintains the temperature of your home—you select the desired temperature and the thermostat does the rest.
- Step scaling – Increase or decrease the current capacity of the fleet based on a set of scaling adjustments, known as step adjustments, that vary based on the size of the alarm breach.
- Scheduled scaling – Increase or decrease the current capacity of the fleet based on the date and time.

Considerations When using automatic scaling for your Spot Fleet, consider the following:
- Instance weighting – If you're using instance weighting, keep in mind that Spot Fleet can exceed the target capacity as needed. Fulfilled capacity can be a floating-point number but target capacity must be an integer, so Spot Fleet rounds up to the next integer. You must take these behaviors into account when you look at the outcome of a scaling policy when an alarm is triggered. For example, suppose that the target capacity is 30, the fulfilled capacity is 30.1, and the scaling policy subtracts 1. When the alarm is triggered, the automatic scaling process subtracts 1 from 30.1 to get 29.1 and then rounds it up to 30, so no scaling action is taken.
As another example, suppose that you selected instance weights of 2, 4, and 8, and a target capacity of 10, but no weight 2 instances were available so Spot Fleet provisioned instances of weights 4 and 8 for a fulfilled capacity of 12. If the scaling policy decreases target capacity by 20% and an alarm is triggered, the automatic scaling process subtracts 12*0.2 from 12 to get 9.6 and then rounds it up to 10, so no scaling action is taken.
- Cooldown period – The scaling policies that you create for Spot Fleet support a cooldown period. This is the number of seconds after a scaling activity completes where previous trigger- related scaling activities can influence future scaling events. For scale-out policies, while the cooldown period is in effect, the capacity that has been added by the previous scale-out event that initiated the cooldown is calculated as part of the desired capacity for the next scale out.
The intention is to continuously (but not excessively) scale out. For scale in policies, the cooldown period is used to block subsequent scale in requests until it has expired. The intention is to scale in conservatively to protect your application's availability. However, if another alarm triggers a scale-out policy during the cooldown period after a scale-in, automatic scaling scales out your scalable target immediately.
- Use detailed monitoring – We recommend that you scale based on instance metrics with a 1-minute frequency because that ensures a faster response to utilization changes. Scaling on metrics with a 5-minute frequency can result in slower response time and scaling on stale metric data. To send metric data for your instances to CloudWatch in 1-minute periods, you must specifically enable detailed monitoring. For more information, see Manage detailed monitoring for your EC2 instances and Create a Spot Fleet request using defined parameters.
- AWS CLI – If you use the AWS CLI for configuring scaling for Spot Fleet, you'll use the application-autoscaling commands.

### IAM permissions required for Spot Fleet automatic scaling Automatic scaling for Spot Fleet is made possible by a combination of the Amazon EC2, Amazon CloudWatch, and Application Auto Scaling APIs. Spot Fleet requests are created with Amazon EC2, alarms are created with CloudWatch, and scaling policies are created with Application Auto Scaling.
In addition to the IAM permissions required for using Spot Fleet and Amazon EC2, the user that accesses the fleet scaling settings must have the appropriate permissions for the services that support automatic scaling.
To use automatic scaling for Spot Fleet, users must have permissions to use the actions shown in the following example policy.
JSON { "Version":"2012-10-17", "Statement": [ { "Effect": "Allow", "Action": [ "application-autoscaling:*", "ec2:DescribeSpotFleetRequests", "ec2:ModifySpotFleetRequest", "cloudwatch:DeleteAlarms", "cloudwatch:DescribeAlarmHistory", "cloudwatch:DescribeAlarms", "cloudwatch:DescribeAlarmsForMetric", "cloudwatch:GetMetricStatistics", "cloudwatch:ListMetrics", "cloudwatch:PutMetricAlarm", "cloudwatch:DisableAlarmActions", "cloudwatch:EnableAlarmActions", "iam:CreateServiceLinkedRole", "sns:CreateTopic", "sns:Subscribe", "sns:Get*", "sns:List*"
            ], "Resource": "*"
        } ]

} You can also create your own IAM policies that allow more fine-grained permissions for calls to the Application Auto Scaling API. For more information, see Identity and Access Management for Application Auto Scaling in the Application Auto Scaling User Guide.
The Application Auto Scaling service also needs permission to describe your Spot Fleet and CloudWatch alarms, and permissions to modify your Spot Fleet target capacity on your behalf.
If you enable automatic scaling for your Spot Fleet, it creates a service-linked role named AWSServiceRoleForApplicationAutoScaling_EC2SpotFleetRequest. This service-linked role grants Application Auto Scaling permission to describe the alarms for your policies, to monitor the current capacity of the fleet, and to modify the capacity of the fleet. The original managed Spot Fleet role for Application Auto Scaling was aws-ec2-spot-fleet-autoscale-role, but it is no longer required. The service-linked role is the default role for Application Auto Scaling. For more information, see Service-linked roles for Application Auto Scaling in the Application Auto Scaling User Guide.
### Target tracking scaling: Scale Spot Fleet by targeting a value for a specific metric With target tracking scaling, you create a target tracking scaling policy by selecting a metric and setting a target value. Spot Fleet then creates and manages the CloudWatch alarms that trigger the scaling policy, and calculates the scaling adjustment based on the chosen metric and target value. The scaling policy adjusts capacity by adding or removing instances as needed to keep the metric at, or close to, the specified target value. A target tracking policy not only keeps the metric close to the target value, but also adjusts to the fluctuations in the metric due to a fluctuating load pattern and minimizes rapid capacity fluctuations.
You can create multiple target tracking scaling policies for a Spot Fleet, provided each policy uses a different metric. The fleet scales based on the policy that specifies the largest fleet capacity. This allows you to cover multiple scenarios to ensure sufficient capacity for your application workloads.
To ensure application availability, the fleet scales out proportionally to the metric as fast as it can, but scales in more gradually.
When a Spot Fleet terminates a Spot Instance because the target capacity was decreased, the instance receives a Spot Instance interruption notice.

Note Do not edit or delete the CloudWatch alarms that Spot Fleet manages for a target tracking scaling policy. Spot Fleet deletes the alarms automatically when you delete the target tracking scaling policy.
Prerequisites
- The Spot Fleet request must have a request type of maintain. Automatic scaling is not supported for requests of type request.
- Configure the IAM permissions required for Spot Fleet automatic scaling.
- Review the Considerations.
To configure a target tracking policy
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Spot Requests.
3. Select your Spot Fleet request.
4. Choose the Auto Scaling tab near the bottom of the screen. If you selected the link for your Spot Fleet, there is no tab; instead, scroll down to the Auto Scaling section.
5. If automatic scaling is not configured, choose Configure.
6. Use Scale capacity between to set the minimum and maximum capacity for your fleet.
Automatic scaling does not scale your fleet below the minimum capacity or above the maximum capacity.
7. For Policy name, enter a name for the policy.
8. Choose a Target metric.
9. Enter a Target value for the metric.
10. For Cooldown period, specify a new value (in seconds) or keep the default.
11. (Optional) To omit creating a scale-in policy based on the current configuration, select Disable scale-in. You can create a scale-in policy using a different configuration.
12. Choose Save.

To configure a target tracking policy using the AWS CLI
1. Register the Spot Fleet request as a scalable target using the register-scalable-target command.
2. Create a scaling policy using the put-scaling-policy command.
### Step scaling: Scale Spot Fleet using step scaling policies With step scaling policies, you specify CloudWatch alarms to trigger the scaling process. For example, if you want to scale out when CPU utilization reaches a certain level, create an alarm using the CPUUtilization metric provided by Amazon EC2.
When you create a step scaling policy, you must specify one of the following scaling adjustment types:
- Add – Increase the target capacity of the fleet by a specified number of capacity units or a specified percentage of the current capacity.
- Remove – Decrease the target capacity of the fleet by a specified number of capacity units or a specified percentage of the current capacity.
- Set to – Set the target capacity of the fleet to the specified number of capacity units.
When an alarm is triggered, the automatic scaling process calculates the new target capacity using the fulfilled capacity and the scaling policy, and then updates the target capacity accordingly. For example, suppose that the target capacity and fulfilled capacity are 10 and the scaling policy adds
1. When the alarm is triggered, the automatic scaling process adds 1 to 10 to get 11, so Spot Fleet launches 1 instance.
When a Spot Fleet terminates a Spot Instance because the target capacity was decreased, the instance receives a Spot Instance interruption notice.
Prerequisites
- The Spot Fleet request must have a request type of maintain. Automatic scaling is not supported for requests of type request.
- Configure the IAM permissions required for Spot Fleet automatic scaling.
- Consider which CloudWatch metrics are important to your application. You can create CloudWatch alarms based on metrics provided by AWS or your own custom metrics.

- For the AWS metrics that you will use in your scaling policies, enable CloudWatch metrics collection if the service that provides the metrics does not enable it by default.
- Review the Considerations.
To create a CloudWatch alarm
1. Open the CloudWatch console at https://console.aws.amazon.com/cloudwatch/.
2. In the navigation pane, expand Alarms and choose All alarms.
3. Choose Create alarm.
4. On the Specify metric and conditions page, choose Select metric.
5. Choose EC2 Spot, then Fleet Request Metrics, and then select a metric (for example, TargetCapacity), and then choose Select metric.
The Specify metric and conditions page appears, showing a graph and other information about the metric you selected.
6. For Period, choose the evaluation period for the alarm, for example, 1 minute. When evaluating the alarm, each period is aggregated into one data point.
Note A shorter period creates a more sensitive alarm.
7. For Conditions, define the alarm by defining the threshold condition. For example, you can define a threshold to trigger the alarm whenever the value of the metric is greater than or equal to 80 percent.
8. Under Additional configuration, for Datapoints to alarm, specify how many datapoints (evaluation periods) must be in the ALARM state to trigger the alarm, for example, 1 evaluation period or 2 out of 3 evaluation periods. This creates an alarm that goes to ALARM state if that many consecutive periods are breaching. For more information, see Evaluating an alarm in the Amazon CloudWatch User Guide.
9. For Missing data treatment, choose one of the options (or leave the default of Treat missing data as missing). For more information, see Configuring how CloudWatch alarms treat missing data in the Amazon CloudWatch User Guide.
10. Choose Next.

11. (Optional) To receive notification of a scaling event, for Notification, you can choose or create the Amazon SNS topic you want to use to receive notifications. Otherwise, you can delete the notification now and add one later as needed.
12. Choose Next.
13. Under Add name and description, enter a name and description for the alarm and choose Next.
14. Choose Create alarm.
To configure a step scaling policy for your Spot Fleet
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Spot Requests.
3. Select your Spot Fleet request.
4. Choose the Auto Scaling tab near the bottom of the screen. If you selected the link for your Spot Fleet, there is no tab; instead, scroll down to the Auto Scaling section.
5. If automatic scaling is not configured, choose Configure.
6. Use Scale capacity between to set the minimum and maximum capacity for your fleet. Scaling policies do not scale your fleet below the minimum capacity or above the maximum capacity.
7. Under Scaling policies, for Policy type, choose Step scaling policy.
8. Initially, Scaling policies contain step scaling policies named ScaleUp and ScaleDown. You can complete these policies, or choose Remove policy to delete them. You can also choose Add policy.
9. To define a policy, do the following: a.
For Policy name, enter a name for the policy. b.
For Policy trigger, select an existing alarm, or choose Create alarm to open the Amazon CloudWatch console and create an alarm. c.
For Modify capacity, define the amount by which to scale and the lower and upper bound of the step adjustment. You can add or remove a specific number of instances or a percentage of the existing fleet size, or set the fleet to an exact size.
For example, to create a step scaling policy that increases the capacity of the fleet by 30 percent, choose Add, enter 30 in the next field, and then choose percent. By default, the lower bound for an add policy is the alarm threshold and the upper bound is positive (+)

infinity. By default, the upper bound for a remove policy is the alarm threshold and the lower bound is negative (-) infinity. d.
(Optional) To add another step, choose Add step. e.
For Cooldown period, specify a new value (in seconds) or keep the default.
10. Choose Save.
To configure step scaling policies for your Spot Fleet using the AWS CLI
1. Register the Spot Fleet request as a scalable target using the register-scalable-target command.
2. Create a scaling policy using the put-scaling-policy command.
3. Create an alarm that triggers the scaling policy using the put-metric-alarm command.
### Scheduled scaling: Scale Spot Fleet on a schedule Scaling your fleet on a schedule enables you to scale your application in response to predictable changes in demand. By creating scheduled actions, you can instruct Spot Fleet to perform scaling activities at specific times. To create a scheduled action, you must specify an existing Spot Fleet, the time when the scaling activity must occur, and the desired minimum and maximum capacity.
Scheduled actions can be configured to scale once or on a recurring schedule. If you needs change, you can edit or delete scheduled actions.
Prerequisites
- Scheduled actions can only be created for existing Spot Fleets. You can't create a scheduled action when you create a Spot Fleet.
- The Spot Fleet request must have a request type of maintain. Automatic scaling is not supported for requests of type request.
- Configure the IAM permissions required for Spot Fleet automatic scaling.
- Review the Considerations.
To create a one-time scheduled action
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Spot Requests.

3. Select your Spot Fleet request.
4. Choose the Scheduled Scaling tab near the bottom of the screen. If you selected the link for your Spot Fleet, there is no tab; instead, scroll down to the Scheduled Scaling section.
5. Choose Create scheduled action.
6. For Name, specify a name for the scheduled action.
7. Enter a value for Minimum capacity, Maximum capacity, or both.
8. For Recurrence, choose Once.
9. (Optional) Choose a date and time for Start time, End time, or both.
10. Choose Create.
To create a recurring scheduled action
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Spot Requests.
3. Select your Spot Fleet request.
4. Choose the Scheduled Scaling tab near the bottom of the screen. If you selected the link for your Spot Fleet, there is no tab; instead, scroll down to the Scheduled Scaling section.
5. For Name, specify a name for the scheduled action.
6. Enter a value for Minimum capacity, Maximum capacity, or both.
7. For Recurrence, choose one of the predefined schedules (for example, Every day), or choose Custom and enter a cron expression. For more information about the cron expressions supported by scheduled scaling, see Cron expressions in the Amazon EventBridge User Guide.
8. (Optional) Choose a date and time for Start time, End time, or both.
9. Choose Submit.
To edit a scheduled action
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Spot Requests.
3. Select your Spot Fleet request.
4. Choose the Scheduled Scaling tab near the bottom of the screen. If you selected the link for your Spot Fleet, there is no tab; instead, scroll down to the Scheduled Scaling section.
