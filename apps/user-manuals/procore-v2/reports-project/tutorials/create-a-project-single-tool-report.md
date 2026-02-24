# Create a Project Single Tool Report

Source: https://v2.support.procore.com/product-manuals/reports-project/tutorials/create-a-project-single-tool-report

---

## Background

The 360 Reporting tool gives users the ability to create, generate, and export customized reports. When designing a report, its author can include data captured by specific Procore tools, specify the desired column layout, and also define how to group and filter report data. After generating a report, it can also be exported from Procore into Microsoft Excel.

## Things to Consider

- **Required User Permissions:**

  - *To create a single tool project report*, 'Standard' permissions or higher on the project 360 Reporting tool, plus permissions for the data source tool:

    - **Directory**: 'Admin' level permissions.
    - **Financial Management Tools**: 'Standard' level permission or higher.
    - **All Other Tools** (Core, Project Management, Quality & Safety): 'Read Only' level permissions or higher.
  - *To create a 360 project report:* 'Standard' level permissions or higher on the Project 360 Reporting tool, with additional permissions depending on the field group.
- **Additional Information:**

  - Custom reports are only visible and available to the individual who created them.
  - Reports can include data from these Procore tools and sources:

## Steps

### Create a New Custom Report

1. Navigate to the Project **360 Reporting** tool.
2. Click **Create Report** in the top right corner.
3. Click **Single Tool Report**.
4. You will then have the option to Create a New Report or choose an existing template. To create a brand new report, click the Create New Report tile.
5. Enter in the report name by clicking the pencil icon next to Enter Report Name.
6. Enter in a description of the report by clicking the pencil icon next to Enter Description.
7. In the right pane is a list of tools you can report on. Select a tool you wish to report on.
8. Once you have selected a tool, the right pane will populate with a list of columns you want to add to your report. Drag and drop columns into your report, or add all of the columns by clicking **Add All**.

   1. Once you've added the desired columns, you have these options:

      - **Group report data**  
         In the **Group by** list, select one of the items in the drop-down menu to group report data by the specified column (e.g., you may want to group data by the responsible contractor).
      - **Filter your report data**  
         Click the **Add Filter** drop-down menu to select what you would like to filter by. Once you've specified a filter, you can add another filter. You can also filter data by date range by selecting a start and end date.
      - **Change the column order**   
         Use a drag-and-drop operation to place the column into the desired position.
      - **Aggregate data**  
         Click the ***fx*** in the column and select one of the following (for numeric values): count, sum, min, max, or average. Once the report is created, you will see the count, sum, min, max, or average of the values at the bottom of the column. For field types that are not a numeric value, you have the option to aggregate by count.
9. To add a new tool to your report, click Add Tab at the top of the report and repeat step 6-7 above.

When finished configuring your report layout, click Create Report.

### Create a New Single Tool Report

1. Navigate to the Company **360** **Reporting** tool.
2. Click **Create Report**.
3. Click **Single Tool Report**.
4. Add a name and description for your new report as follows:

   1. **Enter Report Name**. Click the pencil icon and then type a name for your report in this field.
   2. **Enter Description**. Click the pencil icon and then type a descriptive statement for your report in this field.
5. Click **Add Tab** and select a Procore project tool for the new report tab's source data:

   ##### Â Notes

   - You are limited to choosing one (1) Procore project tool as the source for each tab in your report.
   - You can add multiple tabs to a report.
   - You can choose from multiple options by clicking the arrow for some tools. For example, in the illustration below, you can expand the **Meetings** tool and choose **Meeting Items**.
   - By default, Procore uses the selected tool or item name as the name of your report tab.

  
 - (Optional) If you want to change the default name of the report tab, do the following:

  1. Click GRAY cog icon next to the tab.
  2. In the **Edit Tab** window, type a new **Title** for the selected tab.
  3. (Optional) To change the source tool for the tab, choose the tool from the **Associated Tool** drop-down list.
  4. Click **Update** to save your changes.
- Add columns to your report as follows:

  - To add a column, use a drag-and-drop operation to move a column from the right pane into the body of your report.
  - To add all of the available columns, click **Add All**.
  - To change the position of a column, use a drag-and-drop operation to move the column to the desired position in the report table.
  - To remove all of the columns from your report, click **Remove All**.
- Once you've added the desired columns, you have these options:

  1. **Aggregate data**  
      Click the ***fx*** in the column and select one of the following (for numeric values): count, sum, min, max, or average. Once the report is created, you will see the count, sum, min, max, or average of the values at the bottom of the column. For field types that are not a numeric value, you have the option to aggregate by count.
  2. **Change the column order**   
      Place the column into the desired position using a drag-and-drop operation.
  3. **Filter your report data**  
      Click the **Add Filter** drop-down menu to select what you would like to filter by. Once you've specified a filter, you can add another filter. You can also filter data by date range by selecting a start and end date.
  4. **Group report data**  
      In the **Group by** list, select one of the items in the drop-down menu to group report data by the specified column (e.g., you may want to group data by the responsible contractor).
- *Optional:* If you want to add additional tools to your report, click **Add Tab**. Then repeat the steps above.
- Click **Create Report** to save the changes.

### Create a Report from a Template

Templates enable you to build reports without starting from scratch.

1. Navigate to the Company **360** **Reporting** tool.
2. Click the **Templates** tab.
3. Click **Preview** under one of the available report templates. See [What report templates are available in the 360 Reporting tools?](/faq-what-report-templates-are-available-in-the-360-reporting-tools)
4. A preview of your data in the report will load. To create a report from this template, click **Use Template**.  
    Your report is created and can be found under "My Reports" in the 360 Reporting tool.