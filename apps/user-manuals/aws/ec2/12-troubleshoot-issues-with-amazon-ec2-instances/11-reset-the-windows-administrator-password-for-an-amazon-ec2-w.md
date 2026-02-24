# Reset the Windows administrator password for an Amazon EC2 Windows instance

Source: apps/user-manuals/aws/ec2-ug.pdf

---

diskpart
8. Run the select disk DiskPart command and specify the disk number for the volume with the disk signature collision.
Tip To check the disk number for the volume with the disk signature collision, use the Disk Management utility. Open a command prompt, type compmgmt.msc and press Enter. In the left-hand navigation panel, double-click Disk Management. In the Disk Management utility, check the disk number for the offline volume with the disk signature collision.
DISKPART> select disk 1 Disk 1 is now the selected disk.
9. Run the following DiskPart command to get the disk signature.
DISKPART>  uniqueid disk Disk ID: 0C764FA8
10. If the disk signature shown in the previous step doesn't match the disk signature that you wrote down earlier, use the following DiskPart command to change the disk signature so that it matches:
DISKPART> uniqueid disk id=E9EB3AA5
# Reset the Windows administrator password for an Amazon EC2 Windows instance Windows instance If you are no longer able to connect to your Amazon EC2 Windows instance because the Windows administrator password is lost or expired, you can reset the password.

Note There is an AWS Systems Manager Automation document that automatically applies the manual steps necessary to reset the local administrator password. For more information, see Reset passwords and SSH keys on EC2 instances in the AWS Systems Manager User Guide.
The manual methods to reset the administrator password use EC2Launch v2, EC2Config, or EC2Launch.
- For all supported Windows AMIs that include the EC2Launch v2 agent, use EC2Launch v2.
- For Windows AMIs before Windows Server 2016, use the EC2Config service.
- For Windows Server 2016 and later AMIs, use the EC2Launch service.
These procedures also describe how to connect to an instance if you lost the key pair that was used to create the instance. Amazon EC2 uses a public key to encrypt a piece of data, such as a password, and a private key to decrypt the data. The public and private keys are known as a key pair. With Windows instances, you use a key pair to obtain the administrator password and then log in using RDP.
Note If you have disabled the local administrator account on the instance and your instance is configured for Systems Manager, you can also re-enable and reset your local administrator password by using EC2Rescue and Run Command. For more information, see Use EC2Rescue for Windows Server with Systems Manager Run Command.
Contents
- Reset Windows admin password for EC2 instance using EC2Launch v2
- Reset Windows admin password for EC2 instance using EC2Launch
- Reset Windows admin password for EC2 instance using EC2Config

## Reset Windows admin password for EC2 instance using EC2Launch v2 If you have lost your Windows administrator password and are using a supported Windows AMI that includes the EC2Launch v2 agent, you can use EC2Launch v2 to generate a new password.
If you are using a Windows Server 2016 or later AMI that does not include the EC2Launch v2 agent, see Reset Windows admin password for EC2 instance using EC2Launch.
If you are using a Windows Server AMI earlier than Windows Server 2016 that does not include the EC2Launch v2 agent, see Reset Windows admin password for EC2 instance using EC2Config.
Note If you have disabled the local administrator account on the instance and your instance is configured for Systems Manager, you can also re-enable and reset your local administrator password by using EC2Rescue and Run Command. For more information, see Use EC2Rescue for Windows Server with Systems Manager Run Command.
Note There is an AWS Systems Manager Automation document that automatically applies the manual steps necessary to reset the local administrator password. For more information, see Reset passwords and SSH keys on EC2 instances in the AWS Systems Manager User Guide.
To reset your Windows administrator password using EC2Launch v2, you need to do the following:
- Step 1: Verify that the EC2Launch v2 agent is running
- Step 2: Detach the root volume from the instance
- Step 3: Attach the volume to a temporary instance
- Step 4: Delete the .run-once file
- Step 5: Restart the original instance

