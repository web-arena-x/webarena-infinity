# Add 'Sub Job' Segment Items to a Procore Project

Source: https://v2.support.procore.com/product-manuals/admin-project/tutorials/add-sub-job-segment-items-to-a-procore-project

---

## Background

In Procore, a *sub job* allows you to compartmentalize job costs within a project. Once they are added to Procore (or imported via an 

In Procore, the term *integrated ERP System*, is used to refer to *Enterprise Resource Planning (ERP)* software applications that can be configured to exchange data between Procore and a supported application using the Company level ERP Integrations tool. See [Which ERP integrations are supported by Procore?](/faq-which-erp-integrations-are-supported-by-procore)

Integrated ERP System) you can monitor your project budgets and costs against them to help you better determine if you are making money on your project. For example, if your project is a multi-story commercial building, you might create a separate sub job for the build of each floor. Or, if your project is a multi-unit development, you might create a separate sub job for each individual structure.

After a sub job has been created, you can issue specific line items on the 

A *Schedule of Values (SOV)* is a list of line items that details all of the agreed-upon costs (for example, labor, materials, and so on) on a project. Abbreviated as SOV, it itemizes the contract amount into individual pay items to show how the entire contract sum is allocated to all of the project's work. An SOV is also based on the project's approved budget and commonly used to determine progress payments to the contractor(s).

Schedule of Values (SOV) for a 

A *Change Order* (CO) is a written record of a contract modification that details any amendment(s) to the original agreement's scope of work. Most construction contracts are executed with a clearly defined scope of work, so any work that is added, substituted, or deleted from the original contract's scope (such as changes to a project's designs, conditions, schedules, and/or costs) will typically require an approved change order.

Change Order to the sub job.

## Things to Consider

- **Required User Permissions:**

 One of the following:

 - 'Admin' level permissions on the Project level Admin tool.
 - 'Read-Only' or 'Standard' level permissions on the Project level Admin tool with the ['Manage Segment Items' granular permission](/product-manuals/permissions-company/tutorials/grant-granular-permissions-in-a-project-permissions-template) enabled on your permissions template. *Note:* Your Procore Administrator must configure additional settings for you to edit or delete a custom segment. To learn more, see the "Notes" in [Admin: Manage WBS Codes](/product-manuals/permissions-company/tutorials/grant-granular-permissions-in-a-project-permissions-template).
- **Additional Information:**

 - Adding 'Sub Jobs' to a project also adds it to your Company level 'Segments' list. The 'Sub Jobs' segment is counted as one (1) of the thirteen (13) available segments.
- **Limitations:**

 - **For customers using the Company level ERP Integrations tool**The default segments in WBS are compatible with Procore's tool. However, some integrations do NOT yet support custom segments.
 - **For customers who have independently developed or purchased a third-party solution to integrate with Procore**To take advantage of the custom segment capabilities associated with WBS, any existing API integrations that you have independently developed or purchased to interact with Procore must be updated to support Procore's new WBS API.

## Prerequisites

- [Enable Sub Jobs on Projects for WBS](/process-guides/company-administration-work-breakdown-structure-guide/enable-sub-jobs-for-projects)
- [Add Company Cost Codes](/process-guides/company-administration-work-breakdown-structure-guide/add-company-cost-codes)
- [Copy Company Cost Codes to a Project](/process-guides/project-administration-work-breakdown-structure-guide/copy-company-cost-codes-to-a-project)

## Steps

1. Navigate to the project's **Admin** tool.
2. Under 'Project Settings', click the **Work Breakdown Structure** link.
3. In the 'Segments' table, click the **Sub Jobs** link.

   ##### Â Notes

   - If the 'Sub Jobs' link is not visible in the 'Segments' table, see [Enable](/process-guides/company-administration-work-breakdown-structure-guide/enable-sub-jobs-for-projects) [Sub Jobs on Projects for WBS](/process-guides/company-administration-work-breakdown-structure-guide/enable-sub-jobs-for-projects).
   - Before you can add a sub job to a project, your company's Procore Administrator must add your company cost codes. See [Add Company Cost Codes](/process-guides/company-administration-work-breakdown-structure-guide/add-company-cost-codes).
   - For sub jobs, cost codes are copied over from the company level standard cost code list, and not the project level cost code list.

- Choose from these options:

 - If you are creating sub jobs for the first time, click the **Add Segment Items** button.   
     OR
 - If you are adding sub jobs to an existing list, click the **Add Item** button.
- Enter the following information:

 - **Code**. Enter an alphanumeric code for the sub job.
 - **Description**. Enter a description for the new sub job.
- Click anywhere outside the line item to save it. Procore displays the work 'Saved' in GREEN text.

 ##### Â Important

 As shown below, after you add the 'Sub Job' segment to a project, it will automatically be added to the 'Segments' table in the Company level Admin tool with a tooltip beside it. Adding the 'Sub Job' to a project counts as using one (1) of your company's thirteen (13) available segments.