# Real-time Eligibility Guide - Setting up Payers for eligibility checks (Paid Add-On)

Source: https://help.elationhealth.com/s/article/Real-time-Eligibility-Set-Up-Payers

---

# **Contents**

- [Overview](#overview)
 - [What is Real-Time Eligibility?](#description)
- [Setup](#initial_setup)
 - [Sending credentials & eligibility enrollment details to Elation](#complete_registration)
 - [Updating Insurance Eligibility Settings](#insurance_eligibility_settings)
 - [Updating Carrier Settings](#Carrier_Settings)
    - [Adding Eligibility Payer ID and setting Submitter Type for each Payer](#add_eligibility_payer_ID)
 - [Checking for eligibility enrollment requirements](#check_for_enrollments)
- [Workflow Instructions](#maintenance)
 - [Maintaining your Carrier list](#maintain_carrier_list)
 - [Adding new Carriers](#add_new_carriers)
 - [Adding new Providers](#add_new_providers)
- [Troubleshooting common errors](#troubleshooting)
 - [Incorrect Payer ID selection](#incorrect_payer_ID)
 - [Patient has active coverage but the eligibility response says 'inactive' or 'invalid'](#patient_showing_wrong_status)
 - [Provider NPI has not been enrolled for eligibility with payer](#provider_not_enrolled)
 - [Payer ID does not support real-time eligibility. Invalid payer name...](#payer_no_RTE)
- [Frequently Asked Questions (FAQ)](#faq)

# **Overview**

## **What is Real-time Eligibility?**

Real-time Eligibility (RTE) in Elation EHR enables you to request a patient's primary and secondary insurance eligibility, coverage, and benefits based on the insurance details in their demographics. This article explains how to configure Carriers (Payers) in your EHR to ensure you receive insurance eligibility and benefits information.

📖 **RECOMMENDED READING** [Click here to learn more about Elation's Real-time Eligibility feature and how to use it](https://help.elationemr.com/s/article/Real-Time-Eligibility).

# **Setup**

ℹ️   **REQUIREMENT**

The following actions must be completed to start using the Real-time Eligibility feature. Follow the detailed instructions below for guidance.

1. [Send credentials and eligibility enrollment details to Elation](#complete_registration) **after** completing the following Settings configurations:
   1. Review your [Insurance Eligibility Settings](#insurance_eligibility_settings).
   2. [Configure](#Carrier_Settings) the **Eligibility Payer ID** and **Submitter Type**for each Carrier you want to run eligibility checks for.
2. Wait for approval from ClaimMD (Elations' Clearinghouse for RTE).
   - This typically takes 2-3 business days.

## **Sending credentials & eligibility enrollment details to Elation**

Elation must assist with completing Provider registration and eligibility enrollments before you can start using the Real-Time Eligibility feature. To begin this process:

| | |
| --- | --- |
| **1** | Download [this file](https://elation.my.salesforce.com/sfc/p/37000000L9cg/a/Ui000003PSoz/BkV3AZj5bg1MW0.K5HKS8IhYkvH1Ybs99RRyCD_mFO0) and fill out the following two tabs of the spreadsheet:   - **Group info**: Enter all the Provider or Group NPIs associated with your practice and their TINs.   - Add any Group NPIs associated with your practice to your [Insurance Eligibility Settings](#insurance_eligibility_settings) (instructions below). - **Special enrollment**: Enter the following information into each row for **each Payer** that requires eligibility enrollment. To find the Payers that need eligibility enrollment, go through the exercise of [updating your Carrier Settings](#Carrier_Settings) (instructions below).   - Payer ID   - NPI(s) associated with the Payer contract   - Name(s) associated with the NPI(s) |
| **2** | Once your file is complete and ready, click **I need help** -> **Contact Elation Support**. |
| **3** | Choose **Something else** under **Select an issue**. |
| **4** | Enter the following information in the **Details** box:   - *Please help me complete Provider registration and submit Payer enrollments for RTE. Details are in the attached file.* |
| **5** | Click **Next** to continue to the next step of the contact Support process. |
| **6** | Click **No, I still need help**. |
| **7** | Confirm the **Details** & click **Add Attachment** to attach the filled out spreadsheet. |
| **8** | Click **Next**. |
| **9** | Click **Submit** after confirming the name and email we should contact once the enrollment is completed. |
| **10** | Enrollments will be completed within two business days, after which you will begin receiving eligibility responses for that payer. |

## **Updating Insurance Eligibility Settings**

By default, the Real-time Eligibility feature uses the NPI of the **Provider assigned in practice** to run eligibility checks. If your practice is contracted with any payers using a Group NPI then you must add those Group NPI(s) to the **Insurance Eligibility Settings** to configure running eligibility checks using the Group NPI. You can add as many Group NPIs as needed.
![]()
To add Group NPI information for eligibility checks:

| | |
| --- | --- |
| **1** | Go to **Settings** -> **Insurance**. |
| **2** | Click **+ Add New Group** under **Insurance Eligibility Settings**. |
| **3** | Enter the **Group Details**:   - **Group name**\***:** Name of your group as associated with Payer contracts. - **Group nickname**: Any preferred names the group goes by. - **Group NPI**\*: NPI of the group associated with Payer contracts. |
| **4** | Click **Save**. |

## **Updating Carrier Settings**

Two fields in the Insurance Carrier details are required for eligibility checks: **Eligibility Payer ID** and **Submitter Type**. Please review these fields for each Carrier and make appropriate changes as needed to ensure successful eligibility responses.

- *Additional Details* - **Eligibility Payer ID**
 - The **Eligibility Payer ID** field stores the ID required (as designated by the Payer) to run eligibility checks for a specific payer. [Click here to find the Eligibility Payer ID for a Payer](https://www.claim.md/payer-list).
- *Credentialing & Enrollment* **- Submitter Type**
 - The **Submitter Type**allows you to specify whether an Individual Provider NPI will be used to run eligibility checks or whether one of the [Group NPIs](#insurance_eligibility_settings) will be used to run eligibility checks.
    - If **Credentialed as a group** is selected and you have multiple Groups, an additional dropdown will appear to allow you to select which 'Group' will be submitted for eligibility checks.

### **Adding Eligibility Payer ID and setting Submitter Type for each Payer**

Follow the steps outlined in the quick video below to add the **Eligibility Payer ID** and set the **Submitter Type** for each Payer. You will need to have two windows or two tabs open in your web browser- one for Elation EHR and the other for [ClaimMD's Payer List](https://www.claim.md/payer-list) (ClaimMD is the Clearinghouse Elation uses for eligibility checks).

You can also follow the steps below, as demonstrated in the video above.

| | |
| --- | --- |
| **1** | Open the **Insurance** Settings page in Elation. |
| **2** | Open this list of Payers from ClaimMD in another tab or window of your browser: <https://www.claim.md/payer-list> |
| **3** | Search for the Payer you want to run eligibility checks for in the ClaimMD Payer List and see if they have ‘Prime Eligibility’ listed in the Services column.   - If they do, this means they offer eligibility/benefits information and you can run an eligibility check for them via Elation. - If they do not then you cannot run eligibility checks for this Payer via Elation. |
| **4** | If the Payer has ‘Prime Eligibility’ listed in the Services column, copy the Payer ID under the **Payer ID** column and then go back to Elation. |
| **5** | Click the **Edit** (pencil) button next to a Payer's name. |
| **6** | Paste the Payer ID you copied into the **Eligibility Payer ID** field. |
| **7** | Scroll down to the **Credentialing and Enrollment** section and specify under **Submitter Type** whether the Providers in your practice are **Credentialed as individual providers** or **Credentialed as a group** for this payer.   - This is important to guarantee a successful eligibility check. If **Credentialed as a group** is selected and you have multiple Groups, an additional dropdown will appear to allow you to select which 'Group' will be submitted for eligibility checks. |
| **8** | Click **Save** in the Insurance details in Elation to save your edits. |
| **9** | Return to the ClaimMD tab in your browser and click **View Payer**. Check the **Eligibility / Benefits** row for the word "Enrollment." If it appears, a special enrollment process must be completed by Elation on your behalf. Notify Elation immediately by following the [steps outlined in the *'Sending credentials & eligibility enrollment details to Elation'* section above](#complete_registration). |
| **10** | Repeats steps 3-9 for each Payer you want to run eligibility checks for. |

## **Checking for eligibility enrollment requirements**

Certain payers require you to complete a special enrollment process in order to obtain eligibility information.

To verify whether a payer requires eligibility enrollments:

| | |
| --- | --- |
| **1** | Open this list of Payers from ClaimMD in another tab or window of your browser: <https://www.claim.md/payer-list> |
| **2** | Search for the Payer you want to run eligibility checks for in the ClaimMD Payer List and see if they have ‘Prime Eligibility’ listed in the Services column.   - If they do, this means they offer eligibility/benefits information and you can run an eligibility check for them via Elation. - If they do not then you cannot run eligibility checks for this Payer via Elation. |
| **3** | Click **View Payer** if the payer offers eligibility checks. |
| **4** | Check the **Eligibility / Benefits** row for the word "Enrollment." If it appears, a special enrollment process must be completed by Elation on your behalf. |
| **5** | Download [this file](https://elation.my.salesforce.com/sfc/p/37000000L9cg/a/Ui000003PSoz/BkV3AZj5bg1MW0.K5HKS8IhYkvH1Ybs99RRyCD_mFO0) and fill out the following two tabs of the spreadsheet:   1. **Group info**: Enter all the Provider or Group NPIs associated with your practice and their TINs. 2. **Special enrollment**: Enter the following information into each row for **each Payer** that requires enrollment:    1. Payer ID    2. NPI(s) associated with the Payer contract    3. Name(s) associated with the NPI(s) |
| **6** | Notify Elation immediately by following the [steps outlined in the *'Sending credentials & eligibility enrollment details to Elation'* section above](#complete_registration). |

# **Workflow Instructions**

## **Maintaining your Carrier list**

Depending on how your organize your Carriers, you may have multiple entries for the same Carrier. Make sure the **Eligibility Payer ID** is populated for all entries of the same Carrier in order for eligibility checks to run properly.

Here is an example of a list of Aetna Carriers and how the Eligibility ID field may look:

| **Payer Name** | **Eligibility Payer ID** |
| --- | --- |
| Aetna PPO | 60054 |
| Aetna Affordable Health Choices | 60054 |
| Aetna HMO | 66054 |

## **Adding new Carriers**

When you are about to add a new Carrier to your Carrier list:

| | |
| --- | --- |
| **1** | Review your existing list of Carriers to make sure a new Carrier is needed. [Click here for instructions on how to add a new Carrier](https://help.elationemr.com/s/article/Managing-Carriers-and-Plans#add_carrier_or_plan). |
| **2** | [Add the **Eligibility Payer ID** and set the **Submitter Type** for the Payer](#add_eligibility_payer_ID). |
| **3** | [Send eligibility enrollment details to Elation as needed](#complete_enrollments). |

ℹ️   **CAUTION** If you add the correct **Eligibility Payer ID** from ClaimMD but are still unable to receive eligibility checks for that Payer, notify Elation with the following details:

- Payer Name
- Payer ID
- NPI(s) associated with the Payer contract
- Name(s) associated with the NPI(s)

## **Adding new Providers**

When adding a new Provider to your practice, you must notify Elation to complete their registration process so eligibility checks can be run for that Provider's patients. To notify Elation:

| | |
| --- | --- |
| **1** | Download [this file](https://elation.my.salesforce.com/sfc/p/37000000L9cg/a/Ui000003PSoz/BkV3AZj5bg1MW0.K5HKS8IhYkvH1Ybs99RRyCD_mFO0) and fill out the following two tabs of the spreadsheet:   - **Group info**: Enter all the Provider or Group NPIs associated with your practice and their TINs. - **Special enrollment**: Enter the following information into each row for **each Payer** that [requires enrollment:](#add_eligibility_payer_ID)   - Payer ID   - NPI(s) associated with the Payer contract   - Name(s) associated with the NPI(s) |
| **2** | Click **I need help** -> **Contact Elation Support**. |
| **3** | Choose **Something else** under **Select an issue**. |
| **4** | Enter the following information in the **Details** box:   - *Please help me complete Provider registration and submit Payer enrollments for RTE. Details are in the attached file.* |
| **5** | Click **Next** to continue to the next step of the contact Support process. |
| **6** | Click **No, I still need help**. |
| **7** | Confirm the **Details** & click **Add Attachment** to attach the filled out spreadsheet. |
| **8** | Click **Next**. |
| **9** | Click **Submit** after confirming the name and email we should contact once the registration is completed. |
| **10** | Enrollments will be completed within two business days, after which you will begin receiving eligibility responses for that payer. |

# **Troubleshooting Common Errors**

## **Incorrect Payer ID selection**

Selecting the wrong Eligibility Payer ID is a common cause of eligibility check failures.

- **Using a commercial payer ID for a Medicare product:** Some payers use different Payer IDs for their commercial plans versus their Medicare Advantage products.
 - For example, UnitedHealthcare's commercial plans may have a different Eligibility Payer ID than AARP-branded Medicare Advantage plans offered through UnitedHealthcare. Always confirm the correct Payer ID for the specific product your patient is enrolled in.
- **Using a generic payer ID when the payer has distinct IDs for eligibility versus claims:** Some payers have separate Payer IDs for eligibility checks and claims submission. The Eligibility Payer ID stored in your Carrier record must match the ID designated for eligibility, not claims.

## **Patient has active coverage but the eligibility response says 'inactive' or 'invalid'**

| | |
| --- | --- |
| **1** | Look up the payer's Eligibility Payer ID on the [ClaimMD Payer List](https://www.claim.md/payer-list). |
| **2** | Compare the Payer ID listed on ClaimMD with the **Eligibility Payer ID** stored in the corresponding Carrier record in Elation. |
| **3** | If the IDs do not match, click the **Edit** (pencil) button next to the Carrier name in your **Insurance Settings** and update the **Eligibility Payer ID** field with the correct value from ClaimMD. |
| **4** | Click **Save**. |

### **If eligibility checks still fail after updating the Payer ID**

If you continue to see failures after confirming and updating the Eligibility Payer ID, contact Elation Support and include the following details:

- Payer name
- Payer ID currently configured in Elation
- Example Patient IDs and dates of failed eligibility checks

## **Provider NPI has not been enrolled for eligibility with payer**

If you see the following error when performing Eligibility checks- ‘*Provider NPI [] has not been enrolled for eligibility with payer []*’, this could mean one of the following:

| | |
| --- | --- |
| **Issue** | **Solution** |
| The Provider/Group did not complete eligibility enrollment for the Payer and will not be able to receive eligibility information until enrollment is completed and approved. | [Notifying Elation about eligibility enrollments](#notify_enrollments). |
| The Provider/Group completed enrollments but the incorrect **Submitter Type** is associated with the Carrier. | Check the **Submitter Type** setting for that Carrier and select the correct type. |

**Payer ID does not support real-time eligibility. Invalid payer name...**

If you see the following error when performing Eligibility checks - ‘*Payer ID … does not support real-time eligibility. Invalid payer name…*’, this could mean one of the following:

| | |
| --- | --- |
| **Issue** | **Solution** |
| The Carrier does not support electronic eligibility checks through ClaimMD. | Verify patient's eligibility via other means. |
| The **Eligibility Payer ID** is not stored in the Insurance Settings for the Carrier. | [Add the **Eligibility Payer ID** to the Carrier](#add_eligibility_payer_ID). |
| The **Eligibility Payer ID** stored in the Insurance Settings for the Carrier is incorrect. | [Verify the **Eligibility Payer ID** for the Carrier and update the **Eligibility Payer ID** to the correct one](#add_eligibility_payer_ID). |

# **Frequently Asked Questions**

**What NPI information is used for an eligibility check?**

The NPI information used for an eligibility check will depend on the following:

- If a patient’s insurance carrier has **Credentialed as a group** listed under **Submitter Type**, then the **Group name** and **Group NPI** configured in the Insurance Settings will be used for both manual and automatic eligibility checks.
- If a patient’s insurance carrier has **Credentialed as individual providers** listed under **Submitter Type**, then the name and NPI of the patient’s **Provider assigned in practice** will be used for both manual and automatic eligibility checks.

#### **How often do I need to update Carrier Settings?**

The **Eligibility Payer ID** rarely changes for a Payer. If you are notified of a change in the Payer's Eligibility ID then [update the **Eligibility Payer ID** in Carrier Settings](#add_eligibility_payer_ID).

The **Submitter Type** typically only changes when you change how you are contracted with a Payer. You can update the Submitter Type as needed.

**I have a Clearinghouse through my billing software. Is Elation connected to my Clearinghouse?** Elation's Real-time Eligibility feature is powered by Elation's connection to ClaimMD. Elation is not connected to your Clearinghouse, even if your Clearinghouse is also ClaimMD.

# **Related Articles**

- [Real-time Eligibility Guide - Checking for patient's insurance eligibility in real-time](https://help.elationemr.com/s/article/Real-Time-Eligibility)
- [Patient Demographics Guide](Patient-Demographics-Guide.md)
- [Patient Demographics Guide- Managing patient insurance](Managing-Insurance.md)