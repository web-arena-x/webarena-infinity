# Send Subcontractor Invoices to ERP Integrations for Accounting Acceptance

Source: https://v2.support.procore.com/product-manuals/erp-integrations-company/tutorials/send-subcontractor-invoices-to-erp-integrations-for-accounting-acceptance

---

##### ERP DOCUMENTATION

**Each Procore-built ERP integration offers its own unique feature set.** Your integration might not support the action described on this page.

To learn about your integration and its supported features, see [Which ERP integrations are supported by Procore?](/faq-which-erp-integrations-are-supported-by-procore)

## Background

To sync invoices in a Procore project with your ERP system, they must be sent to the ERP Integrations tool in Procore for acceptance by an accounting approver. After acceptance, the system will export the invoice data to your integrated ERP system. After invoices are sent to the ERP Integrations tool, users will NOT be able to edit the invoice in the Commitments tool (with the exception of the invoice's attachments).

## Things to Consider

- **Required User Permissions**:

 - 'Admin' permission on the project's Commitments tool.

    ##### Â Notes

    - Access permissions to the Invoicing & Progress Billings tools are governed by the permissions set on the Commitments and/or Client Contracts, Funding, or Prime Contracts tool. Procore tool names vary, depending on the point-of-view dictionary configured in Procore. See [What tool names and terms are different in Procore for general contractors, owners, and specialty contractors?](/faq-what-tool-names-and-terms-are-different-in-procore-for-general-contractors-owners-and-specialty-contractors)
    - > If you are a collaborator (for example, an 
      >
      > An *Invoice Contact* is a person who ensures that an invoice is submitted to an upstream contractor for payment. In Procore, an invoice contact is always an employee of the designated 'Contract Company' on a purchase order or subcontract. The contract company is the party responsible for performing work and/or supplying materials for a project. For customers in the United States using Procore's Progress Billings tool, this term is synonymous with progress billing contact.
      >
      > Invoice Contact employed by a company performing work on a project managed in Procore, your ability to perform invoice-related tasks is determined by the Procore company account holder. Settings that the account holder may choose to provide to you include:

      - A Procore User account.
      - Access permissions to the project's Commitments and/or Client Contracts, Funding, or Prime Contracts tool.
      - Membership on the 'Private' list of a specific contract or funding
      - Designated as an 'Invoice Contact' on the contract or funding.

- **Requirements**:

 - The invoice must be in the *Approved, Approved as Noted,* or *Pending Owner Approval* status.