### Step 1: Verify that the EC2Launch v2 agent is running Before you attempt to reset the administrator password, verify that the EC2Launch v2 agent is installed and running. You use the EC2Launch v2 agent to reset the administrator password later in this section.
To verify that the EC2Launch v2 agent is running
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Instances and then select the instance that requires a password reset. This instance is referred to as the original instance in this procedure.
3. Choose Actions, Monitor and troubleshoot, Get system log.
4. Locate the EC2 Launch entry, for example, Launch: EC2Launch v2 service v2.0.124. If you see this entry, the EC2Launch v2 service is running.
If the system log output is empty, or if the EC2Launch v2 agent is not running, troubleshoot the instance using the Instance Console Screenshot service. For more information, see Capture a screenshot of an unreachable instance.
### Step 2: Detach the root volume from the instance You can't use EC2Launch v2 to reset an administrator password if the volume on which the password is stored is attached to an instance as the root volume. You must detach the volume from the original instance before you can attach it to a temporary instance as a secondary volume.
To detach the root volume from the instance
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Instances.
3. Select the instance that requires a password reset and choose Instance state, Stop instance.
After the status of the instance changes to Stopped, continue with the next step.
4. (Optional) If you have the private key that you specified when you launched this instance, continue with the next step. Otherwise, use the following steps to replace the instance with a new instance that you launch with a new key pair. a.
Create a new key pair using the Amazon EC2 console. To give your new key pair the same name as the one for which you lost the private key, you must first delete the existing key pair.

b.
Select the instance to replace. Note the instance type, VPC, subnet, security group, and IAM role of the instance. c.
With the instance selected, choose Actions, Image and templates, Create image. Type a name and a description for the image and choose Create image. d.
In the navigation pane, choose AMIs. Wait for the image status to change to available.
Then, select the image and choose Launch instance from AMI. e.
Complete the fields to launch an instance, making sure to select the same instance type, VPC, subnet, security group, and IAM role as the instance to replace, and then choose Launch instance. f.
When prompted, choose the key pair that you created for the new instance, and then choose Launch instance. g.
(Optional) If the original instance has an associated Elastic IP address, transfer it to the new instance. If the original instance has EBS volumes in addition to the root volume, transfer them to the new instance.
5. Detach the root volume from the original instance as follows: a.
Select the original instance and choose the Storage tab. Note the name of the root device under Root device name. Find the volume with this device name under Block devices, and note the volume ID. b.
In the navigation pane, choose Volumes. c.
In the list of volumes, select the volume that you noted as the root device, and choose Actions, Detach Volume. After the volume status changes to available, continue with the next step.
6. If you created a new instance to replace your original instance, you can terminate the original instance now. It's no longer needed. For the remainder of this procedure, all references to the original instance apply to the new instance that you created.
### Step 3: Attach the volume to a temporary instance Next, launch a temporary instance and attach the volume to it as a secondary volume. This is the instance you use to modify the configuration file.
To launch a temporary instance and attach the volume
1. Launch the temporary instance as follows:

a.
In the navigation pane, choose Instances, choose Launch instances, and then select an AMI.
Important To avoid disk signature collisions, you must select an AMI for a different version of Windows. For example, if the original instance runs Windows Server 2019, launch the temporary instance using the base AMI for Windows Server 2016. b.
Leave the default instance type and choose Next: Configure Instance Details. c.
On the Configure Instance Details page, for Subnet, select the same Availability Zone as the original instance and choose Review and Launch.
Important The temporary instance must be in the same Availability Zone as the original instance. If your temporary instance is in a different Availability Zone, you can't attach the original instance's root volume to it. d.
On the Review Instance Launch page, choose Launch. e.
When prompted, create a new key pair, download it to a safe location on your computer, and then choose Launch Instances.
2. Attach the volume to the temporary instance as a secondary volume as follows: a.
In the navigation pane, choose Volumes, select the volume that you detached from the original instance, and then choose Actions, Attach Volume. b.
In the Attach Volume dialog box, for Instances, start typing the name or ID of your temporary instance and select the instance from the list. c.
For Device, type xvdf (if it isn't already there), and choose Attach.
### Step 4: Delete the .run-once file You must now delete the .run-once file from the offline volume attached to the instance.
This directs EC2Launch v2 to run all tasks with a frequency of once, which includes setting the administrator password. The file path in the secondary volume that you attached will be similar to D:\ProgramData\Amazon\EC2Launch\state\.run-once.

To delete the .run-once file
1. Open the Disk Management utility, and bring the drive online using these instructions: Make an Amazon EBS volume available for use.
2. Locate the .run-once file in the disk you brought online.
3. Delete the .run-once file.
Important Any scripts set to run once will be triggered by this action.
### Step 5: Restart the original instance After you have deleted the .run-once file, reattach the volume to the original instance as the root volume and connect to the instance using its key pair to retrieve the administrator password.
1. Reattach the volume to the original instance as follows: a.
In the navigation pane, choose Volumes, select the volume that you detached from the temporary instance, and then choose Actions, Attach Volume. b.
In the Attach Volume dialog box, for Instances, start typing the name or ID of your original instance and then select the instance. c.
For Device, type /dev/sda1. d.
Choose Attach. After the volume status changes to in-use, continue to the next step.
2. In the navigation pane, choose Instances. Select the original instance and choose Instance state, Start instance. After the instance state changes to Running, continue to the next step.
3. Retrieve your new Windows administrator password using the private key for the new key pair and connect to the instance. For more information, see Connect to your Windows instance using RDP.
Important The instance gets a new public IP address after you stop and start it. Make sure to connect to the instance using its current public DNS name. For more information, see Amazon EC2 instance state changes.

4. (Optional) If you have no further use for the temporary instance, you can terminate it. Select the temporary instance, and choose Instance State, Terminate instance.
## Reset Windows admin password for EC2 instance using EC2Launch If you have lost your Windows administrator password and are using a Windows Server 2016 or later AMI, you can use the EC2Rescue tool, which uses the EC2Launch service to generate a new password.
If you are using a Windows Server 2016 or later AMI that does not include the EC2Launch v2 agent, you can use EC2Launch v2 to generate a new password.
If you are using a Windows Server AMI earlier than Windows Server 2016, see Reset Windows admin password for EC2 instance using EC2Config.
Warning When you stop an instance, the data on any instance store volumes is erased. To keep data from instance store volumes, be sure to back it up to persistent storage.
Note If you have disabled the local administrator account on the instance and your instance is configured for Systems Manager, you can also re-enable and reset your local administrator password by using EC2Rescue and Run Command. For more information, see Use EC2Rescue for Windows Server with Systems Manager Run Command.
Note There is an AWS Systems Manager Automation document that automatically applies the manual steps necessary to reset the local administrator password. For more information, see Reset passwords and SSH keys on EC2 instances in the AWS Systems Manager User Guide.
To reset your Windows administrator password using EC2Launch, you need to do the following:

- Step 1: Detach the root volume from the instance
- Step 2: Attach the volume to a temporary instance
- Step 3: Reset the administrator password
- Step 4: Restart the original instance
### Step 1: Detach the root volume from the instance You can't use EC2Launch to reset an administrator password if the volume on which the password is stored is attached to an instance as the root volume. You must detach the volume from the original instance before you can attach it to a temporary instance as a secondary volume.
To detach the root volume from the instance
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Instances.
3. Select the instance that requires a password reset and choose Instance state, Stop instance.
After the status of the instance changes to Stopped, continue with the next step.
4. (Optional) If you have the private key that you specified when you launched this instance, continue with the next step. Otherwise, use the following steps to replace the instance with a new instance that you launch with a new key pair. a.
Create a new key pair using the Amazon EC2 console. To give your new key pair the same name as the one for which you lost the private key, you must first delete the existing key pair. b.
Select the instance to replace. Note the instance type, VPC, subnet, security group, and IAM role of the instance. c.
With the instance selected, choose Actions, Image and templates, Create image. Type a name and a description for the image and choose Create image. d.
In the navigation pane, choose AMIs. Wait for the image status to change to available.
Then, select the image and choose Launch instance from AMI. e.
Complete the fields to launch an instance, making sure to select the same instance type, VPC, subnet, security group, and IAM role as the instance to replace, and then choose Launch instance. f.
When prompted, choose the key pair that you created for the new instance, and then choose Launch instance.

g.
(Optional) If the original instance has an associated Elastic IP address, transfer it to the new instance. If the original instance has EBS volumes in addition to the root volume, transfer them to the new instance.
5. Detach the root volume from the original instance as follows: a.
Select the original instance and choose the Storage tab. Note the name of the root device under Root device name. Find the volume with this device name under Block devices, and note the volume ID. b.
In the navigation pane, choose Volumes. c.
In the list of volumes, select the volume that you noted as the root device, and choose Actions, Detach Volume. After the volume status changes to available, continue with the next step.
6. If you created a new instance to replace your original instance, you can terminate the original instance now. It's no longer needed. For the remainder of this procedure, all references to the original instance apply to the new instance that you created.
### Step 2: Attach the volume to a temporary instance Next, launch a temporary instance and attach the volume to it as a secondary volume. This is the instance you use to run EC2Launch.
To launch a temporary instance and attach the volume
1. Launch the temporary instance as follows: a.
In the navigation pane, choose Instances, choose Launch instances, and then select an AMI.
Important To avoid disk signature collisions, you must select an AMI for a different version of Windows. For example, if the original instance runs Windows Server 2019, launch the temporary instance using the base AMI for Windows Server 2016. b.
Leave the default instance type and choose Next: Configure Instance Details. c.
On the Configure Instance Details page, for Subnet, select the same Availability Zone as the original instance and choose Review and Launch.

Important The temporary instance must be in the same Availability Zone as the original instance. If your temporary instance is in a different Availability Zone, you can't attach the original instance's root volume to it. d.
On the Review Instance Launch page, choose Launch. e.
When prompted, create a new key pair, download it to a safe location on your computer, and then choose Launch Instances.
2. Attach the volume to the temporary instance as a secondary volume as follows: a.
In the navigation pane, choose Volumes, select the volume that you detached from the original instance, and then choose Actions, Attach Volume. b.
In the Attach Volume dialog box, for Instances, start typing the name or ID of your temporary instance and select the instance from the list. c.
For Device, type xvdf (if it isn't already there), and choose Attach.
### Step 3: Reset the administrator password Next, connect to the temporary instance and use EC2Launch to reset the administrator password.
To reset the administrator password
1. Connect to the temporary instance and use the EC2Rescue for Windows Server tool on the instance to reset the administrator password as follows: a.
Download the EC2Rescue for Windows Server zip file, extract the contents, and run EC2Rescue.exe. b.
On the License Agreement screen, read the license agreement, and, if you accept the terms, choose I Agree. c.
On the Welcome to EC2Rescue for Windows Server screen, choose Next. d.
On the Select mode screen, choose Offline instance. e.
On the Select a disk screen, select the xvdf device and choose Next. f.
Confirm the disk selection and choose Yes. g.
After the volume has loaded, choose OK.

h.
On the Select Offline Instance Option screen, choose Diagnose and Rescue. i.
On the Summary screen, review the information and choose Next. j.
On the Detected possible issues screen, select Reset Administrator Password and choose Next. k.
On the Confirm screen, choose Rescue, OK. l.
On the Done screen, choose Finish. m.
Close the EC2Rescue for Windows Server tool, disconnect from the temporary instance, and then return to the Amazon EC2 console.
2. Detach the secondary (xvdf) volume from the temporary instance as follows: a.
In the navigation pane, choose Instances and select the temporary instance. b.
On the Storage tab for the temporary instance, note the ID of the EBS volume listed as xvdf. c.
In the navigation pane, choose Volumes. d.
In the list of volumes, select the volume noted in the previous step, and choose Actions, Detach Volume. After the volume status changes to available, continue with the next step.
### Step 4: Restart the original instance After you have reset the administrator password using EC2Launch, reattach the volume to the original instance as the root volume and connect to the instance using its key pair to retrieve the administrator password.
To restart the original instance
1. Reattach the volume to the original instance as follows: a.
In the navigation pane, choose Volumes, select the volume that you detached from the temporary instance, and then choose Actions, Attach Volume. b.
In the Attach Volume dialog box, for Instances, start typing the name or ID of your original instance and then select the instance. c.
For Device, type /dev/sda1. d.
Choose Attach. After the volume status changes to in-use, continue to the next step.

2. In the navigation pane, choose Instances. Select the original instance and choose Instance state, Start instance. After the instance state changes to Running, continue to the next step.
3. Retrieve your new Windows administrator password using the private key for the new key pair and connect to the instance. For more information, see Connect to your Windows instance using RDP.
4. (Optional) If you have no further use for the temporary instance, you can terminate it. Select the temporary instance, and choose Instance State, Terminate instance.
## Reset Windows admin password for EC2 instance using EC2Config If you have lost your Windows administrator password and are using a Windows AMI before Windows Server 2016, you can use the EC2Config agent to generate a new password.
If you are using a Windows Server 2016 or later AMI, see Reset Windows admin password for EC2 instance using EC2Launch or, you can use the EC2Rescue tool, which uses the EC2Launch service to generate a new password.
Note If you have disabled the local administrator account on the instance and your instance is configured for Systems Manager, you can also re-enable and reset your local administrator password by using EC2Rescue and Run Command. For more information, see Use EC2Rescue for Windows Server with Systems Manager Run Command.
Note There is an AWS Systems Manager Automation document that automatically applies the manual steps necessary to reset the local administrator password. For more information, see Reset passwords and SSH keys on EC2 instances in the AWS Systems Manager User Guide.
To reset your Windows administrator password using EC2Config, you need to do the following:
- Step 1: Verify that the EC2Config service is running
- Step 2: Detach the root volume from the instance

- Step 3: Attach the volume to a temporary instance
- Step 4: Modify the configuration file
- Step 5: Restart the original instance
### Step 1: Verify that the EC2Config service is running Before you attempt to reset the administrator password, verify that the EC2Config service is installed and running. You use the EC2Config service to reset the administrator password later in this section.
To verify that the EC2Config service is running
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Instances and then select the instance that requires a password reset. This instance is referred to as the original instance in this procedure.
3. Choose Actions, Monitor and troubleshoot, Get system log.
4. Locate the EC2 Agent entry, for example, EC2 Agent: Ec2Config service v3.18.1118. If you see this entry, the EC2Config service is running.
If the system log output is empty, or if the EC2Config service is not running, troubleshoot the instance using the Instance Console Screenshot service. For more information, see Capture a screenshot of an unreachable instance.
### Step 2: Detach the root volume from the instance You can't use EC2Config to reset an administrator password if the volume on which the password is stored is attached to an instance as the root volume. You must detach the volume from the original instance before you can attach it to a temporary instance as a secondary volume.
To detach the root volume from the instance
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Instances.
3. Select the instance that requires a password reset and choose Instance state, Stop instance.
After the status of the instance changes to Stopped, continue with the next step.

4. (Optional) If you have the private key that you specified when you launched this instance, continue with the next step. Otherwise, use the following steps to replace the instance with a new instance that you launch with a new key pair. a.
Create a new key pair using the Amazon EC2 console. To give your new key pair the same name as the one for which you lost the private key, you must first delete the existing key pair. b.
Select the instance to replace. Note the instance type, VPC, subnet, security group, and IAM role of the instance. c.
With the instance selected, choose Actions, Image and templates, Create image. Type a name and a description for the image and choose Create image. d.
In the navigation pane, choose AMIs. Wait for the image status to change to available.
Then, select the image and choose Launch instance from AMI. e.
Complete the fields to launch an instance, making sure to select the same instance type, VPC, subnet, security group, and IAM role as the instance to replace, and then choose Launch instance. f.
When prompted, choose the key pair that you created for the new instance, and then choose Launch instance. g.
(Optional) If the original instance has an associated Elastic IP address, transfer it to the new instance. If the original instance has EBS volumes in addition to the root volume, transfer them to the new instance.
5. Detach the root volume from the original instance as follows: a.
Select the original instance and choose the Storage tab. Note the name of the root device under Root device name. Find the volume with this device name under Block devices, and note the volume ID. b.
In the navigation pane, choose Volumes. c.
In the list of volumes, select the volume that you noted as the root device, and choose Actions, Detach Volume. After the volume status changes to available, continue with the next step.
6. If you created a new instance to replace your original instance, you can terminate the original instance now. It's no longer needed. For the remainder of this procedure, all references to the original instance apply to the new instance that you created.

### Step 3: Attach the volume to a temporary instance Next, launch a temporary instance and attach the volume to it as a secondary volume. This is the instance you use to modify the configuration file.
To launch a temporary instance and attach the volume
1. Launch the temporary instance as follows: a.
In the navigation pane, choose Instances, choose Launch instances, and then select an AMI.
Important To avoid disk signature collisions, you must select an AMI for a different version of Windows. For example, if the original instance runs Windows Server 2019, launch the temporary instance using the base AMI for Windows Server 2016. b.
Leave the default instance type and choose Next: Configure Instance Details. c.
On the Configure Instance Details page, for Subnet, select the same Availability Zone as the original instance and choose Review and Launch.
Important The temporary instance must be in the same Availability Zone as the original instance. If your temporary instance is in a different Availability Zone, you can't attach the original instance's root volume to it. d.
On the Review Instance Launch page, choose Launch. e.
When prompted, create a new key pair, download it to a safe location on your computer, and then choose Launch Instances.
2. Attach the volume to the temporary instance as a secondary volume as follows: a.
In the navigation pane, choose Volumes, select the volume that you detached from the original instance, and then choose Actions, Attach Volume. b.
In the Attach Volume dialog box, for Instances, start typing the name or ID of your temporary instance and select the instance from the list. c.
For Device, type xvdf (if it isn't already there), and choose Attach.

### Step 4: Modify the configuration file After you have attached the volume to the temporary instance as a secondary volume, modify the Ec2SetPassword plugin in the configuration file.
To modify the configuration file
1. From the temporary instance, modify the configuration file on the secondary volume as follows: a.
Launch and connect to the temporary instance. b.
Use the following instructions to bring the drive online: Make an Amazon EBS volume available for use. c.
Navigate to the secondary volume, and open \Program Files\Amazon \Ec2ConfigService\Settings\config.xml using a text editor, such as Notepad. d.
At the top of the file, find the plugin with the name Ec2SetPassword, as shown in the screenshot. Change the state from Disabled to Enabled and save the file.

2. After you have modified the configuration file, detach the secondary volume from the temporary instance as follows: a.
Using the Disk Management utility, bring the volume offline. b.
Disconnect from the temporary instance and return to the Amazon EC2 console. c.
In the navigation pane, choose Volumes, select the volume, and then choose Actions, Detach Volume. After the volume's status changes to available, continue with the next step.
### Step 5: Restart the original instance After you have modified the configuration file, reattach the volume to the original instance as the root volume and connect to the instance using its key pair to retrieve the administrator password.
1. Reattach the volume to the original instance as follows: a.
In the navigation pane, choose Volumes, select the volume that you detached from the temporary instance, and then choose Actions, Attach Volume. b.
In the Attach Volume dialog box, for Instances, start typing the name or ID of your original instance and then select the instance. c.
For Device, type /dev/sda1. d.
Choose Attach. After the volume status changes to in-use, continue to the next step.
2. In the navigation pane, choose Instances. Select the original instance and choose Instance state, Start instance. After the instance state changes to Running, continue to the next step.
3. Retrieve your new Windows administrator password using the private key for the new key pair and connect to the instance. For more information, see Connect to your Windows instance using RDP.
Important The instance gets a new public IP address after you stop and start it. Make sure to connect to the instance using its current public DNS name. For more information, see Amazon EC2 instance state changes.
4. (Optional) If you have no further use for the temporary instance, you can terminate it. Select the temporary instance, and choose Instance State, Terminate instance.
