# Configure Settings: Invoicing

Source: https://v2.support.procore.com/product-manuals/invoicing-project/tutorials/configure-settings-invoicing

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

An [invoice administrator](/process-guides/payor-setup-guide/add-invoice-administrators) should configure the Invoicing tool settings before your team members create any invoices on a Procore project.

## Things to Consider

- [Required User Permissions](/product-manuals/invoicing-project/permissions)

## Steps

1. Navigate to the project's **Invoicing** tool.
2. Click **Configure Settings** .
3. Under **Settings**, configure the options.

### Default Billing Period

These settings populate the date fields in the 'Set Up Billing Period' prompt when users [Create Manual Billing Periods with the Invoicing Tool](/product-manuals/invoicing-project/tutorials/create-manual-billing-periods).

##### Â Tip

**Want to simplify billing period creation for future cycles?** An [invoice administrator](/process-guides/payor-setup-guide/add-invoice-administrators) can configure default billing period dates to preset the dates in the **From**, **To**, and **Due Date** fields in the 'Set Up Billing Period' prompt. See [Create Manual Billing](/product-manuals/invoicing-project/tutorials/create-manual-billing-periods) [Periods with the Invoicing Tool](/product-manuals/invoicing-project/tutorials/create-manual-billing-periods). If you don't complete this configuration, no preset dates show. Instead, you will see: mm/dd/yyyy

To configure the **Default Billing Period** settings:

1. Choose these dates:

   - **Start Date**. Accept the default start date of '1st of the month' or choose a different date. This populates the 'From' date in the prompt.
   - **End Date**. Accept the default end date of '31st of the month' or choose a different date. This populates the 'To' date in the prompt.
   - **Due Date**. Accept the default due date of '25th of the month' or choose a different date. This populates the 'Due Date' field in the prompt.
2. Select a **Subcontractor Default Invoice Type** option from the drop-down list:

   - **Work and Materials**. Allow invoice contacts to create invoices to bill for work and materials.
   - **Work, Materials & Retainage.** Allow invoice contacts to create invoices to bill for work, materials, and retainage release.
   - **None (must be invited to create an invoice)**. Only allow invoice contacts to create invoices after sending an 'Invite to Bill'.

     ##### Â Note

     The 'Invoice Type' is always set to 'Work, Materials & Retainage' when a user with 'Admin' level permissions on the Commitments tool creates a new invoice.