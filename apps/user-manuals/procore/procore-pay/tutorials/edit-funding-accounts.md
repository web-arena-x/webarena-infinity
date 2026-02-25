# Edit Funding Accounts as a Payor

Source: https://v2.support.procore.com/product-manuals/procore-pay/tutorials/edit-funding-accounts

---

##### Â General Availability in Select Markets (United States)

[Procore Pay](https://www.procore.com/pay)  is available in the United States. It is designed for General Contractors and Owner-Builders who act as their own General Contractors on a job. Procore Pay extends the [Invoice Management](https://www.procore.com/invoice-management) functionality in the Procore web application to handle the payment process between general and specialty contractors.

## Background

After adding a funding account to Procore Pay, a [Payments Admin](/process-guides/payor-setup-guide/authorize-payment-admins) can modify some of the account information.

## Things to Consider

- [Required User Permissions](/product-manuals/procore-pay/permissions)

## Prerequisites

- [Add Funding Accounts as a Payor](/process-guides/about-the-payment-processing-tab-in-the-payments-tool/add-funding-accounts)

## Steps

1. Navigate to the Company level **Payments** tool.
2. Click the **Payments Settings**  icon.This opens the Payments Settings page.  
    The 'Business Entities' page in the 'Payments Processing' tab is active by default and lists each 

   In Procore Pay, a business entity is an organization recognized as separate from its owner(s). Some construction companies operate as a single business entity, while others operate as multiple business entities, with each entity, subsidiary, or division focusing on overseeing a different market or sector.

   Business Entity that pays invoices for your company's Procore Pay software.
3. Locate the business entity to modify and click its funding account link.
4. Locate the account to modify.
5. Click the **Overflow** menu and choose **Edit** from the drop-down menu.  
      
      
      
    This opens the Edit Account Details page.
6. In the **Edit Account Details** page, do the following:

   - \*\***Nickname**. Enter a unique nickname for the account. Nicknames quickly identify the bank account for disbursements while helping to protect the privacy of its account number.
   - **Business Entity**. Shows the name of the current business entity.
   - **Bank ID**. Enter a bank identifier. Procore uses the bank ID as a prefix for a payment's check number. You can change this number at any time. However, any new changes only impact new check numbers.

     ##### Â Important

     **For companies using the**  **ERP Integrations tool**: The bank identifier must match the funding account's 'Bank ID' in your integrated ERP system.

- **Check Number**. Enter a *check number* for the next invoice payment. This provides each check a unique identification number for this account. See [How does Procore assign numbers to disbursement payouts?](/faq-how-does-procore-pay-assign-numbers-to-disbursements-and-checks) It also helps users who manage disbursements to identify transactions.

  ##### Â Important

  **For companies using the**  **ERP Integrations tool**:

  - After Procore Pay processes an invoice payment in a disbursement, the 'Bank ID' and 'Check Number' combination is exported to your integrated ERP system.
  - To avoid potential ERP synchronization errors, ensure the **Check Number** entered is higher than the last check number in your ERP system to prevent duplication in your integrated ERP system. See [How do payments made in Procore Pay sync with an integrated ERP system?](/faq-how-do-payments-made-in-procore-pay-sync-with-an-integrated-erp-system)