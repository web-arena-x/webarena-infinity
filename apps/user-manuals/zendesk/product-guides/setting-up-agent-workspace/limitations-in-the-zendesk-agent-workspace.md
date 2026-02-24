# Limitations in the Zendesk Agent Workspace

Source: https://support.zendesk.com/hc/en-us/articles/4408821805338-Limitations-in-the-Zendesk-Agent-Workspace

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Live chat and messaging Team, Professional, or Enterprise |

This article describes some current limitations in the Zendesk Agent Workspace. As product development continues, Zendesk will work to add more features and remove limitations.
To learn more about items to consider before you migrate to the Zendesk Agent Workspace, see [Migrating to the Zendesk Agent Workspace](https://support.zendesk.com/hc/en-us/articles/4583448479514).

This article contains the following sections:

- [Security limitations](#topic_kb4_mqr_vkb)
- [Dashboard limitations](#topic_j5d_rvl_mkb)
- [Messaging limitations](#topic_u4c_wzp_wnb)
- [Chat limitations](#topic_f2b_hgp_wnb)
- [Data Center Location (DCL) limitations](#topic_lts_bdf_vpb)

**Related articles**

- [Documentation resources for the Zendesk Agent Workspace](https://support.zendesk.com/hc/en-us/articles/4408827107226)
- [About the Zendesk Agent Workspace](https://support.zendesk.com/hc/en-us/articles/4408821259930)

## Security limitations

Unlike Support, Chat does not support the concept of restricted agents - all Chat agents have access to all chat messages. If you are using restricted agents such as light agents in Support, it is possible for those agents to access chat messages. Light agents can serve chats in the Chat mobile app, but they cannot serve chats in the Agent Workspace because they have a Light agent role, not an Agent role in Support. An Agent role is required to serve chats in the Agent Workspace.

## Dashboard limitations

This section describes some important limitations for the settings-only Chat dashboard in the Zendesk Agent Workspace.

Limitations for administrators include:

- Administrators will not be able to initiate proactive chats.
- The Visitors List only has information about ongoing chat conversations. Visitor-level browsing information is not available. Instead, refer to [Visitor path](https://support.zendesk.com/hc/en-us/articles/4408829170458#topic_ehg_1qz_vkb) in the Agent Workspace.
- The Visitors List is a legacy Chat feature. It does not apply to messaging.
- Tags are not visible in chat history. Admins will be redirected to the Agent Workspace to view or edit any tags associated with that chat.

Limitations for agents include:

- Multi-agent conversation options are not supported and agents will not be able to initiate chats.
- The export transcript option is not available for ongoing chats.
- Custom chat apps are not available, but you can create custom Support apps and use them for chats in the Zendesk Agent Workspace.

## Messaging limitations

This section describes some important messaging limitations for social and web messaging in the Zendesk Agent Workspace.

- Incidents can link to problem tickets, but when the problem ticket is solved, public comments are sent via email only if the user has an email address in their user profile.
- All ticket-based [reporting](https://support.zendesk.com/hc/en-us/articles/4408822342938) works except for metrics such as Unreplied tickets, % One-touch, Two-touch solves, Comments (all user types), and Agent updates. These metrics only consider email replies on the ticket.
- Sunshine Conversations channels do not receive events from WhatsApp if the business number is blocked by an end user. In this case, the events log will not show the delivery status of an agent message sent to the end user.
- To create a clickable link in a messaging conversation in Agent Workspace, you must use a complete URL. Hyperlinks are not active.

## Chat limitations

This section describes some important Chat limitations in the Zendesk Agent Workspace.

- If your account supports a high volume of chats or has a large number of chat-only agents, check with your Zendesk account representative before migrating to the Zendesk Agent Workspace. For best performance, follow these guidelines:
 - Do not exceed 1,300 online Chat agents actively serving chats. If necessary, you can have up to 2,000 Chat agents actively serving chats, but you will need to reduce the number of concurrent chats served on your account to prevent potential performance degradation.
 - No more than 4,000 concurrent chats with 200,000 total chats per day.
 - No more than 6,000 concurrent visitors with 300,000 total visitors per day.
    Concurrent visitors is the sum of all visitors on your website who have the Web Widget open to chat.
- Apps and macros are available for chats, with the following limitations:

 - Support apps have some limitations during chats. See the [Ticket editor API](https://developer.zendesk.com/apps/docs/support-api/ticket_editor#api-restrictions-when-ticket-is-in-chat-mode) . Some apps will not be able to add content in chats.
 - Chat apps cannot be downloaded in the Zendesk Agent Workspace.
 - Macros that switch the assignee value to an online agent or group do not initiate a chat transfer. When the original user submits the ticket, the ticket assignee is updated to an online agent or group and the chat is ended.
 - Macros can post text into chats, but text indentions are not supported.
- To prevent application conflicts and potential tracking issues, Zendesk does not recommend using the Zendesk [Chat app](https://www.zendesk.com/apps/support/zendesk-chat/) with the Zendesk Agent Workspace. When the Agent Workspace is enabled, the Zendesk Chat app is automatically disabled on your account. See [Activating the Zendesk Agent Workspace](https://support.zendesk.com/hc/en-us/articles/4581758611866).
- Chat actions such as invite agent, start a conversion with another agent (or visitor), and export transcript, are not supported.
- After migration to the Zendesk Agent Workspace, chat transcripts are no longer counted as end-user comments in Explore which may impact your Explore reports.
- Agents can transfer chats, provided Chat departments are mapped to Support groups. See [Migrating to the Zendesk Agent Workspace](https://support.zendesk.com/hc/en-us/articles/4583448479514) for details.
- Chat [shortcuts with options](https://support.zendesk.com/hc/en-us/articles/4408832184346#topic_kwr_mgd_h2b) are not supported. Dynamic content is not supported in chat shortcuts.
- Agents must end all chats before logging out.
- After migrating Chat departments to Support groups, App developers should update all public APIs for Chat department Create, Update, and Delete to public APIs for Support group Create, Update, and Delete.
- Agents with custom roles may not be able to use the Agent Workspace because of channel-specific settings. Make sure your custom roles allow for Chat access. Light agents cannot serve chats in the Zendesk Agent Workspace. They need to be upgraded to an Agent role.
- Agent idle timeout is available on accounts that [turn on omnichannel routing with unified agent status](https://support.zendesk.com/hc/en-us/articles/5866925319962). [Chat-specific idle timeout](https://support.zendesk.com/hc/en-us/articles/4408828519706#topic_egs_t4j_ws) isn't available and agent idle timeout settings carried over from the Standard agent interface after migration to the Agent Workspace cannot be changed.
- To create a clickable link in a chat conversation in the Agent Workspace, you must use a complete URL. Hyperlinks are not active.
- Transferring chats in bulk to a new group is possible but not recommended. When doing so, the tickets associated with chats are transferred to the new group, but the chat conversations remain in the original group's queue. Therefore, only agents in the original group are notified when a customer responds to the chat. This limitation applies only to chats transferred in bulk. When transferring a chat individually, both the ticket and the chat conversation are transferred to the new group.

## Data Center Location (DCL) limitations

Currently, certain messaging features in the Zendesk Agent Workspace are not supported by Zendesk's [Data Center Location](https://support.zendesk.com/hc/en-us/articles/4408838409754-About-Data-Center-Location) (DCL) offering. Our [Regional Data Hosting Policy](https://support.zendesk.com/hc/en-us/articles/4408883599130-Regional-Data-Hosting-Policy) lists all covered features. This topic describes the current DCL limitations in the Agent Workspace, specifying covered and uncovered features within the Agent Workspace. Zendesk is working to remove these limitations and ensure that Agent Workspace fully supports DCL.

In the Agent Workspace, the Support ticketing system *is* covered by DCL.
This includes tickets, users, attachments, and the Facebook and X (formerly Twitter)
channels you activate through **Facebook pages** and **X accounts** in Admin Center.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_dcl_limitations_admin_center.png)

Live chat features (formerly known as Chat) *are* covered by DCL with exceptions listed in the [Regional Data Hosting Policy](https://support.zendesk.com/hc/en-us/articles/4408883599130-Regional-Data-Hosting-Policy). These are the live chat features you activate from the Chat dashboard. See [Location of Service Data in Zendesk Chat](https://support.zendesk.com/hc/en-us/articles/4408830625690) for details.

Messaging features that you activate in **Admin Center > Channels >
Messaging setup** *may not be covered* by DCL, although data locality support for all messaging customers is a current priority for Zendesk. Until then:

- Accounts created with messaging enabled after April 17, 2023 may have Service Data hosted in any of the AWS Regions where Zendesk hosts data. For now, Zendesk does not currently support transfers of this service to other supported regions. If your account is not currently hosted in the desired region of choice, a new instance will need to be created. Reach out to your account representative for more assistance.
- Accounts created before this date will require hosting in both the US and EEA regions, unless customers have selected a data locality hosting region. In which case only customers based in the US will have full data locality support on messaging.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_dcl_limitations_messaging2.png)

You can confirm whether messaging has been activated in your account on the Chat dashboard by checking for a banner at the top of the page:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_dcl_limitations_chat_all2.png)