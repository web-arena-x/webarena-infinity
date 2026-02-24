# Amazon EC2 instance attestation

Source: apps/user-manuals/aws/ec2-ug.pdf

---

    "InstanceId": "i-1234567890abcdef0", "KeyFormat": "der", "KeyType": "rsa-2048", "KeyValue": "MIIBIjANBgEXAMPLEw0BAQEFAAOCAQ8AMIIBCgKCAQEA6JF3taEXAMPLEXWH8DGZb4 JcTFuUbykRR82bQs4uJifaKSOv5NGoEXAMPLEG8Rio3hnuMowP+6xuGxBoAHWAoDlGbO6FJrMdEXAMP LEnYUHvMO2GVLsc0a5ifl4buqcmd1FxqRL6I3FPwe9/REXAMPLE0yz5inhI7ppTbwxP8lmQ4qxch0x6 tjcZ1Zs1DP0EXAMPLERUYLQ/Id/OBU7RBNMlUZ0PGG/G1cI670Zh/RytuOdx9iEXAMPLEtZ0N2A4pYX 1+PMPK0lIOGssA5Ry03Mc8J3/3aXnOD2/ASRQ4gUBKznQLT/zTZEXAMPLEJUe8IJr2VgKIB/Ef+9gqi 8AAQIDAQAB"
} PowerShell To retrieve the public endorsement key for an instance Use the Get-EC2InstanceTpmEkPub cmdlet.
Example 1 The following example gets the rsa-2048 public endorsement key in tpmt format for the specified instance.
Get-EC2InstanceTpmEkPub `
    -InstanceId i-1234567890abcdef0 `
    -KeyFormat tpmt `
    -KeyType rsa-2048 Example 2 The following example gets the rsa-2048 public endorsement key in der format for the specified instance.
Get-EC2InstanceTpmEkPub `
    -InstanceId i-1234567890abcdef0 `
    -KeyFormat der `
    -KeyType rsa-2048
# Amazon EC2 instance attestation Attestation is a process that allows you to cryptographically prove to any party that only trusted software, drivers, and boot processes are running on an Amazon EC2 instance. Amazon EC2

instance attestation is powered by the Nitro Trusted Platform Module (NitroTPM) and Attestable AMIs.
The first step to attestation is to build an Attestable AMI and determine the reference measurements of that AMI. An Attestable AMI is an AMI built from the ground up for attestation.
The reference measurements are measurements of all of your software and configurations that you have included in your AMI. For more information about how you can obtain the reference measurements, see Build the sample image description.
The next step is to launch a Nitro-TPM enabled EC2 instance with the Attestable AMI. After you have launched the instance, you can use the  NitroTPM tools to generate the Attestation Document.
Then you can compare the actual measurements of your EC2 instance from the Attestation Document against the reference measurements to check if the instance has the software and configurations that you trust.
By comparing the reference measurements generated during the Attestable AMI creation process with the measurements included in an instance's Attestation Document, you can validate that only software and code that you trust are running on the instance.

## Integration with AWS KMS To make the process of comparing measurements easier, you can use AWS Key Management Service (AWS KMS) as a verifier for Attestation Documents. With AWS KMS, you can create attestation-based KMS key policies that allow specific operations with the KMS key only if you provide an Attestation Document with measurements that match the reference measurements.
To do this, you add specific condition keys to your KMS key policies that use the reference measurements as the condition key values, and then specify which KMS operations are allowed if the condition key is satisfied.
When you perform KMS operations using the KMS key, you must attach an Attestation Document to the KMS request. AWS KMS then validates the measurements from the Attestation Document against the reference measurements in the KMS key policy, and allows key access only if the measurements match.
Additionally, when you generate the Attestation Document for an instance, you must specify a public key for a key pair that you own. The specified public key is included in the Attestation Document. When AWS KMS validates the Attestation Document and allows a decryption operation, it automatically encrypts the response with the public key included in the Attestation Document before it is returned. This ensures that the response can be decrypted and used only with the matching private key for the public key included in the Attestation Document.
This ensures that only instances running trusted software and code can perform cryptographic operations using a KMS key.

