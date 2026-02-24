# Real-time Eligibility Guide - Checking for patient's insurance eligibility in real-time (Paid Add-On)

Source: https://help.elationhealth.com/s/article/Real-Time-Eligibility

---

# **Contents**

- Overview
 - [What is Real-time Eligibility?](#description)
 - [What are the benefits of the Real-time Eligibility feature?](#value)
- [Setup](#getting_started)
 - [Enabling Real-time Eligibility](#Enable)
 - [Completing registration & configuring Settings](#configure_settings)
- [Workflow Instructions](#workflow_instructions)
 - [Viewing updates to the demographics box](#demographics)
 - [Running manual eligibility checks](#manual_eligibility_checks)
 - [Running automated eligibility checks for patients with appointments](#automated_eligibility_checks)
 - [Viewing eligibility status in the patient's demographics](#status_demographics)
 - [Viewing eligibility status in the Clinical Profile](#status_clinical_profile)
 - [Viewing eligibility status in the Appointment](#status_appointment)
 - [Managing mismatched demographics](#mismatched_demographics)
 - [Documenting eligibility checks when real-time eligibility is unavailable](#document_eligibility)
- [Frequently Asked Questions (FAQ)](#faq)

# **Overview**

## **What is Real-time Eligibility?**

Real-time Eligibility in Elation EHR enables you to request a patient's primary and secondary insurance eligibility, coverage, and benefits based on the insurance details in their demographics. If the request is successful, the retrieved information will be displayed in the patient's demographics for easy access.

## **What are the benefits of the Real-time Eligibility feature?**

Real-time Eligibility is valuable because

- it allows you to request updated insurance information from patients if their coverage has lapsed, especially while they are in the office with you.
- the eligibility, coverage and benefits details will allow you to collect any patient responsibility at the point of care, if preferred.
- the eligibility, coverage and benefits details will allow you to inform the patient in advance for any additional responsibility they may have for the services rendered.

# **Setup**

## **Enabling Real-time Eligibility**

This Real-time Eligibility feature is a custom add-on product for EHR customers. This feature comes with additional costs. If you would like to use this feature, please reach out to Elation using the **I need help** -> **Contact Elation Support** button and a member of our team will reach out to assist you.

## **Completing registration & configuring Settings**

ℹ️   **REQUIREMENT** You must follow the instructions in this article to correctly register your practice and set up your Carriers to ensure you successfully receive eligibility information: [Click here for instructions on how to set up your Payers for eligibility checks](https://help.elationemr.com/s/article/Real-time-Eligibility-Set-Up-Payers).

In the above article you will find instructions for the following:

1. Reviewing your Insurance Eligibility Settings.
2. Configuring the **Eligibility Payer ID** and **Submitter Type**for each carrier you want to run eligibility checks for.
3. Sending credentials and eligibility enrollment details to Elation.

Once you have completed registration and configured your settings, you can start using the Real-time Eligibility feature.

# **Workflow Instructions**

## **Viewing updates to the demographics box**

In each patient's Demographics Box, you will see a section at the top of the **Primary Insurance** and **Secondary Insurance** sections for Eligibility Checks.

- If insurance information is empty, you will see text that says *'Enter insurance information to run eligibility check.'*. You must enter insurance information for the patient in order to run an eligibility check.
- If you see text that says *'Payer ID … does not support real-time eligibility. Invalid payer name…'* it means one of three things:
 - The Carrier does not offer electronic eligibility checks and they do not have an Eligibility Payer ID.
 - The Eligibility Payer ID is not entered in your Insurance Settings for the Carrier.
 - The Eligibility Payer ID entered in your Insurance Settings for the Carrier is incorrect.
- If you see a blue **Check Eligibility** button and text that says '*Run eligibility check to view insurance status*', it means eligibility check is available for the Carrier and you can click the **Check Eligibility** button to run an eligibility check.

**💡**  **USER TIP** If the **Check Eligibility** button is disabled, hover your mouse over the button to see why it is disabled and then add/correct the information needed to continue checking eligibility.

## **Running manual eligibility checks**

There are two ways to manually check insurance eligibility:

1. **From Patient Demographics** - Click the **Check Eligibility** button in the Patient Demographics to run eligibility checks for the patient's **Primary Insurance** and **Secondary Insurance**.

![]()

1. **From an Appointment** - Click the **Check Eligibility** button in the Create Event dialogue for a new appointment or in any created appointment for a patient to run an eligibility check for the patient's **Primary Insurance**.

![]()

Eligibility checks may take up to 20 seconds to run. Once the eligibility check is complete, the status of the eligibility check as well as the details of successful eligibility checks will appear in the demographics and/or appointment.

**💡**  **USER TIPS**

- If you see the following error when performing Eligibility Checks - *'Payer ID … does not support real-time eligibility. Invalid payer name…',* this could mean one of three things:
 - The Carrier does not support Eligibility checks.
 - The Eligibility Payer ID is not stored in the Insurance Settings for the Carrier.
 - The Eligibility Payer ID stored in the Insurance Settings for the Carrier is incorrect.
- If the **Check Eligibility** button is disabled, hover your mouse over the button to see why it is disabled and then add/correct the information needed to continue checking eligibility.

## **Running automated eligibility checks for patients with appointments**

Each night at approximately 3:30 AM Eastern, Elation will automatically run an eligibility check for patients who

1. have an appointment in the Elation Calendar for the following day **AND**
2. who have an eligibility enabled Carrier on file

This feature is automatic and does not need to be configured or enabled in any way. This feature cannot be disabled at this time.

## **Viewing eligibility status in the patient's demographics**

Eligibility response information will display above the **Primary Insurance** and **Secondary Insurance** information. The summarized eligibility details will display the date the insurance eligibility check was run, status of the insurance, Copay, Coinsurance, remaining Deductible and Effective Date as long as the information is made available by the Payer.

This is what the Eligibility response summary information will look like:

![]()

To view the full details of the Eligibility response, click the **Open Full Report** button under the summary. The full details of the eligibility response can include:

- a breakdown of various coverages & benefits
- coverage level
- prior authorization requirements
- out of pocket costs
- coverage limitations

This is an example of what the full report looks like. You may click on the header of the different objects (ex. Copay, Coinsurance) or Service Type (ex. General, Physical Therapy) to filter for specific details.

![]()

## **Viewing eligibility status in the Clinical Profile**

New icons have been added to the Clinical Profile next to the patient's Primary Insurance to display the status of the Primary Insurance's eligibility. The Clinical Profile will not display the status of the Secondary Insurance's eligibility.

![]()

The icon will change to one of the following depending on the status:

| Icon | Status |
| --- | --- |
| | Eligibility not run- click into the demographics to run an eligibility check |
| | Active |
| | Inactive |
| | Error - additional or updated information is needed for eligibility check |

## **Viewing eligibility status in the Appointment**

A new section has been added to the *Create Event* box and *Appointment* details to show the Eligibility status of the the patient's Primary Insurance. The summarized eligibility details will display the date the insurance eligibility check was run, status of the insurance, Copay, Coinsurance, remaining Deductible and Effective Date as long as the information is made available by the Payer. You can click the **Open Full Report** button to view the details of the eligibility response.

![]()

If you do not see any **Primary Insurance** information in the appointment, it means the patient does not have **Primary Insurance** information on file.

## **Managing mismatched demographics**

If the information returned in the Eligibility response does not match what is on file in the patient's Demographics, a notification will appear in the Demographics or Appointment that says *'Updated information from ... fields is available from eligibility response.'*Click the **View** button to view the discrepancies or click the **Dismiss** button to dismiss the notification and view it again the next time you view the patient's Demographics.

- If you click the **View** button to view the discrepancies, Elation will show you the information you have on file alongside the information provided by the Eligibility Report to allow you to compare the information. You can then check off the Demographics fields you want to update using the information from the Eligibility Report and click **Update All Fields** to make use of the new information.

![]()

**💡**  **USER TIPS**

- Eligibility checks for a patient with Primary and Secondary Insurance may yield conflicting suggestions (ex: the Carrier for Primary Insurance says the patient’s address should be ‘123 Main St.’ while the Carrier for the Secondary Insurance says the patient’s address should be ‘456 Index Ave.’). In these cases, it may be best to have the patient correct their information with their insurance carrier(s).
- If a carrier returns the **Patient relation to policyholder** field value as 'Other', it means it did not match any of the existing relationship options offered by Elation ('Child', 'Self' or 'Spouse').

## Documenting eligibility checks when real-time eligibility is unavailable

Some payers do not support real-time eligibility checks, or you may need to verify eligibility outside of Elation (for example, by calling the payer or checking their online portal). In these cases, use the Notes field in the patient's insurance section to document your manual verification.

To record a manual eligibility verification:

| | |
| --- | --- |
| 1 | Open the patient's chart and click on the patient's name to open their demographics. |
| 2 | Scroll to the Insurance, Payment & Membership section and locate the relevant insurance record (Primary, Secondary, or Tertiary). |
| 3 | In the Notes field, enter details about your verification, such as:   - Date and time of verification - Method used (phone call, payer portal, etc.) - Key financial details confirmed (deductible remaining, copay amount, coinsurance percentage, etc.) - Name of representative spoken to (if applicable) |
| 4 | Click Save & Close. |

**Example note:** *Verified via BlueCross portal on 1/23/2026. Active coverage confirmed. Deductible: $500 remaining. Copay: $25 for office visit. - JSmith*

💡   **USER TIP** For per-visit context, you can also add notes in the Billing notes field within the appointment. To do this, click on the appointment, click Edit, and enter details in the Billing notes field.

# **Frequently Asked Questions (FAQ)**

#### **Why is the "Check Eligibility" button disabled for a patient?**

The **Check Eligibility** button will be disabled if Elation receives a certain error when trying to run an eligibility check for a patient. If the **Check Eligibility** button is disabled, hover your mouse over the button to see why it is disabled and then add/correct the information needed to continue checking eligibility.

#### **How long will it take to receive results after requesting an eligibility check?**

It may take 10-20 seconds to receive results after requesting an eligibility check.

#### **When will automatic eligibility checks be run? Can I configure when automatic eligibility checks will be run?**

An automatic job will run nightly (around 3:30am Eastern) to perform eligibility checks for all patients with appointments scheduled for the following day. This functionality cannot be configured at this time.

#### **How are the summarized copay, coinsurance, and remaining deductible amounts in Demographics, Appointment Details, and Create an Event selected?**

Elation will attempt to find values for copay, coinsurance, and remaining deductible for each combination below. If a value is not found for a combination, the next combination will be tried.

If multiple matching values are returned for a given category in a combination (ex: 2 'In Network' $25 copays for 'Individual' coverage level for service type code 98), then that value will be displayed.

If multiple different values are returned for a given category in a combination (ex: 1 $25 copay and 1 $50 copay that are both 'In Network' for 'Individual' coverage level for service type code 98), then a **See Full Report** message will display.

The sequence and combinations below may be refined over time

| | | | |
| --- | --- | --- | --- |
| **Sequence** | **Service Type Code** | **Coverage Level** | **In-Network** |
| 1 | 30 - Health Benefit Plan Coverage | Individual | Yes, Not Applicable, or (blank) |
| 2 | 30 - Health Benefit Plan Coverage | Employee | Yes, Not Applicable, or (blank) |
| 3 | 30 - Health Benefit Plan Coverage | (Any) | Yes, Not Applicable, or (blank) |
| 4 | 98 - Professional Physician Office Visit | Individual | Yes, Not Applicable, or (blank) |
| 5 | 98 - Professional Physician Office Visit | Employee | Yes, Not Applicable, or (blank) |
| 6 | 98 - Professional Physician Office Visit | (Any) | Yes, Not Applicable, or (blank) |
| 7 | 96 - Professional Physician | Individual | Yes, Not Applicable, or (blank) |
| 8 | 96 - Professional Physician | Employee | Yes, Not Applicable, or (blank) |
| 9 | 96 - Professional Physician | (Any) | Yes, Not Applicable, or (blank) |
| 10 | BZ - Physician Visit Well | Individual | Yes, Not Applicable, or (blank) |
| 11 | BZ - Physician Visit Well | Employee | Yes, Not Applicable, or (blank) |
| 12 | BZ - Physician Visit Well | (Any) | Yes, Not Applicable, or (blank) |
| 13 | BY - Physician Visit Sick | Individual | Yes, Not Applicable, or (blank) |
| 14 | BY - Physician Visit Sick | Employee | Yes, Not Applicable, or (blank) |
| 15 | BY - Physician Visit Sick | (Any) | Yes, Not Applicable, or (blank) |

#### **What should I do if the eligibility check results in an error?**

Details on the cause of the error should be displayed in Elation. Please use the available information to resolve any data issues. You can then click the **Check Eligibility** button after updating the information to re-run the eligibility check.

For example, if you see the error *'Payer ID … does not support real-time eligibility. Invalid payer name…’*, double check that the correct **Eligibility Payer ID** is added to the Carrier in Elation.

#### **What NPI information is used for an eligibility check?**

The NPI information used for an eligibility check will depend on the following:

- If a patient’s insurance carrier has **Credentialed as a group** listed under **Submitter Type**, then the **Group name** and **Group NPI** configured in the Insurance Settings will be used for both manual and automatic eligibility checks.
- If a patient’s insurance carrier has **Credentialed as individual providers** listed under **Submitter Type**, then the name and NPI of the patient’s **Provider assigned in practice** will be used for both manual and automatic eligibility checks.

📖 **RECOMMENDED READING**

[Click here for instructions on how to set up your Payers for eligibility checks](https://help.elationemr.com/s/article/Real-time-Eligibility-Set-Up-Payers).

**I have a Clearinghouse through my billing software. Is Elation connected to my Clearinghouse?** Elation's Real-time Eligibility feature is powered by Elation's connection to ClaimMD. Elation is not connected to your Clearinghouse, even if your Clearinghouse is also ClaimMD.

#### Is there a manual "eligibility confirmed" toggle?

Elation does not currently have a dedicated toggle or button to manually mark eligibility as confirmed. The eligibility status icon in the Clinical Profile and Demographics reflects the most recent successful automated or manual real-time eligibility check run through Elation.

For payers that do not support real-time eligibility, or when you verify eligibility outside of Elation (via phone or payer portal), record your verification details in the Notes field within the patient's insurance record in Demographics. You can also use the Billing notes field in the appointment for visit-specific context.

#### What if my payer doesn't support real-time eligibility?

If you see the message *'Payer ID … does not support real-time eligibility. Invalid payer name…'* it means one of the following:

- The Carrier does not offer electronic eligibility checks.
- The Eligibility Payer ID is not entered in your Insurance Settings for the Carrier.
- The Eligibility Payer ID entered in your Insurance Settings for the Carrier is incorrect.

**If the payer does not support electronic eligibility checks:**

| | |
| --- | --- |
| 1 | **Verify eligibility directly** - Contact the payer by phone or through their online portal. |
| 2 | **Document your verification** - [Click here for full instructions](#document_eligibility). |
| 3 | **Add visit-specific notes (optional)** - Add notes in the Billing notes field within the appointment for per-visit context. |

**I****f you believe the payer should support eligibility checks:**

Verify the Eligibility Payer ID is correctly configured in your Insurance Settings. Reference the [Real-time Eligibility Guide - Setting up Payers for eligibility checks](https://help.elationemr.com/s/article/Real-time-Eligibility-Set-Up-Payers) for instructions on how to add or correct the Eligibility Payer ID.

# **Related Articles**

- [Real-time Eligibility Guide - Setting up Payers for eligibility checks](https://help.elationemr.com/s/article/Real-time-Eligibility-Set-Up-Payers)
- [Patient Demographics Guide](Patient-Demographics-Guide.md)
- [Patient Demographics Guide- Managing patient insurance](Managing-Insurance.md)