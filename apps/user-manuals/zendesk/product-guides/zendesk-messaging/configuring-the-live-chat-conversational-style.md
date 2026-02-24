# Configuring the live chat conversational style

Source: https://support.zendesk.com/hc/en-us/articles/6088983050138-Configuring-the-live-chat-conversational-style

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

Live chat is a real-time conversation between an end user and an agent, with a related
ticket that closes immediately (or close to it) after it is solved.

To configure the live chat conversation style for all tickets, you'll need to create a
trigger that performs the following actions:

1. Look for tickets with the status category of **Solved** and the channel
   **Messaging**.
2. Change the ticket status category to **Closed**.

This style works best in conversations where the AI agent doesn't need a lot of
clarification or information from the user. If there is a lot of back-and-forth, the
trigger could possibly solve the ticket before the conversation is finished, resulting
in the user not seeing AI agent replies and starting a new ticket when they return to
the widget.

Before you start, read [Conversational styles in messaging](https://support.zendesk.com/hc/en-us/articles/6088892450586) for an overview of each
conversational style.

This article contains the following sections:

- [Creating the trigger](#topic_dhb_rdz_pyb)
- [More information](#topic_il5_pzy_pyb)

## Creating the trigger

Use the following procedure to create a trigger that changes the status category of
solved messaging tickets to **Closed**.

**To create the trigger**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Business rules >
   Triggers**.
2. Click **Add trigger**.
3. Enter **Live chat conversational style** as a **Name** for your
   trigger.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/lccs-1.png)

   Tip: To help organize your triggers, you can [create a category](https://support.zendesk.com/hc/en-us/articles/4408834781594) that groups
   this type of triggers.
4. Click **Add condition**.
5. Configure the following two conditions:
   - **Ticket > Status category** > **Is** > **Solved**
   - **Ticket > Channel** > **Is** > **Messaging**

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/lccs-2.png)
6. Click **Add action** to configure what happens when the trigger conditions
   are met.
7. Configure the following action:

   - **Ticket > Status category** > **Closed**

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/lccs-3.png)
8. When you are finished, click **Create**.

Now, when tickets have a status category of **Solved** and are in the **Messaging**channel, their status category will automatically be set to **Closed**.

Tip: To apply the live chat conversational style to specific types of tickets, you'll
need to add additional conditions to this trigger.

## More information

- [Conversational styles in
  messaging](https://support.zendesk.com/hc/en-us/articles/6088892450586)
- [Configuring the live chat for returning
  customers conversational style](https://support.zendesk.com/hc/en-us/articles/6088999921434)
- [Configuring the social messaging
  conversational style](https://support.zendesk.com/hc/en-us/articles/6089032137754)