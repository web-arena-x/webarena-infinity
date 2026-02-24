# About automations and how they work

Source: https://support.zendesk.com/hc/en-us/articles/4408832701850-About-automations-and-how-they-work

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Admin Center > Objects and rules > Business rules > Automations

Automations are similar to triggers because both define conditions and actions that modify ticket properties and optionally send email notifications to customers and agents. Where they differ is that automations execute when an event occurs after a ticket property was set or updated, rather than immediately after a ticket is created or updated.

All automations *run* once every hour on all non-closed tickets. They execute, or *fire*, on all tickets where conditions are met.

Topics covered in this article:

- [Essential facts for automations](#topic_ft5_n3z_sm)
- [Examples for using automations](#topic_jc5_qvn_fm)
- [Ensuring your automation only runs once](#topic_mbl_q4f_tm)
- [Understanding when automations run](#topic_h3z_svn_fm)
- [Understanding when automation actions fire](#topic_fys_1gz_jm)

For information about creating and managing automations, see [Creating and managing automations for time-based events](https://support.zendesk.com/hc/en-us/articles/4408883801626) . For a list of standard automations, see [About the standard Support automations](https://support.zendesk.com/hc/en-us/articles/4408835051546).

## Essential facts for automations

The Automations page in Admin Center is used to create, edit, and manage your automations. It's broken down into two tabs based on the automations' status: active and inactive.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/automations_list.png)

We've distilled some essential facts for you about automations. These are explained in greater detail in this article.

- Automations are time-based; they take action when a time-event occurs, not immediately after a ticket is created or updated.
- Automations run every hour, but not necessarily top-of-the-hour; they will start *at some point* during the hour.
- Automations can fire on a maximum of 1,000 tickets per hour.
- Automations do not run or fire on closed tickets.
- Each ticket can be updated a maximum of 100 times by automations.
- An automation must contain a condition that is true only once or an action that nullifies at least one of the conditions.
- All active automations must be unique. They can have some overlapping conditions, but they can't be identical.
- Automations, like all business rules, must be smaller than 65kb.
- You can have a maximum of 500 active automations at a time.
- On non-Enterprise plans, automations are visible to agents, including light agents and contributors, but can only be edited by admins. On Enterprise plans, automations are visible only to [agents in custom roles with permission](https://support.zendesk.com/hc/en-us/articles/4408882153882) to manage automations.

## Examples for using automations

Automations help you manage your workflow and, potentially, improve performance and customer satisfaction by alerting you to tickets that remain unresolved and need to be escalated (for example).

Here are some uses for automations:

- Notifying agents when an assigned ticket remains unresolved for x number of hours
- Notifying agent groups when a new ticket remains unassigned for x number of hours
- Notifying the assigned agent after x number of hours when a pending ticket has been updated by the requester
- Closing tickets x number of days after they have been set to solved
- Finding "abandoned" tickets that haven't been updated for a certain number of days
- Sending an SMS text message when an urgent ticket has been unattended for more than 48 hours (using a target with an automation; see [Using targets in automations and triggers](https://support.zendesk.com/hc/en-us/articles/4408883282458#topic_cjz_eqa_vb))

Zendesk provides an automation that demonstrates one of these common uses:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/automation_conditions_96hrs2.png)

This automation closes tickets 96 hours after they have been solved (96 hours is a support best practice for the minimum amount of time a ticket should remain in the solved state before it is closed). When the automation runs, any tickets that meet these criteria are closed. The close action looks like this:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/automation_actions_96hrs2.png)

Once a ticket is closed, it can't be modified anymore and automations no longer affect it.

This example also illustrates an important rule of automations: ***an automation must contain an action that cancels a condition***. The ‘Status equals Solved’ condition is canceled by the ‘Status equals Closed’ action. If there were no canceling action, the automation would continue to fire in an endless loop because the status would remain solved (not closed) and continue to meet the condition criteria.

## Ensuring your automation only runs once

Automations check every hour to see if their conditions are met. So an automation must include one of the following:

- an action that nullifies at least one of the conditions, or
- a condition than can be true only once

If there is no nullifying action or true-only-once condition, the unmodified conditions will continue to be met and the automation will continue to fire in an endless loop.

An example of a condition that is commonly nullified is a "ticket priority" condition. A ticket priority condition is usually paired with a "hours since created" condition. For example, if the ticket priority is Normal (Ticket: Priority > Is > Normal), the condition is nullified by including an action that changes the priority to High (Ticket: Priority > High) or some other priority.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/automation_close_after_4days.png)

An example of a condition that can only be true once is the "hours since open is" condition. This condition doesn't require a nullifying action. For example, if the hours since the ticket is open is 4 hours (Ticket: Hours since created > Is > 4), then the condition will only be true on one check. On the next check, the hours since open will be 5, and the condition will be false.

However, it’s important to be thoughtful when using an “hours since...is” condition. Because of the slight variation of run times for automations in any given hour, it's unlikely but possible for an “is” condition to never evaluate to true. This situation is more likely for larger accounts, or accounts with many automations. For details, see [Using the “Hours since” condition in automations](using-the-hours-since-condition-in-automations.md#topic_ld3_5d1_tqb).

An easy way to cancel a condition is to add a tag. The automation would check for a tag and, if *not* present, the automation would add the tag to the ticket and perform any actions (such as, sending a notification). If the tag *is* present on the ticket, the automation will not perform the action again.

## Understanding when automations run

All automations *run* once every hour on non-closed tickets to see if conditions are met. They execute, or *fire*, on tickets where conditions are met.

Note: Tickets that are not closed but have had more than 100 automation audits occur during the life of the ticket are excluded from the hourly automations run. To view events for a ticket, see [Viewing a ticket's audit trail](https://support.zendesk.com/hc/en-us/articles/4408829602970).

Your automations run every hour, but that does not necessarily mean top-of-the-hour. Your automations will start running *at some point* during the hour, maybe five minutes after the hour or thirty-eight minutes after the hour, for example.

The entire time it takes your automations to run and execute depends on how many automations and tickets there are to process. Automations run again at some point during the subsequent hour.

Each automation can act on a maximum of 1,000 tickets each hour. If there are more than 1,000 tickets where conditions are met for an automation, 1,000 tickets will be processed in that hour, and the remaining tickets will be processed during the next hour, if conditions are still met, or the hour after that, until all tickets are checked. On jobs that are very large it may take many hours to work through all of the tickets that meet the conditions of that automation.

An extended automation cycle increases the chances for agents to be making routine ticket updates at the same time as automations are running. To prevent ticket update collisions, Zendesk automations double-check the state of the ticket at the time of the update, instead of just acting based on the state of the ticket when the automation cycle started.

To prevent unnecessary activity, automations do not run on accounts that haven't had anyone sign in within the last 14 days.

## Understanding when automation actions fire

Automations run in order every hour and fire on tickets where conditions are met. Each automation fires—that is, takes action on a ticket—when the automation runs and conditions are met. That means the ticket is being updated each time an automation fires during the cycle, so not all automations see the ticket in the same state. The actions of one automation *can* affect another automation in the same hour.

Consider you have three automations:

- Automation #1: If status is Pending greater than 48 hours, notify Assignee.
- Automation #2: If status is Pending greater than 48 hours, change priority to High.
- Automation #3: If priority is High, notify Escalation group.

Automations run and fire (if conditions are met) in order. So, if you have a ticket that has been pending for 48 hours, when automations run in the 49th hour, Automation #1 runs and fires, then #2 runs and fires. After Automation #2 fires, the ticket is updated to High priority. This means that when Automation #3 runs, the condition is met, so Automation #3 will fire.

As mentioned previously, automations, unlike triggers, do not execute an action immediately after a ticket satisfies the conditions. And automations do not execute exactly one hour after conditions are met. For automations, ticket updates depend on when your automations run each hour.

- **Let's consider an example where the action will happen when the automation runs.** Suppose a ticket update at 10:15am satisfies the conditions for an automation to send an email notification. If your automations run at 11:10, then the notification will not be sent until 55 minutes after the conditions are met. If your automations, however, run at 10:20, then the notification will be sent 5 minutes after the conditions are met.

- **Let's look at example with a time-based "Hours since" condition.** Time-based conditions have to be satisfied within a window of time or after a minimum amount of time has passed. The first time an automation runs after an event occurs counts as "zero" hours since that event happened (because it's less than one whole hour). Suppose you have an automation that performs an action two hours after a ticket is solved and a ticket is solved at 9:15am. Here's what will happen:
  1. If your automations run at 10:10am, the ticket has been solved for only 55 minutes and the automation will not fire.
  2. Automations run again at 11:10am, the ticket has been solved 1 hour and 55 minutes, which the automation counts as one hour (because it is less than two hours).
  3. Automations run again at 12:10pm, the ticket has been solved 2 hours and 55 minutes, which the automation counts as two hours. This means the condition is met and the automation will fire and update the ticket.

Note: You can see when an automation fired for a ticket by viewing the events for that ticket. For more information, see [Viewing a ticket's audit trail](https://support.zendesk.com/hc/en-us/articles/4408829602970).