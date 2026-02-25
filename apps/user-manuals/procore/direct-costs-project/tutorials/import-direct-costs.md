# Import Direct Costs

Source: https://v2.support.procore.com/product-manuals/direct-costs-project/tutorials/import-direct-costs

---

## Things to Consider

- **Required User Permissions:**

 - 'Admin' level permissions on the project's Direct Costs tool.
 - 'Standard' level permissions on the project's Direct Costs tool with the ['Create Direct Cost' granular permission](/product-manuals/permissions-company/tutorials/grant-granular-permissions-in-a-project-permissions-template) enabled on your permissions template.
- **Import Template Requirements:**
- For general considerations, see [How do I prepare my data for import into Procore?](/product-manuals/procore-imports/tutorials/prepare-your-data-for-import-into-procore)

 - Enter data in the completed template in the XLSX format. Then save the file to the CSV format.
- **Required Column Data:**

 - ***Important!*** To avoid import errors, do not add empty rows, do NOT add blank columns, do NOT add new data columns, and do not delete the header row to the import template.
 - The first line of the table must include the *header*, which defines the fields in the Excel table and the database in Procore.

    - The following headers are required: Type, Invoice #, Description, Employee Email, Status, Terms, Date, Received Date, Paid Date, Vendor, and Cost Code.
 - The import process will fail if you modify values in column headers.
 - The import process will fail if you insert new columns, move columns, or remove columns from the template.
 - The import process will fail if you change the column header order in the template.
- **Required Row Data:**

 ##### Â Important

 To import a direct cost line item, the following fields are required: Type, Status, Cost Code, and Cost type.

- There is no limit to the number of rows you can import.
- You **MUST** enter the appropriate cost type abbreviation. For example, enter 'L' for 'Labor', 'E' for 'Equipment', 'M' for 'Materials', 'S' for 'Commitment', 'OC' for 'Owner Cost', 'SVC' for 'Professional Services', or 'O' for 'Other') for Cost Type. This entry is case-sensitive.
- Each row in the table corresponds to a direct cost line item. At a minimum, each record requires a Type value. If you enter 'Invoice' in the Type cell, the Vendor and Invoice Number values are required.
- Other columns and cells in a single row may be left blank.

- **Supported Date Formats:**

 - Date entries MUST be entered using the required format. For details, see [Which date formats are supported when importing direct costs from a CSV file?](/faq-which-date-formats-are-supported-when-importing-direct-costs-from-a-csv-file)
- **Limitations:**

 - Budget Codes

    - The direct costs import template and process does NOT support budget codes (see [What is a budget code in Procore's WBS?](/faq-what-is-a-budget-code-in-procores-wbs)). Instead, you must enter the appropriate [cost code](/glossary-of-terms), [cost type](/glossary-of-terms), and [sub job](/glossary-of-terms) combination for your direct cost line items directly in the import template.
 - Sub Jobs:

    - If your company has enabled the sub job feature for the optional ERP Integrations tool (see [Add a {{integrations\_Sage300CRE}} Extra to a Procore Project as a Sub Job](https://support.procore.com/tc/procore/Legacy/ERP%5FArchives/Legacy-Sage300CRE-Tutorials/add-a-sage-300-cre-extra-to-a-procore-project-as-a-sub-job)) or if you have added sub jobs in the Admin tool (see [Add 'Sub Job' Segment Items to a Procore Project](/process-guides/project-administration-work-breakdown-structure-guide/add-sub-jobs-to-a-project)), you will not be able to add sub jobs via the import process.
- **Additional Information:**

 - If you need assistance with the import process, send an email request to: [support@procore.com](mailto:support@procore.com)

## Prerequisites

- **Users:**

 - If you will be associating a direct cost with a Procore user in the 'Employee Email' field, ensure that the users have been added to the Company or Project Directory. For the Company Directory, see [Add a User Account to the Company Directory](/product-manuals/directory-company/tutorials/add-a-user-account-to-the-company-directory) or [Import Users & Vendors into your Company Level Directory Tool (Procore Imports)](/product-manuals/procore-imports/tutorials/import-users-vendors-into-your-company-level-directory-tool-procore-imports). For the Project Directory, see [Add a User Account to the Project Directory](/product-manuals/directory-project/tutorials/add-user-account-to-project-directory) or [Import Users & Vendors into your Project Level Directory Tool (Procore Imports)](/product-manuals/procore-imports/tutorials/import-users-vendors-into-your-project-level-directory-tool-procore-imports).
- **Vendors:**

 - If you will be assigning a vendor/company as the 'Vendor' for the direct cost, ensure that the vendor/company has been added to the Company or Project Directory. For the Company Directory, see [Add a Company to the Company Directory](/product-manuals/directory-company/tutorials/add-a-company-to-the-company-directory) or [Import Users & Vendors into your Company Level Directory Tool (Procore Imports)](/product-manuals/procore-imports/tutorials/import-users-vendors-into-your-company-level-directory-tool-procore-imports). For the Project Directory, see [Add a Company to the Project Directory](/process-guides/set-up-a-project-directory/create-companies) or [Import Users & Vendors into your Project Level Directory Tool (Procore Imports)](/product-manuals/procore-imports/tutorials/import-users-vendors-into-your-project-level-directory-tool-procore-imports).
- **Cost Codes:**

 - Your cost codes must exist in the 'Cost Code' segment in Procore's [Work Breakdown Structure](https://support.procore.com/products/online/work-breakdown-structure).
 - If your company has enabled the company's ERP Integrations tool, the [integrated ERP system](/glossary-of-terms) must be synced with Procore and each cost code must be assigned to a cost type.

*Note:* If your company is using Sage 300 CREÂ®, see [Add {{integrations\_Sage300CRE}} Standard Cost Codes to a Project](https://support.procore.com/integrations/sage-300-cre/tutorials/add-sage-300-cre-standard-cost-codes-to-a-project) and [Assign Default Cost Types To Cost Codes](https://support.procore.com/tc/procore/Legacy/ERP%5FArchives/Legacy%5FGeneral%5FERP%5FTutorials/assign-default-cost-types-to-cost-codes).

## Steps

#### Step 1: Download the Direct Costs Import Template

1. Navigate to the project's **Direct Costs** tool.
2. Click one of the available tabs:

   - **Summary**
   - **Summary by Cost Code**
3. Click **Create**. Then choose **Import Direct Costs** from the shortcut menu.
4. In the Import Direct Costs window, choose the delimiter for the file:

   ##### Â Tip

   **What is a delimiter?** A *delimiter* is a character used to separate values or text strings. It marks both the beginning and end of a unit of data.

- **Comma**. Separates data using a comma (,). This is Procore's default option.
- **Semicolon**. Separates data using a semicolon (;).

- Click the **Download Direct Costs Import Template** link.

This downloads a CSV file that you must use as an import template.

#### Step 2: Complete the Direct Costs Import Template

1. Open the CSV file in Microsoft Excel.
2. Complete the data entry as follows: 
   *Note*: An asterisk (\*) below denotes a required field.

   - **Type**Enter 'Invoice,' 'Expense', or 'Payroll'. This is a required field.

     ##### Â Important

     - If you enter a value other than 'Invoice,' 'Expense', or 'Payroll', the import will fail.
     - The first letter of the entry in the 'Type' cell must always be capitalized.
     - The entry in the 'Type' cell is case-sensitive.