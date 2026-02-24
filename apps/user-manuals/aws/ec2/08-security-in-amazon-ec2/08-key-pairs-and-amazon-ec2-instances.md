# Amazon EC2 key pairs and Amazon EC2 instances

Source: apps/user-manuals/aws/ec2-ug.pdf

---

Microsoft provides several options for managing Windows OS and application changes. SCCM, for example, provides full lifecycle coverage of environment modifications. Select tools that address business requirements and control how changes will affect application SLAs, capacity, security, and disaster recovery procedures. Avoid manual changes and instead leverage automated configuration management software or command line tools such as the EC2 Run Command or Windows PowerShell to implement scripted, repeatable change processes. To assist with this requirement, use bastion hosts with enhanced logging for all interactions with your Windows instances to ensure that all events and tasks are automatically recorded.
## Audit and accountability for Amazon EC2 Windows instances AWS CloudTrail, AWS Config, and AWS Config Rules provide audit and change tracking features for auditing AWS resource changes. Configure Windows event logs to send local log files to a centralized log management system to preserve log data for security and operational behavior analysis. Microsoft System Center Operations Manager (SCOM) aggregates information about Microsoft applications deployed to Windows instances and applies preconfigured and custom rulesets based on application roles and services. System Center Management Packs build on SCOM to provide application-specific monitoring and configuration guidance. These Management Packs support Windows Server Active Directory, SharePoint Server 2013, Exchange Server 2013, Lync Server 2013, SQL Server 2014, and many more servers and technologies.
In addition to Microsoft systems management tools, customers can use Amazon CloudWatch to monitor instance CPU utilization, disk performance, network I/O, and perform host and instance status checks. The EC2Config, EC2Launch, and EC2Launch v2 launch agents provide access to additional, advanced features for Windows instances. For example, they can export Windows system, security, application, and Internet Information Services (IIS) logs to CloudWatch Logs which can then be integrated with Amazon CloudWatch metrics and alarms. Customers can also create scripts that export Windows performance counters to Amazon CloudWatch custom metrics.
# Amazon EC2 key pairs and Amazon EC2 instances A key pair, consisting of a public key and a private key, is a set of security credentials that you use to prove your identity when connecting to an Amazon EC2 instance. For Linux instances, the private key allows you to securely SSH into your instance. For Windows instances, the private key is required to decrypt the administrator password, which you then use to connect to your instance.

Amazon EC2 stores the public key on your instance, and you store the private key, as shown in the following diagram. It's important that you store your private key in a secure place because anyone who possesses your private key can connect to your instances that use the key pair.
When you launch an instance, you can specify a key pair, so that you can connect to your instance using a method that requires a key pair. Depending on how you manage your security, you can specify the same key pair for all your instances or you can specify different key pairs.
For Linux instances, when your instance boots for the first time, the public key that you specified at launch is placed on your Linux instance in an entry within ~/.ssh/authorized_keys. When you connect to your Linux instance using SSH, to log in you must specify the private key that corresponds to the public key.
For more information about connecting to your EC2 instance, see Connect to your EC2 instance.
Important Because Amazon EC2 doesn't keep a copy of your private key, there is no way to recover a private key if you lose it. However, there can still be a way to connect to instances for which you've lost the private key. For more information, see I've lost my private key. How can I connect to my instance?

As an alternative to key pairs, you can use AWS Systems Manager Session Manager to connect to your instance with an interactive one-click browser-based shell or the AWS Command Line Interface (AWS CLI).
Contents
- Create a key pair for your Amazon EC2 instance
- Describe your key pairs
- Delete your key pair
- Add or replace a public key on your Linux instance
- Verify the fingerprint of your key pair
## Create a key pair for your Amazon EC2 instance You can use Amazon EC2 to create your key pairs, or you can use a third-party tool to create your key pairs, and then import them to Amazon EC2.
Amazon EC2 supports 2048-bit SSH-2 RSA keys for Linux and Windows instances. Amazon EC2 also supports ED25519 keys for Linux instances.
For instructions on how to connect to your instance after you have created a key pair, see the section called "Connect to your Linux instance using SSH" and the section called "Connect to your Windows instance using RDP".
Contents
- Create a key pair using Amazon EC2
- Create a key pair using AWS CloudFormation
- Create a key pair using a third-party tool and import the public key to Amazon EC2
### Create a key pair using Amazon EC2 When you create a key pair using Amazon EC2, the public key is stored in Amazon EC2, and you store the private key.
You can create up to 5,000 key pairs per Region. To request an increase, create a support case. For more information, see Creating a support case in the Support User Guide.

