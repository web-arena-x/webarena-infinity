# Using structured messages in Zendesk Chat

Source: https://support.zendesk.com/hc/en-us/articles/4408831142554-Using-structured-messages-in-Zendesk-Chat

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Enterprise or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Live chat and messaging Enterprise |

The structured messaging feature in Zendesk Chat allows you to provide elements that enhance and simplify a customer's chat experience. These elements include quick reply buttons, GIFs (as image in a template), and persistent panel templates, among others.

Currently, accounts use the [Chat Conversations API](https://developer.zendesk.com/rest_api/docs/chat/conversations-api) to add structured messages to their chats.

You do not need to manually enable the structured messaging feature. If your account meets the requirements described in this article, you can begin using structured messages in chats.
This article includes the following topics:

- [Requirements and restrictions](#topic_r4t_khs_jpb)
- [Structured message types](#topic_vsk_lmr_jgb)
- [Using structured messages in chats](#topic_b35_lmr_jgb)

## Requirements and restrictions

To use structured messaging, you must meet the following requirements:

- Your Zendesk Chat account is Enterprise or Premium (Legacy)
- You are using the [Web Widget (Classic)
 integrated Chat experience](https://support.zendesk.com/hc/en-us/articles/4408825767962#topic_ib1_t22_yfb).

 OR

 You are using the Chat Web SDK version 1.6.0 or above. See [Structured Message Payload](https://api.zopim.com/web-sdk/structured-message.html) for details.
- You have access to the Zendesk [Chat Conversations API](https://developer.zendesk.com/rest_api/docs/chat/conversations-api).

Additionally, each message type has certain restrictions, regarding the number and type of included items. See the [descriptions below](#topic_vsk_lmr_jgb) for specifics.

Note: Structured messages are not currently supported on the [Chat Android SDK](https://developer.zendesk.com/embeddables/docs/chat-sdk-v-2-for-android/introduction) and [Chat iOS SDK](https://developer.zendesk.com/embeddables/docs/chat-sdk-v-2-for-ios/introduction).

## Structured message types

The available structured message types are:

- [Quick replies](#topic_dbp_z1s_jgb)
- [Button templates](#topic_vgt_z1s_jgb)
- [Panel templates](#topic_e2x_z1s_jgb)
- [Panel template carousel](#topic_uj4_mnn_pgb)
- [List templates](#topic_cwv_mnn_pgb)

### Quick replies

Quick replies allow an agent to send a message with a number of option buttons for an end user to choose from. When the end user clicks a button, it sends a pre-defined reply to the agent.

You can include up to 11 buttons in a quick reply.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/chat_quick_replies.png)

### Button templates

A button template allows an agent to send a message along with a list of buttons. When clicked by the end user, these buttons can:

- Launch a quick reply, as described above, or
- Open a URL in a new tab

A button template must include at least one button, and can include a maximum of three buttons.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/chat_button_template.png)

### Panel templates

A panel template allows an agent to send a message with a panel and a list of buttons.

The panel can include an image, title, and subtitle. When clicked by the end user, the panel can:

- Open a URL in a new tab

When clicked by the end user, the buttons can:

- Launch a quick reply, as described above, or
- Open a URL in a new tab

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/chat_panel_template.png)

### Panel template carousel

A panel template carousel allows an agent to send an array of panel templates as a carousel.

A carousel must include at least two items, and can include a maximum of 10 items.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/chat_panel_template_carousel.png)

### List template

A list template allows an agent to send an array of items with an optional button.

A list template should include at least two items, and can inlcude a maximum of four items. The template should include no more than one button.

The item(s) can include an title, subtitle, and an optional image. When clicked by the end user, the item can:

- Open a URL in a new tab

When clicked by the end user, the button can:

- Launch a quick reply, as described above, or
- Open a URL in a new tab

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/chat_list_template.png)

## Using structured messages in chats

To use structured messages in chats, you must use the [Chat Conversations API](https://developer.zendesk.com/rest_api/docs/chat/conversations-api). To familiarize yourself with this, see [Getting Started with the Chat Conversations API](https://developer.zendesk.com/documentation/live-chat/getting-started/getting-started-with-the-chat-conversations-api).

We recommend you write an application that can act as an agent using the Conversations API. For a step-by-step walkthrough on writing this application, see the section [Getting Started](https://developer.zendesk.com/documentation/live-chat/getting-started/getting-started-with-the-chat-conversations-api). Once this is completed, instead of using the `sendMessage` mutation to deliver a text message to the end user, the application can use the following mutations to send a structured message:

Note: These mutations support a fallback parameter, which is used in situations where structured messaging is not supported (see [Requirements and restrictions](#topic_vdf_lmr_jgb), above).

Table 1.

| Structured message type | Conversations API mutation name |
| --- | --- |
| Quick replies | `sendQuickReplies` |
| Button templates | `sendButtonTemplate` |
| Panel templates | `sendPanelTemplate` |
| Panel template carousel | `sendPanelTemplateCarousel` |
| List template | `sendListTemplate` |

Refer to the Conversations [API schema documentation](https://zendesk.github.io/conversations-api/) for the full API details.