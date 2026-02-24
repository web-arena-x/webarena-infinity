# Using Google Sheets actions in action flows

Source: https://support.zendesk.com/hc/en-us/articles/9836727346970-Using-Google-Sheets-actions-in-action-flows

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

By connecting the [Action builder](https://support.zendesk.com/hc/en-us/articles/8855513857306) to external systems, such as Google Sheets,
admins can integrate Zendesk with external systems in automated workflows, improving
collaboration and maintaining a seamless experience across multiple platforms.

Note: The
steps associated with external systems in action flows are referred to collectively
as *external actions*.

This article contains the following topics:

- [Connecting Google Sheets to action builder](#topic_fqz_sn4_zgc)
- [Using Google Sheets actions in action flows](#topic_pk2_vn4_zgc)
- [Recipe: Logging new Zendesk tickets in a Google Sheet](#topic_olr_yxv_ghc)

## Connecting Google Sheets to action builder

Before you can include external actions in your action flows, you must connect the
action builder to the external system.

When connecting to external systems for use in action flows, the following best practices are recommended:

- All external actions performed by an action flow are attributed to the user who connected the
  external system. Therefore, it's a best practice to use a dedicated service
  account rather than personal credentials when connecting to each external
  system.
- All integrations request access to necessary scopes. However, it's important that you review and validate the scopes before authorizing the connection to the external system.
- When managing credentials for API key-based tools, such as OpenAI, it's best to store keys in a secure vault or credential manager.

**To connect action builder to Google Sheets**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)
   **Apps and integrations** in the sidebar, then select **Actions > Action
   flows**.
2. [Create](https://support.zendesk.com/hc/en-us/articles/8855601898266) or [edit](https://support.zendesk.com/hc/en-us/articles/9052312956570) an action flow.
3. Open the step sidebar.
4. Under **External actions**, click **Google Sheets**.
5. Click **Connect**.
6. Follow Google's prompts to authenticate and complete the
   connection.

   You'll log into a Google Workspace or Gmail account, and
   admin approval might be required in managed environments.

   Note: All
   external actions performed by an action flow are attributed to the user
   who connected the external system. Therefore, it is a best practice to
   use a dedicated service account rather than personal credentials when
   connecting to each external system.

After you've connected to the system, you'll see an indicator that it's connected and
details about the instance you're connected to, as well as the actions available for
Google Sheets.

## Using Google Sheets actions in action flows

Google Sheets action steps can be used to create spreadsheets and add data, such as
an AI-generated ticket summary, to the sheet, which can then be shared with other
users.

The following Google Sheet actions are available:

- [Create spreadsheet](#topic_lck_r44_zgc)
- [Create a new sheet](#topic_jj3_s44_zgc)
- [Append row](#topic_w21_544_zgc)

### Creating a new Google spreadsheet

Use the *Create spreadsheet* action to create a spreadsheet.

This action has the following inputs and outputs:

|  | Variables |
| --- | --- |
| Inputs | `spreadsheet_title` |
| Output | `spreadsheet_id`, `sheet_title`, |

### Creating a new sheet in a Google spreadsheet

Use the *Create sheet* action to add a sheet to an existing spreadsheet. You
have the option to specify column headings and an initial row of data.

This action has the following inputs and outputs:

|  | Variables |
| --- | --- |
| Inputs | `spreadsheet_id`, `sheet_title` |
| Output | `spreadsheet_id`, `sheet_title` |

### Appending a row to a Google spreadsheet

Use the *Append row* action to add a row to a sheet previously created by
the action flow.

This action has the following inputs and outputs:

|  | Variables |
| --- | --- |
| Inputs | `spreadsheet_id`, `sheet_title`, `values` |
| Output | `spreadsheet_id`, `sheet_title`, `values` |

## Recipe: Logging new Zendesk tickets in a Google Sheet

The following example action flow adds data to a centralized ticket log in Google
Sheets. Each time a Zendesk ticket submitted, the action flow automatically adds a
new row to the spreadsheet with the full details. This allows the team to automate
the tracking of trends, analization of impact, and reporting on volume.

Such an action flow would consist of the following steps:

1. Add an action flow trigger with the following details:
   1. Click **Add trigger**.
   2. In the step sidebar, under **Zendesk**, click
      **Tickets**.
   3. Click **Lifecycle** and select **Ticket created**.
2. Add a step to look up ticket details:
   1. In the action builder, beneath the action flow trigger, click the
      **Add step** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_action_flows_add.png)).
   2. In the step sidebar, under **Zendesk actions**, click **Look up
      ticket**.
   3. Under **Ticket ID**, click into the field and then click
      **Select a variable instead**.
   4. Within the variable menu, select **Ticket created** as the step
      that output the variable you want to use, and then select **Ticket
      ID**.
3. Add a step to look up user details about the ticket requester:
   1. In the action builder, click the **Add step** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_action_flows_add.png)).
   2. In the step sidebar, under **Zendesk actions**, click **Look up
      user**.
   3. Under **User ID type**, select **Zendesk user ID**.
   4. For **User ID**, click **Add variable**.
   5. Within the variable menu, select **Look up ticket** as the step
      that outputs the variale you want to use, and then select
      **Requester ID**.
4. Add a step to lookup details about the ticket requester's organization:
   1. In the action builder, click the **Add step** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_action_flows_add.png)).
   2. In the step sidebar, under **Zendesk actions**, click **Look up
      organization**.
   3. Under **Organization ID type**, select **Zendesk organization
      ID**.
   4. For **Organization ID**, click **Add variable**.
   5. Within the variable menu, select **Look up user** as the step
      that outputs the variale you want to use, and then select
      **Organization ID**.
5. Add a step to look up user details about the ticket assignee:
   1. In the action builder, click the **Add step** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_action_flows_add.png)).
   2. In the step sidebar, under **Zendesk actions**, click **Look up
      user**.
   3. Under **User ID type**, select **Zendesk user ID**.
   4. For **User ID**, click **Add variable**.
   5. Within the variable menu, select **Look up ticket** as the step
      that outputs the variale you want to use, and then select
      **Assignee ID**.
6. Add a step that adds a row to a Google Sheets spreadsheet with the
   information you collected for the ticket, requester, organization, and
   assignee:
   1. In the action builder, click the **Add step** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_action_flows_add.png)).
   2. In the step sidebar, under **External actions**, click **Google
      Sheets** and then select **Append row to sheet**.
   3. Select an existing **Spreadsheet** or click **Create new** and
      enter a **Spreadsheet title**.
   4. Select the **Sheet** to which the row is being added.
   5. Under **Row values**, use variables from the previous steps to
      capture the details you want about the ticket, requester,
      organization, and assignee associated with the ticket. Enter the
      data in the order the columns appear in the sheet, separating each
      column's value by a comma.

      For example, this might include the
      ticket's ID, subject, and date created; the ticket requester's
      name; the organization's name, and more.
7. Click **Save**.
8. Click **Test** to [test the action flow](https://support.zendesk.com/hc/en-us/articles/9052312956570#topic_uyj_qsw_3fc).
9. Click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options-menu-icon-small.png)) and select **Activate** to begin using the
   action flow to automatically log incident tickets in your Google Sheets
   spreadsheet.