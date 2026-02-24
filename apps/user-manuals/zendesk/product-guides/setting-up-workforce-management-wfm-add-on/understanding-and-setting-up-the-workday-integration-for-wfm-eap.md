# Understanding and setting up the Workday integration for WFM (EAP)

Source: https://support.zendesk.com/hc/en-us/articles/9704360178586-Understanding-and-setting-up-the-Workday-integration-for-WFM-EAP

---

As an admin, you can integrate Workday with your Zendesk Workforce management (WFM) account to automatically import approved time off data from Workday into WFM.

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | Workforce Management (WFM) or Workforce Engagement Management (WEM) |

Verified AI summary ◀▼

Integrate Workday with your Workforce Management to automatically import approved time off data, streamlining leave management. Syncs occur hourly, mapping users by email. Set up involves creating an OAuth client in Workday, configuring integration settings, and mapping time off reasons. Partial day requests need manual approval. You can edit or disconnect the integration anytime, ensuring flexibility in managing time off data.

The Workday integration for Workforce management is currently available
as part of an early access program (EAP). You can [sign up for the EAP here](https://docs.google.com/forms/d/1rlCjxcldFthYF-fQCoQCXefEyXaW5g0MEnREepTI8ZE/viewform?edit_requested=true#responses).

As an admin, you can integrate Workday with your Zendesk Workforce management (WFM)
account to automatically import approved time off data from Workday into WFM.

This article contains the following topics:

- [About the Workday integration with
  Workforce management](#topic_a4x_1nr_pgc)
- [Connecting the Workday integration
  with Zendesk WFM](#topic_vrb_ltr_pgc)
- [Reviewing Workday partial time off
  requests](#topic_ivd_btz_pgc)
- [Editing the Workday integration
  with Zendesk WFM](#topic_skp_sms_pgc)
- [Disconnecting the Workday
  integration with Zendesk WFM](#topic_s5g_1rt_pgc)

## About the Workday integration with Workforce management

After connecting Workday with WFM, Zendesk admins and team members in a [custom role with permission](https://support.zendesk.com/hc/en-us/articles/4408882153882) can configure the integration to
automatically import time off data from Workday.

When using this integration, approved time off requests in Workday are visible on
the [WFM Time off management page](https://support.zendesk.com/hc/en-us/articles/6443393050394). Within the list, these requests can
be identified by having Workday as their source. Full day time off requests appear under the
Closed tab, while partial time off requests display under the Pending tab and must undergo
[manual review and approval](#topic_ivd_btz_pgc) by an
admin.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_schedule_timeoff_full.png)

Time off in Workday also syncs to WFM and displays in the [Schedule page](https://support.zendesk.com/hc/en-us/articles/6443348279194).

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_schedule_workday.png)

Published Workday time off is displayed to agents on their [agent schedule](https://support.zendesk.com/hc/en-us/articles/6443374353434) page.

## Connecting the Workday integration with Zendesk WFM

When you use the Workday integration for WFM, data from Workday, including
time off and leave, syncs to WFM every hour.

Workday users are mapped to WFM users by email. Time off data is synced only for mapped users. Users who have the same email address assigned to multiple users in Workday
can't be synced.

One Workday instance can be connected to multiple Zendesk instances. For the integration to
work properly, separate OAuth clients have to be created in Workday and provided in the
integration setup.

**To connect the Workday integration with Zendesk WFM**

1. [Create an OAuth client in
   Workday](#topic_q34_qtr_pgc)
2. [Configure the Workday integration for WFM
   in Admin Center](#topic_ily_vbs_pgc)
3. [Configure the Workday with Zendesk WFM
   integration settings](#topic_qd2_gqb_qgc)

### Step 1: Creating an OAuth client in Workday

Workday uses OAuth 2.0 for authorization. A Workday administrator must set up an OAuth 2.0 client in Workday to provide Zendesk secure access to your data in
Workday.

After you save the OAuth configuration, Workday generates a Client ID and
Client Secret. Save these securely. Both values are needed when [configuring the Workday integration for WFM in
Admin Center](#topic_ily_vbs_pgc).

Note: The Client Secret displays only once. Copy and save it in a secure location, such as a
password manager.

**To set up an OAuth 2.0 client in Workday**

1. Sign into your Workday account as an administrator.
2. In the Workday search bar, type **Edit Tenant Setup - Security**, then select the matching option from the search results list.
3. Scroll down to the OAuth 2.0 Settings section and turn on the **OAuth 2.0** configuration.
4. Configure the API client:
   - **Search**: Select **Register API Client**.
   - **Client Name**: Enter a meaningful name for your client, such as *Zendesk
     connection*.
   - **Client Grant Type**: Choose **Authorization Code**. See [OAuth 2.0 Security Best Current Practice](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-security-topics) for more information about grant types.
   - **Client Redirect URL**: Enter

     ```
     https://zis.zendesk.com/api/services/zis/connections/oauth/callback
     ```
5. Use the **API scopes** field to specify the following permissions for the app to access Workday data:
   - ```
     System
     ```
   - ```
     Staffing
     ```
   - ```
     Time off and leave
     ```
6. Click **Save**.
7. After saving, securely save the following generated values that appear in Workday. These are required for connection, authentication, and token generation.
   - Client ID
   - Client Secret

     Note: The Client Secret displays only once. Copy and save it in a secure
     location, such as a password manager.
   - Token Endpoint URL
   - Authorization Endpoint URL
   - Workday REST API URL

Note: If an Admin changes the password in Workday, the OAuth2 client stops functioning. When this happens, you must remove the existing connection and set it up again.

### Step 2: Configuring the Workday integration for WFM in Admin Center

You can set up a connection with multiple Workday instances. Approved time off
data from these instances syncs to WFM.

**To configure a Workday integration for WFM in Admin Center**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)
   **Apps and integrations** in the sidebar, then select **Integrations >
   Integrations**.
2. Click **Workday** in the list.
3. Click **Create connection** and select **Workforce management**.
4. This opens the Workday Client configuration page.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/workday_wfm_integration_setup.png)

   - Enter an **Integration name**. If you're setting up multiple connections, give
     the integration a unique and identifiable name, such as the company or brand name to
     which the connection applies.
   - Enter the values provided in Workday when you created the OAuth client in [Step 1](#topic_q34_qtr_pgc):
     1. Enter the **Client ID** value generated by Workday when you
        created the OAuth client.
     2. Enter the **Client Secret** value generated by Workday when you
        created the OAuth client.
     3. Enter the **Authorize URL** value generated by Workday when you
        created the OAuth client.
     4. Enter the **Token URL** value generated by Workday when you
        created the OAuth client.
     5. Enter the **Scopes** you specified for the Workday OAuth client. Use spaces
        to separate scopes, but don’t include spaces between words within a scope name.
        The value should be:

        ```
        system staffing timeoffandleave
        ```
5. Select **Built by Zendesk Terms of Use** to confirm you agree to the
   terms of this integration.
6. Click **Next**.
7. Under **Authentication**, click **Connect** and sign in to your Workday
   account.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_workday_connect.png)
8. After signing in successfully, click **Allow** to authorize WFM to access your
   Workday account.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_workday_authorize.png)

   If an internal server
   error occurs during the authorization process for WFM to access your Workday account,
   sign into your Workday account first and then set up the connection again.

### Step 3: Configuring the Workday with Zendesk WFM integration settings

Configure how you want Zendesk WFM to import time off data from Workday.

**To configure the Workday with Zendesk WFM integration settings**

1. Select **Import time off data from Workday to Zendesk Workforce management** to
   view your Workday time off data in [WFM schedule](https://support.zendesk.com/hc/en-us/articles/6443348256794).

   Note: If you later [edit the
   integration](#topic_skp_sms_pgc) and deselect this option, the connection remains active but no
   more [time off](https://support.zendesk.com/hc/en-us/articles/6443393050394) data is synced from Workday to
   WFM.
2. (Optional) Select **Delete time off duplicates** to prioritize Workday time off
   requests over Zendesk WFM requests and remove any duplicates.
3. (Optional) Select **Turn off time off requests in Zendesk Workforce management** to
   ensure that agents cannot [request time off from the agent schedule app within Zendesk](https://support.zendesk.com/hc/en-us/articles/6443360882586),
   but only from Workday.
4. Under **Time off reasons mapping** assign a Zendesk type ([planned or unplanned](https://support.zendesk.com/hc/en-us/articles/6443329403034#h_01HGBQJCESJFEA5PTFNAZDZ8PA)) to each Workday time off
   reason.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_workday_configure.png)

   If you see the message “No time off reasons in sight,” it might
   indicate a disruption in the API connection that prevented the time off reasons from
   syncing. In this case, save and enter the connection configuration
   again.

   You can later [edit the time off reason types on the Time off
   reasons page in WFM](https://support.zendesk.com/hc/en-us/articles/6443329403034#h_01HGBQJQVMYJHTRK111ZR0TBNN) and they will automatically sync in Admin
   Center.
5. Click **Save**.

This connection between Workday and WFM is now set up and data is syncing.

Each time new Workday time off reasons are detected, you'll receive an email indicating
that an update to the Workday integration is required to use the new time off reasons in
WFM.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_workday_update_required_email.png)

Clicking the "Assign in Admin Center" button automatically takes you to the
[connection settings page,](#topic_qd2_gqb_qgc) where you
can assign them under "Time off reasons mapping".

The message “Update required” is also displayed under the connection
Status.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_workday_integration_update_required.png)

[Edit the connection](#topic_skp_sms_pgc) to assign the
new Workday time off reason to a Zendesk type.

## Reviewing Workday partial time off requests

Partial day time off requests in Workday must undergo manual review and approval
by an admin before they display on the WFM [Schedule page](https://support.zendesk.com/hc/en-us/articles/6443348279194).

Ensure that you align with the time zone of the agent for whom you are
assigning a time off start time. To do this, use the [WFM time zone switcher](https://support.zendesk.com/hc/en-us/articles/6443314319258).

**To review Workday partial day time off requests**

1. By default, pending time off requests are displayed. You can view pending
   time off requests by team or individual agent. See [Viewing time off requests](https://support.zendesk.com/hc/en-us/articles/6443393050394#topic_t2b_1hs_kbc).
2. Hover over the request you want to review. In the Action column, click
   **Review**.![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_partial_timeoff_review.png)
3. To allocate this time off request in the schedule, add its start time.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_review_partial_timeoff_start.png)
4. Click **Save**.

   The time off is automatically approved.

## Editing the Workday with Zendesk WFM integration settings

After you’ve successfully [connected
the Workday integration with Zendesk WFM](#topic_vrb_ltr_pgc), you can update and edit its settings at
any time.

**To edit the Workday integration with Zendesk WFM settings**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)
   **Apps and integrations** in the sidebar, then select **Integrations >
   Integrations**.
2. Click **Workday** in the list.
3. Select the **Workforce management** tab.
4. Click the name of the connection you want to edit.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_workday_integration_update_required.png)
5. Update the [integration
   settings](#topic_qd2_gqb_qgc).
6. Click **Save**.

## Disconnecting the Workday integration with Zendesk WFM

If you disconnect the Workday integration with Zendesk WFM, data stops syncing
from Workday into WFM. All imported time off entries that showed Workday as the source that
have already occurred will continue to display Workday as the source on the [WFM Time off management page](https://support.zendesk.com/hc/en-us/articles/6443393050394) and the [time off reasons page](https://support.zendesk.com/hc/en-us/articles/6443329403034#h_01HGBQJ9NW4NJ1FBMBV6DJM1N1). All imported time off entries
that showed Workday as the source but are still to occur are changed to show WFM as the
source.

Each time you disconnect and reconnect the integration, a new time off reason is
created.

**To disconnect the Workday integration with Zendesk WFM**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)
   **Apps and integrations** in the sidebar, then select **Integrations >
   Integrations**.
2. Click **Workday**.
3. Select the **Workforce management** tab.
4. Click the name of the connection you want to edit.
5. Click **Actions** and select **Disconnect.**

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_integrations_workday_disconnect.png)
6. Click **Disconnect** to confirm.