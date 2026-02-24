# Instance launch behavior with Amazon EC2 boot modes

Source: apps/user-manuals/aws/ec2-ug.pdf

---

Use the disable-image-deregistration-protection command. aws ec2 disable-image-deregistration-protection --image-id ami-0abcdef1234567890 PowerShell To turn off deregistration protection Use the Disable-EC2ImageDeregistrationProtection cmdlet.
Disable-EC2ImageDeregistrationProtection -ImageId ami-0abcdef1234567890
# Instance launch behavior with Amazon EC2 boot modes When a computer boots, the first software that it runs is responsible for initializing the platform and providing an interface for the operating system to perform platform-specific operations.
In Amazon EC2, two variants of the boot mode software are supported: Unified Extensible Firmware Interface (UEFI) and Legacy BIOS.
Possible boot mode parameters on an AMI An AMI can have one of the following boot mode parameter values: uefi, legacy-bios, or uefi-preferred. The AMI boot mode parameter is optional. For AMIs with no boot mode parameter, the instances launched from these AMIs use the default boot mode value of the instance type.
Purpose of the AMI boot mode parameter The AMI boot mode parameter signals to Amazon EC2 which boot mode to use when launching an instance. When the boot mode parameter is set to uefi, EC2 attempts to launch the instance on UEFI. If the operating system is not configured to support UEFI, the instance launch will be unsuccessful.
UEFI Preferred boot mode parameter You can create AMIs that support both UEFI and Legacy BIOS by using the uefi-preferred boot mode parameter. When the boot mode parameter is set to uefi-preferred, and if the instance

type supports UEFI, the instance is launched on UEFI. If the instance type does not support UEFI, the instance is launched on Legacy BIOS.
Warning Some features, like UEFI Secure Boot, are only available on instances that boot on UEFI.
When you use the uefi-preferred AMI boot mode parameter with an instance type that does not support UEFI, the instance will launch as Legacy BIOS and the UEFI-dependent feature will be disabled. If you rely on the availability of a UEFI-dependent feature, set your AMI boot mode parameter to uefi.
Default boot modes for instance types
- Graviton instance types: UEFI
- Intel and AMD instance types: Legacy BIOS Zone support UEFI boot is not supported in Wavelength Zones.
Boot mode topics
- Requirements to launch an EC2 instance in UEFI boot mode
- Determine the boot mode parameter of an Amazon EC2 AMI
- Determine the supported boot modes of an EC2 instance type
- Determine the boot mode of an EC2 instance
- Determine the boot mode of the operating system for your EC2 instance
- Set the boot mode of an Amazon EC2 AMI
- UEFI variables for Amazon EC2 instances
- UEFI Secure Boot for Amazon EC2 instances
## Requirements to launch an EC2 instance in UEFI boot mode The boot mode of an instance is determined by the configuration of the AMI, the operating system contained in it, and the instance type. To launch an instance in UEFI boot mode, you must meet the following requirements.

AMI The AMI must be configured for UEFI as follows:
- Operating system – The operating system contained in the AMI must be configured to use UEFI; otherwise, the instance launch will fail. For more information, see Determine the boot mode of the operating system for your EC2 instance.
- AMI boot mode parameter – The boot mode parameter of the AMI must be set to uefi or uefi-preferred. For more information, see Determine the boot mode parameter of an Amazon EC2 AMI.
Linux – The following Linux AMIs support UEFI:
- Amazon Linux 2023
- Amazon Linux 2 (Graviton instance types only)
For other Linux AMIs, you must configure the AMI, import the AMI through VM Import/Export, or import the AMI through CloudEndure.
Windows – The following Windows AMIs support UEFI:
- Windows_Server-2025-* (except for AMIs with the BIOS- name prefix)
- TPM-Windows_Server-2022-English-Full-Base
- TPM-Windows_Server-2022-English-Core-Base
- TPM-Windows_Server-2019-English-Full-Base
- TPM-Windows_Server-2019-English-Core-Base
- TPM-Windows_Server-2016-English-Full-Base
- TPM-Windows_Server-2016-English-Core-Base Instance type All instances built on the AWS Nitro System support both UEFI and Legacy BIOS, except the following: bare metal instances, DL1, G4ad, P4, u-3tb1, u-6tb1, u-9tb1, u-12tb1, u-18tb1, u-24tb1, and VT1. For more information, see the section called "Instance type boot mode".
The following table shows that the boot mode of an instance (indicated by the Resulting instance boot mode column) is determined by a combination of the boot mode parameter of the AMI (column 1), the boot mode configuration of the operating system contained in the AMI (column 2), and the boot mode support of the instance type (column 3).

AMI boot mode parameter Operating system boot mode configura tion Instance type boot mode support Resulting instance boot mode UEFI UEFI UEFI UEFI Legacy BIOS Legacy BIOS Legacy BIOS Legacy BIOS UEFI Preferred UEFI UEFI UEFI UEFI Preferred UEFI UEFI and Legacy BIOS UEFI UEFI Preferred Legacy BIOS Legacy BIOS Legacy BIOS UEFI Preferred Legacy BIOS UEFI and Legacy BIOS Legacy BIOS No boot mode specified - ARM UEFI UEFI UEFI No boot mode specified - x86 Legacy BIOS UEFI and Legacy BIOS Legacy BIOS
## Determine the boot mode parameter of an Amazon EC2 AMI The AMI boot mode parameter is optional. An AMI can have one of the following boot mode parameter values: uefi, legacy-bios, or uefi-preferred.
Some AMIs don't have a boot mode parameter. When an AMI has no boot mode parameter, the instances launched from the AMI use the default value of the instance type, which is uefi on Graviton, and legacy-bios on Intel and AMD instance types.
Console To determine the boot mode parameter of an AMI
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose AMIs, and then select the AMI.
3. Inspect the Boot mode field.

