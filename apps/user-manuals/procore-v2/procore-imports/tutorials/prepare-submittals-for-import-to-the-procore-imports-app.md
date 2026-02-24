# Prepare Submittals for Import to the Procore Imports App

Source: https://v2.support.procore.com/product-manuals/procore-imports/tutorials/prepare-submittals-for-import-to-the-procore-imports-app

---

## Background

The Procore Imports app is used to self-import your submittals in bulk to your Project's Submittals tool. This will add as many submittals to your project as you need without having to manually add each submittal in Procore.

## Things to Consider

- **Required User Permissions:**

  - 'Admin' level permissions on the project's Submittals tool.  
    *Note:* Granular Permissions are not supported in the Procore Imports application.
- **Additional Information:**

  - This import can only be used to add submittals. Your import will not edit or delete any existing submittals in your project.

## Prerequisites

Before submitting your import data to Procore, complete these prerequisites:

- **Users:**

  - If you will be adding a user's email address as a Submittal Manager value, ensure that these users have been added to the company's or project's Directory tool. See [Prepare Users & Vendors for Import to the Procore Imports App (Company Directory)](/product-manuals/procore-imports/tutorials/prepare-users-and-vendors-for-import-to-the-procore-imports-app) and [Prepare Users & Vendors for Import to the Procore Imports App (Project Directory)](/product-manuals/procore-imports/tutorials/prepare-users-vendors-for-import-to-the-procore-imports-app).
- **Vendors:**

  - If you will be assigning a vendor/company as the 'Responsible Contractor' for a submittal, ensure that the vendor/company has been added to the company's or project's Directory tool. See [Prepare Users & Vendors for Import to the Procore Imports App (Company Directory)](/product-manuals/procore-imports/tutorials/prepare-users-and-vendors-for-import-to-the-procore-imports-app) and [Prepare Users & Vendors for Import to the Procore Imports App (Project Directory)](/product-manuals/procore-imports/tutorials/prepare-users-vendors-for-import-to-the-procore-imports-app).
- **Locations:**

  - If your project is using single-tier locations, you can either create a new location to the Admin tool during the import process or you can associate a submittal with an existing location during the import process. See [Add Office Locations](/product-manuals/admin-company/tutorials/add-an-office-location).   
     OR
  - If your project is using multi-tiered locations, the tiers must already exist in Procore in order to associate a submittal with the location. See [Add Multi-Tiered Locations to the Admin Tool](/product-manuals/admin-project/tutorials/add-multi-tiered-locations-to-a-project) and [How Do I Add a Multi-Tiered Location To An Item?](/product-manuals/admin-project/tutorials/add-a-multi-tiered-location-to-an-item).
- **Specifications:**

  - If your company is using the Specifications tool to manage specifications, upload the project specifications to Procore (see [Upload Specifications](/product-manuals/specifications-project/tutorials/upload-specifications)) or manually add them to Procore. See [Manually Create Divisions](/product-manuals/specifications-project/tutorials/manually-create-divisions) and [Manually Create Specification Sections](/product-manuals/specifications-project/tutorials/manually-create-spec-sections).   
     OR
  - If your company is using the Admin tool to manage specs, you must [Add Specification Sections to the Admin Tool](/product-manuals/admin-project/tutorials/add-spec-sections-to-the-admin-tool).
- **Submittal Packages:**

  - If you plan to import submittals into an existing submittal package, the existing package's Package Title, Package Specification Section, and Package Number must match.
- **Admin: Configure Submittal Settings:**

  - See [Best Practices: Company Level Submittal Settings](/process-guides/best-practices-submittals/company-level-settings) and [Best Practices: Submittal Project Configurations](/process-guides/best-practices-submittals/project-configurations).

## Steps

- Download the Submittals Import Template
- Format the Submittals Import Template

#### Download the Submittals Import Template

