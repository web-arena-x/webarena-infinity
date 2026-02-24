# About data extraction in Hubdoc

Source: https://central.xero.com/s/article/About-data-extraction-in-Hubdoc

---

## Overview

- The data extraction process that new documents in Hubdoc go through.

The extraction process

### How it works

Every document imported into Hubdoc goes through a data extraction process, unless the organisation is in a non-paying state or data extraction is disabled. The extraction process usually happens within seconds, but can sometimes take up to 24 hours, depending on the document.

You can import different file types into Hubdoc, but data only gets extracted from DOC, PDF, GIF, JPG, PNG, HTML, TXT, HEIC and HEIF files.

New documents waiting to have data extracted show on the **Processing** tab. Once extraction is complete, documents move to the **Review** tab. If Hubdoc can’t extract any data, documents move to the **Failed** tab.

To successfully complete data extraction, a document must include a date, supplier name, and total amount. These details are extracted and stored in the organisation, along with the document image. Hubdoc also extracts any invoice number or due date showing on the document.

The extracted data shows in the data toolbar, to the right of the document. Hubdoc creates a folder based on the supplier's name to store the document, or adds it to an existing folder for that supplier.

Hubdoc doesn't automatically extract line item data from a document. You need to enter this information manually or save the line items in any configured supplier rules you have set up.

When publishing documents with multiple line items, click **Add last items** to pull in the last items published for the selected supplier.

You can [turn data extraction off and on](Turn-off-data-extraction-in-Hubdoc.md) to suit your needs.

### Potential duplicate documents

When you email or manually upload a document, Hubdoc checks to see if it's a duplicate with an existing document.

Hubdoc identifies a new document as a potential duplicate if it has the same date, supplier name, and total amount as one or more existing documents.

Any invoice numbers on documents are also checked. Two documents must have the same invoice numbers to show as potential duplicates.

Hubdoc identifies a potential duplicate by an icon in the data toolbar. Click **Show Duplicates** to open a panel showing the document alongside all other potential duplicate documents. Choose to mark a document as **Not a duplicate**, or click **Move to Trash** to delete it.

You can [turn off duplicate detection for a particular supplier](Customise-account-connections.md) if you regularly get duplicate documents from the same supplier and want to keep them.

If you've set up [automatic publishing to Xero](Publish-Hubdoc-documents-to-Xero.md) for a particular supplier, any potential duplicate documents from that supplier aren't automatically published.

### Dates

Hubdoc identifies an organisation’s region based on the currency selected when the organisation is set up. You can enter a date in any format, but the region determines how Hubdoc extracts and displays the date.

- For organisations in the US and Canada, the date format is assumed to be MM/DD/YYYY.
- For organisations in the UK, AU, NZ, and the rest of the world the date format is assumed to be DD/MM/YYYY.

On some documents, the date can be ambiguous if the correct date format isn’t identified. If the date format based on the organisation’s currency results in a future date, we’ll automatically use the other format. If you need to change the currency selected for your organisation, you can do this in the [organisation settings](Update-Hubdoc-organisation-settings.md).

### Currencies

Hubdoc automatically recognises a wide range of currencies in your documents. If we can't determine the currency of the original document, we'll use the base currency of the organisation. You can change the currency extracted from a document in the edit data toolbar.

Sometimes Hubdoc misreads amounts where figures are separated by commas. To fix this, change the amount in the edit data toolbar.

If you’re publishing multicurrency documents to Xero, make sure the currency is set up in Xero first, then select the currency on the document.

Tax extraction

If your organisation is connected to Xero and you’ve enabled tax data to be published, you can [turn on auto-tax extraction](Turn-off-data-extraction-in-Hubdoc.md). When this is enabled, Hubdoc extracts the GST amount in addition to the supplier name, date, and total amount. If the GST amount can’t be found on the document, we use the tax rate selected for the supplier or the default tax rate for the organisation.

However, selecting a single tax rate from the tax rate field doesn’t always result in the correct tax amount for the document.

