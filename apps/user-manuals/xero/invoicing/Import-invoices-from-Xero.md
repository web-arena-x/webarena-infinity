# Import invoices from Xero into Practice Manager

Source: https://central.xero.com/s/article/Import-invoices-from-Xero

---

## Overview

- Set up Practice Manager to import invoices you've created in Xero and assign them to jobs or clients.
- You can also import payments and credits so your work in progress is accurate.

## How it works

You need to [connect Practice Manager to Xero](Connect-Practice-Manager-to-Xero.md) before you can import invoices from Xero.

Practice Manager imports:

- Invoices created in Xero that day
- Previously imported invoices you've edited in Xero, including applying a credit note or payment, if you've deleted the invoice in Practice Manager
- Invoices imported into Xero from another accounting system, if they've been edited in Xero within the last 14 days

Practice Manager doesn't import:

- Invoices edited in Xero but not deleted in Practice Manager
- Invoices created before the [lock date in Xero](Set-up-and-work-with-lock-dates.md), even if the invoice was edited after the lock date
- Information in the description field on the invoice in Xero
- The status of the Xero invoice

Invoices are imported overnight and are assigned an interim status. Since the status of the Xero invoice isn’t imported, you’ll need to either:

- Manually set the invoice status in Practice Manager
- Use Xero as the source of truth for invoice statuses

Practice Manager doesn’t overwrite existing invoices. If you edit an invoice in Xero, you must delete the invoice in Practice Manager before the updated invoice can be imported.

You can use the reference field on the invoice to assign the invoice to a job. If Practice Manager can’t find a matching job, you can have it create an ad hoc job to assign the invoice to. Otherwise, Practice Manager assigns the invoice to the client.

Warning

If Practice Manager assigns the invoice to a client, you can’t reassign it to a job or a different client.

Invoices assigned to a job reduce work in progress by the value of the invoice. Invoices assigned to the client have no effect on work in progress.

## Set up Practice Manager to import invoices and payments

1. In the **Business** menu, select **Settings**.
2. Under **Connections**, click **Xero**.
3. (Optional) Under **Invoices**, select the checkbox next to **Invoice Payments** to automatically import invoice payments and credits from Xero.
4. Under **KPI/WIP reporting** select **Automatically import invoices from Xero**.
5. (Optional) Select the checkbox to have Practice Manager create an ad hoc job and assign the invoice to it when it can’t find a matching job, then select:
   - **For all invoices** – to assign the invoice to a job even if the reference is blank
   - **Excluding invoices with no reference (will be allocated to the client)** – to assign the invoice to the client if the reference is blank
6. Under **Invoice Summary**, enter the wording you want to appear in the **Description** field of all invoices imported invoices.
7. Click **Save**.
8. (Optional) To import payments from Xero immediately, click **Import Payments** on the left hand side of the screen.

Tip

Practice Manager doesn't recognise imported job numbers, so you’ll need to [update the number sequence](Import-data-into-Practice-Manager.md) when you’re doing an import. If you don't, you might receive a [job number allocation error](Troubleshoot-importing-and-exporting-invoices.md).

## What's next?

If you're having trouble importing invoices, see [fix issues with importing and exporting invoices](Troubleshoot-importing-and-exporting-invoices.md).