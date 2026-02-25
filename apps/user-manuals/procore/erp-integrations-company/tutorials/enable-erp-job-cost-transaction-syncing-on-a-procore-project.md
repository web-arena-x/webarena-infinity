# Enable ERP Job Cost Transaction Syncing on a Procore Project

Source: https://v2.support.procore.com/product-manuals/erp-integrations-company/tutorials/enable-erp-job-cost-transaction-syncing-on-a-procore-project

---

##### ERP DOCUMENTATION

**Each Procore-built ERP integration offers its own unique feature set.** Your integration might not support the action described on this page.

To learn about your integration and its supported features, see [Which ERP integrations are supported by Procore?](/faq-which-erp-integrations-are-supported-by-procore)

## Background

If your company's Procore account is integrated with an ERP system that supports this feature, you can import job cost transaction data from your ERP. Once imported, the values of those transactions can be viewed in the 'Direct Costs' column on a budget line item in a Procore project.

Users who are assigned the appropriate granular permission can click the values in the 'Direct Costs' column in the budget tool to open a window showing detailed information about the item.

- **Add a 'Direct Costs' source column to your Procore project's budget view** Provides authorized users with the ability to add a 'Direct Costs' column to your project's budget view.
- **Track ERP costs in a Procore** **budget** Once the 'Direct Costs' column has been added to a budget view, project users with access permissions to the budget can view the lump-sum totals from the job cost transactions as a value on a budget line item. The value in this column shows your project's 'Direct Costs' total for the types and statuses selected in the column configuration. To learn more see [Add Columns to a Budget View for ERP Job Cost Transaction Detail](/product-manuals/erp-integrations-company/tutorials/add-columns-to-a-budget-view-for-erp-job-cost-transaction-detail).
- **View direct cost transaction detail on a budget line item.** Project users with the ['View Direct Cost Detail' granular permission](/product-manuals/permissions-company/tutorials/grant-granular-permissions-in-a-project-permissions-template) enabled on their permission template can click the hyperlink in the Direct Costs column of a budget line item to open the direct cost's details in a popup window. This granular permission is located in the 'Budget' area when configuring a permission template.

## Things to Consider

- **Required User Permissions**:

 - *To enable this setting,* 'Admin' level permissions on the project's Admin tool.
 - *To submit a request to enable the feature in your company's Procore account,* you must be your company's 

    A *Procore Administrator* is a user who has 'Admin' level permissions on all of the Company level Tools in Procore. Granting a user âAdminâ level permissions in the Company level Directory tool automatically assigns that user âAdminâ permissions on all Company level tools. Also called a *Company Administrator*.

    ProcoreÂ Administrator or the designated ERP Integration Contact on your company's Procore account.
- **Requirements**:

 - Your company's Procore Administrator must submit a request to your company's Procore point of contact to enable this feature on the backend of Procore.
 - A user with 'Admin' permission on the project's Admin tool must enable the job cost transaction syncing capability as described in the steps below.
 - Your Procore Administrator must update your project's budget view(s) to complete these steps:

    1. If you have previously completed the steps described in [Add the 'ERP Direct Costs' Column to a Procore Budget View for ERP Integrations](/product-manuals/admin-company/tutorials/add-the-erp-direct-costs-column-to-a-procore-budget-view-for-erp-integrations), you will need to remove both the existing 'ERP Direct Costs' calculated column and the 'ERP Job to Date Costs' source column.
    2. After removing these columns, you will need to add the recommended columns for job cost transaction syncing to your budget view. For instructions, see [Add Columns to a Budget View for ERP Job Cost Transaction Detail](/product-manuals/erp-integrations-company/tutorials/add-columns-to-a-budget-view-for-erp-job-cost-transaction-detail).

## Steps

1. Navigate to the project's **Admin** tool.
2. Under 'Project Settings', click **General**.
3. Scroll to 'Advanced'.
4. Mark the checkbox to **Enable ERP Job Cost Transaction Syncing**. 
   This action enables the syncing feature in the project.
5. Click **Update**.

## Next Steps

- [Add Columns to a Budget View for ERP Job Cost Transaction Detail](/product-manuals/erp-integrations-company/tutorials/add-columns-to-a-budget-view-for-erp-job-cost-transaction-detail)