# Enable Procore Pay as a Payor

Source: https://v2.support.procore.com/product-manuals/procore-pay/tutorials/enable-procore-pay-as-a-payor

---

##### Â General Availability in Select Markets (United States)

[Procore Pay](https://www.procore.com/pay)  is available in the United States. It is designed for General Contractors and Owner-Builders who act as their own General Contractors on a job. Procore Pay extends the [Invoice Management](https://www.procore.com/invoice-management) functionality in the Procore web application to handle the payment process between general and specialty contractors.

## Background

After purchasing Procore Pay, Procore assigns an Implementation Project Manager to oversee the Procore Pay implementation process. The Project Manager schedules time with your team to identify key contacts and technical leads, develop a project plan, roll-out strategy, conduct product training with your end users, and walk you through the payee onboarding steps.

## Steps

- Step 1: Initial Procore Pay Setup
- Step 2: Achieve Payment Readiness
- Step 3: Payment Testing & Project Closeout

#### Step 1: Initial Procore Pay Setup

The Payment Operations team at Procore works with your company's key contacts and technical leads to set up Procore Pay.

##### Â Tip

- **Does your company want to use Procore's** [Monthly Sandbox](/faq-what-is-the-monthly-sandbox-environment) **environment to test new tools and features?** Companies enabling Procore Pay need to request an additional configuration to maintain access to your Monthly Sandbox. See

**Click here to view the steps.**

During the initial phase, the Payment Operations team collaborates with your company's key contacts and tech leads to activate Procore Pay in your Procore account:

- **Procore Pay Activation**. The Payment Operations team will activate Procore Pay in your Procore account. They will also activate features for Payment Requirements, Lien Waivers, and the Invoice Management tools.
- **Single Sign-On (SSO) Configuration**. If you utilize an SSO solution, our team works with your technical leads to adjust your solution's settings to grant authorized team members Procore Pay access.
- **Multi-Factor Authentication (MFA)**. Procore Pay requires users to authenticate their identity through MFA when logging in and before performing sensitive financial transactions. Your technical team will need to choose a TOTP-compliant one-time password application. See [Why is MFA mandatory for Procore Pay and how does it work?](/process-guides/payments-disburser-guide/how-does-mfa-work-with-procore-pay)

As the payor, you will be assisted by the Payment Operations team in establishing a deposit account with Procore's banking partner and setting up user access to Procore Pay:

- **Approval of Banking Partner Agreements**. You will need to complete forms to open a Procore Pay Deposit Account. Following this, we can initiate the integration of your deposit account with the transaction banking system. See [Open a Deposit Account for Procore Pay as a Payor](/process-guides/payor-setup-guide/open-deposit-accounts).
- **Submission of Authorized Payment Administrator Form**. This form empowers our Payment Operations team to grant access to your designated Payments Admins. Post-completion, we can grant user access to your Payments Admins. See [Add or Remove Payments Admins as a Payor](/process-guides/about-the-payment-processing-tab-in-the-payments-tool/add-or-remove-payments-admins).
- **MFA Setup for Payment Admins**. After configuring your SSO solution, your company's authorized Payment Admins can set up MFA for Procore Pay on their mobile devices. See [Set Up MFA for Procore Pay on Your Device](/process-guides/payor-setup-guide/set-up-mfa-on-a-mobile-device) and [Log in to Procore using MFA](/product-manuals/procore-mfa/tutorials/log-in-to-procore-using-mfa).

This diagram details the initial Procore Pay setup workflow.

---

#### Step 2: Achieve Payment Readiness

For the next step, Procore assigns a Strategic Product Consultant to work with your company's key contacts and team members to manage your implementation process so you can achieve payment readiness. This phase typically includes payor onboarding and training with your Procore Strategic Product Consultant.

**Click here to view the onboarding workflow.**

**Click here to view the sample training agendas.**

To maximize the effectiveness of your company's training session(s), Procore encourages your key contacts and future Procore Pay to share your company's specific goals and target outcomes for Procore Pay with your Procore point of contact  and Implementation Project Manager.

##### Sample Training Agenda: Overview Company Payments Tool

For teams interested in an overview of the Company Payments tool:

- **Payment Settings**. See [About the Payments Settings](/product-manuals/procore-pay/tutorials/about-the-payments-settings).

  - **Payment Processing.**

    - Funding Accounts. See [Add Funding Accounts as a Payor](/process-guides/about-the-payment-processing-tab-in-the-payments-tool/add-funding-accounts).
    - Payment Permissions.
    - Project Controls
    - Change History. See [View the Payments Tool Change History](/process-guides/about-the-payment-processing-tab-in-the-payments-tool/view-history).
    - *Optional.* Workflow Settings. See [Best Practices for Creating a Payments Workflow](/process-guides/about-the-payment-processing-tab-in-the-payments-tool/best-practices).
    - Advanced Settings.
  - **Payment Requirements**. See [Configure Payment Requirements as a Payor](/process-guides/payor-setup-guide/configure-payment-requirements).

    - Enabling Lien Waivers. See [Enable Lien Waivers in the Company Payments Tool](/process-guides/payor-setup-guide/enable-lien-waivers).
    - Managing Payment Requirements. See [Manage Payment Requirements as a Payor](/product-manuals/procore-pay/tutorials/manage-payment-requirements-as-a-payor).
- **Subcontractor Invoices Tab**. See [About the Subcontractor Invoices Tab in the Payments Tool](/process-guides/payments-disburser-guide/about-the-subcontractor-invoices-tab).
- **Disbursements Tab**. See [About the Disbursements Tab in the Payments Tool](/process-guides/payments-disburser-guide/about-the-disbursements-tab).
- **Beneficiaries Tab**. See [About the Beneficiaries Tab in the Payments Tool](/process-guides/payments-beneficiary-approver-guide/about-the-beneficiaries-tab).

##### Sample Training Agenda: Streamline Lien Waiver Collection with Procore Pay

For teams interested in streamlining lien waiver collection:

- **Manage Lien Waivers on Subcontractor Invoices**

  - As a payor:

    - [Enable Lien Waivers in the Company Payments Tool](/process-guides/payor-setup-guide/enable-lien-waivers)
    - [Enable Lien Waivers & Set Default Templates on Projects](/process-guides/payor-setup-guide/enable-templates-on-projects)
    - [Generate Lien Waivers on Project Invoices](/process-guides/invoice-administrator-guide/generate-lien-waivers)
    - [Preview Lien Waivers on Project Invoices](/process-guides/invoice-administrator-guide/preview-lien-waivers)
    - [Send a Request to Unlock a Signed Unconditional Lien Waiver](/process-guides/invoice-administrator-guide/request-to-unlock-signed-unconditional-waivers)
  - As a payee:

    - [Sign Lien Waivers on Project Invoices](/process-guides/payee-user-guide/sign-lien-waivers)
    - [Unlock a Signed Unconditional Lien Waiver as an Invoice Contact](/product-manuals/procore-pay/tutorials/unlock-a-signed-unconditional-lien-waiver-as-an-invoice-contact)
- **Pay Invoices with Procore Pay**

  - [Create Disbursements](/process-guides/payments-admin-guide/create-disbursements)

##### Sample Training Agenda: Manage Payment Requirements & Payment Holds on Subcontractor Invoices with Procore Pay

For teams interested in managing payment requirements and payment holds:

- **Manage Payment Holds as a Payor**

  - [Create and Apply a Manual Hold on an Invoice](/process-guides/payor-setup-guide/create--apply-payment-holds)
  - [Edit a Manual Hold on an Invoice](/process-guides/invoice-administrator-guide/edit-holds)
  - [Release a Manual Hold on an Invoice](/process-guides/invoice-administrator-guide/release-holds)
- **Manage Payment Requirements**

  - As a payor:

    - [Configure Payment Requirements as a Payor](/process-guides/payor-setup-guide/configure-payment-requirements)
    - [View Payment Requirements on a Project Invoice as an Invoice Administrator](/process-guides/invoice-administrator-guide/view-requirements)
    - [View Payment Requirements as a Payor](/process-guides/payments-admin-guide/view-payment-requirements)
  - As a payee:

    - [View Payment Requirements as the Invoice Contact for a Payee](/product-manuals/procore-pay/tutorials/view-payment-requirements-as-the-invoice-contact-for-a-payee)