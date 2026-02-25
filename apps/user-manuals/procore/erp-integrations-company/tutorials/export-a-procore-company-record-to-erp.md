# Export a Procore Company Record to ERP

Source: https://v2.support.procore.com/product-manuals/erp-integrations-company/tutorials/export-a-procore-company-record-to-erp

---

##### ERP DOCUMENTATION

**Each Procore-built ERP integration offers its own unique feature set.** Your integration might not support the action described on this page.

To learn about your integration and its supported features, see [Which ERP integrations are supported by Procore?](/faq-which-erp-integrations-are-supported-by-procore)

## Background

Some ERP integrations allow you to export the company records in the Company Directory to your ERP system. After creating a record, you must send it to the ERP Integrations tool where it must then be accepted for export by an [accounting approver](/glossary-of-terms).

## Things to Consider

- **Required User Permissions**:

 - You need both:

    - 'Standard' or 'Admin' on the company's ERP Integrations tool.
    - The person's account must be granted the 'Can Push to Accounting' privilege in the Company Directory. See [Grant Accounting Approver Privileges](/product-manuals/erp-integrations-company/tutorials/grant-accounting-approver-privileges).

## Steps

There are three steps you need to take to export a company record to your integrated ERP system:

1. [Add a Company in the Project Directory](/process-guides/set-up-a-project-directory/create-companies) or [Add a Company in the Company Directory](/product-manuals/directory-company/tutorials/add-a-company-to-the-company-directory).
2. Send a Procore Company to the ERP Integrations tool for Accounting Acceptance *Note:* If you need to make changes to a company record before the data has been accepted by an 

   In Procore, an *Accounting Approver* is an individual with the authority to accept and reject Procore data for export to an integrated ERP system. Accounting approvers can unlink several item types, such as commitments, commitment change orders, prime contract change orders, and subcontractor invoices, that have been synced between Procore and an integrated ERP system. See [Which ERP Integrations are supported by Procore?](/faq-which-erp-integrations-are-supported-by-procore)

   Accounting Approver for export, see:

   - [Retrieve a Company from ERP Integrations Before Acceptance](/product-manuals/erp-integrations-company/tutorials/retrieve-a-company-from-erp-integrations-before-acceptance)
   - [Resend a Rejected Company to ERP Integrations for Accounting Acceptance](/product-manuals/erp-integrations-company/tutorials/resend-a-rejected-company-to-erp-integrations-for-accounting-acceptance)
3. [Accept or Reject a Company for Export to ERP](/product-manuals/erp-integrations-company/tutorials/accept-or-reject-a-company-for-export-to-erp)