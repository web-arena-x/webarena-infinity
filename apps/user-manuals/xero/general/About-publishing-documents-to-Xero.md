# About publishing documents to Xero

Source: https://central.xero.com/s/article/About-publishing-documents-to-Xero

---

## Overview

- Create a new transaction in Xero when you publish a document from Hubdoc, or republish a document to update the transaction in Xero.

How it works

### Publishing a document

You need one of the following Hubdoc user roles to publish documents from Hubdoc to Xero, regardless of your user role in the connected Xero organisation:

- Upload Only + Publish Documents
- Standard + Publish Documents
- Accountant/Bookkeeper

Once a document is uploaded to Hubdoc and the data has been extracted, configure the data for the document, then publish it to Xero.

When you publish a document, Hubdoc creates a transaction in Xero. The transaction will have a draft, awaiting approval or awaiting payment status, depending on the configuration settings. If the document is under 3MB, Xero attaches a copy of the document to the transaction. If the document is larger than 3MB, it shows as a link rather than an attachment.

Warning

[Setting a lock date in Xero](Set-up-and-work-with-lock-dates.md) doesn't prevent users from publishing documents from Hubdoc with an awaiting approval or awaiting payment status. However, it will restrict who can approve the transaction in Xero.

When configuring data for a document:

- Data for fields such as the contact, billable expenses, tracking categories and untracked inventory items are imported from your Xero organisation. You can only integrate purchased inventory items. For documents with tracked inventory items, publish the document and add the items to the transaction in Xero.
- Use multiple line items to code transactions to different account codes, separate the taxable and non-taxable portions, or include inventory items. You can also enter different descriptions for each line item. Click **Add last items** to populate all the line item details that were last published for the selected supplier.
- Hubdoc rounds to two decimal places. If the document shows several decimal places, [manually change the tax amount](Manually-enter-data-for-a-document.md) on the document in Hubdoc to two decimal places, then edit the transaction in Xero to show the correct amount.
- Hubdoc will identify any document that appears to be a credit note and flag it for review. If Hubdoc detects a credit note, you need to review the document before publishing it to Xero.

You can also [enable autosync for a supplier](Publish-Hubdoc-documents-to-Xero.md) so Hubdoc automatically configures and publishes all documents from a supplier.

Hubdoc currently doesn’t integrate with Xero Projects or Xero Expenses.

### Re-publishing a document

Once a document has been published, the **Re-publish** button shows.

If you re-publish a document, it updates the transaction initially published in Xero with the new information. It doesn’t create a new transaction.

You can’t re-publish a document if:

- It’s a purchase document that was initially published with a status of approved
- The initial transaction created in Xero is deleted, voided, edited, reconciled, or paid

When you re-publish a document to Xero, you can’t change the type of transaction the document was published as (**Publish As** field) or the **Status** field.

Types of documents you can publish to Xero

The types of documents you can publish from Hubdoc to Xero depends on whether your Xero organisation is on a business or partner edition pricing plan. If your Hubdoc organisation is connected to a:

- Xero business edition subscription, you can publish documents as **Purchase**, **Spend Money**, **Invoice (AR)** or **Credit Note** transactions.
- Xero partner edition subscription, you can only publish documents as **Spend Money** transactions.

Each document type allows you to configure different details before you publish.

### Purchase

Documents published as **Purchase** create a bill in Xero. Select this document type for bills that you have to pay by a certain date.

Select **Draft** to create a draft bill, **Awaiting Approval** for bills that need to be approved, or **Awaiting Payment** to create an approved bill that’s ready to be paid. Once published to Xero, you can find these transactions in the Bills screen within the relevant status tab, **Draft**, **Awaiting Approval**, or **Awaiting Payment**.

To match a bill in Hubdoc to an existing purchase order in Xero, you need to [send the document to Xero Files](Send-documents-directly-to-Xero-Files.md), then attach the file and [create a bill from the purchase order](Creating-bills-from-purchase-orders.md).

### Spend Money

Select **Spend Money** if you pay for a purchase straight away. In Xero, this creates a spend money transaction in the bank account used for the purchase.

### Invoice (AR)

