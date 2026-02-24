# Correct your STP data after a change in ABN or branch number

Source: https://central.xero.com/s/article/Correct-your-STP-data-after-a-change-in-ABN

---

## Overview

- Changes to your ABN or branch number during the tax year can cause double counting of employee year-end income and tax amounts.
- Fix Single Touch Payroll (STP) data errors by running a reset event to zero out the amounts for the incorrect ABN or branch.

What you need to know

Your Australian Business Number (ABN) and branch number are key identifiers for the Australian Tax Office (ATO) and are displayed on taxpayers’ income statements.

If you [update the ABN or branch number](Update-your-ABN-or-branch-number-for-STP.md) in Xero during a financial year, this can result in double counting of employee income and tax year-to-date (YTD) amounts. This is because:

- Any changes made to the ABN or branch number in Xero are filed with the ATO via STP along with the YTD amounts for each employee.
- The ATO system counts the multiple ABNs or branch numbers as different organisations.
- It’s possible employees could receive more than one income statement in their myGov portal for duplicate YTD amounts.

Based on the scenario that’s relevant to you, follow the instructions below to prevent double counting of your employees income and tax amounts.

Warning

We recommend that you speak with your financial advisor or the ATO if you’re unsure whether your organisation needs these adjustments.

STP data filed under incorrect ABN or branch number for current or prior financial year

If you’ve filed payroll with STP under the wrong ABN or branch number, you can fix this using the reset tool which:

- Zeroes out and finalises your employees’ YTD income and tax amounts for the incorrect ABN or branch number
- Sends an update to the ATO that zeroed-out YTD amounts are now displayed against income statements for the incorrect ABN or branch numbers
- Doesn’t impact your pay run journals or your general ledger amounts

When you run your next pay run or file a finalisation with STP, your employees' YTD amounts are updated at the ATO with the correct ABN and branch number from your organisation settings.

To use the reset tool:

1. In the **Payroll** menu, select **Single Touch Payroll**.
2. Select the **Tools** tab, then click **Go to Reset and finalise YTD amounts tool**.
3. Select the relevant tax year.
4. Choose the ABN and branch number combination to be reset. If it isn't shown, select **None of the above** then enter the ABN and branch number to be reset.
5. Click **Next**.
6. Select all the employees to include in the reset event, then click **Next**. Their records will be finalised with $0.00 YTD amounts for the selected ABN and branch number.
7. Select the checkbox for filing authorisation, then click **Submit to ATO**.
8. Review the organisation settings to ensure the correct ABN and branch number are correct for future STP filings, and make any changes if needed.

If the update event to reset and finalise is for your current ABN and branch number combination, the status of the STP finalisation will update in the **Finalisation** tab.

To check the amounts reported in this submission, download a CSV file from the reset and finalise filing.

Your next STP filing for the relevant tax year, including pay runs and finalisation, will report employee’s YTD amounts against the correct ABN and branch number.

For employees in the reset filing, follow up with an STP filing with the correct ABN and branch number to report their YTD amounts to the ATO.

This also applies when a branch number hasn't been entered. The STP filings will default to branch 001 and might need correcting. If you're unsure what your branch number is, reach out to the ATO.

ABN or branch number was changed during the current or prior financial year

### Zero out amounts for the new ABN or branch number

If your business structure has changed part way through the financial year, such as from a sole trader to a company, you need to report payroll information under multiple ABNs or branch numbers. In this case, you need to set up a new Xero organisation for the new ABN and branch number.

If you’ve filed income and tax information with STP under the new ABN and branch number, use the reset tool to zero out amounts for the new ABN and branch number. This avoids duplicate reporting of employees' YTD figures.

Using the reset tool won’t impact your pay run journals or your general ledger amounts.

To use the reset tool:

1. In the **Payroll** menu, select **Single Touch Payroll**.
2. Select the **Tools** tab, then click **Go to Reset and finalise YTD amounts tool**.
3. Select the relevant tax year.
4. Select the latest ABN and branch number combination to reset and finalise with $0.00 YTD amounts. If it isn't shown, select **None of the above** then enter the ABN and branch number to be reset.
5. Click **Next**.
6. Select all the employees to include in the reset event, then click **Next**. These employees will be finalised with $0.00 YTD amounts for the selected ABN and branch number.
7. Select the checkbox for filing authorisation, then click **Submit to ATO**.

Once the reset filing is accepted by the ATO, the employee’s STP data is finalised for the new ABN and branch number.

Next, [update the organisation details](/s/article/Update-your-organisation-s-settings-AU) to include your previous ABN or branch number. Your next STP filing will report your employee’s current YTD amounts to the ATO.

Reverse payroll amounts posted in the current organisation

Once you’ve used the reset tool to zero out amounts for the new ABN or branch number, use an unscheduled pay run to reverse payroll amounts relating to the new ABN or branch number in your current organisation. To do this:

