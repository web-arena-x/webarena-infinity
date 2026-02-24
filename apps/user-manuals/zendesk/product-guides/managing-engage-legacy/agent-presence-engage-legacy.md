# Agent Presence (Engage Legacy)

Source: https://support.zendesk.com/hc/en-us/articles/9731498295834-Agent-Presence-Engage-Legacy

---

The Agent Presence feature in Engage is designed to help customer service agents easily transfer calls to other available agents within your team. This guide walks you through the steps of using this feature and its key functionalities.

## ‍**Prerequisites for Agent Presence**

Before enabling and using the Agent Presence feature in Engage, ensure the following prerequisites are met:

- **CloudFormation Stack Upgrade**:
  - Your Engage instance must be updated to **version 5.99.2 or higher**. Ensure that the latest CloudFormation stack is deployed.

‍

- **Contact Flow Setup:**   
  - Add the following two contact flows (both of type 'Transfer to Queue') to the Amazon Connect instance to route the contact to a given agent/queue given in the contact attributes:

‍

Please reach out to our Support team at engage-support@getlocalmeasure.com to receive JSON file exports of the following Contact Flows so you can easily import them into your instance

‍

**Direct Queue Transfer Contact Flow**

![__wf_reserved_inherit](https://support.zendesk.com/hc/article_attachments/9731474388634)

‍

**Direct Agent Transfer Contact Flow**

![__wf_reserved_inherit](https://support.zendesk.com/hc/article_attachments/9731474417562)

- **Quick Connects Setup**:
  - Create two **Quick Connects** of type "Queue" in Amazon Connect with the following names:
    - **`Direct Queue Transfer`** - link to the Direct Queue Transfer contact flow.
    - **`Direct Agent Transfer`** - link to the Direct Agent Transfer contact flow.**‍**
  - **Note:** These Quick Connects do not need to be added to queues like standard Quick Connects. Engage can still access and use them even if the agent does not have direct access to them.

![__wf_reserved_inherit](https://support.zendesk.com/hc/article_attachments/9731465996826)

![__wf_reserved_inherit](https://support.zendesk.com/hc/article_attachments/9731449528346)

- **Engage Workflow Settings**:
  - Once the Quick Connects are created, configure them within the **Engage Workflow Settings** to ensure proper routing.

![__wf_reserved_inherit](https://support.zendesk.com/hc/article_attachments/9731461924506)

## Initiating a Call Transfer

When you're on a call and need to transfer it to another agent:

1. Click the Transfer button. This will open the Transfer Modal.
2. The transfer modal includes the following tabs:   
   **Agents** (Displays a list of Quick Connect Agents).  
   **Queues** (Displays a list of Quick Connect queues).  
   **External** (Shows a list of all the external numbers that have been configured).  
   **Number Pad** (Displays a number pad where you can manually enter a contact number). Once you've chosen a tab, you can transfer the call to an available agent who is prepared to take the call.

## Searching and Filtering Agents

The transfer modal allows you to search for specific agents or filter the list based on various criteria. Use the Search Bar to quickly find an agent by typing their name. Apply filters to sort agents by their availability (e.g., Available, Busy, Offline) or any custom filters that have been set up in your system, for example filtering by Routing Profiles.   
Additionally, agents can filter by **Queues**, allowing them to see which agents are assigned to specific customer service queues (e.g., Sales, Support). This helps ensure that the transfer goes to the agent best suited for the customer’s needs based on their assigned role and expertise.  
‍

## Viewing Agent Status and Availability

Next to each agent's name, you will see real-time information about their status:

- Availability: The agent’s current status is displayed (e.g., green for available, red for busy).
- Active Chats/Calls: You can see how many active chats an agent is handling.
- Agents who are offline or unavailable will have the Transfer button disabled, preventing any errors.
- The agent status will automatically update when you switch between tabs or when you click on the refresh icon.

![__wf_reserved_inherit](https://support.zendesk.com/hc/article_attachments/9731449549338)

## Transferring a Contact

1. To transfer a contact to either an Agent, Queue, or External Contact simply select the option of the name you wish to transfer to and then click the Transfer button. This will invoke the transfer procedure within Engage.
2. The system will then route the contact to the agent, queue or external number. You'll see a brief loading indicator while the transfer is being processed.
3. If you are transferring a chat, your interaction with the customer goes into the ACW workflow, and the chat is transferred to the selected destination. If you are transferring a call, you will have the option to select 'join' to create a conference call with yourself, the other agent and the caller. If you do not wish to create a conference call you can disconnect the interaction on your side and you will transition into ACW.

## Real-Time Updates

The agent list updates in real-time by clicking on the refresh icon or by switching between tabs, so you’ll always have the latest information on your colleagues' status. Any changes in their availability or activity will reflect immediately, ensuring smooth and informed transfers.

![__wf_reserved_inherit](https://support.zendesk.com/hc/article_attachments/9731466042138)

Agent desktop screen

## Agent Presence Settings ‍

1. To change the Agent Presence transfer settings, go to the Workflows tab in Engage's settings.
2. Select a workflow to edit and then scroll down to Transfer Targets.
3. To enable Quick Connects (Queues, Agents, External), select the checkboxes you want to activate and click "Save Workflow" to apply the changes. During call transfers, agents can only see the quick-connects that they have selected.
4. To allow Agents calling customer numbers, Enable the "Dialpad / Custom Numbers" option.
5. In the "Agent Search and Transfer" section, enable AgentSearch and Transfer and, if necessary, limit the results. To apply the changes, click "Save Workflow". Agents can now look for agents both online and offline.
6. To perform a Quick Connect transfer, select the Quick Connect option from the dropdown menu. To limit the search results for an agent, you can select the desired option. To apply the changes, click "Save Workflow".
7. To change the Transfer Types settings, select "Disable transfers to queues or agents" and click "Save Workflow" to apply the changes.

## ‍

![__wf_reserved_inherit](https://support.zendesk.com/hc/article_attachments/9731498440346)