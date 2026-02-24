# About native Chat time duration metrics

Source: https://support.zendesk.com/hc/en-us/articles/8203054518298-About-native-Chat-time-duration-metrics

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Explore Professional or Enterprise |

In this article, you'll learn more about some of the metrics built into Zendesk live Chat that help you measure the duration between two events.

The engagement time metrics are defined similarly to the full chat time metrics, but they specifically refer to interactions between a customer and a particular agent. For more details, please refer to the section on [What is an engagement in Chat?](https://support.zendesk.com/hc/en-us/articles/4408830638234-What-is-an-engagement-in-Chat#:~:text=A%20chat%20engagement%20is%20measured,this%20starts%20a%20new%20engagement.).

This article covers only the native live Chat metrics. Support and SLA metrics might have identical names but their behavior is different. See: [About native Support time duration metrics](about-native-support-time-duration-metrics.md#:~:text=The%20native%20duration%20metrics%20are,the%20specific%20events%20take%20place.) and [Defining and using SLA policies](https://support.zendesk.com/hc/en-us/articles/4408829459866-Defining-SLA-policies#topic_gpr_ppv_tr).

For more information about the live chat metrics and attributes you can use with Explore, see [Metrics and attributes for live chat](metrics-and-attributes-for-live-chat.md).

This article contains the following topics:

- [First reply time](#topic_irt_v3b_ldc)
- [Chat duration](#topic_ur1_w3b_ldc)
- [Chat no reply time](#topic_phb_w3b_ldc)
- [Chat wait time](#topic_kvb_w3b_ldc)
- [Chat longest reply time](#topic_b3c_w3b_ldc)

Related articles:

- [Metrics and attributes for live chat](https://support.zendesk.com/hc/en-us/articles/4409149177242)
- [What is the difference between dropped chats and missed chats?](https://support.zendesk.com/hc/en-us/articles/4408826868250)
- [About native Support time duration metrics](https://support.zendesk.com/hc/en-us/articles/4408834848154)

## First reply time

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/met10.png)

- **Definition**: The time between the end user joining the chat and the agent's first response. An end user joins a chat when they send the first chat message or reply to a proactive message.
- **First timestamp**: End user joining the chat.
- **Second timestamp**: The agent's first response.

The definition of engagement first reply time behaves as follows:

- **For broadcast mode**: Starts at the oldest unanswered end user comment, including time in queue, and ends at the agent's first comment.
- **For assigned mode**: Starts when the agent is assigned to the chat and ends at the agent's first comment.
- **For agent chat transfers**: Start at agent assignment and end at agent's first reply to an unanswered end user comment.

## Chat duration

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/met11.png)

- **Definition**: The time duration from the first to the last chat message. The first message can come from an end user or from a proactive chat trigger.
- **First timestamp**: First message in the chat.
- **Second timestamp**: Last message in the chat.

## Chat no reply time

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/met12.png)

- **Definition**: The time from the end user's last unanswered comment to the end user leaving the chat session.
- **First timestamp**: End user last unanswered comment.
- **Second timestamp**: End user leaving the chat.

## Chat wait time

- **Definition**: The time the end user waited for the first reply time from an agent. If no agent replies, then this returns the total time the end user waited before leaving the chat session.
- **First timestamp**: End user joining the chat.
- **Second timestamp**: The agent's first response or the end user leaving the chat.

## Chat longest reply time

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/met13.png)

- **Definition**: The maximum time it took for an agent to reply to the end user comments during the chat session.
- **First timestamp**: End user's comment.
- **Second timestamp**: Agent's response with the longest reply time.