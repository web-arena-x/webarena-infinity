# [CMS165v12] Controlling High Blood Pressure (MIPS 2024)

Source: https://help.elationhealth.com/s/article/CMS165v12-Controlling-High-Blood-Pressure-MIPS-2024

---

**Important Note**: This Help Center Article is no longer relevant for the current calendar year. This Help Center Article is retained in the event of an audit for fidelity of information to align with changes over time and so we keep this article hosted. If you are looking for current calendar year information please ensure the calendar year is included in the title of the Help Center Article.

## **Contents**

- [Measure Details](#measuredetails)
- [Measure Parameters](#measureparameters)
- [Elation Workflows](#elationworkflows)
- [Measure Information](#measureinformation)
- [Attachments](#attachments)

## **Measure Details**

Percentage of patients 18-85 years of age who had a diagnosis of essential hypertension starting before and continuing into, or starting during the first six months of the measurement period, and whose most recent blood pressure was adequately controlled (<140/90mmHg) during the measurement period

## **Measure Parameters**

**Numerator**: Patients whose blood pressure at the most recent visit is adequately controlled (systolic blood pressure < 140 mmHg and diastolic blood pressure < 90 mmHg) during the measurement period.

**Denominator**: Patients 18-85 years of age who had a visit and diagnosis of essential hypertension starting before and continuing into, or starting during the first six months of the measurement period.

**Exclusions/Exceptions:**

- Patients with evidence of end stage renal disease (ESRD), dialysis or renal transplant before or during the measurement period.
- Patients with a diagnosis of pregnancy during the measurement period.
- Patients who are in hospice care for any part of the measurement period.
- Exclude patients receiving palliative care during the measurement period.
- Patients 66 and older by the end of the measurement period who are living long term a nursing home any time on or before the end of the measurement period.
- Exclude patients 81 and older with an indication of frailty for any part of the measurement period.
- Exclude patients 66 and older with an indication of frailty for any part of the measurement period who meet any of the following criteria:
 - Advanced illness with two outpatient encounters during the measurement period or the year prior
 - OR advanced illness with one inpatient encounter during the measurement period or the year prior
 - OR taking dementia medications during the measurement period or the year prior

These are the exclusion document tags for this measure (**Reference**: [Tag Reports and Notes with Document Tags](tag-reports-and-notes-with-document-tags.md)):

- EXCLUSION: HOSPICE CARE
- EXCLUSION: IP DISCHARGE STATUS TO HEALTH CARE FACILITY FOR HOSPICE CARE
- EXCLUSION: IP DISCHARGE STATUS TO HOME FOR HOSPICE CARE

**How to document frailty**

To document frailty in Elation, both conditions below have to be met:

1. add a frailty diagnosis to the patient's Problem List
2. meet one of the following criteria:
   1. record an advanced illness diagnosis in 2 outpatient encounters
   2. record an advanced illness in 1 inpatient counter
   3. record a dementia medication in the patient's chart

**User Tip:**Attachments with frailty codes and advanced illness codes can be found in the [Attachments](#attachments) section of this article.

You can also document the use of a frailty device to claim the first part of the exclusion. To do so, please add a document tag that represents the frailty device to a visit note from the reporting year. The document tag should have the device code and description and can be created directly in the visit note or within your Document Tags Settings page in Elation. Attachments with device codes are also in the [Attachments](#attachments) section of this article.

## **Elation Workflows**

1. Ensure the patient has a diagnosis of Hypertension in their problem list (I10) whose diagnosis date is in the measurement year or earlier:

![]()

1. Record Blood Pressure for the Patient in a Visit Note, readings below 140/90 will count for the numerator of this measure. If you record multiple blood pressure readings, the lowest systolic and lowest diastolic result across all BPs will be used in this measure’s calculation

![]()

## **Measure Information**

High blood pressure (HBP) or hypertension, known as the “silent killer,” increases risks of heart disease and stroke which are two of the leading causes of death in the U.S. (Yoon, Fryar, & Carroll, 2015). A person who has HBP is four times more likely to die from a stroke and three times more likely to die from heart disease (CDC, 2012). The National Vital Statistics Systems reported that in 2014 there were approximately 73,300 deaths directly due to HBP and 410,624 deaths with any mention of HBP (CDC, 2014). Between 2006 and 2016 the number of deaths due to HBP rose by 46.3 percent (Benjamin et al, 2019). Managing and treating HBP would reduce cardiovascular disease mortality for males and females by 30.4 percent and 38.0 percent, respectively (Patel et al., 2015).

The estimated annual average direct and indirect cost of HBP from 2014 to 2015 was $55.9 billion (Benjamin et al, 2019). Total direct costs of HBP is projected to increase to $220.9 billion by 2035 (Benjamin et al, 2019). A study on cost-effectiveness on treating hypertension found that controlling HBP in patients with cardiovascular disease and systolic blood pressures of >= 160 mm Hg could be effective and cost-saving (Moran, 2015).

Many studies have shown that controlling high blood pressure reduces cardiovascular events and mortality. The Systolic Blood Pressure Intervention Trial (SPRINT) investigated the impact of obtaining a SBP goal of <120 mm Hg compared to a SBP goal of <140 mm Hg among patients 50 and older with established cardiovascular disease and found that the patients with the former goal had reduced cardiovascular events and mortality (SPRINT Research Group et al., 2015).

Controlling HBP will significantly reduce the risks of cardiovascular disease mortality and lead to better health outcomes like reduction of heart attacks, stroke, and kidney disease (James et al., 2014). Thus, the relationship between the measure (control of hypertension) and the long-term clinical outcomes listed is well established.

[Reference: Measure Information from CMS](https://ecqi.healthit.gov/ecqm/ec/2024/cms0165v12)

## **Attachments**

- [Advanced Illness Codes](https://elation.my.salesforce.com/sfc/p/37000000L9cg/a/Ui000000iUs1/J4tbcoX3jNHpweMThhzg3a.G12VMTmlfqytVdZKAg4U)
- [Frailty Codes](https://elation.my.salesforce.com/sfc/p/37000000L9cg/a/Ui000000iUqP/BMIpeifo2JM7d6l5rmrVDktggJs4MmpaMCwp.nQtYQo)
- [Frailty Descriptions](https://elation.my.salesforce.com/sfc/p/37000000L9cg/a/Ui000000iUon/sJjyTsgIFcKuDfpvy36I0iobhe_TTvSUnn6QgVgs38Y)

## **Related Articles**

- [MIPS (2024)- Quality Category](Quality-Category-MIPS-2024.md)
- [Clinical Quality Measures Reports Guide](elations-cqm-dashboards.md)
- [Clinical Reminders for Clinical Quality Measures](clinical-reminders-for-clinical-quality-measures.md)
- [Tag Reports and Notes with Document Tags](tag-reports-and-notes-with-document-tags.md)
- [MIPS (2024) Overview](MIPS-2024-Overview.md)
- [MIPS (2024)- Quick Start Guide](MIPS-2024-Quick-Start-Guide.md)

###