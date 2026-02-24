# Detect whether a host is an EC2 instance

Source: apps/user-manuals/aws/ec2-ug.pdf

---

IMDSv1 [ec2-user ~]$ echo $user_data | cut -d"|" -f"$ami_launch_index" replicate-every=5min
# Detect whether a host is an EC2 instance You might need to know whether your application or website is running on an EC2 instance, especially if you have a mixed computing environment. You can use one of the following options to determine whether the host for your application or website is an EC2 instance.
Options
- Inspect the instance identity document
- Inspect the system UUID
- Inspect the system virtual machine generation identifier
## Inspect the instance identity document Each instance has a signed instance identity document that you can verify cryptographically. You can find these documents using the Instance Metadata Service (IMDS).
For more information, see Instance identity documents.
## Inspect the system UUID You can get the system UUID and look in the beginning octet of the UUID for EC2 (in Linux, this might be lowercase ec2). This method is quick, but potentially inaccurate because there's a small chance that a system that is not an EC2 instance could have a UUID that starts with these characters. Furthermore, some versions of SMBIOS use the little-endian format, which doesn't include EC2 at the beginning of the UUID. This might be the case for EC2 instances that use SMBIOS 2.4 for Windows, or for Linux distributions other than Amazon Linux that have their own implementation of SMBIOS.
Linux example: Get the UUID from DMI (HVM AMIs only)
Use the following command to get the UUID using the Desktop Management Interface (DMI):

[ec2-user ~]$ sudo dmidecode --string system-uuid In the following example output, the UUID starts with "EC2", which indicates that the system is probably an EC2 instance.
EC2E1916-9099-7CAF-FD21-012345ABCDEF In the following example output, the UUID is represented in little-endian format.
45E12AEC-DCD1-B213-94ED-012345ABCDEF Alternatively, for instances built on the Nitro system, you can use the following command:
[ec2-user ~]$ cat /sys/devices/virtual/dmi/id/board_asset_tag If the output is an instance ID, as the following example output, the system is an EC2 instance: i-0af01c0123456789a Linux example: Get the UUID from the hypervisor (PV AMIs only)
Use the following command to get the UUID from the hypervisor:
[ec2-user ~]$ cat /sys/hypervisor/uuid In the following example output, the UUID starts with "ec2", which indicates that the system is probably an EC2 instance. ec2e1916-9099-7caf-fd21-012345abcdef Windows example: Get the UUID using WMI or Windows PowerShell Use the Windows Management Instrumentation command line (WMIC) as follows: wmic path win32_computersystemproduct get uuid Alternatively, if you're using Windows PowerShell, use the Get-WmiObject cmdlet as follows:

PS C:\> Get-WmiObject -query "select uuid from Win32_ComputerSystemProduct" | Select UUID In the following example output, the UUID starts with "EC2", which indicates that the system is probably an EC2 instance.
EC2AE145-D1DC-13B2-94ED-012345ABCDEF For instances using SMBIOS 2.4, the UUID might be represented in little-endian format; for example:
45E12AEC-DCD1-B213-94ED-012345ABCDEF
## Inspect the system virtual machine generation identifier A virtual machine generation identifier consists of a unique buffer of 128-bit interpreted as cryptographic random integer identifier. You can retrieve the virtual machine generation identifier to identify your Amazon Elastic Compute Cloud instance. The generation identifier is exposed within the guest operating system of the instance through an ACPI table entry. The value will change if your machine is cloned, copied, or imported into AWS, such as with VM Import/Export.
Example: Retrieve the virtual machine generation identifier from Linux You can use the following commands to retrieve the virtual machine generation identifier from your instances running Linux.
Amazon Linux 2
1. Update your existing software packages, as necessary, using the following command: sudo yum update
2. If necessary, source the busybox package with the following command: sudo curl https://www.rpmfind.net/linux/epel/next/8/Everything/x86_64/Packages/ b/busybox-1.35.0-2.el8.next.x86_64.rpm --output busybox.rpm
3. If necessary, install the prerequisite packages using the following command:

