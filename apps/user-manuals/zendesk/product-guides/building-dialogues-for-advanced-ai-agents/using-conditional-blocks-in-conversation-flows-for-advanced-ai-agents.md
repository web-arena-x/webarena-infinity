# Using conditional blocks in conversation flows for advanced AI agents

Source: https://support.zendesk.com/hc/en-us/articles/8357733406234-Using-conditional-blocks-in-conversation-flows-for-advanced-AI-agents

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | AI agents - Advanced |

In the [dialogue builder](https://support.zendesk.com/hc/en-us/articles/8357749494810), conditional blocks activate dialogue branches based on information in the conversation. This article explains what conditional blocks are and how to set them up for an advanced AI agent.

The article contains the following sections:

- [Understanding conditional blocks](#topic_sds_xwp_xfc)
- [Adding a conditional block to a dialogue](#topic_nbw_nxp_xfc)

## Understanding conditional blocks

Conditional blocks let you customize a conversation flow based on certain conditions. You can create conditional blocks based on:

- [Parameters](https://support.zendesk.com/hc/en-us/articles/9522180655386), which let you shape conversations based on information from your CRM platform, session data, or backend integrations.
- [Segments](https://support.zendesk.com/hc/en-us/articles/9413046533530), which let you shape conversations based on different types of customers.

Each conditional block represents a conditional statement that requires:

- A condition (a parameter or segment)
- An operator (such as “is” or “Is ANY of”)
- A value or set of values (including a null value)

When the conversation reaches the conditional block within a dialogue, the system evaluates the conditional statement as true or false. Based on the outcome, the conversation continues down the appropriate branch in the dialogue, as configured by you.

For example, you could configure the following conditional block:

- Parameter: country
- Operator: is
- Values: Germany, Japan

In this example, a customer reaching out to your AI agent will receive a different message based on their location, which is determined by the country parameter. Referencing the image below, if the customer is in:

- Germany, the conversation progresses down the left branch.
- Japan, the conversation progresses down the middle branch.
- Any other country, the conversation progresses down the right branch (the fallback branch).

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_conditional_block_example.png)

It’s important to understand and account for all possible scenarios when creating a conditional block and its resulting conversational branches, especially if you’re using values returned from an API.

Conditions are checked from left to right. Ensure that broader conditions you configure are positioned to the right of other, narrower conditions. The fallback condition, the broadest condition, is always positioned furthest right and can’t be moved.

## Adding a conditional block to a dialogue

In the dialogue builder, you can add a conditional block to a dialogue. When you do, you can:

- [Configure a conditional block based on a parameter](#topic_u44_kdc_cgc)
- [Configure a conditional block based on a segment](#topic_e3n_ldc_cgc)

### Configure a conditional block based on a parameter

Configuring a conditional block based on a parameter lets you shape conversations based on information from your CRM platform, session data, or backend integrations.

**To configure a conditional block based on a parameter**

1. [Open the dialogue builder](https://support.zendesk.com/hc/en-us/articles/9066753203738) for the dialogue you want to add a conditional block to.
2. In the appropriate location in the dialogue, click the plus (+) icon and select **Conditional**.

   A set of blocks appear, including Conditional, Parameter, and Fallback.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_conditional_dialogue_parameter.png)
3. In the Conditional block, use the second drop-down field to select the [parameter](https://support.zendesk.com/hc/en-us/articles/9522180655386#topic_cth_4xp_xfc) you want to use.

   If the parameter you want isn’t there, you can [create an action](https://support.zendesk.com/hc/en-us/articles/8357756623770) to capture it.
4. In the Parameter block, select the [operator](https://support.zendesk.com/hc/en-us/articles/9522180655386#topic_jbc_qxp_xfc) and enter the value to check for.
5. Click the plus (+) icon below the Parameter block and configure the conversational flow that should follow if the condition evaluates as true.

   Tip: You can even add another conditional block for increasingly tailored conversational flows.
6. (Optional) Add another condition by clicking the plus (+) icon on the right.

   An additional Parameter block is added to the left of the Fallback block.

   Repeat steps 4 and 5.
7. Under the Fallback block, click the plus (+) icon and configure the conversational flow that should follow if none of the conditions are met.

### Configure a conditional block based on a segment

Configuring a conditional block based on a segment lets you shape conversations based on different types of customers.

**To configure a conditional block based on a parameter**

1. [Open the dialogue builder](https://support.zendesk.com/hc/en-us/articles/9066753203738) for the dialogue you want to add a conditional block to.
2. In the appropriate location in the dialogue, click the plus (+) icon and select **Conditional**.

   A set of blocks appear, including Conditional, Parameter, and Fallback.
3. In the Conditional block, use the first drop-down field to select Segment.

   The Parameter block changes to a Segment block.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_conditional_dialogue_segment.png)
4. In the Segment block, select the:
   - Operator (**Is ANY of**, **Is NOT ANY of**, **Is ALL of**)
   - Segments to check for
5. Click the plus (+) icon below the Segment block and configure the conversational flow that should follow if the condition evaluates as true.

   Tip: You can even add another conditional block for increasingly tailored conversational flows.
6. (Optional) Add another condition by clicking the plus (+) icon on the right.

   An additional Segment block is added to the left of the Fallback block.

   Repeat steps 4 and 5.
7. Under the Fallback block, click the plus (+) icon and configure the conversational flow that should follow if none of the conditions are met.