# Telehealth Guide- Setting up your integrated practice management system for telehealth

Source: https://help.elationhealth.com/s/article/Setting-up-your-Elation-account-for-telehealth

---

## **Contents**

- [Why is it important to configure telehealth billing for Elation & my PMS?](#value)
- [General information](#general_info)
- [General Elation instructions](#general)
 - [Adjusting the Place of Service (POS) in Elation](#Elation_POS)
 - [Adjusting CPT Codes in Elation](#Elation_CPT)
- [Kareo](#Kareo)
- [Akamai](#Akamai)
- [CollaborateMD](#CollaborateMD)
- [PracticeSuite](#PracticeSuite)
- [ConnxtMD](#ConnxtMD)
- [AdvancedMD](#AdvancedMD)

## **Why is it important to configure telehealth billing for Elation & my PMS?**

Teleheath workflows and coding allows providers to care for patients and get paid for their work during the COVID-19 public health emergency. This article also applies to providers who normally offer telehealth services. If you are using an integrated practice management/billing system (PMS) alongside Elation, you will want to make sure Elation and your PMS are set up to allow you to successfully get paid for telehealth services rendered in a streamlined fashion.

Our team has created this resource to guide you through the necessary settings updates to bill for telehealth services rendered to patients. Each section linked below provides detailed step-by-step instructions to ensure that your practice can successfully send telehealth charges from Elation to your integrated practice management/billing system (PMS).

The instructions on Elation's end will always remain the same for any PMS and can be seen in the [general Elation instructions](#general) section. Please click on the link below to view instructions relevant to your PMS if you need to make any adjustments in your PMS:

- [Kareo](#Kareo)
- [Akamai](#Akamai)
- [CollaborateMD](#CollaborateMD)
- [PracticeSuite](#PracticeSuite)
- [ConnxtMD](#ConnxtMD)
- [AdvancedMD](#AdvancedMD)



## **General information**

Telehealth coding regulations can change from time to time and may be different for each payer. For tips on which Place of Service (POS) and CPT Codes to use for telehealth, see our [Telehealth Billing Workflow](Telehealth-Coding-and-Workflows-Recommendations.md) guide. We recommend consulting with your payer's coding guidelines for the most up to date information.



## **General Elation instructions**

These instructions apply to any Elation customer using any integrated practice management/billing system (PMS) with Elation. For tips on which Place of Service (POS) and CPT Codes to use for telehealth, see our [Telehealth Billing Workflow](Telehealth-Coding-and-Workflows-Recommendations.md) guide.

### **Adjusting the Place of Service (POS) in Elation**

1. In Elation, go to "Settings" >> "Practice Location"
2. Click "+ Add Practice Location" to add a new location where you would like to bill from
3. Fill out the information for the new service location including the relevant POS code. For example, for *Telehealth*, that code is (02).
4. Click "Save" to save your new Practice Location in Elation
5. Look at the relevant practice management/billing system (PMS) instructions below to create a corresponding Practice Location in your PMS.


**User Tip**: If you are providing in person and telehealth services from your office, you can have the same Practice Location but different Place of Service codes to designate the type of service being rendered.


### **Adjusting CPT Codes in Elation**

1. In Elation, go to "Settings" >> "Billing"
2. Click "+Add CPT code"
3. Enter the desired telehealth related CPT codes and corresponding descriptions
   - User Tip: Popular telehealth codes can be found here: [Telehealth Billing Workflow](Telehealth-Coding-and-Workflows-Recommendations.md)
4. Click "Create"
5. Look at the relevant practice management/billing system (PMS) instructions below to create a corresponding CPT Code in your PMS as needed.

## **Kareo**

These instructions can be used alongside the [general instructions](#general) above for any customer using the Elation-Kareo integration. For tips on which Place of Service (POS) and CPT Codes to use for telehealth, see our [Telehealth Billing Workflow](Telehealth-Coding-and-Workflows-Recommendations.md) guide.


### **Kareo- Adjusting the Place of Service (POS)**

Navigate to Kareo's "Setup" page and add a service location for “telehealth - (02)”

### **Kareo- Adjusting CPT® Codes**

1. Click "Settings" >> "Codes" >> "Find Procedures" on the top menu.
   - **User Tip**: To avoid duplication, best practice is to first search the database to see if the procedure code already exists in the system
2. If the procedure code is not in the system, click "New" at the bottom
3. Enter the required information.
4. When finished, click "Save"
5. Log out of Kareo and log back in to utilize the new code

### **Elation- Important Place of Service (POS) steps**

After following the [general instructions](#Elation_POS) above, you must select the matching Kareo service location name from the drop down menu for any matching Elation Service Location under "Settings" >> "Practice Location".

### **Elation- Important CPT Code information**

If you are adding CPT Codes in Elation using the [general instructions](#Elation_CPT) above, please be sure that the CPT code you add to Elation matches exactly to the CPT code in Kareo. Without an exact match, the bills containing the CPT code will fail.

## **Akamai**

These instructions can be used alongside the [general instructions](#general) above for any customer using the Elation-Akamai integration. For tips on which Place of Service (POS) and CPT Codes to use for telehealth, see our [Telehealth Billing Workflow](Telehealth-Coding-and-Workflows-Recommendations.md) guide.

### **Akamai- Adjusting the Place of Service (POS) & CPT Codes**

Navigate to the Akamai "Settings" page and add the service location and CPT codes there.

- Please note that the service location name must match exactly to what is listed as the Practice Location name in Elation
- Please do not hesitate to contact Akamai Support ([support@akamaipm.com](mailto:support@akamaipm.com)) for assistance with updating the billing codes and/or service location.

### **Elation- Important Place of Service (POS) and CPT Code steps**

Please be sure that the CPT codes and service location that you add to Akamai match exactly to the service location and CPT codes in Elation. Without an exact match, the corresponding bills will fail.

## **CollaborateMD**

These instructions can be used alongside the [general instructions](#general) above for any customer using the Elation-CollaborateMD integration. For tips on which Place of Service (POS) and CPT Codes to use for telehealth, see our [Telehealth Billing Workflow](Telehealth-Coding-and-Workflows-Recommendations.md) guide.

##

### **CollaborateMD- Adjusting the Place of Service (POS)**

1. In CollaborateMD, go to "Customer Setup" >> "Facilities"
2. Click "+New Facility" >> "Add Manually"
   - You can also choose "Add via NPI Registry" if you want to add your service location using a unique NPI number
3. Fill in the all of the details and most importantly enter a "Place of Service" under *Claim Defaults*
   - For tips on which Place of Service (POS) to use for telehealth, see our [Telehealth Billing Workflow](Telehealth-Coding-and-Workflows-Recommendations.md) guide.
4. Click "Save" to save the new Facility

### **CollaborateMD- Adjusting CPT® Codes**

1. In CollaborateMD, go to "Customer Setup" >> "Codes..." >> "Procedure"
2. Click "+ New CPT/HCPCS"
3. Enter the code, description and other required fields
   - For tips on which CPT Codes to use for telehealth, see our [Telehealth Billing Workflow](Telehealth-Coding-and-Workflows-Recommendations.md) guide.
4. Click "Save" to save the new Procedure Code.

### **Elation- Important Place of Service (POS) and CPT Code steps**

Please be sure that the CPT codes that you add to Elation match exactly to the Procedure codes in CollaborateMD. Please also make sure the Practice Location you add to Elation matches the Facility you add to CollaborateMD. Without an exact match, the corresponding bills will fail.

## **PracticeSuite**

These instructions can be used alongside the [general instructions](#general) above for any customer using the Elation-PracticeSuite integration. For tips on which Place of Service (POS) and CPT Codes to use for telehealth, see our [Telehealth Billing Workflow](Telehealth-Coding-and-Workflows-Recommendations.md) guide.

##

### **PracticeSuite- Adjusting the Place of Service (POS)**

1. In PracticeSuite, go to "Master Setup" >> "Service Location"
2. Click "+ Add Service Location"
3. Fill in the all of the details and most importantly enter a Place of Service Code in the "POS" field
   - For tips on which Place of Service (POS) to use for telehealth, see our [Telehealth Billing Workflow](Telehealth-Coding-and-Workflows-Recommendations.md) guide.
4. Click "Save" to save the new Service Location

### **PracticeSuite- Adjusting CPT® Codes**

1. In PracticeSuite, go to "Billing Setup" >> "Fee Schedule"
2. Click "+Add CPT"
3. Enter the code, description and other required fields. Make sure you keep the "Active" checkbox checked.
   - *​​​​​​​​​​​​​​*For tips on which CPT Codes to use for telehealth, see our [Telehealth Billing Workflow](Telehealth-Coding-and-Workflows-Recommendations.md) guide.
4. Click "Save" to save the new CPT Code

### **Elation- Important Place of Service (POS) and CPT Code steps**

Please be sure that the CPT codes that you add to Elation match exactly to the CPT codes in PracticeSuite. Please also make sure the Practice Location you add to Elation matches the Service Location you add to PracticeSuite. Without an exact match, the corresponding bills will fail.

## **ConnxtMD**

These instructions can be used alongside the [general instructions](#general) above for any customer using the Elation-ConnxtMD integration. For tips on which Place of Service (POS) and CPT Codes to use for telehealth, see our [Telehealth Billing Workflow](Telehealth-Coding-and-Workflows-Recommendations.md) guide.

### **ConnxtMD- Adjusting the Place of Service (POS) & CPT Codes**

1. In ConnxtMD, go to the "Practice Setup" page
2. Add CPT Codes and charge amounts to the Fee Schedule
3. Add a new Facility for teleheath if needed

**Important Note**: Schedule appointments in ConnxtMD using the *Telehealth* facility. The interface links Elation charges to existing ConnxtMD appointments resulting in charges that use the appointment’s chosen facility.

### **Elation- Important Place of Service (POS) and CPT Code steps**

Please be sure that the CPT codes that you add to Elation match exactly to the CPT codes in PracticeSuite. Please also make sure the Practice Location you add to Elation matches the Service Location you add to PracticeSuite. Without an exact match, the corresponding bills will fail.

## **AdvancedMD**

##

### **AdvancedMD- Adjusting the Place of Service (POS)**

1. In AdvancedMD, go to "System Settings" >> "Facilities"
2. Do not click on any existing Facility to the left, just enter the data for the new facility in the form
3. Make sure you select a "Place of Service"
4. Click "Save"

### **AdvancedMD- Adjusting CPT® Codes**

1. In AdvancedMD, go to "System Settings" >> "Transaction Codes" >> "Charge Codes"
2. ​​​​​​​Fill in the code, description and other desired fields.
   - *​​​​​​​​​​​​​​*For tips on which CPT Codes to use for telehealth, see our [Telehealth Billing Workflow](Telehealth-Coding-and-Workflows-Recommendations.md) guide.
3. Click "Save"

### **Elation- Important Place of Service (POS) and CPT Code steps**

Please be sure that the CPT codes that you add to Elation match exactly to the CPT codes in AdvancedMD. Without an exact match, the corresponding bills will fail.

After adding a new Facility to AdvancedMD and Practice Location to Elation, contact Elation using the "I need help" >> "I need help from Elation Team Member" button and notify us of the AdvancedMD Facility Code (in the "Code" field of the Facility you added) and we will work with AdvancedMD to map your new Place of Service for billing. You will not see this mapping for bills created via the Elation-AdvancedMD integration until this mapping step is complete and the bills sent from Elation will default to your primary Facility in AdvancedMD.

*CPT copyright 2022 American Medical Association. All rights reserved.*

## **Related Articles**

- [Telehealth: Billing & Workflow Recommendations](Telehealth-Coding-and-Workflows-Recommendations.md)
- Billing Guide- Creating a Super Bill and coding for your visit
- [Practice Locations Guide- Listing your service locations](adding-a-second-practice-location.md)
- [Billing Guide- Setting up CPT Codes and Place of Service](billing-settings---service-locations--procedure-codes.md)