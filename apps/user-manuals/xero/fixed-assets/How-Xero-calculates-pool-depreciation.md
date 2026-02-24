# Pool depreciation in Xero

Source: https://central.xero.com/s/article/How-Xero-calculates-pool-depreciation

---

## Overview

- Xero calculates depreciation differently for assets that have been added directly to, or transferred into a pool.

## How it works

- Xero calculates depreciation on all assets in the pool using the diminishing value depreciation method, as if they were a single asset.
- The value of the pool is adjusted for [assets added or transferred to the pool](Add-or-transfer-an-asset-to-a-pool.md) during the year, and for any pool adjustments in the year.
- New assets pooled on purchase are depreciated in the pool at half rate in the first year.
- Assets transferred into a pool in the second, or later year after you add them in Xero, are depreciated at full rate in the pool.

## Depreciation for pooled assets

### Depreciable value

The depreciable value of an asset in a pool is the pooled amount you enter when you register the asset, or transfer it into the pool.

### Depreciation rate

If you select the Small Business Pool or Low Value Pool, Xero applies default depreciation rates set by the ATO:

- Small Business Pool – Full rate 30.00%, half rate 15.00%
- Low Value Pool – Full rate 37.50%, half rate 18.75%

If you [set up a custom pool](Create-a-fixed-asset-pool.md), you can set your own depreciation rate.

### Pool balance before depreciation

Xero calculates the pool balance before depreciation as:

Opening balance + transferred assets + new assets - disposals + adjustments

## Calculating depreciation

The year's pool depreciation is calculated when depreciation is run for the last month of the financial year. If the pool balance before depreciation is 0 or negative, no depreciation is calculated.

| Amount to be depreciated | Depreciation rate |
| --- | --- |
| Pool opening balance | Full rate |
| New assets added to pool Adjustment for current year addition | Half rate |
| Existing registered assets transferred to pool Adjustment for opening balance or business use | Full rate |

To depreciate an asset at half rate in the first year:

1. [Roll back depreciation](/s/article/Run-or-roll-back-depreciation-AU#) to before the asset's tax depreciation start date.
2. [Edit the asset](/s/article/Edit-fixed-assets-AU) and change the tax Depreciation Method to **Pooled**.
3. Re-run depreciation.

## What's next?

For more details about tax and pool depreciation take a look at the page about how to [run depreciation](/s/article/Run-or-roll-back-depreciation-AU).