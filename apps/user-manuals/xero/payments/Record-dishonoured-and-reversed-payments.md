# Record dishonoured and reversed payments

Source: https://central.xero.com/s/article/Record-dishonoured-and-reversed-payments

---

## Overview

- Record a payment that's bounced or been dishonoured by the bank.
- Remove the payment from an individual invoice or bill, or take the payment out of a batch deposit or batch payment.

## Account for the payment

When a customer's payment bounces or is dishonoured, or a supplier payment you made is reversed, remove the payment from the invoice or bill to reset it to an awaiting payment status. If the invoice or bill is included in a batch deposit or batch payment, you'll need to edit the batch first and then remove the invoice or bill.

### Single payment on an individual invoice or bill

If the dishonoured payment is recorded on a single invoice or bill, remove it, then reconcile the bank statement lines for the original payment and reversal:

1. Find and delete the original payment [from your bank account](Delete-an-account-transaction.md) or [from the invoice or bill](Remove-payment-from-an-invoice-or-bill.md).
2. Reconcile the statement line for the original payment with a [receive money](Add-a-receive-money-transaction.md) or [spend money](Add-a-spend-money-transaction.md) transaction. Allocate the transaction to a dishonoured or reversed payments account, or [create a new account](Add-or-edit-an-account-in-your-chart-of-accounts.md).
3. For the payment reversal, reconcile the statement line with a spend or receive money transaction, using the same account as above. The two transactions will offset against each other.
4. (Optional) Add a note to the invoice or bill to record why the payment was deleted.

When the replacement payment is made, [reconcile it with the unpaid invoice or bill](Reconcile-a-bank-statement-line-using-Find-Match.md).

You can run the [Account Transactions report](Account-Transactions-report-New.md) for your dishonoured or reversed payment account to check the balance of the account is zero.

### Payment is part of a batch

If the payment is recorded as part of a batch deposit or a batch payment, remove it from the batch, then reconcile the bank statement lines for the original payment and reversal:

1. Find and [unreconcile the batch deposit or batch payment](Unreconcile-an-account-transaction.md).
2. Edit the [batch deposit](Edit-a-batch-deposit.md) or [batch payment](Edit-batch-payments.md) to remove the invoice or bill from the batch, then click **Save**. This updates the batch with a new total and the invoice or bill returns to awaiting payment.
3. Create a receive or spend money transaction for the original payment. Allocate the amount to a dishonoured or reversed payments account, or [create a new account](Add-or-edit-an-account-in-your-chart-of-accounts.md).
4. [Use find & match](Reconcile-a-bank-statement-line-using-Find-Match.md) to reconcile the original payment in your bank account with both the revised batch deposit or batch payment and receive or spend money transaction created above.
5. Reconcile the statement line for the reversed payment with a spend or receive money transaction, using the same account as above. The two transactions will offset against each other.
6. (Optional) Add a note to the invoice or bill to record why the payment was deleted.

When the replacement payment is made, [reconcile it with the unpaid invoice or bill](Reconcile-a-bank-statement-line-using-Find-Match.md).

You can run the [Account Transactions report](Account-Transactions-report-New.md) for your dishonoured or reversed payment account to check the balance of the account is zero.

## Charge the customer for bank fees incurred

In some instances, you might want to charge your customer for bank fees related to the dishonoured or bounced payment. One way you can do this is to create spend and receive money transactions:

1. When the bank charge appears on your bank statement, create a spend money transaction and allocate it to an account such as Bank Fees.
2. Let your customer know that they owe you money for the bank charges incurred.
3. When you receive the customer payment, create a receive money transaction and allocate it to the same bank fees account.

## What's next?

If your customer doesn't repay the dishonoured payment, you might need to raise a credit note to [write the debt off](Record-a-bad-debt-in-Xero.md).