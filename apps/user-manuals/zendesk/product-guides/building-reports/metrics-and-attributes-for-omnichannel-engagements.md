# Metrics and attributes for omnichannel engagements

Source: https://support.zendesk.com/hc/en-us/articles/9204180217498-Metrics-and-attributes-for-omnichannel-engagements

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Explore Professional or Enterprise |

Verified AI summary ◀▼

The omnichannel engagements dataset helps you track and analyze agent interactions across channels. It provides metrics like engagement duration and wait times, and attributes such as engagement start and end reasons. This data allows supervisors to generate detailed reports on ticket interactions, helping you understand agent performance and customer engagement dynamics without needing to navigate complex workflows.

The omnichannel engagements dataset contains metrics and attributes that relate to when
an agent is interacting with a customer within one channel. Supervisors can use this
information to create reports that give them an in-depth look at which tickets agents
have interacted with, on which channel, for how long, and why the interaction started or
ended.

This article contains the following topics:

- [What is an engagement?](#topic_yg3_bb3_2fc)
- [Omnichannel engagement metrics](#topic_cvy_hb3_2fc)
- [Omnichannel engagement attributes](#topic_prx_sb3_2fc)
- [Engagement start and end reasons](#topic_zwf_fm3_2fc)

## What is an engagement?

Engagements represent individual legs of agent interactions in the overall ticket
lifecycle. Metrics start getting measured when an agent interacts with a ticket or,
for messaging, with active conversations that have had an end-user reply in the last
10 minutes.

In this section, you'll learn about how engagements work in Zendesk analytics:

- **Retention period for open engagements:** Ongoing engagements can be
  stored for only 14 days. This means that if an engagement started longer
  than 14 days ago but has not ended, that engagement will not be recorded for
  the engagement reports. To address this, consider managing your ongoing
  workflows with [auto-release capacity setting.](https://support.zendesk.com/hc/en-us/articles/7043034053658-Automatically-releasing-agent-capacity-for-messaging-conversations)
- **Agent activities that can be reported as an engagement:** Engagement
  reporting relies on [work items](https://developer.zendesk.com/api-reference/agent-availability/agent-availability-api/work_items/) taking up capacity for
  any given agent across channels. For customers with omnichannel routing
  enabled, this changes how engagements are reported. For example:
  - When [inactive conversations count
    towards agent capacity](../routing/managing-your-omnichannel-routing-configuration.md#topic_glj_pmr_wbc)

    When this setting is
    enabled, messaging engagements will remain open and continue to
    count towards key metrics such as engagement duration.
  - When [agents switch channels from the
    composer](../../agent-guide/ticket-management/about-channel-switching-logic-in-the-ticket-composer.md), only select channel changes can be detected:
    - From messaging to voice
    - From email to voice

The following workflows cannot be tracked:

- From messaging to email (unless the agent has [ended the messaging conversation](https://support.zendesk.com/hc/en-us/articles/8009788438042)
  and the admin has the "transform to email" setting enabled).
- From voice to email

For these workflows, the following channel engagement will continue
counting towards the latest engagement detected.

## Omnichannel engagement metrics

This section lists and defines all of the engagement metrics available.

|  |  |  |
| --- | --- | --- |
| **Metric** | **Definition** | **Calculation** |
| Engagement duration | Time from the start of engagement to the end of engagement. | VALUE(Engagement End time - Engagement Start time) |
| Engagement - Offer time to agent | Time from when the ticket was offered to the agent that eventually accepted the assignment to when the agent accepted the assignment. | VALUE(Latest accepted time - Latest offered time) |
| Engagement - Assignment to first reply | Time from assignment to agent’s first response. This will exclude offer state and engagements outside of business hours. If a ticket is reopened, this counts as a new assignment. | VALUE(Agent first message time - Ticket assignment time) |
| Agent messages | Number of messages sent by an agent during an engagement. | COUNT(Agent interactions) |
| Engagement - Average requester wait time | The average time between an end user response and the agent’s reply during the engagement. | SUM(Total Response Time on Active Assigned Conversation) / COUNT(Agent replies on Active Assigned Conversations) |
| Engagement - Longest requester wait time | The longest time between an end user response and the agent’s reply during the engagement. | MAX(Response Time on Active Assigned Conversations) |
| Engagement start reason | The reason an engagement started. | N/A |
| Engagement end reason | The reason an engagement ended. | N/A |
| Ticket status - Start of engagement | The status assigned to the ticket at the start of the engagement. | N/A |
| Ticket status - End of engagement | The status assigned to the ticket at the end of the engagement. | N/A |

## Omnichannel engagement attributes

This section lists and defines all the engagement attributes available.

|  |  |
| --- | --- |
| **Attribute** | **Definition** |
| Engagement ID | The system ID of the engagement. |
| Ticket ID | The system ID of the ticket. |
| Agent ID | The ID of the agent. |
| Channel | The channel through which the agent and end user are interacting. Values are messaging or support. |
| Group ID | The ID number of the group. |
| Requester ID | The ID number for a ticket's requester. |
| Engagement start reason | The reason an engagement started. See [Engagement start reasons](#topic_z3t_hm3_2fc). |
| Engagement end reason | The reason an engagement ended. See [Engagement end reasons](#topic_etw_3m3_2fc). |
| Ticket Status - Start | The ticket’s status at the start of the engagement. |
| Ticket Status - End | The ticket’s status at the end of the engagement. |
| Start Time of engagement | Timestamp of when the engagement started |
| End Time of engagement | Timestamp of when the engagement ended |

## Engagement start and end reasons

The engagements dataset provides engagement start and end reason attributes
to show how and why an interaction with an agent started and ended.

### Engagement start reasons

|  |  |
| --- | --- |
| Reason | Event |
| Routing assignment accepted | This happens when:  - The agent has been assigned a ticket from the   routing engine. - The agent accepts an offered assignment. - The agent accepts an offered assignment from a   group or a queue transfer. |
| Assigned | The agent as a sole agent in a group is assigned a ticket. |
| Manual assignment | This happens when:   - The agent manually assigns themselves a new   ticket. - A supervisor manually assigns the agent a new   ticket. |
| Reopened | The agent changes the status from Pending, On-hold, or Solved to Open. |
| Transferred | The agent is a recipient of a transferred messaging ticket. |

### Engagement end reasons

|  |  |
| --- | --- |
| Reason | Event |
| Inactivity timeout | The messaging ticket becomes inactive when an end user hasn’t sent a reply in the last 10 minutes. Note: If you've turned on omnichannel routing, and [messaging activity routing](../routing/managing-your-omnichannel-routing-configuration.md#topic_glj_pmr_wbc) is turned on, the engagement will not end when the ticket becomes inactive. |
| Agent closed conversation | The agent ends the messaging session. This is only available when you [allow agents to end messaging sessions](https://support.zendesk.com/hc/en-us/articles/8009788438042-Allowing-agents-to-end-messaging-sessions). |
| Transferred | The agent transfers the ticket to another agent or group. |
| Ticket status updated - Pending/On Hold | The agent changes the status from Open to Pending or On-hold. |
| Ticket status updated - Solved | The agent changes the status from Open to Solved. |