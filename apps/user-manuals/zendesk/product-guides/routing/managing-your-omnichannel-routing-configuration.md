# Managing your omnichannel routing configuration

Source: https://support.zendesk.com/hc/en-us/articles/4828787357210-Managing-your-omnichannel-routing-configuration

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Verified AI summary ◀▼

Manage your omnichannel routing configuration to streamline ticket handling across email, calls, and messaging. Plan your configuration to optimize routing logic, set priorities, and use capacity rules. Customize settings like skills-based routing, focus mode, and reassignment options to suit your needs. Regularly review and adjust configurations based on feedback and performance data to ensure optimal support operations.

Location:  Admin Center > Objects and rules > Omnichannel routing > Routing configuration

This article assumes omnichannel routing has been turned on for
your account. See [Turning on and setting up omnichannel routing](https://support.zendesk.com/hc/en-us/articles/5866925319962).

[Omnichannel routing](https://support.zendesk.com/hc/en-us/articles/4409149119514) is a highly configurable routing
solution that can route new and open tickets from [email (including web form, side conversations, and
API)](https://support.zendesk.com/hc/en-us/articles/4409149119514#topic_psx_hxk_3yb), calls, and messaging. Omnichannel routing provides the most
sophisticated routing logic, which can increase agent efficiency and effectiveness. It
works out of the box, but you'll get the most value if you take your time planning your
routing configuration. Your routing configuration applies to all [omnichannel routing queues](https://support.zendesk.com/hc/en-us/articles/6712096584090).

This article contains the following topics:

- [Planning your routing configuration](#topic_frn_1vc_yxb)
- [Editing the routing configuration](#topic_ymt_btp_m5b)
- [Configuring omnichannel routing to route tickets based on priority](#topic_hfx_jjb_yxb)
- [Evolving your routing configuration](#topic_rsj_c5w_4xb)

## Planning your routing configuration

Omnichannel routing [works out of the box](https://support.zendesk.com/hc/en-us/articles/4409149119514#topic_nlb_c3p_m5b). As long as you
already have a mechanism in place to assign incoming tickets to groups, such as
triggers, omnichannel routing can start routing calls and messaging conversations as
soon as it's turned on and email tickets as soon as the auto-routing tag is added to
them. Therefore, when you set up omnichannel routing or adjust your routing
configuration, it's best to have a detailed plan ahead of time.

**To plan out your omnichannel routing configuration**

1. (Optional) To make the most informed decisions about your routing
   configuration settings, you might want to consider the questions posed in
   [Best practices: Planning your routing
   workflow](https://support.zendesk.com/hc/en-us/articles/5866820143770).
2. On all plan types, do the following:
   - [Email (including web form, side
     conversations, and API)](https://support.zendesk.com/hc/en-us/articles/4409149119514#topic_psx_hxk_3yb) must have a unique routing tag to
     be routed through the standard omnichannel routing queue. However,
     the auto-routing tag isn't needed to route email tickets through
     [custom routing queues](https://support.zendesk.com/hc/en-us/articles/6712096584090),
     unless they don't match any custom queues and you want them to get
     picked up by the standard omnichannel routing queue. You can use the
     default auto-routing tag (*auto-routing*) or specify a
     different one.
   - You probably already use triggers to assign tickets to groups. If
     you're using the standard omnichannel routing queue, you need to
     ensure one or more triggers have an action to add the routing tag to
     any email tickets you want routed by omnichannel routing. The group
     assignment and auto-routing tag aren't required for tickets routed
     through [custom queues](https://support.zendesk.com/hc/en-us/articles/6712096584090). See [Requirements for the routing
     triggers](https://support.zendesk.com/hc/en-us/articles/5866925319962#topic_asz_ljb_yxb). Decide if you are going to modify existing
     triggers to function as routing triggers, or create new ones.
   - Omnichannel routing uses capacity rules to control how much work is
     assigned to each agent at a given time. There is a built-in capacity
     rule that is used by default, but you can define alternative rules
     that better meet your unique needs. Decide what [capacity rules](https://support.zendesk.com/hc/en-us/articles/4776409839770) you will
     need. For each rule, decide what the capacities will be for each
     channel and which agents will be assigned to the rule.
   - Decide whether you want to assign work to agents based on who has
     the most spare capacity for the channel (the standard configuration)
     or based on who hasn't been routed work from the channel in the
     longest time (round robin). If using spare capacity, decide whether
     you want that based on agents' percentage of spare capacity or
     numeric values.
   - [Review the standard unified agent
     statuses](https://support.zendesk.com/hc/en-us/articles/5133588225690). When omnichannel routing is on, [standard agent statuses](https://support.zendesk.com/hc/en-us/articles/5133523363226)
     are automatically available for agents to use across channels. The
     standard agent statuses can't be edited, but it's important to
     understand how they're configured.
   - Decide how you want to handle the situation when messaging
     conversations and calls are routed to agents but not accepted by
     them. Are you going to turn on [messaging reassignment timing](#topic_v24_2pr_wbc), where a
     messaging ticket is reassigned to a different team member if not
     addressed within the specified timing? Would you prefer to [auto-accept messaging
     tickets for agents](#topic_crn_f4r_wbc)?
   - How do you want agents to see the [email tickets](https://support.zendesk.com/hc/en-us/articles/4409149119514#topic_psx_hxk_3yb) assigned to
     them by omnichannel routing? Should they use a view to see their
     assigned tickets, or should the email tickets open in a new tab
     automatically, similar to messaging conversations?
3. On Professional and Enterprise plans, you'll also need to decide the
   following:
   - When you turn on omnichannel routing, it's configured to use the
     standard omnichannel routing queue that routes work from all
     channels to the ticket's assigned group. However, we recommend [creating custom queues](https://support.zendesk.com/hc/en-us/articles/6712096584090) to
     route tickets that meet specific conditions to multiple primary and
     secondary (fallback) groups. Decide if you need additional queues,
     what their conditions will be, and which groups will be primary and
     secondary. See [Understanding how omnichannel
     routing uses queues to route work to
     agents](https://support.zendesk.com/hc/en-us/articles/6712096584090).

     Note: Creating additional queues might require
     adjustments to your triggers so they continue working correctly
     to help you route work into the appropriate queues.
   - What [unified agent statuses](https://support.zendesk.com/hc/en-us/articles/5133523363226) are
     you going to use? Just the standard agent statuses or [custom statuses](https://support.zendesk.com/hc/en-us/articles/4410525357594), too? For
     each custom status, what will be the name of the status and what
     will be the per-channel statuses?
   - Are you routing based on ticket priority? If so, what triggers will
     you use to add and manage priority on tickets?
   - Are you [using skills](https://support.zendesk.com/hc/en-us/articles/4408838892826)? If so, what
     skills will you define and which agents have them? What routing
     rules or triggers will you use to add and manage skills on tickets?
     Do you want to fall back to routing without regard to skills if
     agents with the skills aren't available? If so, how long should it
     take for optional skills to time out? Which skills are always
     required and which are optional?
   - (Enterprise plans only) Are you going to turn on [call offering time limits](https://support.zendesk.com/hc/en-us/articles/4408823877146),
     which acts as a reassignment time threshold for incoming calls?
   - How do you want to handle [reopened email and messaging tickets](#topic_bpp_rqr_wbc) if the
     agent has certain statuses? For which statuses would you want to
     reassign email tickets? For which statuses would you want to
     reassign messaging tickets?
   - How do you want to handle reassigning tickets? Do you want new
     tickets to be prioritized over them and therefore rely on the
     standard queue for reassignment, or would you like them to be
     prioritized equally against new work and [reassigned through
     custom queues](#topic_g4r_x1z_rcc)?

## Editing the routing configuration

After you set up omnichannel routing, you can use the default
configuration or review and modify how omnichannel routing distributes the messages.
You can edit your routing configuration at any time.

Warning: Don't refresh your browser while viewing or editing your routing
configuration. Doing so causes all settings to be lost, regardless of whether they
were saved.

**To set up a routing configuration**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Omnichannel routing > Routing
   configuration**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ocr_4_GA.png)
2. On the **Routing Configuration** page, click **Edit** next to
   the Initial routing configuration.
3. On the **Initial routing configuration** page, you can see the name
   and description for the routing configuration.
4. Configure the following **Global routing** options, which apply to tickets
   from emails, messaging conversations, and calls across all omnichannel routing
   queues:
   - **[Ticket
     sorting](#topic_qyr_nsr_fdc)**: Determines whether tickets are ordered in the
     queues and assigned by date created, ticket priority, or nearest SLA
     breach.
   - **[Assignment
     method](#topic_y3p_mh2_rcc)**: Determines whether omnichannel routing
     assigns work to agents with the highest spare capacity or agents who
     have gone the longest without being assigned work for the channel.
     Regardless of the method you select, agents must have an eligible status
     and spare capacity for the channel to be routed work.
   - **[Turn on skills-based
     routing](#topic_ag5_tlr_wbc)**: (Professional plans and above for Zendesk
     Suite, Support, Talk, and Chat) Routes tickets to agents with matching
     skills who also have an eligible status and spare capacity. When using
     skills to route tickets, we recommend configuring a skills timeout.
   - **[Turn on focus
     mode](#topic_u1v_zsr_wbc)**: Assigns an agent work from one real-time
     channel at a time. Email tickets aren't included in this
     restriction.
   - **[Reassign reopened
     tickets](#topic_bpp_rqr_wbc)**: (Professional plans and above for Zendesk
     Suite, Support, and Chat) Reassigns email and messaging tickets if the
     assigned agent has a specified status when the ticket status changes
     from Solved, Pending, or On-hold back to Open.
   - **[Auto-reassign open
     tickets](#topic_xlt_ccg_w2c)**: Reassigns up to the 50 most-recently updated
     open email and messaging tickets of specified priorities when the
     assigned agent's status changes to a status configured for
     reassignment.
   - **[Reassign tickets
     through queues](#topic_g4r_x1z_rcc)**: (Professional plans and above for
     Zendesk Suite, Support, and Chat) Uses custom queues to reassign tickets
     that have been assigned to an agent and are then assigned back to a
     group. When not selected, tickets are reassigned through the standard
     queue.
5. Under **Email routing**, configure whether to **[Automatically open email
   tickets](#topic_etl_vhm_pcc)**. This determines whether newly assigned email tickets
   are opened in a new tab for the agent. Regardless of this setting, agents
   receive a notification that a new ticket has been assigned to them.
6. Configure the following **Messaging routing** options:
   - Choose whether to **Wait until the agent accepts** offered tickets
     or **[auto-accept for the
     agent](#topic_crn_f4r_wbc)**. Determines whether messaging tickets are
     offered to agents or automatically assigned to them by omnichannel
     routing.
   - **[Reassign if
     agent doesn't accept within time limit](#topic_v24_2pr_wbc)**: (Professional
     plans and above for Zendesk Suite, Support, and Chat) Reassigns work to
     a different team member if it isn’t addressed in the time you
     specify.
   - **[Count inactive
     conversations towards an agent's capacity](#topic_glj_pmr_wbc)**: Determines
     whether inactive messaging tickets are counted toward agent capacity and
     how inactive tickets are routed to agents.
   - **[Route all agent-ended
     messaging sessions as email](#topic_hr4_1lh_n2c)**: Determines whether
     tickets associated with messaging conversations are routed as email
     tickets after an [agent ends the messaging
     session](https://support.zendesk.com/hc/en-us/articles/8009788438042).
7. When you are finished, click **Save**.

### Global routing options

Global routing configuration settings affect all channels.

#### Ticket sorting

The standard omnichannel routing logic assigns work to agents in order of the
[routing eligibility timestamp](https://support.zendesk.com/hc/en-us/articles/6712096584090#topic_qjf_gyz_31c)
(commonly when the ticket is created). On Professional plans and above,
ticket priority is also considered by default. However, in some cases, it's
preferable to assign work in order of least time until an [service level agreement (SLA)](https://support.zendesk.com/hc/en-us/articles/4408829459866)
breach. Sorting tickets by SLA is available on Team plans and
above.

If you decide to order work by SLA breach times, tickets are ordered by
nearness to SLA breach, beginning with those that have already breached and
followed by tickets with upcoming breach times. All tickets with an SLA are
prioritized over those without; tickets that aren't subject to an SLA are
sorted behind all SLA-related tickets based on their priority and routing
eligibility timestamp.

Note: The ticketing sorting method you choose applies to the tickets in all
omnichannel routing queues.

**To prioritize tickets with SLA agreements**

- Under **Ticket sorting**, select **Prioritize tickets with a
  service level agreement (SLA)**.

#### Assignment method

The standard omnichannel routing configuration uses a combination of agent
statuses and capacity to predict which agent is most available to handle
each ticket. Admins can also decide whether they want to determine spare
capacity numerically or as a percentage of an agent's maximum capacity.
However, the complex interactions of how capacity is counted, having
multiple capacity rules for different agents, and custom statuses, means it
can sometimes be challenging for Zendesk admins and team leads to understand
why tickets are being routed the way they are. If you want all the other
benefits of omnichannel routing, but would like to increase the
predictability of which agent will receive work, you can configure
omnichannel routing to use the round robin method, which assigns work to
agents in a sequential order.

**To configure the assignment method**

- Under **Assignment method**, select one of the following:
  - **Highest numeric spare capacity**: (Default) When
    selected, highest spare capacity is based on the difference
    between their maximum capacity for the channel and their
    assigned work in the channel. Omnichannel routing compares
    the results of the following equation for each agent to
    determine which has the highest spare capacity:
    `maximum capacity for channel - number of channel
    tickets assigned`. The agent with the biggest
    integer is determined to have the highest spare
    capacity.
  - **Highest percentage spare capacity**: When selected,
    highest spare capacity is based on the percentage of an
    agent’s capacity consumed by work currently assigned to them
    for that channel. Omnichannel routing compares the results
    of the following equation for each agent to determine which
    has the highest spare capacity: `(number of channel
    tickets assigned / maximum capacity for channel) x
    100`. The agent with the lowest percentage is
    determined to have the highest spare capacity.
  - **Round robin**: When selected, omnichannel routing
    assigns tickets to agents in a sequential order, meaning the
    agent who has gone the longest period of time since last
    receiving work for the channel. Agents still must have spare
    capacity and eligible statutes to receive work for the
    channel.

    Note: Offering a call or messaging conversation
    to an agent and the reopening of a ticket are counted as
    assignment events for the purposes of the round robin
    assignment method.

    See [Using round robin
    routing for email, messaging conversations, and call
    tickets](https://support.zendesk.com/hc/en-us/articles/7990049158554).

#### Skills-based routing

On Professional plans and above, you can route tickets to agents with
matching skills who also have an eligible status and spare capacity. To use
this feature you must have [defined skills](https://support.zendesk.com/hc/en-us/articles/4408838892826) for your account
and a way to [assign skills to tickets](https://support.zendesk.com/hc/en-us/articles/5833458075930). When
using ticket triggers to assign skills to tickets, you can specify whether
each skill is required or optional. Skills marked as *required* can't
time out and are always part of the criteria for routing the ticket to an
agent, but *optional* skills stop being considered for routing purposes
when a skills timeout occurs.

If you turn on skills-based routing, we recommend configuring a skills
timeout. When you configure a timeout, work may be assigned to agents
without the optional skills if none of the agents with all of the skills are
available. For email tickets, which are always assigned to agents by
omnichannel routing, a skills timeout occurs when a ticket reaches the front
of the queue and no agent with all of the matching skills is available for a
specified duration. However, for messaging and calls, a skills timeout can
occur only if no agents with the matching skills are available (online, with
spare capacity) for the timeout duration. If any agent with matching skills
is available, omnichannel routing will continuously offer the ticket to them
until either they accept it or all agents with matching skills become
unavailable for the specified timeout duration.

If you don't turn on the skills timeout, email and messaging tickets with
skills remain in the queue indefinitely until an agent with all of the
matching skills becomes available, and calls remain in the queue until the
maximum queue wait time is reached and the call is sent to voicemail.

See [About using skills to route
tickets](https://support.zendesk.com/hc/en-us/articles/5833468891674).

**To turn on and configure skills-based routing within your routing
configuration**

1. Select **Turn on skills-based routing**.
2. (Recommended) Select **Turn on skills timeout** and configure
   your timeout thresholds per channel.
   - **Email**: The skills timeout threshold for email
     tickets. The default is one hour.
   - **Messaging**: The skills timeout threshold for messaging
     conversations. The default is 30 seconds. This also [applies to chats in some
     circumstances](https://support.zendesk.com/hc/en-us/articles/6249962577690).
   - **Talk**: The skills timeout threshold for calls. The
     default is 30 seconds.

#### Focus mode

On Team plans and above, you can configure omnichannel routing to help agents
focus when handling tickets from real-time channels (calls, messaging
conversations, and live chats). When you turn on focus mode, omnichannel
routing only routes an agent work from one real-time channel at a time.
Ticket priority is compared across channels to ensure the highest priority
real-time ticket is assigned first. For more information, see [About focus mode](https://support.zendesk.com/hc/en-us/articles/4408835750042#topic_oht_2cs_n4b).

Email tickets aren't included in this restriction and can still be assigned
while agents address more time-sensitive tickets from other channels.

**To turn on focus mode within your routing configuration**

- Select **Turn on focus mode**.

Note: Changing your messaging activity routing settings while focus mode is on
can cause messaging tickets to consume an agent's capacity, regardless of
the ticket's status, for up to 24 hours after the ticket is closed.

#### Reassign reopened tickets

On Professional plans and above, you can reassign email and
messaging tickets if the assigned agent has a specified status when a
ticket's status changes from Solved, Pending, or On-hold back to Open. If
you are using [custom ticket statuses](https://support.zendesk.com/hc/en-us/articles/4412575841306#topic_hmv_5kl_dwb), this
applies to all custom ticket statuses in the Solved, Pending, or On-hold
status categories. Depending on your other routing configuration settings,
ticket reassignment can be to another agent in the ticket's assigned group
or [through custom
queues](#topic_g4r_x1z_rcc).

Note: To configure reassignment of reopened tickets, your account must [allow agents to assign tickets back
to their groups](https://support.zendesk.com/hc/en-us/articles/4408834893978).

**To turn on and configure reassignment of reopened tickets within your
routing configuration**

1. Select **Turn on reassignment for reopened tickets**.
2. Select the agent statuses for which you want to reassign reopened
   **Email** tickets.

   If [reassigment through queues](#topic_g4r_x1z_rcc) is also on,
   all reopened email tickets are reassigned regardless of the
   routing tag. Otherwise this reassignment behavior applies to
   email tickets with the routing tag only, even if the ticket
   wasn't originally assigned by omnichannel
   routing.
3. Select the agent statuses for which you want to reassign reopened
   **Messaging** tickets. This also [applies to chats in some
   circumstances](https://support.zendesk.com/hc/en-us/articles/6249962577690).

#### Reassign open email and messaging tickets

You can choose whether open email and messaging tickets are re-assigned when
the currently-assigned agent changes status to a specified status. When on,
the 50 most-recently updated open email and messaging tickets of specified
priority that are assigned to the agent are reassigned when their status
changes to a specified status. When an agent's status changes, there is a
1-minute delay prior to the open tickets being reassigned.

**To reassign open email and messaging tickets**

1. Select **Auto-reassign open tickets**.
2. Select the channels you want to apply this setting to: **Email**
   or **Messaging**.
3. For each channel, specify the following:
   - **Agent status**: The agent statuses that should cause an
     agent's open tickets to be reassigned.

     Note: If you want to
     avoid the reassignment of work when agents are
     disconnected because of inactivity, ensure you configure
     different agent statuses for the [idle timeout](https://support.zendesk.com/hc/en-us/articles/5286614817562)
     and this feature.
   - **Ticket priority**: Which of the possible ticket
     priorities should be reassigned in these circumstances.

#### Reassign email and messaging tickets through custom queues

On Professional plans and above, if you use [custom queues](https://support.zendesk.com/hc/en-us/articles/6716530152858), you can choose how
omnichannel routing handles email and messaging tickets that get reassigned
back to a group after being assigned to an agent. When you turn on this
setting, tickets that are reassigned back to a group are inserted into the
first custom queue they match. If they don't match a custom queue, they're
inserted into the standard queue. Likewise, if you don't select to reassign
tickets through queues, all tickets that are reassigned back to a group are
routed through the standard queue.

Note: Tickets routed through custom queues
are prioritized over all tickets in the standard queue.

**To turn on reassignment of tickets through queues within your routing
configuration**

- Select **Reassign tickets through queues**.

### Email routing options

The following setting applies only to how omnichannel routing assigns email
tickets to agents.

#### Automatically opening email tickets

You can choose whether a newly assigned [email ticket](https://support.zendesk.com/hc/en-us/articles/4409149119514#topic_psx_hxk_3yb) opens automatically
in a new tab for the assigned agent, similar to messaging conversations.
Regardless of this setting, the agent receives a notification of the
assignment. If you choose not to automatically open email tickets, it's a
good idea to have agents use [views](https://support.zendesk.com/hc/en-us/articles/4408829483930) to monitor the tickets
assigned to them.

**To automatically open email tickets**

- Select **Automatically open assigned email tickets**.

### Messaging routing options

The following settings apply only to how omnichannel routing offers and assigns
messaging conversations to agents.

#### Auto-accept messaging tickets for the agent

Typically, messaging conversations are offered to agents rather than
automatically assigned. On Team plans and above, you can configure
omnichannel routing to automatically assign messaging tickets to agents
instead of offering them. This also [applies to chats in some
circumstances](https://support.zendesk.com/hc/en-us/articles/6249962577690).

This feature can't be used at the same time as messaging reassignment
timing.

**To decide how agents receive messaging tickets through omnichannel
routing**

- Select either **Wait until the agent accepts** (the standard
  configuration) or **Auto-accept for the agent**.

#### Messaging reassignment timing

On Professional plans and above, you can configure omnichannel routing to
reassign messaging tickets to a different team member if the assigned agent
hasn't addressed it in the time you specify. When messaging reassignment
timing is enabled, a specified time, in seconds, can elapse before work is
reassigned to another agent. Depending on your other routing configuration
settings, ticket reassignment can be to another agent in the ticket's
assigned group or [through
custom queues](#topic_g4r_x1z_rcc). The timing is 30 seconds on Professional plans,
and customizable on Enterprise plans. This also [applies to chats in some
circumstances](https://support.zendesk.com/hc/en-us/articles/6249962577690).

This feature can't be used at the same time as auto-accept for messaging.

**To turn on and configure messaging reassignment timing within your routing
configuration**

1. Select **Reassign if agent doesn't accept within the time
   limit**.

   The timing is 30 seconds on Professional
   plans.
2. (Enterprise plans only) Enter the **Messaging timing** in
   seconds.

Note: On Enterprise plans, you can also set a reassignment timing
threshold for incoming calls with the **Call offering time limit**.
See [Managing phone line
settings](https://support.zendesk.com/hc/en-us/articles/4408823877146).

#### Count inactive conversations towards agent capacity

On Team plans and above, you can choose whether to count all open active and
inactive messaging tickets towards an agent's [capacity](https://support.zendesk.com/hc/en-us/articles/4776409839770) or only active messaging
tickets. This setting was previously referred to as *messaging activity
routing*.

When selected, active and inactive messaging tickets are counted and offered
to agents through the Accept button.

When not selected, only active messaging tickets are counted towards capacity
and offered to agents through the Accept button. Inactive messages are
automatically assigned to a previously-offered agent or other available
agent.
See
[Understanding how capacity rules work for
messaging conversations and live chats](https://support.zendesk.com/hc/en-us/articles/4776409839770#topic_n2p_wxx_41c).

**To count inactive conversations towards agent capacity**

- Select **Count inactive conversations towards an agent's
  capacity**.

Note: Changing your messaging activity routing settings while focus mode is on
can cause messaging tickets to consume an agent's capacity, regardless of
the ticket's status, for up to 24 hours after the ticket is closed.

#### Route agent-ended messaging sessions as email tickets

When your account is configured to [allow agents to end messaging
sessions](https://support.zendesk.com/hc/en-us/articles/8372292195354), you can use this setting to determine how omnichannel
routing treats tickets associated with those messaging conversations. When
selected, omnichannel routing treats tickets associated with messaging
conversations for which the agent has ended the session as email tickets.
This means they are counted towards agents' email capacity. However, they
still appear as messaging tickets in the Agent Workspace and the ticket’s
via type doesn’t change. The only indication that this setting has been
applied to a ticket is in the [ticket event history](https://support.zendesk.com/hc/en-us/articles/4408829602970).

When messaging tickets are treated as email tickets for routing, they are
automatically assigned to the agent who ended the session. That agent can
reassign it to a group to have it re-routed by omnichannel routing. However,
these tickets must have the auto-routing tag to be routed by omnichannel
routing because that is a requirement.

When this setting isn't selected, tickets associated with ended messaging
sessions can't be routed by omnichannel routing.

Note: This setting applies to all messaging tickets whose session is ended
by an agent after the setting is turned on. If you'd prefer to only
route *some* messaging conversations as email tickets, you can
configure a trigger to use the [Ticket > Set routing channel
action](https://support.zendesk.com/hc/en-us/articles/4408893545882).

**To route messaging tickets as email tickets after the messaging session
ends**

- Select **Route agent-ended messaging sessions as email
  tickets**.

## Configuring omnichannel routing to route tickets based on priority

On Professional and Enterprise plans, omnichannel routing automatically considers
ticket priority if it's set. All you have to do is set a ticket's priority before it
is assigned to an agent. We recommend using triggers to automatically set the
ticket's priority when it enters the queue. This can be done with the same routing
triggers you're already using to assign groups and the routing tag, or separate
triggers.

**To use triggers to set ticket priority**

1. [Create a new trigger](https://support.zendesk.com/hc/en-us/articles/4408886797466) or [edit](https://support.zendesk.com/hc/en-us/articles/4408882237722) an existing one.
2. Add conditions to define the tickets you want to set the priority for.
3. Add an action **Ticket > Priority** and select the priority value you
   want to assign.

## Evolving your routing configuration

The standard unified agent statuses and default values for omnichannel routing
settings, such as capacity rules and reassignment timing thresholds, can provide a
good starting point if you're unsure of the right values to configure for your
organization. Whether you use the standard and default values or came up with your
own based on your research, it's likely that after you use omnichannel routing for a
while, you will find ways to start honing your configuration to improve how it works
for your organization. These changes could be identified based on feedback and
reporting data, or because something about your organization has changed and needs
to be factored in. Either way, it's good to check in on your routing configuration
periodically to ensure it's still optimized to meet your needs. For example, you
might ask yourself:

- Are your reassignment timeouts correct? If your agents often have spare
  capacity, you could try reducing these thresholds. If they are typically at
  capacity with a large queue of work waiting for an available agent, reducing
  the threshold probably isn't a great idea.
- Is your ticket prioritization working for each channel? Are any adjustments
  needed?
- Are your unified agent statuses still meeting your needs? Have you noticed
  any trends in agent productivity based on their status usage? If you aren't
  using custom agent statuses, would they be helpful to you?
- Has anything changed for you organizationally that should be reflected in
  our routing configuration, triggers, or other business rules?

When you need to adjust your routing configuration, see [Editing the routing configuration](#topic_ymt_btp_m5b).