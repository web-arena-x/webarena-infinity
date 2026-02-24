# Send an eInvoice

Source: https://central.xero.com/s/article/Send-an-e-invoice

---

## Overview

- Send an approved invoice electronically to a registered customer through the Peppol network.
- eInvoices are sent directly between accounting systems by a secure network instead of as a PDF or email.

## How it works

An eInvoice is sent directly to the accounts payable software of your customer through a secure eInvoicing network. Xero uses Peppol for its eInvoicing network because it's the framework that the New Zealand and Australian governments adopted for standardised eInvoicing.

Your customer needs to [register with Peppol](Register-to-receive-e-invoices.md) to receive eInvoices. When you send an eInvoice, their registration is validated. If they're not registered, you'll be notified that the eInvoice can't be sent and you can send the invoice as a PDF or by email instead. You don't need to be registered with Peppol to send an eInvoice.

You can send eInvoices even if your customer is using a different software system. The eInvoice is delivered directly into your customer’s accounting system, where it can be approved without the need for manual entry.

You can’t send eInvoices to a business or government agency in another country.

## Before you start

- Make sure you've added your business's ABN, branch number (if applicable) and registered business name in your [organisation's settings](Update-your-organisation-s-settings.md).
- [Find your customer’s ABN](https://abr.business.gov.au/) (ABN Lookup website) and [add it to their contact details](Edit-a-contact.md) in Xero, so they can receive the eInvoice. Their ABN is entered in the **Tax** field under **Financial Details**.
- Confirm that your customer is registered to receive eInvoices through their accounting software. You can use the [Peppol directory](https://directory.peppol.eu/public) to see if your customer is registered.

## Send an eInvoice

You’ll need the advisor, standard, invoice only - approve and pay, or invoice only - sales only user role to approve and send eInvoices. Users with an invoice only - draft user role will need to submit the invoice for approval before it can be sent.

1. [Create an invoice](Invoice-a-customer.md).
2. Select **Send as an eInvoice**. You'll need to add a contact to the invoice before you'll see the **Send as an eInvoice** toggle.
3. Enter the invoice details.
4. (Optional) If your customer is a government agency or large enterprise, they might have asked you to include additional information in the **Reference** field. Use a prefix of:
   - PO: for purchase order (eg add PO:123 to send a purchase order reference of 123).
   - CN: for contract number.
   - PN: for project number.
   - TN: for tender number.

   Any reference without a prefix will be sent as a buyer reference (eg add 456 to send a buyer reference of 456). You can send multiple reference types and separate them with a comma (eg add PO:123, TN:765).
5. (Optional) To attach a PDF, CSV, JPG or PNG file, click **Attach files**, then **Upload files**. Select **Include with online Invoice** under the name of the file. The total size of all attachments should be less than 10 MB.
6. Double check that the invoice details are correct, as once an eInvoice is successfully sent and received you won’t be able to make changes and resend it.
7. Click **Approve & send**.
8. (Optional) Clear **Include a PDF copy** if you don’t want one for this invoice.
9. (Optional) Select **Include payment information**, then choose the saved bank account details you'd like to add to the eInvoice.
10. (Optional) Select **Attach files to eInvoice** to include the attachments.
11. Click **Send** again to confirm that you want to send the invoice as an eInvoice. It might take a few seconds to validate the information. If you haven't entered any required information for the eInvoice you'll be prompted to add it to your eInvoice before you can send it again.

If your recipient hasn't registered to receive eInvoices, you'll be notified that the eInvoice can't be sent. Instead, [send the invoice as a PDF or email](Approve-and-send-a-customer-invoice.md).

The eInvoice is confirmed as sent in the history and notes section. It also displays in the contact's **Activity** tab. This might take a few minutes to update.

## What's next?

[Set up invoice reminders](How-invoice-reminders-work.md) to automatically follow up any overdue amounts on a regular basis.