# Import data from Xero into Workpapers

Source: https://central.xero.com/s/article/Connect-Workpapers-to-Xero

---

## Overview

- Connect your client’s Xero organisation to populate the trial balance in Workpapers. Refresh the data if anything changes in Xero.
- Resolve any issues with connecting Workpapers to Xero.

Tip

Workpapers is currently in beta and is available to selected practices. We’ve renamed our original solution classic Workpapers.

About importing Xero data

Workpapers (beta) Classic Workpapers

When you add a new client and their Xero organisation to your practice, you can then create a new workpaper for that client.

The client’s data automatically syncs to Workpapers from their Xero organisation, but you can [refresh it manually](Refresh-a-workpaper-pack.md) if you make changes in Xero.

- Connect a workpapers pack to your client’s Xero organisation and import their financial data to populate the trial balances in classic Workpapers.
- Refresh the data if something changes in Xero, such as updates to financial details or changes to report codes.
- Disconnect from the current Xero organisation and reconnect to a new organisation to change the data that a workpapers pack uses.
- You need [access to the client’s Xero organisation](Manage-access-to-your-practice-s-organisations.md) to connect to it, and access to reports to import the data.

Import data from Xero

Workpapers (beta) Classic Workpapers

This process doesn’t apply to Workpapers as the client’s data automatically syncs from their Xero organisation.

### Connect to Xero and import data

1. Select the **Workpaper Packs** tab, then click your client's name.
2. Select the **Import** tab, then click **Import from Xero**.
3. If no other packs for this client are connected to Xero, select your client's organisation from the list, then click **Import**.
4. When the import finishes, click either:
   - **Edit Trial Balance** to [review and update the trial balance figures](Trial-balances.md) imported from Xero
   - **Go to Workpapers** to continue working on your client's workpapers

### Refresh Xero data

1. Select the **Workpaper Packs** tab, then click your client's name.
2. Select the **Import** tab, then click **Refresh from Xero**.
3. When the import finishes, click either:
   - **Edit Trial Balance** to [review and update the trial balance figures](Trial-balances.md) imported from Xero
   - **Go to Workpapers** to continue working on your client's workpapers

When you refresh Xero data, changes made in Xero such as an update to financial details or a change to report codes are reflected in classic Workpapers. Changes to an account name in Xero are also updated in the trial balance and the related workpaper.

Refreshing Xero data doesn't automatically update any account group names that classic Workpapers created. You need to double click on the account group name and enter the new name manually.

Fix errors in data imported from Xero

Workpapers (beta) Classic Workpapers

This functionality doesn’t apply to Workpapers.

To fix an error in the Xero data imported into a workpaper:

1. Click the Xero link icon on the workpaper line that contains the incorrect data.
2. Review the information in the related report in Xero and resolve the error.
3. Import your client’s data into classic Workpapers again to update the workpaper line.

Remove or change the connection to Xero

Workpapers (beta) Classic Workpapers

This functionality doesn’t apply to Workpapers.

### How it works

If you disconnect your classic Workpapers client from a Xero organisation:

- The connection is removed for all workpaper packs for that client.
- Any data, supporting documents or queries on the workpapers will remain unchanged until you connect to another Xero organisation and import data from the new organisation.
- The link to Xero found on most workpapers in the pack won't work until you reconnect your workpaper pack and import the data again.

If you change the Xero organisation that your classic Workpapers client is connected to:

- Any previous supporting documents or queries remain, but they won’t be attached to any particular line on that workpaper.
- When you connect to the new organisation, you'll see a note about the change on the **Import** tab. The note shows in any workpaper packs for the client that are still using data from the previous organisation.
- After you import the data from the new organisation, the workpapers are rebuilt using the new data. Any supporting documents and queries previously attached to a specific line in the workpaper won’t be attached to that line, but they are retained on the workpaper.
- Any supporting balances manually entered on a workpaper are removed when you import the new data. In addition, any account codes added as lines on a [custom workpaper](Custom-workpapers.md) become labels (known as non-Xero lines) and the data is fixed and can’t be updated.

Tip

You can only connect your classic Workpapers client to one Xero organisation. If a Xero organisation changes, for example due to sale or merger, set up a new classic Workpapers client rather than continuing to use the original one.

### Delete the connection

1. Select the **Workpaper Packs** tab, then click your client's name.
2. Select the **Import** tab, then click **Delete Xero Connection**.
3. Click **Delete** to confirm.

### Change the connection

1. Delete the existing connection to Xero, then click **Import from Xero**.
2. Select your client's organisation from the list, then click **Import**.
3. When the import finishes, click either:
   - **Edit Trial Balance** to [review and update the trial balance figures](Trial-balances.md) imported from Xero
   - **Go to Workpapers** to continue working on your client's workpapers

Fix common problems with the Xero connection

Workpapers (beta) Classic Workpapers

This process isn’t required in Workpapers.

### You’re not prompted to select your client’s organisation

You can only connect your classic Workpapers client to one Xero organisation. If you have an active workpaper pack for your client and the pack is connected to a Xero organisation, you won’t be prompted to choose an organisation when you import data. Classic Workpapers will simply import the data from the Xero organisation you connected to previously.

To resolve this issue, either change the connection for all active workpaper packs, or [archive any old packs](Archive-a-workpaper-pack.md) before importing data into the new pack.

### Your client's organisation doesn't appear in the list

If you don't see your client's organisation in the list to import from, you might not have access to the organisation. You need someone with manage users permission to [add you to the organisation](Add-a-new-user-to-your-organisation.md).

### Importing data from Xero into classic Workpapers failed

If you receive an **Import failed** message when you import data from Xero into your client's workpapers, check with your practice administrator to make sure your [role in Xero Business](User-role-access-to-reports-budgets-and-manual-journals-in-Xero.md) or [role in Xero Partner Edition](Partner-Edition-user-role-access-to-reports-budgets-manual-journals-and-fixed-assets.md) gives you access to reports.

## What's next?

Now that you’ve imported the trial balance data, see how to work with [supporting documents and information](Attach-manage-supporting-documents-information.md).