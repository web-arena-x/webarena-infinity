# Understanding and installing the Workday app for Zendesk Support

Source: https://support.zendesk.com/hc/en-us/articles/8220920383258-Understanding-and-installing-the-Workday-app-for-Zendesk-Support

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Verified AI summary ◀▼

Integrate the Workday app to access employee data directly within tickets, enhancing your ticketing experience. Sign in using Workday credentials to view relevant employee information, aiding in quick resolutions. Customize the app to fit your needs, ensuring data security and flexibility. Install and connect the app via the marketplace, and manage its availability with options to turn off or disconnect as needed.

If your organization uses Zendesk to manage employee support requests, integrating the
Workday sidebar app can significantly enhance your ticketing experience. The app allows
agents to access essential employee data directly within Zendesk tickets, expediting
ticket resolution and optimizing agent workflows.

This article includes the following topics:

- [About the Workday app for Zendesk Support](#topic_spz_k3r_mdc)
- [Installing and connecting the Workday app](#topic_tv2_5m3_ldc)
- [Turning off the Workday app](#topic_pj3_cbq_jdc)
- [Disconnecting the Workday app](#topic_qky_bq3_ldc)

## About the Workday app for Zendesk Support

The Workday sidebar app integration with Zendesk enhances agents' efficiency by
offering a view of employee data directly within Zendesk tickets.

For example, an HR agent working on tickets related to policy questions can view
information (such as the employee's position or employment status) without switching
to Workday. Similarly, an IT agent assisting with a hardware purchase can reference
an employee's address to determine where to send equipment.

Agents sign in to the app from the Apps panel (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_omnipanel_apps.png)) using their Workday credentials. After signing in,
agents see the ticket requester's employee data in the sidebar of a ticket. This
information is presented based on field matching you've configured between Workday
and Zendesk.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/workday_sidebar_app_worker.png)

The app is customizable by admins, as described in [Configuring the Workday app for Zendesk Support](https://support.zendesk.com/hc/en-us/articles/9391945391642). The app
ensures data security by displaying only information that agents can access in
Workday. Additionally, the app supports multiple Workday and Zendesk instances,
ensuring flexibility for organizations with various configurations.

Workday data will be cached for one hour to minimize API calls. Agents can refresh
the data on demand anytime by clicking the refresh icon available in the Workday
app.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/workday_refresh_icon.png)

Watch the video below for information about the Workday app for Zendesk Support.

Workday integration: Deliver fast employee service with insights (1:39)

## Installing and connecting the Workday app

To get your organization started with the Workday app, follow these steps:

- [Step 1: Create an OAuth client
  in Workday](#topic_qlr_1n3_ldc)
- [Step 2: Install and connect
  the Workday app](#topic_ipz_bn3_ldc)

### Step 1: Create an OAuth client in Workday

Workday uses OAuth 2.0 for authorization, which requires setting up an OAuth 2.0
client in Workday. This allows Zendesk to obtain secure access to your data in
Workday. You must be a Workday administrator to create an OAuth client.

After you save the OAuth configuration, Workday generates a Client ID and Client
Secret. Save these securely, as they will be needed when creating the Workday
configuration in Zendesk.

**To set up an OAuth 2.0 client in Workday**

1. Log in to your Workday account as an administrator.
2. In the Workday search bar, type **Edit Tenant Setup - Security**, then
   select the matching option from the search results list.
3. Scroll down to the OAuth 2.0 Settings section and turn on the **OAuth
   2.0** configuration.
4. Configure the API client:
   - **Search**: Select **Register API Client**.
   - **Client Name**: Enter a meaningful name for your client
     (example: "Zendesk sidebar app").
   - **Client Grant Type**: Choose **Authorization Code**. See
     [OAuth 2.0 Security Best Current
     Practice](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-security-topics) for more information about grant types.
   - **Client Redirect URL**: Enter
     `https://zis.zendesk.com/api/services/zis/connections/oauth/callback`
5. Assign the necessary **API scopes** (permissions) for the app to access
   Workday data. For example, include Workday API scopes like employee
   information (such as the Workday Human Resources API).
   - Add `system`, as it is a required scope.
   - For security purposes, provide the app with only the minimally
     required permissions.
6. Click **Save**.
7. After saving, a new page appears. Workday generates values for the following
   fields, which will be required for connection, authentication, and token
   generation. Record these values and securely save them.
   - Client ID
   - Client Secret
   - Token Endpoint URL
   - Authorization Endpoint URL

   Important: The Client Secret will
   *be displayed only once*. Copy and save it in a safe place,
   such as in a password manager.

### Step 2: Install and connect the Workday app

The Workday sidebar app can be installed from the Zendesk Marketplace.

**To install the Workday app**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)
   **Apps and integrations** in the sidebar, then select **Apps > Zendesk Support
   apps**.
2. Click **Marketplace**.
3. In the **Keywords** search box, type **Workday** to locate the Workday
   app.
4. Click the **Workday** app, then click **Install**.
5. Review the terms and conditions, then select the checkbox to accept.

   You
   are directed to the Workday configuration page Admin Center.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/workday_zendesk_config.png)
6. Complete the fields on the Workday configuration page.
   - **Integration name**: Enter a name for the integration. If you
     are setting up multiple connections, give the integration a
     meaningful name, such as the company or brand name to which the
     connection applies.
   - **OAuth grant type**: Select **Authorization code** or
     **Client credentials**. See [OAuth 2.0 Security Best Current
     Practice](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-security-topics) for more information about grant types.
   - Enter these values in their respective fields. These values were
     provided in Workday when you created the [OAuth client](#topic_qlr_1n3_ldc) in
     step 1.
     - Client ID
     - Client Secret
     - Authorize URL
     - Token URL
     - Scopes
7. Select the **Built by Zendesk Terms of Use** checkbox to confirm you
   agree to the terms of this integration.
8. Click **Next**.
9. Click **Save**.

The Workday app is connected and turned on for agents.

## Turning off the Workday app

If you want to hide the Workday app from agents temporarily, you can turn it off. The
app will no longer be visible to agents in the Apps panel.

**To turn off the Workday app for agents**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)
   **Apps and integrations** in the sidebar, then select **Integrations >
   Integrations**.
2. Click **Workday** in the list.
3. If you have multiple connections set up, click the name of the Workday
   connection you want to turn off.
4. Clear the **Turn on Workday app for Zendesk Support** checkbox.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/workday_turn_off.png)
5. Click **Save**.

## Disconnecting the Workday app

You can disconnect the Workday app if you no longer want to use it in your Zendesk
account. The app will no longer be visible to agents in the Apps panel, and you'll
have to create a new Workday configuration if you decide to use the app again.

**To disconnect the Workday app**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)
   **Apps and integrations** in the sidebar, then select **Integrations >
   Integrations**.
2. Click **Workday** in the list.
3. If you have multiple connections set up, click the name of the Workday
   connection you want to disconnect.
4. Click **Actions**, then click **Disconnect** from the drop-down menu.
5. Click **Disconnect** in the confirmation message.