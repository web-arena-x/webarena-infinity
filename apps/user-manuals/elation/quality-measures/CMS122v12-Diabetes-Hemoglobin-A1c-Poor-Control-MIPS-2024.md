# [CMS122v12] Diabetes: Hemoglobin A1c (HbA1c) Poor Control (> 9%) (MIPS 2024)

Source: https://help.elationhealth.com/s/article/CMS122v12-Diabetes-Hemoglobin-A1c-Poor-Control-MIPS-2024

---

**Important Note**: This Help Center Article is no longer relevant for the current calendar year. This Help Center Article is retained in the event of an audit for fidelity of information to align with changes over time and so we keep this article hosted. If you are looking for current calendar year information please ensure the calendar year is included in the title of the Help Center Article.

## **Contents**

- [Measure Details](#MeasureDetails)
- [Measure Parameters](#MeasureParameters)
- [Elation Workflows](#ElationFlows)
- [Measure Information](#MeasureInformation)
- [Additional Information/FAQ](#AdditionalInfo)
- [Attachments](#attachments)

### **Measure Details**

Report on the percentage of patients 18-75 years of age with diabetes who had hemoglobin A1c > 9.0% during the measurement period. ***This is a reverse measure; the goal is to ensure patients keep their A1c < 9%.  Practices should try to lower their percentage for this reverse measure.***

### **Measure Parameters**

**Numerator**: Patients whose most recent HbA1c level (performed during the measurement period) is >9.0% or is missing, or was not performed during the measurement period.

**Denominator**: Patients 18-75 years of age with diabetes with a visit during the measurement period.

Exclusions/Exceptions:

- Exclude patients who are in hospice care for any part of the measurement period.
- Exclude patients 66 and older by the end of the measurement period who are living long term in a nursing home any time during the measurement period.
- Exclude patients 66 and older by the end of the measurement period with an indication of frailty for any part of the measurement period who meet any of the following criteria:
 - Advanced illness with two outpatient encounters during the measurement period or the year prior
 - OR advanced illness with one inpatient encounter during the measurement period or the year prior
 - OR taking dementia medications during the measurement period or the year prior
- Exclude patients receiving palliative care for any part of the measurement period.

The qualifying exclusion tags for this measure are called (**Reference**: [Tag Reports and Notes with Document Tags](tag-reports-and-notes-with-document-tags.md)):

- EXCLUSION: HOSPICE CARE
- EXCLUSION: IP DISCHARGE STATUS TO HEALTH CARE FACILITY FOR HOSPICE CARE
- EXCLUSION: IP DISCHARGE STATUS TO HOME FOR HOSPICE CARE

### **How to document frailty in Elation**

To document frailty in Elation, both conditions below have to be met:

1. add a frailty diagnosis to the patient's Problem List
2. meet one of the following criteria:
   1. record an advanced illness diagnosis in 2 outpatient encounters
   2. record an advanced illness in 1 inpatient counter
   3. record a dementia medication in the patient's chart

**User Tip:** Attachments with frailty codes and advanced illness codes can be found in the [Attachments](#attachments) section of this article.

You can also document the use of a frailty device to claim the first part of the exclusion. To do so, please add a document tag that represents the frailty device to a visit note from the reporting year. The document tag should have the device code and description and can be created directly in the visit note or within your Document Tags Settings page in Elation. Attachments with device codes are also in the [Attachments](#attachments) section of this article.

![]()

**Elation Workflows**

1. Ensure the patient has a diagnosis of Diabetes (E11.9, etc):

1. Receive HbA1c Labs from a Lab Vendor electronically through Elation
2. Manually document a patient’s HbA1c Results.

   1. The HbA1c can be recorded in a structured format by clicking "Actions" next to an uploaded report and then selecting "Add Lab Values for Trending."

      - **Reference**: [How to record structured lab results from in-house or faxed lab report](https://help.elationemr.com/s/article/record-structured-data-from-in-house-or-faxed-lab-reports)

1. Clicking "Notes" -> "Point-of-Care Labs"

   - **Reference**: [How to use the Point-of-Care Labs feature](https://help.elationemr.com/s/article/record-structured-data-from-in-house-or-faxed-lab-reports)

**Measure Information**

Diabetes is the seventh leading cause of death in the United States. In 2017, diabetes affected approximately 34 million Americans (10.5% of the U.S. population) and killed approximately 84,000 people (Centers for Disease Control and Prevention [CDC], 2020a). Diabetes is a long-lasting disease marked by high blood glucose levels, resulting from the body's inability to produce or use insulin properly (CDC, 2020a). People with diabetes are at increased risk of serious health complications including vision loss, heart disease, stroke, kidney damage, and amputation of feet or legs (CDC, 2018).

In 2017, diabetes cost the U.S. an estimated $327 billion: $237 billion in direct medical costs and $90 billion in reduced productivity. This is a 34% increase from the estimated $245 billion spent on diabetes in 2012 (American Diabetes Association [ADA], 2018).

Controlling A1c blood levels helps reduce the risk of microvascular complications (eye, kidney and nerve diseases) (ADA, 2020).

[Reference: Measure Information from CMS](https://ecqi.healthit.gov/ecqm/ec/2024/cms0122v12)

## **Additional Information/FAQ**

Although this measure can be satisfied by manually entering lab results, we recommend getting interfaced lab results, if possible. Electronic lab results directly from the lab will also count towards this measure, limiting the need for additional documentation.

## **Attachments**

- [Advanced Illness Codes](https://elation.my.salesforce.com/sfc/p/37000000L9cg/a/Ui000000fkZx/AL.Juz7l4u5QaNM4QDBRhf8Pvfo.y5AgwbMitkfUM3o)
- [Frailty Codes](https://elation.my.salesforce.com/sfc/p/37000000L9cg/a/Ui000000fkrh/3B3NkCdGxD2Lh1Sr7UdlnzJzA7QRPQ6pvrX.URDXV7I)
- [Frailty Descriptions](https://elation.my.salesforce.com/sfc/p/37000000L9cg/a/Ui000000fken/aQdggwWTC4kzHcitS7igp9y_moN6nfDheEnFD8qYBPA)

## **Related Articles**

- [MIPS (2024)- Quality Category](Quality-Category-MIPS-2024.md)
- [Clinical Quality Measures Reports Guide](elations-cqm-dashboards.md)
- [Clinical Reminders for Clinical Quality Measures](clinical-reminders-for-clinical-quality-measures.md)
- [Tag Reports and Notes with Document Tags](tag-reports-and-notes-with-document-tags.md)
- [How to record structured lab results from in-house or faxed lab reports](record-structured-data-from-in-house-or-faxed-lab-reports.md)
- [How to use the Point-of-Care Labs feature](point-of-care-labs.md)
- [MIPS (2024) Overview](MIPS-2024-Overview.md)
- [MIPS (2024)- Quick Start Guide](MIPS-2024-Quick-Start-Guide.md)