- A value of uefi indicates that the AMI supports UEFI.
- A value of uefi-preferred indicates that the AMI supports both UEFI and Legacy BIOS.
- If there is no value, the instances launched from the AMI use the default value of the instance type.
To determine the boot mode parameter of an AMI when launching an instance When launching an instance using the launch instance wizard, at the step to select an AMI, inspect the Boot mode field. For more information, see Application and OS Images (Amazon Machine Image).
AWS CLI To determine the boot mode parameter of an AMI Use the describe-images command to determine the boot mode of an AMI. aws ec2 describe-images \ --region us-east-1 \ --image-id ami-0abcdef1234567890 \ --query Images[].BootMode \ --output text The following is example output. uefi In the output, a value of uefi indicates that the AMI supports UEFI. A value of uefi- preferred indicates that the AMI supports both UEFI and Legacy BIOS. If there is no value, the instances launched from the AMI use the default value of the instance type.
PowerShell To determine the boot mode parameter of an AMI Use the Get-EC2Image cmdlet to determine the boot mode of an AMI.
Get-EC2Image -Region us-east-1 `
    -ImageId ami-0abcdef1234567890 | Format-List Name, BootMode, TpmSupport

The following is example output.
Name       : TPM-Windows_Server-2016-English-Full-Base-2023.05.10 BootMode   : uefi TpmSupport : v2.0 In the output, the value of BootMode indicates the boot mode of the AMI. A value of uefi indicates that the AMI supports UEFI. A value of uefi-preferred indicates that the AMI supports both UEFI and Legacy BIOS. If there is no value, the instances launched from the AMI use the default value of the instance type.
## Determine the supported boot modes of an EC2 instance type You can determine the supported boot modes of an instance type.
The Amazon EC2 console does not display the supported boot modes of an instance type.
AWS CLI Use the describe-instance-types command to determine the supported boot modes of an instance type. The --query parameter filters the output to return only the supported boot modes.
The following example shows that the specified instance type supports both UEFI and Legacy BIOS boot modes. aws ec2 describe-instance-types \ --instance-types m5.2xlarge \ --query "InstanceTypes[*].SupportedBootModes"
The following is example output.
[ [ "legacy-bios", "uefi"
    ]
]
The following example shows that t2.xlarge supports only Legacy BIOS.

aws ec2 describe-instance-types \ --instance-types t2.xlarge \ --query "InstanceTypes[*].SupportedBootModes"
The following is example output.
[ [ "legacy-bios"
    ]
]
PowerShell Use the Get-EC2InstanceType cmdlet to determine the supported boot modes of an instance type.
The following example shows that m5.2xlarge supports both UEFI and Legacy BIOS boot modes.
Get-EC2InstanceType -InstanceType m5.2xlarge | Format-List InstanceType, SupportedBootModes The following is example output.
InstanceType       : m5.2xlarge SupportedBootModes : {legacy-bios, uefi} The following example shows that t2.xlarge supports only Legacy BIOS.
Get-EC2InstanceType -InstanceType t2.xlarge | Format-List InstanceType, SupportedBootModes The following is example output.
InstanceType       : t2.xlarge SupportedBootModes : {legacy-bios} To determine the instance types that support UEFI

You can determine the instance types that support UEFI. The Amazon EC2 console does not display the UEFI support of an instance type.
AWS CLI The available instance types vary by AWS Region. To see the available instance types that support UEFI in a Region, use the describe-instance-types command. Include the --filters parameter to scope the results to the instance types that support UEFI and the --query parameter to scope the output to the value of InstanceType. aws ec2 describe-instance-types \ --filters Name=supported-boot-mode,Values=uefi \ --query "InstanceTypes[*].[InstanceType]" --output text | sort

PowerShell The available instance types vary by AWS Region. To see the available instance types that support UEFI in a Region, use the Get-EC2InstanceType cmdlet.
Get-EC2InstanceType | `
 Where-Object {$_.SupportedBootModes -Contains "uefi"} | `
 Sort-Object InstanceType | `
 Format-Table InstanceType -GroupBy CurrentGeneration To determine the instance types that support UEFI Secure Boot and persist non-volatile variables Bare metal instances do not support UEFI Secure Boot and non-volatile variables, so these examples exclude them from the output. For information about UEFI Secure Boot, see UEFI Secure Boot for Amazon EC2 instances.
AWS CLI Use the describe-instance-types command, and exclude the bare metal instances from the output. aws ec2 describe-instance-types \ --filters Name=supported-boot-mode,Values=uefi Name=bare-metal,Values=false \

    --query "InstanceTypes[*].[InstanceType]" \ --output text | sort PowerShell Use the Get-EC2InstanceType cmdlet, and exclude the bare metal instances from the output.
Get-EC2InstanceType | `
    Where-Object { `
        $_.SupportedBootModes -Contains "uefi" -and `
        $_.BareMetal -eq $False } | `
    Sort-Object InstanceType  | `
    Format-Table InstanceType, SupportedBootModes, BareMetal, `
        @{Name="SupportedArchitectures"; Expression={$_.ProcessorInfo.SupportedArchitectures}}
## Determine the boot mode of an EC2 instance The boot mode of an instance is displayed in the Boot mode field in the Amazon EC2 console, and by the currentInstanceBootMode parameter in the AWS CLI.
When an instance is launched, the value for its boot mode parameter is determined by the value of the boot mode parameter of the AMI used to launch it, as follows:
- An AMI with a boot mode parameter of uefi creates an instance with a currentInstanceBootMode parameter of uefi.
- An AMI with a boot mode parameter of legacy-bios creates an instance with a currentInstanceBootMode parameter of legacy-bios.
- An AMI with a boot mode parameter of uefi-preferred creates an instance with a currentInstanceBootMode parameter of uefi if the instance type supports UEFI; otherwise, it creates an instance with a currentInstanceBootMode parameter of legacy-bios.
- An AMI with no boot mode parameter value creates an instance with a currentInstanceBootMode parameter value that is dependent on whether the AMI architecture is ARM or x86 and the supported boot mode of the instance type. The default boot mode is uefi on Graviton instance types, and legacy-bios on Intel and AMD instance types.

