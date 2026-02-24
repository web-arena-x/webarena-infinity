# Forward a Subcontractor Invoice by Email

Source: https://v2.support.procore.com/product-manuals/invoicing-project/tutorials/forward-a-subcontractor-invoice-by-email

---

##### Using Owner or Specialty Contractor Terminology?

Procore can be configured to use terminology specific to General Contractors, Owners, or Specialty Contractors. Learn [how to apply the dictionary options.](/faq-what-tool-names-and-terms-are-different-in-procore-for-general-contractors-owners-and-specialty-contractors)

- To learn the differences: **Show/Hide**

 - This table shows the differences in tool names (**bold**) and terms across the point-of-view dictionaries for Project Financials.

    | **General Contractors English (United States) - Default** | **Owners** ***English (Owner Terminology V2)*** | **Specialty Contractors** ***English (Specialty Contractor Terminology)*** |
    | --- | --- | --- |
    | **Invoicing** | ***Invoicing*** | ***Progress Billings*** |
    | Owner | *Funding* | *Owner* |
    | Owner/Client | *Owner/Client* | *GC/Client* |
    | Prime Contract Change Order | *Funding Change Order* | *Client Contract Change Order* |
    | **Prime Contracts** | ***Funding*** | ***Client Contracts*** |
    | Revenue | *Funding* | *Revenue* |
    | Subcontract | *Contract* | *Subcontract* |
    | Subcontractor | *Contractor* | *Subcontractor* |
    | Subcontractor Schedule of Values (SSOV) | *Contractor Schedule of Values (CSOV)* | *Subcontractor Schedule of Values (SSOV)* |

    ##### About These Dictionaries

    - **Default Setting:** The 'General Contractor' dictionary is enabled by default for all accounts.
    - **Availability:** These alternate dictionaries in *italics* are available in US English only.

    ##### How to Switch Your Dictionary

    To change your company's terminology to the Owner or Specialty Contractor dictionary, contact your company's 

    A *Procore Administrator* is a user who has 'Admin' level permissions on all of the Company level Tools in Procore. Granting a user âAdminâ level permissions in the Company level Directory tool automatically assigns that user âAdminâ permissions on all Company level tools. Also called a *Company Administrator*.

    ProcoreÂ Administrator. They will work with your Procore Point of Contact to make the change.

## Background

Once an invoice is created, a Procore project user granted the required user permissions can forward an invoice to recipients. Recipients must have a user account in the Project Directory. An invoice administrator can also set up a 'Commitments Distribution' list for recipients in the project's Commitments tool. This automatically populates the 'To' field with distribution list members when sending a new email. You can add or remove recipients before sending the invoice.

## Things to Consider

- **Required User Permissions**:

 - You must be an [invoice administrator](/process-guides/payor-setup-guide/add-invoice-administrators). 
    OR
 - You must have 'Standard' level permissions on the project's Commitments tool. 
    AND You must be added to the 'Private' drop-down list on the commitment.

## Prerequisites

- [Create a Subcontractor Invoice](/process-guides/invoice-administrator-guide/create-subcontractor-invoices)
- [Add a User Account to the Project Directory](/product-manuals/directory-project/tutorials/add-user-account-to-project-directory)
- [Add an Existing User to Projects in Your Company's Procore Account](/product-manuals/directory-company/tutorials/add-an-existing-user-to-projects-in-your-companys-procore-account).

## Steps

1. Navigate to the project's **Commitment** tool.
2. Go to Commitment for the invoice you want to distribute.
3. Click the **Invoicing** tab
4. Locate the invoice to distribute and click its **Number** link.
5. In the invoice, click the **Emails** tab.
6. In the **Emails** tab, click **Email Invoice**.
7. In the Email pane, click **Email**.
8. Under the **Forward Invoice [Number] for Contract [Number - Date]** area:

   - **To**. Select recipient(s) from the drop-down list.

     ##### Â Tip

     **Need a default distribution list?** An invoice administrator can set up a 'Commitments Distribution' list in the project's Commitments tool. This auto-populates the 'To' field with list members when crafting a new email. See [Configure Settings: Commitments](/product-manuals/commitments-project/tutorials/configure-advanced-settings-commitments).

- **CC**. Select recipients from the drop-down list.
- **BCC**. Select recipients from the drop-down list.
- **Private**. Place a mark in the box to make the invoice 'Private' to recipients and administrators.
- **Subject**. Add a subject line for the commitment.
- **Attachments**. Attach any relevant files. You have these options:

 - Click **Attach File(s)** and select files from your computer. 
    OR
 - Use a drag-and-drop operation to move files from your computer into the Attachments area.
- **Message**. Type the message body in this box.
- Click **Send**.   
 Procore sends your email to the named recipients. A copy of the email and any replies are stored as a communication thread in the Emails tab of the invoice.