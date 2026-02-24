# Send and receive an e-invoice

Source: https://central.xero.com/s/article/Send-and-receive-invoices-with-e-invoicing

---

## Overview

- Send and receive an e-invoice and receive an electronic purchase order (ePO) as a draft invoice in Xero.

Tip

If you’re an existing GST-registered business, you can voluntarily [activate the GST InvoiceNow requirement](https://central.xero.com/s/article/Register-and-send-an-e-Invoice-SG).

How it works

e-invoicing in Xero enables businesses to connect to the Peppol network in order to send and receive e-invoices and electronic purchase orders (ePOs).

Invoices are delivered in a standardised format, so even if your customers and suppliers don’t use Xero, they can still receive e-invoices sent by you from Xero.

If a business or government agency sends your organisation an electronic purchase order (ePO), it appears in Xero as a draft invoice.

If you’re registered for the GST InvoiceNow requirement, when you send an invoice to your customer over the InvoiceNow network, Invoici automatically sends the transaction data to Inland Revenue Authority of Singapore (IRAS) on your behalf.

Send an e-invoice to a customer

Tip

If you’ve activated the GST InvoiceNow requirement, [send the invoice to your customer and IRAS](Send-GST-InvoiceNow-submissions-to-IRAS.md).

Once you’ve [created an invoice](Invoice-a-customer.md) for your customer:

1. In the **Sales** menu, select **Invoices**.
2. Select the **Draft** or **Awaiting Approval** tab, then find and open the invoice you want to send.
3. Click **Approve & email**.
4. (Optional) If your customer has remaining credit, click **Apply credit** to allocate it to the invoice, or click **Skip for now** to use the credit another time.
5. In the **To** field, enter the email address as your customer's Peppol ID then @invoi.ci as the domain name. You need to replace the colon (:) in the ID with a hyphen (-).

   For example, if your customer’s Peppol ID is 123456789M, enter 123456789M@invoi.ci as the email address.

   To send the invoice to multiple email addresses, separate them with either a comma (,) or a semicolon (;).
6. Complete the other fields in the **Send invoice** window.
7. Click **Send**.

You can check that your e-invoice was sent successfully. It show as **Sent** in Xero, and a confirmation message and unique transmission id will display in the [history and notes](View-history-and-notes-for-individual-transactions-and-inventory-items.md).

For more information, watch our YouTube video on how to [send and receive e-invoices](https://www.youtube.com/watch?v=ZCdO7vJg-7k) (YouTube).

Send an e-invoice to a government agency

If the Singapore government is a customer of yours and you need to send them an e-invoice, there are additional requirements to be aware of.

To meet these requirements, refer to the table below when you create the invoice in Xero.

| Invoice field in Xero | Description |
| --- | --- |
| **Contact Name** | The customer’s contact name in Xero must include the Business Unit at the beginning, eg '12345 - Business Unit Name'. Find the business unit name in this [list of Ministries / Statutory Boards](https://www.vendors.gov.sg/UsefulReferences/MinStatuaryBoards.aspx) (Singapore Government Agency website). |
| **Primary Person** | Add the name of the liaison officer at your client agency as the [primary person](Contact-fields.md) of the contact. The name can’t contain more than 20 characters or any special characters. |
| **Invoice number** | The invoice number must be unique, include less than 30 characters, and not include spaces or special characters. |
| **Reference** | Enter the reference number/ID of the invoicing instruction. |
| **Issued date** | The date the invoice is issued. This date can’t be in the future or backdated more than seven days. |
| **Due date** | The date the invoice is due. The credit term is automatically calculated from your invoice's due date. For example, if your credit term is 30 days, set your due date to 30 days from the current date. |
| **Description** | Add an extra line item to your invoice in Xero. In this line item, leave all fields blank except the Description field. You need to enter the invoice description in this field. |

If you haven’t activated the GST InvoiceNow requirement, you need to use the email address T08GA0028A@invoi.ci to send the e-invoice to the government agency.

If you’ve activated the GST InvoiceNow requirement, enter the Unique Entity Number (UEN) ‘T08GA0028A’ into the **Business Registration Number** field of the customer contact, then [send the invoice to your customer and IRAS](Send-GST-InvoiceNow-submissions-to-IRAS.md).

For more information, see [E-invoice Submission to Singapore Government Agencies via InvoiceNow](https://www.vendors.gov.sg/doc/Guide-E-invoice_Submission_via_InvoiceNow.pdf?ver=1.1) (Vendors@Gov website) or contact the [Accountant-General Department helpdesk](https://app.helpdesk.agd.gov.sg/public_user/common/Helpdesk.aspx?c9osI0quCY6Ly9siZW8epKc2QbDMoJJw9LSQzrVc7kX+xOb+nc3OK4IelfsO5ZGd) (Accountant-General Department website).

Receive an e-invoice or ePO

### Receive an e-invoice

If your supplier is registered on the Peppol network, give them your Peppol ID so they can send invoices directly to your Xero organisation.

All Peppol IDs in Singapore start with 0195:SGUEN and the rest of your number is based on your UEN. For example, if your UEN is 12345678X, then your Peppol ID is 0195:SGUEN12345678X.

Your suppliers don’t need to use Xero to send you invoices with e-invoicing.

When you receive an e-invoice to your Peppol ID, it's automatically created as a draft bill in your Xero organisation. Add the account code and make any other changes, then [approve the bill](Add-and-approve-bills.md).

### Receive an ePO

When you receive an ePO to your Peppol ID, it's automatically created as a draft invoice in your Xero organisation. You need to log in to Xero to open the draft invoice, adjust any line items, then approve it. The invoice is then ready to send using e-invoicing.

## What's next?

If you’re registered for the GST InvoiceNow requirement, find out more about the data you need to [submit to IRAS](Send-GST-InvoiceNow-submissions-to-IRAS.md).