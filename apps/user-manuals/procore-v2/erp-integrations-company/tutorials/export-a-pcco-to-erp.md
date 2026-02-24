# Export a PCCO to ERP

Source: https://v2.support.procore.com/product-manuals/erp-integrations-company/tutorials/export-a-pcco-to-erp

---

##### ERP DOCUMENTATION

**Each Procore-built ERP integration offers its own unique feature set.** Your integration might not support the action described on this page.

To learn about your integration and its supported features, see [Which ERP integrations are supported by Procore?](/faq-which-erp-integrations-are-supported-by-procore)

## Things to Consider

- **Required User Permissions**:

 - You need both:

    - 'Standard' or 'Admin' on the company's ERP Integrations tool.
    - The person's account must be granted the 'Can Push to Accounting' privilege in the Company Directory. See [Grant Accounting Approver Privileges](/product-manuals/erp-integrations-company/tutorials/grant-accounting-approver-privileges).
- **Prerequisites**:

 - The Prime Contracts and Change Orders tools must be enabled on the project(s) that you want to sync.
- **Requirements**:

 - There must be a Prime Contract synced between the Procore Project and your ERP system.
 - The 'Date Created' field on the PCCO is required.
 - The PCCO must be in the 'Approved' status.

## Steps

1. [Create a PCCO](/product-manuals/prime-contracts-project/tutorials/create-a-prime-contract-change-order)
2. [Send a PCCO to ERP Integrations for Accounting Acceptance](/product-manuals/erp-integrations-company/tutorials/send-a-pcco-to-erp-integrations-for-accounting-acceptance)
3. [Accept or Reject a PCCO for Export to ERP](/product-manuals/erp-integrations-company/tutorials/accept-or-reject-a-pcco-for-export-to-erp)