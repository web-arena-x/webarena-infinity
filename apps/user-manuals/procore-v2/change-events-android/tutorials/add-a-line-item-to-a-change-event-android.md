# Add a Line Item to a Change Event (Android)

Source: https://v2.support.procore.com/product-manuals/change-events-android/tutorials/add-a-line-item-to-a-change-event-android

---

## Background

With the Change Events tool, your project users have the ability to add financial line items to a change event on your iOS mobile device.

## Things to Consider

- **Required User Permissions:**

 - 'Standard' or 'Admin' level permissions on the project's Change Events tool.
- **Additional Information:**

 - This action can be performed in offline mode if the asset/item was previously viewed and cached on your mobile device. Tasks performed in offline mode will sync with Procore once a network connection is reestablished.

## Prerequisites

- [Create a Change Event (Android)](/product-manuals/change-events-android/tutorials/create-a-change-event-android)

## Steps

1. Navigate to the project's **Change Events** tool using the Procore app on an Android mobile device.
2. Tap the change event that you want to add a line item to.
3. Scroll down to **Line Items** and tap **+ADD**.
4. Complete the line item data entry as follows:

   - **Description** Enter a description for the line item.
   - **Vendor** Select a the vendor's company name from the drop-down menu. See [Add a Company to the Project Directory](/process-guides/set-up-a-project-directory/create-companies).
   - **Contract** Select the impacted purchase order or subcontract from the drop-down menu. See [Create a Commitment](https://support.procore.com/products/online/user-guide/project-level/commitments/tutorials/create-a-commitment).
   - **Provide Budget Code** Tap the slider to select the budget code to assign a budget code to the line item. See [What is a budget code in Procore's WBS?](/faq-what-is-a-budget-code-in-procores-wbs)
   - **Cost ROM** Enter a numeric estimation of the cost's Rough Order of Magnitude (ROM). This entry has NO financial impact on values in other Procore tools. You can add the ROM to the Budget by following the steps in [Add Cost ROM, RFQ & Non-Commitment Cost Source Columns to a Budget View](/product-manuals/change-events-project/tutorials/add-cost-rom-rfq-and-non-commitment-source-columns-to-a-budget-view).
     *Notes:*\* If you are using the enhancements for unit-based financials, this column will capture unit changes to UOM on both Rev ROM and Cost ROM.\* If you follow those steps to show the ROM value in the budget, and the change event line item ends up having no cost, you will need to zero out the ROM to remove it from the budget