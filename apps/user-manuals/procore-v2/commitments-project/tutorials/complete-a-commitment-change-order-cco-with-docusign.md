# Complete a Commitment Change Order with DocuSignÂ®

Source: https://v2.support.procore.com/product-manuals/commitments-project/tutorials/complete-a-commitment-change-order-cco-with-docusign

---

## Background

After you create commitment change order for a commitment, Procore users with a DocuSignÂ® account can prepare a DocuSignÂ® envelope and send the Procore document to the appropriate recipient(s) to request a signature.

If you are the recipient of a signature request, you do not need a DocuSignÂ® account. However, if you do have a DocuSignÂ® account and the email address matches the email you use in Procore, a copy of any documents you sign will be saved in your DocuSignÂ® account. See [Do I need a DocuSignÂ© account?](/faq-do-i-need-a-docusign-account)

## Things to Consider

- **Required User Permissions:**

 - 'Admin' level permissions on the project's Commitments tool. 
     AND
 - If the Change Events tool is added to the project, 'Standard' or 'Admin' level permissions on the project's Change Events tool.
- **Additional Information:**

 - Once you log into your DocuSignÂ® account from Procore, you will NOT need to sign in again until the login token expires. Once expired, the 'Re-Authentication Required' banner appears in Procore. To learn more, see [What do the different DocuSignÂ® banners in Procore mean?](/faq-what-do-the-different-docusign-banners-in-procore-mean)

## Prerequisites

- [Enable the DocuSignÂ® Integration on Your Company's Procore Account](/product-manuals/admin-company/tutorials/enable-the-docusign-integration-on-your-companys-procore-account)
- [Enable the DocuSignÂ® Integration on a Project](/product-manuals/admin-project/tutorials/enable-or-disable-the-docusign-integration-on-a-procore-project)
- To request signatures with Procore + DocuSignÂ®: You must have an active DocuSignÂ® account. Recipients do NOT need an account to sign a document. See [Do I need a DocuSignÂ© account](/faq-do-i-need-a-docusign-account) and [How do I get a DocuSignÂ® account?](/faq-how-do-i-get-a-docusign-account)

- **Create a commitment change order**. You will need to know the change order tier setting configured on the project's Commitments tool. See [What are the different change order tier settings in Project Financials?](/faq-what-are-the-different-change-order-tier-settings-in-project-financials) If your project is configured with the:

 - **1-Tier Setting**. See [Create a Commitment Change Order](/process-guides/materials-user-guide-with-financials/create-a-change-order-cco).
 - **2- or 3-Tier Setting**. See [Create a Change Event](/product-manuals/change-events-project/tutorials/create-a-change-event) and then [Create a Commitment Change Order from a Change Event](/product-manuals/change-events-project/tutorials/create-a-commitment-change-order-from-a-change-event).

## Steps

- Open the Commitment Change Order in Procore
- Log in to DocuSignÂ®
- Prepare the DocuSignÂ® Envelope

### Open a Commitment Change Order in Procore

The steps below show you how to open a commitment change order in Procore.

1. Navigate to the project's **Commitments** tool.
2. In the **Contracts** tab, locate the commitment to work with and click the arrow to expand the commitment's change orders.
3. Click the **Change Order** link to open it.
4. In the change order, click **Edit**.
5. Mark the **Sign with DocuSign** check box.
6. Scroll to the bottom of the page and click **Complete with DocuSign**.   
      
      
    Procore launches the DocuSignÂ® web application. If you are NOT logged into your DocuSignÂ® account, you must follow the steps in Log in to DocuSignÂ®. If you are already logged in, proceed to Prepare the DocuSignÂ® Envelope.

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

Once you are logged into the DocuSignÂ®, the 'Upload a Document and Add Envelope Recipient' page appears. Complete these steps:

- Add Documents to the Envelope
- Add Recipients to the Envelope
- Add a Message to All Recipients
- Preview the Signature Fields & Send the Envelope

#### Add Documents to the Envelope

The following Procore information automatically populates the DocuSignÂ® envelope:

- A PDF copy of the change order is automatically added to the 'Add Documents to Envelope' section.
- The required signature boxes for each 'Role' on the contract. For example, the *General Contractor* or *Subcontractor* whose contract is affected by the change order. This includes each users 'Name' and 'Email Address.' For more information, see Add Recipients to the Envelope below.

1. *Optional:* If you want to add additional documents to the envelope, choose one of the available options under the 'Add Documents to the Envelope' section:

   ##### Â Note

   The available options in the 'Add Documents to the Envelope' section are developed and maintained by DocuSignÂ®. To learn how to use DocuSignÂ®, Procore recommends reviewing the content on [support.docusign.com](https://support.docusign.com/).

1. **Upload**
2. **Use a Template**
3. **Get From Cloud**

#### Add Recipients to the Envelope

To add recipients to the envelope:

1. Under 'Add Recipients to the Envelope', keep the default recipient blocks, their names, and their email addresses. This data is added to the envelope automatically by the Procore+DocuSignÂ® integration. If the data was specified in Procore, the values in the 'Name' and 'Email Address' fields of the recipient blocks correspond to these fields in Procore:

   - **Subcontractor**. This is the individual designated in the 'Architect/Engineer' field of the commitment associated with the change order.
   - **General Contractor**. This the individual who is designated in the 'Primary Contact' field in the Project Directory for the company designated in the 'Contractor' field of the commitment associated with the change order.

     ##### Â Tip

     - **Not seeing one of the recipient blocks in DocuSignÂ®?** If your company has engaged [Procore Custom Solutions](https://support.procore.com/products/online/custom-solutions) to customize your Procore form, tool, or workflow or if your company has implemented one of Procore's language or point-of-view dictionaries, the recipient blocks in your environment may be different. To learn more, see [Procore Custom Solutions](https://support.procore.com/products/online/custom-solutions), [What languages are available in Procore?](/faq-what-languages-are-available-in-procore), and [What tool names and terms are different in Procore for general contractors, owners, and specialty contractors?](/faq-what-tool-names-and-terms-are-different-in-procore-for-general-contractors-owners-and-specialty-contractors)
     - **Not seeing a 'Name' or 'Email Address' in a recipient block?** If data wasn't entered in one of the required fields before sending the item to DocuSignÂ®, there was no data in Procore to transfer. To resolve this, you can return to Procore, void the DocuSignÂ® envelope, enter the data in the appropriate field, and resend the document to DocuSignÂ®.