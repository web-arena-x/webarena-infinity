# Unlink CCOs Synced with ERP

Source: https://v2.support.procore.com/product-manuals/erp-integrations-company/tutorials/unlink-ccos-synced-with-erp

---

##### ERP DOCUMENTATION

**Each Procore-built ERP integration offers its own unique feature set.** Your integration might not support the action described on this page.

To learn about your integration and its supported features, see [Which ERP integrations are supported by Procore?](/faq-which-erp-integrations-are-supported-by-procore)

## Background

When a CCO in Procore is synced with your ERP system, a link is created between the records in each system. Sometimes, you might need to edit or delete a CCO that has already been synced. To be able to modify or delete a synced CCO, you must first unlink it.

## Things to Consider

- **Required User Permissions**:

 - You need the following:

    - 'Admin' on the project's Commitments tool.
    - 'Standard' or 'Admin' on the ERP Integrations tool.
    - The person's account must be granted the 'Can Push to Accounting' privilege in the Company Directory. To request to enable this privilege, submit a request to your Procore point of contact. This must be enabled for you by Procore.

## Steps

1. Navigate to the company's **ERP Integrations** tool.
2. Click **Commitment Change Orders**.
3. Locate the desired CCO under **Change Orders - Successfully Synced with ERP.**
4. Click **Unlink**.

   - If the unlink action is successful, the 'Successful Unlinked' message appears in GREEN.
   - If the unlink action is not successful, the "The CCO is still in ERP. Please delete it before retrying" message appears in RED.