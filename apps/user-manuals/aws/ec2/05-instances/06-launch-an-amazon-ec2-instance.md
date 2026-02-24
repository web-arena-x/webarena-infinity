# Launch an Amazon EC2 instance

Source: apps/user-manuals/aws/ec2-ug.pdf

---

Use the Remove-EC2TemplateVersion cmdlet and specify the version numbers to delete. You can specify up to 200 launch template versions to delete in a single request.
Remove-EC2TemplateVersion `
    -LaunchTemplateId lt-0abcd290751193123 `
    -Version 1
# Launch an Amazon EC2 instance An instance is a virtual server in the AWS Cloud. You launch an instance from an Amazon Machine Image (AMI). The AMI provides the operating system, application server, and applications for your instance.
When you create your AWS account, you can get started with Amazon EC2 for free using the AWS Free Tier. Your Free Tier benefits depend on when you created your AWS account. If your created your AWS account before July 15, 2025 and it's less than 12 months old, you can use the Free Tier to launch and use a t2.micro instance for free (in Regions where t2.micro is unavailable, you can use a t3.micro instance under the Free Tier). You incur charges for your instance or usage that counts against your Free Tier limits while the instance is running, even if it remains idle. For more information, see Amazon EC2 pricing. If you created your AWS account on or after July 15, 2025, you can use t3.micro, t3.small, t4g.micro, t4g.small, c7i-flex.large, and m7i- flex.large instance types for 6 months or until your credits are used up. For more information, see Free Tier benefits before and after July 15, 2025.
When you launch your instance, you can launch your instance in a subnet that is associated with one of the following resources:
- An Availability Zone – This option is the default.
- A Local Zone – To launch an instance in a Local Zone, you must opt in to the Local Zone, and then create a subnet in the zone. For more information, see Get started with Local Zones.
- A Wavelength Zone – To launch an instance in a Wavelength Zone, you must opt in to the Wavelength Zone, and then create a subnet in the zone. For information about how to launch an instance in a Wavelength Zone, see Get started with AWS Wavelength.
- An Outpost – To launch an instance in an Outpost, you must create an Outpost. For information about how to create an Outpost, see Get started with AWS Outposts.

After you launch your instance, you can connect to it and use it. To begin, the instance state is pending. When the instance state is running, the instance has started booting. There might be a short time before you can connect to the instance. Note that bare metal instance types might take longer to launch.
Depending on how you plan to connect to your instance, you might want to make certain configurations while launching your instance. These configurations could include specifying inbound security group rules for certain traffic or associating an instance profile role. For more information on the connection methods you can use to connect and their requirements, see Connect to your EC2 instance.
The instance receives a public DNS name that you can use to contact the instance from the internet. The instance also receives a private DNS name that other instances within the same VPC can use to contact the instance.
When you're finished with an instance, to avoid incurring unnecessary costs, be sure to terminate it.
For more information, see Terminate Amazon EC2 instances.
The following methods are some of the ways that you can launch an instance.
Method Tool Documentation Use the launch instance wizard to specify the launch parameters.
Amazon EC2 console Launch an EC2 instance using the launch instance wizard in the console Create a launch template and launch the instance from the launch template.
Amazon EC2 console Launch EC2 instances using a launch template Use an existing instance as the base.
Amazon EC2 console Launch an EC2 instance using details from an existing instance Use an AMI that you purchased from the AWS Marketplace.
Amazon EC2 console Launch an Amazon EC2 instance from an AWS Marketplace AMI

Method Tool Documentation Use an AMI that you specify.
AWS CLI Launching, listing, and deleting Amazon EC2 instances in the AWS CLI Use an AMI that you specify.
AWS Tools for Windows PowerShell Launch an Amazon EC2 Instance Using Windows PowerShell Use EC2 Fleet to provision capacity across different EC2 instance types and Availabil ity Zones, and across On- Demand Instance, Reserved Instance, and Spot Instance purchasing options.
AWS CLI EC2 Fleet and Spot Fleet Use a CloudFormation template to specify an instance.
AWS CloudFormation AWS::EC2::Instance in the AWS CloudFormation User Guide Use a language-specific AWS SDK to launch an instance.
AWS SDK AWS SDK for .NET AWS SDK for C++ AWS SDK for Go AWS SDK for Java AWS SDK for JavaScript AWS SDK for PHP V3 AWS SDK for Python AWS SDK for Ruby V3

## Tutorials for launching EC2 instances There are different ways to launch and configure an Amazon EC2 instance. The method and configuration you use depends on your specific use case.
The following tutorials can help you learn how to launch EC2 instances. If you're new to Amazon EC2, we recommend that you start with the first tutorial. The tutorials start by introducing you to the basics, and help you build on the basics by introducing more configuration options.
Objective Link to tutorial Launch my very first EC2 instance Learn how to quickly launch an Amazon EC2 instance by using the default settings in the Amazon EC2 launch instance wizard. Also learn how to review the instance configuration fields and terminate the instance.
Duration: 10 minutes Tutorial 1: Launch my very first Amazon EC2 instance Launch a test EC2 instance and connect to it Learn how to launch an Amazon EC2 instance that you can use for testing purposes. This instance will have no advanced configuration and won't store sensitive information. You will also learn about the essential instance configuration settings, how to connect to the instance, and how to stop it.
Duration: 30 minutes Tutorial 2: Launch a test EC2 instance and connect to it
### Looking for other tutorials?
- Tutorial: Install a LAMP server on AL2023
- Tutorial: Configure SSL/TLS on AL2023
- Tutorial: Host a WordPress blog on AL2023

- Tutorial: Complete the configuration required to connect to your instance using EC2 Instance Connect
- Tutorial: Connect an Amazon EC2 instance to an Amazon RDS database
### Tutorial 1: Launch my very first Amazon EC2 instance Tutorial objective Learn how to quickly launch an Amazon EC2 instance by using the default settings in the Amazon EC2 launch instance wizard. Also learn how to review the instance configuration fields and terminate the instance.
EC2 experience Beginner Duration 10 minutes Cost Free Tier eligible When you create your AWS account, you can get started with Amazon EC2 for free using the AWS Free Tier.
If you created your AWS account before July 15, 2025, it's less than 12 months old, and you haven't already exceeded the Free Tier benefits for Amazon EC2, it won't cost you anything to complete this tutorial, because we help you select options that are within the Free Tier benefits. Otherwise, you'll incur the standard Amazon EC2 usage fees from the time that you launch the instance (even if it remains idle) until you terminate it.
If you created your AWS account on or after July 15, 2025, it's less than 6 months old, and you haven't used up all your credits, it won't cost you anything to complete this tutorial,

because we help you select options that are within the Free Tier benefits.
For information on how to determine whether you're eligible for the Free Tier, see the section called "Track your Free Tier usage".
Prerequisites
- You must have an AWS account, configure a user with administrator access, and use the administrator user to sign into the AWS Management Console. Not sure how to do this? Try this tutorial: Setting Up Your AWS Environment
- You must have general familiarity with the AWS console. Not sure where to start? Try this getting started guide: Getting Started with the AWS Management Console
#### Tutorial overview This tutorial is designed for beginners with no prior experience using Amazon EC2. We'll guide you through the steps for creating—we call it launching—your very first EC2 instance using the EC2 console. An instance is essentially a web server in the AWS Cloud. After launching your instance, we'll show you how to find it in the console. Finally, to help you manage costs, we'll show you how to delete—we call it terminate—your instance.
This tutorial is divided into the following short tasks. You must complete each task before moving to the next one.
- Task 1: Launch your instance
- Task 2: Find your instance
- Task 3: View your instance configuration
- Task 4: Terminate your instance

#### Task 1: Launch your instance In this task, you'll take the quickest path to launching your instance by doing only the essentials.
We'll use the EC2 launch instance wizard, a web-based form that provides all the fields for configuring and launching your instance. It simplifies the process by providing default values for the instance configuration fields.
Before you start Make sure you've completed the prerequisites listed in the preceding table, including signing into the AWS Management Console with your administrator user.
Follow these steps to quickly launch your instance
1. Open the Amazon EC2 console:
Go to https://console.aws.amazon.com/ec2/.
2. Open the EC2 launch instance wizard:
From the EC2 dashboard, choose Launch instance.
The Launch an instance web-based form opens. This is the EC2 launch instance wizard.
3. Name your instance:
Under Name and tags, for Name, enter a descriptive name like My first EC2 instance.
While naming your instance isn't required, it helps identify your instance later.
4. Proceed without a key pair:
Under Key pair (login), for Key pair name, choose Proceed without a key pair (Not recommended).
A key pair can be used for secure login. However, because we won't be logging into the instance in this tutorial, you don't need a key pair for now.
5. Launch your instance:
In the Summary panel on the right, choose Launch instance.
Amazon EC2 quickly launches your instance using the default settings. A Success banner confirms the launch.

Congratulations! You've successfully launched your very first EC2 instance!
#### Task 2: Find your instance In this task, you'll locate the instance that you just launched in the EC2 console.
Follow these steps to find your instance in the EC2 console
1. Open the Instances page:
If you're still on the success page, choose Instances in the breadcrumb at the top of the screen.
You might need to choose the three ellipses first to access it.
If you've navigated away, choose Instances from the navigation pane.
2. Locate your instance:
In the Name column, find your instance by the name you gave it.
#### Task 3: View your instance configuration In this task, you'll become familiar with viewing your instance's configuration details.
Follow these steps to view your instance's configuration
1. Locate the instance ID:
In the Instance ID column, take note of your instance's unique ID. It begins with i– followed by 17 alphanumeric characters, for example, i-01aeed690c9fb5322.
The instance ID is automatically assigned to your instance when it's launched.
2. Open the instance details page:
In the Instance ID column, choose the ID link to open the instance details page where you can review its configuration.
3. Explore instance configuration details:
Take a few minutes to explore the configuration details of your instance. In the next tutorial, we'll dive deeper into the configuration. For now, use this time to familiarize yourself with the instance details page.
Tip: To quickly find a field, press Ctrl+F or command+F on your keyboard.

