# Delete a Commitment Synced with ERP

Source: https://v2.support.procore.com/product-manuals/erp-integrations-company/tutorials/delete-a-commitment-synced-with-erp

---

##### ERP DOCUMENTATION

**Each Procore-built ERP integration offers its own unique feature set.** Your integration might not support the action described on this page.

To learn about your integration and its supported features, see [Which ERP integrations are supported by Procore?](/faq-which-erp-integrations-are-supported-by-procore)

## Background

In some cases you might need to delete a synced commitment from your project in Procore. Commitments can't be deleted while synced with ERP, so before deleting you must first unlink the commitment from your ERP system.

## Things to Consider

- **Required User Permission**:

 - 'Admin' level permissions on the project's Commitments tool.
- **Prerequisites**:

 - Unlink the commitment. See [Unlink Commitments Synced with ERP](/product-manuals/erp-integrations-company/tutorials/unlink-commitments-synced-with-erp).
 - You might need to first delete the commitment from your ERP system prior to deletion in Procore. This and other prerequisites can vary depending on the ERP system your Procore account is integrated with. See [Which ERP integrations are supported by Procore?](/faq-which-erp-integrations-are-supported-by-procore) for details.
- **Additional Information**:

 - When a synced commitment or change order is deleted from Procore, the delete action is captured in the individual item's Change History subtab.
- **Limitations**:

 - After a synced commitment is reset and deleted, the data is permanently removed from the system and cannot be restored.

## Steps

1. Complete any prerequisites required for your specific ERP integration.
2. Navigate to the project's **Commitments** tool.
3. Locate the synced commitment (i.e,. subcontract or purchase order) that you requested to delete. Then click **View** or **Edit**.
4. Update the status of the commitment to **Draft**.
5. Click **Save**.
6. Click **Delete**.