# Pennsylvania State- PIERS- Immunization Registry Interface User Guide

Source: https://help.elationhealth.com/s/article/Pennsylvania-State-PIERS-Immunization-Registry-Interface-User-Guide

---

To support the importance of promoting and prioritizing interoperability and exchange of patient immunization data across various healthcare platforms, Elation has established an electronic interface with the Pennsylvania Immunization Electronic Registry System (PIERS), formerly known as PA-SIIS.


## **Contents**

- [What is the PIERS Immunization Registry Interface?](#WhatIsPIERSConnection)
- [Why is the PIERS Immunization Registry Interface valuable?](#WhyIsConnectionValuable)
- [How to establish interface between Elation & PIERS](#HowToEstablishConnection)
- [How to send vaccination data to PIERS using Elation](#HowToSubmitData)
- [How to query for vaccination history/forecast using PIERS](#HowToQuery)
- [Frequently Asked Questions (FAQ)](#FAQ)

## **What is the PIERS Immunization Registry Interface?**

The PIERS Immunization Registry Interface allows connected practices to send vaccination information from their Elation EHR directly to PIERS, the Pennsylvania Immunization Electronic Registry System, formerly known as PA-SIIS. Practices can also query PIERS for vaccination history or forecast.



## **Why is the PIERS Immunization Registry Interface valuable?**

With the PIERS Immunization Registry Interface, practices no longer need to separately log in to PIERS to enter vaccination records for their patients. Once the vaccination is recorded in Elation during the patient encounter, the information can be sent immediately from the patient's chart in Elation to PIERS. You can also pull vaccination history for specific patients from PIERS to allow you to populate your patient's clinical profile and make informed decisions for administering vaccines. This interface saves you time and allows you to streamline your vaccination workflows.

## **How to establish interface between Elation & PIERS**

The Elation Team will assist you with initiating an interface with KSWebIZ. To notify us of your interest,

1. [Click here to fill out our contact form](https://app.elationemr.com/support/)
2. Select "I am a provider or staff member who uses Elation" for **What is your role?**
3. Select "Something else" for **Select an issue**
4. Enter the following information in the **Details** field:
   - Name of the Immunization Registry you want to connect to.
5. Click "Next".
6. Click "No, I still need help" in the next window.
7. Complete [this request form](https://elation.my.salesforce.com/sfc/p/#37000000L9cg/a/1G000001A2Z6/8t4o6FXmPurP9CRNC8hjO24jF8BZcjpQooIV0Q5yWwQ).
8. Click "Add Attachments" and attach the completed request form.
9. Click "Next".
10. Confirm your contact information and then click "Submit" to submit your request to Elation.



## **How to submit vaccination data to PIERS using Elation**

You will use the Vaccine Form in the patient's chart to document the vaccination data and submit it the data to PIERS. Learn more about how to use the Vaccine Form using the [Vaccination Documentation Guide](Vaccination-Form-Guide.md).

**User Tip**: All submissions are one-time only. If you need to edit any vaccination data after it is sent to the Immunization Registry, you will need to update the data in both the patient's chart and the Immunization Registry directly.



## **How to query for vaccination history/forecast using PIERS**

You can query for vaccination history/forecast directly within a patient's chart by following the instructions listed in the ['*Querying for vaccination history and/or forecast using an Immunization Registry Interface*' section of the Vaccination Documentation Guide](Vaccination-Form-Guide.md#query_IR).

**Important Note**: When querying for vaccination history, you may notice results are not returned even though the patient has records in PIERS. This is a known limitation with the PIERS interface that PIERS hopes to improve by the end of 2024. We recommend signing in to PIERS directly to double check for vaccination history if you notice blank results in Elation when querying PIERS.




## **Frequently Asked Questions (FAQ)**

#### **How can I tell if the vaccination record was successfully submitted to the immunization registry?**

You can log into your State’s registry to review vaccination records submitted from Elation to the registry through the interface from time to time. If you have questions about a specific vaccination record, [please send the patient ID and the name of the immunization to the Support Team](https://help.elationhealth.com/s/contactsupport) and we can look into the vaccination record.


#### **How can I edit or delete a vaccination record from the registry using Elation?**

At this time, vaccination records submitted through Elation can only be edited or deleted within the registry. If you do make a change to or delete the vaccination record in the registry, we also recommend making the same change in Elation.

#### **I am running into errors when using the "Check Registry" or the "Check Forecast" buttons. What should I do?**

Follow the instructions in the ['*Managing querying errors*' section of the Vaccination Documentation Guide](Vaccination-Form-Guide.md#query_errors).


#### **Does Elation have an interface with the Philadelphia Department of Public Health's Immunization Information System (PhilaVax)?**

Yes, Elation has an interface with PhilaVax. [Learn more about the PhilaVax Interface here](Philadelphia-City-PhilaVax-Immunization-Registry-Interface-Guide.md).


## **Related Articles**

- [Vaccination Documentation Guide](Vaccination-Form-Guide.md)
- [Philadelphia (PA)- PhilaVax- Immunization Registry Interface Guide](Philadelphia-City-PhilaVax-Immunization-Registry-Interface-Guide.md)