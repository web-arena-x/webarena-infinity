# Update General Project Information

Source: https://v2.support.procore.com/product-manuals/admin-project/tutorials/update-general-project-information

---

## Things to Consider

- **Required User Permissions:**

 - You need one of the following:

    - 'Admin' level permissions on the Project level Admin tool.
    - 'Read Only' level permissions or higher on the Project level Admin tool with the ['Manage General' granular permission](/product-manuals/permissions-company/tutorials/grant-granular-permissions-in-a-project-permissions-template) enabled on your permission template.
- **Additional Information:**

 - The project information entered on this page may appear in numerous locations throughout Procore including when accessing the project in Procore Web and Procore Drive, project-related emails sent from Procore, CSV and PDF files exported from the project's tools, and others.
 - Weather data on the project's Home and Daily Log tools are determined by Latitude and Longitude coordinates entered on this page. See [How do I determine the latitude and longitude values of an address?](/faq-how-do-i-determine-the-latitude-and-longitude-values-of-an-address)
 - If your company has enabled the Company level ERP Integrations tool and you have synced data with a third-party accounting solution, a green ERP banner appears on the 'General Project Information' page to alert you that the project is integrated with an ERP system.
 - At the bottom of the Project's landing page, the following information appears:

    - Name and email of the person who created the project.
    - Date and time of the project's creation.
    - Date and time of the most recent update to the project's details.

## Steps

1. Navigate to the Project level **Admin** tool.
2. Under 'Project Settings', click **General**.
3. Update project information in the following sections as appropriate. 
   *Note:* An asterisk (\*) in the sections below indicates a required field.

   - Project Information
   - Project Location
   - Advanced
4. Click **Update** to save the changes.

### Project Information

- **Project Template**. Click the project template name to open the template.
- **Stage**. This represents the stage your project is currently in. Certain stages enable certain actions in Procore (for example, bidding in the Bidding stage). See [Add Custom Project Stages to Your Company](/product-manuals/admin-company/tutorials/add-a-custom-project-stage) to add custom stages.
- **Name\***. Enter an updated name for the project if necessary.
- **Project Number**. Enter or update the project number for your project.
- **Project ID**. View or copy the Project ID.
- **Description**. Enter or update the description of your project.
- **Work Scope**. Categorize the work according to scope, such as New Construction or Renovation/Alteration.
- **Project Sector**. Categorize the project based on the facility's function or purpose, such as Retail, Roadwork, or Multifamily.
- **Delivery Method**. Define how stakeholders will collaborate across each phase of the project including planning, design, and build. For example, Design-Bid-Build, Design-Build, or Construction Manager at Risk.
- **Logo.** Upload, replace, or remove a project logo. The project logo will display in the upper-left corner of the project navigation bar as well as in PDF exports, reports, and project emails. See [Upload a Project Logo](/product-manuals/admin-project/tutorials/upload-a-project-logo).
- **Project Photo.** Upload or remove a project photo. The project photo will help identify your project on the company's Portfolio and the project's Home pages. 
 *Note:* The file should have dimensions of 200 x 100 pixels, must not exceed the 3MB maximum, and must be saved in the GIF, JPG, or PNG file format.
- **Square Footage**. Enter or update the total number square feet of your project. This will only be reflected here for informational purposes.
- **Total Value\*.** This is the total amount of construction work performed, planned, or put in place during the project.
- **Code**. Enter a project code to help your team identify and locate the project in Procore. This should be an abbreviation of the 'Project Name.' *Note:* For projects using the Document Management tool, the 'Code' entered above integrates with the naming standards you specify in the tool's Configure Settings page. To learn more, see [What is the 'Code' field on the project creation page?](/faq-what-is-the-code-field-on-the-project-creation-page)
- **Language-Country:** Select one of the available language or point-of-view dictionary options from the drop-down list. To learn more about the available options, see [What languages are available in Procore?](/faq-what-languages-are-available-in-procore) and [What tool names and terms are different in Procore for general contractors, owners, and specialty contractors?](/faq-what-tool-names-and-terms-are-different-in-procore-for-general-contractors-owners-and-specialty-contractors)
- **Type:** This represents the type of project. Project types can be added in the Company level **Admin** tool. See [Create Custom Project Types](/product-manuals/admin-company/tutorials/add-a-custom-project-type). Select a project type from the drop-down menu.
- **Bid Type:** Select the bid type from the list. These selections are managed in the Company level Admin tool. See [Add a Custom Bid Type](/product-manuals/admin-company/tutorials/add-a-custom-bid-type).
- **Program:** Select the program to classify your project under. âThese options are managed in the Company level Admin tool. See [Add Programs](/product-manuals/programs-company/tutorials/add-programs). 
 *Note:* You can view your projects by program using the Programs tool.
