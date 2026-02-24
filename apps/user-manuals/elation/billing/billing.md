# Billing Guide- Creating a superbill & coding for your visit

Source: https://help.elationhealth.com/s/article/billing

---

## **Contents**

- [What is the Billing Form?](#description)
- [Why is it important to store billing information for each patient encounter?](#value)
- [Entering billing details in the Billing Form](#entering_billing_details)
 - [Locating the Billing Form in a Visit Note](#location_of_form)
 - [Adding Service Location & other service details](#billing_details)
 - [Adding Procedure and Diagnosis codes](#coding)
    - [Exporting Diagnosis codes to a Visit Note](#export_billing)
 - [Saving the Billing Form](#save)
- [Using an integrated PMS with Elation](#pms)
- [Coding Tips](#tips)
 - [Copying billing items](#copying_line_items)
 - [Deleting billing items](#deleting_line_items)
 - [Automatic Coding](#automated_coding)
- [Frequently Asked Questions](#faq)

## **What is the Billing Form?**

The Billing Form is the section at the bottom of the visit note used to store Procedure Codes, Diagnosis Codes and other billing information generally used for insurance claims submissions. All available fields are listed below. Fields with an asterisk (\*) can be made available to you in the [Billing Settings](https://help.elationemr.com/s/article/billing-settings---service-locations--procedure-codes):

- Service Location
- Place of Service Code
- Referring Provider details
 - State the Referring Provider is located in
 - Name of the Referring Provider
- Patient Payment
- Ordering Provider details\*
 - State the Ordering Provider is located in\*
 - Name of the Ordering Provider\*
- Rendering Provider
- Supervising Provider Name\*
- Prior Authorization\*
- Billing Provider Name\*
- Procedure Codes (CPT or HCPCS)
- Diagnosis Codes (ICD-10)
- Modifier
- Amount, Quantity and Subtotal fields- generally for customers using the [Patient Invoicing](patient-invoicing.md) feature.

## **Why is it important to store billing information for each patient encounter?**

Billing information is generally used by insurance companies (also known as Payers) to understand the services rendered (based on procedure codes) during a patient encounter as well as understand the justification (based on diagnosis codes) behind the services rendered. This information is then used to calculate how much a provider is reimbursed for services rendered. Accurate and complete coding will result in timely payments from Payers and minimize the time and effort needed to receive reimbursement.

Elation strives to be the single place for all clinical information for your patients. You can use the Billing Form in the Visit Note to create a Super Bill for your patients. If you are using one of our integrated Practice Management System (PMS) partners, the claim will be automatically generated in the Practice Management System after you sign your visit note and you will not need to double document.

- **Important Note**: Only certain fields in the Billing Form sync with each integrated PMS. Consult the User Guide for your integrated PMS for detailed information on which fields sync to your integrated PMS.

## **Entering billing details in the Billing Form**

### **Locating the Billing Form in a Visit Note**

At the bottom of each Visit Note format, there is a button to "+ Add Billing Information." Click this button to open the Billing Form.

### **Adding Service Location & other service details**

Before adding your procedure and diagnosis codes to the Billing Form, review the following fields (as needed) to ensure all supporting details are sent along with your codes. Fields with an asterisk (\*) can be made available to you in the [Billing Settings](https://help.elationemr.com/s/article/billing-settings---service-locations--procedure-codes).

- **Service Location**
 - **Service Location** is a required field. The service locations listed is pulled from your Practice Locations Settings. If you need to add a new location, click “Edit Locations”. [Learn more about Practice Locations here.](adding-a-second-practice-location.md)
 - If you recently added a new service location to your Practice Location Settings, you may need to click “refresh list” for it to appear in the list of service locations to select for the Billing Form.
- **Place of Service**
 - If the Service Location you selected has a default Place of Service (POS) code, the default POS code is selected automatically. You can update the POS code for the claim as needed.
- Referring Provider details
 - **State**
    - Store the state the Referring Provider is located in.
 - **Referring Provider**
    - Store the name of the Referring Provider.
- **Patient Payment**
 - Store any payments received from the patient for the encounter (i.e. Copay, Deductible, Coinsurance, etc).
- Ordering Provider details\*
 - **State\***
    - Store the state the Ordering Provider is located in.
 - **Ordering Provider\***
    - Store the name of the Ordering Provider.
- **Rendering Provider**
 - Store the name of the Provider that rendered the services on the bill.
- **Supervising Provider\***
 - Select the name of the Supervising Provider.
- **Prior Authorization\***
 - Store the Prior Authorization # for services rendered
- **Mark as incident-to billing\***
 - **Billing Provider\***
    - Select the name of the Provider that the services should be billed under.
- Add any additional billing notes needed in the **Additional billing notes** field at the bottom of the Billing Form.
- Customers using the [Patient Invoicing](patient-invoicing.md) feature may need to use the following fields when generating a patient invoice:
 - **Amt ($)**
    - Store the amount you want to charge a patient for the procedure rendered.
    - You can use the minus (-) sign to enter a negative amount (such as a discount) if needed.
 - **Qty**
    - Store the quantity of the procedure you are charging for.
 - **Subtotal ($)**
    - The subtotal is automatically calculated by multiplying the **Amt ($)** and **Qty** fields.

**Important Notes**:
All fields with an asterisk (\*) above can be made available to you in the [Billing Settings](https://help.elationemr.com/s/article/billing-settings---service-locations--procedure-codes).

- For [Elation Billing](https://help.elationemr.com/s/article/Elation-Billing-All-in-One) customers, data stored in enabled fields will also push to Elation Billing when you push the bill over.
- For customers using the [Puredi integration](https://help.elationemr.com/s/article/Elation-Puredi-Integration-Guide), data stored in enabled fields will also push to Puredi when you push the bill over, with the exception of the **Ordering Provider** fields.
- \*\*These fields do not sync with other integrated PMS at this time.

### **Adding Procedure and Diagnosis codes**

Certain automated coding features will automatically add CPT codes or ICD-10 codes to the Billing Form:

- Selecting from your [personal CPT/HCPCS Code database](https://help.elationemr.com/s/article/billing-settings---service-locations--procedure-codes#Where%20do%20I%20find%20the%20Popular%20Procedure%20Codes%20list?) in the [Visit Note Procedures field](documenting-procedures.md)
- Selecting from the ICD-10 database from the [Visit Note Assessments field](visit-note-assessments.md)

You can also manually enter codes by following these instructions

1. Click in the **Procedure** field to type any CPT or HCPCS code you want to document.
   - If you have any CPT/HCPCS codes you commonly use, store it in your [Popular CPT Codes Settings](https://help.elationemr.com/s/article/billing-settings---service-locations--procedure-codes#Where%20do%20I%20find%20the%20Popular%20Procedure%20Codes%20list?) to create a personalized database. CPT/HCPCS codes in your personal database can be found by:
     1. Typing in the CPT/HCPCS code
     2. Typing in the description text of the procedure code you are looking for
     3. Scrolling through the list Elation automatically shows you, which includes your practice’s popular CPT/HCPCS codes.

![]()

- For non-insurance bills, instead of typing in CPT/HCPCS codes you can also free-text any service you want to bill for (ex. *Records Copy*) in the **Procedure** field. The **Procedure** field can hold up to 20 characters.

1. Click in the **Modifiers** field to type in any modifier code, as needed.
2. Click the “+ Add Dx” button or type in a blank **Dx** field to search for the diagnosis code you want to document and select the appropriate code from Elation’s Diagnosis Code database. You can search by:
   1. Typing in the description of the diagnosis
   2. Typing in the ICD-10 code
   - The diagnosis codes from the patient's Problem List will also appear automatically for selection
   - You can also search by ICD-9 code but only the ICD-10 code will appear in the Billing Form.
3. Click the "+ Add Billing Item" button to add additional billing lines.
4. Click one of the "Save" options to save your edits.

#### **Exporting diagnosis codes to a Visit Note**

You can also add ICD-10 codes to your Billing Form by exporting the problems from the patient’s Problem List in the Clinical Profile. You can either export all of the problems to a visit note, or select individual problems to export, by clicking “Actions” and selecting one of the “Export to Note” options that exports to Billing.

![]()

**Important Note:** If your Problem List contains deprecated, non-billable diagnosis codes, you will be unable to export those codes to the Billing section of a visit note. Please follow the instructions in [this Guide](Managing-deprecated-ICD10-codes.md) to update the deprecated codes to active codes to optimize usage of the export feature from the Problem List.



### **Saving the Billing Form**

Use one of the "Save" options at the bottom of the Billing Form to save any data entered in the Billing Form.

- If you click "Discard", any edits made will be discarded.


A Billing Guidance feature is also available to help your practice ensure you are not missing billing information when signing visit notes. When turned on, this feature is designed to trigger a reminder at visit note sign-off to review your bill for missing procedure or diagnosis codes. [Learn more about the Billing Guidance feature here.](billing-settings---service-locations--procedure-codes.md#coding_guidance)


## **Using an integrated PMS with Elation**

Only certain fields in the Billing Form sync with each integrated Practice Management System (PMS). Consult the User Guide for your integration PMS for detailed information on which fields sync to your integrated PMS.


## **Coding Tips**

### **Copying billing items**

To expedite your code entry workflow, use the ![]() (duplicate button) to the right of a billing line to create a copy of all the procedure and diagnosis codes from that billing line to a new billing line. This makes it easy for you to code for multiple procedures that have similar supporting diagnosis codes.

### **Deleting billing items**

Click the ![]() (delete button) to the right of the billing line to delete an entire line of billing entry (including all the procedure codes, diagnosis codes and modifiers you have entered).


### **Automated Coding**

Learn more about automatic coding options in the following [Automatic Coding Guide](elation-coding-automation.md).



## **Frequently Asked Questions (FAQ)**

#### **Can I edit my billing information at any time?**

Yes! To edit the billing information before a visit note is signed off, simply click "Edit Billing" where the billing information you've entered is displayed at the bottom of the visit note.

Once a visit note is signed by a Provider Level User, only the Provider Level User that signed the visit note or their [billing delegate](staff-permissions--staff-delegates.md#bills_view) can edit the billing information tied to the visit note. To edit billing information for a visit note after that visit note is signed, find the visit note in the chronological record in the patient's chart and click “Actions” -> “Edit Bill”.

**Important Note**: For customers using a Practice Management System (PMS) integration with Elation, edits to the billing information will not be pushed to the PMS. You must edit the bill/claim directly in your PMS if changes are needed.

#### **Can the bill show both ICD-9 and ICD-10 codes for Dx?**

Elation will automatically show both the ICD-9 and ICD-10 in the diagnosis database every time you search for a diagnosis code. You can also search by both ICD-9 and ICD-10 codes. Only the ICD-10 code will display in the Billing Form and only the ICD-10 code is sent to an integrated PMS.

#### **Can I add charges to the Billing Form?**

Turn on Patient Invoicing to print patient invoices after entering charges in the **Amt ($)**, **Qty** and **Subtotal ($)** fields of the Billing Form. [Learn more about Patient Invoicing here](patient-invoicing.md).

**Important Note**: For customers using a Practice Management System (PMS) integration with Elation, the **Amt ($)**, **Qty** and **Subtotal ($)** fields do not sync with any PMS.

## **Next Step**

**Start coding for your visits today!**

## **Related Articles**

- [Billing Home Guide- A dashboard for managing your bills](Billing-Home.md)
- [Billing Guide- Navigating Billing Settings](billing-settings---service-locations--procedure-codes.md)
- [Billing Guide- Patient Invoicing- Generating invoices to patients for services rendered](patient-invoicing.md)
- [Billing Guide- Frequently Asked Questions](Billing-Guide-Frequently-Asked-Questions.md)
- [Visit Note Documentation Guide- Procedures](documenting-procedures.md)
- [Visit Note Documentation Guide- Assessments](visit-note-assessments.md)
- [Patient Demographics Guide- Managing patient insurance](Managing-Insurance.md)
- [Insurance Card Image Upload Guide](Insurance-Card-Image-Upload-Guide.md)
- [Visit Note Templates Guide](elation-visit-note-templates.md)
- [Billing Guide- Delayed Billing](How-to-set-up-Delayed-Billing.md)
- [Elation Billing- Using Elation's all-in-one billing solution to manage your claims](Elation-Billing-All-in-One.md)