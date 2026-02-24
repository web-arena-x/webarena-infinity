# Differences in AI agent functionality on social messaging channels

Source: https://support.zendesk.com/hc/en-us/articles/4408822333722-Differences-in-AI-agent-functionality-on-social-messaging-channels

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

This article applies to [AI agents - Essential](https://support.zendesk.com/hc/en-us/articles/6970583409690) and [legacy AI agent functionality](../ai-agent-basics/about-ai-agents.md#topic_zps_zmk_f2c:~:text=Legacy%20AI%20agent%20functionality).

You can [create an AI agent](https://support.zendesk.com/hc/en-us/articles/4408824263578) and [add it to your messaging channels](https://support.zendesk.com/hc/en-us/articles/9543022336794), including web, mobile,
and social channels. However, AI agents on social messaging channels have the following
differences in functionality as compared to web and mobile channels:

- **Greetings.** On social channels, the AI agent is not able to send the greeting
  message to begin a conversation. The user must speak first, and then the AI agent
  will follow normal behavior when receiving a free-text message and attempt to find a
  conversational shortcut.
- **Automatic translations**. Social messaging channels do not pass the locale, so
  [automatic translation](https://support.zendesk.com/hc/en-us/articles/4408842754202#topic_ddp_kcj_bpb) for AI agent
  messages, text, links, variables, and so on, is not available for a social messaging
  AI agent.
- **Language support.** Social messaging AI agents automatically detect a user's
  language based on the following information provided by the Sunshine Conversations
  platform (determined in order):
  - Locale or language information sent by the source channel.
  - The content of the user’s messages.
  - The Zendesk account’s locale.

    If none of these can be determined, the AI
    agent sends messages in English.
- **Quick reply options experience**. (Applies to [legacy AI agent functionality](../ai-agent-basics/about-ai-agents.md#topic_zps_zmk_f2c:~:text=Legacy%20AI%20agent%20functionality).) For
  channels like WeChat, Instagram, and X (formerly known as Twitter), quick reply
  options aren't supported, and will degrade to a text-based experience to list the
  options for the user. The AI agent will say “You can say” followed by the options
  configured in bot builder. The AI agent can't be configured per channel at this
  stage and will be enabled across all Zendesk integrated social channels, including
  Sunshine Conversation integrations.

  Note: Quick reply options
  are currently available on WhatsApp using [Sunshine Conversations integrations](https://docs.smooch.io/guide/structured-messages/#reply-buttons).
- **Data capture**. (Applies to [legacy AI agent functionality](../ai-agent-basics/about-ai-agents.md#topic_zps_zmk_f2c:~:text=Legacy%20AI%20agent%20functionality).) Data
  capture is not available on social messaging channels. For instance, if an answer
  includes the **Ask for details** step requesting information from the customer,
  the AI agent will skip that answer and move to the next one in the flow.
- **Intent characters limitation**. (Applies to [legacy AI agent functionality](../ai-agent-basics/about-ai-agents.md#topic_zps_zmk_f2c:~:text=Legacy%20AI%20agent%20functionality).) The AI
  agent intent title and the presented options for social media have to fit the limit
  of 20 characters.
- **Authentication and messaging metadata variables**. (Applies to [legacy AI agent functionality](../ai-agent-basics/about-ai-agents.md#topic_zps_zmk_f2c:~:text=Legacy%20AI%20agent%20functionality).) [Messaging authentication](https://support.zendesk.com/hc/en-us/articles/4411666638746) and [messaging metadata variables](https://support.zendesk.com/hc/en-us/articles/5314129059482) are only available for the
  Web Widget and mobile SDK channels.

For a summary of all social channel capabilities, see [Sunshine
Conversations: Channel capabilities](https://docs.smooch.io/guide/channel-capabilities/).