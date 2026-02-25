# Complete Owner Invoices with DocuSignÂ®

Source: https://v2.support.procore.com/product-manuals/prime-contracts-project/tutorials/complete-owner-invoices-with-docusign

---

## Background

After your team creates an owner invoice, Procore users with a DocuSignÂ® account can prepare a DocuSignÂ® envelope for the invoice to send to the appropriate recipient(s) to request a signature.

If you are the recipient of a signature request, you do not need a DocuSignÂ® account. However, if you do have a DocuSignÂ® account and the email address matches the email you use in Procore, a copy of any documents you sign will be saved in your DocuSignÂ® account. After all of the required signatures are collected in DocuSignÂ®, Procore changes the status of the commitment to **Approved**.

## Things to Consider

- **Required User Permissions:**

  - 'Admin' level permissions on the project's **Prime Contracts** tool
- **Additional Information:**

  - Once you log into your DocuSignÂ® account from Procore, you will NOT need to sign in again until the login token expires. Once expired, the **Re-Authentication Required** banner appears in Procore. To learn more, see [What do the different DocuSignÂ® banners in Procore mean?](/faq-what-do-the-different-docusign-banners-in-procore-mean)
  - To complete the steps below, the invoice must be in *Approved*, *Approved as Noted*, or *Pending Owner Approval* status.

## Prerequisites

- [Enable the DocuSignÂ® Integration on Your Company's Procore Account](/product-manuals/admin-company/tutorials/enable-the-docusign-integration-on-your-companys-procore-account)
- [Enable the DocuSignÂ® Integration on a Project](/product-manuals/admin-project/tutorials/enable-or-disable-the-docusign-integration-on-a-procore-project)
- To request signatures using the Procore + DocuSignÂ® integration, you must have an active DocuSignÂ® account. You do NOT need a DocuSignÂ® account to sign a document. For details, see:

  - [Do I need a DocuSignÂ© account?](/faq-do-i-need-a-docusign-account)
  - [How do I get a DocuSignÂ® account?](/faq-how-do-i-get-a-docusign-account)
- [Create Owner Invoices](/product-manuals/prime-contracts-project/tutorials/create-owner-invoices)

## Steps

- Open the Owner Invoice
- Log in to DocuSignÂ®
- Prepare the DocuSignÂ® Envelope

### Open the Owner Invoice

There are two ways to open an owner invoice:

- From the **Prime Contracts** Tool
- From the **Invoicing** Tool

#### From the Prime Contracts Tool

1. Navigate to the project's **Prime Contracts** tool.
2. Locate prime contract associated with the owner invoice. Then click its **Number** link.
3. Click the **Invoices** tab.
4. In the **Invoices (Payment Applications)** table, click the **Invoice #** link.
5. In the invoice, click the **Edit** button.
6. In the **Summary** tab, click the **Update & Set Up DocuSign** button.

#### From the Invoicing Tool

If you have 'Admin' level permission on the **Prime Contracts** tool, you can also use the project's Invoicing tool to send invoices to DocuSignÂ® in bulk.

1. Navigate to the project's **Invoicing** tool.
2. Click the **Owner** tab.
3. Locate the invoice in the table. Then
4. , click the **Invoice #** link.
5. In the invoice, click the **Edit** button.
6. In the **Summary** tab, click the **Update & Set Up DocuSign** button.

Procore launches the DocuSignÂ® application. If you are not already logged into DocuSignÂ®, you will be prompted to enter your login credentials.

### Log in to DocuSignÂ®

If you are NOT logged into your DocuSignÂ®account when you launch the DocuSignÂ® application from Procore:

##### Â Notes

- To learn how to gain access to DocuSignÂ® from a Procore tool, see one of the tasks in [Which Procore project tools support the DocuSignÂ® integration?](/faq-which-procore-project-tools-support-the-docusign-integration)
- To log into DocuSignÂ® from Procore, you need valid login credentials (an email address and a password) for a DocuSignÂ® account. To learn more, see [Do I need a DocuSignÂ© account?](/faq-do-i-need-a-docusign-account) and [How do I get a DocuSignÂ® account?](/faq-how-do-i-get-a-docusign-account)

1. At the DocuSignÂ® Log In page, type your email address in the **Email** box:
2. Click **Next**.
3. Enter your password.
4. Click **Log In**.

### Prepare the DocuSignÂ® Envelope

Once you are logged into the DocuSignÂ®, the **Upload a Document and Add Envelope Recipient** page appears. Complete these steps:

- Add Documents to the Envelope
- Add Recipients to the Envelope
- Add a Message to All Recipients
- Add the Signature Fields & Send the Envelope

#### Add Documents to the Envelope

The following Procore information automatically populates the DocuSignÂ® envelope:

- A PDF copy of the invoice is automatically added to the **Add Documents to Envelope** section.

You have the option to add other documents as follows:

1. *Optional:* If you want to add additional documents to the envelope, choose one of the available options under the 'Add Documents to the Envelope' section:

   ##### Â Note

   The available options in the 'Add Documents to the Envelope' section are developed and maintained by DocuSignÂ®. To learn how to use DocuSignÂ®, Procore recommends reviewing the content on [support.docusign.com](https://support.docusign.com/).

1. **Upload**
2. **Use a Template**
3. **Get From Cloud**

#### Add Recipients to the Envelope

To add recipients to the envelope:

1. Under **Add Recipients to the Envelope**, keep the default recipient blocks, their names, and their email addresses. For owner invoices, you will typically add two (2) recipients as follows:

   - **Recipient 1.** In the **Name** box, type the name of the person at your company who is responsible for signing the payment applications. If a matching user exists in the Procore Project Directory, that user's name appears as a selection in the drop-down list and the Procore + DocuSignÂ® integration completes the email address on file. If the person is NOT in the Project Directory, you can type the email address here.
   - **Recipient 2.** In the **Name** box, type the name of the architect who is responsible for certifying the payment application with a signature. Typically, this is the architect or engineer on the project. If a matching user exists in the Procore Project Directory, that user's name appears as a selection in the drop-down list and the Procore + DocuSignÂ® integration completes the email address on file. If the person is NOT in the Project Directory, you can type the email address here.

##### Â Tip

**Want to add, change, or remove recipients DocuSignÂ®?** The options in the 'Add Recipients to the Envelope' section are developed and maintained by DocuSignÂ®. If you change the recipient information in DocuSignÂ®, keep in mind that any changes made in DocuSignÂ® do NOT update in Procore and can lead to unwanted results. To ensure the integration works as designed, Procore recommends keeping any recipient fields that may have been added to DocuSignÂ® by Procore. To learn how to use DocuSignÂ®, Procore recommends reviewing the content on [support.docusign.com](https://support.docusign.com/).