# Troubleshoot an unreachable Amazon EC2 instance

Source: apps/user-manuals/aws/ec2-ug.pdf

---

## Terminated instance still displayed After you terminate an instance, it remains visible for a short while before being deleted. The state shows as terminated. If the entry is not deleted after several hours, contact Support.
## Error: The instance may not be terminated. Modify its 'disableApiTermination' instance attribute 'disableApiTermination' instance attribute If you try to terminate an instance and get the The instance i-1234567890abcdef0 may not be terminated. Modify its 'disableApiTermination' instance attribute error message, it indicates that the instance has been enabled for termination protection.
Termination protection prevents the instance from being accidentally terminated.
You must disable termination protection before you can terminate the instance.
For more information, see Change instance termination protection.
## Instances automatically launched or terminated Generally, the following behaviors mean that you've used Amazon EC2 Auto Scaling, EC2 Fleet, or Spot Fleet to scale your computing resources automatically based on criteria that you've defined:
- You terminate an instance and a new instance launches automatically.
- You launch an instance and one of your instances terminates automatically.
- You stop an instance and it terminates and a new instance launches automatically.
To stop automatic scaling, find the Auto Scaling group or the fleet that is launching the instances and either set its capacity to 0 or delete it.
# Troubleshoot an unreachable Amazon EC2 instance The following information can help you troubleshoot unreachable Amazon EC2 instances. You can capture screenshots or access console output to help diagnose problems and determine if you should reboot your instance. For unreachable Windows instances, troubleshoot by reviewing screenshots returned by the service.
Contents
- Instance reboot

- Instance console output
- Capture a screenshot of an unreachable instance
- Common screenshots to troubleshoot unreachable Windows instances
- Instance recovery when a host computer fails
- Instance appeared offline and unexpectedly rebooted
## Instance reboot The ability to reboot instances that are otherwise unreachable is valuable for both troubleshooting and general instance management.
Just as you can reset a computer by pressing the reset button, you can reset EC2 instances using the Amazon EC2 console, CLI, or API. For more information, see Reboot your Amazon EC2 instance.
## Instance console output Console output is a valuable tool for problem diagnosis. It is especially useful for troubleshooting kernel problems and service configuration issues that could cause an instance to terminate or become unreachable before its SSH daemon can be started.
- Linux instances – The instance console output displays the exact console output that would normally be displayed on a physical monitor attached to a computer. The console output returns buffered information that was posted shortly after an instance transition state (start, stop, reboot, and terminate). The posted output is not continuously updated; only when it is likely to be of the most value.
- Windows instances – The instance console output includes the last three system event log errors.
Only the instance owner can access the console output.
You can retrieve the latest serial console output during the instance lifecycle. This option is only supported on Nitro-based instances.
Console To get console output
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.

2. In the left navigation pane, choose Instances.
3. Select the instance.
4. Choose Actions, Monitor and troubleshoot, Get system log.
AWS CLI To get console output Use the get-console-output command. aws ec2 get-console-output --instance-id i-1234567890abcdef0 PowerShell To get console output Use the Get-EC2ConsoleOutput cmdlet.
Get-EC2ConsoleOutput -InstanceId i-1234567890abcdef0
## Capture a screenshot of an unreachable instance If you are unable to connect to your instance, you can capture a screenshot of your instance and view it as an image. The image can provide visibility as to the status of the instance, and allows for quicker troubleshooting.
You can generate screenshots while the instance is running or after it has crashed. The image is generated in JPG format and is no larger than 100 kb. There is no data transfer cost for the screenshot.
Limitations This feature is not supported for the following:
- Bare metal instances (instances of type *.metal)
- Instance is using an NVIDIA GRID driver
- Instances powered by Arm-based Graviton processors

- Windows instances on AWS Outposts
- Windows instances on AWS Local Zones Region support This feature is not available in the following Regions:
- Asia Pacific (Thailand)
- Mexico (Central)
- GovCloud Regions Console To get a screenshot of an instance
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the left navigation pane, choose Instances.
3. Select the instance to capture.
4. Choose Actions, Monitor and troubleshoot, Get instance screenshot.
5. Choose Download, or right-click the image to download and save it.
AWS CLI To capture a screenshot of an instance Use the get-console-screenshot command. The output is base64-encoded. aws ec2 get-console-screenshot --instance-id i-1234567890abcdef0 PowerShell To capture a screenshot of an instance Use the Get-EC2ConsoleScreenshot cmdlet. The output is base64-encoded.
Get-EC2ConsoleScreenshot -InstanceId i-1234567890abcdef0

