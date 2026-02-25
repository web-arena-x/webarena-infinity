# Create a New Expense Allocation

Source: https://v2.support.procore.com/product-manuals/admin-company/tutorials/create-a-new-expense-allocation

---

## Background

Procore has designed a new Expense Allocations feature in the Company level Admin tool to provide General Contractors a statement of cost allocation for the project level. This provides GCs with the ability to bill Procore costs to the owner. As a GC, the costs for your Procore technology investment may be reimbursable. This feature creates the necessary statement of allocation to ensure that you have the proper PDF documentation to recover the cost of your Procore investment.

To use this feature you will need to select the active project to allocate and complete three (3) fields relevant to that project:

1. Estimated Start Date
2. Estimated End Date
3. Estimated Contract Value

Based on this information, Procore will generate a statement of cost allocation by multiplying your Basis Points pricing rate on the Date of Allocation by the Contract Value. Procore then generates this statement as a PDF, which you can submit to the owner for reimbursement and keep for your records.

It is important to note that the total amount of cost allocated cannot exceed the cost of your annual Procore license.

### Things to Consider

- **Required User Permissions**:

 - 'Admin' on the company's Admin tool
- **Requirements**:

 - Users must enter data in ALL fields.
 - Users are limited to creating one (1) expense allocation per Procore project per one (1) year billing period.
 - An expense allocation cannot span multiple billing periods.
- **Limitations**:

 - You can only create one (1) expense allocation per project.
 - Users cannot delete an expense allocation.
- **Additional Information**:

 - The term expense allocation represents the billing period for your company's Procore account. If you have specific questions about your company's costs for Procore during the duration of a project, it is recommended that you contact your Procore point of contact .
 - The billing period for an expense allocation has NO relationship to the billing periods on your project.
 - ***IMPORTANT!*** An expense allocation cannot be back dated.
 - You can create a new expense allocation on any date within a one (1) year billing period. However, you cannot create a expense allocation that spans multiple Procore billing periods.
 - The Actual Contract Value (ACV) of your Procore Contract is used to calculate the total for the owner on the expense allocation. If your company's ACV changes during a billing period and you create a new expense allocation, the new ACV will always be used to calculate the bill amount.
 - Expense allocations for multi-year Procore contracts are NOT supported.

## Steps

1. Navigate to the Company level **Admin** tool.
2. Under **Company Settings**, click **Expense Allocations**.
3. Click **New Expense Allocation.**
4. Complete the following required fields:

   - **Project**. Select the desired project from the list. Only active Procore projects will appear in this list.

     - If you select an active project with an existing expense allocation, the 'Project has already been taken' error message appears.
     - You can create only one (1) expense allocation for a project during the one (1) year billing period. For example, if your company has a single-year Procore contract that started on January 1, 2025, you could create up to one (1) expense allocation on or before December 31, 2025. If your company has a multi-year Procore contract that started on January 1, 2025, the first billing period would end on December 30, 2025. The second year's billing period would start on January 1, 2026 and end on December 31, 2026.
   - **Estimated Contract Value**. Enter the estimated original contract value.   
     *Note*: This value should match the amount entered in the Project level **Admin** tool's **Estimated Project Value** field on the **General** page.
   - **Estimated Start Date**. Enter the estimated project start date.

     - This date should match the date entered in the Project level **Admin** tool's **Estimated Start Date** field on the **General** page.
     - This date must be within your company's current billing period start and end date in your Procore contract.
   - **Estimated End Date**. Enter the estimated project end date.   
     *Note*: This date should match the date entered in the Project level **Admin** tool's **Estimated End Date** field on the **General** page.
5. Click **Create**. 
   Note: Click the **PDF icon** next to the expense allocation item to download or export a copy. Basis points will **not** appear in the generated PDF.