# Troubleshoot Amazon EC2 instance stop issues

Source: apps/user-manuals/aws/ec2-ug.pdf

---

If your issue is not resolved and you continue receiving a launch failure error, you can decode the authorization failure message included in the error. The decoded message includes the permissions that are missing from the IAM policy. For more information, see How do I decode an authorization failure message after I receive an "UnauthorizedOperation" error during an EC2 instance launch?
## High CPU usage shortly after Windows starts (Windows instances only)
Note This troubleshooting tip is for Windows instances only.
If Windows Update is set to Check for updates but let me choose whether to download and install them (the default instance setting) this check can consume anywhere from 50 - 99% of the CPU on the instance. If this CPU consumption causes problems for your applications, you can manually change Windows Update settings in Control Panel or you can use the following script in the Amazon EC2 user data field: reg add "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\WindowsUpdate\Auto Update" /v AUOptions /t REG_DWORD /d 3 /f net stop wuauserv net start wuauserv When you run this script, specify a value for /d. The default value is 3. Possible values include the following:
1. Never check for updates
2. Check for updates but let me choose whether to download and install them
3. Download updates but let me choose whether to install them
4. Install updates automatically After you modify the user data for your instance, you can run it. For more information, see Run commands on your Windows instance at launch.
# Troubleshoot Amazon EC2 instance stop issues If your Amazon EBS-backed instance appears stuck in the stopping state, the issue might be with the underlying host computer.

To resolve the issue, follow these steps:
1. Force stop the instance Use the Amazon EC2 console or the AWS CLI to force stop the instance. For the steps, see Force stop an instance.
The instance will first attempt a graceful shutdown, which includes flushing file system caches and metadata (although you can optionally bypass the graceful shutdown). If the graceful shutdown fails to complete within the timeout period, the instance shuts down forcibly without flushing the file system caches and metadata.
2. After force stop Perform file system check and repair procedures.
Important Performing these procedures is crucial because a forced stop prevents flushing of file system caches and metadata.
3. If force stop fails If, after 10 minutes, the instance has not stopped, do the following: a.
Post a request for help on AWS re:Post. To help expedite a resolution, include the instance ID, and describe the steps that you've already taken. b.
Alternatively, if you have a support plan, create a technical support case in the Support Center. c.
While waiting for assistance, you can create a replacement instance if needed. For the steps, see (Optional) Create a replacement instance.
There is no cost for instance usage while an instance is in the stopping state or in any other state except running. You are only charged for instance usage when an instance is in the running state.
Contents
- Force stop an instance
- (Optional) Create a replacement instance

## Force stop an instance You can force an instance to stop. If, after 10 minutes, the instance has not stopped, post a request for help on AWS re:Post. To help expedite a resolution, include the instance ID, and describe the steps that you've already taken. Alternatively, if you have a support plan, create a technical support case in the Support Center.
Note Using the console, you can force an instance to stop while the instance is in the stopping state only. Using the AWS CLI, you can force an instance to stop while the instance is in the pending, running, or stopping state.
Console To force stop an instance
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Instances and select the stuck instance.
3. Choose Instance state, Force stop instance.
Note that Force stop instance is only available in the console if your instance is in the stopping state. If your instance is in another state (except shutting-down and terminated) you can use the AWS CLI to force stop your instance.
4. (Optional) To bypass the graceful OS shutdown during the force stop, select the Skip OS shutdown checkbox.
5. Choose Force stop.
AWS CLI To force stop an instance Use the stop-instances command with the --force option. aws ec2 stop-instances \ --instance-ids i-1234567890abcdef0 \ --force

To bypass the graceful OS shutdown during force stop, include the --skip-os-shutdown option. aws ec2 stop-instances \ --instance-ids i-1234567890abcdef0 \ --force \ --skip-os-shutdown PowerShell To force stop an instance Use the Stop-EC2Instance cmdlet and set -Enforce to true.
Stop-EC2Instance `
    -InstanceId i-1234567890abcdef0 `
    -Enforce $true To bypass the graceful OS shutdown during force stop, include -SkipOsShutdown $true.
Stop-EC2Instance `
    -InstanceId i-1234567890abcdef0 `
    -Enforce $true `
    -SkipOsShutdown $true
## (Optional) Create a replacement instance While you are waiting for assistance from AWS re:Post or the Support Center, you can create a replacement instance if needed. Create an AMI from the stuck instance, and launch a new instance using the new AMI.
Important You can create a replacement instance if the stuck instance produces system status checks only, as instance status checks will result in the AMI copying over an exact replica of the broken operating system. After you've confirmed the status message, create the AMI and launch a new instance using the new AMI.

Console To create a replacement instance
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Instances and select the stuck instance.
3. Choose Actions, Image and templates, Create image.
4. On the Create image page, do the following: a.
Enter a name and description for the AMI. b.
Clear Reboot instance. c.
Choose Create image.
For more information, see the section called "Create an AMI from an instance".
5. Launch a new instance from the AMI and verify that the new instance is working.
6. Select the stuck instance, and choose Actions, Instance state, Terminate (delete) instance.
If the instance also gets stuck terminating, Amazon EC2 automatically forces it to terminate within a few hours.
If you are unable to create an AMI from the instance as described in the previous procedure, you can set up a replacement instance as follows:
(Alternate) To create a replacement instance using the console
1. Select the instance and choose Description, Block devices. Select each volume and make note of its volume ID. Be sure to note which volume is the root volume.
2. In the navigation pane, choose Volumes. Select each volume for the instance, and choose Actions, Create Snapshot.
3. In the navigation pane, choose Snapshots. Select the snapshot that you just created, and choose Actions, Create Volume.
4. Launch an instance with the same operating system as the stuck instance. Note the volume ID and device name of its root volume.
5. In the navigation pane, choose Instances, select the instance that you just launched, and choose Instance state, Stop instance.

6. In the navigation pane, choose Volumes, select the root volume of the stopped instance, and choose Actions, Detach Volume.
7. Select the root volume that you created from the stuck instance, choose Actions, Attach Volume, and attach it to the new instance as its root volume (using the device name that you made note of). Attach any additional non-root volumes to the instance.
8. In the navigation pane, choose Instances and select the replacement instance. Choose Instance state, Start instance. Verify that the instance is working.
9. Select the stuck instance, choose Instance state, Terminate (delete) instance. If the instance also gets stuck terminating, Amazon EC2 automatically forces it to terminate within a few hours.
AWS CLI To create a replacement instance
1. Create an AMI from the stuck instance using the create-image command with the --no- reboot option. aws ec2 create-image \ --instance-id i-1234567890abcdef0 \ --name "my-replacement-ami" \ --description ""AMI for replacement instance" \ --no-reboot
2. Launch a new instance from the AMI that you just created, using the run-instances command.
3. Verify that the new instance is working.
4. (Optional) Terminate the stuck instance using the terminate-instances command. aws ec2 terminate-instances --instance-ids i-1234567890abcdef0 PowerShell To create a replacement instance
1. Create an AMI from the stuck instance using the New-EC2Image cmdlet and set - NoReboot to true.
