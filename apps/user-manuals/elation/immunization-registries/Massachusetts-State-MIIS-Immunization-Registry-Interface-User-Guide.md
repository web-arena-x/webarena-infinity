# Massachusetts State- MIIS- Immunization Registry Interface User Guide

Source: https://help.elationhealth.com/s/article/Massachusetts-State-MIIS-Immunization-Registry-Interface-User-Guide

---

To support the importance of promoting and prioritizing interoperability and exchange of patient immunization data across various healthcare platforms, Elation has established an electronic interface with the Massachusetts State Immunization Registry known as MIIS.

## **Contents**

- [What is the MIIS Immunization Registry Interface?](#WhatIsMIISConnection)
- [Why is the MIIS Immunization Registry Interface valuable?](#WhyIsConnectionValuable)
- [How to establish interface between Elation & MIIS](#HowToEstablishConnection)
- [How to send vaccination data to MIIS using Elation](#HowToSubmitData)
- [How to query for vaccination history/forecast using MIIS](#HowToQuery)
- [Frequently Asked Questions (FAQ)](#FAQ)

## **What is the MIIS Immunization Registry Interface?**

The MIIS Immunization Registry Interface allows connected practices to **send** vaccination information from their Elation EHR directly to MIIS; the Massachusetts Immunization Information System. Practices can also query MIIS for vaccination history or forecast.


## **Why is the MIIS Immunization Registry Interface valuable?**

With the MIIS Immunization Registry Interface, practices no longer need to separately log in to HIR to enter vaccination records for their patients. Once the vaccination is recorded in Elation during the patient encounter, the information can be sent immediately from the patient's chart in Elation to MIIS. You can also pull vaccination history for specific patients from MIIS to allow you to populate your patient's clinical profile and make informed decisions for administering vaccines. This interface saves you time and allows you to streamline your vaccination workflows.

## **How to establish interface between Elation & MIIS**

The Elation Team will assist you with initiating interface with MIIS. To notify us of your interest, please [click here to fill out our contact form](https://help.elationhealth.com/s/contactsupport) and select "Immunization Registry" as the *Request Type*.

## **How to submit vaccination data to MIIS using Elation**


You will use the Vaccine Form in the patient's chart to document the vaccination data and submit it the data to MIIS. Learn more about how to use the Vaccine Form using the [Vaccination Documentation Guide](Vaccination-Form-Guide.md).

**User Tip**: All submissions are one-time only. If you need to edit any vaccination data after it is sent to the Immunization Registry, you will need to update the data in both the patient's chart and the Immunization Registry directly.

## **How to query for vaccination history/forecast using MIIS**

You can query for vaccination history/forecast directly within a patient's chart by following the instructions listed in the ['*Querying for vaccination history and/or forecast using an Immunization Registry Interface*' section of the Vaccination Documentation Guide](Vaccination-Form-Guide.md#query_IR).


## **Frequently Asked Questions (FAQ)**

#### **How can I tell if the vaccination record was successfully submitted to the immunization registry?**

You can log into your State’s registry to review vaccination records submitted from Elation to the registry through the interface from time to time. If you have questions about a specific vaccination record, [please send the patient ID and the name of the immunization to the Support Team](https://help.elationhealth.com/s/contactsupport) and we can look into the vaccination record.

#### **How can I edit or delete a vaccination record from the registry using Elation?**

At this time, vaccination records submitted through Elation can only be edited or deleted within the registry. If you do make a change to or delete the vaccination record in the registry, we also recommend making the same change in Elation.

#### **I am running into errors when using the "Check Registry" or the "Check Forecast" buttons. What should I do?**

Follow the instructions in the ['*Managing querying errors*' section of the Vaccination Documentation Guide](Vaccination-Form-Guide.md#query_errors).

#### **Can I use MIIS inventory management with Elation?**

Yes! If you are using MIIS for inventory management, any vaccine reported to MIIS should deduct automatically from your inventory in the MIIS portal if the vaccine was reported via Elation with all the correct matching fields filled out (especially lot number and funding type).

These are the circumstances in which you will still need to log in to MIIS to manually track inventory:

1. If the administered vaccine is reported with an incorrect field, such as an incorrect lot number or lot type (funding type), the administered doses will not decrement appropriately, and the record will be listed in the MIIS website’s inventory decrementing tool for you to manually correct: [Inventory Decrementing Tool Mini Guide](https://resources.miisresourcecenter.com/trainingcenter/Inventory%20Decrementing%20Tool_2019_Mini%20Guide.pdf).
2. If you transfer state-supplied doses to another location, the inventory must be transferred within the MIIS portal manually as well: [Vaccines Transfer Mini Guide](https://resources.miisresourcecenter.com/trainingcenter/Vaccine%20Transfers_2018_Mini%20Guide.pdf).




## **Related Articles**

- [Vaccination Documentation Guide](Vaccination-Form-Guide.md)