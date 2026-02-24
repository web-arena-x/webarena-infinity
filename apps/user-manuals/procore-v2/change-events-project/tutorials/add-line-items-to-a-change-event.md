# Add Change Event Line Items

Source: https://v2.support.procore.com/product-manuals/change-events-project/tutorials/add-line-items-to-a-change-event

---

## Background

There are three ways to add line items to a change event:

- **Manually add each line item** This allows you to add line items one-by-one.
- **Add line items in bulk using the 'Add Line Items for All Commitments' link** This option creates a new line item on the change event for each line item on a commitment that is in the 'Approved' state.
- **Import Line Items from a CSV File.**

## Things to Consider

- **Required User Permissions:**

 - 'Standard' level permissions or higher on the project's Change Events tool.
- **Additional Information:**

 - For companies using Procore's Project Financials and Resource Management tools, you can log changes to production quantities (for example, if the change event includes a production quantity change for additional drywall) on the Production Quantities tab. For details, see [Record Changes to Production Quantities in a Change Event](/process-guides/resource-tracking-and-project-financials-setup-guide/record-changes-on-a-change-event).

## Steps

##### Â Tip

**Did you know a user with 'Admin' settings on the Change Events tool can turn the Change Events tool's 'Column Display' settings ON and OFF?** For best results, your project's column display settings should be determined at the beginning of a project. To learn more, see [How do the Change Events tool's column display settings work?](/faq-how-do-the-change-event-tools-column-display-settings-work)

1. Navigate to the project's **Change Events** tool.
2. Choose from these options:

   - Click the **Detail** tab. Then find the change event to update and click **Edit**. 
        
      OR
   - Follow the steps in [Create Change Events](/product-manuals/change-events-project/tutorials/create-change-events).
3. In the 'Edit Change Event' page, scroll to the 'Line Items' card.
4. Choose from these options:

   - To add one (1) new line item on the change event, click **Add Line**.   
      OR
   - To add line items in bulk using line items from all of the project's commitments in the 'Approved' status, click **Add Lines for All Commitments**.   
      OR
   - To import line items from a CSV file, see [Import Change Event Line Items from a CSV File](/product-manuals/change-events-project/tutorials/import-change-event-line-items-from-a-csv-file).
5. Complete the line item data entry as follows:

   - **Budget Code**

     Select a budget code or click **Create Budget Code**. See [What is a budget code in Procore's WBS?](/faq-what-is-a-budget-code-in-procores-wbs)

     Budget Codes

     ##### Â Note

     If the budget code sync configure setting is enabled, the budget code of any items connected to the change event line item will also be updated. See [Configure Settings: Change Events](/product-manuals/change-events-project/tutorials/configure-advanced-settings-change-events).
6. **Description**Enter a description for the line item.

   Description
7. **Vendor**. Select the vendor's company name from the drop-down menu. See [Add a Company to the Project Directory](/process-guides/set-up-a-project-directory/create-companies).

   Vendor
8. **Contract**

   Select the impacted purchase order or subcontract from the drop-down menu. See [Create a Purchase Order](/product-manuals/commitments-project/tutorials/create-a-purchase-order) or [Create a Subcontract](/product-manuals/commitments-project/tutorials/create-a-subcontract).

   Contract
9. **Qty**

   Enter a numeric value in this box to indicate the number of units that correspond to the unit of measurement that you specify.

   Qty
10. Select a *Unit of Measure (UOM)* from the drop-down list. To learn about the default selections in this list, see [Which units of measure are included in Procore's master list?](/faq-which-units-of-measure-are-included-in-procores-master-list) and [Add a Unit of Measure to the Unit of Measure Master List](/product-manuals/admin-company/tutorials/update-a-unit-of-measure-on-the-unit-of-measure-master-list).

    UOM
11. **Unit Cost**

    Enter the monetary cost in this box to indicate the cost per unit of measurement.

    Unit Cost
12. **Cost ROM**. Enter a numeric estimation of the cost's Rough Order of Magnitude (ROM). This entry has NO financial impact on values in other Procore tools. You can add the ROM to the Budget by following the steps in [Add Cost ROM, RFQ & Non-Commitment Cost Source Columns to a Budget View](/product-manuals/change-events-project/tutorials/add-cost-rom-rfq-and-non-commitment-source-columns-to-a-budget-view).

    Cost ROM

    ##### Â Note

    - If you are using the enhancements for unit-based financials, this column will capture unit changes to UOM on both Rev ROM and Cost ROM.
    - If you follow those steps to show the ROM value in the budget, and the change event line item ends up having no cost, you will need to zero out the ROM to remove it from the budget.

- **Non-Committed Cost**

 Enter the amount of costs that are not associated with a Commitment or Commitment Change Order.

 Non-Committed Cost