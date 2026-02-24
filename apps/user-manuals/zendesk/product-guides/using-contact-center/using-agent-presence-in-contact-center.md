# Using agent presence in Contact Center

Source: https://support.zendesk.com/hc/en-us/articles/9696113111706-Using-agent-presence-in-Contact-Center

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | Zendesk for Contact Center |

Verified AI summary ◀▼

Agent presence in Contact Center lets you transfer calls to available agents, enhancing team collaboration. Ensure prerequisites like CloudFormation Stack upgrade and feature flag activation are met. Initiate call transfers via agents, queues, or external numbers, and update agent presence settings to manage availability. Use real-time updates to keep track of agent status and optimize call routing.

Agent presence in Contact Center helps customer service agents easily transfer
calls to other available agents within your team. In this article, you'll learn about
agent presence and its key functionalities.

This article contains the following topics:

- [Prerequisites for agent presence](#topic_lnd_4yw_qgc)
- [Initiating a call transfer](#topic_ohx_3fx_qgc)
- [Updating the agent list](#topic_nxy_lfx_qgc)
- [Updating agent presence settings](#topic_wdg_4fx_qgc)

## Prerequisites for agent presence

Before enabling agent presence in Contact Center, ensure the following prerequisites
are met:

- **CloudFormation Stack upgrade**: Update your Contact Center instance to version 5.99.2 or higher. Ensure that the latest
  CloudFormation stack is deployed.
- **Feature flag activation:** Activate agent presence on a per-account
  basis and must be manually activated by the Contact Center team. Get in touch
  with the Contact Center team to request activation.
- **Contact flow setup:** Add the following two contact flows (both of type
  'Transfer to queue') to the Amazon Connect instance to route the contact to a
  given agent or queue:
  - Direct queue transfer
  - Direct agent transfer

Contact Zendesk to receive JSON file exports of the following contact
flows so you can easily import them into your instance.

- **Quick connects setup**:
  - Create two **Quick connects** of type 'Queue' in Amazon
    Connect with the following names:
    - **Direct Queue Transfer** - link to the direct
      queue transfer contact flow.
    - **Direct Agent Transfer** - link to the direct
      agent transfer contact flow.‍

    Note: These quick connects do not need to be added to queues like
    standard quick connects. Contact Center can still access and use
    them even if the agent does not have direct access to them.

    ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_ap_1.png)

    ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_ap_2.png)
  - Once the quick connects are created, configure them within the
    Contact Center workflow settings to ensure proper routing.

    ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_ap_3.png)

## Initiating a call transfer

When you're on a call, you can transfer it to another
agent.

**To transfer a call**

1. Click **Transfer**. This will open the transfer page.
2. Select one of the following tabs:
   - **Agents:** (Displays a list of quick connect agents).
   - **Queues:** (Displays a list of quick connect queues).
   - **External:** (Shows a list of all the external numbers that have
     been configured).
   - **Number pad:** Displays a number pad where you can manually enter a
     contact number.

   Once you've chosen a tab, you can transfer the call to an available
   agent who is prepared to take the call.

### Searching and filtering agents

The transfer page allows you to search for specific agents or filter the list
based on various criteria. Use the search bar to quickly find an agent by typing
their name. Apply filters to sort agents by their availability (Available, Busy,
Offline) or any custom filters that have been set up in your system, for example
filtering by routing profiles.

Additionally, agents can filter by queues, allowing them to see which agents are
assigned to specific customer service queues (for example, Sales or Support).
This helps ensure that the transfer goes to the agent best suited for the
customer’s needs based on their assigned role and expertise.

### Viewing Agent Status and Availability

Next to each agent's name, you will see real-time information about
their status:

- Availability: The agent’s current status is displayed (e.g., green
  for available, red for busy).
- Active Chats/Calls: You can see how many active chats an agent is
  handling.
- Agents who are offline or unavailable will have the transfer
  button disabled, preventing any errors.
- The agent status will automatically update when you switch between
  tabs or when you click the refresh icon.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_ap_4.png)

### Transferring a contact

If you need help from another agent, you can transfer a contact to them. You can
either remain on the call, or disconnect after the transfer.

**To transfer a contact**

- Select the name of the agent you wish to transfer to and then click
  **Transfer**.

  The system routes the contact to the agent,
  queue, or external number you selected.

If you are transferring a chat, your interaction with the customer goes
into the ACW workflow, and the chat is transferred to the selected destination.
If you are transferring a call, you will have the option to select **Join**
to create a conference call with yourself, the other agent, and the caller. If
you do not want to create a conference call you can disconnect, and you will
transition into ACW.

## Updating the agent list

The agent list updates in real-time, by clicking on the refresh icon, or by
switching between tabs, so you’ll always have the latest information on your
colleagues' availability or activity.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_ap_5.png)

## Updating agent presence settings

You can update your agent presence settings from the Workflows tab.

**To change agent presence settings**

1. Go to the Workflows tab in Contact Center settings.
2. Select a workflow to edit and then scroll down to Transfer
   targets.
3. To enable quick connects (queues, agents, or external), select the
   checkboxes you want to activate and click **Save workflow**. During call
   transfers, agents can only see the quick-connects that they have selected.
4. To allow agents to call customers, turn on the Dialpad/Custom numbers
   option.
5. In the Agent search and transfer section, select Agent search and
   transfer and, if necessary, limit the results.
6. Click **Save workflow**.

   Agents can now look for agents both
   online and offline.
7. To perform a quick connect transfer, select the Quick connect option
   from the dropdown menu. To limit the search results for an agent, you can select
   the required filter.
8. Cick **Save workflow**.
9. To change the transfer types settings, select **Disable transfers to
   queues or agents**.
10. Click **Save workflow** to apply the changes.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_ap_6.png)