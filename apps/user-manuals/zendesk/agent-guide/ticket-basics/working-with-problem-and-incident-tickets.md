# Working with problem and incident tickets 

Source: https://support.zendesk.com/hc/en-us/articles/4408835103898-Working-with-problem-and-incident-tickets

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Problem-and-incident tickets are useful when a problem or service interruption is reported by more than one person. For example, when the wireless network in an office stops working, several people might file tickets. You can treat the tickets as incident reports. Instead of handling each ticket separately, you can link the tickets to one problem ticket, and then solve the problem ticket to solve all the incident tickets.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/incident_workflow.png)

Here's the general workflow:

You must have the ticket **Type** field available in your ticket form to create this workflow.

1. Identify a service interruption or problem that's causing people to file tickets.
2. Create your own ticket to address the problem.
3. Change the other tickets to incident tickets and link them to your problem ticket.
4. Solve the problem ticket.

When you solve the problem ticket, the status of all the incident tickets is automatically set to solved. The comment added to the problem ticket when solved is added to all incident tickets that aren't already solved.

Refrain from solving any of the incident tickets directly. Solving an incident ticket still leaves the other tickets unsolved. Save work by solving only the problem ticket. It automatically solves all the linked incident tickets. When the problem ticket is solved, any empty required fields on linked incident tickets are ignored and the tickets are solved anyway.

When you solve a problem ticket, linked incident tickets are updated with a comment.
Customers are not notified using the messaging channel.

Note: [AI agent tickets](https://support.zendesk.com/hc/en-us/articles/9204149016346) can’t be linked to problem and incident tickets.

Tip: For advice on how to manage problem-and-incident tickets see Rani Sivesind's [Full circle: The right way to use ticket status and type](https://support.zendesk.com/hc/en-us/community/posts/4409506686362).

**To create and solve problem-and-incident tickets**

1. After identifying a problem that's causing people to file tickets, create your own ticket describing the problem and set the ticket type to **Problem**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/incident_problem_ticket.png)
2. For every other ticket reporting the same problem, set the ticket type to **Incident** and link it to the problem ticket.

   After you set the type to Incident, a second menu appears that lets you link the incident to a problem ticket.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/incident_link.png)

   Make sure to click **Submit** to update and save the changes to the ticket.
3. Return to the problem ticket to view the linked tickets and review the incident reports.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/incident_problem_link.png)
4. When you're ready to solve the problem ticket and linked incidents, add a comment. Note that the comment you add when solving the problem ticket is only included in unsolved linked incident tickets.

   You may want to use placeholders to personalize the comment for wide distribution. For example:

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/incident_comment.png)

   See [Using placeholders](../../product-guides/business-rules/using-placeholders.md).

   Use caution when using macros to update problem and incident tickets. See [Using macros to update problem and incident tickets](https://support.zendesk.com/hc/en-us/articles/4408887656602#topic_abf_z5m_n1c).
5. Solve the problem ticket, then confirm that you want to solve all open linked incident tickets.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/problem_ticket_confirm_solve.png)

If you decide to reopen the solved problem ticket, the incident tickets aren't updated. They stay solved. If you solved a problem ticket prematurely or if you need to communicate something more to the requesters, you can reopen the incident tickets before solving the problem ticket again. Click the **Incidents** tab when viewing the problem ticket and bulk edit all of the tickets. Submit the tickets as open and proceed with re-solving the problem ticket.

**Related topics**

- [Streamline support using Problem and Incident tickets](https://support.zendesk.com/hc/en-us/articles/4408829669274)