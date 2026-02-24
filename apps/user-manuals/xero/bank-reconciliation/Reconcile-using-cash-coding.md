# Reconcile statement lines in bulk

Source: https://central.xero.com/s/article/Reconcile-using-cash-coding

---

## Overview

- Reconcile statement lines in bulk using cash coding.
- Cash coding creates new receive or spend money transactions for cash payments, so isn't suitable if the transaction is already entered in Xero.

About cash coding

### How it works

Cash coding in Xero is a fast and easy way to reconcile multiple statement lines relating to cash transactions in one go.

When you use cash coding to reconcile a statement line, you create a receive or spend money transaction.

Statement lines are displayed in a spreadsheet format so it's easy to sort and code similar transactions. You can view up to 200 lines at once. Work through them one by one or select multiple lines to reconcile at the same time.

To avoid creating duplicate transactions, you shouldn't use cash coding if you've already entered a transaction in Xero.

Cash coding isn't available to organisations on the Xero Starter pricing plan. You need to [upgrade your pricing plan](Changing-pricing-plan.md) for cash coding to be available.

You need to have the advisor or standard + cash coding user role to use cash coding. Users with manage users permission can [update a user role](Change-a-user-s-role-or-permissions.md) to include this option.

### Before you start

Only reconcile statement lines using cash coding that relate to cash you've spent or received.

To avoid reconciling statement lines that match an invoice or other transaction you've already entered in Xero, [reconcile the following items](Bank-reconciliation-in-Xero.md) in the Reconcile tab first:

- Sales invoices and bills
- Credit note refunds
- Overpayments and prepayments
- Expense claims
- Transfers between bank accounts
- Any spend or receive money transactions already entered

Access cash coding

1. In the **Accounting** menu, select **Bank accounts**.
2. Click the bank account name that you want to reconcile.
3. Select the **Cash coding** tab.

Apply bank rules using cash coding

In cash coding, statement lines with the **Description**, **Account** and **Tax Rate** fields pre-populated indicates that a [bank rule](Create-a-bank-rule.md) is applied.

1. Select the checkbox next to each bank statement line with a bank rule applied.
2. (Optional) To apply the same rule to multiple statement lines, select each statement line. Click **Apply rule**, then select the rule you want to apply.
3. Click **Save & Reconcile Selected**.

Enter details manually using cash coding

For any remaining statement lines, you can fill out the relevant fields manually and reconcile in bulk.

When entering details manually, the **Payee**, **Description** and any tracking fields aren't mandatory. If you don't enter a payee, Xero creates the account transaction against a contact named **Unknown**.

If there are any statement lines you need to allocate to different accounts, you can split the statement line or create a new bank rule.

### Code and reconcile lines with the same details

If you want to code multiple lines using the same details:

1. Select the checkbox for each statement line with the same details that you want to code.
2. In the **Account** field, select the account you want to allocate the selected statement lines to. When you move to the next field, the selected account is automatically applied to all lines.
3. (Optional) Enter details for the remaining fields.
4. Click **Save & Reconcile Selected**.

### Split a transaction

Split a statement line to allocate it to different accounts, tracking categories or tax rates.

1. Click the arrow at the end of the bank statement line, then select **Split**.
2. Enter the transaction details, then click **Save**.
3. Click **Save & Reconcile Selected**.

If you've split a transaction but it won't save, check the following:

- Empty rows – if you have an empty row, you need to delete it before you can save the transaction. Click the delete icon at the end of the blank line.
- **Account** and **Tax Rate** fields – each line needs to have an account and tax rate selected.
- The split transaction equals the bank statement line total – the total of the split transaction lines needs to match the total of the bank statement line.

Cash coding tips

Take a look at these tips to help you reconcile more efficiently.

- Sort statement lines by a specific column to group similar transaction lines together. Do this first to avoid losing any changes.
- Click **Shortcut keys** to view time-saving shortcuts.
- By default, cash coding doesn’t show [statement lines with a suggested match in Xero](Reconcile-a-bank-statement-line-using-Find-Match.md). To see them, select the **Show lines with suggested matches** checkbox. A green tick shows at the end of the statement line if there's a suggested match.

- Reconcile fewer than 100 statement lines at a time.
- If you've already [entered a payee as a contact](Add-a-new-contact.md), start typing the contact's name in the **Payee** field, then select them from your contact list. This avoids creating a duplicate contact if the payee on the statement line is different to the contact name in Xero.
- Hover over the note icon to view a [comment added to the statement line](Add-a-comment-to-a-bank-statement-line.md).
- Click the bank account name to easily switch between bank accounts.
- [Create bank rules for regular transactions](Create-a-bank-rule.md) while cash coding, so you don't have to code them again next time.

## What's next?

To see all your cash transactions for a particular period or account code, run the [Account Transactions report](Account-Transactions-report-New.md) on a cash basis.