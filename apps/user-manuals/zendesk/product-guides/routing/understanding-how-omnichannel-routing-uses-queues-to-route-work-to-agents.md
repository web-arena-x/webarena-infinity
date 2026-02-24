# Understanding how omnichannel routing uses queues to route work to agents

Source: https://support.zendesk.com/hc/en-us/articles/6712096584090-Understanding-how-omnichannel-routing-uses-queues-to-route-work-to-agents

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Professional or Enterprise |

Omnichannel routing assigns new and open tickets from [email (including web form, side conversations, and
API)](https://support.zendesk.com/hc/en-us/articles/4409149119514#topic_psx_hxk_3yb), calls, and messaging directly to agents based on agent availability and
capacity and, on some plans, can be configured to also factor in service level agreement
(SLA) targets, ticket priority, and skills.

The standard omnichannel routing configuration directs all eligible tickets into a single
queue, assigning work to agents based on the ticket's assigned group. If a single queue
is insufficient for your use case, you can create additional custom omnichannel routing
queues. You must have the [Agent Workspace](https://support.zendesk.com/hc/en-us/articles/4408821259930) to use omnichannel routing.

This article contains the following topics:

- [Essential facts about omnichannel routing queues](#topic_n1k_wsh_j1c)
- [Using custom queues with omnichannel routing](#topic_acc_qf4_j1c)
- [Understanding how omnichannel routing orders tickets within queues](#topic_ns2_rf4_j1c)

## Essential facts about omnichannel routing queues

Using multiple queues can be a valuable aspect of your omnichannel routing
configuration. However, it's important to understand how queues work before
implementing them. Keep the following essential facts about queues in mind:

- The [omnichannel routing configuration](https://support.zendesk.com/hc/en-us/articles/4828787357210)
  settings apply to all of your queues.
- When a new ticket is created, ticket triggers fire first. Then omnichannel
  routing immediately attempts to assign it to an agent. If no agent is
  available to take it, the ticket is added to the appropriate queue.
- There are two types of queues in omnichannel routing:
  - **Standard omnichannel routing queue**: This is the default queue
    used by omnichannel routing when you [turn on omnichannel
    routing](https://support.zendesk.com/hc/en-us/articles/5866925319962) and haven't created custom queues or when tickets
    don't meet the conditions of your custom queues but are otherwise
    eligible to be routed by omnichannel routing. Sometimes this is
    referred to as *group-based omnichannel routing* because
    tickets routed through the standard queue go to agents in the group
    specified in the ticket's group field. The standard queue isn't
    listed on the Queues page in Admin Center.
  - **Custom omnichannel routing queues**: (Professional plans and
    above for Zendesk Suite, Support, Talk, and Chat plans) These are
    custom queues defined by admins. When using custom queues, tickets
    are inserted into the first queue they match the conditions for.
    Custom queues can route tickets to multiple primary and secondary
    groups. If a ticket is routed through a custom queue, omnichannel
    routing ignores the ticket's group field and uses the queue's
    primary and secondary groups.
    - **Subqueues**: (Enterprise plans only) Custom queues can
      be split into up to five subqueues to distribute certain
      percentages of tickets that meet the custom queue's
      conditions to different primary and secondary groups. The
      percentages for subqueues must total 100%. Which subqueue
      any given ticket is inserted into is randomized.
- The auto-routing tag isn't used by custom queues. Regardless of the presence
  of the auto-routing tag, all email tickets, messaging conversations, and
  calls are automatically evaluated for matches to custom queues. However,
  email tickets that don't match any custom queues must have the auto-routing
  tag if you want them to be routed through the standard omnichannel routing
  queue.
- Omnichannel routing matches tickets to queues in the order the queues appear
  on the Queues page. Tickets are added to the first queue they meet the
  conditions for.
- Tickets that don't match the conditions for any of your custom queues are
  inserted into the standard omnichannel routing queue. However, omnichannel
  routing prioritizes all tickets routed through custom queues over those
  routed through the standard omnichannel routing queue, regardless of the
  ticket's priority.
- The way your order tickets, whether by priority and timestamp or time to SLA
  breach, applies to both the standard omnichannel routing queue and custom
  queues.
- When an agent is eligible to receive work from multiple queues, tickets from
  the queue with the higher priority are assigned before tickets from a queue
  with a lower priority. See [Creating custom omnichannel routing
  queues](https://support.zendesk.com/hc/en-us/articles/6716530152858).
- After a ticket has been assigned to an agent, it leaves the queue.
- Call tickets can’t be reassigned by omnichannel routing. Email and messaging
  tickets can be reassigned, but your routing configuration determines whether
  reassignments occur through custom queues or the standard queue.
  - On Team and Growth plans, tickets can't re-enter a custom queue
    after being assigned to an agent. However, if a ticket becomes
    eligible for re-routing, it's inserted into the standard omnichannel
    routing queue based on its routing-eligibility timestamp and routed
    based on the ticket's assigned group.
  - On Professional plans and above, you can configure omnichannel
    routing to [reassign tickets through custom
    queues](https://support.zendesk.com/hc/en-us/articles/4828787357210#topic_g4r_x1z_rcc). When configured, tickets that are reassigned back
    to a group after being assigned to an agent are inserted into the
    first matching queue. If the ticket doesn't meet the conditions for
    any custom queues, it's inserted into the standard omnichannel
    routing queue and routed based on the ticket's assigned group.
- When the [messaging session ends](https://support.zendesk.com/hc/en-us/articles/8009788438042) for a
  messaging ticket, if the ticket's routing channel is *messaging*, it
  isn't eligible to be routed by omnichannel routing. However, if the routing
  channel is changed to *email*, the ticket remains eligible for
  routing.
- You can report on the performance of your custom queues in Explore. See
  [Explore recipe: Reporting on custom
  omnichannel queue performance](https://support.zendesk.com/hc/en-us/articles/7217081202714).

## Using custom queues with omnichannel routing

Omnichannel routing is Zendesk's most sophisticated and complete routing solution. It
provides consistent routing logic across channels and considers many factors when
assigning work to agents. For many use cases, the single, standard omnichannel
routing queue that's activated when you turn on omnichannel routing is sufficient.
When relying on the standard omnichannel routing queue, tickets must be assigned to
a group to be routed to an agent with omnichannel routing, and email tickets must
have the auto-routing tag. Think of this as *group-based omnichannel routing*.

In some cases, it's not realistic or desirable to have your tickets routed to the
single group assigned to the ticket. Creating custom queues allows you to route work
to multiple groups based on the queue the tickets are assigned to. Multiple queues
also give you the option to define secondary or "overflow" groups that receive
tickets through a queue only if all agents in the primary groups are unavailable.
When you assign multiple primary and secondary groups to a queue, omnichannel
routing treats all primary groups as a single pool of agents, and when necessary,
expands it to include all agents in the secondary groups as well.
When you use *queue-based routing*, omnichannel
routing uses the queue's primary and secondary groups to assign the ticket to an
agent, ignoring any group that might be specified on the ticket itself.

For more information, see [Creating additional omnichannel routing queues](https://support.zendesk.com/hc/en-us/articles/6716530152858).

## Understanding how omnichannel routing orders tickets within queues

As soon as a ticket is eligible for routing, omnichannel routing attempts to assign
it to an eligible and available agent. When using the standard queue, ticket
triggers automatically run when a ticket is created or updated. Then, omnichannel
routing attempts to assign the ticket to an available agent in the ticket's group.
If no agents in the group are available, the ticket is inserted into the queue. When
using custom queues, ticket triggers automatically run when a ticket is created or
updated, then omnichannel routing matches the ticket to a queue and attempts to
assign it immediately to an agent in the queue's primary or secondary groups; if no
agents in any of the queue's groups are available, the ticket is inserted into the
queue. If a ticket doesn't match the conditions for any custom queues but has an
assigned group, omnichannel routing attempts to assign the ticket to an available
agent in the ticket's group and, if no agent in the group is available, inserts the
ticket into the standard queue.

When tickets are inserted into a queue, there are two ways you can configure
omnichannel routing to insert and order tickets within queues: ticket priority and
timestamp or time to SLA breach. The standard configuration uses the time at which a
ticket becomes eligible for routing and, on Professional plans and above, the
ticket's priority.

### Ordering tickets by priority and timestamp

In the standard omnichannel routing configuration, there are four characteristics
of a ticket that omnichannel routing tracks to determine its place within a
queue:

- [Ticket eligibility for routing](#id_s3g_bn4_j1c)
- [Routing eligibility timestamps](#topic_qjf_gyz_31c)
- [Routing ineligibility time](#topic_zdg_d44_j1c)
- [Ticket priority](#topic_ppf_w55_fdc)
  (Professional plans and above)

#### Ticket eligibility for routing

Ticket
eligibility for routing by omnichannel routing depends on whether the
tickets are entering the standard queue or custom queues.

For tickets to be eligible to enter the *standard omnichannel routing
queue*, including tickets that don't match the conditions for any of
your custom queues, the following must be true:

- Assigned to a group
- In a status or status category of New or Open
- Unassigned
- ([Email tickets](https://support.zendesk.com/hc/en-us/articles/4409149119514#topic_psx_hxk_3yb) only) Has
  the auto-routing tag

For tickets to be eligible to enter a *custom omnichannel routing
queue*, the following must be true:

- In a status or status category of New or Open
- Unassigned

Conversely, if any of the following conditions are true, a ticket isn't
eligible for routing by omnichannel routing in either the standard queue or
custom queues:

- The ticket isn't assigned to a group and doesn't match a custom
  queue.
- The ticket is assigned to an agent.
- The ticket has a status (or status category) of Pending, On Hold, or
  Solved.
- The ticket's messaging session has ended and the routing channel is
  *messaging*.
- The ticket has been soft deleted.
- (Email tickets and the standard queue only) The ticket doesn't have
  the auto-routing tag.

#### Routing eligibility timestamps

There are plenty of scenarios when tickets will change back and forth between
[eligible](#id_s3g_bn4_j1c) and
ineligible for routing with omnichannel routing. That means omnichannel
routing needs to track two types of routing eligibility timestamps: initial
and subsequent.

- The *initial eligible for routing* timestamp is when a ticket
  becomes eligible for routing through omnichannel routing for the
  first time.
- A *subsequent eligible for routing* timestamp is when a ticket
  becomes eligible again for routing through omnichannel routing after
  having already been eligible and ineligible previously.

#### Routing ineligibility time

Omnichannel routing tracks the time tickets spend being ineligible for
routing and uses this to determine which routing timestamp to use when
inserting a ticket back into the routing queue. This is referred to as the
*routing ineligibility time*.

When a ticket's ineligibility for routing has never lasted 15 days or more,
the *initial eligible for routing* timestamp determines the ticket's
place in the routing queue. However, when a ticket's ineligibility period
extends to 15 days or more, omnichannel routing uses the latest
*subsequent eligible for routing* timestamp when inserting the
ticket back into the routing queue.

Note: The switch at 15 days isn't exact.
Instead, a job runs regularly to evaluate routing ineligibility times
and determines which eligibility timestamp to use. The first time the
job completes after a ticket reaches 15 days of ineligibility,
omnichannel routing switches from using the ticket's *initial eligible
for routing* timestamp (or previous *subsequent eligible for
routing* timestamp) to its latest *subsequent eligible for
routing* timestamp.

Checking ticket ineligibility for routing prevents performance issues caused
by tracking an ever-growing number of timestamps and accounts for decreasing
priority as tickets age.

#### Ticket priority

On Professional plans and above, omnichannel routing automatically orders
tickets based on priority first and then by their routing eligibility
timestamp. This sorting method prioritizes the oldest and most important
tickets.

However, if you use SLAs, ticket priority and age might not be the most
important metrics to use for ordering tickets within your queues.

### Ordering tickets by time to SLA breach

Ordering tickets by time to SLA breach brings your routing logic into alignment
with your service commitments and can improve your ability to meet those
goals.

Consider the following when ordering tickets based on SLA targets:

- The method of ticket ordering you use determines the order of tickets
  within any given queue, but doesn't influence the priority of ticket
  assignment across queues. If an agent can receive work from multiple
  queues, tickets from the queue with the higher priority are assigned to
  the agent before tickets from the lower priority queue. This is true
  regardless of how soon tickets in the lower priority queue will breach
  their SLA targets. Take this into consideration when creating and
  ordering custom queues.
- When ordering tickets based on the time to their next SLA
  breach, the setting is applied only to new and reopened tickets. Tickets
  already in the queue when this setting is turned on remain ordered by
  priority and timestamp as they were before.
- Ticket ordering is based on the SLA targets as they existed when the
  ticket entered the queue. If SLA policies are modified before the ticket
  is routed to an agent, the old SLA targets are still used for the
  purposes of routing.
- When ordering tickets based on the time to their next SLA breach, all
  tickets with SLA targets are ordered ahead of tickets without SLA
  targets, regardless of ticket priority and timestamp. Tickets without
  SLA targets are ordered based on their [priority and routing eligibility
  timestamp](#topic_ktj_345_fdc).

If you want to order tickets based on SLA targets, update your omnichannel
routing configuration to [prioritize tickets with service level
agreements](https://support.zendesk.com/hc/en-us/articles/4828787357210#topic_qyr_nsr_fdc).

### Putting it together: Ordering tickets by priority and timestamp in a queue

The standard configuration orders and assigns tickets based on the ticket's
priority and routing eligibility time. Let's walk through a ticket's life cycle
with the standard omnichannel routing configuration:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/omnichannel_routing_queue_order.png)

1. On January 1, 2024, a customer sends an email, and a ticket is created
   at 08:30.
2. The creation of the ticket causes the triggers to run and then
   omnichannel routing to evaluate queues for the ticket.
   1. When the triggers fire, the auto-routing tag is added and the
      ticket is assigned to *Group 1*. These ticket updates occur
      one minute after the ticket was created. (08:31)

      The
      *initial eligible for routing* timestamp is
      2024:01:01:08:31.
   2. Omnichannel routing recognizes the ticket as eligible for
      routing and adds it to the queue using the ticket's *initial
      eligible for routing* timestamp to determine its
      order.
      - If all tickets in the queue have the same priority,
        tickets with timestamps before 2024:01:01:08:31 will be
        ahead of this ticket in the queue, and those with
        timestamps after that will be behind it.
      - If not all tickets have the same priority, tickets with
        the highest priority are all added to the front of the
        queue in timestamp order, followed by tickets with the
        next highest priority in timestamp order, and so
        on.
3. When the ticket reaches the front of the queue, omnichannel routing
   looks for an agent in Group 1 that is available and has spare capacity.
   It finds an agent at 08:37 and assigns the ticket to them.

   The ticket
   becomes ineligible for routing as soon as it's assigned to the
   agent. The ticket's *routing ineligibility time* begins at
   2024:01:01:08:37.
4. After three days of working on the ticket, at noon (12:00) on January 4,
   2024, the agent reassigns the ticket to *Group 2*.

   The ticket
   becomes eligible for routing again because the new group assignment
   removes the previous agent assigned to the ticket. Because the
   ticket's *routing ineligibility time* was less than 15 days, it
   re-enters the queue and is ordered based on its initial eligible for
   routing timestamp (2024:01:01:08:31).

   Assuming equal priority,
   this ticket is inserted ahead of all tickets that became eligible
   for routing after this ticket was initially added to the
   queue.
5. Omnichannel routing assigns the ticket to an agent in Group 2 a few
   minutes after it's added to the queue.
6. After 20 days of being assigned to the agent in Group 2, the agent
   decides to reassign it to another group to which they don't belong.
   (Timestamp: 2024:01:24:10:45)

   Because the ticket's *routing
   ineligibility time* exceeded 15 days, the ticket is placed in
   the queue based on its priority and latest *subsequent eligible
   for routing* timestamp of 2024:01:24:10:45. Tickets of equal
   or greater priority that became eligible for routing prior to
   January 24, 2024, at 10:45 am and haven't had an ineligibility
   period of 15 days are ahead of this ticket in the queue.
7. When the ticket reaches the front of the queue, omnichannel routing
   assigns it to another agent. This agent works on the ticket and changes
   the status to Solved.