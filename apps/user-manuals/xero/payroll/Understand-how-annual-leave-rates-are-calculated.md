# How annual leave rates are calculated

Source: https://central.xero.com/s/article/Understand-how-annual-leave-rates-are-calculated

---

## Overview

- Understand how Xero calculates annual leave rates.
- Learn how you can manually calculate annual leave rates.

What you need to know

It’s important for employers to understand and comply with their obligations under the [Holidays Act 2003](http://legislation.govt.nz/act/public/2003/0129/latest/DLM236387.html) (New Zealand Legislation website) including those related to correctly calculating employee leave entitlements and payments for annual holidays.

For this calculation to be accurate, you need to ensure that what represents a working week for your employees is clear. This needs [to be entered into Xero](Change-an-employee-s-salary-and-wages-details.md) and kept up to date so when it’s used by Xero, you’re confident rates of pay are correct.

Talk to your accountant or bookkeeper or [contact the Ministry of Business, Innovation and Employment (MBIE)](https://www.mbie.govt.nz/about/contact-us/) for further guidance about how to comply with the Holidays Act 2003. See [Employment NZ's website](https://www.employment.govt.nz/pay-and-hours/pay-and-wages/leave-and-holiday-pay) for more information about leave entitlements and calculations.

How Xero calculates annual leave rates

### How it works

When an employee takes annual leave, their employer must pay them the greater amount of:

- The employee's ordinary weekly pay (OWP) at the time the leave is taken
- Their average weekly earnings (AWE) for the 12 months prior to the pay period in which the leave is taken

This means Xero calculates the annual leave rate based on the period in which the leave is taken, not on the period in which it's paid.

To view the rate for an employee within a pay run:

1. In the **Payroll** menu, select **Pay employees.**
2. Select a draft pay run and click on your employee’s name.
3. Click **Review** next to their annual leave line on their payslip.

### About ordinary weekly pay (OWP)

The amount an employee receives under their employment agreement for an ordinary working week includes:

- Regular allowances, such as a shift allowance
- Regular productivity or incentive-based payments, including commission or piece rates
- Cash value of board or lodgings
- Regular overtime

Xero calculates the OWP using the employee’s current salary and wages plus any other regular earnings from their pay template. This total is divided by the number of weeks in the pay period. The hourly rate is then calculated by dividing the OWP by the employee's hours per week (hours per day x days per week).

For example, if your employee’s hourly rate is $37.50, they have a car allowance of $100 a week and they work for 5 hours a day, 4 days a week on a fortnightly pay frequency. The OWP is calculated by:

1. Pay period earnings: $1,500 + $100 = $1,600
2. OWP: $1,600 / 2 = $800
3. Hourly rate: $800 / (4 \* 5) = $40

### About average weekly earnings (AWE)

Xero calculates the AWE using the employee’s previous 12 months gross earnings, or the earnings since they started work if they’ve been working less than 12 months. This figure is divided by the number of paid weeks before the leave is taken.

For an employee employed for:

- More than a year, paid weeks will be 52 minus any unpaid weeks
- Less than a year, the paid weeks will be the number of weeks since their start date minus any unpaid weeks rounded up to whole weeks

The AWE is then divided by their hours per week to get the hourly rate.

For example, your employee has an OWP of $800 and they received a bonus of $3,000 during the last 12 months. They had taken 2 weeks of continuous unpaid leave. Leave was taken in their 13th month of employment. The AWE is calculated by:

1. Total gross earnings for the last 12 months = $43,000
2. AWE: $43,000 / (52 - 1) = $843.137255
3. Hourly rate: $843.137255 / (4 \* 5) = $42.156863

If you’d like to verify the earnings and the weeks used in the AWE calculations, you can run the gross earnings report for the 12 months prior to the pay period the leave was taken, as reflected in the review dialog box.

If the days per week or the hours per day are zero, the hourly rate can't be calculated. The rate defaults to their normal hourly rate. We recommend that you [update any permanent employee’s Pay & work pattern](Change-an-employee-s-salary-and-wages-details.md) to have values greater than zero in both the days per week and hours per day. This should reflect the average days and hours the employee works.

Gross earnings might slightly differ if pay periods have been processed for that time period, after the pay run was processed. The modal calculations were accurate at the date the pay run was processed.

Manually calculate annual leave rates

### How it works

You can calculate the Ordinary Weekly Pay (OWP) and Average Weekly Earnings (AWE) for yourself.

It's recommended that you [update any permanent employee’s Pay & work pattern](Change-an-employee-s-salary-and-wages-details.md) to have values greater than zero for the days per week and hours per day. This should reflect the average days and hours the employee works.

You’ll need to know what the average hours worked per week is to manually calculate the hourly rate from the higher of the OWP and AWE. This can be found by looking at the employee’s salary and wages at the time the leave was taken.

Alternatively, use the Pay History report to review the hours worked by an employee for a given time period. Ensure you use the same time period to work out the average hours per week as for the earnings used in the AWE calculation. If this differs from the current salary & wages, consider updating the employee’s salary & wages.

The hourly rate entered on the employee’s payslip should be the higher of the two values.

Reach out to a payroll professional if you need help with these calculations

### Calculate Ordinary Weekly Pay (OWP)

1. In the **Payroll menu**, select **Employees**.
2. Click on your employee, then select **Pay template**.
3. Add the total value of all regular earnings and other gross earnings pay items together.
4. Divide the total by the number of weeks in the pay period. This is considered the employee’s OWP.
5. Divide the OWP by the employees average hours per week. This will give you their hourly OWP rate.

If your employee has an irregular work pattern you might need to use the [4 week average](How-to-manually-calculate-annual-leave-rates.md) to calculate their OWP.

### Calculate Average Weekly Earnings (AWE)

1. In the **Reporting** menu, select **All reports**.
2. Under **Payroll**, click **Gross Earnings**.
3. Under **Employees**, select the employee.
4. Select the date range to report on.
5. Click **Update** to run the report.
6. Take the total of that report and divide it by the number of weeks in that date range less any unpaid weeks. This will give you the AWE.
7. Divide the AWE by the employees average hours per week. This will give you their hourly AWE rate.

## What's next?

Now you understand annual leave calculations in Xero, you can [submit a leave request on behalf of your employee](/s/article/Submit-an-employee-s-leave-request-NZ).