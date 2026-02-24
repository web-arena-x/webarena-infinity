# Enabling customers to continue conversations through social channels

Source: https://support.zendesk.com/hc/en-us/articles/4409103296154-Enabling-customers-to-continue-conversations-through-social-channels

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Live chat and messaging Team, Professional, or Enterprise |

Social channel linking connects the messaging Web Widget to your WhatsApp, Facebook Messenger, and Instagram DM channels, allowing your end users to start conversations via the Web Widget and continue them in the social channel of their choice.

This article includes the following topics:

- [About social channel linking](#topic_o3r_5w4_jrb)
- [The end user experience](#topic_ujv_5w4_jrb)
- [The agent experience](#topic_dkz_5w4_jrb)
- [Enabling social channel linking](#topic_dpd_vw4_jrb)

## About social channel linking

When social channel linking is enabled on an account, end users can switch their messaging conversation from the Web Widget to their preferred social channel.
This allows them to step away from (but not end) a conversation while, for example, waiting for a response from an agent, and return to it at their convenience, from another device or location.

To use social channel linking, your account must meet the following requirements:

- Is on a Zendesk Suite plan
- Agent Workspace is enabled
- Has connected one or more of the following social channels to your Zendesk account:
 - [WhatsApp](https://support.zendesk.com/hc/en-us/articles/4408842821786)
 - [Facebook Messenger](https://support.zendesk.com/hc/en-us/articles/4408835753370)
 - [Instagram DM](https://support.zendesk.com/hc/en-us/articles/4408835013018)

It’s important to note that, because of social channel-side limitations, each social channel only displays the responses sent and received through that channel. A conversation’s entire history, regardless of the channel it was conducted in, appears in the Web Widget. We’ll discuss this further in [The end user experience](#topic_ujv_5w4_jrb), below.

## The end user experience

When social channel linking is enabled, an end user can choose at any point to switch their Web Widget-based conversation to any enabled social channel listed above. The end user can then switch back and forth between the Web Widget and the selected social channel to continue the conversation.

The end user is in control of where the conversation takes place. As such, there are a few steps they need to take to switch the conversation from Web Widget to another channel.

Note: Channel-side steps for the end user can vary for each platform and may not precisely follow the path described below.

Once social channel linking is enabled by an admin, an options menu icon appears at the top of Web Widget. When the customer hovers over this icon, the enabled social channels are displayed:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/crosschannel_menu_open.png)

The end user selects their channel, and is asked to scan a QR code or open the app on their current device. They can also choose to return to the previous screen by clicking the back icon in the top-left:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/crosschannel_QR_WA.png)

When the conversation begins in the social channel, the end user will first be asked to verify that the link is correct, and they can continue the conversation in the social channel as needed. Any comments sent by the agent will appear in the selected social channel until the end user chooses to return to the Web Widget, at which point those comments appear in the widget.

Over the course of the conversation, the end user can choose to connect to different social channels, and only the conversation conducted through that social channel is visible in the conversation history.

For instance, a customer can choose to switch their conversation from the widget to their Facebook Messenger account while they’re away from their desktop, then returns to the Web Widget when they’re back at their computer. Later, they decide to switch their conversation to their WhatsApp account.

- In the Web Widget, the entire conversation – Web Widget, Facebook Messenger, and WhatsApp comments – appears in the conversation history, with each comment noting the channel used.
- In Facebook Messenger, the conversation history begins with the first comment left by either the end user or agent *after* the end user has switched the conversation to Facebook Messenger, and does not include any comments while the conversation was conducted via Web Widget or WhatsApp.
- In What’sApp, the conversation history begins with the first comment left by either the end user or agent *after* the end user has switched the conversation to WhatApp, and does not include any comments while the conversation was conducted via Web Widget or Facebook Messenger.

End users can disconnect their widget conversation from the social channel by returning to the Web Widget and clicking Disconnect:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/crosschannel_disconnect.png)

## The agent experience

Agents communicate with customers through the Agent Workspace, regardless of the channel the end user is on.

In the Agent Workspace, the end user’s channel selection is indicated in the conversation history:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/crosschannel_AW_ex.png)

By default, agent responses will be delivered to whichever channel was last used by the end user. All messages exchanged between the end user and the agent will be synced to the Web Widget. This continues as long as the end user's social messaging identity remains linked to the Web Widget.

The customer's social channel identity is added to the customer card in addition to the existing information.

If the end user has previously reached out using the social messaging channel, then customers created through that social messaging channel will be merged with the related customer in the Web Widget. Older non-closed tickets will be Closed. The agent should use the most recent non-closed ticket for responding to the end user.

Note: The above does not apply to Instagram DM. If a customer links Instagram DM from the Web Widget, a new ticket will be created.

## Enabling social channel linking

You can enable social channel linking in your account’s Admin Center.

**To enable social channel linking**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Messaging and social >
   Messaging**.
2. Click the Web Widget you want to use with channel linking.
3. In the widget’s Basics tab, under Allow customers to switch channels, select the social channels you want to link to the widget. You can only select channels currently enabled in your account.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/admin_ux_xchannel.png)
4. Click **Save settings**.

You can disable social channel linking by returning to this page and deselecting the channels you no longer want to connect, then clicking **Save settings**.