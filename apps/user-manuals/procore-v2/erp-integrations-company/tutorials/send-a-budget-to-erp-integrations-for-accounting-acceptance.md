# Send a Budget to ERP Integrations for Accounting Acceptance

Source: https://v2.support.procore.com/product-manuals/erp-integrations-company/tutorials/send-a-budget-to-erp-integrations-for-accounting-acceptance

---

##### ERP DOCUMENTATION

**Each Procore-built ERP integration offers its own unique feature set.** Your integration might not support the action described on this page.

To learn about your integration and its supported features, see [Which ERP integrations are supported by Procore?](/faq-which-erp-integrations-are-supported-by-procore)

## Background

When you create or update a project's budget in Procore, you will want to send the new and updated data in Procore's Budget tool to your company's ERP Integrations tool. After the data is successfully sent to the ERP Integrations tool, it can then be accepted or rejected for export to your ERP by your company's accounting approver.

## Things to Consider

- **Required User Permission**:

 - 'Admin' permission on the project's Budget tool. 
    OR
 - 'Standard' permission on the project's Budget tool with the ['Send and Retrieve Budgets from ERP' granular permission](/product-manuals/permissions-company/tutorials/grant-granular-permissions-in-a-project-permissions-template) enabled on your permission template.
- **Additional Information:**

 - The budget must be locked before the export. See [Lock a Budget](/product-manuals/budget-project/tutorials/lock-a-budget).
 - You will not be permitted to unlock the Procore project's Budget tool, unless the following is true:

    - The exported entries have been manually posted to your your ERP system system using the Job Cost function. 
      OR
    - The budget is rejected by the accounting approver
 - If you sent the budget by mistake or need to make a change, you can [Retrieve a Budget Sent to ERP Integrations Before Acceptance](/product-manuals/erp-integrations-company/tutorials/retrieve-a-budget-from-erp-integrations-before-acceptance).

## Steps

1. Navigate to the project's **Budget** tool.   
   This reveals the Budget page.
2. In the 'Budget' page, review the budget's line items.
3. When you are ready to send your budget to the ERP Integrations tool for acceptance by an accounting approver, click **Send to ERP** (or, if you've previously sent the budget, click **Re-send to ERP**).
4. If you are updating a Procore budget that has been synced with your ERP, see [Create a Budget Line Item](/product-manuals/budget-project/tutorials/add-a-budget-line-item) and [Create a Budget Change](/product-manuals/budget-project/tutorials/create-budget-changes).

The system sends the original budget and budget modifications to the ERP Integrations tool where it can be accepted or rejected for export to your ERP by an accounting approver.