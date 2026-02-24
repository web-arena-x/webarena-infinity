# About native Support time duration metrics

Source: https://support.zendesk.com/hc/en-us/articles/4408834848154-About-native-Support-time-duration-metrics

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Explore Professional or Enterprise |

In this article, you'll learn more about some of the metrics built into Zendesk Support that help you measure the duration between two events.

Note: This article covers only the native Support metrics. SLA metrics might have identical names but their behavior is different because they are live counters. See: [Defining and using SLA policies](https://support.zendesk.com/hc/en-us/articles/4408829459866-Defining-and-using-SLA-policies-Professional-and-Enterprise-#topic_gpr_ppv_tr).

For more information about the metrics and attributes you can use with Explore, see [Understanding Explore datasets](https://support.zendesk.com/hc/en-us/articles/4408839218842-Metric-and-attribute-reference).

The native duration metrics are not live counters, instead, they measure time duration between specific events. Support computes the time difference between two event timestamps and adds the results with the following behaviors:

- The new metric value is recorded on the ticket only after the specific events take place.
- The metric’s value will appear as null until two required events occur at least once.

This article contains the following topics:

- [First reply time](#h_b9d9e012-c734-4ec8-ad9e-db20a9a7ac19)
- [First resolution time](#h_dda6899c-5c6b-48b8-b364-ab9a973ed971)
- [Full resolution time](#h_6074d102-0734-4fce-b9d4-b687f96a56fd)
- [Requester wait time](#h_fd75857f-1dc5-4aa4-bb9c-b58ba2078617)
- [Agent wait time](#h_82473d55-2c4c-451b-9da2-0fbd274b312c)
- [On-hold time](#h_c920c1a1-6528-4179-864e-a39e46b98d0a)

Tip: In the graphics below, green indicates time counted and gray indicates time not counted.

## First reply time

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/FRT.png)

- **Definition:** The duration between ticket creation and the first public agent reply on the ticket.
- **First timestamp:** Ticket creation.
- **Second timestamp:** The first public comment by any agent.
- **Exceptions:**  If the ticket is created by an agent and the first comment is public the second timestamp shifts to the second public agent comment. If the ticket is created via private [sharing agreement](https://support.zendesk.com/hc/en-us/articles/4408893967514-Sharing-tickets-with-other-Zendesk-Support-accounts), the first private note by any agent will be considered as the second timestamp. For more details see: [Calculating first reply time](https://support.zendesk.com/hc/en-us/articles/4408821871642-Calculating-first-reply-time-Professional-and-Enterprise-)

## First resolution time

### FResT.png

- **Definition:**Duration between ticket creation and its first resolution.
- **First timestamp:** Ticket creation.
- **Second timestamp: The first time the**ticket status is set to solved.
- **Exceptions:**  If the unsolved ticket is set to closed by a business rule or API, this event is considered as the second timestamp.

## Full resolution time

![FulResT.png](https://support.zendesk.com/hc/article_attachments/7856671597850)

- **Definition:**Duration between ticket creation and its most recent resolution.
- **First timestamp:** Ticket creation.
- **Second timestamp: The last time the**ticket status was set to solved.
- **Exceptions:**  If the unsolved ticket is set to closed by a business rule or API, this event is considered as the second timestamp.

## Requester wait time

![](https://support.zendesk.com/hc/article_attachments/7856671596314)

- **Definition:**The total combined time ticket was in the new, open, and on-hold statuses.
- **First timestamp:** Ticket status is changed to new, open, or on-hold.
- **Second timestamp: Ticket status is changed from new, open, or on-hold to any other status.**

## Agent wait time

![](https://support.zendesk.com/hc/article_attachments/7856626606618)

- **Definition:**The total combined time the ticket was in the pending status.
- **First timestamp:** Ticket status is changed to pending.
- **Second timestamp: Ticket status is changed from pending to any other status.**

## On-hold time

![](https://support.zendesk.com/hc/article_attachments/7856626605594)

- **Definition:**The total combined time the ticket was in the on-hold status.
- **First timestamp:** Ticket status is changed to on-hold.
- **Second timestamp: Ticket status is changed from on-hold to any other status.**