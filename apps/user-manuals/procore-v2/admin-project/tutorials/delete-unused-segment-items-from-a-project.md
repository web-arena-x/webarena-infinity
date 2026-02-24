# Delete Unused Segment Items from a Project

Source: https://v2.support.procore.com/product-manuals/admin-project/tutorials/delete-unused-segment-items-from-a-project

---

## Background

At the Project level, segments and segment items can be deleted in accordance with the policies set by your company's Procore Administrator when the segment was created (see [Add Custom Segments](/process-guides/resource-tracking-and-unit-quantity-based-budget-setup-guide/add-custom-segments)). Much like segment items in your Company level WBS, Project level segment items can be deleted only when they have not been used to create a budget code on your project.

##### Â Note

[Add Custom Segments](/process-guides/resource-tracking-and-unit-quantity-based-budget-setup-guide/add-custom-segments)[Edit Custom Segment Settings](/process-guides/company-administration-work-breakdown-structure-guide/edit-custom-segment-settings)

## Things to Consider

- **Required User Permissions:**

 One of the following:

 - 'Admin' level permissions on the Project level Admin tool.
 - 'Read-Only' or 'Standard' level permissions on the Project level Admin tool with the ['Manage Segment Items' granular permission](/product-manuals/permissions-company/tutorials/grant-granular-permissions-in-a-project-permissions-template) enabled on your permissions template. *Note:* Your Procore Administrator must configure additional settings for you to edit or delete a custom segment. To learn more, see the "Notes" in [Admin: Manage WBS Codes](/product-manuals/permissions-company/tutorials/grant-granular-permissions-in-a-project-permissions-template).
- **Additional Information**:

 - After a segment item is used to create a budget code on a project, it cannot be deleted. However, it can be deactivated to prevent future use. See [Deactivate Segment Items](/process-guides/company-administration-work-breakdown-structure-guide/deactivate-segment-items).
- **Limitations:**

 - **For customers using the Company level ERP Integrations tool**The default segments in WBS are compatible with Procore's tool. However, some integrations do NOT yet support custom segments.
 - **For customers who have independently developed or purchased a third-party solution to integrate with Procore**To take advantage of the custom segment capabilities associated with WBS, any existing API integrations that you have independently developed or purchased to interact with Procore must be updated to support Procore's new WBS API.

## Prerequisites

- [Add Segment Items](/process-guides/company-administration-work-breakdown-structure-guide/add-segment-items)

## Steps

1. Navigate to the Project level **Admin** tool.
2. Under 'Project Settings', click the **Work Breakdown Structure** link.
3. In the 'Segments' table, click the segment that contains the item(s) to delete.
4. Locate the segment item to delete. If you are deleting a tiered segment, you will want to navigate to the segment item and highlight it in the left pane.
5. Click the vertical ellipsis on the segment item's line item, and choose **Delete** from the **Overflow** menu.

## Next Steps

- [Arrange the Company Budget Code Structure](/process-guides/company-administration-work-breakdown-structure-guide/set-company-budget-code-structure)