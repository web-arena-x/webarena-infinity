# Michigan State- MCIR- Immunization Registry Interface User Guide

Source: https://help.elationhealth.com/s/article/Michigan-State-MCIR-Immunization-Registry-Interface-User-Guide

---

To support the importance of promoting and prioritizing interoperability and exchange of patient immunization data across various healthcare platforms, Elation has established an electronic interface with the Michigan State Immunization Registry (MCIR).


## **Contents**

- [What is the MCIR Immunization Registry Interface?](#WhatIsMCIRConnection)
- [Why is the](#WhyIsConnectionValuable) [MCIR](#WhatIsASIISConnection) [Immunization Registry Interface valuable?](#WhyIsConnectionValuable)
- [How to establish interface between Elation &](#HowToEstablishConnection) [MCIR](#WhatIsASIISConnection)
- [How to send vaccination data to](#HowToSubmitData) [MCIR](#WhatIsASIISConnection) [using Elation](#HowToSubmitData)
- [How to query for vaccination history/forecast using](#HowToQuery) [MCIR](#WhatIsASIISConnection)
- [Frequently Asked Questions (FAQ)](#FAQ)

## **What is the MCIR Immunization Registry Interface?**

The MCIR Immunization Registry Interface allows connected practices to send vaccination information from their Elation EHR directly to MCIR, the Michigan State Immunization Registry known as Michigan Care Improvement Registry. Practices can also query MCIR for vaccination history or forecast.



## **Why is the MCIR Immunization Registry Interface valuable?**

With the MCIR Immunization Registry Interface, practices no longer need to separately log in to MCIR to enter vaccination records for their patients. Once the vaccination is recorded in MCIR during the patient encounter, the information can be sent immediately from the patient's chart in Elation to MCIR. You can also pull vaccination history for specific patients from MCIR to allow you to populate your patient's clinical profile and make informed decisions for administering vaccines. This interface saves you time and allows you to streamline your vaccination workflows.

###

## **How to establish interface between Elation & MCIR**

The Elation Team will assist you with initiating interface with MCIR. To notify us of your interest, please follow the instructions below:

1. Register with [Michigan Health System Testing Repository](https://mimu.michiganhealthit.org/)
   1. Follow the instructions listed in this guide: <https://michiganhealthit.org/wp-content/uploads/HSTRUserGuide.pdf>
   2. Make sure the following information is filled in during the registration process:
      - *Registration Type:* **Professional**
      - *HL7 version:* **2.5.1** *Is EHR configured to capture the MCIR HL7 fields?:* **Yes**
      - *Does this Registration participate with MAPS?* MAPS is the Michigan Prescription Monitoring Program (PMP). **You should indicate Yes if your team has a MAPS login.**
      - *Our EHR System is:* **Elation Health**
      - *EHR Vendor:* **Elation Health**
      - *EHR Product / Version:* **ElationEMR v3**
      - *EHR Implementation Date:* **the date you started using Elation**
2. [Click here to fill out our contact form](https://help.elationhealth.com/s/contactsupport), select "Immunization Registry" as the *Request Type*, and send the following information to Elation:

- Does your practice participate in VFC? If so, what is your VFC PIN?
- What is your MCIR site ID number? You can follow [these instructions](https://www.mcir.org/wp-content/uploads/2014/08/Finding-Site-ID-Number.pdf) to find your MCIR ID.
- Who will be the point of contact for this interface setup? Please also provide a backup contact (backup required by MCIR).
- Does your practice administer vaccines? Do you have any other physical locations that administer vaccines?
- ​​​​​​​Does your practice have a relationship with MiHIN (Michigan Health Information Network)?

## **How to submit vaccination data to MCIR using Elation**

You will use the Vaccine Form in the patient's chart to document the vaccination data and submit it the data to MCIR. Learn more about how to use the Vaccine Form using the [Vaccination Documentation Guide](Vaccination-Form-Guide.md).

**User Tip**: All submissions are one-time only. If you need to edit any vaccination data after it is sent to the Immunization Registry, you will need to update the data in both the patient's chart and the Immunization Registry directly.



## **How to query for vaccination history/forecast using MCIR**

You can query for vaccination history/forecast directly within a patient's chart by following the instructions listed in the ['*Querying for vaccination history and/or forecast using an Immunization Registry Interface*' section of the Vaccination Documentation Guide](Vaccination-Form-Guide.md#query_IR).



## **Frequently Asked Questions (FAQ)**

#### **How can I tell if the vaccination record was successfully submitted to the immunization registry?**

You can log into your State’s registry to review vaccination records submitted from Elation to the registry through the interface from time to time. If you have questions about a specific vaccination record, [please send the patient ID and the name of the immunization to the Support Team](https://help.elationhealth.com/s/contactsupport) and we can look into the vaccination record.

#### **How can I edit or delete a vaccination record from the registry using Elation?**

At this time, vaccination records submitted through Elation can only be edited or deleted within the registry. If you do make a change to or delete the vaccination record in the registry, we also recommend making the same change in Elation.


#### **I am running into errors when using the "Check Registry" or the "Check Forecast" buttons. What should I do?**

Follow the instructions in the ['*Managing querying errors*' section of the Vaccination Documentation Guide](Vaccination-Form-Guide.md#query_errors).


## **Related Articles**

- [Vaccination Documentation Guide](Vaccination-Form-Guide.md)