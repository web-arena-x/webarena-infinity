# Apply a PVA adjustment to a VAT return

Source: https://central.xero.com/s/article/Apply-a-PVA-adjustment-to-a-VAT-return

---

## Overview

- Apply a postponed VAT accounting (PVA) adjustment to your VAT return.
- Add a bill to make a PVA adjustment.

What you need to know

Eligible UK businesses can apply PVA adjustments to their VAT returns. PVA adjustments let you postpone VAT payments on imports instead of having to pay them up front, then recover them later. [Check if you’re eligible](https://www.gov.uk/guidance/check-when-you-can-account-for-import-vat-on-your-vat-return) (GOV UK website) to make PVA adjustments.

If you’re on a standard VAT scheme, you can apply PVA adjustments directly to your return. The PVA adjustment updates box 1 and 4 of your VAT return.

If you’re on the flat rate VAT scheme, you can [add a non-posting adjustment](Adjust-the-amounts-on-a-VAT-return.md) to boxes 1 and 7 of the return to record a PVA transaction.

If you prefer to account for PVA with a transaction, you can create a bill instead.

To account for VAT on imports without PVA, use the [VAT on Imports tax rate](/s/article/Using-non-standard-tax-rates-UK).

Apply a PVA adjustment to your return

Before you apply the adjustment to your VAT return, [download your Monthly Postponed Import VAT Statement (MPIVS)](https://www.gov.uk/guidance/get-your-postponed-import-vat-statement) (GOV UK website) so that you have the most current amounts to refer to.

1. In the **Reporting** menu, select **All reports**.
2. Find and open the **UK VAT Return**.
3. Open the VAT return period you need to add the adjustment to.
4. Scroll down, then click **Apply Postponed VAT Accounting (PVA) adjustments**.
5. Select a **MPIVS Period**, then enter the **MPIVS Amount**.
6. (Optional) Add details about the adjustment. These appear in the history section and **Transactions by VAT box** tab of your VAT return.
7. (Optional) To attach a file, in the **Upload Monthly Postponed Import VAT Statement** section click **Select file**, or drag and drop an attachment from your computer into this section.
8. (Optional) To add another adjustment, click **Add additional statement**. You can add up to 13 adjustments to a VAT return.
9. Click **Save**. Box 1 and 4 of your VAT return will be updated.

Create a bill to make a PVA adjustment

Before you start, [add a new custom tax rate](/s/article/Add-or-edit-tax-rates-UK) called Postponed VAT @ 20% or something similar using the Domestic Reverse Charge Expense tax type and the tax percentage that applies. This allows the tax rate to function in the same way PVA is intended.

After you've added the new tax rate, [create a bill](Add-and-approve-bills.md) with two transaction lines.

Within the bill:

1. In the **Amounts are** field, select **Tax Exclusive**.
2. In the first transaction line:
   - In the **Unit Price** field, enter the total purchase amount.
   - In the **Tax Rate** field, select the PVA tax rate you set up. This updates box 1 and 4 of your VAT return.
3. In the second line:

   - In the **Unit Price** field, enter the same total purchase amount as a negative value to reverse the amount. Use the same account code as the line above.
   - In the **Tax Rate** field, select a zero rated tax rate. This ensures no additional amounts are reported in box 7 of your return.

The gross line amounts of the bill will show in reports, but if you use the same account they will offset each other in the totals.

Attach a file to a PVA adjustment

You can attach a file while applying a PVA adjustment to your VAT return.

If you’ve already applied a PVA adjustment to your VAT return, you can attach a file:

1. In your VAT return, select the **Transactions by VAT box** tab.
2. Next to the PVA adjustment, click the add file icon .
3. In the **Monthly Postponed Import VAT Statement (MPIVS)** section, click **Select file**then choose the relevant file from your computer, or drag and drop an attachment from your computer into this section.
4. Once you've attached the file, in the top left corner close the window.

When a file has been attached, you'll see a file icon  next to the adjustment.

To delete the attachment:

1. Click the file icon .
2. In the **Transaction detail** window, click the delete icon  next to the attachment, then click **Remove**.

## What's next?

Review your [standard MTD](The-VAT-Return.md), [flat rate MTD](The-Flat-Rate-VAT-Return.md) or [non-MTD VAT](Prepare-a-new-non-MTD-VAT-return.md) return.