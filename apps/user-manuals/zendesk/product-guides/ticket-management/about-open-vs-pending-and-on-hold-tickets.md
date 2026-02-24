# About open vs. pending and on-hold tickets

Source: https://support.zendesk.com/hc/en-us/articles/4408843029658-About-open-vs-pending-and-on-hold-tickets

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

One of the major benefits to using an Zendesk to handle your customer interactions is that, unlike an email inbox, the interactions in a ticketing system have a defined end-point: you mark a ticket solved. This closed loop process is important for both your company and your customers; it puts you both on the same page - an agreement that the issue or question has been resolved and ultimately closed.

But of course, there are a few steps between a customer sending a ticket and you marking it solved. To handle these various stages, all tickets have a *ticket* *status.* The default ticket statuses are New, Open, Pending, On-hold, or Solved.

## Understanding which status to use and when

New and Solved might be self-explanatory: they mark the beginning of the interaction and the end. But what about Open, Pending, and On-Hold? By understanding and making use of these statuses, you can stay on top of your support workload and bring any outstanding tickets to solved in an efficient manner.

Ticket Status can be manually set within each ticket.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/onhold_lotus.png)

An Open ticket is defined as a ticket assigned to an agent. Open tickets are the heart of your support workload. These tickets indicate the issues that you're working on. Once a ticket's status has been changed from New, it can never be set back to New.

Where this begins to be important is when you set up views, triggers, and automations based on a ticket's status.  It is probably useful, for instance, to see a grouping of all your Open tickets that need to be solved.

But, of course, oftentimes to solve a ticket, you need to collect more information from the requesting customer. For example, you might need the specific text of the error that they are seeing, or you might need their account number.  So you write them back.  In those cases, you want to be able to move the ticket off the list of things that need your attention, but at the same time not forget about it. This is why the Pending status is so useful. Pending is like saying: "This ticket is not yet solved but I'm waiting on information from the requester before I can work on it further."

The On-hold status is similar to Pending, and used to indicate that you are waiting for information or action from someone other than the requester, for example, one of your supervisors or an internal developer. On-hold is an optional, internal status. It can be [enabled by an administrator](https://support.zendesk.com/hc/en-us/articles/4408889282458), and if it isn't enabled, you will not see it in your status options. Ticket requesters do not see this status. On-hold tickets appear as Open to your customers.

## Example: Creating a view to show tickets that are not solved

To see how these states might be useful, let's take a look at how you could set up a view that shows you all your unsolved tickets but groups them according to whether they are Open or Pending.

**To create a view of tickets less-than-solved**

1. Create [a new view](https://support.zendesk.com/hc/en-us/articles/4408888828570).
2. Add the condition **Ticket: Status less than solved**. 
   We'll keep this simple and just collect all our tickets that are not solved, or in this case, less than solved. 
   ![](https://support.zendesk.com/hc/article_attachments/7856561844250)
3. Next, we'll set the **Format Options** to display by **Table** , and then choose to **Group** the tickets by **Status***: 
   *![](https://support.zendesk.com/hc/article_attachments/7856556412954)**
4. Click **Save**.

***Now, when we update and return to this view, we'll see our tickets grouped according to whether they are New, Open, Pending, or On-hold. This way, we can see those tickets where we've written back to the customer or internal expert for more information but they are separate from those that require our active attention.***

*![](https://support.zendesk.com/hc/article_attachments/7856556412314)**When our customer or internal expert replies to us with the information we requested, we can update the status from Pending or On-hold to Open. So the next time we look at our "All Unsolved Tickets" view, that ticket will appear in our Open list, and hopefully closer on its way to Solved!*