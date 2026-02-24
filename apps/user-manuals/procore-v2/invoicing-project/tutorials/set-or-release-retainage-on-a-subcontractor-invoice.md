# Set or Release Retainage on a Subcontractor Invoice

Source: https://v2.support.procore.com/product-manuals/invoicing-project/tutorials/set-or-release-retainage-on-a-subcontractor-invoice

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

In Procore, the term *Retainage* refers to the practice of withholding of a portion of a contract amount until the work is deemed satisfactorily complete. The withheld amount is specified in an agreement between the contracting party (the party paying for the work) and a contracted party (the person or company performing the work). A common practice is to withhold 5-10% of a contract's total value until a milestone is reached. Then, the withheld amount can be released as a progress payment. When work is substantially complete, the withheld amount can be released as a final payment.

## Things to Consider

- **Required User Permissions:**

 - *To set and release retainage when editing the most recent invoice before, during, or after the billing period's 'Due Date':*

    - You must be an [invoice administrator](/process-guides/payor-setup-guide/add-invoice-administrators).
 - *To release retainage when editing the most recent invoice during the current billing period:*

    - Ensure the Invoice type includes retainage. To know more, [Configure Settings: Invoicing](/product-manuals/invoicing-project/tutorials/configure-settings-invoicing)
    - You must have 'Standard' level permissions on the Project level Commitments tool.   
      AND
    - You must be added to the 'Private' drop-down list on the commitment.
 - Read about required user permissions for downstream collaborators: **Show** **/Hide**

    - Some Procore customers choose to provide their [downstream collaborators](/faq-what-is-a-downstream-collaborator) with access to the Project level Commitments tool:
    - *To modify retainage amounts on the most recent invoice before the billing period's 'Due Date'*:

      - You must be an [invoice contact](/faq-what-is-an-invoice-contact) on the commitment.   
         AND
      - You must have 'Read Only' level permissions on the Project level Commitments tool.
- **Additional Information:**

 - If there are multiple invoices for a single billing period, you can only edit the billed amounts on the most recent invoice.
 - If you are adding a payment schedule after the invoice is approved, enter the amount for the work you are claiming this period in the 'Proposed Amount' column of the invoice detail. To learn more, see [Create a Payment Schedule](/product-manuals/invoicing-project/tutorials/create-a-payment-schedule).
 - You can also manage withholding using the sliding scale retention feature. To learn more, see [What is sliding scale retention?](/faq-what-is-sliding-scale-retention)

## Prerequisites

- [Create a Subcontract](/product-manuals/commitments-project/tutorials/create-a-subcontract)
- [Enable Retainage on a Purchase Order or Subcontract](/product-manuals/commitments-project/tutorials/enable-retainage-on-a-purchase-order-or-subcontract)
- [Create a Subcontractor Invoice](/process-guides/invoice-administrator-guide/create-subcontractor-invoices)

## Steps

- Edit the Schedule of Values
- Set Retainage on Line Items
- Release Retainage on Line Items

### Edit the Schedule of Values

1. Navigate to the project's **Commitment** tool.
2. Go to Commitment for the invoice you want to distribute.
3. Click the **Invoicing** tab
4. In the table, locate the invoice to edit.
5. Click the **Invoice #** link to open it.
6. Scroll to the **Schedule of Values**.
7. Click **Edit**.

### Set Retainage on Line Items

To set retainage on invoice line items:

1. In the **General** tab of the invoice, scroll to the **Schedule of Values**.
2. In the **Schedule of Values**, locate the line item(s) to modify and scroll to the right of the page to view the retainage columns.
3. Choose one (1) of these options:

   - Enter an amount to withhold for the line item the **Work Retainage this Period ($)** column. Procore automatically calculates the entry in the **Work Retainage (%)** column.   
     OR
   - Enter a percentage amount to withhold for the line item in the **Work Retainage (%)** column. Procore automatically calculates the entry in the **Work Retainage ($)** column.

     ##### Examples

     - When you enter a currency amount in the **Work Retainage this Period ($)** column, Procore calculates the entry in the **Work Retainage (%)** column. For example, if you enter $1,250.00 on line item 1, Procore calculates the Work Retainage this Period (%) as 5%.
     - When you enter a percentage amount in the **Work Retainage this Period (%)** column, Procore calculates the entry in the **Work Retainage this Period ($)** column. For example, if you enter 5% on line item 2, Proore calculates the Work Retainage this period as $625.00.

- Update the amount of retainage to release in each line item on the invoice as needed.
- Click **Save**.

### Release Retainage on Line Items

To release retainage on invoice line items:

1. In the **General** tab of the invoice, scroll to the **Schedule of Values**.
2. In the **Schedule of Values**, locate the line item(s) to modify and scroll to the right of the page to view the retainage columns.
3. Enter the amount to release in the **Total Retainage Released** column.

   ##### Example

   Before data entry, the cumulative total amount withheld for each line item is shown in the **Total Retainage** column. In line item 1, the **Total Retainage** is $2,500.00. In line item 2, it is $1,250.00.

   Enter the amount of retainage to release:

   - To release all of the amount withheld, enter 100% of the Total Retainage value. In line item 1, enter $2,500.00 to release the entire amount.
   - To release half of the amount withheld, enter 50% of the Total Retainage value. In line item 2, enter $625.00 to release 50% of the $1250.00 amount.

   After data entry, Procore reduces the **Total Retainage** value by the amount of your data entry: