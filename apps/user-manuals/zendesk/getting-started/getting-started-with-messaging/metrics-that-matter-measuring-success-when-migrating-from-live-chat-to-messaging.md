# Metrics that matter: Measuring success when migrating from live chat to messaging

Source: https://support.zendesk.com/hc/en-us/articles/6330405002906-Metrics-that-matter-Measuring-success-when-migrating-from-live-chat-to-messaging

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

When you migrate from live chat to messaging, one area to think about is how you’ll use Explore to measure the success of your messaging implementation. With a little preparation, you can limit the amount of change introduced by the migration while still enjoying all the benefits afforded by messaging.

This article walks you through several important reporting considerations related to messaging, including how the conversation style you choose affects your metrics, which metrics to consider when defining success, and when to use real-time monitoring versus historical reporting.

This article contains the following topics:

- [Understanding how messaging conversation styles affect metrics](#topic_d5x_2k4_hzb)
- [Defining success for the "live chat" conversation style](#topic_phz_gk4_hzb)
- [Using real-time and historical data to measure success](#topic_rhl_mk4_hzb)

Related articles:

- [Migrating from live chat to messaging](https://support.zendesk.com/hc/en-us/articles/4408821531162)
- [Analyzing your messaging tickets](https://support.zendesk.com/hc/en-us/articles/4724610509082)

## Understanding how messaging conversation styles affect metrics

During the migration to messaging, one of the main decisions you’ll make is which messaging conversation styles you want to implement. The conversation styles you choose will have an effect on the Explore metrics you use in your reports.

The table below summarizes the different messaging conversation styles and how metrics are affected.

| **Conversation style** | **Description** | **How metrics are affected** |
| --- | --- | --- |
| “Live chat” | A single live interaction with a clear start and end. This is the most Chat-like experience, where the messaging ticket is solved and automatically closed after the interaction. Zendesk recommends choosing this style for your initial messaging migration, and, if appropriate, later migrating to one of the styles below. You might choose not to migrate at all, or you might choose to support multiple styles. | Because the “live chat” style is so closely related to the way legacy live chat works, the metrics you use to measure live chat have direct comparisons with messaging. For example, you should still have low first reply times and high first contact resolutions. For details, see [Defining success for the “live chat” conversation style](#ariaid-title3). |
| Reopened | Multiple live interactions. This is similar to the live chat conversation style with the exception that after the initial live interaction, the agent places the ticket in a solved state. The ticket remains in this state for a period of time to allow the customer to return to this conversation with the same agent, rather than having to open a new chat, wait in queue again, and likely have their chat assigned to a different agent. | Because the reopened style allows for tickets to be reopened, you can expect inflated metrics related to the ticket lifecycle (such as Requester Wait Time or Full Resolution Time) when compared to legacy live chat. These inflated metrics don’t necessarily indicate poorer performance, as a single reopened ticket in this context would have been two separate chats in the legacy live chat experience. |
| Asynchronous | Multiple live and non-live interactions. The customer interacts with the same or different agents over a longer period of time. The ticket lifecycle extends until the customer has fully been served, which can be days or weeks. | Because the asynchronous style takes place over a longer period of time and can include waiting for the customer to respond, metrics related to the ticket lifecycle (such as Requester Wait Time or Full Resolution Time) are less likely to be reliable indicators for staffing or forecasting. The prebuilt Zendesk Messaging dashboard includes reports that are designed to help you monitor agent performance and customer satisfaction for this conversation style. See [Analyzing your messaging tickets](https://support.zendesk.com/hc/en-us/articles/4724610509082). |

## Defining success for the "live chat" conversation style

As mentioned above, the metrics you’re used to measuring for live chat often have direct comparisons for the “live chat” style of messaging because of the similarities between these two approaches.

Even so, there are different metrics you can analyze in Explore depending on which outcome is most important to your organization: handling volume, fine-tuning the customer experience, or improving agent performance.

This section compares legacy chat metrics in each of these three areas with their equivalent messaging metrics. This comparison allows you to better evaluate how the migration from chat to messaging is working for your business.

### Metrics for monitoring volume

The table below lists the volume-based metrics for legacy chat compared to the equivalent metrics for the “live chat” messaging conversation style.

| **Legacy chat metric** From the [Engagement dataset](https://support.zendesk.com/hc/en-us/articles/4409149177242#topic_r34_grl_mfb) | **Equivalent messaging metric** From the [Messaging tickets dataset](https://support.zendesk.com/hc/en-us/articles/4724624097818) |
| --- | --- |
| **Chats** The number of chat sessions. | **Messaging tickets** The total number of tickets created from messaging channels. |
| **Completed chats** The number of chat sessions successfully completed by agents (excludes agent-dropped and missed chats). | **Solved tickets** The number of solved or closed messaging tickets. |
| **Missed inbound chats** The number of inbound chat sessions where the visitor ends the chat without an agent response. The inbound chat sessions are initiated by visitors (end users). | **Unreplied unsolved messaging tickets** The number of unsolved messaging tickets that currently have no agent replies. Filter by a Status of New. |
| **Dropped chats** The number of chats accepted by or assigned to the agent where the visitor responds to an agent message, then leaves the chat. | Messaging doesn’t have a direct comparison to dropped chats, as conversations can be resumed later. Instead, consider measuring “stale” conversations, where you look at messaging tickets that have been in a Pending status for longer than a day or week. |
| **Transferred chats** The number of chats that were transferred to other departments or agents. | **Reassigned messaging tickets** The number of messaging tickets that have been assigned to more than one agent. |
| **Offline messages** The number of offline messages left when no agents were online. | **Messaging tickets created outside of business hours** The number of messaging tickets created outside of the schedule assigned at the time of ticket creation. |

### Metrics for monitoring the customer experience

The table below lists the customer experience–based metrics for legacy chat compared to the equivalent metrics for the “live chat” messaging conversation style.

| **Legacy chat metric** From the [Engagement dataset](https://support.zendesk.com/hc/en-us/articles/4409149177242#topic_r34_grl_mfb) | **Equivalent messaging metric** From the [Messaging tickets dataset](https://support.zendesk.com/hc/en-us/articles/4724624097818) |
| --- | --- |
| **% Chat satisfaction score** The percentage of chat sessions rated by the visitor as good from the total number of rated chats. | **Good satisfaction tickets** The number of messaging tickets with a good satisfaction rating. |
| **Chat duration (sec)** The time duration from the first to the last chat message in seconds. | **Full resolution time (min)** The duration in minutes from when the messaging ticket was created to its latest resolution. (This assumes messaging tickets are solved and closed after engagement completion.) |
| **Chat wait time (sec)** The time the end user waited for the first reply from an agent. If no agent replies, then this returns the total time the end user waited before leaving the chat session. | **First reply time (sec)** The duration in seconds between when the messaging ticket was created and the first agent reply on the ticket. |
| **Chat first reply time (sec)** The time in seconds between the customer joining the chat and the agent's first response. | **First reply time (sec)** The duration in seconds between when the messaging ticket was created and the first agent reply on the ticket. |
| **Chat average reply time (sec)** The average time in seconds it took for an agent to reply to visitor comments during the chat session. | **Requester wait time average (sec)** The average time in seconds from the end user sending a message and the agent’s response. |
| **Chat agent messages** The number of comments entered by an agent during the chat session. | **Agent messages** The number of messages sent by the agent. |
| **Chat visitor messages** The number of comments submitted during the chat session by the visitor (end user). | **Requester messages** The number of messages sent by the requester. |

### Metrics for monitoring agent performance

The table below lists the agent performance–based metrics for legacy chat compared to the equivalent metrics for the “live chat” messaging conversation style.

| **Legacy chat metric** From the [Engagement dataset](https://support.zendesk.com/hc/en-us/articles/4409149177242#topic_r34_grl_mfb) | **Equivalent messaging metric** From the [Messaging tickets dataset](https://support.zendesk.com/hc/en-us/articles/4724624097818) |
| --- | --- |
| **Assignments** The number of engagements which were assigned to agents. During a chat session, an end user can interact with multiple agents. Each interaction is counted as a different engagement. | **Assignee stations** The number of agents a ticket has been assigned to. |
| **% Chat satisfaction score** The percentage of chat sessions rated by the visitor as good from the total number of rated chats. | **Good satisfaction tickets** (the number of messaging tickets with a good satisfaction rating) divided by **Rated satisfaction tickets** (the number of messaging tickets that were rated either bad or good by the requester). |
| **Chat wait time** The time the end user waited for the first reply from an agent. If no agent replies, then this returns the total time the end user waited before leaving the chat session. | **Assignment to first reply (sec)** The time in seconds from last assignment to the first agent reply. |
| **Engagement duration (min)** The time in seconds from the agent joining the chat to when the visitor or agent leaves the chat, whichever occurs first. During a chat session, the end user can interact with multiple agents. Each interaction is counted as a different engagement. | **Handle time (min)** The time in minutes that the agent spends interacting with the end user on the messaging ticket. For details, see [How is the Handle time metric calculated?](https://support.zendesk.com/hc/en-us/articles/5940001113754) |
| **Chat average reply time (sec)** The average time in seconds it took for agent to reply to visitor comments during the chat session. | **Requester wait time average (sec)** The average time in seconds from the end user sending a message and the agent’s response. |
| **% Assignment acceptance rate** The percentage of assignments which were assigned and accepted by an agent to the total number of agent assignments. | The volume of tickets compared to how many tickets an agent was assigned to (compared against the team as well as their personal historical performance). |

## Using real-time and historical data to measure success

On Professional plans and above, you have access to real-time data in addition to historical reporting data. Using a mix of real-time and historical data gives you an even fuller picture of your success with messaging.

### When to use real-time monitoring (Professional and above)

Regardless of the messaging conversation style you choose, you can use real-time data to identify the current volume of tickets in the queue and, if you’ve activated [omnichannel routing with unified agent status](https://support.zendesk.com/hc/en-us/articles/4409149119514), current agent status and capacity.

Use real-time monitoring when you want to answer questions such as:

- What are my agents currently working on?
- What status are my agents in right now?
- How big is my backlog at the moment?
- What is the state of my operations?
- Do I have sufficient staffing to address the queue?
- Am I providing a good customer experience?
- What’s my current customer sentiment?

For more on real-time monitoring of messaging metrics, see the following articles:

- [Overview of the Explore live dashboard](https://support.zendesk.com/hc/en-us/articles/4408843771546)
- [Seeing live agent status and activities](https://support.zendesk.com/hc/en-us/articles/4422485166746)
- [Live data widgets for Explore dashboards](https://support.zendesk.com/hc/en-us/articles/4408843357210#topic_mq4_yxb_n4b)

### When to use historical data

Historical data, like the metrics presented in the previous section, allows you to analyze ticket and agent data after conversations have been handled. Data can be analyzed at various levels of granularity to identify your team’s performance against expectations, as well as to identify opportunities for improvement.

Use historical reporting when you want to answer questions such as:

- What is my average first reply time?
- When was my peak ticket volume last week?
- How did my peak volume affect my agents’ first reply times?

For more on historical reporting for messaging tickets, see the following articles:

- [Analyzing your messaging tickets](https://support.zendesk.com/hc/en-us/articles/4724610509082)
- [Metrics and attributes for Zendesk messaging](https://support.zendesk.com/hc/en-us/articles/4724624097818)