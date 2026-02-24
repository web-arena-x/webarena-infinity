# Configuring the Jira app for Zendesk Support

Source: https://support.zendesk.com/hc/en-us/articles/9810169980058-Configuring-the-Jira-app-for-Zendesk-Support

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Verified AI summary ◀▼

Configure the Jira app to create and view linked issues from tickets. Customize project access, add or remove fields in the sidebar, and adjust the issue creation form. Manage attachments, linked issues, and automation settings. Temporarily disable the app during setup without disconnecting accounts. This integration does not support Jira Data Center or Server.

As described in [Using the Jira integration for Zendesk](https://support.zendesk.com/hc/en-us/articles/9827173048858), the Jira app for Zendesk Support allows agents to create and view linked Jira issues from a ticket in Zendesk. The app is available to agents in Zendesk after you've [connected your Jira instance to Zendesk](https://support.zendesk.com/hc/en-us/articles/9797104268058).

Admins can configure the app to customize and enhance the integration to suit their company's needs. The app can also be turned on or off to support flexible management during setup.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/jira_v2_sidebar_config_large.png)

Note: This integration doesn't support Jira Data Center and Jira Server, as Atlassian is planning to discontinue these platforms. See Atlassian's announcements for [Jira Data Center](https://www.atlassian.com/migration) and [Jira Server](https://www.atlassian.com/licensing/server-end-of-support#serv-end-of-support).

This article contains the following topics:

- [Including Jira projects](#topic_gdb_dl3_xgc)
- [Adding and removing Jira fields from the app sidebar](#topic_emy_hd3_xgc)
- [Adding Jira fields to the issue creation form](#topic_mgd_rj4_qz)
- [Configuring attachments, linked issues, and automation](#topic_k2v_qc1_b3c)
- [Turning off the app](#topic_ulg_wc3_xgc)

## Including Jira projects

Zendesk admins can configure the Jira app to include specific projects, so that when an agent tries to create or link a Jira issue, only those projects will be available. This feature is particularly useful if you'd only like to permit ticket creation for certain projects.

**To include Jira projects in the app**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)
   **Apps and integrations** in the sidebar, then select **Integrations >
   Integrations**.
2. Click the **Jira** link.
3. If you have multiple connections, click the name of the connection you are setting up.
4. On the Support app tab, select which projects to allow ticket creation in the **Allowed projects** field.

   If you'd rather select only the projects to exclude, select those projects in the **Restricted projects** field. This option is useful if you only need to exclude a small number of projects, such as internal projects.

   You can only use one option at a time:
   **Allowed projects** or **Restricted projects**. These fields cannot be used together. If you're looking for a specific project that isn't immediately visible in the drop-down list, you can start typing its name to find it quickly.
5. Click **Save**.

## Adding and removing Jira fields from the app sidebar

With a ticket open in Zendesk, users can access the Jira app in the right sidebar. If the app is not displayed on the right side of the Agent Workspace, agents can click the Apps icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_omnipanel_apps.png)) in the [context panel](https://support.zendesk.com/hc/en-us/articles/4408836526362) to open it.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/jira_v2_app_sidebar.png)

Zendesk admins can customize the app to display the Jira fields most relevant to agents handling tickets. This configuration process involves adding the desired Jira fields to the app and organizing them within the Summary and Details sections of the sidebar.

**To add Jira fields to the app sidebar**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)
   **Apps and integrations** in the sidebar, then select **Integrations >
   Integrations**.
2. Click the **Jira** link.
3. If you have multiple connections, click the name of the connection you're setting up.
4. In the Manage issue section, select the field you'd like to add in the **Select field** menu, then click **Add field**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/jira_v2_app_sidebar_fields_3.png)
5. Select where to display the field in the sidebar: the **Summary** and/or **Details** section.

   If a field is selected but grayed out, it means that the field is already added to the section by default and can't be removed.
6. To reorder fields in the sidebar, click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/salesforce_grabber_icon.png) and drag them to the desired location. The order represented in the configuration determines the order in which fields are displayed in the sidebar.
7. Click **Save**.

The preview pane displays how the added field will appear to agents. Use the preview to determine whether objects need to be adjusted or reordered.

**To remove Jira fields from the app sidebar**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)
   **Apps and integrations** in the sidebar, then select **Integrations >
   Integrations**.
2. Click the **Jira** link.
3. If you have multiple connections, click the name of the connection you're setting up.
4. In the Manage issue section, click the **X** icon next to the fields to remove.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/jira_v2_remove_app_field.png)

   If a field is selected but grayed out, it means that the field can't be removed.
5. Click **Save**.

## Adding Jira fields to the issue creation form

When [creating a Jira issue](https://support.zendesk.com/hc/en-us/articles/9827173048858#topic_fwb_hwc_zm) from a Zendesk Support ticket, agents are asked to enter details about the issue being reported in the Create issue form.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/jira_v2_create_issue_blank.png)

The empty Create issue form includes the following fields:

- Project
- Work type
- Summary
- Description

These default fields can't be removed. Zendesk Support admins can add pre-existing or custom Jira fields to this form. Adding fields to the issue creation form makes them visible to all agents when creating issues for the selected project and work type.

Fields marked as mandatory for a selected project and issue type in Jira will always appear by default in the Zendesk sidebar app. These fields are set by Jira and are not configurable in Admin Center. Admins can't remove or reorder these fields within Zendesk.

**To add fields to the Create issue form**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)
   **Apps and integrations** in the sidebar, then select **Integrations >
   Integrations**.
2. Click the **Jira** link.
3. If you have multiple connections, click the name of the connection you are setting up.
4. On the Support app tab, scroll down to the Create issue fields section and click **Configure**.
5. Click **Add project**.
6. In the Select project field, select the project for which you'd like to configure fields.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/jira_v2_configure_fields_select_project.png)
7. Expand the issue type for which you'd like to add fields to the issue creation form.
8. Use the **Select field** menu to add fields to the form:
   1. Select a field in the dropdown menu.
   2. To make the field required on the Create issue form, select **Is Required?**.
   3. Click **Add field**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/jira_v2_configure_add_field_3.png)
