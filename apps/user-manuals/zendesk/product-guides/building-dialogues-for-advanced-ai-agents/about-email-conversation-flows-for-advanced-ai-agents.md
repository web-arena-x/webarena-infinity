# About email conversation flows for advanced AI agents

Source: https://support.zendesk.com/hc/en-us/articles/8357758805146-About-email-conversation-flows-for-advanced-AI-agents

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | AI agents - Advanced |

If you've [connected an advanced AI agent to email](https://support.zendesk.com/hc/en-us/articles/8357750858010), the AI agent
can have multiple interactions with the customer over email, offering greater automation
potential. For example, if a customer emails a request but leaves out key details, such as
order ID, the AI agent can request the missing information before going any further.

Email conversation flows notify the AI agent when there is a new customer reply, and
recognize when a human agent is needed. Using these data points, you can track reopen rates
and [measure automation performance](https://support.zendesk.com/hc/en-us/articles/9510024609178) for the AI agent.

This article covers the following topics:

- [Understanding email conversation flows](#topic_z4m_lqq_q2c)
- [Limitations for email conversation flows](#topic_ljm_1xq_q2c)

## Understanding email conversation flows

You [use the dialogue builder](https://support.zendesk.com/hc/en-us/articles/8357749494810) to create conversation flows for an email
AI agent, similar to creating conversation flows for a messaging AI agent. However, the
available block types differ between the two types of AI agents. For details, see [Available block types](https://support.zendesk.com/hc/en-us/articles/8357749494810#topic_krz_vym_g2c).

Additionally, email conversation flows support automating the first triggered use case in
every conversation. When the dialogue of the triggered use case is complete, and the ticket
won't receive any more responses from the AI agent, the tag
`escalated_by_ultimate` is added to the ticket to indicate that the
automation is complete.

The `escalated_by_ultimate` tag is automatically applied in the following
scenarios:

- [Actions without a reply](#topic_xnx_qxn_5fc)
- [Single-reply dialogues](#topic_ezr_b5q_q2c)
- [Link to](#topic_q21_c5q_q2c)
- [Multiple-reply dialogues](#topic_h53_c5q_q2c)
- [Escalation block](#topic_dgy_15q_q2c)

Whenever this tag is added, the AI agent does not provide any more responses. This includes
instances where a human agent manually adds the tag before the automation is complete.

### Applying actions without sending a reply

Simply add actions in a reply and leave the text reply block empty. This way your email
AI agent will apply actions without sending anything to your customer.

### Using single-reply dialogues

Single-reply dialogues with conversation flows work the same way as without conversation
flows. If nothing follows a ticket reply block in the dialogue builder, the automation is
considered complete.

### Using link to

While email conversation flows are limited to one use case per conversation, linking
allows you to continue the conversation in another dialogue, so the link to block is not
considered the end of the conversation. Even though it's the final block in the dialogue,
you can link to other single- or multi-reply dialogues.

### Using multiple-reply dialogues

Multiple-reply dialogues can use the additional block options available for email
conversation flows, including customer messages, link to blocks, and multiple ticket
replies.

These dialogues allow the AI agent to send follow-up questions to confirm the customer's
intention or request missing information. Additional messages from the customer can be
processed and used during the automation.

The number of blocks is not limited, but it's a good idea to use no more than three
messages to gather the required information to automate a case.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_21170190572434.png)

There following events are supported for advanced AI agents for email, and can be
triggered in multiple-reply scenarios:

- **Ticket received by AI agents - Advanced**: This event is triggered only once per
  conversation, when the first customer message is received.
- **Ticket processed by AI agents - Advanced**: This event and the related actions are triggered
  with each ticket reply.
- **Ticket reply delay events**: The delay events are triggered for each reply. When
  using delays with email conversation flows, don't set long reply delays, but consider
  reply delays of 10-30 minutes.

### Using an escalation block

When an email conversation needs to be escalated to a human agent, you can use an
escalation block. This block adds the escalation tag to the ticket, can trigger additional
actions, and sends the ticket to a human agent to take over.

For more information, see [Configuring escalation strategies and flows for advanced AI
agents](https://support.zendesk.com/hc/en-us/articles/8357756604186).

## Limitations for email conversation flows

Email conversation flows have the following limitations:

- No rule-based escalations
- No AI agent replies to tickets older than three days