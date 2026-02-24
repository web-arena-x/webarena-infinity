# Monitor Amazon EC2 resources

Source: apps/user-manuals/aws/ec2-ug.pdf

---

# Monitor Amazon EC2 resources Monitoring is an important part of maintaining the reliability, availability, and performance of your Amazon EC2 instances and your AWS solutions. You should collect monitoring data from all of the parts in your AWS solutions so that you can more easily debug a multi-point failure if one occurs.
AWS provides various tools that you can use to monitor Amazon EC2. The Amazon EC2 and CloudWatch console dashboards provide an at-a-glance view of the state of your Amazon EC2 environment. In addition, we provide the following:
- System status checks – Monitor the AWS systems required to use your instance to ensure that they are working properly. These checks detect problems with your instance that require AWS involvement to repair. When a system status check fails, you can choose to wait for AWS to fix the issue or you can resolve it yourself (for example, by stopping and restarting or terminating and replacing an instance). Examples of problems that cause system status checks to fail include:
- Loss of network connectivity
- Loss of system power
- Software issues on the physical host
- Hardware issues on the physical host that impact network reachability For more information, see Status checks for Amazon EC2 instances.
- Instance status checks – Monitor the software and network configuration of your individual instance. These checks detect problems that require your involvement to repair. When an instance status check fails, typically you will need to address the problem yourself (for example, by rebooting the instance or by making modifications in your operating system). Examples of problems that may cause instance status checks to fail include:
- Failed system status checks
- Misconfigured networking or startup configuration
- Exhausted memory
- Corrupted file system
- Incompatible kernel For more information, see Status checks for Amazon EC2 instances.
- Amazon CloudWatch alarms – Watch a single metric over a time period you specify, and
