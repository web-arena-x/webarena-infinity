# Use the 'Forecast to Complete' Feature

Source: https://v2.support.procore.com/product-manuals/budget-project/tutorials/use-the-forecast-to-complete-feature

---

## Background

To ensure that future activities and costs on your project remain accurate and consistent, it is important to actively manage and monitor your project's budget. If that activity is your responsibility (for example, if you are a project manager or project accountant), you may have a need to generate weekly or monthly reports to clearly account for all your project's billable costs (in other words, *what has been completed on the project*) and projected costs (in other words, *what remains to be completed on the project*).

To help your project team gain a greater understanding of what remains to be completed on a project, a 'Forecast to Complete' column is included, by default, on several of the Budget tool's 'Standard Views' (for example, *Procore Standard Budget*, *Blank Budget View*, *(Multi-Level) Procore Standard Budget*, and *Procore ERP Direct Cost Budget*). This column can also be added to any customized budget views that you choose to create. See [Set up a New Budget View](/process-guides/project-equipment-user-guide/assign-the-budget-view-to-a-procore-project).

With the 'Forecast to Complete' column, you can:

- **Estimate the 'Projected Over/Under' cost for each budget line item** This ensures that the total in the 'Estimated Cost at Completion' column is accurate and consistent with your previous weekly or monthly projection.
- **Choose the calculation method to apply on a per-line item basis**

 - The *Automatic Calculation* setting calculates the remaining project costs based on the difference between the 'Projected Budget' and the 'Projected Costs' in order to maintain a net-zero ($0) 'Projected Over/Under' value for each budget line item.
 - The *Manual Entry* setting lets you add items and amounts to define a more realistic forecasting number based upon key job insights.
 - The *Monitored Resources* setting lets you add time/duration based items that automatically drawdown as time progresses throughout the project.
- **Add forecasting notes** Record a helpful note that documents the reasoning for the forecasted value for each budget line item. There is no limit on the number of characters you can enter on a note.

## Things to Consider

- **Required User Permissions:**

 - 'Standard' level permissions or higher on the project's Budget tool.
- **Additional Information:**

 - You can configure the 'Forecast to Complete' setting to *Automatic Calculation,* *Manual Entry,* or *Monitored Resources* on a per-line-item basis.
 - You can add notes to each line item.
 - The 'Notes' entry is preserved if you decide to switch between *Automatic Calculation,* *Manual Entry*, and *Monitored Resources*.
 - ***Important!*** When you switch from *Manual Entry* to *Automatic Calculation*, all previously added *Manual Entry* items will be deleted.
- **Net Zero Calculations:**

 - A user with 'Admin' permissions on the Budget tool can configure the 'Forecast to Complete' column to have an automatic net-zero calculation under the Budget tool's configuration settings. 
    *Note*: This setting is applied only to new line items that you add to the budget.
 - A lightning bolt icon in the 'Forecast to Complete' column indicates the automatic net-zero calculation has been applied.
 - A question mark **?** icon indicates the 'Forecast to Complete' column cannot be changed. See [Add a Partial Budget Line Item](/product-manuals/budget-project/tutorials/add-a-partial-budget-line-item).
- **For companies using the ERP Integrations tool:**

 - You can export cost forecast from Procore to some integrated ERP systems. See [How do I export cost forecast data from a Procore budget to ERP?](/faq-how-do-i-export-cost-forecast-data-from-a-procore-budget-to-erp)

## Prerequisites

- [Set up a New Budget View](/process-guides/project-equipment-user-guide/assign-the-budget-view-to-a-procore-project)

## Steps

1. Navigate to the project's **Budget** tool.
2. Click the **Budget** tab.
3. Locate the budget line item that you want to examine.
4. In the **Forecast to Complete** column, click the link to the right of the lightning bolt icon.
5. Select the desired calculation method:

   - Automatic Calculation
   - Manual Entry
   - Lump Sum Entry (Forecasting Tab)
   - Monitored Resources

### Automatic Calculation

Follow the steps below to enable the A\_utomatic Calculation\_ option on a budget line item. Automatic calculation is the default setting in the project's Budget tool. This option calculates the difference between the values in the 'Projected Budget' and 'Projected Costs' columns. That difference is displayed as the value in 'Project Over/Under' column.

