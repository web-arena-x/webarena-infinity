# Can't apply a supplier credit

Source: https://central.xero.com/s/article/Can-t-allocate-a-supplier-credit-note

---

## Overview

- If the option to allocate credit isn’t showing and you can’t apply a credit to a bill, check these things.

## What you need to know

Suppliers can have credit transactions that are overpayments, prepayments, or credit notes:

- Overpayments occur when you [pay more than you owe](Record-an-overpayment.md).
- Prepayments are [payments made in advance](Record-a-prepayment.md) of an invoice being raised.
- Credit notes [reduce the amount](Add-a-credit-note-to-a-bill.md) you owe, and are often used when you return goods or the sale doesn’t go through.

When you apply a credit to a bill, Xero uses the most recent date from the bill or credit as the date to apply the credit.

If you can’t see the option to apply the credit, it might be because:

- You’re trying to apply the credit while reconciling the bank account
- The credit is raised against the wrong supplier, or that supplier doesn’t have a bill that’s in awaiting payment status
- The credit and bill are in different currencies
- The credit is in a locked period

## You're trying to apply a credit while reconciling

You can’t select credits when using find & match during bank reconciliation. You first need to [apply the credit to the bill](Apply-a-supplier-s-credit-to-a-bill.md), or [record a cash refund on the credit](/s/article/Process-a-customer-or-supplier-refund?userregion=true).

Once you’ve applied or refunded the credit, you can then reconcile any outstanding balance on the bill to the relevant statement line.

## The credit is raised against the wrong contact

If you can’t see the option to apply the credit, it might be because there are duplicate contact records, or the credit is for a supplier who doesn’t have any bills in awaiting payment status.

Check that the contact name is identical on both the credit and the bill. Xero treats even small differences as two separate contacts. If there are duplicate contact records, you need to [merge the two contacts](Merge-contacts.md).

If the supplier is correct, check that they have a bill that’s awaiting payment – a bill that’s approved but not paid and shows on the **Awaiting Payment** tab in the **Bills** screen. A supplier credit can only be applied to a purchase bill.

## The bill and credit are in different currencies

Tip

Check with your accountant or bookkeeper for advice on the best way to manage credits in different currencies.

If the organisation is set up for multi-currency, check that the currency of the credit and the bill are the same.

If the currencies are different and the bill and credit are both in the same tax period, void one of them and re-enter it in the same currency as the other transaction.

Alternatively, you could apply the credit to the bill using a suspense-type account:

1. [Enable payments](Enable-payments-to-an-account.md) to the account you want to apply the credit to.
2. [Record a refund on the credit](/s/article/Process-a-customer-or-supplier-refund?userregion=true) and select the suspense account as the **Paid To** account.
3. [Record payment on the bill](Record-payment-of-a-bill.md) from the same payment account you selected above.

Make sure that you use the same payment date on the bill and the credit, and that you enter the correct exchange rate. This ensures no balance remains in the suspense account.

## The credit is in a locked period

Lock dates stop changes being made to transactions during a past period. They can be set to either stop all users making changes, or all users except advisors.

If a [lock date is set](https://xero.lightning.force.com/s/article/Set-up-and-work-with-lock-dates?userregion=true) for the period the credit is in, you might not be able to apply the credit, depending on your user role and the date the accounts are locked at.

If a lock date is for all users including advisors, an advisor needs to temporarily remove the lock date, apply the credit, then set the lock date again.

If a lock date is for all users except advisors, advisors can apply a credit:

- Within the locked period to a bill dated after the lock date
- Dated after the lock date to a bill dated within the locked period
- To a bill if both the bill and credit are dated within the locked period

All other users can only apply a credit to a bill within a locked period if either the bill or credit is dated after the lock date.

## What's next?

If you still can’t apply a credit, contact Xero support. Provide us with as much detail as you can on the issue, including any screenshots.