## Attesting isolated compute environments In general, you can build and configure an EC2 instance to be an isolated compute environment, which provides no interactive access and no mechanism for your administrators and users to access the data that is being processed in the EC2 instance. With EC2 instance attestation you can prove to a third-party or service that your instance is running as an isolated compute environment. For more information, see Isolate data from your own operators.
For an example, see the sample Amazon Linux 2023 image description that creates an isolated compute environment. You can use this sample image description as a starting point and customize it to meet your requirements.
## AWS shared responsibility model NitroTPM and Attestable AMIs are building blocks that can help you to set up and configure attestation on your EC2 instances. You are responsible for configuring the AMI to meet your respective use case. For more information, see AWS Shared Responsibility Model.
Topics
- Attestable AMIs
- Prepare AWS KMS for attestation
- Get the NitroTPM Attestation Document
- Integrating with AWS KMS
- Isolate data from your own operators
## Attestable AMIs An Attestable AMI is an Amazon Machine Image (AMI) with a corresponding cryptographic hash that represents all of its contents. The hash is generated during the AMI creation process, and it is calculated based on the entire contents of that AMI, including the applications, code, and boot process.
### Maintaining an Attestable State An instance's measurements are based on its initial boot state. Any software or code changes made to the instance after launch and that persist after restarts will change the instance's measurement

after restarts. If the measurements are altered, they deviate from the reference measurements of the Attestable AMI, and the instance will no longer be able to successfully attest to AWS KMS after the instance restarts. Therefore, for Attestable AMIs to be useful, instances need to return to their original boot state after they restart.
Always returning to the original boot state ensures that an instance can successfully attest after it restarts. The following utilities can be used to ensure that your instances remain attestable after restarts:
- erofs — Enhanced Read-Only File System. This utility ensures that your root filesystem is read- only. With this utility, writes to the filesystem, including /etc, /run, and /var, are stored in memory and lost when the instance is restarted, leaving the root filesystem in its original launch state. For more information, see the erofs documentation.
- dm-verity — Provides integrity protection for the read-only root filesystem. The utility calculates a hash of the filesystem blocks and stores it in the kernel command line. This allows the kernel to verify the integrity of the filesystem during boot. For more information, see the dm-verity documentation.
### Requirements for creating Attestable AMIs Attestable AMIs have the following requirements:
- Base operating system – Amazon Linux 2023 and NixOS
- Architecture – x86_64 or arm64 architecture
- TPM support – NitroTPM must be enabled. For more information, see Requirements for using NitroTPM with Amazon EC2 instances.
- Boot mode – UEFI boot mode must be enabled.
Topics
- Creating Attestable AMIs
- Build the sample Amazon Linux 2023 image description
- Sample Amazon Linux 2023 image description
- Customize the sample Amazon Linux 2023 image description for your workload
- Compute PCR measurements for a custom AMI

### Creating Attestable AMIs To create an Attestable AMI, you will need to use Amazon Linux 2023 with KIWI Next Generation (KIWI NG). Amazon Linux 2023 provides all of the software and utilities needed to build an Attestable AMI using KIWI NG.
KIWI NG is an open-source tool for building pre-configured Linux-based images. KIWI NG uses XML image descriptions that define the contents of an image. The image description specifies the base operating system, software, kernel configuration, and scripts to run in order to build a ready-to-use AMI for a specific use case.
During AMI build time, you need to use the nitro-tpm-pcr-compute utility to generate the reference measurements based on the Unified Kernel Image (UKI) generated by KIWI NG. For more information about using the nitro-tpm-pcr-compute utility, see Compute PCR measurements for a custom AMI.
AWS provides a sample Amazon Linux 2023 image description that includes all configurations needed to configure an EC2 instance in an isolated compute environment. For more information, see Build the sample Amazon Linux 2023 image description.
### Build the sample Amazon Linux 2023 image description AWS provides a sample Amazon Linux 2023 image description that you can use as a starting point for creating your own custom Attestable AMIs for your workloads. The sample image description includes Amazon Linux 2023 as the base operating system, dm-verity and erofs configurations for filesystem immutability, and it removes all interactive access (such as SSH, EC2 instance connect, and serial console) to create an isolated compute environment. For more information about the sample image description, see the  Github repo.
The sample image description automatically installs the NitroTPM tools (nitro-tpm-pcr- compute and nitro-tpm-attest) in the built image in the /usr/bin/ directory. This ensures that the tools are preinstalled on instances launched from the AMI.
The sample image description includes a script, edit_boot_install.sh, which includes the commands needed to generate the reference measurements. The script mounts the raw disk image file (.raw) created by KIWI NG to a loopback device, locates the UKI, which has the .efi file extension, and then runs the nitro-tpm-pcr-compute utility to generate the reference measurements for the AMI. The script is automatically executed by KIWI NG during build time.
This tutorial shows you how to build the sample image description to create an Attestable AMI.

