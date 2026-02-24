# Compare the statement balance in Xero to your actual bank balance

Source: https://central.xero.com/s/article/Compare-the-statement-balance-in-Xero-to-your-actual-bank-balance

---

## Overview

- If your statement balance in Xero doesn't match your actual balance for the same date, either the opening balance in Xero is wrong or there's an error in the bank statement lines in Xero.
- Follow these steps to identify and fix the error.

**1** Check the opening bank balance is entered correctly and saved

1. Make sure the [opening balance entered for the bank account](Add-your-opening-bank-balances-in-Xero.md) matches the actual closing bank balance, as per your online banking or paper statements, for the day before you started using Xero.
2. Check that [uncleared funds from your previous accounting system](/s/article/Enter-uncleared-cheques-when-converting-to-Xero?userregion=true) have been entered using a suspense account and that they aren't included in the conversion balance.
3. Check the conversion balances have been confirmed and saved.

**2** Identify when the error happened

Once you've confirmed the opening balance is correct, identify the date the error happened.

1. Find the date the statement balance in Xero last matched the actual bank account balance.
2. Run the [Bank Reconciliation Summary report](/s/article/Bank-Reconciliation-Summary?userregion=true) for a month from this date. For example, if the balances last matched on 31 March, run the Bank Reconciliation Summary report as at 30 April.
3. Compare the balance shown on the report against the actual bank balance at this date. For example, compare the statement balance in Xero as at 30 April with your actual bank balance for the same date. If they match, run the report for the next month and do the same.
4. When the balances don't match it means the error has occurred within this period. For example, if the balances don't match at 31 May, it means the error happened in May.
5. Run the Bank Reconciliation Summary report for a date within the month to narrow down the date the error happened. For example, run the report as at 15 May and compare the balances. Keep doing this until you've identified the date where the balances go out.

**3** Identify the error

Once you've identified the date range where you think the error happened, identify what the error is. Check for:

- A missing bank statement line
- A duplicate bank statement line (one that was imported twice into Xero)
- A bank statement line deleted in error
- An account transaction that was marked as reconciled by mistake (which has created a manual bank statement line)

To do this:

1. Compare the information in the Bank Statement report in the [Bank Reconciliation report pack](/s/article/Bank-Reconciliation-Summary?userregion=true) to your actual bank statement, line by line. Any difference you identify might be the cause of the error.
2. Check the Statement Exceptions report in the Bank Reconciliation report pack for any deleted, manual and duplicate bank statement lines to confirm if they're correct:

   - **Deleted** – It's correct to delete a statement line if you accidentally imported it more than once. However, if you deleted the line in error, you might need to restore it so your balances match.
   - **Manual** – Manually marking a bank statement line as reconciled is ok if you couldn't import the statement line from your bank account. If you marked a transaction as reconciled, then imported its statement line, you'll need to delete the statement you created.
   - **Duplicate** – Duplicate bank statement lines are usually double ups. [View the bank statement lines](View-bank-statements-and-bank-statement-lines.md) that were imported to check.

If you have many statement lines to work through, you might find it easier to export both your bank statement in Xero and your actual bank statement to an Excel or Google spreadsheet.

**4** Fix the error

Now that you've found the error in Xero, fix it as follows:

- **Missing bank statement line** – [Import a bank statement file](About-manually-importing-bank-statements.md) for the missing transaction. If you can't import it, you'll need to [manually mark the transaction as reconciled](Reconcile-an-account-transaction-without-an-imported-bank-statement.md).
- **Duplicate bank statement line** – If the statement line was duplicated in error, [delete it](Delete-or-restore-a-bank-statement-line.md).
- **Deleted bank statement line** – If the statement line was deleted by mistake, [restore it](Delete-or-restore-a-bank-statement-line.md).
- **Manual bank statement line** – If you marked a transaction as reconciled, then imported its statement line, [delete the manual bank statement](Delete-a-bank-statement.md).

## What's next?

Now that the statement balance in Xero matches your actual bank balance, make sure the [balance in Xero matches the statement balance in Xero](Why-are-the-statement-balance-and-balance-in-Xero-different.md).