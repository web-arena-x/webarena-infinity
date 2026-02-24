# Add email templates

Source: https://central.xero.com/s/article/Add-email-templates

---

## Overview

- Add up to 10 templates to reuse for the different types of emails you send from Xero.
- You can add email templates for quotes, invoices (including repeating), receipts, remittance advices, credit notes, purchase orders, and statements.

How it works

- Customise the email message you send to your contacts when emailing transactions from Xero.You can edit the default templates or create new ones.
- Xero provides default email templates for each template type. They’re named 'Basic' in your Email Settings. All email templates contain a default subject, message text, and placeholders.
- You can hide the **View invoice** button and summary information (amount due, due date, invoice number) in your invoice emails.
- To display your logo on emails sent from Xero, [upload this to your invoice template](Add-or-adjust-logo-on-invoices-quotes.md#AddyourlogotoemailssentfromXero).
- [Invoice reminders](How-invoice-reminders-work.md) also use email templates that you can edit when you add the reminder.
- You can't bulk email contacts from Xero, but you can generate a [smart list](Work-with-smart-lists.md) to export the email addresses and copy this to your own email program.

Add an email template

1. Click on the organisation name, then select**Settings**.
2. Under **General**, click **Email settings**.
3. Next to **Templates**, click **Edit**.
4. Under the templates list, click **Add email template**.
5. Select the type of email template you want to set up. Xero enters default text and placeholders into the fields based on your selection.
6. Enter information in the email template.
7. ​Click **Save**.

Select a default email template

If you've set up a custom email template, you can set this as the default for an email template type.

1. Click on the organisation name, then select **Settings**.
2. Under **General**, click **Email Settings**.
3. Next to **Templates**, click **Edit**.
4. Find and open the email template you want to set as default.
5. Select the **Default checkbox**.
6. Click **Save**.

The default option is greyed out if there isn't another email template for the same transaction type. Once you have multiple email templates for the same transaction type, you can select the Default box for the template you want to be the default.

Fields in an email template explained

This section provides guidance and tips on the email template fields.

| **Field** | **Description** |
| --- | --- |
| Type | Select an email template type when creating a new template. Xero enters default text and placeholders into the fields based on your selection: - Credit Note - Purchase Order - Quote - Sales Invoice (which is also the template type Xero uses for prepayments) - Remittance Advice - Repeating Invoice - Statement - Receipt - Auto pay (displays when the organisation has offered [auto pay](Auto-pay-invoices-with-Stripe.md) on a repeating invoice template). |
| Name | Enter a unique name for your template. |
| Default | Select this to make a template the default. To override an existing default, select this option in another email template and click **Save**. |
| Include link to online statement | Select this to include the **Review** **and pay** button in a statement email. |
| Replace existing repeating invoice messages | Select this to replace email messages that accompany [repeating invoices you've set to approve and send](/s/article/Add-or-edit-a-repeating-bill?userregion=true). |
| Include quick link to online invoice and detail summary | Select this to show the **View invoice** button and summary invoice information (amount due, due date, invoice number) in your invoice emails. |
| Message | Edit the email subject and message. Insert placeholders for other content you want to include. |

Insert placeholders

Placeholders are named markers, where content from Xero displays when you send the email. Placeholders have square brackets around them, for example [Contact Name].

Insert placeholders into the subject and message by selecting from the placeholder list. You can also type them in, but you'll need to enter square brackets around the placeholder name, for example [Trading Name] (Xero inserts the placeholder into the template wherever your cursor is.)

###

Placeholders you can use for each email type

Placeholders described where applicable for a statement, credit note, purchase order, invoice reminder, quote, receipt, remittance advice, repeating invoice and a sales invoice:

| | | |
| --- | --- | --- |
| **Placeholder** | **Description** | **Default field in template** |
| Amount Due Without Currency | The amount due on the invoice, or remaining credit on the prepayment, including tax, without the currency code. | Credit note Invoice reminder Sales invoice Repeating invoice |
| Amount Due | The amount due on the invoice, or remaining credit on the prepayment, with the currency code included. | Invoice reminder Sales invoice Repeating invoice |
| Balance with Currency and Symbol | If you email a statement, use this placeholder to show the customer's current statement balance with both the currency symbol and currency type included in the email. | Statement |
| Balance with Symbol | If you email a statement, use this placeholder to show the customer's current statement balance with the currency symbol included in the email. | Statement |
| Contact / Customer First Name | The first name of the contact/customer stored in your contact's details. | Purchase order Invoice reminder Quote Receipt Remittance advice Sales invoice Statement Repeating invoice |
| Contact/Customer Last Name | The last name of the contact/customer stored in your contact's details. | Purchase order Invoice reminder Quotes Receipt Remittance advice Sales invoice Statement Repeating invoice |
| Contact/Customer Name | The name of the contact/customer stored in your contact's details. | Purchase order Invoice reminder Quote Receipt Remittance advice Sales invoice Statement Repeating invoice |
| Credit Total Without Currency | The total credit note value, including tax, without the currency code. | Credit note |
| Credit Total | The total credit note value, including tax, with the currency code included. | Credit note |
| Currency Code | The 3-letter code that represents the currency type. | Credit note Purchase order Invoice reminder Quote Receipt Remittance advice Sales invoice Repeating invoice |
| Currency Symbol | The symbol representing the currency type. | Credit note Purchase order Invoice reminder Quote Receipt Remittance advice Sales invoice Repeating invoice |
| Current Month | The current month of the year, for example, October. You can edit this placeholder to display earlier or later months. For example, [Month+1] will display the month after the invoice date. | Repeating invoice |
| Customer Total Without Currency | The total amount received, including tax, without the currency code. | Receipt |
| Customer Total | The amount received, with the currency code included. | Receipt |
| Delivery Address | The delivery address selected for the purchase order. | Purchase order |
| Delivery Contact | The **Attention** field from the purchase order. | Purchase order |
| Delivery Date | The delivery date from the purchase order. | Purchase order |
| Delivery Details | Includes purchase order delivery address, instructions, contact and phone. | Purchase order |
| Delivery Instructions | The delivery instructions from the purchase order. | Purchase order |
| Delivery Phone Number | The **Telephone** field from the purchase order. | Purchase order |
| Due Date | The due date from the invoice. | Invoice reminder Sales invoice Repeating invoice |
| Expiry | The expiry date of the quote. | Quote |
| Invoice Number | The number of the credit note, invoice etc. | Credit note Invoice reminder Sales invoice Repeating invoice |
| Invoice Total Without Currency | The total invoice amount, including tax, without the currency code. | Invoice reminder Sales invoice Repeating invoice |
| Invoice Total | The total invoice amount, including tax, with the currency code included. | Invoice reminder Sales invoice Repeating invoice |
| Month Year | The current month and year, for example, October 2014. You can edit this placeholder to display earlier or later dates. For example, if the current month is December 2014, [Month Year+1] will display January 2015. | Credit note Purchase order Invoice reminder Sales invoice Repeating invoice |
| Month | The current month of the year, for example, October. You can edit this placeholder to display earlier or later months. For example, [Month+1] will display the month after the invoice date. | Credit note Purchase order Invoice reminder Sales invoice Repeating invoice |
| Online Invoice/Quote Link | The link to the online credit note, invoice, or quote. | Credit note Invoice reminder Quotes Sales invoice Repeating invoice |
| Quote Total Without Currency | The total quote amount, including tax, without the currency code. | Quote |
| Quote Total | The total of the quote, with the currency code included. | Quote |
| Purchase Order Number | The order number from the purchase order. | Purchase order |
| Purchase Order Total Without Currency | The total purchase order value, including tax, without the currency code. | Purchase order |
| Purchase Order Total | The total purchase order value, including tax, with the currency code included. | Purchase order |
| Quote Number | The quote number from the quote. | Quote |
| Reference | The reference from the credit note, invoice or quote etc | Credit note Purchase order Invoice reminder Quote Sales invoice Repeating invoice |
| Remaining Credit Without Currency | The amount due on the invoice, or remaining credit on the prepayment, including tax, without the currency code. | Credit note |
| Remaining Credit | The amount due on the invoice, or remaining credit on the prepayment, with the currency code included. | Credit note |
| Statement Date Range | The period covered by the statement. | Statement |
| Statement Balance | If you're emailing a statement, use this placeholder to show the customer's current statement balance with the currency code included in the email. | Statement |
| Summary | The summary from the quote. | Quote |
| Supplier Total | The amount paid, with the currency code included. | Remittance advice |
| Supplier Total Without Currency | The total amount paid, including tax, without the currency code. | Remittance advice |
| Trading Name | Your organisation's legal/trading name set up in Organisation Settings. | Credit note Purchase order Invoice reminder Quote Receipt Remittance advice Sales invoice Statement Repeating invoice |
| Terms | The terms from the quote. | Quote |
| Title | The title from the quote. | Quote |
| Week Year | The current week and year, for example, 46 2014. Weeks start on Monday. You can edit this placeholder to display earlier or later dates. For example, if the current week is 46 2014, [Week Year+1] will display 47 2014. | Credit note Purchase note Invoice reminder Sales invoice Repeating invoice |
| Week | The current week of the calendar year, for example, Week 8. Weeks start on Monday. You can edit this placeholder to display earlier or later weeks. For example, [Week+1] will display the week after the invoice date. Week calculations follow the ISO 8601 standard. Week 1 starts on Monday and always includes the first Thursday of the new year. The last week of the year will be either 52 or 53. | Credit note Purchase note Invoice reminder Sales invoice Repeating invoice |
| Year | The current year. You can edit this placeholder to display earlier or later years. For example, [Year-1] will display the year before the invoice date. | Credit note Purchase note Invoice reminder Sales invoice Repeating invoice |

####

## What's next?

You can [change your default email template or edit or delete a template](Change-edit-or-delete-email-templates.md).