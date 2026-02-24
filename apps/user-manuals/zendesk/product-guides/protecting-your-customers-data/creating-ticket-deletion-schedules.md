# Creating ticket deletion schedules

Source: https://support.zendesk.com/hc/en-us/articles/6388012977306-Creating-ticket-deletion-schedules

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Verified AI summary ◀▼

Create ticket deletion schedules to automatically remove archived tickets after a set period, helping you comply with data retention laws and manage data storage. You can set conditions like ticket age, brand, or type. Remember, deleted tickets can't be restored, and schedules continuously delete tickets meeting the criteria. Use the audit log to track deletions.

In most cases, Zendesk automatically [archives tickets](https://support.zendesk.com/hc/en-us/articles/4408887617050) 120 days after they are closed. While
archived tickets are still accessible, it's recommended that you delete them
regularly.

Admins and [agents in custom roles](https://support.zendesk.com/hc/en-us/articles/4408882153882) with permission can
create deletion schedules to delete archived tickets after a specified period of time.
This is an automated way to help comply with data retention laws and [manage data storage](https://support.zendesk.com/hc/en-us/articles/4408835043994) in your Zendesk account. If tickets
contain sensitive information, a deletion schedule helps you create data retention
policies to comply with privacy legislation such as the EU General Data Protection
Regulation (GDPR) and the California Privacy Rights Act (CRPA).

For example, you can create ticket deletion schedules like these:

- Delete tickets that haven't been updated in three years
- Delete tickets for Brand A that haven't been updated in six months
- Delete tickets with the type Question that haven't been updated in 200 days

Important: Deleted archived tickets can't be restored.
Exercise caution when activating deletion schedules.

This article covers the following topics:

- [About ticket deletion schedules](#topic_z1v_vz5_qzb)
- [Creating ticket deletion schedules](#topic_jtq_g1v_qzb)
- [Building condition statements for ticket deletion schedules](#topic_sxn_sfy_m1c)

Related articles:

- [Managing deletion schedules](https://support.zendesk.com/hc/en-us/articles/8301879320474)
- [Creating attachment deletion
  schedules](https://support.zendesk.com/hc/en-us/articles/9783945525658)

## About ticket deletion schedules

Ticket deletion schedules allow you to create [conditions](#topic_sxn_sfy_m1c) for automatically deleting tickets. Deletion
schedules delete only [archived tickets](https://support.zendesk.com/hc/en-us/articles/4408887617050), which are tickets that have been
closed for more than 120 days.

Ticket deletion schedules continuously search for and delete tickets that have been
*closed and not modified* for a specified period. For example, if you
create a schedule that deletes tickets 365 days after they are closed, and the
ticket was modified within that time (for example, ticket content was redacted), the
ticket is not deleted. The clock starts over, and the ticket will be deleted 365
days from the modification date.

Ticket deletion schedules start to delete eligible tickets within 72 hours of meeting
the defined criteria. For example, if a schedule deletes tickets that are three
years old, it will start deleting them within 72 hours of reaching that age. Up to
200,000 tickets per account per day will be deleted.

After they are activated, deletion schedules aren't a one-off event. Zendesk
continuously searches for and deletes tickets that meet the conditions unless you
deactivate the schedule. There is no impact on performance when schedules delete a
large volume of tickets or run during busy periods.

Tickets deleted by deletion schedules aren't included in the Deleted Tickets view.
You can track these changes in the [audit log](https://support.zendesk.com/hc/en-us/articles/4408828001434) by filtering by **Activity type:
Deleted**.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/tickets_deleted_audit_log.png)

Note: Deleted tickets are excluded from most Explore reports by
default. To report on ticket deletion events, use the [Updates history dataset](https://support.zendesk.com/hc/en-us/articles/4408827693594#topic_as3_slp_4y) to create a report
with the **Activity > Deletions** metric. SLA data from deleted tickets is also
retained in the [SLAs dataset](https://support.zendesk.com/hc/en-us/articles/4408827693594#topic_cyq_fr4_l2b).

## Considerations

- If you're also using attachment deletion schedules, you may want to delete
  tickets by when they're *created* instead of when they're *updated*.
  When attachments are removed from tickets through attachment deletion schedule,
  the ticket is updated. This will which impact when tickets are deleted if you
  set your conditions based on updated date.
- Deleted attachments are excluded from most Explore reports by default. To report
  on ticket deletion events, use the [Updates history dataset](https://support.zendesk.com/hc/en-us/articles/4408827693594#topic_as3_slp_4y) to create a
  report with the **Activity > Deletions** metric. SLA data from deleted
  tickets is also retained in the [SLAs dataset](https://support.zendesk.com/hc/en-us/articles/4408827693594#topic_cyq_fr4_l2b).

## Creating ticket deletion schedules

Admins and [agents in custom roles](https://support.zendesk.com/hc/en-us/articles/4408882153882) with permission can
create up to 10 ticket deletion schedules, but only one ticket deletion schedule can
be active at a time. If you have the [Advanced Data Privacy and Protection add-on](https://support.zendesk.com/hc/en-us/articles/6561144266906), you can
activate up to 10 ticket deletion schedules.

Tip: To give feedback on more conditions to add,
complete this short [Google form](https://docs.google.com/forms/d/e/1FAIpQLSdjZXhMzcZ3IGl7-6GubfPKOGfHCkyGjJdKevLMPGfvQap7Ag/viewform).

**To create a ticket deletion schedule**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png)
   **Account** in the sidebar, then select **Security > Deletion schedules**.
2. Click **Create deletion schedule** > **Tickets**.

   If you already have
   10 ticket deletion schedules created, a message appears notifying you that
   you’ve reached your limit. You must delete a schedule before you can create
   a new one.
3. Enter the **Schedule name**.

   Use a consistent naming convention to help you
   recognize similar types of deletion schedules.
4. (Optional) Enter a **Description** for your deletion schedule.
5. For **Category**, indicate when to delete tickets based on when the ticket
   was **Created** or **Last updated**. This field is required.
6. Click **Add condition** to add an additional *All* condition for
   deleting tickets, such as by organization or brand. See [Building condition statements for ticket deletion schedules](#topic_sxn_sfy_m1c).

   If you have the [Advanced Data Privacy and Protection
   add-on](https://support.zendesk.com/hc/en-us/articles/6561144266906), you can add deletion criteria that meet *All* or
   *Any* conditions. There is no limit to the number of conditions you
   can add.
7. Select a **Category**, **Operator**, and **Value** for each
   condition.

   The operator determines the relationship between the category
   and the value. For example, if you select the operator *Is*, your
   category must equal the value.

   Note: Deletion
   schedules delete only archived tickets, which are tickets that have been
   closed for more than 120 days. If you create a condition to delete tickets
   before 120 days, tickets are deleted at 120 days.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/deletion_schedule_conditions.png)
8. (Optional) After conditions are added, click **Preview** to preview an
   approximate number of tickets that match and will be deleted when the schedule
   is active.
9. Click **Create**.

   Your new deletion schedule is added to the end of the
   list as an inactive schedule.
10. [Activate](https://support.zendesk.com/hc/en-us/articles/8301879320474#topic_nlj_q4y_fdc) the deletion schedule.

## Building condition statements for ticket deletion schedules

Condition statements consist of categories, field operators, and condition values
(which vary depending on the category selected). Condition statements are
essentially "if" statements that delete tickets meeting the specified criteria.

The table below lists the categories available for building condition statements for
ticket deletion schedules.

Table 1. Ticket deletion schedule categories

| Category | Description |
| --- | --- |
| Last updated | Deletes tickets based on when they were last updated. At least one Last updated condition is required. Deletion schedules delete tickets that have been *closed and not modified* for the period of time specified for Last updated. For example, if Last updated is set to 365 days, and the ticket was modified within that time, the ticket is not deleted. The clock starts over, and the ticket will be deleted 365 days from the modification date. |
| Created at | Deletes tickets based on when they were created. |
| Custom fields | Deletes tickets based on custom field values. |
| Attachment | Deletes tickets based on whether an attachment is present (does not include Messaging attachments). |
| Brand | Deletes tickets by brand. |
| Support type | Deletes tickets based on whether they were handled by an agent or [AI agent](https://support.zendesk.com/hc/en-us/articles/6970583409690). See [Creating a deletion schedule for AI agent tickets](https://support.zendesk.com/hc/en-us/articles/9752192560410). |
| Form | Deletes tickets by ticket form, if you use multiple [ticket forms](https://support.zendesk.com/hc/en-us/articles/4408846520858). |
| Group | Deletes tickets by [group](https://support.zendesk.com/hc/en-us/articles/4408894175130). |
| Type | Deletes tickets based on the ticket type: Question, Incident, Problem, or Task. |
| Support type | Deletes tickets based on the support type: Agent (human) or AI agent (bot). [Learn more about AI agent tickets.](https://support.zendesk.com/hc/en-us/articles/9204149016346) |
| Requester | Deletes tickets based on the requester name. |
| Organization | Deletes tickets based on organization, if you have multiple [organizations](https://support.zendesk.com/hc/en-us/articles/4408886146842). |
| Tags | Deletes tickets with the selected [ticket tags](https://support.zendesk.com/hc/en-us/articles/4408835059482). |