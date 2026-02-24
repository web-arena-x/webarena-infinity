# EC2 Serial Console for instances

Source: apps/user-manuals/aws/ec2-ug.pdf

---

aws ssm send-command --instance-ids "i-0cb2b964d3e14fd9f" --document-name "AWSSupport- RunEC2RescueForWindowsTool" --parameters "Command=ResetAccess, Parameters=a133dc3c- a2g4-4fc6-a873-6c0720104bf0" --output text Note In this example, the KMS key is a133dc3c-a2g4-4fc6-a873-6c0720104bf0.
# EC2 Serial Console for instances With the EC2 serial console, you have access to your Amazon EC2 instance's serial port, which you can use to troubleshoot boot, network configuration, and other issues. The serial console does not require your instance to have any networking capabilities. With the serial console, you can enter commands to an instance as if your keyboard and monitor are directly attached to the instance's serial port. The serial console session lasts during instance reboot and stop. During reboot, you can view all of the boot messages from the start.
Access to the serial console is not available by default. Your organization must grant account access to the serial console and configure IAM policies to grant your users access to the serial console.
Serial console access can be controlled at a granular level by using instance IDs, resource tags, and other IAM levers. For more information, see Configure access to the EC2 Serial Console.
The serial console can be accessed by using the EC2 console or the AWS CLI.
The serial console is available at no additional cost.
Topics
- Prerequisites for the EC2 Serial Console
- Configure access to the EC2 Serial Console
- Connect to the EC2 Serial Console
- Disconnect from the EC2 Serial Console
- Troubleshoot your Amazon EC2 instance using the EC2 Serial Console

## Prerequisites for the EC2 Serial Console To connect to the EC2 Serial Console and use your chosen tool for troubleshooting, the following prerequisites must be met:
- AWS Regions
- Wavelength Zones and AWS Outposts
- Local Zones
- Instance types
- Grant access
- Support for browser-based client
- Instance state
- Amazon EC2 Systems Manager
- Configure your chosen troubleshooting tool
### AWS Regions Supported in all AWS Regions except Asia Pacific (Taipei).
### Wavelength Zones and AWS Outposts Not supported.
### Local Zones Supported in all Local Zones.
### Instance types Supported instance types:
- Linux
- All virtualized instances built on the Nitro System.
- All bare metal instances except:
- General purpose: a1.metal, mac1.metal, mac2.metal
- Accelerated computing: g5g.metal

- Memory optimized: u-6tb1.metal, u-9tb1.metal, u-12tb1.metal, u-18tb1.metal, u-24tb1.metal
- Windows All virtualized instances built on the Nitro System. Not supported on bare metal instances.
### Grant access You must complete the configuration tasks to grant access to the EC2 Serial Console. For more information, see Configure access to the EC2 Serial Console.
### Support for browser-based client To connect to the serial console using the browser-based client, your browser must support WebSocket. If your browser does not support WebSocket, connect to the serial console using your own key and an SSH client.
### Instance state Must be running.
You can't connect to the serial console if the instance is in the pending, stopping, stopped, shutting-down, or terminated state.
For more information about the instance states, see Amazon EC2 instance state changes.
### Amazon EC2 Systems Manager If the instance uses Amazon EC2 Systems Manager, then SSM Agent version 3.0.854.0 or later must be installed on the instance. For information about SSM Agent, see Working with SSM Agent in the AWS Systems Manager User Guide.
### Configure your chosen troubleshooting tool To troubleshoot your instance using the serial console, you can use GRUB or SysRq on Linux instances, and Special Admin Console (SAC) on Windows instances. Before you can use these tools, you must first perform configuration steps on every instance on which you'll use them.
Use the instructions for your instance's operating system to configure your chosen troubleshooting tool.

#### (Linux instances) Configure GRUB To configure GRUB, choose one of the following procedures based on the AMI that was used to launch the instance.
Amazon Linux 2 To configure GRUB on an Amazon Linux 2 instance
1. Connect to your Linux instance using SSH
2. Add or change the following options in /etc/default/grub:
- Set GRUB_TIMEOUT=1.
- Add GRUB_TERMINAL="console serial".
- Add GRUB_SERIAL_COMMAND="serial --speed=115200".
The following is an example of /etc/default/grub. You might need to change the configuration based on your system setup.
GRUB_CMDLINE_LINUX_DEFAULT="console=tty0 console=ttyS0,115200n8 net.ifnames=0 biosdevname=0 nvme_core.io_timeout=4294967295 rd.emergency=poweroff rd.shell=0"
GRUB_TIMEOUT=1 GRUB_DISABLE_RECOVERY="true"
GRUB_TERMINAL="console serial"
GRUB_SERIAL_COMMAND="serial --speed=115200"
3. Apply the updated configuration by running the following command.
[ec2-user ~]$ sudo grub2-mkconfig -o /boot/grub2/grub.cfg Ubuntu To configure GRUB on an Ubuntu instance
1. Connect to your instance.
2. Add or change the following options in /etc/default/grub.d/50-cloudimg- settings.cfg:
- Set GRUB_TIMEOUT=1.

