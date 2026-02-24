# Using round robin routing for email, messaging conversations, and call tickets

Source: https://support.zendesk.com/hc/en-us/articles/7990049158554-Using-round-robin-routing-for-email-messaging-conversations-and-call-tickets

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Location:  Admin Center > Objects and rules > Omnichannel routing > Routing configuration

This article assumes omnichannel routing has been turned on for
your account. See [Turning on omnichannel routing](https://support.zendesk.com/hc/en-us/articles/5866925319962).

Omnichannel routing is a highly configurable routing solution that can route tickets from
[email (including web form, side conversations, and
API)](https://support.zendesk.com/hc/en-us/articles/4409149119514#topic_psx_hxk_3yb), calls, and messaging conversations. Agents are considered available to
receive work through omnichannel routing when they have an [eligible status](https://support.zendesk.com/hc/en-us/articles/5133523363226) and [spare capacity](https://support.zendesk.com/hc/en-us/articles/4776409839770) for the channel.

When configuring omnichannel routing, you can choose whether to assign work based on the
highest spare capacity or based on the time elapsed since agents last received work for
that channel, which is commonly referred to as *round robin*.

This article contains the following topics:

- [Understanding how round robin routing changes the standard omnichannel routing behavior](#topic_lcv_sj2_rcc)
- [Turning on round robin routing](#topic_omj_rj2_rcc)

## Understanding how round robin routing changes the standard omnichannel routing behavior

The assignment methods for omnichannel routing are straightforward on the surface:
either you're routing based on spare capacity or time since last assignment for the
channel. However, the way these methods interact with other routing configuration
options can help you make an informed decision when setting up your own omnichannel
routing workflows.

When using round robin assignment, omnichannel routing bases the round robin
assignment on the last time each available agent was assigned work for the channel
([email](https://support.zendesk.com/hc/en-us/articles/4409149119514#topic_psx_hxk_3yb), messaging, or calls). Therefore,
it's important to understand that omnichannel routing considers the following events
as assignments:

- Any ticket assignment to an agent, whether manual or by omnichannel
  routing
- A call or messaging ticket is offered to an agent
- A ticket assigned to an agent is reopened

The following examples demonstrate how each assignment method would cause omnichannel
routing to offer a messaging conversation ticket in different scenarios:

- [Scenario 1: Agents available](#topic_igm_qk2_rcc)
- [Scenario 2: No agents have spare capacity](#topic_eyw_tk2_rcc)
- [Scenario 3: Routing with focus mode turned on](#topic_qbs_5k2_rcc)

### Scenario 1: Agents available

In this scenario, there are three agents in the group, all of whom have a status
of Online.

- **Agent 1**: Has a spare capacity of 1. Was assigned a messaging
  conversation ticket 5 minutes ago.
- **Agent 2**: Has a spare capacity of 2. Was assigned a messaging
  conversation ticket 3 minutes ago.
- **Agent 3**: Has a spare capacity of 3. Was assigned a messaging
  conversation ticket 1 minute ago.

**Round robin**

If you're using the round robin method, omnichannel routing assigns the messaging
ticket to agent 1 because they've had the longest time elapsed since being
assigned a ticket for the channel. This behavior is consistent across all
channels.

**Highest spare capacity**

If you're using the standard method of highest spare capacity, omnichannel
routing assigns the messaging ticket to agent 3 because they have the most spare
capacity for the channel. This behavior is consistent across all channels.

### Scenario 2: No agents have spare capacity

In this scenario, there are three agents in the group, all of whom have a status
of Online and they are all at their maximum capacity for the messaging
channel.

- **Agent 1**: Has no spare capacity. Was assigned a messaging
  conversation ticket 5 minutes ago.
- **Agent 2**: Has no spare capacity. Was assigned a messaging
  conversation ticket 3 minutes ago.
- **Agent 3**: Has no spare capacity. Was assigned a messaging
  conversation ticket 1 minute ago.

In this scenario, omnichannel routing would behave the same way for both routing
methods. The ticket would be assigned to the first agent that drops below their
maximum capacity. This is true for all channels.

### Scenario 3: Routing with focus mode turned on

In this scenario, there are three agents in the group, all of whom have a status
of Online. Additionally, [focus mode](https://support.zendesk.com/hc/en-us/articles/4828787357210#topic_u1v_zsr_wbc) has been turned on.

- **Agent 1**: Has a spare capacity of 4. Was assigned a messaging
  conversation ticket 5 minutes ago. Is on an active call.
- **Agent 2**: Has a spare capacity of 2. Was assigned a messaging
  conversation ticket 3 minutes ago. Isn't on an active call.
- **Agent 3**: Has a spare capacity of 4. Was assigned a messaging
  conversation ticket 1 minute ago. Isn't on an active call.

**Round robin**

If you're using the round robin method with focus mode, omnichannel routing
assigns the messaging ticket to agent 2 because they've had the longest time
elapsed since being assigned a ticket for the channel while also not having an
active call. This is because focus mode prevents omnichannel routing from
assigning messaging tickets to an agent while they're working on a call and vice
versa. Email tickets are excluded from focus mode, and therefore would be routed
to agent 1 in this scenario.

Additionally, if focus mode wasn't enabled but all other factors remained the
same, omnichannel routing would assign the ticket to agent 1 because they've had
the longest time elapsed since being assigned a ticket for the channel.

**Highest spare capacity**

If you're using the standard method of highest spare capacity with focus mode,
omnichannel routing assigns the messaging ticket to agent 3 because they have
the most spare capacity for the channel while also not having an active call.
This is because focus mode prevents omnichannel routing from assigning messaging
tickets to an agent while they're working on a call and vice versa.

Email tickets are excluded from focus mode, and therefore would be routed to
agent 1 in this scenario because agent 1 and agent 3 have the same spare
capacity, but agent 1 has gone longer without being assigned work for the
channel. This would also be the behavior if focus mode was off but all other
factors remained the same.

## Turning on round robin routing

Round robin routing can be turned on in your [omnichannel routing configuration](https://support.zendesk.com/hc/en-us/articles/4828787357210).

**To turn on round robin routing**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Omnichannel routing > Routing
   configuration**.
2. On the **Routing Configuration** page, click **Edit** next
   to the Initial routing configuration.
3. Under **Assignment method**, select **Round robin**.
4. Click **Save**.