# Setting up the Zendesk agent for Microsoft 365 Copilot

Source: https://support.zendesk.com/hc/en-us/articles/9958422946842-Setting-up-the-Zendesk-agent-for-Microsoft-365-Copilot

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Verified AI summary ◀▼

Integrate Microsoft 365 Copilot to allow users to access support directly within Microsoft apps like Teams and Outlook. Users can search help center articles, create and manage tickets, and track their progress. Admins must connect their Microsoft account, enable user access, and can disconnect when needed. Ensure admin roles remain active for continuous integration functionality.

The Zendesk agent for Microsoft 365 Copilot helps users get support directly within
Microsoft apps such as Teams and Outlook.

With this integration, your users can do the following within Microsoft 365 apps:

- Search help center articles
- Create Zendesk tickets
- Add public ticket comments
- Resolve tickets created by them
- View the tickets they created to keep track of progress

This article walks you through how to set up the Zendesk agent so it's available to your
users working in Microsoft. For more information on Copilot, see the [Microsoft 365 Copilot documentation](https://learn.microsoft.com/en-us/copilot/microsoft-365/).

This article includes the following topics:

- [Considerations](#topic_acv_grl_fhc)
- [Connecting your Microsoft account](#topic_tfz_mrl_fhc)
- [Allowing users to install the Zendesk agent](#topic_fvp_bdd_jhc)
- [Disconnecting your Microsoft account](#topic_gtt_rxl_fhc)

## Considerations

- You must be an admin in both Microsoft 365 and Zendesk Support to set up the
  integration.
- If the Zendesk admin who connected the integration has their role downgraded,
  the integration will cease to function. It will require the integration to be
  disconnected, then reconnected in Admin Center by another Zendesk admin.

## Connecting your Microsoft account

Set up and configure your integration in Admin Center.

Multiple connections are supported. Repeat these steps for each Microsoft account
you’d like to connect to Zendesk.

**To connect your Microsoft account to Zendesk**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)
   **Apps and integrations** in the sidebar, then select **Integrations >
   Integrations**.
2. On the Integrations page, click **Microsoft Copilot**.
3. Select **I agree to the Built by Zendesk Terms of Use**.
4. Click **Connect**.
5. Click the Microsoft account you'd like to connect.

   You must be an
   administrator of this account to connect the integration.

   You are
   directed back to Admin Center. The new connection displays in the
   Copilot connections list with all features active.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/copilot_int_connections.png)
6. Click the name of the connection to access connection settings.
7. To deactivate a feature, clear the check box next to its name.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/copilot_int_settings.png)

   See [Using the Zendesk agent in Microsoft
   365 Copilot](https://support.zendesk.com/hc/en-us/articles/9958331458458) for more information about each of these
   features.
8. Click **Save**.

## Allowing users to install the Zendesk agent

After you've connected your Microsoft account to Zendesk, you must make the Zendesk
agent available to your end users in Microsoft 365. For more information, see the
[Microsoft 365 admin center
documentation](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/manage-copilot-agents-integrated-apps).

To allow users to install the Zendesk agent

1. Sign in to the Microsoft 365 admin center.
2. Go to **Copilot** > **Agents**.
3. Search for **Zendesk Agent**, then click on it to open settings.
4. For Assign users, select which users at your company can install and use the
   Zendesk agent.
5. Click **Update**.

## Disconnecting your Microsoft account

You can disconnect your Microsoft account from Zendesk in Admin Center. After it's
disconnected, Microsoft users can no longer access the Zendesk agent in Copilot.

**To disconnect a Microsoft account**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)
   **Apps and integrations** in the sidebar, then select **Integrations >
   Integrations**.
2. On the Integrations page, click **Microsoft Copilot**.
3. Click the options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options-menu-icon-small.png)) next to the Microsoft account you want to
   disconnect, then click **Disconnect**.