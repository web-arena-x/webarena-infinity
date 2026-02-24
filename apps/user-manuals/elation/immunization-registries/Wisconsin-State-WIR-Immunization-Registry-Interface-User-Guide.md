# Wisconsin State- WIR- Immunization Registry Interface User Guide

Source: https://help.elationhealth.com/s/article/Wisconsin-State-WIR-Immunization-Registry-Interface-User-Guide

---

To support the importance of promoting and prioritizing interoperability and exchange of patient immunization data across various healthcare platforms, Elation has established an electronic interface with the Wisconsin State Immunization Registry (WIR).

## **Contents**

- [What is the WIR Immunization Registry Interface?](#WhatIsWIRConnection)
- [Why is the WIR Immunization Registry Interface valuable?](#WhyIsConnectionValuable)
- [How to establish interface between Elation & WIR](#HowToEstablishConnection)
- [How to send vaccination data to WIR using Elation](#HowToSubmitData)
- [How to query for vaccination history/forecast using WIR](#HowToQuery)
- [Registering with PHREDS](#phreds)
- [Frequently Asked Questions (FAQ)](#FAQ)

## **What is the WIR Immunization Registry Interface?**

The WIR Immunization Registry Interface allows connected practices to send vaccination information from their Elation EHR directly to WIR; the Wisconsin State Immunization Registry. Practices can also query ASIIS for vaccination history or forecast.



## **Why is the WIR Immunization Registry Interface valuable?**

With the WIR Immunization Registry Interface, practices no longer need to separately log in to WIR to enter vaccination records for their patients. Once the vaccination is recorded in Elation during the patient encounter, the information can be sent immediately from the patient's chart in Elation to WIR. You can also pull vaccination history for specific patients from WIR to allow you to populate your patient's clinical profile and make informed decisions for administering vaccines. This interface saves you time and allows you to streamline your vaccination workflows.

###

## **How to establish interface between Elation & WIR**

The Elation Team will assist you with initiating interface with WIR. To notify us of your interest, please [click here to fill out our contact form](https://help.elationhealth.com/s/contactsupport), select "Immunization Registry" as the *Request Type*, and send the following information to Elation:

1. Are you currently administering vaccines? If so
   1. How often do you administer immunizations?
   2. Are you administering COVID vaccines?
2. Do you have an account with WIR (or do you have a login to WIR)?
3. Do you want to set up Inventory Deduction?
   - Inventory Deduction allows WIR to automatically deduct vaccine inventory after submitting a vaccination to the registry
4. Is your practice already registered with PHREDS (the Public Health Registration for Electronic Data Submission System)? If you are not, [follow the instructions below to register with PHREDS](#phreds)
5. Are you a VFC provider?
6. Will you be working to attest to Meaningful Use Stage 3?
7. How are you currently entering immunization data in WIR? What Organization are you recording under, if any?
8. There is a possibility that your staff will need to change their immunization documentation workflow. How long do you anticipate it will take you to update your staff on the new process?

## **How to submit vaccination data to WIR using Elation**

You will use the Vaccine Form in the patient's chart to document the vaccination data and submit it the data to WIR. Learn more about how to use the Vaccine Form using the [Vaccination Documentation Guide](Vaccination-Form-Guide.md).

**User Tip**: All submissions are one-time only. If you need to edit any vaccination data after it is sent to the Immunization Registry, you will need to update the data in both the patient's chart and the Immunization Registry directly.




## **How to query for vaccination history/forecast using WIR**

You can query for vaccination history/forecast directly within a patient's chart by following the instructions listed in the ['*Querying for vaccination history and/or forecast using an Immunization Registry Interface*' section of the Vaccination Documentation Guide](Vaccination-Form-Guide.md#query_IR).


## **Registering with PHREDS**

WIR requires you to have registered with PHREDS (the Public Health Registration for Electronic Data Submission System) in order to send immunization data electronically from an EHR to WIR. Follow the steps below to register with PHREDS.

1. You first need a Wisconsin Logon Management System (WILMS) account to access PHREDS.
   1. If you already have a WILMS account and know your account information, send an email to the Wisconsin eHealth Program ([ehealth@wisconsin.gov](mailto:ehealth@wisconsin.gov)) with your WILMS account name and the subject line "PHREDS Access."
   2. If you are not sure if you have a WILMS account, check the [Department of Administration account management](https://register.wisconsin.gov/AccountManagement/acctrecovery/EmailEntry.aspx) website to see if you have an account.
      1. If you do have a WILMS account, you will receive an email with your WILMS account information. Send an email to the Wisconsin eHealth Program ([ehealth@wisconsin.gov](mailto:ehealth@wisconsin.gov)) with your WILMS account name and the subject line "PHREDS Access."
      2. If you do not have a WILMS account, the following text will display: 'The E-Mail address you entered was not found. Please enter the correct E-Mail address.' Follow Step c below to register for a WILMS account
   3. If you do not have a WILMS account, create a WILMS account on the [Self Registration](https://register.wisconsin.gov/AccountManagement/AccountCreationOverview.aspx) page.
      1. Under *Systems You Will Access,* select "PHREDS" and proceed with creating a WILMS account
      2. After you create a new WILMS account, an automated email will be sent to the Wisconsin eHealth Program to notify them of your account information
2. You will receive an email granting you access to the PHREDS within three business days. If you do not receive this email within three days, email the Wisconsin eHealth Program ([ehealth@wisconsin.gov](mailto:ehealth@wisconsin.gov)).

## **Frequently Asked Questions (FAQ)**

##

#### **How can I tell if the vaccination record was successfully submitted to the immunization registry?**

You can log into your State’s registry to review vaccination records submitted from Elation to the registry through the interface from time to time. If you have questions about a specific vaccination record, [please send the patient ID and the name of the immunization to the Support Team](https://help.elationhealth.com/s/contactsupport) and we can look into the vaccination record.

#### **How can I edit or delete a vaccination record from the registry using Elation?**

At this time, vaccination records submitted through Elation can only be edited or deleted within the registry. If you do make a change to or delete the vaccination record in the registry, we also recommend making the same change in Elation.

#### **I am running into errors when using the "Check Registry" or the "Check Forecast" buttons. What should I do?**

Follow the instructions in the ['*Managing querying errors*' section of the Vaccination Documentation Guide](Vaccination-Form-Guide.md#query_errors).

## **Related Articles**

- [Vaccination Documentation Guide](Vaccination-Form-Guide.md)