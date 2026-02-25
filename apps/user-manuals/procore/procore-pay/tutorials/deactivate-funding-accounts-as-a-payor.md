# Deactivate Funding Accounts as a Payor

Source: https://v2.support.procore.com/product-manuals/procore-pay/tutorials/deactivate-funding-accounts-as-a-payor

---

##### Â General Availability in Select Markets (United States)

[Procore Pay](https://www.procore.com/pay)  is available in the United States. It is designed for General Contractors and Owner-Builders who act as their own General Contractors on a job. Procore Pay extends the [Invoice Management](https://www.procore.com/invoice-management) functionality in the Procore web application to handle the payment process between general and specialty contractors.

## Background

Only a [Payments Admin](/process-guides/payor-setup-guide/authorize-payment-admins) can deactivate a funding account in the 

In Procore Pay, a *payor* is a general contractor who sends invoice payments to specialty contractors.

Payor environment. You will deactivate accounts when you no longer want your 

In Procore Pay, a *Payments Disburser* is a Procore user granted permission to create and view disbursements in the Company level Payments tool. Because of the sensitive nature of payments, only a Payments Admin can add/remove disbursers.

Payments Disburser to select that account for 

In Procore Pay, a *drawdown* refers to the disbursement of funds from a payor's funding account to the payor's deposit account held by a financial institution.

Drawdown requests on a new 

A *disbursement* is the action of paying out money from a fund. In Procore Pay, a disbursement withdraws funds from a general contractor's funding account and transmits them to the general contractor's deposit account. Payment orders are then issued to withdraw funds from the deposit account to pay invoices.

Disbursement.

## Things to Consider

- [Required User Permissions](/product-manuals/procore-pay/permissions)

## Prerequisites

- [Add Funding Accounts](/process-guides/about-the-payment-processing-tab-in-the-payments-tool/add-funding-accounts)

## Steps

1. Navigate to the Company level **Payments** tool.
2. Click the Payments Settings  icon.  
    This opens the Payments Settings page. The 'Business Entities' page in the 'Payments Processing' tab is active by default. This page lists each 

   In Procore Pay, a business entity is an organization recognized as separate from its owner(s). Some construction companies operate as a single business entity, while others operate as multiple business entities, with each entity, subsidiary, or division focusing on overseeing a different market or sector.

   Business Entity configured to pay invoices in your company's Procore Pay software.
3. Locate the business entity to modify and click its funding account(s) link.
4. Locate the funding account to edit.
5. Click the **Overflow** menu and choose **Deactivate** from the drop-down menu.

   ##### Â Tip

   **Can I deactivate a default account?** No. A default account cannot be deactivated unless you first designate another account as the default. See [Set a Default Funding Account as a Payor](/process-guides/about-the-payment-processing-tab-in-the-payments-tool/set-a-default-funding-account).

  
- In the 'Deactivate Funding Account' confirmation prompt, review the message.

  ##### Â Important

  Before you deactivate the funding account, be aware of the following:

  - If the account being deactivated is also your default funding account, a Payments Admin must first set a new default account for those projects. See [Update Your Project's Bank Accounts](/product-manuals/procore-pay/tutorials/manage-payments-project-controls-for-a-single-project).
  - Once deactivated, Payments Disbursers can no longer select the funding account when creating new disbursements.
  - Drawdown requests for existing disbursements are NOT canceled. If the existing disbursement's funds request is successful, Procore Pay withdraws the aggregate disbursement amount from your funding account and transfers it to your deposit account to process invoice payments.