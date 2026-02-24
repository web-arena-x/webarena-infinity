# Generating and publishing your WFM schedule

Source: https://support.zendesk.com/hc/en-us/articles/6443348279194-Generating-and-publishing-your-WFM-schedule

---

After configuring your organization structure, you can generate a schedule based on youractive forecasts. Your forecasted workload, combined with your organizational setup, allows you to automatically generate a detailed schedule complete with breaks, channel specific assignments, and more.

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | Workforce Management (WFM) or Workforce Engagement Management (WEM) |

Verified AI summary ◀▼

Generate and publish your WFM schedule to align staffing with forecasted workloads. Create schedules for all agents or specific groups, and publish them so agents receive notifications of changes. You can revert to the last published version if needed. This process helps manage staffing needs effectively, ensuring agents are aware of their tasks and shifts.

After configuring your organization structure, you can generate a schedule based on your [active forecasts](https://support.zendesk.com/hc/en-us/articles/9940054229402). Your forecasted workload, combined with your
organizational setup, allows you to automatically generate a detailed schedule complete with
breaks, channel specific assignments, and more.

Automatically generating the schedule based on your active forecast helps you create better
schedules. You can still [edit your schedule](https://support.zendesk.com/hc/en-us/articles/6443365957274) to optimize your staffing requirements
further.

When you publish the schedule, agents see any change to their schedule on their [Agent Schedule app in Zendesk](https://support.tymeshift.com/hc/en-us/articles/21706381844115).

This article contains the following sections:

- [Understanding how the schedule is
  generated](#topic_lsj_spl_y1c)
- [Generating the schedule](#topic_pvq_cs5_zzb)
- [Publishing the schedule](#topic_jtc_ds5_zzb)
- [Reverting published schedules](#topic_khv_fnm_bgc)

Related articles

- [About the WFM Schedule page](https://support.tymeshift.com/hc/en-us/articles/22420502704915)

## Understanding how the schedule is generated

The schedule is generated based on the [active forecasts](https://support.zendesk.com/hc/en-us/articles/9940054229402). If there's no forecast for a workstream, the
schedule is based on coverage and location requirements.

A schedule can’t be generated if the forecast fails to generate. For example, the
forecast won’t generate if a workstream has no data.

If a workstream has data but displays zero inbound volume when you're generating
the schedule, then the automatic schedule will randomly assign a workstream to an agent.

## Generating the schedule

You must be an admin to generate the schedule. You can generate the schedule for all agents in your
account or choose to generate it for a single agent, by group, location, or team.

You can generate a schedule up to 90 days in the future.

Note: Your organization structure must be set up before you can generate a schedule. See [Setting up your organization structure](https://support.zendesk.com/hc/en-us/articles/6514632760730#topic_l4n_wmd_d1c).

**To generate the schedule for all agents**

1. In [Workforce management](https://support.zendesk.com/hc/en-us/articles/4408838272410), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_calendar.png)
   **Schedule** in the navigation bar, then select **Schedule**.

   The schedule opens in the day view.
2. (Optional) Click the **Day** menu to switch to week or month view, or select a
   specific date or date range from the date picker.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ts_schedule_date_view.png)
3. Click **Generate**.
4. Select the date range for when you want a schedule to be created, then click
   **Run**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ts_schedule_generate_date_range.png)

   The schedule begins to generate. Depending on how many agents you
   have, it may take a few minutes to complete.

   When the schedule generation is
   complete, you'll see an assigned shift next to each agent. The [shift](https://support.zendesk.com/hc/en-us/articles/6443345205402) contains the tasks they need to work on at a particular
   time as well as any general tasks configured in the shift.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_schedule_unpublished_day.png)

   Agents’ shifts are highlighted and a yellow dot appears next to
   their names, indicating that the shifts are unpublished (see [Distinguishing unpublished shifts](https://support.zendesk.com/hc/en-us/articles/6443348256794#topic_mgb_hvl_y1c)).

   Next,
   you must publish the schedule so that agents will see the updated schedule in their
   Agent schedule app in Zendesk.

**To generate the schedule for a single agent, group, location, or team**

You can generate a shift for a single agent or for a group, location or team instead of
generating a schedule for your entire roster.

1. In [Workforce management](https://support.zendesk.com/hc/en-us/articles/4408838272410), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_calendar.png)
   **Schedule** in the navigation bar, then select **Schedule**.

   The schedule opens in the day view.
2. Hover over an agent, group, location, or team then click the plus sign (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_plus_icon.png)) icon.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ts_agent_schedule_by_team.png)

## Publishing the schedule

After you've generated the schedule, you must publish it so that agents can see their
schedule in the Agent schedule in Zendesk.

Tip: Highlighted shifts that have a yellow dot next to an agent’s name are
unpublished.

**To publish the schedule**

1. After [generating the schedule](#topic_pvq_cs5_zzb),
   click **Publish**.
2. Select the **Date range** you want to publish the schedule for. You can publish your
   schedule up to 90 days in the future.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ts_agent_schedule_publish_date_range.png)
3. Click the **Agents** tab and select which agents to publish the schedule for. You can
   publish the schedule for all agents, individual agents, by group, team, or location.
4. Click **Publish schedule**.

Note: Currently, there is no specific limit on the maximum period for publishing schedules in
the future. However, exceeding a two-year period may result in performance issues.

Whenever an agent’s schedule change is published, they receive a Zendesk push
notification.

![](https://zen-marketing-assets.s3.amazonaws.com/images/wfm_changes_schedule_notification.png)

Clicking the notification’s hyperlink takes the agent directly to their [agent schedule view](https://support.zendesk.com/hc/en-us/articles/6443374353434).

They also receive a push notification five minutes before the scheduled start
time of a new task.

![](https://zen-marketing-assets.s3.amazonaws.com/images/wfm_next_task_notification.png)

Third-party cookies must be allowed in the browser, and pop-up
blockers must be turned off for push notifications to work.

## Reverting published changes

You can revert the schedule to the last published version. This action applies to
a specific period and a selected set of agents, giving you control over which changes to
revert.

You can revert your schedule up to 90 days at once.

**Tip:** All changes can be tracked under the [WFM audit log](https://support.zendesk.com/hc/en-us/articles/6641426375066).

**To revert a published schedule**

1. In [Workforce management](https://support.zendesk.com/hc/en-us/articles/4408838272410), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_calendar.png)
   **Schedule** in the navigation bar, then select **Schedule**.
2. Click the **Revert schedule to last published** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_revert.png)) in the top right.
3. Select the **Date range** you want to revert the published schedule for.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_revert_schedule.png)
4. Click the **Agents** tab and select which agents to revert the published schedule
   for. You can revert a published schedule for all agents, individual agents, a group, [team](https://support.zendesk.com/hc/en-us/articles/6443329411994), or [location](https://support.zendesk.com/hc/en-us/articles/6443329411994).
5. Click **Revert changes**.