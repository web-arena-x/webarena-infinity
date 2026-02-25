# Update Project Cost Codes for Export to Sage 300 CREÂ®

Source: https://v2.support.procore.com/product-manuals/sage-300-cre/tutorials/update-project-cost-codes-for-export-to-sage-300-cre

---

## Background

If your company is using the ERP Integrations tool and a user adds new project cost codes to the Sage 300 CREÂ® Standard Cost Code List, those updates must be sent to the ERP Integrations tool so the changes can be reviewed by an 

In Procore, an *Accounting Approver* is an individual with the authority to accept and reject Procore data for export to an integrated ERP system. Accounting approvers can unlink several item types, such as commitments, commitment change orders, prime contract change orders, and subcontractor invoices, that have been synced between Procore and an integrated ERP system. See [Which ERP Integrations are supported by Procore?](/faq-which-erp-integrations-are-supported-by-procore)

Accounting Approver.

##### Â Important

Before you can export data to your ERP system, you must always update the project's cost codes first. The accounting approver then reviews the new cost codes and cost type assignments in the ERP Integrations tool and then updates the codes as described in the Steps below. This approves the cost code updates in Procore and gives Procore the permission it needs to export those codes to your Sage 300 CREÂ® system, so your Procore project and the Sage 300 CREÂ® job are in sync.

## Things to Consider

- **Required User Permission**:

  - You need both:

    - 'Standard' or 'Admin' on the company's ERP Integrations tool.
    - The person's account must be granted the 'Can Push to Accounting' privilege in the Company Directory. See [Grant Accounting Approver Privileges](/product-manuals/erp-integrations-company/tutorials/grant-accounting-approver-privileges).
- **Prerequisites**:

  - A user must add at least one new cost code to the ERP-synced project in Procore. See [Add ERP Standard Cost Codes to a Project](/product-manuals/erp-integrations-company/tutorials/add-erp-standard-cost-codes-to-a-project).
- **Additional Information**:

  - If a new cost code that already has a different cost type assignment in Procore is approved/updated, both cost type assignments will be tied to the cost code.
  - Existing cost code descriptions in Sage 300 CREÂ® will not be overwritten. For example, if the cost code already has a description in Sage 300 CREÂ® that's different from the Standard Cost Code's description that appears in Procore, the cost code's description in Sage 300 CREÂ® will stay the same.

## Steps

1. Navigate to the company's **ERP Integrations** tool.
2. Click **Jobs**.
3. Under **Filters**, click **Ready to Update**.  
   *Note*: To refresh the content in the Ready to Update page, click **Refresh Job List**.
4. Click **View Requested Updates**.
5. Review the details in the **Cost Codes for Update** window.   
      
   *Note*: Editing is NOT permitted in this window, so the checkboxes are dimmed and unavailable.
6. When you are ready to proceed, click **Close (X**).
7. Continue with one of these steps:

   - Accept the Codes
   - Reject the Codes

### Accept the Codes

1. Review the information in the **Jobs** tab.
2. Choose **Accept**.
3. Click **Export to Sage 300**.  
    Procore exports the codes and assignments during the next data sync. For more information, see [How often can I sync data between Sage 300 CREÂ® and Procore?](/faq-how-often-can-i-sync-data-between-sage-300-cre-and-procore)

### Reject the Codes

1. Review the information in the **Jobs** tab.
2. Choose **Reject**.
3. Enter a brief comment to explain why the project cost codes were rejected in the **Enter a Comment (Optional)** field.
4. Click **Reject**.