# Understanding ticket channels in Explore

Source: https://support.zendesk.com/hc/en-us/articles/4408836378394-Understanding-ticket-channels-in-Explore

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Explore Professional or Enterprise |

With Explore, you'll often want to create reports based on the channel from which a
ticket was created. *Channels* are the means by which your customers create support
requests and how you engage with them.

The channels you see will depend on the channels you have installed. For example, if you
haven't set up Facebook integration with Zendesk Support, you won't see the Facebook
channel.

Use this article to learn how to view the channels you can report about in Explore, and
to learn how channel names will appear when you create reports that use them.

To learn more about channels in general, see [About Zendesk Support channels](https://support.zendesk.com/hc/en-us/articles/4408824097050).

This article contains the following topics:

- [How to view ticket channels in Explore](#topic_bfn_g2c_lhb)
- [Support channels in Explore](#topic_wp4_gvb_lhb)

## How to view ticket channels in Explore

Use this simple report to see the names of all ticket channels you have used and the
number of tickets assigned to each channel. If you need help creating a report, see
[Creating reports](https://support.zendesk.com/hc/en-us/articles/4408821589530).

**To view your ticket channels**

1. In Explore, open a new report using the Support: Tickets dataset.
2. In the **Metrics** panel of the report builder, add the **Tickets**
   metric.
3. In the **Rows** panel, add the attribute **Ticket channel**.

You'll see a table that looks similar to the example below:

![Explore channels report](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_channels_1.png)

## Support channels in Explore

The following support channels are available in Explore reports. The channels that
are shown will vary depending on the channels you've configured.

| Ticket channel | Displayed in Explore as | Description |
| --- | --- | --- |
| Any channel | Any channel | Tickets created from third-party Zendesk integrations. |
| Web service (API) | Api | Tickets generated or updated from the Zendesk API, for example:  - API phone call inbound - Web service - Ticket sharing - Group change - Linked problem - Rule - User change - Merge |
| Chat | Chat | Tickets created from a Zendesk Chat session. |
| Closed ticket | Closed ticket | Tickets created by replying to closed tickets, also known as follow-up tickets.  This channel value can be returned in Explore only for the **Update channel** attribute in the [Updates history dataset](metrics-and-attributes-for-zendesk-support.md#topic_zdl_flq_4y). (The **Ticket channel** attribute in the [Support datasets](https://support.zendesk.com/hc/en-us/articles/4408827693594) returns a value of **Web** for all follow-up tickets.) |
| Messaging | Messaging | Tickets generated from a web messaging conversation. For more information, see [About messaging](https://support.zendesk.com/hc/en-us/articles/4408846454682). |
| Email | Email | Tickets originating with an email request. |
| Facebook message Facebook post | Facebook | Tickets generated from Facebook posts and messages. |
| Forum topic (deprecated) | Forum | Tickets originating from a community post in the web portal. |
| Help Center post | Help center | Tickets that were created from a community post, article comment, or post comment in the help center. |
| Mobile | Mobile | Tickets originating from a Zendesk mobile app. |
| Mobile SDK | Mobile SDK | Tickets generated from a custom app using the Zendesk Mobile SDK. |
| Text | SMS | Tickets originating from a text message. |
| System | System | Tickets created by Zendesk Support. Examples include tickets created by importing from another application. |
| X (formerly Twitter) X (formerly Twitter) DM  X (formerly Twitter) Like | Twitter | Tickets originating from an X (formerly Twitter) mention, DM, or like. |
| Phone call (incoming) Phone call (outgoing)  Voicemail | Voice | Tickets originating from calls and voicemails. |
| Answer Bot for Web Widget | Answer Bot for Web Widget | Tickets created from article recommendations feature in the Web Widget (Classic) that led to a ticket being solved. |
| Web form Web Widget | Web | Tickets originating from a Support web form, the Support agent interface (created by an agent), or the Web Widget. For the **Ticket channel** attribute in the [Support datasets](https://support.zendesk.com/hc/en-us/articles/4408827693594), follow-up tickets are also shown in this channel regardless of how they are created. (The **Update channel** attribute in the [Updates history dataset](metrics-and-attributes-for-zendesk-support.md#topic_zdl_flq_4y) can return a value of **Closed ticket**.) |
| Social messaging | - WhatsApp - LINE - WeChat - Facebook Messenger - Twitter Direct Message | If you're using the Zendesk Agent Workspace and add a social messaging channel, these appear as ticket channels you can use in your Explore reports. If you're not using the agent workspace, you can use tags associated with each channel in your reports. For help, see [Monitoring your social media channels](https://support.zendesk.com/hc/en-us/articles/4408838593690). |
| Side conversation | Side conversation | Tickets created from [side conversation child tickets](https://support.zendesk.com/hc/en-us/articles/4408836521498). |

For more information, see [About Zendesk channels](https://support.zendesk.com/hc/en-us/articles/4408824097050).