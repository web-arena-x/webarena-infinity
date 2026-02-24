# Troubleshoot Amazon EC2 Linux instances with failed status checks

Source: apps/user-manuals/aws/ec2-ug.pdf

---

### Step 9: Clean up (Optional) You can terminate the temporary instance if you have no further use for it. Select the temporary instance, and choose Instance state, Terminate (delete) instance.
# Troubleshoot Amazon EC2 Linux instances with failed status checks checks The following information can help you troubleshoot issues if your Linux instance fails a status check. First determine whether your applications are exhibiting any problems. If you verify that the instance is not running your applications as expected, review the status check information and the system logs.
For examples of problems that can cause status checks to fail, see Status checks for Amazon EC2 instances.
Contents
- Review status check information
- Retrieve the system logs
- Troubleshoot system log errors for Linux instances
- Out of memory: kill process
- ERROR: mmu_update failed (Memory management update failed)
- I/O error (block device failure)
- I/O ERROR: neither local nor remote disk (Broken distributed block device)
- request_module: runaway loop modprobe (Looping legacy kernel modprobe on older Linux versions)
- "FATAL: kernel too old" and "fsck: No such file or directory while trying to open /dev" (Kernel and AMI mismatch)
- "FATAL: Could not load /lib/modules" or "BusyBox" (Missing kernel modules)
- ERROR Invalid kernel (EC2 incompatible kernel)
- fsck: No such file or directory while trying to open... (File system not found)
- General error mounting filesystems (failed mount)
- VFS: Unable to mount root fs on unknown-block (Root filesystem mismatch)

- Error: Unable to determine major/minor number of root device... (Root file system/device mismatch)
- XENBUS: Device with no driver...
- ... days without being checked, check forced (File system check required)
- fsck died with exit status... (Missing device)
- GRUB prompt (grubdom>)
- Bringing up interface eth0: Device eth0 has different MAC address than expected, ignoring.
(Hard-coded MAC address)
- Unable to load SELinux Policy. Machine is in enforcing mode. Halting now. (SELinux misconfiguration)
- XENBUS: Timeout connecting to devices (Xenbus timeout)
## Review status check information To investigate impaired instances using the Amazon EC2 console
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Instances, and then select your instance.
3. Select the Status and alarms tab to see the individual results for all System status checks, Instance status checks, and Attached EBS status checks.
If a status check has failed, you can try one of the following options:
- Create an alarm to recover the instance in response to the failed status check. For more information, see Create alarms that stop, terminate, reboot, or recover an instance.
- (Instance status checks) If you changed the instance type to a Nitro-based instance, status checks fail if you migrated from an instance that does not have the required ENA and NVMe drivers. For more information, see Compatibility for changing the instance type.
- For an instance with an EBS root volume, stop and restart the instance. For more information, see Stop and start Amazon EC2 instances.
- For an instance with an instance store root volume, terminate the instance and launch a replacement instance. For more information, see Terminate Amazon EC2 instances.
- Wait for Amazon EC2 to resolve the issue.

- Contact Support or post your issue to AWS re:Post.
- If your instance is in an Auto Scaling group:
- (System status checks and instance status checks) By default, Amazon EC2 Auto Scaling automatically launches a replacement instance. For more information, see Health checks for instances in an Auto Scaling group in the Amazon EC2 Auto Scaling User Guide.
- (Attached EBS status checks) You must configure Amazon EC2 Auto Scaling to automatically launch a replacement instance. For more information, see  Monitor and replace Auto Scaling instances with impaired Amazon EBS volumes in the Amazon EC2 Auto Scaling User Guide.
- Retrieve the system log and look for errors. For more information, see Retrieve the system logs.
## Retrieve the system logs If an instance status check fails, you can reboot the instance and retrieve the system logs. The logs may reveal an error that can help you troubleshoot the issue. Rebooting clears unnecessary information from the logs.
To reboot an instance and retrieve the system log
1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
2. In the navigation pane, choose Instances, and select your instance.
3. Choose Instance state, Reboot instance. It might take a few minutes for your instance to reboot.
4. Verify that the problem still exists; in some cases, rebooting may resolve the problem.
5. When the instance is in the running state, choose Actions, Monitor and troubleshoot, Get system log.
6. Review the log that appears on the screen, and use the list of known system log error statements below to troubleshoot your issue.
7. If your issue is not resolved, you can post your issue to AWS re:Post.
## Troubleshoot system log errors for Linux instances For Linux instances that have failed an instance status check, such as the instance reachability check, verify that you followed the steps above to retrieve the system log. The following list contains some common system log errors and suggested actions you can take to resolve the issue for each error.

