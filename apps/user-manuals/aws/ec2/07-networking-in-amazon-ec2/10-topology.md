# Amazon EC2 topology

Source: apps/user-manuals/aws/ec2-ug.pdf

---

# Amazon EC2 topology Amazon EC2 topology provides a hierarchical view of the relative proximity of your compute capacity. You can use this information to manage high performance computing (HPC), machine learning (ML), and generative AI compute infrastructure at scale.
Available APIs Amazon EC2 provides two APIs for understanding your EC2 topology:
- DescribeInstanceTopology
- Shows where your running instances are located relative to each other in the network hierarchy.
- Helps optimize where to run your workloads on your existing instances.
- DescribeCapacityReservationTopology
- Shows where your reserved capacity will be located relative to each other in the network hierarchy before you launch instances.
- Helps with capacity planning by letting you know the placement of reserved capacity before launching instances.
Key benefits EC2 topology provides the following key benefits:
- Capacity management – Optimize resource utilization.
- Job scheduling – Make informed decisions about workload placement.
- Node ranking – Understand relative proximity for performance optimization on tightly coupled instances.
Considerations
- Topology views are only available for:
- Instances in the running state
- Capacity Reservations in the pending or active state
- Each topology view is unique per AWS account.
- The AWS Management Console does not support viewing topology.

- While topology information helps you understand instance placement, you can't use it to launch a new instance physically close to an existing instance. To influence instance placement, you can create Capacity Reservations in cluster placement groups.
Pricing There is no additional cost for describing your EC2 topology.
Contents
- How Amazon EC2 topology works
- Prerequisites for Amazon EC2 topology
- Examples for Amazon EC2 instance topology
## How Amazon EC2 topology works The AWS network is arranged in a hierarchy of layers. EC2 instances connect into the network at or below the third layer, depending on the instance type. An instance's topology is described by a set of nodes, with one node in each layer of the network. The node set in the DescribeInstanceTopology or DescribeCapacityReservationTopology API response provides a top- down view of the network hierarchy, with the bottom node connected to an instance.
Note Some instance types comprise 4 network nodes in a node set representing 4 layers in the network, while others comprise 3 network nodes representing 3 layers in the network. For the supported instance types, see Instance types.
Depending on the type of Capacity Reservation, you might see only 1, 2, or 3 network nodes.
The following diagram provides a visual representation that you can use to understand EC2 topology. The network nodes are identified as NN1 – NN7. The numerals i, ii, and iii identify the network layers. The numbers 1, 2, 3, and 4 identify the EC2 instances. Instances connect to a node in the bottom layer, identified by iii in the following diagram. More than one instance can connect to the same node.

In this example:
- Instance 1 connects to network node 4 (NN4) in layer iii. NN4 connects to network node 2 (NN2) in layer ii, and NN2 connects to network node 1 (NN1) in layer i, which is the top of the network hierarchy in this example. The network node set comprises NN1, NN2, and NN4, expressed hierarchically from the upper layers to the bottom layer.
- Instance 2 also connects to network node 4 (NN4). Instance 1 and instance 2 share the same network node set: NN1, NN2, and NN4.
- Instance 3 connects to network node 5 (NN5). NN5 connects to NN2, and NN2 connects to NN1.
The network node set for instance 3 is NN1, NN2, and NN5.
- Instance 4 connects to network node 6 (NN6). Its network node set is NN1, NN3, and NN6.
When considering the proximity of instances 1, 2, and 3, instances 1 and 2 are closer to each other because they connect to the same network node (NN4), while instance 3 is further away because it connects to a different network node (NN5).

