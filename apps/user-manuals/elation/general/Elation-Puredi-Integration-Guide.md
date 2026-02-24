# Elation-Puredi Integration Guide- Using Puredi as your Revenue Cycle Management system alongside Elation

Source: https://help.elationhealth.com/s/article/Elation-Puredi-Integration-Guide

---

## **Contents**

- [What is Puredi?](#Puredi-intro)
- [What is the Elation-Puredi Integration?](#integration_overview)
- [How do I get started?](#getting_started)
- [Accessing Puredi from Elation EHR](#accessing_Puredi)
- [What information is synchronized?](#information_sync)
 - [Mapping Data](#mapping_data)
- [Patient Charts](#patient_charts)
 - [Creating Charts](#create_charts)
 - [Merging Charts](#merge_chart)
 - [Deleting Charts](#delete_chart)
- [Patient Demographics](#demographics)
- [Insurance](#insurance)
 - [Carriers](#carriers_and_plans)
- [Appointments](#appointments)
- [Bills](#bills)
 - [Additional billing fields](#additional_billing_fields)
- [Getting Support](#support)




## **What is Puredi?**

Puredi® is a Revenue Cycle Management software that practices can use alongside Elation. Practices most commonly use Puredi to submit claims to Payers for services rendered and track the progress of claim payments.


## **What is the Elation-Puredi Integration?**

The Elation-Puredi integration allows practices to send claims-related data from Elation to Puredi for practices to submit claims to Payers (through Puredi) for services rendered in Elation. The Elation-Puredi integration reduces the need for double documenting in two softwares and allows practices to store all their clinical data in Elation while using Puredi side-by-side to manage their revenue.



## **How do I get started?**

You must first have an account with Puredi before you can use this integration. Elation will work with Puredi to set you up on Puredi and turn on the integration if you do not have Puredi account yet. You can send Elation a request to turn on the Puredi integration by

- emailing [implementation@elationhealth.com](mailto:implementation@elationhealth.com) if you are being onboarded to Elation
- emailing [integrations@elationhealth.com](mailto:integrations@elationhealth.com) after you exited the onboarding phase

## **Accessing Puredi from Elation EHR**

Customers using Elation and Puredi can access the Puredi login page directly from Elation. Click on the "Billing System" button under the "Billing" button at the top of the Elation Practice Home page to access the Puredi login page.
![]()


## **What information is synchronized?**

| | |
| --- | --- |
| **Data** | **Sync Direction** |
| Patient Charts | Elation ****→****Puredi |
| Demographics | Elation ****↔**** Puredi |
| Insurance | Elation ****→****Puredi |
| Appointments | Elation ****→****Puredi \* |
| Bills | Elation ****→****Puredi |

##

### **Mapping Data**

Follow these instructions to map the following data between Elation & Puredi:

1. Providers- notify Elation and/or Puredi if new providers are added to both systems. Additional actions have to be taken on the backend to connect new providers to each other across systems
2. Practice Locations-  notify Elation and/or Puredi if new Practice Locations (Service Locations) are added to both systems. Additional actions have to be taken on the backend to connect new locations to each other across systems


You can freely add Appointment Types and CPT Codes in Elation and those will be automatically pushed to Puredi.

## **Patient Charts**

### **Creating Charts**

All patient charts must be created in Elation in order for the patient's chart to be created in Puredi. See the [Patient Demographics section](#demographics) for details about managing demographics information after charts are created in Elation.

####

### **Merging Charts**

Each chart can only have a one to one connection between Elation and Puredi and this connection is established upon chart creation. If you happen to see a duplicate chart for the same patient in Elation, please make sure you find the chart that is connected between the two systems and keep the connected chart after performing a merge.

- For example, patient John Smith has one chart in Puredi but two charts in Elation. The best way to find out which of the two charts in Elation is connected to Puredi is by looking at the "External Link" field in Puredi to see which Elation Patient ID is tied to the Puredi chart.


Here are the proper merge steps for Elation charts:

1. Open the duplicate chart that is not connected to the integration
2. Click on the patient's name to open their Demographics
3. Click on the "Merge Chart" button
4. Find & select the chart you want to keep (the one that is connected to the integration)
5. Click "Merge Chart"
6. Confirm you understand the transfer of data and then click "Yes, merge charts"

### **Deleting Charts**

Deleting a chart in Elation will not delete the chart in Puredi and vice versa. Please take caution when deleting charts in Elation while using the Puredi integration as charts have a one to one connection via the integration. If the patient is still active in your practice, the deleted chart must be restored in order for the patient's information to sync properly across the two systems. Contact Elation using the "I need help" button if you need to restore a deleted chart in Elation.


## **Patient Demographics**

After a patient's chart is created in Elation, the synchronization of Patient Demographics is bi-directional. Any changes made in one system will be pushed to the other system. The following table shows a mapping of the Patient Demographics fields that are shared between Elation and Puredi and their matching field names.

- **User Tip**: As best practice, we recommend managing demographics in Elation when possible because you will already be managing insurance information and appointments in Elation. This will allow your front office staff to stay in one system (Elation) for a majority of their work.

| Elation Field Name | Puredi Field Name |
| --- | --- |
| Legal First Name | First |
| Legal Last Name | Last |
| Date of birth | Birth Date |
| Sex at Birth | Gender |
| SSN | SSN |
| Ethnicity | Race/Ethnicity |
| Home Phone | Home Phone |
| Mobile Phone | Mobile Phone |
| Email | Primary Email |
| Address | Address |
| Ste or apt # | Address |
| City | City |
| State | State |
| Zip | Zip |
| Provider Assigned in Practice | Provider |
| Elation Patient ID | External Link |




## ****Insurance****

The synchronization of insurance information is uni-directional from Elation to Puredi. Practices must enter insurance information in Elation in order for the insurance information to push to Puredi.

The following table lists the insurance related fields that are pushed from Elation to Puredi and show how the Elation fields map to the Puredi fields. Fields that are not listed are not shared between Elation and Puredi:

| Elation Field Name | Puredi Field Name |
| --- | --- |
| Insurance Carrier Name | Payer |
| Group ID | Group Number |
| Member ID | Member Id |

**User Tip**: The Insurance Policyholder fields are not connected via the integration. If the patient insurance policyholder is not the patient, please enter the policyholder's information in both Elation and Puredi.

### **Carriers**

Insurance Carriers and plans details should only be maintained in Elation as Elation is the source of truth for insurance. It is most important for you to create Carriers in Elation to avoid creating duplicate Payers in Puredi.

**Important Note**: Elation 'Plans' do not sync to Puredi. If a specific Payer has multiple Plans and there is a different Payer ID or mailing address for different Plans, we recommend creating separate Elation 'Carriers' for each Payer ID or Mailing Address.

- For example: The Payer called "American Global Insurance" has a PPO option (with Payer ID 1234) and a Medicare Advantage option (with Payer ID 6789). I will create two Carriers in Elation to make sure claims are routed properly in Puredi- one Carrier called "American Global Insurance- PPO" and one called "American Global Insurance- Medicare Advantage". This way I will also have two separate Payers in Puredi to house the respective Payer ID's.

## **Appointments**

The synchronization of new appointments is uni-directional from Elation to Puredi. Practices must create new appointments in Elation for the appointment to push to the corresponding Provider calendar in Puredi.

After new appointments are created in Elation, you may update appointment details in either Elation or Puredi. We recommend making updates in Elation when possible to keep workflows in one system and have a single source of truth for Appointment details.

The following table lists the Appointment fields that are pushed from Elation to Puredi and show how the Elation fields map to the Puredi fields. Fields that are not listed are not shared between the Elation and Puredi:

| Elation Field Name | Puredi Field Name |
| --- | --- |
| Patient name | Patient |
| Description - chief complaint (CC) | Reason for Visit |
| Date | Date |
| Start time | Time |
| Duration | End Time |
| Appointment Type | Appointment Type |
| Status | Appointment Status |
| Provider | Resource & Provider |
| Location | Facility |




## **Bills**

The synchronization of bills is uni-directional from Elation to Puredi. Once a provider signs a visit note in Elation, the billing information in the visit note will be pushed to Puredi as a *Claim*. Once a bill is pushed to Puredi, edits must be made in both Elation and Puredi if needed. If you are missing any CPT and ICD-10 codes upon signing your visit note, Elation will notify you and prompt you to update your billing information before sending it to Puredi.


**Important Note**: The "Delayed Billing" feature is supported by the Puredi integration. Learn more about the feature [here](https://help.elationemr.com/s/article/How-to-set-up-Delayed-Billing).



The following table lists the fields that are pushed from Puredi to Elation and show how the Puredi fields map to the Elation fields. Fields that are not listed are not shared between Elation and Puredi:

| Elation Field Names | Puredi Field Names |
| --- | --- |
| CPT Code | Service |
| Modifier | Modifiers |
| Dxs | Dx |
| Service Location (POS) | Facility |

### **Additional billing fields**

You can enable additional billing fields, especially for incident-to billing, and synchronize these fields from Elation EHR to Puredi. The fields include S**upervising Provider**, **Billing Provider**, and **Prior Authorization** and the mapping is shown below. To enable any of these fields:

1. Go to Elation EHR
2. Click on your email at the top of your account and then click “Settings”
3. Click “Billing” to open the Billing settings
4. Scroll down to the Billing Fields section
5. Click on the toggle to configure the fields you want to include on your bills - green is ON (enabled) and gray is OFF (disabled)
6. Once a field is enabled, it will appear at the top of the bill in your EHR visit notes
   - Data stored in enabled fields will also push to Puredi when you push the bill over.

| Elation Field Names | Puredi Field Names |
| --- | --- |
| Supervising Provider | Supervising Provider |
| Prior Authorization | Auth Number |
| Billing Provider (appears after you check off the “Mark as incident-to encounter” box) | Billing Provider |

- **Billing Provider**: This field is commonly used for incident-to billing.




## **Getting Support**

####

### **Puredi**

If you need assistance with your Puredi configuration or have questions about the Puredi Application, contact Puredi here: [support@puredi.com](mailto:support@puredi.com)

####

### **Elation**

If you need assistance with Elation or the Elation-Puredi integration, contact Elation using the "I need help" >> "I need help from an Elation Team Member" button at the top of your Elation account.



## **Related Articles**

- [Patient Demographics Guide- Managing patient insurance](Managing-Insurance.md)
- [Billing Guide- Creating a Super Bill and coding for your visit](billing.md)
- [Billing Guide- Setting up CPT Codes and Place of Service](billing-settings---service-locations--procedure-codes.md)