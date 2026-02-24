# Medication History Download Management Guide

Source: https://help.elationhealth.com/s/article/mergingreconciling-downloaded-meds-with-existing-meds

---

Before every patient encounter, you may retrieve the patient's medication information to obtain the latest medications that the patient has filled from the pharmacy, including medications that were prescribed by other physicians who are taking care of the patient.

## **Recommended Reading**

Please reference the [Introduction to Elation's Medication History Download feature](retrieving-previous-medication-history-for-your-patients.md) article to learn how to download medication history for a patient.

## **Contents**

- [Reviewing the list of medications retrieved](#Review)
- [Importing or removing retrieved medications one-by-one](#one)
- [Importing retrieved medications all at once](#all)
- [Not importing any retrieved medications](#not_importing_downloaded_meds)
- [Merging & unmerging medications](#merge)
- [Frequently Asked Questions (FAQ)](#FAQ)

## **Reviewing the list of medications retrieved**

After the medications have been retrieved from Surescripts, an Outstanding Item will appear at the top of the patient's chart with a summary of how many medications were received and the details retrieved for each medication. You may review the medication information retrieved by clicking on the "XX medication fills received" text.

A list of each medication that the patient has obtained from the pharmacy for the past 6 months will display, sorted by the medication and then date. The downloaded medications will also appear highlighted in yellow within in the Clinical Profile.

- **Important Note**:Highlighted medications are not a permanent part of the patient's medication history. Highlighted medications will not display in printed or shared records. You must [sign off](#one) on the highlighted medications before they become a permanent part of the patient's medication history.

Depending on the patient's insurance pharmacy benefits manager (PBM), you will receive some or all of the following information:

- Medication name and strength ("Medication")
- Date that the patient filled the prescription and picked it up from the pharmacy ("Fill Date")
- The number of pills that the pharmacist gave the patient ("Qty")
- The number of days that the medication fill should last the patient before running out ("Supply")
- Physician who prescribed the medication ("Prescriber")

###

By default, downloaded medication fills are grouped together by the National Drug Code (NDC) code that may be supplied to us during the download. If an NDC code was not supplied during the download then medications will not be grouped together.

- **User Tips**:
 - If you wish to separate downloaded medications by strength, Elation can turn a special feature on for you to achieve this. If you are interested in this feature, contact the Support Team using the "I need help" -> "Contact Elation Support" button.
 - Not all downloaded medication fills will come with NDC does. If the Pharmacy Benefits Manager (PBM) does not store the NDC code for the medication then we will not receive any NDC information from the download.

## **Importing or removing retrieved medications one-by-one**

After reviewing the preview of how the retrieved medication will be reconciled with the entire Medication History (or a medication that is already documented in the patient's chart), you accept the reconciliation by signing off on the medication. You two options for sign off:

1. Clicking on the "Sign Off" button for that treatment in the Medication History, as shown below:

![]()

1. Clicking "Actions" >> "Sign Off" in the Clinical Profile, as show below:

![]()

This allows you to inspect each medication listed in the patient chart and reconcile only those medications that you would like to include in the patient's medication list. If you would like to remove a medication fill from the record, you may

1. Clicking on the "Actions" button next to the associated medication in the Medication History and click "Remove"

1. Clicking "Actions" >> "Remove" in the Clinical Profile, as show below:

![]()

**User Tip:** Only Provider level users or their Prescription (Rx) Delegates can sign off on downloaded medication fills.

## **Importing retrieved medications all at once**

If you would like to incorporate all of the retrieved medications with a single click, click on the "Sign" button that is displayed over the "XX medication fills received" item in the Requiring Action queue.

**User Tip:** Only Provider level users or their Prescription (Rx) Delegates can sign off on downloaded medication fills.

Once the retrieved medications have been incorporated into the patient's medication list, the yellow highlights on each medication will disappear, and the patient's medication list will be updated with the current medications that the patient is taking.

**Important Note**: Duplicate medications in the medication list may be created due to the way that the [PBMs provide the information](#duplicate_medications). When duplicates appear we recommend merging them, instead of deleting them, to keep the medication history and fills history accurate.



## **Not importing any retrieved medications**

If you do not wish to incorporate any downloaded medications into the patient's medication list, click "Actions" > "Sign Off & Do NOT Add to Med List" to simply acknowledge the medication history download but **not** import these medications into the chart's med history list. This document now becomes a report.


### **Merging and Unmerging Medications**

For information on how to merge and unmerge medications, please have a look at the [How to manage the patient's medication list](medication-history.md) article.

**Important Note**:When you merge the two medications, Elation takes the name, dosage, and signature of the most recently documented scripts for the medication, and we re-purpose this as the name of the entire medication thread.




## **Frequently Asked Questions (FAQ)**

#### **What's the effectiveness for medication history download?**

Only 60-70% of patients in a regular fee-for-service patient panel will have medications available for download. See question #2 for more details on why this is the case.

#### **Why is the Medication History Download feature not successful for some patients?**

1. Surescripts does not have enough information about the patient, resulting in multiple patients that could match the criteria Elation sent to Surescripts. To avoid HIPAA violations, Surescripts defaults to not sending us information if there is ambiguity around whether we are referencing the same patient.
2. A patient just changed insurance plans (even if it is a different plan with the same insurer). All of this information depends on what information is stored at the patient's insurance plan's pharmacy benefits management system. If there is a change in insurer or pharmacy benefits manager (this is determined by the insurer or self-insured employer), the pharmacy benefits manager will not have the patient's medication refill history because they just started managing that patient's medication usage.
3. The patient has decided to pay for their prescriptions with cash instead of using their insurance to cover the bill. This results in the insurance company not having data about dispensed prescriptions.
4. The patient's insurer is using a Pharmacy Benefits Manager (PBM) that is out of network with Surescripts. Approximately 99% of the PBMs in the USA participate in the [Surescripts network.](https://surescripts.com/network-connections/eprescribing-payers-and-pbms)

#### **How often can medication history be downloaded?**

Medication history can be downloaded every 90 days per patient.


#### **Why is the download creating duplicate medications in the Medication List?**

By default, downloaded medication fills are grouped together by the National Drug Code (NDC) code that may be supplied to us from the Pharmacy Benefits Manager (PBM) during the download. If the PBM did not share certain NDC codes with us then downloaded medications without NDC codes will not be grouped together.

To merge duplicate medications, follow the instructions in the [Merging and Unmerging Medications](#merge) section.

#### **Can I delete medication history download reports?**

Medication history download reports cannot be deleted.


**Which insurers or insurance plans are supported?**

Since insurers can change pharmacy benefits managers or use multiple pharmacy benefits managers depending on the plan, Surescripts avoided making this system dependent on participating insurers. 99% of the pharmacy benefits management companies participate in the [Surescripts network](https://surescripts.com/network-connections/eprescribing-payers-and-pbms).



**Can the Medication History Download feature be turned off?**

The Medication History Download feature cannot be turned off. We recommend clicking the "Sign off & Do Not Add to Med List" option to store each download as a report. This option will keep the downloaded medications separate from the medication list you have maintained.



**Can patients opt-out of medication history download?**

Yes, patients can opt-out of medication history download by emailing Surescripts at [privacyofficer@surescripts.com](mailto:privacyofficer@surescripts.com). Once opted out at the Surescripts level, the patient’s medication history will not be shared with Elation or any other vendor using Surescripts for medication history.





**Next Step**

**Try reconciling the downloaded medications to keep a clear and concise medication list!**

## **Related Articles**

- [Introduction to Elation's Medication History Download feature](retrieving-previous-medication-history-for-your-patients.md)
- [How to manage the patient's medication list](medication-history.md)