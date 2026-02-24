# Create or edit a job

Source: https://central.xero.com/s/article/Create-or-edit-a-job

---

## Overview

- Create a job to record time and costs on a project for a client.
- If you already have an existing job or job template, create a new job from it to save time, then edit it to add or correct details.
- You can also create a job from a quote or by importing a job.

Before you start

The client must exist in Practice Manager before you can create a job for them. If you're adding a new client, [add a contact person for the client](Create-a-client-in-Practice-Manager.md) as well.

It's also a good idea to customise your [job settings](About-jobs.md) before you create a job to simplify the job setup process and better manage your organisation's workflow.

If you won't invoice for any time recorded against the job, select **Exclude from Estimated Billings** to exclude the job from the work in progress list.

Create, copy or import a job

### Create a job

Create a job to record time and costs on a project for a client.

1. In the **Jobs** menu, select **Jobs**.
2. Click **Create new job**.
3. Select or add the client the job is for.
4. Complete the details.
5. (Optional) Under **Schedule Information**, [assign staff](View-staff-allocation.md) to the job.
6. Click **Save**.

### Copy a job

Create a new job from an existing job, then edit it to add or update the details.

1. In the **Jobs** menu, select **Jobs**.
2. Open the job you want to copy.
3. Hover over **Options**, then select **Copy Job**.
4. Change the job name and edit details as required.
5. Click **Save**.

### Import jobs

Tip

Recurring jobs and job budgets can’t be imported. You need to create it manually.

[Prepare an import file](Import-data-into-Practice-Manager.md) using the details listed below.

| | |
| --- | --- |
| Example file | [Job Import Example.csv](https://xero.my.salesforce.com/sfc/p/o0000000biwC/a/1N000000UYvn/2pgcL0owWaGIZFMqDQ1g9Sk.GP2GEGZpu19wjMCUMHs) |
| Required fields | Job Number, Name, Client, Start Date, Due Date |
| Job Import Options | **State** – The job state that will be applied to the imported data. **Category** (optional) – The job category, if required. **Template** (optional) – The job template to use, if required. These import options need to be grouped into the state, category or template first, then imported separately. Different import options can’t be imported in the same file. |
| Notes | Values for the **Start Date** and **Due Date** fields can use either d-m-yyyy or d/m/yyyy format. You can’t enter dates further in the future than 2030. You can’t use an import to update existing jobs. You can’t import custom job fields. |

To import the data:

1. In the **Business** menu, select **Settings**.
2. Under **Connections**, click **Import**.
3. For **File Type**, select **Generic - Job**.
4. Select the format of your import file, then click **Next**.
5. Select a job state and any other applicable options.
6. Click **Choose File**, then select your import file.
7. Click **Import**.

The number of rows imported and any errors are displayed at the bottom of the screen. You might also want to spot check the details of a few jobs to verify the import.

Create a job from a template or quote

### Create a job from a template

Use a job template to create a job with the same structure.

1. In the **Jobs** menu, select **Jobs**.
2. Click **Create new job**.
3. Under **Job Information**, select a job template.
4. Complete the fields.
5. If you won't invoice for any time recorded against the job, select **Exclude from Estimated Billings**.
6. Click **Save**.

You can add extra templates to a job, to include those template items on the job as well.

1. In the **Jobs** menu, select **Jobs**.
2. Open the job you want to add templates to.
3. Hover over **Options**, then select **Apply Additional Templates**.
4. Select one or more templates from the list. If a task isn’t already on the job, it will be added to it.
5. (Optional) If tasks will be duplicated, choose how they’ll be handled. Select:
   - **Add additional tasks to the job** – to add the new tasks alongside the existing ones
   - **Append to existing tasks on the job** – to combine the time estimates and show a single task
6. Click **Save**.

### Create a job from a quote

Quotes and estimates convert to jobs [when they are accepted](Save-issue-or-accept-a-quote-in-Practice-Manager.md).

Edit a job

Edit a job to add or change details.

1. In the **Jobs** menu, select **Jobs**.
2. Open the job you want to edit.
3. Click **Edit Job**.
4. Make your changes.
5. Click **Save**.

## What's next?

[Create a task](Set-up-your-tasks.md) and [add it to the new job](Job-tasks.md).