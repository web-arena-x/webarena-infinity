# Check Synced ERP Job Costs for Accuracy

Source: https://v2.support.procore.com/product-manuals/budget-project/tutorials/how-do-i-check-my-synced-erp-job-costs-for-accuracy

---

## Background

For ERP Connectors that offer transactional syncing, there can be occasional discrepancies in the values for Job Costs on a project.

## Things to Consider

- **Required User Permissions**:

 - 'Admin' on the Company Admin tool.
- **Additional Information**:

 - To set up a budget view for real-time labor productivity, see [Resource Tracking and Project Financials: Setup Guide](/process-guides/resource-tracking-and-project-financials-setup-guide/).
 - To set up a labor productivity cost budget view, see [Set Up the Procore Labor Productivity Cost Budget View](/product-manuals/admin-company/tutorials/set-up-the-procore-labor-productivity-cost-budget-view).
 - Any user with 'Read Only' permission or higher on the Budget tool has access permission to apply the view to a project's budget. See [Apply the View, Snapshot, Group, and Filter Options on a Budget or Forecasting View](/product-manuals/budget-project/tutorials/apply-the-view-snapshot-group-and-filter-options-on-a-budget-view).
- For companies using the ERP Integrations tool: **Show/Hide**

 - If your company account is using the ERP Integrations tool, Procore automatically provides you with a budget view for your 

    In Procore, the term *integrated ERP System*, is used to refer to *Enterprise Resource Planning (ERP)* software applications that can be configured to exchange data between Procore and a supported application using the Company level ERP Integrations tool. See [Which ERP integrations are supported by Procore?](/faq-which-erp-integrations-are-supported-by-procore)

    Integrated ERP System. See [Which ERP integrations are supported by Procore?](/faq-which-erp-integrations-are-supported-by-procore) for details about your specific ERP connector.
 - Any custom budget views that you create for an ERP Integration must contain all of the required ERP data columns. This ensures that Procore can send the required budget data to the company's ERP Integrations tool for acceptance for export to the integrated ERP system by an 

    In Procore, an *Accounting Approver* is an individual with the authority to accept and reject Procore data for export to an integrated ERP system. Accounting approvers can unlink several item types, such as commitments, commitment change orders, prime contract change orders, and subcontractor invoices, that have been synced between Procore and an integrated ERP system. See [Which ERP Integrations are supported by Procore?](/faq-which-erp-integrations-are-supported-by-procore)

    Accounting Approver. See [Send a Budget to ERP Integrations for Accounting Acceptance.](/product-manuals/erp-integrations-company/tutorials/send-a-budget-to-erp-integrations-for-accounting-acceptance)

## Steps

#### Create a new Budget View

1. Navigate to the company's **Admin** tool.
2. Under 'Tool Settings', click **Budget**.

   ##### Â Tip

   **Did you know you can also launch the 'Budget Views' page directly from the project's Budget tool?** A Procore Administrator can open the 'Budget Views' page in the Company Admin tool directly from a project's budget. To do this, maximize the right sidebar in the Budget tool when viewing the 'Budget' tab. Under the 'Configurations' section, click the **Configure Budgeting Views** link.

- Click **Set Up New Budget View**.
- In the **Setup a New Budget** window, select the **Procore ERP Direct Cost Budget** and click **Create.**
- Click **Configure Columns.**

#### Create a Source Column to display transactional Job Cost values in:

1. Click **Create Source Column.**
2. Configure the New Source column.

   - Enter 'Transactional Job Costs' in the **Column Name** field.
   - Select **Direct Costs** in the **Column Source** field.
3. Select the following filters:

   - **Type.** Add checkmarks to the boxes next to the following item types:

     - **Invoice**
     - **Expense**
     - **Payroll**
     - **Subcontractor Invoices**
   - **Status.** Add a checkmark to the **Approved** status.
   - Click **Save** to save your source column configuration.

#### Create a Source Column to display ERP Job Cost values in:

1. Click **Create Source Column.**
2. Configure the New Source column.

   - Enter ERP Job Costs in the **Column Name** field.
   - Select **ERP Job Costs** in the **Column Source** field.
3. Click **Save** to save your source column configuration.

#### Create a Calculated Column to determine the variance:

1. Click **Create Calculated Column.**
2. Configure the **New Formula** column:

   - Enter 'Variance' in the **Column Name** field.
   - Select **Currency** in the **Format** drop-down menu.
   - In the first **Pick a Column** drop-down menu, select **ERP Job Costs.**
   - Select **Subtract (-)** from the Operations drop-down menu.
   - In the second **Pick a Column** drop-down menu, select **Transactional Job Costs**.
   - Click **Save** to save the new calculated column.

After closing the Configure Columns window, the system returns you to the new budget view's window, where you can preview the new view and assign it to your projects.

**Assign to Projects.** Place a checkmark next to the desired projects in the drop-down menu.

**Preview with Project.** Select a project from the drop-down menu to preview with the new view applied. In the Preview, the newly created columns will appear to the right of the table.

If you find any unexpected variance(s), to confirm the steps to resolve.