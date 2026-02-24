# Add, edit or delete depreciation settings

Source: https://central.xero.com/s/article/Change-depreciation-settings

---

## Overview

- Set up or edit an initial depreciation setting to calculate depreciation.
- Add, edit or delete an adjustment period to change how an asset depreciates in a particular financial year without altering previous depreciation journals.

What you need to know

### How it works

- An asset's initial depreciation settings come from its [asset type](Add-edit-or-delete-a-fixed-asset-type.md). Change the initial settings when you add the asset or edit them at a later date. You can't delete the first depreciation settings for an asset.
- The initial settings apply from the asset's depreciation start date until it stops depreciating, or you add new settings.
- To edit a depreciation setting that's not an initial setting, you need to edit the asset details. If you change the purchase price, depreciation start date, prior accumulated depreciation or asset type, all depreciation is rolled back and re-posted according to the new details.
- To change how an asset depreciates without altering previous depreciation journals, you need to add a new adjustment period. An adjustment applies to the whole financial year, and each asset can only have one adjustment in that financial year.
- You can date new settings for an asset from your fixed assets start date or later.

### Depreciation settings

The initial depreciation settings and an adjustment period for an asset include:

- Depreciation method
- Private use percentage
- Averaging method
- Cost limit
- Residual value
- Depreciation rate
- Effective life
- Investment Boost

#### Requirements for depreciation

- Adjustment periods apply for a full financial year. In the initial financial year, depreciation settings apply from the asset’s depreciation start date through to the end of that financial year.
- An asset can't have more than one depreciation setting in a single financial year.
- You can add an adjustment period for any financial year following the initial financial year, as long as that year doesn’t already have depreciation settings.
- [Lock dates](Set-up-and-work-with-lock-dates.md) prevent you from adding, editing or deleting depreciation settings.
- If assets have more than one depreciation setting across different financial years, only run the Depreciation Schedule for one financial year at a time. Assets with multiple depreciation settings show multiple times if the report period covers more than one setting.

#### Private use of fixed assets

If you add a private use percentage to the depreciation settings for a period, Xero splits the depreciation between the depreciation expense account and private use account. For example, if private use is 20%, 20% of the depreciation for the period is posted to the private use account and 80% to the depreciation expense account.

The depreciation expense account and private use account come from the asset's type. If the asset's private use account field is blank, you need to add a private use account to the asset type before you can add a private use percentage.

When private use is enabled, the depreciation and disposal schedules have additional columns to show the private use portion of depreciation and disposal gains and losses.

#### Investment Boost

If you select 20% for Investment Boost, Xero will make the 20% claim in the month of purchase. Xero will then base the depreciation calculation on the remaining 80%.

Tip

An Investment Boost tax deduction of 20% was rolled out for certain eligible assets purchased on or after 22 May, 2025. Find out more information about [Investment Boost here](https://www.ird.govt.nz/income-tax/income-tax-for-businesses-and-organisations/types-of-business-expenses/new-assets---investment-boost) (IRD website).

Set up the initial depreciation settings

To set up the initial depreciation settings:

1. In the **Accounting** menu, select **Fixed assets**.
2. Select the **Draft** tab.
3. Open the relevant asset by clicking its asset number.
4. At **Book depreciation settings**, select the date the settings are effective from. You'll receive an error if the date you save is before the fixed asset start date.
5. Check the default settings for the asset type, make any necessary changes.
6. Click **Save as draft** or **Register**.

Edit the initial depreciation settings

Warning

If depreciation has already been run for the edited period, Xero rolls back the depreciation for that period and re-posts it using the new settings.

To edit initial depreciation settings for a particular asset:

1. In the **Accounting** menu, select **Fixed assets**.
2. Select the **Registered** tab.
3. Open the relevant asset by clicking its asset number.
4. At **Book depreciation settings**, select **Edit settings**, then make the changes.
5. Click **Save**.

Add a new adjustment period

To change how an asset depreciates without altering previous depreciation journals:

1. In the **Accounting** menu, select **Fixed assets**.
2. Select the **Registered** tab.
3. Open the relevant asset by clicking its asset number.
4. At **Adjustments**, click **New adjustment**.
5. Under **Period**, select the date the new settings are effective from. The effective date is always the first day of that financial year. You'll receive an error if the date you save is before the fixed asset start date.
6. Enter your preferred settings, then click **Save**.

Edit or delete an adjustment period

To edit or delete an adjustment period:

1. In the **Accounting** menu, select **Fixed assets**.
2. Select the **Registered** tab.
3. Open the relevant asset by clicking its asset number.
4. At **Adjustments**, click the edit icon , then make your adjustments.
   To delete, select the period you want to delete, then click **Delete**.

## What's next?

Run the [Depreciation Schedule](Depreciation-Schedule-new.md) to check the depreciation settings for all your assets.