Console To determine the boot mode of an instance
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Instances, and then select your instance.
3. On the Details tab, inspect the Boot mode field.
AWS CLI To determine the boot mode of an instance Use the describe-instances command to determine the boot mode of an instance. You can also determine the boot mode of the AMI that was used to the create the instance. aws ec2 describe-instances \ --region us-east-1 \ --instance-ids i-1234567890abcdef0 \ --query Reservations[].Instances[].BootMode \ --output text The following is example output. uefi PowerShell To determine the boot mode of an instance Use the Get-EC2Image cmdlet to determine the boot mode of an instance. You can also determine the boot mode of the AMI that was used to the create the instance.
(Get-EC2Instance `
    -InstanceId i-1234567890abcdef0).Instances | Format-List BootMode, CurrentInstanceBootMode, InstanceType, ImageId The following is example output.
BootMode                : uefi CurrentInstanceBootMode : uefi

InstanceType            : c5a.large ImageId                 : ami-0abcdef1234567890
## Determine the boot mode of the operating system for your EC2 instance instance The boot mode of the AMI guides Amazon EC2 on which boot mode to use to boot an instance. To view whether the operating system of your instance is configured for UEFI, you need to connect to your instance using SSH (Linux instances) or RDP (Windows instances).
Use the instructions for your instance's operating system.
### Linux To determine the boot mode of the instance's operating system
1. Connect to your Linux instance using SSH.
2. To view the boot mode of the operating system, try one of the following:
- Run the following command.
[ec2-user ~]$ sudo /usr/sbin/efibootmgr Expected output from an instance booted in UEFI boot mode BootCurrent: 0001 Timeout: 0 seconds BootOrder: 0000,0001 Boot0000* UiApp Boot0001* UEFI Amazon Elastic Block Store vol-xyz
- Run the following command to verify the existence of the /sys/firmware/efi directory.
This directory exists only if the instance boots using UEFI. If this directory doesn't exist, the command returns Legacy BIOS Boot Detected.
[ec2-user ~]$ [ -d /sys/firmware/efi ] && echo "UEFI Boot Detected" || echo "Legacy BIOS Boot Detected"
Expected output from an instance booted in UEFI boot mode

UEFI Boot Detected Expected output from an instance booted in Legacy BIOS boot mode Legacy BIOS Boot Detected
- Run the following command to verify that EFI appears in the dmesg output.
[ec2-user ~]$ dmesg | grep -i "EFI"
Expected output from an instance booted in UEFI boot mode [    0.000000] efi: Getting EFI parameters from FDT:
[    0.000000] efi: EFI v2.70 by EDK II
### Windows To determine the boot mode of the instance's operating system
1. Connect to your Windows instance using RDP.
2. Go to System Information and check the BIOS Mode row.

## Set the boot mode of an Amazon EC2 AMI By default, an AMI inherits the boot mode of the EC2 instance used to create the AMI. For example, if you create an AMI from an EC2 instance running on Legacy BIOS, the boot mode of the new AMI is legacy-bios. If you create an AMI from an EC2 instance with a boot mode of uefi- preferred, the boot mode of the new AMI is uefi-preferred.
When you register an AMI, you can set the boot mode of the AMI to uefi, legacy-bios, or uefi- preferred.
When the AMI boot mode is set to uefi-preferred, the instance boots as follows:
- For instance types that support both UEFI and Legacy BIOS (for example, m5.large), the instance boots using UEFI.
- For instance types that support only Legacy BIOS (for example, m4.large), the instance boots using Legacy BIOS.
If you set the AMI boot mode to uefi-preferred, the operating system must support the ability to boot both UEFI and Legacy BIOS.

To convert an existing Legacy BIOS-based instance to UEFI, or an existing UEFI-based instance to Legacy BIOS, you must first modify the instance's volume and operating system to support the selected boot mode. Then, create a snapshot of the volume. Finally, create an AMI from the snapshot.
Considerations
- Setting the AMI boot mode parameter does not automatically configure the operating system for the specified boot mode. You must first make suitable modifications to the instance's volume and operating system to support booting using the selected boot mode. Otherwise, the resulting AMI is not usable. For example, if you are converting a Legacy BIOS-based Windows instance to UEFI, you can use the MBR2GPT tool from Microsoft to convert the system disk from MBR to GPT.
The modifications that are required are operating system-specific. For more information, see the manual for your operating system.
- You can't use the register-image command or the Register-EC2Image cmdlet to create an AMI that supports both NitroTPM and UEFI Preferred.
- Some features, like UEFI Secure Boot, are only available on instances that boot on UEFI. When you use the uefi-preferred AMI boot mode parameter with an instance type that does not support UEFI, the instance launches as Legacy BIOS and the UEFI-dependent feature is disabled.
If you rely on the availability of a UEFI-dependent feature, set your AMI boot mode parameter to uefi.
AWS CLI To set the boot mode of an AMI
1. Make suitable modifications to the instance's volume and operating system to support booting via the selected boot mode. The modifications that are required are operating system-specific. For more information, see the manual for your operating system.
Warning If you don't perform this step, the AMI will not be usable.
2. To find the volume ID of the instance, use the describe-instances command. You'll create a snapshot of this volume in the next step. aws ec2 describe-instances \

    --instance-ids i-1234567890abcdef0 \ --query Reservations[].Instances[].BlockDeviceMappings The following is example output.
[ [ { "DeviceName": "/dev/xvda", "Ebs": { "AttachTime": "2024-07-11T01:05:51+00:00", "DeleteOnTermination": true, "Status": "attached", "VolumeId": "vol-1234567890abcdef0"
            } } ]
]
3. To create a snapshot of the volume, use the create-snapshot command. Use the volume ID from the previous step. aws ec2 create-snapshot \ --volume-id vol-01234567890abcdef \ --description "my snapshot"
The following is example output.
{ "Description": "my snapshot", "Encrypted": false, "OwnerId": "123456789012", "Progress": "", "SnapshotId": "snap-0abcdef1234567890", "StartTime": "", "State": "pending", "VolumeId": "vol-01234567890abcdef", "VolumeSize": 30, "Tags": []
}

4. Wait until the state of the snapshot is completed before you go to the next step. To get the state of the snapshot, use the describe-snapshots command with the snapshot ID from the previous step. aws ec2 describe-snapshots \ --snapshot-ids snap-0abcdef1234567890 \ --query Snapshots[].State \ --output text The following is example output. completed
5. To create a new AMI, use the register-image command. Use the value of SnapshotId from the output of CreateSnapshot.
- To set the boot mode to UEFI, add the --boot-mode parameter with a value of uefi. aws ec2 register-image \ --description "my image" \ --name "my-image" \ --block-device-mappings "DeviceName=/dev/ sda1,Ebs={SnapshotId=snap-0abcdef1234567890,DeleteOnTermination=true}" \ --root-device-name /dev/sda1 \ --virtualization-type hvm \ --ena-support \ --boot-mode uefi
- To set the boot mode to uefi-preferred, set the value of --boot-mode to uefi- preferred aws ec2 register-image \ --description "my description" \ --name "my-image" \ --block-device-mappings "DeviceName=/dev/ sda1,Ebs={SnapshotId=snap-0abcdef1234567890,DeleteOnTermination=true}" \ --root-device-name /dev/sda1 \ --virtualization-type hvm \ --ena-support \ --boot-mode uefi-preferred

6. (Optional) To verify that the newly-created AMI has the boot mode that you specified, use the describe-images command. aws ec2 describe-images \ --image-id ami-1234567890abcdef0 \ --query Images[].BootMode \ --output text The following is example output. uefi PowerShell To set the boot mode of an AMI
1. Make suitable modifications to the instance's volume and operating system to support booting via the selected boot mode. The modifications that are required are operating system-specific. For more information, see the manual for your operating system.
Warning If you don't perform this step, the AMI will not be usable.
2. To find the volume ID of the instance, use the Get-EC2Instance cmdlet.
(Get-EC2Instance `
    -InstanceId i-1234567890abcdef0).Instances.BlockDeviceMappings.Ebs The following is example output.
