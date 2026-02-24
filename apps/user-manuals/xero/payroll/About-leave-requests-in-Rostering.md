# About leave requests in Rostering (BETA)

Source: https://central.xero.com/s/article/About-leave-requests-in-Rostering

---

## Overview

- Learn how leave requests and leave balances work in Rostering and advanced timesheets.
- View your employees' leave balances.

Tip

Rostering and advanced timesheets is currently in closed beta and is restricted to a small number of users.

## What you need to know

Warning

We recommend leave is requested in Rostering and advanced timesheets for employees using Rostering and advanced timesheets, with exceptions to salary pay rate employees, to avoid duplication in Xero payroll.

Leave balances and leave types are set up in Xero payroll and sync to Rostering and advanced timesheets. Before employees can add a leave request in Rostering and advanced timesheets, [set up their leave entitlements in Xero payroll](Set-up-an-employee-s-leave.md). Leave balances in Xero payroll sync to Rostering and advanced timesheets every 60 minutes.

Any current leave requests in Xero payroll won’t sync to Rostering and advanced timesheets as a leave request. You can either:

- Keep the leave requests in Xero payroll and [mark the employee as unavailable](Add-unavailability-for-a-shift.md) for those dates.
- [Reject the leave in Xero payroll](Approve-leave-as-a-Payroll-Admin.md) and add a new leave request in Rostering and advanced timesheets.

Employees can request leave using the Deputy mobile app. You can edit the [business settings in Rostering and advanced timesheets](Update-business-settings-for-Rostering.md) to allow employees to edit their approved leave requests and view their leave balances.

System administrators can [enter and approve leave on behalf of an employee](Add-a-leave-request-in-Rostering.md). Supervisors can enter leave on behalf of an employee and approve the date of leave but not the leave type.

[Family and domestic violence leave](Process-family-and-domestic-violence-leave.md) don't sync to Rostering and advanced timesheets. This leave type can only be requested in Xero payroll.

On the day the leave is taken, a leave timesheet will automatically be created for the employee. Leave request from Rostering and advanced timesheets will create an approved leave request in Xero when you [export the timesheet](Approve-or-unapprove-a-timesheet.md). A separate leave request is created in Xero for each day or partial day of leave taken in Rostering and advanced timesheets. For example, a leave request for five working days in Rostering and advanced timesheets will create five individual leave requests in Xero.

Timesheets don’t export to Xero payroll for employees with a salary pay rate. You can add leave requests for salaried employees in Rostering and advanced timesheets to help with scheduling, however their [leave requests need to be manually created](Submit-an-employee-s-leave-request.md) in Xero payroll.

System administrators and supervisors can view their employees' leave balances and upcoming leave requests. Leave balances in Rostering and advanced timesheets won’t show the employee’s correct leave balance until the timesheet for the pay period is exported to Xero.

## Leave balances fields explained

An employee’s leave balance shows the following information:

- **Leave type** – All leave entitlements for the employee based on their leave entitlements in Xero payroll.
- **Current balance**– The balance in Xero payroll based on the last updated date. Leave balances in Xero payroll sync to Rostering and advanced timesheets every 60 minutes.
- **Upcoming balance** – The employees' future leave request. This balance doesn’t include any leave taken on today’s date.
- **Future balance** – Total of **Current balance** less **Upcoming** balance.

Leave balances in Rostering and advanced timesheets and Xero payroll might not be up-to-date while the employee is taking leave. In Xero payroll, the current leave balance is the employee’s current balance less any approved leave requests. Leave requests in Rostering and advanced timesheets don't sync to Xero payroll until the timesheets are exported. This means the employee’s current balance and future balance can be overstated in Rostering and advanced timesheets and Xero payroll while the employee is on leave.

For example, an employee with a current leave balance in Xero payroll of 60 hours has an approved five days (40 hours) of annual leave for Monday to Friday in Rostering and advanced timesheets.

The employees leave balance in Rostering and advanced timesheets before the leave is taken on Monday:

- **Current balance** – 60h 0m (7.5d)
- **Upcoming** – 40h 0m (5d)
- **Future balance** – 20h 0m (2.5d)

The employees leave balance in Rostering and advanced timesheets on Wednesday:

- **Current balance** – 60h 0m (7.5d)
- **Upcoming** – 16h 0m (2d)
- **Future balance** – 44h 0m (5.5d)

The upcoming balance is 16 hours because the employee has two more days of leave after Wednesday. Rostering and advanced timesheets calculates future balance as current balance less upcoming leave. The employee’s future leave balance increases because the timesheet hasn’t yet been exported to Xero payroll. The employee’s current balance remains at 60 hours because this syncs from Xero payroll.

The employees leave balance in Rostering and advanced timesheets on the following Monday and the timesheet is exported to Xero:

- **Current balance** – 20h 0m (2.5d)
- **Upcoming** – 0h 0m (0d)
- **Future balance** – 20h 0m (2.5d)

The employee’s timesheet is exported to Xero creating the leave requests for five days in Xero. In Xero, the leave balance updates to 20 hours. The current balance in Rostering and advanced timesheets also updates once the leave balance syncs from Xero payroll which decreases the future balance and as a result shows the current up-to-date leave balance for the employee.

## View an employee’s leave balances and leave requests in Rostering and advanced timesheets

1. In the **Payroll** menu, select **Rostering and advanced timesheets**.
2. Select the **People** tab.
3. Select the employee you want their leave balances.
4. Select **Leave**.

## What's next?

[Enter leave on behalf of an employee](Add-a-leave-request-in-Rostering.md) or [approve leave](Approve-or-decline-a-leave-request.md) they’ve requested themselves.