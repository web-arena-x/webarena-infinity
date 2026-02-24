# Edit Budget Code Descriptions on a Project

Source: https://v2.support.procore.com/product-manuals/admin-project/tutorials/edit-budget-code-descriptions-on-a-project

---

## Background

If your team has created budget codes on a project and you want to edit their descriptions, you can use the steps below to make the desired changes. This action changes the Budget Code description displayed in the Budget and [schedule of values (SOV)](/glossary-of-terms) line items.

## Things to Consider

- **Required User Permissions:**

 - 'Admin' level permissions on the Project level Admin tool.   
     OR
 - 'Read Only' or 'Standard' level permissions on the Project level Admin tool with the ['Manage WBS Codes' granular permission](/product-manuals/permissions-company/tutorials/grant-granular-permissions-in-a-project-permissions-template) enabled on your permission template.
- **For ERP Integrated accounts:**

 - Most ERP integrations do not have a field that directly corresponds to Budget Codes or their related descriptions in Procore, and so there will be no impact to data within your ERP system unless an exception is outlined below:\* NetSuiteÂ®**.** When creating a new budget code description and syncing that data to NetSuiteÂ® for the first time, the description WILL export. However, edits made to budget code descriptions in Procore will NOT export to NetSuiteÂ®.

## Steps

### Edit a Budget Code Description in the Admin Tool

1. Navigate to the project's **Admin** tool.
2. Click the **Work Breakdown Structure** link.
3. Click the **Budget Code Usage** tab.
4. Locate the budget code that you want to modify.

   ##### Â Note

   - To search for a specific budget code, type in the desired code in the **Search** box.

- Click the **Description** field and edit the description.   
     
 *Note:* Leaving the Description field blank will return the Budget Code to the default concatenated description.

### Edit a Budget Code Description in the Budget

1. Navigate to the project's **Budget** tool.
2. Locate the Budget line item containing the Budget Code you want to modify.
3. Scroll the budget to the right and click the pencil icon.
4. Click **Custom** under the 'Budget Code Description' section.
5. Enter a custom budget code description.
6. Click **Save**. 
   *Note:* The new description will also be updated in the Admin tool.
7. *Optional:* Click **Default** to return the budget code to the concatenated description.