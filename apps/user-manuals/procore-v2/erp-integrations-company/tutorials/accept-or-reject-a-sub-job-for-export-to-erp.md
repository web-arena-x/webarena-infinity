# Accept or Reject a Sub Job for Export to ERP

Source: https://v2.support.procore.com/product-manuals/erp-integrations-company/tutorials/accept-or-reject-a-sub-job-for-export-to-erp

---

##### ERP DOCUMENTATION

**Each Procore-built ERP integration offers its own unique feature set.** Your integration might not support the action described on this page.

To learn about your integration and its supported features, see [Which ERP integrations are supported by Procore?](/faq-which-erp-integrations-are-supported-by-procore)

## Background

After a user sends a sub job to the ERP Integrations tool for accounting acceptance, an accounting approver has the option to accept or reject it for export to the ERP system.

## Things to Consider

- **Required User Permissions**:

 - You need both:

    - 'Standard' or 'Admin' on the company's ERP Integrations tool.
    - The person's account must be granted the 'Can Push to Accounting' privilege in the Company Directory. See [Grant Accounting Approver Privileges](/product-manuals/erp-integrations-company/tutorials/grant-accounting-approver-privileges).

*Note*: Users who are granted only 'Standard' level permission to the ERP Integrations tool can view information, but do not have sufficient permission to accept/reject Sub Jobs for export.

## Steps

- Review a Sub Job

 - Accept a Sub Job
 - Reject a Sub Job

### Review a Sub Job

1. Navigate to the company's **ERP Integrations** tool.
2. Click the **Sub Jobs** tab.
3. Under **Filters**, click **Ready to Export**.
4. Continue with one of the following:

   - Accept a Sub Job
   - Reject a Sub Job

### Accept a Sub Job

1. Under **Sub Jobs Only in ERP**, locate the Sub Job that you want to accept.
2. Choose **Accept**.   
      
   *Note:* If this button is NOT visible, you have NOT been granted the 'Can Push to Accounting' privilege in the Company Directory. Your company's 

   A *Procore Administrator* is a user who has 'Admin' level permissions on all of the Company level Tools in Procore. Granting a user âAdminâ level permissions in the Company level Directory tool automatically assigns that user âAdminâ permissions on all Company level tools. Also called a *Company Administrator*.

   ProcoreÂ Administrator must submit a request to your Procore point of contact to enable it.
3. In the text box that appears, verify that the pre-filled **ERP Job ID** number is correct.
4. Click **Export to [ERP System]**.   
    This exports the Sub Job to your ERP system. The process typically takes a few minutes, then a 'Successfully Exported' message will appear in GREEN.   
   *Notes*:

   - If for any reason a Sub Job (or another item) fails to export to your ERP system, you can view the failed item(s) by clicking the **Failed to Export** link in the **Views** menu in the right pane.
   - When a Sub Job fails to sync, follow the steps in Reject a Sub Job. Next, [Edit Sub Jobs on a Project](/process-guides/project-administration-work-breakdown-structure-guide/edit-sub-jobs-on-a-project) as needed and then resend the Sub Job to ERP for acceptance.
5. (Optional) To verify that the sync was successful, log into your ERP system and verify that your data appears as expected.

### Reject a Sub Job

1. Under **Sub Jobs Only in ERP**, locate the Sub Job that you want to reject.
2. Choose **Reject**. 
   *Note:* If this button is NOT visible, you have NOT been granted the 'Can Push to Accounting' privilege in the Company Directory. Your company's 

   A *Procore Administrator* is a user who has 'Admin' level permissions on all of the Company level Tools in Procore. Granting a user âAdminâ level permissions in the Company level Directory tool automatically assigns that user âAdminâ permissions on all Company level tools. Also called a *Company Administrator*.

   ProcoreÂ Administrator must submit a request to your Procore point of contact to enable it.
3. Enter a short explanation about the reason(s) for the rejection.
4. Click **Reject**. 
      
      
    The following events occur:

   - The system removes the Sub Job from the ERP Integrations tool so you can update it in the Project level Admin tool.
   - The system sends an automated email notification to the user who created the Sub Job to alert the user of the 'Reject' response.