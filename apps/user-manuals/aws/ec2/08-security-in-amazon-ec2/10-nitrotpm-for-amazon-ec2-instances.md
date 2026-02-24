# NitroTPM for Amazon EC2 instances

Source: apps/user-manuals/aws/ec2-ug.pdf

---

# NitroTPM for Amazon EC2 instances Nitro Trusted Platform Module (NitroTPM) is a virtual device that is provided by the AWS Nitro System and conforms to the TPM 2.0 specification. It securely stores artifacts (such as passwords, certificates, or encryption keys) that are used to authenticate the instance. NitroTPM can generate keys and use them for cryptographic functions (such as hashing, signing, encryption, and decryption).
NitroTPM provides measured boot, a process where the bootloader and operating system create cryptographic hashes of every boot binary and combine them with the previous values in NitroTPM internal Platform Configuration Registers (PCRs). With measured boot, you can obtain signed PCR values from NitroTPM and use them to prove to remote entities the integrity of the instance's boot software. This is known as remote attestation.
With NitroTPM, keys and secrets can be tagged with a specific PCR value so that they can never be accessed if the value of the PCR, and thus the instance integrity, changes. This special form of conditional access is referred to as sealing and unsealing. Operating system technologies, like BitLocker, can use NitroTPM to seal a drive decryption key so that the drive can only be decrypted when the operating system has booted correctly and is in a known good state.
To use NitroTPM, you must select an Amazon Machine Image (AMI) that has been configured for NitroTPM support, and then use the AMI to launch Nitro-based instances. You can select one of Amazon's prebuilt AMIs or create one yourself.
Pricing There is no additional cost for using NitroTPM. You pay only for the underlying resources that you use.
Contents
- Requirements for using NitroTPM with Amazon EC2 instances
- Enable a Linux AMI for NitroTPM
- Verify that an AMI is enabled for NitroTPM
- Enable or stop using NitroTPM on an Amazon EC2 instance
- Verify that an Amazon EC2 instance is enabled for NitroTPM
- Retrieve the public endorsement key for an EC2 instance

## Requirements for using NitroTPM with Amazon EC2 instances To launch an instance with NitroTPM enabled, you must meet the following requirements.
Topics
- AMIs
- Instance types
- Considerations
### AMIs The AMI must have NitroTPM enabled.
Linux AMIs There are no preconfigured AMIs. You must configure your own AMI. For more information, see Enable a Linux AMI for NitroTPM.
Windows AMIs To find an AWS Windows AMI that's preconfigured for NitroTPM and UEFI Secure Boot with Microsoft keys, see Find Windows Server AMIs configured with NitroTPM and UEFI Secure Boot in the AWS Windows AMIs Reference.
Note Operating system — The AMI must include an operating system with a TPM 2.0 Command Response Buffer (CRB) driver. Most current operating systems include a TPM 2.0 CRB driver.
UEFI boot mode — The AMI must be configured for UEFI boot mode. For more information, see UEFI Secure Boot for Amazon EC2 instances.
### Instance types You must use one of the following virtualized instance types:
- General purpose: M5, M5a, M5ad, M5d, M5dn, M5n, M5zn, M6a, M6g, M6gd, M6i, M6id, M6idn, M6in, M7a, M7g, M7gd, M7i, M7i-flex, M8a, M8azn, M8g, M8gb, M8gd, M8gn, M8i, M8id, M8i- flex, T3, T3a, T4g

