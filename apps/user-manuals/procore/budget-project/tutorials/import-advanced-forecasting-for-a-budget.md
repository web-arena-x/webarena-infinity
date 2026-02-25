# Import Advanced Forecasting for a Budget

Source: https://v2.support.procore.com/product-manuals/budget-project/tutorials/import-advanced-forecasting-for-a-budget

---

## Background

When setting up your budget in a new Procore project, you have the option to add the line items manually (see [Add a Budget Line Item](/product-manuals/budget-project/tutorials/add-a-budget-line-item)) or use the steps below to import your data.

## Things to Consider

- **Required User Permissions:**

 - 'Admin' level permissions on the project's Budget tool. 
     OR
 - 'Read Only' or 'Standard' level permissions on the project's Budget tool with the ['Import Budget From File' and 'Create and Edit Original Budget Amount' granular permissions](/product-manuals/permissions-company/tutorials/grant-granular-permissions-in-a-project-permissions-template) enabled on your permissions template.

    ##### Â Notes

    - If a user with 'Read Only' or 'Standard' permissions has only the 'Import Budget From File' granular permission enabled, they can only import a budget. They cannot manually create or edit the budget.
    - If a user with 'Read Only' or 'Standard' permissions have only the 'Create and Edit Original Budget Amount' granular permission enabled, they can only manually create or edit a budget. They cannot import a budget.

- **Supported Import File Type:**

 - XLSX
- **Additional Information:**

 - To create new line items, the import file must contain data in the following columns:\* Cost Code\* Cost Type\* Manual Calculation
 - To import multiple line items with the same cost code, each item MUST have a different cost type assignment. For example:\* 02-300 - Earthwork, M, $30,000\* 02-300 - Earthwork, L, $10,500
 - Do NOT edit, update, or change data in the 'Importer Data Fields' worksheet of the import template. This worksheet is for reference only and shows the options are available for selection in the drop-down lists on the 'Budget Line Items' tab. These options reflect what options were available for selection on your Procore project at the time you downloaded the import template.
- **Limitations:**

 - Exported Procore Budget files are NOT supported. CSV and PDF export files contain additional data columns and cannot be used to re-import a budget.
 - **Budget Codes**\* The import template does NOT contain a 'Budget Code' column. Instead, Procore automatically create budget codes on your project when you enter the [cost code](/glossary-of-terms), [cost type](/glossary-of-terms), and [sub job](/glossary-of-terms) (if enabled) combination on your line items in the import template. To learn more about budget codes, see [What is a budget code in Procore's WBS?](/faq-what-is-a-budget-code-in-procores-wbs)\* In order to import data into Procore, the database requires the presence of a 'Description' column in the import template. You can leave this field blank to use the default concatenated description in your company's Work Breakdown Structure or you can input a description to import a custom description. To learn more about the Description field, see [Edit Budget Code Descriptions on a Project](/product-manuals/admin-project/tutorials/edit-budget-code-descriptions-on-a-project).
 - The maximum number of line items allowed for an individual budget import is 500.

##### Â Tip

To avoid overwriting the values in a project's budget, Procore recommends importing your budget once. If you want to import a new version of your budget, you may. However, it's important to keep these points in mind:

- Any line items added to your original import will be added.
- All changes to the 'Budget Amount' values on existing line items are overwritten.
- If you want to preserve 'Budget Amount' values, make sure the values in the updated import file match the original import file before importing it into Procore.

For assistance with an import, email: [support@procore.com](mailto:support@procore.com)