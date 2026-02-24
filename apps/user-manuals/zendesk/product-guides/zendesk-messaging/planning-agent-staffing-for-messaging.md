# Planning agent staffing for messaging

Source: https://support.zendesk.com/hc/en-us/articles/4408846612250-Planning-agent-staffing-for-messaging

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

In this article, we’ll discuss some common questions you should ask yourself before building a team to cover incoming messaging requests, basic staffing models, and the Zendesk features that can help you determine the best way to organize your agents for messaging.

This article includes the following topics:

- [Estimating agent staffing needs](#topic_jld_fgb_rqb)
- [Managing customer support expectations](#topic_bsg_1kb_rqb)
- [Considerations when migrating from live chat to messaging](#topic_gjv_2gb_rqb)

## Estimating agent staffing needs

Each organization has its own set of support requirements and will consequently have different staffing needs. The list below includes issues you might consider when determining the number of agents required for messaging support.

The list below includes issues you might consider when determining the number of agents required for messaging support.

- **Number of visitors**. How many visitors (to your website or help center, for example) do you expect during the period that agents are available?
- **Agent availability period**. How many hours in the day will agents be available to serve messaging requests?
- **Average conversation duration**. How long do you expect agents to spend on a single conversation (in mins)?
- **Concurrent conversations**. How many conversations will an agent serve simultaneously?

Answering the questions above can help you determine how many agents you need. For instance:

- Number of visitors: 10,000
- Agent availability period: 8 hours
- Average conversation duration: 12 mins
- Concurrent conversations: 4

Based on this, we can estimate that:

- You’ll receive 1,000 support requests a day (10% of visitors, which is a conservative estimate, and includes requests made outside of staffed hours)
- That translates to 125 requests per hour (1000 requests per day divided by the 8 hour agent availability period)

So in this scenario, you’d need 6.25 agents. (25 agents can serve 125 requests per hour at 12 minutes per conversation. 6.25 agents can solve that number if they serve 4 conversations at a time.)

Keep in mind that the above formula is merely a guide and ignores things like breaks for your agents, multiple shifts, and vastly different customer requirements.

## Managing customer support expectations

It’s a good idea to set expectations with your customers on when agents will be available. There are a few ways you can accomplish this in messaging.

- [Use out-of-office notifications](#topic_qqw_fkb_rqb) to inform customers when agents are unavailable.
- [Enable continuous conversations](#topic_y3b_gkb_rqb) to allow customers to send a request, then leave the conversation and receive a notification when an agent has responded.

### Using out-of-office notifications

You can create an automated out-of-office message, shown to your customers when your agents are offline, using a [Chat trigger](https://support.zendesk.com/hc/en-us/articles/4408884148762).

This message is displayed to any customer opening the Web Widget to begin (or continue) a conversation, when all agents are offline. It can include your business hours or any other helpful information.

See [Creating an out-of-office response for messaging](https://support.zendesk.com/hc/en-us/articles/4408842866074) for more information.

### Using continuous conversations

Continuous conversations functionality allows you to automatically send an email notification to customers who abandon a conversation conducted through the web messaging channel, encouraging them to re-engage with your agents through their preferred channel. This is useful when agents are unavailable to serve a customer support request because they are offline, or are busy handling other requests.

See [Enabling customers to continue their conversation over email](https://support.zendesk.com/hc/en-us/articles/4408829095706) for more information.

## Considerations when migrating from live chat to messaging

Staffing needs for messaging look a little different than those for live chat. Messaging can be synchronous, with clear starting and ending points, *or* asynchronous, which means that there’s no start and end to a conversation. Asynchronous messaging conversations require you to plan differently than for a synchronous channel like live chat.

One difference you’re likely to notice is in the volume and timing of incoming support requests.

- **Live chat requests** are *session-based* and *synchronous*. They require a live agent for resolution, so incoming chat requests are typically limited to your business hours, when agents are online and available.
- **Messaging requests** are *persistent* and can be *asynchronous* or *synchronous*. They can potentially be resolved by built-in automations, so messaging volume can start before your business hours and continue after they end.

Because messaging volume doesn’t tend to see the same peaks and valleys that live chat does, it’s important to strategize your staffing model based on the volume you’re seeing, and reset customer expectations, such as with set office hours. See [Managing customer support expectations](#topic_bsg_1kb_rqb) for more information and suggestions.