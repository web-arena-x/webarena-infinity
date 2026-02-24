# Using Google Drive actions in action flows

Source: https://support.zendesk.com/hc/en-us/articles/10327936440218-Using-Google-Drive-actions-in-action-flows

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

By connecting the [action builder](https://support.zendesk.com/hc/en-us/articles/8855513857306) to external systems, such as Google Drive, admins can integrate Zendesk with external systems in automated workflows, improving collaboration and maintaining a seamless experience across multiple platforms.

Note: The steps associated with external systems in action flows are referred to collectively as *external actions*.

This article contains the following topics:

- [Connecting Google Drive to action builder](#topic_fcs_gtn_g3c)
- [Using Google Drive actions in action flows](#topic_z1q_htn_g3c)
- [Recipe: Looking up the sales playbook in Google Drive when a Zendesk ticket is identified as a lead](#topic_y2s_4sn_g3c)

## Connecting Google Drive to action builder

Before you can include external actions in your action flows, you must connect the action builder to the external system.

When connecting to external systems for use in action flows, the following best practices are recommended:

- All external actions performed by an action flow are attributed to the user who connected the external system. Therefore, it's a best practice to use a dedicated service account rather than personal credentials when connecting to each external system.
- All integrations request access to necessary scopes. However, it's important that you review and validate the scopes before authorizing the connection to the external system.
- When managing credentials for API key-based tools, such as OpenAI, it's best to store keys in a secure vault or credential manager.

**To connect action builder to Google Drive**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)
   **Apps and integrations** in the sidebar, then select **Actions > Action flows**.
2. [Create](https://support.zendesk.com/hc/en-us/articles/8855601898266) or [edit](https://support.zendesk.com/hc/en-us/articles/9052312956570) an action flow.
3. Open the step sidebar.
4. Under **External actions**, click **Google Drive**.
5. Click **Connect**.
6. Follow Gmail's prompts to authenticate and complete the connection.

   You'll log into a Google Workspace or Google Drive account, and admin approval might be required in managed environments.

   The following scope is required for the account you authenticate with:
   `https://www.googleapis.com/auth/drive.file`.

   Note: All external actions performed by an action flow are attributed to the user who connected the external system. Therefore, it is a best practice to use a dedicated service account rather than personal credentials when connecting to each external system.

After you've connected to the system, you'll see an indicator that it's connected and details about the instance you're connected to, as well as the actions available for Google Drive.

## Using Google Drive actions in action flows

Google Drive action steps can be used to send new emails.

The following Google Drive actions are available:

- [Search file](#topic_fy1_1wn_g3c)
- [Search folder](#topic_vt4_j1r_33c)
- [Create folder](#topic_u1t_v1r_33c)
- [Create file](#topic_pp3_cbr_33c)

### Searching for files in Google Drive

Use the *Search file* action to find a file based on the file's name and other file metadata.

This action has the following inputs and outputs:

| | Variables |
| --- | --- |
| Inputs | Required: `File name` Optional: `Match type`, `Additional filters`, `Parent folder ID`, `File type` |
| Output | File metadata, including `original file name`, `ID`, `Owner`, `type`, and `Modified timestamp` |

### Searching for folders in Google Drive

Use the *Search folder* action to find a folder based on the folder's name and other metadata.

This action has the following inputs and outputs:

| | Variables |
| --- | --- |
| Inputs | Required: `File name` Optional: `Match type`, `Additional filters`, `Parent folder ID` |
| Output | File metadata, including `original file name`, `ID`, `Owner`, `type`, and `Modified timestamp` |

### Creating a folder in Google Drive

Use the *Create folder* action to create a new folder in Google Drive.

This action has the following inputs and outputs:

| | Variables |
| --- | --- |
| Inputs | Required: `Folder name` Optional: `Parent folder ID` |
| Output | File metadata |

### Creating a file in Google Drive

Use the *Create file* action to create a file in Google Drive.

This action has the following inputs and outputs:

| | Variables |
| --- | --- |
| Inputs | Required: `File name`, `File content` Optional: `File type`, `Parent folder ID` |
| Output | File metadata |

## Recipe: Looking up the sales playbook in Google Drive when a Zendesk ticket is identified as a lead

The following example action flow uses ticket tags added by agents to automatically look up the appropriate sales playbook file in Google Drive and send a link to it to the Sales team when a ticket is identified as a lead.

Such an action flow would consist of the following steps:

1. Add an action flow trigger with the following details:
   1. Click **Add trigger**.
   2. In the step sidebar, under **Zendesk**, click **Tickets**.
   3. Click **Lifecycle** and select **Ticket is tagged**.
   4. Click **Add condition**.
   5. Under **Variable**, click **Ticket tags changed** and select **Tags (added)**.
   6. Set the **Operator** to **Contains at least 1 of**.
   7. Under **Value**, enter **sales\_lead**.
2. Add a step to look up ticket details:
   1. In the action builder, beneath the action flow trigger, click the **Add step** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_action_flows_add.png)).
   2. In the step sidebar, under **Zendesk actions**, click **Look up ticket**.
   3. Under **Ticket ID**, click into the field and then click **Select a variable instead**.
   4. Within the variable menu, select **Ticket is tagged** as the step that output the variable you want to use, and then select **Ticket ID**.
3. Add a step to look up user details about the ticket requester:
   1. In the action builder, click the **Add step** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_action_flows_add.png)).
   2. In the step sidebar, under **Zendesk actions**, click **Look up user**.
   3. Under **User ID type**, select **Zendesk user ID**.
   4. For **User ID**, click **Add variable**.
   5. Within the variable menu, select **Look up ticket** as the step that outputs the variable you want to use, and then select **Requester ID**.
4. Add a step to lookup details about the ticket requester's organization:
   1. In the action builder, click the **Add step** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_action_flows_add.png)).
   2. In the step sidebar, under **Zendesk actions**, click **Look up organization**.
   3. Under **Organization ID type**, select **Zendesk organization ID**.
   4. For **Organization ID**, click **Add variable**.
   5. Within the variable menu, select **Look up user** as the step that outputs the variable you want to use, and then select **Organization ID**.
5. Add a step that searches Google Drive for the relevant sales playbook file:
   1. In the action builder, click the **Add step** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_action_flows_add.png)).
   2. In the step sidebar, under **External actions**, click **Search file**.
   3. Under **File name**, enter **sales\_playbook\_`location`\_.pdf**, where **`location`** is a variable:

      Click **Add variable**. Within the variable menu, select **Look up ticket** as the step that outputs the variable you want to use, and then select **Location**.
