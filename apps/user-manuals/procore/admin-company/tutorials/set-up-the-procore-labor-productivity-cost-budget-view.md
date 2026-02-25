# Set Up the Procore Labor Productivity Cost Budget View

Source: https://v2.support.procore.com/product-manuals/admin-company/tutorials/set-up-the-procore-labor-productivity-cost-budget-view

---

## Background

The 'Procore Labor Productivity Cost' budget view provides project teams with the ability to include production quantities on the project's budget. See [What are 'production quantities'?](/faq-what-are-production-quantities) Building off the [Real-Time Labor Costing](https://support.procore.com/tc/procore/Legacy/Release%5FDocumentation%5FArchives/2020/Project%5FFinancials:%5FReal-Time%5FLabor%5FProductivity%5Fand%5FUnit-Based%5FBudgets) feature, the 'Procore Labor Productivity Cost' budget view is designed to provide self-performing and specialty contractors with the ability to gain greater insight into your project's production rates to make better decisions that maximize profit margins. With this release, you can:

- Add and import production units to a project's budget in Procore's Financial Management tools: Budget, Change Events, and Change Orders.
- Collect production units from field personnel with Timecard Entries in the Daily Log and both the Timecards and Timesheets tools.
- Track and compare budgeted production units to installed production units using Procore's Budget and Reports tools.

By default, Procore provides its users with a standard 'Procore Labor Productivity Cost' budget view, which is available to your company's [Procore Administrator](https://support.procore.com/procore-learning-paths/general-contractor/procore-administrator) in the Company level Admin tool.

##### Example

**Procore Labor Productivity Cost Budget View in the Budget Tool**

The illustration below shows you the recommended layout for the 'Procore Labor Productivity Cost' budget view, as it will look when applied to your project's Budget tool.

## Things to Consider

- **Required User Permission**:

 - *To add or edit a budget view*, 'Admin' on the Company Admin tool. 
    *Note*: Your company's Procore account must be using Procore's Project Financials and Resource Tracking tools.
