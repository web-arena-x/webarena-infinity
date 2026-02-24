# Copy Bid Forms from a Previous Bid Package

Source: https://v2.support.procore.com/product-manuals/bidding-project/tutorials/copy-bid-forms-from-a-previous-bid-package

---

## Background

After you create a new bid package, you can copy bid forms from previous bid packages to the new one. You can choose which bid forms to copy, and if you want to copy both bidders and line items to the new bid package.

## Things to Consider

- **Required User Permissions**

 - 'Admin' level permissions to the project's Bidding tool. 
    *Note:* You will only have access to copy bid packages from projects that you have access to.
- **Additional Information**

 - Copying bid forms is only available for bid packages created after March 18, 2024.
 - Bid forms can be copied from projects that:

    - Use the Enhanced Bidding Experience.
    - Are active and not archived.
    - Have at least one bid form in the bid package.
    - Cost codes from the previous project must match your current project.

## Prerequisites

- [Create a Bid Package](/product-manuals/bidding-project/tutorials/create-a-bid-package)

## Steps

1. Navigate to the project's **Bidding** tool.
2. Next to the bid package, click **View**.
3. Click the **Bidding** tab.
4. Click **Create Bid Form** and select **From Bid Package**.
5. Select the **bid package**.
6. Choose what information to copy to the new bid forms.

   ##### Â Note

   If you are copying **line items** from a bid package on another project, the current project will need to include the same cost code set as the source project. The following scenarios will occur if the projects do not have matching cost code sets.

   - For both ERP and non-ERP synced projects with **NO** cost codes, a cost code set will need to be added *manually* before the form can be copied.
   - For both ERP and non-ERP synced projects with cost code sets that do NOT match the source project, users will be shown both cost code sets so they can choose how they would like to proceed.
   - When the cost code set in the current project *does* match the source project but the current project is still missing specific cost codes, the following will take place:

     - Non-ERP Synced. Click **Continue** to add missing cost codes to the current project. A second confirmation will appear before the cost codes are added to the project.
     - ERP Synced. Click **Continue** to add any missing *non-project specific* cost codes to the current project. If the source project contains project specific cost codes, those must be added manually. A list of the missing cost codes will be provided as a reference when the cost codes are being added.

- Mark the checkboxes for the bid forms you want to copy.
- Click **Create**. After you have copied the bid forms, you can make edits as needed for the current project.