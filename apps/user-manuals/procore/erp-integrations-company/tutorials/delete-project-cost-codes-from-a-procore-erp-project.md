# Delete Project Cost Codes from an ERP Integrated Project

Source: https://v2.support.procore.com/product-manuals/erp-integrations-company/tutorials/delete-project-cost-codes-from-a-procore-erp-project

---

##### ERP DOCUMENTATION

**Each Procore-built ERP integration offers its own unique feature set.** Your integration might not support the action described on this page.

To learn about your integration and its supported features, see [Which ERP integrations are supported by Procore?](/faq-which-erp-integrations-are-supported-by-procore)

## Background

If your company's Procore account is integrated with an ERP system, you can delete Project Cost Codes if they are not in use on any items in the project.

## Things to Consider

- **Required User Permission**:

 - 'Admin' level permission on the project's Admin tool.
- **Prerequisites**, **Requirements, and Limitations**:

 - The cost code(s) must NOT be in use on any object in the Procore project.
 - You might need to first delete the code from your ERP system before deleting it in Procore.

## Steps

To delete unused cost codes from the project's 'Cost Code' segment:

1. Navigate to the Project level **Admin** tool.
2. Under 'Project Settings', click the **Work Breakdown Structure** link.
3. In the 'Segments' table, click the segment that contains the item(s) to delete.
4. Locate the segment item to delete. If you are deleting a tiered segment, you will want to navigate to the segment item and highlight it in the left pane.
5. Click the vertical ellipsis on the segment item's line item, and choose **Delete** from the **Overflow** menu.