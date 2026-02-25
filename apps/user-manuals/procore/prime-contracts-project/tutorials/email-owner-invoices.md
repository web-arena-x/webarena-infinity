# Email Owner Invoices

Source: https://v2.support.procore.com/product-manuals/prime-contracts-project/tutorials/email-owner-invoices

---

##### Using Owner or Specialty Contractor Terminology?

Procore can be configured to use terminology specific to General Contractors, Owners, or Specialty Contractors. Learn [how to apply the dictionary options.](/faq-what-tool-names-and-terms-are-different-in-procore-for-general-contractors-owners-and-specialty-contractors)

- To learn the differences: **Show/Hide**

  - This table shows the differences in tool names (**bold**) and terms across the point-of-view dictionaries for Project Financials.

    | **General Contractors  English (United States) - Default** | **Owners** ***English (Owner Terminology V2)*** | **Specialty Contractors** ***English (Specialty Contractor Terminology)*** |
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

You can create an owner invoice that bills against a prime contract and then email it to your recipients. If you need to send your invoice to the project owner, this method allows them to view the invoice in your Procore (only they have a Procore user account and you've granted the user access). This proves useful when you want to capture the owner's written approval or rejection reason in writing. Procore automatically stores all replies from recipients in the 'From' address of your outgoing message in the Emails tab of the invoice.

## Things to Consider

- [Required User Permissions](/product-manuals/prime-contracts-project/permissions)
- **Additional Information:**

  - Clicking the **Email Invoice** button sends a copy of the invoice's 'Detail' tab to the designated recipients.

## Prerequisites

- [Create Owner Invoices](/product-manuals/prime-contracts-project/tutorials/create-owner-invoices)

## Steps

1. Navigate to the Project level **Invoicing** tool.
2. Click the **Owner** tab.
3. Locate the invoice to send by email.
4. Click the **Invoice #** link to open it.
5. Click the **Emails** tab.
6. Click **Compose Email**.   
    This opens the Compose New Email page.
7. Complete the following fields:

   - **Private**. Mark this checkbox to make the email private. Private emails are only shared with the recipient(s) and the sender.
   - **To**. Type to search the Project Directory for a list of matching recipient(s).
   - **CC**. Type to search the Project Directory for a list of matching recipient(s) to carbon copy. Your name appears here by default.
   - **BCC**. Type to search the Project Directory for a list of matching recipient(s) to carbon copy.
   - **Subject**. This field will populate with the number of the invoice. The subject line is added automatically. You can change it if you want.
   - **Message**. Type the body of your email message.
   - **Attachments**. Attach any related documents or files.
8. Click **Send**.  
    A YELLOW 'Communication Created' banner appears to confirm the outgoing message has been created and added to Procore's outgoing email queue.

   ##### Â Note

   - A record of your outgoing message is saved in the 'Emails' tab on the invoice.
   - Any messages sent to the 'From' address on your outgoing message are automatically saved in the invoice's 'Emails' tab. This provides your message recipients with the convenience to use the reply feature in their email program. It also captures your collaborator's approve or reject responses in writing.