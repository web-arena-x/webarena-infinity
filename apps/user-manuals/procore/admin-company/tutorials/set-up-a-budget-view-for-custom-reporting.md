# Set Up a Budget View for Custom Reporting

Source: https://v2.support.procore.com/product-manuals/admin-company/tutorials/set-up-a-budget-view-for-custom-reporting

---

## Background

Using the budget view feature in Procore's Company Admin tool, you can create a budget view that can then be used as a source for creating custom budget reports with the Reports tool. Using this approach will help you generate meaningful custom reports that you can adapt to fit your company's specific business needs.

## Things to Consider

- **Required User Permission**:

 - *To create custom budget report and access a project's budget data, you need both*:

    - 'Admin' on the Company Admin tool
    - 'Standard' or higher on the project's Budget tool.
 - *To run a custom budget report and a view a project's budget data*:

    - 'Admin' on the Company Admin tool.
- **Additional Information**:

 - As detailed below, you must first set up a new budget view to use with custom reporting. For easy recognition, it is recommended that you add 'Custom Reporting View' to your budget view's title.
 - If you rename your custom view, look for the tool tip next to the View name in the Budget Views list. The tool tip will display this message when you hover your mouse cursor over it: "Budget Custom Reporting will use columns from this view. The columns can be configured as needed."
 - Your 'Custom Reporting View' can then be used to create your custom budget reports. It is recommended that you use your custom view, instead of the Financial Line Item Summary report.
- **Limitations**:

 - You can only create one (1) custom reporting view per Procore company account.
 - For non-ERP integrated projects, a Direct Costs source column pulls data from the Direct Costs tool when that tool has been turned on, and it pulls data from in-line editable Direct Costs when the Direct Costs tool is off. Please note that the report will only pull in Direct Costs values for a project based on the current Direct Costs configuration for that particular project.
 - If the Custom Reporting View is using the âPercentâ format for a column, those values will not be summed up in the custom report.
- **For companies using the ERP Integrations tool**:

 - If your company has enabled the ERP Integrations tool, follow the steps in Set Up New Budget View for Custom Reporting with ERP Integrations below.

## Prerequisites

- Before you can create the calculated columns shown in this tutorial, you will first need to add the ERP Source columns. For details, see [Create a Source Column](/process-guides/project-equipment-user-guide/assign-the-budget-view-to-a-procore-project).

## Steps

- Set Up a New Budget View for Use with Custom Reporting
- Set Up a New Budget View for Custom Reporting with ERP Integrations

### Set Up a New Budget View for Use with Custom Reporting

1. Navigate to the Company **Admin** tool.
2. Under **Tool Settings**, click **Budget**.
3. Click **Set Up New Budget View**.
4. Under **Standard Views**, select the *Procore Standard Budget (Custom Reporting View)*.

   ##### Â Notes

   - By default, the available columns in the 'Procore Standard Budget (Custom Reporting View)' exactly match those in the default 'Procore Standard View.'
   - Changes that you make in one view are NOT automatically reflected in the other. For example, if you edit the 'Procore Standard Budget (Custom Reporting View),' those changes are NOT automatically reflected in the 'Procore Standard Budget' view.

 
- Edit the 'Procore Standard Budget (Custom Reporting View)' as needed.

 ##### Â Notes

 - To learn more about the options you have when editing a budget view, see [Set up a New Budget View](/process-guides/project-equipment-user-guide/assign-the-budget-view-to-a-procore-project).
 - All columns added to a budget view are available to you when creating a custom report. This includes columns that are both hidden visible and hidden. It is common for columns to be hidden when the value associated with the column is required to perform an operation defined in a visible calculated column.

- Click **Done**. 
   This makes any changes you made to the 'Procore Standard Budget (Custom Reporting View)' immediately available for use in the Reports tool.

 ##### Example

 The illustration below shows you where you can find the data columns for your 'Procore Standard Budget (Custom Reporting View)' in the Reports tool.