Memory Errors
- Out of memory: kill process
- ERROR: mmu_update failed (Memory management update failed)
Device Errors
- I/O error (block device failure)
- I/O ERROR: neither local nor remote disk (Broken distributed block device)
Kernel Errors
- request_module: runaway loop modprobe (Looping legacy kernel modprobe on older Linux versions)
- "FATAL: kernel too old" and "fsck: No such file or directory while trying to open /dev" (Kernel and AMI mismatch)
- "FATAL: Could not load /lib/modules" or "BusyBox" (Missing kernel modules)
- ERROR Invalid kernel (EC2 incompatible kernel)
File System Errors
- fsck: No such file or directory while trying to open... (File system not found)
- General error mounting filesystems (failed mount)
- VFS: Unable to mount root fs on unknown-block (Root filesystem mismatch)
- Error: Unable to determine major/minor number of root device... (Root file system/device mismatch)
- XENBUS: Device with no driver...
- ... days without being checked, check forced (File system check required)
- fsck died with exit status... (Missing device)
Operating System Errors
- GRUB prompt (grubdom>)

- Bringing up interface eth0: Device eth0 has different MAC address than expected, ignoring.
(Hard-coded MAC address)
- Unable to load SELinux Policy. Machine is in enforcing mode. Halting now. (SELinux misconfiguration)
- XENBUS: Timeout connecting to devices (Xenbus timeout)
## Out of memory: kill process An out-of-memory error is indicated by a system log entry similar to the one shown below.
[115879.769795] Out of memory: kill process 20273 (httpd) score 1285879 or a child [115879.769795] Killed process 1917 (php-cgi) vsz:467184kB, anon- rss:101196kB, file-rss:204kB
### Potential cause Exhausted memory
### Suggested actions For this instance type Do this Amazon EBS-backed Do one of the following:
- Stop the instance, and modify the instance to use a different instance type, and start the instance again. For example, a larger or a memory-optimized instance type.
- Reboot the instance to return it to a non- impaired status. The problem will probably occur again unless you change the instance type.
Instance store-backed Do one of the following:
- Terminate the instance and launch a new instance, specifying a different instance

