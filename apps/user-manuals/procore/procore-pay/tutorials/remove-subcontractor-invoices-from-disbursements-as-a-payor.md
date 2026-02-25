# Remove Subcontractor Invoices from Disbursements as a Payor

Source: https://v2.support.procore.com/product-manuals/procore-pay/tutorials/remove-subcontractor-invoices-from-disbursements-as-a-payor

---

##### Â General Availability in Select Markets (United States)

[Procore Pay](https://www.procore.com/pay)  is available in the United States. It is designed for General Contractors and Owner-Builders who act as their own General Contractors on a job. Procore Pay extends the [Invoice Management](https://www.procore.com/invoice-management) functionality in the Procore web application to handle the payment process between general and specialty contractors.

## Background

Only authorized users can remove subcontractor invoices from a 'Draft' disbursement. The 

In Procore Pay, a *Payments Admin* is a designated Procore user who administers the Company level Payments tool for that company's Procore account. Typically, one (1) or a small number of trusted users are designated to perform the tasks associated with this role.

Payments Admin, 

In Procore Pay, a *Payments Disburser* is a Procore user granted permission to create and view disbursements in the Company level Payments tool. Because of the sensitive nature of payments, only a Payments Admin can add/remove disbursers.

Payments Disburser, and 

In Procore Pay, a *Disbursement Contributor* is a Procore user with limited access to the Company level Payments tool. They can add or remove subcontractor invoices from 'Draft' disbursements and save their changes as a 'Draft'. Only a Payments Admin can assign a user to the Disbursement Contributor role.

Disbursement Contributor roles can remove invoices from the 'Review Invoices' page of a 'Draft' disbursement. When using a payments workflow, users can only remove invoices while the workflow is active, and they must provide a reason.

Disbursement Contributors can only add or remove invoices and save changes to 'Draft' disbursements, so they do not require MFA. Payments Admins and Payments Disbursers can also start custom workflows, authorize disbursements, and adjust invoice amounts for partial payments (see [About Partial Payments with Procore Pay](https://support.procore.com/products/online/procore-pay/tutorials/about-partial-payments-with-procore-pay)). Both roles must [Set Up MFA for Procore Pay on Your Device](/process-guides/payor-setup-guide/set-up-mfa-on-a-mobile-device).

## Things to Consider

- [Required User Permissions](/product-manuals/procore-pay/permissions)
- **Additional Information**:

  - Invoices cannot be removed from a disbursement:\* After the disbursement is authorized.\* The disbursement has been submitted to the banking system for payment processing.
  - To learn how to cancel a disbursement, see [Cancel Disbursements](/product-manuals/procore-pay/tutorials/cancel-disbursements-before-authorization-as-a-payor).

## Prerequisites

- [Add Payments Admins as a Payor](/process-guides/about-the-payment-processing-tab-in-the-payments-tool/add-or-remove-payments-admins) and [Set Up MFA for Procore Pay on Your Device](/process-guides/payor-setup-guide/set-up-mfa-on-a-mobile-device).
- [Add Payments Disbursers as a Payor](/process-guides/about-the-payment-processing-tab-in-the-payments-tool/add-disbursers) and [Set Up MFA for Procore Pay on Your Device](/process-guides/payor-setup-guide/set-up-mfa-on-a-mobile-device).
- [Add Disbursement Contributors as a Payor](/product-manuals/procore-pay/tutorials/add-disbursement-contributors-as-a-payor). This role doesnât require MFA setup.
- [Create Disbursements](/process-guides/payments-admin-guide/create-disbursements)

## Steps

- Remove Subcontractor Invoices from a New Disbursement
- Remove Subcontractor Invoices During a Payments Workflow

### Remove Subcontractor Invoices from a New Disbursement

Authorized users can remove invoices from new disbursements during creation and when they're in the 'Draft' status.

1. Follow the steps in [Create Disbursements](/process-guides/payments-admin-guide/create-disbursements).
2. In the **Review Invoices** page of the **New Disbursement**, locate the invoice to remove.
3. Click the trash can icon.   
    Procore Pay removes the subcontractor invoice from the Review Invoices page.

### Remove Subcontractor Invoices During a Payments Workflow

Authorized users can remove invoices from draft disbursements when a [Payments Workflow](/process-guides/about-the-payment-processing-tab-in-the-payments-tool/best-practices) is in progress.

1. Open a disbursement in the *Under Review* status.
2. In the **General** tab, the **Included Invoices** card lists all of the invoices included in the disbursement.
3. Locate the invoice to remove and click the trash can icon.   
    This opens the Remove Invoice from Disbursement prompt.
4. In the **Reason for Removal** box, enter the reason for removing the disbursement. This is a required field.
5. Click **Remove** to confirm.   
    Procore Pay removes the subcontractor invoice from the disbursement. See [View a](/process-guides/payments-disburser-guide/view-a-disbursement) [Disbursement](/process-guides/payments-disburser-guide/view-a-disbursement). In addition, it appears in the **Removed Invoices** card on the **General** tab of the disbursement. It is also logged in the disbursement's **Change History** tab.