- Add GRUB_TIMEOUT_STYLE=menu.
- Add GRUB_TERMINAL="console serial".
- Remove GRUB_HIDDEN_TIMEOUT.
- Add GRUB_SERIAL_COMMAND="serial --speed=115200".
The following is an example of /etc/default/grub.d/50-cloudimg-settings.cfg.
You might need to change the configuration based on your system setup.
# Cloud Image specific Grub settings for Generic Cloud Images
# CLOUD_IMG: This file was created/modified by the Cloud Image build process
# Set the recordfail timeout GRUB_RECORDFAIL_TIMEOUT=0
# Do not wait on grub prompt GRUB_TIMEOUT=1 GRUB_TIMEOUT_STYLE=menu
# Set the default commandline GRUB_CMDLINE_LINUX_DEFAULT="console=tty1 console=ttyS0 nvme_core.io_timeout=4294967295"
# Set the grub console type GRUB_TERMINAL="console serial"
GRUB_SERIAL_COMMAND="serial --speed 115200"
3. Apply the updated configuration by running the following command.
[ec2-user ~]$ sudo update-grub RHEL To configure GRUB on a RHEL instance
1. Connect to your instance.
2. Add or change the following options in /etc/default/grub:
- Remove GRUB_TERMINAL_OUTPUT.

- Add GRUB_TERMINAL="console serial".
- Add GRUB_SERIAL_COMMAND="serial --speed=115200".
The following is an example of /etc/default/grub. You might need to change the configuration based on your system setup.
GRUB_TIMEOUT=1 GRUB_DISTRIBUTOR="$(sed 's, release .*$,,g' /etc/system-release)"
GRUB_DEFAULT=saved GRUB_DISABLE_SUBMENU=true GRUB_CMDLINE_LINUX="console=tty0 console=ttyS0,115200n8 net.ifnames=0 rd.blacklist=nouveau nvme_core.io_timeout=4294967295 crashkernel=auto"
GRUB_DISABLE_RECOVERY="true"
GRUB_ENABLE_BLSCFG=true GRUB_TERMINAL="console serial"
GRUB_SERIAL_COMMAND="serial --speed=115200"
3. Apply the updated configuration by running the following command.
[ec2-user ~]$ sudo grub2-mkconfig -o /boot/grub2/grub.cfg --update-bls-cmdline For RHEL 9.2 and earlier, use the following command.
[ec2-user ~]$ sudo grub2-mkconfig -o /boot/grub2/grub.cfg CentOS For instances that are launched using a CentOS AMI, GRUB is configured for the serial console by default.
The following is an example of /etc/default/grub. Your configuration might be different based on your system setup.
GRUB_TIMEOUT=1 GRUB_DISTRIBUTOR="$(sed 's, release .*$,,g' /etc/system-release)"
GRUB_DEFAULT=saved GRUB_DISABLE_SUBMENU=true GRUB_TERMINAL="serial console"
GRUB_SERIAL_COMMAND="serial --speed=115200"

GRUB_CMDLINE_LINUX="console=tty0 crashkernel=auto console=ttyS0,115200"
GRUB_DISABLE_RECOVERY="true"
#### (Linux instances) Configure SysRq To configure SysRq, you enable the SysRq commands for the current boot cycle. To make the configuration persistent, you can also enable the SysRq commands for subsequent boots.
To enable all SysRq commands for the current boot cycle
1. Connect to your instance.
2. Run the following command.
[ec2-user ~]$ sudo sysctl -w kernel.sysrq=1 This setting will clear on the next reboot.
To enable all SysRq commands for subsequent boots
1. Create the file /etc/sysctl.d/99-sysrq.conf and open it in your favorite editor.
[ec2-user ~]$ sudo vi /etc/sysctl.d/99-sysrq.conf
2. Add the following line. kernel.sysrq=1
3. Reboot the instance to apply the changes.
[ec2-user ~]$ sudo reboot
4. At the login prompt, enter the username of the password-based user that you set up previously, and then press Enter.
5. At the Password prompt, enter the password, and then press Enter.

#### (Windows instances) Enable SAC and the boot menu Note If you enable SAC on an instance, the EC2 services that rely on password retrieval will not work from the Amazon EC2 console. Windows on Amazon EC2 launch agents (EC2Config, EC2Launch v1, and EC2Launch v2) rely on the serial console to execute various tasks.
These tasks do not perform successfully when you enable SAC on an instance. For more information about Windows on Amazon EC2 launch agents, see the section called "Configure Windows instances". If you enable SAC, you can disable it later. For more information, see Disable SAC and the boot menu.
Use one of the following methods to enable SAC and the boot menu on an instance.
PowerShell To enable SAC and the boot menu on a Windows instance
1. Connect to your instance and perform the following steps from an elevated PowerShell command line.
2. Enable SAC. bcdedit /ems '{current}' on bcdedit /emssettings EMSPORT:1 EMSBAUDRATE:115200
3. Enable the boot menu. bcdedit /set '{bootmgr}' displaybootmenu yes bcdedit /set '{bootmgr}' timeout 15 bcdedit /set '{bootmgr}' bootems yes
4. Apply the updated configuration by rebooting the instance. shutdown -r -t 0

Command prompt To enable SAC and the boot menu on a Windows instance
1. Connect to your instance and perform the following steps from the command prompt.
2. Enable SAC. bcdedit /ems {current} on bcdedit /emssettings EMSPORT:1 EMSBAUDRATE:115200
3. Enable the boot menu. bcdedit /set {bootmgr} displaybootmenu yes bcdedit /set {bootmgr} timeout 15 bcdedit /set {bootmgr} bootems yes
4. Apply the updated configuration by rebooting the instance. shutdown -r -t 0
## Configure access to the EC2 Serial Console To configure access to the serial console, you must grant serial console access at the account level and then configure IAM policies to grant access to your users. For Linux instances you must also configure a password-based user on every instance so that your users can use the serial console for troubleshooting.
EC2 Serial Console uses a virtual serial port connection to interact with an instance. This connection is independent of the instance VPC, so that you can work with the instance operating system and run troubleshooting tools even if there are boot failures or network configuration issues. Because this connection is outside of the VPC network, EC2 Serial Console does not use the instance security group or the subnet network ACL to authorize traffic to the instance.
Before you begin Verify that the prerequisites are met.
Contents
- Levels of access to the EC2 Serial Console

