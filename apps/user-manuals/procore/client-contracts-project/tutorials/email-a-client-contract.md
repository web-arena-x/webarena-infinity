# Email a Client Contract

Source: https://v2.support.procore.com/product-manuals/client-contracts-project/tutorials/email-a-client-contract

---

##### Â Limited Release

The Client Contracts tool is available as a [limited release](https://support.procore.com/tc/procore/Legacy/Release%5FDocumentation%5FArchives/2022/Limited%5FRelease:%5FNew%5FPoint-of-View%5FDictionary%5Ffor%5FOwners%5F&%5FSpecialty%5FContractors%5Fin%5FUS%5FEnglish) for Procore customers in the United States who have implemented the Procore for Specialty Contractors point-of-view dictionary. To learn more, see [What tool names and terms are different in Procore for general contractors, owners, and specialty contractors?](/faq-what-tool-names-and-terms-are-different-in-procore-for-general-contractors-owners-and-specialty-contractors)

## Background

After you create one or more client contracts, you may have a need to share that information with other individuals. Unlike other Procore tools that send automatic email notifications to members of a distribution group or list when items are created, updated, or approved, a client contract contains sensitive financial data. To protect that data, client contracts much be explicitly sent to individuals.

## Things to Consider

- **Required User Permissions:**

 - *To send a client contract by email*, 'Standard' level permissions or higher permissions on the project's Client Contracts tool.
 - *To be named as a recipient in the To or CC field*, you must have a user account in the Project Directory.   
    *Note*: All recipients named in the To or CC field can view your client contract data in the PDF attached to the email message.
 - *To gain access to a contract by clicking the 'View this Contract' or 'View Online' link in the email message*:\* 'Admin' level permissions on the project's Client Contracts tool.   
     OR\* 'Read Only' or 'Standard' level permissions on the project's Client Contracts tool AND your name must be listed under 'Make this Visible only to Administrators and the Following Users.'
- **Limitations:**

 - Your recipients must have a user account in Procore's Project Directory. See [Add a User Account to the Project Directory](/product-manuals/directory-project/tutorials/add-user-account-to-project-directory).
 - Unlike other Procore tools, which send automated email notifications to distribution groups or lists, the Client Contracts tool requires you to use the steps below.

## Steps

1. Navigate to the project's **Client Contracts** tool.
2. Locate the client contract to work with. Then click its **Number** link.
3. Click **Email Contract**.
4. Complete the following fields:

   - **To** Start typing in this field to select your primary recipients from a list of users in the Project Directory. See [Add a User Account to the Project Directory](/product-manuals/directory-project/tutorials/add-user-account-to-project-directory).

     ##### Â Caution

     **Does your client contract contain attachments that don't want your email recipients to view?** If your project team has added attachments to the client contract you are sending by email, be sure to review all of those attachments to ensure you are OK with sending them to your recipients. Your recipients will have the ability to download those attachments. To learn how these attachments were added, see [Create Client Contracts](https://support.procore.com/products/online/user-guide/project-level/client-contracts/tutorials/create-client-contracts) and [Edit a Client Contract](https://support.procore.com/products/online/user-guide/project-level/client-contracts/tutorials/edit-a-client-contract).

- **CC** Start typing in this field to select your secondary recipients from a list of users in the Project Directory. See [Add a User Account to the Project Directory](/product-manuals/directory-project/tutorials/add-user-account-to-project-directory).
- **Private** Place a mark in this checkbox if you want to restrict recipients who have not been granted 'Admin' permission to the Client Contracts tool from gaining access to the client contract in the Procore web application.
 *Note*: All recipients named in the To or CC field will retain the ability to click **View PDF**.
- **Subject** This field automatically completes based on the name of the client contract, but you may make any additional changes to the field.
- **Attachments** Attach any related files or documents.
- **Message** Include a message to the recipients.
- Click **Send**.