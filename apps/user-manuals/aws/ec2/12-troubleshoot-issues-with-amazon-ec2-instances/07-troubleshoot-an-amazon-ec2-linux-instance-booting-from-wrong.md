# Troubleshoot an Amazon EC2 Linux instance booting from wrong volume

Source: apps/user-manuals/aws/ec2-ug.pdf

---

### Potential causes
- The block device is not connected to the instance
- This instance is using an old instance kernel
### Suggested actions For this instance type Do this Amazon EBS-backed Do one of the following:
- Modify the AMI and instance to use a modern kernel and relaunch the instance.
- Reboot the instance.
Instance store-backed Do one of the following:
- Terminate the instance.
- Modify the AMI to use a modern kernel, and launch a new instance using this AMI.
# Troubleshoot an Amazon EC2 Linux instance booting from wrong volume wrong volume In some situations, a volume other than the volume attached to /dev/xvda or /dev/sda becomes the root volume of a Linux instance. This can happen when you have attached the root volume of another instance, or a volume created from the snapshot of a root volume, to an instance with an existing root volume.
This is due to how the initial ramdisk in Linux works. It chooses the volume defined as / in the / etc/fstab, and in some distributions, this is determined by the label attached to the volume partition. Specifically, you find that your /etc/fstab looks something like the following:
LABEL=/ / ext4 defaults,noatime 1 1 tmpfs /dev/shm tmpfs defaults 0 0 devpts /dev/pts devpts gid=5,mode=620 0 0

sysfs /sys sysfs defaults 0 0 proc /proc proc defaults 0 0 If you check the label of both volumes, you see that they both contain the / label:
[ec2-user ~]$ sudo e2label /dev/xvda1 / [ec2-user ~]$ sudo e2label /dev/xvdf1 / In this example, you could end up having /dev/xvdf1 become the root volume that your instance boots to after the initial ramdisk runs, instead of the /dev/xvda1 volume from which you had intended to boot. To solve this, use the same e2label command to change the label of the attached volume that you do not want to boot from.
In some cases, specifying a UUID in /etc/fstab can resolve this. However, if both volumes come from the same snapshot, or the secondary is created from a snapshot of the primary volume, they share a UUID.
[ec2-user ~]$ sudo blkid /dev/xvda1: LABEL="/" UUID=73947a77-ddbe-4dc7-bd8f-3fe0bc840778 TYPE="ext4"
 PARTLABEL="Linux" PARTUUID=d55925ee-72c8-41e7-b514-7084e28f7334 /dev/xvdf1: LABEL="old/" UUID=73947a77-ddbe-4dc7-bd8f-3fe0bc840778 TYPE="ext4"
 PARTLABEL="Linux" PARTUUID=d55925ee-72c8-41e7-b514-7084e28f7334 To change the label of an attached ext4 volume
1. Use the e2label command to change the label of the volume to something other than /.
[ec2-user ~]$ sudo e2label /dev/xvdf1 old/
2. Verify that the volume has the new label.
[ec2-user ~]$ sudo e2label /dev/xvdf1 old/ To change the label of an attached xfs volume
- Use the xfs_admin command to change the label of the volume to something other than /.
