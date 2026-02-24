# Using text notifications with triggers: Recipes and tips

Source: https://support.zendesk.com/hc/en-us/articles/4408882005402-Using-text-notifications-with-triggers-Recipes-and-tips

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Talk Team, Professional, or Enterprise |

Important: You are responsible for using the call and text features in Zendesk in compliance with all applicable laws. Certain jurisdictions may require end-user consent prior to initiating telephonic outreach. By enabling these features, you agree that you have received the required consent.

Support your customers via SMS with text. With text, you and your team can get creative about finding new ways to help customers with notifications, updates and proactive texts.

For general information about triggers and text, see [Automating SMS support with text triggers](https://support.zendesk.com/hc/en-us/articles/4408885601178-Automating-SMS-support-with-Text-triggers-Talk-Basic-and-Advanced-).

This article contains the following topics:

- [Send automated text responses](#topic_ayx_dj3_xhb)
- [Alert agents when a ticket needs attention](#topic_etg_1j3_xhb)
- [Start a text conversation with proactive outbound texts](#topic_arl_s33_xhb)
- [Create a proactive ticket](#topic_qrf_j33_xhb)
- [Respond to texts within a new ticket](#topic_c2c_333_xhb)

## Send automated text responses

When customers submit a request, set up this trigger to automatically notify them you've received it. For example, you might want customers to receive a text that says "We've received your message! We'll get back to you shortly."

For this procedure to work, the customer's number needs to be in E.164 format like +14155551212.

If an end user has more than one phone number associated with their profile and you send them a text message, the message is sent to the first phone number that was added to their user profile. If you want text messages to be sent to another phone number, you’ll need to remove all phone numbers from the profile and re-add them, ensuring that the first phone number you add is the one you want text messages sent to.

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Business rules >
   Triggers**.
2. Click **Add trigger**.
3. Enter a title for your trigger, like “Auto response to inbound text.”
4. Add the following conditions and actions for your trigger (see screenshot below):
   - Meets all of the following criteria:
     - Ticket Channel Is SMS
     - Ticket Is Created
   - Perform these actions:
     - Notifications: SMS User: requester
     - From (select SMS number)
     - Body (include text you'd like in your automated outbound SMS)
5. Click **Create trigger**.

![](http://zen-marketing-documentation.s3.amazonaws.com/docs/en/text_ex_1.png)

Tip: Use *unformatted* placeholders to personalize your text support. Learn more about placeholders [here](../business-rules/using-placeholders.md).

## Alert agents when a ticket needs attention

Help ensure your agents prioritize tickets appropriately by notifying them when tickets that meet certain criteria need attention. This can be helpful if you want to prioritize tickets from VIP customers or have Service Level Agreement (SLA)
targets to meet.

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Business rules >
   Triggers**.
2. Click **Add trigger**.
3. Enter a title for your trigger, like “VIP customer text update.”
4. Add the following conditions and actions for your trigger:
   - Meets all of the following criteria:
   - - Ticket Is...Updated
     - Organization Is: The organization of the VIP customer, in this example "Legal"
   - Perform these actions:
     - Notifications: Text Group
     - From (select text number)
     - Body (include text you'd like in your automated outbound SMS)
5. Click **Create trigger**.

![](http://zen-marketing-documentation.s3.amazonaws.com/docs/en/text_ex_2.png)

## Start a text conversation with proactive outbound texts

Reach out to customers on a personal level with proactive outbound text. For this recipe to work, you need to set up a trigger and then create the proactive ticket yourself.

**To create a trigger**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Business rules >
   Triggers**.
2. Click **Add trigger**.
3. Enter a title for your trigger.
4. Add the following conditions and actions for your trigger:
   - Meets all of the following criteria:
     - **Ticket** > **Is** > **Created**
     - **Tags** > **Contains at least one of the following**
       > [create a tag like proactive\_text]
   - Perform these actions:
     - **Notifications** > **Text user** >
       **(requester)**
     - **From** > (choose a text number)
     - **Body**: {{ticket.latest\_public\_comment}}
     - **Status** > **Closed**
     - **Remove tags**: proactive\_text (or whatever tag name you used)

     If you want to use Explore to report on proactive outbound texts, add a unique tag (such as *proactive\_texts\_sent*) to the trigger actions. For help, see [Reporting with tags](https://support.zendesk.com/hc/en-us/articles/4408838151450).
5. Click **Create trigger**.

Note: Make sure that ticket status is set to “closed”. If your customers respond to your outbound texts, that will create a new ticket. Like other inbound texts, you can respond to your customers’ text via public comment in the ticket. If you do not wish to send an email notification, add your "proactive\_text" tag to a Ticket:Tags Contains none of the following condition in your Notify requesters of received request trigger. See [How do I prevent email notifications from being sent out on SMS tickets?](https://support.zendesk.com/hc/en-us/articles/4408820432282) in our Support tech notes.

## Create a proactive ticket

**To create a proactive ticket**

1. Click **+Add** - New… Ticket
2. Make the requester your text recipient. The recipient must be a current end-user in the account.
3. Assign an agent.
4. **Subject** - anything that helps your team (will not affect the text)
5. **Description** - type your outbound text message
6. **Tag:** include “proactive\_text” tag.
7. Submit as Solved.

For repeated outbound texts, create a macro that’ll automatically add your proactive text tag and populate the description with your message. Learn more about macros [here](../../agent-guide/ticket-automation-and-collaboration/organizing-and-managing-your-macros.md#topic_dgn_12j_mw).

Important: Keep the body text short or it might be broken into multiple messages.
Remember that placeholders will be expanded. A text message (including expanded placeholders) cannot exceed 1,600 characters. If your text message goes over this limit, you'll receive a delivery failure.

Tip: Send proactive texts in bulk using the Proactive Ticket app (requires Customer Lists, an Add-on available to customers on Support Professional plans and above). Learn more [here](https://support.zendesk.com/hc/en-us/articles/4408887441690-Can-I-bulk-create-tickets-to-email-my-users-).

![](http://zen-marketing-documentation.s3.amazonaws.com/docs/en/text_recipe_four.png)

## Respond to texts within a new ticket

If a customer responds to your outbound text, their reply text will create a new ticket. The text (or placeholder content) from the body of the trigger you created in the previous step will be added as an internal note in the newly created ticket.
You can respond to that ticket as you would any other channel -- public responses will be sent as texts.

![](http://zen-marketing-documentation.s3.amazonaws.com/docs/en/text_recipe_five.png)