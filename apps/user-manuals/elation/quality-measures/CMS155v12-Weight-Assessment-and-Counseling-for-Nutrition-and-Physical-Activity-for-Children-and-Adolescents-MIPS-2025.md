# [CMS155v13] Weight Assessment and Counseling for Nutrition and Physical Activity for Children and Adolescents (MIPS 2025)

Source: https://help.elationhealth.com/s/article/CMS155v12-Weight-Assessment-and-Counseling-for-Nutrition-and-Physical-Activity-for-Children-and-Adolescents-MIPS-2025

---

## **Contents**

- [Measure Details](#details)
- [Measure Parameters](#parameters)
- [Elation Workflows](#workflows)
- [Measure Information](#info)

## **Measure Details**

Percentage of patients 3-17 years of age who had an outpatient visit with a Primary Care Physician (PCP) or Obstetrician/Gynecologist (OB/GYN) and who had evidence of the following during the measurement period. Three rates are reported.

- Percentage of patients with height, weight, and body mass index (BMI) percentile documentation
- Percentage of patients with counseling for nutrition
- Percentage of patients with counseling for physical activity

## **Measure Parameters**

**Numerator 1**: Patients in the denominator have their height, weight, and BMI recorded in EHR.

**Numerator 2**: Patients in the denominator that have had counseling for nutrition.

**Numerator 3**: Patients in the denominator that have had counseling for physical activity.

**Denominator**: Patients 3-17 years of age by the end of the measurement period with at least one outpatient visit with a primary care physician (PCP) or an obstetrician/gynecologist (OB/GYN) during the measurement period.


**Exclusions/Exceptions:**

- Patients who have a diagnosis of pregnancy during the measurement period.
- Exclude patients who are in hospice care for any part of the measurement period.

These are the exclusion document tags for this measure (**Reference**: [Tag Reports and Notes with Document Tags](tag-reports-and-notes-with-document-tags.md)):

- EXCLUSION: HOSPICE CARE
- EXCLUSION: IP DISCHARGE STATUS TO HEALTH CARE FACILITY FOR HOSPICE CARE
- EXCLUSION: IP DISCHARGE STATUS TO HOME FOR HOSPICE CARE

## **Elation Workflows**

**Important Note**: Elation has implemented dedicated workflows that reflect standardized requirements we do not control for certification to ensure structured and reportable tracking of measure specifications for supported electronic Clinical Quality Measures. To optimize performance per the specifications, please adhere precisely to the workflows outlined in the referenced Help Center article.

All 3 numerators need to be met in order to close this measure for the patient.

1. To meet Numerator 1, ensure that the patient has had their height and weight recorded in a visit note during the measurement period. Once these are recorded, the BMI will be automatically calculated.

![]()

1. To meet Numerator 2 and Numerator 3, use the Clinical Reminders rules that apply to this measure, one to meet the requirement for Exercise Counseling, and the other to meet the requirement for Nutrition Counseling. You can also add one of these document tags in a visit note or report (**Reference**: [Tag Reports and Notes with Document Tags](tag-reports-and-notes-with-document-tags.md)):
   - Nutrition Cnsl
   - Diet Cnsl
   - Ref to Diet Svc
   - Ref to Wt Mgt Program
   - Exc Cnsl

![]()

## **Measure Information**

Over the last four decades, childhood obesity has more than tripled in children and adolescents 2 to 19 years of age (from a rate of approximately 5 percent to 18.5 percent) (Fryar, Carroll, & Ogden, 2014; Hales et al., 2017). Non-Hispanic black and Hispanic youth are more likely to be obese than their non-Hispanic white and non-Hispanic Asian counterparts. In 2015-2016, approximately 22 percent of non-Hispanic black and 26 percent of Hispanic youth were obese compared to approximately 14 percent of non-Hispanic white and 11 percent of non-Hispanic Asian youth (Hales et al., 2017).

Childhood obesity has both immediate and long-term effects on health and well-being. Children who are obese have higher rates of physical health conditions, such as risk factors for cardiovascular disease (like high blood pressure and high cholesterol), type 2 diabetes, asthma, sleep apnea, and joint problems. There is also a correlation between childhood obesity and mental health conditions, such as anxiety and depression (Centers for Disease Control and Prevention, 2016). In addition, children who are obese are more likely to be obese as adults and are therefore at risk for adult health problems, such as heart disease, type 2 diabetes, and several types of cancer (Centers for Disease Control and Prevention, 2016).

The direct medical costs associated with childhood obesity total about $19,000 per child, contributing to the $14 billion spent on care related to childhood obesity in the United States (Finkelstein, Graham, & Malhotra, 2014).

Because obesity can become a lifelong health issue, it is important to screen for obesity in children and adolescents, and to provide interventions that promote weight loss (U.S. Preventive Services Task Force, 2017).

[Reference: Measure Information from CMS](https://ecqi.healthit.gov/ecqm/ec/2025/cms0155v13)

## **Related Articles**

- MIPS (2025) - Quality Category
- [Clinical Quality Measures Reports Guide](elations-cqm-dashboards.md)
- [Clinical Reminders for Clinical Quality Measures](clinical-reminders-for-clinical-quality-measures.md)
- [Tag Reports and Notes with Document Tags](tag-reports-and-notes-with-document-tags.md)
- [MIPS (2025) Overview](https://help.elationemr.com/s/article/MIPS-2025-Overview)