# Receivable Invoice Detail report

Source: https://central.xero.com/s/article/Receivable-Invoice-Detail-report-New

---

## Overview

- Run this report to view details of all sales invoices, credit notes and overpayments in a given period. You can include prepayments and quotes in the report.
- Adjust the report to show top customers.

## About the report

Run the Receivable Invoice Detail report to see line-by-line details of sales invoices, credit notes and overpayments for your customers. You can:

- Include prepayments and quotes in the report
- Adjust the report to show top customers

This report includes all invoices by default, including any deleted and voided invoices. You can apply filters to exclude these or group the report by status so they have separate totals.

If you use [multicurrency](About-multicurrency.md), the report shows the value of foreign currency transactions in both source (foreign) and base currencies. Foreign currency amounts are converted using the same exchange rate as when the transaction was added to Xero.

You need the advisor, standard + reports or read only user role to access this report.

## Run the report

1. In the **Reporting** menu, select **All reports**.
2. Find and open the **Receivable Invoice Detail** report. You can use the search field in the top right corner.
3. Select a **Date range**. You can also click the arrow next to the date to choose a set reporting period, eg **This month** or **This quarter**.
4. Under **Date Search**, select the type of date you'd like to search by, such as **Due Date** or **Invoice Date**.
5. Click **Update**.

## Customise your report

Use the settings and filters at the top of the report to customise it:

- Choose which **Columns** appear on your report, such as **Contact Account Number**, **Due Date** and **Last Payment Date**.
- Change the report layout by **Grouping/Summarising** the details.
- Add a **Filter** to refine the report results, then click **Apply**.
- Click **More** to include prepayments or quotes, or show decimals.

After choosing an option above, click **Update** to rerun the report with your option selected.

To filter by prepayments or quotes, you must first include them on the report under **More**.

| Common column options | Description |
| --- | --- |
| Balance | The outstanding balance of the invoice as at the report date. If you have multicurrency, the exchange rate for the Balance (base currency) column is as at the transaction date. |
| Contact Account Number | The unique number pulled from the Account Number field in the contact's details. For example, a registration or membership number. |
| Discount (ex) and Discount (inc) | Shows the value of any discount attached to the transaction. Ex = excludes sales tax and inc = includes sales tax. |
| Discount % | Shows the discount as a percentage of the unit price. |
| Expected Date | Displays the [expected payment date](Add-an-expected-payment-date-to-an-unpaid-invoice.md) entered for the invoice in the Sales screen. The due date displays if you haven't entered an expected date. |
| Invoice Sent | Shows if the [invoice was emailed](Email-multiple-customer-invoices.md) from within Xero, since its creation date. |
| Invoice Seen | Confirms if the online invoice has been viewed, since it was created. |
| Last Payment Date | The date of the most recent payment added to the invoice in Xero. |
| Unit Price (ex) and Unit Price (inc) | Shows the price of a single product or service. Ex = excludes sales tax and inc = includes sales tax. |
| Foreign exchange (FX) | If you use multicurrency, you can add or remove columns that show foreign currency transactions in their source (foreign) currency. Add the Currency Rate column to see the currency rate for the transactions. |

## Show top customers or quotes

### About common formats for top customers or quotes

Select one of the following common formats and Xero will configure the report for you:

- Top customers – a list of your top customers, based on sales invoice value over the last quarter.
- All quotes detail – a detailed list of quotes grouped by invoice number.
- Outstanding quotes detail – a detailed list of open quotes and invoices grouped by customer.

### Select a common format

1. In the **Reporting** menu, select **All reports**.
2. Find and open the **Receivable Invoice Detail** report. You can use the search field in the top right corner.
3. From the panel on the left side of the screen, select **Top customers**, **All quotes detail** or **Outstanding quotes detail**.
4. (Optional) Click a row on the report to see details of the underlying invoices and quotes.

You can exit the common format and return to the standard report if you prefer. On the panel, under **Xero standard report**, click **Receivable Invoice Detail**. To hide the panel, click **Minimise**.

If you use a common format frequently, you can [mark it as a favourite](Access-and-browse-reports.md).

## What's next?

If you'd like to refer back to these results at another time, you can [save the report as a draft or publish it](Save-or-publish-a-report.md). You can also [export the report](Export-or-print-a-report.md) to either a PDF or spreadsheet format.