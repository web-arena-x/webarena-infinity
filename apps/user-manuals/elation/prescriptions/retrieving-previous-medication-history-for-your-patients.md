# Medication History Download Introduction

Source: https://help.elationhealth.com/s/article/retrieving-previous-medication-history-for-your-patients

---

## **Contents**

- [What is Medication History Download?](#WhatIsMedHistoryDownload)
- [Why is Medication History Download valuable?](#WhyIsItValuable)
- [What do I need in order to use the Medication History Download feature?](#WhatDoINeed)
- [How do I trigger a Medication History Download?](#HowToTriggerDownload)
- [How do I manage downloaded medications?](#ManageDownloadedMeds)
- [Frequently Asked Questions (FAQ)](#FAQ)

###

## **What is Medication History Download?**

Elation has partnered with Surescripts, an information technology company that supports electronic transmission of medical records, to offer Medication History Download to retrieve data related to the last 6 months of medications that your patient has retrieved from their pharmacies. This medication history is independent of which prescriber wrote the script for the patient. Surescripts retrieves this information from the pharmacy benefits managers [PBM] (companies that manage drug benefits on behalf of insurers) connected to their network.

###

## **Why is Medication History Download valuable?**

This feature is a convenient way to populate the patient's medication list automatically when first transitioning to the Elation platform. You can also use this feature to maintain up to date knowledge of all medications received by your patient from all of their clinical caretakers.

###

## **What do I need in order to use the Medication History Download feature?**

In order use the medication history download feature, the following requirements must be met:

1. The "Provider assigned in practice" must have ePrescribing privileges in Elation and must have sent 5 prescriptions electronically through Elation
2. Patient charts must have the following information in the [Patient Demographics](https://help.elationemr.com/s/article/Patient-Demographics-Guide)
   - **Legal first name**
   - **Legal last name**
   - **Date of birth**
   - **Sex at birth**
   - **City**
   - **Zip**

**User Tip:** Surescripts uses the demographic information in the chart to attempt to match the patient with the prescription insurance information. The more demographic information you can document in the patient chart, the higher the chance of obtaining a match and successfully retrieving the patient's medication history.

## **How do I trigger a Medication History Download?**

### **Automation from schedule appointments**

Elation can automatically retrieve your patients' medication history. To trigger an automatic download, ensure all patients with appointments have their appointment documented in the Elation calendar by 9pm (local time) the day before the appointment. Elation will attempt to download medication history for all patients on the calendar the night before their appointment.

If a download was successful, you will see the medication history report in the 'Outstanding Items' section at the top of the patient’s chart. The report will list all of the prescriptions retrieved since the previous download or up to the past 6 months depending on when the last download occurred.

### **Manual Download**

You can retrieve the medication history "on demand" for a patient by following one of the steps below:

- **(From the Calendar)** To trigger a manual download from the calendar, especially for walk-in patients,
 1. Add the patient's appointment to the Elation Calendar.
 2. Update the appointment status from ‘Scheduled’ to ‘Checked In’.
 3. A new dialog titled ‘Confirm Patient Details for:...’ will open up
 4. Verify the patient’s demographic information and then click the "Save & Close " button.
 5. Elation will attempt to download medication history for the patient. If a download was successful, you will see the medication history report in the Outstanding Items section at the top of the patient’s chart. The report will list all of the prescriptions retrieved since the previous download or up to the past 6 months depending on when the last download occurred.
- **(From the chart)** To trigger a manual download from the patient’s chart,
 1. Open the patient's chart
 2. Click the "Meds Hx" button in the gray navigation bar and then click "Download Fills"
 3. Elation will attempt to download medication history for the patient. If a download was successful, you will see the medication history report in the Outstanding Items section at the top of the patient’s chart. The report will list all of the prescriptions retrieved since the previous download or up to the past 6 months depending on when the last download occurred.
     - If a medication history download attempt was made within the last 24 hours then another attempt cannot be made.

**Important Note:** We cannot guarantee retrieval of medication history for all patients. See the [Frequently Ask Questions](#FAQ) section below to learn more about the limitations.

###

## **How do I manage downloaded medications?**



The [How to manage downloaded medication history](mergingreconciling-downloaded-meds-with-existing-meds.md) article will guide you on how to manage downloaded medications.


## **Frequently Asked Questions (FAQ)**

#### **What's the effectiveness for medication history download?**

Only 60-70% of patients in a regular fee-for-service patient panel will have medications available for download. See question #2 for more details on why this is the case.

#### **Why is the Medication History Download feature not successful for some patients?**

1. Surescripts does not have enough information about the patient, resulting in multiple patients that could match the criteria Elation sent to Surescripts. To avoid HIPAA violations, Surescripts defaults to not sending us information if there is ambiguity around whether we are referencing the same patient.
2. A patient just changed insurance plans (even if it is a different plan with the same insurer). All of this information depends on what information is stored by the patient's insurance plan's pharmacy benefits management system. If there is a change in insurer or pharmacy benefits manager (this is determined by the insurer or self-insured employer), the pharmacy benefits manager will not have the patient's medication refill history because they just started managing that patient's medication usage.
3. The patient has decided to pay for their prescriptions with cash instead of using their insurance to cover the bill. This results in the insurance company not having data about dispensed prescriptions.
4. The patient's insurer is using a Pharmacy Benefits Manager (PBM) that is out of network with Surescripts. Approximately 90% of the PBMs in the USA participate in the [Surescripts network.](https://surescripts.com/network-connections/eprescribing-payers-and-pbms)

#### **How often can medication history be downloaded?**

Medication history can be downloaded every 90 days per patient.

**Which insurers or insurances plans are supported?**

Since insurers can change pharmacy benefits managers or use multiple pharmacy benefits managers depending on the plan, Surescripts avoided making this system dependent on participating insurers. 90% of the pharmacy benefits management companies participate in the [Surescripts network](https://surescripts.com/network-connections/eprescribing-payers-and-pbms).



**Can the Medication History Download feature be turned off?**

The Medication History Download feature cannot be turned off because it is a valuable tool for Elation users to maintain awareness of all medications received by their patients. We recommend clicking the "Sign off & Do Not Add to Med List" option to store each download as a report. This option will keep the downloaded medications separate from the medication list you have maintained.



**Can patients opt-out of Medication History Download?**

Yes, patients can opt-out of Medication History Download by emailing Surescripts at [privacyofficer@surescripts.com](mailto:privacyofficer@surescripts.com). Once opted out at the Surescripts level, the patient’s Medication History will not be shared with Elation or any other vendor using Surescripts for Medication History.

##

**Next Step

Try downloading medication history for a patient!**





**Related Articles**

- [How to manage downloaded medication history](mergingreconciling-downloaded-meds-with-existing-meds.md)
- [How to manage the patient's medication list](medication-history.md)