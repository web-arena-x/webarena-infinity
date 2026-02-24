# Enter carried back or forward losses

Source: https://central.xero.com/s/article/Enter-carried-back-or-forward-losses

---

## Overview

- Enter carried back or carried forward losses in your client’s accounts and tax return in Xero Tax.

Enter carried back losses

### Before you start

Before you make changes in your client's Xero organisation and company accounts and tax return, you need to manually calculate the repayment due.

You should also download copies of all documents in Xero Tax, as any changes you make override any documents already generated.

### Account for the refund in your Xero organisation

Add two [new accounts in your chart of accounts](Add-or-edit-an-account-in-your-chart-of-accounts.md), a new expense account specifically for corporation tax adjustments and a new current asset account for the tax debtor. We recommend you name the accounts ‘Corp tax adjustments’ and ‘Tax debtor’ to help Xero Tax apply the correct tags.

[Post a manual journal](https://central.xero.com/s/article/Add-import-and-post-manual-journals-UK) to the new accounts, in the current accounting period, for the tax refund amount.

Warning

Xero Tax treats anything posted to the default corporation tax account as an estimate. It overrides any amount posted to this account with calculations from the tax return.

### Edit the current year accounts and tax return

If the accounts and tax return have already been generated in Xero Tax, [reload the data from the Xero organisation](Edit-generated-accounts-and-reports.md) to ensure the data is up to date.

If you haven’t already started the accounts and tax return, you need to [start a new filing](Generate-company-accounts.md).

On the profit and loss tagging page:

1. Find the new expense account.
2. In the **Tag** column, click the edit icon .
3. From the tagging list, select **Increase (decrease) in current tax from adjustment for prior periods**.
4. Click **Save**.

Then, in the tax return:

1. In the **About this return** section, select box **45** to indicate there’s a claim or relief affecting an earlier period.
2. In the **Income** section, copy the amount from box **155.Z** and enter this figure in box **285.W** in the **Deductions and reliefs** section.

Ensure all boxes in the **Bank details (for repayment)** section are completed so that HMRC can make a refund.

### Edit previous year tax return

If box **45** is selected on the current year's return and the loss has been carried back in the computation, you might not need to submit an amended return. We recommend you check the latest [HMRC guidance](https://www.gov.uk/guidance/corporation-tax-calculating-and-claiming-a-loss) (HMRC website).

If you want to submit an amended return to support your claim, you need to edit the previous tax return. If the previous year's tax return was completed in Xero Tax, unlock and edit the return. If it wasn’t completed in Xero Tax, you need to re-create the return.

In the tax return you’ll need to:

1. Select box **35.D** to indicate this is an amended return, if appropriate.
2. Complete box **275.M** with the total trading losses of the current year accounting period.
3. Select box **280** to confirm the losses are included. Box **295** automatically populates once this is entered.
4. Ensure all boxes in the **Bank details (for repayment)** section are completed so that HMRC can make a refund.

You can then be resubmit the return.

Enter carried forward losses

The first time you file a tax return for a client using Xero Tax you need to manually enter carried forward losses. The losses carried forward are automatically populated in future returns.

You can enter carried forward loss amounts in boxes **160.A** and **285.A** on the tax return.

For more information on completing the tax return, please see [HMRCs website](https://www.gov.uk/government/collections/corporation-tax-forms).

## What's next?

[Complete a final review](Review-company-accounts-and-corporation-tax-returns.md) of the accounts and tax return.