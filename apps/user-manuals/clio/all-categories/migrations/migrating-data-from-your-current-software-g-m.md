# Migrating Data From Your Current Software [G-M]

Source: https://help.clio.com/hc/en-us/articles/10263146574107-Migrating-Data-From-Your-Current-Software-G-M

---

This article explains what data can be migrated from your current practice management software and how to export the data from that software. Software applications starting with the letters H, I, J, L, and M are listed below.

**Tip:** See one of the articles below if your current practice management software does not start with the letters H, I, J, L, or M .

- [Migrating Data From Your Current Software [A-B]](https://help.clio.com/hc/en-us/articles/9813809475995)
- [Migrating Data From Your Current Software [C-F]](https://help.clio.com/hc/en-us/articles/10263045235867)
- [Migrating Data From Your Current Software [N-S]](https://help.clio.com/hc/en-us/articles/9815681343003)
- [Migrating Data From Your Current Software [T-Z]](https://help.clio.com/hc/en-us/articles/9812890677531)

## Harvest

What can I migrate? How do I migrate my data?

- Contacts
- Matters
- Unbilled Time Entries
- Unbilled Expense Entries

**Contacts**

1. Navigate to the **Manage**s ection.
2. Click **Export**at the top of the page.

**Matters**

1. Navigate to the **Projects** section.
2. Click **Export** at the top of the page.

**Time entries**

1. Go to the **Reports** section.
2. Click **Detailed Time**.
3. Change filters to **All Time** and select **Include archived items in filters**.
4. Click **Run Detailed Time Report**.
5. Click **Export** at the top of the page and choose CSV.

**Expenses**

1. Go to the **Reports** section.
2. Click **Detailed Expenses**
3. Change filters to **All Time** and select **Include archived items in filters**.
4. Click **Run Detailed Expense Report**.
5. Click **Export** at the top of the page and choose CSV.

## Highrise

What can I migrate? How do I migrate my data?

- Contacts

1. Click the **Contacts** page link.
2. Click the **Export** link in the sidebar.
   - If you do not see an **Export** link, this means that you do not have export permissions enabled. Ask your account owner or an administrator to update your permissions to enable exporting.
3. Select the type of export you want. CSV format is recommended.
   - If you export less than 100 contacts, an automatic file download will begin.
   - If you export more than 100 contacts, Highrise will send you an email with the file once the export is complete.

## HoudiniEsq

What can I migrate? How do I migrate my data?

- Contacts
- Matters

**Contacts**

1. Go to the **Contacts** tab.
2. Choose the **Filter** symbol on the left side of the screen.
3. Click **CSV**.
4. Click **Export**.
5. Wait until you are prompted to download the file.

**Matters**

1. Go to the **Matters** tab.
2. Choose the **Filter** symbol on the left side of the screen.
3. Click **CSV**.
4. Click **Export**.
5. Wait until you are prompted to download the file.

## Hubspot

What can I migrate? How do I migrate my data?

- Contacts
- Deals as matters

**Contacts**

1. Hover over **CRM** on the left-hand side bar, then click **Contacts**.
2. Click **Export**.
3. Remove all filter to ensure a full export.
4. Click Export.

**Matters**

Deals in Hubspot can be imported as matters.

1. Hover over **CRM** on the left-hand side bar, then click **Deals**.
2. Click **Export**.

**Note:** Deals cannot be matched to contacts so the client will have to fill in a first and last name to the matter

## Infusion (Keap, InfusionSoft)

What can I migrate? How do I migrate my data?

- Contacts
- Matters (derived from contacts)

1. Click the three horizontal lines on the top left of the page and select **Contacts**.
2. Filter the contacts to include **Clients** or **Entire Contacts**.
3. Click **Actions** on the mid left of the page and select **Export**.
4. Choose columns that needs to be exported.
5. For the **Delivery method** of the exported data select **View in browser/download** or **Email**.
6. Select the file type for export.
7. Click **Process** and then click **Okay** to continue.
8. Save the CSV file to your computer or find it in your email inbox.

## Insightly

What can I migrate? How do I migrate my data?

- Contacts
- Matters
- Tasks
- Notes

You can export data from all tabs (all of the records of a certain type, such as contacts or organizations) or a subset of data from a tab. Additionally, users must have export permissions to perform these exports. Insightly admins can access this setting by clicking **Profile icon** > **System Settings** > **Users** and checking the box next to **Data Export Enabled** for a user.

**Export data from all tabs:**

1. From the left navigation bar, select the page you would like to export records from (Contacts, Organizations, Opportunities, Projects, or Tasks).
2. Select **type**.
3. On the right sidebar, click the **Export** link.
4. **For *contacts and organizations records:*** You will be presented with another page of options to select from. Click the appropriate link for exporting contacts, organizations, or their notes.
5. The export will produce a CSV file that you can save from your browser. You can rename the file and choose a folder to save it to.
6. Repeat these steps for each category where you have data to export.

**Export a subset of data from a tab:**

1. Select the page you would like to export records from (Contacts, Organizations, Opportunities, Projects, or Tasks).
2. Narrow down the list of records by using one of the following methods:
   - Choose an option from the **Filter** or **View** lists above the records (this is the only option for tasks).
   - Select from the tag list in the right sidebar.
   - Create a custom filter.
3. Click the checkbox above the records. This will select all the visible records.
4. Click **More** above the list, and then click **Export**. Your browser will save the file to your computer.

## INSZoom

What can I migrate? How do I migrate my data?

- Contacts
- Matters

**Contacts**

1. Log in to INSZoom.
2. Select **Reports** in the left navigation bar.
3. Select **Reports 1.0**.
4. Select **Adhoc Reports** from the list of reports. If you do not see **Adhoc Reports** in the list, you may need to contact INSZoom to request access to the Adhoc reporting functionality.
5. Select **Add Template**.
6. Enter a name for the template (e.g. Clio Contact Export) and save.
7. Add the **Input Columns**. There is a maximum of 100 columns per report. These are the columns you will use as filters:
   - Select **Attach/Remove Columns** above the **Input Columns** box.
   - Choose **Client** from the **Find In** dropdown.
   - Choose the columns in the **Removed Columns** list on the left side.
   - Select **Add** to move them to the **Attached Columns** list on the right side.
   - Select **Save**.
8. Add the **Export Columns**. There is a maximum of 100 columns per report. These are the columns that will be exported for the contact:  
   - Select **Attach/Remove Columns** above the **Output Columns** box.
   - Choose **Client** from the **Find In** dropdown.
   - Choose the columns in the **Removed Columns** list on the left side. Include **Client ID** in order to link the contact to the matter.
   - Select **Add** to move them to the **Attached Columns** list on the right side.
   - Select **Save**.
9. Run the report.
10. Select the value(s) for the **Input Columns** you added to filter the report accordingly.
11. Select **Get Report**. Check that popups are not blocked.
12. Select **Click Here to download the report as an excel/csv file** from the popup window.

**Matters**

1. Log in to INSZoom.
2. Select **Reports** in the left navigation bar.
3. Select **Reports 1.0**.
4. Select **Adhoc Reports** from the list of reports. If you do not see **Adhoc Reports** in the list, you may need to contact INSZoom to request access to the Adhoc reporting functionality.
5. Select **Add Template**.
6. Enter a name for the template (e.g. Clio Matter Export) and save.
7. Add the **Input Columns**. There is a maximum of 100 columns per report. These are the columns you will use as filters:  
   - Select **Attach/Remove Columns** above the **Input Columns** box
   - Choose **Case** from the **Find In** dropdown.
   - Choose the columns in the **Removed Columns** list on the left side.
   - Select **Add** to move them to the **Attached Columns** list on the right side.
   - Select **Save**.
8. Add the **Export Columns**. There is a maximum of 100 columns per report. These are the columns that will be exported for the contact:
   - Select **Attach/Remove Columns** above the **Input Columns** box
   - Choose **Case** from the **Find In** dropdown.
   - Choose the columns in the **Removed Columns** list on the left side. Include **Client ID** in order to link the contact to the matter.
   - Select **Add** to move them to the **Attached Columns** list on the right side.
   - Select **Save**.
9. Run the report.
10. Select the value(s) for the **Input Columns** you added to filter the report accordingly.
11. Select **Get Report**. Check that popups are not blocked.
12. Select **Click Here to download the report as an excel/csv file** from the popup window.

## Interbill

At this time there is no option to export usable format from Interbill for migration data. The **Export/Import** option has been known to completely remove data from the database, rather than make a copy. We recommend not using this option without assistance from Interbill support.

## Juris

What can I migrate? How do I migrate my data?

- Contacts
- Matters
- Unbilled Time Entries
- Unbilled Expense Entries
- Outstanding Balance (a single line item that represents the summative balance at time of export for a matter)

There are two options for backing up Juris data. See the steps below for more information.

- **[Juris Management Console Backup](https://lexisnexis.custhelp.com/app/answers/answer_view/a_id/1086069)**
- **[Backing up Juris using SQL Server management Studio](https://lexisnexis.custhelp.com/app/answers/answer_view/a_id/1092958)**

**Note:** All users will need to be logged out of Juris for the backup.

**Option 1: [Juris Management Console Backup](https://lexisnexis.custhelp.com/app/answers/answer_view/a_id/1086069)**

Juris backups include Juris Suite time and expense entries that have been synchronized with the server, as indicated with an entry key within the grid. Time and expense entries stored only in the local cache file (not synchronized) are not included in the backup. Additionally, backing up via Juris Management Console also shrinks the LDF file upon completion. Follow these steps to create a backup using the Juris Management Console (JMC):

1. Verify that all users have closed Juris.
2. Click the **Start** button on the **Windows Taskbar**.
3. Select **Programs** > **Juris** > **Administrative Tools** > **Juris Management Console** to the open the Juris Management Console window.
4. Double-click **Juris Management Console** to expand the folder in the **Juris Console** list.
5. Double-click **[Your Firms Name] Data** to expand the folder.
6. Right-click the **Database** folder and select **All Tasks** and then **Backup** to open the **Juris Backup** wizard.
7. Click the **Right Arrow** button once.
8. Select **New Backup** from the **Backup Device** list.
9. Enter the **Name of your backup** in the **Name** field. For example you can enter Monday, Tuesday, Wednesday, or End of year as the name of your backup file.
10. Click to check the **File** radial box to enter a destination path for saving your backup.
11. Click the ellipsis button to open the **Browse for location of Backup file** window.
12. Select the folder you want to save your backup to. The file path needs to reside on the server and not on the local workstation.
13. Click **OK** to return to the **Add New Backup Device** window.
14. Enter \**[Name of your backup].bak** at the end of the destination path in the **File** field. The [Name of your backup] is the same name as you entered for step 9.
15. Click **OK**.
16. Click the **Right Arrow** button once.
17. Click the **Right Arrow** button to open the **Backup Confirmation** window and do not change the **Media Name** field. The Media Name field is populated from the **Windows System Clock**.
18. Click **Finish** to backup Juris.
19. Click the **X** to close the **Juris Management Console**.

**Option 2:** **[Backing up Juris using SQL Server management Studio](https://lexisnexis.custhelp.com/app/answers/answer_view/a_id/1092958)**

Follow these steps to backup your Juris data using the SQL Server Management Studio:

1. Verify that all users have closed the Juris program.
2. Place Juris in [Maintenance or Backup](https://lexisnexis.custhelp.com/app/answers/answer_view/a_id/1074795) mode depending on reason for backup.
3. Click **Start** and select **Programs** > **Microsoft SQL Server** > **SQL Server Management Studio** to the open the **Microsoft SQL Server Management Studio** window.
4. Log in with your credentials.
5. Click next to **Databases** to expand it.
6. Right-click **Juris [ your client code ]** and select **Tasks**, and then **Back Up..**. to open the **Back Up Database - Juris[ your client code ]**window.
7. Select **Full** from the **Backup type:** dropdown list.
8. Enter the**[ Name of your backup ]** in the **Name** field.
9. Click **Add...** to open the **Select Backup Destination** window.
10. Click the ellipsis button to the right of the **File name** field to open the **Locate Database Files** window.
11. Click to select the folder where you want to save your backup.
12. Enter the**[ Name of your backup ].bak** in the **File name** field and click **OK**.
13. Click **OK** on the **Select Backup Destination** window.
14. Click **OK** on the **Back Up Database - Juris [ your client code ]** window to start the backup.
15. Click **OK** on the **Microsoft SQL Server Management Studio The backup of database 'Juris[ your client code ]' completed successfully** window.
16. Right-click **JBills[ your client code ]** and select **Tasks**, and then **Back Up...** to open the **Back Up Database - JBills[ your client code ]** window.
17. Select **Full** from the **Backup type** dropdown list.
18. Enter the **[ name of your backup ]** in the **Name** field. Use the same **Backup set Name** that you used for **Juris[ your client code ]**to append the **JBills** database backup to the **Juris** database backup.
19. Click **Add...** to open the **Select Backup Destination** window.
20. Click the **ellipsis** button to the right of the **File name** field to open the **Locate Database Files** window.
21. Click to select the folder where you want to save your backup. Use the same destination file that you used for**Juris[ your client code ]**to append the JBills database backup to the **Juris** database backup.
22. Enter the name of your backup in the **File name** field and click **OK**. Use the same **File name** that you used for**Juris[ your client code ]**to append the **JBills** database backup to the **Juris** database backup.
23. Click **OK** on the **Select Backup Destination** window.
24. Click **OK** on the **Back Up Database - JBills[ your client code ]** window to start the backup.
25. Click **OK** on the **Microsoft SQL Server Management Studio The backup of database 'JBills[ your client code ]' completed successfully** window.
26. Close **Microsoft SQL Server Management Studio**.

## LawBillity

What can I migrate? How do I migrate my data?

**Note:** Confirm your version of LawBillity allows for the export time and expense entries.

- Contacts
- Matters
- Unbilled Time Entries
- Unbilled Expense Entries

1. Go to **Settings**.
2. Scroll to the bottom of the page and select **Export All Data for your Firm**.
3. Once the file is created, select **Click Here to Download**.

## LawCloud

What can I migrate? How do I migrate my data?

- Contacts
- Matters
- Unbilled Time Entries
- Unbilled Expense Entries

You must contact LawCloud to get access to your LawCloud Database ([support@lawware.co.uk](mailto:support@lawware.co.uk)). They will send you an email that contains and encrypted and compressed back up file. The password is your default LawCloud password. Then you can follow the steps below to access your data in your backup. LawCloud may offer to extract the data into a requested format, but the service will incur a fee. If you have any issues with these instructions please contact LawCloud directly.

1. Open [SQL Server Management Studio Express](https://learn.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms?view=sql-server-2017) and connect to the SQL server.
2. Expand **Databases**.
3. Right-click on the database you want to back up, and then select **Tasks > Back up** (this is not available for version 2018/2019).
4. On the **Back Up Database** window, make sure the **Database** field contains the name of the database you want to back up.
5. Select **Full** for the **Backup Type**.
6. Click **Remove** to remove the default/last backup file name.
7. Click **Add** to open the **Select Backup Destination** window.
8. Click **[...]** next to the **File Name** field.
9. On the **Locate Database Files** window, select the folder where you want the backup file to go. By default, it is **..\Microsoft SQL Server\MSSQL.1\MSSQL\Backup**.
10. In the **File Name** field, type the name for this backup, with a **.bak** extension. For example, **xyz\_20080221.bak** for a backup of the XYZ database created on 21 February 2008.
11. Click **OK** to close the **Locate Database Files** window.
12. Click **OK** to close the **Select Backup Destination** window.
13. Click **OK**to start the backup. The progress icon displays in the lower-left corner, and a **completed successfully** message displays when it is done.

## Lawcus

What can I migrate? How do I migrate my data?

- Contacts
- Matters
- Unbilled Time Entries
- Unbilled Expense Entries

**Contacts (clients)**

1. Click **User Profile** in the upper right corner and then select **Settings**.
2. Click **Apps & Integrations** and then select **Export and Import**.
3. Select **Clients** > **Export** > **Exported Contacts**.
   - Exported clients will be in .xlsx format.

**Matters (cases)**

1. Click **User Profile** in the upper right corner and then select **Settings**.
2. Click **Apps & Integrations** and then select **Export and Import**.
3. Select **Matters** > **Export**.
4. Check the box for all open matters and all closed matters and then click **Export Matters**.
   - Exported matters will be in .xlsx format.

**Unbilled time entries**

Your firm must confirm which time entries are unbilled before the export.

1. Click **User Profile** in the upper right corner and then select **Settings**.
2. Click **Apps & Integrations** and then select **Export and Import**.
3. Select **Time Entries** > **Export**.
   - Exported time entries will be in .xlsx format.

**Unbilled expenses**

Your firm must confirm which expenses are unbilled before the export.

1. Click **User Profile** in the upper right corner and then select **Settings**.
2. Click **Apps & Integrations** and then select **Export and Import**.
3. Select **Expenses** > **Export**.
   - Exported expenses will be in .xlsx format.

**To create a full backup**

1. Click **User Profile** in the upper right corner and then select **Settings**.
2. Click **Apps & Integrations** and then select **Export and Import**.
3. Select **Full Back Up** > **Export** > **Create Full Backup**.
   - Exported backup will be in a zipped folder.

## LawLogix

What can I migrate? How do I migrate my data?

- Contacts
- Matters
- Notes
- Accounts receivable balances

1. In the navigation menu on the left, click **Reports**.
2. Add a new template.
3. Select the relevant report from the dropdown and then select **yes** under **Holiday Card Recipient**, otherwise the report will not show any results.
4. Select all of the report column tabs.

## LeanLaw

What can I migrate? How do I migrate my data?

- Contacts
- Matters
- Unbilled Time Entries
- Unbilled Expense Entries
- Outstanding Balance (a single line item that represents the summative balance at time of export for a matter)

1. Sign in to your LeanLaw account.
2. Click **Settings**.
3. Click **Firm Info**.
4. Click **Download Firm Data**.

## LEAP

What can I migrate? How do I migrate my data?

- Contacts
- Matters
- Unbilled Time Entries
- Unbilled Expense Entries
- Outstanding Balances (a single line item that represents the summative balance at the time of export for a matter)
- Trust Balances (a single line item that represents the balance at time of export for a matter or contact)

**Contacts (Clients)**

1. Go to **Reports**. The report will open in a new browser window.
2. Select **Matters and Clients** at the top of the page.
3. Select **Client and Cards**.
4. Select **Client Detail**.
5. Under **Card Type,** click **Select** **All**.
6. Remove the filter for **Creation Date**.
7. Click **Search**.
8. Change **Selected Cards** to **All Cards** and **Excel** to **CSV** for file output.
9. Select **Download**.

**Matters**

1. Go to **Reports.**The report will open in a new browser window.
2. Select **Matters and Clients** at the top of the page.
3. Select **Matter List**.
4. Update the **Start Date** and **End Date** to capture all matters.
5. Select the following filters:
   - **Matter Status** > **Select All**
   - **Matter Type** > **Select All**
   - **Include Inactive Staff** > **Yes**
   - **Include Archived Matters** > **Yes**
   - **Group by** > **Staff Responsible**.
6. Click **View**.
7. Export as **Excel Worksheet**.

**Unbilled time entries (Desktop App)**

You can export up to five years of unbilled time entries from the LEAP desktop app using the steps below.

1. Go to **Menu** > **Accounting**
2. Select **Time and Fees Report**
3. Apply the following filters:

   - De-select **Billed**
   - Select **Bill Later** and **Bill Next Invoice**
   - Do not select **Non-billable**. If you need to export non-billable unbilled time entries, generate separate reports for billable and non-billable time.
   - Select **All Billable**
   - Select **Time** and set the required timeframe.
4. Click **Submit**
5. Click the **print** icon on the top bar
6. Select **Excel** for file output and click **Download**

**Unbilled time entries (Web App)**

1. Go to **Menu** > **Accounting**
2. Select **Time and Fees**
3. Select **All Billable**.
   - For the **Date Range,** export time entries 1 year at a time.
4. Toggle **Excel** to **CSV** for file output.
5. Select **Download**.

**Unbilled expense entries**

1. Go to **Menu >** **Reports**.
2. Select **Office** > **Aged Expenses Repor**t.
3. Select the following filters:
   - **Matter Status** > **Select All**
   - **Include Inactive Staff** > **Yes**
4. Click **View**.
5. Under **Export type**, select **Excel Worksheet**.
6. Click **Export All**

**Accounts receivable balances**

Export the accounts receivable report and aged debtors report.

Accounts receivable report

1. Go to **Menu** > **Reports**.
2. Select **Operating Account** > **Accounts Receivable**.
3. Click **Print** and select **Export to Excel**.

Aged debtors report

1. Go to **Menu** > **Reports**.
2. Select **Office** > **Aged Debtors Report**
3. Click **Print** and select **Export to Excel**.

**Client Account Balances**

1. Go to **Menu >** **Reports**.
2. Select **Office** > **Matter Balances**.
3. Click **Print** and select **Export to Excel**.

**Trust balances**

1. Go to **Menu >** **Reports**.
2. Select **Trust** > **Trust Trial Balance**.
3. Click **Print** and select **Export to Excel**.

## LegalMaster

What can I migrate? How do I migrate my data?

**What**

- Contacts
- Matters
- Outstanding Balances(a single line item that represents the summative balance at the time of export for a matter)

1. In LegalMaster, go to **Reports** and select **Add**.
2. Click **Print**, select **Data**, and add extensions to the file.

## Legal Files

What can I migrate? How do I migrate my data?

- Contacts
- Matters
- Related contacts
- Notes

1. Open [SQL Server Management Studio Express](https://learn.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms?view=sql-server-2017) and connect to the SQL server.
2. Expand **Databases**.
3. Right-click on the database you want to back up, and then select **Tasks > Back up** (this is not available for version 2018/2019).
4. On the **Back Up Database** window, make sure the **Database** field contains the name of the database you want to back up.
5. Select **Full** for the **Backup Type**.
6. Click **Remove** to remove the default/last backup file name.
7. Click **Add** to open the **Select Backup Destination** window.
8. Click **[...]**next to the **File Name** field.
9. On the **Locate Database Files** window, select the folder where you want the backup file to go. By default, it is **..\Microsoft SQL Server\MSSQL.1\MSSQL\Backup**.
10. In the **File Name** field, type the name for this backup, with a **.bak** extension. For example, **xyz\_20080221.bak** for a backup of the XYZ database created on 21 February 2008.
11. Click **OK** to close the **Locate Database Files** window.
12. Click **OK** to close the **Select Backup Destination** window.
13. Click **OK** to start the backup. The progress icon displays in the lower-left corner, and a **completed successfully** message displays when it is done.

## LollyLaw

What can I migrate? How do I migrate my data?

- Contacts

**Note:** LollyLaw has additional reports that can be run, but these reports only provide segmented information that is not sufficient for migrating data. For instance, a report on only certain matter types can be exported at a time, while a full listing of ALL matters is required for migrating them. In addition, a "notes" report only provides one note per export, but a listing of ALL notes linked to the case or contact is required for migrating.

1. Select **Settings**.
2. Click **Export**.
3. Select **Download All Contacts in Account**. An email will be sent to the account owner with the download file.

## Mattero

What can I migrate?How do I migrate my data?

- Contacts
- Matters
- Matter Notes
- Unbilled Time Entries

**Note:** Clio may be able to export tasks, unbilled time entries, and unbilled expenses depending on the data export.

1. Contact Mattero support and request a backup.

## MerusCase

What can I migrate? How do I migrate my data?

- Contacts
- Matters

**Contacts**

1. Open Merus Case
2. Navigate to **Contact Listing** page.
3. Hold down **SHIFT+6** to show entire contact listing list.
4. At the top right of the table, select **Export to Excel**.

**Matters**

1. Open Merus Case
2. Navigate to **Cases** on top left.
3. Click on **Browse Cases**.
4. Select **Open** or **Closed** cases.
5. Navigate to the printer symbol on top right and select **Export to Excel**.

## MinuteDock

What can I migrate? How do I migrate my data?

- Contacts
- Matters
- Matter Notes
- Unbilled Time Entries
- Outstanding (a single line item that represents the summative balance at time of export for a matter)

There are no export instructions at this time.

## 

## MyCase

What can I migrate? How do I migrate my data?

- Contacts
- Matters
- Contact Notes
- Matter Notes
- Tasks
- Unbilled Time Entries
- Unbilled Expense Entries
- Phone Communications
- Calendar Events
- Outstanding Balances (a single line item that represents the summative balance at time of export for a matter)
- Trust Balances (a single line item that represents the balance at time of export for a matter or contact)

**Note:** We cannot import emails because they cannot be exported properly from My Case.

1. Click your name and select **Settings**.
2. Click **All Settings**.
3. Click **Import/Export**and select the **Full Backup** subtab.
4. Click **Create Backup**.
5. Under **cases**, check the box for **All Firm Cases**.
6. Under **options,** click to check the box for **Include Archived Items**.
7. Click **Create Backup**.

**Trust balances**

1. Click **Reports** > **Trust Account Summary**.
2. Uncheck **Include contacts with $0 balances**.
3. Click **Export** and then save in csv format.

## My Invoice Estimates Deluxe 10.0

What can I migrate? How do I migrate my data?

- Contacts
- Matters

1. Click **Run Reports**.
2. Generate the **Accounts Receivable** report.
3. Click **Save** and then save as **CSV**.
4. Repeat steps 2 and 3 to generate the **Custom List** report.