Console To create a key pair using Amazon EC2
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, under Network & Security, choose Key Pairs.
3. Choose Create key pair.
4. For Name, enter a descriptive name for the key pair. Amazon EC2 associates the public key with the name that you specify as the key name. A key name can include up to 255 ASCII characters. It can't include leading or trailing spaces.
5. Select a key pair type appropriate for your operating system:
(Linux instances) For Key pair type, choose either RSA or ED25519.
(Windows instances) For Key pair type, choose RSA. ED25519 keys are not supported for Windows instances.
6. For Private key file format, choose the format in which to save the private key. To save the private key in a format that can be used with OpenSSH, choose pem. To save the private key in a format that can be used with PuTTY, choose ppk.
7. To add a tag to the public key, choose Add tag, and enter the key and value for the tag.
Repeat for each tag.
8. Choose Create key pair.
9. The private key file is automatically downloaded by your browser. The base file name is the name that you specified as the name of your key pair, and the file name extension is determined by the file format that you chose. Save the private key file in a safe place.
Important This is the only chance for you to save the private key file.
10. If you plan to use an SSH client on a macOS or Linux computer to connect to your Linux instance, use the following command to set the permissions of your private key file so that only you can read it. chmod 400 key-pair-name.pem

If you do not set these permissions, then you cannot connect to your instance using this key pair. For more information, see Error: Unprotected private key file.
AWS CLI To create a key pair using Amazon EC2
1. Use the create-key-pair command as follows to generate the key pair and to save the private key to a .pem file. The --query option prints the private key material to the output. The --output option saves the private key material in the specified file. The extension should be either .pem or .ppk, depending on the key format. The private key name can be different from the public key name, but for ease of use, use the same name. aws ec2 create-key-pair \ --key-name my-key-pair \ --key-type rsa \ --key-format pem \ --query "KeyMaterial" \ --output text > my-key-pair.pem
2. If you plan to use an SSH client on a macOS or Linux computer to connect to your Linux instance, use the following command to set the permissions of your private key file so that only you can read it. chmod 400 key-pair-name.pem If you do not set these permissions, then you cannot connect to your instance using this key pair. For more information, see Error: Unprotected private key file.
PowerShell To create a key pair using Amazon EC2 Use the New-EC2KeyPair cmdlet as follows to generate the key and save it to a .pem or .ppk file. The Out-File cmdlet saves the private key material in a file with the specified extension.
The extension should be either .pem or .ppk, depending on the key format. The private key name can be different from the public key name, but for ease of use, use the same name.

