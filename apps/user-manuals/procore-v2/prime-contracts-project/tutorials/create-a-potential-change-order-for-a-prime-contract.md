# Create a Potential Change Order for a Prime Contract

Source: https://v2.support.procore.com/product-manuals/prime-contracts-project/tutorials/create-a-potential-change-order-for-a-prime-contract

---

## Background

When a change to the scope of work or the original prime contract amount occurs during a construction project, the change management process begins. You can create a PCO if your company's [Procore Administrator](https://support.procore.com/procore-learning-paths/general-contractor/procore-administrator) configures the Prime Contracts tool with the two (2)- or three (3)-tier change order configuration setting. See [What are the different change order tier settings in Project Financials?](/faq-what-are-the-different-change-order-tier-settings-in-project-financials)

## Things to Consider

- **Required User Permissions:**

  - Admin' level permissions on the project's Change Orders tool.

    ##### Â Important

    **Do not use the steps below when**:

    - The Change Events tool is enabled on the projects. Follow these steps instead: [Create a Prime Potential Change Order from a Change Event](/product-manuals/change-events-project/tutorials/create-a-prime-potential-change-order-from-a-change-event).
    - The Prime Contracts tool is configured with the one (1) tier change order configuration setting. Follow these steps instead: [Create a Prime Contract Change Order](/product-manuals/prime-contracts-project/tutorials/create-a-prime-contract-change-order).

- **Additional Information:**

  - After a PCO is approved, the next step depends on the Prime Contracts tool's change order configuration setting:\* For the two (2)-tier change order setting, continue with these steps: Create Prime Potential Change Order\* For the three (3)-tier change order setting, continue with these steps: [Create a Change Order Request for a Prime Contract](/product-manuals/prime-contracts-project/tutorials/create-a-change-order-request)
- For companies using the  ERP Integrations tool: **Show/Hide**

  - Not all ERP integrations support the sync of change orders. For those that do, additional requirements, limitations, and considerations vary depending on the ERP system your company's account is integrated with. See [Things to Know About your ERP Integration](https://support.procore.com/products/online/user-guide/company-level/erp-integrations/things-to-know-about-your-erp-integration) for details.

## Prerequisites

- Its recommended that you configure the Prime Contracts tool with the 2-tier change order configuration setting. The 3-tier setting is also supported. See [What are the different change order tier settings in Project Financials?](/faq-what-are-the-different-change-order-tier-settings-in-project-financials)

## Steps

- Create a Potential Change Order
- Add a Schedule of Values to a Potential Change Order

### Create a Potential Change Order

1. Navigate to the project's **Prime Contracts** tool.
2. Locate the prime contract to work with. Then click its **Number** link.
3. Click the **Change Orders** tab.
4. Click **Create Potential CO**.
5. Complete the following fields:

   - **Number**  
      Procore automatically assigns a sequential number to the new PCO. You can change this number if you want.
   - **Date Created**  
      Shows the creation date and time. This value cannot be changed.
   - **Revision**  
      Shows the revision number. The first version is zero (0), subsequent revisions are assigned in sequential order. A PCO might have several revisions, depending on its reviewer/approver feedback.
   - **Created By**  
      Shows the Procore user who created the PCO. This value cannot be changed.
   - **Contract Company**  
      Shows the name of the company responsible for performing the work on the contract.
   - **Contract**  
      If you have been assigned access permissions to the Prime Contracts tool, click this link to open the contract.
   - **Title**  
      Enter a title for the PCO in this box.
   - **Prime Contract Change Order**  
      Select a [Prime Contract Change Order (PCCO)](/glossary-of-terms) from the list to link it to the PCO.
   - **Status**  
      Select the current state of the PCO. To learn more, see [What are the default statuses for change orders in Procore?](/faq-what-are-the-default-statuses-for-change-orders-in-procore)
   - **Change Reason**  
      Select the reason for the PCO, either *Client Request*, *Design Development*, *Allowance*, *Existing Condition*, *Back Charge*, or any additional options created for your specific environment by your company's [Procore Administrator](https://support.procore.com/procore-learning-paths/general-contractor/procore-administrator). See [Set Default Change Management Configurations](/product-manuals/admin-company/tutorials/set-the-default-change-management-configurations).
   - **Change Order Request**

     ##### Â Note

     The [Change Order Request (COR)](/glossary-of-terms) setting is only required when the Prime Contracts tool is using the 3-Tier change order configuration setting. See [What are the different change order tier settings in Project Financials?](/faq-what-are-the-different-change-order-tier-settings-in-project-financials)

     - **None**. A PCO can be linked to a COR at a later time.
     - **Add to Existing**. Link the PCO to an existing COR.
     - **Create New**. Create a new COR. You also have the option to create a new PCCO at the same time.

- **Private**  
   Mark this checkbox if you only want the potential change order to be visible to users with 'Admin' permissions on the Prime Contracts tool.
- **Accounting Method**  
   This field inherits the accounting method that was specified in the prime contract. See [How do I set the accounting method for a contract or funding?](/faq-how-do-i-set-the-accounting-method-for-a-contract-or-funding)
- **Description**  
   Enter a more detailed description of the reason for the PCO.
- **Request Received From**  
   Select the Procore user for whom you are submitting the PCO.
- **Schedule Impact**  
   If known, provide an estimate for the additional number of days required to complete work when the PCO is approved.
- **Location**  
  Use this drop-down list to select a location related to the PCO. You can select an existing location or [Add a Multi-tiered Location to an Item](/product-manuals/admin-project/tutorials/add-a-multi-tiered-location-to-an-item).
- **Reference**  
   Add any other important tools, materials, drawings, or documents to uses as a reference for the PCO.
- **Field Change**  
   Check this box if the PCO requires a field change.
- **Paid in Full**  
   Check this box to indicate you have received payment for this change.
- **Attachments**  
   Select and add any relevant documents.
- Click **Create**.

### Add a Schedule of Values to a Potential Change Order

When there are costs associated with a PCO, you must add line items to the SOV.

1. In the PCO click the **Schedule of Values** tab

   ##### Â Notes

   - If sub-jobs are enabled (see [Enable Sub Jobs on Projects for WBS](/process-guides/company-administration-work-breakdown-structure-guide/enable-sub-jobs-for-projects)), the Sub Jobs drop-down list contains all sub-jobs added to the project. See [Add 'Sub Job' Segment Items to a Procore Project](/process-guides/project-administration-work-breakdown-structure-guide/add-sub-jobs-to-a-project).
   - All cost codes related to the sub-jobs will appear in the following field.