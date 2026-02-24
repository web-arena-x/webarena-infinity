# Automatic activity statements

Source: https://central.xero.com/s/article/Automatic-activity-statements

---

## Overview

- Enable the automatic creation of activity statements for any clients with an outstanding obligation.
- Select up to six staff members to be emailed each time the process is run.
- You can run the process outside the scheduled time to check for missing obligations.

How it works

Automatic activity statements is a scheduled process that creates an activity statement for any clients with outstanding obligations. This runs at 8am AEST on the first three days of each month, and uses the list obligation to create the statements.

The process can take up to three hours, and identifies all your clients that have **Yes** selected for **Prepare Activity Statements** in their client record. They also need to have previously created an activity statement within the last 120 days. New clients need to have an activity statement created manually before they can be included in this process.

You can still [create manual activity statements](Activity-statements.md) for your clients if the automated process is turned on. To enable automatic activity statements, you’ll need to have the administrator user privilege.

The **History** tab in the **ATO Online Services** section shows the status of the feature and the staff member who changed the setting. If you receive an error when running the automatic activity statement service, you can view the error details and the clients impacted in the **History** tab.

Enable automatic activity statements

Xero Tax Practice Manager

1. In the **Business** menu, select **Settings**.
2. Click **ATO Online Services**.
3. In the **Automatic Activity Statement** section, select the **Enable Automatic Activity Statement** checkbox.

When the scheduled task is run each month, all the activity statements that are created will appear under the **Tax Returns** tab of the client record.

1. In the **Business** menu, select **Settings**.
2. Click **ATO Online Services**.
3. In the **Automatic Activity Statement** section, select the **Enable Automatic Activity Statement** checkbox.

As Practice Manager requires activity statements to be created within jobs, there are three ways to do this:

### Create Activity Statements in the most recent existing (or recurring) job for the client

The automated task will add the activity statement to the last job created for each client.

Most practices that set up [recurring jobs](Recurring-jobs.md) for their clients will set the creation date of these jobs to the first or last day of the month. As this aligns with the automated task, this should be the easiest way for you to manage the auto-creation of activity statements and jobs.

If there's no previous job for a client, a new one will be created using the template**[Automatic Activity Statement Job]**.

### Create Activity Statements in a newly-generated job

Practice Manager will create a new job for each activity statement. If multiple outstanding obligations are found, Practice Manager will create a new job for each one.

The template name for this job will be **[Automatic Activity Statement Job] [month] [year]**, eg Automatic Activity Statement Job September 2019.

### Create all Activity Statements for a given year in a single job for the client

Practice Manager will create a new job, and all activity statements created for the year will be linked to this job. If outstanding obligations are found across multiple years, Practice Manager will create a new yearly job for each relevant year.

The template name for this job will be **[Automatic Activity Statement Job] [year]**, eg Automatic Activity Statement Job 2019.

Warning

If you change the auto-generated job name, the system won’t recognise the existing job, and will create a new yearly one.

Notify staff the process has been run

In the **Notify via email** field, you can add up to six staff members to be notified when the process is run. Note that each staff member must be a user in your account to be added here.

The email will show the total results of the task run for the practice. This includes:

- How many activity statements were created
- How many were not created
- How many failed due to error

Perform an unscheduled run

You have the option to run the automatic activity statement process on an adhoc basis.

This may take up to three hours to run. Once you’ve started, the option to do this will be disabled until the previous process is completed.

1. In the **Business** menu, select **Settings**.
2. Click **ATO Online Services**.
3. In the **Automatic Activity Statement** section, click the **Run now** button.

Choose when to create auto activity statements

Automatic activity statements create all outstanding activity statements for every client with **Prepare Activity Statements** selected. This process is a scheduled task that runs on the first three days of every month.

You can choose to automatically create any combination of monthly, quarterly and annual activity statements. This could be done when a client manages their own monthly activity statement lodgments, but you look after the quarterly or yearly lodgments.

To do this:

1. From the **Clients** menu, select the client you want to create the activity statement for.
2. Click **Options**, then **Edit**.
3. In the **Tax and Company** section, ensure the **Prepare Activity Statements** checkbox is selected.
4. Select the relevant boxes from the following options for **Automatically Retrieve from ATO**:
   - **Monthly** – Only forms with the monthly option will be created.
   - **Quarterly** – Only forms with the quarterly option will be created.
   - **Annually** – Only forms with the annual option will be created.
   - **Opt-Out** – No forms will be created.
5. Click **Save**.

By default, all activity statements available for the client (ie **Monthly**, **Quarterly** and **Annually**) are created automatically. If you clear an option, this means the client/tax payer will handle that lodgment.

If you select **Annually** and the client doesn’t have other activity statements created manually during the year, the client's annual GST return might not be created automatically due to the 120 day limitation. A practice staff member might need to manually create an annual activity statement for the client every year.

If you re-save the client details page manually, these individual options appear in the **Automatically Retrieve from ATO** field. There's no option to bulk update this field.

Tip

To reset the default options, clear the **Prepare Activity Statements** checkbox and re-select.

## What's next?

Make sure your BAS client details are correct to ensure they’re included in this process. If you need to update them, you can manually [edit the client record](/s/article/Edit-a-client-in-Practice-Manager-NZ-AU) or [bulk update from the BAS or Tax Agent Portal](Import-client-data-into-Xero-Tax.md).