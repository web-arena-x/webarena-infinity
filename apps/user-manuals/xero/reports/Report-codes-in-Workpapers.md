# Use report codes in Workpapers

Source: https://central.xero.com/s/article/Report-codes-in-Workpapers

---

## Overview

- Map Xero general ledger account codes to Workpapers report codes.
- Exclude codes to customise the information that appears in a workpaper.

Tip

Workpapers is currently in beta and is available to selected practices. We’ve renamed our original solution classic Workpapers.

How it works

Workpapers (beta) Classic Workpapers

Workpapers uses report codes to map the data that imports from Xero to the workpapers in a workpaper pack.

The report code mapping is done automatically when you activate your Workpapers organisation. Currently it’s not possible to modify the report code mapping.

You can view the report code mapping for each workpaper in the **Workpaper mapping** tab of **Workpaper settings**. The report codes used to map the accounts in a client’s workpaper pack display in the **Report code** column of the **Working trial balance** tab.

- Classic Workpapers uses report codes to map the data you import from Xero to the workpapers in a workpaper pack.
- When you set up a pack, you can choose to use the account code to report code mappings from your client’s Xero chart of accounts, or let classic Workpapers predict the report codes based on the account names.
- After you import the data, you might need to adjust the report codes to make sure you have the right data in the right workpaper. If you use the Xero report codes, you must edit the report codes directly in Xero. Otherwise, edit them in classic Workpapers.
- Some workpapers use specific, preset report codes or don’t use report codes at all. You can’t change the report code mappings for these workpapers.
- You need the [practice admin user role](User-roles-in-Workpapers.md) in classic Workpapers to change the mappings between report codes and workpapers.

Edit Xero report codes

Workpapers (beta) Classic Workpapers

This functionality isn’t currently available in Workpapers.

1. Select the **Workpaper Packs** tab, then click your client's name.
2. Select the **Import** tab, then click **Edit Trial Balance**.
3. Click **Edit Xero report codes**, then [change the report code mappings](Report-codes-for-practices-using-report-templates.md) in Xero.
4. Return to classic Workpapers.
5. Click **Refresh from Xero** to import the revised mappings.

Edit Workpapers report codes

Workpapers (beta) Classic Workpapers

This functionality isn’t available in Workpapers.

1. Select the **Workpaper Packs** tab, then click your client's name.
2. Select the **Import** tab, then click **Edit Trial Balance**.
3. Select an account category, then click a report code.
4. Select headings in the report code screen to edit the current path of a report code. Selecting a heading in the first column moves the report code back a level. Selecting a heading in the middle column moves a report code forward a level.
5. Click **Save**.

Change report code to workpaper mappings

Workpapers (beta) Classic Workpapers

This functionality isn’t currently available in Workpapers.

Change the report code mappings for individual workpapers by adding or removing codes to include or exclude. You can enter more than one report code to include or exclude for a workpaper. Use a comma to separate the report codes.

If you don’t see the include and exclude fields for a workpaper, the workpaper doesn’t use report codes. If the include field is locked and the exclude field isn’t shown, the mappings can’t be changed.

1. Select the **Settings** tab.
2. Under **Workpapers**, click **Xero Report Code Defaults** or **Workpaper Report Code Defaults**.
3. For each workpaper you want to change, update the codes under **Include report codes** and **Exclude report codes** to customise the information that appears in the workpaper.
4. (Optional) Select the **Apply changes to existing workpaper packs** checkbox to update all existing workpaper packs. These changes override any report code mappings you've applied to individual clients.
5. Click **Save**.

Working with the Exclude Report Codes column

Workpapers (beta) Classic Workpapers

This functionality isn’t currently available in Workpapers.

In this worked example, we'll show how to exclude information from a specific workpaper.

Let's say your practice uses the Prepayments workpaper. You can exclude prepayments from the Accounts Receivable workpaper so you don't repeat information. Type the report code ASS.CUR.REC.PRE in the **Exclude Report Codes** column for the Accounts Receivable workpaper.

You can also delete report codes to show information in a workpaper. For example, your practice might want to show loans to directors in the Non-Current Assets workpaper. Delete the report code ASS.NCA.DIR from the **Exclude Report Codes** column for the Non-Current Assets workpaper.

## What's next?

After you set up report codes, review your client's [trial balances](Trial-balances.md).