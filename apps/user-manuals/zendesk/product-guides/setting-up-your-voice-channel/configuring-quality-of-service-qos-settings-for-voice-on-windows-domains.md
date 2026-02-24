# Configuring quality of service (QoS) settings for voice on Windows domains

Source: https://support.zendesk.com/hc/en-us/articles/4408839174682-Configuring-quality-of-service-QoS-settings-for-voice-on-Windows-domains

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Talk Team, Professional, or Enterprise |

You can use DSCP tags in Microsoft Windows domains to let your network appliances know how to prioritize traffic. For example, it’s common that RTP traffic (audio) in a VoIP call gets a DSCP tag of 46. This allows you to set up custom traffic shaping rules that prioritize your voice traffic and increase your overall call quality.

Windows overwrites DSCP values that are set by applications and sets them to 0; basically, it doesn't trust software to set these values. Because of this there are some settings that you'll need to modify so that your traffic gets tagged appropriately.

For more information, see [Microsoft’s Quality of Service (QoS) Policy](https://docs.microsoft.com/en-us/windows-server/networking/technologies/qos/qos-policy-top)

Generally only customers that have a large number of voice agents on the same network should consider configuring this.

This article contains the following sections:

- [Setting Up Group Policy rules](#set-up-group-policy-rules)
- [About network switches](#h_01EXQJPR6RCDASVD0PZ8B6VG21)

## Setting Up Group Policy rules

You control the QoS settings that are used for certain applications by creating Group Policy rules.

**To create a Group Policy rule**

1. In Windows, open a command prompt and type “**gpedit.msc**” to open the local Group Policy editor.
2. In the Group Policy editor, under **Computer Configuration**, right-click **Policy-based QoS settings** and select **Create New Policy**. You'll then follow a wizard to configure the QoS rules to use.
3. On the first page, enter “**Zendesk Talk Policy**” for the policy name and specify a DSCP value of “**46**“, then click **Next**.  
   ![](https://support.zendesk.com/hc/article_attachments/4408850538394)
4. On the second page, specify which applications the policy applies to. Select **All applications**, then click **Next**.  
   ![](https://support.zendesk.com/hc/article_attachments/4408851609498)
5. On the third page of the Wizard, you can limit both the source and destination IP address. Select **Any source IP address** and **Any destination IP address**. When you are finished, click **Next**.  
   ![](https://support.zendesk.com/hc/article_attachments/4408850538010)
6. In the fourth and final screen, under **Select the protocol that this QoS policy applies to**, select **TCP and UDP**. Under **Specify The source port number**, select **From any source port** and under **Specify the destination port number**, select **To any destination port**. **![](https://support.zendesk.com/hc/article_attachments/4408850537626)**
7. When you are ready, click ****Finish.****
8. After you complete these changes, you'll need to restart for the settings to take effect or refresh the group policy on each client machine.

## About network switches

If you have network switches through which voice traffic flows, be sure that these are set to respect the DSCP and expedited forwarding rules. Some switches will wipe DSCP traffic, negating all the work done to set it up. Setting up a packet capture would help you identify if there is a piece of network hardware wiping the DSCP from the packets.

Generally, older switches, by default, reset QoS settings if they are not enabled to trust what they receive. However, this is also only if QoS is enabled by default and on such switches it generally isn't. On older switches, the default generally is that QoS isn't enabled meaning markings will not be changed. If the switch's QoS is enabled, the default then usually means QoS markings are reset to zero.

Recent switches behave much like routers that, by default, don't reset QoS markings unless configured to do so meaning they implicitly trust a frame or packet's QoS markings. However, by default, the device might not offer any special treatment for specific QoS markings unless configured to do so. Be sure to configure it to do so!