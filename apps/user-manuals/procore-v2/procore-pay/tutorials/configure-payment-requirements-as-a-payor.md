# Configure Payment Requirements as a Payor

Source: https://v2.support.procore.com/product-manuals/procore-pay/tutorials/configure-payment-requirements-as-a-payor

---

##### Â General Availability in Select Markets (United States)

[Procore Pay](https://www.procore.com/pay)  is available in the United States. It is designed for General Contractors and Owner-Builders who act as their own General Contractors on a job. Procore Pay extends the [Invoice Management](https://www.procore.com/invoice-management) functionality in the Procore web application to handle the payment process between general and specialty contractors.

## Things to Consider

- [Required User Permissions](/product-manuals/procore-pay/permissions)
- **Additional Information**:

  - Who can view payment requirements and where you can view them depends on your role.

    - [View Payment Requirements as a Payor](/product-manuals/procore-pay/tutorials/view-payment-requirements-as-a-payor)
    - [View Payment Requirements as an Invoice Administrator](/product-manuals/procore-pay/tutorials/view-payment-requirements-as-an-invoice-administrator)
    - [View Payment Requirements as the Invoice Contact for a Payee](/product-manuals/procore-pay/tutorials/view-payment-requirements-as-the-invoice-contact-for-a-payee)
  - Incomplete requirements do NOT prevent a 

    In Procore Pay, a *Payments Disburser* is a Procore user granted permission to create and view disbursements in the Company level Payments tool. Because of the sensitive nature of payments, only a Payments Admin can add/remove disbursers.

    Payments Disburser from paying invoices unless you configure the 'Required and Prevents Payment' setting.
  - Any manual payment holds applied to an invoice can be viewed on an invoice in the Payment Requirements.

## Prerequisites

- Add a [Payments Admin](/process-guides/payor-setup-guide/authorize-payment-admins) or [Company Admin](/faq-what-is-a-company-admin) who can perform this step.

## Steps

1. Navigate to the Company level **Payments** tool.
2. Click the **Payments Settings**  icon.   
    This opens the Payments Settings page.
3. Click the **Payment Requirements** tab.
4. Click **Payment Requirements**.
5. Choose one (1) option for each requirement:

   - **Not Required**. Doesn't track the payment requirement.
   - **Required but Allows Payment**. Alerts users about unsatisfied payment requirements but lets them send payments.
   - **Required and Prevents Payment**. Alerts users about unsatisfied payment requirements and prevents them from sending payments.
6. Configure the options in each section as desired:

### Available Payment Requirements

| Option | **When ON...** | When OFF... | Learn More |
| --- | --- | --- | --- |
| **Holds Released** | Tracks the status of any payment holds applied to invoices. Holds must be released before payment. | Doesn't track invoices for payment holds. |  |
| **Commitment Executed** | Tracks the commitment associated with the invoice to ensure a check mark appears in the 'Executed' box. | Doesn't track the 'Executed' state on the commitment. | [Create a Commitment](/product-manuals/commitments-project/tutorials/create-a-commitment-change-order-cco)  [Edit a Commitment](/product-manuals/commitments-project/tutorials/edit-a-commitment) |
| **Contract Compliant** | Tracks the status of the contract compliance documents for the commitment. | Doesn't track the compliance status of the insurance certificates |  |
| **Change Orders Executed** | Tracks change orders that impact the contract associated with the invoice and require them to be in the 'Executed' state. | Doesn't track change orders. | [Create a Change Order](/product-manuals/change-orders-project/tutorials/create-a-change-order) |
| **Insurance Compliant** | Tracks the status of the insurance certifications for the commitment. | Doesn't track the compliance status of the insurance certificates. | [Manage Insurance & Compliance Statuses for a Commitment](/process-guides/invoice-administrator-guide/manage-insurance-documents--statuses) |
| **Invoice Approved** | Tracks invoices to ensure they are in one of these statuses: *Approved*, *Approved as Noted*, and *Pending Owner Approval*. See [What are the default statuses for Procore invoices?](/faq-what-are-the-default-statuses-for-procore-invoices) | Doesn't track invoice status. | [Bulk Edit the Status of Subcontractor Invoices with the Invoicing Tool](/product-manuals/invoicing-project/tutorials/bulk-edit-subcontractor-invoice-status-with-the-invoicing-tool) |
| **Invoice Compliant** | Tracks required compliance documents on subcontractor invoices. | Doesn't track invoice status. | [Add Required Compliance Documents to Compliance Templates](/process-guides/about-the-compliance-tab-on-subcontractor-invoices-with-procore-pay/add-requirements) |
| **Owner Funding Received** | Tracks the total **'Payment Received'** entries against the **'Current Payment Due'** for the owner invoice's billing period to ensure the owner invoice is fully paid. | Doesn't track **'Payment Received'** entries. | [Create a Record for a Payment Received](/product-manuals/invoicing-project/tutorials/create-a-record-for-a-payment-received) |
| **Sync to ERP** | Tracks the invoice to ensure it is synced with an integrated ERP system. | Doesn't track invoice syncing with ERP |  |
| **First-Tier Conditional Lien Waiver Signed** | Tracks first-tier signatures on conditional lien waivers on your invoices. *Note:* Only appears on an invoice when the requirement is enabled on its project. See [Enable Lien Waiver Templates on a Project](/process-guides/payor-setup-guide/enable-templates-on-projects). | Doesn't track signatures | [Create Lien Waiver Templates](/process-guides/payor-setup-guide/create-lien-waiver-templates) |
| **First-Tier Unconditional Lien Waiver Signed** | Tracks first-tier signatures on unconditional lien waivers for your invoices. *Note:* Only appears on an invoice when the requirement is enabled on its project. See [Enable Lien Waiver Templates on a Project](/process-guides/payor-setup-guide/enable-templates-on-projects). | Doesn't track signatures | [Create Lien Waiver Templates](/process-guides/payor-setup-guide/create-lien-waiver-templates) |
| **First-Tier Unconditional Unlocked for the Previous Invoice** | Tracks first-tier signatures on unlocked unconditional lien waivers for the commitment's previous invoices. *Notes:* Only appears on an invoice when the requirement is enabled on its project. See [Enable Lien Waiver Templates on a Project](/process-guides/payor-setup-guide/enable-templates-on-projects). | Doesn't track signatures | An invoice administrator can [Send a Request to Unlock a Signed Unconditional Lien Waiver](/process-guides/invoice-administrator-guide/request-to-unlock-signed-unconditional-waivers).  An unconditional lien waiver can only be unlocked by an invoice contact. See [Unlock a Signed Unconditional Lien Waiver as an Invoice Contact](/product-manuals/procore-pay/tutorials/unlock-a-signed-unconditional-lien-waiver-as-an-invoice-contact). |
| **Sub-Tier Waivers** | Tracks when sub-tier waivers are in the 'Approved' status. This requirement will not exist on projects that has disabled sub-tier waivers. *Note:* If sub-tier waivers are disabled on a project, this requirement won't appear. See [Enable the Sub-Tiers Card & Add Instructions on Project Invoices](/process-guides/payor-setup-guide/enable-sub-tier-waivers). | Doesn't track signatures | [Manage Sub-Tier Waivers](/product-manuals/procore-pay/tutorials/manage-lien-waivers-on-project-invoices) |

## Next Steps

- [Manage Payment Holds as a Payor](https://support.procore.com/products/online/user-guide/company-level/payments/tutorials/manage-payment-holds-as-a-payor)