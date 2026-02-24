# Update the Financials Budget Report Parameters

Source: https://v2.support.procore.com/product-manuals/procore-analytics/tutorials/update-the-financials-budget-report-parameters

---

## Background

This tutorial shows you how to update the parameters in Procore Analytics Financials Budget Report using Power BI.

## Steps

1. Download a copy of your Financials Budget Report using one of these options:

   - Use the Procore Analytics Google Drive link.  
     OR
   - Download a copy from Power BI. To learn how, see [Download a Report from the Power BI Service to Power BI Desktop](https://learn.microsoft.com/en-us/power-bi/create-reports/service-export-to-pbix).
2. Open the file in the Microsoft Power BI Desktop application.
3. Click **Transform Data** and choose **Edit Parameters**.
4. In the **Edit Parameters** page, do the following:

   - **ReportName**. Keep the report name specified with the downloaded file. For example: `Procore Financials Budget`.
   - **Release Version**. Keep the version number specified with the downloaded file.
   - **Budget View Name**. Type the name of your company's budget view in this box.

     ##### Â Note

     Procore's default budget view is the 'Procore Standard Budget View.' See [About the Procore Standard Budget](/product-manuals/budget-project/tutorials/about-the-procore-standard-budget-view) [View](/product-manuals/budget-project/tutorials/about-the-procore-standard-budget-view). Keep in mind that the budget views and columns in your specific budget view may be different.

     - To learn about Procore's budget views, see [What are Procore's standard budget views?](/faq-what-are-procores-standard-budget-views) and [What are Procore's standard budget views for ERP Integrations?](/faq-what-are-procores-standard-budget-views-for-erp-integrations)

- **Forecast View Name**. Type the name of your company's forecasting view in this box.

  ##### Â Note

  Procore's default forecasting view is the 'Procore Standard Forecast View.' This is an optional feature that can be turned ON/OFF in Procore projects. To learn more, see [About the Procore Standard Forecast View](/product-manuals/budget-project/tutorials/about-the-procore-standard-forecast-view).

- Click **Transform Data**.
- In the **Queries** panel, click the **Budget** table.

  ##### Â Note

  - The steps below illustrate changes on the Budget table. However, you must perform these steps on both the **Budget** and **Budget2** queries.
  - If your company's projects are using optional Advanced Forecasting feature, you must also perform these steps on the Procore Standard Forecast View. See [About the Procore Standard Forecast View](/product-manuals/budget-project/tutorials/about-the-procore-standard-forecast-view).