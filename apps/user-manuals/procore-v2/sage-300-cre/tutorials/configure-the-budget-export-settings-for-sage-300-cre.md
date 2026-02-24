# Configure the ERP Budget Export Settings for Sage 300 CREÂ®

Source: https://v2.support.procore.com/product-manuals/sage-300-cre/tutorials/configure-the-budget-export-settings-for-sage-300-cre

---

## Background

For companies using the ERP Integrations tool to sync data between Procore and Sage 300 CREÂ®, you can specify several configuration settings for the export process using the controls in a project's Budget tool on the ERP Settings page.

## Things to Consider

- **Required User Permissions:**

  - 'Admin' level permissions on the project's Budget tool.

## Prerequisites

- Enable the ERP Integrations tool on the company's Procore account.
- Integrate your company's Procore account with Sage 300 CREÂ®.
- Add the Sage 300 CREÂ® Job to your company's ERP Integrations tool.
- Ensure the project's cost codes are updated with the synced job in Sage 300 CREÂ®.
- Ensure the Budget tool has been added to Procore's Project Tools menu.

## Steps

1. Navigate to the project's **Budget** tool.
2. Click **Configure Settings**.
3. Click **ERP Settings**.
4. Under **ERP Budget Export Settings**, set your configuration preferences as follows:

   - **Export Forecast Amounts**  
      Place a checkmark in this box to export any updated forecast values for all of the budget line items on the project. Remove a checkmark to omit forecast values from the export process.
   - **Default ERP Budget View**  
      Select one of your company's budget views from the list box. Your budget view selection must contain the 'Forecast to Complete' column. See [Use the 'Forecast to Complete' Feature](/product-manuals/budget-project/tutorials/use-the-forecast-to-complete-feature). The budget view you select here will export the 'Forecast to Complete' value and the value in the 'Designated Estimated Cost At Completion Column' that you specify next.

     ##### Â Notes

     - You can select one (1) ERP budget view per project.
     - Your company's Procore Administrator creates budget views and assigns them to projects in your company's Procore account using the Company level Admin tool. See [Set up a New Budget View](/product-manuals/admin-company/tutorials/set-up-a-new-budget-view).

- **Designated Estimated Cost At Completion Column**  
   Select a column from your ERP budget view. This value will be exported to Sage 300 CREÂ® every time a user exports a budget from Procore.
- Click **Update**.