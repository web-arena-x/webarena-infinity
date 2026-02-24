# Search for and Filter RFIs - Procore

Source: https://support.procore.com/products/online/user-guide/project-level/rfi/tutorials/search-for-and-filter-rfis

---

## Objective

To use the search, filter, and sort options to locate RFIs.

## Things to Consider

- **Required User Permissions:**
  - 'Read Only' level permissions or higher on the project's RFIs tool.
- **Additional Information:**
  - Use the search tool to further narrow the displayed results. The search tool respects any selected filter parameters and will only search for items within the filtered results.
  - The filters that you apply (by selecting items in the Add a Filter drop-down list) are persistent and will be retained for your next session, unless you click **Clear All**.

## Steps

- [Search for an RFI](#Search_for_an_RFI "Search for and Filter RFIs")
- [Filter the RFIs List](#Filter_the_RFIs_List "Search for and Filter RFIs")
- [Sort the RFIs Log](#Sort_the_RFIs_Log "Search for and Filter RFIs")

### Search for an RFI

1. Navigate to the project's **RFIs** tool.
2. Click the **Items** tab.
3. Enter a word or phrase in the **Search** box and press ENTER on your keyboard or click the ![icon-search.png](https://support.procore.com/@api/deki/files/90727/icon-search.png?revision=1&size=bestfit&width=15&height=15) icon.

   The search feature supports the use of advanced search symbols. To learn more, see [What is an advanced search symbol in Procore?](https://support.procore.com/faq/what-is-an-advanced-search-symbol-in-procore "What is an advanced search symbol in Procore?")

     
   ![search-rfis.png](https://support.procore.com/@api/deki/files/75073/search-rfis.png?revision=1)  
     
   The following fields are searchable in the RFIs tool:
   - Number
   - Subject
   - Question
   - Response

**SUPERUSER ONLY**

The system also searches the **Reference** field. The reference field is used only by a limited number of customers.

When using the asterisk (\*) in a search query, it can only be used after a term. For example, door\* would find *door*, *doors*, *doorframe*, *doorframes*, and *doorway*. It cannot be used before a term (e.g., \*.pdf) or inside a term (e.g., "Hollow\*Doorframe" would not search for *Hollow Metal Doorframe* or *Hollow Wooden Doorframe*).

### Filter the RFIs List

1. Navigate to the project's **RFIs** tool.
2. Click the **Items** tab.
3. Click the**filter** ![icon-filter2.png](https://support.procore.com/@api/deki/files/280258/icon-filter2.png?revision=1&size=bestfit&width=17&height=17) icon and select from the following options:
   - **Revision.**Filters the list by current revisions OR by all revisions including outdated RFIs.
   - **Status**. Filters the list by the status of the RFI. *Note:* this does NOT include RFIs in the recycle bin.
   - **Responsible Contractor**. Filters the list by the contractor or subcontractor with responsibility for completing the work related to the RFI.
   - **Received From**. Select the person from whom the RFI was received.
   - **Assignees**. Select the name(s) of the Assignees to only show  RFIs assigned to those individuals.
   - **RFI Manager**. Filters the list by the [RFI Manager](../../../../../../references/construction-management/glossary-of-terms.md#RFI_Manager_(Coming_Soon) "Glossary of Terms").
   - **Ball In Court**. Select the name(s) of a [Ball In Court](../../../../../../references/construction-management/glossary-of-terms.md#Ball_In_Court "Glossary of Terms") person.
   - **Overdue**. Select *Overdue* and then mark the Yes checkbox to narrow you selection to overdue RFIs.
   - **Location**. Select *Location* from the drop-down list. Then, you have these options to narrow your selection to specific sub-locations:
     - If you want to include the project's sub-locations in your search, mark the ​**Include Sub-locations**checkbox. To ignore sub-locations, remove the checkmark. See [How do I filter by multi-tiered locations?](https://support.procore.com/faq/how-do-i-filter-items-by-multi-tiered-locations "How do I filter by multi-tiered locations?")
     - If you want to include only a specific location (or locations) in your search, mark the corresponding checkboxes.   
       *Note:* For the checkboxes above to appear as selections, at least one (1) submittal on your project must be associated with a sub-location.
   - **Cost Code**. Select a cost code to limit the log to only RFIs associated with the selected code.
   - **RFI Stage**. Select RFI Stage and mark one or more checkboxes from the list to narrow the list to your selections.
   - **Created By**. Mark the checkboxes that correspond to the desired RFI creators.
   - ##### In Beta

     This feature is currently in beta for Procore customers. See [User Guide: Procore Connect for RFIs](../../connection-manager/tutorials/user-guide-procore-connect-for-RFIs.md).

     When projects are connected using the [**Connection Manager**](https://support.procore.com/products/online/user-guide/project-level/connection-manager/overview "Connection Manager - Overview") tool, two more options will appear to identify RFIs linked to External RFIs:

     - A filterable column titled **Linked To**.
     - A checkbox filter titled **Linked to External RFIs.**
4. Press ESC on your keyboard to view the filtered list of RFIs.
5. *Optional:*Repeat the steps above to add more filters.
6. To clear one filter, click the X next to its name.  
   OR  
   To clear all filters, click **Clear All**.

### Sort the RFIs Log

1. Navigate to the project's **RFIs** tool.
2. Click the **Items** tab.
3. Click one of the following column names to sort the list of RFIs by data from the corresponding fields:
   - #
   - Subject
   - Responsible Contractor
   - Received From
   - Date Initiated
   - RFI Manager
   - Due Date
   - Closed Date
   - Schedule Impact
   - Cost Impact
   - Cost Code
   - Status
   - Location
   - Assignee
   - Ball-in-Court
   - Custom Fields ('Number', 'Date', 'Checkbox', and 'Plain Text')  
     *Note:* Columns for custom fields are hidden by default. See [Customize the Column Display in the RFIs Tool](https://support.procore.com/products/online/user-guide/project-level/rfi/tutorials/customize-the-column-display-in-the-rfis-tools "Customize the Column Display in the RFIs Tool") for information about showing, hiding, and rearranging columns in the RFIs list.  
       
     ![switch-column-order.png](https://support.procore.com/@api/deki/files/75075/switch-column-order.png?revision=1)
4. *Optional:* Click the column name again to switch the results between ascending and descending order.

## See Also

- [View RFIs](https://support.procore.com/products/online/user-guide/project-level/rfi/tutorials/view-rfis "View RFIs")
- [Create New Custom Fields](https://support.procore.com/products/online/user-guide/company-level/admin/tutorials/create-new-custom-fields "Create New Custom Fields")