AssociatedResource  :
AttachTime          : 7/11/2024 1:05:51 AM DeleteOnTermination : True Operator            :
Status              : attached VolumeId            : vol-01234567890abcdef

3. To create a snapshot of the volume, use the New-EC2Snapshot cmdlet. Use the volume ID from the previous step.
New-EC2Snapshot `
    -VolumeId vol-01234567890abcdef `
    -Description "my snapshot"
The following is example output.
AvailabilityZone          :
Description               : my snapshot Encrypted                 : False FullSnapshotSizeInBytes   : 0 KmsKeyId                  :
OwnerId                   : 123456789012 RestoreExpiryTime         :
SnapshotId                : snap-0abcdef1234567890 SseType                   :
StartTime                 : 4/25/2025 6:08:59 PM State                     : pending StateMessage              :
VolumeId                  : vol-01234567890abcdef VolumeSize                : 30
4. Wait until the state of the snapshot is completed before you go to the next step. To get the state of the snapshot, use the Get-EC2Snapshot cmdlet with the snapshot ID from the previous step.
(Get-EC2Snapshot `
    -SnapshotId snap-0abcdef1234567890).State.Value The following is example output. completed
5. To create a new AMI, use the Register-EC2Image cmdlet. Use the value of SnapshotId from the output of New-EC2Snapshot.
- To set the boot mode to UEFI, add the -BootMode parameter with a value of uefi.
$block = @{SnapshotId=snap-0abcdef1234567890}

Register-EC2Image `
   -Description "my image" `
   -Name "my-image" `
   -BlockDeviceMapping @{DeviceName="/dev/xvda";Ebs=$block} `
   -RootDeviceName /dev/xvda `
   -EnaSupport $true `
    -BootMode uefi
- To set the boot mode to uefi-preferred, set the value of -BootMode to uefi- preferred $block = @{SnapshotId=snap-0abcdef1234567890} Register-EC2Image `
   -Description "my image" `
   -Name "my-image" `
   -BlockDeviceMapping @{DeviceName="/dev/xvda";Ebs=$block} `
   -RootDeviceName /dev/xvda `
   -EnaSupport $true `
    -BootMode uefi-preferred
6. (Optional) To verify that the newly-created AMI has the boot mode that you specified, use the Get-EC2Image cmdlet.
(Get-EC2Image `
    -ImageId ami-1234567890abcdef0).BootMode.Value The following is example output. uefi
## UEFI variables for Amazon EC2 instances When you launch an instance where the boot mode is set to UEFI, a key-value store for variables is created. The store can be used by UEFI and the instance operating system for storing UEFI variables.
UEFI variables are used by the boot loader and the operating system to configure early system startup. They allow the operating system to manage certain settings of the boot process, like the boot order, or managing the keys for UEFI Secure Boot.

