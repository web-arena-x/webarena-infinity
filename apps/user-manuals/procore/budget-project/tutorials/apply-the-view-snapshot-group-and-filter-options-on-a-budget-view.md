# Apply the View, Snapshot, Group, and Filter Options on a Budget View

Source: https://v2.support.procore.com/product-manuals/budget-project/tutorials/apply-the-view-snapshot-group-and-filter-options-on-a-budget-view

---

## Background

The budget view provides various filtering and grouping choices to help teams analyze their budget data. Users can view budget data in full-screen mode, click links to explore budget details, and take snapshots to capture budget data for a point in time.

## Things to Consider

- **Required User Permissions:**

 - 'Read Only' level permissions or higher on the project's Budget tool.
- **Additional Information:**

 - The 'Sub Job' filter is always in the Group menu, even when sub jobs are off in Procore. See [Enable Sub Jobs on Projects for WBS](/process-guides/company-administration-work-breakdown-structure-guide/enable-sub-jobs-for-projects).
 - The 'Division' option in the Group and Filter menu corresponds to 'Cost Code Tier 1' in the Work Breakdown Structure.

## Prerequisites

- [Set up a New Budget View](/process-guides/project-equipment-user-guide/assign-the-budget-view-to-a-procore-project)
- [Create a Budget Snapshot](/process-guides/budget-and-forecast-snapshots-user-guide/create-a-snapshot)
- *Optional*: [Create Budget Code Attributes for Project Work Breakdown Structure](/product-manuals/admin-project/tutorials/create-budget-code-attributes-for-project-work-breakdown-structure)
- *Optional:* [Enable Sub Jobs for WBS](/process-guides/company-administration-work-breakdown-structure-guide/enable-sub-jobs-for-projects)

## Steps

### Apply a Budget View to Your Budget

Navigate to the project's **Budget** tool. Then click the **Budget**, **Budget Details**, or **Project Snapshot Status** tab and select an option from the **View** menu. To add views to this menu, see [Assign a Budget View to a Project](/product-manuals/admin-company/tutorials/assign-a-budget-view-to-a-procore-project).

##### Â Notes

