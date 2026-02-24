# Connect to your EC2 instance

Source: apps/user-manuals/aws/ec2-ug.pdf

---

12. When your instance is in the running state, you can connect to it. To do this, select your instance in the list, choose Connect, and choose a connection option. For more information about connecting to your instance, see Connect to your EC2 instance.
Important Check the vendor's usage instructions carefully, as you might need to use a specific username to connect to your instance. For information about accessing your subscription details, see Manage your AWS Marketplace subscriptions.
13. If the instance fails to launch or the state immediately goes to terminated instead of running, see Troubleshoot Amazon EC2 instance launch issues.
To launch an instance from an AWS Marketplace AMI using a command line tool To launch instances from AWS Marketplace products using a command line tool, first ensure that you are subscribed to the product. You can then launch an instance with the product's AMI ID using the following methods:
Method Documentation AWS CLI Use the run-instances command, or see the following topic for more information: Launch your instance in the AWS Command Line Interface User Guide.
AWS Tools for Windows PowerShell Use the New-EC2Instance command, or see the following topic for more information: Launch an Amazon EC2 Instance Using Windows PowerShell Query API Use the RunInstances request.
# Connect to your EC2 instance Your Amazon EC2 instance is a virtual server in the AWS Cloud. To log on to your instance, you must establish a connection to the instance. How you connect to your instance depends on the operating system of the instance and the operating system on the computer that you use to connect to the instance. The following table details the requirements for each connection method.

Connectio n option Instance operating system Inbound traffic rule IAM permissio ns Instance profile role Software on instance Software on connectin g system Key pair SSH client Linux Yes No No No Yes Yes EC2 Instance Connect Linux Yes Yes No Yes ¹ No No PuTTY Linux Yes No No No Yes Yes RDP client Windows Yes No No No Yes Yes ² Fleet Manager Windows No Yes Yes Yes ¹ No Yes Session Manager Linux, Windows No Yes Yes Yes ¹ No No EC2 Instance Connect Endpoint Linux, Windows Yes Yes No No No No ³ ¹ The required software is only pre-installed on certain AMIs. You can manually install the required software as needed on supported operating systems.
² The key pair is only required if you are using the randomly generated password for the local Administrator user account.
³ A key pair is required if you use the SSH connection method.
For more information, see the documentation for the connection option that you intend to use.

Connection options
- Connect to your Linux instance using an SSH client
- Connect to your Linux instance using PuTTY
- Connect to your Windows instance using an RDP client
- Connect to your Windows instance using Fleet Manager
- Connect using Session Manager
- Connect using a public IP and EC2 Instance Connect
- Connect using a private IP and EC2 Instance Connect Endpoint
## General connection prerequisites The following are general prerequisites to connect to an instance. Note that there might be additional prerequisites that are specific to the connection option that you choose.
General prerequisites
- Check that your instance has passed its status checks. It can take a few minutes for an instance to be ready to accept connection requests. For more information, see View status checks.
- Get the required instance details.
- Locate the private key and set permissions.
- (Optional) Get the instance fingerprint.
### Get the required instance details To prepare to connect to your instance, get the following information from the Amazon EC2 console or by using the command line.

- Get the public DNS name of the instance.
You can get the public DNS for your instance from the Amazon EC2 console. Check the Public IPv4 DNS column of the Instances pane. If this column is hidden, choose the settings icon ( ) in the top-right corner of the screen, and select Public IPv4 DNS. You can also find the public DNS in the instance information section of the Instances pane. When you select the instance in the Instances pane of the Amazon EC2 console, information about that instance will appear on the lower half of the page. Under the Details tab, look for Public IPv4 DNS.
If you prefer, you can use the describe-instances (AWS CLI) or Get-EC2Instance (AWS Tools for Windows PowerShell) commands.
If no Public IPv4 DNS is displayed, verify that the Instance state is Running, and that you have not launched the instance in a private subnet. If you launched your instance using the launch instance wizard, you may have edited the Auto-assign public IP field under Network settings and changed the value to Disable. If you disable the Auto-assign public IP option, the instance is not assigned a public IP address when it is launched.
- (IPv6 only instances) Get the IPv6 address of the instance.

If you assigned an IPv6 address to your instance, you can optionally connect to the instance using its IPv6 address instead of a public IPv4 address or public IPv4 DNS hostname. Your local computer must have an IPv6 address and must be configured to use IPv6. You can get the IPv6 address of your instance from the Amazon EC2 console. Check the IPv6 IPs column of the Instances pane. Or, you can find the IPv6 address in the instance information section. When you select the instance in the Instances pane of the Amazon EC2 console, information about that instance will appear on the lower half of the page. Under the Details tab, look for IPv6 address.
If you prefer, you can use the describe-instances (AWS CLI) or Get-EC2Instance (AWS Tools for Windows PowerShell) commands. For more information about IPv6, see IPv6 addresses.
- (Linux instances) Get the username for your instance.
You can connect to your instance using the username for your user account or the default username for the AMI that you used to launch your instance.
- Get the username for your user account.
For more information about how to create a user account, see Manage system users on your Amazon EC2 Linux instance.
- Get the default username for the AMI that you used to launch your instance.
- Amazon Linux – ec2-user
- CentOS – centos or ec2-user
- Debian – admin
- Fedora – fedora or ec2-user
- FreeBSD – ec2-user
- RHEL – ec2-user or root
- SUSE – ec2-user or root
- Ubuntu – ubuntu
- Oracle – ec2-user
- Bitnami – bitnami
- Rocky Linux – rocky
- Other – Check with the AMI provider

### Locate the private key and set permissions You must know the location of your private key file to make the initial connection to a Linux instance using SSH or a Windows instances using RDP. For SSH connections, you must set file permissions so that only you can read the private key.
For information about how key pairs work when using Amazon EC2, see Amazon EC2 key pairs and Amazon EC2 instances.
- Locate the private key.
Get the fully-qualified path to the location on your computer of the .pem file for the key pair that you specified when you launched the instance. For more information, see the section called "Identify the public key specified at launch".
If you can't find your private key file, see I've lost my private key. How can I connect to my instance?
(Linux instances) If you are connecting to your instance using PuTTY and need to convert the .pem file to .ppk, see Convert your private key using PuTTYgen.
- (Linux instances) Set the permissions of your private key so that only you can read it.
- Connect from macOS or Linux If you plan to use an SSH client on a macOS or Linux computer to connect to your Linux instance, use the following command to set the permissions of your private key file so that only you can read it. chmod 400 key-pair-name.pem If you do not set these permissions, then you cannot connect to your instance using this key pair. For more information, see Error: Unprotected private key file.
- Connect from Windows Open File Explorer and right-click on the .pem file. Select Properties > Security tab and choose Advanced. Choose Disable inheritance. Remove access to all users except for the current user.

### (Optional) Get the instance fingerprint To protect yourself from man-in-the-middle attacks, you can verify the authenticity of the instance you're about to connect to by verifying the fingerprint that is displayed. Verifying the fingerprint is useful if you launched your instance from a public AMI provided by a third party.
Task overview First, get the instance fingerprint from the instance. Then, when you connect to the instance and are prompted to verify the fingerprint, compare the fingerprint you obtained in this procedure with the fingerprint that is displayed. If the fingerprints don't match, someone might be attempting a man-in-the-middle attack. If they match, you can confidently connect to your instance.
Prerequisites to get the instance fingerprint
- The instance must not be in the pending state. The fingerprint is available only after the first boot of the instance is complete.
- You must be the instance owner to get the console output.
- There are various ways to get the instance fingerprint. If you want to use the AWS CLI, it must be installed on your local computer. For information about installing the AWS CLI, see Getting started with the AWS CLI in the AWS Command Line Interface User Guide.
To get the instance fingerprint In Step 1, you get the console output, which includes the instance fingerprint. In Step 2, you find the instance fingerprint in the console output.
1. Get the console output using one of the following methods.
Console
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. From the left navigator, choose Instances.
3. Select your instance, and then choose Actions, Monitor and troubleshoot, Get system log.

