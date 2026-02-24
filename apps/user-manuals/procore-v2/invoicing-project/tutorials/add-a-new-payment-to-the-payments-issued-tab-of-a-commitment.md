# Add a New Payment to the Payments Issued Tab of a Commitment

Source: https://v2.support.procore.com/product-manuals/invoicing-project/tutorials/add-a-new-payment-to-the-payments-issued-tab-of-a-commitment

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

To manually record any payments issued to the [downstream collaborator](/faq-what-is-a-downstream-collaborator) on a commitment, use the 'Payments Issued' tab on the commitment.

- #### For companies using Procore Pay: **Show/Hide** - To learn about the required settings to accurately track and manage joint check payments when using Procore Pay to pay subcontractor invoices, read [About Joint Checks with Procore Pay](https://support.procore.com/products/online/procore-pay/tutorials/about-joint-checks-with-procore-pay).

## Things to Consider

- [Required User Permissions](/product-manuals/invoicing-project/permissions)

## Prerequisites

- [Enable the Payments Issued Tab for Invoicing](/product-manuals/invoicing-project/tutorials/enable-the-payments-issued-tab-for-invoicing)

## Steps

1. Navigate to the project's **Invoicing** tool.

   ##### Â Tip

   **You can also open a commitment from the Commitments tool.** To do this, navigate to the Project level **Commitments** tool. In the **Contracts** tab, click the **Number** link.

- Click the **Subcontractor** tab.
- Locate the contract or invoice for the new payment record.
- Choose from these options to open the commitment.

 - **Contract**. Click the **Contract** link to open the commitment.
 - **Invoice #**. Click the **Invoice #** link and then click the **Contract #** breadcrumb link.
- In the commitment, click the **Payments Issued** tab.
- Click **Add Payment**.
- In the Add Payment prompt, enter:

 - **Invoice.** Select an existing invoice from the drop-down that the issued payment is attached to.
 - **Payment #.** Enter the related payment number for the issued payment.
 - **Payment** **Method.** Select a payment method from the drop-down list: *Check*, *Credit Card*, and *Electronic*.
 - **Amount.** Enter the amount of the payment.
 - **Date.** Enter the issue date for the payment
 - **Invoice #.** Enter the related invoice number for the payment issued.
 - **Check #.** Enter the related check number for the payment issued.
 - **Notes.** Enter any additional notes regarding the issued payment for record purposes.
 - **Attachments.** Attach any relevant files or documents.
- Click **Add**.