# Using Microsoft Outlook actions in action flows

Source: https://support.zendesk.com/hc/en-us/articles/9840940606106-Using-Microsoft-Outlook-actions-in-action-flows

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

By connecting the [action builder](https://support.zendesk.com/hc/en-us/articles/8855513857306)
to external systems, such as Microsoft Outlook, admins can integrate Zendesk with external systems in automated workflows, improving collaboration and maintaining a seamless experience across multiple platforms.

Note: The steps associated with external systems in action flows are referred to collectively as *external actions*.

This article contains the following topics:

- [Connecting Microsoft Outlook to action builder](#topic_fwh_xdw_zgc)
- [Using Microsoft Outlook actions in action flows](#topic_agq_f2w_zgc)
- [Recipe: Email Sales team when a ticket is identified as a new prospect opportunity](#topic_ng5_q5v_2hc)

## Connecting Microsoft Outlook to action builder

Before you can include external actions in your action flows, you must connect the action builder to the external system.

When connecting to external systems for use in action flows, the following best practices are recommended:

- All external actions performed by an action flow are attributed to the user who connected the external system. Therefore, it's a best practice to use a dedicated service account rather than personal credentials when connecting to each external system.
- All integrations request access to necessary scopes. However, it's important that you review and validate the scopes before authorizing the connection to the external system.
- When managing credentials for API key-based tools, such as OpenAI, it's best to store keys in a secure vault or credential manager.

**To connect Microsoft Outlook to action builder**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)
   **Apps and integrations** in the sidebar, then select **Actions > Action flows**.
2. [Create](https://support.zendesk.com/hc/en-us/articles/8855601898266)
   or [edit](https://support.zendesk.com/hc/en-us/articles/9052312956570)
   an action flow.
3. Open the step sidebar.
4. Under **External actions**, click **Microsoft Outlook**.
5. Click **Connect**.
6. Use Microsoft to authenticate the account.

   Ensure the account used for authentication has the necessary permissions to send and read emails.
   The following scopes are required:
   `Mail.Send` and `Mail.Read`, `Mail.ReadWrite`.

   Note: All external actions performed by an action flow are attributed to the user who connected the external system. Therefore, it is a best practice to use a dedicated service account rather than personal credentials when connecting to each external system.

After you've connected to the system, you'll see an indicator that it's connected and details about the instance you're connected to, as well as the actions available for Microsoft Outlook.

## Using Microsoft Outlook actions in action flows

Microsoft Outlook action steps can be used to send, reply to, forward, and search for emails in Microsoft Outlook. These steps use the [Microsoft Graph API](https://learn.microsoft.com/en-us/graph/use-the-api)
to provide secure and reliable email automation, streamlining communication, reducing manual email handling, and improving response times.

The following Outlook actions are available:

- [Search for email](#topic_i4f_n2w_zgc)
- [Forward email](#topic_xql_r2w_zgc)
- [Reply to email](#topic_owv_33w_zgc)
- [Send email](#topic_ddg_q3w_zgc)

### Searching for an email

Use the *Search for email* action to retrieve an email based on the email's subject or sender details for further use in the action flow.

This action has the following inputs and outputs:

| | Variables |
| --- | --- |
| Inputs | `sender's email`, `subject` |
| Output | `body`, `categories`, `change_key`, `conversation_id`, `conversation_index`, `created_datetime`, `from_address`, `from_name`, `has_attachments`, `id`, `internet_message_id`, `is_delivery_receipt_requested`, `is_draft`, `is_read`, `is_read_receipt_requested`, `last_modified_datetime`, `parent_folder_id`, `received_datetime`, `replyTo_address`, `replyTo_name`, `sent_datetime`, `subject`, `web_link` |

### Fowarding an email

Use the *Forward email* action to forward an existing email to a specified recipient.

This action has the following inputs and outputs:

| | Variables |
| --- | --- |
| Inputs | `email ID` (identifying the message you're forwarding), `recipient emails`, `comment` |
| Output | none |

### Replying to an email

Use the *Reply to email* action to send a reply to an existing email using the email ID.

This action has the following inputs and outputs:

| | Variables |
| --- | --- |
| Inputs | `email ID` (identifying the message you're replying to), `comment`, `additional recipients`, `CC emails`, `BCC emails` |
| Output | none |

### Sending an email

Use the *Send email* action to send a new email to a specified recipient with the defined subject and body.

This action has the following inputs and outputs:

| | Variables |
| --- | --- |
| Inputs | `recipient's email`, `subject`, `body`, `type`, `CC emails`, `BCC emails`, `save to sent items` |
| Output | none |

## Recipe: Email Sales team when a ticket is identified as a new prospect opportunity

The following example action flow automatically sends an email to the Sales team through Microsoft Outlook when a Zendesk ticket is determined to be a new prospect opportunity. This ensures prompt follow-up by the Sales team, who doesn't work directly with Zendesk tickets.

Such an action flow would consist of the following steps:

1. Add an action flow trigger with the following details:
   1. Click **Add trigger**.
   2. In the step sidebar, under **Zendesk**, click **Tickets**.
   3. Click **Properties** and select **Ticket tags changed**.
   4. Click **Add condition**.
   5. Under **Variable**, click **Ticket tags changed** and select **Tags (added)**.
   6. Set the **Operator** to **Contains at least 1 of**.
   7. Under **Value**, enter **sales\_prospect**.
2. Add a step to look up ticket details:
   1. In the action builder, beneath the action flow trigger, click the **Add step** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_action_flows_add.png)).
   2. In the step sidebar, under **Zendesk actions**, click **Look up ticket**.
   3. Under **Ticket ID**, click into the field and then click **Select a variable instead**.
   4. Within the variable menu, select **Ticket tags changed** as the step that output the variable you want to use, and then select **Ticket ID**.
3. Add a step to look up user details about the ticket assignee:
   1. In the action builder, click the **Add step** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_action_flows_add.png)).
   2. In the step sidebar, under **Zendesk actions**, click **Look up user**.
   3. Under **User ID type**, select **Zendesk user ID**.
   4. For **User ID**, click **Add variable**.
   5. Within the variable menu, select **Look up ticket** as the step that outputs the variable you want to use, and then select **Requester ID**.
4. Add a step that sends an email based on the information you collected for the ticket, assignee, and organization:
   1. In the action builder, click the **Add step** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_action_flows_add.png)).
   2. In the step sidebar, under **External actions**, click **Microsoft Outlook** and then select **Send email**.
   3. Under **Recipient's email**, enter the Sales team distribution list. For example, **sales@yourcompany.com**.
   4. Under **Subject**, enter **Ticket *Ticket ID* Identified as New Prospect**, where *Ticket ID* is a variable.

      Click **Add variable**, select **Look up ticket**, and select **Ticket ID**, to insert the *Ticket ID* variable into the subject.
   5. Under **Body**, enter the message you want to send to the Sales team for new prospects. Include relevant ticket and user information as variables from the Look up ticket and Look up user steps, respectively, to streamline their ability to follow up.
      In the following example, all variables are italicized:

      ```
      Hi Sales Team,

      Ticket Ticket ID has been identified as a new prospect. Can you please follow up with User Name as soon as possible?

      User contact information:
      - Email: User Email
      - Phone: User Phone
      - Locale and timezone: User Locale - User IANA timezone
      - Notes: User Notes

      Here's more context on the ticket:
      - Ticket subject: Ticket Subject
      - Ticket description: Ticket Description
      - Last ticket update: Ticket's Latest agent update
      ```
5. Click **Save**.
6. Click **Test** to [test the action flow](https://support.zendesk.com/hc/en-us/articles/9052312956570#topic_uyj_qsw_3fc).
7. Click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options-menu-icon-small.png))
   and select **Activate** to begin using the action flow to automatically send an email to the Sales team when a ticket is identified and tagged as a new sales prospect.