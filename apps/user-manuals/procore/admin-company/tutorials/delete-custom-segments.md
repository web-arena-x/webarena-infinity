# Delete Custom Segments

Source: https://v2.support.procore.com/product-manuals/admin-company/tutorials/delete-custom-segments

---

## Things to Consider

- **Required User Permissions**:

 - 'Admin' level permissions on the Company level Admin tool.
- **Additional Information**:

 - A custom segment cannot be deleted after it has been added to the 

    A *budget code structure* is a sequence of [segments](/faq-what-are-segments-and-segment-items) used to build meaningful budget codes in accordance with the pattern established by your organization. In Procore's Work Breakdown Structure, the budget code structure for a company or project can be comprised of multiple segments.

    Budget Code Structure on one (1) or more projects in your company's Procore account.
 - A Procore 

    In Procore, a segment is a discrete category that an organization uses to break down its work into manageable components. A default segment is one that is automatically provided for use with your Procore company account. Procore's WBS has two required default segments: cost code and cost type. It also has an optional default segment: sub job.

    Default Segment cannot be deleted.
- **For companies using the** **ERP Integrations tool: Show/Hide**

 - Custom Segments are NOT supported with the ERP Integrations tool.

## Prerequisites

- [Add Custom Segments](/process-guides/resource-tracking-and-unit-quantity-based-budget-setup-guide/add-custom-segments)
- [Edit Custom Segment Settings](/process-guides/company-administration-work-breakdown-structure-guide/edit-custom-segment-settings)

## Steps

1. Navigate to the Company level **Admin** tool.
2. Under 'Company Settings', click the **Work Breakdown Structure** link.
3. In the 'Segments' table, locate the segment to delete.

   ##### Â Notes

   - Procore's default segments cannot be deleted.
   - A custom segment cannot be deleted after it is has been added to the budget code structure for one (1) or more projects.
   - If you add segment items to a segment, the total number of items displays in the 'Items' column on the 'Segments' table.

- Click the vertical ellipsis and choose **Delete** from the **Overflow** menu.
- In the 'Delete Segment?' popup window, click the **Delete** button to confirm the removal action. This permanently deletes the segment from Procore. The segment cannot be recovered.