# About rich-text formatting in messaging conversations

Source: https://support.zendesk.com/hc/en-us/articles/9017484189466-About-rich-text-formatting-in-messaging-conversations

---

Rich-text formatting adds structure to messages displayed to users in the messaging Web Widget, mobile SDKs, and Agent Workspace. Rich-text formatting is automatically applied to generated responses in messaging conversations, and can be used by admins when creating AI agent messages. Additionally, rich text messages can be sent by using ourSunshine Conversations API, or by third-party bots.

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

Rich-text formatting adds structure to messages displayed to users in the messaging Web Widget, mobile SDKs, and Agent Workspace. Rich-text formatting is automatically applied to generated responses in messaging conversations, and can be used by admins when creating AI agent messages. Additionally, rich text messages can be sent by using our [Sunshine Conversations API](https://developer.zendesk.com/documentation/conversations/messaging-platform/programmable-conversations/structured-messages/#rich-text), or by third-party bots.

This article explains how rich-text formatting can be used in messaging conversations, and provides examples of how rich-text formatting appears in the Web Widget, mobile SDKs, and Agent Workspace. For information on rich-text formatting in the ticket composer, see [Rich text formatting options reference](https://support.zendesk.com/hc/en-us/articles/4408844184730).

This article includes the following topics:

- [Requirements and limitations for rich-text formatting in messaging conversations](#topic_bv2_3ys_q2c)
- [Supported rich-text formatting](#topic_y5j_3ys_q2c)

## Requirements and limitations for rich-text formatting in messaging conversations

Your account must meet the following requirements to apply and display rich-text formatting in messaging conversations:

- Advanced AI agents: [Activate rich messaging](https://support.zendesk.com/hc/en-us/articles/10050437105946#topic_yf3_1gk_jhc) to use rich-text formatting in pre-defined messages in dialog builder.
- Mobile SDK: Messaging iOS or Android SDKs v2.30.0 or later. Older versions of the SDKs don't support rich-text messages.

Currently, this feature has the following limitations:

- End users can’t apply rich-text formatting to their messages.
- Rich-text messages are not supported in the Zendesk Unity SDK or some third-party social channels. Rich-text formatting is supported in social channels that provide rich-text formatting. For example, WhatsApp.

## Supported rich-text formatting

To send rich text messages with the [Sunshine Conversations API](https://docs.smooch.io/rest/#operation/postMessage), you can use either the HTML tags in the table below or markdown. See our [developer documentation](https://docs.smooch.io/guide/structured-messages/#rich-text) for information on sending messages with rich text using the API.

| **Format** | **Supported tags** | Example |
| --- | --- | --- |
| Bold | <strong>, <b> | |
| Italics | <em>, <i> | |
| Underline | <u>, <ins> | |
| Strikethrough | <s>, <del> | |
| Hyperlink | <a> | Web Widget: Mobile:    Agent workspace: |
| Numbered list | <ol>, <li> | |
| Bullet list | <ul>, <li> | |
| Nested lists | <ol>, <ul>, <li> | |
| Headings | <h1>, <h2>, <h3>, <h4>, <h5>, <h6> | |
| Code block | <code> | Web Widget: Mobile:    Agent workspace: |
| Quote | <q> | |
| Other common HTML tags | <p>, <br>, <span> | n/a |