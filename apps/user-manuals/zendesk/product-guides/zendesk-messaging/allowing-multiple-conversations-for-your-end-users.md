# Allowing multiple conversations for your end users 

Source: https://support.zendesk.com/hc/en-us/articles/8008427696410-Allowing-multiple-conversations-for-your-end-users

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

Verified AI summary ◀▼

Enable multiple conversations to let end users handle several messaging threads at once, enhancing their support experience. This feature is available on Web Widget, iOS, Android, and Unity SDKs, but not on social channels. Consider the irreversible changes to user experience and ticket management before activation. Manage settings to control conversation creation and prevent reopening closed threads in the Web Widget.

Multi-conversations let your end users conduct multiple messaging conversations simultaneously with the click of a button, providing faster resolutions to their support issues and a more satisfying customer experience. This feature is available on the Web Widget, iOS SDK, Android SDK, and Unity SDK channels. Multi-conversations are not available for social messaging channels.

Zendesk customers who have access to the Sunshine Conversations API can [set custom titles and avatars for multi-conversations](https://developer.zendesk.com/documentation/conversations/configuring-multi-conversations/).

This article includes the following topics:

- [About multi-conversations](#topic_jft_cmy_1dc)
- [Turning on multi-conversations](#topic_yhy_vjy_1dc)
- [Removing the New conversation button](#topic_nwd_wjy_1dc)
- [Preventing end users from reopening closed conversations in the Web Widget](#topic_x5w_pdk_33c)

## About multi-conversations

This topic includes the following sections:

- [Considerations when turning on multi-conversations](#topic_lbc_hmy_1dc)
- [Active and inactive messaging tickets](#topic_qng_5cj_q2c)
- [Requirements and limitations](#topic_lmh_hmy_1dc)
- [Understanding the agent experience](#topic_epm_hmy_1dc)

### Considerations when turning on multi-conversations

Important: Turning on multi-conversations changes the [end-user experience](https://support.zendesk.com/hc/en-us/articles/8195486407706) and how the Agent Workspace manages conversations. These updates can’t be rolled back.

Before activating multi-conversations for your account, consider the following:

- **All web, iOS, and Android messaging channels are updated when you turn on multi-conversations for any messaging channel.** Channels that aren't selected to display the New conversation button perform as described in [Removing the New conversation button](#topic_nwd_wjy_1dc). Consider turning on multi-conversations for all available messaging channels to align the end-user experience.
- **You can't fully revert to the single conversation experience for end users after you turn on multi-conversations.** You can prevent end users from starting additional conversations by [removing the New conversation button](#topic_nwd_wjy_1dc), but *end users will continue to have access to all conversations in the conversations list*. End users can raise new issues by continuing any conversation in the conversations list.
- **Merging authenticated users no longer combines conversations into a single history.** By default, before turning on multi-conversations, authenticating an end user *after* starting a messaging conversation merges that end user with the matching authenticated user profile, and conversations under the authenticated user profile are combined into a single conversation history. When you turn on multi-conversations, authenticating an end user after starting a messaging conversation still merges them with the authenticated user profile. However, the conversation isn’t merged with prior conversations. This change is irreversible. If you are [authenticating your end users](https://support.zendesk.com/hc/en-us/articles/4411666638746) you should work with your developers to ensure the authentication occurs before starting messaging conversations. Delaying authentication may result in duplicate tickets for the same issue. See [Configuring multi-conversations](https://developer.zendesk.com/documentation/conversations/configuring-multi-conversations/)
 for more information.

### Active and inactive messaging tickets

Multi-conversation behavior in messaging conversations depends on whether the tickets associated with those conversations are *active* or *inactive*.

A messaging conversation is *active* when any of the following are true:

- An AI agent is in the conversation.
- The related ticket's status is New, Open, On-hold, Pending, or Solved.
- An agent [has not ended the messaging session](https://support.zendesk.com/hc/en-us/articles/8009788438042).

A messaging conversation is *inactive* when either of the following are true:

- The related ticket's status is Closed, or in the closed state if [custom ticket statuses are activated](https://support.zendesk.com/hc/en-us/articles/8263915942938#topic_zxw_4yk_fdc).
- An agent [has ended the messaging session](https://support.zendesk.com/hc/en-us/articles/8009788438042).

### Requirements and limitations

Multi-conversations are available on accounts that meet the following requirements:

- Messaging is activated.
- Zendesk iOS or Android SDK version 2.10.0 or later. For the best user experience, version 2.25.0 or later is recommended. Older SDK versions do not support this feature and default to a single conversation experience.
- Zendesk Unity SDK version 3.4.0 or later. Older SDK versions do not support this feature and default to a single-conversation experience.

Currently, the following functionality is not supported for multi-conversations:

- Third-party social messaging channels connected to your account.
- V1 SunCo APIs.
- Social channel linking (allowing an end user to move the conversation from the Web Widget to a social channel) in subsequent conversations on social channels. Social linking is available for only the first conversation started by the end user. End users can't continue subsequent conversations on social channels.

See our [Developer documentation](https://developer.zendesk.com/documentation/conversations/configuring-multi-conversations/) for more information, including additional Sunshine Conversations API capabilities and limitations.

### Understanding the agent experience

In the Agent Workspace, your agents likely support more than one conversation simultaneously. In this sense, turning on multi-conversations does not impact how they work with and view incoming conversations.

Even though each new conversation created by an end user and handed off to an agent results in a new ticket, agent interaction with these tickets and end-user profiles in the Agent Workspace remains unchanged.

## Turning on multi-conversations

Important: Read and understand [these considerations](https://support.zendesk.com/hc/en-us/articles/8195486407706#topic_lbc_hmy_1dc) before turning on multi-conversations.

You can turn on multi-conversations for Web Widget, Android SDK, or iOS SDK in Admin Center.

**To turn on multi-conversations**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Messaging and social >
   Messaging**.
2. At the top of the page, click **Manage settings**.
3. Under Web Widget and Mobile SDKs, expand **Multi-conversations**.
4. Click **Set up multi-conversations**.
5. Click **Turn on multi-conversations for your account**, then select the channels on which you want to offer multi-conversations.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/multi-convos-admin.png)

   Note: Turning on multi-conversations for one messaging channel updates all web, iOS, and Android messaging channels. Any channels not selected during this step perform as described in [Removing the New conversation button](#topic_nwd_wjy_1dc).
6. Click **Save settings**.

After you have turned on multi-conversations for a channel, you can manage the configuration on the Manage multi-conversations settings page or from the Basics tab configuration for [Web Widget](https://support.zendesk.com/hc/en-us/articles/7178617945498#topic_hw2_dsq_gnb) or [mobile SDKs](https://support.zendesk.com/hc/en-us/articles/4408834810394#topic_kzg_ync_gnb).

## Removing the New conversation button

You can remove the New conversation button from a channel to prevent end users from creating new conversations.

However, when you remove the New conversation button, it’s important to understand that end users will not completely revert back to the single-conversation experience.

After the New conversation button is removed, end users:

- Won’t be able to create additional conversations.
- Will see the conversations list when clicking or tapping the launcher button, if they have started multiple conversations.
- Will be able to access all conversations from the conversations list.
- Will raise new issues in their existing conversations from the conversations list.

End users will continue to receive [push notifications](https://support.zendesk.com/hc/en-us/articles/8195486407706#topic_c5z_pny_1dc) (for mobile channels), and [proactive messages](https://support.zendesk.com/hc/en-us/articles/8195486407706#topic_rpg_qny_1dc) (for web channels) will be appended to the latest updated conversation.

**To remove the New conversation button from a channel**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Messaging and social >
   Messaging**.
2. At the top of the page, click **Manage settings**.
3. Under Advanced, expand **Multi-conversations**.
4. Click **Manage multi-conversations settings**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/multi-convos-prevent_reopening.png)
5. Deselect the channels where you want to remove the New conversation button.
6. Click **Save settings**. The New conversation button is removed from those channels.

## Preventing end users from reopening closed conversations in the Web Widget

By default, end users can reopen closed conversations in the Web Widget by adding a new comment. You can prevent end users from doing this by hiding the composer (the text field for adding comments to a conversation).

Note: You must turn on this setting as a prerequisite for [allowing end users to end conversations](https://support.zendesk.com/hc/en-us/articles/10046732687770).

**To hide the composer on closed conversations**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Messaging and social >
   Messaging**.
2. At the top of the page, click **Manage settings**.
3. Under Advanced, expand **Multi-conversations**.
4. Click **Manage multi-conversations settings**.
5. Under Reopening conversations, select **Require users to start a new conversation instead of reopening**.
6. Click **Save settings**.