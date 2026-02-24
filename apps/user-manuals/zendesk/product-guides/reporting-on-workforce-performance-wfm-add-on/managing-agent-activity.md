# Managing agent activity

Source: https://support.zendesk.com/hc/en-us/articles/6487941570970-Managing-agent-activity

---

Admins can manage agent activity by adding, editing, and deleting completed activities on theAgent activity page. Ongoing activities cannot be edited or deleted. All changes apply only to past, fully completed activities from the last 31 days.

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | Workforce Management (WFM) or Workforce Engagement Management (WEM) |

Verified AI summary ◀▼

Manage agent activity to ensure accurate tracking of their work. You can add, edit, or delete completed activities from the last 31 days, addressing issues like forgotten task switches or tracking errors. Note that ongoing activities can't be modified. Changes update metrics immediately, but adherence recalculations may take time. Use hidden activities to prevent overlaps when adjusting timelines.

Admins can manage agent activity by adding, editing, and deleting completed activities on the
[Agent activity page](https://support.zendesk.com/hc/en-us/articles/6443347506970). Ongoing activities cannot be edited or deleted.
All changes apply only to past, fully completed activities from the last 31 days.

It’s important to manage agents' activities to ensure their work is tracked
accurately. For example, you may need to address situations where:

- An agent forgot to switch to a [general task](https://support.zendesk.com/hc/en-us/articles/7069811858586) or [unified status](https://support.zendesk.com/hc/en-us/articles/10114746509978), such as a lunch break.
- An activity was mistakenly deleted and needs to be restored.
- There was a tracking error, resulting in no activity being recorded.
- The timeline needs to align with the actual work done, including associating
  ticket activities with the correct workstream.

**To manage agent activities**

1. In [Workforce management](https://support.zendesk.com/hc/en-us/articles/4408838272410), click the agent folder (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_agent_folder_icon.png)) in the navigation bar, then select **Agent
   activity**.
2. (Optional) If you want to edit activity for a previous day, use the date picker.
3. Click the name of the agent whose activity you want to edit.
4. From the **Summary** panel, click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/macros_edit_menu_icon.png)) and select **Edit activities**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ts_agent_activity_edit_activity.png)
5. Take any of the following actions:

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_activities_editing.png)

   - Edit the time spent on an activity by adjusting its start or end time, or update the
     activity performed during that time.

     Note: When updating an activity, it's not possible
     to change one workstream to another workstream, update a general task to a workstream,
     edit the activity type for [agent statuses](https://support.zendesk.com/hc/en-us/articles/10114746509978), or change untracked time to a
     workstream.
   - Manually add new activities, such as ticket activities, general tasks, agent statuses,
     or untracked time, directly into the agent’s activity timeline. New activities can be
     added before or after existing ones; therefore, they can only be added to days that
     already have activities.

     For ticket activities, add the ticket ID.

     Note: If you’ve [activated the unified agent status synchronization for
     WFM](https://support.zendesk.com/hc/en-us/articles/10114746509978), you can only add or edit ticket-based activities. [Chrome Extension activities](https://support.zendesk.com/hc/en-us/articles/6676772528026) can only be deleted.
   - Delete the activity. This action can't be undone.
6. Click **Done**.

   Metrics associated with new activities, such as total work
   time and ticket count, are updated immediately and reflected across all views, including
   reports and agent attendance. However, adherence recalculation is handled asynchronously,
   which means the timing of this update is not immediate and may vary depending on the
   effort required for recalculation.

   When an activity is edited or deleted, you can
   view who made the change and when by hovering over the information icon.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ts_agent_acitivity_edited_view.png)

## About hidden activities

When editing an activity, in between the End Day and Start Day, there's a *Hidden*
activity entry. This entry behaves like any other activity, with the exception that the
activity type can't be changed and is visible only when editing activities.

The hidden activity helps you avoid overlapping entries when extending or reducing Start
Day and End Day times. With this entry, when extending start or end times, you must edit the
hidden activity to the desired extended time first and then extend the start or end times to
the same time.

To edit and add a new activity immediately after a hidden activity,
set its end time to 00:00:00. Adjust the start time of the existing activity to prevent
overlap with the new one, and then click to add a new activity before the existing one.
This ensures that the hidden activity is no longer visible due to the time
adjustment.