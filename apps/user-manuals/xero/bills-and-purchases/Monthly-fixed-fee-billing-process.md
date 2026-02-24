# Invoice a client for a fixed amount on a regular basis

Source: https://central.xero.com/s/article/Monthly-fixed-fee-billing-process

---

## Overview

- Regularly invoice a client against the same job for a fixed amount, such as a monthly service fee or a maintenance contract.
- Import the recurring invoices from Xero into Practice Manager.

## Before you start

- If you haven’t already, [connect Practice Manager to Xero](Connect-Practice-Manager-to-Xero.md) and set up Practice Manager to [import invoices from Xero](Import-invoices-from-Xero.md) automatically.
- Make sure Practice Manager doesn’t create an ad hoc job if it can’t find a job that matches the reference field on the Xero invoice.
- Decide if you want the time recorded against the job you create to be included in your [work in progress (WIP)](Work-in-progress.md). If you set up the job to be excluded from estimated billings, any time recorded against the job won’t accumulate as WIP. Otherwise, you’ll need to [write off WIP](Remove-or-exclude-a-job-from-the-WIP-list.md) from the job or [create a final invoice](Create-a-final-invoice.md) and mark the time as invoiced or written off.

## Set up the job and repeating invoice

1. [Create a job in Practice Manager](Create-or-edit-a-job.md) and take note of the job number or client order number.
2. [Set up a repeating invoice in Xero](Add-or-edit-a-repeating-invoice-template.md) using the job number or client order number from the job in Practice Manager as the reference for the invoice template.

Each time Xero generates an invoice, Practice Manager will import the invoice overnight and assign it to the job.

Tip

When you set up the connection to Xero, clear the checkbox for creating an ad hoc job. Clearing the checkbox ensures that the repeating invoices are recorded against the correct job for KPI and reporting purposes.

## What's next?

If you perform regular jobs for clients, you can [set up recurring jobs](Recurring-jobs.md) in Practice Manager.