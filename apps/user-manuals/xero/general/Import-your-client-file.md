# Import clients to Practice Manager

Source: https://central.xero.com/s/article/Import-your-client-file

---

## Overview

- Set up your client list initially, add or update clients, or add contacts to your clients.
- When you import a client in Xero Practice Manager, the client is automatically created in Xero HQ as well.
- If you’re trialing Practice Manager, use [this process](Import-clients-during-your-Practice-Manager-trial.md) instead.

Warning

If you export any files from Practice Manager, don’t remove the exported values when importing additional data using this file. Blank fields will replace existing data.

**1** Prepare the client import file

Tip

We recommend creating a backup file for your existing data in Practice Manager before importing the updated file. This might be useful for data recovery if you get an import error.

### What you need to know

You can [prepare an import file](Import-data-into-Practice-Manager.md) using a blank file, [Xero template](https://xero.my.salesforce.com/sfc/p/o0000000biwC/a/1N000000UYqJ/RNg0oI4HKp0UrDjjiaRF5aluePMtQbW._YtepLOH_SU) (CSV, 648 bytes) or an exported file from your practice or your practice’s Xero organisation.

If you’re using an exported file from Practice Manager to import your data, don’t remove the client UUID or contact UUID information. These are unique client IDs that are used to match imported data against existing clients and contacts, and help prevent duplication when you re-import your file.

In your import file, each column header identifies a data field that you want to include in your import. You need to specify column headers for only those fields that you want to import.

The column headers in your import file must match the column headers in the Xero template file. You need to use the same capitalisation with any spaces, punctuation or other characters as shown in the column headers of the template.

You can import contacts when you import clients, or create a separate import file just for contacts. If you want to import multiple contacts for a client, [import the contact details](Import-client-contacts.md) into the first client then link these contacts to other clients. You can also [export your contacts](Export-contacts-out-of-Xero.md) from Practice Manager.

When updating existing contacts, ensure the client name is the same to avoid creating duplicates.

You can’t use an import file to delete clients or contacts. If your data contains more than 500 rows, split the data into multiple files and import each separately.

When you import a client in Practice Manager, the client is automatically created in Xero HQ as well.

### Required fields

**Name** is the required field in your import file. If there’s a match for this field in Practice Manager and:

- You select the **Update Existing** checkbox – Practice Manager updates the existing client
- You don’t select **Update Existing** – the details in Practice Manager don’t change

**ContactName** is also required if you’re importing contact details. If this field matches an existing contact for a client, Practice Manager creates a duplicate contact for that client.

### Client fields explained

| | |
| --- | --- |
| **BalanceMonth** | Enter the last month of your client's financial year as either the 3-letter abbreviation for the month or the number of the calendar month. |
| **BusinessStructure** | The value must match an [existing business structure](Set-up-custom-business-structures-in-Practice-Manager.md). |
| **CompanyNumber** | Your client's company number without dashes or spaces. |
| **DateofBirth** | The value must be in d/m/yyyy format. |
| **ExportCode** | Enter the [optional code](Edit-a-client-in-Practice-Manager.md) used by an external system, such as your CRM system. |
| **Group** | The value must match the name of an existing [group in Practice Manager](/s/article/Group-clients-in-Practice-Manager?userregion=true). If the group doesn't exist, Practice Manager will create it. |
| **GstPeriod** | Enter the number that corresponds to the monthly GST filing period: **1**, **2** or **6**. |
| **GstBasis** | Enter the GST basis:   - **P** – Payment - **H** – Hybrid - **I** – Invoice |
| **JobManager** | The value must match the name of an existing staff member in Practice Manager. |
| **Name** | Enter the value for the client’s name. This is a required field. |
| **TaxNumber** | Enter the client’s IRD number without dashes or spaces. |
| **WebSite** | Enter the full URL of your client’s website. |

### Additional column names for Individual type clients

When you import Individual type clients, you can include values in the **FirstName**, **LastName**, and **OtherName** columns. Practice Manager uses this additional name information on the tax returns for Individual type clients.

**2** Import the data

Tip

We recommend creating a test file with some line items and then importing it into Xero. This is to check if the file you’ve created is formatted correctly and will import successfully. Once you’re happy with the results, you can then import your actual file.

1. In the **Business** menu, select **Settings**.
2. Under **Connections**, click **Import**.
3. For **File Type**, select **Generic - Client**.
4. Select the format of your import file.
5. To update the existing clients, select the checkbox.
6. Click **Choose File** and select your import file.
7. Click **Import**.

The number of rows imported and any errors are displayed at the bottom of the screen. You might also want to spot check the details of a few clients to verify the import.

## What's next?

After you import your client list, [manage your clients](About-clients-and-contacts-in-Practice-Manager.md).