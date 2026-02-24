# Patient Payments Guide – Troubleshooting Stripe activation and connection issues

Source: https://help.elationhealth.com/s/article/Troubleshooting-Stripe-activation-and-connection-issues

---

# Contents

- [Overview](#overview)
 - [When to suspect a Stripe connection issue](#when-to-suspect-a-stripe-connection-issue)
- [Workflow Instructions](#workflow-instructions)
 - [Check your Stripe account from Elation](#check-your-stripe-account-from-elation)
 - [Review your Stripe account status](#review-your-stripe-account-status)
 - [Verify your Industry setting in your Stripe account (for HSA/FSA issues)](#verify-your-industry-setting-for-hsafsa-issues)
- [When to contact Elation Support](#when-to-contact-elation-support)
 - [How to contact Support](#how-to-contact-support)
 - [Information to provide](#information-to-provide)

# Overview

## When to suspect a Stripe connection issue

You may have a Stripe activation or connection issue if the Patient Payments feature is visible in Elation, but you experience any of the following:

- All payment charges fail.
- Stripe shows no issues, yet no transactions appear in Elation.
- Stripe shows issues (such as verification warnings or payout holds), but your staff are unaware because they have not checked the Stripe **Dashboard**.

# Workflow Instructions

Before contacting Elation Support, complete the following checks to identify and resolve common issues.

## Check your Stripe account from Elation

| | |
| --- | --- |
| 1 | Go to Settings → Patient Payments. |
| 2 | Click Go to Stripe account to open your Stripe Dashboard. |

## Review your Stripe account status

Once in the Stripe Dashboard, check for the following:

- **Pending verification tasks:** Stripe may require additional identity or business verification before you can process payments. Look for any alerts or banners prompting you to complete verification steps.
- **Payout holds:** Confirm there are no holds on your payouts. Stripe may pause payouts if verification is incomplete or if there are issues with your account.
- **Bank account information:** Verify that your bank account details (account and routing numbers) are correct and match the entity type you selected during setup.

## Verify your Industry setting in your Stripe account (for HSA/FSA issues)

If you are having trouble receiving FSA or HSA payments, confirm your Industry setting in Stripe account is set to "Doctors and Physicians":

| | |
| --- | --- |
| 1 | In your Patient Payments settings page in Elation, click Go to Stripe account. |
| 2 | In the Stripe Dashboard, locate and click Settings. |
| 3 | Scroll down to Professional details or Business details. |
| 4 | Click Edit to view the details. |
| 5 | When the Additional Information dialog window opens, click Edit to make changes. |
| 6 | Update your Industry to "Doctors and Physicians". |

# When to contact Elation Support

If you have completed the self-service checks above and are still experiencing issues, contact Elation Support for further assistance.

## How to contact Support

Use the I need help → Contact Elation Support button at the top of your Elation account.

## Information to provide

To help resolve your issue quickly, include the following details in your support request:

- **Practice name**
- **Patient example:** Patient name (or ID) and the date/time of the attempted charge.
- **Stripe charge ID(s):** If available, include any Stripe charge ID(s) from failed transactions.
- **Screenshots:** If you are able, any non-PHI screenshots of error messages or examples you can provide.

# Related Articles

- [Patient Payments Guide – Securely collect payments digitally from patients](using-elation-to-securely-collect-patient-payments.md)
- [Patient Payments – Frequently Asked Questions](Patient-Payments-Frequently-Asked-Questions.md)
- [How to register for Stripe account with Elation](https://docsend.com/view/u5pujrn5mrghwnkj)
- [Patient Payments Guide – Obtaining a 1099 Tax Form for your Stripe account](Patient-Payments-Guide-Obtaining-a-1099-Tax-Form-for-your-Stripe-account.md)