When considering the proximity of all the instances in this diagram, instances 1, 2, and 3 are closer to each other than they are to instance 4 because they share NN2 in their network node set.
As a general rule, if the network node connected to any two instances is the same, these instances are physically close to each other, as is the case with instances 1 and 2. Furthermore, the fewer the number of hops between network nodes, the closer the instances are to each other. For example, instances 1 and 3 have fewer hops to a common network node (NN2) than they have to the network node (NN1) they have in common with instance 4, and are therefore closer to each other than they are to instance 4.
There are no instances running under network node 7 (NN7) in this example, and therefore the API output won't include NN7.
### How to interpret the DescribeInstanceTopology output You can describe the instance topology using the DescribeInstanceTopology API. The output provides a hierarchical view of the underlying network topology for an instance.
The following example output corresponds to the network topology information of the four instances in the preceding diagram. Comments are included in the example output for the purposes of this example.
The following information in the output is important to note:
- NetworkNodes describes the network node set of a single instance.
- In each network node set, the network nodes are listed in hierarchical order from top to bottom.
- The network node that is connected to the instance is the last network node in the list (the bottom layer).
- To work out which instances are close to each other, first find common network nodes in the bottom layer. If there are no common network nodes in the bottom layer, then find common network nodes in the upper layers.
In the following example output, i-1111111111example and i-2222222222example are located closest to each other compared to the other instances in this example because they have the network node nn-4444444444example in common in the bottom layer.

Note The response contains 3 or more network nodes. For information about the number of network nodes in the response for each supported instance type, see Instance types.
{ "Instances": [ { "InstanceId": "i-1111111111example",  //Corresponds to instance 1 "InstanceType": "p4d.24xlarge", "GroupName": "ML-group", "NetworkNodes": [ "nn-1111111111example",           //Corresponds to NN1 in layer i "nn-2222222222example",           //Corresponds to NN2 in layer ii "nn-4444444444example"            //Corresponds to NN4 in layer iii - bottom layer, connected to the instance ], "CapacityBlockId": "null", "ZoneId": "usw2-az2", "AvailabilityZone": "us-west-2a"
        }, { "InstanceId": "i-2222222222example",  //Corresponds to instance 2 "InstanceType": "p4d.24xlarge", "NetworkNodes": [ "nn-1111111111example",           //Corresponds to NN1 - layer i "nn-2222222222example",           //Corresponds to NN2 - layer ii "nn-4444444444example"            //Corresponds to NN4 - layer iii - connected to instance ], "CapacityBlockId": "null", "ZoneId": "usw2-az2", "AvailabilityZone": "us-west-2a"
        }, { "InstanceId": "i-3333333333example",  //Corresponds to instance 3 "InstanceType": "trn1.32xlarge", "NetworkNodes": [ "nn-1111111111example",           //Corresponds to NN1 - layer i "nn-2222222222example",           //Corresponds to NN2 - layer ii

                "nn-5555555555example"            //Corresponds to NN5 - layer iii - connected to instance ], "CapacityBlockId": "null", "ZoneId": "usw2-az2", "AvailabilityZone": "us-west-2a"
        }, { "InstanceId": "i-444444444example",  //Corresponds to instance 4 "InstanceType": "trn1.2xlarge", "NetworkNodes": [ "nn-1111111111example",          //Corresponds to NN1 - layer i "nn-3333333333example",          //Corresponds to NN3 - layer ii "nn-6666666666example"           //Corresponds to NN6 - layer iii - connected to instance ], "CapacityBlockId": "null", "ZoneId": "usw2-az2", "AvailabilityZone": "us-west-2a"
        } ], "NextToken": "SomeEncryptedToken"
}
### How to interpret the DescribeCapacityReservationTopology output You can describe the Capacity Reservation topology using the DescribeCapacityReservationTopology API. The output provides a hierarchical view of the underlying network topology for the reserved capacity.
The following example output corresponds to the network topology information in the preceding diagram. Comments are included in the example output for the purposes of this example.
The following information in the output is important to note:
- NetworkNodes describes the network node set of a single Capacity Reservation.
- In each network node set, the network nodes are listed in hierarchical order from top to bottom.
- The network node that is connected to the Capacity Reservation is the last network node in the list (the bottom layer).

