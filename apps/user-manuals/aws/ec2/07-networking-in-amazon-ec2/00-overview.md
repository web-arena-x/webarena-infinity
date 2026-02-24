# Networking in Amazon EC2

Source: apps/user-manuals/aws/ec2-ug.pdf

---

# Networking in Amazon EC2 Amazon VPC enables you to launch AWS resources, such as Amazon EC2 instances, into a virtual network dedicated to your AWS account, known as a virtual private cloud (VPC). When you launch an instance, you can select a subnet from the VPC. The instance is configured with a primary network interface, which is a logical virtual network card. The instance receives a primary private IP address from the IPv4 address of the subnet, and it is assigned to the primary network interface.
You can control whether the instance receives a public IP address from Amazon's pool of public IP addresses. The public IP address of an instance is associated with your instance only until it is stopped or terminated. If you require a persistent public IP address, you can allocate an Elastic IP address for your AWS account and associate it with an instance or a network interface. An Elastic IP address remains associated with your AWS account until you release it, and you can move it from one instance to another as needed. You can bring your own IP address range to your AWS account, where it appears as an address pool, and then allocate Elastic IP addresses from your address pool.
To increase network performance and reduce latency, you can launch instances in a placement group. You can get significantly higher packet per second (PPS) performance using enhanced networking. You can accelerate high performance computing and machine learning applications using an Elastic Fabric Adapter (EFA), which is a network device that you can attach to a supported instance type.
Features
- Regions and Zones
- Amazon EC2 instance IP addressing
- EC2 instance hostnames and domains
- Bring your own IP addresses (BYOIP) to Amazon EC2
- Elastic IP addresses
- Elastic network interfaces
- Amazon EC2 instance network bandwidth
- Enhanced networking on Amazon EC2 instances
- Elastic Fabric Adapter for AI/ML and HPC workloads on Amazon EC2
- Amazon EC2 topology
- Placement groups for your Amazon EC2 instances
