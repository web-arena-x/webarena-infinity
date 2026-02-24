# Creating an out of office response for messaging

Source: https://support.zendesk.com/hc/en-us/articles/4408842866074-Creating-an-out-of-office-response-for-messaging

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

You can use a messaging trigger to create an automated out of office message, shown to your customers when your agents are offline.

Note: You can only create this out of office message if you have two or more agents enabled on your account.

**To create an out of office message**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Business rules > Messaging triggers**

   Note: In some Zendesk accounts, this page is located in the Chat dashboard. Go to **Chat > Settings > Triggers**.
2. Click **Create trigger**.
3. Enter a name and brief description for your trigger.
4. Click **Activate this trigger**.
5. Customize the trigger as follows:
   - **Run trigger**: When a customer requests a conversation
   - **Conditions**: Match ALL of the following conditions
     - Account status | equals | Offline
   - **Actions**
     - Send message to customer | Responder | [*message text, such as "Sorry, I’m offline"*]
6. Click **Create**.

The trigger defined above will run whenever a customer requests a chat in the Web Widget or mobile SDK for an offline account.