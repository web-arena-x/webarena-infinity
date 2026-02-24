# Using the Slack for Zendesk Support integration

Source: https://support.zendesk.com/hc/en-us/articles/4408843621530-Using-the-Slack-for-Zendesk-Support-integration

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

After the Slack for Zendesk Support integration has been [installed](https://support.zendesk.com/hc/en-us/articles/4408833756698) and [configured](https://support.zendesk.com/hc/en-us/articles/6894206691866), you can create and comment on Zendesk Support tickets.
If your Zendesk administrator has configured [triggers for Slack](https://support.zendesk.com/hc/en-us/articles/4963959597594), you will also see ticket updates in your Slack
channels.

This article includes the following topics:

- [Viewing ticket notifications in Slack](#topic_qt2_1z4_ldb)
- [Creating tickets in Slack](#topic_xgp_1z4_ldb)
- [Viewing tickets created in Slack](#topic_pp2_vl2_v2b)
- [Adding internal notes to existing tickets in Slack](#topic_c1d_xjd_xdb)
- [FAQ](#topic_umb_w5w_zdb)

Related articles:

- [Creating and managing triggers for Slack](https://support.zendesk.com/hc/en-us/articles/4963959597594)
- [Using side conversations for Slack](https://support.zendesk.com/hc/en-us/articles/4408844202778)
- [Using the Answer Bot for Slack integration](https://support.zendesk.com/hc/en-us/articles/4408827411098)

## Viewing ticket notifications in Slack

If your administrator configured Zendesk triggers for Slack, you’ll see
notifications in your Slack channels similar to the example below when tickets are created
or updated in Zendesk. The content within these notifications is typically high-level and
customizable by your administrator.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/slack_channel_message_4.png)

Click the subject line (in the example above, the subject is **Delivery to wrong address**) or the ticket number in the footer to open the ticket in Zendesk
Support.

The footer also includes the ticket status, the Zendesk account in which the ticket was
created, and the time the notification was sent.

## Creating tickets in Slack

You can create tickets in Slack for agents to solve in Zendesk Support. The requester is
set to the Slack authenticated user by default but can be changed.

You can create tickets directly in Slack in the following ways.

- Using the `/zendesk`
  [global shortcut](#topic_sk3_cc5_1tb)
- Using a [Slack action](#topic_rlf_fd5_1tb), which
  converts a Slack message into a ticket
- Using the [Zendesk app](#topic_ywp_vsg_s1c) in the
  Slack sidebar
- In a [Slack Connect channel](#topic_xcj_hd5_1tb), using
  the @zendesk mention in a message

Depending on how your administrator configured notifications, you might see notifications
in your Slack channels after creating a ticket.

The **created\_from\_slack** tag is automatically added to tickets if created in Slack.
(Using the @zendesk mention in a Slack Connect channel does not add this tag to tickets.)
Use this tag to create views or business rules to assist with the ticket workflow. See [Viewing tickets created in Slack](#topic_pp2_vl2_v2b).

### Creating tickets with a global shortcut

You can use the `/zendesk` shortcut to create a ticket without creating a
Slack message first. The shortcut can be used in channels where the Slack for Zendesk
Support integration has been [invited to the channel](https://support.zendesk.com/hc/en-us/articles/6894206691866#topic_tjj_vjx_dvb).

See the [Slack documentation](https://api.slack.com/interactivity/shortcuts) for more information about global
shortcuts.

**To create a ticket using a shortcut**

1. In a channel, type: `/zendesk`
2. Select **Create a ticket** from the menu that appears.

   The Create new
   ticket form appears.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/slack_new_ticket_subdomain.png)
3. Enter the following information:

   - **Subdomain**: If your company has multiple Zendesk accounts connected to the
     workspace, select the Zendesk [subdomain](https://support.zendesk.com/hc/en-us/articles/4409381383578) you're creating a ticket in.
   - **Subject**: A brief, descriptive subject for the ticket.
   - **Requester (optional)**: The user submitting the ticket is selected as the
     requester. However, you can click and type in this field to display a searchable
     list of existing Slack users.

     If an unrecognized user creates the ticket in Slack, a
     new Zendesk Support end user is created and assigned to the ticket. Similarly,
     when an agent creates a ticket on behalf of someone else, they can select a
     requester from a list of existing Slack users or create a new end user.
   - **Assignee (optional)**: The name of the Zendesk group you want to assign the
     ticket to. Click this field to display a list of groups or enter the group's name.
     As you type, you can select the assignee from the displayed list of matches.
   - **Description (public)**: A more detailed description of the ticket. Anyone
     with access to the ticket can view the information in this field.
4. Click **Submit**.

   A ticket is created in Zendesk Support and a
   notification is sent to the Zendesk app in Slack under the Messages tab.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/slack_Zendesk_app_notify_3.png)

   Other channels may be notified if
   your administrator set up notifications using Zendesk triggers.

### Creating tickets with a Slack action

You can convert an existing Slack message into a ticket by selecting the **Create a
ticket** action in the **More actions** menu. The action works only in channels
where the Slack for Zendesk Support integration has been [invited to the channel](https://support.zendesk.com/hc/en-us/articles/6894206691866#topic_tjj_vjx_dvb).

**To create a ticket using the Slack action**

1. In the Slack channel, hover over the message to display the
   options.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/slack_more_actions_3.png)
2. Click the **More actions** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_options_icon.png)) to display the message actions, then click **Create a
   ticket**.
3. Complete the ticket fields in the Create new ticket form.

   The
   **Description** field is pre-populated with the text of the Slack message you're
   using to create the ticket. You can leave it as is or edit the text.
4. Click **Submit**.

   The ticket is created in Support and is added as a reply to
   the Slack thread with the Zendesk metadata (ticket number, status, account, and
   date/time) included.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/slack_ticket_thread_4.png)

Note: Single-channel guests do not have access to several commands. To
gain access, they must be assigned as a multi-channel guest and have access granted. This
is a limitation set by Slack workspaces for guest usage permission limitations. For more
information on granting guests access, see [Manage app approval for your workspace](https://slack.com/intl/en-ca/help/articles/222386767-Manage-app-installation-settings-for-your-workspace).

### Creating tickets using the Zendesk app

You can create tickets from the Zendesk app in Slack.

1. Click **Apps** > **Zendesk** in the Slack sidebar.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/slack_zendesk_app.png)
2. Click **Create a ticket** on the **Home** tab.
3. Complete the ticket fields in the Create new ticket form.
4. Click **Submit**.

A ticket is created in Zendesk Support and a notification is sent to the Zendesk app in
Slack under the Messages tab. Other channels may be notified if your administrator set up
notifications using Zendesk triggers.

### Creating tickets in a Slack Connect channel

[Slack
Connect](https://slack.com/connect) lets you work with people outside your company. Internal and external
users within a Slack Connect channel can create tickets using the @zendesk mention. The
**Assignee** field is not available for external users in the Create new ticket form.

The @zendesk mention can be used in channels where the Slack for Zendesk Support
integration has been [invited to the channel](https://support.zendesk.com/hc/en-us/articles/6894206691866#topic_tjj_vjx_dvb).

**To create a ticket in a Slack Connect channel**

1. In a Slack Connect channel, enter the **@zendesk** mention in a
   message.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/slack_tag_integration_.png)

   For internal
   users, the integration will respond with a message and a button to create a new
   ticket. For external users, the integration will include the workspace icon.
2. Click **Create a ticket**.
3. Complete the fields in the Create new ticket form.

   External users will not
   see the **Assignee** field.
4. Click **Submit**.

   The ticket is created in Support and added as a reply to the
   Slack thread.

## Viewing tickets created in Slack

To filter tickets created by the Slack integration, you can leverage the
**created\_from\_slack** tag, which is automatically added to tickets created using the
[global shortcut](#topic_sk3_cc5_1tb) or [Slack action](#topic_rlf_fd5_1tb).

To do that, create a new view in Zendesk Support that filters tickets based on
tags. See [Adding views](https://support.zendesk.com/hc/en-us/articles/4408888828570#topic_vcr_xfp_ec).

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/slack_support_tickets_view.png)

## Adding internal notes to existing tickets in Slack

You can add an internal note (also called a private comment) to an existing ticket in Slack
from the ticket's notification thread. Only other Zendesk agents can view a ticket's
internal notes.

You can add an internal note directly from the original ticket notification or by replying
to the notification in Slack and converting the reply to a comment.

**To add an internal note to a ticket**

1. In Slack, hover over the ticket notification or reply message to display the
   options.
2. Click the **More actions** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_options_icon.png)) to display the message actions.
3. Click **Add as internal note**.
4. Add your comment in the **Internal note** field.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/slack_internal_note_2.png)
5. Complete the fields for the internal note. Depending on how you created the note, some
   fields may be pre-populated from the message or the ticket.
6. Click **Submit**.

   An internal note is added to the Zendesk Support ticket, and a
   new notification is added to the original notification thread.

## FAQ

This FAQ covers the following questions about using the Slack for Zendesk Support
integration.

### Why is the Requester field on tickets created via the integration set to the person who installed the integration?

If the Requester field is left blank on a Zendesk ticket created in Slack, or if there
were issues with setting the value in that field, the Requester is set to the user who
authenticated to Zendesk during the installation process.

### Can attachments be included in the ticket notification in Slack?

Comment attachments aren't currently included in the notification in Slack, but light
agents can click on the ticket link to see them in Zendesk. Inline images and image links
included in the comment are posted to Slack.

### Can I close tickets from Slack?

You cannot currently close tickets using Slack.

### Can I edit ticket fields in Slack?

You cannot currently edit ticket fields in Slack, but they can be edited from your
Zendesk Support account.

### If I create a new ticket from Slack, can other users on the channel see it?

Anyone in the channel can see tickets created in the channel.

### Can I create a ticket in a direct conversation with the Zendesk app, and will other users see it?

Yes, you can. The notification is posted back to you. Other channels on your Slack
account may be configured to receive ticket notifications and could also see your ticket
notification.

### Can I assign a ticket to a Zendesk user instead of a group?

No, the integration only allows tickets to be assigned to a group.

### Can external users create Support tickets in Slack Connect?

Users from external workspaces in Slack Connect channels cannot access the global
shortcut command. They can create tickets in channels where the Zendesk Slack app has been
added by tagging the app.