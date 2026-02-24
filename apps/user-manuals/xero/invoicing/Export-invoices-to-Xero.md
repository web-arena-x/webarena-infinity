# Export invoices from Practice Manager to Xero

Source: https://central.xero.com/s/article/Export-invoices-to-Xero

---

## Overview

- Export invoices you've created in Practice Manager to Xero.
- Set your preferences for the details shown in Xero.

How invoices are exported to Xero

- Once you've [connected Practice Manager to Xero](Connect-Practice-Manager-to-Xero.md), every invoice you approve in Practice Manager exports immediately to Xero. If you edit an approved invoice, you need to export it to Xero again manually.
- Practice Manager only exports the contact name, email and salutation to Xero, overwriting any existing details. It doesn't automatically export all of the client details on invoices so you'll need to enter them manually.
- Practice Manager doesn't export payments or credits applied to invoices. In Xero, you'll need to manually apply payments and credits to invoices exported from Practice Manager.

Select your invoice preferences

### About invoice numbering

You can either use the Xero numbering system for both Practice Manager and Xero or use a [separate number sequence](Edit-job-invoice-and-quote-numbers.md) for Practice Manager invoices.

- **Xero** – Use Xero invoice numbers for your exported invoices in both Xero and Practice Manager. This is helpful if you invoice directly from your Xero account and makes it easier to reconcile invoices between the systems.
- **Xero Practice Manager** – Use invoice numbers from Practice Manager for your exported invoices in both Xero and Practice Manager. This makes it easy to identify the source of each invoice.

### Set your preferences

1. In the **Business**menu, select **Settings**.
2. Under **Connections**, select **Xero**.
3. Under **Invoices**:
   - For **Export as**, we recommend you select **Draft** until you’re sure the export is set up correctly. This determines how your invoices are recorded in Xero after export.
   - For **Invoice Number Sequence**, select **Xero** or **Xero Practice Manager**.
   - Select **Include Invoice Description** to include the invoice description on the exported invoices.
4. Click **Save**.

Choose the amount of invoice detail exported

### What you need to know

You can export invoice information to Xero with two levels of detail. Either export details of individual tasks and costs, or export only the job or invoice total.

When you export the total:

- If there’s only one job on the invoice, a single total is displayed
- If there are multiple jobs on the invoice, you’ll see a line for each job

Exporting the total might not be the best choice for your practice if you do any of the following:

- Map your tasks and costs to accounts in Xero. Xero maps to the job category level instead, or to default mappings if you don’t use job categories.
- Use the Xero tracking option at the task and costs level. Xero maps to the job category level instead, or to default mappings if you don’t use job categories.
- Include your timesheet notes on tasks. Timesheet notes are included in a single field on invoices.

### Display details for tasks and costs

1. In the **Business** menu, select **Settings**.
2. Under **Connections**, select **Xero**.
3. Under **Invoices**, for **Details**, select **Individual tasks and costs**.
4. Complete the **Job Summary**. Enter any text and placeholders you want to include on job invoices.
5. Select task and cost options:
   - **Show task description** – to display the task description in the **Notes** field on the job’s **Time Sheet** tab
   - **Show tasks with zero value** – to show clients work you’re doing and items you’re purchasing without charging for
   - **Show cost notes** – to display cost notes in the **Notes** field on the job’s **Cost** tab
   - **Show costs with zero value** – to show clients costs you’ve incurred without charging for
6. Click **Save**.

### Display a single total

1. In the **Business** menu, select **Settings**.
2. Under **Connections**, select **Xero**.
3. Under **Invoices**, for **Details**, select **Job or miscellaneous invoice total**.
4. Complete the **Job Invoice Description** for job invoices and **Miscellaneous Invoice Description** for miscellaneous invoices.
   Enter any text and placeholders you want to include on invoices into the appropriate field. If you leave these fields blank, the description on the invoice is pulled through instead.
5. Click **Save**.

Export an edited invoice to Xero

Practice Manager doesn't automatically re-export edited invoices. If you export an invoice to Xero, then edit it in Practice Manager, you'll need to delete the invoice in Xero and export it again.

1. [Delete the previously exported invoice](Delete-or-void-a-sales-invoice.md) in Xero.
2. In Practice Manager, select **Business**, then select **Invoices**.
3. Find and open your edited invoice.
4. Hover over **Options**, then select **Export Invoice to Xero**.
5. Click **Yes**. The invoice is exported to Xero immediately.

Cancelled or deleted Practice Manager invoices in Xero

Xero handles cancelled and deleted invoices in Practice Manager in different ways depending on several factors.

### Cancelled invoices

When you cancel an invoice in Practice Manager, if the status of the invoice is:

- **Draft** or **Awaiting approval** – the invoice is deleted from Xero
- **Awaiting payment** (no payments or credits applied) – the invoice in Xero is voided
- **Awaiting payment** (payments or credits are applied) or **Paid** – the invoice in Xero isn’t changed but an error is displayed

Tip

To avoid getting an error when you cancel a partially or fully paid invoice, remove the payment or credit from the invoice in Practice Manager before cancelling it.

### Deleted invoices

When you delete an invoice in Practice Manager, the invoice in Xero isn’t changed. You’ll need to manually delete the invoice in Xero. This applies for all invoice statuses.

## What's next?

Set up Practice Manager to [import invoices you've created Xero](Import-invoices-from-Xero.md).