# Add a Visual to a Company Single Tool Report

Source: https://v2.support.procore.com/product-manuals/reports-company/tutorials/add-a-visual-to-a-company-single-tool-report

---

## Background

Make your report's data easier to interpret at a glance by adding a visual. You can create various charts, such as bar or line graphs, to highlight key trends, proportions, and comparisons.

## Things to Consider

- **Required User Permissions**

  - **360 Reporting**: 'Standard' level permissions or higher
  - **Data Source Tool**: 'Read Only' level permission or higher. See [How do 360 Reporting permissions work?](/faq-how-do-360-reporting-permissions-work)
- **Additional Information**

  - **Cloned Reports**: If you [make a copy of a report](/product-manuals/reports-company/tutorials/copy-a-company-single-tool-report), only you (the creator) can add new visuals.
  - **Data Limit**: The 'Add Visual' button only appears on reports with fewer than 2,500 records.
  - **Tab Limit**: You can only add [one visual per tab](/faq-why-is-the-add-visual-button-unavailable-on-a-single-tool-report).

## Steps

1. Navigate to the Company **360** **Reporting** tool.
2. In the **Reports** tab, locate the desired report.
3. Click the report to open it.
4. Click **+ Add Visual**.
5. Enter a name for the visual in the **Descriptive Title** box.
6. Under **Type of Visual**, select a visual for your report. The one you choose determines which calculation measures are available.

   | **Chart Type** | **Best Use Case** | **Available Measures** |
   | --- | --- | --- |
   | Bar | Comparing values across different categories or discrete time periods. | COUNT, SUM, AVG, MIN, MAX |
   | Donut | Displaying the relative proportions or percentage breakdown of a whole. | COUNT, SUM |
   | Line | Showing continuous trends and changes over a period of time. | COUNT, SUM, AVG, MIN, MAX |
   | Stacked Bar | Comparing categories while also showing the composition (part-to-whole) of each category. | COUNT, SUM, AVG, MIN, MAX |
   | Horizontal Bar | Comparing categories, especially useful when the category labels are long. | COUNT, SUM, AVG, MIN, MAX |
   | Gauge | Visualizing a single value against a set threshold to indicate performance (e.g., good, poor). | COUNT |
7. Click **Save**.
8. *Optional:* To export your report with your new visual, click **Export** and select **PDF with Visuals**.