# Reimburse an employee’s expense claim using Xero payroll (BETA)

Source: https://central.xero.com/s/article/Reimburse-an-employee-s-expense-claim-using-payroll-US

---

## Overview

- Reimburse an employee’s expense claim in the next payroll.
- Set up Xero expenses then assign an expense account in Xero Payroll for clearing reimbursements.
- Mark expenses paid through the suspense account.

Tip

Xero Payroll is currently in closed beta and is restricted to a small number of users.

**1** Before you start

### Check Xero expenses is set up

Before an expense can be received and reimbursed using payroll, the administrator must ensure [Xero expenses](Set-up-expenses.md) is set up for the organization and employees have [access to expenses](New-Expenses-user-permissions.md).

Once set up, your employee can [submit their expense claim](Create-a-new-expense.md).

### Create an expense suspense account in the chart of accounts

You’ll need to add a suspense account in Xero. If you don’t have one already set up, you can create one.

1. In the **Accounting** menu, select **Chart of accounts**.
2. Click **Add Account**, then complete the [required fields](Components-of-an-account-in-your-chart-of-accounts.md).
3. Give the account a name such as ‘Reimbursement claim suspense’.
4. Select the **Enable payments to this account** checkbox.
5. Click **Save**.

### Check payroll category is assigned in Xero Payroll

Check your [reimbursement payroll category](Assign-payroll-categories-to-your-chart-of-accounts.md) is correctly assigned to the suspense account in Xero Payroll.

**2** Check and approve the expense claim

Check the expense claim your employee has submitted and [approve it](Approve-or-decline-expense-claims.md).

**3** Add and submit the reimbursement in a payroll

Add the reimbursement to the employee’s pay in a regular payroll.

1. In the **Payroll** menu, select **Run** **payroll**.
2. In the **New** **payroll** tab, select a pay period, then click **Run** **payroll**.
3. Click the menu icon next to the employee you’re reimbursing, then click **Edit payroll**.
4. Under **Reimbursement**, enter the claim amount.
5. Make any other adjustments as required, then click **Save**.

Once you’re ready to submit the payroll:

1. In the draft payroll, click **Save & continue**.
2. Click **Submit payroll**.

Once you submit the payroll, a bill is created in Xero for the payroll payment.

**4** Mark the expense claim as paid

Once payroll has processed and your employees have been paid, record the expense claim payment against the same suspense account you assigned in the payroll category. This ensures that the accounts payable and suspense expense accounts balance.

1. In the **Purchases** menu, select **Expenses**.
2. Select the **To pay** tab.
3. Next to the employee, click **Pay**.
4. Under **Make a payment**, enter the payment details.
5. Under **Paid From**, select the expense claim suspense account assigned to the payroll category.
6. Click **Add Payment**.

**5** Reconcile payroll

When the employee is paid, [reconcile the payroll payment transaction](Reconcile-a-bank-statement-line-using-Find-Match.md) against the statement line in your bank account in Xero.

## What's next?

Run the [Account Transactions report](Account-Transactions-report-New-US.md) for expense accounts to check that the debit and credit entries for all claims balance.