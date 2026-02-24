# Migrating advanced AI agents from chat to messaging

Source: https://support.zendesk.com/hc/en-us/articles/8357758003098-Migrating-advanced-AI-agents-from-chat-to-messaging

---

Configuring chat channels for advanced AI agents is no longer recommended. Instead, you should migrate your advanced AI agents to work on messaging channels. This article walks you through the migration process.

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | AI agents - Advanced |

Configuring chat channels for advanced AI agents is no longer recommended. Instead, you should migrate your advanced AI agents to work on messaging channels. This article walks you through the migration process.

This article contains the following topics:

- [Before you start](#topic_pm4_zc5_33c)
- [Step 1: Clone your advanced AI agent](#topic_txz_1d5_33c)
- [Step 2: Update your advanced AI agent’s configuration](#topic_w5n_cd5_33c)
- [Step 3: Test your advanced AI agent’s conversation flows](#topic_cw2_3d5_33c)
- [Step 4: Finalize and launch your advanced AI agent on messaging channels](#topic_wt3_jd5_33c)
- [Step 5: Monitor your advanced AI agent’s performance](#topic_jql_kd5_33c)

## Before you start

Before you start, keep the following requirements and considerations in mind.

### Requirements

To successfully migrate an advanced AI agent from chat to messaging, you’ll need:

- The [client admin role](https://support.zendesk.com/hc/en-us/articles/4408832171034#topic_thq_lnf_dgc) in AI agents - Advanced
- A [sandbox environment](https://support.zendesk.com/hc/en-us/articles/6150628316058) with [Web Widget set up](https://support.zendesk.com/hc/en-us/articles/4409103246874)
- (Optional) Access to your website and/or app's source code
 - This is required only if you want to configure more complex automation using actions than is available by default.

### Considerations

When migrating an advanced AI agent from chat to messaging, you may wish to consider creating multiple advanced AI agents for different types of messaging channels. For example, you might want to have one AI agent for web-based messaging and another for social messaging (such as WhatsApp).

The reason for this is that request types and communication styles differ depending on the channel a customer reaches out on. In addition, which features are supported depends on the messaging channel. See [Getting started with social messaging](https://support.zendesk.com/hc/en-us/articles/4408831648794)
for more information on the available channels.

## Step 1: Clone your advanced AI agent

To ensure there's no disruption in your customer service, [clone the advanced AI agent](https://support.zendesk.com/hc/en-us/articles/8357749415066#topic_mkr_hb3_23c) you want to migrate. The original AI agent will stay active on your chat channels until you’ve completed the steps below and are ready to launch your migrated AI agent on messaging channels instead.

Note: Analytics and other historic data are *not* transferred from the original AI agent to the cloned AI agent.

## Step 2: Update your advanced AI agent’s configuration

In the cloned AI agent, you should review and adjust the forms, actions, and escalation strategy to ensure they work on messaging channels.

This section contains the following topics:

- [Step 2.1 Recreating the pre-chat form](#topic_brf_2d5_33c)
- [Step 2.2: Reviewing and adjusting actions](#topic_i3s_fd5_33c)
- [Step 2.3: Re-evaluating your escalation strategy](#topic_al1_hd5_33c)
- [Step 2.4: Creating tickets for AI agent–handled requests](#topic_y5j_xkw_33c)

### Step 2.1 Recreating the pre-chat form

The [pre-chat form](https://support.zendesk.com/hc/en-us/articles/4408882974234) is not available on messaging channels. If you still want to collect information from the customer before the AI agent conversation starts, you’ll need to recreate the form. See [Using and sanitizing forms in conversation flows for advanced AI agents](https://support.zendesk.com/hc/en-us/articles/8357720543514).

Tip: Customers are more likely to drop off if asked to provide a lot of information immediately upon entering a conversation. It’s recommended to design your conversation flows to allow customers to ask their questions first, and use a form to collect user information only if the conversation needs to be escalated.

### Step 2.2: Reviewing and adjusting actions

Not all actions that are available on chat channels are available on messaging channels. [Review the actions you created](https://support.zendesk.com/hc/en-us/articles/8566644914202) for your advanced AI agent and adjust them as needed.

The following table summarizes the actions available on chat channels compared to messaging channels. The ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_table_icon_x.png) icon means an action isn’t available by default and requires additional configuration.

| | |
| --- | --- |
| **Chat action** | **Messaging action** |
| [Get customer info](#topic_amk_xg5_33c) | Get user |
| [Update customer info](#topic_pdg_1h5_33c) | Update user |
| [Get tag](#topic_e1p_bh5_33c) | |
| [Add tag](#topic_cgk_ch5_33c) | Add user tag Add conversation tag Overwrite user tag Overwrite conversation tag |
| [Trigger reply](#topic_l5r_dh5_33c) | Trigger reply |
| [Leave channel](#topic_m14_2h5_33c) | |

For more information on the actions available for messaging, see [Available CRM actions for advanced AI agents and Sunshine Conversations](https://support.zendesk.com/hc/en-us/articles/8357734565402).

If there’s information you want to continue using that’s not available by default, you’ll need to customize the Web Widget snippet to capture it. See [Using messaging metadata with the Zendesk Web Widget and SDKs](https://support.zendesk.com/hc/en-us/articles/5658339908378).

#### Get customer info

This action allows you to retrieve visitor information on Zendesk. This information can then be saved to personalize your messages or create reply variations.

The table below compares the specific customer info that can be retrieved and used in dialogues in chat and messaging. The ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_table_icon_x.png) icon means an action isn’t available by default and requires additional configuration. The ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_table_icon_check.png) icon means the information can be defined in your Web Widget code. For help, see the following articles:

- [Using messaging metadata with the Zendesk Web Widget and SDKs](https://support.zendesk.com/hc/en-us/articles/5658339908378)
- [Setting up user authentication for messaging](https://support.zendesk.com/hc/en-us/articles/4411666638746)
- [Custom Web Widget initialization behavior](https://developer.zendesk.com/documentation/conversations/messaging-platform/users/authenticating-users-help-center/#custom-web-widget-initialization-behavior)

| | | |
| --- | --- | --- |
| **Customer info** | **Chat “Get customer info” action details** | **Messaging “Get user” action details** |
| Name | - Display name (what users enter in the [pre-chat   form](../configuring-the-chat-widget/enabling-the-pre-chat-form-on-the-chat-widget.md)) | - Given name - Surname |
| Locale | - Current region - Current country - Current city | - Locale in [BCP 47](https://en.wikipedia.org/wiki/IETF_language_tag#List_of_major_primary_language_subtags)   format |
| Email | | |
| External ID | | |
| Phone | | |
| Notes | | |
| Status | | |
| Device | | |
| Tags | | |
| Avatar URL | | |
| [Metadata](https://support.zendesk.com/hc/en-us/articles/5658339908378) | | |

#### Update customer info

This action allows the AI agent to fetch the information visitors offer during a conversation and update it on the visitor's Zendesk ticket.

The table below compares the specific customer info that can be retrieved and used in dialogues in chat and messaging. The ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_table_icon_x.png) icon means an action isn’t available by default and requires additional configuration. The ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_table_icon_check.png) icon means the information can be defined in your Web Widget code. For help, see the following articles:

- [Using messaging metadata with the Zendesk Web Widget and SDKs](https://support.zendesk.com/hc/en-us/articles/5658339908378)
- [Setting up user authentication for messaging](https://support.zendesk.com/hc/en-us/articles/4411666638746)
- [Custom Web Widget initialization behavior](https://developer.zendesk.com/documentation/conversations/messaging-platform/users/authenticating-users-help-center/#custom-web-widget-initialization-behavior)

| | | |
| --- | --- | --- |
| **Customer info** | **Chat “Update customer info” action details** | **Messaging “Update user” action details** |
| Name | - Display name (what users enter in the [pre-chat   form](../configuring-the-chat-widget/enabling-the-pre-chat-form-on-the-chat-widget.md)) | - Given name - Surname |
| Locale | - Ccurrent region - Current country - Current city | - Locale in [BCP 47](https://en.wikipedia.org/wiki/IETF_language_tag#List_of_major_primary_language_subtags)   format |
| Email | | |
| External ID | | |
| Phone | | |
| Notes | | |
| Status | | |
| Device | | |
| Tags | | Update Sunshine tag |
| Avatar URL | | |
| [Metadata](https://support.zendesk.com/hc/en-us/articles/5658339908378) | | |
| Priority | | |
| Organization ID | | |
| Group ID | | |
| Assignee ID | | |
| Brand ID | | |

#### Get tag

This action allows you to pull existing tags from chat into an advanced AI agent. The Get tag action doesn’t exist for messaging.

However, you can add tags as part of the conversation metadata. The AI agent can access these tags through the Get conversation action, where the *Field to retrieve* value is set to *(Metadata)*. You then need to add a code snippet to the Web Widget. The action requires a prefix of `"zen:ticket:tags":` to retrieve tags successfully. See [Setting conversation fields and tags](https://support.zendesk.com/hc/en-us/articles/5658339908378#topic_fxm_qh3_xxb).

#### Add tag

This action adds custom tags to a chat which can give you insights into your tickets.

On messaging, there are four tag-related actions:

- [Add user tags](https://support.zendesk.com/hc/en-us/articles/8357734565402#h_01G7EHGR7P2Q3NRX65WGX817VJ)
- [Overwrite user tags](https://support.zendesk.com/hc/en-us/articles/8357734565402#h_01JEBDARZB1AT5KMBRMMQPS5QB)
- [Add conversation tags](https://support.zendesk.com/hc/en-us/articles/8357734565402#01HHY64VZ9WV1DMGS60HQ7XRCZ)
- [Overwrite conversation tags](https://support.zendesk.com/hc/en-us/articles/8357734565402#01HHY64A7HYDBPY03AZ5P9GG41)

#### Trigger reply

This action stays the same. See [Triggering a reply when a conversation starts or becomes inactive](https://support.zendesk.com/hc/en-us/articles/8357756623770#topic_axm_d23_g3c).

#### Leave channel

This action is used to [show the queue position to customers](https://support.zendesk.com/hc/en-us/articles/8357720370330-Best-practices-of-actions-Zendesk-Chat#h_01FHAGEBFCFWDJNE6T3GBK6JZP) for chat and is not available for messaging.

### Step 2.3: Re-evaluating your escalation strategy

Migrating from chat to messaging presents an opportunity to re-evaluate your escalation strategy. For more information, see [About escalation strategies and flows for advanced AI agents](https://support.zendesk.com/hc/en-us/articles/8357756604186).

### Step 2.4: Creating tickets for AI agent–handled requests

With chat, you could [automatically create a ticket in Support](https://support.zendesk.com/hc/en-us/articles/8357772371482) when a chat ended and attach the transcript. To create the same result in messaging, it’s recommended to use the [AI agent ticket feature](https://support.zendesk.com/hc/en-us/articles/9204149016346), which automatically creates tickets for messaging conversations that were handled entirely by your AI agent.

## Step 3: Test your advanced AI agent’s conversation flows

After you’ve updated your advanced AI agent’s configuration, the next step is testing. Before going live, perform thorough testing to ensure all conversation flows work as intended. See [Testing conversation flows in advanced AI agents](https://support.zendesk.com/hc/en-us/articles/8357758879130).

## Step 4: Finalize and launch your advanced AI agent on messaging channels

Finalizing and launching your advanced AI agent consists of the following tasks:

1. If you cloned your AI agent to a sandbox environment and made any updates to the sandbox Web Widget code, make sure to update the production Web Widget code to match, including any metadata, user authentication, or tags.
2. Update the IDs of any build items to make sure they point to your production subdomain, not your sandbox domain. You’ll need to do this for:
   - **Actions**: See [Editing an action](https://support.zendesk.com/hc/en-us/articles/8566644914202#topic_npt_qpl_rgc).
   - **Transfer groups**: See [Managing messaging channel settings for an advanced AI agent](https://support.zendesk.com/hc/en-us/articles/10050437105946#topic_yf3_1gk_jhc).
   - **Forms**: See [Using and sanitizing forms in conversation flows for advanced AI agents](https://support.zendesk.com/hc/en-us/articles/8357720543514).
3. [Set your advanced AI agent as the default responder](https://support.zendesk.com/hc/en-us/articles/8357757911834) on the messaging channels of your choice.

## Step 5: Monitor your advanced AI agent’s performance

The final and ongoing step is to monitor your advanced AI agent to ensure everything is working as intended. See [Analyzing advanced AI agent performance with the reporting dashboard](https://support.zendesk.com/hc/en-us/articles/9510024609178).