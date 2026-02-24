# Creating a Zendesk ticket from an advanced AI agent

Source: https://support.zendesk.com/hc/en-us/articles/8929793141146-Creating-a-Zendesk-ticket-from-an-advanced-AI-agent

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | AI agents - Advanced |

The integration builder can be used to create a Zendesk ticket from a conversation using an AI agent. This article will take you through the steps on how to do so.

For reference, you can find the relevant Zendesk developer documentation on this [here](https://developer.zendesk.com/api-reference/ticketing/tickets/tickets/#create-ticket).

This article contains the following topics:

- [Prerequisites](#h_01JMMFYEASBRWXXRAF28XNKQKD)
- [Create integration](#h_01JMMG427HNW5W4PRRK5XF8Z4R)
- [Environment and endpoint](#h_01JMMFPMYGCPMPY9W0T1D2YY83)
- [Auth](#h_01JMMFQ43657G51D38ZNH6M41F)
- [Request parameters](#h_01JMMFQBCBH3ES3XV31PB31320)
- [Body](#h_01JMMFQHBNWZ94J5M8R8XF4TEG)
- [Chat transcript formatting: Standard vs HTML body](#h_01JMMFQQN277KPJZMT0ETWJ2MK)
- [Standard fields vs Custom field values](#h_01JMMGVKJ5KYYBZKRXYF3ZWGXY)
- [Building in the dialogue builder](#h_01JMMFR1R5VAT44D7PFWQZX68X)

## Prerequisites

Required to get set up you will need:

- Your Zendesk subdomain
- Your authorization token (see the section below for more information)

## Create integration

1. Create a new Integration in API Integrations.
2. Give it a name such as Create Zendesk Ticket and a description.

## Environment and endpoint

To access the Zendesk Ticket API, you will need to make a POST request to the following endpoint: *http://[your-zendesk-subdomain].zendesk.com/api/v2/tickets*

With your Zendesk subdomain, you can construct the endpoint URL to your Zendesk instance. This URL is then used in the Environments section of the integration builder to make the POST request.

1. Navigate to the Environments section of the integration builder.
2. For Method type, select POST.
3. Add your constructed URL endpoint for the Ticket API.  
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_create_ticket_1.png)

## Auth

To access the Zendesk API, you will need to create a token in Admin Center.

1. In Admin center, go to Apps and integrations and select APIs > Zendesk API.  
   You will see the below screen where you can add a new token.  
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_create_ticket_2.png)
2. Click **Add API token**.
3. Give it a name such as **Create Ticket**.
4. Copy the token somewhere safe, as you will need this for setting up the integration in the integration builder.

Once you have these, you can add them to your integration in the integration builder.

1. In the **Environment** section, click **Authorization**.
2. In **Authorization** type, select **Basic Auth**.
3. Enter an admin email address with **/token** appended at the end.
4. Paste your created token as the password.  
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_create_ticket_3.png)
5. Make sure to include the authorization token in the request by manually constructing it in the headers.  
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_create_ticket_4.png)

## Request Parameters

This is where you will be passing data from the AI agent conversation into the integration to create the ticket.

For the live integration, you will need to set the parameters on your dialogue and then match these to your request parameters in the integration builder. For testing purposes, you can create the request parameters with test values as we are not using live data from a conversation.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_create_ticket_5.png)

Make sure that your request parameter names match those that you have set in your dialogue (via actions). See [Building in the dialogue builder](#h_01JMMFR1R5VAT44D7PFWQZX68X) for more information.

## Body

The body is where you are going to send all of the data from the conversation to create the ticket via the Ticket API. The structure of this body must match the schema for the Ticket API.

To see the schema and which fields can be created with your ticket, see the Zendesk developer documentation [here](https://developer.zendesk.com/api-reference/ticketing/tickets/tickets/#json-format).

Below is an example request body with the request parameters we created earlier.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_create_ticket_6.png)

Test the integration by clicking **Test Production**.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_create_ticket_7.png)

You should then be able to see your newly created ticket in your Zendesk dashboard.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_create_ticket_8.png)

## Chat transcript formatting: Standard vs HTML body

The Ticket API supports either *body* or *html\_body* for comments. When using *body*, multiple consecutive spaces are collapsed into a single space and multiple new line (“/n”) characters are collapsed into a single new line. Whereas, when using *html\_body*, you're able to use standard HTML syntax for your comment formatting.

For more information, see the Zendesk developer documentation [here](https://developer.zendesk.com/api-reference/ticketing/tickets/ticket_comments/#bodies).

To use either in your created ticket, you'll structure the one you want to use in “comment” in the request body.

Note: Use either option, not both as in the demonstration below.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_create_ticket_9.png)

If you're sending the chat transcript from the conversation, then it's recommended that you use the reformat values tool to make the transcript more readable. Rather than just being one big chunk of text, you can add line breaks for the beginning of each message.

If you're sending an HTML body, then you can use the Reformat values tool to add your HTML.

For instructions on how to use the Reformat values tool, see [Reformatting values in request parameters for advanced AI agents](https://support.zendesk.com/hc/en-us/articles/8560203369242).

In the screenshot below, we've reformatted the chat transcript to make clickable URLs and added line breaks with *<br>*.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_create_ticket_10.png)

## Standard fields vs Custom field values

In addition to the standard fields that can be created and sent in the body of the request, you can also create custom field values. For instructions on how to set up custom fields in the body, see the Zendesk developer documentation [here](https://developer.zendesk.com/documentation/ticketing/managing-tickets/creating-and-updating-tickets/#setting-custom-field-values).

## Building in the Dialogue Builder

1. Add the API Node and select the Create Zendesk Ticket integration that you created above.
2. Create an [action](https://support.zendesk.com/hc/en-us/articles/8357756651290) on the API node which sets the parameters from the conversation.  
   It will look something like this:  
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_create_ticket_11.png)
3. Add a message for the Success and Fallback scenarios.  
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_create_ticket_12.png)