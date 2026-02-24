# Tutorial: Connect an Amazon EC2 instance to an Amazon RDS database

Source: apps/user-manuals/aws/ec2-ug.pdf

---

- If you upgraded to Windows Server 2008 and all status checks fail after several hours, the upgrade may have failed and be presenting a prompt to Click OK to confirm rolling back.
Because the console is not accessible at this state, there is no way to click the button. To get around this, perform a reboot via the Amazon EC2 console or API. The reboot takes ten minutes or more to initiate. The instance might become available after 25 minutes.
- Remove applications or server roles from the server and try again.
If the instance does not pass all status checks after removing applications or server roles from the server, do the following.
- Stop the instance and attach the root volume to another instance. For more information, see the description of how to stop and attach the root volume to another instance in "Waiting for the metadata service".
- Analyze Windows Setup log files and event logs for failures.
For other issues or problems with an operating system upgrade or migration, we recommend reviewing the articles listed in Before you begin an in-place upgrade.
# Tutorial: Connect an Amazon EC2 instance to an Amazon RDS database database
## Tutorial objective The objective of this tutorial is to learn how to configure a secure connection between an Amazon EC2 instance and an Amazon RDS database by using the AWS Management Console.
There are different options for configuring the connection. In this tutorial, we explore the following three options:
- Option 1: Automatically connect an instance to an RDS database using the EC2 console Use the automatic connection feature in the EC2 console to automatically configure the connection between your EC2 instance and your RDS database to allow traffic between the EC2 instance and the RDS database.
- Option 2: Automatically connect an instance to an RDS database using the RDS console

Use the automatic connection feature in the RDS console to automatically configure the connection between your EC2 instance and your RDS database to allow traffic between the EC2 instance and the RDS database.
- Option 3: Manually connect an instance to an RDS database by creating security groups Configure the connection between your EC2 instance to your RDS database by manually configuring and assigning the security groups to reproduce the configuration that is automatically created by the automatic connection feature in Option 1 and Option 2.
## Context As context for why you'd want to configure a connection between your EC2 instance and an RDS database, let's consider the following scenario: Your website presents a form to your users to fill in. You need to capture the form data in a database. You can host your website on an EC2 instance that's been configured as a web server, and you can capture the form data in an RDS database.
The EC2 instance and the RDS database need to be connected to each other so that the form data can go from the EC2 instance to the RDS database. This tutorial explains how to configure that connection. Note that this is just one example of a use case for connecting an EC2 instance and an RDS database.
## Architecture The following diagram shows the resources that are created and the architectural configuration that results from completing all the steps in this tutorial.

The diagram illustrates the following resources that you'll create:
- You'll create an EC2 instance and an RDS database in the same AWS Region, VPC, and Availability Zone.
- You'll create the EC2 instance in a public subnet.
- You'll create the RDS database in a private subnet.
When you use the RDS console to create the RDS database and automatically connect the EC2 instance, the VPC, DB subnet group, and public access settings for the database are automatically selected. The RDS database is automatically created in a private subnet within the same VPC as the EC2 instance.
- Internet users can connect to the EC2 instance by using SSH or HTTP/HTTPS via an Internet gateway.
- Internet users cannot connect directly to the RDS database; only the EC2 instance is connected to the RDS database.
- When you use the automatic connection feature to allow traffic between the EC2 instance and the RDS database, the following security groups are automatically created and added:

- Security group ec2-rds-x is created and added to the EC2 instance. It has one outbound rule that references the rds-ec2-x security group as its destination. This allows traffic from the EC2 instance to reach the RDS database with the rds-ec2-x security group.
- Security group rds-ec2-x is created and added to the RDS database. It has one inbound rule that references the ec2-rds-x security group as its source. This allows traffic from the EC2 instance with the ec2-rds-x security group to reach the RDS database.
By using separate security groups (one for the EC2 instance, and one for the RDS database), you have better control over the security of the instance and the database. If you were to use the same security group on both the instance and the database, and then modified the security group to suit, say, only the database, the modification would affect both the instance and the database. In other words, if you were to use one security group, you could unintentionally modify the security of a resource (either the instance or the database) because you'd forgotten that the security group was attached to it.
The security groups that are automatically created also respect least privilege as they only allow the mutual connection for this workload on the database port by creating a workload-specific security group pair.
## Considerations Consider the following when you complete the tasks in this tutorial:
- Two consoles – You will use the following two consoles for this tutorial:
- Amazon EC2 console – You will use the EC2 console to launch instances, to automatically connect an EC2 instance to an RDS database, and for the manual option to configure the connection by creating the security groups.
- Amazon RDS console – You will use the RDS console to create an RDS database and to automatically connect an EC2 instance to an RDS database.
- One VPC – To use the automatic connection feature, your EC2 instance and your RDS database must be in the same VPC.
If you were to manually configure the connection between your EC2 instance and your RDS database, you could launch your EC2 instance in one VPC and your RDS database in another VPC; however, you'd need to set up additional routing and VPC configuration. This scenario is not covered in this tutorial.

