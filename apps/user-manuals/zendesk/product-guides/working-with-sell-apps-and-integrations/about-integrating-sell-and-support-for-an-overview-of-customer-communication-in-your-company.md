# About integrating Sell and Support for an overview of customer communication in your company

Source: https://support.zendesk.com/hc/en-us/articles/4408833438746-About-integrating-Sell-and-Support-for-an-overview-of-customer-communication-in-your-company

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

![Available on all Sell plans](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/plan_available_sell_all.png)

If you integrate Zendesk Sell and Zendesk Support, you can access your Support tickets in Sell, and see your Sell data from your Support interface. This makes it easier to access the most important information about your contacts and also helps the sales and support teams to communicate.

Integrating Zendesk Sell with Zendesk Support means you and your teams can gain a comprehensive overview of your customers in Sell. When you click on your contacts in Sell, the integration enables you to see the history of their communication with Support, and all of their tickets, (beginning with those that are unsolved). To skip to configuring your integration, see [Setting up the Zendesk Sell-Support integration](https://support.zendesk.com/hc/en-us/articles/4408828146586).

Note: This feature requires you have any Zendesk Sell plan and a Zendesk Support Team, Professional, or Enterprise plan.

This article covers the following topics:

- [Understanding ticket connections for Sell users](#topic_j2k_hw3_2nb)
- [Helping your Sales team achieve better cross-department communication](#topic_mv5_hw3_2nb)
- [Requesting tickets on behalf of a customer](#topic_yj2_3w3_2nb)
- [Helping your support teams](#topic_ztq_3w3_2nb)

## **Understanding ticket permissions for Sell users**

All users with a Zendesk Sell account can access Support with limited permissions, (by default the role in Support is the Contributor role). The integration uses this to grant access to Support and fetch ticket data. For full visibility of customer tickets [add your Sales representatives to all of the groups](https://support.zendesk.com/hc/en-us/articles/4408894175130-Creating-managing-and-using-groups#topic_wyj_dse_bc) in Support where those tickets can be assigned.

The permissions of a Sales representative role in Support often prevents them from seeing the tickets that are not yet assigned to any group. If this is the case, [create a trigger](https://support.zendesk.com/hc/en-us/articles/4408820783898-How-do-I-create-a-trigger-Video-) that assigns any new tickets to one of the groups that the Sales representatives have access to.

![Sell Support integration trigger settings](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_support_integration_trigger_settings.png)

If a Sales representative only has a Contributor role in Support, this means they do not have permission to create end-users. If a Contributor creates a ticket, on behalf of contacts that don’t yet have end-users in Support, the Contributor will be the requestor of the ticket. Therefore, a note with the actual requester data (of the Sell contact), is automatically added to the ticket, and the agent who takes the ticket can specify the correct requester, so the ticket response is sent to the contact.

## **Helping your Sales team achieve better cross-department communication**

To increase closure rate and renewal of deals, a Sales representative preparing for a call with a contact needs to know about any issues that have been reported through Support tickets, and to see the most relevant information relating to that contact.

With Zendesk Sell and Zendesk Support integration, Sales representatives can stay on top of all communication with their contacts without leaving the Sell interface. When email addresses or phone numbers of a Lead or a Contact in Sell match with requester data in Support, the tickets are automatically displayed inside the **Tickets** widget of a Sell object card.

![Sell Support integration widget](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_support_integration_widget.png)

To promote clarity and prevent events overload, the Tickets widget shows only the most important unsolved tickets. You can see all of the tickets in the **Browse tickets** view, (including solved tickets).

On a Contact company card, you can see the tickets that are related by the emails or phone numbers of employees of that company, as well as the company name, (if it is the same as the organization in Support). For deals, only the tickets for primary contacts are shown.

Note: If a company has many employees, Sell cannot display all of the requested tickets. Instead Sell will show only 100 tickets of the most recently contacted employees.

## **Requesting tickets on behalf of a customer**

Sometimes issues are reported during sales talks, or a Sales representative may receive information about an issue because they are the main contact for a customer.

A Sales representative can submit a ticket on behalf of a customer, directly in Sell, by clicking (**+**) on the **Tickets** widget, and filling in a short form about the issue. For clarity, the ticket description is added as an internal note, visible only to Support staff. When the Agent responds to the ticket, the public reply is sent directly to the customer.

When a ticket is requested on behalf of a customer that does not yet exist in Support, the email address and phone number of the customer is passed on to Support to ensure a smooth flow of communication for the agent.

## **Helping your support teams**

Integrating Zendesk Sell and Zendesk Support enables support agents to easily familiarize themselves with the context of customer sales and to pass sales-related insights on to the Sales department. For more information about this feature, see [Working with the Zendesk Sell app in Support](https://support.zendesk.com/hc/en-us/articles/4408831980314).