(New-EC2KeyPair `
    -KeyName "my-key-pair" `
    -KeyType "rsa" `
    -KeyFormat "pem").KeyMaterial | Out-File -Encoding ascii -FilePath C:\path\my- key-pair.pem
### Create a key pair using AWS CloudFormation When you create a new key pair using CloudFormation, the private key is saved to AWS Systems Manager Parameter Store. The parameter name has the following format:
/ec2/keypair/key_pair_id For more information, see AWS Systems Manager Parameter Store in the AWS Systems Manager User Guide.
To create a key pair using CloudFormation
1. Specify the AWS::EC2::KeyPair resource in your template.
Resources:
  NewKeyPair:
    Type: 'AWS::EC2::KeyPair'
    Properties:
      KeyName: new-key-pair
2. Use the describe-key-pairs command as follows to get the ID of the key pair. aws ec2 describe-key-pairs --filters Name=key-name,Values=new-key-pair --query KeyPairs[*].KeyPairId --output text The following is example output. key-05abb699beEXAMPLE
3. Use the get-parameter command as follows to get the parameter for your key and save the key material in a .pem file.

aws ssm get-parameter --name /ec2/keypair/key-05abb699beEXAMPLE --with-decryption --query Parameter.Value --output text > new-key-pair.pem Required IAM permissions To enable CloudFormation to manage Parameter Store parameters on your behalf, the IAM role assumed by CloudFormation or your user must have the following permissions:
- ssm:PutParameter – Grants permission to create a parameter for the private key material.
- ssm:DeleteParameter – Grants permission to delete the parameter that stored the private key material. This permission is required whether the key pair was imported or created by CloudFormation.
When CloudFormation deletes a key pair that was created or imported by a stack, it performs a permissions check to determine whether you have permission to delete parameters, even though CloudFormation creates a parameter only when it creates a key pair, not when it imports a key pair.
CloudFormation tests for the required permission using a fabricated parameter name that does not match any parameter in your account. Therefore, you might see a fabricated parameter name in the AccessDeniedException error message.
### Create a key pair using a third-party tool and import the public key to Amazon EC2 EC2 Instead of using Amazon EC2 to create a key pair, you can create an RSA or ED25519 key pair by using a third-party tool and then import the public key to Amazon EC2.
Requirements for key pairs
- Supported types:
- (Linux and Windows) RSA
- (Linux only) ED25519 Note ED25519 keys are not supported for Windows instances.
- Amazon EC2 does not accept DSA keys.

- Supported formats:
- OpenSSH public key format (for Linux, the format in ~/.ssh/authorized_keys)
- (Linux only) If you connect using SSH while using the EC2 Instance Connect API, the SSH2 format is also supported.
- SSH private key file format must be PEM or PPK
- (RSA only) Base64 encoded DER format
- (RSA only) SSH public key file format as specified in RFC 4716
- Supported lengths:
- 1024, 2048, and 4096.
- (Linux only) If you connect using SSH while using the EC2 Instance Connect API, the supported lengths are 2048 and 4096.
To create a key pair using a third-party tool
1. Generate a key pair with a third-party tool of your choice. For example, you can use ssh- keygen (a tool provided with the standard OpenSSH installation). Alternatively, Java, Ruby, Python, and many other programming languages provide standard libraries that you can use to create a key pair.
Important The private key must be in the PEM or PPK format. For example, use ssh-keygen -m PEM to generate the OpenSSH key in the PEM format.
2. Save the public key to a local file. For example, ~/.ssh/my-key-pair.pub (Linux, macOS) or C:\keys\my-key-pair.pub (Windows). The file name extension for this file is not important.
3. Save the private key to a local file that has the .pem or .ppk extension. For example, ~/.ssh/ my-key-pair.pem or ~/.ssh/my-key-pair.ppk (Linux, macOS) or C:\keys\my-key- pair.pem or C:\keys\my-key-pair.ppk (Windows). The file extension is important because, depending on the tool you use to connect to your instance, you'll need a specific file format. OpenSSH requires a .pem file, while PuTTY requires a .ppk file.

Important Save the private key file in a safe place. You'll need to provide the name of your public key when you launch an instance, and the corresponding private key each time you connect to the instance.
After you have created the key pair, use one of the following methods to import your public key to Amazon EC2.
Console To import the public key to Amazon EC2
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Key Pairs.
3. Choose Import key pair.
4. For Name, enter a descriptive name for the public key. The name can include up to 255 ASCII characters. It can't include leading or trailing spaces.
Note When you connect to your instance from the EC2 console, the console suggests this name for the name of your private key file.
5. Either choose Browse to navigate to and select your public key, or paste the contents of your public key into the Public key contents field.
6. Choose Import key pair.
7. Verify that the public key that you imported appears in the list of key pairs.
AWS CLI To import the public key to Amazon EC2 Use the import-key-pair command. aws ec2 import-key-pair \

    --key-name my-key-pair \ --public-key-material fileb://path/my-key-pair.pub To verify that the key pair was imported successfully Use the describe-key-pairs command. aws ec2 describe-key-pairs --key-names my-key-pair PowerShell To import the public key to Amazon EC2 Use the Import-EC2KeyPair cmdlet.
$publickey=[Io.File]::ReadAllText("C:\Users\TestUser\.ssh\id_rsa.pub")
Import-EC2KeyPair `
    -KeyName my-key-pair `
    -PublicKey $publickey To verify that the key pair was imported successfully Use the Get-EC2KeyPair cmdlet.
Get-EC2KeyPair -KeyName my-key-pair
## Describe your key pairs You can describe the key pairs that you stored in Amazon EC2. You can also retrieve the public key material and identify the public key that was specified at launch.
Tasks
- Describe your key pairs
- Retrieve the public key material
- Identify the public key specified at launch

### Describe your key pairs You can view the following information about your public keys that are stored in Amazon EC2: public key name, ID, key type, fingerprint, public key material, the date and time (in the UTC time zone) the key was created by Amazon EC2 (if the key was created by a third-party tool, then it's the date and time the key was imported to Amazon EC2), and any tags that are associated with the public key.
Console To view information about your key pairs
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the left navigator, choose Key Pairs.
3. You can view the information about each public key in the Key pairs table.
4. To view a public key's tags, select the checkbox next to the key, and then choose Actions, Manage tags.
AWS CLI To view information about a key pair Use the describe-key-pairs command. aws ec2 describe-key-pairs --key-names key-pair-name PowerShell To view information about a key pair Use the Get-EC2KeyPair cmdlet.
Get-EC2KeyPair -KeyName key-pair-name

### Retrieve the public key material You can get the public key material for your key pairs. The following is an example public key. Note that there are line breaks added for readability. ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQClKsfkNkuSevGj3eYhCe53pcjqP3maAhDFcvBS7O6V hz2ItxCih+PnDSUaw+WNQn/mZphTk/a/gU8jEzoOWbkM4yxyb/wB96xbiFveSFJuOp/d6RJhJOI0iBXr lsLnBItntckiJ7FbtxJMXLvvwJryDUilBMTjYtwB+QhYXUMOzce5Pjz5/i8SeJtjnV3iAoG/cQk+0FzZ qaeJAAHco+CY/5WrUBkrHmFJr6HcXkvJdWPkYQS3xqC0+FmUZofz221CBt5IMucxXPkX4rWi+z7wB3Rb BQoQzd8v7yeb7OzlPnWOyN0qFU0XA246RA8QFYiCNYwI3f05p6KLxEXAMPLE Private key To retrieve the public key material using ssh-keygen (Linux)
On your local Linux or macOS computer, use the ssh-keygen command. Specify the path where you downloaded your private key (the .pem file). ssh-keygen -y -f /path_to_key_pair/my-key-pair.pem If this ssh-keygen command fails, run the following chmod command to ensure that the private key file has the required permissions. chmod 400 key-pair-name.pem To retrieve the public key material using PuTTYgen (Windows)
On your local Windows computer, start PuTTYgen. Choose Load. Select the .ppk or .pem private key file. PuTTYgen displays the public key under Public key for pasting into OpenSSH authorized_keys file. You can also view the public key by choosing Save public key, specifying a name for the file, saving the file, and then opening the file.
AWS CLI To retrieve the public key material Use the following describe-key-pairs command and specify the --include-public-key option. aws ec2 describe-key-pairs \ --key-names key-pair-name \

    --include-public-key \ --query "KeyPairs[].PublicKey"
PowerShell To retrieve the public key material Use the Get-EC2KeyPair cmdlet.
(Get-EC2KeyPair -KeyName key-pair-name -IncludePublicKey $true).PublicKey IMDSv2 Linux Run the following commands from your Linux instance.
TOKEN=`curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata- token-ttl-seconds: 21600"` \ && curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta- data/public-keys/0/openssh-key Windows Run the following cmdlets from your Windows instance.
[string]$token = Invoke-RestMethod -Headers @{"X-aws-ec2-metadata-token-ttl-seconds"
 = "21600"} -Method PUT -Uri http://169.254.169.254/latest/api/token Invoke-RestMethod -Headers @{"X-aws-ec2-metadata-token" = $token} -Method GET -Uri http://169.254.169.254/latest/meta-data/public-keys/0/openssh-key IMDSv1 Linux Run the following command from your Linux instance. curl http://169.254.169.254/latest/meta-data/public-keys/0/openssh-key Windows

Run the following cmdlet from your Windows instance.
Invoke-RestMethod -uri  http://169.254.169.254/latest/meta-data/public-keys/0/ openssh-key
### Identify the public key specified at launch If you specify a public key when you launch an instance, the public key name is recorded by the instance. The public key name reported for an instance does not change, even if you change the public key on the instance or add public keys.
Console To identify the public key specified at instance launch
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Instances.
3. Select the instance.
4. On the Details tab, under Instance details, find Key pair assigned at launch.
AWS CLI To identify the public key specified at instance launch Use the following describe-instances command. aws ec2 describe-instances \ --instance-id i-1234567890abcdef0 \ --query "Reservations[].Instances[].KeyName" \ --output text The following is example output. key-pair-name PowerShell To identify the public key specified at instance launch

Use the Get-EC2Instance cmdlet.
(Get-EC2Instance -InstanceId i-1234567890abcdef0).Instances | Select KeyName The following is example output.
KeyName
------- key-pair-name
## Delete your key pair You can delete a key pair, which removes the public key that is stored in Amazon EC2. Deleting a key pair does not delete the matching private key.
When you delete a public key using the following methods, you're only deleting the public key that you stored in Amazon EC2 when you created or imported the key pair. Deleting a public key doesn't remove the public key from any instances to which you've added it, either when you launched the instance or later. It also doesn't delete the private key on your local computer. You can continue to connect to instances that you launched using a public key that you've deleted from Amazon EC2 as long as you still have the private key (.pem) file.
Important If you're using an Auto Scaling group (for example, in an Elastic Beanstalk environment), ensure that the public key you're deleting is not specified in an associated launch template or launch configuration. If Amazon EC2 Auto Scaling detects an unhealthy instance, it launches a replacement instance. However, the instance launch fails if the public key cannot be found. For more information, see Launch templates in the Amazon EC2 Auto Scaling User Guide.
Console To delete your public key on Amazon EC2
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Key Pairs.

3. Select the key pair to delete and choose Actions, Delete.
4. In the confirmation field, enter Delete and then choose Delete.
AWS CLI To delete your public key on Amazon EC2 Use the delete-key-pair command. aws ec2 delete-key-pair --key-name my-key-pair PowerShell To delete your public key on Amazon EC2 Use the Remove-EC2KeyPair cmdlet.
Remove-EC2KeyPair -KeyName my-key-pair
## Add or replace a public key on your Linux instance If you lose a private key, you lose access to any instances that use the key pair. For more information about connecting to an instance using a different key pair than the one that you specified at launch, see I've lost my private key.
When you launch an instance, you can specify a key pair. If you specify a key pair at launch, when your instance boots for the first time, the public key material is placed on your Linux instance in an entry within ~/.ssh/authorized_keys. When you first connect to your Linux instance using SSH, you specify the default user and the private key that corresponds to the public key that is stored on your Linux instance.
After you connect to your instance, you can change the key pair that is used to access the default system account of your instance by adding a new public key on the instance, or by replacing the public key (deleting the existing public key and adding a new one) on the instance. You can also remove all public keys from an instance.
You might add or replace a key pair for the following reasons:

- If a user in your organization requires access to the system user using a separate key pair, you can add the public key to your instance.
- If someone has a copy of the private key (.pem file) and you want to prevent them from connecting to your instance (for example, if they've left your organization), you can delete the public key on the instance and replace it with a new one.
- If you create a Linux AMI from an instance, the public key material is copied from the instance to the AMI. If you launch an instance from the AMI, the new instance includes the public key from the original instance. To prevent someone who has the private key from connecting to the new instance, you can remove the public key from the original instance before creating the AMI.
Use the following procedures to modify the key pair for the default user, such as ec2-user. For information about adding users to your instance, see the documentation for the operating system on your instance.
To add or replace a key pair
1. Create a new key pair using the Amazon EC2 console or a third-party tool.
2. Retrieve the public key from your new key pair. For more information, see Retrieve the public key material.
3. Connect to your instance.
4. On the instance, using the text editor of your choice, open the .ssh/authorized_keys file.
Paste the public key information from your new key pair underneath the existing public key information and then save the file.
5. Disconnect from your instance. Test that you can connect to your instance using the private key file from the new key pair.
6. If you're using Auto Scaling, EC2 fleet, or a launch template to launch your instances, check whether the key pair that you're replacing is specified in your launch template or launch configuration. Otherwise, instance launches will fail.
7. (Optional) If you're replacing an existing key pair, connect to your instance and delete the public key information for the original key pair from the .ssh/authorized_keys file.
To remove a public key from an instance
1. Connect to your instance.

2. Using a text editor of your choice, open the .ssh/authorized_keys file on the instance.
Delete the public key information, and then save the file.
Warning If you remove all the public keys from an instance and disconnect from the instance, you can't connect to the instance again unless you've configured an alternate way to log in.
## Verify the fingerprint of your key pair To verify the fingerprint of your key pair, compare the fingerprint displayed on the Key pairs page in the Amazon EC2 console, or returned by the describe-key-pairs command, with the fingerprint that you generate using the private key on your local computer. These fingerprints should match.
When Amazon EC2 calculates a fingerprint, Amazon EC2 might append padding to the fingerprint with = characters. Other tools, such as ssh-keygen, might omit this padding.
If you're trying to verify the fingerprint of your Linux EC2 instance, not the fingerprint of your key pair, see Get the instance fingerprint.
### How the fingerprints are calculated Amazon EC2 uses different hash functions to calculate the fingerprints for RSA and ED25519 key pairs. Furthermore, for RSA key pairs, Amazon EC2 calculates the fingerprints differently using different hash functions depending on whether the key pair was created by Amazon EC2 or imported to Amazon EC2.
The following table lists the hash functions that are used to calculate the fingerprints for RSA and ED25519 key pairs that are created by Amazon EC2 and imported to Amazon EC2.
(Linux instances) Hash functions used to calculate fingerprints Key pair source RSA key pairs (Windows and Linux)
ED25519 key pairs (Linux)
Created by Amazon EC2 SHA-1 SHA-256 Imported to Amazon EC2 MD5¹ SHA-256

¹ If you import a public RSA key to Amazon EC2, the fingerprint is calculated using an MD5 hash function. This is true regardless of how you created the key pair, for example, by using a third-party tool or by generating a new public key from an existing private key created using Amazon EC2.
### When using the same key pair in different Regions If you plan to use the same key pair to connect to instances in different AWS Regions, you must import the public key to all of the Regions in which you'll use it. If you use Amazon EC2 to create the key pair, you can Retrieve the public key material so that you can import the public key to the other Regions.
Note
- If you create an RSA key pair using Amazon EC2, and then you generate a public key from the Amazon EC2 private key, the imported public keys will have a different fingerprint than the original public key. This is because the fingerprint of the original RSA key created using Amazon EC2 is calculated using a SHA-1 hash function, while the fingerprint of the imported RSA keys is calculated using an MD5 hash function.
- For ED25519 key pairs, the fingerprints will be same regardless of whether they're created by Amazon EC2 or imported to Amazon EC2, because the same SHA-256 hash function is used to calculate the fingerprint.
### Generate a fingerprint from the private key Use one of the following commands to generate a fingerprint from the private key on your local machine.
If you're using a Windows local machine, you can run the following commands using the Windows Subsystem for Linux (WSL). Install the WSL and a Linux distribution using the instructions in the How to install Linux on Windows with WSL. The example in the instructions installs the Ubuntu distribution of Linux, but you can install any distribution. You are prompted to restart your computer for the changes to take effect.
- If you created the key pair using Amazon EC2 Use the OpenSSL tools to generate a fingerprint as shown in the following examples.
For RSA key pairs:
