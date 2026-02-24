# Managing chat triggers when migrating from Chat to messaging

Source: https://support.zendesk.com/hc/en-us/articles/4408822204698-Managing-chat-triggers-when-migrating-from-Chat-to-messaging

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

When you migrate from live chat to [messaging](https://support.zendesk.com/hc/en-us/articles/4408846454682) for Web Widget and mobile SDKs, new triggers are
created and a number of updates are made to existing triggers to accommodate the
functionality changes. If you do not update an existing trigger, these changes do not
impact its functionality for live chat.

For most accounts, messaging triggers are managed in Admin Center, while chat triggers
are still managed in the Chat dashboard.

This article includes the following topics:

- [Trigger changes when
  migrating from Chat to messaging](#topic_ot4_bmp_pnb)
- [About the messaging
  triggers](#topic_h3t_bmp_pnb)

For more information, see the following articles:

- [Creating chat triggers](https://support.zendesk.com/hc/en-us/articles/4408884148762)
- [When should I use bot builder and ticket
  triggers in messaging?](https://support.zendesk.com/hc/en-us/articles/5090634460826)

## Changes to your Chat triggers when migrating from Chat to messaging

Note: If you're using a conversation bot with your messaging configuration, chat
triggers fire on the first customer message after the conversation is handed off to
a live agent.

The basic way you work with chat triggers remains unchanged when you move
from Chat to messaging. You can view, edit, and add chat triggers from the main chat
triggers page, accessed from the Chat dashboard at **Settings > Triggers**.

However, you will see the following changes when viewing, adding, or
editing triggers through the Chat dashboard:

- The Channel drop-down field
- Updated Run trigger options
- Updated condition options
- Updated action options

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/chat_triggers_edit_page_messaging.png)

### The Channel field

When messaging is turned on for your account, a *channel* field is added to
the chat and messaging triggers. It's used to specify whether the trigger runs
on conversations originating from Chat, messaging, or both.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/chat_triggers_edit_page_messaging.png)

When you turn on messaging, the channel value is set to chat for all
existing chat triggers. This means the chat trigger options don't change, and
the trigger performs as described in our [standard Chat triggers documentation](https://support.zendesk.com/hc/en-us/articles/4408886127898).
However, if you edit an existing chat trigger or create a new trigger and select
either **Messaging** or **Chat and messaging**, subsequent trigger
customization options are modified to support messaging functionality
changes.

### Updated Run trigger options

When a chat trigger is configured to run for messaging or chat and
messaging, you can no longer choose to run the trigger *when a visitor has
loaded the Chat widget* because the Chat widget is not used in messaging.

Instead, you can choose from the following run events:

- When a visitor requests a chat
- When a visitor sends a chat message

### Updated condition options

When a chat trigger is configured to run for messaging or chat and
messaging, the conditions available to you change to the following:

- Hour of day
- Day of week
- Visitor previous chats
- Visitor name
- Visitor email
- Visitor triggered
- Account status
- Department status
- Visitor is chatting
- Visitor requesting chat
- Visitor served
- Department (Only available when Run trigger = A visitor requests a
  chat)
- Sender (Only available when Run trigger = When a chat message is
  sent)
- Sender type (Only available when Run trigger = When a chat message
  is sent)
- Message (Only available when Run trigger = When a chat message is
  sent)
- Queue size (account)

For a complete list of trigger conditions and descriptions, including those that
are not available for messaging, see [Zendesk Chat triggers conditions and actions
reference: Trigger conditions](https://support.zendesk.com/hc/en-us/articles/4408842880282#topic_d3p_q5f_rhb).

### Updated action options

When a chat trigger is configured to run for messaging or chat and messaging, the
actions available to you change to the following:

- Send message to visitor
- Set triggered (shown on dashboard)
- Wait
- Set name of visitor
- Block visitor

For a complete list of chat and messaging trigger actions, including those that
aren't available for messaging, see [Building chat and messaging trigger action
statements](https://support.zendesk.com/hc/en-us/articles/4408842880282#topic_hxz_q5f_rhb).

## Updating chat triggers to apply to messaging

There are three standard chat and messaging triggers that exist after messaging is
turned on for your account: [First
Reply](#topic_x4j_mhj_3rb), [Request Contact
Details](#topic_fc4_mhj_3rb), and [All Agents
Offline](#topic_fc4_mhj_3rb). By default, these apply only to live chats, but can be updated
to apply to messaging or live chats and messaging.

If you would like them to work with your messaging channel, you must edit the trigger
to modify which channels it applies to and ensure that the trigger is enabled.

**To update chat triggers to apply to messaging**

1. From the Chat dashboard, select **Settings > Triggers**.
2. From the list, click the row of the trigger you want to edit.
3. Change the **Channel** to either **Messaging** or **Chat and
   messaging**.
4. Next to **Trigger status**, select **Enable trigger**.
5. Make any other changes to the content of the trigger as needed to work with
   your messaging channel.

   Note: If a condition or action that is only available
   for the Chat channel is selected while the channel is set to
   *messaging* or *Chat and messaging*, you can't save your
   changes until you resolve the discrepancy.
6. Click **Save changes**.

### First Reply trigger

This trigger sends an automated reply to customers that request a chat, so they
know their request is being attended to.

When messaging is turned on for your account, the trigger is configured as
follows:

- **Run trigger: When a visitor requests a chat**
- **Check conditions: Check all of the following conditions**
  - **Visitor requesting chat | Is true**
- **Perform the following actions**
  - **Wait | 5** (in seconds)
  - **Send message to visitor | Customer Service | Thanks for your
    message, please wait a moment while our agents attend to
    you.**

### Request Contact Details trigger

When your account is set to away, this trigger asks customers requesting a chat
to leave their email address.

When messaging is turned on for your account, the trigger is configured as
follows:

- **Run trigger: When a visitor requests a chat**
- **Check conditions: Check all of the following conditions**
  - **Account status | Equals | Away**
- **Perform the following actions**
  - **Send message to visitor | Customer Service | Hi, sorry we are
    away at the moment. Please leave your email address and we will
    get back to you as soon as possible.**

### All Agents Offline trigger

When all agents are offline, this trigger send an automated reply to warn the end
user to expect a delayed response.

When messaging is turned on for your account, the trigger is configured as
follows:

- **Run trigger: When a chat message is sent**
- **Check conditions: Check all of the following conditions**
  - **Account status | Equals | Offline**
- **Perform the following actions**
  - **Send message to visitor | Automated Response | Hi there! Thanks
    for reaching out to us. We're offline right now, but we'll
    respond to your message when we're back online in a few
    hours.**