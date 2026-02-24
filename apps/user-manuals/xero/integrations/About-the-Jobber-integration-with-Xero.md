# About the Jobber integration with Xero

Source: https://central.xero.com/s/article/About-the-Jobber-integration-with-Xero

---

## Overview

- Connect Jobber to Xero to automatically sync contacts, invoices and invoice payments from Jobber to Xero. The sync is one-way only.
- Learn how the fields in Jobber match up to the fields in Xero.

## How it works

Connect Jobber to your Xero organisation to sync contacts, invoices and inventory items (products and services) from Jobber to Xero. The connection is one-way, so for changes to appear in both Jobber and Xero, make them in Jobber.

Once connected, when you create or update a contact or invoice in Jobber, this also appears in Xero:

- Draft invoices created in Jobber appear in the **Draft** tab in Xero.
- When an invoice is emailed to the client or marked as sent in Jobber, the invoice moves to the **Awaiting Payment** tab in Xero.
- A Jobber product or service included on an invoice [adds an untracked inventory item in Xero](Add-an-inventory-item.md).
- When payments are added to an invoice in Jobber, these are reflected in Xero. Once the invoice is fully paid in Jobber, the invoice moves to the **Paid** tab in Xero.
- Deleting a client in Jobber archives the contact in Xero.

Historical invoices or existing clients in Jobber that were created before the connection was set up don’t automatically sync to Xero. Update the existing invoice or client in Jobber to sync the invoice or client to Xero.

The Jobber to Xero integration is free. Xero organisations on [business plans](Xero-pricing-plans.md) can connect with Jobber accounts on the Grow or Connect plan. If you don’t have a Jobber account, you can view their plans on [Jobber's website](https://getjobber.com/pricing/).

## Connect Jobber to Xero

You can [connect Jobber to your Xero organisation](Getting-started-with-Xero-Connected-Apps.md) from the Xero App Store.

## How the fields match up between Jobber and Xero

### Clients created or updated in Jobber

When you create a new client or edit an existing client in Jobber, the following details update in Xero:

| | | |
| --- | --- | --- |
| **Jobber field** | **Xero field** | **Additional details** |
| Title | Contact name | - |
| First Name | Contact name First Name | - |
| Last Name | Contact name Last Name | - |
| Company Name | Contact name | If the first name and last name is entered in Jobber, select the **Use company name as primary** checkboxto update using the company name in Xero. |
| Phone number | Phone number | If there are multiple phone numbers added for the Jobber client, the phone number marked as primary will update in Xero. |
| Email | Email | If there are multiple emails added for the Jobber client, the email marked as primary will update in Xero. |
| Address | Billing address | If the billing address isn’t entered in Jobber, the address entered in Jobber is used. |
| Billing Address | Billing address | - |

### Invoices created or updated in Jobber

When you create a new invoice or editing an existing invoice in Jobber, the following details update in Xero:

| | | |
| --- | --- | --- |
| **Jobber field** | **Xero field** | **Additional details** |
| Client | Contact | - |
| Issued date | Issue date | - |
| Payment due | Due date | - |
| Product / Service Name | Item | The **Item** field in Xero updates if the product or service selected is from your [products and services list](https://help.getjobber.com/hc/en-us/articles/115009735848-Products-Services-List#h_9b552317-b7f6-4e46-986f-b99a7eec7d97) (Jobber website). |
| Product / Service Description | Description | - |
| Qty | Qty | - |
| Unit Price | Price | - |
| Discount | Disc | - |
| Tax rate | Tax rate | - |
| Invoice number | Reference | - |
| Invoice ID | Invoice number | The numbers after **/invoices/** in the URL of the jobber invoice is the invoice ID. |
| Payments | Payments | Includes deposits on the Jobber invoice. Tips and overpayments won't sync to Xero. You'll need to manually add this in Xero. |

### Products and services updated in Jobber

Any products or services created or updated in Jobber sync to Xero when they appear on a Jobber invoice:

| | | |
| --- | --- | --- |
| **Jobber field** | **Xero field** | **Additional details** |
| Name | Name | Xero will only sync up to 50 characters. |
| Description | Description | Updates the purchase and sell description. |
| Cost ($) | Cost price | - |
| Unit price ($) | Sale price | - |

## What's next?

Find out more about [working with connected apps in Xero](Xero-Connected-Apps.md).