# Export a Budget to an Integrated ERP System

Source: https://v2.support.procore.com/product-manuals/budget-project/tutorials/export-a-budget-to-an-integrated-erp-system

---

# Export a Procore Budget to ERP

##### ERP DOCUMENTATION

**Each Procore-built ERP integration offers its own unique feature set.** Your integration might not support the action described on this page.

To learn about your integration and its supported features, see [Which ERP integrations are supported by Procore?](/faq-which-erp-integrations-are-supported-by-procore)

## Objective

To export a budget in Procore to your ERP system.

## Background

Using the ERP Integrations tool, you can export a budget from a Procore project to your [integrated ERP system](/glossary-of-terms).

## Things to Consider

- **Required User Permission**:

 - You need both:

    - 'Standard' or 'Admin' on the company's ERP Integrations tool.
    - The person's account must be granted the 'Can Push to Accounting' privilege in the Company Directory. See [Grant Accounting Approver Privileges](/product-manuals/erp-integrations-company/tutorials/grant-accounting-approver-privileges).
- **Prerequisites**:

 - The project where the budget is located must be synced with your ERP system.
 - Project cost codes must have a cost type assigned in the 'Admin' tool.
- **Requirements**:

 - The budget must be locked. See [Lock a Budget](/product-manuals/budget-project/tutorials/lock-a-budget).
- **Limitations**:

 - Procore's ERP integrations do NOT sync 'Unit of Measure (UOM)' and 'Unit Qty' values between systems. Currently, the Budget sync is amount-based only. This means you must manually enter the units in both Procore and in your integrated ERP system.
 - Procore's ERP integrations do NOT sync Prime Contract Change Orders to your ERP system as Budget Revisions, even though these impact the budget as such in Procore. In order to sync budget revisions to your ERP system, those revisions must be entered into Procore as budget changes or revised budget estimates.
- **Additional considerations, limitations, or requirements might apply depending on the ERP system your company is integrated with. See** [Things to Know about your ERP Integration](https://support.procore.com/products/online/user-guide/company-level/erp-integrations/things-to-know-about-your-erp-integration) **for details.**

## Steps

1. [Set up a Budget in a New Procore Project](/product-manuals/budget-project/tutorials/set-up-a-budget-in-a-new-procore-project)
2. [Lock the Budget](/product-manuals/budget-project/tutorials/lock-a-budget)
3. [Send a Budget to ERP for Accounting Acceptance](/product-manuals/erp-integrations-company/tutorials/send-a-budget-to-erp-integrations-for-accounting-acceptance)
4. [Accept or Reject a Budget for Export to ERP](/product-manuals/erp-integrations-company/tutorials/accept-or-reject-a-budget-for-export-to-erp)

## See Also

- [Things to Know about your ERP Integration](https://support.procore.com/products/online/user-guide/company-level/erp-integrations/things-to-know-about-your-erp-integration)
- [Create a Budget Line Item](/process-guides/resource-tracking-and-project-financials-setup-guide/add-a-budget-line-item)