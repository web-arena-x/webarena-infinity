# Managing conversation handoff and handback

Source: https://support.zendesk.com/hc/en-us/articles/4408824482586-Managing-conversation-handoff-and-handback

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

In this article, we’ll explain messaging conversation handoff and handback, the actions that can change the first responder in a conversation from an AI agent to a live agent, and back again.

- **Handoff** is removing the AI agent as the conversation’s first responder and making an agent the first responder.
- **Handback** is removing a live agent as the first responder in a conversation, clearing the way for the AI agent to be the first responder when the customer starts a new conversation. Handing a conversation back to the AI agent is, effectively, ending one conversation, clearing the way for a new conversation to address a new problem or support request.

This article includes the following topics:

- [Understanding handoff events](#topic_azj_cqq_5pb)
- [Understanding and managing handback events](#topic_ux4_cqq_5pb)
- [Additional settings to consider](#topic_mvs_cqq_5pb)

## Understanding handoff events

When the conversation is handed off to a live agent, those agents are notified of the pending support request based on the account’s [established routing flow](https://support.zendesk.com/hc/en-us/articles/4408829019162), and the AI agent can no longer respond to the conversation.

An agent remains the first responder until the ticket associated with the conversation is closed.

## Understanding and managing handback events

Conversation handback is initiated when the status of the ticket associated with the conversation is changed from *Solved* to *Closed*. Then, when the customer begins a new conversation, the AI agent becomes the first responder again. It’s important to note, however, that the AI agent does not automatically send the first message in a subsequent conversation. The returning customer must send a message to initiate a response from the AI agent, which will then attempt to find a conversational shortcut. If no shortcut is found, the AI agent will respond according to normal free-text entry behavior. See [Conversational shortcuts and article suggestions](https://support.zendesk.com/hc/en-us/articles/4408824263578#topic_mgq_d4n_jnb) for more information.

Until the status of the ticket is changed to *Closed*, a customer returning to the messaging channel while the ticket is still marked Solved would find the previous conversation still active, and the agent would still be the first responder. The customer would be unable to start a new conversation to address a new support request. By default the time between a solving and closing a ticket is four days, which can cause some confusion for customers returning to your messaging channel.

You can avoid this scenario in two ways:

- [Adjusting your default automation](#topic_dgn_3sq_5pb)
- [Creating a trigger to manage handback timing](#topic_xbt_3sq_5pb)

### Adjusting your default automation

Automatically updating a Solved ticket status to Closed is managed through a default Support automation, *Close ticket 4 days after status is set to solved*.

You can [edit this automation](https://support.zendesk.com/hc/en-us/articles/4408883801626#topic_rsh_miv_ub)
to manage how much time passes before the ticket status changes to Closed. You may want to change the time frame to close the ticket within the following hour or you can extend the time to up to 28 days after the ticket is Solved. To close a ticket immediately, see the trigger recipe in the following section.

### Creating a trigger to manage handback timing

You can also [create a trigger](https://support.zendesk.com/hc/en-us/articles/4408886797466#topic_tpw_gay_tb)
to automatically close solved tickets, essentially overriding the default automation.

To do this, you’ll need to add a tag (such as *close* ) to any ticket that has its status changed to *Solved.*

Then, create a trigger that fires on any ticket with the added tag and closes the ticket. The trigger should have the following properties:

- **Condition**: Tags | Contains at least one of the following | close
- **Action**: Status | Closed

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/solve_ticket_trigger_ex.png)

If you are using CSAT to gauge customer satisfaction in messaging, it’s important to note that the survey is sent immediately when the ticket status is set to Solved. If you are using CSAT surveys, we recommend that you keep at least a small time buffer between solving and closing a ticket, to avoid any conflicts. See [About the CSAT (customer satisfaction) user experience for email and messaging](https://support.zendesk.com/hc/en-us/articles/4408886173338) for more information.

## Additional settings to consider

There are a number of settings that, while not directly related to messaging handoff or handback actions, can impact how they perform, and how your end users experience them.

- **Out-of-office triggers** can set a customer’s expectations for when a live agent might engage them in the conversation. See [Creating an out-of-office message in a Web Widget or mobile SDK](https://support.zendesk.com/hc/en-us/articles/4408842866074)
 for more information.
 *Out of office triggers only fire after handoff occurs*.
- **Continuous conversations** let you automatically send email notifications to end users who have left a conversation in a Web Widget before it was concluded. See [Enabling customers to continue their conversation over email](https://support.zendesk.com/hc/en-us/articles/4408829095706-Enabling-customers-to-continue-their-conversation-over-email)
 for more information.
- **Routing settings** manage how a messaging conversation and its associated ticket are passed from the AI agent to a live agent or group, after a handoff event occurs. See [About routing in messaging](https://support.zendesk.com/hc/en-us/articles/4408829019162) for more information.