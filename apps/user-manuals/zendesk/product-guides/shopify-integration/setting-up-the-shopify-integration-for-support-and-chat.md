# Setting up the Shopify integration for Support and Chat

Source: https://support.zendesk.com/hc/en-us/articles/4408820093850-Setting-up-the-Shopify-integration-for-Support-and-Chat

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Support customers must also have Chat to use this integration.

The Shopify integration for Support and Chat includes an app so agents can view Shopify order information, reducing context switching and serving customers faster. They can also process Shopify order refunds and cancellations in the Support app without leaving the context of their ticket.

The integration allows multiple Shopify storefront connections to your Zendesk account. You can also add Web Widget (Classic) on your Shopify storefront page so that customers can contact your support team while visiting your site.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/shopify_v3_app1.png)![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/shopify_v3_app2.png)

To set up the integration, you need to have a Shopify account.

Note: After setting up the integration, one or more **Shopify order ID** custom ticket fields are added to your ticket forms. These fields were used in a legacy integration and can be ignored. They will be removed in a future release.

This article includes the following topics:

- [Connecting a Shopify storefront to Zendesk](#topic_jyf_nbc_f4b)
- [Configuring the Shopify app in Support or Chat](#topic_kdg_jcc_f4b)
- [Adding Web Widget to your Shopify storefront](#topic_j3b_kcc_f4b)
- [Connecting another Shopify storefront to Zendesk](#topic_fdn_pcc_f4b)
- [Disconnecting a Shopify storefront connection](#topic_fsc_qcc_f4b)

## Connecting a Shopify storefront to Zendesk

Setting up the Shopify integration initially requires installing the integration from the Shopify app store, then creating a connection between Zendesk and your Shopify storefront.

**To connect Zendesk and a Shopify storefront**

1. Go to the [Zendesk app](https://apps.shopify.com/zendesk) in the Shopify app store and click **Install**.
2. Select the storefront in which to install the integration.
3. Click **Install**.
4. Add your Zendesk subdomain, then click **Submit**.

   You are directed to Zendesk [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554).
5. In **Connection name**, enter a name for your integration, then click **Connect**.

The Zendesk app is automatically installed in your Shopify storefront, and you are redirected back to Admin Center.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/shopify_v3_connection.png)

Once the connection has been established, you can connect more storefronts or configure different features, as described in the following sections.

## Configuring the Shopify app in Support or Chat

After connecting a Shopify storefront, the Shopify sidebar app is automatically enabled in Admin Center to display in Support and Chat. A sidebar app is displayed for each Shopify storefront.

**To configure the Sidebar app for Support**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)
   **Apps and integrations** in the sidebar, then select **Integrations >
   Integrations**.
2. On the Integrations page, click **Shopify**.
3. In the storefront connection card, click **Configure**.
4. Select **Sidebar app** in the left sidebar.
5. In the **Sidebar app for Support** or **Sidebar app for Chat** card, select **Configure**.
6. To display the app, select the **Sidebar app** checkbox.
7. In the **Sidebar app for Support** card, select the **Refunds and cancellations** checkbox to enable the refunds and cancellations feature.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/shopify_v3_enable_refunds2.png)
8. Click **Save**.

**To uninstall the Shopify app**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)
   **Apps and integrations** in the sidebar, then select **Integrations >
   Integrations**.
2. On the Integrations page, click **Shopify**.
3. In the storefront connection card, click **Configure**.
4. Select **Sidebar app** in the left sidebar.
5. In the **Sidebar app for Support** or **Sidebar app for Chat** card, select **Configure**.
6. To uninstall the app, select the **Uninstall** link.

**To reinstall the Shopify app**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)
   **Apps and integrations** in the sidebar, then select **Integrations >
   Integrations**.
2. On the Integrations page, click **Shopify**.
3. In the storefront connection card, click **Configure**.
4. Select **Sidebar app** in the left sidebar.
5. Install the sidebar apps you require.
   - To install the Support app, select **Configure** in the Sidebar app for Support card, then click **Install**.
   - To install the Chat app, select **Configure** in the Sidebar app for Chat card, then click **Install**.

## Adding Web Widget to your Shopify storefront

Web Widget can be displayed on your Shopify storefront page so customers can self-serve or connect with your agents. By default, [messaging functionality](https://support.zendesk.com/hc/en-us/articles/4408827701530) is automatically enabled for Web Widget. See [Enabling messaging for migrating accounts](https://support.zendesk.com/hc/en-us/articles/4408832031898). If messaging functionality is disabled, Web Widget (Classic) will be installed.

Note: You can only add the default brand Web Widget to each Shopify store you have within the Shopify integration. If you have more than one Web Widget, manually insert the code for the specific brand into the theme of the Shopify store.

**To add the Web Widget to your Shopify storefront**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)
   **Apps and integrations** in the sidebar, then select **Integrations >
   Integrations**.
2. On the Integrations page, click **Shopify**.
3. In the storefront connection card, click **Configure**.
4. In the left sidebar, select **Web Widget**.
5. Activate **Enable Web Widget**.   
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/shopify_enable_web_widget.png)
6. Click **Go to Shopify Theme Apps Editor**.
7. In the Shopify **App embeds** menu on the left, activate **Web Widget**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/shopify_app_enable_web_widget.png)
8. Click **Save**.

## Connecting another Shopify storefront to Zendesk

The integration supports connecting multiple Shopify storefronts to a Zendesk instance.

**To connect your account to another Shopify storefront**

1. Log in to the Shopify storefront that you wish to add. (If you are only logged into your original Shopify storefront, you won't be able to add the new storefront.)
2. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)
   **Apps and integrations** in the sidebar, then select **Integrations >
   Integrations**.
3. On the Integrations page, click **Shopify**.
4. Click **New connection**.
5. In the Shopify app store, click **Add app**.
6. If prompted, select the Shopify storefront in which to install the integration.
7. Click **Install app**.
8. Add your Zendesk subdomain, then click **Submit**.

   In Zendesk, the integrations page opens the new storefront to connect.
9. Under **Connection name**, enter a name for your integration, then click **Connect**.

   The Zendesk app is automatically installed in your Shopify storefront, and you are redirected back to Admin Center displaying your storefront connections.

## Disconnecting a Shopify storefront connection

You can disconnect your storefront connection to Zendesk in Admin Center, which will also remove the Shopify sidebar apps, Web Widget in your storefront, and the Zendesk app in your Shopify storefront.

**To disconnect your integration**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)
   **Apps and integrations** in the sidebar, then select **Integrations >
   Integrations**.
2. On the Integrations page, click **Shopify**.
3. In the storefront connection card, click **Configure**.
4. Click **Disconnect** in the upper right corner.
5. Click **Confirm**.