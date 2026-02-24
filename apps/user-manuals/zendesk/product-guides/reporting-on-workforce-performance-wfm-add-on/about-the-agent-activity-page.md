# About the Agent activity page

Source: https://support.zendesk.com/hc/en-us/articles/6443347506970-About-the-Agent-activity-page

---

The Agent activity page in Zendesk Workforce management (WFM) helps you visualize the time agents spend in differentworkstreams,general tasks,unified agent statuses, anduntracked time, or idle time throughout the day.

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | Workforce Management (WFM) or Workforce Engagement Management (WEM) |

Verified AI summary ◀▼

The Agent activity page helps you track and analyze agent productivity and adherence by visualizing their daily tasks and time allocation. You can monitor workstreams, general tasks, and untracked time, and export data for deeper analysis. This feature aids in workforce planning, performance evaluation, and identifying trends or areas for improvement.

The Agent activity page in Zendesk Workforce management (WFM) helps you visualize the time agents
spend in different [workstreams](https://support.zendesk.com/hc/en-us/articles/6443314489242), [general tasks](https://support.zendesk.com/hc/en-us/articles/6443329426330), [unified agent statuses](https://support.zendesk.com/hc/en-us/articles/10114746509978), and [untracked time](https://support.zendesk.com/hc/en-us/articles/6443376913818#topic_xwv_3n4_52c__untracked_time), or idle time throughout the day.

Use this page to see what agents are working on compared to what they’re scheduled for. You
can also monitor adherence percentage and visualize agent productivity by viewing the [points](https://support.zendesk.com/hc/en-us/articles/6443376913818#topic_ocb_3n4_52c) agents receive while handling tickets.

This article contains the following sections:

- [Understanding agent activity
  tracking](#topic_evy_c2d_tzb)
- [Accessing the Agent activity
  page](#topic_bm2_k2d_tzb)
- [Viewing and filtering agent
  activity](#topic_ey3_5hd_tzb)
- [Monitoring agent's activity](#topic_ub5_whd_tzb)
- [Exporting agent talk activity
  statuses](#topic_yqp_wv3_dcc)
- [Exporting agent activity](#topic_css_zf5_ngc)

Related articles

- [Managing agent activity](https://support.zendesk.com/hc/en-us/articles/6487941570970)

## Understanding agent activity tracking

Agents are automatically clocked in when they start their first activity of the day. If
agents' days start with a task or status other than ticketing work, such as a meeting, you
can [create general tasks](https://support.zendesk.com/hc/en-us/articles/6443329426330) or [unified agent statuses](https://support.zendesk.com/hc/en-us/articles/10114746509978) for them to manually clock into.

All activities agents perform in Zendesk are automatically tracked. Their activity is
displayed on the Agent activity page and is separated into workstreams, general tasks, and
untracked time.

The tracked activity includes the points attributed to agents for ticketing work. Points
are metrics that measure agents’ ticketing activity. For example, an agent receives an
*attended point* when they change the status of the ticket. Learn more about [point metrics](https://support.zendesk.com/hc/en-us/articles/6443376913818#topic_ocb_3n4_52c).

On the Agent activity page, the points attributed to agents are displayed in their
*Productivity* timelines. See [Monitoring an agent’s activity](#topic_ub5_whd_tzb).

## Accessing the Agent activity page

The Agent activity page provides real-time monitoring that can help you make informed
decisions about allocating your workforce and quickly correct activity. In addition to the
day’s activity, you can access past days to analyze and correct agents’ activities, habits,
and patterns.

**To access the Agent activity page**

- In [Workforce management](https://support.zendesk.com/hc/en-us/articles/4408838272410), click the agent folder (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_agent_folder_icon.png)) in the navigation bar, then select **Agent
  activity**.

## Viewing and filtering agent activity

View groupings of agents by [location](https://support.zendesk.com/hc/en-us/articles/6443345205402), [Zendesk group](https://support.zendesk.com/hc/en-us/articles/4408886146842), or [team](https://support.zendesk.com/hc/en-us/articles/6443329411994). You can also view all agents.

**To view agent activity**

1. [Access](#topic_bm2_k2d_tzb) the Agent activity
   page.
2. In the left sidebar, click the menu and select a viewing option.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/tymeshift_agent_activity_grouping.png)
3. Filter agents with the following options:
   - Collapse or expand the folders to view only certain agents.
   - Search for agents, groups, teams, or locations. Enter an agent's name or email in
     the search bar to find a certain agent.

     Alternatively, use the [Zendesk WFM Quick Switcher keyboard shortcuts](https://support.zendesk.com/hc/en-us/articles/6443354534554) to quickly
     find an agent.
   - Use the date picker to view a previous day's activity. By default, the Agent
     activity page displays activity for the current date.

## Monitoring agent’s activity

You can monitor an agent’s activity more closely and view what they’re scheduled for, what
they’ve been working on, and their productivity.

Note: Agents must have a generated [schedule](https://support.zendesk.com/hc/en-us/articles/6443348279194). If an agent doesn't have one, they'll always be out of
adherence, which affects overall team adherence.

**To monitor an agent’s activity**

1. [Access](#topic_bm2_k2d_tzb) the Agent activity
   page.
2. [Find the agent](#topic_ey3_5hd_tzb) whose activity you
   want to view, then click their name.

   The agent’s activity expands. You can view their
   schedule, adherence, adherence percentage, talk state, and productivity.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ts_agent_activity_producitivity.png)

   When the [unified agents status synchronization](https://support.zendesk.com/hc/en-us/articles/10114746509978) is turned on you can
   also view agents’ status and availability.
3. Hover over an entry to view additional information, such as the workstreams or general
   tasks the agent clocked into, the ticket ID, the start and end time of the entry, the
   duration the agent spent on a ticket, any [chrome extension activity](https://support.zendesk.com/hc/en-us/articles/6676772528026), and the points the agent received
   while handling a ticket.

   Entries displayed in black indicate either a [No Workstream](https://support.zendesk.com/hc/en-us/articles/6443345024538#topic-1__no_workstreams) or a [Multiple Workstreams](https://support.zendesk.com/hc/en-us/articles/6443345024538#topic-1__multiple_workstreams) status.

   Note: To
   troubleshoot issues with tickets marked as No Workstream that you believe meet a
   workstream condition, see [Why do I see some agent activity entries in black?](https://support.zendesk.com/hc/en-us/articles/6947927377818).

   If you've activated [task lock](https://support.zendesk.com/hc/en-us/articles/6443329357210), you can track the time that agents spend locked
   into a task. These tasks appear as a diagonal line in the agent's activity.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/tymehsift_agent_activity_task_lock.png)
4. Use the right panel to view the **User summary** for the agent.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ts_agent_activity_user_summary.png)

   The summary includes their activities separated into [paid time](https://support.zendesk.com/hc/en-us/articles/6443376913818#topic_xwv_3n4_52c__paid_time) and [unpaid time](https://support.zendesk.com/hc/en-us/articles/6443376913818#topic_xwv_3n4_52c__unpaid_general_task_time).

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ts_agent_activity_user_summary_2.png)

   The summary also includes the agent’s talk states and productivity
   breakdown, which includes the agent’s points. See [point metrics](https://support.zendesk.com/hc/en-us/articles/6443376913818#Assigned%20Point).
5. To hide certain points from the Productivity timeline, hover over a points value in the
   Summary and click **Hide**.

## Exporting agent talk activity statuses

You can export agents’ talk activity statuses to a comma-separated values (CSV)
file.

By exporting data on agents' talk statuses durations into a spreadsheet, you can
analyze how your agents allocate their time, pinpoint areas for improvement, and tailor
insights to their specific needs.

The exported file reports on the tracked duration an agent spends in each state:
Online, Offline, Transfers Only, Away, On a Call, and Wrap Up for a selected day.

The generated report can also help you identify patterns in agent behavior over
time. You may uncover trends like frequent Away periods or constant switches to Transfers
Only state.

These insights can be leveraged to optimize operations and enhance agent
efficiency.

**To export agent talk activity**

1. [Access](#topic_bm2_k2d_tzb) the Agent activity
   page.
2. Select a past day or the current date for your export.
3. Click **Export CSV** in the top-right corner and select **Export Talk
   activity**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_export_talk_activity_button.png)
4. Check your inbox for an email with the link to download the CSV export of your agents’
   talk activity for the selected date.

   The CSV file is accessible only
   through this secure link and expires after 30 days.

The report contains the following information about each agent's status:

- Agent name
- Agent email
- Status name
- Start time
- End time
- Duration

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_talk_activity_csv.png)

Note: When exporting talk activity data for the current day, the request will display the
start time of each agent's status at the time of export. However, it will not include an
end time or duration for ongoing statuses.

## Exporting agent activity

Export agents’ activity timelines to a CSV file. This export includes detailed
entries of an agent’s day, such as workstreams, general tasks, and untracked time. It
provides a structured view of time allocation for deeper analysis outside of the WFM
interface.

These insights can be leveraged to optimize workforce planning and analysis, such
as identifying bottlenecks, unproductive periods, or excessive untracked time. They can also
support compliance and auditing, such as verifying activity logs against schedules and
internal policies. Additionally, these insights facilitate performance evaluations by
comparing time distribution trends across agents.

**To export agent activity**

1. [Access](#topic_bm2_k2d_tzb) the Agent activity
   page.
2. Select a past day or the current date for your export.
3. Click **Export CSV** in the top-right corner and select **Export agent
   activity**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_export_talk_activity_button.png)
4. Check your inbox for an email with the link to download the CSV export of your agents
   activity for the selected date.

   The CSV file is accessible only through this
   secure link and expires after 30 days.

The report contains the following information about each agent:

- Agent name
- Agent email
- Activity name
- Activity locked
- Activity type
- End time
- Duration

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_agent_activity_csv.png)