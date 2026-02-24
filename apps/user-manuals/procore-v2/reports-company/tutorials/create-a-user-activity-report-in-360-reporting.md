# Create a User Activity Report in 360 Reporting

Source: https://v2.support.procore.com/product-manuals/reports-company/tutorials/create-a-user-activity-report-in-360-reporting

---

## Background

The User Activity Dataset allows you to create 360 Reports that show how people use Procore. You can audit your company's activity by tracking specific tools, actions, and users over time. This information provides administrators and managers with insights into company-wide Procore adoption, enabling them to audit employee activity in cases of errors or platform misuse.

##### Â Tip

**What are the key differences between User Activity Reporting and the legacy User Sessions Report?** The User Activity Report offers a more powerful and flexible way to see what's happening in your account. Here are the key advantages:

- **Get a longer, more complete history.** You can track activity over 31 daysâa major increase from the 7-day limit in the User Sessions Reportâand view actions from both web and mobile apps.
- **Build highly specific reports.** Create a custom view with the exact fields you need. You can then filter by any data point (like 'Actor Email' or 'Event Type') to get granular insights, even without adding those fields as columns.

## Things to Consider

- **Required User Permissions**

  - To create a user activity report, 'Admin' level permissions on the 360 Reporting tool.

    - To include company-wide activity, 'Admin' level permissions on the Company Directory.
    - To include project-specific activity, 'Admin' level permissions on the Project Directory for the project(s):

      - **If you have 'Admin' on a Project Directory:** When you run a report, you will see a full audit trail for users on that project.
      - **If you do not have 'Admin' on a Project Directory:** That specific project's data will either be blank or excluded from your report results, even if you are the report creator.
- **Additional Information & Limitations**

  - User Activity reports utilize a single dataset with no joins.
  - Reports created with the User Activity dataset cannot be distributed.
  - Exported reports are limited by row count: **CSV** (700,000), **Excel** (200,000), and **PDF** (5,000).
  - Users can click the Object ID in the report to jump straight to an item.

## Steps

Follow these steps to build a user activity report.

### Start Your Report

1. Navigate to the **Company 360** or **Project 360** Reporting tool.
2. Click **Create Report**, choose **Create 360 Report**, then select the **Create 360 Report** tile.

### Select Your Data

1. Click **Select Data Set > Product Area.**
2. Choose **User Activity**.

### Configure Columns

To get started, open the **Columns** panel by clicking the columns icon in the right sidebar.

#### Add Columns

- To find a field, enter a keyword in the **Search** box.
- To browse, click the **>** arrow to expand a field group.
- Mark the check box next to a field name to add it as a column.

#### Arrange and Resize Columns

- **Move a Column:** Click and drag the column header to a new position.
- **Resize a Column:** Hover over the vertical line next to a column's header until the **â** cursor appears, then click and drag to adjust the width.

#### Additional Column Options

Click the vertical ellipsis (**â®**) on a column header for more actions:

- **Group by:** Organizes your report by the values in this column.
- **Pin Column:** Freezes the column on the left side of the view.
- **Autosize This Column:** Adjusts the selected column's width to fit its content.
- **Autosize All Columns:** Adjusts all columns to fit their content.

### Apply Filters

Use filters to narrow down the data in your report. A field doesn't need to be a column to be used as a filter.

1. Open the **Filters** panel by clicking the filters icon in the right sidebar.
2. Click **Add Filters** and select a field from the list or use the search bar.
3. Configure the filter based on its data type:

   - **For Text Fields:** Choose to **Include** or **Exclude** values, then select one or more values from the drop-down menu.
   - **For Date Fields:** Select a preset range (e.g., *This Month*), a *Fixed Date Range* with a start/end date, or a *Custom Time Period*.
   - **For Yes/No Fields:** Select **Yes**, **No**, or **None**.
4. To remove a filter, click the **X** next to its name. To clear all filters at once, click the vertical ellipsis (**â®**) at the top of the Filters panel and select **Delete all filters**.

### Group Data

Grouping organizes your report by stacking rows that share a common value (e.g., grouping all tasks by 'Project Name').

1. To create a group, click the vertical ellipsis (**â®**) on a column header and select **Group by**.
2. To manage your groups, click the **Table Groups** button at the top of the report.

   - **Rearrange:** Click and drag the vertical grip icon (**â®â®**) to reorder the groups.
   - **Remove:** Click the **X** next to a group's name to remove it.
3. Click **Update** to save your changes.