# Configuring the live chat for returning customers conversational style

Source: https://support.zendesk.com/hc/en-us/articles/6088999921434-Configuring-the-live-chat-for-returning-customers-conversational-style

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

Live chat with a returning customer is similar to the live chat-type conversation, but
has a gap between solving a ticket and closing it. This enables the end user to return
to the conversation within a set period of time to reopen the ticket and continue
discussing the original topic.

Before configuring this conversational style you will need to decide the length
of time you want to wait before marking the solved ticket as closed. The length of time
you decide on will depend on the type of query you are handling, the nature of your
business and how likely it is that the customer will return to continue a conversation
on the same issue.

To configure the live chat for returning customers conversation style for messaging,
you'll need to create an automation that performs the following actions:

1. Looks for tickets with a status category of **Solved**, the channel
   **Messaging**, and the number of hours since the ticket status category
   was solved, in this case, one business hour.
2. Set that ticket status category to **Solved**.

Before you start, read [Conversational styles in messaging](https://support.zendesk.com/hc/en-us/articles/6088892450586) for an overview of each
conversational style.

This article contains the following sections:

- [Creating the automation](#topic_ydm_drz_pyb)
- [More information](#topic_il5_pzy_pyb)

## Creating the automation

Use the following procedure to create an automation that changes the status category
of solved messaging tickets that have been open for more than one business hour to
**Closed**.

**To create the automation**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Business rules >
   Automations**.
2. Select **Add Automation**.
3. Enter **Live chat returning customer conversation style** as a **Name**
   for your trigger.

   Tip: To help organize your triggers, you can [create a category](https://support.zendesk.com/hc/en-us/articles/4408834781594) that groups
   this type of triggers.
4. Click **Add condition**.
5. Configure the following two conditions:
   - **Ticket > Status category** > **Is** > **Solved**
   - **Ticket > Channel** > **Is** > **Messaging**
   - **Ticket: Hours since status category solved** > **(business)
     greater than** > **1**

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/lccs4.png)
6. Click **Add action** to configure what happens when the trigger conditions
   are met.
7. Configure the following action:

   - **Ticket > Status category** > **Closed**
   - ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/lccs5.png)
8. When you are finished, click **Create automation**.

Now, when tickets have a status category of **Solved**, are in the **Messaging**channel, and have been solved for more than one hour, the ticket status catefory
is set to **Closed**.

Tip: To apply the live chat for returning customers conversational style
to specific types of tickets, you'll need to add additional conditions to be
added to this trigger.

## More information

- [Conversational styles in
  messaging](https://support.zendesk.com/hc/en-us/articles/6088892450586)
- [Configuring the live chat conversational
  style](https://support.zendesk.com/hc/en-us/articles/6088983050138)
- [Configuring the social messaging
  conversational style](https://support.zendesk.com/hc/en-us/articles/6089032137754)