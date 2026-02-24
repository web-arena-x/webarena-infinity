# About the Agent attendance page

Source: https://support.zendesk.com/hc/en-us/articles/6443347522074-About-the-Agent-attendance-page

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | Workforce Management (WFM) or Workforce Engagement Management (WEM) |

Verified AI summary ◀▼

The Agent attendance page helps you track and analyze agent attendance metrics, such as logged time, breaks, and time off. You can filter attendance data by criteria like location and team, and export it to a CSV file for further analysis. This feature aids in understanding agent performance and identifying patterns, supporting better workforce management decisions.

The Agent attendance page in Zendesk Workforce management (WFM) allows you to easily view who is currently working, their logged time, who may have started late, who is absent, and more.

Managers can analyze detailed attendance metrics, such as time logged, unpaid breaks, and time off. They can also view exact clock in and clock out times for each agent's shift, understand how agents allocate their time across shifts, and identify patterns over time, such as frequent late logins or unplanned time off. These insights can support better decision-making in workforce management.

This article contains the following sections:

- [Accessing the Agent attendance page](#topic_pvz_qpj_wbc)
- [Understanding agent attendance](#topic_otg_2vj_wbc)
- [Filtering agent attendance](#topic_iwl_wrj_wbc)
- [Exporting agent attendance indicators](#topic_bww_3zk_tfc)

## **Accessing the Agent attendance page**

You must be a WFM admin or a [manager with permission](https://support.zendesk.com/hc/en-us/articles/6443374440090) to view the Agent attendance page in WFM.

**To access the Agent attendance page**

- In [Workforce management](https://support.zendesk.com/hc/en-us/articles/4408838272410), click the agent folder (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_agent_folder_icon.png)) in the navigation bar, then select **Agent attendance**.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_attendance_2shifts.png)

 From this page, you can do the following:
 - [View agent attendance information](#topic_otg_2vj_wbc)
 - [Filter the information on the page](#topic_iwl_wrj_wbc)
 - [Export agent attendance information to a CSV file](#topic_bww_3zk_tfc)

## Understanding agent attendance

The Agent attendance page helps you understand agent performance. Click an agent’s row for a more granular view.

As a manager, you can see agents' attendance for your selected day in your local time zone.
However, if you're viewing data for an agent in a different time zone, times may appear as if they're from the previous day. It's recommended that you adjust your time zone settings to match the agent you are viewing. See [Using the WFM time zone switcher](https://support.zendesk.com/hc/en-us/articles/6443314319258).

The Agent attendance page consists of the following fields:

- **Scheduled**:The agent's assigned shift for the selected day.

 If an agent displays an expandable list, this indicates that they have two shifts on the same day. Each line displays the indicators for that shift.
- **Time Scheduled**: The duration of the agent's scheduled workday.
- **Logged**: Time intervals when the agent was logged in, tracked through clock-in and clock-out events.

 Data in the user interface refreshes every five minutes.
- **Time Logged**: The total duration the agent was logged in up to the latest data refresh.
- **Unpaid Breaks**: The duration of unpaid break time logged by the agent.
- **Late**: The time between the scheduled start and the actual login time.
- **Left Early**: The time the agent logged off before the scheduled end of their shift.
- **Overtime**: On the attendance page, data is grouped by shift. If an agent is logged in and records activities throughout the day during a one-hour window before a scheduled shift starts and a one-hour window after a scheduled shift ends, this activity time is counted as overtime.

 Any activities outside the period starting one hour before the shift and ending one hour after the shift time frame are no longer categorized as overtime under a regular shift. Instead, these activities are categorized as a new shift (Shift 2) and as Not scheduled.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_not_scheduled_shift.png)
- **Unplanned time off**: The duration of unplanned time off, shown in hours.
- **Planned time off**: The duration of planned time off, shown in hours.
- **[Occupancy](https://support.zendesk.com/hc/en-us/articles/6443331680538#topic_ocb_3n4_52c__occupancy_rate)**: Percentage of time used in productive activities within paid time.

## **Filtering agent attendance**

Filter agents' attendance based on criteria such as attendance type, location, team, and group. You can also hide agents meeting specific conditions.

The following filtering options are available:

**Attendance**

- Clocked in
- Clocked in and not scheduled
- Late today (Agents who arrived late at any point during the day. They may currently be working.)
- Late right now (Agents who are late and have not started their shift at the time the report is being consulted.)
- Left early
- Overtime
- Shift started
- Time off

**Hide**

- Hide users with no schedule
- Hide users with no activity

## Exporting agent attendance indicators

You can export agents' attendance indicators to a CSV file.

The exported file reports agents' attendance indicators for a selected day, and can help you identify patterns in agent behavior over time.

Note that the CSV export reflects the latest backend state at the time of the export request however, the user interface refreshes every five minutes. If changes occur within this refresh interval, such as scope adjustments or [updates to the allowed and blocked agent lists](https://support.zendesk.com/hc/en-us/articles/6443374452250), the list of agents displayed on your screen may not match the export.

**To export agents' attendance indicators**

1. In [Workforce management](https://support.zendesk.com/hc/en-us/articles/4408838272410), click the agent folder (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_agent_folder_icon.png)) in the navigation bar, then select **Agent attendance**.
2. Click the date picker to select a specific date or date range for your CSV export file.

   Note: The export is limited to 800 agents and 800 activities per agent. If your export request exceeds this limit, use the filters to decrease it.
3. Click **Export CSV** in the top right corner of the Agent attendance page.
4. Check your inbox for an email with the link to download the CSV export of your agents’ attendance activity for the selected date and metrics.

   The CSV file is accessible only through this secure link. The link expires after 30 days.

   The exported report includes the following:

   - Date
   - Agent name
   - Schedule
   - Time Scheduled
   - Logged
   - Time Logged
   - Unpaid breaks
   - Late
   - Left early
   - Overtime
   - Planned Time off
   - Unplanned Time off
   - Occupancy