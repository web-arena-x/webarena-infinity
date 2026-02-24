# Resend a Rejected Subcontractor Invoice to ERP Integrations for Accounting Acceptance

Source: https://v2.support.procore.com/product-manuals/erp-integrations-company/tutorials/resend-a-rejected-subcontractor-invoice-to-erp-integrations-for-accounting-acceptance

---

##### ERP DOCUMENTATION

**Each Procore-built ERP integration offers its own unique feature set.** Your integration might not support the action described on this page.

To learn about your integration and its supported features, see [Which ERP integrations are supported by Procore?](/faq-which-erp-integrations-are-supported-by-procore)

## Background

If an invoice is sent to the ERP Integrations tool for acceptance by an accounting approver, the approver has the option to 'Reject' it for export to the ERP system. When rejected, the approver will typically include a reason for the rejection to clarify the changes needed. When an item is rejected for export, Procore sends an automated email notification to the person who sent the item to the ERP Integrations tool to notify them of the rejection.

Next, the user is expected to address the reason(s) for the rejection by updating the invoice. After the invoice is corrected, follow the steps below to resend it to the ERP Integrations tool for accounting acceptance.

## Things to Consider

- **Required User Permissions**:

 - 'Admin' level permission on the Project level Commitments tool.

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

- **Additional Information**:

 - The **Re-send to ERP** button is only available when an invoice has previously been sent to the ERP Integrations tool and was rejected for export by an accounting approver.
 - Since there are several reasons why an invoice could be rejected, you may need to fix multiple issues. If you have questions, contact your company's accounting approver for more information about the rejection reason(s).
 - When you re-send an invoice to the ERP Integrations tool, your company's designated accounting approver(s) will immediately receive an email notification to alert them. It will also be included in the "ERP Integrations Daily Summary" email notification.