# Executive Summary

Source: https://central.xero.com/s/article/Executive-Summary

---

## Overview

- Run the Executive Summary to get an overview of your income and performance.
- The Executive Summary gathers key performance indicators from the Cash Summary report, the Profit and Loss (Income Statement) report and the Balance Sheet.

## About the Executive Summary

The Executive Summary shows key performance indicators for your selected date range. It pulls amounts from other reports or shows ratios based on those amounts.

Click an amount in the Cash, Profitability or Balance Sheet sections to go to the base report.

- Cash amounts drill down to the Cash Summary report.
- Profitability amounts drill down to the Profit and Loss (Income Statement) report.
- Balance Sheet amounts drill down to the Balance Sheet.

Xero calculates the amounts and percentages in the Sales, Performance and Position sections. When you export the report to either Excel or Google Sheets, the figures are copied across, but the formulas aren’t. You can't drill down to other reports from these figures.

If you use multicurrency, the report converts foreign currency amounts to your base currency.

Users in your organisation with read-only, standard + reports and advisor user roles can view the Executive Summary.

## Run the basic report

1. In the **Reporting** menu, select **All reports**.
2. Find and open the **Executive Summary**. You can use the search field in the top right corner.
3. Select a **Date range**. You can also click the arrow next to the date to choose a set reporting period, eg **Last month** or **Month to date**.
4. Select other options you want the report to show.
5. Click **Update**.

Whenever you like, you can click **Save as** and save a report as:

- **Draft** – shown on the **Draft** tab and can be edited
- **Published** – shown on the **Published** tab and can’t be edited
- **Custom** – shown on the **Custom** tab, and can be customised

Alternatively, click **Export** to download an Excel, Sheets or PDF copy of the report.

## Report options

### Compare with

Compare amounts for your chosen date range with amounts from previous periods, the average amount, or no comparison.

By default, Xero compares like with like. For example, if you choose **Last month** as your date range, Xero uses months for your comparison periods. You can choose other comparison periods to suit your needs.

If you choose to compare with the previous period or the average, the report includes a variance column. The column shows the percentage change between one row and another. The arrow icons show whether the variance is an increase (up arrow) or decrease (down arrow), and whether it’s favourable (green) or unfavourable (red).

The average is for the same period as your selected date range, and is calculated from the start of the financial year. For example, if you run the report for a month, the average will be the monthly average since the start of that financial year.

### Filter

Use the **Filter** button to include or exclude specific lines in the report. For example, select the checkbox next to **Net assets** to include it as a line in the report. Once you’ve selected your filters, click **Apply**.

### More

Click **More** to:

- Select or clear the **Decimals** checkbox to display two decimal places or round numbers only.
- Add a **Year to date** column to the report.
- Show or hide the **Exchange rate note** if your organisation uses multicurrency. This displays foreign currency disclosures on your report and details of the conversion rates used.

## Executive Summary calculations

### Cash

- **Cash received**: Total of all payments received to all bank accounts, including credit card transactions.
- **Cash spent**: Total of all payments made from all bank accounts, including credit card transactions.
- **Foreign currency gain (loss)**: Unrealised gains (losses) on all bank accounts, including credit card transactions. Equivalent to the Currency Adjustment row in the Cash Summary report.

 This line only shows if you have multicurrency, and there’s a gain or loss in a foreign currency bank account.
- **Cash surplus (deficit)**: Cash Received - Cash Spent + Foreign currency gain (loss).
- **Closing bank balance**: Sum of all bank accounts at their base currency amount, including credit card balances.

### Profitability

- **Income**: Total of all accounts with the Revenue account type in your chart of accounts.
- **Direct costs**: Total of all accounts with the Direct Costs account type in your chart of accounts.
- **Gross profit (loss)**: Income - Direct cost.
- **Other income**: Total of all accounts with the Other Income account type in your chart of accounts.
- **Expenses**: Total of all accounts with the Expenses account type in your chart of accounts.
- **Profit (loss)**: Gross profit (loss) + Other Income - Expenses.

### Balance Sheet

- **Debtors**: Total owed to you by your customers.
- **Creditors**: Total owed by you to suppliers + unpaid expense claims.

 Unpaid expense claims added using [classic expense claims](About-Xero-Expenses.md) won't show in this report.
- **Net assets**: Agrees with the total equity figures on the Balance Sheet. There might be a small rounding discrepancy.

### Sales

- **Number of invoices issued**: Agrees with the number of approved sales invoices for the selected period. Excludes prepayments, overpayments and credit notes.
- **Average value of invoices**: (Total tax exclusive value of invoices for the period - Total tax exclusive value of credit notes) / Number of sales invoices in the period.

 If the value of credit notes exceeds the value of sales invoices, the average will be zero.

### Performance

When you export the report to Excel or Google Sheets, the formulas aren’t copied across.

- **Gross profit margin (%)**: Gross profit (loss) / Revenue x 100.
- **Net profit margin (%)**: Profit (loss) / Revenue x 100.
- **Return on investment (p.a.) (%)**: Profit (loss) / Net assets x Date range.

 For example, if your selected date range is quarters, the formula is Profit (loss) / Net assets x 4.

### Position

When you export the report to Excel or Google Sheets, the formulas aren’t copied across.

- **Average debtor days**: (Accounts receivable balance / Sales) x Days in period.
- **Average creditor days**: (Accounts payable balance / Cost of goods sold) x Days in period.
- **Short term cash forecast**: Debtors - Creditors.
- **Term assets to liabilities:** Fixed assets / Non-current liabilities. Non-current liabilities in this formula includes accounts with the Non-current liability or Liability type.
- **Current assets to liabilities**: Current assets / Current liabilities. Current assets in this formula include accounts with the Current Asset, Prepayment and Bank type. Bank accounts with a credit balance are treated as Current Assets.

## What's next?

You've nailed it. We recommend a well-earned break!