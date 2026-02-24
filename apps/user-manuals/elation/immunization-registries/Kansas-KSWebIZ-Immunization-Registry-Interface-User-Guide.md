# Kansas - KSWebIZ - Immunization Registry Interface User Guide

Source: https://help.elationhealth.com/s/article/Kansas-KSWebIZ-Immunization-Registry-Interface-User-Guide

---

To support the importance of promoting and prioritizing interoperability and exchange of patient immunization data across various healthcare platforms, Elation has established an electronic interface with the Kansas State Immunization Registry known as KSWebIZ.

## **Contents**

- [What is the KSWebIZ Immunization Registry Interface?](#WhatIsKSWebIZConnection)
- [Why is the KSWebIZ Immunization Registry Interface valuable?](#WhyIsConnectionValuable)
- [How to establish interface between Elation & KSWebIZ](#HowToEstablishConnection)
- [How to send vaccination data to KSWebIZ using Elation](#HowToSubmitData)
- [How to query for vaccination history/forecast using KSWebIZ](#HowToQuery)
- [Frequently Asked Questions (FAQ)](#FAQ)

## **What is the KSWebIZ Immunization Registry Interface?**

The KSWebIZ Immunization Registry Interface allows connected practices to send vaccination information from their Elation EHR directly to KSWebIZ, the Kansas Immunization Registry. Practices can also query KSWebIZ for vaccination history or forecast.


## **Why is the KSWebIZ Immunization Registry Interface valuable?**

With the KSWebIZ Immunization Registry Interface, practices no longer need to separately log in to KSWebIZ to enter vaccination records for their patients. Once the vaccination is recorded in Elation during the patient encounter, the information can be sent immediately from the patient's chart in Elation to KSWebIZ. You can also pull vaccination history for specific patients from KSWebIZ to allow you to populate your patient's clinical profile and make informed decisions for administering vaccines. This interface saves you time and allows you to streamline your vaccination workflows.

###

## **How to establish interface between Elation & KSWebIZ**

The Elation Team will assist you with initiating an interface with KSWebIZ. To notify us of your interest,

1. [Click here to fill out our contact form](https://app.elationemr.com/support/)
2. Select "I am a provider or staff member who uses Elation" for **What is your role?**
3. Select "Something else" for **Select an issue**
4. Enter the following information in the **Details** field:
   - Name of the immunization registry you want to connect to.
   - What county is your practice in?
   - What are the names and emails of the users in your practice who will need access to KSWebIZ?
   - Is your practice enrolled with Vaccines for Children (VFC)? If so, what is your VFC PIN?
   - Is your practice part of a medical group? If so, what is the name of the medical group and how many practices are a part of the medical group?
   - Is your practice a member of the Kansas Health Information Exchange (KHIE), Kansas Health Information Network (KHIN), or Lewis and Clark Information Exchange (LACIE)?
   - Have the individual who is responsible for you facility’s security complete this [Kansas HL7 Security Agreement](https://elation.my.salesforce.com/sfc/p/#37000000L9cg/a/6O000000IBA7/fIft9ouQX2Zs.gQFkpRTo5nKvuEACKUpccOLwrVV6Bs). (You will share the completed Agreement with Elation in a later step).
   - Complete this [Site Enrollment Agreement](https://elation.my.salesforce.com/sfc/p/#37000000L9cg/a/6O000000IBA8/GEImC3NcatJqNIwyTPjctS2ioX0D_xKTKmmvbgFr0Io). (You will share the completed Agreement with Elation in a later step).
5. Click "Next".
6. Click "No, I still need help" in the next window.
7. Click "Add Attachments" and attach the completed [Kansas HL7 Security Agreement](https://elation.my.salesforce.com/sfc/p/#37000000L9cg/a/6O000000IBA7/fIft9ouQX2Zs.gQFkpRTo5nKvuEACKUpccOLwrVV6Bs) & [Site Enrollment Agreement](https://elation.my.salesforce.com/sfc/p/#37000000L9cg/a/6O000000IBA8/GEImC3NcatJqNIwyTPjctS2ioX0D_xKTKmmvbgFr0Io).
8. Click "Next".
9. Confirm your contact information and then click "Submit" to submit your request to Elation.

## **How to submit vaccination data to KSWebIZ using Elation**

You will use the Vaccine Form in the patient's chart to document the vaccination data and submit it the data to KSWebIZ. Learn more about how to use the Vaccine Form using the [Vaccination Documentation Guide](Vaccination-Form-Guide.md).

**User Tip**: All submissions are one-time only. If you need to edit any vaccination data after it is sent to the Immunization Registry, you will need to update the data in both the patient's chart and the Immunization Registry directly.




## **How to query for vaccination history/forecast using KSWebIZ**

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