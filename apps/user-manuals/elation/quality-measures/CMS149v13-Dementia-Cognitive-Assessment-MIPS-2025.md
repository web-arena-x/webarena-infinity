# [CMS149v13] Dementia: Cognitive Assessment (MIPS 2025)

Source: https://help.elationhealth.com/s/article/CMS149v13-Dementia-Cognitive-Assessment-MIPS-2025

---

## **Contents**

- [Measure Details](#details)
- [Measure Parameters](#parameters)
- [Elation Workflows](#workflows)
- [Measure Information](#info)
- [Additional Information](#additional)

##

## **Measure Details**

Percentage of patients, regardless of age, with a diagnosis of dementia for whom an assessment of cognition is performed and the results reviewed at least once within a 12 month period who have two or more visits during the measurement period.

## **Measure Parameters**

**Numerator**: Patients for whom an assessment of cognition is performed and the results reviewed at least once within a 12-month period.

**Denominator**: All patients, regardless of age, with a diagnosis of dementia.

**Exclusions/Exceptions:**Documentation of patient reason(s) for not assessing cognition.

These are the exclusion document tags for this measure (**Reference**: [Tag Reports and Notes with Document Tags](tag-reports-and-notes-with-document-tags.md)):

- EXCLUSION: NO COG ASSESSMT

## **Elation Workflows**

**Important Note**: Elation has implemented dedicated workflows that reflect standardized requirements we do not control for certification to ensure structured and reportable tracking of measure specifications for supported electronic Clinical Quality Measures. To optimize performance per the specifications, please adhere precisely to the workflows outlined in the referenced Help Center article.

1. Add a diagnosis of dementia to the patient’s problem list:![]()
2. Patients with dementia will also receive a Clinical Reminders alert if a cognitive assessment is due. This will appear at the top of the chart, and allow you to address the issue directly.

![]()

1. Create any document that allows for document tags (Visit Note, Non-Visit Note, or Report) complete the cognitive assessment, and click the “+Tag” item at the bottom of the note, after clicking “+Tag,” search for “Cognitive Assessment” and add it to the note.
   - **Reference**: [Tag Reports and Notes with Document Tags](tag-reports-and-notes-with-document-tags.md)
2. If the document tagged with "COGNITIVE ASSESSMENT" is a Non-Visit Note or Report, a visit note needs to be documented on or after the date of the report in order for the measure to be properly counted.

**To Document an Exclusion:**

- Click +Tag at the bottom of a visit note, or other area where document tags can be added, and select “EXCLUSION: NO COG ASSESSMT”.

## **Measure Information**

An estimated 5.8 million of adults in the US were living with dementia in 2019. Dementia is often characterized by the gradual onset and continuing cognitive decline in one or more domains including memory, communication and language, ability to focus or pay attention, reasoning and judgment and visual perception (Alzheimer’s Association, 2019). Cognitive deterioration represents a major source of morbidity and mortality and poses a significant burden on affected individuals and their caregivers (Daviglus et al., 2010). Although cognitive deterioration follows a different course depending on the type of dementia, significant rates of decline have been reported. For example, one study found that the annual rate of decline for Alzheimer's disease patients was more than four times that of older adults with no cognitive impairment (Wilson et al., 2010). Nevertheless, measurable cognitive abilities remain throughout the course of dementia (American Psychiatric Association, 2007). Initial and ongoing assessments of cognition are fundamental to the proper management of patients with dementia. These assessments serve as the basis for identifying treatment goals, developing a treatment plan, monitoring the effects of treatment, and modifying treatment as appropriate.

[Reference: Measure Information from CMS](https://ecqi.healthit.gov/ecqm/ec/2025/cms0149v13)

## **Additional Information**

Tools for cognitive assessment:

- [Mini-Mental State Examination](https://elation.my.salesforce.com/sfc/p/37000000L9cg/a/1G000000uHdr/ZzVqQmhRLHywkGErt_pVKnMpfzADgt1egXb0sl1P7SA)
 - **Important Note**: The MMSE has not been well validated for non-Alzheimer's dementias
- [Mini-cog](https://elation.my.salesforce.com/sfc/p/37000000L9cg/a/1G000000uHe6/MPIurJ9BfH9Y4bZLb2FOUcW4rasXvfHORMfBQsA_YVw)

Use these tools to satisfy Dementia: Cognitive Assessment, which tracks the percentage of older adults with a Dementia diagnosis who have had an annual cognitive assessment.

## **Related Articles**

- MIPS (2025) - Quality Category
- [Clinical Quality Measures Reports Guide](elations-cqm-dashboards.md)
- [Clinical Reminders for Clinical Quality Measures](clinical-reminders-for-clinical-quality-measures.md)
- [Tag Reports and Notes with Document Tags](tag-reports-and-notes-with-document-tags.md)
- [MIPS (2025) Overview](MIPS-2024-Overview.md)