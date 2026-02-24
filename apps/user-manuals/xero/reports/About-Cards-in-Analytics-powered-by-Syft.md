# About widgets in Analytics

Source: https://central.xero.com/s/article/About-Cards-in-Analytics-powered-by-Syft

---

## Overview

- Widgets in Analytics display key financial information about your organisation.
- Understand how widgets and their metrics are calculated.

What you need to know

If you have advisor or standard + reports access, you can use widgets in [Analytics dashboards](Dashboards-with-Analytics-powered-by-Syft.md) to give you enhanced insights of your organisation’s financial data.

Widgets are interactive panels that make up dashboards. When you add, edit or delete a widget, the change is visible to anyone who can view it.

To understand how widget metrics are calculated, check the definition and formula used for each widget’s calculation.

Widgets in Analytics are divided into categories: **Profitability, Cash**, **Customers**, **Products**, **Profit & Loss and Balance Sheet**, **Business health scorecards** and **External data.**The **Image** categorylets you add up to three images onto a widget.

You can [edit and customise widgets](Add-edit-or-delete-cards-in-Analytics-powered-by-Syft.md) in your dashboards to adjust widget size, period displayed, graph type and colour theme. You can use artificial intelligence in the template widgets available on the [performance dashboard](Dashboards-with-Analytics-powered-by-Syft.md) template.

Click on the graph or **Click to drill down** to view more detailed data about the graphs in a widget.

Analytics refreshes your data every 24 hours. To ensure the dashboard and widgets are up-to-date, click **Refresh now** to manually refresh your data.

Profitability widget calculations

| **Category** | **Definition** | **Analytics formula** |
| --- | --- | --- |
| Income and expenses | A comparison between what your business receives and what it spends. | Income and expenses = total income vs total expenses. Total income = The sum of all accounts that have the Account type set as Revenue, Sales or Other income. Total expenses = The sum of all accounts that have the Account type set as Expenses, Overheads, Direct costs and Depreciation. |
| Income | The income received by your business from all sources. | Total income = The sum of all accounts that have the Account type set as Revenue, Sales or Other income. |
| Expenses | The total costs and outlays your business incurred. | Total expenses = The sum of all accounts that have the Account type set as Expenses, Overheads, Direct costs and Depreciation. |
| Profit and loss | Profit is the difference between income and expenses. If expenses are less than income, this results in a profit. If expenses are more than income, this results in a loss. | Profit = Income - Expenses. Total income = The sum of all accounts that have the Account type set as Revenue, Sales or Other income. Total expenses = The sum of all accounts that have the Account type set as Expenses, Overheads, Direct costs and Depreciation. |
| Top sales accounts | The sales earned from core operations. | Top sales accounts = The account codes with Revenue or Sales account types. The highest 3–10 accounts are displayed. Other income is excluded. |
| Top expenses accounts | Represents top operating expenses related to keeping your business running, but not directly linked to making products to sell. For example, rent, power, internet, office supplies and depreciation. | Top expenses accounts = Operating expenses. Operating expenses = The sum of all accounts with an Expenses, Depreciation or Overheads account type. The highest 3–10 accounts are displayed. Direct costs are excluded. |
| Top cost of sales accounts | Cost of sales or costs of goods sold. Costs directly linked to making products to sell. | Top cost of sales accounts = The total of all transactions in the period coded to an account code with the Direct Costs account type. The highest 3–10 accounts are displayed. |
| Top other income accounts | Money earned from activities outside your main business activities. | Top other income accounts = Other income. The total of all transactions coded to an account code with account type Other income. The highest 3–10 accounts are displayed. |

Cash widget calculations

| **Category** | **Definition** | **Analytics formula** |
| --- | --- | --- |
| Cash in vs cash out | A comparison of money received (cash in) versus money spent (cash out) during a period. | Cash in vs cash out = Cash inflows vs cash outflows. (i) Excluding bank transfers. |
| Cash in | The total money received by the business (positive movements on the bank account). | Cash in = Cash inflows. (i) Excluding bank transfers. |
| Cash out | The total money spent by the business (negative movements on the bank account). | Cash out = Cash outflows. (i) Excluding bank transfers. |
| Net cash flow | The difference between cash in and cash out over a period (movement in the bank accounts). | Net cash flow = Cash in - Cash out. (i) Excluding bank transfers. |

Customers widget calculations

