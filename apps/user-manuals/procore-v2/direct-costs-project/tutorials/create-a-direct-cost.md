# Create a Direct Cost

Source: https://v2.support.procore.com/product-manuals/direct-costs-project/tutorials/create-a-direct-cost

---

## Background

In Procore, the term *direct cost* is used to refer to a cost on a construction project that is NOT associated with a [purchase order](/glossary-of-terms) or [subcontract](/glossary-of-terms). Using the Direct Costs tool, you can create these items:

- **Invoices**. Create a direct cost for a paper invoice from a non-contracted vendor for items such as printer ink, computer paper, or postage.
- **Expenses**. Create a direct cost expense for computer equipment, telephones, or internal equipment rentals.
- **Payroll**. Create a direct cost for monthly payroll costs classified by cost code, so that payroll amounts reflect each month on the budget.

Once you change the status of a direct cost from *Draft* to either *Pending*, *Revise and Resubmit*, or *Approved*, the project's Budget tool automatically displays the amount of the direct cost in the 'Direct Costs' column on its corresponding budget line item. For 'Approved' direct costs, Procore also automatically adds any direct cost line items with a matching [budget code](/glossary-of-terms) onto the appropriate owner invoice's [Schedule of Values](/glossary-of-terms) (SOV). See [Create Owner Invoices](/product-manuals/prime-contracts-project/tutorials/create-owner-invoices).

## Things to Consider

- **Required User Permissions:**

 - 'Admin' level permissions on the project's Direct Costs tool OR
 - 'Read Only' or 'Standard' level permissions on the project's Direct Costs tool with the ['Create Direct Cost' granular permission](/product-manuals/permissions-company/tutorials/grant-granular-permissions-in-a-project-permissions-template) enabled on your permission template.
- Considerations:

 - If you would prefer to import your direct cost line items using a Comma Separated Values (CSV) file, see [Import Direct Costs](/product-manuals/direct-costs-project/tutorials/import-direct-costs).

## Prerequisites

- Add the Direct Costs tool to the project. See [Enable the Direct Costs Tool](/product-manuals/direct-costs-project/tutorials/enable-the-direct-costs-tool).
- Add the vendor associated with the direct cost to the Company Directory. See [Add a Company to the Company Directory](/product-manuals/directory-company/tutorials/add-a-company-to-the-company-directory). 
 *Note*: Vendors do NOT need to be added to the Project Directory to be associated with a direct cost.

## Steps

- Add a New Direct Cost
- Add a Line Item to a Direct Cost

### Add a New Direct Cost

1. Navigate to the project's **Direct Costs** tool.
2. Click **Create**. Then select **Create Direct Cost** from the drop-down menu.
3. Under **General Information**, do the following:

   1. **Type**Select *Expense*, *Invoice*, or *Payroll* from the drop-down list.
   2. **Date**Choose the date you want to apply to the direct cost from the calendar control.
   3. **Status**Select *Draft*, *Pending*, *Revise and Resubmit*, or *Approved*. 
      *Note*: If you set the direct cost to any status other than *Draft*, the direct costâs line item amount is automatically populated as a value in the 'Direct Cost' column of the projectâs budget.
   4. **Vendor**Select a vendor from the drop-down list. 
      *Notes*:

      - The selections in this list are populated from the Company Directory (and NOT the Project Directory).
      - This field is only required when 'Invoice' is selected.
   5. **Employee**Select the employee that reported the direct cost.
   6. **Terms**Enter any terms for the seller. You can either select one of the options from the drop-down or create your own by entering text into the Terms text box. 
      *Note*: This drop-down requires a supported web browser. See [Which web browsers are supported by Procore?](/faq-which-web-browsers-are-supported-by-procore)
   7. **Description**Enter in a more detailed description of the direct cost.
   8. **Received Date**Enter a date the direct cost was received. 
      *Note*: The received date must fall within the start and end date of the billing period.
   9. **Paid Date**Enter a date the direct cost was paid.
   10. **Attachments**Add an attachment, such as a digital copy of an invoice, bill, or receipt for the direct cost.
4. If you want to add new line items for the direct cost, see the next steps below.

### Add a Line Item to a Direct Cost

While editing the direct cost that you want to add the line item to, do the following:

1. Click **Add Line**.
2. Complete the data entry as follows:

   - **Budget Code**Select a budget code from the list or click **Create Budget Code** to create a new one. See [What](/faq-what-is-a-budget-code-in-procores-wbs) [is a budget code in Procore's WBS?](/faq-what-is-a-budget-code-in-procores-wbs)
   - **Autocalculate vs. Override Amount**Click the icon in the column until the calculation method you want to use is active:\* If you want Procore to consider your *Qty*, *UOM*, and *Unit Cost* entries to automatically calculate the 'Amount', click the column until a calculator icon appears.\* If you want to manually override the automatic calculation and enter the amount, click the column until the icon with the exclamation point appears.
   - **Description**Enter a description for the line item.
   - **Qty**Enter in the quantity of units.
   - **UOM**Select the **Unit of Measure (UOM)** from the drop-down list. See [Which units of measure are included on Procore's master list?](/faq-which-units-of-measure-are-included-in-procores-master-list) and [Add a Unit of Measure to the Unit of Measure Master List](/product-manuals/admin-company/tutorials/update-a-unit-of-measure-on-the-unit-of-measure-master-list).
   - **Unit Cost**Enter the unit cost in the box provided.
   - **Amount**The system automatically calculates the subtotal for you, based on the *Qty*, *UOM*, and *Unit Cost* entries.
3. Choose one of these options:

   - **Save**. Click this button to save the line item.
   - **Save & Create New**. Click this button to save the line item and create a new one.

##### Â Note

After you change the status of a direct cost from *Draft* to any other status (i.e., *Pending*, *Revise and Resubmit*, or *Approved),* Procore matches the division, cost code, and cost type for the budget code of the direct cost and updates these Procore tools as appropriate:

- **Budget Tool**Adds the direct cost as a line item on the project's budget. The direct cost 'Amount' shows on the budget line item in the 'Direct Costs' column. If the budget code's cost code and cost type are not budgeted, Procore highlights the line item in RED so you can add it to the budget. See [Add a Partial Budget Line Item](/product-manuals/budget-project/tutorials/add-a-partial-budget-line-item).
- **Invoicing Tool**Adds the direct cost as a line item on an owner invoice's Schedule of Values (SOV) if the direct cost's 'Received Date' occurs within the owner invoice's billing period. See [Create Owner Invoices](/product-manuals/prime-contracts-project/tutorials/create-owner-invoices).

**Prime Contracts Tool** Adds the direct cost as a line item on an owner invoice's Schedule of Values (SOV) if the direct cost's 'Received Date' occurs within the owner invoice's billing period. See [Create Owner Invoices](/product-manuals/prime-contracts-project/tutorials/create-owner-invoices).