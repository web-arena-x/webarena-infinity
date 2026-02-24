# Send GST InvoiceNow submissions to IRAS

Source: https://central.xero.com/s/article/Send-GST-InvoiceNow-submissions-to-IRAS

---

## Overview

- Submit invoice transaction data to the Inland Revenue Authority of Singapore (IRAS) to comply with the GST InvoiceNow requirement.

Tip

If you haven’t activated the GST InvoiceNow requirement, send each e-invoice to your customer [via the Peppol network](Send-and-receive-invoices-with-e-invoicing.md).

How it works

Once you’ve registered for the GST InvoiceNow requirement, Invoici automatically sends transaction data to the Inland Revenue Authority of Singapore (IRAS) for all the transactions you send over the InvoiceNow network.

If you don’t send a transaction via the InvoiceNow network, you need to send the data to IRAS manually.

How you send the data to IRAS depends on the type of submission:

| **IRAS data flow** | **Type of submission** | **Process** |
| --- | --- | --- |
| 1A | Invoice is sent via Peppol | Send the invoice to peppol@invoi.ci when you send the invoice to your customer. |
| 1B | Bill is received via Peppol | Xero automatically submits the bill when you approve it. The exception is bills with the **No Tax** tax code – Xero doesn’t submit these. |
| 2A | Invoice isn’t sent via Peppol (sent manually) | Send the invoice to IRAS@invoi.ci when you send the invoice to your customer. |
| 2B | Transaction is a point of sale (POS) or a simple tax invoice (STI) | Create a cash invoice and send it to IRAS@invoi.ci. |
| 3A | Bill is received manually (not via Peppol) | Xero automatically submits a bill when you approve it, unless it has the **No Tax** tax code – Xero doesn’t submit these. |
| 3B | Petty cash purchases (PCP) | Create a cash bill. If the assigned contact has **PCP** in the **Business Registration Number** field, Xero automatically submits the bill to IRAS when the bill is approved. |

For more information about the types of submissions and process to submit transaction data, see the [IRAS e-Tax Guide](https://brandfolder.xero.com/W2K0UFY7/at/94f76gm39s7qjjqv3qg6w7/IRAS_e-Tax_Guide.pdf) (PDF file, 1 MB).

Send an e-invoice to a customer and IRAS (data flow 1A)

Before you start, make sure the customer’s contact record in Xero shows their:

- Unique Entity Number (UEN) in the **Business registration number** field
- (Optional) GST number in the **Tax Identification Number** field

To send the invoice:

1. In the **Sales** menu, select **Invoices**.
2. Select the **Draft** or **Awaiting Approval** tab, then find and open the invoice you want to send.
3. Click **Approve & email**.
4. In the **To** field, add the email address peppol@invoi.ci, separated by a comma (,).
5. Click **Send email**.

Once the invoice is successfully delivered to the customer, Invoici automatically sends the invoice data to IRAS.

Send an invoice as a GST InvoiceNow submission (data flow 2A)

Before you start, make sure the customer’s contact record in Xero shows their:

- Unique Entity Number (UEN) in the **Business registration number** field. If the customer is an individual, you don’t need to enter their National ID card (NRIC) or name, just enter ‘NA’.
- (Optional) GST number in the **Tax Identification Number** field

If you’re registered for the GST InvoiceNow requirement, any invoices that aren’t sent as an e-invoice via InvoiceNow need to be sent to IRAS as a GST InvoiceNow submission:

1. In the **Sales** menu, select **Invoices**.
2. Select the **Draft** or **Awaiting Approval** tab, then find and open the invoice you want to send.
3. Check that the invoice details are correct. Once the e-invoice is successfully sent and received you won’t be able to make changes to it.
4. Click **Approve & email**.
5. In the **To** field, add the email address IRAS@invoi.ci, separated by a comma (,).
6. Click **Send email** to confirm that you want to send the invoice to IRAS as a GST InvoiceNow submission.

It might take a few seconds to transmit the information to IRAS.

Submit a bill to IRAS (data flow 1B and 3B)

Before you start, make sure the customer’s contact record in Xero shows their:

- Unique Entity Number (UEN) in the **Business registration number** field
- GST number in the **Tax Identification Number** field

If you’re registered for the GST InvoiceNow requirement, all approved bills must be transmitted to IRAS via the InvoiceNow network.

Once you’ve registered for the requirement, when you approve a bill, Xero automatically submits the data to IRAS on your behalf. Xero doesn’t submit any data for bills that have the tax code **No Tax**.

To send and submit a bill:

1. [Create the bill](Add-and-approve-bills.md) in Xero.
2. Click **Approve**.

Xero automatically submits the bill to IRAS.

If you’ve edited the bill and need to resend it:

1. Log in to [Invoici](http://sg.invoici.net) (Invoici website) with your Xero login details.
2. Select the **eInvoices** tab.
3. Search for and find the bill, then click **Resubmit**.

Submit cash transactions to IRAS (data flow 2B and 3B)

### How it works

To report cash transactions to IRAS as a GST InvoiceNow submission, you need to create:

- An invoice for a cash sale
- A bill for a petty cash purchase

For each contact you create an invoice or bill for, you need to enter a 3-digit code as the **Business Registration Number (BRN)** in their contact record. For:

- Cash sales – enter **POS** (Point of Sale)
- Cash sales via simplified tax invoice – enter **STI** (Simplified Tax Invoice)
- Cash purchases – enter **PCP** (Petty cash purchases)

### Create a cash invoice (data flow 2B)

1. [Create the invoice](Invoice-a-customer.md) in Xero.
2. Assign it to a contact that has **POS** or **STI** in the **Business Registration Number** field.
3. Click **Approve & email**.
4. In the **To** field, enter IRAS@invoi.ci as the email address.
5. Click **Send email**.

### Create a cash bill (data flow 3B)

1. [Create the bill](Add-and-approve-bills.md) in Xero.
2. Assign it to a contact that has **PCP** in the **Business Registration Number** field.
3. Click **Approve**.

Xero automatically submits the bill to IRAS.

Submit a credit note via InvoiceNow

In Xero, [credit notes](Credit-notes.md) can be applied to invoices and bills. The process to send a credit note to IRAS is the same as when you send an invoice or bill, depending on the specific situation. Follow the relevant steps above for each credit note you need to submit.

## What's next?

Reconcile the GST InvoiceNow submissions [sent to IRAS](Reconcile-GST-InvoiceNow-submissions.md).