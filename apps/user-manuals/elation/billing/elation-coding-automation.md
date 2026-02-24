# Automatic Coding Guide- Automatically code for BMI, Blood Pressure, and negative PHQ-9 documentation

Source: https://help.elationhealth.com/s/article/elation-coding-automation

---

## **Contents**

- [What is the automatic coding feature?](#description)
- [What are the benefits of automatic coding?](#value)
- [Using the automatic coding feature](#how_to)
 - [Enabling automatic coding](#enable_coding)
 - [Applying coding automation in visit notes](#coding_visit_notes)
- [Using vitals related coding automations](#vitals_coding)
 - [Using the *Body Mass Index* coding automation](#BMI)
 - [Using the *Blood Pressure* coding automation](#BP)
- [Using the *PHQ-9* depression screening coding automation](#PHQ9)
- [Frequently Asked Questions (FAQ)](#faq)

## **What is the automatic coding feature?**

Elation's automatic coding feature is designed to help you get credit in quality programs for the documentation already present in your visit note by automatically adding CPT and/or ICD-10 codes to the billing information section of your visit notes based on certain information you store in your visit notes.

Currently this feature applies to body mass index assessments (BMI), blood pressure (BP) recordings, and negative PHQ-9 depression screening results documentation.

## **What are the benefits of automatic coding?**

When automatic coding is enabled for body mass index assessments (BMI), blood pressure (BP) recordings, and negative PHQ-9 depression screening results documentation, Elation uses the documentation already present in your visit note to automatically apply the corresponding CPT or ICD-10 codes to the Billing Information section of your visit note. Your practice no longer need to (1) remember to code, or (2) remember which code needs to be added to the bill, based on the resulting vitals or screening results. This will reduce time spent on double documentation on your practice, allowing you to focus more time on patient care.

## **Using the automatic coding feature**

### **Enabling automatic coding**

Admin Level Users within your practice can turn the automatic coding features on or off by using the toggle in the Settings section.

To adjust your automatic coding preferences:

1. Click on your email at the top of your Elation account and then click "Settings" -> "Billing"
2. Use the toggles next to turn the corresponding coding automations ON (green) or OFF (grey) for any of the listed workflows. Once enabled, the coding automation will work for all users in your practice.

- **User Tip**: When the “Admin only” toggle at the top right of the page is turned on, only Admin Level Users will be able to turn the feature on or off. For more information on Admin privileges, please reference the [User Accounts Guide- Administrative privilege](administrative-privileges.md).

### **Applying coding automation in visit notes**

When automatic coding is turned on, taking certain actions in the visit note, such as entering blood pressure information or importing a PHQ-9 result from the Clinical Profile, will result in associated CPT or ICD-10 codes being automatically inputted in the Billing Information section of associated visit note. Reference the information below to understand how each coding automation works.

## **Using vitals related coding automations**

Simply use the corresponding, structured *Vitals* section in the visit note to record your patient’s BMI and blood pressure to trigger the coding automations listed below.

### **Using the *Body Mass Index* (BMI) coding automation**

For the *Body Mass Index* coding automation, enter the patient's height and weight in the *Vitals* section of the visit note and Elation will automatically input the calculated BMI value's corresponding ICD-10 code in the billing section of the visit note.

- **Important Note**: BMI coding automation is available for patients who are 20 years or older as of the visit note creation date. BMI coding automation is not available for patients under 20 years of age. Manually input the diagnosis codes associated with the BMI percentiles for patients 20 years of age and younger as needed.

The ICD-10 added will correspond to this chart:

| BMI value | ICD-10 Code |
| --- | --- |
| Body mass index (BMI) 19 or less, adult | Z68.1 |
| Body mass index (BMI) 20.0-20.99, adult | Z68.20 |
| Body mass index (BMI) 21.0-21.99, adult | Z68.21 |
| Body mass index (BMI) 22.0-22.99, adult | Z68.22 |
| Body mass index (BMI) 23.0-23.99, adult | Z68.23 |
| Body mass index (BMI) 24.0-24.99, adult | Z68.24 |
| Body mass index (BMI) 25.0-25.99, adult | Z68.25 |
| Body mass index (BMI) 26.0-26.99, adult | Z68.26 |
| Body mass index (BMI) 27.0-27.99, adult | Z68.27 |
| Body mass index (BMI) 28.0-28.99, adult | Z68.28 |
| Body mass index (BMI) 29.0-29.99, adult | Z68.29 |
| Body mass index (BMI) 30.0-30.99, adult | Z68.30 |
| Body mass index (BMI) 31.0-31.99, adult | Z68.31 |
| Body mass index (BMI) 32.0-32.99, adult | Z68.32 |
| Body mass index (BMI) 33.0-33.99, adult | Z68.33 |
| Body mass index (BMI) 34.0-34.99, adult | Z68.34 |
| Body mass index (BMI) 35.0-35.99, adult | Z68.35 |
| Body mass index (BMI) 36.0-36.99, adult | Z68.36 |
| Body mass index (BMI) 37.0-37.99, adult | Z68.37 |
| Body mass index (BMI) 38.0-38.99, adult | Z68.38 |
| Body mass index (BMI) 39.0-39.99, adult | Z68.39 |
| Body mass index (BMI) 40.0-44.99, adult | Z68.41 |
| Body mass index (BMI) 45.0-49.99, adult | Z68.42 |
| Body mass index (BMI) 50-59.99, adult | Z68.43 |
| Body mass index (BMI) 60.0-69.99, adult | Z68.44 |
| Body mass index (BMI) 70 or greater, adult | Z68.45 |

### **Using the *Blood Pressure* (BP) coding automation**

For the *Blood Pressure* coding automation, enter blood pressure readings into the **BP** section of the visit note for any of your hypertensive or diabetic patients and Elation will automatically input the resulting systolic and diastolic value's CPT® codes in the billing section of the visit note.

If multiple blood pressures are recorded in the **BP** fields, the coding automation will input codes for the lowest systolic and diastolic readings across all values entered in the visit note.

- **Important Note**: BP coding automation only applies to hypertensive and diabetic patients who are between 18-85 years of age as of the visit note creation date, and will only occur when documented BP levels are within a controlled range (<140 for systolic and <90 for diastolic). BP coding automation will not occur for patients without an active or controlled diagnosis of hypertension or diabetes in their Clinical Profile or visit note.

The CPT Category II code added will correspond to this chart:

| **Blood Pressure Reading** | **CPT Category II® Code** |
| --- | --- |
| Systolic 130-139 | 3075F |
| Systolic <130 | 3074F |
| Diastolic 80-89 | 3079F |
| Diastolic <80 | 3078F |

###

## **Using the *PHQ-9* depression screening coding automation**

For the *PHQ-9* coding automation, use the 'Depression (PHQ-9 Questionnaire)' to record a patient’s PHQ-9 depression screening results in their Clinical Profile. Afterwards, when you export the completed PHQ-9 screening into a visit note, Elation will automatically input the G8510 CPT code in the billing section of the visit note if the screening results were negative (the PHQ-9 score is between 0-4).

See below for an example:

- **Important Note**: Coding is not automated for patients who have a positive screening result (PHQ-9 score of 5 or higher) through this version of the coding automation. If you would like to automate coding for patients who have a positive screening result, [click here to learn more about the Premium EHR coding automations](https://help.elationemr.com/s/article/Automatic-Coding-Guide-Advanced-Coding-Automations).

For more information about how to fill out the PHQ-9 clinical form in the Clinical Profile, please see [Clinical Profile Guide- Structured Questionnaires](structured-questionnaires.md).

##

## **Frequently Asked Questions (FAQ)**

#### **Are there additional coding automations available in Elation?**

Yes, there are additional coding automations available as part of Elation's Premium EHR subscription. [Click here to learn more about the Premium EHR coding automations](https://help.elationemr.com/s/article/Automatic-Coding-Guide-Advanced-Coding-Automations).

#### **Can I create my own coding automations in Elation?**

Yes, you can automatically apply CPT, CPT II, or HCPCS codes to a bill by using the Document Tags feature. To create your own coding automations using Document Tags:

1. First, you need to create a Document Tag with an associated CPT, CPT II, or HCPCS code.
   1. Click the "Tag" button in a Report or Document.
   2. Enter a name for the Document Tag in the *Edit Document Tags* window.
   3. Click the "Add new tag" button at the bottom of the window.
   4. Enter a description if needed.
   5. Select whether the code you want to associate with the tag is a *CPT*, *CPT II* or *HCPCS* code.
      - Coding automation is not available for *ICD-9*, *ICD-10*, *LOINC* or *SNOMED* codes.
   6. Enter the code for the Document Tag in the code field.
   7. Click "Save" to save the Document Tag and associated code.
2. Next, apply the Document Tag to the a visit note to input the associated code in the bill.

[Click here to learn more about Document Tags](https://help.elationemr.com/s/article/tag-reports-and-notes-with-document-tags).

## **Related Articles**

- [Automatic Coding Guide- Advanced coding automations (Premium)](https://help.elationemr.com/s/article/Automatic-Coding-Guide-Advanced-Coding-Automations)
- [Visit Note Documentation Guide- Best practices for documenting a patient encounter](Best-practices-for-documenting-a-patient-encounter.md)
- [Billing Guide- Creating a Super Bill and coding for your visit](billing.md)
- [Clinical Profile Guide- Structured Questionnaires](structured-questionnaires.md)