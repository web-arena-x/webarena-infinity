# Billing Guide- Navigating Billing Settings

Source: https://help.elationhealth.com/s/article/billing-settings---service-locations--procedure-codes

---

## **Contents**

- [Billing Settings Overview](#How do I find my billing's settings?)
- [How to use Automatic Coding](#automatic_coding)
- [How to turn on Patient Invoicing](#how-do-i-turn-on-patient-invoicing)
- [How to enable Billing Guidance](#billing_guidance)
- [How to add Place of Service for Billing](#how-do-i-find-my-practice-locations-settings)
- [How to manage Popular CPT (Procedure) Codes](#Where do I find the Popular Procedure Codes list?)
- [How to enable additional billing fields](#enabled_billing_fields)
- [Practice Management System (PMS) Integration Users Only](#PMS_users_only)
 - [How to turn on Delayed Billing](#DelayedBilling)
 - [How to enable the "Bulk Send to PMS" button](#bulk_send_to_PMS)
 - [How to enable the "Send to PMS" button in the Visit Note draft](#send_to_PMS_from_visit_note)

## **Billing Settings Overview**

To view your Billing Settings, go to "Settings" >> "Billing". The Billing Settings allows you to do the following for your practice:

1. set automatic coding preferences
2. turn on Elation's [Patient Invoicing](patient-invoicing.md) feature
3. turn on reminders to code your visits
4. manage your practice's CPT Code database
5. enable additional billing fields
6. turn on special settings for Practice Management System (PMS) Integration users

## **How to use Automatic Coding**

Elation's coding automation is designed to help you get credit in quality programs for the documentation already present in your visit note by automatically adding CPT and/or ICD-10 codes to the billing information section of your visit notes based on certain information you enter or certain actions you take. Currently this feature applies to body mass index assessments (BMI), blood pressure (BP), and negative PHQ-9 depression screening results. For more information on this feature, please reference [Elation Coding Automation for BMI, Blood Pressure, and negative PHQ-9 screen results](elation-coding-automation.md).



## **How to turn on Patient Invoicing**

Patient Invoicing is a practice-wide setting that can be turned on or off inside Billing settings. Patient Invoicing can allow you to assign charges to procedures and generate invoices for patients from your bills. For more information on updating these settings and understanding this functionality please [click here](patient-invoicing.md).

**User Tip**: You can create your own custom code to use as a Popular CPT Code to charge patients for services that do not have standard CPT Codes when using [Patient Invoicing](patient-invoicing.md). Here are some common use cases:

- You can create a code called *FORMS* and associate a charge of $10 to it if you charge patients $10 for completing medical paperwork.
- You can create a code called *RCOPY*and associate a charge of $25 to it if you charge patients $25 for a copy of their medical records.
- You can create a code called *VMB12* and associate a charge of $35 to if if you charge patients $35 for Vitamin B12 injections.

## **How to enable Billing Guidance**

Billing Guidance is available to help your practice ensure you have entered all appropriate Procedure Codes and Diagnosis Codes in the [Billing Form](billing.md) when signing visit notes. This feature is designed to trigger a reminder at visit note sign-off if any Procedure Codes or Diagnosis Codes are missing. To enable this feature

1. Go "Billing Settings" -> "Billing Guidance"
2. Click the button on the right hand side to toggle the feature on (green)
3. Select which type of reminder you wish to use from the dropdown for each rule

The three options for Billing Guidance reminders are as follows:

- *None* = You would not see any reminders for that rule
- *Warning* = You will see a reminder that suggests adding additional billing information prior to signing your visit note. You can then continue by clicking
 1. “Add Billing Information” to add additional codes
 2. “Sign Anyway” to sign the visit note without adding additional codes
- *Prevent sign-off* = You will see a reminder that blocks you from signing your visit note until you add additional billing information. You can then continue by clicking
 1. “Add Billing Information” to add additional codes
 2. “Cancel” to return to your visit note draft

**Reminder as a suggestion (warning) at sign-off:**
![]()

**Reminder as a blocker, prevents sign-off:**
![]()

## **How to add Place of Service for billing**

When billing for a visit, you can specify a practice/service location and corresponding Place of Service (POS) code in your Practice Locations Settings page.

1. Go to "Settings" >> "Practice Locations"
2. Click "+ Add Practice Location" to add a new place of service or click "Edit" to edit an existing location
3. In the edit window, click on the *POS code* box to select the Place of Service code that corresponds to your practice location.
4. Click "Save"

For more details see: [Practice Locations Guide- Listing your service locations](adding-a-second-practice-location.md)

##

## **How to manage Popular CPT (Procedure) Codes**

The list of CPT (procedure) codes (that will appear in the billing window) is stored under Billing settings. Each practice can freely add, edit, or remove codes from the list or change the order in which they appear.

Under Billing Settings, scroll down to the section called Popular CPT® codes. Click "+Add CPT codes" to add additional codes, "edit" to make changes to existing CPT codes, "Delete" to delete codes, or drag and drop codes to re-order them.

**User Tips**:

- You can store codes with up to 8 characters.
- Cater the description to one that you can easily remember. This will make it easier for your to find CPT Codes when entering billing information in our visit notes.
- If you already have a patient chart open in another tab while you make changes to your Procedure list in Settings you will need to refresh that patient chart in order to view the changes.

### **'Charge' field**

If you have patient invoicing turned on, you can add default charges to each Procedure code in your list in Billing settings. Simply click "edit" and enter the charge amount. When you add a Procedure code with a default charge to your bill, the "Charge" field will automatically fill with the default charge value. Charges will then print on invoices when you generate an invoice for a patient.

## **How to enable additional billing fields**

You can enable additional billing fields and synchronize these fields; some of which will come in handy for customers who bill incident-to encounters. The fields include Supervising Provider, Billing Provider, Ordering Provider and Prior Authorization. To enable any of these fields:

1. Scroll down to the Billing Fields section
2. Click on the toggle to configure the fields you want to include on your bills - green is ON (enabled) and gray is OFF (disabled)
   - **Supervising Provider**
     - This field is for the Rendering Provider to store the name of their Supervising Provider if required by their State regulations.
       - **User Tip**: Each Provider Level User can select a default Supervising Provider under [User Settings](https://help.elationemr.com/s/article/User-Accounts-Guide-Provider-User#account_details).
   - **Billing Provider**
     - This field is used to store the name of the Provider that the claim is to be billed under and is commonly used for incident-to billing.
       - **User Tip**: Each Provider Level User can select a default Supervising Provider under [User Settings](https://help.elationemr.com/s/article/User-Accounts-Guide-Provider-User#account_details).
   - **Ordering Provider**
     - This field is used when services provided require a referral or order from another healthcare provider such as diagnostic imaging, laboratory tests, specialist consultations, and certain medical procedures. This is not a common field for Primary Care.
   - **Prior Authorization**
     - This field is used to store the Prior Authorization number, if required, for any services rendered on the bill.
3. Once a field is enabled, it will appear at the top of the bill in your EHR visit notes

**Important Notes**:

- For [Elation Billing](https://help.elationemr.com/s/article/Elation-Billing-All-in-One) customers, data stored in enabled fields will also push to Elation Billing when you push the bill over.
- For customers using the [Puredi integration](https://help.elationemr.com/s/article/Elation-Puredi-Integration-Guide), data stored in enabled fields will also push to Puredi when you push the bill over.
- \*\*These fields do not sync with other integrated PMS at this time.

## **Practice Management System (PMS) Integration Users Only**

The following Settings will only be available (and visible) for certain Practice Management System (PMS) Integration Users.

**Important Note**: Always consult your Practice Management System (PMS) user manual for the full details around how bills are synchronized between Elation and your integrated PMS.

### **How to turn on Delayed Billing**

Delayed Billing is a special setting for customers who are utilizing certain Practice Management System (PMS) integrations with Elation. [Learn more about the Delayed Billing feature here](How-to-set-up-Delayed-Billing.md).

### **How to enable the "Bulk Send to PMS" button**

The **Billing Home - Bulk Send to PMS** setting will allow you to enable or disable the “Bulk Send Bills to PMS” button in [Billing Home](Billing-Home.md). When toggled on, the “Bulk Send Bills to PMS” button allows you to bulk send all bills of a specific status to your integrated PMS. When toggled off the “Bulk Send Bills to PMS” button will not be available and each bill will need to be sent to your integrated PMS individually via the Actions Menu ![](). Note that bulk send actions impact ALL bills in the respective status you select.


You also have 3 options that you can configure along with the “Bulk Send Bills to PMS” button:

- Enable option to bulk send "Signed" bills
 - This Setting requires the ‘Delayed Bills’ setting to also be enabled in your Billing Settings. A ”Send all **Signed**” action will be available under “Bulk Send Bills to PMS” to allow you to send all bills in the **Signed** status to your integrated PMS.
- Enable option to bulk resend "Failed to Send" bills
 - A ”Resend all **Failed to send**” action will be available under “Bulk Send Bills to PMS” to allow you to send all bills in the **Failed to Send** status to your integrated PMS.
- Enable option to bulk resend "Sent to PMS" bills
 - A ”Resend all **Sent to PMS**” action will be available under “Bulk Send Bills to PMS” to allow you to send all bills in the **Sent to PMS** status to your integrated PMS.

![]()

## **How to enable the "Send to PMS" button in the Visit Note draft**

Certain PMS Integrations will allow you to send your bill to the PMS prior to signing the visit note. This feature is controlled by the **Sent to PMS from Visit Note** Setting. When toggled on, a "Send to PMS" button will appear in your visit note drafts and clicking on the button will immediately send the billing information entered over to your integrated PMS. When toggled off, the "Send to PMS" button will not be visit note in your visit note draft and the action of signing the Visit Note will push the billing information entered over to your integrated PMS (unless you have [Delayed Billing](#DelayedBilling) turned on).

##

**Next Step

Create your CPT Codes List and start utilizing it for billing today!**

## **Related Articles**

- [Billing Guide- Creating a Super Bill and coding for your visit](billing.md)
- [Billing Home Guide- A dashboard for managing your bills](Billing-Home.md)
- [Billing Guide- Patient Invoicing- Generating invoices to patients for services rendered](patient-invoicing.md)
- [Billing Guide- Frequently Asked Questions](Billing-Guide-Frequently-Asked-Questions.md)
- [Billing Guide- Delayed Billing](How-to-set-up-Delayed-Billing.md)
- [Visit Note Documentation Guide- Procedures](documenting-procedures.md)
- [Visit Note Documentation Guide- Assessments](visit-note-assessments.md)
- [Patient Demographics Guide- Managing patient insurance](Managing-Insurance.md)
- [Elation Coding Automation for BMI, Blood Pressure, and negative PHQ-9 screen results](elation-coding-automation.md)

##

**CPT c***opyright 1995 - 2022 American Medical Association. All rights reserved.*