# Viewing the WFM audit log for changes

Source: https://support.zendesk.com/hc/en-us/articles/6641426375066-Viewing-the-WFM-audit-log-for-changes

---

The workforce management (WFM) audit log shows various changes in your account. Like theZendesk audit log, it saves a record of these changes, allowing you to view the entire change history or select a date range. Admins with permission can view the WFM audit log for changes, such as updates to automations or changes made to your schedule.

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | Workforce Management (WFM) or Workforce Engagement Management (WEM) |

Verified AI summary ◀▼

The WFM audit log helps you track changes in your account, capturing details like who made changes and when. You can view updates to settings, automations, schedules, and more. Use filters and search options to find specific events, making it easier to manage user-initiated changes like shift trades and time off requests. Adjust timestamps based on your timezone for accurate tracking.

The workforce management (WFM) audit log shows various changes in your account. Like
the [Zendesk audit log](https://support.zendesk.com/hc/en-us/articles/4408828001434), it saves a record of these changes, allowing you
to view the entire change history or select a date range. Admins with permission can view the
WFM audit log for changes, such as updates to automations or changes made to your
schedule.

Note: The WFM audit log shows changes from the date it’s activated in your account
onward.

This article contains the following sections:

- [About the WFM audit log
  changes](#topic_d1s_xmh_q1c)
- [Viewing the WFM audit log](#topic_bg4_c4h_q1c)
- [Filtering and searching the WFM audit
  log](#topic_ycn_wsh_q1c)

## About the WFM audit log changes

The audit log captures types of changes and provides details for each log entry. Use the
audit log to have a better understanding of the changes that occur in your account. The
audit log can help you solve day-to-day questions, such as what changed, who made the
change, and when it happened.

Admins can keep track of user-initiated changes made in the account. For example, you can
view when agents request shift trades and when time off requests are approved or denied.

### Changes captured in the WFM audit log

The WFM audit log shows user-initiated changes to the following areas:

|  |  |
| --- | --- |
| **Area** | **Type of activity** |
| [Account settings](https://support.zendesk.com/hc/en-us/articles/6443329207834#topic_e3l_23k_1bc) | - Account settings updated - Allow list turned on/off - Allow list email addresses updated - Block list turned on/off - Block list email addresses updated - [Unified agent status synchronization](https://support.zendesk.com/hc/en-us/articles/10114746509978)   turned on/off |
| [Automations](https://support.zendesk.com/hc/en-us/articles/6443374423066) | - Automation created - Automation updated - User assignment in automation updated - Automation deleted |
| [General tasks](https://support.zendesk.com/hc/en-us/articles/6443329426330) | - General task created - General task updated - General task deleted |
| Integrations | - [Google Calendar integration](https://support.zendesk.com/hc/en-us/articles/6443354603418) turned on   or off |
| [Locations](https://support.zendesk.com/hc/en-us/articles/6443345205402) | - Location created - Location updated - Location deleted - Modifications to shifts and folders within locations:   - Shift created, updated, and deleted   - Folder created, updated, and deleted |
| Organization structure  This area captures changes to [Teams](https://support.zendesk.com/hc/en-us/articles/6443329411994) only. | - Team created - Team updated |
| [Roles and permissions](https://support.zendesk.com/hc/en-us/articles/6443374440090) | - Role created - Role deleted - Role permissions updated - Role scopes updated - Role members updated |
| [Schedule](https://support.zendesk.com/hc/en-us/articles/6443348256794) | - Schedule published - Schedule generated - Schedule imported - Shift updated - Shift deleted - Partial or full day time off added - Time off deleted - Bulk edited:   - Add task   - Delete shift   - Edit shift |
| [Shift trade management](https://support.zendesk.com/hc/en-us/articles/6443354721178) | - Shift trade approved/denied - Shift trade requested |
| [Time off management](https://support.zendesk.com/hc/en-us/articles/6443393050394) | - Time off reason created - Time off reason updated |
| [User management](https://support.zendesk.com/hc/en-us/articles/7052274669338) | - Task lock updated: Turned on or off - Auto-tracking updated: Turned on or off - Export CSV team members list |
| Workstreams | - Workstream created - Workstream updated - User assignment in workstream updated - Workstream deleted - Workstream prioritization (EAP) enabled/disabled |

### WFM audit log entries

The following information is included for each entry in the audit log:

|  |  |
| --- | --- |
| **Column** | **Description** |
| Time | Time and date the event occurred |
| Area | The area affected by the event |
| Item | Object changed by the actor |
| Activity type | Type of action for the event (created, deleted, exported, or updated) |
| Actor | User that caused the event |
| Activity | Details about the event |

The WFM audit log timestamps are based on the timezone settings of each user. Click the
[timezone picker icon](https://support.zendesk.com/hc/en-us/articles/6443314319258) (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_timezone_icon.png)) in the upper-right corner of the
navigation bar to adjust the timestamps accordingly.

## Viewing the WFM audit log

You can access the WFM audit log from the admin menu in WFM. From there, you can
sort the log by time, select a date range, or [filter and search the list](#topic_ycn_wsh_q1c).

**To view the WFM audit log**

1. In [Workforce management](https://support.zendesk.com/hc/en-us/articles/4408838272410), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_admin_icon.png)
   **Settings** in the navigation bar, then select **Audit log**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ts_wfm_audit_log.png)

## Filtering and searching the WFM audit log

When you visit the WFM audit log, you may only have partial information. For
example, you might know when a change occurred but not what changed, or who made a change
but not when it happened. Since the audit log can contain a large volume of events, using
filters and search options can help you find what you’re looking for more easily.

**To filter and search the
WFM audit log**

1. In [Workforce management](https://support.zendesk.com/hc/en-us/articles/4408838272410), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_admin_icon.png)
   **Settings** in the navigation bar, then select **Audit log**.
2. Take any of the following actions:
   - Click the **Time** column to sort the entries by date.
   - Click the date picker to select a specific date or date range.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ts_audit_log_date_picker.png)

   There's no specific limit on the period for generating audit
   logs. However, exceeding a one-year period may result in performance issues.
3. To filter by area or activity type, click **Filter**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_audit_log_filter.png)
4. Select the checkboxes for each area or activity type.
5. To search for a change made by a specific user, click the **Actor** column and enter
   the name of the user.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ts_audit_log_actor.png)