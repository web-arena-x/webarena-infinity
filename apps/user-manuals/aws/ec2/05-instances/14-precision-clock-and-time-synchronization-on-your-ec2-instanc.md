# Precision clock and time synchronization on your EC2 instance

Source: apps/user-manuals/aws/ec2-ug.pdf

---

Example 2: Configure Medium level STIG settings on your instance Run the following command to install the STIG script and run it with the Level input parameter set to Medium. For more information about input parameters, see AWSEC2- ConfigureSTIG input parameters.
Send-SSMCommand -DocumentName "AWSEC2-ConfigureSTIG" -InstanceId "i-1234567890abcdef0" -Parameter @{'Level'='Medium'} If successful, the command document installs the script and configures your instance. If the command execution failed, view the command output for details about why the execution failed.
# Precision clock and time synchronization on your EC2 instance A consistent and accurate time reference on your Amazon EC2 instance is crucial for many server tasks and processes. Time stamps in system logs play an essential role in identifying when issues occurred and the chronological order of events. When you use the AWS CLI or an AWS SDK to make requests from your instance, these tools sign requests on your behalf. If your instance's date and time settings are inaccurate, it can result in a discrepancy between the date in the signature and the date of the request, leading to AWS rejecting your requests.
To address this important aspect, Amazon offers the Amazon Time Sync Service, which is accessible from all EC2 instances and used by various AWS services. The service uses a fleet of satellite- connected and atomic reference clocks in each AWS Region to deliver accurate and current time readings of the Coordinated Universal Time (UTC) global standard.
For the best performance, we recommend using the local Amazon Time Sync Service on your EC2 instances. For a backup to the local Amazon Time Sync Service on your instances, or to connect resources outside of Amazon EC2 to the Amazon Time Sync Service, you can use the public Amazon Time Sync Service located at time.aws.com. The public Amazon Time Sync Service, like the local Amazon Time Sync Service, automatically smears any leap seconds that are added to UTC. The public Amazon Time Sync Service is supported globally by our fleet of satellite-connected and atomic reference clocks in each AWS Region.
## Hardware packet timestamping You can enable hardware packet timestamping on your instance to add a 64-bit nanosecond- precision timestamp to every incoming network packet. Because hardware packet timestamping

occurs at the hardware level—before the packet reaches the kernel, socket, or application layer —you bypass any delays added by software timestamping. The underlying reference clock for hardware timestamping is the Amazon Time Sync Service PTP hardware clock.
Benefits Hardware packet timestamping provides the following benefits:
- Improves event ordering, which can also be used to determine the actual order in which packets arrive at your EC2 instance, ensuring fair packet processing.
- Measures one-way network latency.
- Increases distributed transaction speed with higher precision and accuracy compared to most on- premises solutions.
Prerequisites and configuration To enable hardware packet timestamping, your instance must meet the following prerequisites:
- Must be a Linux instance.
- Meet the requirements to support the PTP hardware clock.
For the configuration instructions, see Hardware Packet Timestamping on the Linux kernel driver for Elastic Network Adapter (ENA) family page on GitHub.
## Leap seconds Leap seconds, introduced in 1972, are occasional one-second adjustments to UTC time to factor in irregularities in the earth's rotation in order to accommodate differences between International Atomic Time (TAI) and solar time (Ut1). To manage leap seconds on behalf of customers, we designed leap second smearing within the Amazon Time Sync Service. For more information, see Look Before You Leap – The Coming Leap Second and AWS.
Leap seconds are going away, and we are in full support of the decision made at the 27th General Conference on Weights and Measures to abandon leap seconds by or before 2035.
To support this transition, we still plan on smearing time during a leap second event when accessing the Amazon Time Sync Service over the local NTP connection or our public NTP pools (time.aws.com). The PTP hardware clock, however, does not provide a smeared time option.

In the event of a leap second, the PTP hardware clock will add the leap second following UTC standards. Leap-smeared and leap second time sources are the same in most cases. But because they differ during a leap second event, we do not recommend using both smeared and non- smeared time sources in your time client configuration during a leap second event.

