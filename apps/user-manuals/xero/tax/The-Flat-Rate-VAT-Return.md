# File an MTD VAT return for a flat rate scheme

Source: https://central.xero.com/s/article/The-Flat-Rate-VAT-Return

---

## Overview

- Use our flat rate Making Tax Digital (MTD) VAT return if you're on a VAT flat rate scheme.
- Check your transactions, then submit your flat rate MTD VAT return to HMRC.

Tip

We have separate instructions for our [standard rate MTD VAT return](The-VAT-Return.md) and [non-MTD VAT return](Prepare-a-new-non-MTD-VAT-return.md).

How the flat rate MTD VAT return works

Xero creates your VAT returns using the date ranges supplied by HMRC. Xero calculates the VAT return box amounts by applying your flat rate percentage to the transactions you’ve entered.

The VAT return reports on transactions in the current period. However, it will include transactions from earlier periods if they're added during the current return period, and they relate to a period where the VAT return has been filed.

Xero doesn’t include specific transaction details when you submit your VAT return to HMRC. HMRC's [Transaction Monitoring Privacy Notice](https://www.gov.uk/government/publications/transaction-monitoring-privacy-notice/transaction-monitoring-privacy-notice) has information about the data they collect when you're connected to their systems.

You need the advisor or standard + reports user role to run the VAT return, and the [file MTD VAT returns user permission](/s/article/User-roles-and-permissions-in-Xero-Business-edition-UK) to file MTD VAT returns.

The Flat Rate VAT return in Xero doesn’t support Domestic Reverse Charge (DRC), so transactions need to be [manually added using the reverse charge provision](Create-a-Domestic-Reverse-Charge-invoice-or-bill.md).

###

Run your flat rate MTD VAT return

### Before you start

- You need to [connect Xero to HMRC](Switch-to-our-new-VAT-return-for-MTD.md).
- Check that you've selected a flat rate VAT scheme, and your VAT number is correct in your [financial settings](/s/article/Set-up-your-organisation-s-financial-details-UK).
- Add a flat rate adjustment account in your [financial settings](/s/article/Set-up-your-organisation-s-financial-details-UK) if you want Xero to automatically balance your VAT account when you submit your return.
- Enter all transactions for the period and make sure your bank reconciliation is up to date.

### Review your flat rate VAT return

1. In the **Reporting** menu, select **All reports**.
2. Find and open the **UK VAT Return**.
3. From the **Needs Attention** list, click **Review** by the earliest return period.
4. (Optional) To change your flat rate percentage, next to **Flat Rate [number]%**, click **edit**, enter the new percentage, then click **Update**

### Check your transactions

Select the **Transactions by tax rate** tab to check your transactions.

If necessary, [adjust the VAT box amounts](Adjust-the-amounts-on-a-VAT-return.md) on your return. View adjustments on the **Non-Posting adjustments by VAT box** tab.

### Review late claims

Late claims are transactions entered into Xero after the VAT return for the same period was filed. They can also arise if you edit, void or delete transactions in a different period than the one in which the transaction was originally entered.

If a transaction that was originally included in a previous VAT return period is edited or deleted, Xero shows the original transaction as **Reversed** in the current VAT return. If it's an edited transaction, Xero also shows the updated transaction in the current VAT return.

Xero automatically includes late claims in the next period’s VAT return. However, you need to manually add late claims if:

- It’s your first VAT return in Xero. All future VAT returns will automatically include late claims.
- You've added transactions dated before your conversion date, or have made any changes to these transactions.
- You've [changed to a different VAT scheme](Select-or-update-your-VAT-settings.md). You need to check and manually include any missing, or remove any double counted, transactions.

### Attach a file to a transaction

To attach a file to a VAT transaction:

1. In your VAT return, select the **Transactions by tax rate** tab.
2. Next to the transaction you want to attach a file to, click the add file icon , click **Select files**, then choose the relevant file(s) from your computer.
3. Once you've attached the file, close the window.

Alternatively, you can drag and drop an attachment from your computer into the **Files attached** section.

When a file has been attached, you'll see a file icon next to the transaction.

When a file is attached to a transaction on the VAT return, it's recorded as a note in the transaction's history.

To delete an attachment:

1. Click the file icon .
2. In the **Transaction details** window, next to the attachment, click the delete icon , then click **Remove**.

Submit your flat rate VAT return to HMRC

### About submitting the return

- When you submit the return, Xero creates a manual journal to balance your VAT account.
- If you've added a flat rate adjustment account in your [financial settings](/s/article/Set-up-your-organisation-s-financial-details-UK), Xero will post the manual journal when you file your return. You can then [view the manual journal](View-edit-or-copy-a-manual-journal.md).
- If you haven't added a flat rate adjustment account, you can check and [post the draft manual journal](/s/article/Add-import-and-post-manual-journals-UK) yourself. You need to add an adjustment account to the journal before you post it.

### File your return

You need the [file MTD VAT returns user permission](/s/article/User-roles-and-permissions-in-Xero-Business-edition-UK) to submit MTD VAT returns.

1. In the **Reporting** menu, select **All reports**.
2. Find and open the **UK VAT Return**.
3. From the **Needs Attention** list, click **Review** by the earliest return period.
4. Click **Submit to HMRC**.
5. Select the checkbox to confirm you accept the declaration to file, then click **Submit**.

To create a draft bill or invoice for the amount payable, click **Create draft bill for return** or **Create draft invoice for return**. The transaction will be coded to the VAT account in Xero.

Alternatively, click **Back to VAT Returns** to go back to the VAT Returns screen.

You can also click **Download VAT receipt** to download a PDF receipt of your submission for your records. To download a VAT receipt at a later date, go to the [VAT overview](Understanding-your-VAT-overview.md), open a completed VAT return, then click **Download VAT receipt**.

If you want to keep a copy of the VAT return outside of Xero, view the return, click **Export** and select either **Excel** or **PDF**.​​

## What's next?

To prevent further changes and close the period, [set a lock date](Set-up-and-work-with-lock-dates.md).