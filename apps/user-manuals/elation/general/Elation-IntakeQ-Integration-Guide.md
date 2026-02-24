# Elation-IntakeQ Integration Guide

Source: https://help.elationhealth.com/s/article/Elation-IntakeQ-Integration-Guide

---

This article describes the Elation-IntakeQ integration for electronic intake forms.

# **Contents**

- [Overview](#overview)
 - [What is IntakeQ?](#intakeQ_info)
 - [What is the Elation-IntakeQ Integration?](#integration_introduction)
 - [How do I get started?](#getting_started)
 - [What information is shared between Elation and IntakeQ?](#shared_information)
    - [Patient demographics](#demographics_sync)
- [Workflow Instructions](#workflows)
 - [Mapping Providers](#map_providers)
 - [Specifying integration settings in IntakeQ](#IntakeQ_sync_settings)
 - [Linking patient charts](#link_charts)
    - [Automatically creating charts in Elation from completed IntakeQ forms](#create_charts_from_IntakeQ_forms)
    - [Syncing Elation patients to IntakeQ](#sync_Elation_patients)
 - [Updating demographics](#update_demographics)
    - [Updating demographics after forms were completed](#updating_demographics_after_forms_complete)
 - [Managing IntakeQ Forms](#managing_forms)
    - [Managing IntakeQ Form Options](#form_options)
    - [Automatically sending completed IntakeQ forms to Elation](#share_completed_forms)
    - [Preventing specific IntakeQ Forms from syncing to Elation](#prevent_sync_specific_forms)

# **Overview**

## **What is IntakeQ?**

IntakeQ is a HIPAA-compliant online intake forms software. Practices can create electronic intake forms for patients to complete anywhere and at any time. Analytical data is also available to help practices monitor operations and performance.


## **What is the Elation-IntakeQ Integration?**

The Elation-IntakeQ integration syncs completed IntakeQ forms with Elation and uses the collected demographic information to create or update patient charts. IntakeQ can also retrieve a patient's contact details from Elation to send intake forms.


## **How do I get started?**

[Contact Elation](https://app.elationemr.com/support/) to request this integration and a member of our Implementation Team will reach out with next steps.

- IntakeQ is a paid software and you must [subscribe](https://intakeq.com/pricing?r=aw_bbc_sitelink&utm_term=intakeq&utm_campaign=IntakeQ_BrandSearch&utm_source=ppc&utm_medium=google_ads&hsa_acc=6542293186&hsa_cam=18538221264&hsa_grp=140614257965&hsa_ad=633227122212&hsa_src=g&hsa_tgt=kwd-372151297908&hsa_kw=intakeq&hsa_mt=e&hsa_net=adwords&hsa_ver=3&gad_source=1&gclid=CjwKCAjwl6-3BhBWEiwApN6_klDTIkUw80HC3CZxzcXYfR-QkmxU94GMhse4WnUospv4O-7ABwWWohoCDC4QAvD_BwE) to their services in order to use them.

## **What information is shared between Elation and IntakeQ?**

The following information is shared between Elation and IntakeQ:

| Elation | | IntakeQ | Notes |
| --- | --- | --- | --- |
| Chart Creation | ↔ | Client (Patient) Creation | For charts to be created in Elation, at least one form completed by the patient in IntakeQ must include the patient's First Name, Last Name, Date of Birth and Sex at birth. |
| Demographics Updates | ↔ | Contact Information Updates | Elation is the source of truth for patient demographics.    \* Demographic information from IntakeQ will only be sent to Elation based on answers submitted through IntakeQ forms. Demographics information stored in the IntakeQ profile **IS NOT** shared with Elation. |
| Report | ← | Completed Form | When a patient submits an intake package via IntakeQ, the forms are automatically uploaded as PDFs to the patient's chart in Elation. |

### **Patient demographics**

The synchronization of Patient Demographics is bi-directional. Any changes made in Elation will be pushed to IntakeQ. Demographic information from IntakeQ will only be sent to Elation based on answers submitted through IntakeQ forms. **Demographics information stored in the IntakeQ profile IS NOT synced to Elation.**

The following table shows a mapping of the Patient Demographics fields that are shared between Elation and IntakeQ Forms and their matching field names. The fields with an asterisk ( \* ) are required by Elation.

- **User Tip**: As best practice, we recommend managing demographics in Elation as various other features and integrations depend on accurate demographics in Elation.

| Elation Field Name | IntakeQ Form Field Name |
| --- | --- |
| Legal first name\* | First Name |
| Legal last name\* | Last Name |
| Middle Name | Middle Initial |
| Date of birth\* | Date of Birth |
| Sex at birth\* | Gender |
| Address | Address |
| Mobile Phone | Mobile Phone |
| Home Phone | Home Phone |
| Work Phone | Work Phone |
| Email | Email Address |
| Preferred contact method | Preferred contact method |
| Primary Insurance carrier name\* | Primary Insurance Company |
| Primary Insurance Plan name\* | Primary Insurance Plan |
| Primary Insurance Group ID | Group Number |
| Primary Insurance Member ID | Member ID / Policy # |
| Primary Insurance Policyholder - Patient's relation to policyholder | Client Relationship to Insured |
| Primary Insurance Policyholder - First name | Insured First Name |
| Primary Insurance Policyholder - Last name | Insured Last Name |
| Primary Insurance Policyholder - Date of birth | Insured Date of Birth |
| Primary Insurance Policyholder - Sex at birth | Insured Gender |
| Primary Insurance Policyholder - Address | Insured Street Address |
| Primary Insurance Policyholder - City | Insured City |
| Primary Insurance Policyholder - State | Insured State |
| Primary Insurance Policyholder - Zip | Zip Code |

**Important Note**: For patient's insurance details to sync from IntakeQ to Elation, you must have an IntakeQ Form with the primary insurance fields listed above. For required fields (marked with an asterisk), mark off the 'Is Required' checkbox for those fields in your form. IntakeQ will sync your list of Insurance Carriers from Elation and the intake form will show a dropdown list of all insurance carriers you have in Elation for the patient to select from.





# **Workflow Instructions**

## **Mapping Providers**

To map Provider Level Users in Elation with Practitioner accounts in IntakeQ:

1. Click on the "MORE" button at the top right corner of your IntakeQ account
2. Click "Settings"
3. Click "Integrations"
4. Click "Elation Health Integration"
5. Select the corresponding Elation Provider for each IntakeQ Practitioner under **Practitioner Mapping**.

## **Specifying integration settings in IntakeQ**

IntakeQ offers a few Settings you can configure for the Elation-IntakeQ integration. To configure these Settings in IntakeQ:

1. Click on the "MORE" button at the top right corner of your IntakeQ account
2. Click "Settings"
3. Click "Integrations"
4. Click "Elation Health Integration"
5. Configure any of the following settings as needed (checking the box enables the corresponding Setting):

| Setting | Enabled Behavior | Disabled Behavior |
| --- | --- | --- |
| Split intake packages into multiple files | Each intake form will be its own Report PDF in Elation. | Each intake package (which can consist of multiple forms) will be a single Report PDF in Elation. |
| Allow IntakeQ to update patient demographics | Allow demographic information from completed IntakeQ forms to populate or update demographic details in Elation. | The Elation-IntakeQ integration will never populate or update demographics details in Elation. |
| Prevent IntakeQ from creating new patients in the EHR | Prevent the Elation-IntakeQ integration from creating new charts in Elation. | Allow the Elation-IntakeQ integration to create new charts in Elation. |
| Upload forms after practitioner signs it | Only push completed forms to Elation after a Practitioner signs the form in IntakeQ. | Push completed forms to Elation after the patient submits the form. |
| Allow IntakeQ to sync patient insurance information in the EHR | Allow insurance information from completed IntakeQ forms to populate or update insurance details in Elation. | The Elation-IntakeQ integration will never populate or update insurance details in Elation. |




## **Linking patient charts**

### **Automatically creating charts in Elation from completed IntakeQ forms**

When a patient submits an intake package via IntakeQ, the forms are automatically uploaded as PDFs to the patient chart in Elation. If the patient does not have a chart in Elation yet, IntakeQ will create a patient chart in Elation using demographics information from the completed form(s). By default, for a chart to be created in Elation, at least one form completed by the patient in IntakeQ must include the patient's First Name, Last Name, Date of Birth, and Sex at Birth.

**Important Note**: The functionality that allows IntakeQ to create charts in Elation is a [Setting in IntakeQ](#IntakeQ_sync_settings). If this Setting is disabled then the Elation-IntakeQ integration will never create charts in Elation.




### **Syncing Elation patients to IntakeQ**

Any patient chart in Elation will be automatically visible in IntakeQ when searching for a Client (Patient) to send them forms. Simply type the patient's name in the **Name** field and select them from the search results.
![]()


## **Updating demographics**

When a patient submits an intake package via IntakeQ, the forms are automatically uploaded as PDFs to the patient chart in Elation. If the completed forms contain demographic information for [synchronized fields](#demographics_sync), that data will be used to populate or update the demographic details in Elation.

- **Important Notes**:
 - The functionality that allows IntakeQ to populate/update demographic information in Elation is a [Setting in IntakeQ](#IntakeQ_sync_settings). If this Setting is disabled then the Elation-IntakeQ integration will never populate/update demographic information in Elation.
 - Demographics information stored in a patient's IntakeQ profile **IS NOT** synced to Elation.

IntakeQ will also pull contact information such as Email or Phone from Elation to send intake forms to patients.


### **Updating demographics after forms were completed**

By default, demographic information from IntakeQ will only be sent to Elation based on answers submitted through IntakeQ forms. If a patient submitted wrong or incomplete demographics information, you can use one of the following workflows to update that patient's demographics information:

1. Resend the IntakeQ Form to the patient to fix or update the information. After the form is resubmitted, IntakeQ will sync the new information to Elation.
2. Manually update the information in the patient's demographics in Elation.




## **Managing IntakeQ Forms**

### **Managing IntakeQ Form Options**

There are two form options that can be configured for each IntakeQ:

- Elation Report Category
 - By default, all completed IntakeQ Forms are pushed to Elation as an 'Intake' Report category.
 - To select a different [Report Category](report-types.md) for a specific IntakeQ Form:
    1. Click "Open Form Options".
    2. Select a category for the Form Name.
    3. Click "Save" to save your changes.
- Disable Sync
 - By default, all completed IntakeQ Forms are pushed to Elation.
 - To disabled the sync for a specific IntakeQ Form:
    1. Click "Open Form Options".
    2. Check the "Disable Sync" box next to the name of the form you do not want to sync to Elation.
    3. Click "Save" to save your changes.

### **Automatically sending completed IntakeQ forms to Elation**

When a patient submits an intake package via IntakeQ, the forms are automatically uploaded as PDFs to the patient chart in Elation. The Provider assigned to the completed IntakeQ Forms will see the forms in the Requiring Action section of the patient's chart for sign off.


### **Preventing specific IntakeQ Forms from syncing to Elation**

By default, all completed IntakeQ Forms are pushed to Elation. To disabled the sync for a specific IntakeQ Form:

1. Click "Open Form Options".
2. Check the "Disable Sync" box next to the name of the form you do not want to sync to Elation.
3. Click "Save" to save your changes.

# **Related Articles**

- [Patient Demographics Guide](https://help.elationemr.com/s/article/Patient-Demographics-Guide)
- [Report Category Guide- Categorizing patient documents](https://help.elationemr.com/s/article/report-types)
- [IntakeQ's Guide to the EIation-IntakeQ Integration](https://support.intakeq.com/article/432-elation-ehr)
- [IntakeQ's Insurance Information Sync Guide](https://support.intakeq.com/article/475-elation-ehr-insurance-information-sync)