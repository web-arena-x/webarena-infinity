# Add Invoice Contacts to a Purchase Order or Subcontract

Source: https://v2.support.procore.com/product-manuals/invoicing-project/tutorials/add-invoice-contacts-to-a-purchase-order-or-subcontract

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

To provide [downstream collaborators](/faq-what-is-a-downstream-collaborator) with permissions to submit new subcontractor invoices in a Procore project, an invoice administrator must add an invoice contact to their commitment. If a collaborator has more than one commitment on your Procore project, administrators can add a different invoice contact to each commitment. Alternatively, your company's [Procore Administrator](/faq-what-is-a-company-admin) can [set a default invoice contact](/product-manuals/directory-company/tutorials/add-a-company-to-the-company-directory) in the downstream collaborator's company record.

## Things to Consider

- [Required User Permissions](/product-manuals/invoicing-project/permissions)
- **Additional Information:**

 - Subcontractor invoices originate in the Project level Commitments tool.

## Prerequisites

- Complete the steps in [How do I add invoice contacts to Procore?](/faq-what-is-an-invoice-contact)
- Create the commitment to which you want to add the invoice contact. See [Create a Commitment](https://support.procore.com/products/online/user-guide/project-level/commitments/tutorials/create-a-commitment).

## Steps

1. Navigate to the project's **Invoicing** tool.

   ##### Â Tip

   **You can also open a commitment from the Commitments tool.** To do this, navigate to the Project level **Commitments** tool. In the **Contracts** tab, click the **Number** link.

- Click the **Subcontractor** tab.
- Locate the invoice to update, and click its **Contract** link.   
   This opens the commitment. A subcontractor invoice originates from a commitment.
- In the commitment, click **Edit**.
- Under **General Information**, do the following:

 - **Contact Company**. Select the company record from the drop-down list.
 - **Invoice Contacts**. Select an employee of the company from the drop-down list.

    ##### Â Tips

    - **Don't see the right company in the 'Contact Company' list?** The company record must be added to the Project Directory. See [Add a Company to the Project Directory](/process-guides/set-up-a-project-directory/create-companies).
    - **Don't see the desired user in the list?** The user must ben an employee of the company record in the Project Directory. See [Add a User Account to the Project Directory](/product-manuals/directory-project/tutorials/add-user-account-to-project-directory).