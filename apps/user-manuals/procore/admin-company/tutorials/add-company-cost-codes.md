# Add Company Cost Codes

Source: https://v2.support.procore.com/product-manuals/admin-company/tutorials/add-company-cost-codes

---

## Background

In Procore's WBS, there is is a default segment named 'Cost Code' that is available in the 'Segments' table of the Company Admin tool. This segment contains individual segment items, commonly known as cost codes. A *cost code* is a series of alphanumeric characters used to represent the different labor and material costs for a specific type work being performed on the job. Your cost codes are used to manage the dollar amounts and quantities on a project's budget.

By default, Procore's 'Cost Code' segment contains cost codes that align with the 

The *MasterFormat* is an organization standard that defines the master list of Divisions, Sections, and Section Titles for construction project specifications in the United States and Canada. It is authored by the *Construction Standards Institute (CSI)* and *Construction Specifications Canada (CSC)*. See [CSI MasterFormatÂ®](https://www.csiresources.org/standards/masterformat).

MasterFormat. To learn more, see [What are Procore's default cost codes?](/faq-what-are-procores-default-cost-codes)

## Things to Consider

- **Required User Permissions:**

 - 'Admin' level permissions on the Company level Admin tool.
- **Additional Information:**

 - The 'Cost Codes' segment is a [required segment](/faq-what-are-segments-and-segment-items) on both the Company and Project level budget code structure.
 - The 'Cost Codes' segment is a [tiered segment](/faq-what-are-segments-and-segment-items) that is available in Procore by default.
 - In a tiered segment, duplicate entries in the 'Code' field are NOT permitted when the segment items are children of the same parent segment.
 - There is no limit on the number of tiers you can create in the 'Cost Codes' segment.
 - There is no limit on the number of segment items (or individual cost codes) you can add to each tier.
 - Duplicate entries in the 'Code' field are NOT permitted. Entries in the 'Code' field for each segment item must be unique.
 - There are no character limits or other limitations on entries in the 'Description' field.
 - You cannot use a drag-and-drop operation to move cost codes from one segment to another.
- **Limitations:**

 - **For customers using the Company level ERP Integrations tool**The default segments in WBS are compatible with Procore's tool. However, some integrations do NOT yet support custom segments.
 - **For customers who have independently developed or purchased a third-party solution to integrate with Procore**To take advantage of the custom segment capabilities associated with WBS, any existing API integrations that you have independently developed or purchased to interact with Procore must be updated to support Procore's new WBS API.

 - Custom Segments are NOT supported with the ERP Integrations tool.

## Steps

1. Navigate to the Company level **Admin** tool.
2. Under 'Company Settings', click the **Work Breakdown Structure** link.
3. In the 'Segments' table, click the 'Cost Codes' segment.
4. In the tree structure on the left side of the page, highlight the root folder named **Cost Codes**.
5. To add cost codes to the 'Cost Codes' tree, navigate to the parent branch where you want to add the new child code.

   - Click the **Add Items** button.
   - Complete this data entry:

     - **Code** Enter a unique alphanumeric code for the segment item. In this example, we are creating tiered cost codes to align to Procore's default cost code list which aligns with the CIS MasterFormat, so we will enter: 012000
     - **Description** Enter a description of the segment item. In this example, we are creating tiered cost codes to align to Procore's default cost code list which aligns with the CIS MasterFormat, so we will enter: Furnishing
6. Repeat the steps above for every tier and all the cost codes that you want to add to the segment.

## Next Steps

- [Arrange the Company Budget Code Structure](/process-guides/company-administration-work-breakdown-structure-guide/set-company-budget-code-structure)