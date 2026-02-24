# Prepare or adjust an AIM return

Source: https://central.xero.com/s/article/Prepare-an-AIM-return

---

## Overview

- Prepare an AIM return for your client in Practice Manager to Inland Revenue (IR).
- Make adjustments to an AIM return or amend a filed AIM return.

Warning

We no longer support AIM returns for clients with foreign exchange transactions. AIM returns still support clients without foreign exchange transactions.

Prepare an AIM return to submit to IR

Prepare an AIM return for your client to submit to IR or create a demo return to learn how Practice Manager handles AIM.

The fields in the return are self-explanatory, but there are a few things to note:

- There are a number of adjustments you can make on the form itself. For more information, click **AIM adjustments**.
- If the prior year revenue was over $5m, select the section **76** checkbox to comply with legislation and record that you'd like to continue to file AIM returns.

Before you create an AIM return for a client, [set up your organisation to submit AIM with Practice Manager](Set-up-a-tax-agent-or-bookkeeper-to-file-AIM-returns-in-Practice-Manager.md). This includes configuring the report codes, and mapping them to the client's chart of accounts.

1. In the **Tax** menu, select **Returns**.
2. Find and select the AIM return you've created for your client.
3. Click **Options**, then select **Update from Xero**.
4. Click **[year] AIM** to open the AIM return.
5. Fill in the applicable fields on each tab of the return. When a section has a worksheet, use the worksheet to enter detailed information for the section. Practice Manager saves your changes before you move to another section of the return.
6. Once you’ve filled the form, click **Save & Close**.
7. When the return is ready for review, click **Mark as Complete**.
8. When the return is reviewed, click **Mark as Approved**.
9. When the return is ready to submit, click **Mark as Signed**.

Make adjustments to the AIM return

### About AIM adjustments

Make the YTD taxable profit more accurate by adjusting the raw data imported from Xero on the AIM form itself. Provide as much information as possible so the tax calculations are accurate.

When you make an adjustment on the form, both the original amount from Xero and the revised amount are sent to IR.

Enter negative amounts for adjustments that decrease profit, and positive amounts for adjustments that increase profit.

There isn’t a category of adjustments for coding errors or similar mistakes but you can fix the error in Xero, then click **Update from Xero** to refresh the form.

### Examples of AIM return adjustments

| | |
| --- | --- |
| **Adjustment** | **Detail** |
| **Inventory adjustment** | If inventory levels aren’t maintained in Xero, Practice Manager uses the amount in section **3** **–** **Opening stock (incl. WIP)** or section **5** **–** **Closing stock (incl**. **WIP)**. Click **Override** to adjust the amount in section **5** so it matches the actual inventory. |
| **Fixed asset adjustments** | If the fixed asset schedule is maintained outside Xero, make the following adjustments to include those figures in the AIM calculation:   - **Depreciation adjustment** – Override section **52** with the actual YTD depreciation. The adjustment to profit appears in section **60**. - **Depreciation recovered adjustment** – sections **61A** and **61B** show the depreciation recovered amount from Xero. Click Override and update section **61B** if you've calculated a different amount. The variance becomes the profit adjustment in section **61**. - **Loss on disposal adjustment** – In section **66** **–** **Other adjustments**, add a custom adjustment with the description ‘Loss on disposal’. |
| **Accounts payable adjustment** | If the accounts payable aren’t maintained in Xero these can still be included in the AIM calculation by entering the total in section **45**:   - If the new amount includes some items without GST, amend the GST amount in section **45A.** - If there are non-deductible items in the total accounts payable, enter the GST exclusive amount of these in section **45C.** - The profit adjustment shows in section **45D** and updates into section **64.**   If the accounts payable amount in Xero doesn’t include all invoices, enter the invoices into Xero, then click **Update from Xero**. |
| **Accounts receivable adjustment** | If the accounts receivable isn’t maintained in Xero, these can still be included in the AIM calculation by entering the total in section **30**.   - If the new amount includes some items without GST, you can amend the GST amount in section **30A**. - If there are non-assessable items in the total accounts receivable, enter the GST exclusive amount of these in section **30C**. - The profit adjustment shows in section **30D** and updates intosection **63**.   If the accounts receivable amount in Xero doesn’t include all invoices, enter the invoices into Xero, then click **Update from Xero**. |
| **Private use adjustment** | If additional private use hasn’t been added to the Xero trial balance ie it’s included in the raw profit figure in section **29**, enter this in section **62**. You should enter the YTD amount of any such private use adjustment. |
| **Provisions adjustment** | If there are non-deductible provisions included in the raw profit figure in section **29**, adjust these by overriding the provisions amount in section **44**. The adjustment updates the total in **65**. |
| **Withholding tax deducted on income** | If the business has had withholding tax deducted on income that’s included in sections **2**, **7**, **8**, **9** or **10**, enter the YTD amount in section **72A**. |
| **Losses brought forward** | IR automatically populates any assessed losses that can be deducted from the YTD profit. You can’t manually enter an amount in this field. If shareholding changes mean that last year’s assessed loss can’t be deducted. Click **Override** to change the amount to 0.00. |
| **Other adjustments** | To make sure the YTD taxable profit is as accurate as possible, you can enter up to 20 other adjustments into the worksheet at section **66**. Practice Manager rolls these forward from the previous period’s return. Make sure to always enter the YTD amount. |
| **Shareholders salaries adjustment (companies only)** | If sufficient provisional tax is paid by the company to cover the proposed shareholders salaries, these provisions can be deducted from the YTD profit. Enter the name and YTD salary provision for each shareholder:   - The pro-rated tax shows for each shareholder. - The YTD profit is reduced by the total salaries provision. - The YTD amount of all other income earned by the shareholder isn't taxed. It’s used to ensure the correct marginal tax rates are applied to the salary. Note the flat rate percentages in this formula are only two decimal places so you might see some rounding variances of under $1. - The pro-rated tax is added to the YTD tax due by the company. - To turn off IR provisional tax notifications for a shareholder, include their IRD number in this worksheet. |
| **Penalties & interest** | Penalties and interest charges are displayed at section **73A**. Select the **Override** checkbox to adjust the a**mount. Total year to date amount due** at section **73B** combines sections **73** and **73A**. |
| **Sole traders YTD other income (sole traders only)** | Enter the YTD amount of all other income earned by the individual into section **71A**. This amount isn't taxed but is used to ensure the correct marginal tax rates are applied to the AIM profit. The flat rate percentages in this formula are only two decimal places so you might see some rounding variances of under $1. |

Amend a filed AIM return

If you find an error in the filed return, select the **Do you want to file an amended return** checkbox to file an amendment directly with IR through Xero.

If the return wasn’t successfully filed due to an error, click **Amend** to unlock it so you can retry filing.

Tip

If you want to work on a draft amendment, and review before you submit, click **Save & Close** without submitting to IR.

1. In the **Tax** menu, select **Returns**.
2. Find and open the AIM return you've filed for your client.
3. Under the **Options** menu, select **Amend**, then click **Amend**.
4. Click **[year] AIM** to open the AIM return.
5. Select the **Amended** tab.
6. Select the **Do you want to file an amended return** checkbox.
7. Select a **Reason for amended return** option.
8. Enter **Amended return** details.
9. Click **Save & Close**.

## What's next?

If you haven’t connected a client to Xero before, you’ll be prompted to select the appropriate Xero ledger.