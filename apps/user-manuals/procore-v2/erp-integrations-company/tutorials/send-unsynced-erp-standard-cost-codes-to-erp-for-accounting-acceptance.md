# Send Unsynced ERP Standard Cost Codes to ERP Integrations for Accounting Acceptance

Source: https://v2.support.procore.com/product-manuals/erp-integrations-company/tutorials/send-unsynced-erp-standard-cost-codes-to-erp-for-accounting-acceptance

---

##### ERP DOCUMENTATION

**Each Procore-built ERP integration offers its own unique feature set.** Your integration might not support the action described on this page.

To learn about your integration and its supported features, see [Which ERP integrations are supported by Procore?](/faq-which-erp-integrations-are-supported-by-procore)

## Background

If you've added new cost codes to the 'ERP Standard Cost Codes' list in the company's Admin tool, those codes will need to be synced with your integrated ERP system. With most ERP integrations, you must first send the new codes to the company's ERP Integrations tool where it can then be accepted for export to your ERP system by an accounting approver.

If your ERP integration supports this method of cost code syncing, it's important to send your cost code list to the ERP Integration tool for acceptance when changes are made, before sending items to ERP that reference a new or updated cost code.

If you're not sure how your ERP integration syncs cost codes, see [Which ERP integrations are supported by Procore?](/faq-which-erp-integrations-are-supported-by-procore) for more information.

## Things to Consider

- **Required User Permissions**:

 - 'Admin' user permissions on the company's Admin tool.

## Steps

1. Navigate to the company's **Admin** tool.
2. Under **Company Settings**, click **Work Breakdown Structure**.
3. Under **Segments**, click **Cost Code**.
4. Choose one of the following options:

   1. If your company only has an **ERP Standard Cost Code** list, it appears on this page. Continue with the next step.   
      OR
   2. If your company has multiple cost code lists, select the **ERP Standard Cost Code** list before continuing to the next step.
5. Click **Send to ERP**.

   ##### Â Tips

   - If the **Send to ERP** button is grayed-out and unavailable, hover your cursor over the button to view the reason the button is not available. Most commonly it's because the page needs to be refreshed.
   - If you have previously sent information from the Admin tool to the ERP Integrations tool, the button will read **Re-send to ERP**.