After clicking the link in the **Forecast to Complete** column next to the lightning bolt icon, do the following:

1. In the **Forecast to Complete** section that appears below the table in the Budget tab, choose the **Automatic Calcu**lation option.
2. *Optional:* Enter any relevant information about the forecast in the **Notes** box.
3. Click the close icon at the top right of the **Forecast to Complete** section to close it.

### Manual Entry

After clicking the link in the **Forecast to Complete** column next to the lightning bolt icon, do the following:

1. Under **Calculation Method**, choose the **Manual Entry** option.
2. *Optional:* Enter any relevant information in the **Notes** box.
3. *Optional:* To add line items, click **Add new line item**.

   1. For each line item, enter the following:

      - **Description** Enter a description for the new line item.
      - **Quantity** Enter a quantity. By default, the entry is set to 1.
      - **Units** Select a unit of measure (see [Which units of measure are included on Procore's master list?](/faq-which-units-of-measure-are-included-in-procores-master-list)). The default selection âlsâ (lump sum).
      - **Unit Cost** Enter the cost per unit. For example, type: 100.00. The default entry is zero (0.00).
      - **Amount** Enter the total cost associated with the line item. This is the number of units multiplied by the unit cost.
   2. Add line items as needed.
4. Depending on the experience you are using, click **Done** or close icon save your changes and return to the budget.

### Lump Sum Entry (Forecasting Tab)

This Lump Sum Entry method should be used when you want to input a single figure to forecast the remaining cost at completion for a specific budget code in a project's budget. In the Budget tab, Procore populates the 'Lump Sum Entry' amount with the 'Forecast to Complete' amount. If you want to input a different amount, you must edit the amount in the 'Forecasting' tab. To learn how to set up a forecasting view, see [Set Up a New Forecasting View](/product-manuals/admin-company/tutorials/set-up-a-new-forecasting-view).

1. Click the **Forecasting** tab.
2. Click the link in the **Forecast to Complete** column next to the lightning bolt icon, do the following.
3. Under **Calculation Method**, choose the **Lump Sum Entry** option.
4. Enter a lump sum amount in the text box.

   ##### Â Important

   Because your lump sum entry overrides the 'Forecast to Complete' amount in the budget, it is important to understand the implication that using this calculation can have on your overall budget forecast.

- *Optional:* Enter any relevant information in the **Notes** box.
- Depending on the experience you are using, click **Done** or close icon save your changes and return to the budget.

### Monitored Resources

The 'Monitored Resources' column forecasts your projected costs based on the resource rates and time and then introducing resources, applying a time and date, and adding a unit cost and utilization rate for resources within a budget code. Procore automatically draws down the 'Forecast to Complete' amount as time passes.

After clicking the link in the **Forecast to Complete** column next to the lightning bolt icon:

1. Under **Calculation Method**, choose the **Monitored Resources** option.
2. *Optional:* Enter any relevant information in the **Notes** box.
3. *Optional:* To add an additional entries, click **Add new line item**.

   1. For each line item, enter the following:

      - **Description** Enter a description for the new resource line item.

        ##### Example

        Examples include:

        - Project Manager Level 1, Level 2
        - Office Trailer Rental
        - Temporary Toilet Facilities
        - Temporary Storage Container Rental

- **Start Date** Select a start date the resource's line item.
- **End Date** Select an end date for the resource's line item.
- **Units Remaining** Choose *Weeks* or *Months*. Weeks is the default selection. Procore uses today's date to automatically calculate the 'Units Remaining' value and continues to draw down the remaining amount at the end of each week or month.
- **Unit Cost** Add the cost per unit. The default setting is zero (0.00). For example, type: 100.00\* **Utilization** Enter in the percent of the resource that is utilized within the given duration of the line item.

 ##### Â Note

 Your entry in the previous column determines how the value in each column populates.

 *Note:* Procore does not permit you to pro-rate costs. For example, 8 days is equal to 2 weeks, not 1.14 weeks.

 | | |
 | --- | --- |
 | **Column Name** | **Calculation** |
 | **Calculated Unit Cost** | Utilization Rate \* Unit Cost |
 | **Forecast to Complete** | Calculated Unit Cost \* Units Remaining |
 | **Planned** | Calculated Unit Cost \* Total Units *This value applies to the start and end date that you specificed.* |