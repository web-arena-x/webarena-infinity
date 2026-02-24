# Export Owner Invoices

Source: https://v2.support.procore.com/product-manuals/prime-contracts-project/tutorials/export-owner-invoices

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

You can export an owner invoice to the CSV or PDF file format. You also have the option to download the invoice and any attachments to a PDF file.

## Things to Consider

- **Required User Permissions:**

  - **Admin** level permissions to the Project level Prime Contracts tool.
- **Supported File Formats:**

  - CSV
  - PDF
  - PDF with Attachments
- **Limitations:**

  - The **PDF with Attachments** option is not available when using Procore with **DocuSignÂ©.**

## Prerequisites

- [Create Owner Invoices](/product-manuals/prime-contracts-project/tutorials/create-owner-invoices)

## Steps

1. Navigate to the project's **Prime Contracts** tool.
2. Locate the contract to open.

   ##### Â Tip

   **How to find a contract?** Use the **Search** and **Select a Column to Group** features to quickly find the contract.

- Click the appropriate **Number** link to open the contract.
- Click the **Invoices** tab.
- Locate the invoice to open in the **Invoices (Payment Applications)** tab.
- Click the **Invoice #** link to open it.
- Scroll to the **Schedule of Values** card and select the desired option from the **Column View When Exported** drop-down list:

  - **Industry Standard**. This is the default column layout for an owner invoice's Schedule of Values.
  - **Current Configuration**. If you have customized the column layout of your schedule of values, choose this option to select your custom view before proceeding with the export.

    ##### Â Tip

    **Do you want your PDF export file to show which change orders are being billed against?** Apply the *Prime Contract Change Order*, *Potential Change Order*, or *Change Order Request* options in the **Select Groups to Display** menu at the top of the invoice's Schedule of Values. Procore will include both the change order number and complete title of those items in the PDF.