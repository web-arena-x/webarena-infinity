# Request a Punch List Import

Source: https://v2.support.procore.com/product-manuals/punch-list-project/tutorials/request-a-punch-list-import

---

##### IMPORTANT!

In order to protect the integrity of your companyâs data, Procore Employees are restricted from modifying the data that clients submit in all Procore Import Templates. This restriction applies to all data modifications, including correcting typographical errors. If Procore determines that errors are present in any Procore Import Template that you submit to Procore, it will be returned to you for correction. **Please note that the import process may take up to 72 hours to process.**

## Background

You can import punch list items in bulk for use on a new project.

## Things to Consider

- **Required User Permissions:**

  - 'Admin' level permission on the project's Punch List tool.
  - 'Admin' level permission on the Project level Admin tool.
- **Additional Information:**

  - You can expedite the import process by performing your own punch list import using the Procore Imports app. See [Import Punch List Items into your Project Level Punch List Tool (Procore Imports)](/product-manuals/procore-imports/tutorials/import-punch-list-items-into-your-project-level-punch-list-tool-procore-imports) for more information.

## Prerequisites

- **Users:**  
   Any users added to the applicable fields in the template must already exist in your company's or the project's Directory tool. See [Import Users & Vendors into your Company Level Directory Tool (Procore Imports)](/product-manuals/procore-imports/tutorials/import-users-vendors-into-your-company-level-directory-tool-procore-imports) and [Import Users & Vendors into your Project Level Directory Tool (Procore Imports)](/product-manuals/procore-imports/tutorials/import-users-vendors-into-your-project-level-directory-tool-procore-imports), or [Add a User Account to the Company Directory](/product-manuals/directory-company/tutorials/add-a-user-account-to-the-company-directory) and [Add a User Account to the Project Directory](/product-manuals/directory-project/tutorials/add-user-account-to-project-directory).
- **Locations:**  
   If your project is using single-tier locations, you can either create new a new location to the Admin tool during the import process or you can associate a punch list item with an existing location during the import process. See [Add Office Locations](/product-manuals/admin-company/tutorials/add-an-office-location).  
   OR  
   If your project is using multi-tiered locations, the tiers must already exist in Procore in order to associate a punch list item with the location. See [Import Locations to your Project Admin Tool](/product-manuals/procore-imports/tutorials/import-locations-into-your-project-level-admin-tool-procore-imports).
- **Punch List** **Types:**  
   If you will be specifying 'Punch Item Type' valueâs, ensure the types have been added to your project's Punch List tool. See [Configure Advanced Settings: Punch List](/product-manuals/punch-list-project/tutorials/configure-advanced-settings-punch-list).

## Steps

1. Download the Punch List Import Template
2. Format the Punch List Import Template
3. Validate the Import

### Download the Punch List Import Template

