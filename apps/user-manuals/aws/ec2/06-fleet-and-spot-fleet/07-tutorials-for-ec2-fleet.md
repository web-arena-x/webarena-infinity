# Tutorials for EC2 Fleet

Source: apps/user-manuals/aws/ec2-ug.pdf

---

iamFleetRoleInvalid The Spot Fleet does not have the required permissions to either launch or terminate an instance. allLaunchSpecsTemporarilyBlacklisted None of the configurations are valid, and several attempts to launch instances have failed. For more information, see the description of the event. spotInstanceCountLimitExceeded You've reached the limit on the number of Spot Instances that you can launch. spotFleetRequestConfigurationInvalid The configuration is not valid. For more information, see the description of the event.
# Tutorials for EC2 Fleet There are different ways to configure an EC2 Fleet. The configuration you choose depends on your specific use case.
The following tutorials cover some of the possible use cases and provide the tasks required to implement them.
Use case Link to tutorial Use instance weighting to manage the availability and performance  of your EC2 Fleet.
With instance weighting, you assign a weight to each instance type in your EC2 Fleet to  represent their compute capacity and performance relative to each other.  Based on the weights, the fleet can use any combinati on of the specified instance types, as long as it can fulfil the desired target  capacity.
## Tutorial: Configure EC2 Fleet to use On-Demand Instances as the primary capacity weighting

Use case Link to tutorial Use On-Demand capacity to ensure availabil ity during peak periods,  but benefit from additional Spot capacity at a lower  cost.
Configure your EC2 Fleet to use On-Demand Instances as the primary capacity to ensure available capacity  during peak periods. In addition, allocate some capacity to Spot Instances to  benefit from discounted pricing, while keeping in mind that Spot Instances can be  interrupted if Amazon EC2 needs the capacity back.
## Tutorial: Configure EC2 Fleet to launch On-Demand Instances using targeted Capacity Reservations Demand Instances as the primary capacity Use Capacity Reservations to reserve compute capacity for your  On-Demand Instances.
Configure your EC2 Fleet to use targeted Capacity Reservations first when launching On-Demand Instances. If  you have strict capacity requirements, and are running business-critical  workloads that require a certain level of long or short-term capacity assurance, we recommend that you create a Capacity Reservation to ensure that you always have access to Amazon EC2 capacity when you need it, for as long  as you need it.
Tutorial: Configure EC2 Fleet to launch On- Demand Instances using targeted Capacity Reservations Use Capacity Blocks to reserve highly sought-after GPU instances for  your ML workloads.
Configure your EC2 Fleet to launch instances into Capacity Blocks.
## Tutorial: Configure your EC2 Fleet to launch instances into Capacity Blocks instances into Capacity Blocks

## Tutorial: Configure EC2 Fleet to use instance weighting This tutorial uses a fictitious company called Example Corp to illustrate the process of requesting an EC2 Fleet using instance weighting.
### Objective Example Corp, a pharmaceutical company, wants to use the computational power of Amazon EC2 for screening chemical compounds that might be used to fight cancer.
### Planning Example Corp first reviews Spot Best Practices. Next, Example Corp determines the requirements for their EC2 Fleet.
Instance types Example Corp has a compute- and memory-intensive application that performs best with at least 60 GB of memory and eight virtual CPUs (vCPUs). They want to maximize these resources for the application at the lowest possible price. Example Corp decides that any of the following EC2 instance types would meet their needs:
Instance type Memory (GiB) vCPUs r3.2xlarge 61 8 r3.4xlarge 122 16 r3.8xlarge 244 32 Target capacity in units With instance weighting, target capacity can equal a number of instances (the default) or a combination of factors such as cores (vCPUs), memory (GiBs), and storage (GBs). By considering the base for their application (60 GB of RAM and eight vCPUs) as one unit, Example Corp decides that 20 times this amount would meet their needs. So the company sets the target capacity of their EC2 Fleet request to 20 units.

