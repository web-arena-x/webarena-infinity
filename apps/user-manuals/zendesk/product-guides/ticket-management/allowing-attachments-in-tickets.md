# Allowing attachments in tickets

Source: https://support.zendesk.com/hc/en-us/articles/4408832757146-Allowing-attachments-in-tickets

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Verified AI summary ◀▼

Enable attachments in tickets to allow agents and end users to share files through various channels, including email and web forms. Configure settings for privacy, file types, and size limits. Use private attachments for sensitive documents, set expiration periods for public access, and ensure security by scanning for malware. Customize permissions for agents and end users to enhance ticket interactions.

Location: Admin Center > Objects and rules > Tickets >
Settings

Agents and end users can send each other attachments through tickets. Zendesk Support accepts attachments from users sent in [via the API,](https://developer.zendesk.com/rest_api/docs/support/attachments) email, web form, Web Widget, and Web Widget (Classic) channels in your help center.

Administrators can configure how attachments are handled in a number of ways, including setting privacy rules, end user permissions, and attachment methods.

This article includes the following topics:

- [About email attachments](#topic_hcs_zmx_xdb)
- [Allowing agents to attach files in emails](#topic_yfj_1nx_xdb)
- [Allowing end users to attach files to tickets](#topic_c2w_1nx_xdb)
- [Allowing private attachments](#topic_nrp_bnx_xdb)
- [Setting an expiration period for public attachments](#topic_x3c_ffc_jgc)
- [Setting allowed file types for attachments](#topic_r1p_2k5_pfc)
- [Attachment size limitations](#topic_lv2_cnx_xdb)

## About email attachments

Agents and end users can add attachments when creating or updating a ticket, or replying to an email notification. The attachments become *linked attachments*, which are links to external files that can be used to download the attachments, if and when they’re needed. This is the default behavior for attachments sent by email and this is what happens when email attachments are not allowed.

If *email attachments* are allowed, the behavior is different.
Agents and end users can send email attachments instead of linked attachments. Email notifications caused by creating or updating a ticket, or replying to an email, include actual attachments, instead of links to attachments. Email attachments appear as images and are a preview of the first page of the file.

There are two types of email attachments:

- **Inline attachment**: You can drag and drop files into the body of an email or comment. The image of the file appears wherever you dropped the file.
- **Appended attachment:** Attachments that appear at the bottom of a comment and that send as part of the comment's email notification.

Note: If you've set up business rules to send automated replies to end users (with placeholders such as `ticket.verbatim_description`), any attachments originally sent by the end user will not be included in the automated email notification.

All files attached via email are scanned for malware before being sent in an email notification. If an attachment is found to include a virus, several actions are taken. The attachment:

- Isn't included in the email notification. Instead, the recipient is notified that an attachment wasn't sent.
- Won't be visible within the ticket to end users.
- Will be visible within the ticket to agents but labeled with a malware warning and unavailable for download.
- Will be visible within the ticket to admins but labeled with a malware warning. Admins can download potentially malicious attachments and choose to override the restricted access for agents.

The sender does not receive a notification when an attachment is not sent.

When email attachment file size limitations are exceeded, links to attachments appear in email notifications instead (see [Attachment size limitations](#topic_lv2_cnx_xdb)).

Note: Some attachments may initiate Zendesk firewall rules. For example, if your attachment contains code, the firewall rule may be initiated. Zendesk recommends you zip or encrypt the file to bypass this rule.

Here are examples of what attachments look like to agents and end users.

| Situation | Example |
| --- | --- |
| Linked email attachment in an email notification in Gmail account | |
| Email attachment in an email notification in Gmail account | |
| Attachment in the ticket interface in Support | |
| Malicious attachment in the ticket interface in Support (visible only to team members) | |

## Allowing agents to attach files in emails

The default attachment configuration allows your agents to add files to ticket comments and email notifications as links. You can allow agents to attach files directly to the comment. This type of attachment is stored in Zendesk Support and is accessible from the ticket interface. You can attach any file type you want.

Note: The types of [comment placeholders](https://support.zendesk.com/hc/en-us/articles/4408886858138) you use in ticket triggers can also affect whether email attachments appear as links. Use rich text comment placeholders to allow attachments when **Allow agents to attach files in emails** is turned on.

You can also allow end users to add attachments to tickets (see [Allowing end users to attach files to tickets](#topic_c2w_1nx_xdb)).

**To allow email attachments**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Tickets > Settings**.
2. Click **Downloads and attachments** to expand it.
3. Select **Allow agents to attach files in emails**.

   Note: This setting doesn't appear and can't be turned on if secure downloads are allowed.
4. At the bottom of the page, click **Save**.

Once turned on, when an agent attaches a file to a comment, it is included as an attachment rather than a link. Only files attached to the current ticket comment are included in the email notification.
Files attached to earlier ticket comments are not attached to later email notifications.

For information about how to send an attachment as an agent, see [Adding attachments to ticket comments](https://support.zendesk.com/hc/en-us/articles/4408835822618).

## Allowing end users to attach files to tickets

You can allow end users to send attachments when filing a ticket or responding to an email notification. In addition, you can set end-user attachments as private, requiring agent authentication for files uploaded by end users.

The permissions granted to agents, described in [Allowing agents to attach files in emails](#topic_yfj_1nx_xdb), apply to end users when this setting is configured. Additionally, inline attachments are available only for signed-in end users.

**To allow attachments from end users** 

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Tickets > Settings**.
2. Click **Downloads and attachments** to expand it.
3. Select **Allow end users to attach files**.
4. Select **Private end user attachments** to require agent authentication when accessing customer-provided files, preventing unauthorized access.

   If **Allow secure downloads** is turned off, agent-uploaded attachments remain accessible to end users without requiring a sign-in or a Zendesk account.

   This setting doesn't apply to the messaging channel. See [private attachments in messaging](https://support.zendesk.com/hc/en-us/articles/8435939957914).
5. Click **Save**.

## Allowing private attachments

Attachments usually aren't indexed by search engines or included in threat intelligence platforms (TIPs) unless their URLs are publicly shared, like in a help center article or within email notifications to users. Regular attachments to tickets are secured using a URL with an attachment token that is considerably complex and random, but are visible to anyone with the URL and token. When relying on this type of security, if an email notification is misdirected to someone other than the intended end user, sensitive information may be accidentally exposed.

If sensitive documents are attached to your tickets, especially identification documents such as passports and driver's licenses, you can allow private attachments. When turned on, agents must be signed in to view attachments.

End users can see private attachments in their tickets in help center because they have to sign in to view their tickets. However, the attachments will appear as links in email tickets. They'll need to click the links and sign in to the help center to view the attachments.

Note the following about allowing private attachments:

- Private attachments can only be used if Guide is activated. If Guide isn't activated, private attachments prevent end users from downloading attachments since they can't be authenticated.
- If you allow private attachments, it will disable inline images for users who aren't signed in, and it will also prevent agents and admins from being able to add inline images in Support. Inline images are disabled only for Zendesk hosted images and not images that are publicly accessible.
- When an attachment is associated with a ticket, visibility is restricted to users with access to the ticket.
- In the Zendesk Agent Workspace, this setting also applies to attachments sent as part of a live chat, but it does not apply to web, mobile, or social messaging attachments (see [Securing chat attachments in the Zendesk Agent Workspace](https://support.zendesk.com/hc/en-us/articles/4408842669594)).
- To allow private attachments for messaging, see [About private attachments in messaging](https://support.zendesk.com/hc/en-us/articles/8435939957914).

Note: Access controls should be implemented to ensure only authorized personnel can view sensitive attachments, and staff should be educated on the importance of data security and the proper handling of attachments. See [General security best practices](https://support.zendesk.com/hc/en-us/articles/4408888782618) for more information about keeping your Zendesk account secure.

**To allow private attachments**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Tickets > Settings**.
2. Click **Downloads and attachments** to expand it.
3. Select **Allow secure downloads**.

   Note: **Allow agents to attach files in emails** doesn't appear and can't be turned on if secure downloads are allowed.
   Additionally, when you turn on secure downloads, agents can't copy and paste images from their computer into ticket comments.
4. Click **Save**.

## Setting an expiration period for public attachments

Admins can turn on an expiration period for public attachments.
Attachment expiration allows attachments to remain publicly accessible for a designated period, after which they become private and require user authentication to access.

Attachment expiration for public attachments provides an alternative to [private attachments](#topic_nrp_bnx_xdb), which require end users to authenticate before accessing attachments. This feature is particularly beneficial for organizations with large end-user bases that prefer not having authentication barriers for attachment access.

By default, attachments remain publicly accessible for 24 hours. When the expiration period lapses, attachments function as private, requiring user authentication for access.

This feature doesn't apply to images attached to macros or embedded within macro comments.

**To turn on an expiration period for public attachments**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Tickets > Settings**.
2. Click **Downloads and attachments** to expand it.
3. Select **Attachment expiration**.

   Note: **Attachment expiration** is hidden if **Allow secure downloads** is turned on.
4. In the Hours field, enter the number of hours to keep attachments public. After this time period, the attachment can only be accessed through a secure link that requires sign-in.
5. Click **Save**.

## Setting allowed file types for attachments

By default, when ticket attachments are turned on, attachments are restricted to a recommended list of commonly used file extensions that are generally considered safe. This helps protect your account from potentially harmful files such as .exe attachments, which are often exploited in security attacks.

Note: If your account was created before August 13, 2025, all attachment file extension types are allowed by default.

The list of recommended file types includes the following file formats:

`har, json, 3g2, 3gp, 7z, aac, amr, avi, bmp, csv, doc, docx, eml, gif, heic, heif, ics, jfif, jpeg, jpg, key, log, m4a, m4v, mov, mp3, mp4, mp4a, mpeg, mpg, mpga, neon, numbers, odt, oga, ogg, ogv, opus, pages, pdf, png, pps, ppsx, ppt, pptx, qt, svg, tif, tiff, txt, vcf, wav, webm, webp, wmv, xls, xlsx, xml, yaml, yml, zip`

You can change this setting to allow all file types or create a custom list of allowed file types. When you change the setting, existing tickets and attachments are not affected retroactively.

File type restrictions apply to files attached to new tickets created through these channels:

- Email
- Help center *Submit a request* form
- Zendesk Support mobile app
- Web Widget (Classic)

When attachment file types are restricted, agents receive an error message if they attempt to attach a file with a disallowed extension, a mismatched file type and extension, or a missing file extension.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/file_type_disallowed.png)

End users don't see an error if they attach a disallowed file. Instead, a ticket is created without the attachment. Agents see a warning in the ticket conversation and [ticket events](https://support.zendesk.com/hc/en-us/articles/4408829602970) that explains why the attachment wasn't included. This is true even if the disallowed file was the only content in the ticket.

**Zendesk Support mobile app limitations**

The Zendesk Support mobile app doesn't recognize allowed file type settings. The app always accepts the following file types:

`bmp, csv, dib, doc, docx, gif, heic, heif, hif, icns, ico, jpe, jpeg, jpg, key, numbers, odt, pages, pdf, png, pps, ppsx, ppt, pptx, svg, svgz, text, tif, tiff, txt, webp, xls, xls`

**To set allowed file types for attachments**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Tickets > Settings**.
2. Click **Downloads and attachments** to expand it.
3. Select an option for **Allowed file types**:
   - **All file types**: No restrictions.
   - **Only recommended file types**: Restrict file attachments to a suggested list of commonly used file types that are generally considered safe. Zendesk recommends this option.
   - **Only use these file types**: Create a custom list of allowed file types.
4. If you selected **Only use these file types**, list the allowed file extensions, separated by commas, without periods. Example: pdf, jpg, png
5. If you selected **All file types** or **Only use these file types**, you must select the **I agree to the potential security risk involved by allowing all/only these file types and extensions** checkbox to continue.
6. Click **Save**.

## Attachment size limitations

Email and web form attachment limits are as follows:

- The inbound email and web form attachment limit for a single file is 50 MB. If a file attachment exceeds 50 MB, the ticket is created without the attachment.
- The outbound email attachment limit for a single file is 7 MB. When this limit is exceeded, Support will process the attachment as a linked attachment instead.
- The total of all outbound email attachments cannot exceed 10 MB. When these limits are exceeded, Support will process the attachment as a linked attachment instead.
- The outbound email attachment limit for a single *linked* file is 50 MB. Up to 500 files can be attached.

 If you try to attach a file larger than 50 MB, an error message will display and inform you that the file is too large. The attachment will not be attached to the ticket (as either an email or linked attachment).
- When you upload GIF files with a large number of frames, the upload might fail with a timeout error. If this occurs, try recreating the GIF file with fewer frames.

For more information about attachment types, see [About email attachments](#topic_hcs_zmx_xdb).

Attachments from earlier comments are included in email notifications as linked attachments. If you add multiple attachments to a reply, the attachments are prioritized based on the attachment type and size. Inline attachments take precedence over appended attachments when calculating size limits. Note that when inline attachments are sent as links, they still appear as images in the body of the email notification.

The scenarios below describe how this works.

**Scenario 1**

Two files are attached in the following order:

- Email attachment A (3 MB)
- Email attachment B (6 MB)

Behavior:

- Files A and B are included as email attachments.

**Scenario 2**

Three files are attached in the following order:

- Inline attachment A (5 MB)
- Email attachment B (5 MB)
- Email attachment C (4 MB)

Behavior:

- Inline attachment A is sent as an email attachment.
- Attachments B and C are included as file links, as they push the total email attachment file size over 10 MB.

**Scenario 3**

Three files are attached in the following order:

- Inline attachment A (5 MB)
- Inline attachment B (6 MB)
- Inline attachment C (4 MB)

Behavior:

- Attachment A is included as an email attachment.
- Attachment B is included as a file link, as it pushes the total email attachment file size over 10 MB.
- Attachment C is included as a real attachment, as it brings the total email attachment file size to 9 MB.