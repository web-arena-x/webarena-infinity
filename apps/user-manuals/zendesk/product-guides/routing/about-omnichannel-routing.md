# About omnichannel routing 

Source: https://support.zendesk.com/hc/en-us/articles/4409149119514-About-omnichannel-routing

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Verified AI summary ◀▼

Omnichannel routing directs tickets from various channels to agents based
on availability and capacity, enhancing response times and prioritizing high-value
customer interactions. It supports unified agent status, custom queues, and
skills-based routing. While it requires setup and configuration, it streamlines
ticket assignment, prevents cherry-picking, and allows agents to handle multiple
channels. Note limitations like unsupported chat-only routing and specific
plan-based features.

Omnichannel routing allows you to direct new and open tickets from [email (including web form, side
conversations, and API), calls, and messaging](#topic_psx_hxk_3yb) to agents based on their
availability and capacity. On [Growth plans
and above](#topic_hhb_2xk_3yb), tickets can be routed based on time to service level agreement
breaches. On Professional plans and above, tickets can also be routed based on priority
and skills.

Using omnichannel routing means agents can set a [single unified status](https://support.zendesk.com/hc/en-us/articles/5133523363226) for all channels, and important
tickets are assigned to the agents who are most available to work on them. This provides
the following benefits:

- Agents can respond to tickets faster
- You can prioritize work from high-value customers, including calls
- Agents are automatically assigned tickets and don’t have to go looking for
  them
- Agents can’t "cherry pick" the tickets they want to work on
- Agents can work on multiple ticket channels at once
- You can route calls to specific groups of agents based on the caller's country code
  of callers or other attributes

You can use *capacity rules* to limit the amount of work that’s assigned
to agents at one time. However, regardless of these rules, agents can assign themselves
work in excess of these limits if they want to (see [Creating capacity rules to balance agent workloads](https://support.zendesk.com/hc/en-us/articles/4776409839770)).

With omnichannel routing, instead of setting status individually by channel, agents can
set a single unified status for email, voice, and messaging. On Professional plans and
above, admins can also define their own custom statuses such as “Out to lunch” or “In a
meeting.” This can assist you when deciding how you want to route work items (calls,
tickets, and messages) based on the agent status and capacity. See [Adding unified agent statuses](https://support.zendesk.com/hc/en-us/articles/4410525357594).

This article contains the following sections:

- [Requirements and limitations of omnichannel routing](#topic_zlk_c3p_m5b)
- [How omnichannel routing works](#topic_nlb_c3p_m5b)
- [Summary of features](#topic_hhb_2xk_3yb)
- [Related articles](#topic_r1l_c3p_m5b)

## Requirements and limitations of omnichannel routing

To use omnichannel routing, you have to [set it up](https://support.zendesk.com/hc/en-us/articles/5866925319962) and [configure it](https://support.zendesk.com/hc/en-us/articles/4828787357210). If you decide to stop using it, you can
[turn it off](https://support.zendesk.com/hc/en-us/articles/5095079121690).

There are a few requirements for using omnichannel routing, as well as some
limitations you should consider.

### Requirements

Your account must meet the following requirements to use omnichannel routing:

- The [Agent Workspace](https://support.zendesk.com/hc/en-us/articles/4408821259930) must be
  activated for your account.
- If your account has a Chat subscription, native messaging or Sunshine
  Conversations must also be activated.
- Messaging must be activated to turn on omnichannel routing while using
  live chat. Limited support for Chat is provided for accounts [migrating to Messaging and
  omnichannel routing](https://support.zendesk.com/hc/en-us/articles/6249962577690).

### Limitations

Omnichannel routing with unified agent status currently has the
following limitations:

- Omnichannel routing can't be activated if you’re using only live
  chat. Messaging must be activated,
  too.
- At the time omnichannel routing is activated, agent statuses are
  automatically set to *offline* initially, then agents are prompted to
  set their own status after that.
- Only tickets with a status of *new* or *open* are routed by
  omnichannel routing.
- Broadcast and hybrid modes for messaging aren't supported.
- When using [unified agent statuses](https://support.zendesk.com/hc/en-us/articles/5133523363226), operating
  hours won't automatically set an agent's status.
- [Light agents](https://support.zendesk.com/hc/en-us/articles/4408846501402) can't be assigned
  tickets and can't set a status.
- The ability to change a Talk agent’s status from the Talk
  dashboard, mobile apps, or by using the Talk APIs isn't supported.
  Integrations that use Talk APIs to change agent statuses might also be
  impacted.
- When using custom queues, work routed through your custom queues are
  prioritized over all work routed through the standard queue, regardless of
  the individual ticket priority.
- Tickets are created for all calls received during business hours
  as soon as they enter the queue. The tickets are routed to agents only if the call is
  active. Abandoned calls and calls that exceed the maximum queue waiting time are considered inactive,
  and therefore aren't routed by omnichannel routing. The channel for calls received during business hours, whether the
  call is answered or goes to voicemail, is *inbound call*.

  Calls received outside of business
  hours go directly to voicemail and their tickets have a channel of
  *voicemail*. Tickets generated by voicemails can't be routed by
  omnichannel routing. Tickets
  for calls that go to voicemail, regardless of when they're received,
  have a subject beginning with "Voicemail from."
- The setting “Create tickets for abandoned calls” is no longer
  available.

  Tip: You can [create a workflow to automatically
  close tickets](https://support.zendesk.com/hc/en-us/articles/5027246725786) created for abandoned calls.
- If call forwarding is enabled and the status of an agent is
  automatically set to offline because the agent has been disconnected, calls
  to the agent will no longer be forwarded to the agent’s phone.
- When using priority phone numbers in Zendesk, calls that reference a
  priority line are assigned to agents first. Then, calls are assigned to
  agents in order based on the associated tickets' priority and timestamp.
  Tickets associated with calls on priority lines have a priority of
  *High*.
- Talk Partner Edition isn't supported. The way you route calls for Talk
  Partner Edition depends on the integration you're using.
- When offering messaging conversations (and sometimes live chats) to agents,
  only 20 *offered to* events are recorded per ticket. Omnichannel
  routing will continue to offer the ticket beyond 20 times as needed, until
  an agent accepts the ticket, but any offers after the first 20 aren't
  recorded in the [ticket event log](https://support.zendesk.com/hc/en-us/articles/4408829602970).
- After a voice ticket has been assigned to an agent, omnichannel routing won't
  reassign it, even if the ticket becomes unassigned or gets assigned back to
  a group. For email and messaging channels, ticket reassignment depends on
  your plan and routing configuration. On Team and Growth plans, email and
  messaging tickets can be reassigned through the standard omnichannel routing
  queue, but they can't re-enter custom queues.
  On Professional plans and above, you can choose to [reassign email and messaging tickets
  through custom queues](https://support.zendesk.com/hc/en-us/articles/4828787357210#topic_g4r_x1z_rcc) or rely on the standard queue.
- If you're using a ticket trigger to assign a group to tickets for calls,
  when an agent uses the group transfer feature in Talk, it can cause the
  ticket trigger to fire and overwrite the agent's group assignment back to
  the trigger's group assignment. To avoid this, you can configure ticket
  triggers that assign a group to call tickets to include either a **Ticket |
  Is | Create** condition, meaning it fires only on newly created
  tickets rather than updates such as a group transfer, or **Ticket > Comment
  text | Does not contain the following string | Call transferred**,
  meaning it fires only on tickets that haven't been transferred.
- Omnichannel routing doesn’t work on [AI agent tickets](https://support.zendesk.com/hc/en-us/articles/9204149016346) until the ticket
  is escalated to a human agent.

## How omnichannel routing works

When you use omnichannel routing, tickets are generated for all channels of work as
soon as they are received, enabling you to run triggers on them, including incoming
calls. For brevity, channels of work are labeled as *Email* (including tickets
generated from email, web form, side conversations, and API), *Messaging*
([sometimes including tickets from Chat](https://support.zendesk.com/hc/en-us/articles/6249962577690)),
and *Talk*. Omnichannel routing classifies tickets based on the original
channel through which they are received, even if other channels are used in the
course of resolving the ticket.

As soon as a ticket becomes eligible for routing, omnichannel routing
attempts to assign it to the first eligible and available agent. If no eligible
agents are available at the time, the ticket is inserted into a queue and routed
based on the following:

- **Queue**: This is defined by the [omnichannel routing queue](https://support.zendesk.com/hc/en-us/articles/6712096584090) the ticket
  is inserted into. Omnichannel routing uses one or more queues to order and
  assign tickets to agents: a single, standard omnichannel routing queue (default)
  or custom omnichannel routing queues. The queue assignment determines which
  groups of agents are eligible to be assigned to each ticket. If you aren't using
  [custom queues](https://support.zendesk.com/hc/en-us/articles/6716530152858), all tickets are
  inserted into the standard omnichannel routing queue.
- **Availability**: This is defined by the [single unified status](https://support.zendesk.com/hc/en-us/articles/4410545721114) the agent sets
  across channels.
- **Capacity** for each work channel: You define the agents' maximum
  capacity for each channel and decide which email tickets are eligible for
  routing.
- **Assignment method**: This is defined by the assignment method in your
  routing configuration and applies to all channels and queues. When assigning by
  spare capacity, you also select whether that is based on the percentage of an
  agent's capacity consumed by assigned tickets or the number of tickets they
  still have capacity to be assigned for the channel.
- **Skills**: This is defined by the [skills assigned to agents and tickets](https://support.zendesk.com/hc/en-us/articles/5833468891674)
  and applies to all channels.

Then triggers are used to assign the tickets to groups, assign a ticket
priority, and add tags to the ticket. After triggers run on a ticket, custom
omnichannel routing queues are evaluated, and the ticket is inserted into the first
queue it meets the conditions for. When using the standard omnichannel routing
queue, messaging conversations and calls enter the queue as soon as they are
received, but email tickets must have a routing tag added to them before they can
enter the queue. Tickets in the standard queue rely on the ticket's assigned group
to identify eligible agents. If you create custom omnichannel routing queues, email
tickets are treated the same as messaging conversations and calls, and are evaluated
and matched to a queue as soon as they are received, regardless of tags. If a ticket
doesn't meet the conditions for any of your custom queues, it's inserted into the
standard omnichannel routing queue and routed to an agent in the ticket's assigned
group.

If you have multiple brands, omnichannel routing respects the [brand memberships](https://support.zendesk.com/hc/en-us/articles/7584022494874) of your agents. Tickets are only
assigned to agents who are members of the ticket's brand.

After a ticket is assigned to an agent, it is removed from the omnichannel
routing queues.

The following table shows the order in which tickets are routed to
agents:

| Plan | Order in which tickets are routed |
| --- | --- |
| Suite Team | The ticket with the oldest eligible-for-routing timestamp within the queue is routed first. |
| Suite Growth and above | Admins can configure whether the ticket with the oldest eligible-for-routing timestamp within the queue or the ticket with the soonest [service level agreement](https://support.zendesk.com/hc/en-us/articles/4408829459866) breach is routed first. |
| Suite Professional and above | Admins can configure whether the ticket with the highest priority and oldest eligible-for-routing timestamp or the ticket with the soonest service level agreement breach is routed first.  Although skills don't influence the order of tickets within a queue, they can cause tickets to remain in the queue awaiting an agent with the matching skills while tickets of lower priority and newer timestamps get assigned. |

When a ticket makes it to the front of the queue, it's assigned to agents
based on the following:

1. The ticket's group or queue's groups:
   - If you're not using custom queues, a ticket must be assigned to a group
     to be eligible for routing with omnichannel routing.
   - Custom queues can be used to route work to multiple groups of agents
     with omnichannel routing. Tickets in queues are routed to the queue's
     groups, ignoring the ticket's assigned group.
   - When using custom queues, work is assigned to agents in the primary
     groups first. If no agents from those groups are available when a ticket
     reaches the front of the queue, omnichannel routing looks for available
     agents in the secondary or "fallback" groups.
   - If an agent can receive work from more than one queue, omnichannel
     routing assigns work from the queue with the highest priority
     first.
   - If a ticket doesn't match a custom queue, it's inserted into the
     standard omnichannel routing queue and routed to an agent based on the
     group assigned to the ticket. Tickets from all channels that don't meet
     the conditions for your custom queues must have a group assigned to be
     routed through the standard omnichannel routing queue. Furthermore,
     email tickets that don't meet the conditions for any custom queues must
     also have the auto-routing tag.

   See [Understanding omnichannel routing
   queues](https://support.zendesk.com/hc/en-us/articles/6712096584090).
2. An agent's status for the channel:
   - **Email tickets**: An agent must have a status of *online* or
     *away* to receive email tickets.
   - **Messaging conversations**: An agent must have a status of
     *online* to receive messaging tickets.
   - **Calls**: An agent must have a status of *online* to
     receive incoming call tickets.

   Agents are automatically set to offline or away, as defined by
   an admin, when they are idle for longer than the [idle status threshold](https://support.zendesk.com/hc/en-us/articles/4828787357210).
   Additionally, if an agent forgets to set their status to offline, the status
   of the agent is automatically set to offline when one of the following
   events is detected:

   - An agent closes the Agent Workspace without signing out (by
     closing down their computer or browser window or putting their computer
     to sleep)
   - An agent’s connection is lost due to a network outage

   See [Setting your unified agent status with
   omnichannel routing](https://support.zendesk.com/hc/en-us/articles/4410545721114).
3. Assignment method:
   - **Highest spare capacity**: The standard omnichannel routing
     configuration assigns work to the available agent with the most spare
     capacity for the channel.
     - Agents must have spare capacity to be eligible to receive work
       through omnichannel routing. Spare capacity is defined as having
       fewer open tickets assigned than their maximum capacity for that
       channel. See [Creating capacity rules to
       balance agent
       workload](https://support.zendesk.com/hc/en-us/articles/4776409839770).
     - Spare capacity can be measured numerically or as a percentage.
       See [Managing your omnichannel
       routing configuration assignment method](https://support.zendesk.com/hc/en-us/articles/4828787357210#topic_y3p_mh2_rcc).
     - If more than one agent has an eligible status and
       spare capacity, the agent with the highest spare capacity for
       the relevant channel is assigned.
     - If more than one agent has an eligible status and the same spare
       capacity for the relevant channel, the ticket is assigned to the
       agent who hasn't been assigned a ticket from the relevant
       channel in the longest time. Omnichannel routing treats
       re-opened tickets as assignment events.
     - To be assigned an inactive messaging ticket (more than 10
       minutes without a reply), an agent must have spare capacity.
       Whether inactive messaging tickets count towards an agent's
       capacity depends on your routing configuration.
   - **[Round robin](https://support.zendesk.com/hc/en-us/articles/7990049158554)**: Assigns
     the work to the available agent who's gone the longest time without
     being assigned work for the channel. Agents still must have spare
     capacity to be assigned work.
4. An agent's skills:
   - An agent must have the same skills as the ticket in addition to having
     an eligible status and spare capacity.
   - If a skill is a high priority for an agent, omnichannel routing will
     look for tickets in the queue with that high priority skill to assign to
     the agent. If no tickets with the agent's high priority skills are
     found, then other tickets they are eligible to receive are assigned. See
     [Configuring the priority of an
     agent's skills](https://support.zendesk.com/hc/en-us/articles/4408838892826#topic_ysc_fq4_ghc).
   - If you configure a [skills timeout](https://support.zendesk.com/hc/en-us/articles/4828787357210#:~:text=Turn%20on%20skills%20timeout), tickets are
     assigned without regard to optional skills if an agent with all of the
     matching skills is unavailable for a specified duration after a ticket
     reaches the front of the queue. If a skills timeout isn't configured,
     all skills are treated as required and tickets will sit in the queue
     until an agent with the matching skills becomes available or a call
     reaches the maximum time in queue and is sent to voicemail. See [Using skills with omnichannel
     routing](https://support.zendesk.com/hc/en-us/articles/5833468891674#topic_d2l_bnx_txb).

Here's an example of a scenario for omnichannel routing:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ocrdiag22.png)

1. An important VIP end user has an urgent issue that needs to be
   resolved.
2. They submit a ticket using the email channel.
3. The account admin has set up a trigger for the account to add the
   auto-routing tag to these tickets and then assign a group, priority, and
   skills.
4. After the triggers fire, the end user's ticket is matched to an
   omnichannel routing queue and inserted based on the ticket's priority of
   *Urgent* and it's eligible-for-routing timestamp.
5. Omnichannel routing now assesses the ticket based on agent skills,
   status, and capacity.
6. The routing system first understands that three agents are available
   for work.
7. Second, it identifies that two of the agents have the skill (German
   language) required for the ticket.
8. Finally, it finds which of those two agents has the most spare
   capacity for emails and assigns the ticket to this agent.

### Reassigning messages and calls in omnichannel routing

Messaging conversations and calls require time-sensitive responses. Therefore,
omnichannel routing has special reassignment logic for each. For more
information about how tickets enter and leave the queue to be routed by
omnichannel routing, see [Understanding how omnichannel routing orders
tickets in a queue](https://support.zendesk.com/hc/en-us/articles/6712096584090).

**Reassigning messaging conversations and chats**

With reassignment timing, a message or chat can be reassigned to another agent in
the group if the original agent does not accept the work within a specific time
threshold. The default threshold is 30 seconds. On Enterprise and above, that
threshold can be customized.

The reassignment timing setting must be [turned on during configuration](https://support.zendesk.com/hc/en-us/articles/4828787357210) to
reassign messages automatically if they aren’t accepted within the specified
time. If that setting isn’t enabled, the routing engine will keep trying the
same agent.

**Reassigning incoming calls**

When a call is offered to an agent, they can choose to accept or decline it. If
the agent declines the call or doesn't answer within 30 seconds, the call is
returned to the queue and assigned to another available agent. The call will
continue to be offered to available agents in a round-robin fashion until the
[maximum queue waiting time](https://support.zendesk.com/hc/en-us/articles/4408838035866#topic_w1l_j14_5fb) expires.
When using skills-based routing for calls, you can leverage the skills timeout
settings to "overflow" the calls to agents without the matching skill when
needed; you can also use custom queues with primary and secondary groups to
accomplish this "overflow" behavior.

Because call tickets are created as soon as the call comes in, admins can create
a [view in Support](https://support.zendesk.com/hc/en-us/articles/4408888828570) that shows details
about waiting calls. To create such a view, use at least the following
conditions:

- **Hours since created** > **(calendar) Less than**
  >**1**
- **Status** > **Less than** >**Solved**
- **Channel** > **is** > **Phone call (incoming)**

After a call ends, the ticket generated by the call is removed from the
omnichannel routing queue. If an agent needs to add more information to the
ticket after a call ends, they must manually find the ticket, either by searching
or using a view.

## Summary of features

Omnichannel routing has a broad scope, so here's a quick reference of features and
functionality.

### Channels supported by omnichannel routing

At a high level, omnichannel routing can be used to route tickets from email,
messaging, and calls. However, in business rules, these categories of tickets
are broken down into [`via` types](https://developer.zendesk.com/documentation/ticketing/reference-guides/via-types/). The
following lists show the supported via types (referred to as *[channels](https://support.zendesk.com/hc/en-us/articles/4408824097050)*) as they appear in
Admin Center business rule conditions.

**Email tickets**

- Email
- Web form
- Web service (API)
- Closed ticket
- Ticket sharing
- Facebook post
- X (formerly Twitter)
- Web widget
- Mobile SDK
- Side conversation
- Merge
- Legacy channel framework (any\_channel)
- [SMS texts](https://support.zendesk.com/hc/en-us/articles/4408885601178)

**Messaging conversations**

- Native messaging
- LINE
- SMS (through Sunshine Conversations
  only)
- Facebook Messenger (through Sunshine Conversations
  only)
- Telegram
- X (formerly Twitter) Direct Message
- WeChat
- WhatsApp
- Google RCS
- Apple Messages for Business
- Google Business Messages
- KakaoTalk
- Instagram Direct Messenger
- Sunshine Conversations API
- Chat (only supported in [some circumstances](https://support.zendesk.com/hc/en-us/articles/6249962577690))

**Calls**

- Phone call (incoming)
- Phone call (outgoing)

### Summary of features by plan

The availability of omnichannel routing features varies by plan level. The
following applies to your Zendesk Suite plan level, or to the plan level of all
individual products:

| Team | Growth | Professional | Enterprise |
| --- | --- | --- | --- |
| Routing email, messaging and call tickets | Routing email, messaging and call tickets | Routing email, messaging, and call tickets | Routing email, messaging, and call tickets |
| Routing based on capacity and agent status | Routing based on capacity and agent status | Routing based on capacity, agent status, skills, and queue | Routing based on capacity, agent status, skills, and queue |
| Default unified agent statuses | Default unified agent statuses | Default and custom unified agent statuses | Default and custom unified agent statuses |
| Focus mode for agents working on messaging and calls | Focus mode for agents working on messaging and calls | Focus mode for agents working on messaging and calls | Focus mode for agents working on messaging and calls |
| Include or exclude inactive messaging tickets when calculating agent capacity | Include or exclude inactive messaging tickets when calculating agent capacity | Include or exclude inactive messaging tickets when calculating agent capacity | Include or exclude inactive messaging tickets when calculating agent capacity |
| Automatic assignment of messaging tickets | Automatic assignment of messaging tickets | Automatic assignment of messaging tickets | Automatic assignment of messaging tickets |
| Assignment based on spare capacity or round robin | Assignment based on spare capacity or round robin | Assignment based on spare capacity or round robin | Assignment based on spare capacity or round robin |
| Message reassignment | Message reassignment | Message reassignment | Customizable reassignment time |
| Routing in order of soonest SLA breach | Routing in order of soonest SLA breach | Routing in order of soonest SLA breach or highest priority | Routing in order of soonest SLA breach or highest priority |
|  |  | Reassignment of reopened tickets when the assigned agent is unavailable | Reassignment of reopened tickets when the assigned agent is unavailable |
|  |  | Custom omnichannel routing queues | Custom omnichannel routing queues |
|  |  | Up to 5 custom statuses | Up to 100 custom statuses |

## Related articles

See the following articles for more information to help you get up and
running with omnichannel routing and agent statuses:

- [Turning on and setting up omnichannel
  routing](https://support.zendesk.com/hc/en-us/articles/5866925319962)
- [Managing your omnichannel routing
  configuration](https://support.zendesk.com/hc/en-us/articles/4828787357210)
- [Understanding queues in omnichannel
  routing](https://support.zendesk.com/hc/en-us/articles/6712096584090)
- [Creating capacity rules to balance agent
  workload](https://support.zendesk.com/hc/en-us/articles/4776409839770)
- [About unified agent statuses](https://support.zendesk.com/hc/en-us/articles/5133523363226)
- [Adding unified agent statuses](https://support.zendesk.com/hc/en-us/articles/4410525357594)
- [Managing unified agent statuses](https://support.zendesk.com/hc/en-us/articles/5133588225690)
- [About using skills to route
  tickets](https://support.zendesk.com/hc/en-us/articles/5833468891674)