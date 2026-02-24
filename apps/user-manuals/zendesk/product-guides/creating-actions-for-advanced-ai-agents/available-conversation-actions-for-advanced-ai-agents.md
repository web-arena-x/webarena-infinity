# Available conversation actions for advanced AI agents

Source: https://support.zendesk.com/hc/en-us/articles/8357756631706-Available-conversation-actions-for-advanced-AI-agents

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | AI agents - Advanced |

Conversation actions allow you to create or modify [labels](https://support.zendesk.com/hc/en-us/articles/8357749583130) and [parameters](https://support.zendesk.com/hc/en-us/articles/9522180655386), forming the basis for your business logic in conversation design. These actions are versatile and can be used for various purposes, including:

- **Labeling conversations**: Tag conversations, making them easier to track and analyze within [conversation logs](https://support.zendesk.com/hc/en-us/articles/8357749580186) and [analytics](https://support.zendesk.com/hc/en-us/articles/9510024609178).
- **Creating parameters**: Save parameters to use in conditional logic within the [dialogue builder](https://support.zendesk.com/hc/en-us/articles/8357749494810), enabling more dynamic and responsive conversation flows.
- **Updating parameters**: Update existing parameters, such as changing the language of the conversation based on user preferences or other criteria.

This article contains the following topics:

- [Available conversation actions](#topic_hlt_dpl_rgc)
- [Creating a conversation action](#topic_gq4_2pl_rgc)

Related articles:

- [About actions for advanced AI agents](https://support.zendesk.com/hc/en-us/articles/8357756651290)
- [Creating and adding actions for advanced AI agents](https://support.zendesk.com/hc/en-us/articles/8357756623770)
- [Reviewing and managing actions for advanced AI agents](https://support.zendesk.com/hc/en-us/articles/8566644914202)

## Available conversation actions

The table below lists and describes the available conversation actions.

| | | |
| --- | --- | --- |
| **Name** | **Description** | **Action-specific fields** |
| Set | Sets the value of one or multiple parameters. You can overwrite existing parameters or define new ones. Accepts both strings and numbers. If you use only numbers, you can apply numeric operators on them in conditional blocks, such as “Greater than.” | *Click* ***Select Another Field****.* **Field to update:** Enter the name of the field the action should update. **Value:** Enter the string or number you want to set for each specified field. |
| Unset | Removes the value of a parameter. You can unset the value of only one parameter per action. | **Field to update:** Enter the name of the field the action should update. |
| Increment | Increases the value of a numeric parameter by the specified amount. Use only numbers in the Value field, and ensure the parameters you use also contain only numbers to avoid overwriting. For example, to track the number of use cases triggered in a conversation, you could [create a parameter](https://support.zendesk.com/hc/en-us/articles/8357733406234#h_01F7WZQVWAZJQ6GXYF39JM7Y3M) called *usecasesTriggered* and increment its value by one for each use case–level action. | **Field to update:** Enter the name of the field the action should update. **Value:** Enter the number by which the specified field should be incremented. |
| Push | Allows you to store multiple values in a single parameter as an array. For example, you could store customer information for the session, like “B2C, EMEA.” | **Field to update:** Enter the name of the field the action should update. **Data type:** Select **string**, **number**, or **boolean**. **Value:** Enter the values you want to store. |
| Add label | Adds a label to the conversation, which can be used for filtering in conversation logs and for enriching analytics. You can add multiple labels to a single conversation and filter on them individually. | **Value:** Enter the label you want to add. |

## Creating a conversation action

Conversation actions can be created at the AI agent, use case, or block level. For details, see [Creating and adding actions for advanced AI agents](https://support.zendesk.com/hc/en-us/articles/8357756623770).