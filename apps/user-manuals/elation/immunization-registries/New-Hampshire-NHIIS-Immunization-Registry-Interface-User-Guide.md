# New Hampshire - NHIIS - Immunization Registry Interface User Guide

Source: https://help.elationhealth.com/s/article/New-Hampshire-NHIIS-Immunization-Registry-Interface-User-Guide

---

To support the importance of promoting and prioritizing interoperability and exchange of patient immunization data across various healthcare platforms, Elation has established an electronic interface with the New Hampshire State Immunization Registry known as NHIIS.

## **Contents**

- [What is the NHIIS Immunization Registry Interface?](#WhatIsNHIISConnection)
- [Why is the NHIIS Immunization Registry Interface valuable?](#WhyIsConnectionValuable)
- [How to establish interface between Elation & NHIIS](#HowToEstablishConnection)
- [How to send vaccination data to NHIIS using Elation](#HowToSubmitData)
- [How to query for vaccination history/forecast using NHIIS](#HowToQuery)
- [Frequently Asked Questions (FAQ)](#FAQ)

## **What is the NHIIS Immunization Registry Interface?**

The NHIIS Immunization Registry Interface allows connected practices to send vaccination information from their Elation EHR directly to NHIIS, the New Hampshire Immunization Information System. Practices can also query NHIIS for vaccination history or forecast.


## **Why is the NHIIS Immunization Registry Interface valuable?**

With the NHIIS Immunization Registry Interface, practices no longer need to separately log in to NHIIS to enter vaccination records for their patients. Once the vaccination is recorded in Elation during the patient encounter, the information can be sent immediately from the patient's chart in Elation to NHIIS. You can also pull vaccination history for specific patients from NHIIS to allow you to populate your patient's clinical profile and make informed decisions for administering vaccines. This interface saves you time and allows you to streamline your vaccination workflows.

###

## **How to establish interface between Elation & NHIIS**

The Elation Team will assist you with initiating an interface with NHIIS. To notify us of your interest,

1. [Click here to fill out our contact form](https://app.elationemr.com/support/)
2. Select "I am a provider or staff member who uses Elation" for **What is your role?**
3. Select "Something else" for **Select an issue**
4. Enter the following information in the **Details** field:
   - Which Immunization Registry would you like to connect to?
   - Does your practice participate in Vaccines for Children (VFC)? If so, what is your VFC pin?
   - Does your practice serve pediatrics and adolescents only (0-18 years) only, adults only (18+ years), or all ages?
   - What are the average number of administered vaccines per year for each group?
   - Who is the primary practice decision maker and who is the primary point of contact for onboarding?
5. Click "Next".
6. Click "No, I still need help" in the next window.
7. Click "Next".
8. Confirm your contact information and then click "Submit" to submit your request to Elation.




## **How to submit vaccination data to NHIIS using Elation**

You will use the Vaccine Form in the patient's chart to document the vaccination data and submit it the data to NHIIS. Learn more about how to use the Vaccine Form using the [Vaccination Documentation Guide](Vaccination-Form-Guide.md).

**Important Notes**: In order to submit vaccination data to NHIIS, the following details are required for patients and vaccines:

- Store the **Race** and **Ethnicity** for ALL patients in their [Patient Demographics](https://help.elationemr.com/s/article/Patient-Demographics-Guide).
- Store the **Emergency Contact** information in the [Patient Demographics](https://help.elationemr.com/s/article/Patient-Demographics-Guide) for patients 18 years and younger.
- Type the “Unit of sale” NDC (rather than “unit of use” NDC) in the **NDC #** field of the Vaccination Form.
 - For some vaccines, there are differences between the NDC on the vial/syringe and on the box. NHIIS must have the unit of sale NDC from the box. If you do not have the box or packaging, NHIIS recommends utilizing [this CDC NDC crosswalk site](https://www2a.cdc.gov/vaccines/iis/iisstandards/vaccines.asp?rpt=ndc) to determine the appropriate unit of sale NDC.

**User Tip**: All submissions are one-time only. If you need to edit any vaccination data after it is sent to the Immunization Registry, you will need to update the data in both the patient's chart and the Immunization Registry directly.




## **How to query for vaccination history/forecast using NHIIS**

You can query for vaccination history/forecast directly within a patient's chart by following the instructions listed in the ['*Querying for vaccination history and/or forecast using an Immunization Registry Interface*' section of the Vaccination Documentation Guide](Vaccination-Form-Guide.md#query_IR).



## **Frequently Asked Questions (FAQ)**

#### **How can I tell if the vaccination record was successfully submitted to the immunization registry?**

You can log into your State’s registry to review vaccination records submitted from Elation to the registry through the interface from time to time. If you have questions about a specific vaccination record, [please send the patient ID and the name of the immunization to the Support Team](https://help.elationhealth.com/s/contactsupport) and we can look into the vaccination record.

#### **How can I edit or delete a vaccination record from the registry using Elation?**

At this time, vaccination records submitted through Elation can only be edited or deleted within the registry. If you do make a change to or delete the vaccination record in the registry, we also recommend making the same change in Elation.

#### **I am running into errors when using the "Check Registry" or the "Check Forecast" buttons. What should I do?**

Follow the instructions in the [*'Managing querying errors'* section of the Vaccination Documentation Guide](Vaccination-Form-Guide.md#query_errors).

## **Related Articles**

- [Vaccination Documentation Guide](Vaccination-Form-Guide.md)