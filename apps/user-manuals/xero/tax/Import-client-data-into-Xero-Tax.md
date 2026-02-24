# Import client data into Xero Tax

Source: https://central.xero.com/s/article/Import-client-data-into-Xero-Tax

---

## Overview

- Import your client data from the ATO, Reckon Elite or Tax Assist.
- You can also import your client's data using a CSV file.

Import from the BAS or Tax Agent Portal

### Download your ATO report

To create or update client records by importing reports from the ATO BAS Agent Portal or Tax Agent Portal, start by downloading one of the following reports from the relevant ATO portal:

| Report | BAS Agent Portal | Tax Agent Portal | Available fields for import |
| --- | --- | --- | --- |
| Income tax lodgment status report | **-** | **✔** | - Client name - Business structure - TFN - Due date - Prepare tax form checkbox |
| Outstanding activity statement report | **✔** | **✔** | - Name - Business structure - ABN - Prepare Activity Statement form checkbox - Branch/CAC/ICA # |
| Client account running balance report | **✔** | **-** | - Client name - ABN |

### Using the new Online services for agents portal

Warning

The identifier in the Client Running Account Balance Report, downloadable from the ATO's new online service for agent's portal, has changed. This means that you can't import the report at the moment.

The ATO have changed file naming conventions in their new Online services for agents portal. This can cause the error 'client list filename is not valid' when reports are imported into Xero.

To avoid this, change the file name to the old convention listed below for each report type. You can use any date and time in the file name.

- For the Income tax lodgment status report, the file name convention should be 'TAN Client Lodgment List - IT DownloadedDate DownloadedTime'.
- For the Outstanding activity statement report, the file name convention should be 'TAN Client Lodgment List - Outstanding AS DownloadedDate DownloadedTime'.

For example, the file names could be:

- 01122333 Client Lodgment List - IT 20190418 17-20
- 01122333 Client Lodgment List - Outstanding AS 20190418 17-20

### Import the ATO report

Warning

Limit your file to 500 clients to avoid gateway errors. Also, don't make any changes to the ‘Client account running balance’ report after it’s been downloaded.

Once you’ve downloaded the required report, you can import your client's data:

1. In the **Business** menu**,** select **Settings**.
2. Under **Connections**, click **Import**.
3. Select one of the following options from the **File Type** list:
   - **Tax Agent Portal - Income Tax/Activity Statement Client List Report**
   - **ATO Portal - Client account running balance report**
4. (Optional) If you're updating client details or tax return due dates, select the **Update Existing?** checkbox so that the existing details are replaced. Otherwise, existing client records might be duplicated.
5. From the **File Format** list select **Comma-separated**.
6. Choose if you want to update existing files.
7. Click **Choose File** and browse to the report on your computer, then click **Open**.
8. Click **Import**.

Once the upload is finished, the results show under the **Import Result** heading at the bottom of the page.

Any lines that aren't added are listed in these results, with details of the error. You'll need to separately [add these tax clients](/s/article/Create-a-client-in-Practice-Manager-AU).

Import from Reckon Elite

Export your clients' names and addresses from Reckon Elite, and import them into Xero Tax in bulk. You’ll need to send your exported client data to Xero Support so we can format it for you.

Begin by exporting your client data from Reckon Elite:

1. In Reckon Elite, go to **Client Management**, then select all clients.
2. Select the **File** tab, then click **Export**.
3. Click **Marked Clients** to export clients selected. Take note of any clients you're not exporting, so you can upload them manually.
4. Choose a location to save the ZIP file to.
5. Raise a case with Xero Support, attach your export file so we can process the file and send you back a formatted version you can import into Xero Tax.

To import the converted file into Xero Tax:

1. In the **Business** menu, select **Settings**.
2. Under **Connections**, click **Import**.
3. From the **File Type** list, select **Tax Assist - Client**.
4. From the **File Format** list, select **Comma-separated**.
5. Click **Next**.
6. Click **Choose File** and select the formatted file you received from Xero Support.
7. Click **Import**.

Import from Tax Assist

If you're moving to Xero Tax from Tax Assist, you can import your client tax list into Xero Tax.

Start by exporting your client tax data from Tax Assist:

1. In Tax Assist, select all of the clients whose records you want to export.
2. From the **File** menu, select **Export Data**.
3. Select **Client Details**. You'll see the **Export Client Details** window.
4. Select all of the fields in the left part of the window, and then click **>>**.
5. Click **Export**.
6. When prompted, give the CSV file a descriptive name.
7. Select where you want to save the file.
8. Click **Save**.

