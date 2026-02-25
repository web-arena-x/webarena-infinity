# Delete a Budget Line Item

Source: https://v2.support.procore.com/product-manuals/budget-project/tutorials/delete-a-budget-line-item

---

## Background

If your budget is unlocked or has a budget amount of $0, you can use the steps below to delete budget line items.

##### Â Important

A line item cannot be deleted when:

- The budget is locked.
- The budget line item has an 'Original Budget' amount greater than $0.
- The budget line item has a budget change.
- The 'Forecast to Complete' on the budget line item has a manual override/update.

## Things to Consider

- **Required User Permissions:**

 - 'Admin' level permissions on the project's Budget tool OR
 - 'Read Only' or 'Standard' level permissions on the Budget tool with the ['Delete Budget Line Items' granular permission](/product-manuals/permissions-company/tutorials/grant-granular-permissions-in-a-project-permissions-template) enabled on your permission template.
- **Additional Information:**

 - If a budget is locked, a budget line item cannot be deleted if it has an "Original Budget" value greater than $0, contains a budget change, or has a manual override/update of the Forecast to Complete.
 - If a line item appears in the budget with a "?", it can not be deleted. See [Add a Partial Budget Line Item](/product-manuals/budget-project/tutorials/add-a-partial-budget-line-item).
 - If a line item is deleted that is associated with a financial item, even if that financial item's source or filter is not used in your Budget view, the line item will re-appear with a "?." See [Add a Partial Budget Line Item](/product-manuals/budget-project/tutorials/add-a-partial-budget-line-item).
- **For companies using the ERP Integrations tool:**

 - Deleted budget line items are synced with the 

    In Procore, the term *integrated ERP System*, is used to refer to *Enterprise Resource Planning (ERP)* software applications that can be configured to exchange data between Procore and a supported application using the Company level ERP Integrations tool. See [Which ERP integrations are supported by Procore?](/faq-which-erp-integrations-are-supported-by-procore)

    Integrated ERP System during the export process. See [Export a Budget to an Integrated ERP System](/product-manuals/budget-project/tutorials/export-a-budget-to-an-integrated-erp-system).

## Prerequisites

- [Unlock a Budget](/product-manuals/budget-project/tutorials/unlock-a-budget)

## Steps

1. Navigate to the project's **Budget** tool.
2. Click the **Delete** icon for each line item that you want to delete.
3. Verify that the subtotal amounts were updated appropriately.