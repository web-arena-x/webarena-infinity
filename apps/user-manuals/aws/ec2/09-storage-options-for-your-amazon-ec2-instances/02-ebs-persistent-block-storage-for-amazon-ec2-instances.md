# Amazon EBS persistent block storage for Amazon EC2 instances

Source: apps/user-manuals/aws/ec2-ug.pdf

---

File caching
- Use Amazon File Cache with Amazon EC2 instances — Amazon File Cache provides temporary, high-performance cache on AWS for processing file data. The cache provides read and write data access to compute workloads on Amazon EC2 with sub-millisecond latencies, up to hundreds of GB/s of throughput, and up to millions of IOPS.
The following figure shows the relationship between these storage options and your instance.
# AWS Storage pricing Open AWS Pricing, scroll to Pricing for AWS products and select Storage. Choose the storage product to open its pricing page.
# Amazon EBS persistent block storage for Amazon EC2 instances Amazon Elastic Block Store (Amazon EBS) provides scalable, high-performance block storage resources that can be used with Amazon EC2 instances. With Amazon EBS, you can create and manage the following block storage resources:
- Amazon EBS volumes — These are storage volumes that you attach to Amazon EC2 instances.
After you attach a volume to an instance, you can use it in the same way you would use block storage. The instance can interact with the volume just as it would with a local drive.

- Amazon EBS snapshots — These are point-in-time backups of Amazon EBS volumes that persist independently from the volume itself. You can create snapshots to back up the data on your Amazon EBS volumes. You can then restore new volumes from those snapshots at any time.
You can create and attach EBS volumes to an instance during launch, and you can create and attach EBS volumes to an instance at any time after launch. You can also increase the size or performance of your EBS volumes without detaching the volume or restarting your instance.
You can create EBS snapshots from an EBS volume at any time after creation. You can use EBS snapshots to back up the data stored on your volumes. You can then use those snapshots to instantly restore volumes, or to migrate data across AWS accounts, AWS Regions, or Availability Zones. You can use Amazon Data Lifecycle Manager or AWS Backup to automate the creation, retention, and deletion of your EBS snapshots.
A managed EBS volume is managed by a service provider, such as Amazon EKS Auto Mode. You can't directly modify the settings of a managed EBS volume. Managed EBS volumes are identified by a true value in the Managed field. For more information, see Amazon EC2 managed instances.
For more information about working with volumes and snapshots, see the Amazon EBS User Guide.
## Amazon EBS volume limits for Amazon EC2 instances The maximum number of Amazon EBS volumes that you can attach to an instance depends on the instance type and instance size. If you exceed the volume attachment limit for an instance, the attachment request fails with the AttachmentLimitExceeded error.
When considering how many volumes to attach to your instance, you should consider whether you need increased I/O bandwidth or increased storage capacity.
Bandwidth versus capacity For consistent and predictable bandwidth use cases, use Amazon EBS-optimized instances with General Purpose SSD volumes or Provisioned IOPS SSD volumes. For maximum performance, match the IOPS you have provisioned for your volumes with the bandwidth available for your instance type.
For RAID configurations, you might find that arrays larger than 8 volumes have diminished performance returns due to increased I/O overhead. Test your individual application performance and tune it as required.

Contents
- Volume limits for instances built on the Nitro System
- Dedicated EBS volume limit
- Shared EBS volume limit
- Volume limits for Xen-based instances
- Linux instances
- Windows instances
### Volume limits for instances built on the Nitro System The volume limits for instances built on the Nitro System depend on the instance type. Some Nitro instance types have a dedicated EBS volume limit, while most have a shared volume limit. To view the volume attachment limits for each instance type, see the following:
- Amazon EBS specifications – General purpose
- Amazon EBS specifications – Compute optimized
- Amazon EBS specifications – Memory optimized
- Amazon EBS specifications – Storage optimized
- Amazon EBS specifications – Accelerated computing
- Amazon EBS specifications – High-performance computing
- Amazon EBS specifications – Previous generation
#### Dedicated EBS volume limit The following Nitro instance types have a dedicated EBS volume limit that varies depending on instance size. The limit is not shared with other device attachments. In other words, you can attach any number of EBS volumes up to the volume attachment limit, regardless of the number of attached devices, such as NVMe instance store volumes and network interfaces.
- General purpose: M7a | M7i | M7i-flex | M8a | M8azn | M8g | M8gb | M8gd | M8gn | M8i | M8id | M8i-flex
- Compute optimized: C7a | C7i | C7i-flex | C8a | C8g | C8gb | C8gd | C8gn | C8i | C8id | C8i-flex

