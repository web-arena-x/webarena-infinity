# Setting your agent status for Support, Messaging, and Talk with omnichannel routing 

Source: https://support.zendesk.com/hc/en-us/articles/4410545721114-Setting-your-agent-status-for-Support-Messaging-and-Talk-with-omnichannel-routing

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Tip: If you're not using omnichannel routing, see [Setting your Talk agent status](https://support.zendesk.com/hc/en-us/articles/4408829114138) and [Setting your conversation status](https://support.zendesk.com/hc/en-us/articles/6937345201562).

When [omnichannel routing](https://support.zendesk.com/hc/en-us/articles/4409149119514) is enabled for your
account, agents working in [the Zendesk Agent Workspace](https://support.zendesk.com/hc/en-us/articles/4408821259930) can set a single, unified status
across [multiple Zendesk channels](https://support.zendesk.com/hc/en-us/articles/4409149119514#topic_hhb_2xk_3yb) (Support, Messaging,
and Talk). The status set by the agent determines when and what type of tickets from
these channels can be routed to them with omnichannel routing.

Light agents can't use unified agent statuses.

This article contains the following topics:

- [About unified agent statuses](#topic_zkk_xhp_m5b)
- [Setting your status](#topic_xvw_ytp_m5b)

## About unified agent statuses

Unified agent statuses are used to inform routing behavior for tickets from
Support, Messaging, and Talk. There are four standard unified statuses for
agents:

- Online - Tickets from Talk, Messaging, and Support can be routed to
  the agent.
- Away - Only Support tickets can be routed to the agent.
- Transfer only - Only tickets that have already been reviewed and need
  to be transferred to the agent can be routed to them.
- Offline - No tickets can be routed to the agent.

On Professional and Enterprise plans, admins can create additional custom
unified statuses for agents to use. When an admin creates custom statuses, they
define one of the default statuses for each channel that will be applied when an
agent uses the custom status. For example, if an admin creates a new status called
“In meeting”, they probably don't want the most time-sensitive channels of work
routed to agents with this status. In that case, they could set Email (Support) to
online, and Messaging and Talk to away. That would result in agents with the “In
meeting” status only receiving tickets generated from Support email.

Make sure you understand how to use any custom unified statuses that are
available for you to use.

## Setting your status

Agents set a single status in the Agent Workspace for Support, Messaging,
and Talk. Before you start setting your agent status, consider the following:

- When using unified agent statuses, chat operating hours won't
  automatically set your messaging status.
- It's important that you set your status to offline before any periods of
  inactivity, such as signing off for the day. Your status is only inferred if one
  of the following events is detected:
  - An agent closes the Agent Workspace without signing out (by
    closing down their computer or browser window or putting their computer
    to sleep)
  - An agent’s connection is lost due to a network outage
  - An agent is idle for longer than the idle status threshold defined by
    admins

**To set your status**

- In the ticket interface, click your profile icon in the top bar and
  select the status you want from the profile menu.

  ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/unified_status_selection_AW.png)