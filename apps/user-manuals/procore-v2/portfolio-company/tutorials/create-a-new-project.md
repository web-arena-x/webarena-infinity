# Create a New Project

Source: https://v2.support.procore.com/product-manuals/portfolio-company/tutorials/create-a-new-project

---

## Background

The Project Creation Assistant gives you the ability to quickly create Procore projects and efficiently upload key project documents (e.g., project drawings and specifications).

## Things to Consider

- **Required User Permissions:**

  - 'Admin' level permissions on the Company level Directory tool.  
     OR
  - 'Read Only' or higher on the company's Portfolio tool with the privilege to create new projects. See [Allow Users to Create New Projects](/product-manuals/directory-company/tutorials/allow-users-to-create-new-projects).
- **Prerequisites:**

  - *If your company is planning to use the Project level Bidding tool*, complete the steps in [Add Project Bid Types](/product-manuals/admin-company/tutorials/add-a-custom-bid-type).
  - *If your company is planning to organize its projects in the company's Programs tool*, complete the steps in [Add Programs](/product-manuals/admin-company/tutorials/add-a-custom-program).
  - *If your company uses a classification system to organize your projects by type*, complete the steps in [Add a Custom Project Types](/product-manuals/admin-company/tutorials/add-a-custom-project-type).
- For companies using the ERP Integrations tool:

  - **Do NOT use the steps in this article. Refer the article for your** [integrated ERP system](/glossary-of-terms) **instead:** Add a Procore Project to your ERP Software
