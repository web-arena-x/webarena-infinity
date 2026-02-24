# Delete an employee or end their employment

Source: https://central.xero.com/s/article/Delete-an-employee-and-end-their-employment

---

## Overview

- Delete an employee record if they haven't been paid yet.
- End an employee's employment.

What you need to know

Xero payroll calculates final pay using information in the employee’s profile based on the [Holidays Act 2003](http://legislation.govt.nz/act/public/2003/0129/latest/DLM236387.html) (New Zealand Legislation website).

When calculating leave and final pay there are many complexities, especially for employees with irregular hours or changing work patterns. It’s important for employers to understand and comply with their obligations under the Holidays Act 2003 including those related to correctly calculating permanent employee leave entitlements and payments for annual holidays.

It is your obligation to ensure you comply with the Holidays Act 2003. Talk to your accountant or bookkeeper or [contact MBIE](https://www.mbie.govt.nz/about/contact-us/) for further guidance about how to comply with the Holidays Act 2003. For more information about leave entitlements and calculations see [Employment NZ's website](https://www.employment.govt.nz/pay-and-hours/pay-and-wages/final-pay).

If there's a payroll transaction on the employee’s record, you'll need to end their employment before you start the steps.

An employee's annual leave entitlements automatically flow through to their final payslip and might not reflect the balance in their leave record or the **Leave Balances report**.

For organisations created before 5 August 2024, if you've selected **Include leave available to take in advance in the balance**, [clear the checkbox](Include-annual-leave-in-advance-in-leave-balance.md) so that the balance shown is the true balance.

For organisations created after 5 August 2024, if you’ve selected **Show leave available in advance**, clear the checkbox so that the balance shown is the true balance.

Delete an employee record

You can only delete an employee if there are no payroll related transactions for the employee in Xero. If the employee has been included in a pay run, you need to terminate the employee.

To delete an employee:

1. In the **Payroll** menu, select **Employees**.
2. Click the employee's name to open their details.
3. Next to the employee's initials, select the menu icon , then select **End employment.**
4. Click **End employment****.**

End an employment with a final pay

When an employee has outstanding leave balances or other earnings to be paid, you can end their employment in a final pay.

According to the legislation, if an employee has unused annual leave when their employment ends, they might also be entitled to payment for any public holidays that occur during that leave period. If a public holiday falls within this period and on a day the employee would normally have worked, the employee must be compensated for that day. This is why public holidays might be included in the final pay. For more information about leave and holiday payments in a final pay, visit [Employment NZ's website](https://www.employment.govt.nz/pay-and-hours/pay-and-wages/final-pay).

Any sick leave an employee might have accrued over the time of their employment isn’t paid out on their last day unless the employer and employee have an agreement.

If an employee’s [leave in advance is set in Xero](Include-annual-leave-in-advance-in-leave-balance.md):

- Their available leave in advance isn’t paid out. It’s a time equivalent estimate of any **Holiday pay** that has accrued since the last anniversary.
- **Holiday pay** is paid out instead of the available leave in advance.
- **Holiday pay** owing should be at least eight percent of their gross earnings since their last anniversary date.

### Step 1. Run and review the Leave Balances report

Before you process their final pay, review the employee's leave balances by running the [Leave Balances report](Leave-Balances-report.md).

You can manually correct leave balances in an [unscheduled pay run](Adjust-previous-payroll-payments.md) before processing the final pay to:

- Move leave from one leave type to another
- Add a positive or negative accrual in the leave section of a payslip

### Step 2. Create leave requests

If the employee has any outstanding leave for leave types other than **Annual Leave** and **Alternative Holidays**, such as long service leave (LSL), create leave requests before processing the employee’s final pay.

1. In the **Payroll** menu, select **Employees**.
2. Click the employee's name to open their details
3. Select **Leave.**
4. Click **New leave request**, then select the leave type.
5. Select a start and end date which falls within the pay period for the pay run.

   For example, if an employee is paid fortnightly with one week LSL, and leaves on the last day of the fortnight, the end date is the last day of the pay period.
6. Under **Leave to be paid**, enter the leave balance in hours you’re paying out, including any hours the employee will accrue for the current pay period.
7. Click **Approve**.

### Step 3. Process the employee's final pay in a pay run

You can process the employee's final payment in your next normal pay run, or in a separate unscheduled pay run after their last normal pay run was posted.

1. In the **Payroll** menu, select **Pay employees**.
2. Process or delete any draft pay runs for the pay frequency.
3. Under **New Pay Run**, select the relevant pay run period, then click **Process Pay Run**.
4. Click the employee’s name.
5. Click **Set As Final Pay**.
6. Select the last day of their employment date, then click **OK**. The date must be prior to the pay period end date.

### Step 4. Review negative annual leave in a final pay

If an employee has a negative annual leave balance in their final pay, it’s because they’ve taken more leave than they were entitled to at the time of their last day of employment.

You can run the [Leave Transactions report](https://central.xero.com/s/article/Leave-Transactions-report?userregion=true) to review the value of the leave taken in advance.

When you set an employee’s payslip as their final pay, the negative annual leave balance flows through into their final payslip. The rate is calculated by taking the total value of the leave paid in advance, divided by the total number of hours taken in advance.

For example, an employee has an annual leave opening balance of 25 hours and takes 32 hours leave. Their balance is -7 or seven hours taken in advance. The 32 hours of annual leave were paid out at $25.00 p/h. The seven hours of annual leave at $25 per hour totaling $175 taken in advance would be deducted from their final pay.

### Step 5. Amend employee's payslip and post pay run

In the final pay run, add any additional hours worked. If necessary **Edit tax settings** to correctly tax any lump sum amounts in the employee's payslip.

1. Next to **Earnings**, click **Add** to enter any additional hours worked or other earnings still to be paid.
2. Under **Employee Taxes**, click **Edit tax settings** to specify how much of the pay is a lump sum and specify the appropriate lump sum tax rate.
3. Under **Leave Accruals**, ensure the following leave balances are zero:
   - **Annual Leave**
   - **Alternative Holidays**
4. Click **Save & Close**.
5. Review all other employees included in the pay run and make any other changes as needed.
6. Once the pay run is correct, if you're:
   - Not connected to myIR for Payday filing – click **Post**, then click **Post** again to confirm your pay run.
   - [Connected to myIR for Payday filing](Set-up-or-reconnect-your-myIR-connection-for-Payday-filing.md) – click **Post** **and** **file**, then click **Post** **and** **File** again to post the pay run and submit the payday file to IR
7. Once the pay run is correct, click **Post**, then **Post and File**.

End an employment with no final pay

If an employee’s holiday pay and leave balances are zero and they’re owed no further earnings you can end their employment without doing a final pay. This method is useful for casuals and contractors.

1. In the **Payroll** menu, select **Employees**.
2. Click the employee’s name to open their details.
3. Next to the employee’s initials, click the menu icon , then select **End Employment**.
4. Select their last day, then click **End Employment**.

## What's next?

You're all done.