- Memory optimized: R7a | R7i | R7iz | R8a | R8g | R8gb | R8gd | R8gn | R8i | R8id | R8i-flex | U7i-6tb | U7i-8tb | U7i-12tb | U7in-16tb | U7in-24tb | U7in-32tb | U7inh-32tb | X8g | X8aedz | X8i
- Storage optimized: I7i | I7ie | I8g | I8ge
- Accelerated computing: F2 | G6 | G6e | G6f | Gr6 | Gr6f | G7e | P4d | P4de | P5 | P5e | P5en | P6- B200 | P6-B300 | P6e-GB200 | Trn2 | Trn2u
- High performance computing: Hpc7a | Hpc8a
#### Shared EBS volume limit All other Nitro instance types (not listed in Dedicated EBS volume limit) have a volume attachment limit that is shared between Amazon EBS volumes, network interfaces, and NVMe instance store volumes. You can attach any number of Amazon EBS volumes up to that limit, less the number of attached network interfaces and NVMe instance store volumes. Keep in mind that every instance must have at least one network interface, and that NVMe instance store volumes are automatically attached at launch.
Most Nitro instances support a maximum of 28 attachments. The following examples demonstrate how to calculate how many EBS volumes you can attach.
Examples
- With an m5.xlarge instance with only the primary network interface, you can attach 27 EBS volumes.
28 volumes - 1 network interface = 27
- With an m5.xlarge instance with two additional network interfaces, you can attach 25 EBS volumes.
28 volumes - 3 network interfaces = 25
- With an m5d.xlarge instance with two additional network interfaces, you can attach 24 EBS volumes.
28 volumes - 3 network interfaces - 1 NVMe instance store volume = 24
### Volume limits for Xen-based instances The volume limits for Xen-based instances, such as T2, depend on the operating system.

For more information, see Xen-based instances.
#### Linux instances Attaching more than 40 volumes to a Xen-based Linux instance can cause boot failures. This number includes the root volume, plus any attached instance store volumes and Amazon EBS volumes.
If you experience boot problems on an instance with a large number of volumes, stop the instance, detach any volumes that are not essential to the boot process, start the instance, and then reattach the volumes after the instance is running.
Important Attaching more than 40 volumes to a Xen-based Linux instance is supported on a best effort basis only and is not guaranteed.
#### Windows instances The following table shows the volume limits for Xen-based Windows instances based on the driver used. That these numbers include the root volume, plus any attached instance store volumes and Amazon EBS volumes.
Driver Volume Limit AWS PV 26 Citrix PV 26 Red Hat PV 17 We recommend that you do not that attach more than 26 volumes to a Xen-based Windows instance with AWS PV or Citrix PV drivers, as it is likely to cause performance issues. To determine which PV drivers your instance is using, or to upgrade your Windows instance from Red Hat to Citrix PV drivers, see the section called "Upgrade PV drivers".

Important Attaching more than the following number of volumes to a Xen-based Windows instance is supported on a best effort basis only and is not guaranteed.
For more information about how device names are related to volumes, see How volumes are attached and mapped for Amazon EC2 Windows instances.
## EBS cards Most instance types support one EBS card. Instance types that support multiple EBS cards provide higher EBS-optimized performance, both in EBS throughput and IOPS. Your Amazon EC2 instance maximum performance is spread equally across each EBS card. For example, on an EC2 instance that supports 1,000,000 total IOPS with 2 EBS cards, each EBS card can support up to 500,000 IOPS. For information about the supported Amazon EBS performance of your Amazon EC2 instance, see Amazon EBS-optimized instance types.
When you attach an Amazon EBS volume to an instance that supports multiple EBS cards, you can select the EBS card for the volume by specifying the EBS card index. The root volume must be attached to EBS card index 0.
### Instance types with multiple EBS cards The following instance types support multiple EBS cards. For information about the number of Amazon EBS volumes that an instance type supports, see Amazon EBS volume limits for Amazon EC2 instances.
Instance Type Number of EBS cards c8gb.48xlarge 2 c8gb.metal-48xl 2 m8gb.48xlarge 2 r8gb.48xlarge 2 r8gb.metal-48xl 2
