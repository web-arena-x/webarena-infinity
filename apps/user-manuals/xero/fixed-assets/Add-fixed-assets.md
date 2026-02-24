# Add or copy a fixed asset

Source: https://central.xero.com/s/article/Add-fixed-assets

---

## Overview

- Add a fixed asset directly to the register, or create one from a purchase transaction.
- Record a fixed asset bought outright, or one on hire purchase and paid off in instalments.
- Create a new fixed asset by copying an existing fixed asset with similar details.

Before you start

- You need the advisor or standard user role to create fixed assets in Xero.
- Set the [default fixed asset settings](Set-up-fixed-assets.md) in your organisation.
- Check there are no [lock dates](Set-up-and-work-with-lock-dates.md) set which will prevent you registering the asset.
- [Import assets in bulk](Import-fixed-assets.md) to create multiple fixed assets.

Asset fields explained

**Asset name** and **Asset number** – These are the only fields you need to complete to save a draft asset. Xero automatically assigns a number to each asset in a sequence, but you can change this.

**Warranty expiry** – Enter the date the asset's warranty expires. This information doesn't affect depreciation or the effective life of the asset.

**Serial number** – Enter information to help you identify the asset. This information doesn't affect depreciation.

**Cost limit** – The value of the asset you want to depreciate, if this is less than the cost of the asset. For example, an asset costs 20,000 but you only want to depreciate 15,000. Enter 20,000 at **Purchase price** and 15,000 at **Cost limit**. Xero calculates depreciation on 15,000.

**Residual value** – The value of the asset remaining when you've fully depreciated it. Xero depreciates the asset to nil value if a residual value isn't entered. For example, you believe that your asset will be worth 500 at the end of its depreciable life. Enter 500 at **Residual value**. Xero stops depreciating the asset when its book value reaches 500.

Create a fixed asset in the register

### Assets with existing depreciation

If assets were purchased and depreciated before you moved to Xero, enter the prior depreciation when you create the asset in Xero.

- Set the asset’s **Depreciation start date** as the actual date depreciation began for that asset.
- If the asset's **Depreciation start date** is earlier than the organisation's [fixed asset start date](Set-your-fixed-asset-start-date.md), enter the amount of depreciation the asset had accumulated up to your start date for fixed assets in Xero.
- Xero uses the amount you entered to automatically calculate the asset's value as at the Fixed asset start date.

### Assets that don't depreciate

If you have an asset that isn’t subject to depreciation, such as land, under **Depreciation method**, select **No depreciation**.

### Manually add a fixed asset

Manually add fixed assets to the fixed asset register. No corresponding entry is created in the balance sheet, so you need to record this separately or create a fixed asset from a purchase transaction.

1. In the **Accounting** menu, select **Fixed assets**.
2. Click **New asset.**
3. Enter an **Asset name** and select an **Asset type**.
4. (Optional) Change the asset number assigned to the asset.
5. (Optional) Complete any other details as required.
6. If you don’t want to use the default settings of the asset type, select a **Depreciation method** and edit the depreciation fields.
7. Click **Save as draft** or **Register**.

Create a fixed asset from a transaction

Code a purchase transaction to a fixed asset account code to automatically create a draft fixed asset in the register.

- The transaction description becomes the asset name. If you don't include a description, no asset will be added to the register.
- Xero automatically creates both a draft fixed asset and the balance sheet entry.
- If the quantity on the purchase transaction is nine or less, Xero creates multiple fixed assets. If the quantity is more than nine, Xero combines them into a single fixed asset.
- The fixed asset has a link to see the original transaction. Click the link to see the transaction the asset was created from.
- Editing or deleting the asset doesn’t effect the purchase transaction and vice versa. If you need to change any details, you need to edit both the asset and the transaction.
- Xero doesn’t create a fixed asset if the fixed asset account is assigned after the transaction is approved. Add the asset to the register manually, or delete the original transaction and add a new one.

To create a draft asset from a purchase transaction:

1. Add a new bill, expense claim, or spend money transaction.
2. In the **Account** field, enter a fixed asset account code.
3. In the **Description** field, enter the asset name.
4. Complete the other transaction fields.
5. Approve the bill or expense claim, or save the spend money transaction.
6. [Edit the asset](/s/article/Edit-fixed-assets?userregion=true) and complete the relevant fields, then click **Register**.

Record a fixed asset bought on hire purchase

### How it works

Use a bill or manual journal to record the purchase of a fixed asset that's being paid off in instalments.

Record the value of the item purchased as an asset, and the total amount to be repaid as a liability. Code the repayment transactions to the same liability account to reduce the amount owing.

Tip

Modify the suggested steps below to suit your particular situation. Check with your accountant or financial advisor if you're unsure about any details.

### Use a bill

Use a bill to automatically create the fixed asset in the register.

1. [Add a bill](Add-and-approve-bills.md) Code it to a fixed asset account as if the asset was bought outright.
2. [Record payment on the bill](Record-payment-of-a-bill.md) from your chosen liability account. You may need to [enable payments](Enable-payments-to-an-account.md) to the account first.
3. [Register the fixed asset](Register-fixed-assets.md) created.

### Use a manual journal

Use a manual journal if you don’t want the transaction showing on cash reports such as the Statement of Cash Flows (Business Cash Flow Summary). Manual journals don't automatically create assets in the register, so you need to manually add the asset after posting the journal.

1. Add a manual journal, with:
   - One line recording the fixed asset, and the other the amount owed
   - **Show journal on cash basis reports** cleared
2. Manually add and register the fixed asset.

### Make repayments

Code the payment transactions to the same account you used to record the amount owed. Each time a payment is made to the account, the balance goes down.

To record repayments, either:

- [Create spend money transactions](Add-a-spend-money-transaction.md) in the bank account.
- [Set up a repeating bill](/s/article/Add-or-edit-a-repeating-bill?userregion=true) If the amounts vary, set the bills to save as draft so you can edit the amount.

To split the interest from the principal, record them on separate lines of the spend money or bill, or create separate transactions.

Duplicate an existing fixed asset

Duplicate a draft or registered fixed asset with similar details, then edit the details as required.

To duplicate a draft fixed asset:

1. In the **Draft** tab, open the asset you want to duplicate.
2. Click **Duplicate**.

To duplicate a registered fixed asset:

1. In the **Registered** tab, open the asset you want to duplicate.
2. Click **Options**, then click **Duplicate**.
3. Make any required changes to the new asset.
4. Click **Save** **as draft** or **Register**.

Change the asset numbering sequence

Xero automatically assigns an **Asset number** to an asset when it’s created, based on an automatic sequence.

You can edit the number for that particular asset, or edit the automatic sequence so it applies to all future assets.

1. When creating the new asset, click the arrow next to **Asset number**.
2. Edit the **Prefix** or **Next number**, or both.
3. Click **Ok**.

## What's next?

Make sure all assets [are registered](Register-fixed-assets.md) so they can be depreciated.