Topics
- Set the time reference on your EC2 instance to use the local Amazon Time Sync Service
- Set the time reference on your EC2 instance or any internet-connected device to use the public Amazon Time Sync Service
- Compare timestamps for your Linux instances
- Change the time zone of your instance

Related resources
- AWS Compute Blog: It's About Time: Microsecond-Accurate Clocks on Amazon EC2 Instances
- AWS Cloud Operations & Migrations Blog: Manage Amazon EC2 instance clock accuracy using Amazon Time Sync Service and Amazon CloudWatch – Part 1
- (Linux) https://chrony-project.org/
## Set the time reference on your EC2 instance to use the local Amazon Time Sync Service Time Sync Service The local Amazon Time Sync Service either uses the Network Time Protocol (NTP), or provides a local Precision Time Protocol (PTP) hardware clock on supported instances. The PTP hardware clock supports either an NTP connection (Linux and Windows instances), or a direct PTP connection (Linux instances only). The NTP and direct PTP connections use the same highly accurate time source, but the direct PTP connection is more accurate than the NTP connection. The NTP connection to the Amazon Time Sync Service supports leap smearing while the PTP connection to the PTP hardware clock does not smear time. For more information, see Leap seconds.
Your instances can access the local Amazon Time Sync Service as follows:
- Through NTP at the following IP address endpoints:

- IPv4: 169.254.169.123
- IPv6: fd00:ec2::123 (Only accessible on Nitro-based instances.)
- (Linux only) Through a direct PTP connection to connect to a local PTP hardware clock:
- PHC0 Amazon Linux AMIs, Windows AMIs, and most partner AMIs configure your instance to use the NTP IPv4 endpoint by default. This is the recommended setting for most customer workloads. No further configuration is required for instances launched from these AMIs unless you want to use the IPv6 endpoint or connect directly to the PTP hardware clock.
NTP and PTP connections do not require any VPC configuration changes, and your instance does not require access to the internet.
Considerations
- There is a 1024 packet per second (PPS) limit to services that use link-local addresses. This limit includes the aggregate of Route 53 Resolver DNS Queries, Instance Metadata Service (IMDS) requests, Amazon Time Service Network Time Protocol (NTP) requests, and Windows Licensing Service (for Microsoft Windows based instances) requests.
- Only Linux instances can use a direct PTP connection to connect to the local PTP hardware clock.
Windows instances use NTP to connect to the local PTP hardware clock.
Contents
- Connect to the IPv4 endpoint of the Amazon Time Sync Service
- Connect to the IPv6 endpoint of the Amazon Time Sync Service
- Connect to the PTP hardware clock
### Connect to the IPv4 endpoint of the Amazon Time Sync Service Your AMI might already have configured the Amazon Time Sync Service by default. Otherwise, use the following procedures to configure your instance to use the local Amazon Time Sync Service through the IPv4 endpoint.
For help troubleshooting issues, see Troubleshoot NTP synchronization issues on Linux instances or Troubleshoot time issues on Windows instances.

Amazon Linux AL2023 and recent versions of Amazon Linux 2 are configured to use the Amazon Time Sync Service IPv4 endpoint by default. If you confirm that your instance is already configured, you can skip the following procedure.
To verify that chrony is configured to use the IPv4 endpoint Run the following command. In the output, the line that starts with ^* indicates the preferred time source. chronyc sources -v | grep -F ^* ^* 169.254.169.123               3   4   377    14    +12us[+9653ns] +/-  290us To configure chrony to connect to the IPv4 endpoint on older versions of Amazon Linux 2
1. Connect to your instance and uninstall the NTP service.
[ec2-user ~]$ sudo yum erase 'ntp*'
2. Install the chrony package.
[ec2-user ~]$ sudo yum install chrony
3. Open the /etc/chrony.conf file using a text editor (such as vim or nano). Add the following line before any other server or pool statements that may be present in the file, and save your changes: server 169.254.169.123 prefer iburst minpoll 4 maxpoll 4
4. Restart the chrony daemon (chronyd).
[ec2-user ~]$ sudo service chronyd restart Starting chronyd:                                          [  OK  ]

