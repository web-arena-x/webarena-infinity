# Compile Subcontractor Invoice Backups with the Invoicing Tool

Source: https://v2.support.procore.com/product-manuals/invoicing-project/tutorials/compile-subcontractor-invoice-backups-with-the-invoicing-tool

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

An *invoice backup* generates a PDF copy of a contract's subcontractor invoices and includes them in the backup file as PDF attachments. Users can compile backups in bulk, saving time and eliminating the need to export multiple invoices and manually combine files. Backups can only be compiled from the Subcontractor tab of the Invoicing tool.

## Things to Consider

- [Required User Permissions](/product-manuals/invoicing-project/permissions)

 - With the Procore + DocuSignÂ© integration, Procore includes the signed DocuSignÂ© invoice once the signature workflow is complete.

## Prerequisites

- [Create a Subcontractor Invoice](/process-guides/invoice-administrator-guide/create-subcontractor-invoices)
- Place all previously invoiced billing periods for the contract(s) the *Closed* status. See [Edit Billing Periods](/product-manuals/invoicing-project/tutorials/edit-billing-periods). Never delete a billing period if its linked to an invoice.

## Steps

1. Navigate to the project's **Invoicing** tool.
2. Click the **Subcontractor** tab.
3. Mark the checkboxes for the contracts for which you want to compile invoice backup.

   ##### Â Note

   For a successful compile, place all of the contract's previously invoiced billing periods into the *Closed* status. See [Edit Billing Periods](/product-manuals/invoicing-project/tutorials/edit-billing-periods). Never delete billing period if its linked to an invoice.

- Click **Compile Invoice Backups**.

**For payors using Procore Pay, click here for additional steps.**

In the **Compile** window that appears for Procore Pay, mark a check box to include the item. Remove a mark to exclude it.

- **All**. The files attached to the **Attachments** card of the invoice.
- **Cover Sheet.** A cover sheet for the backup file.
- **Attachments**. The files added to the Attachments card of the invoices.
- **First-Tier Waivers**. The *Conditional* and/or *Unconditional* first-tier lien waivers. If you don't see this option, enable first-tier lien waivers on the project. See [Enable Lien Waivers & Set Default Templates on Projects](/process-guides/payor-setup-guide/enable-templates-on-projects).
- **Sub-Tier Waivers**. The lien waivers added for any sub-tier subcontractors. If you don't see this option, enable sub-tier waivers on the project. See [Enable Sub-Tier Waivers on Subcontractor Invoices as an Invoice Administrator](/process-guides/payor-setup-guide/enable-sub-tier-waivers).

1. Click **Compile**.

##### Example

This is an example of the email with the downloadable file link. For ease of identification, Proocore names the file: Subcontractor invoice backup - [project name] - [project number] - [date] - [time].pdf

When compiling the PDF to include in a backup, Procore organizes invoices by 'Contract #' in ascending order, and applies the 'Invoice Position' number as the secondary sort order. This ensures invoices are clearly presented in logical order in the backup file.