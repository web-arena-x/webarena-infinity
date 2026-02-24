# Coding Guide- Managing deprecated, non-billable ICD-10 codes

Source: https://help.elationhealth.com/s/article/Managing-deprecated-ICD10-codes

---

## **Contents**

- [What are deprecated ICD-10 codes?](#description)
- [Why is it important to recognize deprecated codes?](#value)
- [How to update deprecated ICD-10 codes](#updated_deprecated_ICD10)
- [How can I locate patient charts with deprecated ICD-10 codes?](#search_code)
- [Frequently Asked Questions (FAQ)](#faq)

## **What are deprecated ICD-10 codes?**

Deprecated ICD-10 codes are ICD-10 codes that are no longer billable according to the Centers for Medicare & Medicaid Services (CMS) guidelines. ICD-10 codes are updated by CMS every year and include ICD-10 code deletions, as well as additions and revisions.

In Elation, deprecated ICD-10 codes are indicated by an orange dot in the Problem List of the patient’s Clinical Profile and are labeled as “non-billable codes”. The total number of deprecated ICD-10 codes is listed in a banner at the top of the Problem List.

![]()



## **Why is it important to recognize deprecated codes?**

It is important to recognize which codes have been deprecated by CMS because submitting a claim with any deprecated codes will lead to claim rejections. Using Elation’s deprecated ICD-10 codes feature to identify and update ICD-10 codes will help ensure that only valid ICD-10 codes are referenced in your encounter and billing documentation.

**Important Note**: If you do not submit any ICD-10 codes for billing, you can ask Elation to turn on a feature to hide the deprecated ICD-10 code indicators from your Problem List. Contact the Support Team using the “I need help” -> “Contact Support Button” button at the top of your Elation account if you want Elation to turn this feature on.




## **How to update deprecated ICD-10 codes**

There are two ways to update deprecated ICD-10 codes in a patient’s chart:

1. Fix all deprecated codes in the Problem List using the "Fix" button
   1. Look for a banner at the top of the Problem List that tells you, if any exist, how many non-billable (deprecated) ICD-10 codes are in the Problem List.
   2. Click "Fix” to start updating deprecated ICD-10 codes.
   3. Find a replacement ICD-10 code in the diagnosis search & select it from the ICD-10 database.
   4. Click the “x” to the right of the deprecated code to delete to disassociate the deprecated code from the problem.
   5. Click "Save" to save your changes.
   6. Repeat steps 2 to 5 until the banner is gone.

![]()

1. Edit individual problems
   - To edit a specific Problem with a deprecated code:
     1. Click "Actions" >> "Edit" next to the problem.
     2. Find a replacement ICD-10 code in the diagnosis search & select it from the ICD-10 database.
     3. Click the “x” to the right of the deprecated code to delete to disassociate the deprecated code from the problem.
     4. Click "Save" to save your changes.

![]()




## **How can I locate all patient charts with deprecated ICD-10 codes?**

Search for patient charts with deprecated ICD-10 codes using the [Patient List Report](find-patients-with-elations-patient-list.md) so that you can proactively update the deprecated codes to active, billable codes.

Follow the steps below to locate patient charts with deprecated ICD-10 codes:

1. Click the "Reports" button in the blue navigation bar.
2. Click "Patient List".
3. Enter one of the deleted ICD-10 codes in the Active Problems in Clinical Profile box to filter for only patients who have that code in their Problem List.
    Once you are ready to generate your report, click "Generate List"
4. Once you are ready to generate your report, click "Generate List"
   - **User Tip**: If you would like to apply additional filtering, reference our [Patient List Report Guide](https://help.elationemr.com/s/article/find-patients-with-elations-patient-list) for additional guidance.
5. The list of patients with the corresponding deprecated ICD-10 code will appear on the right of the screen. Click on each patient's name to open their chart and find the ICD-10 code you searched for in their Problem List.
6. Click "Actions" >> "Edit" next to the problem.
7. Find a replacement ICD-10 code in the diagnosis search & select it from the ICD-10 database.
8. Click the “x” to the right of the deprecated code to delete to disassociate the deprecated code from the problem.
9. Click "Save" to save your changes.
10. Repeat steps 5 to 9 for each affected patient.
11. Repeat steps 1 to 10 for each deprecated ICD-10 code.



## **Frequently Asked Questions**

#### **What happens if I send a claim with a deprecated code?**

Your claim will be rejected if you send a claim with a deprecated code.

#### **What will happen if I try to export a deprecated ICD-10 code to different areas of the visit note?**

You can export deprecated ICD-10 codes to the Assessment section of the visit note but you will not be able to export deprecated ICD-10 codes to the billing section of the visit note. Please [update the deprecated ICD-10 code](#updated_deprecated_ICD10) to an active, billable ICD-10 code before exporting ICD-10 codes to the billing section of the visit note.


#### **Can I add a deprecated ICD-10 code to the billing section of a visit note?**

No, deprecated ICD-10 codes cannot be added to the billing section of a visit note once they are deemed non-billable as they are no longer valid for use. The codes will be grayed-out with a yellow banner detailing that they are non-billable codes.

![]()




## **Related Articles**

- [Problem List Guide](managing-your-problem-list.md)
- [Billing Guide- Creating a Super Bill & coding for your visit](billing.md)
- [Billing Guide- Frequently Asked Questions](Billing-Guide-Frequently-Asked-Questions.md)