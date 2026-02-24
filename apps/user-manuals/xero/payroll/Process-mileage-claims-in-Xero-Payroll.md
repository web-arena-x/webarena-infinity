# Process mileage claims in payroll

Source: https://central.xero.com/s/article/Process-mileage-claims-in-Xero-Payroll

---

## Overview

- Process mileage claims in payroll for tax and reporting purposes.

How it works

If you’ve paid your employee for mileage using [expenses in Xero](About-Xero-Expenses.md) or another expense app, process these through payroll for tax and reporting purposes. This helps you avoid double accounting or paying your employee twice.

Once you’ve processed your employee’s mileage claims in expenses, set up two allowance pay items in payroll for the taxable and non-taxable portions of the claim. If you haven’t already, add a post-tax deduction pay item to offset against the allowances. Both the allowances and deduction must be coded to the same expense account.

You can then process the allowances and deduction as part of your pay run.

For more information on [withholding allowances](https://www.ato.gov.au/Business/PAYG-withholding/Payments-you-need-to-withhold-from/Payments-to-employees/Allowances-and-reimbursements/Withholding-for-allowances/), please check the ATO website.

Set up mileage pay items

### Before you start

Choose a mileage expense account to record your employee’s mileage expenses in payroll. You can either use the account you code your mileage claims to in your expense app, or [set up a separate expense clearing account](Add-or-edit-an-account-in-your-chart-of-accounts.md).

If you want to set up a separate clearing expense account, you can call it 'Mileage (processed via payroll)' or similar. This will help you differentiate between the mileage claimed in expenses or your expense app and the same mileage expenses processed through payroll.

You should also process the mileage claims in your expense app. If you're using expenses in Xero, [record a payment on the expense claim](Record-expense-claim-payment.md) your employee submitted.

### Add allowance pay items

Add two allowance pay items, one for the taxable portion and the other for the non-taxable portion.

1. In the **Payroll** menu, select **Payroll settings**.
2. Select the **Pay Items** tab.
3. Click **Add**, then select **Allowance**.
4. Select the allowance type and name the pay item. You can call it ‘Mileage (taxable)’ or similar.
5. Set the rate type as be per unit (in kilometres). The rate will be the taxable portion of the tax rate. For example, if the full rate is 78 cents and the ATO approved rate is 68 cents, the taxable portion will be 10 cents.
6. Select the relevant expense account. This can either be the expense account used to process mileage claims, or the new separate clearing expense account.
7. Complete the other details as needed and click **Add**.

Repeat these steps to create the second allowance pay item and call it ‘Mileage (non-taxable)’ or similar. Set this pay item as exempt from PAYG, and ensure the rate is ATO approved.

### Add a deduction pay item

1. In the **Payroll** menu, select **Payroll settings**.
2. Select the **Pay Items** tab.
3. Select **Deductions**.
4. Click **Add**, then select the deduction type.
5. Name the pay item. You can call it ‘Mileage paid via expenses’ or similar.
6. Select the relevant expense account. This must be the same account as your allowance pay items.
7. Ensure the **Reduces PAYG Withholding** checkbox is empty.
8. Click **Add**.

Include a claim in a pay run

Tip

For employees receiving mileage reimbursements regularly, [add the allowance and deduction pay items to their pay template](Create-or-edit-a-pay-template-for-an-employee.md) so these items automatically appear in their payslip.

1. In the **Payroll** menu, select **Pay employees**.
2. If you haven’t already, [add a pay run](/s/article/Process-a-pay-run-and-pay-employees?userregion=true).
3. In the draft pay run, for each employee requiring mileage to be processed, click the employee.
4. Click **Add Earnings Line**, select the relevant allowance pay item such as ‘Mileage (non-taxable)', then click **OK**.
5. Enter the number of kilometres as the quantity.
6. Repeat the two steps above to add the taxable allowance line.
7. Click **Add Deduction Line**, select the deduction created previously, then click **OK**.
8. Enter the amount paid through expenses.
9. Click **Save**.

Once you’ve made the relevant updates, [post the pay run](/s/article/Process-a-pay-run-and-pay-employees?userregion=true).

## What's next?

[Send payslips](Send-payslips-to-employees.md) to your employees.