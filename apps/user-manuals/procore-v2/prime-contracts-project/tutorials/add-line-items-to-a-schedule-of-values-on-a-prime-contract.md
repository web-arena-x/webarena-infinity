# Add Line Items to a Schedule of Values on a Prime Contract

Source: https://v2.support.procore.com/product-manuals/prime-contracts-project/tutorials/add-line-items-to-a-schedule-of-values-on-a-prime-contract

---

## Background

An SOV is an itemized list of all the work items on a project. Each line item shows the work item's cost.

## Things to Consider

- **Required User Permissions:**

  - 'Admin' level permissions on the project's **Prime Contracts** tool.  
    *Note*: To limit subcontractors (and other users in other roles) from viewing your contract data, configure the granular permissions feature when applying permission templates. See [Edit a Project Permissions Template](/product-manuals/permissions-company/tutorials/edit-a-project-permissions-template).
- **Additional Information:**

  - Other methods for adding SOV line items to a contract include:

    - [Import a Prime Contract SOV from a CSV File](/product-manuals/prime-contracts-project/tutorials/import-a-prime-contract-sov-from-a-csv-file)
    - [Create a Prime Contract SOV from the Project Budget](/product-manuals/prime-contracts-project/tutorials/create-a-prime-contract-sov-from-the-project-budget)   
      *Note*: Not recommended for projects with multiple prime contracts. See [Are there any system limitations when creating multiple prime contracts?](/faq-are-there-any-system-limitations-when-creating-multiple-prime-contracts)

## Prerequisites

- [Create Prime Contracts](/product-manuals/prime-contracts-project/tutorials/create-prime-contracts)
- Set the accounting method on the contract. See [Edit the Advanced Settings on a Prime Contract](/product-manuals/prime-contracts-project/tutorials/edit-the-advanced-settings-on-a-prime-contract).

## Steps

1. Navigate to the project's **Prime Contracts** tool.
2. Locate the contract to update and click its **Number** link.
3. Click the **Schedule of Values** tab.
4. Click **Add Line.**
5. Complete the data entry as follows:

   1. **Budget Code**  
      Select a budget code or click **Create Budget Code**. See [What is a budget code in Procore's WBS?](/faq-what-is-a-budget-code-in-procores-wbs)
   2. **Description**  
      Enter a description for the line item. For example, type: Monthly Service Fee
   3. **Qty**  
      Enter the number of units.
   4. **UOM**  
      Select a *Unit of Measure (UOM)* from the drop-down list. To learn about the default selections in this list, see [Which units of measure are included in Procore's master list?](/faq-which-units-of-measure-are-included-in-procores-master-list) and [Add a Unit of Measure to the Unit of Measure Master List](/product-manuals/admin-company/tutorials/update-a-unit-of-measure-on-the-unit-of-measure-master-list).
   5. **Unit Cost**  
      Enter the cost per unit in this box. You'll notice that the value in this column contains four (4) decimal points (for example, $0.0000) to allow you to enter the specific value required to calculate accurate pricing.

      ##### Example

      If you are buying 50,000 units for $1,006,625.00, you would enter a unit price of $20.1325.

- **Amount**  
  The system automatically calculates the subtotal for you, based on the *Qty*, *UOM*, and *Unit Cost* entries.
- Repeat the above steps for all line items.

  ##### Â Tip

  **Want to arrange the line items on your schedule of values into groups?** Click the **Add Group** menu and select the desired grouping options. The default options include *Cost Code, Cost Type,* *Sub Job (if enabled)*, as well as any custom segments that have been added for your company or project. See [What are Segments and Segment Items](/faq-what-are-segments-and-segment-items).

- Choose one of these options:

  - Click **Save**  
    OR
  - Click **Save & Email**.