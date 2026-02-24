# Correct payment summary issues

Source: https://central.xero.com/s/article/Troubleshoot-published-payment-summary-issues

---

## Overview

- Unpublish PAYG payment summaries to identify and correct issues.
- Republish and resend PAYG payment summaries to employees.

**1** Unpublish payment summaries

Unlock your payroll data by unpublishing the payment summary that contains errors.

1. In the **Payroll** menu, select **Employees**.
2. Click **Payment Summaries**.

   If you've set up Single Touch Payroll, you can access previous years' payment summaries. Click **End of year reports**, select **Payment Summaries**, then click **View payment summaries**.
3. Enter your organisation's details, then click **Confirm and Continue**.
4. Select the checkbox next to the employee(s) whose details you need to correct, then click **Unpublish**.
5. ​Click **Unpublish** again to confirm.

**2** Identify and fix errors

### Deductions

If you make a change to a deduction category, Xero automatically applies the change to all payments unless the payment summaries have been published. Before making changes to the deduction category, you need to unpublish any related payment summaries.

### Allowances & gross wages

When the earnings type is set to **Allowance**, allowance amounts are automatically applied to the payment summary. You might find amounts included under Allowances should be included under Gross Wages (or vice versa).

Once you've identified the error being incorrectly reported:

- If the correction is to report an amount as an allowance, [create a new allowance earnings rate](Add-an-allowance-type-to-a-pay-item.md).
- If the correction is to report an amount as gross wages, select **Ordinary Time Earnings**.

You might want to rename the original earnings rate so you don't accidentally use this going forward. Don't change the earnings type of the original pay items. This will only change the reporting of the pay item from the next time the pay item is used. Previously posted pay runs won't change.

If you've added a new earnings rate:

- Run a [Transaction Listing Summary](Transaction-Listing-Summary-report.md) report for the employee to help identify total amounts to reverse.
- Reverse any amount to the earnings rate that you've processed incorrectly and re-enter them using the new earnings rate created.

### RESC

When the superannuation line contribution type is set to **Additional Employer Contribution (RESC)** or **Pre-Tax Voluntary Contribution (RESC)**, RESC amounts are automatically applied to the payment summary.

If you find that employee RESC amounts aren't being included in the RESC field, you might have processed superannuation contributions as a deduction rather than a superannuation line (RESC):

1. Run a [Transaction Listing Summary](Transaction-Listing-Summary-report.md) report for the employee to help identify total amounts to reverse.
2. Reverse any amount to the deduction rate that you've processed incorrectly and re-enter them using a super line. Make sure you select the contribution type **Pre-Tax Voluntary Contribution (RESC)**.

### Workplace giving or union fees

When the deduction category is set to **Workplace Giving** or **Union/Association Fees**, these amounts are automatically applied to the payment summary.

If you find that amounts for deductions such as workplace giving or union fees are missing, check the deduction pay items to make sure that the deduction category is applied correctly:

- **Other / None** isn't reported on the payment summary.
- **Workplace Giving** is reported on the payment summary **Workplace Giving** field.
- **Union Fees** is reported on the payment summary **Union** and **Association Fee****s** fields.

### RFBA or lump sum

Edit the values against each employee as required in the payment summary review screen.

Once the amounts are correct:

- If you're correcting payment summaries that aren't for the end of year payroll, republish the payment summaries.
- If you're correcting payment summaries for the end of year payroll, you can check the payment summary details.

**3** Republish payment summaries

Once you've corrected the mistakes, you need to republish the payment summaries.

1. In the **Payroll** menu, select **Employees**.
2. Click **Payment Summaries**.

   If you've set up Single Touch Payroll, you can access previous years' payment summaries. Click **End of year reports**, select **Payment Summaries**, then click **View payment summaries**.
3. Enter your organisation's details, then click **Confirm and Continue**.
4. Ensure that the checkboxes for the employees whose summaries have been corrected are selected, then click **Publish**.
5. Select **Yes** to produce an amended payment summary.
6. Click **Publish** to confirm.

The summaries will be updated in each employee's Xero Me.

**4** Resend payment summaries to employees

You can publish and resend a payment summary at any time during the year. All payment summaries must be published and distributed as part of the end of year payroll process.

1. From the **Payment Summaries** screen, select the checkbox next to the employees you want to resend summaries to.
2. Click **Send to Employee**.

If you can't select a customer, check that an email address has been [entered against an employee](/s/article/Add-an-employee-AU#1Addanemployeeandentertheirbasicinformation).

## What's next?

If you're still unable to submit your payment summary, contact Xero support below.