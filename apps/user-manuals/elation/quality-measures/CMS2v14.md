# [CMS2v14] Preventive Care and Screening: Screening for Depression and Follow-Up Plan (MIPS 2025)

Source: https://help.elationhealth.com/s/article/CMS2v14

---

# **Contents**

- [Measure Details](#measure_details)
- [Measure Parameters](#measure_parameters)
- [Elation Workflows](#workflows)
 - [Meeting requirements](#workflow_meeting_requirements)
 - [Documenting exclusions](#documenting_exclusions)
 - [Documenting exceptions](#documenting_exceptions)
- [Measure Information](#measure_information)
- [Frequently Asked Questions](#FAQ)

# **Measure Details**

Percentage of patients aged 12 years and older screened for depression on the date of the encounter or up to 14 days prior to the date of the encounter using an age-appropriate standardized depression screening tool AND if positive a follow-up plan is documented on the date of or up to two days after the date of the qualifying encounter.

# **Measure Parameters**

**Numerator**: Patients screened for depression on the date of the encounter or up to 14 days prior to the date of the encounter using an age-appropriate standardized tool AND if positive, a follow-up plan is documented on the date of or up to two days after the date of the visit.

**Denominator**: All patients aged 12 years and older at the beginning of the measurement period with at least one visit note during the measurement period.

**Exclusions:**

Patients who have ever been diagnosed with bipolar disorder at any time prior to the qualifying encounter.

**Exceptions**:

- Exclude patients who refuse to participate in or complete the depression screening.
- Exclude patients with documentation of medical reason for not screening patient for depression (e.g., cognitive, functional, or motivational limitations that may impact accuracy of results; patient is in an urgent or emergent situation where time is of the essence and to delay treatment would jeopardize the patient's health status).

# **Elation Workflows**

**Important Notes**:

1. The automated clinical reminders for this measure are currently unavailable - which means you won't receive an alert in the patient's visit note when a depression screening needs to be performed. Review the denominator definition carefully so that you can independently identify when a depression screening is necessary.
2. To address this measure, follow the exact instructions below to appropriately add patients to the denominator, numerator, exclusion, and/or exception.
3. When asked to apply a Document Tag, make sure you select one that was created by Elation, and not by a user in your practice. Patients who are accounted for correctly with the workflows below will automatically appear in your CQM report.
4. Once the automated clinical reminders and optimized workflows are available later this year, we will update the instructions below to reflect these changes.

##

## **Meeting requirements**

1. If the patient is 12 years and older by January 1, 2025, create an Elation visit note (any layout) with a date that falls in the 2025 calendar year.
   - Doing so will add the patient to the measure’s Denominator.
2. Document a Depression Screening:
   1. Go to the **Psych** section of the Clinical Profile and then click “add special”.
   2. Select “Depression (PHQ-2 Questionnaire)” or “Depression (PHQ-9 Questionnaire)”.
   3. Complete the questionnaire with the patient.
      1. If the result is negative, no further action is needed.
         - If the patient has a PHQ-2 score less than or equal to 2 (negative result), then they will be automatically added to the measure's Numerator.
         - If the patient has a PHQ-9 score less than or equal to 4 (negative result), then they will be automatically added to the measure's Numerator.
      2. If the result is positive, record a follow-up plan on the date of the visit or up to 2 days after the date of the visit. The follow-up plan must be one of the following actions.

| | |
| --- | --- |
| Prescribe pharmaceutical intervention. | Prescribe pharmaceutical intervention using [Elation’s Prescription Form](Prescriptions-Forms-Guide-ePrescribing-and-ordering-meds.md) on the date of the visit or two days prior to the visit. Select the appropriate medication from Elation’s database (i.e. not a user created medication) in order for the system to calculate the patient in the Numerator. [Click here for a list of medications that meet this requirement](https://elation.my.salesforce.com/sfc/p/37000000L9cg/a/Ui000003Zhmj/LIILUVoOLWmUooyViotVpeqHwHe4Ctmbi2boObp6yi4). |
| Refer for counseling. | 1. Use the [Referral](https://help.elationemr.com/s/article/how-to-send-a-letter-on-elation) feature to refer the patient for counseling. 2. Add the corresponding Document Tag to the visit note to reflect the action taken during the encounter.     - The following Document Tags can be used for this follow-up action:      - *Referral to intellectual disability psychiatrist (procedure)*      - *Referral to intellectual disability psychiatry service (procedure)*      - *Referral to psychiatry service (procedure)*      - *Referral to psychiatrist for the elderly mentally ill (procedure)*      - *Refer to mental health worker (procedure)*      - *Referral to emergency clinic (procedure)*      - *Referral to liaison psychiatry service (procedure)*      - *Referral to psychogeriatric service (procedure)*      - *Referral to psychogeriatric day hospital (procedure)*      - *Referral to mental health counseling service (procedure)*      - *Referral for mental health counseling (procedure)*      - *Referral to mental health counselor (procedure)*      - *Referral to child and adolescent psychiatrist (procedure)*      - *Referral to psychologist (procedure)*      - *Referral to psychiatrist (procedure)*      - *Child referral - clinical psychologist (procedure)*      - *Referral to mental health team (procedure)*      - *Referral to primary care service (procedure)*      - *Referral to family therapy (procedure)*      - *Referral to support group (procedure)* |
| Prescribe other follow-up plan (besides pharmaceutical intervention or counseling). | 1. Take any actions you normally would to prescribe other follow-up plan(s) for depression (see options below). 2. Add the corresponding Document Tag to the visit note to reflect the action taken during the encounter.     - The following Document Tags can be used for this Numerator requirement:      - *Family psychotherapy procedure (regime/therapy)*      - *Brief group psychotherapy (regime/therapy)*      - *Expressive psychotherapy (regime/therapy)*      - *Individual psychotherapy (regime/therapy)*      - *Cognitive and behavioral therapy (regime/therapy)*      - *Exercise therapy (regime/therapy)*      - *Interactive group medical psychotherapy (regime/therapy)*      - *Implementation of measures to provide psychological support (regime/therapy)*      - *Coping support assessment (procedure)*      - *Coping support management (procedure)*      - *Emotional support assessment (procedure)*      - *Emotional support education (procedure)*      - *Emotional support management (procedure)*      - *Mental health history taking assessment (procedure)*      - *Mental health history taking education (procedure)*      - *Mental health history taking management (procedure)*      - *Telephone consultation (procedure)*      - *Completion of mental health crisis plan (procedure)*      - *Dialectical behavior therapy (regime/therapy)*      - *Mental health care assessment (procedure)*      - *Mental health care education (procedure)*      - *Mental health care management (procedure)*      - *Mental health promotion assessment (procedure)*      - *Mental health promotion education (procedure)*      - *Mental health promotion management (procedure)*      - *Mental health screening assessment (procedure)*      - *Mental health screening education (procedure)*      - *Mental health screening management (procedure)*      - *Mental health treatment assessment (procedure)*      - *Mental health treatment education (procedure)*      - *Management of mental health treatment (procedure)*      - *Case management follow up (procedure)*      - *Discharge by mental health primary care worker (procedure)*      - *Crisis intervention with follow-up (regime/therapy)* |

## **Documenting exclusions**

To exclude a **patient that has bipolar disorder**, the patient must have been diagnosed with bipolar disorder at any time prior to the qualifying 2025 visit note. This means one or more of the following must be true:

- An ICD-10 code for bipolar disorder is recorded in the patient’s Problem List with a start date prior to the date of qualifying 2025 visit note.
- An ICD-10 code for bipolar disorder is recorded in a visit note dated prior to the date of qualifying 2025 visit note.

[Click here for a list of qualifying ICD-10 codes for bipolar disorder](https://elation.my.salesforce.com/sfc/p/37000000L9cg/a/Ui000003Zhpx/zvHUPh1pT_bp7NbwL3.9k9tluS2j1e5lntc3inopivQ).

## **Documenting exceptions**

To document that a **patient refuses to participate in or complete the depression screening**:

1. Click the “+Tag” button in the corresponding visit note draft.
2. Add one of these Document Tags to the visit note based on the patient’s age:
   1. 12-17 years old: *Adolescent depression screening - declined (situation)*
   2. 18 years and older: *Adult depression screening - declined (situation)*

To document that the **patient has a CMS approved medical reason for not screening the patient for depression**:

1. Go to the “+Tag” section of the visit note draft.
2. Add the corresponding Document Tag to the visit note to reflect the CMS approved medical reason for not screening a patient for depression. Choose the *Adolescent* version for patients ages 12-17 and *Adult* version for patients 18 and older.

- - The following Document Tags can be used for this Denominator exception:
    - *Adolescent depression screening not performed - Procedure contraindicated (situation)*
    - *Adolescent depression screening not performed - Treatment not indicated (situation)*
    - *Adolescent depression screening not performed - Drug treatment not indicated (situation)*
    - *Adolescent depression screening not performed - Absent response to treatment (situation)*
    - *Adolescent depression screening not performed - Late effect of medical and surgical care complica...*
    - *Adolescent depression screening not performed - Drug resistance (disorder)*
    - *Adolescent depression screening not performed - Complication of medical care (disorder)*
    - *Adolescent depression screening not performed - Treatment not tolerated (situation)*
    - *Adolescent depression screening not performed - Not indicated (qualifier value)*
    - *Adolescent depression screening not performed - Contraindicated (qualifier value)*
    - *Adolescent depression screening not performed - Allergy to drug (finding)*
    - *Adolescent depression screening not performed - Procedure not indicated (situation)*
    - *Adolescent depression screening not performed - Intolerance to drug (finding)*
    - *Adolescent depression screening not performed - Adverse reaction caused by drug (disorder)*
    - *Adolescent depression screening not performed - Drug interaction (finding)*
    - *Adult depression screening not performed - Procedure contraindicated (situation)*
    - *Adult depression screening not performed - Treatment not indicated (situation)*
    - *Adult depression screening not performed - Drug treatment not indicated (situation)*
    - *Adult depression screening not performed - Absent response to treatment (situation)*
    - *Adult depression screening not performed - Late effect of medical and surgical care complication ...*
    - *Adult depression screening not performed - Drug resistance (disorder)*
    - *Adult depression screening not performed - Complication of medical care (disorder)*
    - *Adult depression screening not performed - Treatment not tolerated (situation)*
    - *Adult depression screening not performed - Not indicated (qualifier value)*
    - *Adult depression screening not performed - Contraindicated (qualifier value)*
    - *Adult depression screening not performed - Allergy to drug (finding)*
    - *Adult depression screening not performed - Procedure not indicated (situation)*
    - *Adult depression screening not performed - Intolerance to drug (finding)*
    - *Adult depression screening not performed - Adverse reaction caused by drug (disorder)*
    - *Adult depression screening not performed - Drug interaction (finding)*

[Reference: CMS2v14 eCQM Flow](https://ecqi.healthit.gov/sites/default/files/ecqm/measures/CMS2v14-eCQM-Flow.pdf)

# **Measure Information**

Depression affects more than two hundred sixty million people across the world and is a leading cause of disability, with a variety of depressive disorders that are independent risk factors for chronic diseases, such as cardiovascular disease and diabetes, lending screening for depression as paramount to identify depressive disorders that can affect the most vulnerable populations (Costantini et al., 2021). Results from a 2018 U.S. survey indicated that 14.4 percent of adolescents (3.5 million adolescents) had a major depressive episode (MDE) in the past year, with nine percent of adolescents (2.4 million adolescents) having one MDE with severe impairment (Substance Abuse and Mental Health Services Administration, 2019). The odds of a diagnosis of depression are believed to be 2.6 times greater for children and adolescents exposed to trauma as compared to those unexposed or less exposed (Vibhakar et al., 2019). Children and teens with major depressive disorder (MDD) have been found to have difficulty carrying out their daily activities, relating to others, growing up healthy, and are at an increased risk of suicide (Siu on behalf of the U.S. Preventive Services Task Force [USPSTF], 2016).

[Reference: Measure information from CMS](https://ecqi.healthit.gov/ecqm/ec/2025/cms0002v14?qt-tabs_measure=measure-information)

# **Frequently Asked Questions**

#### **How can I enter a PHQ-2 or PHQ-9 result from the past to count toward this measure’s Numerator?**

To document a past PHQ-2 or PHQ-9 result, enter it in the Psych section of the patient’s Clinical Profile in the exact format shown below:

- Depression: PHQ-2 Score: X (MM/DD/YYYY)
- Depression: PHQ-9 Score: X (MM/DD/YYYY)

For example, a PHQ-9 evaluation performed on May 1, 2025 with a score of 11 will look like:

- Depression: PHQ-9 Score: 11 (05/01/2025)

#### **Do I need to reference the PHQ-2 or PHQ-9 result in the visit note for it to count towards the Numerator?**

No, you do not need to reference any PHQ-2 or PHQ-9 results in visit notes for it to count towards the Numerator. By default, the measure will look for the score and the date of the evaluation in the **Psych** section of the patient’s Clinical Profile.

# **Related Articles**

- [MIPS (2025) Overview](https://help.elationemr.com/s/article/MIPS-2025-Overview)
- [Document Tags for Visit Notes & Reports Guide](https://help.elationemr.com/s/article/tag-reports-and-notes-with-document-tags)
- [MIPS (2025) - Quality Category](https://help.elationemr.com/s/article/MIPS-2025-Quality-Category)