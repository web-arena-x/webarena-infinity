# Configure the Financial Health Section for the Health Dashboard

Source: https://v2.support.procore.com/product-manuals/admin-company/tutorials/configure-the-financial-health-section-for-the-health-dashboard

---

## Background

Before you can view budget information in the Financial Health section, you must first set up a budget view that can be used with this dashboard.

## Things to Consider

- **Required User Permission**

 - 'Admin' on the Company Admin tool.   
     AND
 - 'Standard' or higher on the project's Budget tool.

    ##### Â Important

    - The Dashboard only includes data from the project budgets to which you have been granted access permission. If you want the Financial Health section of the Dashboard to include data from ALL of the project's in your company's account, you must be granted 'Standard' permission or higher on the Budget tool for all of your account's Procore projects.

- **Additional Information**

 - When setting up this new budget view, you should check the budget calculations in this view to make sure that they meet your business needs. "Procore Standard Budget (Custom Reporting View)" may differ from the budget views that you are currently using.

## Prerequisites

- Your company must be using Procore's Construction Financials and Project Financials tools.
- You must enable the Budget tool on your projects. See [Add and Remove Project Tools](/product-manuals/admin-project/tutorials/add-and-remove-project-tools).
- You must set up a budget view and assign it to your company's Procore projects. See [Set up a New Budget View](/process-guides/project-equipment-user-guide/assign-the-budget-view-to-a-procore-project).
- You must create a budget in all of the Procore project's that you want your data visualizations to source data from. See [Set up a Budget in a New Procore Project](/product-manuals/budget-project/tutorials/set-up-a-budget-in-a-new-procore-project).

## Steps

1. Navigate to the Company level **Admin** tool.
2. Under "Tool Settings," click **Budget**.
3. Click **Set Up New Budget View**.
4. Select **Procore Standard Budget (Custom Reporting View)**. 
   *Notes*:

   - The 'Procore Standard Budget (Custom Reporting View)' is a default view provided by Procore.
   - This view supports the following features:

     - It provides users with the ability to select the Budget as a source for a custom report in the Company level Reports tool. See [Create a Custom Company Report](/product-manuals/reports-company/tutorials/create-a-company-single-tool-report).
     - It allows the Financial Health section of the Dashboard to source data from the Procore projects to which it is assigned.
   - You can customize this view as your needs require. If you customize this view, it is recommended that you create a copy of the 'Procore Standard Budget (Custom Reporting View)' and give it a unique name.
   - For companies using the ERP Integrations tool, there are additional customization steps. For details, see [Set Up a Budget View for Custom Reporting](/product-manuals/admin-company/tutorials/set-up-a-budget-view-for-custom-reporting).
5. Click **Create**. 
   *Note*: This takes you to the view's configuration page.
6. *Optional*: Under the "Assign to Projects" drop-down menu, assign the view to projects where you want to reference the view.   
   *Notes*:

   - *Important!* Do not change the header names in the Column Configuration section. The Financial Health section uses the header names when generating data; changing the header names may cause errors.
   - The Financial Health section will still display the needed data from all active projects even if you do not assign the view to any projects.
7. Configure columns as needed. 
   *Note*: See [Set up a New Budget View](/process-guides/project-equipment-user-guide/assign-the-budget-view-to-a-procore-project).
8. Click **Done**.
9. Navigate back to the Health Dashboard in the Company level Portfolio tool.
10. View your configured Financial Health section.