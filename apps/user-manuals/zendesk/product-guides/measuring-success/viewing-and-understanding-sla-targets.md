# Viewing and understanding SLA targets

Source: https://support.zendesk.com/hc/en-us/articles/4408832852122-Viewing-and-understanding-SLA-targets

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Professional or Enterprise |

[A service level agreement (SLA)](https://support.zendesk.com/hc/en-us/articles/5600997516058) is a policy you define that specifies and measures the response and resolution times that your support team delivers to your customers.

On Enterprise plans, you can define group SLAs. Group SLAs are separate agreements between your internal teams that define a target ownership time for a group.

You can use the SLA and group SLA information that are visible in views and tickets to prioritize the tickets you address.

For more information about setting up SLA policies, see [Defining SLA policies](https://support.zendesk.com/hc/en-us/articles/4408829459866) and [Defining group SLA policies for internal teams](https://support.zendesk.com/hc/en-us/articles/5322445643802).

This article contains the following sections:

- [Understanding SLA target statuses](#topic_g5y_1jw_rr)
- [Seeing SLA statuses in views](#topic_opl_mhw_rr)
- [Seeing SLA statuses in tickets](#topic_wqq_n3w_rr)
- [Viewing which SLA policies have been applied to a ticket](#topic_rct_l2w_tr)

## Understanding SLA target statuses

Similar to ticket statuses, SLA targets have different statuses on a ticket.

- **Active**: An active SLA target is one whose metric has not yet been completed.
 For example, if the metric is "First Reply Time" and there has been no first public reply on a ticket, the "First Reply Time" target is still active on that ticket.
- **Paused**: A paused SLA target is one whose metric has not yet been completed, but we’ve temporarily paused the clock. A target can get into this state if its metric definition excludes certain statuses, like Requester Wait Time. When a ticket is put into pending, the Requester Wait Time target will be paused.
- **Closed**: A closed SLA target is one whose metric has been completed. For example, a ticket that’s already received a public reply will have a closed target for the “First Reply Time” metric.
- **Active (breached), Paused (breached), and Closed (breached)**: There are also breached variants of each of these three states. Any given SLA target can be both active and breached, or paused and breached, or closed and breached. This just means that in addition to the definition above, the metric has surpassed the target time assigned to that ticket.

## Seeing SLA statuses in views

You can view the SLA target status in the **SLA** and **Group SLA** view columns.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/support_ticket_view_SLA_badges_updated.png)

The color of the SLA badge tells you how much time is left before the SLA is breached:

- **Green**: Greater than 15 minutes
- **Amber**: Fewer than 15 minutes
- **Red**: 0 minutes (the SLA has been breached)

SLA badges round to the nearest minute, hour, or day, with the exact halfway point rounding down. For example, if an SLA target is 1:30:00, it will round down to a 90m badge. If the SLA target is 1:31:00, it will round up to the 2h badge. Similarly, if the target is 36:30:00, it's rounded down to a 36h badge. If the target is 36:31:00, it's rounded up to a 2d badge.

If a ticket does not have an SLA policy applied or if all of the targets on that ticket are closed, the **SLA** value will be blank for that ticket.

If at least one target on the ticket is active, the calendar time remaining before that target is breached appears. Once the target has been breached, a negative time value, like -15m or 4h, appears in red.

If the next target is paused, a pause icon will appear in the **SLA** column. For targets that haven't been breached yet, a green pause icon appears. For targets that have already been breached, the pause icon appears in red.

If a ticket has multiple active SLA targets, the soonest expiring target displays. This includes targets that have already been breached.

If your view contains the **SLA** or **Group SLA** columns, SLA and group SLA information will appear in the ticket preview when you hover over the ticket in the view.
This information won't appear if your view doesn't contain the **SLA** or **Group SLA** column.

If an SLA is applied to a ticket well after it is created, it uses the ticket's metrics to calculate its targets, rather than starting from the time it is applied. For example: A ticket is submitted at 9 AM. At 12 PM, an SLA is created and applied to that ticket, with a First Reply Time requirement set for 1h. That SLA will immediately appear as breached when the SLA policy is applied at 12 PM because SLAs can't put events in the past.
However, the breach time itself starts counting from when the SLA policy is applied. In this example, the breach time starts from 12 PM and continues until the ticket is replied to.

## Seeing SLA statuses in tickets

When you start using SLAs, SLA information will automatically start appearing on any ticket where an SLA policy has been applied. Group SLAs are identified with a “Group Ownership Time” label and display which group the SLA is applied to.

The next action that needs to be taken by the agent will appear in each ticket along with the amount of calendar time that is left before the target will breach.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/SLA_group_ticket.png)

**To view more information about the SLA target**

Hover over the SLA badge to see other active SLA targets for the ticket and the exact date and time when the target will be breached. When the SLA policy is fulfilled, the badge disappears.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/SLA_group_ticket_badge.png)

The SLA badge will always show the hours until the targets are due in calendar hours and days, but the target due date will be based on the hours as defined in your SLA policies and business hours. This means that SLA targets set with business hours can carry over to the following business day depending on the target set and what time of day the ticket was created.

For example, a ticket may have a target of eight business hours, but because it's a Friday afternoon, the target rolls over to Monday morning and the badge will show three days. This is because SLA badges are designed to help agents prioritize their workflows in real time.
It's important to get all the badges on the same scale in a way that agents can easily understand.

## Viewing which SLA policies have been applied to a ticket

You can see which SLA policy and corresponding targets have been applied to a given ticket by checking the ticket's events (see [Viewing all events of a ticket](https://support.zendesk.com/hc/en-us/articles/4408829602970-Viewing-all-events-of-a-ticket)).

Each time a policy or target is applied, removed, or changed, an event will appear.
However, no event appears when an SLA is breached or fulfilled.