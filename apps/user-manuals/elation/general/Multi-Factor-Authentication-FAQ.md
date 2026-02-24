# Multi-Factor Authentication Guide - Frequently Asked Questions

Source: https://help.elationhealth.com/s/article/Multi-Factor-Authentication-FAQ

---

This FAQ walks through real-world MFA situations and how to handle them safely. For an overview of MFA concepts and factor types, see [Multi-Factor Authentication Introduction](Multifactor-Authentication-MFA.md).

# Contents

- [Getting Started](#getting-started)
- [Account Lockout and Login Issues](#lockout)
- [Authentication Factor Types and Compatibility](#factor-types)
- [Email Authentication](#email-auth)
- [Login Behavior and Sessions](#login-behavior)
- [Scribes, SSO, and Shared Accounts](#shared-accounts)
- [Patient Passport](#patient-passport)

# Getting Started

## Does the entire practice need to enroll in multi-factor authentication at the same time?

Each user must independently set up an authentication factor but it does not have to be done at the same time.

## How do I update my authentication factor(s)?

[Click here for instructions on updating authentication factors](Updating-authentication-factors-for-MFA.md).

# Account Lockout and Login Issues

## I am not able to sign in to Elation to reset my authentication factor. What should I do?

If you find yourself locked out, **ask an Admin Level User in your practice to reset your authentication factors for you** in the [Manage Accounts](https://app.elationemr.com/settings/allaccounts/) settings page ([click here for instructions](Resetting-authentication-factors-for-MFA.md)). If you are the sole administrator of an Elation practice, [click here](https://app.elationemr.com/support/) to contact the Support Team. We will send you an email to verify your identity and reset your authentication factor(s) on your behalf.

**💡**  **USER TIP** After you have successfully logged in, set up additional authentication factors as back up in case this happens again.

## I set up an authentication factor but cannot log in to my Elation account, what should I do?

If you find yourself locked out, **ask an Admin Level User in your practice to reset your authentication factors for you** in the [Manage Accounts](https://app.elationemr.com/settings/allaccounts/) settings page ([click here for instructions](Resetting-authentication-factors-for-MFA.md)).

For security reasons, Admin Level Users are responsible for resetting authentication factors for their practice; Elation will not readily do so on a user's behalf. If you are the sole administrator of an Elation practice, [click here](https://app.elationemr.com/support/) to contact the Support Team. We will send you an email to verify your identity and reset your authentication factor(s) on your behalf.

**💡**  **USER TIP** After you have successfully logged in, set up additional authentication factors as back up in case this happens again.

## I lost my phone or got a new phone. What should I do?

If you can no longer access the device you used for MFA (for example, you lost your phone or replaced it with a new one), you will need to reset your MFA factors and set them up again.

### Step 1: Contact your practice admin first

Your practice admin is your first line of support for MFA and login issues. They can:

- Reset your MFA from Settings → Manage Accounts → Reset multi-factor so you can enroll new factors.
- Confirm that your user account is active and not disabled.

If your practice does not have an active admin, or your admin cannot access Manage Accounts, please contact Elation Support.

### Step 2: Re‑enroll MFA on your new device

After your admin resets MFA:

| | |
| --- | --- |
| 1 | Sign in - Sign in to Elation with your username and password. |
| 2 | Set up factors - Follow the prompts to set up at least one **reusable factor**, such as:   - An authenticator app (recommended), and/or - Email verification codes. |
| 3 | Avoid single-device factors - Avoid relying on only device‑bound factors (for example, Touch ID/Face ID or platform security keys) on a single device, since those do not transfer automatically when you change devices. |

**USER TIP** We strongly recommend configuring **at least two factors** so you have a backup if you lose access to one.

# Authentication Factor Types and Compatibility

## Which Authenticator Apps can I use?

Any Authenticator App that uses the same TOTP (Time-Based One-Time Password) algorithm as Google Authenticator can be used. Common TOTP Apps include:

- Google Authenticator
- Microsoft Authenticator
- Symantec VIP Access (mobile app)
- Authy
- Duo Mobile
- 1Password (with integrated TOTP support)
- LastPass Authenticator
- FreeOTP
- andOTP
- OTP Auth

## Which Security Keys and Biometric Authenticators can I use?

Any software or hardware that verifies your identity using public-key cryptography can be used. Common examples include:

- Password managers that store a Security Key (e.g. 1Password, LastPass, etc.)
- Windows Hello (pin)
- YubiKey
- Feitian ePass / K27 / BioPass
- Google Titan Security Key
- SoloKey
- Thetis FIDO U2F Key
- OnlyKey
- MacBook Touch ID
- Apple Face ID
- Windows Hello fingerprint
- Windows Hello Face
- USB fingerprint readers

## Can I use SMS as an authentication factor?

Security research has shown that SMS is less secure than other authentication factors. It is possible for your cell phone number to be compromised in a "SIM Swap" attack, where a bad actor tricks your carrier to port over your phone number to them. When a bad actor has access to your phone number, they can then receive the security codes used for multi-factor authentication, increasing their chances of successfully gaining unauthorized access to your account. As a result, Elation decided to only support other more secure factors for multi-factor authentication.

## Can I set up more than one authentication factor for a single account?

Yes, you can set up more than one authentication factor for a single account and this is recommended practice. Note that you can only set up one of each type of factor (e.g. one Authenticator App, one Security Key). You can follow [these instructions](Multifactor-Authentication-MFA.md#options) to learn how to choose which factor you want to use when logging in.

## Can I log in to my account from different devices using a single authentication factor?

You can log in to your account from different devices using a single authentication factor if the authentication factor is not a Security Key or Biometric Authenticator as those are typically device specific. If you want to use a Security Key or Biometric Authenticator when logging in through your computer set up an additional authentication factor like Google Authenticator for logging in through other devices.

## I use Elation on multiple computers and my phone. Which MFA factors should I choose?

If you regularly access Elation from more than one device (for example, a work desktop, a laptop, and your phone), choose factors that are easy to use across all of them.

### Recommended setup

- Primary factor: An authenticator app on your mobile device.
- Backup factor: Email verification codes.

This combination:

- Works on any browser where you can enter a one‑time code.
- Avoids getting locked into a single device's built‑in biometric or security hardware.

You can also enable device‑specific options like Touch ID/Face ID on trusted devices. Remember:

- Some factors (for example, platform biometrics and certain security keys) are **device‑specific** and will not automatically work on another computer.
- The "remember this device" or "keep me signed in" behavior only applies to the specific device and browser where you chose it, and for a limited period of time.

For more details on factor types and timeouts, see [Multi-Factor Authentication Introduction](Multifactor-Authentication-MFA.md).

# Email Authentication

## If I choose to use Email Authentication, do I have to use the email address associated with my Elation account?

Yes, when using the Email Authentication option for multi-factor authentication, the email account must be the email address you use to log in to your Elation account.

To use a different email for Email Authentication, update your login email address from your Account Details Settings page in Elation first.

## Why am I unable to set up Email Authentication from my Elation Settings?

Email Authentication is deemed as the least secure authentication method; therefore, we want you to set up a more secure authentication factor when possible. However, if Email Authentication is the only authentication factor you can use, log out of your Elation account and you'll be able to set up Email Authentication from the login screen.

## I am setting up Email Authentication but I have not received the email with my Verification Code, what should I do?

The Verification Code can take a few minutes to arrive in your email inbox. If you've waited a few minutes and still do not see the email with the Verification Code, click Send again on the verify screen in Elation to prompt Elation to email the code to you again. If you continue to not receive the email, [click here](https://app.elationemr.com/support/) to contact the Support Team.

# Login Behavior and Sessions

## Why is Elation automatically logging me out even when I checked the 24 hour box?

MFA login must still comply with your device's and browser's security as well as Elation's timeout policy.

- The 24-hour MFA bypass is tied to **both your device and the browser** that was in use at the time you signed in.
 - If log in from a different device, switch browsers, or use an incognito/private window, Elation will ask for your MFA again for security reasons- **even if the 24-hour box was checked.**
- The bypass does not override Elation's **session timeout policy**.
 - If you are logged out due to inactivity (the standard timeout is 2 hours), you will be asked to re-authenticate when logging back in- **even if the 24-hour box was checked.**

For higher‑risk workflows (e.g., multiple staff working on the same visit note, stepping away from computer, etc.), it's still best practice to explicitly click Save as Draft & Close in your visit note to reduce any chance of data conflicts or loss.

## How often do I have to re-authenticate when using multi-factor authentication to log in?

By default, you are required to re-authenticate each time you log in. Check off the Do not challenge me on this device for the next 24 hours box if you want to bypass multi-factor authentication while logging in and out of Elation for the next 24 hours for that browser and device.

If your account is logged out due to inactivity, you'll need to re-authenticate unless you previously chose to skip authentication for 24 hours and that time hasn't fully elapsed.

## Will multi-factor authentication still allow me to be logged in to multiple places at the same time?

Yes, you can still be logged in to multiple places at the same time.

## Will I need to use my authentication factor when logging in to Elation Go (Elation's mobile application)?

Yes, you will need to use your authentication factor when logging in to Elation Go. This is great use case for setting up multiple authentication factors, especially if you are using a Security Key or Biometric Authenticator when logging in through your computer - these will not work on your phone. Setting up an additional authentication factor like Google Authenticator will allow you to login to Elation Go on your phone.

# Scribes, SSO, and Shared Accounts

## My scribe needs to login to complete my visit notes daily. How do I give them access to my authentication factor?

You cannot share accounts while using multi-factor authentication. It's important to highlight that shared, or generic, user accounts or passwords are strictly prohibited by [Elation's Terms of Use](https://www.elationhealth.com/terms-of-use/) and security policies. Individuals who use the EHR must log in using their own, unique account.

## My scribe can't log in. How should we set up MFA for scribes?

Each person who documents or works in Elation must use **their own user account** with their own MFA factors. Shared logins are not permitted for security and compliance reasons.

### Recommended pattern

- Scribes should have staff-level accounts tied to the supervising clinician, with appropriate permissions configured by a practice admin. For more about provider vs staff capabilities, see [Provider vs staff level account privileges](User-Accounts-Guide-Provider-vs-staff-level-account-privileges.md).
- Scribes set up MFA on their own accounts, just like any other user.

### If a scribe cannot log in

| | |
| --- | --- |
| 1 | Verify credentials - Confirm they are using **their own username and password**, not the clinician's. |
| 2 | Admin assistance - Ask the practice admin to:    - Confirm that the staff account is active (not disabled), and - Reset the user's MFA from Settings → Manage Accounts if needed. |
| 3 | Contact Support - If your practice has no active admin or your admin cannot perform these steps, contact Elation Support. |

For additional security guidance, see [Best practices for keeping your Elation account secure](Best-practices-for-keeping-your-Elation-account-secure.md).

## Can I use the single sign-on feature with multi-factor authentication?

If your organization uses its own single sign-on (SSO) provider to access Elation, all the security—like checking your password and asking for a verification code—is already handled by your company. As a result, you will not be required to use Elation's built-in MFA feature.

Learn more about the Single Sign-On feature through our [User Accounts Guide – Using Single Sign-On to access your Elation EHR account](https://help.elationemr.com/s/article/single-sign-on) Help Center article.

# Patient Passport

## Will patients need to use multi-factor authentication for their Patient Passport account?

No, patients will not need to use multi-factor authentication for their Patient Passport account.

# Related Articles

- [Multi-Factor Authentication Introduction](Multifactor-Authentication-MFA.md)
- [Multi-Factor Authentication - Setting up authentication factors](Setting-up-authentication-factors-for-MFA.md)
- [Multi-Factor Authentication - Updating authentication factors](Updating-authentication-factors-for-MFA.md)
- [Multi-Factor Authentication - Resetting authentication factors](Resetting-authentication-factors-for-MFA.md)
- [Multi-Factor Authentication - Quick Start Guide](Multi-Factor-Authentication-Quick-Start-Guide.md)
- [Provider vs staff level account privileges](User-Accounts-Guide-Provider-vs-staff-level-account-privileges.md)
- [Best practices for keeping your Elation account secure](Best-practices-for-keeping-your-Elation-account-secure.md)