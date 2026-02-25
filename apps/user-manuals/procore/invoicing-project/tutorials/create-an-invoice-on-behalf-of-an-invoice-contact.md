# Create a Subcontractor Invoice on Behalf of an Invoice Contact

Source: https://v2.support.procore.com/product-manuals/invoicing-project/tutorials/create-an-invoice-on-behalf-of-an-invoice-contact

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

If your company or project doesn't want to grant external collaborators access permission to your Procore project so they can [submit their own invoices](/process-guides/payee-user-guide/submit-an-invoice), your team can collect the digital or paper invoices from your invoice contacts outside of Procore. Once collected, invoice administrators can create them in Procore on each invoice contact's behalf.

## Things to Consider

- [Required User Permissions](/product-manuals/invoicing-project/permissions)
- **Additional Information:**

 - An invoice administrator can:\* Create invoices for all of a project's commitments.\* Edit amounts on a Schedule of Values when the invoice is in the *Draft* or *Revise & Resubmit* status. When multiple invoices exist for one commitment during one billing period, you can only amounts on the latest invoice.\* For users legally required to provide claimants with a payment schedule, see [Export a Payment Schedule.](/process-guides/invoice-administrator-guide/create-subcontractor-invoices)\* Revise the 'Payment Due Date' on the invoice for Early Pay Programs.

## Prerequisites

To perform the Steps in this tutorial, the invoice's commitment must have:

- A subcontracting company assigned as the 'Contract Company'. See [Create a Commitment](https://support.procore.com/products/online/user-guide/project-level/commitments/tutorials/create-a-commitment).
- An employee of the 'Contract Company' assigned as the 'Invoice Contact'. See [Add Invoice Contacts to a Purchase Order or Subcontract](/process-guides/payor-setup-guide/add-invoice-contacts).
- A status of *Approved* or *Complete*. See [What are the default commitment statuses in Procore?](/faq-what-are-the-default-commitment-statuses-in-procore)
- All line items on the [Subcontractor Schedule of Values](/faq-what-is-a-subcontractor-schedule-of-values) must be in the *Approved* status. See [Review a Subcontractor Invoice as an Invoice Administrator](/process-guides/invoice-administrator-guide/review--approve-invoices). To learn how to enable the optional Subcontractor SOV tab, see [Add a Subcontractor SOV to a Commitment](/product-manuals/commitments-project/tutorials/add-a-subcontractor-sov-to-a-commitment).

In addition, an invoice administrator must create a billing period for the invoice. See [Manage Billing Periods](/product-manuals/invoicing-project/tutorials/manage-billing-periods).

## Steps

1. Open the New Invoice Page
2. Update the General Information Card
3. Update the Schedule of Values Card
4. Update the Payment Details Card
5. Add Attachments
6. Save the Invoice
7. *Optional:* Send an Invoice with DocuSignÂ©

### Open the New Invoice Page

Users always create invoices in the project's Commitments tool.

1. Navigate to the project's **Commitments** tool.
2. Find the commitment to create an invoice for in the 'Contracts' tab.
3. Click the **Number** link to open it.
4. At the top of the commitment, click **Create** and choose **Create Invoice** from the menu.

   ##### Â Tip

   **Is the 'Create Invoice' option inactive?** To learn why, hover your mouse cursor over the tooltip. This option only activates when Prerequisites are met.

 
   
 This opens the 'New Invoice for [Contract Number]' page so you can update the General Information card.

### Update the General Information Card

In the New Invoice page, update the **General Information** card. Once updated, continue by updating the Schedule of Values.

##### Â Note

The element circled in ORANGE is only available with [Procore Pay](https://support.procore.com/products/online/procore-pay).