# About the Budget Detail Tab

Source: https://v2.support.procore.com/product-manuals/budget-project/tutorials/about-the-budget-detail-tab

---

## Background

All Procore company accounts include the 'Procore Standard Budget' view, which is the default view that is available for use with the project's Budget tool. This view can be applied to both the Budget tab and Budget Detail tab. This tutorial details the data columns that are available when the 'Procore Standard Budget' view is applied to the Budget Detail tab.

With the Budget Detail tab, you can also:

- **Apply Budget Views with the View Menu.** Similar to the tool's existing 'Budget' tab, you can apply your company's budget views to the Budget Details tab's data using the Views drop-down menu.
- **Apply Options Using the Add Group and Add Filter Menus.** You can also apply your desired grouping options using the options in the new 'Add Group' and 'Add Filters' drop-down menus. To learn more about your options, see [Apply Group Options to Organize Your Data](/process-guides/project-equipment-user-guide/apply-the-budget-view-to-your-budget) and [Add Filters to Narrow Your Data](/process-guides/project-equipment-user-guide/apply-the-budget-view-to-your-budget).
- **Export your Budget Detail tab to the CSV or PDF**. As with other Project Financials tools, you can export your budget detail to a flat file in the Comma Separated Values (CSV) format. When exporting the Budget Detail tab, any group and filter options applied to the table at the time are included in the Portable Document Format (PDF).

##### Example

**How the Procore Standard Budget View appears in the 'Budget Detail' tab**

The illustration below shows you the default layout for the 'Procore Standard Budget' view, as it looks when assigned to your project and applied to the 'Budget Detail' tab in the project's Budget tool.

**Default Columns**

The following table details the default column and layout of the 'Procore Standard Budget' view when it is assigned to the project and then applied to the 'Budget Detail' tab in the project's Budget tool. Note that when applied to the 'Budget Detail' tab, only Standard and Source columns from your view are available with the exception Invoicing sources. 'Calculated' columns are not supported.

| Column Name | Column Type | Column Format | Description |
| --- | --- | --- | --- |
| Budget Code | Standard | n/a | Shows the project's budget code and budget code description. Depending on your budget code, this shows the [division](/glossary-of-terms), [cost code](/glossary-of-terms), and [cost type](/glossary-of-terms) associated with the budget line item. If sub jobs are enabled in Procore (see [Enable Sub Jobs on Projects for WBS](/process-guides/company-administration-work-breakdown-structure-guide/enable-sub-jobs-for-projects)), this column shows the name of the sub job associated with the budget line item. |
| Vendor | Standard | n/a | Shows the name of the vendor associated with the budget line item. |
| Item | Standard | n/a | Shows any Procore items associated with the budget line item, such as change event. |
| Detail Type | Standard | n/a | Shows the type of detail such as the original budget, budget changes, forecast to complete, prime contract change orders, commitments, commitment change orders, change events, and direct cost details. |
| Approved COs | Source | n/a | This visible column shows the commitment change orders in the *Approved* status by default. It also provides advanced options that permit you to include/exclude change orders in other statuses and Prime Contract. This column is also used to calculate the 'Forecast to Complete' value in the budget line item. |
| Budget Changes | Standard | Currency | Shows the amount of a [budget change](/glossary-of-terms) for the budget line item. |
| Committed Costs | Source | Currency | This visible column shows the commitment costs for subcontracts in the *Approved* and *Complete* statuses, purchase orders in the *Approved* status, and change orders in the *Approved* status. It also provides advanced options that permit you to include/exclude other status options for commitments and change orders. |
| Direct Costs | Source | Currency | This visible column shows direct costs in the *Pending*, *Revise and Resubmit*, and *Approved* status. |
| Forecast to Complete | Standard | Currency | This visible column is an automatic calculation of the Projected Budget - Project Costs. |
| Original Budget Amount | Standard | Currency | Shows the original budget amount for the budget line item. |
| Pending Budget Changes | Source | Currency | This visible column shows the all budget changes in the *Pending -* statuses for the budget line item. |
| Pending Cost Changes | Source | Currency | This visible column shows subcontracts in the *Out for Signature* status, purchase order contracts in the *Processing*, *Submitted*, *Partially Received*, and *Received Status*, and change orders in the *Pending -* statuses. |