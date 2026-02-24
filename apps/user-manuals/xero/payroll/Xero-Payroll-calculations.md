# Xero Payroll calculations

Source: https://central.xero.com/s/article/Xero-Payroll-calculations

---

## Overview

- Find out how Xero payroll calculates various aspects of employees’ pay and leave in Australia.

What you need to know

Australian employers have an obligation to keep records of various employee and payroll information for seven years. These records are required to be readily available to a Fair Work Inspector, be in a legible form and in English. Finding out more about how Xero payroll calculates various aspects of payroll and leave can help employers with record-keeping obligations.

You can find information about record-keeping obligations on the [Fair Work Australia](https://www.fairwork.gov.au/pay-and-wages/paying-wages/record-keeping) website. If you need advice on payroll calculations or record-keeping obligations, we recommend seeking this advice from your accountant or financial advisor.

Payroll days per year (364/365 days)

### How payroll year settings work

Organisations that joined Xero after 15 September 2014 have a default payroll year setting of 364 days (52 weeks). Prior to this change, organisations could choose either a 364 or 365 day payroll year setting. If the 365-day option was selected, these organisations weren't automatically changed to 364 days.

The ability to view and adjust the payroll year settings was removed after September 2014 to avoid unnecessary confusion. This is also consistent with other accounting software providers who have moved to a 364 day calendar.

For employees on an annualised salary, the payroll year for an organisation will cause minor differences in some calculations in Payroll, such as hourly rates, annual salaries and leave accruals. It is ultimately a business decision which payroll year an organisation chooses to use.

If your preferred calendar needs to be updated at any time, you'll need to contact Xero support.

### Payroll calculations

Xero payroll uses the following calculations in a pay run, based on the payroll year and pay period.

If employees are paid weekly:

- 365 days per year divided by 7 days per week = 52.142857 weeks in a year
- 364 days per year divided by 7 days per week = 52 weeks in a year

If employees are paid fortnightly:

- 365 days per year divided by 14 days per fortnight = 26.0714 fortnights in a year
- 364 days per year divided by 14 days per fortnight = 26 fortnights in a year

If employees are paid monthly, the same calculation is used on both the 364 and 365 day payroll year setting for employees on annualised salaries who are paid on a monthly basis. Xero payroll currently calculates their hours each month based on the number of business days in that month and the number of hours worked per week. The gross amount stays the same each month, based on the salary entered in the pay template, however the number of hours and hourly rate changes each month to achieve the gross amount.

For example, Alex is paid an annual salary of $90,000 and works 38 hours a week.

If Alex was on a weekly frequency, the calculation would be:

- $90,000 divided by 52.142857 weeks (365 days) = $1,726.03 gross pay per week
- $90,000 divided by 52 weeks (364 days) = $1,730.77 gross per week

If Alex was was on a fortnightly frequency, the calculation would be:

- $90,000 divided by 26.0714 fortnights (365 days) = $3,452.06 gross pay per week
- $90,000 divided by 26 fortnights (364 days) = $3,461.54 gross pay per week

If Alex was on a monthly frequency, using July 2022 as an example, the calculation would be:

- $90,000 divided by 12 months (the same for both 364 and 365) = $7,500 gross pay per month. As July has 21 business days, the hours and hourly rate would be:
 - 7.6 hours x 21 days = 159.60 hours for July 2022
 - $7,500 gross pay divided by 159.60 hours = $46.992481 gross pay per hour

If you aren’t sure which payroll year setting is best for your organisation, please reach out to an accountant or advisor.

When you complete [year-end reconciliation](Finalise-Single-Touch-Payroll-data.md), you can check if the total figures add up to what you‘re expecting and are in line with your employer obligations.

You can review year-end payroll details when you [prepare payroll for year-end](Payroll-year-end.md).

Superannuation calculations

As of 1 July 2022, statutory superannuation is calculated at 10.5% of an employee's ordinary time earnings each pay period, which is in line with legislation. Superannuation won’t be calculated when you create a pay item and select the **Exempt from Superannuation Guarantee** checkbox.

Note that Statutory Superannuation is an additional 10.5% amount on top of the employee’s base earnings, which is to be paid by the employer.

If an employee’s superannuation needs to be calculated at a different percentage, [Payroll can be edited](Updates-to-superannuation-guarantee-contributions.md) to reflect this amount.

PAYG calculations

To calculate the PAYG withholding for an employee, Xero payroll uses the current ATO tax tables, the employee's **Taxes** tab, the payroll calendar the employee is linked to (ie monthly, fortnightly, or weekly), and the pay items used. When reviewed:

- If an employee’s tax is calculated lower than expected, the pay item might have **Exempt from PAYG Withholding** selected in the pay item’s settings. You can [edit a pay item](/s/article/Edit-inactivate-or-delete-a-pay-item-AU) if you need to update it.
- If tax is calculated higher than expected, it's possible this is a pay period that has already been processed for this employee. This means tax is being calculated on the entire gross earnings for the pay period.

If you need to adjust the total tax being withheld in the pay run if required, you can [manually adjust tax](/s/article/Manually-adjust-tax-for-an-employee-s-pay-AU) for an employee's pay.

Leave requests calculations

Xero payroll calculates hours in a leave request based on the **Hours in a Pay Period** value entered in the employee's leave types. When calculating **Hours in a Pay Period**, Payroll considers all leave types that have been assigned to an employee, then selects the lowest number of hours listed for a full pay period.

If an employee's leave is based on ordinary earnings, the hours in a leave request are calculated by the number of hours in a full pay period, divided by the number of business days in the pay period.

For example, 40 hours per week divided by 5 working days = 8 hours per day.

The number of business days in a monthly pay period varies from month to month, which affects the hours calculated in a leave request.

If you need to, you can edit the hours in the [leave request](Approve-leave-as-a-Payroll-Admin.md) by clicking into the request and editing the **Hours** field.

Bonus & commission calculations

Xero calculates PAYG withholding on [bonus and commission](Add-bonuses-and-commissions-or-lump-sum-E-pay-items.md#HowXerocalculatestaxusingMethodBiiofSchedule5) payments based on ATO’s Schedule 5 tax table, and more specifically, [Method B(ii)](https://www.ato.gov.au/rates/schedule-5---tax-table-for-back-payments,-commissions,-bonuses-and-similar-payments/) (ATO website).

If you’d like to calculate bonus and commission PAYG based on a method that isn't B(ii), this needs to be manually calculated and a [manual tax adjustment](/s/article/Manually-adjust-tax-for-an-employee-s-pay-AU) can be added in the employee’s draft payslip.

Award calculations

At this stage, Xero payroll doesn’t have the functionality to enter industry awards for calculations. This is because payroll and award interpretation might be different for each business and each employee.

If awards need to be taken into consideration, you can [set up custom pay items](Add-a-custom-pay-item.md) to support these awards.

## What's next?

Now you’ve learned how payroll works in Xero, you can get started [paying employees](/s/article/Process-a-pay-run-and-pay-employees).