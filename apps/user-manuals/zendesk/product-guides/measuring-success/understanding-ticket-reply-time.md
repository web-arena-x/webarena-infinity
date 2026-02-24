# Understanding ticket reply time

Source: https://support.zendesk.com/hc/en-us/articles/4408821871642-Understanding-ticket-reply-time

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

When you use Zendesk to support customers, a question that people commonly ask is “How long does it typically take for one of my agents to respond to a ticket after it’s first created?”

Zendesk Support records the time from when a ticket was created to the first *public* agent response. Zendesk Explore reads this value and makes it available in a metric named **First reply time**.

Note: All Support plans record first reply times. The method you use to interact with these depends on your Support plan and are typically available on Support Professional and Enterprise only.

This article describes how first reply time works and how you can use it in your reports.

This article contains the following sections:

- [How first reply time is calculated](#topic_jvw_nqd_1hb)
- [Reporting first reply time](#topic_etg_4qd_1hb)
- [Zendesk SLAs and first reply time](#topic_hxr_pqd_1hb)

Related article:

- [Tips for lowering first reply time](https://support.zendesk.com/hc/en-us/articles/4409148782234)

## How first reply time is calculated

The Zendesk first reply time metric measures the time between ticket creation and the first public agent comment after that.

After the first public reply, the system calculates the first reply time in calendar hours and business hours. Both metrics are stored with the ticket data, so you can use either (or both) to build reports.

First reply time works essentially the same way regardless of the channel from which the ticket originated. For example:

- A customer email creates a ticket. Timing starts when the ticket is created and ends at the first public agent comment.
- An agent creates a ticket. Timing starts when the ticket is created and ends at the agent's *next* public comment.
- An agent takes a phone call that creates a ticket and solves the ticket with no new comment. The customer later re-opens the ticket, and the agent then responds with a public comment. First reply time ends when that comment is posted.

When an agent adds a public comment from another account using ticket sharing, this doesn't count toward your account's first reply time.

### Additional details for messaging and live chat first reply time

Note: Live chat users must [activate reply time SLAs](https://support.zendesk.com/hc/en-us/articles/6670155267994) to track chat reply time. Reply time SLAs are turned off by default.

First reply time is calculated exclusively based on agent replies.
That means automated or bot-related actions in conversations aren’t considered when calculating the first reply time. Across all channels, ticket creation starts the first reply timer. Live conversation channels are no exception. However, because public replies aren’t an agent response option for live chat and messaging tickets, the actions that stop the timer are different:

- **On messaging tickets**, the timer stops when the agent clicks **Send** on their first Messaging reply to the conversation.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/messaging_response_option-AW.png)
- **On live chat tickets with reply-time SLAs turned on**, the timer stops when the agent clicks **Send** on their first comment in the conversation.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_chat_start_ticket3.png)

Messaging and live chat tickets also have an additional metric:
First reply time (sec). This metric is often a more accurate measure of first reply times for tickets from live conversations, which tend to move more quickly than tickets from other channels. Unlike the standard First reply time metrics, the First reply time (sec) metric ignores your [messaging business hours](https://support.zendesk.com/hc/en-us/articles/4500737327258#topic_nxy_njd_btb) and [live chat operating hours](https://support.zendesk.com/hc/en-us/articles/4408822398106) settings.

## Reporting first reply time

The following sections describe how to use the Zendesk reporting tools to read first reply time information.

### Reporting using Explore

Explore reads first reply time information from Support. The reports:

- Read data from Support using the Zendesk API.
 They do not calculate calendar hours or business hours.
- Display information on pre-built reports in calendar hours. However, metrics for business hours are available and can be used in your own reports.

See [Metrics and attributes for Zendesk Support](https://support.zendesk.com/hc/en-us/articles/4408827693594), [Metrics and attributes for Zendesk messaging](https://support.zendesk.com/hc/en-us/articles/4724624097818), and [Metrics and attributes for live chat](https://support.zendesk.com/hc/en-us/articles/4409149177242).

### Reporting using External analytic tools

If you're not using any Zendesk reporting methods, you can still read first reply time information using the Zendesk API. The first reply time information in calendar hours is stored together with the first reply time in business hours and clearly labelled. See [API metrics documentation](https://developer.zendesk.com/rest_api/docs/support/ticket_metrics).

## Zendesk SLAs and first reply time

Important: The first reply time metric described in this article and a SLA first reply time metric both use the first reply time, but work in different ways. If you want to use SLA times, make sure you review the information in this section first.

A service level agreement, or SLA, is a policy you define that specifies and measures the response and resolution times that your support team delivers to your customers. To determine these times, your SLA policies may also use the first reply time metric.

Note: The SLA reply time metric may behave differently than the standard behavior described in this article if advanced SLA settings were configured for a policy. See [Customizing your SLAs with advanced settings](https://support.zendesk.com/hc/en-us/articles/7412192349466).

However, there are differences in the way that the first reply time metric work with SLAs:

- If a ticket is created with a public comment from an agent, the SLA first reply time target is not run.
- If a ticket is created with a private comment, the SLA first reply time target will not start until the ticket gets a first public comment from an end user.

 An exception to this rule is that if the requester is a light agent, the first reply time SLA target starts at creation even without a public comment.
- SLA first reply time targets are fulfilled when a ticket is solved, even if the ticket never had a public comment from an agent.
- SLA targets can be run in calendar or business hours, but not both.
- Business hour SLA targets pause outside business hours, then restart when business hours begin.

For more information, see [Defining SLA policies](https://support.zendesk.com/hc/en-us/articles/4408829459866).