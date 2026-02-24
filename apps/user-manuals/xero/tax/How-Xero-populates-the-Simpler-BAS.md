# How Xero populates the Activity Statement

Source: https://central.xero.com/s/article/How-Xero-populates-the-Simpler-BAS

---

## Overview

- The GST sections of the Activity Statement are prefilled using your transaction detail. You need to complete other sections manually.

Tip

The labels that display in your Activity Statement vary according to what information you need to report to the ATO. Your Activity Statement might contain only some of the labels listed below.

Goods and services tax

#### G1 – Total sales

The tax inclusive total of all transaction lines in the period using the following tax rates:

- GST on Income
- GST Free Exports
- GST Free Income
- Input Taxed (when used with sales accounts)
- Your own tax rates with the tax types Sales, GST Free Sales and Exempt Income

#### G2 – Export sales

The total of all transaction lines in the period using the tax rate GST Free Exports.

#### G3 – Other GST-free sales

The total of all transaction lines in the period using the following tax rates:

- GST Free Income
- Your own tax rates with the tax type GST Free Sales

#### G10 – Capital purchases

The tax inclusive total of all transaction lines in the period using the following tax rates:

- GST on Capital
- GST Free Capital
- GST on Capital Imports

#### G11 – Non-capital purchases

The tax inclusive total of all transaction lines in the period using the following tax rates:

- GST on Expenses
- GST Free Expenses
- GST on Imports
- Input Taxed (when used with expense accounts)
- Your own tax rates with the tax types Purchases, GST Free Expenses and Exempt Income (when used with expense accounts)

Select the **Transactions**tab to see a breakdown of the transactions that make up these totals.

PAYG tax withheld

### Automatic or manual updates

If you use payroll in Xero, you can set up your pay items to [automatically populate boxes](Add-a-custom-pay-item.md) W1 and W2 in your Activity Statement. You can manually overwrite the amounts populated by Xero to make any edits.

If you don’t use payroll in Xero, you can manually enter your PAYG tax withheld amounts.

### ATO PAYG withholding pre-fill

From July 2023, PAYG withholding labels W1 and W2 will be pre-filled in [ATO online services](https://www.ato.gov.au/Business/Single-Touch-Payroll/ATO-PAYG-withholding-pre-fill-for-activity-statements/) (ATO website) using the information reported through Single Touch Payroll (STP).

Currently, we’re working with the ATO to enable this integration so that we can make this data available in Xero. In the meantime, ensure that you verify your records before lodging the Activity Statements.

### Before lodging your Activity Statement

To ensure the details of your Activity Statements are up to date before you lodge it, you can:

- Check that pre-populated PAYG withholding amounts on your Activity Statement match the STP records displayed in ATO online services.
- Run the [Payroll Employee Summary report](Payroll-Employee-Summary-report.md) to reconcile payroll amounts to your Activity Statement for the period under review.
- Check that [pay items in boxes W1 and W2](Add-a-custom-pay-item.md) are set up correctly. You can edit current or previous returns in Payroll settings to ensure future payruns and Activity Statements are correct.
- Correct pre-populated PAYG withholding amounts at labels W1 and W2 if required, making sure to report total amounts.
- Enter PAYG withholding labels W3 and W4 if applicable.
- Check and enter in all remaining labels as needed.

### Why ATO PAYG withholding pre-fill may not match your STP records

- You didn’t lodge all your pay events through STP.
- You started reporting through STP part way through an Activity Statement period.
- An STP report you’ve lodged for the period has not been processed yet. Full file replacements are processed overnight.
- An STP report you lodged for the period wasn't able to be successfully processed.
- You’ve reported a retrospective correction in STP.
- You withheld an out of scope or voluntary payment in STP reporting such as reportable employer super contributions and Reportable fringe benefit amount.
- You might have processed a reimbursement as an allowance which has then been reported through STP.

Tip

Contact the ATO or your advisor if you're unsure what to include or exclude from W1. You can find more information on the ATO website about [completing the PAYG withholding labels](https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/business-activity-statements-bas/pay-as-you-go-payg-withholding).

PAYG income tax instalment

Xero pulls through PAYGI tax instalments if your Xero is connected to the ATO.

If your Xero organisation isn't connected to the ATO, you'll need to calculate your instalment details and enter them into this section manually. Use the [Profit and Loss](Profit-and-Loss-New.md) and [Account Transactions report](Account-Transactions-report-New.md) to help you work out your instalments.

Fringe benefits tax (FBT) instalment

This section isn’t populated by Xero. You’ll need to calculate your instalment details and enter them into this section manually.

Amounts you owe the ATO

| Label | Explanation |
| --- | --- |
| 1A – GST on sales | Includes the GST portion of all transactions that use a tax rate that has a Sales tax type, and any adjustments you’ve entered in the Activity Statement. Select the **Transactions**tab in the Activity Statement to see a breakdown of the transactions that make up this total. |
| 1C – Wine equalisation tax | This label isn’t populated by Xero. You’ll need to calculate the value and enter it into this label manually. |
| 1E – Luxury car tax | This label isn’t populated by Xero. You’ll need to calculate the value and enter it into this label manually. |
| 4 – PAYG tax withheld | The PAYG withholding total for the period. This value is copied down from W5. |
| 5A – PAYG income tax instalment | The PAYG income tax instalment for the period. This value is copied down from T7/T11. |
| 6A – FBT Instalment | The FBT instalment for the period. This value is copied down from F1. |
| 7C – Fuel tax credit over claim | This label isn’t populated by Xero. You’ll need to calculate the value and enter it into this label manually. |
| 8A – Total owed to the ATO | Sum total of taxes owed to the ATO for the period. This total is offset with the total in label 8B to work out your payment to, or refund from, the ATO. |

Amounts the ATO owes you

| Label | Explanation |
| --- | --- |
| 1B – GST on purchases | Includes the GST portion of all transactions that use a tax rate that has a Purchases tax type, and any adjustments you’ve entered in the Activity Statement. Select the **Transactions** tab in the Activity Statement to see a breakdown of the transactions that make up this total. |
| 1D – Wine equalisation tax refundable | This label isn’t populated by Xero. You’ll need to calculate the value and enter it into this label manually. |
| 1F – Luxury car tax refundable | This label isn’t populated by Xero. You’ll need to calculate the value and enter it into this label manually. |
| 5B – Credit from PAYG income tax instalment variation | This label isn’t populated by Xero. You’ll need to calculate the value and enter it into this label manually. |
| 6B – Credit from FBT instalment variation | This label isn’t populated by Xero. You’ll need to calculate the value and enter it into this label manually. |
| 7D – Fuel tax credit | This label isn’t populated by Xero. You’ll need to calculate the value and enter it into this label manually. |
| 8B – Total owed by the ATO | Total GST credits for the period. This total is offset with the total in label 8A to work out your payment to, or refund from, the ATO. |

Payment / Refund

Section 9 on the Activity Statement shows the amount you pay to, or receive from, the ATO.

## What's next?

Once you’ve checked your Activity Statement, you can [lodge it with the ATO](The-Simpler-Business-Activity-Statement.md#LodgeyouractivitystatementwiththeATO).