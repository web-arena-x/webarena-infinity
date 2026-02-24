# Update Project Cost Codes for Export to Sage IntacctÂ®

Source: https://v2.support.procore.com/product-manuals/sage-intacct/tutorials/update-project-cost-codes-for-export-to-sage-intacct

---

## Background

If your company is using the ERP Integrations tool and a user adds new project cost codes to the Sage IntacctÂ® Standard Cost Code List, those updates must be sent to the ERP Integrations tool so the changes can be reviewed by an [accounting approver](/glossary-of-terms).

##### Â Important

Before you can export data to your ERP system, you must always update the project's cost codes first.

The accounting approver then reviews the new cost codes and cost type assignments in the ERP Integrations tool and then updates the codes as described in the steps below. This approves the cost code updates in Procore and gives Procore the permission it needs to export those codes to your Sage IntacctÂ® system, so your Procore project and the Sage IntacctÂ® job are in sync.

## Things to Consider

- **Required User Permission**:

  - You need both:

    - 'Standard' or 'Admin' on the company's ERP Integrations tool.
    - The person's account must be granted the 'Can Push to Accounting' privilege in the Company Directory. See [Grant Accounting Approver Privileges](/product-manuals/erp-integrations-company/tutorials/grant-accounting-approver-privileges).
- **Prerequisites**:

  - A user must add at least one new cost code to the ERP-synced project in Procore.
- **Additional Information**:

  - If a new cost code that already has a different cost type assignment in Procore is approved/updated, both cost type assignments will be tied to the cost code.
  - Existing cost code descriptions in Sage IntacctÂ® will not be overwritten. For example, if the cost code already has a description in Sage IntacctÂ® that's different from the Standard Cost Code's description that appears in Procore, the cost code's description in Sage IntacctÂ® will stay the same.

## Steps

1. Navigate to the company's **ERP Integrations** tool.
2. Click **Jobs**.
3. Under **Filters**, click **Ready to Update**.  
   *Note*: To refresh the content in the Ready to Update page, click **Refresh Job List**.
4. Click **View Requested Updates**.
5. Review the details in the **Cost Codes for Update** window.   
      
   *Notes*: Editing is NOT permitted in this window, so the checkboxes are dimmed and unavailable.
6. When you are ready to proceed, click **Close (X**).
7. Continue with one of these steps:

   - Accept the Codes
   - Reject the Codes

### Accept the Codes

1. Review the information in the **Jobs** tab.
2. Choose **Accept**.
3. Click **Export to Sage Intacct**.  
    Procore exports the codes and assignments during the next data sync.

### Reject the Codes

1. Review the information in the **Jobs** tab.
2. Choose **Reject**.
3. Enter a brief comment to explain why the project cost codes were rejected in the **Enter a Comment (Optional)** field.
4. Click **Reject**.