Instance weights After determining the target capacity, Example Corp calculates instance weights. To calculate the instance weight for each instance type, they determine the units of each instance type that are required to reach the target capacity as follows:
- r3.2xlarge (61.0 GB, 8 vCPUs) = 1 unit of 20
- r3.4xlarge (122.0 GB, 16 vCPUs) = 2 units of 20
- r3.8xlarge (244.0 GB, 32 vCPUs) = 4 units of 20 Therefore, Example Corp assigns instance weights of 1, 2, and 4 to the respective launch configurations in their EC2 Fleet request.
Price per unit hour Example Corp uses the On-Demand price per instance hour as a starting point for their price. They could also use recent Spot prices, or a combination of the two. To calculate the price per unit hour, they divide their starting price per instance hour by the weight. For example:
Instance type On-Demand price Instance weight Price per unit hour r3.2xLarge $0.7 1 $0.7 r3.4xLarge $1.4 2 $0.7 r3.8xLarge $2.8 4 $0.7 Example Corp could use a global price per unit hour of $0.7 and be competitive for all three instance types. They could also use a global price per unit hour of $0.7 and a specific price per unit hour of $0.9 in the r3.8xlarge launch specification.
### Verify permissions Before creating an EC2 Fleet, Example Corp verifies that it has an IAM role with the required permissions. For more information, see EC2 Fleet prerequisites.

### Create a launch template Next, Example Corp creates a launch template. The launch template ID is used in the following step. For more information, see Create an Amazon EC2 launch template.
### Create the EC2 Fleet Example Corp creates a file, config.json, with the following configuration for its EC2 Fleet. In the following example, replace the resource identifiers with your own resource identifiers.
{ "LaunchTemplateConfigs": [ { "LaunchTemplateSpecification": { "LaunchTemplateId": "lt-07b3bc7625cdab851", "Version": "1"
            }, "Overrides": [ { "InstanceType": "r3.2xlarge", "SubnetId": "subnet-482e4972", "WeightedCapacity": 1 }, { "InstanceType": "r3.4xlarge", "SubnetId": "subnet-482e4972", "WeightedCapacity": 2 }, { "InstanceType": "r3.8xlarge", "MaxPrice": "0.90", "SubnetId": "subnet-482e4972", "WeightedCapacity": 4 } ]
        } ], "TargetCapacitySpecification": { "TotalTargetCapacity": 20, "DefaultTargetCapacityType": "spot"
    } }

Example Corp creates the EC2 Fleet using the following create-fleet command. aws ec2 create-fleet --cli-input-json file://config.json For more information, see Create an EC2 Fleet.
### Fulfillment The allocation strategy determines which Spot capacity pools your Spot Instances come from.
With the lowest-price strategy (which is the default strategy), the Spot Instances come from the pool with the lowest price per unit at the time of fulfillment. To provide 20 units of capacity, the EC2 Fleet launches either 20 r3.2xlarge instances (20 divided by 1), 10 r3.4xlarge instances (20 divided by 2), or 5 r3.8xlarge instances (20 divided by 4).
If Example Corp used the diversified strategy, the Spot Instances would come from all three pools. The EC2 Fleet would launch 6 r3.2xlarge instances (which provide 6 units), 3 r3.4xlarge instances (which provide 6 units), and 2 r3.8xlarge instances (which provide 8 units), for a total of 20 units.
Tutorial: Configure EC2 Fleet to use On-Demand Instances as the primary capacity This tutorial uses a fictitious company called ABC Online to illustrate the process of requesting an EC2 Fleet with On-Demand as the primary capacity, and Spot capacity if available.
### Objective ABC Online, a restaurant delivery company, aims to provision Amazon EC2 capacity across EC2 instance types and purchasing options to achieve their desired scale, performance, and cost.
### Plan ABC Online requires a fixed capacity to handle peak periods, but would like to benefit from additional capacity at a lower cost. The company determines the following requirements for their EC2 Fleet:
- On-Demand Instance capacity – ABC Online requires 15 On-Demand Instances to ensure that they can accommodate traffic at peak periods.

- Spot Instance capacity – To enhance performance, but at a lower price, ABC Online plans to provision 5 Spot Instances.
### Verify permissions Before creating an EC2 Fleet, ABC Online verifies that it has an IAM role with the required permissions. For more information, see EC2 Fleet prerequisites.
### Create a launch template Next, ABC Online creates a launch template. The launch template ID is used in the following step.
For more information, see Create an Amazon EC2 launch template.
### Create the EC2 Fleet ABC Online creates a file, config.json, with the following configuration for its EC2 Fleet. In the following example, replace the resource identifiers with your own resource identifiers.
{ "LaunchTemplateConfigs": [ { "LaunchTemplateSpecification": { "LaunchTemplateId": "lt-07b3bc7625cdab851", "Version": "2"
            } } ], "TargetCapacitySpecification": { "TotalTargetCapacity": 20, "OnDemandTargetCapacity":15, "DefaultTargetCapacityType": "spot"
    } } ABC Online creates the EC2 Fleet using the following create-fleet command. aws ec2 create-fleet --cli-input-json file://config.json For more information, see Create an EC2 Fleet.

