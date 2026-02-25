# Add the 'ERP Direct Costs' Column to a Procore Budget View for ERP Integrations

Source: https://v2.support.procore.com/product-manuals/admin-company/tutorials/add-the-erp-direct-costs-column-to-a-procore-budget-view-for-erp-integrations

---

## Background

In Procore, a *budget view* defines the data column layout that appears in the Budget tab in the project's Budget tool. By default, the Procore web application provides users with four (4) budget views that you can use as-is or customize to suit your business needs. See [Set up a New Budget View](/product-manuals/admin-company/tutorials/set-up-a-new-budget-view) and [Configure](/product-manuals/admin-company/tutorials/add-the-unit-based-columns-to-a-budget-view) [Budget View Columns](/product-manuals/admin-company/tutorials/add-the-unit-based-columns-to-a-budget-view). Each budget view includes a unique set of columns designed to help you see the data that you want to see in Procore's Budget tool.

When your company is using Procore with one of the 

In Procore, the term *integrated ERP System*, is used to refer to *Enterprise Resource Planning (ERP)* software applications that can be configured to exchange data between Procore and a supported application using the Company level ERP Integrations tool. See [Which ERP integrations are supported by Procore?](/faq-which-erp-integrations-are-supported-by-procore)

Integrated ERP System and you (or another project user) have enabled the Direct Costs tool on your integrated projects, it is recommended that you add an 'ERP Direct Costs' column. The 'ERP Direct Costs' column is a *calculated column* that also requires you to create two (2) *source columns* to enable the system to automatically perform the required calculation.

## Things to Consider

##### Â Important

This article describes how to set up a budget view to show job cost summary information. Some ERP integrations offer the ability to sync job cost transaction detail, instead of job cost summary information. See [Things to Know about your ERP Integration](https://support.procore.com/products/online/user-guide/company-level/erp-integrations/things-to-know-about-your-erp-integration) to learn more about how your integration can sync job cost information.

To configure the necessary budget views for job cost transaction detail instead of job cost summary, see [Add Columns for ERP Job Cost Transaction Detail](/product-manuals/erp-integrations-company/tutorials/add-columns-to-a-budget-view-for-erp-job-cost-transaction-detail).

- **Required User Permissions**:

 - 'Admin' on the Company Admin tool. 
    AND Consider utilizing the Budget tool's 'View Direct Cost Details' granular permission in your permission templates to control who can and cannot click a value in the 'Direct Costs' column of a budget view to open a popup window that shows job cost transaction detail in the Budget tool. See Grant Granular Permissions in a Permission Template.
- **Requirements**:

 - The ERP Integrations tool must be active on your Procore company account.
 - Enable these Project Tools:

    - Budget Tool. See [Add and Remove Project Tools](/product-manuals/admin-project/tutorials/add-and-remove-project-tools).
    - Direct Costs Tool. See [Enable the Direct Costs Tool](/product-manuals/direct-costs-project/tutorials/enable-the-direct-costs-tool).
 - Set up the desired budget views for your project. See [Set up a New Budget View](/product-manuals/admin-company/tutorials/set-up-a-new-budget-view).

    - [Which budget views should I add to my projects?](/faq-which-budget-views-should-i-add-to-my-projects)

## Steps

1. Navigate to the Company **Admin** tool.
2. Under **Tool Settings**, click **Budget**.
3. Click the budget view that you want to add the new column.
4. Click **Configure Columns** under **Column Configuration**.
5. Create a new source column as follows:

   1. Click **Create** at the top of the window and choose **Source** from the drop-down list.
   2. **Column Name**. Enter the new source column name in the list. For example, type `ERP Job to Date Costs`.
   3. **Column Source**. Select *ERP Job Costs* from this drop-down list.
   4. **ERP Job to Date Costs**. Place a checkmark in this box.
   5. Click **Create** at the bottom of the window.
6. Create another source column as follows:

   1. Click **Create** at the top of the window and choose **Source** from the drop-down list.
   2. **Column Name**. Enter the new source column name in the list. For example, type `ERP Commitment Invoiced`.
   3. **Column Source**. Select *ERP Job Costs* from this drop-down list.
   4. **ERP Commitment Invoiced**. Place a checkmark in this box.
   5. Click **Create** at the bottom of the window.
7. Verify that the new **ERP Commitment Invoiced** column and the **ERP Job to Date Costs** column appear under **Source**.
8. Create a calculated column as follows:

   1. Click **Create** at the top of the window and choose **Calculated** from the drop-down list.
   2. **Column Name**. Enter a new name for the column. For example, type `ERP Direct Costs`.
   3. **Format**. Choose *Currency* or *Percent*.
   4. **Pick a Column**. Define the calculation as follows:

      1. Select *ERP Job to Date Costs* from the top **Pick a Column** drop-down list.
      2. Select *ERP Commitment Invoiced* from the next **Pick a Column** drop-down list.
      3. Select the minus sign (-) from the drop-down list to the left of your column.
      4. Click **Create** at the bottom of the window.
9. Verify that the new **ERP Direct Costs** column appears under **Calculated**.
10. If your budget view was created from the 'Procore Standard Budget' template, you must do the following:

    - Highlight **Projected** **Costs** under **Calculated**.
    - Ensure a checkmark appears in the **Projected Costs** box.
    - Click **Edit**.
    - Change the drop-down list selection from *Direct Costs* to *ERP Direct Costs*.
    - Click **Save as New**.
    - Click **Update.**
11. Close the Configure Columns window by clicking the (x).