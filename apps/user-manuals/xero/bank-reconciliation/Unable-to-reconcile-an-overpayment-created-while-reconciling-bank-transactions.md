# Unable to reconcile an overpayment created while reconciling bank transactions

Source: https://central.xero.com/s/article/Unable-to-reconcile-an-overpayment-created-while-reconciling-bank-transactions

---

## Overview

- Identify and work around a known issue with reconciling overpayments you create while reconciling your bank account.

## Scenario

In some instances, you receive an error when you try to reconcile an overpayment that you create while reconciling your bank account. The error message says that overpayments can’t have tax even though the overpayment doesn’t have tax on it, and reconciliation fails.

The error reads in full: "An error occurred for the following reason: Overpayments cannot have tax."

## Steps to reproduce

Tip

This is an intermittent issue and doesn’t affect every overpayment created using this method

1. [Record an overpayment](Record-an-overpayment.md) during bank reconciliation. An overpayment created while reconciling a bank account won’t have tax on it by default.
2. Click **Reconcile**.

Xero generates an error, and the overpayment can’t be reconciled.

## How to resolve the issue

To resolve the issue, [create the overpayment](Record-an-overpayment.md#CreateanoverpaymentfromanywhereinXero) outside of the reconciliation process, then reconcile it using [find and match](Reconcile-a-bank-statement-line-using-Find-Match.md).

## What's next?

If you need further help, contact Xero support.