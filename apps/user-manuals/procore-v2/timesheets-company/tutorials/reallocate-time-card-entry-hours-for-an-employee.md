# Reallocate Timecard Entry Hours for an Employee

Source: https://v2.support.procore.com/product-manuals/timesheets-company/tutorials/reallocate-time-card-entry-hours-for-an-employee

---

## Background

You can split time on unapproved timecards into multiple entries. For example, you can change a 10-hour entry of 'Regular Time' into 8 hours of 'Regular Time' and 2 hours of 'Overtime' to reflect a worker's actual hours.

## Things to Consider

- [Required User Permissions](/product-manuals/timesheets-company/permissions)
- To reallocate time into multiple entries, the sum of each entry must equal the total hours of the original timecard.

## Steps

1. Navigate to the company's **Timesheets** tool.
2. Locate the timecard entry for the employee whose time you want to split.
3. Click the **Split Timecard**  icon on the timecard entry.
4. Split the Time.

   - **For project timecards using the 'Total Hours'**

     - Enter a smaller number of hours in the **Total Time** value column on the first timecard entry.
     - Enter the balance in the next timecard entry (or create multiple timecard entries to reallocate the balance). Your timecard entries must add up to the total number of hours of the original timecard entry. When finished, click **Save**.
   - **For project timecards configured to use the 'Start Time/Stop Time'**

     1. Change the values in the **Start Time** and **Stop Time** columns on the first timecard entry.
     2. An additional timecard entry is automatically created with the remaining hours for the original timecard.
     3. Continue to add entries to match the work performed as long as the **Total Time** of the original timecard entry remains the same.
5. *Optional:* Update the timecard entries.

   - **Project**. Select the appropriate project to reallocate the hours for each timecard entry.
   - **Sub Job**. Select the appropriate sub job to reallocate the hours for each timecard entry.
   - **Cost Code**. Select the appropriate cost code to reallocate the hours for each timecard entry.
   - **Time Type**. Select the appropriate time type to reallocate the hours for each timecard entry.
6. Click **Save**.