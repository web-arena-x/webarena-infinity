# Set up pension contribution refunds

Source: https://central.xero.com/s/article/Set-up-pension-contribution-refunds

---

## Overview

- If an employee opts out of your pension scheme, refund any existing pension contributions.
- Set up pay items and assign them to an employee's pay template to process pension refunds.

How it works

### Opt out option and refunds

During the opt out period, an employee can opt out of your pension scheme directly with your pension provider. After you [remove the employee from your scheme](Opt-in-or-opt-out-of-a-pension-scheme.md), you need to refund any existing pension contributions.

To refund any existing contributions, you need to add two pay items, a deduction and an employer pension, then update the employee's pay template.

Refund pay items need to match the pension type the contributions were originally processed as. For example, if the pension scheme is set up as Pre-Tax Pension (NPA), the refund pay item also needs to be set up as Pre-Tax Pension (NPA).

### Negative year-to-date pension values

The current Real Time Information (RTI) submission to HMRC doesn't allow negative year-to-date (YTD) pension values. For example, if you think you'll have employees to enrol in March and expect to have refunds to process in April, Xero sends a negative pension value for the period, and a nil pension for YTD.

If this is the case, HMRC will expect you to use an [Earlier Year Update (EYU)](/s/article/Adjust-previous-payroll-payments-UK) submission to amend the previous tax year pension YTD value. This is applicable for tax years prior to 2020/21. To correct past and current year corrections from and including tax year 2020/21, create an unscheduled pay run.

To work around this, you can use the postponement feature in Xero to push your assessments into the following tax year.

Create pension refund pay items

### Set up a deduction pay item

1. In the **Payroll** menu, select **Payroll settings**.
2. Select the **Pay Items** tab, then select **Deductions**.
3. Click **Add**, then select the category that matches your pension arrangement, either **Pre-Tax Pension (NPA)**, **Post-Tax Pension (RAS)**, or **Salary Sacrifice**.
4. Enter a name for the pay item. We recommend you use an easy to identify name, such as [Pension provider name] refund.
5. Under **Calculation Type**, click **Fixed Amount**, then under **Standard Amount** enter 0.00.
6. Under **Liability Account**, select the same liability account as set out in the **Workplace Pension** tab.
7. (Optional) If you're setting up a **Post-Tax Pension (RAS)**deduction pay item, select the **Reduce By PAYE Basic Rate** checkbox to reduce employee contributions by the PAYE basic rate.
8. Click **Add**.

### Set up an employer pensions pay item

1. In the **Payroll** menu, select **Payroll settings**.
2. Select the **Pay Items** tab, then select **Employer Pensions**.
3. Click **Add**, then select **Pension**.
4. Enter a name for the pension. This name appears on employee payslips.
5. Under **Calculation Type**, click **Fixed Amount**, then under **Standard Amount** enter 0.00.
6. Under **Liability Account**, select the account to code the pension liability to.
7. Under **Expense Account**, select the account to code the pension expense to.
8. (Optional) Select the **Show Balance to Employee** checkbox to include the balance on employee payslips.
9. Click **Add**.

Assign the pay items to an employee's pay template

Once the refund pay items are set up, you can then add them to the employee's pay template:

1. In the **Payroll** menu, select **Employees**.
2. Click an employee's name to open their details, then select **Pay template**.
3. Under **Deductions**, click **Deduction**, then select the new pay item you set up for the deduction.
4. Select **Fixed Amount**, then enter 0.00.
5. Under **Employer pensions**, click **Pension**, select the new pay item you set up for the employer pension, then enter 0.00.
6. (Optional) Add a **Company Max** to the employer pension pay item.
7. Click **Save**.

If the employee is included in a draft pay run, you need to reset the employee's payslip for the changes to be included. To do this:

1. In the **Payroll** menu, select **Pay employees**.
2. Under **Pay period**, select the draft pay run.
3. Click the employee's name.
4. Click **Reset Payslip**, then click **Yes**.
5. Enter negative values to refund contributions using the newly created pay items.
6. Click **Save**.

## What's next?

[Process a pay run](/s/article/Process-a-pay-run-and-pay-employees-UK) to pay your employee a pension contribution refund.