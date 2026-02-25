# Edit Segment Items

Source: https://v2.support.procore.com/product-manuals/admin-company/tutorials/edit-segment-items

---

## Background

A *segment* is a discrete category that an organization uses to break down its work into manageable components. A *segment item* is one of many distinct items in a segment. After creating a segment, you can add an unlimited number of segment items to it. You can also use the steps below to edit your custom segment items.

## Things to Consider

- **Required User Permissions**:

 - 'Admin' level permissions on the Company level Admin tool.
- **Additional Information:**

 - Any edits you make at the Company level are automatically reflected on all of your company's existing Procore projects.
- **Limitations:**

 - **For customers using the Company level ERP Integrations tool**The default segments in WBS are compatible with Procore's tool. However, some integrations do NOT yet support custom segments.
 - **For customers who have independently developed or purchased a third-party solution to integrate with Procore**To take advantage of the custom segment capabilities associated with WBS, any existing API integrations that you have independently developed or purchased to interact with Procore must be updated to support Procore's new WBS API.

 - You cannot edit the 'Code' field on a custom segment when it is being used on a project's budget code.
 - In a flat segment, duplicate entries in the 'Code' field are NOT permitted.
 - In a tiered segment, duplicate entries in the 'Code' field are NOT permitted when the segment items are children of the same parent segment.
 - There are no character limits or other limitations on entries in the 'Description' field.\* Custom Segments are NOT supported with the ERP Integrations tool.

## Prerequisites

- [Add Segment Items](/process-guides/company-administration-work-breakdown-structure-guide/add-segment-items)

## Steps

1. Navigate to the Company level **Admin** tool.
2. Under 'Company Settings', click the **Work Breakdown Structure** link.
3. In the 'Segments' table, click the segment that you want to work with.

       

   ##### Â Note

   For example, let's assume you created a custom segment named 'Phase' with segment items named 'Phase I', 'Phase II', and 'Phase III' You want to rename the segment 'Stage' and its segment items 'Stage 1, Stage 2, and Stage 3.'

- In the 'Segment Item' table, do the following:

      
 - **Code**. Type over the existing entry with a unique alphanumeric code for the segment item. Then press the TAB key to move system focus to the 'Description' field. For example, enter: Stage

    ##### Â Important

    If the custom segment item is being used on a project's budget code, you will NOT be able to change its 'Code' value.

- **Description**. Type of the existing entry with an updated description of the segment item. Then press the TAB key to save the new segment item to the list. A GREEN 'Success' banner appears to confirm that the update was saved. For example, enter: Stage 1, Stage 2, or Stage 3
- Repeat the steps above to change other segment items as needed.