- Procore offers company accounts several standard budget views. See [What are Procore's standard budget views?](/faq-what-are-procores-standard-budget-views)
- Your company can create custom budget views or modify existing views. For details, see [Set up a New Budget View](/process-guides/project-equipment-user-guide/assign-the-budget-view-to-a-procore-project).

### View a Budget Snapshot

Navigate to the project's **Budget** tool. Then, click the **Budget** or **Forecasting** tab and select an option from the **Snapshot** menu. To add snapshots to this menu, see [Create a Budget Snapshot](/process-guides/budget-and-forecast-snapshots-user-guide/create-a-snapshot).

### Apply Group Options to Organize Your Data

Navigate to the project's **Budget** tool. Then, click the **Budget**, **Budget Details**, or **Forecasting** tab to choose the options to apply from the **Group** menu. Remove groupings by clicking the 'x' next to them. The sort order can be adjusted by dragging and dropping a group with the more menu (â¡) icon. To revert the grouping to the default budget view, click **Reset**.

Below are the options in the menu.

| **Option** | **To filter data...** | **To learn more...** |
| --- | --- | --- |
| **Sub Job** | Select one or more sub-jobs. This option is always visible in the **Group** menu, even when the sub-jobs feature is disabled. | - [Enable Sub Jobs on Project in WBS](/process-guides/company-administration-work-breakdown-structure-guide/enable-sub-jobs-for-projects) |
| **Cost Code Tier 1** *This option was previously named 'Division'. See* [Where is the 'Division' in the 'Cost Code' segment in Procore's WBS?](https://support.procore.com/faq/where-is-the-division-in-the-cost-code-segment-in-procores-wbs) | Select one or more cost code tiers. Each tier corresponds to a tiered 'Cost Code' segment in the Work Breakdown Structure. | - [Add Company Cost Codes](/process-guides/company-administration-work-breakdown-structure-guide/add-company-cost-codes) - [Where is the 'Division' in the 'Cost Code' segment in Procore's WBS?](https://support.procore.com/faq/where-is-the-division-in-the-cost-code-segment-in-procores-wbs) |
| **Cost Code Tier 2** *This option was previously named 'Cost Code' See* [What is the difference between a flat and tiered segment in Procore's WBS?](/faq-what-is-the-difference-between-a-flat-and-tiered-segment-in-procores-wbs) | Select one or more cost codes. Each code corresponds to a tiered 'Cost Code' segment in the Work Breakdown Structure. Additional levels in the 'Cost Code' segment show as *Cost Code Tier 3*, *Cost Code Tier 4*, etc | - [Add Company Cost Codes](/process-guides/company-administration-work-breakdown-structure-guide/add-company-cost-codes) - [What are Procore's default cost codes?](/faq-what-are-procores-default-cost-codes) |
| **Cost Type** | Select one or more cost types. Each choice matches a 'Cost Type' segment in the Work Breakdown Structure. | - [Add Company Cost Types](/process-guides/company-administration-work-breakdown-structure-guide/add-company-cost-types) - [What are Procore's default cost types?](/faq-what-are-procores-default-cost-types) |
| Beta **Budget Code Attributes** | Apply custom grouping options if your team created budget code attributes for the Work Breakdown Structure. | - [About Budget Code Attributes](https://support.procore.com/products/online/user-guide/project-level/budget/tutorials/about-budget-code-attributes) - [Create Budget Code Attributes for Project Work Breakdown Structure](/product-manuals/admin-project/tutorials/create-budget-code-attributes-for-project-work-breakdown-structure) |

### Add Filters to Narrow Your Data

Navigate to the project's **Budget** tool. Then, click the **Budget**, **Budget Details**, **Forecasting**, **Budget Changes**, or **Change History** tab choose the filtering options to apply from the **Filter** menu. When sub-filters exist, mark the checkboxes to apply the sub-filters you want. To clear individual filters, remove a checkmark or click **Clear Filters** to clear them all.

Below are the options in the menu.

| **Option** | **To filter data...** | **To learn more, see...** |
| --- | --- | --- |
| **Sub Job** | Select one or more sub-jobs. This option is always visible in the **Group** menu, even when the sub-jobs feature is disabled. | - [Enable Sub Jobs on Projects for WBS](/process-guides/company-administration-work-breakdown-structure-guide/enable-sub-jobs-for-projects) - [Add 'Sub Job' Segment Items to a Procore Project](/process-guides/project-administration-work-breakdown-structure-guide/add-sub-jobs-to-a-project) |
| **Cost Code Tier 1** *This option was previously named 'Division'. See Where is the 'Division' in the 'Cost Code' segment in Procore's WBS?* | Select one or more cost code tiers. Each tier corresponds to a tiered 'Cost Code' segment in the Work Breakdown Structure. | - [Add Company Cost Codes](/process-guides/company-administration-work-breakdown-structure-guide/add-company-cost-codes) - [What is the difference between a flat and tiered segment in Procore's WBS?](/faq-what-is-the-difference-between-a-flat-and-tiered-segment-in-procores-wbs) |
| **Cost Code Tier 2** *This option was previously named 'Cost Code' See What is the difference between a flat and tiered segment in Procore's WBS?* | Select one or more cost codes. Each code corresponds to a tiered 'Cost Code' segment in the Work Breakdown Structure. Additional levels in the 'Cost Code' segment show as *Cost Code Tier 3*, *Cost Code Tier 4*, etc | - [Add Company Cost Codes](/process-guides/company-administration-work-breakdown-structure-guide/add-company-cost-codes) - [What are Procore's default cost codes?](/faq-what-are-procores-default-cost-codes) |
| **Cost Type** | Select one or more cost types. Each choice matches a 'Cost Type' segment in the Work Breakdown Structure. | - [Add Company Cost Types](/process-guides/company-administration-work-breakdown-structure-guide/add-company-cost-types) - [What are Procore's default cost types?](/faq-what-are-procores-default-cost-types) |
| **Forecast Start Date** | Pick a start date from the calendar. | - [Use the Forecast to Complete Feature](/product-manuals/budget-project/tutorials/use-the-forecast-to-complete-feature) |
| **Actuals by Date** | Choose this filter to see budget items within the dates you set. Knowing the source and columns in your budget view helps you understand how the 'Actuals By Date' filter works. | - [Set up a New Budget View](/process-guides/project-equipment-user-guide/assign-the-budget-view-to-a-procore-project) - [How does the 'Actuals by Date' filter work on a budget view?](/faq-how-does-the-actual-date-filter-work-on-a-budget-view) |
| **Budget Row Type** | Choose this and check the **Budgeted** and/or **Non-Budgeted** boxes to apply this filter. | - [Add a Partial Budget Line Item](/product-manuals/budget-project/tutorials/add-a-partial-budget-line-item) |
| Beta **Budget Code Attributes** | Apply custom filtering options if your team created budget code attributes for the Work Breakdown Structure. | - [About Budget Code Attributes](https://support.procore.com/products/online/user-guide/project-level/budget/tutorials/about-budget-code-attributes) - [Create Budget Code Attributes for Project Work Breakdown Structure](/product-manuals/admin-project/tutorials/create-budget-code-attributes-for-project-work-breakdown-structure) |
| Beta **Prime Contract** | Select a prime contract if your project has multiple prime contracts. | |
| Beta **Notes** | Choose to show or hide budget items with notes | - [Set up a New Budget View](/process-guides/project-equipment-user-guide/assign-the-budget-view-to-a-procore-project) |

### Additional Options

You also have these options:

- **Full screen** Click this button to view the budget in your browser window in full screen mode.
- **Arrows** Click the arrows in the table to expand and collapse group summaries of your data.
- **Tool tips** Hover over a column's title to view details that show how the value in a column is calculated or to learn the tool source and filters for that column,.
- **Drill-downs** Click any budget value displayed in BLUE font to open a window showing detailed information about that value.