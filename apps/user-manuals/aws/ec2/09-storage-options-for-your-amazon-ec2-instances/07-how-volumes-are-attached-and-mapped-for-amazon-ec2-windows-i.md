# How volumes are attached and mapped for Amazon EC2 Windows instances

Source: apps/user-manuals/aws/ec2-ug.pdf

---

swap The ami device is the root volume as seen by the instance. The instance store volumes are named ephemeral[0-23]. The swap device is for the page file. If you've also mapped EBS volumes, they appear as ebs1, ebs2, and so on.
To get details about an individual block device in the block device mapping, append its name to the previous query, as shown here.
PS C:\> Invoke-RestMethod -uri http://169.254.169.254/latest/meta-data/block-device- mapping/ephemeral0
# How volumes are attached and mapped for Amazon EC2 Windows instances Windows instances Note This topic applies to Windows instances only.
Your Windows instance comes with an EBS volume that serves as the root volume. If your Windows instance uses AWS PV or Citrix PV drivers, you can optionally add up to 25 volumes, making a total of 26 volumes. For more information, see Amazon EBS volume limits for Amazon EC2 instances.
Depending on the instance type of your instance, you'll have from 0 to 24 possible instance store volumes available to the instance. To use any of the instance store volumes that are available to your instance, you must specify them when you create your AMI or launch your instance. You can also add EBS volumes when you create your AMI or launch your instance, or attach them while your instance is running.
When you add a volume to your instance, you specify the device name that Amazon EC2 uses. For more information, see Device names for volumes on Amazon EC2 instances. AWS Windows Amazon Machine Images (AMIs) contain a set of drivers that are used by Amazon EC2 to map instance store and EBS volumes to Windows disks and drive letters.
Methods to map disks to EBS volumes
- Map NVMe disks on Amazon EC2 Windows instance to volumes

- Map non-NVMe disks on Amazon EC2 Windows instance to volumes
## Map NVMe disks on Amazon EC2 Windows instance to volumes With Nitro-based instances, EBS volumes are exposed as NVMe devices. This topic explains how to view the NVMe disks that are available to the Windows operating system on your instance. It also shows how to map those NVMe disks to the underlying Amazon EBS volumes and the device names specified for the block device mappings used by Amazon EC2.
Topics
- List NVMe disks
- Map NVMe disks to volumes
### List NVMe disks You can find the disks on your Windows instance using Disk Management or Powershell.
Disk Management To find the disks on your Windows instance
1. Log in to your Windows instance using Remote Desktop. For more information, see Connect to your Windows instance using RDP.
2. Start the Disk Management utility.
3. Review the disks. The root volume is an EBS volume mounted as C:\. If there are no other disks shown, then you didn't specify additional volumes when you created the AMI or launched the instance.
The following is an example that shows the disks that are available if you launch an r5d.4xlarge instance with two additional EBS volumes.

PowerShell The following PowerShell script lists each disk and its corresponding device name and volume.
It is intended for use with Nitro-based instances, which use NVMe EBS and instance store volumes.

