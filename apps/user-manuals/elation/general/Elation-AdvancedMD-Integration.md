# Elation-AdvancedMD Integration Guide

Source: https://help.elationhealth.com/s/article/Elation-AdvancedMD-Integration

---

## **Contents**

- [What is AdvancedMD?](#description_AMD)
- [What is the Elation-AdvancedMD Integration?](#elation_amd)
- [How do I get started?](#get_started)
- [What information is synchronized?](#information_synced)
 - [Mapping Data](#mapping_data)
- [Patient Charts](#patient_charts)
 - [Creating Charts](#creating_charts)
 - [Merging Charts](#merging_charts)
 - [Deleting Charts](#deleting_charts)
- [Patient Demographics](#demographics)
- [Insurance](#insurance)
 - [Carriers](#carriers)
- [Appointments](#appointments)
- [Bills](#bills)
- [Getting Support](#getting_support)

## **What is AdvancedMD?**

AdvancedMD® is a Practice Management software that practices can use alongside Elation. Practices most commonly use AdvancedMD to submit claims to Payers for services rendered and track the progress of claim payments.



## **What is the Elation-AdvancedMD Integration?**

The Elation-AdvancedMD integration allows practices to send claims-related data from Elation to AdvancedMD for practices to submit claims to Payers (through AdvancedMD) for services rendered in Elation. The Elation-AdvancedMD integration reduces the need for double documenting in two softwares and allows practices to store all their clinical data in Elation while using AdvancedMD side-by-side to manage their revenue.



## **How do I get started?**

You must first have an account with AdvancedMD before you can use this integration. Elation will work with AdvancedMD to set you up on AdvancedMD and turn on the integration if you do not have an AdvancedMD account yet. You can send Elation a request to turn on the AdvancedMD integration by:

- emailing [implementation@elationhealth.com](mailto:implementation@elationhealth.com) if you are being onboarded to Elation
- emailing [integrations@elationhealth.com](mailto:integrations@elationhealth.com) after you exited the onboarding phase

## **What information is synchronized?**

| Data | Sync Direction |
| --- | --- |
| Patient Charts | AdvancedMD → Elation |
| Demographics | AdvancedMD → Elation |
| Insurance | AdvancedMD → Elation |
| Appointments | AdvancedMD → Elation |
| Bills | Elation → AdvancedMD |




## **Mapping Data**

Follow these instructions to map the following data between Elation & AdvancedMD:

1. **Providers**- notify Elation and/or AdvancedMD if new providers are added to both systems. Additional actions have to be taken on the backend to connect new providers to each other across systems.
2. **Practice Locations**- notify Elation and/or AdvancedMD if new Practice Locations (Service Locations) are added to both systems. Additional actions have to be taken on the backend to connect the new locations to each other across systems.
3. **Payers**- new insurance Carriers need to be added to the AdvancedMD Insurance Carriers list and to a patient chart in AdvancedMD in order to be pushed to Elation. Do not create new insurance carriers in Elation.
   1. You can manage insurance carriers in AdvancedMD under **System Settings >> Carriers >> Carriers**.
4. **Appointment Types**- Appointment Types are automatically synced from AdvancedMD to Elation.
5. **CPT Codes**- You can freely add CPT Codes in Elation and those will be automatically pushed to AdvancedMD.
   1. Add the CPT Code to your Fee Schedule in AdvancedMD (with an associated charge) if you have a default billed amount you want to assign to the CPT Code for your claims. You can find your Fee Schedule in AdvancedMD under **System Settings >> Fee Schedule**.
   2. While any CPT code entered in a bill will transfer from Elation to AdvancedMD, the CPT code and additional details will need to be added directly in your AdvancedMD Chart Code database if you require these details for your claims (ex. NDC information). You can add CPT Codes in AdvancedMD by going to **System Settings >> Transaction Codes >> Charge Codes**.



## **Patient Charts**

### **Creating Charts**

All patient charts must be created in AdvancedMD in order for the patient's chart to be created in Elation. See the [Patient Demographics section](#demographics) for details about managing demographics information after charts are created in Elation.

### **Merging Charts**

Each chart can only have a one to one connection between Elation and AdvancedMD and this connection is established upon chart creation. If you happen to see a duplicate chart for the same patient in Elation, please make sure you find the chart that is connected between the two systems and keep the connected chart after performing a merge.

- We recommend making a small demographic change in AdvancedMD to see which Elation chart the change occurs in. Once you locate the connected chart in Elation, you will merge the duplicate, not-connected chart into the connected one by following the steps detailed below.


Here are the proper merge steps for Elation charts:

1. Open the duplicate chart that is not connected to the integration
2. Click on the patient's name to open their Demographics
3. Click on the "Merge Chart" button
4. Find & select the chart you want to keep (the one that is connected to the integration)
5. Click "Merge Chart"
6. Confirm you understand the transfer of data and then click "Yes, merge charts"

### **Deleting Charts**

Deleting a chart in Elation will not delete the chart in AdvancedMD and vice versa. Please take caution when deleting charts in Elation while using the AdvancedMD integration as charts have a one to one connection via the integration. If the patient is still active in your practice, the deleted chart must be restored in order for the patient's information to sync properly across the two systems. Contact Elation using the "I need help" button if you need to restore a deleted chart in Elation.



## **Patient Demographics**

The synchronization of Patient Demographics is unidirectional from AdvancedMD to Elation. Any changes or updates to demographics information must occur in AdvancedMD. The following table shows a mapping of the Patient Demographics fields that are shared between Elation and AdvancedMD and their matching field names.

| Elation Field Name | AdvancedMD Field Name |
| --- | --- |
| Legal First Name | Patient Name    *\*When creating charts in AMD, the patient’s name must be entered as: Last name, First name Middle name* |
| Legal Last Name | Patient Name    *\*When creating charts in AMD, the patient’s name must be entered as: Last name, First name Middle name* |
| Date of birth | Date of Birth |
| Sex at Birth | Sex |
| Primary Phone - “Cell” from AdvancedMD will display as “Mobile” in Elation | Preferred Phone - The following phone number types will sync to Elation:   - Home, Work, Cell |
| Secondary Phone | Work Phone *or* Other |
| Email | Email |
| Address | Address |
| Ste or apt # | Apt / Ste # |
| City | City |
| State | State |
| Zip | Zip Code |
| Provider assigned in practice | Provider Profile    *\*A patient’s assigned provider will automatically be the first provider listed in Elation if the provider from AdvancedMD is not properly mapped between Elation and AdvancedMD.* |




## **Insurance**

The synchronization of insurance information is unidirectional from AdvancedMD to Elation. Practices must enter insurance information in AdvancedMD in order for the insurance information to push to Elation.
The following table lists the insurance related fields that are pushed from AdvancedMD to Elation and show how the AdvancedMD fields map to the Elation demographic fields for insurance. Fields that are not listed are not shared between Elation and AdvancedMD:

- **Important Note:** Only Primary Insurance and Secondary Insurance will sync between AdvancedMD and Elation.

| Elation Field Name | AdvancedMD Field Name |
| --- | --- |
| Insurance carrier name | Carrier |
| Group ID | Group # |
| Member ID | Subscriber ID |

### **Carriers**

Insurance Carrier details should only be maintained in AdvancedMD as AdvancedMD is the source of truth for insurance. It is most important for you to create Carriers in AdvancedMD to avoid creating duplicate Payers in Elation. Best practice is to create a unique Carrier in AdvancedMD for each unique Payer (with a unique Payer ID). You can manage insurance carriers in AdvancedMD under **System Settings >> Carriers >> Carriers**.

- **Important Note:** Elation ‘Plan’ level details are not supported by the integration. If it is important to distinguish between different coverage plans under different Payers, create a separate AdvancedMD **Carrier** for each coverage plan.



## **Appointments**

The synchronization of appointments is unidirectional from AdvancedMD to Elation. Practices must create new appointments in AdvancedMD for the appointment to push to the corresponding Provider calendar in Elation. After new appointments are created in AdvancedMD, you may update appointment details in AdvancedMD and the updates will push to Elation.

The following table lists the Appointment fields that are pushed from AdvancedMD to Elation and show how the AdvancedMD fields map to the Elation fields. Fields that are not listed are not shared between the Elation and AdvancedMD:

| Elation Field Name | AdvancedMD Field Name |
| --- | --- |
| Patient name | Last name, First name    *\*Displayed at the top of the appointment window* |
| Date | Date |
| Start Time | Time |
| Duration | Duration |
| Status    \*Only the following statuses are supported at this time: - Checked In - Checked Out - Canceled - No show | Status Indicator     *\*Displayed in the left hand column of the appointment window* |
| Provider | Provider |
| Appointment type | Appointment Type |

**Important Note**: Deleting an appointment in AdvancedMD will also delete the appointment in Elation. Best practice is to update the status of cancelled appointments to 'Canceled' instead of deleting it.




## **Bills**

The synchronization of bills is uni-directional from Elation to AdvancedMD. Once a provider signs a visit note in Elation, the billing information in the visit note will be pushed to AdvancedMD as a Superbill. Once a bill is pushed to AdvancedMD, edits must be made in both Elation and AdvancedMD if needed. If you are missing any CPT and ICD-10 codes upon signing your visit note, Elation will notify you and prompt you to update your billing information before sending it to AdvancedMD.

- **Important Note:** The "Delayed Billing" feature is supported by the AdvancedMD integration. Learn more about the feature [here](How-to-set-up-Delayed-Billing.md).


The following table lists the fields that are pushed from Elation to AdvancedMD and show how the Elation fields map to the AdvancedMD fields. Fields that are not listed are not shared between Elation and AdvancedMD:

| Elation Field Name | AdvancedMD Field Name |
| --- | --- |
| Procedure | Procedure |
| + Add Dx | ICD-10 Diagnosis Codes |
| Place of Service | POS |

- **User Tip:** If the bill is sent successfully from Elation to AdvancedMD, a billing reference number from AdvancedMD will be sent to Elation. This reference number will be stored in [Billing Home](https://help.elationemr.com/s/article/Billing-Home) and in the corresponding signed visit note/bill in the patient’s chart.



## **Getting Support**

### **AdvancedMD**

If you need assistance with your AdvancedMD configuration or have questions about the AdvancedMD Application, contact AdvancedMD by clicking on “Help” >> “Contact Support” in the black bar at the top of your AdvancedMD account.

### **Elation**

If you need assistance with Elation or the Elation-AdvancedMD integration, contact Elation using the "I need help" >> "I need help from an Elation Team Member" button at the top of your Elation account.



## **Related Articles**

- [Billing Guide- Delayed Billing](How-to-set-up-Delayed-Billing.md)