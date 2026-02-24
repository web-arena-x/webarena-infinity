# About workforce management automations

Source: https://support.zendesk.com/hc/en-us/articles/6443314435610-About-workforce-management-automations

---

Zendesk Workforce management (WFM) automations are designed to streamline repetitive tasks. Automations allow you to manage certain agent activities automatically, such as ending agents' days when they forget to clock out.

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | Workforce Management (WFM) or Workforce Engagement Management (WEM) |

Verified AI summary ◀▼

Workforce management automations help you manage agent activities automatically, reducing manual tasks like correcting timesheets. Set conditions for actions such as clocking out agents or sending notifications. Automations activate based on events, tasks, and durations you define, applying to all or specific agents. Note that these automations work only on activities occurring after setup, not retroactively.

Zendesk Workforce management (WFM) automations are designed to streamline repetitive tasks. Automations allow you to manage certain agent activities automatically, such as ending agents' days when they forget to clock out.

Similar to Zendesk automations, WFM automations perform an action when the conditions you define are met. Automations can reduce your manual workload and increase efficiency and accuracy.

This article contains the following sections:

- [About WFM automations](#h_01HD2JVQ6XBTRWGAMMN3QGTB9F)
- [Structure of a WFM automation](#structure-of-wfm-automations)
- [How WFM automations work](#how-wfm-automations-work)

Related articles

- [Creating workforce management automations to manage agent activity](https://support.zendesk.com/hc/en-us/articles/6443374423066)

## About WFM automations

Similar to Zendesk automations, WFM automations perform actions when the conditions you define are met. WFM automations are focused on managing agent activity.

Some examples of automation uses include:

- Correcting recorded time if agents forget to clock out for the day.
- Moving agents from a task or workstream to a general task or untracked time.
- Ending the workday for agents who forget to clock out.
- Sending a notification message.

Note: When the [unified agents status synchronization](https://support.zendesk.com/hc/en-us/articles/10114746509978)
is turned on, the only actions that automations can perform are to clock out users, delete timesheets, end the day, and send a message.

By setting up automations, managers are freed up from performing the repetitive tasks related to correcting agent timesheets.

### Structure of a WFM automation

WFM automations have a set structure. You can think of the structure as an *if statement.* For example:

`If an agent is [Clocked in] to [task] for over [20m] then [clock out agent]`

The structure of a WFM automation consists of:

- A *Run event*, that determines when the automation activates. The default event is *Clocked into*, but it can be changed to *Early to* or *Late to*.

 The Clocked into event means that the automation will run after a specified duration since an agent clocks into a task, status, or workstream. These automations can be used, for example, to notify managers when agents have been working on a task for too long, such as handling calls for over two hours, and switch agents to a different task, such as following up on pending tickets or participating in training activities.

 The Early and Late to events consider the agent’s adherence to their scheduled start and end times. The Early to event runs on a specified duration before an agent’s scheduled start or end time. The Late to event runs after a specified duration beyond an agent’s scheduled start or end time.

 These automations can be used, for example, to remind agents that they have clocked in earlier than expected, or to prompt them to clock out if they are working beyond their scheduled shift, such as when handling extended customer calls. They can also be used by managers to promote adherence to labor policies by preventing unauthorized overtime and undertime, while improving agent compliance through automated corrective actions.
- One or more *tasks* (this can be any of your workstreams, unified agent statuses, or general tasks), or a condition (End day or Start day) that the event is related to.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_automation_create.png)
- A set *duration*. This measures how long the agent must be clocked into a task, unified agent status, or workstream for the automation to run. The Early to event runs on the specified duration before an agent’s scheduled start or end time. The Late to event runs after a specified duration beyond an agent’s scheduled start or end time.
- The *actions* that the automation will perform. Choose from the following predefined actions:
 - Clock out user, Delete timesheet (this involves removing the agent's activity from both the [agent activity page](https://support.zendesk.com/hc/en-us/articles/6443347506970) and related reports), [End day](../../agent-guide/schedule-management-and-time-tracking-wfm-add-on/starting-and-ending-your-day-in-the-zendesk-wfm-time-tracker.md#ending_your_day)
 - Clock out user, [End day](../../agent-guide/schedule-management-and-time-tracking-wfm-add-on/starting-and-ending-your-day-in-the-zendesk-wfm-time-tracker.md#ending_your_day)
 - Send a message. The users you select will receive a push notification in their [Agent Workspace](https://support.zendesk.com/hc/en-us/articles/4408821259930) in Zendesk Support.
 - Shift user to general task

    Note: This action is not available when the [unified agents status synchronization](https://support.zendesk.com/hc/en-us/articles/10114746509978) is turned on on your account.
 - Shift user to untracked time

    Note: This action is not available when the [unified agents status synchronization](https://support.zendesk.com/hc/en-us/articles/10114746509978) is turned on on your account.
- A list of *agents* that the automation applies to. Automations can apply to all agents in an account or only specified agents.

### How WFM automations work

Similar to Zendesk automations, WFM automations execute actions when defined conditions are met. The conditions for a WFM automation consist of the specified event that runs the automation, a task, and a duration of time.

When these conditions are met, the corresponding action is performed for the designated agents.

Note: Automations don't run retroactively. Actions are performed for agent activities that occur after the automation is created. Additionally, the Clocked into event automations run for new tickets only after they're saved for the first time.