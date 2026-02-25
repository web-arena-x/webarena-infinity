# Add Segment Items

Source: https://v2.support.procore.com/product-manuals/admin-company/tutorials/add-segment-items

---

## Background

A *segment* is a discrete category that an organization uses to break down its work into manageable components. A *segment item* is one of many distinct items in a segment. After creating a segment, you can add an unlimited number of segment items to it.

## Things to Consider

- **Required User Permissions**:

 - 'Admin' level permissions on the Company level Admin tool.
- **Additional Information:**

 - Segment items are placed into the active state upon creation. If you don't want your company's project users to have access to a specific segment item, you can [Deactivate Segment Items](/process-guides/company-administration-work-breakdown-structure-guide/deactivate-segment-items).
 - 'Code' and 'Description' are required fields.
- **Limitations:**

 - **For customers using the Company level ERP Integrations tool**The default segments in WBS are compatible with Procore's tool. However, some integrations do NOT yet support custom segments.
 - **For customers who have independently developed or purchased a third-party solution to integrate with Procore**To take advantage of the custom segment capabilities associated with WBS, any existing API integrations that you have independently developed or purchased to interact with Procore must be updated to support Procore's new WBS API.

 - In a flat segment, duplicate entries in the 'Code' field are NOT permitted.
 - In a tiered segment, duplicate entries in the 'Code' field are NOT permitted when the segment items are children of the same parent segment.
 - There are no character limits or other limitations on entries in the 'Description' field.
 - There is no limit on the number of segment items you can add.

    - Custom Segments are NOT supported with the ERP Integrations tool.

## Prerequisites

- [Add Custom Segments](/process-guides/resource-tracking-and-unit-quantity-based-budget-setup-guide/add-custom-segments)

## Steps

1. Navigate to the Company level **Admin** tool.
2. Under 'Company Settings', click the **Work Breakdown Structure** link.
3. In the 'Segments' table, click the segment that you want to work with.

       

   ##### Â Tips

   - **Where are my individual cost codes and cost types?** The 'Cost Code' and 'Cost Type' segments in Work Breakdown Structure are Procore's default segments. The individual cost codes and cost types listed in each segment list are called segment items. See [What are segment and segment items?](/faq-what-are-segments-and-segment-items)
   - **What are sub jobs?** The 'Sub Job' segment is an optional segment that you can enable. See [Enable Sub Jobs for WBS](/process-guides/company-administration-work-breakdown-structure-guide/enable-sub-jobs-for-projects). Once enabled, you can add sub jobs to your projects. See [Add Sub Jobs to a Project](/process-guides/project-administration-work-breakdown-structure-guide/add-sub-jobs-to-a-project).
   - **What are custom segments?** Your company can also create custom segments. For example, you could create a 'Phase' segment and then add segment items named 'Phase I', 'Phase II', and 'Phase III.' See [Add Custom Segments](/process-guides/resource-tracking-and-unit-quantity-based-budget-setup-guide/add-custom-segments).
   - **What is the difference between a flat segment and a tiered segment?** To learn the difference, see [What is the difference between a flat and tiered segment in Procore's WBS?](/faq-what-is-the-difference-between-a-flat-and-tiered-segment-in-procores-wbs)

- In the 'Segments' table, do the following:

 - Click the **Add Items** button.

    - **Code**. Enter a unique alphanumeric code for the segment item. Then press the TAB key to move system focus to the 'Description' field. For example, enter: P1, P2, or P3

      ##### Â Notes

      - You can set character limits on the 'Code' field when adding or editing a segment. See [Add a Company Level Custom Segment](/process-guides/resource-tracking-and-unit-quantity-based-budget-setup-guide/add-custom-segments) or [Edit a Company Level Custom Segment](/process-guides/company-administration-work-breakdown-structure-guide/edit-custom-segment-settings).
      - To save a new segment item, you must enter both a 'Code' and 'Description'. if you do not enter data in these fields, a RED banner appears to alert you that the fields cannot be empty.

- **Description**. Enter a description of the segment item. Then press the TAB key to save the new segment item to the list. A GREEN 'Success' banner appears to confirm that the new segment item was saved. For example, enter: Phase I, Phase II, or Phase III

 ##### Â Important

 In order to navigate off the page, you must enter both a 'Code' and 'Description'. If you do NOT have an entry in both fields and try to move your cursor's focus to a new page, a popup message reminds you that any changes you've made will NOT be saved.

 - To finish your data entry on the line item, click **Cancel**.
 - To proceed without saving the line item, click **Leave**.