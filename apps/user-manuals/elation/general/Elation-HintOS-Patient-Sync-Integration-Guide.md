# Elation-HintOS Patient-Sync Integration Guide

Source: https://help.elationhealth.com/s/article/Elation-HintOS-Patient-Sync-Integration-Guide

---

## **Contents**

- [What is the Elation-HintOS Patient-Sync Integration?](#WhatIsIt)
- [Why is the integration valuable?](#WhyIsItValuable)
- [How can I start using the integration?](#HowToIntegrate)
- [What information is shared between Elation & HintOS?](#InformationSync)
 - [New Charts](#NewCharts)
 - [Demographics](#Demographics)
 - [Insurance](#Insurance)
 - [Memberships](#Memberships)
- [How to use the integration](#HowToUseIntegration)
 - [Patient Self-Registers in HintOS](#PatientSelfRegisterInHintOS)
 - [Practice Enrolls Patients](#PracticeEnrollsPatients)
- [How to merge duplicate charts](#MergeCharts)

###

## **What is the Elation-HintOS Patient-Sync Integration?**

If you are an Elation EHR customer who also uses [HintOS©](https://support.hint.com/en/articles/5708819-elation-patient-sync) then this integration is ideal for you. The Elation-HintOS Patient-Sync Integration allows you to synchronize patient demographic information, and keep changes up to date, in either system. Any chart that is created in HintOS will automatically be created in Elation EHR and vice versa. If a chart already exists in the other system, the system will try to match the charts using the patient's first name, last name, date of birth, sex and other demographics information before creating a new chart.

## **Why is this integration valuable?**


The interface between Elation and HintOS allows you to use Elation for clinical documentation while still being able to efficiently manage your patients' memberships using HintOS. The bi-directional synchronization capabilities amongst the demographics fields allows for streamlined workflows in both systems. You can continue to view which memberships your patients are subscribed to in HintOS directly in their Elation chart.


## **How can I start using this integration?**

To begin using this integration, [click here to tell the Elation you are interested](https://help.elationemr.com/s/contactsupport). Elation's Implementation Team will work with you to get you connected and link the providers between Elation and HintOS.



## **What information is shared between Elation & HintOS?**

### **New Charts**

There are two ways to create patient charts. If you create a chart in HintOS, make sure you assign the patient to an Elation [linked provider in HintOS](https://support.hint.com/en/articles/5718673-how-to-create-a-provider) to push the new chart to Elation.

1. Patients can be registered in HintOS and the new patient will be matched to an existing patient or created as a new patient in Elation.
2. Patients can be registered in Elation and the new patient will be matched to an existing patient or created as a new patient in HintOS

You can review a patient's sync status in the "Integrations" section at the bottom of the patient's details in HintOS.

**User Tips**:

- If you do not want a patient in HintOS to sync to Elation, do not assign them to an Elation linked provider.
- The integration uses first name, last name, date of birth, sex, and other demographic information to determine matches between the systems.
- If there are duplicates created by this process refer to the section on [merging charts](#MergeCharts) for more information.
- If you only want new charts created in HintOS to be pushed to Elation but not Elation > HintOS, turn off "Create Patients From Elation" in the [HintOS Integrations page](https://app.hint.com/admin/elationv2).

### **Demographics**

The chart below describes how demographics fields map to each other between Elation and Hint.

- **User Tip**: Take caution when changing the patient’s phone number in HintOS and make sure the change maps to the correct phone type in Elation; especially the “Mobile” number. The "Mobile" phone type in Elation can be tied to features like the Patient Passport Invitation Code, Appointment Reminders and Virtual Visit instructions.

![]()




### **Insurance**

Insurance synchronization will only occur when HintOS creates a chart in Elation for a new patient. Once a patient has a chart in Elation, **updates to insurance information must be made in both systems**. We recommend keeping insurance information up-to-date in Elation because insurance information is used for other features.

Only the following fields sync from HintOS to Elation when charts are created in HintOS:

![]()




### **Memberships**

Maintain the patient membership information in HintOS. Membership details will appear as Patient Tags in the Elation patient chart.  Any edits made to the below patient membership information in HintOS will update Patient Tags in Elation. The Patient Tags in Elation should be considered as “read-only” and any modifications made in Elation will not appear in or sync to HintOS.

![]()

**User Tips**:

- The *Membership*, *Employer*, *Plan* and *Patient’s Balance* tags will not appear if a patient is archived.
- < > indicates information will populate based on what is indicated in HintOS. (Ex. If membership status says inactive in HintOS, the Patient Tag in Elation will say “Inactive Membership”)



## **How to use the Integration**

### **Patient Self-Registers in HintOS**

This workflow is optimal if you would like memberships and insurance information for new patients synchronized in both Elation and HintOS.

1. Patients self-registers in HintOS and patient information is collected during this enrollment. If HintOS creates a new chart for patient in Elation, the Elation chart will include insurance information if it is available. If a chart already exists in Elation, insurance information will not be synced.
   - Edit patient demographics in either Elation or HintOS.
   - Maintain and edit insurance information in Elation
2. Maintain the patient’s membership information in HintOS. The Patient Tags in the Elation patient chart will update based on the patient’s membership information in HintOS.

### **Practice Enrolls Patients**

This workflow is ideal if patients only have memberships in HintOS and you do not need insurance information saved in HintOS.

1. Create new patient chart in Elation or HintOS. Any new patient charts created in one system will trigger a chart to be created in the other system.
   - Edit patient demographics in Elation or HintOS.
   - Maintain and edit insurance information in Elation.
2. Maintain the patient’s membership information in HintOS. The Patient Tags in the Elation patient chart will update based on the patient’s membership information in HintOS.

## **How to merge duplicate charts**

Deleting or merging patients in either system will not synchronize. The deletion or merge needs to be completed in both systems.

First, in Elation:

1. Go to the "losing" duplicate patient chart you would like to remove.
2. Click on the patient's name to edit patient details and click the "Merge Chart" button at the bottom right-hand corner.
3. Enter the name of the "winning" chart you would like to keep and click "Merge Chart". Everything except for the demographics and "losing" HintOS ID will be merged into the "winning" chart.

Second, in HintOS:

1. Go to the "losing" or inactive patient chart you would like to remove.
2. Click "Edit Patient" and click "Merge".
3. Select which fields you would like to keep on the "winning" chart. You will have the option to choose the winning Elation ID as part of this flow. To successfully complete the chart merge, the Elation ID chosen here needs to belong to the "winning" chart in Elation.
4. Click "Merge"

*© Copyright 2023 Hint Health Inc.*

## **Additional Resources**

- [HintOS Guide for Patient Sync Integration](https://support.hint.com/en/articles/5708819-elation-patient-sync)
- [HintOS Guide for Integration Set Up](https://support.hint.com/en/articles/5708873-migrating-to-elation-health-patient-sync-v2)