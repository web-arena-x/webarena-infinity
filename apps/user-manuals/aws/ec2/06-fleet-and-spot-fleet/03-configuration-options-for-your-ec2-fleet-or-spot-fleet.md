# Configuration options for your EC2 Fleet or Spot Fleet

Source: apps/user-manuals/aws/ec2-ug.pdf

---

Fleet method When to use?
Use case lifecycle, rather use an Auto Scaling group.
# Configuration options for your EC2 Fleet or Spot Fleet When planning your EC2 Fleet or Spot Fleet, we recommend that you consider the following options when deciding how to configure your fleet.
Configura tion option Question Documentation Fleet request type Do you want a fleet that submits a one-time request for the desired target capacity, or  a fleet that maintains target capacity over time?
EC2 Fleet and Spot Fleet request types Spot Instances Do you plan to include Spot Instances in your fleet? Review the Spot best practices and use them  when you plan your fleet so that you can provision the instances at the  lowest possible price.
Best practices for Amazon EC2 Spot Spending limit for your fleet Do you want to limit how much you'll pay for your fleet per hour?
Set a spending limit for your EC2 Fleet or Spot Fleet Instance types and attribute -based instance type selection Do you want to specify the instance types in your fleet, or let Amazon EC2  select the instance types that meet your application  requirements?
Specify attributes for instance type selection for EC2 Fleet or Spot Fleet

Configura tion option Question Documentation Instance weighting Do you want to assign weights to each instance type to represent their compute capacity  and performance, so that Amazon EC2 can select any combination of available instance types to fulfil your desired target capacity?
Use instance weighting to manage cost and performanc e of your EC2 Fleet or Spot Fleet Allocation strategies Do you want to decide whether to optimize for available capacity, price, or instance  types to use for the Spot Instances and On-Demand Instances in your fleet?
Use allocation strategies to determine how EC2 Fleet or Spot Fleet fulfills Spot and On-Demand capacity Capacity Rebalanci ng Do you want your fleet to automatically replace at-risk Spot Instances?
Use Capacity Rebalancing in EC2 Fleet and Spot Fleet  to replace at-risk Spot Instances On- Demand Capacity Reservati on Do you want to reserve capacity for the On- Demand Instances in your fleet?
Use Capacity Reservations to reserve  On-Demand capacity in EC2 Fleet
## EC2 Fleet and Spot Fleet request types The request type for an EC2 Fleet or Spot Fleet determines whether the request is synchronous or asynchronous, and whether it is a one-time request for the desired target capacity or an ongoing effort to maintain the capacity over time. When configuring your fleet, you must specify the request type.
Both EC2 Fleet and Spot Fleet offer two request types: request and maintain. In addition, EC2 Fleet offers a third request type called instant.

Fleet request types instant (EC2 Fleet only)
If you configure the request type as instant, EC2 Fleet places a synchronous one-time request for your desired capacity. In the API response, it returns the instances that launched and provides errors for those instances that could not be launched. For more information, see Configure an EC2 Fleet of type instant. request If you configure the request type as request, the fleet places an asynchronous one-time request for your desired capacity. If capacity diminishes due to Spot interruptions, the fleet does not attempt to replenish Spot Instances, nor does it submit requests in alternative Spot capacity pools if capacity is unavailable. When creating a Spot Fleet of type request using the console, clear the Maintain target capacity checkbox. maintain (default)
If you configure the request type as maintain, the fleet places an asynchronous request for your desired capacity, and maintains it by automatically replenishing any interrupted Spot Instances. When creating a Spot Fleet of type maintain using the console, select the Maintain target capacity checkbox
### Configure an EC2 Fleet of type instant The EC2 Fleet of type instant is a synchronous one-time request that makes only one attempt to launch your desired capacity. The API response lists the instances that launched, along with errors for those instances that could not be launched. There are several benefits to using an EC2 Fleet of type instant, which are described in this article. Example configurations are provided at the end of the article.
For workloads that need a launch-only API to launch EC2 instances, you can use the RunInstances API. However, with RunInstances, you can only launch On-Demand Instances or Spot Instances, but not both in the same request. Furthermore, when you use RunInstances to launch Spot Instances, your Spot Instance request is limited to one instance type and one Availability Zone. This targets a single Spot capacity pool (a set of unused instances with the same instance type and Availability Zone). If the Spot capacity pool does not have sufficient Spot Instance capacity for your request, the RunInstances call fails.

Instead of using RunInstances to launch Spot Instances, we recommend that you rather use the CreateFleet API with the type parameter set to instant for the following benefits:
- Launch On-Demand Instances and Spot Instances in one request. An EC2 Fleet can launch On- Demand Instances, Spot Instances, or both. The request for Spot Instances is fulfilled if there is available capacity and the maximum price per hour for your request exceeds the Spot price.
- Increase the availability of Spot Instances. By using an EC2 Fleet of type instant, you can launch Spot Instances following Spot best practices with the resulting benefits:
- Spot best practice: Be flexible about instance types and Availability Zones.
Benefit: By specifying several instance types and Availability Zones, you increase the number of Spot capacity pools. This gives the Spot service a better chance of finding and allocating your desired Spot compute capacity. A good rule of thumb is to be flexible across at least 10 instance types for each workload and make sure that all Availability Zones are configured for use in your VPC.
- Spot best practice: Use the price-capacity-optimized allocation strategy.
Benefit: The price-capacity-optimized allocation strategy identifies instances from the most-available Spot capacity pools, and then automatically provisions instances from the lowest priced of these pools. Because your Spot Instance capacity is sourced from pools with optimal capacity, this decreases the possibility that your Spot Instances will be interrupted when Amazon EC2 needs the capacity back.
- Get access to a wider set of capabilities. For workloads that need a launch-only API, and where you prefer to manage the lifecycle of your instance rather than let EC2 Fleet manage it for you, use the EC2 Fleet of type instant instead of the RunInstances API. EC2 Fleet provides a wider set of capabilities than RunInstances, as demonstrated in the following examples.
For all other workloads, you should use Amazon EC2 Auto Scaling because it supplies a more comprehensive feature set for a wide variety of workloads, like ELB-backed applications, containerized workloads, and queue processing jobs.
You can use EC2 Fleet of type instant to launch instances into Capacity Blocks. For more information, see Tutorial: Configure your EC2 Fleet to launch instances into Capacity Blocks.
AWS services like Amazon EC2 Auto Scaling and Amazon EMR use EC2 Fleet of type instant to launch EC2 instances.

#### Prerequisites for EC2 Fleet of type instant For the prerequisites for creating an EC2 Fleet, see EC2 Fleet prerequisites.
#### How instant EC2 Fleet works When working with an EC2 Fleet of type instant, the sequence of events is as follows:
1. Configure: Configure the CreateFleet request type as instant. For more information, see Create an EC2 Fleet. Note that after you make the API call, you can't modify it.
2. Request: When you make the API call, Amazon EC2 places a synchronous one-time request for your desired capacity.
3. Response: The API response lists the instances that launched, along with errors for those instances that could not be launched.
4. Describe: You can describe your EC2 Fleet, list the instances associated with your EC2 Fleet, and view the history of your EC2 Fleet.
5. Terminate instances: You can terminate the instances at any time.
6. Delete fleet request: The fleet request can be deleted either manually or automatically:
- Manual: You can delete the fleet request after your instances launch.
Note that a deleted instant fleet with running instances is not supported. When you delete an instant fleet, Amazon EC2 automatically terminates all its instances. For fleets with more than 1000 instances, the deletion request might fail. If your fleet has more than 1000 instances, first terminate most of the instances manually, leaving 1000 or fewer. Then delete the fleet, and the remaining instances will be terminated automatically.
- Automatic: Amazon EC2 deletes the fleet request some time after either:
- All the instances are terminated.
- The fleet fails to launch any instances.
#### Examples The following examples show how to use EC2 Fleet of type instant for different use cases. For more information about using the EC2 CreateFleet API parameters, see CreateFleet in the Amazon EC2 API Reference.
### Examples
- Example 1: Launch Spot Instances with the capacity-optimized allocation strategy