For more information about creating your own image descriptions, see the following KIWI NG documentation:
- Quick Start
- Image Description
- Sample Amazon Linux 2023 image description To build the sample Amazon Linux 2023 image description using KIWI NG
1. Launch an Amazon EC2 instance using the latest AL2023 AMI. To ensure that your instance has enough storage space to build the AMI, ensure that you provision at least 12 GB of storage.
2. Install the required dependencies. The following command installs the following utilities:
- kiwi-cli
- veritysetup
- erofs-utils
- aws-nitro-tpm-tools sudo dnf install -y kiwi-cli python3-kiwi kiwi-systemdeps-core python3-poetry-core qemu-img veritysetup erofs-utils git cargo aws-nitro-tpm-tools
3. Install the coldsnap utility. This utility enables you to create Amazon EBS snapshots from raw image data. You'll use this utility to create an EBS snapshot from the raw disk image file created by KIWI NG. git clone https://github.com/awslabs/coldsnap.git cd coldsnap cargo install --locked coldsnap cd ..
4. Get the sample image description files. sudo dnf install kiwi-image-descriptions-examples The sample image description files are downloaded to the following directory: /usr/share/ kiwi-image-descriptions-examples/al2023/attestable-image-example

5. Build the sample image description using the KIWI NG system build command. The following command creates a raw disk image file in the ./image directory. sudo kiwi-ng \ --color-output \ --loglevel 0 \ system build \ --description /usr/share/kiwi-image-descriptions-examples/al2023/attestable-image- example \ --target-dir ./image For more information, see the  kiwi-ng system build documentation.
6. Get the reference measurements for the AMI. The measurements are generated by the nitro- tpm-pcr-compute utility during image build time in the previous step. You can locate the reference measurements in the following file: ./image/pcr_measurements.json.
The measurements are provided in the following JSON format:
{ "Measurements": { "HashAlgorithm": "SHA384 { ... }", "PCR4": "PCR4_measurement", "PCR7": "PCR7_measurement", "PCR12": "PCR12_measurement"
  } }
7. Use the coldsnap utility to upload the raw disk image created by KIWI NG to an EBS snapshot. The command returns the snapshot ID. Make a note of the ID, you'll need it for the next step.
SNAPSHOT=$(.cargo/bin/coldsnap upload ./image/kiwi*.raw) echo "Created snapshot: $SNAPSHOT"
For more information about the coldsnap utility, see the  coldsnap GitHub repo.
8. Register a TPM 2.0-enabled AMI with UEFI boot mode using the snapshot from the previous step. For --architecture, specify x86_64 for Intel, or arm64 for Graviton. aws ec2 register-image \ --name "attestable_isolated_al2023_ami" \

--virtualization-type hvm \ --boot-mode uefi \ --architecture x86_64|arm64 \ --root-device-name /dev/xvda \ --block-device-mappings DeviceName=/dev/xvda,Ebs={SnapshotId=${SNAPSHOT}} \ --tpm-support v2.0 \ --ena-support
### Sample Amazon Linux 2023 image description The sample Amazon Linux 2023 image description has the following characteristics:
1. Unified Kernel Image (UKI) boot — Boot using a single, signed binary that combines the kernel, initrd, and boot parameters into one immutable image.
2. Read-only root filesystem — Use Enhanced Read-Only File System (erofs) with dm-verity protection to ensure that the root filesystem cannot be modified and maintains cryptographic integrity verification.
3. Ephemeral overlay filesystem — Create a temporary overlay filesystem that allows temporary writes to directories like /etc, /run, and /var. Since this overlay filesystem exists only in memory, all changes are automatically lost when the instance reboots, ensuring the system returns to its original trusted state.
4. Disabled remote access methods — Remove the following remote access mechanisms to prevent remote access:
Access Method Description Image descripti on implement ation SSH Excludes OpenSSH server. Makes the instance inherentl y incapable of handling SSH traffic.
Ignore the openssh- server package * User Data Removes Cloud-init. Eliminates the ability for operators to provide user data to instances and run boot-time scripts.
Ignore the cloud-init and cloud-ini

