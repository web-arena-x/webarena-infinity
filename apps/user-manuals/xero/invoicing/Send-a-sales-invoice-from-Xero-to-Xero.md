# Send a sales invoice via Xero to Xero

Source: https://central.xero.com/s/article/Send-a-sales-invoice-from-Xero-to-Xero

---

## Overview

- Send a sales invoice directly to another Xero organisation using the Xero to Xero network to create a draft bill in their organisation.

## What you need to know

### How it works

- You need to add [a customer's Xero network key](Enter-a-Xero-network-key-received-from-another-Xero-organisation.md) to their contact details before you can use Xero to Xero. You can send an invoice using the Xero Network if you have the contact's Xero network key entered, but no other relevant business numbers.
- You can only send invoices that don't have any transactions, such as payments or tax adjustments, recorded against them. If transactions are recorded on the invoice, you need to email the invoice instead.
- The bill in the receiving organisation shows the legal or trading name of the source organisation, not their display name.
- When a source organisation sends an invoice with an account code or tax rate, the receiving organisation's draft bill doesn’t display these. Xero doesn't assume that the tax rates or chart of accounts set up in the receiving organisation are the same as in the source organisation.
- You need the advisor, standard, invoice only (approve & pay) or invoice only (sales) user role to send an invoice via Xero to Xero.

### Foreign currency invoices

If you have a pricing plan [with multicurrency](About-multicurrency.md), you can send an invoice in a foreign currency using Xero to Xero. How it’s received in the other organisation depends on how you send the invoice, whether they use multicurrency and if they have the currency set up in their organisation.

- If both organisations use multicurrency and the recipient has added the currency to their organisation, they receive the invoice in the same currency for the same amount. When they approve the bill in their organisation, the foreign currency gain/loss is calculated using the exchange rate they use in their organisation.
- If you send an invoice using **Send via Xero Network** within an invoice, the receiving organisation needs to have multicurrency, with the same currency as the invoice enabled. If they don’t, you’ll receive an error when attempting to send the invoice.
- When using the Xero Network from the invoice list view:

 - If both organisations use multicurrency but the receiving organisation hasn't added the currency, Xero automatically adds the currency to their organisation.
 - If the receiving organisation doesn't use multicurrency, they receive it in their base currency. They need to manually calculate the foreign currency amount so the correct payment is made.

## Send an invoice via the Xero Network

1. [Create an invoice](Invoice-a-customer.md).
2. Enable **Send via Xero Network** at the bottom of the invoice. You'll need to add a contact to the invoice before you'll see the **Send via Xero Network** switch.
3. Enter the invoice details. Any reference without a prefix will be sent as a buyer reference (eg add 456 to send a buyer reference of 456). You can send multiple reference types and separate them with a comma (eg add PO:123, TN:765).
4. (Optional) To attach a PDF, CSV, JPG or PNG file, click **Attach files**.
5. Click **Approve & send**, or select the arrow next to this to choose another approval option.
6. (Optional) Clear the Include a PDF copy of this invoice checkbox if you don’t want one for this invoice.
7. Click **Send**.

## Send a Xero to Xero invoice from the invoice list view

Warning

Only resend a Xero to Xero invoice if your contact deletes it from their Xero organisation and they ask for another one.

If you’re in a region where eInvoicing is available, you’ll see the option to **Send as an eInvoice** in the invoice details. You’ll see **Send via the Xero Network** if you’ve only entered the customer’s Xero network key, with no other relevant business numbers.

To send an invoice using the Xero Network when eInvoicing is enabled, you need to do this from the invoice list view:

1. In the **Sales** menu, select **Invoices**.
2. Select the **Awaiting Payment** tab.
3. Select the checkbox next to each invoice you want to send.
4. Click **Email**.
5. (Optional) Update the information in the Send Invoice window. If you enter or change the email address, Xero saves it to the contact details.
6. Choose to email your customer an online link, PDF or both. Files you've attached to the invoice can't be sent from Xero to Xero.
7. Make sure the Xero Network checkbox is selected for each invoice, then click **Send**.

## What's next?

If you'd like to receive your bills into your organisation via Xero to Xero and your supplier also uses Xero, [send your Xero network key](Send-your-Xero-network-key-to-another-Xero-organisation.md) and ask your supplier to set you up.