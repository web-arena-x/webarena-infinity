# Approve or unapprove a timesheet in Rostering (BETA)

Source: https://central.xero.com/s/article/Approve-or-unapprove-a-timesheet

---

## Overview

- Approve a timesheet in Rostering and advanced timesheets to confirm shift details before you export the timesheet to payroll.
- Unapprove a timesheet to edit pay or time.
- Recalculate a timesheet to make sure an employee’s pay matches their pay rules.

Tip

Rostering and advanced timesheets is currently in closed beta and is restricted to a small number of users.

How it works

Approve timesheets in Rostering and advanced timesheets to confirm shift details before you export the timesheet to Xero payroll. You should always approve the oldest timesheets first to make sure overtime and shift loading calculations are accurate.

You can approve different timesheets depending on your access level:

- Supervisors can approve timesheets for users with employee access. Supervisors can only view the time component of the timesheet. Once they approve a timesheet, the pay component will be automatically approved.
- System administrators can approve timesheets for all users. System administrators can approve and edit both the time and pay components of a timesheet.

Approve a timesheet

To approve a timesheet:

1. In the **Payroll** menu, select **Rostering and advanced timesheets**.
2. Select the **Timesheets** tab.
3. Select the date range for the timesheet you want to approve.
4. Click the employee’s name, then select the **Pending** tab to view their pending timesheets.
5. Click the timesheet and review the details.
6. (Optional) In the **Enter comment** field, add a comment to the timesheet.
7. Click **Approve** to approve the timesheet or click **Approve and next** to be taken to the next timesheet.

If a shift was scheduled but the employee who was scheduled for the shift didn’t clock in or out, a timesheet will be created with an **Absent** status. You either need to enter the shift details and approve the timesheet, or discard the timesheet if the shift wasn’t worked.

To approve multiple timesheets:

1. In the **Payroll** menu, select **Rostering and advanced timesheets**.
2. Select the **Timesheets** tab.
3. Select the date range for the timesheets you want to approve.
4. Select the **Pending** tab.
5. Select the checkboxes next to the timesheets you want to approve, then click **Approve [number] with no issues**.

Only pending timesheets can be approved in bulk.

Unapprove a timesheet

1. In the **Payroll** menu, select **Rostering and advanced timesheets**.
2. Select the **Timesheets** tab.
3. Select the date range for the timesheet you want to unapprove.
4. Click the employee’s name, then select the **Approved** tab to view their approved timesheets.
5. Click the timesheet you want to unapprove, then click **Unapprove time** or **Unapprove pay**.

When you unapprove time, the timesheet reverts to a **Pending** status and you can edit the time, area and break fields.

When you unapprove pay, the timesheet reverts to a **Time approved** status and you can edit the pay details.

Recalculate an approved timesheet

### What you need to know

Recalculate a timesheet to make sure an employee’s pay still matches any pay rules that apply to them based on their assigned pay rate.

You might want to recalculate timesheets if you approve timesheets out of order. This might happen if you approve timesheets by area, an employee was on leave when they were scheduled or the hours need to be updated on an employee’s submitted timesheet. In these situations, the actual time worked by the employee is changed so Rostering and advanced timesheets needs to make sure employees are paid correctly according to their assigned pay rate and pay conditions.

The following recalculation options are available:

- **Off** – No recalculation of any timesheets will occur when approving timesheets.
- **Only from the selected timesheet and onwards (within the applicable range)** – When you approve a timesheet, any already approved timesheets that fall after this one (date or time wise) are automatically recalculated to ensure the correct pay.
- **All timesheets within the applicable range** – When you approve a timesheet, any of the selected employees' already approved timesheets before and after the currently selected timesheet are recalculated to ensure the correct pay. Note that using this option might increase the time it takes to approve timesheets.

### Set up timesheet recalculation

1. In the **Payroll** menu, select **Rostering and advanced timesheets**.
2. In the **Settings** menu, select **General settings**.
3. Select the **Timesheets** tab.
4. Under **Recalculate approved timesheets in chronological order**, select the relevant option.
5. Click **Apply Changes**.

## What's next?

Now that you’ve approved your timesheets, [export your timesheets to payroll](Export-a-timesheet-from-Rostering.md).