# Adding attachments to ticket comments

Source: https://support.zendesk.com/hc/en-us/articles/4408835822618-Adding-attachments-to-ticket-comments

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Agents can add attachments to ticket comments from the agent interface and by email. End users can send emails to Support that become ticket comments and, [if enabled by an administrator](https://support.zendesk.com/hc/en-us/articles/4408832757146), attachments that they add to those messages are added to the ticket comments in Support. End users cannot remove an attachment from a ticket comment that has already been submitted, but agents with delete permission can [redact](https://support.zendesk.com/hc/en-us/articles/4408846470170) attachments.

This article includes these sections:

- [Adding attachments to ticket comments from the agent interface](#topic_el2_3n4_rpb)
- [About downloading linked attachments](#topic_dxv_lbp_rpb)
- [About adding attachments to private comments](#topic_vlb_bd4_rpb)

**Related articles:**

- [About email attachments](https://support.zendesk.com/hc/en-us/articles/4408832757146#topic_hcs_zmx_xdb)
- [Adding comments to tickets](https://support.zendesk.com/hc/en-us/articles/4408828489370)
- [Managing malicious attachments](https://support.zendesk.com/hc/en-us/articles/4483794022170)

## About adding attachments to private comments

All users (agents, admins, and end users) can create private comments. However, Support handles attachments to private comments differently depending on certain factors.

Private comments appear in the agent interface as an **Internal note**. Private comments and internal notes are the same thing. This article uses the term **private comment** to describe these types of comments because it is possible to have comments from external end user CC on the **Internal note** tab.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ticket_comment_internal_note.png)

Note the following about how attachments work with private comments:

- Agents and admins can add attachments to private comments. If the private comment includes an attachment, the email notification includes the attachment. However, whether it is a **linked attachment** or an **email attachment**, depends on your admin settings and the file size. For more information, see [About email attachments](https://support.zendesk.com/hc/en-us/articles/4408832757146#topic_hcs_zmx_xdb) and [Enabling attachments in tickets](https://support.zendesk.com/hc/en-us/articles/4408832757146).
- End users can only send (but not receive) private comments to Support by email. They can only add attachments to public or private comments if **Customer can attach files** is enabled. For more information, see [Understanding when email replies become public or private comments](https://support.zendesk.com/hc/en-us/articles/4408842992538) and [Allowing end users to attach files to tickets](https://support.zendesk.com/hc/en-us/articles/4408832757146#topic_c2w_1nx_xdb).
- Support sends email notifications about private comments to team members, but never to end users.
- There is no Help Center functionality that allows end users to view a record of private comments and attachments associated with private comments that have already been submitted. For more information, see [Viewing your assigned, requested, and CC tickets in your Support profile](https://support.zendesk.com/hc/en-us/articles/4408829574810).

## About downloading linked attachments

The files attached to ticket comments are added to email notifications. If **Enable secure downloads** is enabled, only logged-in users can view **linked attachments** that were uploaded to your Zendesk instance. Otherwise, anyone with the link to a linked attachment can view the file [as long as it isn't flagged as malware](https://support.zendesk.com/hc/en-us/articles/4483794022170). This does not affect inline links to attachments not hosted in your Zendesk instance. For more information about making attachments private, and about linked attachments vs. email attachments, see [Enabling attachments in tickets](https://support.zendesk.com/hc/en-us/articles/4408832757146).

Note: If **Enable secure downloads** is enabled, you'll no longer be able to paste inline images into the body of a ticket comment.

Attachments are not indexed by search engines unless the link to a linked attachment has been published in a help center article or something similar. This is the case whether **Enable secure downloads** is turned on or off.

## Adding attachments to ticket comments from the agent interface

This procedure explains how to add attachments to public and private comments from the agent interface. You can add attachments to **Public replies** or **Internal notes**.

**To attach a file to a comment from the agent interface**

1. In a ticket comment, click the paperclip icon.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ticket_comment_attach.png)
2. Browse to the file you want to attach.
3. Select the file, and click **Open**.

   The file is added to the comment.

   For information about how the attachment is handled by the subsequent the email notification, see the earlier sections of this article and [About email attachments](https://support.zendesk.com/hc/en-us/articles/4408832757146#topic_hcs_zmx_xdb).