# Common issues for find and recode

Source: https://central.xero.com/s/article/Troubleshooting-for-Find-Recode

---

## Overview

- Fix problems with transaction lines, contacts or accounts that haven’t displayed.
- What to do if recoding hasn’t worked as intended.

Tip

If you can’t access find and recode, [check your user role](Change-a-user-s-role-or-permissions.md). You need the advisor user role to use find and recode.

Transaction line, contact or account doesn't show

### Transaction lines aren't displayed

- Transaction lines created prior to a [lock date](Set-up-and-work-with-lock-dates.md) won't display in the search results unless the lock date was set for all user roles except advisors. Check the transaction line you're searching for isn't subject to a lock date.
- Search results show both the transaction total and the line total, but the search query is on the transaction total only. Check your search query is for the transaction total, not the line total.
- Xero displays the original transaction total in the search results, even if part payments or credits have been applied. Check your search query is for the original transaction total.

### Contact isn't listed as a search option

You can’t search for archived contacts, so they won’t display as a search option. Check the contact you're searching for is an active contact. If the contact has been archived in error, [restore it](Archive-or-restore-contacts.md).

### Account isn't listed as an option to recode

The following account types can't be edited and are excluded from find and recode:

- Accounts receivable
- Accounts payable
- Unpaid expense claims
- Tracking transfers
- Bank revaluations
- Unrealised currency gains
- Bank accounts
- Fixed assets
- Tracked inventory (account type = inventory)

You can’t search for or recode purchase transaction lines, such as bills, supplier credit notes and spend money transactions, which contain tracked inventory (where the account type is inventory).

Transaction lines on sales transactions, such as invoices, sales credit notes and receive money transactions, which contain tracked inventory will show in search results if they match other search conditions.

Recoding didn't affect everything

### The contact on an expense claim or receipt wasn't recoded

You can’t recode the contact on an expense claim or expense claim receipt. If a group of transaction lines include expense claims, the expense claim lines will be excluded from the contact recode. The accounts, tax rates and tracking options will be recoded normally.

### An associated transaction wasn't recoded

When you recode a transaction, such as an invoice or bill, any associated transactions, such as a credit note, prepayment allocation or overpayment aren't automatically recoded and must be recoded separately. Only the transaction lines you select will be recoded, so we recommend you include search conditions for the associated transactions in your query.

When you recode transaction lines on a repeating invoice or bill, the template won’t be affected by the recode. Edit the template directly if you want to update future invoices and bills.

### Only part of a transaction was recoded

Find and recode changes the individual transaction lines, not the entire transaction. To recode an entire transaction, check you've selected each of the transaction lines in the search results, or edit the transaction manually.

Recoding hasn't worked properly

### Recoding results in an error

If you get an error on any transaction line, none of the transaction lines in that transaction will be recoded. We recommend you manually edit the transaction.

### Recoding activity isn't listed in the transaction’s History & Notes

If an error has prevented the transaction being recoded, the recoding activity won't be listed in the transaction's History & Notes. Check the [Recode Summary](View-transaction-information-and-recoding-history.md) to view the recoding details, including the transactions that had errors.

### Reverse the recoding

Once you’ve recoded a transaction line, it can’t be undone. To reverse the changes, recode the transaction line again or edit the individual transaction.

## What's next?

If you're still having problems, check your [transactions are supported or investigate your transaction lines](About-Find-Recode.md).