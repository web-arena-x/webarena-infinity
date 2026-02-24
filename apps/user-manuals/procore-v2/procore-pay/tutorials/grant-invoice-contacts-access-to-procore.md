# Grant Invoice Contacts Access to Procore

Source: https://v2.support.procore.com/product-manuals/procore-pay/tutorials/grant-invoice-contacts-access-to-procore

---

An *Invoice Contact* is a person who ensures that an invoice is submitted to an upstream contractor for payment. In Procore, an invoice contact is always an employee of the designated 'Contract Company' on a purchase order or subcontract. The contract company is the party responsible for performing work and/or supplying materials for a project. For customers in the United States using Procore's Progress Billings tool, this term is synonymous with progress billing contact.

### Steps

To add an invoice contact, an authorized user for the company managing the [commitment](/glossary-of-terms) in the Procore project must:

1. **Add the subcontracting company to the Company Directory**. The subcontracting company corresponds to the 'Contract Company' on a commitment. See [Add a Company to the Company Directory](/product-manuals/directory-company/tutorials/add-a-company-to-the-company-directory). The user who will be the invoice contact must be added to the company. See [Add Users to the Company](/product-manuals/directory-company/tutorials/add-a-company-to-the-company-directory).

   ##### Â NotesÂ

   - *Optional.* You can select one (1) user to be the default invoice contact in a company record. See [Add a Company to the Company Directory](/product-manuals/directory-company/tutorials/add-a-company-to-the-company-directory).

- **Grant the invoice contact's user account 'Read Only' level permissions on the Project level Commitments tool**. Procore recommends managing invoice contact permissions with a project permissions template. See [Edit a Project Permissions Template](/product-manuals/permissions-company/tutorials/edit-a-project-permissions-template).
- **Add the 'Contract Company' and 'Invoice Contact' to the commitment**. See [Add Invoice Contacts to a Purchase Order or Subcontract](/process-guides/payor-setup-guide/add-invoice-contacts).
- ***Optional.*** **Configure optional email notifications for the invoice contact:**

  - To send an email notification when an invoice's status is changed to 'Approved', see [Configure Settings: Invoicing](/product-manuals/invoicing-project/tutorials/configure-settings-invoicing).