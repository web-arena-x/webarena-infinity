# Import fixed assets

Source: https://central.xero.com/s/article/Import-fixed-assets

---

## Overview

- Import multiple fixed assets into your fixed asset register in Xero.
- Create an import file using our CSV template or import a file exported from another Xero organisation.

What you need to know

### About importing fixed assets

- You need the advisor or standard user role to import fixed assets.
- [Create asset types](Add-edit-or-delete-a-fixed-asset-type.md) before you import the assets.
- If the organisation is going to use tracking, [set up the tracking categories](Set-up-tracking-categories.md) before you import the assets.
- [Turn on tax reporting](Turn-on-tax-reporting-and-pooling-for-fixed-assets.md) and [create fixed asset pools](Create-a-fixed-asset-pool.md) if you're going to import tax and pool depreciation details.
- Assets are imported as draft assets, so you need to register them before they can be depreciated.
- Download the latest version of the import template each time you import assets into Xero. Older versions may differ from the current version and may not upload successfully.

### Importing book and depreciation details

- If your organisation has tax reporting turned on, you need to use an import file that includes the tax value columns. If tax reporting is turned on for your organisation and you download our CSV template, it includes the tax value columns.
- If your organisation doesn't have tax reporting turned on, you can still use an import file that includes the tax value columns. Just leave the columns blank, and Xero will ignore them.
- If you want to import opening tax value balances for registered fixed assets already in Xero, [use the bulk edit process](Bulk-edit-tax-values-for-fixed-assets.md).

Rules and requirements

### Import file rules and requirements

- The first row of the import file should always be the header row.
- Don't delete or re-order any columns.
- Edit or delete all sample data in the template file.
- The asset number must be unique:
 - If the file contains an asset with the same number as an existing draft asset, the details of the draft asset are overwritten by the imported data.
 - If the file contains an asset with the same number as an existing registered or disposed asset, the import won't complete. Change the asset number or remove the asset from the import file.
- Select one format for all dates in the template. Choose either dd/mm/yyyy, mm/dd/yyyy or yyy/mm/dd.
- Only the **AssetName** and **AssetNumber** fields are mandatory. Leave other fields blank if:
 - You want the default settings for the asset type to apply
 - You're going to complete a field after the import
 - The field doesn't apply to that asset

### Template field requirements

Fields with an asterisk (\*) are mandatory.

