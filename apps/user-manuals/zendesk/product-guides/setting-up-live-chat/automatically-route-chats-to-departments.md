# Automatically route chats to departments

Source: https://support.zendesk.com/hc/en-us/articles/4408881953434-Automatically-route-chats-to-departments

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Live chat and messaging Team, Professional, or Enterprise |

You can use departments in Zendesk Chat to filter chat requests to specific groups of agents.
For example, you might want of your billing and payment questions to go to your Billing
department, while troubleshooting questions should go to the Tech Support department.

When a chat is assigned to a certain department, the chat request appears only in the queues
of agents in that department. Just as without departments, an agent must click **Serve
Request** to respond to the chat.

One way to assign a chat to a department is to list departments on the Pre-Chat form so
visitors can select the department they want to chat with. For more information, see [Enabling the Pre-Chat form](https://support.zendesk.com/hc/en-us/articles/4408882974234). If you'd rather automatically send chats
to a certain department based on the visitor's current page, tags, locale, or other
information, you can do so using triggers.

You should use the *Still on site* condition to add a one-second delay at the
beginning of this routing trigger. All triggers fire at the same time and run through their
conditions and actions sequentially, and the *Still on site* condition allows
other triggers to perform actions that might be required before you can accurately route your
chat. For example, if you need to reference a visitor tag to determine which department should
receive a chat, this delay will allow the trigger that assigns the visitor tag to perform that
action before it's used as a condition in your routing trigger. See below for an example of
this condition.

**To route chats automatically**

1. From the dashboard, go to **Manage** > **Triggers**.
2. Click **Create Trigger**.
3. Set up your trigger's conditions and actions.

   - Set the *Still on site* condition to add a one-second delay.
   - Choose the condition (in this case, a visitor tag) you're using to identify which
     department should receive the chat.
   - Select the *Set Visitor Department* action and select a department.

   For example, if you want to automatically send chats from the pricing page to the
   Sales department, you might set up your trigger up as shown below:

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/chat_trigger_route_department.png)
4. Click **Create Triggers**.

Note: The widget will display as available for chats even if the department set by the visitor
tag (by the API or trigger) is offline. To display the widget when specific departments are
online, see [Can I configure the Web Widget (Classic) to present Chat on
my webpage only when a specific department is online?](https://support.zendesk.com/hc/en-us/articles/4408820372890)