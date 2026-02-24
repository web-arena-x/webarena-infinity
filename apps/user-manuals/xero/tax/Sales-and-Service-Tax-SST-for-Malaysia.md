# Sales and Service Tax (SST) for Malaysia

Source: https://central.xero.com/s/article/Sales-and-Service-Tax-SST-for-Malaysia

---

## Overview

- Use the account transactions report to collect data for your SST Return.
- Record a SST payment that is delayed, in part or full, after 12 months from the date of the invoice.

Collect data for your SST return

Before you start

1. Check you’ve [set up the sales and service tax rates](Add-or-edit-tax-rates-GL.md) in your organisation to match the product and service requirements set by the [Royal Malaysian Customs Department (RMCD)](http://www.customs.gov.my/en) for SST.
2. Apply your tax rates to the relevant accounts within your organisation’s [chart of accounts](Add-or-edit-an-account-in-your-chart-of-accounts.md).

Use the account transactions report to view your transactions

To gather the data you need to complete your SST return:

1. Run the [Account Transactions report](Account-Transactions-report-New.md) on an accruals basis and group your results by Tax Rate Name. Sales taxes are generally calculated on an accruals basis.

1. Run the [Account Transactions report](Account-Transactions-report-New.md) again but on a cash basis, grouping your results by Tax Rate Name. Service taxes are generally calculated on a cash basis.

Tip

You could [create reusable custom report layouts](Create-reusable-custom-report-layouts.md) to group and filter the transactions that are relevant for each report.

Adjust a SST Tax filing for service tax invoices paid after 12 months

Tip

We recommend you check with your advisor if you're unsure of the reporting or tax implications of adjusting SST tax filing.

When a service tax invoice is raised within Xero (eg 30 Sep 2018), there is no impact on SST reporting while the payment remains unpaid to the RMCD.

If a payment for service tax isn’t made, in part or full, at the time the invoice is created, you will need to make the payment a day after 12 months (eg 1 Oct 2019).

If a customer pays you after 12 months (eg 31 Jan 2020) and you have already paid RMCD, you will need to adjust your records to avoid paying RMCD again for this transaction.

To adjust a SST Tax filing for service tax invoices paid after 12 months in Xero:

1. Locate the unpaid invoice using the [Aged Receivables Detail report](Aged-Receivables-Detail-report-New.md) to filter out invoices unpaid after 12 months. These entries will appear in Xero as Accounts Receivable Debit, Sales Credit, and Service Tax Payable Credit.
2. Report the Service Tax Payable for the SST on accrual basis to the RMCD a day after 12 months. You do not need to create an entry in Xero for this.
3. Make the relevant payment for Service Tax to the RMCD.
4. Should the customer pay the invoice after 12 months and after you have paid service tax to RMCD for that invoice, [mark this invoice as paid](Record-payment-of-a-sales-invoice.md#Web) in Xero. These will show in Xero as Bank Debit and Accounts Receivable Credit.
5. Run an [Account Transactions report](Account-Transactions-report-New.md) on a cash basis. This will include the transaction with Service Tax reported earlier.
6. Reduce the SST payable amount in the Account Transactions report by [posting a manual journal](/s/article/Add-or-edit-a-single-manual-journal-US-GL) on the date of the payment in step 4, as this amount has already been reported to RMCD. This image shows an example of the manual journal with SST reduction.

## What's next?

Find out more about [adding tax rates to your organisation](Add-or-edit-tax-rates-GL.md).