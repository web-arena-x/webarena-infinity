# Viewing the audit log for changes to your account

Source: https://support.zendesk.com/hc/en-us/articles/4408828001434-Viewing-the-audit-log-for-changes-to-your-account

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Enterprise or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Enterprise |

Verified AI summary ◀▼

Access the audit log to track changes made by admins and agents to your account. View detailed entries, including time, actor, and activity type. Use filters to find specific events and export the log as a CSV file. This feature helps you monitor account modifications and maintain a clear record of activities.

Location:  Admin Center > Account > Logs > Audit log

The audit log allows customers on Enterprise plans and above to view various
changes in their Zendesk account since the account was created. It saves a
record of these changes indefinitely, and you can view the entire change
history.

Admins and [agents with permission](https://support.zendesk.com/hc/en-us/articles/4408882153882) can
view the audit log in [Admin
Center](#topic_msk_g4r_slb) or through the [Support API](https://developer.zendesk.com/rest_api/docs/support/audit_logs).

This article contains the following sections:

- [About the audit log changes](#topic_j15_wxq_slb)
- [Viewing the audit log in Admin Center](#topic_msk_g4r_slb)
- [Filtering the audit log](#topic_lvh_mft_jsb)
- [Exporting the audit log](#topic_vsy_nss_jsb)

## About the audit log changes

There are two key things to understand about the audit log: the [types of changes
captured](#topic_gfd_rpg_nxb) and the [details provided for each log
entry](#topic_a5l_tpg_nxb).

### Changes captured in the audit log

The audit log tracks changes that agents and admins have made to
your Zendesk account. End user activities are not
captured.

The audit log shows changes to the following areas:

- Account information and settings
- Users (updates to existing users only; activities
  related to creating new users are not captured)
- Apps
- Web Widget
- Business rules
- Ticket settings
- Organizations
- Custom objects

### Audit log entries

For each entry in the audit log, the following information is
included:

| Column | Description |
| --- | --- |
| Time | Time and date the event occurred |
| Actor | User or system that caused the event Some changes are performed through automated system processes and appear as actions by the system user "Zendesk." |
| IP address | IP address of the user who caused the event |
| Item | Object changed by the actor |
| Activity type | Type of action for the event (Created, Updated, Deleted, Exported, or Signed in) |
| Activity | Details about the event |

In Admin Center, audit log timestamps appear in [your account's time
zone](https://support.zendesk.com/hc/en-us/articles/4408887059866#topic_dil_hnc_xe). If you are unsure what time the audit
log is using, hover over the information icon in the
**Time** column heading.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/audit_log_time_zone.png)

In the Zendesk API and CSV export file, audit log timestamps
appear in Coordinated Universal Time (UTC).

## Viewing the audit log in Admin Center

From the Audit log page in Admin Center, you can view the audit log as a
whole, sort the log by time, [filter the list](#topic_lvh_mft_jsb), or export a copy of
the log.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_audit_log_type.png)

**To view the audit log**

- In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png)
  **Account** in the sidebar, then select **Logs > Audit log**.

## Filtering the audit log

Often, only part of the picture is available when you visit the audit
log. For example, you might know when something changed (but not
what) or who changed something (but not when). Since the audit log
can include a large volume of events, filtering makes it easier to
find what you’re looking for.

While top audit events are available as filters, not all event types can
be filtered. Additional audit events will be added over time.

Tip: If you repeat the same audit log
filters, bookmark them in your web browser after you apply them. The
filter displays in the URL.

**To filter the audit log**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png)
   **Account** in the sidebar, then select **Logs > Audit log**.
2. Click the **Time** column to sort the entries by date.
3. To use more filters, click **Filter**.

   Additional filters
   appear in a side drawer.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_audit_log_filters_drawer.png)
4. To find entries within a specific date range, enter a **Start
   date** and **End date**.
5. Enter a name in the **Actor** field to filter by the
   people or systems responsible for the
   activities.
6. Select an **Activity type** to filter entries by the action
   type (Created, Updated, Deleted, Exported, or Signed
   In).
7. Use the filters in the Item section to filter by a specific
   setting, user, or business rule that has changed.
   1. In the **Type** field, select or search for
      the generic item type you want to filter by (for
      example, "trigger").

      An initial list of item
      types appears in the dropdown, but you can start
      typing to access more. For example, typing
      **cus** displays the Customer, Custom Status,
      and Custom Object item types.
   2. In the **Names** field, select or search for
      the specific items you want to filter by (for
      example, the trigger named "Notify assignee of
      comment update").
8. Click **Apply filters**.

## Exporting the audit log

You can export a CSV formatted copy of the audit log. If you filter the
list before starting the export, the CSV file is also filtered this
way. The exported copy is emailed to your primary Zendesk email
address.

**To export a copy of the audit log**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png)
   **Account** in the sidebar, then select **Logs > Audit log**.
2. [Filter the audit
   log](#topic_lvh_mft_jsb) as needed.
3. Click **Email CSV**.