6. Add a step that sends an email based on the information you collected for the ticket, user, and organization:
   1. In the action builder, click the **Add step** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_action_flows_add.png)).
   2. In the step sidebar, under **External actions**, click **Gmail** and then select **Send email**.
   3. Under **Recipient's email**, enter the Inside sales team distribution list. For example, **sales@yourcompany.com**.
   4. Under **Subject**, enter **Ticket *Ticket ID* Identified as Lead**, where *Ticket ID* is a variable.

      Click **Add variable**, select **Look up ticket**, and select **Ticket ID**, to insert the *Ticket ID* variable into the subject.
   5. Under **Body**, enter the message you want to send to the Inside sales team for new prospects. Include relevant ticket and user information as variables from the Look up ticket and Look up user steps, respectively, to streamline their ability to follow up. In the following example, all variables are italicized:

      ```
      Hi Sales Team,

      Ticket Ticket ID has been identified as a lead. Can you please follow up with User Name as soon as possible?

      User contact information:
      - Email: User Email
      - Phone: User Phone
      - Locale and timezone: User Locale - User IANA timezone
      - Sales playbook: file link

      Here's more context on the ticket:
      - Ticket subject: Ticket Subject
      - Ticket description: Ticket Description
      - Last ticket update: Ticket's Latest agent update
      ```
7. Click **Save**.
8. Click **Test** to [test the action flow](https://support.zendesk.com/hc/en-us/articles/9052312956570#topic_uyj_qsw_3fc).
9. Click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options-menu-icon-small.png)) and select **Activate** to begin automatically emailing links to the appropriate sales playbook when Zendesk tickets are identified as sales leads.