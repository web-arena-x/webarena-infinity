# [CMS124v13] Cervical Cancer Screening (MIPS 2025)

Source: https://help.elationhealth.com/s/article/CMS124v13-Cervical-Cancer-Screening-MIPS-2025

---

## **Contents**

- [Measure Details](#details)
- [Measure Parameters](#parameters)
- [Elation Workflows](#workflows)
- [Measure Information](#info)

## **Measure Details**

Percentage of women 21-64 years of age who were screened for cervical cancer using either of the following criteria:

- Women age 21-64 who had cervical cytology (Pap Test) performed within the last 3 years
- Women age 30-64 who had cervical human papillomavirus (HPV) testing performed within the last 5 years

##

### **Measure Parameters**

**Numerator:**Women with one or more screenings for cervical cancer. Appropriate screenings are defined by any one of the following criteria:

- Cervical cytology (Pap Test) performed during the measurement period or the two years prior to the measurement period for women who are at least 24-64 years of age by the end of the measurement period.
- Cervical human papillomavirus (HPV) testing performed during the measurement period or the four years prior to the measurement period for women who are 30 years or older at the time of the test.

**Denominator:** Women 24-64 years of age with a visit during the measurement period

**Exclusions/Exceptions:**

- Women who had a hysterectomy with no residual cervix or a congenital absence of cervix.
- Exclude patients who are in hospice care for any part of the measurement period.
- Exclude patients receiving palliative care for any part of the measurement period.

**Additional CMS Guidance:** To ensure the measure is only looking for a cervical cytology test only after a woman turns 21 years of age, the youngest age in the initial population is 23.

- **Please Note:**
 - The measure may include screenings performed outside the age range of patients referenced in the initial population. Screenings that occur prior to the measurement period are valid to meet measure criteria.
 - Evidence of hrHPV testing within the last 5 years also captures patients who had co-testing; therefore additional methods to identify co-testing are not necessary.

These are the qualifying exclusion document tags for this measure (**Reference**: [Tag Reports and Notes with Document Tags](tag-reports-and-notes-with-document-tags.md)):

- EXCLUSION: HOSPICE CARE
- EXCLUSION: IP DISCHARGE STATUS TO HEALTH CARE FACILITY FOR HOSPICE CARE
- EXCLUSION: IP DISCHARGE STATUS TO HOME FOR HOSPICE CARE
- EXCLUSION: HYSTERECTOMY
- CQM EXCL: CONGENITAL ABS OF CERVIX

## **Elation Workflows**

**Important Note**: Elation has implemented dedicated workflows that reflect standardized requirements we do not control for certification to ensure structured and reportable tracking of measure specifications for supported electronic Clinical Quality Measures. To optimize performance per the specifications, please adhere precisely to the workflows outlined in the referenced Help Center article.

1. Recording from a visit note:
   - Elation's Clinical Reminders Feature allows you to easily document screenings. When a patient is due for a Cervical Cancer Screen, an alert will report at the top of the patient's visit note. Selecting Address on any of these will give a set of options to address that Quality Measure:

![]()

1. Click on Cervical Cancer Screening, and indicate the date of the patient’s most recent Pap Smear and/or HPV test, enter result of test, and click *Save New*.

![]()

1. ​​​Tag a report in the patient’s record with the approved document tag(s). This alone will meet the health maintenance requirement.

![]()

- 4 Document Tags that will satisfy this measure (**Reference**: [Tag Reports and Notes with Document Tags](tag-reports-and-notes-with-document-tags.md)):
 - HPV test (result: negative)
 - HPV test (result: positive)
 - Pap Smear (result: negative)
 - Pap Smear (result: positive)
- The following test LOINC codes qualify for these screenings
 - HPV Test
    - 21440-3, 30167-1, 38372-9, 59263-4, 59264-2, 59420-0, 69002-4, 71431-1, 75694-0, 77379-6, 77399-4, 77400-0, 82354-2, 82456-5, 82675-0, 95539-3
 - Pap Test
    - 10524-7, 18500-9, 19762-4, 19764-0, 19765-7, 19766-5, 19774-9, 33717-0, 47527-7, 47528-5

##

## **Measure Information**

All women are at risk for cervical cancer. In 2020, an estimated 13,800 women were diagnosed with cervical cancer in the U.S., resulting in an estimated 4,290 deaths (National Cancer Institute, 2020). Screening can identify precancerous lesions and can detect invasive cancer early, when treatment is more likely to be successful (American Cancer Society, 2020).

[Reference: Measure Information from CMS](https://ecqi.healthit.gov/ecqm/ec/2025/cms0124v13)

## **Related Articles**

- MIPS (2025) - Quality Category
- [Clinical Quality Measures Reports Guide](elations-cqm-dashboards.md)
- [Clinical Reminders for Clinical Quality Measures](clinical-reminders-for-clinical-quality-measures.md)
- [Tag Reports and Notes with Document Tags](tag-reports-and-notes-with-document-tags.md)
- [Health Maintenance Documentation and Reminders](health-maintenance.md)
- [MIPS (2025) Overview](https://help.elationemr.com/s/article/MIPS-2025-Overview)