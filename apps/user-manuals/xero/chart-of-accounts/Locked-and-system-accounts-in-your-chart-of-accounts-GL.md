# Locked and system accounts in your chart of accounts

Source: https://central.xero.com/s/article/Locked-and-system-accounts-in-your-chart-of-accounts-GL

---

## Overview

- Learn how to use locked accounts and system accounts in Xero.
- Understand what the Tracking Transfers account is and when Xero uses it.
- Record movements in system accounts by adding a secondary account or using manual journals.

Locked accounts

If an account is locked in your organisation’s chart of accounts, then it has a specific purpose. Most locked accounts are system accounts, but Xero does lock other accounts if they’ve been used for the following purposes:

- Repeating invoice
- Bank rule that you’ve set up
- Tracked inventory
- Registered fixed asset
- Payment account for a Payment Service

Locked accounts can’t be deleted or archived, but you can [edit them](Add-or-edit-an-account-in-your-chart-of-accounts.md). You need the standard or advisor user role to do this.

You can identify locked accounts by the padlock icon next to the account code. Hover over the padlock icon to see the reason the account is locked.

You can use locked accounts in transactions and manual journals if it’s not a system account.

System accounts

System accounts are set by Xero. They're used for specific reporting or accounting purposes. You won't see all these accounts on your chart of accounts as some are used on reports or in the background by Xero. Also, some accounts only apply if you use multicurrency in Xero.

Xero automatically creates default system accounts for specific reporting or accounting purposes. They'll always balance, and equal the sum of the approved invoices, bills or wages payable.

Xero allows you to enter transactions or manual journals to some system accounts. System accounts can't be unlocked, deleted or archived.

| System account | Allows transactions or manual journals |
| --- | --- |
| Accounts Payable | No\* |
| Accounts Receivable | No\* |
| Bank Revaluation | No |
| Current Earnings | No |
| Historical Adjustments | Yes |
| Realised Currency Gains | Yes |
| Retained Earnings | Yes |
| Rounding | Yes |
| Sales Tax | Yes |
| Tracking Transfers | No |
| Unpaid Expense Claims | No |
| Unrealised Currency Gains | No |

\* You can record movements in a system account in another way, even if Xero doesn't allow you to enter transactions or manual journals to the account.

Tracking Transfers account

The Tracking Transfers account is a system account in your chart of accounts. Xero uses it to make sure the Balance Sheet balances when you filter it by tracking category.

Xero creates journals in the Tracking Transfers account when you create a transaction or journal that affects a tracking category's balance, but you don't change the source transaction. This might happen when you:

- Create a journal to transfer part of the balance from one account to another, but you don't change the coding of the underlying bills.
- Create a credit note for an invoice or bill with a tracking category.

The amount in the Tracking Transfers account on the Balance Sheet for one tracking option is offset by the amounts in that account for the other tracking options.

As the account is a system account, you can't archive or delete it. You also can't use it in transactions or manual journals. You can change its name and account code, but this won't change how Xero uses the account. Although you can change its account type, we don't recommend doing this.

Tip

To change where the account appears on a report, [edit the layout](Edit-layout-of-a-new-financial-report.md) of the report.

Record movements in system accounts

Tip

Before you make any changes, we suggest you speak to your accountant for any taxation or reporting implications.

Add a secondary account for each system account that you want to journal to. You can then add the manual journals and customise the Balance Sheet layout.

You need the advisor user role to add accounts to the chart of accounts.

1. [Add an account to your client's chart of accounts](Add-or-edit-an-account-in-your-chart-of-accounts.md) for each system account you want to journal to. Use the same account type as the system account. For example:

   - Add a current asset account for accounts receivable.
   - Add current liability accounts for accounts payable and wages payable.
2. Give the new account a name relating to the system account that's unique in the chart of accounts.
3. [Add a manual journal](Add-import-and-post-manual-journals.md) and any relevant reversals, to show the accruals required for the system accounts.
4. Create a custom layout to [group system and secondary accounts](Customise-the-Balance-Sheet-layout-for-system-and-secondary-accounts.md) on the Balance Sheet.

## What's next?

If the pricing plan includes multicurrency, find out more about [foreign currency accounts in the chart of accounts](Foreign-currency-accounts-in-the-chart-of-accounts.md).