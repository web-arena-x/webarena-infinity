# Creating chat triggers

Source: https://support.zendesk.com/hc/en-us/articles/4408884148762-Creating-chat-triggers

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Support with** | Live chat and messaging Team, Professional, or Enterprise |

Chat triggers allow you to set up automated actions when certain conditions are met for
live chat interactions with users.

This article contains the following sections:

- [Essential facts about chat triggers](#topic_dlz_vrt_rdc)
- [Creating chat triggers](#topic_qxj_czx_zhb)

Related articles:

- [Zendesk chat triggers conditions and actions
  reference](https://support.zendesk.com/hc/en-us/articles/4408842880282)
- [Editing and managing chat
  triggers](https://support.zendesk.com/hc/en-us/articles/8554265015322)

## Essential facts about chat triggers

In addition to the [essential facts that are true of all Zendesk
triggers](https://support.zendesk.com/hc/en-us/articles/4408822236058#topic_xzp_zsq_4bc), consider the following information specific to chat
triggers:

- In addition to conditions and actions, chat triggers also contain a run event
  that determines when the trigger runs on live chats.
- Chat triggers don't fire when:
  - No agents are online.
  - Every agent's [availability status](https://support.zendesk.com/hc/en-us/articles/4408828519706) is set to
    *Invisible*.

### Example chat trigger

The following example is a chat trigger that sends a message to users visiting
your product's pricing page.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/new_chat_trigger_page.png)

## Creating chat triggers

Chat triggers are created on the Chat dashboard.

**To create a chat trigger**

1. From the Chat dashboard, select **Settings > Triggers**.
2. Click **Add trigger**.
3. Enter a name and brief description for your trigger.
4. Click **Enabled** at the top to enable your trigger.
5. If the trigger should fire only once per individual, select the **Each visitor
   will receive this message only once** check box. Deselect this box if you
   want the trigger to fire every time an individual meets the trigger
   conditions.
6. In the Customize Trigger section, use the **Run trigger** drop-down to select
   one of the following events that should fire the trigger:

   - Select **When a visitor has loaded the chat widget** if you want
     the trigger to run when the chat widget appears on the page, but the
     visitor has not interacted with it.
   - Select **When a visitor requests a chat** if you want the trigger
     to run when the visitor has requested a chat.
   - Select **When a chat message is sent** if you want the trigger to
     run when the visitor has entered and sent text in the chat
     widget.
7. Under **Check conditions**:

   - Select **Check all of the following conditions** if you want
     every condition you create to be met before the trigger is
     fired.
   - Select **Check any of the following conditions** if you want one
     or more of the conditions you create to be met before the trigger is fired.

     Note: You cannot use a combination of **Check all of the
     following conditions** and **Check any of the
     following conditions** when creating a Chat trigger.
     You can only select one option or the other. This is also
     not possible in Developer view.
8. Select actions under **Perform the following actions**. To add placeholders,
   type @.
9. Click **Create triggers**.

When the trigger is created and enabled, a check mark appears in the Enabled column
on the Triggers settings page.

Note: If you have multiple triggers that must be executed in a certain order, you need
to add at least one second of wait time between each trigger. This is required due
to the fact that triggers do not run in a particular order and are evaluated and
executed simultaneously.