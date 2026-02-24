# Patient Chart Guide- Managing confidential records

Source: https://help.elationhealth.com/s/article/confidential-items-in-your-patient-chart

---

## **Contents**

- [What are confidential records?](#description)
- [What are the benefits of separating confidential records?](#value)
- [Confidential section of the clinical profile](#confidential_section)
- [Marking records as confidential](#confidential_section)
- [Confidential Records and Patient Passport](#confidential_passport)
- [Confidential records & shared charts](#shared_charts)
- [21st Century Act and Information Blocking](#Cures_Act)
- [Frequently Asked Questions](#faq)

## **What are confidential records?**

Confidential records are text, notes, orders, reports or other documents that you do not want to share with patients or anyone you are collaborating with to care for your patient outside of your practice. Confidential records in the patient's chart consists of:

1. a *Confidential* section in the Clinical Profile that allows you to document and store confidential and private notes for the patient that can only be seen by members of your office. Notes in the *Confidential* section will never be printed, will not be visible in Passport and will not be shared outside of your practice when you attach the Clinical Profile to any Provider Letters or Referral Orders.
2. ability to mark any record/document in the patient's chart as 'Confidential' to allow any member of your practice to take caution when sharing the record/document outside of your practice.

   - **Important Note:** The “Keep as confidential” checkbox on visit notes is intended to call attention to visit notes marked as confidential to ensure that confidential visit notes are only shared explicitly (and not implicitly) with third parties (other than the patients) via features like Letters or Referral Orders — it does not impact which, and how, visit notes are shared with patients via Passport. A signed visit note will always be shared with the patient as a visit summary via Passport, whether the note is marked confidential or not, and those visit summaries include the information documented in the following sections of the visit note:
     - **Vitals**
     - **Plan** (\*SOAP [Visit Note Format](https://help.elationemr.com/s/article/Visit-Note-Documentation-Guide-Visit-Note-Formats) only)
     - **Proc** (Procedure)
     - **Tests/Treatments**
       - This includes any Referrals, medications and diagnostic test orders.
     - **Care Plan** (Instructions)
     - **F/U** (Follow-up)

## **What are the benefits of separating confidential records?**

It is important to separate confidential records to allow you to confidently share only records you want to share with anyone outside of your practice.

- Notes in the *Confidential* section of the Clinical Profile will never be printed or shared outside of your practice.
- If you mark a record as 'Confidential, that record will always have a special indicator that can be seen from anywhere in the patient's chart- this will allow members of your practice to take caution when printing or sharing the record
- If you mark a record as 'Confidential, that record will not be shared when you generate [C-CDA (CCDA) files](Supported-Elation-CCDA-types.md) for the patient

## **Confidential section of the Clinical Profile**

Every patient chart has a *Confidential* section in the [Clinical Profile](clinical-profile-record-patient-medical-history.md) section of their chart. The *Confidential* section is at the very bottom of the Clinical Profile. Any information added to this *Confidential* section by any member of your practice:

1. can be viewed and edited by anyone in your practice
2. will never be printed or shared whenever you print the Clinical Profile or share the Clinical Profile through Patient Passport or Letter/Referral
3. will never be exported when exporting the contents of the patient chart as a [C-CDA (CCDA) file](Supported-Elation-CCDA-types.md)
4. will never be shared with or visible to other providers using the Patient Longitudinal Record or Collaborative Health Record features (if you are using these features).

## **Marking records as confidential**

Any member of your practice can mark any notes, orders, reports or documents as 'Confidential' in the patient's chart. To mark records as confidential:

1. Use the "Keep this confidential" checkbox at the bottom of notes and orders

![]()

1. Click the "Action" >> "Mark Confidential" button next to any signed notes, orders, reports or documents

If you need to remove the 'Confidential' marker on any record, click "Actions" >> "Unmark Confidential".

**Important Note**: Letters, referrals, prescriptions and office messages cannot be marked as 'Confidential' using this feature.

​​​

## **Confidential Records and Patient Passport**

To withhold confidential or sensitive information from patients for patient safety reasons, we recommend using the [Confidential section of the Clinical Profile](#confidential_section).

The “Keep this confidential” checkbox on documents is intended to call attention to records marked as confidential to ensure that these confidential records are only shared explicitly (and not implicitly) with patients when sharing records via Patient Letters; with the exception of visit notes. The confidential checkbox on visit notes does not impact which visit notes are shared with patients via Passport. Visit summaries for all signed visit notes are always automatically shared with Patient Passport Users regardless of whether or not the visit note is marked as confidential, and those visit summaries include the information documented in the following sections of the visit note:

- **Vitals**
- **Plan** (\*SOAP [Visit Note Format](https://help.elationemr.com/s/article/Visit-Note-Documentation-Guide-Visit-Note-Formats) only)
- **Proc** (Procedure)
- **Tests/Treatments**
 - This includes any Referrals, medications and diagnostic test orders.
- **Care Plan** (Instructions)
- **F/U** (Follow-up)

## **Confidential records & shared charts**

The [Collaborative View](the-collaborative-view-hi-only.md) and [Patient Longitudinal Record (PLR)](introducing-elations-patient-longitudinal-record-enterprise-only.md) are special features used by large groups of Elation users who are part of the same geographic location or Enterprise.

By marking certain records as 'Confidential' in your patient's chart, you will be able to withhold the data within those records and prevent the records from being seen by collaborating providers.

**Important Note**: Only records that are automatically shared through these features (visit notes, non-visit notes, reports, and orders) can be marked as 'Confidential'. Anything marked 'Confidential' can still be manually shared via Letters or Referrals but you will see a 'Confidential' marker on the record to allow you review the record before choosing to share it outside of your practice.

## **21st Century Cures Act and Information Blocking**

The 21st Century Cures Act Information Blocking provision was effective beginning April 5, 2021. The Information Blocking Provision requires health care actors, like providers, to not take any action that constitutes blocking of Electronic Health Information (EHI). There are some exceptions that allow for patient information to not to be shared with patients and Elation recommends only using the Confidential section of the Clinical Profile for information that fits the Information Blocking exceptions conditions. If you are not sure if your use case meets the exception conditions, consult a legal resource. ([Read more about the 21st Century Cures Act here](21st-Century-Cures-Act-and-Elation-EHR.md) and [read more about Information Blocking Provisions here](Cures-Act-Staying-compliant-with-Information-Blocking-Provisions.md).)

## **Frequently Asked Questions (FAQ)**

#### **Can I set it so that only specific members of my practice can edit 'Confidential' information and records?**

The 'Confidential' feature can be used by both staff and provider and you cannot set it so that only specific members of your practice can use this feature. Elation has a [VIP Charts](vip-chart-feature.md) feature that will give you more control over who in your office has access to patient records. Please feel free to explore the [VIP Charts](vip-chart-feature.md) feature.


#### **Can I set it so that only****specific members of my practice** **can view 'Confidential' information and records?**

'Confidential' information and records can be seen by anyone that has access to your Elation EHR practice. You can set additional security around chart access using the [VIP Charts](vip-chart-feature.md) feature. Please feel free to explore the [VIP Charts Guide](vip-chart-feature.md) to learn more about the feature.

#### **Why can't I mark letters, referrals, prescriptions and office messages as 'Confidential'?**

This feature is not available in Elation at this time. Elation will notify you when this feature becomes available.



## **Related Articles**

- [Clinical Profile Guide- A snapshot of the patient's health status](clinical-profile-record-patient-medical-history.md)
- [VIP Charts- Limiting access to certain patient charts](vip-chart-feature.md)
- [Collaborative Health Record View Guide](the-collaborative-view-hi-only.md)
- [Patient Chart Guide- Using the Patient Longitudinal Record (PLR) to share patients within a network](introducing-elations-patient-longitudinal-record-enterprise-only.md)
- [21st Century Cures Act Guide- Staying compliant with Information Blocking Provisions](Cures-Act-Staying-compliant-with-Information-Blocking-Provisions.md)