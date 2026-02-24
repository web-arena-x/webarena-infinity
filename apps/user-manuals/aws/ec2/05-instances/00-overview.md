# Amazon EC2 instances

Source: apps/user-manuals/aws/ec2-ug.pdf

---

# Amazon EC2 instances An Amazon EC2 instance is a virtual server in the AWS cloud environment. You have full control over your instance, from the time that you first start it (referred to as launching an instance) until you delete it (referred to as terminating an instance). You can choose from a variety of operating systems when you launch your instance. You can connect to your instance and customize it to meet your needs. For example, you can configure the operating system, install operating system updates, and install applications on your instance.
Amazon EC2 provides a wide range of instance types. You can choose an instance type that provides the compute resources, memory, storage, and network performance that you need to run your applications.
With Amazon EC2, you pay only for what you use. Billing for your instance starts when you launch your instance and it transitions to the running state. Billing stops when you stop your instance and resumes when you start your instance. When you terminate your instance, billing stops when it transitions to the shutting down state.
Amazon EC2 provides features that you can use to optimize the performance and the cost of your instances. For example, you can use Amazon EC2 Fleet or Amazon EC2 Auto Scaling to scale your capacity up or down as your instance utilization changes. You can reduce the costs for your instances using Spot Instances or Savings Plans.
A managed instance is managed by a service provider, such as Amazon EKS Auto Mode. You can't directly modify the settings of a managed instance. Managed instances are identified by a true value in the Managed field. For more information, see Amazon EC2 managed instances.
Features and tasks
- Amazon EC2 instance types
- Amazon EC2 managed instances
- Use nested virtualization to run hypervisors in Amazon EC2 instances
- Amazon EC2 billing and purchasing options
- Store instance launch parameters in Amazon EC2 launch templates
- Launch an Amazon EC2 instance
- Connect to your EC2 instance