- Manage account access to the EC2 Serial Console
- Configure IAM policies for EC2 Serial Console access
- Set an OS user password on a Linux instance
### Levels of access to the EC2 Serial Console By default, there is no access to the serial console at the account level. You need to explicitly grant access to the serial console at the account level. For more information, see Manage account access to the EC2 Serial Console.
You can use a service control policy (SCP) to allow access to the serial console within your organization. You can then have granular access control at the user level by using an IAM policy to control access. By using a combination of SCP and IAM policies, you have different levels of access control to the serial console.
Organization level You can use a service control policy (SCP) to allow access to the serial console for member accounts within your organization. For more information about SCPs, see Service control policies in the AWS Organizations User Guide.
Instance level You can configure the serial console access policies by using IAM PrincipalTag and ResourceTag constructions and by specifying instances by their ID. For more information, see Configure IAM policies for EC2 Serial Console access.
User level You can configure access at the user level by configuring an IAM policy to allow or deny a specified user the permission to push the SSH public key to the serial console service of a particular instance. For more information, see Configure IAM policies for EC2 Serial Console access.
OS level (Linux instances only)
You can set a user password at the guest OS level. This provides access to the serial console for some use cases. However, to monitor the logs, you don't need a password-based user. For more information, see Set an OS user password on a Linux instance.

### Manage account access to the EC2 Serial Console By default, there is no access to the serial console at the account level. You need to explicitly grant access to the serial console at the account level.
This setting is configured at the account level, either directly in the account or by using a declarative policy. It must be configured in each AWS Region where you want to grant access to the serial console. Using a declarative policy allows you to apply the setting across multiple Regions simultaneously, as well as across multiple accounts simultaneously. When a declarative policy is in use, you can't modify the setting directly within an account. This topic describes how to configure the setting directly within an account. For information about using declarative policies, see Declarative policies in the AWS Organizations User Guide.
Contents
- Grant permission to users to manage account access
- View account access status to the serial console
- Grant account access to the serial console
- Deny account access to the serial console
#### Grant permission to users to manage account access To allow your users to manage account access to the EC2 serial console, you need to grant them the required IAM permissions.
The following policy grants permissions to view the account status, and to allow and prevent account access to the EC2 serial console.
JSON { "Version":"2012-10-17", "Statement": [ { "Effect": "Allow", "Action": [ "ec2:GetSerialConsoleAccessStatus", "ec2:EnableSerialConsoleAccess", "ec2:DisableSerialConsoleAccess"

            ], "Resource": "*"
        } ]
} For more information, see Creating IAM policies in the IAM User Guide.
#### View account access status to the serial console Console To view account access to the serial console
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. On the left navigation pane, choose EC2 Dashboard.
3. From Account attributes, choose EC2 Serial Console.
4. On the EC2 Serial Console tab, the value of EC2 Serial Console access is either Allowed or Prevented.
AWS CLI To view account access to the serial console Use the get-serial-console-access-status command. aws ec2 get-serial-console-access-status The following is example output. A value of true indicates that the account is allowed access to the serial console.
{ "SerialConsoleAccessEnabled": true, "ManagedBy": "account"
} The ManagedBy field indicates the entity that configured the setting. The possible values are account (configured directly) or declarative-policy. For more information, see Declarative policies in the AWS Organizations User Guide.

PowerShell To view account access to the serial console Use the Get-EC2SerialConsoleAccessStatus cmdlet.
Get-EC2SerialConsoleAccessStatus -Select * The following is example output. A value of True indicates that the account is allowed access to the serial console.
ManagedBy SerialConsoleAccessEnabled --------- -------------------------- account   True The ManagedBy field indicates the entity that configured the setting. The possible values are account (configured directly) or declarative-policy. For more information, see Declarative policies in the AWS Organizations User Guide.
#### Grant account access to the serial console Console To grant account access to the serial console
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. On the left navigation pane, choose EC2 Dashboard.
3. From Account attributes, choose EC2 Serial Console.
4. Choose Manage.
5. To allow access to the EC2 serial console of all instances in the account, select the Allow checkbox.
6. Choose Update.
AWS CLI To grant account access to the serial console Use the enable-serial-console-access command.

aws ec2 enable-serial-console-access The following is example output.
{ "SerialConsoleAccessEnabled": true } PowerShell To grant account access to the serial console Use the Enable-EC2SerialConsoleAccess cmdlet.
Enable-EC2SerialConsoleAccess The following is example output.
True
#### Deny account access to the serial console Console To deny account access to the serial console
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. On the left navigation pane, choose EC2 Dashboard.
3. From Account attributes, choose EC2 Serial Console.
4. Choose Manage.
5. To prevent access to the EC2 serial console of all instances in the account, clear the Allow checkbox.
6. Choose Update.
AWS CLI To deny account access to the serial console

Use the disable-serial-console-access command. aws ec2 disable-serial-console-access The following is example output.
{ "SerialConsoleAccessEnabled": false } PowerShell To deny account access to the serial console Use the Disable-EC2SerialConsoleAccess cmdlet.
Disable-EC2SerialConsoleAccess The following is example output.
False
### Configure IAM policies for EC2 Serial Console access By default, your users do not have access to the serial console. Your organization must configure IAM policies to grant your users the required access. For more information, see Creating IAM policies in the IAM User Guide.
For serial console access, create a JSON policy document that includes the ec2-instance- connect:SendSerialConsoleSSHPublicKey action. This action grants a user permission to push the public key to the serial console service, which starts a serial console session. We recommend restricting access to specific EC2 instances. Otherwise, all users with this permission can connect to the serial console of all EC2 instances.
Example IAM policies
- Explicitly allow access to the serial console
- Explicitly deny access to the serial console

