# Fix problems with a NEST pension filing

Source: https://central.xero.com/s/article/Fix-problems-with-pension-filing

---

## Overview

- Correct a pension file sent from Xero that was rejected by NEST.

Tip

Most errors are caused by a mismatch between pension details in Xero and NEST.

Find out why your pension file declined

If NEST rejects the pension file, the payroll admin will get an email from Xero about the error. Click on the link in the email to view the pension error report.

Alternatively, you can download an error report in Xero:

1. In the **Payroll** menu, select **Pension Filings**.
2. Look for submissions with a **Rejected** status.
3. Next to the submission, click **Download Error Report (PDF)**.

Once you’ve read the report, fix the error using the instructions below.

Invalid header or trailer record

**Error message:** IFC01916 You must provide a valid header or trailer record.

You might receive this error if:

- The pay reference period dates in Xero don’t match those in your NEST account
- An employee’s pension group or subgroup in Xero doesn’t match the group in NEST

### Check pay reference period dates

The pay reference period relates to when you paid your employees, rather than when they worked the hours.

Under automatic enrolment rules, assessments and contributions must be calculated based on the pay reference period that includes the payment date. On an arrears pay run, this means the pay reference period will be different to the pay period (earnings period).

For example, if you set up a monthly frequency from 1–31 March with a payment date on 31 March, the pay reference period will be 1–31 March. However, if you set the payment date to fall in the next period (eg 1 April), the pay reference period will be 1–30 April. The same principle applies to other frequencies (eg weekly or fortnightly).

Check your pay reference period dates in Xero match those in NEST. You can find the pay reference period in Xero on the Pension Filings page (it’s listed under each pension file).

### Check employee groups or subgroups

Check your employee groups and subgroups in Xero match those in NEST. If necessary, you can adjust the groups in Xero:

1. In the **Payroll** menu, select **Employees**.
2. Click an employee’s name to open their details.
3. In the **Pension** section, update the **Pension Group** and **Pension Subgroup** fields if necessary.
4. Click **Save**.
5. In the **Payroll** menu, select **Pay employees**.
6. Find the pay run that generated the pension file and [revert it to draft](/s/article/Revert-a-pay-run-to-draft-UK).
7. Post the pay run again and submit the updated pension file.

If the groups in Xero are correct and you’ve recently reassigned an employee to a different group in NEST, simply [submit the pension file again](Connect-and-file-pension-contributions-with-NEST.md#SubmitpensioncontributionfileswithNEST) in Xero.

If you create a new group in NEST, refresh your scheme details in Xero:

1. In the **Payroll** menu, select **Payroll settings**.
2. Select the **Workplace Pension** tab, then click **Refresh scheme**.
3. Follow the steps in the section above to check employee groups and subgroups, reset the pay run and resubmit the pension file.

Member's start date is in the future

**Error message**: IFC01821 We can't enrol a member using a start date in the future.

This error message might appear you pay your employees in arrears and the employee's Assessment date is in the future. In this case, you should submit the pension file once the employee's Assessment date has passed.

As the pension file was rejected, it’s not possible to submit it electronically. We recommend manually submitting the pension contributions for the period. You can then continue submitting the pension files electronically for future pay runs.

One or more contributions are less than the minimum

**Error message**: MIN\_CONTR\_VAL\_FLD\_RLTD One or more contributions you've entered for this member are less than the minimum you've agreed to pay for them.

This error might appear if:

- An employee’s details in NEST aren’t set up as eligible for tax relief
- An employee’s pensionable earnings in NEST aren’t correct (eg the auto calculate button in your NEST account isn’t selected correctly)
- The pension contribution percentages in your organisation are lower than the minimum set for the tax year

To check an employee's settings for tax relief and pensionable earnings, [contact NEST](https://www.nestpensions.org.uk/schemeweb/nest/resources/contact-us.html).

To ensure pension contribution percentages meet the [minimum for the tax year](https://www.thepensionsregulator.gov.uk/en/business-advisers/automatic-enrolment-guide-for-business-advisers/minimum-contribution-increases-planned-by-law-phasing) (The Pensions Regulator website), check the **Workplace Pension** tab and update the percentages if they’re incorrect:

1. In the **Payroll** menu, select **Payroll settings**.
2. Select the **Workplace Pension** tab.
3. Under **Pension scheme**, check the employee and employer contribution percentages.
4. If the percentages are incorrect, click **Refresh scheme** to update them.

Then, check the contribution percentages in your employee pay templates:

1. In the **Payroll** menu, select **Employees**.
2. Click each relevant employee’s name to open their details.
3. Select the **Pay template** section.
4. Under **Deductions**, update the employee contribution percentage if necessary.
5. Under **Employer pensions**, update the employer contribution percentage if necessary.
6. Click **Save**.

You can then revert your pay run to draft, reset payslips and resubmit the pension file:

1. In the **Payroll** menu, select **Pay employees**.
2. Find the pay run that generated the pension file and [revert it to draft](/s/article/Revert-a-pay-run-to-draft-UK).
3. In the draft pay run for each employee:

   - Click an employee’s name to open their payslip.
   - Click **Reset Payslip**, then click **Save**.
4. Post the pay run again and submit the updated pension file.

## What's next?

For further guidance on error messages, see [NEST’s page on fixing errors](https://www.nestpensions.org.uk/schemeweb/helpcentre/fixing-errors.html). If you still can't fix an error message, contact Xero support below.