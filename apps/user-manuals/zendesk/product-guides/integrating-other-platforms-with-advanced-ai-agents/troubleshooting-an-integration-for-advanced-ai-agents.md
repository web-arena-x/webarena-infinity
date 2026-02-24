# Troubleshooting an integration for advanced AI agents

Source: https://support.zendesk.com/hc/en-us/articles/8919342194074-Troubleshooting-an-integration-for-advanced-AI-agents

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | AI agents - Advanced |

You might need to troubleshoot an integration between the AI agents - Advanced add-on and another system if it isn’t behaving the way you expect. This article outlines a number of troubleshooting steps you can perform to attempt to identify an integration issue.

This article contains the following topics:

- [Test the integration in the integration builder](#h_01JMFETPT77NP59HSPQF20496M)
- [Check that the request parameters match](#h_01JMFEVSVZ59F4S0YKK9XWEGPD)
- [Check the conversation logs for session parameters](#h_01JMFEVBSY6VJNTAKZDDP2Q3A9)
- [Output raw values in the failure scenario](#h_01JMFEY2DQV73K7AHTG4T4K5SG)
- [Check the HTTP status code](#h_01JMFEWMJNHJGY2XTJR0W0TG53)
- [Investigate any technical errors in the dialogue](#h_01JMFEX39SKR70ES514JQSNDT8)

Related articles:

- [Integration builder resources](https://support.zendesk.com/hc/en-us/articles/8498753675290)

## Test the integration in the integration builder

As your first step in troubleshooting an integration, [test it in the integration builder](https://support.zendesk.com/hc/en-us/articles/8357756844442#h_01HAY9KGH0W4XZ3BSZ8XPT9R51). Make sure that you’re getting a response and that you see the right data in the session parameters.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_troubleshooting_integration_1.png)

## Check that the request parameters match

The [request parameters](https://support.zendesk.com/hc/en-us/articles/8357756844442#h_01HAY9KGH06WFPD1BMJAPA3D0Q) you’re using in the integration builder—whether in the URL query, body, or header—must exactly match those captured in the dialogue.

Ensure the following:

- There are no typos.
- If you updated the spelling or name of a parameter at any stage in the dialogue, you also updated it in the integration.
- The case matches exactly. Parameters are case-sensitive.

Tip: We recommend adopting a consistent naming convention for all your request or session parameters, such as lowerCamelCase or snake\_case.

## Check the conversation logs for session parameters

Check the [conversation logs](https://support.zendesk.com/hc/en-us/articles/8357749580186) for more information, such as session data. You can search for conversations using the API by filtering for tags. If the conversation uses the API then you will be able to search for it.

When you are in conversation logs, at the top left, click Add filter.

On the menu on the left, navigate to Labels.

Here you can filter for the integration by name and by the scenario such as whether it was success, failure, or if there was an API error.

For integrations built in the integration builder, they will be prefixed by API, followed by the name of the integration and then end with the name of the scenario.

An example from the screenshot below is API-Chloe Demo: Apple Cart-Success:

- API = prefix
- Chloe Demo: Apple Cart = Name of the integration
- Success = name of scenario

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_troubleshooting_integration-2.png)

As a quick look to see if an integration, you can also hover over the tag symbol on a conversation log to see the tags associated with the conversation.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_troubleshooting_integration_3.png)

If you only want to see why a conversation with an API errored, in the Labels search, search for apiError.

Then, select your conversation to see more information.

When you are in the conversation, you can check what exists in the session data.

To do this, click Details in the top right.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_troubleshooting_integration_4.png)

Once you click this, you will see the Conversation Overview. Next, click Session Data.

Now you can see the session data in the chat. Out of interest here, we see at the bottom, the session parameters coming from the API integration.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_troubleshooting_integration_5.png)

## Check the dialogue for session parameters

To quickly check that the session parameters exist for the session you can log them in an AI agent message via the dialogue. This is safest to do when testing the dialogue in a staging environment or, if the integration is live, make sure that you do not save the dialogue when testing.

In the AI agent message below, the session parameters are being logged so that they are visible when testing.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_troubleshooting_integration_6.png)

## Output the raw values into a failure scenario

Make a string of all the data in the response by wrapping ‘data’ in the function `$string(data)`. This can then be logged in the failure scenario when testing to quickly see what is being returned.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_troubleshooting_integration_7.png)

## Check the HTTP status code

When you test the integration, make sure to check the http status code that is returned. You will see this in the response on the right with the key of `statusCode`.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_troubleshooting_integration_8.png)

### 2xx: Success

- **200 OK:** The request was successful, and the server responded with the expected data.  
  - This is the ideal response when testing an integration.

### 4xx: Client errors

Errors in this range generally indicate an issue with the request sent in the integration builder.

- **400 Bad Request:** The server could not understand the request due to invalid syntax or missing parameters.  
  - Check the request payload for errors, missing fields, or incorrect formatting.
- **401 Unauthorized:** Authentication is required but was not provided or is invalid.  
  - Verify the API key, token, or other authentication credentials. Double-check authorization headers.
- **403 Forbidden:** The server understood the request but refuses to authorize it.  
  - Ensure that your IP addresses are allowlisted, or verify permissions for the API.
- **404 Not Found:** The requested resource could not be found on the server.  
  - Check the URL or endpoint. Ensure the correct path is being used and the resource exists.

### 5xx: Server Errors

Errors in this range typically indicate an issue on the backend server.

- **500 Internal Server Error:** A generic error indicating that something went wrong on the backend server.  
  - Contact the backend team with details of the request for further debugging.
- **502 Bad Gateway:** The server received an invalid response from an upstream server.  
  - This often indicates an issue with the backend's internal services or dependencies.
- **503 Service Unavailable:** The server is currently unable to handle the request, possibly due to overload or maintenance.  
  - Retry after some time, and check if there is scheduled downtime.
- **504 Gateway Timeout:** The server did not receive a timely response from an upstream server.  
  - Ensure the backend service is operational and check for latency issues.

## Investigate any technical errors in the dialogue

Sometimes, you might see a message with a technical error. A technical error includes the following text:

“I'm really sorry, there seems to be a technical problem. I hope I'll be back to working order soon.”

In this scenario, the issue is most likely a dialogue error, rather than anything related to the integration itself. Here are some tips:

- Check the dialogue to ensure that the flow reaches the integration. Use buffer messages to confirm, and check for issues like mixed button functionalities, broken links, or circular references.
- Verify that any required parameters are present. Missing required parameters will trigger errors before the integration runs.
- For dynamic content, such as cards and carousels, ensure that all fields are populated. Undefined, blank, or null values can break these components and cause errors.