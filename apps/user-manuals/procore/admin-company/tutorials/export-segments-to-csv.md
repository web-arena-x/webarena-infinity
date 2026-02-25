# Export WBS Segments to CSV

Source: https://v2.support.procore.com/product-manuals/admin-company/tutorials/export-segments-to-csv

---

## Background

You can export a segment and all of its segment items at any time.

## Things to Consider

- **Required User Permissions:**

 - *To export segments to CSV from the Company level Admin tool:* 'Admin' level permissions on the Company level Admin tool.
 - *To export segments to CSV from the Project level Admin tool, you need one of the following:*

    - 'Admin' level permissions on the Project level Admin tool.
    - 'Read-Only' or 'Standard' level permissions on the Project level Admin tool with the ['Update Cost Codes' granular permission](/product-manuals/permissions-company/tutorials/grant-granular-permissions-in-a-project-permissions-template) enabled on your permissions template.
- **Limitations:**

 - **For customers using the Company level ERP Integrations tool**The default segments in WBS are compatible with Procore's tool. However, some integrations do NOT yet support custom segments.
 - **For customers who have independently developed or purchased a third-party solution to integrate with Procore**To take advantage of the custom segment capabilities associated with WBS, any existing API integrations that you have independently developed or purchased to interact with Procore must be updated to support Procore's new WBS API.

 - Custom Segments are NOT supported with the ERP Integrations tool.

## Prerequisites

- [Add Segment Items](/process-guides/company-administration-work-breakdown-structure-guide/add-segment-items)

## Steps

1. Navigate to the Company or Project level **Admin** tool.
2. In the 'Segments' table, click the segment to work with.
3. At the top of the page, click the **Export as CSV** link. Procore exports the parent segment and all of its children.

##### Example

This example shows you a CSV export file of a flat segment, when opened in Microsoft Excel.

This example shows you a CSV export file a tiered segment, when opened in Microsoft Excel.