# Edit tax depreciation details for multiple assets

Source: https://central.xero.com/s/article/Bulk-edit-tax-values-for-fixed-assets

---

## Overview

- Update the tax depreciation details of multiple registered fixed assets at once.
- Download existing tax details to a CSV file, make changes, then re-upload the file into your organisation.

What you need to know

- You need the advisor user role to bulk edit tax depreciation details.
- New assets can't be added using this process. To add new assets, use our [fixed asset import](Import-fixed-assets.md) process.
- Assets can be added to pools using this process, but they can't be transferred to pools. [Transfers to pools](Add-or-transfer-an-asset-to-a-pool.md) need to be made outside the bulk edit process.
- The CSV file you download includes all non-pooled assets and all pool additions. It excludes draft, sold and disposed assets and any pool transfers.
- Tax depreciation details are updated as at the tax depreciation start date. If you've run depreciation past this date, [roll it back](Run-or-roll-back-depreciation.md).

Template rules and requirements

### Rules for entering tax depreciation details

- Leave the first row in place as the header row.
- Keep the columns in the same order and don't remove any columns.
- Don't change any asset numbers.
- Any assets uploaded with **Pooled** selected as the tax depreciation method are treated as pool additions. Transfers to pools need to be made outside the bulk edit process.
- You can only bulk update the tax depreciation details (columns X to AH) for existing registered assets. Changes made to any other fields in the CSV file are ignored.

### Template field requirements

| Column | Column header in template | Asset field in Xero | Description |
| --- | --- | --- | --- |
| X | Tax\_Depreciation Method | Tax Value Depreciation Method | Exact text of the depreciation method **Non-pooled asset:**   - No Depreciation - Straight Line - Diminishing Value - Diminishing Value (150%) - Diminishing Value (200%) - Full Depreciation at Purchase   **Pooled asset:**   - Pooled |
| Y | Tax\_PoolName | Tax Value Pool Name | **Non-pooled asset:** Leave blank **Pooled asset:** Exact pool name |
| Z | Tax\_PooledDate | Tax Value Pooled Date | **Non-pooled asset:** Leave blank **Pooled asset:** Pooled date |
| AA | Tax\_PooledAmount | Tax Value Pooled Amount | **Non-pooled asset:** Leave blank **Pooled asset:** The pooled value of the asset on its pooling date Number (no currency symbol or commas), for example, 1250.75 Can't be greater than PurchasePrice Can't be negative |
| AB | Tax\_Depreciation StartDate | Tax Depreciation StartDate | **Non-pooled asset:** Date format **Pooled asset:** Leave blank |
| AC | Tax\_CostLimit | Tax Value Cost Limit | **Non-pooled asset:** Number (no currency symbol or commas), for example, 1250.75 Can't be greater than PurchasePrice Can't be negative **Pooled asset:** Leave blank |
| AD | Tax\_ResidualValue | Tax Value Residual Value | **Non-pooled asset:** Number (no currency symbol or commas), for example, 1250.75 Can't be greater than Tax\_CostLimit (if entered) or Purchase Price Can't be negative **Pooled asset:** Leave blank |
| AE | Tax\_AveragingMethod | Tax Value Averaging Method | **Non-pooled asset:** Exact text of averaging method:   - Actual Days   **Pooled asset:** Leave blank |
| AF | Tax\_Rate | Tax Depreciation Rate | Enter information in either AF or AG, not both. **Non-pooled asset:** If the Tax\_DepreciationMethod in column X is No Depreciation, Diminishing Value (150%), Diminishing Value (200%) or Full Depreciation at Purchase, leave this field blank. Otherwise enter either:   - Depreciation rate - Enter a number, for example, 15.25 - Years - For example, 5   Enter information in one column only. **Pooled asset:** Leave blank |
| AG | Tax\_EffectiveLife | Tax Value Effective Life (Yrs) |
| AH | Tax\_OpeningAccumulated Depreciation | Tax Value Accumulated Depreciation. | **Non-pooled asset:** Number (no currency symbol or commas), for example, 1250.75 If you've previously depreciated this fixed asset outside Xero, enter the accumulated tax depreciation amount. **Pooled asset:** Leave blank |
| AI | Tax\_Value | Tax Value | For information purposes only. Information in these columns isn't imported into Xero. |
| AJ | Tax\_Accumulated Depreciation | Tax Accumulated Depreciation |

Update the tax details

Before you start:

- Make sure [tax reporting is turned on](Turn-on-tax-reporting-and-pooling-for-fixed-assets.md).
- [Register](Register-fixed-assets.md) all the fixed assets you want to update.
- [Set up any pools](Create-a-fixed-asset-pool.md) you want to add assets to.
- Check there are no [lock dates](Set-up-and-work-with-lock-dates.md) preventing changes to the tax reporting start date.

If you roll back depreciation before bulk updating your assets, any transferred assets will be removed from their pools. To keep them as transfers, either:

- Transfer them back to their pools before following the steps below.
- Leave them as non-pooled assets during the bulk update, then transfer them back to their pools afterwards.

To bulk update tax depreciation details:

1. In the **Accounting** menu, select **Fixed assets**.
2. Click **Settings**.
3. Select the **Tax Reporting** tab, then click **Bulk Update**.
4. Click **Download registered assets** to download a list of your registered assets as a CSV file.
5. Open the downloaded file in a spreadsheet program such as Microsoft Excel or Google Sheets.
6. Enter or edit information in tax depreciation columns X to AH only, following the rules and formatting requirements.
7. Save the updated CSV file. If there are more than 500 registered assets in the file, split it into multiple files so each file has no more than 500 assets.
8. In Xero, in the **Update Registered Assets** screen, select a date format.
9. Click **Browse**, thenselect the updated CSV file.
10. Click **Continue**, then click **Update**. If you have more than one file, repeat the update process.

## What's next?

If you want to turn off tax reporting, [change the start date](Turn-on-tax-reporting-and-pooling-for-fixed-assets.md).