Note On RHEL and CentOS (up to version 6), the service name is chrony instead of chronyd.
5. To configure chronyd to start at each system boot, use the chkconfig command.
[ec2-user ~]$ sudo chkconfig chronyd on
6. Verify that chrony is using the 169.254.169.123 IPv4 endpoint to synchronize the time.
[ec2-user ~]$ chronyc sources -v | grep -F ^* In the output, ^* indicates the preferred time source.
^* 169.254.169.123               3   6    17    43    -30us[ -226us] +/-  287us
7. Verify the time synchronization metrics that are reported by chrony.
[ec2-user ~]$ chronyc tracking Reference ID    : A9FEA97B (169.254.169.123)
Stratum         : 4 Ref time (UTC)  : Wed Nov 22 13:18:34 2017 System time     : 0.000000626 seconds slow of NTP time Last offset     : +0.002852759 seconds RMS offset      : 0.002852759 seconds Frequency       : 1.187 ppm fast Residual freq   : +0.020 ppm Skew            : 24.388 ppm Root delay      : 0.000504752 seconds Root dispersion : 0.001112565 seconds Update interval : 64.4 seconds Leap status     : Normal

Ubuntu To configure chrony to connect to the IPv4 endpoint on Ubuntu
1. Connect to your instance and use apt to install the chrony package. ubuntu:~$ sudo apt install chrony Note If necessary, update your instance first by running sudo apt update.
2. Open the /etc/chrony/chrony.conf file using a text editor (such as vim or nano). Add the following line before any other server or pool statements that are already present in the file, and save your changes: server 169.254.169.123 prefer iburst minpoll 4 maxpoll 4
3. Restart the chrony service. ubuntu:~$ sudo /etc/init.d/chrony restart Restarting chrony (via systemctl): chrony.service.
4. Verify that chrony is using the 169.254.169.123 IPv4 endpoint to synchronize the time. ubuntu:~$ chronyc sources -v | grep -F ^* In the output, the line starting with ^* indicates the preferred time source.
^* 169.254.169.123               3   6    17    12    +15us[  +57us] +/-  320us
5. Verify the time synchronization metrics that are reported by chrony. ubuntu:~$ chronyc tracking Reference ID    : 169.254.169.123 (169.254.169.123)
Stratum         : 4 Ref time (UTC)  : Wed Nov 29 07:41:57 2017

System time     : 0.000000011 seconds slow of NTP time Last offset     : +0.000041659 seconds RMS offset      : 0.000041659 seconds Frequency       : 10.141 ppm slow Residual freq   : +7.557 ppm Skew            : 2.329 ppm Root delay      : 0.000544 seconds Root dispersion : 0.000631 seconds Update interval : 2.0 seconds Leap status     : Normal SUSE Linux Starting with SUSE Linux Enterprise Server 15, chrony is the default implementation of NTP.
To configure chrony to connect to IPv4 endpoint on SUSE Linux
1. Open the /etc/chrony.conf file using a text editor (such as vim or nano).
2. Verify that the file contains the following line: server 169.254.169.123 prefer iburst minpoll 4 maxpoll 4 If this line is not present, add it.
3. Comment out any other server or pool lines.
4. Open YaST and enable the chrony service.
### Windows Starting with the August 2018 release, Windows AMIs use the Amazon Time Sync Service by default. No further configuration is required for instances launched from these AMIs and you can skip the following procedures.
If you're using an AMI that doesn't have the Amazon Time Sync Service configured by default, first verify your current NTP configuration. If your instance is already using the IPv4 endpoint of the Amazon Time Sync Service, no further configuration is required. If your instance is not using the Amazon Time Sync Service, then complete the procedure to change the NTP server to use the Amazon Time Sync Service.

