# Using triggers to display estimated wait time in messaging conversations 

Source: https://support.zendesk.com/hc/en-us/articles/8009787999514-Using-triggers-to-display-estimated-wait-time-in-messaging-conversations

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Live chat and messaging Team, Professional, or Enterprise |

Admins can set up messaging triggers to share an estimated wait time with customers for agent engagement. Estimated wait time is calculated and displayed after an AI agent hands off a messaging conversation and a ticket is created. Wait time is estimated based on the ticket’s position in the ticket queue using recent ticketing data. Admins can also set up triggers to send a message to the customer after the messaging ticket is assigned to an agent from a queue.

This article includes the following sections:

- [About estimated wait time in messaging conversations](#topic_gm2_g5c_tcc)
- [Displaying estimated wait time](#topic_a3m_g5c_tcc)
- [Sending a follow-up message when a ticket is assigned to an agent](#topic_vvx_g5c_tcc)

Related article:

- [Messaging triggers conditions and actions reference](https://support.zendesk.com/hc/en-us/articles/8015292388378)

## About estimated wait time in messaging conversations

Wait time is estimated using a statistical model that considers the average wait time for the customer's queue position and historical wait time only for that queue or group. The model pulls performance data from the most recent period available: the previous 10 minutes, two hours, or three weeks.

Estimation requires data. The wait time will be available only for queues/groups with at least 1 ticket routed in the last 7 days. The trigger(s) will not be activated with insufficient data.

On third-party bots, the trigger is activated after the bot hands over control, and the created ticket is placed in the queue.

The following situations may impact the accuracy of wait time estimates:

- A surge in ticket submissions. Accuracy will increase as more new data is available.
- Insufficient recent ticket data.
- Queues that recently came online.
- Queues with irregular wait times due to insufficient agent capacity or a lack of agent availability.

## Displaying estimated wait time

To display the estimated wait time to a customer, you must build a trigger that runs *only when a conversation is initially added to the queue* and sends a message to the customer using the *@wait\_time\_min* and *@wait\_time\_max* placeholders.

Applying this trigger to a small agent group or customer segment is recommended to ensure it functions as expected before rolling it out to your entire team.

Consider communicating clearly to your customers that estimated wait times are just that – estimates – and are not guaranteed (“Expect to wait at least @wait\_time\_min minutes” or "We should be with you within @wait\_time\_max minutes," for example).

**To display an estimated wait time**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Business rules > Messaging triggers**.
2. Click **Create trigger**.
3. Enter a name and brief description for your trigger.
4. Click **Activate this trigger.**
5. Customize the trigger as follows:

   - **Run trigger**: When a conversation is added to the queue.
   - **Conditions**: Match ALL of the following conditions:

     - Initial routing | is | True
     - Group | is | <group name>
     - Group status | <group name> | Online
   - **Actions**

     - Send message to customer | Responder | [message text, such as "Your estimated wait time is @wait\_time\_min-@wait\_time\_max mins."]
6. Click **Create**.

## Sending a follow-up message when a ticket is assigned to an agent

After you implement the estimated wait time trigger described above, you can create a trigger that sends another message to the customer when the ticket is assigned from a queue to an agent.

**To send a message to an end user when a ticket is assigned to an agent**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Business rules > Messaging triggers**.
2. Click **Create trigger**.
3. Enter a name and brief description for your trigger.
4. Click **Activate this trigger.**
5. Customize the trigger as follows:

   - **Run trigger**: When a conversation is assigned from a queue.
   - **Conditions**: Match ALL of the following conditions:

     - Group | is | <group name>
     - Group status | <group name> | Online
   - **Actions**

     - Send message to customer | Responder | [message text, such as "An agent will be with you shortly."]
6. Click **Create**.