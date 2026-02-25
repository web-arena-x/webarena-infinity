# Update Project Cost Codes for Export to Sage 100 ContractorÂ®

Source: https://v2.support.procore.com/product-manuals/sage-100/tutorials/update-project-cost-codes-for-export-to-sage-100

---

## Background

If your company has enabled the ERP Integrations tool and a user has added a new project cost codes to the Sage 100 ContractorÂ® Standard Cost Code List (see [Add ERP Standard Cost Codes to a Project](/product-manuals/erp-integrations-company/tutorials/add-erp-standard-cost-codes-to-a-project)), a user must send those updates to the ERP Integrations tool so the changes can be reviewed by an [accounting approver](/glossary-of-terms).

***Important!*** Before you can export any contracts or contract change orders to your ERP system, you must always update the project's cost codes first.The accounting approver then reviews the new cost codes and cost type assignments in the ERP Integrations tool and then updates the codes as described in the Steps below. This approves the cost code updates in Procore and gives Procore the permission it needs to export those codes to your Sage 100 ContractorÂ® system, so your Procore project and the Sage 100 ContractorÂ® job are in sync.

## Things to Consider

- **Required User Permission**:

  - You need both:

    - 'Standard' or 'Admin' on the company's ERP Integrations tool.
    - The person's account must be granted the 'Can Push to Accounting' privilege in the Company Directory. See [Grant Accounting Approver Privileges](/product-manuals/erp-integrations-company/tutorials/grant-accounting-approver-privileges).
- **Prerequisites**:

  - A user must add at least one new cost code to the ERP-synced project in Procore. See [Add ERP Standard Cost Codes to a Project](/product-manuals/erp-integrations-company/tutorials/add-erp-standard-cost-codes-to-a-project).
- **Additional Information**:

  - If a new cost code that already has a different cost type assignment in Procore is approved/updated, both cost type assignments will be tied to the cost code.
  - Existing cost code descriptions in Sage 100 ContractorÂ® will not be overwritten. For example, if the cost code already has a description in Sage 100 ContractorÂ® that's different from the Standard Cost Code's description that appears in Procore, the cost code's description in Sage 100 ContractorÂ® will stay the same.

## Steps

1. Navigate to the Company level **ERP Integrations** tool.  
   This reveals the ERP Integration page.
2. Click the **Jobs** tab.
3. Under **Filters**, click **Ready to Update**.  
   This reveals a list of all the Procore projects that can be exported to Sage 100 ContractorÂ®.
4. Click **View Requested Updates**.   
   This reveals the 'Cost Codes for Update' window.
5. Review the new cost codes.   
   *Note*: You cannot make any changes to cost codes or cost type assignments in this window. These checkboxes are grayed out and unavailable.
6. Click the close (x) to exit out of the 'Cost Codes for Update' window.
7. If you are ready to accept the new cost codes, click **Update**.   
   The system will export the new codes codes in Procore to your integrated Sage 100 ContractorÂ® system during the next data sync. See [How often can I sync data between Sage 100 Contractor and Procore?](/faq-how-often-can-i-sync-data-between-sage-100-contractor-and-procore)