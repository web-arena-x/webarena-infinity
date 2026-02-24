# Record a payment on a Practice Manager invoice

Source: https://central.xero.com/s/article/Record-a-payment-on-an-invoice

---

## Overview

- When you receive payment from your client, mark the invoice as paid.
- Record an invoice as partially or fully paid.

About invoice payments

- Record as many partial payments as you need to, or record a payment as received in full.
- Invoices are archived when they’re paid in full. To view archived invoices in the Invoice Manager, click **All Invoices** and select **Archived Invoices**.
- If a payment is incorrect, select the **Payment** tab of the invoice and click the **X** icon next to the payment to remove it.
- If you've set up Practice Manager to [import invoices from Xero](Import-invoices-from-Xero.md), you can also choose to import payments applied to invoices in Xero.

Record payment received in full

Record a payment as received in full to archive the invoice.

1. In the **Business** menu, select **Invoices**.
2. Select either the **Awaiting Payment** or **Overdue** tab.
3. Select the checkbox for each invoice you want to mark as paid.
4. Click **Mark as Paid**.

Record part payment received

You can record as many partial payments as necessary to complete the payment. Alternatively, if you decide not to pursue the balance of an invoice, you can [write it off](Cancel-or-delete-an-invoice.md#Writeoffaninvoice).

1. In the **Business** menu, select **Invoices**.
2. Select either the **Awaiting Payment** or **Overdue** tab.
3. Click anywhere on the line of the invoice you want to record payment for.
4. Select the **Payments** tab.
5. Enter the details of the part payment:
   - **Date Paid** – Enter the date you received the payment.
   - **Amount Paid** – Update the default amount due on the invoice with the actual amount paid.
   - **Ref/Cheque Number** – (Optional) Enter your practice's reference for the payment.
6. Click **Add Payment**.

Import invoice payments

### Prepare the import file

[Prepare an import file](Import-data-into-Practice-Manager.md) using the details listed below.

| | |
| --- | --- |
| Example file | [Payments Import Example](https://xero.my.salesforce.com/sfc/p/o0000000biwC/a/1N000000nQwj/2UOQkqKX4PGVivwPB6k3GqF.AqZGV3sG.uR.oy05Kzo) (CSV, 199 bytes) |
| Required fields | Invoice No, Date, Amount and Reference |
| Notes | Values for the **Date** field must use DD/MM/YYYY format. The invoice that you are importing payments against must exist. |

### Import the data

1. In the **Business** menu, select **Settings**.
2. Under **Connections**, click **Import**.
3. For **File Type**, select **Generic - Payment**.
4. Select the format of your import file.
5. Click **Next**.
6. Click **Choose file** and select your import file.
7. Click **Import**.

The number of rows imported and any errors are displayed at the bottom of the screen. You might also want to spot check the details of a few invoice payments to verify the import.

## What's next?

You’ve now recorded your payment – you’re all done!