# Complete a Prime Contract with DocuSignÂ®

Source: https://v2.support.procore.com/product-manuals/prime-contracts-project/tutorials/complete-a-prime-contract-with-docusign

---

## Background

After a project team member creates a prime contract, Procore users with a DocuSignÂ® account can prepare a DocuSignÂ® envelope for the contract to send to the appropriate recipient(s) to request a signature.

If you are the recipient of a signature request, you do not need a DocuSignÂ® account. However, if you do have a DocuSignÂ® account and the email address matches the email you use in Procore, a copy of any documents you sign will be saved in your DocuSignÂ® account. See [Do I need a DocuSignÂ© account?](/faq-do-i-need-a-docusign-account)

## Things to Consider

- **Required User Permissions:**

  - 'Admin' level permissions on the project's Prime Contracts tool.
- **Additional Information:**

  - Once you sign into you DocuSignÂ® account from Procore, you will NOT need to sign in again until the login token expires. Once expired, the 'Re-Authentication Required' banner appears in Procore. To learn more, see [What do the different DocuSignÂ® banners in Procore mean?](/faq-what-do-the-different-docusign-banners-in-procore-mean)

## Prerequisites

- [Enable the DocuSignÂ® Integration on Your Company's Procore Account](/product-manuals/admin-company/tutorials/enable-the-docusign-integration-on-your-companys-procore-account)
- [Enable the DocuSignÂ® Integration on a Project](/product-manuals/admin-project/tutorials/enable-or-disable-the-docusign-integration-on-a-procore-project)
- To request signatures with Procore + DocuSignÂ®: You must have an active DocuSignÂ® account. Recipients do NOT need an account to sign a document. See [Do I need a DocuSignÂ© account](/faq-do-i-need-a-docusign-account) and [How do I get a DocuSignÂ® account?](/faq-how-do-i-get-a-docusign-account)

- [Create Prime Contracts](/product-manuals/prime-contracts-project/tutorials/create-prime-contracts) or [(Beta) Create Prime Contracts](/product-manuals/prime-contracts-project/tutorials/beta-create-prime-contracts)

## Steps

- Open the Prime Contract in Procore
- Log in to DocuSignÂ®
- Prepare the DocuSignÂ® Envelope

### Open the Prime Contract in Procore

1. Navigate to the project's **Prime Contract** tool.
2. In the **Contracts** tab, locate the contract.
3. Click the **Number** link to open it.
4. In the contract's **General Information** card, click **Edit**.
5. Mark the **Sign with DocuSign****Â®**check box.
6. Complete the data entry as required. See [(Beta) Create Prime Contracts](/product-manuals/funding-project/tutorials/beta-create-fundings).
7. Click **Save**.
8. After the data entry is complete, choose an option:

   - If this is an existing contract, click **Send with DocuSign** at the top of the page.
   - If this is a new contract, click **Create & Send with DocuSign** at the bottom of the page.   
        
        
        
      This launches DocuSignÂ®.

### Log In to DocuSignÂ®

If you are NOT logged into your DocuSignÂ®account when you launch the DocuSignÂ® application from Procore:

##### Â Notes

- To learn how to gain access to DocuSignÂ® from a Procore tool, see one of the tasks in [Which Procore project tools support the DocuSignÂ® integration?](/faq-which-procore-project-tools-support-the-docusign-integration)
- To log into DocuSignÂ® from Procore, you need valid login credentials (an email address and a password) for a DocuSignÂ® account. To learn more, see [Do I need a DocuSignÂ© account?](/faq-do-i-need-a-docusign-account) and [How do I get a DocuSignÂ® account?](/faq-how-do-i-get-a-docusign-account)

1. At the DocuSignÂ® Log In page, type your email address in the **Email** box:
2. Click **Next**.
3. Enter your password.
4. Click **Log In**.

### Prepare the DocuSignÂ® Envelope

Once you are logged in, the 'Upload a Document and Add Envelope Recipient' page appears. Complete these steps:

- Add Documents to the Envelope
- Add Recipients to the Envelope
- Add a Message to All Recipients
- Preview the Signature Fields & Send the Envelope

#### Add Documents to the Envelope

The following Procore information automatically populates the DocuSignÂ® envelope:

- A PDF copy of the contract is automatically added to the 'Add Documents to Envelope' section.
- The required signature boxes for each 'Role' on the contract. For example, the *Owner/Client*, *Contractor*, and *Architect/Engineer* who are parties on the contract. This includes each users 'Name' and 'Email Address.' For more information, see [Add Recipients to the Envelope](https://support.procore.com/products/online/user-guide/project-level/funding/tutorials/complete-a-funding-with-docusign) below.

You have the option to add other documents as follows:

1. *Optional:* If you want to add additional documents to the envelope, choose one of the available options under the 'Add Documents to the Envelope' section:

       

   ##### Â Note

   The available options in the 'Add Documents to the Envelope' section are developed and maintained by DocuSignÂ®. To learn how to use DocuSignÂ®, Procore recommends reviewing the content on [support.docusign.com](https://support.docusign.com/).

1. **Upload**
2. **Use a Template**
3. **Get From Cloud**

#### Add Recipients to the Envelope

To add recipients to the envelope:

1. Under 'Add Recipients to the Envelope', keep the default recipient blocks, their names, and their email addresses. This data is added to the envelope automatically by the Procore+DocuSignÂ® integration. If the data was specified in Procore, the values in the 'Name' and 'Email Address' fields of the recipient blocks correspond to these fields in Procore:

- **Architect**. This is the individual designated in the 'Architect/Engineer' field of the contract.
- **General Contractor**. This the individual who is designated in the 'Primary Contact' field in the Project Directory for the company designated in the 'Contractor'' field of the contract.
- **Owner**. This is the individual designated as the 'Owner/Client' in the contract.

  ##### Â Tips

  - **Not seeing one of the recipient blocks in DocuSignÂ®?** If your company has engaged the [Procore Custom Solutions](https://support.procore.com/products/online/custom-solutions) team to add custom fields to the Prime Contracts tool or if your company has implemented one of Procore's language or point-of-view dictionaries, the recipient blocks in your environment may be different. Check with your company's Procore Administrator to see if your tool has any custom fields. To learn more, see [What languages are available in Procore?](/faq-what-languages-are-available-in-procore) and [What tool names and terms are different in Procore for general contractors, owners, and specialty contractors?](/faq-what-tool-names-and-terms-are-different-in-procore-for-general-contractors-owners-and-specialty-contractors)
  - **Not seeing a 'Name' or 'Email Address' in a recipient block?** If data wasn't entered in one of the contract fields before you sent the item to DocuSignÂ®, there was no data to transfer to DocuSignÂ®. You will need to return to Procore, enter the data in the appropriate field, and resend the envelope to DocuSignÂ®.