# Billing Guide- Frequently Asked Questions

Source: https://help.elationhealth.com/s/article/Billing-Guide-Frequently-Asked-Questions

---

## **Contents**

- [What billing features are available in Elation?](#billing_features)
- [Generating bills](#generating_bills)
 - [Where do I enter billing information in Elation EHR?](#where_to_enter_billing)
 - [What billing information can I store in Elation?](#billing_fields)
 - [Who can enter billing  information?](#who_can_enter)
 - [How many claims can I generate per encounter?](#claims_per_encounter)
 - [How do I enter codes?](#how_to_enter)
 - [I want to save the bill and come back at a later time to complete my coding. Is that possible?](#save_as_draft)
 - [Can I edit my billing information at any time?](#when_to_edit)
 - [How do I edit billing information before signing?](#when_to_edit)
 - [How do I adjust the Date of Service of a bill?](#date_of_service)
 - [Can I add custom fields to the Billing Form?](#custom_fields)
 - [Are there any ‘required’ fields in a bill?](#required_fields)
 - [Can I add charges to the Billing Form?](#add_charges)
 - [How do I mark my bill as complete?](#mark_bill_as_complete)
 - [Where can I see all my incomplete bills?](#see_incomplete_bills)
 - [Can I create a bill without a visit note?](#bill_without_visit)
 - [How do I bill for a lab or procedure that I performed in-house?](#in_house_procedure)
- [Coding for an encounter](#coding)
 - [How many codes can I add to a bill?](#code_limit)
 - [How do I enter a procedure code?](#entering_procedure_codes)
 - [Does Elation have a CPT Code (Procedure Code) database for me to select from?](#cpt_database_not_available)
 - [Do I have to add a CPT Code to my Popular CPT Code Settings in order to use it?](#CPT_settings_requirement)
 - [How do I delete or correct procedure codes?](#correct_CPT)
 - [How do I enter modifiers?](#entering_modifiers)
 - [Does Elation have a modifier database for me to select from?](#modifier_database)
 - [How do I delete or correct modifiers?](#correct_modifiers)
 - [How do I enter a diagnosis code?](#entering_diagnosis_codes)
 - [Does Elation have an ICD-10 Code (Diagnosis Code) database for me to select from?](#ICD10_database)
 - [Can I reuse codes from the patient’s Problem List?](#resuse_problem_list)
 - [How do I delete or correct diagnosis codes?](#correct_diagnosis_codes)
 - [Can the bill show both ICD-9 and ICD-10 codes for Dx?](#ICD9)
 - [Can I edit my billing information at any time?](#when_to_edit)
 - [A procedure code is in the wrong place, what’s the quickest way to move it to the correct place in the bill?](#moving_procedure_codes)
 - [A diagnosis code is in the wrong place, what’s the quickest way to move it to the correct place in the bill?](#moving_diagnosis_codes)
 - [I am billing for a couple of services with the same diagnosis codes. Is there a convenient way to enter this information?](#reusing_codes)
 - [Does Elation offer any coding guidance or coding edits? (Ex. Recommending codes based on certain documentation or workflows.)](#coding_edits)
 - [Does Elation offer any automatic coding?](#automatic_coding)
 - [Certain codes are always billed together. Can I save those as templates?](#billing_templates)
- [Managing signed bills](#managing_signed_bills)
 - [Can I edit a bill after I signed my visit note?](#edit_after_sign)
 - [How do I edit billing information after a visit note is signed off?](#how_to_edit_after_sign)
 - [Where can I see all my signed bills?](#seeing_signed_bills)
 - [How do I submit a bill to the patient’s insurance company?](#submitting_claims)
 - [How can I share all my bills with my biller?](#share_with_biller)
 - [How do I bill a patient for the encounter?](#bill_patient)
- [Billing Settings](#billing_settings)
 - [What Settings need to be configured in order to effectively bill for an encounter?](#settings_best_practice)
 - [What billing settings do Elation offer?](#available_settings)
 - [Does the 'Patient Invoicing' setting allow me to send an invoice to my patient to collect payment?](#patient_invoicing)
 - [How do I add more Service Locations?](#service_locations)
 - [How do I add more CPT codes to my CPT code database?](#add_to_CPT_settings)
 - [What is Billing Guidance?](#billing_guidance)
 - [What is Automatic Coding?](#automatic_coding)
- [Billing Home](#billing_home)
 - [What is Billing Home?](#billing_home_overview)
 - [What can I see in Billing Home?](#billing_home_contents)
 - [How many bills can I see in the Billing Home at any given time?](#billing_home_count)
 - [What actions can I take on a bill from Billing Home?](#billing_home_actions)
 - [Can I edit my bill details from Billing Home without opening the chart?](#edit_from_Billing_Home)
 - [What filter options are available in Billing Home?](#billing_home_filters)
 - [Can I customize the quick filters available?](#customize_quick_filters)
 - [Can I save frequently used filters?](#save_filters)
 - [Can I download a report of my bills?](#download_bills_report)
 - [Can I print a report of my bills?](#print_bills_report)
 - [Can I set permissions around the actions that users are permitted to take?](#billing_home_permissions)
 - [Can I switch back to the old Billing Report view?](#switch_back_to_billing_report)
- [Practice Management System (PMS) Integration Users](#PMS_users)
 - [What billing information is typically shared with my integrated PMS?](#billing_fields_synced_to_PMS)
 - [When is billing information sent to my integrated PMS?](#when_is_bill_sent)
 - [How can I tell if billing information was pushed to my integrated PMS?](#how_to_tell_if_bills_synced)
 - [Can I choose when to push my bills to my integrated PMS?](#when_to_push_bills_to_PMS)
 - [What is Delayed Billing?](#delayed_billing)
 - [What is the 'Billing Home - Bulk Send to PMS' setting?](#bulk_send_to_PMS)
 - [What does the "Bulk Send Bills to PMS" button do?](#bulk_send_button)
 - [How do I send individual bills from a specific date range to my integrated PMS?](#send_individual_bills)
 - [How do I bulk send all the bills from a specific date range to my integrated PMS?](#bulk_send)
 - [Do all CPT Codes sync to my integrated PMS?](#CPT_code_syncing)
 - [How many diagnosis codes can I send to my integrated PMS?](#ICD10_syncing)
 - [If I edit a bill in Elation after I send the billing information to my integrated PMS, will my integrated PMS receive the changes?](#edit_after_send)
 - [If I edit a bill in my PMS, will Elation receive the changes?](#edit_bill_in_PMS)
- [Non-insurance billing](#non_insurance_billing)
 - [Can I use the Billing Form to create bills for my patient?](#bills_to_patients)
 - [Can I bill for services without using any codes?](#bill_without_coding)
 - [How do I generate an invoice?](#generate_an_invoice)
 - [How do I generate a superbill/receipt for the patient to send to their insurance company for reimbursement?](#patient_reimbursement)
 - [What should I do if part of a visit is payable by insurance and part of it is patient self-pay?](#insurance_plus_self_pay)

## **What billing features are available in Elation?**

| Feature | Description | |
| --- | --- | --- |
| [Elation Billing](https://help.elationemr.com/s/article/Elation-Billing-All-in-One) | Elation’s all-in-one billing solution for practices that bill insurance | |
| [Billing Form](https://help.elationemr.com/s/article/billing) | Enter billing information for each patient encounter | |
| [Billing Home](https://help.elationemr.com/s/article/Billing-Home) | Dashboard for managing all your bills | |
| [Patient Invoicing](https://help.elationemr.com/s/article/patient-invoicing) | Generate invoices to bill patients | |
| [Patient Payments](https://help.elationemr.com/s/article/using-elation-to-securely-collect-patient-payments) | Securely collect credit card & debit card payments from patients | |
| [Membership Management](https://help.elationemr.com/s/article/Introduction-to-Membership-Management-with-Elation) | Collect recurring membership payments from patients | |




## **Generating bills**

| | |
| --- | --- |
| Where do I enter billing information in Elation EHR? | Billing information is always tied to a visit note in the EHR. Go to the bottom of a visit note draft, click “+Add Billing Information” or “Edit Billing” to use the [Billing Form](billing.md) to add billing information for the encounter. |
| What billing information can I store in Elation? | Elation’s [Billing Form](billing.md) allows you to store the following billing information for each encounter:   - Date of Service - Service Location - Place of Service Code - State in which services were rendered - Name of a Referring Provider - Patient payment notes - Procedure codes, modifiers and diagnosis codes - Charge details (for patient invoices only) |
| Who can enter billing  information? | While a visit note is still in draft (not signed off), anyone in the practice can enter billing information into the [Billing Form](billing.md). Once a visit note is signed by a Provider Level User, only the Provider Level User that signed the visit note or their [billing delegate](staff-permissions--staff-delegates.md#bills_view) can edit the billing information tied to the visit note. |
| How many claims can I generate per encounter? | You can only generate one bill/claim per visit note. If you need multiple claims for the same encounter, you will need to generate two visit notes for that encounter. |
| How do I enter codes? | See the *[Coding for an encounter](#coding)* section for more details about coding for an encounter. |
| I want to save the bill and come back at a later time to complete my coding. Is that possible? | Yes! You can save your work at any time by clicking “Save & Close” at the bottom of the [Billing Form](billing.md). As best practice, also click “Save as Draft & Close” at the bottom of your Visit Note to save your documentation as well. |
| Can I edit my billing information at any time? | Yes! To edit the billing information before a visit note is signed off, simply click "Edit Billing" where the billing information you've entered is displayed at the bottom of the visit note.    Once a visit note is signed by a Provider Level User, only the Provider Level User that signed the visit note or their [billing delegate](staff-permissions--staff-delegates.md#bills_view) can edit the billing information tied to the visit note. To edit billing information for a visit note after that visit note is signed, find the visit note in the chronological record in the patient's chart and click “Actions” -> “Edit Bill”. **Important Note**: For PMS integration users, Elation’s PMS integrations are NOT built to receive edits after billing information is sent to the PMS. You must edit the bill/claim in both Elation EHR and your PMS. |
| How do I edit billing information before signing? | To edit the billing information before a visit note is signed off, simply click "Edit Billing" where the billing information you've entered is displayed at the bottom of the visit note. Once a visit note is signed by a Provider Level User, only the Provider Level User that signed the visit note or their [billing delegate](staff-permissions--staff-delegates.md#bills_view) can edit the billing information tied to the visit note. To edit billing information for a visit note after that visit note is signed, find the visit note in the chronological record in the patient's chart and click “Actions” -> “Edit Bill”. |
| How do I adjust the Date of Service of a bill? | Billing information is always tied to a visit note in the EHR. To correct the date of service, go to the top of the Visit Note draft and click on the date to adjust it. |
| Can I add custom fields to the Billing Form? | You cannot customize any field on the Billing Form at this time. For any additional information that you might need to include on a claim (ex. ‘Date of Injury’ or NDC codes), use the **Additional billing notes** field at the bottom of the Billing Form. |
| Are there any ‘required’ fields in a bill? | By default, the only required field is **Service Location**. If you would like to make procedure codes and diagnosis codes required, you can turn on the [Billing Guidance](billing-settings---service-locations--procedure-codes.md#billing_guidance) feature to set reminders to add codes before signing off on a visit note. Best practice is to enter all the details and codes needed to effectively receive payment from a Payer when submitting a claim. This information usually includes but is not limited to:   - Procedure codes - Diagnosis codes - Service Location - Place of Service Code   **Important Note**: As best practice, always verify coding requirements with the Payer. |
| Can I add charges to the Billing Form? | Yes, you can use the **Amt ($)**, **Qty** and **Subtotal ($)** fields in the Billing Form to add charges to your Procedure Codes. The charges will display when you use the Patient Invoicing feature to generate patient invoices. [Click here to learn more about Patient Invoicing](patient-invoicing.md). **Important Note**: For customers using a Practice Management System (PMS) integration with Elation, the **Amt ($)**, **Qty** and **Subtotal ($)** fields do not sync with any PMS. |
| How do I mark my bill as complete? | There isn’t a distinct status that you can set to show that a bill is complete. The best practice for marking a bill as complete is signing the visit note. |
| Where can I see all my incomplete bills? | You can use [Billing Home](Billing-Home.md) to manage all your signed bills; including editing bills. Use the Awaiting sign-off or No bill filters at the top of Billing Home to see all your incomplete bills. |
| Can I create a bill without a visit note? | No, billing information can only be tied to a visit note in the EHR. |
| How do I bill for a lab or procedure that I performed in-house? | Codes that are required for you to get paid for labs or procedures need to be added manually to the visit note’s Billing Form. These codes will not automatically appear as a result of other workflows (ex. Lab Order form, Vaccine form). |




## **Coding for an encounter**

| | |
| --- | --- |
| How many codes can I add to a bill? | You can add as many procedure codes and diagnosis codes as applicable when billing for an encounter. **Important Note**: For PMS integration users, certain PMS integrations may limit how many diagnosis codes they can accept. Please consult your PMS User Manual for full details about how many codes sync to your integrated PMS. |
| How do I enter a procedure code? | The recommended workflow for adding procedure codes (such as CPT Code or HCPCS Code) is to open the Billing Form at the bottom of the visit note. Under the Coding section in this form, you can enter a code in the **Procedure** field and add additional codes by clicking “+ Add Billing Item”. |
| Does Elation have a CPT Code (Procedure Code) database for me to select from? | No, Elation does not have a full CPT Code database for customers to select from. However, customers can use Elation’s [Popular CPT Code Setting](billing-settings---service-locations--procedure-codes.md#Where%20do%20I%20find%20the%20Popular%20Procedure%20Codes%20list?) feature to save the codes they commonly use. |
| Do I have to add a CPT Code to my Popular CPT Code Settings in order to use it? | No, you do not have to add a CPT Code to your [Popular CPT Code Setting](billing-settings---service-locations--procedure-codes.md#Where%20do%20I%20find%20the%20Popular%20Procedure%20Codes%20list?) in order to use it. You can free text any code you wish in the Billing Form’s **Procedure** field at any time. **Important Note**: PMS Integration users must consult their PMS User Manual for full details on how to utilize Procedure codes while using an integrated PMS. |
| How do I delete or correct procedure codes? | To delete a procedure code, place your cursor at the end of the code you want to delete and then use the ‘Delete’ key on your keyboard to delete the unwanted code. You can then enter a new procedure code in the **Procedure** field as needed. If you want to delete the entire billing line, including the associated diagnosis codes & modifiers, click on the ‘trashcan’ button  to the right of the billing line. **Important Note**: Information deleted from a bill cannot be restored. Please delete with caution. |
| How do I enter modifiers? | Use the **Modifiers** field within the Billing Form to enter modifiers. |
| Does Elation have a modifier database for me to select from? | No, Elation does not have a modifier database for customers to select from. Customers can enter any modifier of their choice when entering billing information into the **Modifiers** field of a bill. |
| How do I delete or correct modifiers? | To delete a modifier, place your cursor at the end of the modifier you want to delete and then use the ‘Delete’ key on your keyboard to delete the unwanted code. You can then enter a new modifier as needed. **Important Note**: Information deleted from a bill cannot be restored. Please delete with caution. |
| How do I enter a diagnosis code? | Use the **Dx** field to enter diagnosis codes. Click the “+ Add Dx” button if you need additional diagnosis fields. |
| Does Elation have an ICD-10 Code (Diagnosis Code) database for me to select from? | Yes, Elation does have a full ICD-10 Code database for customers to select from. You can find any code in the ICD-10 Code database by typing in the code or description in the **Dx** field of a bill. Click the “+ Add Dx” button if you need additional diagnosis fields. |
| Can I reuse codes from the patient’s Problem List? | Yes, you can reuse codes from the patient’s Problem List. To export an ICD-10 code from the Problem List to a bill, locate the problem in the Problem List, and then click “Actions” -> “Export to Note (Billing)”. Use the “Export to Note (A, Billing)” option if you want to export the problem to the Assessment section as well as the Billing section. |
| How do I delete or correct diagnosis codes? | To delete a diagnosis code click the “x” button to the right of the code. You can then click “+ Add Dx” to enter a new diagnosis code as needed. **Important Note**: Information deleted from a bill cannot be restored. Please delete with caution. |
| Can the bill show both ICD-9 and ICD-10 codes for Dx? | Elation will automatically show both the ICD-9 and ICD-10 in the diagnosis database every time you search for a diagnosis code. You can also search by both ICD-9 and ICD-10 codes. Only the ICD-10 code will display in the Billing Form and only the ICD-10 code is sent to an integrated PMS. |
| Can I edit my billing information at any time? | Yes! To edit the billing information before a visit note is signed off, simply click "Edit Billing" where the billing information you've entered is displayed at the bottom of the visit note.    Once a visit note is signed by a Provider Level User, only the Provider Level User that signed the visit note or their [billing delegate](staff-permissions--staff-delegates.md#bills_view) can edit the billing information tied to the visit note. To edit billing information for a visit note after that visit note is signed, find the visit note in the chronological record in the patient's chart and click “Actions” -> “Edit Bill”. **Important Note**: For PMS integration users, Elation’s PMS integrations are NOT built to receive edits after billing information is sent to the PMS. You must edit the bill/claim in both Elation EHR and your PMS. |
| A procedure code is in the wrong place, what’s the quickest way to move it to the correct place in the bill? | To move a procedure code to a different place in the bill:   1. Find the ‘drag’ button  to the left of the procedure code you want to move 2. Click and hold onto the button with your mouse cursor 3. Drag it to the desired location in the bill & then let go of your mouse cursor |
| A diagnosis code is in the wrong place, what’s the quickest way to move it to the correct place in the bill? | To move a diagnosis code to a different place in the bill:   1. Find the ‘drag’ button  to the left of  the diagnosis code you want to move 2. Click and hold onto the button with your mouse cursor 3. Drag it to the desired location in the bill & then let go of your mouse cursor |
| I am billing for a couple of services with the same diagnosis codes. Is there a convenient way to enter this information? | Yes, you can use the ‘duplicate’ button  to the right of a billing line to create a copy of all the procedure and diagnosis codes from that billing line to a new billing line. This makes it easy for you to code for multiple procedures that have similar supporting diagnosis codes. |
| Does Elation offer any coding guidance or coding edits? (Ex. Recommending codes based on certain documentation or workflows.) | Elation does not offer any coding guidance features at this time. |
| Does Elation offer any automatic coding? | Yes, Elation offers a few automatic coding features:   1. CPT Codes will automatically be added to the Billing Form if any procedures with CPT codes were added to the [Procedure](documenting-procedures.md) section of the Visit Note draft 2. ICD-10 codes will automatically be added to the first line of the Billing Form if any diagnoses were added to the [Assessment](visit-note-assessments.md) section of the Visit Note draft 3. Certain CPT codes or ICD-10 codes will automatically be added to the Billing Form when the [Automatic Coding Setting](elation-coding-automation.md) is turned on for the following workflows: - When BMI is calculated after you enter the patient’s height and weight in a visit note - When blood pressure is entered in a visit note - When you export a PHQ-9 screening into the visit note |
| Certain codes are always billed together. Can I save those as templates? | You can use the [Visit Note Template](elation-visit-note-templates.md) feature to store codes that are commonly billed together as templates. These templates can be used in any visit note draft. |




## **Managing signed bills**

| | |
| --- | --- |
| Can I edit a bill after I signed my visit note? | Once a visit note is signed by a Provider Level User, only the Provider Level User that signed the visit note or their [billing delegate](staff-permissions--staff-delegates.md#bills_view) can edit the billing information tied to the visit note. To edit billing information for a visit note after that visit note is signed, find the visit note in the chronological record in the patient's chart and click “Actions” -> “Edit Bill”. **Important Note**: For PMS integration users, Elation’s PMS integrations are NOT built to receive edits after billing information is sent to the PMS. You must edit the bill/claim in both Elation EHR and your PMS. |
| How do I edit billing information after a visit note is signed off? | Once a visit note is signed by a Provider Level User, only the Provider Level User that signed the visit note or their [billing delegate](staff-permissions--staff-delegates.md#bills_view) can edit the billing information tied to the visit note. To edit billing information for a visit note after that visit note is signed, find the visit note in the chronological record in the patient's chart and click “Actions” -> “Edit Bill”. **Important Note**: For PMS integration users, Elation’s PMS integrations are NOT built to receive edits after billing information is sent to the PMS. You must edit the bill/claim in both Elation EHR and your PMS. |
| Where can I see all my signed bills? | You can use [Billing Home](Billing-Home.md) to manage all your signed bills; including editing bills. Use the Signed filter at the top of Billing Home to see all your signed bills. |
| How do I submit a bill to the patient’s insurance company? | You can sign up for Elation Billing or use a Practice Management System (PMS) to send claims to the Payer.   - [Click here to learn more about Elation Billing; Elation’s all-in-one billing solution](https://help.elationemr.com/s/article/Elation-Billing-All-in-One) - [Click here for a list of integrated PMS](https://www.elationhealth.com/integrations/) |
| How can I share all my bills with my biller? | There are two options for sharing billing information with your biller:   1. Give the biller a Staff Level User account in the EHR and the biller can sign in to view all your bills in [Billing Home](Billing-Home.md).    - [Click here to learn more about inviting the biller to create an Elation account](managing-user-accounts.md#invite_staff). 2. If you do not want or need the biller to have access to the EHR, [download a report of your bills from Billing Home](Billing-Home.md#download_report) and share the report with your biller using HIPAA-compliant methods. |
| How do I bill a patient for the encounter? | You can use the Patient Invoicing feature to generate a patient-facing invoice to bill a patient for the encounter. [Click here to learn more about Patient Invoicing](patient-invoicing.md). **Important Note**: The Patient Invoicing feature does not charge the patient. To create a payment request or charge the patient, please use our [Patient Payments feature](https://help.elationemr.com/s/article/using-elation-to-securely-collect-patient-payments), powered by Stripe. |




## **Billing Settings**

| | |
| --- | --- |
| What Settings need to be configured in order to effectively bill for an encounter? | At a minimum, each practice should   1. Store all their [Practice Locations](adding-a-second-practice-location.md) in Elation. You will then be able to see and select from your Practice Locations in the **Service Location** field for each bill. 2. Turn on [Billing Guidance](billing-settings---service-locations--procedure-codes.md#billing_guidance) to ensure coding is completed for each encounter. 3. Store all your commonly used [CPT Codes](billing-settings---service-locations--procedure-codes.md#Where%20do%20I%20find%20the%20Popular%20Procedure%20Codes%20list?) in your Billing Settings to easily find and use these codes when coding for an encounter.   [Click here to see all available Billing Settings](billing-settings---service-locations--procedure-codes.md). |
| What billing settings do Elation offer? | To view your Billing Settings, go to "Settings" -> "Billing". The Billing Settings allows you to do the following for your practice:   - set automatic coding preferences - turn on Elation's Patient Invoicing feature - turn on reminders to code your visits - manage your practice's CPT Code database - turn on special settings for Practice Management System (PMS) Integration users   [Click here to learn more about Billing Settings](billing-settings---service-locations--procedure-codes.md). |
| Does the 'Patient Invoicing' setting allow me to send an invoice to my patient to collect payment? | Turning “Patient Invoicing” on only allows you to print an invoice for the encounter. It doesn’t not automatically deliver the invoice electronically to the patient nor create a payment request. To generate invoices that patients can pay, please use our [Patient Payments feature](https://help.elationemr.com/s/article/using-elation-to-securely-collect-patient-payments), powered by Stripe. |
| How do I add more Service Locations? | First, add all your Service Locations to your [Practice Locations](adding-a-second-practice-location.md) Setting. You will then be able to see and select from your Practice Locations in the **Service Location** field for each bill. |
| How do I add more CPT codes to my CPT code database? | Use the [Popular CPT Codes Setting](billing-settings---service-locations--procedure-codes.md#Where%20do%20I%20find%20the%20Popular%20Procedure%20Codes%20list?) to store all your commonly used procedure codes in your Billing Settings to easily find and use these codes when coding for an encounter. |
| What is Billing Guidance? | The [Billing Guidance](billing-settings---service-locations--procedure-codes.md#billing_guidance) feature allows you to set reminders to complete coding before signing off on a visit note. |
| What is Automatic Coding? | The [Automatic Coding Setting](elation-coding-automation.md) automatically adds CPT codes or ICD-10 codes to the bill for the following workflows:   - When BMI is calculated after you enter the patient’s height and weight in a visit note - When blood pressure is entered in a visit note - When you export a PHQ-9 screening into the visit note |




## **Billing Home**

| | |
| --- | --- |
| What is Billing Home? | Billing Home is a dashboard of all the bills for your practice. [Click here to learn more about Billing Home](Billing-Home.md). |
| What can I see in Billing Home? | Billing Home shows you all the visit notes tied to patient encounters as well as their associated billing details including:   - Date of service - Patient’s name - Status of the bill - Provider tied to the bill - Service location - Place of Service (POS) code - Billing reference # - Primary insurance name, Group ID and Member ID - Secondary insurance name, Group ID and Member ID - Codes - Charges - Patient payment notes - Any other billing notes |
| How many bills can I see in the Billing Home at any given time? | You can see all bills from Billing Home.   - If you are a Provider Level User, the dashboard will default to only showing your bills. Use the Providers filter to see bills of other Providers in your practice if needed. - If you are a Staff Level User, the dashboard will default to showing bills for all Providers. Use the Providers filter to see bills of specific Providers only if needed.   By default Billing Home will show you bills from the last 7 days and you can use the filters to adjust the date range at any time. Each page of Billing Home will show up to 25 bills. |
| What actions can I take on a bill from Billing Home? | Depending on the status of your bill, you may take one or more of the following actions when clicking on the Actions Menu button  next to any bill:   - Edit your bill from Billing Home - Open the Visit Note & chart tied to the bill - Mark a bill as ‘Billed’ - Edit the Billing Reference # associated with a bill - View the history of status changes on a bill - Push the bill to your PMS (for PMS integration users only)   [Click here to learn more about the various actions you can take on a bill](Billing-Home.md#actions_menu). |
| Can I edit my bill details from Billing Home without opening the chart? | Yes, click on the Actions Menu Actions  next to the bill you want to edit and click “Add Bill” or “Open Bill” to edit the bill directly in Billing Home. This action is only available for bills in the No bill or Awaiting Sign Off statuses. |
| What filter options are available in Billing Home? | There are two filter options in Billing Home:   1. Quick Filters - These buttons allow you to see the bills tied to specific statuses with the click of a button. The Quick Filters are:    - Last 90 days    - Awaiting sign-off    - Signed    - No bill    - Mark as billed 2. Customer Filters - You can now apply your own custom filters for the following bill details. Customer filters are:    - Visit dates    - Status    - Providers    - Service location    - Place of service   [Click here to learn more about the different filters in Billing Home](Billing-Home.md#using_filters). |
| Can I customize the quick filters available? | The available Quick filters cannot be customized at this time. We will notify you if this feature becomes available in the future. |
| Can I save frequently used filters? | The ability to save commonly used filters is not available at this time. We will notify you if this feature becomes available in the future. |
| Can I download a report of my bills? | Yes. To download a copy of the bills displayed as a .CSV file, click on the Download button at the top of Billing Home. You can open the report using any spreadsheet software and then you can print the report from that software. |
| Can I print a report of my bills? | Yes. To print a report of your bills, first download a copy of the bills displayed by clicking on the Download button  at the top of Billing Home. Afterwards, open the report using any spreadsheet software and then print the report from that software. |
| Can I set permissions around the actions that users are permitted to take? | The ability to set permissions around which users can take which actions is not available at this time. We will notify you if this feature becomes available in the future. |
| Can I switch back to the old Billing Report view? | Yes, you can switch back to the old Billing Report view by clicking the "Switch to old Billing Report" button at the top of Billing Home. |





## **Practice Management System (PMS) Integration Users**

| | |
| --- | --- |
| What billing information is typically shared with my integrated PMS? | The following billing information is always sent to the PMS:   - Date of Service - Service Location - Place of Service Code - Procedure Codes and their associated modifiers and diagnosis codes   **Important Note**: Always consult your Practice Management System (PMS) user manual for the full details around what information is synchronized between Elation and your integrated PMS and how the information is synchronized. |
| When is billing information sent to my integrated PMS? | By default, billing information is pushed to the integrated PMS whenever a Provider Level User signs the associated visit note. There are a couple of exceptions that will allow you to send billing information to your PMS that is independent of signing a Visit Note:   1. Certain PMS integrations support a "Send To PMS from Visit Note" feature where you can use the “Send to PMS” button at the bottom of a visit note to send the billing information to your integrated PMS prior to signing the visit note. 2. Certain PMS integrations support the [Delayed Billing](How-to-set-up-Delayed-Billing.md) feature which allows you to hold your bills in [Billing Home](Billing-Home.md) and manually push them over to your integrated PMS whenever you choose.   **Important Note**: Consult your Practice Management System (PMS) user manual to see which features your integrated PMS supports, if any. |
| How can I tell if billing information was pushed to my integrated PMS? | Depending on which PMS integration you use with Elation:   1. Certain PMS will tell us they received the billing information and return a Billing Reference #, which you will see on the bill. 2. Certain PMS will tell us if they failed to receive a bill. If this happens the bill will be put in the Failed to Send status in [Billing Home](Billing-Home.md) and you can attempt to resend the bill.   Otherwise, the best option for seeing if a bill was pushed to your PMS is by checking your PMS. **Important Note**: Consult your Practice Management System (PMS) user manual to see which features your integrated PMS supports, if any. |
| Can I choose when to push my bills to my integrated PMS? | Yes, certain PMS integrations support the following features that will allow you to manually push your bills to your integrated PMS at your own preference.   1. Certain PMS integrations support a "Send To PMS from Visit Note" feature where you can use the “Send to PMS” button at the bottom of a visit note to send the billing information to your integrated PMS prior to signing the visit note. 2. Certain PMS integrations support the [Delayed Billing](How-to-set-up-Delayed-Billing.md) feature which allows you to hold your bills in [Billing Home](Billing-Home.md) and manually push them over to your integrated PMS whenever you choose.   **Important Note**: Consult your PMS User Manual to see which features your integrated PMS supports, if any. |
| What is Delayed Billing? | Turning on the Delayed Billing feature will allow you to push claims to your integrated PMS independent of signing the visit note. [Click here to learn more about the Delayed Billing feature.](How-to-set-up-Delayed-Billing.md)   - To send individual bills, click the Actions Menu  next to the bill in the Billing Home and select "Send to PMS". - To send bills in bulk, turn on the [Billing Home - Bulk Send to PMS](billing-settings---service-locations--procedure-codes.md#bulk_send_to_PMS) setting and then click on the "Bulk Send Bills to PMS" button at the top of Billing Home.   **Important Note**: Consult your PMS User Manual to see if it supports the Delayed Billing feature. |
| What is the 'Billing Home - Bulk Send to PMS' setting? | The **Billing Home - Bulk Send to PMS** setting will allow you to enable or disable the “Bulk Send Bills to PMS” button in Billing Home. - When toggled on, the “Bulk Send Bills to PMS” button allows you to bulk send ALL bills of a specific status to your integrated PMS. - When toggled off the “Bulk Send Bills to PMS” button will not be available and each bill will need to be sent to your integrated PMS individually via the Actions Menu .    [Click here to learn more about the 'Billing Home - Bulk Send to PMS' setting.](billing-settings---service-locations--procedure-codes.md#bulk_send_to_PMS) |
| What does the "Bulk Send Bills to PMS" button do? | The “Bulk Send Bills to PMS” button at the top of Billing Home allows you to send all bills of a specific status to your integrated PMS. The following three actions are available: - ”Send all Signed” - allows you to send all bills in the Signed status to your integrated PMS. - ”Resend all Sent to PMS” - allows you to send all bills in the Sent to PMS status to your integrated PMS. - ”Resend all Failed to send” - allows you to send all bills in the Failed to Send status to your integrated PMS. [Click here to learn more about the 'Billing Home - Bulk Send to PMS' setting.](billing-settings---service-locations--procedure-codes.md#bulk_send_to_PMS) |
| How do I send individual bills from a specific date range to my integrated PMS? | To send individual bills from a specific data range to your integrated PMS, use the date filter to filter by the date range you want to send and then click on the Actions Menu  next to the bill and select "Send to PMS". |
| How do I bulk send all the bills from a specific date range to my integrated PMS? | You cannot bulk send bills from a specific date range to your integrated PMS as the filters are not tied to the 'Bulk Send' feature. When you click the "Bulk Send" button, all bills of that status will be sent to your integrated PMS regardless of what filters you applied to Billing Home. |
| Do all CPT Codes sync to my integrated PMS? | Certain PMS Integrations might require you to enter the CPT Code in the PMS’s CPT Code database in order for it to sync from Elation. Please consult your PMS User Manual for full details on how to utilize Procedure codes while using an integrated PMS. |
| How many diagnosis codes can I send to my integrated PMS? | Certain PMS integrations may limit how many diagnosis codes they will accept. Please consult your PMS User Manual for full details about how many codes sync to your integrated PMS. |
| If I edit a bill in Elation after I send the billing information to my integrated PMS, will my integrated PMS receive the changes? | Elation’s PMS integrations are NOT built to receive edits after billing information is sent to the PMS. You must edit the bill/claim in both Elation EHR and your PMS. |
| If I edit a bill in my PMS, will Elation receive the changes? | No, edits made to a bill in the PMS will not update the corresponding billing details in Elation. |




## **Non-insurance billing**

| | |
| --- | --- |
| Can I use the Billing Form to create bills for my patient? | Yes, you can use the Billing Form and the Patient Invoicing feature to generate invoices and bills for services rendered. [Click here to learn more about Patient Invoicing](patient-invoicing.md). **Important Note**: The Patient Invoicing feature does not charge the patient. To create a payment request or charge the patient, please use our [Patient Payments feature](https://help.elationemr.com/s/article/using-elation-to-securely-collect-patient-payments), powered by Stripe. |
| Can I bill for services without using any codes? | If you are billing patients directly instead of their insurance for service, you can free text service names (ex. Quarterly Check Up or Records Copy) in the **Procedure** field and not enter any CPT codes or diagnosis codes. The **Procedure** field can store up to 20 characters. |
| How do I generate an invoice? | You can use the Patient Invoicing feature to generate and print invoices for services rendered. [Click here to learn more about Patient Invoicing](patient-invoicing.md). |
| How do I generate a superbill/receipt for the patient to send to their insurance company for reimbursement? | You can use the Patient Invoicing feature to generate a superbill/receipt for the patient to send to their insurance company for reimbursement. You can enter the amount the patient paid in the **Patient Payment** field in the Billing Form and then print a ‘Claims Invoice’ for your patient to share with their insurance company. [Click here to learn more about Patient Invoicing](patient-invoicing.md). |
| What should I do if part of a visit is payable by insurance and part of it is patient self-pay? | Since only one bill can be created for each visit note, include all of the necessary line-items for both insurance and self-pay in the Billing Form.   - In Elation, use the **Procedure** field to type in which line-items are self-pay.   - **User Tip**: Use a custom CPT Code or Procedure name (Ex. ‘SP99212’ or ‘Self Pay Follow Up’) to easily identity self pay services - After the billing details are transmitted to your PMS, remove self-pay items before submitting your claim. |