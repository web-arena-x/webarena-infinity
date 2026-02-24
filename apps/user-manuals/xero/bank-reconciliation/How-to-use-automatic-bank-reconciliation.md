# How to use automatic bank reconciliation (BETA)

Source: https://central.xero.com/s/article/How-to-use-automatic-bank-reconciliation

---

## Overview

- Turn on automatic (auto) bank reconciliation and view the transactions reconciled by JAX.
- Fix a transaction that JAX has reconciled incorrectly.

Tip

Automatic bank reconciliation is currently in an open beta. We're making enhancements and improvements over the coming months.

## What you need to know

Automatic (auto) bank reconciliation is a feature you can turn on or off for each bank account in your organisation. Only one user in the organisation needs to turn it on for each bank account. You need to be the subscriber or have the advisor user role to turn auto bank reconciliation on or off.

Once you turn auto bank reconciliation on, JAX reviews all future statement lines that import into the bank account, it doesn’t review historical statement lines. JAX reconciles any statement lines that meet the high-confidence criteria.

You can view all the reconciled transactions on the **Reconciled transactions** screen in each bank account.

Before you turn auto bank reconciliation on, [understand how it works](About-auto-bank-reconciliation-powered-by-JAX.md).

Auto bank reconciliation is available to organisations on the Xero Grow (Australia, New Zealand and UK), Growing (US), and Standard (Global) plans and above.

## Turn auto bank reconciliation on or off

To turn auto bank reconciliation on for a specific bank account:

1. In the **Accounting** menu, select **Bank accounts**.
2. Click the name of the bank account you want to turn automation on for.
3. Select the **Reconcile** tab.
4. Click **Auto-reconcile**.
5. Select the checkbox to confirm you want to automatically reconcile statement lines for this bank account, then click **Save**.

To turn auto bank reconciliation off for a specific bank account:

1. In the **Accounting** menu, select **Bank accounts**.
2. Click the name of the bank account you want to turn automation off for.
3. Select the **Reconcile** tab.
4. Click **Auto-reconcile**.
5. Clear the **Automatically reconcile statement lines** checkbox, then click **Save**.
6. (Optional) Provide feedback on why you turned automation off, then click **Send feedback**, or click **Skip**.

## View all reconciled transactions

To view all the reconciled transactions for a bank account:

1. In the **Accounting** menu, select **Bank accounts**.
2. Click **Reconcile [number] items** for the relevant bank account.

   If there are no statement lines to reconcile, click the bank account name, then select the **Reconcile** tab.
3. Click **View all Reconciled**.

If a transaction is reconciled by JAX, it has the label **Rule**, **Match**, **Memory** or **Prediction**, to show the method JAX used. For each transaction, hover over the label to view the reasoning JAX used to reconcile the transaction.

If you reconcile a transaction manually, the transaction has the label **Manual**.

## Fix transactions reconciled incorrectly

### What you need to know

If JAX makes a mistake and reconciles a transaction incorrectly, the best thing to do is to correct it. When you fix a reconciliation, JAX learns from it and is less likely to make the same mistake in the future.

If JAX:

- Creates the wrong account transaction, such as a spend or receive money transaction – use remove and redo to delete the account transaction and move the bank statement line back to unreconciled.
- Matches the wrong invoice or bill – use remove and redo to remove the payment transaction from the invoice or bill. The bank statement line moves back to unreconciled and the invoice or bill returns to awaiting payment.

If the payment transaction is applied to the correct invoice or bill but it’s reconciled with the wrong statement line, you can unreconcile it instead. This removes the connection between the two, but keeps the payment transaction applied to the invoice or bill and moves the statement line back to unreconciled. The payment transaction remains on the **Account Transactions** tab and the statement line remains on the **Bank statements** tab.

You can then navigate back to the **Reconcile** tab to manually reconcile the bank statement line correctly.

### Delete an account transaction

1. On the **Reconciled transactions** screen, select the checkbox for the transaction you want to delete.
2. Click **Remove & Redo**.
3. Click **Delete transaction**.
4. Navigate back to the **Reconcile** tab of the bank account to manually reconcile the statement line correctly.

### Unreconcile an account transaction

1. On the **Reconciled transactions** screen, click the relevant transaction.
2. Under **Has been reconciled with the following payments**, click the payment.
3. Click **Options**, then select **Unreconcile.**
4. Click **OK**.

If there’s a padlock icon on a transaction, this indicates that the transaction is in a locked or closed period so you can’t use remove & redo to delete it. To edit this transaction, you need to [remove the lock date](Set-up-and-work-with-lock-dates.md) or open the closed period first.

## What's next?

Click **Give feedback** on the **Reconciled transactions** screen to share any thoughts you have about automatic bank reconciliation. We value your input to help us keep improving. You need to log in to view and share your feedback.