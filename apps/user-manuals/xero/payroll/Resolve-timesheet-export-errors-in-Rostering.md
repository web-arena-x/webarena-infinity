# Resolve timesheet export errors in Rostering (BETA)

Source: https://central.xero.com/s/article/Resolve-timesheet-export-errors-in-Rostering

---

## Overview

- Resolve errors when exporting timesheets from Rostering and advanced timesheets to Xero payroll.

Tip

Rostering and advanced timesheets is currently in closed beta and is restricted to a small number of users.

## Earnings pay item not allocated to expense account or allocated to invalid account

Your export will fail if an earnings pay item in Xero hasn’t been allocated to an expense account, or the expense account is invalid or archived. This includes inactive earnings pay items.

To resolve this error, ensure all earnings pay items are allocated to the correct expense account. If you haven’t used the pay item and aren’t going to use it in the future, [delete it instead](/s/article/Edit-inactivate-or-delete-a-pay-item-AU).

For an inactive pay item, you’ll need to [mark it as active](/s/article/Edit-inactivate-or-delete-a-pay-item-AU), allocate an expense account, then mark the pay item as inactive again.

## Allowance pay item doesn’t include allowance type

Your export will fail if an allowance pay item in Xero doesn’t include an allowance type.

To resolve this error, [add an allowance type to the pay item](Add-an-allowance-type-to-a-pay-item.md). If you haven’t used the pay item and aren’t going to use it in the future, [delete it instead](/s/article/Edit-inactivate-or-delete-a-pay-item-AU).

## Posted pay runs in payroll

Your export will fail if there is a posted pay run in Xero for the same date range as the timesheets you’re exporting.

To resolve this error, [revert the pay run to draft](Revert-a-pay-run-to-draft.md) in Xero payroll before you export the timesheets from Rostering and advanced timesheets.

## Timesheet created in Xero Me

Your export will fail if a timesheet has been created in Xero Me for the same employee and pay period as the timesheet you’re exporting from Rostering and advanced timesheets.

Employees shouldn’t use Xero Me or Xero timesheets to create timesheets if they use Rostering and advanced timesheets.

## Other reasons timesheet exports fail

- An employee’s mobile number doesn’t match between Rostering and advanced timesheets and Xero payroll. Check the employee’s mobile number and update the mobile number in Xero to match, then export the timesheet again.
- If the pay period has already been processed and the timesheets have already been exported to Xero payroll.
- You can’t export timesheets for an employee if the employee’s pay rate is set to Salary in Rostering and advanced timesheets.

## What's next?

If you receive an error that's not listed here or you’re still having trouble, contact Xero support below.