- To work out whether Capacity Reservations will be close to each other, first find common network nodes in the bottom layer in the output. If there are no common network nodes in the bottom layer, then find common network nodes in the upper layers.
In the following example output, cr-1111111111example is located on nn-2222222222example and cr-2222222222example is located on nn-3333333333example.
Because the Capacity Reservations are on different network nodes in layer ii, communication from instances in one Capacity Reservation to instances in the other Capacity Reservation will be inefficient.
Note The response contains 1, 2, or 3 network nodes depending on the type of Capacity Reservation.
{ "CapacityReservations": [ { "CapacityReservationId": "cr-1111111111example", "CapacityBlockId": "null", "State": "active", "InstanceType": "p4d.24xlarge", "NetworkNodes": [ "nn-1111111111example",      //Corresponds to NN1 - layer i "nn-2222222222example"       //Corresponds to NN2 - layer ii // Visibility of additional nodes requires an instance launch and // the DescribeInstanceTopology API ], "AvailabilityZone": "us-west-2a"
        }, { "CapacityReservationId": "cr-2222222222example", "CapacityBlockId": "null", "State": "active", "InstanceType": "trn1.2xlarge", "NetworkNodes": [ "nn-1111111111example",      //Corresponds to NN1 - layer i "nn-3333333333example"       //Corresponds to NN3 - layer ii // Visibility of additional nodes requires an instance launch and

                // the DescribeInstanceTopology API ], "AvailabilityZone": "us-west-2a"
        } ], "NextToken": "SomeEncryptedToken"
}
### Differences between DescribeInstanceTopology and DescribeCapacityReservationTopology DescribeCapacityReservationTopology The following table compares the key differences between the DescribeInstanceTopology and DescribeCapacityReservationTopology APIs:
Comparison point DescribeInstanceTopology DescribeCapacityReservation Topology Usage phase Post-launch (execution mode)
Pre-launch (planning and management mode)
Primary purpose Optimize workloads on running instances Capacity planning and Capacity Reservation management (merge, split, assign) before instance launch Number of network nodes Shows all nodes for a running instance. If the instance is in a Capacity Reservation, the first nodes will match the corresponding Capacity Reservation topology, followed by additional nodes to connect to the instance.
Shows a partial set of nodes, which vary based on the Capacity Reservation state (pending or active) and type.*
### State Instances must be in running state Capacity Reservations must be in pending or active state Use cases
- Workload optimization
- Capacity planning

Comparison point DescribeInstanceTopology DescribeCapacityReservation Topology
- Performance tuning
- Runtime topology analysis
- Capacity Reservation management (merge/split/ assign)
- Pre-launch topology assessment
* For Capacity Blocks for Ultraservers, the network node set is the same when describing the topology for an active Capacity Reservation or its running instance.
## Prerequisites for Amazon EC2 topology To describe your Amazon EC2 topology, ensure that your instances and Capacity Reservations meet the following prerequisites.
Prerequisites for:
- AWS Regions
- Instance types
- State
- IAM permissions
### AWS Regions Supported AWS Regions:
- US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon)
- Africa (Cape Town)
- Asia Pacific (Jakarta), Asia Pacific (Hong Kong), Asia Pacific (Hyderabad), Asia Pacific (Melbourne), Asia Pacific (Mumbai), Asia Pacific (Osaka), Asia Pacific (Seoul), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Tokyo)
- Canada (Central)
- Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Paris), Europe (Spain), Europe (Stockholm), Europe (Zurich)

- Israel (Tel Aviv)
- Middle East (Bahrain), Middle East (UAE)
- South America (São Paulo)
- AWS GovCloud (US-West)
The DescribeCapacityReservationTopology API is not supported in Israel (Tel Aviv) and AWS GovCloud (US-West).
### Instance types Supported instance types:
- Returns 3* network nodes in the response:
- g6e.xlarge | g6e.2xlarge | g6e.4xlarge | g6e.8xlarge | g6e.12xlarge | g6e.16xlarge | g6e.24xlarge | g6e.48xlarge | g7e.2xlarge | g7e.4xlarge | g7e.8xlarge | g7e.12xlarge | g7e.24xlarge | g7e.48xlarge
- hpc6a.48xlarge | hpc6id.32xlarge | hpc7g.4xlarge | hpc7g.8xlarge | hpc7g.16xlarge | hpc7a.12xlarge | hpc7a.24xlarge | hpc7a.48xlarge | hpc7a.96xlarge | hpc8a.96xlarge
- p3dn.24xlarge | p4d.24xlarge | p4de.24xlarge | p5.48xlarge | p5e.48xlarge | p5en.48xlarge | p6e-gb200.36xlarge
- trn1.2xlarge | trn1.32xlarge | trn1n.32xlarge | trn2.48xlarge | trn2u.48xlarge
- Returns 4* network nodes in the response:
- p6-b200.48xlarge | p6-b300.48xlarge
* The number of network nodes returned is only applicable when using the DescribeInstanceTopology API. For the DescribeCapacityReservationTopology API, the number of network nodes returned will vary depending on the type and state of the Capacity Reservation.
The available instance types vary by Region. For more information, see Amazon EC2 instance types by Region.
State
- For DescribeInstanceTopology – Instances must be in the running state.

