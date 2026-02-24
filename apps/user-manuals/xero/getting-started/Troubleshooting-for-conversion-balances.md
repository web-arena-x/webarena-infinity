# Troubleshooting for conversion balances

Source: https://central.xero.com/s/article/Troubleshooting-for-conversion-balances

---

## Overview

- If you're having trouble saving or changing your conversion balances, it could be related to a lock date or pre-conversion invoices and bills.
- You must update your conversion balances if you enter additional pre-conversion transactions.

Reset your conversion date

You can reset or change your conversion date if you need to, even if you’ve already started using Xero.

1. In the **Accounting** menu, select **Accounting settings**, then click **Conversion balances**.
2. Click **Conversion Date**.
3. Check the conversion date is correct.
4. Click **Save**.
5. Check the conversion balances are correct.
6. Click **Save**.

If there’s a lock date in place, you might not be able to save the change if you’ve got the standard user role. You’ll need to ask someone with the advisor user role to make the change instead.

After you’ve saved the conversion date and balances, Xero may prompt you to add transactions to match the Accounts Receivable and Accounts Payable balances. The next section of this article tells you how to create matching transactions if you need to.

Your historical invoices or bills don't match your conversion balance

If you’ve entered balances against the accounts receivable and accounts payable accounts, you also need to add the invoices, bills or credit notes making up those two balances. If the totals of the transactions and the accounts receivable and accounts payable balances don't exactly match, Xero won't save your conversion balances.

Xero shows any difference between the accounts receivable and accounts payable balances and historical transactions after you try to save the conversion balances. You can [add or delete transactions individually](Enter-unpaid-invoices-and-bills-for-your-conversion-balances.md) from the error page. If you have a lot of transactions to add, you can [import them](Import-customer-invoices.md), then save the conversion balances.

If you continue to have problems, check that you've used Xero's [system accounts](Locked-and-system-accounts-in-your-chart-of-accounts.md) to enter the accounts receivable and accounts payable balances. You should also check that the transactions:

- Have been approved
- Are made up only of invoices, bills, credit notes and expenses
- Don't include spend or receive money transactions
- Are dated before the conversion date
- Are entered with the outstanding amounts, not the original amounts

Your accounts are locked

You can use lock dates to prevent changes being made during a past period. To check lock dates:

1. In the **Accounting** menu, select **Accounting settings**.
2. Click **Financial settings**.

If your accounts are locked, only users with the [advisor user role](Adviser-user-role.md) can:

- Update data that occurs before the lock date.
- [Change or remove the lock date](Set-up-and-work-with-lock-dates.md) in the organisation's financial settings.

You can also [invite your accountant or bookkeeper](Add-a-new-user-to-your-organisation.md) into your organisation with the advisor user role and get them to make the change.

If your accounts haven't been locked or your conversion date is not in a locked period, you can update the conversion balances even if you have the [standard user role](Standard-user-role.md).

Your opening balances are not updating or have been reversed

If you record your opening balances using manual journals and then save any balances in the Conversion Balances screen, Xero will create conversion journals to adjust the opening balances back to what you've saved. This also applies if there are transactions in Xero that are dated prior to your conversion date.

Xero will always ensure that the opening balances match the saved balances in the Conversion Balances screen by creating conversion journals. Xero uses these balances as the starting point for reporting. Because of this, you need to record opening balances in the Conversion Balances screen rather than using manual journals.

### Example

If the conversion balance for your sales account is 500, but you've already entered a pre-conversion invoice with 300 coded to sales, the conversion journal will only post an amount of 200 for the sales account.

You could run the [Account Transactions report](Account-Transactions-report-New.md) to see any transactions that have dates before your conversion date, and the conversion journals. You'll need to run the report for a period that ends on the day before your conversion date. Eg if your conversion date is 1 November 2018, run the report from a date that is before your conversion date, up to 31 October 2018. The report will show:

- Transactions dated before your conversion date
- The conversion journals for each account
- The total showing for each account equalling the last saved conversion balance for the account

## What's next?

If you still need help with your conversion balances, contact Xero support.