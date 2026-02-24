# Prepare a non-MTD VAT return

Source: https://central.xero.com/s/article/Prepare-a-new-non-MTD-VAT-return

---

## Overview

- If you haven't moved to MTD for VAT, check your VAT transactions, then export your VAT return to file outside of Xero.

Tip

VAT registered businesses must use [HMRC's Making Tax Digital (MTD) services](https://www.gov.uk/vat-record-keeping/making-tax-digital-for-vat) (HMRC website) to submit VAT returns. We have separate instructions for our [MTD VAT return](The-VAT-Return.md) or [Flat rate MTD VAT return](The-Flat-Rate-VAT-Return.md).

How it works

The non-MTD VAT return is for businesses who aren’t required to file returns via HMRC’s Making Tax Digital (MTD) service.

Standard rate VAT scheme Flat rate VAT scheme

- Xero calculates the VAT return figures from transactions and journals entered in Xero for the return period.
- You need to select your standard rate VAT scheme in your [financial settings](Set-up-your-organisation-s-financial-details.md) to create a standard rate VAT return in Xero.
- Your VAT scheme controls which transactions your VAT return includes, and when it includes them. [Xero bases this on VAT cash or accrual reporting](/s/article/How-VAT-works-in-Xero-UK) requirements.
- The VAT tax rate selected for a transaction line controls how the VAT return includes line amounts.
- The **Transactions by VAT box** tab and the **Transactions by tax rate** tab list the individual transaction lines and VAT amounts for the period.
- You need the advisor or standard with reports user role to access VAT returns.

- You need to select your flat rate VAT scheme in your [financial settings](Set-up-your-organisation-s-financial-details.md) to create a flat rate VAT return in Xero.
- Your VAT scheme also controls which transactions your VAT return includes, and when it includes them. [Xero bases this on VAT cash or accrual reporting](/s/article/How-VAT-works-in-Xero-UK) requirements.
- [Xero calculates the VAT return box amounts](/s/article/How-VAT-works-in-Xero-UK) by applying your flat rate to transactions and journals you’ve entered. Xero uses the tax rate from the transaction when applying HMRC’s flat rate rules.
- The **Transactions by tax rate** tab lists the individual transaction lines and VAT amounts for the period.
- We have separate instructions if you've switched to our [flat rate MTD VAT return](The-Flat-Rate-VAT-Return.md).
- You need the advisor or standard with reports user role to access VAT returns.

The flat rate VAT return in Xero doesn’t support Domestic Reverse Charge (DRC), so transactions need to be [manually added using the reverse charge provision](Create-a-Domestic-Reverse-Charge-invoice-or-bill.md). Contact Xero support for details on how to record DRC transactions under the flat rate VAT Scheme.

Xero creates a manual journal to balance your VAT account when you finalise your VAT return. You can choose how Xero posts the manual journal.

- If you want Xero to post the journal immediately, add a [flat rate adjustment account](Set-up-your-organisation-s-financial-details.md) in your financial settings. You can view the journal in the Manual Journals screen.
- If you want to check the journal before posting it, leave the **Flat Rate Adjustment Account** field blank in your financial settings. You'll need to add the [account to the draft journal manually](View-edit-or-copy-a-manual-journal.md).

Run the non-MTD VAT return

Standard rate VAT scheme Flat rate VAT scheme

### Before you start

- Check that your VAT scheme and VAT number are correct in your [financial settings](Set-up-your-organisation-s-financial-details.md).
- Enter all transactions for the period and make sure your bank reconciliation is up to date.

### Run the return

1. In the **Reporting** menu, select **All reports**.
2. Find and open the **UK VAT Return**. You can use the search field in the top right corner.
3. If you see:
   - The MTD screen, click **Go to VAT returns without MTD**.
   - The **How would you like to file your VAT?** screen, select **VAT without MTD**, then click **Continue to VAT**.

If you’re using the non-MTD VAT return but want to switch to the MTD VAT return, click **Sign up for MTD**.

### Before you start

- Check that your VAT scheme and VAT number are correct in your [financial settings](Set-up-your-organisation-s-financial-details.md).
- Enter all transactions for the period and make sure your bank reconciliation is up to date.
- Add a flat rate adjustment account in your [financial settings](Set-up-your-organisation-s-financial-details.md) if you want Xero to automatically post a journal to balance your VAT account when you submit your return. You can view the journal in the Manual Journals screen.
- Leave the **Flat Rate Adjustment Account** field blank in your financial settings, if you want to check the journal before posting it. You'll need to add the [account to the draft journal](View-edit-or-copy-a-manual-journal.md) manually.

### Run the return

1. In the **Reporting** menu, select **All reports**.
2. Find and open the **UK VAT Return**. You can use the search field in the top right corner.
3. If you see:
   - The MTD screen, click **Go to VAT returns without MTD**.
   - The **How would you like to file your VAT?** screen, select **VAT without MTD**, then click **Continue to VAT**.
4. If the **Update financial settings box** shows, enter your **Flat rate percentage**, then click **Update**.

If you’re using the non-MTD VAT return but want to switch to the MTD VAT return, click **Sign up for MTD**.

Review the VAT return

Standard rate VAT scheme Flat rate VAT scheme

### Check your transactions

Select the **Transactions by VAT box** or **Transactions by tax rate** tab to check transactions included.

Check that your late claims are included as expected. If it’s your first return in Xero, you need to [add these manually](Adjust-the-amounts-on-a-VAT-return.md)

If you’re on the standard rate VAT scheme, you can [adjust the VAT box amounts](Adjust-the-amounts-on-a-VAT-return.md).

To export a return, click **Export** within a return, then select **Excel** or **PDF**.

### Late claims

Late claims are transactions entered into Xero after the VAT return for the same period was finalised.

Late claims can also arise if you edit, void or delete transactions in a different period than the one in which the transaction was originally entered.

When a transaction that has been included in a previous VAT return period is edited or deleted, Xero will show the original transaction as **Reversed** in the current VAT return. If it's an edited transaction, Xero will also show the updated transaction in the current VAT return.

Xero automatically includes late claims in the next period’s VAT return. However, you need to manually add late claims if:

- It’s your first VAT return in Xero. All future VAT returns will automatically include late claims.
- You've added transactions dated before your conversion date, or have made any changes to these transactions.
- You've [changed to a different VAT scheme](Select-or-update-your-VAT-settings.md). You need to check and manually include any missing transactions, or remove any double counted transactions.

To manually add or exclude late claims, [adjust the return amounts](Adjust-the-amounts-on-a-VAT-return.md).

### Check your transactions

Select the **Transactions by tax rate** tab to check transactions included.

Check that your late claims are included as expected. If it’s your first return in Xero, you need to add these manually.

If necessary, [adjust the VAT box amounts](Adjust-the-amounts-on-a-VAT-return.md) on your return. View adjustments on the **Non-Posting adjustments by VAT box** tab.

To export a return, click **Export** within a return, then select **Excel** or **PDF**.

### Late claims

Late claims are transactions entered into Xero after the VAT return for the same period was finalised.

Late claims can also arise if you edit, void or delete transactions in a different period than the one in which the transaction was originally entered.

When a transaction that has been included in a previous VAT return period is edited or deleted, Xero will show the original transaction as **Reversed** in the current VAT return. If it's an edited transaction, Xero will also show the updated transaction in the current VAT return.

Xero automatically includes late claims in the next period’s VAT return. However, you need to manually add late claims if:

- It’s your first VAT return in Xero. All future VAT returns will automatically include late claims.
- You've added transactions dated before your conversion date, or have made any changes to these transactions.
- You've [changed to a different VAT scheme](Select-or-update-your-VAT-settings.md). You need to check and manually include any missing transactions, or remove any double counted transactions.

To manually add or exclude late claims on the flat rate VAT scheme, use the Tax Rate field in a [manual journal](Adjust-the-tax-amount-on-paid-transactions.md). You can adjust all boxes, except for Box 1 (VAT due on sales) and Box 6 (total value of sales).

Attach a file to a transaction

You can attach most standard file types to a VAT transaction, except executable, audio, or video files. Accepted file types include:

| | | |
| --- | --- | --- |
| BMP | NUMBERS | RTF |
| CSV | ODF | RTF/TEXT |
| DOC | ODS | TIF |
| DOCX | ODT | TIFF |
| EML | PAGES | TXT |
| GIF | PDF | XLS |
| JPEG | PNG | XLSX |
| JPG | PPT | ZIP |
| KEYNOTE | PPTX | 7Z |
| MSG | RAR | |

To attach a file to a VAT transaction:

1. From your VAT return, select the **Transactions by VAT box** or **Transactions by tax rate** tab.
2. Click the add file icon next to the transaction.
3. Click **Select files** and choose the relevant file(s) from your computer.
4. Once you've attached the file, close the window.

Alternatively, you can drag and drop an attachment from your computer into the **Files attached** section.

When a file has been attached, you'll see a file icon  next to the transaction along with the number of files attached. To view the files attached to a transaction, click on the file icon .

When a file is attached to a transaction on the VAT return, this will be recorded as a note in the transaction's history.

To delete the attachment:

1. Click the file icon .
2. In the **Transaction details** window, click the delete icon  next to the attachment, then click **Remove**.

Finalise the return

Once you've reviewed the return, click **Finalise VAT return** to save a final copy of your return.

To create a draft bill or invoice for the amount payable, click **Create draft bill for return** or **Create draft invoice for return**. The transaction will be coded to the VAT account in Xero.

After you finalise a return, it’s no longer possible to finalise non-MTD returns or [file MTD](The-VAT-Return.md) returns for previous and overlapping periods.

To delete a finalised return in Xero, click **Delete VAT Return** in the relevant return.

## What's next?

To prevent further changes and close the period, [set a lock date](Set-up-and-work-with-lock-dates.md). You need the [advisor user role](Adviser-user-role.md) to do this.