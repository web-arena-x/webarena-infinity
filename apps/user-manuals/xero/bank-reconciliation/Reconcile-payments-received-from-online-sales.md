# Reconcile bulk payments received from online sales

Source: https://central.xero.com/s/article/Reconcile-payments-received-from-online-sales

---

## Overview

- If your online store directly integrates with Xero, reconcile the bulk payments in your bank account using a clearing account.

Warning

The following is one way to reconcile these transactions. We recommend you discuss this with your accountant or bookkeeper for the best method that suits your organisation.

Set up Xero clearing account

[Set up a separate current asset account](Add-or-edit-an-account-in-your-chart-of-accounts.md) for each type of bulk payment you receive, for example, Eftpos, Mastercard, Visa, American Express. Make sure you [enable payments to this account](Enable-payments-to-an-account.md).

When you apply a payment to an invoice, select the clearing account in the **Paid To** field. Then reconcile the bulk payment in your bank account and allocate it to the same clearing account. The payment into your bank account and payments applied to invoices will cancel each other out, leaving a balance of zero in the clearing account.

###

Set up your online sales system

If your online store or payments processor directly connects to Xero, edit the settings so when it marks your Xero invoices as paid, the payment shows in the clearing account.

For example, if you've created a current asset account called 'Mastercard Clearing Account', edit the settings in your online store or payments processor to apply invoice payments using this account.

Process merchant fees

Some payment processors deduct their fees from their payments to your bank account. If this applies, you should receive a regular statement from the payments processor showing the fees deducted.

To record the fees in Xero, [create a bank fees adjustment while reconciling](Reconcile-a-bank-statement-line-using-Find-Match.md) the statement line in your bank account.

Refund a customer

If you refund a customer for part or all of a sale:

1. [Create a sales credit note](Add-a-credit-note-to-a-customers-invoice.md) for the amount of the refund. Reference the original invoice number on the credit note.
2. Apply a payment to the credit note by entering a [cash refund](/s/article/Process-a-customer-or-supplier-refund?userregion=true) and select the clearing account as the payment account.

The total amount received should match the invoices less the credit note in your clearing account.

When reconciling, allocate the full amount of sales to your clearing account.

Reconcile your bank account

When the bulk receipt from your online store or payments processor appears in your bank account in Xero, from the **Create** tab, [create a new receive money transaction](Add-a-receive-money-transaction.md) and allocate it to your clearing account.

If your statement details are the same each time, you could set up a [bank rule](Create-a-bank-rule.md) to create the transaction for you.

### Check your clearing account balance

You should regularly check the transactions in your clearing account using the [Account Transactions report](Account-Transactions-report-New.md). Total payments applied to your invoices on a particular day should match the bulk receipt you allocated when reconciling. If the balance isn't zero, it could be due to either:

- Invoices you haven't received payment for yet
- Payment received in your bank account but the individual invoice payments haven't been downloaded by your online store or payments processor yet

## What's next?

You might find it easier to [export](Export-or-print-a-report.md) the Account Transactions report and reconcile it in a spreadsheet program such as Microsoft Excel.