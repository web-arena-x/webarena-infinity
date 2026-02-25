# Export Subcontractor Invoices from Procore to ERP

Source: https://v2.support.procore.com/product-manuals/erp-integrations-company/tutorials/export-subcontractor-invoices-from-procore-to-erp

---

##### ERP DOCUMENTATION

**Each Procore-built ERP integration offers its own unique feature set.** Your integration might not support the action described on this page.

To learn about your integration and its supported features, see [Which ERP integrations are supported by Procore?](/faq-which-erp-integrations-are-supported-by-procore)

## Background

If you want to export your subcontractor invoices to your ERP system, you need to sync the Subcontract to your ERP system and create the Subcontract in your Procore project.

After your subcontractor invoices are reviewed by a member of your project team and placed in the 'Approved' status, an 

In Procore, an *Accounting Approver* is an individual with the authority to accept and reject Procore data for export to an integrated ERP system. Accounting approvers can unlink several item types, such as commitments, commitment change orders, prime contract change orders, and subcontractor invoices, that have been synced between Procore and an integrated ERP system. See [Which ERP Integrations are supported by Procore?](/faq-which-erp-integrations-are-supported-by-procore)

Accounting Approver can export them to your ERP system, if that function is supported by your ERP integration.

## Things to Consider

- **Required User Permissions**:

 - You need both:

    - 'Standard' or 'Admin' on the company's ERP Integrations tool.
    - The person's account must be granted the 'Can Push to Accounting' privilege in the Company Directory. See [Grant Accounting Approver Privileges](/product-manuals/erp-integrations-company/tutorials/grant-accounting-approver-privileges).

## Steps

1. [Send Subcontractor Invoices to ERP Integrations for Accounting Acceptance](/product-manuals/erp-integrations-company/tutorials/send-subcontractor-invoices-to-erp-integrations-for-accounting-acceptance)
2. [Accept or Reject a Subcontractor Invoice for Export to ERP](/product-manuals/erp-integrations-company/tutorials/accept-or-reject-subcontractor-invoices-for-export-to-erp)