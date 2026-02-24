# Using Microsoft Teams in side conversations

Source: https://support.zendesk.com/hc/en-us/articles/5191537451290-Using-Microsoft-Teams-in-side-conversations

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Collaboration add-on |

Side conversations are spaces in a ticket where agents can have a conversation
with a specific group of people, or discuss a specific area of concern or
course of action. Side conversations are available in email, Slack, and as
child tickets.

As an alternative, you can use side conversations in a ticket to initiate and
participate in Microsoft Teams threads in channels. The Microsoft Teams side
conversations you initiate can be viewed in the ticket and the Microsoft
Teams application. Like email, Slack conversations, and child tickets,
Microsoft Teams side conversation messages are recorded as ticket events.
You can also use them as trigger conditions.

This feature is available only if an admin has [installed](https://zendeskforteams.com/installation-guide) the latest version of [Zendesk for Microsoft Teams](https://www.zendesk.com/marketplace/apps/support/767198/microsoft-teams-for-support/)
and [activated side
conversations](https://support.zendesk.com/hc/en-us/articles/4408832279962-Enabling-and-disabling-side-conversations).

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/side_convo_MS_teams_and_support.png)

This article includes these topics:

- [Creating a side
  conversation with Microsoft Teams](#topic_mt1_rng_gfb)
- [Adding attachments
  to a Microsoft Teams side conversation](#topic_gbv_2r1_vvb)
- [About limitations
  and breaking the link between Support and Microsoft
  Teams](#topic_kk5_rng_gfb)

Related articles:

- [About side
  conversations](https://support.zendesk.com/hc/en-us/articles/4408844206746)

## Creating a side conversation using Microsoft Teams

You can create a side conversation with Microsoft Teams from within
Support.

**To create a side conversation using Microsoft Teams**

1. In a ticket, open the [context panel](https://support.zendesk.com/hc/en-us/articles/4408836526362)
   and click the **Side conversations** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_omnipanel_side_conversations.png)) icon, then click the plus
   sign (+).
2. Select **Microsoft Teams** as the conversation
   type.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/side_convo_select_MS_teams.png)
3. Enter the Microsoft Teams’ team, channel, and your message. You
   can also add ticket comments.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/side_convo_MS_teams_send.png)

   For more information about the
   composer, see [Rich text editing
   in the side conversation
   composer](https://support.zendesk.com/hc/en-us/articles/4604347676954#topic_llv_sl1_rnb).

   You can start a side
   conversation in one team and channel at a time. You
   can't combine Microsoft Teams, Slack, and email
   conversations.

   If you have a lot of teams and
   channels, it may take a few moments to display the
   list. The Team appears before the channel address,
   for example, Team 1 - General, Team 2 - General, and
   so on.
4. When you’ve finished composing your message, click **Send**.

   Anyone in the Microsoft Teams channel
   can view your message and reply to the thread
   directly, without logging into Zendesk Support.

   Microsoft Teams replies are
   automatically included in the ticket’s side
   conversation. The conversation can continue back and
   forth, as long as necessary, until you get the
   information you need.
5. When the side conversation is complete, click **Done**.

   Note:
   This action is not reflected in the Microsoft Teams
   application.

## Adding attachments to a Microsoft Teams side conversation

You can add attachments to a side conversation from the Microsoft Teams
application by using the bot that appears at the beginning of a
conversation. Using the bot allows attachments to appear in both
Support and Microsoft Teams.

Note: Attachments sent directly in the Microsoft Teams side conversation do
not appear in the ticket’s side conversation in Support. Likewise,
attachments sent directly in Support do not appear in the Microsoft
Teams side conversation.

**To add attachments to side conversations from Microsoft Teams**

1. In Microsoft Teams, open a side conversation.
2. Scroll up to the beginning of the conversation where the bot
   first responded.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/side_convo_MS_teams_attachment.png)
3. Click **Click here** and upload the file you want to
   attach.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Side_convo_MS_Teams_upload_attachment.png)
4. Click **Upload files**.

## About limitations and breaking the link between Support and Microsoft Teams

Note the following limitations when using Microsoft Teams side
conversations:

- **Deleting messages**: You can’t delete a message
  from a Microsoft Teams side conversation.
- **Attachments**: Attachments sent directly in the
  Microsoft Teams side conversation do not appear in
  the ticket’s side conversation in Support. Likewise,
  attachments sent directly in Support do not appear
  in the Microsoft Teams side conversation. For
  attachments to appear in both Support and Microsoft
  Teams, see [Adding attachments to a Microsoft
  Teams side conversation](#topic_gbv_2r1_vvb).

The following Microsoft Teams features are not supported:

- Direct messages

  As a workaround, the administrator
  can set up separate channels with only one member (for example, “Team Finance Experts – Support”) and add the Zendesk for Microsoft Teams app to this team.
- Microsoft Teams @mentions
- Emoji reactions
- Typing indicators

If the link breaks between Zendesk and Microsoft Teams (for example, an admin removes the Zendesk app from a Microsoft Teams channel or archives or deletes a Microsoft Teams channel that you used for side conversations), you can still open and view these side conversations in a ticket, but you can no longer use that Microsoft Teams channel to send or receive updates to side conversations.

If you're experiencing issues with the Microsoft Teams app, contact [Softserve](https://zendeskforteams.com/), a third-party group which
owns the Microsoft Teams functionality.

If you experience ongoing problems using side conversations with
Microsoft Teams, you can choose to **Allow dynamic subdomain
detection**. Activating this setting can negatively impact
the performance of side conversations in Microsoft Teams, and is
only recommended when standard troubleshooting does not resolve
issues that prevent proper function. See [Activating and configuring
side conversations](https://support.zendesk.com/hc/en-us/articles/4408832279962).