# Set up standard costs and markup

Source: https://central.xero.com/s/article/Set-up-your-standard-costs

---

## Overview

- Create or import a list of costs you use frequently in Practice Manager.
- Create standard cost with default descriptions for deposit and lump sum payments.
- Link standard costs to accounts in Xero to allocate income and cost of sales.

How it works

- Costs are the expenses that you incur when working on jobs. These costs don’t include staff labour costs, which are based on the time worked on tasks.
- For costs you use frequently, set up standard costs. These are saved in the costs list where they can also be edited or deleted.
- You can select from your standard costs to add to quotes, estimates, jobs, invoices and job templates as needed.
- Use Practice Manager to calculate the markup on costs for you. You can change or override the default markup.
- You need the cost admin privilege to set up standard costs.

Add or import a standard cost to the cost list

### Add a standard cost

1. In the **Business** menu, select **Settings**.
2. Under **Practice**, click **Costs**, then click **New Cost**.
3. Under **General Information**, complete the fields.
4. For **Unit Cost** and **Unit Price**, choose an action:
   - Click **Calculate Markup** to use a standard markup. Enter the **Unit Cost** and **Markup%**, then click **Calculate**. Practice Manager will calculate the **Unit Price** for you.
   - Enter the **Unit Cost** and **Unit Price** if you don't want to apply a standard markup.
5. Select the **Billable** checkbox if the cost will be charged to your clients.
6. Under **Tax on Invoices, Quotes and Estimates** and **Tax on Purchase Orders**, select the tax rate which commonly applies to this cost.
7. (Optional) If you've [connected Practice Manager to Xero](Connect-Practice-Manager-to-Xero.md), under **Xero Tracking**, select the **Category** and **Option** to [track the item](Set-up-tracking-categories.md) on invoices, bills and purchase orders in Xero.
8. (Optional) If you’ve connected Practice Manager to Xero, under **Interface Information**, select the **Income Account** and **Cost of Sale Account**.
9. Click **Save**.

Depending on the [job settings](Set-up-your-practice-settings.md) for your practice, you can also add a new cost to the cost list when you [add it to a job](Enter-costs-and-expenses-on-a-job.md).

### Cost fields explained

Most of the cost fields are straightforward, but the following might need an explanation:

- **Unit price** – The price of each item, calculated automatically from the unit cost and the markup. The unit price can be overridden.
- **Code** – A unique identifier, usually the supplier's reference code. It can also be used to set a default description for use with new progress invoices for deposits. All standard costs need a code as Practice Manager uses them to avoid duplicates.
- **Billable** – Select if the item is to be included in invoices for chargeable work.
- **Notes** – Any information to display for this cost on quotes or invoices.
- **Tax** – Select a tax rate for the item if it’s different from the default tax rate you use on invoices or quotes.
- **Category** – If you've connected Practice Manager and Xero, you can select a tracking category that’s set up in Xero.
- **Option** – If you've selected a tracking category, choose the options you want to track for it.

### Import a standard cost

Before you start, [prepare an import file](Import-data-into-Practice-Manager.md) using a blank file or a [cost import example file](https://xero.my.salesforce.com/sfc/p/o0000000biwC/a/1N000000UYvd/7DuMMiswMrvQqQPcY.yNTfIsttcf7NaROpoIpn5BJo8) (CSV, 223 bytes) with the following specifications:

- Code, description, cost and price are required fields.
- Use the **c****ode** field to avoid duplicating items.

To import the data:

1. In the **Business** menu, select **Settings**.
2. Under **Connections**, click **Import**.
3. For **File Type**, select **Generic - Cost**.
4. Select the format of your import file.
5. Click **Next**.
6. Click **Choose File** and select your import file.
7. Click **Import**.

The number of rows imported and any errors are displayed at the bottom of the screen. You might also want to spot check a few standard costs to verify the import.

Set a default description for deposit or lump sum payment invoices

To set a default description for deposit and lump sum payments, create a standard cost and use the **Code** field as below. These descriptions apply to new [progress invoices](Create-an-invoice.md).

1. In the **Business** menu, select **Settings**.
2. Under **Practice**, click **Costs**, then click **New Cost**.
3. For **Description**, enter the default description for progress invoices.
4. In the **Unit Cost** and **Unit Price** fields, enter 0. You’ll provide correct values in the invoices you create later.
5. In the **Code** field, enter one of the following code values:
   - PROGRESS-INVOICE – the description will be used for invoices based on a lump sum.
   - PERCENTAGE-INVOICE – the description will be used for invoices based on a percentage of the originally quoted value for the job. The quote must be approved for this to display when creating a deposit invoice.
6. Click **Save**.

Connect costs to accounts in Xero

If you’ve connected Practice Manager to Xero, you can [link a cost](Mapping-account-codes-to-Xero.md) to a specific income account and cost of sale account. This allocates income for jobs that include the cost to the correct general ledger accounts.

If you change any of your accounts in Xero, you must adjust the linked account in Practice Manager.

You can update the accounts for each cost individually. If you want to link multiple costs to the same account, you can do this in bulk.

To link a cost to an income or cost of sale account:

1. In the **Business** menu, select **Settings**.
2. Under **Practice**, click **Costs**, then select the **Accounting Interface** tab.
3. Select the required account status to display:
   - **Unallocated** – costs have one or no accounts allocated
   - **Allocated** – costs have both accounts allocated
   - **All costs** – costs have one, both or no accounts allocated
4. Select the checkbox next to each cost you want to update.
5. Select the **Income Account** and **Cost of Sale Account** you want to allocate the costs to. The option **select account** removes the account allocation.
6. Click **Apply**.

Accounts display in a drop-list if you’ve linked Practice Manager and Xero. Otherwise, you’ll see a field.

Edit or delete a standard cost

### Edit a cost

1. In the **Business** menu, select **Settings**.
2. Under **Practice**, click **Costs**.
3. Find and open the cost you want to edit.
4. Make your changes, then click **Save**.

### Delete a cost

1. In the **Business** menu, select **Settings**.
2. Under **Practice**, click **Costs**.
3. Find and open the cost you want to delete.
4. Click **Delete Cost**, then click **Yes** to confirm.

## What's next?

After you've created your standard costs, add them to your [quotes](Add-costs-to-quotes-apply-markup.md), [jobs](Enter-costs-and-expenses-on-a-job.md), [invoices](Add-costs-to-invoices-apply-markup.md) and [job templates](Manage-tasks-costs-and-milestones-on-job-templates.md).