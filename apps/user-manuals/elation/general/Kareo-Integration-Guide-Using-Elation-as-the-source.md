# Elation-Kareo Integration Guide- Using Elation as the source of truth for demographics and appointments

Source: https://help.elationhealth.com/s/article/Kareo-Integration-Guide-Using-Elation-as-the-source

---

**Overview**

This guide reviews one of two configurations for the Elation-Kareo integration. This version of the integration is for customers who want to complete majority of their front office workflows, such as patient intake and scheduling, in Elation and appointment information is not synchronized between Elation and Kareo. View the [Elation-Kareo Integration Guide- Using Kareo as the source of truth for insurance and appointments](Kareo-Integration-Guide-Using-Kareo-for-insurance-and-appointments.md) article if you wish to only enter insurance and appointments in Kareo.

## **Contents**

- [What is Kareo?](#Kareo_description)
- [What is the Elation-Kareo integration?](#integration_description)
- [How do I get started?](#start)
 - [Mapping Providers](#map_providers)
 - [Mapping Practice Locations](#map_locations)
- [What information is synchronized?](#sync)
 - [Patient Charts](#charts)
    - [Creating Charts](#create_charts)
    - [Merging Charts](#merge_chart)
    - [Deleting Charts](#delete_chart)
 - [Patient Demographics](#demographics)
 - [Insurance](#insurance)
    - [Carriers & Plans](#carriers_and_plans)
    - [Adding insurance information](#add_insurance)
    - [Correcting insurance information](#correct_insurance)
    - [Updating insurance information with new policy](#update_insurance)
    - [Removing an inactive insurance policy from a list of policies](#remove_policy)
    - [Removing all inactive policies](#remove_insurance)
 - [Appointments](#appointments)
 - [Bills](#bills)
- [Getting Support](#support)
- [Frequently Asked Questions](#faq)

## **What is Kareo?**

Kareo® is a Practice Management and Medical Billing Solution software that practices can use alongside Elation. Practices most commonly use Kareo to submit claims to Payers for services rendered and track the progress of claim payments.

## **What is the Elation-Kareo integration?**

The Elation-Kareo integration allows practices to send claims-related data from Elation to Kareo for practices to submit claims to Payers (through Kareo) for services rendered in Elation. The Elation-Kareo integration reduces the need for double documenting in two softwares and allows practices to store all their clinical data in Elation while using Kareo side-by-side to manage their revenue.

**Important Information**: This guide reviews one of two configurations for the Elation-Kareo integration. This version of the integration is for customers who want to complete all front office workflows, such as intake and scheduling, in Elation and appointment information is not synchronized between Elation and Kareo. View the [Elation-Kareo Integration Guide- Using Kareo as the source of truth for insurance and appointments](Kareo-Integration-Guide-Using-Kareo-for-insurance-and-appointments.md) article if you wish to only enter insurance and appointments in Kareo.

## **How do I get started?**

You must first have an account with Kareo before you can use this integration. Once you have worked with Kareo to set up your account, you can request to turn on the Kareo integration by clicking **I need help** -> **Contact Elation Support**.

### **Mapping Providers**

Each Provider level user must have an account in both Elation and Kareo in order for Elation to be able to map patient data across the two systems. Please work with Elation and Kareo to make sure you have the correct accounts needed for the integration.

### **Mapping Practice Locations**

Each Practice Location in Elation must be mapped to a Service Location in Kareo in order for your [Bills](#bills) to push from Elation to Kareo. Follow these steps to map your Elation Practice Location to the corresponding Service Location in Kareo:

1. Sign in to your Elation account and click on your email address at the top of your account
2. Go to "Settings" >> "Practice Locations"
3. Click the "Edit" button next to the Practice Location you want to map
4. Select a *POS code* and *Kareo name* for the Practice Location
5. Click "Save"

Follow the instructions in [this article](https://helpme.kareo.com/01_Kareo_PM/04_Settings/Service_Locations/Service_Locations) if you need to create/add a Service Location in Kareo.

## **What information is synchronized?**

The following information is synchronized between Elation and Kareo for this version of the integration:

| | |
| --- | --- |
| **Data** | **Sync Direction** |
| Patient Charts | Elation ****↔**** Kareo |
| Demographics | Elation ****↔**** Kareo |
| Insurance | Elation ****↔**** Kareo |
| Appointments | Not synchronized |
| Bills | Elation ****→**** Kareo |

### **Patient Charts**

**Creating Charts**

Patient charts can be created in either system because Patient Demographics is bi-directional. Creating a patient chart in one system will also create the patient chart in the other system.

- **User Tip**: As best practice, we recommend creating Patient Charts in Kareo when possible because you will already be managing insurance information and appointments in Kareo. This will allow your front office staff to stay in one system (Kareo) for a majority of their work.

#### **Merging Charts**

Each chart can only have a one to one connection between Elation and Kareo and this connection is established upon chart creation. If you happen to see a duplicate chart for the same patient in either system, please make sure you find the chart that is connected between the two systems and keep the connected chart after performing a merge.

- For example, patient John Smith has one chart in Kareo but two charts in Elation. The best way to find out which of the two charts in Elation is connected to Kareo is by updating one of the connected demographics fields in Kareo to see which of the two charts in Elation receives the update. The chart that receives the update must be the chart that you keep in Elation when performing a chart merge.

Here are the proper merge steps for Elation charts:

1. Open the duplicate chart that is not connected to the integration
2. Click on the patient's name to open their Demographics
3. Click on the "Merge Chart" button
4. Find & select the chart you want to keep (the one that is connected to the integration)
5. Click "Merge Chart"
6. Confirm you understand the transfer of data and then click "Yes, merge charts"

#### **Deleting Charts**

Deleting a chart in Elation will not delete the chart in Kareo. Please take caution when deleting charts in Elation while using the Kareo integration as charts have a one to one connection via the integration. If the patient is still active in your practice, the deleted chart must be restored in order for the patient's information to sync properly across the two systems. Contact Elation using the "I need help" button if you need to restore a deleted chart.

### **Patient Demographics**

The synchronization of Patient Demographics is bi-directional. Any changes made in one system will be pushed to the other system. Creating a patient chart in one system will also create the patient chart in the other system. The following table shows a mapping of the Patient Demographics fields that are shared between Elation and Kareo and their matching field names. Fields that are not listed are not shared between Elation and Kareo.

| Elation Field Name | Kareo Field Name |
| --- | --- |
| Legal First Name | First name |
| Middle Name | M |
| Legal Last Name | Last name |
| Date of birth | DOB |
| Sex at Birth | Sex |
| Phone- *Home*, *Mobile* or *Work* type only (and up to 2 only) | Home Phone, Mobile Phone or Work Phone (depending on what is stored in Elation) |
| Email | Personal Email |
| Address | Address Line 1 |
| Ste or apt # | Address Line 2 |
| City | City |
| State | State/Province |
| Zip | Zip/Postal Code |
| Provider assigned in practice | Primary Provider |

### **Insurance**

The synchronization of insurance information is bidirectional between Elation and Kareo. Customers can enter insurance information in Elation or Kareo.

**Important Note**: Kareo uses a feature called an *Insurance* *Case* to store insurance policy information. Each period or type of insurance coverage in Kareo should be tied to its own *Insurance* *Case*. For example:

- If patient John Smith has medical coverage and separate insurance for an automobile accident, John Smith should have two *Insurance* *Cases* in Kareo, one *Insurance* *Case* for his personal medical insurance and the other *Insurance* *Case* for his automobile accident insurance. Make sure you set the primary *Insurance Case* as the the one you wish to share with Elation.
- If patient Jane Doe has Aetna® insurance from 1/1/2021 to 12/31/2021 and then changes to Blue Cross® beginning 1/1/2022 then Jane Doe should have two *Insurance* *Cases* in Kareo, one *Insurance* *Case* for Aetna that is marked as "Inactive" and one *Insurance* *Case* for Blue Cross that is the new primary, active *Insurance Case*.

The following table lists the insurance related fields that are pushed from Kareo to Elation and show how the Kareo fields map to the Elation fields. Fields that are not listed are not shared between Elation and Kareo:

| Kareo Field Name | Elation Field Name |
| --- | --- |
| Plan Name | Plan name |
| Company Name (\*hidden behind *Plan Name* in Kareo) | Insurance carrier name |
| Policy Number | Member ID |
| Group Number | Group ID |
| Copay Amount | Copay |
| Deductible Amount | Deductible |
| Relationship to Primary Policy Holder | Patient's relation to policyholder |
| Insured Name | First Name & Last Name |
| Street Address | Address |
| City | City |
| State | State |
| Zip | Zip |
| SSN | SSN |
| DOB | Date of birth |
| Gender | Sex at birth |

- **User Tip**: If you need to add a new Insurance Company or Plan to your Kareo database, follow the instructions in [this article](https://helpme.kareo.com/Platform/Practice_Settings/Insurance/Add_New_Insurance_Company).

#### **Carriers & Plans**

Insurance Carriers and plans details should be maintained in Kareo as Kareo can store more detailed information about Payers such as the Payer ID. It is most important for you to create Plans in Kareo (especially when it is for a Payer you already send claims to in Kareo) to avoid creating duplicate Payers in Kareo.

After the Carrier or Plan is created in Kareo and it is added to a patient's chart in Kareo, the Carrier and Plan will push over to Elation and you will be able to select them within Elation. If you need to add a new Insurance Company or Plan to your Kareo database, follow the instructions in [this article](https://helpme.kareo.com/Platform/Practice_Settings/Insurance/Add_New_Insurance_Companyhttp://).

- **User Tip**: The address for Carriers in Elation is pulled from the *Insurance Plan* setting of Kareo (and not the *Insurance Company* setting).

**Important Note**: You can create Carriers in Elation as well but you must remember to update the Insurance Company's *Electronic Claims* setting in Kareo in order to send claims electronically to the Payer. Never create Plans in Elation- this will cause duplication of Insurance Companies in Kareo.

#### **Adding insurance information**

For patients who do not have any active insurance information in Kareo, follow the appropriate steps below to add insurance to their chart in Kareo (which then pushes the insurance information over to Elation). Kareo allows you to store more detailed information about the insurance policies such as policy start and end dates.

| Kareo Web Browser Application | Kareo Windows PC Desktop Application |
| --- | --- |
| 1. Open the patient's chart in Kareo 2. Go to "Account" >> "Insurance" 3. Click"+ Add New Insurance Case" to add an *Insurance* *Case*    1. Fill out the *Payment Method*, *Name* and *Status* of the case. 4. Go to the *Policy #1: New Insurance* section and fill in the patient's primary insurance policy information.    1. Search for the appropriate *Insurance Plan* and select it from the database.       - If you need to add a new Insurance Company or Plan to your Kareo database, follow the instructions in [this article](https://helpme.kareo.com/Platform/Practice_Settings/Insurance/Add_New_Insurance_Company). 5. Click the "Save Policy" button once you have filled in all the information for the insurance policy you are adding 6. If the patient has secondary insurance coverage, click "+Add Another Policy" to add their Secondary Insurance information to the case. 7. Click "Save & Finish" at the very bottom of the page to save the case after you have added all the policies to the case | 1. Open the patient's chart in Kareo 2. Go to *Cases* 3. Click"Add..." to add a *Case*    1. Fill out the *Name,* check off the *Active?* box and select a *Payer Scenario* for the case. 4. Go to the *Insurance* section and click "Add" to add a new insurance policy to the*Case*    1. Search for the appropriate *Insurance Plan*, select it from the database and click "Ok" to proceed       - If you need to add a new Insurance Company or Plan to your Kareo database, follow the instructions in [this article](https://helpme.kareo.com/Platform/Practice_Settings/Insurance/Add_New_Insurance_Companyhttp://).    2. Fill out the *Policy #* and any other relevant fields needed for claims submission    3. Click "Save" to save the new insurance policy 5. If the patient has secondary insurance coverage, click "Add.." again to add their Secondary Insurance information to the case. 6. Click "Save" at the very bottom of the *New Case* window to save the case after you have added all the policies to the case 7. Click "Save" at the very bottom of the *Edit Patient* window to save your changes to the patient's chart |

**Important Note**: You can add insurance information for the first time for patients in Elation but we recommend performing updates and removals in Kareo to track historical insurance information and to track the policy end date.

#### **Correcting insurance information**

If policy information was entered incorrectly follow the steps below to make corrections as needed in Kareo (which then updates the insurance information in Elation):

| Kareo Web Browser Application | Kareo Windows PC Desktop Application |
| --- | --- |
| 1. Locate the patient's chart in Kareo 2. Go to "Account" >> "Insurance" 3. Click the "Edit" button next to the *Insurance* *Case* that is tied to the insurance policy 4. Click the "Edit" button next to the *Policy* you need to edit 5. Make the appropriate changes 6. Click "Save Policy" to save your changes to the policy information 7. Click "Save & Finish" to save your changes to the *Case* | 1. Locate the patient's chart in Kareo 2. Go to "Cases" 3. Select the *Case* with the policy that needs corrections 4. Click the "Edit..." button 5. Select the *Insurance Policy* that needs corrections 6. Click the "Edit..." button 7. Make the appropriate changes 8. Click "Save" to save your changes to the policy information 9. Click "Save" on the *Case* to save your changes to the *Case* 10. Click "Save" at the very bottom of the *Edit Patient* window to save your changes to the patient's chart |

**Important Note**: You can correct insurance information for patients in Elation via the [Patient Demographics](Patient-Demographics-Guide.md) but we recommend performing updates and removals in Kareo to track historical insurance information and to track the policy end date.

#### **Updating insurance information with new policy**

If all of the patient's policies within a given *Insurance Case* are no longer in effect, (ex. patient's old Primary & Secondary insurances changed), follow the steps listed below to mark the old policy as inactive and then add the new policies to the patient's chart. The new policy information will replace the old policy information in Elation. Use the [Update insurance information with new policy section](#update_insurance) if you are replacing an inactive insurance policy with an active one.

| Kareo Web Browser Application | Kareo Windows PC Desktop Application |
| --- | --- |
| 1. Locate the patient's chart in Kareo 2. Go to "Account" >> "Insurance" 3. Click the "Edit" button next to the *Insurance* *Case* that is tied to the insurance policy 4. Change the "Status" to "Inactive" & click "Save & Finish"    - **Important Note**: Making an *Insurance* *Case* inactive in Kareo will delete all of the Primary and Secondary insurance information in the Elation chart. Only make an *Insurance* *Case* inactive in Kareo if the insurance policies tied to the case are no longer in effect. 5. Follow the [Adding insurance information](#add_insurance) steps to add the new insurance policy information to the patient's chart in Kareo | 1. Locate the patient's chart in Kareo 2. Go to "Cases" 3. Select the *Case* that you want to mark as inactive 4. Click "Edit..." 5. Uncheck the *Active?* Box    - **Important Note**: Making a *Case* inactive in Kareo will delete all of the Primary and Secondary insurance information in the Elation chart. Only make a *Case* inactive in Kareo if the insurance policies tied to the case are no longer in effect. 6. Click "Save" to save you changes to the *Case* 7. Click "Save" at the very bottom of the *Edit Patient* window to save your changes to the patient's chart 8. Follow the [Adding insurance information](#add_insurance) steps to add the new insurance policy information to the patient's chart in Kareo |

**Important Note**: You can replace insurance policy information for patients in Elation via the [Patient Demographics](Patient-Demographics-Guide.md) but we recommend performing updates and removals in Kareo to track historical insurance information and to track the policy end date.

#### **Removing an inactive insurance policy from a list of policies**

If the patient has both a Primary and Secondary insurance policy and one of them are no longer in effect, you can remove the inactive policy from their chart (ex. patient's Secondary insurance is no longer in effect) by following the steps listed below. The inactive policy will be removed from Elation. Use the [Update insurance information with new policy section](#update_insurance) if you are replacing an inactive insurance policy with an active one.

| Kareo Web Browser Application | Kareo Windows PC Desktop Application |
| --- | --- |
| 1. Locate the patient's chart in Kareo 2. Go to "Account" >> "Insurance" 3. Click the "Edit" button next to the *Insurance* *Case* that is tied to the insurance policy 4. Click the "Edit" button next to the policy that is no longer in effect 5. Enter the policy end effective date in the *Policy End* field 6. Update the *Status* to "Inactive" 7. Click "Save Policy" to save your changes on the policy 8. Click "Save & Finish" to save your changes on the *Insurance Case*. | 1. Locate the patient's chart in Kareo 2. Go to "Cases" 3. Select the *Case* with the policy that is no longer in effect 4. Click the "Edit..." button 5. Select the *Insurance Policy* that is no longer in effect 6. Click the "Edit..." button 7. Enter the policy end effective date in the*Effective End* field 8. Uncheck the *Active?* box 9. Click "Save" to save your changes to the policy information 10. Click "Save" on the *Case* to save your changes to the *Case* 11. Click "Save" at the very bottom of the *Edit Patient* window to save your changes to the patient's chart |

**Important Note**: You can delete an inactive insurance policy in Elation via the [Patient Demographics](Patient-Demographics-Guide.md) but we recommend performing updates and removals in Kareo to track historical insurance information and to track the policy end date.

#### **Removing all inactive policies**

If all of the patient's policies within a give *Insurance Case* are no longer in effect, (ex. patient's Primary & Secondary insurances are no longer in effect), follow the steps listed below to mark the insurance case as inactive which removes the insurance information from the patient's chart in Elation. Use the [Update insurance information with new policy section](#update_insurance) if you are replacing an inactive insurance policy with an active one.

| Kareo Web Browser Application | Kareo Windows PC Desktop Application |
| --- | --- |
| 1. Locate the patient's chart in Kareo 2. Go to "Account" >> "Insurance" 3. Click the "Edit" button next to the *Insurance* *Case* that is tied to the insurance policy 4. Change the "Status" to "Inactive" & click "Save & Finish"    - **Important Note**: Making an *Insurance* *Case* inactive in Kareo will delete all of the Primary and Secondary insurance information in the Elation chart. Only make an *Insurance* *Case* inactive in Kareo if the insurance policies tied to the case are no longer in effect. | 1. Locate the patient's chart in Kareo 2. Go to "Cases" 3. Select the *Case* with the policy that is no longer in effect 4. Click the "Edit..." button 5. Uncheck the *Active?* box    - **Important Note**: Making a *Case* inactive in Kareo will delete all of the Primary and Secondary insurance information in the Elation chart. Only make a *Case* inactive in Kareo if the insurance policies tied to the case are no longer in effect. 6. Click "Save" on the *Case* to save your changes to the *Case* 7. Click "Save" at the very bottom of the *Edit Patient* window to save your changes to the patient's chart |

**Important Note**: You can delete all inactive insurance policies in Elation via the [Patient Demographics](Patient-Demographics-Guide.md) but we recommend performing updates and removals in Kareo to track historical insurance information and to track the policy end date.

### **Appointments**

Patient appointments do not synchronize between Elation and Kareo. Track patient appointments in Elation to ensure providers have visibility into their schedule.

### **Bills**

The synchronization of bills is uni-directional from Elation to Kareo. Once a provider signs a visit note in Elation, the billing information in the visit note will be pushed to Kareo as a *Charge*. The following table lists the fields that are pushed from Elation & Kareo and show how the Kareo fields map to the Elation fields.

| Elation Field Name | Kareo Field Name |
| --- | --- |
| CPT | Procedure Code |
| Modifier | Mod |
| Charge | Charge |
| Qty | Units |
| Dx | Diagnosis |
| Service Location (POS) | Service Location & Place of Service |
| Additional Billing Notes | Notes |

**Important Notes**:

- Kareo will only ingest the first 12 diagnosis codes (ICD-10 codes) entered in Elation. If different ICD-10 codes were used for different service lines, Kareo will ingest up to 4 ICD-10s per service line and then ingest the remainder of the ICD-10 codes (but only up to 12 total)
- Procedure Codes, ICD-10 codes and Modifiers used in Elation must be in the Kareo database in order for Kareo to accept the charges. You will see a Bill Error if the code you added is not in Kareo. Reference the following articles if you need to add additional codes to your Kareo database:
 - [Add CPT/Procedure code](https://helpme.kareo.com/01_Kareo_PM/05_Codes/02_Procedure_Codes/Procedure_Codes)
 - [Add Diagnosis code](https://helpme.kareo.com/01_Kareo_PM/05_Codes/06_Diagnosis_Codes/Diagnosis_Codes)
 - [Add Modifier](https://helpme.kareo.com/01_Kareo_PM/05_Codes/03_Procedure_Modifier_Codes/Procedure_Modifier_Codes)

##

## **Getting Support**

#### **Kareo**

If you need assistance with your Kareo configuration or have questions about the Kareo Windows PC Desktop Application or Web Browser Application, contact Kareo here: <https://helpme.kareo.com/Contact_Us>

#### **Elation**

If you need assistance with Elation or the Elation-Kareo integration, contact Elation using the **I need help** -> **Contact Elation Support** button at the top of your Elation account.

## **Frequently Asked Questions (FAQ)**

#### **How long does it take information to synchronize between the two systems?**

Information between Elation and Kareo usually synchronizes within a few seconds but can take up to 5 minutes depending on how busy the servers are.

#### **I created a patient chart in one system but the patient chart did not surface in the other system. What should I do?**

We recommend making an update to the demographics in the system you originally created the chart in to trigger another connection between the two systems.

If you are using the Kareo Windows PC Desktop Application, make sure you click the "Save" button at the bottom of the *Edit Patient* window after making any changes to the patient's Kareo chart (demographics, cases or insurance) to save the changes and push the changes to Elation.

If you continue to run into synchronization issues, use the **I need help** -> **Contact Elation Support** button at the top of your Elation account to reach our Support Team for further assistance.

#### **I see duplicate charts for a patient. What should I do?**

Review the [Merging Charts](#merge_chart) section of this article to understand how to correct for duplicate charts issues.

#### **I updated/added demographics information to a patient's chart but the information did not synchronize between Elation and Kareo. What should I do?**

We recommend making an update to the demographics again in the system you originally made edits in to trigger another connection between the two systems. If you are using the Kareo Windows PC Desktop Application, make sure you click the "Save" button at the bottom of the *Edit Patient* window after making any changes to the patient's Kareo chart (demographics, cases or insurance) to save the changes and push the changes to Elation.

If you continue to run into synchronization issues, use the **I need help** -> **Contact Elation Support** button at the top of your Elation account to reach our Support Team for further assistance.

#### **Can I update billing information in Elation after sending it to Kareo?**

The default behavior is that billing information is sent to Kareo after a provider signs the corresponding visit note in Elation. Once billing information is sent to Kareo, you must make updates manually in both Elation and Kareo. Changes or updates in Elation will not automatically be pushed to Kareo.

If you prefer to have extra time to review and update billing information after signing the visit note, you can use the *Delayed Billing* feature to hold bills in Elation and manually send them to Kareo once the billing information is complete. Learn more about the *Delayed Billing* feature in this [Billing Guide- Delayed Billing](How-to-set-up-Delayed-Billing.md).

#### **I received a "Bill Error" after trying to send charge details from Elation to Kareo. Why?**

There are a few common reasons why you may receive a "Bill Error" after attempting to send a charge from Elation to Kareo:

- There are missing CPT Codes or ICD-10 codes on service lines
- There are invalid CPT Codes, ICD-10 codes or Modifiers on service lines
- The CPT Codes, ICD-10 codes or Modifiers you added to Elation is not in your Kareo database. Reference the following articles if you need to add additional codes to your Kareo database:
 - [Add CPT/Procedure code](https://helpme.kareo.com/01_Kareo_PM/05_Codes/02_Procedure_Codes/Procedure_Codes)
 - [Add Diagnosis code](https://helpme.kareo.com/01_Kareo_PM/05_Codes/06_Diagnosis_Codes/Diagnosis_Codes)
 - [Add Modifier](https://helpme.kareo.com/01_Kareo_PM/05_Codes/03_Procedure_Modifier_Codes/Procedure_Modifier_Codes)
- You selected a Practice Location that is not mapped to a Kareo Service Location. Follow the instructions in the [Map Practice Locations section](#map_locations) to map your practice locations.

To bills with errors, you can click the "Edit Bill" button to edit the billing information and then click "Save & Re-send" to attempt to send the charges to Kareo again. If you continue to run into errors after troubleshooting, use the **I need help** -> **Contact Elation Support** button at the top of your Elation account to reach our Support Team for further assistance.

#### **I am unable to find a Carrier or Plan in Elation but I see it in Kareo. What should I do?**

New Carriers and Plans created in Kareo or Elation must be tied to a patient in order for the Carrier or Plan to synchronize between the two systems. If you added a new Insurance Company or Insurance Plan in Kareo, add it to the proper patient account in Kareo and then you will see the Carrier or Plan in your Elation database.


*Kareo © 2022 All Rights Reserved* *©2022 Aetna Inc**All Rights Reserved* © 2022 Blue Cross Blue Shield Association. All Rights Reserved.

## **Related Articles**

- [Patient Demographics Guide](Patient-Demographics-Guide.md)
- [Patient Demographics Guide- Managing patient insurance](Managing-Insurance.md)
- [Billing Guide- Creating a Super Bill and coding for your visit](billing.md)
- [Billing Guide- Setting up CPT Codes and Place of Service](billing-settings---service-locations--procedure-codes.md)
- [Billing Guide- Delayed Billing](How-to-set-up-Delayed-Billing.md)