# Multi-Factor Authentication Guide - Quick Start Guide

Source: https://help.elationhealth.com/s/article/Multi-Factor-Authentication-Quick-Start-Guide

---

# **Contents**

- [What is Elation's multi-factor authentication (MFA) feature?](#description)
- [What are the benefits of using multi-factor authentication with Elation?](#benefits)
- [Who does what for multi-factor authentication?](#responsibilities)
- [Comparing authentication factors](#authentication_factors)
- [Setting up multi-factor authentication](#set_up_factors)
- [Signing in with multi-factor authentication](#signing_in)
- [Resetting authentication factors (if locked out)](#reset)

Click here for a breakdown of the different chapters in this video.

- 00:06 - Who needs MFA?
- 00:25 - MFA Overview
- 01:05 - Login Workflow
- 02:47 - Roles & Responsibilities
- 03:55 - Comparison of Authentication Factors
- 05:06 - Setup from Settings
- 05:46 - Setup From Login Screen

# **What is Elation's multi-factor authentication (MFA) feature?**

Elation's multi-factor authentication feature requires all users to enter their login email address and password as the first authentication method and at least one additional authentication factor in order to access their Elation EHR account.

To comply with proposed cybersecurity guidelines from the U.S. Department of Health and Human Services, follow security best practices, address the growing threat of cyber attacks and protect your patient’s data, Elation requires all users to use either multi-factor authentication or [single sign-on](https://help.elationemr.com/s/article/single-sign-on).

# **What are the benefits of using multi-factor authentication with Elation?**

Multi-factor authentication significantly lowers the risk of unauthorized access to sensitive patient data, supporting ongoing HIPAA compliance. Multi-factor authentication helps prevent cyber attackers from accessing your account by requiring both your login credentials and a verification factor—something they are unlikely to have, even during phishing attempts.

# **Who does what for multi-factor authentication?**

Here’s how responsibilities are shared when it comes to multi-factor authentication at your practice:

| **Everyone** | **Admin Level Users** |
| --- | --- |
| **Each user** must set up their own authentication factor(s) under their  Account Settings.   - Set up **multiple authentication methods** even though only one is required. - Choose the authentication methods you are most familiar with that are most suitable for your workflows. | **Admin Level Users** can maintain the use of multi-factor authentication for the entire practice by resetting authentication factors for users who are logged out. If an Admin Level User is unavailable, contact Elation. |

# **Comparing authentication factors**

Choose from four types of authentication factors for multi-factor authentication. While only one is required, we recommend setting up **multiple** options so you have a backup if one becomes unavailable.

| | | | |
| --- | --- | --- | --- |
| **Authentication Factor** | **Verification Method** | **Use Case** | **Additional Considerations** |
| **Authenticator App**   (i.e. Google Authenticator, Windows Authenticator, Authy, etc.). [Click here for additional examples](https://help.elationemr.com/s/article/Multifactor-Authentication-MFA#authenticator_apps). | Enter a code that is generated from a mobile app. | - You always carry a mobile device (e.g. your phone) with you. - You share computers with other users in your practice. | - **Default option for most.** - You must have a smart phone or tablet. - You can be locked out if your phone is lost or misplaced. - Can be used across devices. |
| **Okta Verify** | Enter a code that is generated from the Okta Verify mobile app **OR** send a push notification to the Okta Verify mobile app. | - You always carry a mobile device (e.g. your phone) with you. - You share computers with other users in your practice. | - You must have a smart phone or tablet. - You can be locked out if your phone is lost or misplaced. - Can be used across devices. - Ideal option if your company/business uses Okta to manage the accounts you have access to. |
| **Security Key or Biometric Authenticator**   (i.e. password manager, Touch ID, Face ID, Windows Hello, etc.) [Click here for additional examples](https://help.elationemr.com/s/article/Multifactor-Authentication-MFA#Security_Keys_Biometric_Authenticators). | Use a key stored on your computer/laptop **OR** a biometrics reader that is connected to your computer/laptop. | You access Elation on a single, personal device. | - Not suitable if you are working in multiple environments (e.g. home & office) on different devices. - Can be more complex to set up.   **Recommendation**: Set up an additional authentication factor in case you need to access Elation on a different device. |
| **Email Authentication** | Enter a code sent to your login email address. | You are unable to use other authentication factors. | - **Least secure.** - You can only set up Email Authentication when setting up authentication factors for the **first time** through the login screen workflow. - If you are using Email Authentication as a backup, set up Email Authentication first. - Verification code email can be blocked by IT or spam filters. |

# **Setting up your own authentication factors**

Each user in the practice should set up their own authentication factors. [Click here for step by step instructions](https://help.elationemr.com/s/article/Setting-up-authentication-factors-for-MFA).

# **Signing in with multi-factor authentication**

With multi-factor authentication, each time you log in to your Elation EHR account, you will be prompted to enter your login email address, password, and your authentication factor before you are granted access to your account.

- If you have multiple authentication factors, click the  ⏷  button to select the authentication factor you want to use.
- Check off the **Do not challenge me on this device for the next 24 hours** box on the authentication screen if you want to bypass multi-factor authentication while logging in and out of Elation for the next 24 hours for that browser and device.

[Click here for more information about signing in](https://help.elationemr.com/s/article/Multifactor-Authentication-MFA#signing_in_with_MFA).

# **Resetting authentication factors (if locked out)**

If you find yourself locked out, **ask an Admin Level User in your practice to reset your authentication factors for you** by clicking **Reset Multi-factor** next to your name in the [Manage Accounts](https://app.elationemr.com/settings/allaccounts/) settings page. If you are the sole administrator of an Elation practice, [click here](https://app.elationemr.com/support/) to contact the Support Team. We will send you an email to verify your identity and reset your authentication factor(s) on your behalf.

# **Related Articles**

- [Multi-Factor Authentication Introduction](Multifactor-Authentication-MFA.md)
- [Multi-Factor Authentication Guide - Setting up authentication factors](Setting-up-authentication-factors-for-MFA.md)
- [Multi-Factor Authentication Guide - Updating authentication factors](Updating-authentication-factors-for-MFA.md)
- [Multi-Factor Authentication Guide - Resetting authentication factors](Resetting-authentication-factors-for-MFA.md)
- [Multi-Factor Authentication Guide - Frequently Asked Questions](Multi-Factor-Authentication-FAQ.md)
- [User Accounts Guide- Managing Elation accounts for providers and staff](managing-user-accounts.md)
- [User Accounts Guide- Using Single-Sign On to access your Elation EHR account](single-sign-on.md)