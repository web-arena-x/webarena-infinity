# Understanding live conversation translation

Source: https://support.zendesk.com/hc/en-us/articles/4408832500506-Understanding-live-conversation-translation

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

You can give your agents the power to automatically translate incoming messages from live conversation channels in the Zendesk Agent Workspace, if they so choose. This allows agents to communicate with end users and other agents, even if they are using different languages. This article describes how live conversation translation works. To activate conversation translations, see [Activating AI translations for ticket conversations](https://support.zendesk.com/hc/en-us/articles/9837507006106).

For information about using live conversation translation after it is activated, see [Translating conversations in the Zendesk Agent Workspace](https://support.zendesk.com/hc/en-us/articles/6327770807450).

This article includes the following topics:

- [About live conversation translation](#topic_hdf_y3d_3nb)
- [How conversations are translated](#topic_psw_pdq_zgc)
- [The end-user experience](#topic_qgd_rdq_zgc)

## About live conversation translation

Live conversation translation gives agents the option to automatically translate incoming messages (coming from the end user) and outgoing messages (going to the end user) in the Zendesk Agent Workspace. It works in live conversations from the following channels:

- Live chat
- Social channels
- Sunshine Conversations channel
- Zendesk messaging

Additionally, the live conversation translation feature in Agent Workspace also supports the automatic translation of incoming comments sent via other channels, such as email, web form, or API. However, it doesn't support the translation of any outbound emails sent to end users.

Note: AI translation for outbound email, web form, and API messages is currently available in an Early Access Program (EAP). [Sign up for the EAP here](https://docs.google.com/forms/d/e/1FAIpQLSdQgUO6trKj7gzud3oR8KtxfZDTKDTTXdEnMR4CZKIhMWM1sA/viewform).

If the agent’s and end user’s languages differ, a translation banner is displayed informing the agent of the language difference, and they can choose to enable translation for that conversation.

Limitations to this feature include:

- There is a 5,000-character limit per message for translation. Any message over 5,000 characters will not be translated.
- [SunCo Shorthands](https://docs.smooch.io/guide/shorthand/) are not supported for translations.
- Translations for third-party widgets are not supported.
- Our translation service (Amazon translate) cannot accurately translate texts written in a phonetic manner. For example, translation will only work for Hindi text in Devanagari script but won't work when it is written in Roman script.

## How conversations are translated

A user’s language is determined based on recent messages they have sent, then [Amazon Translate](https://docs.aws.amazon.com/translate/latest/dg/how-it-works.html) is used to translate text.

The length and number of the messages can affect the language analysis. There's no guaranteed length at which the language will always be detected, but longer messages produce better results.

If the text scan detects that the agent’s and end user’s languages are different, the translation banner is displayed. If the text scan can't detect the language (for example, the message was too short to determine the language), the banner doesn’t appear.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aw_auto_translate_banner.png)

If you don't see the translation banner, click the ticket options menu, then click **Translate**.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ticket_translate_1.png)

Both the original and translated messages sent by the agent appear in the Event log. End-user messages appear only in the original language.

## The end-user experience

When an agent turns on automatic translation for a live conversation, the end user does not receive an activation notification—agent messages simply appear in their detected language. However, translated agent messages *are* identified in the conversation.

In a **live chat**, translated messages have a **Show original** link, which end users can click to display the untranslated message:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aw_auto_translate_enduser_chat.png)

In messaging and Social Messaging conversations, translated messages are identified by the word **Translated** in their detected language. Unlike live chat conversations, however, they cannot display the untranslated version of the message:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aw_auto_translate_enduser_social.png)