1. Download the Punch List Import Template: [import-punch-list.xlsx](https://support.procore.com/Media%5FLibrary/Language%5FSpecific%5FMedia/import-punchlist-items.xlsx)

### Format the Punch List Import Template

1. Complete the import template.
2. Suggestions to help expedite your submittal import:

   - Required Column Data:

     - ***Important!*** To avoid import errors, do not add empty rows, do NOT add blank columns, do NOT add new data columns, and do not delete the header row from the contact import template.
     - The first line of the table must include the *header*, which defines the fields in the Excel table and your company's contact database in Procore.
     - The import process will fail if you modify values in column headers.

       - The import process will fail if you insert new columns, move columns, or remove columns from the template.
       - The import process will fail if you change the column header order in the template.
   - Required Row Data:

     - ***Important!*** There is no limit to the number of rows you can import. However, rows cannot be blank.
     - Each row in the table corresponds to a punch list item. At a minimum, each record requires a value for the Item Name. Other columns and cells in a single row may be left blank.
     - Each row in the table corresponds to a Punch List line item.
   - Maximum File Size: The maximum file size for a Punch List import is 1 MB.
3. See below for considerations when filling out the template.   
   *Note:* An asterisk (**\***) indicates a required field.

   - **Item Name\***  
      Enter a descriptive title for the punch list item. You can enter up to 255 alphanumeric characters. This is a required field.
   - **Punch Item #\***  
      Enter a numeric value in this box for each data row. Values in the column are commonly entered in ascending numeric order (for example, 1, 2, 3, and so on). Duplicate values are allowed. However, this field cannot be blank.
   - **Punch Item Type**  
      Enter one item type to categorize the punch list item (for example, Electrical, Instrumentation, or Mechanical). For a successful import, types must be added to the Punch List tool before the import process, see [Configure Advanced Settings: Punch List: Add Punch Item Types](/product-manuals/punch-list-project/tutorials/configure-advanced-settings-punch-list).
   - **Due Date**  
      Enter the date the punch list item must be completed using the MM/DD/YYYY format (for example, 06/01/2016).  
     ***Important!*** Do NOT enter dates in the M/D/YYYY format (for example, do NOT enter 6/1/2016) or the import will fail.  
     *Note*: If the Excel column is not permitting you to add a leading zero, select the entire column, choose Format > Cells and then create a 'Custom' Number Format named 'mm/dd/yyyy' in the Number tab. See [Create or Delete a Custom Number Format in Excel](https://support.office.com/en-us/article/Create-or-delete-a-custom-number-format-78f2a361-936b-4c03-8772-09fab54be7f4).
   - **Trade**  
      Enter the trade name exactly as it appears in the Company level Admin tool. See [Add or Delete Trade Names](/product-manuals/admin-company/tutorials/add-a-custom-trade). Use the pipe (|) symbol as a separator to include multiple trade names (for example, Concrete | Masonry).
   - **Location**  
      Enter the location exactly as you want it to appear in Procore.  
     ***Important!*** If your project is using multi-tiered locations, you must enter the location exactly as it appears in Procore and separate each tier with the greater than (>) symbol and no SPACES between tiers (for example, Lot 1>Section A).
   - **Cost Code**  
      Associate a cost code with a punch list item. The cost code must be formatted "division - cost code" written with the exact amount of digits as listed in your project or company in Procore. See [Add Company Cost Codes](/process-guides/company-administration-work-breakdown-structure-guide/add-company-cost-codes).
   - **Schedule Impact**  
      Enter one of the following values for each punch list item. Any entry other than the ones below will result in a blank entry after the import:

     - **tbd**. Enter this if the impact to the schedule is currently being assessed. This is short for 'To Be Determined'.
     - **n\_a**. Enter this value to leave the field blank.
     - **no\_impact**. Indicates the punch list item has no impact to on the project schedule.
     - **yes\_unknown**. Indicates the punch list item will impact the project schedule, but the impact is not known.
     - **yes\_known**. Indicates the punch list item impacts the project schedule and the number of days by which the project schedule will be impacted is known. If you enter this value, you must enter a number of days in the 'Schedule Impact Days' field.
   - â**Schedule Impact Days**  
      If you entered 'yes\_known' in the 'Schedule Impact' field, enter a number of days by which the project schedule will be impacted (for example, 7 or 14).
   - **Cost Impact**  
      Enter in one of the following values as it applies to each punch list item. Any entry other than these will cause the field to be left blank.

     - If the cost impact is "to be determined," enter "**tbd**"\* To leave the field blank intentionally, enter "**n\_a**"\* If there is not an impact to the schedule, enter "**no\_impact**"
     - If there is an impact on the cost, and the amount of time is not known, enter "**yes\_unknown**"
     - If there is an impact on the cost due to the punch list item, and the cost amount is known, enter "**yes\_known**"
   - **Cost Impact Amount**  
      If you entered 'yes\_known' in the 'Cost Impact' field, enter the dollar amount here. Do NOT include the dollar sign ($) symbol.
   - **Priority**  
      Enter 'Low' 'Medium', or 'High' to indicate the priority of the punch list item.  
     \_**Important!**\_This entry is case-sensitive and must use the initial case (for example, the first letter of the value is capitalized). If this format is not used, the field will be blank after the import.
   - **Reference**  
      Enter a relevant keyword or phrase to use as an item reference. This is a free-form text field to be used as specified by your organization. For example, if the item was created at the client's request, enter "client request".
   - **Created** **By\*  
      â**Enter the full email address of the user who created the punch list item. Always enter the email address exactly as it appears in the Project Directory.  
     ***Important!*** Do NOT enter a user name in this field. You must enter an email address. The person must already be added or imported to the Project Directory. This user must also be granted 'Admin' level permissions or higher to the Punch List tool.
   - **Punch Item Manager\***   
      Enter the full email address of the user who will serve as the Punch Item Manager. Always enter the email address exactly as it appears in the Project Directory.  
     ***Important!*** Do NOT enter a user name in this field. You must enter an email address. The person must already be added or imported to the Project Directory. This user must also be granted 'Admin' level permissions or higher to the Punch List tool. This user must also be granted 'Admin' level permissions or higher to the Punch List tool, or a 'Standard' user and granted special permission to act as Punch Item Manager.
   - **Final Approver\***  
      Enter the full email address of the user who will serve as the Final Approver. Always enter the email address exactly as it appears in the Project Directory.  
     ***Important!*** Do NOT enter a user name in this field. You must enter an email address. The person must already be added or imported to the Project Directory. This user must also be granted 'Admin' level permissions or higher to the Punch List tool, or a 'Standard' user and granted special permission to act as Final Approver.
   - **Description**  
      Enter additional descriptive information related to completing the punch list item. You can enter up to 255 alphanumeric characters.
   - **Assigned To**  
      Enter the full email address of the person who is responsible for closing out the punch list item.  
     ***Important!*** Do NOT enter a user name in this field. You must enter an email address. The person must already be added or imported to the Project Directory. This user must also be granted 'Standard' level permissions or higher to the Punch List tool and will be automatically designated as the [Ball In Court](/glossary-of-terms) person for the punch list item.  
     ***Important!*** You can add multiple assignees to this field, but each email MUST be separated by the pipe ("|") symbol.
   - **Comments**  
      Enter in additional comments you may have on the punch list item. You can enter up to 255 alphanumeric characters.
4. Send the completed template to your Procore point of contact  or to [imports@procore.com](mailto:imports@procore.com).

### Validate the Import

After you are notified that the import is complete, do the following:

1. Navigate to the project's **Punch List** tool.
2. Validate that the imported punch list items are displaying as expected.