To verify the NTP configuration
1. From your instance, open a Command Prompt window.
2. Get the current NTP configuration by typing the following command: w32tm /query /configuration This command returns the current configuration settings for the Windows instance and will show if you're connected to the Amazon Time Sync Service.
3. (Optional) Get the status of the current configuration by typing the following command: w32tm /query /status This command returns information such as the last time the instance synced with the NTP server and the poll interval.
To change the NTP server to use the Amazon Time Sync Service
1. From the Command Prompt window, run the following command: w32tm /config /manualpeerlist:169.254.169.123 /syncfromflags:manual /update
2. Verify your new settings by using the following command: w32tm /query /configuration In the output that's returned, verify that NtpServer displays the 169.254.169.123 IPv4 endpoint.
Default NTP settings for Amazon Windows AMIs Amazon Machine Images (AMIs) generally adhere to the out-of-the-box defaults except in cases where changes are required to function on EC2 infrastructure. The following settings have been determined to work well in a virtual environment, as well as to keep any clock drift to within one second of accuracy:

- Update Interval – Governs how frequently the time service will adjust system time towards accuracy. AWS configures the update interval to occur once every two minutes.
- NTP Server – Starting with the August 2018 release, AMIs use the Amazon Time Sync Service by default. This time service is accessible from any AWS Region at the 169.254.169.123 IPv4 endpoint. Additionally, the 0x9 flag indicates that the time service is acting as a client, and to use SpecialPollInterval to determine how frequently to check in with the configured time server.
- Type – "NTP" means that the service acts as a standalone NTP client instead of acting as part of a domain.
- Enabled and InputProvider – The time service is enabled and provides time to the operating system.
- Special Poll Interval – Checks against the configured NTP Server every 900 seconds (15 minutes).
Registry path Key name Data HKLM:\System\Curre ntControlSet\services\w32ti me\Config UpdateInterval 120 HKLM:\System\Curre ntControlSet\services\w32ti me\Parameters NtpServer 169.254.169.123,0x9 HKLM:\System\Curre ntControlSet\services\w32ti me\Parameters Type NTP HKLM:\System\Curre ntControlSet\services\w32ti me\TimeProviders\NtpClient Enabled 1 HKLM:\System\Curre ntControlSet\services\w32ti me\TimeProviders\NtpClient InputProvider 1

Registry path Key name Data HKLM:\System\Curre ntControlSet\services\w32ti me\TimeProviders\NtpClient SpecialPollInterval 900
### Connect to the IPv6 endpoint of the Amazon Time Sync Service This section explains how the steps described in Connect to the IPv4 endpoint of the Amazon Time Sync Service differ if you are configuring your instance to use the local Amazon Time Sync Service through the IPv6 endpoint. It doesn't explain the entire Amazon Time Sync Service configuration process.
The IPv6 endpoint is only accessible on Nitro-based instances.
We don't recommend using both the IPv4 and IPv6 endpoint entries together. The IPv4 and IPv6 NTP packets come from the same local server for your instance. Configuring both IPv4 and IPv6 endpoints is unnecessary and will not improve the accuracy of the time on your instance.
### Linux Depending on the Linux distribution you're using, when you reach the step to edit the chrony.conf file, you'll be using the IPv6 endpoint of the Amazon Time Sync Service (fd00:ec2::123) rather than the IPv4 endpoint (169.254.169.123): server fd00:ec2::123 prefer iburst minpoll 4 maxpoll 4 Save the file and verify that chrony is using the fd00:ec2::123 IPv6 endpoint to synchronize time:
[ec2-user ~]$ chronyc sources -v In the output, if you see the fd00:ec2::123 IPv6 endpoint, the configuration is complete.
### Windows When you reach the step to change the NTP server to use the Amazon Time Sync Service, you'll be using the IPv6 endpoint of the Amazon Time Sync Service (fd00:ec2::123) rather than the IPv4 endpoint (169.254.169.123):

