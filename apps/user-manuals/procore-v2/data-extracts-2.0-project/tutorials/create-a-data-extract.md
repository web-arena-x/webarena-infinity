# Create a Data Extract

Source: https://v2.support.procore.com/product-manuals/data-extracts-2.0-project/tutorials/create-a-data-extract

---

### Background

The Data Extracts 2.0 tool allows users to create, customize, and export extracts. When creating an extract, you can include data captured by specific project level Procore tools, specify the desired column layout, and define how to filter and group the data. After an extract is created, you can download it to your computer.

### Things to Consider

- [Required User Permissions](/product-manuals/data-extracts-2.0-project/permissions)
- **Additional Information:**

 - You can only extract data from active projects. See [Change a Project's Status to Active or Inactive](/product-manuals/admin-project/tutorials/change-a-projects-status-to-active-or-inactive).
 - For details on the project level Procore tools from which data can be extracted, see [Which Procore tools can I extract project data from using the Data Extracts 2.0 tool?](/faq-which-procore-tools-can-i-extract-project-data-from-using-the-data-extracts-2.0-tool)
 - Extracts are only visible and available to the individual who created them.
 - You must select at least one Procore tool to create an extract.
 - You must select at least one item for each selected Procore tool to create an extract.

### Steps

1. Navigate to the project level **Data Extracts** tool. 
   The Data Extracts page displays a list of all extracts for the project. When you access this page for the first time, the list will be empty.
2. Click **Create** in the top right corner.
3. Enter the following information: 
   *Note*: An asterisk (\*) denotes a required field.

   - **Name\*.** Enter a unique name for the extract. The name must be at least three characters.
   - **Include Table of Contents.** Mark this checkbox to include a table of contents in the extract.
   - **Tools.** Select one or more project level Procore tools for which you are creating the extract. 
     *Note:* To view tools, you must have 'Admin' level permissions or higher for the relevant tool.
4. Click **Create**.
5. Under the **General** tab, click on the subtab for the tool you want to configure.
6. Configure your extract using the available options:

   - **Settings.** Configure the settings for the selected tool. See [Configure Settings for Procore Tools in Data Extracts](/product-manuals/data-extracts-2.0-project/tutorials/configure-settings-for-procore-tools-in-data-extracts).
   - **Filters.** Click the filters icon to select what you would like to filter by. See [Configure Filters for Data Extracts](/product-manuals/data-extracts-2.0-project/tutorials/configure-filters-for-data-extracts).
   - **Group By.** Click the **Group By** button to group the tool's data by the specified option(s) (e.g., you may want to group data by the responsible contractor). See [Configure Grouping for Data Extracts](/product-manuals/data-extracts-2.0-project/tutorials/configure-grouping-for-data-extracts).
   - **Configure.** Click the configure icon to configure the columns on your extract. See [Configure Columns for Data Extracts](/product-manuals/data-extracts-2.0-project/tutorials/configure-columns-for-data-extracts).
7. Mark the checkbox next to each item to include specific items in your extract. 
   OR Mark the checkbox in the first column heading of the tool's table to include all items in your extract.

   ##### NOTE

   For the Documents tool, you can click on a folder to select specific files.

- Repeat step 5 - 7 above for each of the selected tools.
- Click **Extract**.

##### NOTE

- You can track the status of the extraction on the **Data Extracts** page.
- Once the extraction is complete, you will receive an email notification to download the extract. See [Download a Data Extract](/product-manuals/data-extracts-2.0-project/tutorials/download-a-data-extract).