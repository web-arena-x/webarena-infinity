# Lock a Budget

Source: https://v2.support.procore.com/product-manuals/budget-project/tutorials/lock-a-budget

---

## Background

When setting up a construction project in Procore, it is important to lock the budget once the original budget is finalized. This ensures that project users are restricted from making changes to the project's original budget data and that your team has an accurate historical record of all the budget modifications and change orders that affect the budget over the course of the project.

## Things to Consider

- **Required User Permissions:**

 - 'Admin' level permissions on the project's Budget tool OR
 - 'Read Only' or 'Standard' level permissions on the project's Budget tool and the user must be granted the ['Lock Budget' granular permission](/product-manuals/permissions-company/tutorials/grant-granular-permissions-in-a-project-permissions-template) on your permissions template.
- **Additional Information:**

 - When you lock a budget:

    - The 'Original Budget' data column is no longer editable in order to preserve the Original Budget values.
    - If you are using the 'Procore Labor Productivity Cost' budget view, locking the budget also locks 'Production Quantities.' See [Set Up the Procore Labor Productivity Cost Budget View](/process-guides/resource-tracking-and-project-financials-setup-guide/preview-the-budget-view).
 - Once a budget is locked, changes can only be made via Change Orders or Budget Modifications, which will give you an accurate historical record of all changes and their impact to the project's original budget. As a result, you will have a clear understanding of how your original budget evolved into the current budget over time.
- For companies using the ERP Integrations tool: **Show/Hide**

 You must lock the budget before you can send it to the ERP Integrations tool for acceptance for export by an [accounting approver](/glossary-of-terms). After locking the budget, see: [Send a Budget to ERP Integrations for Accounting Acceptance](/product-manuals/erp-integrations-company/tutorials/send-a-budget-to-erp-integrations-for-accounting-acceptance)

## Prerequisites

- [Set up a Budget in a New Procore Project](/product-manuals/budget-project/tutorials/set-up-a-budget-in-a-new-procore-project)

## Steps

1. Navigate to the project's **Budget** tool.
2. Review the original budget to ensure that no further changes are required.
3. Click the **Lock Budget** button.

   ##### Â Note

   If you realize that you need to make a change to the budget, users with 'Admin' level permission to the Budget tool can unlock a budget.