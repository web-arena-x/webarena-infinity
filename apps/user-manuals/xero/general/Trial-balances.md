# Trial balances in Workpapers

Source: https://central.xero.com/s/article/Trial-balances

---

## Overview

- Workpapers uses data from your client’s Xero organisation to show the closing balance of the previous and current reporting periods.

Tip

Workpapers is currently in beta and is available to selected practices. We’ve renamed our original solution classic Workpapers.

## About trial balances

Workpapers (beta) Classic Workpapers

When you create a new workpaper pack for your client, Workpapers creates the Working trial balance.

The Working trial balance shows all account balances pulled from the chart of accounts in the client’s Xero organisation and is the starting point for workpapers preparation or review.

| **Column** | **Description** |
| --- | --- |
| Account name | The name of the account in the client’s chart of accounts in their Xero organisation. |
| Report code | The report code used to map the account in the client’s Xero organisation to the workpapers in a workpaper pack. |
| LY balance (Last year) | The balance of the accounts in the workpaper up to the period end date of the pack for the last reporting period. |
| CY balance (Current year) | The balance of the accounts in the workpaper up to the period end date of the pack for the current reporting period. |
| Variance | The percentage difference between the values in the **CY balance** and **LY balance** columns. |
| Adjustments | The total of any adjustments made using manual journals. |
| Adjusted balance | The CY balance plus any adjustments made. |
| Status | The status of the workpaper associated with the account. |
| Assignee | The preparer of the workpaper associated with the account. |

From the Working trial balance, you can add documents and notes to accounts, post adjustment journals and recode balances as needed. Once you’ve finalised the journals, you can post them back to the client’s Xero organisation.

You can filter the accounts on the Working trial balance by status. You can also select a different accounts view using the dropdown menu above the **Account name** column.

When you [import your client’s Xero data](Connect-Workpapers-to-Xero.md), classic Workpapers generates a trial balance based on the balances in your client’s Xero accounts. Use the trial balance to check the state of the accounts for the period covered by the workpapers pack.

Classic Workpapers also uses the imported data, together with the report code mappings you’ve set up, to determine which workpapers to include in a pack. If an account has a balance at the end of the reporting period, or if the balance has changed during the period, classic Workpapers creates a workpaper for the account.

When classic Workpapers creates a workpaper, it populates the values as follows:

- **Prior Period Balance** – Balance of the mapped account for the same period in the previous year, if there is one
- **Balance in Xero** – Balance of the mapped account for the period covered by the workpaper

The Xero balance shows you the target for reconciliation, while the two figures together show the movement in the account period-on-period.

Some workpapers aren’t mapped to an account, so not every workpaper in the pack uses imported Xero data.

## Review and reconcile the trial balance

Workpapers (beta) Classic Workpapers

To review the Working trial balance for a client:

1. On the **Workpapers** screen, click the client’s workpaper pack.
2. Select the **Working trial balance** tab.
3. (Optional) Filter the accounts by status and select an **Accounts view**.
4. For each account type, click the expand icon  to view the accounts and their balances.

For each account on the Working trial balance screen, you can:

- [Create a manual journal](Journals-in-Workpapers.md) to make an adjustment.
- Click the attachment icon  to attach a supporting document to verify the balances. You can also [attach documents to a workpaper](Attach-manage-supporting-documents-information.md).
- Click the notes icon  to add a note.
- Click the view workpapers icon  to go to the related workpaper.
- Click the Xero icon  to view the related transaction report in Xero.

### Review the data

When you click **Edit Trial Balance** after you [import your client's Xero data](Connect-Workpapers-to-Xero.md), classic Workpapers displays the prior period and current period balances for each account. In addition to the balances, you can also review and update the [report code mappings](Report-codes-in-Workpapers.md).

Tip

If a balance appears to be incorrect, we recommend that you update the values in Xero and import data from your client's Xero account again.

### Reconcile the balances

Collect and tally the information from your client’s financial statements and use it to reconcile the account balances.

1. Select the **Workpaper Packs** tab, then click your client's name.
2. For each workpaper with Xero data in it, click the workpaper name.
3. Select the **Workpaper** tab, then enter the balance from your client’s financial statements in the **Supporting Balance** field on each line. When your supporting balance matches the Xero balance to within the materiality threshold, the reconciled icon changes to yellow.
4. After you’ve reconciled the line, click the complete icon .

When you’ve reconciled and marked all of the lines in the workpaper as complete, the status of the workpaper changes to **Completed**.

## What's next?

Once you’ve reviewed the Working trial balance and posted any adjustments, change the status of the workpaper.