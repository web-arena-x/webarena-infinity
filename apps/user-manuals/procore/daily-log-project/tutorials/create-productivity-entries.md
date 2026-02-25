# Create Productivity Entries

Source: https://v2.support.procore.com/product-manuals/daily-log-project/tutorials/create-productivity-entries

---

## Background

The **Productivity** section allows you to track the material received on site and the material installed. This section displays if there are any approved subcontracts or purchase orders utilizing the Unit/Quantity accounting method, allowing you to track installation progress against line items in the contract.

## Things to Consider

- **Required User Permissions:**

 - *To create entries:* 'Standard' or 'Admin' level permissions on the project's **Daily Log** tool. 
    *Note*: Users must be able to view the relevant contract in order to add it to the Productivity entry.
 - *To create pending entries as a collaborator*: 'Read Only' or 'Standard' permissions to the project's **Daily Log** tool with the ['Collaborator Entry Only' granular permission](/product-manuals/permissions-company/tutorials/grant-granular-permissions-in-a-project-permissions-template) enabled on your permissions template.
- **Additional Information:**

 - In order to complete a Productivity entry, you must ensure the following about the commitment:

    - Set to use the Unit/Quantity accounting method.
    - Be in the 'Approved' status.
    - Have one or more line items added to the Schedule of Values (SOV).
- **Limitations:**

 - If you are using Procore's Project Financials tools, keep in mind that productivity entries do NOT sync with the *'Procore Labor Productivity Cost*' budget view.

## Steps

1. Navigate to the project's **Daily Log** tool.
2. Scroll to the Productivity section.
3. Enter the following information:

   - **#**: This uneditable field counts the number of entries in a section (e.g. the first entry created will be # 1, and the second entry will be # 2).

     No.
   - **Company**: Select the company name from the drop-down menu.   
     Companies must be added to the Directory tool to be selected in this drop-down menu.   
     See [Add a Company to the Project Directory](/process-guides/set-up-a-project-directory/create-companies).

     Company
   - **Contract**: Select the approved purchase orders from the Commitments tool that corresponds to the items that were put-in-place.

     Contract
   - **Line Item (#-Description-Qty Units)**: Select the applicable line item.

     Line Item (#-Description-Qty Units)
   - **Previously Delivered**: If there was a previous delivery of these items/materials, enter the number of items that were delivered to the job site previous to this date.

     Previously Delivered
   - **Previously Put-In-Place**: If there your team has already installed or put in place some of these items/materials, enter the total number of these items/materials that were previously put in place on the job site.

     Previously Put-In-Place
   - **Quantity Delivered**: Enter the total number of these items/materials that were delivered in on this date.

     Quantity Delivered
   - **Quantity Put-In-Place**: Enter the total number of items/materials that were installed or put in their final place on the job site on this date.

     QuantityÂ Put-In-Place
   - **Comments**: Enter any comments that may be needed to further describe the entry.

     Comments
4. Click **Create**.