# Account for uncleared, lost or expired cheques

Source: https://central.xero.com/s/article/Record-unpresented-cheques

---

## Overview

- Account for a cheque you’ve issued to a supplier that’s lost or expired.
- Move an uncleared cheque out of your bank account in Xero so the balance is more accurate.

## What you need to know

If the cheque is:

- **Lost** – remove the payment from the bill and reissue the cheque
- **Waiting to clear** – leave the bill as paid and use a suspense or clearing account to reflect the outstanding liability

Speak to your accountant or bookkeeper about the best option for your business, especially if the payment spans financial reporting periods.

We have a separate article on [undeposited customer invoice payments](Process-cheques-or-cash-before-being-banked.md).

If you're recording conversion balances, follow the process for [entering uncleared cheques when converting to Xero](/s/article/Enter-uncleared-cheques-when-converting-to-Xero?userregion=true).

## Remove a lost cheque payment from the bill and reissue the cheque

If you want your accounts payable to accurately reflect your liability for a bill, remove the existing cheque payment. When you reissue the cheque, record a new payment against the bill to reflect the new payment date.

1. [Add a note](View-history-and-notes-for-individual-transactions-and-inventory-items.md) to the bill to keep a record of what has happened, eg 'Paid by cheque #100 on 21 Mar 2023 but got lost in the mail'.
2. [Use remove and redo](Remove-payment-from-an-invoice-or-bill.md) to delete the existing cheque payment from the bill. This returns the bill to awaiting payment status and deletes the unreconciled payment transaction in the bank account.
3. When a new cheque is issued, record the new payment on the bill. This moves the bill back to paid status and creates a new unreconciled payment transaction in the bank account.

   If you want your general ledger to reflect the outstanding amount until the payment clears the bank account, use a suspense or clearing account as the **Paid From** account. Make sure you've [enabled payments](Enable-payments-to-an-account.md) to this account in the chart of accounts.
4. When the payment clears, reconcile the statement line against the payment transaction for your reissued cheque.

   If you've used a suspense or clearing account, create a spend money transaction coded to this account. This offsets the payment transaction, resulting in a nil balance on the account.

## Leave a bill about to clear as paid but account for the outstanding liability

If the cheque is received and is about to clear, but you want your balance sheet to accurately reflect the bank balance, offset the bank transactions while leaving the bill as paid.

1. [Add a note](View-history-and-notes-for-individual-transactions-and-inventory-items.md) to the bill to keep a record of what you're doing.
2. [Create a receive money transaction](Add-a-receive-money-transaction.md) using the same bank account the payment came out of, but coded to a suspense or clearing account.
3. Manually mark the original payment transaction and the receive money transaction as reconciled. These cancel each other out, removing the impact on the bank account.
4. When the payment clears, create a spend money transaction coded to the same suspense or clearing account. This balances out the suspense or clearing account.

Tip

Regularly run the [Account Transactions report](Account-Transactions-report-New.md) for the suspense or clearing account to monitor outstanding payments.

## What's next?

You're all done. You can continue [reconciling your bank account](Reconcile-your-bank-account.md).