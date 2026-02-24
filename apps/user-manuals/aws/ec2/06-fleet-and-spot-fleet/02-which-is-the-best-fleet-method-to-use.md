# Which is the best fleet method to use?

Source: apps/user-manuals/aws/ec2-ug.pdf

---

Multiple purchasing options A fleet can launch multiple purchase options (Spot and On-Demand Instances), allowing you to optimize costs through Spot Instance usage. You can also take advantage of Reserved Instance and Savings Plans discounts by using them in conjunction with On-Demand Instances in the fleet.
Automated replacement of Spot Instances If your fleet includes Spot Instances, it can automatically request replacement Spot capacity if your Spot Instances are interrupted. Through Capacity Rebalancing, a fleet can also monitor and proactively replace your Spot Instances that are at an elevated risk of interruption.
Reserve On-Demand capacity A fleet can use an On-Demand Capacity Reservation to reserve On-Demand capacity. A fleet can also include Capacity Blocks for ML, allowing you to reserve GPU instances on a future date to support short duration machine learning (ML) workloads.
# Which is the best fleet method to use?
As a general best practice, we recommend launching fleets of Spot and On-Demand Instances with Amazon EC2 Auto Scaling because it provides additional features you can use to manage your fleet.
The list of additional features includes automatic health check replacements for both Spot and On- Demand Instances, application-based health checks, and an integration with Elastic Load Balancing to ensure an even distribution of application traffic to your healthy instances. You can also use Auto Scaling groups when you use AWS services such as Amazon ECS, Amazon EKS (self-managed node groups), and Amazon VPC Lattice. For more information, see the Amazon EC2 Auto Scaling User Guide.
If you can't use Amazon EC2 Auto Scaling, then you might consider using EC2 Fleet or Spot Fleet.
EC2 Fleet and Spot Fleet offer the same core functionality. However, EC2 Fleet is only available using a command line and does not provide console support. Spot Fleet provides console support, but is based on a legacy API with no planned investment.
Use the following table to determine which fleet method to use.

Fleet method When to use?
Use case Amazon EC2 Auto Scaling
- You need multiple instances with either a single configuration or a mixed configuration.
- You want to automate the lifecycle management of your instances.
Create an Auto Scaling group that manages the lifecycle of your instances while maintaini ng the desired number of instances. Supports horizontal scaling (adding more instances ) between specified minimum and maximum limits.
EC2 Fleet
- You need multiple instances with either a single configuration or a mixed configuration.
- You want to self-manage your instance lifecycle.
- If you don't need auto scaling, we recommend that you use an instant type EC2 Fleet.
Create an instant fleet of both On-Demand Instances and Spot Instances in a single operation, with multiple launch specifications that vary by instance type, AMI, Availability Zone, or subnet.
The Spot Instance allocation strategy defaults to lowest- price  per unit, but we recommend changing it to price-capacity-opt imized .
Spot Fleet
- We strongly discourage using Spot Fleet because it is based on a legacy API with no planned investmen t.
- If you want to manage your instance lifecycle, rather use EC2 Fleet.
- If you don't want to manage your instance Use Spot Fleet only if you need console support for a use case for when you would use EC2 Fleet.
