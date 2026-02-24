# Adding the Slack Direct Messages channel

Source: https://support.zendesk.com/hc/en-us/articles/4629038081306-Adding-the-Slack-Direct-Messages-channel

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Live chat and messaging Team, Professional, or Enterprise |

Location: Admin Center > Channels > Messaging and social >
Messaging

This article describes how to add the Slack Direct Messages channel.

With the Slack DM channel, end users can create tickets by sending a direct message to a handle within Slack. These tickets are then managed in Zendesk, as with other messaging tickets, using triggers, automations, and macros. This feature supports both internal help desk use cases and business to business conversations.

This article includes the following sections:

- [About the Slack Direct Messages channel](#topic_wd1_zjm_25b)
- [Creating a dedicated Slack handle](#topic_rtk_w2w_v5b)
- [Adding the Slack Direct Messages channel](#topic_mjq_zjm_25b)
- [Using the integration](#topic_k12_rmf_g5b)

## About the Slack Direct Messages channel

The Slack Direct Messages channel facilitates collaboration between an end user and a Zendesk agent through a dedicated handle added to your Slack workspace.
End users can send direct messages for assistance, which are converted into messaging tickets.

Note: The Slack Direct Messages channel is not a replacement for the [Slack for Zendesk Support integration](https://support.zendesk.com/hc/en-us/articles/4408833756698), which provides internal teams a way to collaborate and create tickets within Slack.

You can perform the following actions when the channel is created:

- Internal users can send a direct message to a handle and raise a Support ticket within Zendesk.
- Reply to the ticket from the Zendesk Agent Workspace
- Continue a conversation with an end user after a ticket created through Slack DMs has been closed
- Use automations, macros, and triggers on a Slack Direct ticket, as you would with other messaging tickets

### Requirements and limitations

The Slack account you are integrating must have [Require App Approval](https://slack.com/help/articles/222386767-Manage-app-approval-for-your-workspace#h_01EC8H3AWBYEAAN5AKBTVKPC5K) enabled.

In addition, the following limitations apply:

- Slack DM as a channel is intended to support 1:1 requests.
 Currently, one to many (multi-conversation) is not supported.
- Thread conversations are not supported for this iteration, this means replying within a thread in the direct message will not come over to Zendesk.
- Sending a direct message to the Slack handle, while logged in as the handle, will *not* create a live message in Zendesk (to prevent echoing).
- @replies to the handle within a channel will not start a messaging conversation in Zendesk.
- By default, five file types are [supported as attachments](../live-chat-agent-guide/sending-files-in-a-chat.md) (.pdf, .png, .jpeg, .gif, and .txt) when file sending is activated. Other file types can be added to the allowed list.

## Creating a dedicated Slack handle

Before creating the Slack DM channel, you’ll need to create a dedicated Slack handle, or user, to use with the channel. The handle can be named for its intended use – for HR Services, customer on-boarding, or anything you want to associate with the Slack Direct Messages channel.

This handle is created in Slack. See the Slack article [Getting started for new Slack users](https://slack.com/intl/en-au/help/articles/218080037-Getting-started-for-new-Slack-users) for instructions.

Any agent or admin signed into Slack with the global handle can see and participate in the conversation. However, Slack does delete conversations after a certain number is reached. A conversation deleted in Slack still remains available to agents and admins through the Agent Workspace.

## Adding the Slack Direct Messages channel

When your Slack handle has been created, you can add Slack Direct Messages as a messaging channel.

**To add the Slack channel**

1. Sign in to your Slack account, using the Slack handle you want to add.
2. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Messaging and social >
   Messaging**.
3. Click **Add channel**, then select **Slack**.
4. Enter a **Channel name** that will allow users to easily identify your account.
5. If your account has [multiple brands](https://support.zendesk.com/hc/en-us/articles/4408829476378), select a **Brand** to associate with the channel.
6. Click **Next**, then click **Link workspace in Slack** .
7. On the approval page, click **Allow**. If the Allow button is not active, make sure you have enabled [Require App Approval](https://slack.com/help/articles/222386767-Manage-app-approval-for-your-workspace#h_01EC8H3AWBYEAAN5AKBTVKPC5K) on the Slack account.

   Your Slack account is now an active channel in Zendesk.

You can now finish the setup process:

- [**Set up your workflows**](https://support.zendesk.com/hc/en-us/articles/4408831648794#topic_dzb_jyr_zqb).
 Configure any triggers, automations, and views you want to associate with the Slack channel.
- [**Give agents access to messaging**](https://support.zendesk.com/hc/en-us/articles/6073485578010). Set agent roles for agents who will participate in social messaging conversations, as needed.

## Using the integration

Slack Direct Messages can be used in two ways:

- As an [Internal help desk support](#topic_ocw_vmf_g5b)
- As [Partnership support via Slack Connect](#topic_sv4_vmf_g5b)

### Internal help desk support

You can set the Slack handle linked to the Slack Direct Messages channels as IT support, HR services, sales, or any internal workflow that may need its own channel for conversations.

Any direct message to the handle will come in as a messaging conversation to Zendesk via Slack. This allows you to set up triggers to assign messages to groups, and have an agent directly support your employees using live messages. Groups can then use Macros and other support apps to serve your employees and help them get the support they need.

Using the Slack Direct Messages channel as an internal help desk, you can:

- See the full conversation history between the employee and the Slack handle and create a complete history of that employee's records with this group
- Link the employee user profile to any existing profile for a full and complete record of your employee
- Report from Explore on groups performance and see a full history of support provided to employees from the designated Slack handle
- Manage all of your channels in the Zendesk Admin Center

### Partnership support via Slack Connect

Slack Direct Messages allow you to create a partnership integration via [Slack Connect](https://slack.com/intl/en-au/connect). This lets you invite partners and contractors to collaborate with the Slack handle via a Connect channel. Utilizing this approach you can set up your handle to support onboarding new customers with premium support or marketing collaborations and a lot more.

**To configure your handle to support customer onboarding**

1. Create a [Slack Connect channel](https://slack.com/intl/en-au/help/articles/360035092414-Use-Slack-Connect-to-work-with-other-companies-in-channels) with the handle and invite the collaborator.
2. Now that the connection has been made between your workspace and the collaborators, inform them that they can directly message the handle at any time.

- Direct messages with the handle will come across to Zendesk, much like the internal employee support allowing you to manage and support these partnerships.
- Zendesk user profiles are automatically created for end users who send direct messages.
- Explore reports allow you to gain insight into these collaborations.