# Deactivate Segment Items

Source: https://v2.support.procore.com/product-manuals/admin-company/tutorials/deactivate-segment-items

---

## Background

A *segment* is a discrete category that an organization uses to break down its work into manageable components. A *segment item* is one of many distinct items in a segment. In Procore's Financial Management tools, segments are the building blocks that define the pattern of your company's 

A *budget code structure* is a sequence of [segments](/faq-what-are-segments-and-segment-items) used to build meaningful budget codes in accordance with the pattern established by your organization. In Procore's Work Breakdown Structure, the budget code structure for a company or project can be comprised of multiple segments.

Budget Code Structure.

When you create a new segment item, it is active in your company account by default. You can use the steps below to deactivate it. When a segment is in a deactivated state, it is grayed out to indicate it is unavailable in the 'Segments' table.

## Things to Consider

- **Required User Permissions:**

 - 'Admin' level permissions on the Company level Admin tool.
- **Additional Information:**

 - Segments can only be deactivated at the Company level. This function is NOT currently available on projects.
 - Before you deactivate a segment, be aware of the following:\* If you deactivate a segment item that is used in a budget code on an existing project, it will continue to be available on that project. If you do NOT want the segment item to be used in a budget code on the existing project in the future, it is strongly recommended that you communicate this directive to your project team.\* If you deactivate a segment item that is not used in a budget code on an existing project, it will not be available for use on that project.\* If you deactivate a segment item and then create a new project, it will NOT be available for use on the new project.
 - If you want to permanently remove a segment item to prevent it from being available on all new projects, see [Delete Segment Items](/product-manuals/admin-company/tutorials/delete-segment-items).
- **Limitations:**

 - **For customers using the Company level ERP Integrations tool**The default segments in WBS are compatible with Procore's tool. However, some integrations do NOT yet support custom segments.
 - **For customers who have independently developed or purchased a third-party solution to integrate with Procore**To take advantage of the custom segment capabilities associated with WBS, any existing API integrations that you have independently developed or purchased to interact with Procore must be updated to support Procore's new WBS API.

##### Â Important

Before you deactivate a segment, be aware of the following:

- If you deactivate a segment item that is used in a budget code on an existing project, it will still appear on projects where it is already in use. However, it will no longer be an available option when creating new budget codes.
- If you deactivate a segment item that is not used in a budget code on an existing project, it will be deactivated on that project.
- If you deactivate a segment item and then create a new project, it will NOT be available for use on the new project.