- Use resource tags to control access to the serial console
#### Explicitly allow access to the serial console By default, no one has access to the serial console. To grant access to the serial console, you need to configure a policy to explicitly allow access. We recommend configuring a policy that restricts access to specific instances.
The following policy allows access to the serial console of a specific instance, identified by its instance ID.
Note that the DescribeInstances, DescribeInstanceTypes, and GetSerialConsoleAccessStatus actions do not support resource-level permissions, and therefore all resources, indicated by the * (asterisk), must be specified for these actions.
JSON { "Version":"2012-10-17", "Statement": [ { "Sid": "AllowDescribeInstances", "Effect": "Allow", "Action": [ "ec2:DescribeInstances", "ec2:DescribeInstanceTypes", "ec2:GetSerialConsoleAccessStatus"
            ], "Resource": "*"
        }, { "Sid": "AllowinstanceBasedSerialConsoleAccess", "Effect": "Allow", "Action": [ "ec2-instance-connect:SendSerialConsoleSSHPublicKey"
            ], "Resource": "arn:aws:ec2:us- east-1:111122223333:instance/i-0598c7d356eba48d7"
        } ]
}

#### Explicitly deny access to the serial console The following IAM policy allows access to the serial console of all instances, denoted by the * (asterisk), and explicitly denies access to the serial console of a specific instance, identified by its ID.
JSON { "Version":"2012-10-17", "Statement": [ { "Sid": "AllowSerialConsoleAccess", "Effect": "Allow", "Action": [ "ec2-instance-connect:SendSerialConsoleSSHPublicKey", "ec2:DescribeInstances", "ec2:DescribeInstanceTypes", "ec2:GetSerialConsoleAccessStatus"
            ], "Resource": "*"
        }, { "Sid": "DenySerialConsoleAccess", "Effect": "Deny", "Action": [ "ec2-instance-connect:SendSerialConsoleSSHPublicKey"
            ], "Resource": "arn:aws:ec2:us- east-1:111122223333:instance/i-0598c7d356eba48d7"
        } ]
}
#### Use resource tags to control access to the serial console You can use resource tags to control access to the serial console of an instance.
Attribute-based access control is an authorization strategy that defines permissions based on tags that can be attached to users and AWS resources. For example, the following policy allows a user to initiate a serial console connection for an instance only if that instance's resource tag and the principal's tag have the same SerialConsole value for the tag key.

For more information about using tags to control access to your AWS resources, see Controlling access to AWS resources in the IAM User Guide.
Note that the DescribeInstances, DescribeInstanceTypes, and GetSerialConsoleAccessStatus actions do not support resource-level permissions, and therefore all resources, indicated by the * (asterisk), must be specified for these actions.
JSON { "Version":"2012-10-17", "Statement": [ { "Sid": "AllowDescribeInstances", "Effect": "Allow", "Action": [ "ec2:DescribeInstances", "ec2:DescribeInstanceTypes", "ec2:GetSerialConsoleAccessStatus"
            ], "Resource": "*"
        }, { "Sid": "AllowTagBasedSerialConsoleAccess", "Effect": "Allow", "Action": [ "ec2-instance-connect:SendSerialConsoleSSHPublicKey"
            ], "Resource": "arn:aws:ec2:us-east-1:111122223333:instance/*", "Condition": { "StringEquals": { "aws:ResourceTag/SerialConsole":
 "${aws:PrincipalTag/SerialConsole}"
                } } } ]
}

### Set an OS user password on a Linux instance You can connect to the serial console without a password. However, to use the serial console for troubleshooting a Linux instance, the instance must have a password-based OS user.
You can set the password for any OS user, including the root user. Note that the root user can modify all files, while each OS user might have limited permissions.
You must set a user password for every instance for which you will use the serial console. This is a one-time requirement for each instance.
Note By default, AMIs provided by AWS are not configured with a password-based user. If you launched your instance using an AMI that already has the root user password configured, you can skip these instructions.
To set an OS user password on a Linux instance
1. Connect to your instance. You can use any method for connecting to your instance, except the EC2 Serial Console connection method.
2. To set the password for a user, use the passwd command. In the following example, the user is root.
[ec2-user ~]$ sudo passwd root The following is example output.
Changing password for user root.
New password:
3. At the New password prompt, enter the new password.
4. At the prompt, re-enter the password.
## Connect to the EC2 Serial Console You can connect to the serial console of your EC2 instance by using the Amazon EC2 console or through SSH. After connecting to the serial console, you can use it for troubleshooting boot,

network configuration, and other issues. For more information about troubleshooting, see Troubleshoot your Amazon EC2 instance using the EC2 Serial Console.
Considerations
- Only 1 active serial console connection is supported per instance.
- The serial console connection typically lasts for 1 hour unless you disconnect from it. However, during system maintenance, Amazon EC2 will disconnect the serial console session.
The duration of the connection is not determined by the duration of your IAM credentials. If your IAM credentials expire, the connection continues to persist until the maximum duration of the serial console connection is reached. When using the EC2 Serial Console console experience, if your IAM credentials expire, terminate the connection by closing the browser page.
- It takes 30 seconds to tear down a session after you've disconnected from the serial console in order to allow a new session.
- Supported serial console ports: ttyS0 (Linux instances) and COM1 (Windows instances)
- When you connect to the serial console, you might observe a slight drop in your instance's throughput.
Topics
- Connect using the browser-based client
- Connect using your own key and SSH client
- EC2 Serial Console endpoints and fingerprints
### Connect using the browser-based client You can connect to your EC2 instance's serial console by using the browser-based client. You do this by selecting the instance in the Amazon EC2 console and choosing to connect to the serial console.
The browser-based client handles the permissions and provides a successful connection.
EC2 serial console works from most browsers, and supports keyboard and mouse input.
Before connecting, make sure you have completed the prerequisites.
To connect to your instance's serial port using the browser-based client (Amazon EC2 console)
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.

