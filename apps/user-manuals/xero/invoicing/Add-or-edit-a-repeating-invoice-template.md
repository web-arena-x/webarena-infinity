# Add or edit a repeating invoice template

Source: https://central.xero.com/s/article/Add-or-edit-a-repeating-invoice-template

---

## Overview

- Add a repeating invoice template for invoices you create and send regularly.
- Read through our table of repeating transaction fields to understand what each field means.

How repeating invoices work

Based on your custom template, Xero automatically creates and saves recurring transactions, and emails recurring invoices for you. You can also [create a repeating invoice directly from an accepted quote](Copy-a-single-quote-or-multiple-quotes.md).

When you set up a repeating invoice, all fields are mandatory except for **End Date** and **Reference**. To reorder invoice lines, drag and drop them. Unused lines are automatically removed when you save the transaction. You can also set up online payments for the invoice from the **New Repeating Invoice** screen. For more advanced customisation for your repeating transactions, search the [Xero App Store](https://apps.xero.com/function/invoicing-jobs?utm_source=xc&utm_medium=internal-referral&utm_campaign=invoicing&utm_content=invoicing-jobs) for a suitable app.

You can [attach files to a repeating template](Attach-a-file-to-a-transaction.md), but these files aren't automatically included with each new invoice that's generated. To include an attachment, you’ll need to add it to the invoice each time it’s created. Similarly, if you create a repeating invoice from an existing invoice that has an attachment, the file isn't copied across to the repeating template.

If you update an inventory item's selling price on the template, the updated price won’t flow through to new repeating invoices. The price needs to be manually changed on the invoice after it’s created.

If a repeating invoice is set to be created on the 31st of the month, Xero automatically adjusts the date for shorter months. The invoice will instead be generated on the last day of that month.

When you select the **Approve for Sending** option, repeating invoices will only send the first invoice if the invoice date is set in the future. If the invoice date is today or in the past, the initial invoice will be approved but not automatically sent. To have repeating invoices start from today, the initial invoice needs to be created manually.

Repeating templates are shown on the **Repeating** tab with the date of the next transaction.

Tip

Your [pricing plan](https://www.xero.com/pricing) determines the number of transactions you can approve each month. If you reach the limit, repeating transactions that were set to approve are saved as draft.

Add or edit a repeating invoice template

### Add a repeating invoice template

1. In the **Sales** menu, select **Invoices**.
2. Select the **Repeating** tab, then click **New Repeating Invoice**.
3. Enter your information in the repeating transaction fields.
4. (Optional) To accept payments from credit card, debit card, PayPal or other payment services, click **Manage**under **Online payments** and [follow the steps](Assign-edit-or-delete-payment-services.md).
5. (Optional) To set up an annual repeating template, under the **Repeat this transaction every** option:
   - Enter **52** and select **Week(s)** – to repeat on a particular day of the week
   - Enter **12** and select **Month(s)** – to repeat on a particular calendar date
6. Click **Save**.

### Edit a repeating invoice template

1. In the **Sales** menu, select **Invoices**.
2. Select the **Repeating** tab.
3. Click the existing template from the list.
4. Edit your information in the repeating transaction fields.
5. Click **Save**.

If you're editing an existing template, your changes are applied to all subsequent transactions. You can view your changes in the [History & Notes](View-history-and-notes-for-individual-transactions-and-inventory-items.md).

Add a repeating invoice from an existing invoice

If you've invoiced a customer who regularly purchases the same items, create a repeating invoice from their last invoice. This will copy across all existing details which you can edit before saving the repeating template.

1. In the **Sales** menu, select **Invoices**.
2. Click into the **Awaiting Payment** or **Paid** tab and select an invoice.
3. Click the menu icon , then select **Repeat**.
4. Update any details as required for the repeating invoice.
5. Click **Save**.

For more tips on how to save time invoicing and get paid faster, see our guide [Get your invoices paid faster](/s/guide/a5B3m000000UU3vEAG/get-your-invoices-paid-faster).

Warning

The [reply-to](Email-settings.md) email address for repeating invoices is based on your email settings. You can change this to your email address by re-saving the repeating template, if needed.

Repeating transaction fields explained

This section provides guidance and tips on some of the repeating transaction fields.

| **Field** | **Description** |
| --- | --- |
| Repeat this transaction every | When and how often the transactions will be created eg weekly or monthly. |
| Invoice Date | The date you want the transactions to begin. It can be in the past (going back to the start of your previous [financial year in Xero](Set-up-your-organisation-s-financial-details.md)), today's date, or in the future. If you use a past or current date, a series of past-dated transactions are created. To automatically send the first invoice, ensure you select a future date. If your accounts are [locked](Set-up-and-work-with-lock-dates.md) and the start date is before the lock date, you won't be able to set up a repeating transaction that's automatically approved, or approved and sent. Future-dated transactions are created on that date and shown on the relevant tab. |
| Next Invoice Date | Editing existing templates only. The date the next transaction is due to be created. If transactions have already been created from this template and you change the next transaction date to a past date, all transactions are created again from that date. You may want to delete or void the original transactions. |
| Due Date | The date that the transaction is due to be paid. If you want the transaction to be created and due on the same date, enter 0 and select the **days after the invoice date** option. |
| End Date | (Optional) The last date that a transaction is created for this template. |
| Save As Draft | Select **Save As Draft** if:   - The transactions will vary so you can edit each one when it's created - You need to approve each transaction separately - The template has [tracked inventory items](Add-an-inventory-item.md) |
| Approve | Select **Approve** if each transaction can be approved immediately for payment. They'll show on the **Awaiting Payment** tab. You'll still need to send each invoice to your customer, and wait for the invoice payment before you can reconcile. You can't use this option with transactions that have tracked inventory items. |
| Approve for Sending | Select **Approve for Sending** if each transaction can be approved for payment and sent to the customer automatically. The invoice will be emailed on the date it's created, based on the schedule you've entered on the repeating invoice template. |
| Confirm Message Settings | This populates after you click **Save**if you select **Approve for Sending**. You can edit the [email template](Add-email-templates.md) for the customer, if needed. If you want the invoice status to automatically update once it's sent, select **Mark as sent.** Changes to the message settings will apply to all future invoices created using the email template. |
| Reference/ Description | If the transaction details should vary, enter placeholders so you can update the information before approving or sending it. Put your cursor in the **Reference** or **Description** field, click **Insert Placeholder** and select the placeholder option. Inserting **Week** in the **Reference** field shows the number of the week of the calendar year. For example, 46. Weeks begin on Monday. You can add and subtract in a placeholder to change the value. For example, [Month-1] will display the previous month to the transaction month. |
| Preview placeholders | Shows how the placeholders will appear in the transaction. When previewing the placeholders, Xero will use today's date as the basis date not the transaction date. |
| Online payments | Set up online payments so you can receive payments from credit card, debit card, PayPal and other payment services. Only one payment method can show on repeating invoices at a time. If you have multiple payment services, including Stripe autopay, it takes priority and shows on the online invoice for your customer. If you want to use another payment service for repeating invoices, you need to remove Stripe autopay from the invoice template. |
| Currency | If you have a business edition plan with multicurrency, you can select a foreign currency that you've already added or click **Add currency** to add a new one. You can [edit the exchange rate](Edit-the-exchange-rate-for-a-date-or-date-range.md) if required. If you set up repeating invoices to be automatically approved, there must be an exchange rate for the transaction date before it can be saved as approved. Invoices that have been automatically approved can't have the exchange rate edited. |
| Amounts are | Select the tax setting to apply to the amounts. If the item has GST, select:   - **Tax Exclusive** to add the tax to each item amount. - **Tax Inclusive** to include the tax with each item amount. Each item shows as tax exclusive when approved. Xero automatically splits out the tax component for reporting. |

## What's next?

Once you've finished editing, you might like to [download or print an invoice](Print-or-preview-a-customer-invoice.md).