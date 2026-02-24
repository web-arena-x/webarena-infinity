# New York City- CIR- Immunization Registry Interface User Guide

Source: https://help.elationhealth.com/s/article/New-York-City-CIR-Immunization-Registry-Interface-User-Guide

---

To support the importance of promoting and prioritizing interoperability and exchange of patient immunization data across various healthcare platforms, Elation has established an electronic interface with the New York City Immunization Registry (CIR).


## **Contents**

- [What is the CIR Immunization Registry Interface?](#WhatIsCIRConnection)
- [Why is the CIR Immunization Registry Interface valuable?](#WhyIsConnectionValuable)
- [How to establish interface between Elation & CIR](#HowToEstablishConnection)
- [How to send vaccination data to CIR using Elation](#HowToSubmitData)
- [How to query for vaccination history/forecast using CIR](#HowToQuery)
- [Frequently Asked Questions (FAQ)](#FAQ)



## **What is the CIR Immunization Registry Interface?**

The CIR Immunization Registry Interface allows connected practices to send vaccination information from their Elation EHR directly to CIR, the New York City Immunization Registry. Practices can also query CIR for vaccination history or forecast.



## **Why is the CIR Immunization Registry Interface valuable?**

With the CIR Immunization Registry Interface, practices no longer need to separately log in to CIR to enter vaccination records for their patients. Once the vaccination is recorded in Elation during the patient encounter, the information can be sent immediately from the patient's chart in Elation to CIR. You can also pull vaccination history for specific patients from CIR to allow you to populate your patient's clinical profile and make informed decisions for administering vaccines. This interface saves you time and allows you to streamline your vaccination workflows.

###

## **How to establish interface between Elation & CIR**

The Elation Team will assist you with initiating an interface with WyIR. To notify us of your interest,

1. [Click here to fill out our contact form](https://app.elationemr.com/support/).
2. Select "I am a provider or staff member who uses Elation" for **What is your role?**
3. Select "Something else" for **Select an issue**.
4. Enter the following information in the **Details** field:
   - Which Immunization Registry do you want to connect to?
   - What CIR facility code(s) or PIN(s) has CIR provided to your organization?
     - You may search for your organization's CIR facility code(s) by logging into the CIR facility manager system here: CIR Facility Registration and Management. If this facility does not have a CIR facility code, please enroll the site in the facility manager system.
       - CIR facility codes may be in this format ####A## or #####A##.
       - CIR PINs may be four-digit code (####) or AA###
   - How many facilities are in your organization that administer vaccinations? For each facility, please provide the following information:
     - Point of contact name, title, email, and phone number
     - Facility CIR code
     - Address
     - Age range of patients receiving vaccinations (min to max age in years)
     - Is this site enrolled in Vaccines for Children (VFC)?
     - Funding type for the vaccine stock: 0-18 year old Public, 19+ Public, and/or Private
     - Type of vaccines administered: Childhood and adult vaccines, travel vaccine, influenza vaccine, COVID-19 vaccine, and/or Mpox vaccine
     - Average weekly volume of vaccines administered (excluding flu and COVID-19)
     - Does this facility have a CIR web portal account?
     - Does this site use CIR to manage vaccine inventory? If yes, which vaccine inventory is managed in CIR?: 0-18 year Public, 19+ Public, and/or Private
   - Does your practice already have a live CIR interface with another EHR?
5. Click "Next".
6. Click "No, I still need help" in the next window.
7. Print & fill out [this Confidentiality Statement](https://elation.my.salesforce.com/sfc/p/#37000000L9cg/a/1G0000019h6m/5DboH7EB7QCKSX3PQqwFUAelGRImyytIY.zG9KLV4go) & then click "Add Attachment" to share the completed file with us.
8. Click "Next".
9. Confirm your contact information and then click "Submit" to submit your request to Elation.




## **How to submit vaccination data to CIR using Elation**

You will use the Vaccine Form in the patient's chart to document the vaccination data and submit it the data to CIR. Learn more about how to use the Vaccine Form using the [Vaccination Documentation Guide](Vaccination-Form-Guide.md).

**Important Note**: Parent recall historical vaccinations are not accepted by CIR.

**User Tip**: All submissions are one-time only. If you need to edit any vaccination data after it is sent to the Immunization Registry, you will need to update the data in both the patient's chart and the Immunization Registry directly.




## **How to query for vaccination history/forecast using ASIIS**

You can query for vaccination history/forecast directly within a patient's chart by following the instructions listed in the ['*Querying for vaccination history and/or forecast using an Immunization Registry Interface*' section of the Vaccination Documentation Guide](Vaccination-Form-Guide.md#query_IR).


## **Frequently Asked Questions (FAQ)**

#### **How can I tell if the vaccination record was successfully submitted to the immunization registry?**

You can log into your State’s registry to review vaccination records submitted from Elation to the registry through the interface from time to time. If you have questions about a specific vaccination record, [please send the patient ID and the name of the immunization to the Support Team](https://help.elationhealth.com/s/contactsupport) and we can look into the vaccination record.

#### **How can I edit or delete a vaccination record from the registry using Elation?**

At this time, vaccination records submitted through Elation can only be edited or deleted within the registry. If you do make a change to or delete the vaccination record in the registry, we also recommend making the same change in Elation.

#### **I am running into errors when using the "Check Registry" or the "Check Forecast" buttons. What should I do?**

Follow the instructions in the ['*Managing querying errors*' section of the Vaccination Documentation Guide](Vaccination-Form-Guide.md#query_errors).

#### **Can I send immunization information electronically to NYSIIS (New York State Immunization Information System)?**

Yes, please review the [New York State- NYSIIS- Immunization Registry Interface User Guide](New-York-State-NYSIIS-Immunization-Registry-Interface-User-Guide.md) for more information about sending immunization information to NYSIIS. The NYSIIS interface is different from the CIR interface.




## **Related Articles**

- [Vaccination Documentation Guide](Vaccination-Form-Guide.md)