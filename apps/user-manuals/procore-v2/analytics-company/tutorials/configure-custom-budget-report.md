# Configure a Custom Budget Report

Source: https://v2.support.procore.com/product-manuals/analytics-company/tutorials/configure-custom-budget-report

---

## Background

The Analytics 2.0 Financials Budget Report (Custom) allows users to view budget data. You can also modify the report to view the data that's most important to you.

## Things to Consider

- [Required User Permissions](/product-manuals/analytics-company/permissions)
- Intermediate Power BI development knowledge is recommended.
- When editing a visualization, the fields used in it will be marked as 'checked' when selected, making it easier to identify and modify formulas.
- For details on changing the data type of columns in your custom budget view, see Microsoft's [Data types in Power BI Desktop](https://learn.microsoft.com/en-us/power-bi/connect-data/desktop-data-types) article.
- For details on the Applied Steps list, see Microsoft's [Using the Applied Steps list](https://learn.microsoft.com/en-us/power-query/applied-steps) article.

## Steps

- Select Budget Views
- Modify Visuals in the Report View

### Select Budget Views

1. Open Power BI Desktop.
2. Go to the top menu bar and click the **Transform data** drop-down.
3. Select **Data source settings**.
4. Select **Edit Permissions**.
5. Click **Edit**.
6. Enter the token you received from Analytics 2.0.
7. Click **Save**.
8. Click **OK**.
9. Click **Close**.
10. Open **Query Editor (Transform Data)**.
11. Open **CustomBudgetViews**.
12. Filter **[name]** to correct view. 
     Needed if multiple companies with different views, or multi-select budgets enabled.
13. Open **CustomForecastingViews**.
14. Filter **[name]** to correct view. 
     Needed if there are multiple companies with different views, or if multi-select budgets is enabled.
15. Steps 10-14 will filter needed queries to correct views.
16. Open **Budget**.
17. Go to 'Select Budget View Columns' step.
18. Click the **gear** icon.
19. Select columns from the checkbox dialog box (may need to click 'load more').
20. Click **OK**.
21. Change Column Types to the appropriate type (in most cases, this will be decimal). 
     This can be inserted as a new step to the 'Applied Steps' or done as the last step in the query.
22. Open **BudgetSnapshots**.
23. Go to 'Select Budget Snapshot Columns' step.
24. Click the **gear** icon.
25. Select columns from the checkbox dialog box (may need to click 'load more').
26. Click **OK**.
27. Change Column Types to the appropriate type (in most cases, this will be decimal). 
    This can be inserted as a new step to the 'Applied Steps' or done as the last step in the query.
28. Click **Apply Changes**.

### Modify Visuals in the Report View

When editing a visualization, the fields used in it will be marked as 'checked' when selected, making it easier to identify and modify formulas

#### Budget Insights report

1. Add view columns to the Budget Summary visual.

   - Fields can be selected by marking the check box from the fields pane.
   - By default, the field appears as 'Sum of [field name]'.

     - You can edit this by double-clicking on the field name in the **Values** section of your visualization page.
   - Repeat this process for all of your budget columns.
2. Edit % Committed visual.

   - There is a % committed formula that uses [Revised Budget] and [committed Costs]. If these fields do not exist in your view, you will need to replace them with other fields.
   - The formula can be edited by selecting the formula from the fields pane on the right and then editing the formula in the 'formula bar'.
3. Edit Revised Budget vs Estimated Cost at Completion visual.

   - By default this visual uses [Revised Budget] and [Estimated Cost at Completion].
   - Replace these with relevant fields if necessary.
4. Edit Budget vs Committed Cost visual.

   - By default this visual uses [Revised Budget], [Committed Costs], and [Project over Under]
   - Replace these with relevant fields if necessary.

#### Key Influencers

1. Edit the 'Overbudget Influencers' visual.
2. This visual uses a formula to show 'Over Budget' or 'Not Over Budget'. See the formula below: 
    Budget Indicator = IF(Budget[Projected over Under] <0, 'Overbudget', 'Not Overbudget')
