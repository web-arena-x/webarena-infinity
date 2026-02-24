# Promoting Interoperability (MIPS) - Health Information Exchange (HIE) - Sending & Receiving Health Information

Source: https://help.elationhealth.com/s/article/Promoting-Interoperability-MIPS-HIE-Sending-Receiving-Health-Information

---

## **Contents**

- [Part 1: Support Electronic Referral Loops by Sending Health Information](#sending_health_information)
 - [Measure Details](#P1_measure_details)
 - [Measure Parameters](#P1_measure_parameters)
 - [Elation Workflows](#P1_workflows)
 - [Additional Information](#P1_additional_info)
- [Part 2: Support Electronic Referral Loops by Receiving Health Information](#receiving_health_information)
 - [Measure Details](#P2_measure_details)
 - [Measure Parameters](#P2_measure_parameters)
 - [Elation Workflows](#P2_workflows)
 - [Additional Information](#P2_additional_info)

## **Part 1: Support Electronic Referral Loops by Sending Health Information**

### **Measure Details**

For at least one transition of care or referral, the MIPS eligible clinician that transitions or refers their patient to another setting of care or health care provider — (1) creates a summary of care record using certified electronic health record technology (CEHRT); and (2) electronically exchanges the summary of care record.

### **Measure Parameters**

**Numerator**: The number of transitions of care and referrals in the denominator where a summary of care record was created using CEHRT and exchanged electronically.

**Denominator**: Number of transitions of care and referrals during the performance period for which the MIPS eligible clinician was the transferring or referring health care clinician.

**Exclusion**: Any MIPS eligible clinician who transfers a patient to another setting or refers a patient fewer than 100 times during the performance period.

### **Elation Workflows**

This objective needs to be met for at least 1 patient. In the patient's visit note, attach any reports that you have reviewed during the encounter. At the bottom of the visit note, you must indicate that the patient is undergoing a transition of care to an outside provider in the MIPS section. Afterwards, sign the visit note, attach the visit note to an Elation Referral and send the referral electronically to the receiving provider via Elation. Please reference the exact steps outlined below:

1. Start a visit note draft for a patient encounter
2. Link any reports relevant to the visit to the visit note draft. While the visit note draft is open, you can link a report to a visit note with the options below:
   1. Find the report in the patient’s Chronological Record. Click "Actions" >> "Export to Note as Data"
      - **User Tip**: If your computer display is large enough for the 3 Pane View and you can see the Chronological Record alongside your visit note draft, click on the report’s name to open the report. The report will automatically be referenced in the 'Data' section of your visit note draft.
   2. Click on the "Reports" button at the top of the patient's chart to open the 'Reports' window. Click on the name of a report to expand the report. The report will automatically be referenced in the 'Data' section of your visit note draft.
3. Check the box for "Referring to another setting or provider" at the bottom of the visit note draft.
4. Click “Yes” for “Was summary of care record provided?”.
5. Lastly, sign your visit note. This will associate the patient to the Denominator for this measure.

![]()

1. Attach the visit note to a Referral and send the Referral. This will associate the patient with the Numerator for this measure.
   1. Click the “Referral” button at the top of the same patient's chart.
   2. In the “To” field, enter the recipient. If sending to a non-Elation provider, you must include either a fax, email, or Direct Address in the recipient's Contact details. If the provider is already using Elation, the Referral will be sent directly to their Elation account.

![]()

1. Scroll to the Attachments section. Do not delete any of the existing attachments (Clinical Profile and Demographics). Click “Select chart items to attach” and check the box for the visit note that you signed. When prompted to include linked reports, click “Yes”. Afterwards click “Attach Items”.

![]()

1. Lastly, click either “Sign, Send & Print Pt Copy” to send the Referral and print a copy for the patient or “Sign & More" >> "Sign & Send” if you do not need to print.![]()

##

### **Additional Info/FAQs**

Your signed Visit Note must be sent to a provider via an Elation Referral in order for you to receive credit for both the numerator and denominator for this measure. Simply checking the fields at the bottom of the Visit Note in the absence of a Referral does not qualify. Sending a Referral without the Visit Note attached also does not qualify.

[CMS 2023 MIPS Promoting Interoperability User Guide](https://www.cms.gov/files/document/medicare-pi-program-webinar-presentation.pdf)

## **Part 2: Support Electronic Referral Loops by Receiving and Reconciling Health Information**

### **Measure Details**

For at least one electronic summary of care record received for patient encounters during the performance period for which a MIPS eligible clinician was the receiving party of a transition of care or referral, or for patient encounters during the performance period in which the MIPS eligible clinician has never before encountered the patient, the MIPS eligible clinician conducts clinical information reconciliation for medication, medication allergy, and current problem list.

##

### **Measure Parameters**

**Numerator**: The number of electronic summary of care records in the denominator for which clinical information reconciliation is completed using CEHRT for the following three clinical information sets: (1) Medication – Review of the patient's medication, including the name, dosage, frequency, and route of each medication; (2) Medication allergy – Review of the patient's known medication allergies; and (3) Current Problem List – Review of the patient’s current and active diagnoses.

**Denominator**: Number of electronic summary of care records received using CEHRT for patient encounters during the performance period for which a MIPS eligible clinician was the receiving party of a transition of care or referral, and for patient encounters during the performance period in which the MIPS eligible clinician has never before encountered the patient.

**Exclusion**: Any MIPS eligible clinician who receives transitions of care or referrals or has patient encounters in which the MIPS eligible clinician has never before encountered the patient fewer than 100 times during the performance period.

### **Elation Workflows**

Receive a CCDA from the care setting who referred the patient to your practice within 2 months of the encounter date (up to 1 month before or after the visit). This can be achieved in two ways:

1. Receive a CCDA in Elation through Direct Message. All Elation providers are assigned a Direct Address and providers outside of Elation can send a CCDA file directly to this Direct Address. Providers can locate their Direct Address under "Settings" >> "Account Details" >> "Direct address". The Direct address ends with '[direct.elationemr.com](http://direct.elationemr.com)'. If you do not see a Direct Address listed, you can [Contact Support](https://help.elationhealth.com/s/contactsupport) to request one.
2. Receive a CCDA outside of Elation. If you’ve obtained a CCDA file outside of Elation, you can drag and drop the CCDA file into the Elation chart to upload. (instructions [linked here](import-patient-information-from-another-ehr-c-cda-format.md))

Follow the workflow below to complete clinical information reconciliation:

1. Sign Off on the CCDA file and import any relevant medications, allergies and problems from the CCDA file into the patient's chart
2. At the bottom of your visit note, check the box for Select “Received from other setting or provider”. This must be done before you sign off on the visit note.![]()
3. Specify "Yes" for the question "Were medications, allergies, and problems reconciled during encounter?"
4. Sign the Visit Note

### **Additional Info/FAQs**

The CCDA for the encounter must be imported into the patient’s chart within 2 months of the encounter (up to 1 month before and 1 month after the encounter date) in order for the CCDA to be counted towards the measure.

[CMS 2023 MIPS Promoting Interoperability User Guide](https://www.cms.gov/files/document/medicare-pi-program-webinar-presentation.pdf)

## **Related Articles**

- Promoting Interoperability (MIPS 2023)