- **Additional Information**:
- - Your field team can enter or import timecard entry hours using the appropriate tutorials for these project tools:\* [My Time (Android)](/product-manuals/my-time-ios/)\* [My Time (iOS)](/product-manuals/my-time-ios/)\* [Timecard](https://support.procore.com/products/online/user-guide/company-level/timecard)\* [Timesheets](https://support.procore.com/products/online/user-guide/project-level/timesheets)
 - Your budget team can add budget line items or import budget data, budgeted production quantities, and installed quantities using these tutorials:\* [Add a Budget Line Item](/process-guides/resource-tracking-and-project-financials-setup-guide/add-a-budget-line-item)\* [Import a Budget](/process-guides/resource-tracking-and-project-financials-setup-guide/import-a-budget)\* [Import a Unit Quantity Based Budget](/process-guides/resource-tracking-and-unit-quantity-based-budget-setup-guide/import-your-budget)\* [Add Budgeted Production Quantities to a Project's Budget](/process-guides/resource-tracking-and-project-financials-setup-guide/add-budgeted-production-quantities)\* [Import Installed Quantities for the Labor Productivity Cost Budget View](/process-guides/resource-tracking-and-project-financials-setup-guide/import-installed-quantities)
 - Your team can log changes to budgeted quantities and hours using the Unit of Measure (UOM) features in the 'Production Quantities' tab of the Change Events tool. See [Record Changes to Production Quantities in a Change Event](/process-guides/resource-tracking-and-project-financials-setup-guide/record-changes-on-a-change-event).
 - Your team can log changes to budgeted production quantities using the UOM features in the 'Production Quantities' tab on a Prime Potential Change Order (Prime PCO). See [Record Changes to Production Quantities on a Potential Change Order for a Prime Contract](/process-guides/resource-tracking-and-project-financials-setup-guide/record-changes-for-a-prime-contract).
 - Your team can also update production quantities and hours using the UOM features your project's Prime Contract Change Orders (PCCOs). 
    *Note*: When PCCOs are placed in the 'Approved' status (see [Approve or Reject Prime Contract Change Orders](/product-manuals/change-orders-project/tutorials/approve-or-reject-prime-contract-change-orders)), it automatically updates data in the Procore Labor Productivity Cost budget view and the Field Production Report. See [View a Field Production Report](/process-guides/resource-tracking-and-unit-quantity-based-budget-setup-guide/view-the-field-production-report).
- **Limitations**: 
   If you are using this budget view on your Procore project:

 - For companies using the ERP Integrations tool, you will NOT be able to add the 'Actual Cost' or 'Actual Units' columns, without performing the additional configuration steps noted below.

## Prerequisites

- Verify that the Timesheets tool is active in your company's Procore account. 
 *Note*: To do this, navigate to the Company Admin tool. Under Company Settings, click Account Information. Under Resource Management, verify that Timesheets is 'Licensed.'
- Assign the Default Cost Type for timecard entries in the Company level Timesheets tool. See [Configure Settings: Company Level Timesheets](/product-manuals/timesheets-company/tutorials/configure-advanced-settings-company-level-timesheets).
- Add the following tools to the Project Tools menu. See [Add and Remove Project Tools](/product-manuals/admin-project/tutorials/add-and-remove-project-tools).

 - Direct Costs
 - Prime Contracts
 - *Optional* *:* Timecards
 - Timesheets
 - Budget

## Steps

- Step 1: Create a New Budget View
- Step 2: *Optional:* Customize the Budget View
- Step 3: Preview the Budget View
- Step 4: Assign the Budget View to a Procore Project

### Step 1: Create a New Budget View

1. Navigate to the Company **Admin** tool.
2. Under **Tool Settings**, click **Budget**.
3. Click **Set Up New Budget View**.
4. Under **Standard Views**, highlight **Procore Labor Productivity Cost**.
5. Click **Create**.
6. Name your view as follows:

   - **View Name**. Enter a name for your new view. In this example, we named it: Labor Productivity Cost
   - **View Description**. Enter a description for your view. In this example, we entered: Recommended view for labor cost productivity report
7. Click **Configure Columns**. 
    This opens the Configure Columns window pictured below. From this point, continue with Step 2: (Optional) Customize the Budget View.

### Step 2: Optional: Customize the Budget View

If you want to customize the Procore Labor Productivity Cost budget view, you can click the **Configure Columns** button. This opens the Configure Columns window, which allows you to edit the budget view. To learn about your editing options, see [Configure the Columns for a Budget View](/process-guides/project-equipment-user-guide/assign-the-budget-view-to-a-procore-project) in the [Set Up a New Budget View](/process-guides/project-equipment-user-guide/assign-the-budget-view-to-a-procore-project) tutorial. When you are finished, click the 'x' in the Configure Columns window to close it.

### Step 3: Preview the Budget View

After closing the Configure Columns window, the system returns you to the new budget view's window. Under **Column Configuration**, you can get an idea of how your budget view will look in Procore by selecting a project from the **Preview with Project** drop-down list.

### Step 4: Assign the Budget View to a Procore Project

1. In the 'Procore Labor Productivity Cost' view window, place checkmarks next to project boxes of your choice in the **Assign to Projects** list.

   - To assign the budget view to all of your company's Procore projects, place a checkmark in the **All Projects Selected** box.   
     *Notes*:\* For companies using the ERP Integrations tool, you will see the 'All Project Using ERP Direct Costs' checkbox.\* You may also see the 'All Projects Using Procore Direct Costs' checkbox. However, it only appears when the Direct Costs tool is enabled on the project.
   - To assign the budget view to one (1) or more projects, place a checkmark next to the desired projects.
2. Click **Done**.

##### Â Tip

After completing all of the above steps, you can provide your project teams with instructions for applying the budget view to their project budgets. For details, see [Apply the View, Snapshot, Group, and Filter Options on a Budget View](/process-guides/project-equipment-user-guide/apply-the-budget-view-to-your-budget).