# Troubleshoot issues with Amazon EC2 Windows instances

Source: apps/user-manuals/aws/ec2-ug.pdf

---

# Troubleshoot issues with Amazon EC2 Windows instances The following are troubleshooting tips to help you solve the issues with Amazon EC2 Windows instances.
Issues
- Unable to connect AWS Systems Manager Sessions Manager to a Windows Server 2025 instance
- EBS volumes don't initialize on Windows Server 2016 and 2019
- Boot an EC2 Windows instance into Directory Services Restore Mode (DSRM)
- Instance loses network connectivity or scheduled tasks don't run when expected
- Unable to get console output
- Windows Server 2012 R2 not available on the network
- Disk signature collision
## Unable to connect AWS Systems Manager Sessions Manager to a Windows Server 2025 instance Windows Server 2025 instance You may encounter an issue connecting AWS Systems Manager Sessions Manager to a Windows Server 2025 instance. To address this issue, log onto the instance, then navigate to Settings
> Apps > Optional Features, and add WMIC. Restart the SSM Agent service or reboot the instance, and Sessions Manager should connect.
You can also use the following PowerShell command to perform the same action:
Start-Process -FilePath "$env:SystemRoot\system32\Dism.exe" -ArgumentList @('/ Online', '/Add-Capability', '/CapabilityName:WMIC~~~~') -Wait; Restart-Service -Name AmazonSSMAgent
## EBS volumes don't initialize on Windows Server 2016 and 2019 Instances created from Amazon Machine Images (AMIs) for Windows Server 2016 and 2019 use the EC2Launch v1 agent for a variety of startup tasks, including initializing EBS volumes. By default, EC2Launch v1 doesn't initialize secondary volumes. However, you can configure EC2Launch v1 to initialize these disks automatically, as follows.

Map drive letters to volumes
1. Connect to the instance to configure and open the C:\ProgramData\Amazon\EC2-Windows \Launch\Config\DriveLetterMappingConfig.json file in a text editor.
2. Specify the volume settings as follows:
{ "driveLetterMapping": [ { "volumeName": "sample volume", "driveLetter": "H"
 }]
}
3. Save your changes and close the file.
4. Open Windows PowerShell and use the following command to run the EC2Launch v1 script that initializes the disks:
PS C:\>  C:\ProgramData\Amazon\EC2-Windows\Launch\Scripts\InitializeDisks.ps1 To initialize the disks each time the instance boots, add the -Schedule flag as follows:
PS C:\>  C:\ProgramData\Amazon\EC2-Windows\Launch\Scripts\InitializeDisks.ps1 - Schedule The EC2Launch v1 agent can run instance initialization scripts such as initializeDisks.ps1 in parallel with the InitializeInstance.ps1 script. If the InitializeInstance.ps1 script reboots the instance, it might interrupt other scheduled tasks that run at instance startup. To avoid any potential conflicts, we recommend that you add logic to your initializeDisks.ps1 script to ensure that instance initialization has finished first.
Note If the EC2Launch script does not initialize the volumes, ensure that the volumes are online. If the volumes are offline, run the following command to bring all disks online.

PS C:\> Get-Disk | Where-Object IsOffline -Eq $True | Set-Disk -IsOffline $False
## Boot an EC2 Windows instance into Directory Services Restore Mode (DSRM)
(DSRM)
If an instance running Microsoft Active Directory experiences a system failure or other critical issues you can troubleshoot the instance by booting into a special version of Safe Mode called Directory Services Restore Mode (DSRM). In DSRM you can repair or recover Active Directory.
### Driver support for DSRM How you enable DSRM and boot into the instance depends on the drivers the instance is running.
In the EC2 console you can view driver version details for an instance from the System Log. The following table shows which drivers are supported for DSRM.
Driver Versions DSRM Supported?
Next Steps Citrix PV 5.9 No Restore the instance from a backup. You cannot enable DSRM.
AWS PV 7.2.0 No Though DSRM is not supported for this driver, you can still detach the root volume from the instance, take a snapshot of the volume or create an AMI from it, and attach it to another instance in the same Availability Zone as a secondary volume. You can then enable DSRM (as described in this section).
AWS PV 7.2.2 and later Yes Detach the root volume, attach it to another instance, and enable DSRM (as described in this section).
Enhanced Networking Yes Detach the root volume, attach it to another instance, and enable DSRM (as described in this section).

For information about how to enable enhanced networking, see the section called "Elastic Network Adapter (ENA)". For information about upgrading AWS PV drivers, see Upgrade PV drivers on Windows instances.
### Configure an instance to boot into DSRM EC2 Windows instances do not have network connectivity before the operating system is running.
For this reason, you cannot press the F8 button on your keyboard to select a boot option. You must use one of the following procedures to boot an EC2 Windows Server instance into DSRM.
If you suspect that Active Directory has been corrupted and the instance is still running, you can configure the instance to boot into DSRM using either the System Configuration dialog box or the command prompt.
To boot an online instance into DSRM using the System Configuration dialog box
1. In the Run dialog box, type msconfig and press Enter.
2. Choose the Boot tab.
3. Under Boot options choose Safe boot.
4. Choose Active Directory repair and then choose OK. The system prompts you to reboot the server.
To boot an online instance into DSRM using the command line From a Command Prompt window, run the following command: bcdedit /set safeboot dsrepair If an instance is offline and unreachable, you must detach the root volume and attach it to another instance to enable DSRM mode.
To boot an offline instance into DSRM
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Instances.
3. Locate and select the affected instance. Choose Instance state, Stop instance.
4. Choose Launch instances and create a temporary instance in the same Availability Zone as the affected instance. Choose an instance type that uses a different version of Windows.