- Example 2: Launch a single Spot Instance with the capacity-optimized allocation strategy
- Example 3: Launch Spot Instances using instance weighting
- Example 4: Launch Spot Instances within single Availability Zone
- Example 5: Launch Spot Instances of single instance type within single Availability zone
- Example 6: Launch Spot Instances only if minimum target capacity can be launched
- Example 7: Launch Spot Instances only if minimum target capacity can be launched of same Instance Type in a single Availability Zone
- Example 8: Launch instances with multiple Launch Templates
- Example 9: Launch Spot Instance with a base of On-Demand Instances
- Example 10: Launch Spot Instances using capacity-optimized allocation strategy with a base of On-Demand Instances using Capacity Reservations and the prioritized allocation strategy
- Example 11: Launch Spot Instances using capacity-optimized-prioritized allocation strategy
- Example 12: Specify a Systems Manager parameter instead of an AMI ID
##### Example 1: Launch Spot Instances with the capacity-optimized allocation strategy The following example specifies the parameters required in an EC2 Fleet of type instant: a launch template, target capacity, default purchasing option, and launch template overrides.
- The launch template is identified by its launch template name and version number.
- The 12 launch template overrides specify 4 different instance types and 3 different subnets, each in a separate Availability Zone. Each instance type and subnet combination defines a Spot capacity pool, resulting in 12 Spot capacity pools.
- The target capacity for the fleet is 20 instances.
- The default purchasing option is spot, which results in the fleet attempting to launch 20 Spot Instances into the Spot capacity pool with optimal capacity for the number of instances that are launching.
{ "SpotOptions": { "AllocationStrategy": "capacity-optimized"
    }, "LaunchTemplateConfigs": [ { "LaunchTemplateSpecification":{

            "LaunchTemplateName":"ec2-fleet-lt1", "Version":"$Latest"
         }, "Overrides":[ { "InstanceType":"c5.large", "SubnetId":"subnet-fae8c380"
            }, { "InstanceType":"c5.large", "SubnetId":"subnet-e7188bab"
            }, { "InstanceType":"c5.large", "SubnetId":"subnet-49e41922"
            }, { "InstanceType":"c5d.large", "SubnetId":"subnet-fae8c380"
            }, { "InstanceType":"c5d.large", "SubnetId":"subnet-e7188bab"
            }, { "InstanceType":"c5d.large", "SubnetId":"subnet-49e41922"
            }, { "InstanceType":"m5.large", "SubnetId":"subnet-fae8c380"
            }, { "InstanceType":"m5.large", "SubnetId":"subnet-e7188bab"
            }, { "InstanceType":"m5.large", "SubnetId":"subnet-49e41922"
            }, { "InstanceType":"m5d.large", "SubnetId":"subnet-fae8c380"
            },

            { "InstanceType":"m5d.large", "SubnetId":"subnet-e7188bab"
            }, { "InstanceType":"m5d.large", "SubnetId":"subnet-49e41922"
            } ]
      } ], "TargetCapacitySpecification": { "TotalTargetCapacity": 20, "DefaultTargetCapacityType": "spot"
    }, "Type": "instant"
}
##### Example 2: Launch a single Spot Instance with the capacity-optimized allocation strategy You can optimally launch one Spot Instance at a time by making multiple EC2 Fleet API calls of type instant, by setting the TotalTargetCapacity to 1.
The following example specifies the parameters required in an EC2 Fleet of type instant: a launch template, target capacity, default purchasing option, and launch template overrides. The launch template is identified by its launch template name and version number. The 12 launch template overrides have 4 different instance types and 3 different subnets, each in a separate Availability Zone. The target capacity for the fleet is 1 instance, and the default purchasing option is spot, which results in the fleet attempting to launch a Spot Instance from one of the 12 Spot capacity pools based on the capacity-optimized allocation strategy, to launch a Spot Instance from the most-available capacity pool.
{ "SpotOptions": { "AllocationStrategy": "capacity-optimized"
    }, "LaunchTemplateConfigs": [ { "LaunchTemplateSpecification":{ "LaunchTemplateName":"ec2-fleet-lt1", "Version":"$Latest"
         },

         "Overrides":[ { "InstanceType":"c5.large", "SubnetId":"subnet-fae8c380"
            }, { "InstanceType":"c5.large", "SubnetId":"subnet-e7188bab"
            }, { "InstanceType":"c5.large", "SubnetId":"subnet-49e41922"
            }, { "InstanceType":"c5d.large", "SubnetId":"subnet-fae8c380"
            }, { "InstanceType":"c5d.large", "SubnetId":"subnet-e7188bab"
            }, { "InstanceType":"c5d.large", "SubnetId":"subnet-49e41922"
            }, { "InstanceType":"m5.large", "SubnetId":"subnet-fae8c380"
            }, { "InstanceType":"m5.large", "SubnetId":"subnet-e7188bab"
            }, { "InstanceType":"m5.large", "SubnetId":"subnet-49e41922"
            }, { "InstanceType":"m5d.large", "SubnetId":"subnet-fae8c380"
            }, { "InstanceType":"m5d.large", "SubnetId":"subnet-e7188bab"

            }, { "InstanceType":"m5d.large", "SubnetId":"subnet-49e41922"
            } ]
      } ], "TargetCapacitySpecification": { "TotalTargetCapacity": 1, "DefaultTargetCapacityType": "spot"
    }, "Type": "instant"
}
##### Example 3: Launch Spot Instances using instance weighting The following examples use instance weighting, which means that the price is per unit hour instead of per instance hour. Each launch configuration lists a different instance type and a different weight based on how many units of the workload can run on the instance assuming a unit of the workload requires a 15 GB of memory and 4 vCPUs. For example an m5.xlarge (4 vCPUs and 16 GB of memory) can run one unit and is weighted 1, m5.2xlarge (8 vCPUs and 32 GB of memory) can run 2 units and is weighted 2, and so on. The total target capacity is set to 40 units. The default purchasing option is spot, and the allocation strategy is capacity-optimized, which results in either 40 m5.xlarge (40 divided by 1), 20 m5.2xlarge (40 divided by 2), 10 m5.4xlarge (40 divided by 4), 5 m5.8xlarge (40 divided by 8), or a mix of the instance types with weights adding up to the desired capacity based on the capacity-optimized allocation strategy.
For more information, see Use instance weighting to manage cost and performance of your EC2 Fleet or Spot Fleet.
{ "SpotOptions":{ "AllocationStrategy":"capacity-optimized"
   }, "LaunchTemplateConfigs":[ { "LaunchTemplateSpecification":{ "LaunchTemplateName":"ec2-fleet-lt1", "Version":"$Latest"
         }, "Overrides":[

            { "InstanceType":"m5.xlarge", "SubnetId":"subnet-fae8c380", "WeightedCapacity":1 }, { "InstanceType":"m5.xlarge", "SubnetId":"subnet-e7188bab", "WeightedCapacity":1 }, { "InstanceType":"m5.xlarge", "SubnetId":"subnet-49e41922", "WeightedCapacity":1 }, { "InstanceType":"m5.2xlarge", "SubnetId":"subnet-fae8c380", "WeightedCapacity":2 }, { "InstanceType":"m5.2xlarge", "SubnetId":"subnet-e7188bab", "WeightedCapacity":2 }, { "InstanceType":"m5.2xlarge", "SubnetId":"subnet-49e41922", "WeightedCapacity":2 }, { "InstanceType":"m5.4xlarge", "SubnetId":"subnet-fae8c380", "WeightedCapacity":4 }, { "InstanceType":"m5.4xlarge", "SubnetId":"subnet-e7188bab", "WeightedCapacity":4 }, { "InstanceType":"m5.4xlarge", "SubnetId":"subnet-49e41922", "WeightedCapacity":4

            }, { "InstanceType":"m5.8xlarge", "SubnetId":"subnet-fae8c380", "WeightedCapacity":8 }, { "InstanceType":"m5.8xlarge", "SubnetId":"subnet-e7188bab", "WeightedCapacity":8 }, { "InstanceType":"m5.8xlarge", "SubnetId":"subnet-49e41922", "WeightedCapacity":8 } ]
      } ], "TargetCapacitySpecification":{ "TotalTargetCapacity":40, "DefaultTargetCapacityType":"spot"
   }, "Type":"instant"
}
##### Example 4: Launch Spot Instances within single Availability Zone You can configure a fleet to launch all instances in a single Availability Zone by setting the Spot options SingleAvailabilityZone to true.
The 12 launch template overrides have different instance types and subnets (each in a separate Availability Zone) but the same weighted capacity. The total target capacity is 20 instances, the default purchasing option is spot, and the Spot allocation strategy is capacity-optimized. The EC2 Fleet launches 20 Spot Instances all in a single AZ, from the Spot capacity pool(s) with optimal capacity using the launch specifications.
{ "SpotOptions": { "AllocationStrategy": "capacity-optimized", "SingleAvailabilityZone": true }, "LaunchTemplateConfigs": [

      { "LaunchTemplateSpecification":{ "LaunchTemplateName":"ec2-fleet-lt1", "Version":"$Latest"
         }, "Overrides":[ { "InstanceType":"c5.4xlarge", "SubnetId":"subnet-fae8c380"
            }, { "InstanceType":"c5.4xlarge", "SubnetId":"subnet-e7188bab"
            }, { "InstanceType":"c5.4xlarge", "SubnetId":"subnet-49e41922"
            }, { "InstanceType":"c5d.4xlarge", "SubnetId":"subnet-fae8c380"
            }, { "InstanceType":"c5d.4xlarge", "SubnetId":"subnet-e7188bab"
            }, { "InstanceType":"c5d.4xlarge", "SubnetId":"subnet-49e41922"
            }, { "InstanceType":"m5.4xlarge", "SubnetId":"subnet-fae8c380"
            }, { "InstanceType":"m5.4xlarge", "SubnetId":"subnet-e7188bab"
            }, { "InstanceType":"m5.4xlarge", "SubnetId":"subnet-49e41922"
            }, { "InstanceType":"m5d.4xlarge",

               "SubnetId":"subnet-fae8c380"
            }, { "InstanceType":"m5d.4xlarge", "SubnetId":"subnet-e7188bab"
            }, { "InstanceType":"m5d.4xlarge", "SubnetId":"subnet-49e41922"
            } ]
      } ], "TargetCapacitySpecification": { "TotalTargetCapacity": 20, "DefaultTargetCapacityType": "spot"
    }, "Type": "instant"
}
##### Example 5: Launch Spot Instances of single instance type within single Availability zone You can configure a fleet to launch all instances of the same instance type and in a single Availability Zone by setting the SpotOptions SingleInstanceType to true and SingleAvailabilityZone to true.
The 12 launch template overrides have different instance types and subnets (each in a separate Availability Zone) but the same weighted capacity. The total target capacity is 20 instances, the default purchasing option is spot, the Spot allocation strategy is capacity-optimized. The EC2 Fleet launches 20 Spot Instances of the same instance type all in a single AZ from the Spot Instance pool with optimal capacity using the launch specifications.
{ "SpotOptions": { "AllocationStrategy": "capacity-optimized", "SingleInstanceType": true, "SingleAvailabilityZone": true }, "LaunchTemplateConfigs": [ { "LaunchTemplateSpecification":{ "LaunchTemplateName":"ec2-fleet-lt1", "Version":"$Latest"

         }, "Overrides":[ { "InstanceType":"c5.4xlarge", "SubnetId":"subnet-fae8c380"
            }, { "InstanceType":"c5.4xlarge", "SubnetId":"subnet-e7188bab"
            }, { "InstanceType":"c5.4xlarge", "SubnetId":"subnet-49e41922"
            }, { "InstanceType":"c5d.4xlarge", "SubnetId":"subnet-fae8c380"
            }, { "InstanceType":"c5d.4xlarge", "SubnetId":"subnet-e7188bab"
            }, { "InstanceType":"c5d.4xlarge", "SubnetId":"subnet-49e41922"
            }, { "InstanceType":"m5.4xlarge", "SubnetId":"subnet-fae8c380"
            }, { "InstanceType":"m5.4xlarge", "SubnetId":"subnet-e7188bab"
            }, { "InstanceType":"m5.4xlarge", "SubnetId":"subnet-49e41922"
            }, { "InstanceType":"m5d.4xlarge", "SubnetId":"subnet-fae8c380"
            }, { "InstanceType":"m5d.4xlarge",

               "SubnetId":"subnet-e7188bab"
            }, { "InstanceType":"m5d.4xlarge", "SubnetId":"subnet-49e41922"
            } ]
      } ], "TargetCapacitySpecification": { "TotalTargetCapacity": 20, "DefaultTargetCapacityType": "spot"
    }, "Type": "instant"
}
##### Example 6: Launch Spot Instances only if minimum target capacity can be launched You can configure a fleet to launch instances only if the minimum target capacity can be launched by setting the Spot options MinTargetCapacity to the minimum target capacity you want to launch together.
When specifying MinTargetCapacity, you must specify at least one of these parameters:
SingleInstanceType or SingleAvailabilityZone. In this example, SingleInstanceType is specified, so that all 20 instances must use the same instance type.
The 12 launch template overrides have different instance types and subnets (each in a separate Availability Zone) but the same weighted capacity. The total target capacity and the minimum target capacity are both set to 20 instances, the default purchasing option is spot, and the Spot allocation strategy is capacity-optimized. The EC2 Fleet launches 20 Spot Instances from the Spot capacity pool with optimal capacity using the launch template overrides, only if it can launch all 20 instances at the same time.
{ "SpotOptions": { "AllocationStrategy": "capacity-optimized", "SingleInstanceType": true, "MinTargetCapacity": 20 }, "LaunchTemplateConfigs": [ { "LaunchTemplateSpecification":{

            "LaunchTemplateName":"ec2-fleet-lt1", "Version":"$Latest"
         }, "Overrides":[ { "InstanceType":"c5.4xlarge", "SubnetId":"subnet-fae8c380"
            }, { "InstanceType":"c5.4xlarge", "SubnetId":"subnet-e7188bab"
            }, { "InstanceType":"c5.4xlarge", "SubnetId":"subnet-49e41922"
            }, { "InstanceType":"c5d.4xlarge", "SubnetId":"subnet-fae8c380"
            }, { "InstanceType":"c5d.4xlarge", "SubnetId":"subnet-e7188bab"
            }, { "InstanceType":"c5d.4xlarge", "SubnetId":"subnet-49e41922"
            }, { "InstanceType":"m5.4xlarge", "SubnetId":"subnet-fae8c380"
            }, { "InstanceType":"m5.4xlarge", "SubnetId":"subnet-e7188bab"
            }, { "InstanceType":"m5.4xlarge", "SubnetId":"subnet-49e41922"
            }, { "InstanceType":"m5d.4xlarge", "SubnetId":"subnet-fae8c380"
            },

            { "InstanceType":"m5d.4xlarge", "SubnetId":"subnet-e7188bab"
            }, { "InstanceType":"m5d.4xlarge", "SubnetId":"subnet-49e41922"
            } ]
      } ], "TargetCapacitySpecification": { "TotalTargetCapacity": 20, "DefaultTargetCapacityType": "spot"
    }, "Type": "instant"
}
##### Example 7: Launch Spot Instances only if minimum target capacity can be launched of same Instance Type in a single Availability Zone Instance Type in a single Availability Zone You can configure a fleet to launch instances only if the minimum target capacity can be launched with a single instance type in a single Availability Zone by setting the Spot options MinTargetCapacity to the minimum target capacity you want to launch together along with SingleInstanceType and SingleAvailabilityZone options.
The 12 launch specifications which override the launch template, have different instance types and subnets (each in a separate Availability Zone) but the same weighted capacity. The total target capacity and the minimum target capacity are both set to 20 instances, the default purchasing option is spot, the Spot allocation strategy is capacity-optimized, the SingleInstanceType is true and SingleAvailabilityZone is true. The EC2 Fleet launches 20 Spot Instances of the same Instance type all in a single AZ from the Spot capacity pool with optimal capacity using the launch specifications, only if it can launch all 20 instances at the same time.
{ "SpotOptions": { "AllocationStrategy": "capacity-optimized", "SingleInstanceType": true, "SingleAvailabilityZone": true, "MinTargetCapacity": 20 }, "LaunchTemplateConfigs": [

      { "LaunchTemplateSpecification":{ "LaunchTemplateName":"ec2-fleet-lt1", "Version":"$Latest"
         }, "Overrides":[ { "InstanceType":"c5.4xlarge", "SubnetId":"subnet-fae8c380"
            }, { "InstanceType":"c5.4xlarge", "SubnetId":"subnet-e7188bab"
            }, { "InstanceType":"c5.4xlarge", "SubnetId":"subnet-49e41922"
            }, { "InstanceType":"c5d.4xlarge", "SubnetId":"subnet-fae8c380"
            }, { "InstanceType":"c5d.4xlarge", "SubnetId":"subnet-e7188bab"
            }, { "InstanceType":"c5d.4xlarge", "SubnetId":"subnet-49e41922"
            }, { "InstanceType":"m5.4xlarge", "SubnetId":"subnet-fae8c380"
            }, { "InstanceType":"m5.4xlarge", "SubnetId":"subnet-e7188bab"
            }, { "InstanceType":"m5.4xlarge", "SubnetId":"subnet-49e41922"
            }, { "InstanceType":"m5d.4xlarge",

               "SubnetId":"subnet-fae8c380"
            }, { "InstanceType":"m5d.4xlarge", "SubnetId":"subnet-e7188bab"
            }, { "InstanceType":"m5d.4xlarge", "SubnetId":"subnet-49e41922"
            } ]
      } ], "TargetCapacitySpecification": { "TotalTargetCapacity": 20, "DefaultTargetCapacityType": "spot"
    }, "Type": "instant"
}
##### Example 8: Launch instances with multiple Launch Templates You can configure a fleet to launch instances with different launch specifications for different instance types or a group of instance types, by specifying multiple launch templates. In this example we want have different EBS volume sizes for different instance types and we have that configured in the launch templates ec2-fleet-lt-4xl, ec2-fleet-lt-9xl and ec2-fleet-lt-18xl.
In this example, we are using 3 different launch templates for the 3 instance types based on their size. The launch specification overrides on all the launch templates use instance weights based on the vCPUs on the instance type. The total target capacity is 144 units, the default purchasing option is spot, and the Spot allocation strategy is capacity-optimized. The EC2 Fleet can either launch 9 c5n.4xlarge (144 divided by 16) using the launch template ec2-fleet-4xl or 4 c5n.9xlarge (144 divided by 36) using the launch template ec2-fleet-9xl, or 2 c5n.18xlarge (144 divided by 72) using the launch template ec2-fleet-18xl, or a mix of the instance types with weights adding up to the desired capacity based on the capacity-optimized allocation strategy.
{ "SpotOptions": { "AllocationStrategy": "capacity-optimized"
    }, "LaunchTemplateConfigs": [ {

         "LaunchTemplateSpecification":{ "LaunchTemplateName":"ec2-fleet-lt-18xl", "Version":"$Latest"
         }, "Overrides":[ { "InstanceType":"c5n.18xlarge", "SubnetId":"subnet-fae8c380", "WeightedCapacity":72 }, { "InstanceType":"c5n.18xlarge", "SubnetId":"subnet-e7188bab", "WeightedCapacity":72 }, { "InstanceType":"c5n.18xlarge", "SubnetId":"subnet-49e41922", "WeightedCapacity":72 } ]
      }, { "LaunchTemplateSpecification":{ "LaunchTemplateName":"ec2-fleet-lt-9xl", "Version":"$Latest"
         }, "Overrides":[ { "InstanceType":"c5n.9xlarge", "SubnetId":"subnet-fae8c380", "WeightedCapacity":36 }, { "InstanceType":"c5n.9xlarge", "SubnetId":"subnet-e7188bab", "WeightedCapacity":36 }, { "InstanceType":"c5n.9xlarge", "SubnetId":"subnet-49e41922", "WeightedCapacity":36 } ]

      }, { "LaunchTemplateSpecification":{ "LaunchTemplateName":"ec2-fleet-lt-4xl", "Version":"$Latest"
         }, "Overrides":[ { "InstanceType":"c5n.4xlarge", "SubnetId":"subnet-fae8c380", "WeightedCapacity":16 }, { "InstanceType":"c5n.4xlarge", "SubnetId":"subnet-e7188bab", "WeightedCapacity":16 }, { "InstanceType":"c5n.4xlarge", "SubnetId":"subnet-49e41922", "WeightedCapacity":16 } ]
      } ], "TargetCapacitySpecification": { "TotalTargetCapacity": 144, "DefaultTargetCapacityType": "spot"
    }, "Type": "instant"
}
##### Example 9: Launch Spot Instance with a base of On-Demand Instances The following example specifies the total target capacity of 20 instances for the fleet, and a target capacity of 5 On-Demand Instances. The default purchasing option is spot. The fleet launches 5 On-Demand Instance as specified, but needs to launch 15 more instances to fulfill the total target capacity. The purchasing option for the difference is calculated as TotalTargetCapacity – OnDemandTargetCapacity = DefaultTargetCapacityType, which results in the fleet launching 15 Spot Instances form one of the 12 Spot capacity pools based on the capacity-optimized allocation strategy.