- **Parent Project:** Select the name of the parent project in Procore from the drop-down list. In Procore, a parent job is a Procore project that has been designated as the 'parent' project for one or more related project(s) in Procore's Portfolio tool. To learn more, see [What's the difference between a job, a parent job, and a sub job?](/faq-what's-the-difference-between-a-job-a-parent-job-and-a-sub-job)
- **Owner Type:** Select the owner type from the list. These selections are managed in the Company level Admin tool. See [Add a Custom Owner Type](/product-manuals/admin-company/tutorials/add-a-custom-owner-type).
- **Flag:** Choose a project flag color you want to have appear next to this project in the company's Portfolio tool. 
 *Note:* The flag is used for your company's organizational purposes only and does not have any other impact on the project. For example, you can flag all commercial projects as GREEN and all internal projects as RED to easily identify them in your list of projects.
- **Active/Inactive:**

 - Click the toggle to the ON position to set the project to *Active*.
 - Click the toggle to the OFF position to set the project to *Inactive*.

### Project Location

- **Country\*.** Select the country where the project is located.
- **Street Address**. Enter the address of the project's job site.
- **City**. Enter the city where the project is located.
- **State**. Select the state where the project is located.
- **Zip**. Enter the zip code for the project. You can enter the number in the 5-digit ZIP Code format (93013, for example) or in ZIP + 4 format (93013-2931, for example).
- **County**. Enter the county where the project is located.
- **Timezone\***. Select the time zone for the project. This time zone will determine time stamps on items throughout the project.
- **Latitude** and **Longitude**. If you want weather to be populated for the project, enter the exact GPS coordinates of your job site. For more information, see [Which weather providers are supported by Procore?](/faq-which-weather-providers-are-supported-by-procore) and [How do I determine the latitude and longitude values of an address?](/faq-how-do-i-determine-the-latitude-and-longitude-values-of-an-address)
- **Region:** Select the region for your project. These options are managed in the Company level Admin tool. See [Add a Custom Project Region](/product-manuals/admin-company/tutorials/add-a-custom-project-region).
- **Office:** Choose the office that is managing this project. See [Add an Office Location](/product-manuals/admin-company/tutorials/add-an-office-location).
- **Phone**. Enter the phone number of the primary contact for the job site.
- **Fax**. Enter the fax number where faxes should be sent for the project.

### Dates

- **Start Date\*:** This represents the date the contract for the project was signed and also will be used to calculate construction volume. Select a new date if necessary.
- **Actual Start Date:** This represents the actual date that the project started and is displayed on the Portfolio page. Select a date from the calendar to manually update the 'Actual Start Date'. 
 *Notes:*

 - If a schedule has been uploaded to the project's Schedule tool, this field will inherit the start date value from the uploaded schedule. See [Upload a Project Schedule File to Procore's Web Application](/product-manuals/schedule-project/tutorials/upload-a-project-schedule-file-to-procores-web-application).
 - If no schedule has been uploaded, the field will inherit the value that is entered in the 'Start Date' field
- **Completion Date\*:** This represents the date all parties agree the project meets or must meet "substantial completion" and also will be used to calculate construction volume. Select a new date if necessary.
- **Projected Finish Date:** This represents the actual date that the project finished and also will be displayed on the Portfolio page. Select a date from the calendar to manually update the 'Projected Finish Date'.   
 *Notes:*

 - If a schedule has been uploaded to the project's Schedule tool, this field will inherit the last schedule task from the uploaded schedule.
 - If no schedule has been uploaded, the field will inherit the value from the âCompletion Dateâ field
- **Warranty Start Date:** Select the start date for the construction 

 A *Contract Warranty* is a legal or implied contract that guarantees any work defects found in the original construction will be repaired during the specified warranty period.

 Contract Warranty.
- **Warranty End Date:** Select the end date for the construction 

 A *Contract Warranty* is a legal or implied contract that guarantees any work defects found in the original construction will be repaired during the specified warranty period.

 Contract Warranty.

### Advanced