- For DescribeCapacityReservationTopology – Capacity Reservations must be in the pending or active state.
You can't get topology information for instances or Capacity Reservations in any other state.
### IAM permissions Your IAM identity (user, user group, or role) requires the following permissions:
- ec2:DescribeInstanceTopology
- ec2:DescribeCapacityReservationTopology
## Examples for Amazon EC2 instance topology You can use the describe-instance-topology command to describe the topology for your EC2 instances. And you can use the describe-capacity-reservation-topology command to describe the topology of your Capacity Reservations.
When you use the describe-instance-topology or describe-capacity-reservation- topology command without parameters or filters, the response includes all your instances or Capacity Reservations (depending on the command used) that match the supported instance types for this command in the specified Region. You can specify the Region by including the --region parameter, or by setting a default Region. For more information about setting a default Region, see Select a Region for your Amazon EC2 resources.
You can include parameters to return instances or Capacity Reservations that match specified instance or Capacity Reservation IDs or placement group names. You can also include filters to return instances or Capacity Reservations that match a specified instance type or instance family, or instances or Capacity Reservations in a specified Availability Zone or Local Zone. You can include a single parameter or filter, or a combination of parameters and filters.
The output is paginated, with up to 20 instances or Capacity Reservations per page by default.
You can specify up to 100 instances or Capacity Reservations per page using the --max-results parameter.
For more information, see describe-instance-topology and describe-reservation-topology- topology.

Required permissions The following permissions are required:
- ec2:DescribeInstanceTopology – For describing instance topology
- ec2:DescribeCapacityReservationTopology – For describing Capacity Reservation topology Examples
- Example 1: DescribeInstanceTopology - Instance IDs
- Example 2: DescribeInstanceTopology - Placement group name parameter
- Example 3: DescribeInstanceTopology - Instance type filter
- Example 3a – Exact match filter for a specified instance type
- Example 3b – Wild card filter for an instance family
- Example 3c – Combined instance family and exact match filters
- Example 4: DescribeInstanceTopology - Zone ID filter
- Example 4a – Availability Zone filter
- Example 4b – Local Zone filter
- Example 4c – Combined Availability Zone and Local Zone filters
- Example 5: DescribeInstanceTopology - Instance type and zone ID filters
- Example 6: DescribeCapacityReservationTopology - Capacity Reservation IDs
- Example 7: DescribeCapacityReservationTopology - Instance type filter
### Example 1: DescribeInstanceTopology - Instance IDs AWS CLI To describe the topology of specific instances Use the describe-instance-topology command with the --instance-ids parameter. The output includes only the instances that match the specified instance IDs. aws ec2 describe-instance-topology \ --region us-west-2 \

    --instance-ids i-1111111111example i-2222222222example The following is example output.
{ "Instances": [ { "InstanceId": "i-1111111111example", "InstanceType": "p4d.24xlarge", "GroupName": "ML-group", "NetworkNodes": [ "nn-1111111111example", "nn-2222222222example", "nn-3333333333example"
            ], "CapacityBlockId": "null", "ZoneId": "usw2-az2", "AvailabilityZone": "us-west-2a"
        }, { "InstanceId": "i-2222222222example", "InstanceType": "trn1n.32xlarge", "GroupName": "HPC-group", "NetworkNodes": [ "nn-1111111111example", "nn-2222222222example", "nn-3214313214example"
            ], "CapacityBlockId": "null", "ZoneId": "usw2-az2", "AvailabilityZone": "us-west-2a"
        } ], "NextToken": "SomeEncryptedToken"
} PowerShell To describe the topology of specific instances Use the Get-EC2InstanceTopology cmdlet.
Get-EC2InstanceTopology `

    -InstanceId i-1111111111example, i-2222222222example
### Example 2: DescribeInstanceTopology - Placement group name parameter AWS CLI To describe the topology of instances in a specific placement group Use the describe-instance-topology command with the group-names parameter. The output includes only the instances that are in either of the specified placement groups. aws ec2 describe-instance-topology \ --region us-west-2 \ --group-names ML-group HPC-group The following is example output.
{ "Instances": [ { "InstanceId": "i-1111111111example", "InstanceType": "p4d.24xlarge", "GroupName": "ML-group", "NetworkNodes": [ "nn-1111111111example", "nn-2222222222example", "nn-3333333333example"
            ], "CapacityBlockId": "null", "ZoneId": "usw2-az2", "AvailabilityZone": "us-west-2a"
        }, { "InstanceId": "i-2222222222example", "InstanceType": "trn1n.32xlarge", "GroupName": "HPC-group", "NetworkNodes": [ "nn-1111111111example", "nn-2222222222example", "nn-3214313214example"
            ], "CapacityBlockId": "null",

            "ZoneId": "usw2-az2", "AvailabilityZone": "us-west-2a"
        } ], "NextToken": "SomeEncryptedToken"
} PowerShell To describe the topology of instances in a specific placement group Use the Get-EC2InstanceTopology cmdlet.
Get-EC2InstanceTopology `
    -GroupName ML-group, HPC-group
