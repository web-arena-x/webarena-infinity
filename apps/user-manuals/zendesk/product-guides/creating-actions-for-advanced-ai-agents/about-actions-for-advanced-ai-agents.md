# About actions for advanced AI agents

Source: https://support.zendesk.com/hc/en-us/articles/8357756651290-About-actions-for-advanced-AI-agents

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | AI agents - Advanced |

Actions let your AI agents perform certain tasks during conversations with customers.
Actions can be used to:

- **Enrich the conversation experience for the customer** by leveraging [parameters](https://support.zendesk.com/hc/en-us/articles/9522180655386) to create more dynamic and responsive conversation flows.
- **Retrieve or send conversation details to your CRM platform** so you can use important customer information during conversations or store for later.
- **Improve your understanding of your customer conversations overall** by applying situation-specific [labels](https://support.zendesk.com/hc/en-us/articles/8357749583130) to conversations for later analysis.

Actions can be applied at different points in the conversation journey, giving you flexibility to manage conversations, personalize responses, and interact efficiently with your CRM system.

This article contains the following topics:

- [Types of actions](#topic_zjd_cnl_rgc)
- [Where actions can be applied](#topic_adr_cnl_rgc)

Related articles:

- [Creating and adding actions for advanced AI agents](https://support.zendesk.com/hc/en-us/articles/8357756623770)
- [Reviewing and managing actions for advanced AI agents](https://support.zendesk.com/hc/en-us/articles/8566644914202)
- [About events for advanced AI agents](https://support.zendesk.com/hc/en-us/articles/8357749555610)

## Types of actions

There are two types of actions:

- [Conversation actions](#topic_pnp_3nl_rgc)
- [CRM actions](#topic_kyv_jnl_rgc)

### Conversation actions

Conversation actions allow AI agents to perform tasks during conversations with customers. These actions are versatile and can be used for various purposes, including:

- **Creating parameters**: Save parameters to use in conditional logic within the dialogue builder, enabling more dynamic and responsive conversation flows.
- **Modifying parameters**: Update existing parameters, such as changing the language of the conversation based on user preferences or other criteria.
- **Labeling conversations**: Tag conversations, making them easier to track and analyze within conversation logs and analytics.

For a list of available conversation actions, see [Available conversation actions for advanced AI agents](https://support.zendesk.com/hc/en-us/articles/8357756631706).

### CRM actions

CRM actions enable communication between AI agents and your CRM platform. These actions are platform-specific, meaning different actions are available for each CRM platform.

For a list of available conversation actions for each CRM platform, see the articles below:

- [Available CRM actions for advanced AI agents and Zendesk Support](https://support.zendesk.com/hc/en-us/articles/8357750876826)
- [Available CRM actions for advanced AI agents and Zendesk Chat](https://support.zendesk.com/hc/en-us/articles/8357750804250)
- [Available CRM actions for advanced AI agents and Sunshine Conversations](https://support.zendesk.com/hc/en-us/articles/8357734565402)

## Where actions can be applied

Actions, whether they’re conversation actions or CRM actions, can be applied at three different levels:

- [AI agent–level actions](#topic_nnm_znl_rgc)
- [Use case–level actions](#topic_lwg_14l_rgc)
- [Block-level actions](#topic_msf_b4l_rgc)

### AI agent–level actions

AI agent–level actions are executed in every conversation your AI agent engages in. They require an [event](https://support.zendesk.com/hc/en-us/articles/8357749555610) and an associated action. For example, you could create an action associated with the “Conversation started” event to automatically pull in customer information from your CRM when a conversation begins.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ultimate_bot-level_action_example.png)

To create an AI agent–level action, see [Adding an action at the AI agent level](https://support.zendesk.com/hc/en-us/articles/8357756623770#topic_opk_kyl_rgc).

### Use case–level actions

Use case–level actions are executed when a specific use case is triggered during a conversation. You select the action you want to execute when the use case is triggered. Use case–level actions are particularly useful if you want to apply actions to all replies within a use case.

For example, you can apply conversation tags or internal notes based on the use case.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ultimate_intent-level_action_example.png)

To create a use case–level action, see [Adding an action at the use case level](https://support.zendesk.com/hc/en-us/articles/8357756623770#topic_zbz_kyl_rgc).

### Block-level actions

Block-level actions are executed when a particular block within a conversation flow is reached. These actions are useful for more granular control within your dialogues.

For example, you could add labels to conversations, check for specific parameters, or store detailed information relevant to the ongoing conversation.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ultimate_block-level_action_example.png)

To add a block-level action, see [Adding an action at the block level](https://support.zendesk.com/hc/en-us/articles/8357756623770#topic_b4n_lyl_rgc).