{ "SpotOptions": { "AllocationStrategy": "capacity-optimized"
    }, "LaunchTemplateConfigs": [ { "LaunchTemplateSpecification":{ "LaunchTemplateName":"ec2-fleet-lt1", "Version":"$Latest"
         }, "Overrides":[ { "InstanceType":"c5.large", "SubnetId":"subnet-fae8c380"
            }, { "InstanceType":"c5.large", "SubnetId":"subnet-e7188bab"
            }, { "InstanceType":"c5.large", "SubnetId":"subnet-49e41922"
            }, { "InstanceType":"c5d.large", "SubnetId":"subnet-fae8c380"
            }, { "InstanceType":"c5d.large", "SubnetId":"subnet-e7188bab"
            }, { "InstanceType":"c5d.large", "SubnetId":"subnet-49e41922"
            }, { "InstanceType":"m5.large", "SubnetId":"subnet-fae8c380"
            }, { "InstanceType":"m5.large", "SubnetId":"subnet-e7188bab"
            },

            { "InstanceType":"m5.large", "SubnetId":"subnet-49e41922"
            }, { "InstanceType":"m5d.large", "SubnetId":"subnet-fae8c380"
            }, { "InstanceType":"m5d.large", "SubnetId":"subnet-e7188bab"
            }, { "InstanceType":"m5d.large", "SubnetId":"subnet-49e41922"
            } ]
      } ], "TargetCapacitySpecification": { "TotalTargetCapacity": 20, "OnDemandTargetCapacity": 5, "DefaultTargetCapacityType": "spot"
    }, "Type": "instant"
}
##### Example 10: Launch Spot Instances using capacity-optimized allocation strategy with a base of On-Demand Instances using Capacity Reservations and the prioritized allocation strategy On-Demand Instances using Capacity Reservations and the prioritized allocation strategy You can configure a fleet to use On-Demand Capacity Reservations first when launching a base of On-Demand Instances with the default target capacity type as spot by setting the usage strategy for Capacity Reservations to use-capacity-reservations-first. And if multiple instance pools have unused Capacity Reservations, the chosen On-Demand allocation strategy is applied. In this example, the On-Demand allocation strategy is prioritized.
In this example, there are 6 available unused Capacity Reservations. This is less than the fleet's target On-Demand capacity of 10 On-Demand Instances.
The account has the following 6 unused Capacity Reservations in 2 pools. The number of Capacity Reservations in each pool is indicated by AvailableInstanceCount.

{ "CapacityReservationId": "cr-111", "InstanceType": "m5.large", "InstancePlatform": "Linux/UNIX", "AvailabilityZone": "us-east-1a", "AvailableInstanceCount": 3, "InstanceMatchCriteria": "open", "State": "active"
}

{ "CapacityReservationId": "cr-222", "InstanceType": "c5.large", "InstancePlatform": "Linux/UNIX", "AvailabilityZone": "us-east-1a", "AvailableInstanceCount": 3, "InstanceMatchCriteria": "open", "State": "active"
} The following fleet configuration shows only the pertinent configurations for this example. The On-Demand allocation strategy is prioritized, and the usage strategy for Capacity Reservations is use-capacity-reservations-first. The Spot allocation strategy is capacity-optimized. The total target capacity is 20, the On-Demand target capacity is 10, and the default target capacity type is spot.
{ "SpotOptions": { "AllocationStrategy": "capacity-optimized"
    }, "OnDemandOptions":{ "CapacityReservationOptions": { "UsageStrategy": "use-capacity-reservations-first"
       }, "AllocationStrategy":"prioritized"
    }, "LaunchTemplateConfigs": [ { "LaunchTemplateSpecification":{ "LaunchTemplateName":"ec2-fleet-lt1", "Version":"$Latest"
         }, "Overrides":[

            { "InstanceType":"c5.large", "SubnetId":"subnet-fae8c380", "Priority": 1.0 }, { "InstanceType":"c5.large", "SubnetId":"subnet-e7188bab", "Priority": 2.0 }, { "InstanceType":"c5.large", "SubnetId":"subnet-49e41922", "Priority": 3.0 }, { "InstanceType":"c5d.large", "SubnetId":"subnet-fae8c380", "Priority": 4.0 }, { "InstanceType":"c5d.large", "SubnetId":"subnet-e7188bab", "Priority": 5.0 }, { "InstanceType":"c5d.large", "SubnetId":"subnet-49e41922", "Priority": 6.0 }, { "InstanceType":"m5.large", "SubnetId":"subnet-fae8c380", "Priority": 7.0 }, { "InstanceType":"m5.large", "SubnetId":"subnet-e7188bab", "Priority": 8.0 }, { "InstanceType":"m5.large", "SubnetId":"subnet-49e41922", "Priority": 9.0

            }, { "InstanceType":"m5d.large", "SubnetId":"subnet-fae8c380", "Priority": 10.0 }, { "InstanceType":"m5d.large", "SubnetId":"subnet-e7188bab", "Priority": 11.0 }, { "InstanceType":"m5d.large", "SubnetId":"subnet-49e41922", "Priority": 12.0 } ]
      } ], "TargetCapacitySpecification": { "TotalTargetCapacity": 20, "OnDemandTargetCapacity": 10, "DefaultTargetCapacityType": "spot"
    }, "Type": "instant"
} After you create the instant fleet using the preceding configuration, the following 20 instances are launched to meet the target capacity:
- 7 c5.large On-Demand Instances in us-east-1a – c5.large in us-east-1a is prioritized first, and there are 3 available unused c5.large Capacity Reservations. The Capacity Reservations are used first to launch 3 On-Demand Instances plus 4 additional On-Demand Instances are launched according to the On-Demand allocation strategy, which is prioritized in this example.
- 3 m5.large On-Demand Instances in us-east-1a – m5.large in us-east-1a is prioritized second, and there are 3 available unused c3.large Capacity Reservations.
- 10 Spot Instances from one of the 12 Spot capacity pools that has the optimal capacity according to the capacity-optimized allocation strategy.

After the fleet is launched, you can run describe-capacity-reservations to see how many unused Capacity Reservations are remaining. In this example, you should see the following response, which shows that all of the c5.large and m5.large Capacity Reservations were used.
{ "CapacityReservationId": "cr-111", "InstanceType": "m5.large", "AvailableInstanceCount": 0 }

{ "CapacityReservationId": "cr-222", "InstanceType": "c5.large", "AvailableInstanceCount": 0 }
##### Example 11: Launch Spot Instances using capacity-optimized-prioritized allocation strategy The following example specifies the parameters required in an EC2 Fleet of type instant: a launch template, target capacity, default purchasing option, and launch template overrides. The launch template is identified by its launch template name and version number. The 12 launch specifications which override the launch template have 4 different instance types with a priority assigned, and 3 different subnets, each in a separate Availability Zone. The target capacity for the fleet is 20 instances, and the default purchasing option is spot, which results in the fleet attempting to launch 20 Spot Instances from one of the 12 Spot capacity pools based on the capacity-optimized-prioritized allocation strategy, which implements priorities on a best-effort basis, but optimizes for capacity first.
{ "SpotOptions": { "AllocationStrategy": "capacity-optimized-prioritized"
    }, "LaunchTemplateConfigs": [ { "LaunchTemplateSpecification":{ "LaunchTemplateName":"ec2-fleet-lt1", "Version":"$Latest"
         }, "Overrides":[ { "InstanceType":"c5.large",

               "SubnetId":"subnet-fae8c380", "Priority": 1.0 }, { "InstanceType":"c5.large", "SubnetId":"subnet-e7188bab", "Priority": 1.0 }, { "InstanceType":"c5.large", "SubnetId":"subnet-49e41922", "Priority": 1.0 }, { "InstanceType":"c5d.large", "SubnetId":"subnet-fae8c380", "Priority": 2.0 }, { "InstanceType":"c5d.large", "SubnetId":"subnet-e7188bab", "Priority": 2.0 }, { "InstanceType":"c5d.large", "SubnetId":"subnet-49e41922", "Priority": 2.0 }, { "InstanceType":"m5.large", "SubnetId":"subnet-fae8c380", "Priority": 3.0 }, { "InstanceType":"m5.large", "SubnetId":"subnet-e7188bab", "Priority": 3.0 }, { "InstanceType":"m5.large", "SubnetId":"subnet-49e41922", "Priority": 3.0 }, {

               "InstanceType":"m5d.large", "SubnetId":"subnet-fae8c380", "Priority": 4.0 }, { "InstanceType":"m5d.large", "SubnetId":"subnet-e7188bab", "Priority": 4.0 }, { "InstanceType":"m5d.large", "SubnetId":"subnet-49e41922", "Priority": 4.0 } ]
      } ], "TargetCapacitySpecification": { "TotalTargetCapacity": 20, "DefaultTargetCapacityType": "spot"
    }, "Type": "instant"
}
##### Example 12: Specify a Systems Manager parameter instead of an AMI ID The following example uses a launch template to specify the configuration for the instances in the fleet. In this example, for ImageId, instead of specifying an AMI ID, the AMI is referenced with a System Manager parameter. On instance launch, the Systems Manager parameter will resolve to an AMI ID.
In this example, the Systems Manager parameter is specified in a valid format: resolve:ssm:golden-ami. There are other valid formats for the Systems Manager parameter.
For more information, see Use a Systems Manager parameter instead of an AMI ID.
Note The fleet type must be of type instant. Other fleet types do not support specifying a System Manager parameter instead of an AMI ID.
{

    "LaunchTemplateData": { "ImageId": "resolve:ssm:golden-ami", "InstanceType": "m5.4xlarge", "TagSpecifications": [{ "ResourceType": "instance", "Tags": [{ "Key": "Name", "Value": "webserver"
            }]
        }]
    } }
## Set a spending limit for your EC2 Fleet or Spot Fleet You can set a limit on how much you're willing to spend per hour on your EC2 Fleet or Spot Fleet.
When your spending limit is reached, the fleet stops launching instances, even if the target capacity hasn't been reached.
There are separate spending limits for On-Demand Instances and Spot Instances.
To configure a spending limit for On-Demand Instances and Spot Instances in your EC2 Fleet Use the create-fleet command and the following parameters:
- For On-Demand Instances: In the OnDemandOptions structure, specify your spending limit in the MaxTotalPrice field.
- For Spot Instances: In the SpotOptions structure, specify your spending limit in the MaxTotalPrice field.
To configure a spending limit for On-Demand Instances and Spot Instances in your Spot Fleet You can use the Amazon EC2 console or the AWS CLI to configure your spending limit.
(Console) When creating the Spot Fleet, select the Set maximum cost for Spot Instances checkbox, and then enter a value for Set your max cost (per hour). For more information, see step 6.e. in Create a Spot Fleet request using defined parameters.
(AWS CLI) Use the request-spot-fleet command and the following parameters:
- For On-Demand Instances: Specify your spending limit in the OnDemandMaxTotalPrice field.

- For Spot Instances: Specify your spending limit in the SpotMaxTotalPrice field.
Examples The following examples show two different scenarios. In the first example, the fleet stops launching On-Demand Instances when it has met the target capacity set for On-Demand Instances (OnDemandTargetCapacity). In the second example, the fleet stops launching On-Demand Instances when it has reached the maximum amount you're willing to pay per hour for On-Demand Instances (MaxTotalPrice).
Example: Stop launching On-Demand Instances when target capacity is reached Given a request for m4.large On-Demand Instances, where:
- On-Demand Price: $0.10 per hour
- OnDemandTargetCapacity: 10
- MaxTotalPrice: $1.50 The fleet launches 10 On-Demand Instances because the total of $1.00 (10 instances x $0.10) does not exceed the MaxTotalPrice of $1.50 for On-Demand Instances.
Example: Stop launching On-Demand Instances when maximum total price is reached Given a request for m4.large On-Demand Instances, where:
- On-Demand Price: $0.10 per hour
- OnDemandTargetCapacity: 10
- MaxTotalPrice: $0.80 If the fleet launches the On-Demand target capacity (10 On-Demand Instances), the total cost per hour would be $1.00. This is more than the amount ($0.80) specified for MaxTotalPrice for On- Demand Instances. To prevent spending more than you're willing to pay, the fleet launches only 8 On-Demand Instances (below the On-Demand target capacity) because launching more would exceed the MaxTotalPrice for On-Demand Instances.

