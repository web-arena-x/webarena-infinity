# Integration builder FAQs

Source: https://support.zendesk.com/hc/en-us/articles/8560379152282-Integration-builder-FAQs

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | AI agents - Advanced |

The [integration builder](https://support.zendesk.com/hc/en-us/articles/8357756844442)
is a powerful no-code tool that allows you to connect your AI agent to any API or data source without extended technical or programming skills. This article covers frequently asked questions (FAQs) about the integration builder.

This article contains the following topics:

- [Parameters and data FAQs](#h_01JFB58NCA8RFM3DHX4YSXAGWZ)
- [Environments FAQs](#h_01JFB5NWYZFCEJEGRNFJ6WQDSD)
- [Cards and carousels FAQs](#h_01JFB5Q0QNPCHSS0JJ4FSRG75H)
- [Authentication FAQs](#h_01JFB5QKYATTKTF0Y3AFMQPTB3)

Related articles:

- [Integration builder resources](https://support.zendesk.com/hc/en-us/articles/8498753675290)

## Parameters and data FAQs

### How is session data from the conversation collected?

Session data collection in AI agent conversations starts with the automatic capture of user metadata when the session begins and continues through the interaction with the AI agent, where inputs, responses, and entities can be captured.

When a chat session is initiated, especially if the user is logged in, certain metadata is automatically collected. This metadata typically includes user-specific details which may include user ID or account information, session ID, location, timestamps, and more. This data can then be saved as a [conversation action](https://support.zendesk.com/hc/en-us/articles/8357756651290).

During the conversation, you can choose to capture certain responses (either written as free text or submitted with buttons) from the user. You can do this as either:

- A parameter using the "Collect parameter" setting in a conditional block
- An [entity](https://support.zendesk.com/hc/en-us/articles/8357749740698)

These parameters can then be passed to the integration and can be used as [request parameters](https://support.zendesk.com/hc/en-us/articles/8357756844442#h_01HAY9KGH06WFPD1BMJAPA3D0Q)
in the URL endpoint or in the body of the request.

### What is a URL parameter and how do I use one?

A URL parameter is a dynamic parameter in the URL that changes based on the information passed to the integration in the request parameters that come from the conversation.

Here is an example of a user ID used as a parameter:

```
https://{{zendesk_subdomain}}.zendesk.com/api/v2/users/{{user_id}}
```

In the double curly brackets, the parameter *user\_id* is added to the URL.

### How can I access data from the conversation for use in the API?

To use data from the conversation, the data must be saved to the session as a parameter as described above, either collecting the parameter or saving metadata to a parameter in the session data. The data must be saved as a request parameter in the integration builder if it’s coming from the conversation or as session data/metadata to be sent to the API. You can then also dynamically send that parameter in the body of the request.

### How can I access the parameters or data from the API response for use in the conversation?

To use parameters or data from the API response, they must be saved as a session parameter in the [environment](https://support.zendesk.com/hc/en-us/articles/8357756844442#h_01HAY9KGH0CWG0E9T0BEAJ7772)
(in most cases, the success scenario). Once saved and once the API lands in a certain scenario, you can access and use the session parameter for use in an AI agent message or as a parameter for a [conditional block](https://support.zendesk.com/hc/en-us/articles/8357733406234):

- In an AI agent message, it’s accessed as *{{parameterName}}*.
- In a conditional block, it’s accessed with the parameter name.

### How do I send request parameters in the body?

To send a request parameter in the body, you must include it in double curly brackets like this:

```
{{exampleParameter}}
```

### Can I send an array in the request body?

Yes, you can select the data type as an array when defining your request parameters. When testing, make sure to [reformat the value](https://support.zendesk.com/hc/en-us/articles/8560203369242)
with the JSONata function *$eval($)*. The eval function parses and evaluates a string containing either a JSON expression or a JSONata expression as if it were JSON.

In this case, we’re taking a string included in an array and using *$eval()* to parse it as an array. The most common use case for this is when sending an array of orders.

### When testing, why am I not receiving any request parameters or incorrect parameters?

For testing purposes, you must use a test value that matches real data in your endpoint for your request parameter in the integration builder. However, in a live conversation, this parameter’s value comes from the conversation.
If you aren’t able to see the parameter and value in the session data when testing, should check to make sure that you’re capturing and saving it as the correct parameter in the dialogue.

Keep in mind that [sanitized session data](https://support.zendesk.com/hc/en-us/articles/8357749756442)
will not show up in the conversation logs. In this case, you might need to log those temporarily into an AI agent message to debug instead.

### Why am I seeing [Object, object]?

Seeing *[Object, object]* means that you're attempting to output an object, but the system doesn’t have a structured way to display it. To resolve this, you need to convert the object into a string format.

### Do you log successful calls?

No, for PII and GDPR reasons, we do not log successful data calls. We do log unsuccessful calls so that we can provide more information on what went wrong during troubleshooting, if necessary.

## Environments FAQs

### Why might I need different environments?

When testing your integration, you might not want to use real-life or live data. If you have access to a sandbox, staging, or development environment (we suggest finding out from your technical team or API documentation), then you’re able to set this up within the integration builder.

Environments share request parameters and outputs. However, they differ in endpoints and authentication details. In the dialogue builder, you can easily switch between environments on the API node. This means you only need to build one dialogue when testing, and then you can switch to a production environment when you’re ready to take the integration live.

## Cards and carousels FAQs

### Do I need to set a maximum number of cards?

For the Sunshine Conversations integration, there is a maximum of 10 cards.

We suggest limiting the number of cards in a carousel to 9 cards, or 8 cards with one fallback card. A fallback card gives the user a way out of the carousel (for example, if they don’t see their item).

### Do I need to display images on cards in a carousel?

Yes, image is a required data field. You can populate the image field with a generic image link if you don’t require dynamic images (for example, an image per product).

## Authentication FAQs

### What authentication methods can I use?

You can use the following authentication methods:

- API key
- Bearer token
- Expiration token
- Basic auth
- OAuth 2.0
- IP allowlists

To get started with authentication for the integration builder, see [Integration technical requirements](https://support.zendesk.com/hc/en-us/articles/8357749781274).

### Can I build an integration with an allowlisted endpoint?

Yes. To do so, you must add our IP addresses to your allowlist. For a list of IP addresses, see [Allow IPs to connect advanced AI agents to your CRM](https://support.zendesk.com/hc/en-us/articles/8357756859546).

### What is an auth-only integration and when do I need it?

To learn more about auth-only integrations, see [Using custom authorization with the integration builder](https://support.zendesk.com/hc/en-us/articles/8357749813658).

### Can I implement rate limiting and throttling?

We do not impose rate limiting and throttling directly. Rate limiting is typically enforced by the systems or APIs we integrate with, such as your backend system. These limits depend on the configuration of your backend.

### What happens if my API takes longer than 9 seconds to respond?

The AI agents - Advanced add-on enforces a 9-second timeout for API responses.
If your API doesn’t provide a response within this time, the request will time out and return the error *ECONNABORTED*. Additionally, longer response times can negatively impact the user experience, as users may find it frustrating to wait for information.

To address this, if you anticipate that certain API responses will take longer than 9 seconds, we recommend making the necessary API calls at the start of the conversation if possible (for example, upon the Chat started [event](https://support.zendesk.com/hc/en-us/articles/8357749555610))
and storing the relevant information in the session. This ensures that the data is ready when needed, avoiding delays during the conversation flow.