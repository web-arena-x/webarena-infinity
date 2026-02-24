# Creating conversations integrations in Admin Center

Source: https://support.zendesk.com/hc/en-us/articles/4576083789850-Creating-conversations-integrations-in-Admin-Center

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

Note: You must have a [Zendesk Suite Professional plan or above](https://support.zendesk.com/hc/en-us/articles/4408846875034) to create conversations integrations. Learn about [Sunshine Conversations pricing](https://www.zendesk.com/pricing/) or [Contact Sales](https://www.zendesk.com/contact/) for more information.

Conversations integrations help businesses unify messages from every channel, chatbot, or third-party app into a single conversation and build interactive experiences everywhere.

Conversations integrations are a bidirectional interaction between your business and Sunshine Conversations. The integration consists of:

- A webhook.
- (optional) A set of API keys to interact with the public API with a scope of integration. For information on creating the API keys, see [Using Conversations API keys](https://support.zendesk.com/hc/en-us/articles/4576088682266).

Note: Conversations integrations were formerly known as [webhooks](https://docs.smooch.io/rest/#tag/Webhooks) in the Sunshine Conversations dashboard.

You can create conversations integrations through the Conversations Integrations page in Admin Center.

You can also create your integration using [curl](https://curl.se/) or [Postman](https://www.postman.com/).

This article includes the following sections:

- [Creating and configuring conversations in Admin Center](#topic_oqh_5y2_nvb)
- [Other integration methods](#topic_qvc_vy2_nvb)

## Creating and configuring conversations in Admin Center

From the Conversations Integrations page, you can:

- [Create a new integration](#topic_ymg_drm_nvb)
- [Add an API key](#topic_wf5_drm_nvb)
- [View, edit, or delete an integration](#topic_wy1_2rm_nvb)

### Creating a new conversation integration

**To create a conversations integration in Admin Center**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png) **Apps and integrations** in the sidebar, then select **Integrations > Conversations integrations**. The Conversations Integrations page opens. Any previously-created conversations appear in the list.

   If this is your *first* time creating an integration in Admin Center, click **Create integration** to view the Conversations Integrations page.
2. Click **Create integration**. The Create Integration page opens.
3. Enter a unique name to identify the integration.
4. In the Webhook section, enter the following information:

   - **Webhook endpoint URL**: The target URL. When a trigger event occurs, the webhook sees the event and sends the data to the target URL. The target URL uses the following format: `https://www.yourdomain.com/path`.
   - **Webhook body data**: Use the checkboxes to indicate whether you want to include the user schema and client and device information in the webhook data.
   - **Webhook subscriptions**: Select the events that you want to be notified on.
5. Click **Save**. The Copy shared secret window opens.
6. (Optional) Copy the Webhook ID and Shared secret. These are used by developers to add another layer of authentication and are not required.
7. Click **Next**. The integration’s configuration page opens. From here you can add an API key, if necessary.

### Adding an API key

On the API key tab, you can configure authentication for the integration. An API key identifies and authenticates an application or user and is composed of three pieces:

- The **App ID** identifies your Zendesk account.
- The **Key ID** when used together with the secret key are the credentials used to authenticate JWTs and API calls.
- The **secret key** is the authentication password.

Note: API keys configured in the Conversations Integrations edit page are for custom integrations. They are scoped to a specific custom integration and cannot modify other integrations. For app-level API keys, see the [Sunshine Conversations Authentication page](https://docs.smooch.io/rest/#section/Introduction/Authentication).

**To create and share an API key**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png) **Apps and integrations** in the sidebar, then select **Integrations > Conversations integrations**. The Conversations Integrations page opens.
2. Click the API key tab.
3. Click **Create API key**. If you are creating your first key, this button appears at the bottom of the page; if you have previously created a key, it appears in the top-right corner.
4. Enter an identifying name for the key in the Create new key dialog, then click **Next**.
5. In the Copy shared secret dialog, click **Copy** for each ID and secret key to save it to your clipboard, then click **Next**. You're returned to the API window, where the new key appears in the list.

If you generate a new key but have reached your 10-key limit, a notification appears, asking you to delete any unused keys.

**To delete an unused key**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png) **Apps and integrations** in the sidebar, then select **Integrations > Conversations integrations**.
2. Click the API key tab.
3. Hover your mouse pointer over the key you want to delete, then click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/support_trigger_options.png)) and select **Delete**.

Confirm the action by clicking **Delete**.

### Viewing, editing, or deleting an integration

**To work with an existing integration**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png) **Apps and integrations** in the sidebar, then select **Integrations > Conversations integrations**. The Conversations Integrations page opens.
2. Hover over the integration you want to update and click the **Options icon** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ticket_field_options_icon.png)), then select an option:

   - **View details**: Displays the integration's details page, where you can view the App, Integration, and Webhook IDs, as well as information on shared secrets, webhook details, and API keys.
   - **Edit**: Opens the Create Integrations page, where you can update the integration's name and webhook details.
   - **Delete**: Launches a deletion wizard. You can cancel and exit the wizard at any time.

## Other integration methods

These methods are available only to users with a separate Sunshine Conversations license, not the license that comes with Zendesk Suite Professional or above.

**To create a conversations integration using curl**

1. Create an integration using the [Create Integration](https://docs.smooch.io/rest/#operation/createIntegration) API and set `type` to `custom`.
2. Provide the necessary parameters as specified in the API. The target is the URL of your server and the list of triggers determines which events to receive.

**To create a conversations integration using Postman**

1. Create an integration using the [Create Integration](https://docs.smooch.io/rest/#operation/createIntegration) API and set `type` to `custom`.
2. Download and install the [Postman](https://www.postman.com/downloads/) application.
3. Download the Sunshine Conversations [Postman collection](https://docs.smooch.io/guide/postman-collection/#postman-collection) and set up your environment.
4. In Postman, select **Smooch > Integrations > Create Integrations**.
5. Provide the necessary parameters as specified by your integration type.

For more information on the Sunshine Conversations APIs, see [Integrations](https://docs.smooch.io/rest/#tag/Integrations).

Also see the guides on [sending](https://docs.smooch.io/guide/sending-messages/) and [receiving](https://docs.smooch.io/guide/receiving-messages/) messages. You will want to [configure webhooks](https://docs.smooch.io/rest/#operation/createWebhook) using REST APIs.