AWS CLI On your local computer (not on the instance you're connecting to), use the get-console- output command. If the output is large, you can pipe it to a text file, where it might be easier to read. aws ec2 get-console-output \ --instance-id i-1234567890abcdef0 \ --query Output \ --output text > temp.txt PowerShell On your local computer, use the following Get-EC2ConsoleOutput cmdlet.
$encodedOutput = (Get-EC2ConsoleOutput -InstanceId i-1234567890abcdef0).Output [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String($encodedOutput
2. In the console output, find the instance (host) fingerprint, which is located under BEGIN SSH HOST KEY FINGERPRINTS. There might be several instance fingerprints. When you connect to your instance, it will display only one of the fingerprints.
The exact output can vary by operating system, AMI version, and whether AWS created the key pairs. The following is example output. ec2:############################################################# ec2: -----BEGIN SSH HOST KEY FINGERPRINTS----- ec2: 256 SHA256:l4UB/neBad9tvkgJf1QZWxheQmR59WgrgzEimCG6kZY no comment (ECDSA) ec2: 256 SHA256:kpEa+rw/Uq3zxaYZN8KT501iBtJOIdHG52dFi66EEfQ no comment (ED25519) ec2: 2048 SHA256:L8l6pepcA7iqW/jBecQjVZClUrKY+o2cHLI0iHerbVc no comment (RSA) ec2: -----END SSH HOST KEY FINGERPRINTS----- ec2: ############################################################# Note You'll reference this fingerprint when you connect to the instance.

## Connect to your Linux instance using SSH There are multiple ways to connect to your Linux instance using SSH. Some ways depend on the operating system of the local computer that you connect from. Other methods are browser-based, such as EC2 Instance Connect or AWS Systems Manager Session Manager, and can be used from any computer. You can use SSH to connect to your Linux instance and run commands, or use SSH to transfer files between your local computer and your instance.
Before you connect to your Linux instance using SSH, complete the following prerequisites:
- Check that your instance has passed its status checks. It can take a few minutes for an instance to be ready to accept connection requests. For more information, see View status checks.
- Ensure that the security group associated with your instance allows incoming SSH traffic from your IP address. For more information, see Rules to connect to instances from your computer.
- Get the required instance details.
- Locate the private key and set permissions.
- (Optional) Get the instance fingerprint.
Then, choose from one of the following options to connect to your Linux instance using SSH.
- Connect using an SSH client
- Connect using PuTTY
- Transfer files using SCP If you can't connect to your instance and need help troubleshooting, see Troubleshoot issues connecting to your Amazon EC2 Linux instance.
### Connect to your Linux instance using an SSH client You can use Secure Shell (SSH) to connect to your Linux instance from your local computer. For more information about other options, see Connect to your EC2 instance.
Note If you receive an error while attempting to connect to your instance, make sure that your instance meets all of the SSH connection prerequisites. If it meets all of the prerequisites,

and you're still not able to connect to your Linux instance, see Troubleshoot issues connecting to your Amazon EC2 Linux instance.
Contents
- SSH connection prerequisites
- Connect to your Linux instance using an SSH client
#### SSH connection prerequisites Before you can connect to your Linux instance using SSH, complete the following tasks.
Complete the general prerequisites.
- Check that your instance has passed its status checks. It can take a few minutes for an instance to be ready to accept connection requests. For more information, see View status checks.
- Get the required instance details.
- Locate the private key and set permissions.
- (Optional) Get the instance fingerprint.
Allow inbound SSH traffic from your IP address.
Ensure that the security group associated with your instance allows incoming SSH traffic from your IP address. For more information, see Rules to connect to instances from your computer.
Install an SSH client on your local computer (if needed).
Your local computer might have an SSH client installed by default. You can verify this by entering the following command in a terminal window. If your computer doesn't recognize the command, you must install an SSH client. ssh The following are some of the possible options for Windows. If your computer runs a different operating system, see the documentation for that operating system for SSH client options.

#### Install OpenSSH on Windows After you install OpenSSH on Windows, you can connect to your Linux instance from your Windows computer using SSH. Before you begin, ensure that you meet the following requirements.
Windows version The version of Windows on your computer must be Windows Server 2019 or later.
For earlier versions of Windows, download and install Win32-OpenSSH instead.
PowerShell requirements To install OpenSSH on your Windows OS using PowerShell, you must be running PowerShell version 5.1 or later, and your account must be a member of the built-in Administrators group.
Run $PSVersionTable.PSVersion from PowerShell to check your PowerShell version.
To check whether you are a member of the built-in Administrators group, run the following PowerShell command:
(New-Object Security.Principal.WindowsPrincipal([Security.Principal.WindowsIdentity]::GetCurrent())).Is If you are a member of the built-in Administrators group, the output is True.
To install OpenSSH for Windows using PowerShell, run the following PowerShell command.
Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0 The following is example output.
Path          :
Online        : True RestartNeeded : False To uninstall OpenSSH from Windows using PowerShell, run the following PowerShell command.
Remove-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0 The following is example output.

Path          :
Online        : True RestartNeeded : True
#### Install Windows Subsystem for Linux (WSL)
After you install WSL on Windows, you can connect to your Linux instance from your Windows computer using Linux command line tools, such as an SSH client.
Follow the instructions in Install Windows Subsystem for Linux on your EC2 Windows instance. If you follow the instructions in Microsoft's installation guide, they install the Ubuntu distribution of Linux. You can install a different Linux distribution if you prefer.
In a WSL terminal window, copy the .pem file (for the key pair that you specified for your instance at launch) from Windows to WSL. Note the fully-qualified path to the .pem file on WSL to use when connecting to your instance. For information about how to specify the path to your Windows hard drive, see How do I access my C drive?. cp /mnt/<Windows drive letter>/path/my-key-pair.pem ~/WSL-path/my-key-pair.pem For information about uninstalling Windows Subsystem for Linux, see How do I uninstall a WSL Distribution?.
#### Connect to your Linux instance using an SSH client Use the following procedure to connect to your Linux instance using an SSH client.
To connect to your instance using an SSH client
1. Open a terminal window on your computer.
2. Use the ssh command to connect to the instance. You need the details about your instance that you gathered as part of the prerequisites. For example, you need the location of the private key (.pem file), the username, and the public DNS name or IPv6 address. The following are example commands.
- (Public DNS) To use the public DNS name, enter the following command. ssh -i /path/key-pair-name.pem instance-user-name@instance-public-dns-name
- (IPv6) Alternatively, if your instance has an IPv6 address, enter the following command to use the IPv6 address.

ssh -i /path/key-pair-name.pem instance-user-name@2001:db8::1234:5678:1.2.3.4 The following is an example response.
The authenticity of host 'ec2-198-51-100-1.compute-1.amazonaws.com (198-51-100-1)' can't be established.
ECDSA key fingerprint is l4UB/neBad9tvkgJf1QZWxheQmR59WgrgzEimCG6kZY.
Are you sure you want to continue connecting (yes/no)?
3. (Optional) Verify that the fingerprint in the security alert matches the fingerprint. If these fingerprints don't match, someone might be attempting a man-in-the-middle attack. If they match, continue to the next step. For more information, see Get the instance fingerprint.
4. Enter yes.
You see a response like the following:
Warning: Permanently added 'ec2-198-51-100-1.compute-1.amazonaws.com' (ECDSA) to the list of known hosts.
### Connect to your Linux instance using PuTTY You can connect to your Linux instance using PuTTY, a free SSH client for Windows.
If you're running Windows Server 2019 or later, we recommend that you use OpenSSH, an open source connectivity tool for remote login using the SSH protocol.
Note If you receive an error while attempting to connect to your instance, make sure that your instance meets all of the SSH connection prerequisites. If it meets all of the prerequisites, and you're still not able to connect to your Linux instance, see Troubleshoot issues connecting to your Amazon EC2 Linux instance.
Contents
- Prerequisites
- (Optional) Convert your private key using PuTTYgen

- Connect to your Linux instance
#### Prerequisites Before you connect to your Linux instance using PuTTY, complete the following tasks.
Complete the general prerequisites.
- Check that your instance has passed its status checks. It can take a few minutes for an instance to be ready to accept connection requests. For more information, see View status checks.
- Get the required instance details.
- Locate the private key and set permissions.
- (Optional) Get the instance fingerprint.
Allow inbound SSH traffic from your IP address.
Ensure that the security group associated with your instance allows incoming SSH traffic from your IP address. For more information, see Rules to connect to instances from your computer.
Install PuTTY on your local computer (if needed).
Download and install PuTTY from the PuTTY download page. If you already have an earlier version of PuTTY installed, we recommend that you download the latest version. Be sure to install the entire suite.
Convert your private key to PPK format using PuTTYgen.
You must specify the private key for the key pair that you specified when you launched the instance. If you created the private key in .pem format, you must convert it to a PPK file for use with PuTTY. Locate the private key (.pem file), and then follow the steps in Convert your private key using PuTTYgen.
#### (Optional) Convert your private key using PuTTYgen PuTTY does not natively support the PEM format for SSH keys. PuTTY provides a tool named PuTTYgen, which converts PEM keys to the required PPK format for PuTTY. If you created the key using PEM format instead of PPK format, you must convert your private key (.pem file) into this format (.ppk file) for use with PuTTY.

To convert your private key from PEM to PPK format
1. From the Start menu, choose All Programs, PuTTY, PuTTYgen.
2. Under Type of key to generate, choose RSA. If your version of PuTTYgen does not include this option, choose SSH-2 RSA.
3. Choose Load. By default, PuTTYgen displays only files with the extension .ppk. To locate your .pem file, choose the option to display files of all types.
4. Select your .pem file for the key pair that you specified when you launched your instance and choose Open. PuTTYgen displays a notice that the .pem file was successfully imported. Choose OK.
5. To save the key in the format that PuTTY can use, choose Save private key. PuTTYgen displays a warning about saving the key without a passphrase. Choose Yes.
Note A passphrase on a private key is an extra layer of protection. Even if your private key is discovered, it can't be used without the passphrase. The downside to using a passphrase is that it makes automation harder because human intervention is needed to log on to an instance, or to copy files to an instance.
6. Specify the same name for the key that you used for the key pair (for example, key-pair- name) and choose Save. PuTTY automatically adds the .ppk file extension.
Your private key is now in the correct format for use with PuTTY. You can now connect to your instance using PuTTY's SSH client.

#### Connect to your Linux instance Use the following procedure to connect to your Linux instance using PuTTY. You need the .ppk file that you created for your private key. For more information, see (Optional) Convert your private key using PuTTYgen in the preceding section. If you receive an error while attempting to connect to your instance, see Troubleshoot issues connecting to your Amazon EC2 Linux instance.
Last tested version – PuTTY .78 To connect to your instance using PuTTY
1. Start PuTTY (from the Start menu, search for PuTTY and then choose Open).
2. In the Category pane, choose Session and complete the following fields: a.
In the Host Name box, do one of the following:
- (Public DNS) To connect using your instance's public DNS name, enter instance- user-name@instance-public-dns-name.
- (IPv6) Alternatively, if your instance has an IPv6 address, to connect using your instance's IPv6 address, enter instance-user- name@2001:db8::1234:5678:1.2.3.4.
For information about how to get the username for your instance, and the public DNS name or IPv6 address of your instance, see Get the required instance details. b.
Ensure that the Port value is 22. c.
Under Connection type, select SSH.

3. (Optional) You can configure PuTTY to automatically send 'keepalive' data at regular intervals to keep the session active. This is useful to avoid disconnecting from your instance due to session inactivity. In the Category pane, choose Connection, and then enter the required interval in Seconds between keepalives. For example, if your session disconnects after 10 minutes of inactivity, enter 180 to configure PuTTY to send keepalive data every 3 minutes.
4. In the Category pane, expand Connection, SSH, and Auth. Choose Credentials.
5. Next to Private key file for authentication, choose Browse. In the Select private key file dialog box, select the .ppk file that you generated for your key pair. You can either double- click the file or choose Open in the Select private key file dialog box.
6. (Optional) If you plan to connect to this instance again after this session, you can save the session information for future use. In the Category pane, choose Session. Enter a name for the session in Saved Sessions, and then choose Save.
7. To connect to the instance, choose Open.
8. If this is the first time you have connected to this instance, PuTTY displays a security alert dialog box that asks whether you trust the host to which you are connecting.

a.
(Optional) Verify that the fingerprint in the security alert dialog box matches the fingerprint that you previously obtained in (Optional) Get the instance fingerprint. If these fingerprints don't match, someone might be attempting a "man-in-the-middle" attack. If they match, continue to the next step. b.
Choose Accept. A window opens and you are connected to your instance.
Note If you specified a passphrase when you converted your private key to the PuTTY format, you must provide that passphrase when you log in to the instance.
If you receive an error while attempting to connect to your instance, see Troubleshoot issues connecting to your Amazon EC2 Linux instance.
### Transfer files to a Linux instance using SCP One way to transfer files between your local computer and a Linux instance is to use the secure copy protocol (SCP). SCP is a good option for simple operations, such as as one-time file copies.
SCP secures files transfers using the same .pem file that you use to connect to an instance using SSH. If you need to keep files synchronized, or if the files are large, rsync is faster and more efficient than SCP. For security, use rsync over SSH, as rsync transfers data using plain text by default.
Before you connect to your Linux instance using SCP, complete the following tasks:
- Complete the general prerequisites.
- Check that your instance has passed its status checks. It can take a few minutes for an instance to be ready to accept connection requests. For more information, see View status checks.
- Get the required instance details.
- Locate the private key and set permissions.
- (Optional) Get the instance fingerprint.
- Allow inbound SSH traffic from your IP address.
Ensure that the security group associated with your instance allows incoming SSH traffic from your IP address. For more information, see Rules to connect to instances from your computer.
- Install an SCP client.

Most Linux, Unix, and Apple computers include an SCP client by default. If yours doesn't, the OpenSSH project provides a free implementation of the full suite of SSH tools, including an SCP client. For more information, see https://www.openssh.com.
The following procedure steps you through using SCP to transfer a file using the instance's public DNS name, or the IPv6 address if your instance has one.
To use SCP to transfer files between your computer and your instance
1. Determine the location of the source file on your computer and the destination path on the instance. In the following examples, the name of the private key file is key-pair-name.pem, the file to transfer is my-file.txt, the username for the instance is ec2-user, the public DNS name of the instance is instance-public-dns-name, and the IPv6 address of the instance is 2001:db8::1234:5678:1.2.3.4.
- (Public DNS) To transfer a file to the destination on the instance, enter the following command from your computer. scp -i /path/key-pair-name.pem /path/my-file.txt ec2-user@instance-public-dns- name:path/
- (IPv6) To transfer a file to the destination on the instance if the instance has an IPv6 address, enter the following command from your computer. The IPv6 address must be enclosed in square brackets ([ ]), which must be escaped (\). scp -i /path/key-pair-name.pem /path/my-file.txt ec2-user@ \[2001:db8::1234:5678:1.2.3.4\]:path/
2. If you haven't already connected to the instance using SSH, you see a response like the following:
The authenticity of host 'ec2-198-51-100-1.compute-1.amazonaws.com (10.254.142.33)' can't be established.
RSA key fingerprint is 1f:51:ae:28:bf:89:e9:d8:1f:25:5d:37:2d:7d:b8:ca:9f:f5:f1:6f.
Are you sure you want to continue connecting (yes/no)?
(Optional) You can optionally verify that the fingerprint in the security alert matches the instance fingerprint. For more information, see (Optional) Get the instance fingerprint.

Enter yes.
3. If the transfer is successful, the response is similar to the following:
Warning: Permanently added 'ec2-198-51-100-1.compute-1.amazonaws.com' (RSA) to the list of known hosts. my-file.txt                                100%   480     24.4KB/s   00:00
4. To transfer a file in the other direction (from your Amazon EC2 instance to your computer), reverse the order of the host parameters. For example, you can transfer my-file.txt from your EC2 instance to the a destination on your local computer as my-file2.txt, as shown in the following examples.
- (Public DNS) To transfer a file to a destination on your computer, enter the following command from your computer. scp -i /path/key-pair-name.pem ec2-user@instance-public-dns-name:path/my- file.txt path/my-file2.txt
- (IPv6) To transfer a file to a destination on your computer if the instance has an IPv6 address, enter the following command from your computer. The IPv6 address must be enclosed in square brackets ([ ]), which must be escaped (\). scp -i /path/key-pair-name.pem ec2-user@\[2001:db8::1234:5678:1.2.3.4\]:path/ my-file.txt path/my-file2.txt
### Manage system users on your Amazon EC2 Linux instance Each Linux instance launches with a default Linux system user. You can add users to your instance and delete users.
For the default user, the default username is determined by the AMI that was specified when you launched the instance.
Note By default, password authentication and root login are disabled, and sudo is enabled. To log in to your instance, you must use a key pair. For more information about logging in, see
## Connect to your Linux instance using a public IP address and EC2 Instance Connect

You can allow password authentication and root login for your instance. For more information, see the documentation for your operating system.
Note Linux system users should not be confused with IAM users. For more information, see IAM users in the IAM User Guide.
Contents
- Default usernames
- Considerations
- Create a user
- Remove a user
#### Default usernames The default username for your EC2 instance is determined by the AMI that was specified when you launched the instance.
The default usernames are:
- For an Amazon Linux AMI, the username is ec2-user.
- For a CentOS AMI, the username is centos or ec2-user.
- For a Debian AMI, the username is admin.
- For a Fedora AMI, the username is fedora or ec2-user.
- For a FreeBSD AMI, the username is ec2-user.
- For a RHEL AMI, the username is ec2-user or root.
- For a SUSE AMI, the username is ec2-user or root.
- For an Ubuntu AMI, the username is ubuntu.
- For an Oracle AMI, the username is ec2-user.
- For a Bitnami AMI, the username is bitnami.

Note To find the default username for other Linux distributions, check with the AMI provider.
#### Considerations Using the default user is adequate for many applications. However, you may choose to add users so that individuals can have their own files and workspaces. Furthermore, creating users for new users is much more secure than granting multiple (possibly inexperienced) users access to the default user, because the default user can cause a lot of damage to a system when used improperly. For more information, see Tips for Securing Your EC2 Instance.
To enable users SSH access to your EC2 instance using a Linux system user, you must share the SSH key with the user. Alternatively, you can use EC2 Instance Connect to provide access to users without the need to share and manage SSH keys. For more information, see Connect to your Linux instance using a public IP address and EC2 Instance Connect.
#### Create a user First create the user, and then add the SSH public key that allows the user to connect to and log into the instance.
Important In Step 1 of this procedure, you create a new key pair. Because a key pair functions like a password, it's crucial to handle it securely. If you create a key pair for a user, you must ensure that the private key is sent to them securely. Alternatively, the user can complete Steps 1 and 2 by creating their own key pair, keeping the private key secure on their machine, and then sending you the public key to complete the procedure from Step 3.
To create a user
1. Create a new key pair. You must provide the .pem file to the user for whom you are creating the user. They must use this file to connect to the instance.
2. Retrieve the public key from the key pair that you created in the previous step.
$ ssh-keygen -y -f /path_to_key_pair/key-pair-name.pem

The command returns the public key, as shown in the following example. ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQClKsfkNkuSevGj3eYhCe53pcjqP3maAhDFcvBS7O6Vhz2ItxCih +PnDSUaw+WNQn/mZphTk/a/gU8jEzoOWbkM4yxyb/wB96xbiFveSFJuOp/ d6RJhJOI0iBXrlsLnBItntckiJ7FbtxJMXLvvwJryDUilBMTjYtwB+QhYXUMOzce5Pjz5/ i8SeJtjnV3iAoG/cQk+0FzZqaeJAAHco +CY/5WrUBkrHmFJr6HcXkvJdWPkYQS3xqC0+FmUZofz221CBt5IMucxXPkX4rWi +z7wB3RbBQoQzd8v7yeb7OzlPnWOyN0qFU0XA246RA8QFYiCNYwI3f05p6KLxEXAMPLE
3. Connect to the instance.
4. Use the adduser command to create the user and add it to the system (with an entry in the /etc/passwd file). The command also creates a group and a home directory for the user. In this example, the user is named newuser.
- AL2023 and Amazon Linux 2 With AL2023 and Amazon Linux 2, the user is created with password authentication disabled by default.
[ec2-user ~]$ sudo adduser newuser
- Ubuntu Include the --disabled-password parameter to create the user with password authentication disabled.
[ubuntu ~]$ sudo adduser newuser --disabled-password
5. Switch to the new user so that the directory and file that you create will have the proper ownership.
[ec2-user ~]$ sudo su - newuser The prompt changes from ec2-user to newuser to indicate that you have switched the shell session to the new user.
6. Add the SSH public key to the user. First create a directory in the user's home directory for the SSH key file, then create the key file, and finally paste the public key into the key file, as described in the following sub-steps.

a.
Create a .ssh directory in the newuser home directory and change its file permissions to 700 (only the owner can read, write, or open the directory).
[newuser ~]$ mkdir .ssh [newuser ~]$ chmod 700 .ssh Important Without these exact file permissions, the user will not be able to log in. b.
Create a file named authorized_keys in the .ssh directory and change its file permissions to 600 (only the owner can read or write to the file).
[newuser ~]$ touch .ssh/authorized_keys [newuser ~]$ chmod 600 .ssh/authorized_keys Important Without these exact file permissions, the user will not be able to log in. c.
Open the authorized_keys file using your favorite text editor (such as vim or nano).
[newuser ~]$ nano .ssh/authorized_keys Paste the public key that you retrieved in Step 2 into the file and save the changes.
Important Ensure that you paste the public key in one continuous line. The public key must not be split over multiple lines.
The user should now be able to log into the newuser user on your instance, using the private key that corresponds to the public key that you added to the authorized_keys

file. For more information about the different methods of connecting to a Linux instance, see Connect to your Linux instance using SSH.
#### Remove a user If a user is no longer needed, you can remove that user so that it can no longer be used.
Use the userdel command to remove the user from the system. When you specify the -r parameter, the user's home directory and mail spool are deleted. To keep the user's home directory and mail spool, omit the -r parameter.
[ec2-user ~]$ sudo userdel -r olduser
## Connect to your Windows instance using RDP You can connect to Amazon EC2 instances created from most Windows Amazon Machine Images (AMIs) using Remote Desktop. Remote Desktop uses the Remote Desktop Protocol (RDP) to connect to and use your instance in the same way you use a computer sitting in front of you (local computer). It is available on most editions of Windows and is also available for Mac OS.
The license for the Windows Server operating system allows two simultaneous remote connections for administrative purposes. The license for Windows Server is included in the price of your Windows instance. If you require more than two simultaneous remote connections, you must purchase a Remote Desktop Services (RDS) license. If you attempt a third connection, an error occurs.
Tip If you need to connect to your instance in order to troubleshoot boot, network configuration, and other issues for instances built on the AWS Nitro System, you can use the EC2 Serial Console for instances.
Contents
- Connect to your Windows instance using an RDP client
- Connect to your Windows instance using Fleet Manager
- Transfer files to a Windows instance using RDP

### Connect to your Windows instance using an RDP client You can connect to your Windows instance using an RDP client as follows.
Tip Alternatively, you can connect to your Windows instance using Systems Manager Fleet Manager or EC2 Instance Connect Endpoint.
#### Prerequisites You must meet the following prerequisites to connect to your Windows instance using an RDP client.
- Complete the general prerequisites.
- Check that your instance has passed its status checks. It can take a few minutes for an instance to be ready to accept connection requests. For more information, see View status checks.
- Get the required instance details.
- Locate the private key and set permissions.
- (Optional) Get the instance fingerprint.
- Install an RDP client.
- (Windows) Windows includes an RDP client by default. To verify, type mstsc at a Command Prompt window. If your computer doesn't recognize this command, download the Microsoft Remote Desktop app from the Microsoft Store.
- (macOS X) Download the Windows App for Mac (previously named Microsoft Remote Desktop from the Mac App Store.
- (Linux) Use Remmina.
- Allow inbound RDP traffic from your IP address.
Ensure that the security group associated with your instance allows incoming RDP traffic from your IP address. For more information, see Rules to connect to instances from your computer.
#### Retrieve the administrator password If you joined your instance to a domain, you can connect to your instance using the domain credentials from Directory Service. On the Remote Desktop login screen, instead of using the

local computer name and the generated password, use the fully-qualified username for the administrator (for example, corp.example.com\Admin), and the password for this account.
To connect to a Windows instance using RDP, you must retrieve the initial administrator password and then enter this password when you connect to your instance. It takes a few minutes after instance launch before this password is available. Your account must have permission to call the GetPasswordData action. For more information, see Example policies to control access the Amazon EC2 API.
The default username for the Administrator account depends on the language of the operating system (OS) contained in the AMI. To determine the correct username, identify the language of the OS, and then choose the corresponding username. For example, for an English OS, the username is Administrator, for a French OS it's Administrateur, and for a Portuguese OS it's Administrador. If a language version of the OS does not have a username in the same language, choose the username Administrator (Other). For more information, see Localized Names for Administrator Account in Windows in the Microsoft website.
To retrieve the initial administrator password
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Instances.
3. Select the instance and then choose Connect.
4. On the Connect to instance page, choose the RDP client tab.
5. For Username, choose the default username for the Administrator account. The username you choose must match the language of the operating system (OS) contained in the AMI that you used to launch your instance. If there is no username in the same language as your OS, choose Administrator (Other).
6. Choose Get password.
7. On the Get Windows password page, do the following: a.
Choose Upload private key file and navigate to the private key (.pem) file that you specified when you launched the instance. Select the file and choose Open to copy the entire contents of the file to this window. b.
Choose Decrypt password. The Get Windows password page closes, and the default administrator password for the instance appears under Password, replacing the Get password link shown previously.

c.
Copy the password and save it in a safe place. This password is required to connect to the instance.
#### Connect to your Windows instance The following procedure uses the Remote Desktop Connection client for Windows (MSTSC). If you're using a different RDP client, download the RDP file and then see the documentation for the RDP client for the steps to establish the RDP connection.
To connect to a Windows instance using an RDP client
1. On the Connect to instance page, choose Download remote desktop file. When the file download is finished, choose Cancel to return to the Instances page. The RDP file is downloaded to your Downloads folder.
2. Run mstsc.exe to open the RDP client.
3. Expand Show options, choose Open, and select the .rdp file from your Downloads folder.
4. By default, Computer is the public IPv4 DNS name of the instance and User name is the administrator account. To connect to the instance using IPv6 instead, replace the public IPv4 DNS name of the instance with its IPv6 address. Review the default settings and change them as needed.
5. Choose Connect. If you receive a warning that the publisher of the remote connection is unknown, choose Connect to continue.
6. Enter the password that you saved previously, and then choose OK.
7. Due to the nature of self-signed certificates, you might get a warning that the security certificate could not be authenticated. Do one of the following:
- If you trust the certificate, choose Yes to connect to your instance.
- [Windows] Before you proceed, compare the thumbprint of the certificate with the value in the system log to confirm the identity of the remote computer. Choose View certificate and then choose Thumbprint from the Details tab. Compare this value to the value of RDPCERTIFICATE-THUMBPRINT in Actions, Monitor and troubleshoot, Get system log.
- [Mac OS X] Before you proceed, compare the fingerprint of the certificate with the value in the system log to confirm the identity of the remote computer. Choose Show Certificate, expand Details, and choose SHA1 Fingerprints. Compare this value to the value of RDPCERTIFICATE-THUMBPRINT in Actions, Monitor and troubleshoot, Get system log.

8. If the RDP connection is successful, the RDP client displays the Windows login screen and then the Windows desktop. If you receive an error message instead, see the section called "Remote Desktop can't connect to the remote computer". When you are finished with the RDP connection, you can close the RDP client.
#### Configure user accounts After you connect to your instance over RDP, we recommend that you perform the following tasks:
- Change the administrator password from the default value. You can change the password while you are logged on to the instance itself, just as you would on any computer running Windows Server.
- Create another user with administrator privileges on the instance. This is a safeguard in case you forget the administrator password or have a problem with the administrator account. The new user must have permission to access the instance remotely. Open System Properties by right- clicking on the This PC icon on your Windows desktop or File Explorer and selecting Properties.
Choose Remote settings, and choose Select Users to add the user to the Remote Desktop Users group.

### Connect to your Windows instance using Fleet Manager You can use Fleet Manager, a capability of AWS Systems Manager, to connect to Windows instances using the Remote Desktop Protocol (RDP) and display up to four Windows instances on the same page in the AWS Management Console. You can connect to the first instance in the Fleet Manager Remote Desktop directly from the Instances page in the Amazon EC2 console. For more information about Fleet Manager, see Connect to a managed instance using Remote Desktop in the AWS Systems Manager User Guide.
You do not need to specifically allow incoming RDP traffic from your IP address if you use Fleet Manager to connect. Fleet Manager handles that for you.
Prerequisites Before attempting to connect to an instance using Fleet Manager, you must set up your environment. For more information, see Setting up your environment in the AWS Systems Manager User Guide.

To connect to a Windows instance using Fleet Manager
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. From the navigation pane, choose Instances.
3. Select the instance and then choose Connect.
4. On the RDP client tab, for Connection Type, choose Connect using Fleet Manager.
5. Choose Fleet Manager Remote Desktop. This opens the Fleet Manager Remote Desktop page in the AWS Systems Manager console.
6. Enter your credentials and then choose Connect.
7. If the RDP connection is successful, Fleet Manager displays the Windows desktop. When you are finished with the session, choose Actions, End session.
For more information, see Connecting to a Windows Server managed instance using Remote Desktop in the AWS Systems Manager User Guide.
### Transfer files to a Windows instance using RDP You can work with your Windows instance in the same way that you would work with any Windows server. For example, you can transfer files between a Windows instance and your local computer using the local file sharing feature of the Microsoft Remote Desktop Connection (RDP) software.
You can access local files on hard disk drives, DVD drives, portable media drives, and mapped network drives.
To access your local files from your Windows instances, you must enable the local file sharing feature by mapping the remote session drive to your local drive. The steps are slightly different depending on whether your local computer operating system is Windows or macOS X.
For more information about the prerequisites to connect using RDP, see Prerequisites.
Windows To map the remote session drive to your local drive on your local Windows computer
1. Open the Remote Desktop Connection client.
2. Choose Show Options.
3. Add the instance host name to the Computer field and username to the User name field, as follows:

a.
Under Connection settings, choose Open..., and browse to the RDP shortcut file that you downloaded from the Amazon EC2 console. The file contains the Public IPv4 DNS host name, which identifies the instance, and the Administrator user name. b.
Select the file and choose Open. The Computer and User name fields are populated with the values from the RDP shortcut file. c.
Choose Save.
4. Choose the Local Resources tab.
5. Under Local devices and resources, choose More...
6. Open Drives and select the local drive to map to your Windows instance.
7. Choose OK.

8. Choose Connect to connect to your Windows instance. macOS X To map the remote session drive to your local folder on your local macOS X computer
1. Open the Remote Desktop Connection client.
2. Browse to the RDP file that you downloaded from the Amazon EC2 console (when you initially connected to the instance), and drag it onto the Remote Desktop Connection client.
3. Right-click the RDP file, and choose Edit.
4. Choose the Folders tab, and select the Redirect folders checkbox.

5. Choose the + icon at bottom left, browse to the folder to map, and choose Open. Repeat this step for every folder to map.
6. Choose Save.
7. Choose Connect to connect to your Windows instance. You'll be prompted for the password.
8. On the instance, in File Explorer, expand This PC, and find the shared folder from which you can access your local files. In the following screenshot, the Desktop folder on the local computer was mapped to the remote session drive on the instance.

For more information on making local devices available to a remote session on a Mac computer, see Get started with the macOS client.
## Connect to your Amazon EC2 instance using Session Manager Session Manager is a fully-managed AWS Systems Manager capability for managing your Amazon EC2 instances through an interactive, one-click, browser-based shell, or through the AWS CLI. You can use Session Manager to start a session with an instance in your account. After the session is started, you can run interactive commands on the instance as you would for any other connection type. For more information about Session Manager, see AWS Systems Manager Session Manager in the AWS Systems Manager User Guide.
Prerequisites Before you attempt to connect to an instance using Session Manager, you must complete the required setup steps. For example, the instance must be managed by SSM and must have an attached IAM role with the AmazonSSMManagedInstanceCore policy. For more information, see Setting up Session Manager.

To connect to an Amazon EC2 instance using Session Manager on the Amazon EC2 console
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Instances.
3. Select the instance and choose Connect.
4. For the connection method, choose Session Manager.
5. Choose Connect to start the session.
Troubleshooting If you receive an error that you're not authorized to perform one or more Systems Manager actions (ssm:command-name), you must update your policies to allow you to start sessions from the Amazon EC2 console. For more information and instructions, see Quickstart default IAM policies for Session Manager in the AWS Systems Manager User Guide.
Connect to your Linux instance using a public IP address and EC2 Instance Connect Amazon EC2 Instance Connect provides a secure way to connect to your Linux instances over Secure Shell (SSH). With EC2 Instance Connect, you use AWS Identity and Access Management (IAM) policies and principals to control SSH access to your instances, removing the need to share and manage SSH keys. All connection requests using EC2 Instance Connect are logged to AWS CloudTrail so that you can audit connection requests.

You can use EC2 Instance Connect to connect to your instances using the Amazon EC2 console or the SSH client of your choice.
When you connect to an instance using EC2 Instance Connect, the EC2 Instance Connect API pushes an SSH public key to the instance metadata where it remains for 60 seconds. An IAM policy attached to your user authorizes your user to push the public key to the instance metadata. The SSH daemon uses AuthorizedKeysCommand and AuthorizedKeysCommandUser, which are configured when EC2 Instance Connect is installed, to look up the public key from the instance metadata for authentication, and connects you to the instance.
Tip EC2 Instance Connect is one of the options to connect to your Linux instance. For other options, see Connect to your Linux instance using SSH. To connect to a Windows instance, see Connect to your Windows instance using RDP.
Pricing EC2 Instance Connect is available at no additional cost.
Region availability EC2 Instance Connect is available in all AWS Regions, except Asia Pacific (Taipei). It is not supported in Local Zones.
Contents
- Tutorial: Complete the configuration required to connect to your instance using EC2 Instance Connect
- Prerequisites for EC2 Instance Connect
- Grant IAM permissions for EC2 Instance Connect
- Install EC2 Instance Connect on your EC2 instances
- Connect to a Linux instance using EC2 Instance Connect
- Uninstall EC2 Instance Connect For a blog post that discusses how to improve the security of your bastion hosts using EC2 Instance Connect, see Securing your bastion hosts with Amazon EC2 Instance Connect.

### Tutorial: Complete the configuration required to connect to your instance using EC2 Instance Connect EC2 Instance Connect To connect to your instance using EC2 Instance Connect in the Amazon EC2 console, you first need to complete the prerequisite configuration that will allow you to successfully connect to your instance. The purpose of this tutorial is to guide you through the tasks to complete the prerequisite configuration.
Tutorial overview In this tutorial, you'll complete the following four tasks:
- Task 1: Grant permissions required to use EC2 Instance Connect First you'll create an IAM policy that contains the IAM permissions that allow you to push a public key to the instance metadata. You'll attach this policy to your IAM identity (user, user group, or role) so that your IAM identity gets these permissions.
- Task 2: Allow inbound traffic from the EC2 Instance Connect service to your instance Then you'll create a security group that allows traffic from the EC2 Instance Connect service to your instance. This is required when you use EC2 Instance Connect in the Amazon EC2 console to connect to your instance.
- Task 3: Launch your instance You'll then launch an EC2 instance using an AMI that is pre-installed with EC2 Instance Connect and you'll add the security group that you created in the previous step.
- Task 4: Connect to your instance Finally, you'll use EC2 Instance Connect in the Amazon EC2 console to connect to your instance. If you can connect, then you can be sure that the prerequisite configuration you completed in Tasks 1, 2, and 3 were successful.
#### Task 1: Grant permissions required to use EC2 Instance Connect When you connect to an instance using EC2 Instance Connect, the EC2 Instance Connect API pushes an SSH public key to the instance metadata where it remains for 60 seconds. You need an IAM policy attached to your IAM identity (user, user group, or role) to grant you the required permission to push the public key to the instance metadata.

Task objective You'll create the IAM policy that grants the permission to push the public key to the instance. The specific action to allow is ec2-instance-connect:SendSSHPublicKey. You must also allow the ec2:DescribeInstances action so that you can view and select your instance in the Amazon EC2 console.
After you've created the policy, you'll attach the policy to your IAM identity (user, user group, or role) so that your IAM identity gets the permissions.
You'll create a policy that is configured as follows:
JSON { "Version":"2012-10-17", "Statement": [{ "Effect": "Allow", "Action": "ec2-instance-connect:SendSSHPublicKey", "Resource": "*"
        }, { "Effect": "Allow", "Action": "ec2:DescribeInstances", "Resource": "*"
        } ]
} Important The IAM policy created in this tutorial is a highly permissive policy; it allows you to connect to any instance using any AMI username. We're using this highly permissive policy to keep the tutorial simple and focused on the specific configurations that this tutorial is teaching.
However, in a production environment, we recommend that your IAM policy is configured to provide least-privilege permissions. For example IAM policies, see Grant IAM permissions for EC2 Instance Connect.

To create and attach an IAM policy that allows you to use EC2 Instance Connect to connect to your instances
1. First create the IAM policy a.
Open the IAM console at https://console.aws.amazon.com/iam/. b.
In the navigation pane, choose Policies. c.
Choose Create policy. d.
On the Specify permission page, do the following: i.
For Service, choose EC2 Instance Connect. ii.
Under Actions allowed, in the search field start typing send to show the relevant actions, and then select SendSSHPublicKey. iii.
Under Resources, choose All. For a production environment, we recommend specifying the instance by its ARN, but for this tutorial, you're allowing all instances. iv.
Choose Add more permissions. v.
For Service, choose EC2. vi.
Under Actions allowed, in the search field start typing describein to show the relevant actions, and then select DescribeInstances. vii. Choose Next. e.
On the Review and create page, do the following: i.
For Policy name, enter a name for the policy. ii.
Choose Create policy.
2. Then attach the policy to your identity a.
In the IAM console, in the navigation pane, choose Policies. b.
In the list of policies, select the option button next to the name of the policy you created.
You can use the search box to filter the list of policies. c.
Choose Actions, Attach. d.
Under IAM entities, select the checkbox next to your identity (user, user group, or role).
You can use the search box to filter the list of entities. e.
Choose Attach policy.

##### View an animation: Create an IAM policy
##### View an animation: Attach an IAM policy

#### Task 2: Allow inbound traffic from the EC2 Instance Connect service to your instance When you use EC2 Instance Connect in the Amazon EC2 console to connect to an instance, the traffic that must be allowed to reach the instance is traffic from the EC2 Instance Connect service.
This is different to connecting from your local computer to an instance; in that case, you must allow traffic from your local computer to your instance. To allow traffic from the EC2 Instance Connect service, you must create a security group that allows inbound SSH traffic from the IP address range for the EC2 Instance Connect service.
AWS uses prefix lists to manage IP address ranges. The names of the EC2 Instance Connect prefix lists are as follows, with region replaced by the Region code:
- IPv4 prefix list name: com.amazonaws.region.ec2-instance-connect
- IPv6 prefix list name: com.amazonaws.region.ipv6.ec2-instance-connect Task objective You'll create a security group that allows inbound SSH traffic on port 22 from the IPv4 prefix list in the Region in which your instance is located.
To create a security group that allows inbound traffic from the EC2 Instance Connect service to your instance
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Security Groups.
3. Choose Create security group.
4. Under Basic details, do the following: a.
For Security group name, enter a meaningful name for your security group. b.
For Description, enter a meaningful description for your security group.
5. Under Inbound rules, do the following: a.
Choose Add rule. b.
For Type, choose SSH. c.
For Source, leave Custom. d.
In the field next to Source, select the prefix list for EC2 Instance Connect.

For example, if your instance is located in the US East (N. Virginia) (us-east-1) Region and your users will connect to its public IPv4 address, choose the following prefix list: com.amazonaws.us-east-1.ec2-instance-connect
6. Choose Create security group.
##### View an animation: Create the security group
#### Task 3: Launch your instance When you launch an instance, you must specify an AMI that contains the information required to launch the instance. You can choose to launch an instance with or without EC2 Instance Connect pre-installed. In this task, we specify an AMI that comes pre-installed with EC2 Instance Connect.
If you launch your instance without EC2 Instance Connect pre-installed, and you want to use EC2 Instance Connect to connect to your instance, you'll need to perform additional configuration steps. These steps are outside the scope of this tutorial.
Task objective You'll launch an instance with the Amazon Linux 2023 AMI, which comes pre-installed with EC2 Instance Connect. You'll also specify the security group that you created earlier so that you can use EC2 Instance Connect in the Amazon EC2 console to connect to your instance. Because you'll

use EC2 Instance Connect to connect to your instance, which pushes a public key to your instance's metadata, you won't need to specify an SSH key when you launch your instance.
To launch an instance that can use EC2 Instance Connect in the Amazon EC2 console for connection
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation bar at the top of the screen, the current AWS Region is displayed (for example, Ireland). Select a Region in which to launch your instance. This choice is important because you created a security group that allows traffic for a specific Region, so you must select the same Region in which to launch your instance.
3. From the Amazon EC2 console dashboard, choose Launch instance.
4. (Optional) Under Name and tags, for Name, enter a descriptive name for your instance.
5. Under Application and OS Images (Amazon Machine Image), choose Quick Start. Amazon Linux is selected by default. Under Amazon Machine Image (AMI), Amazon Linux 2023 AMI is selected by default. Keep the default selection for this task.
6. Under Instance type, for Instance type, keep the default selection, or choose a different instance type.
7. Under Key pair (login), for Key pair name, choose Proceed without a key pair (Not recommended). When you use EC2 Instance Connect to connect to an instance, EC2 Instance Connect pushes a key pair to the instance's metadata, and it is this key pair that is used for the connection.
8. Under Network settings, do the following: a.
For Auto-assign public IP, leave Enable.
Note To use EC2 Instance Connect in the Amazon EC2 console to connect to an instance, the instance must have a public IPv4 or IPv6 address. b.
For Firewall (security groups), choose Select existing security group. c.
Under Common security groups, choose the security group that you created earlier.
9. In the Summary panel, choose Launch instance.

##### View an animation: Launch your instance
#### Task 4: Connect to your instance When you connect to an instance using EC2 Instance Connect, the EC2 Instance Connect API pushes an SSH public key to the instance metadata where it remains for 60 seconds. The SSH daemon uses AuthorizedKeysCommand and AuthorizedKeysCommandUser to look up the public key from the instance metadata for authentication, and connects you to the instance.
Task objective In this task, you'll connect to your instance using EC2 Instance Connect in the Amazon EC2 console.
If you completed the prerequisite Tasks 1, 2, and 3, the connection should be successful.
Steps to connect to your instance Use the following steps to connect to your instance. To view an animation of the steps, see View an animation: Connect to your instance.
To connect an instance using EC2 Instance Connect in the Amazon EC2 console
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.

2. In the navigation bar at the top of the screen, the current AWS Region is displayed (for example, Ireland). Select the Region in which your instance is located.
3. In the navigation pane, choose Instances.
4. Select your instance and choose Connect.
5. Choose the EC2 Instance Connect tab.
6. Choose Connect using a Public IP.
7. Choose Connect.
A terminal window opens in the browser, and you are connected to your instance.
##### View an animation: Connect to your instance
### Prerequisites for EC2 Instance Connect The following are the prerequisites for installing and using EC2 Instance Connect:
- Install EC2 Instance Connect
- Ensure network connectivity
- Allow inbound SSH traffic

- Grant permissions
- Install an SSH client on your local computer
- Meet username requirements
#### Install EC2 Instance Connect To use EC2 Instance Connect to connect to an instance, the instance must have EC2 Instance Connect installed. You can either launch the instance using an AMI that comes pre-installed with EC2 Instance Connect, or you can install EC2 Instance Connect on instances that are launched with supported AMIs. For more information, see Install EC2 Instance Connect on your EC2 instances.
#### Ensure network connectivity Instances can be configured to allow users to connect to your instance over the internet or through the instance's private IP address. Depending on how your users will connect to your instance using EC2 Instance Connect, you must configure the following network access:
- If your users will connect to your instance over the internet, then your instance must have a public IPv4 or IPv6 address and be in a public subnet with a route to the internet. If you haven't modified your default public subnet, then it contains a route to the internet for IPv4 only, and not for IPv6. For more information, see Enable VPC internet access using internet gateways in the Amazon VPC User Guide.
- If your users will connect to your instance through the instance's private IPv4 address, then you must establish private network connectivity to your VPC, such as by using AWS Direct Connect, AWS Site-to-Site VPN, or VPC peering, so that your users can reach the instance's private IP address.
If your instance does not have a public IPv4 or IPv6 address and you prefer not to configure the network access as described above, you can consider EC2 Instance Connect Endpoint as an alternative to EC2 Instance Connect. With EC2 Instance Connect Endpoint, you can connect to an instance using SSH or RDP even if the instance does not have a public IPv4 or IPv6 address. For more information, see Connect to your Linux instance using the Amazon EC2 console.
#### Allow inbound SSH traffic When using the Amazon EC2 console to connect to an instance

When users connect to an instance using the Amazon EC2 console, the traffic that must be allowed to reach the instance is traffic from the EC2 Instance Connect service. The service is identified by specific IP address ranges, which AWS manages through prefix lists. You must create a security group that allows inbound SSH traffic from the EC2 Instance Connect service. To configure this, for the inbound rule, in the field next to Source, select the EC2 Instance Connect prefix list.
AWS provides different managed prefix lists for IPv4 and IPv6 addresses for each Region. The names of the EC2 Instance Connect prefix lists are as follows, with region replaced by the Region code:
- IPv4 prefix list name: com.amazonaws.region.ec2-instance-connect
- IPv6 prefix list name: com.amazonaws.region.ipv6.ec2-instance-connect For the instructions for creating the security group, see Task 2: Allow inbound traffic from the EC2 Instance Connect service to your instance. For more information, see Available AWS-managed prefix lists in the Amazon VPC User Guide.
When using the CLI or SSH to connect to an instance Ensure that the security group associated with your instance allows inbound SSH traffic on port 22 from your IP address or from your network. The default security group for the VPC does not allow incoming SSH traffic by default. The security group created by the launch instance wizard allows incoming SSH traffic by default. For more information, see Rules to connect to instances from your computer.
#### Grant permissions You must grant the required permissions to every IAM user who will use EC2 Instance Connect to connect to an instance. For more information, see Grant IAM permissions for EC2 Instance Connect.
#### Install an SSH client on your local computer If your users will connect using SSH, they must ensure that their local computer has an SSH client.
A user's local computer most likely has an SSH client installed by default. They can check for an SSH client by typing ssh at the command line. If their local computer doesn't recognize the command, they can install an SSH client. For information about installing an SSH client on Linux or macOS X, see http://www.openssh.com. For information about installing an SSH client on Windows 10, see OpenSSH in Windows.

There is no need to install an SSH client on a local computer if your users use only the Amazon EC2 console to connect to an instance.
#### Meet username requirements When using EC2 Instance Connect to connect to an instance, the username must meet the following requirements:
- First character: Must be a letter (A-Z, a-z), a digit (0-9), or an underscore (_)
- Subsequent characters: Can be letters (A-Z, a-z), digits (0-9), or the following characters: @ . _ -
- Minimum length: 1 character
- Maximum length: 31 characters
### Grant IAM permissions for EC2 Instance Connect To connect to an instance using EC2 Instance Connect, you must create an IAM policy that grants your users permissions for the following actions and condition:
- ec2-instance-connect:SendSSHPublicKey action – Grants permission to push the public key to an instance.
- ec2:osuser condition – Specifies the name of the OS user that can push the public key to an instance. Use the default username for the AMI that you used to launch the instance. The default username for AL2023 and Amazon Linux 2 is ec2-user, and for Ubuntu it's ubuntu.
- ec2:DescribeInstances action – Required when using the EC2 console because the wrapper calls this action. Users might already have permission to call this action from another policy.
- ec2:DescribeVpcs action – Required when connecting to an IPv6 address.
Consider restricting access to specific EC2 instances. Otherwise, all IAM principals with permission for the ec2-instance-connect:SendSSHPublicKey action can connect to all EC2 instances.
You can restrict access by specifying resource ARNs or by using resource tags as condition keys.
For more information, see Actions, resources, and condition keys for Amazon EC2 Instance Connect.
For information about creating IAM policies, see Creating IAM policies in the IAM User Guide.

#### Allow users to connect to specific instances The following IAM policy grants permission to connect to specific instances, identified by their resource ARNs.
In the following example IAM policy, the following actions and condition are specified:
- The ec2-instance-connect:SendSSHPublicKey action grants users permission to connect to two instances, specified by the resource ARNs. To grant users permission to connect to all EC2 instances, replace the resource ARNs with the * wildcard.
- The ec2:osuser condition grants permission to connect to the instances only if the ami- username is specified when connecting.
- The ec2:DescribeInstances action is specified to grant permission to users who will use the console to connect to your instances. If your users will only use an SSH client to connect to your instances, you can omit ec2:DescribeInstances. Note that the ec2:Describe* API actions do not support resource-level permissions. Therefore, the * wildcard is necessary in the Resource element.
- The ec2:DescribeVpcs action is specified to grant permission to users who will use the console to connect to your instances using an IPv6 address. If your users will only use a public IPv4 address, you can omit ec2:DescribeVpcs. Note that the ec2:Describe* API actions do not support resource-level permissions. Therefore, the * wildcard is necessary in the Resource element.
JSON { "Version":"2012-10-17", "Statement": [{ "Effect": "Allow", "Action": "ec2-instance-connect:SendSSHPublicKey", "Resource": [ "arn:aws:ec2:us- east-1:111122223333:instance/i-1234567890abcdef0", "arn:aws:ec2:us-east-1:111122223333:instance/i-0598c7d356eba48d7"
            ], "Condition": { "StringEquals": { "ec2:osuser": "ami-username"

                } } }, { "Effect": "Allow", "Action": [ "ec2:DescribeInstances", "ec2:DescribeVpcs"
            ], "Resource": "*"
        } ]
}
#### Allow users to connect to instances with specific tags Attribute-based access control (ABAC) is an authorization strategy that defines permissions based on tags that can be attached to users and AWS resources. You can use resource tags to control access to an instance. For more information about using tags to control access to your AWS resources, see Controlling access to AWS resources in the IAM User Guide.
In the following example IAM policy, the ec2-instance-connect:SendSSHPublicKey action grants users permission to connect to any instance (indicated by the * wildcard in the resource ARN) on condition that the instance has a resource tag with key=tag-key and value=tag-value.
The ec2:DescribeInstances action is specified to grant permission to users who will use the console to connect to your instances. If your users will use only an SSH client to connect to your instances, you can omit ec2:DescribeInstances. Note that the ec2:Describe* API actions do not support resource-level permissions. Therefore, the * wildcard is necessary in the Resource element.
The ec2:DescribeVpcs action is specified to grant permission to users who will use the console to connect to your instances using an IPv6 address. If your users will only use a public IPv4 address, you can omit ec2:DescribeVpcs. Note that the ec2:Describe* API actions do not support resource-level permissions. Therefore, the * wildcard is necessary in the Resource element.
JSON { "Version":"2012-10-17",

    "Statement": [{ "Effect": "Allow", "Action": "ec2-instance-connect:SendSSHPublicKey", "Resource": "arn:aws:ec2:us-east-1:111122223333:instance/*", "Condition": { "StringEquals": { "aws:ResourceTag/tag-key": "tag-value"
                } } }, { "Effect": "Allow", "Action": [ "ec2:DescribeInstances", "ec2:DescribeVpcs"
            ], "Resource": "*"
        } ]
}
### Install EC2 Instance Connect on your EC2 instances To connect to a Linux instance using EC2 Instance Connect, the instance must have EC2 Instance Connect installed. Installing EC2 Instance Connect configures the SSH daemon on the instance.
For more information about the EC2 Instance Connect package, see aws/aws-ec2-instance- connect-config  on the GitHub website.
Note If you configured the AuthorizedKeysCommand and AuthorizedKeysCommandUser settings for SSH authentication, the EC2 Instance Connect installation will not update them. As a result, you can't use EC2 Instance Connect.
#### Install prerequisites Before you install EC2 Instance Connect, ensure that you meet the following prerequisites.
- Verify that the instance uses one of the following:

- Amazon Linux 2 prior to version 2.0.20190618 *
- AL2023 minimal AMI or Amazon ECS-optimized AMI
- CentOS Stream 8 and 9
- macOS Sonoma prior to 14.2.1, Ventura prior to 13.6.3, and Monterey prior to 12.7.2 *
- Red Hat Enterprise Linux (RHEL) 8 and 9
- Ubuntu 16.04 and 18.04 * Tip
* For Amazon Linux 2, macOS, and Ubuntu: If you launched your instance using a later version than those listed above, EC2 Instance Connect comes preinstalled and no manual installation is required.
- Verify the general prerequisites for EC2 Instance Connect.
For more information, see Prerequisites for EC2 Instance Connect.
- Verify the prerequisites for connecting to your instance using an SSH client on your local machine.
For more information, see Connect to your Linux instance using SSH.
- Get the ID of the instance.
You can get the ID of your instance using the Amazon EC2 console (from the Instance ID column). If you prefer, you can use the describe-instances (AWS CLI) or Get-EC2Instance (AWS Tools for Windows PowerShell) command.
#### Manually install EC2 Instance Connect Note If you launched your instance using one of the following AMIs, EC2 Instance Connect is pre- installed and you can skip this procedure:
- AL2023 standard AMI
- Amazon Linux 2 2.0.20190618 or later
- macOS Sonoma 14.2.1 or later

- macOS Ventura 13.6.3 or later
- macOS Monterey 12.7.2 or later
- Ubuntu 20.04 or later Use one of the following procedures for installing EC2 Instance Connect, depending on the operating system of your instance.
Amazon Linux 2 To install EC2 Instance Connect on an instance launched with Amazon Linux 2
1. Connect to your instance using SSH.
Replace the example values in the following command with your values. Use the SSH key pair that was assigned to your instance when you launched it and the default username of the AMI that you used to launch your instance. For Amazon Linux 2, the default username is ec2-user.
$ ssh -i my_ec2_private_key.pem ec2-user@ec2-a-b-c-d.us- west-2.compute.amazonaws.com For more information about connecting to your instance, see Connect to your Linux instance using an SSH client.
2. Install the EC2 Instance Connect package on your instance.
[ec2-user ~]$ sudo yum install ec2-instance-connect You should see three new scripts in the /opt/aws/bin/ folder: eic_curl_authorized_keys eic_parse_authorized_keys eic_run_authorized_keys
3. (Optional) Verify that EC2 Instance Connect was successfully installed on your instance.
[ec2-user ~]$ sudo less /etc/ssh/sshd_config

EC2 Instance Connect was successfully installed if the AuthorizedKeysCommand and AuthorizedKeysCommandUser lines contain the following values:
AuthorizedKeysCommand /opt/aws/bin/eic_run_authorized_keys %u %f AuthorizedKeysCommandUser ec2-instance-connect
- AuthorizedKeysCommand sets the eic_run_authorized_keys script to look up the keys from the instance metadata
- AuthorizedKeysCommandUser sets the system user as ec2-instance-connect Note If you previously configured AuthorizedKeysCommand and AuthorizedKeysCommandUser, the EC2 Instance Connect installation will not change the values and you will not be able to use EC2 Instance Connect.
CentOS To install EC2 Instance Connect on an instance launched with CentOS
1. Connect to your instance using SSH.
Replace the example values in the following command with your values. Use the SSH key pair that was assigned to your instance when you launched it and the default username of the AMI that you used to launch your instance. For CentOS, the default username is centos or ec2-user.
$ ssh -i my_ec2_private_key.pem centos@ec2-a-b-c-d.us- west-2.compute.amazonaws.com For more information about connecting to your instance, see Connect to your Linux instance using an SSH client.
2. If you use an HTTP or HTTPS proxy, you must set the http_proxy or https_proxy environment variables in the current shell session.
If you're not using a proxy, you can skip this step.

- For an HTTP proxy server, run the following commands:
$ export http_proxy=http://hostname:port $ export https_proxy=http://hostname:port
- For an HTTPS proxy server, run the following commands:
$ export http_proxy=https://hostname:port $ export https_proxy=https://hostname:port
3. Install the EC2 Instance Connect package on your instance by running the following commands.
The EC2 Instance Connect configuration files for CentOS are provided in a Red Hat Package Manager (RPM) package, with different RPM packages for CentOS 8 and CentOS 9 and for instance types that run on Intel/AMD (x86_64) or ARM (AArch64).
Use the command block for your operating system and CPU architecture.
- CentOS 8 Intel/AMD (x86_64)
[ec2-user ~]$ mkdir /tmp/ec2-instance-connect [ec2-user ~]$ curl https://amazon-ec2-instance-connect-us- west-2.s3.us-west-2.amazonaws.com/latest/linux_amd64/ec2-instance- connect-2.0.0-5.rhel8.x86_64.rpm -o /tmp/ec2-instance-connect/ec2-instance- connect.rpm [ec2-user ~]$ curl https://amazon-ec2-instance-connect-us-west-2.s3.us- west-2.amazonaws.com/latest/linux_amd64/ec2-instance-connect- selinux-2.0.0-5.noarch.rpm -o /tmp/ec2-instance-connect/ec2-instance-connect- selinux.rpm [ec2-user ~]$ sudo yum install -y /tmp/ec2-instance-connect/ec2-instance- connect.rpm /tmp/ec2-instance-connect/ec2-instance-connect-selinux.rpm ARM (AArch64)
[ec2-user ~]$ mkdir /tmp/ec2-instance-connect [ec2-user ~]$ curl https://amazon-ec2-instance-connect-us- west-2.s3.us-west-2.amazonaws.com/latest/linux_arm64/ec2-instance-

connect-2.0.0-5.rhel8.aarch64.rpm -o /tmp/ec2-instance-connect/ec2-instance- connect.rpm [ec2-user ~]$ curl https://amazon-ec2-instance-connect-us-west-2.s3.us- west-2.amazonaws.com/latest/linux_arm64/ec2-instance-connect- selinux-2.0.0-5.noarch.rpm -o /tmp/ec2-instance-connect/ec2-instance-connect- selinux.rpm [ec2-user ~]$ sudo yum install -y /tmp/ec2-instance-connect/ec2-instance- connect.rpm /tmp/ec2-instance-connect/ec2-instance-connect-selinux.rpm
- CentOS 9 Intel/AMD (x86_64)
[ec2-user ~]$ mkdir /tmp/ec2-instance-connect [ec2-user ~]$ curl https://amazon-ec2-instance-connect-us- west-2.s3.us-west-2.amazonaws.com/latest/linux_amd64/ec2-instance- connect-2.0.0-5.rhel9.x86_64.rpm -o /tmp/ec2-instance-connect/ec2-instance- connect.rpm [ec2-user ~]$ curl https://amazon-ec2-instance-connect-us-west-2.s3.us- west-2.amazonaws.com/latest/linux_amd64/ec2-instance-connect- selinux-2.0.0-5.noarch.rpm -o /tmp/ec2-instance-connect/ec2-instance-connect- selinux.rpm [ec2-user ~]$ sudo yum install -y /tmp/ec2-instance-connect/ec2-instance- connect.rpm /tmp/ec2-instance-connect/ec2-instance-connect-selinux.rpm ARM (AArch64)
[ec2-user ~]$ mkdir /tmp/ec2-instance-connect [ec2-user ~]$ curl https://amazon-ec2-instance-connect-us- west-2.s3.us-west-2.amazonaws.com/latest/linux_arm64/ec2-instance- connect-2.0.0-5.rhel9.aarch64.rpm -o /tmp/ec2-instance-connect/ec2-instance- connect.rpm [ec2-user ~]$ curl https://amazon-ec2-instance-connect-us-west-2.s3.us- west-2.amazonaws.com/latest/linux_arm64/ec2-instance-connect- selinux-2.0.0-5.noarch.rpm -o /tmp/ec2-instance-connect/ec2-instance-connect- selinux.rpm [ec2-user ~]$ sudo yum install -y /tmp/ec2-instance-connect/ec2-instance- connect.rpm /tmp/ec2-instance-connect/ec2-instance-connect-selinux.rpm You should see the following new script in the /opt/aws/bin/ folder:

eic_run_authorized_keys
4. (Optional) Verify that EC2 Instance Connect was successfully installed on your instance.
- For CentOS 8:
[ec2-user ~]$ sudo less /lib/systemd/system/sshd.service.d/ec2-instance- connect.conf
- For CentOS 9:
[ec2-user ~]$ sudo less /etc/ssh/sshd_config.d/60-ec2-instance-connect.conf EC2 Instance Connect was successfully installed if the AuthorizedKeysCommand and AuthorizedKeysCommandUser lines contain the following values:
AuthorizedKeysCommand /opt/aws/bin/eic_run_authorized_keys %u %f AuthorizedKeysCommandUser ec2-instance-connect
- AuthorizedKeysCommand sets the eic_run_authorized_keys script to look up the keys from the instance metadata
- AuthorizedKeysCommandUser sets the system user as ec2-instance-connect Note If you previously configured AuthorizedKeysCommand and AuthorizedKeysCommandUser, the EC2 Instance Connect installation will not change the values and you will not be able to use EC2 Instance Connect. macOS To install EC2 Instance Connect on an instance launched with macOS
1. Connect to your instance using SSH.

Replace the example values in the following command with your values. Use the SSH key pair that was assigned to your instance when you launched it and the default username of the AMI that you used to launch your instance. For macOS instances, the default username is ec2-user.
$ ssh -i my_ec2_private_key.pem ec2-user@ec2-a-b-c-d.us- west-2.compute.amazonaws.com For more information about connecting to your instance, see Connect to your Linux instance using an SSH client.
2. Update Homebrew using the following command. The update will list the software that Homebrew knows about. The EC2 Instance Connect package is provided via Homebrew on macOS instances. For more information, see Update the operating system and software on Amazon EC2 Mac instances.
[ec2-user ~]$ brew update
3. Install the EC2 Instance Connect package on your instance. This will install the software and configure sshd to use it.
[ec2-user ~]$ brew install ec2-instance-connect You should see the following new script in the /opt/aws/bin/ folder: eic_run_authorized_keys
4. (Optional) Verify that EC2 Instance Connect was successfully installed on your instance.
[ec2-user ~]$ sudo less /etc/ssh/sshd_config.d/60-ec2-instance-connect.conf EC2 Instance Connect was successfully installed if the AuthorizedKeysCommand and AuthorizedKeysCommandUser lines contain the following values:
AuthorizedKeysCommand /opt/aws/bin/eic_run_authorized_keys %u %f AuthorizedKeysCommandUser ec2-instance-connect

- AuthorizedKeysCommand sets the eic_run_authorized_keys script to look up the keys from the instance metadata
- AuthorizedKeysCommandUser sets the system user as ec2-instance-connect Note If you previously configured AuthorizedKeysCommand and AuthorizedKeysCommandUser, the EC2 Instance Connect installation will not change the values and you will not be able to use EC2 Instance Connect.
RHEL To install EC2 Instance Connect on an instance launched with Red Hat Enterprise Linux (RHEL)
1. Connect to your instance using SSH.
Replace the example values in the following command with your values. Use the SSH key pair that was assigned to your instance when you launched it and the default username of the AMI that you used to launch your instance. For RHEL, the default username is ec2- user or root.
$ ssh -i my_ec2_private_key.pem ec2-user@ec2-a-b-c-d.us- west-2.compute.amazonaws.com For more information about connecting to your instance, see Connect to your Linux instance using an SSH client.
2. If you use an HTTP or HTTPS proxy, you must set the http_proxy or https_proxy environment variables in the current shell session.
If you're not using a proxy, you can skip this step.
- For an HTTP proxy server, run the following commands:
$ export http_proxy=http://hostname:port $ export https_proxy=http://hostname:port

- For an HTTPS proxy server, run the following commands:
$ export http_proxy=https://hostname:port $ export https_proxy=https://hostname:port
3. Install the EC2 Instance Connect package on your instance by running the following commands.
The EC2 Instance Connect configuration files for RHEL are provided in a Red Hat Package Manager (RPM) package, with different RPM packages for RHEL 8 and RHEL 9 and for instance types that run on Intel/AMD (x86_64) or ARM (AArch64).
Use the command block for your operating system and CPU architecture.
- RHEL 8 Intel/AMD (x86_64)
[ec2-user ~]$ mkdir /tmp/ec2-instance-connect [ec2-user ~]$ curl https://amazon-ec2-instance-connect-us- west-2.s3.us-west-2.amazonaws.com/latest/linux_amd64/ec2-instance- connect-2.0.0-5.rhel8.x86_64.rpm -o /tmp/ec2-instance-connect/ec2-instance- connect.rpm [ec2-user ~]$ curl https://amazon-ec2-instance-connect-us-west-2.s3.us- west-2.amazonaws.com/latest/linux_amd64/ec2-instance-connect- selinux-2.0.0-5.noarch.rpm -o /tmp/ec2-instance-connect/ec2-instance-connect- selinux.rpm [ec2-user ~]$ sudo yum install -y /tmp/ec2-instance-connect/ec2-instance- connect.rpm /tmp/ec2-instance-connect/ec2-instance-connect-selinux.rpm ARM (AArch64)
[ec2-user ~]$ mkdir /tmp/ec2-instance-connect [ec2-user ~]$ curl https://amazon-ec2-instance-connect-us- west-2.s3.us-west-2.amazonaws.com/latest/linux_arm64/ec2-instance- connect-2.0.0-5.rhel8.aarch64.rpm -o /tmp/ec2-instance-connect/ec2-instance- connect.rpm [ec2-user ~]$ curl https://amazon-ec2-instance-connect-us-west-2.s3.us- west-2.amazonaws.com/latest/linux_arm64/ec2-instance-connect- selinux-2.0.0-5.noarch.rpm -o /tmp/ec2-instance-connect/ec2-instance-connect- selinux.rpm

[ec2-user ~]$ sudo yum install -y /tmp/ec2-instance-connect/ec2-instance- connect.rpm /tmp/ec2-instance-connect/ec2-instance-connect-selinux.rpm
- RHEL 9 Intel/AMD (x86_64)
[ec2-user ~]$ mkdir /tmp/ec2-instance-connect [ec2-user ~]$ curl https://amazon-ec2-instance-connect-us- west-2.s3.us-west-2.amazonaws.com/latest/linux_amd64/ec2-instance- connect-2.0.0-5.rhel9.x86_64.rpm -o /tmp/ec2-instance-connect/ec2-instance- connect.rpm [ec2-user ~]$ curl https://amazon-ec2-instance-connect-us-west-2.s3.us- west-2.amazonaws.com/latest/linux_amd64/ec2-instance-connect- selinux-2.0.0-5.noarch.rpm -o /tmp/ec2-instance-connect/ec2-instance-connect- selinux.rpm [ec2-user ~]$ sudo yum install -y /tmp/ec2-instance-connect/ec2-instance- connect.rpm /tmp/ec2-instance-connect/ec2-instance-connect-selinux.rpm ARM (AArch64)
[ec2-user ~]$ mkdir /tmp/ec2-instance-connect [ec2-user ~]$ curl https://amazon-ec2-instance-connect-us- west-2.s3.us-west-2.amazonaws.com/latest/linux_arm64/ec2-instance- connect-2.0.0-5.rhel9.aarch64.rpm -o /tmp/ec2-instance-connect/ec2-instance- connect.rpm [ec2-user ~]$ curl https://amazon-ec2-instance-connect-us-west-2.s3.us- west-2.amazonaws.com/latest/linux_arm64/ec2-instance-connect- selinux-2.0.0-5.noarch.rpm -o /tmp/ec2-instance-connect/ec2-instance-connect- selinux.rpm [ec2-user ~]$ sudo yum install -y /tmp/ec2-instance-connect/ec2-instance- connect.rpm /tmp/ec2-instance-connect/ec2-instance-connect-selinux.rpm You should see the following new script in the /opt/aws/bin/ folder: eic_run_authorized_keys
4. (Optional) Verify that EC2 Instance Connect was successfully installed on your instance.
- For RHEL 8:

[ec2-user ~]$ sudo less /lib/systemd/system/sshd.service.d/ec2-instance- connect.conf
- For RHEL 9:
[ec2-user ~]$ sudo less /etc/ssh/sshd_config.d/60-ec2-instance-connect.conf EC2 Instance Connect was successfully installed if the AuthorizedKeysCommand and AuthorizedKeysCommandUser lines contain the following values:
AuthorizedKeysCommand /opt/aws/bin/eic_run_authorized_keys %u %f AuthorizedKeysCommandUser ec2-instance-connect
- AuthorizedKeysCommand sets the eic_run_authorized_keys script to look up the keys from the instance metadata
- AuthorizedKeysCommandUser sets the system user as ec2-instance-connect Note If you previously configured AuthorizedKeysCommand and AuthorizedKeysCommandUser, the EC2 Instance Connect installation will not change the values and you will not be able to use EC2 Instance Connect.
Ubuntu To install EC2 Instance Connect on an instance launched with Ubuntu 16.04 or later
1. Connect to your instance using SSH.
Replace the example values in the following command with your values. Use the SSH key pair that was assigned to your instance when you launched it and use the default username of the AMI that you used to launch your instance. For an Ubuntu AMI, the username is ubuntu.

$ ssh -i my_ec2_private_key.pem ubuntu@ec2-a-b-c-d.us- west-2.compute.amazonaws.com For more information about connecting to your instance, see Connect to your Linux instance using an SSH client.
2. (Optional) Ensure your instance has the latest Ubuntu AMI.
Run the following commands to update all the packages on your instance. ubuntu:~$ sudo apt-get update ubuntu:~$ sudo apt-get upgrade
3. Install the EC2 Instance Connect package on your instance. ubuntu:~$ sudo apt-get install ec2-instance-connect You should see three new scripts in the /usr/share/ec2-instance-connect/ folder: eic_curl_authorized_keys eic_parse_authorized_keys eic_run_authorized_keys
4. (Optional) Verify that EC2 Instance Connect was successfully installed on your instance. ubuntu:~$ sudo less /lib/systemd/system/ssh.service.d/ec2-instance-connect.conf EC2 Instance Connect was successfully installed if the AuthorizedKeysCommand and AuthorizedKeysCommandUser lines contain the following values:
AuthorizedKeysCommand /usr/share/ec2-instance-connect/eic_run_authorized_keys % %u %%f AuthorizedKeysCommandUser ec2-instance-connect
- AuthorizedKeysCommand sets the eic_run_authorized_keys script to look up the keys from the instance metadata
- AuthorizedKeysCommandUser sets the system user as ec2-instance-connect

Note If you previously configured AuthorizedKeysCommand and AuthorizedKeysCommandUser, the EC2 Instance Connect installation will not change the values and you will not be able to use EC2 Instance Connect.
### Connect to a Linux instance using EC2 Instance Connect The following instructions explain how to connect to your Linux instance using EC2 Instance Connect through the Amazon EC2 console, the AWS CLI, or an SSH client.
When you connect to an instance using EC2 Instance Connect through the console or AWS CLI, the EC2 Instance Connect API automatically pushes an SSH public key to the instance metadata where it remains for 60 seconds. An IAM policy attached to your user authorizes this action. If you prefer using your own SSH key, you can use an SSH client and explicitly push your SSH key to the instance using EC2 Instance Connect.
### Considerations After connecting to an instance using EC2 Instance Connect, the connection persists until the SSH session is terminated. The duration of the connection is not determined by the duration of your IAM credentials. If your IAM credentials expire, the connection continues to persist. When using the EC2 Instance Connect console experience, if your IAM credentials expire, terminate the connection by closing the browser page. When using your own SSH client and EC2 Instance Connect to push your key, you can set a SSH timeout value to terminate the SSH session automatically.
Requirements Before you begin, be sure to review the prerequisites.
Connection options
- Connect using the Amazon EC2 console
- Connect using the AWS CLI
- Connect using your own key and SSH client
- Troubleshoot

#### Connect using the Amazon EC2 console You can connect to an instance using EC2 Instance Connect through the Amazon EC2 console.
Requirements To connect using the Amazon EC2 console, the instance must have either a public IPv4 or IPv6 address. If the instance only has a private IPv4 address, you can use the ec2-instance-connect AWS CLI to connect.
To connect to your instance using the Amazon EC2 console
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Instances.
3. Select the instance and choose Connect.
4. Choose the EC2 Instance Connect tab.
5. Choose Connect using a Public IP.
6. If there is a choice, select the IP address to connect to. Otherwise, the IP address is selected automatically.
7. For Username, verify the username.
8. Choose Connect to establish a connection. An in-browser terminal window opens.
#### Connect using the AWS CLI You can use the ec2-instance-connect AWS CLI to connect to your instance with an SSH client. EC2 Instance Connect attempts to establish a connection using an available IP address in a predefined order, based on the specified connection type. If an IP address isn't available, it automatically tries the next one in the order.
Connection types auto (default)
EC2 Instance Connect tries to connect using the instance's IP addresses in the following order and with the corresponding connection type:
1. Public IPv4: direct
2. Private IPv4: eice
3. IPv6: direct

direct EC2 Instance Connect tries to connect using the instance's IP addresses in the following order:
1. Public IPv4
2. IPv6
3. Private IPv4 (it does not connect over an EC2 Instance Connect Endpoint) eice EC2 Instance Connect tries to connect using the instance's private IPv4 address and an EC2 Instance Connect Endpoint.
Note In the future, we might change the behavior of the auto connection type. To ensure that your desired connection type is used, we recommend that you explicitly set the -- connection-type to either direct or eice.
Requirements You must use AWS CLI version 2. For more information, see Install or update to the latest version of the AWS CLI.
To connect to an instance using the instance ID If you only know the instance ID, and want to let EC2 Instance Connect determine the connection type to use when connecting to your instance, use the ec2-instance-connect ssh CLI command with the instance ID. aws ec2-instance-connect ssh --instance-id i-1234567890example To connect to an instance using the instance ID and an EC2 Instance Connect Endpoint If you want to connect to your instance over an EC2 Instance Connect Endpoint, use the preceding command and also specify the --connection-type parameter with the eice value. aws ec2-instance-connect ssh --instance-id i-1234567890example --connection-type eice To connect to an instance using the instance ID and your own private key file

If you want to connect to your instance over an EC2 Instance Connect Endpoint using your own private key, specify the instance ID and the path to the private key file. Do not include file:// in the path; the following example will fail: file:///path/to/key. aws ec2-instance-connect ssh --instance-id i-1234567890example --private-key-file / path/to/key.pem Tip If you get an error when using these commands, make sure that you're using AWS CLI version 2, because the ssh command is only available in this major version. We also recommend regularly updating to the latest minor version of AWS CLI version 2 to access the latest features. For more information, see About AWS CLI version 2 in the AWS Command Line Interface User Guide.
#### Connect using your own key and SSH client You can use your own SSH key and connect to your instance from the SSH client of your choice while using the EC2 Instance Connect API. This enables you to benefit from the EC2 Instance Connect capability to push a public key to the instance. This connection method works for instances with public and private IP addresses.
Requirements
- Requirements for key pairs
- Supported types: RSA (OpenSSH and SSH2) and ED25519
- Supported lengths: 2048 and 4096
- For more information, see Create a key pair using a third-party tool and import the public key to Amazon EC2.
- When connecting to an instance that has only private IP addresses, the local computer from which you are initiating the SSH session must have connectivity to the EC2 Instance Connect service endpoint (to push your SSH public key to the instance) as well as network connectivity to the instance's private IP address to establish the SSH session. The EC2 Instance Connect service endpoint is reachable over the internet or over an Direct Connect public virtual interface. To connect to the instance's private IP address, you can leverage services such as Direct Connect, AWS Site-to-Site VPN, or VPC peering.

To connect to your instance using your own key and any SSH client
1. (Optional) Generate new SSH private and public keys You can generate new SSH private and public keys, my_key and my_key.pub, using the following command: ssh-keygen -t rsa -f my_key
2. Push your SSH public key to the instance Use the send-ssh-public-key command to push your SSH public key to the instance. If you launched your instance using AL2023 or Amazon Linux 2, the default username for the AMI is ec2-user. If you launched your instance using Ubuntu, the default username for the AMI is ubuntu.
The following example pushes the public key to the specified instance in the specified Availability Zone, to authenticate ec2-user. aws ec2-instance-connect send-ssh-public-key \ --region us-west-2 \ --availability-zone us-west-2b \ --instance-id i-001234a4bf70dec41EXAMPLE \ --instance-os-user ec2-user \ --ssh-public-key file://my_key.pub
3. Connect to the instance using your private key Use the ssh command to connect to the instance using the private key before the public key is removed from the instance metadata (you have 60 seconds before it is removed). Specify the private key that corresponds to the public key, the default username for the AMI that you used to launch your instance, and the instance's public DNS name (if connecting over a private network, specify the private DNS name or IP address). Add the IdentitiesOnly=yes option to ensure that only the files in the ssh config and the specified key are used for the connection. ssh -o "IdentitiesOnly=yes" -i my_key ec2- user@ec2-198-51-100-1.compute-1.amazonaws.com

The following example uses timeout 3600 to set your SSH session to terminate after 1 hour.
Processes started during the session may continue running on your instance after the session terminates. timeout 3600 ssh -o "IdentitiesOnly=yes" -i my_key ec2- user@ec2-198-51-100-1.compute-1.amazonaws.com
#### Troubleshoot If you receive an error while attempting to connect to your instance, see the following:
- Troubleshoot issues connecting to your Amazon EC2 Linux instance
- How do I troubleshoot issues connecting to my EC2 instance using EC2 Instance Connect?
### Uninstall EC2 Instance Connect To disable EC2 Instance Connect, connect to your Linux instance and uninstall the ec2-instance- connect package that is installed on the OS. If the sshd configuration matches what it was set to when you installed EC2 Instance Connect, uninstalling ec2-instance-connect also removes the sshd configuration. If you modified the sshd configuration after installing EC2 Instance Connect, you must update it manually.
Amazon Linux You can uninstall EC2 Instance Connect on AL2023 and Amazon Linux 2 2.0.20190618 or later, where EC2 Instance Connect is preconfigured.
To uninstall EC2 Instance Connect on an instance launched using Amazon Linux
1. Connect to your instance using SSH. Specify the SSH key pair you used for your instance when you launched it and the default username for the AL2023 or Amazon Linux 2 AMI, which is ec2-user.
For example, the following ssh command connects to the instance with the public DNS name ec2-a-b-c-d.us-west-2.compute.amazonaws.com, using the key pair my_ec2_private_key.pem.

$ ssh -i my_ec2_private_key.pem ec2-user@ec2-a-b-c-d.us- west-2.compute.amazonaws.com
2. Uninstall the ec2-instance-connect package using the yum command.
[ec2-user ~]$ sudo yum remove ec2-instance-connect Ubuntu To uninstall EC2 Instance Connect on an instance launched using an Ubuntu AMI
1. Connect to your instance using SSH. Specify the SSH key pair you used for your instance when you launched it and the default username for the Ubuntu AMI, which is ubuntu.
For example, the following ssh command connects to the instance with the public DNS name ec2-a-b-c-d.us-west-2.compute.amazonaws.com, using the key pair my_ec2_private_key.pem.
$ ssh -i my_ec2_private_key.pem ubuntu@ec2-a-b-c-d.us- west-2.compute.amazonaws.com
2. Uninstall the ec2-instance-connect package using the apt-get command. ubuntu:~$ sudo apt-get remove ec2-instance-connect
## Connect to your instances using a private IP address and EC2 Instance Connect Endpoint Connect Endpoint EC2 Instance Connect Endpoint allows you to connect securely to an instance from the internet, without using a bastion host, or requiring that your virtual private cloud (VPC) has direct internet connectivity.
Benefits
- You can connect to your instances without requiring the instances to have a public IPv4 or IPv6 address. AWS charges for all public IPv4 addresses, including public IPv4 addresses associated

with running instances and Elastic IP addresses. For more information, see the Public IPv4 Address tab on the Amazon VPC pricing page.
- You can connect to your instances from the internet without requiring that your VPC has direct internet connectivity through an internet gateway.
- You can control access to the creation and use of the EC2 Instance Connect Endpoints to connect to instances using  IAM policies and permissions.
- All attempts to connect to your instances, both successful and unsuccessful, are logged to CloudTrail.
Pricing There is no additional cost for using EC2 Instance Connect Endpoints. If you use an EC2 Instance Connect Endpoint to connect to an instance in a different Availability Zone, there is an additional charge for data transfer across Availability Zones.
Contents
- How it works
- Considerations
- Grant permissions to use EC2 Instance Connect Endpoint
- Security groups for EC2 Instance Connect Endpoint
- Create an EC2 Instance Connect Endpoint
- Modify an EC2 Instance Connect Endpoint
- Delete an EC2 Instance Connect Endpoint
- Connect to an Amazon EC2 instance using EC2 Instance Connect Endpoint
- Log connections established over EC2 Instance Connect Endpoint
- Service-linked role for EC2 Instance Connect Endpoint
- Quotas for EC2 Instance Connect Endpoint
### How it works EC2 Instance Connect Endpoint is an identity-aware TCP proxy. The EC2 Instance Connect Endpoint Service establishes a private tunnel from your computer to the endpoint using the credentials for your IAM entity. Traffic is authenticated and authorized before it reaches your VPC.

You can configure additional security group rules to restrict inbound traffic to your instances.
For example, you can use inbound rules to allow traffic on management ports only from the EC2 Instance Connect Endpoint.
You can configure route table rules to allow the endpoint to connect to any instance in any subnet of the VPC.
The following diagram shows how a user can connect to their instances from the internet using an EC2 Instance Connect Endpoint. First, create an EC2 Instance Connect Endpoint in subnet A. We create a network interface for the endpoint in the subnet, which serves as the entry point for traffic destined to your instances in the VPC. If the route table for subnet B allows traffic from subnet A, then you can use the endpoint to reach instances in subnet B.
Considerations Before you begin, consider the following.

- EC2 Instance Connect Endpoint is intended specifically for management traffic use cases, not for high volume data transfers. High volume data transfers are throttled.
- You can create an EC2 Instance Connect Endpoint to support traffic to an instance that has a private IPv4 address or IPv6 address. The IP address type of the endpoint must match the IP address of the instance. You can create an endpoint that supports all IP address types.
- (Linux instances) If you use your own key pair, you can use any Linux AMI. Otherwise, your instance must have EC2 Instance Connect installed. For information about which AMIs include EC2 Instance Connect and how to install it on other supported AMIs, see Install EC2 Instance Connect.
- You can assign a security group to an EC2 Instance Connect Endpoint. Otherwise, we use the default security group for the VPC. The security group for an EC2 Instance Connect Endpoint must allow outbound traffic to the destination instances. For more information, see Security groups for EC2 Instance Connect Endpoint.
- You can configure an EC2 Instance Connect Endpoint to preserve the source IP addresses of clients when routing requests to the instances. Otherwise, the IP address of the network interface becomes the client IP address for all incoming traffic.
- If you turn on client IP preservation, the security groups for the instances must allow traffic from the clients. Also, the instances must be in the same VPC as the EC2 Instance Connect Endpoint.
- If you turn off client IP preservation, the security groups for the instances must allow traffic from the VPC. This is the default.
- Client IP preservation is only supported on IPv4 EC2 Instance Connect Endpoints. To use client IP preservation, the IP address type of the EC2 Instance Connect Endpoint must be IPv4. Client IP preservation is not supported when the IP address type is dual-stack or IPv6.
- The following instance types do not support client IP preservation: C1, CG1, CG2, G1, HI1, M1, M2, M3, and T1. If you turn on client IP preservation and attempt to connect to an instance with one of these instance types by using EC2 Instance Connect Endpoint, the connection fails.
- Client IP preservation is not supported when traffic is routed through a transit gateway.
- When you create an EC2 Instance Connect Endpoint, a service-linked role is automatically created for the Amazon EC2 service in AWS Identity and Access Management (IAM). Amazon EC2 uses the service-linked role to provision network interfaces in your account, which are required when creating EC2 Instance Connect Endpoints. For more information, see Service-linked role for EC2 Instance Connect Endpoint.

- You can create only 1 EC2 Instance Connect Endpoint per VPC and per subnet. For more information, see Quotas for EC2 Instance Connect Endpoint. If you need to create another EC2 Instance Connect Endpoint in a different Availability Zone within the same VPC, you must first delete the existing EC2 Instance Connect Endpoint. Otherwise, you'll receive a quota error.
- Each EC2 Instance Connect Endpoint can support up to 20 concurrent connections.
- The maximum duration for an established TCP connection is 1 hour (3,600 seconds). You can specify the maximum allowed duration in an IAM policy, which can be up to 3,600 seconds.
For more information, see Permissions to use EC2 Instance Connect Endpoint to connect to instances.
The duration of the connection is not determined by the duration of your IAM credentials. If your IAM credentials expire, the connection continues to persist until the specified maximum duration is reached. When you connect to an instance using the EC2 Instance Connect Endpoint console experience, set Max tunnel duration (seconds) to a value that is less than the duration of your IAM credentials. If your IAM credentials expire early, terminate the connection to your instance by closing the browser page.
### Grant permissions to use EC2 Instance Connect Endpoint By default, IAM entities don't have permission to create, describe, or modify EC2 Instance Connect Endpoints. An IAM administrator can create IAM policies that grant the permissions required to perform specific actions on the resources that they need.
For information about creating IAM policies, see Creating IAM policies in the IAM User Guide.
The following example policies show how you can control the permissions that users have to EC2 Instance Connect Endpoints.
Examples
- Permissions to create, describe, modify, and delete EC2 Instance Connect Endpoints
- Permissions to use EC2 Instance Connect Endpoint to connect to instances
- Permissions to connect only from a specific IP address range
#### Permissions to create, describe, modify, and delete EC2 Instance Connect Endpoints To create and modify an EC2 Instance Connect Endpoint, users require permissions for the following actions:

- ec2:CreateInstanceConnectEndpoint
- ec2:CreateNetworkInterface
- ec2:CreateTags
- ec2:ModifyInstanceConnectEndpoint
- iam:CreateServiceLinkedRole To describe and delete EC2 Instance Connect Endpoints, users require permissions for the following actions:
- ec2:DescribeInstanceConnectEndpoints
- ec2:DeleteInstanceConnectEndpoint You can create a policy that grants permission to create, describe, modify, and delete EC2 Instance Connect Endpoints in all subnets. Alternatively, you can restrict actions for specified subnets only by specifying the subnet ARNs as the allowed Resource or by using the ec2:SubnetID condition key. You can also use the aws:ResourceTag condition key to explicitly allow or deny endpoint creation with certain tags. For more information, see Policies and permissions in IAM in the IAM User Guide.
Example IAM policy In the following example IAM policy, the Resource section grants permission to create, modify, and delete endpoints in all subnets, specified by the asterisk (*). The ec2:Describe* API actions do not support resource-level permissions. Therefore, the * wildcard is necessary in the Resource element.
#### Permissions to use EC2 Instance Connect Endpoint to connect to instances The ec2-instance-connect:OpenTunnel action grants permission to establish a TCP connection to an instance to connect over the EC2 Instance Connect Endpoint. You can specify the EC2 Instance Connect Endpoint to use. Alternatively, a Resource with an asterisk (*) allows users to use any available EC2 Instance Connect Endpoint. You can also restrict access to instances based on the presence or absence of resource tags as condition keys.

Conditions
- ec2-instance-connect:remotePort – The port on the instance that can be used to establish a TCP connection. When this condition key is used, attempting to connect to an instance on any other port other than the port specified in the policy results in a failure.
- ec2-instance-connect:privateIpAddress – The destination private IP address associated with the instance that you want to establish a TCP connection with. You can specify a single IP address, such as 10.0.0.1/32, or a range of IPs through CIDRs, such as 10.0.1.0/28.
When this condition key is used, attempting to connect to an instance with a different private IP address or outside the CIDR range results in a failure.
- ec2-instance-connect:maxTunnelDuration – The maximum duration for an established TCP connection. The unit is seconds and the duration ranges from a minimum of 1 second to a maximum of 3,600 seconds (1 hour). If the condition is not specified, the default duration is set to 3,600 seconds (1 hour). Attempting to connect to an instance for longer than the specified duration in the IAM policy or for longer than the default maximum results in a failure. The connection is disconnected after the specified duration.
If maxTunnelDuration is specified in the IAM policy and the value specified is less than 3,600 seconds (the default), then you must specify --max-tunnel-duration in the command when connecting to an instance. For information about how to connect to an instance, see Connect to an Amazon EC2 instance using EC2 Instance Connect Endpoint.
You can also grant a user access to establish connections to instances based on the presence of resource tags on the EC2 Instance Connect Endpoint. For more information, see Policies and permissions in IAM in the IAM User Guide.
For Linux instances, the ec2-instance-connect:SendSSHPublicKey action grants permission to push the public key to an instance. The ec2:osuser condition specifies the name of the OS (operating system) user that can push the public key to an instance. Use the default username for the AMI that you used to launch the instance. For more information, see Grant IAM permissions for EC2 Instance Connect.
Example IAM policy The following example IAM policies allow an IAM principal to connect to an instance using only the specified EC2 Instance Connect Endpoint, identified by the specified endpoint ID eice-123456789abcdef. The connection is successfully established only if all the conditions are satisfied.

Note The ec2:Describe* API actions do not support resource-level permissions. Therefore, the
* wildcard is necessary in the Resource element.
Linux This example evaluates if the connection to the instance is established on —port 22 (SSH), if the private IP address of the instance lies within the range of 10.0.1.0/31 (between 10.0.1.0 and 10.0.1.1), and the maxTunnelDuration is less than or equal to 3600 seconds. The connection is disconnected after 3600 seconds (1 hour).
JSON { "Version":"2012-10-17", "Statement": [{ "Sid": "EC2InstanceConnect", "Action": "ec2-instance-connect:OpenTunnel", "Effect": "Allow", "Resource": "arn:aws:ec2:us-east-1:111122223333:instance-connect- endpoint/eice-123456789abcdef", "Condition": { "NumericEquals": { "ec2-instance-connect:remotePort": "22"
                }, "IpAddress": { "ec2-instance-connect:privateIpAddress": "10.0.1.0/31"
                }, "NumericLessThanEquals": { "ec2-instance-connect:maxTunnelDuration": "3600"
                } } }, { "Sid": "SSHPublicKey", "Effect": "Allow", "Action": "ec2-instance-connect:SendSSHPublicKey", "Resource": "*", "Condition": {

                "StringEquals": { "ec2:osuser": "ami-username"
                } } }, { "Sid": "Describe", "Action": [ "ec2:DescribeInstances", "ec2:DescribeInstanceConnectEndpoints"
            ], "Effect": "Allow", "Resource": "*"
        } ]
} Windows This example evaluates if the connection to the instance is established on port 3389 (RDP), if the private IP address of the instance lies within the range of 10.0.1.0/31 (between 10.0.1.0 and 10.0.1.1), and the maxTunnelDuration is less than or equal to 3600 seconds. The connection is disconnected after 3600 seconds (1 hour).
JSON { "Version":"2012-10-17", "Statement": [{ "Sid": "EC2InstanceConnect", "Action": "ec2-instance-connect:OpenTunnel", "Effect": "Allow", "Resource": "arn:aws:ec2:us-east-1:111122223333:instance-connect- endpoint/eice-123456789abcdef", "Condition": { "NumericEquals": { "ec2-instance-connect:remotePort": "3389"
                }, "IpAddress": { "ec2-instance-connect:privateIpAddress": "10.0.1.0/31"
                },

                "NumericLessThanEquals": { "ec2-instance-connect:maxTunnelDuration": "3600"
                } } }, { "Sid": "Describe", "Action": [ "ec2:DescribeInstances", "ec2:DescribeInstanceConnectEndpoints"
            ], "Effect": "Allow", "Resource": "*"
        } ]
}
#### Permissions to connect only from a specific IP address range The following example IAM policy allows an IAM principal to connect to an instance on condition they are connecting from an IP address within the IP address range specified in the policy. If the IAM principal calls OpenTunnel from an IP address not within 192.0.2.0/24 (the example IP address range in this policy), the response is Access Denied. For more information, see aws:SourceIp in the IAM User Guide.
JSON { "Version":"2012-10-17", "Statement": [{ "Effect": "Allow", "Action": "ec2-instance-connect:OpenTunnel", "Resource": "arn:aws:ec2:us-east-1:111122223333:instance-connect- endpoint/eice-123456789abcdef", "Condition": { "IpAddress": { "aws:SourceIp": "192.0.2.0/24"
                }, "NumericEquals": { "ec2-instance-connect:remotePort": "22"
                }

            } }, { "Sid": "SSHPublicKey", "Effect": "Allow", "Action": "ec2-instance-connect:SendSSHPublicKey", "Resource": "*", "Condition": { "StringEquals": { "ec2:osuser": "ami-username"
                } } }, { "Effect": "Allow", "Action": [ "ec2:DescribeInstances", "ec2:DescribeInstanceConnectEndpoints"
            ], "Resource": "*"
        } ]
}
### Security groups for EC2 Instance Connect Endpoint A security group controls the traffic that is allowed to reach and leave the resources that it is associated with. For example, we deny traffic to and from an Amazon EC2 instance unless it is specifically allowed by the security groups associated with the instance.
The following examples show you how to configure the security group rules for the EC2 Instance Connect Endpoint and the target instances.
Examples
- EC2 Instance Connect Endpoint security group rules
- Target instance security group rules

#### EC2 Instance Connect Endpoint security group rules The security group rules for an EC2 Instance Connect Endpoint must allow outbound traffic destined for the target instances to leave the endpoint. You can specify either the instance security group or the IPv4 or IPv6 address range of the VPC as the destination.
Traffic to the endpoint originates from the EC2 Instance Connect Endpoint Service, and it is allowed regardless of the inbound rules for the endpoint security group. To control who can use EC2 Instance Connect Endpoint to connect to an instance, use an IAM policy. For more information, see Permissions to use EC2 Instance Connect Endpoint to connect to instances.
Example outbound rule: Security group referencing The following example uses security group referencing, which means that the destination is a security group associated with the target instances. This rule allows outbound traffic from the endpoint to all instances that use this security group.
Protocol Destination Port range Comment TCP ID of instance security group 22 Allows outbound SSH traffic to all instances associated with the instance security group Example outbound rule: IPv4 address range The following example allows outbound traffic to the specified IPv4 address range. The IPv4 addresses of an instance is assigned from its subnet, so you can use the IPv4 address range of the VPC.
Protocol Destination Port range Comment TCP VPC IPv4 CIDR 22 Allows outbound SSH traffic to the VPC Example outbound rule: IPv6 address range

The following example allows outbound traffic to the specified IPv6 address range. The IPv6 addresses of an instance is assigned from its subnet, so you can use the IPv6 address range of the VPC.
Protocol Destination Port range Comment TCP VPC IPv6 CIDR 22 Allows outbound SSH traffic to the VPC
#### Target instance security group rules The security group rules for target instances must allow inbound traffic from the EC2 Instance Connect Endpoint. You can specify either the endpoint security group or an IPv4 or IPv6 address range as the source. If you specify an IPv4 address range, the source depends on whether client IP preservation is off or on. For more information, see Considerations.
Because security groups are stateful, the response traffic is allowed to leave the VPC regardless of the outbound rules for the instance security group.
Example inbound rule: Security group referencing The following example uses security group referencing, which means that the source is the security group associated with the endpoint. This rule allows inbound SSH traffic from the endpoint to all instances that use this security group, whether client IP preservation is on or off. If there are no other inbound security group rules for SSH, then the instances accept SSH traffic only from the endpoint.
Protocol Source Port range Comment TCP ID of endpoint security group 22 Allows inbound SSH traffic from the resources associated with the endpoint security group Example inbound rule: Client IP preservation off The following example allows inbound SSH traffic from the specified IPv4 address range. Because client IP preservation is off, the source IPv4 address is the address of the endpoint network

interface. The address of the endpoint network interface is assigned from its subnet, so you can use the IPv4 address range of the VPC to allow connections to all instances in the VPC.
Protocol Source Port range Comment TCP VPC IPv4 CIDR 22 Allows inbound SSH traffic from the VPC Example inbound rule: Client IP preservation on The following example allows inbound SSH traffic from the specified IPv4 address range. Because client IP preservation is on, the source IPv4 address is the address of the client.
Protocol Source Port range Comment TCP Public IPv4 address range 22 Allows inbound traffic from the specified client IPv4 address range
### Create an EC2 Instance Connect Endpoint You can create an EC2 Instance Connect Endpoint to allow secure connection to your instances.
Considerations
- Shared subnets – You can create an EC2 Instance Connect Endpoint in a subnet shared with you.
However, you can't use EC2 Instance Connect Endpoints that the VPC owner created in a subnet shared with you.
- IP address types – EC2 Instance Connect Endpoints support the following address types, which must be compatible with your subnet:
- ipv4 – Connect only to EC2 instances with private IPv4 addresses.
- dualstack – Connect to EC2 instances with either private IPv4 addresses or IPv6 addresses.
- ipv6 – Connect only to EC2 instances with IPv6 addresses.
Prerequisites

You must have the required IAM permissions to create an EC2 Instance Connect Endpoint. For more information, see Permissions to create, describe, modify, and delete EC2 Instance Connect Endpoints.
Console To create an EC2 Instance Connect Endpoint
1. Open the Amazon VPC console at https://console.aws.amazon.com/vpc/.
2. In the left navigation pane, choose Endpoints.
3. Choose Create endpoint, and then specify the endpoint settings as follows: a.
(Optional) For Name tag, enter a name for the endpoint. b.
For Type, choose EC2 Instance Connect Endpoint. c.
Under Network settings, for VPC, select the VPC that has the target instances. d.
(Optional) To preserve client IP addresses, expand Additional settings and select the Preserve Client IP check box. Otherwise, the default is to use the endpoint network interface as the client IP address.
Note This option is only available when the endpoint's IP address type is configured as IPv4. e.
(Optional) For Security groups, select the security group to associate with the endpoint. Otherwise, the default is to use the default security group for the VPC. For more information, see Security groups for EC2 Instance Connect Endpoint. f.
For Subnet, select the subnet in which to create the endpoint. g.
For IP address type, choose the IP address type for the endpoint. Choose Dualstack if you need to support both IPv4 and IPv6 connections to your instances. Choose IPv4 if you need to support client IP preservation. h.
(Optional) To add a tag, choose Add new tag and enter the tag key and the tag value.
4. Review your settings and then choose Create endpoint.
The initial status of the endpoint is Pending. Before you can connect to an instance using this endpoint, you must wait until the endpoint status is Available. This can take a few minutes.

5. To connect to an instance using your endpoint, see Connect to an instance.
AWS CLI To create an EC2 Instance Connect Endpoint Use the create-instance-connect-endpoint command. aws ec2 create-instance-connect-endpoint \ --subnet-id subnet-0123456789example To specify the type of traffic that the endpoint supports, include the --ip-address-type parameter. Valid values are ipv4, dualstack, or ipv6. The subnet must support the IP address type that you specify. When the --ip-address-type parameter is omitted, the default value is determined by the IP address type supported by the subnet. aws ec2 create-instance-connect-endpoint \ --subnet-id subnet-0123456789example \ --ip-address-type ipv4 The following is example output.
{ "OwnerId": "111111111111", "InstanceConnectEndpointId": "eice-0123456789example", "InstanceConnectEndpointArn": "arn:aws:ec2:us-east-1:111111111111:instance- connect-endpoint/eice-0123456789example", "State": "create-complete", "StateMessage": "", "DnsName": "eice-0123456789example.0123abcd.ec2-instance-connect- endpoint.us-east-1.amazonaws.com", "FipsDnsName": "eice-0123456789example.0123abcd.fips.ec2-instance-connect- endpoint.us-east-1.amazonaws.com", "NetworkInterfaceIds": [ "eni-0123abcd"
        ], "VpcId": "vpc-0123abcd", "AvailabilityZone": "us-east-1a", "AvailabilityZoneId": "use1-az4", "CreatedAt": "2023-04-07T15:43:53.000Z", "SubnetId": "subnet-0123abcd",

        "PreserveClientIp": false, "SecurityGroupIds": [ "sg-0123abcd"
        ], "Tags": [], "IpAddressType": "ipv4"
} To monitor the creation status The initial value for the State field is create-in-progress. Before you can connect to an instance using this endpoint, wait until the state is create-complete. Use the describe- instance-connect-endpoints command to monitor the status of the EC2 Instance Connect Endpoint. The --query parameter filters the results to the State field. aws ec2 describe-instance-connect-endpoints --instance-connect-endpoint- ids eice-0123456789example --query InstanceConnectEndpoints[*].State --output text The following is example output. create-complete PowerShell To create the EC2 Instance Connect Endpoint Use the New-EC2InstanceConnectEndpoint cmdlet.
New-EC2InstanceConnectEndpoint -SubnetId subnet-0123456789example To specify the type of traffic that the endpoint supports, include the -IpAddressType parameter. Valid values are ipv4, dualstack, or ipv6. The subnet must support the IP address type that you specify. When the -IpAddressType parameter is omitted, the default value is determined by the IP address type supported by the subnet.
New-EC2InstanceConnectEndpoint -SubnetId subnet-0123456789example - IpAddressType ipv4 The following is example output.
OwnerId                     : 111111111111

InstanceConnectEndpointId   : eice-0123456789example InstanceConnectEndpointArn  : arn:aws:ec2:us-east-1:111111111111:instance-connect- endpoint/eice-0123456789example State                       : create-complete StateMessage                :
DnsName                     : eice-0123456789example.0123abcd.ec2-instance-connect- endpoint.us-east-1.amazonaws.com FipsDnsName                 : eice-0123456789example.0123abcd.fips.ec2-instance- connect-endpoint.us-east-1.amazonaws.com NetworkInterfaceIds         : {eni-0123abcd} VpcId                       : vpc-0123abcd AvailabilityZone            : us-east-1a AvailabilityZoneId          : use1-az4 CreatedAt                   : 4/7/2023 3:43:53 PM SubnetId                    : subnet-0123abcd PreserveClientIp            : False SecurityGroupIds            : {sg-0123abcd} Tags                        : {} IpAddressType               : ipv4 To monitor the creation status The initial value for the State field is create-in-progress. Before you can connect to an instance using this endpoint, wait until the state is create-complete. Use the Get- EC2InstanceConnectEndpoint cmdlet to monitor the status of the EC2 Instance Connect Endpoint. .State.Value filters the results to the State field.
(Get-EC2InstanceConnectEndpoint -InstanceConnectEndpointId "eice-0123456789example").State.Value The following is example output. create-complete
### Modify an EC2 Instance Connect Endpoint You can modify existing EC2 Instance Connect Endpoints using the AWS CLI or an SDK. The Amazon EC2 console doesn't support endpoint modification.
Before you begin, you must have the required IAM permissions. For more information, see Permissions to create, describe, modify, and delete EC2 Instance Connect Endpoints.

#### Parameters you can modify You can modify the following EC2 Instance Connect Endpoint parameters:
Security groups You can specify new security groups for the EC2 Instance Connect Endpoint. The new security groups replace the current security groups.
When modifying the security groups, you must specify:
- At least one security group, even if it's just the default security group in the VPC.
- The IDs of the security groups, not the names.
IP address type You can specify a new IP address type for the EC2 Instance Connect Endpoint.
Valid values: ipv4 | dualstack | ipv6 Preserve client IP setting You can specify whether to preserve the client IP address as the source.
Note Preserving the client IP is only supported on IPv4 EC2 Instance Connect Endpoints.
When enabling PreserveClientIp, either the endpoint's existing IP address type must be ipv4, or if modifying the IP address type in the same request, the new value must be ipv4.
AWS CLI To modify an EC2 Instance Connect Endpoint Use the modify-instance-connect-endpoint command and specify the EC2 Instance Connect Endpoint and the parameters to modify. The following example modifies all the parameters in a single request. aws ec2 modify-instance-connect-endpoint \ --instance-connect-endpoint-id eice-0123456789example \

    --security-group-ids sg-0123456789example \ --ip-address-type dualstack \ --no-preserve-client-ip The following is example output.
{ "Return": true } To monitor the update status During modification, the EC2 Instance Connect Endpoint status changes to update-in- progress. The update process runs asynchronously and completes with either an update- complete or update-failed status. The endpoint uses its old configuration until the status changes to update-complete.
Use the describe-instance-connect-endpoints command to monitor the update status. The -- query parameter filters the results to the State field. aws ec2 describe-instance-connect-endpoints \ --instance-connect-endpoint-ids eice-0123456789example \ --query InstanceConnectEndpoints[*].State --output text The following is example output. update-complete PowerShell To modify an EC2 Instance Connect Endpoint Use the Edit-EC2InstanceConnectEndpoint cmdlet and specify the EC2 Instance Connect Endpoint and the parameters to modify. The following example modifies all the parameters in a single request.
Edit-EC2InstanceConnectEndpoint `
    -InstanceConnectEndpointId eice-0123456789example `
    -SecurityGroupIds sg-0123456789example `
    -IpAddressType dualstack `

    -PreserveClientIp $false The following is example output.
True To monitor the update status During modification, the EC2 Instance Connect Endpoint status changes to update-in- progress. The update process runs asynchronously and completes with either an update- complete or update-failed status. The endpoint uses its old configuration until the status changes to update-complete.
Use the Get-EC2InstanceConnectEndpoint command to monitor the update status.
.State.Value filters the results to the State field.
(Get-EC2InstanceConnectEndpoint -InstanceConnectEndpointId "eice-0123456789example").State.Value The following is example output. update-complete
### Delete an EC2 Instance Connect Endpoint When you are finished with an EC2 Instance Connect Endpoint, you can delete it.
You must have the required IAM permissions to create an EC2 Instance Connect Endpoint. For more information, see Permissions to create, describe, modify, and delete EC2 Instance Connect Endpoints.
When you delete an EC2 Instance Connect Endpoint using the console, it enters the Deleting state. If deletion is successful, the deleted endpoint no longer appears. If deletion fails, the state is delete-failed and Status message provides the failure reason.
When you delete an EC2 Instance Connect Endpoint using the AWS CLI, it enters the delete-in- progress state. If deletion is successful, it enters the delete-complete state. If deletion fails, the state is delete-failed and StateMessage provides the failure reason.

Console To delete an EC2 Instance Connect Endpoint
1. Open the Amazon VPC console at https://console.aws.amazon.com/vpc/.
2. In the left navigation pane, choose Endpoints.
3. Select the endpoint.
4. Choose Actions, Delete VPC endpoints.
5. When prompted for confirmation, enter delete.
6. Choose Delete.
AWS CLI To delete an EC2 Instance Connect Endpoint Use the delete-instance-connect-endpoint command and specify the ID of the EC2 Instance Connect Endpoint to delete. aws ec2 delete-instance-connect-endpoint --instance-connect-endpoint- id eice-03f5e49b83924bbc7 The following is example output.
{ "InstanceConnectEndpoint": { "OwnerId": "111111111111", "InstanceConnectEndpointId": "eice-0123456789example", "InstanceConnectEndpointArn": "arn:aws:ec2:us-east-1:111111111111:instance- connect-endpoint/eice-0123456789example", "State": "delete-in-progress", "StateMessage": "", "NetworkInterfaceIds": [], "VpcId": "vpc-0123abcd", "AvailabilityZone": "us-east-1d", "AvailabilityZoneId": "use1-az2", "CreatedAt": "2023-02-07T12:05:37+00:00", "SubnetId": "subnet-0123abcd"
    } }

PowerShell To delete an EC2 Instance Connect Endpoint Use the Remove-EC2InstanceConnectEndpoint cmdlet and specify the ID of the EC2 Instance Connect Endpoint to delete.
Remove-EC2InstanceConnectEndpoint -InstanceConnectEndpointId eice-03f5e49b83924bbc7 The following is example output.
@{ InstanceConnectEndpoint = @{ OwnerId = "111111111111"
        InstanceConnectEndpointId = "eice-0123456789example"
        InstanceConnectEndpointArn = "arn:aws:ec2:us-east-1:111111111111:instance- connect-endpoint/eice-0123456789example"
        State = "delete-in-progress"
        StateMessage = ""
        NetworkInterfaceIds = @()
        VpcId = "vpc-0123abcd"
        AvailabilityZone = "us-east-1d"
        AvailabilityZoneId = "use1-az2"
        CreatedAt = "2023-02-07T12:05:37+00:00"
        SubnetId = "subnet-0123abcd"
    } }
### Connect to an Amazon EC2 instance using EC2 Instance Connect Endpoint You can use EC2 Instance Connect Endpoint to connect to an Amazon EC2 instance that supports SSH or RDP.
Prerequisites
- You must have the required IAM permission to connect to an EC2 Instance Connect Endpoint.
For more information, see Permissions to use EC2 Instance Connect Endpoint to connect to instances.
- The EC2 Instance Connect Endpoint must be in one of the following states:
- create-complete for a new endpoint

- update-in-progress, update-complete, or update-failed for an existing endpoint being modified. When modifying an endpoint, it continues using its original configuration until the status changes to update-complete.
If your VPC doesn't have an EC2 Instance Connect Endpoint, you can create one. For more information, see Create an EC2 Instance Connect Endpoint.
- The EC2 Instance Connect Endpoint IP address type must be compatible with the IP address type of the instance. If your endpoint IP address type is dual-stack, then it can work for both IPv4 and IPv6 addresses.
- (Linux instances) To use the Amazon EC2 console to connect to your instance, or to use the CLI to connect and have EC2 Instance Connect handle the ephemeral key, your instance must have EC2 Instance Connect installed. For more information, see Install EC2 Instance Connect.
- Ensure that the security group of the instance allows inbound SSH traffic from the EC2 Instance Connect Endpoint. For more information, see Target instance security group rules.
Connection options
- Connect to your Linux instance using the Amazon EC2 console
- Connect to your Linux instance using SSH
- Connect to your Linux instance with its instance ID using the AWS CLI
- Connect to your Windows instance using RDP
- Troubleshoot
#### Connect to your Linux instance using the Amazon EC2 console You can connect to an instance using the Amazon EC2 console (a browser-based client) as follows.
To connect to your instance using the Amazon EC2 console
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Instances.
3. Select the instance, and then choose Connect.
4. Choose the EC2 Instance Connect tab.
5. For Connection type, choose Connect using a Private IP.

6. Choose either Private IPv4 address or IPv6 address. The options are available based on the IP addresses assigned to your instance. If an option is greyed out, your instance does not have an IP address of that type assigned to it.
7. For EC2 Instance Connect Endpoint, choose the ID of the EC2 Instance Connect Endpoint.
Note The EC2 Instance Connect Endpoint must be compatible with the IP address you chose in the previous step. If your endpoint IP address type is dual-stack, then it can work for both IPv4 and IPv6 addresses. For more information, see Create an EC2 Instance Connect Endpoint.
8. For Username, if the AMI that you used to launch the instance uses a username other than ec2-user, enter the correct username.
9. For Max tunnel duration (seconds), enter the maximum allowed duration for the SSH connection.
The duration must comply with any maxTunnelDuration condition specified in the IAM policy. If you don't have access to the IAM policy, contact your administrator.
10. Choose Connect. This opens a terminal window for your instance.
#### Connect to your Linux instance using SSH You can use SSH to connect to your Linux instance, and use the open-tunnel command to establish a private tunnel. You can use open-tunnel in single connection or multi-connection mode. You can specify your instance ID, a private IPv4 address, or an IPv6 address.
For information about using the AWS CLI to connect to your instance using SSH, see Connect using the AWS CLI.
The following examples use OpenSSH. You can use any other SSH client that supports a proxy mode.
##### Single connection To allow only a single connection to an instance using SSH and the open-tunnel command Use ssh and the open-tunnel AWS CLI command as follows. The -o proxy command encloses the open-tunnel command that creates the private tunnel to the instance.

ssh -i my-key-pair.pem ec2-user@i-1234567890abcdef0 \ -o ProxyCommand='aws ec2-instance-connect open-tunnel --instance- id i-1234567890abcdef0'
For:
- -i – Specify the key pair that was used to launch the instance.
- ec2-user@i-1234567890abcdef0 – Specify the username of the AMI that was used to launch the instance, and the instance ID. For instances with an IPv6 address, you must specify the IPv6 address instead of the instance ID.
- --instance-id – Specify the ID of the instance to connect to. Alternatively, specify %h, which extracts the instance ID from the user. For instances with an IPv6 address, replace --instance-id i-1234567890abcdef0 with --private-ip-address 2001:db8::1234:5678:1.2.3.4.
##### Multi-connection To allow multiple connections to an instance, first run the open-tunnel AWS CLI command to start listening for new TCP connections, and then use ssh to create a new TCP connection and a private tunnel to your instance.
To allow multiple connections to your instance using SSH and the open-tunnel command
1. Run the following command to start listening for new TCP connections on the specified port on your local machine. aws ec2-instance-connect open-tunnel \ --instance-id i-1234567890abcdef0 \ --local-port 8888 Expected output:
Listening for connections on port 8888.
2. In a new terminal window, run the following ssh command to create a new TCP connection and a private tunnel to your instance. ssh -i my-key-pair.pem ec2-user@localhost -p 8888

Expected output – In the first terminal window, you'll see the following:
[1] Accepted new tcp connection, opening websocket tunnel.
You might also see the following:
[1] Closing tcp connection.
#### Connect to your Linux instance with its instance ID using the AWS CLI If you only know your instance ID, you can use the ec2-instance-connect ssh AWS CLI command to connect to your instance using an SSH client. For more information, see Connect using the AWS CLI.
Prerequisites
- Install AWS CLI version 2 and configure it using your credentials. For more information, see Install or update to the latest version of the AWS CLI and Configure the AWS CLI in the AWS Command Line Interface User Guide.
- Alternatively, open AWS CloudShell and run AWS CLI commands in its pre-authenticated shell.
To connect to an instance using the instance ID and an EC2 Instance Connect Endpoint If you only know the instance ID, use the ec2-instance-connect ssh CLI command, and specify the ssh command, the instance ID, and the --connection-type parameter with the eice value to use an EC2 Instance Connect Endpoint. If the instance only has an IPv6 address, you must also include the --instance-ip parameter with the IPv6 address.
- If the instance has a private IPv4 address (it can also have an IPv6 address) use the following command and parameters: aws ec2-instance-connect ssh \ --instance-id i-1234567890example \ --os-user ec2-user \ --connection-type eice
- If the instance only has an IPv6 address, include the --instance-ip parameter with the IPv6 address:

aws ec2-instance-connect ssh \ --instance-id i-1234567890example \ --instance-ip 2001:db8::1234:5678:1.2.3.4 \ --os-user ec2-user \ --connection-type eice Tip If you get an error, make sure that you're using AWS CLI version 2. The ssh parameter is only available in AWS CLI version 2. For more information, see About AWS CLI version 2 in the AWS Command Line Interface User Guide.
#### Connect to your Windows instance using RDP You can use Remote Desktop Protocol (RDP) over EC2 Instance Connect Endpoint to connect to a Windows instance without a public IPv4 address or public DNS name.
To connect to your Windows instance using an RDP client
1. Complete Steps 1 – 8 in Connect to your Windows instance using RDP. After downloading the RDP desktop file at Step 8, you'll get an Unable to connect message, which is to be expected because your instance does not have a public IP address.
2. Run the following command to establish a private tunnel to the VPC in which the instance is located. --remote-port must be 3389 because RDP uses port 3389 by default. aws ec2-instance-connect open-tunnel \ --instance-id i-1234567890abcdef0 \ --remote-port 3389 \ --local-port any-port
3. In your Downloads folder, find the RDP desktop file that you downloaded, and drag it onto the RDP client window.
4. Right-click the RDP desktop file and choose Edit.
5. In the Edit PC window, for PC name (the instance to connect to), enter localhost:local- port, where local-port uses the same value as you specified in Step 2, and then choose Save.

Note that the following screenshot of the Edit PC window is from Microsoft Remote Desktop on a Mac. If you are using a Windows client, the window might be different.
6. In the RDP client, right-click the PC (that you just configured) and choose Connect to connect to your instance.
7. At the prompt, enter the decrypted password for the administrator account.

#### Troubleshoot Use the following information to help diagnose and fix issues that you might encounter when using EC2 Instance Connect Endpoint to connect an instance.
##### Can't connect to your instance The following are common reasons why you might not be able to connect to your instance.
- Security groups – Check the security groups assigned to the EC2 Instance Connect Endpoint and your instance. For more information about the required security group rules, see Security groups for EC2 Instance Connect Endpoint.
- Instance state – Verify that your instance is in the running state.
- Key pair – If the command you're using to connect requires a private key, verify that your instance has a public key and that you have the corresponding private key.
- IAM permissions – Verify that you have the required IAM permissions. For more information, see Grant permissions to use EC2 Instance Connect Endpoint.
For more troubleshooting tips for Linux instances, see Troubleshoot issues connecting to your Amazon EC2 Linux instance. For troubleshooting tips for Windows instances, see the section called "Windows instance RDP issues".
##### ErrorCode: AccessDeniedException If you receive an AccessDeniedException error, and the maxTunnelDuration condition is specified in the IAM policy, be sure to specify the --max-tunnel-duration parameter when connecting to an instance. For more information about this parameter, see open-tunnel in the AWS CLI Command Reference.
### Log connections established over EC2 Instance Connect Endpoint You can log resource operations and audit connections established over the EC2 Instance Connect Endpoint with AWS CloudTrail logs.
For more information about using AWS CloudTrail with Amazon EC2, see Log Amazon EC2 API calls using AWS CloudTrail.

#### Log EC2 Instance Connect Endpoint API calls with AWS CloudTrail EC2 Instance Connect Endpoint resource operations are logged to CloudTrail as management events. When the following API calls are made, the activity is recorded as a CloudTrail event in Event history:
- CreateInstanceConnectEndpoint
- DescribeInstanceConnectEndpoints
- DeleteInstanceConnectEndpoint You can view, search, and download recent events in your AWS account. For more information, see Viewing events with CloudTrail Event history in the AWS CloudTrail User Guide.
#### Use AWS CloudTrail to audit users who connect to an instance using EC2 Instance Connect Endpoint Endpoint Connection attempts to instances via EC2 Instance Connect Endpoint are logged in CloudTrail in Event history. When a connection to an instance is initiated through an EC2 Instance Connect Endpoint, the connection is logged as a CloudTrail management event with the eventName of OpenTunnel.
You can create Amazon EventBridge rules that route the CloudTrail event to a target. For more information, see the Amazon EventBridge User Guide.
The following is an example of an OpenTunnel management event that was logged in CloudTrail.
{ "eventVersion": "1.08", "userIdentity": { "type": "IAMUser", "principalId": "ABCDEFGONGNOMOOCB6XYTQEXAMPLE", "arn": "arn:aws:iam::1234567890120:user/IAM-friendly-name", "accountId": "123456789012", "accessKeyId": "ABCDEFGUKZHNAW4OSN2AEXAMPLE", "userName": "IAM-friendly-name"
     }, "eventTime": "2023-04-11T23:50:40Z", "eventSource": "ec2-instance-connect.amazonaws.com", "eventName": "OpenTunnel", "awsRegion": "us-east-1", "sourceIPAddress": "1.2.3.4",

     "userAgent": "aws-cli/1.15.61 Python/2.7.10 Darwin/16.7.0 botocore/1.10.60", "requestParameters": { "instanceConnectEndpointId": "eici-0123456789EXAMPLE", "maxTunnelDuration": "3600", "remotePort": "22", "privateIpAddress": "10.0.1.1"
     }, "responseElements": null, "requestID": "98deb2c6-3b3a-437c-a680-03c4207b6650", "eventID": "bbba272c-8777-43ad-91f6-c4ab1c7f96fd", "readOnly": false, "resources": [{ "accountId": "123456789012", "type": "AWS::EC2::InstanceConnectEndpoint", "ARN": "arn:aws:ec2:us-east-1:123456789012:instance-connect-endpoint/ eici-0123456789EXAMPLE"
     }], "eventType": "AwsApiCall", "managementEvent": true, "recipientAccountId": "123456789012", "eventCategory": "Management"
}
### Service-linked role for EC2 Instance Connect Endpoint Amazon EC2 uses AWS Identity and Access Management (IAM) service-linked roles. A service-linked role is a unique type of IAM role that is linked directly to Amazon EC2. Service-linked roles are predefined by Amazon EC2 and include all the permissions that Amazon EC2 requires to call other AWS services on your behalf. For more information, see Service-linked roles in the IAM User Guide.
Service-linked role permissions for EC2 Instance Connect Endpoint Amazon EC2 uses AWSServiceRoleForEC2InstanceConnect to create and manage network interfaces in your account that are required by EC2 Instance Connect Endpoint.
The AWSServiceRoleForEC2InstanceConnect service-linked role trusts the following service to assume the role:
- ec2-instance-connect.amazonaws.com The AWSServiceRoleForEC2InstanceConnect service-linked role uses the following managed policy:

- Ec2InstanceConnectEndpoint To view the permissions for the managed policy, see Ec2InstanceConnectEndpoint in the AWS Managed Policy Reference.
Create a service-linked role for EC2 Instance Connect Endpoint You don't need to manually create this service-linked role. When you create an EC2 Instance Connect Endpoint, Amazon EC2 creates the service-linked role for you.
Edit a service-linked role for EC2 Instance Connect Endpoint EC2 Instance Connect Endpoint doesn't allow you to edit the AWSServiceRoleForEC2InstanceConnect service-linked role.
Delete a service-linked role for EC2 Instance Connect Endpoint If you no longer need to use EC2 Instance Connect Endpoint, we recommend that you delete the AWSServiceRoleForEC2InstanceConnect service-linked role.
You must delete all EC2 Instance Connect Endpoint resources before you can delete the service- linked role.
To delete the service-linked role, see Delete a service-linked role in the IAM User Guide.
You must configure permissions to allow an IAM entity (a user, group, or role) to create, edit, or delete a service-linked role. For more information, see Service-linked role permissions in the IAM User Guide.
### Quotas for EC2 Instance Connect Endpoint Your AWS account has default quotas, formerly referred to as limits, for each AWS service. Unless otherwise noted, each quota is Region-specific.
Your AWS account has the following quotas related to EC2 Instance Connect Endpoint.
Name Default Adjustable Maximum number of EC2 Instance Connect Endpoints per AWS account per AWS Region 5 No
