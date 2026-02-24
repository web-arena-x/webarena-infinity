# Export fixed assets

Source: https://central.xero.com/s/article/Export-fixed-assets

---

## Overview

- Export your fixed asset register to a CSV file.
- All fixed assets are included in the file, including disposed assets.

## How it works

- You need the [advisor user role](/s/article/User-roles-and-permissions-in-Xero-Business-edition?userregion=true) to export the fixed asset register.
- Xero exports your entire fixed asset register, including disposed assets, even if you limit the search criteria.
- The assets are grouped by status (Draft, Registered, Sold/disposed), then ordered alphanumerically by asset number.
- The data in the exported file is current as at the export date.

To export the fixed asset register:

1. In the **Accounting** menu, select **Fixed assets**.
2. Click the menu icon , then select **Export**.

## Additional columns in the export file

The fixed assets export file has the same columns as [the import file](Import-fixed-assets.md), with these additional columns:

| Column | Column header | Description |
| --- | --- | --- |
| C | AssetStatus | Whether the asset is:   - Draft - Registered - Sold/disposed |
| V | Book\_BookValue | The asset's current book value |
| W | AccumulatedDepreciation | Accumulated depreciation on the asset at the export date |
| X | DepreciationToDate | The last date depreciation was run in Xero |
| Y | DisposalDate | If the asset is disposed, the date of disposal |

## What's next?

If you're going to re-import this file into your organisation to make bulk changes, take a look at our guide on [importing assets](Import-fixed-assets.md) to ensure the format of your file is correct.