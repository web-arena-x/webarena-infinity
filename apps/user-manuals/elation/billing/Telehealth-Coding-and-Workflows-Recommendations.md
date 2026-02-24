# Telehealth: Billing & Workflow Recommendations

Source: https://help.elationhealth.com/s/article/Telehealth-Coding-and-Workflows-Recommendations

---

If your practice is exploring alternative methods to remotely check-in with your patients and evaluate their health, there are a number of telemedicine services that may be reimbursable by CMS and private payers. CMS specifically categorizes virtual services into 4 groups: telehealth visits, virtual check-ins, eVisits, and (new) telephone-only E/M.

In this article, we will cover the differences between each of these telemedicine services and how to bill for them.

## **Contents**

- [Telehealth Billing Decision Tree](#billingdecisiontree)
- [Telehealth waivers in place due to the COVID-19 public health emergency](#waivers)
- [Setting up your Elation account for telehealth](#Elationsettings)
- [Setting up your integrated billing system for telemedicine](#pmsSettings)
- [Types of virtual services](#typesofservices)
 - [Telehealth Visits](#TelehealthVisits)
 - [Virtual Check-ins](#VirtualCheckin)
 - [eVisits](#eVisits)
 - [Telephone-Only E/M](#TelephoneOnly)
- [Additional Resources from CMS](#Resources)

## **Telehealth Billing Decision Tree**

The below decision tree was designed to help you understand which virtual services your practice may be delivering today. For more information about each type of virtual service and the billing codes associated with each, please see the information at the bottom of this article.

![]()

## **Telehealth waivers in place due to the COVID-19 public health emergency**

The government has expanded Medicare’s telehealth benefits under the 1135 waiver authority, the Coronavirus Preparedness and Response Supplemental Appropriations Act, the Coronavirus Aid, Relief, and Economic Security (CARES) Act and CMS’ Interim Final Rule.

What does this mean for you?

- **Telehealth requirements for originating/distant site status of the physician and beneficiary waived.** Historical restrictions that prevented clinicians from being paid except under certain circumstances (ex. a patient must be from a rural area and present at an approved facility as the “originating site” of service) have now been lifted.
- **Telehealth reimbursement increased to be on par with in-person services.** As long as the COVID-19 Public Health Emergency (PHE) is in effect, clinicians can bill for telehealth services provided for dates of service starting March 6, 2020. Telehealth services are paid under the Physician Fee Schedule for the same amount as in-person services as long as the proper coding is submitted. See billing guidance below for more information about how to bill for facility vs. non-facility rates.
 - **User Tip:** These policies are based on CMS standards. Always double check with the policies designated by other Payers to ensure you are following their coding guidelines for telehealth services.
- **HIPAA regulations loosened.** The government is now allowing clinicians to use everyday technology (FaceTime, Skype, etc.) to interact with patients during the Public Health Emergency, in good faith that practices will continue to exercise caution under HIPAA.\*
- **Out-of-state providers do not need to be licensed in the state** where they are providing services if they are licensed in another state.\*
- **Telehealth and virtual check-in services can be provided to new patients.** To the extent that the 1135 waiver requires an established relationship, the HHS will not conduct audits to ensure that a prior relationship existed for claims submitted for telehealth visits during this public health emergency. Virtual check-ins may now be completed for new patients as opposed to only established beneficiaries. Note that the same does not apply to eVisits.
- **Remote staff supervision allowed.** Clinicians can supervise staff members virtually instead of needing to be on-site.
- **New telephone/audio-only E&M codes are now reimbursable by CMS.** For the duration of the COVID-19 Public Health Emergency, CMS will be reimbursing care provided via phone/audio-only using the following newly accepted CPT® codes: 98966-98968 for qualified non-physicians and 99441-99443 for physicians. These codes allow for a greater amount of time spent to be coded for at a higher reimbursement rate than the existing G2012 telephone-only code.

*\*Additional information applicable to the above waivers:*

- *The above updates apply to CMS Medicare FFS beneficiaries. Private payers may have specific coding requirements for telehealth, and states may have their own rules and regulations. Contact your state’s department of health or payer to confirm state- or payer- specific requirements.*
- *During the COVID-19 public health emergency, some states and payers are allowing telemedicine services to be provided via audio only/telephone. An example of this is California - where the Department of Managed Health Care released an [all payer letter](http://www.dmhc.ca.gov/Portals/0/Docs/OPL/APL%2020-009%20(OPL)%20-%20Reimbursement%20for%20Telehealth%20Services%20(3_18_20).pdf?ver=2020-03-18-105612-547) (and this follow up [letter](https://cts.vresp.com/c/?PBGH/a419d7e414/cbe69ed1e8/94289e51dd/ver=2020-04-07-093820-233)) stating that audio visits will be reimbursed the same as in-person E&M, provided requirements are met for care delivery. Contact your state’s department of health or payer to confirm state-specific requirements.*
- *States may have their own requirements protection of healthcare data and licensure requirements.*

## **Setting up your Elation account for telehealth**

To learn more about how you can use Elation to deliver care for your patients through telemedicine with minimal disruption to care delivery and to the financial health of your practice, please see our step-by-step guide [here](https://docsend.com/view/g85h4xn). This guide covers how to complete a patient encounter through telemedicine and how to set-up your Elation account to support this.

Below are several quick set-up steps that you can take in your Elation account today so that you can begin seeing patients and billing for telehealth services:

| **Category** | **Set-up Step** | **Why?** |
| --- | --- | --- |
| Appointments | [Create a telehealth appointment type\*](calendar-and-booking-settings.md#appt_types) | Easily see which appointments on your calendar are telehealth |
| [Set-up your booking site](Patient-Booking-Site.md) | Allow your patients to self-schedule based on your availability for convenience and time-savings |
| [Enable appointment reminders](appointment-reminders.md) | Save your practice time by automating appt reminders to your patients |
| Completing the encounter | Use your Elation supplied HIPPA-compliant [Zoom](Elation-Telehealth-powered-by-Zoom.md)® account. | The Elation-Zoom integration is covered under a Business Associate Agreement and fully HIPPAA compliant. |
| Documentation | [Create a telehealth, phone and/or eVisit visit note category](https://help.elationhealth.com/s/article/visit-note-types). Tie this to your telehealth appointment type! | Label your visits by type in the chronological order for easy search capabilities |
| FFS Billing | [Create service locations as needed (POS 10 for home, POS 2 for non-home)](billing-settings---service-locations--procedure-codes.md)    (See the [Telehealth visits requirement](#TelehealthVisits) below for more details) | For proper claim submission. |
| [Add telehealth CPT codes](billing-settings---service-locations--procedure-codes.md) | For easy search capability within the visit note and bill, and for proper claim submission |
| [Collect patient responsibility digitally from patients](using-elation-to-securely-collect-patient-payments.md) (optional) | For collection of patient responsibility using Elation's secure-payment collection integration powered by Stripe®. |
| [Enable patient invoicing](patient-invoicing.md) (optional) | To enable easy generation of invoices for your patients to submit to their insurance company for reimbursement (if you are collecting payment upfront) |
| Non-Member / Flat-Fee Billing | Create a rate for telehealth visits | Establish your rate for these services |
| [Create a mechanism to track non-member patients](adding-patient-tags.md) (ie. patient tag) | Easily track which patients will be billed via flat-fee |
| Passport | Set up Passport and communicate with your patients via Passport.   - [Invite your patients to Patient Passport](https://help.elationemr.com/s/article/elation-patient-passport-an-introduction#howdoigetstarted) - [Enable “Patient Initiated Messages”](elation-patient-passport-an-introduction.md#7) and adjust your message routing settings - [Send individual messages to your patient via “Patient Letters”](elation-patient-passport-an-introduction.md#3) - [Send bulk messages to your patient panel via “Bulk Letters”](introduction-to-bulk-letters.md) | Use Passport as a secure method to communicate with your patients. Allow patients to initiate messages to your practice, which may be reimbursable virtual services. |



## **Setting up your integrated billing system for telemedicine**

Our team has created resources that will guide you through the necessary settings page updates to bill for telehealth. Each guide linked below provides detailed step-by-step instructions to ensure that your practice can successfully send telehealth charges from Elation to your integrated practice management system (PMS).

- [Kareo](Setting-up-your-Elation-account-for-telehealth.md#Kareo)
- [Akamai](Setting-up-your-Elation-account-for-telehealth.md#Akamai)
- [CollaborateMD](Setting-up-your-Elation-account-for-telehealth.md#CollaborateMD)
- [Practice Suite](Setting-up-your-Elation-account-for-telehealth.md#PracticeSuite)
- [ConnxtMD](Setting-up-your-Elation-account-for-telehealth.md#ConnxtMD)
- [AdvancedMD](Setting-up-your-Elation-account-for-telehealth.md#AdvancedMD)
- [HealthBiller](Setting-up-your-Elation-account-for-telehealth.md#HealthBiller)

## **Types of Virtual Services**

Breakdown of Virtual Service Types & Requirements

![]()

### **Telehealth Visits**

Telehealth visits are full-visits which require audio-visual, real-time, two-way interactive communication systems. Out of the three types of virtual services covered in this help center article (telehealth, virtual check-ins, eVisits), telehealth visits typically provide the highest reimbursement rate for Medicare/Medicaid. You can use Elation's HIPAA-compliant, [integrated video](Elation-Telehealth-powered-by-Zoom.md) feature powered by Zoom to complete your telehealth visits. See table above for additional requirements of Telehealth Visits.

**Important Notes:**

- CMS’ updated coding recommendation to earn the proper reimbursement rates, as of 1/1/2022, is to use the 99202-99205, 99211-99215 or CMS AWV G0438-G0439 codes + a 95 modifier + the POS code for the location where the patient received health related services
 - *POS 02: Telehealth Provided Other than in Patient’s Home:*The location where health services and health related services are provided or received, through telecommunication technology. Patient is not located in their home when receiving health services or health related services through telecommunication technology.
 - *POS 10: Telehealth Provided in Patient’s Home:*The location where health services and health related services are provided or received through telecommunication technology. Patient is located in their home (which is a location other than a hospital or other facility where the patient receives care in a private residence) when receiving health services or health related services through telecommunication technology.
- Previously, CMS’ recommendation was to use these CPT codes with modifier 95 + POS 02 (telehealth).

**User Tip:** These policies are based on CMS standards. We recommend confirming telehealth coding requirements with each Payer before you submit your claims.

### **Virtual Check-ins**

Virtual Check-ins are reimbursable services for brief communications between providers and patients for specific purposes. These services are not restricted by originating site and other Medicare telehealth regulations. They can be provided when patients are in their homes, regardless of public health emergency declaration. These services can be rendered via telephone, email, or Elation’s Patient Passport.

While Virtual Check-ins must be patient initiated, providers can let patients know that they can reach out through this method to receive care, and patients may agree to change a previously scheduled face-to-face visit to a virtual encounter. Time spent should be documented in the note, and information that can be stored and shared should be stored in the patient’s electronic health record.  See table above for additional requirements of Virtual Check-ins.

Billable codes and CMS Physician Fee Schedule Non-Facility estimated prices are listed below. Please note that these reimbursement rates may differ based on your locality for Medicare. Please check your health plan provider network representative for accepted codes and contracted rates, as coding requirements may differ by payer.

| Communication Method | Code | Estimated Reimbursement\* |
| --- | --- | --- |
| Phone call (audio only) | G2012 | $14.80 |
| Image or video submitted by patient reviewed | G2010 | $12.27 |




### **eVisits**

eVisits are reimbursable services that occur between an established patient and their provider through an online HIPAA-compliant portal, like Elation Passport. These services are not restricted by originating site and other Medicare telehealth regulations. They can be provided when patients are in their homes, regardless of public health emergency declaration.

eVisits must include clinical decision making and evaluation, assessment and management that would have otherwise been provided in the office. Simply responding to the portal or secure email messages does not qualify as a billable service.

While eVisits must be patient initiated, providers can let patients know that they can reach out through this method to receive care, and patients may agree to change a previously scheduled face-to-face visit to a virtual encounter. Time spent should be documented in the note, and information that can be stored and shared should be stored in the patient’s electronic health record.  See table above for additional requirements of eVisits.

Billable codes and CMS Physician Fee Schedule Non-Facility estimated prices are listed below. Please note that these reimbursement rates may differ based on your locality for Medicare. Please check your health plan provider network representative for accepted codes and contracted rates, as coding requirements may differ by payer.

| Requirement | Code | Estimated Reimbursement\* |
| --- | --- | --- |
| 5-10 min | 99421 | $15.52 |
| 11-20 min | 99422 | $31.04 |
| 21+ min | 99423 | $50.16 |
| Qualified nonphysician, 5-10 min | G2061 | $12.27 |
| Qualified nonphysician, 11-20 min | G2062 | $21.65 |
| Qualified nonphysician, 21+ min | G2063 | $33.92 |




### **Telephone-Only E/M**

Telephone-only E/M codes are newly reimbursable services (for the extent of the COVID-19 public health emergency only) that occur between a patient and their provider through an audio-only/telephone call. The codes require assessment and management of a problem over the phone and require medical necessity to be billable. These codes allow for a greater amount of time spent to be coded for at a higher reimbursement rate than the existing G2012 telephone-only code for a Virtual Check-in. See table above for additional requirements of these telephone-only E/M codes.

Under CMS’ interim final rule, Medicare is also extending the definition of qualified non-physician practitioner for the CPT codes 98966-98968 to include LCSWs, clinical psychologists, physical therapists, occupational therapists, and speech language pathologists -- when the visit pertains to a service within the benefit category of those practitioners. These telephone E/M services may also be provided to family/guardians of Medicare beneficiaries, regarding the care of the beneficiary.

Billable codes are listed below. Please check your health plan provider network representative for accepted codes and contracted rates, as coding requirements may differ by payer.

| Requirement | Code |
| --- | --- |
| Physician, 5-10 min | 99441 |
| Physician, 11-20 min | 99442 |
| Physician, 21-30 min | 99443 |
| Qualified nonphysician, 5-10 min | 98966 |
| Qualified nonphysician, 11-20 min | 98967 |
| Qualified nonphysician, 21-30 min | 98968 |




*\*This article is provided for instructional purposes only. Elation Health does not support or guarantee anything other than relay useful information from various organizations. Elation Health also does not provide support for third-party technologies. We recommend consulting your coding guidelines or* AMA *for the most up to date information.*

*CPT copyright 2022 American Medical Association. All rights reserved.* *Copyright ©2022 Zoom Video Communications, Inc. All rights reserved.
© 2022 Stripe, Inc. All rights reserved.*

## **Additional Resources from CSM**

- [2022 Medicare Physician Fee Schedule Final Rule](https://www.cms.gov/newsroom/fact-sheets/calendar-year-cy-2022-medicare-physician-fee-schedule-final-rule)
- [New/Modifications to the Place of Service (POS) Codes for Telehealth](https://www.cms.gov/files/document/mm12427-newmodifications-place-service-pos-codes-telehealth.pdf)
- [AMA special coding advice during COVID-19 public health emergency](https://www.ama-assn.org/system/files/covid-19-coding-advice.pdf)
- [COVID-19 Frequently Asked Questions on Medicare Fee-for-Service Billing](https://www.cms.gov/files/document/03092020-covid-19-faqs-508.pdf)

## **Related Articles**

- [Adding Patient Tags](adding-patient-tags.md)
- [Automated Appointment Reminders](appointment-reminders.md)
- [Getting started with Patient Passport](elation-patient-passport-an-introduction.md)
- [How to set up Patient Invoicing](patient-invoicing.md)
- [How to set up your Elation Calendar](calendar-and-booking-settings.md)
- [How to set up your Patient Booking Site](Patient-Booking-Site.md)
- [Elation Integrated Video- Connecting with patients using video](Elation-Telehealth-powered-by-Zoom.md)
- [Visit Note Types](visit-note-categories.md)