- **Limitations:**

  - Procore projects cannot be deleted. However, you can change its status of Inactive. For instructions, see [Change a Project's Status to Active or Inactive](/product-manuals/admin-project/tutorials/change-a-projects-status-to-active-or-inactive).
  - When your company's Procore account meets the limit defined by your account's Maximum # of Active Projects, the Create Project button is automatically disabled.
- **Troubleshooting:**

  - If you are not able to create a new project, see [Why am I unable to create or activate Procore projects?](/faq-why-cant-i-create-or-activate-procore-projects)

    - Procore does *not* limit the number of active or inactive projects on an account.

## Steps

Use the Project Creation Assistant to add a new project. These are the steps:

1. Launch the Project Creation Assistant
2. Add Project Details
3. Add and Remove Tools in the Project Toolbox
4. Add Project Cost Codes
5. Update Directory
6. Upload Drawings
7. Upload Specifications
8. Upload Schedule

### Launch the Project Creation Assistant

1. Navigate to the company's **Portfolio** tool.
2. Click **Create Project**.

### Add Project Details

1. Under **Project Information**, complete the following information as necessary:  
   *Note*: An asterisk (\*) below indicates a required field.

   - **Template**. Choose a project template from the list or choose 'Do Not Apply a Template'.  
     *Notes:*

     - This field is only visible and available when the project templates feature is enabled on your company's Procore account.
     - To select a template from the list, the desired project template must be active. See [Configure a Project Template](/product-manuals/portfolio-company/tutorials/configure-a-project-template).
     - If a template is already chosen, your company has set it as [the default](/product-manuals/admin-company/tutorials/manage-project-templates) for new projects. You can still select a different template from the list.

     Template (Project)
   - **Name**\*. Enter a name for the project. This is a required field.

     Name (Project)\*
   - **Code**. Enter a project code to help your team identify and locate the project in Procore. This should be an abbreviation of the 'Project Name.'

     *Note:* For projects using the Document Management tool, the 'Code' entered above integrates with the naming standards you specify in the tool's Configure Settings page. To learn more, see [What is the 'Code' field on the project creation page?](/faq-what-is-the-code-field-on-the-project-creation-page)

     Code
   - **Total Value**. Enter the anticipated project value upon completion. Enter a value to the nearest whole number. For example, if your project's estimated value is $18 million dollars, enter $18,000,000.00 in the box.

     EstimatedÂ Value
   - **Start Date**. This represents the date that the project will start and also will be used to calculate construction volume.

     Start Date
   - **Completion Date**. Select the anticipated project completion date. Once the project has begun, you can compare this field against the actual finish date.

     Completion Date
   - **Stage**. Select a project stage from the list. These selections are created with the company's Admin tool. See [Add Custom Project Stages to Your Company](/product-manuals/admin-company/tutorials/add-a-custom-project-stage).

     Stage (Project)
   - **Type**. Select a project type from the drop-down list. These selections are created in the company's Admin tool. See [Add a Custom Project Type](/product-manuals/admin-company/tutorials/add-a-custom-project-type).

     Type (Project)
   - **Project Number**. Enter a unique project ID or number to differentiate it from other company projects.

     Project Number
   - **Square Feet**. Enter the project's square footage.

     Square Feet
   - **Store Number**. Enter the store number for the project. This field is only visible and available if the 'Include Store Number and Designated Market Area' setting is enabled in the 'Default Project Settings' section of the Company Admin tool.

     Store NumberÂ
   - **Description**. Enter a brief project summary.

     Description (Project)
   - **Active**. Click the toggle to the ON position to set the project to *Active,* or click the toggle to the OFF position to set the project to *Inactive*.

     Active
   - **Logo**. Drag and drop an image or click the area to select an image file to upload as a logo for the project. The file should have dimensions of 200 x 70 pixels, must not exceed the 3MB maximum, and must be saved in the GIF, JPG, or PNG file format. To change this logo at a later time, see [Update General Project Information](/product-manuals/admin-project/tutorials/update-general-project-information).

     Logo (Project)
   - **Photo**. Drag and drop an image or click the area to select an image file to upload as the project photo. The file should have dimensions of 200 x 100 pixels, must not exceed the 3MB maximum, and must be saved in the GIF, JPG, or PNG file format. To change this photo at a later time, see [Update General Project Information](/product-manuals/admin-project/tutorials/update-general-project-information) or [Add a Project Photo.](/product-manuals/photos-project/tutorials/set-a-project-photo)

     Photo (Project)
   - **Delivery Method.** Define how stakeholders will collaborate across each phase of the project including planning, design, and build. For example, Design-Bid-Build, Design-Build, or Construction Manager at Risk.
   - **Project Sector.** Categorize the project based on the facility's function or purpose, such as Retail, Roadwork, or Multifamily.
   - **Work Scope.** Categorize the work according to scope, such as New Construction or Renovation/Alteration.
2. Under **Project Location**, complete the following information as necessary:  
   Some fields might not appear, and additional fields may be required if your company's account is customized.

   - **Country**. Select the country from the drop-down list.

     Country
   - **Timezone**. Choose the correct time zone for the project from the drop-down list. This time zone will determine time stamps on items in the project.

     Timezone
   - **Address**. Enter the address for the project's job site.*Notes*:

     - Procore uses a third-party service to automatically determine the County name based on the 'Address' and 'ZIP' fields. Since this is auto-determined, there is no data-entry for County in the Create New Project page. To change the County value, see [Update General Project Information](/product-manuals/admin-project/tutorials/update-general-project-information).
     - ***Important!*** If you want weather data to be shown in the project's Home and Daily Log tools, you will need to enter Latitude and Longitude coordinates for the address after the project is created. See [Update General Project Information](/product-manuals/admin-project/tutorials/update-general-project-information) and [How do I determine the latitude and longitude values of an address?](https://support.procore.com/faq/how-do-i-determine-the-latitude-and-longitude-values-on-an-address)

     Address (Project)
   - **City**. Enter the full city name for the project.*Note*: Do not abbreviate the city name.

     City
   - **State**. Select the state for the project from the drop-down list.

     State
   - **Zip**. Enter the ZIP/postal code for the project.*Note*: Procore uses a third-party service to automatically determine the County name based on the 'Address' and 'ZIP' fields. Since this is auto-determined, there is no data-entry for County in the Create New Project page. To change the County value, see [Update General Project Information](/product-manuals/admin-project/tutorials/update-general-project-information).

     ZIP
   - **Phone**. Enter in the main contact phone number for the job site. Team members will be able to see this phone number.

     Phone (Job)
   - **Fax**. Enter the onsite fax number (if available). This gives team members the ability to see and use the project's fax number when needed.

     Fax (Job)
   - **Designated Market Area**. Enter the designated market area for the project.*Note*: This field is only visible and available if the 'Include Store Number and Designated Market Area' setting is enabled in the 'Defaults' section of the Company Admin tool.

     Designated Market Area
3. Under **Advanced**, complete the following information as necessary:

   - **Office**. Choose the office that is managing this project. These selections are created in the company's Admin tool. See [Add an Office Location](/product-manuals/admin-company/tutorials/add-an-office-location).

     Office
   - **Departments**. Select one or more departments who have responsibility for the project. These selections are created with the company's Admin tool. See [Custom Company Projects](/product-manuals/admin-company/tutorials/configure-your-company-settings).*Note*: These departments appear in the Timecard and Directory tool, and may also appear in other Procore tools depending on your company's specific configuration.

     Departments
   - **Program**. Select the program to classify your project under. âThese selections are created with the company's Admin tool. See [Add Programs](/product-manuals/programs-company/tutorials/add-programs).*Note*: You can view your projects by program using the Programs tool.

     Program
   - **Flag**. Select a color for the project flag from the drop-down list. The system's default color selections are: RED, YELLOW, and GREEN. This allows you to visually organize your projects (e.g., you might want to flag internal projects as RED and commercial projects as GREEN).

     Flag (Project)
   - **Region**. Select the region you want to classify your project into. These selections are created with the company's Admin tool. See [Add Project Regions](/product-manuals/admin-company/tutorials/add-a-custom-project-region).*Note*: You can view projects by region in the Portfolio tool.

     Region
   - **Bid Type**. Select the bid type from the list. These selections are created with the company's Admin tool. See [Add a Custom Bid Type](/product-manuals/admin-company/tutorials/add-a-custom-bid-type).

     Bid Type
   - **Owner Type**. Select the owner type from the drop-down list. These selections are created in the company's Admin tool. See [Add a Custom Owner Type](/product-manuals/admin-company/tutorials/add-a-custom-owner-type).

     Owner Type
   - **Parent Project**. Select the name of the parent project in Procore from the drop-down list. In Procore, a *parent job* is a Procore project that has been designated as the 'parent' project for one or more related project(s) in Procore's Portfolio tool. To learn more, see [What's the difference between a job, a parent job, and a sub job?](/faq-what's-the-difference-between-a-job-a-parent-job-and-a-sub-job)

     Parent (Project)
   - **Warranty Start Date**. Select the start date for the construction [contract warranty](/glossary-of-terms).

     Warranty Start Date
   - **Warranty End Date**. Select the end date for the construction [contract warranty](/glossary-of-terms).

     Warranty End Date
   - **Copy Directory From**. Select one of the projects in your company's Procore account to copy the user and company information from that project's Directory into your current project's Directory tool. See [Copy Directory From One Project to Another](/product-manuals/admin-project/tutorials/copy-directory-from-one-project-to-another).

     Copy Directory From
   - **Language-Country**: Select the language you want the project to display in.*Note:* If 'None Selected' is chosen, the project's language will match the company's language for users that have not changed their user account's language in 'My Profile Settings'. See [Can I change the language of my Company, Project, or User in Procore?](/faq-can-i-change-the-language-of-my-company-project-or-user-in-procore)

     Language - Country
   - **Test Project**: Mark the checkbox if this project is being used for learning purposes only. See [What is a Test Project?](/faq-what-is-a-test-project)

     Test Project
   - **Create Multiple PCIs.** If your company's Procore Administrator has enabled this setting on the backend of Procore, select this checkbox to allow your project team to export PCCOs with multiple PCOs as individual PCIs to CMiC. See [Export a PCCO with Multiple PCOs as Individual PCIs to CMiC](/product-manuals/cmic/tutorials/export-a-pcco-with-multiple-pcos-as-individual-pcis-to-cmic).

     Create Multiple PCIs
   - **Create Owner Change Orders.** If your company's Procore Administrator has enabled this setting on the backend of Procore, select this checkbox to allow your project team to export PCCOs as OCOs to CMiC. See [Export a PCCO as an OCO to CMiC](/product-manuals/cmic/tutorials/export-a-pcco-as-an-oco-to-cmic).

     Create Owner Change Orders

     ### ERP Project Creation

     Under **ERP Integration**, do the following (*Note: this step is only relevant to companies that are integrated with certain ERP systems*):

     1. **Allow project to be synced with ERP**. Leave this checkbox marked if you plan to sync any part of the project's financials with your ERP software. This will ensure that the ERP Standard cost code list will be available to select from when configuring your Project Level cost codes.

     ##### Â Important

     - This checkbox will be marked by default if your company has an available set of ERP cost codes, unless the template the project is created from does not have this box marked.
     - If you plan to sync your new Procore project with your ERP software you MUST leave this checkbox marked. If you un-mark this box, you will not be able to re-mark it later if cost codes from a different Company Level list have been copied to the Project Level list in the Project Admin tool.

- Click **Create Project**.

### Add and Remove Tools in the Project Toolbox

Tools selected on this page will appear in the project's tools menu, while tools that are not selected will not appear in the tools menu, and cannot be used.  
*Note*: If you want to change which tools are available later, you can do so by navigating to the project's Admin tool. See [Add and Remove Project Tools](/product-manuals/admin-project/tutorials/add-and-remove-project-tools).

1. Make sure **Tools** is highlighted.  
   ***Important!*** If the **Tools** link does NOT appear in the Project Creation Assistant, it is because the project template that you applied to your new project already determined the project's tools.
2. Add and remove tools for the project as follows:

   - **To add a tool individually**: Mark the checkbox next to box that corresponds to desired tool.
   - **To add all available tools within a category**: Mark the checkbox next to the category name.  
     OR  
     **To add all available tools from all categories**: Mark the checkbox next to **Select All**.  
     *Note*: Clicking the checkbox again will deselect all tools.
   - **To remove a tool**: Clear the checkbox for that tool.
3. If you want to rearrange the order of tools on the project's toolbar for all users:

   1. Drag-and-drop a tool to move it to a new position in the product category.
4. Click **Select Tools**.   
   *Note*: The system displays a GREEN banner to confirm your settings were saved.

### Add Project Cost Codes

##### Â Notes

- This page is only available in the Project Creation Assistant if your Procore account has the ERP Integrations tool enabled.
- Cost codes are managed in Procore's [Work Breakdown Structure](/product-manuals/work-breakdown-structure/) as segment items in the 'Cost Code' segment. See [What are segments and segment items?](/faq-what-are-segments-and-segment-items)

1. Make sure **Cost Code** is highlighted.  
   *Notes*:

   - For information about Procore's default cost codes, see [What are Procore's default cost codes?](/faq-what-are-procores-default-cost-codes)
   - If your company account has enabled the Company level ERP Integrations tool, you will have the option to select the cost code list for your [integrated ERP system](/glossary-of-terms) from a **Source** drop-down list.
   - To learn about cost codes for your specific integrated ERP system, see [Configure Cost Code Preferences for ERP Integrations](/product-manuals/admin-company/tutorials/configure-cost-code-preferences-for-erp-integrations).
   - If your company account has enabled the Procore + ViewpointÂ® SpectrumÂ®, you must use the Standard Cost Code List. See [Add ViewpointÂ® Vistaâ¢ Standard Cost Codes to a Project](/product-manuals/vista/tutorials/add-viewpoint-vista-standard-cost-codes-to-a-project).
