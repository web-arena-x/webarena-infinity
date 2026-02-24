# Conversational styles in messaging

Source: https://support.zendesk.com/hc/en-us/articles/6088892450586-Conversational-styles-in-messaging

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

Messaging, unlike live chat, allows you to have persistent conversations with
your customers. One of the main benefits of this is that these conversations may adopt
different conversational styles, for example they could behave like live chat where a
customer has real time, synchronous interactions with an agent or behave more like
social messaging channels where the customer interactions with the agent may occur
asynchronously or occur over a period of time.

With messaging you have the flexibility to adopt one conversational style for
all customer queries or different conversational styles for different customer
queries.

This article contains the following sections:

- [Live chat](#topic_bkp_f3t_pyb)
- [Live chat with a returning customer](#topic_mjk_r3t_pyb)
- [Social messaging](#topic_cxk_r3t_pyb)

## Live chat

*Live chat* is a real-time conversation between an end user and an
agent, with a related ticket that closes immediately (or soon) after it is solved,
effectively ending the conversation. This conversational style uses a custom trigger
to close the ticket sooner than the default solve-to-close time period. If, or when
the end user returns to the conversation, a new ticket is created, so there is no
overlap between the first and subsequent conversations.

|  |  |
| --- | --- |
| The customer initiates a new conversation by engaging using the Web Widget, the mobile SDK, or a social messaging channel. At this stage a messaging ticket is created with a ticket status of New.  [Omnichannel routing](https://support.zendesk.com/hc/en-us/articles/4409149119514) can be used to automatically assign this ticket to the most appropriate agent based on their availability, capacity and skills. When the agent accepts the ticket, the ticket status changes to Open.  The customer and agent exchange messages in real time until the issue is resolved and the agent changes the ticket status to Solved.  To mimic the ending of the session in live chat we use a trigger to automatically set the ticket status to Closed. If the customer returns, any new interaction will cause a new ticket to be created. |  |

For more help and examples, see [Configuring the live chat conversational
style](https://support.zendesk.com/hc/en-us/articles/6088983050138).

### When to use the live chat conversational style

If you are currently using live chat, this conversational style allows
for an easier transition to messaging as the customer and agent experience, and
the metrics you'll track are similar.

The live chat conversational style is best suited to businesses where
you want to have a quick response to real time queries, for example, food
delivery, gambling, and taxi services.

Additionally, this style should be used for unauthenticated website
visitors. These visitors typically don't return to the site, so should always be
prioritized as a live chat.

## Live chat with a returning customer

*Live chat with a returning customer* is similar to the live chat
conversation style, but has a gap between solving a ticket and closing it. This
enables the end user to return to the conversation within a set period of time to
reopen the ticket and continue discussing the original topic. The ticket uses a
custom automation that leaves more time between solving and closing than the live
chat style conversational style.

|  |  |
| --- | --- |
| This begins in the same way as the live chat conversational style but instead of closing the ticket immediately when it is marked as Solved, we leave a period of time before doing so.  If the customer returns and posts a new message during the period in which the ticket is marked as Solved, the ticket will reopen allowing the customer to continue their conversation until it is resolved.  This could happen multiple times until the conversation is closed. |  |

For more help and examples, see [Configuring the live chat for returning customers
conversational style](https://support.zendesk.com/hc/en-us/articles/6088999921434).

### When to use the live chat with a returning customer conversational style

This conversational style leads to an improved experience for the
customer as they will not have to wait in the queue again and will be able to
continue the same conversation with the same agent, rather than having to
explain their issue again to a new agent.

The agent experience is also more efficient as the agent will not have
to handle multiple tickets for the same issue.

The live chat returning customer conversational style is best suited to
businesses where the customer is likely to return with a follow up query on the
same issue.

Using a conversational style can change how you measure success. Even though a
single ticket might take longer to resolve, you'll likely have fewer individual
tickets than with live chat. Plus, reassigning the ticket to the original agent
might result in a lower total handle time compared to dealing with many separate
tickets. So, consider revising your metrics to reflect these changes.

## Social messaging

*Social messaging* is an ongoing conversation, over a longer period of
time. Tickets created from this type of conversation are not closed by a custom
trigger; rather, they use the default automation “close ticket 4 days after status
is set to solved” to update them, if needed, to up to 28 days between solved and
closed status. This allows the customer to come back over this period of time to
continue the conversation, and have the information gathered during those return
visits applied to the initial ticket.

|  |  |
| --- | --- |
| This conversational style is similar to what we experience on social messaging channels with the customer and agent being able to have a series of interactions, which take place over a longer period of time.  In contrast to the other conversational styles, the ticket is not automatically closed.  The conversation begins in the same way as the other conversational styles but the agent uses ticket statuses such as Pending, On Hold and Solved to define the current status of the ticket. If using omnichannel routing, then switching the ticket to any of these statuses will free up an agent’s capacity and so they will be able to accept another incoming conversation rather than having this ongoing conversation consuming capacity and preventing them from accepting new work.  If the customer responds whilst the ticket is in any of these statuses then the ticket will go back to the Open status and consume agent capacity.  If the conversation spends 28 days in the Solved status it will automatically move to the Closed status. If a customer responds after this then a new ticket will be created. |  |

For more help and examples, see [Configuring the social messaging conversational
style](https://support.zendesk.com/hc/en-us/articles/6089032137754).

### When to use the social messaging conversational style

This conversational style is useful for long running or complex issues
that may take place over a period of time, for example, a dispute, a discussion
about a medical issue, or for issues that are not time sensitive.

Customers will be able to continue their existing conversation with the
same agent, without having to wait in the queue again.