1. Download the Submittals Import Template: [import-submittals.xlsx](https://procore-imports-templates.s3.amazonaws.com/import%5Ftemplate%5Fsubmittals.xlsx)

#### Format the Submittals Import Template

1. See below considerations when filling out the template.

   - **Email Addresses** (Submittal Manager). Usersâ email addresses must be in the Project Directory in order to be imported. Please ensure the email address on the import template is exactly how it is input in the Project Directory.
   - **Required Fields.** Submittal Manager and Submittal Number
2. Complete the import template. *Notes:*

   - If you want to import submittals WITHOUT adding them to a package, leave cells A-D blank.
   - If you want to import submittals with spec sections, enter the existing spec sections in the columns Submittal Spec Section Number and Submittal Spec Section Description.

###### Submittal Package Information

For submittals you want in a package, include the following information:

- **Package Title**. To create a submittal in a package, enter the package title here exactly as it appears in the Submittals tool. To include multiple submittals in a package, repeat the package title entry in each submittal entry.
- **Package Spec Section Number**. Enter the spec section number for the submittal package exactly as it appears in the Specifications or Admin tool.   
  *Note:* If the Microsoft Excel column does NOT permit you to add a leading zero, select the entire column, choose Format > Cells, and then create a 'Custom' Number Format that matches your spec section numbering convention in the Number tab. See [Create or Delete a Custom Number Format in Excel](https://support.office.com/en-us/article/Create-or-delete-a-custom-number-format-78f2a361-936b-4c03-8772-09fab54be7f4).
- **Package Spec Section Description**. Enter the spec section description exactly as it appears in the Specifications tool.
- **Package Number**. Enter the submittal package number exactly as it appears in the Submittals tool. Duplicate package numbers are allowed and the value entered in this field must be less than 255 characters.

#### Submittal Information

For individual submittals, include the following information:

- **Submittal Title**  
   Enter a submittal title. You can enter the same title for multiple submittals. To create the submittal in a package, the row must contain data in the **Package Title** and **Package Number** columns.
- **Submittal Spec Section Number**  
   Enter the spec section number for the submittal exactly as it appears in the Specifications or Admin tool.   
  *Note:* If you are creating the submittal in a new or existing submittal package and you entered data in the **Package Spec Section Number** column, the **Submittal Spec Section Number** is a required column.  
  ***Important!*** The spec section number must be entered exactly as it is listed in Procore or the import will fail.
- **Submittal Spec Section Description**  
   Enter the spec section description for the submittal. This is an open text field.  
  *Note:* If the Spec Section Number that you entered in the previous column exactly matches an existing Spec Section in the project's Specifications tool, the Spec Section Description that is present in the Specifications tool will take precedence over your entry in this worksheet.
- **Submittal Number\***  
   Enter the submittal number. Duplicate numbers are permitted (i.e., more than one submittal can have the same number). This is a required field.  
  *Note:* Do not include revision numbers.
- **Description**  
   Enter a description for the submittal. This is an open text field. Duplicate submittal descriptions are permitted (i.e., more than one submittal can have the same description).
- **Submittal Manager\***  
   Enter the email address for the Procore user you want to designate as the submittal's Submittal Manager. In Procore, a *submittal manager* is the person responsible for overseeing a submittal throughout its lifecycle.  
  *Note:* Users added to this row need to be already added to the Project Directory with 'Standard' level permissions or higher on the project's Submittals tool. See [Add a User Account to the Project Directory](/product-manuals/directory-project/tutorials/add-user-account-to-project-directory).  
  ***Important!*** The email address must be entered exactly as it is listed in Procore or the import will fail.
- **Submittal Status**  
   Enter a status for the submittal. The Procore default statuses that are available to assign to a submittal include: *Open*, *Draft*, and *Closed*. To create a custom status, see [Create a Custom Submittal Log Status](/product-manuals/admin-company/tutorials/create-custom-submittal-log-statuses).  
  ***Important!*** The status must be entered exactly as it is listed in Procore or the import will fail.
- **Submittal Type**  
   Enter the information type associated with the submittal. The default type selections in Procore include: *Document*, *Plans*, *Prints*, *Product Information*, *Product Manual*, *Sample*, *Shop Drawing*, and *Other*. To create a custom type, see [Create Custom Submittal Types](/product-manuals/admin-company/tutorials/create-custom-submittal-types).  
  ***Important!*** The type must be entered exactly as it is listed in Procore or the import will fail.
- **Location**  
   Enter the location at the job site for the submittal. This can be an existing location from the Location list or a tiered location. See [Add Tiered Locations to a Project](/product-manuals/admin-project/tutorials/add-multi-tiered-locations-to-a-project).  
  ***Important!*** If your project is using multi-tiered locations, you must enter the location exactly as it appears in Procore and separate each tier with the greater than (>) symbol. Do NOT use spaces between tiers on either side of the greater than (>) symbol. For example, a correct two-tier location entry might look like: **Lot 1>Section A**.
- **Received** **Date**  
   Enter the date the submittal was received using the date format MM/DD/YYYY.  
  ***Important!*** If you enter dates in another format such as M/D/YYYY, the import will fail.   
  *Note:* The 'Number Format' for cells in this column must be 'Text'. This is the default setting for this column in the Submittals Import Template file.
- **Issue** **Date**  
   Enter the date the submittal was issued using the date format MM/DD/YYYY.   
  ***Important!*** If you enter dates in another format such as M/D/YYYY, the import will fail.  
  *Note:* The 'Number Format' for cells in this column must be 'Text'. This is the default setting for this column in the Submittals Import Template file.
- **Submit By Date**  
   Enter the date the submittal must be submitted to the design team on the submittal workflow for review using the date format MM/DD/YYYY.  
  ***Important!*** If you enter dates in another format such as M/D/YYYY, the import will fail.  
  *Note:* The 'Number Format' for cells in this column must be 'Text'. This is the default setting for this column in the Submittals Import Template file.
- **Responsible Contractor Name**  
   Enter the company name of the contractor/subcontractor that is responsible for completing the work specified on the submittal.  
  ***Important!*** The company name must be entered exactly as it is listed in Procore or the import will fail.

For **Submittal Schedule Calculations**, do the following:

- If the Submittal Schedule Calculations feature is disabled (this is the default setting), leave columns R, S, T, and U columns blank.   
  *Note:* If you include information in any of these columns, the data will be disregarded by the import because the feature is disabled. If you enable the feature at a later time, you will need to manually enter this information.  
   OR
- If you have enabled the Submittal Schedule Calculations feature in the Submittals tool (see [Enable Submittal Schedule Calculations](/product-manuals/submittals-project/tutorials/enable-submittal-schedule-calculations)), you have the option to include this information:

  - **Required On-Site** **Date**  
     Enter the on-site date for the submittal using the date format MM/DD/YYYY.   
    ***Important!*** If you enter dates in another format such as M/D/YYYY, the import will fail.  
    *Note:* The 'Number Format' for cells in this column must be 'Text'. This is the default setting for this column in the Submittals Import Template file.
  - **Lead Time**  
     Enter a number of days (e.g., 15 or 30) to specify the lead time for the submittal.
  - **Design Team Review Time**  
     Enter a number of days (e.g., 15 or 30) to specify the total of days allotted to the design team to review and approve the submittal.
  - **Internal Review Time**  
     Enter a number of days (e.g., 15 or 30) to specify the total number of days allotted to the submittal for internal review.

## Next Steps

- [Import](/product-manuals/procore-imports/tutorials/import-submittals-into-your-project-level-submittals-tool-procore-imports) [Submittals into your Project Level Submittals Tool (Procore Imports)](/product-manuals/procore-imports/tutorials/import-submittals-into-your-project-level-submittals-tool-procore-imports)  
     
   OR

1. Send an email request to: [imports@procore.com](mailto:imports@procore.com) and add the completed XLSX file as an attachment.  
   *Note:* In your email's 'Subject' line, include your project's name and ID. See [How do I find the project ID?](/faq-how-do-i-find-the-project-id)  
   ***Important!*** You will not be able to undo the import, so it is imperative that the data that you submit to Procore for the import is accurate.
2. After your Procore point of contact notifies you that the import is complete, navigate to the Submittals tool to validate that the imported submittal records are displaying as expected.