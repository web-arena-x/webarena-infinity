# Examples of generative procedures for AI agents with agentic AI

Source: https://support.zendesk.com/hc/en-us/articles/9424547984026-Examples-of-generative-procedures-for-AI-agents-with-agentic-AI

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | AI agents - Advanced |

Generative procedures are AI-generated procedures that help power the decision-making capabilities of [AI agents with agentic AI](https://support.zendesk.com/hc/en-us/articles/8966284087066). Instead of building scripted conversation flows in the dialogue builder, you can simply enter your business policies and let the AI agent generate a procedure to map out the best path to resolution.

This article provides examples of generative procedures for different scenarios to help you get an idea of how to construct your own procedures.

This article contains the following topics:

- [Example procedure: Order status](#topic_gdt_mcf_wfc)
- [Example procedure: Damaged item](#topic_lc2_ncf_wfc)

Related articles:

- [Best practices for creating and using generative procedures for AI agents with agentic AI](https://support.zendesk.com/hc/en-us/articles/9424547622298)
- [Creating generative procedures for AI agents with agentic AI](https://support.zendesk.com/hc/en-us/articles/8979864563610)

## Example procedure: Order status

**Step 1: Acknowledge customer intent and inform general order delivery times**

- Acknowledge you have understood the customer’s intent to receive the status of their order.
- Let the customer know [company name] orders are processed, picked, and delivered to customers in 3 days since the order is received.

**Step 2: Collect order details**

- IF orderNumber already exists, skip this step and continue to ask for customer email.
- IF orderNumber DOES NOT exist, ask the customer to provide it. The correct format for order numbers is 5 digits.
- IF the order number is provided in an incorrect format, ask the customer to try providing their order number in the correct format (5 digits). IF a customer provides their order number in an incorrect format twice, ALWAYS escalate to a human agent.
- When orderNumber is received in the correct format, save it to the session as /orderNumber and use action /updateOrderNumber to Zendesk ticket.
- Then, ask the customer to provide their email address. Validate email is provided in a correct format.
- IF the email address is provided in an incorrect format, ask the customer to try providing their email address once more. In case the format is provided incorrectly twice, ALWAYS escalate to human agent.
- Once you have received email correctly, save it to the session as /email and use action /updateUserEmail to update user email to Zendesk ticket.

**Step 3: Check order status**

- Trigger API /checkOrderStatus to obtain customer order status.
- Personalize the response using orderStatus, estDelDate, and courier information obtained through the API. If available, provide trackingURL. Display the details using bullet points and one item per line:

 Order Status:
 {{orderStatus}}

 Estimated delivery date: {{estDelDate}}

 Courier:
 {{courier}}

 Tracking link: {{trackingUrl}}
- IF orderStatus is ‘cancelledByMerchant’, inform the customer their order has been cancelled by the merchant due to insufficient stock, and a refund will be issued on their card.

## Example procedure: Damaged item

**Step 1: Confirm the issue and express empathy**

- Express understanding and apologize for the inconvenience caused by the damaged item.
- Clearly acknowledge that the customer has reported a damaged item.

**Step 2: Collect essential details**

- Request the customer’s order number. Remind the customer of the correct format (5 digits).
- If the customer provides an incorrect order number (e.g., not 5 digits), ask them to try again. If the customer provides the order number incorrectly twice, escalate them to customer service.
- Ask for the name or description of the damaged product.
- Request a description of the damage.
- Politely ask if the customer can provide a photo of the damaged item.
- Save the order number to session as orderNumber, and save the name of the damaged product to session as damagedProduct.

**Step 3: Provide next steps**

- Inform the customer that you will escalate their request to a support team who will get in touch with them in 3-5 business days.
- Trigger /API-Create-ZD-Ticket to submit a ticket.

**Step 4: Close the interaction politely**

- Thank the customer for their patience and understanding.
- Reassure the customer that the issue will be resolved.