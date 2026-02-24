# EPCS Guide - Signing up for EPCS

Source: https://help.elationhealth.com/s/article/how-to-complete-the-epcs-sign-up-process

---

### **Recommended Reading**

Reference the [Introduction to Electronic Prescribing of Controlled Substances (EPCS)](introduction-to-electronic-prescribing-of-controlled-substances-epcs.md) article to learn about the value and purpose of EPCS.

##

# **Contents**

- [Introduction](#Intro)
- [Name Confirmation and VIP Access App](#name_and_app)
- [Accessing the EPCS Sign Up Window](#signup_window)
- [Completing EPCS Sign Up](#complete)
 1. [Get Started: Select Token Type & Complete ID Proofing](#get_started)
     1. [Select Token Type & Review Rules & Conditions](#token_rules)
     2. [Complete Experian Identity Proofing](#IDP)
 2. [Setup 2-Factor Credentials](#TwoStepAuth)
     1. [VIP Access App (software token)](#software_token_setup)
     2. [Key fob (hardware token)](#hardware_token_setup)
 3. [Enter 2-Factor Activation Code](#ActivationCode)
 4. [Access Control- Set Permissions](#AccessControls)
     1. [Setting up Access Controls for the first time as the first provider](#first_time)
        - [Multi-provider Practice](#multi)
        - [Single Provider Practice](#single)
     2. [Setting up Access Controls after the first provider](#after_first)
- [Frequently Asked Questions](#FAQ)

# **Introduction**

In order to electronically prescribe controlled substance medications in Elation, you must complete a series of registration steps via our third party EPCS provider, MDToolbox. Each prescriber is required to complete the signup process individually, as the Identity Proofing (IDP) is designed exclusively for the one prescribing, and the Two-Factor Authentication is unique and individual to each provider.

This process usually takes a total of 20 minutes of your time and involves going through Identity Proofing (IDP) with Experian, setting up 2-Factor Authentication Credentials and setting up Access Controls. This article walks you through the entire sign up process in Elation and MDToolbox.

- **Important Note**: Depending on what information is used to share your one-time 2-Factor Authentication code with you, this process may take 2-5 business days to complete. Please see [Step #3 under Completing EPCS Sign Up](#ActivationCode) for more information.

Additionally, other users in your practice may need to be involved for the final step, [Access Control Permissions](#AccessControls), depending on how many providers there are in your practice.

# **Name Confirmation and VIP Access App**

Before starting, it's important to:

1. Confirm your name in Elation matches your legal name in your credit profile (ex: personal credit cards and bills). If your name appears differently in your credit report, you will need to change your name in Elation to the name that appears on your credit report before proceeding with the MDToolbox sign up process as your identity proofing is based on the details of your credit report. After you complete EPCS Sign Up, you can change your name in Elation back to your preferred name. To update your name in Elation:
   1. Sign in to your Elation account
   2. Click on your email address at the top of your account & click "Settings"
   3. Go to the "Account Details" section and click "Edit Profile"
   4. Update your first, middle and last name to the name that would appear on your credit report
   5. Click "Save" to save your changes
   6. [Access the EPCS Sign Up window](#signup_window) to push your updated name to MDToolbox
   7. [Complete EPCS Sign Up](#complete)
   8. Revert your name back to your preferred name in your Elation Settings once you have completed EPCS Sign Up.
2. Download the free VIP Access app from your smartphone's app store (App Store, Google Play, etc) to use the VIP Access mobile app as a software token for 2 factor authentication. It is the most convenient token option for providers who carry their smartphone with them daily. To find the VIP Access app in your app store, search for "VIP Access". The correct app has the following icon:
   ![]()

   **User Tips**:

   - To assist with security code entry when prescribing controlled substance medications in Elation, allow notifications in the VIP Access app to push notifications to your phone.
   - If you prefer to use a key fob (hardware token), you do not need to download the VIP Access mobile app.

# **Accessing the EPCS Sign Up Window**

1. Navigate to top of your Elation account, click on your email address and then click "Settings".
2. On the left side of the settings page, click into the "ePrescribing Controlled Substances (EPCS)" section and then click the "Sign Up" button.

![]()

1. A new tab will open in your web browser to bring you to the EPCS Sign Up window via MDToolbox; Elation's third party EPCS provider.
   - **Please Note**: If a new tab does not open in you browser, it's most likely due to a *Pop-up Blocker*, as seen below. If you see the icon with the little red X, click on the icon and select the "Always allow pop-ups from..." option.

![]()

# **Completing EPCS Sign Up**

1. [Get Started: Select Token Type & Complete ID Proofing](#get_started)
   1. [Select Token Type & Review Rules & Conditions](#token_rules)
   2. [Complete Experian Identity Proofing](#IDP)
2. [Setup 2-Factor Credentials](#TwoStepAuth)
3. [Enter 2-Factor Activation Code](#ActivationCode)
4. [Access Control- Set Permissions](#AccessControls)

### **1. Get Started: Select Token Type & Complete ID Proofing**

#### **Select Token & Review Rules & Conditions**

Once you arrive on the EPCS Sign Up page, click "Get Started: Select Token Type & Complete ID Proofing" to proceed with the first step.
![]()

1. You'll be prompted to choose the preferred first method of 2-Factor Authentication.
   - If you prefer to use an application on your smartphone called 'VIP Access', select "[Software Token](#software_token_setup)" (Elation recommends this option for easier access).
     - **User Tip**: Please note that if you use a software token, anytime you change your smartphone, you will have to deactivate the old token on your old smartphone and the register the new token on your new smartphone.
   - If you prefer to use a physical Key Fob that will be mailed to your office and carried around with you, select "[Hardware Token](#hardware_token_setup)"
   - If you already have an existing token from a previous system and you want to use that existing token with your Elation EPCS account, click "I already have an approved token - ID Proof and Set it up" to register your existing token to your Elation EPCS account

![]()

1. After making a selection, click "Next>>" at the bottom of the page.
2. The following page will ask you to read the terms of use for EPCS. Please read through the *Rules and Conditions*, select the "I have read and agree..." box at the bottom, and click "Next>>".

![]()

#### **Complete Experian Identity Proofing with Photo ID Verification**

After agreeing to the terms above, you'll begin the Identity Proofing (IDP) process.

1. Click "Next>>" on ID Proof page to begin the identity proofing process to confirm your identity.
2. Complete Photo ID Verification
   - You will need to upload a valid driver's license or passport and take a selfie in order to complete this step.
     1. Enter your birthdate in the birthdate field in the following format: MM/DD/YYYY
     2. Select one of two options for what device you will be using to complete Photo ID Verification. Elation providers will generally select option **A** as they are completing EPCS sign up via their laptop/computer.
        1. *'I am using a laptop/computer, give me a link I can open on my phone for taking pics'*
        2. *'I am logged in with my mobile device now (open camera)'*
     3. Click "Next>>"
     4. Follow the instructions on the page to use your phone or other camera-enabled mobile device to take pictures of your driver's license or passport and your face. An application called 'docupass' will load on your phone or mobile device to assist you. (If you need assistance with this step, [reference the 3:20 to 5:12 timeframe in this video](https://mdtoolbox.com/how-to/help/erxsignup.mp4?AspxAutoDetectCookieSupport=1)- the screen with the QR code will look slightly different but the instructions will be the same.)
        1. Click "Start Verification" on your phone or mobile device
        2. Click "Grand Permission" to allow 'docupass' to access your camera
        3. A preview window displaying your rear facing camera will appear for taking a picture of your ID. Please make sure you have good lighting & frame your ID. The app will automatically take a picture once it detects the ID.
        4. After the app takes a picture of your ID, you will see a page asking you to confirm the information that was pulled from your ID
           1. If the information matches your ID, click "Accept" to continue
           2. If the information does not match your ID, click "Back" to scan your ID again
        5. Afterwards, a preview of your forward facing camera will appear for taking a picture of your face. Place your face in the circle and then follow the prompts at the bottom of the screen. The app will automatically take a picture once it detects your face.
        6. Once the selfie is taken, the app will confirm that all documentation has been accepted and you will see a *'You have successfully completed identity verification process, you may now close this window'* message. Click "OK" to close the window.
           - **User Tip**: If there were issues validating your documentation, you will see an *'Oops... name verification failed'* message on your device. Click "Try Again" to attempt Photo ID Verification again. You will need to get a new QR code by logging out of Elation and then logging back in to restart the EPCS Sign Up process.
     5. Once you have successfully completed Photo ID Verification, go back to your laptop/computer and then click "I have completed PhotoCheck on my phone - NEXT >>" to continue with the next steps of identity proofing
3. Begin the next step of identity proofing by entering your personal information (and not your business information) when filling out your personal details. The information entered will be used to generate your identity proofing questions based on your personal credit report from Experian.

- **User Tip**: Enter your **home information.** If you have recently moved and run into issues with the subsequent steps, enter your former address and try again.
 ![]()

1. Click "I AGREE ->" and you will be prompted to answer a series of questions based on your personal credit history. You have 5 minutes to answer these questions, and are given 3 attempts every 24 hours.

   - **User Tip**: The questions will be based off your credit history according to the [Experian](https://www.experian.com/help/) database. If you need a copy of your credit report, you can request one [here](https://www.experian.com/contact/personal-services-contacts.html#content-03) or call Experian at 888-397-3742. Once you have correctly answered all of the questions click "Submit" to submit your answers. Here is an example of what the questions look like:
     ![]()
2. (Conditional) You may be asked to answer a second set of questions based on your personal credit history.
3. Click "Submit" to submit your answers. After you have passed identity proofing, proceed to the next step to set up your 2-Factor Authentication.

### **2. Setup 2-Factor Credentials**

The DEA requires 2 factor authentication to ePrescribe each controlled substance. The first factor is a personal password (created during this step of the process and referred to as a *Token Password*) and the second is a security code that is either generated within the *VIP Access App* on your smartphone (software token) or on the key fob (hardware token). Follow the step-by-step instructions below to setup both factors.

#### **VIP Access App (software token)**

1. Download the free VIP Access app from your smartphone's app store (App Store, Google Play, etc) if you chose to use a software token in [Step #1](#token_rules). To find the VIP Access app in the app store, search for "VIP Access".
   - The correct app has the following icon: ![]()
2. After successfully downloading the app to your phone, click “I have it - Register My Token” on the EPCS Sign Up page to continue

![]()

1. Enter a personal password in the "Select a Token Password" field that you can easily remember because this will be used every time you ePrescribe a controlled substance. The password must be 6+ characters with at least one number or one symbol.
2. Enter the same password again in the "Re-type your password" field
3. Open the VIP Access app on your smartphone
4. Enter the Credential ID (including the four letters at the front of the ID) at the top of the app in the "Credential ID" field
5. Enter the 6-digit Security Code that displays inside the circle on the VIP Access app in the "Security Code" field

![]()

1. Click "Register >>"
2. Click "Finish/Close"

#### **Key Fob (hardware token)**

Please reference [this article](https://live.mdtoolbox.net/rx/help2/index.htm?context=940) from MDToolbox for more detail on how to set up your key fob.

1. Once you have received your key fob, click "Setup 2-Factor credentials" to pick up where you left off in the sign up process. If you have left the session, you will need to complete ID Proofing again.
2. Click "I have it – Register My Token" to begin the key fob registration
3. Enter a personal password in the "Select a Token Password" field that you can easily remember because this will be used every time you ePrescribe a controlled substance. The password must be 6+ characters with at least one number or one symbol.
4. Enter the same password again in the "Re-type your password" field
5. Enter the Credential ID from the back of your key fob in box 3
6. Enter the Security Code showing on the front of your key fob in box 4 and click "Register". To generate a code press the Power button on the front of the key fob device.
7. Click "Register >>"
8. Click "Finish/Close"

![]()

![]()

### **3. Enter 2-Factor Activation Code**

Experian will send a final one-time activation code to you to complete the prescriber verification process. This will be sent as an automated voice message to the Experian verified phone (home or smartphone) number they have on file for you OR by mail to your Experian verified home address within 2 to 5 business days if they cannot reach you by phone.

If you are expecting a call, and do not receive it within 5 minutes, please click "I need help" >> "I need help from Elation Team member" at the top of your Elation account or [fill out this form](https://help.elationhealth.com/s/contactsupport) and a member of the Elation Team will reach out to our EPCS provider, MDToolbox, and verify with them which method was used to share the activation code with you and if the activation was shared via a phone call, we will ask them to call you again.

- **Important Note**: MDToolbox can only call the the Experian verified phone number on file for you to supply the activation code. MDToolbox will not be able to tell us the exact phone number they called. If you need a copy of your credit report to verify which phone number MDToolbox has on file, you can request one [here](https://www.experian.com/contact/personal-services-contacts.html#content-03) or call Experian at 888-397-3742.

Once you receive your 7 digit activation code, enter the 7 digit activation code under step "3. Enter Your 2-Factor Activation Code" & click "Activate"

- If you need to return to the EPCS Sign Up screen, follow these steps:
 1. Go to "Settings" >> "ePrescribing Controlled Substances EPCS)" within Elation
 2. Click the "Sign Up" button to get back into the EPCS Sign Up page

![]()

### **4. Final Step: Access Control- Set Permissions**

The Access Control Permissions set up workflow differs depending on whether you are:

1. [Setting up Access Controls for the first time as the first provider](#first_time)
   - [Multi-provider Practice](#multi)
   - [Single Provider Practice](#single)
2. [Setting up Access Controls after the first provider](#after_first)

**Important Note**: The DEA requires that two users, a Provider Level User and a second Provider Level User or an Admin Level Staff User, are present in order to enable EPCS within Elation. This is a checks and balances system to ensure that any provider who is given EPCS permissions can legally prescribe controlled substance medications.

1. Multi-provider practices
   - If you work in a practice that has multiple providers, best practice is to have the second person assisting with sign up be another Provider Level User in your practice. You will need to assign them "Admin" level privileges but this action can be one-time only for purposes of completing EPCS sign up and you can revoke the "Admin" level privileges once you have completed EPCS sign up.
2. Single Provider practices
   - If you are the only provider in your practice, we recommend one of the following:
     1. Using an existing staff user in your office as the second person. You will need to assign them "Admin" level privileges but this action can be one-time only for purposes of completing EPCS sign up and you can revoke the "Admin" level privileges once you have completed EPCS sign up.
     2. If you do not have any existing Staff Level Users in your office, ask a trusted friend or family member to be the second person. You will need to invite them to register for an Elation account and assign them "Admin" level privileges but this will only be temporary and you can disable their account (and access) immediately after you have completed EPCS sign up.

### **Setting up Access Controls for the first time as the first provider**

The steps in this section apply to you (the provider) if your entire practice is new to Elation and this is the first time a provider in the practice is signing up for EPCS. Each provider should **always complete steps 1 to 3 in the** [**EPCS Sign Up Process Guide**](how-to-complete-the-epcs-sign-up-process.md) first before setting up their Access Control Permissions.

#### **Multi-Provider Practices**

**Important Note:** Please note the user definitions for the workflow detailed in this section.

- First user = Provider signing up for EPCS
- Second user = Provider Level User who is assisting with sign up
 - Must be an Admin Level User at the practice
 - Will become an Access Control Manager by assisting with sign up

1. Assign "Admin" level privileges to the second user (Provider Level User assisting with sign up) in your practice if they do not already have this permission
   - Go to "Manage Accounts" and then click "Make Admin" next to the second user's name
2. Ask the second user to login to their Elation account
3. Ask the second user to click on their email at the top of their Elation account & click "Settings"
4. Ask the second user to click into the "ePrescribing Controlled Substance (EPCS)” settings section and click on "Access Controls"
5. The second user will then be brought to a page called "EPCS Permissions- Logical Access Control Setup"
6. Under Grant Permissions, ask the second user to check off all of the following boxes next to your name:
   - Access Control Manager?
   - Authorization Verifier?
   - Can Approve EPCS?
   - Can Sign & Send?
7. Under Grant Permissions, ask the second user to check off the following boxes next to their name:
   - Access Control Manager?
   - Authorization Verifier?
8. If the second user plans on signing up for EPCS at a later time, have them check off the following boxes next to their own name as well:
   - Can Approve EPCS?
   - Can Sign & Send?
9. Under Signoff & Save Permissions:

- **Important Note:**Please note the following definitions for the **Signoff & Save Permissions** fields on the "EPCS Permissions- Logical Access Control Setup" page.
 1. **First User (Prescriber w/ Token)** = Provider signing up for EPCS
     - Ask the second user to select your own name in the dropdown for this field
 2. **Second User (Prescriber or Admin)** = Access Control Manager (who is an Admin Level User) assisting with sign up
     - The second user's name should already be filled in in the dropdown for this field

1. Have the second user click "Save" and a new box will appear under the **Second User (Prescriber or Admin)** field that prompts the second user to enter their email address
2. Have the second user enter their email address & click "Save". A box will pop up with a message that says "Second User approval code has been sent to their email...."
3. Have the second user check their email inbox for an email with the subject line "EPCS Permission Request" from the email address "[noreply@mdnotification.net](mailto:noreply@mdnotification.net)". The body of the email will contain a 7 digit approval code
4. Have the second user enter the 7 digit code in the "Approval Code" box that now appears under the **Second User (Prescriber or Admin)** field
5. Have the second user click "Save" to save the approval code
6. A box will pop up asking you (First User/the provider completing EPCS Sign Up) to enter your EPCS Token Password and Security Code. Enter this information and click "Sign and Authorize" to complete the final step of this process.

####

**Congratulations on completing EPCS Sign Up!** You can now close the MDToolbox tab in your web browser.

To ensure that everything has been setup properly, go to a patient’s chart and click "Rx" >> "Controlled Substance Form"- if the blue button now says “ePrescribe”, you’re good to go! [Click here to view our how to e-Prescribe controlled substance guide](http://help.elationemr.com/customer/portal/articles/2746249-how-to-e-prescribe-controlled-substances).

**Single Provider Practices**

1. If you have a staff member with a Staff Level Elation account, assign them "Admin" level privileges if they do not already have this permission
   - Go to "Manage Accounts" and then click "Make Admin" next to the user's name
2. If you do not have any staff, ask a trusted friend or family member to assist you
   - Invite them to Elation by going to "Manage Accounts" >> "+ Invite Staff"
   - Enter their name and email and then click "Invite"
   - Ask them to find the invitation in their email inbox and click "Click here to complete your Registration"
     - The invitation email will come from "[support@elationemr.com](mailto:support@elationemr.com)" and will have the subject line 'Your Elation Account is Ready!'
   - Supply them with your practice's fax number to complete registration
3. After registration, ask them to click on their email at to top of their account and click "Settings"
4. Ask them to click into the "ePrescribing Controlled Substance (EPCS)" section and click "Access Controls"
5. The Admin Level Staff User will then be brought to a page called "EPCS Permissions- Logical Access Control Setup".
6. Under Grant Permissions, ask the Admin Level Staff User to check off all of the following boxes next to your name:
   - Access Control Manager?
   - Authorization Verifier?
   - Can Approve EPCS?
   - Can Sign & Send?
7. Under Grant Permissions, ask the Admin Level Staff User to check off all of the following boxes next to their own name:
   - Access Control Manager?
   - Authorization Verifier?
8. Under Signoff & Save Permissions:

- **Important Note:** Please note the following definitions for the **Signoff & Save Permissions** fields on the "EPCS Permissions- Logical Access Control Setup" page.
 1. **First User (Prescriber w/ Token)** = Provider signing up for EPCS
     - Ask the second user to select your own name in the dropdown for this field
 2. **Second User (Prescriber or Admin)** = Admin Level Staff User assisting with sign up
     - The second user's name should already be filled in in the dropdown for this field

1. Click "Save" and a new box will appear under the **Second User (Prescriber or Admin)** field that prompts the Admin Level Staff User to enter their email address
2. Have the Admin Level Staff User enter their email address & click "Save". A box will pop up with a message that says "Second User approval code has been sent to their email...."
3. Have the Admin Level Staff User check their email inbox for an email with the subject line "EPCS Permission Request" from the email address "[noreply@mdnotification.net](mailto:noreply@mdnotification.net)". The body of the email will contain a 7 digit approval code
4. Have the Admin Level Staff User enter the 7 digit code in the "Approval Code" box that now appears under the **Second User (Prescriber or Admin)** field
5. Have the Admin Level Staff User click "Save" to save the approval code
6. A box will pop up asking you (the provider completing EPCS Sign Up / First User) to enter your EPCS Token Password and Security Code. Enter this information and click "Sign and Authorize" to complete the final step of this process

Congratulations on completing EPCS Sign Up! You can now close the MDToolbox tab in your web browser.

To ensure that everything has been setup properly, go to a patient’s chart and click "Rx" >> "Controlled Substance Form"- if the blue button now says “ePrescribe”, you’re good to go! [Click here to view our how to e-Prescribe controlled substance guide](http://help.elationemr.com/customer/portal/articles/2746249-how-to-e-prescribe-controlled-substances).

### **Setting up Access Controls after the first provider**

The steps in this section apply to you (the provider) if another Provider Lever User in the practice has already completed EPCS Sign Up. Each provider should **always complete steps 1 to 3 in the** [**EPCS Sign Up Process Guide**](how-to-complete-the-epcs-sign-up-process.md) first before setting up their Access Control Permissions.

There are three options available for necessary users present when setting up Access Controls when there are already two established Access Control Managers at a practice (one being a Provider Level User):

| Option 1 | Option 2 | Option 3 |
| --- | --- | --- |
| - One Provider Level User/established Access Control Manager - One Staff Level User/established Access Control Manager | - Two Provider Level Users/established Access Control Managers | - Provider Level User signing up for EPCS - Provider or Staff Level User/established Access Control Manager |
| \*Please utilize the steps detailed below | \*Please utilize the steps detailed below | \*Please utilize the [steps detailed for setting up a Provider Level User for the first time in a multi-provider practice](#multi) if only these users are present |

1. Ask any established Access Control Manager to login to their Elation account
2. Ask the Access Control Manager to click on their email at the top of their Elation account & click "Settings"
3. Ask the Access Control Manager to click into the "ePrescribing Controlled Substance (EPCS)” settings section and click on "Access Controls"
4. The Access Control Manager will then be brought to a page called "EPCS Permissions- Logical Access Control Setup"
5. Under Grant Permissions, ask the Access Control Manager to check off all the boxes for the fields listed below that apply next to your name. (**At a minimum, Provider Level Users must have 'Can Approve EPCS?' and ‘Can Sign & Send' checked off** in order to send electronic controlled substance medications via Elation):
   - Access Control Manager?
   - Authorization Verifier?
   - **Can Approve EPCS?**
   - **Can Sign & Send?**
6. Under Signoff & Save Permissions:
   - For the **First User (Prescriber w/ Token)** field, ask the Access Control Manager to select the name of the other Access Control Manager (must be a Provider Level User, usually already signed up for EPCS)
   - For the **Second User (Prescriber or Admin)** field, the original Access Control Manager's own name should already be filled in
7. Have the Access Control Manager click "Save" and a prompt will appear asking the Access Control Manager to approve their own changes. Have the Access Control Manager click "OK" to continue
8. A box will pop up for the First User (the other Access Control Manager/Provider Level User) to enter their EPCS Token Password and Security Code. Have the First User enter this information and click "Sign and Authorize" to complete the final step of this process

####

Congratulations on completing EPCS Sign Up! You and the Access Control Manager can now close the MDToolbox tab in your web browser.

To ensure that everything has been setup properly, go to a patient’s chart and click "Rx" >> "Controlled Substance Form"- if the blue button now says “ePrescribe”, you’re good to go! [Click here to view our how to e-Prescribe controlled substance guide](http://help.elationemr.com/customer/portal/articles/2746249-how-to-e-prescribe-controlled-substances).

# **Frequently Asked Questions (FAQ)**

#### **Who do I use as an Access Control Manager if I am a single-provider practice with no staff?**

If you are the only provider in your practice and you do not have any staff, we recommend asking a trusted friend or family member to be a temporary Access Control Manager. You will need to invite them to register for an Elation account and assign them "Admin" level privileges but this will only be temporary and you can disable their account (and access) immediately after you have completed EPCS Sign Up.

#### **How do I update my name in Elation if it differs from the name on my credit report?**

If your name appears differently in your credit report, you will need to change your name in Elation to the name that appears on your credit report before proceeding with the MDToolbox sign up process as your identity proofing is based on the details of your credit report. After you complete EPCS Sign Up, you can change your name in Elation back to your preferred name. To update your name in Elation:

1. Sign in to your Elation account
2. Click on your email address at the top of your account & click "Settings"
3. Go to the "Account Details" section and click "Edit Profile"
4. Update your first, middle and last name to the name that would appear on your credit report
5. Click "Save" to save your changes
6. [Access the EPCS Sign Up window](#signup_window) to push your updated name to MDToolbox
7. [Complete EPCS Sign Up](#complete)
8. Revert your name back to your preferred name in your Elation Settings once you have completed EPCS Sign Up.

#### **MDToolbox will not accept my Credential ID and Security Code for my 2-Factor Credential software token (VIP Access) set up. What should I do?**

Make sure to include the four letters ahead of the Credential ID. In the example, below, the Credential ID is SYMC63234388.

![]()

#### **I did not receive a phone call with my activation code. What should I do?**

If you are expecting a call, and do not receive it within 5 minutes, please click "I need help" >> "I need help from Elation Team member" at the top of your Elation account or [fill out this form](https://help.elationhealth.com/s/contactsupport) and a member of the Elation Team will reach out to our EPCS provider, MDToolbox, and verify with them which method was used to share the activation code with you. If the activation was shared via a phone call, we will ask them to call you again.

- **Important Note**: MDToolbox can only call the the Experian verified phone number on file for you to supply the activation code. MDToolbox will not be able to tell us the exact phone number they called. If you need a copy of your credit report to verify which phone number MDToolbox has on file, you can request one [here](https://www.experian.com/contact/personal-services-contacts.html#content-03) or call Experian at 888-397-3742.

###

# **Next Step**

Send a controlled substance prescription electronically using the Controlled Substance Form in your Patient's chart! Learn **[How to e-Prescribe Controlled Substances](how-to-e-prescribe-controlled-substances.md).**




# **Related Articles**

- [EPCS Guide - ePrescribing controlled substance medications & troubleshooting](how-to-e-prescribe-controlled-substances.md)
- [EPCS (Electronic Prescribing of Controlled Substances) Introduction](introduction-to-electronic-prescribing-of-controlled-substances-epcs.md)
- [EPCS Guide - Managing EPCS Access Controls](how-to-set-up-epcs-access-controls.md)
- [EPCS Guide - Updating your EPCS Token or password](how-to-update-your-epcs-token.md)
- [EPCS Guide - Frequently Asked Questions](epcs-faq-page.md)
- [How to Complete Identity Proofing with Elation](how-to-complete-identity-proofing.md)