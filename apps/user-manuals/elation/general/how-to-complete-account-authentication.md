# User Accounts Guide- Setting up Elation EHR accounts and Provider account authentication

Source: https://help.elationhealth.com/s/article/how-to-complete-account-authentication

---

The Elation Team is excited to welcome you to our user community! Please complete your account details to fully set up your new Elation EHR account.

## **Contents**

- [What is EHR Account Setup?](#EHR_account_setup)
- [How to complete EHR Account Setup](#account_setup_process)
- [What is Provider Level User Account Authentication?](#WhatIsAccountAuthentication)
- [Why is Account Authentication required for Provider Level Users?](#WhyIsItImportant)
- [How Provider Level Users complete Account Authentication](#CompleteAccountAuthentication)
- [Profile Level User Profile Fields](#provider_fields)
 - [Account Details](#account_details)
 - [Credentials](#credentials)
 - [Authentication Documents](#authentication_documents)
 - [Electronic Signature](#electronic_signature)
 - [Lab Identifiers](#lab_identifiers)
- [Staff Level User Profile Fields](#staff_fields)

## **What is EHR Account Setup?**

All users must set up a password for their Elation EHR account in order to gain access to their EHR account. In addition to creating a password, [Provider Level Users](User-Accounts-Guide-Provider-vs-staff-level-account-privileges.md) must also complete account authentication, verify their credentials and set up their electronic signature.



## **How to complete EHR Account Setup**

**Important Note**: A small subset of customers may still be seeing the legacy EHR Account Setup workflow. Both workflows will allow you to register for an Elation Account. If you have any questions about the experience you are seeing, [click here to contact Elation Support](https://help.elationhealth.com/s/contactsupport).




To complete EHR account Set Up:

1. Go to your email inbox and look for an email from '[sysadmin@elationemr.com](mailto:sysadmin@elationemr.com)' with the Subject Line *‘Welcome to Elation! Quickly complete your account setup.'*

*​​​​​​*![]()

1. Click the “Get Started” button in the body of the email.
2. Choose a password for your account and enter it in the **Password** field. The requirements for your password are as follows:
   - At least 12 characters long
   - At least 1 capital letter (uppercase letter)
   - At least 1 number
   - At least of the following special characters @ # \* ( ) + = { } / ? ~ ; , . - \_

![]()

1. Re-enter the same password in the **Retype Password** field.
2. Click “Set Password” to complete account set up.
3. **[PROVIDER LEVEL USERS ONLY]** Go to the [*'How Provider Level Users complete Account Authentication'* section](#CompleteAccountAuthentication) of this article to proceed with the next step, Account Authentication. Staff Level Users have complete EHR account setup and have no additional steps.




## **What is Provider Level User Account Authentication?**

Account Authentication is the process Elation takes to verify a [Provider Level User's](User-Accounts-Guide-Provider-vs-staff-level-account-privileges.md) identity and credentials before we give Provider Level Users full access to tools that grant them access to all Protected Health Information (PHI) features; especially e-Prescribing.

###

## **Why is Account Authentication required for Provider Level Users?**

Account Authentication is required for [Provider Level Users](User-Accounts-Guide-Provider-vs-staff-level-account-privileges.md) because Elation must make sure the correct ‘person’ is granted access to Protected Health Information (PHI) and related features and interfaces. It is a shared responsibility to make sure your patients' PHI is accessed by the correct individuals. Account Authentication is also required for each Provider Level User before Elation can grant them prescribing privileges.

###

## **How Provider Level Users complete Account Authentication**

**Important Note**: A small subset of customers may still be seeing the [legacy Provider Account Authentication workflow](how-to-complete-account-authentication.md). Both workflows will allow you to complete Account Authentication. If you have any questions about the experience you are seeing, [click here to contact Elation Support](https://help.elationhealth.com/s/contactsupport).




To complete Account Authentication, [Provider Level Users](User-Accounts-Guide-Provider-vs-staff-level-account-privileges.md) must complete the following steps:

1. After you, the Provider Level User, set up your password, you will be brought to the Identify Verification page. Click the “Verify Identity” button to verify your identity with our identity verification service provider, Stripe. [Click here for step by step instructions on the identity verification process](https://help.elationemr.com/s/article/how-to-complete-identity-proofing).

![]()

1. Click the “Continue Set Up” button after you complete identity verification. ![]()
2. Review your account information in the Credential Verification page & select your timezone in the **Timezone** field.

![]()

- **Important Note**: If you do not have an NPI, select the “I do not have an NPI” option to proceed with credential verification.

1. Click “Yes, looks correct” once all the information on the Credential Verification page is accurate.
2. Lastly, you will set your electronic signature for your EHR account. To set your signature:
   - Use your mouse or touchpad to draw your signature in the signature box OR
   - Click the “Use a separate device” button to scan a QR code with a mobile device to draw your signature using the mobile device. ​​​​​![]()
3. Click “Save & Complete” to save your electronic signature. ![]()
4. You will now have access to your EHR account and should see a ‘Congratulations….” box. This means you have successfully completed Provider Account Authentication. ​​​​​​​​​​​​​​![]()
5. Next, go to the[*'Provider Level User Profile Fields'* section](#provider_fields) below to see if you need to store any additional, optional identifiers in your EHR Profile. You can also edit your profile information in this section of your account at any time.

If you experience any issues with the Provider Account Authentication process and need assistance, [please click here to contact the Elation Team](https://help.elationemr.com/s/contactsupport).

## **Profile Level User Profile Fields**

To view your account profile:

1. Click on your email address (username) at the time right corner of your EHR account
2. Click “Settings”
3. Click “Edit profile” in the Account Details page


The Provider Level User profile fields are divided into the following sections:

- [Account Details](#account_details)
- [Credentials](#credentials)
- [Authentication Documents](#authentication_documents)
- [Electronic Signature](#electronic_signature)
- [Lab Identifiers](#lab_identifiers)

### **Account Details**

- Profile picture
 - Your profile picture appears in the Elation Provider Directory.
- **First name\*** and **Last name\***
 - This is how your name will display on all Elation records.
 - **User Tip:** Do not include credentials in these fields. You must enter your legal name. You can enter your credentials in the **Credentials\*** field.
- **Email\***
 - This is the email address that you will use to log in to Elation and Elation will use this email to contact you.
- **Credentials\***
 - Your credentials will appear after your name on all Elation records.
- Tax ID Number (**TIN**)
- **NPI\***

### **Credentials**

- Medical License **State\***
- Medical License Number**\*** (Next to the **State\*** field)
- **DEA Number**
 - **User Tip:** This is required if you will be [ePrescribing Controlled Substances](how-to-complete-the-epcs-sign-up-process.md) via Elation.
- **Supervising Provider**
 - Your Supervising Provider must have their own Elation Provider Level User account. Afterwards you can select their name of this dropdown.
- **Rx Authorization** Number
 - **Rx Authorization** number is an optional field for NPs who have additional license numbers for ePrescribing.
 - **Important Note:** If you have a supervising provider, invite them to create their own [Provider Level User](User-Accounts-Guide-Provider-vs-staff-level-account-privileges.md) account in Elation. Afterwards, you only need to select their name in the **Supervising Provider** field**.** This will ensure their prescribing information (DEA number, etc.) is included on the prescriptions you prescribe.
- **XDEA/NADEAN**
 - **XDEA/NADEAN** is an optional field for Providers who have additional license numbers for prescribing controlled substance medications.

###

### **Authentication Documents**

- Identity Verification
 - You may need to click "Verify identity through Stripe ID Proofing" again if you did not pass identity proofing the first time. [Click here for detailed information about the identity proofing process.](how-to-complete-identity-proofing.md)
- **Medical License**
 - Click the "Upload photo" buttons under Medical License to store a copy of your medical license if preferred.

### **Electronic Signature**

Click on your wet signature to update your wet signature on your account.\*

- Click "Save & Close" after drawing your signature to save it.
- Elation will attach an image of the wet signature for providers whenever provider-signed records are printed or shared from their Elation account.
- If you prefer to use an alternative device to draw your signature, such as a tablet or phone, click the "Use a separate device for my signature" button to scan a QR code with the alternative device.

### **Lab Identifiers**

Enter your lab identification numbers for Quest or Labcorp if applicable.

## **Staff Level User Profile Fields**

To view your account profile:

1. Click on your email address (username) at the time right corner of your EHR account
2. Click “Settings”
3. Click “Edit profile” in the Account Details page



Staff Level Users can store the following information in their account profile:

- Profile picture
- **First name**
- **Last name**
- **Email** (username)
- **Default physician**




*© 2023 Experian. All rights reserved.
© 2023 Stripe, Inc.*


**Next Step

Excited to get started with Elation? We invite you to explore the** [**On-Demand Courses on Elation University**](https://www.elationhealth.com/elation-university/#on-demand) **to learn more about Elation EHR.**

#

## **Related Articles**

- [How to Complete Identity Proofing with Elation](how-to-complete-identity-proofing.md)
- [User Accounts Guide- Managing Elation accounts for providers and staff](managing-user-accounts.md)