- One AWS Region – The EC2 instance and RDS database must be located in the same Region.
- Two security groups – The connectivity between the EC2 instance and the RDS database is configured by two security groups—a security group for your EC2 instance, and a security group for your RDS database.
When you use the automatic connection feature in the EC2 console or RDS console to configure the connectivity (Option 1 and Option 2 of this tutorial), the security groups are automatically created and assigned to the EC2 instance and RDS database.
If you do not use the automatic connection feature, you'll need to manually create and assign the security groups. You do this in Option 3 of this tutorial.
## Time to complete the tutorial 30 minutes You can complete the entire tutorial in one sitting, or you can complete it one task at a time.
## Costs By completing this tutorial, you might incur costs for the AWS resources that you create.
You can use Amazon EC2 under the Free Tier provided your AWS account qualifies for the Free Tier and you configure your resources according to the Free Tier requirements. For more information, Free Tier benefits before and after July 15, 2025.
If your EC2 instance and your RDS database are in different Availability Zones, you will incur data transfer fees. To avoid incurring these fees, the EC2 instance and the RDS database must be in the same Availability Zone. For information about data transfer fees, see Data Transfer on the Amazon EC2 On-Demand Pricing page.
To prevent incurring costs after you've completed the tutorial, make sure to delete the resources if they are no longer needed. For the steps to delete the resources, see Task 4 (Optional): Clean up.
## Option 1: Automatically connect an instance to an RDS database using the EC2 console the EC2 console The objective of Option 1 is to explore the automatic connection feature in the EC2 console that automatically configures the connection between your EC2 instance and RDS database to allow

traffic from the EC2 instance to the RDS database. In Option 3, you'll learn how to manually configure the connection.
Tasks
- Before you begin
- Task 1 (Optional): Create an RDS database
- Task 2 (Optional): Launch an EC2 instance
- Task 3: Automatically connect your EC2 instance to your RDS database
- Task 4: Verify the connection configuration
- Task 5 (Optional): Clean up
### Before you begin You'll need the following to complete this tutorial:
- An RDS database that is in the same VPC as the EC2 instance. You can either use an existing RDS database or follow the steps in Task 1 to create a new RDS database.
- An EC2 instance that is in the same VPC as the RDS database. You can either use an existing EC2 instance or follow the steps in Task 2 to create a new EC2 instance.
- Permissions to call the following operations:
- ec2:AssociateRouteTable
- ec2:AuthorizeSecurityGroupEgress
- ec2:CreateRouteTable
- ec2:CreateSecurityGroup
- ec2:CreateSubnet
- ec2:DescribeInstances
- ec2:DescribeNetworkInterfaces
- ec2:DescribeRouteTables
- ec2:DescribeSecurityGroups
- ec2:DescribeSubnets
- ec2:ModifyNetworkInterfaceAttribute
- ec2:RevokeSecurityGroupEgress

### Task 1 (Optional): Create an RDS database Note Creating a Amazon RDS database is not the focus of this tutorial. If you already have an RDS database and would like to use it in this tutorial, you can skip this task.
If you use an existing RDS database, make sure that it is in the same VPC as your EC2 instance so that you can use the automatic connection feature.
The objective of this task is to create an RDS database so that you can complete Task 3 where you configure the connection between your EC2 instance and your RDS database. The steps in this task configure the RDS database as follows:
- Engine type: MySQL
- Template: Free tier
- DB instance identifier: tutorial-database-1
- DB instance class: db.t3.micro Important In a production environment, you should configure your database to meet your specific needs.
To create a MySQL RDS database
1. Open the Amazon RDS console at https://console.aws.amazon.com/rds/.
2. From the Region selector (at top right), choose an AWS Region. The database and the EC2 instance must be in the same Region in order to use the automatic connection feature in the EC2 console.
3. On the dashboard, choose Create database.
4. Under Choose a database creation method, check that Standard create is selected. If you choose Easy create, the VPC selector is not available. You must ensure that your database is in the same VPC as your EC2 instance in order to use the automatic connection feature in the EC2 console.

