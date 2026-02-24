# Understand a historical adjustment balance

Source: https://central.xero.com/s/article/Work-with-the-Historical-Adjustment-account

---

## Overview

- Learn how the historical adjustment account balances your figures and why your debit and credit might not match.
- Clear a historical adjustment account balance by updating your conversion balances, or enter a manual journal.

## How it works

The historical adjustment account is a system account Xero uses to balance transactions. You can't delete it, but you can use it in manual journals and make changes to it.

If the debit and credit totals in a transaction don't match, Xero enters the difference in the historical adjustment account. This occurs when:

- You save your conversion balances with debit and credit totals that don’t match
- Bills or invoices unpaid at conversion are entered in a foreign currency
- The account that holds the value of your inventory wasn’t specified when you imported your opening tracked inventory balances

## Conversion balances don't match

When the [conversion balances](Enter-conversion-balances.md) are saved with debit and credit totals that don’t match, a historical adjustment will be posted for the difference. In the conversion balances screen, adjust the account balances until debits equal credits and click **Save**.

When the conversion balances are saved with matching debit and credit balances, the historical adjustment is removed. If your conversion balances match and you still have a historical adjustment balance, this may relate to historical foreign currency transactions.

## Tracked inventory opening balance not selected

If you use tracked inventory, you [choose the account that holds the opening value of your inventory](Set-up-tracked-inventory.md#4Choosetheaccountthatholdstheopeningvalueofyourinventory) during the setup process. Check if the opening balance was parked in the historical adjustment account by running the [trial balance report](Trial-Balance-report-new-version.md). If it was, enter a [manual journal](Add-import-and-post-manual-journals.md) to move the balance to a more appropriate account.

## Historical transactions in a foreign currency

If you enter a bill or invoice in a foreign currency, Xero calculates any unrealised gains or losses that arise until the transaction is paid. For [transactions entered before your conversion date](Enter-unpaid-invoices-and-bills-for-your-conversion-balances.md), the unrealised gain or loss is included in your opening balances. This can lead to a situation where a balance is posted to the historical adjustment account to offset the revaluation of your accounts receivable and accounts payable accounts.

### Multicurrency transaction example

Let’s say your Xero organisation has a conversion date of 1 January 2020 when the exchange rate is 1.5500. You also have an unpaid foreign currency invoice for $1,000.00 dated 1 November 2019 when the exchange rate was 1.6000.

The unpaid invoice has a base currency value of $625.00 on 1 November 2019. On the conversion date of 1 January 2020 the base currency depreciated to 1.5500. The accounts receivable at year end (31 December 2019) would revalue to $645.16 and Xero will calculate an unrealised currency gain of $20.16.

This transaction would be recorded in your conversion balances like this:

- Accounts receivable 645.16 debit
- Sales 625.00 credit
- Adjustments 20.16 credit (total debits exceed total credits by 20.16)

The unrealised currency gain account doesn't display in the conversion balances screen and total debits will not equal total credits. However, 20.16 is posted to the unrealised currency gains account and included in your reports.

If you force your conversion balances to match, Xero will post an additional balance to the historical adjustment account to offset the unrealised gain. In this example, an unrealised gain of 20.16 would appear in the Profit and Loss report and an offsetting historical adjustment balance would appear in the Balance Sheet.

## What's next?

If you need to update your conversion balances to remove a historical adjustment balance, read our [tips for entering conversion balances](Tips-for-entering-conversion-balances.md).