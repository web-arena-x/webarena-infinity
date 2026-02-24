# EPCS Guide - ePrescribing controlled substance medications & troubleshooting

Source: https://help.elationhealth.com/s/article/how-to-e-prescribe-controlled-substances

---

# Contents

- [Overview](#overview)
 - [What is EPCS prescribing?](#what-is-epcs-prescribing)
- [Prerequisites for EPCS prescribing](#prerequisites-for-epcs-prescribing)
 - [Verifying your EPCS sign-up status](#verifying-your-epcs-sign-up-status)
- [Workflow Instructions](#workflow-instructions)
 - [Prescribing a controlled substance](#prescribing-a-controlled-substance)
 - [Addressing Controlled Substance refill requests](#RefillRequest)
 - [Using Staff Delegates in EPCS Workflow](#StaffDelegates)
 - [Prescribing on the behalf of another Provider](#EPCSForAnotherProvider)
- [Common issues and troubleshooting](#common-issues-and-troubleshooting)
 - [No token prompt appears when prescribing](#no-token-prompt-appears-when-prescribing)
 - [Token PIN incorrect or token out of sync](#token-pin-incorrect-or-token-out-of-sync)
 - [Prescription fails to send](#prescription-fails-to-send)
- [Frequently Asked Questions (FAQ)](#frequently-asked-questions)

# Overview

## What is EPCS prescribing?

[Click here to learn more about the overview of EPCS (Electronic Prescribing of Controlled Substances)](https://help.elationemr.com/s/article/introduction-to-electronic-prescribing-of-controlled-substances-epcs).

# Prerequisites for EPCS prescribing

Before you can electronically prescribe controlled substances, confirm the following are complete:

| | |
| --- | --- |
| 1 | **EPCS sign-up is complete** - You have finished identity proofing with Experian and set up two-factor authentication through MDToolbox. Follow the instructions in the next section to verify your sign-up status. |
| 2 | **Your token is registered** - Your software token (**VIP Access App**) or hardware token (key fob) is registered to your EPCS account. |
| 3 | **Access Controls are configured** - An Access Control Manager has granted you the **Can Approve EPCS?** and **Can Sign & Send?** permissions on the **EPCS Permissions- Logical Access Control Setup** page. |
| 4 | **You have access to your token** - Keep your smartphone (with the **VIP Access App**) or key fob available when prescribing. |

## Verifying your EPCS sign-up status

To verify your sign-up is complete:

| | |
| --- | --- |
| 1 | Go to Settings. |
| 2 | Scroll down and click **ePrescribing Controlled Substances (EPCS)** from the left-hand navigation bar. |
| 3 | Click the **Sign Up** or Update Token/Password button. |

If the sign-up is not yet complete, [further steps](https://help.elationemr.com/s/article/how-to-complete-the-epcs-sign-up-process) will be available for you to do. If the sign-up is complete, you will be given options to update your **Token Password** (EPCS password) instead.

# Workflow Instructions

## Prescribing a controlled substance

When everything is set up correctly, follow these steps to electronically prescribe a controlled substance:

| | |
| --- | --- |
| 1 | Click **Rx** -> **Prescription Form (Rx/OTC/CS)** in the gray navigation bar at the top of the patient's chart |
| 2 | Complete the required (\*) fields   - - [Click here for more information about the various fields in the Prescription Form](Prescriptions-Forms-Guide-ePrescribing-and-ordering-meds.md#fill_out_details).   ℹ️ **NOTE** Ensure the medication is not user-created. User-created medications cannot be ePrescribed as controlled substances. |
| 3 | Select an EPCS-certified pharmacy. Pharmacies that support EPCS display an **EPCS** label next to their name in the search results. |
| 4 | Click **Prescribe**. |
| 5 | Review the **Prescription Summary** and click **Prescribe** again. |
| 6 | When the **Controlled Substance Signoff Required** window appears, enter your **Token Password** (the password you created during EPCS sign-up). |
| 7 | Open the **VIP Access App** on your smartphone or retrieve your key fob and enter the 6-digit **Security Code** displayed on your token. This code changes every 30 seconds.   - This is how the Security Code displays on the VIP Access App on a smartphone. - This is how the Security Code displays on a key fob. |
| 8 | Click **Sign + Send**. |
| 9 | Click OK to close the confirmation screen. The prescription is now sent to the pharmacy. |

## **Addressing Controlled Substance refill requests**

To regulate the use of controlled substances, the National Council of Prescription Drug Programs (NCPDP) only allows electronic controlled substance refill requests to be denied or replaced with new intentional prescriptions.

This means when presented with a controlled substance medication refill request in Elation, your response options will be to either replace the request with a new prescription or deny the refill request. The NCPDP also does not allow the replacement prescription to be automatically filled, therefore selecting **Renew** will launch a blank Prescription Form and you will need to specify the medication details again. The NCPDP's intent for this is to require more intentional subsequent controlled substance prescriptions.

| | |
| --- | --- |
| **1** | Open the relevant Patient Chart. |
| **2** | Identify the relevant refill request   1. Click **Deny** if you would like to deny the request 2. Click **Renew** if you would like to send a new prescription back to the pharmacy that initiated the request     1. A new **Prescription Form** will open.    2. Fill in the details of the medication & click one of the **Prescribe** options.    3. Enter the password you created during the EPCS registration process via MDToolbox.    4. Open your VIP Access App on your smartphone.    5. Enter the 6 digit **Security Code** that displays on your VIP Access App.    6. Click **Sign + Send**.    7. Click **OK** to close the confirmation screen. |

## **Using Staff Delegates in EPCS Workflow**

Authorized Staff Delegates cannot e-prescribe controlled substances on your behalf. Authorized Staff Delegates can draft controlled substance prescriptions on your behalf and click **Save as Draft & Close** to save the prescription for you to sign off at a later time.

Providers can find drafted scripts in the **Draft Orders** inbox on their **Practice Home** page and send the prescription with their password and **VIP Access App**.

## **Prescribing on the behalf of another Provider**

When a provider opens an in-draft controlled substance order that was drafted by another provider, they will see a DEA required pop up notification to acknowledge the transfer of ownership.

# Common issues and troubleshooting

## No token prompt appears when prescribing

If you do not see the **Token Password** and **Security Code** prompt after clicking **Prescribe**, check the following:

- **EPCS enrollment status** - Confirm you completed the full EPCS sign-up process, including identity proofing and two-factor authentication setup. [Click here for instructions](#verify_EPCS_sign_up_status).
- **Token registration** - Confirm your token is registered. If you recently changed phones, you need to deactivate your old token and register the new one.
- **Access Control permissions** - Contact your practice's Access Control Manager to confirm you have **Can Approve EPCS?** and **Can Sign & Send?** permissions enabled.
- **Pharmacy selection** - Confirm you selected an EPCS-certified pharmacy. Only pharmacies with the **EPCS** label support electronic controlled substance prescriptions.

## Token PIN incorrect or token out of sync

If your **Token Password** or **Security Code** is not accepted:

- **Forgot Token Password** - Reset your password by going to Settings → ePrescribing Controlled Substances (EPCS) → **Update Token/Password**. Click **Reset my token password** and follow the prompts.
- **Credential ID mismatch** - Confirm the **Credential ID** you enter matches the ID shown in your VIP Access App (including the four letters before the numbers) or on the back of your key fob. If the IDs are different, proceed to the next suggestions.
- **New phone or device** - Deactivate the token on your old device and register the token on your new device. Go to Settings → ePrescribing Controlled Substances (EPCS) → **Update Token/Password** and follow the steps under **Setup a New Phone**.
- **Lost token and forgot password** - You will need to complete identity proofing again. Go to Settings → ePrescribing Controlled Substances (EPCS) → **Update Token/Password** and select **I don't have my old token- use IDP to setup Token and New Password**.

## Prescription fails to send

If your controlled substance prescription fails after entering your token credentials:

- **Check patient demographics** - Confirm patient demographics are complete with no special characters or abbreviations in the **Name** and **Address** fields.
- **Verify patient address** - Confirm the patient has an address on file. If the patient is experiencing homelessness, enter **HOMELESS** in the **Address** field with the **City**, **State**, and **Zip** for your local area.
- **Check Schedule II restrictions** - Schedule I and II drugs do not allow post-dated prescriptions or refills. Ensure the **Refill** field shows **0** for these medications.

# Frequently Asked Questions

#### Can my staff send controlled substance prescriptions for me?

No. DEA regulations require the prescriber to sign each controlled substance prescription with their own two-factor EPCS credential. Staff delegates cannot send controlled substance prescriptions on your behalf, even if they are Authorized Prescription Delegates.

Staff can draft controlled substance prescriptions and save them using **Save as Draft & Close**. You can then find drafted prescriptions in the **Draft Orders** inbox on your Practice Home page and complete them with your own **Token Password** and **Security Code**.

#### Why do I need to register a new token when I change my phone?

Each phone is a unique token with a unique **Credential ID**. To ensure only you can prescribe controlled substances, the correct token must be registered to your account.

#### Can I use two different EPCS tokens at the same time?

Yes. After completing EPCS registration with your first token, you can register a second token by:

| | |
| --- | --- |
| 1 | **Navigate to Settings** - Go to Settings. |
| 2 | **Open EPCS settings** - Scroll down and click **ePrescribing Controlled Substances (EPCS)** from the left-hand navigation bar. |
| 3 | **Update token** - Click the Update Token/Password button. |
| 4 | **Register second token** - Enter your current **Token Password** in the **Register a 2nd Token** section. |

#### Where can I find more information about EPCS setup?

For complete information about electronic prescribing of controlled substances, see the **Related Articles** section below.

#### **Can I print the prescription after the prescription is sent electronically?**

Yes, but the print out will be watermarked per DEA regulations.

#### **Can I print a controlled substance script instead of sending it to a pharmacy?**

Yes, you can print the controlled substance script on tamper proof paper and hand it to a patient (if your State regulations permit).


ℹ️ **NOTE** Controlled substance scripts can only be printed within 10 minutes of the script being signed (this is in case you run into printer issues). Afterwards a watermark will be printed over the script per DEA regulations.

#### **Why can't I e-prescribe custom or compound controlled substance medications?**

The database of medications that are available to e-prescribe through Elation are provided by the national Medispan medication database. All active and certified drugs are available in this database. We recommend searching for the drug using different nomenclatures to find it.

Each medication that is prescribed electronically must have a National Drug Code associated with it for purposes of identifying drug schedule information. We cannot add to the Medispan database or send through medications that are not in this database as Surescripts will not approve prescriptions without schedule information.

#### **Why can't I approve a controlled substance prescription request I received from a pharmacy?**

The National Council of Prescription Drug Programs (NCPDP) only allows controlled substance refill requests to be denied or replaced with new prescriptions. This means when presented with a controlled substance refill request, your response options will be to deny the refill request or to replace the medication with a new prescription. The NCPDP also does not allow the replacement prescriptions to be autofilled, therefore selecting "Renew" will launch a blank Prescription Form and you will need to specify the medication details again. The NCPDP's intention was not to slow you down but to require more intentional subsequent controlled substance prescriptions.

#### **Why can't I send the same script to the pharmacy again?**

Per controlled substance regulations, the same controlled substance for the same patient on the same fill date cannot be sent more than once to the same pharmacy.

- Ex. If you sent Lorazepam to CVS #2283 for patient Jane Doe to be filled on 10/10/2021, you cannot send another prescription for Lorazepam to CVS #2283 for patient Jane Doe to be filled on 10/10/2021.

If you are replacing the original prescription to the same pharmacy, we recommend going to the original prescription and clicking **Actions** -> **Cancel this eRx order** to cancel the script and then you will be able to send a corrected prescription once the pharmacy accepts the cancel request.

If the pharmacy does not accept cancelling prescriptions electronically or you are unable to wait for the pharmacy to accept your cancel request, you must call the pharmacy to cancel the order. However, due to this EPCS constraint, your script for Lorazepam to be filled on 10/10/2021 must still be sent to a different pharmacy (not CVS #2283).

####

#### **Why can't I remove the controlled substance prescription from the Chronological Record?**

The DEA requires that any prescription for a controlled substance remains documented within the patient's chart for record keeping purposes.

[Click here for additional FAQs about EPCS](https://help.elationemr.com/s/article/epcs-faq-page).

# Related Articles

- [EPCS (Electronic Prescribing of Controlled Substances) Introduction](introduction-to-electronic-prescribing-of-controlled-substances-epcs.md)
- [EPCS Guide - Signing up for EPCS](how-to-complete-the-epcs-sign-up-process.md)
- [EPCS Guide - ePrescribing controlled substance medications & troubleshooting](how-to-e-prescribe-controlled-substances.md)
- [EPCS Guide - Managing EPCS Access Controls](how-to-set-up-epcs-access-controls.md)
- [EPCS Guide - Updating your EPCS Token or password](how-to-update-your-epcs-token.md)
- [EPCS Guide - Frequently Asked Questions](epcs-faq-page.md)
- [How to Complete Identity Proofing with Elation](how-to-complete-identity-proofing.md)
- [Prescription (Rx) Templates](create-and-use-custom-rx-templates.md)
- [Prescriptions Guide- Frequently Asked Questions](Prescriptions-Guide-Frequently-Asked-Questions.md)