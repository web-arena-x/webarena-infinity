# Update the Submittals Import Template - Procore

Source: https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/update-the-submittals-import-template

---

**NOTE TO SUPERUSERS:**

Effective June 20, 2018, customers are being encouraged to use the Submittal Builder. For instructions, see [Submittal Builder: Generate Submittals from Specifications](https://support.procore.com/products/online/user-guide/project-level/specifications/tutorials/generate-submittal-log "Generate Submittals from Specifications (Submittal Builder)"). The XLSX version of the submittals import is no longer available to end users directly. Instead, they must submit a request to: [imports@procore.com](mailto:imports@procore.com "mailto:imports@procore.com")

1. [Send a Completed Submittals Import Template to Procore](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/send-a-completed-submittals-import-template-to-procore "Send a Completed Submittals Import Template to Procore") This is a public-facing article that is available to end users on the Support site. It describes how to submit a request for a submittals import.
2. AFTER the user submits the completed template:
   1. Verify that the user account has the appropriate permission to request a data import.
   2. Verify that the user has properly completed all of the import template requirements.  
      ****IMPORTANT!****  ***Procore Employees are restricted from modifying the data that clients submit in all Procore Import Templates. If errors are found, return the template to the end user for correction.***

Click here to read an important note about Data Imports
:   ***IMPORTANT!***In order to protect the integrity of your company’s data, Procore Employees are restricted from modifying the data that clients submit in all Procore Import Templates. This restriction applies to all data modifications, including correcting typographical errors. If Procore determines that errors are present in any Procore Import Template that you submit to Procore, it will be returned to you for correction. **Please note that the import process may take up to 72 hours to process.**

## Objective

To update the submittals import template.

## Things to Consider

- **Required User Permissions:**
  - *To update the import template:*None. This task is performed in Microsoft Excel.
- **Import Template Requirements:**  
  For general formatting considerations, see [How do I prepare my data for import into Procore?](https://support.procore.com/products/procore-imports/tutorials/prepare-your-data-for-import-into-procore "https://support.procore.com/faq/how-do-i-prepare-my-data-for-import-into-procore")
  - The template must be formatted as a table.
  - The first line of the table must include the *header*, which defines the fields in the database.
    - For submittals, the following headers are supported: *Package Title, Package Spec Section Number, Package Spec Section Description, Package Number, Submittal Title, Submittal Spec Section Number, Submittal Spec Section Description, Submittal Number, Description, Submittal Manager, Submittal Status, Submittal Type, Location, Received Date, Issue Date,**Submit By Date and Responsible Contractor Name*.   
      *Note:* At a minimum, your complete import template must include data in the *Submittal Number* and *Submittal Manager* fields for a successful import.
    - If the Submittal Schedule Calculations feature is enabled (see [Set Up Submittal Schedule Calculations](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/set-up-submittal-schedule-calculations "products/online/user-guide/project-level/submittals/tutorials/set-up-submittal-schedule-calculations")), these headers are also supported: Required On-Site Date, Lead Time, Design Team Review Time, and Internal Review Time
  - If you leave the 'Submittal Status' value blank in the import template, the system sets the status to 'Draft' by default.
- **Additional Information****:**
  - You are allowed to create submittals with the same submittal number. The import process can only be used to add new submittals to the project. The import process will not overwrite or delete a project's existing submittals.
  - If your project is using multi-tiered locations, you can only associate submittals with existing tiers or create new multi-tier locations via the import process.

## Prerequisites

- [Download the Submittals Import Template](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/download-the-submittals-import-template "Download the Submittals Import Template")
- Before submitting your import data to Procore, complete these prerequisites:
  - **Users:**
    - If you will be adding a user's email address as a Submittal Manager value, ensure that these users have been added to your company's or the project's Directory tool. See [Prepare Users & Vendors for Import to the Procore Imports App (Company Directory)](https://support.procore.com/products/procore-imports/company-directory/tutorials/prepare-users-and-vendors-for-import-to-the-procore-imports-app "Prepare Users & Vendors for Import to the Procore Imports App") and [Prepare Users & Vendors for Import to the Procore Imports App (Project Directory)](https://support.procore.com/products/procore-imports/project-directory/tutorials/prepare-users-vendors-for-import-to-the-procore-imports-app "Prepare Users & Vendors for Import to the Procore Imports App").
  - **Vendors:**
    - If you will be assigning a vendor/company as the 'Responsible Contractor' for a submittal, ensure that the vendor/company has been added to the company's or project's Directory tool. See [Prepare Users & Vendors for Import to the Procore Imports App (Company Directory)](https://support.procore.com/products/procore-imports/company-directory/tutorials/prepare-users-and-vendors-for-import-to-the-procore-imports-app "Prepare Users & Vendors for Import to the Procore Imports App") and [Prepare Users & Vendors for Import to the Procore Imports App (Project Directory)](https://support.procore.com/products/procore-imports/project-directory/tutorials/prepare-users-vendors-for-import-to-the-procore-imports-app "Prepare Users & Vendors for Import to the Procore Imports App").
  - **Locations:**
    - If your project is using single-tier locations, you can either create new a new location to the Admin tool during the import process or you can associate a submittal with an existing location during the import process. See [Add Office Locations](https://support.procore.com/products/online/user-guide/company-level/admin/tutorials/add-an-office-location "products/online/user-guide/company-level/admin/tutorials/add-office-locations").   
      OR
    - If your project is using multi-tiered locations, the tiers must already exist in Procore in order to associate a submittal with the location. See [Add Multi-Tiered Locations to the Admin Tool](https://support.procore.com/products/online/user-guide/project-level/admin/tutorials/add-multi-tiered-locations-to-a-project "products/online/user-guide/project-level/admin/tutorials/add-multi-tiered-locations-to-the-admin-tool") and [How Do I Add a Multi-Tiered Location To An Item?](https://support.procore.com/products/online/user-guide/project-level/admin/tutorials/add-a-multi-tiered-location-to-an-item "faq/how-do-i-add-a-multi-tiered-location-to-an-item")
  - **Specifications:**
    - If your company is using the Specifications tool to manage specifications, upload the project specifications to Procore (see [Upload Specifications](https://support.procore.com/products/online/user-guide/project-level/specifications/tutorials/upload-specifications "Upload Specifications")) or manually add them to Procore. See [Manually Create Divisions](https://support.procore.com/products/online/user-guide/project-level/specifications/tutorials/manually-create-divisions "Manually Create Divisions") and [Manually Create Specification Sections](https://support.procore.com/products/online/user-guide/project-level/specifications/tutorials/manually-create-spec-sections "Manually Create Spec Sections").   
      OR
    - If your company is using the Admin tool to manage specifications, you must [Add Specification Sections to the Admin Tool](https://support.procore.com/products/online/user-guide/project-level/admin/tutorials/add-spec-sections-to-the-admin-tool "/products/online/user-guide/project-level/admin/tutorials/add-spec-sections-to-the-admin-tool").
  - **Submittal Packages:**
    - If you plan to import submittals into an existing submittal package, the existing package's Package Title, Package Specification Section, and Package Number must match.
  - **Admin: Configure Submittal Settings:**
    - See [Best Practices: Company Level Submittal Settings](https://support.procore.com/products/online/user-guide/project-level/submittals/best-practices-submittals/best-practices-company-level-submittal-settings "Best Practices: Company Level Submittal Settings") and [Best Practices: Submittal Project Configurations](https://support.procore.com/products/online/user-guide/project-level/submittals/best-practices-submittals/best-practices-submittal-project-configurations "Best Practices: Submittal Project Configurations").

## Steps

1. Complete the **Submittal Package Information** as follows:  
   If you will be importing [submittal package](../../../../../../references/construction-management/glossary-of-terms.md#Submittal_Package "Glossary of Terms") information, include the following information for each submittal line item. If you want to import submittals without adding them to a package, leave cells A-D blank and continue with Step 3.
   1. **Package Title**  
      To create a submittal in a package, enter the package title here. To include multiple submittals in a package, repeat the package title entry in each submittal record (i.e., row).
   2. **Package Spec Section Number**  
      Enter the spec section number for the submittal package exactly as it appears in the Specifications or Admin tool.  
      *Note*: If the Microsoft Excel column does NOT permit you to add a leading zero, select the entire column, choose Format > Cells, and then create a 'Custom' Number Format that matches your spec section numbering convention in the Number tab. See [Create or Delete a Custom Number Format in Excel](https://support.office.com/en-us/article/Create-or-delete-a-custom-number-format-78f2a361-936b-4c03-8772-09fab54be7f4 "https://support.office.com/en-us/article/Create-or-delete-a-custom-number-format-78f2a361-936b-4c03-8772-09fab54be7f4").
   3. **Package Spec Section Description**  
      Enter the spec section description here (e.g., 03 or 04). This is an open text field.
   4. **Package Number**  
      Enter a submittal package number (e.g., 0001, PKG001, etc.). If you want to create a submittal package via the import process, this is a required field. Duplicate package numbers are allowed and the value entered in this field must be less than 255 characters.
2. **Submittal Information**  
   For individual submittals, include the following information:
   5. **Submittal Title**  
      Enter a submittal title. You can enter the same title for multiple submittals. To create the submittal in a package, the row must contain data in the **Package Title** and **Package Number** columns.
   6. **Submittal Spec Section Number**  
      Enter the spec section number for the submittal exactly as it appears in the Specifications or Admin tool.   
      *Note:*If you are creating the submittal in a new or existing submittal package and you entered data in the **Package Spec Section Number** column, the **Submittal Spec Section Number** is a required column.  
      ***Important!*** The spec section number must be entered exactly as it is listed in Procore or the import will fail.
   7. **Submittal Spec Section Description**  
      Enter the spec section description for the submittal. This is an open text field.  
      *Note*: If the Spec Section Number that you entered in the previous column exactly matches an existing Spec Section in the project's Specifications tool, the Spec Section Description that is present in the Specifications tool will take precedence over your entry in this worksheet.
   8. **Submittal Number\***  
      Enter the submittal number. Duplicate numbers are permitted (i.e., more than one submittal can have the same number). This is a required field.  
      *Note*: Do not include revision numbers.
   9. **Description**  
      Enter a description for the submittal. This is an open text field. Duplicate submittal descriptions are permitted (i.e., more than one submittal can have the same description).
   10. ****Submittal Manager\*****  
       Enter the email address for the Procore user you want to designate as the submittal's Submittal Manager. In Procore, a **submittal manager**is the person responsible for overseeing a submittal throughout its lifecycle.  
       **Note*:* Users added to this row need to be already added to the Project Directory with 'Standard' level permissions or higher on the project's Submittals tool. See [Add a User Account to the Project Directory](https://support.procore.com/products/online/user-guide/project-level/directory/tutorials/add-user-account-to-project-directory "Add a User Account to the Project Directory").  
       ***Important!***The email address must be entered exactly as it is listed in Procore or the import will fail.
   11. **Submittal Status**  
       Enter a status for the submittal. The Procore default statuses that are available to assign to a submittal include: *Open*, *Draft*, and *Closed*. To create a custom status, see [Create a Custom Submittal Log Status](https://support.procore.com/products/online/user-guide/company-level/admin/tutorials/create-custom-submittal-log-statuses "Create Custom Submittal Log Statuses").  
       ***Important!***The status must be entered exactly as it is listed in Procore or the import will fail.
   12. **Submittal Type**  
       Enter the information type associated with the submittal. The default type selections in Procore include: **Document**, **Plans**, **Prints**, **Product Information**, **Product Manual**, **Sample**, **Shop Drawing**, and **Other**. To create a custom type, see [Create Custom Submittal Types](https://support.procore.com/products/online/user-guide/company-level/admin/tutorials/create-custom-submittal-types "Create Custom Submittal Types").  
       ***Important!***The type must be entered exactly as it is listed in Procore or the import will fail.
   13. **Location**  
       Enter the location at the job site for the submittal. This can be an existing location from the Location list or a tiered location. See [Add Tiered Locations to a Project](https://support.procore.com/products/online/user-guide/project-level/admin/tutorials/add-multi-tiered-locations-to-a-project "Add Tiered Locations to a Project").  
       ***Important!***The location must be entered exactly as it is listed in Procore or the import will fail. Tiered locations must be entered with an angle bracket symbol (>) between each tier (for example, Parking Lot A > Ground Floor > East).
   14. **Received Date**  
       Enter the date the submittal was received using the date format MM/DD/YYYY.  
       ***Important!*** If you enter dates in another format such as M/D/YYYY, the import will fail.   
       *Note:* If the Excel column is not permitting you to add a leading zero, select the entire column, choose Format > Cells and then create a 'Custom' Number Format named 'mm/dd/yyyy' in the Number tab. See Microsoft's [Create a Custom Number Format](https://support.office.com/en-us/article/create-a-custom-number-format-78f2a361-936b-4c03-8772-09fab54be7f4?ui=en-US&rs=en-US&ad=US "https://support.office.com/en-us/article/create-a-custom-number-format-78f2a361-936b-4c03-8772-09fab54be7f4?ui=en-US&rs=en-US&ad=US").
   15. **Issue Date**  
       Enter the date the submittal was issued using the date format MM/DD/YYYY.   
       ***Important!***If you enter dates in another format such as M/D/YYYY, the import will fail.  
       *Note*: If the Excel column is not permitting you to add a leading zero, select the entire column, choose Format > Cells and then create a 'Custom' Number Format named 'mm/dd/yyyy' in the Number tab. See Microsoft's [Create a Custom Number Format](https://support.office.com/en-us/article/create-a-custom-number-format-78f2a361-936b-4c03-8772-09fab54be7f4?ui=en-US&rs=en-US&ad=US "https://support.office.com/en-us/article/create-a-custom-number-format-78f2a361-936b-4c03-8772-09fab54be7f4?ui=en-US&rs=en-US&ad=US").
   16. **Submit By Date**  
       Enter the date the submittal must be submitted to the design team on the submittal workflow for review using the date format MM/DD/YYYY.   
       ***Important!***If you enter dates in another format such as M/D/YYYY, the import will fail.  
       *Note:* If the Excel column is not permitting you to add a leading zero, select the entire column, choose Format > Cells and then create a 'Custom' Number Format named 'mm/dd/yyyy' in the Number tab. See Microsoft's [Create a Custom Number Format](https://support.office.com/en-us/article/create-a-custom-number-format-78f2a361-936b-4c03-8772-09fab54be7f4?ui=en-US&rs=en-US&ad=US "https://support.office.com/en-us/article/create-a-custom-number-format-78f2a361-936b-4c03-8772-09fab54be7f4?ui=en-US&rs=en-US&ad=US").
   17. **Responsible Contractor Name**  
       Enter the company name of the contractor/subcontractor that is responsible for completing the work specified on the submittal.  
       ***Important!***The company name must be entered exactly as it is listed in Procore or the import will fail.
3. For **Submittal Schedule Calculations**, do the following:
   - If the Submittal Schedule Calculations feature is disabled (this is the default setting), leave columns R, S, T, and U columns blank. *Note*: If you include information in any of these columns, the data will be disregarded by the import because the feature is disabled. If you enable the feature at a later time, you will need to manually enter this information.  
     OR
   - If you have enabled the Submittal Schedule Calculations feature in the Submittals tool (see [Enable Submittal Schedule Calculations](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/enable-submittal-schedule-calculations "Enable Submittal Schedule Calculations")), you have the option to include this information:
   18. **Required On-Site Date**  
       Enter the on-site date for the submittal using the date format MM/DD/YYYY.   
       ***Important!***If you enter dates in another format such as M/D/YYYY, the import will fail.  
       *Note:* If the Excel column is not permitting you to add a leading zero, select the entire column, choose Format > Cells and then create a 'Custom' Number Format named 'mm/dd/yyyy' in the Number tab. See Microsoft's [Create a Custom Number Format](https://support.office.com/en-us/article/create-a-custom-number-format-78f2a361-936b-4c03-8772-09fab54be7f4?ui=en-US&rs=en-US&ad=US "https://support.office.com/en-us/article/create-a-custom-number-format-78f2a361-936b-4c03-8772-09fab54be7f4?ui=en-US&rs=en-US&ad=US").
   19. **Lead Time**  
       Enter a number of days (e.g., 15 or 30) to specify the lead time for the submittal.
   20. **Design Team Review Time**  
       Enter a number of days (e.g., 15 or 30) to specify the total of days allotted to the design team to review and approve the submittal.
   21. **Internal Review Time**  
       Enter a number of days  (e.g., 15 or 30) to specify the total number of days allotted to the submittal for internal review.
4. Save your updates to the file.
5. When your data entry is complete, continue with [Send a Completed Submittals Import Template to Procore](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/send-a-completed-submittals-import-template-to-procore "Send a Completed Submittals Import Template to Procore").

## 

If you would like to learn more about Procore's submittals management software and how it can help your business, please visit our [construction submittals software product page ![icon-external-link.png](https://support.procore.com/@api/deki/files/186764/icon-external-link.png?revision=2&size=bestfit&width=14&height=14)](https://www.procore.com/project-management/submittals "https://www.procore.com/project-management/submittals").