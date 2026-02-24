# Using Gmail action in action flows

Source: https://support.zendesk.com/hc/en-us/articles/10327942889242-Using-Gmail-action-in-action-flows

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

By connecting the [action builder](https://support.zendesk.com/hc/en-us/articles/8855513857306) to external systems, such as Gmail, admins
can integrate Zendesk with external systems in automated workflows, improving
collaboration and maintaining a seamless experience across multiple platforms.

Note: The
steps associated with external systems in action flows are referred to collectively
as *external actions*.

This article contains the following topics:

- [Connecting Gmail to action builder](#topic_fcs_gtn_g3c)
- [Using Gmail actions in action flows](#topic_z1q_htn_g3c)
- [Recipe: Sending emails to your Inside Sales team when a Zendesk ticket is identified as a lead](#topic_y2s_4sn_g3c)

## Connecting Gmail to action builder

Before you can include external actions in your action flows, you must connect the
action builder to the external system.

When connecting to external systems for use in action flows, the following best practices are recommended:

- All external actions performed by an action flow are attributed to the user who connected the
  external system. Therefore, it's a best practice to use a dedicated service
  account rather than personal credentials when connecting to each external
  system.
- All integrations request access to necessary scopes. However, it's important that you review and validate the scopes before authorizing the connection to the external system.
- When managing credentials for API key-based tools, such as OpenAI, it's best to store keys in a secure vault or credential manager.

**To connect action builder to Gmail**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)
   **Apps and integrations** in the sidebar, then select **Actions > Action
   flows**.
2. [Create](https://support.zendesk.com/hc/en-us/articles/8855601898266) or [edit](https://support.zendesk.com/hc/en-us/articles/9052312956570) an action flow.
3. Open the step sidebar.
4. Under **External actions**, click **Gmail**.
5. Click **Connect**.
6. Follow Gmail's prompts to authenticate and complete the connection.

   You'll
   log into a Google Workspace or Gmail account, and admin approval might
   be required in managed environments.

   The following scope is
   required for the account you authenticate with:
   `https://www.googleapis.com/auth/gmail.send`.

   Note: All
   external actions performed by an action flow are attributed to the user
   who connected the external system. Therefore, it is a best practice to
   use a dedicated service account rather than personal credentials when
   connecting to each external system.

After you've connected to the system, you'll see an indicator that it's connected and
details about the instance you're connected to, as well as the actions available for
Gmail.

## Using Gmail actions in action flows

Gmail action steps can be used to send new emails.

The following Gmail actions are available:

- [Sending emails in Gmail](#topic_fy1_1wn_g3c)

### Sending emails in Gmail

Use the *Send email* action to send a new email.

This action has the following inputs and outputs:

|  | Variables |
| --- | --- |
| Inputs | Required: `Recipient's email`, `Subject`, `Body` Optional: `BCC emails`, `CC emails` |
| Output | `threadID`, `ID`, `labelIds` |

## Recipe: Sending emails to your Inside Sales team when a Zendesk ticket is identified as a lead

The following example action flow uses ticket tags added by agents to automatically
send notification emails to the Inside Sales team when a ticket is identified as a
lead.

Such an action flow would consist of the following steps:

1. Add an action flow trigger with the following details:
   1. Click **Add trigger**.
   2. In the step sidebar, under **Zendesk**, click
      **Tickets**.
   3. Click **Lifecycle** and select **Ticket is tagged**.
   4. Click **Add condition**.
   5. Under **Variable**, click **Ticket tags changed** and select
      **Tags (added)**.
   6. Set the **Operator** to **Contains at least 1 of**.
   7. Under **Value**, enter **sales\_lead**.
2. Add a step to look up ticket details:
   1. In the action builder, beneath the action flow trigger, click the
      **Add step** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_action_flows_add.png)).
   2. In the step sidebar, under **Zendesk actions**, click **Look up
      ticket**.
   3. Under **Ticket ID**, click into the field and then click
      **Select a variable instead**.
   4. Within the variable menu, select **Ticket is tagged** as the step
      that outputs the variable you want to use, and then select **Ticket
      ID**.
3. Add a step to look up user details about the ticket requester:
   1. In the action builder, click the **Add step** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_action_flows_add.png)).
   2. In the step sidebar, under **Zendesk actions**, click **Look up
      user**.
   3. Under **User ID type**, select **Zendesk user ID**.
   4. For **User ID**, click **Add variable**.
   5. Within the variable menu, select **Look up ticket** as the step
      that outputs the variable you want to use, and then select
      **Requester ID**.
4. Add a step to lookup details about the ticket requester's organization:
   1. In the action builder, click the **Add step** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_action_flows_add.png)).
   2. In the step sidebar, under **Zendesk actions**, click **Look up
      organization**.
   3. Under **Organization ID type**, select **Zendesk organization
      ID**.
   4. For **Organization ID**, click **Add variable**.
   5. Within the variable menu, select **Look up user** as the step
      that outputs the variable you want to use, and then select
      **Organization ID**.
5. Add a step that sends an email based on the information you collected for
   the ticket, user, and organization:
   1. In the action builder, click the **Add step** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_action_flows_add.png)).
   2. In the step sidebar, under **External actions**, click
      **Gmail** and then select **Send email**.
   3. Under **Recipient's email**, enter the Inside sales team
      distribution list. For example, **sales@yourcompany.com**.
   4. Under **Subject**, enter **Ticket *Ticket ID* Identified as
      Lead**, where *Ticket ID* is a variable.

      Click **Add
      variable**, select **Look up ticket**, and select
      **Ticket ID**, to insert the *Ticket ID* variable
      into the subject.
   5. Under **Body**, enter the message you want to send to the Inside
      sales team for new prospects. Include relevant ticket and user
      information as variables from the Look up ticket and Look up user
      steps, respectively, to streamline their ability to follow up. In
      the following example, all variables are
      italicized:

      ```
      Hi Sales Team,

      Ticket Ticket ID has been identified as a lead. Can you please follow up with User Name as soon as possible?

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
6. Click **Save**.
7. Click **Test** to [test the action flow](https://support.zendesk.com/hc/en-us/articles/9052312956570#topic_uyj_qsw_3fc).
8. Click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options-menu-icon-small.png)) and select **Activate** to begin sending
   emails to the sales team when Zendesk tickets are identified as sales
   leads.