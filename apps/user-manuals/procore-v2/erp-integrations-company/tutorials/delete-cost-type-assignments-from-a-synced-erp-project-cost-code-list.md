# Delete Cost Type Assignments from a Synced ERP Project Cost Code List

Source: https://v2.support.procore.com/product-manuals/erp-integrations-company/tutorials/delete-cost-type-assignments-from-a-synced-erp-project-cost-code-list

---

##### ERP DOCUMENTATION

**Each Procore-built ERP integration offers its own unique feature set.** Your integration might not support the action described on this page.

To learn about your integration and its supported features, see [Which ERP integrations are supported by Procore?](/faq-which-erp-integrations-are-supported-by-procore)

## Background

If your company's Procore account is integrated with an ERP system, you must assign at least one (1) project cost type to your project's listed cost codes. This is required for most ERP integrations to be able to carry over financial data from Procore to your ERP system.

After cost code data is synced between Procore and your ERP system, you may occasionally discover a need to delete one (1) or more cost type assignments from your project's cost code list.

## Things to Consider

- **Required User Permission**:

 - 'Admin' level permission on the project's Admin tool.
- **Requirements**:

 - The project must be configured to use the 'ERP Standard Cost Code' list.
 - **Requirements, considerations, and limitations vary depending on the ERP system your company is integrated with.***Note: It is common across many integrations to require that you delete cost types from your ERP system before you can delete them in Procore.*
 - The cost type(s) you want to delete must be removed from all items in Procore (e.g., Change Orders, Commitments, or Purchase Orders).

## Steps

1. Navigate to the project's **Admin** tool.
2. Under **Project Settings**, click **Cost Code Cost Type Assignments**.
3. In the **Cost Code/Cost Type Matrix** tab, remove the checkmark from any BLUE checkbox.   
      
   *Note*:

   - If a check box is grayed out and unavailable, it does not meet one or more of the requirements for deletion. The check box will be BLUE and available when the requirements are satisfied.
4. Click **Save**. 
    The system will process the delete request. 
   *Notes*:

   - If the delete action is successful, the checkmark is removed from the specified box.
   - If the delete action fails, the checkmark remains in the box and the request is logged in the **Delete History** tab.