# Using Slack actions in action flows

Source: https://support.zendesk.com/hc/en-us/articles/9849650344730-Using-Slack-actions-in-action-flows

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

By connecting the [action builder](https://support.zendesk.com/hc/en-us/articles/8855513857306) to external systems, such as Slack, admins can integrate Zendesk with external systems in automated workflows, improving collaboration and maintaining a seamless experience across multiple platforms.

Note: The steps associated with external systems in action flows are referred to collectively as *external actions*.

This article contains the following topics:

- [Connecting Slack to action builder](#topic_urq_djr_1hc)
- [Using Slack actions in action flows](#topic_j22_2jr_1hc)
- [Recipe: Notifying agents of newly assigned tickets in Slack](#topic_evq_pzd_fhc)

## Connecting Slack to action builder

Before you can include external actions in your action flows, you must connect the action builder to the external system.

When connecting to external systems for use in action flows, the following best practices are recommended:

- All external actions performed by an action flow are attributed to the user who connected the external system. Therefore, it's a best practice to use a dedicated service account rather than personal credentials when connecting to each external system.
- All integrations request access to necessary scopes. However, it's important that you review and validate the scopes before authorizing the connection to the external system.
- When managing credentials for API key-based tools, such as OpenAI, it's best to store keys in a secure vault or credential manager.

**To connect action builder to Slack**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)
   **Apps and integrations** in the sidebar, then select **Actions > Action flows**.
2. [Create](https://support.zendesk.com/hc/en-us/articles/8855601898266) or [edit](https://support.zendesk.com/hc/en-us/articles/9052312956570) an action flow.
3. Open the step sidebar.
4. Under **External actions**, click **Slack**.
5. Click **Connect**.
6. Use Slack to authenticate the account.

   To complete authentication, you must invite the Zendesk connector app: `/invite @Zendesk Connector`.

   Note: All external actions performed by an action flow are attributed to the user who connected the external system. Therefore, it is a best practice to use a dedicated service account rather than personal credentials when connecting to each external system.

After you've connected to the system, you'll see an indicator that it's connected and details about the instance you're connected to, as well as the actions available for Slack.

## Using Slack actions in action flows

Slack action steps can be used in action flows to streamline communication and make sure users know about other things being performed by action flows. For example, you can send messages to channels and individual users alerting them of new tickets or Jira issue assignments, post AI-generated summaries of tickets into a Slack thread, escalate direct messages to public channels for broader visibility, add reactions to automatically acknowledge messages, or extract message details for analysis and reply with AI-generated content.

Note: For all Slack actions, mentions of users, groups, and special mentions require the following formatting. For example, `@here` must be formatted as `<!here>` in the message input. See [Slack's Advanced formatting with special parsing](https://docs.slack.dev/messaging/formatting-message-text/#advanced).

The following Slack actions are available:

- [Post message to channel](#topic_itj_3kr_1hc)
- [Send direct message](#topic_d2y_3kr_1hc)
- [Reply to message thread](#topic_ysv_jkr_1hc)
- [Fetch thread messages](#topic_aq5_kkr_1hc)
- [Add reaction](#topic_xyd_mkr_1hc)
- [Fetch message](#topic_lz5_mkr_1hc)
- [Find user](#topic_w3r_nkr_1hc)

### Posting a message to a channel

Use the *Post message to channel* action to send a message to a public or private channel.

This action has the following inputs and outputs:

| | Variables |
| --- | --- |
| Inputs | `channel`, `message` |
| Output | `channel`, `ts`, `ok` |

### Sending a direct message

Use the *Send direct message* action to send a direct message to a specific user.

Note: Although Slack supports DMs with up to 9 other individuals, this step only supports sending a direct message to a single individual.

| | Variables |
| --- | --- |
| Inputs | `email`, `message` |
| Output | Full message data |

### Replying to a message in a thread

Use the *Reply to message thread* action to post a reply to a message in a thread. This step can create a thread or reply within an existing thread.

This action has the following inputs and outputs:

| | Variables |
| --- | --- |
| Inputs | `email`, `message` |
| Output | None |

### Fetching all messages in a thread

Use the *Fetch thread messages* action to retrieve all messages in a thread.

This action has the following inputs and outputs:

| | Variables |
| --- | --- |
| Inputs | `channel`, `thread_ts`, `reply_ts` |
| Output | `messages` |

### Adding a reaction to a message

Use the *Add reaction* action to add an emoji reaction to a message.

This action has the following inputs and outputs:

| | Variables |
| --- | --- |
| Inputs | `channel`, `name`, `timestamp` |
| Output | `success` |

### Fetching a message

Use the *Fetch message* action to retrieve the content and metadata of a message.

This action has the following inputs and outputs:

| | Variables |
| --- | --- |
| Inputs | `channel`, `timestamp` |
| Output | `text`, `user` |

### Finding a user

use the *Find user* action to retrieve a Slack user so they can be referenced later in the action flow.

This action has the following inputs and outputs:

| | Variables |
| --- | --- |
| Inputs | `user_id` |
| Output | `display_name`, `email`, `real_name`, `user_id` |

## Recipe: Notifying agents of newly assigned tickets in Slack

The following example action flow automatically sends notifications to agents in Slack when a Zendesk ticket is assigned to them. This sort of notification can reduce response time and prevent tickets from slipping through the cracks.

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
6. Add a step that sends a direct message in Slack to the ticket assignee that contains the information you collected for the ticket, assignee, and organization:
   1. In the action builder, click the **Add step** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_action_flows_add.png)).
   2. In the step sidebar, under **External actions**, click **Slack** and then select **Post direct message**.
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
9. Click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options-menu-icon-small.png)) and select **Activate** to begin using the action flow to automatically notify agents in Slack that a Zendesk ticket has been assigned to them.