## Common screenshots to troubleshoot unreachable Windows instances You can use the following information to help you troubleshoot an unreachable Windows instance based on screenshots returned by the service.
- Log on screen (Ctrl+Alt+Delete)
- Recovery console screen
- Windows boot manager screen
- Sysprep screen
- Getting ready screen
- Windows Update screen
- Chkdsk
### Log on screen (Ctrl+Alt+Delete)
Console Screenshot Service returned the following.
If an instance becomes unreachable during logon, there could be a problem with your network configuration or Windows Remote Desktop Services. An instance can also be unresponsive if a process is using large amounts of CPU.
#### Network configuration Use the following information to verify that your AWS, Microsoft Windows, and local (or on- premises) network configurations aren't blocking access to the instance.

AWS network configuration Configuration Verify Security group configuration Verify that port 3389 is open for your security group. Verify you are connecting to the right public IP address. If the instance was not associated with an Elastic IP, the public IP changes after the instance stops/starts. For more information, see Remote Desktop can't connect to the remote computer.
VPC configuration (Network ACLs)
Verify that the access control list (ACL) for your Amazon VPC is not blocking access. For information, see Network ACLs in the Amazon VPC User Guide.
VPN configuration If you are connecting to your VPC using a virtual private network (VPN), verify VPN tunnel connectivity. For more information, see Troubleshooting AWS Client VPN: Tunnel connectivity issues to a VPC.
Windows network configuration Configuration Verify Windows Firewall Verify that Windows Firewall isn't blocking connections to your instance. Disable Windows Firewall as described in bullet 7 of the remote desktop troubleshooting section, Remote Desktop can't connect to the remote computer.
Advanced TCP/IP configuration (Use of static IP)
The instance may be unresponsive because you configured a static IP address. For a VPC, create a network interface and attach it to the instance.

Local or on-premises network configuration Verify that a local network configuration isn't blocking access. Try to connect to another instance in the same VPC as your unreachable instance. If you can't access another instance, work with your local network administrator to determine whether a local policy is restricting access.
#### Remote Desktop Services issues If the instance can't be reached during logon, there could a problem with Remote Desktop Services (RDS) on the instance.
Tip You can use the AWSSupport-TroubleshootRDP runbook to check and modify various settings that might affect Remote Desktop Protocol (RDP) connections. For more information, see AWSSupport-TroubleshootRDP in the AWS Systems Manager Automation runbook reference.
Remote Desktop Services configuration Configuration Verify RDS is running Verify that RDS is running on the instance. Connect to the instance using the Microsoft Management Console (MMC)
Services snap-in (services.msc ). In the list of services, verify that Remote Desktop Services is Running. If it isn't, start it and then set the startup type to Automatic. If you can't connect to the instance by using the Services snap-in, detach the root volume from the instance, take a snapshot of the volume or create an AMI from it, attach the original volume to another instance in the same Availability Zone as a secondary volume, and modify the Start registry key. When you are finished, reattach the root volume to the original instance.
RDS is enabled Even if the service is started, it might be disabled. Detach the root volume from the instance, take a snapshot of the volume or create an AMI from it, attach the original volume to another instance in the same Availability Zone as a secondary volume,

Configuration Verify and enable the service by modifying the Terminal Server registry key as described in Enable Remote Desktop on an EC2 instance with remote registry.
When you are finished, reattach the root volume to the original instance.
#### High CPU usage Check the CPUUtilization (Maximum) metric on your instance by using Amazon CloudWatch. If CPUUtilization (Maximum) is a high number, wait for the CPU to go down and try connecting again. High CPU usage can be caused by:
- Windows Update
- Security Software Scan
- Custom Startup Script
- Task Scheduler For more information, see Get Statistics for a Specific Resource in the Amazon CloudWatch User Guide. For additional troubleshooting tips, see High CPU usage shortly after Windows starts (Windows instances only).
### Recovery console screen Console Screenshot Service returned the following.

