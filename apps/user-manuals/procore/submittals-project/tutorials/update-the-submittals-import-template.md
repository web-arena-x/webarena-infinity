# Update the Submittals Import Template

Source: https://v2.support.procore.com/product-manuals/submittals-project/tutorials/update-the-submittals-import-template

---

***IMPORTANT!*** In order to protect the integrity of your companyâs data, Procore Employees are restricted from modifying the data that clients submit in all Procore Import Templates. This restriction applies to all data modifications, including correcting typographical errors. If Procore determines that errors are present in any Procore Import Template that you submit to Procore, it will be returned to you for correction. **Please note that the import process may take up to 72 hours to process.**

## Things to Consider

- **Required User Permissions:**

  - *To update the import template:* None. This task is performed in Microsoft Excel.
- **Import Template Requirements:**  
   For general formatting considerations, see [How do I prepare my data for import into Procore?](/product-manuals/procore-imports/tutorials/prepare-your-data-for-import-into-procore)

  - The template must be formatted as a table.
  - The first line of the table must include the *header*, which defines the fields in the database.\* For submittals, the following headers are supported: *Package Title, Package Spec Section Number, Package Spec Section Description, Package Number, Submittal Title, Submittal Spec Section Number, Submittal Spec Section Description, Submittal Number, Description, Submittal Manager, Submittal Status, Submittal Type, Location, Received Date, Issue Date,* *Submit By Date and Responsible Contractor Name*.   
    *Note:* At a minimum, your complete import template must include data in the *Submittal Number* and *Submittal Manager* fields for a successful import.\* If the Submittal Schedule Calculations feature is enabled (see [Set Up Submittal Schedule Calculations](/product-manuals/submittals-project/tutorials/set-up-submittal-schedule-calculations)), these headers are also supported: Required On-Site Date, Lead Time, Design Team Review Time, and Internal Review Time
  - If you leave the 'Submittal Status' value blank in the import template, the system sets the status to 'Draft' by default.
- **Additional Information** **:**

  - You are allowed to create submittals with the same submittal number. The import process can only be used to add new submittals to the project. The import process will not overwrite or delete a project's existing submittals.
  - If your project is using multi-tiered locations, you can only associate submittals with existing tiers or create new multi-tier locations via the import process.

## Prerequisites

- [Download the Submittals Import Template](/product-manuals/submittals-project/tutorials/download-the-submittals-import-template)
- Before submitting your import data to Procore, complete these prerequisites:

  - **Users:**\* If you will be adding a user's email address as a Submittal Manager value, ensure that these users have been added to your company's or the project's Directory tool. See [Prepare Users & Vendors for Import to the Procore Imports App (Company Directory)](/product-manuals/procore-imports/tutorials/prepare-users-and-vendors-for-import-to-the-procore-imports-app) and [Prepare Users & Vendors for Import to the Procore Imports App (Project Directory)](/product-manuals/procore-imports/tutorials/prepare-users-vendors-for-import-to-the-procore-imports-app).
  - **Vendors:**\* If you will be assigning a vendor/company as the 'Responsible Contractor' for a submittal, ensure that the vendor/company has been added to the company's or project's Directory tool. See [Prepare Users & Vendors for Import to the Procore Imports App (Company Directory)](/product-manuals/procore-imports/tutorials/prepare-users-and-vendors-for-import-to-the-procore-imports-app) and [Prepare Users & Vendors for Import to the Procore Imports App (Project Directory)](/product-manuals/procore-imports/tutorials/prepare-users-vendors-for-import-to-the-procore-imports-app).
  - **Locations:**\* If your project is using single-tier locations, you can either create new a new location to the Admin tool during the import process or you can associate a submittal with an existing location during the import process. See [Add Office Locations](/product-manuals/admin-company/tutorials/add-an-office-location).   
     OR\* If your project is using multi-tiered locations, the tiers must already exist in Procore in order to associate a submittal with the location. See [Add Multi-Tiered Locations to the Admin Tool](/product-manuals/admin-project/tutorials/add-multi-tiered-locations-to-a-project) and [How Do I Add a Multi-Tiered Location To An Item?](/product-manuals/admin-project/tutorials/add-a-multi-tiered-location-to-an-item)
  - **Specifications:**\* If your company is using the Specifications tool to manage specifications, upload the project specifications to Procore (see [Upload Specifications](/product-manuals/specifications-project/tutorials/upload-specifications)) or manually add them to Procore. See [Manually Create Divisions](/product-manuals/specifications-project/tutorials/manually-create-divisions) and [Manually Create Specification Sections](/product-manuals/specifications-project/tutorials/manually-create-spec-sections).   
     OR\* If your company is using the Admin tool to manage specifications, you must [Add Specification Sections to the Admin Tool](/product-manuals/admin-project/tutorials/add-spec-sections-to-the-admin-tool).
  - **Submittal Packages:**\* If you plan to import submittals into an existing submittal package, the existing package's Package Title, Package Specification Section, and Package Number must match.
  - **Admin: Configure Submittal Settings:**\* See [Best Practices: Company Level Submittal Settings](/process-guides/best-practices-submittals/company-level-settings) and [Best Practices: Submittal Project Configurations](/process-guides/best-practices-submittals/project-configurations).