w32tm /config /manualpeerlist:fd00:ec2::123 /syncfromflags:manual /update Verify that your new settings are using the fd00:ec2::123 IPv6 endpoint to synchronize time: w32tm /query /configuration In the output, verify that NtpServer displays the fd00:ec2::123 IPv6 endpoint.
### Connect to the PTP hardware clock The PTP hardware clock is part of the AWS Nitro System, so it is directly accessible on supported bare metal and virtualized EC2 instances without using any customer resources.
The NTP endpoints for the PTP hardware clock are the same as those for the regular Amazon Time Sync Service. If your instance has a PTP hardware clock and you configured the NTP connection (to either the IPv4 or IPv6 endpoint), your instance time is automatically sourced from the PTP hardware clock over NTP.
For Linux instances, you can configure a direct PTP connection, which will give you more accurate time than the NTP connection. Windows instances only support an NTP connection to the PTP hardware clock.
#### Requirements The PTP hardware clock is available on an instance when the following requirements are met:
- Supported AWS Regions: US East (N. Virginia), US East (Ohio), Asia Pacific (Malaysia), Asia Pacific (Thailand), Asia Pacific (Tokyo), and Europe (Stockholm)
- Supported Local Zones: US East (New York City)
- Supported instance families:
- General purpose: M7a, M7g, M7i
- Memory optimized: R7a, R7g, R7i
- Storage optimized: I8g, I8ge
- (Linux only) ENA driver version 2.10.0 or later installed on a supported operating system. For more information about supported operating systems, see the driver prerequisites on GitHub.

