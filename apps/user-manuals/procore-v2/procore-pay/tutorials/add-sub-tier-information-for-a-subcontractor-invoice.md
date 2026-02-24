# Add Sub-Tier Subcontractor Information to a Subcontractor Invoice

Source: https://v2.support.procore.com/product-manuals/procore-pay/tutorials/add-sub-tier-information-for-a-subcontractor-invoice

---

##### Â General Availability in Select Markets (United States)

[Procore Pay](https://www.procore.com/pay)  is available in the United States. It is designed for General Contractors and Owner-Builders who act as their own General Contractors on a job. Procore Pay extends the [Invoice Management](https://www.procore.com/invoice-management) functionality in the Procore web application to handle the payment process between general and specialty contractors.

## Background

General Contractors (i.e., payors) must report all project participants to property owners, including all sub-tier subcontractors who provide services or supplies for a construction project. As an invoice contact for a Specialty Contractor, one of your roles is to add your sub-tier subcontractor's information on the invoices you submit.

You can add multiple levels of sub-tier subcontractors on an invoice and enter the 'Amount Billed' for each. To limit repetitive data entry, this sub-tier subcontractor information carries over to future invoices, showing a $0.00 balance on the next invoice. You can also update the amount for active sub-tiers.

Users can add up to 100 sub-tiers per invoice, with up to five (5) nested levels per tier. Keep in mind that when adding nested sub-tier subcontractors, Procore restricts subcontractors from hiring themselves. In addition, you can only add or change sub-tier details on invoices in the *Draft* or *Revise & Resubmit* status. Once added to an invoice, you are not permitted to edit the sub-tier subcontractor information. If you make a data entry error, contact your General Contractor, who can edit the information in the project's commitment.

## Things to Consider

- [Required User Permissions](/product-manuals/procore-pay/permissions)
- **Additional Information**:

  - Users can add up to one hundred (100) first-level sub-tier subcontractor entries to a commitment. Each first-level sub-tier subcontractor can have up to five (5) nested sub-tier subcontractors. An error message appears if a user attempts to add a sixth tier.
  - Sub-tier subcontractors and nested sub-tiers can be added or edited on a commitment at any time. On subcontractor invoices, they can only be edited when the invoice is in the *Revise & Resubmit* or *Draft* status.
  - [Invoice administrators](/process-guides/payor-setup-guide/add-invoice-administrators) for the payor can also add sub-tier subcontractor information to a commitment. See [Add Sub-Tier Subcontractor Information to a Commitment](/product-manuals/procore-pay/tutorials/add-sub-tier-subcontractor-information-to-commitments).
  - To learn about sub-tier subcontractors, see [What is a sub-tier subcontractor?](/process-guides/invoice-administrator-guide/what-is-a-sub-tier-subcontractor)

## Prerequisites

- [Enable Lien Waivers in the Company Payments Tool](/process-guides/payor-setup-guide/enable-lien-waivers)
- [Enable Lien Waivers & Set Default Templates on Projects](/process-guides/payor-setup-guide/enable-templates-on-projects)
- [Enable Sub-Tier Waivers on Project Invoices as an Invoice Administrator](/process-guides/payor-setup-guide/enable-sub-tier-waivers)
- [Create a Subcontractor Invoice](/process-guides/invoice-administrator-guide/create-subcontractor-invoices)

## Steps

1. Navigate to the Project level **Invoicing** tool.
2. Click the **Subcontractor** tab to view a list of the project's subcontractor invoices.
3. Locate the invoice and click its **Invoice #** link to open it.
4. In the invoice, click the **Lien Rights** tab.
5. Scroll to the **Sub-Tier Waivers** card for this invoice.

   ##### Â Note

   The invoice may include one or more sub-tier waiver cards based on the project's configuration settings for waiver collection. See [Enable Sub-Tier Waivers on Subcontractor Invoices as an Invoice Administrator](/process-guides/payor-setup-guide/enable-sub-tier-waivers).

- Choose from these options:

  - Add Sub-Tiers
  - Certify No Sub-Tiers

### Add Sub-Tiers

To provide a complete list of everyone working on a project:

1. Scroll to the desired sub-tier card in the invoice and click **Edit**.  
      
    This places the selected card into editing mode.
2. Click **Add Sub-Tier** at the bottom of the data table, and click **Create New**.  
      
      
    This opens the **Add Sub-Tier** panel.
3. Enter the following information in the line item:

   ##### Â Note

   An asterisk (\*) below denotes a required field.