### Fulfillment The allocation strategy determines that the On-Demand capacity is always fulfilled, while the balance of the target capacity is fulfilled as Spot if there is available capacity.
Tutorial: Configure EC2 Fleet to launch On-Demand Instances using targeted Capacity Reservations This tutorial walks you through all the steps that you must perform so that your EC2 Fleet launches On-Demand Instances into targeted Capacity Reservations.
You will learn how to configure a fleet to use targeted On-Demand Capacity Reservations first when launching On-Demand Instances. You will also learn how to configure the fleet so that, when the total On-Demand target capacity exceeds the number of available unused Capacity Reservations, the fleet uses the specified allocation strategy for selecting the instance pools in which to launch the remaining target capacity.
EC2 Fleet configuration In this tutorial, the fleet is configured as follows:
- Target capacity: 10 On-Demand Instances
- Total unused targeted Capacity Reservations: 6 (less than the fleet's On-Demand target capacity of 10 On-Demand Instances)
- Number of Capacity Reservation pools: 2 (us-east-1a and us-east-1b)
- Number of Capacity Reservations per pool: 3
- On-Demand allocation strategy: lowest-price (When the number of unused Capacity Reservations is less than the On-Demand target capacity, the fleet determines the pools in which to launch the remaining On-Demand capacity based on the On-Demand allocation strategy.)
Note that you can also use the prioritized allocation strategy instead of the lowest-price allocation strategy.
To launch On-Demand Instances into targeted Capacity Reservations, you must perform a number of steps, as follows:
- Step 1: Create Capacity Reservations
- Step 2: Create a Capacity Reservation resource group

- Step 3: Add the Capacity Reservations to the Capacity Reservation resource group
- (Optional) Step 4: View the Capacity Reservations in the resource group
- Step 5: Create a launch template that specifies that the Capacity Reservation targets a specific resource group
- (Optional) Step 6: Describe the launch template
- Step 7: Create an EC2 Fleet
- (Optional) Step 8: View the number of remaining unused Capacity Reservations
### Step 1: Create Capacity Reservations Use the create-capacity-reservation command to create the Capacity Reservations, three for us- east-1a and another three for us-east-1b. Except for the Availability Zone, the other attributes of the Capacity Reservations are identical.
3 Capacity Reservations in us-east-1a aws ec2 create-capacity-reservation \ --availability-zone us-east-1a \ --instance-type c5.xlarge \ --instance-platform Linux/UNIX \ --instance-count 3 \ --instance-match-criteria targeted Example of resulting Capacity Reservation ID cr-1234567890abcdef1 3 Capacity Reservations in us-east-1b aws ec2 create-capacity-reservation \ --availability-zone us-east-1b \ --instance-type c5.xlarge \ --instance-platform Linux/UNIX \ --instance-count 3 \ --instance-match-criteria targeted Example of resulting Capacity Reservation ID

cr-54321abcdef567890
### Step 2: Create a Capacity Reservation resource group Use the resource-groups service and the create-group command to create a Capacity Reservation resource group. In this example, the resource group is named my-cr-group. For information about why you must create a resource group, see Use Capacity Reservations to reserve On-Demand capacity in EC2 Fleet. aws resource-groups create-group \ --name my-cr-group \ --configuration '{"Type":"AWS::EC2::CapacityReservationPool"}'
 '{"Type":"AWS::ResourceGroups::Generic", "Parameters": [{"Name": "allowed-resource- types", "Values": ["AWS::EC2::CapacityReservation"]}]}'
### Step 3: Add the Capacity Reservations to the Capacity Reservation resource group Use the resource-groups service and the group-resources command to add the Capacity Reservations that you created in Step 1 to the Capacity Reservations resource group. Note that you must reference the On-Demand Capacity Reservations by their ARNs. aws resource-groups group-resources \ --group my-cr-group \ --resource-arns \ arn:aws:ec2:us-east-1:123456789012:capacity-reservation/cr-1234567890abcdef1 \ arn:aws:ec2:us-east-1:123456789012:capacity-reservation/cr-54321abcdef567890 Example output { "Failed": [], "Succeeded": [ "arn:aws:ec2:us-east-1:123456789012:capacity-reservation/cr-1234567890abcdef1", "arn:aws:ec2:us-east-1:123456789012:capacity-reservation/cr-54321abcdef567890"
   ]
}

