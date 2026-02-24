# Understanding and using the prospect and customer statuses

Source: https://support.zendesk.com/hc/en-us/articles/4408832470554-Understanding-and-using-the-prospect-and-customer-statuses

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

![Available on all Sell plans](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/plan_available_sell_all.png)

To differentiate between the contacts that have deals associated with them, Sell uses the **Prospect** and **Customer** statuses. As a contact goes through the sales pipeline, first having a deal (or deals) associated with it, then having deals completed (won), its status changes from prospect to customer. This is done automatically by Sell.

In other words, when a deal is associated with a contact it becomes a prospect, and when a deal is won the contact becomes a customer (Contact > Prospect > Customer).

You can use these statuses to track your active contacts (those with associated and won deals) and separate them out from your other contacts. For example, if you want to see all your active, not closed deals you can track just your prospects.

This article covers the following topics:

- [How the prospects and customers are applied to contacts](#h_b3e6c7d4-3547-4a05-afba-524164570378)
- [Companies and employees and automatic status changes](#h_23ac5c78-ca11-4a1d-a7d6-95f819605484)
- [Viewing and tracking your prospects and customers](#h_cb646ed5-e043-463b-a73b-fd5944d866f6)
- [Adding custom fields and tags for customers and prospects](#h_ee732cb4-e4e7-458f-900f-119872d4b633)

## How the prospects and customers are applied to contacts

As a contact progresses through the sales pipeline, its status changes automatically. As an example, a contact that has just been associated with a deal shows the following status:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell-contact-prospect-status-2.png)

The prospect status is shown as being current. Each status, prospect and customer, has a number of different states to provide more information about the contact and where it is in the sales pipeline. 

**Prospect states**

- **Current Prospect** means that a deal has been associated with the contact. The contact remains a current prospect until the deal is closed or, for some reason, the contact is removed from the associated deal.
- **Lost Prospect** indicates that the associated deal has been changed to **Lost** or **Unqualified**. The contact remains in this state until a new deal is associated with it.
- **Non** **Prospect** indicates that there are no deals associated with the contact.

**Customer states**

- **Current Customer** indicates that a deal has been won. The contact remains a current customer until you manually mark it as a past customer.
- **Past Customer** is selected manually and it’s something you may want to do if you haven't worked with a customer for a while (or if you had deals with the customer before you began using Sell) and you want to renew your relationship.
- **Non Customer** indicates that there are no deals associated with the contact.

Statuses and their states are automatically changed as the status of the contact’s associated deal changes (for example, the contact automatically becoming a prospect when a deal is associated with the contact). You can also set some of these statuses and states manually. However, you cannot manually make changes in the following circumstances:

- A contact with an active deal cannot be manually set as a **Non Prospect** or **Lost Prospect**.
- A contact with at least one Won deal cannot be manually set as a **Lost Prospect**.

Note: To remove all statuses from a contact, you need to first delete all deals associated with a contact.

## Companies and employees and automatic status changes

If a deal is associated with an employee of a company (the employee is the deal's main contact, as shown by the star icon by their name), automatic status changes affect both the employee and the company. This means that both the employee and the company will become current prospects upon deal creation and, when a deal is won, both the employee and the company will become current customers.

## Viewing and tracking your prospects and customers

When viewing your contacts in the **Contacts** page, you can add filters for both prospects and customers using the **Prospect Status** and **Customer Status** fields.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell-customers-prospects-filters.png)

When you add the customers and prospects fields to your filters, you can then select the various states of each to display only those contacts. For example, you might want to create a bulk email communication to all your customers. By selecting **Current Customer** in the filters panel, you can create a list and quickly send them all an email message.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell-email-contacts.png)

## Adding custom fields and tags for customers and prospects

As with leads, contacts, and deals, you can create custom fields and tags for your contacts that have been marked (either automatically or manually) as prospects and customers. For more information, see [Creating and managing custom fields](https://support.zendesk.com/hc/en-us/articles/4408838289562).