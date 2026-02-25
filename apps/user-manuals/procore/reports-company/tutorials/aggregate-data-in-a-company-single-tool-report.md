# Aggregate Data in a Company Single Tool Report

Source: https://v2.support.procore.com/product-manuals/reports-company/tutorials/aggregate-data-in-a-company-single-tool-report

---

## Background

Use data aggregation functions to quickly make sense of your reports, instead of manually reviewing long lists of entries. These tools summarize an entire column of data into a single, insightful value such as *Sum*, *Count*, *Average*, *Min*, or *Max*. This lets you instantly analyze key metrics and spot trends directly within the report.

## Things to Consider

- **Required User Permissions:**

  - 'Admin' level permissions on the Company 360 Reporting tool  
     AND
  - 'Admin' level permissions on the Procore tool being used for the report's source data.

## Steps

1. Navigate to the Company **360 Reporting** tool.
2. Locate the report in the **Reports** tab.
3. Click the vertical ellipsis (â®) and choose **Edit**.
4. Open the **Group By** menu and choose one of the listed options.
5. Select an aggregate function by clicking the **fx** symbol in a column. Available functions depend on the data typeâfor example, **'**Count**'** is only available for non-numeric data:

   - **Count**: The number of values.
   - **Sum**: The sum of all values.
   - **Min**: The smallest value.
   - **Max**: The largest value.
   - **Average**: The average of all values.
6. Click **Update Report**.  
   A summary (*Count*, *Sum*, *Min*, *Max*, or *Average*) appears at the bottom of each column.