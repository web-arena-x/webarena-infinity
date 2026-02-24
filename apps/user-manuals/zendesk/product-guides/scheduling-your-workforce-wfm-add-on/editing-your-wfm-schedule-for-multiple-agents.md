# Editing your WFM schedule for multiple agents

Source: https://support.zendesk.com/hc/en-us/articles/6443365957274-Editing-your-WFM-schedule-for-multiple-agents

---

Aftergenerating your workforce management (WFM) schedule, you can edit it as needed. Quickly make changes to many agents' schedules at once with bulk editing. You can add, edit, and delete agents' shifts, schedule and replace tasks, and add time off.

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | Workforce Management (WFM) or Workforce Engagement Management (WEM) |

Verified AI summary ◀▼

Edit your workforce management schedule for multiple agents with bulk editing. You can add, edit, or delete shifts, schedule tasks, and manage time off. This feature helps you efficiently handle changes for many agents at once, saving time and ensuring your team’s schedule is always up-to-date. Use filters to target specific groups or agents for precise schedule adjustments.

Location: Zendesk WFM > Schedule

After [generating your workforce management (WFM) schedule](https://support.zendesk.com/hc/en-us/articles/6443348279194#topic_pvq_cs5_zzb), you can edit it as needed. Quickly make changes to many agents' schedules at once with bulk editing. You can add, edit, and delete agents' shifts, schedule and replace tasks, and add time off.

If you want to make changes to your schedule for a single agent, see [Editing your WFM schedule for an agent](https://support.zendesk.com/hc/en-us/articles/6931913462042).

This article contains the following topics:

- [Adding shifts](#topic_byj_tgc_v1c)
- [Editing shifts](#topic_gl2_13c_fdc)
- [Adding a task](#topic_dfm_5gc_v1c)
- [Deleting shifts](#topic_b3v_jyn_51c)
- [Adding time off](#topic_vlr_lzn_51c)
- [Replacing tasks](#topic_ttm_ctn_xgc)

Related article:

- [About the Schedule page](https://support.tymeshift.com/hc/en-us/articles/22420502704915)
- [Duplicating agent schedules](https://support.zendesk.com/hc/en-us/articles/9474004874010)

## Adding shifts

Edit your WFM schedule by adding shifts for multiple agents at once. When adding shifts in bulk, you can specify the shift type, a date range, and the agents for whom the shifts are being added.

**To add shifts for multiple agents**

1. In [Workforce management](https://support.zendesk.com/hc/en-us/articles/4408838272410), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_calendar.png)
   **Schedule** in the navigation bar, then select **Schedule**.
2. Click the **Bulk edit** menu, then select **Add shifts**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ts_schedule_bulk_edit_menu.png)
3. In the **Shifts** menu, select a shift type.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_add_shift_bulk.png)

   Your shifts are organized by location and include automatic, fixed, and rotating shifts. Learn more about [locations and shifts](https://support.zendesk.com/hc/en-us/articles/6443345205402).
4. Choose a **Date range**.
5. Optionally, select **Force generate shifts for all selected days regardless of location rules**.

   If you select this option, the days of the week in fixed shifts and the requirements and operational hours set in locations in automatic shifts are not applied.
6. Click the **Agents** tab and select the agents to whom you're adding this shift.
7. Click **Add shifts**.
8. Click **Publish** to publish the updated schedule.

## Editing shifts

Edit your WFM schedule by moving shifts for multiple agents at once. When changing shift start or end times in bulk, you can specify exact times or make relative adjustments by adding or subtracting time.

**To change shift start or end times for multiple agents**

1. In [Workforce management](https://support.zendesk.com/hc/en-us/articles/4408838272410), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_calendar.png)
   **Schedule** in the navigation bar, then select **Schedule**.
2. Click the **Bulk edit** menu, then select **Edit shifts**.
3. Choose a date range and select the agents whose shifts you need to change.
4. Click **Edit shifts** at the bottom and select **Change end time** or **Change start time**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_bulk_edit_shift_change_start_time.png)
5. Select the tab for either **Specific times** or **Relative adjustments**.
6. If you selected **Specific times**, choose the new start or end time using the calendar selector or the input field, then click **OK**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_bulk_edit_specific_times.png)
7. If you selected **Relative adjustments**, enter a time value to add or subtract to the current start or end time. For example, enter +00:30 to end 30 minutes later. Then click **OK**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_bulk_edit_relative_adjustment.png)

## Adding a task

Edit your WFM schedule by adding [general tasks](https://support.zendesk.com/hc/en-us/articles/6443329426330), [unified agent status](https://support.zendesk.com/hc/en-us/articles/10114746509978), or [workstreams](https://support.zendesk.com/hc/en-us/articles/6443314489242) for multiple agents at once.

When adding tasks, you have the option to make them recurring. For example, you may want to schedule recurring 1:1 meetings or trainings.

**To add a task for multiple agents**

1. In [Workforce management](https://support.zendesk.com/hc/en-us/articles/4408838272410), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_calendar.png)
   **Schedule** in the navigation bar, then select **Schedule**.
2. Click the **Bulk edit** menu, then select **Add task**.
3. From the **Task** menu, select a general task, unified status, or workstream.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_bulk_edit_task.png)
4. Choose a **Date**, **Start time**, and **Duration**.

   You can also add a note to provide more context to agents when this task is selected.

   The task displays a white corner, and agents can see the note by hovering over it.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/agent_schedule_task_note.png)
5. Keep **Add task even if user has no shift scheduled for this time** selected if the task occurs outside of the shift. For example, you may want to use this option for required meetings.
6. Optionally, turn on **Schedule recurring task**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_schedule_recurring_tasks.png)
7. If you're scheduling a recurring task, select how often you want the task to repeat and an end date.

   Note: You can schedule a recurring task to occur for up to 60 days in advance.
8. Click the **Agents** tab and select the agents to whom you're adding the task.
9. Click **Add tasks**.
10. Click **Publish** to publish the updated schedule.

    Agents receive a push notification informing them of the schedule changes. Clicking the link in the notification takes them to their [schedule](https://support.zendesk.com/hc/en-us/articles/6443374353434).

    ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_agent_schedule_notification.png)

## Deleting shifts

You can delete shifts for one or more agents. Save time by deleting multiple shifts at once, instead of one at a time.

**To delete shifts for multiple agents**

1. In [Workforce management](https://support.zendesk.com/hc/en-us/articles/4408838272410), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_calendar.png)
   **Schedule** in the navigation bar, then select **Schedule**.
2. Click the **Bulk edit** menu, then select **Edit shifts**.

   The Bulk edit shifts dialog opens. The date range you were viewing is selected by default.
3. Optionally, select a **Date range**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ts_bulk_edit_shifts.png)
4. Filter by **Group**, **Location**, or **Team**. You can select multiple groups, locations, or teams.

   Alternatively, search for specific agents in the **Agents** search bar.
5. Click **Filter results**.

   The agents’ shifts appear in a list.
6. Select the check box at the top of the table to select all filtered shifts. Or, select check boxes for shifts individually.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ts_schedule_bulk_edit_shifts_checkbox.png)
7. Click **Edit shifts**, then **Delete shifts**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ts_schedule_edit_shifts_delete_menu.png)
8. Confirm you want to delete the shifts by clicking **Delete shifts**.
9. Click **Publish** to publish the updated schedule.

## Adding time off

You can add time off for one or more agents. When you add time off in bulk, you can select multiple dates, as well as choose between full and partial days off.

If you want to manage your agents’ time off requests, see [About the Time off management page](https://support.zendesk.com/hc/en-us/articles/6443393050394).

**To add time off for multiple agents**

1. In [Workforce management](https://support.zendesk.com/hc/en-us/articles/4408838272410), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_calendar.png)
   **Schedule** in the navigation bar, then select **Schedule**.
2. Click the **Bulk edit** menu, then select **Add time off**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ts_schedule_bulk_edit_menu.png)

   The Bulk add time off dialog opens.
3. Select a predefined time off **Reason**.
4. For the Type, select either **Full day** or **Partial**.

   If you select Partial, define the **Start time** and **End time**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ts_schedule_bulk_time_off_partial.png)
5. Select one or more **Dates**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ts_schedule_bulk_time_off_dates.png)
6. Click the **Agents** tab.
7. Filter the list by **Group**, **Location**, or **Team**. You can also select specific agents or select all agents.

   For example, you may want to select all agents if you’re scheduling time off for a holiday.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_bulk_add_time_off.png)
8. Click **Add time off**.

   The time off for the selected agents is added to your schedule and published immediately.

## Replacing tasks

Edit your WFM schedule by replacing tasks for multiple agents at once. When replacing tasks in bulk, you can specify the original and the replacement [general task](https://support.zendesk.com/hc/en-us/articles/6443329426330) or [workstream](https://support.zendesk.com/hc/en-us/articles/6443314489242), a date range, a start and end time, and the agents for whom the task is being replaced.

**To replace a task for multiple agents**

2. Click the **Bulk edit** menu, then select **Replace tasks**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_schedule_bulk_edit_menu.png)
3. In the Bulk replace tasks menu, select the original general task or workstream you want to replace.
4. Select a replacement general task or workstream.
5. Choose a date range.
6. Define a time range for when the task starts for each day in your selected date range.
   For example, you can select October 5 to 10 between 10 AM and 11 AM. This selection finds all tasks that start between 10 AM and 11 AM on each day within that date range.
7. Select the agents for whom you’re replacing the task.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_bulk+replace+tasks.png)
8. (Optional) Click **Filter** to filter and search for team members by Group, Location, or Team. Enter the beginning of a name to autocomplete or select from the drop-down menu.
   You can select multiple groups, locations, teams, and users. Alternatively, search for specific agents in the Team member search bar.
9. Click **Replace tasks**.
10. Click **Publish** to updated the schedule.