# Elation-Healee Integration Guide

Source: https://help.elationhealth.com/s/article/Elation-Healee-Integration-Guide

---

# **Contents**

- [Overview](#overview)
 - [What is Healee?](#Healee_info)
 - [What is the Elation-Healee integration?](#integration_intro)
 - [How do I get started?](#activate_integration)
 - [What information is shared between Elation & Healee?](#sync_overview)
- [Workflow Instructions](#workflow_instructions)
 - [Linking Patients](#linking_patients)
    - [Automatically linking charts created in Elation](#create_patient_in_Elation)
    - [Automatically linking charts (contacts) created in Healee](#create_patient_in_healee)
    - [Manually linking charts between Elation and Healee](#link_patients_manually)
 - [Synchronizing demographics](#synchronizing_demographics)
 - [Synchronizing messages](#synchronizing_messages)

# **Overview**

## **What is Healee?**

Healee offers a secure, HIPAA-compliant communication platform that facilitates smooth interactions between patients and healthcare providers. Through Healee, patients can effortlessly discuss symptoms via messaging, make phone calls, or book virtual video appointments with their providers, all within one integrated platform. This ensures that both patients and providers experience secure, simple, and adaptable care delivery.

By using Healee, healthcare providers can manage patient communications in a centralized and efficient manner, reducing the need for multiple communication tools. Patients benefit from the convenience of having all their interactions with healthcare providers in one place, enhancing their overall experience and engagement with their care. Healee also supports the continuity of care by allowing easy follow-up consultations and maintaining a comprehensive record of all patient-provider communications. With Healee, the entire process of seeking and providing care becomes more streamlined, ensuring that both patients and providers can focus on what matters most: effective and timely healthcare.


## **What is the Elation-Healee integration?**

The Elation-Healee integration offers the following functionalities:

- Bi-directional automatic link between charts for patients in Healee when you create their chart in Elation.
- Keep patient contact information up to date in both systems effortlessly.
- Ability to transfer conversations from Healee to Elation, ensuring all clinical data is stored in one place within Elation EHR.

## **How do I get started?**

To begin using this integration, [click here to tell Elation you are interested](https://help.elationemr.com/s/contactsupport). A member of Elation's Implementation Team will contact you about next steps.


## **What information is shared between Elation & Healee?**

The following information is shared between Elation and Healee:

| Elation | | Healee | Notes |
| --- | --- | --- | --- |
| Chart Creation | ↔ | Contact Profile Creation | When a new patient is created either in Healee or Elation, they are linked to their respective chart in the other system. |
| Demographics Edits | ↔ | Demographics Edits | Demographic edits can be made in either platform and will be reflected across both. |
| Non-visit note | ← | Message history (conversations) | Conversations can be manually synced from Healee to Elation as a non-visit note. |




# **Workflow Instructions**

## **Linking Patients**

### **Automatically linking charts created in Elation**

Patients need a Contact in Healee in order for them to communicate with your practice via SMS, Secure Message, or Video. When a new chart is created in Elation, Elation will automatically link the chart to the patient's respective Healee contact profile based on the patient's First Name, Last Name and Date of Birth.

**Important Note**: If Elation is unable to automatically find a contact with the same parameters, you can link the Elation chart to the Healee contact manually. [See below for instructions](#link_patients_manually).




### **Automatically linking charts (contacts) created in Healee**

When patients create a new Contact profile for themselves in Healee, the integration will automatically link the Contact to the patient's Elation chart if it exists. The link will be based on the following parameters in the following order:

- Match by the Email in the patient's chart in Elation
- If Email is not found then we will match by any primary phone number.
- If primary phone number is not found then we will match by First Name, Last Name and Date of Birth.

**Important Note**: If the integration is unable to automatically find a chart with the same parameters, you can link the Elation chart to the Healee contact manually. [See below for instructions](#link_patients_manually).





### **Manually linking charts between Elation and Healee**

To link a patient chart in Elation to a Contact in Healee, follow these steps:

1. Open the patient's Contact details in Healee.
2. Click on the 3 dots at the top right corner
3. Click **Link to Elation**
4. Open the patient’s chart in Elation
5. Copy the patient’s ID from the URL (the set of numbers after the / )
6. Paste the patient’s ID in Healee
7. Click **Save Changes**

To remove a link, follow the same instructions above and click **Remove link**.



## **Synchronizing demographics**

Once the patient is linked between Elation and Healee, updates to the following demographic fields in either Elation or Healee will be synchronized immediately:

- First Name
- Last Name
- Primary Phone number
- Email address
- Date of birth
- Sex at birth

**Important Note**: If there is any discrepancy in data upon initial linking, Healee’s data will prevail, assuming that the patient has entered their correct data in Healee when they created their Contact profile.




## **Synchronizing messages**

Messages from Healee can be manually synced into Elation as Non-Visit Notes by following these instructions:

1. Open the message conversation in Healee.
2. Hover over any message until three horizontal dots appear, then click on the dots.
3. Click **Select**.
4. Click on the radio buttons beside the messages you want to sync to select them individually or click **Select All** to select all messages.
5. Click **Send to EHR Elation** at the bottom of the conversation to send all selected messages to the patient's chart in Elation.
6. Open or refresh the patient’s chart in Elation to view the synchronized messages in a Non-visit note in Requiring Action.
7. Sign off on the Non-visit note once you are ready to store the conversation in the patient's Chronological Record.

#