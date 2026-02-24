# Turning on private attachments in messaging

Source: https://support.zendesk.com/hc/en-us/articles/8435939957914-Turning-on-private-attachments-in-messaging

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Live chat and messaging Team, Professional, or Enterprise |

Zendesk messaging attachments allow both agents and end users to send and receive various types of files within a messaging conversation. This is helpful for providing detailed support, sharing necessary documents, and improving the overall communication experience.

Messaging attachments can be either conversation-scoped or app-scoped. App-scoped attachments refer to files or documents that are linked to a specific account within a broader platform or system, such as Zendesk. These attachments are accessible by anyone that is associated with the account. These files still require authentication, ensuring that only authorized users can access them. When using the post message API to send an app-scoped attachment, all participants across any conversation within the account who have access to the URL will be able to access the attachment.

Note: The private attachments in messaging feature is on by default for accounts created on or after December 5, 2024. Make sure to turn on [secure downloads](https://support.zendesk.com/hc/en-us/articles/4408842669594-Enabling-secure-chat-attachments-in-the-Zendesk-Agent-Workspace). This setting controls whether agent-facing attachment URLs require authentication, and should be enabled to ensure attachments are always kept private.

For information about configuring private attachments, see [Configuring private attachments for messaging](https://developer.zendesk.com/documentation/zendesk-web-widget-sdks/messaging_private_attachments/).

This article includes the following sections:

- [Understanding how private attachments differ from public attachments](#topic_qjl_wvr_mdc)
- [Supported file types for messaging attachments](#topic_v1r_rwr_mdc)
- [Turning on private attachments for messaging](#topic_zhs_n5t_dfc)

## Understanding how private attachments differ from public attachments

Private and public attachments offer ways to store and distribute documents or files within systems, each providing varying degrees of accessibility. Both can be uploaded, downloaded, and managed with a user interface or an API, depending on the system's configuration.

A private attachment is an attachment that is only accessible within the specific conversation in which it was shared. To access the attachment, a client must [authenticate themselves](https://support.zendesk.com/hc/en-us/articles/4411666638746-Authenticating-end-users-for-messaging) to prove they have permission to view it.

Here are some comparisons between public and private attachments in messaging.

| | Public attachments | Private attachments |
| --- | --- | --- |
| Accessibility | Accessible to anyone who has the link or access to the channel where the attachment is shared. No specific permissions are required to view public attachments, making them suitable for information intended for general distribution. | Restricted based on user permissions or participation in a private messaging conversation between the agent and the end user. Private attachments are ideal for confidential or sensitive information that should not be accessible to everyone on the platform. |
| Use cases | Often used for less sensitive information like general announcements, public reports, marketing materials, or any content intended for wide distribution. | Commonly used for sharing confidential documents such as personal information, internal reports, strategic documents, or any other content that requires controlled access. |
| Security measures | Extensive security controls are not applied because these files are intended for public access. | Robust security measures are in place, including strict authentication protocols to guard against unauthorized access. |
| Visibility and tracking | Visibility is broad, and tracking who has accessed the document can be challenging unless specific analytic tools are employed. | Access can be closely monitored, and usage analytics are often more detailed, allowing administrators to see who has accessed the file and when (based on their IP address). |

## Supported file types for messaging attachments

Zendesk messaging supports the following file types as attachments:

3g2, 3gp, 7z, aac, amr, avi, bmp, caf, csv, doc, docx, eml, gif, heic, heif, ics, jfif, jpeg, jpg, key, log, m4a, m4v, mov, mp3, mp4, mp4a, mpeg, mpg, mpga, neon, numbers, odt, oga, ogg, ogv, opus, pages, pdf, pkpass, png, pps, ppsx, ppt, pptx, qt, svg, tif, tiff, txt, usdz, vcf, wav, webm, webp, wmv, xls, xlsx, xml, yaml, yml, zip

## Turning on private attachments for messaging

**To turn on private attachments for messaging**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Tickets > Settings**.
2. Click **Downloads and attachments** to expand it.
3. Select **Enable secure downloads in messaging**.
4. At the bottom of the page, click **Save**.