# Accept or Reject a Project for Export to ERP

Source: https://v2.support.procore.com/product-manuals/erp-integrations-company/tutorials/accept-or-reject-a-project-for-export-to-erp

---

##### ERP DOCUMENTATION

**Each Procore-built ERP integration offers its own unique feature set.** Your integration might not support the action described on this page.

To learn about your integration and its supported features, see [Which ERP integrations are supported by Procore?](/faq-which-erp-integrations-are-supported-by-procore)

## Background

After sending a project to your ERP Integrations tool, a designated accounting approver has the option to accept or reject it for export to your ERP system.

## Things to Consider

- **Required User Permissions**:

 - You need both:

    - 'Standard' or 'Admin' on the company's ERP Integrations tool.
    - The person's account must be granted the 'Can Push to Accounting' privilege in the Company Directory. See [Grant Accounting Approver Privileges](/product-manuals/erp-integrations-company/tutorials/grant-accounting-approver-privileges).

## Steps

### Review Projects in the 'Ready to Export' List

1. Navigate to the company's **ERP Integrations** tool. 
   *Notes*:

   - If the project does not appear in this tab, see [Why is my Procore project missing from the ERP Integrations tool?](/faq-why-is-my-procore-project-missing-from-the-erp-integrations-tool)
2. Click the **Jobs** tab.
3. Under **Filters**, click **Ready to Export**.
4. Continue with one of the following:

   - âAccept the Project
   - Reject the Project

### Accept the Project

1. Review the project information in the **Jobs** tab.   
   *Note*: To view the project information in more detail, click the hyperlink in the 'Project Name' field. You must have access permission to the project in order to use this hyperlink.
2. Click **Accept**.
3. Complete any additional entries required for your integration. If additional entries are required, fields will appear when you click **Accept.** *Note:* Examples of additional fields that might be required by some ERP integrations include:

   - ERP Integration Job ID
   - Subaccount ID
   - Template ID
   - Company Reference ID
4. Click **Export to ERP.** *Note*: If the export process is successful, the system moves the project(s) to the 'Synced Projects' list. To view this list, click **Synced** in the 'Filters' menu.
    If the export process fails, an error message will appear. The system also moves the project(s) that failed to sync to the 'Projects in Procore Failed to Sync to ERP' list. To view this list, click **Failed To Sync** in the 'Filters' menu.

### Reject the Project

1. Review the project information in the **Jobs** tab.   
   *Note*: To view the project information in more detail, click the hyperlink in the 'Project Name' field. You must have access permission to the project in order to use this hyperlink.
2. Choose **Reject**.
3. Enter a brief comment to explain why the project was rejected in the **Enter a Comment (Optional)** field.
4. Click **Reject**. 
    The system sends an automated email notification with the subject line 'ERP Project Rejection Notification' to the person who created the commitment and to any users designated as an accounting approver on the project. Procore removes the project from the 'Ready to Export' list and returns it to an editable state in the project's Admin tool, so the user can make the correction and then re-send the project to the ERP Integrations tool for acceptance by an accounting approver.