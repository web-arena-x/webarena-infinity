# About Sunshine Conversations in Zendesk Suite

Source: https://support.zendesk.com/hc/en-us/articles/5514406080538-About-Sunshine-Conversations-in-Zendesk-Suite

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

Zendesk Suite Professional, Enterprise, and Enterprise Plus plans come with a low-volume,
self-service version of Sunshine Conversations , which lets you access the Sunshine
Conversations API through Admin Center, without having to purchase a separate Sunshine
Conversations license.

Note: If you are a Suite Professional, Enterprise, or Enterprise
Plus user and previously purchased a Sunshine Conversations license, you can choose
to access your account via the new Admin Center UI or the Sunshine Conversations
dashboard. Your account and functionality will not be impacted.

This article includes the following sections:

- [Overview of Sunshine Conversations capabilities](#topic_ljj_31y_1xb)
- [The Sunshine Conversations workflow](#topic_zkr_31y_1xb)
- [Understanding channel integrations](#topic_nnw_31y_1xb)
- [Configuring conversational control (Sunshine Conversations custom bot users only)](#topic_fwd_ylm_y1c)

For subscription and usage information, see [About Sunshine Conversations platform access and
support](https://support.zendesk.com/hc/en-us/articles/5514407356954).

## Overview of Sunshine Conversations capabilities

Sunshine Conversations lets you extend your messaging options by
providing a unified API to manage and automate your conversations across
multiple channels. You can integrate your Zendesk instance with another app
or program, such as a custom bot or an external reporting tool, or an app
that triggers a desired action.

Adding an external chatbot to your
Zendesk setup is one of the more common usage scenarios. You can connect with
customers through channels that are not currently available through [Zendesk’s internal messaging channel](https://support.zendesk.com/hc/en-us/articles/4408846454682)
and [manage these channels through the AI agents
page](https://support.zendesk.com/hc/en-us/articles/5064149334426) in Admin Center. Then your agents can respond to customers
across all of these channels from a single interface, the Agent Workspace.

## The Sunshine Conversations workflow

The basic process for setting up a Sunshine Conversations integration
between your third-party tool and Zendesk involves tasks completed in the
third-party tool’s UI and across Admin Center,

These tasks include:

- **Creating and configuring your third-party tool**. This is
  completed in the tool’s own UI. Each tool has its own unique setup flow. Part of
  the process is, in most cases, sharing some details about your Zendesk account,
  so have that information handy. See [Managing third-party bots in Admin
  Center](https://support.zendesk.com/hc/en-us/articles/5064149334426) for more information.
- **Creating a Conversations API key.** An API key identifies and
  authenticates an application or user, so you can create the integration
  between the app and Sunshine Conversations. See [Using the Conversations API](https://support.zendesk.com/hc/en-us/articles/4576088682266) for
  more information.
- **Creating and managing a conversation integration**. The
  integration is how you link your business with Sunshine Conversations, and
  the channels you want to connect to. This task includes creating a webhook
  and selecting the conversation events that trigger it. See [Integrating conversations in Admin
  Center](https://support.zendesk.com/hc/en-us/articles/4576083789850) for more information.
- **Adding the channel to the Agent Workspace**. Finally, if
  you’re adding a chatbot or social channel, you can add it to Agent
  Workspace, so your agents can respond to customer support requests across
  all channels without switching platforms. See [Adding Sunshine Conversations channels to
  the Zendesk Agent Workspace](https://support.zendesk.com/hc/en-us/articles/4408836484378) for more information.
- **Configuring conversation control** (Sunshine Conversations custom bot users
  Switchboard users only). Decide how the switchboard determines control when
  conversations are resolved. See [Conversational control model](https://docs.smooch.io/guide/switchboard/#conversational-control-model) in our
  Sunshine Conversations documentation for more information.There is no action
  required if you are using the out-of-the-box messaging experience.

## Understanding channel integrations

Channel integration means, simply put, that you are creating a link between your
Zendesk instance and an external system or channel.

Note: Before integrating an external tool, we recommend installing and completing
any tasks required by the third-party tool. Visit the tool’s website or help
center for information on those tasks.

The types of external
channels you can integrate include:

- **Over-the-top (OTT) messaging apps**, such as Apple Messages for Business
  or Viber
- **SMS**, through integrations with third parties like
  Twilio

The list below includes channels you can connect to with Sunshine Conversations.
Follow the links to learn more about each channel.

- Sunshine Conversations [Web Messenger](https://support.zendesk.com/hc/en-us/articles/4408834108186#topic_bxb_2dw_m4b)
- [Apple Messages for Business](https://register.apple.com/resources/messages/messaging-documentation/#introduction)
- SMS (requires a [MessageBird](https://developers.messagebird.com/api/sms-messaging/) or [Twilio](https://www.twilio.com/docs/sms/api) SMS account)
- [Telegram](https://core.telegram.org/bots)
- [Google Business Messages](https://businessmessages.google/)
- [Kakao](https://www.kakaocorp.com/page/?lang=ENG&tab=all)
- [Viber](https://developers.viber.com/docs/)

## Configuring conversational control (Sunshine Conversations custom bot users only)

If you are using Switchboard APIs to create a custom bot, you’ll need to
define how resolved conversations are handled by the switchboard.

**To set conversation control**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Messaging and social >
   Messaging**.
2. On the Messaging channels page, click **Manage settings**.
3. Expand the Conversation control section and select your control option.

   - **Release control:** Clears any existing switchboard integrations
     for the conversation and hands over control to its default state.
     This is recommended when using proactive messaging.
   - **Pass control**: Automatically calls the next configuration and
     hands over the conversation flow to the specified integration.
4. Click **Save settings**.

For more information on conversation control settings, see [Conversational control model](https://docs.smooch.io/guide/switchboard/#conversational-control-model) in our
Sunshine Conversations documentation.