# Using Microsoft Calendar actions in action flows

Source: https://support.zendesk.com/hc/en-us/articles/9849724302234-Using-Microsoft-Calendar-actions-in-action-flows

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

By connecting the [action builder](https://support.zendesk.com/hc/en-us/articles/8855513857306) to external systems, such as Microsoft Calendar, admins can integrate Zendesk with external systems in automated workflows, improving collaboration and maintaining a seamless experience across multiple platforms.

Note: The steps associated with external systems in action flows are referred to collectively as *external actions*.

This article contains the following topics:

- [Connecting Microsoft Calendar to action builder](#topic_ehn_bqr_1hc)
- [Using Microsoft Calendar actions in action flows](#topic_t1l_4qr_1hc)
- [Recipe: Automatically creating handover meeting in Microsoft Calendar when a ticket is reassigned](#topic_npy_2wf_dhc)

## Connecting Microsoft Calendar to action builder

Before you can include external actions in your action flows, you must connect the action builder to the external system.

When connecting to external systems for use in action flows, the following best practices are recommended:

- All external actions performed by an action flow are attributed to the user who connected the external system. Therefore, it is a best practice to use a dedicated service account rather than personal credentials when connecting to each external system.
- All integrations request access to necessary scopes. However, it's important that you review and validate the scopes before authorizing the connection to the external system.
- When managing credentials for API key-based tools, such as OpenAI, it's best to store keys in a secure vault or credential manager.

**To connect Microsoft Calendar to action builder**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)
   **Apps and integrations** in the sidebar, then select **Actions > Action flows**.
2. [Create](https://support.zendesk.com/hc/en-us/articles/8855601898266) or [edit](https://support.zendesk.com/hc/en-us/articles/9052312956570) an action flow.
3. Open the step sidebar.
4. Under **External actions**, click **Microsoft Calendar**.
5. Click **Connect**.
6. Use Microsoft to authenticate the account.

   You must use a service account when connecting to Microsoft Calendar because it uses User Scopes.
   Authenticating with a personal account won't work properly.

   The following scopes are required: `offline_access`, `User.Read`, `Calendars.Read`, `Calendars.ReadWrite`, `MailboxSettings.Read`, `MailboxSettings.ReadWrite`.

   Note: All external actions performed by an action flow are attributed to the user who connected the external system.

After you've connected to the system, you'll see an indicator that it's connected and details about the instance you're connected to, as well as the actions available for Jira.

## Using Microsoft Calendar actions in action flows

Microsoft Calendar action steps can be used to automatically create, update, and manage calendar events in Microsoft Calendar.

The following Microsoft Calendar actions are available:

- [Create event](#topic_o3x_nrr_1hc)
- [Update event](#topic_bk4_4rr_1hc)
- [Search for event](#topic_nqw_qrr_1hc)
- [Delete event](#topic_ktk_rrr_1hc)

### Creating a calendar event

Use the *Create event* action to create a new calendar event. For example, you might want to automatically create follow-up meetings or reminders when high-priority tickets are created in Zendesk.

This action has the following inputs and outputs:

| | Variables |
| --- | --- |
| Inputs | `external_id`, `calendar_id`, `title`, `start_time`, `end_time`, `attendees`, `description`, `location` |
| Output | `id`, `link` |

### Updating a calendar event

Use the *Update event* action to modify an existing calendar event, such as rescheduling it when a ticket due date changes.

This action has the following inputs and outputs:

| | Variables |
| --- | --- |
| Inputs | `external_id`, `calendar_id`, `event_id`, `updated_fields` |
| Output | `id`, `link` |

### Searching for a calendar event

Use the *Search for calendar event* action to retrieve information about an existing calendar event. This is useful for checking whether an event already exists and verifying the details of an existing event.

This action has the following inputs and outputs:

| | Variables |
| --- | --- |
| Inputs | `external_id`, `query (title, date range, attendee)` |
| Output | `events (id, title, start_time, end_time, attendees, link)` |

### Deleting a calendar event

Use the *Delete event* action to delete an existing calendar event.

This action has the following inputs and outputs:

| | Variables |
| --- | --- |
| Inputs | `external_id`, `calendar_id`, `event_id` |
| Output | none |

## Recipe: Automatically creating handover meeting in Microsoft Calendar when a ticket is reassigned

The following example action flow automatically creates a meeting in Microsoft Calendar when a ticket is reassigned and invites the previous asignee and new assignee. This ensures consistent transfer of ownership with full context of the ticket, which reduces delays and improves accountability.

Such an action flow might consist of the following steps:

1. Add an action flow trigger with the following details:
   1. Click **Add trigger**.
   2. In the step sidebar, under **Zendesk**, click **Tickets**.
   3. Click **Routing** and select **Ticket agent assignment changed**.
2. Add a step to look up ticket details:
   1. In the action builder, beneath the action flow trigger, click the **Add step** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_action_flows_add.png)).
   2. In the step sidebar, under **Zendesk actions**, click **Look up ticket**.
   3. Under **Ticket ID**, click into the field and then click **Select a variable instead**.
   4. Within the variable menu, select **Ticket assignment changed** as the step that output the variable you want to use, and then select **Ticket ID**.
3. Add a step to look up user details about the ticket assignee:
   1. In the action builder, click the **Add step** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_action_flows_add.png)).
   2. In the step sidebar, under **Zendesk actions**, click **Look up user**.
   3. Under **User ID type**, select **Zendesk user ID**.
   4. For **User ID**, click **Add variable**.
   5. Within the variable menu, select **Look up ticket** as the step that outputs the variable you want to use, and then select **Assignee ID**.
4. Add a step to lookup details about the ticket requester's organization:
   1. In the action builder, click the **Add step** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_action_flows_add.png)).
   2. In the step sidebar, under **Zendesk actions**, click **Look up organization**.
   3. Under **Organization ID type**, select **Zendesk organization ID**.
   4. For **Organization ID**, click **Add variable**.
   5. Within the variable menu, select **Look up user** as the step that outputs the variable you want to use, and then select **Organization ID**.
5. Add a step that creates a calendar event based on the information you collected for the ticket, assignee, and organization:
   1. In the action builder, click the **Add step** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_action_flows_add.png)).
   2. In the step sidebar, under **External actions**, click **Microsoft Calendar** and then select **Create event**.
   3. Under **Calendar**, select the appropriate calendar from the connected account in which to create the event.
   4. Under **Title**, enter **Handoff ticket** and then click **add variable** **Ticket ID**.
6. Click **Save**.
7. Click **Test** to [test the action flow](https://support.zendesk.com/hc/en-us/articles/9052312956570#topic_uyj_qsw_3fc).
8. Click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options-menu-icon-small.png)) and select **Activate** to begin using the action flow to automatically schedule ticket handoff meetings when a ticket's assignee changes.