# The GST Calculation Worksheet

Source: https://central.xero.com/s/article/The-GST-Calculation-Worksheet

---

## Overview

- The GST Calculation Worksheet shows how GST is calculated for the older Business Activity Statement (BAS).
- You can access the worksheet while you are running your BAS.

Tip

This page explains how to complete your activity statement using Xero's old BAS report. See the page for completing [the Activity Statement](The-Simpler-Business-Activity-Statement.md) if you use the new report.

## About the GST Calculation Worksheet

The GST Calculation Worksheet shows how Xero calculates the GST figures in the BAS, when using the Full BAS reporting method.

The GST Calculation Worksheet is not included with the BAS in Xero if you selected a GST Calculation option of **Quarterly (Option 2)** or **Quarterly (Option 3)** in your [Activity statement settings](Set-up-your-organisation-s-financial-details.md).

The worksheet is one of the reports making up the Full BAS. Xero creates it at the same time - you can't run it separately.

## Access the GST Calculation Worksheet

When you run your BAS, select the **GST Calculation Worksheet** tab to see the report.

## How Xero populates fields in the worksheet

You can view transactions making up each amount on the [GST Audit Report](/s/article/The-GST-Audit-Report-AU). Xero populates the worksheet's fields with tax-inclusive transaction amounts in the reporting period using the following rules:

### GST amounts you owe the Tax Office from sales

**G1** - All transaction lines with these tax rates:

- GST on Income
- GST Free Exports
- GST Free Income
- Sales accounts with the tax rate Input Taxed
- Your own tax rates with the tax types Sales, GST Free Sales, and Exempt Income when used with sales accounts.

**G2** - All transaction lines with the tax rate GST Free Exports.

**G3** - All transaction lines with these tax rates:

- GST Free Income
- Your own tax rates with the tax type GST Free Sales.

**G4** - All transaction lines with these tax rates:

- Sales accounts with the tax rate Input Taxed
- Your own tax rates with the tax type Exempt Income when used with sales accounts.

**G9** - The value in G8 divided by 11. There may be a small rounding difference between this figure and actual GST on the GST Audit Report.

### GST amounts the Tax Office owes you from purchases

**G10** - All transaction lines with these tax rates:

- GST on Capital
- GST Free Capital
- GST on Capital Imports (the GST amount on the GST Audit Report multiplied by 11)

**G11** - All transaction lines with these tax rates:

- GST on Expenses
- GST Free Expenses
- Expense accounts with the tax rate Input Taxed
- GST on Imports (the GST amount on the GST Audit Report multiplied by 11)
- Your own tax rates with the tax types Purchases, GST Free Expenses and Exempt Income when used with expense accounts.

**G13** - All transaction lines with these tax rates:

- Expense accounts with the tax rate Input Taxed
- Your own tax rates with the tax type Exempt Income when used with expense accounts.

**G14** - All transaction lines with these tax rates:

- GST Free Expenses
- GST Free Capital
- Your own tax rates with tax type GST Free Expenses.

**G20** - The value in G19 divided by 11. There may be a small rounding difference between this figure and actual GST on the GST Audit Report.

## Some transaction types aren't included in this worksheet

The following transaction types are not included in the GST Calculation Worksheet:

- Transactions using the tax rate or tax type BAS Excluded.
- Transactions with the tax rate Input Taxed when used with asset, liability or equity account types.

## Manual adjustments flow through to the BAS

If you enter an amount in an editable field on the GST Calculation Worksheet, Xero automatically includes that amount in the total GST payment or refund shown on the BAS. However, Xero doesn't create a journal for the adjustment so there will be a difference to the GST Audit Report.

Make sure you process the transaction in Xero. Talk to your accountant or bookkeeper if you're not sure how to enter it.

## What's next?

Run the [Full BAS report](The-Full-Business-Activity-Statement.md).