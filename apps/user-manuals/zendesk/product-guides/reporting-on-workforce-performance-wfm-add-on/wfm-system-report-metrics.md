# WFM system report metrics

Source: https://support.zendesk.com/hc/en-us/articles/6443331680538-WFM-system-report-metrics

---

This article lists the metrics available for the system report templates in Zendesk Workforce management (WFM).

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | Workforce Management (WFM) or Workforce Engagement Management (WEM) |

This article lists the metrics available for the system report templates in Zendesk Workforce management (WFM).

This article contains the following topics:

- [Agent attendance report metrics](#topic_ocb_3n4_52c)
- [Time off report metrics](#topic_xwv_3n4_52c)

Related articles

- [About system WFM report templates](https://support.zendesk.com/hc/en-us/articles/6443363334810)
- [WFM custom report metrics](https://support.zendesk.com/hc/en-us/articles/6443376913818)

## Agent attendance report metrics

The Agent attendance report metrics include:

- [Attendance (duration)](#topic_ocb_3n4_52c__attendance_duration)
- [Attendance (rate)](#topic_ocb_3n4_52c__attendance_rate)
- [Late (duration)](#topic_ocb_3n4_52c__late_duration)
- [Late (occurrences)](#topic_ocb_3n4_52c__late_occurences)
- [Left early (duration)](#topic_ocb_3n4_52c__left_early_duration)
- [Left early (occurrences)](#topic_ocb_3n4_52c__left_early_occurrences)
- [Occupancy rate](#topic_ocb_3n4_52c__occupancy_rate)
- [Occupancy rate (with unified agent status synchronization)](#topic_ocb_3n4_52c__occupancy_rate_ocr)
- [Overtime (duration)](#topic_ocb_3n4_52c__overtime_duration)
- [Overtime (occurrences)](#topic_ocb_3n4_52c__overtime_occurrences)
- [Scheduled time](#topic_ocb_3n4_52c__scheduled_time)
- [Total time](#topic_ocb_3n4_52c__total_time)
- [Unpaid general task or status (duration)](#topic_ocb_3n4_52c__unpaid_general_task_duration)

| Metric | Description | Formula |
| --- | --- | --- |
| Attendance (duration) | Number of hours agents worked during their scheduled timeframes, regardless of adherence to their allocated schedules, within the requested timeframe. | N/A |
| Attendance (rate) | Measure of the hours an agent is scheduled to work against the hours they actually worked within the requested timeframe and date range. | Number of hours the agent is working / Number of hours the agent was scheduled to work |
| Late (duration) | Total time elapsed between the shift start and when the agent logged in, within the selected date range. | Sum of time of clock in time after schedule start time |
| Late (occurrences) | Count of occurrences when an agent logged in after their scheduled shift start time. This may happen multiple times in a single day. | Count clock in time after schedule start time |
| Left early (duration) | Total time elapsed between when the agent logged off and the scheduled end time of their shift for occurrences identified within the selected date range. | Sum of time of clock out before schedule end time |
| Left early (occurrences) | Count of occurrences when an agent logged off before their scheduled shift end time. This may happen multiple times in a single day. | Count of instances where the clock-out time is before the scheduled end time |
| Occupancy rate | Occupancy rate indicates the proportion of an agent's paid time spent on support-related activities versus non-support activities. The industry standard is 75-85%. | (Ticket time + Productive general task time) / (Ticket time + Productive general task time + Untracked time + Unproductive general task time) If you use [activity type as an attribute](https://support.zendesk.com/hc/en-us/articles/6443331692698#topic_tmj_khs_3fc) to group your report, the total of the grouping level above is used as the denominator in the calculation of occupancy. |
| Occupancy rate (with [unified agent status synchronization](https://support.zendesk.com/hc/en-us/articles/10114746509978)) | Occupancy rate helps you to understand how much of an agent's time is spent on support-related activities versus non-support activities within their paid time. Industry-standard is 75-85%. Note: This calculation applies only to customers with [unified agent status synchronization](https://support.zendesk.com/hc/en-us/articles/10114746509978). | (Ticket time + Productive status time) / (Ticket time + Idle time - Unpaid status time) If you use [activity type as an attribute](https://support.zendesk.com/hc/en-us/articles/6443331692698#topic_tmj_khs_3fc) to group your report, the total of the grouping level above is used as the denominator in the calculation of occupancy. |
| Overtime (duration) | Total recorded time outside of the scheduled hours for occurrences identified within the selected date range. | Sum of time of clock-outs that occur outside of scheduled hours |
| Overtime (occurrences) | Count of occurrences where time is recorded outside of scheduled hours. An agent can have multiple shifts in a day, so this may happen more than once. | Count of clock-outs outside of scheduled hours |
| Scheduled time | Total amount of time the agent was scheduled to work within the requested timeframe. Schedules have to be published to be counted. | N/A |
| Total time | Total amount of time the agent was logged in within the time frame requested. Includes time in all activities, general tasks, and untracked time. | N/A |
| Unpaid general task or status (duration) | Sum time an agent tracked in a [general task](https://support.zendesk.com/hc/en-us/articles/6443329426330) or [unified agent status](https://support.zendesk.com/hc/en-us/articles/10114746509978) where the option to log as paid time is turned off under Occupancy settings. | N/A |

## Time off report metrics

The Time off report metrics include:

- [Approved (duration)](#topic_xwv_3n4_52c__approved_duration)
- [Approved (occurrences)](#topic_xwv_3n4_52c__approved_occurrences)
- [Planned time off(duration)](#topic_xwv_3n4_52c__planned_duration)
- [Planned time off (occurrences)](#topic_xwv_3n4_52c__planned_occurrences)
- [Unplanned time off (duration)](#topic_xwv_3n4_52c__unplanned_duration)
- [Unplanned time off (occurrences)](#topic_xwv_3n4_52c__unplanned_occurrences)

| Metric | Description | Formula |
| --- | --- | --- |
| Approved (duration) | Sum of time of approved, planned, and unplanned time off (occurrences). | N/A |
| Approved (occurrences) | Count of occurrences, of approved planned, and unplanned occurrences. | N/A |
| Planned time off (duration) | This comes from the time off request reason, specifically, the planned type. | Sum of time of planned occurrences for the requested time frame |
| Planned time off (occurrences) | This comes from the time off request reason, specifically, the planned type. | Count of planned occurrences for the requested time frame |
| Unplanned time off (duration) | This comes from the time off request reason, specifically, the unplanned type. | Sum of time of unplanned occurrences for the requested time frame |
| Unplanned time off (occurrences) | This comes from the time off request reason, specifically, the unplanned type. | Count of unplanned occurrences for the requested time frame |