- Compute optimized: C5, C5a, C5ad, C5d, C5n, C6a, C6g, C6gd, C6gn, C6i, C6id, C6in, C7a, C7g, C7gd, C7gn, C7i, C7i-flex, C8a, C8g, C8gb, C8gd, C8gn, C8i, C8id, C8i-flex
- Memory optimized: R5, R5a, R5ad, R5b, R5d, R5dn, R5n, R6a, R6g, R6gd, R6i, R6id, R6idn, R6in, R7a, R7g, R7gd, R7i, R7iz, R8a, R8g, R8gb, R8gd, R8gn, R8i, R8id, R8i-flex, U7i-6tb, U7i-8tb, U7i-12tb, U7in-16tb, U7in-24tb, U7in-32tb, X2idn, X2iedn, X2iezn, X8g, X8aedz, X8i, z1d
- Storage optimized: D3, D3en, I3en, I4i, I7i, I7ie, I8g, I8ge, Im4gn
- Accelerated computing: F2, G4dn, G5, G6, G6e, G6f, Gr6, Gr6f, G7e, Inf1, Inf2, P5, P5e, P5en, P6- B200, P6-B300, Trn2, Trn2u
- High-performance computing: Hpc6a, Hpc6id, Hpc8a
### Considerations The following considerations apply when using NitroTPM:
- After you launch an instance using an AMI with NitroTPM enabled, if you want to change the instance type, the new instance type that you choose must also support NitroTPM.
- BitLocker volumes that are encrypted with NitroTPM-based keys can only be used on the original instance.
- The NitroTPM state is not displayed in the Amazon EC2 console.
- The NitroTPM state is not included in Amazon EBS snapshots.
- The NitroTPM state is not included in VM Import/Export images.
- NitroTPM is not supported on AWS Outposts., Local Zones, or Wavelength Zones.
## Enable a Linux AMI for NitroTPM To enable NitroTPM for an instance, you must launch the instance using an AMI with NitroTPM enabled. You must configure your Linux AMI with NitroTPM support when you register it. You can't configure NitroTPM support later on.
For the list of Windows AMIs that are preconfigured for NitroTPM support, see Requirements for using NitroTPM with Amazon EC2 instances.
You must create an AMI with NitroTPM configured by using the RegisterImage API. You can't use the Amazon EC2 console or VM Import/Export.

To enable a Linux AMI for NitroTPM
1. Launch a temporary instance with your required Linux AMI. Note the ID of its root volume, which you can find in the console on the Storage tab for the instance.
2. After the instance reaches the running state, create a snapshot of the instance's root volume.
For more information, see Create a snapshot of an EBS volume.
3. Register the snapshot you created as an AMI. In the block device mapping, specify the snapshot that you created for the root volume.
The following is an example register-image command. For --tpm-support, specify v2.0. For --boot-mode, specify uefi. aws ec2 register-image \ --name my-image \ --boot-mode uefi \ --architecture x86_64 \ --root-device-name /dev/xvda \ --block-device-mappings DeviceName=/dev/ xvda,Ebs={SnapshotId=snap-0abcdef1234567890} \ --tpm-support v2.0 The following is an example for the Register-EC2Image cmdlet.
$block = @{SnapshotId=snap-0abcdef1234567890} Register-EC2Image `
    -Name my-image `
    -Architecture "x86_64" `
    -RootDeviceName /dev/xvda `
    -BlockDeviceMapping @{DeviceName="/dev/xvda";Ebs=$block} `
    -BootMode Uefi `
    -TpmSupport V20
4. Terminate the temporary instance that you launched in step 1.
## Verify that an AMI is enabled for NitroTPM To enable NitroTPM for an instance, you must launch the instance using an AMI with NitroTPM enabled. You can describe an image to verify that it is enabled for NitroTPM. If you are the AMI owner, you can describe the tpmSupport image attribute.

The Amazon EC2 console does not display TpmSupport.
AWS CLI To verify that NitroTPM is enabled Use the describe-images command. aws ec2 describe-images \ --image-ids ami-0abcdef1234567890 \ --query Images[*].TpmSupport If NitroTPM is enabled for the AMI, the output is as follows. If TPM is not enabled, the output is empty.
[ "v2.0"
]
Alternatively, if you are the AMI owner, you can use the describe-image-attribute command with the tpmSupport attribute. aws ec2 describe-image-attribute \ --image-id ami-0abcdef1234567890 \ --attribute tpmSupport The following is example output.
{ "ImageId": "ami-0abcdef1234567890", "TpmSupport": { "Value": "v2.0"
    } } To find AMIs with NitroTPM enabled The following example lists the IDs of the AMIs that you own with NitroTPM enabled. aws ec2 describe-images \ --owners self \

    --filters Name=tpm-support,Values=v2.0 \ --query Images[].ImageId PowerShell To verify that NitroTPM is enabled Use the Get-EC2Image cmdlet.
