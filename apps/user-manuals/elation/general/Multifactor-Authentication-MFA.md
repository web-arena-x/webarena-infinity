# Multi-Factor Authentication Introduction

Source: https://help.elationhealth.com/s/article/Multifactor-Authentication-MFA

---

# Contents

- [Overview](#overview)
 - [What is multi-factor authentication (MFA)?](#description)
 - [What are the benefits of using multi-factor authentication with Elation?](#description)
 - [Which authentication factors are available for Elation?](#options)
- [Set-up](#setup)
 - [Enabling multi-factor authentication for the practice](#enable_MFA)
 - [Setting up authentication factors](#setting_up_MFA)
- [Workflow Instructions](#workflows)
 - [Signing in with multi-factor authentication](#signing_in_with_MFA)
 - [Updating authentication factors](#updating_MFA)
 - [Resetting authentication factors (if locked out)](#resetting_MFA)
- [Frequently Asked Questions (FAQ)](#FAQ)

ℹ️   **REQUIREMENT** All Elation EHR users are **required** to use multi-factor authentication for security and compliance purposes.

# Overview

## What is multi-factor authentication (MFA)?

Multi-factor authentication (MFA) is a security process that requires two or more verification methods to access an application or online account.

Elation's multi-factor authentication feature requires all users to enter their login email address and password as the first authentication method and at least one additional authentication factor in order to access their Elation EHR account.

**ℹ️ FOR PRACTICE ADMINS** You are the first line of support for MFA and login issues at your organization. From Settings → Manage Accounts, you can unlock accounts and reset multi-factor authentication for your users. Contact Elation Support only if your practice has no active admin or an admin cannot access Manage Accounts.

## What are the benefits of using multi-factor authentication with Elation?

Multi-factor authentication significantly lowers the risk of unauthorized accessto sensitive patient data, supporting ongoing HIPAA compliance. Multi-factor authentication helps prevent cyber attackers from accessing your account by requiring both your login credentials and a verification factor—something they are unlikely to have, even during phishing attempts.

## Which authentication factors are available for Elation?

There are currently 4 authentication factors you can use. Choose the authentication factor that is most suitable for your workflows. You are only required to set-up one of these, but we recommend setting up additional factors. This way you have a back up in case one becomes compromised or you run into issues using one of your authentication factors.

| Authentication Factor | Verification Method | Use Case | Additional Considerations |
| --- | --- | --- | --- |
| Authenticator App (i.e. Google Authenticator, Windows Authenticator, Authy, etc.). [Click here for additional examples](#authenticator_apps). | Enter a code that is generated from a mobile app. | • You always carry a mobile device (e.g. your phone) with you. • You share computers with other users in your practice. | Default option for most. • You must have a smart phone or tablet. • You can be locked out if your phone is lost or misplaced. • Can be used across devices. |
| Okta Verify | Enter a code that is generated from the Okta Verify mobile app OR send a push notification to the Okta Verify mobile app. | • You always carry a mobile device (e.g. your phone) with you. • You share computers with other users in your practice. | • You must have a smart phone or tablet. • You can be locked out if your phone is lost or misplaced. • Can be used across devices. • Ideal option if your company/business uses Okta to manage the accounts you have access to. |
| Security Key or Biometric Authenticator (i.e. password manager, Touch ID, Face ID, Windows Hello, etc.) [Click here for additional examples](#Security_Keys_Biometric_Authenticators). | Use a key stored on your computer/laptop OR a biometrics reader that is connected to your computer/laptop. | You access Elation on a single, personal device. | • Not suitable if you are working in multiple environments (e.g. home & office) on different devices. • Can be more complex to set up. Recommendation: Set up an additional authentication factor in case you need to access Elation on a different device. |
| Email Authentication | Enter a code sent to your login email address. | You are unable to use other authentication factors. | Not recommended. Least secure. • You can only set up Email Authentication when setting up authentication factors for the **first time** through the login screen workflow. • If you are using Email Authentication as a backup, set up Email Authentication first. • You will be unable to login if the verification code email is blocked by your IT or spam filters. |

SMS or phone calls are not supported by Elation due to known vulnerabilities (e.g. SIM Swapping & phishing).

For guidance on shared logins and protecting your devices, see [Best practices for keeping your Elation account secure](Best-practices-for-keeping-your-Elation-account-secure.md).

# Set-up

## Enabling multi-factor authentication for the practice

Multi-factor authentication is automatically enabled for every practice.

## Setting up authentication factors

[Click here for instructions on how to set up authentication factors](Setting-up-authentication-factors-for-MFA.md).

# Workflow Instructions

ℹ️   **NOTE** You cannot share accounts while using multi-factor authentication. Shared, or generic, user accounts or passwords are strictly prohibited by [Elation's Terms of Use](https://www.elationhealth.com/terms-of-use/) and security policies. Individuals who use the EHR must log in using their own, unique account.

## Signing in with multi-factor authentication

With multi-factor authentication, each time you log in to your Elation EHR account, you will be prompted to enter your login email address, password, and your authentication factor before you are granted access to your account.

- If you have multiple authentication factors, click the ⏷ button to select the authentication factor you want to use.
- Check off the Do not challenge me on this device for the next 24 hours box on the authentication screen if you want to bypass multi-factor authentication while logging in and out of Elation for the next 24 hours in that browser and device.

| | |
| --- | --- |
| Authenticator App \* If you use an authenticator app other than Google Authenticator, you can still enter its code when prompted for a Google Authenticator code during login. | • Enter your Elation login email address and password and then click Sign In. • Enter the 6 digit number that appears on your Google Authenticator app in the Enter Code field. • Click Verify to complete authentication and proceed to the Practice Home. |
| Okta Verify | • Enter your Elation login email address and password and then click Sign In. • Click Send Push to send a notification to your Okta Verify app for you to confirm your identity. • Alternatively click Or enter code to enter the 6 digit number that appears on your Okta Verify app in the Enter Code field. • Click Verify to complete authentication and proceed to the Practice Home. |
| Security Key or Biometrics Authentication | • Enter your Elation login email address and password and then click Sign In. • Follow the prompts on your screen to verify your identity and proceed to the Practice Home. Examples: |
| Email | • Enter your Elation login email address and password and then click Sign In. • Click Send me a code. Elation will send a verification code to the email address you use to log in to Elation. • Look for an email with the subject line One-time verification code. • Enter the 6 digit number from the email into the Verification code box. • Click Verify to complete authentication and proceed to the Practice Home. |

## Updating authentication factors

[Click here for instructions on updating authentication factors](Updating-authentication-factors-for-MFA.md).

## Resetting authentication factors (if locked out)

[Click here for instructions on resetting authentication factors if you are locked out of Elation](Resetting-authentication-factors-for-MFA.md).

# Frequently Asked Questions (FAQ)

[Click here for answers to common MFA questions—including troubleshooting login issues, choosing authentication factors, and more—see our dedicated](Multi-Factor-Authentication-FAQ.md).

# Related Articles

- [Multi-Factor Authentication Guide - Frequently Asked Questions](Multi-Factor-Authentication-FAQ.md)
- [Multi-Factor Authentication Guide - Setting up authentication factors](https://help.elationemr.com/s/article/Setting-up-authentication-factors-for-MFA)
- [Multi-Factor Authentication Guide - Updating authentication factors](https://help.elationemr.com/s/article/Updating-authentication-factors-for-MFA)
- [Multi-Factor Authentication Guide - Resetting authentication factors](https://help.elationemr.com/s/article/Resetting-authentication-factors-for-MFA)
- [Multi-Factor Authentication - Quick Start Guide](https://help.elationemr.com/s/article/Multi-Factor-Authentication-Quick-Start-Guide)
- [User Accounts Guide – Managing Elation accounts for providers and staff](https://help.elationemr.com/s/article/managing-user-accounts)
- [User Accounts Guide – Using Single Sign-On to access your Elation EHR account](https://help.elationemr.com/s/article/single-sign-on)