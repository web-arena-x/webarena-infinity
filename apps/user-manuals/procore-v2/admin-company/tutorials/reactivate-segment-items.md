# Reactivate Segment Items

Source: https://v2.support.procore.com/product-manuals/admin-company/tutorials/reactivate-segment-items

---

## Background

A *segment* is a discrete category that an organization uses to break down its work into manageable components. A *segment item* is one of many distinct items in a segment. In Procore's Financial Management tools, segments are the building blocks that define the pattern of your company's 

A *budget code structure* is a sequence of [segments](/faq-what-are-segments-and-segment-items) used to build meaningful budget codes in accordance with the pattern established by your organization. In Procore's Work Breakdown Structure, the budget code structure for a company or project can be comprised of multiple segments.

Budget Code Structure.

When you create a new segment item, it is active in your company account by default. You have the option to deactivate it at the company level. If you change your mind or if you want to use the segment item later, you can also use the steps below to reactivate it.

## Things to Consider

- **Required User Permissions**:

 - 'Admin' level permissions on the Company level Admin tool.
- **Additional Information:**

 - If you reactivate a segment item, it will immediately be available in all new projects and on any existing projects where it was previously deactivated.
- **Limitations:**

 - **For customers using the Company level ERP Integrations tool**The default segments in WBS are compatible with Procore's tool. However, some integrations do NOT yet support custom segments.
 - **For customers who have independently developed or purchased a third-party solution to integrate with Procore**To take advantage of the custom segment capabilities associated with WBS, any existing API integrations that you have independently developed or purchased to interact with Procore must be updated to support Procore's new WBS API.

 - Custom Segments are NOT supported with the ERP Integrations tool.

## Prerequisites

- [Deactivate Segment Items](/process-guides/company-administration-work-breakdown-structure-guide/deactivate-segment-items)

## Steps

- Reactivate Flat Segment Items
- Reactivate Tiered Segment Items

### Reactivate Flat Segment Items

1. Navigate to the Company level **Admin** tool.
2. Under 'Company Settings', click the **Work Breakdown Structure** link.
3. In the 'Segments' table, locate the segment to reactivate and then click its link.

   ##### Â Tip

   **How do I know when a segment item is inactive?** When segment items are in the deactivated state, they are grayed out to indicate they are unavailable.

- Click the vertical ellipsis and choose **Reactivate** from the **Overflow** menu.

      

 Procore reactivates the segment item. The line item is grayed out, to indicate it is no longer available in the list of segment items in the 'Segment' table.

### Reactivate Tiered Segment Items

1. Navigate to the Company level **Admin** tool.
2. Under 'Company Settings', click the **Work Breakdown Structure** link.
3. In the 'Segments' table, locate segment(s) to reactivate.
4. Place a checkmark in the boxes that correspond to the segment(s).

   ##### Â Tip

   **How do I know when a segment item is inactive?** When segment items are in the deactivated state, they are grayed out to indicate they are unavailable.

- Click the vertical ellipsis and choose **Reactivate** from the **Overflow** menu at the top of the 'Segments' table. Procore reactivates the segment item.