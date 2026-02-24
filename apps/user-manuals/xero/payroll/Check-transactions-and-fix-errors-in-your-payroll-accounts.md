# Check transactions and fix errors in your payroll accounts

Source: https://central.xero.com/s/article/Check-transactions-and-fix-errors-in-your-payroll-accounts

---

## Overview

- Before you file returns or make tax deductions, check your payroll transactions to find and fix any errors with reconciling or coding

How it works

### Check payroll transactions before filing

It's important to check your payroll transactions in the general ledger periodically to confirm that your balances are correct. You should identify and fix any reconciling or coding errors before filing returns or making tax deductions.

When you post a pay run, Xero creates entries in the general ledger payroll expense and payroll payable accounts (payroll payable accounts might also be called liability accounts). Xero uses the accounts entered in your payroll settings to do this.

You need the advisor or standard + reports user role to find and fix transaction errors.

### Difference between my bank accounts and general ledger accounts in Xero

When you pay your employees from your actual bank account, this transaction appears in your bank account in Xero, ready to reconcile against your wages payable account.

When you post a pay run, Xero records your payroll transaction in general ledger (GL) accounts which keeps track of your payroll finances and provides accurate reporting. For example, employee pay, payroll tax, and superannuation. The general ledger accounts used are based on what you've set up in Payroll settings.

Once you’ve processed the pay run and paid the amounts from your bank account, reconcile your bank account to your Xero accounts to make sure they balance.

Warning

If your bank payments are coded to a payroll expense account instead of a payroll payable account, the expense account balance will be incorrect. The wages payable account will also be incorrect, continuing to show a balance.

Run payroll account balances

### Run the Account Transaction report

Amounts posted to the payroll payable accounts need to be paid to employees or other parties, for example tax payments. Before you do this, we recommend you check the amounts are correct.

1. In the **Reporting** menu, select **All r****eports**.
2. Find and open the **Account Transactions** **report.** You can use the search field in the top right corner.
3. Under **Accounts**, select your payroll accounts.
4. Select a **Date range**.
5. Under **Columns**, select the checkboxes for **Account Code**, **Account Type**, **Credit**, **Date**, **Debit**, **Gross**, **Reference** and **Source**. You can select other columns as needed.
6. Under **Grouping/Summarising**, select **Group by** and **Account**.
7. Click **More**, then select the checkboxes to show opening and closing balances for both **Asset, liability and equity** and **Revenue and expense**.
8. Click **Update** to run the report.
9. Check the balances for your payable accounts are correct.

### What to look for

The wages, tax deduction and other payable accounts balance for previous months should be 0.00 once each month’s payments have been made.

At the end of the financial year, the balance of the wages, tax deduction and other payable accounts should only represent the amounts that aren't yet due for payment.

Check payroll account transactions

### Run the Account transactions report

Once you’ve created your payroll payments and reconciled the transactions in your bank account, check the payments are coded correctly by running the [Account Transactions report](Account-Transactions-report-New.md).

1. In the **Report****ing** menu, select **All r****eports**.
2. Find and open the **Account Transactions** **report**. You can use the search field in the top right corner.
3. Under **Accounts**, select your payroll accounts.
4. Select a **Date range**.
5. Under **Columns**, select the checkboxes for **Account Code**, **Account Type**, **Gross**, **Reference** and **Source**. You can select other columns as needed.
6. Click **Update** to run the report.
7. Review and confirm your transactions are coded to your payroll accounts correctly.

### What to look for

To recognise the expense portion of wages and salaries paid through a pay run, your wages expense account should have **Payroll Expense** as the **Source**.

Payroll payable accounts should have two types of transactions once the payments are made and reconciled:

- **Payroll Expense** records the employee amounts payable
- **Spend Money** transactions record the payments made to employees

Sometimes the wages expense account might show transactions with **Spend Money** as the **Source** if payroll payments in your bank account were reconciled incorrectly. To correct this:

1. From the **Account Transactions report**, click the transaction to see the details.
2. If the transaction is for a wage payment made to an employee for a Xero payroll payment, [edit the spend money transaction](/s/article/Edit-a-spend-or-receive-money-transaction-UK) to change the account to the wages payable account. You can open the transaction in a different tab on your computer screen to do this.
3. Go back to the Account Transactions report and click **Update** to see the new account balances.

## What's next?

Once you've confirmed your account balances and transactions have been recorded correctly, take a look at our guide on [end of year requirements](/s/article/End-of-financial-year-payroll-requirements-UK).