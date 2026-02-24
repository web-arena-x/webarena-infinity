# Setting up the Zendesk Support for Jira integration (Legacy)

Source: https://support.zendesk.com/hc/en-us/articles/4408837969946-Setting-up-the-Zendesk-Support-for-Jira-integration-Legacy

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Verified AI summary ◀▼

Integrate Support with Jira to link or create Jira issues from tickets, track progress, and enhance collaboration between product and support teams. Ensure admin permissions in both platforms, configure custom fields, and manage access. Use a dedicated integration user for escalations, and reinstall if needed to maintain connections. This setup supports Jira Cloud and Data Center, excluding Jira Server and mobile apps.

The Zendesk Support for Jira integration encourages collaboration between product and support teams. For example, agents can link or create new Jira issues from a Zendesk ticket. They can then use the link to track the progress made by the product team on addressing the issue.

The integration supports Atlassian Jira Cloud and Jira Data Center. It is not supported on the Jira Cloud mobile app. If you've installed this integration on Jira Server, it will continue to function, but you can no longer receive support for this configuration, as Atlassian has [ended support for Jira Server](https://www.atlassian.com/licensing/server-end-of-support).

This article covers the following topics:

- [Installation requirements](#topic_zkr_sr3_wn)
- [Jira custom field type compatibility](#topic_jtn_k5c_wxb)
- [Installing and configuring the integration](#topic_shw_xdd_qn)
- [Restricting access to the Jira app in Zendesk Support](#topic_k24_dqr_ymb)
- [Adding fields to the Jira issue creation form in Zendesk Support](#topic_mgd_rj4_qz)
- [Using the dedicated integration user option](#topic_mm1_3t3_scb)
- [Reinstalling the integration](#topic_dsy_fys_5pb)

Related topics:

- [Using the Zendesk Support for Jira integration](https://support.zendesk.com/hc/en-us/articles/4408827996058)
- [Restricting access to projects in your Jira integration](https://support.zendesk.com/hc/en-us/articles/4408839373850)
- [Updating a ticket when the status of a Jira issue changes](https://support.zendesk.com/hc/en-us/articles/4408832025114)

## Installation requirements

You must have administrator permissions in both Jira and Zendesk Support to set up the integration.

Additionally, you must meet the following requirements:

- Be a member of the **jira-administrators** and **jira-software-users** groups.
- Have no permission schemes that prevent you from creating or updating projects.
- The **reporter** field is on the **Create Issue** screen for the respective projects.
- **Atlassian add-ons have permission to access your Jira projects**. This is enabled by default. To verify this, check the **Project Permissions** page for each project in Jira. The various project actions should have a Project Role called `Project Role (atlassian-addons-project-access)`.
- **Third-party cookies are enabled**. However, if third-party cookies need to remain disabled on your system, add `jiraplugin.zendesk.com` as well as your Jira subdomain to the list of content exceptions.

## Jira custom field type compatibility

The Zendesk Support for Jira integration enables you to create a Jira issue from a ticket using the Jira app in Zendesk Support, located in the sidebar of the agent interface. The form used to create Jira issues includes default fields, but Zendesk Support admins can add custom Jira fields to this form.

See [Using the Jira field syncing feature](https://support.zendesk.com/hc/en-us/articles/4408825394458) for a list of the Jira custom field types compatible with the Jira app in Zendesk Support. You can [add compatible field types to the Jira issue creation form](#topic_mgd_rj4_qz). You can also [add compatible field types to views of linked Jira issues](https://support.zendesk.com/hc/en-us/articles/4408827996058-Using-the-Zendesk-Support-for-Jira-integration#topic_frt_jyr_zm).

## Installing and configuring the integration

Note: Before you start the installation, make sure you meet all the [installation requirements](#topic_zkr_sr3_wn), including having third-party cookies enabled.

The integration setup process involves installing the Zendesk Support for Jira app in Atlassian Marketplace from your Jira account, then configuring the app.

**To install and configure the integration**

1. In Jira, click **Apps** in the top navigation bar, then select **Explore more apps**.
2. On the **Marketplace apps** page, search for **Zendesk**.
3. Locate and click the **Zendesk Support for Jira** entry in the search results.
4. Click **Get app**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/install_jira_entry.png)
5. Click **Get it now**.
6. When the installation success notification modal appears, click **Configure**.
7. Enter your Zendesk subdomain. By default, the **Create a new dedicated Zendesk user for this integration** checkbox is selected. We recommend using this feature to allow all escalations from Jira to Zendesk Support to not come from the admin who set up the integration, but from the dedicated user. This automatically creates a new admin user in your Zendesk account that is only used by the Jira integration. For more information, see [Using the dedicated integration user option](#topic_mm1_3t3_scb).
8. Click **Authenticate**.
9. Click **Allow**.
10. A second browser page opens, requesting you to sign in to your Zendesk account. Enter your login credentials. The page will close.
11. On the app's settings page, select the details to display in linked Jira issues.

    ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/jira_v4_update.png)
12. Click **Save**.

In Jira Cloud, the integration creates a free admin user called Zendesk Support for Jira.
You can change the avatar of the user on the Profile page.

You can check the integration works by confirming that the Zendesk Support for Jira user appears in a user drop-down field in Jira.

## Restricting access to the Jira app in Zendesk Support

If you want to control who has access to the app in Zendesk Support, for example, admins or agents only, you can make the change in Zendesk.

**To restrict access to the Jira app in Zendesk Support**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)
   **Apps and integrations** in the sidebar, then select **Apps > Zendesk Support apps**.
2. Under the Currently Installed tab, click the **JIRA** app.
3. Under Installation, select the **Enable role restrictions?** checkbox to restrict access to the app to specific roles, then select the roles.
4. Select the **Enable group restrictions?** checkbox to restrict access to the app to specific groups, then select the groups.
5. Click **Update** to save and apply the changes.

Your teams can now start collaborating using Zendesk and Jira. See [Using the Zendesk Support for Jira integration](https://support.zendesk.com/hc/en-us/articles/4408827996058).

## Adding fields to the Jira issue creation form in Zendesk Support

When [creating a Jira issue from a Zendesk Support ticket](https://support.zendesk.com/hc/en-us/articles/4408827996058#topic_fwb_hwc_zm), you're asked to enter details about the issue being reported in the **Create a new Jira issue** form:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/jira_issue_form_blank.png)

This form includes several default fields:

- Project
- Issue type
- Reporter
- Assignee
- Summary
- Description

These default fields can't be removed and are specific to the selected Jira project and issue type.

Zendesk Support admins can add pre-existing or custom Jira fields to this form. Adding fields to the issue creation form makes them visible to all agents when creating issues for the selected project and issue type.

See [Using the Jira field syncing feature](https://support.zendesk.com/hc/en-us/articles/4408825394458) for a list of the Jira custom field types compatible with the Jira app in Zendesk support.

**To add fields to the Jira issue creation form**

1. In Zendesk Support, go to the ticket you want to use as a basis for a new Jira issue.
2. Click **Create Issue** in the Jira app next to the ticket.
3. In the **Project** field, select the project.

   The **Configure fields** button appears after you select a project. This button is visible only to Zendesk Support admins.
4. Select the **Issue type**.
5. Click **Configure fields**.

   A drop-down list of available fields displays.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/jira_issue_form_configure_fields.png)
6. Select the fields to add to the Jira issue creation form.

   These fields will be visible to all agents when creating issues for this project and issue type.
7. Finish creating the issue, as described in [Creating a Jira issue from a ticket](https://support.zendesk.com/hc/en-us/articles/4408827996058#topic_fwb_hwc_zm).
8. Click **Create issue**.

## Using the dedicated integration user option

If you choose to create a dedicated integration user in your Zendesk Support account, a new, verified admin user (`Jira Integration`) is automatically created, along with an email address (`jira_integration_XXXXXX@jira.zendesk-integrations.com`). This user account is fully managed by the integration and will be suspended if the integration is removed.

Note:

- The dedicated integration user option requires an available agent seat. While in use, that seat will not be available for other agents.
- The admin account who installed the Jira integration and the dedicated integration user must always have admin rights and be active for the integration to function. If you suspend or downgrade the admin account or the dedicated integration user, the integration will not function.

After the authentication and creation processes are completed, the integration service is ready to use. All the commenting and field sync actions will be performed as if they’re done by the dedicated integration user.

If you decide to stop using the dedicated integration user, you can disconnect the integration from the Jira side. When disconnected, Jira will stop using the dedicated integration user. The dedicated integration user in the Zendesk Support account will be downgraded to an end user and suspended. Uninstalling the plugin will also downgrade and suspend the user.

**To disconnect the dedicated integration user**

1. In Jira, click **Settings**, then go to **Apps > Manage apps**.
2. Click to expand the **Zendesk Support for JIRA** app, then click **Configure**.
3. Click **Disconnect** to disconnect your subdomain.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/jira3_disconnect_zd.png)
4. Re-enter your subdomain, and **deselect the option to create a dedicated integration user**.
5. Click **Authenticate** to re-authenticate your subdomain.

## Reinstalling the integration

Reinstalling the integration is usually required in the following situations:

- Changing the integration user
- Changing the Jira instance linked to your Zendesk Support account
- Changing the Zendesk Support instance linked to your Jira instance (including sandboxes)
- Reestablish your connection between Zendesk and Jira after clearing the plugin cache

If you are reintegrating the same Zendesk and Jira accounts, your linked issue data remains intact.

**To reinstall the integration**

1. In Jira, navigate to **Apps** > **Manage your apps**.
2. Click **Zendesk Support for JIRA**, then select **Configure**.
3. Click **Disconnect**.
4. Go back to the Manage your apps page, click **Zendesk Support for JIRA**, then click **Uninstall**.
5. Complete the setup process. See [Installing and configuring the integration](#topic_shw_xdd_qn).