Warning Anyone who can connect to the instance (and potentially any software running on the instance), or anyone with permissions to use the  GetInstanceUefiData API on the instance can read the variables. You should never store sensitive data, such as passwords or personally identifiable information, in the UEFI variable store.
UEFI variable persistence
- For instances that were launched on or before May 10, 2022, UEFI variables are wiped on reboot or stop.
- For instances that are launched on or after May 11, 2022, UEFI variables that are marked as non- volatile are persisted on reboot and stop/start.
- Bare metal instances don't preserve UEFI non-volatile variables across instance stop/start operations.
## UEFI Secure Boot for Amazon EC2 instances UEFI Secure Boot builds on the long-standing secure boot process of Amazon EC2, and provides additional defense-in-depth that helps customers secure software from threats that persist across reboots. It ensures that the instance only boots software that is signed with cryptographic keys.
The keys are stored in the key database of the UEFI non-volatile variable store. UEFI Secure Boot prevents unauthorized modification of the instance boot flow.
Contents
- How UEFI Secure Boot works with Amazon EC2 instances
- Requirements for UEFI Secure Boot on Amazon EC2
- Verify whether an Amazon EC2 instance is enabled for UEFI Secure Boot
- Create a Linux AMI with custom UEFI Secure Boot keys
- Create the AWS binary blob for UEFI Secure Boot
### How UEFI Secure Boot works with Amazon EC2 instances UEFI Secure Boot is a feature specified in UEFI, which provides verification about the state of the boot chain. It is designed to ensure that only cryptographically verified UEFI binaries are executed

after the self-initialization of the firmware. These binaries include UEFI drivers and the main bootloader, as well as chain-loaded components.
UEFI Secure Boot specifies four key databases, which are used in a chain of trust. The databases are stored in the UEFI variable store.
The chain of trust is as follows:
Platform key (PK) database The PK database is the root of trust. It contains a single public PK key that is used in the chain of trust for updating the key exchange key (KEK) database.
To change the PK database, you must have the private PK key to sign an update request. This includes deleting the PK database by writing an empty PK key.
Key exchange key (KEK) database The KEK database is a list of public KEK keys that are used in the chain of trust for updating the signature (db) and denylist (dbx) databases.
To change the public KEK database, you must have the private PK key to sign an update request.
Signature (db) database The db database is a list of public keys and hashes that are used in the chain of trust to validate all UEFI boot binaries.
To change the db database, you must have the private PK key or any of the private KEK keys to sign an update request.
Signature denylist (dbx) database The dbx database is a list of public keys and binary hashes that are not trusted, and are used in the chain of trust as a revocation file.
The dbx database always takes precedence over all other key databases.
To change the dbx database, you must have the private PK key or any of the private KEK keys to sign an update request.
The UEFI Forum maintains a publicly available dbx for many known-bad binaries and certs at https://uefi.org/revocationlistfile.

Important UEFI Secure Boot enforces signature validation on any UEFI binaries. To permit execution of a UEFI binary in UEFI Secure Boot, you sign it with any of the private db keys described above.
By default, UEFI Secure Boot is disabled and the system is in SetupMode. When the system is in SetupMode, all key variables can be updated without a cryptographic signature. When the PK is set, UEFI Secure Boot is enabled and the SetupMode is exited.
### Requirements for UEFI Secure Boot on Amazon EC2 When you launch an Amazon EC2 instance with a supported AMI and a supported instance type, that instance will automatically validate UEFI boot binaries against its UEFI Secure Boot database.
No additional configuration is required. You can also configure UEFI Secure Boot on an instance after launch.
Note UEFI Secure Boot protects your instance and its operating system against boot flow modifications. If you create a new AMI from a source AMI that has UEFI Secure Boot enabled and modify certain parameters during the copy process, such as changing the UefiData within the AMI, you can disable UEFI Secure Boot.
Contents
- Supported AMIs
- Supported instance types
#### Supported AMIs Linux AMIs To launch a Linux instance, the Linux AMI must have UEFI Secure Boot enabled.
Amazon Linux supports UEFI Secure Boot starting with AL2023 release 2023.1. However, UEFI Secure Boot isn't enabled in the default AMIs. For more information, see UEFI Secure Boot in the

AL2023 User Guide. Older versions of Amazon Linux AMIs aren't enabled for UEFI Secure Boot. To use a supported AMI, you must perform a number of configuration steps on your own Linux AMI.
For more information, see Create a Linux AMI with custom UEFI Secure Boot keys.
Windows AMIs To launch a Windows instance, the Windows AMI must have UEFI Secure Boot enabled. To find an AWS Windows AMI that's preconfigured for UEFI Secure Boot with Microsoft keys, see Find Windows Server AMIs configured with NitroTPM and UEFI Secure Boot in the AWS Windows AMIs Reference.
Currently, we do not support importing Windows with UEFI Secure Boot by using the import-image command.
#### Supported instance types All virtualized instance types that support UEFI also support UEFI Secure Boot. For the instance types that support UEFI Secure Boot, see Requirements for UEFI boot mode.
Note Bare metal instance types do not support UEFI Secure Boot.
### Verify whether an Amazon EC2 instance is enabled for UEFI Secure Boot You can use the following procedures to determine whether an Amazon EC2 is enabled for UEFI Secure Boot.
#### Linux instances You can use the mokutil utility to verify whether a Linux instance is enabled for UEFI Secure Boot.
If mokutil is not installed on your instance, you must install it. For the installation instructions for Amazon Linux 2, see Find and install software packages on an Amazon Linux 2 instance. For other Linux distributions, see their specific documentation.
To verify whether a Linux instance is enabled for UEFI Secure Boot Connect to your instance and run the following command as root in a terminal window.

