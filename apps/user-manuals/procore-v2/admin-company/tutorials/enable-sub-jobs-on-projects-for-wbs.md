# Enable Sub Jobs on Projects for WBS

Source: https://v2.support.procore.com/product-manuals/admin-company/tutorials/enable-sub-jobs-on-projects-for-wbs

---

## Background

In Procore, a *sub job* allows you to compartmentalize job costs within a project. Once they are added to Procore (or imported via an 

In Procore, the term *integrated ERP System*, is used to refer to *Enterprise Resource Planning (ERP)* software applications that can be configured to exchange data between Procore and a supported application using the Company level ERP Integrations tool. See [Which ERP integrations are supported by Procore?](/faq-which-erp-integrations-are-supported-by-procore)

Integrated ERP System) you can monitor your project budgets and costs against them to help you better determine if you are making money on your project. For example, if your project is a multi-story commercial building, you might create a separate sub job for the build of each floor. Or, if your project is a multi-unit development, you might create a separate sub job for each individual structure.

## Things to Consider

- **Required User Permissions:**

 - 'Admin' level permissions on the Company level Admin tool.
- **Additional Information:**

 - To learn more about Sub Jobs, see: [What's the difference between a job, a parent job, and a sub job?](/faq-what's-the-difference-between-a-job-a-parent-job-and-a-sub-job)
- **Limitations:**

 - **For customers using the Company level ERP Integrations tool**The default segments in WBS are compatible with Procore's tool. However, some integrations do NOT yet support custom segments.
 - **For customers who have independently developed or purchased a third-party solution to integrate with Procore**To take advantage of the custom segment capabilities associated with WBS, any existing API integrations that you have independently developed or purchased to interact with Procore must be updated to support Procore's new WBS API.

## Steps

1. Navigate to the Company level **Admin** tool.
2. Under 'Company Settings', click **Work Breakdown Structure**.
3. Click the **Configure Settings** icon.
4. Check the box under **Sub Jobs.**
5. Click **Save**.