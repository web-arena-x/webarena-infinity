# Assign Project Cost Codes to Sub Jobs

Source: https://v2.support.procore.com/product-manuals/admin-project/tutorials/assign-project-cost-codes-to-sub-jobs

---

## Background

Assigning cost codes to sub-jobs is a key practice for achieving financial control, project efficiency, informed decisions, and greater profitability, delivering crucial granular financial visibility organization-wide. Once company cost codes have been added to a Procore project, users can add those codes to your project's sub jobs to provide the team with better tracking of financial information. In the Project level Admin too, users can quickly locate cost codes using a search feature and assign them to sub jobs in bulk or manually add codes to each sub job.

## Things to Consider

- **Required User Permissions:**

 - 'Admin' level permission on the Project level Admin tool.
- **Limitations:**

 - **For customers using the Company level ERP Integrations tool**The default segments in WBS are compatible with Procore's tool. However, some integrations do NOT yet support custom segments.
 - **For customers who have independently developed or purchased a third-party solution to integrate with Procore**To take advantage of the custom segment capabilities associated with WBS, any existing API integrations that you have independently developed or purchased to interact with Procore must be updated to support Procore's new WBS API.

 - Custom Segments are NOT supported with the ERP Integrations tool.

## Prerequisites

- [Enable Sub Jobs for WBS](/process-guides/company-administration-work-breakdown-structure-guide/enable-sub-jobs-for-projects)
- [Add Sub Jobs to a Project](/process-guides/project-administration-work-breakdown-structure-guide/add-sub-jobs-to-a-project)

## Steps

- Add Cost Codes to Sub Jobs in Bulk
- Add Individual Cost Codes to Sub Jobs

### Add Cost Codes to Sub Jobs in Bulk

1. Navigate to the project's **Admin** tool.
2. Under 'Project Settings', click **Work Breakdown Structure**.
3. In the 'Segments' table, click **Sub Jobs**.

   ##### Â Notes

   - If the 'Sub Jobs' link is not visible in the 'Segments' table, see [Enable Sub Jobs for WBS](/process-guides/company-administration-work-breakdown-structure-guide/enable-sub-jobs-for-projects).
   - To add sub-jobs, your Procore Administrator must first [Add Company Cost Codes](/process-guides/company-administration-work-breakdown-structure-guide/add-company-cost-codes).
   - Cost codes are copied from the company's cost code list, not the project's list.

- Click **Bulk Add Company Cost Codes**.
- In the **Search** box, type to search for the code(s). The system lists any codes matching your entry.
- Choose from these options:

 - To select all matching codes, click **Select All**.
 - To choose specific codes, highlight them in the list.
- Click **Next**.
- In the 'Select Sub Jobs' window, mark the desired **Sub Job** checkboxes to add the selected codes.
- Click **Add**.

### Add Individual Cost Codes to Sub Jobs

1. Navigate to the project's **Admin** tool.
2. Under 'Project Settings', click the **Work Breakdown Structure** link.
3. In the 'Segments' table, click the **Sub Jobs** link.

   ##### Â Notes

   - If the 'Sub Jobs' link is not visible in the 'Segments' table, see [Enable Sub Jobs for WBS](/process-guides/company-administration-work-breakdown-structure-guide/enable-sub-jobs-for-projects).
   - Before you can add a sub job to a project, your company's Procore Administrator must add your company cost codes. See [Add Company Cost Codes](/process-guides/company-administration-work-breakdown-structure-guide/add-company-cost-codes).
   - For sub jobs, cost codes are copied over from the company level standard cost code list, and not the project level cost code list.

- In the 'Sub Jobs' list, locate the sub job to assign cost codes to.
- Click the icon on the sub job.
- Choose from these options:

 - To assign all of your company's cost codes to the selected sub job, click the **Cost Codes from Company** button.
 - To create cost codes for the selected sub job, click **Add Cost Code** at the bottom of the list.
- Enter a **Code** and **Description.**
- Set the **Status** of the cost code.

 ##### Â Notes

 - If any selected cost code(s) are already being used by an existing project cost code, Procore will NOT assign those cost codes to the sub job. Instead, a YELLOW banner appears to notify you that the affected cost code(s) are already in use. To see the list of the affected cost codes, click the **Show Details** button.