mokutil --sb-state The following is example output.
- If UEFI Secure Boot is enabled, the output contains SecureBoot enabled.
- If UEFI Secure Boot is not enabled, the output contains SecureBoot disabled or Failed to read SecureBoot.
#### Windows instances To verify whether a Windows instance is enabled for UEFI Secure Boot
1. Connect to your instance.
2. Open the msinfo32 tool.
3. Check the Secure Boot State field. If UEFI Secure Boot is enabled, the value is Supported, as shown in the following image.
You can also use the Windows PowerShell Cmdlet Confirm-SecureBootUEFI to check the Secure Boot status. For more information about the cmdlet, see Confirm-SecureBootUEFI in the Microsoft Documentation.

### Create a Linux AMI with custom UEFI Secure Boot keys These instructions show you how to create a Linux AMI with UEFI Secure Boot and custom-made private keys. Amazon Linux supports UEFI Secure Boot starting with AL2023 release 2023.1. For more information, see UEFI Secure Boot on AL2023 in the Amazon Linux 2023 User Guide.
Important The following procedure is intended for advanced users only. You must have sufficient knowledge of SSL and Linux distribution boot flow to use these procedures.
Prerequisites
- The following tools will be used:
- OpenSSL – https://www.openssl.org/
- efivar – https://github.com/rhboot/efivar
- efitools – https://git.kernel.org/pub/scm/linux/kernel/git/jejb/efitools.git/
- get-instance-uefi-data command
- Your Linux instance must have been launched with a Linux AMI that supports UEFI boot mode, and have non-volatile data present.
Newly created instances without UEFI Secure Boot keys are created in SetupMode, which allows you to enroll your own keys. Some AMIs come preconfigured with UEFI Secure Boot and you cannot change the existing keys. If you want to change the keys, you must create a new AMI based on the original AMI.
You have two ways to propagate the keys in the variable store, which are described in Option A and Option B that follow. Option A describes how to do this from within the instance, mimicking the flow of real hardware. Option B describes how to create a binary blob, which is then passed as a base64-encoded file when you create the AMI. For both options, you must first create the three key pairs, which are used for the chain of trust.
To create a Linux AMI that supports UEFI Secure Boot, first create the three key pairs, and then complete either Option A or Option B, but not both:
- Task 1: Create key pairs
- Task 2 - Option A: Add keys to the variable store from within the instance

- Task 2 - Option B: Create a binary blob containing a pre-filled variable store
#### Task 1: Create key pairs UEFI Secure Boot is based on the following three key databases, which are used in a chain of trust: the platform key (PK), the key exchange key (KEK), and the signature database (db).¹ You create each key on the instance. To prepare the public keys in a format that is valid for the UEFI Secure Boot standard, you create a certificate for each key. DER defines the SSL format (binary encoding of a format). You then convert each certificate into a UEFI signature list, which is the binary format that is understood by UEFI Secure Boot. And finally, you sign each certificate with the relevant key.
Tasks
- Prepare to create the key pairs
- Key pair 1: Create the platform key (PK)
- Key pair 2: Create the key exchange key (KEK)
- Key pair 3: Create the signature database (db)
- Sign the boot image (kernel) with the private key
##### Prepare to create the key pairs Before creating the key pairs, create a globally unique identifier (GUID) to be used in key generation.
1. Connect to the instance.
2. Run the following command in a shell prompt. uuidgen --random > GUID.txt
##### Key pair 1: Create the platform key (PK)
The PK is the root of trust for UEFI Secure Boot instances. The private PK is used to update the KEK, which in turn can be used to add authorized keys to the signature database (db).
The X.509 standard is used for creating the key pair. For information about the standard, see X.509 on Wikipedia.

To create the PK
1. Create the key. You must name the variable PK. openssl req -newkey rsa:4096 -nodes -keyout PK.key -new -x509 -sha256 -days 3650 - subj "/CN=Platform key/" -out PK.crt The following parameters are specified:
- -keyout PK.key – The private key file.
- -days 3650 – The number of days that the certificate is valid.
- -out PK.crt – The certificate that is used to create the UEFI variable.
- CN=Platform key – The common name (CN) for the key. You can enter the name of your own organization instead of Platform key.
2. Create the certificate. openssl x509 -outform DER -in PK.crt -out PK.cer
3. Convert the certificate into a UEFI signature list. cert-to-efi-sig-list -g "$(< GUID.txt)" PK.crt PK.esl
4. Sign the UEFI signature list with the private PK (self-signed). sign-efi-sig-list -g "$(< GUID.txt)" -k PK.key -c PK.crt PK PK.esl PK.auth
##### Key pair 2: Create the key exchange key (KEK)
The private KEK is used to add keys to the db, which is the list of authorized signatures to boot on the system.
To create the KEK
1. Create the key. openssl req -newkey rsa:4096 -nodes -keyout KEK.key -new -x509 -sha256 -days 3650 - subj "/CN=Key Exchange Key/" -out KEK.crt
2. Create the certificate.

openssl x509 -outform DER -in KEK.crt -out KEK.cer
3. Convert the certificate into a UEFI signature list. cert-to-efi-sig-list -g "$(< GUID.txt)" KEK.crt KEK.esl
4. Sign the signature list with the private PK. sign-efi-sig-list -g "$(< GUID.txt)" -k PK.key -c PK.crt KEK KEK.esl KEK.auth
##### Key pair 3: Create the signature database (db)
The db list contains authorized keys that are authorized to be booted on the system. To modify the list, the private KEK is necessary. Boot images will be signed with the private key that is created in this step.
To create the db
1. Create the key. openssl req -newkey rsa:4096 -nodes -keyout db.key -new -x509 -sha256 -days 3650 - subj "/CN=Signature Database key/" -out db.crt
2. Create the certificate. openssl x509 -outform DER -in db.crt -out db.cer
3. Convert the certificate into a UEFI signature list. cert-to-efi-sig-list -g "$(< GUID.txt)" db.crt db.esl
4. Sign the signature list with the private KEK. sign-efi-sig-list -g "$(< GUID.txt)" -k KEK.key -c KEK.crt db db.esl db.auth
##### Sign the boot image (kernel) with the private key For Ubuntu 22.04, the following images require signatures.

