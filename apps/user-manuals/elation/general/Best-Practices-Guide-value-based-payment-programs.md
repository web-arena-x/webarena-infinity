# Best Practices Guide- Using Elation for value-based payment programs

Source: https://help.elationhealth.com/s/article/Best-Practices-Guide-value-based-payment-programs

---

## **Contents**

- [What are value-based payment programs?](#description)
- [Which EHR features can be used for value-based payment programs?](#EHR_features)
- [Quick Start Guide](#quick_start)
- [Video Library](#Video_library)

## **What are value-based payment programs?**

Value-based payment programs are healthcare models and reimbursement approaches that focus on delivering high-quality healthcare while controlling costs. Value-based payment programs incentivize healthcare providers to prioritize patient outcomes and the overall value of care over volume of services delivered. These programs typically emphasize performance against quality metrics, risk adjustment coding and support for transition of care/care coordination services.



## **Which EHR features can be used for value-based payment programs?**

The following EHR features can help support value-based payment program related workflows. Features with an asterisk need to be manually enabled in your Elation Settings or be turned on by Elation.

- [Automatic Coding](https://help.elationemr.com/s/article/elation-coding-automation)\*
- [Clinical Reminders](https://help.elationemr.com/s/article/clinical-reminders-for-clinical-quality-measures)\*
- [MIPS Reporting](https://help.elationemr.com/s/article/MIPS-2023-Overview)
- [Popular CPT Codes](https://help.elationemr.com/s/article/billing-settings---service-locations--procedure-codes#Where%20do%20I%20find%20the%20Popular%20Procedure%20Codes%20list?)
- [Risk Assessment](https://help.elationemr.com/s/article/what-is-risk-assessment)\*
- [Visit Note Automation](https://help.elationemr.com/s/article/visit-note-automation)
- [Visit Note Templates](https://help.elationemr.com/s/article/elation-visit-note-templates)
- [Prescription insurance benefits information](Prescription-Form-Guide-patient-prescription-benefits.md)\*
- [Carequality integration](Carequality-Integration-Introduction.md)\*

## **Quick Start Guide**

| **Incorporate quality reporting CPT/ICD-10 codes in your encounter documentation to ease administrative burden and ensure you get credit for services delivered to your patients** |
| **Feature** | **How to turn on** | **Key workflows** |
| [Automatic Coding](https://help.elationemr.com/s/article/elation-coding-automation) - Automatically adds CPT and/or ICD-10 codes to the billing information section of your visit notes for body mass index assessments, blood pressure recordings, and negative PHQ-9 depression screening results documentation. | To turn on Automatic Coding, Admin level users in your practice can: 1. Navigate to the Settings page by clicking on your email address in the top right-hand corner of the page and selecting "Settings" from the dropdown menu. 2. Under Practice Settings in the leftmost pane, click "Billing". The Automatic Coding settings are at the top of this section. 3. Toggle the buttons next to *Body Mass Index*, *Blood Pressure*, and *PHQ-9* to green to turn the automatic coding features on for these components. | There are 3 key workflows to remember during each patient encounter. [Click here for more detailed information about the Automatic Coding feature](https://help.elationemr.com/s/article/elation-coding-automation). 1. Always record the height and weight for patients 18+ in the Vitals section of your visit notes. Elation will automatically calculate and display the patient's BMI for you when height and weight is recorded. 2. Always record controlled blood pressure readings in the Vitals section of your visit notes, especially for patients with 'Hypertension' and/or 'Diabetes' in their [Problem List](https://help.elationemr.com/s/article/managing-your-problem-list). 3. If you accessed the patient for depression using the [PHQ-9 questionnaire in the Clinical Profile](https://help.elationemr.com/s/article/structured-questionnaires) and referenced/exported the data into your visit note, Elation will add the G code to your bill for negative results. Positive results require a follow-up plan and therefore are not automatically coded for. |
| [Popular CPT Codes](https://help.elationemr.com/s/article/billing-settings---service-locations--procedure-codes#Where%20do%20I%20find%20the%20Popular%20Procedure%20Codes%20list?) - Store a list of commonly used Category II CPT codes for performance measures in your Popular CPT Codes database to easily add these codes to your encounter documentation. | This feature is always on in the EHR. To configure a a popular CPT Code database for your practice: 1. Navigate to the Settings page by clicking on your email address in the top right-hand corner of the page and selecting "Settings" from the dropdown menu. 2. Under Practice Settings, click "Billing". The Popular CPT Codes settings are towards the bottom of this section. 3. Click "+Add CPT Code" to add additional Category II CPT codes. | 1. If you performed any quality performance related actions during an encounter, enter the correlated procedure/service and its Category II CPT code in the Procedure section of your visit note. The code will then automatically be added to the bill for you to send along with your claims. - You can search for codes by description for easier documentation. |
| **Drive performance in quality measures to improve quality of care** |
| **Feature** | **How to turn on** | **Key workflows** |
| [Clinical Reminders](https://help.elationemr.com/s/article/clinical-reminders-for-clinical-quality-measures) - Reminds you to follow up on certain health conditions based on the patient's demographics and conditions. Tied to certain Clinical Quality Measures if you are participating in MIPS. | **(Providers Only)** To turn on Clinical Reminders for yourself: 1. Navigate to the Settings page by clicking on your email address in the top right-hand corner of the page and selecting "Settings" from the dropdown menu. 2. Under User Settings, click "Preferences". The Clinical Reminders (MIPS) section is at the bottom of this page. 3. Toggle the **Enable Clinical Reminder Service (CRS)** setting to "Yes" to turn on the overall Clinical Reminder feature. 4. Use the toggles to turn on individual Clinical Reminders for each patient care item you want to monitor for. To turn on Clinical Reminders for Staff level users in the practice: 1. Navigate to the Settings page by clicking on your email address in the top right-hand corner of the page and selecting "Settings" from the dropdown menu. 2. Under Practice Settings, click "Clinical Care Measure Settings". 3. Toggle the **Enable Clinical Reminder Service (CRS)** setting to "Yes" to turn on the overall Clinical Reminder feature. 4. Use the toggles to turn on individual Clinical Reminders for each patient care item you want staff to see while they assist you with preparing for an encounter. | 1. During each patient encounter, look at the top of the visit note draft to address any (or all) Clinical Reminders you see during the encounter. |
| [MIPS Reporting](https://help.elationemr.com/s/article/MIPS-2023-Overview) - Track your MIPS program performance and submit your data to CMS for reporting. | This feature can be turned on by an Elation Team member. To see if you have this feature on, look for the 'Clinical Quality Measures' report in the Reports section of the blue navigation bar at the top of your Elation account. | 1. Track outstanding quality measures for patients and use the MIPS reporting as a worklist for proactive outreach for care follow up. 2. Use the [Clinical Quality Measures Report](https://help.elationemr.com/s/article/elations-cqm-dashboards) to track your performance against the Quality category. 3. Use the [Promoting Interoperability Report](https://help.elationemr.com/s/article/Promoting-Interoperability-MIPS-2023) to track your performance against the Promoting Interoperability category. |
| **Define and manage risk tiers within your patient panel** |
| **Feature** | **How to turn on** | **Key workflows** |
| [Risk Assessment](https://help.elationemr.com/s/article/what-is-risk-assessment) - Shows you the level of 'risk' assigned to each patient based on the Centers for Medicare and Medicaid Services (CMS) HCC Risk Adjustment Model. | To turn on the Risk Assessment feature 1. Navigate to the Settings page by clicking on your email address in the top right-hand corner of the page and selecting "Settings" from the dropdown menu. 2. Under Practice Settings, click "Clinical Care Measure Settings". The Risk Assessment section is at the bottom of this page. 3. Toggle the Risk Assessment to "Yes" to turn on the Risk Assessment feature. | 1. Store all of your patient's active problems in their [Problem List](https://help.elationemr.com/s/article/managing-your-problem-list) in the Clinical Profile. 2. [Assess for all risk-adjusted conditions](https://help.elationemr.com/s/article/how-to-use-elations-risk-assessment-feature#patient_encounter) every calendar year. 3. Add the ICD-10 code for any assessed risk-adjusted condition in the billing section of your visit note. 4. [Monitor your patient panel](find-patients-with-elations-patient-list.md) by risk level. |
| **Automate documentation for common encounters** |
| **Feature** | **How to turn on** | **Key workflows** |
| [Visit Note Templates](https://help.elationemr.com/s/article/elation-visit-note-templates) - Create templated documentation for common evaluations and procedures (ex. annual exams) to expedite charting. | This feature is always on in the EHR. [Click here to learn more about creating Visit Note Templates](https://help.elationemr.com/s/article/elation-visit-note-templates). | 1. [Create Visit Note Templates](https://help.elationemr.com/s/article/visit-note-automation) for evaluations and procedures that must be performed periodically in adherence to program requirements. 2. [Tie Visit Note Template to Appointment Types](https://help.elationemr.com/s/article/visit-note-automation) to automate template application as needed. 3. Use Visit Note Templates as reminders for what you need to assess during an encounter and to expedite charting. Ex. Create a visit note template for annual wellness visits and link the template to an ‘Annual Exam’ Appointment Type to automate documentation and coding. |
| [Visit Note Automation](https://help.elationemr.com/s/article/visit-note-automation) - Automatically apply Visit Note Templates to visit notes based on the appointment type tied to the patient's appointment to expedite charting. | This feature is always on in the EHR. [Click here to learn more about the Visit Note Automation feature.](https://help.elationemr.com/s/article/visit-note-automation) | 1. [Create Appointment Types](https://help.elationemr.com/s/article/calendar-and-booking-settings) tied to evaluations and procedures that must be performed periodically in adherence to program requirements (ex. annual exams). 2. Tie [Visit Note Templates](https://help.elationemr.com/s/article/elation-visit-note-templates) to their correlated program-specific appointment types. 3. Associate patient appointments to program-specific appointment types as appropriate. 4. Open the patient's chart from their appointment to automatically create a visit note with its associated Visit Note Templates applied. Ex. Create a visit note template for annual wellness visits and link the template to an ‘Annual Exam’ Appointment Type to automate documentation and coding. |
| **Improve patient drug therapy experience while reducing the total cost of care of your patient panel** |
| [Prescription insurance benefits information](Prescription-Form-Guide-patient-prescription-benefits.md#cost_estimate) - Use prescription formulary and cost estimate details to make cost effective prescribing decisions for your patients | This feature will be available to all customers by October 4, 2023. Reach out to an Elation Team member if you are interested in using this feature earlier and we will turn this feature on for you. | 1. Review [prescription formulary information and cost estimate data](Prescription-Form-Guide-patient-prescription-benefits.md) when prescribing medications and select the most appropriate and cost effective medication for the patient. |
| **Connect to external patient data sources for a 360 view of your patient’s care delivery** |
| [Carequality integration](Carequality-Integration-Introduction.md) - Share and query for data from any Carequality-enabled providers | This feature is currently in beta. Reach out to an Elation Team member if you are interested in this feature and we can assess whether you are a good fit to be a beta tester. | 1. Query for new patient information during each encounter. |



## **Video Library**

[Click here to explore our video library about value-based payment program related features](https://vimeo.com/showcase/elation-vbp).



## **Related Articles**

- [Billing Guide- Creating a superbill & coding for your visit](billing.md)
- [Billing Guide- Navigating Billing Settings](billing-settings---service-locations--procedure-codes.md)
- [Clinical Reminders for Clinical Quality Measures](clinical-reminders-for-clinical-quality-measures.md)
- [Elation's Carequality Integration Introduction (Beta)](Carequality-Integration-Introduction.md)
- MIPS (2023) Overview
- [Patient List Report Guide- Searching your patient panel](find-patients-with-elations-patient-list.md)
- [Prescription Form Guide- Viewing patient prescription benefits](Prescription-Form-Guide-patient-prescription-benefits.md)
- [Problem List Guide](managing-your-problem-list.md)
- [Risk Assessment Introduction- Risk Assessment Factors (RAF) and Hierarchical Condition Categories (HCC)](what-is-risk-assessment.md)
- [Visit Note Documentation Guide- Using visit note automation for appointments](visit-note-automation.md) [Visit Note Templates Guide](elation-visit-note-templates.md)