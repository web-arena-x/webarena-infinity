# Update Project Cost Codes for Export to ViewpointÂ® SpectrumÂ®

Source: https://v2.support.procore.com/product-manuals/viewpoint-spectrum/tutorials/update-project-cost-codes-for-export-to-viewpoint-spectrum

---

## Background

If your company has enabled the ERP Integrations tool and a user has added a new project cost codes to the Spectrum Standard Cost Code List, a user must send those updates to the ERP Integrations tool so the changes can be reviewed by an 

In Procore, an *Accounting Approver* is an individual with the authority to accept and reject Procore data for export to an integrated ERP system. Accounting approvers can unlink several item types, such as commitments, commitment change orders, prime contract change orders, and subcontractor invoices, that have been synced between Procore and an integrated ERP system. See [Which ERP Integrations are supported by Procore?](/faq-which-erp-integrations-are-supported-by-procore)

Accounting Approver.

***Important!*** Before you can export any contracts or contract change orders to Spectrum, you must always update the project's cost codes first.The accounting approver then reviews the new cost codes and category assignments in the ERP Integrations tool and then updates the codes as described in the steps below.

## Things to Consider

- **Required User Permission**:

  - You need both:

    - 'Standard' or 'Admin' on the company's ERP Integrations tool.
    - The person's account must be granted the 'Can Push to Accounting' privilege in the Company Directory. See [Grant Accounting Approver Privileges](/product-manuals/erp-integrations-company/tutorials/grant-accounting-approver-privileges).
- **Prerequisites**:

  - At least one new cost code has been added to the ERP-synced project in Procore.
- **Additional Information**:

  - If a new cost code that already has a different category assignment in Procore is approved/updated, both category assignments will be tied to the cost code.
  - Existing cost code descriptions in Spectrum will not be overwritten. For example, if the cost code already has a description in ViewpointÂ® SpectrumÂ® that's different from the Standard Cost Code's description that appears in Procore, the cost code's description in Spectrum will stay the same.

## Steps

### Review Projects

1. Navigate to the company's **ERP Integrations** tool.
2. Click the **Jobs** tab.
3. Under **Filters**, click **Ready to Update**.
4. Click **View Requested Updates**.

       

   This reveals the 'Cost Codes for Update' window.
5. Review the new cost codes. *Note*: You cannot make any changes to cost codes or category assignments in this window. These checkboxes are grayed out and unavailable.
6. Click the 'x' to exit out of the 'Cost Codes for Update' window.
7. If you are ready to accept the new cost codes, click **Update**. The system will export the new codes codes in Procore to your integrated Spectrum system during the next data sync.