- **Departments:** Choose one or more departments of your company that are working on this project. This will be reflected in the Timecard tool, Portfolio tool, and additional places throughout Procore depending on your settings. See [Add a Custom Department](/product-manuals/admin-company/tutorials/add-a-custom-department).
- **QuickBooks Customer:** If your company has an equivalent QuickBooksÂ® Desktop project for the project, enter the 'QB Customer Name' for the project exactly as it appears in your QuickBooksÂ® Desktop account. This allows you to transfer time entries from Procore to QuickBooksÂ® Desktop. See [Transfer Procore Time Entries to QuickBooksÂ® Desktop](/product-manuals/timesheets-company/tutorials/transfer-procore-timecard-entries-to-quickbooks-desktop) and [Export Time Entries from Procore to Import into QuickBooksÂ® Software](/product-manuals/timesheets-company/tutorials/export-timecard-entries-from-procore-to-import-into-quickbooks-software).
- **Copy Directory From:** Select one of the projects in your company's Procore account to copy the user and company information from that project's Directory into your current project's Directory tool. See [Copy Directory From One Project to Another](/product-manuals/admin-project/tutorials/copy-directory-from-one-project-to-another).
- **Use Tax Codes:**

 ##### Â Note

 The Tax Codes feature was designed for Procore customers in Australia, New Zealand, or Canada. However, the feature is available to all Procore customers. To learn more, see [How can I use tax codes on a Procore project?](/faq-how-can-i-use-tax-codes-on-a-procore-project)

- **Do not use Tax Codes:** Select this option if you do not want to use tax codes. This is the default setting for a Procore project.
- **Company Default:** Select this option to use the tax code that you specified as your company's default. See [Configure Tax Code Settings](/product-manuals/admin-company/tutorials/configure-tax-code-settings).
- **[Custom Tax Codes]:** Select one of the options if your company has created custom tax codes for use in your Procore company Account. See [Configure Tax Code Settings](/product-manuals/admin-company/tutorials/configure-tax-code-settings).

 ##### Â Tip

 **How do we ensure our projects and users apply the same dictionary setting set for our Procore company account?** In Procore, different dictionary settings can be applied at the Company, Project, and User level. If you want your project(s) and users(s) to apply the same dictionary setting as your company's Procore account, inform your project administrators and end users to always choose the *None Selected* option.

 - To change the setting for your company's Procore account, your Procore Administrator must send an email request to your Procore point of contact .
 - To change the setting for a specific project, select one of the available options from the 'Language-County' as described above.
 - To change the setting as an end user, see [Change Your Account Language in 'My Profile Settings'](/product-manuals/home-project/tutorials/change-your-account-language-in-my-profile-settings).
 - To learn more about the options for changing language settings, see [Can I change the language of my Company, Project, or User in Procore?](/faq-can-i-change-the-language-of-my-company-project-or-user-in-procore)
 - Procore's Drawings tool also allows users to choose the language when scanning drawings. For details, see [Can I change the language that Procore scans my drawings for?](/faq-can-i-change-the-language-that-procore-scans-my-drawings-for)

- **Enable Docusign.** See [Enable or Disable the DocuSignÂ® Integration on a Procore Project](/product-manuals/admin-project/tutorials/enable-or-disable-the-docusign-integration-on-a-procore-project)
- **Prevent Overbilling on this Project:** Place a mark in this checkbox if you want to prevent overbilling on invoices.   
 *Note:* If the 'Prevent Overbilling on All Projects' setting is enabled in the Company level Admin tool, this setting cannot be changed here for the project.
- **Non-Commitment Costs:** Place a mark in this checkbox if you want to show non-commitment costs on change events. If enabled, a new cost column will appear on Change Event line items that can be used to record approved costs that are not associated with a Commitment or Commitment Change Order. This column will be available as a configurable column.
- **Test Project:** Mark the checkbox if this project is being used for learning purposes only. See [What is a Test Project?](/faq-what-is-a-test-project)
- **Labor Productivity for Budget, Change Events, and Change Orders:** Place a checkmark in this box to enable several features in multiple tools that support the 'Procore Labor Productivity Cost' budget view. For details, see [Enable the Labor Productivity Features for Project Financials](/process-guides/resource-tracking-and-project-financials-setup-guide/enable-labor-productivity).
- **Enable ERP Job Cost Transaction Syncing:** If your company's Procore Administrator has enabled ERP job cost transaction syncing on the backend of Procore, place a mark in this checkbox to give your project team the ability to import job cost transactions from ERP into a Procore budget. To learn more, see [Enable ERP Job Cost Transaction Syncing on a Procore Project](/product-manuals/erp-integrations-company/tutorials/enable-erp-job-cost-transaction-syncing-on-a-procore-project).
- **Create Multiple PCIs:** If your company's Procore Administrator has enabled this setting on the backend of Procore, select this checkbox to allow your project team to export Procore PCCOs with multiple PCOs as individual PCIs to CMiC. See [Export a PCCO with Multiple PCOs as Individual PCIs to CMiC](/product-manuals/cmic/tutorials/export-a-pcco-with-multiple-pcos-as-individual-pcis-to-cmic).
- **Create Owner Change Orders:** If your company's Procore Administrator has enabled this setting on the backend of Procore, select this checkbox to allow your project team to export Procore PCCOs as OCOs to CMiC. See [Export a PCCO as an OCO to CMiC](/product-manuals/cmic/tutorials/export-a-pcco-as-an-oco-to-cmic).