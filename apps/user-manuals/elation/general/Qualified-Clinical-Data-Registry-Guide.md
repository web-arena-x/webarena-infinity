# Qualified Clinical Data Registry (QCDR) Guide

Source: https://help.elationhealth.com/s/article/Qualified-Clinical-Data-Registry-Guide

---

## **Contents**

- [What is a Qualified Clinical Data Registry (QCDR)?](#description)
- [Collection Types](#colllection_types)
- [What does Elation support for Quality measures and collection types?](#support)

## **What is a Qualified Clinical Data Registry (QCDR)?**

A Qualified Clinical Data Registry (QCDR) is an entity approved by the Centers for Medicare & Medicaid Services (CMS) to collect clinical data for the purpose of tracking to support quality improvement. Unlike traditional claims-based reporting, QCDRs can collect a broader range of clinical data, including patient-reported outcomes and data from electronic health records (EHRs). They often offer measures beyond those available in the standard MIPS program, allowing for more specialized and relevant quality reporting, and are frequently used by ACOs to aggregate and report quality metrics across participating practices. QCDRs are an outside entity that is registered to calculate quality measures and report that data to CMS programs.

QCDRs accept data in multiple formats, have a variety of ways to work with them, and are available for additional understanding and hands on support of providers for reporting requirements. Elation customers have worked with outside QCDRs successfully to report to MIPS and other CMS programs. If you would prefer hands on support for MIPS reporting, a QCDR would be a good option as Elation offers the technology tools, but does not offer hands on support for reporting. Here are some QCDRs you can use:

- [Healthmonix](https://healthmonix.com/?utm_term=healthmonix&utm_campaign=RR+-+MIPS+Campaign&utm_source=adwords&utm_medium=ppc&hsa_acc=8408405268&hsa_cam=16602259110&hsa_grp=131965243902&hsa_ad=588439124547&hsa_src=g&hsa_tgt=kwd-1644891274937&hsa_kw=healthmonix&hsa_mt=e&hsa_net=adwords&hsa_ver=3&gad_source=1&gclid=Cj0KCQjwhMq-BhCFARIsAGvo0KcgOoPDyUdWOMWF0u5-4HBTs0vvWlsTTknzR1U4ntqlqS2L8wWI-r8aAo3zEALw_wcB)
- [MDinteractive](https://mdinteractive.com/)

Working with a QCDR generally works by providing the CCDA download from Elation which can be accomplished by referencing this [Help Center Article](Supported-Elation-CCDA-types.md).

An analogy of how this works is similar to reporting taxes. Elation is similar to a TurboTax and provides the technology and information but as you have more complicated tax reporting and schedules to report you may need to hire a CPA. A QCDR works similarly in this way that they will take the data and support you with your submission beyond what Elation supports.

## **Collection Types**

- **Electronic Clinical Quality Measures (eCQMs)**
 - eCQMs are standardized measures that a Certified EHR Technology (CEHRT) meets to specification and is certified to. There are currently 47 eCQMs available to report to MIPS in 2025. Elation is certified to 12 eCQMs, and 9 eCQMs are eligible for Traditional MIPS reporting. eCQMs are measured as part of your regular workflows and can be found regularly in the Quality Dashboard of Elation. During reporting, eCQMs are extracted as a QRDA file and submitted to the QPP.
 - Important Note: (QRDA files and eCQMs are used and submitted to other CMS programs and are applicable for other program participants as such, eCQMs no longer applicable in traditional MIPS are applicable for MVPs and APMs and remain in production and functionality in Elation.s well).
 - These are the eCQMs that Elation supports in 2025 (9 bolded eCQMs that contribute to traditional MIPS and the total 12):
 - [**[CMS124v13] Cervical Cancer Screening (MIPS 2025)**](https://help.elationhealth.com/s/article/CMS124v13-Cervical-Cancer-Screening-MIPS-2025)
 - [**[CMS122v13] Diabetes: Glycemic Status Assessment Greater Than 9% (MIPS 2025)**](https://help.elationhealth.com/s/article/CMS122v13-Diabetes-Glycemic-Status-Greater-than-9percent)
 - [**[CMS131v13] Diabetes: Eye Exam (MIPS 2025)**](https://help.elationhealth.com/s/article/CMS131v13-Diabetes-Eye-Exam-MIPS-2025)
 - [**[CMS139v13] Falls: Screening for Future Fall Risk (MIPS 2025)**](https://help.elationhealth.com/s/article/CMS139v13-Falls-Screening-for-Future-Fall-Risk-MIPS-2025)
 - [**[CMS149v13] Dementia: Cognitive Assessment (MIPS 2025)**](https://help.elationhealth.com/s/article/CMS149v13-Dementia-Cognitive-Assessment-MIPS-2025)
 - [**[CMS155v13] Weight Assessment and Counseling for Nutrition and Physical Activity for Children and Adolescents (MIPS 2025)**](https://help.elationhealth.com/s/article/CMS155v12-Weight-Assessment-and-Counseling-for-Nutrition-and-Physical-Activity-for-Children-and-Adolescents-MIPS-2025)
 - [**[CMS165v13] Controlling High Blood Pressure (MIPS 2025)**](https://help.elationhealth.com/s/article/CMS165v13-Controlling-High-Blood-Pressure-MIPS-2025)
 - **[CMS2v14] Preventive Care and Screening: Screening for Depression and Follow-Up Plan (MIPS 2025)**
 - **[CMS159v13] Depression Remission at Twelve Months (MIPS 2025)**
 - [[CMS69v13] Preventive Care and Screening: Body Mass Index (BMI) Screening and Follow-Up Plan (not available for Traditional MIPS)](https://help.elationhealth.com/s/article/CMS69v13-Preventive-Care-and-Screening-Body-Mass-Index-BMI-Screening-and-Follow-Up-Plan)
 - [[CMS125v13] Breast Cancer Screening (not available for Traditional MIPS)](https://help.elationhealth.com/s/article/CMS125v13-Breast-Cancer-Screening)
 - [[CMS130v13] Colorectal Cancer Screening (not available for Traditional MIPS)](https://help.elationhealth.com/s/article/CMS130v13-Colorectal-Cancer-Screening)
- **MIPS Clinical Quality Measures (CQMs)**
 - MIPS CQMs are often collected by third party intermediaries and submitted on behalf of MIPS eligible clinicians. You may choose to work with a  Qualified Registry.
- **Medicare Part B Claims Measures**
 - This collection type is only available to those designated with the small practice special status (15 or fewer clinicians). Medicare Part B claims measures are always reported with the clinician’s individual (rendering) NPI even when reporting as a group, subgroup (MVPs only) virtual group (traditional MIPS), or APM Entity. For more information about reporting quality measures through Medicare Part B claims, download [this guide](https://qpp-cm-prod-content.s3.amazonaws.com/uploads/2649/2024PartBClaimsReportingGuide.pdf) from the QPP.

## **What does Elation support for Quality measures and collection types?**

Elation supports 12 eCQMs, 9 of which count in Traditional MIPS, and 3 are used in the MVP Value in Primary Care group. Administrative Claims Based measures may be selected to support additional measure selections for MIPS to report for Traditional MIPS and MVPs. Elation supports APM reporting with the selected eCQMs, and other measures supported depending on collection type.

- **Traditional MIPS:** You may report using 6 eCQMs or a combination of eCQMs and claims based measures, or reporting through a registry. To report through a registry, we recommend connecting with MDInteractive.
- **MVPs:** You may report on the Value in Primary Care MVP the 4 bolded measures above which include 3 eCQMs and 1 Claims Based Measures.
- **APP:** If you have signed up with an APM to participate this year, such as an ACO, or REACH, ensure your quality reporting is aligned with the measures the ACO administrator selected and only one quality submission is required, the quality submission reported with your APM.

**Important Note**: Elation Health provides the tools to support certain reporting requirements. All reporting requirements are the sole responsibility of the reporting provider. The changing nature of CMS programs and MIPS as part of those programs, require continuous changes to the program. If you have concerns with the measures required to report to MIPS or CMS programs please direct that feedback to CMS and the QPP. Elation Health provides a certain set of eCQMs that require significant development work to meet requirements for PCPs. If you have additional needs beyond the eCQMs that are supported in Elation, such as, support with reporting to MIPS or CMS programs, that should be directed to those relevant agencies. The QPP provides a not insignificant amount of support for reporting.

## **Related Articles**

- [Patient Chart Guide- Sharing clinical care summaries with collaborating providers using C-CDA (CCDA) format](Supported-Elation-CCDA-types.md)