Connect to your Windows instance and run the following command to enable PowerShell script execution.
Set-ExecutionPolicy RemoteSigned Copy the following script and save it as mapping.ps1 on your Windows instance.
# List the disks for NVMe volumes function Get-EC2InstanceMetadata { param([string]$Path)
    (Invoke-WebRequest -Uri "http://169.254.169.254/latest/$Path").Content } function GetEBSVolumeId { param($Path)
    $SerialNumber = (Get-Disk -Path $Path).SerialNumber if($SerialNumber -clike 'vol*'){ $EbsVolumeId = $SerialNumber.Substring(0,20).Replace("vol","vol-")
    } else { $EbsVolumeId = $SerialNumber.Substring(0,20).Replace("AWS","AWS-")
    } return $EbsVolumeId } function GetDeviceName{ param($EbsVolumeId) if($EbsVolumeId -clike 'vol*'){

        $Device  = ((Get-EC2Volume -VolumeId $EbsVolumeId ).Attachment).Device $VolumeName = ""
    } else { $Device = "Ephemeral"
        $VolumeName = "Temporary Storage"
    } Return $Device,$VolumeName } function GetDriveLetter{ param($Path)
    $DiskNumber =  (Get-Disk -Path $Path).Number

    if($DiskNumber -eq 0){ $VirtualDevice = "root"
        $DriveLetter = "C"
        $PartitionNumber = (Get-Partition -DriveLetter C).PartitionNumber } else { $VirtualDevice = "N/A"
        $DriveLetter = (Get-Partition -DiskNumber $DiskNumber).DriveLetter if(!$DriveLetter)
        { $DriveLetter = ((Get-Partition -DiskId $Path).AccessPaths).Split(",")[0]
        } $PartitionNumber = (Get-Partition -DiskId $Path).PartitionNumber }

    return $DriveLetter,$VirtualDevice,$PartitionNumber } $Report = @() foreach($Path in (Get-Disk).Path)
{ $Disk_ID = ( Get-Partition -DiskId $Path).DiskId $Disk = ( Get-Disk -Path $Path).Number $EbsVolumeId  = GetEBSVolumeId($Path)
    $Size =(Get-Disk -Path $Path).Size $DriveLetter,$VirtualDevice, $Partition = (GetDriveLetter($Path))
    $Device,$VolumeName = GetDeviceName($EbsVolumeId)
    $Disk = New-Object PSObject -Property @{ Disk          = $Disk Partitions    = $Partition DriveLetter   = $DriveLetter EbsVolumeId   = $EbsVolumeId Device        = $Device VirtualDevice = $VirtualDevice VolumeName= $VolumeName } $Report += $Disk } $Report | Sort-Object Disk | Format-Table -AutoSize -Property Disk, Partitions, DriveLetter, EbsVolumeId, Device, VirtualDevice, VolumeName

Run the script as follows:
PS C:\> .\mapping.ps1 The following is example output for an instance with a root volume, two EBS volumes, and two instance store volumes.
Disk Partitions DriveLetter EbsVolumeId           Device    VirtualDevice VolumeName ---- ---------- ----------- -----------           ------    ------------- ---------- 0          1 C           vol-03683f1d861744bc7 /dev/sda1 root 1          1 D           vol-082b07051043174b9 xvdb      N/A 2          1 E           vol-0a4064b39e5f534a2 xvdc      N/A 3          1 F           AWS-6AAD8C2AEEE1193F0 Ephemeral N/A           Temporary Storage 4          1 G           AWS-13E7299C2BD031A28 Ephemeral N/A           Temporary Storage If you did not configure your credentials for Tools for Windows PowerShell on the Windows instance, the script cannot get the EBS volume ID and uses N/A in the EbsVolumeId column.
### Map NVMe disks to volumes You can use the  Get-Disk command to map Windows disk numbers to Amazon EBS volumes and Amazon EC2 instance store volumes.
PS C:\> Get-Disk Number Friendly Name Serial Number                    HealthStatus OperationalStatus      Total Size Partition

                      Style ------ ------------- -------------                    ------------ -----------------      ---------- ---------- 3      NVMe Amazo... AWS6AAD8C2AEEE1193F0_00000001.   Healthy              Online 279.4 GB MBR 4      NVMe Amazo... AWS13E7299C2BD031A28_00000001.   Healthy              Online 279.4 GB MBR 2      NVMe Amazo... vol0a4064b39e5f534a2_00000001.   Healthy              Online 8 GB MBR 0      NVMe Amazo... vol03683f1d861744bc7_00000001.   Healthy              Online 30 GB MBR

