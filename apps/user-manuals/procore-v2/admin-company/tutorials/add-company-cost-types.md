# Add Company Cost Types

Source: https://v2.support.procore.com/product-manuals/admin-company/tutorials/add-company-cost-types

---

## Background

The 'Cost Type' segment is one of the default segments in Procore's 

In Procore, a *Work Breakdown Structure (WBS)* is a feature that provides users with a flexible method for organizing and reporting on financial information. With WBS, Owners, General Contractors, and Specialty Contractors can create a customized framework of unique segments and rules for tagging, tracking, and reporting with Procore's Financial Management tools.

Work Breakdown Structure. It is a flat segment that is typically is used to perform 

*Job Costing* is an accounting practice in the construction industry used to track the costs for certain job activities and projects using a consistent organizational system to record and report on costs.

Job Costing. In WBS, a *segment* is a discrete category that an organization uses to break down its work into manageable components. A *segment item* is one of many distinct items in a segment. After creating a segment, you can add an unlimited number of segment items to it. To learn more, see [What are segments and segment items?](/faq-what-are-segments-and-segment-items)

##### Example

Procore's 'Cost Type' segment includes the following segment items. See [What are Procore's default cost types?](/faq-what-are-procores-default-cost-types) Other segment items to add to your 'Cost Type' segment might include Direct Labor (DL), Direct Materials (DM), and Overhead (OH):

## Things to Consider

- **Required User Permissions:**

 - 'Admin' level permissions on the Company level Admin tool.
- **Additional Information:**

 - 'Code' and 'Description' are required fields and cannot be empty.
 - Duplicate entries in the 'Code' field are NOT permitted. Entries in the 'Code' field for each segment item must be unique.
 - There are no character limits on entries in the 'Description' field.
 - There is no limit on the number of segment items you can add.
 - Your Company level 'Cost Type' segment items cannot be edited or deleted at the project level.
- **Limitations:**

 - **For customers using the Company level ERP Integrations tool**The default segments in WBS are compatible with Procore's tool. However, some integrations do NOT yet support custom segments.
 - **For customers who have independently developed or purchased a third-party solution to integrate with Procore**To take advantage of the custom segment capabilities associated with WBS, any existing API integrations that you have independently developed or purchased to interact with Procore must be updated to support Procore's new WBS API.

## Prerequisites

Read the following:

- [Create Your Company's Default Work Breakdown Structure](/product-manuals/admin-company/tutorials/create-your-companys-default-work-breakdown-structure)
- [Create Your Project's Work Breakdown Structure](/process-guides/resource-tracking-and-unit-quantity-based-budget-setup-guide/create-your-projects-wbs)
- [What are Procore's default cost types?](/faq-what-are-procores-default-cost-types)

## Steps

1. Navigate to the Company level **Admin** tool.
2. Under 'Company Settings', click the **Work Breakdown Structure** link.
3. In the 'Segments' table, click the 'Cost Types' segment to open it.
4. Do the following:

       
   - If you are setting up segment items for the first time or if you want to add more cost types, click the **Add Items** button.
   - **Code**. Enter a unique alphanumeric code for the segment item. This is a required field. Duplicate entries are NOT permitted. In this example, we will enter: L
   - **Description**. Enter a description of the segment item. This is a required field. In this example, we will enter: Labor

     ##### Â Note

     The 'Code' and 'Description' fields are required. Duplicate entries are NOT permitted in the 'Code' field. If you attempt to leave a field blank or add a duplicate, Procore displays a RED banner to notify you of the issue.

- Repeat the steps above for every cost type that you want to add.