For example, if your instance is Windows Server 2016, then choose a Windows Server 2019 instance.
Important If you do not create the instance in the same Availability Zone as the affected instance you will not be able to attach the root volume of the affected instance to the new instance.
5. In the navigation pane, choose Volumes.
6. Locate the root volume of the affected instance. Detach the volume and attach it to the temporary instance you created earlier. Attach it with the default device name (xvdf).
7. Use Remote Desktop to connect to the temporary instance, and then use the Disk Management utility to make the volume available for use.
8. Open a command prompt and run the following command. Replace D with the actual drive letter of the secondary volume you just attached: bcdedit /store D:\Boot\BCD /set {default} safeboot dsrepair
9. In the Disk Management Utility, choose the drive you attached earlier, open the context (right- click) menu, and choose Offline.
10. In the EC2 console, detach the affected volume from the temporary instance and reattach it to your original instance with the device name /dev/sda1. You must specify this device name to designate the volume as a root volume.
11. Start the instance.
12. After the instance passes the health checks in the EC2 console, connect to the instance using Remote Desktop and verify that it boots into DSRM mode.
13. (Optional) Delete or stop the temporary instance you created in this procedure.
## Instance loses network connectivity or scheduled tasks don't run when expected expected If you restart your instance and it loses network connectivity, it's possible that the instance has the wrong time.

By default, Windows instances use Coordinated Universal Time (UTC). If you set the time for your instance to a different time zone and then restart it, the time becomes offset and the instance temporarily loses its IP address. The instance regains network connectivity eventually, but this can take several hours. The amount of time that it takes for the instance to regain network connectivity depends on the difference between UTC and the other time zone.
This same time issue can also result in scheduled tasks not running when you expect them to. In this case, the scheduled tasks do not run when expected because the instance has the incorrect time.
To use a time zone other than UTC persistently, you must set the RealTimeIsUniversal registry key.
Without this key, an instance uses UTC after you restart it.
To resolve time issues that cause a loss of network connectivity
1. Ensure that you are running the recommended PV drivers. For more information, see the section called "Upgrade PV drivers".
2. Verify that the following registry key exists and is set to 1: HKEY_LOCAL_MACHINE\SYSTEM \CurrentControlSet\Control\TimeZoneInformation\RealTimeIsUniversal
## Unable to get console output For Windows instances, the instance console displays the output from tasks performed during the Windows boot process. If Windows boots successfully, the last message logged is Windows is Ready to use. You can also display event log messages in the console, but this feature might not be enabled by default depending on your version of Windows. For more information, see the section called "Windows launch agents".
To get the console output for your instance using the Amazon EC2 console, select the instance, and then choose Actions, Monitor and troubleshoot, Get system log. To get the console output using the command line, use one of the following commands: get-console-output (AWS CLI) or Get-EC2ConsoleOutput (AWS Tools for Windows PowerShell).
For instances running Windows Server 2012 R2 and earlier, if the console output is empty, it could indicate an issue with the EC2Config service, such as a misconfigured configuration file, or that Windows failed to boot properly. To fix the issue, download and install the latest version of EC2Config. For more information, see the section called "Install EC2Config".

## Windows Server 2012 R2 not available on the network For information about troubleshooting a Windows Server 2012 R2 instance that is not available on the network, see  Windows Server 2012 R2 loses network and storage connectivity after an instance reboot.
## Disk signature collision You can check for and resolve disk signature collisions using EC2Rescue for Windows Server. Or, you can manually resolve disk signature issues by performing the following steps.
Warning The following procedure describes how to edit the Windows Registry using Registry Editor.
If you are not familiar with the Windows Registry or how to safely make changes using Registry Editor, see Configure the Registry.
1. Open a command prompt, type regedit.exe, and press Enter.
2. In the Registry Editor, choose HKEY_LOCAL_MACHINE from the context menu (right-click), and then choose Find.
3. Type Windows Boot Manager and then choose Find Next.
4. Choose the key named 11000001. This key is a sibling of the key you found in the previous step.
5. In the right pane, choose Element and then choose Modify from the context menu (right- click).
6. Locate the four-byte disk signature at offset 0x38 in the data. This is the Boot Configuration Database signature (BCD). Reverse the bytes to create the disk signature, and write it down.
For example, the disk signature represented by the following data is E9EB3AA5:
...
0030  00 00 00 00 01 00 00 00 0038   A5 3A EB E9 00 00 00 00 0040  00 00 00 00 00 00 00 00 ...
7. In a Command Prompt window, run the following command to start Microsoft DiskPart.
