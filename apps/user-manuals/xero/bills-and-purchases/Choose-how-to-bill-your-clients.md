# Choose how to invoice your clients

Source: https://central.xero.com/s/article/Choose-how-to-bill-your-clients

---

## Overview

- Choose an invoicing method to determine how you invoice your clients.
- Practice Manager applies invoicing rates in a specific order.

## Choose an invoicing method

The invoicing method determines how you invoice your clients. There are two methods to choose from:

- An agreed fixed price when you create a [quote](Create-a-quote-in-Practice-Manager.md) or [invoice](Create-an-invoice.md) for a job
- A task invoice rate based on a specific task (task billable rate) or staff member (staff billable rate)

The task invoice rate can be a:

- **Task Billable Rate** – The same hourly rate will be charged regardless of who’s working on it. If you select this rate, the staff billable rates or custom staff billable rates won’t apply.
- **Staff Billable Rate**– The rate is based on which staff member is doing the work. The jobs you create use this setting to determine the invoicing method. If you change this setting, it will only apply to new jobs.

To select a task invoice rate:

1. In the **Business** menu, select **Settings**.
2. Under **Practice**, click **Practice Settings**.
3. Under **Job**, select a **Task Invoice Rate**. If you select a:
   - **Task Billable Rate** set **Time Allocation** to **Staff** or **Task**
   - **Staff Billable Rate** set **Time Allocation** to **Staff**, or you won't be able to save your current changes
4. Click **Save**.

If you want to apply job-specific rates for individual jobs, you can [set a custom job rate](/s/article/Set-custom-job-rates?userregion=true). This will override the above task invoice rate setting.

## Order of invoice rates explained

### How it works

When you create an invoice, Practice Manager applies invoicing rates in a specific order. If a particular rate has been set up, then each subsequent rate overrides the previous one:

- Use the default **Task Billable Rate** or **Staff Billable Rate** based on the setting of the **Task Invoice Rate**. If you select **Task Billable Rate**, the staff billable rates or custom staff billable rates won’t apply.
- If there’s a custom staff rate for a task, use it instead.
- If there’s a custom task rate for a client, use that rate instead.
- If there’s a custom task or staff rate for a job when working on the job, use the **Task Billable Rate** or **Staff Billable Rate** based on the job's set **Task Invoice Rate**.

### Historic invoicing rates

You can change the invoicing rates for a staff member or task while a job is in progress. To transition from the old rate to the new rate for reporting and invoicing purposes, you can apply [historic invoicing rates](Lock-staff-and-task-billable-rates.md).

### Default invoicing rates

The [default invoicing rates](Set-up-default-invoicing-rates.md) consist of a base and billable rate which you can set for each [new staff member](/s/article/Add-staff#AddastaffmembertoPracticeManager?userregion=true) or [task](Set-up-your-tasks.md).

These rates are used for all invoicing and reporting unless you set up historic invoicing rates or use custom invoicing rates.

### Custom invoicing rates

Use custom invoicing rates to apply specific rates to specific staff, clients, jobs and tasks. You can set a:

- Custom staff rate for a task or job
- Custom task rate for a client or job

## What's next?

Once you’ve chosen an invoicing method, you can decide whether you want to set up a [default rate](Set-up-default-invoicing-rates.md) or a [custom invoicing rate](Set-up-custom-billing-rates.md).