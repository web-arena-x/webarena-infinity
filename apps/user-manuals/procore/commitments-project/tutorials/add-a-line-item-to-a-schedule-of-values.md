# Add a Line Item to a Commitment's Schedule of Values

Source: https://v2.support.procore.com/product-manuals/commitments-project/tutorials/add-a-line-item-to-a-schedule-of-values

---

## Background

After you create a commitment, use the steps below to add line items to the Schedule of Values.

## Things to Consider

- **Required User Permissions:**

 - 'Admin' level permissions on the project's Commitments tool.
- **Additional Information:**

 - To complete the steps below, the contract will need to be in the 'Draft' status. However, if the 'Enable Always Editable Schedule of Values' configuration setting is turned ON in this tool, users with the required user permission to [Edit a Commitment](/product-manuals/commitments-project/tutorials/edit-a-commitment) can edit the Schedule of Values when a commitment is in any status. To learn more, [What is the 'Enable Always Editable Schedule of Values' setting?](/faq-what-is-the-enable-always-editable-schedule-of-values-setting)
- **For companies using the** **ERP Integrations tool:** Prerequisites, requirements, limitations, and considerations might apply depending on the ERP system your Procore account is integrated with.

## Prerequisites

- [Create a Commitment](https://support.procore.com/products/online/user-guide/project-level/commitments/tutorials/create-a-commitment)
- Set the accounting method. See [Edit the Advanced Settings on a Commitment](/product-manuals/commitments-project/tutorials/edit-the-advanced-settings-on-a-commitment).

## Steps

1. Navigate to the project's **Commitments** tool.
2. Under the **Contracts** tab, locate the commitment to update. Then click **Edit**.
3. Click **Schedule of Values**.
4. Click **Add Line**.

   ##### Â Note

   If the 'Enable Always Editable Schedule of Values' setting is turned ON in the Commitments tool, users with the required user permission to Edit a Commitment can modify the Schedule of Values while a commitment is in any status.

- Follow the appropriate steps depending on whether your accounting method is **Amount Based** or **Unit/Quantity Based**:

 ##### Â Note

 To edit your accounting method before adding SOV line items, see [Edit the Advanced Settings Tab on a Commitment](/product-manuals/commitments-project/tutorials/edit-the-advanced-settings-on-a-commitment). To learn more, see [How do I set the accounting method for a contract or funding?](/faq-how-do-i-set-the-accounting-method-for-a-contract-or-funding)

1. **For contracts using the** ***Amount Based*** **accounting method**:

   1. **#**Automatically enters a line item number in sequential order.
   2. **Change Event Line Item**If you have change events enabled, you can select a change event line item if the commitment needs to be linked to a change event.
   3. **Budget** **Code**Select a budget code from the list or click **Create Budget Code** to create a new one. See [What is a budget code in Procore's WBS?](/faq-what-is-a-budget-code-in-procores-wbs)
   4. **Description**Enter a description for the line item. For example, type: Monthly Service Fee
   5. **Amount**Enter the amount of the cost.
   6. **Billed to Date**The system automatically calculates the amount billed on the commitment up to the current date.
   7. **Amount Remaining**Enter the amount that has NOT been billed to the current date.
   8. **Tax Code**Enter a tax code to use for this line item. This field only appears if you have enabled the tax codes feature. See [How can I use tax codes on a project?](/faq-how-can-i-use-tax-codes-on-a-procore-project)
2. **For contracts using the** ***Unit/Quantity Based*** **accounting method**:

   1. **#**Automatically enters a line item number in sequential order.
   2. **Change Event Line Item**If you have change events enabled, you can select a change event line item if the commitment needs to be linked to a change event.
   3. **Budget Code**Select a budget code from the list or click **Create Budget Code** to create a new one. See [What is a budget code in Procore's WBS?](/faq-what-is-a-budget-code-in-procores-wbs)
   4. **Description**Enter a description for the line item. For example, type: Monthly Service Fee
   5. **Qty**Enter the number of units.
   6. **UOM**Enter the **Unit of Measure (UOM)**.

      ##### Â Notes

      - To view the default options in the list, see [Which units of measure are included on Procore's master list?](/faq-which-units-of-measure-are-included-in-procores-master-list)
      - To update the available options in the list, see [Update a Unit of Measure to the Unit of Measure Master List](/product-manuals/admin-company/tutorials/update-a-unit-of-measure-on-the-unit-of-measure-master-list).