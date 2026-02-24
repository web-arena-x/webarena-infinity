# Using and sanitizing forms in conversation flows for advanced AI agents with Sunshine Conversations

Source: https://support.zendesk.com/hc/en-us/articles/8357720543514-Using-and-sanitizing-forms-in-conversation-flows-for-advanced-AI-agents-with-Sunshine-Conversations

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | AI agents - Advanced |

Form messages are a type of structured message from Sunshine Conversations that allow you to capture user data in an ongoing conversation by displaying a form that can contain text inputs as well as select dropdowns.

### Before you start

Before integrating a form into AI agents - Advanced, though, you will need to create your form on Sunshine Conversations side. You can find information [here](https://docs.smooch.io/guide/template-messages/#form-message) on how to do this. Contact your CSM if you have any questions about this.

You will need the exact name of the form later on.

In this article we will cover:

- [Using Forms with AI agents - Advanced](#h_01G7EGYGY2R55EQAG7SG0MFVM9)
- [Sanitize Customer Responses](#h_01G7EGYCDE84M7G0SVB7DE4BAR)
  - [How to Sanitize Form Data](#h_01G7EGY0WX66AKMWR7HD7TRYCY)

## Using Forms with AI agent - Advanced

Forms are a great way to collect customer data without having the AI agent ask multiple questions. Typical use cases include security, identification questions, or data change requests.

Once your form is created, go to your respective Dialogue that you would like to add the form and follow the below steps. 

### Steps:

1. Add an AI agent message with the shorthand code to capture the form and insert it. In the picture below we are adding our lead\_capture form. However, you will add the name of your form in between template: and ))% in the snippet below.  
     
   `%((template: nameOfTemplate))%`
2. Add a *customer message (Free Text Written)* block right after the AI agent message. This captures the user's responses.
3. Add another AI agent message block following the customer message with some kind of acknowledgment of the customers' completion of the form, such as a thank you.
4. The user's answers are locked in the metadata. If you want to use them later in the chat, you will want to retrieve them - this is completely optional. We do this with Actions.

   Add the `Get Conversation` action, select `<Metadata>`, and complete the fields to save the answers from customers to the session. In the Metadata Key, use the form fields name, as configured in your Sunshine Conversations template. Learn more about [Sunshine Conversation Actions.](https://support.zendesk.com/hc/en-us/articles/8357734565402)

   ![Screenshot_2022-07-08_at_10.58.19.png](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_6506766887314.png)

## Sanitize Customer Responses

Sanitizing responses is something you will want to do if you are asking for any PII data from your customers. This is something you will be familiar with from entities, for example, we by default sanitize email addresses and IBAN numbers. To understand more about Sanitizing check out the below articles.

[AI agents - Advanced data processing explained](https://support.zendesk.com/hc/en-us/articles/8357751648666)

[Recipe: Sanitize Personal Identifiable Information (PII) data with entities](https://support.zendesk.com/hc/en-us/articles/8357749756442)

### How to sanitize form data

Depending on the use case you have for the forms, you may want to sanitize the information. This is easy to do. 

1. Click the blue bar where it says "if..." to open the details panel.
2. Click the "Sanitize the user's answer" box to have the details hidden within AI agents - Advanced.

![Screenshot_2022-07-08_at_10.58.38.png](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_6506766879634.png)

The result of this means that when you review the conversation within AI agents - Advanced, it will look as shown below.

![Sanitized_Responses.png](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_6506857329810.png)