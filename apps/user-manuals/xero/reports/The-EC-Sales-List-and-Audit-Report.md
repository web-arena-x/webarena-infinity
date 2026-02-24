# The EC Sales List and Audit Report

Source: https://central.xero.com/s/article/The-EC-Sales-List-and-Audit-Report

---

## Overview

- The EC Sales List report displays the total values of goods and services you have sold to customers in the European Union for a selected period.
- An audit report is also available showing the individual transactions making up the total goods and services sales for each customer on the sales list.

About the EC Sales List report

From 1 January 2021, most UK businesses no longer need to use EC tax rates and reports to account for VAT on imports. If you're eligible, you can [apply Postponed VAT Accounting (PVA) adjustments to your VAT return](Apply-a-PVA-adjustment-to-a-VAT-return.md) instead.

If you’re a business in Northern Ireland and you trade with customers or suppliers in Ireland, you might still need to use the EC tax rates to assign transactions to the correct boxes in your VAT return, and EC Sales List.

Get in touch with your customs agent or courier, or HMRC, to check how to account for VAT on imports.

When you run the EC Sales List report, it:

- Displays sales by customer in GBP for the selected period – the VAT rate used on the transaction has either an **EC Sales Goods** or **EC Sales Services** tax type
- Only includes approved invoices and credit notes
- Is run on an accruals basis only, as required by HMRC
- Doesn't cater for late claims (ie a transaction entered in this period with a transaction date that falls within a filed period) – late claims must be added manually before submission to HMRC

Run the EC Sales List report

1. In the **Reporting** menu, select **All reports**.
2. Find and open the **EC Sales List** report. You can use the search field in the top right corner.
3. Enter a **Date Range**.
4. Click **Update**.

Click on the **EC Sales Audit Report** tab to view individual transactions that make up each line on the report.

Complete and file your EC Sales List with HMRC

### Download the submission file

Download the file in CSV format by clicking **Export**, then select **HMRC submission file**. You can download the submission file even if required information is missing, for example, missing contact details due to a manual journal, or a late claim is to be added.

### Edit the submission file for manual journals and late claims

You'll need to edit the file before submitting it to HMRC if your advisor has posted a manual journal affecting zero-rated EC sales VAT in the report period, or if you have late claims.

You might want to ask your advisor for help with this step.

1. Once you've downloaded the submission file, find and open it in Notepad or another text editor program.
2. Where information is missing for a manual journal, add the customer's country code and VAT number to the file.
3. To add information for a late claim, enter the following data, separating each item with a comma:

   - Two letter country code for the customer
   - Customer VAT number
   - Amount of transaction in GBP rounded down to a whole pound figure
   - **0** for goods or **3** for services.
4. Save the edited file to your computer.

### Submit the EC Sales List to HMRC

When your submission file is complete and correct, file your EC Sales List with HMRC. Ask your advisor for help if required.

Refer to the [HMRC website](http://www.gov.uk/guidance/vat-how-to-report-your-eu-sales#5) for more information on how to submit your EC Sales List.

Common issues and how to resolve them

### Report doesn't load

A report might not load if there are too many transactions for the period. You could either:

- Export the report to Microsoft Excel or Google Sheets. Even though the report doesn't appear on your screen, it will be exported.
- Run the report in stages for a shorter date range, then export the report to Excel or Google Sheets to consolidate the data.

### Contact has missing or invalid details

- Contact record is incomplete – click on the line for the contact to go to the contact record. Update the country and VAT number and save the changes, then run the report again.
- Customer is not located in the EU – find the transaction on the EC Sales Audit report and edit it to change the VAT rate used.
- Duplicate contact – if you have two or more versions of the same contact, [merge the contacts](/s/article/Merge-contacts-UK).
- Transaction created using cash coding – sometimes transactions created using cash coding might be missing details, such as payee. Find the transaction on the EC Sales Audit report, then edit it to add the correct payee.
- Transaction from a manual journal – if there's a posted manual journal affecting EC Sales VAT, the journal is listed under the **Manual Journals** section on the EC Sales Audit report. Edit the CSV file to add the customer's country and VAT number before submitting the file to HMRC.

### Customer is from a country not required by this report

Zero-rated EC Sales VAT rate is incorrectly used for a customer with a UK VAT number. View and edit the transaction on the EC Sales Audit report.

EC Sales Audit report

The audit report shows individual transactions making up the total goods and services sales for each customer on the EC Sales List report. Xero creates the EC Sales Audit report at the same time as the EC Sales List report – you can't run it separately.

### Adjust for manual journals

If there's a posted manual journal affecting zero-rated EC Sales VAT, it's listed in the audit report's **Manual Journals** section. You'll need to edit the export submission file and add the customer's country and VAT number before submitting the file to HMRC.

You might want to talk to your advisor before making an adjustment.

### View and edit transactions on the report

You might want to talk to your advisor before editing the tax rate on a transaction as it might affect your [VAT return](The-VAT-Return.md). To view and edit transactions, run the report, then:

1. Click anywhere on a line in the report to view the transaction details.
2. Click **Invoice Options** or **Credit Note Options**, then select **Edit**. If the invoice or credit note is paid, [delete the payment transaction](Remove-payment-from-an-invoice-or-bill.md) first.
3. Edit the **Tax Rate** field.
4. (Optional) If you removed a payment from your invoice or credit note, apply the payment again.
5. Run the EC Sales List report again, then click into the **EC Sales Audit Report** tab to check the transaction is correct.

## What's next?

You can [export the report](Export-or-print-a-report.md) to file it with HMRC.