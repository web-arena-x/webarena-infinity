# Revise & Resubmit a Subcontractor Invoice as an Invoice Contact

Source: https://v2.support.procore.com/product-manuals/invoicing-project/tutorials/revise-and-resubmit-a-subcontractor-invoice-as-an-invoice-contact

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

After an invoice contact submits a subcontractor invoice to the upstream contractor for payment, an [invoice administrator](/glossary-of-terms) reviews the invoice to approve or reject the payment. See [Review a Subcontractor Invoice as an Invoice Administrator](/process-guides/invoice-administrator-guide/review--approve-invoices). Once an invoice administrator rejects one (1) or more line item(2) on the invoice's Schedule of Values, its status changes to *Revise & Resubmit* and Procore sends an email notification to alert the invoice contact.

As an invoice contact, you can now review the rejected line item(s) and adjust the amount(s) on the item(s) as needed. To do this, the upstream collaborator must grant you sufficient access permissions. If you have been granted the required user permissions detailed below, one of the following marks appears in the corresponding 'Line Item Approval' column(s) on the invoice's 'Schedule of Values' card:

- A GREEN checkmark shows the line item is approved.
- A RED X shows the line item is rejected. A reason might appear in the 'Comment' column. A Comment is an optional entry for upstream collaborator's invoice administrator.

## Things to Consider

- **Required User Permissions:**

 - You must be an [invoice contact](/faq-what-is-an-invoice-contact) on the commitment.

## Prerequisites

- [Create a Subcontractor Invoice](/process-guides/invoice-administrator-guide/create-subcontractor-invoices)
- [Review a Subcontractor Invoice as an Invoice Administrator](/process-guides/invoice-administrator-guide/review--approve-invoices)

## Steps

1. Navigate to the project's **Commitments** tool.
2. Locate the commitment contract related to the invoice in the Commitments list.
3. Click the **Number** link to open the commitment contract.
4. Click the **Invoices** tab.
5. Look for the invoice in the *Revise and Resubmit* status.
6. Click the **Invoice #** link to open it.
7. In the invoice, click the **Edit** button.
8. Scroll down to the **Schedule of Values** card.
9. In the **Line Item Approval** column, identify which line items were approved or rejected by the invoice administrator:

   - A GREEN checkmark shows the line item is approved.
   - A RED X shows the line item is rejected. A reason might appear in the 'Comment' column.
10. *Optional:* If one (1) or more line item(s) were rejected, review the reason provided in the **Comment** column.

    ##### Â Note

    A 'Comment' entry is optional. If a reason is NOT provided and you have questions about the line item, contact your upstream collaborator's invoice administrator.

- Adjust the amounts in each rejected line item(s). See [Submit a New Subcontractor Invoice as an Invoice Contact](/product-manuals/invoicing-project/tutorials/create-a-new-subcontractor-invoice-as-an-invoice-contact).
- Choose one (1) of these options:

- **Cancel**. Click this link to cancel your data entry.
- **Save as Draft**. Click this button to save your data entry without sending the invoice to the invoice administrator for review. This action changes the status of the invoice from Re\_vise and Resubmit\_ to *Draft*.
- **Send**. Click this button to resubmit your invoice to the invoice administrator for review.