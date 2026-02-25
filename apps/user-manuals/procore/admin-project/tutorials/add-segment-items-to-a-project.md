# Add Segment Items to a Project

Source: https://v2.support.procore.com/product-manuals/admin-project/tutorials/add-segment-items-to-a-project

---

## Background

A *segment* is a discrete category that an organization uses to break down its work into manageable components. A *segment item* is one of many distinct items in a segment. After creating a segment, your company's Procore Administrator can add an unlimited number of segment items to it at the Company level. However, whether or not you are permitted to use the steps below to add custom segment items at the Project level, depends on the segment's Company level settings.

##### Â Note

The steps below are only available when your Procore Administrator places a checkmark in the 'Add/Edit/Delete Project Level Segment Items' box. To learn more, see [Add Custom Segments](/process-guides/resource-tracking-and-unit-quantity-based-budget-setup-guide/add-custom-segments) and [Edit Custom Segment Settings](/process-guides/company-administration-work-breakdown-structure-guide/edit-custom-segment-settings).

## Things to Consider

- **Required User Permissions:**

 One of the following:

 - 'Admin' level permissions on the Project level Admin tool.
 - 'Read-Only' or 'Standard' level permissions on the Project level Admin tool with the ['Manage Segment Items' granular permission](/product-manuals/permissions-company/tutorials/grant-granular-permissions-in-a-project-permissions-template) enabled on your permissions template. *Note:* Your Procore Administrator must configure additional settings for you to edit or delete a custom segment. To learn more, see the "Notes" in [Admin: Manage WBS Codes](/product-manuals/permissions-company/tutorials/grant-granular-permissions-in-a-project-permissions-template).
- **Additional Information:**

 - - To allow project users to edit or delete a company level custom segment item that is later copied to a project, the **Add/Edit/Delete Project Level Segment Items** and **Delete Segment Items Inherited from a Company** settings must be turned ON when completing the steps below.

      - When editing a company level segment item that was copied to your project, users can will only be able to change the 'Description' field of the segment item. See [Edit Segment Items on a Project](/process-guides/project-administration-work-breakdown-structure-guide/edit-segment-items).
      - When editing a project level segment item that was specifically created on a project, users will be able change both the 'Code' and 'Description' of the segment item. See [Edit Segment Items on a Project](/process-guides/project-administration-work-breakdown-structure-guide/edit-segment-items).
      - Procore's default 'Cost Type' segment can only be managed by a Procore Administrator in the Company level Admin tool. See [Add Company Cost Types](/process-guides/company-administration-work-breakdown-structure-guide/add-company-cost-types).
- **Limitations:**

 - **For customers using the Company level ERP Integrations tool**The default segments in WBS are compatible with Procore's tool. However, some integrations do NOT yet support custom segments.
 - **For customers who have independently developed or purchased a third-party solution to integrate with Procore**To take advantage of the custom segment capabilities associated with WBS, any existing API integrations that you have independently developed or purchased to interact with Procore must be updated to support Procore's new WBS API.

 - In a flat segment, duplicate entries in the 'Code' field are NOT permitted.
 - In a tiered segment, duplicate entries in the 'Code' field are NOT permitted when the segment items are children of the same parent segment.
 - There are no character limits or other limitations on entries in the 'Description' field.
 - There is no limit on the number of segment items you can add.

## Prerequisites

- [Add Custom Segments](/process-guides/resource-tracking-and-unit-quantity-based-budget-setup-guide/add-custom-segments)

## Steps

1. Navigate to the project's **Admin** tool.
2. Under 'Company Settings', click the **Work Breakdown Structure** link.
3. In the 'Segments' table, click the segment that you want to work with.

   ##### Â Note

   For example, you can create a custom segment named 'Phase' and will add segment items named 'Phase I', 'Phase 2', and 'Phase 3.'

- In the 'Segment' table, click the **Add Items** button. Then do the following:

 - **Code**. Enter a unique alphanumeric code for the segment item. For example, enter: P1, P2, or P3

    ##### Â Note

    - You can set character limits on the 'Code' field when adding or editing a segment. See [Add Custom Segments](/process-guides/resource-tracking-and-unit-quantity-based-budget-setup-guide/add-custom-segments) or [Edit Custom Segment Settings](/process-guides/company-administration-work-breakdown-structure-guide/edit-custom-segment-settings).