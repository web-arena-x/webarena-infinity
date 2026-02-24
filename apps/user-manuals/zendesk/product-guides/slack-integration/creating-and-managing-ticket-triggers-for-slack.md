# Creating and managing ticket triggers for Slack

Source: https://support.zendesk.com/hc/en-us/articles/4963959597594-Creating-and-managing-ticket-triggers-for-Slack

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

When using the [Slack for Zendesk Support integration](https://support.zendesk.com/hc/en-us/articles/4408833756698), you can set up [ticket triggers](https://support.zendesk.com/hc/en-us/articles/4408822236058) to notify Slack users about Zendesk ticket events in specified Slack channels.

This article covers the following topics:

- [Creating ticket triggers for Slack ticket notifications](#topic_tk1_csx_dvb)
- [Using Markdown to format text and alert users in Slack](#topic_yfs_jyx_dvb)
- [Managing ticket triggers for Slack](#topic_jsf_2cy_dvb)

Related articles:

- [Configuring the Slack for Zendesk Support integration](https://support.zendesk.com/hc/en-us/articles/6894206691866)
- [Using the Slack for Zendesk Support integration](https://support.zendesk.com/hc/en-us/articles/4408843621530)

## Creating ticket triggers for Slack ticket notifications

Remember that before creating a ticket trigger, you must [add the app](https://support.zendesk.com/hc/en-us/articles/6894206691866#topic_tjj_vjx_dvb) to the Slack channel where you’d like to send the notification. You must be an admin to create triggers for Slack.

**To create ticket triggers for Slack**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Business rules >
   Triggers**.

   Tip: You can also create and manage Slack triggers in [Slack integration settings](https://support.zendesk.com/hc/en-us/articles/6894206691866)
   by navigating to Admin Center > **Integrations** >
   **Integrations** and clicking **View** under Slack.
2. On the Triggers page, click the **Tickets** tab.
3. Click **Add trigger**.

   Alternatively, you can [copy an existing trigger](https://support.zendesk.com/hc/en-us/articles/4408882237722#topic_dwq_zoy_tb) and modify it.
4. In the **Trigger name** field, enter a name for the trigger.

   It's recommended to include the Slack workspace and channel in the trigger name to help identify it. Example: "New ticket for #delivery-support - Workspace 1"
5. (Optional) Enter a **Description** for your trigger to provide details about what the trigger does.

   Example: "Notifies all users in the
   #delivery-support channel when a new ticket is assigned to the Support group."
6. Select an existing **Category** for your trigger or [create](https://support.zendesk.com/hc/en-us/articles/4408834781594) a new one.

   It is recommended to create a **Slack** category for your Slack triggers.
7. Click **Add condition** to set up the trigger to meet **All** or **Any** conditions.

   Conditions are the qualifications needed for the trigger to fire.
8. Select a **Condition**, **Field operator**, and **Value** for each condition you add.

   The field operator determines the relationship between the condition and the value. For example, if you select the field operator "Is", your condition must be equal to the value. Different conditions will contain different field operators.

   See [Building trigger condition statements](https://support.zendesk.com/hc/en-us/articles/4408893545882#topic_i3y_fkz_1cb).

   Note: It is recommended to keep your trigger statements simple. The more complicated a trigger is, the harder it will be to troubleshoot and maintain.
9. Click **Add action**, then select **Notify Zendesk integration** and **Slack integration** from the drop-down lists.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/slack_triggers_actions.png)
10. If you have multiple Slack workspaces connected to this Zendesk account, choose the workspace in the **Slack workspace** field.
11. In the **Slack channel** field, select the channel you want notifications posted in.

    ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/slack_trigger_workspace.png)

    Only channels to which the Zendesk app has been added appear in the drop-down list. To see additional channels here, [add the app](https://support.zendesk.com/hc/en-us/articles/6894206691866#topic_tjj_vjx_dvb) to those channels.
    If you see the message `Slack channels couldn't be loaded`, then the Zendesk app hasn't been added to any channels.

    The Slack channel list includes private channels that you (the current admin) are a member of. If the app is a member of a private channel you're not a member of, you won’t see it here until you are invited to that channel. If you don't see your private channels in Zendesk (and you do see them in Slack), make sure you added the Zendesk app to these channels. Also, ensure that your default email in Zendesk matches your Slack email address.

    If you are editing a trigger and don't have access to a private channel listed here, "Private Channel" displays in this field, but you can still edit and save the trigger.
12. Use static text and [placeholders](https://support.zendesk.com/hc/en-us/articles/4408886858138) in the **Notification header** and **Notification body** fields to create the notification.

    A simple notification header and body have been created for you. You can use these as-is or modify them. You can also use [markdown](#topic_yfs_jyx_dvb) to alert channel members or format text in Slack.

    Below is an example notification header and body configured in a trigger and the resulting notification in Slack.

    ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/slack_trigger_notification_2.png)

    ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/slack_channel_message_4.png)
13. Click **Create**.

Your new trigger is added to the end of the list of triggers. You can [reorder the list](https://support.zendesk.com/hc/en-us/articles/4408882237722#topic_vnl_zpy_tb) of triggers or [edit any ticket trigger](https://support.zendesk.com/hc/en-us/articles/4408882237722#topic_dwq_zoy_tb).

## Using Markdown to format text and alert users in Slack

Slack supports Markdown, which is a formatting syntax for plain text. For example, if you surround a word with asterisks (\*like this\*), it appears bold in Slack.

Slack also supports user @mentions and alerts, which can be especially useful in ticket notifications. For example, add **<!here>** in the message header to alert all members of the Slack channel when a notification is posted.

The table below includes the Markdown formatting you can use in the **Notification header** and **Notification body** of your Slack triggers.

| Type | Markdown | Result |
| --- | --- | --- |
| Italics | `_italic_` | *italic* |
| Bold | `*bold*` | **bold** |
| Strikethrough | `~strike~` | |
| Emojis | `:smile:` | |
| Channel alert (notify channel) | `<!here>` | Notifies all members of the channel. |
| [User mention](https://api.slack.com/reference/surfaces/formatting#mentioning-users) | To notify user ID U024BE7LH: `<@U024BE7LH>` | Links to the mentioned user’s Slack profile, and the mentioned user is notified. |
| [Group mention](https://api.slack.com/reference/surfaces/formatting#mentioning-groups) | To mention a [Slack user group](https://slack.com/help/articles/212906697), provide the group ID using the following syntax: `<!subteam^ID>` `!subteam^` is required before the group ID. | Links to the mentioned group’s Slack profile, and all members of the mentioned group are notified. |

## Managing ticket triggers for Slack

View your ticket triggers for Slack on the Triggers page, where you can manage your existing triggers and create new ones.

See [Opening and viewing your triggers list](https://support.zendesk.com/hc/en-us/articles/4408818901530) for more information on accessing and taking action on triggers.