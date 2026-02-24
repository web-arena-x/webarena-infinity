# Migrating Data From Your Current Software [A-B]

Source: https://help.clio.com/hc/en-us/articles/9813809475995-Migrating-Data-From-Your-Current-Software-A-B

---

This article explains what data can be migrated from your current practice management software and how to export the data from that software. Software applications starting with the letters A and B are listed below.

**Tip:** See one of the articles below if your current practice management software does not start with the letters A or B.

- [Migrating Data From Your Current Software [C-F]](https://help.clio.com/hc/en-us/articles/10263045235867)
- [Migrating Data From Your Current Software [G-M]](https://help.clio.com/hc/en-us/articles/10263146574107)
- [Migrating Data From Your Current Software [N-S]](https://help.clio.com/hc/en-us/articles/9815681343003)
- [Migrating Data From Your Current Software [T-Z]](https://help.clio.com/hc/en-us/articles/9812890677531)

## Abacus

What can I migrate? How do I migrate my data?

- Contacts
- Matters
- Contact notes
- Matter notes
- Related Contacts
- Tasks
- Calendar Events
- Email Communications

**Note:** The following steps apply to exporting your contacts, matters, and notes. To export other data types, such as calendar events or tasks, follow the instructions in the Abacus help center.

Before migrating your data, ensure all users are logged out of AbacusLaw, Abacus Accounting, MessageSlips, and Microsoft Outlook. If you need to force all users out, go to **File** > **Setup > Scheduled Shutdown**. Under the **Immediate shutdown** section, click **Shutdown Now**.

**Option 1: Back up your data**

**Important:** If your firm uses a **PostgreSQL** server for Abacus, standard backup methods will not be sufficient for a complete data export. The DATA01 folder will not contain up-to-date data, and this backup option will not work. You can identify your server type by going to **Help >** **About Abacus**. **For PostgreSQL servers, use one of the other export options below.**

1. Log in to Abacus.
2. Click **File**.
3. Select **Utilities** > **Backup** > **Backup**.
4. Check that the **Destination** is set to your preferred location.
5. Click **Backup.** A backup file in the form of **LAW\_XXX.zip** will be created and stored in the selected directory. The "X" refers to the backup number.

**Option 2: Export your data**

1. In Abacus, go to **File** > **Reports**.
2. Select one of the following: **Names**, **Calendar**, **Matters**, **Matter Notes**, or **Name Notes**.
3. Click **New Report**.
4. Enter a new name for the report (e.g., Clio Contact Export) and click **OK**.
5. In the upper left of the screen, click **Add**.
6. Click **Run**.
7. Click **Comma Delimited**.
8. Click **Ok** and then save the file.
9. Search for **law9.adt**  or **law9.dbf** in the Abacus folder on your computer.

**Option 3: Export from a PostgreSQL server**

If you have a PostgreSQL server, you will need to use a different export method.

1. Use the export feature in **Abacus Accounting**.
2. In **Abacus Law**, select **File** > **Export** and follow the instructions on the web page.
3. You can also contact Abacus directly to request an export for a fee.

## Abacus Sky

What can I migrate? How do I migrate my data?

- Contacts
- Matters
- Contact Notes
- Related Contacts
- Tasks
- Calendar Events
- Email Communications

Before migrating your data, ensure all users are logged out of AbacusLaw, Abacus Accounting, MessageSlips, and Microsoft Outlook. If you need to force all users out, go to **File** > **Setup** > **Scheduled Shutdown**. Under the **Immediate shutdown** section, click **Shutdown Now**.

**Option 1: Back up your data**

**Important:** If your firm uses a **PostgreSQL** server for Abacus, standard backup methods will not be sufficient for a complete data export. The DATA01 folder will not contain up-to-date data, and this backup option will not work. You can identify your server type by going to **Help** > **About Abacus**. **For PostgreSQL servers, use one of the other export options below.**

1. Log in to Abacus.
2. Click **File**.
3. Select **Utilities** > **Backup** > **Backup.**
4. Check that the **Destination** is set to your preferred location.
5. Click **Backup.** A backup file in the form of **LAW\_XXX.zip** will be created and stored in the selected directory. The "X" refers to the backup number.

**Option 2: Export your data**

1. In Abacus, go to **File** > **Reports**.
2. Select one of the following: **Names, Calendar, Matters,** **Matter Notes**, or **Name Notes**.
3. Click **New Report**.
4. Enter a new name for the report (e.g., Clio Contact Export) and click **OK**.
5. In the upper left of the screen, click **Add**.
6. Click **Run**.
7. Click **Comma Delimited**.
8. Click **Ok** and then save the file.
9. Search for **law9.adt**  or **law9.dbf** in the Abacus folder on your computer.

**Option 3: Export from a PostgreSQL server**

If you have a PostgreSQL server, you will need to use a different export method.

1. Use the export feature in **Abacus Accounting**.
2. In **Abacus Law**, select **File** > **Export** and follow the instructions on the web page.
3. You can also contact Abacus directly to request an export for a fee.

## ACT!

What can I migrate? How do I migrate my data?

- Contacts
- Matters
- Activities as Calendar
- Notes
- History as Notes

1. Log in to your database as an Administrator or a Manager level Act! user.
2. Click **File** > **Back Up** > **Database...**
3. Click **Browse...**, then find the location where you will save the backup.
4. Give the file a new name (if desired), and then click **Save**.
5. Uncheck **Include Attachments**. These are not included in the migration.
6. Choose whether you want to password-protect the database backup file.
7. Click **OK** to begin backing up the items into a .ZIP file.
8. Once the backup is completed and the confirmation window appears, click **OK** to complete the backup process.

The following article outlines the above steps in greater detail: [How to backup and restore an Act! database](https://help.act.com/hc/en-us/articles/360024245394-How-to-backup-and-restore-an-Act-database).

## ActionStep

What can I migrate? How do I migrate my data?

- Contacts
- Matters
- Related Contacts
- Tasks
- Email Communications
- Unbilled Time Entries
- Unbilled Expense Entries

Obtain a full backup of your data from [ActionStep Support](https://support.actionstep.com/support/home) to ensure the migration of more complete data, including contact and matter custom fields and matter notes.

## Aderant

What can I migrate? How do I migrate my data?

Client Profiles

- Contacts
- Matters
- Tasks
- Calendars
- Email Communications
- Matter Notes

ADR Live

- Contacts
- Matters
- Related Contacts

1. Open SQL Server Management Studio Express and connect to the SQL server.
2. Expand **Databases**.
3. Right-click on the database you want to back up, then select **Tasks** > **Back up**. (This is not available for version 2018/2019).
4. On the **Back Up Database** window, make sure the **Database**field contains the name of the database you want to back up.
5. Under **Backup Type**, select **Full**.
6. Click **Remove**to remove the default/last backup file name.
7. Click **Add**to open the **Select Backup Destination** window.
8. Click **[...]**next to the **File Name** field.
9. On the **Locate Database Files** window, select the folder where you want the backup file to go. By default, it is **..\Microsoft SQL Server\MSSQL.1\MSSQL\Backup**.
10. In the **File Name** field, type the name for this backup, with a **.bak**extension. For example, **xyz\_20080221.bak** for a backup of the XYZ database created on 21 February 2008.
11. Click **OK** to close the **Locate Database Files** window.
12. Click **OK** to close the **Select Backup Destination** window.
13. Click **OK**to start the backup. The progress icon displays in the lower-left corner, and a **completed successfully** message displays when it is done.

## AdvologiX

What can I migrate? How do I migrate my data?

- Contact Listing
- Matter Listing
- Calendar Events

**Important:** Users with the Data Export permission can view all exported data and all custom objects and fields in the Export Service page. This permission is granted by default only to the System Administrator profile because it enables account-wide visibility.

1. Click **Your Name | Setup | Data Management | Data Export and Export Now** or **Schedule Export**. The **Export Now** option prepares your files for export immediately. This option is only available if enough time has passed since your last export. The **Schedule Export** option allows you to schedule the export process for weekly or monthly intervals.
2. Select the desired encoding for your export file.
3. Select **Include in export** to include attachments in your export data.
4. Select **Replace carriage returns with spaces** to have spaces instead of carriage returns or line breaks in your export files. This may be useful if you plan to use your export files for importing or other integrations.
5. If you are scheduling your export, select the frequency (only available for organizations with monthly exports), start and end dates, and time of day for your scheduled export.
6. Select the types of data to include in your export. We recommend that you include all data if you are not familiar with the terminology used for some of the types of data. Note the following:
   - - Formula and roll-up summary fields are always excluded from exports.
     - If your organization uses divisions, data from all divisions is included in the export.
     - If your organization uses person accounts and you are exporting accounts, all account fields are included in the account data.
     - If your organization uses person accounts and you are exporting contacts, person account records are included in the contact data. However, the contact data only includes the fields shared by contacts and person accounts.
     - For information on field limitations, see the [Salesforce Field Reference Guide](https://developer.salesforce.com/docs/atlas.en-us.238.0.sfFieldRef.meta/sfFieldRef/salesforce_field_reference.htm).
7. Click **Start Export** or **Save**.

## Amicus (Attorney Premium)

What can I migrate? How do I migrate my data?

- Contacts
- Matters
- Notes
- Related Contacts
- Tasks
- Email Communications
- Phone Communications
- Unbilled Time Entries
- Unbilled Expense Entries
- Calendar Events
- Outstanding Balances

**Note**: Depending on the data, we may also be able to migrate balances forward/outstanding balances.

1. Confirm that all users are logged out of Amicus.
2. Navigate to the **Firm Settings** view of the **Office** module.
3. Select **Maintenance** > **Utilities**.
4. Under the **Backup** section, click **Browse**.
5. Select the location where you will save your backup. The location must be on the same drive as your server.
6. Click **Apply**.
7. Click **Backup Now**. The backup can take a significant amount of time depending on the size of the database.
8. Once the database backup is complete, navigate to the location you selected. You will see files with the following format (you may have up to 5 file): BcAmicus\_XXXX\_XX\_XX\_XX\_XX\_XX.bak
9. Provide your database backup files to your data migration specialist ahead of the export call to accelerate the migration process.

## Amicus (Cloud/Online)

What can I migrate? How do I migrate my data?

- Contacts
- Matters
- Matter Notes
- Related Contacts
- Tasks
- Unbilled Time Entries
- Unbilled Expense Entries
- Calendar Events
- Outstanding Balances

The Amicus Cloud interface does not have export functionality. You can request a backup of your data in .bacpac (Microsoft Azure database) format from Amicus.

## Amicus (Small Firm Edition)

What can I migrate? How do I migrate my data?

- Matters
- Contacts
- Tasks
- Calendar Events

1. Log in to Amicus Small Firm.
2. Go to **File** > **Reports**.
3. Run a report for each desired export:
   - Contacts
   - Matters
   - Calendars
   - Tasks
4. Save the files with a .csv extension to open them in excel.

**Note:** The exports are not guaranteed. Without Amicus Administrator, some options may not be available.

## AppColl

What can I migrate? How do I migrate my data?

- Contacts
- Matters
- Tasks
- Unbilled Time Entries
- Unbilled Expense Entries

1. Log in to AppColl.
2. Go to the main page.
3. Click **Export** and select **CSV**.

## Basecamp

What can I migrate? How do I migrate my data?

- Contacts

1. Go to the **Account** page.
2. Click **Set Up** or **Download and Export**.
3. Select **All Active Projects**.
4. You will receive an email when the export is complete.

## BestCase

What can I migrate? How do I migrate my data?

- Contacts

**Note:** Depending on the data, we may also be able to migrate matters.

You can export your client list and some matter information from Best Case into CSV format. A CSV file can be opened in Excel and used for mailing or tracking purposes.

1. From the **Client List**, navigate to the menu bar and select **File/Export Client List**.
2. Click **Report**.
3. Filter the contacts list using active/closed status and date ranges if needed.
4. Export list into CSV.
5. Choose the folder destination where you want to save the CSV file. Best Case automatically names the file BestCaseClients.csv, but you can change the name by editing the **File Name** field.

## BigTime

What can I migrate? How do I migrate my data?

- Contacts
- Matters

**Note:** Depending on the quality of your data, we may be able to migrate related contacts, unbilled time and expenses, and tasks.

1. At the top menu bar, select **Reports**.
2. Select **Report Center**.
3. Click the **Magnifying Glass** button.
4. Choose **Create your Report**.
5. Select **Matter List**from the options.
6. Check any relevant boxes on the right-hand side.
7. Click the **Click Here** link in the bottom right corner.
8. Enter a name for you report as well as the relevant report group and click **OK**.
9. Select **Reports**from the top menu bar.
10. Click **Report Center**.
11. Select the report you created.
12. Click **Export** and choose **XLS** from the dropdown.
13. Repeat the above steps for matters.

## Bill4Time

What can I migrate? How do I migrate my data?

- Contacts
- Matters
- Contact Notes
- Unbilled Time Entries
- Unbilled Expense Entries
- =Outstanding Balances (a single line item that represents the summative balance of a matter at the time of export.)

**Note:** Depending on the quality of your data, we may be able to migrate accounts receivable data. Accounts receivables are derived from the Invoice.csv file with "Unpaid" status and may not accurately provide a true outstanding balance since payments are not being applied to these amounts. Additionally, we cannot migrate outstanding balances when multiple matters are invoiced on one bill. These will need to be entered into Clio manually for each matter. Learn more [here](https://help.clio.com/hc/en-us/articles/9228623050139-Migration-Templates-for-Importing-Into-Clio#import-balances-forward-outstanding-balances--0-9).

1. In the top right, click your name.
2. Select **Data Management**from the dropdown menu.
3. Click the **Export** tab, select a report from the dropdown menu, and set the date range.
4. Click **Export Data** on the top right.
5. Go to the **File Downloads** subtab and click the **Download** icon. The export is in .csv format.

## Billings Pro

What can I migrate? How do I migrate my data?

- Clients
- Matters
- Unbilled Time Entries

1. Go to **File** > **Export** > **Export to all TSV**.
   - The download will provide several exports in .txt format.
2. Import into Excel using the text converter (Data - From Text).

## BillQuick Online

What can I migrate? How do I migrate my data?

- Contacts
- Matters
- Unbilled Time Entries
- Unbilled Expense Entries
- Outstanding Balances

**Contacts**

1. Click **Reports**.
2. Under **Reports Group**, select **Master Information List**.
3. Click **Client Address and phone details by group**.
4. Click **export**.
5. Select **CSV**.

**Matters**

1. Click **Reports**.
2. Under **Reports Group**, select **Master Information List**.
3. Click on **Project Details By Client**.
4. Click **export**.
5. Select **CSV**.

## BillQuick Desktop

What can I migrate? How do I migrate my data?

- Contacts
- Matters

**Versions:** BillQuick v21 and later

1. Click **File** > **Utilities**.
2. Click **Import/Export**.

**Versions:** BillQuick v20 and earlier

1. Go to **Utilities** at the top of your window.
2. Select **Import/Export**.
3. Type the following:
   - Contact/Client (Contacts in Clio)
   - Project (Matters in Clio)
   - Time Entry (Time Entries in Clio)
   - Expense Log List (Expense Entries in Clio)
4. Send to **Excel**.