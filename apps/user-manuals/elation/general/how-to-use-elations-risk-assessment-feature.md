# Risk Assessment Guide- Managing your patient's risk score

Source: https://help.elationhealth.com/s/article/how-to-use-elations-risk-assessment-feature

---

## **Recommended Reading**

Read the [Risk Assessment Introduction](what-is-risk-assessment.md) article to learn more about the importance of evaluating health risks for your patients.

## **Contents**

- [Turning on the Risk Assessment feature](#turn_on_feature)
- [Viewing the Risk Score in the patient's Clinical Profile](#risk_score_clinical_profile)
- [Reviewing risk-adjusted conditions in the Problem List](#risk_conditions)
- [Addressing risk-adjusted conditions during a patient encounter](#patient_encounter)
- [Viewing the Risk Score in the billing details](#risk_score_billing_details)
- [Reporting & filtering by risk score](#Reporting)

## **Turning on the Risk Assessment feature**

1. Go to "Settings" >> "Clinical Care Measures Settings"
2. At the bottom of the page set the “Risk Assessment” toggle to "Yes" to turn on the Risk Assessment feature.

![]()

## **Viewing the Risk Score in the patient's Clinical Profile**

The aggregated Risk Score is at the top left corner of the patient’s chart under the patient’s Date of Birth. The average Medicare patient has a score of 1.0, so this estimated score in Elation will give you insight into how sick your patient is. The lowest possible risk score is 0 (lowest risk).

**Important Note**: The Risk Score you see at the top of the patient’s chart is the 2025 CMS HCC Risk Model calculation which is a blend of version 24 (33%) and version 28 (67%). To see a detailed breakdown of the Risk Score, click on the Risk Score.

Clicking on the Risk Score will open a box with a detailed breakdown of how the score is calculated. The score is a reflection of the patient’s demographics, and all risk-adjusted chronic conditions that are added to the patient’s Problem List in the chart. For 2025, CMS is using a blended score of HCC Risk Model version 24 (at 33%) and HCC Risk Model version 28 (at 67%). You will see the Risk Model v24 score, Risk Model v28 score and the blended score in its own columns.

## **Reviewing risk-adjusted conditions in the Problem List**

In the problem list, any problems associated with a chronic condition will show the relative weight (risk factor) of the condition and how it contributes to the overall risk score (in orange).

**Important Note**: The risk factor you see next to each diagnosis code in the Problem List is based on CMS Risk Model version 28.

![]()


CMS requires that each risk-adjusted condition be addressed at least once per calendar year in order to be eligible for reimbursement. If the problem has not been addressed in the current calendar year, the last addressed date (displayed underneath each condition) will be available so that you can quickly see which problems need attention. You can also see the last addressed date of a condition by clicking on the problem name.

When searching for a new problem, the risk factor related to specific ICD-10 code(s) will appear in the last column of the diagnosis search results. You can use this to help choose the correct code to adequately represent the complexity and severity of the problem.
![]()

## **Addressing risk-adjusted conditions during a patient encounter**

To address a risk-adjusted condition, you must reference the ICD-10 code of the condition into the assessment and billing information sections of visit note and sign the visit note. This will update the *Last Addressed....* date for the condition and help you track the progress of your patient's risk conditions. To complete this workflow

1. Go to condition you are addressing in the Problem List
2. Click "Actions" >> "Export to Note (A, Billing)"
3. Complete your visit note documentation and coding and then click "Sign Visit Note".

## **Viewing the Risk Score in the billing details**

For extra visibility into risk-adjusted conditions, the risk score for risk-adjusted conditions will be visible in the [billing information](billing.md) section of the visit note as well as in the **Codes** column of [Billing Home](Billing-Home.md).

## **Reporting and filtering by Risk Score**

Risk Scores can be used at the practice-wide level to help provide an overview of patient scores and identify patients over a range of risk scores. This can aid with identifying the highest risk patients at the practice, or be used to stratify patients into broad risk categories. To report on patients by Risk Score:

1. Select "Reports" >> "Patient List Report" in the blue navigation bar at the top of your Elation account
2. Check off the *HCC Risk Score* filter and choose whether you want to look for scores above, below or between certain numbers
   - Important Note:  The Risk Score you will search for is the blended score of the 2025 CMS Risk Model version 24 (33%) and Risk Model version 28 (67%).
3. Click "Generate List" once you are ready to see a list of applicable patients
4. The resulting report will include all relevant patients, and will have a column that displays their risk score. Any of the columns, including risk score, can be sorted by ascending or descending by clicking on the name of the column at the top of the list.

- **User Tip**: Click "Download" >> "Download CSV" to download the report to apply additional filtering if needed.
- **Important Note**:  The Risk Score you will search for is the blended score of the 2025 CMS Risk Model version 24 (33%) and Risk Model version 28 (67%). To see the Risk Score details, open the patient’s chart and click on the Risk Score.

## **Related Articles**

- [Risk Assessment Introduction- Risk Assessment Factors (RAF) and Hierarchical Condition Categories (HCC)](what-is-risk-assessment.md)
- [Problem List Guide](managing-your-problem-list.md)
- [Visit Note Documentation Guide- Using Clinical Profile documentation to facilitate charting](no-double-documentation-with-the-clinical-profile.md)
- [Patient Demographics Guide](Patient-Demographics-Guide.md)
- [Billing Guide- Creating a Super Bill and coding for your visit](billing.md)