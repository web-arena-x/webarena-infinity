# Create a Custom Financial Line Items Report to Compare Budget Snapshots

Source: https://v2.support.procore.com/product-manuals/reports-project/tutorials/create-a-custom-financial-line-items-report-to-compare-budget-snapshots

---

## Background

You can use Procore's custom report feature to create a custom financial line items reports to compare your project's budget snapshots. A *budget snapshot* is a picture of your budget in its current state and snapshots can be taken at different times during a project's lifecycle. For example, your project team might take a budget snapshot at the end of each month or after a forecast update. Using budget snapshots lets you analyze how your budget changes over the course of a project and you can enhance that ability by creating a financial line item report to compare your project's budget snapshots.

## Things to Consider

- **Required User Permissions:**

  - 'Admin' on the Project level Reports tool.
- **Requirements:**  
   To create and run a report with meaningful data:

  - The project must have at least one (1) budget view. See [Set Up a New Budget View](/process-guides/project-equipment-user-guide/assign-the-budget-view-to-a-procore-project).
  - The project's budget must have data. see [Set up a Budget in a New Procore Project](/product-manuals/budget-project/tutorials/set-up-a-budget-in-a-new-procore-project).
  - The project requires at least one (1) budget snapshot. See [Create a Budget Snapshot](/process-guides/budget-and-forecast-snapshots-user-guide/create-a-snapshot).

## Steps

1. Navigate to the Project level **Reports** tool.
2. Click **Create Report** and select **Single Tool Report.**
3. Do the following:

   - **Enter Report Name**Type a name for the report. This is a required field.
   - *Optional:* **Enter Description**  
     Type a description for the report.
4. Under **Tool**, expand **Financial Line Items** and click **Configurable Budget Snapshots**.
5. Use a drag-and-drop motion to add the following source columns into the **Configurable Budget Snapshots** tab of your new report.
6. Add a report filter as follows:

   - Click the **Add Filter** menu and select **Budget View**.
   - In the secondary menu that appears, you have these options:

     - To include all budget views, click **Select All**.
     - To include one (1) or more budget views, place a checkmark next to the desired budget views.   
       *Note:* If you click Clear All, the system removes the checkmark from all selected views. However, you must select at least one (1) view to add this filter to your report.
7. Group the report data by clicking the **Add Group** menu and select one **Budget Snapshot Name** or **Date**.

   ##### Â Tip

   ***Want to compare different columns from different budget views?*** You can add multiple tabs to a single report. For example, you can add one tab for the 'Procore Standard Budget View' to compare the *Projected Over/Under* column and a second tab to compare the *Buyout Savings* column in the 'Buyout Savings' view. To learn more about Procore's default budget views, see [What are Procore's standard budget views?](/faq-what-are-procores-standard-budget-views)

- Click **Create Report**.