1. [Check the ABN or branch number](/s/article/Update-your-organisation-s-settings-AU) entered is the new one.
2. Download a copy of the [Payroll Activity Summary report](Payroll-Activity-Summary-report.md) for each employee to use as a reference when entering these values in the unscheduled pay run. When running the report, use a date range that includes the date the organisation’s ABN or branch number changed.
3. Create the first [unscheduled pay run](/s/article/Adjust-previous-payroll-payments-AU) to process the negative YTD amounts for all employees, using the figures from the Payroll Activity Summary report as a reference. This will reverse the total payroll amounts for all employees filed under the second ABN or branch number. When the negative unscheduled pay run is filed with the ATO through STP, a nil YTD figure is submitted for each employee under the new ABN and branch number combination.
4. (Optional) If no further payroll amounts need to be processed for your employees under the old ABN and branch number, you can finalise STP in this organisation. Before doing so, update the organisation details to include the old ABN or branch number.

Now you can create a new Xero organisation to reprocess the payroll amounts for your new ABN and branch number.

1. [Create a new Xero organisation](Create-a-Xero-user-account.md) with the new ABN or branch number.
2. Set up payroll and your employee records.
3. (Optional) When setting up payroll, you can select whether YTD values were reported via STP or via PSAR in the STP settings. This ensures opening balances aren’t included in STP reporting.
4. Process an unscheduled pay run to reprocess the YTD amounts that were reversed in your previous Xero organisation. These are the amounts that relate to your new ABN and branch number.
5. File the pay run with STP to report current YTD amounts for the new ABN and branch number.

You can continue to use your new Xero organisation for reporting STP for your new ABN and branch number.

Your employee will now have two income statements with the correct YTD values against each ABN or branch number.

STP data filed with incorrect ABN or branch number for a tax year more than 12 months ago

If STP data has been filed with the incorrect ABN or branch number, fix this by running two unscheduled pay runs. You’ll then have a full year's worth of YTD amounts under the correct ABN or branch number.

For the first unscheduled pay run:

1. Download a copy of the [Payroll Activity Summary report](Payroll-Activity-Summary-report.md) to use as a reference when entering these values in the pay run.
2. [Check the ABN or branch number](/s/article/Update-your-organisation-s-settings-AU) entered is the incorrect one.
3. Create the first [unscheduled pay run](/s/article/Adjust-previous-payroll-payments-AU) to process the negative YTD amounts for all employees. This will reverse the total payroll amounts for all employees filed under the incorrect ABN or branch number. When the negative unscheduled pay run files with the ATO through STP, a nil YTD figure will be submitted for each employee under the incorrect details.

For the second unscheduled pay run:

1. Update the organisation details to include the correct ABN or branch number.
2. Create the second unscheduled pay run for the same amounts, but with positive YTD values. This reposts the YTD payroll amounts for all employees, which can then be filed to the ATO using the correct ABN or branch number.
3. When you’re ready, complete an [STP finalisation](Finalise-Single-Touch-Payroll-data.md) for this ABN or branch number.

Your employee will now see two income statements, one showing nil values with the incorrect ABN or branch number and another with the YTD figures under the correct ABN or branch number.

ABN or branch number was changed during tax year for a tax year more than 12 months ago

If you’ve already filed your STP data but have since changed your ABN or branch number partway through the tax year and need to file these separately, set up a new Xero organisation to file the separate ABN or branch number totals. To do this, you’ll need to process three unscheduled pay runs.

For the first unscheduled pay run:

1. Download a copy of the [Payroll Activity Summary report](Payroll-Activity-Summary-report.md) to use as a reference when entering these values in the pay run.
2. Create the first [unscheduled pay run](/s/article/Adjust-previous-payroll-payments-AU) to reverse the employee YTD data against the current ABN or branch number.
3. [Change your ABN or branch number](/s/article/Update-your-organisation-s-settings-AU) to the correct number for the first part of the year.

For the second unscheduled pay run:

1. Create the second unscheduled pay run to re-process the employee YTD data against the original ABN or branch number.
2. Complete a [STP finalisation](Finalise-Single-Touch-Payroll-data.md) for this ABN or branch number.
3. [Create a new Xero organisation](Create-a-Xero-user-account.md) with the new ABN or branch number.
4. (Optional) When setting up Payroll, you can select YTD where values were reported via STP or PSAR in the [STP settings](Prepare-payroll-balances-before-switching-to-Xero.md). This ensures opening balances aren’t included in STP reporting.

For the third unscheduled pay run, create the third unscheduled pay run to process the employee YTD data that should be filed against the new ABN or branch number.

Your employee will now have two income statements with the correct YTD values against each ABN or branch number.

Submit key identifiers for finalisation or correction

Error code CMN.ATO.PAYEVNT.EM92168 is returned when no scheduled pay runs have been filed under your organisation’s current ABN and branch number. To submit the ABN and branch number to the ATO:

1. Click **Submit key identifiers**.
2. Select the tax year to enable the ABN and branch number for, then click **Next**.
3. Select the employees to report under the ABN and branch number, then click **Next**.
4. Confirm that you accept the authorisation to file, then click **Submit to ATO**.
5. Click **Check filing status** to track the progress of the submission with the ATO.

The ATO will normally process the submission within 15 minutes, but it can take up to 72 hours. You can also check the submission status in the STP Overview page in Xero.

Once the ATO has confirmed the submission is successful, you can finalise your STP data or make a correction using an unscheduled pay run.

## What's next?

Now that you’ve corrected your STP data, it’s ready to [be finalised](Finalise-Single-Touch-Payroll-data.md).