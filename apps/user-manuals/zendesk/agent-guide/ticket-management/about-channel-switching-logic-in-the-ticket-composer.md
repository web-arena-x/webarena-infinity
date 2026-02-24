# About channel switching logic in the ticket composer

Source: https://support.zendesk.com/hc/en-us/articles/5924725590682-About-channel-switching-logic-in-the-ticket-composer

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

In the [Zendesk Agent Workspace](https://support.zendesk.com/hc/en-us/articles/4408821259930), agents can work across [multiple channels](https://support.zendesk.com/hc/en-us/articles/4408824097050) all within the same ticket. Because of this flexibility, the ticket composer includes some rules (logic) for channel switching within a ticket. This logic controls which channels are available to you when you send a reply.

This article contains the following topics:

- [Channel switching options in the composer](#topic_fdp_5xs_dyb)
- [Channel switching logic for talk tickets](#topic_o3q_h1t_dyb)
- [Channel switching logic for chat tickets](#topic_xjf_xct_dyb)
- [Channel switching logic for messaging tickets](#topic_nwd_hgt_dyb)
- [Channel switching logic for any ticket, light agents](#topic_nzv_kgt_dyb)
- [Channel switching logic for email and other ticket types](#topic_ks3_sgt_dyb)

**Related articles**

- [Composing messages in the Zendesk Agent Workspace](https://support.zendesk.com/hc/en-us/articles/4408831849882)

## Channel switching options in the composer

The following simplified diagram shows which channel switching options are available for agents, based on the ticket type.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aw_available_channels.png)

Some examples include:

- After you end a chat with a customer, you can switch to the email channel to send a follow-up email.
- After you receive an email ticket from a customer who needs a detailed, personalized reply for an urgent matter, you can switch to the talk channel and call the customer.
- If you have an email ticket paired with [private by default settings](https://support.zendesk.com/hc/en-us/articles/4408822560410#topic_k3f_q1f_hlb) in Admin Center, internal note automatically shows in the composer when you open the ticket.

You can use the channel menu to switch channels manually in the composer. See [Switching channels in the composer](https://support.zendesk.com/hc/en-us/articles/4408831849882#topic_gtw_j1h_rmb). You can also rely on automatic channel switching logic to help out. When you open a ticket, channel switching logic can automatically present the best channel option, reducing the time it takes to reply to customers.

Channel switching logic varies depending on which channels were used to create the ticket.
It also depends on which default privacy settings are set in Admin Center. See below for details. The default privacy settings in Admin Center apply to email, talk, and other channels, but not to messaging and chat. See [Changing the default privacy of ticket comments](https://support.zendesk.com/hc/en-us/articles/4408822560410).

## Channel switching logic for talk tickets

When you open a talk ticket with the call ended, here are the results. The behavior changes depending on which [privacy defaults](https://support.zendesk.com/hc/en-us/articles/4408822560410) for ticket comments are set in Admin Center.

| **Situation** | **Condition 1** | **Condition 2** | **Result** |
| --- | --- | --- | --- |
| Agent opens a talk ticket | The call has ended. | The Set the composer channel to public setting is selected in Admin Center. | Composer shows Public reply. |
| The Set the composer channel to public setting is not selected in Admin Center. | Composer shows Internal note. |

There’s one exception to the privacy defaults for ticket comments. Tickets that only have internal notes and no public comments will always default to internal notes, even if the Public by default setting is turned on.

## Channel switching logic for chat tickets

When you open a chat ticket, here are the results. Because chat is considered a *live* channel, the [privacy defaults](https://support.zendesk.com/hc/en-us/articles/4408822560410) for ticket comments that are set in Admin Center don’t apply.

| **Situation** | **Condition 1** | **Condition 2** | **Result** |
| --- | --- | --- | --- |
| Agent opens a chat ticket **Note**: The default privacy settings in Admin Center don’t apply. | The chat is active | | Composer shows the Chat channel. |
| The chat is inactive | The chat user has a known email address | Composer shows the Email channel. |
| The chat is inactive | The chat user doesn’t have a known email address | Composer shows Internal note. |

## Channel switching logic for messaging tickets

When you open a messaging ticket, here are the results. Because messaging is considered a *live* channel, the [privacy defaults](https://support.zendesk.com/hc/en-us/articles/4408822560410) for ticket comments that are set in Admin Center don’t apply to *active* messages.

| **Situation** | **Condition** | **Result** |
| --- | --- | --- |
| Agent opens a messaging ticket **Note**: For active messages, the default privacy settings in Admin Center *don’t* apply. | The messaging channel has not timed out. It is still available. Timeouts vary from 24 hours to 7 days, depending on the type of messaging channel. | Composer shows the applicable messaging channel. For example, WhatsApp, Facebook, WeChat, Messaging, and so on. |
| Agent opens a messaging ticket **Note**: For inactive messages or email replies, the default privacy settings in Admin Center *do* apply. | The applicable messaging channel has timed out. | The default privacy settings in Admin Center do apply. The Composer shows Internal note. |
| The customer’s last reply was by email, regardless of channel timeout. | The default privacy settings in Admin Center do apply. The Composer shows Internal note. |

## Channel switching logic for any ticket, light agents

When a light agent opens any ticket, the composer shows Internal note. Light agents can only add internal notes, not public replies. See [Understanding what light agents can do](https://support.zendesk.com/hc/en-us/articles/4408846501402#topic_vwz_qm1_blb).

## Channel switching logic for email and other ticket types

For email and other types of tickets, channel switching logic is applied based on the [privacy defaults](https://support.zendesk.com/hc/en-us/articles/4408822560410) for ticket comments that are set in Admin Center.

There’s one exception to the privacy defaults for ticket comments. Tickets that only have internal notes and no public comments will always default to internal notes, even if the Public by default setting is turned on.