a.
Instance type: Can you find the instance type? It might be t3.micro, for example. b.
Public IPv4 address: Can you find the public IPv4 address that was allocated to your instance? It's in a format similar to the following example: 34.242.148.128. c.
Instance owner: Can you identify the owner of this instance? It's you! Your AWS account number is listed under the Owner field. d.
Instance tags: The name you gave your instance is actually a tag. Can you find your instance tags? Choose the Tags tab. The key is Name, and the value is the name you provided. e.
Launch time: Can you find when you launched your instance? Choose the Details tab and find the Launch time field. f.
Instance state: Can you verify the state of your instance? It should be Running.
Take a few more minutes to explore the other instance configuration fields. When you're ready, proceed to the next task.
#### Task 4: Terminate your instance Warning Terminating an instance is permanent and irreversible.
After you terminate an instance, you can no longer connect to it, and it can't be recovered.
All attached Amazon EBS volumes that are configured to be deleted on termination are also permanently deleted and can't be recovered. All data stored on instance store volumes is permanently lost. For more information, see How instance termination works.
Before you terminate an instance, ensure that you have backed up all data that you need to retain after the termination to persistent storage.
In this task, you'll delete your instance to preserve your Free Tier benefits. In EC2, terminate is the term used for deleting an instance.
Follow these steps to terminate your instance
1. Initiate termination:
If you're still on the instance details page, choose the Instance state menu (top right), and then choose Terminate (delete) instance.

If you've navigated away, choose Instances from the navigation pane. Then, on the Instances page, select the checkbox next to the name of your instance, and then choose the Instance state menu (top right), and choose Terminate (delete) instance.
2. Confirm termination:
In the Terminate (delete) instance window that opens, choose the Terminate (delete) button to confirm that you want to terminate your instance.
3. Monitor instance state:
On the Instances page, check the Instance state column. The state of your instance changes to Shutting-down. If you don't see the full text, try widening the column.
Once the instance has shut down, Amazon EC2 deletes the instance, and it disappears from the Instances page.
#### Key takeaways In this tutorial, you covered the following key concepts:
- Instance refers to an Amazon EC2 web server in the AWS Cloud.
- Launch refers to creating an EC2 instance.
- Terminate refers to deleting an EC2 instance.
- The EC2 launch instance wizard contains default values for instance configuration, allowing for a quick and easy instance launch.
- The instance ID is a unique identifier automatically assigned to your instance, while the instance name is an optional tag that you can assign for easier identification.
#### Next steps To build confidence in launching and terminating instances, consider repeating the steps in this tutorial. Be sure to terminate any instances that you launch to preserve your Free Tier benefits.
Once you're comfortable with these basics, move onto the next tutorial, which provides a deeper dive into key instance configuration fields.

### Tutorial 2: Launch a test EC2 instance and connect to it Tutorial objective Learn how to launch an Amazon EC2 instance that you can use for testing purposes. This instance will have no advanced configuration and won't store sensitive information. You will also learn about the essential instance configuration settings, how to connect to the instance, and how to stop it.
EC2 experience Beginner Duration 30 minutes Cost Free Tier eligible When you create your AWS account, you can get started with Amazon EC2 for free using the AWS Free Tier.
If you created your AWS account before July 15, 2025, it's less than 12 months old, and you haven't already exceeded the Free Tier benefits for Amazon EC2, it won't cost you anything to complete this tutorial, because we help you select options that are within the Free Tier benefits. Otherwise, you'll incur the standard Amazon EC2 usage fees from the time that you launch the instance (even if it remains idle) until you terminate it.
If you created your AWS account on or after July 15, 2025, it's less than 6 months old, and you haven't used up all your credits, it won't cost you anything to complete this tutorial, because we help you select options that are within the Free Tier benefits.

For information on how to determine whether you're eligible for the Free Tier, see the section called "Track your Free Tier usage".
Prerequisites Complete Tutorial 1: Launch my very first Amazon EC2 instance.
#### Tutorial overview This tutorial is designed for beginners who want to launch an EC2 instance that they can use for testing purposes.
We'll explain the key instance configuration fields, and then guide you through the steps for launching a test instance using the default values in the EC2 console. After launching your instance, we'll show you how to log into—we call it connect to—your instance. We'll also show you how to create a key pair, which is required for connecting to your instance in this tutorial. Finally, to help manage costs, we'll show you to stop your instance to avoid usage charges.
You'll launch a Linux instance in this tutorial. While the steps in this tutorial can be used for launching instances with other operating systems, the instructions for connecting to an instance are specific to Linux instances.
This tutorial is divided into the following short tasks. You must complete each task before moving to the next one.
- Task 1: Familiarize yourself with key components for launching an instance
- Task 2: Review a technical diagram
- Task 3: Create a key pair
- Task 4: Launch your test instance
- Task 5: Find your instance
- Task 6: View your instance configuration
- Task 7: Familiarize yourself with key components for connecting to an instance
- Task 8: Connect to your instance
- Task 9: Stop your instance

#### Task 1: Familiarize yourself with key components for launching an instance In this task, you'll explore the key components required to launch an EC2 instance. These are the AMI, instance type, key pair, security group, network (VPC and subnet), and Amazon EBS volume.
You'll also explore an optional component, the Name tag.
To help visualize these components, think of an instance like a rental house. Just as renting a house gives you a place to live without your needing to own and maintain the property, EC2 instances provide computing power without your needing to own and maintain the underlying infrastructure.
When deciding on the kind of instance to launch, you'll consider the configuration criteria for the instance, just as you would consider the criteria you want from a house. While this analogy simplifies things, it offers a helpful way to visualize the components until you're more familiar with them.
- AMI – House building materials and amenities: The Amazon Machine Image (AMI) determines the operating system and applications your instance starts with. This is like choosing the building materials (like brick, steel, or wood) and amenities (like appliances and furnishings) of your house. A base AMI is like an unfurnished house with basic appliances, while a custom AMI with pre-installed software is like a fully furnished house.
- Instance type – House size and power: The instance type defines the size and capabilities of your EC2 instance, much like choosing the size of a house, number of rooms, and energy capacity. Each instance type determines the amount of CPU, memory, storage, and networking capacity of your instance. The selected AMI might limit what instance types you can choose.
- Key pair – Front door key: A key pair is like the lock and key to the front door of your house.
The public key acts as the lock on your instance, while the private key is the key you must keep securely on your local computer. If someone else gets hold of your private key, they can access your instance, much like how someone with your front door key can enter your house.
- Network (VPC and subnet) – Property boundary, sectioned areas, and house number: Your virtual private cloud (VPC) is like the entire property where your house is located, and the subnet is the sectioned-off area around the house. If you have multiple houses (instances) on your property, you might want to section them off into distinct areas (different subnets) depending on their purpose. Some houses allow visitors to roam freely through the gardens (public subnets with internet access), while others have fenced-off gardens to restrict entry (private subnets without internet access). Each subnet contains a range of IP addresses, much like house numbers, which can be assigned to instances within the subnet.

- Security group – The gatekeeper: The security group acts like a gatekeeper, controlling who is allowed to visit your house. It enforces a set of rules that controls what traffic is allowed to reach your instance. For example, a rule that allows SSH traffic from a specific IP address is like the gatekeeper letting in only a specific person to deliver groceries. Similarly, allowing HTTPS traffic from anywhere is like letting the public come and take a look at the exterior of your house.
- Amazon EBS volume – Storage units: EBS volumes are like storage units where you can store your belongings. Each instance has a root volume (where the AMI is stored), and you can add more volumes (storage) at any time as needed.
- Name tag – The house name: The Name tag functions like a sign on a house, helping you easily identify who lives there. While the Name tag makes it easier to distinguish between instances, it's not required when launching an instance.
#### Task 2: Review a technical diagram In this task, you'll become familiar with a typical technical diagram that we use in the AWS documentation. The following diagram represents the configuration for the test instance you'll launch in this tutorial. In the previous task, we introduced these components using the analogy of a rental house. Now, we'll focus on the actual EC2 components themselves. The numbered labels correspond to the descriptions that follow.

1. AMI – The AMI is the image you choose when launching an instance. It's a template that contains the operating system and software to run on your instance. For example, if you want to launch a Linux instance, you can choose the Amazon Linux 2023 AMI. Or, if you want to launch a Windows instance, you can choose the Microsoft Windows Server 2022 Base AMI. The AMI catalog in the Amazon EC2 console contains 1000s of images to choose from.
2. Instance type – The instance type is the hardware that determines the CPU, memory, storage, and networking capacity of the host computer used for your instance. Amazon EC2 offers over 600 instance types to choose from, each varying in hardware configuration and size, allowing you to choose the best fit for your application's needs.
3. Key pair – A key pair is set of security credentials that you use to prove your identity when connecting to your instance. The public key is on your instance and the private key is on your local computer.
In EC2, connecting to your instance refers to logging into your instance from your local computer.
While there are other ways to securely connect to your instance, in this tutorial we use a key pair.

