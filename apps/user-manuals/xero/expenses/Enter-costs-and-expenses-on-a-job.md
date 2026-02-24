# Add costs to a job

Source: https://central.xero.com/s/article/Enter-costs-and-expenses-on-a-job

---

## Overview

- Costs are the expenses you charge to a client.
- Set up standard costs for reuse, import costs, or add a one-off cost to a job.

How it works

Costs are the expenses incurred on a job that you’ll charge to your client. These are shown as line items on invoices.

There are three ways to add a cost to a job:

- [Set up standard costs](Set-up-your-standard-costs.md) for costs you use frequently, then add them to jobs as needed.
- Import a cost for a specific job.
- Create a new cost on a job as a one-off. You can change your settings so that each time you do this, it’ll be saved as a standard cost.

You need the cost admin privilege to add costs to jobs.

Import a job cost

[Prepare an import file](Import-data-into-Practice-Manager.md) using the details listed below.

| | |
| --- | --- |
| Example file | [Job Cost Import Example.csv](https://xero.my.salesforce.com/sfc/p/o0000000biwC/a/1N000000UYvi/2pD3Vo_6Dl1IQ3XLIi6L2oiDI0UmZESN4fsxCbhKP_k) |
| Required fields | Job Number, Description, Price |
| Notes | Values for the **Date** fields can use either d-m-yyyyy or d/m/yyyy format. Values for the **Billable** field can be either '0' (zero) or 'no' for a non-billable cost, or '1' (one), 'yes', or blank for a billable cost. If no value is provided for a **Quantity**, a quantity of '1' (one) is used. You can’t use an import to update existing job costs. |

Import the data.

1. In the **Business** menu, select **Settings**.
2. Under **Connections**, click **Import**.
3. For **File Type**, select **Generic - Job Cost**.
4. Select the format of your import file.
5. Click **Next**.
6. Click **Choose File** and select your import file.
7. Click **Import**.

The number of rows imported and any errors are displayed at the bottom of the screen. You may also want to spot check the details of a few job costs to verify the import.

Add or create a job cost

Tip

If you want to save a new cost to the cost list automatically, make sure you’ve selected the **When adding a cost to a job, also add costs to Cost Admin** option in the [job settings](Set-up-your-practice-settings.md) for your practice.

If you want to save this cost for later, first change your settings, or [set up a standard cost](Set-up-your-standard-costs.md).

1. In the **Jobs** menu, select **Jobs**.
2. Open the job you want to add a cost to.
3. Select the **Costs** tab.
4. Start typing a description of the cost in the **Description** field, then either:
   - Select a cost from the list of standard costs
   - Enter the description of a new cost
5. Complete the details. If you’ve selected a standard cost, any changes you make only apply to the cost on the job.
6. Click **Save**.
7. Use the checkbox to the left of the cost item to identify items as **Actual** or **Estimated** costs:
   - Select the checkbox to mark the cost item as an **Actual** cost, which includes the cost on invoices for **Actual Time and Costs**. Only actual costs are included on these invoices.
   - Clear the checkbox to mark the cost item as an **Estimated** cost, which includes the cost on invoices for **Quoted/Estimated Time and Costs**. Both actual and estimated costs are included on these invoices.

Edit or delete a job cost

When you edit or delete a job cost from a job, the changes don't affect standard costs or costs on other jobs.

### Edit a cost on a job

1. In the **Jobs** menu, select **Jobs**.
2. Click the job you want to edit a cost for.
3. Select the **Costs** tab.
4. Click the cost you want to edit.
5. Make your changes, then click **Save**.

### Delete a cost from a job

1. In the **Jobs** menu, select **Jobs**.
2. Click the job you want to delete a cost from.
3. Select the **Costs** tab.
4. Click the cost you want to delete.
5. Click **Delete**, then click **Yes**.

## What's next?

After you've added your job costs, create a [progress](Create-an-invoice.md) or [final](Create-a-final-invoice.md) invoice.