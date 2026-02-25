# Create a Custom Report for Action Plans

Source: https://v2.support.procore.com/product-manuals/action-plans-project/tutorials/create-a-custom-report-for-action-plans

---

## Things to Consider

- **Required User Permissions:**

 - *To create a custom report with action plans data in the Company level Reports tool:*\* 'Read Only' level permissions or higher on the project's Action Plans tool. 
     AND\* 'Standard' level permissions or higher on the Company level Reports tool.
 - *To create a custom report with action plans data in the Project level Reports tool:*\* 'Read Only' level permissions or higher on the project's Action Plans tool. 
     AND\* 'Standard' level permissions or higher on the Project level Reports tool.

## Steps

1. Navigate to the Company level **Reports** tool. 
    OR Navigate to the Project level **Reports** tool.
2. Click **Create Report**.
3. Click **Create New Report**.
4. Add a name and description for your new report as follows:

   1. **Enter Report Name**. Click the icon and then type a name for your report in this field.
   2. **Enter Description**. Click the icon and then type a descriptive statement for your report in this field.
5. In the 'Select Tool' menu, click **Action Plans**.
6. Click **Add Tab** and select a Procore project tool for the new report tab's source data: 
   *Note:* By default, Procore uses 'Action Plans' as the name the tab.
7. *Optional:* To rename the tab, do the following:

   1. Click gray gear icon next to the tab name.
   2. In the **Edit Tab** window, type a new **Title** for the selected tab.
   3. Click **Update**.
8. Add columns to your report as follows:

   - To add a column, use a drag-and-drop operation to move a column from the right pane into the body of your report.   
      OR
   - To add all of the available columns, click **Add All**.   
      OR
   - To change the position of a column, use a drag-and-drop operation to move the column to the desired position in the report table.   
      OR
   - To remove all of the columns from your report, click **Remove All**.
9. Once you've added the desired columns, you have these options:

   - **Aggregate data** Click **fx** in the column heading and select one of the following (for numeric values): count, sum, min, max, or average.
     *Notes:*\* Once the report is created, you will see the count, sum, min, max, or average of the values at the bottom of the column.\* For field types that are not a numeric value, you have the option to aggregate by count.
   - **Change the column order** Use a drag-and-drop operation to place the column into the desired position.
   - **Filter your report data** Click the **Add Filter** drop-down menu to select what you would like to filter by. Once you've specified a filter, you can add another filter. You can also filter data by date range by selecting a start and end date.
   - **Group report data** In the **Group by** list, select one of the items in the drop-down menu to group report data by the specified column (e.g., you may want to group data by the responsible contractor).
10. *Optional:* If you want to add additional tools to your report, click **Add Tab** and select the tool. Then repeat the steps above.
11. Click **Create Report**.