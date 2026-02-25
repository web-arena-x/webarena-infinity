# Bulk Create Commitment Change Orders from a Change Event

Source: https://v2.support.procore.com/product-manuals/change-events-project/tutorials/bulk-create-commitment-change-orders-from-a-change-event

---

## Background

In Procore, a 

A *Change Event* is any event resulting in a modification that affects the *scope of work* on a construction project and the project's schedule and/or cost(s). In Procore, a change event can be recorded in the system and precedes the creation of a *change order*, which allows your team members and stakeholders to prepare for a cost change before it becomes an actual cost.

Change Event is any change that affects the scope of a construction project. Once a change event is recorded in Procore, project teams can create a Request for Quote (RFQ) to obtain quotes from the responsible contractors. See [Create RFQs from a Change Event](/product-manuals/change-events-project/tutorials/create-rfqs-from-a-change-event).

If you have a change event that impacts multiple contracts, you can bulk create multiple commitment change orders at once from the change events Line Items view.

## Things to Consider

- **Required User Permissions:**

 - 'Standard' level permissions or higher on the project's Change Events tool. 
     AND
 - 'Admin' level permissions on the project's Commitments tool.
- **Additional Information:**

 - Requirements for Change Event Line Items:\* Before executing bulk creation of Commitment Change Orders, specific criteria must be met for each selected line item:\* Change Event Line Item(s) must not be associated with another Commitment Change Order.\* Change Event Line Item(s) must have an assigned commitment contract and vendor.\* The associated commitment(s) must be 'Approved'.
 - Created Draft Commitment Change Orders:\* Commitment Change Orders created in bulk are given a default title of "CCO # - CE # - Title"\* The description will include the 'CE # - title' for all Change Events associated with the CCO, as well as the description of that Change Event.
 - Attachments:\* When Change Event Line Items are categorized by commitment contract, any attachments added to the associated Change Event of that line item will be migrated into the created draft Commitment Change Order.
- **ERP Information:**

 - Line item associations between change orders and commitment contract SOV must be made within the **ERP Integration** tab of the change orders after they are created.

## Steps

1. Navigate to the project's **Change Events** tool.
2. Select one or more change event line items to include in the 'Draft' change order.

   ##### Â Tip

   **Does the change impact line items from multiple change events?** If so, you can select line items across multiple change events. To filter the list by vendor, select the desired options from the **Filter** drop-down menu.

- Choose **Add To** **>** **Commitment CO > Create Bulk Draft Commitment COs**. 
   Procore populates the line items on the change order's Schedule of Values with the change event line items you select.
- *Optional:* Review any items that will not be added and select **Continue** or **Cancel**.

 ##### Â Tip

 If your company is using 2- or 3-tiered change orders for commitments, these steps will create commitment potential change orders that are later combined to create a commitment change order as follows:

 - **2-Tier: CE > CPCO > CCO**
 - **3-Tier: CE > CPCO > COR > CCO**

- Review the list of change orders that you will create for each vendor.
- Begin generating the change orders by clicking the **Create Commitment COs** button.

 ##### Â Important

 Do NOT navigate away from the page until the change order creation is complete. This ensures all change orders are created.