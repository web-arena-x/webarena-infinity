# Add or edit a repeating bill

Source: https://central.xero.com/s/article/Add-or-edit-a-repeating-bill-US

---

## Overview

- Use a template to create a new repeating bill.
- Changes made to existing templates are applied to all subsequent transactions.

What you need to know

- You need the advisor, standard, invoice only (approve and pay) or invoice only (purchases) user role to create templates for bills.
- Once a repeating bill is added, you can approve any drafts, and pay or reconcile those awaiting payment.
- The number of transactions you can approve each month depends on your [pricing plan](https://www.xero.com/pricing-plans/). If you reach the limit, any repeating transactions that were set to approve are saved as draft.
- Repeating templates display on the **Repeating** tab under **Purchases overview** and show the date the next transaction is due to be created.
- All repeating transaction fields are mandatory, except **End Date** and **Reference**.
- Xero automatically creates and saves recurring transactions based on your custom template.
- If your [accounts are locked](Set-up-and-work-with-lock-dates.md) and the template bill date is before the lock date, you can’t set up a repeating bill to automatically approve, or approve and send.
- You can attach files to the template, but they don't attach to each transaction. You'll need to [attach the file](Attach-a-file-to-a-transaction.md) to the transaction each time it's created.

Add a repeating bill

1. There are a number of ways to create a new template, either:
   - In the **Purchases** menu, select **Bills**, click **New bill**, then select**New repeating bill.**
   - In the **Purchases** menu, select **Bills**, select the **Repeating** tab, then click **New repeating bill**.
   - From a contact record, click **New**, thenselect **Repeating bill**.
   - On an existing bill, click **Bill Options**,then select **Repeat**.
2. Enter or edit the information in the repeating transaction fields.
3. (Optional) Drag and drop the item lines to reorder them. Unused lines are removed when you save the transaction.
4. (Optional) To set up an annual repeating template, under **Repeat this transaction every**, select:

   - **52** and **Week(s)** to repeat the bill on a particular day of the week
   - **12** and **Month(s)** to repeat the bill on a particular calendar date
5. Click **Save**.

Edit a repeating bill

1. In the **Purchases** menu, select **Bills**.
2. Select the **Repeating** tab, then find the bill template in the list.
3. Click the supplier's name.
4. Edit the information in the fields as required.
5. Click **Save**.

When you edit an existing template, your changes are applied to all subsequent transactions. You can view your changes in the [History & Notes](View-history-and-notes-for-individual-transactions-and-inventory-items.md) of a transaction.

Repeating transaction fields explained

This section provides guidance and tips on some of the repeating transaction fields.

| **Field** | **Description** |
| --- | --- |
| Repeat this transaction every | When and how often the transactions will be created eg weekly or monthly. |
| Bill Date | The date you want the transactions to begin. It can be in the past (going back to the start of your previous [financial year in Xero](Set-up-your-organisation-s-financial-details.md)), today's date, or in the future. If you use a past date, a series of past-dated transactions are created. |
| Next Bill Date | The date the next transaction is due to be created. This shows when you edit an existing template. If transactions have already been created from a template and you change the next transaction date to a past date, all transactions are created again from that date. You may want to delete or void the original transactions. |
| Due Date | The date that the transaction is due to be paid. If you want the transaction to be created and due on the same date, enter 0 and select the **days after the bill date** option. |
| End Date | (Optional) The last date that a transaction is created for a template. |
| Save As Draft | Select this if:   - The transactions will vary so you can edit each one when it's created - You need to approve each transaction separately - The template has [tracked inventory items](Track-your-inventory.md) |
| Approve | Select this if each transaction can be approved immediately for payment. They'll show on the **Awaiting payment** tab. You'll need to wait for payment before you can reconcile. You can't use this option with transactions that have tracked inventory items. |
| Reference/ Description | If the transaction details should vary, enter placeholders so you can update the information before approving or sending it. Put your cursor in the **Reference** or **Description** field, click **Insert Placeholder** and select the placeholder option. Inserting **Week** into the **Reference** field shows the number of the week of the calendar year. For example, 46. Weeks begin on Monday. You can add and subtract in a placeholder to change the value. For example, [Month-1] displays the previous month to the transaction month. |
| Preview placeholders | Shows you how the placeholders will appear in the transaction. When previewing placeholders, Xero uses today's date as the basis date, not the transaction date. |
| Currency | If you have a pricing plan with multicurrency, you can select a foreign currency that you've already added or click **Add currency** to add a new one. You can also [edit the exchange rate](Edit-the-exchange-rate-for-a-date-or-date-range.md) if required. If you set up repeating bills to be automatically approved, there must be an exchange rate for the transaction date before Xero can approve it. You can’t edit the exchange rate for bills that are automatically approved. |
| Amounts are | Select the tax setting to apply to the amounts. If the item has sales tax, select:   - **Tax Exclusive** to add the tax to each item amount. - **Tax Inclusive** to include the tax with each item amount. Each item shows as tax exclusive when approved. Xero automatically splits out the tax component for reporting. |

## What's next?

Once you've finished editing, you might like to [download or print a bill](/s/article/View-save-or-print-a-bill-or-credit-note?userregion=true).