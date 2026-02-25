# Add Payments Beneficiary Approvers as a Payor

Source: https://v2.support.procore.com/product-manuals/procore-pay/tutorials/add-payments-beneficiary-approvers-as-a-payor

---

##### Â General Availability in Select Markets (United States)

[Procore Pay](https://www.procore.com/pay)  is available in the United States. It is designed for General Contractors and Owner-Builders who act as their own General Contractors on a job. Procore Pay extends the [Invoice Management](https://www.procore.com/invoice-management) functionality in the Procore web application to handle the payment process between general and specialty contractors.

## Background

In Procore Pay, a *Payments Beneficiary Approver* is a user who has been granted permission to approve and manage beneficiary accounts in the Company level Payments tool. Approving a beneficiary account provides payees with the ability to receive payments.

## Things to Consider

- [Required User Permissions](/product-manuals/procore-pay/permissions)
- **Additional Information**:

  - A Payments Admin or Payments Disburser cannot be a Payments Beneficiary Approver.

    - A Payments Admin can already approve beneficiary accounts by default. See [Approve a Beneficiary Bank Account as a Payor](/process-guides/payor-setup-guide/approve-beneficiary-accounts).
    - A Payments Disburser cannot approve beneficiary accounts.
  - The Payments Beneficiary Approver role grants Procore users these privileges on the Company level Payments tool:

    - To approve and manage accounts in the Beneficiaries tab of the Payments tool. See [About the Beneficiaries Tab in the Payments Tool](/process-guides/payments-beneficiary-approver-guide/about-the-beneficiaries-tab).
    - To view the Subcontractor Invoices tab in the Company level Payments tool. See [About the Subcontractor Invoices Tab in the Payments Tool](/process-guides/payments-disburser-guide/about-the-subcontractor-invoices-tab).
    - To learn more about this role, see [What is a Payments Beneficiary Approver?](/process-guides/payor-setup-guide/add-payments-beneficiary-approvers)

## Prerequisites

To be added as a Payments Beneficiary Approver:

- You must have a user account in the Company level Directory tool. See [Add a User Account to the Company Directory](/product-manuals/directory-company/tutorials/add-a-user-account-to-the-company-directory).
- Your account must be designated as an employee in the Company Directory tool. See [How do I add someone as an employee of my company?](/product-manuals/directory-company/tutorials/add-someone-as-an-employee-of-your-company)

## Steps

1. Navigate to the Company level **Payments** tool.
2. Click the **Payments Settings**  icon.   
    This opens the Payment Settings page. The External Bank Accounts page is active by default.
3. Click the **Payment Processing** tab.   
    This is the active tab by default.
4. Click **Payments Permissions**.
5. Scroll to **Payments Beneficiary Approvers**.
6. Click **Add Beneficiary Approvers**.  
    This opens the **Add Beneficiary Approvers** window.
7. In the Add Beneficiary Approvers window, add one (1) or more employees from your company as follows:

   ##### Â Tip

   **Which users are available in the Search People list?** Any Procore user account marked as an employee of your company in the Company level Directory tool. Payment Beneficiary Approvers must be employees of your company. See [How do I add someone as an employee of my company?](/product-manuals/directory-company/tutorials/add-someone-as-an-employee-of-your-company)

- Start typing the user's name in the **Search People** list.
- Select the matching user from the drop-down list.

- Click **Continue**.
- Review the names in the **Payments Beneficiary Approvers** list.
- Click **Add Approver**.   
   A GREEN banner indicates the action was successful. Procore also logs the 'User added as Approver' action in the Change History.