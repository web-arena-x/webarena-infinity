# Edit a pooled fixed asset

Source: https://central.xero.com/s/article/Edit-a-pooled-fixed-asset

---

## Overview

- Change the tax depreciation method of an asset from pooled to another option, to remove an asset from a pool.
- How you edit a pooled asset depends on whether the asset was added directly or transferred into the pool.

## About editing a pooled asset

Edit any field in the **Details** and **Book Value** sections according to the rules in [edit a registered fixed asset](/s/article/Edit-fixed-assets?userregion=true).

The way you make changes in the **Tax Value** section depends on whether an asset was added directly to or transferred into a pool.

If you change the **Depreciation Method** from **Pooled** to another option, the asset is removed from the pool.

If you make a change to a pooled fixed asset and:

- Depreciation for the pool is rolled back and recalculated, your tax reports since the roll back date are affected
- It changes the asset's tax or book opening value in Xero, you may need to re-enter the asset's and pool's opening balances in Xero

## Edit an asset added to a pool

If an asset was directly added to a pool, and:

- Pool depreciation has been run for one financial year from the pooled date, or hasn't been run, edit any field in the **Tax Value** section. When you save your changes:

 - Xero rolls back any pool depreciation since the asset's pooled date
 - Xero recalculates depreciation using the new asset details
 - The pool closing balance may change
- Pool depreciation has been run for more than one financial year after the asset was pooled, you need to [roll back depreciation](/s/article/Run-or-roll-back-depreciation-AU) before you can edit the **Tax Value** section.

 Roll back depreciation to a date where Xero only has to recalculate pool depreciation for one financial year.

To edit a pooled asset:

1. In the **Accounting** menu, select **Fixed assets**.
2. Select the **Registered** tab, then click the asset number to open the asset details.
3. Click **Options**, then select **Edit**.
4. Make your changes, then click **Save**.
5. (Optional) If your changes affect depreciation, click **Continue**.

## Edit an asset transferred into a pool

If you transferred an existing asset into a pool, you can't change any field in the **Tax Value** section of the asset unless you roll back depreciation. To make a change:

1. [Roll back depreciation](/s/article/Run-or-roll-back-depreciation-AU) to the pooled date. Xero removes the asset from the pool and it reverts to a registered non-pooled asset.
2. [Edit the asset](/s/article/Edit-fixed-assets-AU).
3. (Optional) [Transfer the asset to the pool](Add-or-transfer-an-asset-to-a-pool.md).
4. [Run depreciation](/s/article/Run-or-roll-back-depreciation-AU).

## What's next?

After you've edited registered assets, use the [Fixed Asset Reconciliation report](Fixed-Asset-Reconciliation-report-new.md) to check whether the asset register matches the Balance Sheet.