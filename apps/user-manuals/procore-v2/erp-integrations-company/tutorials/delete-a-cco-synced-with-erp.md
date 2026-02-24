# Delete a CCO Synced with ERP

Source: https://v2.support.procore.com/product-manuals/erp-integrations-company/tutorials/delete-a-cco-synced-with-erp

---

##### ERP DOCUMENTATION

**Each Procore-built ERP integration offers its own unique feature set.** Your integration might not support the action described on this page.

To learn about your integration and its supported features, see [Which ERP integrations are supported by Procore?](/faq-which-erp-integrations-are-supported-by-procore)

## Background

After syncing a CCO with your ERP system, users will typically follow the change order process when a CCO needs to be modified. However, you might sometimes need to delete a synced CCO on a project. Since Procore does not allow deletion of synced commitments, you must first unlink the records in the two systems before you can delete the CCO.

## Things to Consider

- **Required User Permissions:**

 - 'Admin' level permissions on the project's Commitments tool.
- **Limitations:**

 - You cannot delete an 'Approved' change order.
 - After a synced CCO is unlinked and deleted, the data is permanently removed from the system and cannot be restored.
- **Prerequisites:**

 - Prerequisites vary depending on which ERP system your account is integrated with. For most integrations, deletion of the item in the ERP system is a prerequisite for unlinking in Procore. To learn more about your specific integration, see [Which ERP integrations are supported by Procore?](/faq-which-erp-integrations-are-supported-by-procore)
 - [Unlink CCOs Synced with ERP](/product-manuals/erp-integrations-company/tutorials/unlink-ccos-synced-with-erp) before attempting to delete.

## Steps

1. Navigate to the project's **Commitments** tool.   
   *Note*: Before proceeding, make sure the CCO is unlinked. See [Unlink CCOs Synced with ERP](/product-manuals/erp-integrations-company/tutorials/unlink-ccos-synced-with-erp).
2. Locate the synced CCO in the list.
3. Click **View** or **Edit**.
4. Update status to **Draft**.
5. Click **Save**.
6. Return to the project's **Commitments** main tool page.
7. Locate the CCO that you want to delete. Click **Delete** .