For this instance type Do this type. For example, a larger or a memory-op timized instance type.
- Reboot the instance to return it to an unimpaired status. The problem will probably occur again unless you change the instance type.
## ERROR: mmu_update failed (Memory management update failed)
Memory management update failures are indicated by a system log entry similar to the following:
...
Press `ESC' to enter the menu... 0   [H[J  Booting 'Amazon Linux 2011.09 (2.6.35.14-95.38.amzn1.i686)' root (hd0)
 Filesystem type is ext2fs, using whole disk kernel /boot/vmlinuz-2.6.35.14-95.38.amzn1.i686 root=LABEL=/ console=hvc0 LANG= en_US.UTF-8 KEYTABLE=us initrd /boot/initramfs-2.6.35.14-95.38.amzn1.i686.img ERROR: mmu_update failed with rc=-22
### Potential cause Issue with Amazon Linux
### Suggested action Post your issue to AWS re:Post or contact Support.

## I/O error (block device failure)
An input/output error is indicated by a system log entry similar to the following example:
[9943662.053217] end_request: I/O error, dev sde, sector 52428288 [9943664.191262] end_request: I/O error, dev sde, sector 52428168 [9943664.191285] Buffer I/O error on device md0, logical block 209713024 [9943664.191297] Buffer I/O error on device md0, logical block 209713025 [9943664.191304] Buffer I/O error on device md0, logical block 209713026 [9943664.191310] Buffer I/O error on device md0, logical block 209713027 [9943664.191317] Buffer I/O error on device md0, logical block 209713028 [9943664.191324] Buffer I/O error on device md0, logical block 209713029 [9943664.191332] Buffer I/O error on device md0, logical block 209713030 [9943664.191339] Buffer I/O error on device md0, logical block 209713031 [9943664.191581] end_request: I/O error, dev sde, sector 52428280 [9943664.191590] Buffer I/O error on device md0, logical block 209713136 [9943664.191597] Buffer I/O error on device md0, logical block 209713137 [9943664.191767] end_request: I/O error, dev sde, sector 52428288 [9943664.191970] end_request: I/O error, dev sde, sector 52428288 [9943664.192143] end_request: I/O error, dev sde, sector 52428288 [9943664.192949] end_request: I/O error, dev sde, sector 52428288 [9943664.193112] end_request: I/O error, dev sde, sector 52428288 [9943664.193266] end_request: I/O error, dev sde, sector 52428288 ...
### Potential causes Instance type Potential cause Amazon EBS-backed A failed Amazon EBS volume Instance store-backed A failed physical drive
### Suggested actions For this instance type Do this Amazon EBS-backed Use the following procedure:
1. Stop the instance.

For this instance type Do this
2. Detach the volume.
3. Attempt to recover the volume.
Note It's good practice to snapshot your Amazon EBS volumes often. This dramatically decreases the risk of data loss as a result of failure.
4. Re-attach the volume to the instance.
5. Start the instance.
Instance store-backed Terminate the instance and launch a new instance.
Note Data cannot be recovered. Recover from backups.
Note It's a good practice to use either Amazon S3 or Amazon EBS for backups. Instance store volumes are directly tied to single host and single disk failures.

## I/O ERROR: neither local nor remote disk (Broken distributed block device) device)
An input/output error on the device is indicated by a system log entry similar to the following example:
... block drbd1: Local IO failed in request_timer_fn. Detaching...
Aborting journal on device drbd1-8. block drbd1: IO ERROR: neither local nor remote disk Buffer I/O error on device drbd1, logical block 557056 lost page write due to I/O error on drbd1 JBD2: I/O error detected when updating journal superblock for drbd1-8.
### Potential causes Instance type Potential cause Amazon EBS-backed A failed Amazon EBS volume Instance store-backed A failed physical drive
### Suggested action Terminate the instance and launch a new instance.
For an Amazon EBS-backed instance you can recover data from a recent snapshot by creating an image from it. Any data added after the snapshot cannot be recovered.
## request_module: runaway loop modprobe (Looping legacy kernel modprobe on older Linux versions) modprobe on older Linux versions)
This condition is indicated by a system log similar to the one shown below. Using an unstable or old Linux kernel (for example, 2.6.16-xenU) can cause an interminable loop condition at startup.

Linux version 2.6.16-xenU (builder@xenbat.amazonsa) (gcc version 4.0.1 20050727 (Red Hat 4.0.1-5)) #1 SMP Mon May 28 03:41:49 SAST 2007 BIOS-provided physical RAM map:
 Xen: 0000000000000000 - 0000000026700000 (usable)
0MB HIGHMEM available.
... request_module: runaway loop modprobe binfmt-464c request_module: runaway loop modprobe binfmt-464c request_module: runaway loop modprobe binfmt-464c request_module: runaway loop modprobe binfmt-464c request_module: runaway loop modprobe binfmt-464c
### Suggested actions For this instance type Do this Amazon EBS-backed Use a newer kernel, either GRUB-based or static, using one of the following options:
Option 1: Terminate the instance and launch a new instance, specifying the -kernel and - ramdisk parameters.
Option 2:
1. Stop the instance.
2. Modify the kernel and ramdisk attributes to use a newer kernel.
3. Start the instance.

For this instance type Do this Instance store-backed Terminate the instance and launch a new instance, specifying the -kernel and - ramdisk parameters.
## "FATAL: kernel too old" and "fsck: No such file or directory while trying to open /dev" (Kernel and AMI mismatch) to open /dev" (Kernel and AMI mismatch)
This condition is indicated by a system log similar to the one shown below.
Linux version 2.6.16.33-xenU (root@dom0-0-50-45-1-a4-ee.z-2.aes0.internal)
(gcc version 4.1.1 20070105 (Red Hat 4.1.1-52)) #2 SMP Wed Aug 15 17:27:36 SAST 2007 ...
FATAL: kernel too old Kernel panic - not syncing: Attempted to kill init!
### Potential causes Incompatible kernel and userland
### Suggested actions For this instance type Do this Amazon EBS-backed Use the following procedure:
1. Stop the instance.
2. Modify the configuration to use a newer kernel.
3. Start the instance.
Instance store-backed Use the following procedure:
1. Create an AMI that uses a newer kernel.
2. Terminate the instance.
"FATAL: kernel too old" and "fsck: No such file or directory while trying to open /dev" (Kernel and AMI

For this instance type Do this
3. Start a new instance from the AMI you created.
## "FATAL: Could not load /lib/modules" or "BusyBox" (Missing kernel modules) modules)
This condition is indicated by a system log similar to the one shown below.
[    0.370415] Freeing unused kernel memory: 1716k freed Loading, please wait...
WARNING: Couldn't open directory /lib/modules/2.6.34-4-virtual: No such file or directory FATAL: Could not open /lib/modules/2.6.34-4-virtual/modules.dep.temp for writing: No such file or directory FATAL: Could not load /lib/modules/2.6.34-4-virtual/modules.dep: No such file or directory Couldn't get a file descriptor referring to the console Begin: Loading essential drivers... ...
FATAL: Could not load /lib/modules/2.6.34-4-virtual/modules.dep: No such file or directory FATAL: Could not load /lib/modules/2.6.34-4-virtual/modules.dep: No such file or directory Done.
Begin: Running /scripts/init-premount ...
Done.
Begin: Mounting root file system... ...
Begin: Running /scripts/local-top ...
Done.
Begin: Waiting for root file system... ...
Done.
Gave up waiting for root device.  Common problems:
 - Boot args (cat /proc/cmdline)
   - Check rootdelay= (did the system wait long enough?)
   - Check root= (did the system wait for the right device?)
 - Missing modules (cat /proc/modules; ls /dev)
FATAL: Could not load /lib/modules/2.6.34-4-virtual/modules.dep: No such file or directory FATAL: Could not load /lib/modules/2.6.34-4-virtual/modules.dep: No such file or directory

ALERT! /dev/sda1 does not exist. Dropping to a shell!
BusyBox v1.13.3 (Ubuntu 1:1.13.3-1ubuntu5) built-in shell (ash)
Enter 'help' for a list of built-in commands.
(initramfs)
### Potential causes One or more of the following conditions can cause this problem:
- Missing ramdisk
- Missing correct modules from ramdisk
- Amazon EBS root volume not correctly attached as /dev/sda1
### Suggested actions For this instance type Do this Amazon EBS-backed Use the following procedure:
1. Select corrected ramdisk for the Amazon EBS volume.
2. Stop the instance.
3. Detach the volume and repair it.
4. Attach the volume to the instance.
5. Start the instance.
6. Modify the AMI to use the corrected ramdisk.
Instance store-backed Use the following procedure:
1. Terminate the instance and launch a new instance with the correct ramdisk.
2. Create a new AMI with the correct ramdisk.

## ERROR Invalid kernel (EC2 incompatible kernel)
This condition is indicated by a system log similar to the one shown below.
... root (hd0)
 Filesystem type is ext2fs, using whole disk kernel /vmlinuz root=/dev/sda1 ro initrd /initrd.img ERROR Invalid kernel: elf_xen_note_check: ERROR: Will only load images built for the generic loader or Linux images xc_dom_parse_image returned -1 Error 9: Unknown boot failure Booting 'Fallback'

root (hd0)
 Filesystem type is ext2fs, using whole disk kernel /vmlinuz.old root=/dev/sda1 ro Error 15: File not found
### Potential causes One or both of the following conditions can cause this problem:
- Supplied kernel is not supported by GRUB
- Fallback kernel does not exist
### Suggested actions For this instance type Do this Amazon EBS-backed Use the following procedure:

For this instance type Do this
1. Stop the instance.
2. Replace with working kernel.
3. Install a fallback kernel.
4. Modify the AMI by correcting the kernel.
Instance store-backed Use the following procedure:
1. Terminate the instance and launch a new instance with the correct kernel.
2. Create an AMI with the correct kernel.
3. (Optional) Seek technical assistance for data recovery using Support.
## fsck: No such file or directory while trying to open... (File system not found) found)
This condition is indicated by a system log similar to the one shown below.
  Welcome to Fedora Press 'I' to enter interactive startup.
Setting clock : Wed Oct 26 05:52:05 EDT 2011 [  OK  ]
Starting udev: [  OK  ]
Setting hostname localhost:  [  OK  ]
No devices found Setting up Logical Volume Management: File descriptor 7 left open No volume groups found [  OK  ]
Checking filesystems Checking all file systems.
[/sbin/fsck.ext3 (1) -- /] fsck.ext3 -a /dev/sda1 /dev/sda1: clean, 82081/1310720 files, 2141116/2621440 blocks [/sbin/fsck.ext3 (1) -- /mnt/dbbackups] fsck.ext3 -a /dev/sdh fsck.ext3: No such file or directory while trying to open /dev/sdh

/dev/sdh:
The superblock could not be read or does not describe a correct ext2 filesystem.  If the device is valid and it really contains an ext2 filesystem (and not swap or ufs or something else), then the superblock is corrupt, and you might try running e2fsck with an alternate superblock: e2fsck -b 8193 <device>
[FAILED]
*** An error occurred during the file system check.
*** Dropping you to a shell; the system will reboot *** when you leave the shell.
Give root password for maintenance (or type Control-D to continue):
### Potential causes
- A bug exists in ramdisk filesystem definitions /etc/fstab
- Misconfigured filesystem definitions in /etc/fstab
- Missing/failed drive
### Suggested actions For this instance type Do this Amazon EBS-backed Use the following procedure:
1. Stop the instance, detach the root volume, repair/modify /etc/fstab the volume, attach the volume to the instance, and start the instance.
2. Fix ramdisk to include modified /etc/fstab (if applicable).
3. Modify the AMI to use a newer ramdisk.

For this instance type Do this The sixth field in the fstab defines availabil ity requirements of the mount – a nonzero value implies that an fsck will be done on that volume and must succeed. Using this field can be problematic in Amazon EC2 because a failure typically results in an interactive console prompt that is not currently available in Amazon EC2. Use care with this feature and read the Linux man page for fstab.
Instance store-backed Use the following procedure:
1. Terminate the instance and launch a new instance.
2. Detach any errant Amazon EBS volumes and the reboot instance.
3. (Optional) Seek technical assistance for data recovery using Support.
## General error mounting filesystems (failed mount)
This condition is indicated by a system log similar to the one shown below.
Loading xenblk.ko module xen-vbd: registered block device major 8 Loading ehci-hcd.ko module Loading ohci-hcd.ko module Loading uhci-hcd.ko module USB Universal Host Controller Interface driver v3.0 Loading mbcache.ko module Loading jbd.ko module Loading ext3.ko module Creating root device.
Mounting root filesystem. kjournald starting.  Commit interval 5 seconds

EXT3-fs: mounted filesystem with ordered data mode.
Setting up other filesystems.
Setting up new root fs no fstab.sys, mounting internal defaults Switching to new root and running init. unmounting old /dev unmounting old /proc unmounting old /sys mountall:/proc: unable to mount: Device or resource busy mountall:/proc/self/mountinfo: No such file or directory mountall: root filesystem isn't mounted init: mountall main process (221) terminated with status 1 General error mounting filesystems.
A maintenance shell will now be started.
CONTROL-D will terminate this shell and re-try.
Press enter for maintenance (or type Control-D to continue):
### Potential causes Instance type Potential cause Amazon EBS-backed
- Detached or failed Amazon EBS volume.
- Corrupted filesystem.
- Mismatched ramdisk and AMI combination (such as Debian ramdisk with a SUSE AMI).
Instance store-backed
- A failed drive.
- A corrupted file system.
- A mismatched ramdisk and combination (for example, a Debian ramdisk with a SUSE AMI).

### Suggested actions For this instance type Do this Amazon EBS-backed Use the following procedure:
1. Stop the instance.
2. Detach the root volume.
3. Attach the root volume to a known working instance.
4. Run filesystem check (fsck -a /dev/...).
5. Fix any errors.
6. Detach the volume from the known working instance.
7. Attach the volume to the stopped instance.
8. Start the instance.
9. Recheck the instance status.
Instance store-backed Try one of the following:
- Start a new instance.
- (Optional) Seek technical assistance for data recovery using Support.
## VFS: Unable to mount root fs on unknown-block (Root filesystem mismatch) mismatch)
This condition is indicated by a system log similar to the one shown below.
Linux version 2.6.16-xenU (builder@xenbat.amazonsa) (gcc version 4.0.1 20050727 (Red Hat 4.0.1-5)) #1 SMP Mon May 28 03:41:49 SAST 2007 ...
Kernel command line:  root=/dev/sda1 ro 4 ...
Registering block device major 8 ...

Kernel panic - not syncing: VFS: Unable to mount root fs on unknown-block(8,1)
### Potential causes Instance type Potential cause Amazon EBS-backed
- Device not attached correctly.
- Root device not attached at correct device point.
- Filesystem not in expected format.
- Use of legacy kernel (such as 2.6.16-XenU).
- A recent kernel update on your instance (faulty update, or an update bug)
Instance store-backed Hardware device failure.
### Suggested actions For this instance type Do this Amazon EBS-backed Do one of the following:
- Stop and then restart the instance.
- Modify root volume to attach at the correct device point, possible /dev/sda1 instead of / dev/sda.
- Stop and modify to use modern kernel.
- Refer to the documentation for your Linux distribution to check for known update bugs. Change or reinstall the kernel.
Instance store-backed Terminate the instance and launch a new instance using a modern kernel.

## Error: Unable to determine major/minor number of root device... (Root file system/device mismatch) file system/device mismatch)
This condition is indicated by a system log similar to the one shown below.
...
XENBUS: Device with no driver: device/vif/0 XENBUS: Device with no driver: device/vbd/2048 drivers/rtc/hctosys.c: unable to open rtc device (rtc0)
Initializing network drop monitor service Freeing unused kernel memory: 508k freed :: Starting udevd... done.
:: Running Hook [udev]
:: Triggering uevents...<30>udevd[65]: starting version 173 done.
Waiting 10 seconds for device /dev/xvda1 ...
Root device '/dev/xvda1' doesn't exist. Attempting to create it.
ERROR: Unable to determine major/minor number of root device '/dev/xvda1'.
You are being dropped to a recovery shell Type 'exit' to try and continue booting sh: can't access tty; job control turned off [ramfs /]#
### Potential causes
- Missing or incorrectly configured virtual block device driver
- Device enumeration clash (sda versus xvda or sda instead of sda1)
- Incorrect choice of instance kernel
### Suggested actions For this instance type Do this Amazon EBS-backed Use the following procedure:
1. Stop the instance.
2. Detach the volume.
3. Fix the device mapping problem.

For this instance type Do this
4. Start the instance.
5. Modify the AMI to address device mapping issues.
Instance store-backed Use the following procedure:
1. Create a new AMI with the appropriate fix (map block device correctly).
2. Terminate the instance and launch a new instance from the AMI you created.
## XENBUS: Device with no driver...
This condition is indicated by a system log similar to the one shown below.
XENBUS: Device with no driver: device/vbd/2048 drivers/rtc/hctosys.c: unable to open rtc device (rtc0)
Initializing network drop monitor service Freeing unused kernel memory: 508k freed :: Starting udevd... done.
:: Running Hook [udev]
:: Triggering uevents...<30>udevd[65]: starting version 173 done.
Waiting 10 seconds for device /dev/xvda1 ...
Root device '/dev/xvda1' doesn't exist. Attempting to create it.
ERROR: Unable to determine major/minor number of root device '/dev/xvda1'.
You are being dropped to a recovery shell Type 'exit' to try and continue booting sh: can't access tty; job control turned off [ramfs /]#
### Potential causes
- Missing or incorrectly configured virtual block device driver
- Device enumeration clash (sda versus xvda)
- Incorrect choice of instance kernel

### Suggested actions For this instance type Do this Amazon EBS-backed Use the following procedure:
1. Stop the instance.
2. Detach the volume.
3. Fix the device mapping problem.
4. Start the instance.
5. Modify the AMI to address device mapping issues.
Instance store-backed Use the following procedure:
1. Create an AMI with the appropriate fix (map block device correctly).
2. Terminate the instance and launch a new instance using the AMI you created.
## ... days without being checked, check forced (File system check required) required)
This condition is indicated by a system log similar to the one shown below.
...
Checking filesystems Checking all file systems.
[/sbin/fsck.ext3 (1) -- /] fsck.ext3 -a /dev/sda1 /dev/sda1 has gone 361 days without being checked, check forced
### Potential causes Filesystem check time passed; a filesystem check is being forced.

### Suggested actions
- Wait until the filesystem check completes. A filesystem check can take a long time depending on the size of the root filesystem.
- Modify your filesystems to remove the filesystem check (fsck) enforcement using tune2fs or tools appropriate for your filesystem.
## fsck died with exit status... (Missing device)
This condition is indicated by a system log similar to the one shown below.
Cleaning up ifupdown....
Loading kernel modules...done.
...
Activating lvm and md swap...done.
Checking file systems...fsck from util-linux-ng 2.16.2 /sbin/fsck.xfs: /dev/sdh does not exist fsck died with exit status 8 [31mfailed (code 8).[39;49m
### Potential causes
- Ramdisk looking for missing drive
- Filesystem consistency check forced
- Drive failed or detached
### Suggested actions For this instance type Do this Amazon EBS-backed Try one or more of the following to resolve the issue:
- Stop the instance, attach the volume to an existing running instance.
- Manually run consistency checks.
- Fix ramdisk to include relevant utilities.

For this instance type Do this
- Modify filesystem tuning parameters to remove consistency requirements (not recommended).
Instance store-backed Try one or more of the following to resolve the issue:
- Rebundle ramdisk with correct tooling.
- Modify file system tuning parameters to remove consistency requirements (not recommended).
- Terminate the instance and launch a new instance.
- (Optional) Seek technical assistance for data recovery using Support.
## GRUB prompt (grubdom>)
This condition is indicated by a system log similar to the one shown below.
    GNU GRUB  version 0.97  (629760K lower / 0K upper memory)
       [ Minimal BASH-like line editing is supported.   For the   first   word,  TAB  lists  possible  command completions.  Anywhere else TAB lists the possible completions of a device/filename. ] grubdom>

### Potential causes Instance type
### Potential causes Amazon EBS-backed
- Missing GRUB configuration file.
- Incorrect GRUB image used, expecting GRUB configuration file at a different location.
- Unsupported filesystem used to store your GRUB configuration file (for example, converting your root file system to a type that is not supported by an earlier version of GRUB).
Instance store-backed
- Missing GRUB configuration file.
- Incorrect GRUB image used, expecting GRUB configuration file at a different location.
- Unsupported filesystem used to store your GRUB configuration file (for example, converting your root file system to a type that is not supported by an earlier version of GRUB).
### Suggested actions For this instance type Do this Amazon EBS-backed Option 1: Modify the AMI and relaunch the instance:
1. Modify the source AMI to create a GRUB configuration file at the standard location (/ boot/grub/menu.lst).
2. Verify that your version of GRUB supports the underlying file system type and upgrade GRUB if necessary.

For this instance type Do this
3. Pick the appropriate GRUB image, (hd0-1st drive or hd00 – 1st drive, 1st partition).
4. Terminate the instance and launch a new one using the AMI that you created.
Option 2: Fix the existing instance:
1. Stop the instance.
2. Detach the root filesystem.
3. Attach the root filesystem to a known working instance.
4. Mount filesystem.
5. Create a GRUB configuration file.
6. Verify that your version of GRUB supports the underlying file system type and upgrade GRUB if necessary.
7. Detach filesystem.
8. Attach to the original instance.
9. Modify kernel attribute to use the appropria te GRUB image (1st disk or 1st partition on 1st disk).
10.Start the instance.

For this instance type Do this Instance store-backed Option 1: Modify the AMI and relaunch the instance:
1. Create the new AMI with a GRUB configura tion file at the standard location (/boot/gr ub/menu.lst).
2. Pick the appropriate GRUB image, (hd0-1st drive or hd00 – 1st drive, 1st partition).
3. Verify that your version of GRUB supports the underlying file system type and upgrade GRUB if necessary.
4. Terminate the instance and launch a new instance using the AMI you created.
Option 2: Terminate the instance and launch a new instance, specifying the correct kernel.
Note To recover data from the existing instance, contact Support.
## Bringing up interface eth0: Device eth0 has different MAC address than expected, ignoring. (Hard-coded MAC address) expected, ignoring. (Hard-coded MAC address)
This condition is indicated by a system log similar to the one shown below.
...
Bringing up loopback interface:  [  OK  ]
Bringing up interface eth0:  Device eth0 has different MAC address than expected, ignoring.
[FAILED]
Bringing up interface eth0: Device eth0 has different MAC address than expected, ignoring. (Hard-coded

Starting auditd: [  OK  ]
### Potential causes There is a hardcoded interface MAC in the AMI configuration
### Suggested actions For this instance type Do this Amazon EBS-backed Do one of the following:
- Modify the AMI to remove the hardcoding and relaunch the instance.
- Modify the instance to remove the hardcoded MAC address.
OR Use the following procedure:
1. Stop the instance.
2. Detach the root volume.
3. Attach the volume to another instance and modify the volume to remove the hardcoded MAC address.
4. Attach the volume to the original instance.
5. Start the instance.
Instance store-backed Do one of the following:
- Modify the instance to remove the hardcoded MAC address.
- Terminate the instance and launch a new instance.
Bringing up interface eth0: Device eth0 has different MAC address than expected, ignoring. (Hard-coded

## Unable to load SELinux Policy. Machine is in enforcing mode. Halting now. (SELinux misconfiguration) now. (SELinux misconfiguration)
This condition is indicated by a system log similar to the one shown below. audit(1313445102.626:2): enforcing=1 old_enforcing=0 auid=4294967295 Unable to load SELinux Policy. Machine is in enforcing mode. Halting now.
Kernel panic - not syncing: Attempted to kill init!
Potential causes SELinux has been enabled in error:
- Supplied kernel is not supported by GRUB
- Fallback kernel does not exist
### Suggested actions For this instance type Do this Amazon EBS-backed Use the following procedure:
1. Stop the failed instance.
2. Detach the failed instance's root volume.
3. Attach the root volume to another running Linux instance (later referred to as a recovery instance).
4. Connect to the recovery instance and mount the failed instance's root volume.
5. Disable SELinux on the mounted root volume. This process varies across Linux distributions; for more information, consult your OS-specific documentation.

For this instance type Do this Note On some systems, you disable SELinux by setting SELINUX=d isabled  in the /mount_poi nt /etc/sysconfig/selinux file, where mount_point  is the location that you mounted the volume on your recovery instance.
6. Unmount and detach the root volume from the recovery instance and reattach it to the original instance.
7. Start the instance.
Instance store-backed Use the following procedure:
1. Terminate the instance and launch a new instance.
2. (Optional) Seek technical assistance for data recovery using Support.
## XENBUS: Timeout connecting to devices (Xenbus timeout)
This condition is indicated by a system log similar to the one shown below.
Linux version 2.6.16-xenU (builder@xenbat.amazonsa) (gcc version 4.0.1 20050727 (Red Hat 4.0.1-5)) #1 SMP Mon May 28 03:41:49 SAST 2007 ...
XENBUS: Timeout connecting to devices!
...
Kernel panic - not syncing: No init found.  Try passing init= option to kernel.