1      NVMe Amazo... vol082b07051043174b9_00000001.   Healthy              Online 8 GB MBR You can also run the ebsnvme-id command to map NVMe disk numbers to EBS volume IDs and device names.
PS C:\> C:\PROGRAMDATA\Amazon\Tools\ebsnvme-id.exe Disk Number: 0 Volume ID: vol-03683f1d861744bc7 Device Name: sda1 Disk Number: 1 Volume ID: vol-082b07051043174b9 Device Name: xvdb Disk Number: 2 Volume ID: vol-0a4064b39e5f534a2 Device Name: xvdc
## Map non-NVMe disks on Amazon EC2 Windows instance to volumes For instances launched from a Windows AMI that uses AWS PV or Citrix PV drivers, you can use the relationships described on this page to map your Windows disks to your instance store and EBS volumes. This topic explains how to view the non-NVMe disks that are available to the Windows operating system on your instance. It also shows how to map those non-NVMe disks to the underlying Amazon EBS volumes and the device names specified for the block device mappings used by Amazon EC2.
Note If you launch an instance If your Windows AMI uses Red Hat PV drivers, you can update your instance to use the Citrix drivers. For more information, see the section called "Upgrade PV drivers".
Topics
- List non-NVMe disks
- Map non-NVMe disks to volumes

### List non-NVMe disks You can find the disks on your Windows instance using Disk Management or PowerShell.
Disk Management To find the disks on your Windows instance
1. Log in to your Windows instance using Remote Desktop. For more information, see Connect to your Windows instance using RDP.
2. Start the Disk Management utility.
On the taskbar, right-click the Windows logo, and then choose Disk Management.
3. Review the disks. The root volume is an EBS volume mounted as C:\. If there are no other disks shown, then you didn't specify additional volumes when you created the AMI or launched the instance.
The following is an example that shows the disks that are available if you launch an m3.medium instance with an instance store volume (Disk 2) and an additional EBS volume (Disk 1).

4. Right-click the gray pane labeled Disk 1, and then select Properties. Note the value of Location and look it up in the tables in Map non-NVMe disks to volumes. For example, the following disk has the location Bus Number 0, Target Id 9, LUN 0. According to the table for EBS volumes, the device name for this location is xvdj.

PowerShell The following PowerShell script lists each disk and its corresponding device name and volume.
Requirements and limitations
- Requires Windows Server 2012 or later.
- Requires credentials to get the EBS volume ID. You can configure a profile using the Tools for PowerShell, or attach an IAM role to the instance.
- Does not support NVMe volumes.
- Does not support dynamic disks.
Connect to your Windows instance and run the following command to enable PowerShell script execution.
Set-ExecutionPolicy RemoteSigned

Copy the following script and save it as mapping.ps1 on your Windows instance.
# List the disks function Convert-SCSITargetIdToDeviceName { param([int]$SCSITargetId)
  If ($SCSITargetId -eq 0) { return "sda1"
  } $deviceName = "xvd"
  If ($SCSITargetId -gt 25) { $deviceName += [char](0x60 + [int]($SCSITargetId / 26))
  } $deviceName += [char](0x61 + $SCSITargetId % 26) return $deviceName } [string[]]$array1 = @()
