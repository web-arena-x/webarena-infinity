# Import or pre-fill information into a tax form

Source: https://central.xero.com/s/article/Import-or-pre-fill-information-into-a-tax-form

---

## Overview

- For Individual tax returns, you can import information from the ATO directly into your client's return using the pre-filling report.
- For all return types, you can import trial balance amounts from your client’s connected Xero organisation. Data from trial organisations can’t be imported due to ATO security requirements.
- You can import self-managed superannuation fund (SMSF) annual returns from other software you use.

Warning

[Tax manager](/s/article/About-the-new-Xero-Tax-manager-beta?userregion=true) is currently in beta and is restricted to a small number of users.

Pre-fill an Individual tax return with information from the ATO

### Automatically pre-fill an Individual tax return

Warning

You should not rely exclusively on the pre-fill report to complete your client's tax return, as not all payment types are imported from the pre-fill report. View all information by opening the pre-fill report from the ATO.

This option is only available for Individual tax returns for the tax year 2017 and later.

When you [create an Individual tax return](Create-a-new-tax-return.md), select the **Retrieve Prefill [PLS]** checkbox in the new return screen to load the available pre-fill information. This adds a note to the return history log recording that the return was pre-filled.

Reload the latest pre-fill at any time by selecting **Online PLS Pre-fill** from the options menu .

