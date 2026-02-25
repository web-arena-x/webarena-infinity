# Record Changes to Production Quantities in a Change Event

Source: https://v2.support.procore.com/product-manuals/change-events-project/tutorials/record-changes-to-production-quantities-in-a-change-event

---

## Background

For companies using Procore's Project Financials and Resource Management tools with the 'Procore Labor Productivity Cost' budget view, you can log additional production quantities and production hours associated with your change event line items in the 'Production Quantities' section of a change event.

##### Example

Let's assume that after your project's budget is locked, the project owner requests a design change that is out of scope with the original design. The change requires additional drywall, so you first create a change event and add a line item to that change event for that drywall. If that change represents a change to production, you will also want to record that change in the 'Production Quantities' tab of the change event.

Once you record the production quantities in the change events, the values are updated in the Change Events view page. The production quantities may also be associated with any Prime potential change order or Budget Change created from a Change Event. However, you must follow these steps: [Create a Prime Potential Change Order from a Change Event](/product-manuals/change-events-project/tutorials/create-a-prime-contract-change-order-from-a-change-event).

After you have submitted your prime contract change order to the owner for review, the owner can then approve or reject it. See [Approve or Reject Prime Contract Change Orders](/product-manuals/change-orders-project/tutorials/approve-or-reject-prime-contract-change-orders). When the status of the prime contract change order changes to 'Approved', the updated production quantities are reflected in the 'Procore Labor Productivity Cost' budget view and the Field Production Report.

## Things to Consider

- **Required User Permissions:**

 - 'Standard' level permissions or higher on the project's Change Events tool.

## Prerequisites

For production quantities to interact with labor productivity tracking feature, you must:

- [Enable the Labor Productivity Cost Features for Project Financials](/process-guides/resource-tracking-and-project-financials-setup-guide/enable-labor-productivity)
- [Set Up the Procore Labor Productivity Cost Budget View](/process-guides/resource-tracking-and-project-financials-setup-guide/preview-the-budget-view)
- [Set Up a Field Production Report](/product-manuals/timesheets-project/tutorials/set-up-a-field-production-report)

## Steps

Production Quantities relate to contracts and the budget through a combination of sub job and cost code. Users may edit these fields when editing change events line items in the change events edit page. However, if the Production Quantities are associated with a Prime potential change order or Budget Change, the Production Quantity will be locked unless unlinked from the change objects.

1. Navigate to the project's **Change Events** tool.
2. Locate and open an existing change event in the **Line Items** tab. 
    OR Create a new change event. See [Create Change Events](/product-manuals/change-events-project/tutorials/create-change-events).
3. Scroll to the **Production Quantities** card.
4. Click **Add Line**.
5. Complete the line item data entry as follows:

   - **Sub Job.** Select a sub job from the list.
   - **Cost Code.** Select a cost code from the list.
   - **Description.** Enter a description for the line item.
   - **Qty.** Enter a numeric value in this box to indicate the number of units that correspond to the unit of measurement that you specify.
   - **UOM.** Select a *Unit of Measure (UOM)* from the drop-down list. To learn about the default selections in this list, see [Which units of measure are included in Procore's master list?](/faq-which-units-of-measure-are-included-in-procores-master-list) and [Add a Unit of Measure to the Unit of Measure Master List](/product-manuals/admin-company/tutorials/update-a-unit-of-measure-on-the-unit-of-measure-master-list).
6. Click **Save**.