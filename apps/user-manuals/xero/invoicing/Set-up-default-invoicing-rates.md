# Use default invoicing rates

Source: https://central.xero.com/s/article/Set-up-default-invoicing-rates

---

## Overview

- Set default invoicing rates for staff members or tasks.
- Use the staff billable rate or task billable rate to calculate costs at the quoting and job stages.

How it works

- Default invoicing rates are made up of the [staff base and billable rates and the task base and billable rates](Choose-how-to-bill-your-clients.md).
- Default invoicing rates are used for all invoicing and reporting unless you override these rates with [historic](Lock-staff-and-task-billable-rates.md) or [custom](Set-up-custom-billing-rates.md) invoicing rates.

Set a staff rate

### Base rate

When you [add a staff member](/s/article/Add-staff?userregion=true) to Practice Manager, you need to add their base rate. This is the hourly amount your business pays for a staff member’s time. This rate is used to calculate the actual cost to your business and it affects all profit calculations.

To calculate the base rate, add annual leave allowances, sick leave, public holidays, bonuses, accident levies, superannuation, and any other relevant costs to their basic hourly rate. The more accurate this rate, the more accurate your profitability reporting.

### Billable rate

When you add a staff member to Practice Manager, you need to add their billable rate. This is the rate you use to invoice your client for this staff member’s time, regardless of what task this staff member performs.

Set a task rate

### Base rate

When you [create a task](Set-up-your-tasks.md), you need to give it a base rate. This rate is only used at the quoting stage when no staff members have been assigned to tasks. The base rate is the best estimate of the actual cost of the task to you.

If only one person records time against a task, the task base rate will be the same as that person's staff base rate. However, if several staff members record time against the task and you haven’t yet assigned staff to the task, the best estimate of the actual cost will be the average of the staff base rates for those staff members.

### Billable rate

When you create a task, you need to give it a billable rate. This is the hourly rate you use to invoice your client for the task, regardless of which staff member does the work.

Quote & invoice using the staff billable rate

When you [create a quote](Create-a-quote-in-Practice-Manager.md) using the staff billable rate, the estimated cost of a task on the quote is either:

- Estimated Time \* [task] Base Rate (no staff allocated to the task)
- Estimated Time \* [staff] Base Rate of allocated staff (if staff have been allocated to the task)

The quoted amount for the task will be either:

- Estimated Time \* [task] Billable Rate (no staff allocated to the task)
- Estimated Time \* [staff] Billable Rate of allocated staff (if staff have been specifically allocated to the task)

To override the quoted amount, change the quote's **Pricing Mode** from **Calculated Price** to **Fixed Price**.

At the job stage:

- The actual cost of performing the job will always be the Actual Time \* [staff] Base Rate of the staff member writing the time sheet
- The calculated invoiced amount will always be the Actual Time \* [staff] Billable Rate
- The amount actually invoiced to your client will be determined by whether you’re invoicing based on a quoted amount, or on actual billable time and actual billable costs

To override the calculated invoiced amount, change the job's **Pricing Mode** from **Calculated Price** to **Fixed Price**.

Quote & invoice using the task billable rate

When you create a quote using the task billable rate, the estimated cost of a task on the quote will always be the Estimated Time \* [task] Base Rate (as staff can't be specifically allocated to tasks at the quote stage if you select **Task Billable Rate**).

The quoted amount for a task will be the Estimated Time \* [task] Billable Rate.

To override the calculated quoted amount, change the quote's **Pricing Mode** from **Calculated Price** to **Fixed Price**.

At the job stage:

- The actual cost of performing the job will always be the Actual Time \* [staff] Base Rate of the staff member writing the time sheet to the task
- The calculated invoiced amount will always be the Actual Time \* [task] Billable Rate
- The invoice amount is determined by whether you’re invoicing based on a quoted amount, or on actual invoiced time and costs

To override the calculated invoiced amount, change the job's **Pricing Mode** from **Calculated Price** to **Fixed Price**.

## What's next?

To override default invoicing rates, you can [set up custom invoicing rates](Set-up-custom-billing-rates.md).