# Create Your Project's Work Breakdown Structure

Source: https://v2.support.procore.com/product-manuals/admin-project/tutorials/create-your-projects-work-breakdown-structure

---

## Background

After creating a new project in your company's Procore account, you can use the built-in WBS features to define the cost structure for Procore's Project Financials tools. When defining a project's WBS cost structure, you have two choices. If you are unsure which choice to make, contact your company's Procore Administrator for guidance:

- **Apply your Company's Default WBS.** This is the WBS defined by your company's Procore Administrator and you can use it exactly as it was created.
- **Copy the WBS from Another Project.** This is the WBS defined on one of your existing Procore project templates. Keep in mind that you can create a unique WBS for each project in your company's account. In order to copy the WBS from another source project to your new target project, you must first save the source project as a project template. See [Configure a Project Template](/product-manuals/portfolio-company/tutorials/configure-a-project-template).

## Things to Consider

- **Required User Permissions:**

 - 'Admin' level permissions on the Project level Admin tool.
- **Additional Information:**

 - The Project level 'Work Breakdown Structure' page is similar to the Company level page. The primary differences are:

    - You cannot add custom segments at the Project level. They must always be added at the Company level. See [Add Custom Segments](/process-guides/resource-tracking-and-unit-quantity-based-budget-setup-guide/add-custom-segments).
    - You cannot edit the budget code structure at the Project level. The budget code structure is always defined at the Company level. See [Arrange the Company Budget Code Structure](/process-guides/company-administration-work-breakdown-structure-guide/set-company-budget-code-structure).
    - You cannot add sub jobs at the Company level. Sub jobs are always added at the Project level. See [Enable Sub Jobs on Projects for WBS](/process-guides/company-administration-work-breakdown-structure-guide/enable-sub-jobs-for-projects) and [Add Sub Jobs to a Project](/process-guides/project-administration-work-breakdown-structure-guide/add-sub-jobs-to-a-project).
- **Limitations**:

 - **For customers using the Company level ERP Integrations tool**The default segments in WBS are compatible with Procore's tool. However, some integrations do NOT yet support custom segments.
 - **For customers who have independently developed or purchased a third-party solution to integrate with Procore**To take advantage of the custom segment capabilities associated with WBS, any existing API integrations that you have independently developed or purchased to interact with Procore must be updated to support Procore's new WBS API.

## Prerequisites

- [Create Your Company's Default Work Breakdown Structure](/product-manuals/admin-company/tutorials/create-your-companys-default-work-breakdown-structure)

##### Â Tip

**Do you want to copy the WBS from an existing project to your new project?** If so, a Procore user who meets the required user permissions will need to configure the source project as a project template. A *source project* is the project that contains the WBS you want to copy to your new one. For instructions see, [Configure a Project Template](/product-manuals/portfolio-company/tutorials/configure-a-project-template). One that step is complete, you'll be able to select the 'Copy the WBS from Another Project' option detailed in the Steps below.

## Steps

1. Navigate to the Project level **Admin** tool.
2. Under 'Project Settings', click the **Work Breakdown Structure** link.
3. Review the information about WBS, Budget Codes, Budget Code Segments in the dialog box sequence. Click **Next**.
4. In the 'Create Project WBS dialog box, choose one of these optons:

   - **Apply the Company's Default WBS**. Choose this option button if you want the project to use your company's default WBS. Your company's Procore Administrator is responsible for creating this structure.
   - **Copy the WBS from Another Project**. Choose this option button if you want to use an existing project's WBS. Then, start typing a project name and when the match appears, choose it in **Select a Project** list.
5. Click **Create**.

##### Â Tip

**Did you know you can customize the budget code descriptions for your project?** Customization is useful when your team wants to create two or more descriptions for a single budget code. Customization can also improve the readability of your codes on financial line items for your end users. To learn more, see [Why and how do I create a custom budget code description for Procore's Project Financials tools?](/faq-why-and-how-do-i-create-a-custom-budget-code-description-for-procores-project-financials-tools)