/boot/efi/EFI/ubuntu/shimx64.efi /boot/efi/EFI/ubuntu/mmx64.efi /boot/efi/EFI/ubuntu/grubx64.efi /boot/vmlinuz To sign an image Use the following syntax to sign an image. sbsign --key db.key --cert db.crt --output /boot/vmlinuz /boot/vmlinuz Note You must sign all new kernels. /boot/vmlinuz will usually symlink to the last installed kernel.
Refer to the documentation for your distribution to find out about your boot chain and required images.
¹ Thanks to the ArchWiki community for all of the work they have done. The commands for creating the PK, creating the KEK, creating the DB, and signing the image are from Creating keys, authored by the ArchWiki Maintenance Team and/or the ArchWiki contributors.
#### Task 2 - Option A: Add keys to the variable store from within the instance After you have created the three key pairs, you can connect to your instance and add the keys to the variable store from within the instance by completing the following steps. Alternatively, complete the steps in the section called "Task 2 - Option B: Create a binary blob containing a pre- filled variable store".
Option A steps:
- Step 1: Launch an instance that will support UEFI Secure Boot
- Step 2: Configure an instance to support UEFI Secure Boot
- Step 3: Create an AMI from the instance

##### Step 1: Launch an instance that will support UEFI Secure Boot When you launch an instance with the following prerequisites, the instance will then be ready to be configured to support UEFI Secure Boot. You can only enable support for UEFI Secure Boot on an instance at launch; you can't enable it later.
Prerequisites
- AMI – The Linux AMI must support UEFI boot mode. To verify that the AMI supports UEFI boot mode, the AMI boot mode parameter must be uefi. For more information, see Determine the boot mode parameter of an Amazon EC2 AMI.
Note that AWS only provides Linux AMIs configured to support UEFI for Graviton-based instance types. AWS currently does not provide x86_64 Linux AMIs that support UEFI boot mode. You can configure your own AMI to support UEFI boot mode for all architectures. To configure your own AMI to support UEFI boot mode, you must perform a number of configuration steps on your own AMI. For more information, see Set the boot mode of an Amazon EC2 AMI.
- Instance type – All virtualized instance types that support UEFI also support UEFI Secure Boot.
Bare metal instance types do not support UEFI Secure Boot. For the instance types that support UEFI Secure Boot, see Requirements for UEFI boot mode.
- Launch your instance after the release of UEFI Secure Boot. Only instances launched after May 10, 2022 (when UEFI Secure Boot was released) can support UEFI Secure Boot.
After you've launched your instance, you can verify that it is ready to be configured to support UEFI Secure Boot (in other words, you can proceed to Step 2) by checking whether UEFI data is present.
The presence of UEFI data indicates that non-volatile data is persisted.
To verify whether your instance is ready for Step 2 Use the get-instance-uefi-data command and specify the instance ID. aws ec2 get-instance-uefi-data --instance-id i-1234567890abcdef0 The instance is ready for Step 2 if UEFI data is present in the output. If the output is empty, the instance cannot be configured to support UEFI Secure Boot. This can happen if your instance was launched before UEFI Secure Boot support became available. Launch a new instance and try again.

##### Step 2: Configure an instance to support UEFI Secure Boot
###### Enroll the key pairs in your UEFI variable store on the instance Warning You must sign your boot images after you enroll the keys, otherwise you won't be able to boot your instance.
After you create the signed UEFI signature lists (PK, KEK, and db), they must be enrolled into the UEFI firmware.
Writing to the PK variable is possible only if:
- No PK is enrolled yet, which is indicated if the SetupMode variable is 1. Check this by using the following command. The output is either 1 or 0. efivar -d -n 8be4df61-93ca-11d2-aa0d-00e098032b8c-SetupMode
- The new PK is signed by the private key of the existing PK.
To enroll the keys in your UEFI variable store The following commands must be run on the instance.
If SetupMode is enabled (the value is 1), the keys can be enrolled by running the following commands on the instance:
[ec2-user ~]$ efi-updatevar -f db.auth db [ec2-user ~]$ efi-updatevar -f KEK.auth KEK [ec2-user ~]$ efi-updatevar -f PK.auth PK To verify that UEFI Secure Boot is enabled To verify that UEFI Secure Boot is enabled, follow the steps in Verify whether an Amazon EC2 instance is enabled for UEFI Secure Boot.

You can now export your UEFI variable store with the get-instance-uefi-data CLI command, or you continue to the next step and sign your boot images to reboot into a UEFI Secure Boot-enabled instance.
##### Step 3: Create an AMI from the instance To create an AMI from the instance, you can use the console or the CreateImage API, CLI, or SDKs.
For the console instructions, see Create an Amazon EBS-backed AMI. For the API instructions, see CreateImage.
Note The CreateImage API automatically copies the UEFI variable store of the instance to the AMI. The console uses the CreateImage API. After you launch instances using this AMI, the instances will have the same UEFI variable store.
#### Task 2 - Option B: Create a binary blob containing a pre-filled variable store After you have created the three key pairs, you can create a binary blob containing a pre-filled variable store containing the UEFI Secure Boot keys. Alternatively, complete the steps in the section called "Task 2 - Option A: Add keys to the variable store from within the instance".
Warning You must sign your boot images before you enroll the keys, otherwise you won't be able to boot your instance.
Option B steps:
- Step 1: Create a new variable store or update an existing one
- Step 2: Upload the binary blob on AMI creation
##### Step 1: Create a new variable store or update an existing one You can create the variable store offline without a running instance by using the python-uefivars tool. The tool can create a new variable store from your keys. The script currently supports the EDK2 format, the AWS format, and a JSON representation that is easier to edit with higher-level tooling.

