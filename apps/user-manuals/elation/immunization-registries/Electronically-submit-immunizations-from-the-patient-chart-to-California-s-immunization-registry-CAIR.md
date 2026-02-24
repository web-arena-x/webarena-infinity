# California State- CAIR- Immunization Registry Interface User Guide

Source: https://help.elationhealth.com/s/article/Electronically-submit-immunizations-from-the-patient-chart-to-California-s-immunization-registry-CAIR

---

To support the importance of promoting and prioritizing interoperability and exchange of patient immunization data across various healthcare platforms, Elation has established an electronic interface with the California State Immunization Registry known as CAIR.

## **Contents**

- [What is the CAIR Immunization Registry Interface?](#WhatIsCAIRConnection)
- [Why is the CAIR Immunization Registry Interface valuable?](#WhyIsConnectionValuable)
- [How to establish interface between Elation & CAIR](#HowToEstablishConnection)
 - [(New to CAIR) Register to submit immunizations electronically via Elation](#new_register)
 - [(Existing CAIR User) Register to submit immunizations electronically via Elation](#existing_register)
- [How to send vaccination data to CAIR using Elation](#HowToSubmitData)
- [How to query for vaccination history/forecast using CAIR](#HowToQuery)
- [Frequently Asked Questions (FAQ)](#faq)

##

## **What is the CAIR Immunization Registry Interface?**

The CAIR Immunization Registry Interface allows connected practices to send vaccination information from their Elation EHR directly to CAIR- the California Immunization Registry. Practices can also query CAIR for vaccination history or forecast.

## **Why is the CAIR Immunization Registry Interface valuable?**

With the CAIR Immunization Registry Interface, practices no longer need to separately log in to CAIR to enter vaccination records for their patients. Once the vaccination is recorded in Elation during the patient encounter, the information can be sent immediately from the patient's chart in Elation to CAIR. You can also pull vaccination history for specific patients from CAIR to allow you to populate your patient's clinical profile and make informed decisions for administering vaccines. This interface saves you time and allows you to streamline your vaccination workflows.

###

## **How to establish interface between Elation & CAIR**

The Elation Team will assist you with initiating an interface with CAIR. First you must notify CAIR of your intent to connect electronically via Elation EHR via one of the steps below. After you have notified CAIR, please [click here to fill out our contact form](https://help.elationhealth.com/s/contactsupport), select "Immunization Registry" as the *Request Type*, and send the following information to Elation:

- Your CAIR Site ID for each office location

### **(New to CAIR) Register to submit immunizations electronically via Elation**

1. Navigate directly to the [CAIR registration page](https://igs.cdph.ca.gov/CAIR/Provider/Register).
2. Under *Site intends to* section, choose the second option, that your Site intends to “Submit immunization data through a Sending Facility.” (A “Sending Facility” is a vendor like Elation that submits records on your behalf.)
3. You will then be prompted to enter the “Sending Facility ID of your Data Submitter.” Elation’s Sending Facility ID is *SF-001728*.![]()
4. Complete the required fields about your practice and your practice’s contact information (fields in red text are required for registration).

   ![]()
5. Under “Data Exchange Information”, enter the following information:

   - What is the name (+version) of the EMR/EHR software used by this office? ElationEMR v3
   - Which vendor developed the EMR/EHR software used by this office? Elation Health
   - Is this EHR/EHR Certified? YES
   - Can this EMR/EHR send HL7 formatted data? YES
   - DE/Vendor Contact First Name: Elation
   - DE/Vendor Contact Last Name: Support
   - Company: Elation Health
   - Position: (Leave blank)
   - Phone: 415-231-5178
   - Email: [integrations@elationhealth.com](mailto:integrations@elationhealth.com)
   - Retype Email: [integrations@elationhealth.com](mailto:integrations@elationhealth.com)

1. Click "Continue" and review the CAIR Organization Access & Confidentiality Agreement. If you have reviewed the information and wish to continue,
   1. Check the box to agree that your Organization will abide CAIR rules.
   2. Enter the name of your Organization Representative
   3. Enter the title of your Organization Representative
   4. Click "Complete Site Registration"![]()

### **(Existing CAIR User) Register to submit immunizations electronically via Elation**

If you are already registered with CAIR and have your CAIR ID, you can log into the [CAIR IZ Portal](https://igs.cdph.ca.gov/cair/) using your CAIR ID and zip code.

- **User Tip**: If you are not sure what your CAIR ID is or your zip code is not working with your CAIR ID, you will need to contact [CAIRDataExchange@cdph.ca.gov](mailto:CAIRDataExchange@cdph.ca.gov) or 800-578-7889 for assistance.

Once logged in, you can complete a form to notify CAIR you would like to start submitting immunization data electronically via Elation EHR. Under “Data Exchange Information”, enter the following information:

- What is the name (+version) of the EMR/EHR software used by this office? ElationEMR v3
- Which vendor developed the EMR/EHR software used by this office? Elation Health
- Is this EHR/EHR Certified? YES
- Can this EMR/EHR send HL7 formatted data? YES
- DE/Vendor Contact First Name: Elation
- DE/Vendor Contact Last Name: Support
- Company: Elation Health
- Position: (Leave blank)
- Phone: 415-231-5178
- Email: [integrations@elationhealth.com](mailto:integrations@elationhealth.com)
- Retype Email: [integrations@elationhealth.com](mailto:integrations@elationhealth.com)

###

## **How to submit vaccination data to CAIR using Elation**

You will use the Vaccine Form in the patient's chart to document the vaccination data and submit it the data to CAIR. Learn more about how to use the Vaccine Form using the [Vaccination Documentation Guide](Vaccination-Form-Guide.md).

**User Tip**: All submissions are one-time only. If you need to edit any vaccination data after it is sent to the Immunization Registry, you will need to update the data in both the patient's chart and the Immunization Registry directly.

## **How to query for vaccination history/forecast using CAIR**

You can query for vaccination history/forecast directly within a patient's chart by following the instructions listed in the ['*Querying for vaccination history and/or forecast using an Immunization Registry Interface*' section of the Vaccination Documentation Guide](Vaccination-Form-Guide.md#query_IR).

## **Frequently Asked Questions (FAQ)**

##

#### **How can I tell if the vaccination record was successfully submitted to the immunization registry?**

You can log into your State’s registry to review vaccination records submitted from Elation to the registry through the interface from time to time. If you have questions about a specific vaccination record, [please send the patient ID and the name of the immunization to the Support Team](https://help.elationhealth.com/s/contactsupport) and we can look into the vaccination record.

#### **How can I edit or delete a vaccination record from the registry using Elation?**

At this time, vaccination records submitted through Elation can only be edited or deleted within the registry. If you do make a change to or delete the vaccination record in the registry, we also recommend making the same change in Elation.

##

#### **I am running into errors when using the "Check Registry" or the "Check Forecast" buttons. What should I do?**

Follow the instructions in the ['*Managing querying errors*' section of the Vaccination Documentation Guide](Vaccination-Form-Guide.md#query_errors).

#### **How do I use the CAIR IZ Portal?**

[This is a helpful video on manually documenting vaccinations in CAIR2](https://www.youtube.com/watch?v=guH29UKtQE4) and [this is the User Guide](http://cairweb.org/docs/CAIR2RegularUserGuide_092616.pdf). You can also contact CAIR at 800-578-7889, Hours: 9am-4pm Monday to Thursday, 10am-4pm Friday or at [CAIRHelpdesk@cdph.ca.gov](mailto:CAIRHelpdesk@cdph.ca.gov).

#### **How do I know if I am registered with CAIR? How do I find my CAIR ID?**

If you have registered with CAIR using the [CAIR2 IZ Portal Registration form](https://igs.cdph.ca.gov/CAIR/Provider/Register) before, you may log into the [CAIR2 IZ Portal Login](https://igs.cdph.ca.gov/cair/) using your CAIR ID and zip code to confirm your site is registered to submit immunizations electronically to CAIR.

If you are not sure what your CAIR ID is or your zip code is not working with your CAIR ID, you will need to contact [CAIRDataExchange@cdph.ca.gov](mailto:CAIRDataExchange@cdph.ca.gov) or 800-578-7889 for assistance.

## **Related Articles**

- [Vaccination Documentation Guide- Managing vaccination information](Vaccination-Form-Guide.md)