### (Optional) Step 4: View the Capacity Reservations in the resource group Use the resource-groups service and the list-group-resources command to optionally describe the resource group to view its Capacity Reservations. aws resource-groups list-group-resources --group my-cr-group Example output { "ResourceIdentifiers": [ { "ResourceType": "AWS::EC2::CapacityReservation", "ResourceArn": "arn:aws:ec2:us-east-1:123456789012:capacity-reservation/ cr-1234567890abcdef1"
        }, { "ResourceType": "AWS::EC2::CapacityReservation", "ResourceArn": "arn:aws:ec2:us-east-1:123456789012:capacity-reservation/ cr-54321abcdef567890"
        } ]
}
### Step 5: Create a launch template that specifies that the Capacity Reservation targets a specific resource group targets a specific resource group Use the create-launch-template command to create a launch template in which to specify the Capacity Reservations to use. In this example, the fleet will use targeted Capacity Reservations, which have been added to a resource group. Therefore, the launch template data specifies that the Capacity Reservation targets a specific resource group. In this example, the launch template is named my-launch-template. aws ec2 create-launch-template \ --launch-template-name my-launch-template \ --launch-template-data \ '{"ImageId": "ami-0123456789example", "CapacityReservationSpecification":
            {"CapacityReservationTarget":
                { "CapacityReservationResourceGroupArn": "arn:aws:resource-groups:us- east-1:123456789012:group/my-cr-group" }

            } }'
### (Optional) Step 6: Describe the launch template Use the describe-launch-template-versions command to optionally describe the launch template to view its configuration. aws ec2 describe-launch-template-versions --launch-template-name my-launch-template Example output { "LaunchTemplateVersions": [ { "LaunchTemplateId": "lt-01234567890example", "LaunchTemplateName": "my-launch-template", "VersionNumber": 1, "CreateTime": "2021-01-19T20:50:19.000Z", "CreatedBy": "arn:aws:iam::123456789012:user/Admin", "DefaultVersion": true, "LaunchTemplateData": { "ImageId": "ami-0947d2ba12ee1ff75", "CapacityReservationSpecification": { "CapacityReservationTarget": { "CapacityReservationResourceGroupArn": "arn:aws:resource- groups:us-east-1:123456789012:group/my-cr-group"
                    } } } } ]
}
### Step 7: Create an EC2 Fleet Create an EC2 Fleet that specifies the configuration information for the instances that it will launch. The following EC2 Fleet configuration shows only the pertinent configurations for this example. The launch template my-launch-template is the launch template you created in Step
5. There are two instance pools, each with the same instance type (c5.xlarge), but with different

