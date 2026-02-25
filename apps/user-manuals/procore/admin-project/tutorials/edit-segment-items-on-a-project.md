# Edit Segment Items on a Project

Source: https://v2.support.procore.com/product-manuals/admin-project/tutorials/edit-segment-items-on-a-project

---

## Background

A *segment* is a discrete category that an organization uses to break down its work into manageable components. A *segment item* is one of many distinct items in a segment. After creating a segment, your company's Procore Administrator can add an unlimited number of segment items to it at the Company level. However, whether or not you are permitted to use the steps below to edit segments at the Project level, depends on the segment's Company level settings.

##### Â Note

To edit a company level custom segment item that was copied to your project, the **Add/Edit/Delete Project Level Segment Items** setting must be turned ON by your company's Procore Administrator when adding the segment. To learn more, see [Add Custom Segments](/process-guides/resource-tracking-and-unit-quantity-based-budget-setup-guide/add-custom-segments).

## Things to Consider

- **Required User Permissions:**

 One of the following:

 - 'Admin' level permissions on the Project level Admin tool.
 - 'Read-Only' or 'Standard' level permissions on the Project level Admin tool with the ['Manage Segment Items' granular permission](/product-manuals/permissions-company/tutorials/grant-granular-permissions-in-a-project-permissions-template) enabled on your permissions template. *Note:* Your Procore Administrator must configure additional settings for you to edit or delete a custom segment. To learn more, see the "Notes" in [Admin: Manage WBS Codes](/product-manuals/permissions-company/tutorials/grant-granular-permissions-in-a-project-permissions-template).
- **Additional Information:**

 - To edit or delete a company level custom segment item that was copied to your project, the **Add/Edit/Delete Project Level Segment Items** and **Delete Segment Items Inherited from a Company** settings must be turned ON by your company's Procore Administrator when adding the segment. To learn more, see [Add Custom Segments](/process-guides/resource-tracking-and-unit-quantity-based-budget-setup-guide/add-custom-segments), the Steps below, and [Delete Unused Segment Items from a Project](/process-guides/project-administration-work-breakdown-structure-guide/delete-unused-segment-items).
 - When editing a company level segment item that was copied to your project, you can only change the 'Description' field of the segment item.
 - When editing a project level segment item that was specifically created on a project, you can change both the 'Code' and 'Description' of the segment item.
 - Procore's default 'Cost Type' segment can only be managed by a Procore Administrator in the Company level Admin tool. See [Add Company Cost Types](/process-guides/company-administration-work-breakdown-structure-guide/add-company-cost-types).
- **Limitations:**

 - **For customers using the Company level ERP Integrations tool**The default segments in WBS are compatible with Procore's tool. However, some integrations do NOT yet support custom segments.
 - **For customers who have independently developed or purchased a third-party solution to integrate with Procore**To take advantage of the custom segment capabilities associated with WBS, any existing API integrations that you have independently developed or purchased to interact with Procore must be updated to support Procore's new WBS API.

 - In a flat segment, duplicate entries in the 'Code' field are NOT permitted.
 - In a tiered segment, duplicate entries in the 'Code' field are NOT permitted when the segment items are children of the same parent segment.
 - There are no character limits or other limitations on entries in the 'Description' field.
 - There is no limit on the number of segment items you can add.\* Custom Segments are NOT supported with the ERP Integrations tool.

## Prerequisites

- [Add Custom Segments](/process-guides/resource-tracking-and-unit-quantity-based-budget-setup-guide/add-custom-segments)

## Steps

1. Navigate to the project's **Admin** tool.
2. Under 'Project Settings', click the **Work Breakdown Structure** link.
3. In the 'Segments' table, click the segment that you want to work with.
4. In the 'Segment' table, locate the segment to edit.
5. Click in the **Description** field and type over the existing value with your new one.

   ##### Example

   In this example, we changed the 'Description' field from "Phase 1" to "Phase I" on a custom segment named 'Phase'.