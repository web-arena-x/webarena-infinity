# Understand codes for Amazon EC2 in billing and usage reports

Source: apps/user-manuals/aws/ec2-ug.pdf

---

- Under Offer usage (monthly), take note of your usage of Linux instances, Windows instances, and EBS storage. The percentage indicates how much of your Free Tier limits you've used this month. If you're at 100%, you will incur charges for further use.
Note This information appears only after you've created an instance. However, usage information is not updated in real time; it's updated three times a day.
5. To avoid incurring further charges, delete any resources that are either incurring charges now, or will incur charges if you exceed your Free Tier limit usage.
- For the instructions to delete your instance, see Terminate Amazon EC2 instances.
- To check if you have resources in other Regions that might be incurring charges, in the EC2 Free Tier box, choose View Global EC2 resources to open the EC2 Global View. For more information, see View resources across Regions using AWS Global View.
6. To view your resource usage for all AWS services under the AWS Free Tier, at the bottom of the EC2 Free Tier box, choose View all AWS Free Tier offers. For more information, see Trying services using AWS Free Tier in the AWS Billing User Guide.
# Understand codes for Amazon EC2 in billing and usage reports When you use Amazon EC2, we include related codes in your AWS billing and usage reports.
Reviewing these codes helps you understand your costs and usage patterns for Amazon EC2.
Tracking and managing your expenses is essential for optimizing your costs.
The following tables describe the codes for Amazon EC2 that appear in your billing and usage reports. For a list of the Region codes used in the billing and usage reports, see AWS Region billing codes.
Billing codes for:
- Instances
- Bare metal instances
- Dedicated Hosts
- Dedicated Instances
- EBS optimization

- Capacity Reservations Related resources
- the section called "Billing and purchasing options"
- the section called "Understand AMI billing"
- Amazon EC2 pricing
## Instances Code Description Units region-BoxUsage :instance-type The running time for On-Demand Instances.
Hours region-HostBoxU sage :instance- type The running time for instances on Dedicated Hosts.
Hours region-SpotUsag e :instance-type The running time for Spot Instances.
Hours
## Bare metal instances Code Description Units region-BoxUsage :instance- family .metal The running time for bare metal On-Demand Instances.
Hours region-HostBoxU sage :instance- family .metal The running time for bare metal instances on Dedicated Hosts.
Hours

Code Description Units region-SpotUsag e :instance- family .metal The running time for bare metal Spot Instances.
Hours
## Dedicated Hosts Code Description Units region-HostUsag e :host-type The time that Dedicated Hosts are provision ed.
Hours region-Reserved HostUsage :host- type The time that Dedicated Host Reservations are applied.
Hours
## Dedicated Instances Code Description Units region-Dedicate dUsage :instance- type The running time for Dedicated Instances.
Hours + per-Region fee
## EBS optimization Code Description Units region-EBSOptim ized :instance- type The time that EBS optimization is enabled.
Hours
