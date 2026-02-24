# Record a payroll deduction in a non-liability account

Source: https://central.xero.com/s/article/Record-a-payroll-deduction-in-a-non-liability-account

---

## Overview

- Switch a deduction from a liability account to a non-liability account.

## How it works

- You can create a deduction pay item to take payments from an employee's payslip. For example, create a deduction pay item to recoup an advance payment to an employee.
- At the moment, you can only assign a deduction pay item to a liability account. But you can add a manual journal or sales invoice to shift the deduction to a non-liability account.
- Create a manual journal to reallocate the deduction if the repayment is completed within one pay run.
- If the repayment is made over multiple pay runs, create a sales invoice to reallocate the deduction.

## Create a manual journal to reallocate a deduction

[Create a manual journal](Add-import-and-post-manual-journals.md) to shift the deduction to a non-liability account.

You can't use a manual journal to shift the deduction to some [system accounts](Locked-and-system-accounts-in-your-chart-of-accounts.md). Xero reserves these accounts for specific reporting or accounting purposes.

To create the manual journal to shift the deduction:

1. In the **Reporting** menu, select **All reports**.
2. Find and open the **Journal Report**. You can use the search field in the top right corner.
3. Click **Add new journal**, then enter the journal details in the relevant fields.
4. On the first line in the journal, debit the deduction from the liability account.
5. On the second line in the journal, credit the deduction to the non-liability account.
6. Click **Post** to post the journal to the general ledger.

## Create a sales invoice to reallocate a deduction

If you create a sales invoice to reallocate the deduction, rather than a manual journal, you can add more detail about the deduction. You can also track the balance of a loan if an employee makes repayments over several pay periods.

Using a sales invoice to reallocate the deduction will reduce the liability account and record the deduction in the non-liability account.

If repayments are made over multiple pay periods, create one invoice for the full amount of the loan, and add a payment to the invoice for after each pay run is posted.

To shift the deduction using an invoice:

1. Create a sales invoice for your employee in the same way you'd [invoice a customer](Invoice-a-customer.md).
2. Enter the deduction as a line item on the invoice and code it to the desired non-liability account.
3. Approve the sales invoice.
4. [Add a deduction pay item](/s/article/Add-a-custom-pay-item-NZ) and select a liability account (such as a suspense account).
5. Use the deduction pay item to [adjust an employee's pay and post a pay run](/s/article/Process-a-pay-run-and-pay-employees-NZ). This will post the deduction to the liability account.
6. [Enable payments to the liability account](Enable-payments-to-an-account.md) that's linked to the deduction.
7. Add a payment on the sales invoice:

   - Under **Amount paid**, enter the amount deducted from the employee's wages.
   - Under **Account**, select the liability account linked to the deduction.

## What's next?

Run the [Account Transactions report](Account-Transactions-report-New.md) for the liability and non-liability account to check you've shifted the deduction from one account to another.