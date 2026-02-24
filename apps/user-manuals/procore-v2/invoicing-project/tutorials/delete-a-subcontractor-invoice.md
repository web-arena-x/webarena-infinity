# Delete a Subcontractor Invoice

Source: https://v2.support.procore.com/product-manuals/invoicing-project/tutorials/delete-a-subcontractor-invoice

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

You can only delete the most recent subcontractor invoice on a commitment. Procore records delete actions in the 'Change History' tab of a commitment. Once deleted, the invoice is permanently removed and its data is irretrievable.

## Things to Consider

- [Required User Permissions](/product-manuals/invoicing-project/permissions)
- **Additional Information**:

 - You can only delete the most recent subcontractor invoice on a commitment.
- For companies using the ERP Integrations tool: **Show/Hide**

 - Before you can delete a subcontractor invoice that has been synced with an integrated ERP system, you will first need to unlink the synced invoice:
 - [Unlink Subcontractor Invoices Synced with ERP](/product-manuals/erp-integrations-company/tutorials/unlink-subcontractor-invoices-synced-with-erp)

## Prerequisites

- [Create a Subcontractor Invoice](/process-guides/invoice-administrator-guide/create-subcontractor-invoices)

## Steps

1. Navigate to the Project level **Invoicing** tool.
2. Click the **Subcontractor** tab.
3. Locate the invoice and click its **Contract** link.   
    This opens the commitment in the Project level **Commitments** tool.

   ##### Â Tip

   **You can also open a commitment from the Commitments tool.** To do this, navigate to the Project level **Commitments** tool. In the **Contracts** tab, click the **Number** link.

- Choose from these options:

 - **To delete an invoice from the 'Invoice' tab in the commitment**:1. Click the **Invoices** tab.2. Hover your mouse cursor over the invoice row.3. Click the **Delete** icon.
 - **To delete an invoice from the commitment's 'Invoice (Requisition)' page:**1. Click the **Invoice #** link.2. Click the **Overflow** menu and choose **Delete** from the drop-down menu.