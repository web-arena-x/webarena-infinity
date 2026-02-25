# View the Company Cost Type Segment Settings

Source: https://v2.support.procore.com/product-manuals/admin-company/tutorials/view-the-company-cost-type-segment-settings

---

## Background

Use the steps below whenever you want to view the settings on the 'Cost Type' segment in your company's WBS.

## Things to Consider

- **Required User Permissions**:

 - 'Admin' level permissions on the Company level Admin tool.
- **Limitations:**

 - **For customers using the Company level ERP Integrations tool**The default segments in WBS are compatible with Procore's tool. However, some integrations do NOT yet support custom segments.
 - **For customers who have independently developed or purchased a third-party solution to integrate with Procore**To take advantage of the custom segment capabilities associated with WBS, any existing API integrations that you have independently developed or purchased to interact with Procore must be updated to support Procore's new WBS API.

## Prerequisites

- [Add Company Cost Types](/process-guides/company-administration-work-breakdown-structure-guide/add-company-cost-types)

## Steps

1. Navigate to the Company level **Admin** tool.
2. Under 'Company Settings', click the **Work Breakdown Structure** link.
3. In the 'Segments' table, click the 'Cost Types' segment.
4. Above the 'Cost Types' table, click **Configure Settings** icon.
5. In the 'Segment Settings' dialog box under 'Project Level Actions,' you have these options:

   ##### Â Note

   The 'Cost Type' segment is a [default segment](/faq-what-are-segments-and-segment-items). You cannot edit the 'Segment Name' or the 'Segment Structure' settings.

- **Add/Edit/Delete Project Level Segment Items**. This checkbox is grayed out and unavailable by default.
- **Delete Segment Items Inherited by Default**. This checkbox is grayed out and unavailable by default.
- **Available for Use on New Projects**. Place a checkmark in this box to make the segment and its items available for use on new Procore projects. This is Procore's default setting. Remove the checkmark if you do NOT want the segment or its items to be available on projects.

- Click **Close**.

## Next Steps

- [Arrange Segments to Form the Company's Budget Code Structure](/process-guides/company-administration-work-breakdown-structure-guide/set-company-budget-code-structure)