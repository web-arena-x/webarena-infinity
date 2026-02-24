# Create a Bid Package with Bid Management Enhanced Experience - Procore

Source: https://support.procore.com/products/online/user-guide/project-level/bidding/tutorials/create-a-bid-package-bid-management-enhanced-experience

---

##### Note

The content below describes functionality that is part of the new *Bid Management Enhanced Experience*. See [About Bid Management Enhanced Experience](https://support.procore.com/products/online/user-guide/project-level/bidding/tutorials/about-bid-management-enhanced-experience "About Bid Management Enhanced Experience").

## Background

The Enhanced Bid Management experience for creating a bid package is designed to streamline your workflow. It focuses on simplifying the creation of the bid package, which is a comprehensive set of documents (including drawings, specifications, and scope of work). This package provides all the information potential contractors need to prepare an accurate and competitive proposal.

## Things to Consider

- **Required User Permissions:**
  - 'Admin' level permissions on the project's Bidding tool.
- **Additional Information:**
  - The project does not have to be in a Bidding stage to create a bid package.
  - 'Admin' level permissions are required in order to be assigned as a Primary Bidding Contact.

## Prerequisites

- [Update to the New Bid Management Experience](https://support.procore.com/products/online/user-guide/project-level/bidding/tutorials/update-to-the-new-bid-management-experience "Update to the New Bid Management Experience")

## Steps

1. Navigate to the project's **Bidding** tool.
2. Click **+ Create Bid Package**.
3. Enter the following information:
   - **Information**:
     - **Name**\*: Enter a name for your bid package. This will show up on the Bidding tool’s list page and in the email that your subcontractors will receive.
     - **Number**: Enter a number for your bid package. If you have existing bid packages, this field will populate with the next number in the sequence.
     - **Status**: Select 'Open' if the bid package is still in progress. Select 'Closed' if the bid has been awarded and closed. Once a bid is 'Closed', bidders will be unable to see the bid information.
     - **Primary Bidding Contact**\*: Specify a primary contact from whose name you want the bid invitation to be sent.
       - The Primary Bidding Contact will be listed on all bid correspondence and receive all bid-related emails instead of the bid package creator.
     - **Bid Submission Notifications**: Add members to this list who will be notified when bids are submitted.
       - Users with 'Read Only' or 'Standard' permissions will receive bid package access when added to the **Bid Submission Notifications** field.
   - **Dates**:
     - **Bid Due Date**\*: Set the date and time when this bid will be due. If the bid is extended, immediately change the date so bidders can enter amounts.   
       *Note:* You can check the 'To be determined' checkbox if the bid due date is undetermined.
     - **RFI Deadline**: Set an RFI deadline date.
     - **Anticipated Award Date**: Set an anticipated award date.
     - **Pre-Bid Meeting Date:**Set a pre-bid meeting date.
       - **Address**: Enter pre-bid meeting address.
       - **Online** **Meeting** Link: Enter online meeting link if available.
       - **Notes**: Enter any pre-bid meeting notes.
     - **Site Walkthrough Date**: Set the Walkthrough date.
       - **Walkthrough Notes**: Enter any relevant information about the walkthrough.
   - **Invitation to Bid:**
     - **Project Description\*:**Enter a description that will appear on the invitation email that is sent to invited bidders.
     - **Bidding Instructions\*:**Enter Bid instructions and a link to Procore's Bidding Support page for bidders to quickly find document download guidance.
       - Set a default for both the **Project Description** and **Bidding Instructions** fields in the Company Admin tool to auto-populate each time you create a bid package. See [Set the Default Company Bidding Configuration](https://support.procore.com/products/online/user-guide/company-level/admin/tutorials/set-the-default-company-bidding-configuration "Set the Default Company Bidding Configuration").
   - **General Settings:**
     - **Flexible Bid Due Date:** Select the box to accept bid submissions past the due date.
       - You can also enable late submissions for all project bid packages. See [Configure Advanced Settings: Bidding](https://support.procore.com/products/online/user-guide/project-level/bidding/tutorials/configure-advanced-settings-bidding "Configure Advanced Settings: Bidding") for more information.
     - **Bid Documents:**Select the box to include documents as downloadable files in the invitation to bid email.
       - You can also include documents as downloadable files for all project bid packages. See [Configure Advanced Settings: Bidding](https://support.procore.com/products/online/user-guide/project-level/bidding/tutorials/configure-advanced-settings-bidding "Configure Advanced Settings: Bidding") for more information.
     - **Bid Reminder Emails:**Enter the number of days before the bid due date to start sending reminder emails.
       - Bid Reminder Emails are sent at 11:30AM UTC (3:30AM PST) daily.
       - You can also enable bid reminder emails for all project bid packages. See [Configure Advanced Settings: Bidding](https://support.procore.com/products/online/user-guide/project-level/bidding/tutorials/configure-advanced-settings-bidding "Configure Advanced Settings: Bidding") for more information.
     - **Offline Bids:**Select the box to *only* allow offline bid submissions.  
       *Note:* Bidders will not be able to submit bids in Procore when this setting is enabled.
     - **Bid Submission Confirmation Message:**Enter a message that will be sent to bidders once they submit their bid.  
       **Note:** Set a default for this field in Company Admin tool to auto-populate each time you create a bid package. See [Set the Default Company Bidding Configuration](https://support.procore.com/products/online/user-guide/company-level/admin/tutorials/set-the-default-company-bidding-configuration "Set the Default Company Bidding Configuration").
   - **Privacy and Visibility Settings:**
     - **Blind Bidding:**Select the box to enable Blind Bidding. Blind bidding hides all bids until the Bid Due Date passes. See [What is blind bidding?](https://support.procore.com/faq/what-is-blind-bidding "What is blind bidding?")
       - Once enabled, you have the option to select a **Manager**.
         - Assigning a manager will bypass the Bid Due Date and allow the manager to reveal the bids at any time.
       - **Public Bid Opening Details:**
         - **Date**: Enter public bid opening date.
         - **Online** **Meeting** **Link**: Enter online meeting link if available.
         - **Address**: Enter address if available.
       - You can also enable blind bidding for all project bid packages. See [Configure Advanced Settings: Bidding](https://support.procore.com/products/online/user-guide/project-level/bidding/tutorials/configure-advanced-settings-bidding "Configure Advanced Settings: Bidding") for more information.
     - **Non-Disclosure Agreement (NDA):**Select the box to Require an NDA. Bidders will need to sign an NDA to see the project name and details. See [Non-Disclosure Agreement (NDA) FAQ](https://support.procore.com/products/online/user-guide/project-level/bidding/non-disclosure-agreement-nda-faq "Non-Disclosure Agreement (NDA) FAQ") for more information.
       - Once enabled, you have the option to select the box next to **Show project name before NDA is signed**.
         - This allows bidders to see the project name before they sign the NDA. All other project details will be hidden.
       - Click **Upload File**to upload your NDA file. Only 1 file can be added to this section.
     - **Public Discovery:**Select the box to enable public discovery.
       - Once enabled your bid package will be listed on the Procore Construction Network, making it searchable to thousands of external vendors. See [Enable Public Discovery](https://support.procore.com/products/online/user-guide/project-level/bidding/tutorials/enable-public-discovery "Enable Public Discovery") for more information.
       - **Procore Construction Network Project Details:** Complete the fields below to help subcontractors find your project on the network.
         - **Trades and Services**
         - **Business Classifications**
         - **Funding Type**
         - Check the **Location Visibility for NDA Projects**box to allow city and state to appear in public search results for NDA projects. Full address will not be shown.

### Attach Bid Documents

##### Important

Bid packages containing more than 100,000 files may lead to degraded application performance.

**Note:**We recommend creating a designated folder in the project's Documents tool to upload bid documents to. See [Create a Folder](https://support.procore.com/products/online/user-guide/project-level/documents/tutorials/create-a-new-folder-in-the-project-level-documents-tool "(missing link) Create a Folder in the Documents Tool"). You can create unlimited subfolders for each bid package and upload the relevant documents into each area. See [Upload Bid Documents](https://support.procore.com/products/online/user-guide/project-level/bidding/tutorials/upload-bid-documents "Upload Bid Documents") or [Upload Files or Folders to the Project Level Documents Tool](https://support.procore.com/products/online/user-guide/project-level/documents/tutorials/upload-files-or-folders-to-the-project-level-documents-tool "Upload Files or Folders to the Project Level Documents Tool").

1. On the Attach Files page, add files from the following tools as necessary.
   - **Drawings**
   - **Documents**
   - **Specifications**
   - ##### Regional Availability

     The Document Management tool is available in select countries. It is not yet available for Procore accounts in the U.S. To learn more, please reach out to your Procore point of contact.

     - ****Document Management****
2. Click **Attach Files**.

## Next Steps

- Create a bid form before you can add bidders. See [Create a Bid Form](https://support.procore.com/products/online/user-guide/project-level/bidding/tutorials/create-a-bid-form "Create a Bid Form (Beta)") and [Add Bidders to a Bid Form](https://support.procore.com/products/online/user-guide/project-level/bidding/tutorials/add-bidders-to-a-bid-form "Add Bidders to a Bid Form (Beta)").

## See Also

- [Add Notes to the Bid List](https://preview.support.procore.com/product-manuals/bidding-project/tutorials/add-notes-to-the-bid-list)
- [View a Bid Package](https://preview.support.procore.com/product-manuals/bidding-project/tutorials/view-a-bid-package)
- [Edit a Bid Package](https://preview.support.procore.com/product-manuals/bidding-project/tutorials/edit-a-bid-package)