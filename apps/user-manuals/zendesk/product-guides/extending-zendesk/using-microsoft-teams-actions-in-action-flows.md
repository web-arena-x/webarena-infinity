# Using Microsoft Teams actions in action flows

Source: https://support.zendesk.com/hc/en-us/articles/9841034139674-Using-Microsoft-Teams-actions-in-action-flows

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

By connecting the [action builder](https://support.zendesk.com/hc/en-us/articles/8855513857306) to external systems, such as Microsoft Teams, admins can integrate Zendesk with external systems in automated workflows, improving collaboration and maintaining a seamless experience across multiple platforms.

Note: The steps associated with external systems in action flows are referred to collectively as *external actions*.

This article contains the following topics:

- [Connecting Microsoft Teams to action builder](#topic_o34_2jw_zgc)
- [Using Microsoft Teams actions in action flows](#topic_t22_tjw_zgc)
- [Recipe: Notifying agents of newly assigned tickets in Microsoft Teams](#topic_en1_xpd_fhc)

## Connecting Microsoft Teams to action builder

Before you can include external actions in your action flows, you must connect the action builder to the external system.

When connecting to external systems for use in action flows, the following best practices are recommended:

- All external actions performed by an action flow are attributed to the user who connected the external system. Therefore, it is a best practice to use a dedicated service account rather than personal credentials when connecting to each external system.
- All integrations request access to necessary scopes. However, it's important that you review and validate the scopes before authorizing the connection to the external system.
- When managing credentials for API key-based tools, such as OpenAI, it's best to store keys in a secure vault or credential manager.

**To connect Microsoft Teams to action builder**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)
   **Apps and integrations** in the sidebar, then select **Actions > Action flows**.
2. [Create](https://support.zendesk.com/hc/en-us/articles/8855601898266) or [edit](https://support.zendesk.com/hc/en-us/articles/9052312956570) an action flow.
3. Open the step sidebar.
4. Under **External actions**, click **Microsoft Teams**.
5. Click **Connect**.
6. Use Microsoft to authenticate the account.

   You must use a service account when connecting to Microsoft Teams because it uses User Scopes.
   Authenticating with a personal account won't work properly.

   The following scopes are required: `ChannelMessage.Send`, `Chat.ReadWrite`, `ChannelMessage.Read.All`, `User.ReadBasic.All`, `User.Read.All`, `offline_access`.

   Note: All external actions performed by an action flow are attributed to the user who connected the external system.

After you've connected to the system, you'll see an indicator that it's connected and details about the instance you're connected to, as well as the actions available for Microsoft Teams.

## Using Microsoft Teams actions in action flows

Microsoft Teams action steps can be used to send updates and notifications from Zendesk to Microsoft Teams. This allows for automated actions, such as posting messages to channels or individuals and adding reactions to messages. Automating interactions in Microsoft Teams can streamline collaboration and keep teams aligned without needing to leave their primary workspace.

The following Teams actions are available:

- [Add reaction to channel message](#topic_ssz_bkw_zgc)
- [Add reaction to direct message](#topic_a5y_ckw_zgc)
- [Look up thread](#topic_tqf_2kw_zgc)
- [Look up user](#topic_yz1_fkw_zgc)
- [Post message to channel](#topic_evw_gkw_zgc)
- [Post direct message](#topic_pyb_3kw_zgc)

## Adding a reaction to a channel message

Use the *Add reaction to channel message* action to add an emoji reaction to a message in a channel.

This action has the following inputs and outputs:

| | Variables |
| --- | --- |
| Inputs | `external_id`, `team_id`, `channel_id`, `message_id`, `reaction` |
| Output | none |

## Adding a reaction to a direct message

Use the *Add reaction to direct message* action to add an emoji reaction to a direct message.

This action has the following inputs and outputs:

| | Variables |
| --- | --- |
| Inputs | `external_id`, `message_id`, `reaction` |
| Output | none |

## Looking up a thread

Use the *Look up thread* action to retrieve a thread of messages from a channel or direct message.

This action has the following inputs and outputs:

| | Variables |
| --- | --- |
| Inputs | `external_id`, `team_id`, `channel_id`, `message_id` |
| Output | `messages` |

## Looking up a user

Use the *Look up user* to retrieve data about a user in Microsoft Teams for further use in the action flow.

This action has the following inputs and outputs:

| | Variables |
| --- | --- |
| Inputs | `external_id`, `user_id` |
| Output | `display_name`, `email`, `real_name`, `user_id` |

## Posting a message to a channel

Use the *Post message to channel* action to send a message to a specific channel in Microsoft Teams.

This action has the following inputs and outputs:

| | Variables |
| --- | --- |
| Inputs | `external_id`, `team_id`, `channel_id`, `message` |
| Output | `id` |

## Sending a direct message

Use the *Post direct message* action to send a message to a specified user in Microsoft Teams.

This action has the following inputs and outputs:

| | Variables |
| --- | --- |
| Inputs | `external_id`, `message` |
| Output | `id` |

## Recipe: Notifying agents of newly assigned tickets in Microsoft Teams

The following example action flow automatically sends notifications to agents in Microsoft Teams when a Zendesk ticket is assigned to them. This sort of notification can reduce response time and prevent tickets from slipping through the cracks.

Such an action flow might consist of the following steps:

1. Add an action flow trigger with the following details:
   1. Click **Add trigger**.
   2. In the step sidebar, under **Zendesk**, click **Tickets**.
   3. Click **Routing** and select **Ticket assignment changed**.
2. Add a step to look up ticket details:
   1. In the action builder, beneath the action flow trigger, click the **Add step** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_action_flows_add.png)).
   2. In the step sidebar, under **Zendesk actions**, click **Look up ticket**.
   3. Under **Ticket ID**, click into the field and then click **Select a variable instead**.
   4. Within the variable menu, select **1 Ticket agent assignment changed** as the step that output the variable you want to use, and then select **Ticket ID**.
3. Add a step to look up user details about the ticket assignee:
   1. In the action builder, click the **Add step** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_action_flows_add.png)).
   2. In the step sidebar, under **Zendesk actions**, click **Look up user**.
   3. Under **User ID type**, select **Zendesk user ID**.
   4. For **User ID**, click **Add variable**.
   5. Within the variable menu, select **2 Look up ticket** as the step that outputs the variable you want to use, and then select **Assignee ID**.
4. Add a step to look up user details about the ticket requester:
   1. In the action builder, click the **Add step** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_action_flows_add.png)).
   2. In the step sidebar, under **Zendesk actions**, click **Look up user**.
   3. Under **User ID type**, select **Zendesk user ID**.
   4. For **User ID**, click **Add variable**.
   5. Within the variable menu, select **2 Look up ticket** as the step that outputs the variable you want to use, and then select **Requester ID**.
5. Add a step to lookup details about the ticket requester's organization:
   1. In the action builder, click the **Add step** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_action_flows_add.png)).
   2. In the step sidebar, under **Zendesk actions**, click **Look up organization**.
   3. Under **Organization ID type**, select **Zendesk organization ID**.
   4. For **Organization ID**, click **Add variable**.
   5. Within the variable menu, select **4 Look up user** as the step that outputs the variable you want to use, and then select **Organization ID**.
6. Add a step that sends a direct message in Teams to the ticket assignee that contains the information you collected for the ticket, assignee, and organization:
   1. In the action builder, click the **Add step** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_action_flows_add.png)).
   2. In the step sidebar, under **External actions**, click **Microsoft Teams** and then select **Post direct message**.
   3. Under **Email**, click **Add variable**.
   4. Within the variable menu, select **3 Look up user** as the step that outputs the variable, and then select **Email**.
   5. Under **Message**, enter the message you want to send to the newly assigned agent. Include relevant ticket, requester, and organization information as variables from the Look up ticket and Look up user steps, respectively, to streamline their ability to solve the ticket. In the following example, all variables are italicized:

      ```
      Hi Assignee > Name,

      Ticket Ticket ID has been assigned to you. Please respond as soon as possible.

      User contact information:
      - Email: Requester > Email
      - Locale and timezone: Requester > Locale - Requester > IANA timezone
      - Notes: Requester > Notes

      Here's more context on the ticket:
      - Ticket subject: Ticket Subject
      - Ticket description: Ticket Description
      - Last ticket update: Ticket's Latest agent update
      ```
7. Click **Save**.
8. Click **Test** to [test the action flow](https://support.zendesk.com/hc/en-us/articles/9052312956570#topic_uyj_qsw_3fc).
9. Click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options-menu-icon-small.png)) and select **Activate** to begin using the action flow to automatically notify agents in Microsoft Teams that a Zendesk ticket has been assigned to them.