### Example 3: DescribeInstanceTopology - Instance type filter You can filter by a specified instance type (exact match) or filter by an instance family (using a wildcard). You can also combine a specified instance type filter and instance family filter.
#### Example 3a – Exact match filter for a specified instance type AWS CLI To describe the topology of instances with a specific instance type Use the describe-instance-topology command with the instance-type filter. The output includes only the instances with the specified instance type. aws ec2 describe-instance-topology \ --region us-west-2 \ --filters Name=instance-type,Values=trn1n.32xlarge The following is example output.
{ "Instances": [ { "InstanceId": "i-2222222222example",

            "InstanceType": "trn1n.32xlarge", "NetworkNodes": [ "nn-1111111111example", "nn-2222222222example", "nn-3333333333example"
            ], "CapacityBlockId": "null", "ZoneId": "usw2-az2", "AvailabilityZone": "us-west-2a"
        } ], "NextToken": "SomeEncryptedToken"
} PowerShell To describe the topology of instances with a specific instance type Use the Get-EC2InstanceTopology cmdlet.
Get-EC2InstanceTopology `
    -Filter @{Name="instance-type"; Values="trn1n.32xlarge"}
#### Example 3b – Wild card filter for an instance family AWS CLI To describe the topology of instances with a specific instance family Use the describe-instance-topology command with the instance-type filter. The output includes only the instances with the specified instance family. aws ec2 describe-instance-topology \ --region us-west-2 \ --filters Name=instance-type,Values=trn1* The following is example output.
{ "Instances": [ {

            "InstanceId": "i-2222222222example", "InstanceType": "trn1n.32xlarge", "NetworkNodes": [ "nn-1111111111example", "nn-2222222222example", "nn-3333333333example"
            ], "CapacityBlockId": "null", "ZoneId": "usw2-az2", "AvailabilityZone": "us-west-2a"
        }, { "InstanceId": "i-3333333333example", "InstanceType": "trn1.32xlarge", "NetworkNodes": [ "nn-1212121212example", "nn-1211122211example", "nn-1311133311example"
            ], "CapacityBlockId": "null", "ZoneId": "usw2-az4", "AvailabilityZone": "us-west-2d"
        }, { "InstanceId": "i-444444444example", "InstanceType": "trn1.2xlarge", "NetworkNodes": [ "nn-1111111111example", "nn-5434334334example", "nn-1235301234example"
            ], "CapacityBlockId": "null", "ZoneId": "usw2-az2", "AvailabilityZone": "us-west-2a"
        } ], "NextToken": "SomeEncryptedToken"
} PowerShell To describe the topology of instances with a specific instance family Use the Get-EC2InstanceTopology cmdlet.

Get-EC2InstanceTopology `
    -Filter @{Name="instance-type"; Values="trn1*"}