Get-EC2Image `
    -ImageId ami-0abcdef1234567890 | Select TpmSupport If NitroTPM is enabled for the AMI, the output is as follows. If TPM is not enabled, the output is empty.
TpmSupport
---------- v2.0 Alternatively, if you are the AMI owner, you can use the Get-EC2ImageAttribute cmdlet with the tpmSupport attribute.
Get-EC2ImageAttribute `
    -ImageId ami-0abcdef1234567890 `
    -Attribute tpmSupport To find AMIs with NitroTPM enabled The following example lists the IDs of the AMIs that you own with NitroTPM enabled.
Get-EC2Image `
    -Owner self `
    -Filter @{Name="tpm-support; Values="v2.0"} | Select ImageId
## Enable or stop using NitroTPM on an Amazon EC2 instance You can enable an Amazon EC2 instance for NitroTPM only at launch. Once an instance is enabled for NitroTPM, you can't disable it. If you no longer need to use NitroTPM, you must configure the operating system to stop using it.

Topics
- Launch an instance with NitroTPM enabled
- Stop using NitroTPM on an instance
### Launch an instance with NitroTPM enabled When you launch an instance with the  prerequisites, NitroTPM is automatically enabled on the instance. You can enable NitroTPM on an instance only at launch. For information about launching an instance, see Launch an Amazon EC2 instance.
### Stop using NitroTPM on an instance After launching an instance with NitroTPM enabled, you can't disable NitroTPM for the instance.
However, you can configure the operating system to stop using NitroTPM by disabling the TPM 2.0 device driver on the instance by using the following tools:
- For Linux instances, use tpm-tools.
- For Windows instances, use the TPM management console (tpm.msc).
For more information about disabling the device driver, see the documentation for your operating system.
## Verify that an Amazon EC2 instance is enabled for NitroTPM You can verify whether an Amazon EC2 instance is enabled for NitroTPM. If NitroTPM support is enabled on the instance, the command returns "v2.0". Otherwise, the TpmSupport field is not present in the output.
The Amazon EC2 console does not display the TpmSupport field.
AWS CLI To verify whether an instance is enabled for NitroTPM Use the describe-instances command. aws ec2 describe-instances \ --instance-ids i-1234567890abcdef0 \ --query Reservations[].Instances[].TpmSupport

PowerShell To verify whether an instance is enabled for NitroTPM Use the Get-EC2Instance cmdlet.
(Get-EC2Instance `
    -InstanceId i-1234567890abcdef0).Instances.TpmSupport
### Verify NitroTPM access on your Windows instance (Windows instances only) To verify whether the NitroTPM is accessible to Windows
1. Connect to your EC2 Windows instance.
2. On the instance, run the tpm.msc program.
The TPM Management on Local Computer window opens.
3. Check the TPM Manufacturer Information field. It contains the manufacturer's name and the version of the NitroTPM on the instance.
## Retrieve the public endorsement key for an EC2 instance You can securely retrieve the public endorsement key for an instance at any time.

AWS CLI To retrieve the public endorsement key for an instance Use the get-instance-tpm-ek-pub command.
Example 1 The following example gets the rsa-2048 public endorsement key in tpmt format for the specified instance. aws ec2 get-instance-tpm-ek-pub \ --instance-id i-1234567890abcdef0 \ --key-format tpmt \ --key-type rsa-2048 The following is the example output.
{ "InstanceId": "i-01234567890abcdef", "KeyFormat": "tpmt", "KeyType": "rsa-2048", "KeyValue": "AAEACwADALIAIINxl2dEhLEXAMPLEUal1yT9UtduBlILZPKh2hszFGmqAAYAgABDA EXAMPLEAAABAOiRd7WmgtdGNoV1h/AxmW+CXExblG8pEUfNm0LOLiYnEXAMPLERqApiFa/UhvEYqN4 Z7jKMD/usbhsQaAB1gKA5RmzuhSazHQkax7EXAMPLEzDthlS7HNGuYn5eG7qnJndRcakS+iNxT8Hvf 0S1ZtNuItMs+Yp4SO6aU28MT/JZkOKsXIdMerY3GdWbNQz9AvYbMEXAMPLEPyHfzgVO0QTTJVGdDxh vxtXCOu9GYf0crbjEXAMPLEd4YTbWdDdgOKWF9fjzDytJSDhrLAOUctNzHPCd/92l5zEXAMPLEOIFA Ss50C0/802c17W2pMSVHvCCa9lYCiAfxH/vYKovAAE="
} Example 2 The following example gets the rsa-2048 public endorsement key in der format for the specified instance. aws ec2 get-instance-tpm-ek-pub \ --instance-id i-1234567890abcdef0 \ --key-format der \ --key-type rsa-2048 The following is the example output.
{