2. In the navigation pane, choose Instances.
3. Select the instance and choose Actions, Monitor and troubleshoot, EC2 Serial Console, Connect.
Alternatively, select the instance and choose Connect, EC2 Serial Console, Connect.
An in-browser terminal window opens.
4. Press Enter. If a login prompt returns, you are connected to the serial console.
If the screen remains black, you can use the following information to help resolve issues with connecting to the serial console:
- Check that you have configured access to the serial console. For more information, see Configure access to the EC2 Serial Console.
- (Linux instances only) Use SysRq to connect to the serial console. SysRq does not require that you connect using the browser-based client. For more information, see (Linux instances)
Use SysRq to troubleshoot your instance.
- (Linux instances only) Restart getty. If you have SSH access to your instance, then connect to your instance using SSH, and restart getty using the following command.
[ec2-user ~]$ sudo systemctl restart serial-getty@ttyS0
- Reboot your instance. You can reboot your instance by using SysRq (Linux instances), the EC2 console, or the AWS CLI. For more information, see (Linux instances) Use SysRq to troubleshoot your instance (Linux instances) or Reboot your Amazon EC2 instance.
5. (Linux instances only) At the login prompt, enter the username of the password-based user that you set up previously, and then press Enter.
6. (Linux instances only) At the Password prompt, enter the password, and then press Enter.
### Connect using your own key and SSH client You can use your own SSH key and connect to your instance from the SSH client of your choice while using the serial console API. This enables you to benefit from the serial console capability to push a public key to the instance.
After pushing the SSH key to the instance, the SSH connection is not subject to the IAM policies that you configured to grant users EC2 Serial Console access.

Before you begin Verify that the prerequisites are met.
To connect to an instance's serial console using SSH
1. Push your SSH public key to the instance to start a serial console session Use the send-serial-console-ssh-public-key command to push your SSH public key to the instance. This starts a serial console session.
If a serial console session has already been started for this instance, the command fails because you can only have one session open at a time. It takes 30 seconds to tear down a session after you've disconnected from the serial console in order to allow a new session. aws ec2-instance-connect send-serial-console-ssh-public-key \ --instance-id i-001234a4bf70dec41EXAMPLE \ --serial-port 0 \ --ssh-public-key file://my_key.pub \ --region us-east-1
2. Connect to the serial console using your private key Use the ssh command to connect to the serial console before the public key is removed from the serial console service. You have 60 seconds before it is removed.
Use the private key that corresponds to the public key.
The username format is instance-id.port0, which comprises the instance ID and port 0. In the following example, the username is i-001234a4bf70dec41EXAMPLE.port0.
The endpoint of the serial console service is different for each Region. See the EC2 Serial Console endpoints and fingerprints table for each Region's endpoint. In the following example, the serial console service is in the us-east-1 Region. ssh -i my_key i-001234a4bf70dec41EXAMPLE.port0@serial-console.ec2-instance- connect.us-east-1.aws The following example uses timeout 3600 to set your SSH session to terminate after 1 hour.
Processes started during the session may continue running on your instance after the session terminates.

timeout 3600 ssh -i my_key i-001234a4bf70dec41EXAMPLE.port0@serial-console.ec2- instance-connect.us-east-1.aws
3. (Optional) Verify the fingerprint When you connect for the first time to the serial console, you are prompted to verify the fingerprint. You can compare the serial console fingerprint with the fingerprint that's displayed for verification. If these fingerprints don't match, someone might be attempting a "man-in- the-middle" attack. If they match, you can confidently connect to the serial console.
The following fingerprint is for the serial console service in the us-east-1 Region. For the fingerprints for each Region, see EC2 Serial Console endpoints and fingerprints.
SHA256:dXwn5ma/xadVMeBZGEru5l2gx+yI5LDiJaLUcz0FMmw The fingerprint only appears the first time you connect to the serial console.
4. Press Enter. If a prompt returns, you are connected to the serial console.
If the screen remains black, you can use the following information to help resolve issues with connecting to the serial console:
- Check that you have configured access to the serial console. For more information, see Configure access to the EC2 Serial Console.
- (Linux instances only) Use SysRq to connect to the serial console. SysRq does not require that you connect using SSH. For more information, see (Linux instances) Use SysRq to troubleshoot your instance.
- (Linux instances only) Restart getty. If you have SSH access to your instance, then connect to your instance using SSH, and restart getty using the following command.
[ec2-user ~]$ sudo systemctl restart serial-getty@ttyS0
- Reboot your instance. You can reboot your instance by using SysRq (Linux instances only), the EC2 console, or the AWS CLI. For more information, see (Linux instances) Use SysRq to troubleshoot your instance (Linux instances only) or Reboot your Amazon EC2 instance.
5. (Linux instances only) At the login prompt, enter the username of the password-based user that you set up previously, and then press Enter.
6. (Linux instances only) At the Password prompt, enter the password, and then press Enter.

