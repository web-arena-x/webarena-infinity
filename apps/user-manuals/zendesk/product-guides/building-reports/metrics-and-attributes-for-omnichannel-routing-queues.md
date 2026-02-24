# Metrics and attributes for omnichannel routing queues

Source: https://support.zendesk.com/hc/en-us/articles/9046662025498-Metrics-and-attributes-for-omnichannel-routing-queues

---

All Suites | Professional, Enterprise, or Enterprise Plus

Support with | Explore Professional or Enterprise

The omnichannel routing queues dataset contains metrics and attributes that
relate to how agents are assigned new and open tickets from email (including web form,
side conversations, and API), calls, and messaging.

Consider the following when you use this dataset:

- You must be using [omnichannel routing queues](https://support.zendesk.com/hc/en-us/articles/6716530152858) to use the
  dashboard described in this article.
- Currently, call tickets are not captured by the omnichannel routing queues dataset.

This section lists all the available elements for the dataset, and contains the
following topics:

- [Queue metrics](#topic_spn_rm2_t2c)
- [Queue attributes](#topic_wbg_5m2_t2c)

## Queue metrics

This section lists and defines all of the queue metrics available.

These metrics capture ticket interactions with a queue at the point in time
the event occurs.

|  |  |  |
| --- | --- | --- |
| **Metric** | **Definition** | **Calculation** |
| Inbound traffic count | The total number of tickets that have entered a queue. | D\_COUNT(Work Item ID entering the queue) |
| Outbound traffic count | The total number of tickets that have exited a queue. | D\_COUNT(Work Item ID exiting the queue) |
| Net new work items traffic count | The number of newly created tickets that entered a queue. | IF [Ticket status - Unsorted] = “New” THEN [Work Item ID] ENDIF |
| Transferred in traffic count | The number of tickets transferred into the queue from a different queue or workflow that places a previously routed ticket back into a queue. | IF [Had previously been assigned to a custom queue] THEN [Work Item ID] ENDIF |
| Transferred out traffic count | The number of tickets transferred out of the queue from a different queue or workflow that places a previously routed ticket back into a queue. | IF [Had previously been assigned to a custom queue] THEN [Work Item ID] ENDIF |
| Queue wait time | The duration in seconds that a ticket spent in the queue. | Time ticket exited the queue - Time ticket entered the queue |

## Queue attributes

This section lists and defines all the queue attributes available.

|  |  |
| --- | --- |
| **Attribute** | **Definition** |
| Queue ID | The ID number of a configured custom queue. |
| Queue name | Name of the custom queue. |
| Queue order | The assigned order value in which configured queues are evaluated to route any ticket. |
| Group ID | The ID number of a Support group that has been assigned to the custom queue. |
| Group name | Name of the group that has been assigned to the custom queue. |
| Group type | Type of queue group - Primary or Secondary. |
| Channel | The channel by means customers create support requests. |
| Work item ID | The ID number of a work item. A work item is a ticket that would be assigned to an agent for a particular channel. |
| Ticket ID | The ID number of the ticket. |
| Call ID | The ID number of a call.  As calls are not currently supported, querying this attribute will yield empty results. |
| Inbound Reason | The reason a ticket had entered a queue. |
| Outbound Reason | The reason a ticket had exited a queue. |
| Start queue time | The time at which the ticket entered the queue. |
| End queue time | The time at which the ticket exited the queue. |
| Event time | The time at which the ticket was last processed by omnichannel routing queue activities. |

## Queue inbound and outbound reasons

The omnichannel routing queues dataset provides inbound and outbound
reasons to show how and why a ticket entered or exited the queue.

**Inbound reasons**

|  |  |
| --- | --- |
| **Reason** | **Description** |
| New | Describes newly created tickets entering the queue. |
| Transferred in | Describes tickets that have entered the queue as a result of a queue transfer or other workflows. |

**Outbound reasons**

|  |  |
| --- | --- |
| **Reason** | **Description** |
| Transferred Out | Describes tickets that have exited the queue as a result of a queue transfer or other workflows. |