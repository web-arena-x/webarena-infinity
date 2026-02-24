# Problem List Guide

Source: https://help.elationhealth.com/s/article/managing-your-problem-list

---

# **Contents**

- [Overview](#overview)
 - [What is the Problem List?](#description)
 - [Why is the Problem List useful?](#value)
- [Workflow Instructions](#workflows)
 - [Adding a problem to the Problem List](#adding_problem)
 - [Searching for diagnoses and ICD-10 codes](#search_tips)
 - [Editing an existing problem](#editing_problems)
 - [Exporting a problem to a visit note](#export)
 - [Using the Problem List for billing](#billing)
 - [Using the Problem List for prescriptions, orders and referrals](#rx_orders_referrals)
 - [Using the Problem List for reporting](#reporting)
- [Frequently Asked Questions](#faqs)

# **Overview**

## **What is the Problem List?**

The Problem List is a repository for all of the medical issues or conditions that impacting a patient's health. This repository can include active, controlled or resolved issues or conditions. Each record in the Problem List can include an ICD-10 code, ICD-10 code description, a personalized title, the onset date of the issue/condition, the status of the issue/condition and additional notes.

## **Why is the Problem List useful?**

The Problem List allows you to see all of the patients medical issues or conditions at a glance. Associated ICD-10 codes can also be used for other clinical workflows such as:

- prescribing medications
- ordering tests (lab, imaging, etc)
- creating referrals
- billing for services rendered

If you are using Elation's Risk Assessment feature, the *Problem List* will also help you calculate the patient's Risk Score. Learn more about the Risk Assessment feature in the [Risk Assessment Introduction- Risk Assessment Factors (RAF) and Hierarchical Condition Categories (HCC)](what-is-risk-assessment.md) article.

# **Workflow Instructions**

## **Adding a problem to the Problem List**

| | |
| --- | --- |
| **1** | Open a patient's chat & go to the **Clinical Profile**. |
| **2** | Click **+ Add Problem** under theProblem List section. |
| **3** | Fill in the following fields:   - **Search for a diagnosis** - Search the diagnosis database for a diagnosis. You can search by ICD-9 Code, ICD-10 Code or description. - **Title** *-* Defaults to the description of the diagnosis you selected from the database but you can always adjust it to your preference. - **Dx Date** *-* Specify when the problem began. The date will default to 'today' if you do not change the date. - **Status** *-* Specify if the problem is **Active**, **Controlled** or **Resolved**. The default is **Active.**   - Setting the status as **Resolved** will append a resolved date of 'today' to the problem. - **Synopsis** *-* Add notes about the diagnosis. |
| **4** | Click **Save** or **Save & Add Another** to save the Problem. |

The most recently added item is by default added to the bottom of the Problem List. Use the 3 horizontal line button next to the problem to drag and reorder the Problem List as needed.

## **Searching for diagnoses and ICD-10 codes**

Our search tool includes common abbreviations and shorthands to allow you to find problem codes faster. For example, try:

- "fx" for fractures (no need to capitalize!)
- "hx" for history
- "hbp" for high blood pressure

For diagnoses with many specific sub-diagnoses, you can use simple abbreviations or the first few letters of a word to narrow your search:

- "w" - for well-controlled diagnoses
- "un" - for uncontrolled diagnoses
- "po" - for poorly-controlled diagnoses

Similarly, for diagnoses with both adult and pediatric codes, you can use:

- "a" for the adult diagnoses
- "p" for the pediatric diagnoses

**💡**  **USER TIP** The search results only show the single best diagnosis for each ICD-9+ICD-10 pair. If you want to see every possible diagnosis (including duplicates) prepend a "!" in front of your query (ex. "!bmi") and you will see all possible search results.

![]()

## **Editing an existing problem**

You can edit existing problems in the Problem List when changes need to be made, or an ICD-10 code for the problem has been deprecated and is no longer billable. For more information on how to manage deprecated, non-billable ICD-10 codes, please read [Billing Guide - Managing deprecated, non-billable ICD-10 codes](Managing-deprecated-ICD10-codes.md).


To edit an existing problem:

| | |
| --- | --- |
| **1** | Locate the problem on the patient's Problem List. |
| **2** | Click on the name of problem (or click **Actions** -> **Edit** next to the problem). |
| **3** | Make the changes you need & click **Save**. |

### **Changing the status of a Problem**

To quickly mark a problem as controlled or resolved:

| | |
| --- | --- |
| **1** | Locate the problem on the patient's Problem List. |
| **2** | Click **Actions** -> **Mark as Controlled** or **Mark as Resolved** next to the problem.   - Changing the status from **Active** or **Controlled** to **Resolved** will append a resolved date of 'today' to the problem. - Changing the status to **Active** to **Controlled** will turn the text to a gray color on the Problem List to allow you to visually distinguish controlled problems from active/resolved problems. - Changing the status from **Resolved** to **Active** or **Controlled** will remove the resolved date from the problem. |

## **Exporting a problem to a visit note**

Any record in the Problem List can be referenced into a note or visit note to facilitate documentation of a clinical encounter. You can click the **Actions** button next to the Problem List section header to export the entire Problem List to a note or visit note. You can also click **Actions** next to a specific problem to only export that problem to a note or visit note.

Learn more about [using Clinical Profile documentation to facilitate charting here](no-double-documentation-with-the-clinical-profile.md).

## **Using the Problem List for billing**

Recording ICD-10 codes in your problem list will simplify and facilitate your ability to code a visit for insurance billing. Coded problems will automatically appear first in the**Add Dxs** field, of the billing information section of your visit notes, so that you will not need to search for them again when coding for a visit.

You can also use the **Actions** -> **Export to Note (Billing)** option to export the ICD-10 code the the billing information section of your visit note directly.

The Problem List will also indicate if any ICD-10 codes for the problems detailed in this list have been deprecated and can no longer be used for billing. For more information on how to manage deprecated, non-billable ICD-10 codes, please read [Billing Guide - Managing deprecated, non-billable ICD-10 codes](Managing-deprecated-ICD10-codes.md).

## **Using the Problem List for prescriptions, orders & referrals**

Recording ICD-10 codes in your problem list will simplify and facilitate your ability to write prescriptions, create orders for testing and generate referrals. Coded problems will automatically appear first in the **Diagnosis (Dx)**fields of prescription forms, order forms and the referral form so that you will not need to search for them again when completing these forms.

## **Using the Problem List for reporting**

Elation's Patient List report allows you to search your patient panel and run reporting on specific characteristics. One of the available filters in the Patient List report is **Active Problems in Clinical Profile**. This filter will allow you to search for patients with specific issues or conditions in case you want to follow up with those patients for specific reasons such as medication or treatment follow-ups or changes.

Learn more about the Patient List report in the [Patient List Report Guide](find-patients-with-elations-patient-list.md).

# **Frequently Asked Questions (FAQ)**

#### **What does the “+” sign next to an ICD-10 code in the search results mean?**

A **+** sign next to an ICD-10 code in the search results means there is more than 1 corresponding ICD-9 or ICD-10 code for the diagnosis. When you choose a diagnosis with this scenario, you will see multiple ICD codes show up next to the diagnosis you just selected. For example, the diagnosis “bilateral knee pain” does not have a single corresponding ICD-10 code. Instead, selecting “bilateral knee pain” will automatically apply M25.561 “pain in right knee” and M25.562 “pain in left knee”.

#### **What does it mean to “Add Another Dx?” to a problem? Is it beneficial to do this?**

Elation allows flexibility when codifying/classifying a patient problem. If the problem you are treating is a combination of diagnoses, you can list all of the diagnoses and corresponding codes for that problem. Add additional diagnoses to a problem by clicking **+ Add Another Dx**. When exporting a problem to a Visit Note, all diagnoses and codes will be transferred to both the Visit Note and bill for that visit.

#### **Can the problem list be ordered by relevancy not chronologically?**

Yes, you can order your problems any way you like. The most recently added item is usually added to the bottom of the list. Use the 3 horizontal line button next to the problem to drag and reorder the list.

#### **What is a SNOMED code and why does it show up when I select a diagnosis code?**

The Systematized Nomenclature of Medicine (SNOMED) is a collection of medical terms which classifies diagnoses. Codifying your Problem List using SNOMED is a requirement for Medicare Meaningful Use Stage 2. Elation will add the corresponding SNOMED code every time you select a diagnosis from the ICD-10 database.

####

#### **What does it mean to "crosswalk" a problem? How do I do that in Elation?**

A crosswalk is also referred to as "General Equivalence Mapping (GEM)" and is a term that is used when codes from one system links to codes in another system.

If you use CCD or CCDA files to import problem data from other electronic health record systems into your Elation chart, sometimes those problems will not contain any ICD codes or they will only contain ICD-9 codes. You can easily add ICD-10 codes to these these problems by following the steps below:

1. Click on the problem in your *Problem List* (or click **Actions** -> **Edit** on the problem). At the top of the dialog, we will display the original description and code(s) from the problem. In the dropdown, a list of potential matches and their corresponding ICD-10 & ICD-9 codes will be automatically displayed for you to crosswalk.
2. Select the most appropriate diagnosis from the list of results that corresponds to the original problem. Elation will then automatically update the code on the problem list with the corresponding ICD-10, ICD-9, and SNOMED codes.
3. Click **Save** and then move on to the next problem that needs to be crosswalked.

**Next Step**

**Document ICD-10 codes with your patient problems to streamline your clinical workflows!**

# **Related Articles**

- [Clinical Profile Guide- A snapshot of the patient's health status](clinical-profile-record-patient-medical-history.md)
- [Visit Note Documentation Guide- Using Clinical Profile documentation to facilitate charting](no-double-documentation-with-the-clinical-profile.md)
- [Billing Guide - Managing deprecated, non-billable ICD-10 codes](Managing-deprecated-ICD10-codes.md)
- [Risk Assessment Introduction- Risk Assessment Factors (RAF) and Hierarchical Condition Categories (HCC)](what-is-risk-assessment.md)
- [Risk Assessment Guide- Managing your patient's risk score](how-to-use-elations-risk-assessment-feature.md)
- [Prescription Form Guide- ePrescribing & Ordering Medications](/s/article/eprescribing-and-ordering-medications-with-the-upgraded-rx-form)
- [Billing Guide- Creating a Super Bill and coding for your visit](billing.md)
- [Patient List Report Guide- Searching your patient panel](find-patients-with-elations-patient-list.md)