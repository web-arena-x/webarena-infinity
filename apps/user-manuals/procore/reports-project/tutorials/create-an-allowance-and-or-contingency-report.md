# Create an Allowance and/or Contingency Report

Source: https://v2.support.procore.com/product-manuals/reports-project/tutorials/create-an-allowance-and-or-contingency-report

---

## Background

When setting up your project's budget, Procore recommends that clients set up both allowance and contingency cost types. To create new cost types in your company's Work Breakdown Structure, see [Add Company Cost](/process-guides/company-administration-work-breakdown-structure-guide/add-company-cost-types) [Types](/process-guides/company-administration-work-breakdown-structure-guide/add-company-cost-types). You can also assign your allowance or contingency cost type to your cost codes so that when your team later creates change orders, your budget line items can use the same cost code/cost type as the contract scope.

When you create a Prime PCO, each change order line item becomes a negative line item against the allowance/contingency and a positive line item against the purchase order or subcontract. Because allowance and/or contingency shows a net zero ($0) in the Prime Potential Change Order's log, you can create the report below to the 'Original Budget Amount' from your contingency and/or allowance 

A *Cost Code* identifies a specific type of work on a project to track its associated expenses, such as labor, materials, and equipment.

Cost Code[cost codes](/glossary-of-terms).

## Things to Consider

- **Required User Permissions:**

  - For information, see [Create a Project Single Tool Report](/product-manuals/reports-project/tutorials/create-a-project-single-tool-report).

## Steps

1. Navigate to the project **360 Reporting** tool.
2. Click **+ Create Report**.
3. Click **Single Tool Report**.
4. Complete the following information:

   - **Enter Report Name:** Type a name for your report. For example, type: Allowance & Contingency Report
   - **Enter Description:** Enter a descriptive summary of the report.
5. Under Select Tool, do the following:

   - Click **Financial Line Item**.
   - Click **Financial Line Item Details**.   
      This adds a 'Financial Line Item Details' tab to your report.
6. In the right pane, search for these columns and use a drag-and-drop operation to place them in your report:

   - *Optional:* **Project Name**. If you are creating a Company level report, add this column to each project's name.
   - **Cost Code**. This column shows the cost code.
   - **Type**. This column is included to group the report by type. The grouping will show how many dollars were used.
   - **PCO #**. This column provides the PCO number.
   - **Description**. This column provides the PCOs description.
   - **Amount**. This column shows the dollar amount.
7. Add a filter to your report as follows:

   - Click the **Add Filter** menu and choose **Type**.
   - In the secondary filter drop-down, mark these checkboxes:

     - **Original Budget**
     - **Prime Contract PCO**
8. Add another filter to your report as follows:

   - Click the **Add Filter** menu and choose **Cost Code**.
   - In the secondary filter drop-down, mark the checkbox that corresponds to your **Contingency** cost code.
9. At the top of the **Amount** column, click **fx** and select **SUM**.
10. Add a grouping to your report as follows:

    1. Click the **Group By** menu.
    2. Choose the following items:

       - ***Optional:*** **Project Name:** You only need to select this option if you are creating the report using the Company 360 Reporting tool.
       - **Cost Code:** This option will show cost code subtotals on the report.
       - **Type:** This option will show subtotals for how much is used.
11. Click **Create** to save your report.