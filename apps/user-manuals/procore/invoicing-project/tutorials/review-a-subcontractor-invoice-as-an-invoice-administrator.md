# Review a Subcontractor Invoice as an Invoice Administrator

Source: https://v2.support.procore.com/product-manuals/invoicing-project/tutorials/review-a-subcontractor-invoice-as-an-invoice-administrator

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

Automated Commitment Invoice Numbering allows companies to define a company-level numbering scheme for all newly created Commitment/Subcontractor Invoices. This automation reduces manual entry, ensures consistency, and streamlines financial operations across all invoices.

## Things to Consider

- [Required User Permissions](/product-manuals/invoicing-project/permissions)

 - 'Admin' level permissions on the **Company level** Admin tool.
- **Additional Information:**

 - This process allows you to access the Invoicing toolâs settings page.
 - You will be modifying the company-level configuration for invoice numbering.

## Prerequisites

- [Create a Subcontractor Invoice](/process-guides/invoice-administrator-guide/create-subcontractor-invoices)
- The invoice must be in the 'Under Review' status.

## Steps

1. Log in to your Procore account with Admin permissions.
2. Navigate to **Admin** tool.
3. Under **Tool Settings.** click **Invoicing**.
4. In the Invoicing settings, click the **Settings** tab.
5. Under the **Subcontractor Invoicing** section, find the **Invoice Numbering** setting and **Format Preview** panel.
6. Click **Edit** to open the **Invoice Number Format**.
7. Preview the Invoice Number. Use **Preview** to verify the format. The number appears in sequential order in the preview based on the starting value.
8. Configure the Invoice number format by adding and arranging the required components in the desired order, using the first or last five characters of each component. Select the components you want to include in your invoice numbers. The options include:

   - **Invoice Position** - You cannot delete the position number.
   - **Commitment Number** -Â  Uses the commitment number.
   - **Billing Period** - Uses the billing period.
   - **Billing Period End Date** - Uses the Invoice billing end date.
   - **Billing Period Number** - Uses the Invoice billing period number.
   - **Custom Text** - Type any fixed text ( For example, INV, BILL or Code).
   - **Retainage Conditional** - Will be based on the selected property format.
   - **Project Number** - Uses the Project number.
9. Configure component separator to define how each component is separated. Select the **Component Separator** from the drop-down list.

   - Dash (-)
   - Point (.)
   - Forward slash (/)
   - Underscore (\_)
   - None
10. Configure the characters for each component. Select the components you want to include in your invoice numbers. Options may include:

    - FormatÂ
    - LengthÂ

      - Invoice Position
      - Characters

    *Note: Arrange the components and set formatting options as desired.*
11. The system will validate the total character count for the invoice number.

    - *Note: If your ERP system specifies a maximum character count, Procore will enforce it. Otherwise, the default limit is 100 characters.*
12. Review the format preview to ensure it meets your requirements.
13. Click **Save** to apply the numbering scheme. 
    Note:

    - *Invoice numbers for these invoices will be auto-generated and non-editable.*
    - *The new numbering scheme will now be enforced for all newly created Commitment/Subcontractor Invoices.*

## Next Step

- [Revise & Resubmit a Subcontractor Invoice as an Invoice Contact](/product-manuals/invoicing-project/tutorials/revise-and-resubmit-a-subcontractor-invoice-as-an-invoice-contact)