#### Example 3c – Combined instance family and exact match filters AWS CLI To describe the topology of instances with an instance family or instance type Use the describe-instance-topology command with the instance-type filter. The output includes only the instances that meet the specified criteria. aws ec2 describe-instance-topology \ --region us-west-2 \ --filters "Name=instance-type,Values=p4d*,trn1n.32xlarge"
The following is example output.
{ "Instances": [ { "InstanceId": "i-1111111111example", "InstanceType": "p4d.24xlarge", "GroupName": "ML-group", "NetworkNodes": [ "nn-1111111111example", "nn-2222222222example", "nn-3333333333example"
            ], "CapacityBlockId": "null", "ZoneId": "usw2-az2", "AvailabilityZone": "us-west-2a"
        }, { "InstanceId": "i-2222222222example", "InstanceType": "trn1n.32xlarge", "NetworkNodes": [ "nn-1111111111example", "nn-2222222222example", "nn-4343434343example"
            ],

            "CapacityBlockId": "null", "ZoneId": "usw2-az2", "AvailabilityZone": "us-west-2a"
        } ], "NextToken": "SomeEncryptedToken"
} PowerShell To describe the topology of instances with an instance family or instance type Use the Get-EC2InstanceTopology cmdlet.
Get-EC2InstanceTopology `
    -Filter @{Name="instance-type"; Values="p4d*", "trn1n.32xlarge"}
### Example 4: DescribeInstanceTopology - Zone ID filter You can use the zone-id filter to filter by an Availability Zone or Local Zone. You can also combine an Availability Zone filter and Local Zone filter.
#### Example 4a – Availability Zone filter AWS CLI To describe the topology of instances in a specific Availability Zone Use the describe-instance-topology command with the zone-id filter. The output includes only the instances in the specified Availability Zone. aws ec2 describe-instance-topology \ --region us-east-1 \ --filters Name=zone-id,Values=use1-az1 The following is example output.
{ "Instances": [ { "InstanceId": "i-2222222222example",

            "InstanceType": "trn1n.32xlarge", "NetworkNodes": [ "nn-1111111111example", "nn-2222222222example", "nn-3214313214example"
            ], "CapacityBlockId": "null", "ZoneId": "use1-az1", "AvailabilityZone": "us-east-1a"
        } ], "NextToken": "SomeEncryptedToken"
} PowerShell To describe the topology of instances in a specific Availability Zone Use the Get-EC2InstanceTopology cmdlet.
Get-EC2InstanceTopology `
    -Filter @{Name="zone-id"; Values="use1-az1"}
#### Example 4b – Local Zone filter AWS CLI To describe the topology of instances in a specific Local Zone Use the describe-instance-topology command with the zone-id filter. The output includes only the instances in the specified Local Zone. aws ec2 describe-instance-topology \ --region us-east-1 \ --filters Name=zone-id,Values=use1-atl2-az1 The following is example output.
{ "Instances": [ {

            "InstanceId": "i-1111111111example", "InstanceType": "p4d.24xlarge", "GroupName": "ML-group", "NetworkNodes": [ "nn-1111111111example", "nn-2222222222example", "nn-3333333333example"
            ], "CapacityBlockId": "null", "ZoneId": "use1-atl2-az1", "AvailabilityZone": "us-east-1-atl-2a"
        } ], "NextToken": "SomeEncryptedToken"
} PowerShell To describe the topology of instances in a specific Local Zone Use the Get-EC2InstanceTopology cmdlet.
Get-EC2InstanceTopology `
    -Filter @{Name="zone-id"; Values="use1-atl2-az1"}
#### Example 4c – Combined Availability Zone and Local Zone filters AWS CLI To describe the topology of instances in a specific zone Use the describe-instance-topology command with the zone-id filter. The output includes only the instances that are in either of the specified zones. aws ec2 describe-instance-topology \ --region us-east-1 \ --filters Name=zone-id,Values=use1-az1,use1-atl2-az1 The following is example output.
{

    "Instances": [ { "InstanceId": "i-1111111111example", "InstanceType": "p4d.24xlarge", "GroupName": "ML-group", "NetworkNodes": [ "nn-1111111111example", "nn-2222222222example", "nn-3333333333example"
            ], "CapacityBlockId": "null", "ZoneId": "use1-atl2-az1", "AvailabilityZone": "us-east-1-atl-2a"
        }, { "InstanceId": "i-2222222222example", "InstanceType": "trn1n.32xlarge", "NetworkNodes": [ "nn-1111111111example", "nn-2222222222example", "nn-3214313214example"
            ], "CapacityBlockId": "null", "ZoneId": "use1-az1", "AvailabilityZone": "us-east-1a"
        } ], "NextToken": "SomeEncryptedToken"
} PowerShell To describe the topology of instances in a specific zone Use the Get-EC2InstanceTopology cmdlet.
Get-EC2InstanceTopology `
    -Filter @{Name="zone-id"; Values="use1-az1", "use1-atl2-az1"}
