# Create Custom 360 Reports with Visuals and Dashboards (Beta)

Source: https://v2.support.procore.com/product-manuals/reports-company/tutorials/create-custom-360-reports-with-visuals-and-dashboards

---

## Background

360 Reporting offers multiple visual formats, such as bar graphs, tables, and scorecards, allowing you to choose the best way to represent your data. Because each visual type has unique requirementsâlike defining axes for a graph versus selecting columns for a tableâthe specific configuration steps will vary depending on the format you select.

## Things to Consider

- **Required User Permissions**:

  - [How do 360 Reporting permissions work?](/faq-how-do-360-reporting-permissions-work)

## Steps

With the 360 Reporting tool, users can select from these custom data visuals when creating new reports:

    

With the 360 Reporting tool, users can select from these custom data visual types when creating new reports:

    

##### Tip

**New to 360 Reporting?** See these learning resources:

- To learn the basics, see .
- For information about 360 Reporting data sets, see [360 Reporting: Data Guide](/process-guides/enhanced-reporting-data-guide/).

Expand the steps below to learn how to create your own reports using the **Create Visuals** option.

### Tabular Report

A **tabular report** organizes data into a grid of rows and columns for detailed granular data needs.

To configure a report:

##### Best Practice

**How many columns should you include in a report?** The number of columns in your table depends on the data being presented, your goal, and the medium (online vs. print). Some best practices when building reports are:

- Avoid overwhelming the user and include only the columns necessary to understand the data or complete a task.
- When building a report for print, consider the physical page width and font legibility.

1. Navigate to the **360 Reporting** tool.
2. Click **Create Report**. Then select the **360 Report (Visuals and Dashboards)** option.
3. Select the **Tabular Report** tile and click **Continue** again.
4. Select a data set tile and click **Continue** again. For data sets, see [360 Reporting: Data Guide](/process-guides/enhanced-reporting-data-guide/).
5. On the **Visual** tab, use the **Search Columns** box or expand the arrows to find and mark the checkboxes for the columns to add.
6. *Optional:* Apply **Filters** or **Calculations**. See [Configure Filters, Calculations, and Info for 360 Reports](/product-manuals/reports-company/tutorials/configure-filters-and-calculations-for-custom-360-reports).
7. The **Load Data Manually** toggle is turned ON by default to improve performance for large data sets. You can choose to turn this feature OFF.
8. Click **Add to 360 Report**. To add another visual, click **Add Visual** and repeat the steps.
9. When finished, click **Save**.

### Vertical Bar Graph

A **vertical bar graph** uses vertical bars of varying heights to compare the quantities of different categories side-by-side.

To configure a report:

##### Best Practice

**How should you configure your vertical bar graph for clarity?** A vertical bar graph is excellent for comparing a numeric value (like *Cost* or *Count*) across distinct categories (like *Assignee* or *Project Name*). To ensure your chart is effective and easy to read, consider these best practices:

- **Limit the Number of Bars:** Avoid overwhelming users with too many bars. Use the **Max Bars Displayed** setting to focus on the most relevant data (e.g., the Top 10 or 15 categories).
- **Sort Your Data Logically:** Since categories on the **Horizontal Axis** (like 'Name' or 'Assignee') often have no natural order, sort the chart by the **Bar Measure** (i.e., numeric value) in **Descending** or **Ascending** order. This makes it easier to compare values by identify highs and lows.
- **Use Clear Formatting:** Use the **Display Units** (e.g., 'Thousands', 'Millions') to simplify large numbers on the Y-axis, and consider turning the **Show Value Labels** toggle ON if precise values are important to your audience.

1. Navigate to the **360 Reporting** tool.
2. Click **Create Report**, select the **360 Report Visuals and Dashboards Open Beta** option and click **Continue**.Â
3. Select the **Vertical Bar Graph** tile, click **Continue**, select your data set, and click **Continue** again.Â For data sets, see [360 Reporting: Data Guide](/process-guides/enhanced-reporting-data-guide/).
4. Set the **Vertical Axis (Y-Axis)**: Click the **Bar Measure** menu and select a numeric field (e.g., 'Cost', 'Count') and a **Color**.
5. Set the **Horizontal Axis (X-Axis)**: Click the **Horizontal Axis** menu and select a category field (e.g., 'Assignee', 'Name').
6. *Optional:* Turn the **Show Value Labels** toggle ON to include value labels on the chart.
7. Set the chart's **Sort by** setting by selecting **Ascending** or **Descending** for the **Bar Measure** or **Horizontal Axis**.
8. Expand **Advanced Options** to configure settings like **Max Bars Displayed**, **Display Units**, and **Vertical Axis Min/Max**.