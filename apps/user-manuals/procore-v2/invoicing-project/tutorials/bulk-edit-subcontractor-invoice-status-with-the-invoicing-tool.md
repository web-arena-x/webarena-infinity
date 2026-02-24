# Bulk Edit Subcontractor Invoice Status with the Invoicing Tool

Source: https://v2.support.procore.com/product-manuals/invoicing-project/tutorials/bulk-edit-subcontractor-invoice-status-with-the-invoicing-tool

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

Use the steps below to change the status of multiple subcontractor invoices at once.

## Things to Consider

- [Required User Permissions](/product-manuals/invoicing-project/permissions)
- You can edit subcontractor invoice status in bulk only with the Invoicing tool.

## Prerequisites

- [Create a Subcontractor Invoice](/process-guides/invoice-administrator-guide/create-subcontractor-invoices)

## Steps

1. Navigate to the project's **Invoicing** tool.
2. Click the **Subcontractor** tab.
3. Mark the checkboxes that correspond to the commitments with invoices:

   ##### Â Note

   To change the status of the selected invoices in bulk, each commitment that you select must have an invoice.

- To select all invoices, mark the checkbox that corresponds to the heading in the **Status** column. This selects all of the commitments in the list.
- To select individual invoices, mark the checkbox that corresponds to an commitment line item.

- Click **Edit**.
- Select the appropriate status from the **Select a Status** drop-down list.

 ##### Â Notes

 - To learn more about statuses, see [What are the default statuses for Procore invoices?](/faq-what-are-the-default-statuses-for-procore-invoices)
 - When creating an invoice (see [Create a Subcontractor Invoice](/process-guides/invoice-administrator-guide/create-subcontractor-invoices)), change the invoice's status to 'Under Review' when you are ready to send it to the [invoice administrator](/glossary-of-terms). The administrator can then change its status to 'Approved' as needed.
 - Users with 'Standard' level permissions can bulk edit invoices only when the invoice is in the 'Draft' or 'Revise & Resubmit' status.