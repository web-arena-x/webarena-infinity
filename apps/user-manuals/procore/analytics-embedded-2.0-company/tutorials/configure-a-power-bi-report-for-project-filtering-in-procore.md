# Configure a Power BI Report for Project Filtering in Procore

Source: https://v2.support.procore.com/product-manuals/analytics-embedded-2.0-company/tutorials/configure-a-power-bi-report-for-project-filtering-in-procore

---

## Background

For a Power BI report to be automatically filtered by the selected project in Procore, it must contain a specific table and column used by the Procore Analytics Embedded app. The required naming convention is:

- Table Name: `projects`
- Column Name: `project_id`

Older versions of Procore Analytics 2.0 reports or custom reports often use different names, such as `Project` for the table and `id` for the column. Use the steps below to rename them to match Procore's requirements.

## Steps

Follow these steps to update the necessary fields in your Power BI report:

1. Open your report in Power BI desktop.
2. Rename the table:

   1. Right-click the table name and select **Rename** (or double-click it).
   2. Change the name to **`projects`**.
3. Rename the column:

   1. Right-click the column name and select **Rename** (or double-click it).
   2. Change the name to **`project_id`**.
4. Save the report.
5. Proceed to [Retrieve a Report's Embed URL from the Power BI Service](/product-manuals/analytics-embedded-2.0-company/tutorials/retrieve-a-reports-embed-url-from-the-power-bi-service).