### Example 5: DescribeInstanceTopology - Instance type and zone ID filters You can combine filters in a single command.

AWS CLI To describe the topology of instances with specific instance types, instance families, and zones Use the describe-instance-topology command with the instance-type and zone-id filters.
The response contains any instances with either of the specified instance types and are in either of the specified zones. aws ec2 describe-instance-topology \ --region us-east-1 \ --filters "Name=instance-type,Values=p4d*,trn1n.32xlarge" \ "Name=zone-id,Values=use1-az1,use1-atl2-az1"
The following is example output.
{ "Instances": [ { "InstanceId": "i-1111111111example", "InstanceType": "p4d.24xlarge", "GroupName": "ML-group", "NetworkNodes": [ "nn-1111111111example", "nn-2222222222example", "nn-3333333333example"
            ], "CapacityBlockId": "null", "ZoneId": "use1-atl2-az1", "AvailabilityZone": "us-east-1-atl-2a"
        }, { "InstanceId": "i-2222222222example", "InstanceType": "trn1n.32xlarge", "NetworkNodes": [ "nn-1111111111example", "nn-2222222222example", "nn-3214313214example"
            ], "CapacityBlockId": "null", "ZoneId": "use1-az1", "AvailabilityZone": "us-east-1a"
        }

    ], "NextToken": "SomeEncryptedToken"
} PowerShell To describe the topology of instances with specific instance types, instance families, and zones Use the Get-EC2InstanceTopology cmdlet.
Get-EC2InstanceTopology `
    -Filter @{Name="instance-type"; Values="p4d*", "trn1n.32xlarge"} `
            @{Name="zone-id"; Values="use1-az1", "use1-atl2-az1"}
### Example 6: DescribeCapacityReservationTopology - Capacity Reservation IDs AWS CLI To describe the topology of specific Capacity Reservations Use the describe-capacity-reservation-topology command with the capacity-reservation- id parameter. The output includes only the Capacity Reservations that match the specified Capacity Reservation IDs. aws ec2 describe-capacity-reservation-topology \ --region us-east-1 \ --capacity-reservation-id cr-1111111111example cr-2222222222example The following is example output.
{ "CapacityReservations": [ { "CapacityReservationId": "cr-1111111111example", "CapacityBlockId": "null", "State": "active", "InstanceType": "p5.48xlarge", "NetworkNodes": [ "nn-1111111111example",

                "nn-2222222222example"
            ], "AvailabilityZone": "us-east-1a"
        }, { "CapacityReservationId": "cr-2222222222example", "CapacityBlockId": "null", "State": "active", "InstanceType": "p5en.48xlarge", "NetworkNodes": [ "nn-1111111111example", "nn-2222222222example"
            ], "AvailabilityZone": "us-east-1a"
        } ], "NextToken": "SomeEncryptedToken"
} PowerShell To describe the topology of specific Capacity Reservations Use the Get-EC2CapacityReservationTopology cmdlet.
Get-EC2CapacityReservationTopology `
    -CapacityReservationId cr-1111111111example cr-2222222222example
### Example 7: DescribeCapacityReservationTopology - Instance type filter You can filter by a specified instance type (exact match) or filter by an instance family (using a wildcard). You can also combine a specified instance type filter and instance family filter.
AWS CLI To describe the topology of Capacity Reservations with a specific instance type Use the describe-capacity-reservation-topology command with the instance-type filter. The response contains any instances with the specified instance type. aws ec2 describe-capacity-reservation-topology \ --region us-east-1 \
