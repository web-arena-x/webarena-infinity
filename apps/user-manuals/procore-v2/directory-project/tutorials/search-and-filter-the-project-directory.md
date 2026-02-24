# Search and Filter the Project Directory

Source: https://v2.support.procore.com/product-manuals/directory-project/tutorials/search-and-filter-the-project-directory

---

## Things to Consider

- [Required User Permissions](/product-manuals/directory-project/permissions)
- The search function respects any selected filter parameters and only searches for items within the filtered results.
- Filters are only supported on the Users and Companies tabs.
- The 'Contacts' and 'Inactive Contacts' tabs are populated with contacts created from one or more projects on supported tools. See [What is a 'contact' in Procore and which project tools support the concept?](/faq-what-is-a-contact-in-procore-and-which-project-tools-support-the-concept)
- The search feature supports the use of advanced search symbols. To learn more, see [What is an advanced search symbol in Procore?](/faq-what-is-an-advanced-search-symbol-in-procore)
- **If your company has enabled the ERP Integrations tool:**

 - You will have the added ability to filter the **Companies** view by the cost codes for your integrated ERP system.

## Steps

- Legacy Project Directory

 - Search the Project Directory
 - Add Filters to the Project Directory
 - Group Users by Company in the Project Directory
- Beta Project Directory

 - Search the Project Directory (Beta)
 - Filter the Project Directory (Beta)
 - Sort the Project Directory (Beta)

### Legacy Project Directory Experience

#### Search the Project Directory

1. Navigate to the Project level **Directory** tool.
2. Click the desired tab.
3. Enter a keyword into the search box, then press ENTER. See [What fields are searched in the Directory tool?](/faq-what-fields-are-searched-in-the-directory-tool)

#### Add Filters to the Project Directory

1. Navigate to the Project level **Directory** tool.
2. Click the **Users** or **Companies** tab.
3. Select **Add Filter** drop-down list:

   - **Users**

     - **Permission Template (Default)** This filters the list of users by the default permission template that is assigned to the end user. 
       *Note:* Only users with 'Admin' level permissions on the Project level Directory can apply this filter.
     - **Trades**. This filters the list of users by the Trade associated with the user's company record. See [Add a Custom Trade](/product-manuals/admin-company/tutorials/add-a-custom-trade).
   - Companies

     - **[Project Name] Cost Codes**. This filters results by the cost codes in the 'Cost Code' segment of Procore's [Work Breakdown Structure](/product-manuals/work-breakdown-structure/).
     - If you have an ERP Integration, choose **[ERP Integration Name] Cost Code** to filter by the cost codes that have been configured for your specific integrated ERP system.
     - **Trades**. This filters the list of companies by the Trade associated with the company record. See [Add a Custom Trade](/product-manuals/admin-company/tutorials/add-a-custom-trade).

#### Group Users by Company in the Project Directory

1. Navigate to the Project level **Directory** tool.
2. Click the **Users** tab.
3. From the **Group By** list, choose **Company.**

### Beta Project Directory Experience

##### Â In Beta

A redesigned version of the Project Directory is currently in beta and can be enabled with [Procore Explore](/product-manuals/admin-company/tutorials/manage-features-with-procore-explore).

#### Search the Project Directory (Beta)

1. Navigate to the Project level **Directory** tool.
2. Click the desired tab.
3. Enter a keyword into the search box, then press ENTER.

#### Filter the Project Directory (Beta)

1. Navigate to the project's **Directory** tool.
2. Click the **Users** or **Companies** tab.
3. Click the **filters** icon.
4. Select to filter by the following fields:

   - Users

     - User Status
     - Permissions Template (Assigned)
     - Trade
   - Companies

     - Company Status
     - Cost Code
     - Trade
5. To clear filters, click the 'x' on the individual filter or click **Clear all Filters**.

#### Sort the Project Directory (Beta)

1. Navigate to the project's **Directory** tool.
2. Click the desired tab.
3. Click the column header to sort by that column.

   - Click again to switch between ascending or descending order:

     - **Ascending**
     - **Descending**
   - You can sort by the following columns:
   - Users

     - Name
     - Job Title
     - Company
     - Permissions Template
   - Companies and Distribution Groups

     - Name