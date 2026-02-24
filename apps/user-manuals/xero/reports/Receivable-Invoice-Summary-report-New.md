# Receivable Invoice Summary report

Source: https://central.xero.com/s/article/Receivable-Invoice-Summary-report-New

---

## Overview

- The Receivable Invoice Summary lists sales invoices, credit notes and overpayments for the report period. You can include prepayments and quotes in the report.
- Adjust the report to show top customers.

## About the report

Run the Receivable Invoice Summary report to see a list of sales invoices, credit notes and overpayments for your customers. You can:

- Include prepayments and quotes in the report
- Adjust the report to show top customers

The report includes all invoices by default, including any deleted and voided invoices. You can apply filters to exclude these or group the report by status so they have separate totals.

If you use [multicurrency](About-multicurrency.md), the report can show the value of foreign currency transactions in both source (foreign) and base currencies. Foreign currency amounts are converted using the exchange rate as at the date of the report.

You need the advisor, standard + reports or read only user role to access this report.

## Run the report

1. In the **Reporting** menu, select **All reports**.
2. Find and open the **Receivable Invoice Summary** report. You can use the search field in the top right corner.
3. Select a **Date range**. You can also click the arrow next to the date to choose a set reporting period – for example, **This month** or **This quarter**.
4. Under **Date Search**, choose the type of date you'd like to search by, such as **Due Date** or **Invoice Date**.
5. Click **Update**.

## Customise your report

Use the settings and filters at the top of the report to customise it:

- Choose which **Columns** appear on your report, such as **Contact Account Number**, **Due Date** and **Last Payment Date**.
- Change the report layout by **Grouping/Summarising** the details.
- Add a **Filter** to refine the report results, then click **Apply**.
- Click **More** to:

 - Include **Prepayments** or **Quotes.**
 - Show or hide **Decimals.**
 - Show or hide the **Exchange rate note** if your organisation uses multicurrency. This displays foreign currency disclosures on your report and details of the conversion rates used.

After choosing an option above, click **Update** to rerun the report with your option selected.

To filter by prepayments or quotes, you must first include them on the report under **More**.

| Common column options | Description |
| --- | --- |
| Balance | The outstanding balance of the invoice as at the report date. If you have multicurrency, the exchange rate for the Balance (base currency) column is as at the report date. |
| Contact Account Number | The unique number pulled from the Account Number field in the contact's details. For example, a registration or membership number. |
| Discount (ex) and Discount (inc) | Shows the value of any discount attached to the transaction. Ex = excludes sales tax and inc = includes sales tax. |
| Expected Date | The expected payment date entered for an invoice, or the due date if you haven't entered an expected payment date. |
| Invoice Seen | Whether your contact has viewed the online invoice. Only applies if you've sent an online invoice. This applies for all time, not just within the date range of the report. |
| Invoice Sent | Whether your invoice was [emailed from within Xero](Email-multiple-customer-invoices.md). This applies for all time, not just within the date range of the report. |
| Last Payment Date | The date of the most recent payment added to the invoice in Xero. |
| Payments/Credits | All payments and credit allocations. When you've applied a prepayment to an invoice, it will appear in this column even if your report doesn't include prepayments individually. If you have multicurrency, the exchange rate for the Payments/Credits (base currency) column is the same as when the transaction was added to Xero. |
| Realised Gains | The gain or loss realised when you apply a payment or credit to a foreign currency invoice. |
| Unrealised Gains | The unrealised gain or loss associated with a foreign currency invoice. This doesn't apply to draft invoices. |
| Foreign exchange (FX) | If you use multicurrency, you can add or remove columns that show foreign currency transactions in their source (foreign) currency. Add the Currency Rate column to see the currency rate for the transactions. |

## Show top customers or quotes

### About common formats for top customers or quotes

Select one of the following common formats and Xero will configure the report for you:

- All quotes summary – a summarised list of quotes in chronological order.
- Approved, sent and paid – shows approved, sent and paid sales invoices, credit notes, overpayments and prepayments for your customers.
- Outstanding quotes summary – a summarised list of open quotes and invoices grouped by customer.
- Top customers – a list of your top customers, based on sales invoice value, over the last quarter. This format includes a chart to illustrate your top customers.

### Select a common format

1. In the **Reporting** menu, select **All reports**.
2. Find and open the **Receivable Invoice Summary** report. You can use the search field in the top right corner.
3. From the panel on the left side of the screen, select **All quotes summary**, **Approved, sent and paid**, **Outstanding quotes summary**or **Top customers**.

   If you select **Top customers**, click **Chart**, then choose **None**, **Chart Only** or **Chart and table**.
4. (Optional) Click a row on the report to see details of the underlying invoices or quotes.

You can exit the common format and return to the standard report if you prefer. On the panel, under **Xero standard report**, click **Receivable Invoice Summary**. To hide the panel, click **Minimise**.

If you use a common format frequently, you can [mark it as a favourite](Access-and-browse-reports.md).

## What's next?

To refer back to these results at another time, [save the report as a draft or publish it](Save-or-publish-a-report.md). You can also [export the report](Export-or-print-a-report.md) to either a PDF or spreadsheet format.