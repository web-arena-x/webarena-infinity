# Edit a Direct Cost

Source: https://v2.support.procore.com/product-manuals/direct-costs-project/tutorials/edit-a-direct-cost

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

1. Navigate to the project's **Direct Costs** tool.
2. Click **Summary** or **Summary by Cost Code**.
3. Locate the direct cost that you want to edit in the list.
4. Click **Edit**.
5. Under **General Information**, edit the direct cost as follows: 
   *Note*: The **Type** field cannot be edited after you create a Direct Cost. See [Create a Direct Cost](/product-manuals/direct-costs-project/tutorials/create-a-direct-cost).

   1. **Date**Choose the date you want to apply to the direct cost from the calendar control.
   2. **Status**Select *Draft*, *Pending*, *Revise and Resubmit*, or *Approved*. 
      *Notes*:

      - If you set the direct cost to any status other than *Draft*, the direct costâs line item amount is automatically populated as a value in the 'Direct Cost' column of the projectâs budget.
      - For *Approved* direct costs, Procore also automatically adds any direct cost line items with a matching [budget code](/glossary-of-terms) onto the appropriate owner invoice's [Schedule of Values](/glossary-of-terms) (SOV). See [Create Owner Invoices](/product-manuals/prime-contracts-project/tutorials/create-owner-invoices).
   3. **Vendor**Select a vendor from the drop-down list. 
      *Notes*:

      - The selections in this list are populated from the Company Directory (and NOT the Project Directory).
      - This field is only when 'Invoice' is selected.
   4. **Employee**Select the employee that reported the direct cost.
   5. **Terms**Enter any terms for the seller. You can either select one of the options from the drop-down or create your own by entering text into the Terms text box. 
      *Note*: This drop-down requires a supported web browser. See [Which web browsers are supported by Procore?](/faq-which-web-browsers-are-supported-by-procore)
   6. **Description**Enter in a more detailed description of the direct cost.
   7. **Received Date**Enter a date the direct cost was received. 
      *Note*: The received date must fall within the start and end date of the billing period.
   8. **Paid Date**Enter a date the direct cost was paid.
   9. **Attachments**Add an attachment, such as a digital copy of an invoice, bill, or receipt for the direct cost.
6. Edit an existing line item by clicking a cell and modifying it inline.
7. Add a line item choosing one of these options:

   - Click the **Add Line** button. 
     OR
   - Click vertical ellipsis (â®) and choose **Add Above** or **Add Below** from the shortcut menu.
8. Delete a line item by clicking the vertical ellipsis (â®) and choosing **Delete** from the shortcut menu.
9. Save your edits as follows:

   - Click **Save** to save the update.   
     OR
   - Click **Save & Create New** to save the update and continue adding line items.