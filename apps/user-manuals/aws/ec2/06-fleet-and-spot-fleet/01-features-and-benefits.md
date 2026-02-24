# Features and benefits

Source: apps/user-manuals/aws/ec2-ug.pdf

---

EC2 Fleet and Spot Fleet EC2 Fleet and Spot Fleet are designed to be a useful way to launch a fleet of tens, hundreds, or thousands of Amazon EC2 instances in a single operation. Each instance in a fleet is either configured by a launch template or a set of launch parameters that you configure manually at launch.
Topics
- Features and benefits
- Which is the best fleet method to use?
- Configuration options for your EC2 Fleet or Spot Fleet
- Work with EC2 Fleet
- Work with Spot Fleet
- Monitor your EC2 Fleet or Spot Fleet
- Tutorials for EC2 Fleet
- Example CLI configurations for EC2 Fleet
- Example CLI configurations Spot Fleet
- Quotas for EC2 Fleet and Spot Fleet
# Features and benefits Fleets provide the following features and benefits, enabling you to maximize cost savings and optimize availability and performance when running applications on multiple EC2 instances.
Multiple instance types A fleet can launch multiple instance types, ensuring it isn't dependent on the availability of any single instance type. This increases the overall availability of instances in your fleet.
Distributing instances across Availability Zones A fleet can launch into multiple Availability Zones, enabling you to reduce costs and improve availability. If your fleet includes Spot Instances, the fleet automatically selects Availability Zones based on your preferences regarding price and interruptions.
