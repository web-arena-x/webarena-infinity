# Copy Company Cost Codes to a Project

Source: https://v2.support.procore.com/product-manuals/admin-project/tutorials/copy-company-cost-codes-to-a-project

---

## Background

A *Cost Code* identifies a specific type of work on a project to track its associated expenses, such as labor, materials, and equipment.

## Things to Consider

- **Required User Permissions:**

 - You need one of the following:

    - 'Admin' level permission on the Project level Admin tool.
    - 'Read Only' or 'Standard' level permissions on the project level Admin tool with the ['Manage WBS Codes' granular permission](/product-manuals/permissions-company/tutorials/grant-granular-permissions-in-a-project-permissions-template) enabled on your permissions template.
- **Limitations:**

 - **For customers using the Company level ERP Integrations tool**The default segments in WBS are compatible with Procore's tool. However, some integrations do NOT yet support custom segments.
 - **For customers who have independently developed or purchased a third-party solution to integrate with Procore**To take advantage of the custom segment capabilities associated with WBS, any existing API integrations that you have independently developed or purchased to interact with Procore must be updated to support Procore's new WBS API.

## Prerequisites

- [Add Company Cost Codes](/process-guides/company-administration-work-breakdown-structure-guide/add-company-cost-codes)

## Steps

1. Navigate to the Project level **Admin** tool.
2. Under 'Project Settings', click the **Work Breakdown Structure** link.
3. In the 'Segments' list, click the **Cost Codes** link.
4. Click **Cost Codes from Company**.
5. In the 'Add Cost Codes to this Project' window, choose from these options:

   - To copy all company cost codes to the project, click **Select All**.
   - To select specific cost codes, type a code in the **Search Cost Codes** box and highlight the codes to add.
   - To choose cost codes, expand the desired segment items and highlight the segment items to copy.
6. Click **Add**.

## Next Steps

- [Assign Project Cost Codes to Sub Jobs](/process-guides/project-administration-work-breakdown-structure-guide/assign-project-cost-codes-to-sub-jobs)