# Coding Guide - Managing periodic ICD-10 code updates

Source: https://help.elationhealth.com/s/article/ICD-10-code-updates

---

# **Contents**

- [Overview](#overview)
 - [What are ICD-10 code updates?](#description)
 - [How does Elation maintain the latest ICD-10 code changes?](#Elation_updates)
- [Workflow Instructions](#workflows)
 - [Managing yearly ICD-10 updates](#update_codes)
- [Resources](#resources)

# **Overview**

## **What are ICD-10 code updates?**

Every year, the Centers for Medicaid & Medicaid Services (CMS) updates the list of ICD-10 codes permitted for billing patient encounters. The yearly update includes ICD-10 code additions, revisions, and deletions. [Click here to review the latest ICD-10 code information from CMS](https://www.cms.gov/medicare/coding-billing/icd-10-codes).

## **How does Elation maintain the latest ICD-10 code changes?**

To ensure only valid ICD-10 codes are used, Elation automatically updates your account with the corresponding ICD-10 code changes on the date that the changes take effect. Once this update is complete,:

- Only valid ICD-10 codes will appear as search results within  the problem lists, visit note assessment, and Billing Form.
- Deprecated ICD-10 codes will continue to remain in all historical records, including the patient’s Problem List.
 - You will still be able to export deprecated ICD-10 codes to the **Assessment** section of the visit note, but you will not be able to export deprecated ICD-10 codes to the **Billing** section of the visit note since deprecated codes are non-billable. [Click here to learn more about managing deprecated ICD-10 codes](https://help.elationemr.com/s/article/Managing-deprecated-ICD10-codes).
 - To identify deprecated ICD-10 codes in the Problem List, use one of the two methods:
    - Look for an orange dot to the left of the problem.
    - Refer to a banner at the the top of the Problem List that tells you how many non-billable codes are in the Problem List.

# **Workflow Instructions**

## **Managing yearly ICD-10 updates**

To avoid exporting deprecated ICD-10 codes to your visit notes, we recommend

1. Updating any deprecated ICD-10 codes in your patients’ Problem List with one of the following options detailed in [this article](https://help.elationemr.com/s/article/Managing-deprecated-ICD10-codes).
   1. Review and update any deprecated ICD-10 codes in each patient’s Problem List as they come in for their next encounter.
   2. Search for all patients with deprecated ICD-10 codes and update them before waiting for the patients’ next encounters.
2. Reviewing your Visit Note Templates and updating any deprecated ICD-10 codes with appropriate, current alternatives.

# **Resources**

- [CMS ICD-10 Details](https://www.cms.gov/medicare/coding-billing/icd-10-codes)
- [2025 Model Software/ICD-10 Mappings](https://www.cms.gov/medicare/payment/medicare-advantage-rates-statistics/risk-adjustment/2025-model-software/icd-10-mappings)

# **Related Articles**

- [Coding Guide - Managing deprecated, non-billable ICD-10 codes](https://help.elationemr.com/s/article/Managing-deprecated-ICD10-codes)
- [Coding Guide - Managing periodic CPT code updates](https://help.elationemr.com/s/article/Managing-periodic-CPT-code-updates)