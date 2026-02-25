# Sync Cost Codes from Procore to QuickBooksÂ® Online (QBO)

Source: https://v2.support.procore.com/product-manuals/qbo/tutorials/sync-cost-codes-from-procore-to-quickbooks-online-qbo

---

## Background

With the QuickBooksÂ® Online integration, cost codes are synced via the budget in Procore, not through the WBS section of the Admin tool. The integration automatically creates corresponding service items (cost codes) in QuickBooksÂ® Online when new budget line items are detected on a synced Procore project.Â  These cost codes appear in the QuickBooksÂ® Online Products and Services list as project-specific service items.

## Things to Consider

- **Required User Permissions:**

  - âAdmin' user permissions on the projectâs Admin tool and Budget tool.
- **Additional Information:**

  - Project WBS Codes (Cost Codes + Cost Type) in Procore equate to Service type Items in your QuickBooksÂ® Online Products and Services List.

    - The format of those Service Items will be **[project number in Procore]-[cost code].[cost type]**.
  - The integration will look for new WBS codes across all synced projects, and create the corresponding project specific service items in QBO every 5 mins.
  - Custom WBS segments ARE supported. If custom WBS segments are used on an integrated project, they will be built into the QuickBooksÂ® Online Service Item name in the same order that they are arranged in Procore.
  - Sub Jobs are NOT supported.
  - The Procore budget does not need to be locked for cost codes to sync to QBO.

## Prerequisites

- Cost codes need to be added to the Company level Admin tool in the QuickBooksÂ® Online ERP Integration Standard Cost Codes list.
- The project must be synced with QuickBooksÂ® Online.

## Steps

1. Navigate to the **Project level Admin** tool.
2. Under Project Settings, click **Work Breakdown Structure**.
3. Under Segments, click **Cost Code**.
4. Click **+ Cost Codes from Company**.
5. Select the cost codes you would like to add to the project, click **Add**.  
   *Note:* Make sure you are selecting cost codes from the **Quickbooks Online ERP Integration Standard Cost Codes list.**
6. Then, navigate to the **Budget** tool within your project.
7. Create your budget. There are two ways to add budget data to a Procore project:

   - You can import your project's budget data by adding your data to a Procore-built CSV template and then importing it into the Budget tool. For instructions, see [Import a Budget](/product-manuals/budget-project/tutorials/import-a-budget).
   - You can create a budget in Procore by manually adding line items to the project's Budget tool. See [Add a Budget Line Item](/product-manuals/budget-project/tutorials/add-a-budget-line-item).
8. Every 5 minutes, the integration will look for new budget codes across all synced projects and create the corresponding project specific Service items in QBO.