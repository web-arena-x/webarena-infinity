# Installing and using the Out of Office app

Source: https://support.zendesk.com/hc/en-us/articles/4408828358682-Installing-and-using-the-Out-of-Office-app

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

62082233

The Out of Office app is a tool for managing the availability of an agent in Zendesk Support, and ensuring that tickets assigned to unavailable agents are properly handled if updated by a customer.

This article covers the following topics to help you install, use, and extend the app:

- [How the app works](#h_88c8dfa2-fbfa-486b-b59f-99bb2dfc8a79)
- [Installing the app](#h_3c3352e3-afd1-4d5b-8869-cef3fbe3f3de)
- [Changing the app settings](#h_7e19a352-4a02-4911-8876-ecc59b90507c)
- [Using the app](#using)
- [Understanding the 'agent\_ooo' tag](#tag)
- [Known limitations](#limits)
- [Troubleshooting](#h_42e1184d-0373-40f6-8be1-6b7d8f94f649)

# How the app works

The Out of Office app displays the availability status of the agent assigned to tickets in Zendesk Support.

![](https://support.zendesk.com/hc/article_attachments/7856507763610)

For administrators, it also displays a list of agents and their availability.

![](https://support.zendesk.com/hc/article_attachments/7856552677274)

The app prevents tickets from being accidentally assigned to an agent who is unavailable. When this occurs, a pop-up notification is displayed to the agent.

# Installing the app

**To install the Out of Office app**

1. In the [Zendesk App Marketplace](https://www.zendesk.com/marketplace/apps)
   search bar, search for **Out of Office,** and select the app from the results list.
2. Click **Install**in the upper-right corner. 
   ![](https://support.zendesk.com/hc/article_attachments/7856507763866)
3. Select or unselect the **Confirm status change** checkbox. Unselecting this option disables the status change confirmation message. As a result, you cannot choose to unassign an agent's open tickets when marking them as unavailable. 
   ![](https://support.zendesk.com/hc/article_attachments/7856552677018)
4. Select or unselect the **Force unassign tickets** checkbox. Enabling this setting unassigns an agent's open tickets automatically when their status is changed to unavailable. Tickets in Pending or On-hold status remain assigned to the unavailable agent until the status changes back to Open (typically, when the end user replies to the ticket).
   This option is disabled by default, allowing the unassign action to be run on a case-by-case basis.
5. Select or unselect the **Prevent assignment** checkbox.
   Disabling this option allows tickets to be saved if they're assigned to an agent who's unavailable. A warning is still displayed that the assignee is unavailable, and agents can assign tickets to themselves regardless of their status.
6. Select or unselect the **Surface errors encountered when bulk updating tickets?** checkbox. Enabling this option causes the unassign process to take longer. Some tickets may still not get updated by Out of Office even with this setting turned on. This setting simply verifies the ticket updates and surfaces any errors encountered whilst updating tickets.
7. If required, select and configure role restrictions and group restrictions.

   To allow all roles and groups to use the app, leave the **Enable role restrictions** and **Enable group restrictions** checkboxes deselected.
   To add restrictions, select **Enable role restrictions** or **Enable group restrictions**, then select the roles or groups that should have access to the app.
8. Click **Install** to complete the setup.

The app settings can be changed after installation by navigating to **Admin Center**> **Zendesk Support Apps**, under the **Currently installed** tab, click the Out of Office app icon to reveal the dropdown menu, and select **Change settings**.

# Changing the app settings

You can modify the app's default behavior by changing the app settings.

**To change the app settings**

1. In Admin Center, select **Apps and integrations** > **Zendesk Support Apps**.
2. In the Out of Office app icon, select **Change Settings** from the dropdown options menu**.**
3. Modify your settings and click **Update**.

# Using the app

An agent can modify their status using the app in the ticket sidebar or accessing their user profile.

**To modify your availability**

1. Open a ticket in Zendesk Support. Alternatively, select your user profile icon the upper right, and then click **View Profile**.
2. In the ticket app sidebar, under the Out of Office app, select the **Availability** toggle button. A confirmation dialog box opens to confirm the change.
3. Click **Set as Available** to enable availability, or **Set as Unavailable** to set your status as unavailable**.
   ![](https://support.zendesk.com/hc/article_attachments/7856507763610)**

An administrator can access the Out of Office dashboard to view the availability of agents and modify an agent's status.

**To view and modify an agent's availability**

1. In Support, select the Out of Office icon in the left navigation bar. The dashboard opens.
   ![](https://support.zendesk.com/hc/article_attachments/7856552677274)
2. Click on the **Availability** toggle button next to agent. A confirmation dialog box opens to confirm the change.
3. Click **Set as Available** to enable availability, or **Set as Unavailable** to set an agent's status as unavailable**.**

Changing the availability status either adds or removes the **agent\_ooo** tag from tickets. For more information, see [Understanding the agent\_ooo tag](#tag) below.

When a pending or on-hold ticket is reopened by an end user and the assignee is unavailable, a trigger fires that returns the ticket to the unassigned ticket queue.

The app checks the status of the assignee each time a ticket is saved.
If the assignee is unavailable, the app warns the updater that the assignee is unavailable. If the **Prevent assignment** setting is enabled, it also prevents tickets from being saved if the new assignee is unavailable.

The following functions and behavior can occur when using the Out of Office app in Zendesk Support:

- An agent can assign a ticket to themselves if they are unavailable**.**The following warning is displayed after the ticket is saved: 
 ![](https://support.zendesk.com/hc/article_attachments/7856552676762)
- An agent cannot update a ticket if they're not the assignee and the assignee is unavailable. A warning notification is displayed that the current assignee is unavailable:
 ![](https://support.zendesk.com/hc/article_attachments/7856507762458)
- Tickets that are assigned to an unavailable agent with a **Pending** and **On-Hold** status, but are updated to **Open,** are reassigned to the respective ticket's parent group. However, the **Assignee** field becomes empty. Status changes from **Pending** or **On-Hold** occurs when an end-user replies to an email notification.

# Understanding the agent\_ooo tag

When the Out of Office app is installed, it automatically creates in Zendesk Support the following items:

- A user field that applies an **agent\_ooo** tag to users marked as unavailable
- A trigger to handle the unassign action on a ticket based on the **agent\_ooo** tag
- A trigger to remove the **agent\_ooo** tag from a ticket when it's assigned to a different agent

**Note**: These items are required for the app to work.
Don't delete or modify them.

Changing the availability status either adds or removes an **agent\_ooo** tag on tickets based on the following rules:

- When an agent marks themselves as unavailable, the **agent\_ooo** tag is added to the agent's user profile in the **Agent Out?** user field.
- Adding or removing the **agent\_ooo** tag, or selecting/deselecting the **Agent Out?** field doesn't change the agent's availability. Availability can only be changed using the **Availability** toggle button.
- When the agent changes their status to unavailable, the tag is added to all tickets assigned to the agent with a **Pending**, **On-Hold**, or **Solved** status.
- When the agent changes their status to available, the tag is removed from these tickets.
- Any open tickets with the tag are unassigned on update.
- If the ticket assignee is changed, then the tag is removed.
- If the tag is removed from a ticket, no other tags are removed.

# Limitations

The Out of Office app has the following limitations:

- Agents require permissions to edit ticket tags to mark themselves out-of-office. Without this permission, agents can use the **Availability** toggle to modify their availability, but their tickets will not be updated with the tag. If ticket tag editing permissions cannot be enabled for agents requiring out-of-office functionality, admins must manage their out-of-office status on their behalf.
- The app does not reassign tickets if the agent's out of office status is changed outside of the Out of Office app.
- The app does not work on [Side Conversations.](../../agent-guide/ticket-automation-and-collaboration/about-side-conversations.md)
- The app does not prevent assigning tickets unless the ticket is updated individually through the Zendesk interface. Triggers, Mail API, REST API, and bulk editing will be able to bypass the assignment restrictions.
- Agents can still self assign/take ownership of tickets while they are out of office. The app will not prevent this. The app also can't prevent tickets being assigned to agents while they are out of office when done through outside the Zendesk interface.
- Agents without administrator rights can't change their status using the app dashboard in the left navigation bar of the agent interface.
- [Agent statuses](https://support.zendesk.com/hc/en-us/articles/4409149119514-About-omnichannel-routing-beta-)doesn't affect Out of Office app functionality.
- If the **Prevent assignment** setting is disabled and a ticket is assigned from one unavailable agent to another unavailable agent, the **agent\_ooo** tag will be lost. This means that the ticket will not be unassigned if it is reopened.
- Groups with only one agent:
 - Agents are able to assign a ticket to a group with only one agent even if the sole agent in that group is unavailable.
 - If there is only one agent in a group that can be assigned tickets, all tickets assigned to that group will automatically be assigned to that one agent. Some agents in groups, such as light agents, do not have permission to be assigned tickets.
 - If an agent is the only agent in a group and the agent goes out of office, the assigned tickets will not be re-assigned back to the group. This is due to the[inborn system ticket rules](https://support.zendesk.com/hc/en-us/articles/4408894213018-About-the-inborn-system-ticket-rules).
- The **agent\_ooo** tag is added to solved tickets. If the ticket is closed while the tag is applied, however, the tag will not be removable because Tickets in the closed status cannot be updated. This may be undesirable for reporting purposes.
 If so, the system automation that closes solved tickets should be modified to remove the **agent\_ooo** tag before closing the ticket.
- When a ticket assigned to an out of office agent gets updated, the ticket is assigned back to the parent group with a null Assignee value. The trigger working in the background during this action does not currently send an email notification to the agents in the group
- In some instances, if an agent is downgraded to an end user while unavailable, they will retain the **agent\_ooo** tag until it is removed manually. Any tickets that the end user creates also inherits the **agent\_ooo** tag.
- Follow-up tickets are not unassigned when the **Copy original group and assignee to follow-up ticket** and **Force unassign tickets** settings are turned on, and the agent is unavailable; they are added to the original assignee's queue.
- API Limits:
 - When updating a large amount of tickets API rate limits can be encountered causing the update process to take longer than usual. Please be patient and allow the app to finish the update process. The update process is finished when the app no longer displays "Updating..." in lieu of the agent's OOO status
 - The volume of tickets associated with an Agent will impact app performance and updating a large amount of assigned tickets can fail resulting in the **agent\_ooo** tag not being added to all the tickets resulting in tickets not being assigned back to the parent group
 - When marking an agent as OOO and un-assigning all open tickets, only some of the tickets will actually get unassigned
 - If an agent closes the browser tab in the midst of an update or if there is a network issue, OOO updates may be lost causing incomplete updates to tickets.
- The framework within which the Out of Office app is built in has inherent limitations in terms of resolving errors and retrying. In cases where it encounters errors updating tickets or API limits can result in issues such as: some or all of the assigned tickets missing the **agent\_ooo** tag when an agent changes their status to "Unavailable". The following workarounds can be tried to resolve such issues.
 - Enable the **Surface errors encountered when bulk updating tickets** app setting. This will notify if any errors were encountered when updating the assigned tickets - either removing or adding the **agent\_ooo** tag.
    By default this setting is disabled.
 - Toggle the status in the app to "Available" and toggle the status to "Unavailable" (again) - or vice versa.
 - [Bulk update](../../agent-guide/ticket-management/managing-tickets-in-bulk.md)all tickets and *add* the **agent\_ooo** tag if the agent is going to be "Unavailable" or *remove* the **agent\_ooo** tag if the agent is going to be "Available"

Troubleshooting

If you cannot install the Out of Office app, and get and error "agent\_ooo has already been taken", review the following steps:

- [Remove the user field](../end-users-and-organizations/managing-custom-user-fields.md)
 that has the field key **agent\_ooo**- most likely named "[Out of Office] Agent Out" or the user field is in inactive state
- If you get an error while removing the user field, check your triggers or automations and remove any references to this user field