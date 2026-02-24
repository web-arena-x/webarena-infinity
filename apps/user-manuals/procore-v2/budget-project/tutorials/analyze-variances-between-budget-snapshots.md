# Analyze Variance Between Budget Snapshots

Source: https://v2.support.procore.com/product-manuals/budget-project/tutorials/analyze-variances-between-budget-snapshots

---

## Background

If you maintain a project's budget in Procore, you can record how your budget changes over time with the snapshot feature. You might want to create a snapshot at the end of each month, after you update your budget.

Every project team needs to know what is changing month-over-month, so that risk can be identified and mitigated. With the Analyze Variance feature in the Budget, you can compare snapshots directly to each other, or to your Current Budget, to identify variance down to the most granular, line-item level. This allows project teams to quickly and easily identify where things are shifting on the project, directly in the Budget, without the need for side spreadsheets.

## Things to Consider

- **Required User Permissions**:

 - To create a snapshot, 'Standard' level permissions or higher on the Project level Budget tool.
 - To view all snapshots created in a project, 'Read Only' level permissions or higher on the Project level Budget tool.
- **Additional Information:**

 - *The Budget view Analyze Variance tool does* ***not*** *allow comparison of quantity-based columns between snapshots or current data. Only columns that allow for aggregation (summary of values vertically) are included in this tool.*

## Prerequisites

- [Create a Budget Snapshot](/process-guides/budget-and-forecast-snapshots-user-guide/create-a-snapshot)

## Steps

### Analyze Line Item Variance on the Budget Tab

This action analyzes variance by comparing a snapshot with the active budget.

1. Navigate to the project's **Budget** tool.
2. Click the **Budget** tab and select a standard or custom budget view from the **View** menu.
3. Click **Analyze Variance**. 
    This opens the **Select Comparison Columns to Analyze Variance** window.
4. From the **Comparison Snapshot** menu, select the snapshot to compare it with your budget data.
5. Under **Columns to Display**, choose one (1) option:

   - **Comparison Column and Variance Column**. Shows both values.
   - **Comparison Column Only**. Shows the value from the comparison snapshot.
   - **Variance Column Only**. Shows the variance between the comparison snapshot and active budget.
6. Under **Comparison** **Columns**, mark one or more checkboxes to select the columns to analyze for variance.
7. Click **Save**. 
    Procore analyzes the current budget and snapshot for variance.

##### Example

This example shows the **Comparison Column and Variance Column** option using **Estimated Cost at Completion** as the comparison column. The blue column label shows the snapshot data. The column labeled **Variance** shows the difference between the snapshot and your budget.

### Analyze Aggregate Variance Between Snapshots on the Project Status Snapshots Tab

This action analyzes the aggregate variance between two snapshots.

1. Navigate to the project's **Budget** tool.
2. Click the **Project Status Snapshots** tab and select a standard or custom budget view from the **View** menu.
3. Click the snapshot **Name** to open it.
4. On a column where it's available, click the **Variance** icon.   
    This expands the column to show the **Current**, **Previous**, and the **Variance** between the two snapshots.

   ##### Example

   This example shows the **Current**, **Previous**, and **Variance** columns that appear when you click the **Variance** icon on a column.