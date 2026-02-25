# Export a Commitment Change Order (CCO) to ERP

Source: https://v2.support.procore.com/product-manuals/erp-integrations-company/tutorials/export-a-cco-to-erp

---

##### ERP DOCUMENTATION

**Each Procore-built ERP integration offers its own unique feature set.** Your integration might not support the action described on this page.

To learn about your integration and its supported features, see [Which ERP integrations are supported by Procore?](/faq-which-erp-integrations-are-supported-by-procore)

## Background

If you want to export CCOs to your ERP system, first you need to succesfully sync the Commitment. You'll then need to create the CCO in your Procore project.

After your CCOs are reviewed by a member of your project team and placed in the 'Approved' status, an 

In Procore, an *Accounting Approver* is an individual with the authority to accept and reject Procore data for export to an integrated ERP system. Accounting approvers can unlink several item types, such as commitments, commitment change orders, prime contract change orders, and subcontractor invoices, that have been synced between Procore and an integrated ERP system. See [Which ERP Integrations are supported by Procore?](/faq-which-erp-integrations-are-supported-by-procore)

Accounting Approver can export them to your ERP system, if that function is supported by your ERP integration.

## Things to Consider

- **Required User Permissions**:

 - You need both:

    - 'Standard' or 'Admin' on the company's ERP Integrations tool.
    - The person's account must be granted the 'Can Push to Accounting' privilege in the Company Directory. See [Grant Accounting Approver Privileges](/product-manuals/erp-integrations-company/tutorials/grant-accounting-approver-privileges).

## Steps

1. [Send a CCO to an Accounting Approver for Export to ERP](/product-manuals/erp-integrations-company/tutorials/send-a-cco-to-erp-integrations-for-accounting-acceptance)
2. [Accept or Reject a CCO for Export to ERP](/product-manuals/erp-integrations-company/tutorials/accept-or-reject-a-cco-for-export-to-erp)