- Sometimes, the tax on a document doesn’t reflect a flat application of a single tax rate on the total. For example, restaurant meals where the subtotal is taxed but the tip isn’t, or grocery bills where some food items are taxed and others aren’t.
- The amount that Hubdoc extracts is rounded to two decimal places, so depending on how the numbers were rounded on the document, the tax calculation might be off by a cent or two.

To manually change this, you can use an automatic calculator tool to [change the tax amount calculated](Manually-enter-data-for-a-document.md). You can’t use the automatic calculator if you’re only publishing a single line item. To publish a single line item, you need to change the tax rate to a specific rate.

Document fields and types

### Document fields

When a new document appears in your organisation, Hubdoc extracts the **Date**, **Total Amount** and **Supplier**, and if available the **Due Date** and **Invoice / Ref #**. If other fields are required for the document, you need to enter these manually. All mandatory fields must be completed before the document can be published to Xero.

| Field | Description |
| --- | --- |
| Mark as Paid | For your reference, you can select the checkbox to show an invoice or bill as paid. Marking a document as paid doesn't affect how it's published to Xero, or its status in Xero. |
| Document Type | The type of document. View the table below to understand each type. |
| Supplier | Who the document is from. This is a mandatory field. |
| Invoice / Ref # | The invoice or reference number for the document. If this field is blank when you publish the document to Xero, Hubdoc automatically enters **HD - Document ID#** as the default reference. |
| Date | The date of the document. This is a mandatory field. |
| Due Date | The date the document is due to be paid. If you don’t enter a due date before publishing the document to Xero, the transaction date is used as the due date on the transaction in Xero. |
| Total Amount | The total amount and currency of the document. These fields are mandatory. By default, the currency is what's selected in your organisation settings, but you can change it at a document level. If Hubdoc misreads an amount that uses a comma, change the amount in the edit data toolbar. |
| Tax Rate | This field only shows if you’ve enabled tax data to be published. Select the tax rate that applies to the document, or select **Extracted Amount** to use the automatic calculator to adjust the tax amount. If you select a specific **Tax Rate**, Hubdoc calculates the tax amount based on the **Total Amount** entered for the document. If you select **Extracted Amount** as the **Tax Rate**, use the automatic calculator to enter the tax amount. |
| Subtotal | This field only shows if you’ve enabled tax data to be published and you’ve selected a specific tax rate. You can't manually enter the subtotal, Hubdoc automatically calculates it based on the tax rate selected. |

### Document types

Understand what each document type represents.

| Document type | Description |
| --- | --- |
| **Invoice** | A bill you've received from your supplier that you need to pay |
| **Invoice (AR)** | An invoice you've sent to your customer (accounts receivable) |
| **Statement** | Summary of your account with a supplier, or the transactions in your bank account for a certain period |
| **Report** | Any type of business report, such as a builders report, accounting reports or compliance reports |
| **Receipt** | A document acknowledging a payment you've made |
| **CSV** | A file saved as a comma separated values file type, often a spreadsheet used to export transactions from a bank account |
| **Check** | Official bank document directing a bank to pay money out of your bank account to a payee |
| **Deposit** | A document that shows money deposited into an account |
| **eTransfer** | Online money transfer receipt |
| **Payment** | Proof of a payment you've received |
| **Credit Memo** | A document to show money is owed (money refund document), either for accounts receivable or accounts payable |
| **Purchase Order** | A document created by a buyer to order products from suppliers |
| **Other** | Any document that doesn’t fit the above criteria |

Why data won't be extracted

A document can fail the extraction process for a few reasons. The most common are:

- The document is written in a foreign language. Data extraction only recognises documents in English.
- The image is too blurry, crumpled or faded and the information on the document can’t be recognised.
- A piece of mandatory information such as the date, amount or supplier's name is missing from the image.
- There’s more than one document in the same image. Each document has to be uploaded individually into Hubdoc.
- A user starts to manually enter data on the document before the extraction process has finished. You need to wait until the process has finished before manually entering data.

## What's next?

Identify the best way to [get documents into your organisation](About-getting-documents-into-Hubdoc.md) or [resolve issues with data extraction](Resolve-issues-with-documents-in-Hubdoc.md).