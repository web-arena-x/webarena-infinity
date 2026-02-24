# Create a Bid Package with Bid Management Enhanced Experience

Source: https://v2.support.procore.com/product-manuals/bidding-project/tutorials/create-a-bid-package-with-bid-management-enhanced-experience

---

##### Note

The content below describes functionality that is part of the new *Bid Management Enhanced Experience*. See [About Bid Management Enhanced Experience](/process-guides/about-bid-management-enhanced-experience/).

## Background

The Enhanced Bid Management experience for creating a bid package is designed to streamline your workflow. It focuses on simplifying the creation of the bid package, which is a comprehensive set of documents (including drawings, specifications, and scope of work). This package provides all the information potential contractors need to prepare an accurate and competitive proposal.

## Things to Consider

- **Required User Permissions:**

 - 'Admin' level permissions on the project's Bidding tool.
- **Additional Information:**

 - The project does not have to be in a Bidding stage to create a bid package.
 - 'Admin' level permissions are required in order to be assigned as a Primary Bidding Contact.

## Prerequisites

- [Update to the New Bid Management Experience](/product-manuals/bidding-project/tutorials/update-to-the-new-bid-management-experience)

## Steps

1. Navigate to the project's **Bidding** tool.
2. Click **+ Create Bid** **Package**.
3. Enter the following information:

   - **Information**

     - **Name\*:** Enter a name for your bid package. This will show up on the Bidding toolâs list page and in the email that your subcontractors will receive.
     - **Number:** Enter a number for your bid package. If you have existing bid packages, this field will populate with the next number in the sequence.
     - **Status:** Select 'Open' if the bid package is still in progress. Select 'Closed' if the bid has been awarded and closed. Once a bid is 'Closed', bidders will be unable to see the bid information.
     - **Primary Bidding Contact\*:** Specify a primary contact from whose name you want the bid invitation to be sent .

       - The Primary Bidding Contact will be listed on all bid correspondence and receive all bid-related emails instead of the bid package creator.
     - **Bid Submission Notifications:** Add members to this list who will be notified when bids are submitted

       - Users with 'Read Only' or 'Standard' permissions will receive bid package access when added to the Bid Submission Notifications field.
   - **Dates**

     - **Bid Due Date\*:** Set the date and time when this bid will be due. If the bid is extended, immediately change the date so bidders can enter amounts.   
       *Note:* You can check the 'To be determined' checkbox if the bid due date is undetermined.
     - **RFI Deadline:** Set an RFI deadline date.
     - **Anticipated Award Date:** Set an anticipated award date.
     - **Pre-Bid Meeting Date:** Set a pre-bid meeting date.

       - **Address:** Enter pre-bid meeting address.
       - **Online Meeting Link:** Enter online meeting link if available.
       - **Notes:** Enter any pre-bid meeting notes.
     - **Site Walkthrough Date:** Set the Walkthrough date.

       - **Notes:** Enter any relevant information about the walkthrough.
   - **Invitation to Bid**

     - **Project Description\*:** Enter a description that will appear on the invitation email that is sent to invited bidders.
     - **Bidding Instructions\*:** Enter Bid instructions and a link to Procore's Bidding Support page for bidders to quickly find document download guidance.

       - Set a default for both the **Project Description** and **Bidding Instructions** fields in the Company Admin tool to auto-populate each time you create a bid package. See [Set the Default Company Bidding Configuration](/product-manuals/admin-company/tutorials/set-the-default-company-bidding-configuration).
   - **General Settings**

     - **Flexible Bid Due Date:** Select the box to accept bid submissions past the due date.

       - You can also enable late submissions for all project bid packages. See [Configure Advanced Settings: Bidding](/product-manuals/bidding-project/tutorials/configure-advanced-settings-bidding) for more information.
     - **Bid Documents:** Select the box to include documents as downloadable files in the invitation to bid email.

       - You can also include documents as downloadable files for all project bid packages. See [Configure Advanced Settings: Bidding](/product-manuals/bidding-project/tutorials/configure-advanced-settings-bidding) for more information.
     - **Bid Reminder Emails:** Enter the number of days before the bid due date to start sending reminder emails.

       - This setting also configures the frequency of NDA reminder emails.
       - You can also enable bid reminder and NDA reminder emails for all project bid packages. See [Configure Advanced Settings: Bidding](/product-manuals/bidding-project/tutorials/configure-advanced-settings-bidding) for more information.
     - **Offline Bids:** Select the box to *only* allow offline bid submissions.   
       *Note:* Bidders will not be able to submit bids via email and forces the bidders to only bid using the Planroom or Bid Board tools.
     - **Bid Submission Confirmation Message:** Enter a message that will be sent to bidders once they submit their bid.   
       *Note:* Set a default for this field in Company Admin tool to auto-populate each time you create a bid package. See [Set the Default Company Bidding Configuration](/product-manuals/admin-company/tutorials/set-the-default-company-bidding-configuration).
   - **Privacy and Visibility Settings**

     - **Blind Bidding:** Select the box to enable Blind Bidding. Blind bidding hides all bids until the Bid Due Date passes. See [What is blind bidding?](/faq-what-is-blind-bidding)

       - Once enabled, you have the option to select a **Manager**.

         - Assigning a manager will bypass the Bid Due Date and allow the manager to reveal the bids at any time.
       - **Public Bid Opening Details:**

         - **Date:** Enter public bid opening date.
         - **Online Meeting Link:** Enter online meeting link if available.
         - **Address:** Enter address if available.
       - You can also enable blind bidding for all project bid packages. See [Configure Advanced Settings: Bidding](/product-manuals/bidding-project/tutorials/configure-advanced-settings-bidding) for more information.
     - **Non-Disclosure Agreement (NDA):** Select the box to Require an NDA. Bidders will need to sign an NDA to see the project name and details. See [Non-Disclosure Agreement (NDA) FAQ](/faq-non-disclosure-agreement-nda-faq) for more information.

       - Once enabled, you have the option to select the **Show project name before NDA is signed** box.

         - This allows bidders to see the project name before they sign the NDA. All other project details will be hidden.
       - Click **Upload File** to upload your NDA file. Only 1 file can be added to this section.
     - **Public Discovery:** Select the box to enable public discovery.

       - Once enabled your bid package will be listed on the Procore Construction Network, making it searchable to thousands of external vendors. See [Enable Public Discovery](/product-manuals/bidding-project/tutorials/enable-public-discovery) for more information.
       - **Procore Construction Network Project Details:** Complete the fields below to help subcontractors find your project on the network.

         - **Trades and Services**
         - **Business Classifications**
         - **Funding Type**
         - Check the **Location Visibility for NDA Projects** box to allow city and state to appear in public search results for NDA projects. Full address will not be shown.

#### Attach Bid Documents

##### Â Important

Bid packages containing more than 100,000 files may lead to degraded application performance.

*Note:* We recommend creating a designated folder in the project's Documents tool to upload bid documents to. See [Create a Folder](/product-manuals/documents-project/tutorials/create-a-new-folder-in-the-project-level-documents-tool). You can create unlimited subfolders for each bid package and upload the relevant documents into each area. See [Upload Bid Documents](/product-manuals/bidding-project/tutorials/upload-bid-documents) or [Upload Files or Folders to the Project Level Documents Tool](/product-manuals/documents-project/tutorials/upload-files-or-folders-to-the-project-level-documents-tool).

1. On the Attach Files page, add files from the following tools as necessary.

   - **Drawings**
   - **Documents**
   - **Specifications**
   - ##### Regional Availability

     The Document Management tool is available in select countries. It is not yet available for Procore accounts in the U.S. To learn more, please reach out to your Procore point of contact.

     - **Document Management**