[string[]]$array2 = @()
[string[]]$array3 = @()
[string[]]$array4 = @()
Get-WmiObject Win32_Volume | Select-Object Name, DeviceID | ForEach-Object { $array1 += $_.Name $array2 += $_.DeviceID } $i = 0 While ($i -ne ($array2.Count)) { $array3 += ((Get-Volume -Path $array2[$i] | Get-Partition | Get- Disk).SerialNumber) -replace "_[^ ]*$" -replace "vol", "vol-"
  $array4 += ((Get-Volume -Path $array2[$i] | Get-Partition | Get- Disk).FriendlyName)
  $i ++ } [array[]]$array = $array1, $array2, $array3, $array4 Try { $InstanceId = Get-EC2InstanceMetadata -Category "InstanceId"
  $Region = Get-EC2InstanceMetadata -Category "Region" | Select-Object - ExpandProperty SystemName } Catch {

  Write-Host "Could not access the instance Metadata using AWS Get- EC2InstanceMetadata CMDLet.
Verify you have AWSPowershell SDK version '3.1.73.0' or greater installed and Metadata is enabled for this instance." -ForegroundColor Yellow } Try { $BlockDeviceMappings = (Get-EC2Instance -Region $Region -Instance $InstanceId).Instances.BlockDeviceMappings $VirtualDeviceMap = (Get-EC2InstanceMetadata -Category "BlockDeviceMapping").GetEnumerator() | Where-Object { $_.Key -ne "ami" } } Catch { Write-Host "Could not access the AWS API, therefore, VolumeId is not available.
Verify that you provided your access keys or assigned an IAM role with adequate permissions." -ForegroundColor Yellow } Get-disk | ForEach-Object { $DriveLetter = $null $VolumeName = $null $VirtualDevice = $null $DeviceName = $_.FriendlyName $DiskDrive = $_ $Disk = $_.Number $Partitions = $_.NumberOfPartitions $EbsVolumeID = $_.SerialNumber -replace "_[^ ]*$" -replace "vol", "vol-" if ($Partitions -ge 1) { $PartitionsData = Get-Partition -DiskId $_.Path $DriveLetter = $PartitionsData.DriveLetter | Where-object { $_ -notin @("", $null) } $VolumeName = (Get-PSDrive | Where-Object { $_.Name -in @($DriveLetter) }).Description | Where-object { $_ -notin @("", $null) } } If ($DiskDrive.path -like "*PROD_PVDISK*") { $BlockDeviceName = Convert-SCSITargetIdToDeviceName((Get-WmiObject -Class Win32_Diskdrive | Where-Object { $_.DeviceID -eq ("\\.\PHYSICALDRIVE" + $DiskDrive.Number) }).SCSITargetId)
    $BlockDeviceName = "/dev/" + $BlockDeviceName $BlockDevice = $BlockDeviceMappings | Where-Object { $BlockDeviceName -like "*"
 + $_.DeviceName + "*" } $EbsVolumeID = $BlockDevice.Ebs.VolumeId $VirtualDevice = ($VirtualDeviceMap.GetEnumerator() | Where-Object { $_.Value - eq $BlockDeviceName }).Key | Select-Object -First 1

  } ElseIf ($DiskDrive.path -like "*PROD_AMAZON_EC2_NVME*") { $BlockDeviceName = (Get-EC2InstanceMetadata -Category "BlockDeviceMapping")."ephemeral$((Get-WmiObject -Class Win32_Diskdrive | Where- Object { $_.DeviceID -eq ("\\.\PHYSICALDRIVE" + $DiskDrive.Number) }).SCSIPort - 2)"
    $BlockDevice = $null $VirtualDevice = ($VirtualDeviceMap.GetEnumerator() | Where-Object { $_.Value - eq $BlockDeviceName }).Key | Select-Object -First 1 } ElseIf ($DiskDrive.path -like "*PROD_AMAZON*") { if ($DriveLetter -match '[^a-zA-Z0-9]') { $i = 0 While ($i -ne ($array3.Count)) { if ($array[2][$i] -eq $EbsVolumeID) { $DriveLetter = $array[0][$i]
          $DeviceName = $array[3][$i]
        } $i ++ } } $BlockDevice = ""
    $BlockDeviceName = ($BlockDeviceMappings | Where-Object { $_.ebs.VolumeId -eq $EbsVolumeID }).DeviceName } ElseIf ($DiskDrive.path -like "*NETAPP*") { if ($DriveLetter -match '[^a-zA-Z0-9]') { $i = 0 While ($i -ne ($array3.Count)) { if ($array[2][$i] -eq $EbsVolumeID) { $DriveLetter = $array[0][$i]
          $DeviceName = $array[3][$i]
        } $i ++ } } $EbsVolumeID = "FSxN Volume"
    $BlockDevice = ""
    $BlockDeviceName = ($BlockDeviceMappings | Where-Object { $_.ebs.VolumeId -eq $EbsVolumeID }).DeviceName } Else { $BlockDeviceName = $null $BlockDevice = $null }

  New-Object PSObject -Property @{ Disk          = $Disk; Partitions    = $Partitions; DriveLetter   = If ($DriveLetter -eq $null) { "N/A" } Else { $DriveLetter }; EbsVolumeId   = If ($EbsVolumeID -eq $null) { "N/A" } Else { $EbsVolumeID }; Device        = If ($BlockDeviceName -eq $null) { "N/A" } Else { $BlockDeviceName }; VirtualDevice = If ($VirtualDevice -eq $null) { "N/A" } Else { $VirtualDevice }; VolumeName    = If ($VolumeName -eq $null) { "N/A" } Else { $VolumeName }; DeviceName    = If ($DeviceName -eq $null) { "N/A" } Else { $DeviceName }; } } | Sort-Object Disk | Format-Table -AutoSize -Property Disk, Partitions, DriveLetter, EbsVolumeId, Device, VirtualDevice, DeviceName, VolumeName Run the script as follows:
