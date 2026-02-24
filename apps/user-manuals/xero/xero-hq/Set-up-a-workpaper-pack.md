# Create a workpaper pack

Source: https://central.xero.com/s/article/Set-up-a-workpaper-pack

---

## Overview

- Create a workpaper pack for your client's organisation, based on the trial balance in Xero.

Tip

Workpapers is currently in beta and is available to selected practices. We’ve renamed our original solution classic Workpapers.

Generate a new workpaper pack

Workpapers (beta) Classic Workpapers

1. On the **Workpapers** screen, click **New workpaper pack**.
2. Select the **Client** the pack is for.
   If the client isn't showing in the list, check that the master administrator of your practice has the [advisor user role in the client's organisation](Manage-staff-assigned-to-clients-in-Xero-HQ.md).
3. Select the **Financial Year** to prepare the pack for. This defaults to the current financial year.
4. Set the **Reporting Period** as either a full financial year, a quarter or a custom period. New Workpapers sets the **Period Start Date** and **Period End Date** based on the period you select, but you can change these if you need to.
5. Set the **Due Date** for the pack.
6. Under **Preparer**, select the user who’s preparing the pack. This defaults to the current user.
7. Under **Reviewer**, select the user who will review the pack.
8. Under **Accounting Method**, select if the client’s accounts are prepared using accrual or cash basis accounting. New Workpapers autopopulates this based on your client’s Xero organisation settings, but you can change it here if you need to.
9. Click **Generate**.

### Add a pack

1. Select the **Workpaper Packs** tab, then click **New Workpaper Pack**.
2. Enter or select the details for the workpaper pack.
3. Select either:
   - **Xero report codes** to use the report codes from your client’s chart of accounts
   - **Workpapers report codes** to let classic Workpapers predict the report codes based on the names of your clients accounts
4. Click **Save**.

### Workpaper pack fields

| Field | Description |
| --- | --- |
| **Organisation** | If you've [synced classic Workpapers with Practice Manager](Set-up-your-practice-in-Workpapers.md), all your clients are in the list. Otherwise, you can manually add an organisation. |
| **End of Financial Year** | The end of financial year in classic Workpapers needs to be a month-end date. For example, if you're preparing workpapers for 5 April, choose 30 April for the end of the financial year. If you sync classic Workpapers with Practice Manager, make sure your client's balance date in Practice Manager matches classic Workpapers. For example, if your client's 'End of Financial Year' in classic Workpapers is in April, make sure the balance date in Practice Manager is April. To ensure classic Workpapers imports the correct 12-month period of your client's Xero data, check the financial year end in your client's Xero financial settings is set correctly to the exact day and month. If you want to use the bulk queries option, make sure you set a month-end date when creating the packs. |
| **First Day in Pack** and **Last Day in Pack** | If you're creating workpapers for annual accounts, choose the first day and last day of your client's financial year. To make creating workpapers for annual accounts easier, classic Workpapers defaults the dates to the first and last day of your client's financial year. If you want to create a workpaper pack for part of a period, change the dates to the period start and end dates. You can also remove any workpapers in the pack that you don’t need if you want to prepare a partial pack for an interim reporting period. We recommend creating a new workpaper pack for each reporting period rather than edit the dates of an existing workpaper pack. You can archive each of your periodic workpaper packs so you have a record of them. |
| **Job Start Date** and **Job Due Date** | These fields help your practice manage its workpapers and workflow. They help you prioritise work and help you keep track of all your clients' workpapers. You can set up [email notifications](Email-notifications.md) so your staff receive emails to let them know when a workpaper pack is due to start or is overdue. |
| **Assigned To**, **Managed By** and **Partner** | Assign workpapers to staff in your practice. If your practice is small, you might want the same person as partner and manager. If a staff member doesn't appear in the list, [add them to classic Workpapers](User-roles-in-Workpapers.md). |
| **Select a report code set** | Choose to [use the report codes](Report-codes-in-Workpapers.md) from your client’s Xero chart of accounts or let classic Workpapers set up the report codes based on your client’s account names. |

Enter a client's details

Workpapers (beta) Classic Workpapers

This process isn’t required for Workpapers as the client’s details sync through automatically from Practice Manager.

### How it works

- When you add a workpaper pack for a new client, you only need to enter the client’s organisation name and entity type. Add extra details after you create the client.
- Go into any workpaper pack for the client and update the client’s details. The new details apply to all packs for that client.
- If you [connect to Practice Manager](Set-up-your-practice-in-Workpapers.md) and sync at the client level, classic Workpapers copies the client’s address and entity type and the tax-related settings from Practice Manager into classic Workpapers.
- The changes you make to a synced client’s details in classic Workpapers aren’t copied back to Practice Manager. However, any changes to the client's organisation name, entity type, or address will be overwritten if you sync the client with Practice Manager again.

### Enter client details

1. Select the **Workpaper Packs** tab, then click the client’s name.
2. Select the **Settings** tab.
3. Enter or update the client’s details. At a minimum, you must enter the **Organisation Name** and **Email Address**.
4. Click **Save**.

Choose workpapers for a pack

Workpapers (beta) Classic Workpapers

This process isn’t required for Workpapers.

Workpapers generates a workpaper for each account code when you create a new workpaper pack. A workpaper is generated if the account has a balance in the current or previous reporting period, or there’s been movement in the account.

Each individual workpaper has its own status.

When you import your client's data from Xero, classic Workpapers includes the related workpaper in the pack if there's either:

- A balance for that workpaper's account at balance date
- Movement in that workpaper's account during the year

If an account doesn't have a balance or hasn't changed from the previous year, the related workpaper is displayed as 'greyed out'.

To view, add or remove workpapers in a pack:

1. Select the **Workpaper Packs** tab, then click your client's name.
2. Select or clear the checkbox next to a workpaper to add or remove it.

Set the materiality thresholds

Workpapers (beta) Classic Workpapers

This functionality isn’t available in Workpapers.

### How it works

The materiality setting for each workpaper in a pack defaults to the threshold set for the workpaper at the practice level. You can override the default setting when you set up the pack.

Classic Workpapers compares the balances imported from Xero with the materiality threshold and shows a reconciled icon  if the balance is within the threshold.

### Set the thresholds at practice level

1. Select the **Settings** tab, then under **Workpapers**, click **Materiality**.
2. Set or change the materiality thresholds for your practice. You can use a percentage or monetary value.
3. Click **Save**.

### Override the threshold on a workpaper

1. Open your client's workpaper, then click the yellow materiality icon.
2. Select an option from the menu.

## What's next?

If you’re using Workpapers, [add checklist items](/s/article/Create-a-checklist-for-a-workpaper?userregion=true) to your workpaper pack.

If you’re using classic Workpapers, create multiple workpaper packs using [bulk client queries](Using-queries-to-gather-information-from-clients.md).