Availability Zones (us-east-1a and us-east-1b). The price of the instance pools is the same because pricing is defined for the Region, not per Availability Zone. The total target capacity is 10, and the default target capacity type is on-demand. The On-Demand allocation strategy is lowest-price. The usage strategy for Capacity Reservations is use-capacity-reservations- first.
Note The fleet type must be instant. Other fleet types do not support use-capacity- reservations-first.
{ "LaunchTemplateConfigs": [ { "LaunchTemplateSpecification": { "LaunchTemplateName": "my-launch-template", "Version": "1"
            }, "Overrides": [ { "InstanceType": "c5.xlarge", "AvailabilityZone": "us-east-1a"
               }, { "InstanceType": "c5.xlarge", "AvailabilityZone": "us-east-1b"
               } ]
        } ], "TargetCapacitySpecification": { "TotalTargetCapacity": 10, "DefaultTargetCapacityType": "on-demand"
    }, "OnDemandOptions": { "AllocationStrategy": "lowest-price", "CapacityReservationOptions": { "UsageStrategy": "use-capacity-reservations-first"
         } }, "Type": "instant"

} After you create the instant fleet using the preceding configuration, the following 10 instances are launched to meet the target capacity:
- The Capacity Reservations are used first to launch 6 On-Demand Instances as follows:
- 3 On-Demand Instances are launched into the 3 c5.xlarge targeted Capacity Reservations in us-east-1a
- 3 On-Demand Instances are launched into the 3 c5.xlarge targeted Capacity Reservations in us-east-1b
- To meet the target capacity, 4 additional On-Demand Instances are launched into regular On- Demand capacity according to the On-Demand allocation strategy, which is lowest-price in this example. However, because the pools are the same price (because price is per Region and not per Availability Zone), the fleet launches the remaining 4 On-Demand Instances into either of the pools.
### (Optional) Step 8: View the number of remaining unused Capacity Reservations After the fleet is launched, you can optionally run describe-capacity-reservations to see how many unused Capacity Reservations are remaining. In this example, you should see the following response, which shows that all of the Capacity Reservations in all of the pools were used.
{ "CapacityReservationId":  "cr-111", "InstanceType":  "c5.xlarge", "AvailableInstanceCount":  0 } { "CapacityReservationId":  "cr-222", "InstanceType":  "c5.xlarge", "AvailableInstanceCount":  0 } Tutorial: Configure your EC2 Fleet to launch instances into Capacity Blocks This tutorial walks you through the steps that you must perform so that your EC2 Fleet launches instances into Capacity Blocks.

In most cases, the target capacity of the EC2 Fleet request should be less than or equal to the available capacity of the Capacity Block reservation that you are targeting. Target capacity requests that exceed the limits of the Capacity Block reservation will not be fulfilled. If the target capacity request exceeds the limits of your Capacity Block reservation, you will receive an Insufficient Capacity Exception for the capacity that exceeds the limits of your Capacity Block reservation.
Note For Capacity Blocks, EC2 Fleet will not fallback to launching On-Demand Instances for the remainder of the desired target capacity.
If EC2 Fleet is unable to fulfill the requested target capacity in an available Capacity Block reservation, EC2 Fleet will fulfill as much capacity as it can and return the instances that it was able to launch. You can repeat the call to EC2 Fleet again until all the instances are provisioned.
After configuring the EC2 Fleet request, you must wait until the start date of your Capacity Block reservation. If you make requests to EC2 Fleet to launch into a Capacity Block that hasn't started yet, you will receive an Insufficient Capacity Error.
After your Capacity Block reservation becomes active, you can make EC2 Fleet API calls and provision the instances into your Capacity Block based on the parameters you selected. Instances running in the Capacity Block continue to run until you manually stop or terminate them or until Amazon EC2 terminates the instances when the Capacity Block reservation ends.
For more information about Capacity Blocks, see Capacity Blocks for ML.
Considerations
- Only EC2 Fleet requests of type instant are supported for launching instances into Capacity Blocks. For more information, see Configure an EC2 Fleet of type instant.
- Multiple Capacity Blocks in the same EC2 Fleet request aren't supported.
- Using OnDemandTargetCapacity or SpotTargetCapacity while also setting capacity- block as the DefaultTargetCapacity isn't supported.
- If DefaultTargetCapacityType is set to capacity-block, you can't provide OnDemandOptions::CapacityReservationOptions. An exception will occur.

To configure an EC2 Fleet to launch instances into Capacity Blocks
1. Create a launch template.
In the launch template, do the following:
- For InstanceMarketOptionsRequest, set MarketType to capacity-block.
- To target the Capacity Block reservation, for CapacityReservationID, specify the Capacity Block reservation ID.
Make note of launch template name and version. You'll use this information in the next step.
For more information about creating a launch template, see Create an Amazon EC2 launch template.
2. Configure the EC2 Fleet.
Create a file, config.json, with the following configuration for your EC2 Fleet. In the following example, replace the resource identifiers with your own resource identifiers.
For more information about configuring an EC2 Fleet, see Create an EC2 Fleet.
{ "LaunchTemplateConfigs": [ { "LaunchTemplateSpecification": { "LaunchTemplateName": "CBR-launch-template", "Version": "1"
            }, "Overrides": [ { "InstanceType": "p5.48xlarge", "AvailabilityZone": "us-east-1a"
                }, ]
        } ], "TargetCapacitySpecification": { "TotalTargetCapacity": 10, "DefaultTargetCapacityType": "capacity-block"
    }, "Type": "instant"
