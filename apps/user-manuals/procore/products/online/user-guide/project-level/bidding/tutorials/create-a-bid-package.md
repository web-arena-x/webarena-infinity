# Create a Bid Package - Procore

Source: https://support.procore.com/products/online/user-guide/project-level/bidding/tutorials/create-a-bid-package

---

##### Legacy Content

If your project has been updated to [Bid Management Enhanced Experience](https://support.procore.com/products/online/user-guide/project-level/bidding/tutorials/about-bid-management-enhanced-experience "About Bid Management Enhanced Experience"), see [Create a Bid Package with Bid Management Enhanced Experience](https://support.procore.com/products/online/user-guide/project-level/bidding/tutorials/create-a-bid-package-bid-management-enhanced-experience "Create a Bid Package with Bid Management Enhanced Experience") for updated steps.

## Objective

To create a bid package in a project's Bidding tool.

## Background

Procore's Bidding tool allows companies to distribute bid documents, manage bid lists, and invite bidders via email. Once invited, bidders can log in to Procore to retrieve bid documents and submit their bid.

## Things to Consider

- **Required User Permissions:**
  - 'Admin' level permissions on the project's Bidding tool.
- **Additional Information:**
  - The project does not have to be in a Bidding stage to create a bid package.
  - 'Admin' level permissions are required in order to be assigned as a Primary Bidding Contact.

## Prerequisites

- Confirm default settings for bid packages in the Configure Settings tool. See [Configure Advanced Settings: Bidding](https://support.procore.com/products/online/user-guide/project-level/bidding/tutorials/configure-advanced-settings-bidding "Configure Advanced Settings: Bidding").

## Video

|  |
| --- |
|  |

## Steps

1. Navigate to the project's **Bidding** tool.
2. Click **Create Bid Package**.
3. Enter the following information:  
   *Note:* Required fields are indicated by an asterisk (\*).
   - **General Information**:
     - **Title of Package**\*: Enter a title for your bid package. This will show up on the Bidding tool’s list page and in the email that your subcontractors will receive.
     - **Number**: Enter a number for your bid package. If you have existing bid packages, this field will populate with the next number in the sequence.
     - **Status**: Select 'Open' if the bid package is still in progress. Select 'Closed' if the bid has been awarded and closed. Once a bid is 'Closed', bidders will be unable to see the bid information.
     - **Bid Due Date**\*: Set the date and time when this bid will be due. If you receive authorization to extend the bid, you'll have to change the Bid Due Date to reflect this; otherwise, bidders may not be able to enter their amounts if they're attempting to enter their quotes after the initial bid due date. You may enable the option to allow bid submissions after the due date. See [Configure Advanced Settings: Bidding](https://support.procore.com/products/online/user-guide/project-level/bidding/tutorials/configure-advanced-settings-bidding "Configure Advanced Settings: Bidding") for more information. This will appear on the invitation email your subcontractors will receive.  
       *Note:* You can check the 'To be determined' checkbox if the bid due date is undetermined.
   - **Package Contacts**:
     - **Primary Bidding Contact**\*: Specify a primary contact from whose name you want the bid invitation to be sent.  
       *Note:* The primary contact's name will show on the bid invitation and any correspondence as well as receive all bid emails instead of the bid package creator.
     - **Bidding CC Group**: Add members to this list who will be notified when bids are submitted.
   - **Project Description**: Enter a description that will appear on the invitation email that is sent to invited bidders.  
     *Note:* You can set a default for this field in the Company Admin tool to have them populate each time you create a bid package. See [Set the Default Company Bidding Configuration](https://support.procore.com/products/online/user-guide/company-level/admin/tutorials/set-the-default-company-bidding-configuration "Set the Default Company Bidding Configuration").
   - **Bidding Instructions**: Enter instructions that will show on the Bid Sheet and include a link to Procore's Bidding Support page to provide bidders with quick access on how to download bid documents.  
     *Note:* You can set a default for this field in the Company Admin tool to have them populate each time you create a bid package. See [Set the Default Company Bidding Configuration](https://support.procore.com/products/online/user-guide/company-level/admin/tutorials/set-the-default-company-bidding-configuration "Set the Default Company Bidding Configuration").
   - **Pre-Bid Information**:
     - **RFI Deadline**: Click to enable a pre-bid RFI deadline.
       - Set a date and time.
     - **Site Walkthrough**: Click to enable pre-bid Walkthrough.
       - Set a date and time.
       - **Walkthrough Notes**: Enter any relevant information about the walkthrough.
   - **Advanced Settings**:
     - **Anticipated Award Date**: Set an anticipated award date for the package. This date will display on the Bid sheet.
     - **Countdown Email(s)**: Move the toggle on and enable daily countdown emails and enter the start date that is being sent to all bidders who have not declined to bid, starting at the specified number of days prior to the due date.
     - **Accept Submissions past Due Date**: Click if you would like to allow users to submit bid submissions after the specified due date.
     - **Enable Blind Bidding**: Click if you do not want to see any bid amounts or receive any notification emails when bids are placed until the due date. See [What is blind bidding?](https://support.procore.com/faq/what-is-blind-bidding "What is blind bidding?")
     - **Disable Electronic Submission of Bids**: Click on for projects that do not allow subcontractors to submit bids electronically.
     - **Include Bid Documents**: Click if you want to include the Bid documents as downloadable files in the Bid Package invitation email.
     - **Bid Submission Confirmation Message**: Enter a message that will be sent to bidders once they submit their bid.
     - *Note:* You can set a default for this field in the Company Admin tool to have them pre-populate each time you create a bid package. See [Set the Default Company Bidding Configuration](https://support.procore.com/products/online/user-guide/company-level/admin/tutorials/set-the-default-company-bidding-configuration "Set the Default Company Bidding Configuration").
4. Click **Create Bid Package.**
5. See the 'Attach Bid Documents' section below if you want to attach files to the bid package.

### Attach Bid Documents

##### Important

Bid packages containing more than 100,000 files may lead to degraded application performance.

*Note:* We recommend creating a designated folder in the project's Documents tool to upload bid documents to (for example, 'Bid Documents'). See [Create a Folder](https://support.procore.com/products/online/user-guide/project-level/documents/tutorials/create-a-new-folder-in-the-project-level-documents-tool "(missing link) Create a Folder in the Documents Tool"). You can create unlimited subfolders for each bid package and upload the relevant documents into each area. See [Upload Bid Documents](https://support.procore.com/products/online/user-guide/project-level/bidding/tutorials/upload-bid-documents "Upload Bid Documents") or [Upload Files or Folders to the Project Level Documents Tool](https://support.procore.com/products/online/user-guide/project-level/documents/tutorials/upload-files-or-folders-to-the-project-level-documents-tool "Upload Files or Folders to the Project Level Documents Tool").

1. On the Attach Files page, add files from the following tools as necessary.
   - **Drawings**:
     1. Click **Drawings**.
     2. Select **Current** or **Drawing Sets**.
     3. Mark the checkbox next to the drawings that you want to attach.  
        *Notes:* 
        - If you have Drawing Areas enabled, you can only select drawings from one Drawing Area at a time. See [Enable or Disable Drawings Areas](https://support.procore.com/products/online/user-guide/project-level/drawings/tutorials/enable-or-disable-drawing-areas "Enable or Disable Drawing Areas") for more information.
        - You can change the view to either List View or Thumbnail View when selecting drawings.
        - You can filter drawings by Set, Discipline, or Keyword Search.
   - **Documents**:
     1. Click **Documents**.
     2. Mark the checkbox next to the files and folders that you want to include in the bid package.
   - **Specifications**:
     1. Click **Specifications**.
     2. Click **Current Specs** or **Spec Sets.**
     3. Mark the checkbox next to the Specifications folders or individual specifications that you want to attach.  
        *Note:* If the Specifications tool is enabled on the project, the selections in this menu are populated with the spec sections from that tool, and it will display as a link upon saving the bid package. If the Specifications tool is disabled on the project, the selections in this menu are populated with values from the project's Admin tool.
2. Click **Attach Files**.

### Add Bidders

1. Click **Add Bidders**.  
   This directs you to the Bidders tab of the bid package.
2. Select your bidders from the following ways:
   - Search and filter for bidders you want to be added to the bid package. See [Search for Bidders](https://support.procore.com/products/online/user-guide/project-level/bidding/tutorials/search-for-and-invite-bidders "Search for and Invite Bidders") for more information.
   - Add new specialty contractors, vendors, and contacts to your Company Directory. See [Add New Companies and Contacts to the Company Directory from the Bidding Tool](https://support.procore.com/products/online/user-guide/project-level/bidding/tutorials/add-new-companies-and-contacts-to-the-company-directory-from-the-bidding-tool "Add New Companies and Contacts to the Company Directory from the Bidding Tool") for more information.

## Next Steps

- For projects with [Bid Management Enhanced Experience](https://support.procore.com/products/online/user-guide/project-level/bidding/tutorials/about-bid-management-enhanced-experience "About Bid Management Enhanced Experience"), see [Create a Bid Form](https://support.procore.com/products/online/user-guide/project-level/bidding/tutorials/create-a-bid-form "Create a Bid Form (Beta)").
- For projects with the Legacy experience, see [Invite Bidders](search-for-and-invite-bidders.md#Invite_Bidders "Search for and Invite Bidders").

## See Also

- [Edit a Bid Package](https://support.procore.com/products/online/user-guide/project-level/bidding/tutorials/edit-a-bid-package "Edit a Bid Package")
- [Create a Bid Form](https://support.procore.com/products/online/user-guide/project-level/bidding/tutorials/create-a-bid-form "Create a Bid Form (Beta)")