To create the variable store offline without a running instance
1. Download the tool at the following link. https://github.com/awslabs/python-uefivars
2. Create a new variable store from your keys by running the following command. This will create a base64-encoded binary blob in your_binary_blob.bin. The tool also supports updating a binary blob via the -I parameter.
./uefivars.py -i none -o aws -O your_binary_blob.bin -P PK.esl -K KEK.esl --db db.esl --dbx dbx.esl
##### Step 2: Upload the binary blob on AMI creation Use register-image to pass your UEFI variable store data. For the --uefi-data parameter, specify your binary blob, and for the --boot-mode parameter, specify uefi. aws ec2 register-image \ --name uefi_sb_tpm_register_image_test \ --uefi-data $(cat your_binary_blob.bin) \ --block-device-mappings "DeviceName=/dev/sda1,Ebs= {SnapshotId=snap-0123456789example,DeleteOnTermination=true}" \ --architecture x86_64 \ --root-device-name /dev/sda1 \ --virtualization-type hvm \ --ena-support \ --boot-mode uefi
### Create the AWS binary blob for UEFI Secure Boot You can use the following steps to customize the UEFI Secure Boot variables during AMI creation.
The KEK that is used in these steps is current as of September 2021. If Microsoft updates the KEK, you must use the latest KEK.
To create the AWS binary blob
1. Create an empty PK signature list. touch empty_key.crt

cert-to-efi-sig-list empty_key.crt PK.esl
2. Download the KEK certificates. https://go.microsoft.com/fwlink/?LinkId=321185
3. Wrap the KEK certificates in a UEFI signature list (siglist). sbsiglist --owner 77fa9abd-0359-4d32-bd60-28f4e78f784b --type x509 --output MS_Win_KEK.esl MicCorKEKCA2011_2011-06-24.crt
4. Download Microsoft's db certificates. https://www.microsoft.com/pkiops/certs/MicWinProPCA2011_2011-10-19.crt https://www.microsoft.com/pkiops/certs/MicCorUEFCA2011_2011-06-27.crt
5. Generate the db signature list. sbsiglist --owner 77fa9abd-0359-4d32-bd60-28f4e78f784b --type x509 --output MS_Win_db.esl MicWinProPCA2011_2011-10-19.crt sbsiglist --owner 77fa9abd-0359-4d32-bd60-28f4e78f784b --type x509 --output MS_UEFI_db.esl MicCorUEFCA2011_2011-06-27.crt cat MS_Win_db.esl MS_UEFI_db.esl > MS_db.esl
6. The Unified Extensible Firmware Interface Forum no longer provides the DBX files. They are now provided by Microsoft on GitHub. Download the latest DBX update from the Microsoft Secure Boot updates repository at  https://github.com/microsoft/secureboot_objects.
7. Unpack the signed update-binary.
Create SplitDbxContent.ps1 with the script content below. Alternatively, you can install the script from  PowerShell Gallery using Install-Script -Name SplitDbxContent.
<#PSScriptInfo

.VERSION 1.0

.GUID ec45a3fc-5e87-4d90-b55e-bdea083f732d

.AUTHOR Microsoft Secure Boot Team

.COMPANYNAME Microsoft


.COPYRIGHT Microsoft

.TAGS Windows Security

.LICENSEURI

.PROJECTURI

.ICONURI

.EXTERNALMODULEDEPENDENCIES

.REQUIREDSCRIPTS

.EXTERNALSCRIPTDEPENDENCIES

.RELEASENOTES Version 1.0: Original published version.

#>
<# .DESCRIPTION Splits a DBX update package into the new DBX variable contents and the signature authorizing the change.
 To apply an update using the output files of this script, try:
 Set-SecureBootUefi -Name dbx -ContentFilePath .\content.bin -SignedFilePath .
\signature.p7 -Time 2010-03-06T19:17:21Z -AppendWrite'
.EXAMPLE .\SplitDbxAuthInfo.ps1 DbxUpdate_x64.bin
#>
# Get file from script input $file  = Get-Content -Encoding Byte $args[0]
# Identify file signature $chop = $file[40..($file.Length - 1)] if (($chop[0] -ne 0x30) -or ($chop[1] -ne 0x82 )) { Write-Error "Cannot find signature" exit 1 }
# Signature is known to be ASN size plus header of 4 bytes

$sig_length = ($chop[2] * 256) + $chop[3] + 4 $sig = $chop[0..($sig_length - 1)] if ($sig_length -gt ($file.Length + 40)) { Write-Error "Signature longer than file size!" exit 1 }
# Content is everything else $content = $file[0..39] + $chop[$sig_length..($chop.Length - 1)]
# Write signature and content to files Set-Content -Encoding Byte signature.p7 $sig Set-Content -Encoding Byte content.bin $content Use the script to unpack the signed DBX files.
PS C:\Windows\system32> SplitDbxContent.ps1 .\dbx.bin This produces two files — signature.p7 and content.bin. Use content.bin in the next step.
8. Build a UEFI variable store using the uefivars.py script.
./uefivars.py -i none -o aws -O uefiblob-microsoft-keys-empty-pk.bin -P ~/PK.esl -K ~/MS_Win_KEK.esl --db ~/MS_db.esl  --dbx ~/content.bin
9. Check the binary blob and the UEFI variable store.
./uefivars.py -i aws -I uefiblob-microsoft-keys-empty-pk.bin -o json | less
10. You can update the blob by passing it to the same tool again.
./uefivars.py -i aws -I uefiblob-microsoft-keys-empty-pk.bin -o aws -O uefiblob- microsoft-keys-empty-pk.bin -P ~/PK.esl -K ~/MS_Win_KEK.esl --db ~/MS_db.esl  --dbx ~/content.bin Expected output Replacing PK Replacing KEK
