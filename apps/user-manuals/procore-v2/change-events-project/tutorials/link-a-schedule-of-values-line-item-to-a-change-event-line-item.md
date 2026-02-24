# Link a Schedule of Values Line Item to a Change Event Line Item

Source: https://v2.support.procore.com/product-manuals/change-events-project/tutorials/link-a-schedule-of-values-line-item-to-a-change-event-line-item

---

## Background

There are three (3) ways to link an existing change order or a commitment to a change event line item:

- **Use the Bulk Actions menu option to create a change order or commitment line item from the change event**. First, add a change event line item to commitment or a change order while it is in an unapproved status. For commitments and commitment change orders, see [Add a Change Event Line Item to an Unapproved Commitment](/product-manuals/change-events-project/tutorials/add-a-change-event-line-item-to-an-unapproved-commitment) or [Add a Change Event Line Item to an Unapproved Commitment CO](/product-manuals/change-events-project/tutorials/add-a-change-event-line-item-to-an-unapproved-commitment-co). For prime contract change orders, see [Add a Change Event Line Item to an Unapproved Prime PCO](/product-manuals/change-events-project/tutorials/add-a-change-event-line-item-to-an-unapproved-prime-pco).
- **Use the Steps below to link an SOV line item to a change event line item**. You can use the steps below to create a link between an SOV line item on a commitment, commitment change order, or prime contract change order to a change event line item. See Link a Schedule of Values Item to a Change Event Line Item or Link a Schedule of Values Item to a Change Event Line Item.
- **Create a new change event line item from an SOV line item.** You can create new line items on a preexisting change event from an SOV line item. See Create a New Change Event Line Item from an SOV Line Item.

## Things to Consider

- **Required User Permissions:**

 - 'Admin' level permissions on the project's Commitments tool. 
     OR
 - 'Admin' level permissions on the project's Prime Contracts tool.

## Steps

- Link a Commitment's SOV Line Item to a Change Event Line Item
- Link a Change Order's SOV Line Item to a Change Event Line Item
- Create a New Change Event Line Item from an SOV Line Item

### Link a Commitment's SOV Line Item to a Change Event Line Item

1. Navigate to the project's **Commitments** tool.
2. View the commitment you want to edit.
3. In the **General** tab, scroll to the **Schedule of Values** card.
4. Click **Edit** in the Schedule of values card. 
   *Note*: 
    Procore restricts you from editing the commitment when the following is true:

   - There are one or more change orders in the *Approved* status.
   - The commitment has one or more invoices.
5. Click **Add Line** to create a new SOV line item or choose an existing line item and click the **Change Event Line Item** drop-down list.
6. Search for and select an existing change event.
7. Select a line item from the chosen change event to link to the SOV line item
8. Click **Save**.

### Link a Change Order's SOV Line Item to a Change Event Line Item

1. Navigate to the appropriate tool:

   - If you want to link a prime contract change order, navigate to the **Prime Contracts** tool.   
      OR
   - If you want to link a commitment change order, navigate to the **Commitments** tool.
2. View the contract linked to the change order you are editing.
3. Click **Change Orders**.
4. View the Change Order you want to create a new change event line item from.
5. Click **Schedule of Values**.
6. Click **Add Line** to create a new SOV line item or choose an existing line item and click the **Change Event Line Item** drop-down list.
7. Search for and select an existing change event.
8. Select a line item from the chosen change event to link to the SOV line item
9. Click **Save**.

### Create a New Change Event Line Item from an SOV Line Item

1. Navigate to the appropriate tool:

   - If you want to link a prime contract change order, navigate to the **Prime Contracts** tool.   
      OR
   - If you want to link a commitment change order, navigate to the **Commitments** tool.
2. View the contract linked to the change order you are editing.
3. Click **Change Orders**.
4. View the Change Order you want to create a new change event line item from.
5. Click **Schedule of Values**.
6. Click **Add Line** to create a new SOV line item or choose an existing line item and click the **Change Event Line Item** drop-down list.
7. Search for and select an existing change event.
8. Click **Create Line Item**.
9. Enter the following information:

   - **Budget Code**. The cost code from the change event automatically populates the line item.
   - **Description**. Enter a description for the line item.   
     *Note:* On commitment change orders, the **Vendor** and **Contract** fields are automatically populated with information from the contract.
10. Click **Create**.   
    *Note*: When users create a new change event line item, the budget code, description and any information currently in the SOV line item will populate back to the newly created change event line item.