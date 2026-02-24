# Migrating Data From Your Current Software [N-S]

Source: https://help.clio.com/hc/en-us/articles/9815681343003-Migrating-Data-From-Your-Current-Software-N-S

---

This article explains what data can be migrated from your current practice management software and how to export the data from that software. Software applications starting with the letters N, O, P, Q, R, and S are listed below.

**Tip:** See one of the articles below if your current practice management software does not start with the letters N, O, P, Q, R, and S.

- [Migrating Data From Your Current Software [A-B]](https://help.clio.com/hc/en-us/articles/9813809475995)
- [Migrating Data From Your Current Software [C-F]](https://help.clio.com/hc/en-us/articles/10263045235867)
- [Migrating Data From Your Current Software [G-M]](https://help.clio.com/hc/en-us/articles/10263146574107)
- [Migrating Data From Your Current Software [T-Z]](https://help.clio.com/hc/en-us/articles/9812890677531)

## Needles

What can I migrate? How do I migrate my data?

- Contacts
- Matters
- Matter notes
- Tasks
- Calendar Events

Follow the steps below for contacts, matters, and matter notes. Alternatively, pull data from a full database backup (Needles.db and Needles.log files).

**Backup Needle:**

1. Open the **Needles Backup Coordinator**.
2. Click **Start** and then **Programs**.
3. Select **Needles Backup**.
   - You can also open the **Needles Backup Coordinator** desktop app if available.

**Matters:**

1. Go to **Reports** and select **Case Information**.
2. Click **Case Listings**.
3. Select **Party Name**.
4. Select **Status.** The report will appear in the product.
5. Click the print button at the top of screen to print to PDF.
6. Check **Print to file**.
7. Select **Print**.
8. Save under **Excel with headings**.

**Contacts:**

1. Go to **Reports** and select **Mailing Labels**. The report will appear in the product.
2. Click the print button at the top of screen to print to PDF.
3. Check **Print to file**.
4. Select **Print**.
5. Save under **Excel with headings**.

**Matter notes:**

1. Go to **Reports** and select**Case Notes**. The report will appear in the product
2. Click the print button at the top of screen to print to PDF.
3. Check **Print to file**.
4. Select **Print**.
5. Save under **Excel with headings**.

## Orion

What can I migrate? How do I migrate my data?

- Contacts
- Matters

**Note:** The exports will not format headers properly. You will need to export the client and matter listings in PDF format to manually adjust headers.

**Contacts:**

1. Open Orion.
2. On the left side panel, navigate to **Desktop > Reports**.
3. Click **Standard** **Reports** > **File Maintenance**.
4. To export contacts, choose **Client Listing**.
5. Ensure that the **Style** selected is **Details (system)**.
6. Apply any filters under the **Options** section.
7. Choose **Export** > **Excel Data File**. The file will be automatically open after exporting. An error may occur if there is no valid program installed.

**Matters:**

1. Open Orion.
2. On the left side panel, navigate to **Desktop > Reports**.
3. Click **Standard** **Reports** > **File Maintenance**.
4. To export contacts, choose **Matter Listing**.
5. Ensure that the **Style** selected is **Details (system)**.
6. Apply any filters under the **Options** section.
7. Choose **Export** > **Excel Data File**. The file will be automatically open after exporting. An error may occur if there is no valid program installed.

## Osprey

What can I migrate? How do I migrate my data?

- Contacts
- Matters
- Matter Notes

**Step 1: Contact Osprey to get access to your Osprey Database. They will send you three separate emails:**

- The first will contain your Download URL and username to sign in to the backup site.
- The second will include you backup password to sign in to the Backup site.
- The third will include your encryption key to access your extracted database.

**Step 2: Follow the steps in this article:** [Download your Osprey backup](https://support.pracctice.com/guides/download-your-osprey-backup/)

**Step 3: Follow these steps to access the data in your backup:**

1. Open [SQL Server Management Studio Express](https://learn.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms?view=sql-server-2017) and connect to the SQL server.
2. Expand **Databases**.
3. Right-click on the database you want to back up, and then select **Tasks** > **Back up** (this is not available for version 2018/2019).
4. On the **Back Up Database** window, make sure the **Database** field contains the name of the database you want to back up.
5. Select **Full** for the **Backup Type**.
6. Click **Remove** to remove the default/last backup file name.
7. Click **Add** to open the **Select Backup Destination** window.
8. Click **[...]** next to the **File Name** field.
9. On the **Locate Database Files** window, select the folder where you want the backup file to go. By default, it is **..\Microsoft SQL Server\MSSQL.1\MSSQL\Backup**.
10. In the **File Name** field, type the name for this backup, with a **.bak** extension. For example, **xyz\_20080221.bak** for a backup of the XYZ database created on 21 February 2008.
11. Click **OK** to close the **Locate Database Files** window.
12. Click **OK** to close the **Select Backup Destination** window.
13. Click **OK** to start the backup. The progress icon displays in the lower-left corner, and a **completed successfully** message displays when it is done.

## PCLaw

What can I migrate? How do I migrate my data?

- Contacts
- Matters
- Tasks
- Unbilled Time Entries
- Unbilled Expense Entries
- Calendar Events
- Outstanding Balances (a single line item that represents the balance at time of export per matter invoice)
- Trust Balances (a single line item that represents the summative balance at time of export for a Matter or Contact)

**Note:** You are migrating the balance at the time of export as a line item representing outstanding and trust balances.

**User list:**

1. Click **Options** > **Lists** > **Lawyers and Rates**.
2. Select **Include inactive users***.*
3. Click **Print**. If you are prompted to send to the printer change the settings click **File** > **Printer Setup** > **Report** > **Change the printer to Adobe PDF**.
4. Save the PDF file.

**Practice area list:**

1. Click **Options** > **Lists** > **Types of Law**.
2. Click **Print**. If you are prompted to send to the printer change the settings click **File** > **Printer Setup** > **Report** > **Change the printer to Adobe PDF**.
3. Save the PDF file.

**Contacts:**

**Note:** If you need additional fields for contact or matters, check the box next to the fields. These fields will migrate to Clio as custom fields.

1. Go to **File** > **Contact Manager**.
2. Click **Export**.
3. Select **Layout Name** > **All**.
4. Click **Change**.
5. Select the **C****ommon** tab and check boxes for all fields.
6. Click the **Other** tab and check boxes for all fields.
7. Click **Ok**.
8. Under **File Format** select **CSV**.
9. Under **Output File** select **Browse** and pick a destination for saving.
10. Check the boxes for **Contacts**, **Clients**, and **Vendors**, and then click **Export**.
11. Click **Yes** when asked to save changes.
12. Repeat steps 8–11 but select **Word for Windows** as the **File Format**. This will provide you with the headers for the CSV file.

**Open matters:**

**Note:** If you need additional fields for contact or matters, check the box next to the fields. These fields will migrate to Clio as custom fields.

1. Click **File** > **Matter** > **Export**.
2. Select **Layout Name** > **Open Matt**.
3. Click **Change**.
4. Select the **Main** tab and check boxes for all fields except **Disable updates with other software**.
5. Select the **Address** tab and check boxes for all applicable fields.
6. Select the **Selections** tab and check boxes for all fields under **Court** and **File**.
7. Click **OK**.
8. Under **File Format** select **CSV**.
9. Under **Output File** select **Browse** and pick a destination for saving.
10. Leave the **Name** field as **Open Matt**.
11. Click **Export**.
12. Click **Yes** when asked to save changes.
13. Select **Active Cases** only.
14. Click **OK** to start Export.
15. Repeat steps 8-14 but select **Word for Windows** as the **File Format**. This will provide you with the headers for the CSV file.

**Closed matters:**

1. Click **File** > **Matter** > **Export**.
2. Select **Layout Name** > **Open Matt**.
3. Click **Change**.
4. Select the **Main** tab and check boxes for all fields except **Disable updates with other software**.
5. Select the **Address** tab and check boxes for all applicable fields.
6. Select the **Selections** tab and check boxes for all fields under **Court** and **File**.
7. Click **OK**.
8. Under **File Format** select **CSV**.
9. Under **Output File** select **Browse** and pick a destination for saving.
10. Leave the **Name** field as **CloseMat**.
11. Click **Export**.
12. Click **Yes** when asked to save changes.
13. Select **Inactive and/or Archived Cases** only.
14. Click **OK** to start Export.
15. Repeat steps 8–14 but select **Word for Windows** as the **File Format**. This will provide you with the headers for the CSV file.

**Appointments/ToDos:** 

1. Click **Data Entry** > **Register**.
2. Select the **Appointments** tab.
3. Check the box next to **Filters** and click **Filters**.
4. Select the box next to **Uncompleted**.
5. Check that the date range is what you want and click **OK**.
6. Click the **Excel** button.
7. Pick an accessible destination and click **Save**.
8. Repeat **steps 1–7**, and click the **Completed** box in step 4 when complete.

**Unbilled fees (time entries):**

1. Click **Data Entry** > **Register**.
2. Select the **Time** tab.
3. Check the box next to **Filters** and click **Filters**.
4. Select **Unbilled** and click **OK**.
5. Check that the date range is what you want and click **select**.
6. Click the **Excel** button. Filename: **Reg Time [date].xls**.
7. Pick an accessible destination and click **Save**.

**Unbilled disbursements (expense entries):**

1. Click **Reports** > **Client** > **Ledger**.
2. Click the **Matters** subtab or **Advanced** if the Matter tab is not visible.
3. Complete the appropriate fields.
4. Click the **Common** subtab, and select **Adv. Search**.
   - From the drop-down, under **Field**, select **Invoice Number**.
   - Under **Comparison**, select **Is Blank**.
5. Click the **Other** subtab and only leave **Disbs** selected.
6. Click **OK**, and the report will start displaying on the screen. Wait until the report is done. It will show **Report Done** in the bottom left.
7. Click **export to Excel**. Filename: **Client Ledger.xls**.
8. Pick an accessible destination and click **Save**.

**Accounts receivable (outstanding balances):**

1. Click **Reports** > **Journal** > **Billing (Fees) Journal**.
2. On the **Common** subtab select an **End Date**.
3. Uncheck the box for **Include Paid Invoices**.
4. *Optional:* Filter by attorney.
5. Click **ok**. The report will display on the screen.
6. Review the report and once satisfied click **export to Excel**. Filename: **Billing (Fee) Journal.xls**.
7. Pick an accessible destination and click **Save**.

**Trust listings report (trust balances):**

1. Click **Reports**.
2. Select **Client** and then **Trust Listing**.
3. Leave the **Matter**, **Client**, **Acct**, and **Resp Lawyer** boxes blank to run the report for all matters.
4. Enter **12/31/2199** in the **End Date** box to run the report for all dates.
5. Check the **Totals Only** box to only show the client and firm totals, or uncheck the box to also show matter totals.
6. Check the **Firm Totals Only** box to show only firm totals, or uncheck the box to show all matter, client, and firm totals.
7. Check the **Negative Balances Only** box to show only matters with a negative trust balances, or uncheck the box to include all matters with a trust balances.
8. Select **Default** from the **Layout** dropdown.
9. Select **Output options**.
10. Use the **Matters** and **Other** tabs to select additional report options.
    - Click **Advanced** at the bottom of the **Client Trust Listing** window if the **Matters** or **Other** tabs are missing.
11. Click **OK** to generate the report.

## PerfectLaw

What can I migrate? How do I migrate my data?

- Matters
- Contacts
- Related Contacts
- Unbilled Time Entries
- Unbilled Expense Entries
- Phone Communications

1. Open [SQL Server Management Studio Express](https://learn.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms?view=sql-server-2017) and connect to the SQL server.
2. Expand **Databases**.
3. Right-click on the database you want to back up, and then select **Tasks > Back up** (this is not available for version 2018/2019).
4. On the **Back Up Database** window, make sure the **Database** field contains the name of the database you want to back up.
5. Select **Full** for the **Backup Type**.
6. Click **Remove** to remove the default/last backup file name.
7. Click **Add** to open the **Select Backup Destination** window.
8. Click **[...]** next to the **File Name** field.
9. On the **Locate Database Files** window, select the folder where you want the backup file to go. By default, it is **..\Microsoft SQL Server\MSSQL.1\MSSQL\Backup**.
10. In the **File Name** field, type the name for this backup, with a **.bak** extension. For example, **xyz\_20080221.bak** for a backup of the XYZ database created on 21 February 2008.
11. Click **OK** to close the **Locate Database Files** window.
12. Click **OK** to close the **Select Backup Destination** window.
13. Click **OK** to start the backup. The progress icon displays in the lower-left corner, and a **completed successfully** message displays when it is done.

## Perfect Practice

What can I migrate? How do I migrate my data?

- Contacts
- Matters
- Notes
- Calendar Entries
- Tasks

Contact Perfect Practice to request a backup of your data.

## Pika

What can I migrate? How do I migrate my data?

- Contacts
- Matters
- Contact Notes
- Matter Notes

1. Open [SQL Server Management Studio Express](https://learn.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms?view=sql-server-2017) and connect to the SQL server.
2. Expand **Databases**.
3. Right-click on the database you want to back up, and then select **Tasks** > **Back up** (this is not available for version 2018/2019).
4. On the **Back Up Database** window, make sure the **Database** field contains the name of the database you want to back up.
5. Select **Full** for the **Backup Type**.
6. Click **Remove** to remove the default/last backup file name.
7. Click **Add** to open the **Select Backup Destination** window.
8. Click **[...]** next to the **File Name** field.
9. On the **Locate Database Files** window, select the folder where you want the backup file to go. By default, it is **..\Microsoft SQL Server\MSSQL.1\MSSQL\Backup**.
10. In the **File Name** field, type the name for this backup, with a **.bak** extension. For example, **xyz\_20080221.bak** for a backup of the XYZ database created on 21 February 2008.
11. Click **OK** to close the **Locate Database Files** window.
12. Click **OK** to close the **Select Backup Destination** window.
13. Click **OK** to start the backup. The progress icon displays in the lower-left corner, and a **completed successfully** message displays when it is done.

## PracticePanther

What can I migrate? How do I migrate my data?

- Contacts
- Matters
- Contact Notes
- Matter Notes
- Tasks
- Unbilled Time Entries
- Unbilled Expense Entries
- Email Communications
- Phone Communications
- Calendar Events
- Outstanding Balances (a single line item that represents the balance at time of export per matter invoice)
- Trust Balances (a single line item that represents the balance at the time of export for a matter or contact)

**Note:** Only administrators can export client data.

**Step 1: Update your PracticePanther settings as follows:**

1. Click your **Name** in the top right and select **Settings**.
2. Select **Company Settings** on the left side.
3. Under **Display Name** set the **Contact** to **First M Last**.
4. Update **Matter** to **Number-MatterName**.
5. Update Users to **First M Last**.
6. Click **Save**.

**Step 2: Export data. See sections below for specifics.**

**Important:** Once the data listed below is exported to Excel files, all of the files will export with the same name since they all come from the Activities section. In order to differentiate each exported file, change each file's name to a name relevant to the data within the file. For example, after exporting tasks, you can rename the Excel file to "Tasks."

**Contacts:**

1. Click **Contacts** in the menu bar at the top of your screen.
2. Set the filters at the top to:
   - **Primary Contacts**
   - **Assigned To: Any User**
   - **Created Date: All Time**
3. Click **Export to Excel** on the top right section and select **Export All**.
   - This button is generally located next to **Choose Columns** on the far right (look for the page icon with the small **x**).

**Matters:**

1. Click **Matters** in the menu bar at the top of your screen.
2. Set the filters at the top to:
   - **Assigned To: Any User**
   - **Originated By: *Any User***
   - **Status: Any**
   - **Created Date: *All Time***
3. Click **Export to Excel** on the top right section and select **Export All**.
   - This button is generally located next to **Choose Columns** on the far right (look for the page icon with the small **x**).

**Time entries:**

1. Click **Time Entries** in the menu bar at the top of your screen.
2. Set the filters at the top to:
   - **Billed By: Any User**
   - **Status: Any**
   - **Date Range: All Time**
3. Click **Choose Columns** and check ALL column checkboxes.
4. Click **Export to Excel** on the top right section and select **Export All**.
   - This button is generally located next to **Choose Columns** on the far right (look for the page icon with the small **x**).
5. Rename the downloaded file to **Time Entries**.

**Expense entries:**

1. Click **Expense** in the menu bar at the top of your screen. Or, find **Expense** under the **More** dropdown.
2. Set the filters at the top to:
   - **Billed By: Any User**
   - **Status: Any**
   - **Date Range: All Time**
3. Click **Choose Columns** and check ALL column checkboxes.
4. Click **Export to Excel** on the top right section and select **Export All**.
   - This button is generally located next to **Choose Columns** on the far right (look for the page icon with the small **x**).
5. Rename the downloaded file to **Expenses**.

**Invoices:**

1. Go to **Invoices** in the menu bar at the top of your screen.
2. Set the filters at the top to:
   - **All Invoices**
   - **Assigned to: Matter**
   - **Any User**
   - **All Time**
   - **Status: Any**
3. Click **Choose Columns** and click **ALL** column checkboxes
4. Click **Export to Excel** on the top right section and select **Export All**.
   - This button is generally located next to **Choose Columns** on the far right (look for the page icon with the small x).
5. Rename the downloaded file to Invoices.

**Tasks:**

1. Click **Activities** in the menu bar at the top of your screen.
2. Set the filters at the top to:
   - **Tasks**
   - **Status: Any**
   - **Assigned To: Any User**
   - **Created By: Any User**
   - **Date Range: All Time**
3. Click **Choose Columns** and check ALL column checkboxes.
4. Click **Export to Excel** on the top right section and select **Export All**.
   - This button is generally located next to **Choose Columns** on the far right (look for the page icon with the small **x**).
5. Rename the downloaded file to **Tasks**.

**Notes:**

1. Click **Activities** in the menu bar at the top of your screen
2. Set the filters at the top to:
   - **Notes**
   - **Status: Any**
   - **Assigned To: Any User**
   - **Created By: Any User**
   - **Date Range: All Time**
3. Click **Choose Columns** and check ALL column checkboxes.
4. Click **Export to Excel** on the top right section and select **Export All**.
   - This button is generally located next to **Choose Columns** on the far right (look for the page icon with the small **x**).
5. Rename the downloaded file to **Notes**.

**Phone/call logs:**

1. Click **Activities** in the menu bar at the top of your screen.
2. Set the filters at the top to:
   - **Calls**
   - **Status: Any**
   - **Assigned To: Any User**
   - **Created By: Any User**
   - **Date Range: All Time**
3. Click **Choose Columns** and check ALL column checkboxes.
4. Click **Export to Excel** on the top right section and select **Export All**.
   - This button is generally located next to **Choose Columns** on the far right (look for the page icon with the small **x**).
5. Rename the downloaded file to **Call logs**.

**Emails:**

1. Click **Activities** in the menu bar at the top of your screen.
2. Set the filters at the top to:
   - **Emails**
   - **Status: Any**
   - **Assigned To: Any User**
   - **Created By: Any User**
   - **Date Range: All Time**
3. Click **Choose Columns** and check ALL column checkboxes.
4. Click **Export to Excel** on the top right section and select **Export All**.
   - This button is generally located next to **Choose Columns** on the far right (look for the page icon with the small **x**).
5. Rename the downloaded file to **Emails**.

**Calendar events:**

1. Click **Activities** in the menu bar at the top of your screen.
2. Set the filters at the top to:
   - **Events**
   - **Status: Any**
   - **Assigned To: Any User**
   - **Created By: Any User**
   - **Date Range: All Time**
3. Click **Choose Columns** and check ALL column checkboxes.
4. Click **Export to Excel** on the top right section and select **Export All**.
   - This button is generally located next to **Choose Columns** on the far right (look for the page icon with the small **x**).
5. Rename the downloaded file to **Calendar**.

**Trust balances:**

1. Go to **Reports** > **Payments** > **Trust Account Reconciliation Report**.
2. Click **Export to Excel**.

## Prevail

What can I migrate? How do I migrate my data?

- Contacts
- Matters

1. Sign in to Prevail.
2. Open the **Administration** menu. For some versions, go to **File** > **Export**.
3. Select **Export Contacts**.
4. Select a location to save the export file and name the file.

**Note:** If these instructions are not applicable or do not work, contact Prevail for a backup of your data.

## ProDocs

What can I migrate? How do I migrate my data?

- Contacts
- Matters

If your firm has access to ProDoc Small Office Suite, Clio can bring this additional information:

- Unbilled time and expense entries

1. Click **Tools** and then select **Export**.
2. Select **Contacts**.
3. Check the box at the top to include **Closed Cases/Contacts**.
4. Click **Select All**.
5. Click **OK**.
6. Check the box for **Include Header Information** and then include all categories.
7. Save the file.
8. Repeat the steps above for cases (matters).

**ProDoc Small Office Suite:**

1. Click **Tools** and then select **Export Data**.
2. Select **Export Charges** for unbilled time and expenses.

## ProLaw

What can I migrate? How do I migrate my data?

- Contacts
- Matters
- Related Contacts
- Tasks
- Unbilled Time Entries
- Unbilled Expense Entries
- Calendar Events
- Outstanding Balances (a single line item that represents the balance at time of export for a matter)

**Note:** Depending on the quality of your data, we may also be able to migrate your calendar, tasks, related contacts, contact and matter notes, and unbilled time and expense entries.

1. Open [SQL Server Management Studio Express](https://learn.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms?view=sql-server-2017) and connect to the SQL server.
2. Expand **Databases**.
3. Right-click on the database you want to back up, and then select **Tasks** > **Back up** (this is not available for version 2018/2019).
4. On the **Back Up Database** window, make sure the **Database** field contains the name of the database you want to back up.
5. Select **Full** for the **Backup Type**.
6. Click **Remove** to remove the default/last backup file name.
7. Click **Add** to open the **Select Backup Destination** window.
8. Click **[...]** next to the **File Name** field.
9. On the **Locate Database Files** window, select the folder where you want the backup file to go. By default, it is **..\Microsoft SQL Server\MSSQL.1\MSSQL\Backup**.
10. In the **File Name** field, type the name for this backup, with a **.bak** extension. For example, **xyz\_20080221.bak** for a backup of the XYZ database created on 21 February 2008.
11. Click **OK** to close the **Locate Database Files** window.
12. Click **OK** to close the **Select Backup Destination** window.
13. Click **OK** to start the backup. The progress icon displays in the lower-left corner, and a **completed successfully** message displays when it is done.

## QuickBooks Desktop

What can I migrate? How do I migrate my data?

- Contacts
- Matters (derived from contacts or projects)
- Outstanding Balances

1. Navigate to the top of QuickBooks Desktop screen to find tabs for **Customer List**, **Vendor List**, and **Financial data**.
2. Click the **customers** tab or **vendors** tab you want to export.
3. Click the Excel dropdown arrow.
4. Select **Export Customer List** or **Export Vendor List**.
5. In the export window, choose whether to create a new worksheet, update an existing worksheet, or export to a CSV file.
6. Click **Export**.

## QuickBooks Online

What can I migrate? How do I migrate my data?

- Contacts
- Matters (derived from contacts or projects)
- Outstanding balance

**Contacts:**

1. Selec **Reports**.
2. Scroll down the page to find the **Customer Contact List** report (it may also be named **Client Contact List**).
3. Click **Customize** and ensure the **Deleted** state is set to **All** in order to capture all contacts.
4. Click the gear icon to customize the columns included in the report.
5. Check **Client**, **First Name**, **Last Name**, and the billing/shipping **Street**, **City**, **State**, **ZIP**, and **Country**. The **Client** column will be used to generate the matters.
6. Select additional columns as needed.
7. Deselect the columns you do not need (e.g. Full Name).
8. Expand the **Header/Footer** section and uncheck **Company Name** and **Report Title**
9. Click **Run Report**.
10. Select the icon that looks like a sheet of paper with an arrow.
11. Select **Export to Excel**.

**Accounts receivable:**

1. Click **Reports**.
2. Select the **Standard** subtab.
3. Choose **Accounts Receivable Aging** summary.
4. Select **30 days for 3 periods**.
5. Click **Run Report**.
6. Click the icon that shows a square with an arrow pointing upward.
7. Select **Excel** for file format.

## QuickBooks Professional Services

What can I migrate? How do I migrate my data?

- Contacts
- Matters derived from contacts
- Outstanding balances

1. Click **Reports** at the top of the screen and then select **Customers and Receivables**.
2. Select **Customer Contacts List** to show the contacts list and receivables.
3. *Optional:* Customize the report by adding other columns in the top left.
4. Click **Export**.
5. Select **CSV file** for the output file format.

## Rocket Matter

**Note:** If your firm is using Rocket Matter NextGen, refer to the instructions for [Rocket Matter NextGen](migrating-data-from-your-current-software-n-s.md#01JN41FJG1D9H70SFNB968C76W).

What can I migrate? How do I migrate my data?

- Contacts
- Matters
- Related Contacts
- Unbilled Time Entries
- Unbilled Expense Entries
- Outstanding Balances (a single line item that represents the summative balance at time of export for a matter)
- Trust balances (a single line item that represents the balance at time of export for a contact)

**Contacts:**

1. Log in to Rocket Matter.
2. Select **Settings** in the left navigation bar.
3. Under **Data**, click **Export Contacts**.
4. Choose a location to save the file.
5. Click **Save**.

**Tip:** Once your export is downloaded to your computer, you can view to ensure that the number of records in the file matches the number of records from Rocket Matter.

**Matters:**

1. Log in to Rocket Matter.
2. Select **Matters** on the left sidebar.
3. Select **Filters** to include **Open**, **Completed**, and **Closed** cases.
4. Select the **Show/Hide Columns** button and check all boxes.
5. Select **Export Report**.

**Tip:** Once your export is downloaded to your computer, you can view to ensure that the number of records in the file matches the number of records from Rocket Matter.

**Activities (unbilled time and expense entries):**

1. Log in to Rocket Matter.
2. Select **Reports** on the left sidebar.
3. Click **Run Report** under **Billable Activity by User(s)**.
   - Choose the **Date Range** of the exported activities.
   - Add **All Users**.
   - **Exclude Invoiced status**. Failure to do this step may slow down the migration.
   - Include all **Activity types**.
   - Include **Expenses**.
4. Select **Export Report**.

**Matter-related contacts:**

1. Log in to Rocket Matter.
2. In the left navigation bar, click **Reports**.
3. Click **Run Report** under **I Want To See All Matter Related Contacts**.
4. Select **Export Report**.

**Trust balances:**

1. Log in to Rocket Matter.
2. Select **Billing** on the left sidebar.
3. Under **Advanced Deposits**, select the green hyperlink dollar amount for each client.
4. Click **Run Report**.
5. Select **Export Report**.

**Outstanding balances:**

No additional extraction is required. Use the **Current Balance** column from the matters export for the outstanding balances.

## Rocket Matter NextGen

What can I migrate? How do I migrate my data?

- Contacts
- Matters
- Related Contacts
- Unbilled Time Entries
- Unbilled Expense Entries
- Outstanding Balances (a single line item that represents the summative balance at time of export for a matter)
- Trust balances (a single line item that represents the balance at time of export for a contact)

**Contacts:**

1. Log in to Rocket Matter.
2. In the left navigation bar, click **Contacts** > **Address Book**.
3. Make sure all filters are cleared to ensure all contacts are exported.

   **Tip:** You can also apply specific filters if you only want to migrate a specific subset of your contacts.
4. In the top right, click the settings (gear) icon.
5. In the **Columns** tab, make sure all the contact-related fields you want to export are selected, then click **Apply**.
6. Click the export icon.
7. In the pop-up modal, under **Pages**, select **Custom** (to ensure all pages are exported).
8. *Optional:* If you previously opted to apply a specific filter to the displayed list, make sure **Apply current filters** is selected. You also have another opportunity to select or deselect the columns to export.
9. Under **Export Format**, **select CSV (.csv)**.
10. Ensure that all of the contact-related fields you want to export are selected from the list of columns.
11. Click **Export**.

**Tip:** Once your export is downloaded to your computer, you can view to ensure that the number of records in the file matches the number of records from Rocket Matter.

**Matters:**

1. Log in to Rocket Matter.
2. In the left navigation bar, click **Matters**.
3. Make sure all filters are cleared to ensure all matters are exported.

   **Tip:** You can also apply specific filters if you only want to migrate a specific subset of your matters.
4. In the top right, click the settings (gear) icon.
5. In the **Columns** tab, make sure all the matter-related fields you want to export are selected, then click **Apply**.

   **Note:** If you want to export outstanding matter balances, you can do that as part of the matters export by selecting the **Current Balance** field.
6. Click the export icon.
7. In the pop-up modal, under **Pages**, select **Custom** (to ensure all pages are exported).
8. *Optional:* If you previously opted to apply a specific filter to the displayed list, make sure **Apply current filters** is selected. You also have another opportunity to select or deselect the columns to export.
9. Under **Export Format**, **select CSV (.csv)**.
10. Ensure that all of the matter-related fields you want to export are selected from the list of columns.
11. Click **Export**.

**Tip:** Once your export is downloaded to your computer, you can view to ensure that the number of records in the file matches the number of records from Rocket Matter.

**Activities (unbilled time and expense entries):**

1. Log in to Rocket Matter.
2. In the left navigation bar, click **Billing** > **Time & Expense**.
3. Using the filter, make sure the list is filtered to include items with a **Status** set to **Unbilled**.
4. In the top right, click the settings (gear) icon.
5. In the **Columns** tab, make sure all the fields you want to export are selected. You are required to include:

   - **File #**
   - **Time/Exp**

   Click **Apply**.
6. Click the export icon.
7. In the pop-up modal, under **Pages**, select **Custom** (to ensure all pages are exported).
8. Ensure **Apply current filters** is selected.
9. Under **Export Format**, **select CSV (.csv)**.
10. Ensure that all of the fields you want to export are selected from the list of columns (including **File #** and **Time/Exp**.
11. Click **Export**.

**Matter-related contacts:**

1. Log in to Rocket Matter.
2. In the left navigation bar, click **Reports**.
3. Click **Matter Activities** > **Conflict Check**.
4. Click **Run Report** under **I Want To See All Matter Related Contacts**.
5. Select **Export Report**.

**Trust balances:**

1. Log in to Rocket Matter.
2. Select **Trust** on the left sidebar.
3. Click **Run Report** at the top right.
4. Click **Export**.

**Outstanding balances:**

No additional extraction is required. Use the **Current Balance** column from the matters export for the outstanding balances.

## RTG Bills

What can I migrate? How do I migrate my data?

- Contacts (limited)
- Matters (limited)
- Unbilled Time Entries
- Unbilled Expense Entries

**Contacts:**

1. Provide the **Microsoft Access Database** to the Clio representative. You can get the copy in the RTG Bills folder.
2. Navigate to the **Supervisor Menu**.
3. Under the **Links** heading, click on **RTG Bills Menu**.
4. Click **Reports** and then select **Standard Reports**.
5. Select **Export to File**, and then select **Client List (No Hidden Clients) (CSV Format)** from the options.
6. On the next screen, select **One Client** and then delete the client number and name listed in the text boxes. Re-select **All Clients**.
7. On the next screen, **Download** the report.

**Matters:**

1. Provide the **Microsoft Access Database** to the Clio representative. You can get the copy in the RTG Bills folder.
2. Navigate to the **Supervisor Menu**.
3. Under the **Links** heading, click on **RTG Bills Menu**.
4. Click **Reports** and then select **Standard Reports**.
5. Select **Export to File**, and then select **Matters by Practice Area (CSV)** from the options.
6. On the next screen, select **One Client** and then delete the client number and name listed in the text boxes. Re-select **All Clients**.
7. On the next screen, **Download** the report.

**Unbilled activities (time and expense entries):**

1. Provide the **Microsoft Access Database** to the Clio representative. You can get the copy in the RTG Bills folder.
2. Navigate to the **Supervisor Menu**.
3. Under the **Links** heading, click on **RTG Bills Menu**.
4. Click **Reports** and then select **Standard Reports**.
5. Select **Export to File**, and then select **Fees & Expenses (CSV Format)** from the options.
6. On the next screen, select **One Client** and then delete the client number and name listed in the text boxes. Re-select **All Clients**.
7. On the next screen, **Download** the report.

## Sales Nexis

What can I migrate? How do I migrate my data?

- Contacts

1. Contact Sales Nexis to request an export.

## Salesforce

**What:**

- Contacts

## SILQ

What can I migrate? How do I migrate my data?

- Contacts
- Matters
- Unbilled Time Entries
- Unbilled Expense Entries
- Outstanding Balance (as a single line item that represents the summative balance at the time the matter is exported)
- Safe Custody

**Matters:**

1. Navigate to the **Matters** window.
2. Use the filters to update your matters information with the relevant information you want to export:
   - For the **Active** filter, select **All Matters**.
   - For the **Unbilled Work** filter, select **Show all Open Work**.
3. Click the "more" icon (the three vertical dots) in the top-right corner, then click **Field Configuration**.
4. Use the checkboxes to select or deselect any relevant fields you want to include or exclude for your export, then click **Save**.
   - Your **Matters** window will update based on your selections.
5. Click the "more" icon (the three vertical dots) in the top-right corner, then select **Download CSV**. 
   - Use the filename "SILQ\_Matters\_Export\_YYYYMMDD.csv" to quickly find the right file later when you need to upload it to Clio.

**Contacts:**

1. Navigate to the **Contacts** window.
2. Use the filters to update your table with the relevant information you want to export:
   - For the **Active** filter (the first filter towards the top of the page), select **All Contacts**.
3. Click the "more" icon (the three vertical dots) in the top-right corner, then click **Field Configuration**.
4. Use the checkboxes to select or deselect any relevant fields you want to include or exclude for your export, then click **Save**.
   - Your **Contacts** window will update based on your selections.
5. Click the "more" icon (the three vertical dots) in the top-right corner, then select **Download CSV**. 
   - Use the filename "SILQ\_Contacts\_Export\_YYYYMMDD.csv" to quickly find the right file later when you need to upload it to Clio.

**Time Entries:**

1. Navigate to the **Time Entries** window.
2. Set the following filters to update your table with the relevant information you want to export:
   - **Uninvoiced**
   - **Fee Earner** > **All**
   - **Type** > **Time + fixed**
   - **Date range** > **All time**
3. Click the "more" icon (the three vertical dots) in the top-right corner, then click **Field Configuration**.
4. Use the checkboxes to select or deselect any relevant fields you want to include or exclude for your export, then click **Save**.
   - Your **Time Entries** window will update based on your selections.
5. Click the "more" icon (the three vertical dots) in the top-right corner, then select **Download CSV**. 
   - Use the filename "SILQ\_TimeEntries\_Export\_YYYYMMDD.csv" to quickly find the right file later when you need to upload it to Clio.

**Invoices:**

1. Navigate to the **Invoices** window.
2. Set the following filters to update your table with the relevant information you want to export:
   - **All time**
   - **All users**
3. Click the "more" icon (the three vertical dots) in the top-right corner, then click **Field Configuration**.
4. Use the checkboxes to select or deselect any relevant fields you want to include or exclude for your export, then click **Save**.
   - Your **Invoices** window will update based on your selections.
5. Click the "more" icon (the three vertical dots) in the top-right corner, then select **Download CSV**. 
   - Use the filename "SILQ\_Invoices\_Export\_YYYYMMDD.csv" to quickly find the right file later when you need to upload it to Clio.

**Expense Entries:**

1. Navigate to the **Spend Money** window.
2. Set the following filters to update your table with the relevant information you want to export:
   - **All**
   - **All users**
3. Click the "more" icon (the three vertical dots) in the top-right corner, then click **Field Configuration**.
4. Use the checkboxes to select or deselect any relevant fields you want to include or exclude for your export, then click **Save**.
   - Your **Spend Money** window will update based on your selections.
5. Click the "more" icon (the three vertical dots) in the top-right corner, then select **Download CSV**.
   - Use the filename "SILQ\_SpendMoney\_Export\_YYYYMMDD.csv" to quickly find the right file later when you need to upload it to Clio.

**Safe Custody:**

If your firm uses Safe Custody Document Registers:

1. Navigate to the **Safe Custody Data** window.
2. Set the following filters to update your table with the relevant information you want to export:
   - **All**
   - **All users**
3. Click the "more" icon (the three vertical dots) in the top-right corner, then click **Field Configuration**.
4. Use the checkboxes to select or deselect any relevant fields you want to include or exclude for your export, then click **Save**.
   - Your **Safe Custody** window will update based on your selections.
5. Click the "more" icon (the three vertical dots) in the top-right corner, then select **Download CSV**.
   - Use the filename "SILQ\_SafeCustody\_Export\_YYYYMMDD.csv" to quickly find the right file later when you need to upload it to Clio.

## Smokeball

What can I migrate? How do I migrate my data?

- Contacts
- Matters
- Tasks (Incomplete)
- Unbilled Time Entries
- Unbilled Expense Entries

**Note:** Depending on the quality of the data, we may also be able to migrate incomplete tasks. Tasks without a due date will need to be assigned a due date before bringing them into Clio. Additionally, while we cannot migrate calendar events, you might be able to bring these events to Clio using the calendar sync functions in Smokeball and Clio:

- [Syncing Smokeball and Outlook Calendar](https://smokeball.helpdocsonline.com/syncing-smokeball-and-outlook-cale-2)
- [Microsoft Office 365 calendar sync](../calendars/calendar-sync-and-feeds.md#microsoft-office-365-calendar-sync-0-1)

**Contacts:**

1. Select the **Reports** button on the left side of the screen.
2. Select **Contact - Full List**.
3. Click **Save** and select **CSV** format.

**Matters:**

1. Select the **Reports** button on the left side of the screen
2. Select **Matter - Full List**.
3. Click **Save** and select the **CSV** format.

**Unbilled Time and Expense Entries:**

1. Navigate to Smokeball billing and click **Reports** on the left side of the screen
2. Select **Work in Progress - Details** from the dropdown
3. Ensure the filters are set correctly ('All' Timekeepers, 'All' Areas of Law, 'Time Entries and Expense Entries', Date filter).
4. Click CSV to generate the CSV file.

**Tasks:**

1. Go to the **Tasks** tab on the left side.
2. In the top left of the screen, click a user's name dropdown and select **All Staff**.
3. Hover over the column headers and right-click on any of the columns and check all of the boxes.
4. Click **Export** at the top of the page.
5. Choose the desired save location and click **Save** to complete the export.

## Soluno

What can I migrate? How do I migrate my data?

- Contacts
- Matters
- Unbilled time and expense entries
- Outstanding balances (accounts receivables)

**Contacts and matters:**

1. Go to **Views and Reports** > **Contact** > **Contacts**.
2. Click the **V** in the top left.
3. Enter **All** in the search bar and select the relevant option.
4. Click **Play** in the bottom left.
5. Click **Export to Excel** in the top right.

**Vendors:**

1. Go to **Views and Reports** > **Contact** > **Contacts**.
2. Click the **V** in the top left.
3. Enter **Vendors** in the search bar and select the relevant option.
4. Click **Play** in the bottom left.
5. Click **Export to Excel** in the top right.

**Other contacts:**

1. Go to **Views and Reports** > **Contact** > **Contacts**.
2. Click the **V** in the top left.
3. Enter **Other** in the search bar and select the relevant option.
4. Click **Play** in the bottom left.
5. Click **Export to Excel** in the top right.

**Time entries:**

1. Go to **Views and Reports** > **Contact** > **Ledgers**.
2. Click the **V** in the top left.
3. Enter **Time** in the search bar and select the relevant option.
4. Scroll down to **Show Files** and set **Unbilled charges greater than or equal to** to **0.01**.
5. Scroll down to **Entries** and under **Include Billed/Unbilled**, change the value to **Unbilled**.
6. Check that **Fees** is turned on.
7. Click **Play** in the bottom left.
8. Click **Export to Excel** in the top right.

**Expense entries:**

1. Go to **Views and Reports** > **Contact** > **Ledgers**.
2. Click the **V** in the top left.
3. Enter **Expense** in the search bar and select the relevant option.
4. Scroll down to **Show Files** and set **Unbilled charges greater than or equal to** to **0.01**.
5. Scroll down to **Entries** and under **Include Billed/Unbilled**, change the value to **Unbilled**.
6. Check that **Fees, Hard Exp**, and **Soft Exp** are turned on.
7. Click **Play** in the bottom left.
8. Click **Export to Excel** in the top right.

**Outstanding balances (accounts receivables):**

1. Go to **Views and Reports** > **Contact** > **Ledgers**.
2. Click the **V** in the top left.
3. Enter **Summary** in the search bar and select the relevant option.
4. Click **Play** in the bottom left.
5. Click **Export to Excel** in the top right.