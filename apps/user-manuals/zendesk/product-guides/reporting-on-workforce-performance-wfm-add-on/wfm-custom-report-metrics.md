# WFM custom report metrics

Source: https://support.zendesk.com/hc/en-us/articles/6443376913818-WFM-custom-report-metrics

---

This article lists the metrics available for Zendesk Workforce management (WFM) custom reports.

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | Workforce Management (WFM) or Workforce Engagement Management (WEM) |

Verified AI summary ◀▼

This article outlines metrics for Workforce Management custom reports, helping you track and analyze agent performance. It covers point metrics like assigned and solved points, and rate and time metrics such as adherence rate and average handle time. Use these metrics to monitor productivity, adherence, and ticket handling efficiency, enabling data-driven decisions to enhance your team's customer support operations.

This article lists the metrics available for Zendesk Workforce management (WFM) custom
reports.

This article contains the following topics:

- [Point metrics](#topic_ocb_3n4_52c)
- [Rate and time metrics](#topic_xwv_3n4_52c)

Related articles

- [About custom WFM report templates](https://support.zendesk.com/hc/en-us/articles/6443331692698)
- [WFM system report metrics](https://support.zendesk.com/hc/en-us/articles/6443331680538)

## Point metrics

Point metrics include:

- [Assigned
  points](#topic_ocb_3n4_52c__assigned_point)
- [Attended
  points](#topic_ocb_3n4_52c__attended_point)
- [Escalated
  points](#topic_ocb_3n4_52c__escalated_point)
- [Handled points](#topic_ocb_3n4_52c__handled_point)
- [Private
  comments](#topic_ocb_3n4_52c__private_comment)
- [Public
  comments](#topic_ocb_3n4_52c__public_comments)
- [Reopened
  points](#topic_ocb_3n4_52c__reopened_point)
- [Solved points](#topic_ocb_3n4_52c__solved_point)
- [Ticket bounce
  points](#topic_ocb_3n4_52c__bounced_points)

| Metric | Description | Formula |
| --- | --- | --- |
| Assigned points | Assigned points represent the total number of tickets assigned to an agent. An agent receives an assigned point when:   - They assign the ticket to themselves - Another user assigns the ticket to the agent - An automation assigns the ticket to the agent  The agent can receive only one point per ticket. | N/A |
| Attended points | An agent receives an attended point for performing any of the following actions:   - Changing the status of a ticket - Leaving a public comment or an internal note - Reassigning the ticket to themselves - Reassigning the ticket to another agent in the same group   An agent does not receive multiple points for a single audit.  For example, if they leave a comment, change the status, add a tag, and then click submit, they only receive one attended point. However, if they leave a comment, click submit, and then return to the ticket, change the status, and click submit again, they receive a total of two attended points.  Additionally, an attended point is also given to agents who solve or escalate a ticket. They receive a solved point and an attended point respectively. | N/A |
| Escalated points | An escalated point is attributed to an agent when:  - They assign a ticket, previously assigned to them, to a different   group.  An escalated point is not given to an agent when:  - The agent assigns the ticket to themselves in a different group. - The agent has already received an escalated or solved point for that   ticket. | N/A |
| Handled points | Unique count of ticket IDs that an agent worked on. An agent is given a point if:  - The agent updated a ticket by performing any of these actions:   - Adding a public comment   - Adding an internal note   - Assigning the ticket to another group   - Assigning the ticket to another agent or to themselves in another     group   - Changing the ticket status - The agent has not received a handled point for that same Ticket ID within   the last 12 hours. | N/A |
| Private comments | Tracks how many internal notes have been left inside of a ticket. Each internal note an *agent* leaves in the ticket is counted as one private comment. | N/A |
| Public comments | Tracks how many public comments have been sent. Each public comment an agent sends is counted as one public comment. | N/A |
| Reopened points | An agent receives a reopened point every time a ticket changes from solved to open. A reopened point is counted for the agent who previously changed the ticket to solved. | N/A |
| Solved points | A solved point is given to an agent who solves a ticket. The first time a ticket is solved by an agent, the agent solving it receives one solved point. Solved points are counted once per ticket for each agent. | N/A |
| Ticket bounce points | Number of points where the agent recorded time spent on a ticket but no work was actually done. If tickets are updated using bulk editing, it may lead to a higher number of attended tickets compared to touched tickets (where agents actually clocked in). This discrepancy can result in negative bounced points. | (Number of tickets touched - Attended points) |

## Rate and time metrics

Rate and time metrics include:

- [Adherence
  rate](#topic_xwv_3n4_52c__adherence_rate)
- [Average handle time](#topic_xwv_3n4_52c__a_h_t)
- [First response time](#topic_xwv_3n4_52c__f_r_t)
- [First response
  time after assignment](#topic_xwv_3n4_52c__f_r_t_after_assignment)
- [In adherence
  time](#topic_xwv_3n4_52c__in_adherence_time)
- [Number of tickets
  touched](#topic_xwv_3n4_52c__tickets_touched)
- [Number of
  unique tickets with time spent](#topic_xwv_3n4_52c__unique_tiquets_with_time_spent)
- [Out of adherence
  time](#topic_xwv_3n4_52c__out_of_adherence)
- [Paid time](#topic_xwv_3n4_52c__paid_time)
- [Paid general task
  or status time](#topic_xwv_3n4_52c__paid_general_task_time)
- [Productive
  general task or status time](#topic_xwv_3n4_52c__productive_general_task_time)
- [Productive
  time](#topic_xwv_3n4_52c__productive_time)
- [Resolution
  rate](#topic_xwv_3n4_52c__resolution_rate)
- [Solved points per
  paid hour](#topic_xwv_3n4_52c__solved_points_per_hour)
- [Solved
  points per productive hour](#topic_xwv_3n4_52c__solved_points_per_productive_hour)
- [Ticket bounce
  rate](#topic_xwv_3n4_52c__bounce_rate)
- [Ticket solved
  rate](#topic_xwv_3n4_52c__solved_rate)
- [Ticket time](#topic_xwv_3n4_52c__ticket_time)
- [Unproductive
  time](#topic_xwv_3n4_52c__unproductive_time)
- [Unproductive general
  task or status time](#topic_xwv_3n4_52c__entry_nbl_cvt_nfc)
- [Unpaid general
  task or status time](#topic_xwv_3n4_52c__unpaid_general_task_time)
- [Untracked
  time](#topic_xwv_3n4_52c__untracked_time)
- [Utilization](#topic_xwv_3n4_52c__utilization)
- [Utilization (with
  unified agents status synchronization)](#topic_xwv_3n4_52c__utilization_ocr)

| Metric | Description | Formula |
| --- | --- | --- |
| Adherence rate | Percentage of time the agent activities complied with the schedule. | (Time in adherence / Total scheduled time) x 100 |
| Average handle time (AHT) | Represents the average amount of time an agent spends on each ticket they worked on. AHT doesn't include new tickets created by the agent. | Total ticket time / Number of unique tickets with time spent |
| First response time (FRT) | The first response time (FRT) measures the duration between a ticket's creation and the first public reply from an agent. Note that live chat interactions do not count as public comments and will not trigger the FRT count. If you group the data by attributes other than Ticket ID or select a date range, you get an average first response time | Time of first public reply - Time ticket is created |
| First response time after assignment | The time it takes for an agent to send a public comment after a ticket is assigned to them.  Note that live chat or message interactions don't count as public comments and won't trigger the FRT count. | N/A |
| In adherence time | Adherence time refers to the duration an agent is in adherence.  Agents are considered in adherence when they are clocked into a general task, unified agent status, or workstream for which they are scheduled. | N/A |
| Number of tickets touched | A count of all tickets where there's ticket time recorded. This is agent activity-based and is unrelated to ticket data. | N/A |
| Number of unique tickets with time spent | Count of tickets where there's ticket time recorded for an agent. Each unique ticket is counted only once per agent.  If there are two agents on the same team and those two agents spend time on the same ticket, each has a value of one unique ticket. At the team level it has a value of one because it’s only one unique ticket. | N/A |
| Out of adherence time | Duration of time the agent was out of adherence. If the agent is working on a general task, unified status, ticket, or a workstream that isn’t in their schedule, the agent is considered out of adherence. | N/A |
| Paid time | Total time the agent tracked excluding any unpaid general task or status time, for example, lunch. These are [general tasks](https://support.zendesk.com/hc/en-us/articles/6443329426330) and [unified agent statuses](https://support.zendesk.com/hc/en-us/articles/10114746509978) that have the option to log this general task or status as paid time turned off under Occupancy settings. | Total time - Unpaid general task or status time |
| Paid general task or status time | Sum time an agent tracked in a [general task](https://support.zendesk.com/hc/en-us/articles/6443329426330) or [unified agent status](https://support.zendesk.com/hc/en-us/articles/10114746509978) where the option to log this general task or status as paid time is turned on under Occupancy settings. | N/A |
| Productive general task or status time | Sum time an agent tracked in a [general task](https://support.zendesk.com/hc/en-us/articles/6443329426330) or [unified agent status](https://support.zendesk.com/hc/en-us/articles/10114746509978) where the option to log this general task or status as productive time is turned on under Occupancy settings. | N/A |
| Productive time | Total time an agent is actively clocked in a productive state. This includes all ticket time as well as any [general task](https://support.zendesk.com/hc/en-us/articles/6443329426330) or [unified agent statuses](https://support.zendesk.com/hc/en-us/articles/10114746509978) where the option to log this general task or status as productive time is turned on under Occupancy settings. All productive time is included in paid time. | Ticket time (including new ticket time) + All productive general task or status time. |
| Resolution rate | Percentage of tickets assigned to an agent compared to the number of tickets they solve. | (Solved ticket count / Assigned points) x 100 |
| Solved points per paid hour | Number of tickets an agent solved on average for each paid hour the agent tracked. Paid time = Ticket time + Paid general task or status time + Untracked time.  This metric calculates results on a per-hour basis, even if smaller intervals are selected for display. | Solved points / Paid time |
| Solved points per productive hour | Number of tickets an agent solved on average for each productive hour the agent tracked. | Solved points / Productive time |
| Ticket bounce rate | Percentage of tickets the agent recorded time in that were not worked on.  If the tickets are updated using bulk editing, it might result in a higher number of attended tickets than touched tickets (tickets where agents actually clocked in). The percentage can't be below 0% or above 100%. | (Number of tickets touched - Attended points) / Number of tickets touched x 100 |
| Ticket solved rate | Ratio of tickets solved compared to tickets handled. This helps provide a clear picture of agent effectiveness and customer issue resolution speed. | (Solved points / Handled points) x 100 |
| Ticket time | Sum of time an agent tracked in a ticket or new ticket time. | N/A |
| Unpaid general task or status time | Sum of time an agent is tracked in a [general task](https://support.zendesk.com/hc/en-us/articles/6443329426330) or [unified agent status](https://support.zendesk.com/hc/en-us/articles/10114746509978) that has the option to log as paid time turned off under Occupancy settings. | N/A |
| Unproductive time | Total time an agent is tracked in an unproductive state. This includes the [general tasks](https://support.zendesk.com/hc/en-us/articles/6443329426330) or [unified agent statuses](https://support.zendesk.com/hc/en-us/articles/10114746509978) where the option to log as productive time is turned off under Occupancy settings. | Unproductive general task time or status time + Untracked time |
| Unproductive general task or status time | Sum of time an agent tracked in [general tasks](https://support.zendesk.com/hc/en-us/articles/6443329426330) or [unified agent statuses](https://support.zendesk.com/hc/en-us/articles/10114746509978) where the option to log as productive time is turned off under Occupancy settings. | N/A |
| Untracked time | Sum of time an agent tracked while not in a general task or other activities such as tickets, chats, and voice. | N/A |
| Utilization rate | Percentage of paid agent time in which agents are actually logged in and assisting or available to assist customers. | Ticket time + Productive general task time + Untracked time) / (Total time - Unpaid general task time  If you use [activity type as an attribute](https://support.zendesk.com/hc/en-us/articles/6443331692698#topic_tmj_khs_3fc) to group your report, the total of the grouping level above is used as the denominator in the calculation of occupancy. |
| Utilization (with [unified agent status synchronization](https://support.zendesk.com/hc/en-us/articles/10114746509978)) | Percentage of paid agent time in which agents are actually logged in and assisting or available to assist customers.  Note: This calculation applies only to customers who have activated the [unified agent status integration with Zendesk WFM](https://support.zendesk.com/hc/en-us/articles/10114746509978). | Ticket time + Idle time - Unpaid status time) / (Total time - Unpaid status time)  If you use [activity type as an attribute](https://support.zendesk.com/hc/en-us/articles/6443331692698#topic_tmj_khs_3fc) to group your report, the total of the grouping level above is used as the denominator in the calculation of occupancy. |