sudo yum install busybox.rpm iasl -y
4. Run the following iasl command to produce output from the ACPI table: sudo iasl -p ./SSDT2 -d /sys/firmware/acpi/tables/SSDT2
5. Run the following command to review the output of the iasl command: cat SSDT2.dsl The output should yield the address space required to retrieve the virtual machine generation identifier:
Intel ACPI Component Architecture ASL+ Optimizing Compiler/Disassembler version 20190509 Copyright (c) 2000 - 2019 Intel Corporation File appears to be binary: found 32 non-ASCII characters, disassembling Binary file appears to be a valid ACPI table, disassembling Input file /sys/firmware/acpi/tables/SSDT2, Length 0x7B (123) bytes ACPI: SSDT 0x0000000000000000 00007B (v01 AMAZON AMZNSSDT 00000001 AMZN 00000001)
Pass 1 parse of [SSDT]
Pass 2 parse of [SSDT]
Parsing Deferred Opcodes (Methods/Buffers/Packages/Regions)
Parsing completed Disassembly completed ASL Output:    ./SSDT2.dsl - 1065 bytes $ /*
* Intel ACPI Component Architecture
* AML/ASL+ Disassembler version 20190509 (64-bit version)
* Copyright (c) 2000 - 2019 Intel Corporation *
* Disassembling to symbolic ASL+ operators *
* Disassembly of /sys/firmware/acpi/tables/SSDT2, Tue Mar 29 16:15:14 2022 *
* Original Table Header:
*     Signature        "SSDT"

*     Length           0x0000007B (123)
*     Revision         0x01
*     Checksum         0xB8
*     OEM ID           "AMAZON"
*     OEM Table ID     "AMZNSSDT"
*     OEM Revision     0x00000001 (1)
*     Compiler ID      "AMZN"
*     Compiler Version 0x00000001 (1)
*/ DefinitionBlock ("", "SSDT", 1, "AMAZON", "AMZNSSDT", 0x00000001)
{ Scope (\_SB)
{ Device (VMGN)
    { Name (_CID, "VM_Gen_Counter")  // _CID: Compatible ID Name (_DDN, "VM_Gen_Counter")  // _DDN: DOS Device Name Name (_HID, "AMZN0000")  // _HID: Hardware ID Name (ADDR, Package (0x02)
        { 0xFED01000, Zero })
    } } }
6. (Optional) Elevate your terminal permissions for the remaining steps with the following command: sudo -s
7. Use the following command to store the previously gathered address space:
VMGN_ADDR=0xFED01000
8. Use the following command to iterate through the address space and build the virtual machine generation identifier: for offset in 0x0 0x4 0x8 0xc; do busybox devmem $(($VMGN_ADDR + $offset)) | sed 's/0x//' | sed -z '$ s/\n$//' >> vmgenid; done

9. Retrieve the virtual machine generation identifier from the output file with the following command: cat vmgenid ; echo Your output should be similar to the following:
EC2F335D979132C4165896753E72BD1C Ubuntu
1. Update your existing software packages, as necessary, using the following command: sudo apt update
2. If necessary, install the prerequisite packages using the following command: sudo apt install busybox iasl -y
3. Run the following iasl command to produce output from the ACPI table: sudo iasl -p ./SSDT2 -d /sys/firmware/acpi/tables/SSDT2
4. Run the following command to review the output of the iasl command: cat SSDT2.dsl The output should yield the address space required to retrieve the virtual machine generation identifier:
Intel ACPI Component Architecture ASL+ Optimizing Compiler/Disassembler version 20190509 Copyright (c) 2000 - 2019 Intel Corporation File appears to be binary: found 32 non-ASCII characters, disassembling Binary file appears to be a valid ACPI table, disassembling Input file /sys/firmware/acpi/tables/SSDT2, Length 0x7B (123) bytes ACPI: SSDT 0x0000000000000000 00007B (v01 AMAZON AMZNSSDT 00000001 AMZN 00000001)

Pass 1 parse of [SSDT]
Pass 2 parse of [SSDT]
Parsing Deferred Opcodes (Methods/Buffers/Packages/Regions)
Parsing completed Disassembly completed ASL Output:    ./SSDT2.dsl - 1065 bytes $ /*
* Intel ACPI Component Architecture
* AML/ASL+ Disassembler version 20190509 (64-bit version)
* Copyright (c) 2000 - 2019 Intel Corporation *
* Disassembling to symbolic ASL+ operators *
* Disassembly of /sys/firmware/acpi/tables/SSDT2, Tue Mar 29 16:15:14 2022 *
* Original Table Header:
*     Signature        "SSDT"
*     Length           0x0000007B (123)
*     Revision         0x01
*     Checksum         0xB8
*     OEM ID           "AMAZON"
*     OEM Table ID     "AMZNSSDT"
*     OEM Revision     0x00000001 (1)
*     Compiler ID      "AMZN"
*     Compiler Version 0x00000001 (1)
*/ DefinitionBlock ("", "SSDT", 1, "AMAZON", "AMZNSSDT", 0x00000001)
{ Scope (\_SB)
{ Device (VMGN)
    { Name (_CID, "VM_Gen_Counter")  // _CID: Compatible ID Name (_DDN, "VM_Gen_Counter")  // _DDN: DOS Device Name Name (_HID, "AMZN0000")  // _HID: Hardware ID Name (ADDR, Package (0x02)
        { 0xFED01000, Zero })
    } }