3. Edit the formula.
4. Replace [Projected over Under] with the relevant fields if necessary.

#### Root Cause Analysis

1. Edit the 'Budget Detail' visual.
2. Replace [Projected over Under] with the relevant fields if necessary.
3. Edit 'Budget Summary' visual.
4. Fields can be selected by marking the check box from the fields pane.
5. By default, the field will appear as 'Sum of [field name]'. You can edit this by double-clicking on the field name in the **Values** section of your visualization page.

#### Budget Detail

1. Edit the 'Budget Summary' visual.
2. Fields can be selected by marking the check box from the fields pane.
3. By default, the field will appear as 'Sum of [field name]. You can edit this by double-clicking on the field name in the **Values** section of your visualization page.

#### Budget Benchmarking

1. Edit vCost/USF formula.
2. Replace [Revised Budget] with the relevant field if necessary.
3. Edit vCost/USF for AVG Chart formula.
4. Replace [Revised Budget] with the relevant field if necessary.

#### Budget Snapshot Insights

1. Add view columns to the 'Budget Summary' visual.
2. Fields can be selected by marking the check box from the fields pane.
3. By Default the field will appear as 'Sum of [field name]' .
4. You can edit this by double-clicking on the field name in the **Values** section of your visualization Pane.
5. Edit 'Projected Over Under' visual.
6. Replace [Projected over Under] with the relevant field if necessary.

#### Budget Snapshots Over time

1. Replace [Projected over Under] with the relevant field if necessary.
2. Other budget fields can be added to this visualization to see a trend through your snapshots over time.

#### Budget Snapshot Comparison

1. This page has a number of formulas to change in order for the comparisons to work correctly. By default, this page compares Revised Budget, Job to date costs, and Projected Over Under.
2. Formulas that may need to be changed:

   - **vValueRevBgt1** = IF([vShowVariance] = 1, ALCULATE(SUM(BudgetForComparison2[Revised Budget]), SERELATIONSHIP(BudgetForComparison2[vBudgetCompareKey], Selection1[vBudgetCompareKey])), 0)\* Replace [Revised Budget] if necessary
   - **vValueRevBgt2** = IF([vShowVariance]= 1, CALCULATE(SUM(BudgetForComparison2[Revised Budget]), USERELATIONSHIP(BudgetForComparison2[vBudgetCompareKey], Selection2[vBudgetCompareKey])), 0)\* Replace [Revised Budget] if necessary
   - **vValueJTDCosts1** = IF([vShowVariance]= 1, CALCULATE(SUM(BudgetForComparison2[Job to Date Costs]), USERELATIONSHIP(BudgetForComparison2[vBudgetCompareKey], vSelection1[vBudgetCompareKey])), 0)\* Replace [Job to date Costs] if necessary
   - **vValueJTDCosts2** = IF([vShowVariance]= 1, CALCULATE(SUM(BudgetForComparison2[Job to Date Costs]), USERELATIONSHIP(BudgetForComparison2[vBudgetCompareKey], Selection2[vBudgetCompareKey])), 0)\* Replace [Job to date Costs] if necessary
   - **vValueEst1** = IF([vShowVariance]= 1, CALCULATE(SUM(BudgetForComparison2[Estimated Cost at Completion]), USERELATIONSHIP(BudgetForComparison2[vBudgetCompareKey], vSelection1[vBudgetCompareKey])), 0)\* Replace [Estimated Cost at Completion] if necessary
   - **ValueEst2** = IF([vShowVariance]= 1, CALCULATE(SUM(BudgetForComparison2[Estimated Cost at Completion]), USERELATIONSHIP(BudgetForComparison2[vBudgetCompareKey], vSelection2[vBudgetCompareKey])), 0)\* Replace [Estimated Cost at Completion] if necessary

#### No changes or configurations are needed for the following report pages:

- Budget Modifications
- Budget Changes
- Advanced Forecasting
- Cost vs Schedule
- Change Events