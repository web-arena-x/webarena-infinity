# Using Microsoft Excel actions in action flows

Source: https://support.zendesk.com/hc/en-us/articles/9840801141274-Using-Microsoft-Excel-actions-in-action-flows

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

By connecting the [action builder](https://support.zendesk.com/hc/en-us/articles/8855513857306) to external systems, such as Microsoft Excel, admins can integrate Zendesk with external systems in automated workflows, improving collaboration and maintaining a seamless experience across multiple platforms.

Note: The steps associated with external systems in action flows are referred to collectively as *external actions*.

This article contains the following topics:

- [Connecting Microsoft Excel to action builder](#topic_uxz_t1p_zgc)
- [Using Microsoft Excel actions in action flows](#topic_n4d_51p_zgc)
- [Recipe: Using an action flow to maintain a centralized incident log in Excel](#topic_akg_wsq_chc)

## Connecting Microsoft Excel to action builder

Before you can include external actions in your action flows, you must connect the action builder to the external system.

When connecting to external systems for use in action flows, the following best practices are recommended:

- All external actions performed by an action flow are attributed to the user who connected the external system. Therefore, it is a best practice to use a dedicated service account rather than personal credentials when connecting to each external system.
- All integrations request access to necessary scopes. However, it's important that you review and validate the scopes before authorizing the connection to the external system.
- When managing credentials for API key-based tools, such as OpenAI, it's best to store keys in a secure vault or credential manager.

**To connect Microsoft Excel to action builder**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)
   **Apps and integrations** in the sidebar, then select **Actions > Action flows**.
2. [Create](https://support.zendesk.com/hc/en-us/articles/8855601898266) or [edit](https://support.zendesk.com/hc/en-us/articles/9052312956570) an action flow.
3. Open the step sidebar.
4. Under **External actions**, click **Microsoft Excel**.
5. Click **Connect**.
6. Use Microsoft to authenticate the account.

   Depending on your organization's policies, you might need to authorize device or app access.

   Note:
   - All external actions performed by an action flow are attributed to the user who connected the external system. Therefore, it is a best practice to use a dedicated service account rather than personal credentials when connecting to each external system.
   - To ensure the connection is successful, you must have a Microsoft tenant admin add the connector first.

After you've connected to the system, you'll see an indicator that it's connected and details about the instance you're connected to, as well as the actions available for Microsoft Excel.

## Using Microsoft Excel actions in action flows

Microsoft Excel action steps can be used to create and update Excel workbooks and worksheets as well as reading data from them.

The following Excel actions are available:

- [Create workbook](#topic_m51_lbp_zgc)
- [Create worksheet](#topic_evr_pbp_zgc)
- [Add row to sheet](#topic_ezr_rbp_zgc)
- [Fetch row data](#topic_fwt_tbp_zgc)
- [Update row](#topic_t3l_vbp_zgc)

### Creating a new Excel workbook

Use the *Create workbook* action to create a new Excell workbook with a specified name.

This action has the following inputs and outputs:

| | Variables |
| --- | --- |
| Inputs | `workbook_name` |
| Output | `created_date_time`, `http_status_code`, `last_modified_date_time`, `web_url`, `workbook_id`, `workbook_name` |

### Creating a worksheet within a Excel workbook

Use the *Create worksheet* action to create a new worksheet within an existing workbook.

This action has the following inputs and outputs:

| | Variables |
| --- | --- |
| Inputs | `workbook_id`, `worksheet_name` |
| Output | `http_status_code`, `id`, `name`, `position`, `visibility` |

### Adding a row to an Excel worksheet

Use the *Add row to sheet* action to append a new row to an existing worksheet.

This action has the following inputs and outputs:

| | Variables |
| --- | --- |
| Inputs | `workbook_id`, `sheet_name`, `values` |
| Output | `address`, `cell_count`, `column_count`, `column_hidden`, `column_index`, `http_status_code`, `row_count`, `row_hidden`, `row_index`, `values` |

### Fetching data from a row in an Excel worksheet

Use the *Fetch row data* action to retrieve values in a specific row based on a row index.

This action has the following inputs and outputs:

| | Variables |
| --- | --- |
| Inputs | `spreadsheet_id`, `row_index` |
| Output | `row_data` |

### Updating a row in an Excel worksheet

Use the *Update row* action to update values in a specific row based on a row index.

This action has the following inputs and outputs:

| | Variables |
| --- | --- |
| Inputs | `spreadsheet_id`, `header_row` |
| Output | `address`, `cell_count`, `column_count`, `column_hidden`, `column_index`, `http_status_code`, `row_count`, `row_hidden`, `row_index`, `values` |

## Recipe: Using an action flow to maintain a centralized incident log in Excel

The following example action flow adds data to a centralized incident log in Microsoft Excel. Each time a Zendesk ticket is classified as an incident, the action flow automatically adds a new row to the spreadsheet with the full incident details.
This allows the team to automate the tracking of trends, analization of impact, and reporting on incident volume.

Such an action flow would consist of the following steps:

1. Add an action flow trigger with the following details:
   1. Click **Add trigger**.
   2. In the step sidebar, under **Zendesk**, click **Tickets**.
   3. Click **Properties** and select **Ticket type changed**.
   4. Click **Add condition**.
   5. Under **Variable**, select **Ticket type changed** and **Type**.
   6. Set the **Operator** to **Is**.
   7. Under **Value**, enter **Incident**.
2. Add a step to look up ticket details:
   1. In the action builder, beneath the action flow trigger, click the **Add step** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_action_flows_add.png)).
   2. In the step sidebar, under **Zendesk actions**, click **Look up ticket**.
   3. Under **Ticket ID**, click into the field and then click **Select a variable instead**.
   4. Within the variable menu, select **Ticket type changed** as the step that output the variable you want to use, and then select **Ticket ID**.
3. Add a step to look up user details about the ticket requester:
   1. In the action builder, click the **Add step** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_action_flows_add.png)).
   2. In the step sidebar, under **Zendesk actions**, click **Look up user**.
   3. Under **User ID type**, select **Zendesk user ID**.
   4. For **User ID**, click **Add variable**.
   5. Within the variable menu, select **Look up ticket** as the step that outputs the variale you want to use, and then select **Requester ID**.
4. Add a step to lookup details about the ticket requester's organization:
   1. In the action builder, click the **Add step** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_action_flows_add.png)).
   2. In the step sidebar, under **Zendesk actions**, click **Look up organization**.
   3. Under **Organization ID type**, select **Zendesk organization ID**.
   4. For **Organization ID**, click **Add variable**.
   5. Within the variable menu, select **Look up user** as the step that outputs the variale you want to use, and then select **Organization ID**.
5. Add a step that adds a row to an Excel spreadsheet with the information you collected for the ticket, user, and organization:
   1. In the action builder, click the **Add step** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_action_flows_add.png)).
   2. In the step sidebar, under **External actions**, click **Microsoft Excel** and then select **Add row to sheet**.
   3. Select the Excel sheet's **Workbook ID** and **Sheet name**.
   4. Under **Row values**, use variables from the previous steps to capture the details you want about the ticket, user, and organization associated with the incident. Enter the data in the order the columns appear in the sheet, separating each column's value by a comma.

      For example, this might include the ticket's ID, subject, and date created; the ticket requester's name; the organization's name, and more.
6. Click **Save**.
7. Click **Test** to [test the action flow](https://support.zendesk.com/hc/en-us/articles/9052312956570#topic_uyj_qsw_3fc).
8. Click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options-menu-icon-small.png)) and select **Activate** to begin using the action flow to automatically log incident tickets in your Excel spreadsheet.