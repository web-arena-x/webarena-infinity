# Troubleshooting your fixed asset reconciliation

Source: https://central.xero.com/s/article/Troubleshooting-your-fixed-asset-reconciliation

---

## Overview

- Find and fix differences in the Fixed Asset Reconciliation report.
- Points to check include opening balances, draft or unregistered assets and manual journals.

How it works

The Fixed Asset Reconciliation report compares the fixed asset account balances on your Balance Sheet with your asset register.

There are a number of reasons why the asset balances on your Balance Sheet might differ to the values in the register. Use the sections below to troubleshoot the issue.

Check opening balances

If you've converted to Xero, make sure you [enter opening balances for fixed assets](Enter-opening-balances-for-fixed-assets.md). This will create the fixed asset opening balances in your Balance Sheet.

Check the Balance Sheet

The fixed asset might be recorded in the fixed asset register, but not the Balance Sheet. This can occur if you’ve manually added a fixed asset to the register, but you haven’t recorded the cost of the asset on a spend money transaction, bill or expense claim.

Check the fixed asset register

The fixed asset might be recorded in the Balance Sheet, but not the fixed asset register.

When you buy an asset, Xero can automatically add a draft fixed asset to the register. To create a draft fixed asset when approving a transaction, you need to:

- Code the transaction to an asset account
- Include an entry in the description field

You can [add assets manually](Add-fixed-assets.md) if they weren’t created automatically.

The Fixed Asset Reconciliation report doesn’t include draft assets – you need to [register the assets](Register-fixed-assets.md) for them to appear in the report.

Manual journals and credit notes coded to fixed asset or depreciation accounts adjust the Balance Sheet only. They don’t affect the register. You might need to [add an asset manually](Add-fixed-assets.md).

To track down an asset that’s missing from the Balance Sheet:

1. Run the [Depreciation Schedule](Depreciation-Schedule-new.md) for a list of assets that appear in the asset register.
2. Compare the Depreciation Schedule against the [Account Transactions report](Account-Transactions-report-New.md). Look for fixed asset transactions that appear on the report, but not the schedule.

Check the setup of the fixed asset type in the register

Each asset type should have its own unique asset account and accumulated depreciation account. For example: 160 – Computer Equipment matched to 161 – Less Accumulated Depreciation on Computer Equipment.

On the Fixed Asset Reconciliation report, the Balance Sheet line might differ from the actual Balance Sheet if two separate asset types share the same asset account or accumulated depreciation account.

In your fixed asset settings, check if two asset types are sharing the same account. If you do find a double-up, you’ll need to [edit the asset type](Add-edit-or-delete-a-fixed-asset-type.md) if you want the Fixed Asset Reconciliation report to balance.

## What's next?

If you want to adjust fixed assets, you can:

- [Dispose of a fixed asset](Dispose-of-or-sell-a-fixed-asset.md)
- [Roll back depreciation](Run-or-roll-back-depreciation.md)

As a last resort, you can also start again with fixed assets in Xero by [changing the fixed asset start date](Change-the-fixed-asset-start-date.md). Before making the change, we recommend speaking to your financial advisor about any taxation or reporting implications.