# Automatically releasing agent capacity for inactive messaging conversations

Source: https://support.zendesk.com/hc/en-us/articles/7043034053658-Automatically-releasing-agent-capacity-for-inactive-messaging-conversations

---

Configuring the automatic release of an agent’s messagingcapacityallows admins to specify how long a conversation can remain active without input from an end user before it’s considered inactive. Depending on youromnichannel routing configuration, marking a conversation as inactive can remove the ticket from an agent’s capacity, allowing another conversation to be routed to them without requiring them to manually update the ticket status.

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

Configuring the automatic release of an agent’s messaging [capacity](https://support.zendesk.com/hc/en-us/articles/4776409839770) allows admins to specify how long a conversation
can remain active without input from an end user before it’s considered inactive.
Depending on your [omnichannel routing configuration](https://support.zendesk.com/hc/en-us/articles/4828787357210), marking a conversation as
inactive can remove the ticket from an agent’s capacity, allowing another conversation
to be routed to them without requiring them to manually update the ticket status.

This article describes how admins can configure the auto-release capacity
settings, including the inactivity period and the ticket and messaging session status
when a ticket becomes inactive. Additionally, admins can [send up to three reminders](https://support.zendesk.com/hc/en-us/articles/9496171412378) to end users when their
conversation becomes inactive.

This article contains the following topics:

- [About active and inactive messaging tickets](#topic_d1b_hpz_1bc)
- [Considerations when using the capacity release settings](#topic_fr2_prq_1bc)
- [Configuring the auto-release capacity setting](#topic_mfm_prq_1bc)

## About active and inactive messaging tickets

In conversational support, there’s a concept of active and inactive tickets.

- **Active tickets** are those with recent responses from the end user.
- **Inactive tickets** are those that haven’t had a response from the end
  user in a specified period, or that have a status other than *New* or
  *Open*. By default, Zendesk defines a messaging ticket as inactive
  when an end user hasn’t sent a reply in the last 10 minutes.

  Note: The
  capacity release settings, including the inactivity period, apply only
  to messaging conversations already assigned to agents. All unassigned
  messaging conversations have a default inactivity period of 10
  minutes.

The ticket’s activity classification, as well as the ticket status applied to
it, can impact routing, business rules, and an agent’s [capacity](https://support.zendesk.com/hc/en-us/articles/4776409839770).

## Considerations when using the capacity release settings

Consider the following when turning on and configuring the automatic
release of agent capacity:

- If you don’t use the auto-release capacity settings, Zendesk applies a
  default inactivity period of 10 minutes without a response from the end
  user.
- The auto-release capacity settings are applied to all open messaging tickets
  currently assigned to agents and to those that are created or reopened after
  these settings are saved.
- When using the default inactivity period and the [messaging activity routing](https://support.zendesk.com/hc/en-us/articles/4828787357210#topic_glj_pmr_wbc) setting
  for omnichannel routing is turned off, a messaging ticket no longer counts
  towards an agent’s capacity when it becomes inactive, but the ticket's
  status doesn’t change.
- [Inactivity reminders](https://support.zendesk.com/hc/en-us/articles/9496171412378) are available
  for the Web Widget, iOS and Android SDKs, and Zendesk-supported social
  messaging channels.
- The auto-release capacity setting provides a powerful way to manage agent
  capacity when used with omnichannel routing, but can also be used
  effectively with other business rules that rely on changes in ticket status.
- You must be an admin to configure the auto-release capacity setting.
- To avoid any unexpected behavior, we recommend turning on the auto-release
  capacity setting during a low-volume time.
- It can take up to 10 minutes for updates to the auto-release capacity
  setting to begin working.
- If an AI agent is in use, inactivity reminders are sent to end users from
  that AI agent, and the [avatar and bot name](https://support.zendesk.com/hc/en-us/articles/6447066520986) associated
  with it are displayed with the message. If no AI agent is in use, the [logo associated with the Web
  Widget](https://support.zendesk.com/hc/en-us/articles/4500747797914#topic_ubc_nmd_btb) appears with the message.

## Configuring the auto-release capacity setting

Admins can use the auto-release capacity setting to help agents manage their capacity
and help end users remember to keep a conversation active if they want. These
settings can also help business rules, such as triggers, to run more effectively on
tickets because they alter the ticket status when a conversation becomes inactive.
The change in ticket status is captured in the ticket’s audit events:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/auto-release_capacity_event-aw.png)

When [omnichannel routing is configured *not* to
count inactive conversations toward agent capacity](https://support.zendesk.com/hc/en-us/articles/4828787357210#topic_glj_pmr_wbc), the capacity release
settings can increase efficiency by automatically releasing an agent's capacity
without requiring them to manually alter the ticket's status.

Auto-release capacity and inactivity reminders are turned on and configured by
default. The default configuration sends three reminders with simple message
text.

- The initial reminder is sent after five minutes of end-user
  inactivity, and updates the ticket’s status to Pending.
- The second reminder is sent after another five minutes of end-user
  inactivity, and does not update the ticket’s status.
- The third and final reminder is sent after one additional minute of
  end-user inactivity, and updates the ticket’s status to Solved.

You can keep these default settings, customize them, turn off reminders, or
turn off automatic capacity release.

Note: For accounts created after May 19, 2025, the auto-release capacity setting is
turned on by default. Accounts created before this date need to turn on
automatic capacity release before they can configure this setting and the [inactivity reminders](https://support.zendesk.com/hc/en-us/articles/9496171412378).

**To customize the messaging capacity release settings**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Messaging and social >
   Messaging**.
2. Click **Manage settings**.
3. In the Advanced section of the Messaging settings page, click **Capacity
   release**. Make sure **Turn on auto-release capacity** is
   selected.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/auto-release_capacity.png)
4. Under **Inactivity period**, enter a whole number from 3 to 15. This is
   the time in minutes a conversation can go without a reply from an end user
   before it is considered active. This time is measured from any agent’s last
   sent message after the initial ticket assignment. If the agent sends
   multiple messages, the time is counted based on the first message the agent
   sent after the last message from the end user.
5. Under **Ticket status for inactive conversations**, select a status to
   automatically apply to inactive tickets. You can select Pending, On-hold,
   Solved, or a [custom status](https://support.zendesk.com/hc/en-us/articles/4412575861018) mapped to these
   ticket status categories. New and Open statuses can’t be used. Triggers
   using the selected status as a condition will fire when the new status is
   applied.
6. Under **Remind customers about inactive conversations**:

   - Select **Do not remind** if you *don't* want to send any
     messages to end users when a conversation becomes inactive.
     Select **End messaging session after conversation becomes
     inactive** to automatically [end the messaging
     session](https://support.zendesk.com/hc/en-us/articles/8009788438042).
   - Select the number of reminders (up to three) you want to send to
     end users before a conversation becomes inactive. See [Sending conversation
     inactivity reminders to end users](https://support.zendesk.com/hc/en-us/articles/9496171412378) for more
     information about using this setting.

   Note that if you select Solved as the ticket status for the initial
   inactivity period, you will only be able to select **Do not remind**
   or **1 reminder**.
7. Click **Save settings**.