| Column | Header in template | Asset field in Xero | Description |
| --- | --- | --- | --- |
| A | \*AssetName | Asset Name | Required field, name of asset |
| B | \*AssetNumber | Asset Number | Required field, must be unique, can use any format |
| C | PurchaseDate | Purchase Date | Date format |
| D | PurchasePrice | Purchase Price | Number (no currency symbol or commas). For example, 1250.75 |
| E | AssetType | Asset Type | The exact name of the relevant [asset type](Add-edit-or-delete-a-fixed-asset-type.md#Createafixedassettype) in your fixed assets settings. The asset type's default depreciation details are applied to the asset if you leave those fields blank in the template. |
| F | Description | Description | Free text |
| G & H | TrackingCategory1 & TrackingOption1 | | Enter tracking names exactly as they appear in your settings |
| I & J | TrackingCategory2 & TrackingOption2 | | Enter tracking names exactly as they appear in your settings |
| K | SerialNumber | Serial Number | Free text |
| L | WarrantyExpiry | Warranty Expiry | Date format |
| **Book Value** Leave these fields blank if you want the asset to use the asset type defaults. If you want the asset to have different values from the asset type defaults, enter information into these fields. |
| M | Book\_Depreciation StartDate | Depreciation Start Date | Date format |
| N | Book\_CostLimit | Cost Limit | Number (no currency symbol or commas). For example, 1250.75 Can't be greater than the value in **PurchasePrice** Can't be negative |
| O | Book\_ResidualValue | Residual value | Number (no currency symbol or commas). For example, 1250.75 Can't be greater than the value in **Book\_CostLimit** Can't be negative Leave the cell blank if you want the asset to depreciate over time to 0. [Xero stops depreciating the asset when it reaches this book value](Add-fixed-assets.md). |
| P | Book\_Depreciation Method | Depreciation Method | Exact text of the depreciation method:   - No Depreciation - Straight Line - Diminishing Value - Diminishing Value (150%) - Diminishing Value (200%) - Full Depreciation at Purchase |
| Q | Book\_AveragingMethod | Averaging Method | Exact text of averaging method:   - Actual Days |
| R | Book\_Rate | Depreciation Rate | If the Depreciation Method in column P is No Depreciation or Full Depreciation at Purchase, leave both columns R and S blank. If the Depreciation method is Diminishing Value (150%) or Diminishing Value (200%), leave column R blank and enter an effective life in column S. Otherwise enter either:   - a rate in column R, for example 15.25 - an effective life in column S, for example, 5   Don't enter values in both columns. |
| S | Book\_EffectiveLife | Effective Life (Yrs) |
| T | Book\_OpeningBook AccumulatedDepreciation | Accumulated Depreciation | Number (no currency symbol or commas). For example, 1250.75 Enter the amount of depreciation the asset had accumulated up to the Fixed Asset Start Date. Only applies to assets with a Depreciation Start Date earlier than your [Fixed Asset Start Date](Set-your-fixed-asset-start-date.md). |
| **Tax Value** If you use tax reporting:   - Leave these fields blank if you want the asset to use the asset type defaults. - If you select **Pooled** as the depreciation method, you must enter the pool name at column V. If you don't use tax reporting, leave these fields blank. |
| U | Tax\_Depreciation Method | Depreciation Method | Exact text of the tax depreciation method **Non-pooled asset:**   - No Depreciation - Straight Line - Diminishing Value - Diminishing Value (150%) - Diminishing Value (200%) - Full Depreciation at Purchase   **Pooled asset:**   - Pooled |
| V | Tax\_PoolName | Pool Name | **Non-pooled asset:** Leave blank **Pooled asset:** Exact pool name |
| W | Tax\_PooledDate | Pooled Date | **Non-pooled asset:** Leave blank **Pooled asset:** Pooled date |
| X | Tax\_PooledAmount | Pooled Amount | **Non-pooled asset:** Leave blank **Pooled asset:** The pooled value of the asset on its pooling date Number (no currency symbol or commas). For example, 1250.75 Can't be greater than the value in **PurchasePrice** Can't be negative |
| Y | Tax\_Depreciation StartDate | Depreciation Start Date | **Non-pooled asset:** Date format **Pooled asset:** Leave blank |
| Z | Tax\_CostLimit | Cost Limit | **Non-pooled asset:** Number (no currency symbol or commas). For example, 1250.75 Can't be greater than the value in **PurchasePrice** Can't be negative **Pooled asset:** Leave blank |
| AA | Tax\_ResidualValue | Residual Value | **Non-pooled asset:** Number (no currency symbol or commas). For example, 1250.75 Can't be greater than the value in **Tax\_CostLimit** (if entered) or **PurchasePrice** Can't be negative **Pooled asset:** Leave blank |
| AB | Tax\_AveragingMethod | Averaging Method | **Non-pooled asset:** Exact text of averaging method:   - Actual Days   **Pooled asset:** Leave blank |
| AC | Tax\_Rate | Depreciation Rate | **Non-pooled asset:** If the Tax Depreciation Method in column U is No Depreciation or Full Depreciation at Purchase, leave both columns AC and AD blank. If the Depreciation Method is Diminishing Value (150%) or Diminishing Value (200%), leave column AC blank and enter an effective life in column AD. Otherwise enter either:   - a rate in column AC, for example 15.25 - an effective life in column AD, for example 5   Don't enter values in both columns **Pooled asset:** Leave blank |
| AD | Tax\_EffectiveLife | Effective Life (Yrs) |
| AE | Tax\_OpeningAccumulated Depreciation | Accumulated Depreciation | Only applies to assets with a tax Depreciation Start Date earlier than your [Tax Start Date](Turn-on-tax-reporting-and-pooling-for-fixed-assets.md). **Non-pooled asset:** Enter the amount of tax depreciation the asset had accumulated up to the Tax Start Date. Number (no currency symbol or commas). For example, 1250.75 **Pooled asset:** Leave blank |

Download and prepare the import template

To download our CSV template:

1. In the **Accounting** menu, select **Fixed assets**.
2. Click the menu icon , then select **Import.**
3. Click **Download template**.
4. Save the template file to your computer, then open it.
5. Complete the asset fields in the template.
6. Save the file as a CSV or TXT file type.

To import assets from another Xero organisation:

1. [Export the fixed asset register](Export-fixed-assets.md) from the original organisation.
2. Make any required changes to the file.
3. Save the file as a CSV or TXT file type.

Import the fixed asset file

1. In the **Accounting** menu, select **Fixed assets**.
2. Click the menu icon , then select **Import.**
3. Check the **Asset Type list** to ensure all the asset types in the import file are set up in the organisation.
4. Select the format of the date used in the template file.
5. Click **Browse**, locate your file, then click **Open**.
6. Click **Continue**.
7. Review the **Import Summary**. If there are errors, fix them in the template file, re-upload the file, then click **Continue**.
8. Click **Import**.

## What's next?

Once you've imported all your assets into Xero, [add them to the fixed asset register](Register-fixed-assets.md) so you can depreciate them.