4. Network – The network is made up of a VPC and one or more subnets. A VPC is a virtual network within the AWS Cloud. Every AWS customer has their own VPC dedicated to their AWS account. You'll launch your instance into a subnet in your VPC. A subnet is a range of IP addresses within a VPC. Your default subnet is a public subnet, which means it will assign a public IP address and provide internet access to your instance from outside the Amazon network.
5. Security group – A security group acts as a firewall to control the traffic to your instance. A security group contains rules that allow certain types of traffic to enter your instance. To connect through SSH from your local computer to your instance (using your key pair), you need a rule that allows SSH traffic from your local computer.
6. EBS volume – An Amazon EBS volume is a storage device that functions like a physical hard drive. Your instance comes with a root volume, which is a special EBS volume that stores the AMI with the operating system and software needed to boot your instance. You can optionally add data volumes. However, since your test instance won't store any sensitive data, you don't need additional encrypted data volumes.
Congratulations! You've completed the conceptual tasks in this tutorial. In the following tasks, you'll use the Amazon EC2 console to create the components you've learned about.
#### Task 3: Create a key pair In this task, you'll create a key pair. A key pair consists of two parts: a public key, which you'll add to your instance, and a matching private key, which you'll use to securely connect to your instance.
In the next task, you'll select this key pair when launching your instance, which automatically adds the public key to the instance. It's crucial to store the private key securely on your local computer, because anyone with access to it can connect to your instance.
If you prefer to use an existing key pair when you launch your test instance, feel free to skip this task. Otherwise, proceed to create a new key pair.
Before you start Make sure you've completed the prerequisites listed in the preceding table, including signing into the AWS Management Console with your administrator user.
Follow these steps to create a key pair
1. Open the Amazon EC2 console:

Go to https://console.aws.amazon.com/ec2/.
2. Navigate to the Key pairs console page:
In the navigation pane, under Network & Security, choose Key Pairs.
- If you previously created key pairs, they appear in the table.
- If no key pairs exist, the table is empty.
3. Create a new key pair:
Choose the Create key pair button (top right) to open the Create key pair web-based form, and enter your key pair details, as follows: a.
Name your key pair: For Name, enter a name that will help you recognize the key pair, like test-instance-key-pair.
The name can be up to 255 ASCII characters long. It can't include leading or trailing spaces. b.
Choose the key pair type: For Key pair type, choose ED25519.
Linux instances support both RSA and ED25519 key types, while Windows instances support only RSA. Since you'll be launching a Linux instance in this tutorial, you can use an ED25519 key. c.
Choose the private key file format: For Private key file format, choose .pem.
This is the format in which your private key file will be saved.
4. Save the public key to Amazon EC2 and download the private key:
Choose the Create key pair button (bottom right).
Amazon EC2 saves the public key, while your browser downloads the private key file automatically to your local computer. The file is named according to the name that you specified for the key pair, and the extension is the file format that you chose. Move the private key file to a secure location on your computer.
Important This is the only chance you'll have to save the private key file.

5. Set the permissions on the key (for macOS and Linux users):
If you plan to connect to your instance using SSH on a macOS or Linux computer, you must set the correct permissions for your private key file. Open a terminal window and run the following command, replacing test-instance-key-pair with the name of your key pair: chmod 400 test-instance-key-pair.pem This command ensures that only you can read the private key file, which is necessary for establishing a secure connection to your instance. Without these permissions, you won't be able to connect using this key pair.
Congratulations! You've successfully created a key pair!
#### Task 4: Launch your test instance In this task, you'll quickly launch a test instance using the EC2 launch instance wizard. You'll configure the main instance configuration settings for a Linux instance and use the default values for the other fields.
To help you manage costs, we recommend choosing Free tier eligible components.
Follow these steps to launch a test instance
1. Open the Amazon EC2 console:
Go to https://console.aws.amazon.com/ec2/.
2. Open the EC2 launch instance wizard:
From the EC2 dashboard, choose Launch instance.
The Launch an instance web-based form opens. This is the EC2 launch instance wizard.
3. Name your instance:
Under Name and tags, for Name, enter a descriptive name like Test instance.
The instance name is a tag, where the key is Name, and the value is the name that you specify.
Tip: For test instances, a name tag is sufficient. However, for production instances, it's best practice to establish a tagging policy to standardize tagging across all your resources.

4. Choose your operating system and software—the Amazon Machine Image (AMI):
Under Application and OS Images (Amazon Machine Image), for Amazon Machine Image (AMI), the default selection is Amazon Linux 2023 AMI. This AMI is marked Free tier eligible.
In this tutorial, you'll be launching a Linux instance, so leave the default setting to keep under the Free Tier limits.
5. Choose your hardware—the instance type:
Under Instance type, for Instance type, keep the default selection for this tutorial. The default instance type can be used under the Free Tier and its hardware is suitable for your test instance.
6. Prepare for secure login with a key pair:
Under Key pair (login), for Key pair name, choose the key pair you created in the previous task. If you don't see your key pair in the list, choose the refresh icon (to the right of the list).
When your instance launches, it will place the public key on the instance. To connect to your instance after it has launched, you'll use the corresponding private key that you downloaded in the previous task.
7. Configure the network settings to enable internet access:
Under Network settings, the Network (your VPC) and Subnet fields are configured by default.
Keep the default settings for this tutorial to help you get started quickly. If you haven't modified your default subnet, your instance will have internet access.
Tip: Your default subnet is a public subnet, which means it will assign a public IP address and provide internet access to your instance from outside the Amazon network. For test instances, it's okay to use the default subnet settings that provide internet access. However, for production instances, it's best practice to only assign a public IP address and use a subnet with internet access when absolutely necessary.
8. Set up the instance firewall (security group):
Under Network settings, under Firewall (security groups), keep the checkbox Allow SSH traffic from Anywhere (0.0.0.0) selected. This will create a new security group for your test instance that allows SSH traffic from any IP address.

A security group acts as a firewall to control the traffic to your instance. To connect through SSH from your local computer to your instance, you need a rule that allows SSH traffic from your local computer.
Tip: The IP address of your local computer might change over time if your internet service provider uses dynamic IP assignment. We're assuming that when you use an instance for testing purposes, you won't use the instance to store sensitive information, and therefore security measures can be less restrictive. For test instances, it's generally acceptable to allow traffic from any IP address (0.0.0.0/0) so that you can always connect even if your IP address changes. However, for production instances, especially those with sensitive data, it's best practice to allow traffic only from known IP addresses.
9. Configure the instance storage:
Under Configure storage, the Root volume (Encrypted) fields are configured by default. Leave the settings as they are to keep under the Free Tier limits.
Since our test instance won't store any sensitive data, we don't need additional encrypted data volumes.
10. Review the instance configuration:
In the Summary panel on the right, you can review your high-level settings before launching your instance.
11. Launch your instance:
When you're ready to launch your instance, in the Summary panel, choose Launch instance.
Amazon EC2 quickly launches your instance using the settings that you specified. If you didn't specify a setting, the default is used. A Success banner confirms the launch.
Congratulations! You've successfully launched your test instance!
#### Task 5: Find your instance In this task, you'll locate the instance that you just launched in the EC2 console.
Follow these steps to find your instance in the EC2 console
1. Open the Instances page:

If you're still on the success page, choose the instance ID in the Success banner.
If you've navigated away, choose Instances from the navigation pane.
2. Locate your instance:
In the Name column, find your instance by the name you gave it.
#### Task 6: View your instance configuration In this task, you'll become familiar with viewing your instance's configuration details.
Follow these steps to view your instance's configuration
1. Locate your instance:
In the Name column, find your instance by the name you gave it.
2. Open the instance details page:
Select the checkbox next to the name of your instance, and then choose the Actions menu (top right), and choose View details to open the instance details page where you can review its configuration.
In the previous tutorial, you chose the instance's ID link to open the instance details page.
You'll discover that there's more than one way to accomplish a task in the EC2 console.
3. Explore instance configuration details:
Take a few minutes to explore the configuration details of your instance.
Tip: To quickly find a field, press Ctrl+F or command+F on your keyboard. a.
AMI: Can you find the AMI that you used to launch your instance? You can find the information in AMI ID and AMI name on the Details tab. b.
Instance type: Can you find the instance type? It's might be t3.micro, for example. c.
Key pair: Can you find the key pair that you selected when you launched your instance?
It's specified for Key pair assigned at launch. Note that if you change the key pair in the future, the value here won't change.

d.
VPC: Can you find the ID of your VPC? You'll find all networking-related configuration settings on the Networking tab. The VPC ID is in a format similar to the following example: vpc-1a2b3c4d e.
Subnet: Can you find the ID of the subnet in which you launched your instance? It's in a format similar to the following example: subnet-1a2b3c4d f.
Public IPv4 address: Can you find the public IPv4 address that was allocated to your instance? It's in a format similar to the following example: 34.242.148.128. g.
Security group: Can you find the inbound rule that was created to allow SSH traffic from anywhere (0.0.0.0./0)? You'll find all security-related configuration settings on the Security tab. h.
Storage: Can you find the volume that was created for this instance? You'll find all storage-related configuration settings on the Storage tab. i.
Instance tags: The name you gave your instance is actually a tag. Can you find your instance tags? Choose the Tags tab. The key is Name, and the value is the name you provided. j.
Instance state: Can you verify the state of your instance? It should be Running.
Take a few more minutes to explore the other instance configuration fields. When you're ready, proceed to the next task.
#### Task 7: Familiarize yourself with key components for connecting to an instance In this task, you'll explore the key components required to connect to an EC2 instance. These are the connection protocol, public DNS, security group, key pair, and instance username.
To help visualize these components, think of connecting to an instance like going to your house:
- Connection protocol – Your mode of transport: Just like choosing how to get home, you choose the connection protocol that will take you to your instance. In this tutorial, we'll use SSH (Secure Shell), which creates a secure tunnel for connecting your computer to your instance over the internet.
- Public DNS – The house address: Just like your house has a unique address, your EC2 instance has its own public DNS name (for example, ec2-18-201-118-201.eu- west-1.compute.amazonaws.com). This public DNS name enables SSH to connect directly to your instance.

