# North Carolina State- NCIR- Immunization Registry Interface User Guide

Source: https://help.elationhealth.com/s/article/North-Carolina-State-NCIR-Immunization-Registry-Interface-User-Guide

---

To support the importance of promoting and prioritizing interoperability and exchange of patient immunization data across various healthcare platforms, Elation has established an electronic interface with the North Carolina State State Immunization Registry known as NCIR.

## **Contents**

- [What is the NCIR Immunization Registry Interface?](https://elation.lightning.force.com/lightning/r/Knowledge__kav/ka06O000000FY1fQAG/view#WhatIsFLSHOTSConnection)
- [Why is the NCIR Immunization Registry Interface valuable?](https://elation.lightning.force.com/lightning/r/Knowledge__kav/ka06O000000FY1fQAG/view#WhyIsConnectionValuable)
- [How to establish interface between Elation & NCIR](https://elation.lightning.force.com/lightning/r/Knowledge__kav/ka06O000000FY1fQAG/view#HowToEstablishConnection)
- [How to send vaccination data to NCIR using Elation](https://elation.lightning.force.com/lightning/r/Knowledge__kav/ka06O000000FY1fQAG/view#HowToSubmitData)
- [How to query for vaccination history/forecast using NCIR](#HowToQuery)
- [Frequently Asked Questions (FAQ)](https://elation.lightning.force.com/lightning/r/Knowledge__kav/ka06O000000FY1fQAG/view#FAQ)

## **What is the NCIR Immunization Registry Interface?**

The NCIR Immunization Registry Interface allows connected practices to send vaccination information from their Elation EHR directly to NCIR, the North Carolina State Immunization Registry. Practices can also query NCIR for vaccination history or forecast.



## **Why is the NCIR Immunization Registry Interface valuable?**

With the NCIR Immunization Registry Interface, practices no longer need to separately log in to NCIR to enter vaccination records for their patients. Once the vaccination is recorded in Elation during the patient encounter, the information can be sent immediately from the patient's chart in Elation to NCIR. You can also pull vaccination history for specific patients from NCIR to allow you to populate your patient's clinical profile and make informed decisions for administering vaccines. This interface saves you time and allows you to streamline your vaccination workflows.

###

## **How to establish interface between Elation & NCIR**

The Elation Team will assist you with initiating interface with NCIR. To begin the process, you will need to

1. Register for intent with NCIR.
2. Complete an NCIR Provider Agreement. [Click here](https://elation.my.salesforce.com/sfc/p/37000000L9cg/a/6O000000IB1P/dJCttYCkQmTUz4OAxwtSPBWorxRdWOvnO6bApBnUWwg) to download a copy of the agreement.

To register for intent with NCIR, login to your NCIR account by [clicking here](https://idpprod.nc.gov:8443/nidp/idff/sso?id=6&sid=0&option=credential&sid=0&target=https%3A%2F%2Fncid.nc.gov%2FLAGBroker%3F%2522https%3A%2F%2Fncdphmeaningfuluse.org%2Fmup%2Fpublic%2Flogin.action%2522) and then clicking "Start Registration". [Click here](https://ncdphmeaningfuluse.org/NC_RegistrationofIntent_UserGuide.pdf) to view a guide on how to register for intent on the NCIR website. Use the information below to fill out the registration- answers are in italics:

- Please select the EHR Vendor for this provider: *Other*
- Other Vendor: *Elation Health*
- Product name: *ElationEMR*
- Software version: *3*
- Is your EHR capable of sending 2.5.1 transactions?: *Yes*
- Which of the following interfaces are you planning to implement?: *Update transaction (HL7 2.5 VXU/ACK)*
- Does your EHR support real-time messaging using web services?: *Yes*
- Do you have a hub through which all your organizations will send data, so that a single connection can be made to NCIR?: *Yes*
- Do you have a test environment?: *Yes*
- Please provide the name of the person who will be the primary contact for addressing errors/rejects in HL7 messages: *[escalations@elationhealth.com](mailto:escalations@elationhealth.com)*
- Are you planning to connect directly with the NCIR or go through the NC HIE?: *Direct*
- How adaptable is the software being used? are you able to change aspects of the software for NCIR requirements, if needed?: *Yes*
- Is your EHR capable of creating VXU 2.5.1 messages?: *Yes*
- Is your EHR capable of accepting and processing ACK HL7 2.5.1 messages?: *Yes*
- Is your EHR capable of creating 2.5.1 QBP messages and accept resulting RSP messages?: *No*
- How does your application handle reporting errors/warnings (ACKs returned in response to VXU)?: *Regularly reviews and investigates ACK errors*

Once you have completed the two steps above, [click here to fill out our contact form](https://help.elationhealth.com/s/contactsupport) and select "Immunization Registry" as the *Request Type*. A member of the Elation team will collect the completed NCIR Provider Agreement from you.




## **How to submit vaccination data to NCIR using Elation**

You will use the Vaccine Form in the patient's chart to document the vaccination data and submit it the data to NCIR. Learn more about how to use the Vaccine Form using the [Vaccination Documentation Guide](Vaccination-Form-Guide.md).

**User Tip**: All submissions are one-time only. If you need to edit any vaccination data after it is sent to the Immunization Registry, you will need to update the data in both the patient's chart and the Immunization Registry directly.



## **How to query for vaccination history/forecast using NCIR**

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