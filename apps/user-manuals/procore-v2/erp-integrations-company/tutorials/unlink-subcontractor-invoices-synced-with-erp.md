# Unlink Subcontractor Invoices Synced with ERP

Source: https://v2.support.procore.com/product-manuals/erp-integrations-company/tutorials/unlink-subcontractor-invoices-synced-with-erp

---

##### ERP DOCUMENTATION

**Each Procore-built ERP integration offers its own unique feature set.** Your integration might not support the action described on this page.

To learn about your integration and its supported features, see [Which ERP integrations are supported by Procore?](/faq-which-erp-integrations-are-supported-by-procore)

## Background

When an invoice in Procore is synced with your ERP system, a link is created between the records in each system. Sometimes, you might need to edit or delete an invoice that has already been synced. To be able to modify or delete a synced invoice, you must first unlink it.

## Things to Consider

- **Required User Permissions**:

 - You must have all of the following:

    - 'Admin' on the project's Commitments tool.
    - 'Standard' or 'Admin' on the ERP Integrations tool.
    - The person's account must be granted the 'Can Push to Accounting' privilege in the Company Directory. To request to enable this privilege, submit a request to your Procore point of contact . This must be enabled for you by Procore.
- **Prerequisites**:

 - You will likely need to delete the invoice in your ERP system before unlinking in Procore, but this is not necessary for all ERP integrations.

## Steps

1. Complete any prerequisites required for your specific ERP integration.
2. Navigate to the company's **ERP Integrations** tool.
3. Click **Subcontractor Invoices**.
4. Mark the checkbox next to the desired subcontractor invoice under **Subcontractor Invoices - Synced with ERP**.
5. Click **Unlink**.

   - If the unlink action is successful, the 'Successfully Unlinked' message appears in GREEN.
   - If the unlink action is not successful, the "The requisition is still in your ERP system. Please delete it before retrying." message appears in RED.