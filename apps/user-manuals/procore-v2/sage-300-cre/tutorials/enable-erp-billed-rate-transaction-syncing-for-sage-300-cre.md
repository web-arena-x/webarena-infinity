# Enable ERP Billed Rate Transaction Syncing for Sage 300 CREÂ®

Source: https://v2.support.procore.com/product-manuals/sage-300-cre/tutorials/enable-erp-billed-rate-transaction-syncing-for-sage-300-cre

---

## Background

If your Procore company account is integrated with Sage 300 CREÂ®, you have the ability to import billed rate transactions from Sage 300 CREÂ®. This is done by designating specific cost types as billed rate transactions.

Transactions with this designation import the value from the *Billed Amount* in Sage 300 CREÂ®. Once imported, the values of those transactions can be viewed in the 'Direct Costs' column on a budget line item in a Procore project. Also, users with the appropriate granular permission can click the values in the 'Direct Costs' column in the Budget tool to open a window showing detailed information about the item.

- **Add a 'Direct Costs' source column to your Procore project's budget view**
- **Track Sage 300 CREÂ® direct costs in a Procore budget**  
  Once the 'Direct Costs' column has been added to a budget view, project users with permission to the Budget tool can view the lump-sum totals from Sage 300 CREÂ® job cost transactions as a direct cost value on a budget line item. The value in this column shows your project's 'Direct Costs' total for all items in the 'Pending', 'Revise and Resubmit', and 'Approved' status.  
  *Note*: An accounting approver can sync the job cost transaction details from Sage 300 CREÂ® on the Job Costs tab of the ERP Integrations tool.
- **View direct cost transaction detail on a budget line item.**   
  Project users with the ['View Direct Cost Detail' granular permission](/product-manuals/permissions-company/tutorials/grant-granular-permissions-in-a-project-permissions-template) enabled on their permission template can click the link in the Direct Costs column of a budget line item to open the direct cost's details in a popup window.

## Things to Consider

- **Required User Permissions**:

  - To enable this setting, 'Admin' on the project's Admin tool.
  - To submit a request to enable the feature in your company's Procore account, you must be your company's 

    A *Procore Administrator* is a user who has 'Admin' level permissions on all of the Company level Tools in Procore. Granting a user âAdminâ level permissions in the Company level Directory tool automatically assigns that user âAdminâ permissions on all Company level tools. Also called a *Company Administrator*.

    ProcoreÂ Administrator or the designated ERP Integration Contact on your company's Procore account.
- **Requirements**:  
  To enable this feature on a Procore project:

  - You must be sending costs to the Billing (BL) module in Sage 300 CREÂ® and using the Billing module to generate Work in Progress (WIP).
  - Your company's Procore Administrator must to specify which cost types should be designated as billed rate transactions.
  - A user with administrative privileges to your company's Sage 300 CREÂ® server must follow the steps in [Setup the hh](/product-manuals/sage-300-cre/tutorials/set-up-the-hh2-client-to-sync-job-cost-transactions-data).
  - Your Procore Administrator (or a user with 'Admin' permission on the project's Admin tool) must enable the job cost transactions syncing capability as described below.
  - Your Procore Administrator must update your project's budget view(s) to complete these steps:

    1. If you have previously completed the steps described in [Add the 'ERP Direct Costs' Column to a Procore Budget View for ERP Integrations](/product-manuals/admin-company/tutorials/add-the-erp-direct-costs-column-to-a-procore-budget-view-for-erp-integrations), you will need to remove both the existing 'ERP Direct Costs' calculated column and the 'ERP Job to Date Costs' source column.
    2. After removing these columns, you will need to add the recommended columns for job cost transaction syncing to your budget view. For instructions, see [Add the Columns for ERP Job Cost Transaction Detail to a Budget View](/product-manuals/erp-integrations-company/tutorials/add-columns-to-a-budget-view-for-erp-job-cost-transaction-detail).

## Steps

1. Navigate to the project's **Admin** tool.
2. Under **Project Settings**, click **General**.
3. Scroll to **Advanced Settings**.
4. Place a checkmark in the **Enable ERP Job Cost Transaction Syncing** checkbox.  
   This action enables the syncing feature in the project.
5. Click **Update**.

## Next Steps

- [Add the Columns for ERP Job Cost Transaction Detail to a Budget View](/product-manuals/erp-integrations-company/tutorials/add-columns-to-a-budget-view-for-erp-job-cost-transaction-detail)