- Security group – The gatekeeper: Imagine your house has a gatekeeper who controls who may enter or leave. Similarly, the EC2 instance has a security group that acts like a gatekeeper, controlling which types of network traffic are allowed in or out of your instance. Only the traffic you explicitly permit (for example, SSH traffic from your computer's IP address) is allowed in.
- Private key – Your front door key: When you launched the instance, you specified a key pair.
The public key was placed on the instance, and you kept the private key on your computer. The private key acts as your front door key—without it, you can't get into your instance.
- Instance username – The resident: When you arrive at your house, you need to identify yourself to prove you're a resident. Similarly, when connecting to an instance, you provide a username.
Different instances have different default usernames, depending on their operating system. For example, Amazon Linux instances use ec2-user as the default username.
The connection command To connect to your EC2 instance, use the following command in a terminal window: ssh -i "test-instance-key-pair.pem" ec2-user@ec2-18-201-118-201.eu- west-1.compute.amazonaws.com Here's a breakdown of what the command does:
- ssh – This command specifies the connection protocol, initiating an SSH (Secure Shell) connection to your instance.
- -i "test-instance-key-pair.pem" – The -i flag indicates the private key file needed to authenticate the connection. This private key file must match the key pair you specified when launching the instance. If your private key file is saved in a specific folder, specify the full path to the file.
- ec2-user – This is the username for logging into the instance. For Amazon Linux instances, the default username is ec2-user. Other AMIs might use different default usernames, such as ubuntu for Ubuntu instances.
- @ – This symbol separates the username from the instance's address.
- ec2-18-201-118-201.eu-west-1.compute.amazonaws.com – This is the public address of your instance (the public DNS), which includes the public IPv4 address and the AWS Region. It uniquely identifies the instance.
What happens when you run the command

After you run the command, SSH establishes a secure tunnel and authenticates with your private key. If the instance's security group permits the traffic, you gain access to your EC2 instance. You can now control the instance from your computer as if you were sitting right in front of it. You can run commands, install software, and manage files—just like you would on your local machine.
#### Task 8: Connect to your instance In this task, you'll connect to your instance using an SSH client on your computer. In the previous task, we introduced the components for connecting to an instance using the analogy of going to your house. Now, we'll focus on connecting to the actual EC2 instance.
There are different ways to connect to an instance. The method you use to connect depends on the instance's operating system. Since you've launched a Linux instance, you'll use an SSH client on your local computer.
First, check if your computer has an SSH client installed Most computers come with an SSH client pre-installed. To check, open a terminal window on your computer and run the following command: ssh If the command is recognized, you're ready to connect.
If the command isn't recognized, you must install an SSH client. Instructions for installing an SSH client are beyond the scope of this tutorial. If you need help, see SSH connection prerequisites in this user guide or search online for instructions on how to install an SSH client on your operating system.
Follow these steps to connect to your instance
1. Initiate connecting:
If you're on the instance details page in the Amazon EC2 console, choose the Connect button (top right).
If you've navigated away, choose Instances from the navigation pane. Then, on the Instances page, select the checkbox next to the name of your instance and choose the Connect button (top right).
This opens the Connect to instance page.

2. Choose the connection method:
On the Connect to instance page, choose the SSH client tab.
Take a moment to review the text on this page, as these are the steps that you'll follow next.
3. Review the SSH command:
Under Example, you'll see a command that is automatically generated and customized with your instance's details. The private key name is derived from the name of the public key specified at launch.
The command looks something like this: ssh -i "test-instance-key-pair.pem" ec2-user@ec2-18-201-118-201.eu- west-1.compute.amazonaws.com
4. Copy the SSH command:
Choose the copy icon next to the example SSH command.
5. Open a terminal window:
On your local computer, open a terminal window.
6. Paste and run the SSH command:
Paste the SSH command into the terminal window. If you saved your private key file in a specific folder, edit the command to include the full file path.
Press Enter on your keyboard.
You'll see a response similar to the following:
The authenticity of host 'ec2-18-201-118-201.eu-west-1.compute.amazonaws.com (18-201-118-201)' can't be established.
ED25519 key fingerprint is SHA256:examplehxj9aOr1MogvKOoMNskVVIRBQBoq0example.This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])?
7. Complete the connection:
Enter yes and press Return on your keyboard.

Verifying the fingerprint is beyond the scope of this tutorial. To learn more, see (Optional) Get the instance fingerprint.
Upon a successful connection, the terminal prompt changes to display your instance's public DNS.
Congratulations! You've successfully connected to your instance!
#### Task 9: Stop your instance In this task, you'll stop your instance to preserve your Free Tier benefits. When your instance is stopped, you stop incurring costs for it. If you created your AWS account before July 15, 2025 and your qualify for the Free Tier, you will continue to incur costs for the EBS storage.
Follow these steps to stop your instance
1. Initiate stopping:
If you're still on the Connect to instance page, choose Instances from the breadcrumb. If you've navigated away, choose Instances from the navigation pane.
Then, on the Instances page, select the checkbox next to the name of your instance, and then choose the Instance state menu (top right), and choose Stop instance. When prompted, choose Stop.
2. Monitor instance state:
On the Instances page, check the Instance state column. The state of your instance changes to Stopping and then Stopped. If you don't see the full text, try widening the column.
If you think the instance state has changed from Stopping to Stopped, but you don't see it yet, choose the refresh icon (above the table) to refresh the Instances table.
#### Key takeaways In this tutorial, you covered the following key concepts:
- AMI refers to an Amazon Machine Image, which is a template that contains the operating system and software required to launch an instance.

- Instance type refers to the hardware of the host computer used for your instance. It determines the CPU, memory, storage, and networking capacity of your instance.
- Key pair refers to the set of public and private keys that you can use for securely connecting to your instance.
- Network refers to a VPC (a virtual private cloud dedicated to your account within the AWS Cloud) and a subnet (a range of IP addresses within your VPC).
- Security group refers to a set of rules that controls what traffic can reach your instance.
- EBS volume refers to the data storage for your instance. Every instance has a root volume for storing the AMI and one or more optional data volumes.
- Tags are metadata that you can optionally assign to your instance. The instance name is a tag, whose Key is Name, and the Value is your choice.
- Connecting refers to accessing your instance over the internet.
- SSH refers to the Secure Shell connection protocol that you can use to connect to your instance.
- Public DNS is your instance's unique public address.
- Instance username is determined by the operating system of your instance and required for connecting.
- Stopping your instance stops the charges for the instance, but EBS storage charges continue.
#### Next steps To build confidence in launching, connecting to, and stopping instances, consider repeating the steps in this tutorial. Be sure to terminate any instances that you launch to preserve your Free Tier benefits.
Once you're comfortable with these basics, you can explore more advanced tutorials. For more tutorials, see Looking for other tutorials?
If you created your AWS account before July 15, 2025, consider watching the following 6-minute video: How can I avoid charges on my account when using AWS Free Tier services If you created your AWS account on or after July 15, 2025, consider reviewing the following information: Explore AWS services with AWS Free Tier in the AWS Billing User Guide
## Reference for Amazon EC2 instance configuration parameters The launch instance wizard and launch template in the Amazon EC2 console provide all the parameters for configuring an Amazon EC2 instance.

Except for the key pair, the launch instance wizard provides a default value for each parameter. You can accept any or all of the defaults, or configure an instance with your own values. When creating a launch template, the parameters are optional. If you use a launch template to launch an instance, the parameters specified in the launch template override the default values in the launch instance wizard. Any parameter not specified in the launch template will default to the value provided by the launch instance wizard.
The parameters are grouped in the launch instance wizard and launch template. The following descriptions are presented according to the parameter groupings in the console.
Parameters for instance configuration
- Name and tags
- Application and OS Images (Amazon Machine Image)
- Instance type
- Key pair (login)
- Network settings
- Configure storage
- Advanced details
- Summary
### Name and tags The instance name is a tag, where the key is Name, and the value is the name that you specify. You can tag the instance, volumes, and network interfaces. For Spot Instances, you can tag the Spot Instance request only. For information about tags, see Tag your Amazon EC2 resources.
Specifying an instance name and additional tags is optional.
- For Name, enter a descriptive name for the instance. If you don't specify a name, the instance can be identified by its ID, which is automatically generated when you launch the instance.
- To add additional tags, choose Add additional tags. Choose Add tag, and then enter a key and value, and select the resource type to tag. Choose Add tag again for each additional tag to add.
You can only specify the instance name when launch an instance. You can't name the instance when you create a launch template, but you can add tags for the resources that are created when the instance is launched.

### Application and OS Images (Amazon Machine Image)
An Amazon Machine Image (AMI) contains the information required to create an instance. For example, an AMI might contain the software that's required to act as a web server, such as Linux, Apache, and your website.
You can find a suitable AMI as follows. With each option for finding an AMI, you can choose Cancel (at top right) to return to the launch instance wizard without choosing an AMI.
Search bar To search through all available AMIs, enter a keyword in the AMI search bar and then press Enter. To select an AMI, choose Select.
Recents The AMIs that you've recently used.
Choose Recently launched or Currently in use, and then, from Amazon Machine Image (AMI), select an AMI.
My AMIs The private AMIs that you own, or private AMIs that have been shared with you.
Choose Owned by me or Shared with me, and then, from Amazon Machine Image (AMI), select an AMI.
Quick Start AMIs are grouped by operating system (OS) to help you get started quickly.
First select the OS that you need, and then, from Amazon Machine Image (AMI), select an AMI.
To select an AMI that can be used under the AWS Free Tier, make sure that the AMI is marked Free tier eligible.
Browse more AMIs Choose Browse more AMIs to browse the full AMI catalog.
- To search through all available AMIs, enter a keyword in the search bar and then press Enter.
- To find an AMI by using a Systems Manager parameter, choose the arrow button to the right of the search bar, and then choose Search by Systems Manager parameter. For more information, see Reference AMIs using Systems Manager parameters.

