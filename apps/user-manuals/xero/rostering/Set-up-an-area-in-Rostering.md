# Set up an area in Rostering (BETA)

Source: https://central.xero.com/s/article/Set-up-an-area-in-Rostering

---

## Overview

- Add a standard or non-worked type area in Rostering and advanced timesheets.
- Import multiple areas or edit existing ones using a CSV file.

Tip

Rostering and advanced timesheets is currently in closed beta and is restricted to a small number of users.

What you need to know

### About areas

Areas are the teams, groups or roles that work together in your organisation. For example, at a cafe you might have areas set up as Kitchen, Barista, and Manager.

Areas help to ensure employees know where they’re working for their shift and allow managers to designate certain employees to be preferred as working in a specific area.

You need system administrator access to set up an area.

### Non-worked type areas

A non-worked type area supports managers to schedule employees for a shift where the time won’t be calculated as part of the total time worked. It also won’t trigger overtime rates and stress limitations. This is a requirement in many industries, such as Healthcare with National Disability Insurance Scheme (NDIS) customers. The default shift cost is $0 for shifts that occur in a non-worked type area.

You can choose to allow employees to clock in and out or submit timesheets in a non-worked type area in the general settings.

If you create a shift in a non-worked type area, you can’t approve the timesheet that’s automatically generated for that shift. The timesheet will remain in **Pending** status.

Add an area

### Set up a standard area

1. In the **Payroll** menu, select **Rostering and advanced timesheets**.
2. In the **Settings** menu, select **Scheduling settings**.
3. Select **Areas**.
4. Enter the area name. Area names have a maximum length of 32 characters.
5. Click **Add**.

### Set up a non-worked type area

1. In the **Payroll** menu, select **Rostering and advanced timesheets**.
2. In the **Settings** menu, select **Scheduling settings**.
3. Select **Areas**.
4. If you haven’t created an area, enter a name for the area, then click **Add**.
5. Next to the area you want to set up as a non-worked type area, click **Edit**.
6. (Optional) Select a colour to represent the area and select any training requirements or preferred employees.
7. Click **Advanced area settings**.
8. Enable **Don’t count towards worked time?**
9. Click **Save**.

Import multiple areas

### What you need to know

You can use a CSV file to import multiple new areas or update existing areas. You need system administrator access to import multiple areas.

To create your import file, you can download a sample CSV template from Rostering and advanced timesheets or export your existing data. Edit or add to the file before importing it back into Rostering and advanced timesheets.

When preparing your import file, ensure the following:

- **Area Name** and **Location** are required fields.
- **Location** is the name of your Xero organisation.
- If you’ve exported your existing data, don’t edit the **Deputy ID** field. Any changes to this field can override existing areas. If you’re importing new areas, leave this field blank.
- The value of **Colour** must be in HEX colour code.
- Use a comma to add multiple training modules, for example Kitchen, Barista.

When you upload your file, Rostering and advanced timesheets will check the import file for any errors. The **Valid** filter will show all fields that’s ready to import. If there are any errors, these will show in the **Invalid** filter. Hover over the column name or click on the invalid field to learn more about the error. You can fix the error directly on screen or edit the import file, then re-upload it.

### Download a CSV template or export your existing data

1. In the **Payroll** menu, select **Rostering and advanced timesheets**.
2. In the **Settings** menu, select **Scheduling settings**.
3. Click the menu icon , then select **Manage areas via file**.
4. To:
   - Download a sample CSV template – Click **Add areas**, then next to **Download the area template**, click **Download**.
   - Export your existing area data – Click **Update areas** then next to **Download your area data**, click **Download**.
5. Select **CSV** or **Excel (XLSX)**.

### Import your file into Rostering and advanced timesheets

1. In the **Payroll** menu, select **Rostering and advanced timesheets**.
2. In the **Settings** menu, select **Scheduling settings**.
3. Click the menu icon , then select **Manage areas via file**.
4. If you're:
   - Adding new areas – Click **Add areas**.
   - Updating existing areas – Click **Update areas.**
5. Click **Continue to upload**.
6. Click **Upload file**, then select your CSV file from your computer.
7. Check the names of each column match, then click **Continue**.
8. Select the **Invalid** filer to correct any errors, then click **Submit**.

## What's next?

Now that you’ve created an area, edit the area to assign a colour, training requirements or preferred employees.