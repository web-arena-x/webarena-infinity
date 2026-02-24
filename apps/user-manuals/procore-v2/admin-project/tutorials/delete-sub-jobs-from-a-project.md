# Delete Sub Jobs from a Project

Source: https://v2.support.procore.com/product-manuals/admin-project/tutorials/delete-sub-jobs-from-a-project

---

## Background

You can delete sub jobs from a project only if they have NOT been used in a budget code on the project.

## Things to Consider

- **Required User Permissions:**

 One of the following:

 - 'Admin' level permissions on the Project level Admin tool.
 - 'Read-Only' or 'Standard' level permissions on the Project level Admin tool with the ['Manage Segment Items' granular permission](/product-manuals/permissions-company/tutorials/grant-granular-permissions-in-a-project-permissions-template) enabled on your permissions template. *Note:* Your Procore Administrator must configure additional settings for you to edit or delete a custom segment. To learn more, see the "Notes" in [Admin: Manage WBS Codes](/product-manuals/permissions-company/tutorials/grant-granular-permissions-in-a-project-permissions-template).
- **Limitations:**

 - **For customers using the Company level ERP Integrations tool**The default segments in WBS are compatible with Procore's tool. However, some integrations do NOT yet support custom segments.
 - **For customers who have independently developed or purchased a third-party solution to integrate with Procore**To take advantage of the custom segment capabilities associated with WBS, any existing API integrations that you have independently developed or purchased to interact with Procore must be updated to support Procore's new WBS API.

 - Custom Segments are NOT supported with the ERP Integrations tool.

## Prerequisites

- [Add Sub Jobs to a Project](/process-guides/project-administration-work-breakdown-structure-guide/add-sub-jobs-to-a-project)

## Steps

1. Navigate to the project's **Admin** tool.
2. Under 'Project Settings', click the **Work Breakdown Structure** link.
3. In the 'Segments' table, click the **Sub Jobs** link.

   ##### Â Notes

   - If the 'Sub Jobs' link is not visible in the 'Segments' table, see [Enable Sub Jobs on Projects for WBS](/process-guides/company-administration-work-breakdown-structure-guide/enable-sub-jobs-for-projects).
   - You can delete sub jobs from a project only if they have NOT been used in a budget code on the project.

- Locate the line item that you want to delete.
- Click the vertical ellipsis and choose **Delete** from the **Overflow** menu.
- Click anywhere outside the line item to save it. Procore displays the work 'Saved' in GREEN text.