# Create Productivity Entries - Procore

Source: https://support.procore.com/products/online/user-guide/project-level/daily-log/tutorials/create-productivity-entries

---

## Objective

To create Productivity entries in the project's Daily Log tool.

## Background

The Productivity section allows you to track how much material arrives on site and how much is installed. Any "Approved" subcontracts or purchase orders with the Unit/Quantity accounting method will appear here so you can track the installation against the line items in the contract.

## Things to Consider

- **Required User Permissions:**
  - - **To create entries:**
      - 'Standard' or 'Admin' level permissions on the project's Daily Log tool.  
        *Note*: Users must be able to view the relevant contract in order to add it to the Productivity entry. See [View Commitments](https://support.procore.com/products/online/user-guide/project-level/commitments/tutorials/view-commitments "View Commitments").
    - ****To create pending entries as a collaborator****:
      - 'Read Only' or 'Standard' permissions to the Daily Log tool with the ['Collaborator Entry Only' granular permission](../../../company-level/permissions/tutorials/grant-granular-permissions-in-a-project-permissions-template.md#Daily_Log "Grant Granular Permissions in a Permission Template") enabled on your permissions template. See [Create Daily Log Entries as a Collaborator](https://support.procore.com/products/online/user-guide/project-level/daily-log/tutorials/create-daily-log-entries-as-a-collaborator "Create Daily Log Entries as a Collaborator").
- **Additional Information:**
  - In order to complete a Productivity entry, you must ensure the following about the commitment:
    - Set to use the Unit/Quantity accounting method. See [How do I set the accounting method for a contract or funding?](https://support.procore.com/faq/how-do-i-set-the-accounting-method-for-a-contract-or-funding "How do I set the accounting method for a contract or funding?")
    - Be in the 'Approved' status. [Approve and Sign a Commitment Contract](https://support.procore.com/products/online/user-guide/project-level/commitments/tutorials/approve-and-sign-a-subcontract "Approve and Sign a Commitment Contract").
    - Have one or more line items added to the Schedule of Values (SOV). See. [Add a Line Item to a Commitment's Schedule of Values](https://support.procore.com/products/online/user-guide/project-level/commitments/tutorials/add-a-line-item-to-a-schedule-of-values "Add a Line Item to a Commitment's Schedule of Values").
- **Limitations:**
  - For Procore customers using Project Financials tools, keep in mind that productivity entries do NOT interact with the 'Procore Labor Productivity Cost' budget view. For more information, see [Set Up the Procore Labor Productivity Cost Budget View](https://support.procore.com/products/online/user-guide/company-level/admin/tutorials/set-up-the-procore-labor-productivity-cost-budget-view "Set Up the Procore Labor Productivity Cost Budget View").

## Steps

1. Navigate to the project's **Daily Log** tool.
2. Scroll to the Productivity section.
3. Enter the following information:
   - **#**: This uneditable field counts the number of entries in a section (e.g. the first entry created will be # 1, and the second entry will be # 2).
   - **Company**: Select the company name from the drop-down menu. Companies must be added to the Directory tool to be selected in this drop-down menu. See [Add a Company to the Project Directory](https://support.procore.com/products/online/user-guide/project-level/directory/tutorials/add-a-company-to-the-project-directory "products/online/user-guide/project-level/directory/tutorials/add-a-company-to-the-project-directory").
   - **Contract**: Select the approved purchase orders from the Commitments tool that corresponds to the items that were put-in-place.
   - **Line Item (#-Description-Qty Units)**: Select the applicable line item.
   - **Previously Delivered**: If there was a previous delivery of these items/materials, enter the number of items that were delivered to the job site previous to this date.
   - **Previously Put-In-Place**: If there your team has already installed or put in place some of these items/materials, enter the total number of these items/materials that were previously put in place on the job site.
   - **Quantity Delivered**: Enter the total number of these items/materials that were delivered in on this date.
   - **Quantity Put-In-Place**: Enter the total number of items/materials that were installed or put in their final place on the job site on this date.
   - **Comments**: Enter any comments that may be needed to further describe the entry.
4. Click **Create**.

## Next Step

- [Mark a Daily Log as Complete](https://support.procore.com/products/online/user-guide/project-level/daily-log/tutorials/mark-a-daily-log-as-complete "Mark a Daily Log as Complete")

##