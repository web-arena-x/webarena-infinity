# Sell or dispose of a fixed asset

Source: https://central.xero.com/s/article/Dispose-of-or-sell-a-fixed-asset

---

## Overview

- Record the disposal of an asset you've sold or donated.
- Undo a disposal recorded in error.

## What you need to know

### How it works

- If the fixed asset start date in Xero is in an earlier financial year, run depreciation up to the beginning of this financial year. For example, if the year end is 31 March and you're disposing of a registered asset on 20 August 2016, run depreciation in Xero to 31 March 2016.
- If you sold the asset for cash, the disposal doesn't show on your Statement of Cash Flows report until you create a receive money transaction for the proceeds, or reconcile the bank statement line for the cash received to the **Sale proceeds account**.

### Disposal details explained

- **Date disposed** – The date you sold the asset. Also used as the journal entry date.
- **Sale proceeds** – The tax exclusive amount you sold the asset for. Enter 0 if you donated it.
- **Sale proceeds account** – The account used to reconcile the bank transaction for the sale proceeds.
- **Depreciation for this financial year** – Select the option for this asset.
- **Date** – Date used to calculate depreciation for this financial year if you select **All depreciation up to and including** in the **Depreciation for this financial year** field.

### How gains and losses are calculated

- When you sell an asset for more or less than its book value, Xero calculates the gain or loss on disposal and asks you which account to post it to.
- If the sale price is more than the original purchase price, this difference is posted separately as a capital gain.
- If the asset had a private use percentage in its depreciation settings, Xero splits the gain or loss into business and private gain or loss. The split is calculated using the ratio of private use depreciation to total depreciation.
- If the asset had private use before being added to Xero, you may need to post a manual journal to correct the split between private and business use gain or loss. Only private use depreciation posted in Xero is used in the disposal calculations.

#### Capital gain example

| Field | Value | Calculation |
| --- | --- | --- |
| Purchase price | 10,000 | |
| Accumulated depreciation | 2,000 | |
| Sale price | 10,500 | |
| Book value | 8,000 | 10,000 - 2,000 |
| Total gain | 2,500 | 10,500 - 8,000 |
| Capital gain | 500 | 10,500 - 10,000 |
| Gain on disposal | 2,000 | 2,500 - 500 |

#### Private use example

When you sell an asset that had private use depreciation posted, any gain or loss on the sale is split between private and business portions. The split is calculated using the ratio of private use depreciation to total depreciation.

| Field | Value | Calculation |
| --- | --- | --- |
| Purchase price | 10,000 | |
| Business use accumulated depreciation | 2,000 | |
| Private use accumulated depreciation | 1,000 | |
| Sale price | 9,000 | |
| Book value | 7,000 | 10,000 - 2,000 - 1,000 |
| Total gain | 2,000 | 9,000 - 7,000 |
| Private use gain | 666.67 | 2,000 x (1,000 / 3,000) |
| Gain on disposal | 1,333.33 | 2,000 - 666.67 |

#### Disposal depreciation example

Xero adds or reverses depreciation depending on the options and date you use when recording the disposal. For example, the financial year end is 31 December and you’ve run depreciation up to the end of February of this financial year. You dispose of an asset on 16 April of your financial year. If you select:

- **No depreciation** – Xero reverses the depreciation for the asset for January and February
- **All depreciation up to and including** – And:

 - Enter 28 February, Xero doesn't adjust depreciation
 - Enter 16 April, Xero calculates depreciation to 31 March - the last full month you owned the asset
 - Enter 31 January, Xero reverses depreciation for February

## Record the sale or disposal of an asset

1. In the **Accounting** menu, select **Fixed assets**.
2. Select the **Registered** tab.
3. Click the asset number to open the asset details.
4. Click **Dispose**.
5. Enter the details of the disposal. If you donated the asset, enter 0.
6. Click **Show summary**.
7. Review the disposal summary. If you change any disposal details, click **Update summary** to see the revised disposal summary.
8. Click **Review journals**.
9. Review the journal and if required, select the accounts to use for a gain on disposal, capital gain or loss on disposal.
10. Click **Post**.

## Undo the disposal of an asset

1. In the **Accounting** menu, select **Fixed assets**.
2. Select the **Sold/disposed** tab.
3. Click the asset number to open the asset details.
4. Click **Undo disposal**, then click **Undo** to confirm.

## What's next?

If you’ve sold the asset, [create an invoice](Invoice-a-customer.md) or [receive money transaction](Add-a-receive-money-transaction.md) to record the sale in the general ledger.

Check the details of assets that you've sold or disposed of in the [Disposal Schedule](Disposal-Schedule.md).