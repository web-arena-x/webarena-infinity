# Creating messaging triggers

Source: https://support.zendesk.com/hc/en-us/articles/6058753945242-Creating-messaging-triggers

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

Verified AI summary ◀▼

Create messaging triggers to automate actions based on customer interactions in messaging channels. Set conditions using user, conversation, or agent data, and specify actions like sending automated messages. Only admins can create and manage these triggers. Customize triggers using a visual tool or JSON, and define events and conditions to tailor responses to customer needs.

Messaging triggers run when a customer requests or interacts with a conversation through a native or social messaging channel.

Conditions can include user data (like account status), conversation data (such as the time of day a conversation is started), and agent data (such as queue size). When conditions are met, the triggers fire and perform the specified actions through that same messaging channel (such as sending an automated message to the conversation).

In addition to the [standard messaging triggers](https://support.zendesk.com/hc/en-us/articles/8567613882522), admins can create custom messaging triggers.

## Creating messaging triggers

Messaging triggers are created on the [Messaging trigger page](https://support.zendesk.com/hc/en-us/articles/5973077601562#topic_w1p_vpn_q5b)
in Admin Center.

Note: Only admins can create and manage messaging triggers. Even if agents have a custom role with trigger management permissions, they cannot create or manage messaging triggers.

**To create a messaging trigger**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Business rules > Messaging triggers**.
2. Click **Create trigger**.
3. Enter the basic information for your new trigger:

   - **Name**. Use a consistent naming convention to help you recognize similar types of triggers.
   - **Description** (optional). You can provide details about what the trigger does for other agents and admins. You'll be able to search for triggers based on description.
   - **Channels**: Enter the Zendesk messaging or social channels you want to apply the trigger to. *Web Widget & SDKs* is included by default. Click the X to remove it from the Channels list.
   - **Activate this trigger**. Select this option if you want the trigger to be active immediately after creating it.
   - **Run only once per ticket**. Select this option if you want the trigger to run on the ticket *only* the first time the conditions are met.
4. Select **Visual** to build the trigger using the visual editing tool, or **Developer** to edit trigger definitions directly in JSON format.
5. Use the **Run trigger** drop-down to determine the event that initiates the trigger. The trigger is not acted upon unless the conditions are met.

   - **When a customer requests a conversation** initiates the trigger when the conversation is passed to an agent.
   - **When a message is sent** initiates the trigger when a customer sends a comment in an existing conversation.
   - **When a conversation is added to a queue** initiates the trigger when a messaging conversation is assigned to the queue.
   - **When a conversation is assigned from the queue** initiates the trigger when a messaging ticket is assigned to an agent from the queue.
     Only applies when the agent clicks the [Accept button](../../agent-guide/additional-ticket-channels/receiving-and-sending-messages-in-the-zendesk-agent-workspace.md#topic_fzy_pxj_2mb) or when the ticket is [auto-assigned](https://support.zendesk.com/hc/en-us/articles/5020833543450); does not apply when an agent reassigns a ticket to another agent, or when an agent claims a ticket from a group view.
6. Create at least one **condition**:
   - Choose whether the trigger must meet **All** or **Any** of the conditions before it is run.
   - Select a **Condition**, **Field operator**, and **Value** for each condition you add.

     The field operator determines the relationship between the condition and the value. For example, if you select the field operator "Is", your condition will need to be equal to the value. Different conditions will contain different field operators.
   - Click **Add condition** and repeat these steps if needed.

     Note: Only conditions that apply to all selected channels appear in the Select conditions drop-down. When creating a trigger that applies to social channels, device metadata is not available.
7. Create at least one **action**:
   - Select an **Action**, then enter the **action information**.

     The required information is determined by the action selected. For example, if you select *Wait*, you’ll need to enter the time (in seconds) before the next action is performed, or the next trigger fires.
   - Click **Add action** and repeat these steps if needed.

     Note: Only actions that apply to all selected channels appear in the Select action drop-down.
     When creating a trigger that applies to social channels, the Request email action is not available.
8. Click **Create**.

Once created, the trigger is listed on Messaging triggers admin page and can be [modified](https://support.zendesk.com/hc/en-us/articles/8567642504090) as needed.