2. Choose from these options (A) or (B):

   1. If your Procore company account is NOT configured to work with an [integrated ERP system](/glossary-of-terms), you will see the **Standard Cost Code List** page (pictured above). Choose from these options:

      - To copy only selected codes from Procore's standard cost code list:

        1. Expand the desired division folder(s).
        2. Highlight the desired cost codes.
        3. Click **Copy Selected Codes**.
      - To copy all of the codes from Procore's standard cost code list:

        1. Click **Copy All Codes**.  
           The system reveals the following confirmation message: "Once you add this cost code, the source list cannot be changed."
        2. Click **OK** to acknowledge the confirmation message.   
           This moves all the codes in the **Standard Cost Code List** to the **Project Cost Codes** list.

           ##### Â Tip

           - **Need to add, edit, or delete your cost codes list at a later time?** In Procore, cost codes and cost types are segment items on the default 'Cost Code' segment in [Work Breakdown Structure (WBS)](/product-manuals/work-breakdown-structure/). To learn how to manage your company level cost codes in Procore's WBS, see [Add Company Cost Codes](/process-guides/company-administration-work-breakdown-structure-guide/add-company-cost-codes). For companies using Procore with a supported [integrated ERP system](/glossary-of-terms), be sure to review [Why can't I create WBS custom segments?](/faq-why-cant-i-create-wbs-custom-segments)