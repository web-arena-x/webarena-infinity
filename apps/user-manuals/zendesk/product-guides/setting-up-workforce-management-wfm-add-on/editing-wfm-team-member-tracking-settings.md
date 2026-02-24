# Editing WFM team member tracking settings

Source: https://support.zendesk.com/hc/en-us/articles/7446325512730-Editing-WFM-team-member-tracking-settings

---

This article describes how to edit tracking settings for team members in Zendesk Workforce management (WFM) user profiles.

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | Workforce Management (WFM) or Workforce Engagement Management (WEM) |

Verified AI summary ◀▼

Edit team member tracking settings to manage time and attendance. Use auto-tracking to automatically clock in agents with their first activity, or allow manual clock-ins by disabling it. Task lock keeps agents clocked into a single ticket while researching others. You can adjust these settings individually or in bulk, with changes taking precedence over account-level settings.

This article describes how to edit tracking settings for team members in Zendesk Workforce
management (WFM) user profiles.

Note: Tracking settings apply only to [the WFM time tracker](https://support.zendesk.com/hc/en-us/articles/6443354661402) in Zendesk Support. If [unified agent status synchronization](https://support.zendesk.com/hc/en-us/articles/10114746509978) is turned on for WFM, agents
should [set their unified agent statuses](https://support.zendesk.com/hc/en-us/articles/4410545721114#topic_xvw_ytp_m5b) in the Agent
Workspace.

This article contains the following topics:

- [Understanding team member tracking
  settings](#id_x4d_jhk_pdc)
- [Editing a team member's tracking
  settings](#topic_nzr_shk_pdc)
- [Bulk editing team members' tracking
  settings](#topic_swn_4vd_1fc)

Related articles:

- [Accessing and viewing the WFM User management page](https://support.zendesk.com/hc/en-us/articles/7052274669338)

## Understanding team member tracking settings

Zendesk WFM has the following agent tracking settings:

- **Auto-tracking**: With auto-tracking on, Zendesk WFM takes care of time and
  attendance management for most of your agents’ workflows. The first activity that the
  agent does automatically clocks them in and starts their day. This setting is activated
  for everyone by default.

  Deactivating auto-tracking allows agents to manually
  start and end their days. Moving between tabs and views in Zendesk support no longer
  automatically triggers a new activity event. See [Starting and ending your day in the Zendesk WFM time
  tracker](https://support.zendesk.com/hc/en-us/articles/6443354661402).
- **Task lock**: Allows agents to remain clocked into a single ticket or task while
  opening other tickets. This is helpful when an agent needs to research past tickets while
  continuing to track the time for a ticket they're working on. See [Using task lock](https://support.zendesk.com/hc/en-us/articles/6443329257114).

## Editing a team member's tracking settings

Editing the tracking settings from a team member’s WFM profile applies the changes to that
team member only. If you want to manage the tracking settings of multiple team members at a
time, you can [edit them in bulk](#topic_swn_4vd_1fc).

Keep in mind that editing a team member's user settings takes precedence over any
account-level settings. If you edit your [account-level task lock setting](https://support.zendesk.com/hc/en-us/articles/6443329357210) later, the change doesn't apply to
team members who have auto-tracking and task lock set in their WFM profiles already.

**To edit a team member’s tracking settings**

1. In [Workforce management](https://support.zendesk.com/hc/en-us/articles/4408838272410), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_admin_icon.png)
   **Settings** in the navigation bar, then select **User management**.
2. On the User management page, click any team member to access their
   settings.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_user_management.png)
3. If you don't want to track the agent's Zendesk activity automatically, deselect the
   **Turn on auto-tracking** option.

   Deselecting this option allows the agent to
   decide when to clock in and out.
4. To allow agents to remain clocked into a single ticket or task while opening other
   tickets, select **Turn on task lock**, then click **Save**.

## Bulk editing team members' tracking settings

You can edit the tracking settings of multiple team members at once from the User
management page. When you edit team members' tracking settings, the changes in their WFM
profiles take precedence over your [account-level task lock setting](https://support.zendesk.com/hc/en-us/articles/6443329357210).

**To bulk edit team members' tracking settings**

1. In [Workforce management](https://support.zendesk.com/hc/en-us/articles/4408838272410), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_admin_icon.png)
   **Settings** in the navigation bar, then select **User management**.
2. Select the check boxes of the team members whose tracking settings you want to
   edit.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_user_bulk_manage.png)

   To quickly find team members, you
   can [search or filter the list](https://support.zendesk.com/hc/en-us/articles/7052274669338#topic_gb2_kcr_tbc). If you already
   selected team members, then your selections are cleared if you search or
   filter.

   Alternatively, you can select the checkbox at the top of the list to
   select all team members on the page. If you navigate to the another page in the list,
   team members you already selected stay selected.
3. In the footer, click either **Auto tracking** or **Task lock**.
4. If you clicked **Auto tracking**, select one of the following:
   - **Turn on auto tracking**: Automatically tracks the selected agents' activities
     in Zendesk.
   - **Turn off auto tracking and task lock**: Switches to manually tracking the
     selected agents' activities and deactivates task lock for them. Task lock keeps
     agents clocked into a single ticket or general task while browsing other
     tickets.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_user_bulk_manage_auto_tracking.png)
5. If you clicked **Task lock**, select one of the following:
   - **Turn on task lock and auto tracking**: Activates task lock for the selected
     agents and automatically tracks their activities in Zendesk.
   - **Turn off task lock**: Deactivates task lock for the selected agents. When
     agents are browsing other tickets, they'll no longer be clocked into a single ticket
     or general task.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_bulk_manage_task_lock.png)
6. Click **Save**.

   The team members' tracking settings are updated and the changes
   are reflected in [the audit log](https://support.zendesk.com/hc/en-us/articles/6641426375066).