# Create a Subcontractor Schedule of Values (SSOV)

Source: https://v2.support.procore.com/product-manuals/invoicing-project/tutorials/create-a-subcontractor-schedule-of-values-ssov

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

In the same way that you can invite an [invoice contact](/glossary-of-terms) to submit a [subcontractor invoice](/glossary-of-terms) for review, you can also invite an invoice contact to provide a more detailed breakdown of line items on the 'Schedule of Values' tab by enabling the 'Subcontractor SOV' tab on a commitment.

- On the general 'Schedule of Values' tab for a commitment, each line item is assigned to a specific cost code and cost type.
- On the 'Subcontractor SOV' tab on a commitment, you may be asked to provide a more detailed breakdown of a line item on the 'Schedule of Values' tab. This may be required to provide a more full explanation about the amounts to obtain approval on an invoice.

## Things to Consider

- [Required User Permissions](/product-manuals/invoicing-project/permissions)
- **Limitations:**

 - If a commitment is using the Unit/Quantity Based accounting method, adding the Subcontractor SOV is not supported. See [How do I set the accounting method for a contract or funding?](/faq-how-do-i-set-the-accounting-method-for-a-contract-or-funding)
- **Additional Information:**

 - On the purchase order's or subcontract's General tab, you must select your collaborator's user name in the 'Private' and 'Invoice Contact' fields before your collaborator can see the SOV.

    - Only the detail line items added on the Subcontractor SOV tab will carry over to the invoice.
    - For companies using the ERP Integrations tool, the Subcontractor SOV line items that you create do NOT sync with your integrated ERP system.

      ##### Â Tip

      **Are you creating a Subcontractor SOV for your downstream collaborator to update later?** If so, your company must provide the collaborator with a Procore user account in your Company Directory. In addition, that user must be granted the appropriate permissions for an invoice contact. To learn more, see [What is an invoice contact?](/faq-what-is-an-invoice-contact)