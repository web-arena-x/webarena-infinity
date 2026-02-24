# Use nested virtualization to run hypervisors in Amazon EC2 instances

Source: apps/user-manuals/aws/ec2-ug.pdf

---

# Use nested virtualization to run hypervisors in Amazon EC2 instances instances Nested virtualization allows you to run hypervisors such as Hyper-V and KVM inside virtual Amazon EC2 instances. Virtual EC2 instances are non-bare metal instances. This capability extends virtualization flexibility by adding processor-level virtualization support to virtual EC2 instances, enabling a hypervisor running in your instance to create and manage virtual machines.
Nested virtualization can help when you're running development tools like Docker Desktop, Windows Subsystem for Linux 2 (WSL2), Android Studio emulators, or QEMU in your development workflow, as it allows you to choose from a wide range of standard virtual Amazon EC2 instance types that meet your specific performance and price requirements.
There is no additional cost for using nested virtualization.
Contents
- How it works
- Considerations
- Launch a new instance with nested virtualization enabled
- Configure an existing instance to use nested virtualization
## How it works Virtual EC2 instances run on a physical host that has the Nitro hypervisor. To support nested virtualization, the Nitro System passes the processor extensions, such as Intel VT-x, to instances to facilitate running nested virtual machines. The nested virtualization architecture consists of three layers: the physical AWS infrastructure and Nitro hypervisor (L0), your EC2 instance running a hypervisor (L1), and one or more virtual machines created within that instance (L2).
## Considerations Before you begin using nested virtualization, consider the following:
- Supported instance types – Nested virtualization is currently supported on C8i, M8i, and R8i instances.
- Supported hypervisors – Currently, KVM and Hyper-V are the supported L1 hypervisors.
- Windows instances – When nested virtualization is enabled on a Windows instance:

- Credential Guard – Virtual Secure Mode (VSM) is automatically disabled.
- Hibernation – Instance hibernate and resume is not supported.
- CPU limit – Not supported on Windows instances with more than 192 CPUs, such as m8i.96xl.
- Security responsibilities – When using nested virtualization on EC2 instances, AWS is responsible for "security of the cloud," protecting the underlying infrastructure and maintaining the strong isolation boundaries between EC2 instances provided by the AWS Nitro System.
Customers are responsible for "security in the cloud," which includes securing the operating system, hypervisor, nested virtual machines, guest operating systems, applications, and data within the EC2 instances.
- Performance – AWS recommends that customers who want to run workloads that require access to hardware virtualization extensions, and are performance sensitive or have strict latency requirements, to evaluate bare metal instances.
## Launch a new instance with nested virtualization enabled When you launch a new instance, you can turn on nested virtualization to run hypervisors and virtual machines on it.
Prerequisites You must have the required IAM permissions to launch an Amazon EC2 instance.
Console To enable nested virtualization during instance launch
1. Follow the the section called "Launch using the launch instance wizard" procedure and configure your instance as needed.
2. Ensure a supported instance type is selected.
3. Expand Advanced details, and for Nested virtualization, choose Enable.
4. In the Summary panel, review your instance configuration, and then choose Launch instance.
AWS CLI To launch an instance with nested virtualization enabled

Use the run-instances command. aws ec2 run-instances \ --image-id ami-0abcdef1234567890 \ --instance-type r8i.4xlarge \ --cpu-options "NestedVirtualization=enabled" \ --key-name my-key-pair \ --placement "Tenancy=host"
PowerShell To launch an instance with nested virtualization enabled Use the New-EC2Instance command.
New-EC2Instance `
    -ImageId ami-0abcdef1234567890 `
    -InstanceType r8i.4xlarge `
    -CpuOption @{NestedVirtualization='enabled'} `
    -KeyName my-key-pair `
    -Placement_Tenancy host
## Configure an existing instance to use nested virtualization You can turn on nested virtualization on an existing Amazon EC2 instance.
Prerequisites
- The instance must be in a stopped state.
- The instance type must support nested virtualization.
Console To enable nested virtualization on an existing instance
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Instances.
3. Select the instance you want to modify from the instances table.
4. Choose Actions, Instance settings, Change CPU options.
