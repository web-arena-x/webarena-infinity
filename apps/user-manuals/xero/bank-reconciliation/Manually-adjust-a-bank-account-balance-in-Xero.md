# Manually adjust a bank account balance in Xero

Source: https://central.xero.com/s/article/Manually-adjust-a-bank-account-balance-in-Xero

---

## Overview

- If you need to adjust the balance of a bank account, we recommend that you first try to correct the underlying transactions.
- If you're unable to correct the underlying transactions, you can adjust the balance by adding a transaction or setting up a bank account as a current asset.

## What you need to know

- You can't post a manual journal to a bank account in Xero. This is to ensure that auditing and reporting on the account is as accurate as possible.
- The bank accounts in Xero should reflect exactly what happened in the actual bank account. [Compare the statement balance in Xero to your actual bank balance](Compare-the-statement-balance-in-Xero-to-your-actual-bank-balance.md) to identify and fix any errors before you make a manual adjustment or set up a bank account as a current asset.

## Add a transaction to adjust the balance

When you add a spend or receive money transaction, Xero posts a journal to record the transaction in the bank account.

1. Add a [spend money](Add-a-spend-money-transaction.md) or [receive](Add-a-receive-money-transaction.md) [money](Add-a-receive-money-transaction.md) transaction to record the journal side of the entry.
2. [Mark the transaction as reconciled](Reconcile-an-account-transaction-without-an-imported-bank-statement.md) to create a bank statement line in the bank account.
3. Run the [Journal report](Journal-report.md) to view the journals posted.

[Set up a suspense or clearing account](Add-or-edit-an-account-in-your-chart-of-accounts.md) in your chart of accounts if you have a large number of entries at once, or you want to show the movement in the account over a period of time.

If a client sends you a spreadsheet summarising all their transactions for a month, it may be easier to set up their bank accounts as current assets to save adding spend or receive money transactions.

### Example 1: sales deposited into a bank account

To account for sales of 100.00 deposited into your bank account, add a receive money transaction for 100.00 coded to the sales account. Then manually mark the account transaction as reconciled.

This will create a journal that debits the bank account 100.00, and credits the sales account 100.00.

### Example 2: many lines of coding using a suspense or clearing account

You withdraw 20,000.00 from your bank account for payroll and you want to code them to 200 separate expense accounts so you can itemise by employee.

1. Set up a suspense or clearing account in your chart of accounts.
2. Create a spend money transaction and code it to the suspense or clearing account. This will create a debit to the suspense or clearing account for 20,000.00 and a credit to the bank account for 20,000.00
3. [Add a manual journal](Add-import-and-post-manual-journals.md) to record debits to the employee accounts as required, and a credit to the suspense or clearing account for 20,000.00.

   Alternatively you could use a CSV file to [import a manual journal](Add-import-and-post-manual-journals.md) with multiple lines.
4. If a bank statement line has been imported, reconcile the account transaction, or manually Mark as Reconciled if the bank statement line can't be imported.

### Example 3: movement over time

The balance in the bank account has gone up by 788.00 during the month and you want to record the overall movement and summary of income and expenses:

| | |
| --- | --- |
| Sales received | +1,600 |
| Repairs and maintenance | -122 |
| Advertising | -600 |
| Office expenses | -90 |
| **Profit** | **788** |

1. Add a receive money transaction for 788.00 and code it to the suspense or clearing account. This will create a debit to the bank account for the overall increase of 788.00 and a credit to the suspense or clearing account.
2. Add a manual journal to debit the suspense account for 788.00 and credit the relevant income or expense accounts for each amount. This will clear the suspense account and show the individual account movements over the period.

## Set up a bank account as a current asset

If you have a bank account that only has a few transactions, or you want to show the movement in an organisation for a period, you could set the bank account up as a current asset in your chart of accounts, instead of a bank account.

A manual journal can be posted to a current asset account, so this may work for accounts where interest and tax transactions happen once a month or quarter, such as term deposits.

## What's next?

Find out reasons why your [statement balance in Xero and your actual bank account balance are different](Why-are-the-statement-balance-and-balance-in-Xero-different.md).