# Reimburse an employee’s expense claim using Xero payroll

Source: https://central.xero.com/s/article/Pay-an-employee-s-expense-claim-using-payroll

---

## Overview

- Reimburse an employee’s expense claim in the next pay run.
- Set up Xero Expenses, then create an expense suspense account in the chart of accounts for clearing reimbursements.
- Create reimbursement pay items and mark expenses paid through the suspense account.

**1** Before you start

### Check Xero Expenses is set up

Before an expense can be received and reimbursed using payroll, the administrator must ensure [Xero Expenses](Set-up-expenses.md) is set up for the organisation and employees have [access to expenses](New-Expenses-user-permissions.md).

Once set up, your employee can [submit their expense claim](Create-a-new-expense.md).

### Create an expense suspense account in the chart of accounts

If this is the first time you've reimbursed an employee using Xero payroll, you'll need to create a new suspense account in Xero:

1. In the **Accounting** menu, select **Chart of accounts**.
2. Click **Add Account**, then complete the [required fields](Components-of-an-account-in-your-chart-of-accounts.md).
3. Give the account a name such as ‘Expense claim suspense’.
4. Select the **Enable payments to this account** checkbox.
5. Click **Save**.

### Create a reimbursement pay item for expenses

If this is the first time you've reimbursed an employee using Xero payroll, you'll need to create a new reimbursement pay item for expenses in Xero payroll:

1. In the **Payroll** menu, select **Payroll settings**.
2. Select the **Pay Items** tab, then click **Reimbursements**.
3. Click **Add**, then select the GST setting you want.
4. Name the pay item and complete the other details as needed.
5. Under **Account**, select the suspense account created.
6. Click **Add**.

After setting up your new reimbursement pay item, you can use it in a pay run to make a one-time adjustment. To include it in each pay run for recurring expenses, add it to your employees' pay templates.

**2** Check and approve the expense claim

Check the expense claim your employee has submitted and [approve it](Approve-or-decline-expense-claims.md).

**3** Add the reimbursement to a draft pay run

Add the reimbursement pay item to the employee’s pay template or payslip. For recurring expenses, [add it to the employee’s pay template](/s/article/Create-or-edit-a-pay-template-for-an-employee-NZ).

If the reimbursement is a one-off payment in a single pay period, such as travel or office supplies, add it to the employee's draft payslip:

1. In the **Payroll** menu, select **Pay employees**.
2. Select the draft pay run, then click the employee you’re reimbursing.
3. Next to **Reimbursements**, click **Add**.
4. Select the reimbursement pay item.
5. Add a description for the employee's payslip.
6. Enter the claim amount.
7. Click **Save**.

**4** Process the pay run and reconcile payroll

[Post the pay run](/s/article/Process-a-pay-run-and-pay-employees-NZ), then process the payment to your employees.

When the statement line for the payroll payment appears in your bank account in Xero, [reconcile the payroll payment](Reconcile-a-payroll-payment.md) against the wages payable account.

**5** Mark the expense claim as paid

Record the expense claim payment against the same suspense account you used to create the reimbursement pay item. This ensures that the accounts payable and suspense expense accounts balance.

1. In the **Purchases** menu, select **Expenses**.
2. Select the **To pay** tab.
3. Next to the employee, click **Pay**.
4. Under **Make a payment**, enter the payment details.
5. Under **Paid From**, select the Expense claim suspense account you created earlier.
6. Click **Add Payment**.

## What's next?

Run the [Account Transactions report](Account-Transactions-report-New.md) for expense accounts to check that the debit and credit entries for all claims balance.