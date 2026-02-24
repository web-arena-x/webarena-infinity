# Creating attachment deletion schedules

Source: https://support.zendesk.com/hc/en-us/articles/9783945525658-Creating-attachment-deletion-schedules

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Verified AI summary ◀▼

Creating attachment deletion schedules helps you manage data privacy by removing sensitive attachments like PII from archived tickets, while keeping important ticket information intact. You can set conditions to delete attachments based on criteria like ticket age, group, or tags. Remember, once deleted, attachments can't be restored. Track changes via the audit log and manage schedules to suit your data management needs.

Attachments often contain personally identifiable information (PII), such as drivers'
licenses, passports, medical certificates, and tax documents. These documents, typically
used for verification or processing refunds, should be removed once their purpose has
been fulfilled to maintain data privacy and compliance. Attachments can also contribute
to increased [storage usage](https://support.zendesk.com/hc/en-us/articles/4408835043994), resulting in additional costs.

Instead of deleting entire tickets to save space and remove PII, admins and [agents in custom roles](https://support.zendesk.com/hc/en-us/articles/4408882153882) with permission can create deletion
schedules to delete attachments while keeping relevant ticket information intact.

Important: Deleted attachments can't be restored. Exercise
caution when activating deletion schedules.

This article covers the following topics:

- [About attachment deletion schedules](#topic_z1v_vz5_qzb)
- [Creating attachment deletion schedules](#topic_jtq_g1v_qzb)
- [Building condition statements for attachment deletion schedules](#topic_sxn_sfy_m1c)

Related articles:

- [Managing deletion schedules](https://support.zendesk.com/hc/en-us/articles/8301879320474)
- [Creating ticket deletion
  schedules](https://support.zendesk.com/hc/en-us/articles/6388012977306)

## About attachment deletion schedules

Attachment deletion schedules allow you to create [conditions](#topic_sxn_sfy_m1c) for automatically deleting attachments.
Attachment deletion schedules delete only attachments on [archived tickets](https://support.zendesk.com/hc/en-us/articles/4408887617050), which are tickets that have been
closed for more than 120 days.

For example, you can create attachment deletion schedules like these:

- Delete attachments on all tickets that were created more than one year ago.
- Delete attachments on all tickets in the HR ticket group that have been
  closed for more than six months, except tickets with the tag
  `hold`.
- Delete attachments on all tickets that have been closed for more than six
  months, except for tickets in the Legal group.

Tip: If you're using [ticket deletion schedules](https://support.zendesk.com/hc/en-us/articles/6388012977306), review your
conditions for deleting tickets before activating attachment deletion schedules.
When attachments are removed from a ticket, the ticket is considered updated.
Therefore, you may want to delete tickets by when they're *created* instead
of when they're *updated*.

Deletion schedules delete attachments that were attached to tickets using the
following channels:

- Ticket interface in the Agent Workspace
- Email
- API
- SMS
- Webform
- Submit a request/ticket form

All other attachment types, such as attachments in messaging, side conversations, and
help center articles and comments, aren't supported.

Attachment deletion schedules start to delete eligible attachments within 72 hours of
meeting the defined criteria. For example, if a schedule deletes attachments that
are three years old, it will start deleting them within 72 hours of reaching that
age. Up to 24,000 attachments per account per day will be deleted.

After they're activated, deletion schedules aren't a one-off event. Zendesk
continuously searches for and deletes attachments that meet the conditions unless
you deactivate the schedule. There is no impact on performance when schedules delete
a large volume of attachments or run during busy periods.

You can track these changes in the [audit log](https://support.zendesk.com/hc/en-us/articles/4408828001434) by filtering by **Activity type:
Deleted**.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/deletion_schedule_attachment_log.png)

## Creating attachment deletion schedules

Admins and [agents in custom roles](https://support.zendesk.com/hc/en-us/articles/4408882153882) with permission can
create up to 10 attachment deletion schedules, but only one attachment deletion
schedule can be active at a time. If you have the [Advanced Data Privacy and Protection add-on](https://support.zendesk.com/hc/en-us/articles/6561144266906), you can
activate up to 10 attachment deletion schedules.

Tip: To give feedback on more conditions to add,
complete this short [Google form](https://docs.google.com/forms/d/e/1FAIpQLSdjZXhMzcZ3IGl7-6GubfPKOGfHCkyGjJdKevLMPGfvQap7Ag/viewform).

**To create an attachment deletion schedule**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png)
   **Account** in the sidebar, then select **Security > Deletion schedules**.
2. Click **Create deletion schedule** > **Attachments**.

   If you already
   have 10 attachment deletion schedules created, a message appears notifying
   you that you’ve reached your limit. You must delete a schedule before you
   can create a new one.
3. Enter the **Schedule name**.

   Use a consistent naming convention to help you
   recognize similar types of deletion schedules.
4. (Optional) Enter a **Description** for your deletion schedule.
5. For **Category**, indicate when to delete attachments based on when the
   ticket was **Created** or **Last updated**. This field is required.
6. Click **Add condition** to add an additional *All* condition for
   deleting attachments, such as by organization or brand. See [Building condition statements for attachment deletion schedules](#topic_sxn_sfy_m1c).

   If you have the [Advanced Data Privacy and Protection
   add-on](https://support.zendesk.com/hc/en-us/articles/6561144266906), you can add up to 100 additional deletion criteria that
   meet *All* or *Any* conditions.
7. Select a **Category**, **Operator**, and **Value** for each
   condition.

   The operator determines the relationship between the category
   and the value. For example, if you select the operator *Is*, your
   category must equal the value.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/deletion_schedule_attachment.png)
8. (Optional) After conditions are added, click **Preview** to preview an
   approximate number of tickets with attachments to be deleted. (This number is
   not a count of the attachments to be deleted.)
9. Click **Create**.

   Your new deletion schedule is added to the end of the
   list as an inactive schedule.
10. [Activate](https://support.zendesk.com/hc/en-us/articles/8301879320474#topic_nlj_q4y_fdc) the deletion schedule.

## Building condition statements for attachment deletion schedules

Condition statements consist of categories, field operators, and condition values
(which vary depending on the category selected). Condition statements are
essentially "if" statements that delete attachments meeting the specified
criteria.

The table below lists the categories available for building condition statements for
attachment deletion schedules. Conditions specific to attachments, such as file
size, are not available.

Table 1. Attachment deletion schedule categories

| Category | Description |
| --- | --- |
| Created at | Deletes attachments based on when the ticket was created. |
| Last updated | Deletes attachments based on when the ticket was last updated. For example, if Last updated is set to 365 days, and the ticket was modified within that time, the attachment is not deleted. The clock starts over, and the attachment will be deleted 365 days from the modification date. |
| Custom fields | Deletes attachments based on custom field values. |
| Brand | Deletes attachments by brand. |
| Ticket form | Deletes attachments by ticket form, if you use multiple [ticket forms](https://support.zendesk.com/hc/en-us/articles/4408846520858). |
| Group | Deletes attachments by [group](https://support.zendesk.com/hc/en-us/articles/4408894175130). |
| Support type | Deletes attachments based on the support type: Agent or AI agent. |
| Type | Deletes attachments based on the ticket type: Question, Incident, Problem, or Task. |
| Requester | Deletes attachments based on the requester name. |
| Organization | Deletes attachments based on organization, if you have multiple [organizations](https://support.zendesk.com/hc/en-us/articles/4408886146842). |
| Tags | Deletes attachments with the selected [ticket tags](https://support.zendesk.com/hc/en-us/articles/4408835059482). |