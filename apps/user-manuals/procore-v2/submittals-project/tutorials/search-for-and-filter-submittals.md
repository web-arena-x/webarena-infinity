# Search for and Filter Submittals

Source: https://v2.support.procore.com/product-manuals/submittals-project/tutorials/search-for-and-filter-submittals

---

## Background

Because of the large number of submittals that can be created on a project, the project's Submittals tool offers search and filter functions that help you find a submittal or submittal package.

## Things to Consider

- **Required User Permissions:**

  - 'Read Only' level permissions or higher on the project's Submittals tool.
- **Additional Information:**

  - Any filters that you apply in a project's Submittals tool will stay applied for your current and future sessions in the same project until you clear the filters.
  - Search terms and applied filters respect each other's parameters. For example, if you apply one or more filters before starting a search, the search results only include items applicable to the filters.

## Steps

- Search for a Submittal
- Filter the Submittals Log
- Sort the Submittals Log

### Search for a Submittal

1. Navigate to the project's **Submittals** tool.
2. Click the **Items**, **Packages**, **Spec Sections**, or **Ball In Court** tab. See [Switch Between Submittals Views](/product-manuals/submittals-project/tutorials/switch-between-submittals-views).
3. Enter a word or phrase in the **Search** box and press ENTER on your keyboard (or click the  icon).

   The search feature supports the use of advanced search symbols. To learn more, see [What is an advanced search symbol in Procore?](/faq-what-is-an-advanced-search-symbol-in-procore)

   - **Title** Enter a full search term. *Examples:*

     - A search for the term 'alarm' would return submittals titled 'Fire Alarm System' and 'Security Alarm Sounder.'
     - A search for the term 'alarm' and 'system' would return submittals titled 'Fire Alarm System', 'Fire Alarm Cable', 'Security Alarm Sounder', and 'Security System Console'.
     - A search for the term 'cab', would return 'CAB Submittal', but the results would NOT include 'Fire Alarm Cable' or 'Telecommunications Cabinets.'
   - **Description** Enter a word or phrase.
   - **Submittal Number** Enter a full or partial submittal number.
   - **Package Number** Enter a full or partial submittal package number.
   - **Package Title** Enter a full or partial submittal package title.
   - **Spec Section** Enter a spec section number or a partial description.
4. To clear the search results, click the X at the end of the **Search** box.

### Filter the Submittals Log

1. Navigate to the project's **Submittals** tool.
2. Click the **Items**, **Packages**, **Spec Sections**, or **Ball In Court** tab. See [Switch Between Submittals Views](/product-manuals/submittals-project/tutorials/switch-between-submittals-views).
3. Click **Add Filter** and select one of the following options:

   - **Approver**. This reveals a list of any individuals who are named as Approver or Submitter in the 'Submittal Workflow' for your submittals. You can mark one or more checkboxes. See [Add a Submitter and Approvers to the Submittal Workflow](/product-manuals/submittals-project/tutorials/add-submitter-and-approvers-to-the-submittal-workflow).
   - **Ball In Court**. This reveals a list of any individuals who are currently designated as the 'Ball In Court' person on your submittals. You can mark one or more checkboxes.
   - **Created By**. This reveals a list of any individuals who have created a submittal. You can mark one or more checkboxes.
   - **Current Revision**. This reveals a checkbox where you can select 'Yes' to view only current revisions of the submittals.
   - **Division**. This reveals a list of divisions connected to the submittals. A division is a grouping of spec sections. You can mark one or more checkboxes.
   - **Location**. Select *Location* from the drop-down list. Then, you have these options to narrow your selection to specific sub-locations:

     - If you want to include the project's sub-locations in your search, mark the â**Include Sub-locations** checkbox. To ignore sub-locations, remove the checkmark. See [How do I filter by multi-tiered locations](/faq-how-do-i-filter-items-by-multi-tiered-locations)
     - If you want to include only a specific location (or locations) in your search, mark the corresponding checkboxes. *Note*: For the checkboxes above to appear as selections, at least one (1) submittal on your project must be associated with a sub-location.
   - **Private**. This reveals checkboxes where you can select 'Yes' or 'No' to choose whether you want to view Submittals marked 'Private'. See [Mark a Submittal as Private](/product-manuals/submittals-project/tutorials/mark-a-submittal-as-private).
   - **Received From**. This reveals a list of individuals who have been selected as Received From on your submittals. You can mark one or more checkboxes.
   - **Response**. This reveals a list of submittal responses. You can mark one or more checkboxes. See [Manage Custom Submittal Responses](/product-manuals/submittals-project/tutorials/manage-custom-submittal-responses).
   - **Responsible Contractor**. This reveals a list of companies that have been named as the Responsible Contractor on your submittals. You can mark one or more checkboxes.
   - **Spec Section**. This reveals a list of sections from your project's spec book. You can mark one or more checkboxes.
   - **Status**. This reveals a list of statuses (e.g., Open, Draft, and Closed). You can mark one or more checkboxes.
   - **Sub Job**. This reveals a list of sub jobs on the project (if enabled). You can mark one or more checkboxes. See [Enable Sub Jobs on Projects for WBS](/process-guides/company-administration-work-breakdown-structure-guide/enable-sub-jobs-for-projects).
   - **Submittal Manager**. This reveals a list of individuals who have been named as a [submittal manager](/glossary-of-terms).
   - **Submittal Package**. This reveals a list of all submittal packages. You can mark one or more checkboxes. See [Create a Submittal Package](/product-manuals/submittals-project/tutorials/create-a-submittal-package).
   - **Type**. This reveals a list of submittal types. You can mark one or more checkboxes. See [Create Custom Submittal Types](/product-manuals/admin-company/tutorials/create-custom-submittal-types).
4. Press ESC on your keyboard to view the filtered list of submittals.
5. *Optional:* Repeat the steps above to add more filters.
6. To clear one filter, click the X next to its name.  
    OR  
    To clear all filters, click **Clear All**.

### Sort the Submittals Log

1. Navigate to the project's **Submittals** tool.
2. Click the **Items**, **Packages**, **Spec Sections**, or **Ball In Court** tab. See [Switch Between Submittals Views](/product-manuals/submittals-project/tutorials/switch-between-submittals-views).
3. Click one of the following column names to sort the list of submittals by data from the corresponding fields:

   - Spec Section
   - #
   - Title
   - Type
   - Status
   - Responsible Contractor
   - Submit By
   - Received From
   - Received Date
   - Due Date
   - Distributed Date
   - Custom Fields ('Number', 'Date', 'Checkbox', and 'Plain Text')  
     *Note:* Columns for custom fields are hidden by default. See [Customize the Column Display in the Submittals Tool](/product-manuals/submittals-project/tutorials/customize-the-column-display-in-the-submittals-tool) for information about showing, hiding, and rearranging columns in the submittals log.
4. *Optional:* Click the column name again to switch the results between ascending and descending order.