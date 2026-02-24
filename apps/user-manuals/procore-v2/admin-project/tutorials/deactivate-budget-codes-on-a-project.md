# Deactivate Budget Codes on a Project

Source: https://v2.support.procore.com/product-manuals/admin-project/tutorials/deactivate-budget-codes-on-a-project

---

## Background

If your team has created budget codes on a project and you no longer want your project team to assign those codes to line items in Procore's Project Financials tools, you can use the steps below to deactivate selected budget codes from your project. This action deactivates the code on the project and removes it from the drop-down list in the 'Budget Code' column in all of Procore's Project Financial tools.

##### Example

As shown in the illustrations below, an 'Active' budget code is available in the drop-down list as a selection in the 'Budget Code' column in all of Procore's Project Financials tools. An 'Inactive' budget code is not available for use.

##### Active Budget Codes

Appear as options in the 'Budget Code' drop-down list.

##### Inactive Budget Codes

Do NOT Appear as options in the 'Budget Code' drop-down list.

## Things to Consider

- **Required User Permissions:**

 - You need one of the following:

    - 'Admin' level permissions on the Project level Admin tool.
    - 'Read Only' or 'Standard' level permissions on the Project level Admin tool with the ['Manage WBS Codes' granular permission](/product-manuals/permissions-company/tutorials/grant-granular-permissions-in-a-project-permissions-template) enabled on your permission template.
- **If your account is ERP integrated:**

 - Keep in mind that data coming into Procore from your ERP system can still be logged against a deactivated budget code.

## Steps

- Deactivate a Budget Code
- Deactivate Budget Codes in Bulk

### Deactivate a Budget Code

1. Navigate to the project's **Admin** tool.
2. Click the **Work Breakdown Structure** link.
3. Click the **Budget Code Usage** tab.
4. Locate the budget code that you want to deactivate.

   ##### Â Notes

   To help you locate the code, you have these options:

   - To search for a specific budget code, type in the desired code in the **Search** box.

- Click the **Status** drop-down list and select the *Inactive* option.   
     
   Procore deactivates the budget code on the project. The code is removed as a option to select from the drop-down list in the 'Budget Code' column' on all of the tools in Project Financials.

### Deactivate Budget Codes in Bulk

1. Navigate to the project's **Admin** tool.
2. Click the **Work Breakdown Structure** link.
3. Click the **Budget Code Usage** tab.
4. Mark the checkboxes that correspond to one or more 'Active' budget codes in the usage table.
5. Click the **Change Status** menu and choose **Inactive** from the drop-down list.