# Actuals and estimates in Practice Manager

Source: https://central.xero.com/s/article/Actuals-estimates-in-Practice-Manager

---

## Overview

- Learn how actuals and estimates are recorded in Practice Manager.
- See how invoicing affects work in progress (WIP) for actuals and estimates.

How it works

In Practice Manager, you can record information as:

- **Actuals** – what you've completed for the job
- **Estimates** – what you think the job will require

To [view all your WIP](Work-in-progress.md) in one place, in the **Business** menu, select **Work in Progress**.

Invoicing works differently for actual and estimated tasks, costs and interims.

On most invoices, you can select either quoted/estimated or actual time and costs. Once you’ve done this. you can add, select or clear tasks and costs, and edit time sheets.

How invoicing affects WIP for actuals

### Actuals

Actual costs, time and interims are recorded on jobs as WIP, ie what work you've completed for the job. You can select which actuals to include on an invoice. When actuals are invoiced, they’re no longer considered WIP.

### Invoices based on actuals

- Add or select a task or cost to invoice it and remove it from the WIP list.
- If you remove a selected interim, task or cost from a progress invoice based on actuals, or mark time as **Future**, it’s carried forward for future invoicing.
- When you create a progress or deposit invoice based on actuals, the resulting interim is recorded as WIP credit.
- On a final invoice, remove a selected task or cost to write it off.

When you draft an invoice for actual time and costs for a single job, the **Invoice Summary** displays below it.

- **WIP** column – the total amount of time and costs charged against the job, including anything after the invoice cut-off date.
- **Write-ons** column – the total adjustments to time or costs. A positive value is a write-on and a negative value is a write-off.
- **Carry Forward** column – the total amount of time and costs that will be carried forward to the next invoice.
- **Interims** row – the value of any interim payments. These are payments that have already been made for the job.

### Effects on the WIP ledger

In a progress or final invoice for actual time and costs, you can select and remove tasks and costs, and edit time sheets. All these actions have an effect on the WIP ledger:

| | | |
| --- | --- | --- |
| **Action performed in the invoice** | **Effect on progress actual invoice** | **Effect on final actual invoice** |
| Select a billable task | Removed from WIP ledger | - |
| Remove a billable task | WIP carried forward | - |
| Select a non-billable task | Removed from WIP ledger | - |
| Remove a non-billable task | Remains in WIP ledger | Removed from WIP ledger |
| Select a billable cost | Removed from WIP ledger | - |
| Remove a billable cost | WIP carried forward | - |
| Select a non-billable cost | WIP written on | - |
| Remove a non-billable cost | Remains in WIP ledger | Removed from WIP ledger |
| Part bill a cost (reduce quantity) | Unbilled portion carried forward | Outstanding balance written off |
| Increase quantity of a cost | WIP written on | - |
| Mark time as Future | WIP carried forward | - |
| Mark billable time as No | WIP written off | - |
| Edit billable time marked Yes (increase hours) | WIP written on | - |
| Edit billable time marked Yes (reduce hours) | WIP written off | - |
| Mark non-billable time as Yes | WIP written on | - |
| Remove an interim | WIP carried forward | - |
| Add a task to the invoice | WIP written on | - |
| Add a cost to the invoice | WIP written on | - |

How invoicing affects WIP for estimates

### Estimates

Estimated (also called quoted) costs and time, ie what will be done, doesn’t count towards WIP. The value of uninvoiced tasks and costs on accepted quotes is recorded in the **Est Billings** column of the WIP list instead.

If the job is:

- Based on a quote – the chargeable amount for each task and cost is calculated from the estimated times and costs shown in the quote
- Not based on a quote – the chargeable amounts are calculated from the estimated times and costs in the job itself

### Invoices based on estimates

A progress invoice based on a quote or estimate doesn’t create any write-offs because it’s not recorded as WIP.

To add WIP to an invoice, you can:

- Record time against quoted tasks
- Add additional tasks and record time against them
- Add costs marked as actuals

When the final estimated invoice is created, all WIP is removed from the WIP ledger, except deselected interims (percentage or deposit invoices).

The write-on is calculated as follows:

- All costs are absorbed by the invoice amount
- Any balance is allocated pro-rata to the timesheet entries in the job, which allocates write-ons or write-offs to staff according to the time they recorded on the job

### Effects on the WIP ledger

In a progress or final estimated invoice, you can select and remove tasks and costs, and edit time sheets. All these actions have an effect on the WIP ledger:

| | | |
| --- | --- | --- |
| **Action performed in the invoice** | **Effect on progress estimated invoice** | **Effect on final estimated invoice** |
| Remove an estimated task | Remains in WIP ledger | Removed from WIP ledger |
| Select an estimated task | Remains in WIP ledger | Removed from WIP ledger |
| Billable task added to the job (can’t be selected, but time is added to WIP ledger) | Remains in WIP ledger | Removed from WIP ledger |
| Non-billable task added to the job (can’t be selected, but time is added to WIP ledger) | Remains in WIP ledger | Removed from WIP ledger |
| Select a billable cost (cost added to the job) | Removed from WIP ledger | Removed from WIP ledger |
| Remove a billable cost (cost added to the job) | Remains in WIP ledger | Removed from WIP ledger |
| Select a non-billable cost (cost added to the job) | Removed from WIP ledger | Removed from WIP ledger |
| Remove a non-billable cost (cost added to the job) | Remains in WIP ledger | Removed from WIP ledger |
| Part bill a cost (reduce quantity) | Unbilled portion carried forward | Removed from WIP ledger |
| Increase the quantity of a cost | Removed from WIP ledger | Removed from WIP ledger |
| Remove an interim | WIP carried forward | WIP carried forward |
| Add a task to the invoice | WIP is applied to the existing WIP entries | WIP is applied to the existing WIP entries |
| Add a cost to the invoice | WIP is applied to the existing WIP entries | WIP is applied to the existing WIP entries |

## What's next?

[Run reports](Run-reports-in-Practice-Manager.md) to filter your practice's data. For example:

- See WIP changes for a selected date range with the WIP Control report
- View the WIP balance as it was at a selected point in time with the Job WIP Balances report