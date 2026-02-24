# Work with EC2 Fleet

Source: apps/user-manuals/aws/ec2-ug.pdf

---

- For information about configuring Capacity Reservations, see Reserve compute capacity with EC2 On-Demand Capacity Reservations and the On-Demand Capacity Reservation FAQs.
# Work with EC2 Fleet To start using an EC2 Fleet, create a request that includes the total target capacity, On-Demand capacity, Spot capacity, and a launch template specifying the configuration for the instances in the fleet. You can optionally specify additional parameters, or let the fleet use default values. You can also tag the fleet request, and its instances and volumes, when you create the fleet.
The fleet launches On-Demand Instances when there is available capacity, and launches Spot Instances when your maximum price exceeds the Spot price and capacity is available.
Once your fleet is launched, you can describe the fleet request, the instances in the fleet, and any fleet events. You can also assign additional tags as needed.
If you need to change any fleet parameters, such as the total target capacity, you can modify the fleet, provided it was configured to maintain capacity. You can't modify the capacity of a one-time request after it's been submitted.
The fleet request remains active until it expires or you delete it. When you delete the fleet request, you can either terminate the instances or leave them running. If you choose to leave them running, the On-Demand Instances run until you terminate them, and the Spot Instances run until they're interrupted or you terminate them.
Topics
- EC2 Fleet request states
- EC2 Fleet prerequisites
- Create an EC2 Fleet
- Tag a new or existing EC2 Fleet request and the instances and volumes it launches
- Describe an EC2 Fleet, its instances, and its events
- Modify an EC2 Fleet
- Delete an EC2 Fleet request and the instances in the fleet

## EC2 Fleet request states An EC2 Fleet request can be one of various states, with each state indicating a different stage of the request's lifecycle and its management of instances.
An EC2 Fleet request can be in one of the following states: submitted The EC2 Fleet request is being evaluated and Amazon EC2 is preparing to launch the target number of instances. If a request would exceed your fleet limits, it is deleted immediately. active The EC2 Fleet request has been validated and Amazon EC2 is attempting to maintain the target number of running instances. The request remains in this state until it is modified or deleted. modifying The EC2 Fleet request is being modified. The request remains in this state until the modification is fully processed or the request is deleted. Only a maintain fleet type can be modified. This state does not apply to other request types. deleted_running The EC2 Fleet request is deleted and does not launch additional Spot Instances. Its existing instances continue to run until they are interrupted or terminated manually. The request remains in this state until all instances are interrupted or terminated. Only an EC2 Fleet of type maintain or request can have running instances after the EC2 Fleet request is deleted. A deleted instant fleet with running instances is not supported. This state does not apply to instant fleets. deleted_terminating The EC2 Fleet request is deleted and its instances are terminating. The request remains in this state until all instances are terminated. deleted The EC2 Fleet request is deleted and has no running instances. The request is deleted two days after its instances are terminated.

## EC2 Fleet prerequisites To create an EC2 Fleet, the following prerequisites must be in place:
- Launch template
- Service-linked role for EC2 Fleet
- Grant access to customer managed keys for use with encrypted AMIs and EBS snapshots
- Permissions for EC2 Fleet users
### Launch template A launch template specifies the configuration information about the instances to launch, such as the instance type and Availability Zone. For more information about launch templates, see Store instance launch parameters in Amazon EC2 launch templates.
### Service-linked role for EC2 Fleet The AWSServiceRoleForEC2Fleet role grants the EC2 Fleet permission to request, launch, terminate, and tag instances on your behalf. Amazon EC2 uses this service-linked role to complete the following actions:
- ec2:RunInstances – Launch instances.
- ec2:RequestSpotInstances – Request Spot Instances.
- ec2:TerminateInstances – Terminate instances.
- ec2:DescribeImages – Describe Amazon Machine Images (AMIs) for the instances.
- ec2:DescribeInstanceStatus – Describe the status of the instances.
- ec2:DescribeSubnets – Describe the subnets for instances.
- ec2:CreateTags – Add tags to the EC2 Fleet, instances, and volumes.
Ensure that this role exists before you use the AWS CLI or an API to create an EC2 Fleet.
Note An instant EC2 Fleet does not require this role.