To import your client list into Xero Tax:

1. From the **Business** menu, select **Settings**.
2. Under **Connections**, click **Import**.
3. From the **File Type** list, select **Tax Assist - Client**.
4. from the **File Format** list, select **Comma-separated**.
5. Click **Choose File** and find the file you exported from Tax Assist.
6. Click **Import**.

The following information imports into Xero:

| Tax Assist field | Xero Tax field | Notes |
| --- | --- | --- |
| CL\_ReturnType | Business Structure | - EC - Company - EI - Individual - EP - Partnership - ET - Trust - MS - Self Managed Super Fund |
| CL\_FileNo | TFN | **-** |
| CL\_TFN\_Trail | **-** | **-** |
| CL\_ABN | ABN | **-** |
| CL\_ABN\_Div | Branch/CAC/ICA # | **-** |
| CL\_Name | Name | If the return is something other than an **Individual** return |
| CL\_LastName | Last Name | Only if the return is an **Individual** return |
| CL\_FirstName | First Name | Only if the return is an **Individual** return |
| CL\_OtherNames | Other Name | Only if the return is an **Individual** return |
| CL\_BirthDate | Date of Birth | **-** |
| CL\_SpouseLastName | **-** | **-** |
| CL\_SpouseFirstName | **-** | **-** |
| CL\_SpouseOtherNames | **-** | **-** |
| CL\_PhoneArea | Phone | **-** |
| CL\_PhoneNumber | Phone | Practice Manager looks for an entry in the **CL\_Mobile** field. If the **CL\_Mobile** field is blank, it looks at the **CL\_Home** field. If the **CL\_Home** field is blank, Practice Manager uses the entry in the **CL\_Phone** field. |
| CL\_HomeArea | Phone | Needs to include both the area code and number if either **CL\_PhoneNumber** or **CL\_HomePhone** is used |
| CL\_HomePhone | Phone | **-** |
| CL\_FaxArea | Fax | The area code and number must be included if **CL\_Fax** is used |
| CL\_Fax | Fax | **-** |
| CL\_Mobile | Phone | **-** |
| CL\_EMail | Email Address | **-** |
| CL\_WEB | Website | **-** |
| CL\_PAddr1 | Postal Address - Street Address (line 1) | **-** |
| CL\_PAddr2 | Postal Address - Street Address (line 2) | **-** |
| CL\_PSuburb | Postal Address - Town / City | **-** |
| CL\_PState | Postal Address - State / Region | **-** |
| CL\_PPostCode | Postal Address - Postal / Zip code | **-** |
| CL\_PCountry | Postal Address - Country | **-** |
| CL\_HAddr1 | Physical Address - Street Address (line 1) | **-** |
| CL\_HAddr2 | Physical Address - Street Address (line 2) | **-** |
| CL\_HSuburb | Physical Address - Town / City | **-** |
| CL\_HState | Physical Address - State / Region | **-** |
| CL\_HPostCode | Physical Address - Postal / Zip code | **-** |
| CL\_HCountry | Physical Address - Country | **-** |
| CL\_Tax | Prepare Tax Form | If CL\_Tax is **True** then the **Prepare Tax Form** setting in Practice Manager is selected |

###

Import client data using a CSV file

You can import or update information about multiple clients using an import file. You can also assign a partner or manager to your clients.

You can import up to 500 clients in one file. If you have more than 500 clients, import them in multiple files.

Tip

Test the import with a small number of clients first to ensure the information updates as expected.

You can use a blank file, or the example file we provide. We recommend you use an exported file and follow our guidelines for [preparing the client import file](https://central.xero.com/s/article/Import-your-client-file-AU#Preparetheclientimportfile) so that your data imports as you expect.

To export your client data:

1. In the **Business** menu, select **Settings**.
2. Under **Connections**, click **Export**.
3. From the **File Type** option list, select **Generic - Clients**.
4. Click **Export**.
5. Click the **Click to download export file** link.

Once you've made your updates, import your client data file:

1. In the **Business** menu, select **Settings**.
2. Under **Connections**, click **Import**.
3. From the **File Type** option list, select **Generic - Client**.
4. From the **File Forma**t list, select **Comma-separated**.
5. Click **Next**.
6. (Optional) Select **Update Existing?** if you want to import new details for existing clients.
7. Click **Choose File** and find the file containing the data you want to import.
8. Click **Import**.

## What's next?

Now that you've imported your client records, you might also want to:

- [Set up client relationships](Set-up-client-relationships.md)
- [Group clients in Xero Tax](/s/article/Group-clients-in-Practice-Manager)