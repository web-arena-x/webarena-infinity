# Using labels to tag conversation content for advanced AI agents

Source: https://support.zendesk.com/hc/en-us/articles/8357749583130-Using-labels-to-tag-conversation-content-for-advanced-AI-agents

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | AI agents - Advanced |

Labels are a smart way to manage chats/conversations in Conversation Logs as well as your CRM platform.

This article covers:

- [What is a Label?](#h_01FB1HX1TGVMBZN54TV7ZCC3T9)
- [Why add a Label?](#h_01FB1HXANMJW3FNBN4WP444B5E)
- [How to add a Label](#h_01FB1HXFQ4E0X5DC50M0S1WWN7)

## What is a Label?

Labels are keywords that can be added to a chat’s history. They help provide a snapshot of the topics covered in the conversation or certain actions that have taken place within the chat.

Labels set within our Dashboard in dialogue flows can be added to internal Conversation Logs or externally to your CRM platform. This is done through Actions, if you'd like to learn more about actions, check out [Actions and Events Explained.](https://support.zendesk.com/hc/en-us/articles/8357756651290)

## Why add a Label?

Labels, whether internal or external, have a number of uses.

### Session (Internal) labels

Within our dashboard, labels can be used in two ways.

1. **To monitor the quality of a reply.** A label can be added at the intent-level or at a specific point within a dialogue.
2. **To perform** [Content Coverage Analysis](https://support.zendesk.com/hc/en-us/articles/8357758759322). Conversations are tagged with the labels “Existing” or “Non-existing” depending on whether the first meaningful message is covered by an existing intent or not.

Conversation Logs can then be filtered by labels to analyze how a dialogue or a particular path within a dialogue is performing, or to identify potential new intents.

### Platform (External) Labels

Like in our Dashboard, adding a label to your CRM platform allows you to filter and analyze conversations within your CRM.

Labels can also help speed up **Agent Handling Time (AHT)**. When escalation occurs, a label can provide the agent with a snapshot of which intent has been triggered or which path the customer has taken.

## How to add a Label

Labels, whether internal or external, can be added either at the AI agent or content-level.

### AI agent-level

These labels, found under **Settings > Actions**, are added when an action such as `Chat Started` or `Chat Escalated to Human` is triggered.

Example: Chat Started > Zendesk Chat > Add Tag > "bot\_handled"

### Content-level

Content labels can be added manually or automatically to conversations.

Manual labels can only be added to internal Conversation Logs by going to **Conversation Logs >** click the **🏷️ icon >** type the name of the label in the **Select or create label** field.

Automatic labels can be added to an intent or at any point within a dialogue flow.

1. Add to an intent: **click into Intent Detail > Actions > Add Action**
2. Add to a dialogue: **click block > click side-drawer > Add/Edit Action**

You can find an overview of all content-level labels under **Settings > Actions > Content Actions**.

Example: Conversation Documentation (Session) > Add Label > update\_email

If you wish to add the same label both internally and externally, you will need to create separate actions for each.

![mceclip0.png](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_mceclip0_vNy6U.png)