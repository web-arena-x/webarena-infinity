# Viewing and editing system replies for advanced AI agents

Source: https://support.zendesk.com/hc/en-us/articles/8357749481882-Viewing-and-editing-system-replies-for-advanced-AI-agents

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | AI agents - Advanced |

In an advanced AI agent, system replies are designed to deliver specific types of messages at different points in a conversation with a customer. For example, there’s a system reply for the AI agent’s first message to the customer, a system reply for collecting feedback at the end of the conversation, and more.

This article contains the following topics:

- [About system replies](#topic_edj_gnp_xfc)
- [Viewing all system replies](#topic_fjr_d4p_xfc)
- [Editing a system reply](#topic_jhb_k4p_xfc)

Related article:

- [Creating and managing replies for advanced AI agents](https://support.zendesk.com/hc/en-us/articles/9624068102682)

## About system replies

System replies are automatically created for any advanced AI agent you create. Like [other replies you create](https://support.zendesk.com/hc/en-us/articles/9624068102682), each system reply is associated with a:

- Use case that detects what a customer is asking about.
- Dialogue that determines the conversation flow between the AI agent and the customer.

The table below describes the available system replies.

| System reply | Description | Contains a preconfigured dialogue? |
| --- | --- | --- |
| Collect BSAT reply | What the AI agent should say at the end of a conversation to collect feedback from a customer about their experience. See [Collecting AI agent satisfaction (BSAT) ratings for advanced AI agents](https://support.zendesk.com/hc/en-us/articles/8357749459482). | Yes |
| Default reply | What the AI agent should say when no relevant use case is detected and a generative reply can't be produced. | No |
| Escalation reply | What the AI agent should say when escalating a conversation to a human agent. Available only for [AI agents with agentic AI](https://support.zendesk.com/hc/en-us/articles/8966284087066). | No |
| Failed escalation reply | What the AI agent should say when the conversation can't be successfully escalated, such as when no human agents are available. Not available for email AI agents. | No |
| Technical error reply | What the AI agent should say when a technical issue occurs. This might be the result of an error from the advanced AI agent itself or an integration, such as an error when connecting to an external API. | No |
| Generative replies reply / uGPT reply | When no relevant use case is detected, the AI agent replies with an AI-generated message. | Yes |
| No message | What the AI agent should say when the customer's message is empty or doesn't provide any information. | No |
| Unsupported language reply | What the AI agent should say when the customer’s language isn't recognized. See [Configuring language detection for advanced AI agents](https://support.zendesk.com/hc/en-us/articles/8357756692890). | No |
| Welcome reply | What the AI agent should say to greet the customer at the beginning of the conversation. See [Adding and removing the welcome reply for advanced AI agents](https://support.zendesk.com/hc/en-us/articles/8357756557594). | No |

## Viewing all system replies

You can view a list of all system replies.

**To view all system replies**

1. In AI agents - Advanced, [select the advanced AI agent](https://support.zendesk.com/hc/en-us/articles/8357756913178#topic_t25_qvj_tdc) you want to work with.
2. Click **Content** in the sidebar, then select **Use cases**.
3. Click the **Categories** filter, select **System replies**, and click **Apply**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_system_reply_filtering.png)

   The list is filtered to show only system replies.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_system_replies.png)

## Editing a system reply

Even though the system replies are created for you, you still need to review and edit their associated dialogues to ensure these default messages say what you want them to say.

**To edit a system reply**

1. [In the list of system replies](#topic_fjr_d4p_xfc), click the system reply you want to edit.
2. Select the **Replies** tab.
3. Select the reply for the language you want to edit.
4. Click **Edit dialogue**.

   The dialogue builder opens.
5. Update the system reply's dialogue as needed.

   For help, see [Using the dialogue builder to create conversation flows for advanced AI agents](https://support.zendesk.com/hc/en-us/articles/8357749494810).