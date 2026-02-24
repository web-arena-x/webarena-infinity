# Finding your switchboard and responder IDs for AI agents - Advanced

Source: https://support.zendesk.com/hc/en-us/articles/9200200370970-Finding-your-switchboard-and-responder-IDs-for-AI-agents-Advanced

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | AI agents - Advanced |

If you've integrated AI agents - Advanced with your Zendesk instance, it's possible that all of your channels are already using an advanced AI agent as a default responder. If you want certain channels to use an essential AI agent instead, you need to find the AI agent's responder ID to set it as the default responder.

In this scenario, you can use two APIs in combination to find all of your Zendesk instance’s available responders and their corresponding IDs.

Note: This guide uses [Postman](https://www.postman.com/product/what-is-postman/). If you don't have Postman, you can sign up for an account on the [Postman website](https://identity.getpostman.com/signup) and download the app.

This article contains the following topics:

- [Finding your switchboard ID](#topic_r3h_myq_ffc)
- [Finding your responder IDs](#topic_uqv_myq_ffc)

Related articles:

- [Setting per-channel default responders using an API call in Sunshine Conversations](https://support.zendesk.com/hc/en-us/articles/8357757911834)
- [Getting a list of integration IDs from messaging without connecting to AI agents - Advanced](https://support.zendesk.com/hc/en-us/articles/8357757769114)

## Finding your switchboard ID

Use the [List Switchboards](https://docs.smooch.io/rest/#operation/ListSwitchboards) API call to find your switchboard ID. The switchboard is automatically created when you [deploy messaging](https://support.zendesk.com/hc/en-us/articles/5746900266906) on your Zendesk instance.

By default, you have only one switchboard. However, you can create more switchboards using the API. Most organizations will not have created an extra switchboard, but if you did, you’ll need to check all of your switchboards until you find the one with AI agents - Advanced.

**To find your switchboard ID**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)
   **Apps and integrations** in the sidebar, then select **APIs > Conversations API**.
2. Select the API key you created when you integrated with AI agents - Advanced, or else create a new API key to use for the API call that can be deleted when you're done.

   For help, see [Using the Conversations API keys](https://support.zendesk.com/hc/en-us/articles/4576088682266).
3. Note the following information:
   - **App ID**
   - **Key ID**
   - **Secret key**

     Note: For security reasons, you can't actually see the secret key for your original API key in Admin Center. If you didn't save the secret key somewhere safe, you'll need to create a new API key instead.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_api_key_details_example.png)
4. In Postman, use one of the following request URLs, depending on your region:
   - For the US:
     *https://api.smooch.io/v2/apps/{appId}/switchboards*
   - For the EU:
     *https://api.eu-1.smooch.io/v2/apps/{appId}/switchboards*

     Replace *{appId}* with the App ID you noted above.
5. In **Auth Type**, select **Basic Auth**.
6. In **Username**, enter the key ID you noted above.
7. In **Password**, enter the secret key you noted above.
8. Click **Send**.
9. Note the switchboard ID that's returned.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_postman_switchboard_ids.png)

Now that you have your switchboard ID, follow the instructions in the next section to find your responder IDs.

## Finding your responder IDs

Use the [List Switchboard Integrations](https://docs.smooch.io/rest/#operation/ListSwitchboardIntegrations) API call to find your responder IDs.

**To find your responder IDs**

1. In Postman, use one of the following request URLs, depending on your region:
   - For the US:
     *https://api.smooch.io/v2/apps/{appId}/switchboards/{switchboardId}/switchboardIntegrations*
   - For the EU:
     *https://api.eu-1.smooch.io/v2/apps/{appId}/switchboards/{switchboardId}/switchboardIntegrations*

     Replace *{appId}* with the same app ID you noted above, and replace *{switchboardId}* with the switchboard ID you noted above.
2. In **Auth Type**, select **Basic Auth**.
3. In **Username**, enter the key ID you noted above.
4. In **Password**, enter the secret key you noted above.
5. Click **Send**.
6. Note the responder IDs that are returned.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_postman_responder_ids.png)

You now have your responder IDs, which you can use to update your integrations and add or remove them from AI agents - Advanced.