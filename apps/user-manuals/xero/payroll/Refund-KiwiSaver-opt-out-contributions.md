# Refund KiwiSaver contributions

Source: https://central.xero.com/s/article/Refund-KiwiSaver-opt-out-contributions

---

## Overview

- How you process refunds depends on whether the contributions have been paid to Inland Revenue (IR) or not.
- Change an employee’s contribution option when they opt out of KiwiSaver.
- Refund employee’s contribution if they opt out of Kiwisaver.

What you need to know

Once you’ve automatically enrolled a new employee in KiwiSaver, they can opt out after 14 days and before 56 days of starting employment. They’ll need to provide a KS10 with their IR330 and KS2.

The option to opt out expires after eight weeks, unless there are exceptional circumstances. For more information about late opt out requests, please see [IR’s website](https://www.ird.govt.nz/kiwisaver/kiwisaver-employers/employees-who-want-to-opt-out-of-kiwisaver/employees-who-opt-out-late-from-kiwisaver).

When an employee opts out, process refunds through Xero for:

- Employee and employer KiwiSaver contributions made and not yet paid to IR
- Employer contributions already paid to IR

You can get further information about [employees who opt out of KiwiSaver](https://www.ird.govt.nz/kiwisaver/kiwisaver-employers/employees-who-want-to-opt-out-of-kiwisaver) on the IR website.

Process refunds where taxes aren't filed

Run the [Pay History report](Pay-History-report.md), or view previous pay summaries to calculate the:

- Total of employee KiwiSaver deductions not yet paid to IR
- Total of employer KiwiSaver contributions (before ESCT) not yet paid to IR
- Total of ESCT not yet paid to IR

To reverse contributions not yet paid to IR and refund employee deductions:

1. Create an [unscheduled pay run](Adjust-previous-payroll-payments.md) for the most recent pay period.
2. Select the employee, then change the earnings amounts to 0.
3. Under **Statutory Deductions**, add a **KiwiSaver Manual Adjustment** for the employee KiwiSaver deductions as a negative amount.
4. Under **Superannuation**, add a **KiwiSaver Manual Adjustment** for the employer contributions total as a negative amount.
5. Check the **ESCT amount** matches the expected **ESCT total**:
   - The net pay should be positive and equal to the employee KiwiSaver deduction amount
   - The **Net Superannuation amount** should be negative
6. Click **Save & Close**.
7. Click **Post**, then click **Post and file**.
8. Pay the employee the net pay amount.
9. If there have been no employer contributions paid to IR, change the employee’s **Contribution option** to **Opt out** and add an **Opt out date**.

Payday filings don’t send negative amounts. You need to log in to myIR and edit the filings for each of the Payday files with the amounts not yet paid to IR. Now enter 0 for:

- Employee KiwiSaver deduction amounts
- Net Employer KiwiSaver contribution amounts
- ESCT amounts

Process refunds where taxes are filed

Run the [Pay History report](Pay-History-report.md), or view previous pay summaries to calculate the:

- Total of employer KiwiSaver contributions (before ESCT) already paid to IR
- Total of ESCT already paid to IR

To reverse employer contributions already paid to IR:

1. Create an [unscheduled pay run](Adjust-previous-payroll-payments.md) for the last period of the month.
2. Select the employee, then change the earnings amount to 0.
3. Under **Superannuation**, add a **KiwiSaver Manual Adjustment** as a negative amount.
4. Check that the **ESCT amount** matches the expected **ESCT total**:
   - The net pay should be zero
   - There is a negative **Net Superannuation amount**
5. Click **Save & Close**.
6. Click **Post**, then click **Post and file**
7. In the employee's record under **Taxes**,change the **Contribution option** for KiwiSaver to **Opt out** and add an **Opt out date**.

Payday filings don’t send negative amounts so you need to log in to myIR, and edit the filings for each of the pays made to IR. This is to zero out the employer KiwiSaver amounts and the ESCT amounts. Once they've received notification of the opt out IR will:

- Refund the employee deductions directly to the employee, so there’s no need to reverse these in payroll, or in myIR filings.
- Refund the net superannuation
- Refund the ESCT as a credit to the employer’s payroll account in myIR. You’ll need to call IR to request the overpaid ESCT to be refunded or transferred to other periods or tax types.

## What's next?

Understand more about [KiwiSaver status and contribution options](Understand-KiwiSaver-status-and-contribution-options.md).