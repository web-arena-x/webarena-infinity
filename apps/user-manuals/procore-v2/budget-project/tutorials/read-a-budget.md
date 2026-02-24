# Read a Budget

Source: https://v2.support.procore.com/product-manuals/budget-project/tutorials/read-a-budget

---

## Background

In Procore, the project's Budget tool is setup to use the 'Procore Standard Budget' view. This is a pre-configured view that contains data columns that have been determined to be helpful to project teams that want to develop and design a budget for most construction projects. In addition to the 'Procore Standard Budget' view, companies have the ability to apply other pre-configured views to their project's budget or to design custom views to meet their specific budgeting needs. For details, see [Which budget views should I add to my projects?](/faq-which-budget-views-should-i-add-to-my-projects) and [Set Up a New Budget View](/process-guides/project-equipment-user-guide/assign-the-budget-view-to-a-procore-project).

To help you get started, this tutorial describes how to read and interpret the 'Procore Standard Budget' view. Keep in mind that your project may use a different view, so the columns described in this tutorial may be different than the ones being used in your project environment.

## Things to Consider

- **Required User Permissions:**

 - 'Read Only' level permissions and higher on the project's Budget tool. 
     AND
 - *To view the direct costs detail in a popup window*, 'Read Only' or 'Standard' level permissions with the ['View Direct Cost Details' granular permission](/product-manuals/permissions-company/tutorials/grant-granular-permissions-in-a-project-permissions-template) enabled on your permissions template.
- **Additional Information:**

 - Procore displays a line item in RED when any calculated column value is negative.

## Prerequisites

- [Set up a Budget in a New Procore Project](/product-manuals/budget-project/tutorials/set-up-a-budget-in-a-new-procore-project)

## Steps

1. Navigate to the project's **Budget** tool.
2. Click the **Budget** tab.
3. Click the **View** menu and choose *Procore Standard Budget* from the list.

   ##### Example

   **Procore Standard Budget View**

   The illustration below shows you the default layout for the 'Procore Standard Budget' view, as it looks when assigned to a project's Budget tool.

**Default Columns**

The following table details the default column and layout of the 'Procore Standard Budget' view.

| Column Name | Column Type | Column Format | Description |
| --- | --- | --- | --- |
| Description | Standard | n/a | Shows the project's budget code and budget code description. Depending on your budget code, this shows the [division](/glossary-of-terms), [cost code](/glossary-of-terms), and [cost type](/glossary-of-terms) associated with the budget line item. If sub jobs are enabled in Procore (see [Enable Sub Jobs on Projects for WBS](/process-guides/company-administration-work-breakdown-structure-guide/enable-sub-jobs-for-projects)), this column shows the name of the sub job associated with the budget line item. |
| Original Budget Amount | Standard | Currency | Shows the original budget amount for the budget line item. |
| Approved COs | Source | n/a | This visible column shows the commitment change orders in the *Approved* status by default. It also provides advanced options that permit you to include/exclude change orders in other statuses and Prime Contract. This column is also used to calculate the 'Forecast to Complete' value in the budget line item. |
| Revised Budget | Calculated | Currency | This visible column shows the total amount of any Budget Modifications + Approved COs. This column is also used to calculate the 'Forecast to Complete' value in the budget line item. |
| Pending Budget Changes | Source | Currency | This visible column shows the amounts from pending prime contract change orders in the *Pending -* statuses for the budget line item. |
| Projected Budget | Calculated | Currency | This visible column Calculates the value of the Revised Budget + Pending Budget Changes values. It also includes a subtotals and grandtotals. |
| Committed Costs 2 | Source | Currency | This visible column shows the commitment costs for subcontracts in the *Approved* and *Complete* statuses, purchase orders in the *Approved* status, and change orders in the *Approved* status. It also provides advanced options that permit you to include/exclude other status options for commitments and change orders. |
| Direct Costs | Source | Currency | This visible column shows direct costs in the *Pending*, *Revise and Resubmit*, and *Approved* status. |
| Job to Date Costs | Calculated | Currency | This visible column shows Direct Costs + Subcontractor Invoices. |
| Pending Cost Changes 1 | Source | Currency | This visible column shows subcontracts in the *Out for Signature* status, purchase order contracts in the *Processing*, *Submitted*, *Partially Received*, and *Received Status*, and change orders in the *Pending -* statuses. |
| Projected Costs 1 | Calculated | Currency | This visible column shows Committed Costs + Direct Costs + Pending Cost Changes.This column is also used to calculate the 'Forecast to Complete' value in the budget line item. |
| Forecast to Complete | Standard | Currency | This visible column is an automatic calculation of the Projected Budget - Project Costs. |
| Estimated Cost at Completion | Calculated | Currency | This visible column calculates the Projected Costs + Forecast to Complete. |
| Projected Over/Under | Calculated | Currency | This visible column calculates the Projected Budget - Estimated Cost at Completion. |
| Budget ROM | Source | Currency | Shows the budget's [Rough Order of Magnitude](/glossary-of-terms) (ROM) value. |
| Budget Changes 1 | Standard | Currency | Shows the amount of a [budget change](/glossary-of-terms) for the budget line item. |
| Revised Budget (+Changes) | Calculated | Currency | Calculates a value for the Original Budget Amount + Budget Changes. |
| Projected Cost Budget | Calculated | Currency | Calculates a value of the Original Budget Amount + Budget ROM + Budget Changes. |

1 *The Budget Changes column requires users to migrate their data to the new Budget Changes feature. See* [Migrating to Budget Changes from Budget Modifications](/product-manuals/budget-project/tutorials/migrating-to-budget-changes-from-budget-modifications)*.*

2 *This column reflects contract values from Procore's Commitments tool. However, the commitment must be set to a specific status. To learn more, see* [What are the default commitment statuses in Procore?](/faq-what-are-the-default-commitment-statuses-in-procore)