If you manually create your invoices outside of Xero, publish documents from Hubdoc as an **Invoice (AR)** to create a draft sales invoice in Xero. You can’t publish a document to Xero as an authorised invoice. Once published to Xero, find the invoice in the **Draft** tab within **Invoices**, then approve it before sending to your customer.

### Credit Note

Add a credit note that isn’t linked to an invoice or bill by publishing a document as a **Credit Note**. You can publish credit notes as either accounts payable **(A/P credit)** or accounts receivable **(A/R credit)**.

Select **Draft** to create a draft credit note, **Awaiting Approval** for credit notes that need to be approved, or **Awaiting Payment** to create an approved credit note. Once the credit note is created in Xero, find it in the **Draft**, **Awaiting Approval**, or **Awaiting Payment** tabs in the **Invoices** or **Bills** screen. You can then allocate it to an invoice or bill at a later date, or refund to the customer.

Multicurrency in Hubdoc

To import transactions in multiple currencies from Hubdoc to Xero, you need to have a Xero pricing plan that includes multicurrency. If you’re publishing multicurrency documents to Xero, make sure the currencies used by the documents are set up in Xero first. Hubdoc supports all currencies that are available in Xero.

Foreign currency amounts extracted in Hubdoc publish to Xero as the same amount, but in your base currency. For example, an extracted amount of USD250.00 as the foreign currency in Hubdoc imports as EUR250.00 in Xero if your base currency is set as Euros. You can then apply the correct currency to the transaction in Xero.

If the currency extracted in Hubdoc isn’t available in Xero, the imported amount is still the same, but it shows in your base currency. You need to [edit the transaction](Edit-a-spend-or-receive-money-transaction.md) in Xero to manually convert the amount to its value in your base currency.

Document fields explained

Configure the following data before publishing a document to Xero. The fields that display depend on the **Publish As** option selected. All required fields must be completed for the document to publish successfully.

| Field | Description |
| --- | --- |
| Status | Required field for **Purchase** and **Credit Note** documents. Select **Draft** to publish the document as a draft transaction, **Awaiting Approval** for a transaction that needs to be approved, or **Awaiting Payment** to create a transaction that’s ready to be paid. |
| Contact | Required field for all documents. Hubdoc imports your [contact list from Xero](Contacts-in-Xero.md). If you don’t have a saved publishing configuration, Hubdoc matches the supplier from the document with one from your Xero contacts list. If there are no matches, select or begin typing the name of the Xero contact for the document. If the contact isn't created in Xero, click **Add [x] as a new contact**, enter the name, then click **Create** to confirm. The new contact is created in Hubdoc and Xero. |
| Account Code | Required field for all documents. Hubdoc imports your chart of accounts when you connect to Xero. Select or begin typing the appropriate account code from the list. |
| Customer | Optional field for **Purchase** and **Spend Money** documents. Select a contact if you want to [pass the cost of the expense onto your customer](Add-billable-expenses-to-bills.md). The list of contacts represents those in the **All** tab in Xero. A contact not already a customer in Xero will become a customer when the document is published. |
| Description | Optional field for all documents. Use this field to record additional information about this document. Data entered here is imported into the **Description** field in the transaction in Xero. If you publish a document with multiple lines, enter different descriptions for each line. If you select the **Save configuration** checkbox, the description isn’t saved as part of the configuration settings. The **Description** field is blank by default for all new documents. |
| Bank Account | Required field for **Spend Money** documents. Hubdoc imports your account list from Xero. Select or begin typing the name of the bank account that was used to pay for the purchase. If the bank account you're looking for isn't on this list, confirm that it’s [set up in Xero](Add-a-bank-account-or-credit-card-account.md). |
| Credit Note Type | Required field for **Credit Note** documents. Select **A/P Credit** or **A/R Credit**. A/P Credit documents are created as purchase (accounts payable) credit notes in Xero and A/R Credit documents are created as sales (accounts receivable) credit notes in Xero. Xero only displays the **Reference** if there’s a matching invoice with the same reference for that supplier. |

## What's next?

[Publish a document to Xero](Publish-Hubdoc-documents-to-Xero.md).