### EC2 Serial Console endpoints and fingerprints The following are the service endpoints and fingerprints for EC2 Serial Console. To connect programmatically to an instance's serial console, you use an EC2 Serial Console endpoint. The EC2 Serial Console endpoints and fingerprints are unique for each AWS Region.
Region Name Region Endpoint Fingerprint US East (Ohio) us-east-2 serial-console.ec2- instance-connect.us- east-2.aws SHA256:Eh wPkTzRtTY 7TRSzz26XbB0/ HvV9jRM7mCZN0xw/ d/0 US East (N. Virginia) us-east-1 serial-console.ec2- instance-connect.us- east-1.aws SHA256:dXwn5ma/ xadVMeBZGEru 5l2gx+yI5LDiJaLUcz 0FMmw US West (N. Californi a) us-west-1 serial-console.ec2- instance-connect.us- west-1.aws SHA256:OH ldlcMET8u 7QLSX3jmR TRAPFHVtq byoLZBMUCqiH3Y US West (Oregon) us-west-2 serial-console.ec2- instance-connect.us- west-2.aws SHA256:EM CIe23TqKaBI6yGHain qZcMwqNkD hhAVHa1O2JxVUc Africa (Cape Town) af-south-1 ec2-serial-console.af- south-1.api.aws SHA256:RM WWZ2fVePe JUqzjO5jL2KIgXsczo Hlz21Ed00biiWI Asia Pacific (Hong Kong) ap-east-1 ec2-serial-console.ap- east-1.api.aws SHA256:T0 Q1lpiXxChoZHplnAkj

Region Name Region Endpoint Fingerprint bP7tkm2xXViC9bJFsj Ynifk Asia Pacific (Hyderabad) ap-south-2 ec2-serial-console.ap- south-2.api.aws SHA256:WJ gPBSwV4/shN +OPITValoewAuYj1 5DVW845JEhDKRs Asia Pacific (Jakarta) ap-southeast-3 ec2-serial-console.ap- southeast-3.api.aws SHA256:5ZwgrCh+lfn s32XITqL/4O0zIfbx4 bZgsYFqy3o8mIk Asia Pacific (Malaysia) ap-southeast-5 ec2-serial-console.ap- southeast-5.api.aws SHA256:cQ XTHQMRcqR dIjmAGoAM BSExeoRob YyRwT67yTjnEiA Asia Pacific (Melbourne) ap-southeast-4 ec2-serial-console.ap- southeast-4.api.aws SHA256:Av aq27hFgLvjn5gTSShZ 0oV7h90p0 GG46wfOeT6ZJvM Asia Pacific (Mumbai) ap-south-1 serial-console.ec2- instance-connect.ap- south-1.aws SHA256:oB LXcYmklqHHEbliARxE gH8IsO51rezTPiSM35 BsU40 Asia Pacific (Osaka) ap-northeast-3 ec2-serial-console.ap- northeast-3.api.aws SHA256:Am0/ jiBKBnBuFnHr9aXs gEV3G8Tu/ vVHFXE/3UcyjsQ Asia Pacific (Seoul) ap-northeast-2 serial-console.ec2- instance-connect.ap- northeast-2.aws SHA256:FoqWXNX +DZ++GuNTztg9 PK49WYMqBX +FrcZM2dSrqrI

Region Name Region Endpoint Fingerprint Asia Pacific (Singapor e) ap-southeast-1 serial-console.ec2- instance-connect.ap- southeast-1.aws SHA256:PL FNn7WnCQD Hx3qmwLu1Gy/ O8TUX7LQgZuaC6L 45CoY Asia Pacific (Sydney) ap-southeast-2 serial-console.ec2- instance-connect.ap- southeast-2.aws SHA256:yF vMwUK9lEU QjQTRoXXzuN+cW9/ VSe9W984Cf5Tgzo4 Asia Pacific (Thailand) ap-southeast-7 ec2-serial-console.ap- southeast-7.api.aws SHA256:KC AZiRYrR1Q2lqsg7vTw ixWmvc2wm jVT31XRgSdEfDY Asia Pacific (Tokyo) ap-northeast-1 serial-console.ec2- instance-connect.ap- northeast-1.aws SHA256:RQ fsDCZTOfQ awewTRDV1t9Em/ HMrFQe+CRlIOT 5um4k Canada (Central) ca-central-1 serial-console.ec2- instance-connect.ca- central-1.aws SHA256:P2 O2jOZwmpM wkpO6YW73 8FIOTHdUT yEv2gczYMMO7s4 Canada West (Calgary) ca-west-1 ec2-serial-console.ca- west-1.api.aws SHA256:s3rc8lI2xhb hr3iedjJNxGAFLPGOL jx7IxxXrGckk6Q

Region Name Region Endpoint Fingerprint China (Beijing) cn-north-1 ec2-serial-console .cn-north-1.api.am azonwebservices.co m.cn SHA256:2g HVFy4H7uU 3+WaFUxD28v/ ggMeqjvSlgngpgL gGT+Y China (Ningxia) cn-northwest-1 ec2-serial-console .cn-northwest-1.ap i.amazonwebservice s.com.cn SHA256:Td grNZkiQOd VfYEBUhO4 SzUA09VWI 5rYOZGTogpwmiM Europe (Frankfurt) eu-central-1 serial-console.ec2- instance-connect.eu- central-1.aws SHA256:aCMFS/ yIcOdOlkXvOl8A mZ1Toe+bB nrJJ3Fy0k0De2c Europe (Ireland) eu-west-1 serial-console.ec2- instance-connect.eu- west-1.aws SHA256:h2 AaGAWO4Ha thhtm6ezs3Bj7udgUx i2qTrHjZAwCW6E Europe (London) eu-west-2 serial-console.ec2- instance-connect.eu- west-2.aws SHA256:a69rd5CE/ AEG4Amm53I6 lkD1ZPvS/ BCV3tTPW2RnJg8 Europe (Milan) eu-south-1 ec2-serial-console.eu- south-1.api.aws SHA256:lC 0kOVJnpgF yBVrxn0A7 n99ecLbXS X95cuuS7X7QK30

