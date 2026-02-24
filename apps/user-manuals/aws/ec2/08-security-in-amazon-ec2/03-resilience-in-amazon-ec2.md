# Resilience in Amazon EC2

Source: apps/user-manuals/aws/ec2-ug.pdf

---

- Use AWS Systems Manager Session Manager to access your instances remotely instead of opening inbound SSH or RDP ports and managing key pairs.
- Use AWS Systems Manager Run Command to automate common administrative tasks instead of connecting to your instances.
- [Windows instances] Many of the Windows OS roles and Microsoft business applications also provide enhanced functionality such as IP Address Range restrictions within IIS, TCP/IP filtering policies in Microsoft SQL Server, and connection filter policies in Microsoft Exchange. Network restriction functionality within the application layer can provide additional layers of defense for critical business application servers.
Amazon VPC supports additional network security controls, such as gateways, proxy servers, and network monitoring options. For more information, see Control network traffic in the Amazon VPC User Guide.
# Resilience in Amazon EC2 The AWS global infrastructure is built around AWS Regions and Availability Zones. Regions provide multiple physically separated and isolated Availability Zones, which are connected through low-latency, high-throughput, and highly redundant networking. With Availability Zones, you can design and operate applications and databases that automatically fail over between zones without interruption. Availability Zones are more highly available, fault tolerant, and scalable than traditional single or multiple data center infrastructures.
If you need to replicate your data or applications over greater geographic distances, use AWS Local Zones. An AWS Local Zone is an extension of an AWS Region in geographic proximity to your users.
Local Zones have their own connections to the internet and support Direct Connect. Like all AWS Regions, AWS Local Zones are completely isolated from other AWS Zones.
If you need to replicate your data or applications in an AWS Local Zone, AWS recommends that you use one of the following zones as the failover zone:
- Another Local Zone
- An Availability Zone in the Region that is not the parent zone. You can use the describe- availability-zones command to view the parent zone.
For more information about AWS Regions and Availability Zones, see AWS Global Infrastructure.
