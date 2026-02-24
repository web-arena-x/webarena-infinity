# Network requirements for voice support

Source: https://support.zendesk.com/hc/en-us/articles/4408831417498-Network-requirements-for-voice-support

---

Zendesk uses the internet for making and receiving phone calls. As a result, a fast and reliable internet connection is important. For example, a wired network with Wi-Fi turned off gives better results. Regardless of your network configuration, you may have to make adjustments to it for the network to work properly for voice support.

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Talk Team, Professional, or Enterprise |

Zendesk uses the internet for making and receiving phone calls. As a result, a fast and reliable internet connection is important. For example, a wired network with Wi-Fi turned off gives better results. Regardless of your network configuration, you may have to make adjustments to it for the network to work properly for voice support.

Use the information in this article to help minimize network problems. If you can't make these changes yourself, contact your IT department for assistance.

Topics covered in this article:

- [How a network's configuration can affect voice support](#topic_tpl_j35_g1c)
- [Preparing your network for voice support](#topic_vy5_sj2_sxb)
- [Using voice with a proxy, MPLS, or VPN](#topic_wcp_yxz_c1c)
- [Using DSCP](#topic_rjq_rzz_c1c)
- [Troubleshooting](#topic_ptb_5j2_sxb)

Related article:

- [Preparing to offer voice support](https://support.zendesk.com/hc/en-us/articles/4408827987482)

## How a network's configuration can affect voice support

A network's configuration can have a significant impact on the following:

- **Latency**: The time it takes data packets to arrive at the destination.
 High latency means there are significant delays in transmitting the data over the network, which result in interruptions such as voice delivery delays that can cause overlaps in conversation. Lower latency creates a smoother call experience.
- **Jitter**: The change in latency over time. Jitter sounds similar to interference or as though someone is having problems with their microphone connection. It can also lead to one side of the conversation not being heard clearly.
- **Packet loss**: When voice signals are digitized and transmitted, they are divided into data packets. If some of the packets fail to reach their destination, the result is missing pieces of the audio signal causing audible voice distortion to the call.

To minimize network issues, ensure everything is wired. Use wired 3.5mm jack headsets for agents and a wired internet connection instead of a Wi-Fi one.

Some applications use a lot of bandwidth, especially streaming apps. Zendesk requires 500kbps per agent providing voice support. If you have 50 agents, for example, they would each need a dedicated 500kbps, meaning a minimum 25mbps line.

A best practice when troubleshooting network issues is to first close all network-intensive applications such as Netflix, Spotify, and YouTube.

## Preparing your network for voice support

Zendesk uses Twilio as its network provider. If you're applying traffic filtering, you must allow network access to the list of IP addresses, ports, domains, and URLs listed in this section.

Note: Zendesk is hosted by Amazon Web Services (AWS). Ensure you permit all of the AWS IP ranges that are specified in [Configuring your firewall for use with Zendesk](https://support.zendesk.com/hc/en-us/articles/4408842860186).

This section covers the following topics:

- [Required IP addresses, ports, and domains for voice](#topic_vy5_sj2_sxb__section_hq4_5gz_c1c)
- [Required URLs for voice](#topic_vy5_sj2_sxb__section_ybd_t4z_c1c)
- [Recommendations and incompatibilities](#topic_vy5_sj2_sxb__section_m5q_45z_c1c)

### Required IP addresses, ports, and domains for voice

There are two types of traffic that need to make outbound connections, and in response, allow return traffic:

- Media traffic — a Secure Real-time Transport Protocol (SRTP) connection used to send and receive audio
- Signaling traffic — an encrypted Transport Layer Security (TLS)
 connection used for sending and receiving control information to set up calls.

Note: Ensure that any changes you make to your configuration are applied across all network appliances. This includes firewalls, routers, switches, load-balancers, and any other hardware or software (including software-based blocking systems) that could block or interfere with network traffic.

| | | | |
| --- | --- | --- | --- |
| **Media connections** | | | |
| **Secure media (ICE/STUN/SRTP) edge locations** | **Destination IP ranges** | **Destination port ranges** | **Protocol** |
| sydney (au1) sao-paulo (br1) dublin (ie1) frankfurt (de1) tokyo (jp1) singapore (sg1) ashburn (us1) umatilla (us2) roaming (gll) | 168.86.128.0/18 | 10,000 - 60,000 | UDP |

Note: You cannot specify IP ranges for signaling connections. Instead, you must activate communication to the domains listed in the following Signaling connections table. If your internal network environment requires that you add each connecting IP to an allow list, we suggest hosting a server outside your network (such as a network DMZ) to proxy requests from Twilio into the internal network.

| | | | |
| --- | --- | --- | --- |
| **Signaling connections** | | | |
| **Description** | **Destination** | **Destination port** | **Protocol** |
| Secure TLS connection to Twilio signaling gateway | - chunderw-gll.twilio.com - chunderw-vpc-gll.twilio.com - voice-js.roaming.twilio.com | 443 | TCP |
| Secure TLS connection to Twilio regional signaling gateways | - chunderw-vpc-gll-au1.twilio.com - chunderw-vpc-gll-br1.twilio.com - chunderw-vpc-gll-de1.twilio.com - chunderw-vpc-gll-ie1.twilio.com - chunderw-vpc-gll-jp1.twilio.com - chunderw-vpc-gll-sg1.twilio.com - chunderw-vpc-gll-us1.twilio.com - chunderw-vpc-gll-us2.twilio.com - voice-js.ashburn.twilio.com - voice-js.sydney.twilio.com - voice-js.dublin.twilio.com - voice-js.sao-paulo.twilio.com - voice-js.frankfurt.twilio.com - voice-js.tokyo.twilio.com - voice-js.singapore.twilio.com - voice-js.umatilla.twilio.com - voice-js.roaming.twilio.com | 443 | TCP |
| Secure TLS insights logging gateway | - eventgw.twilio.com | 443 | TCP |
| - | - sdk.twilio.com | 443 | TCP |

### Required URLs for voice

For some features to work, you must be able to connect to URLs such as **pubsub-shardC-P-N.zendesk.com**. This is because voice connections are not made via the same URL as the connection requests to the rest of Zendesk (for example, mydomain.zendesk.com). Instead, voice connections use the following format: **pubsub-shardC-P-N.zendesk.com**. Example:
https://pubsub-shard2-17-1.zendesk.com.

- C is the cluster of the account (a value between 1 and 3)
- P is [the pod](https://support.zendesk.com/hc/en-us/articles/4408829092506) of the account
- N is a random number from 1 to 4

You can check the URL that your account uses by checking the connection request in Google Chrome.

**To identify your pubsub-shardC-P-N.zendesk.com connections**

1. Open Chrome and click the **Options** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/macros_edit_menu_icon_vertical.png)) menu.
2. Click **More tools** > **Developer tools**.
3. Go go the **Network** tab (if it's hidden, click **>>**).
4. In the **Filter** field, enter **pubsub**.
5. Refresh your browser page.
6. Click one of the displayed entries, then check the **Headers** tab.

After you've identified the cluster and pod number for the pubsub-shardC-P-N.zendesk.com connections of your account, replace the C and P with the cluster and pod number that you identified for the following URLs. You must allow these URLs (or domains) access to your VPN, firewall, and any antivirus software that you're using.

- https://pubsub-shard**C**-**P**-1.zendesk.com
- https://pubsub-shard**C**-**P**-2.zendesk.com
- https://pubsub-shard**C**-**P**-3.zendesk.com
- https://pubsub-shard**C**-**P**-4.zendesk.com

### Recommendations and incompatibilities

- Ensure both the Zendesk and Twilio IP addresses and domains are excluded from Stateful Packet Inspection (SPI), or you may experience high User Datagram Protocol (UDP) or TCP connection times.
- Twilio’s Network Traversal Service (STUN/TURN) is IPv4-only. If agents are on IPv6 addresses, ensure IPv4 reachability by asking your provider for IPv4 addresses.
- If your router includes the SIP Application Level Gateway (ALG) function or SPI, deactivate both of these functions on the networks that are using for voice.
- Do not plug in hardware that is not meant to be plugged into a smart switch. We are aware that if a switch or other network hardware is plugged into an incorrectly configured Cisco Smart Switch, it could override the allowed domains and IP addresses. Therefore check with your network team that the smart switch is configured to reflect the settings mentioned in this article.
- The Zendesk voice channel is not compatible with virtual desktop environments (VDIs) such as Microsoft Azure Virtual Desktop (formerly Windows Virtual Desktop) and Citrix Virtual Apps and Desktops.

### Using voice with a proxy, MPLS, or VPN

When you need to use a proxy, MPLS, or VPN, it's essential you configure a split tunnel. Implementing a split tunnel is necessary for directing outgoing traffic to Zendesk, Twilio, and your Zendesk subdomain locally. This means excluding Zendesk and Twilio traffic from the proxy, MPLS, or VPN, allowing it to go directly to the internet at the agent's physical location.

The requirement for this configuration is due to the presence of Global Low-Latency (GLL), a background service which is responsible for determining the most efficient network path for handling calls. When proxy, MPLS, or VPN configurations are in use, the actual locations of your agents may not be accurately represented. Consequently, this could result in suboptimal call routing, potential latency-related issues, and other concerns impacting call quality.

In scenarios where using a proxy, MPLS, or VPN is unavoidable, it's crucial to exclude traffic intended for Zendesk and Twilio domains, including your FQDN subdomain.zendesk.com, and the specified IP addresses outlined in the accompanying documentation. This exclusion is critical to ensure the proper functionality within these network configurations.

### Using DSCP

For information about the guidelines to implement DSCP, see [Configuring Quality of Service (QoS) settings for voice on Windows domains.](https://support.zendesk.com/hc/en-us/articles/4408839174682)

DSCP tags in packets are useful for informing network appliances on prioritizing traffic. By default, calls have a DSCP tag of 46. If congestion is an issue on your network, consider implementing [DSCP](http://www.erg.abdn.ac.uk/users/gorry/course/inet-pages/dscp.html) using the instructions in this article. The Twilio Client 1.3 and later enables DSCP by default in compatible browsers such as Google Chrome.

Compatible browsers tag WebRTC media packets, which permits differentiated handling on a LAN, so real-time media can be prioritized above other network traffic. The Differentiated Services (DS) field is located in the IPv4 header TOS octet or the IPv6 Traffic Class octet. A DS-compliant network node (for example, a router) includes a classifier that selects packets based on the value of the DS field, buffer management, and packet scheduling mechanisms that are capable of delivering the specific packet forwarding treatment indicated by the DS field value.

With the Twilio Client 1.3, sent RTP packets will have a DiffServ codepoint on their local [Wireshark](https://www.wireshark.org/) packet captures. When you allow DSCP, the WebRTC engine marks the RTP packets with EF (expedited forwarding) and the values related to this type of forwarding:

- binary: 101 110
- hex: 0x2e
- decimal: 46

You must use a browser that supports WebRTC (such as Chrome or Firefox). If you implement DSCP (recommended), use Chrome (the latest, non-beta version), as this is the only browser that supports it.

**To check if you're on the latest version of Chrome**

1. In Chrome, navigate to chrome://help/ in your address bar.
2. Click **Relaunch** to update Chrome.

This section covers the following topics:

- [Using DSCP functions correctly](#topic_rjq_rzz_c1c__section_mwk_nv2_d1c)
- [Checking DSCP tags for machines on a domain](#topic_rjq_rzz_c1c__section_slj_mv2_d1c)
- [Checking DSCP tags for machines that are not on a domain](#topic_rjq_rzz_c1c__section_jyy_jv2_d1c)
- [Requirements for Windows computers](#topic_rjq_rzz_c1c__section_otq_hv2_d1c)

#### Using DSCP functions correctly

In some Windows-based environments, DSCP tags are filtered out despite the network being set up for DSCP. Your network team can verify if DSCP tags are being filtered out by Windows by running a capture in [Wireshark](https://www.wireshark.org/). Either implement a group policy that enforces DSCP or, if your computers are not on a domain, implement it on a computer-by-computer basis.

#### Checking DSCP tags for machines on a domain

For machines on a domain, you control the QoS settings that are used for certain applications by designing different Group Policy rules.

You must force client machines to pick up new Group Policy rules to make the Dialer work at its best (usually a reboot is enough). To make the Dialer work optimally, use the following steps to ensure that WebRTC packets are prioritized.

**To check DSCP tags for machines on a domain**

1. In your command line, enter gpedit.msc to open the Group Policy rules.
2. In **Group Policy rules**, under **Computer Configuration**, select **Policy Based QoS Settings**.
3. Right-click, then select **Create new Policy**.

   A wizard interface opens to configure the QoS rules.
4. In **Policy name**, enter Salesloft DSCP. For the DSCP value, enter 46.
5. Click **Next**.
6. In the next dialog, select **Only applications with executable name**, then enter Chrome.exe
7. Click **Next**.
8. In the dialog, click **Next** (you do not need to enter any settings).
9. In the next dialog, select the protocol that the QoS applies to. For the Salesloft Dialer, this is limited to UDP.

#### Checking DSCP tags for machines that are not on a domain

This section modifies the registry setting so you can specify the QoS setting that'll be based on your Group Policy configuration.

**To check DSCP tags for a machine not on a domain**

1. Navigate to **HKEY\_LOCAL\_MACHINE** > **CurrentControlSet** >
   **Services** > **tcpip** > **QoS**.
2. If the QoS key does not exist, right-click **TCP/IP** and select **New Key**.
3. For the name, enter QoS.
4. Select the **QoS** key.
5. If the string does not already exist, create a new string "Do not use NLA".
6. Set the value to 1.
7. Reboot your computer and the new settings will take effect.

#### Requirements for Windows computers

You may encounter issues if your computer uses the Windows operating system.
Using the command prompt, customers must use the Quality Windows Audio Visual Experience (QWAVE) service and change the startup type to automatic (as it's set to manual by default).

Note: You must run the Command Prompt as an administrator.

**To ensure QWAVE is activated and startup is automatic**

1. Open the Windows **Start menu**.
2. In the **Search** bar, enter cmd.
3. Right-click **Command Prompt** , then click **Run as administrator**.

   ![](https://support.zendesk.com/hc/article_attachments/7856503151770)
4. Paste the following text into the command line:

   ```
   net start QWAVE
   ```
5. Press **Enter** to see the following results.

   ![](https://support.zendesk.com/hc/article_attachments/7856497648666)
6. To ensure the service startup type is permanently set to automatic, paste the following code into the command prompt.

   ```
   REG add "HKLM\SYSTEM\CurrentControlSet\services\QWAVE" /v Start /t REG_DWORD /d 2 /f
   ```
7. Press **Enter**.

The QWAVE service has set the startup type to automatic. If you encountered an error when following the above steps, ask a member of your IT team or a computer administrator to perform them.

[Create a group policy object](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-firewall/create-a-group-policy-object) on your network to set the service for all client computers to automatic. This will save you from having to set up each computer manually.

## Troubleshooting

### Call quality and connectivity problems

If you're experiencing connectivity or audio problems, it could be related to your network configuration or installed software that is designed to monitor and block IP connections. This includes, for example, firewalls, anti malware, antivirus programs, intrusion prevention systems (IPS), intrusion detection systems (IDS), web application firewalls (WAFs), web filters, and ad blockers.

The following tests will help you troubleshoot most audio and connectivity problems.

- **Disable any interfering software**: Temporarily disable any software that can monitor and block IP connections. Such software includes firewalls and antivirus software, web filters, and ad-blockers.
 This helps determine if they are what's causing connectivity issues.
 Make new test calls and reassess the situation. To keep your system secure, always remember to reactivate your security software after you've completed testing.
- **Unrestrict internet access**: Ensure your computer has unrestricted internet access for connectivity tests, then make new test calls and reassess the situation. A stable and high-quality internet connection is essential for seamless VoIP calls.
- **[Run a Twilio WebRTC Diagnostics](https://networktest.twilio.com/?usenewvoiceips=true) test:** Run a diagnostics test before, and immediately after, making any network changes. Comparing the before and after test results can give you a clearer indication of where the issue is originating from. If you're unsure of how to interpret the results, see [How do I use the Twilio network test to troubleshoot agent calls](https://support.zendesk.com/hc/en-us/articles/4408823183002). It explains the test results line by line.

By carrying out the above tests, you can identify whether the call issues are coming from specific areas, such as network configurations, or from software that is blocking the connection.

For more troubleshooting help, see [How can I troubleshoot voice issues?](https://support.zendesk.com/hc/en-us/articles/4408829651738)

### Error message: Some voice features aren't available

You may receive the following error message: "Some features aren’t available right now. You can still make and receive calls." This message means either your browser or your computer cannot connect to the required URLs. If you don’t allow communication, then you will only be able to accept or decline calls and hang up. Multiple features will not work, including the following:

- Wrap up

 Note: If Wrap up is activated, the user will be immediately dropped from the call.
- Recording
- Transfers
- Hold

**To resolve this error**

1. Contact your network administrator to activate your network to communicate with your computer or browser.
2. Follow the steps in [Troubleshooting agent collision in Play mode](https://support.zendesk.com/hc/en-us/articles/4408825035674-Troubleshooting-agent-collision-in-Play-mode#:~:text=to%20do%20this.-,Agent%20Presence%20URLs,-Connections%20to%20Zendesk).