5. Under Engine options, for Engine type, choose MySQL.
6. Under Templates, choose a sample template to meet your needs. For this tutorial, choose Free tier to create an RDS database at no cost. However, note that the Free Tier is only available for accounts that qualify for the Free Tier. You can read more by choosing the Info link in the Free tier box.
7. Under Settings, do the following: a.
For DB instance identifier, enter a name for the database. For this tutorial, enter tutorial-database-1. b.
For Master username, leave the default name, which is admin. c.
For Master password, enter a password that you can remember for this tutorial, and then, for Confirm password, enter the password again.
8. Under Instance configuration, for DB instance class, leave the default, which is db.t3.micro.If your account qualifies for the Free Tier, you can use this database class for free. For more information, see AWS Free Tier.
9. Under Connectivity, for Compute resource, choose Don't connect to an EC2 compute resource because you'll connect the EC2 instance and the RDS database later in Task 3.
(Later, in Option 2 of this tutorial, you'll try out the automatic connection feature in the RDS console by choosing Connect to an EC2 compute resource.)
10. For Virtual private cloud (VPC), choose a VPC. The VPC must have a DB subnet group. To use the automatic connection feature, your EC2 instance and RDS database must be in the same VPC.
11. Keep all the default values for the other fields on this page.
12. Choose Create database.
On the Databases screen, the Status of the new database is Creating until the database is ready to use. When the status changes to Available, you can connect to the database.
Depending on the database class and the amount of storage, it can take up to 20 minutes before the new database is available.

#### View an animation: Create an RDS database
### Task 2 (Optional): Launch an EC2 instance Note Launching an instance is not the focus of this tutorial. If you already have an Amazon EC2 instance and would like to use it in this tutorial, you can skip this task.
If you use an existing EC2 instance, make sure that it is in the same VPC as your RDS database so that you can use the automatic connection feature.

The objective of this task is to launch an EC2 instance so that you can complete Task 3 where you configure the connection between your EC2 instance and your Amazon RDS database. The steps in this task configure the EC2 instance as follows:
- Instance name: tutorial-instance-1
- AMI: Amazon Linux 2
- Instance type: t2.micro
- Auto-assign public IP: Enabled
- Security group with the following three rules:
- Allow SSH from your IP address
- Allow HTTPS traffic from anywhere
- Allow HTTP traffic from anywhere Important In a production environment, you should configure your instance to meet your specific needs.
To launch an EC2 instance
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. From the Region selector (at top right), choose an AWS Region. The instance and the RDS database must be in the same Region in order to use the automatic connection feature in the EC2 console.
3. On the EC2 Dashboard, choose Launch instance.
4. Under Name and tags, for Name, enter a name to identify your instance. For this tutorial, name the instance tutorial-instance-1. While the instance name is not mandatory, when you select your instance in the EC2 console, the name will help you easily identify it.
5. Under Application and OS Images, choose an AMI that meets your web server needs. This tutorial uses Amazon Linux 2.
6. Under Instance type, for Instance type, select an instance type that meets your web server needs. This tutorial uses t2.micro.

Note Depending on when you created your account, you might be eligible to use Amazon EC2 under the Free Tier.
If your created your AWS account before July 15, 2025 and it's less than 12 months old, you can use Amazon EC2 under the Free Tier by selecting the t2.micro instance type, or the t3.micro instance type in Regions where t2.micro is unavailable. Be aware that when you launch a t3.micro instance, it defaults to Unlimited mode, which might incur additional charges based on CPU usage. If an instance type can be used under the Free Tier, it is labeled Free tier eligible.
If you created your AWS account on or after July 15, 2025, you can use t3.micro, t3.small, t4g.micro, t4g.small, c7i-flex.large, and m7i-flex.large instance types for 6 months or until your credits are used up.
For more information, see Free Tier benefits before and after July 15, 2025.
7. Under Key pair (login), for Key pair name, choose your key pair.
8. Under Network settings, do the following: a.
For Network and Subnet, if you haven't made changes to your default VPC or subnets, you can keep the default settings.
If you have made changes to your default VPC or subnets, check the following: i.
The instance must be in the same VPC as the RDS database to use the automatic connection feature. By default you have only one VPC. ii.
The VPC that you're launching your instance into must have an internet gateway attached to it so that you can access your web server from the internet. Your default VPC is automatically set up with an internet gateway. iii.
To ensure that your instance receives a public IP address, for Auto-assign public IP, check that Enable is selected. If Disable is selected, choose Edit (to the right of Network Settings), and then, for Auto-assign public IP, choose Enable. b.
To connect to your instance by using SSH, you need a security group rule that authorizes SSH (Linux) or RDP (Windows) traffic from your computer's public IPv4 address. By default, when you launch an instance, a new security group is created with a rule that allows inbound SSH traffic from anywhere.

To make sure that only your IP address can connect to your instance, under Firewall (security groups), from the drop-down list next to the Allow SSH traffic from checkbox, choose My IP. c.
To allow traffic from the internet to your instance, select the following checkboxes:
- Allow HTTPs traffic from the internet
- Allow HTTP traffic from the internet
9. In the Summary panel, review your instance configuration and then choose Launch instance.
10. Keep the confirmation page open. You'll need it for the next task when you automatically connect your instance to your database.
If the instance fails to launch or the state immediately goes to terminated instead of running, see Troubleshoot Amazon EC2 instance launch issues.
For more information about launching an instance, see Launch an EC2 instance using the launch instance wizard in the console.

#### View an animation: Launch an EC2 instance
### Task 3: Automatically connect your EC2 instance to your RDS database The objective of this task is to use the automatic connection feature in the EC2 console to automatically configure the connection between your EC2 instance and your RDS database.
To automatically connect an EC2 instance to an RDS database using the EC2 console
1. On the instance launch confirmation page (it should be open from the previous task), choose Connect an RDS database.
If you closed the confirmation page, follow these steps: a.
Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/. b.
In the navigation pane, choose Instances. c.
Select the EC2 instance that you just created, and then choose Actions, Networking, Connect RDS database.

If Connect RDS database is not available, check that the EC2 instance is in the Running state.
2. For Database role, choose Instance. Instance in this case refers to the database instance.
3. For RDS database, choose the RDS database that you created in Task 1.
Note The EC2 instance and the RDS database must be in the same VPC in order to connect to each other.
4. Choose Connect.
#### View an animation: Automatically connect a newly-launched EC2 instance to an RDS database
### Task 4: Verify the connection configuration The objective of this task is to verify that the two security groups were created and assigned to the instance and database.

When you use the automatic connection feature in the console to configure the connectivity, the security groups are automatically created and assigned to the instance and database, as follows:
- Security group rds-ec2-x is created and added to the RDS database. It has one inbound rule that references the ec2-rds-x security group as its source. This allows traffic from the EC2 instance with the ec2-rds-x security group to reach the RDS database.
- Security group ec2-rds-x is created and added to the EC2 instance. It has one outbound rule that references the rds-ec2-x security group as its destination. This allows traffic from the EC2 instance to reach the RDS database with the rds-ec2-x security group.
To verify the connection configuration using the console
1. Open the Amazon RDS console at https://console.aws.amazon.com/rds/.
2. In the navigation page, choose Databases.
3. Choose the RDS database that you created for this tutorial.
4. On the Connectivity & security tab, under Security, VPC security groups, verify that a security group called rds-ec2-x is displayed.
5. Choose the rds-ec2-x security group. The Security Groups screen in the EC2 console opens.
6. Choose the rds-ec2-x security group to open it.
7. Choose the Inbound rules tab.
8. Verify that the following security group rule exists, as follows:
- Type: MYSQL/Aurora
- Port range: 3306
- Source: sg-0987654321example / ec2-rds-x – This is the security group that is assigned to the EC2 instance that you verified in the preceding steps.
- Description: Rule to allow connections from EC2 instances with sg-1234567890example attached
9. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
10. In the navigation pane, choose Instances.
11. Choose the EC2 instance that you selected to connect to the RDS database in the previous task, and choose the Security tab.
12. Under Security details, Security groups, verify that a security group called ec2-rds-x is in the list. x is a number.

13. Choose the ec2-rds-x security group to open it.
14. Choose the Outbound rules tab.
15. Verify that the following security group rule exists, as follows:
- Type: MYSQL/Aurora
- Port range: 3306
- Destination: sg-1234567890example / rds-ec2-x
- Description: Rule to allow connections to database-tutorial from any instances this security group is attached to By verifying that these security groups and security group rules exist and that they are assigned to the RDS database and EC2 instance as described in this procedure, you can verify that the connection was automatically configured by using the automatic connection feature.
#### View an animation: Verify the connection configuration

You have completed Option 1 of this tutorial. You can now either complete Option 2, which teaches you how to use the RDS console to automatically connect an EC2 instance to an RDS database, or you can complete Option 3, which teaches you how to manually configure the security groups that were automatically created in Option 1.
### Task 5 (Optional): Clean up Warning Terminating an instance is permanent and irreversible.
After you terminate an instance, you can no longer connect to it, and it can't be recovered.
All attached Amazon EBS volumes that are configured to be deleted on termination are also permanently deleted and can't be recovered. All data stored on instance store volumes is permanently lost. For more information, see How instance termination works.
Before you terminate an instance, ensure that you have backed up all data that you need to retain after the termination to persistent storage.
Now that you have completed the tutorial, it is good practice to clean up (delete) any resources you no longer want to use. Cleaning up AWS resources prevents your account from incurring any further charges.
If you launched an EC2 instance specifically for this tutorial, you can terminate it to stop incurring any charges associated with it.
To terminate an instance using the console
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Instances.
3. Select the instance that you created for this tutorial, and choose Instance state, Terminate instance.
4. Choose Terminate when prompted for confirmation.
If you created an RDS database specifically for this tutorial, you can delete it to stop incurring any charges associated with it.

To delete an RDS database using the console
1. Open the Amazon RDS console at https://console.aws.amazon.com/rds/.
2. In the navigation pane, choose Databases.
3. Select the RDS database that you created for this tutorial, and choose Actions, Delete.
4. Enter delete me in the box, and then choose Delete.
## Option 2: Automatically connect an instance to an RDS database using the RDS console the RDS console The objective of Option 2 is to explore the automatic connect feature in the RDS console that automatically configures the connection between your EC2 instance and RDS database to allow traffic from the EC2 instance to the RDS database. In Option 3, you'll learn how to manually configure the connection.
Tasks
- Before you begin
- Task 1 (Optional): Launch an EC2 instance
- Task 2: Create an RDS database and automatically connect it to your EC2 instance
- Task 3: Verify the connection configuration
- Task 4 (Optional): Clean up
### Before you begin You'll need the following to complete this tutorial:
- An EC2 instance that is in the same VPC as the RDS database. You can either use an existing EC2 instance or follow the steps in Task 1 to create a new instance.
- Permissions to call the following operations:
- ec2:AssociateRouteTable
- ec2:AuthorizeSecurityGroupEgress
- ec2:CreateRouteTable
- ec2:CreateSecurityGroup
- ec2:CreateSubnet

- ec2:DescribeInstances
- ec2:DescribeNetworkInterfaces
- ec2:DescribeRouteTables
- ec2:DescribeSecurityGroups
- ec2:DescribeSubnets
- ec2:ModifyNetworkInterfaceAttribute
- ec2:RevokeSecurityGroupEgress
### Task 1 (Optional): Launch an EC2 instance Note Launching an instance is not the focus of this tutorial. If you already have an Amazon EC2 instance and would like to use it in this tutorial, you can skip this task.
The objective of this task is to launch an EC2 instance so that you can complete Task 2 where you configure the connection between your EC2 instance and your Amazon RDS database. The steps in this task configure the EC2 instance as follows:
- Instance name: tutorial-instance-2
- AMI: Amazon Linux 2
- Instance type: t2.micro
- Auto-assign public IP: Enabled
- Security group with the following three rules:
- Allow SSH from your IP address
- Allow HTTPS traffic from anywhere
- Allow HTTP traffic from anywhere Important In a production environment, you should configure your instance to meet your specific needs.

To launch an EC2 instance
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. On the EC2 Dashboard, choose Launch instance.
3. Under Name and tags, for Name, enter a name to identify your instance. For this tutorial, name the instance tutorial-instance-2. While the instance name is not mandatory, when you select your instance in the RDS console, the name will help you easily identify it.
4. Under Application and OS Images, choose an AMI that meets your web server needs. This tutorial uses Amazon Linux.
5. Under Instance type, for Instance type, select an instance type that meets your web server needs. This tutorial uses t2.micro.
Note Depending on when you created your account, you might be eligible to use Amazon EC2 under the Free Tier.
If your created your AWS account before July 15, 2025 and it's less than 12 months old, you can use Amazon EC2 under the Free Tier by selecting the t2.micro instance type, or the t3.micro instance type in Regions where t2.micro is unavailable. Be aware that when you launch a t3.micro instance, it defaults to Unlimited mode, which might incur additional charges based on CPU usage. If an instance type can be used under the Free Tier, it is labeled Free tier eligible.
If you created your AWS account on or after July 15, 2025, you can use t3.micro, t3.small, t4g.micro, t4g.small, c7i-flex.large, and m7i-flex.large instance types for 6 months or until your credits are used up.
For more information, see Free Tier benefits before and after July 15, 2025.
6. Under Key pair (login), for Key pair name, choose your key pair.
7. Under Network settings, do the following: a.
For Network and Subnet, if you haven't made changes to your default VPC or subnets, you can keep the default settings.
If you have made changes to your default VPC or subnets, check the following: i.
The instance must be in the same VPC as the RDS database to use the automatic connection configuration. By default you have only one VPC.

ii.
The VPC that you're launching your instance into must have an internet gateway attached to it so that you can access your web server from the internet. Your default VPC is automatically set up with an internet gateway. iii.
To ensure that your instance receives a public IP address, for Auto-assign public IP, check that Enable is selected. If Disable is selected, choose Edit (to the right of Network Settings), and then, for Auto-assign public IP, choose Enable. b.
To connect to your instance by using SSH, you need a security group rule that authorizes SSH (Linux) or RDP (Windows) traffic from your computer's public IPv4 address. By default, when you launch an instance, a new security group is created with a rule that allows inbound SSH traffic from anywhere.
To make sure that only your IP address can connect to your instance, under Firewall (security groups), from the drop-down list next to the Allow SSH traffic from checkbox, choose My IP. c.
To allow traffic from the internet to your instance, select the following checkboxes:
- Allow HTTPs traffic from the internet
- Allow HTTP traffic from the internet
8. In the Summary panel, review your instance configuration and then choose Launch instance.
9. Choose View all instances to close the confirmation page and return to the console. Your instance will first be in a pending state, and will then go into the running state.
If the instance fails to launch or the state immediately goes to terminated instead of running, see Troubleshoot Amazon EC2 instance launch issues.
For more information about launching an instance, see Launch an EC2 instance using the launch instance wizard in the console.

#### View an animation: Launch an EC2 instance
### Task 2: Create an RDS database and automatically connect it to your EC2 instance The objective of this task is to create an RDS database and use the automatic connection feature in the RDS console to automatically configure the connection between your EC2 instance and your RDS database. The steps in this task configure the DB instance as follows:
- Engine type: MySQL
- Template: Free tier
- DB instance identifier: tutorial-database
- DB instance class: db.t3.micro

Important In a production environment, you should configure your instance to meet your specific needs.
To create an RDS database and automatically connect it to an EC2 instance
1. Open the Amazon RDS console at https://console.aws.amazon.com/rds/.
2. From the Region selector (at top right), choose the AWS Region in which you created the EC2 instance. The EC2 instance and the RDS database must be in the same Region.
3. On the dashboard, choose Create database.
4. Under Choose a database creation method, check that Standard create is selected. If you choose Easy create, the automatic connection feature is not available.
5. Under Engine options, for Engine type, choose MySQL.
6. Under Templates, choose a sample template to meet your needs. For this tutorial, choose Free tier to create an RDS database at no cost. However, note that the Free Tier is only available if your account qualifies for the Free Tier. You can read more by choosing the Info link in the Free tier box.
7. Under Settings, do the following: a.
For DB instance identifier, enter a name for the database. For this tutorial, enter tutorial-database. b.
For Master username, leave the default name, which is admin. c.
For Master password, enter a password that you can remember for this tutorial, and then, for Confirm password, enter the password again.
8. Under Instance configuration, for DB instance class, leave the default, which is db.t3.micro.
If your account qualifies for the Free Tier, you can use this instance for free. For more information, see AWS Free Tier.
9. Under Connectivity, for Compute resource, choose Connect to an EC2 compute resource.
This is the automatic connection feature in the RDS console .
10. For EC2 instance, choose the EC2 instance that you want to connect to. For the purposes of this tutorial, you can either choose the instance that you created in the previous task, which you named tutorial-instance, or choose another existing instance. If you don't see your instance in the list, choose the refresh icon to the right of Connectivity.

When you use the automatic connection feature, a security group is added to this EC2 instance, and another security group is added to the RDS database. The security groups are automatically configure to allow traffic between the EC2 instance and the RDS database. In the next task, you'll verify that the security groups were created and assigned to the EC2 instance and RDS database.
11. Choose Create database.
On the Databases screen, the Status of the new database is Creating until the database is ready to use. When the status changes to Available, you can connect to the database.
Depending on the database class and the amount of storage, it can take up to 20 minutes before the new database is available.
To learn more, see  Configure automatic network connectivity with an EC2 instance in the Amazon RDS User Guide.

#### View an animation: Create an RDS database and automatically connect it to an EC2 instance
### Task 3: Verify the connection configuration The objective of this task is to verify that the two security groups were created and assigned to the instance and database.
When you use the automatic connection feature in the console to configure the connectivity, the security groups are automatically created and assigned to the instance and database, as follows:

- Security group rds-ec2-x is created and added to the RDS database. It has one inbound rule that references the ec2-rds-x security group as its source. This allows traffic from the EC2 instance with the ec2-rds-x security group to reach the RDS database.
- Security group ec2-rds-x is created and added to the EC2 instance. It has one outbound rule that references the rds-ec2-x security group as its destination. This allows traffic from the EC2 instance to reach the RDS database with the rds-ec2-x security group.
To verify the connection configuration using the console
1. Open the Amazon RDS console at https://console.aws.amazon.com/rds/.
2. In the navigation page, choose Databases.
3. Choose the RDS database that you created for this tutorial.
4. On the Connectivity & security tab, under Security, VPC security groups, verify that a security group called rds-ec2-x is displayed.
5. Choose the rds-ec2-x security group. The Security Groups screen in the EC2 console opens.
6. Choose the rds-ec2-x security group to open it.
7. Choose the Inbound rules tab.
8. Verify that the following security group rule exists, as follows:
- Type: MYSQL/Aurora
- Port range: 3306
- Source: sg-0987654321example / ec2-rds-x – This is the security group that is assigned to the EC2 instance that you verified in the preceding steps.
- Description: Rule to allow connections from EC2 instances with sg-1234567890example attached
9. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
10. In the navigation pane, choose Instances.
11. Choose the EC2 instance that you selected to connect to the RDS database in the previous task, and choose the Security tab.
12. Under Security details, Security groups, verify that a security group called ec2-rds-x is in the list. x is a number.
13. Choose the ec2-rds-x security group to open it.
14. Choose the Outbound rules tab.

15. Verify that the following security group rule exists, as follows:
- Type: MYSQL/Aurora
- Port range: 3306
- Destination: sg-1234567890example / rds-ec2-x
- Description: Rule to allow connections to database-tutorial from any instances this security group is attached to By verifying that these security groups and security group rules exist and that they are assigned to the RDS database and EC2 instance as described in this procedure, you can verify that the connection was automatically configured by using the automatic connection feature.
#### View an animation: Verify the connection configuration

You have completed Option 2 of this tutorial. You can now either complete Option 3, which teaches you how to manually configure the security groups that were automatically created in Option 2.
### Task 4 (Optional): Clean up Warning Terminating an instance is permanent and irreversible.
After you terminate an instance, you can no longer connect to it, and it can't be recovered.
All attached Amazon EBS volumes that are configured to be deleted on termination are also permanently deleted and can't be recovered. All data stored on instance store volumes is permanently lost. For more information, see How instance termination works.
Before you terminate an instance, ensure that you have backed up all data that you need to retain after the termination to persistent storage.
Now that you have completed the tutorial, it is good practice to clean up (delete) any resources you no longer want to use. Cleaning up AWS resources prevents your account from incurring any further charges.
If you launched an EC2 instance specifically for this tutorial, you can terminate it to stop incurring any charges associated with it.
To terminate an instance using the console
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Instances.
3. Select the instance that you created for this tutorial, and choose Instance state, Terminate instance.
4. Choose Terminate when prompted for confirmation.
If you created an RDS database specifically for this tutorial, you can delete it to stop incurring any charges associated with it.
To delete an RDS database using the console
1. Open the Amazon RDS console at https://console.aws.amazon.com/rds/.

2. In the navigation pane, choose Databases.
3. Select the RDS database that you created for this tutorial, and choose Actions, Delete.
4. Enter delete me in the box, and then choose Delete.
## Option 3: Manually connect an instance to an RDS database by creating security groups security groups The objective of Option 3 is to learn how to manually configure the connection between an EC2 instance and an RDS database by manually reproducing the configuration of the automatic connection feature.
Tasks
- Before you begin
- Task 1 (Optional): Launch an EC2 instance
- Task 2 (Optional): Create an RDS database
- Task 3: Manually connect your EC2 instance to your RDS database by creating security groups and assigning them to the instances
- Task 4 (Optional): Clean up
### Before you begin You'll need the following to complete this tutorial:
- An EC2 instance that is in the same VPC as the RDS database. You can either use an existing EC2 instance or follow the steps in Task 1 to create a new instance.
- An RDS database that is in the same VPC as the EC2 instance. You can either use an existing RDS database or follow the steps in Task 2 to create a new database.
- Permissions to call the following operations:
- ec2:AssociateRouteTable
- ec2:AuthorizeSecurityGroupEgress
- ec2:CreateRouteTable
- ec2:CreateSecurityGroup
- ec2:CreateSubnet

- ec2:DescribeInstances
- ec2:DescribeNetworkInterfaces
- ec2:DescribeRouteTables
- ec2:DescribeSecurityGroups
- ec2:DescribeSubnets
- ec2:ModifyNetworkInterfaceAttribute
- ec2:RevokeSecurityGroupEgress
### Task 1 (Optional): Launch an EC2 instance Note Launching an instance is not the focus of this tutorial. If you already have an Amazon EC2 instance and would like to use it in this tutorial, you can skip this task.
The objective of this task is to launch an EC2 instance so that you can complete Task 3 where you configure the connection between your EC2 instance and your Amazon RDS database. The steps in this task configure the EC2 instance as follows:
- Instance name: tutorial-instance
- AMI: Amazon Linux 2
- Instance type: t2.micro
- Auto-assign public IP: Enabled
- Security group with the following three rules:
- Allow SSH from your IP address
- Allow HTTPS traffic from anywhere
- Allow HTTP traffic from anywhere Important In a production environment, you should configure your instance to meet your specific needs.

To launch an EC2 instance
1. Sign in to the AWS Management Console and open the Amazon EC2 console at https:// console.aws.amazon.com/ec2/.
2. On the EC2 Dashboard, choose Launch instance.
3. Under Name and tags, for Name, enter a name to identify your instance. For this tutorial, name the instance tutorial-instance-manual-1. While the instance name is not mandatory, the name will help you easily identify it.
4. Under Application and OS Images, choose an AMI that meets your web server needs. This tutorial uses Amazon Linux.
5. Under Instance type, for Instance type, select an instance type that meets your web server needs. This tutorial uses t2.micro.
Note Depending on when you created your account, you might be eligible to use Amazon EC2 under the Free Tier.
If your created your AWS account before July 15, 2025 and it's less than 12 months old, you can use Amazon EC2 under the Free Tier by selecting the t2.micro instance type, or the t3.micro instance type in Regions where t2.micro is unavailable. Be aware that when you launch a t3.micro instance, it defaults to Unlimited mode, which might incur additional charges based on CPU usage. If an instance type can be used under the Free Tier, it is labeled Free tier eligible.
If you created your AWS account on or after July 15, 2025, you can use t3.micro, t3.small, t4g.micro, t4g.small, c7i-flex.large, and m7i-flex.large instance types for 6 months or until your credits are used up.
For more information, see Free Tier benefits before and after July 15, 2025.
6. Under Key pair (login), for Key pair name, choose your key pair.
7. Under Network settings, do the following: a.
For Network and Subnet, if you haven't made changes to your default VPC or subnets, you can keep the default settings.
If you have made changes to your default VPC or subnets, check the following:

i.
The instance must be in the same VPC as the RDS database. By default you have only one VPC. ii.
The VPC that you're launching your instance into must have an internet gateway attached to it so that you can access your web server from the internet. Your default VPC is automatically set up with an internet gateway. iii.
To ensure that your instance receives a public IP address, for Auto-assign public IP, check that Enable is selected. If Disable is selected, choose Edit (to the right of Network Settings), and then, for Auto-assign public IP, choose Enable. b.
To connect to your instance by using SSH, you need a security group rule that authorizes SSH (Linux) or RDP (Windows) traffic from your computer's public IPv4 address. By default, when you launch an instance, a new security group is created with a rule that allows inbound SSH traffic from anywhere.
To make sure that only your IP address can connect to your instance, under Firewall (security groups), from the drop-down list next to the Allow SSH traffic from checkbox, choose My IP. c.
To allow traffic from the internet to your instance, select the following checkboxes:
- Allow HTTPs traffic from the internet
- Allow HTTP traffic from the internet
8. In the Summary panel, review your instance configuration and then choose Launch instance.
9. Choose View all instances to close the confirmation page and return to the console. Your instance will first be in a pending state, and will then go into the running state.
If the instance fails to launch or the state immediately goes to terminated instead of running, see Troubleshoot Amazon EC2 instance launch issues.
For more information about launching an instance, see Launch an EC2 instance using the launch instance wizard in the console.

#### View an animation: Launch an EC2 instance
### Task 2 (Optional): Create an RDS database Note Creating an RDS database is not the focus of this part of the tutorial. If you already have an RDS database and would like to use it for this tutorial, you can skip this task.
The objective of this task is to create an RDS database. You'll use this instance in Task 3 when you connect it to your EC2 instance. The steps in this task configure the RDS database as follows:
- Engine type: MySQL
- Template: Free tier
- DB instance identifier: tutorial-database-manual
- DB instance class: db.t3.micro

Important In a production environment, you should configure your instance to meet your specific needs.
To create a MySQL DB instance
1. Open the Amazon RDS console at https://console.aws.amazon.com/rds/.
2. From the Region selector (at top right), choose the AWS Region in which you created the EC2 instance. The EC2 instance and the DB instance must be in the same Region.
3. On the dashboard, choose Create database.
4. Under Choose a database creation method, choose Easy create. When you choose this option, the automatic connection feature to automatically configure the connection is not available.
5. Under Engine options, for Engine type, choose MySQL.
6. For DB instance size, choose Free tier.
7. For DB instance identifier enter a name for the RDS database. For this tutorial, enter tutorial-database-manual.
8. For Master username, leave the default name, which is admin.
9. For Master password, enter a password that you can remember for this tutorial, and then, for Confirm password, enter the password again.
10. Choose Create database.
On the Databases screen, the Status of the new DB instance is Creating until the DB instance is ready to use. When the status changes to Available, you can connect to the DB instance.
Depending on the DB instance class and the amount of storage, it can take up to 20 minutes before the new instance is available.

#### View an animation: Create a DB instance
### Task 3: Manually connect your EC2 instance to your RDS database by creating security groups and assigning them to the instances security groups and assigning them to the instances The objective of this task is to reproduce the connection configuration of the automatic connection feature by performing the following manually: You create two new security groups, and then add a security group each to the EC2 instance and the RDS database.
To create two new security groups and assign one each to the EC2 instance and RDS database
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. First create the security group to add to the EC2 instance, as follows:

a.
In the navigation pane, choose Security Groups. b.
Choose Create security group. c.
For Security group name, enter a descriptive name for the security group. For this tutorial, enter ec2-rds-manual-configuration. d.
For Description, enter a brief description. For this tutorial, enter EC2 instance security group to allow EC2 instance to securely connect to RDS database. e.
Choose Create security group. You'll come back to this security group to add an outbound rule after you've created the RDS database security group.
3. Now, create the security group to add to the RDS database, as follows: a.
In the navigation pane, choose Security Groups. b.
Choose Create security group. c.
For Security group name, enter a descriptive name for the security group. For this tutorial, enter rds-ec2-manual-configuration. d.
For Description, enter a brief description. For this tutorial, enter RDS database security group to allow EC2 instance to securely connect to RDS database. e.
Under Inbound rules, choose Add rule, and do the following: i.
For Type, choose MYSQL/Aurora. ii.
For Source, choose the EC2 instance security group ec2-rds-manual-configuration that you created in Step 2 of this procedure. f.
Choose Create security group.
4. Edit the EC2 instance security group to add an outbound rule, as follows: a.
In the navigation pane, choose Security Groups. b.
Select the EC2 instance security group (you named it ec2-rds-manual- configuration), and choose the Outbound rules tab. c.
Choose Edit outbound rules. d.
Choose Add rule, and do the following: i.
For Type, choose MYSQL/Aurora.

ii.
For Destination, choose the RDS database security group rds-ec2-manual- configuration that you created in Step 3 of this procedure. iii.
Choose Save rules.
5. Add the EC2 instance security group to the EC2 instance as follows: a.
In the navigation pane, choose Instances. b.
Select your EC2 instance, and choose Actions, Security, Change security groups. c.
Under Associated security groups, choose the Select security groups field, choose ec2- rds-manual-configuration that you created earlier, and then choose Add security group. d.
Choose Save.
6. Add the RDS database security group to the RDS database as follows: a.
Open the Amazon RDS console at https://console.aws.amazon.com/rds/. b.
In the navigation pane, choose Databases and select your database. c.
Choose Modify. d.
Under Connectivity, for Security group, choose rds-ec2-manual-configuration that you created earlier, and then choose Continue. e.
Under Scheduling of modifications, choose Apply immediately. f.
Choose Modify DB instance.
You have now completed the manual steps that mimic the automatic steps that occur when you use the automatic connection feature.
You have completed Option 3 of this tutorial. If you've completed Options 1, 2, and 3, and you no longer need the resources that were created in this tutorial, you should delete them to prevent incurring unnecessary costs. For more information, see Task 4 (Optional): Clean up.
### Task 4 (Optional): Clean up Warning Terminating an instance is permanent and irreversible.
After you terminate an instance, you can no longer connect to it, and it can't be recovered.
All attached Amazon EBS volumes that are configured to be deleted on termination are

also permanently deleted and can't be recovered. All data stored on instance store volumes is permanently lost. For more information, see How instance termination works.
Before you terminate an instance, ensure that you have backed up all data that you need to retain after the termination to persistent storage.
Now that you have completed the tutorial, it is good practice to clean up (delete) any resources you no longer want to use. Cleaning up AWS resources prevents your account from incurring any further charges.
If you launched an EC2 instance specifically for this tutorial, you can terminate it to stop incurring any charges associated with it.
To terminate an instance using the console
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Instances.
3. Select the instance that you created for this tutorial, and choose Instance state, Terminate instance.
4. Choose Terminate when prompted for confirmation.
If you created an RDS database specifically for this tutorial, you can delete it to stop incurring any charges associated with it.
To delete an RDS database using the console
1. Open the Amazon RDS console at https://console.aws.amazon.com/rds/.
2. In the navigation pane, choose Databases.
3. Select the RDS database that you created for this tutorial, and choose Actions, Delete.
4. Enter delete me in the box, and then choose Delete.
