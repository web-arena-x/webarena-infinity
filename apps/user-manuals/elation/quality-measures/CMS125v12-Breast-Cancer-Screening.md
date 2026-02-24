# [CMS125v12] Breast Cancer Screening

Source: https://help.elationhealth.com/s/article/CMS125v12-Breast-Cancer-Screening

---

**Important Note**: This Help Center Article is no longer relevant for the current calendar year. This Help Center Article is retained in the event of an audit for fidelity of information to align with changes over time and so we keep this article hosted. If you are looking for current calendar year information please ensure the calendar year is included in the title of the Help Center Article.

## **Contents**

- [Measure Details](#details)
- [Measure Parameters](#parameters)
- [Elation Workflows](#workflows)
- [Measure Information](#info)
- [Attachments](#attachments)

**Important Note**: **This measure has been removed** as an eCQM for Traditional MIPS reporting. This measure is still an applicable eCQM in other programs and is still available in Elation. It will not be eligible to be counted towards Traditional MIPS submissions via QRDA in the 2024 MIPS Performance Year. There are additional ways to report MIPS, please see our [MIPS (2024) Overview](MIPS-2024-Overview.md) article to better understand 2024 MIPS measure options.

## **Measure Details**

Percentage of women 50-74 years of age who had a mammogram to screen for breast cancer in the 27 months prior to the end of the Measurement Period

## **Measure Parameters**

**Numerator:** Women with one or more mammograms any time on or between October 1st two years prior to the measurement period and end of the measurement period

**Denominator:** Women 52-74 years of age with a visit by the end of the measurement period.

**Exclusions/Exceptions:**

- Women who had a bilateral mastectomy or who have a history of a bilateral mastectomy or for whom there is evidence of a right and a left unilateral mastectomy on or before the end of the measurement period.
- Exclude patients whose hospice care overlaps the measurement period.
- Exclude patients receiving palliative care for any part of the measurement period.
- Exclude patients 66 and older by the end of the measurement period who are living long term in a nursing home any time on or before the end of the measurement period.
- Exclude patients 66 and older by the end of the measurement period with indication of frailty for any part of the measurement period who also meet any of the following advanced illness criteria:
 - Advanced illness with two outpatient encounters during the measurement period or the year prior
 - OR advanced illness with one inpatient encounter during the measurement period or the year prior
 - OR taking dementia medications during the measurement period or the year prior

These are the exclusion document tags for this measure: (**Reference**: [Tag Reports and Notes with Document Tags](https://help.elationemr.com/s/article/tag-reports-and-notes-with-document-tags))

- EXCLUSION: NO BSC SCRN Absence of Left Breast
- EXCLUSION: NO BSC SCRN Absence of Right Breast
- EXCLUSION: NO BSC SCRN BIL MAST
- EXCLUSION: NO BSC SCRN UNI MAST
- EXCLUSION: HOSPICE CARE
- EXCLUSION: IP DISCHARGE STATUS TO HEALTH CARE FACILITY FOR HOSPICE CARE
- EXCLUSION: IP DISCHARGE STATUS TO HOME FOR HOSPICE CARE

**How to document frailty:**

To document frailty in Elation, both conditions below have to be met:

1. add a frailty diagnosis to the patient's Problem List
2. meet one of the following criteria:
   1. record an advanced illness diagnosis in 2 outpatient encounters
   2. record an advanced illness in 1 inpatient counter
   3. record a dementia medication in the patient's chart

**User Tip**:Reports with the various frailty codes and advanced illness codes can be found in the [Attachments](#attachments) section of this article.

You can also document the use of a frailty device to claim the frailty diagnosis part of the exclusion. To do so, please add a document tag that represents the frailty device to a visit note for the reporting year. The document tag should have the device's HCPCS code and description and can be created directly in the visit note or within your [Document Tags](https://app.elationemr.com/settings/doc-tags/) settings page in Elation. A report with the various frailty devices and their corresponding HCPCS codes are also in the [Attachments](#attachments) section of this article.

![]()

## **Elation Workflows**

1. Recording from a visit note:
   1. While documenting a visit note, if the patient requires a breast cancer screening, a Clinical Reminders alert will appear at the top of the visit note.
   2. On the right hand side of this alert, you'll be given an option to address or dismiss the alert. Clicking Address will bring up options to address the measure.
   3. When addressing the alert, the only option that will include the patient in the numerator is the "Document existing Mammogram details" option, which will give you a prompt to record the details of a previous mammogram. Use the "MAMMOGRAM (2022 AND LATER)" document tag to record a mammogram for the 2024 MIPS. If they haven't had a mammogram in the measurement, the prompt also gives the options to order a mammogram, or to direct the clinic staff to order one.
2. Recording from a patient chart:
   1. At the bottom of the clinical profile, in the lower left corner of the patient's chart, you'll see the patient's active Health Maintenance items.
   2. If the patient is eligible for the breast cancer screening measure, an alert will appear in the Health Maintenance section. If it's due within the calendar year, a due date will appear in orange to the right of the measure.
      - **Reference**: [Health Maintenance Documentation and Reminders](https://help.elationemr.com/s/article/health-maintenance)
   3. To document and address the measure, click on Breast Cancer Screening, and indicate the date of the patient’s most recent Mammogram, the actual result, and click Save New. Use the "MAMMOGRAM ( 2022 AND LATER)" document tag to record a mammogram for the 2024 MIPS if needed.

![]()

1. Tag any document in the patient’s record with a result-defined “MAMMOGRAM (2022 AND LATER)” document tag. This alone will meet the health maintenance requirement.

![]()

## **Measure Information**

Breast cancer is one of the most common types of cancers, accounting for 15 percent of all new cancer diagnoses in the U.S. (Noone et al, 2018). In 2015, over 3 million women were estimated to be living with breast cancer in the U.S. and it is estimated that 12 percent of women will be diagnosed with breast cancer at some point during their lifetime (Noone et al, 2018).

While there are other factors that affect a woman's risk of developing breast cancer, advancing age is a primary risk factor. Breast cancer is most frequently diagnosed among women ages 55-64; the median age at diagnosis is 62 years (Noone et al, 2018).

The chance of a woman being diagnosed with breast cancer in a given year increases with age. By age 40, the chances are 1 in 68; by age 50 it becomes 1 in 43; by age 60, it is 1 in 29 (American Cancer Society, 2017).

[Reference: Measure information from CMS](https://ecqi.healthit.gov/ecqm/ec/2024/cms0125v12)

## **Attachments**

- [Advanced Illness Codes](https://elation.my.salesforce.com/sfc/p/37000000L9cg/a/Ui000000hjMr/9r1WZ2S9LnMUDEmqex4zyH0qO9MptezpfnKwWk7OjQ4)
- [Frailty Codes](https://elation.my.salesforce.com/sfc/p/37000000L9cg/a/Ui000000hQYl/QCAVO5sW1Iszc0zBpsBAqQx4BWJgfaH4G5CreFh68JE)
- [Frailty Descriptions](https://elation.my.salesforce.com/sfc/p/37000000L9cg/a/Ui000000hjLF/E7nc2CghoKf73XtAR8uVCgLmLy44EaK5SeQXQPune7s)

## **Related Articles**

- [MIPS (2024)- Quality Category](Quality-Category-MIPS-2024.md)
- [Clinical Quality Measures Reports Guide](elations-cqm-dashboards.md)
- [Clinical Reminders for Clinical Quality Measures](clinical-reminders-for-clinical-quality-measures.md)
- [Tag Reports and Notes with Document Tags](tag-reports-and-notes-with-document-tags.md)
- [Health Maintenance Documentation and Reminders](health-maintenance.md)
- [MIPS (2024) Overview](MIPS-2024-Overview.md)
- [MIPS (2024)- Quick Start Guide](MIPS-2024-Quick-Start-Guide.md)