# Using custom authorization with the integration builder

Source: https://support.zendesk.com/hc/en-us/articles/8357749813658-Using-custom-authorization-with-the-integration-builder

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | AI agents - Advanced |

The [integration builder](https://support.zendesk.com/hc/en-us/articles/8357756844442) supports standard authorization types, including API keys, bearer tokens, username and password, and OAuth 2.0. However, based on your organization’s needs and workflows, standard authorization might not be sufficient. That’s why the integration builder also supports a custom auth-only integration type that works with your organization’s authentication and authorization solutions.

This article contains the following topics:

- [About custom authorization](#h_01J8MXSSKDV5ZTW5T1A2SFRV1T)
- [Configuring custom authorization](#h_01J8MY2GKQWV4J4KQ3A8HBXF8M)
- [Creating the data integration](#h_01JTNSPT2D3E3MA2W96W300H3J)
- [Testing custom authorization](#h_01J8MY2RH9JS06CZ0GJDFHZZ67)

## About custom authorization

The custom auth-only integration makes a request for a token and its expiry, which it then passes to the data or main integration for authorization to then make the request for the data.

Overall, the custom authorization flow is as follows:

1. **Authorization request.** The configured auth-only integration sends a request to the server, asking for permission to retrieve an access token. If the server authenticates the request (coming from AI agents - Advanced), it authorizes the retrieval of the access token and, if available, its expiration time.
2. **Handling the token.** After the server responds with the access token, the integration stores two key pieces of information: the token parameter itself and its expiresIn parameter, which determines how long the token is valid.
3. **Passing the token to the data integration.** These two parameters (token and expiresIn) are passed to the next step, which is the data integration. The token is used to authenticate subsequent requests made by the data integration. The token is set and handled internally, and is never exposed to the session or conversation data.
4. **Custom authorization request for data.** With the access token in place, the data integration is now authorized to retrieve the necessary data, which is used to enrich the conversation.

The flowchart below illustrates the custom authorization flow.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ultimate_custom_auth_flowchart.png)

## Configuring custom authorization

You configure custom authorization as part of the normal process of creating an integration in the integration builder.

Note: Don't use more than one environment at a time for the custom authorization. If you want to split into Production, Sandbox, and so forth, split them into separate authorization integrations.

**To configure custom authorization in the integration builder**

1. In the main menu, click **API Integrations**.
2. In the top right, click **Add Integration**.
3. In the **Add Integration** window:
   1. In the **Integration name** field, give your integration a descriptive name.
   2. (Optional) In the **Description** field, enter a description of the integration that helps you remember what it’s for.
   3. Select **Setup as an ‘auth only’ integration**.
   4. Click **Save**. 
      ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ultimate_custom_auth_add_integration.png)
4. In the left sidebar, under **Scenarios**, hover over **Failure**, select the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/macros_edit_menu_icon.png)) and select **Delete**. For custom authorization, you only need Success scenarios. You can’t delete Fallback scenarios. 
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ultimate_custom_auth_delete_failure.png)
5. On the **Success** scenarios page, create two session parameters (by clicking the **+** button) with the following details:
   - token
     - **Key:** token *(must be written exactly like this)*
     - **Query:** Enter a value that defines the token. For example: data.access\_token
   - expiresIn
     - **Key:** expiresIn *(must be written exactly like this)*
     - **Query:** Enter a value that defines the token expiry. For example: data.expires\_in Token expiry may not be part of your data response. In that case, you can hardcode a value (in seconds) of your choice. For example: 3600 We strongly recommend setting a token expiry. If you run into an error when testing, this is the amount of time you’ll need to wait before a new token is issued. With no expiry, the token is set indefinitely, meaning you won’t be able to issue a new one during troubleshooting.
       ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ultimate_custom_auth_params.png)
6. Click **Save**.

## Creating the data integration

Next, create the data integration that will use the custom auth only integration you created in the steps above. Do this as you normally would when creating a new integration. For help, see [Integration Builder Explained](https://support.zendesk.com/hc/en-us/articles/8357756844442).

**To create the data integration**

1. In the left sidebar, under **Environments**, select an environment (such as Production).
2. On the **Authorization** tab, in the **Authorization Type** drop-down field, select **Custom**.
3. In the **API authorization integration** drop-down field, select the custom auth-only integration you created above. 
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ultimate_custom_auth_type.png)
4. Select the **Headers** tab and click **Add Header**.
5. Fill in the following fields:
   - **Key:** Authorization
   - **Value:** Bearer {{apiToken}} *(must be written exactly like this)* 
     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ultimate_custom_auth_header.png)
6. Click **Save**.

## Testing custom authorization

After you configure your custom auth-only integration, we recommend testing it. For help, see [Test Functionality](https://support.zendesk.com/hc/en-us/articles/8357756844442-Integration-Builder-Explained#4-test-functionality).

### Troubleshooting statusCode: null

Additionally, when testing your integration, you might encounter a “statusCode: null” message, as shown in the image below: 
![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ultimate_custom_auth_statusCode_null.png)

First, double-check that your custom auth-only integration has been correctly configured according to the [steps above](#h_01J8MY2GKQWV4J4KQ3A8HBXF8M).

Next, take note of where the error is occurring. If it’s in the auth integration, something likely isn’t configured correctly, or the URL you’re making the request to might be wrong. In this case, we recommend checking with engineers on your side, as they may be able to provide more information on what’s wrong.

If you’ve taken the steps above and are still encountering this error, wait until the token expires and try again.

If you’ve tried all of these troubleshooting steps and the integration still isn’t working, contact your CSM for additional assistance.