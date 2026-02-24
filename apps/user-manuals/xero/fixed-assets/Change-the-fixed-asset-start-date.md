# Change the fixed asset start date

Source: https://central.xero.com/s/article/Change-the-fixed-asset-start-date

---

## Overview

- Change the fixed asset start date to align it with the financial year end date, or to start again with fixed assets in Xero.
- Changing the start date reverses all depreciation for registered and disposed fixed assets.

Tip

Before making the change, we recommend speaking to your financial advisor for any taxation or reporting implications.

**1** What you need to know

### How it works

- You need to change the fixed asset start date if your organisation’s financial year end is updated. Xero notifies you in the Fixed asset screen if the financial year end date has been changed.
- If you change the date to a future date, all fixed assets registered and depreciated before the new start date revert to draft status.
- If you’re using diminishing value as the depreciation method, you’ll need to make sure you select a fixed asset start date where depreciation will be recorded for the full 12 months.
- If a lock date is set for all users, [change the lock date](Set-up-and-work-with-lock-dates.md) to a date earlier than both the old and new fixed assets start dates.
- You need the advisor user role to change the fixed asset start date.

### Which dates you can choose

The earliest financial year you can choose is the year of your Xero conversion date. For example, if your conversion date is April 2023 and your financial year begins on 1 July, the earliest fixed asset start date will be 1 July 2022.

The latest financial year you can choose is the one after the current financial year. For example, if it's now October 2023 and your financial year begins on 1 January, you can choose 1 January 2024 as your fixed asset start date, but not any later.

### Starting again with fixed assets

Change the fixed asset start date to start again with fixed assets in Xero. Changing the start date reverses the depreciation, disposals, and adjustments on all the assets in the register. Then either:

- [Export the assets](Export-fixed-assets.md), make changes to the file, then [import the assets](Import-fixed-assets.md) with the updated details
- [Delete the draft assets](Delete-a-fixed-asset.md) and start again from scratch

If you don't want to change the fixed asset start date in your organisation, you can start a new organisation with the new year end date. Talk to your accounting advisor about how to close your current organisation and open a new one correctly.

**2** Run and publish reports

Before you start, we recommend you run and publish these reports, so you have a record of the assets in the register before the change.

Run these reports for each financial year end and month end if you need monthly figures, starting from when you began using fixed assets in Xero. Also, run the reports for the day before the new fixed asset start date. For example, if your new fixed assets start date is 1 January 2025, run this report as at 31 December 2024:

- [Depreciation Schedule](Depreciation-Schedule-new.md) and [Fixed Asset Reconciliation report](Fixed-Asset-Reconciliation-report-new.md).
- If your organisation uses Tracking, run the [Balance Sheet](Balance-Sheet-New.md) and [Profit and Loss report](Profit-and-Loss-New.md) for each tracking category.
- Run the [Disposal Schedule](Disposal-Schedule.md).

**3** Change the date

Warning

If you’re using diminishing value as the depreciation method, ensure you select a fixed asset start date where depreciation will be recorded for the full 12 months.

Change the fixed assets start date to the first day of the new financial year. For example, if you're changing the financial year end from 30 June to 31 December 2024, change the fixed assets start date to 1 January 2025.

1. In the **Accounting** menu, select **Accounting settings**, then click **Fixed assets settings**.
2. Click **Change start date**, then select the new start date.
3. Click **Save**.

**4** Update the assets

1. [Export the fixed assets](Export-fixed-assets.md) from your organisation.
2. Open the exported file and make the following changes:
   - Delete the rows containing assets disposed before the new fixed assets start date.
   - In the **Book\_OpeningBookAccumulatedDepreciation** column, delete the exported values and enter the accumulated depreciation values from your Depreciation Schedule report as at the day before the new fixed assets start date.
3. Save the file in CSV format.
4. [Import the file](Import-fixed-assets.md) into Xero to update the draft fixed assets.
5. [Register the assets](Register-fixed-assets.md).

**5** Account for movement in fixed asset accounts

[Post manual journals](Add-import-and-post-manual-journals.md) to account for movements in the fixed asset accounts in the previous years you used fixed assets in Xero. Use the reports you ran in Step 2.

You might need to create journals for these movements in fixed assets:

- Depreciation on assets since purchase date or registration date in Xero
- Gain or loss on disposal of disposed assets

## What's next?

Once you've updated the fixed asset start date, you may need to go through and [run depreciation](Run-or-roll-back-depreciation.md) on the assets again.