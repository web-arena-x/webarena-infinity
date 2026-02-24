# About WFM general tasks

Source: https://support.zendesk.com/hc/en-us/articles/7069811858586-About-WFM-general-tasks

---

Zendesk Workforce management (WFM) general tasks are tasks that admins set up to track agent activities or tasks that take place outside of Zendesk. They’re used to track agents’ non-ticketing work, which helps admins and managers to fully understand how agents' time is spent.

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | Workforce Management (WFM) or Workforce Engagement Management (WEM) |

Verified AI summary ◀▼

Workforce Management (WFM) general tasks help you track agents' non-ticketing activities like meetings and breaks. Admins can customize these tasks to monitor paid or productive time, aiding in occupancy rate calculations. Managers can view these tasks in agent activity reports, while agents can clock in to tasks via the time tracker, affecting their availability status.

Note: When the [unified agents status synchronization](https://support.zendesk.com/hc/en-us/articles/10114746509978) is turned on,
you must [map your unified agent statuses](https://support.zendesk.com/hc/en-us/articles/10117789027610) instead of general
tasks.

Zendesk Workforce management (WFM) general tasks are tasks that admins set up to track agent
activities or tasks that take place outside of Zendesk. They’re used to track agents’
non-ticketing work, which helps admins and managers to fully understand how agents' time is
spent.

For example, general tasks may include necessary activities such as meetings or
breaks.

This article contains the following topics:

- [Understanding WFM general
  tasks](#topic_kcp_yv1_cbc)
- [Understanding how team members
  interact with general tasks](#topic_tlt_pw1_cbc)

Related articles

- [Setting up WFM general tasks for non-ticketing
  work](https://support.zendesk.com/hc/en-us/articles/6443329426330)

## Understanding WFM general tasks

WFM general tasks are used to track agents’ time spent on necessary, non-ticketing work or
activities. Sometimes known as [AUX codes](https://cxcentral.com.au/glossary/auxiliary-codes/#:~:text=Glossary%20Auxiliary%20Codes-,Auxiliary%20Codes,employee%20isn't%20being%20productive.) or [AUX states](https://www.callcentrehelper.com/auxiliary-work-state-90793.htm) in a call center, they help you understand how much of
your agents’ time is spent on support-related activity and can be used in calculating your
[occupancy rate](https://support.zendesk.com/hc/en-us/articles/6443376913818#Occupancy%20Rate).

Admins can define and customize the general tasks available in your organization. For
example, some common general tasks are breaks, meetings, and training.

When defining general tasks, admins can determine if the general task is available to all
the teams in your organization or restrict certain general tasks to specific teams.

### About paid time and productive time general task settings

Admins can define if the general task is counted as [paid time](https://support.zendesk.com/hc/en-us/articles/6443376913818#Paid%20Time) or [productive time](https://support.zendesk.com/hc/en-us/articles/6443376913818#Productive%20Time). If the general task is counted as
paid or productive time, it’s included when calculating your occupancy rate.

For example, you may want to define a “lunch” general task as unpaid time. By
defining it as a general task, you’re still tracking agents’ time.

There are certain scenarios where you’ll want to define general tasks as
productive time. For example, if an agent works on social media management outside of
Zendesk, then you could create a general task for that type of work and track it as
productive time. Note that all productive time tasks are included in paid time.

However, not all general tasks need to be defined as productive time.
Unproductive time is a standard part of customer support work. Activities or tasks such as
attending training or meetings could be considered unproductive time. While they’re
necessary activities, they aren’t the core focus of an agent’s job.

## Understanding how team members interact with general tasks

Depending on a [team member’s role and permissions](https://support.zendesk.com/hc/en-us/articles/6443374440090), how they
interact with general tasks will vary. The following list describes how general tasks can be
used by different, common roles.

- **Admins**: Can define and edit general tasks for the organization. Additionally,
  admins can include general tasks as part of the intraday schedule when creating [locations](https://support.zendesk.com/hc/en-us/articles/6443345205402) for their teams.
- **Managers, team leads**: Can view general tasks on the [Agent activity](https://support.zendesk.com/hc/en-us/articles/6443347506970) page, which includes an activity breakdown of
  agents’ paid and unpaid time. General tasks appear in this summary.

  ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_generaltask_paid_unpaid_breakdown.png)

  Team members in these roles can also view this information in
  the [historical Agent activity report](https://support.zendesk.com/hc/en-us/articles/6443363334810#topic_u4j_khr_tzb), as well as
  in any custom reports that use agent activity grouping and metrics. Additionally, if
  the team member is in a role with permission for their [Organization structure](../../getting-started/getting-started-with-zendesk-workforce-management/getting-started-with-zendesk-wfm-admin-guide.md#topic_l4n_wmd_d1c), they can also include
  general tasks in their intraday schedules.
- **Agents**: Agents can view general tasks on their [schedules](https://support.zendesk.com/hc/en-us/articles/6443374353434). They can also [clock in](https://support.zendesk.com/hc/en-us/articles/6443354661402) to general tasks from the WFM time tracker in the top
  navigation bar in Zendesk Support. This will automatically set their availability status
  for voice, as defined by the admin for that general task. See [Setting up WFM general tasks](https://support.zendesk.com/hc/en-us/articles/6443329426330).

  ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_time_tracker_task_manager.png)