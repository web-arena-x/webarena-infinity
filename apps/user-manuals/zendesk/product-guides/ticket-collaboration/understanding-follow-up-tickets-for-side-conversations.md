# Understanding follow-up tickets for side conversations

Source: https://support.zendesk.com/hc/en-us/articles/4408837750170-Understanding-follow-up-tickets-for-side-conversations

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Collaboration add-on |

When someone replies to a side conversation that belongs to a closed or archived ticket, a [follow-up ticket](https://support.zendesk.com/hc/en-us/articles/4408883882522) is automatically created.

This article includes these sections:

- [About follow-up tickets for side conversations](#topic_isq_wrp_gmb)
- [Workflow example for follow-up tickets for side conversations](#topic_snx_shm_hmb)

**Related articles:**

- [Using side conversations in tickets](https://support.zendesk.com/hc/en-us/articles/4408844206746-Using-side-conversations-in-tickets-Collaboration-add-on-)

## About follow-up tickets for side conversations

Most side conversation workflows rely on triggers to take some sort of action when a reply is received, such as changing a ticket’s status to move it into a view, so that agents see that something happened. However, since closed and archived tickets don’t run triggers, replies to side conversations in them can go unnoticed.

When an email or Slack side conversation that belongs to a closed or archived ticket receives a reply, a follow-up ticket is automatically created. The new ticket will have the side conversation in it and keep the original assignee and group value. The new ticket will be able to run triggers so it can show up in the appropriate views.

Note: Follow-up tickets are not created if a side conversation within a child ticket is updated while the parent ticket is closed. For more information about the parent-child relationship of tickets, see [About side conversation child tickets](https://support.zendesk.com/hc/en-us/articles/4408836521498#topic_gql_rlg_2nb).

The follow-up ticket will be initiated with an internal note to prevent sending any updates to the requester, but a public comment can always be added to it, if the reply contains relevant information that they should know about.

For information about the types of data that is pulled from the original ticket into the follow-up ticket, see [Creating a follow-up for a closed ticket](https://support.zendesk.com/hc/en-us/articles/4408883882522).

## Workflow example for follow-up tickets for side conversations

Here's an example of what happens when someone replies to a side conversation on a closed or archived ticket. This assumes that you have triggers for side conversations with condition statements for **Side conversation + Is + Replied to** and **Side conversation
+ Is + Created**.

For additional information about these trigger conditions and how to use them, see the [Ticket trigger conditions and actions reference](https://support.zendesk.com/hc/en-us/articles/4408893545882).

1. Someone replies to a side conversation.

   The person replying can be an agent or an end user. They can be replying via email or from the ticket interface. They have some kind of follow-up question, new information, or perhaps some kind of new, but related issue.
2. The reply is added to the side conversation.
3. You don't get an email notification about the reply.

   This happens even though you have a trigger for side conversations that includes a condition statement for **Side conversation + Is + Replied to** because the ticket is already closed or archived.
4. Support creates a follow-up ticket.

   The follow-up ticket is a new, separate ticket.
   The ticket interface indicates that this is a follow-up ticket and tells you what the original ticket was, in case you need to look at it.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/side_conv_follow_up_ticket.png)

   The side conversation that was replied to is copied and included as part of the follow-up ticket.

   The first comment in the follow-up ticket is a *private comment*. A *private comment* appears in the agent interface as an *internal note*. Private comments and internal notes are the same thing.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ccs_comments_internal.png)
5. You get an email notification that a side conversation was created.

   The email notification is about the side conversation on the follow-up ticket, not the original ticket. This happens because you have a trigger for side conversations that includes a condition statement for **Side conversation + Is + Created**.

   The original ticket remains closed (the ticket status doesn't change).