9. To reorder fields on the form, click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/salesforce_grabber_icon.png) and drag them to the desired location. The order represented in the configuration determines the order in which fields are displayed on the form.
10. Click **Add**.

## Configuring attachments, linked issues, and automation

**To configure attachments, linked issues, and automation**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)
   **Apps and integrations** in the sidebar, then select **Integrations >
   Integrations**.
2. Click the **Jira** link.
3. If you have multiple connections, click the name of the connection for which you'd like to turn off the app.
4. On the Support app tab, scroll to the bottom of the page and turn the following features on or off:
   - **Allow issue creation** allows Zendesk users to [create Jira issues from tickets](https://support.zendesk.com/hc/en-us/articles/9827173048858#topic_fwb_hwc_zm).
   - **Attachments management in linked issue details** allows users to manage attachments within linked Jira issues.
   - **Automatically add agent as watcher when linking Jira issues**
   - **Allow search for closed issues**
   - **[Turn on linked ticket reporting in Jira](https://support.zendesk.com/hc/en-us/articles/10042720591898)**
   - **Manage links** allows API users to [create and update integration links](https://developer.zendesk.com/api-reference/ticketing/jira_v2/jira_integration_links/) via the API.
   - **Update ticket status or comments** allows API users to [sync the status of Zendesk tickets with the status of linked issues in Jira](https://support.zendesk.com/hc/en-us/articles/10055291434394) via the API.
5. Click **Save**.

## Turning off the app

After [connecting your Jira instance to Zendesk](https://support.zendesk.com/hc/en-us/articles/9797104268058), the Jira app is visible to agents in Zendesk by default. You can temporarily hide the app from agents by turning it off. For example, you may want to turn it off while you're configuring it.

Turning the app off doesn't disconnect your accounts. However, agents can't create or link issues.

**To turn off the Jira app**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)
   **Apps and integrations** in the sidebar, then select **Integrations >
   Integrations**.
2. Click the **Jira** link.
3. If you have multiple connections, click the name of the connection for which you'd like to turn off the app.
4. On the Support app tab, deselect the **Turn on Jira app for Zendesk Support** checkbox.

   When you're ready to turn the app back on, select the checkbox.
5. Click **Save**.