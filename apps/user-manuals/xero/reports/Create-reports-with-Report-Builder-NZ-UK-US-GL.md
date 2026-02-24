# Create reports with Report Builder in Practice Manager

Source: https://central.xero.com/s/article/Create-reports-with-Report-Builder-NZ-UK-US-GL

---

## Overview

- Create customised reports for your practice using client, job or tax return information.
- Set the order of fields to control how information appears in the report.

How it works

Report Builder lets you create and run custom reports, as well as providing sample reports. You can run the sample reports unchanged, or use them as a starting point for building custom reports.

You need the [build report user permission](About-staff-privileges-in-Practice-Manager.md) to create reports. Without this permission, you can only view and run reports assigned to you in **My Reports.**

The Report Builder has three tabs:

- **My reports** – lists the custom reports that you have access to. These include reports you've built, or any reports other staff members have created and given you access to.
- **Custom reports** – lists all the custom reports that've been created by any staff member with the build report user permission. You can also create a new report based on existing one or edit an existing report.
- **Samples** – lists the sample reports that you can use unmodified, or as the starting point for creating a custom report.

Create a report

When you create a new report, the available report types relate to the database tables in Practice Manager, such as job or the WIP ledger. Choose the report type that contains the data you want to report on. If you're unable to find the reporting fields you need, you might need to try different report types.

For example, the **Monthly staff expenses** sample report is based on the job cost data table. This is because expenses are stored in the job cost table, rather than a table relating to staff.

Once you save the report, it will list in the **Custom** reports tab. You can run, edit, and resave the report at any time.

### Create a new report

1. In the **Reports** menu, select **Report Builder**.
2. Click **New report**.
3. Select the report type and layout. You can choose from the following layout options:
   - **Table** – creates a standard rows and columns layout.
   - **Bar Chart** – allows you to select a data field to display along the horizontal (X) axis and a value to display along the vertical (Y) axis.
   - **Pie Chart** – allows you to select a field to use for naming the pie segments and a field value to determine the size of segments.
   - **Monthly Summary** – creates a report of a value, such as billable time for each client, broken down into monthly summaries.
4. Click **Create**.
5. In the Report Designer screen, give your new report a name in the **Title** field.
6. Under **Select the fields to display on the report**, add the fields you want shown in your report one at a time from the dropdown list provided. You can click and drag fields into the order you want once you've added them.
7. (Optional) Under **Select the criteria for the report**, select any relevant filters. This determines whether the report will display items that match **all** or **some** of the conditions you select.
8. Under **Select the staff members who can view this report**, select the relevant staff members.
9. Under **Select the options for this report**, select how you want the information to display:
   - Rows can either be **not grouped** or **grouped/sub totalled by the first field** of those added in step 5.
   - You can display the last field **on the same line** as the last line of the report, or **on the next line**. The second option is useful for displaying description or note fields under their details.
   - Choose which report criteria staff can change.
10. Click **Preview Report** to open the report without saving changes, or click **Save**.

### Create a new report from a sample report

You can run Practice Manager’s sample reports as it is, or customise these according to your organisation's needs. When you customise and save a sample report, the changes don't apply to the original report. Instead, a new report is copied and added to the **Custom reports** tab.

1. In the **Reports** menu, select **Report Builder**.
2. Select the **Samples** tab.
3. Find and open the sample report you want to customise.
4. Change the **Title** of the report to something that suits your practice.
5. Edit the report to suit your practice’s needs.
6. Click **Preview Report** to review your changes. To further customise your report, click the back button on your browser to return to the **Report Designer** screen.
7. When you're happy with the report, click **Save**.

### Create a new report from a custom report

The **Custom reports** tab shows all reports any staff member has created and saved. You can use a saved report and copy it to create a new report.

1. In the **Reports** menu, select **Report Builder**.
2. Select the **Custom reports** tab.
3. Find and open the report you want to copy.
4. Hover over **Options**, then select **Copy Report**.
5. Change the **Title** of the report to something that suits your practice.
6. Edit the report to suit your practice’s needs.
7. Click **Preview Report** to review your changes. To further customise your report, click the back button on your browser to return to the **Report Designer** screen.
8. When you're happy with the report, click **Save**.

Search, filter, and delete custom reports

### Search for a report

To search for a specific custom report, in the **Custom reports** tab start typing any part of the report title into the search bar. All reports with the searched wording will automatically show.

### Filter custom reports

Sort and display your practice’s custom reports using a range of filters. To do this:

1. In the **Custom reports** tab, click **Filter** next to the search bar.
2. Click on a filter type from the options available, such as **Created by** or **Last used**.
3. Select the criteria for that filter, then click **Apply**.

### Delete custom reports

You can delete any custom reports that are no longer being used by your practice, or that you have duplicates of.

To do this, select the box next to the reports you want to delete, then click **Delete report** at the bottom of the page.

### Add or remove staff from reports

You can add or remove staff in bulk from custom reports. This helps you keep track of your staff's access to reports.

If a staff member is assigned to a report, they will have access to it under their **My reports** tab in Report Builder.

To add or remove staff:

1. In the **Custom reports** tab, select the box next to the reports you want to add or remove staff from.
2. Click **Remove staff** or **Add staff** at the bottom of the page.
3. Select the box next to the relevant staff members.
4. Click **Add** or **Remove**.

Using the (Totalled) fields

Any field with **(Totalled)** in its name will total that column based upon the grouping of the other selected fields.

Warning

Don't use a single and totalled field together, as you'll get incorrect results. For example, if you use the **[Time] Time** and the **[Time] Time (Totalled)** fields together you won't get accurate results.

If you want to create a Time report with, for example, time broken down by date, then use the **[Time] Time** field to list each entry. You can show time totalled by staff member or task name, then include these fields for task or staff. Select the **[Time] Time (Totalled)** field to consolidate the time entry by task or staff.

## What's next?

Practice Manager has a number of standard and sample reports you can run and modify. Read about [running reports in Practice Manager](Run-reports-in-Practice-Manager.md).