Access Method Description Image descripti on implement ation t-cfg-ec2 packages * Chrony Disables the chrony command port. Prevents operators from running chrony commands on running instances.
Ignore the amazon-ch rony-conf ig  package * MOTD Removes MOTD package. Eliminates the ability for operators to change messages or functionality on running instances.
Ignore the update-motd package * AWS SSM Removes the AWS SSM agent. Prevents remote access to running instances using AWS SSM.
Ignore the amazon-ssm- agent package * EC2 Instance Connect Removes EC2 Instance Connect package. Disables SSH access using this tool.
Ignore the ec2- instance- connect package * Serial Console Disables serial console. Ensures that console access is unavailable for running instances and removes the operators' ability to login to the serial console.
Disabled via kernel command line parameter
* For more information, see  Image Description Elements.

### Customize the sample Amazon Linux 2023 image description for your workload You can customize the sample Amazon Linux 2023 image description and include the software packages, scripts, and files that are needed for your specific workload. Customizations are achieved by adding to or modifying various elements in the KIWI NG image description.
Topics
- Repository management
- Package management
- Adding files and directories
- Adding custom scripts
#### Repository management By default, the sample image description includes a single <repository> element that points to a mirror endpoint for the Amazon Linux 2023 core repositories. If needed, you can add references to other repositories from which to install your required software.
The sample image description uses the dnf package manager, as defined in the <packagemanager> element.
For more information about adding repositories, see Setting up Repositories.
#### Package management By default, the sample image description includes all of the packages needed to create an Amazon Linux 2023 Attestable AMI for an isolated compute environment with an erofs read-only file system.
You can include additional software packages in the image description by adding them to the <packages> element in the image description. The <packages> element defines all of the software that should be installed into the AMI.
You can also use the <packages> element to uninstall or delete specific software packages.
For more information about adding or removing packages in the image description, see Adding and Removing Packages.

#### Adding files and directories The sample image description includes an overlay tree directory (/root/). The overlay tree directory is a directory that contains files and directories that will be copied into the image during the image build process. Any files and directories that you place into the overlay tree directory will be copied directly into the root filesystem of the image during the image building process.
The overlay tree directory is copied into the image after all the packages have been installed. New files are added and existing files are overwritten.
#### Adding custom scripts The sample image description includes a single custom script, edit_boot_install.sh. This script includes the commands that are needed to run the nitro-tpm-pcr-compute utility, which generates the reference measurements based on the image content. This script is called immediately after the bootloader is installed.
If needed, you can include your own custom scripts in the image description to perform tasks or configurations during the image build process or at first boot of the image. Using scripts enables you to customize your images in ways that cannot be achieved using the image description alone.
To include custom scripts in your image description, you need to name them correctly based on the type of script, and add them to the same directory as the appliance.kiwi file. KIWI NG automatically detects and executes the scripts if they are named correctly and placed in the correct location, without the need to explicitly reference them in the image description file.
For more information about the scripts supported by KIWI NG, see User-Defined Scripts.
### Compute PCR measurements for a custom AMI The nitro-tpm-pcr-compute utility enables you to generate the reference measurements for an Attestable AMI during build time based on its Unified Kernel Image (UKI).
The sample Amazon Linux 2023 image description automatically installs the utility in the built image in the /usr/bin/ directory. The sample image description also includes a script with the commands needed to run the utility to generate the reference measurements during image build time. If you are using the sample image description, you don't need to install the utility or run it manually. For more information, see Build the sample Amazon Linux 2023 image description.

