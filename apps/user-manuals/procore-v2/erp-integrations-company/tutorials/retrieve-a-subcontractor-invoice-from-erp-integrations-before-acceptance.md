# Retrieve a Subcontractor Invoice from ERP Integrations Before Acceptance

Source: https://v2.support.procore.com/product-manuals/erp-integrations-company/tutorials/retrieve-a-subcontractor-invoice-from-erp-integrations-before-acceptance

---

##### ERP DOCUMENTATION

**Each Procore-built ERP integration offers its own unique feature set.** Your integration might not support the action described on this page.

To learn about your integration and its supported features, see [Which ERP integrations are supported by Procore?](/faq-which-erp-integrations-are-supported-by-procore)

## Background

After an invoice is sent to the ERP Integrations tool for acceptance by an accounting approver, the system locks the invoice and you are NOT permitted to modify it in Procore, until it is either accepted and exported to the integrated ERP system by your company's designated accounting approver, or rejected by the accounting approver.

However, if you recently sent an invoice to the ERP Integrations tool and realize you need to quickly correct some information, you can use the steps below to retrieve the invoice from the ERP Integrations tool.

## Things to Consider

- **Required User Permission**:

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

- **Prerequisites**:

 - You can only perform these retrieval steps if the accounting approver has not yet accepted or rejected the invoice for export to the ERP system.