# Send a self-billed e-Invoice to the IRBM

Source: https://central.xero.com/s/article/Send-self-billed-eInvoices-to-the-IRBM

---

## Overview

- Send your consolidated self-billed e-invoices to the Inland Revenue Board of Malaysia (IRBM) for validation.

Tip

Check section 8.3 of the [e-Invoice specific guidelines](https://www.hasil.gov.my/media/uwwehxwq/irbm-e-invoice-specific-guideline.pdf) (IRBM website) if you’re unsure what you need to submit.

What you need to know

Self‑billed e‑Invoices are required in specific circumstances that are provided under section 8.3 of the [e-Invoice specific guidelines](https://www.hasil.gov.my/media/uwwehxwq/irbm-e-invoice-specific-guideline.pdf) (IRBM website). Where the transaction doesn’t fall within section 8.3, the Inland Revenue Board of Malaysia (IRBM) doesn’t permit self-billed e-Invoices to be created. If you need more assistance, consult your financial advisor or find one in the [Xero directory](https://www.xero.com/advisors/) (Xero website).

On the e-Invoice in Xero, add a blank line item with a description that states the ID number for each customs declaration form, with a comma between them. For example, CUSTOMS: 123234234, 123123123123.

To mark a bill as self‑billed, assign the **MyInvois Classification** tracking option to each line in the bill.

When you send a self-billed e-Invoice to a foreign supplier, you don’t need to enter a TIN, as they won’t have one. To indicate to Invoici that they’re a foreign supplier, you need to make sure the country field in their contact record reflects an overseas (non-Malaysian) address.

You can [edit a contact](Edit-a-contact.md) to add any missing details. The mandatory contact fields are:

| Field | Description |
| --- | --- |
| **Contact name** | The supplier of the goods or services. |
| **Tax ID number (TIN)** (Not required for foreign customers) | The supplier’s TIN, then their Sales and Service Tax (SST) registration number, separated by a semicolon. Precede the SST number with SST, for example C12345678901;SST12345566. If a business doesn’t have a SST number, leave this out and just enter their TIN, for example C12345678901. For foreign suppliers, leave this field blank and Invoici will populate the field with the generic TIN for suppliers, **EI00000000030**. If an individual doesn’t have a TIN, leave this field blank and Invoici will populate it with the generic TIN for individuals, **EI00000000010**. You must also provide an **NRIC** as the **Business registration number**. |
| **Business registration number** | For businesses, enter the supplier’s business registration number. For Malaysian individuals, enter **NRIC**, then their MyKad or MyTentera IDs. For non-Malaysian individuals, enter **NRIC**, then their MyPR or MyKAS ID, or enter **PASSPORT:** followed by their passport number. |
| **Billing address** | The supplier’s address. Make sure the **Country** field is entered. |
| **Phone number** | The supplier’s phone number. If a foreign supplier doesn’t have a phone number, leave this field blank and Invoici will populate with the IRBM approved number **+00000000**. Enter **NA** if you’re issuing a consolidated e-Invoice. |

Send an individual self-billed e-Invoice

Tip

Businesses in the relaxation phase aren’t required to send individual self-billed e-Invoices.

### Enable individual self-billed e-Invoices

1. Log in to [Invoici](http://my.invoici.net/) (Invoici website) with your Xero login details.
2. Next to the organisation you want, click **Open business**.
3. Click **Settings**.
4. Next to **Self-billing settings**, select **Individual**.

While this setting is enabled, Invoici includes any individual self-billed e-Invoices that fail validation in the end-of-month self-billed consolidated e-Invoice.

You need to create self‑billed e‑Invoices as bills in Xero. When you create the bill, you need to [assign the MyInvois Classification tracking option](Track-transactions.md), then approve the bill. Once the bill is approved, Invoici automatically sends it to MyInvois for validation.

For the self-billed e-Invoice to be validated, it must have an invoice number in the bill’s **Reference** field. Enter the invoice number from the supplier invoice you’re creating the bill from.

It takes IRBM a few minutes to validate the invoice, so there might be a short delay before you can view it. Once it’s validated, the status shows in the **History and notes** section of the invoice.

### Resubmit a self-billed e-Invoice

Self-billed e-Invoices are created as bills in Xero and when you approve them, Xero sends them to IRBM.

If a bill has already been approved but there was an issue with submitting it, once the error is resolved, you can resubmit it for validation:

1. In Invoici, select the **eInvoices** tab.
2. Search for and find the e-Invoice that failed validation.
3. Click **Resubmit**.

### Send a self-billed credit note

Use a self-billed credit note to correct a self-billed e-Invoice that’s already been submitted to IRBM and can’t be cancelled. e-Invoices can only be cancelled within 72 hours of submission.

To submit a self-billed credit note:

1. Create a [supplier credit note](Add-a-credit-note-to-a-bill.md).
2. Approve the credit note.
3. Apply the credit note to the relevant bill in Xero. The bill must have been validated with IRBM as a self-billed e-Invoice.

The supplier credit note is then automatically submitted to Invoici.

For refund notes, process the refund in Xero before you email the credit note to IRBM.

Once you send the credit or refund note, you can check the validation status in the **History and notes** section.

## What's next?

Learn how to [send a consolidated self-billed e-Invoice to the IRBM](Send-consolidated-eInvoices-to-the-IRBM.md) if required.