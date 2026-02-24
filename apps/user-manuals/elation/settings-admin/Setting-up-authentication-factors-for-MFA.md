# Multi-Factor Authentication Guide - Setting up authentication factors

Source: https://help.elationhealth.com/s/article/Setting-up-authentication-factors-for-MFA

---

📖 **RECOMMENDED READING**

[Click here to learn about the different types of authentication factors and what to consider before choosing and setting one up](https://help.elationemr.com/s/article/Multifactor-Authentication-MFA#options).

# **Contents**

- [Overview](#overview)
- [Workflow Instructions](#workflows)
 - [Setting up an Authenticator App (i.e. Google Authenticator)](#Auth_App)
    - [Setting up an Authenticator App by scanning a QR code](#Auth_App_QR)
    - [Setting up an Authentication App by entering a Key instead of scanning a QR code](#Auth_App_no_QR)
 - [Setting up Okta Verify](#Okta_Verify)
    - [Setting up Okta Verify by scanning a QR Code](#Okta_Verify)
    - [Setting up Okta Verify without scanning a QR code](#Okta_no_QR)
 - [Setting up a Security Key or Biometrics Authenticator](#Security_Key_Biometrics)
 - [Setting up Email Authentication](#Email)
- [Frequently Asked Questions (FAQ)](#FAQ)

ℹ️  **REQUIREMENT**

All Elation users are **required** to use multi-factor authentication for security and compliance purposes.

##

# **Overview**

With multi-factor authentication, every active user in the practice is required to set up at least one authentication factor by their next attempt to sign in to their Elation account.

- Users still logged in at the time MFA is enabled can set up an authentication factor by going to **Settings** -> **Account Details** and then clicking **Setup** next to **No active multi-factor authentication**.
 - If you already have an authentication factor set up, this button will be called **Edit factors**.
- Users who are not logged in at the time MFA is enabled will be prompted to set up an authentication factor during their next login.

ℹ️   **NOTE** You cannot share accounts while using multi-factor authentication. Shared, or generic, user accounts or passwords are strictly prohibited by [Elation's Terms of Use](https://www.elationhealth.com/terms-of-use/) and security policies. Individuals who use the EHR must log in using their own, unique account.



# **Workflow Instructions**

## **Setting up an Authenticator App (i.e. Google Authenticator)**

### **Setting up an Authenticator App by scanning a QR code**

To use an Authenticator App such as Google Authenticator as your authentication factor, link the app to your Elation account by following the steps below. The setup process is generally the same for most authenticator apps. We'll use Google Authenticator as an example.

| | |
| --- | --- |
| **1** | Click **Setup** next to the Authenticator App option in Elation. A QR Code will appear for you to use in Step #3.   1. If you are setting up Google Authenticator from the Elation login screen, click **Setup** and then select your device type by clicking either **iPhone** or **Android**. 2. Click **Next**. A QR Code will appear. Keep this screen on and QR code visible for Step #3. |
| **2** | **(As needed)** Install/download the Google Authenticator app on your mobile device if you do not have the app yet. Proceed to step #3 if you already have the app installed.   - Install via the App Store if you are using an iPhone. - Install via the Google Play Store if you are using an Android device. |
| **3** | Link your Elation account to the Google Authenticator app by using your device’s camera to scan the QR Code on your Elation screen.   1. Open the Google Authenticator app on your mobile device. 2. Press **Get started**. 3. Specify if you want to use Google Authenticator with your Google account or without an account.    - Press **Continue as …** if you want to use your Google account.    - Press **Use without an account** if you don’t want to use your Google account. 4. Press the **+** button at the bottom right of the Google Authenticator app to add a new software application. 5. Press **Scan a QR Code** and then point your device’s camera at the QR Code that appears in Elation to scan it.    1. [See the instructions below if you are unable to scan the QR code.](#Auth_App_no_QR) 6. Your Elation account will now appear in Google Authenticator. 7. Go back to your Elation screen and click **Next**. 8. In the **Enter Code** box on your Elation screen, enter the **6 digit number** from your Google Authenticator app and then click **Verify**.    - The 6 digit number will change every 30 seconds. Always enter the numbers that appear most recently in the Google Authenticator app. |
| **4** | You have successfully set up Google Authenticator for multi-factor authentication. If you are completing the setup while logging in to Elation, click **Finish** to proceed to the Practice Home. |

### **Setting up an Authentication App by entering a Key instead of scanning a QR code**

Click here for instructions on how to set up an Authentication App without using a QR code.

This option is only available when completing the Authentication App set up from the login screen.

| | |
| --- | --- |
| **1** | Login to Elation. |
| **2** | Click **Setup** next to the Google Authenticator option. |
| **3** | A QR Code will appear. Click **Can’t scan?** to see a Key instead. |
| **4** | Open the Google Authenticator app on your mobile device. |
| **5** | Press **Get started**. |
| **6** | Specify if you want to use Google Authenticator with your Google account or without an account.   - Press **Continue as …** if you want to use your Google account. - Press **Use without an account** if you don’t want to use your Google account. |
| **7** | Press the **+** button at the bottom right of the Google Authenticator app to add a new software application. |
| **8** | Press **Enter a setup key**. |
| **9** | Enter an **Account name** that will help you identify the account (i.e. ‘Elation’). |
| **10** | Enter the series of letters and numbers that you see on your Elation screen in the **Your key** field. |
| **11** | Leave the **Type of key** field as **Time based**. |
| **12** | Press **Add**. |
| **13** | Your Elation account will now appear in Google Authenticator. |
| **14** | Go back to your Elation screen and click **Next**. |
| **15** | In the **Enter Code** box on your Elation screen, enter the **6 digit number** from your Google Authenticator app and then click **Verify**.   - The 6 digit number will change every 30 seconds. Always enter the numbers that appear most recently in the Google Authenticator app. |
| **16** | You have successfully set up Google Authenticator for multi-factor authentication. Click **Finish** to proceed to the Practice Home. |

##

## **Setting up Okta Verify**

### **Setting up Okta Verify by scanning a QR Code**

| | |
| --- | --- |
| **1** | Click **Setup** next to the Okta Verify option. A QR Code will appear for you to use in Step #3.   - If you are setting up Okta Verify from the Elation login screen, click **Setup** and then select your device type by clicking either **iPhone** or **Android**. - Click **Next**. A QR Code will appear. Keep this screen on and QR code visible for Step #3. |
| **2** | **(As needed)** Install/download the Okta Verify app on your mobile device if you do not have the app yet. Proceed to step #3 if you already have the app installed.   - Install via the App Store if you are using an iPhone. - Install via the Google Play Store if you are using an Android device. |
| **3** | Link your Elation account to the Okta Verify app by using your device’s camera to scan the QR Code on your Elation screen.   1. Open the Okta Verify app on your mobile device. 2. Press **Add Account** in your Okta Verify app. 3. Press **Other**. 4. Press **Scan QR Code** and then point your device’s camera at the QR Code that appears in Elation to scan it.    1. [See the instructions below if you are unable to scan the QR code.](#Okta_no_QR) 5. You will see a confirmation on your screen that says “Account Added”. Click **Done** to close the notification. |
| **4** | You have successfully set up Okta Verify for multi-factor authentication. If you are completing the setup while logging in to Elation, click **Finish** to proceed to the Practice Home. |

###

###

### **Setting up Okta Verify without scanning a QR code**

Click here for instructions on how to set up Okta Verify without using a QR code.

This option is only available when completing the Okta Verify set up from the login screen.

| | |
| --- | --- |
| 1 | Login to Elation. |
| 2 | Click **Setup** next to the Okta Verify option. |
| 3 | A QR Code will appear. Click **Can’t scan?**. |
| 4 | Choose the technique you want to use to set up Okta Verify:   1. Use an activation link sent via SMS to a specified mobile phone number.    1. Select **Send activation link via SMS**.    2. Enter a phone number and then click **Send**.    3. Look for an SMS from Elation with an activation link.    4. Press on the activation link.    5. You will see a confirmation in Okta Verify that says “Account Added”. Click **Done** to close the notification.    6. Use an activation link sent via email to your Elation login email address. 2. Select **Send activation link via email**.    1. Click **Send** and look for an email from Elation with an activation link.    2. Click on the activation link.    3. You will see a confirmation in Okta Verify that says “Account Added”. Click **Done** to close the notification. 3. Use a Key that you manually input in the Okta Verify App.    1. Select **Set up manually without push notification**. A series of letters and numbers will appear on your Elation screen. You will use this in step g below.    2. Open the Okta Verify app on your mobile device.    3. Press **Add Account** in your Okta Verify app.    4. Press **Other**.    5. Press **Enter Key Manually**.    6. Enter an **Account Name** that will help you identify the account (i.e. ‘Elation’).    7. Enter the series of letters and numbers that you see on your Elation screen in the **Key** field.    8. Go back to your Elation screen and click **Next**.    9. In the **Enter Code** box on your Elation screen, enter the **6 digit number** from Okta Verify and then click **Verify**.       - The **6 digit number** will change every 30 seconds. Always enter the numbers that appear most recently in the Okta Verify app.    10. You will see a confirmation in Okta Verify that says “Account Added”. Click **Done** to close the notification. |
| 5 | You have successfully set up Okta Verify for multi-factor authentication. Click **Finish** to proceed to the Practice Home. |

## **Setting up a Security Key or Biometrics Authenticator**

Only use a Security Key or Biometric Authenticator as your authentication factor if you use a single, personal device to access Elation. We recommend setting up a second authentication factor as backup in case you may need to access Elation on a secondary device.

To set up a Security Key or Biometric Authenticator (i.e. password manager, Windows Hello, Face ID, Touch ID, etc):

| | |
| --- | --- |
| **1** | Go to **Settings** -> **Account Details** |
| **2** | Click **Setup** next to **No active multi-factor authentication**.   - If you already have an authentication factor set up then this button will be called **Edit factors**. |
| **3** | Click **Setup** next to the Security Key or Biometric Authenticator option. |
| **4** | Click **Enroll**. |
| **5** | Follow the on-screen prompts to set up a Security Key or Biometric Authenticator. |

ℹ️  **NOTE**

Detailed instructions are unavailable for this setup process as the exact workflows depend on your browser, enabled browser extensions, your computer’s operating system, and available hardware keys. For this reason, Elation will not be able to troubleshoot issues around this authentication factor. Only select this authentication option if you are familiar with this type of authentication factor and are comfortable resolving potential issues on your own.

## **Setting up Email Authentication**

**Email Authentication can only be set from the Elation login screen AND if you don’t have any other types of factors set up yet.**

**💡**  **USER TIP**

Email Authentication is the least secure authentication factor. Only use Email Authentication if you are unable to use other authentication factors.

To set up Email Authentication:

| | |
| --- | --- |
| **1** | Login to Elation. |
| **2** | Click **Setup** next to the Email Authentication option. |
| **3** | Click **Send me a code**. Elation will send a verification code to the email address you use to log in to Elation. |
| **4** | Look for an email with the subject line **Confirm your email address**. |
| **5** | Enter the **6 digit number** from the email into the **Verification code** box on your Elation screen. |
| **6** | Click **Verify**. |
| **7** | You have successfully set up Email Authentication for multi-factor authentication. If you are completing the setup while logging in to Elation, click **Finish** to proceed to the Practice Home. |

# **Frequently Asked Questions (FAQ)**

[Click here for answers to common MFA questions—including troubleshooting login issues, choosing authentication factors, and more](Multi-Factor-Authentication-FAQ.md).

# **Related Articles**

- [Multi-Factor Authentication Introduction](Multifactor-Authentication-MFA.md)
- [Multi-Factor Authentication Guide - Updating authentication factors](Updating-authentication-factors-for-MFA.md)
- [Multi-Factor Authentication Guide - Resetting authentication factors](Resetting-authentication-factors-for-MFA.md)
- [Multi-Factor Authentication Guide - Frequently Asked Questions](Multi-Factor-Authentication-FAQ.md)