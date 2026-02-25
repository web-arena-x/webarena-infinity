# Configure Settings: Change Events

Source: https://v2.support.procore.com/product-manuals/change-events-project/tutorials/configure-advanced-settings-change-events

---

## Background

If you have been granted the appropriate permissions, you can configure a variety of advanced settings for the project's Change Events tool.

## Things to Consider

- **Required User Permissions**:

 - 'Admin' level permissions on the project's Change Events tool.
- **Additional Information**:

 - To learn more about the columns displaying in the Change Events tool, see these links:\* To enable the 'Sub Jobs' column, see [Enable Sub Jobs on Projects for WBS](/process-guides/company-administration-work-breakdown-structure-guide/enable-sub-jobs-for-projects).\* To enable the 'Production Qty' and 'Production UOM' columns, see [Enable the Labor Productivity Cost Features for Project Financials](/process-guides/resource-tracking-and-project-financials-setup-guide/enable-labor-productivity).\* To enable the 'Non-Commitments' column, see [How do I track non-commitment costs on a change event?](/faq-how-do-i-track-non-commitment-costs-on-a-change-event)\* For more information, see [How do the Change Events tool's column display settings work?](/faq-how-do-the-change-event-tools-column-display-settings-work)

## Prerequisites

- Review this FAQ. See [Can I enable the Change Events tool on my existing project?](/faq-can-i-enable-the-change-events-tool-on-my-project)
- Add the Change Events tool to the project. See [Add and Remove Project Tools](/product-manuals/admin-project/tutorials/add-and-remove-project-tools)

## Steps

Follow these steps in these tasks to configure the settings for the Change Events tool:

- Enable and Disable the Column Display
- Maintain Budget Codes Across All Line Items in Sync
- Allow Line Item auto-population of Budget Code, Vendor, and Contracts
- Add Estimated Markup to All of the Change Events on a Project
- Set Attachment Settings
- Configure the Budget ROM Settings
- Prevent Budget Changes and Potential Change Orders on the Same Change Event Line Item
- Set User Permissions

### Configure Latest Cost or Latest Price Change Order Creation

To configure this setting, enable the Change Orders tool. See [Enable the Change Orders Tool](/product-manuals/change-orders-project/tutorials/enable-the-change-orders-tool).

1. Navigate to the project's **Change Events** tool.
2. Click **Configure Settings** .
3. Under **Change Orders**, choose an option to define how Procore creates Commitment Change Orders:

   - To consistently track line item cost, mark the **Always Create Commitment Change Orders Using Latest Cos**t check box. This ensures new commitment change orders track the latest costs on the line item, even if potential change orders exist.   
      OR
   - To consistently track line item revenue, leave this check box blank. This ensures the latest price of the line item and potential change order are passed to the commitment change order.

### Enable and Disable the Column Display

1. Navigate to the project's **Change Events** tool.
2. Click **Configure Settings** .
3. Choose from these options to show or hide columns in the Change Events tool. 
   *Note*: The system turns all column displays on, by default. You can disable these columns by removing the checkmark. For a complete list of column's these settings affect, see [How do the Change Event tool's column display settings work?](/faq-how-do-the-change-event-tools-column-display-settings-work)

   - **Display Revenue ROM, Latest Price, Latest Cost, and Over/Under Columns** This checkbox turns the Revenue ROM columns ON and OFF. The default setting on new Procore projects is ON.\* To enable the columns, place a checkmark in this checkbox.\* To disable the columns, remove the checkmark from this box.

     ##### Â Important

     - If you choose to disable these columns from the Change Events tool, the 'Revenue ROM' column continues to be available in prime contract change orders. To learn more about the Revenue ROM columns, see [Add Financial Markup Lines with Revenue ROM to Change Events](/product-manuals/change-events-project/tutorials/view-or-edit-markup-estimates-on-change-event-line-items).
     - If you create a change event (see [Create a Change](/product-manuals/change-events-project/tutorials/create-a-change-event) [Event](/product-manuals/change-events-project/tutorials/create-a-change-event)) and select 'TBD' or 'In Scope' from the change event's **Scope** drop-down list, the 'Revenue ROM' field in the prime contract change order shows $0. If you choose 'Out of Scope,' the field shows the latest cost.

- **Display UOM, Revenue Qty, Revenue Unit Cost, ROM Unit Qty, and ROM Unit Cost Columns** This checkbox turns the unit-based columns ON and OFF in the view page of a change event. The default setting for this checkbox is OFF.\* To enable the columns, place a checkmark in this box.\* To disable the columns, remove the checkmark from this box.

 ##### Â Notes

 - Removing the setting does NOT disable the columns when creating a change event. They are only hidden when viewing a change event.
 - If your company is going to be creating change events from the T&M Tickets tool, it is recommended that you enable this setting. If you do not, the summarized line item information from a T&M ticket will not be visible in a change event. See [Create a Change Event from a T&M Ticket](/product-manuals/tm-tickets-project/tutorials/create-a-change-event-from-a-tm-ticket).

- Click **Save**.

### Maintain Budget Codes Across All Line Items in Sync

Change event line items associated with change orders will now be editable as long as the change order is also in an editable state. [How are line items and budget codes updated across change objects?](/faq-how-are-financial-line-items-and-budget-codes-updated-across-change-objects)

When users update budget codes they will sync across linked change objects if those objects are also in an editable state.

1. Navigate to the project's **Change Events** tool.
2. Click **Configure Settings** .
3. Check the box next to **Maintain Budget Codes across all Line Items in sync**.
4. Click **Save.**

*Note:* This setting is NOT retroactive. Budget codes that were not matching between objects before enabling this setting will not automatically sync upon activation. Only budget codes changed after enabling this setting will sync between objects.

### Allow Line Item auto-population of Budget Code, Vendor, and Contracts

This setting gives users the option to turn OFF the Change Event Line Item (CELI) pre-fill automation logic. This gives admins more control over data entry by preventing automatic population of fields such as Budget Code, Vendor, and Contracts.

1. Navigate to the project's **Change Events** tool.
2. Click **Configure Settings** .
3. Scroll to the **Line Items** section.
4. Check the box next to **Allow Line Item auto-population of Budget Code, Vendor, and Contracts** to turn the setting ON or OFF.
5. Click **Save**.

### Set Attachment Settings

##### Â Tip

These settings can be turned ON and OFF on your project by a user with 'Admin' permission on the Change Events tool. When the configuration settings are enabled, the system automatically attaches any documentation from the last RFQ response to new prime potential change orders and new commitment change orders when using the Bulk Actions menu to create change orders.