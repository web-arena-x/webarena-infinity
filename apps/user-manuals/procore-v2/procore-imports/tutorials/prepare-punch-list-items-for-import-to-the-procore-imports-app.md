# Prepare Punch List Items for Import to the Procore Imports App

Source: https://v2.support.procore.com/product-manuals/procore-imports/tutorials/prepare-punch-list-items-for-import-to-the-procore-imports-app

---

## Background

You can use the Procore Imports App to self-import a list of punch list items into your project's Punch List tool. This will add as many punch list items to your project as you need without having to manually add each punch list item in Procore.

## Things to Consider

- **Required User Permissions:**

  - 'Admin' level permissions on the project's Punch List tool.
  - 'Admin' level permissions on the Project level Admin tool.
  - 'Standard' level permissions or higher on the Project level Directory tool.

*Note:* Granular Permissions are not supported in the Procore Imports application.

## Steps

- Download the Punch List Import Template
- Format the Punch List Import Template

#### Download the Punch List Import Template

- Download the Punch List Import Template: [import-punch-list.xlsx](https://procore-imports-templates.s3.amazonaws.com/import%5Ftemplate%5Fpunchlist.xlsx)

#### Format the Punch List Import Template

##### Prerequisites

- **Users:**  
   Any users added to the applicable fields in the template must already exist in your company's or the project's Directory tool. See [Import Users & Vendors into your Company Level Directory Tool (Procore Imports)](/product-manuals/procore-imports/tutorials/import-users-vendors-into-your-company-level-directory-tool-procore-imports) and [Import Users & Vendors into your Project Level Directory Tool (Procore Imports)](/product-manuals/procore-imports/tutorials/import-users-vendors-into-your-project-level-directory-tool-procore-imports), or [Add a User Account to the Company Directory](/product-manuals/directory-company/tutorials/add-a-user-account-to-the-company-directory) and [Add a User Account to the Project Directory](/product-manuals/directory-project/tutorials/add-user-account-to-project-directory).
- **Locations:**  
   If your project is using single-tier locations, you can either create a new location to the Admin tool during the import process or you can associate a punch list item with an existing location during the import process. See [Add Office Locations](/product-manuals/admin-company/tutorials/add-an-office-location).  
   OR  
   If your project is using multi-tiered locations, the tiers must already exist in Procore in order to associate a punch list item with the location. See [Import Locations to your Project Admin Tool](/product-manuals/procore-imports/tutorials/import-locations-into-your-project-level-admin-tool-procore-imports).
- **Punch List** **Types:**  
   If you will be specifying 'Punch Item Type' valueâs, ensure the types have been added to your project's Punch List tool. See [Configure Advanced Settings: Punch List](/product-manuals/punch-list-project/tutorials/configure-advanced-settings-punch-list).

##### Steps

1. See below considerations when filling out the template.

   - Required Column Data:

     - ***Important!*** To avoid import errors, do not add empty rows, do NOT add blank columns, do NOT add new data columns, and do not delete the header row from the contact import template.
     - The first line of the table must include the *header*, which defines the fields in the Excel table and your company's contact database in Procore.
     - The following headers are required and an asterisk (**\***) denotes that data is required in the row:

       - Item Name\*
       - **Punch Item #**\*
       - **Punch Item Manager\***
       - **Created By**\*
       - Assigned To
       - Final Approver\*
       - Location
       - Trade
       - Schedule Impact
       - Schedule Impact Days
       - Cost Code
       - Punch Item Type
       - Due Date
       - Priority
       - Cost Impact
       - Cost Impact Amount
       - Reference
       - Description
       - Comments.

         - The import process will fail if you modify values in column headers.
         - The import process will fail if you insert new columns, move columns, or remove columns from the template.
         - The import process will fail if you change the column header order in the template.
   - Required Row Data:

     - ***Important!*** There is no limit to the number of rows you can import. However, rows cannot be blank.
     - Each row in the table corresponds to a punch list item. At a minimum, each record requires a value for the Item Name. Other columns and cells in a single row may be left blank.
     - Each row in the table corresponds to a Punch List line item.
   - Maximum File Size:

     - The maximum file size for a Punch List import is 1 MB.
2. Complete the import template.   
   *Note:* An asterisk (**\***) indicates a required field.

   - **Item Name\***  
      Enter a descriptive title for the punch list item. You can enter up to 255 alphanumeric characters. This is a required field.
   - **Punch Item Number\***  
      Enter a numeric value in this box for each data row. Values in the column are commonly entered in ascending numeric order (e.g., 1, 2, 3, and so on). Duplicate values are allowed. However, this field cannot be blank.
   - **Punch Item Manager\***   
      Enter the full email address of the user who will serve as the Punch Item Manager. Always enter the email address exactly as it appears in the Project Directory.  
     ***Important!*** Do NOT enter a user name in this field. You must enter an email address. The person must already be added or imported to the Project Directory. This user must also be granted 'Admin' level permissions or higher to the Punch List tool. This user must also be granted 'Admin' level permissions or higher to the Punch List tool, or a 'Standard' user and granted special permission to act as Punch Item Manager.
   - **Created** **By\*  
      â**Enter the full email address of the user who created the punch list item. Always enter the email address exactly as it appears in the Project Directory.  
     ***Important!*** Do NOT enter a user name in this field. You must enter an email address. The person must already be added or imported to the Project Directory. This user must also be granted 'Admin' level permissions or higher to the Punch List tool.
   - **Assigned To**  
      Enter the full email address of the person who is responsible for closing out the punch list item.  
     ***Important!*** Do NOT enter a user name in this field. You must enter an email address. The person must already be added or imported to the Project Directory. This user must also be granted 'Standard' level permissions or higher to the Punch List tool and will be automatically designated as the [Ball In Court](/glossary-of-terms) person for the punch list item.  
     ***Important!*** You can add multiple assignees to this field, but each email MUST be separated by the pipe ("|") symbol.
   - **Final Approver\***  
      Enter the full email address of the user who will serve as the Final Approver. Always enter the email address exactly as it appears in the Project Directory.  
     ***Important!*** Do NOT enter a user name in this field. You must enter an email address. The person must already be added or imported to the Project Directory. This user must also be granted 'Admin' level permissions or higher to the Punch List tool, or a 'Standard' user and granted special permission to act as Final Approver.
   - **Location**  
      Enter the location exactly as you want it to appear in Procore.  
     ***I*** ***mportant*** ***!*** If your project is using multi-tiered locations, you must enter the location exactly as it appears in Procore and separate each tier with the greater than (>) symbol. Do NOT use spaces between tiers on either side of the greater than (>) symbol. For example, a correct two-tier location entry might look like: **Lot 1>Section A**.
   - **Trade**  
      Enter the trade name exactly as it appears in the Company level Admin tool. See [Add or Delete Trade Names](/product-manuals/admin-company/tutorials/add-a-custom-trade).
   - **Schedule Impact**  
      Select one of the following options for each punch list item. Any entry other than the ones below will result in a blank entry after the import:

     - **tbd:** This is short for 'To Be Determined'. Select this option if the impact to the schedule is not yet determined.
     - **n\_a:** This is short for 'Not Applicable'. Select this option to leave the field blank.
     - **no\_impact:** Select this option to indicate the punch list item has no impact to on the project schedule.
     - **yes\_unknown:** Select this option to indicate the punch list item will impact the project schedule, but the impact is not known.
     - **yes\_known:** Select this option to indicate the punch list item impacts the project schedule and the number of days by which the project schedule will be impacted is known. If you select this option, you must enter a number of days in the 'Schedule Impact Days' field.
   - **Schedule Impact Days**  
      If you selected **yes\_known** in the 'Schedule Impact' field, enter a number of days by which the project schedule will be impacted by.
   - **Cost Code**  
      Associate a cost code with a punch list item. The cost code must be formatted "division - cost code" written with the exact amount of digits as listed in your project or company in Procore. See [Add Company Cost Codes](/process-guides/company-administration-work-breakdown-structure-guide/add-company-cost-codes).
   - **Punch Item Type**  
      Enter one item type to categorize the punch list item (e.g., Electrical, Instrumentation, or Mechanical). For a successful import, types must be added to the Punch List tool before the import process, see [Configure Advanced Settings: Punch List: Add Punch Item Types](/product-manuals/punch-list-project/tutorials/configure-advanced-settings-punch-list).
   - **Due Date**  
      Enter the date the punch list item must be completed using the MM/DD/YYYY format (e.g., 06/01/2020).  
     ***Important!*** Do NOT enter dates in the M/D/YYYY format (e.g., do NOT enter 6/1/2020) or the import will fail.  
     *Note:* The 'Number Format' for cells in this column must be 'Text'.
   - **Priority**  
      Select one of the following options for each punch list item to indicate their priority levels.

     - **low**
     - **medium**
     - **high**
   - **Cost Impact**  
      Select in one of the following options for each punch list item. Any entry other than these will cause the field to be left blank.

     - **tbd:** This is short for 'To Be Determined'. Select this option if the cost impact is not yet determined.
     - **n\_a:** This is short for 'Not Applicable'. Select this option to leave the field blank.
     - **no\_impact:** Select this option to indicate the punch list item has no cost impact.
     - **yes\_unknown:** Select this option to indicate the punch list item has cost impact, but the cost amount is not known.
     - **yes\_known:** Select this option to indicate the punch list item has cost impact and the cost amount is known. If you select this option, you must also enter a dollar amount in the 'Cost Impact Amount' field.
   - **Cost Impact Amount**  
      If you selected **yes\_known** in the 'Cost Impact' field, enter the dollar amount here. Do NOT include the dollar sign ($) symbol.
   - **Reference**  
      Enter a relevant keyword or phrase to use as an item reference. This is a free-form text field to be used as specified by your organization. For example, if the item was created at the client's request, enter "client request".
   - **Description**  
      Enter additional descriptive information related to completing the punch list item. You can enter up to 255 alphanumeric characters.
   - **Comments**  
      Enter in additional comments you may have on the punch list item. You can enter up to 255 alphanumeric characters.

## Next Steps

- [Import Punch List Items into your Project Level Punch List Tool (Procore Imports)](/product-manuals/procore-imports/tutorials/import-punch-list-items-into-your-project-level-punch-list-tool-procore-imports)