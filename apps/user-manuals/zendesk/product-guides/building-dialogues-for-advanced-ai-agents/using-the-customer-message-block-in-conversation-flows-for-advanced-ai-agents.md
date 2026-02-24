# Using the customer message block in conversation flows for advanced AI agents

Source: https://support.zendesk.com/hc/en-us/articles/9060613203610-Using-the-customer-message-block-in-conversation-flows-for-advanced-AI-agents

---

In thedialogue builder, a customer message block lets you define scenarios for how a user might respond to an advanced AI agent and how the dialogue will progress accordingly.

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | AI agents - Advanced |

In the [dialogue builder](https://support.zendesk.com/hc/en-us/articles/8357749494810), a customer message block lets you
define scenarios for how a user might respond to an advanced AI agent and how the dialogue
will progress accordingly.

The article contains the following sections:

- [About the customer message block](#topic_zmv_bjx_xfc)
- [Examples of customer message block
  scenarios](#topic_u5t_qmx_xfc)
- [Prioritizing customer message
  scenarios](#topic_bjz_wnx_xfc)

## About the customer message block

Use the customer message block to design interactions between the customer and the AI
agent. Because humans don’t all respond in the same way, it’s good to make these
interactions as flexible and comprehensive as possible.

When you add a customer message block in a dialogue, you can configure it to respond to one
or more of the following scenarios:

- **Button clicked**: (Messaging AI agents only) The customer clicks a button with
  specified text.
- **Link clicked**: (Messaging AI agents only) The customer clicks a specified link.
- **Intent predicted**: The customer responds with something that matches a specific
  use case or intent.
- **Entity recognized**: The customer responds with a defined piece of information
  known as an [entity](https://support.zendesk.com/hc/en-us/articles/8357749740698) (such as email or order number).
- **Free text written**: The customer gives a response that isn't recognized as any
  of the other options listed above.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_customer_message_block_email.png)

There are two limitations to using customer message blocks:

- A customer message block can’t be linked to another customer message block.
- For advanced messaging AI agents, you can’t have more than 10 buttons within a single
  customer message.

## Examples of customer message block scenarios

Below are two examples of customer message blocks to determine the next step in the
interaction based on the customer’s response:

- [Yes/no scenarios](#topic_a4j_gnx_xfc)
- [Multiple-answer scenarios](#topic_ipj_snx_xfc)

### Yes/no scenarios

In these scenarios, the AI agent has asked, "Have you received a confirmation email?" and
provided two buttons marked yes and no. A dialogue branch could be built for each scenario
by clicking the plus (+) icon below that block.

For example, the “yes” scenario is triggered when the customer clicks the “yes” button.
But there is an additional condition added:

- Button clicked: Yes
- Intent predicted: Affirmation

The scenario is triggered if either condition is met. You can add additional
conditions to a scenario in the Details pane.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_customer_message_block_yes_no_conditions.png)

### Multiple-answer scenarios

In these scenarios, the AI agent has asked, "What’s your payment method?" and provided
three buttons for credit/debit card, PayPal, and bank transfer. There is also a scenario
if the customer responds in another way (free text written). A dialogue branch could be
built for each scenario by clicking the plus (+) icon below that block.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_customer_message_block_multiple_answer.png)

## Prioritizing customer message scenarios

If you add more than one scenario for a customer message block, the order of the scenarios
matters. When the conversation reaches a customer message block, the AI agent checks the
scenarios from left to right. The first scenario that meets at least one condition will
trigger the next block in the conversation.

You can sort the priority of customer message scenarios in the Details pane.

**To sort the customer message scenarios**

1. In the [dialogue builder](https://support.zendesk.com/hc/en-us/articles/8357749494810), click a customer message block
   to open the Details pane.
2. In the Details pane, click the row for the item scenario you want to move, then drag
   and drop it into another position.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_customer_message_block_scenario_sort.png)