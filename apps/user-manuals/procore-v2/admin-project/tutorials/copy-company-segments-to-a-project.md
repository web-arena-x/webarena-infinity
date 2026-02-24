# Copy Company WBS Segments to a Project

Source: https://v2.support.procore.com/product-manuals/admin-project/tutorials/copy-company-segments-to-a-project

---

## Background

When setting up your project, you can choose which segment items to copy from your company's WBS.

## Things to Consider

- **Required User Permissions**:

 - 'Admin' level permissions on the Company level Admin tool.
- **Limitations:**

 - **For customers using the Company level ERP Integrations tool**The default segments in WBS are compatible with Procore's tool. However, some integrations do NOT yet support custom segments.
 - **For customers who have independently developed or purchased a third-party solution to integrate with Procore**To take advantage of the custom segment capabilities associated with WBS, any existing API integrations that you have independently developed or purchased to interact with Procore must be updated to support Procore's new WBS API.

 - Custom Segments are NOT supported with the ERP Integrations tool.

## Prerequisites

- [Add Custom Segments](/process-guides/resource-tracking-and-unit-quantity-based-budget-setup-guide/add-custom-segments)

## Steps

1. Navigate to the project's **Admin** tool.
2. Under 'Company Settings', click the **Work Breakdown Structure** link.
3. In the 'Segments' table, click the segment that you want to work with. The steps you follow, depend on whether the segment is flat or tiered:

   - Copy Flat Segments
   - Copy Tiered Segments

### Copy Flat Segments

1. Click the **Company Segments** button.
2. Choose from these options:

   - To copy all of a copy segment to the project, click the **Select All Segment Items** button.
   - To copy only selected segment items, mark the checkboxes next to the desired segment items.
3. Click the **Copy** button.

### Copy Tiered Segments

1. Click the **Company Segments** button.
2. Choose from these options:

   - To copy all of a copy segment to the project, click the **Select All Segment Items** button.
   - To copy only selected segment items, expand and collapse the desired segment items and then highlight the segment items to copy.
3. Click the **Copy** button.

## Next Steps

- [Add Segments to the Project's Budget Code Structure](/process-guides/project-administration-work-breakdown-structure-guide/add-custom-segments-to-the-project-budget-code-structure)