To create the role, use the IAM console as follows.
To create the AWSServiceRoleForEC2Fleet role for EC2 Fleet
1. Open the IAM console at https://console.aws.amazon.com/iam/.
2. In the navigation pane, choose Roles.
3. Choose Create role.
4. On the Select trusted entity page, do the following: a.
For Trusted entity type, choose AWS service. b.
Under Use case, for Service or use case, choose EC2 - Fleet.
Tip Be sure to choose EC2 - Fleet. If you choose EC2, the EC2 - Fleet use case does not appear in the Use case list. The EC2 - Fleet use case will automatically create a policy with the required IAM permissions and will suggest AWSServiceRoleForEC2Fleet as the role name. c.
Choose Next.
5. On the Add permissions page, choose Next.
6. On the Name, review, and create page, choose Create role.
If you no longer need to use EC2 Fleet, we recommend that you delete the AWSServiceRoleForEC2Fleet role. After this role is deleted from your account, you can create the role again if you create another fleet.
For more information, see Service-linked roles in the IAM User Guide.
### Grant access to customer managed keys for use with encrypted AMIs and EBS snapshots snapshots If you specify an encrypted AMI or an encrypted Amazon EBS snapshot in your EC2 Fleet and you use an AWS KMS key for encryption, you must grant the AWSServiceRoleForEC2Fleet role permission to use the customer managed key so that Amazon EC2 can launch instances on your behalf. To do this, you must add a grant to the customer managed key, as shown in the following procedure.

When providing permissions, grants are an alternative to key policies. For more information, see Using grants and Using key policies in AWS KMS in the AWS Key Management Service Developer Guide.
To grant the AWSServiceRoleForEC2Fleet role permissions to use the customer managed key
- Use the create-grant command to add a grant to the customer managed key and to specify the principal (the AWSServiceRoleForEC2Fleet service-linked role) that is given permission to perform the operations that the grant permits. The customer managed key is specified by the key-id parameter and the ARN of the customer managed key. The principal is specified by the grantee-principal parameter and the ARN of the AWSServiceRoleForEC2Fleet service- linked role. aws kms create-grant \ --region us-east-1 \ --key-id arn:aws:kms:us- east-1:444455556666:key/1234abcd-12ab-34cd-56ef-1234567890ab \ --grantee-principal arn:aws:iam::111122223333:role/AWSServiceRoleForEC2Fleet \ --operations "Decrypt" "Encrypt" "GenerateDataKey"
 "GenerateDataKeyWithoutPlaintext" "CreateGrant" "DescribeKey" "ReEncryptFrom"
 "ReEncryptTo"
### Permissions for EC2 Fleet users If your users will create or manage an EC2 Fleet, be sure to grant them the required permissions.
To create a policy for EC2 Fleet
1. Open the IAM console at https://console.aws.amazon.com/iam/.
2. In the navigation pane, choose Policies.
3. Choose Create policy.
4. On the Create policy page, choose the JSON tab, replace the text with the following, and choose Review policy.
JSON { "Version":"2012-10-17",

    "Statement": [ { "Effect": "Allow", "Action": [ "ec2:*"
            ], "Resource": "*"
        }, { "Effect": "Allow", "Action": [ "iam:ListRoles", "iam:PassRole", "iam:ListInstanceProfiles"
            ], "Resource":"arn:aws:iam::123456789012:role/DevTeam*"
        } ]
} The ec2:* grants a user permission to call all Amazon EC2 API actions. To limit the user to specific Amazon EC2 API actions, specify those actions instead.
The user must have permission to call the iam:ListRoles action to enumerate existing IAM roles, the iam:PassRole action to specify the EC2 Fleet role, and the iam:ListInstanceProfiles action to enumerate existing instance profiles.
(Optional) To enable a user to create roles or instance profiles using the IAM console, you must also add the following actions to the policy:
- iam:AddRoleToInstanceProfile
- iam:AttachRolePolicy
- iam:CreateInstanceProfile
- iam:CreateRole
- iam:GetRole
- iam:ListPolicies
5. On the Review policy page, enter a policy name and description, and choose Create policy.
6. To provide access, add permissions to your users, groups, or roles:

- Users and groups in AWS IAM Identity Center:
Create a permission set. Follow the instructions in Create a permission set in the AWS IAM Identity Center User Guide.
- Users managed in IAM through an identity provider:
Create a role for identity federation. Follow the instructions in Create a role for a third-party identity provider (federation) in the IAM User Guide.
- IAM users:
- Create a role that your user can assume. Follow the instructions in Create a role for an IAM user in the IAM User Guide.
- (Not recommended) Attach a policy directly to a user or add a user to a user group. Follow the instructions in Adding permissions to a user (console) in the IAM User Guide.
## Create an EC2 Fleet To create an EC2 Fleet, define the fleet configuration in a JSON file and reference the file with the create-fleet command. In the JSON file, you must specify the total target capacity for the fleet, separate target capacities for Spot Instances and On-Demand Instances, and a launch template that defines the configuration for the instances in the fleet, such as an AMI, instance type, subnet or Availability Zone, and one or more security groups. You can optionally specify additional configurations, such as parameters to override the launch template configuration, allocation strategies for selecting Spot Instances and On-Demand Instances from the EC2 capacity pools, and the maximum amount you're willing to pay for the fleet. For more information, see Configuration options for your EC2 Fleet or Spot Fleet.
The EC2 Fleet launches On-Demand Instances when capacity is available, and launches Spot Instances when your maximum price exceeds the Spot price and capacity is available.
If your fleet includes Spot Instances and is of type maintain, Amazon EC2 will attempt to maintain your fleet target capacity when your Spot Instances are interrupted.
### EC2 Fleet limitations The following limitations apply to EC2 Fleet:

- Creating an EC2 Fleet is available only through the Amazon EC2 API, AWS CLI, AWS SDKs, and CloudFormation.
- An EC2 Fleet request can't span AWS Regions. You need to create a separate EC2 Fleet for each Region.
- An EC2 Fleet request can't span different subnets from the same Availability Zone.
### Create an EC2 Fleet To launch a fleet of instances using EC2 Fleet, you need only specify the following parameters in your fleet request, and the fleet will use the default values for the other parameters:
- LaunchTemplateId or LaunchTemplateName – Specifies the launch template to use (which contains the parameters for the instances to launch, such as the instance type and Availability Zone)
- TotalTargetCapacity – Specifies the total target capacity for the fleet
- DefaultTargetCapacityType – Specifies whether the default purchasing option is On- Demand or Spot To override the parameters specified in the launch template, you can specify one or more overrides.
Each override can vary by instance type, Availability Zone, subnet, and maximum price, and can include a different weighted capacity. As an alternative to specifying an instance type, you can specify the attributes that an instance must have, and Amazon EC2 will identify all the instance types with those attributes. For more information, see Specify attributes for instance type selection for EC2 Fleet or Spot Fleet.
For EC2 Fleets of type instant, you can specify a Systems Manager parameter instead of the AMI ID. You can specify the Systems Manager parameter in the override or in the launch template. For more information, see Use a Systems Manager parameter instead of an AMI ID.
You can specify the fleet parameters in a JSON file. For information about all the possible parameters you can specify, see View all the EC2 Fleet configuration options.
For fleet configuration examples, see Example CLI configurations for EC2 Fleet.
There is currently no console support for creating an EC2 Fleet.
To create an EC2 Fleet

