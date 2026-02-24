# Create a Record for a Payment Received

Source: https://v2.support.procore.com/product-manuals/invoicing-project/tutorials/create-a-record-for-a-payment-received

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

An owner invoice is an itemized record of a financial transaction between a project owner and a company responsible for completing work. Typically, it is issued by a general contractor and submitted to a project owner to signal that payment is due for completed work. When you receive a payment from an owner, you can create a record of that payment in Procore's Invoicing tool using the steps below.

## Things to Consider

- [Required User Permissions](/product-manuals/invoicing-project/permissions)

## Prerequisites

- The project's prime contract must be in the 'Approved' or 'Complete' status. See [Approve a Prime Contract](/product-manuals/prime-contracts-project/tutorials/approve-a-prime-contract).
- Create the invoice that you sent to the owner. See [Create Owner Invoices](/product-manuals/prime-contracts-project/tutorials/create-owner-invoices).

## Steps

1. Navigate to the project's **Invoicing** tool.
2. Click the Owner tab.
3. Locate the owner invoice in the list. The click to open it.
4. Click **Create Payment**.
5. Complete the following fields:

   - **Invoice**. Select the associated invoice from the drop-down list.
   - **Date**. Select a date that the payment was received.
   - **Payment #**. Enter the payment number.
   - **Invoice #**. Enter the invoice number for the payment, if applicable.
   - **Check #**: Enter the check number for the payment.
   - **Notes**. Include any additional notes to provide details about the payment.
   - **Amount**. Enter the amount of the payment received.
   - **Attachments**. Include any attachments related to the payment. For example, you might want to attach the check image or the invoice file.
6. Click **Add**. The payment is listed under the 'Contract Summary Report' section in the 'Payments Received' column.
7. Click **Save**.

   ##### Â Notes

   - You will see a list of all payments received, which you can then export to a PDF by choosing **Export > PDF**.
   - All payments received on the project are tracked in the Contract Summary Report in the Prime Contract tool's General tab (see illustration below).