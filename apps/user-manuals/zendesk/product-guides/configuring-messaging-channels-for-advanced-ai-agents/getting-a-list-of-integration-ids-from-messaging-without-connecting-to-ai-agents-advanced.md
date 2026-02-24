# Getting a list of integration IDs from messaging without connecting to AI agents - Advanced

Source: https://support.zendesk.com/hc/en-us/articles/8357757769114-Getting-a-list-of-integration-IDs-from-messaging-without-connecting-to-AI-agents-Advanced

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | AI agents - Advanced |

This guide describes how to obtain a list of integration IDs from messaging without connecting to AI Agents - Advanced.

**Note**: This guide uses [Postman](https://www.postman.com/product/what-is-postman/). If you don't have Postman, you can sign up for an account on the [Postman website](https://identity.getpostman.com/signup) and download the app.

1. From the AI agents - Advanced dashboard, click **Send an API request**.

## 

The following appears.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_21155903259666.png)

2. View the [List Integrations](https://docs.smooch.io/rest/#operation/listIntegrations) GET request from Sunshine Conversations.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_21155903262482.png)

3. Copy the appropriate endpoint server from Sunshine Conversations, depending on your region, and paste it into Postman.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_21155872407058.png)

Next, we'll obtain the App ID as it's a required parameter in the List Integrations endpoint.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_21159052949650.png)

4. In Zendesk Admin Center, click **Apps and integrations** in the sidebar, then select **APIs > Conversations API**.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_21155872410386.png)

5. Click **Create API key**. If you are creating your first key, this button appears at the bottom of the page; if you have previously created a key, it appears in the top-right corner.

6. Enter an identifying name for the key in the Create new key dialog, then click **Next**.

7. In the Copy shared secret dialog, click **Copy** for each ID and secret key to save it to your clipboard, then click **Next**.

**Important**: Be sure to copy the App ID, Key ID and Secret Key and store them in a secure location, as they will not be shown again in the interface.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_21155903275410.png)

8. In Postman, replace {appId} in the URL with the App ID you copied from above.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_21159028563858.png)

9. Click the **Authorization** tab, and select **Basic Auth** from the dropdown menu.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_21159028569618.png)

10. For Username, enter the Key ID you previously copied. For Password, enter the Secret Key you copied earlier.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_21159052964114.png)

11. Click **Send**.

The response will list all of your integration IDs. Each integration ID will specify its type, making it easy to differentiate between them.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_21159052967826.png)

Now that you have the list of all your integrations, you can assign them a default responder. This prevents AI agents - Advanced from taking over that channel when they are connected to AI agents - Advanced.