### Burstable performance instances If you launch your Spot Instances using a burstable performance instance type, and if you plan to use your burstable performance Spot Instances immediately and for a short duration, with no idle time for accruing CPU credits, we recommend that you launch them in Standard mode to avoid paying higher costs. If you launch burstable performance Spot Instances in Unlimited mode and burst CPU immediately, you'll spend surplus credits for bursting. If you use the instance for a short duration, the instance doesn't have time to accrue CPU credits to pay down the surplus credits, and you are charged for the surplus credits when you terminate the instance.
Unlimited mode is suitable for burstable performance Spot Instances only if the instance runs long enough to accrue CPU credits for bursting. Otherwise, paying for surplus credits makes burstable performance Spot Instances more expensive than using other instances. For more information, see When to use unlimited mode versus fixed CPU.
Launch credits are meant to provide a productive initial launch experience for T2 instances by providing sufficient compute resources to configure the instance. Repeated launches of T2 instances to access new launch credits is not permitted. If you require sustained CPU, you can earn credits (by idling over some period), use Unlimited mode for T2 Spot Instances, or use an instance type with dedicated CPU.
## Specify attributes for instance type selection for EC2 Fleet or Spot Fleet When you create an EC2 Fleet or Spot Fleet, you must specify one or more instance types for configuring the On-Demand Instances and Spot Instances in the fleet. As an alternative to manually specifying the instance types, you can specify the attributes that an instance must have, and Amazon EC2 will identify all the instance types with those attributes. This is known as attribute-based instance type selection. For example, you can specify the minimum and maximum number of vCPUs required for your instances, and the fleet will launch the instances using any available instance types that meet those vCPU requirements.
Attribute-based instance type selection is ideal for workloads and frameworks that can be flexible about what instance types they use, such as when running containers or web fleets, processing big data, and implementing continuous integration and deployment (CI/CD) tooling.
Benefits Attribute-based instance type selection has the following benefits:

- Easily use the right instance types – With so many instance types available, finding the right instance types for your workload can be time consuming. When you specify instance attributes, the instance types will automatically have the required attributes for your workload.
- Simplified configuration – To manually specify multiple instance types for a fleet, you must create a separate launch template override for each instance type. But with attribute-based instance type selection, to provide multiple instance types, you need only specify the instance attributes in the launch template or in a launch template override.
- Automatic use of new instance types – When you specify instance attributes rather than instance types, your fleet can use newer generation instance types as they're released, "future proofing" the fleet's configuration.
- Instance type flexibility – When you specify instance attributes rather than instance types, the fleet can select from a wide range of instance types for launching Spot Instances, which adheres to the Spot best practice of instance type flexibility.
Topics
- How attribute-based instance type selection works
- Price protection
- Performance protection
- Considerations
- Create an EC2 Fleet with attribute-based instance type selection
- Create a Spot Fleet with attribute-based instance type selection
- Examples of EC2 Fleet configurations that are valid and not valid
- Examples of Spot Fleet configurations that are valid and not valid
- Preview instance types with specified attributes
### How attribute-based instance type selection works To use attribute-based instance type selection in your fleet configuration, you replace the list of instance types with a list of instance attributes that your instances require. EC2 Fleet or Spot Fleet will launch instances on any available instance types that have the specified instance attributes.
Topics
- Types of instance attributes
- Where to configure attribute-based instance type selection

- How EC2 Fleet or Spot Fleet uses attribute-based instance type selection when provisioning a fleet
#### Types of instance attributes There are several instance attributes that you can specify to express your compute requirements, such as:
- vCPU count – The minimum and maximum number of vCPUs per instance.
- Memory – The minimum and maximum GiBs of memory per instance.
- Local storage – Whether to use EBS or instance store volumes for local storage.
- Burstable performance – Whether to use the T instance family, including T4g, T3a, T3, and T2 types.
For a description of each attribute and the default values, see InstanceRequirements in the Amazon EC2 API Reference.
#### Where to configure attribute-based instance type selection Depending on whether you use the console or the AWS CLI, you can specify the instance attributes for attribute-based instance type selection as follows:
In the console, you can specify the instance attributes in the following fleet configuration components:
- In a launch template, and then reference the launch template in the fleet request
- (Spot Fleet only) In the fleet request In the AWS CLI, you can specify the instance attributes in one or all of the following fleet configuration components:
- In a launch template, and then reference the launch template in the fleet request
- In a launch template override If you want a mix of instances that use different AMIs, you can specify instance attributes in multiple launch template overrides. For example, different instance types can use x86 and Arm- based processors.

- (Spot Fleet only) In a launch specification
#### How EC2 Fleet or Spot Fleet uses attribute-based instance type selection when provisioning a fleet fleet EC2 Fleet or Spot Fleet provisions a fleet in the following way:
- It identifies the instance types that have the specified attributes.
- It uses price protection to determine which instance types to exclude.
- It determines the capacity pools from which it will consider launching the instances based on the AWS Regions or Availability Zones that have matching instance types.
- It applies the specified allocation strategy to determine from which capacity pools to launch the instances.
Note that attribute-based instance type selection does not pick the capacity pools from which to provision the fleet; that's the job of the allocation strategies.
If you specify an allocation strategy, the fleet will launch instances according to the specified allocation strategy.
- For Spot Instances, attribute-based instance type selection supports the price capacity optimized, capacity optimized, and lowest price allocation strategies. Note that we don't recommend the lowest price Spot allocation strategy because it has the highest risk of interruption for your Spot Instances.
- For On-Demand Instances, attribute-based instance type selection supports the lowest price allocation strategy.
- If there is no capacity for the instance types with the specified instance attributes, no instances can be launched, and the fleet returns an error.
### Price protection Price protection is a feature that prevents your EC2 Fleet or Spot Fleet from using instance types that you would consider too expensive even if they happen to fit the attributes that you specified.
To use price protection, you set a price threshold. Then, when Amazon EC2 selects instance types with your attributes, it excludes instance types priced above your threshold.
The way that Amazon EC2 calculates the price threshold is as follows:

- Amazon EC2 first identifies the lowest priced instance type from those that match your attributes.
- Amazon EC2 then takes the value (expressed as a percentage) that you specified for the price protection parameter and multiplies it with the price of the identified instance type. The result is the price that is used as the price threshold.
There are separate price thresholds for On-Demand Instances and Spot Instances.
When you create a fleet with attribute-based instance type selection, price protection is enabled by default. You can keep the default values, or you can specify your own.
You can also turn off price protection. To indicate no price protection threshold, specify a high percentage value, such as 999999.
Topics
- How the lowest priced instance type is identified
- On-Demand Instance price protection
- Spot Instance price protection
- Specify the price protection threshold
#### How the lowest priced instance type is identified Amazon EC2 determines the price to base the price threshold on by identifying the instance type with the lowest price from those that match your specified attributes. It does this in the following way:
- It first looks at the current generation C, M, or R instance types that match your attributes. If it finds any matches, it identifies the lowest priced instance type.
- If there is no match, it then looks at any current generation instance types that match your attributes. If it finds any matches, it identifies the lowest priced instance type.
- If there is no match, it then looks at any previous generation instance types that match your attributes, and identifies the lowest priced instance type.
#### On-Demand Instance price protection The price protection threshold for On-Demand instance types is calculated as a percentage higher than the identified lowest priced On-Demand instance type

(OnDemandMaxPricePercentageOverLowestPrice). You specify the percentage higher that you're willing to pay. If you don't specify this parameter, then a default value of 20 is used to calculate a price protection threshold of 20% higher than the identified price.
For example, if the identified On-Demand instance price is 0.4271, and you specify 25, then the price threshold is 25% more than 0.4271. It is calculated as follows: 0.4271 * 1.25 = 0.533875. The calculated price is the maximum you're willing to pay for On-Demand Instances, and, in this example, Amazon EC2 will exclude any On-Demand instance types that cost more than 0.533875.
#### Spot Instance price protection By default, Amazon EC2 will automatically apply optimal Spot Instance price protection to consistently select from a wide range of instance types. You can also manually set the price protection yourself. However, letting Amazon EC2 do it for you can improve the likelihood that your Spot capacity is fulfilled.
You can manually specify the price protection using one of the following options. If you manually set the price protection, we recommend using the first option.
- A percentage of the identified lowest priced On-Demand instance type [MaxSpotPriceAsPercentageOfOptimalOnDemandPrice]
For example, if the identified On-Demand instance type price is 0.4271, and you specify 60, then the price threshold is 60% of 0.4271. It is calculated as follows: 0.4271 * 0.60 = 0.25626. The calculated price is the maximum you're willing to pay for Spot Instances, and, in this example, Amazon EC2 will exclude any Spot instance types that cost more than 0.25626.
- A percentage higher than the identified lowest priced Spot instance type [SpotMaxPricePercentageOverLowestPrice]
For example, if the identified Spot instance type price is 0.1808, and you specify 25, then the price threshold is 25% more than 0.1808. It is calculated as follows: 0.1808 * 1.25 = 0.226. The calculated price is the maximum you're willing to pay for Spot Instances, and, in this example, Amazon EC2 will exclude any Spot instance types that cost more than 0.266. We do not recommend using this parameter because Spot prices can fluctuate, and therefore your price protection threshold might also fluctuate.

#### Specify the price protection threshold To specify the price protection threshold using the AWS CLI While creating an EC2 Fleet or Spot Fleet using the AWS CLI, configure the fleet for attribute-based instance type selection, and then do the following:
- To specify the On-Demand Instance price protection threshold, in the JSON configuration file, in the InstanceRequirements structure, for OnDemandMaxPricePercentageOverLowestPrice, enter the price protection threshold as a percentage.
- To specify the Spot Instance price protection threshold, in the JSON configuration file, in the InstanceRequirements structure, specify one of the following parameters:
- For MaxSpotPriceAsPercentageOfOptimalOnDemandPrice, enter the price protection threshold as a percentage.
- For SpotMaxPricePercentageOverLowestPrice, enter the price protection threshold as a percentage.
For more information, see Create an EC2 Fleet with attribute-based instance type selection or Create a Spot Fleet with attribute-based instance type selection.
(Spot Fleet only) To specify the price protection threshold using the console While creating a Spot Fleet in the console, configure the fleet for attribute-based instance type selection, and then do the following:
- To specify the On-Demand Instance price protection threshold, under Additional instance attribute, choose On-demand price protection, choose Add attribute, and then enter the price protection threshold as a percentage.
- To specify the Spot Instance price protection threshold, Additional instance attribute, choose Spot price protection, choose Add attribute, choose a base value on which to base your price, and then enter the price protection threshold as a percentage.

Note When creating the fleet, if you set TargetCapacityUnitType to vcpu or memory-mib, the price protection threshold is applied based on the per-vCPU or per-memory price instead of the per-instance price.
### Performance protection Performance protection is a feature that ensures your EC2 Fleet or Spot Fleet uses instance types that are similar to or exceed a specified performance baseline. To use performance protection, you specify an instance family as a baseline reference. The capabilities of the specified instance family establish the lowest acceptable level of performance. When Amazon EC2 selects instance types for your fleet, it considers your specified attributes and the performance baseline. Instance types that fall below the performance baseline are automatically excluded from selection, even if they match your other specified attributes. This ensures that all selected instance types offer performance similar to or better than the baseline established by the specified instance family. Amazon EC2 uses this baseline to guide instance type selection, but there is no guarantee that the selected instance types will always exceed the baseline for every application.
Currently, this feature only supports CPU performance as a baseline performance factor. The CPU performance of the specified instance family's CPU processor serves as the performance baseline, ensuring that selected instance types are similar to or exceed this baseline. Instance families with the same CPU processors lead to the same filtering results, even if their network or disk performance differs. For example, specifying either c6in or c6i as the baseline reference would produce identical performance-based filtering results because both instance families use the same CPU processor.
Unsupported instance families The following instance families are not supported for performance protection:
- General purpose: Mac1 | Mac2 | Mac2-m1ultra | Mac2-m2 | Mac2-m2pro | M1 | M2 | T1
- Compute optimized: C1
- Memory optimized: U-3tb1 | U-6tb1 | U-9tb1 | U-12tb1 | U-18tb1 | u-24tb1 | U7i-12tb | U7in-16tb | U7in-24tb | U7in-32tb
- Accelerated computing: G3 | G3s | P3dn | P4d | P5
- High-performance computing: Hpc7g

