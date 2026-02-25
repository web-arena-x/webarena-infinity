# Link ERP Projects to Existing Procore Projects

Source: https://v2.support.procore.com/product-manuals/erp-integrations-company/tutorials/link-erp-projects-to-procore-projects

---

##### ERP DOCUMENTATION

**Each Procore-built ERP integration offers its own unique feature set.** Your integration might not support the action described on this page.

To learn about your integration and its supported features, see [Which ERP integrations are supported by Procore?](/faq-which-erp-integrations-are-supported-by-procore)

## Background

When your Procore account is integrated with an ERP system, and that integration supports projects, you should link those records for consistency, data integrity, and functional requirements of other elements of your integration.

## Things to Consider

- **Required User Permissions**:

 - 'Admin' level permissions on the company's ERP Integrations tool.
- **Prerequisites**:

 - There must be an unsynced project that has the ERP-integrated setting enabled.
 - The Project must use the ERP standard cost code list.
- **Considerations:**

 - You only need to link active ERP projects that will be managed in Procore. Inactive ERP projects should be archived in the company-level ERP Integration tool.
 - Once a project in your ERP system is linked to a project in Procore, the ERP Integration may sync other dependencies like cost codes.
 - Once a project in your ERP system is linked to a project in Procore, changes may be made automatically, depending on your ERP Integration, or may need to be done manually in both Procore and your ERP system.

## Steps

1. Navigate to the company's **ERP Integrations** tool.
2. Click the **Projects** subtab.
3. Find an ERP project you want to link and click **Link to Existing Project**.
4. Click the dropdown menu to search for eligible Procore projects. When you find a correct match, select it and click **Link**.