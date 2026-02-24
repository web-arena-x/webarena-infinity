# Create and manage your tasks

Source: https://central.xero.com/s/article/Set-up-your-tasks

---

## Overview

- Create tasks to estimate, record and charge for time worked.
- Edit and delete your tasks as needed, and connect tasks to an income account.

How it works

- Practice Manager saves new or imported tasks to the task list where you can edit or delete them.
- Add tasks to as many [jobs](Job-tasks.md), [job templates](Manage-tasks-costs-and-milestones-on-job-templates.md), [quotes](Add-edit-delete-tasks-from-quotes.md) and [invoices](Add-edit-delete-tasks-from-invoices.md) as you want. This won't affect tasks on the task list.
- Tasks display as invoice line items. You can give each task a different [billing rate](Choose-how-to-bill-your-clients.md).
- If you've [connected Practice Manager to Xero](Connect-Practice-Manager-to-Xero.md), you can [link tasks](Mapping-account-codes-to-Xero.md) to specific general ledger accounts.

Create or import a task

### Create a task

1. In the **Business** menu, select **Settings**.
2. Under **Practice,**click**Tasks**.
3. Click **New Task**.
4. Under **General Information**, enter a name and description for the task. The description displays in the quotes, jobs and invoices that use this task.
5. Under **Billing Information**, enter the base and billable rates for the task. These rates are used if you [choose to bill clients](Choose-how-to-bill-your-clients.md) using the [task billable rate](Set-up-default-invoicing-rates.md).
6. (Optional) If you've connected Practice Manager and Xero:
   - Under **Xero Tracking**,select a **Category** and **Option** to [track the task](Set-up-tracking-categories.md) on invoices, bills and purchase orders in Xero.
   - Enter the **Export Code** and select the **Income Account** used by Xero to set a [general ledger account](Mapping-account-codes-to-Xero.md).
7. Click **Save**.

### Import a task

Before you start, [prepare an import file](Import-data-into-Practice-Manager.md) using the following details:

Example file: [Tasks Import Example.csv](https://xero.my.salesforce.com/sfc/p/o0000000biwC/a/1N000000UYw2/7kgD3L8OtIRjJl7jvJ45g7E06DWpSNF05Qm99tjQooE)

Required fields: name, base\_rate, billable\_rate

To import the data:

1. In the **Business** menu, select **Settings**.
2. Under **Connections**, click **Import**.
3. For **File Type**, select **Generic - Task**.
4. Select the format of your import file.
5. To update the existing data, select the checkbox.
6. Click **Choose File** and select your import file.
7. Click **Import**.

The number of rows imported and any errors display at the bottom of the screen. To verify the import, you can spot check a few tasks.

Connect tasks to an income account

If you’ve connected Practice Manager to Xero, you can [link a task](Mapping-account-codes-to-Xero.md) to a specific income account. This allocates income for jobs that include the task to the correct general ledger account.

If any of your Xero income accounts change, you must adjust the linked account in Practice Manager.

To update an income account for:

- A single task – edit the task in the tasks list
- Multiple tasks – update your task settings

To update your task settings:

1. In the **Business** menu, select **Settings**.
2. Under **Practice**, click **Tasks**, then select the **Accounting Interface** tab.
3. Select the required account status to display, **Unallocated**, **Allocated** or **All**.
4. Select the checkbox of each task you want to update.
5. Select the **Income Account** you want to allocate the tasks to.
6. (Optional) To remove an account from the task, for **Income Account** select **(select account)**.
7. Click **Apply**.

Tip

Accounts display in a drop-list if you’ve linked Practice Manager and Xero. Otherwise, you’ll see a field.

Edit a task on the task list

1. In the **Business** menu, select **Settings**.
2. Under **Practice**, click **Tasks**.
3. Click the task you want to edit.
4. Make your changes, then click **Save**.

Delete a task from the task list

1. In the **Business** menu, select **Settings**.
2. Under **Practice**, click **Tasks**.
3. Click the task you want to delete.
4. Click **Delete Task**, then click **Yes** to confirm.

## What's next?

[Add a task to a job](Job-tasks.md) so you can record time against it.