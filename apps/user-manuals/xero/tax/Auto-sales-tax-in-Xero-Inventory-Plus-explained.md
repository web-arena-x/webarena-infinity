# Auto sales tax in Xero Inventory Plus explained

Source: https://central.xero.com/s/article/Auto-sales-tax-in-Xero-Inventory-Plus-explained

---

## Overview

- Use the auto sales tax service to automatically calculate sales tax on your sales orders.
- Find out what factors impact sales tax calculation.

## About auto sales tax

Auto sales tax in Xero Inventory Plus (XIP) automatically calculates sales taxes so that accurate tax rates and attributes are applied to your sales orders. The auto sales tax service is provided by Xero and uses information from Avalara, a company that specializes in sales tax compliance.

When you onboard to XIP, you need to connect to Avalara. As auto sales tax helps to ensure the accurate recording and collection of sales tax, Avalara is a mandatory integration and can’t be disconnected.

Auto sales tax helps you collect taxes on sales orders created in XIP to determine your business' tax liability. Once set up, XIP uses the auto sales tax integration with Avalara to calculate taxes based on:

- The settings entered when you set up the integration
- The US state entered for the sales order shipping address

Warning

The accuracy of tax rate calculations is based on the information you provide during the set up of auto sales tax and relevant information on orders in XIP. We recommend you consult with your tax advisor when setting up sales tax.

Sales orders that XIP imports from your connected eCommerce stores contain the taxes your customer paid at checkout in your online store. XIP won’t alter the collected tax totals or sales order total for imported orders.

When you manually create a sales order in XIP, auto sales tax calculates tax as you add products to the sales order. Once a sales order is complete, the final tax liability calculation is submitted to the auto sales tax service and recorded in Xero. The tax will then show in your [Xero Sales Tax report](Run-the-Sales-Tax-report.md).

The Sales Tax report displays your total tax liability for all sales orders in XIP. You can use the report as a resource when filing your sales tax returns.

## How sales tax is calculated

Factors that impact the tax calculation include:

- **Customers** – Customers can be [marked as tax exempt](View-edit-or-delete-a-customer-in-Xero-Inventory-Plus.md). When you do this, tax won’t be calculated for any further sales orders for that customer. For a customer with both tax exempt and non-exempt sales orders, create a separate customer record for each tax exempt status.
- **Products** – Products should be [assigned a tax code](View-or-edit-a-product-in-Xero-Inventory-Plus.md) which determines the tax rate and attributes that should be applied.
- **Location address** – With auto sales tax, you need to declare whether you are registered for sales tax in the US state a sales order is being shipped to. Consult with a tax professional to determine whether you should register a state.
- **Shipping address** – The sales order shipping address also has an impact on tax calculations and is a factor in determining a transaction’s tax liability.

If you change a customer’s tax exemption status or product tax codes, the changes won't apply to existing open sales order tax totals and rates. This includes both issued and unissued sales orders. Changes to tax settings only impacts estimations on new sales orders.

## What's next?

[Set up the auto sales tax service](Set-up-auto-sales-tax-in-Xero-Inventory-Plus.md) for Xero Inventory Plus.