Region Name Region Endpoint Fingerprint Europe (Paris) eu-west-3 serial-console.ec2- instance-connect.eu- west-3.aws SHA256:q8 ldnAf9pym eNe8BnFVngY3RPAr/ kxswJUzfrlxeEWs Europe (Spain) eu-south-2 ec2-serial-console.eu- south-2.api.aws SHA256:Go CW2DFRlu6 69QNxqFxE csR6fZUz/4F4n7T45Z cwoEc Europe (Stockholm) eu-north-1 serial-console.ec2- instance-connect.eu- north-1.aws SHA256:tk GFFUVUDvo cDiGSS3Cu8Gdl6w2uI 32EPNpKFKLwX84 Europe (Zurich) eu-central-2 ec2-serial-console.eu- central-2.api.aws SHA256:8P px2mBMf6W dCw0NUlzKfwM4/ IfRz4OaXFutQX Wp6mk Israel (Tel Aviv) il-central-1 ec2-serial-console.il- central-1.api.aws SHA256:JR 6q8v6kNNP i8+QSFQ4d j5dimNmZP TgwgsM1SNvtYyU Mexico (Central) mx-central-1 ec2-serial-console .mx-central-1.api.aws SHA256:BC uVl13iQNk+CcVnt18E f4p2ZHUrBBAOxlFetB 32GS0

Region Name Region Endpoint Fingerprint Middle East (Bahrain) me-south-1 ec2-serial-console .me-south-1.api.aws SHA256:nP jLLKHu2Qn LdUq2kVAr soK5xvPJO MRJKCBzCDqC3k8 Middle East (UAE) me-central-1 ec2-serial-console .me-central-1.api.aws SHA256:zpb5duKiBZ +l0dFwPeyy kB4MPBYhI/ XzXNeFSDKBvLE South America (São Paulo) sa-east-1 serial-console.ec2- instance-connect.sa- east-1.aws SHA256:rd2+/32Ognj ew1yVIemENaQzC +Botbih62OqAP Dq1dI AWS GovCloud (US- East) us-gov-east-1 serial-console.ec2 -instance-connect. us-gov-east-1.amaz onaws.com SHA256:tI we19GWsoy LClrtvu38YEEh+DHIk qnDcZnmtebvF28 AWS GovCloud (US- West) us-gov-west-1 serial-console.ec2 -instance-connect. us-gov-west-1.amaz onaws.com SHA256:kf OFRWLaOZfB +utbd3bRf8OlPf8nG O2YZLqXZiIw5DQ
## Disconnect from the EC2 Serial Console If you no longer need to be connected to your instance's EC2 Serial Console, you can disconnect from it. When you disconnect from the serial console, any shell session running on the instance will continue to run. If you want to end the shell session, you'll need to end it before disconnecting from the serial console.

Considerations
- The serial console connection typically lasts for 1 hour unless you disconnect from it. However, during system maintenance, Amazon EC2 will disconnect the serial console session.
- It takes 30 seconds to tear down a session after you've disconnected from the serial console in order to allow a new session.
The way to disconnect from the serial console depends on the client.
Browser-based client To disconnect from the serial console, close the serial console in-browser terminal window.
Standard OpenSSH client To disconnect from the serial console, use the following command to close the SSH connection.
This command must be run immediately following a new line.
~.
The command that you use for closing an SSH connection might be different depending on the SSH client that you're using.
## Troubleshoot your Amazon EC2 instance using the EC2 Serial Console By using EC2 Serial Console, you can troubleshoot boot, network configuration, and other issues by connecting to your instance's serial port.
Use the instructions for your instance's operating system and for the tool you've configured on your instance.
Tools
- (Linux instances) Use GRUB to troubleshoot your instance
- (Linux instances) Use SysRq to troubleshoot your instance
- (Windows instances) Use SAC to troubleshoot your instance Prerequisites

Before you begin, make sure you have completed the  prerequisites, including configuring your chosen troubleshooting tool.
### (Linux instances) Use GRUB to troubleshoot your instance GNU GRUB (short for GNU GRand Unified Bootloader, commonly referred to as GRUB) is the default boot loader for most Linux operating systems. From the GRUB menu, you can select which kernel to boot into, or modify menu entries to change how the kernel will boot. This can be useful when troubleshooting a failing instance.
The GRUB menu is displayed during the boot process. The menu is not accessible via normal SSH, but you can access it using the EC2 Serial Console.
You can boot into single user mode or emergency mode. Single user mode will boot the kernel at a lower runlevel. For example, it might mount the filesystem but not activate the network, giving you the opportunity to perform the maintenance necessary to fix the instance. Emergency mode is similar to single user mode except that the kernel runs at the lowest runlevel possible.
To boot into single user mode
1. Connect to the instance's serial console.
2. Reboot the instance using the following command.
[ec2-user ~]$ sudo reboot
3. During reboot, when the GRUB menu appears, press any key to stop the boot process.
4. In the GRUB menu, use the arrow keys to select the kernel to boot into, and press e on your keyboard.
5. Use the arrow keys to locate your cursor on the line containing the kernel. The line begins with either linux or linux16 depending on the AMI that was used to launch the instance. For Ubuntu, two lines begin with linux, which must both be modified in the next step.
6. At the end of the line, add the word single.
The following is an example for Amazon Linux 2. linux /boot/vmlinuz-4.14.193-149.317.amzn2.aarch64 root=UUID=d33f9c9a-\ dadd-4499-938d-ebbf42c3e499 ro  console=tty0 console=ttyS0,115200n8 net.ifname\ s=0 biosdevname=0 nvme_core.io_timeout=4294967295 rd.emergency=poweroff rd.she\ ll=0 single

