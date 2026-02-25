# Record Changes to Production Quantities on a Potential Change Order for a Prime Contract

Source: https://v2.support.procore.com/product-manuals/prime-contracts-project/tutorials/record-changes-to-production-quantities-on-a-potential-change-order-for-a-prime-contract

---

## Background

For companies using Procore's Project Financials and Resource Management tools with the 'Procore Labor Productivity Cost' budget view, you can log additional production quantities associated with a Prime Potential Change Order (PCO) in the 'Production Quantities' tab on the project's Prime Contract's tool.

## Things to Consider

- **Required User Permissions:**

  - 'Admin' level permissions on the project's **Prime Contracts** tool.

## Prerequisites

For production quantities to interact with the labor productivity tracking feature, you must:

- [Set Up the Procore Labor Productivity Cost Budget View](/process-guides/resource-tracking-and-project-financials-setup-guide/preview-the-budget-view)
- [Set Up a Field Production Report](/product-manuals/timesheets-project/tutorials/set-up-a-field-production-report)

## Steps

1. Navigate to the project's **Prime Contracts** tool.
2. Locate the Prime Potential Change Order (Prime PCO) to work with.
3. Ensure that all of the line items that should be associated with the change event have been added.
4. Click the **Production Quantities** tab.
5. Click **Edit**.
6. Click **Add Line**.

   - **Cost Code**  
     Select the cost code that corresponds to the production quantity change.
   - **Description**  
     Enter a description for the line item.
   - **Unit Qty**  
     Enter a numeric value in this box to indicate the number of units that correspond to the unit of measurement that you specify. Always enter the amount that represents the change to the production quantity.
   - **Unit of Measure (UOM)**  
     Select a unit of measure from the drop-down list. To learn about the default selections in this list, see [Which units of measure are included in Procore's master list?](/faq-which-units-of-measure-are-included-in-procores-master-list) and [Add a Unit of Measure to the Unit of Measure Master List](/product-manuals/admin-company/tutorials/update-a-unit-of-measure-on-the-unit-of-measure-master-list).
7. Click **Save**.

## Next Steps

- [Create a Prime Contract Change Order](/product-manuals/prime-contracts-project/tutorials/create-a-prime-contract-change-order)