#### Install the nitro-tpm-pcr-compute utility If you are using Amazon Linux 2023, you can install the nitro-tpm-pcr-compute utility from the Amazon Linux repository as follows. sudo yum install aws-nitro-tpm-tools The tools are installed in the /usr/bin directory.
#### Use the nitro-tpm-pcr-compute utility The utility provides a single command, nitro-tpm-pcr-compute, for generating the reference measurements.
When you run the command, you must specify the following:
- Unified kernel image (UKI.efi) — Required for Standard boot and UEFI.
To generate the reference measurements for an Attestable AMI:
Use the following command and parameters:
/usr/bin/nitro-tpm-pcr-compute \ --image UKI.efi The utility returns the reference measurements in the following JSON format:
{ "Measurements": { "HashAlgorithm": "SHA384 { ... }", "PCR4": "PCR4_measurement", "PCR7": "PCR7_measurement", "PCR12": "PCR12_measurement"
  } } For a practical example of how to use the nitro-tpm-pcr-compute utility, see the edit_boot_install.sh script included in the  sample Amazon Linux 2023 image description.

## Prepare AWS KMS for attestation Note If you are attesting to a third-party service, you must build your own custom mechanisms for receiving, parsing, and validating Attestation Documents. For more information, see Validate a NitroTPM Attestation Document.
After you have created your Attestable AMI, you should have reference measurements that you can use to validate requests from an Amazon EC2 instance. AWS KMS provides built-in support for attestation with NitroTPM.
For the AWS KMS key that you used to encrypt your secret data, add a key policy that allows key access only if API requests include an Attestation Document with measurements that match the reference measurements you generated during the Attestable AMI creation process. Use PCR4 and PCR12 measurements for standard boot or PCR7 measurements for Secure Boot. This ensures that only requests from instances launched using the Attestable AMI can perform cryptographic operations using the AWS KMS key.
AWS KMS provides kms:RecipientAttestation:NitroTPMPCR4, kms:RecipientAttestation:NitroTPMPCR7, and kms:RecipientAttestation:NitroTPMPCR12 condition keys that enable you to create attestation-based conditions for NitroTPM KMS key policies. For more information, see Condition keys for NitroTPM.
For example, the following AWS KMS key policy allows key access only if the request originates from an instance with the MyEC2InstanceRole instance profile attached, and if the request includes an Attestation Document with specific PCR 4 and PCR 12 values.
{ "Version": "2012-10-17", "Statement": [ { "Sid": "Allow requests from instances with attested AMI only", "Effect": "Allow", "Principal": { "AWS": "arn:aws:iam::111122223333:role/MyEC2InstanceRole"
      },

      "Action": [ "kms:Decrypt", "kms:GenerateDataKey", "kms:GenerateRandom"
      ], "Resource": "*", "Condition": { "StringEqualsIgnoreCase": {

 "kms:RecipientAttestation:NitroTPMPCR4":"EXAMPLE6b9b3d89a53b13f5dfd14a1049ec0b80a9ae4b159adde4

 "kms:RecipientAttestation:NitroTPMPCR12":"0000000000000000000000000000000000000000000000000000 } } } ]
}
## Get the NitroTPM Attestation Document The Attestation Document is a key component of the NitroTPM attestation process. It contains a series of cryptographic measurements that can be used to verify the identity of the instance and to prove that it is running only trusted software. You can use the Attestation Document with AWS KMS, which provides built-in support for NitroTPM attestation, or to build your own cryptographic attestation mechanisms.
The nitro-tpm-attest utility enables you to retrieve a signed NitroTPM Attestation Document for an Amazon EC2 instance during runtime.
The sample Amazon Linux 2023 image description automatically installs the utility in the built image in the /usr/bin/ directory. This ensures that the utility is preinstalled on instances launched using the AMI. You don't need to manually install the utility. For more information, see Build the sample Amazon Linux 2023 image description.
Topics
- Install the nitro-tpm-attest utility
- Use the nitro-tpm-attest utility
- NitroTPM Attestation Document contents
- Validate a NitroTPM Attestation Document

### Install the nitro-tpm-attest utility If you are using Amazon Linux 2023, you can install the nitro-tpm-attest utility from the Amazon Linux repository as follows. sudo yum install aws-nitro-tpm-tools
### Use the nitro-tpm-attest utility The utility provides a single command, nitro-tpm-attest, for retrieving the Attestation Document. The command returns the Attestation Document encoded in Concise Binary Object Representation (CBOR) and signed using CBOR Object Signing and Encryption (COSE).
When you run the command, you can specify the following optional parameters:
- public-key — A public key that can be used by AWS KMS or an external service to encrypt response data before it is returned. This ensures that only the intended recipient, that has possession of the private key, can decrypt the data. For example, if you are attesting with AWS KMS, the service encrypts the plaintext data with the public key in the Attestation Document, and returns the resulting ciphertext in the CiphertextForRecipient field in the response.
Only RSA keys are supported.
- user-data — The user data can be used to deliver any additional signed data to an external service. This user data can be used to complete an agreed protocol between the requesting instance and the external service. Not used for attestation with AWS KMS.
- nonce — The nonce can be used to set up challenge-response authentication between the instance and the external service to help prevent impersonation attacks. Using a nonce enables the external service to verify that it is interacting with a live instance and not an impersonator that is reusing an old Attestation Document. Not used for attestation with AWS KMS.
To retrieve the Attestation Document Use the following command and optional parameters:
/usr/bin/nitro-tpm-attest \ --public-key rsa_public_key \ --user-data user_data \ --nonce nonce

For a complete example that shows how to generate an RSA key pair, and how to request an attestation with the public key, see the nitro-tpm-attest GitHub repo.
### NitroTPM Attestation Document contents An Attestation Document is generated by the NitroTPM and it is signed by the Nitro Hypervisor.
It includes a series of platform configuration registers (PCR) values related to an Amazon EC2 instance. The following PCRs are included in the Attestation Document:
Important PCR0 and PCR1 are generally used to measure the initial boot code, which is controlled by AWS. To allow safe updates of early boot code, these PCRs will always contain constant values.
- PCR0 — Core System Firmware Executable Code
- PCR1 — Core System Firmware Data
- PCR2 — Extended or pluggable executable code
- PCR3 — Extended or pluggable Firmware Data
- PCR4 — Boot Manager Code
- PCR5 — Boot Manager Code Configuration and Data and GPT Partition Table
- PCR6 — Host Platform Manufacturer Specifics
- PCR7 — Secure Boot Policy
- PCR8 - 15 — Defined for use by the Static Operating System
- PCR16 — Debug
- PCR23 — Application Support PCR4, PCR7, and PCR12 specifically are used to validate that an instance was launched using an Attestable AMI. PCR4 and PCR12 can be used to validate with standard boot, and PCR7 can be used to validate with Secure Boot.
- PCR4 (Boot Manager Code) — When an instance starts, the NitroTPM creates cryptographic hashes of all the binaries executed by its UEFI environment. With Attestable AMIs, these boot binaries embed hashes that prevent future loading of binaries that do not have matching hashes.
This way, the single boot binary hash can describe exactly what code an instance will execute.

- PCR7 (Secure Boot Policy) — UEFI boot binaries can be signed with a UEFI Secure Boot signing key. When UEFI Secure Boot is enabled, UEFI will prevent execution of UEFI boot binaries that do not match the configured policy. PCR7 contains a hash of the instance's UEFI Secure Boot policy.
If you need to maintain a single KMS policy that persists across instance updates, you can create a policy that validates against PCR7 to validate a UEFI Secure Boot certificate. During creation of an Attestable AMI, you can then sign the boot binary with your certificate and install it as the only permitted certificate in the AMI's UEFI-data. Keep in mind that this model requires you to still generate a new certificate, install it in your policy and update AMIs if you want to prevent instances launched from old (untrusted) AMIs from passing your KMS policy.
- PCR12 — Contains the hash of the command line passed to the UEFI boot binary. Required in conjunction with PCR4 for standard boot to validate the command line was not modified.
### Validate a NitroTPM Attestation Document Note This topic is intended for users who are using a third-party key management service, and need to build their own Attestation Document validation mechanisms.
This topic provides a detailed overview of the entire NitroTPM attestation flow. It also discusses what is generated by the AWS Nitro system when an Attestation Document is requested, and explains how a key management service should process an Attestation Document.
Topics
- The Attestation Document
- Attestation Document validation The purpose of attestation is to prove that an instance is a trustworthy entity, based on the code and configuration that it is running. The root of trust for the instance resides within the AWS Nitro system, which provides Attestation Documents.
Attestation Documents are signed by the AWS Nitro Attestation Public Key Infrastructure (PKI), which includes a published certificate authority that can be incorporated into any service.

#### The Attestation Document Attestation Documents are encoded in Concise Binary Object Representation (CBOR), and signed using CBOR Object Signing and Encryption (COSE).
For more information about CBOR, see RFC 8949: Concise Binary Object Representation (CBOR).
##### Attestation Document specification The following shows the structure of an Attestation Document.
AttestationDocument = { module_id: text,                     ; issuing Nitro hypervisor module ID timestamp: uint .size 8,             ; UTC time when document was created, in ; milliseconds since UNIX epoch digest: digest,                      ; the digest function used for calculating the ; register values nitrotpm_pcrs: { + index => pcr },   ; map of PCRs at the moment the Attestation Document was generated certificate: cert,                   ; the public key certificate for the public key ; that was used to sign the Attestation Document cabundle: [* cert],                  ; issuing CA bundle for infrastructure certificate ? public_key: user_data,             ; an optional DER-encoded key the attestation ; consumer can use to encrypt data with ? user_data: user_data,              ; additional signed user data, defined by protocol ? nonce: user_data,                  ; an optional cryptographic nonce provided by the ; attestation consumer as a proof of authenticity } cert = bytes .size (1..1024)       ; DER encoded certificate user_data = bytes .size (0..1024) pcr = bytes .size (32/48/64)       ; PCR content index = 0..31 digest = "SHA384"

The optional parameters in the Attestation Document (public_key, user_data, and nonce) can be used to establish a custom validation protocol between an attesting instance and the external service.
#### Attestation Document validation When you request an Attestation Document from the Nitro Hypervisor, you receive a binary blob that contains the signed Attestation Document. The signed Attestation Document is a CBOR- encoded, COSE-signed (using the COSE_Sign1 signature structure) object. The overall validation process includes the following steps:
1. Decode the CBOR object and map it to a COSE_Sign1 structure.
2. Extract the Attestation Document from the COSE_Sign1 structure.
3. Verify the certificate's chain.
4. Ensure that the Attestation Document is properly signed.
Attestation Documents are signed by the AWS Nitro Attestation PKI, which includes a root certificate for the commercial AWS partitions. The root certificate can be downloaded from https:// aws-nitro-enclaves.amazonaws.com/AWS_NitroEnclaves_Root-G1.zip, and it can be verified using the following fingerprint.
64:1A:03:21:A3:E2:44:EF:E4:56:46:31:95:D6:06:31:7E:D7:CD:CC:3C:17:56:E0:98:93:F3:C6:8F:79:BB:5B The root certificate is based on an AWS Certificate Manager Private Certificate Authority (AWS Private CA) private key and it has a lifetime of 30 years. The subject of the PCA has the following format.
CN=aws.nitro-enclaves, C=US, O=Amazon, OU=AWS Topics
- COSE and CBOR
- Semantic validity
- Certificate validity
- Certificate chain validity

##### COSE and CBOR Usually, the COSE_Sign1 signature structure is used when only one signature is going to be placed on a message. The parameters dealing with the content and the signature are placed in the protected header rather than having the separation of COSE_Sign. The structure can be encoded as either tagged or untagged, depending on the context it will be used in. A tagged COSE_Sign1 structure is identified by the CBOR tag 18.
The CBOR object that carries the body, the signature, and the information about the body and signature is called the COSE_Sign1 structure. The COSE_Sign1 structure is a CBOR array. The array includes the following fields.
[ protected:   Header, unprotected: Header, payload:     This field contains the serialized content to be signed, signature:   This field contains the computed signature value.
]
In the context of an Attestation Document, the array includes the following.
18(/* COSE_Sign1 CBOR tag is 18 */ {1: -35}, /* This is equivalent with {algorithm: ECDS 384} */ {}, /* We have nothing in unprotected */ $ATTESTATION_DOCUMENT_CONTENT /* Attestation Document */, signature /* This is the signature */ )
For more information about CBOR, see RFC 8949: Concise Binary Object Representation (CBOR).
##### Semantic validity An Attestation Document will always have their CA bundle in the following order.
[ ROOT_CERT - INTERM_1 - INTERM_2 .... - INTERM_N]
      0          1          2             N - 1 Keep this ordering in mind, as some existing tools, such as Java's CertPath from  Java PKI API Programmer's Guide, might require them to be ordered differently.

To validate the certificates, start from the Attestation Document CA bundle and generate the required chain, Where TARGET_CERT is the certificate in the Attestation Document.
[TARGET_CERT, INTERM_N, ..... , INTERM_2, INTERM_1, ROOT_CERT]
##### Certificate validity For all of the certificates in the chain, you must ensure that the current date falls within the validity period specified in the certificate.
##### Certificate chain validity In general, a chain of multiple certificates might be needed, comprising a certificate of the public key owner signed by one CA, and zero or more additional certificates of CAs signed by other CAs.
Such chains, called certification paths, are required because a public key user is only initialized with a limited number of assured CA public keys. Certification path validation procedures for the internet PKI are based on the algorithm supplied in X.509. Certification path processing verifies the binding between the subject distinguished name and/or subject alternative name and subject public key. The binding is limited by constraints that are specified in the certificates that comprise the path and inputs that are specified by the relying party. The basic constraints and policy constraint extensions allow the certification path processing logic to automate the decision making process.
Note CRL must be disabled when doing the validation.
Using Java, starting from the root path and the generated certificate chain, the chain validation is as follows. validateCertsPath(certChain, rootCertficate) { /* The trust anchor is the root CA to trust */ trustAnchors.add(rootCertificate); /* We need PKIX parameters to specify the trust anchors
     * and disable the CRL validation */ validationParameters = new PKIXParameters(trustAnchors); certPathValidator = CertPathValidator.getInstance(PKIX);

    validationParameters.setRevocationEnabled(false); /* We are ensuring that certificates are chained correctly */ certPathValidator.validate(certPath, validationParameters); }
## Integrating with AWS KMS Your instance should have an application that can make AWS KMS API requests with the Attestation Document retrieved from the NitroTPM. When you make a request with an Attestation Document, AWS KMS validates the measurements in the provided Attestation Document against the reference measurements in the KMS key policy. Requests are allowed only if the measurements in the Attestation Document match the reference measurements in the KMS key policy.
When you call the Decrypt, DeriveSharedSecret, GenerateDataKey, GenerateDataKeyPair, or GenerateRandom API operations with an Attestation Document, these APIs encrypt the plaintext in the response under the public key from the Attestation Document, and return ciphertext instead of plaintext. This ciphertext can be decrypted only by using the matching private key that was generated in the instance.
For more information, see the  Cryptographic attestation for NitroTPM in the AWS Key Management Service Developer Guide.
Note If you are attesting to a third-party service, you must build your own custom mechanisms for receiving, parsing, and validating Attestation Documents. For more information, see Validate a NitroTPM Attestation Document.
## Isolate data from your own operators The AWS Nitro System has  zero operator access. There is no mechanism for any AWS system or person to log in to Amazon EC2 Nitro hosts, access the memory of EC2 instances, or access any customer data stored on local encrypted instance storage or remote encrypted Amazon EBS volumes.
When processing highly sensitive data, you might consider restricting access to that data by preventing even your own operators from accessing the EC2 instance.

You can create custom Attestable AMIs that are configured to provide an isolated compute environment. The AMI configuration depends on your workload and application requirements.
Consider these best practices when building your AMI to create an isolated compute environment.
- Remove all interactive access to prevent your operators or users access to the instance.
- Ensure that only trusted software and code is included in the AMI.
- Configure a network firewall within the instance to block access.
- Ensure read-only and immutable states for all storage and file systems.
- Restrict instance access to authenticated, authorized, and logged API calls.
### Updating Attestable AMIs that have no interactive access Once you launch an instance using an isolated compute environment AMI, there is no way for any user or operator to connect to the instance. This means that there is no way to install or update any software on the instance after launch.
If new software or a software update is required, you must create a new Attestable AMI that includes the required software or software updates. Then, use that AMI to launch a new instance, or to perform a root volume replacement on the original instance. Any software changes made to the AMI will result in a new hash being generated.
The following actions will result in a change to the reference measurements in the NitroTPM Attestation Document:
- Stopping and starting an instance launched with an Attestable AMI
- Performing a root volume replacement with a different AMI If you perform any of these actions, you must then update your attestation service with the new reference measurements. For example, you must update your KMS key policy to the new reference measurements if you are using AWS KMS for attestation.
An instance retains its NitroTPM key material for the entire instance lifecycle, and persists through stop/starts and root volume replacement operations.