If you enable performance protection by specifying a supported instance family, the returned instance types will exclude the above unsupported instance families.
If you specify an unsupported instance family as a value for baseline performance, the API returns an empty response for GetInstanceTypesFromInstanceRequirements and an exception for CreateFleet, RequestSpotFleet, ModifyFleet, and ModifySpotFleetRequest.
Example: Set a CPU performance baseline In the following example, the instance requirement is to launch with instance types that have CPU cores that are as performant as the c6i instance family. This will filter out instance types with less performant CPU processors, even if they meet your other specified instance requirements such as the number of vCPUs. For example, if your specified instance attributes include 4 vCPUs and 16 GB of memory, an instance type with these attributes but with lower CPU performance than c6i will be excluded from selection.
"BaselinePerformanceFactors": { "Cpu": { "References": [ { "InstanceFamily": "c6i"
                } ]
        }
### Considerations
- You can specify either instance types or instance attributes in an EC2 Fleet or Spot Fleet, but not both at the same time.
When using the CLI, the launch template overrides will override the launch template. For example, if the launch template contains an instance type and the launch template override contains instance attributes, the instances that are identified by the instance attributes will override the instance type in the launch template.
- When using the CLI, when you specify instance attributes as overrides, you can't also specify weights or priorities.
- You can specify a maximum of four InstanceRequirements structures in a request configuration.

### Create an EC2 Fleet with attribute-based instance type selection You can configure an EC2 Fleet to use attribute-based instance type selection. It is not possible to create an EC2 Fleet using the Amazon EC2 console.
The attributes for attribute-based instance type selection are specified in the InstanceRequirements structure. When InstanceRequirements is included in the fleet configuration, InstanceType and WeightedCapacity must be excluded; they can't determine the fleet configuration at the same time as instance attributes.
In the AWS CLI and PowerShell examples, the following attributes are specified:
- VCpuCount – A minimum of 2 vCPUs and a maximum of 4 vCPUs. If you don't need a maximum limit, you can omit the maximum value.
- MemoryMiB – A minimum of 8 GiB of memory and a maximum of 16 GiB. If you don't need a maximum limit, you can omit the maximum value.
This configuration identifies any instance types with 2 to 4 vCPUs and 8 to 16 GiB of memory.
However, price protection and the allocation strategy might exclude some instance types when EC2 Fleet provisions the fleet.
AWS CLI To create an EC2 Fleet with attribute-based instance type selection Use the create-fleet command to create an EC2 Fleet. Specify the fleet configuration in a JSON file. aws ec2 create-fleet \ --region us-east-1 \ --cli-input-json file://file_name.json The following example file_name.json file contains the parameters that configure an EC2 Fleet to use attribute-based instance type selection.
{ "SpotOptions": { "AllocationStrategy": "price-capacity-optimized"
    },

    "LaunchTemplateConfigs": [{ "LaunchTemplateSpecification": { "LaunchTemplateName": "my-launch-template", "Version": "1"
        }, "Overrides": [{ "InstanceRequirements": { "VCpuCount": { "Min": 2, "Max": 4 }, "MemoryMiB": { "Min": 8192, "Max": 16384 } } }]
    }], "TargetCapacitySpecification": { "TotalTargetCapacity": 20, "DefaultTargetCapacityType": "spot"
    }, "Type": "instant"
} PowerShell To create an EC2 Fleet with attribute-based instance type selection Use the New-EC2Fleet cmdlet.
$vcpuCount = New-Object Amazon.EC2.Model.VCpuCountRangeRequest $vcpuCount.Min = 2 $vcpuCount.Max = 4 $memoryMiB = New-Object Amazon.EC2.Model.MemoryMiBRequest $memoryMiB.Min = 8192 $memoryMiB.Max = 16384 $instanceRequirements = New-Object Amazon.EC2.Model.InstanceRequirementsRequest $instanceRequirements.VCpuCount = $vcpuCount $instanceRequirements.MemoryMiB = $memoryMiB $launchTemplateSpec = New-Object Amazon.EC2.Model.FleetLaunchTemplateSpecificationRequest $launchTemplateSpec.LaunchTemplateName = "my-launch-template"

$launchTemplateSpec.Version = "1"
$override = New-Object Amazon.EC2.Model.FleetLaunchTemplateOverridesRequest $override.InstanceRequirements = $instanceRequirements $launchTemplateConfig = New-Object Amazon.EC2.Model.FleetLaunchTemplateConfigRequest $launchTemplateConfig.LaunchTemplateSpecification = $launchTemplateSpec $launchTemplateConfig.Overrides = @($override)
New-EC2Fleet `
    -SpotOptions_AllocationStrategy "price-capacity-optimized" `
    -LaunchTemplateConfig @($launchTemplateConfig) `
    -TargetCapacitySpecification_DefaultTargetCapacityType "spot" `
    -TargetCapacitySpecification_TotalTargetCapacity 20 `
    -Type "instant"
### Create a Spot Fleet with attribute-based instance type selection You can configure a fleet to use attribute-based instance type selection.
The attributes for attribute-based instance type selection are specified in the InstanceRequirements structure. When InstanceRequirements is included in the fleet configuration, InstanceType and WeightedCapacity must be excluded; they can't determine the fleet configuration at the same time as instance attributes.
In the AWS CLI and PowerShell examples, the following attributes are specified:
- VCpuCount – A minimum of 2 vCPUs and a maximum of 4 vCPUs. If you don't need a maximum limit, you can omit the maximum value.
- MemoryMiB – A minimum of 8 GiB of memory and a maximum of 16 GiB. If you don't need a maximum limit, you can omit the maximum value.
This configuration identifies any instance types that have 2 to 4 vCPUs and 8 to 16 GiB of memory.
However, price protection and the allocation strategy might exclude some instance types when Spot Fleet provisions the fleet.
Console To configure a Spot Fleet for attribute-based instance type selection
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Spot Requests, and then choose Request Spot Instances.

3. Follow the steps to create a Spot Fleet. For more information, see Create a Spot Fleet request using defined parameters.
While creating the Spot Fleet, configure the fleet for attribute-based instance type selection as follows: a.
For Instance type requirements, choose Specify instance attributes that match your compute requirements. b.
For vCPUs, enter the desired minimum and maximum number of vCPUs. To specify no limit, select No minimum, No maximum, or both. c.
For Memory (GiB), enter the desired minimum and maximum amount of memory. To specify no limit, select No minimum, No maximum, or both. d.
(Optional) For Additional instance attributes, you can optionally specify one or more attributes to express your compute requirements in more detail. Each additional attribute adds further constraints to your request. e.
(Optional) Expand Preview matching instance types to view the instance types that have your specified attributes.
AWS CLI To configure a Spot Fleet for attribute-based instance type selection Use the request-spot-fleet command to create a Spot Fleet. Specify the fleet configuration in a JSON file. aws ec2 request-spot-fleet \ --region us-east-1 \ --spot-fleet-request-config file://file_name.json The following example file_name.json file contains the parameters that configure a Spot Fleet to use attribute-based instance type selection.
{ "AllocationStrategy": "priceCapacityOptimized", "TargetCapacity": 20, "Type": "request", "LaunchTemplateConfigs": [{ "LaunchTemplateSpecification": { "LaunchTemplateName": "my-launch-template",

            "Version": "1"
        }, "Overrides": [{ "InstanceRequirements": { "VCpuCount": { "Min": 2, "Max": 4 }, "MemoryMiB": { "Min": 8192, "Max": 16384 } } }]
    }]
} PowerShell To configure a Spot Fleet for attribute-based instance type selection Use the Request-EC2SpotFleet cmdlet.
$vcpuCount = New-Object Amazon.EC2.Model.VCpuCountRange $vcpuCount.Min = 2 $vcpuCount.Max = 4 $memoryMiB = New-Object Amazon.EC2.Model.MemoryMiB $memoryMiB.Min = 8192 $memoryMiB.Max = 16384 $instanceRequirements = New-Object Amazon.EC2.Model.InstanceRequirements $instanceRequirements.VCpuCount = $vcpuCount $instanceRequirements.MemoryMiB = $memoryMiB $launchTemplateSpec = New-Object Amazon.EC2.Model.FleetLaunchTemplateSpecification $launchTemplateSpec.LaunchTemplateName = "my-launch-template"
$launchTemplateSpec.Version = "1"
$override = New-Object Amazon.EC2.Model.LaunchTemplateOverrides $override.InstanceRequirements = $instanceRequirements $launchTemplateConfig = New-Object Amazon.EC2.Model.LaunchTemplateConfig $launchTemplateConfig.LaunchTemplateSpecification = $launchTemplateSpec $launchTemplateConfig.Overrides = @($override)
Request-EC2SpotFleet `
    -SpotFleetRequestConfig_AllocationStrategy "PriceCapacityOptimized" `

    -SpotFleetRequestConfig_TargetCapacity 20 `
    -SpotFleetRequestConfig_Type "Request" `
    -SpotFleetRequestConfig_LaunchTemplateConfig $launchTemplateConfig
### Examples of EC2 Fleet configurations that are valid and not valid If you use the AWS CLI to create an EC2 Fleet, you must make sure that your fleet configuration is valid. The following examples show configurations that are valid and not valid.
Configurations are considered not valid when they contain the following:
- A single Overrides structure with both InstanceRequirements and InstanceType
- Two Overrides structures, one with InstanceRequirements and the other with InstanceType
- Two InstanceRequirements structures with overlapping attribute values within the same LaunchTemplateSpecification Example configurations
- Valid configuration: Single launch template with overrides
- Valid configuration: Single launch template with multiple InstanceRequirements
- Valid configuration: Two launch templates, each with overrides
- Valid configuration: Only InstanceRequirements specified, no overlapping attribute values
- Configuration not valid: Overrides contain InstanceRequirements and InstanceType
- Configuration not valid: Two Overrides contain InstanceRequirements and InstanceType
- Configuration not valid: Overlapping attribute values
#### Valid configuration: Single launch template with overrides The following configuration is valid. It contains one launch template and one Overrides structure containing one InstanceRequirements structure. A text explanation of the example configuration follows.
{ "LaunchTemplateConfigs": [ {

            "LaunchTemplateSpecification": { "LaunchTemplateName": "My-launch-template", "Version": "1"
                }, "Overrides": [ { "InstanceRequirements": { "VCpuCount": { "Min": 2, "Max": 8 }, "MemoryMib": { "Min": 0, "Max": 10240 }, "MemoryGiBPerVCpu": { "Max": 10000 }, "RequireHibernateSupport": true } } ]
        } ], "TargetCapacitySpecification": { "TotalTargetCapacity": 5000, "DefaultTargetCapacityType": "spot", "TargetCapacityUnitType": "vcpu"
        } } } InstanceRequirements To use attribute-based instance selection, you must include the InstanceRequirements structure in your fleet configuration, and specify the desired attributes for the instances in the fleet.
In the preceding example, the following instance attributes are specified:
- VCpuCount – The instance types must have a minimum of 2 and a maximum of 8 vCPUs.
- MemoryMiB – The instance types must have a maximum of 10240 MiB of memory. A minimum of 0 indicates no minimum limit.

- MemoryGiBPerVCpu – The instance types must have a maximum of 10,000 GiB of memory per vCPU. The Min parameter is optional. By omitting it, you indicate no minimum limit.
TargetCapacityUnitType The TargetCapacityUnitType parameter specifies the unit for the target capacity. In the example, the target capacity is 5000 and the target capacity unit type is vcpu, which together specify a desired target capacity of 5,000 vCPUs. EC2 Fleet will launch enough instances so that the total number of vCPUs in the fleet is 5,000 vCPUs.
#### Valid configuration: Single launch template with multiple InstanceRequirements The following configuration is valid. It contains one launch template and one Overrides structure containing two InstanceRequirements structures. The attributes specified in InstanceRequirements are valid because the values do not overlap—the first InstanceRequirements structure specifies a VCpuCount of 0-2 vCPUs, while the second InstanceRequirements structure specifies 4-8 vCPUs.
{ "LaunchTemplateConfigs": [ { "LaunchTemplateSpecification": { "LaunchTemplateName": "MyLaunchTemplate", "Version": "1"
                }, "Overrides": [ { "InstanceRequirements": { "VCpuCount": { "Min": 0, "Max": 2 }, "MemoryMiB": { "Min": 0 } } }, { "InstanceRequirements": { "VCpuCount": { "Min": 4, "Max": 8

                        }, "MemoryMiB": { "Min": 0 } } } ]
            } ], "TargetCapacitySpecification": { "TotalTargetCapacity": 1, "DefaultTargetCapacityType": "spot"
        } } }
#### Valid configuration: Two launch templates, each with overrides The following configuration is valid. It contains two launch templates, each with one Overrides structure containing one InstanceRequirements structure. This configuration is useful for arm and x86 architecture support in the same fleet.
{ "LaunchTemplateConfigs": [ { "LaunchTemplateSpecification": { "LaunchTemplateName": "armLaunchTemplate", "Version": "1"
                }, "Overrides": [ { "InstanceRequirements": { "VCpuCount": { "Min": 0, "Max": 2 }, "MemoryMiB": { "Min": 0 } } }, { "LaunchTemplateSpecification": {

                    "LaunchTemplateName": "x86LaunchTemplate", "Version": "1"
                }, "Overrides": [ { "InstanceRequirements": { "VCpuCount": { "Min": 0, "Max": 2 }, "MemoryMiB": { "Min": 0 } } } ]
            } ], "TargetCapacitySpecification": { "TotalTargetCapacity": 1, "DefaultTargetCapacityType": "spot"
        } } }
#### Valid configuration: Only InstanceRequirements specified, no overlapping attribute values The following configuration is valid. It contains two LaunchTemplateSpecification structures, each with a launch template and an Overrides structure containing an InstanceRequirements structure. The attributes specified in InstanceRequirements are valid because the values do not overlap—the first InstanceRequirements structure specifies a VCpuCount of 0-2 vCPUs, while the second InstanceRequirements structure specifies 4-8 vCPUs.
{ "LaunchTemplateConfigs": [ { "LaunchTemplateSpecification": { "LaunchTemplateName": "MyLaunchTemplate", "Version": "1"
                }, "Overrides": [ { "InstanceRequirements": {

                        "VCpuCount": { "Min": 0, "Max": 2 }, "MemoryMiB": { "Min": 0 } } } ]
            }, { "LaunchTemplateSpecification": { "LaunchTemplateName": "MyOtherLaunchTemplate", "Version": "1"
                }, "Overrides": [ { "InstanceRequirements": { "VCpuCount": { "Min": 4, "Max": 8 }, "MemoryMiB": { "Min": 0 } } } ]
            } ], "TargetCapacitySpecification": { "TotalTargetCapacity": 1, "DefaultTargetCapacityType": "spot"
        } } }
#### Configuration not valid: Overrides contain InstanceRequirements and InstanceType The following configuration is not valid. The Overrides structure contains both InstanceRequirements and InstanceType. For the Overrides, you can specify either InstanceRequirements or InstanceType, but not both.

{ "LaunchTemplateConfigs": [ { "LaunchTemplateSpecification": { "LaunchTemplateName": "MyLaunchTemplate", "Version": "1"
                }, "Overrides": [ { "InstanceRequirements": { "VCpuCount": { "Min": 0, "Max": 2 }, "MemoryMiB": { "Min": 0 } } }, { "InstanceType": "m5.large"
                } ]
            } ], "TargetCapacitySpecification": { "TotalTargetCapacity": 1, "DefaultTargetCapacityType": "spot"
        } } }
#### Configuration not valid: Two Overrides contain InstanceRequirements and InstanceType The following configuration is not valid. The Overrides structures contain both InstanceRequirements and InstanceType. You can specify either InstanceRequirements or InstanceType, but not both, even if they're in different Overrides structures.
{ "LaunchTemplateConfigs": [ { "LaunchTemplateSpecification": { "LaunchTemplateName": "MyLaunchTemplate",

                    "Version": "1"
                }, "Overrides": [ { "InstanceRequirements": { "VCpuCount": { "Min": 0, "Max": 2 }, "MemoryMiB": { "Min": 0 } } } ]
            }, { "LaunchTemplateSpecification": { "LaunchTemplateName": "MyOtherLaunchTemplate", "Version": "1"
                }, "Overrides": [ { "InstanceType": "m5.large"
                } ]
            } ], "TargetCapacitySpecification": { "TotalTargetCapacity": 1, "DefaultTargetCapacityType": "spot"
        } } }
#### Configuration not valid: Overlapping attribute values The following configuration is not valid. The two InstanceRequirements structures each contain "VCpuCount": {"Min": 0, "Max": 2}. The values for these attributes overlap, which will result in duplicate capacity pools.
{ "LaunchTemplateConfigs": [

            { "LaunchTemplateSpecification": { "LaunchTemplateName": "MyLaunchTemplate", "Version": "1"
                }, "Overrides": [ { "InstanceRequirements": { "VCpuCount": { "Min": 0, "Max": 2 }, "MemoryMiB": { "Min": 0 } }, { "InstanceRequirements": { "VCpuCount": { "Min": 0, "Max": 2 }, "MemoryMiB": { "Min": 0 } } } } ]
            } ], "TargetCapacitySpecification": { "TotalTargetCapacity": 1, "DefaultTargetCapacityType": "spot"
        } } }
### Examples of Spot Fleet configurations that are valid and not valid If you use the AWS CLI to create a Spot Fleet, you must make sure that your fleet configuration is valid. The following examples show configurations that are valid and not valid.

Configurations are considered not valid when they contain the following:
- A single Overrides structure with both InstanceRequirements and InstanceType
- Two Overrides structures, one with InstanceRequirements and the other with InstanceType
- Two InstanceRequirements structures with overlapping attribute values within the same LaunchTemplateSpecification Example configurations
- Valid configuration: Single launch template with overrides
- Valid configuration: Single launch template with multiple InstanceRequirements
- Valid configuration: Two launch templates, each with overrides
- Valid configuration: Only InstanceRequirements specified, no overlapping attribute values
- Configuration not valid: Overrides contain InstanceRequirements and InstanceType
- Configuration not valid: Two Overrides contain InstanceRequirements and InstanceType
- Configuration not valid: Overlapping attribute values
#### Valid configuration: Single launch template with overrides The following configuration is valid. It contains one launch template and one Overrides structure containing one InstanceRequirements structure. A text explanation of the example configuration follows.
{ "SpotFleetRequestConfig": { "AllocationStrategy": "priceCapacityOptimized", "ExcessCapacityTerminationPolicy": "default", "IamFleetRole": "arn:aws:iam::123456789012:role/aws-ec2-spot-fleet-tagging- role", "LaunchTemplateConfigs": [ { "LaunchTemplateSpecification": { "LaunchTemplateName": "My-launch-template", "Version": "1"
                }, "Overrides": [ {

                    "InstanceRequirements": { "VCpuCount": { "Min": 2, "Max": 8 }, "MemoryMib": { "Min": 0, "Max": 10240 }, "MemoryGiBPerVCpu": { "Max": 10000 }, "RequireHibernateSupport": true } } ]
        } ], "TargetCapacity": 5000, "OnDemandTargetCapacity": 0, "TargetCapacityUnitType": "vcpu"
    } } InstanceRequirements To use attribute-based instance selection, you must include the InstanceRequirements structure in your fleet configuration, and specify the desired attributes for the instances in the fleet.
In the preceding example, the following instance attributes are specified:
- VCpuCount – The instance types must have a minimum of 2 and a maximum of 8 vCPUs.
- MemoryMiB – The instance types must have a maximum of 10240 MiB of memory. A minimum of 0 indicates no minimum limit.
- MemoryGiBPerVCpu – The instance types must have a maximum of 10,000 GiB of memory per vCPU. The Min parameter is optional. By omitting it, you indicate no minimum limit.
TargetCapacityUnitType

The TargetCapacityUnitType parameter specifies the unit for the target capacity. In the example, the target capacity is 5000 and the target capacity unit type is vcpu, which together specify a desired target capacity of 5,000 vCPUs. Spot Fleet will launch enough instances so that the total number of vCPUs in the fleet is 5,000 vCPUs.
#### Valid configuration: Single launch template with multiple InstanceRequirements The following configuration is valid. It contains one launch template and one Overrides structure containing two InstanceRequirements structures. The attributes specified in InstanceRequirements are valid because the values do not overlap—the first InstanceRequirements structure specifies a VCpuCount of 0-2 vCPUs, while the second InstanceRequirements structure specifies 4-8 vCPUs.
{ "SpotFleetRequestConfig": { "AllocationStrategy": "priceCapacityOptimized", "ExcessCapacityTerminationPolicy": "default", "IamFleetRole": "arn:aws:iam::123456789012:role/aws-ec2-spot-fleet-tagging- role", "LaunchTemplateConfigs": [ { "LaunchTemplateSpecification": { "LaunchTemplateName": "MyLaunchTemplate", "Version": "1"
                }, "Overrides": [ { "InstanceRequirements": { "VCpuCount": { "Min": 0, "Max": 2 }, "MemoryMiB": { "Min": 0 } } }, { "InstanceRequirements": { "VCpuCount": { "Min": 4, "Max": 8

                        }, "MemoryMiB": { "Min": 0 } } } ]
            } ], "TargetCapacity": 1, "OnDemandTargetCapacity": 0, "Type": "maintain"
    } }
#### Valid configuration: Two launch templates, each with overrides The following configuration is valid. It contains two launch templates, each with one Overrides structure containing one InstanceRequirements structure. This configuration is useful for arm and x86 architecture support in the same fleet.
{ "SpotFleetRequestConfig": { "AllocationStrategy": "priceCapacityOptimized", "ExcessCapacityTerminationPolicy": "default", "IamFleetRole": "arn:aws:iam::123456789012:role/aws-ec2-spot-fleet-tagging- role", "LaunchTemplateConfigs": [ { "LaunchTemplateSpecification": { "LaunchTemplateName": "armLaunchTemplate", "Version": "1"
                }, "Overrides": [ { "InstanceRequirements": { "VCpuCount": { "Min": 0, "Max": 2 }, "MemoryMiB": { "Min": 0 }

                    } }, { "LaunchTemplateSpecification": { "LaunchTemplateName": "x86LaunchTemplate", "Version": "1"
                }, "Overrides": [ { "InstanceRequirements": { "VCpuCount": { "Min": 0, "Max": 2 }, "MemoryMiB": { "Min": 0 } } } ]
            } ], "TargetCapacity": 1, "OnDemandTargetCapacity": 0, "Type": "maintain"
    } }
#### Valid configuration: Only InstanceRequirements specified, no overlapping attribute values The following configuration is valid. It contains two LaunchTemplateSpecification structures, each with a launch template and an Overrides structure containing an InstanceRequirements structure. The attributes specified in InstanceRequirements are valid because the values do not overlap—the first InstanceRequirements structure specifies a VCpuCount of 0-2 vCPUs, while the second InstanceRequirements structure specifies 4-8 vCPUs.
{ "SpotFleetRequestConfig": { "AllocationStrategy": "priceCapacityOptimized", "ExcessCapacityTerminationPolicy": "default", "IamFleetRole": "arn:aws:iam::123456789012:role/aws-ec2-spot-fleet-tagging- role", "LaunchTemplateConfigs": [

            { "LaunchTemplateSpecification": { "LaunchTemplateName": "MyLaunchTemplate", "Version": "1"
                }, "Overrides": [ { "InstanceRequirements": { "VCpuCount": { "Min": 0, "Max": 2 }, "MemoryMiB": { "Min": 0 } } } ]
            }, { "LaunchTemplateSpecification": { "LaunchTemplateName": "MyOtherLaunchTemplate", "Version": "1"
                }, "Overrides": [ { "InstanceRequirements": { "VCpuCount": { "Min": 4, "Max": 8 }, "MemoryMiB": { "Min": 0 } } } ]
            } ], "TargetCapacity": 1, "OnDemandTargetCapacity": 0, "Type": "maintain"
    }

}
#### Configuration not valid: Overrides contain InstanceRequirements and InstanceType The following configuration is not valid. The Overrides structure contains both InstanceRequirements and InstanceType. For the Overrides, you can specify either InstanceRequirements or InstanceType, but not both.
{ "SpotFleetRequestConfig": { "AllocationStrategy": "priceCapacityOptimized", "ExcessCapacityTerminationPolicy": "default", "IamFleetRole": "arn:aws:iam::123456789012:role/aws-ec2-spot-fleet-tagging- role", "LaunchTemplateConfigs": [ { "LaunchTemplateSpecification": { "LaunchTemplateName": "MyLaunchTemplate", "Version": "1"
                }, "Overrides": [ { "InstanceRequirements": { "VCpuCount": { "Min": 0, "Max": 2 }, "MemoryMiB": { "Min": 0 } } }, { "InstanceType": "m5.large"
                } ]
            } ], "TargetCapacity": 1, "OnDemandTargetCapacity": 0, "Type": "maintain"
    } }

#### Configuration not valid: Two Overrides contain InstanceRequirements and InstanceType The following configuration is not valid. The Overrides structures contain both InstanceRequirements and InstanceType. You can specify either InstanceRequirements or InstanceType, but not both, even if they're in different Overrides structures.
{ "SpotFleetRequestConfig": { "AllocationStrategy": "priceCapacityOptimized", "ExcessCapacityTerminationPolicy": "default", "IamFleetRole": "arn:aws:iam::123456789012:role/aws-ec2-spot-fleet-tagging- role", "LaunchTemplateConfigs": [ { "LaunchTemplateSpecification": { "LaunchTemplateName": "MyLaunchTemplate", "Version": "1"
                }, "Overrides": [ { "InstanceRequirements": { "VCpuCount": { "Min": 0, "Max": 2 }, "MemoryMiB": { "Min": 0 } } } ]
            }, { "LaunchTemplateSpecification": { "LaunchTemplateName": "MyOtherLaunchTemplate", "Version": "1"
                }, "Overrides": [ { "InstanceType": "m5.large"
                } ]
            }

        ], "TargetCapacity": 1, "OnDemandTargetCapacity": 0, "Type": "maintain"
    } }
#### Configuration not valid: Overlapping attribute values The following configuration is not valid. The two InstanceRequirements structures each contain "VCpuCount": {"Min": 0, "Max": 2}. The values for these attributes overlap, which will result in duplicate capacity pools.
{ "SpotFleetRequestConfig": { "AllocationStrategy": "priceCapacityOptimized", "ExcessCapacityTerminationPolicy": "default", "IamFleetRole": "arn:aws:iam::123456789012:role/aws-ec2-spot-fleet-tagging- role", "LaunchTemplateConfigs": [ { "LaunchTemplateSpecification": { "LaunchTemplateName": "MyLaunchTemplate", "Version": "1"
                }, "Overrides": [ { "InstanceRequirements": { "VCpuCount": { "Min": 0, "Max": 2 }, "MemoryMiB": { "Min": 0 } }, { "InstanceRequirements": { "VCpuCount": { "Min": 0, "Max": 2 }, "MemoryMiB": {

                              "Min": 0 } } } } ]
            } ], "TargetCapacity": 1, "OnDemandTargetCapacity": 0, "Type": "maintain"
    } }
### Preview instance types with specified attributes You can use the get-instance-types-from-instance-requirements command to preview the instance types that match the attributes that you specify. This is especially useful for working out what attributes to specify in your request configuration without launching any instances. Note that the command does not consider available capacity.
To preview a list of instance types by specifying attributes using the AWS CLI
1. (Optional) To generate all of the possible attributes that can be specified, use the get- instance-types-from-instance-requirements command and the --generate-cli-skeleton parameter. You can optionally direct the output to a file to save it by using input > attributes.json. aws ec2 get-instance-types-from-instance-requirements \ --region us-east-1 \ --generate-cli-skeleton input > attributes.json Expected output { "DryRun": true, "ArchitectureTypes": [ "i386"
    ], "VirtualizationTypes": [ "hvm"

    ], "InstanceRequirements": { "VCpuCount": { "Min": 0, "Max": 0 }, "MemoryMiB": { "Min": 0, "Max": 0 }, "CpuManufacturers": [ "intel"
        ], "MemoryGiBPerVCpu": { "Min": 0.0, "Max": 0.0 }, "ExcludedInstanceTypes": [ ""
        ], "InstanceGenerations": [ "current"
        ], "SpotMaxPricePercentageOverLowestPrice": 0, "OnDemandMaxPricePercentageOverLowestPrice": 0, "BareMetal": "included", "BurstablePerformance": "included", "RequireHibernateSupport": true, "NetworkInterfaceCount": { "Min": 0, "Max": 0 }, "LocalStorage": "included", "LocalStorageTypes": [ "hdd"
        ], "TotalLocalStorageGB": { "Min": 0.0, "Max": 0.0 }, "BaselineEbsBandwidthMbps": { "Min": 0, "Max": 0 },

        "AcceleratorTypes": [ "gpu"
        ], "AcceleratorCount": { "Min": 0, "Max": 0 }, "AcceleratorManufacturers": [ "nvidia"
        ], "AcceleratorNames": [ "a100"
        ], "AcceleratorTotalMemoryMiB": { "Min": 0, "Max": 0 }, "NetworkBandwidthGbps": { "Min": 0.0, "Max": 0.0 }, "AllowedInstanceTypes": [ ""
        ]
    }, "MaxResults": 0, "NextToken": ""
}
2. Create a JSON configuration file using the output from the previous step, and configure it as follows:
Note You must provide values for ArchitectureTypes, VirtualizationTypes, VCpuCount, and MemoryMiB. You can omit the other attributes; when omitted, the default values are used.
For a description of each attribute and their default values, see get-instance-types- from-instance-requirements. a.
For ArchitectureTypes, specify one or more types of processor architecture.

b.
For VirtualizationTypes, specify one or more types of virtualization. c.
For VCpuCount, specify the minimum and maximum number of vCPUs. To specify no minimum limit, for Min, specify 0. To specify no maximum limit, omit the Max parameter. d.
For MemoryMiB, specify the minimum and maximum amount of memory in MiB. To specify no minimum limit, for Min, specify 0. To specify no maximum limit, omit the Max parameter. e.
You can optionally specify one or more of the other attributes to further constrain the list of instance types that are returned.
3. To preview the instance types that have the attributes that you specified in the JSON file, use the get-instance-types-from-instance-requirements command, and specify the name and path to your JSON file by using the --cli-input-json parameter. You can optionally format the output to appear in a table format. aws ec2 get-instance-types-from-instance-requirements \ --cli-input-json file://attributes.json \ --output table Example attributes.json file In this example, the required attributes are included in the JSON file. They are ArchitectureTypes, VirtualizationTypes, VCpuCount, and MemoryMiB. In addition, the optional InstanceGenerations attribute is also included. Note that for MemoryMiB, the Max value can be omitted to indicate that there is no limit.
{

    "ArchitectureTypes": [ "x86_64"
    ], "VirtualizationTypes": [ "hvm"
    ], "InstanceRequirements": { "VCpuCount": { "Min": 4, "Max": 6 }, "MemoryMiB": { "Min": 2048

        }, "InstanceGenerations": [ "current"
        ]
    } } Example output
------------------------------------------
|GetInstanceTypesFromInstanceRequirements| +----------------------------------------+
||             InstanceTypes            ||
|+--------------------------------------+|
||             InstanceType             ||
|+--------------------------------------+|
||  c4.xlarge                           ||
||  c5.xlarge                           ||
||  c5a.xlarge                          ||
||  c5ad.xlarge                         ||
||  c5d.xlarge                          ||
||  c5n.xlarge                          ||
||  d2.xlarge                           || ...
4. After identifying instance types that meet your needs, make note of the instance attributes that you used so that you can use them when configuring your fleet request.
## Use instance weighting to manage cost and performance of your EC2 Fleet or Spot Fleet Fleet or Spot Fleet With instance weighting, you assign a weight to each instance type in your EC2 Fleet or Spot Fleet to represent their compute capacity and performance relative to each other. Based on the weights, the fleet can use any combination of the specified instance types, as long as it can fulfil the desired target capacity. This can help you manage the cost and performance of your fleet.
The weight represents the capacity units that an instance type contributes to the total target capacity.
Example: Use instance weighting for performance management

Suppose your fleet has two instance types, and you assign a different weight to each instance type to reflect how many you need of each to achieve the same performance, as follows:
- m5.large – weight: 1
- m5.2xlarge – weight: 4 By assigning these weights, you're saying that you'd need 4 m5.large instances to achieve the same performance as 1 m5.2xlarge.
To calculate how many instances of each instance type are needed for a given target capacity, use the following formula: target capacity / weight = number of instances If your target capacity is 8 units, the fleet could fulfill the target capacity with either m5.large or m5.2xlarge, or a mix of both, as follows:
- 8 m5.large instances (capacity of 8 / weight of 1 = 8 instances)
- 2 m5.2xlarge instances (capacity of 8 / weight of 4 = 2 instances)
- 4 m5.large and 1 m5.2xlarge Example: Use instance weighting for cost management By default, the price that you specify is per instance hour. When you use the instance weighting feature, the price that you specify is per unit hour. You can calculate your price per unit hour by dividing your price for an instance type by the number of units that it represents. The fleet calculates the number of instances to launch by dividing the target capacity by the instance weight.
If the result isn't an integer, the fleet rounds it up to the next integer, so that the size of your fleet is not below its target capacity. The fleet can select any pool that you specify in your launch specification, even if the capacity of the instances launched exceeds the requested target capacity.
The following table includes examples of calculations to determine the price per unit for a fleet with a target capacity of 10.

Instance type Instance weight Target capacity Number of instances launched Price per instance hour Price per unit hour r3.xlarge 2 10 5 (10 divided by 2)
$0.05 $0.025 (.05 divided by 2) r3.8xlarg e 8 10 2 (10 divided by 8, result rounded up)
$0.10 $0.0125 (.10 divided by 8)
Use the fleet instance weighting as follows to provision the target capacity that you want in the pools with the lowest price per unit at the time of fulfillment:
1. Set the target capacity for your fleet either in instances (the default) or in the units of your choice, such as vCPU, memory, storage, or throughput.
2. Set the price per unit.
3. For each launch specification, specify the weight, which is the number of units that the instance type represents toward the target capacity.
Instance weighting example Consider a fleet request with the following configuration:
- A target capacity of 24
- A launch specification with an instance type r3.2xlarge and a weight of 6
- A launch specification with an instance type c3.xlarge and a weight of 5 The weights represent the number of units that instance type represents toward the target capacity. If the first launch specification provides the lowest price per unit (price for r3.2xlarge per instance hour divided by 6), the fleet would launch four of these instances (24 divided by 6).

If the second launch specification provides the lowest price per unit (price for c3.xlarge per instance hour divided by 5), the fleet would launch five of these instances (24 divided by 5, result rounded up).
Instance weighting and allocation strategy Consider a fleet request with the following configuration:
- A target capacity of 30 Spot Instances
- A launch specification with an instance type c3.2xlarge and a weight of 8
- A launch specification with an instance type m3.xlarge and a weight of 8
- A launch specification with an instance type r3.xlarge and a weight of 8 The fleet would launch four instances (30 divided by 8, result rounded up). With the diversified strategy, the fleet launches one instance in each of the three pools, and the fourth instance in whichever of the three pools provides the lowest price per unit.
## Use allocation strategies to determine how EC2 Fleet or Spot Fleet fulfills Spot and On-Demand capacity fulfills Spot and On-Demand capacity When you use multiple capacity pools (each comprising an instance type and Availability Zone) in an EC2 Fleet or Spot Fleet, you can use an allocation strategy to manage how Amazon EC2 fulfills your Spot and On-Demand capacities from these pools. The allocation strategies can optimize for available capacity, price, and the instance types to use. There are different allocation strategies for Spot Instances and On-Demand Instances.
Topics
- Allocation strategies for Spot Instances
- Allocation strategies for On-Demand Instances
- Choose the appropriate Spot allocation strategy
- Maintain target capacity for Spot Instances
- Prioritize instance types for On-Demand capacity

### Allocation strategies for Spot Instances Your launch configuration determines all the possible Spot capacity pools (instance types and Availability Zones) from which EC2 Fleet or Spot Fleet can launch Spot Instances. However, when launching instances, the fleet uses the allocation strategy that you specify to pick the specific pools from all your possible pools.
Note (Linux instances only) If you configure your Spot Instance to launch with AMD SEV-SNP turned on, you are charged an additional hourly usage fee that is equivalent to 10% of the On-Demand hourly rate for the selected instance type. If the allocation strategy uses price as an input, the fleet does not include this additional fee; only the Spot price is used.
You can specify one of the following allocation strategies for Spot Instances:
Price capacity optimized (recommended)
The fleet identifies the pools with the highest capacity availability for the number of instances that are launching. This means that we will request Spot Instances from the pools that we believe have the lowest chance of interruption in the near term. The fleet then requests Spot Instances from the lowest priced of these pools.
The price capacity optimized allocation strategy is the best choice for most Spot workloads, such as stateless containerized applications, microservices, web applications, data and analytics jobs, and batch processing.
If you're using the AWS CLI, the parameter name is price-capacity-optimized for EC2 Fleet and priceCapacityOptimized for Spot Fleet.
Capacity optimized The fleet identifies the pools with the highest capacity availability for the number of instances that are launching. This means that we will request Spot Instances from the pools that we believe have the lowest chance of interruption in the near term. You can optionally set a priority for each instance type in your fleet, where the fleet optimizes for capacity first, but honors instance type priorities on a best-effort basis.
With Spot Instances, pricing changes slowly over time based on long-term trends in supply and demand, but capacity fluctuates in real time. The capacity optimized strategy automatically

launches Spot Instances into the most available pools by looking at real-time capacity data and predicting which are the most available. This works well for workloads that may have a higher cost of interruption associated with restarting work, such as long Continuous Integration (CI), image and media rendering, Deep Learning, and High Performance Compute (HPC) workloads that may have a higher cost of interruption associated with restarting work. By offering the possibility of fewer interruptions, the capacity optimized strategy can lower the overall cost of your workload.
Alternatively, you can use the capacity optimized prioritized allocation strategy with a priority parameter to order instance types from highest to lowest priority. You can set the same priority for different instance types. The fleet will optimize for capacity first, but will honor instance type priorities on a best-effort basis (for example, if honoring the priorities will not significantly affect the fleet's ability to provision optimal capacity). This is a good option for workloads where the possibility of disruption must be minimized and the preference for certain instance types matters. Note that when you set the priority for instance types for your Spot capacity, the same priority is also applied to your On-Demand Instances if the On-Demand allocation strategy is set to prioritized. For Spot Fleet, using priorities is supported only if your fleet uses a launch template.
If you're using the AWS CLI, the parameter names are capacity-optimized and capacity-optimized-prioritized for EC2 Fleet and capacityOptimized and capacityOptimizedPrioritized for Spot Fleet.
Diversified The Spot Instances are distributed across all Spot capacity pools. If you're using the AWS CLI, the parameter name is diversified for both EC2 Fleet and Spot Fleet.
Lowest price (not recommended)
Warning We don't recommend the lowest price allocation strategy because it has the highest risk of interruption for your Spot Instances.
The Spot Instances come from the lowest priced pool that has available capacity. When using the AWS CLI, this is the default strategy. However, we recommend that you override the default by specifying the price capacity optimized allocation strategy.

With the lowest price strategy, if the lowest priced pool doesn't have available capacity, the Spot Instances come from the next lowest priced pool that has available capacity. If a pool runs out of capacity before fulfilling your desired capacity, the fleet will continue to fulfill your request by drawing from the next lowest priced pool. To ensure that your desired capacity is met, you might receive Spot Instances from several pools.
Because this strategy only considers instance price and not capacity availability, it might lead to high interruption rates.
The lowest price allocation strategy is only available when using the AWS CLI. The parameter name is lowest-price for EC2 Fleet and lowestPrice for Spot Fleet.
Number of pools to use The number of Spot pools across which to allocate your target Spot capacity. Valid only when the allocation strategy is set to lowest price. The fleet selects the lowest priced Spot pools and evenly allocates your target Spot capacity across the number of Spot pools that you specify.
Note that the fleet attempts to draw Spot Instances from the number of pools that you specify on a best effort basis. If a pool runs out of Spot capacity before fulfilling your target capacity, the fleet will continue to fulfill your request by drawing from the next lowest priced pool. To ensure that your target capacity is met, you might receive Spot Instances from more than the number of pools that you specified. Similarly, if most of the pools have no Spot capacity, you might receive your full target capacity from fewer than the number of pools that you specified.
This parameter is only available when specifying the lowest price allocation strategy and only when using the AWS CLI. The parameter name is InstancePoolsToUseCount for both EC2 Fleet and Spot Fleet.
### Allocation strategies for On-Demand Instances Your launch configuration determines all the possible capacity pools (instance types and Availability Zones) from which EC2 Fleet or Spot Fleet can launch On-Demand Instances. However, when launching instances, the fleet uses the allocation strategy that you specify to pick the specific pools from all your possible pools.
You can specify one of the following allocation strategies for On-Demand Instances:

Lowest price The On-Demand Instances come from the lowest priced pool that has available capacity. This is the default strategy.
If the lowest priced pool doesn't have available capacity, the On-Demand Instances come from the next lowest priced pool that has available capacity.
If a pool runs out of capacity before fulfilling your desired capacity, the fleet will continue to fulfill your request by drawing from the next lowest priced pool. To ensure that your desired capacity is met, you might receive On-Demand Instances from several pools.
Prioritized The fleet uses the priority that you assigned to each launch template override, launching instance types in order of the highest priority first. This strategy can't be used with attribute- based instance type selection. For an example of how to use this allocation strategy, see Prioritize instance types for On-Demand capacity.
### Choose the appropriate Spot allocation strategy You can optimize your fleet for your use case by choosing the appropriate Spot allocation strategy.
#### Balance lowest price and capacity availability To balance the trade-offs between the lowest priced Spot capacity pools and the Spot capacity pools with the highest capacity availability, we recommend that you use the price capacity optimized allocation strategy. This strategy makes decisions about which pools to request Spot Instances from based on both the price of the pools and the capacity availability of Spot Instances in those pools. This means that we will request Spot Instances from the pools that we believe have the lowest chance of interruption in the near term, while still taking price into consideration.
If your fleet runs resilient and stateless workloads, including containerized applications, microservices, web applications, data and analytics jobs, and batch processing, then use the price capacity optimized allocation strategy for optimal cost savings and capacity availability.
If your fleet runs workloads that might have a higher cost of interruption associated with restarting work, then you should implement checkpointing so that applications can restart from that point if they're interrupted. By using checkpointing, you make the price capacity optimized allocation

strategy a good fit for these workloads because it allocates capacity from the lowest priced pools that also offer a low Spot Instance interruption rate.
For example JSON configurations that use the price capacity optimized allocation strategy, see the following:
- EC2 Fleet – Example 10: Launch Spot Instances in a price-capacity-optimized fleet
- Spot Fleet – Example 11: Launch Spot Instances in a priceCapacityOptimized fleet
#### When workloads have a high cost of interruption You can optionally use the capacity optimized strategy if you run workloads that either use similarly priced instance types, or where the cost of interruption is so significant that any cost saving is inadequate in comparison to a marginal increase in interruptions. This strategy allocates capacity from the most available Spot capacity pools that offer the possibility of fewer interruptions, which can lower the overall cost of your workload.
When the possibility of interruptions must be minimized but the preference for certain instance types matters, you can express your pool priorities by using the capacity optimized prioritized allocation strategy and then setting the order of instance types to use from highest to lowest priority.
Note that when you set priorities for capacity optimized prioritized, the same priorities are also applied to your On-Demand Instances if the On-Demand allocation strategy is set to prioritized.
Also note that, for Spot Fleet, using priorities is supported only if your fleet uses a launch template.
For example JSON configurations that use the capacity optimized allocation strategy, see the following:
- EC2 Fleet – Example 8: Launch Spot Instances in a capacity-optimized fleet
- Spot Fleet – Example 9: Launch Spot Instances in a capacity-optimized fleet For example JSON configurations that use the capacity optimized prioritized allocation strategy, see the following:
- EC2 Fleet – Example 9: Launch Spot Instances in a capacity-optimized fleet with priorities
- Spot Fleet – Example 10: Launch Spot Instances in a capacity-optimized fleet with priorities

#### When your workload is time flexible and capacity availability is not a factor If your fleet is small or runs for a short time, you can use price capacity optimized to maximize cost savings while still considering capacity availability.
#### When your fleet is large or runs for a long time If your fleet is large or runs for a long time, you can improve the availability of your fleet by distributing the Spot Instances across multiple pools using the diversified strategy. For example, if your fleet specifies 10 pools and a target capacity of 100 instances, the fleet launches 10 Spot Instances in each pool. If the Spot price for one pool exceeds your maximum price for this pool, only 10% of your fleet is affected. Using this strategy also makes your fleet less sensitive to increases in the Spot price in any one pool over time. With the diversified strategy, the fleet does not launch Spot Instances into any pools with a Spot price that is equal to or higher than the On- Demand price.
### Maintain target capacity for Spot Instances After Spot Instances are terminated due to a change in the Spot price or available capacity of a Spot capacity pool, a fleet of type maintain launches replacement Spot Instances. The allocation strategy determines the pools from which the replacement instances are launched, as follows:
- If the allocation strategy is price capacity optimized, the fleet launches replacement instances in the pools that have the most Spot Instance capacity availability while also taking price into consideration and identifying lowest priced pools with high capacity availability.
- If the allocation strategy is capacity optimized, the fleet launches replacement instances in the pools that have the most Spot Instance capacity availability.
- If the allocation strategy is diversified, the fleet distributes the replacement Spot Instances across the remaining pools.
### Prioritize instance types for On-Demand capacity When an EC2 Fleet or Spot Fleet attempts to fulfill your On-Demand capacity, it defaults to launching the lowest priced instance type first. If the On-Demand allocation strategy is set to prioritized, the fleet uses priority to determine which instance type to use first when fulfilling On- Demand capacity. The priority is assigned to the launch template override, and the highest priority is launched first.
Example: Prioritize instance types

In this example, you configure three launch template overrides, each with a different instance type.
The On-Demand price for the instance types range in price. The following are the instance types used in this example, listed in order of price, starting with the least expensive instance type:
- m4.large – least expensive
- m5.large
- m5a.large If you do not use priority to determine the order, the fleet fulfills the On-Demand capacity by starting with the least expensive instance type.
However, say you have unused m5.large Reserved Instances that you want to use first. You can set the launch template override priority so that the instance types are used in the order of priority, as follows:
- m5.large – priority 1
- m4.large – priority 2
- m5a.large – priority 3
## Use Capacity Rebalancing in EC2 Fleet and Spot Fleet to replace at-risk Spot Instances Spot Instances With Capacity Rebalancing, your EC2 Fleet or Spot Fleet can maintain the desired Spot capacity by proactively replacing Spot Instances at risk of interruption. When a Spot Instance is at an elevated risk of interruption, Amazon EC2 sends a rebalance recommendation. If Capacity Rebalancing is enabled, the rebalance recommendation triggers the launch of a new Spot Instance before the at- risk instance is interrupted.
Capacity Rebalancing helps you maintain workload availability by proactively augmenting your fleet with new Spot Instances before running instances are interrupted by Amazon EC2.
To configure EC2 Fleet to use Capacity Rebalancing to launch a replacement Spot Instance Use the create-fleet command and the relevant parameters in the MaintenanceStrategies structure. For an example JSON configuration, see Example 7: Configure Capacity Rebalancing to launch replacement Spot Instances.

To configure Spot Fleet to use Capacity Rebalancing to launch a replacement Spot Instance You can use the Amazon EC2 console or the AWS CLI to configure Capacity Rebalancing.
(Console) When creating the Spot Fleet, select the Capacity rebalance checkbox. For more information, see step 6.d. in Create a Spot Fleet request using defined parameters.
(AWS CLI) Use the request-spot-fleet command and the relevant parameters in the SpotMaintenanceStrategies structure. For an example JSON configuration, see Example 8:
Configure Capacity Rebalancing to launch replacement Spot Instances.
Topics
- Limitations
- Configuration options
- Considerations
### Limitations
- Capacity Rebalancing is available only for fleets of type maintain.
- When the fleet is running, you can't modify the Capacity Rebalancing setting. To change the Capacity Rebalancing setting, you must delete the fleet and create a new fleet.
### Configuration options The ReplacementStrategy for EC2 Fleet and Spot Fleet supports the following two values: launch-before-terminate Amazon EC2 terminates the Spot Instances that receive a rebalance notification after new replacement Spot Instances are launched. When you specify launch-before-terminate, you must also specify a value for termination-delay. After the new replacement instances are launched, Amazon EC2 waits for the duration of the termination-delay, and then terminates the old instances. For termination-delay, the minimum is 120 seconds (2 minutes), and the maximum is 7200 seconds (2 hours).
We recommend that you use launch-before-terminate only if you can predict how long your instance shutdown procedures will take to complete. This will ensure that the old instances

are terminated only after the shutdown procedures are completed. Note that Amazon EC2 can interrupt the old instances with a two-minute warning before the termination-delay.
We strongly recommend against using the lowest-price (EC2 Fleet) or lowestPrice (Spot Fleet) allocation strategy in combination with launch-before-terminate to avoid having replacement Spot Instances that are also at an elevated risk of interruption. launch Amazon EC2 launches replacement Spot Instances when a rebalance notification is emitted for existing Spot Instances. Amazon EC2 does not terminate the instances that receive a rebalance notification. You can terminate the old instances, or you can leave them running. You are charged for all instances while they are running.
### Considerations If you configure an EC2 Fleet or Spot Fleet for Capacity Rebalancing, consider the following:
Provide as many Spot capacity pools in the request as possible Configure your fleet to use multiple instance types and Availability Zones. This provides the flexibility to launch Spot Instances in various Spot capacity pools. For more information, see Be flexible about instance types and Availability Zones.
Avoid an elevated risk of interruption of replacement Spot Instances To avoid an elevated risk of interruption, we recommend the capacity-optimized or capacity-optimized-prioritized allocation strategy. These strategies ensure that replacement Spot Instances are launched in the most optimal Spot capacity pools, and are therefore less likely to be interrupted in the near future. For more information, see Use the price and capacity optimized allocation strategy.
If you use the lowest-price allocation strategy, your replacement Spot Instances might be at an elevated risk of interruption. This is because Amazon EC2 will always launch instances in the lowest priced pool that has available capacity at that moment, even if your replacement Spot Instances are likely to be interrupted soon after being launched.
Amazon EC2 will only launch a new instance if availability is the same or better One of the goals of Capacity Rebalancing is to improve a Spot Instance's availability. If an existing Spot Instance receives a rebalance recommendation, Amazon EC2 will only launch

a new instance if the new instance provides the same or better availability than the existing instance. If the risk of interruption of a new instance will be worse than the existing instance, then Amazon EC2 will not launch a new instance. Amazon EC2 will, however, continue to assess the Spot capacity pools, and will launch a new instance if availability improves.
There is a chance that your existing instance will be interrupted without Amazon EC2 proactively launching a new instance. When this happens, Amazon EC2 will attempt to launch a new instance regardless of whether the new instance has a high risk of interruption.
Capacity Rebalancing does not increase your Spot Instance interruption rate When you enable Capacity Rebalancing, it does not increase your Spot Instance interruption rate (the number of Spot Instances that are reclaimed when Amazon EC2 needs the capacity back). However, if Capacity Rebalancing detects an instance is at risk of interruption, Amazon EC2 will immediately attempt to launch a new instance. The result is that more instances might be replaced than if you'd waited for Amazon EC2 to launch a new instance after the at-risk instance was interrupted.
While you might replace more instances with Capacity Rebalancing enabled, you benefit from being proactive rather than reactive by having more time to take action before your instances are interrupted. With a Spot Instance interruption notice, you typically only have up to two minutes to gracefully shut down your instance. With Capacity Rebalancing launching a new instance in advance, you give existing processes a better chance of completing on your at-risk instance, you can start your instance shutdown procedures, and prevent new work from being scheduled on your at-risk instance. You can also start preparing the newly-launched instance to take over the application. With Capacity Rebalancing's proactive replacement, you benefit from graceful continuity.
As a theoretical example to demonstrate the risks and benefits of using Capacity Rebalancing, consider the following scenario:
- 2:00 PM – A rebalance recommendation is received for instance-A, and Amazon EC2 immediately starts attempting to launch a replacement instance-B, giving you time to start your shutdown procedures.*
- 2:30 PM – A rebalance recommendation is received for instance-B, replaced with instance-C, giving you time to start your shutdown procedures.*
- 2:32 PM – If Capacity Rebalancing wasn't enabled, and if a Spot Instance interruption notice would've been received at 2:32 PM for instance-A, you would only have had up to two minutes to take action, but Instance-A would have been running up till this time.

* If launch-before-terminate is specified, Amazon EC2 will terminate the at-risk instance after the replacement instance comes online.
Amazon EC2 can launch new replacement Spot Instances until fulfilled capacity is double target capacity When a fleet is configured for Capacity Rebalancing, the fleet attempts to launch a new replacement Spot Instance for every Spot Instance that receives a rebalance recommendation.
After a Spot Instance receives a rebalance recommendation, it is no longer counted as part of the fulfilled capacity. Depending on the replacement strategy, Amazon EC2 either terminates the instance after a preconfigured termination delay, or leaves it running. This gives you the opportunity to perform rebalancing actions on the instance.
If your fleet reaches double its target capacity, it stops launching new replacement instances even if the replacement instances themselves receive a rebalance recommendation.
For example, you create a fleet with a target capacity of 100 Spot Instances. All of the Spot Instances receive a rebalance recommendation, which causes Amazon EC2 to launch 100 replacement Spot Instances. This raises the number of fulfilled Spot Instances to 200, which is double the target capacity. Some of the replacement instances receive a rebalance recommendation, but no more replacement instances are launched because the fleet can't exceed double its target capacity.
Note that you are charged for all of the instances while they are running.
We recommend that you configure your fleet to terminate Spot Instances that receive a rebalance recommendation If you configure your fleet for Capacity Rebalancing, we recommend that you choose launch- before-terminate with an appropriate termination delay only if you can predict how long your instance shutdown procedures will take to complete. This will ensure that the old instances are terminated only after the shutdown procedures are completed.
If you choose to terminate the instances that are recommended for rebalance yourself, we recommend that you monitor the rebalance recommendation signal that is received by the Spot Instances in the fleet. By monitoring the signal, you can quickly perform rebalancing actions on the affected instances before Amazon EC2 interrupts them, and then you can manually terminate them. If you do not terminate the instances, you continue paying for them while they are running. Amazon EC2 does not automatically terminate the instances that receive a rebalance recommendation.

You can set up notifications using Amazon EventBridge or instance metadata. For more information, see Monitor rebalance recommendation signals.
The fleet does not count instances that receive a rebalance recommendation when calculating fulfilled capacity during scale in or out If your fleet is configured for Capacity Rebalancing, and you change the target capacity to either scale in or scale out, the fleet does not count the instances that are marked for rebalance as part of the fulfilled capacity, as follows:
- Scale in – If you decrease your desired target capacity, Amazon EC2 terminates instances that are not marked for rebalance until the desired capacity is reached. The instances that are marked for rebalance are not counted towards the fulfilled capacity.
For example, you create a fleet with a target capacity of 100 Spot Instances. 10 instances receive a rebalance recommendation, so Amazon EC2 launches 10 new replacement instances, resulting in a fulfilled capacity of 110 instances. You then reduce the target capacity to 50 (scale in), but the fulfilled capacity is actually 60 instances because the 10 instances that are marked for rebalance are not terminated by Amazon EC2. You need to manually terminate these instances, or you can leave them running.
- Scale out – If you increase your desired target capacity, Amazon EC2 launches new instances until the desired capacity is reached. The instances that are marked for rebalance are not counted towards the fulfilled capacity.
For example, you create a fleet with a target capacity of 100 Spot Instances. 10 instances receive a rebalance recommendation, so the fleet launches 10 new replacement instances, resulting in a fulfilled capacity of 110 instances. You then increase the target capacity to 200 (scale out), but the fulfilled capacity is actually 210 instances because the 10 instances that are marked for rebalance are not counted by the fleet as part of the target capacity. You need to manually terminate these instances, or you can leave them running.
## Use Capacity Reservations to reserve On-Demand capacity in EC2 Fleet With On-Demand Capacity Reservations, you can reserve compute capacity for your On-Demand Instances in a specified Availability Zone for any duration. You can configure an EC2 Fleet to use the Capacity Reservations first when launching On-Demand Instances.
On-Demand Capacity Reservations are available only for EC2 Fleet with the request type set to instant.

Capacity Reservations are configured as either open or targeted. EC2 Fleet can launch On- Demand Instances into either open or targeted Capacity Reservations, as follows:
- If a Capacity Reservation is open, On-Demand Instances that have matching attributes automatically run in the reserved capacity.
- If a Capacity Reservation is targeted, On-Demand Instances must specifically target it to run in the reserved capacity. This is useful for using up specific Capacity Reservations or for controlling when to use specific Capacity Reservations.
If you use targeted Capacity Reservations in your EC2 Fleet, there must be enough Capacity Reservations to fulfil the target On-Demand capacity, otherwise the launch fails. To avoid a launch fail, rather add the targeted Capacity Reservations to a resource group, and then target the resource group. The resource group doesn't need to have enough Capacity Reservations; if it runs out of Capacity Reservations before the target On-Demand capacity is fulfilled, the fleet can launch the remaining target capacity into regular On-Demand capacity.
To use Capacity Reservations with EC2 Fleet
1. Configure the fleet as type instant. You can't use Capacity Reservations for fleets of other types.
2. Configure the usage strategy for Capacity Reservations as use-capacity-reservations- first.
3. In the launch template, for Capacity reservation, choose either Open or Target by group. If you choose Target by group, specify the Capacity Reservations resource group ID.
When the fleet attempts to fulfil the On-Demand capacity, if it finds that multiple instance pools have unused matching Capacity Reservations, it determines the pools in which to launch the On-Demand Instances based on the On-Demand allocation strategy (lowest-price or prioritized).
Related resources
- For CLI examples of how to configure a fleet to use Capacity Reservations to fulfil On-Demand capacity, see Example CLI configurations for EC2 Fleet, specifically Examples 5 through 7.
- For a tutorial that takes you through the steps for creating Capacity Reservations, using them in your fleet, and viewing how many Capacity Reservations are remaining, see Tutorial: Configure EC2 Fleet to launch On-Demand Instances using targeted Capacity Reservations