## Steps

1. Complete the **Submittal Package Information** as follows:  
    If you will be importing 

   A *submittal package* is a container that stores one or more *submittals*. Typically, a *general contractor* creates submittal packages that list all of the individual submittals specific to a particular trade or *subcontractor*. For example, one might create a submittal package to contain all of the plumbing-related submittals in a commercial building project.

   Submittal Package information, include the following information for each submittal line item. If you want to import submittals without adding them to a package, leave cells A-D blank and continue with Step 3.

   1. **Package Title**: To create a submittal in a package, enter the package title here. To include multiple submittals in a package, repeat the package title entry in each submittal record (i.e., row).
   2. **Package Spec Section Number**: Enter the spec section number for the submittal package exactly as it appears in the Specifications or Admin tool. *Note*: If the Microsoft Excel column does NOT permit you to add a leading zero, select the entire column, choose Format > Cells, and then create a 'Custom' Number Format that matches your spec section numbering convention in the Number tab. See [Create or Delete a Custom Number Format in Excel](https://support.office.com/en-us/article/Create-or-delete-a-custom-number-format-78f2a361-936b-4c03-8772-09fab54be7f4).
   3. **Package Spec Section Description**: Enter the spec section description here (e.g., 03 or 04). This is an open text field.
   4. **Package Number:** Enter a submittal package number (e.g., 0001, PKG001, etc.). If you want to create a submittal package via the import process, this is a required field. Duplicate package numbers are allowed and the value entered in this field must be less than 255 characters.
2. **Submittal Information:** For individual submittals, include the following information:

   1. **Submittal Title:** Enter a submittal title. You can enter the same title for multiple submittals. To create the submittal in a package, the row must contain data in the **Package Title** and **Package Number** columns.
   2. **Submittal Spec Section Number:** Enter the spec section number for the submittal exactly as it appears in the Specifications or Admin tool. *Note:* If you are creating the submittal in a new or existing submittal package and you entered data in the **Package Spec Section Number** column, the **Submittal Spec Section Number** is a required column. ***Important!*** The spec section number must be entered exactly as it is listed in Procore or the import will fail.
   3. **Submittal Spec Section Description:** Enter the spec section description for the submittal. This is an open text field. *Note*: If the Spec Section Number that you entered in the previous column exactly matches an existing Spec Section in the project's Specifications tool, the Spec Section Description that is present in the Specifications tool will take precedence over your entry in this worksheet.
   4. **Submittal Number\*:** Enter the submittal number. Duplicate numbers are permitted (i.e., more than one submittal can have the same number). This is a required field. *Note*: Do not include revision numbers.
   5. **Description:** Enter a description for the submittal. This is an open text field. Duplicate submittal descriptions are permitted (i.e., more than one submittal can have the same description).
   6. **Submittal Manager\*:** Enter the email address for the Procore user you want to designate as the submittal's Submittal Manager. In Procore, a *submittal manager* is the person responsible for overseeing a submittal throughout its lifecycle. *Note:* Users added to this row need to be already added to the Project Directory with 'Standard' level permissions or higher on the project's Submittals tool. See [Add a User Account to the Project Directory](/product-manuals/directory-project/tutorials/add-user-account-to-project-directory). ***Important!*** The email address must be entered exactly as it is listed in Procore or the import will fail.
   7. **Submittal Status:** Enter a status for the submittal. The Procore default statuses that are available to assign to a submittal include: *Open*, *Draft*, and *Closed*. To create a custom status, see [Create a Custom Submittal Log Status](/product-manuals/admin-company/tutorials/create-custom-submittal-log-statuses). ***Important!*** The status must be entered exactly as it is listed in Procore or the import will fail.
   8. **Submittal Type**: Enter the information type associated with the submittal. The default type selections in Procore include: *Document*, *Plans*, *Prints*, *Product Information*, *Product Manual*, *Sample*, *Shop Drawing*, and *Other*. To create a custom type, see [Create Custom Submittal Types](/product-manuals/admin-company/tutorials/create-custom-submittal-types). ***Important!*** The type must be entered exactly as it is listed in Procore or the import will fail.
   9. **Location:** Enter the location at the job site for the submittal. This can be an existing location from the Location list or a tiered location. See [Add Tiered Locations to a Project](/product-manuals/admin-project/tutorials/add-multi-tiered-locations-to-a-project). ***Important!*** The location must be entered exactly as it is listed in Procore or the import will fail. Tiered locations must be entered with an angle bracket symbol (>) between each tier (for example, Parking Lot A > Ground Floor > East).
   10. **Received Date:** Enter the date the submittal was received using the date format MM/DD/YYYY. ***Important!*** If you enter dates in another format such as M/D/YYYY, the import will fail.   
       *Note:* If the Excel column is not permitting you to add a leading zero, select the entire column, choose Format > Cells and then create a 'Custom' Number Format named 'mm/dd/yyyy' in the Number tab. See Microsoft's [Create a Custom Number Format](https://support.office.com/en-us/article/create-a-custom-number-format-78f2a361-936b-4c03-8772-09fab54be7f4?ui=en-US&rs=en-US&ad=US).
   11. **Issue Date:** Enter the date the submittal was issued using the date format MM/DD/YYYY.   
       ***Important!*** If you enter dates in another format such as M/D/YYYY, the import will fail. *Note*: If the Excel column is not permitting you to add a leading zero, select the entire column, choose Format > Cells and then create a 'Custom' Number Format named 'mm/dd/yyyy' in the Number tab. See Microsoft's [Create a Custom Number Format](https://support.office.com/en-us/article/create-a-custom-number-format-78f2a361-936b-4c03-8772-09fab54be7f4?ui=en-US&rs=en-US&ad=US).
   12. **Submit By Date:** Enter the date the submittal must be submitted to the design team on the submittal workflow for review using the date format MM/DD/YYYY. ***Important!*** If you enter dates in another format such as M/D/YYYY, the import will fail. *Note:* If the Excel column is not permitting you to add a leading zero, select the entire column, choose Format > Cells and then create a 'Custom' Number Format named 'mm/dd/yyyy' in the Number tab. See Microsoft's [Create a Custom Number Format](https://support.office.com/en-us/article/create-a-custom-number-format-78f2a361-936b-4c03-8772-09fab54be7f4?ui=en-US&rs=en-US&ad=US).
   13. **Responsible Contractor Name:** Enter the company name of the contractor/subcontractor that is responsible for completing the work specified on the submittal. ***Important!*** The company name must be entered exactly as it is listed in Procore or the import will fail.
3. For **Submittal Schedule Calculations**, do the following:

   - If the Submittal Schedule Calculations feature is disabled (this is the default setting), leave columns R, S, T, and U columns blank. *Note*: If you include information in any of these columns, the data will be disregarded by the import because the feature is disabled. If you enable the feature at a later time, you will need to manually enter this information.
   - If you have enabled the Submittal Schedule Calculations feature in the Submittals tool (see [Enable Submittal Schedule Calculations](/product-manuals/submittals-project/tutorials/enable-submittal-schedule-calculations)), you have the option to include this information:
   1. **Required On-Site Date:** Enter the on-site date for the submittal using the date format MM/DD/YYYY. ***Important!*** If you enter dates in another format such as M/D/YYYY, the import will fail.  
      *Note:* If the Excel column is not permitting you to add a leading zero, select the entire column, choose Format > Cells and then create a 'Custom' Number Format named 'mm/dd/yyyy' in the Number tab. See Microsoft's [Create a Custom Number Format](https://support.office.com/en-us/article/create-a-custom-number-format-78f2a361-936b-4c03-8772-09fab54be7f4?ui=en-US&rs=en-US&ad=US).
   2. **Lead Time:** Enter a number of days (e.g., 15 or 30) to specify the lead time for the submittal.
   3. **Design Team Review Time:** Enter a number of days (e.g., 15 or 30) to specify the total of days allotted to the design team to review and approve the submittal.
   4. **Internal Review Time:** Enter a number of days (e.g., 15 or 30) to specify the total number of days allotted to the submittal for internal review.
4. Save your updates to the file.
5. When your data entry is complete, continue with [Send a Completed Submittals Import Template to Procore](/product-manuals/submittals-project/tutorials/send-a-completed-submittals-import-template-to-procore).