# Fix Xero publishing errors in Hubdoc

Source: https://central.xero.com/s/article/Fix-Xero-publishing-errors-in-Hubdoc

---

## Overview

- Resolve error messages received in Hubdoc when publishing documents to Xero.

An error occurred: Please try again

If you receive this error message, check that:

- A document with the same invoice number isn’t already published to Xero
- There’s no [lock date set](Set-up-and-work-with-lock-dates.md) for the period of the invoice date

Invoice # is already published to Xero

The error message **A document with the same Invoice # is already published to Xero** shows when you:

- Select **Invoice (AR)**in the **Publish As** field
- Try to publish a document which has the same invoice number as one already in Xero

Check the invoice in Xero and the invoice in Hubdoc to confirm that the invoice numbers are correct. If the invoice numbers are the same, you need to edit or remove one of them to allow the document to be published.

The tax type code can't be used with account code

The error message **The TaxType code XXX cannot be used with account code XXX** shows if you select an incorrect tax rate for the transaction you’re trying to publish. For example, if you’re publishing a purchase document, you can’t select a sales tax rate.

To resolve this, make sure the tax rate reflects the correct document type. If you’re publishing a document as a:

- Purchase, spend money or A/P credit note – select an expenses tax rate
- Invoice (A/R) or A/R credit note – select an income tax rate

Unrecognised GUID Format (Xero error)

A Globally Unique Identifier (GUID) is a unique reference number used as an identifier in various software platforms.

When publishing to Xero, the most common reason for this error is that one of the required fields in the **Destinations** section of theedit document toolbar hasn't been completed. Often it's the **Contact** or **Account Code** fields.

To resolve the error, you need to make sure that all the required fields in the **Destinations** section are completed. These fields are indicated by a red asterisk. To do this:

1. In the document, click **Edit Document** to open the data toolbar.
2. Under **Destinations**, for each field with an asterisk, select the relevant option for the document. If you're not sure what to select, see the [document field explanations](About-publishing-documents-to-Xero.md).
3. Click **Publish** to try publishing the document again.

Document cannot be re-published with this Publish As type

The error message **This document cannot be re-published with this Publish As type** occurs when you re-publish a document to Xero and either:

- The initial transaction in Xero has been deleted, voided, edited, reconciled or paid.
- You’re changing the **Publish As** field from a purchase type document to a sales type document, or vice versa. For example, you can't re-publish a document as **Invoice (A/R)** if it was initially published as **Purchase**.

This is because when you re-publish a document, it updates the initial transaction in Xero with the new information. It doesn’t create a new transaction.

To resolve this:

1. Upload the document to Hubdoc as a new document.
2. Publish the document to Xero to create a new transaction.
3. (Optional) Delete the original document in Hubdoc to avoid having duplicates.

Document cannot be re-published with this Status type

The error message **This document cannot be re-published with this Status type** occurs if either:

- The initial transaction in Xero has been deleted, voided, edited, reconciled or paid.
- You’re changing the **Status** field in reverse order of the transaction process. For example, you can re-publish a document as **Awaiting Payment** if it was initially published as **Draft**, but you can’t re-publish it as **Draft** if it was initially published as **Awaiting Payment**.

This is because when you re-publish a document, it updates the initial transaction in Xero with the new information. It doesn’t create a new transaction.

To resolve this:

1. Upload the document to Hubdoc as a new document.
2. Publish the document to Xero to create a new transaction.
3. (Optional) Delete the original document in Hubdoc to avoid having duplicates.

Account code isn't valid

The error message **Account code XX is not a valid code for this document** shows because the **Show in expense claims** checkbox isn’t selected for the account in your chart of accounts in Xero.

To resolve this:

1. In Xero, [edit the account code in your chart of accounts](Add-or-edit-an-account-in-your-chart-of-accounts.md).
2. Select the **Show in Expense Claims** checkbox.
3. Refresh the page in Hubdoc, then re-publish the document.

Line item tax amounts error

The error message **Line item tax amounts do not total to document tax amount** shows because the tax value in the **Transactions Details** section doesn’t match the tax value under **Destinations**. This is often due to rounding, as Hubdoc rounds to two decimal places.

To resolve this:

1. Confirm the tax value under **Destinations**.
2. Under **Transaction Details**, click the arrow next to **Tax Rate**, then select **Extracted Amount**.
3. In the dialogue box that appears, enter the correct tax amount.
4. Under **Destinations**, click **Publish**.

Transaction isn’t updated when republishing

If you’ve republished a document in Hubdoc but the transaction in Xero isn’t updating, it might be because:

- It’s a purchase or credit note document that was initially published with a status of **Authorized**
- The initial transaction created in Xero is deleted, voided, edited, has a payment applied to it, or it’s reconciled
- You’re trying to change the **Published As** or **Status** fields

To republish with the updated details, you'll need to:

1. Delete or void the transaction in Xero.
2. Download the document in Hubdoc.
3. Delete the document in Hubdoc.
4. Upload the document into Hubdoc again with the updated details.
5. [Publish to Xero](Publish-Hubdoc-documents-to-Xero.md).

Contact has been archived

The error message **The contact with the specified contact details has been archived. The contact must be un-archived before creating new invoices or credit notes** is prompted by Xero.

When two contacts are merged together in Xero, one of the contacts is archived, depending on how they were merged. If you:

- Merged Customer A into Customer B, then Customer A is archived
- Merged Customer B into Customer A, then Customer B is archived

To resolve this, do one of the following:

- Select a new contact in Hubdoc, then publish the document in Hubdoc again
- [Restore the contact in Xero](Archive-or-restore-contacts.md), then publish the document in Hubdoc again

## What's next?

Once you’ve resolved the error and published the document in Hubdoc, [view the transaction in Xero](Find-and-view-transactions.md).