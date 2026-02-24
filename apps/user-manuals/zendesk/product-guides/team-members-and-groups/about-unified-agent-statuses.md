# About unified agent statuses

Source: https://support.zendesk.com/hc/en-us/articles/5133523363226-About-unified-agent-statuses

---

Unified agent statuses are part ofomnichannel routingand provide a way for agents to control availability for email, voice, and messaging from a single menu. In addition to the standard unified agent statuses available on all plans, admins on Professional plans and above can also define custom unified agent statuses to suit their workflows.

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Location:  Admin Center > Objects and rules > Omnichannel routing > Agent statuses

Unified agent statuses are part of [omnichannel routing](https://support.zendesk.com/hc/en-us/articles/4409149119514) and provide a way for agents to control
availability for email, voice, and messaging from a single menu. In addition to the
standard unified agent statuses available on all plans, admins on Professional plans and
above can also define custom unified agent statuses to suit their workflows.

Unified agent statuses are automatically available to accounts that meet the [requirements](#topic_zvv_bjt_nvb).

This article contains the following topics:

- [About the standard unified agent statuses](#topic_vrd_ld1_4vb)
- [Considerations for unified agent status](#topic_h3t_zc1_4vb)
- [Related articles](#topic_uq2_bxg_4vb)

## About the standard unified agent statuses

Unified agent statuses are used to inform omnichannel routing behavior for
tickets from [email (including web form, side conversations,
and API)](https://support.zendesk.com/hc/en-us/articles/4409149119514#topic_psx_hxk_3yb), calls, messaging conversations, and [sometimes Chat](https://support.zendesk.com/hc/en-us/articles/6249962577690). Agents set their unified status manually
and need to adjust it throughout the day to accurately reflect their availability to
receive work. These standard statuses are the basis for custom agent statuses,
too.

There are four standard agent statuses:

- Online - Tickets from email, calls, messaging conversations, and [sometimes Chat](https://support.zendesk.com/hc/en-us/articles/6249962577690) can be routed to the
  agent.
- Away - Only email tickets can be routed to the agent.
- Transfer only - Only tickets that have already been reviewed and need
  to be transferred to the agent can be routed to them.
- Offline - No tickets can be routed to the agent.

### Modifying an agent's status

In most situations, an agent's status is set manually by the agents
themselves. They are encouraged to change their status to offline before any
breaks. However, when one of the following disconnection events is detected, an
agent is automatically set to *offline*:

- An agent closes the Agent Workspace without signing out (by
  closing their browser window, shutting down their computer, or putting their
  computer in sleep mode)
- An agent’s connection is lost due to a network outage

Additionally, admins can configure the account to automatically adjust an agent's
status to *offline* or *away* when they are idle for longer than the
[idle timeout
threshold](https://support.zendesk.com/hc/en-us/articles/5286614817562).

## Considerations for unified agent status

Consider the following information before enabling and using omnichannel routing and
unified agent status.

### Requirements

Your account must meet the following requirements to use unified agent status and
omnichannel routing:

- The [Agent Workspace](https://support.zendesk.com/hc/en-us/articles/4408821259930) must be
  activated for your account.
- If your account has a Chat subscription, native messaging or Sunshine
  Conversations must also be activated.
- Limited support for Chat is provided for accounts [migrating to Messaging and
  omnichannel routing](https://support.zendesk.com/hc/en-us/articles/6249962577690).

### Limitations

The following limitations currently exist for unified agent status in
omnichannel routing:

- Operating hours won't set an agent's status.
- After you turn on omnichannel routing, you can no longer set agent
  status for voice support from the Talk dashboard, mobile apps, or Talk APIs.
  Integrations that use Talk APIs to change agent statuses might also be
  impacted.
- If call forwarding is enabled and the status of an agent is
  automatically set to offline because the agent has been disconnected, calls
  to the agent will no longer be forwarded to the agent's phone.
- When omnichannel routing is activated, agents are automatically set to
  offline across all channels. When this happens, they are prompted to set a
  new status. Ongoing live conversations aren't interrupted, but calls waiting
  in the queue will be directed to voicemail.
- Based on your plan, there are limits to the number of custom agent
  statuses you can create:
  - Team and Growth: You cannot create custom statuses
  - Professional: 5 custom statuses
  - Enterprise: 100 custom statuses
- Agents working on tickets won't see changes to [status timeout rules](https://support.zendesk.com/hc/en-us/articles/5286614817562) until they
  refresh the page.

### Using unified agent statuses with Zendesk Workforce Management

Unified agent statuses data can be synchronized with Zendesk Workforce Management
(WFM). When this is configured, WFM calculates adherence and activities based on
unified agent statuses rather than general tasks. Admins can map unified agent
statuses to workstreams. Synchronizing unified agent status data with WFM also
allows agents to set their status once, in the Agent Workspace, rather than
needing to maintain it in two systems. For more information, see [Turning on unified agent status
synchronization for Zendesk WFM](https://support.zendesk.com/hc/en-us/articles/10114746509978).

## Related articles

See the following articles for more information to help you get up and
running with unified agent statuses:

- [Creating custom unified agent
  statuses](https://support.zendesk.com/hc/en-us/articles/4410525357594)
- [Managing unified agent statuses](https://support.zendesk.com/hc/en-us/articles/5133588225690)
- [About omnichannel routing with unified agent
  status](https://support.zendesk.com/hc/en-us/articles/4409149119514)