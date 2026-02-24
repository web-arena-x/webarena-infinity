# Import fixed assets using the Conversion Toolbox

Source: https://central.xero.com/s/article/Import-fixed-assets-using-the-Conversion-Toolbox

---

## Overview

- Use the Conversion Toolbox to import your client’s fixed assets from their previous accounting system into their Xero organisation.

What you need to know

### How it works

- The Conversion Toolbox lets you import multiple fixed assets from your client’s previous accounting software into their Xero organisation.
- You can also use the toolbox to update existing draft assets in your organisation. It can’t be used to update assets already registered.
- You need the advisor or standard user role to import fixed assets.
- [Create asset types](Add-edit-or-delete-a-fixed-asset-type.md) before you import the assets, or during the conversion process.
- If the organisation is going to use Tracking, [set up the tracking categories](Set-up-tracking-categories.md) before you import the assets.
- Assets import as draft assets, so you need to register them before they can be depreciated.

### Before you start

To import fixed assets into Xero, the file you export from your client’s previous accounting system must be in comma-separated values (CSV) format.

If your client’s previous accounting system can’t export data in CSV, either:

- [Use the toolbox to convert the file](Convert-data-to-Xero-using-the-Conversion-Toolbox.md)
- Manually create an import file

Create the import file

### Use the toolbox template

If you can’t export your client's fixed assets from their previous accounting system in comma-separated values (CSV) format, you need to create the file manually using our template. To do this:

1. Open the [Conversion Toolbox](https://conversiontoolbox.xero.com/), then click **Ready to connect to Xero**.
2. Select the client organisation, then click **Allow access**.
3. Click **Import Assets**.
4. Click **What files should I upload?**
5. Click the link to download the template file.
6. Open the file in a spreadsheet program, enter the asset details as required, then save the file in CSV format.

### Rules and requirements

- The asset number must be unique.
 - If the file contains an asset with the same asset number as an existing draft asset, the details of the existing draft asset are overwritten by the imported data.
 - If the file contains an asset with the same asset number as an existing registered or disposed asset, the import won't complete. Change the asset number or remove the asset from the import file.
- Select one format for all dates in the template. Choose either dd/mm/yyyy, mm/dd/yyyy or yyy/mm/dd.
- Only the asset name and number fields are mandatory. Leave other fields blank if:
 - You want the default settings for the asset type to apply
 - You're going to complete a field after the import
 - The field doesn't apply to that asset

### Fields for importing fixed assets

When importing fixed assets, you can add the following information for each asset. **Asset Type**, **Asset Name** and **Asset Number** are mandatory fields, all other fields are optional.

| | |
| --- | --- |
| **Import field** | **Requirements** |
| **Main fields** |
| Asset Name (mandatory) | The name of the asset. |
| Asset Number (mandatory) | The number to assign to the asset. It must be unique. |
| Purchase Date | The date the asset was purchased. Enter in date format. |
| Purchase Price | The amount paid for the asset. Enter as a number only, with no currency symbol or commas. |
| Asset Type (mandatory) | The exact name of the relevant asset type in the fixed asset settings. The assets type’s default depreciation details are applied to the asset if you leave those fields blank in the template. |
| Serial Number | If applicable, the serial number of the asset. |
| Warranty Expiry | The date the warranty on the asset expires. Enter in date format. |
| **Book Value** Leave these fields blank if you want the asset to use the asset type defaults. If you want the asset to have different values from the asset type defaults, enter information into these fields. |
| Book Depreciation Start Date | The depreciation start date for the asset. Enter in date format. |
| Book Cost Limit | The cost limit of the asset. Enter as a number, with no currency symbol or commas. This value can’t be greater than the Purchase Price and it can’t be a negative number. |
| Book Residual Value | The residual value of the asset. Enter as a number, with no currency symbol or commas. This value can’t be greater than the Cost Limit and it can’t be a negative number. Leave this field blank if you want the asset to depreciate over time to 0. Xero stops depreciating the asset when it reaches this value. |
| Book Depreciation Method | The depreciation method for the asset. Enter the exact text for the method: - No Depreciation - Straight Line - Diminishing value - Full depreciation at Purchase |
| Book Averaging Method | The averaging method for the depreciation. Enter the exact text for the method:   - Full Month |
| Book Rate | If the Depreciation Method is No Depreciation or Full Depreciation at Purchase, leave this field blank. Otherwise, enter either:   - A Book Rate - An Effective Life (in years)   Don’t enter values in both columns. |
| Book Effective Life |
| Book Opening Accumulated Depreciation | The amount of depreciation the asset had accumulated up to the Fixed Asset Start Date. Enter as a number, with no currency symbol or commas. This field only applies to assets with a Depreciation Start Date earlier than the Fixed Asset Start Date. |

Import the file

1. Open the [Conversion Toolbox](https://conversiontoolbox.xero.com/), then click **Ready to connect to Xero**.
2. Click **Allow access**, then select the client organisation.
3. Click **Import Assets**.
4. Click **Select CSV File to Upload**, select the import file, then click **Start Conversion**.
5. In the **Field** column, select the field that maps to each column in the import file, then click **Next Step**.
6. In the **Xero Asset Type Name** column, select the asset type that matches the imported asset types, then click **Next Step**.
7. Preview the assets to import. Click **Show Details** to expand the list. Click **Previous step** to make changes in the toolbox. If you need to make changes to the import file, go back to step 4 and select the file again.
8. Click **Next Step**, then click **Finish**.

## What's next?

Run the [Fixed Asset Reconciliation report](Fixed-Asset-Reconciliation-report-new.md) to verify everything has imported correctly.