7. Press Ctrl+X to boot into single user mode.
8. At the login prompt, enter the username of the password-based user that you set up previously, and then press Enter.
9. At the Password prompt, enter the password, and then press Enter.

To boot into emergency mode Follow the same steps as single user mode, but at step 6, add the word emergency instead of single.
### (Linux instances) Use SysRq to troubleshoot your instance The System Request (SysRq) key, which is sometimes referred to as "magic SysRq", can be used to directly send the kernel a command, outside of a shell, and the kernel will respond, regardless of what the kernel is doing. For example, if the instance has stopped responding, you can use the SysRq key to tell the kernel to crash or reboot. For more information, see Magic SysRq key in Wikipedia.
You can use SysRq commands in the EC2 Serial Console browser-based client or in an SSH client.
The command to send a break request is different for each client.
To use SysRq, choose one of the following procedures based on the client that you are using.
Browser-based client To use SysRq in the serial console browser-based client
1. Connect to the instance's serial console.
2. To send a break request, press CTRL+0 (zero). If your keyboard supports it, you can also send a break request using the Pause or Break key.
[ec2-user ~]$ CTRL+0
3. To issue a SysRq command, press the key on your keyboard that corresponds to the required command. For example, to display a list of SysRq commands, press h.
[ec2-user ~]$ h

The h command outputs something similar to the following.
[ 1169.389495] sysrq: HELP : loglevel(0-9) reboot(b) crash(c) terminate-all- tasks(e) memory-full-oom-kill(f) kill-all-tasks(i) thaw-filesystems (j) sak(k) show-backtrace-all-active-cpus(l) show-memory-usage(m) nice-all-RT- tasks(n) poweroff(o) show-registers(p) show-all-timers(q) unraw(r ) sync(s) show-task-states(t) unmount(u) show-blocked-tasks(w) dump-ftrace- buffer(z)
SSH client To use SysRq in an SSH client
1. Connect to the instance's serial console.
2. To send a break request, press ~B (tilde, followed by uppercase B).
[ec2-user ~]$ ~B
3. To issue a SysRq command, press the key on your keyboard that corresponds to the required command. For example, to display a list of SysRq commands, press h.
[ec2-user ~]$ h The h command outputs something similar to the following.
[ 1169.389495] sysrq: HELP : loglevel(0-9) reboot(b) crash(c) terminate-all- tasks(e) memory-full-oom-kill(f) kill-all-tasks(i) thaw-filesystems (j) sak(k) show-backtrace-all-active-cpus(l) show-memory-usage(m) nice-all-RT- tasks(n) poweroff(o) show-registers(p) show-all-timers(q) unraw(r ) sync(s) show-task-states(t) unmount(u) show-blocked-tasks(w) dump-ftrace- buffer(z)
Note The command that you use for sending a break request might be different depending on the SSH client that you're using.

### (Windows instances) Use SAC to troubleshoot your instance The Special Admin Console (SAC) capability of Windows provides a way to troubleshoot a Windows instance. By connecting to the instance's serial console and using SAC, you can interrupt the boot process and boot Windows in safe mode.
Note If you enable SAC on an instance, the EC2 services that rely on password retrieval will not work from the Amazon EC2 console. Windows on Amazon EC2 launch agents (EC2Config, EC2Launch v1, and EC2Launch v2) rely on the serial console to execute various tasks.
These tasks do not perform successfully when you enable SAC on an instance. For more information about Windows on Amazon EC2 launch agents, see the section called "Configure Windows instances". If you enable SAC, you can disable it later. For more information, see Disable SAC and the boot menu.
Tasks
- Use SAC
- Use the boot menu
- Disable SAC and the boot menu
#### Use SAC To use SAC
1. Connect to the serial console.
If SAC is enabled on the instance, the serial console displays the SAC> prompt.

2. To display the SAC commands, enter ?, and then press Enter.
Expected output
3. To create a command prompt channel (such as cmd0001 or cmd0002), enter cmd, and then press Enter.
4. To view the command prompt channel, press ESC, and then press TAB.
Expected output
5. To switch channels, press ESC+TAB+channel number together. For example, to switch to the cmd0002 channel (if it has been created), press ESC+TAB+2.
6. Enter the credentials required by the command prompt channel.

The command prompt is the same full-featured command shell that you get on a desktop, but with the exception that it does not allow the reading of characters that were already output.
PowerShell can also be used from the command prompt.
Note that you might need to set the progress preference to silent mode.
#### Use the boot menu If the instance has the boot menu enabled and is restarted after connecting through SSH, you should see the boot menu, as follows.

Boot menu commands ENTER Starts the selected entry of the operating system.
TAB Switches to the Tools menu.
ESC Cancels and restarts the instance.
ESC followed by 8 Equivalent to pressing F8. Shows advanced options for the selected item.
ESC key + left arrow Goes back to the initial boot menu.
The ESC key alone does not take you back to the main menu because Windows is waiting to see if an escape sequence is in progress.

#### Disable SAC and the boot menu If you enable SAC and the boot menu, you can disable these features later.
Use one of the following methods to disable SAC and the boot menu on an instance.
PowerShell To disable SAC and the boot menu on a Windows instance
1. Connect to your instance and perform the following steps from an elevated PowerShell command line.
2. First disable the boot menu by changing the value to no. bcdedit /set '{bootmgr}' displaybootmenu no
3. Then disable SAC by changing the value to off. bcdedit /ems '{current}' off
4. Apply the updated configuration by rebooting the instance.