- To search by category, choose Quickstart AMIs, My AMIs, AWS Marketplace AMIs, or Community AMIs.
The AWS Marketplace is an online store where you can buy software that runs on AWS, including AMIs. For more information about launching an instance from the AWS Marketplace, see Launch an Amazon EC2 instance from an AWS Marketplace AMI. In Community AMIs, you can find AMIs that AWS community members have made available for others to use. AMIs from Amazon or a verified partner are marked Verified provider.
- To filter the list of AMIs, select one or more check boxes under Refine results on the left of the screen. The filter options are different depending on the selected search category.
- Check the Root device type listed for each AMI. Notice which AMIs are the type that you need: either ebs (backed by Amazon EBS) or instance-store (backed by instance store). For more information, see Root volume type.
- Check the Virtualization type listed for each AMI. Notice which AMIs are the type that you need: either hvm or paravirtual. For example, some instance types require HVM. For more information about Linux virtualization types, see Virtualization types.
- Check the Boot mode listed for each AMI. Notice which AMIs use the boot mode that you need: either legacy-bios, uefi, or uefi-preferred. For more information, see Instance launch behavior with Amazon EC2 boot modes.
- Choose an AMI that meets your needs, and then choose Select.
Warning when changing the AMI When you launch an instance, if you modify the configuration of any volumes or security groups associated with the selected AMI, and then you choose a different AMI, a window opens to warn you that some of your current settings will be changed or removed. You can review the changes to the security groups and volumes. Furthermore, you can either view which volumes will be added and deleted, or view only the volumes that will be added. This warning does not appear when creating a launch template.
### Instance type The instance type defines the hardware configuration and size of the instance. Larger instance types have more CPU and memory. For more information, see Amazon EC2 instance types.
- Instance type: Ensure that the instance type is compatible with the AMI that you've specified. For more information, see Amazon EC2 instance types.

Free Tier – You can use instance types that are labeled Free tier eligible for free under the Free Tier. The specific instance types depend on when you created your AWS account.
If your created your AWS account before July 15, 2025 and it's less than 12 months old, you can use Amazon EC2 under the Free Tier by selecting the t2.micro instance type, or the t3.micro instance type in Regions where t2.micro is unavailable. Be aware that when you launch a t3.micro instance, it defaults to Unlimited mode, which might incur additional charges based on CPU usage.
If you created your AWS account on or after July 15, 2025, you can use t3.micro, t3.small, t4g.micro, t4g.small, c7i-flex.large, and m7i-flex.large instance types for 6 months or until your credits are used up.
For more information, see Free Tier benefits before and after July 15, 2025.
- Compare instance types: You can compare different instance types by the following attributes: number of vCPUs, architecture, amount of memory (GiB), amount of storage (GB), storage type, and network performance.
- Get advice: You can get guidance and suggestions for instance types from the EC2 instance type finder. For more information, see Get recommendations from EC2 instance type finder.
- (Launch templates only) Advanced: To specify instance attributes and let Amazon EC2 identify the instance types with those attributes, choose Advanced, and then choose Specify instance type attributes.
- Number of vCPUs: Enter the minimum and maximum number of vCPUs for your compute requirements. To indicate no limits, enter a minimum of 0, and leave the maximum blank.
- Amount of memory (MiB): Enter the minimum and maximum amount of memory, in MiB, for your compute requirements. To indicate no limits, enter a minimum of 0, and leave the maximum blank.
- Expand Optional instance type attributes and choose Add attribute to express your compute requirements in more detail. For information about each attribute, see InstanceRequirementsRequest in the Amazon EC2 API Reference.
- Resulting instance types: You can preview the instance types that match the specified attributes. To exclude instance types, choose Add attribute, and from the Attribute list, choose Excluded instance types. From the Attribute value list, select the instance types to exclude.

### Key pair (login)
For Key pair name, choose an existing key pair, or choose Create new key pair to create a new one.
For more information, see Amazon EC2 key pairs and Amazon EC2 instances.
Important If you choose the Proceed without key pair (Not recommended) option, you won't be able to connect to the instance unless you choose an AMI that is configured to allow users another way to log in.
### Network settings The network settings define the IP addresses, security groups, and network interfaces for your instances. You can use the default network settings or configure them as needed.
- (Launch instance wizard only) VPC: Choose an existing VPC for your instance. The default VPC for the Region is selected by default. Alternatively, you can choose a VPC that you created or that was shared with you. For more information, see Virtual private clouds for your EC2 instances.
- Subnet: Choose a subnet for your instance or choose Create new subnet to create a new subnet using the Amazon VPC console.
- You can create a subnet in any Availability Zone, Local Zone, Wavelength Zone, or Outpost Zone for the selected VPC.
- To launch the instance in an IPv6-only subnet, the instance must be a Nitro-based instance.
- (Launch instance wizard only) Auto-assign Public IP: Enable or disable auto-assignment of public IPv4 addresses. When launching instances into a default subnet, the default value is Enable. When launching instances into a nondefault subnet the default value is Disable. For more information, see Public IPv4 addresses.
You can't enable this option for nondefault subnets if you add a secondary network interface. For more information, see the section called "Assign a public IPv4 address at launch".
- (Launch instance wizard only) Auto-assign IPv6 IP: Enable or disable auto-assignment of IPv6 addresses. For more information, see IPv6 addresses.
- Firewall (security groups): Choose an existing security group or create a new one. Ensure that your security group has rules that allow traffic to and from your instances. All other traffic is ignored.

