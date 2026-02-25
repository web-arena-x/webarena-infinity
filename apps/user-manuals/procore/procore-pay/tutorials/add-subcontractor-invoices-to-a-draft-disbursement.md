# Add Subcontractor Invoices to a 'Draft' Disbursement

Source: https://v2.support.procore.com/product-manuals/procore-pay/tutorials/add-subcontractor-invoices-to-a-draft-disbursement

---

##### Â General Availability in Select Markets (United States)

[Procore Pay](https://www.procore.com/pay)  is available in the United States. It is designed for General Contractors and Owner-Builders who act as their own General Contractors on a job. Procore Pay extends the [Invoice Management](https://www.procore.com/invoice-management) functionality in the Procore web application to handle the payment process between general and specialty contractors.

## Background

Procore Pay's 'Draft' disbursement feature benefits payors by reducing errors and increasing payment accuracy. It serves as a checkpoint, allowing your team to confirm released invoice holds and meet company requirements before authorization. While in 'Draft' status, authorized users can add more subcontractor invoices, enabling accounting teams to collaborate on a single, consolidated disbursement. This reduces funds transfer and banking fees.

A Payments Admin or Payments Disburser can start custom workflows, authorize disbursements, and update an invoice's Payment Amount to issue partial payments. See [About Partial Payments with Procore Pay](https://support.procore.com/products/online/procore-pay/tutorials/about-partial-payments-with-procore-pay). These users are required to [Set Up MFA for Procore Pay on Your Device](/process-guides/payor-setup-guide/set-up-mfa-on-a-mobile-device). Disbursement Contributors are restricted to adding or removing invoices and can only save changes in draft disbursements, so they arenât required to set up Multi-Factor Authentication.

## Things to Consider

- [Required User Permissions](/product-manuals/procore-pay/permissions)
- **Additional Inform**ation:

  - A single disbursement can handle up to 100 subcontractor invoice payments.
  - Invoice payments must be a positive amount. Procore Pay does not support negative invoice payments.
  - Disbursement contributors can only save their disbursements as drafts.
  - Payments Admins and Disbursers can change the Payment Amount to issue partial payments. See [About Partial Payments with Procore Pay](https://support.procore.com/products/online/procore-pay/tutorials/about-partial-payments-with-procore-pay). Updated Payment Amounts must be less than or equal to the Amount Due on an invoice.
  - Payment Admins and Disbursers cannot authorize a disbursement if they are the last approver on any invoice within the disbursement.

## Prerequisites

- [Add Payments Admins as a Payor](/process-guides/about-the-payment-processing-tab-in-the-payments-tool/add-or-remove-payments-admins) and [Set Up MFA for Procore Pay on Your Device](/process-guides/payor-setup-guide/set-up-mfa-on-a-mobile-device).
- [Add Payments Disbursers as a Payor](/process-guides/about-the-payment-processing-tab-in-the-payments-tool/add-disbursers) and [Set Up MFA for Procore Pay on Your Device](/process-guides/payor-setup-guide/set-up-mfa-on-a-mobile-device).
- [Add Disbursement Contributors as a Payor](/product-manuals/procore-pay/tutorials/add-disbursement-contributors-as-a-payor). This role doesnât require MFA setup.
- [Create Disbursements](/process-guides/payments-admin-guide/create-disbursements)

## Steps

1. Navigate to the Company level **Payments** tool.
2. Click the **Subcontractor Invoices** tab.
3. Select the invoices to add to a disbursement by marking the corresponding **Invoice #.** check box(es).
4. Click **Add to Disbursement** and choose the disbursement from the drop-down list.  
    This list only includes disbursements in the 'Draft' status.

   ##### Â Tip

   **Want to create a disbursement for the selected invoices?** Click **Create New**. Then see [Create Disbursements](/process-guides/payments-admin-guide/create-disbursements).

- In the **#1 Review Invoices** page, do the following:

  - If there are invoices in the disbursement that are ineligible for payment: **Show/Hide**

    - When the Review Invoices page shows an error message saying there are invoices ineligible for payment, click **Show Details** to expand the error message and review the details. Click **Hide Details** to hide the error message. You can address the eligibility issue or click the  icon to remove the disbursement to address it later. See [Remove Subcontractor Invoices from Disbursements as a Payor](/product-manuals/procore-pay/tutorials/remove-subcontractor-invoices-from-disbursements-as-a-payor).
  - If you want to issue a partial payment for an invoice: **Show/Hide**

    - 1. In the **Review Invoices** card, confirm the list of invoices to be added to the disbursement.
      2. Expand the **Amounts** column group to review the **Net Amount**, **Paid Amount**, **Joint Check Amount**, **Early Pay Fee**, **Amount Due**, and **Payment Amount** for each invoice.
      3. *(Optional)* To issue a partial payment, click the **Payment Amount** link.  
          This opens the Update Payment Amount window.

         ##### Â Tip

         **Want to learn more about partial payments?** See [About Partial Payments with Procore Pay](https://support.procore.com/products/online/procore-pay/tutorials/about-partial-payments-with-procore-pay)
    - Do the following:

      - Enter an updated amount in the **Payment Amount** box. Entries must be less than or equal to the **Amount Due** of the invoice.
      - Enter relevant information about the updated payment in the **Notes** box.
      - Click **Update**.

    Procore updates the payment amount for the invoice.