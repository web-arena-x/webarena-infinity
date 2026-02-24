# Retrieve a Budget from ERP Before Acceptance

Source: https://v2.support.procore.com/product-manuals/erp-integrations-company/tutorials/retrieve-a-budget-from-erp-integrations-before-acceptance

---

##### ERP DOCUMENTATION

**Each Procore-built ERP integration offers its own unique feature set.** Your integration might not support the action described on this page.

To learn about your integration and its supported features, see [Which ERP integrations are supported by Procore?](/faq-which-erp-integrations-are-supported-by-procore)

## Background

After a budget is sent to the ERP Integrations tool for acceptance by an accounting approver, the system locks the budget. You will only be able to to modify it in Procore, after:

- The budget was accepted for export to the integrated ERP system by your company's designated accounting approver, and has been synced with the integrated ERP system. 
   OR
- The budget was rejected by the accounting approver.

However, if you recently sent a budget to the ERP Integrations tool and realize you need to quickly correct some data, you can use the steps below to retrieve the budget from the ERP Integrations tool. You can only perform these retrieval steps if the accounting approver has not yet approved the budget for export.

## Things to Consider

- **Required User Permission**:

 - 'Admin' permission on the project's Budget tool. 
     OR
 - 'Read Only' or 'Standard' permission on the project's Budget tool with the ['Send and Retrieve Budgets from ERP' granular permission](/product-manuals/permissions-company/tutorials/grant-granular-permissions-in-a-project-permissions-template) enabled on your permission template.
- **Additional Information**:

 - You can only retrieve a budget that was sent to the company's ERP Integrations tool if it has not yet been accepted or rejected by an accounting approver.
 - If you successfully retrieve a budget from the ERP Integrations tool, you will be able to unlock the budget, make edits, and resubmit the budget.

## Steps

1. Navigate to the project's **Budgets** tool.
2. Click **Retrieve from ERP**.
3. Click **Unlock Budget.** *Note:* You cannot unlock a budget if there is a budget modification. See [Create a Budget Modification](/product-manuals/budget-project/tutorials/create-a-budget-modification).