# Resolve issues with documents in Hubdoc

Source: https://central.xero.com/s/article/Resolve-issues-with-documents-in-Hubdoc

---

## Overview

- Resolve issues you have getting a document into Hubdoc, data not extracting or documents not displaying correctly.

Data isn't being extracted

A document can fail the extraction process for a few reasons. The most common are:

- The image is too blurry, crumpled or faded to properly recognise the information.
- Mandatory information such as date, amount or supplier name is missing from the image.
- There are multiple receipts for different transactions in the same image. If there are multiple receipts in one image, they must be for the same transaction.

Can't get documents into Hubdoc

If you send documents into Hubdoc using your organisation's unique email address, you might receive an 'undelivered' error message, or the document won't upload. This most commonly occurs if you're using Outlook to send emails into Hubdoc.

To successfully email documents into your organisation, check the organisation's unique email address has been changed from the default one assigned when the organisation was created. If it hasn't been updated, [change it](Update-Hubdoc-organisation-settings.md) in **Organization Settings**.

If an email sent to your organisation’s unique email address didn’t create a document in Hubdoc, it could be due to one of the following:

- The email address was missing the @app.hubdoc.com domain.
- The attachment wasn’t a PDF or image file.
- The email was blocked as spam. If you’re using a middleware email forwarding service, Hubdoc might return an error message to your email domain because it thinks the email sender is a spammer. To prevent the email forwarding service from blocking Hubdoc’s domain from future emails, look for an allowlist or safesenders list option and enter your @app.hubdoc.com email forwarding address into the allowlist field.
- Hubdoc can't download files through a hyperlink. If the file is only available this way, download the file manually and email it separately to your Hubdoc organisation.
- If you're using Outlook to email documents, a corrupt contact can cause the removal of attachments from the email. Instead of using the existing contact record when creating a new email, type the full email address in the **To** field, without accepting Outlook's suggestion. When the document appears in Hubdoc, delete the corrupt contact in Outlook.

You might also receive an error message attached to a returned email, which gives a more precise cause for the email being rejected.

The document won't load

Sometimes a document won't load properly due to a corrupt file or a Hubdoc system error.

To resolve this:

- Refresh your screen to speed up loading
- Delete the existing document in Hubdoc and try to manually upload it again
- Email the document to your organisation’s unique email address

If you still can't get the document into Hubdoc, please reach out to our support team, and provide the [Document ID](View-a-document-s-audit-trail-in-Hubdoc.md) where available.

Potential duplicate documents

Hubdoc shows a potential duplicate document icon in the data toolbar for any document it identifies as a potential duplicate.

To choose whether to keep or remove a document:

1. Click **Show Duplicates** in the data toolbar to open a panel showing the document alongside all matching documents.
2. For each document, click **Move to Trash** to remove the document from your organisation or **Not a duplicate** to keep the document.

Hubdoc doesn't automatically publish any documents identified as potential duplicates. You need to manually configure and publish the document, even if it's from a supplier you have automatic publishing rules set up for.

Issues caused by auto-fill

Some browser extensions such as LastPass and Dashlane automatically populate online forms. They can incorrectly attempt to populate saved data, which replaces the data already associated with your Hubdoc documents.

Usually this happens when you switch between documents in Hubdoc. The total amount, date and supplier name on the selected document immediately change.

To prevent auto-fill replacing existing data in your documents, disable the browser extension.

Display problems

If you're having display problems, eg the preview image or **Edit Document**isn't showing, it might be due to your browser's zoom settings. To ensure your browser is set to 100% zoom, you can change it to 90% then to 100%.

To adjust your browser’s zoom settings take a look at the help page for your browser:

[Change text, image, and video sizes (zoom)](https://support.google.com/chrome/answer/96810?hl=en) (Google Chrome Help)

[Font size and zoom](https://support.mozilla.org/en-US/kb/font-size-and-zoom-increase-size-of-web-pages) (Mozilla Firefox Support)

[Zoom in on webpages](https://support.apple.com/guide/safari/zoom-in-on-webpages-ibrw1068) (Safari User Guide)

[Ease of Access in Microsoft Edge](https://support.microsoft.com/en-us/help/4000734/windows-10-microsoft-edge-ease-of-access) (Microsoft Edge Support)

Documents are automatically archived

### How it works

The **Archived** tab contains documents that no longer require user action. They show a green checkmark to indicate they’ve passed through the **Processing** and **Review** tabs successfully, and have been published.

### Reasons for archived documents

| Reason | Solution |
| --- | --- |
| Organisation needs upgrading | If your Hubdoc trial has expired, you need to [upgrade to a paying organisation](Update-your-Hubdoc-payment-details.md) before you can process and extract data or publish documents |
| **Auto-sync** is selected | If you have auto-sync enabled for a supplier account, documents from that supplier skip the **Review** tab and are immediately published to your configured destination. Auto-sync needs to be [turned off for a supplier](Publish-Hubdoc-documents-to-Xero.md), including sub-accounts, if you want to review these documents before they're published. |

## What's next?

Once you've resolved the issue, [publish the document to Xero](Publish-Hubdoc-documents-to-Xero.md).