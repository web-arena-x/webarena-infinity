# About side conversations

Source: https://support.zendesk.com/hc/en-us/articles/4408844206746-About-side-conversations

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Customer Service Suite** | Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Employee Service Suite** | Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Collaboration add-on |

Side conversations are spaces in a ticket where agents can have a side conversation with a specific group of people, or discuss a specific area of concern or course of action.
You can use them to organize information about a ticket.

Side conversations are only available if they have been [activated by an administrator](https://support.zendesk.com/hc/en-us/articles/4408832279962).

Note: Viewing and replying to email side conversations are supported on the Android and iOS versions of the [Zendesk Support mobile app](https://support.zendesk.com/hc/en-us/articles/4408846407066). You can still use the email client on your mobile device to create side conversation notifications.

This article includes these topics:

- [Advantages of using side conversations](#topic_z32_jj4_l2b)
- [Recommendations about side conversations](#topic_bj2_jj4_l2b)
- [About side conversation channels](#topic_w4b_ql1_rnb)
- [About support addresses used to send side conversations](#topic_kcb_svr_dvb)

Related articles:

- [Side conversation resources](https://support.zendesk.com/hc/en-us/articles/4408830838170)

## Advantages of using side conversations

Problems often consist of multiple parts, and solving them often consists of conversations with different people. It gets confusing for everyone involved when all of the questions and answers are mixed together in one place without any kind of organization.

For example, let’s say you need to discuss something with your Legal team, but don’t need or want other people involved.

Using side conversations can make it easier to do things like:

- Find, organize, and manage information about a specific part of an issue
- Have a conversation with the right people
- Find specific questions, answers, and replies. Ensure conversations happen outside of the main conversation with the requester
- Have multiple standalone conversations that are separate from each other
- Get outside help without pulling others into the main ticket directly

## Recommendations about side conversations

Here’s some general advice about how to get the most out of side conversations:

- The assignee should create and manage side conversations in the tickets they're responsible for. This allows administrators to create triggers based on the assignee role, and enables easier handoff between agents.
- Set up triggers to take advantage of the side conversation event conditions to fully integrate them into your workflows and to keep agents on top of the activity within them. See the **Ticket: Side conversation** [conditions](https://support.zendesk.com/hc/en-us/articles/4408893545882#topic_i3y_fkz_1cb__side_conversation) and [actions](https://support.zendesk.com/hc/en-us/articles/4408893545882#topic_ncz_4kz_1cb__side_conversation_action).
- Create trigger conditions for side conversations to make sure that assignees know when a side conversation is created, closed, replied to, and reopened.
 Without them, the agent assigned to the ticket (ideally, this person is also the creator of the side conversation) may have a hard time knowing what’s going on with a particular issue.
- Remember that the creator of the side conversation doesn't automatically receive email replies to side conversations. That’s not the default behavior. Also sending side conversations to your own support address is not supported and will result in those side conversations ending up in the Suspended tickets view.
- The creator of the side conversation receives an email reply if another agent responds in an email side conversation. The other agent can manually remove the creator's email address so that it's not included in the reply.
 Agents might want to remove the creator's email address so that it's not displayed in email replies.

## About side conversation channels

When you create a side conversation, you can choose to have the side conversation in one of these channels:

- **Email**: Creates an email-based side conversation (see [Creating side conversations](https://support.zendesk.com/hc/en-us/articles/4604286879642)).
- **Microsoft Teams** (if enabled): Creates a Microsoft Teams-based side conversations (see [Using Microsoft Teams in side conversations](https://support.zendesk.com/hc/en-us/articles/5191537451290)).
- **Slack** (if enabled): Creates a Slack-based side conversation (see [Using Slack in side conversations](https://support.zendesk.com/hc/en-us/articles/4408844202778)).
- **Ticket** (if enabled): Creates a side conversation child ticket (see [Using side conversation child tickets](https://support.zendesk.com/hc/en-us/articles/4408836521498)).

 Note: Side conversation child tickets can be routed by omnichannel routing. See [About omnichannel routing with unified agent status](https://support.zendesk.com/hc/en-us/articles/4409149119514).

Side conversations are created from the [context panel](https://support.zendesk.com/hc/en-us/articles/4408836526362) and can be [printed](https://support.zendesk.com/hc/en-us/articles/4408836523930) from all channels.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/side_convo_select_MS_teams.png)

## About support addresses used to send side conversations

Side conversation notifications are sent from the [support address](https://support.zendesk.com/hc/en-us/articles/4408842868506) associated with the ticket that the side conversation is on (for example, support@*yoursubdomain*.zendesk.com). If you have [multiple brands and support addresses](https://support.zendesk.com/hc/en-us/articles/4408836507162), side conversation notifications come from each of your support addresses (for example, support@*brand*.zendesk.com).

If you have internal email routing rules (for example, in Microsoft Exchange), we recommend that you include references to each of your unique support addresses.
Otherwise, email notification for side conversations will not be routed correctly.
Check your allowlists and blocklists.