PS C:\> .\mapping.ps1 The following is example output.
Disk  Partitions  DriveLetter   EbsVolumeId             Device      VirtualDevice DeviceName              VolumeName ----  ----------  -----------   -----------             ------      ------------- ----------              ---------- 0           1            C   vol-0561f1783298efedd   /dev/sda1   N/A NVMe Amazon Elastic B   N/A 1           1            D   vol-002a9488504c5e35a   xvdb        N/A NVMe Amazon Elastic B   N/A 2           1            E   vol-0de9d46fcc907925d   xvdc        N/A NVMe Amazon Elastic B   N/A If you did not provide your credentials on the Windows instance, the script cannot get the EBS volume ID and uses N/A in the EbsVolumeId column.
### Map non-NVMe disks to volumes The block device driver for the instance assigns the actual volume names when mounting volumes.
Mappings
- Instance store volumes

- EBS volumes
#### Instance store volumes The following table describes how the Citrix PV and AWS PV drivers map non-NVMe instance store volumes to Windows volumes. The number of available instance store volumes is determined by the instance type. For more information, see Instance store volume limits for EC2 instances.
Location Device name Bus Number 0, Target ID 78, LUN 0 xvdca Bus Number 0, Target ID 79, LUN 0 xvdcb Bus Number 0, Target ID 80, LUN 0 xvdcc Bus Number 0, Target ID 81, LUN 0 xvdcd Bus Number 0, Target ID 82, LUN 0 xvdce Bus Number 0, Target ID 83, LUN 0 xvdcf Bus Number 0, Target ID 84, LUN 0 xvdcg Bus Number 0, Target ID 85, LUN 0 xvdch Bus Number 0, Target ID 86, LUN 0 xvdci Bus Number 0, Target ID 87, LUN 0 xvdcj Bus Number 0, Target ID 88, LUN 0 xvdck Bus Number 0, Target ID 89, LUN 0 xvdcl
#### EBS volumes The following table describes how the Citrix PV and AWS PV drivers map non-NVME EBS volumes to Windows volumes.

Location Device name Bus Number 0, Target ID 0, LUN 0 /dev/sda1 Bus Number 0, Target ID 1, LUN 0 xvdb Bus Number 0, Target ID 2, LUN 0 xvdc Bus Number 0, Target ID 3, LUN 0 xvdd Bus Number 0, Target ID 4, LUN 0 xvde Bus Number 0, Target ID 5, LUN 0 xvdf Bus Number 0, Target ID 6, LUN 0 xvdg Bus Number 0, Target ID 7, LUN 0 xvdh Bus Number 0, Target ID 8, LUN 0 xvdi Bus Number 0, Target ID 9, LUN 0 xvdj Bus Number 0, Target ID 10, LUN 0 xvdk Bus Number 0, Target ID 11, LUN 0 xvdl Bus Number 0, Target ID 12, LUN 0 xvdm Bus Number 0, Target ID 13, LUN 0 xvdn Bus Number 0, Target ID 14, LUN 0 xvdo Bus Number 0, Target ID 15, LUN 0 xvdp Bus Number 0, Target ID 16, LUN 0 xvdq Bus Number 0, Target ID 17, LUN 0 xvdr Bus Number 0, Target ID 18, LUN 0 xvds Bus Number 0, Target ID 19, LUN 0 xvdt