If you're encountering issues with pre-fill information on the tax return, take a look at the ATO's website for information on [recurring data issues](https://www.ato.gov.au/Tax-professionals/Prepare-and-lodge/Pre-filling-service/Recurring-data-issues/).

### Manually pre-fill an Individual tax return

Classic tax experience Tax manager

Download the pre-filling report for your client from the Tax Agent Portal, and save it as an XML file. [Pre-filling service – Tax Agent Portal](https://www.ato.gov.au/Tax-professionals/Prepare-and-lodge/Pre-filling-service/Pre-filling-reports/) (ATO website).

To import the pre-filling report:

1. In the **Tax** menu, select **Returns**.
2. Find the return, then click the client name to open it.
3. Click the menu icon , then select **Import XML Pre-fill**.
4. Browse to the pre-filling report XML file on your computer. Click **Import Pre-fill**.
5. Check the **ATO Pre-fill Summary Report**, then click **Apply ATO Pre-fill**.

If you get an error when importing, check the following:

- The report is saved as an XML file type.
- The Tax File Number in the file matches the client's.
- The tax return year is the same in the file and the return.

Once you've made and saved any changes on your computer, import the file again.

Download the pre-filling report for your client from the Tax Agent Portal, and save it as an XML file. [Pre-filling service – Tax Agent Portal](https://www.ato.gov.au/Tax-professionals/Prepare-and-lodge/Pre-filling-service/Pre-filling-reports/) (ATO website).

To import the pre-filling report:

1. In the **Tax** menu, select **Tax manager**.
2. Next to the relevant return, click **Open**.
3. Click the menu icon , then select **Import XML Pre-fill**.
4. Browse to the pre-filling report XML file on your computer. Click **Import Pre-fill**.
5. Check the **ATO Pre-fill Summary Report**, then click **Apply ATO Pre-fill**.

If you get an error when importing, check the following:

- The report is saved as an XML file type.
- The Tax File Number in the file matches the client's.
- The tax return year is the same in the file and the return.

Once you've made and saved any changes on your computer, import the file again.

### Working with pre-fill information

#### Identify pre-fill information in a return

Information from the pre-filling report is marked as **ATO Pre-Fill** (see below).

#### Remove pre-fill information from a return

Click the **Delete** icon to remove information from the pre-filling report you don't want in the return.

You can import the pre-fill report again if you want to restore this information.

#### Edit pre-fill information in a return

Most of the pre-filled information in a return can't be edited. However, descriptions for some items can be changed.

#### Print pre-fill information from a return

This option is available for Individual tax returns for the tax year 2020 and later.

You can print a PDF version of the pre-fill information retrieved for the tax return. Click the menu icon , then select **Print PLS Pre-fill**.

This lets you view pre-fill information that isn't imported into the return (eg the number of rentals a taxpayer has).

Import balances from Xero into a tax return or activity statement

### About importing balances from a Xero organisation

If your client has an active Xero organisation that you have access to, you can import trial balance amounts from that organisation into their tax return. Due to ATO security requirements, you won’t be able to select a trial Xero organisation to import data into tax forms.

You can import amounts from Xero for the following return types:

- Company tax return 2015 onward
- Individual tax return 2015 onward
- Trust tax return 2015 onward
- Partnership tax return 2015 onward
- Self-managed superannuation fund tax return 2015 onward

Before you can import amounts from Xero you must have:

- [Created a tax return](Create-a-new-tax-return.md) for your client
- Finalised or published the [activity statement](Activity-statements.md) in client's Xero organisation

#### Some total fields need to be manually entered

Not all items on the trial balance in Xero directly relate to a field on the return, so you’ll have to manually enter some totals within the return. You can choose to leave a field blank by selecting **Do Not Import** for the relevant field.

#### Amounts don't transfer to schedules or complex worksheets

Amounts don't transfer to schedules or complex worksheets like depreciation, motor vehicles or capital gains.

#### Substituted accounting period

If your client is using a substituted accounting period, you will need to manually complete the tax return without importing trial balances.

### Import amounts from Xero

Classic tax experience Tax manager

The return must be in **Draft** status.

1. In the **Tax** menu, select **Returns**.
2. Click the client name to open the return.
3. Select **Import from Xero** at the top of the page.
4. Select the Xero organisation to connect to, then click **Allow access**.
5. Click each account type, then select the tax return label you want that amount to map to.
6. Continue mapping all account types to tax return labels. All accounts need to be mapped before you can continue. To fill all tax return labels at the one time, click the checkbox to select all accounts, then select a tax return label.
7. Click **Import**.

Amounts that are imported from Xero have the Xero data label.

You can’t edit any of the fields that are transferred from your client's Xero balance in their tax return, but you can update the import.

The return must be in **Draft** status.

1. In the **Tax** menu, select **Tax manager**.
2. Click the client name to open the return.
3. Select **Import from Xero** at the top of the page.
4. Select the Xero organisation to connect to, then click **Allow access**.
5. Click each account type, then select the tax return label you want that amount to map to.
6. Continue mapping all account types to tax return labels. All accounts need to be mapped before you can continue. To fill all tax return labels at the one time, click the checkbox to select all accounts, then select a tax return label.
7. Click **Import**.

Amounts that are imported from Xero have the Xero data label.

You can’t edit any of the fields that are transferred from your client's Xero balance in their tax return, but you can update the import.

### Total fields that are mapped

#### Partnership tax return and Trust tax return 2015 onward

- Current Assets also map to Total Assets.
- Current Liabilities also map to Total Liabilities.

#### Company tax return 2015 onward

- Current Assets also map to Total Assets.
- Current Liabilities also map to Total Liabilities.
- Trade Debtors also map to 8C Trade debtors, 8D All current assets and 8E Total Assets.
- Trade Creditors also map to 8F Trade creditors, 8G All current liabilities and 8H Total liabilities.
- Salary and wage expenses also map to All other expenses in the Income tab and label 8D Total salary and wage expenses.

Update balances from Xero or view a client's connected organisation

### Update balances imported from Xero

Classic tax experience Tax manager

You can re-import data from Xero and change the mapping in the tax return. You might do this if:

- Data was mapped to the incorrect tax return label.
- You edited your client's data in Xero and want to update their tax return.

To update the data:

1. In the **Tax** menu, select **Returns**.
2. Find your client's name and click to open the return.
3. Click **Update from Xero**.
4. Review the labels selected in the **Tax Return Label** column. Make any updates required, and add labels for new accounts imported from Xero (if any).
5. Click **Import**.

You can re-import data from Xero and change the mapping in the tax return. You might do this if:

- Data was mapped to the incorrect tax return label.
- You edited your client's data in Xero and want to update their tax return.

To update the data:

1. In the **Tax** menu, select **Tax manager**.
2. Next to the relevant return, click **Open**.
3. Click **Update from Xero**.
4. Review the labels selected in the **Tax Return Label** column. Make any updates required, and add labels for new accounts imported from Xero (if any).
5. Click **Import**.

### View a client's connected Xero organisation

Importing an activity statement or tax return from Xero creates a connection to the client's Xero organisation. Practice Manager shows the name of the connected Xero organisation on the right side of the client record under **Connected Xero Organisation**.

Click the organisation name to open the Xero organisation in a new tab. To see the subscription details of the Xero organisation, click **View** next to the organisation name.

### Remove a connection

Classic tax experience Tax manager

If a client in Xero Tax or Practice Manager is connected to the wrong Xero organisation, you can remove the connection. To do this:

1. In the **Tax** menu, select **Returns**.
2. Find the client and click their name to open the return.
3. Click the arrow next to **Update from Xero**, then select **Disconnect from Xero**.

Once a connection has been removed:

- Previously imported balances will no longer show
- You can re-import from a different Xero organisation

If a client in Xero Tax or Practice Manager is connected to the wrong Xero organisation, you can remove the connection. To do this:

1. In the **Tax** menu, select **Tax manager**.
2. Next to the relevant return, click **Open**.
3. Click the dropdown next to **Update from Xero**, then select **Disconnect from Xero**.

Once a connection has been removed:

- Previously imported balances will no longer show
- You can re-import from a different Xero organisation

### Things to note

- You can't remove a Xero connection from within the client record. You need to select **Disconnect from Xero** from the tax return or activity statement.
- If you don't have access to the Xero organisation and click on the Xero client link, you'll be directed to your My Xero portal.
- The **View** link displays the organisation's details at the time of the connection. Changes made to the Xero organisation will show after importing from Xero again.
- Once a Xero organisation is connected to a client record in Xero Tax or Practice Manager, you can't connect it to other client records. If you want to connect the Xero to a different client, you’ll need to disconnect the current connection.

Import SMSF return from SMSF admin software

### How it works

Import a Self-managed superannuation fund (SMSF) annual return from other SMSF administration software you use, for lodgment to the ATO using Xero Tax. You can import XML data from:

- BGL
- Class
- Supermate

### Supported schedules

- Capital gains tax schedule
- Losses schedule
- Members' statements

Schedules not supported are: Interposed entity election, Family trust election or revocation, and Payment summary schedules.

### Things to do before you import

In your SMSF admin software:

1. Complete the return, including appropriate worksheets. Worksheet values will be imported as a gross value for each return label.
2. Validate the return, resolving any errors.
3. Export the return.

### What happens when you import

- The fund is matched based first on TFN, then ABN and fund name.
- Members' statements are created for all members, even ones not in Xero Tax.
- Worksheets are created when there is data that needs a line in a worksheet.
- You can import the file again, and this will overwrite existing information from the initial import.

If you’ve rolled over from a previous year, worksheets are appended, but opening balances are overwritten. We recommend that you do not roll over a previous year’s return, as this may result in duplication of schedules and worksheets, as well as incorrect member statements.

### Import SMSF annual return

Before starting these steps, you’ll need to download the SMSF annual return from your SMSF admin software as an XML file onto your computer.

1. [Create a new SMSF annual return](Create-a-new-tax-return.md), or open an existing return that’s in draft.
2. Click the menu icon , then select **Import from XML**.
3. Click **Select File**, then select the XML file you’ve downloaded on your computer.
4. Click **Import**.

### Review data imported

- Review the log file of imported and skipped values from the return **Overview**, under **History**.
- Review the values in the return and member statements against the details in your SMSF admin software.

If the import isn't successful, you need to resolve the errors and try the import again.

## What's next?

If you're preparing a tax return, read our [detailed guides for specific guidance on each tax return type](/s/topic/0TO1N0000017kpmWAA/forms-practice-manager-xero-tax#practice).