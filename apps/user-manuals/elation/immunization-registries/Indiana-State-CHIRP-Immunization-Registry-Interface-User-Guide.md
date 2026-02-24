# Indiana State- CHIRP- Immunization Registry Interface User Guide

Source: https://help.elationhealth.com/s/article/Indiana-State-CHIRP-Immunization-Registry-Interface-User-Guide

---

To support the importance of promoting and prioritizing interoperability and exchange of patient immunization data across various healthcare platforms, Elation has established an electronic interface with the  Indiana State Children and Hoosiers Immunization Registry Program (CHIRP).


## **Contents**

- [What is the CHIRP Immunization Registry Interface?](#WhatIsCHIRPConnection)
- [Why is the CHIRP Immunization Registry Interface valuable?](#WhyIsConnectionValuable)
- [How to establish interface between Elation & CHIRP](#HowToEstablishConnection)
- [How to send vaccination data to CHIRP using Elation](#HowToSubmitData)
- [How to query for vaccination history/forecast using CHIRP](#HowToQuery)
- [Frequently Asked Questions (FAQ)](#FAQ)

## **What is the CHIRP Immunization Registry Interface?**

The CHIRP Immunization Registry Interface allows connected practices to send vaccination information from their Elation EHR directly to CHIRP; the Indiana State Children and Hoosiers Immunization Registry Program. Practices can also query CHIRP for vaccination history or forecast.



## **Why is the CHIRP Immunization Registry Interface valuable?**

With the CHIRP Immunization Registry Interface, practices no longer need to separately log in to CHIRP to enter vaccination records for their patients. Once the vaccination is recorded in Elation during the patient encounter, the information can be sent immediately from the patient's chart in Elation to CHIRP. You can also pull vaccination history for specific patients from CHIRP to allow you to populate your patient's clinical profile and make informed decisions for administering vaccines. This interface saves you time and allows you to streamline your vaccination workflows.

###

## **How to establish interface between Elation & CHIRP**

The Elation Team will assist you with initiating interface with CHIRP. To notify us of your interest please complete [this form for CHIRP](https://elation.my.salesforce.com/sfc/p/37000000L9cg/a/6O0000016jAE/ZNNZ_ib9CL8Adp3TUUxS3p5LKN.olD4wbx4eqTBoyEU) and then [click here to fill out our contact form](https://help.elationhealth.com/s/contactsupport) and select "Immunization Registry" as the *Request Type*. A member of the Elation team will collect the completed CHIRP form from you.




## **How to submit vaccination data to CHIRP using Elation**

You will use the Vaccine Form in the patient's chart to document the vaccination data and submit it the data to CHIRP. Learn more about how to use the Vaccine Form using the [Vaccination Documentation Guide](Vaccination-Form-Guide.md).

**Important Note**: CHIRP will only accept the '*New record (performed now)*' **Record Type** if the vaccination submission date is within 30 days of the vaccination administration date. Vaccines administered more than 30 days ago must be submitted as a '*Historical record (performed previously*' under **Record Type**.



**User Tip**: All submissions are one-time only. If you need to edit any vaccination data after it is sent to the Immunization Registry, you will need to update the data in both the patient's chart and the Immunization Registry directly.




## **How to query for vaccination history/forecast using CHIRP**

You can query for vaccination history/forecast directly within a patient's chart by following the instructions listed in the ['*Querying for vaccination history and/or forecast using an Immunization Registry Interface*' section of the Vaccination Documentation Guide](Vaccination-Form-Guide.md#query_IR).

**Important Note**: Patients must have address information on file in order to use the query and forecast features.




## **Frequently Asked Questions (FAQ)**

#### **How can I tell if the vaccination record was successfully submitted to the immunization registry?**

You can log into your State’s registry to review vaccination records submitted from Elation to the registry through the interface from time to time. If you have questions about a specific vaccination record, [please send the patient ID and the name of the immunization to the Support Team](https://help.elationhealth.com/s/contactsupport) and we can look into the vaccination record.

#### **How can I edit or delete a vaccination record from the registry using Elation?**

At this time, vaccination records submitted through Elation can only be edited or deleted within the registry. If you do make a change to or delete the vaccination record in the registry, we also recommend making the same change in Elation.


#### **I am running into errors when using the "Check Registry" or the "Check Forecast" buttons. What should I do?**

Follow the instructions in the ['*Managing querying errors*' section of the Vaccination Documentation Guide](Vaccination-Form-Guide.md#query_errors).


## **Related Articles**

- [Immunization Registry Interface Introduction](Immunization-Registry-Interface-Introduction.md)
- [Vaccination Documentation Guide](Vaccination-Form-Guide.md)