# About utilities in Contact Center

Source: https://support.zendesk.com/hc/en-us/articles/9459110093594-About-utilities-in-Contact-Center

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | Zendesk for Contact Center |

Verified AI summary ◀▼

Utilities in Contact Center let you configure functionality for agents, appearing in the main or side panel during contacts or after call work. As an admin, you can set up iFrame utilities to display third-party apps and task utilities for follow-up actions. This helps agents access necessary tools without leaving the contact screen, reducing call times and improving customer satisfaction.

Utilities help admins to configure functionality and determine where and when it is available to agents.

You can think of a utility as a customizable UI component that you can configure to contain various functionality. The following is true of utilities:

- You must be an admin to configure utilities.
- Utilities can appear in either the main or side panel in Contact Center, and can be visible to agents during a contact, in after call work, or both.
- Utilities are contact driven, meaning they are available to agents while they are on a contact or in after call work (ACW).
- Utilities are designed to only display information to agents if it is relevant to their ongoing contact or ACW.

Utilities are useful, because agents often use multiple apps to resolve a customer query, and switching among applications is an inefficient process, leading to longer call times and lower customer satisfaction. Utilities make it easier for agents to get the information they need to quickly assist a customer in Contact Center.

Additionally, utilities ensure that when an agent needs to perform additional tasks or actions (such as creating a follow-up task during a call), they can do it quickly, without leaving the contact screen.

## Understanding utility types

There are currently two utility types:

- **iFrame** utilities display third-party applications.
- **Task** utilities display tasks for agents.

### The iFrame embed utility type

The iFrame embed utility displays third-party applications and allows an agent to read, write, or update data within the third-party application, based on their permission in the application.

The following example shows an agent using two utilities:

- In the side panel, an iFrame utility displays a third-party booking application, allowing the agent to book an appointment for the customer without leaving the contact screen.
- In the main panel, an iFrame utility displays points of interest on a custom map, allowing the agent to provide information (in this case, a list of stations) to the customer without leaving the contact screen.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zen_contact_cent_1-1.png)

### The task utility type

The task utility displays specific tasks for agents, and allows agents to create follow-up tasks while on a contact. The task utility allows admins to control when and where tasks appear to agents.

The following example shows a task utility that allows an agent to schedule a callback for a specific time for the customer.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zen_contact_cent_1-2.png)