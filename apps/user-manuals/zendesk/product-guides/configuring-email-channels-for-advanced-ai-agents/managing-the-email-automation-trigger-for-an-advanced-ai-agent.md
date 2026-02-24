# Managing the email automation trigger for an advanced AI agent

Source: https://support.zendesk.com/hc/en-us/articles/9985221852954-Managing-the-email-automation-trigger-for-an-advanced-AI-agent

---

As part ofconnecting an advanced AI agent to email, you create an automation trigger that controls how the AI agent responds to customer requests on the email channel. After you create this trigger, you can manage it in Admin Center.

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | AI agents - Advanced |

As part of [connecting an advanced AI agent to email](https://support.zendesk.com/hc/en-us/articles/8357750858010), you
create an automation trigger that controls how the AI agent responds to customer
requests on the email channel. After you create this trigger, you can manage it in Admin
Center.

This article contains the following topics:

- [About the email automation trigger](#topic_qz2_jgt_khc)
- [Reordering the email automation trigger](#topic_blx_jgt_khc)
- [Editing the email automation trigger](#topic_ahn_kgt_khc)

## About the email automation trigger

When you create the automation trigger for an advanced email AI agent, the trigger
has the following default configuration:

- **Meet ALL of the following conditions**:
  - **Ticket > Comment** | **Is** | **Public**

    This condition
    ensures that the AI agent is notified of each customer, agent, or AI
    agent reply.
  - **Ticket > Channel** | **Is** | **Email**

    This condition
    ensures that the AI agent is notified for comments on the email
    channel only.
  - ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_email_automation_trigger_meet_all.png)
- **Meet ANY of the following conditions**:
  - **Ticket > Ticket** | **Is** | **Created**

    This condition
    ensures the AI agent responds to the first comment in a ticket.
  - **Ticket > Ticket** | **Is** | **Updated**

    This condition
    ensures the AI agent responds to subsequent comments in a
    ticket.

    ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_email_automation_trigger_meet_any.png)
- **Actions**
  - **Category**: Notify by > Active webhook
  - **Value**: Ultimate.ai Automation Webhook: <your AI agent ID>
  - **Endpoint**:
    https://zendesk-support-automation.us.ultimate.ai/v1/webhook
  - **Method**: POST
  - JSON
    body:

    ```
    {"botId": "YOUR_AI_AGENT_ID", 
    "message": "**{{ticket.title}}** \n\n 
    {{ticket.latest_comment_rich}}", 
    "conversationId": "{{ticket.id}}", 
    "type": "message", 
    "tags": "{{ticket.tags}}", 
    "channel": "{{ticket.via}}", 
    "requester": "{{ticket.requester.id}}", 
    "currentUser": "{{current_user.id}}", 
    "submitterRole": "{{ticket.submitter.role}}", 
    "authorRole": "{{ticket.comments.first.author.role}}",
    ```

    The
    JSON body includes details that allow the AI agent to ignore agent
    replies (though you can allow this if you want) and to not reply to
    tickets older than three days. The type is also changed for
    analytical purposes.

    ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_email_automation_trigger_actions.png)

## Reordering the email automation trigger

You can reorder your list of AI agent ticket triggers to designate the order they're
fired in. For more information on the overall impact this can have on your
workflows, see [Reordering triggers](https://support.zendesk.com/hc/en-us/articles/4408882237722#topic_vnl_zpy_tb).

**To reorder the email automation trigger**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Business rules >
   Triggers**.
2. Click **Edit order** in the upper-right.
3. Find the email automation trigger for your advanced AI agent.

   By default,
   this trigger is named *Ultimate.ai Multitouch Ticket Automation:
   <AI agent ID>*.
4. Click and hold the drag-and-drop handle (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/drag_and_drop_handle.png)) for the trigger, drag the trigger
   into position, and release the handle.
5. Click **Save**.

## Editing the email automation trigger

You can edit the email automation trigger as needed.

Some examples of edits you might want to make include:

- [Responding to agent-submitted tickets](#topic_xtw_wgt_khc)
- [Supporting the web form channel](#topic_hxh_vgt_khc)
- [Supporting the API channel](#topic_mt1_lgt_khc)
- [Removing the authorized user condition](#topic_gtd_cjc_h3c)

**To edit the email automation trigger**

1. In AI agents - Advanced, [select the advanced AI agent](https://support.zendesk.com/hc/en-us/articles/8357756913178#topic_t25_qvj_tdc) you want to
   work with.
2. Click **Settings** in the sidebar, then select **CRM integration**.
3. Select the **Integration** tab.
4. Click **Edit automation trigger**.

   The trigger’s configuration page
   opens in Admin Center.
5. Edit the trigger as necessary.
6. Click **Save**.

### Responding to agent-submitted tickets

By default, the email automation trigger is configured so that the AI agent
doesn’t respond to tickets submitted by agents. However, you might want to allow
this, especially during testing.

**To allow the AI agent to respond to agent-submitted tickets**

1. [Edit the email automation
   trigger.](#topic_ahn_kgt_khc)
2. Remove the following lines from the JSON
   body:

   ```
   "submitterRole": "{{ticket.submitter.role}}", 
   "authorRole": "{{ticket.comments.first.author.role}}",
   ```
3. Click **Save**.

### Supporting the web form channel

By default, the email automation trigger is configured to work only on the email
channel. However, you can add web form as a supported channel for your advanced
AI agent.

**To add the web form channel as a supported channel**

1. [Edit the email automation
   trigger.](#topic_ahn_kgt_khc)
2. Under **Meet ALL of the following conditions**, delete the following
   condition:
   - **Ticket > Channel** | **Is** | **Email**
3. Under **Meet ANY of the following conditions**, add the following
   conditions:
   - **Ticket > Channel** | **Is** | **Email**
   - **Ticket > Channel** | **Is** | **Web form**
4. Click **Save**.

Note: Don’t add a condition for the API channel here.
Instead, you must clone the email automation trigger to support the API
channel. See the section below.

### Supporting the API channel

By default, the email automation trigger is configured to work only on the email
channel. However, you can add API as a supported channel for your advanced AI
agent.

When using the Zendesk API, tickets are always created with the authentication
token’s owner’s ID as the currentUser. Because of this, the AI agent interprets
these created tickets as being agent-submitted, which it’s configured to ignore.
However, you can support the API channel by cloning the email automation trigger
and using the copy in addition to the default trigger.

When a conversation is created through the API, only the first message’s source
is marked as API, while the rest of the messages go through email. Because of
that, the trigger needs to cover only the Created event for these conversations.
Furthermore, the two triggers won’t overlap because the default trigger doesn’t
include API as a channel condition, while the copy does.

The JSON body provided below overwrites the currentUser field with this trigger
to contain the requester, making it look like it was submitted by a customer. So
both the requester and currentUser will be equal to {{ticket.requester.id}}.

**To clone the trigger and configure it to support the API channel**

1. In AI agents - Advanced, [select the advanced AI agent](https://support.zendesk.com/hc/en-us/articles/8357756913178#topic_t25_qvj_tdc) you want to
   work with.
2. Click **Settings** in the sidebar, then select **CRM integration**.
3. Select the **Integration** tab.
4. Click **Edit automation trigger**.

   The trigger’s configuration page
   opens in Admin Center.
5. Click **Actions** in the upper-right and select **Clone**.

   A
   copy of the automation trigger is created.
6. Under **Meet ALL of the following conditions**, delete the existing
   conditions and add the following conditions instead:
   - **Ticket > Channel** | **Is** | **Web service (API)**
   - **Ticket > Ticket** | **Is** | **Created**
7. Under **Meet ANY of the following conditions**, delete the existing
   conditions.
8. Under **Actions**, replace the existing JSON body with the
   following:

   ```
   { "botId": "<YOUR_AI_AGENT_ID>", 
   "message": "**{{ticket.title}}** \n\n 
   {{ticket.latest_comment_rich}}", 
   "conversationId": "{{ticket.id}}", 
   "type": "message", 
   "tags": "{{ticket.tags}}", 
   "channel": "{{ticket.via}}", 
   "requester": "{{ticket.requester.id}}", 
   "currentUser": "{{ticket.requester.id}}", 
   "submitterRole": "{{ticket.submitter.role}}", 
   "createdAt": "{{ticket.created_at_with_timestamp}}", 
   "updatedAt": "{{ticket.updated_at_with_timestamp}}" }
   ```
9. Click **Create trigger**.

### Removing the authorized user condition

If you created the email automation trigger before February 11, 2026, the trigger
configuration might include a condition for an authorized user. After this date,
an authorized user is no longer involved in the connection between an advanced
AI agent and the email channel. As a result, your email AI agent may not
function correctly if you still have this condition as part of your trigger.
This condition should be removed.

**To remove the authorized user condition**

1. [Edit the email automation
   trigger.](#topic_ahn_kgt_khc)
2. Remove the following condition:

   **Ticket details > Current user** |
   **Is** | **(agent)**

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_remove_authorized_user_condition.png)
3. Click **Save**.