| **Category** | **Definition** | **Analytics formula** |
| --- | --- | --- |
| Customer sales | The total amount invoiced to all customers over a specific period, excluding tax. | Customer sales = The sum of all invoiced amounts. All account types applied to the invoice are included. (i) This value is based on approved invoices and applied credit notes. Cash sales and credit applied to an invoice from prepayments are not included in the calculation. |
| Growth in customer sales | The increase or decrease in customer sales compared to a previous period. | Growth in customer sales = Current period customer sales - Previous period customer sales. Customer sales = The sum of all invoiced amounts. All account types applied to the invoice are included. Overall average = Sum of the Growth in customer sales in the period selected (daily, monthly or quarterly) / by the number of periods selected. (i) This value is based on approved invoices and applied credit notes. Cash sales and credit applied to an invoice from prepayments are not included in the calculation. |
| % Growth in customer sales | The percentage increase or decrease in customer sales compared to a previous period. | % Growth in customer sales = (Current period customer sales - Previous period customer sales) / Previous period customer sales x 100. Customer sales = The sum of all invoiced amounts. All account types applied to the invoice are included. Overall average = Sum of the % Growth in customer sales in the period selected (daily, monthly or quarterly) / by the number of periods selected. (i) This value is based on approved invoices and applied credit notes. Cash sales and credit applied to an invoice from prepayments are not included in the calculation. |
| Average customer spend | How much, on average, each active customer spends over a specific period. Knowing your average customer spend is helpful in identifying customers' spending habits. | Average customer spend = Total customer sales / Active customers. Customer sales = The sum of all invoiced amounts. All account types applied to the invoice are included.This value is based on approved invoices and applied credit notes. Cash sales and credit applied to an invoice from prepayments are not included in the calculation. Active customers = Count of unique customers with at least one invoice during the given period. Overall average = Sum of the Average customer spend in the period selected (daily, monthly or quarterly) divided by the number of periods selected. |
| Median customer spend | How much revenue you typically make per customer. | Sales are calculated per customer and then ranked from lowest to highest. The middle number is then taken. If the number of customers is even, it’s the average of the two middle values; if odd, it’s the exact middle. Customer sales = The sum of all invoiced amounts. All account types applied to the invoice are included This value is based on approved invoices and applied credit notes. Cash sales and credit applied to an invoice from prepayments are not included in the calculation. |
| Max customer spend | The highest amount spent by a single customer in a given period. | Sales are calculated per customer and then ranked from lowest to highest. The highest number is then taken. Customer sales = The sum of all invoiced amounts. All account types applied to the invoice are included This value is based on approved invoices and applied credit notes. Cash sales and credit applied to an invoice from prepayments are not included in the calculation. |
| Number of purchases by customers | The total number of customer invoices. | Number of invoices by customers = The number of approved invoices in the period. Credit notes are excluded. |
| Growth in purchases | The increase or decrease in the number of customer invoices compared to a previous period. | Growth in customer invoices = Number of invoices in the current period - number of invoices in the previous period. Overall average = Sum of the Growth in purchases in the period selected (daily, monthly or quarterly) / by the number of periods selected. (i) This value is based on approved invoices only. |
| % Growth in purchases | The percentage increase or decrease in the number of customer invoices compared to a previous period. | % Growth in customer invoices = (Number of invoices in the current period - number of invoices in the previous period) / Number of invoices in the previous period x 100. Overall average = Sum of the % Growth in purchases in the period selected (daily, monthly or quarterly) / by the number of periods selected. (i) This value is based on approved invoices only. |
| Discounts given | The total value of discounts applied to invoices. | Discounts given = Discounts added to invoices. (i) This value is based on approved invoices with applied discounts only. |
| Refunds | The total value of credit notes issued to customers for returned or canceled purchases. | Refunds = Credit notes value. (i) This value is based on credit notes that were applied to invoices. |
| Customer cost of sales | The direct costs associated with products or services sold to customers. | Customer cost of sales = Cost price of set Products and Services x units sold. Cost of sales is based on invoices only and doesn’t include the impact of credit notes. Note: Customer cost of sales is recorded when a sales invoice is paid or awaiting payment that includes an inventory item (both tracked or untracked). The Cost of Sales is calculated using the cost price of the item. Xero uses the average cost price to calculate Cost of Goods Sold (COGS). This means there could be a difference between this value and the amount recorded in the profit and loss or sales reports. |
| Active customers | Customers who have made at least one invoice or engaged with your business during a specific period, such as a month, quarter, or year. This metric helps measure customer engagement and retention. | Active customers = Count of unique customers with at least one invoice during the given period. Overall average = Sum of the Active customers in the period selected (daily, monthly or quarterly) / by the number of periods selected. |
| New customers | Number of new customers who were invoiced per period. | New customers = Count of unique customers with their first invoice in the given period. |
| Top customers | Customers who generate the highest revenue or sales amount for your organisation during a specific period. | Top customers based on total amount invoiced. This is a maximum of the top 10 customers, ordered highest by amount received. |