Use the create-fleet command to create the fleet and specify the JSON file that contains the fleet configuration parameters. aws ec2 create-fleet --cli-input-json file://file_name.json The following is example output for a fleet of type request or maintain.
{ "FleetId": "fleet-12a34b55-67cd-8ef9-ba9b-9208dEXAMPLE"
} The following is example output for a fleet of type instant that launched the target capacity.
{ "FleetId": "fleet-12a34b55-67cd-8ef9-ba9b-9208dEXAMPLE", "Errors": [], "Instances": [ { "LaunchTemplateAndOverrides": { "LaunchTemplateSpecification": { "LaunchTemplateId": "lt-01234a567b8910abcEXAMPLE", "Version": "1"
        }, "Overrides": { "InstanceType": "c5.large", "AvailabilityZone": "us-east-1a"
        } }, "Lifecycle": "on-demand", "InstanceIds": [ "i-1234567890abcdef0", "i-9876543210abcdef9"
      ], "InstanceType": "c5.large", "Platform": null }, { "LaunchTemplateAndOverrides": { "LaunchTemplateSpecification": { "LaunchTemplateId": "lt-01234a567b8910abcEXAMPLE", "Version": "1"
        },

        "Overrides": { "InstanceType": "c4.large", "AvailabilityZone": "us-east-1a"
        } }, "Lifecycle": "on-demand", "InstanceIds": [ "i-5678901234abcdef0", "i-5432109876abcdef9"
      ]
  ]
} The following is example output for a fleet of type instant that launched part of the target capacity with errors for instances that were not launched.
{ "FleetId": "fleet-12a34b55-67cd-8ef9-ba9b-9208dEXAMPLE", "Errors": [ { "LaunchTemplateAndOverrides": { "LaunchTemplateSpecification": { "LaunchTemplateId": "lt-01234a567b8910abcEXAMPLE", "Version": "1"
        }, "Overrides": { "InstanceType": "c4.xlarge", "AvailabilityZone": "us-east-1a", } }, "Lifecycle": "on-demand", "ErrorCode": "InsufficientInstanceCapacity", "ErrorMessage": ""
    }, ], "Instances": [ { "LaunchTemplateAndOverrides": { "LaunchTemplateSpecification": { "LaunchTemplateId": "lt-01234a567b8910abcEXAMPLE", "Version": "1"
        }, "Overrides": {

          "InstanceType": "c5.large", "AvailabilityZone": "us-east-1a"
        } }, "Lifecycle": "on-demand", "InstanceIds": [ "i-1234567890abcdef0", "i-9876543210abcdef9"
      ]
  ]
} The following is example output for a fleet of type instant that launched no instances.
{ "FleetId": "fleet-12a34b55-67cd-8ef9-ba9b-9208dEXAMPLE", "Errors": [ { "LaunchTemplateAndOverrides": { "LaunchTemplateSpecification": { "LaunchTemplateId": "lt-01234a567b8910abcEXAMPLE", "Version": "1"
        }, "Overrides": { "InstanceType": "c4.xlarge", "AvailabilityZone": "us-east-1a", } }, "Lifecycle": "on-demand", "ErrorCode": "InsufficientCapacity", "ErrorMessage": ""
    }, { "LaunchTemplateAndOverrides": { "LaunchTemplateSpecification": { "LaunchTemplateId": "lt-01234a567b8910abcEXAMPLE", "Version": "1"
        }, "Overrides": { "InstanceType": "c5.large", "AvailabilityZone": "us-east-1a", } },

      "Lifecycle": "on-demand", "ErrorCode": "InsufficientCapacity", "ErrorMessage": ""
    }, ], "Instances": []
}
### Create an EC2 Fleet that replaces unhealthy Spot Instances EC2 Fleet checks the health status of the instances in the fleet every two minutes. The health status of an instance is either healthy or unhealthy.
EC2 Fleet determines the health status of an instance by using the status checks provided by Amazon EC2. An instance is determined as unhealthy when the status of either the instance status check or the system status check is impaired for three consecutive health status checks. For more information, see Status checks for Amazon EC2 instances.
You can configure your fleet to replace unhealthy Spot Instances. After setting ReplaceUnhealthyInstances to true, a Spot Instance is replaced when it is reported as unhealthy. The fleet can go below its target capacity for up to a few minutes while an unhealthy Spot Instance is being replaced.
Requirements
- Health check replacement is supported only for EC2 Fleets that maintain a target capacity (fleets of type maintain), and not for fleets of type request or instant.
- Health check replacement is supported only for Spot Instances. This feature is not supported for On-Demand Instances.
- You can configure your EC2 Fleet to replace unhealthy instances only when you create it.
- Users can use health check replacement only if they have permission to call the ec2:DescribeInstanceStatus action.
To configure an EC2 Fleet to replace unhealthy Spot Instances
1. Use the information for creating an EC2 Fleet in Create an EC2 Fleet.
2. To configure the fleet to replace unhealthy Spot Instances, in the JSON file, for ReplaceUnhealthyInstances, specify true.

### View all the EC2 Fleet configuration options To view the full list of EC2 Fleet configuration parameters, you can generate a JSON file. For a description of each parameter, see create-fleet.
To generate a JSON file with all possible EC2 Fleet parameters Use the create-fleet (AWS CLI) command and the --generate-cli-skeleton parameter to generate an EC2 Fleet JSON file, and direct the output to a file to save it. aws ec2 create-fleet \ --generate-cli-skeleton input > ec2createfleet.json The following is example output.
{ "DryRun": true, "ClientToken": "", "SpotOptions": { "AllocationStrategy": "price-capacity-optimized", "MaintenanceStrategies": { "CapacityRebalance": { "ReplacementStrategy": "launch"
            } }, "InstanceInterruptionBehavior": "hibernate", "InstancePoolsToUseCount": 0, "SingleInstanceType": true, "SingleAvailabilityZone": true, "MinTargetCapacity": 0, "MaxTotalPrice": ""
    }, "OnDemandOptions": { "AllocationStrategy": "prioritized", "CapacityReservationOptions": { "UsageStrategy": "use-capacity-reservations-first"
        }, "SingleInstanceType": true, "SingleAvailabilityZone": true, "MinTargetCapacity": 0, "MaxTotalPrice": ""
    }, "ExcessCapacityTerminationPolicy": "termination",

    "LaunchTemplateConfigs": [ { "LaunchTemplateSpecification": { "LaunchTemplateId": "", "LaunchTemplateName": "", "Version": ""
            }, "Overrides": [ { "InstanceType": "r5.metal", "MaxPrice": "", "SubnetId": "", "AvailabilityZone": "", "WeightedCapacity": 0.0, "Priority": 0.0, "Placement": { "AvailabilityZone": "", "Affinity": "", "GroupName": "", "PartitionNumber": 0, "HostId": "", "Tenancy": "dedicated", "SpreadDomain": "", "HostResourceGroupArn": ""
                    }, "InstanceRequirements": { "VCpuCount": { "Min": 0, "Max": 0 }, "MemoryMiB": { "Min": 0, "Max": 0 }, "CpuManufacturers": [ "amd"
                        ], "MemoryGiBPerVCpu": { "Min": 0.0, "Max": 0.0 }, "ExcludedInstanceTypes": [ ""
                        ],

                        "InstanceGenerations": [ "previous"
                        ], "SpotMaxPricePercentageOverLowestPrice": 0, "OnDemandMaxPricePercentageOverLowestPrice": 0, "BareMetal": "included", "BurstablePerformance": "required", "RequireHibernateSupport": true, "NetworkInterfaceCount": { "Min": 0, "Max": 0 }, "LocalStorage": "excluded", "LocalStorageTypes": [ "ssd"
                        ], "TotalLocalStorageGB": { "Min": 0.0, "Max": 0.0 }, "BaselineEbsBandwidthMbps": { "Min": 0, "Max": 0 }, "AcceleratorTypes": [ "inference"
                        ], "AcceleratorCount": { "Min": 0, "Max": 0 }, "AcceleratorManufacturers": [ "amd"
                        ], "AcceleratorNames": [ "a100"
                        ], "AcceleratorTotalMemoryMiB": { "Min": 0, "Max": 0 } } } ]

        } ], "TargetCapacitySpecification": { "TotalTargetCapacity": 0, "OnDemandTargetCapacity": 0, "SpotTargetCapacity": 0, "DefaultTargetCapacityType": "on-demand", "TargetCapacityUnitType": "memory-mib"
    }, "TerminateInstancesWithExpiration": true, "Type": "instant", "ValidFrom": "1970-01-01T00:00:00", "ValidUntil": "1970-01-01T00:00:00", "ReplaceUnhealthyInstances": true, "TagSpecifications": [ { "ResourceType": "fleet", "Tags": [ { "Key": "", "Value": ""
                } ]
        } ], "Context": ""
}
## Tag a new or existing EC2 Fleet request and the instances and volumes it launches it launches To help categorize and manage your EC2 Fleet requests and the instances and volumes that it launches, you can tag them with custom metadata. You can assign a tag to an EC2 Fleet request when you create it, or afterward. Similarly, you can assign a tag to the instances and volumes when they're launched by the fleet, or afterward.
When you tag a fleet request, the instances and volumes that are launched by the fleet are not automatically tagged. You need to explicitly tag the instances and volumes launched by the fleet.
You can choose to assign tags to only the fleet request, or to only the instances launched by the fleet, or to only the volumes attached to the instances launched by the fleet, or to all of them.

Note For instant fleet types, you can tag volumes that are attached to On-Demand Instances and Spot Instances. For request or maintain fleet types, you can only tag volumes that are attached to On-Demand Instances.
For more information about how tags work, see Tag your Amazon EC2 resources.
Prerequisite Grant the user the permission to tag resources. For more information, see Example: Tag resources.
To grant a user the permission to tag resources Create a IAM policy that includes the following:
- The ec2:CreateTags action. This grants the user permission to create tags.
- The ec2:CreateFleet action. This grants the user permission to create an EC2 Fleet request.
- For Resource, we recommend that you specify "*". This allows users to tag all resource types.
To provide access, add permissions to your users, groups, or roles:
- Users and groups in AWS IAM Identity Center:
Create a permission set. Follow the instructions in Create a permission set in the AWS IAM Identity Center User Guide.
- Users managed in IAM through an identity provider:
Create a role for identity federation. Follow the instructions in Create a role for a third-party identity provider (federation) in the IAM User Guide.
- IAM users:
- Create a role that your user can assume. Follow the instructions in Create a role for an IAM user in the IAM User Guide.
- (Not recommended) Attach a policy directly to a user or add a user to a user group. Follow the instructions in Adding permissions to a user (console) in the IAM User Guide.
To tag a new EC2 Fleet request

To tag an EC2 Fleet request when you create it, specify the key-value pair in the JSON file used to create the fleet. The value for ResourceType must be fleet. If you specify another value, the fleet request fails.
To tag instances and volumes launched by an EC2 Fleet To tag instances and volumes when they are launched by the fleet, specify the tags in the launch template that is referenced in the EC2 Fleet request.
Note You can't tag volumes attached to Spot Instances that are launched by a request or maintain fleet type.
To tag an existing EC2 Fleet request, instance, and volume Use the create-tags command to tag existing resources. aws ec2 create-tags \ --resources fleet-12a34b55-67cd-8ef9- ba9b-9208dEXAMPLE i-1234567890abcdef0 vol-1234567890EXAMPLE \ --tags Key=purpose,Value=test
## Describe an EC2 Fleet, its instances, and its events You can describe your EC2 Fleet configuration, the instances in your EC2 Fleet, and the event history of your EC2 Fleet.
Tasks
- Describe your EC2 Fleet
- Describe all instances in your EC2 Fleet
- Describe the event history for your EC2 Fleet
### Describe your EC2 Fleet AWS CLI To describe your EC2 Fleet

Use the describe-fleets command. aws ec2 describe-fleets \ --fleet-ids fleet-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE The following is example output.
{ "Fleets": [ { "ActivityStatus": "fulfilled", "CreateTime": "2022-02-09T03:35:52+00:00", "FleetId": "fleet-364457cd-3a7a-4ed9-83d0-7b63e51bb1b7", "FleetState": "active", "ExcessCapacityTerminationPolicy": "termination", "FulfilledCapacity": 2.0, "FulfilledOnDemandCapacity": 0.0, "LaunchTemplateConfigs": [ { "LaunchTemplateSpecification": { "LaunchTemplateName": "my-launch-template", "Version": "$Latest"
                    } } ], "TargetCapacitySpecification": { "TotalTargetCapacity": 2, "OnDemandTargetCapacity": 0, "SpotTargetCapacity": 2, "DefaultTargetCapacityType": "spot"
            }, "TerminateInstancesWithExpiration": false, "Type": "maintain", "ReplaceUnhealthyInstances": false, "SpotOptions": { "AllocationStrategy": "capacity-optimized", "InstanceInterruptionBehavior": "terminate"
            }, "OnDemandOptions": { "AllocationStrategy": "lowestPrice"
            } } ]

} PowerShell To describe your EC2 Fleet Use the Get-EC2FleetList cmdlet.
Get-EC2FleetList `
    -FleetId fleet-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE
### Describe all instances in your EC2 Fleet The returned list of running instances is refreshed periodically and might be out of date.
AWS CLI To describe the instances for the specified EC2 Fleet Use the describe-fleet-instances command. aws ec2 describe-fleet-instances \ --fleet-id fleet-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE The following is example output.
{ "ActiveInstances": [ { "InstanceId": "i-09cd595998cb3765e", "InstanceHealth": "healthy", "InstanceType": "m4.large", "SpotInstanceRequestId": "sir-86k84j6p"
        }, { "InstanceId": "i-09cf95167ca219f17", "InstanceHealth": "healthy", "InstanceType": "m4.large", "SpotInstanceRequestId": "sir-dvxi7fsm"
        }

    ], "FleetId": "fleet-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE"
} PowerShell To describe the instances for the specified EC2 Fleet Use the Get-EC2FleetInstanceList cmdlet.
Get-EC2FleetInstanceList `
    -FleetId fleet-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE
### Describe the event history for your EC2 Fleet For more information about the events in the event history, see EC2 Fleet event types.
AWS CLI To describe the events for the specified EC2 Fleet Use the describe-fleet-history command. aws ec2 describe-fleet-history \ --fleet-id fleet-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE \ --start-time 2020-06-01T00:00:00Z The following is example output.
{ "HistoryRecords": [ { "EventInformation": { "EventSubType": "submitted"
            }, "EventType": "fleetRequestChange", "Timestamp": "2020-09-01T18:26:05.000Z"
        }, { "EventInformation": { "EventSubType": "active"

            }, "EventType": "fleetRequestChange", "Timestamp": "2020-09-01T18:26:15.000Z"
        }, { "EventInformation": { "EventDescription": "t2.small, ami-07c8bc5c1ce9598c3, ...", "EventSubType": "progress"
            }, "EventType": "fleetRequestChange", "Timestamp": "2020-09-01T18:26:17.000Z"
        }, { "EventInformation": { "EventDescription": "{\"instanceType\":\"t2.small\", ...}", "EventSubType": "launched", "InstanceId": "i-083a1c446e66085d2"
            }, "EventType": "instanceChange", "Timestamp": "2020-09-01T18:26:17.000Z"
        }, { "EventInformation": { "EventDescription": "{\"instanceType\":\"t2.small\", ...}", "EventSubType": "launched", "InstanceId": "i-090db02406cc3c2d6"
            }, "EventType": "instanceChange", "Timestamp": "2020-09-01T18:26:17.000Z"
        } ], "FleetId": "fleet-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE", "LastEvaluatedTime": "1970-01-01T00:00:00.000Z", "StartTime": "2020-06-01T00:00:00.000Z"
} PowerShell To describe the events for the specified EC2 Fleet Use the Get-EC2FleetHistory cmdlet.
Get-EC2FleetHistory `
    -FleetId fleet-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE `

    -UtcStartTime 2020-06-01T00:00:00Z
## Modify an EC2 Fleet You can modify the total target capacity, Spot capacity, and On-Demand capacity of an EC2 Fleet.
You can also modify whether running instances should be terminated if the new total target capacity is reduced below the current size of the fleet.
### Considerations Consider the following when modifying an EC2 Fleet:
- Fleet type – You can only modify an EC2 Fleet of type maintain. You can't modify an EC2 Fleet of type request or instant.
- Fleet parameters – You can modify the following parameters of an EC2 Fleet:
- target-capacity-specification – Increase or decrease the target capacity for:
- TotalTargetCapacity
- OnDemandTargetCapacity
- SpotTargetCapacity
- excess-capacity-termination-policy – Whether running instances should be terminated if the total target capacity of the EC2 Fleet is decreased below the current size of the fleet. Valid values are:
- no-termination
- termination
- Fleet behavior when increasing total target capacity – When you increase the total target capacity, the EC2 Fleet launches the additional instances according to the instance purchasing option specified for DefaultTargetCapacityType, which is either On-Demand Instances or Spot Instances, and according to the specified allocation strategy.
- Fleet behavior when decreasing Spot target capacity – When you decrease the Spot target capacity, the EC2 Fleet deletes any open requests that exceed the new target capacity. You can request that the fleet terminate Spot Instances until the size of the fleet reaches the new target capacity. When an EC2 Fleet terminates a Spot Instance because the target capacity was decreased, the instance receives a Spot Instance interruption notice.
Instances are selected for termination based on the allocation strategy:

- capacity-optimized – Terminates instances from pools with the least available capacity.
- price-capacity-optimized – Uses a combination of price and available capacity: terminates instances from pools with the least available capacity and which are the highest- priced among these pools.
- diversified – Terminates instances across all pools.
- lowest-price – Terminates instances from highest-priced pools.
Alternatively, you can request that EC2 Fleet keep the fleet at its current size, but not replace any Spot Instances that are interrupted or that you terminate manually.
- Fleet state – You can modify an EC2 Fleet that is in the submitted or active state. When you modify a fleet, it enters the modifying state.
### Commands for modifying an EC2 Fleet AWS CLI To modify the total target capacity of an EC2 Fleet Use the modify-fleet command. aws ec2 modify-fleet \ --fleet-id fleet-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE \ --target-capacity-specification TotalTargetCapacity=20 If you are decreasing the target capacity but want to keep the fleet at its current size, you can modify the previous example as follows. aws ec2 modify-fleet \ --fleet-id fleet-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE \ --target-capacity-specification TotalTargetCapacity=10 \ --excess-capacity-termination-policy no-termination PowerShell To modify the total target capacity of an EC2 Fleet Use the Edit-EC2Fleet cmdlet.
Edit-EC2Fleet `

    -FleetId "fleet-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE" `
    -TargetCapacitySpecification_TotalTargetCapacity 20 If you are decreasing the target capacity but want to keep the fleet at its current size, you can modify the previous example as follows.
Edit-EC2Fleet `
    -FleetId "fleet-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE" `
    -TargetCapacitySpecification_TotalTargetCapacity 20 `
    -ExcessCapacityTerminationPolicy "NoTermination"
## Delete an EC2 Fleet request and the instances in the fleet If you no longer require an EC2 Fleet request, you can delete it. After you delete a fleet request, all Spot requests associated with the fleet are canceled, so that no new Spot Instances are launched.
When you delete an EC2 Fleet request, you must also specify if you want to terminate all of its instances. These include both On-Demand Instances and Spot Instances. For instant fleets, EC2 Fleet must terminate the instances when the fleet is deleted. A deleted instant fleet with running instances is not supported.
Warning Terminating an instance is permanent and irreversible.
After you terminate an instance, you can no longer connect to it, and it can't be recovered.
All attached Amazon EBS volumes that are configured to be deleted on termination are also permanently deleted and can't be recovered. All data stored on instance store volumes is permanently lost. For more information, see How instance termination works.
Before you terminate an instance, ensure that you have backed up all data that you need to retain after the termination to persistent storage.
If you specify that the instances must be terminated when the fleet request is deleted, the fleet request enters the deleted_terminating state. Otherwise, it enters the deleted_running state, and the instances continue to run until they are interrupted or you terminate them manually.
Restrictions
- You can delete up to 25 fleets of type instant in a single operation.

- You can delete up to 100 fleets of type maintain or request in a single operation.
- You can delete up to 125 fleets in a single operation, provided you do not exceed the quota for each fleet type, as specified above.
- If you exceed the specified number of fleets to delete, no fleets are deleted.
- A deleted instant fleet with running instances is not supported. When you delete an instant fleet, Amazon EC2 automatically terminates all its instances. For instant fleets with more than 1000 instances, the deletion request might fail. If your fleet has more than 1000 instances, first terminate most of the instances manually, leaving 1000 or fewer. Then delete the fleet, and the remaining instances will be terminated automatically.
AWS CLI To delete an EC2 Fleet request and terminate its instances Use the delete-fleets command with the --terminate-instances option. aws ec2 delete-fleets \ --fleet-ids fleet-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE \ --terminate-instances The following is example output.
{ "UnsuccessfulFleetDeletions": [], "SuccessfulFleetDeletions": [ { "CurrentFleetState": "deleted_terminating", "PreviousFleetState": "active", "FleetId": "fleet-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE"
        } ]
} To delete an EC2 Fleet request without terminating its instances Modify the previous example by using the --no-terminate-instances option instead. Note that --no-terminate-instances is not supported for instant fleets. aws ec2 delete-fleets \ --fleet-ids fleet-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE \

    --no-terminate-instances The following is example output.
{ "UnsuccessfulFleetDeletions": [], "SuccessfulFleetDeletions": [ { "CurrentFleetState": "deleted_running", "PreviousFleetState": "active", "FleetId": "fleet-4b8aaae8-dfb5-436d-a4c6-3dafa4c6b7dcEXAMPLE"
        } ]
} PowerShell To delete an EC2 Fleet request and terminate its instances Use the Remove-EC2Fleet cmdlet with the -TerminateInstance parameter.
Remove-EC2Fleet `
    -FleetId "fleet-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE" `
    -TerminateInstance $true To delete an EC2 Fleet request without terminating its instances Modify the previous example by changing the value of the -TerminateInstance parameter.
Remove-EC2Fleet `
    -FleetId "fleet-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE" `
    -TerminateInstance $false
### Troubleshoot when a fleet fails to delete If an EC2 Fleet request fails to delete, UnsuccessfulFleetDeletions in the output returns the ID of the EC2 Fleet request, an error code, and an error message.
The error codes are:
- ExceededInstantFleetNumForDeletion

- fleetIdDoesNotExist
- fleetIdMalformed
- fleetNotInDeletableState
- NoTerminateInstancesNotSupported
- UnauthorizedOperation
- unexpectedError Troubleshoot ExceededInstantFleetNumForDeletion If you try to delete more than 25 instant fleets in a single request, the ExceededInstantFleetNumForDeletion error is returned. The following is example output for this error.
{ "UnsuccessfulFleetDeletions": [ { "FleetId": " fleet-5d130460-0c26-bfd9-2c32-0100a098f625", "Error": { "Message": "Can't delete more than 25 instant fleets in a single request.", "Code": "ExceededInstantFleetNumForDeletion"
           } }, { "FleetId": "fleet-9a941b23-0286-5bf4-2430-03a029a07e31", "Error": { "Message": "Can't delete more than 25 instant fleets in a single request.", "Code": "ExceededInstantFleetNumForDeletion"
            } } .
     .
     .
     ], "SuccessfulFleetDeletions": []
} Troubleshoot NoTerminateInstancesNotSupported

If you specify that the instances in an instant fleet must not be terminated when you delete the fleet, the NoTerminateInstancesNotSupported error is returned. --no-terminate- instances is not supported for instant fleets. The following is example output for this error.
{ "UnsuccessfulFleetDeletions": [ { "FleetId": "fleet-5d130460-0c26-bfd9-2c32-0100a098f625", "Error": { "Message": "NoTerminateInstances option is not supported for instant fleet", "Code": "NoTerminateInstancesNotSupported"
                   } } ], "SuccessfulFleetDeletions": []
} Troubleshoot UnauthorizedOperation If you do not have permission to terminate instances, you get the UnauthorizedOperation error when deleting a fleet that must terminate its instances. The following is the error response.
<Response><Errors><Error><Code>UnauthorizedOperation</Code><Message>You are not authorized to perform this operation. Encoded authorization failure message: VvuncIxj7Z_CPGNYXWqnuFV- YjByeAU66Q9752NtQ-I3-qnDLWs6JLFd KnSMMiq5s6cGqjjPtEDpsnGHzzyHasFHOaRYJpaDVravoW25azn6KNkUQQlFwhJyujt2dtNCdduJfrqcFYAjlEiRMkfDHt7 BHturzDK6A560Y2nDSUiMmAB1y9UNtqaZJ9SNe5sNxKMqZaqKtjRbk02RZu5V2vn9VMk6fm2aMVHbY9JhLvGypLcMUjtJ76 VPiU5v2s- UgZ7h0p2yth6ysUdhlONg6dBYu8_y_HtEI54invCj4CoK0qawqzMNe6rcmCQHvtCxtXsbkgyaEbcwmrm2m01- EMhekLFZeJLr DtYOpYcEl4_nWFX1wtQDCnNNCmxnJZAoJvb3VMDYpDTsxjQv1PxODZuqWHs23YXWVywzgnLtHeRf2o4lUhGBw17mXsS07k7 PT9vrHtQiILor5VVTsjSPWg7edj__1rsnXhwPSu8gI48ZLRGrPQqFq0RmKO_QIE8N8s6NWzCK4yoX-9gDcheurOGpkprPIC </Message></Error></Errors><RequestID>89b1215c-7814-40ae-a8db-41761f43f2b0</ RequestID></Response>
To resolve the error, you must add the ec2:TerminateInstances action to the IAM policy, as shown in the following example.
