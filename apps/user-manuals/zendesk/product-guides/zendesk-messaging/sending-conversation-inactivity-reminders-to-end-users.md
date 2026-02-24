# Sending conversation inactivity reminders to end users

Source: https://support.zendesk.com/hc/en-us/articles/9496171412378-Sending-conversation-inactivity-reminders-to-end-users

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Live chat and messaging Team, Professional, or Enterprise |

Verified AI summary ◀▼

Admins can set up inactivity reminders to notify end users when a conversation becomes inactive. You can configure up to three reminders, adjust wait times, update ticket statuses, and add tags. These reminders help manage conversations across Web Widget, iOS and Android SDKs, and supported social channels. Customize messages and use tags in business rules and reporting to enhance support operations.

Admins can configure up to three reminders to be sent to end users when their messaging
conversation becomes inactive, and tag conversations when reminders are sent.
Configuration options for inactivity reminders are part of the [capacity release settings](https://support.zendesk.com/hc/en-us/articles/7043034053658) in Admin Center.

Note: For accounts created after May 19, 2025, the capacity release and inactivity
reminder settings are turned on by default. Reminder tags are turned on by default
for accounts created after October 16, 2025. Accounts created before these dates
will need to turn these features on before they can configure these settings.

This article includes the following sections:

- [About inactivity reminders](#topic_yym_4vd_1gc)
- [Configuring inactivity reminders](#topic_kc1_mzd_1gc)

## About inactivity reminders

For newer messaging accounts, inactivity reminders are turned on and configured by
default for the Web Widget, iOS and Android SDKs, and Zendesk-supported social
messaging channels. The default configuration sends three reminders with simple
message text in the account’s [default language](https://support.zendesk.com/hc/en-us/articles/4408887059866#topic_rtc_42j_1y), and adds tags to a
conversation. You can keep these default settings or customize them as needed.

By default:

- The **First reminder** is sent after five minutes of end-user inactivity.
  This reminder updates the ticket’s status to Pending, and adds the tag
  *messaging\_reminder\_1* to the conversation.
- The **Second reminder** is sent after another five minutes of end-user
  inactivity. This reminder does not update the ticket’s status, but adds the
  tag *messaging\_reminder\_2* to the conversation.
- The **Third reminder** is sent after one additional minute of end-user
  inactivity. This reminder updates the ticket’s status to Solved, and adds
  the tag *messaging\_reminder\_final* to the conversation.
- The [messaging session does not end
  automatically](https://support.zendesk.com/hc/en-us/articles/8009788438042) when a ticket becomes inactive.

Note: For accounts created before October 16, 2025, there are no default tags.
You’ll need to add tags in the Tags field to include them with inactivity
reminders.

Consider the following when using inactivity reminders:

- You must be an admin to configure inactivity reminders.
- Inactivity reminders are available for the Web Widget, iOS and Android SDKs,
  and Zendesk-supported social messaging channels.
- It can take up to 10 minutes for updates to the inactivity reminder setting
  to begin working.
- If an AI agent is in use, inactivity reminders are sent to end users from
  that AI agent, and the [avatar and bot name](https://support.zendesk.com/hc/en-us/articles/6447066520986) associated
  with it are displayed with the reminder message. If no AI agent is in use,
  the [logo associated with the Web
  Widget](https://support.zendesk.com/hc/en-us/articles/4500747797914#topic_ubc_nmd_btb) appears with the message.
- Reminder tags can be used in business rules, views, reporting, and as [conditions in messaging triggers](https://support.zendesk.com/hc/en-us/articles/8015292388378).
  See [About tags](https://support.zendesk.com/hc/en-us/articles/4408888664474) for more
  information.

## Configuring inactivity reminders

You can set up inactivity reminders when you [configure your messaging capacity release settings](#topic_mfm_prq_1bc), or
update the setting at a later date.

**To customize your inactivity reminder settings**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Messaging and social >
   Messaging**.
2. Click **Messaging settings**.
3. Under **Advanced**, expand the **Capacity release** section.
4. Under **Remind customers about inactive conversations**, select **1
   reminder**, **2 reminders**, or **3 reminders**. Subsequent
   reminder settings are displayed based on this selection.

   To turn off
   inactivity reminders, select **Do not remind**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/auto-release_capacity-reminders.png)

   Note: If you selected Solved as
   the ticket status for [the initial inactivity
   period](https://support.zendesk.com/hc/en-us/articles/7043034053658#topic_mfm_prq_1bc), you will only be able to select **Do not
   remind** or **1 reminder**.
5. Select **End messaging session after last reminder is sent** to automatically [end the messaging session](https://support.zendesk.com/hc/en-us/articles/8009788438042) when the
   ticket becomes inactive.
6. Configure the reminders’ messages, inactivity periods, ticket status
   changes, and tags as needed:

   Note: You can use [dynamic content](https://support.zendesk.com/hc/en-us/articles/4408882999066) in reminder
   messages to automatically translate or customize the messages for end
   users.

   - **First reminder**:
     - Enter the message you want to send when the initial
       inactivity period is reached, or use the default message.
       This reminder uses the wait time and ticket status
       configured for the [initial messaging capacity release
       settings](#topic_mfm_prq_1bc).
     - Update the tag or add additional tags as needed. Clear the
       Tags field to prevent tags from being added to the ticket.
   - **Second** and **Third reminders** (if applicable):
     - Enter a whole number between 1 and 15 for the **Wait time
       after previous reminder** in minutes.
     - Enter the message you want to send.
     - Enter the status change you want to apply to the ticket when
       each subsequent inactivity period is reached. You can select
       No change, Pending, On-hold, Solved, or a custom status
       mapped to these ticket status categories. Note that support
       [ticket triggers](https://support.zendesk.com/hc/en-us/articles/4408886797466)
       using the selected ticket status as a condition will fire
       when the status is applied.
     - Update the tag or add additional tags as needed. Clear the
       Tags field to prevent tags from being added to the ticket.

     Note: The second and third reminders aren't sent if an agent
     solves the ticket after the first reminder.
7. Click **Save settings**.