# Bulk update tax agents linked to clients in Xero Tax

Source: https://central.xero.com/s/article/Bulk-update-tax-agents-linked-to-clients-in-Xero-Tax

---

## Overview

- Edit or change tax agent profiles to bulk update.
- Import a bulk of tax agents in Xero Tax.
- Download report as a CSV file.

## Update existing agent profile with new agent details

You can bulk update tax agents linked to clients in Xero Tax. If you don't need an old agent profile in your Xero Tax account for reporting purposes and you haven't created a new agent profile, you can update the existing profile with the new agent's details. To do this:

1. In the **Business** menu, select **Settings**.
2. Under the **Practice** heading, click **Client Settings**.
3. Select the **Agent** tab.
4. Click the name of the agent whose details you want to edit.
5. Make changes, then click **Save**.

Once you've done this, you can [connect a tax agent to the ATO](Set-up-a-tax-agent-and-connect-to-the-ATO.md) and nominate Xero as the lodgment software for the new agent. Clients already linked to the old agent profile will now be linked to the new agent profile.

The Contact Name field and the Daytime Contact Number field on the Cover page of a draft return won't automatically update when you change the tax agent details. You need to manually update these fields for draft returns.

## Bulk add clients to new agent profile

You can bulk update tax agents linked to clients in Xero Tax. If you've already created a new agent profile, or you don't want to override the existing profile, you can update the agent linked to clients in bulk using the CSV export/import feature. To do this, create a report with a list of active clients that need to be updated:

1. In the **Reports** menu, select **Report Builder**.
2. Select the **Custom reports** tab, and click **New report**.
3. Select **Client and Contact** as the report type, and **Table** as the Report Layout.
4. Click **Create**.
5. In the **Fields** section, select **[Client] Client** and **[Client] Tax Agent**.
6. In the Criteria section, select **[Client] Tax Agent** and under **includes** select the agent that needs to be replaced. You can also use the filter **[Client] Status** to exclude archived clients from the results.
7. In the **Publish** section, select the name of the staff members who can view the report.
8. Click **Save**.

To download the report as a CSV file:

1. In the **Reports** menu, select **Report Builder**.
2. Click **Custom reports**, and select the report you want to download.
3. Click **Preview Report**.
4. In the **Export tab**, select **CSV.**

Update the CSV file with the content in the spreadsheet. You also need to update the column headers below to match the import requirements for updating client details:

- [Client] Client – Change to Name.
- [Client] Tax Agent – Change to TaxAgent. Please note, there's no space in TaxAgent.

In the **Tax Agent** column, enter the exact name of the new agent profile set up in Xero Tax to update the agent field.

Once this is done, you need to import the CSV to complete the set up. You can only import up to 500 rows in one file. We recommend you test the import file with a few client records first. Then check the client details have been updated correctly before you [import your entire list](/s/article/Import-your-client-file-AU), as you can't reverse the imported result.

## What's next?

You're all done!