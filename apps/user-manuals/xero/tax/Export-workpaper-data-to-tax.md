# Export workpaper data to tax (BETA)

Source: https://central.xero.com/s/article/Export-workpaper-data-to-tax

---

## Overview

- Once you’ve completed the workpaper pack for a client, export their data to Xero Tax to complete their tax returns.
- Clear workpaper data that’s imported incorrectly or into the wrong return.

Tip

The Workpapers and Xero Tax integration is currently in beta and is available to selected practices.

## What you need to know

Export data from Workpapers to Xero Tax, to automatically populate your client’s company tax return (CTR).

You can export a workpaper in any status to Xero Tax, but the tax return in Xero Tax needs to be in draft status.

When you export the data, Workpapers maps the data across each workpaper, the Adjusted Working Trial Balance and the Tax Reconciliation workpaper. It then populates the CTR with the resulting values. Xero Tax doesn’t do any calculations as part of the integration – the calculations are done in Workpapers, then the data is exported to Xero Tax.

If you make any changes to the workpapers, you need to re-export the data to Xero Tax to reflect these changes.

## Export to Xero Tax

Before you start, [create the client’s draft tax return](/s/article/Create-a-tax-return-in-Practice-Manager-AU) in Xero Tax. You need to do this before you can export the data from Workpapers.

To export data from Workpapers to Xero Tax:

1. On the **Workpapers** screen, click the client’s workpaper pack.
2. Click the export icon , then select **Export to tax**.
3. (Optional) Click **Review tax mapping** to review and [update the tax mapping](Edit-the-tax-mapping-for-Workpapers.md).
4. Click **Export to tax**.
5. Once the export’s complete, click **Close**, or click **Go to tax return** to view the return in Xero Tax.

## Resolve export issues

### No tax return found

This error indicates that there isn’t a tax return or the matching return isn’t in draft state for the client in Xero Tax yet. To export the data from Workpapers, you need to [create a draft tax return for the client](/s/article/Create-a-tax-return-in-Practice-Manager-AU) in Xero Tax first.

Once you’ve created the draft tax return in Xero Tax, return to the workpaper pack in Workpapers and export it.

### Incorrect permissions

You’ll receive this error if you don’t have the correct permissions to export data in Workpapers or edit the tax return in Xero Tax. Contact your practice administrator to grant you the correct permissions.

### Data does not meet field requirement

This error indicates that the data being sent from Workpapers to Xero Tax isn’t in the correct format. For example, Workpapers might be trying to send a negative amount to a field in Xero Tax that only accepts positive amounts.

To resolve this error, check all the data in the workpapers is correct.

## Clear workpaper data from a tax return

If data has synced incorrectly into a tax return, update the data in the workpaper, then re-export to Xero Tax. You don’t need to clear the workpaper first.

If you don’t want any workpaper data in the tax return at all, clear the workpaper data from Xero Tax:

1. Open the tax return in Xero Tax.
2. Click the options icon , then select **Clear data from workpapers**.
3. Click **Clear data** to confirm you want all the data imported from Workpapers removed.

## What's next?

Once the export is complete, view the return in Xero Tax.