# Migrating Data From Your Current Software [T-Z]

Source: https://help.clio.com/hc/en-us/articles/9812890677531-Migrating-Data-From-Your-Current-Software-T-Z

---

This article explains what data can be migrated from your current practice management software and how to export the data from that software. Software applications starting with the letters T, U, W, and Z, and any numbers are listed below.

**Tip:** See one of the articles below if your current practice management software does not start with the letters T, U, W, Z, or any numbers.

- - [Migrating Data From Your Current Software [A-B]](https://help.clio.com/hc/en-us/articles/9813809475995)
 - [Migrating Data From Your Current Software [C-F]](https://help.clio.com/hc/en-us/articles/10263045235867)
 - [Migrating Data From Your Current Software [G-M]](https://help.clio.com/hc/en-us/articles/10263146574107)
 - [Migrating Data From Your Current Software [N-S]](https://help.clio.com/hc/en-us/articles/9815681343003)

## Tabs3/PracticeMaster

What can I migrate? How do I migrate my data?

- Contacts
- Matters
- Unbilled Expenses Entries
- Unbilled Time Entries
- Related Contacts
- Matter Notes
- Calendar Events
- Tasks
- Email Communications
- Phone Communications
- Outstanding (a single line item that represents the summative balance at time of export for a Matter)
- Trust Balances (a single line item that represents the summative balance at time of export for a Matter or Contact)

**Note:** Depending on the quality of your data, we may also be able to migrate email and phone communications, related contacts, contact and matter notes, calendar events, tasks, and unbilled time and expense entries.

**Note:** Tabs3 does not have an export function. Your data can only be exported through the PracticeMaster interface. The PracticeMaster version should be compatible with the Tabs3 version to synchronize properly. If you are having issues with setting up PracticeMaster or have sync issues, contact Tabs3 support to set up PracticeMaster.

**Contacts, matters, and other files:**

1. Select the **Maintenance** tab and click **File Maintenance.**
2. Select the desired **Export Files****.** 

   | Data type | File location | File name |
   | --- | --- | --- |
   | Matters | Client | CMCLIENT |
   | Contacts | Lookup Files > Contact | CMRELATE |
   | Notes and communications | Common Client Related Files > Journal | CMJRNL |
   | Tasks and calendar | Calendar | CMCAL |
   | Expenses | Common Client Related Files > Cost | CMCOST |
   | Fees | Common Client Related Files > Fee | CMFEES |
3. Click **OK**.
4. Select **Utility** and click **Export Data.**
5. Rename the file and add **.csv** to convert it into a spreadsheet format.
6. Click **Ok**.

**Timekeeper list (with ID numbers):**

1. Go to the **TABS** module.
2. Click **Reports** > **Miscellaneous** > **Timekeepers List.**
3. Export file to XLSX format.

**Category list (with ID numbers and for practice areas):**

1. Go to the **TABS** module
2. Click **Reports** > **Miscellaneous** > **Category List.**
3. Export file to XLSX format.

**Task code list (with ID numbers):**

**Note:** The Tcode column in CMFEE and CMCOST will migrate to the activity categories for time and expenses in Clio.

1. In the search bar, search for **Transaction Code List**.
2. Export file to XLSX format.

**Accounts receivables:**

1. Go to **Reports** > **Accounts Receivable** > **AR Summary Report.**
2. Select **Sort** tab settings.
3. Check **Subtotal by Client.**
4. Selec**t Report Order = None.**
5. Click **OK** to generate the report and then export as Excel format (e.g. xlsx, csv, etc.).

**Trust balances:**

1. Go to the **TAS** (Trust Accounting Software) module on the bottom left of the PM.
2. Click **Reports.**
3. Select **Trust Account List Report** and save the data in xlsx format.

## 

## Thryv

What can I migrate? How do I migrate my data?

- Contacts
- Calendar Events

**Contacts:**

1. Go to **Clients** on the left side panel.
2. *Optional*: Click **Filter** and set parameters as needed.
3. Click **More** **actions** in the top right and select **Export** from the dropdown menu.
4. In the new modal, under **Rows,** if you previously set filters, click **Filtered.**
5. Under **Format,** select **CSV** if not already selected.
6. Click **Download.**

**Calendar:**

1. Go to **Calendar** on the left side panel.
2. *Optional*: Click **Filter** and set appropriate filters.
3. Click **More** **actions** in the top right and select **Export booking data** from the dropdown menu.
4. In the **Appointments and Events Reports** modal, confirm or set a date range.
5. Under **Columns,** select **All.**
6. Under **Rows,** if you previously set filters, click **Custom.**
7. Under **Format,** select **CSV** or **Excel.**
8. Click **Download.**

## Time & Chaos

What can I migrate? How do I migrate my data?

- Contacts
- Matters (limited information from v. 10.2)
- Tasks
- Unbilled Time Entries (v. 10.2)
- Unbilled Expense Entries (v. 10.2)
- Calendar Events

**Note:**We have not confirmed the exact nature of what can be migrated from this program to Clio. You can, however, still follow the export directions.

1. Click **Reports** and select **Contacts.**
2. Right click on any of the columns to show a list of available fields. Select the fields you want included in the export.
3. Click **Find Now.**
4. Select all items.
5. Click **File** and select **Export to Excel.**
6. Repeat the above steps for Calendar and Tasks.

## Time Matters

What can I migrate? How do I migrate my data?

- Contacts
- Matters
- Notes
- Related Contacts
- Tasks (To dos)
- Unbilled Time Entries
- Unbilled Expense Entries
- Calendar Events

**Note:** Depending on the quality of the data, we may be able to migrate email and phone communications and outstanding balances.

**Database Backup**

1. Open Time Matters.
2. Go to **File** > **Backup Time Matters Data**.
3. Verify that the **Shared Files Backup** location is correct.
4. *Optional:* Click the **ellipsis menu** to change the location where the shared files will be saved.
5. Check the box next to **Skip files in the Documents and Documents Index Directories**.
6. Check the box next to **Skip backing up of email attachments**.
7. If you are using a non-default location and want Time Matters to remember the location selected in the **Shared Files Backup**, check the box next to **Remember this destination for future backups**.
8. Click the radio labeled as **Backup Now** in the bottom. This may or may not be an available option.
9. Click **OK** to start the backup process.

**Note:** Only documents and email attachments are backed up to this location. The SQL database is backed up to the default backup location for the Microsoft SQL Server. Time Matters SQL database backups are stored in a different location than Time Matters document and email files backups, which will be backed up to the Server. The default location of the SQL backup data is either C:\Program Files\Microsoft SQL Server\MSSQL.XX\MSSQL\Backup or C:\Program Files(x86)\Microsoft SQL Server\MSSQL.XX\MSSQL\Backup.

**Front-end reports**

**Step 1: Follow these initial steps to get started.**

1. Open Time Matters.
2. Go to **File**> **Setup** > **User and Security** > **Security Settings**.
3. Uncheck the box for **Activate Security Features Throughout the Application (Recommended).**
4. Recheck the box once the export is completed.

**Step 2: Export your data. See the sections below.**

**Important:** When doing a typical Time Matters migration, only the Contacts and Matters front-end reports are exported along with the Time Matters database backup. Additionally, only export the remaining sections as a workaround if you are unable to export a Time Matters database backup.

**Contacts:**

1. Open Time Matters.
2. Go to **File** > **Export** > **Custom Export**.
3. Select **Create a new Export Template.**
4. Click **Next.**
5. On the **Select Export File Format** page, select **ASCII - Comma Delimited (.TXT or .CSV)**>  check **Include field names labels as first record in Export**> click **“...”** > assign the file a name and select a location, typically in c:\Clio Export\ (creating the folder Clio Export).
6. On the **Specify Time Matter Record Type** page, select the **Export the following Record Type** dropdown menu and choose **Contacts.**
7. On the **Select Pre-Merge Record**page, select **None** > click **Next.**
8. On the **Export Custom Forms**page, select **None** > click **Next.**
9. On the **Select Contact Export Fields**page, click **Add All** > remove the **Memo**field from the selection > click **Next** > when it asks about **Archived Status**, make sure to get **BOTH** non-archived data and archived data (unless preferences are otherwise).
10. On the **Launch Application After Export** page, select **No, do not launch an application** > click **Next.**
11. On the **Ready to Begin Export** page, select **Yes. Save this Export Template** > click **Finish.**
12. When the export is complete, click **OK.**

**Matters:**

1. Open Time Matters.
2. Go to **File** > **Export** > **Custom Export**.
3. Select **Create a new Export Template.**
4. Click **Next.**
5. On the **Select Export File Format** page, select **ASCII - Comma Delimited (.TXT or .CSV)**>  check **Include field names labels as first record in Export**> click **“...”** > assign the file a name and select a location, typically in c:\Clio Export\ (creating the folder Clio Export).
6. On the **Specify Time Matter Record Type** page, select the **Export the following Record Type** dropdown menu and choose **Cases.**
7. On the **Select Pre-Merge Record**page, select **None** > click **Next.**
8. On the **Export Custom Forms**page, select **None** > click **Next.**
9. On the **Select Matter Export Fields** page, click **Add All** > remove the **Memo**field from the selection > click **Next** (filter and export by practice area to get header names) > when it asks about **Archived Status**, make sure to get **BOTH** non-archived data and archived data (unless preferences are otherwise).
10. On the **Launch Application After Export** page, select **No, do not launch an application** > click **Next.**
11. On the **Ready to Begin Export** page, select **Yes. Save this Export Template** > click **Finish.**
12. When the export is complete, click **OK.**

**Calendar events:**

1. Open Time Matters.
2. Go to **File** > **Export** > **Custom Export**.
3. Select **Create a new Export Template.**
4. Click **Next.**
5. On the **Select Export File Format** page, select **ASCII - Comma Delimited (.TXT or .CSV)**>  check **Include field names labels as first record in Export**> click **“...”** > assign the file a name and select a location, typically in c:\Clio Export\ (creating the folder Clio Export).
6. On the **Specify Time Matter Record Type** page, select the **Export the following Record Type** dropdown menu and choose **Events.**
7. On the **Select Pre-Merge Record**page, select **None** > click **Next.**
8. On the **Export Custom Forms**page, select **None** > click **Next.**
9. On the **Select Matter Export Fields** page, click **Add All** > remove the **Memo**field from the selection > click **Next** > when it asks about **Archived Status**, make sure to get **BOTH** non-archived data and archived data (unless preferences are otherwise).
10. On the **Launch Application After Export** page, select **No, do not launch an application** > click **Next.**
11. On the **Ready to Begin Export** page, select **Yes. Save this Export Template** > click **Finish.**
12. When the export is complete, click **OK.**

**Tasks:**

1. Open Time Matters.
2. Go to **File** > **Export** > **Custom Export**.
3. Select **Create a new Export Template.**
4. Click **Next.**
5. On the **Select Export File Format** page, select **ASCII - Comma Delimited (.TXT or .CSV)**>  check **Include field names labels as first record in Export**> click **“...”** > assign the file a name and select a location, typically in c:\Clio Export\ (creating the folder Clio Export).
6. On the **Specify Time Matter Record Type** page, select the **Export the following Record Type** dropdown menu and choose **To Dos.**
7. On the **Select Pre-Merge Record**page, select **None** > click **Next.**
8. On the **Export Custom Forms**page, select **None** > click **Next.**
9. On the **Select Matter Export Fields** page, click **Add All** > remove the **Memo**field from the selection > click **Next** > when it asks about **Archived Status**, make sure to get **BOTH** non-archived data and archived data (unless preferences are otherwise).
10. On the **Launch Application After Export** page, select **No, do not launch an application** > click **Next.**
11. On the **Ready to Begin Export** page, select **Yes. Save this Export Template** > click **Finish.**
12. When the export is complete, click **OK.**

**Notes:**

1. Open Time Matters.
2. Go to **File** > **Export** > **Custom Export**.
3. Select **Create a new Export Template.**
4. Click **Next.**
5. On the **Select Export File Format** page, select **ASCII - Comma Delimited (.TXT or .CSV)**>  check **Include field names labels as first record in Export**> click **“...”** > assign the file a name and select a location, typically in c:\Clio Export\ (creating the folder Clio Export).
6. On the **Specify Time Matter Record Type** page, select the **Export the following Record Type** dropdown menu and choose **Notes.**
7. On the **Select Pre-Merge Record**page, select **None** > click **Next.**
8. On the **Export Custom Forms**page, select **None** > click **Next.**
9. On the **Select Matter Export Fields** page, click **Add All** > remove the **Memo**field from the selection > click **Next** > when it asks about **Archived Status**, make sure to get **BOTH** non-archived data and archived data (unless preferences are otherwise).
10. On the **Launch Application After Export** page, select **No, do not launch an application** > click **Next.**
11. On the **Ready to Begin Export** page, select **Yes. Save this Export Template** > click **Finish.**
12. When the export is complete, click **OK.**

**Time and expenses:**

1. Open Time Matters.
2. Go to **File** > **Export** > **Custom Export**.
3. Select **Create a new Export Template.**
4. Click **Next.**
5. On the **Select Export File Format** page, select **ASCII - Comma Delimited (.TXT or .CSV)**>  check **Include field names labels as first record in Export**> click **“...”** > assign the file a name and select a location, typically in c:\Clio Export\ (creating the folder Clio Export).
6. On the **Specify Time Matter Record Type** page, select the **Export the following Record Type** dropdown menu and choose **Billing.**
7. On the **Select Pre-Merge Record**page, select **None** > click **Next.**
8. On the **Export Custom Forms**page, select **None** > click **Next.**
9. On the **Select Matter Export Fields** page, click **Add All** > remove the **Memo**field from the selection > click **Next** > when it asks about **Archived Status**, make sure to get **BOTH** non-archived data and archived data (unless preferences are otherwise).
10. On the **Launch Application After Export** page, select **No, do not launch an application** > click **Next.**
11. On the **Ready to Begin Export** page, select **Yes. Save this Export Template** > click **Finish.**
12. When the export is complete, click **OK.**

## Time59

What can I migrate? How do I migrate my data?

- Contacts
- Matters (derived from contact listing)
- Unbilled time and expense entries

**Contacts:**

1. Click on **export** in the main menu.
2. Select **Export to Excel.**
3. Select **Clients** from the dropdown.
4. Select **All** or the date range for the data.
5. Click **Export.**

**Time entries:**

**Note:** If time entry exports are too large, the file may become corrupted. Time entry data may have to be exported in smaller batches.

1. Click on **export** in the main menu.
2. Select **Export** **to Excel.**
3. Select **Time** from the dropdown.
4. Select **All** or the date range for the data.
5. Click **Export.**

**Expense entries:**

1. Click on **export** in the main menu.
2. Select **Export to Excel.**
3. Select **Expenses** from the dropdown.
4. Select **All** or the date range for the data.
5. Click **Export.**

## TimeSlips

What can I migrate? How do I migrate my data?

- Contacts
- Matters (derived from the client list)
- Unbilled Time Entries
- Unbilled Expense Entries
- Outstanding balances (a single line item that represents the summative balance at time of export for a matter)
- Trust Balances (a single line item that represents the balance at time of export for a matter or contact)

**Note:** You can only export from TimeSlips if you are operating a version of a program from 2006 or later.

**Contacts and matters:**

1. Click **Reports** > **Clients.**
2. Click the **+** sign in the top right of the dialogue box.
3. Click **Add a specific standard report to the report list**.
4. Select the **Client Info Listing** report and then click **Next.**
5. Click **Next.**
6. Click **Open Report Entry** and then click **Next.**
7. Double click **Client Classification** and filter for open, closed, or inactive records as needed.
8. Click Options and confirm that all the boxes are checked.
9. Click **Print to,** select Microsoft Excel File and then click **Print**.
10. Check the box for **Include column titles** and then click **OK**.
    - The excel file will automatically open after the export. Once opened, save the file in .xls format.

**Unbilled time and expense entries:**

1. Click **Reports****.**
2. Click the **+** sign in the top right of the dialogue box.
3. Click **Add a specific standard report to the report list**.
4. Select the **Slip Listing** report and then click **Next.**
5. Click **Next.**
6. Click **Open Report Entry** and then click **Next.**
7. Select **Slips** from **Filter Groups**.
8. Double click **Slip Billed** and set it to **No**.
9. Click **Print to,** select Microsoft Excel File and then click **Print**.
10. Check the box for **Include column titles** and then click **OK**.
    - The excel file will automatically open after the export. Once opened, save the file in .xls format.

**Outstanding balances:**

1. Click **Reports****.**
2. Click the **+** sign in the top right of the dialogue box.
3. Click **Add a specific standard report to the report list**.
4. Select the **Aged AR Balances By Date** report and then click **Next.**
5. Click **Next.**
6. Click **Open Report Entry** and then click **Next.**
7. Click **Print to,** select Microsoft Excel File and then click **Print**.
8. Check the box for **Include column titles** and then click **OK**.
   - The excel file will automatically open after the export. Once opened, save the file in .xls format.

**Trust balances:**

1. Click **Reports****.**
2. Click the **+** sign in the top right of the dialogue box.
3. Click **Add a specific standard report to the report list**.
4. Select the **Funds Account Listing** or **Funds with Running Balances** report and then click **Next.**
5. Click **Next.**
6. Click **Open Report Entry** and then click **Next.**
7. Click **Print to,** select Microsoft Excel File and then click **Print**.
8. Check the box for **Include column titles** and then click **OK**.
   - The excel file will automatically open after the export. Once opened, save the file in .xls format.

## TimeSolv

What can I migrate? How do I migrate my data?

- Contacts
- Matters
- Contact Notes
- Matter Notes
- Unbilled Time Entries
- Unbilled Expense Entries
- Outstanding Balances (a single line item that represents the balance at the time of export for a matter)

**Note:** Depending on the quality of your data, we may also be able to migrate accounts receivables. Accounts Receivables are derived from the Invoice.csv file with "Unpaid" status and may not accurately provide a true outstanding balance as payments are not being applied to these amounts. In addition, we cannot bring in outstanding balances when multiple matters are being invoiced on one bill. These need to be entered into Clio manually to each matter by following these instructions in the **Manually import outstanding balances** tab of [this article](https://help.clio.com/hc/en-us/articles/9228623050139-Migration-Templates-for-Importing-Into-Clio#import-balances-forward-outstanding-balances--0-9).

**Contacts:**

1. Open TimeSolv.
2. Hover over the **Account** tab at the top of the screen and click **Import/Export** from the menu.
3. Select the **Export Excel** subtab.
4. Select **Client** from the dropdown menu.
5. Click **Export.**
6. Repeat the above steps to download the **Client Note** and **Client/Matter contact** options from the dropdown menu as well.

**Matters:**

1. Open TimeSolv.
2. Hover over the **Account** tab at the top of the screen and click **Import/Export** from the menu.
3. Select the **Export Excel** subtab.
4. Select **Matter** from the dropdown menu.
5. Click **Export.**
6. Repeat the above steps to download the **Matter Notes** options from the dropdown menu as well.

**Expense entries:**

1. Open TimeSolv.
2. Hover over the **Account** tab at the top of the screen and click **Import/Export** from the menu.
3. Select the **Export Excel** subtab.
4. Select **Expenses** from the dropdown menu.
5. Select a date range, if applicable. If left blank, all expense entries will be exported.
6. Select **Unbilled** for status.
7. Click **Export.**

**Time entries:**

1. Open TimeSolv.
2. Hover over the **Account** tab at the top of the screen and click **Import/Export** from the menu.
3. Select the **Export Excel** subtab.
4. Select **Time** from the dropdown menu.
5. Select a date range, if applicable. If left blank, all expense entries will be exported.
6. Select **Unbilled** for status.
7. Click **Export.**
8. Repeat the above steps to download the **Task Codes** option from the dropdown menu as well.

**Outstanding balances:**

1. Open TimeSolv.
2. Navigate to the **Reports** tab at the top of the screen.
3. Scroll down to the **Aged Invoices.**
4. Select **csv** as the format the dropdown menu and click **Export.**

## Total Attorneys

What can I migrate? How do I migrate my data?

- Contacts

1. Click **Contacts.**
2. At the bottom of the screen, click **Export to Excel**.

## 

## TrialWorks

What can I migrate? How do I migrate my data?

**Note:** Data types with an asterisk (\*) require a backup from TrialWorks and are subject to review for data quality. See **Option 1** under "How do I migrate my data?" for more information.

- Contacts
- Matters
- Related Contacts\*
- Matter Notes\*
- Tasks\*
- Calendar Entries\*
- Unbilled Time Entries\*
- Unbilled Expense Entries\*
- Email Communication\*

There are two methods for exporting data from Trial Works: by requesting a backup from their database and accessing the backup using Microsoft SQL Server Management Studio Express (option 1), or by exporting using their reports functionality to export contacts, clients, and matters (option 2).

**Option 1**

**Step 1: Contact TrialWorks to request a backup of the [TrialWorks database](http://wiki.trialworks.com/index.php?title=TrialWorks_Data_Protection_and_Backup).**

**Step 2: Follow these steps to access the data in your backup:**

1. Open [SQL Server Management Studio Express](https://learn.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms?view=sql-server-2017) and connect to the SQL server.
2. Expand **Databases**.
3. Right-click on the database you want to back up, and then select **Tasks > Back up** (this is not available for version 2018/2019).
4. On the **Back Up Database** window, make sure the **Database** field contains the name of the database you want to back up.
5. Select **Full** for the **Backup Type**.
6. Click **Remove**to remove the default/last backup file name.
7. Click **Add**to open the **Select Backup Destination** window.
8. Click **[...]**next to the **File Name** field.
9. On the **Locate Database Files** window, select the folder where you want the backup file to go. By default, it is **..\Microsoft SQL Server\MSSQL.1\MSSQL\Backup**.
10. In the **File Name** field, type the name for this backup, with a **.bak**extension. For example, **xyz\_20080221.bak** for a backup of the XYZ database created on 21 February 2008.
11. Click **OK** to close the **Locate Database Files** window.
12. Click **OK** to close the **Select Backup Destination** window.
13. Click **OK**to start the backup. The progress icon displays in the lower-left corner, and a **completed successfully** message displays when it is done.

**Option 2**

**Export contacts:**

1. Click **Reports** in the menu bar and select **Report Writer** to open the **Custom Report Export** window.
2. Click **Edit Queries…**
3. In the **Query/Filter Name** enter an export name. E.g. **Clio Export Contacts**.
4. Select **Contacts Table** for the **Table Name**.
5. Add a new row for each field you want to include in the report:
   - Select the **FieldNam**e that you would like included in the export.
   - Select **SHOW** for the **Condition.**
6. Click the **Exit.**
7. In the **Export Format**, select **Excel** and click **Export.** Save the file when the report opens in Excel.

**Export clients:**

1. Click **Reports** in the menu bar and select **Report Writer** to open the **Custom Report Export** window.
2. Click **Edit Queries…**
3. In the **Query/Filter Name** enter an export name. E.g. **Clio Export Clients**.
4. Select **Clients Table** for the **Table Name**.
5. Add a new row for each field you want to include in the report:
   - Select the **FieldNam**e that you would like included in the export.
   - Select **SHOW** for the **Condition.**
6. Click the **Exit.**
7. In the **Export Format**, select **Excel** and click **Export.** Save the file when the report opens in Excel.

**Export matters:**

1. Click **Reports** in the menu bar and select **Report Writer** to open the **Custom Report Export** window.
2. Click **Edit Queries…**
3. In the **Query/Filter Name** enter an export name. E.g. **Clio Export Matters**.
4. Select **Matters Table** for the **Table Name**.
5. Add a new row for each field you want to include in the report:
   - Select the **FieldNam**e that you would like included in the export.
   - Select **SHOW** for the **Condition.**
6. Click the **Exit.**
7. In the **Export Format**, select **Excel** and click **Export.** Save the file when the report opens in Excel.

## TurboLaw

What can I migrate? How do I migrate my data?

- Contacts

1. Click **Reports** and select the report in **Type of Report.**
2. In **Date Range**, select **All Time.**
3. In **Grouping**, select **Don’t Group, Just List Everything.**
4. Click **Save/Export.**
5. Select **Save as CSV File.**

## Tussman

What can I migrate? How do I migrate my data?

- Contacts
- Matters

1. Go to **Tools** > **List Users Currently Logged On.**
2. Ensure that no other users are logged into the program.
3. Go to **Tools** > **Backup/Restore Data.**
4. Backup your Tussman data.
5. Go to **Clients** > **Label and Export.**
6. Modify selections under the **Include (Y/N)** section if needed.
7. Choose **CSV File Export.**
8. Select any relevant fields and click **OK.**
9. Repeat steps 5 to 8 for matters.

## ULaw

What can I migrate? How do I migrate my data?

- Contacts
- Matters (limited)

**Contacts:**

1. Click **Contacts.**
2. Select **All Contacts.**
3. Click **Export** and select **CSV.**

**Matters:**

1. Click **Quick View.**
2. Set the filter to **All Matters.**
3. Click **Export** and select **CSV.**

## Verdict

What can I migrate? How do I migrate my data?

- Contacts
- Matters
- Accounts receivable balances

1. Go to the file server that Verdict is on.
2. Locate the folder that says **Verdict.**
3. Within the **Verdict** folder, find the **veacct.dbf** file and the **veclient.dbf** file and save a copy of both.
   - Both .dbf files will need to be opened in Open Office to convert them into CSV for processing.

## 

## WealthCounsel

What can I migrate? How do I migrate my data?

- Contacts

1. Click **CONTACTS** from the **MY PRACTICE** menu.
2. Click **MORE**, and then click **Export Contacts.**

## Zoho

What can I migrate? How do I migrate my data?

- Contacts
- Matters
- Notes

1. Log in to Zoho.
2. Click **Setup** > **Data Administration** > **Export.**
3. Go to the **Export Data** page.
4. From the Select Export Module list, select the modules from which you want to export data from. **Leads, Vendors, Customers** are modules you will likely want to export.
5. Click **Export.**
6. Repeat until all desired modules are exported from.

**Note:** There is a limit of 3000 records when exporting. This will affect items such as notes and emails. You can also request a full backup of your data from Zoho to receive all records.

## 17Hats

What can I migrate? How do I migrate my data?

- Contacts

1. Navigate to the **Contacts** tab on the left windowpane.
2. Filter contacts to include **All, Clients, Leads** and **Archived** contacts.
3. Click the gear icon next to the filter options.
4. Click **Export Contacts.** A csv file will download.