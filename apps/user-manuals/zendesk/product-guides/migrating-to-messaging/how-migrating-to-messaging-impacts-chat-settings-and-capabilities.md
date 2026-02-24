# How migrating to messaging impacts Chat settings and capabilities

Source: https://support.zendesk.com/hc/en-us/articles/4408834919834-How-migrating-to-messaging-impacts-Chat-settings-and-capabilities

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Live chat and messaging Team, Professional, or Enterprise |

To use messaging, Zendesk Chat accounts must also have Zendesk
Support with the Agent Workspace enabled.

When you migrate from Zendesk Chat to messaging, a number of changes are made
to your Zendesk Chat functionality.

Administrators must make sure they perform the tasks described in [Setting up Web Widget for messaging when using live chat and Web
Widget (Classic)](https://support.zendesk.com/hc/en-us/articles/4408832031898), in addition to any tasks described in this article.

This article discusses the following topics and areas impacted when messaging
is enabled:

- [Agent Workspace](#topic_mbc_ks4_jnb)
- [Chat dashboard](#topic_tqs_tkm_jnb)
- [Chat triggers](#topic_g2b_5km_jnb)
- [Chat routing](#topic_wrf_5km_jnb)
- [Chat reporting](#topic_hmk_5km_jnb)
- [Chat Conversation APIs](#topic_phf_hzc_g4b)

## Agent Workspace

In the Agent Workspace, messaging creates a well-integrated UI for your agents, with
[fewer limitations than Zendesk Chat](../setting-up-agent-workspace/limitations-in-the-zendesk-agent-workspace.md#topic_u4c_wzp_wnb).

If your account supports a high volume of chats or has a large number of
chat-only agents, check with your Zendesk account representative before migrating to
the Zendesk Agent Workspace. For best performance, follow these guidelines:

- Do not exceed 1,300 online Chat agents actively serving chats. If
  necessary, you can have up to 2,000 Chat agents actively serving chats, but you
  will need to reduce the number of concurrent chats served on your account to
  prevent potential performance degradation.
- No more than 8,000 concurrent conversations/with 200,000 total
  conversations per day.
- No more than 6,000 concurrent visitors with 300,000 total visitors
  per day

## Chat dashboard

Most of the features managed in the Chat dashboard have equivalent management
pages in Admin Center, or elsewhere in the Zendesk UI.

The following table lists the functionality areas in the Chat dashboard, and
where management of comparable messaging functionality is located.

Table 1.

| Menu group in Chat dashboard | Messaging functionality or feature and location |
| --- | --- |
| **Visitors > Simulate chat** | **[Testing the end user's messaging experience](https://support.zendesk.com/hc/en-us/articles/4408835784602)**  - **Admin Center > Channels > Messaging and   social > Messaging** > [Test it now](https://support.zendesk.com/hc/en-us/articles/4408835784602)   button in channel preview. |
| **Visitors > Ban visitor** | **[Suspending users](https://support.zendesk.com/hc/en-us/articles/8009733465370)**   - **Admin Center > Channels > People > Team > Roles** (managing roles to allow user suspension) - **Ticket UI** or **User profile** (suspending   a messaging user) |
| **History** | **[Viewing user history](https://support.zendesk.com/hc/en-us/articles/4408882039450)** - **Agent Workspace**: Agent dashboard, custom   views, or [customer   context](https://support.zendesk.com/hc/en-us/articles/4408829170458) |
| **Analytics** | **Monitoring [AI agent activity](https://support.zendesk.com/hc/en-us/articles/6847708774554) and suggesting improvements** - **Admin Center > AI > AI agents > AI agents**   > Insights dashboard in AI agent's page. **[Monitoring live agent activity](https://support.zendesk.com/hc/en-us/articles/4422485166746)** - Explore dashboard |
| **Monitor** | **[Monitoring live agent activity](https://support.zendesk.com/hc/en-us/articles/4422485166746)** - Explore dashboard |
| **Settings > Agents** | **[Viewing and managing agents](https://support.zendesk.com/hc/en-us/articles/4408843830938)** - **Admin Center > People > Team > Team   members** |
| **Settings > Departments** | **[Viewing and managing groups](https://support.zendesk.com/hc/en-us/articles/4408831652890)** - **Admin Center > People > Team >   Groups** |
| **Settings > Roles** | **[Viewing and managing roles](https://support.zendesk.com/hc/en-us/articles/4408882153882)** - **Admin Center > People > Team > Roles** |
| **Settings > Routing > Settings tab** | **[Omnichannel routing](https://support.zendesk.com/hc/en-us/articles/4828787357210)** - **Admin Center > Objects and rules >   Omnichannel routing > Routing   configuration** |
| **Settings > Routing > Skills tab** | **[Routing tickets based on agent skills](https://support.zendesk.com/hc/en-us/articles/4408838892826)**  - **Admin Center > Objects and rules > Business   rules > Skills** |
| **Settings > Shortcuts** | **[Macros](https://support.zendesk.com/hc/en-us/articles/4408844187034)** - **Admin Center > Workspaces > Agent tools >   Macros** |
| **Settings > Banned** | **[Viewing and managing banned users](https://support.zendesk.com/hc/en-us/articles/8009733465370)** - **Agent Workspace**: Customers > Suspended   users |
| **Settings > Triggers** | **[Messaging triggers](https://support.zendesk.com/hc/en-us/articles/5973077601562)** - **Admin Center > Objects and rules > Messaging   triggers** |
| **Settings > Goals** | N/A |
| **Settings > Widget** | **[Creating a messaging Web Widget](https://support.zendesk.com/hc/en-us/articles/4408832031898)**  - **Admin Center > Channels > Messaging and   social > Messaging** |
| **Settings > Personal** | **[Viewing and editing your user profile](https://support.zendesk.com/hc/en-us/articles/4408835022490)** - **Zendesk Support**: Click profile icon |
| **Settings > Account > Subscription** | [**Viewing and managing plan subscriptions**](https://support.zendesk.com/hc/en-us/articles/4408834640666) - **Admin Center > Account > Billing >   Subscription** |
| **Settings > Account > Zendesk Support** | **[Managing messaging transcript visibility](https://support.zendesk.com/hc/en-us/articles/4408818625690)** - **Admin Center > Objects and rules > Tickets >   Settings** |
| **Settings > Account > SLAs** | **[SLA policies](https://support.zendesk.com/hc/en-us/articles/4408829459866)** - **Admin Center > Objects and Rules > Business   rules > Service level agreements** |
| **Settings > Account > APIs and SDKs** | **[Messaging in your mobile channel](https://support.zendesk.com/hc/en-us/articles/4408834810394)** - **Admin Center > Channels > Messaging and   social > Messaging** |
| **Settings > Account > Email piping** | **[Messaging transcripts](https://support.zendesk.com/hc/en-us/articles/4408818625690)** - **Admin Center > Objects and rules > Tickets >   Settings** |
| **Settings > Account > Chat tags** | **[Automatic ticket tagging](https://support.zendesk.com/hc/en-us/articles/4408829424794)** - **Admin Center > Objects and rules > Tickets >   Settings** |
| **Settings > Account > File sending** | **[Allowing attachments and configuring permissions](https://support.zendesk.com/hc/en-us/articles/4408832757146)** - **Admin Center > Objects and rules > Tickets >   Settings** |
| **Settings > Account > Operating hours** | **[Business hours](https://support.zendesk.com/hc/en-us/articles/4500737327258)** - **Admin Center > Channels > Messaging and   social > Messaging** > Responses section in   channel configuration |
| **Settings > Account > Timezone** | **[Setting a time zone](https://support.zendesk.com/hc/en-us/articles/4408887059866)** - **Admin Center > Account > Appearance >   Localization** |
| **Settings > Account > Security** | **[User authentication in messaging](https://support.zendesk.com/hc/en-us/articles/4411666638746)** - **Admin Center > Account > Security > End user   authentication**  **[Redacting credit card numbers from tickets](https://support.zendesk.com/hc/en-us/articles/4408822124314)**  - A**dmin Center > Account > Security > More   settings** > Zendesk Support tab |

## Chat triggers

If you want to apply automatic responses set up via [Chat triggers](https://support.zendesk.com/hc/en-us/articles/4408884148762) to messaging conversations, you will need
to create new [messaging triggers](https://support.zendesk.com/hc/en-us/articles/5973077601562).

The process for setting up messaging triggers is identical as it is for Chat triggers
with the following exceptions:

- Triggers are created and managed in **Admin Center > Objects and rules >
  Business rules > Messaging triggers**, not on the Chat dashboard.
- Messaging run trigger options are: When a customer requests a conversation,
  When a message is sent, When a conversation is added to the queue, When a
  conversation is assigned from a queue.
- Some routing-related actions are managed with [ticket triggers](https://support.zendesk.com/hc/en-us/articles/4408829019162#topic_tn4_qbq_mpb).

## Chat routing

In messaging for Web Widget or mobile SDKs, when a customer requests assistance from
a live agent during a conversation, a ticket is created, and agents are notified in
the Agent Workspace that a request has been received.

We recommend using [omnichannel routing](https://support.zendesk.com/hc/en-us/articles/6249962577690) to direct messaging tickets to your
agents.

If you choose to use simple routing for messaging tickets, it is based on the [Chat routing rules](https://support.zendesk.com/hc/en-us/articles/4408829019162) defined for your agents.

## Chat reporting

Messaging reports are available on the Support dashboard in Zendesk
Explore. For more information, see [Overview of the Zendesk Support dashboard](https://support.zendesk.com/hc/en-us/articles/4408835985434).

Your account can leverage metrics associated with Tickets in the Support
dashboard and filter by messaging channels.

Key metrics include:

- Estimate staffing - Volume of tickets created per channel, per group,
  per time period
- Monitor team’s performance - Number of tickets solved, Time to
  resolution

**To view messaging reports on the Support dashboard in Explore**

1. Click the Zendesk Products icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/admin_center_product_icon.png)) in the top bar, then select **Analytics**.
2. In the **Dashboards** list, select **Zendesk Support**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/messaging_reporting_ex.png)

Note: Metrics such as First reply time, Unreplied tickets, % One-touch, Two-touch
solves, Comments (all user types), and Agent updates consider only email replies
on the ticket.

## Chat Conversation APIs

Migration to messaging does not apply any code changes to the Chat Conversations API.
When you enable messaging, most CCAPIs will continue to work as expected.
CCAPI-based chatbots, however, may be impacted, depending on your messaging
configuration.

### Understanding the impact on CCAPI-based bots

Because the conversation bot and autoreplies are a central part of messaging
functionality, CCAPI-based chatbots are impacted when messaging is enabled and
they are prevented from being invoked.

### Using chatbots with messaging

If you want to continue using a chatbot on a brand with messaging enabled, you
have a number of options:

**Option 1 (recommended): Moving to Sunshine Conversation APIs**

You can move your existing CCAPI integrations, including CCAPI-based chat bots,
to [Sunshine Conversation APIs](https://docs.smooch.io/guide/api-quickstart/). If you choose this
option, we recommend you do so before migrating your account to messaging.

**Option 2: Creating a Support trigger workaround**

If you do not choose to move your CCAPI integrations to Sunshine Conversations,
you can work around the messaging limitation by creating a Support trigger to
assign a chat bot to any ticket created via messaging:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ccapi_messaging_workaround_trigger.png)