The operating system might boot into the Recovery console and get stuck in this state if the bootstatuspolicy is not set to ignoreallfailures. Use the following procedure to change the bootstatuspolicy configuration to ignoreallfailures.
By default, the policy configuration for public Windows AMIs provided by AWS is set to ignoreallfailures.
1. Stop the unreachable instance.
2. Create a snapshot of the root volume. The root volume is attached to the instance as /dev/ sda1.
Detach the root volume from the unreachable instance, take a snapshot of the volume or create an AMI from it, and attach it to another instance in the same Availability Zone as a secondary volume.
Warning If your temporary instance and the original instance were launched using the same AMI, you must complete additional steps or you won't be able to boot the original instance after you restore its root volume because of a disk signature collision. If you must create a temporary instance using the same AMI, to avoid a disk signature collision, complete the steps in Disk signature collision.

Alternatively, select a different AMI for the temporary instance. For example, if the original instance uses an AMI for Windows Server 2016, launch the temporary instance using an AMI for Windows Server 2019.
3. Log in to the instance and run the following command from a command prompt to change the bootstatuspolicy configuration to ignoreallfailures. bcdedit /store Drive Letter:\boot\bcd /set {default} bootstatuspolicy ignoreallfailures
4. Reattach the volume to the unreachable instance and start the instance again.
### Windows boot manager screen Console Screenshot Service returned the following.
The operating system experienced a fatal corruption in the system file and/or the registry. When the instance is stuck in this state, you should recover the instance from a recent backup AMI or launch a replacement instance. If you need to access data on the instance, detach any root volumes from the unreachable instance, take a snapshot of those volume or create an AMI from them, and attach them to another instance in the same Availability Zone as a secondary volume.
### Sysprep screen Console Screenshot Service returned the following.

You may see this screen if you did not use the EC2Config Service to call Sysprep or if the operating system failed while running Sysprep. You can reset the password using EC2Rescue. Otherwise, see Create an Amazon EC2 AMI using Windows Sysprep.
### Getting ready screen Console Screenshot Service returned the following.

Refresh the Instance Console Screenshot Service repeatedly to verify that the progress ring is spinning. If the ring is spinning, wait for the operating system to start up. You can also check the CPUUtilization (Maximum) metric on your instance by using Amazon CloudWatch to see if the operating system is active. If the progress ring is not spinning, the instance may be stuck at the boot process. Reboot the instance. If rebooting does not solve the problem, recover the instance from a recent backup AMI or launch a replacement instance. If you need to access data on the instance, detach the root volume from the unreachable instance, take a snapshot of the volume or create an AMI from it. Then attach it to another instance in the same Availability Zone as a secondary volume.
### Windows Update screen Console Screenshot Service returned the following.

The Windows Update process is updating the registry. Wait for the update to finish. Do not reboot or stop the instance as this may cause data corruption during the update.
Note The Windows Update process can consume resources on the server during the update. If you experience this problem often, consider using faster instance types and faster EBS volumes.
### Chkdsk Console Screenshot Service returned the following.
Windows is running the chkdsk system tool on the drive to verify file system integrity and fix logical file system errors. Wait for process to complete.

## Instance recovery when a host computer fails If there is an unrecoverable issue with the hardware of an underlying host computer, AWS may schedule an instance stop event. You are notified of such an event ahead of time by email.
To recover an Amazon EBS-backed instance running on a host computer that failed
1. Back up any important data on your instance store volumes to Amazon EBS or Amazon S3.
2. Stop the instance.
3. Start the instance.
4. Restore any important data.
For more information, see Stop and start Amazon EC2 instances.
To recover an instance with an instance store root volume running on a host computer that failed
1. Create an AMI from the instance.
2. Upload the image to Amazon S3.
3. Back up important data to Amazon EBS or Amazon S3.
4. Terminate the instance.
5. Launch a new instance from the AMI.
6. Restore any important data to the new instance.
## Instance appeared offline and unexpectedly rebooted If your instance appears to have been offline and then unexpectedly rebooted, it might have undergone automatic instance recovery. This happens when AWS detects that the instance is unavailable due to an underlying hardware or software issue, and either simplified automatic recovery or CloudWatch action based recovery is enabled on the instance.
During the recovery process, AWS attempts to restore the instance's availability by migrating it to different hardware. To verify whether automatic instance recovery occurred for your instance, see Verify if automatic instance recovery occurred.
