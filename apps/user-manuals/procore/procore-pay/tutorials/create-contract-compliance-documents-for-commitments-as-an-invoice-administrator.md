# Create Contract Compliance Documents for Commitments as an Invoice Administrator

Source: https://v2.support.procore.com/product-manuals/procore-pay/tutorials/create-contract-compliance-documents-for-commitments-as-an-invoice-administrator

---

##### Â General Availability in Select Markets (United States)

[Procore Pay](https://www.procore.com/pay)  is available in the United States. It is designed for General Contractors and Owner-Builders who act as their own General Contractors on a job. Procore Pay extends the [Invoice Management](https://www.procore.com/invoice-management) functionality in the Procore web application to handle the payment process between general and specialty contractors.

## Background

When enabled on a Procore project, Procore Pay adds a 'Compliance' tab to the project's commitments. On a subcontractor invoice, the controls in the 'Contract Compliance Documents' card work with the 'Contract Compliant' setting in the 'Payment Requirements' tab of the Company level Payments tool. This allows your team to track and review the status of the commitment contract's compliance document entries (for example, agreements, bonds, licenses, permits, and more). This helps your team ensure that all documents comply with the contract's requirements before your team releases invoice payments with Procore Pay.

## Things to Consider

- [Required User Permissions](/product-manuals/procore-pay/permissions)
- **Additional Information**:

  - To learn how to manage insurance documents & compliance statuses, see [Manage Insurance Documents & Compliance Statuses for a Commitment](/process-guides/invoice-administrator-guide/manage-insurance-documents--statuses).
  - To preview a file attachment in the **Details** pane of a contract compliance document entry, you must first click **Save** to complete the upload.
  - You are limited to adding one (1) file attachment per entry.

## Prerequisites

- To add the 'Compliance' tab to a project's commitments, enable Procore Pay on the project. See [Enable or Disable Procore Pay on Your Projects](/process-guides/about-the-payment-processing-tab-in-the-payments-tool/enable-or-disable-pay).
- To track compliance status with Procore Pay, turn the 'Contract Compliant' payment requirement ON. See [Configure Payment Requirements: Commitment Requirements](/process-guides/payor-setup-guide/configure-payment-requirements).

## Video

## Steps

1. Navigate to the project's **Commitments** tool.
2. In the **Contracts** tab, locate the commitment to work with.
3. Click the **Number** link to open it.
4. In the commitment, click the **Compliance** tab.
5. Scroll to the **Contract Compliance Documents** card.
6. Click **Create New**.

   ##### Â Note

   The **Create New** button is only visible and available to users granted invoice administrator permissions on the project's **Commitments** tool.

- In the **Details** pane, enter:

  - **Name**. Type the name of the compliance requirement. For example, type: Surety Bond
  - **Type**. Select a requirement type from the drop-down list. The choices are *Bond*, *License*, *Master Agreement*, *Permit*, *Safety*, *W-9*, or *Other*.
  - **Status**. Choose a status for the requirement: *Compliant* or *Not Compliant.*
  - **Effective Date**. Select an effective date for the compliance requirement.
  - **Expiration Date**. Select an expiration date for the compliance requirement.
  - **Send Expiration Notification**. Mark this checkbox to send a daily email notification to the commitment's [invoice contacts](/faq-what-is-an-invoice-contact) when the compliance requirement is within fourteen (14) days of the set 'Expiration Date'.

    ##### Â Note

    To stop the email notification, change or remove the expiration date. Procore stops sending notifications sixty (60) days after the Expiration Date passes.