Products widget calculations

Tip

To populate these metrics you must be using [Xero Inventory (Products & services)](Options-for-managing-inventory-in-Xero-US.md) in Xero.

| **Category** | **Definition** | **Analytics formula** |
| --- | --- | --- |
| Product sales | The total revenue generated from all products, excluding tax. (i) This value is based on invoices only. | The sum of all product sales coded to any account type, from approved invoices only. Both tracked and untracked products are included. |
| Growth in product sales | The increase in product sales compared to the previous period. (i) This value is based on invoices only. | Current period product sales - previous period product sales. Product sales = The sum of all product sales coded to any account type, from approved invoices only. Overall average = Sum of the product sales in the period selected (daily, monthly or quarterly) / by the number of periods selected. Both tracked and untracked products are included. |
| % Growth in product sales | The percentage increase in product sales compared to the previous period. (i) This figure is based on invoices only. | % Growth in product sales = (Current period product sales - previous period product sales)/ previous period product sales x100. Product sales = The sum of all product sales coded to any account type, from approved invoices only. Overall average = Sum of the % Growth in product sales in the period selected (daily, monthly or quarterly) / by the number of periods selected. Both tracked and untracked products are included. |
| Product cost of sales | The direct costs incurred to produce or purchase the products sold. (i) Product cost of sales is calculated using the cost method (cost price per item multiplied by units sold), and is based on approved invoices only. | Product cost of sales = Quantity sold, per approved invoice x cost price per item. The cost price is set on Xero in Products and services, per item. Xero’s inventory reports use the average cost method instead to calculate product cost of sales. Both tracked and untracked products are included. |
| Product gross profit | The profit generated from selling products, after accounting for the direct costs. | Product gross profit = Product sales - product cost of sales. Product sales = The sum of all product sales coded to any account type, from approved invoices only. Product cost of sales = Quantity sold, per approved invoice x cost price per item. The cost price is set on Xero in Products and services, per item. Both tracked and untracked products are included. |
| Unique customers | The total number of distinct customers who made a purchase. (i) This figure is based on invoices only. | Count of unique customers. Overall average = Sum of the Unique customers in the period selected (daily, monthly or quarterly) / by the number of periods selected. |
| Average products per purchase | How many products you sell, on average, per invoice. (i) This value is based on invoices only. | Total number of products sold / the total number of approved invoices involving a product. Overall average = Sum of the Average products per purchase in the period selected (daily, monthly or quarterly) / by the number of periods selected. |
| Median products per purchase | How many products you typically sell per invoice. (i) This figure is based on invoices only. | When the number of products sold per approved invoice are ranked from lowest to highest, the middle number is taken. |
| Max products per purchase | The highest number of products sold on a single invoice. (i) This figure is based on invoices only. | When the number of products sold per approved invoice are ranked from lowest to highest, the highest number is taken. |
| Quantity sold | The total number of product units sold. (i) This figure is based on invoices only. | The quantity of products sold. |
| Growth in quantity sold | The increase or decrease in the total quantity sold compared to the previous period. (i) This figure is based on invoices only. | Growth in quantity sold = Quantity sold in the current period - quantity sold in a previous period. Overall average = Sum of the Growth in quantity sold in the period selected (daily, monthly or quarterly) / by the number of periods selected. |
| % Growth in quantity sold | The percentage increase or decrease in the total quantity sold compared to the previous period. (i) This figure is based on invoices only. | % Growth in quantity sold = (Quantity sold in the current period - quantity sold in a previous period) / quantity sold in a previous period x 100. Overall average = Sum of the % Growth in quantity sold in the period selected (daily, monthly or quarterly) / by the number of periods selected. |
| Number of purchases of products | The number of product purchases by customers. (i) This figure is based on invoices only. | The total number of invoices involving a product. |
| Average spend per purchase | The average amount customers spend on an approved invoice with a product assigned. (i) This value is based only on invoices with products assigned. | Average spend per purchase = Total product sales / The total number of invoices involving a product. Product sales = The sum of all product sales coded to any account type, from approved invoices only. Overall average = Sum of the Average spend per purchase in the period selected (daily, monthly or quarterly) / by the number of periods selected. |