If you create a new security group, we automatically create an inbound rule that allows you to connect to your instance from all IP addresses over SSH (Linux instances) or RDP (Windows instances. You can remove or modify this rule as needed. You can add rules as needed. For more information, see Configure security group rules.
Warning Rules that enable all IP addresses to access your instance over SSH or RDP are acceptable if you are briefly launching a test instance and will stop or terminate it after a short time.
They are unsafe for production environments. You should authorize only a specific IP address range to access your instances.
This security group is added to the primary network interface and any secondary network interfaces. You can select additional security groups for your network interfaces, but you can't remove the one that you select here.
- Advanced network configuration – You can configure the primary network interface as needed.
To add a secondary network interface, choose Add network interface. The number of network interfaces that you can add depends on the instance type that you selected. Note that this section is available only if you choose a subnet.
- Device index: The device index. The primary network interface must be assigned to index 0.
- Network interface: The network interface. Select New interface to let Amazon EC2 create a new interface, or select an existing, available network interface. If you select an existing network interface as the primary network interface, you can't enable Auto-assign Public IP for nondefault subnets.
- Description: A description for the new network interface.
- Subnet: The subnet in which to create the new network interface. The instance is launched in the same subnet as the primary network interface.
You must choose a subnet for a secondary network interface from the same Availability Zone as the subnet for the primary network interface. If you select a subnet from another VPC, the label Multi-VPC appears next to the network interface. This enables you to create multi- homed instances across VPCs with different networking and security configurations.
To launch an EC2 instance into an IPv6-only subnet, you must use a Nitro-based instance.
When launching an IPv6-only instance, it is possible that DHCPv6 might not immediately

provide the instance with the IPv6 DNS name server. During this initial delay, the instance might not resolve public domains. You can change the configuration file and re-image your AMI so that the file has the IPv6 DNS name server address immediately on booting.
- Security groups: The security groups to associate with the network interface. You must choose a security group from the same VPC as the subnet for the network interface.
- (Launch templates only) Auto-assign public IP: Specify whether your instance receives a public IPv4 address. By default, instances in a default subnet receive a public IPv4 address and instances in a nondefault subnet do not. You can select Enable or Disable to override the subnet's default setting. For more information, see Public IPv4 addresses.
- Primary IP: A private IPv4 address from the range of your subnet. Leave blank to let Amazon EC2 choose a private IPv4 address for you.
- Secondary IP: Additional private IPv4 addresses from the range of your subnet. Choose Manually assign and enter an IPv4 address. Choose Add IP to add another IPv4 address.
Alternatively, choose Automatically assign and enter a value to indicate the number of IPv4 addresses that Amazon EC2 chooses for you.
- (IPv6-only) IPv6 IPs: IPv6 addresses from the range of the subnet. Choose Manually assign and enter an IPv6 address. Choose Add IP to add another IPv6 address. Alternatively, choose Automatically assign and enter a value to indicate the number of IPv6 addresses that Amazon EC2 chooses for you.
- IPv4 Prefixes: The IPv4 prefixes for the network interface. Choose Manually assign and enter an IPv4 prefix. Alternatively, choose Automatically assign and enter a value to indicate the number of IPv4 prefixes that Amazon EC2 chooses for you.
- IPv6 Prefixes: The IPv6 prefixes for the network interface. Choose Manually assign and enter an IPv6 prefix. Alternatively, choose Automatically assign and enter a value to indicate the number of IPv6 prefixes that Amazon EC2 chooses for you.
- (Dual-stack and IPv6-only) Assign Primary IPv6 IP: If you select a dual-stack or IPv6-only subnet, assign a primary IPv6 address. This helps prevent disruptions to traffic to the instance or network interface. Enable this option if you rely on the IPv6 address not changing. You can't remove the primary IPv6 address later on. When you enable an IPv6 GUA address to be a primary IPv6, the first IPv6 GUA becomes the primary IPv6 address until the instance is terminated or the network interface is detached. If you have multiple IPv6 addresses associated with a network interface and you let Amazon EC2 assign a primary IPv6 address, the first IPv6 GUA address associated with the network interface is the primary IPv6 address.
- Delete on termination: Indicates whether the network interface is deleted when the instance is deleted.

- Interface type: The network interface type:
- ENA: A high-performance network interface designed to handle high throughput and packet-per-second rates for TCP/IP protocols while minimizing CPU usage. This is the default value. For more information about ENA, see Elastic Network Adapter.
- EFA with ENA: A network interface that supports both ENA and EFA devices for traditional TCP/IP based transport along with SRD based transport. For more information about EFA, see Elastic Fabric Adapter.
- EFA-only: A high-performance network interface designed to handle high throughput, low latency inter-node communication for SRD based transport while bypassing the operating system stack. EFA-only network interfaces do not support IP addresses. For more information about EFA, see Elastic Fabric Adapter.
- Elastic Fabric Adapter: Indicates whether the network interface is an Elastic Fabric Adapter.
For more information, see Elastic Fabric Adapter for AI/ML and HPC workloads on Amazon EC2.
- Network card index: The index of the network card. The primary network interface must be assigned to network card index 0. Some instance types support multiple network cards.
- ENA Express: ENA Express is powered by AWS Scalable Reliable Datagram (SRD) technology.
SRD technology uses a packet spraying mechanism to distribute load and avoid network congestion. Enabling ENA Express allows supported instances to communicate using SRD on top of regular TCP traffic when possible. The launch instance wizard or launch template does not include ENA Express configuration for the instance unless you select Enable or Disable from the list.
- ENA Express UDP: If you've enabled ENA Express, you can optionally use it for UDP traffic. The launch instance wizard or launch template does not include ENA Express configuration for the instance unless you select Enable or Disable.
### Configure storage The AMI you selected includes one or more volumes of storage, including the root volume. You can specify additional volumes to attach to the instance.
(Launch instance wizard only) You can use the Simple or Advanced view. With the Simple view, you specify the size and type of the volume. To specify all volume parameters, choose the Advanced view (at top right of the card).
By using the Advanced view, you can configure each volume as follows:

- Storage type: Select Amazon EBS or instance store volumes to associate with your instance.
The volume types available in the list depend on the instance type that you've chosen. For more information, see Instance store temporary block storage for EC2 instances and Amazon EBS volumes.
- Device name: Select from the list of available device names for the volume.
- Snapshot: Select the snapshot from which to restore the volume. You can search for available shared and public snapshots by entering text into the Snapshot field.
- Size (GiB): For EBS volumes, you can specify a storage size.
- Volume type: For EBS volumes, select a volume type. For more information, see Amazon EBS volume types in the Amazon EBS User Guide.
- IOPS: If you have selected the io1, io2 , or or gp3 volume type, then you can enter the number of I/O operations per second (IOPS) that the volume can support. Required for io1, io2, and gp3 volumes. Not supported for gp2, st1, sc1, or standard volumes. If you omit this paramater for the launch template, you must specify a value for it when you launch an instance from the launch template.
- Delete on termination: For Amazon EBS volumes, choose Yes to delete the volume when the instance is terminated, or choose No to keep the volume. For more information, see Preserve data when an instance is terminated.
- Encrypted: If the instance type supports EBS encryption, you can choose Yes to enable encryption for the volume. If you have enabled encryption by default in this Region, encryption is enabled for you. For more information, see Amazon EBS encryption in the Amazon EBS User Guide.
- KMS key: If you selected Yes for Encrypted, then you must select a customer managed key to use to encrypt the volume. If you have enabled encryption by default in this Region, the default customer managed key is selected for you. You can select a different key or specify the ARN of any customer managed key that you created.
- Throughput: If you have selected the gp3 volume type, then you can enter the throughput, in MiB/s, that the volume can support.
- Volume initialization rate: If you have selected a snapshot, you can optionally specify the volume initialization rate, in MiB/s, at which the snapshot blocks are to be downloaded from Amazon S3 to the volume. For more information, see  Use an Amazon EBS Provisioned Rate for Volume Initialization. To use the default initialization rate or fast snapshot restore (if it is enabled for the selected snapshot), don't specify a rate.

- File systems: Mount an Amazon EFS or Amazon FSx file system to the instance. For more information about mounting an Amazon EFS file system, see Use Amazon EFS with Amazon EC2 Linux instances. For more information about mounting an Amazon FSx file system, see Use Amazon FSx with Amazon EC2 instances
### Advanced details For Advanced details, expand the section to view the fields and specify any additional parameters for the instance.
- (Launch instance wizard only) Domain join directory: Select the Directory Service directory (domain) to which your instance is joined to after launch. If you select a domain, you must select an IAM role with the required permissions. For more information about domain joining, see Seamlessly join an Amazon EC2 Linux instance to your AWS Managed Microsoft AD directory (Linux instances) and Seamlessly join an Amazon EC2 Windows instance to your AWS Managed Microsoft AD directory (Windows instances).
- IAM instance profile: Select an IAM instance profile to associate with the instance. This is a container for an IAM role. For more information, see IAM roles for Amazon EC2.
- Hostname type: Select whether the guest OS hostname of the instance will include the resource name or the IP name. For more information, see EC2 instance hostnames and domains.
- DNS Hostname: Determines if the DNS queries to the resource name or the IP name (depending on what you selected for Hostname type) will respond with the IPv4 address (A record), IPv6 address (AAAA record), or both. For more information, see EC2 instance hostnames and domains.
- Instance auto-recovery: When enabled, recovers your instance if system status checks fail. This setting is enabled by default at launch for supported instance types. For more information, see Configure simplified automatic recovery on an Amazon EC2 instance.
- Shutdown behavior: Select whether the instance should stop or terminate when shut down. For more information, see Change instance initiated shutdown behavior.
- Stop - Hibernate behavior: To enable hibernation, choose Enable. This field is available only if your instance meets the hibernation prerequisites. For more information, see Hibernate your Amazon EC2 instance.
- Termination protection: To prevent accidental termination, choose Enable. For more information, see Change instance termination protection.
- Stop protection: To prevent accidental stopping, choose Enable. For more information, see Enable stop protection.

- Detailed CloudWatch monitoring: Choose Enable to turn on detailed monitoring of your instance using Amazon CloudWatch. Additional charges apply. For more information, see Monitor your instances using CloudWatch.
- Credit specification: Choose Unlimited to enable applications to burst beyond the baseline for as long as needed. This field is only valid for T instances. Additional charges may apply. For more information, see Burstable performance instances.
- Placement group: Specify a placement group in which to launch the instance. You can select an existing placement group, or create a new one. Not all instance types support launching an instance in a placement group. For more information, see Placement groups for your Amazon EC2 instances.
- EBS-optimized instance: An instance that's optimized for Amazon EBS uses an optimized configuration stack and provides additional, dedicated capacity for Amazon EBS I/O. If the instance type supports this feature, choose Enable to enable it. Additional charges apply. For more information, see the section called "EBS optimization".
- Instance bandwidth configuration: You can boost either your networking bandwidth or your EBS bandwidth. For supported instance types only. For more information, see EC2 instance bandwidth weighting configuration.
- Purchasing option: Choose Spot Instances to request Spot Instances at the Spot price, capped at the On-Demand price, and choose Customize Spot Instance options to change the default Spot Instance settings. You can set your maximum price (not recommended), and change the request type, request duration, and interruption behavior. If you do not request a Spot Instance, Amazon EC2 launches an On-Demand Instance by default. For more information, see Manage your Spot Instances.
- Capacity Reservation: Specify whether to launch the instance into any open Capacity Reservation (Open), a specific Capacity Reservation (Target by ID), or a Capacity Reservation group (Target by group). To specify that a Capacity Reservation should not be used, choose None. For more information, see Launch instances into an existing Capacity Reservation.
- Tenancy: Choose whether to run your instance on shared hardware (Shared), isolated, dedicated hardware (Dedicated), or on a Dedicated Host (Dedicated host). If you choose to launch the instance onto a Dedicated Host, you can specify whether to launch the instance into a host resource group or you can target a specific Dedicated Host. Additional charges may apply. For more information, see Amazon EC2 Dedicated Instances and Amazon EC2 Dedicated Hosts.
- RAM disk ID: (Only valid for paravirtual (PV) AMIs) Select a RAM disk for the instance. If you have selected a kernel, you might need to select a specific RAM disk with the drivers to support it.
- Kernel ID: (Only valid for paravirtual (PV) AMIs) Select a kernel for the instance.

- Nitro Enclave: Allows you to create isolated execution environments, called enclaves, from Amazon EC2 instances. Select Enable to enable the instance for AWS Nitro Enclaves. For more information, see What is AWS Nitro Enclaves? in the AWS Nitro Enclaves User Guide.
- License configurations: You can launch instances against the specified license configuration to track your license usage. For more information, see Create a license configuration in the AWS License Manager User Guide.
- Specify CPU options: In the launch instance wizard, this field is only visible if the selected instance type supports specifying CPU options. Choose Specify CPU options to specify a custom number of vCPUs during launch. Set the number of CPU cores and threads per core. For more information, see CPU options for Amazon EC2 instances.
- Metadata accessible: You can enable or disable access to the Instance Metadata Service (IMDS).
For more information, see Configure instance metadata options for new instances.
- Metadata IPv6 endpoint: You can enable the instance to use the IMDS IPv6 address [fd00:ec2::254] to retrieve instance metadata. This option is only available if you are launching Nitro-based instances into an IPv6-supported subnet (dual stack or IPv6 only). For more information about retrieving instance metadata, see Access instance metadata for an EC2 instance.
- Metadata version: If you enable access to the IMDS, you can choose to require the use of Instance Metadata Service Version 2 when requesting instance metadata. For more information, see Configure instance metadata options for new instances.
- Metadata response hop limit: If you enable the IMDS, you can set the allowable number of network hops for the metadata token. For more information, see Configure instance metadata options for new instances.
- Allow tags in metadata: If you select Enable, the instance will allow access to all of its tags from its metadata. If no value is specified, then by default, access to the tags in instance metadata is not allowed. For more information, see Enable access to tags in instance metadata.
- User data: You can specify user data to configure an instance during launch, or to run a configuration script. For more information about user data for Linux instances, see Run commands when you launch an EC2 instance with user data input. For more information about user data for Windows instances, see How Amazon EC2 handles user data for Windows instances.
### Summary Use the Summary panel to specify the number of instances to launch, to review your instance configuration, and to launch your instances.

- Number of instances: Enter the number of instances to launch. All of the instances will launch with the same configuration.
Tip To ensure faster instance launches, break up large requests into smaller batches. For example, create five separate launch requests for 100 instances each instead of one launch request for 500 instances.
- (Optional) If you specify more than one instance, to help ensure that you maintain the correct number of instances to handle demand on your application, you can choose consider EC2 Auto Scaling to create a launch template and an Auto Scaling group. Auto Scaling scales the number of instances in the group according to your specifications. For more information, see the Amazon EC2 Auto Scaling User Guide.
Note If Amazon EC2 Auto Scaling marks an instance that is in an Auto Scaling group as unhealthy, the instance is automatically scheduled for replacement where it is terminated and another is launched, and you lose your data on the original instance. An instance is marked as unhealthy if you stop or reboot the instance, or if another event marks the instance as unhealthy. For more information, see Health checks for instances in an Auto Scaling group in the Amazon EC2 Auto Scaling User Guide.
- Review the details of your instance, and make any necessary changes. You can navigate directly to a section by choosing its link in the Summary panel.
- When you're ready to launch your instance, choose Launch instance.
## Launch an EC2 instance using the launch instance wizard in the console You can launch an Amazon EC2 instance using the launch instance wizard in the Amazon EC2 console. The wizard provides default values for the launch parameters, which you can either accept or modify to suit your requirements. The only parameter that is not specified is the key pair. If you choose to accept the default values, you can quickly launch an instance by selecting only a key pair.

Important You incur charges for the instance while the instance is in the running state, even if it remains idle. However, if you qualify for the Free Tier, you might not incur charges. For more information, see Track your Free Tier usage for Amazon EC2.
For a description of each parameter in the launch instance wizard, see Reference for Amazon EC2 instance configuration parameters.
Topics
- Quickly launch an instance
- Launch an instance using defined parameters
### Quickly launch an instance To set up an instance quickly for testing purposes, follow these steps. You'll select the operating system and your key pair, and accept the default values. Except for the key pair, the launch instance wizard provides default values for all of the parameters. You can accept any or all of the defaults, or configure an instance by specifying your own values for each parameter.
For a description of each parameter in the launch instance wizard, see Reference for Amazon EC2 instance configuration parameters.
To quickly launch an instance using the launch instance wizard
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation bar at the top of the screen, the current AWS Region is displayed (for example, US East (Ohio)). If needed, select a different Region in which to launch the instance.
3. From the Amazon EC2 console dashboard, choose Launch instance.
4. (Optional) Under Name and tags, for Name, enter a descriptive name for your instance.
5. Under Application and OS Images (Amazon Machine Image), choose Quick Start, and then choose the operating system (OS) for your instance.
6. Under Key pair (login), for Key pair name, choose an existing key pair or create a new one.
7. In the Summary panel, choose Launch instance.

### Launch an instance using defined parameters If you're launching an instance that you'll use in production, you'll need to configure the instance to suit your requirements. For a description of each parameter in the launch instance wizard, see Reference for Amazon EC2 instance configuration parameters.
To launch an instance by defining all the launch parameters using the launch instance wizard
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation bar at the top of the screen, the current AWS Region is displayed (for example, US East (Ohio)). If needed, select a different Region in which to launch the instance.
3. From the Amazon EC2 console dashboard, choose Launch instance.
4. (Optional) Under Name and tags, for Name, enter a descriptive name for your instance so that you can easily keep track of it.
The instance name is a tag, where the key is Name, and the value is the name that you specify.
5. Under Application and OS Images (Amazon Machine Image), choose the operating system (OS) for your instance, and then choose an AMI.
An AMI is a template that contains the operating system and software required to launch your instance.
6. Under Instance type, choose an instance type.
The instance type determines the hardware configuration (CPU, memory, storage, and networking capacity) and size of the host computer used for your instance.
If you're not sure which instance type to choose, you can do the following:
- Choose Compare instance types to compare different instance types by the following attributes: number of vCPUs, architecture, amount of memory (GiB), amount of storage (GB), storage type, and network performance.
- Choose Get advice to get guidance and suggestions for instance types from the EC2 instance type finder. For more information, see Get recommendations from EC2 instance type finder.
Note Depending on when you created your account, you might be able to use instance types for free under the Free Tier. These instance types are labeled Free tier eligible.

If your created your AWS account before July 15, 2025 and it's less than 12 months old, you can use Amazon EC2 under the Free Tier by selecting the t2.micro instance type, or the t3.micro instance type in Regions where t2.micro is unavailable. Be aware that when you launch a t3.micro instance, it defaults to Unlimited mode, which might incur additional charges based on CPU usage.
If you created your AWS account on or after July 15, 2025, you can use t3.micro, t3.small, t4g.micro, t4g.small, c7i-flex.large, and m7i-flex.large instance types for 6 months or until your credits are used up.
For more information, see Free Tier benefits before and after July 15, 2025.
7. Under Key pair (login), for Key pair name, choose an existing key pair or create a new one. If you do not require a key pair to connect to your instance, you can choose Proceed without a key pair (not recommended).
8. Under Network settings, you can keep the defaults if you're launching a test instance. If you're launching a production instance, it's best practice to control traffic into and out of your instance using network settings and security groups that you define.
9. Under Configure storage, you can keep the defaults or specify additional storage. The AMI you selected includes one or more volumes of storage, including the root volume. You can specify additional volumes to attach to the instance.
You can use the Simple or Advanced view. With the Simple view, you specify the size and type of the volume. To specify all volume parameters, choose the Advanced view (at top right of the card).
10. For Advanced details, expand the section to view the fields and specify any additional parameters for your instance.
11. In the Summary panel, you can do the following: a.
Specify the number of instances to launch. b.
Review your instance configuration, and navigate directly to a section by choosing its link. c.
When you're ready to launch your instance, choose Launch instance.
If the instance fails to launch or the state immediately goes to terminated instead of running, see Troubleshoot Amazon EC2 instance launch issues.
12. (Optional) You can create a billing alert for the instance. On the confirmation screen, under Next Steps, choose Create billing alerts and follow the directions. Billing alerts can also be

created after you launch the instance. For more information, see Creating a billing alarm to monitor your estimated AWS charges in the Amazon CloudWatch User Guide.
## Launch EC2 instances using a launch template An Amazon EC2 launch template stores instance launch parameters so that you don't have to specify them every time you launch an instance.
Several instance launch services can optionally use launch templates when launching instances, while for other services, like EC2 Fleet, instances can't be launched unless a launch template is used. This topic describes how to use a launch template when launching an instance using the EC2 launch instance wizard, Amazon EC2 Auto Scaling, EC2 Fleet, and Spot Fleet.
For more information about launch templates, including how to create a launch template, see Store instance launch parameters in Amazon EC2 launch templates.
Topics
- Launch an Amazon EC2 instance using a launch template
- Launch instances in an Amazon EC2 Auto Scaling group using a launch template
- Launch an EC2 Fleet using a launch template
- Launch a Spot Fleet using a launch template
### Launch an Amazon EC2 instance using a launch template You can use the parameters contained in a launch template to launch an Amazon EC2 instance.
After selecting the launch template, but before launching the instance, you can modify the launch parameters.
Instances that are launched using a launch template are automatically assigned two tags with the keys aws:ec2launchtemplate:id and aws:ec2launchtemplate:version. You can't remove or edit these tags.
Console To launch an instance using a launch template
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.

2. Use one of the following options to select the launch template:
- From the Amazon EC2 console dashboard, choose the down arrow next to Launch instance, choose Launch instance from template, and then for Source template, select a launch template.
- In the navigation pane, choose Launch Templates, select the launch template, and choose Actions, Launch instance from template.
3. For Source template version, select the launch template version to use.
4. (Optional) You can modify the values for any of the launch parameters. If you don't modify a value, the value defined by the launch template is used. If no value was specified in the launch template, the default value for the parameter is used.
5. In the Summary panel, for Number of instances, specify the number of instances to launch.
6. Choose Launch instance.
If the instance fails to launch or the state immediately goes to terminated instead of running, see Troubleshoot Amazon EC2 instance launch issues.
AWS CLI To launch an instance from a launch template
- Use the run-instances command and specify the --launch-template parameter. Optionally specify the launch template version to use. If you don't specify the version, the default version is used. aws ec2 run-instances \ --launch-template LaunchTemplateId=lt-0abcd290751193123,Version=1
- To override a launch template parameter, specify the parameter in the run-instances command. The following example overrides the instance type that's specified in the launch template (if any). aws ec2 run-instances \ --launch-template LaunchTemplateId=lt-0abcd290751193123 \ --instance-type t2.small

- If you specify a nested parameter that's part of a complex structure, the instance is launched using the complex structure as specified in the launch template plus any additional nested parameters that you specify.
In the following example, the instance is launched with the tag Owner=TeamA as well as any other tags that are specified in the launch template. If the launch template has an existing tag with a key of Owner, the value is replaced with TeamA. aws ec2 run-instances \ --launch-template LaunchTemplateId=lt-0abcd290751193123 \ --tag-specifications "ResourceType=instance,Tags=[{Key=Owner,Value=TeamA}]"
In the following example, the instance is launched with a volume with the device name /dev/xvdb as well as any other block device mappings that are specified in the launch template. If the launch template has an existing volume defined for /dev/xvdb, its values are replaced with the specified values. aws ec2 run-instances \ --launch-template LaunchTemplateId=lt-0abcd290751193123 \ --block-device-mappings "DeviceName=/dev/ xvdb,Ebs={VolumeSize=20,VolumeType=gp2}"
If the instance fails to launch or the state immediately goes to terminated instead of running, see Troubleshoot Amazon EC2 instance launch issues.
PowerShell To launch an instance from a launch template using the AWS Tools for PowerShell
- Use the New-EC2Instance command and specify the -LaunchTemplate parameter.
Optionally specify the launch template version to use. If you don't specify the version, the default version is used.
Import-Module AWS.Tools.EC2 New-EC2Instance `
    -LaunchTemplate ( New-Object -TypeName Amazon.EC2.Model.LaunchTemplateSpecification - Property @{ LaunchTemplateId = 'lt-0abcd290751193123'; Version          = '4'

    } )
- To override a launch template parameter, specify the parameter in the New-EC2Instance command. The following example overrides the instance type that's specified in the launch template (if any).
Import-Module AWS.Tools.EC2 New-EC2Instance `
    -InstanceType t4g.small `
    -LaunchTemplate ( New-Object -TypeName Amazon.EC2.Model.LaunchTemplateSpecification - Property @{ LaunchTemplateId = 'lt-0abcd290751193123'; Version          = '4'
    } )
- If you specify a nested parameter that's part of a complex structure, the instance is launched using the complex structure as specified in the launch template plus any additional nested parameters that you specify.
In the following example, the instance is launched with the tag Owner=TeamA as well as any other tags that are specified in the launch template. If the launch template has an existing tag with a key of Owner, the value is replaced with TeamA.
Import-Module AWS.Tools.EC2 New-EC2Instance `
    -InstanceType t4g.small  `
    -LaunchTemplate ( New-Object -TypeName Amazon.EC2.Model.LaunchTemplateSpecification - Property @{ LaunchTemplateId = 'lt-0abcd290751193123'; Version          = '4'
        } ) `
    -TagSpecification ( New-Object -TypeName Amazon.EC2.Model.TagSpecification -Property @{ ResourceType = 'instance'; Tags         = @( @{key = "Owner"; value = "TeamA" }, @{key = "Department"; value = "Operations" }

            )
        } )
In the following example, the instance is launched with a volume with the device name /dev/xvdb as well as any other block device mappings that are specified in the launch template. If the launch template has an existing volume defined for /dev/xvdb, its values are replaced with the specified values.
Import-Module AWS.Tools.EC2 New-EC2Instance `
    -InstanceType t4g.small  `
    -LaunchTemplate ( New-Object -TypeName Amazon.EC2.Model.LaunchTemplateSpecification - Property @{ LaunchTemplateId = 'lt-0abcd290751193123'; Version          = '4'
    } ) `
    -BlockDeviceMapping  ( New-Object -TypeName Amazon.EC2.Model.BlockDeviceMapping -Property @{ DeviceName = '/dev/xvdb'; EBS        = ( New-Object -TypeName Amazon.EC2.Model.EbsBlockDevice -Property @{ VolumeSize = 25; VolumeType = 'gp3'
                } )
        } )
If the instance fails to launch or the state immediately goes to terminated instead of running, see Troubleshoot Amazon EC2 instance launch issues.
### Launch instances in an Amazon EC2 Auto Scaling group using a launch template You can create an Auto Scaling group and specify a launch template to use for the group. When Amazon EC2 Auto Scaling launches instances in the Auto Scaling group, it uses the launch parameters defined in the associated launch template.

Before you can create an Auto Scaling group using a launch template, you must first create a launch template that includes the parameters required to launch an instance in an Auto Scaling group. Some parameters are required, such as the ID of the AMI, and some parameters are not available to use with an Auto Scaling group. The console provides guidance to help you create a template that you can use with Amazon EC2 Auto Scaling.
To create an Auto Scaling group with a launch template using the console
- For the instructions, see Create an Auto Scaling group using a launch template in the Amazon EC2 Auto Scaling User Guide.
To create or update an Auto Scaling group with a launch template using the AWS CLI
- Use the create-auto-scaling-group or the update-auto-scaling-group command and specify the --launch-template parameter.
For more information, see the following topics in the Amazon EC2 Auto Scaling User Guide:
- Create a launch template for an Auto Scaling group
- Create a launch template using advanced settings
- Examples for creating and managing launch templates with the AWS Command Line Interface (AWS CLI) – Provides examples that show how to create launch templates with various parameter combinations.
- Create Auto Scaling groups using launch templates
- Update an Auto Scaling group
### Launch an EC2 Fleet using a launch template A launch template is a requirement when creating an EC2 Fleet request. When Amazon EC2 fulfills the EC2 Fleet request, it uses the launch parameters defined in the associated launch template.
You can override some of the parameters that are specified in the launch template. For more information, see Create an EC2 Fleet.
To create an EC2 Fleet with a launch template using the AWS CLI
- Use the create-fleet command. Use the --launch-template-configs parameter to specify the launch template and any overrides for the launch template.

### Launch a Spot Fleet using a launch template A launch template is optional when creating a Spot Fleet request. If you don't use a launch template, you can manually specify the launch parameters. If you use a launch template, when Amazon EC2 fulfills the Spot Fleet request, it uses the launch parameters defined in the associated launch template. You can override some of the parameters that are specified in the launch template. For more information, see Create a Spot Fleet.
To create a Spot Fleet request using a launch template
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Spot Requests.
3. Choose Request Spot Instances.
4. Under Launch parameters, choose Use a launch template.
5. For Launch template, choose a launch template, and then, from the field to the right, choose the launch template version.
6. Configure your Spot Fleet by selecting different options on this screen. For more information about the options, see Create a Spot Fleet request using defined parameters.
7. When you're ready to create your Spot Fleet, choose Launch.
To create a Spot Fleet request using a launch template
- Use the request-spot-fleet command. Use the LaunchTemplateConfigs parameter to specify the launch template and any overrides for the launch template.
## Launch an EC2 instance using details from an existing instance The Amazon EC2 console provides a Launch more like this option that enables you to use a current instance as a base for launching other instances. This option automatically populates the Amazon EC2 launch instance wizard with certain configuration details from the selected instance.
Considerations
- We do not clone your instances; we only replicate some of the configuration details. To create a copy of your instance, first create an AMI from it, then launch more instances from the AMI.
Create a launch template to ensure that you launch your instances using the same launch details.
- The current instance must be in the running state.

Copied details The following configuration details are copied from the selected instance into the launch instance wizard:
- AMI ID
- Instance type
- Availability Zone, or the VPC and subnet in which the selected instance is located
- Public IPv4 address. If the selected instance currently has a public IPv4 address, the new instance receives a public IPv4 address, regardless of the selected instance's default public IPv4 address setting. For more information about public IPv4 addresses, see Public IPv4 addresses.
- Placement group, if applicable
- IAM role associated with the instance, if applicable
- Shutdown behavior setting (stop or terminate)
- Termination protection setting (true or false)
- CloudWatch monitoring (enabled or disabled)
- Amazon EBS-optimization setting (true or false)
- Tenancy setting, if launching into a VPC (shared or dedicated)
- Kernel ID and RAM disk ID, if applicable
- User data, if specified
- Tags associated with the instance, if applicable
- Security groups associated with the instance
- [Windows instances] Association information. If the selected instance is associated with a configuration file, the same file is automatically associated with the new instance. If the configuration file includes a joined domain configuration, the new instance is joined to the same domain. For more information about joining a domain, see Seamlessly join a Windows EC2 instance to your AWS Managed Microsoft AD Active Directory in the AWS Directory Service Administration Guide.
Details not copied The following configuration details are not copied from your selected instance. Instead, the wizard applies their default settings or behavior:

- Number of network interfaces – The default is one network interface, which is the primary network interface (eth0).
- Storage – The default storage configuration is determined by the AMI and the instance type.
To launch more instances like an existing instance
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Instances.
3. Select an instance, and then choose Actions, Images and templates, Launch more like this.
4. The launch instance wizard opens. You can make any necessary changes to the instance configuration by selecting different options on this screen.
When you are ready to launch your instance, choose Launch instance.
5. If the instance fails to launch or the state immediately goes to terminated instead of running, see Troubleshoot Amazon EC2 instance launch issues.
## Launch an Amazon EC2 instance from an AWS Marketplace AMI You can subscribe to an AWS Marketplace AMI and launch an instance from it using the Amazon EC2 console or a command line tool. For more information about AWS Marketplace AMIs, see Paid AMIs in the AWS Marketplace for Amazon EC2 instances.
To cancel your subscription to the AMI after launch, you must first terminate all instances that were launched from the AMI. For more information, see Manage your AWS Marketplace subscriptions.
To launch an instance from an AWS Marketplace AMI using the Amazon EC2 console
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. From the Amazon EC2 console dashboard, choose Launch instance.
3. (Optional) Under Name and tags, for Name, enter a descriptive name for your instance.
4. Under Application and OS Images (Amazon Machine Image), choose Browse more AMIs, and then choose the AWS Marketplace AMIs tab. Find a suitable AMI by browsing the categories or using the search functionality. To choose a product, choose Select.
5. A window opens with an overview of the product you've selected. You can view the pricing information, as well as any other information that the vendor has provided. When you're ready, choose Subscribe and launch. This will start your subscription immediately. While the

subscription is underway, you can configure the instance by continuing with the steps in this procedure. If there are any problems with your credit card details, you will be asked to update your account details.
Note You're not charged for using the product until you have launched an instance with the AMI. Take note of the pricing for each supported instance type when you select an instance type. Additional taxes might also apply to the product.
6. For Instance type, select an instance type for your instance. The instance type defines the hardware configuration and size of the instance to launch.
7. Under Key pair (login), for Key pair name, choose an existing key pair or create a new one.
8. Under Network settings, for Firewall (security groups), take note of the new security group that was created according to the vendor's specifications for the product. The security group might include rules that allow all IPv4 addresses (0.0.0.0/0) access on SSH (port 22) on Linux or RDP (port 3389) on Windows. We recommend that you adjust these rules to allow only a specific address or range of addresses to access your instance over those ports.
9. You can use the other fields on the screen to configure your instance, add storage, and add tags. For information about the different options that you can configure, see Reference for Amazon EC2 instance configuration parameters.
10. In the Summary panel, under Software Image (AMI), check the details of the AMI from which you're about to launch the instance. Also check the other configuration details that you specified. When you're ready to launch your instance, choose Launch instance.
11. Depending on the product you've subscribed to, the instance might take a few minutes or more to launch. If there are any problems with your credit card details, you will be asked to update your account details. When the launch confirmation page displays, choose View all instances to go to the Instances page.
Note You are charged the subscription price as long as your instance is in the running state, even if it is idle. If your instance is stopped, you might still be charged for storage.
