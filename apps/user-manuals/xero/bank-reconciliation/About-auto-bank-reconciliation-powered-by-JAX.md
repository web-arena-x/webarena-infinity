# About automatic bank reconciliation powered by JAX (BETA)

Source: https://central.xero.com/s/article/About-auto-bank-reconciliation-powered-by-JAX

---

## Overview

- Understand how automatic (auto) bank reconciliation powered by JAX works in Xero.

Tip

Automatic bank reconciliation is currently in an open beta. We're making enhancements and improvements over the coming months.

## What you need to know

### About automatic bank reconciliation

Automatic (auto) bank reconciliation in Xero is a feature that uses AI to automatically categorise and match bank statement lines. It’s powered by our new AI financial superagent, Just Ask Xero (JAX) and looks at the data in the statement line, then reconciles it against an account transaction.

When a statement line imports into your bank account in Xero, JAX aims to reconcile it against an existing transaction using a find and match, or creates a new transaction using a bank rule, memory or prediction. Auto bank reconciliation only reviews statement lines imported after you turn it on, it doesn't reconcile statement lines that were already in Xero.

To ensure a high level of accuracy, JAX only automatically reconciles a transaction if there’s high confidence in the suggestion. If JAX doesn’t have enough confidence to reconcile the suggestion, it still suggests a match or categorisation, but leaves the bank statement line for you to review and [reconcile manually](Reconcile-your-bank-account.md).

Auto bank reconciliation is available to organisations on the Xero Grow (Australia, New Zealand and UK), Growing (US), and Standard (Global) plans and above.

### Feature improvements

Auto bank reconciliation in Xero is currently available to selected organisations. We're rolling it out to all users gradually over the coming months as part of an open beta.

While the feature's being rolled out, we’re fine tuning how it works. Upcoming improvements include:

- In-line editing – Change account code and tax rate on the **Reconciled transactions** screen
- Filter by reconciliation method – Filter transactions reconciled by each automatic method, those reconciled manually or all transactions
- Source documents – View or add source documents directly on the **Reconciled transactions** screen

## How it works

### Apply a bank rule

First, JAX reviews the bank rules in your organisation to see if it can apply any with high confidence. If the bank statement line matches the conditions of a rule, JAX applies the rule and creates a new account transaction to reconcile the statement line.

### Match to an existing transaction

If there are no applicable bank rules, JAX then compares the details in the bank statement line with existing Xero transactions such as bills, invoices and payments to see if there’s a match.

If there’s high confidence in a match with a:

- Cash payment transaction, such as a spend or receive money transaction – JAX reconciles the statement line
- Existing payment transaction on a bill or invoice – JAX reconciles the statement line
- Invoice or bill that has no payment applied – JAX creates a payment and applies it to the bill or invoice, then reconciles the statement line to the payment

If JAX can’t find a direct match, it checks your past reconciliations to see if similar statement lines were matched to an invoice or bill. If JAX is confident the statement line should be matched to one, but the invoice or bill isn’t in Xero yet, JAX leaves the statement line unreconciled for now.

When the invoice or bill arrives in Xero, JAX rechecks for a high confidence match and reconciles the transaction if it finds one.

### Create a transaction using memory

If there are no high-confidence matches, JAX compares the details of the statement line with up to 5,000 transactions you’ve previously reconciled to identify any patterns.

If there’s a strong pattern with high confidence, JAX follows the pattern and reconciles the statement line.

### Create a transaction using prediction

If JAX can’t apply a high-confidence memorisation, it compares the details of your statement lines to how other Xero users have previously reconciled similar transactions. It uses machine learning algorithms to make a prediction based on the details in the statement line.

If there’s a pattern with high confidence, JAX reconciles the statement line in the same way.

## Improve the automation outcomes

JAX learns from how you use it, gradually automating more as its confidence grows. As it gets smarter, it becomes more accurate and the more it can reconcile for you over time.

To help improve the performance of auto-reconciliation, you can:

- Build a good reconciliation history – The more you reconcile, the more our system learns your patterns
- Keep your contacts and chart of accounts up to date – This helps our system make more accurate suggestions
- Set up bank rules for recurring transactions – bank rules are a powerful way to automate reconciliation

If you see an inaccurate auto-reconciliation, the best thing to do is to correct it. When you make a correction, JAX learns from it and is less likely to make the same mistake in the future.

## What's next?

Now you know how it works, [turn auto bank reconciliation on](How-to-use-automatic-bank-reconciliation.md) and view the transactions reconciled by JAX.