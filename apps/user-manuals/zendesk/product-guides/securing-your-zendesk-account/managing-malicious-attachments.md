# Managing malicious attachments

Source: https://support.zendesk.com/hc/en-us/articles/4483794022170-Managing-malicious-attachments

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Verified AI summary ◀▼

Malware scanning protects your team by blocking potentially harmful attachments in tickets. If an attachment is flagged, agents can't access it, but admins or authorized agents can review and decide on access. This feature covers attachments from email, help center forms, and APIs, but not messaging or social channels. Always consult your company's security policy before handling flagged files.

Malware scanning is a security feature that scans all file attachments to tickets and
blocks any that are flagged as potentially malicious. When an attachment is flagged as
malware, agents are prevented from downloading the file unless an admin or [agent in a custom role with permissions](https://support.zendesk.com/hc/en-us/articles/4408882153882) overrides the
malware identification.

This article includes the following topics:

- [About malware
  scanning](#topic_jyj_r25_xsb__ul_h5j_mf5_xsb)
- [Reviewing potential malware
  attachments](#topic_ojg_dg5_xsb)

## About malware scanning

Zendesk scans attachments to tickets in Support and Zendesk Suite after they are
uploaded. When malware is suspected, agents can't access the attachment, and end
users won't see the attachment. Attachments are also scanned in the Zendesk Support
mobile app on both iOS and Android in the [new agent experience](https://support.zendesk.com/hc/en-us/articles/4408846407066#topic_lmz_hkb_1vb).

Attachments to tickets received from the following channels are scanned:

- Email
- Help center *Submit a request* form
- [Attachments API](https://developer.zendesk.com/api-reference/ticketing/tickets/ticket-attachments/)
- Support Mobile SDK ticket form
- Classic Web Widget ticket form

Malware scanning is not available for messaging channels (including both Agent
Workspace and Web Widget), social messaging, or standalone Chat subscription
channels.

Whether agents see a notification about a blocked attachment and whether admins or
agents in custom roles with permissions can override the malware designation depends
on the Zendesk product, the agent interface in use, and the channel from which the
attachment originated. Specifically, warning labels are only displayed on
potentially malicious attachments if [email attachments are turned on](https://support.zendesk.com/hc/en-us/articles/4408832757146) for the account and
agents are working in Support on the desktop or mobile app.

In Support on the desktop:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/support_ticket_attachment_malware_scan.png)

In the Support mobile app:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/support_mobile_malware_ios.png)

If malware is detected in attachments to tickets created with the *Submit a
request* link in the help center, the attachments are hidden from end
users.

## Reviewing potential malware attachments

Malicious attachments to tickets and conversations in Support and Zendesk Suite are
inaccessible to agents, but admins and agents in custom roles with permissions can
download the flagged attachments and decide whether to allow agents to access them
or keep them restricted. Consult your company's security policy before downloading
or taking action on malicious attachments.

**To view a potential malware attachment**

- In a ticket, click the download icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/DownloadIcon.png)) on the potentially malicious attachment and
  then click **Proceed** in the confirmation dialog to download the
  attachment.

**To permit agents to access a flagged attachment**

- After [reviewing
  the potentially malicious attachment](#topic_ojg_dg5_xsb__ul_o3s_lbq_ysb), under the attachment in the
  ticket click **Allow access**.

**To restrict agent access to a flagged attachment**

- If you want to re-enable agent restrictions to a potentially malicious
  attachment, under the attachment in the ticket click **Restrict
  access**.