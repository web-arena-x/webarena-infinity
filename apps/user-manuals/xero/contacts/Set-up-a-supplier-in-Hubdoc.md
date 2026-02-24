# Set up a supplier in Hubdoc

Source: https://central.xero.com/s/article/Set-up-a-supplier-in-Hubdoc

---

## Overview

- Add a supplier account before you upload a document for them.
- Configure a supplier’s document fields to determine how their documents will be published to Xero or other third party software.

## About suppliers in Hubdoc

When you upload a document for a new supplier, Hubdoc will automatically create a supplier account for them. You can also manually add a supplier account before you upload their first document.

To publish a supplier’s document to Xero or another third party software, you need to configure their document fields. Configurations are rules and settings you apply that determine how the document will be published.

There are two different types of configurations:

- Basic configurations – you can save basic configurations when you set up or [customise a supplier](Customise-account-connections.md) in Hubdoc
- Integration configurations – you can save integration configurations when you set up or customise a supplier or [publish a document](Publish-Hubdoc-documents-to-Xero.md) to Xero

If you configure a document’s fields while publishing it, you have the option to save the configuration to apply to all future documents for the same supplier. If you configure the fields on the supplier level, they will automatically be applied to all their future documents.

## Add a supplier

1. On the dashboard, click the settings icon in the top right-hand corner.
2. Select the **Suppliers** tab.
3. Click **Add**.
4. Enter supplier name, then click **Create Supplier**.
5. Under **Integrations** select which configurations you’d like to set up.
6. Click **Save Changes**.

## Configurations explained

### Basic configurations

You can configure the following data when you set up or customise a supplier in Hubdoc.

| Field | Description |
| --- | --- |
| Document Location | You may want to [change the location where documents are saved](Customise-account-connections.md) in Hubdoc when they’re added. For example, multiple staff members have cell phone accounts with the same supplier, so it’s easier to split accounts by name rather than account number. |
| Duplicate Detection | To [turn off duplicate detection](Customise-account-connections.md) for a particular supplier. |
| Supplier Due Date | The date you select will become the due date of all future documents for this supplier. |
| Autopay | Select the **Autopay** checkbox if the documents relate to bills that are automatically paid via a pre-authorised payment. Selecting this checkbox won't trigger an automatic payment from your bank account. |
| Email Alerts | You can [customise email alerts](Customise-account-connections.md) to let you know there’s a new document in Hubdoc, or that a bill is due in five days. |

### Integration configurations

You can configure the data in the table below when you set up or customise a supplier or publish a document to Xero.

To view the saved integration configurations of a document you’ve already published:

1. [Find and open the document](/s/article/Search-for-documents-in-Hubdoc?userregion=true) you want to publish.
2. In the data panel to the right of the document, under **Destinations** click **Xero** or your other third party software.
3. (Optional) To apply these settings to all future documents for this supplier, select the **Save configuration** checkbox.

| Field | Description |
| --- | --- |
| Status | Required field for **Purchase** and **Credit Note** documents. Select **Draft** to publish the document as a draft transaction, **Awaiting Approval** for a transaction that needs to be approved, or **Awaiting Payment** to create a transaction that’s ready to be paid. |
| Contact | Required field for all documents. Hubdoc imports your [contact list from Xero](Contacts-in-Xero.md). Select or begin typing the name of the Xero contact for the document. If the contact isn't created in Xero, click **Add [x] as a new contact**, enter the name, then click **Create** to confirm. The new contact is created in Hubdoc and Xero. |
| Account Code | Required field for all documents. Hubdoc imports your chart of accounts when you connect to Xero. Select or begin typing the appropriate account code from the list. |
| Customer | Optional field for **Purchase** and **Spend Money** documents. Select a contact if you want to [pass the cost of the expense onto your customer](Add-billable-expenses-to-bills.md). The list of contacts represents those in the **All** tab in Xero. A contact not already a customer in Xero will become a customer when the document is published. |
| Description | Optional field for all documents. Use this field to record additional information about this document. Data entered here is imported into the **Description** field in the transaction in Xero. If you publish a document with multiple lines, enter different descriptions for each line. If you select the **Save configuration** checkbox, the description isn’t saved as part of the configuration settings. The **Description** field is blank by default for all new documents. |
| Bank Account | Required field for **Spend Money** documents. Hubdoc imports your account list from Xero. Select or begin typing the name of the bank account that was used to pay for the purchase. If the bank account you're looking for isn't on this list, confirm that it’s [set up in Xero](Add-a-bank-account-or-credit-card-account.md). |
| Credit Note Type | Required field for **Credit Note** documents. Select **A/P Credit** or **A/R Credit**. A/P Credit documents are created as purchase (accounts payable) credit notes in Xero and A/R Credit documents are created as sales (accounts receivable) credit notes in Xero. Xero only displays the **Reference** if there’s a matching invoice with the same reference for that supplier. |

## What's next?

[Upload or email your supplier’s documents](Upload-or-email-documents-into-Hubdoc.md) into Hubdoc.