#### (Linux only) Configure a direct PTP connection to the PTP hardware clock This section describes how to configure your Linux instance to use the local Amazon Time Sync Service through the PTP hardware clock using a direct PTP connection. It requires adding a server entry for the PTP hardware clock in the chrony configuration file.
To configure a direct PTP connection to the PTP hardware clock (Linux instances only)
1. Install prerequisites Connect to your Linux instance and do the following: a.
Install the Linux kernel driver for Elastic Network Adapter (ENA) version 2.10.0 or later. b.
Enable the PTP hardware clock.
For the installation instructions, see Linux kernel driver for Elastic Network Adapter (ENA) family on GitHub.
2. Verify ENA PTP device Verify that the ENA PTP hardware clock device shows up on your instance.
[ec2-user ~]$ for file in /sys/class/ptp/*; do echo -n "$file: "; cat "$file/ clock_name"; done Expected output /sys/class/ptp/ptp<index>: ena-ptp-<PCI slot>
Where:
- index is the kernel-registered PTP hardware clock index.
- PCI slot is the ENA ethernet controller PCI slot. This is the same slot as shown in lspci | grep ENA.
Example output /sys/class/ptp/ptp0: ena-ptp-05

If ena-ptp-<PCI slot> is not in the output, the ENA driver was not correctly installed.
Review step 1 in this procedure for installing the driver.
3. Configure PTP symlink PTP devices are typically named /dev/ptp0, /dev/ptp1, and so on, with their index depending on the hardware initialization order. Creating a symlink ensures that applications like chrony consistently reference the correct device, regardless of index changes.
The latest Amazon Linux 2023 AMIs include a udev rule that creates the /dev/ptp_ena symlink, pointing to the correct /dev/ptp entry associated with the ENA host.
First check if the symlink is present by running the following command.
[ec2-user ~]$ ls -l /dev/ptp* Example output crw------- 1 root root 245, 0 Jan 31 2025 /dev/ptp0 lrwxrwxrwx 1 root root      4 Jan 31 2025 /dev/ptp_ena -> ptp0 Where:
- /dev/ptp<index> is the path to the PTP device.
- /dev/ptp_ena is the constant symlink, which points to the same PTP device.

If the /dev/ptp_ena symlink is present, skip to Step 4 in this procedure. If it's missing, do the following: a.
Add the following udev rule.
[ec2-user ~]$ echo "SUBSYSTEM==\"ptp\", ATTR{clock_name}==\"ena-ptp-*\", SYMLINK += \"ptp_ena\"" | sudo tee -a /etc/udev/rules.d/53-ec2-network- interfaces.rules b.
Reload the udev rule, either by rebooting the instance, or by running the following command.

[ec2-user ~]$ sudo udevadm control --reload-rules && udevadm trigger
4. Configure chrony chrony must be configured to use the /dev/ptp_ena symlink instead of directly referencing /dev/ptp<index>. a.
Edit /etc/chrony.conf using a text editor and add the following line anywhere in the file. refclock PHC /dev/ptp_ena poll 0 delay 0.000010 prefer b.
Restart chrony.
[ec2-user ~]$ sudo systemctl restart chronyd
5. Verify chrony configuration Verify that chrony is using the PTP hardware clock to synchronize the time on this instance.
[ec2-user ~]$ chronyc sources Expected output MS Name/IP address         Stratum Poll Reach LastRx Last sample ===============================================================================
#* PHC0                          0   0    377    1   +2ns[ +1ns] +/-   5031ns In the output that's returned, * indicates the preferred time source. PHC0 corresponds to the PTP hardware clock. You might need to wait a few seconds after restarting chrony for the asterisk to appear.
## Set the time reference on your EC2 instance or any internet-connected device to use the public Amazon Time Sync Service device to use the public Amazon Time Sync Service You can set your instance, or any internet-connected device such as your local computer or an on- prem server, to use the public Amazon Time Sync Service, which is accessible over the internet at time.aws.com. You can use the public Amazon Time Sync Service as a backup for the local

Amazon Time Sync Service and to connect resources outside of AWS to the Amazon Time Sync Service.
Note For the best performance, we recommend using the local Amazon Time Sync Service on your instances, and only using the public Amazon Time Sync Service as a backup.
Use the instructions for the operating system of your instance or device.
### Linux To set your Linux instance or device to use the public Amazon Time Sync Service using chrony or ntpd
1. Edit /etc/chrony.conf (if you use chrony) or /etc/ntp.conf (if you use ntpd) using a text editor as follows: a.
To prevent your instance or device from trying to mix smeared and non-smeared servers, remove or comment out lines starting with server except any existing connection to the local Amazon Time Sync Service.
Important If you're setting your EC2 instance to connect to the public Amazon Time Sync Service, do not remove the following line which sets your instance to connect to the local Amazon Time Sync Service. The local Amazon Time Sync Service is a more direct connection and will provide better clock accuracy. The public Amazon Time Sync Service should only be used as a backup. server 169.254.169.123 prefer iburst minpoll 4 maxpoll 4 b.
Add the following line to connect to the public Amazon Time Sync Service. pool time.aws.com iburst
2. Restart the daemon using one of the following commands.

- chrony sudo service chronyd force-reload
- ntpd sudo service ntp reload
### macOS To set your macOS instance or device to use the public Amazon Time Sync Service
1. Open System Preferences.
2. Choose Date & Time, and then choose the Date & Time tab.
3. To make changes, choose the lock icon, and enter your password when prompted.
4. For Set date and time automatically, enter time.aws.com.
Windows To set your Windows instance or device to use the public Amazon Time Sync Service
1. Open the Control Panel.
2. Choose the Date and Time icon.
3. Choose the Internet Time tab. This tab is not be available if your PC is part of a domain. In this case, it will synchronize time with the domain controller. You can configure the controller to use the public Amazon Time Sync Service.
4. Choose Change settings.
5. Select the checkbox for Synchronize with an Internet time server.
6. Next to Server, enter time.aws.com.
To set your Windows Server instance or device to use the public Amazon Time Sync Service
- Follow Microsoft's instructions to update your registry.

## Compare timestamps for your Linux instances If you're using the Amazon Time Sync Service, you can compare the timestamps on your Amazon EC2 Linux instances with ClockBound to determine the true time of an event. ClockBound measures the clock accuracy of your EC2 instance, and allows you to check if a given timestamp is in the past or future with respect to your instance's current clock. This information is valuable for determining the order and consistency of events and transactions across EC2 instances, independent of each instance's geographic location.
ClockBound is an open source daemon and library. To learn more about ClockBound, including installation instructions, see ClockBound on GitHub.
ClockBound is only supported for Linux instances.
If you're using the direct PTP connection to the PTP hardware clock, your time daemon, such as chrony, will underestimate the clock error bound. This is because a PTP hardware clock does not pass the correct error bound information to chrony, the way that NTP does. As a result, your clock synchronization daemon assumes the clock is accurate to UTC and thus has an error bound of 0.
To measure the full error bound, the Nitro System calculates the error bound of the PTP hardware clock, and makes it available to your EC2 instance over the ENA driver sysfs filesystem. You can read this directly as a value, in nanoseconds.
To retrieve the PTP hardware clock error bound
1. First get the correct location of the PTP hardware clock device by using one of the following commands. The path in the command is different depending on the AMI used to launch the instance.
- For Amazon Linux 2: cat /sys/class/net/eth0/device/uevent | grep PCI_SLOT_NAME
- For Amazon Linux 2023: cat /sys/class/net/ens5/device/uevent | grep PCI_SLOT_NAME The output is the PCI slot name, which is the location of the PTP hardware clock device. In this example, the location is 0000:00:03.0.

PCI_SLOT_NAME=0000:00:03.0
2. To retrieve the PTP hardware clock error bound, run the following command. Include the PCI slot name from the previous step. cat /sys/bus/pci/devices/0000:00:03.0/phc_error_bound The output is the clock error bound of the PTP hardware clock, in nanoseconds.
To calculate the correct clock error bound at a specific point in time when using the direct PTP connection to the PTP hardware clock, you must add the clock error bound from chrony or ClockBound at the time that chrony polls the PTP hardware clock. For more information about measuring and monitoring clock accuracy, see Manage Amazon EC2 instance clock accuracy using Amazon Time Sync Service and Amazon CloudWatch – Part 1.
## Change the time zone of your instance Amazon EC2 instances are set to the UTC (Coordinated Universal Time) time zone by default. You can change the time on an instance to the local time zone or to another time zone in your network.
Use the instructions for your instance's operating system.
Linux Important This information applies to Amazon Linux. For information about other distributions, see their specific documentation.
To change the time zone on Amazon Linux
1. View the system's current time zone setting.
[ec2-user ~]$ timedatectl
2. List the available time zones.

[ec2-user ~]$ timedatectl list-timezones
3. Set the chosen time zone.
[ec2-user ~]$ sudo timedatectl set-timezone America/Vancouver
4. (Optional) Confirm that the current time zone is updated to the new time zone by running the timedatectl command again.
[ec2-user ~]$ timedatectl Windows To change the time zone on a Windows instance
1. From your instance, open a Command Prompt window.
2. Identify the time zone to use on the instance. To get a list of time zones, use the following command: tzutil /l This command returns a list of all available time zones in the following format: display name time zone ID
3. Locate the time zone ID to assign to the instance.
4. Example: Assign the UTC time zone: tzutil /s "UTC"
Example: Assign Pacific Standard Time: tzutil /s "Pacific Standard Time"

When you change the time zone on a Windows instance, you must ensure that the time zone persists through system restarts. Otherwise, when the instance restarts, it reverts back to using UTC time. You can persist your time zone setting by adding a RealTimeIsUniversal registry key. This key is set by default on all current generation instances. To verify whether the RealTimeIsUniversal registry key is set, see step 3 in the following procedure. If the key is not set, follow these steps from the beginning.
To set the RealTimeIsUniversal registry key
1. From the instance, open a Command Prompt window.
2. Use the following command to add the registry key: reg add "HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\TimeZoneInformation" / v RealTimeIsUniversal /d 1 /t REG_DWORD /f
3. (Optional) Verify that the instance saved the key successfully using the following command: reg query "HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control \TimeZoneInformation" /s This command returns the subkeys for the TimeZoneInformation registry key. You should see the RealTimeIsUniversal key at the bottom of the list, similar to the following:
HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\TimeZoneInformation Bias                            REG_DWORD     0x1e0 DaylightBias                    REG_DWORD     0xffffffc4 DaylightName                    REG_SZ        @tzres.dll,-211 DaylightStart                   REG_BINARY    00000300020002000000000000000000 StandardBias                    REG_DWORD     0x0 StandardName                    REG_SZ        @tzres.dll,-212 StandardStart                   REG_BINARY    00000B00010002000000000000000000 TimeZoneKeyName                 REG_SZ        Pacific Standard Time DynamicDaylightTimeDisabled     REG_DWORD     0x0 ActiveTimeBias                  REG_DWORD     0x1a4 RealTimeIsUniversal             REG_DWORD     0x1
