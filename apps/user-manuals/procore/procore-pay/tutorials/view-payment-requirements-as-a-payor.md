# View Payment Requirements as a Payor

Source: https://v2.support.procore.com/product-manuals/procore-pay/tutorials/view-payment-requirements-as-a-payor

---

##### Â General Availability in Select Markets (United States)

[Procore Pay](https://www.procore.com/pay)  is available in the United States. It is designed for General Contractors and Owner-Builders who act as their own General Contractors on a job. Procore Pay extends the [Invoice Management](https://www.procore.com/invoice-management) functionality in the Procore web application to handle the payment process between general and specialty contractors.

## Background

The table in the 'Subcontractor Invoices' tab of the Company level Payments tool has a 'Payment Readiness' group. In that group are two (2) columns: *Requirements* and *Manual Holds*. The data in these columns helps [Payments Admins](/process-guides/payor-setup-guide/authorize-payment-admins) and [Payments Disbursers](/process-guides/payor-setup-guide/add-payments-disbursers) determine the [payment readiness](https://support.procore.com/products/online/user-guide/company-level/payments/glossary) of your company's subcontractor invoices. The 'Requirements' column includes a pie chart and unit fraction to show the number of [payment requirements](https://support.procore.com/products/online/user-guide/company-level/payments/glossary) met by each invoice. Users can click the unit fraction link to open the 'Payment Readiness' panel to help them determine when an invoice is ready to process and fulfill payment.

## Things to Consider

- [Required User Permissions](/product-manuals/procore-pay/permissions)
- **Additional Information**:

  - What you can see in the Payment Requirements panel depends on your role. For the options, see [View Payment Requirements](https://support.procore.com/products/online/user-guide/company-level/payments/tutorials/view-payment-requirements).
  - Incomplete requirements prevent Payments Admins and Disbursers from paying invoices only with the âRequired and Prevents Paymentâ setting configured. See [Configure Payment Requirements as a Payor](/process-guides/payor-setup-guide/configure-payment-requirements).
  - Any manual payment holds applied to an invoice can be viewed on an invoice in the Payment Requirements:\* To apply or release manual payment holds, see [Manage Payment Holds as a Payor](https://support.procore.com/products/online/user-guide/company-level/payments/tutorials/manage-payment-holds-as-a-payor).

## Prerequisites

- [Configure Payment Requirements as a Payor](/process-guides/payor-setup-guide/configure-payment-requirements)

## Steps

- Open the Payment Readiness Panel
- About the Overview Tab
- About the Holds Tab

### Open the Payment Readiness Panel

1. Navigate to the Company level **Payments** tool.   
    The Subcontractor Invoices tab is active by default.
2. In the **Subcontractor Invoices** table, locate the invoice.
3. Under the **Payment Readiness** group, click the unit fraction link under **Requirements**.  
      
      
      
    This opens the Payment Readiness panel on the right side of the page.

### About the Overview Tab

The Overview tab of the Payment Readiness panel shows the following information.

The table below describes the elements pictured above. To learn more, see [Configure Payment Requirements as a Payor](/process-guides/payor-setup-guide/configure-payment-requirements).

| **Item** | **Description** | **Example (See Above)** |
| --- | --- | --- |
| **Information Banner** | If any holds are applied to the invoice, a YELLOW banner appears at the top of the **Overview** tab above the **Summary**. Click **View Holds** to jump to the **Holds** tab. | *There are one or more holds on this invoice* |
| **Company Name** | Shows the name of the 'Contract Company' on the commitment. | *Earthwork Jim* |
| **Project Number** | Shows the name of the Procore project associated with the invoice. | *Demo Project* |
| **Invoice Link** | Click the hyperlink to open the subcontractor invoice with the Invoicing tool in a separate browser window. | *SC-018: Invoice #001* |
| **Requirements Complete** | Displays a pie chart and unit fraction to show the number of completed payment requirements. See [Manage Payment Requirements as a Payor](/product-manuals/procore-pay/tutorials/manage-payment-requirements-as-a-payor). | *5/10 Requirements Complete* *Note:* The numerator (5) indicates that five requirements are complete. The denominator (10) corresponds to the total number of requirements. To learn more, see View the Invoice Details below. |
| **Total** | The total amount, including retainage (if any), for the invoice. | *$4,5000.00* |
| **Invoice Status** | Shows the invoice's current status. See [What are the default statuses for Procore invoices?](/faq-what-are-the-default-statuses-for-procore-invoices) | *Revise and Resubmit* |
| **Payment Status** | Shows the payment status of the invoice: *Paid* or *Unpaid*. | *Unpaid* |
| **Billing Period** | Shows the billing period for the invoice. See [Create Automatic Billing Periods](/product-manuals/invoicing-project/tutorials/create-automatic-billing-periods) or [Create Manual Billing Periods](/product-manuals/invoicing-project/tutorials/create-manual-billing-periods). | *12/01/21 - 12/31/21* |
| **Requirements** | Displays the tracking requirements and status of your company's subcontractor invoices. This helps your team determine payment readiness on invoices. To configure the tracking requirements, see [Configure Payment Requirements as a Payor](/process-guides/payor-setup-guide/configure-payment-requirements). |  |
| **View** | Click this button to perform requirement-specific actions:  **Commitments**   - **Commitment Executed**. Open the General tab of the commitment so you can edit the General Information card to mark the Executed check box. See [Edit a Commitment](/product-manuals/commitments-project/tutorials/edit-a-commitment). - **Contract Compliant**. Open the Compliance tab of the commitment to modify the information in the Contract Compliance Documents card. See [Manage Contract Compliance Documents & Statuses for a Commitment](/product-manuals/procore-pay/tutorials/view-contract-compliance-documents-for-commitments-as-a-payor). - **Insurance Compliant**. Open the Compliance tab of the commitment to modify the information in the Insurance card. See [Edit Contract Compliance Documents for Commitments as an Invoice Administrator](/product-manuals/procore-pay/tutorials/edit-contract-compliance-documents-for-commitments-as-an-invoice-administrator).   **Invoice**   - **Change Orders Executed**. Open the Change Orders tab of the commitment to view or edit the executed status of the change order. See [Edit a Change Order](/product-manuals/change-orders-project/tutorials/edit-a-change-order). - **Invoice Approved**. Open the subcontractor invoice with the Invoicing tool in a separate browser window to edit its status in the General Information tab. See [Edit the General Information Card of an Invoice](/product-manuals/invoicing-project/tutorials/create-an-invoice-on-behalf-of-an-invoice-contact). - **Owner Funding Received**. Open the Payments Received tab in the prime contract to add an owner invoice payment to the Payments Received list. See [Create a Payment Received for a Prime Contract](/product-manuals/prime-contracts-project/tutorials/create-a-payment-received-for-a-prime-contract) - **Synced to ERP**. Open the General tab of the commitment to check the sync status of the commitment. See [What do the ERP icons mean?](/faq-what-do-the-erp-icons-mean) This option only appears for companies syncing Procore data with an integrated ERP system. | [Configure Payment Requirements as a Payor](/process-guides/payor-setup-guide/configure-payment-requirements) |
| Visible to Payors: **View, Request, or Manage** | Click the available button to perform requirement-specific actions:  **Lien Waivers**   - **View**. Click to open the signed lien waiver in separate browser window. - **Request**. Click to open the 'Send Request to Unlock Waiver?' prompt. Then click **Send Request** to send the invoice contact(s) for the invoice a request to unlock the signed lien waiver. - **Manage**. Click to jump to the **Lien Rights** tab of the subcontractor invoice to upload or approve waivers. | [Send a Request to Unlock a Signed Unconditional Lien Waiver](/process-guides/invoice-administrator-guide/request-to-unlock-signed-unconditional-waivers) |
| Visible to Payees: **View**, **Unlock**, or **Manage** | Click the available button to perform requirement-specific actions:  **Lien Waivers**   - **View**. Click to open the signed lien waiver in separate browser window. - **Unlock**. Click this button to unlock a signed unconditional lien waiver. - **Manage**. Click to jump to the **Lien Rights** tab of the subcontractor invoice to manage lien waivers. | [Unlock a Signed Unconditional Lien Waiver as an Invoice Contact](/product-manuals/procore-pay/tutorials/unlock-a-signed-unconditional-lien-waiver-as-an-invoice-contact) |

### About the Holds Tab

The Holds tab shows the following information.

The table below describes the features in the Holds tab. To learn more, see [Manage Payment Holds as a Payor](https://support.procore.com/products/online/user-guide/company-level/payments/tutorials/manage-payment-holds-as-a-payor).

| **Label** | Element | **Description** |
| --- | --- | --- |
| **Status** | Icon | - A YELLOW caution icon indicates a manual hold has been applied to the invoice. - A GREEN checkmark indicates a manual hold has been released. - No mark indicates a manual hold has not been placed on the invoice. |
| **Create Hold** | Button | Click this button to create a new hold. |
| **Release** | Button | Click this button to release an existing hold. |
| **Edit** | Button | Click this button to modify an existing hold. |
| **Created By** | Field | Shows the name of the user who created the hold. |
| **Last Modified By** | Field | Shows the name of the user who last updated the hold. |
| **Description** | Text | Shows any information entered by the person who created or edited the hold. |
| **Attachments** | File | Shows any attachments added to the hold. Click the file link to download a copy of the file(s). |