# Send a diagnostic interrupt to debug an unreachable Amazon EC2 instance

Source: apps/user-manuals/aws/ec2-ug.pdf

---

shutdown -r -t 0 Command prompt To disable SAC and the boot menu on a Windows instance
1. Connect to your instance and perform the following steps from the command prompt.
2. First disable the boot menu by changing the value to no. bcdedit /set {bootmgr} displaybootmenu no
3. Then disable SAC by changing the value to off. bcdedit /ems {current} off
4. Apply the updated configuration by rebooting the instance. shutdown -r -t 0
# Send a diagnostic interrupt to debug an unreachable Amazon EC2 instance EC2 instance Warning Diagnostic interrupts are intended for use by advanced users. Incorrect usage could negatively impact your instance. Sending a diagnostic interrupt to an instance could trigger an instance to crash and reboot, which could lead to the loss of data.
You can send a diagnostic interrupt to an unreachable or unresponsive instance to manually trigger a kernel panic for a Linux instance, or a stop error (commonly referred to as a blue screen error) for a Windows instance.
### Linux instances

Linux operating systems typically crash and reboot when a kernel panic occurs. The specific behavior of the operating system depends on its configuration. A kernel panic can also be used to cause the instance's operating system kernel to perform tasks, such as generating a crash dump file. You can then use the information in the crash dump file to conduct root cause analysis and debug the instance. The crash dump data is generated locally by the operating system on the instance itself.
### Windows instances In general, Windows operating systems crash and reboot when a stop error occurs, but the specific behavior depends on its configuration. A stop error can also cause the operating system to write debugging information, such as a kernel memory dump, to a file. You can then use this information to conduct root cause analysis to debug the instance. The memory dump data is generated locally by the operating system on the instance itself.
Before sending a diagnostic interrupt to your instance, we recommend that you consult the documentation for your operating system and then make the necessary configuration changes.
Contents
- Supported instance types
- Prerequisites
- Send a diagnostic interrupt
## Supported instance types Diagnostic interrupt is supported on all Nitro-based instance types, except those powered by AWS Graviton processors. For more information, see instances built on the AWS Nitro System and AWS Graviton.
## Prerequisites Before using a diagnostic interrupt, you must configure your instance's operating system. This ensures that it performs the actions that you need when a kernel panic (Linux instances) or stop error (Windows instances) occurs.

Linux instances To configure Amazon Linux 2 or Amazon Linux 2023 to generate a crash dump when a kernel panic occurs
1. Connect to your instance.
2. Install kexec and kdump.
[ec2-user ~]$ sudo yum install kexec-tools -y
3. Configure the kernel to reserve an appropriate amount of memory for the secondary kernel.
The amount of memory to reserve depends on the total available memory of your instance.
Open the /etc/default/grub file using your preferred text editor, locate the line that starts with GRUB_CMDLINE_LINUX_DEFAULT, and then add the crashkernel parameter in the following format: crashkernel=memory_to_reserve. For example, to reserve 256MB, modify the grub file as follows:
GRUB_CMDLINE_LINUX_DEFAULT="crashkernel=256M console=tty0 console=ttyS0,115200n8 net.ifnames=0 biosdevname=0 nvme_core.io_timeout=4294967295 rd.emergency=poweroff rd.shell=0"
GRUB_TIMEOUT=0 GRUB_DISABLE_RECOVERY="true"
4. Save the changes and close the grub file.
5. Rebuild the GRUB2 configuration file.
[ec2-user ~]$ sudo grub2-mkconfig -o /boot/grub2/grub.cfg
6. On instances based on Intel and AMD processors, the send-diagnostic-interrupt command sends an unknown non-maskable interrupt (NMI) to the instance. You must configure the kernel to crash when it receives the unknown NMI. Open the /etc/sysctl.conf file using your preferred text editor and add the following. kernel.unknown_nmi_panic=1
7. Reboot and reconnect to your instance.
8. Verify that the kernel has been booted with the correct crashkernel parameter.
$ grep crashkernel /proc/cmdline

The following example output indicates successful configuration.
BOOT_IMAGE=/boot/vmlinuz-4.14.128-112.105.amzn2.x86_64 root=UUID=a1e1011e- e38f-408e-878b-fed395b47ad6 ro crashkernel=256M console=tty0 console=ttyS0,115200n8 net.ifnames=0 biosdevname=0 nvme_core.io_timeout=4294967295 rd.emergency=poweroff rd.shell=0
9. Verify that the kdump service is running.
[ec2-user ~]$ systemctl status kdump.service The following example output shows the result if the kdump service is running. kdump.service - Crash recovery kernel arming Loaded: loaded (/usr/lib/systemd/system/kdump.service; enabled; vendor preset: enabled)
   Active: active (exited) since Fri 2019-05-24 23:29:13 UTC; 22s ago Process: 2503 ExecStart=/usr/bin/kdumpctl start (code=exited, status=0/SUCCESS)
 Main PID: 2503 (code=exited, status=0/SUCCESS)
Note By default, the crash dump file is saved to /var/crash/. To change the location, modify the /etc/kdump.conf file using your preferred text editor.
To configure SUSE Linux Enterprise, Ubuntu, or Red Hat Enterprise Linux On instances based on Intel and AMD processors, the send-diagnostic-interrupt command sends an unknown non-maskable interrupt (NMI) to the instance. You must configure the kernel to crash when it receives the unknown NMI by adjusting the configuration file for your operating system. For information about how to configure the kernel to crash, see the documentation for your operating system:
- SUSE Linux Enterprise
- Ubuntu
- Red Hat Enterprise Linux (RHEL)

Windows instances To configure Windows to generate a memory dump when a stop error occurs
1. Connect to your instance.
2. Open the Control Panel and choose System, Advanced system settings.
3. In the System Properties dialog box, choose the Advanced tab.
4. In the Startup and Recovery section, choose Settings....
5. In the System failure section, configure the settings as needed, and then choose OK.
For more information about configuring Windows stop errors, see  Overview of memory dump file options for Windows.
## Send a diagnostic interrupt After you have completed the necessary configuration changes, you can send a diagnostic interrupt to your instance using the AWS CLI or Amazon EC2 API.
AWS CLI To send a diagnostic interrupt to your instance Use the send-diagnostic-interrupt command. aws ec2 send-diagnostic-interrupt --instance-id i-1234567890abcdef0 PowerShell To send a diagnostic interrupt to your instance Use the Send-EC2DiagnosticInterrupt cmdlet.
Send-EC2DiagnosticInterrupt -InstanceId i-1234567890abcdef0
