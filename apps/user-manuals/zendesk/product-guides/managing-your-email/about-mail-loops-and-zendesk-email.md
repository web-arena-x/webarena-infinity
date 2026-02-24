# About mail loops and Zendesk email

Source: https://support.zendesk.com/hc/en-us/articles/4408836366362-About-mail-loops-and-Zendesk-email

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Email is complicated. Hundreds of billions of messages are sent every day. Zendesk alone receives and processes millions. Over time, email's mission has changed. It's not just for person-to-person communication but also for mass mailing and machine communication. Complication introduces several threats, including mail loops, which Zendesk Support takes into account for email management.

This article contains the following sections:

- [What's a mail loop?](#topic_crz_sd1_qv)
- [How Zendesk Support prevents mail loops](#topic_knn_td1_qv)

Related articles:

- [Email resources](https://support.zendesk.com/hc/en-us/articles/4408846000410)
- [Understanding how mail loops are prevented between Zendesk accounts](https://support.zendesk.com/hc/en-us/articles/8051189803418)

## What's a mail loop?

Automatic acknowledgment of messages is a common practice for software that receives email. The default trigger **Notify requester and CCs of received request** is one example. When a ticket is created in Zendesk Support, the user is notified by email. This kind of behavior, while common, can result in a problem when two machines email each other.

It's not a problem for machines to receive email from one another. For example, if one system receives an email from another then sends an automatic reply, that's fine. But if *that* system also replies automatically, this can kick off a mail loop. In this scenario, each system will continue to reply automatically to the other every time a notification is received, creating a never-ending loop until someone or something intervenes.

Loops can occur in other ways, as well. Ticket updates may come from the API, ticket sharing, an app, or a web interface. These updates can cause emails sent by trigger notifications such as **Notify requester and CCs of comment update**. Sometimes, those emails can cause another update, not by email, but by some other means.

## How Zendesk prevents mail loops

There are several different things Zendesk does to prevent mail loops. It should be stated clearly that we can't prevent all mail loops all the time. They're a part of the ecosystem now, and we're doing what we can, but just like spam messages, they will occasionally happen.

Here are some of the measures in place to prevent mail loops:

- [Unique support addresses, not used for users](#topic_xrq_vd1_qv)
- [Bulk mail and no-reply addresses do not create tickets](#topic_bgc_zd1_qv)
- [Fall-back limitations for ticket updates by a user in an hour](#topic_t3r_zd1_qv)

To learn how Zendesk prevents Zendesk-to-Zendesk email loops, see [Understanding how mail loops are prevented between Zendesk accounts](https://support.zendesk.com/hc/en-us/articles/8051189803418).

### Unique support addresses, not used for users

Your users contact you at your [support addresses](https://support.zendesk.com/hc/en-us/articles/4408842868506). If you use external support addresses (for example, support@mycompany.com), Zendesk Support prevents mail loops by disallowing users with one of your support addresses as their email. In other words, if you have an end-user whose email address is support@example.com, you cannot enable support@example.com as a support address. If you have support@example.com as a support address, you cannot create a user with that address.

We do this to prevent notifications being sent to your support addresses. If we did send email to one of them, they would automatically forward that email back to Zendesk Support, creating another ticket. This process would continue to loop, resulting in many tickets or comments.

### Bulk mail and no-reply addresses do not create tickets

Certain emails don't create tickets by default, such as bulk mail or messages that identify as machines.

Tickets also aren't created when the sender is a no-reply address. These are mostly governed by [suspended tickets](https://support.zendesk.com/hc/en-us/articles/4408889141146). You can [add the address to the allowlist](https://support.zendesk.com/hc/en-us/articles/4408886840986) if you know the sender is safe; however, doing so will increase the rate limits for that specific email address and the number of suspensions by a factor of ten. At that point, Zendesk will start to drop the traffic. Zendesk reserves the right to suspend or block any traffic exceeding safe levels. The email channel isn't designed for programmatic or automated traffic; that is the exclusive purpose of the [API](https://developer.zendesk.com/api-reference/ticketing/tickets/tickets/). Using the email channel for this type of traffic should be regarded as a temporary workaround.

When a ticket is created on behalf of a bulk sender, Zendesk suppresses automatic notifications.
Agent comments will still trigger notifications, but to avoid mail loops, Zendesk suppresses any message that is sent when no comment is added. This is true when you recover these messages from suspension or add such users to the allowlist.

### Fall-back limitations for ticket updates by a user within an hour

As a last resort form of prevention, Zendesk limits the number of updates a single user can make within an hour. There's a limit of 20 emails from the same user within an hour. Beyond that, the following 20 updates will be suspended. If more than 40 are received, all additional updates within that hour will be rejected (meaning they won't even create suspended tickets). This serves as a way to prevent mail loops from becoming a serious problem.

This limitation *won't* work if the other system doesn't use the same email address every time. Some systems use a new email address for each automated message.

You can [add the address to the allowlist](https://support.zendesk.com/hc/en-us/articles/4408886840986) if you know the sender is safe; however, doing so will increase the rate limits for that specific email address and the number of suspensions by a factor of ten. At that point, Zendesk will start to drop the traffic. Zendesk reserves the right to suspend or block any traffic exceeding safe levels. The email channel isn't designed for programmatic or automated traffic; that is the exclusive purpose of the [API](https://developer.zendesk.com/api-reference/ticketing/tickets/tickets/). Using the email channel for this type of traffic should be regarded as a temporary workaround.