Profit & Loss and Balance Sheet widget calculations

| **Category** | **Definition** | **Analytics formula** |
| --- | --- | --- |
| Summarised Profit and Loss | A condensed version of a company's full profit and loss (income statement), presenting key financial data such as revenue, expenses, and net profit. | N/A |
| Summarised Balance Sheet | A condensed version of a company's full balance sheet that presents key financial data, such as assets, liabilities and equity. | N/A |
| Income | The revenue made from primary business activities, which typically involves buying and selling goods or services. (i) The donut chart displays the top four accounts, with the remaining accounts grouped under Other. | Income = amounts coded to Revenue and Sales account types. Other income is excluded. |
| Cost of goods sold | Cost of sales, also known as the Cost of Goods Sold (COGS), represents the direct costs a business incurs to produce the goods or services it sells. (i) The donut chart displays the top four accounts, with the remaining accounts grouped under Other. | Cost of goods sold = amounts coded to Direct costs. |
| Other income | Income earned from activities outside an organisation's core operations. It's considered supplemental income and isn't directly linked to the primary goods or services offered. (i) The donut chart displays the top four accounts, with the remaining accounts grouped under Other. | Other income = the sum of all account codes with an Other income account type. |
| Operating expenses | Costs an organisation incurs in its day-to-day operations that aren’t directly related to producing the goods or services sold. These are the expenses required to run the business and support its core activities. (i) The donut chart displays the top four accounts, with the remaining accounts grouped under Other. | Operating expenses = the sum of all accounts with a Expenses, Depreciation or Overheads account type. Direct costs are excluded. |
| Current assets | Resources an organisation expects to convert to cash, sell, or consume within one year or within its normal operating cycle. These are liquid assets that are readily available to fund day-to-day operations. (i) The donut chart displays the top four accounts, with the remaining accounts grouped under Other. | Current assets = the sum of all accounts with a Current Asset, Prepayments, Inventory, or Bank account type. The Xero Balance Sheet will automatically switch negative bank accounts from current assets to current liabilities, while this widget doesn't. |
| Cash and cash equivalents | The amount of money a company holds in its checking and savings accounts at financial institutions, readily available for use. (i) The donut chart displays the top four accounts, with the remaining accounts grouped under Other. | The sum of all accounts that have the Account type set as Bank. The Xero Balance Sheet will automatically switch negative bank accounts from current assets to current liabilities, while this widget doesn't. |
| Non-current assets | Assets that an organisation does not expect to convert to cash or use up within one year. This is a broad category that includes fixed assets, as well as intangible assets and long-term investments. (i) The donut chart displays the top four accounts, with the remaining accounts grouped under Other. | Non-current assets = The sum of all accounts with a Non-current assets or Fixed assets account type. |
| Current liabilities | Obligations an organisation expects to settle within one year or within its normal operating cycle, typically using current assets. (i) The donut chart displays the top four accounts, with the remaining accounts grouped under Other. | Current liabilities = The sum of all accounts with a Current Liability account type. Non-current liabilities and Liability account types are excluded. The Xero Balance Sheet will automatically switch negative bank accounts from current assets to current liabilities, while this widget doesn't. |
| Long-term liabilities | Obligations an organisation does not expect to settle within one year. These are long-term debts and commitments. (i) The donut chart displays the top four accounts, with the remaining accounts grouped under Other. | Long term liabilities = The sum of all accounts that have the Account type set as Non-current liabilities or Liability. Current liabilities are excluded. |
| Equity | The total value of what the company owns outright. It may also be referred to as owner’s equity or shareholders' equity. | Equity = Total assets - Total liabilities. |

Business health scorecards widget calculations

Business health scoreboard widgets reflect your business health scorecard templates. To understand how Xero calculates your business health scorecard metrics, you can check the [definitions and formulas used](About-business-health-calculations-in-Analytics-powered-by-Syft.md).

External data widget calculations

The information in the External data widget is entered by the user. No specific calculations are applied to this widget.

## What's next?

If you’re having trouble, contact Xero support below.