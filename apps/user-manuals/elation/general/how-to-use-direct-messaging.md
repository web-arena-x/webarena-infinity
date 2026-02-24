# Letter & Referral Guide - Sending and receiving Direct messages

Source: https://help.elationhealth.com/s/article/how-to-use-direct-messaging

---

# **Contents**

- [Overview](#overview)
 - [What is Direct messaging?](#description)
 - [What are the benefits of Direct messaging?](#benefits)
 - [How do I enable Direct messaging?](#enable)
 - [Prerequisites for sending a Direct message](#prerequisites)
 - [How do I find my Direct Address?](#Direct_address)
 - [What happens when you send a Direct message?](#Direct_message_flow)
 - [What can you send via Direct message?](#send_formats)
 - [What can you receive via Direct message?](#receive_formats)
 - [Enabling Premium EHR Features](#Premium_EHR)
- [Workflow Instructions](#workflow_instructions)
 - [Editing a contact’s Direct Address](#edit_Contact)
 - [Sending a Direct message](#send_Direct_message)
 - [Viewing sent Direct messages](#view_sent_message)
 - [Receiving a Direct message](#receive_Direct_message)
- [Frequently Asked Questions (FAQ)](#FAQ)






# **Overview**

## **What is Direct messaging?**

Direct messaging is a secure, HIPAA-compliant, and encrypted method for electronically exchanging health information between Elation and other EHR systems. Each Provider-Level User is assigned a Direct Address associated with Elation to allow them to send and receive Direct messages within the Elation EHR.





## **What are the benefits of Direct messaging?**

Direct messaging offers the following benefits:

- **Ensure secure and HIPAA-compliant communication** – Use Direct Messaging to encrypt and securely transmit Protected Health Information (PHI) while complying with HIPAA and other privacy regulations.
- **Exchange patient data seamlessly** – Share clinical documents, such as Continuity of Care Documents (CCD/CCDA), lab results, and referrals electronically, eliminating the need for faxing or mailing.
- **Improve care coordination and interoperability** – Facilitate seamless communication among providers, specialists, hospitals, and healthcare organizations across different EHRs to ensure continuity of care.

## **How do I enable Direct messaging?**

Direct messaging is automatically enabled for Provider Level Users during the account set up process.

## **Prerequisites for sending a Direct message**

To send a Direct message,

1. You must be a Provider Level User on Elation **AND**
2. The recipient must meet both conditions:
   1. Have a Direct Address with their non-Elation EHR
   2. Be saved as a contact in your Elation Directory, with their Direct Address included in their contact details.
      - Contacts in the Elation Directory database may already have a Direct Address in their contact details, sourced from Surescripts. You can update a contact’s Direct Address as needed.

ℹ️ **PREMIUM EHR ONLY** If you are a Premium EHR user, go to the [Premium EHR features section](#Premium_EHR) below to learn more about allowing Staff Level Users to send Direct messages on a Provider Level User's behalf.



## **How do I find my Direct Address?**

To view your Direct Address, go to **Settings** -> **Account Details** -> **Direct Address**. The Direct Address is in the following format: *firstname.lastname@practiceID#.[direct.elationemr.com](http://direct.elationemr.com)*.

- For example: *[john.smith@12345.direct.elationemr.com](mailto:john.smith@12345.direct.elationemr.com)*

Click **I need help** -> **Contact Elation Support** to request a Direct Address if you do not see one for your account.



## **What happens when you send a Direct message?**

When you send a Direct message, the message, a CCDA file of the patient’s data, and any attachments you add are sent to the recipient’s EHR. Once received, the actions that the recipient can take to view and import the data will depend on their own EHR.



| | | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| You send a Direct message. | → | The message, along with its attachments & the CCDA of the patient’s data, is encrypted. | → | Data is transmitted securely to the recipient. | → | Recipient receives Direct message. | → | Recipient integrates data into their EHR (if supported). |





## **What can you send via Direct message?**

Any patient records that can be attached to a Letter or Referral can be sent via Direct message as long as the record is in one of the following formats:

- .jpeg
- .pdf
- .png
- .tiff
- .xml (also known as CCD/CCDA files)

Unsupported file types will not be transmitted via Direct message, even if attached to a Letter or Referral.





## **What can you receive via Direct message?**

The chart below lists the file types supported by Elation for received Direct messages and explains how the data appears in the patient’s chart. Unsupported file types will not appear in the patient’s chart.

| | |
| --- | --- |
| **File Type** | **Data is rendered as…** |
| .csv | Hyperlink - download to your computer and opened with compatible software. |
| .doc | Hyperlink - download to your computer and opened with compatible software. |
| .docx | Hyperlink - download to your computer and opened with compatible software. |
| .html | Hyperlink - download to your computer and opened with compatible software. |
| .jpeg | Image - view directly in the patient's chart. |
| .pdf | Image - view directly in the patient's chart. |
| .png | Image - view directly in the patient's chart. |
| .rtf | Image - view directly in the patient's chart. |
| .tiff | Image - view directly in the patient's chart. |
| .xlsx | Hyperlink - download to your computer and opened with compatible software. |
| .xml | [CCD/CCDA](https://help.elationemr.com/s/article/import-patient-information-from-another-ehr-c-cda-format) - view as a structured report in the patient's chart. |




## **Enabling Premium EHR Features**

Premium EHR users can request a feature that would allow Staff Level Users to send Direct messages on behalf of a Provider Level User. Staff Level Users would use the same workflow as Provider Levels Users to send Direct messages via a Provider Letter or Referral. This feature would not allow Staff Level Users to receive Direct messages.

ℹ️ **PREMIUM EHR ONLY**

This feature is part of Elation's Premium EHR offering.

- If you are already a Premium EHR user and you are interested in using this feature, click the **I need help** -> **Contact Elation Support** button to notify Elation and a member of the Elation Team will activate the feature for you.
- If you are interested in upgrading to Premium EHR to use this feature, click the**I need help** -> **Contact Elation Support** button and a member of the Elation team will assist you.

# **Workflow Instructions**

## **Editing a Contact’s Direct Address**

If a contact has a Direct Address, you will see their Direct Address in their **Contact** details. To add or edit a Contact’s Direct Address:

| | |
| --- | --- |
| **1** | Create a new Provider Letter or Referral. |
| **2** | Type the recipient’s name in the **To** field and then select a match from the search results. |
| **3** | Click **Edit Contact**. |
| **4** | Click **Edit** under their main details. |
| **5** | Click **Save** after making your edits. |





## **Sending a Direct message**

To send a Direct message:

| | |
| --- | --- |
| **1** | [Create a new Provider Letter or Referral](https://help.elationemr.com/s/article/sending-letters-and-referrals#initiation). |
| **2** | Type the recipient’s name in the **To** field and then select a match from the search results. [Check if they have a Direct Address on file and add one if needed](#edit_Contact). |
| **3** | Fill out the remaining fields of the Provider Letter or Referral. Click here for a detailed breakdown of the different fields. - **Subject**: Provide a brief overview or context to explain the purpose of the correspondence. - **Body**: Type the main content of your correspondence.   - Use [Wordsmith](https://help.elationemr.com/s/article/Auto-drafting-letters-and-referrals-with-Wordsmith), our generative AI tool, to help you draft your correspondence if needed. - (Referral only) Referral details:   - **Auth For**: Document any authorization details (i.e. the approved service or procedure or number of encounters) as needed.   - **Auth #**: Record the authorization number supplied by the patient’s insurance if applicable.   - **Add Dxs**: Enter the ICD-10 codes that validate the medical necessity of the referral. - Settings   - **Post Date**: Select a future date to send the Provider Letter or Referral.   - **Unread Alert**: **(**[Elation EHR](https://help.elationemr.com/s/article/share-documents-between-other-elationemr-users) **&** [Connect](https://help.elationemr.com/s/article/secure-Provider-Portal) **recipients only**) Alert yourself if the Letter/Referral has not been read by the recipient by a specific timeframe.   - **Print Header**: Select the [Print Header](https://help.elationemr.com/s/article/print-headers) you want to appear on this Letter/Referral. |
| **4** | Adjust/Add attachments as needed. Click here for a detailed breakdown of the attachment options. - Default behavior   - If you initiated the letter or referral from a patient record, the record will automatically be included as an attachment.   - If you are creating a referral, the patient’s demographics and Clinical Profile will automatically be included as attachments. - Options for attaching records:   - **Select Chart Items to Attach**: Use this option to pick and choose individual patient records to attach to the letter or referral.   - **Attach Everything in Chart**: Use this option to attach all attachable records, referenced below, to the letter or referral. - Records available as attachments include:   - Patient demographics   - Clinical Profile   - Immunization History   - Medication List   - Medication History   - Signed Visit Notes & Notes   - Signed Reports   - Signed Orders   - Completed office messages   - Other signed letters or referrals   - Growth Charts |
| **5** | Look for a yellow banner that says *“This letter and attachments will be sent via direct message into the recipient’s EMR account.”* to confirm it’s being sent as a Direct message\*. |
| **6** | **Sign & Send** the correspondence. Click here for a detailed breakdown of the different Send options. - **Sign & Send**: Signs the correspondence and sends it to the recipient using the delivery method specified in the yellow banner. - **Sign, Send & Print Pt Copy**: Signs the correspondence, sends it using the delivery method specified in the yellow banner and prints the body of the correspondence without attachments. - **Sign & Print w/attachments**: Signs the correspondence and prints the entire correspondence and its attachments. - **Sign, Send & Create Follow-up Letter**: Signs the correspondence, sends it to the recipient using the delivery method specified in the yellow banner and then creates a new correspondence draft for the same recipient. |

ℹ️   **EXCEPTIONS** If the **Contact** is an [Elation EHR User](share-documents-between-other-elationemr-users.md) or an [Elation Connect User](https://help.elationemr.com/s/article/secure-Provider-Portal), the message will be sent as a regular Provider Letter or Referral instead of a Direct message (even if the **Contact** has a Direct message address on file) as this routing method is more immediate and secure.



## **Viewing sent Direct messages**

Check the Provider Letter or Referral in the **Chronological Record** to confirm that the Direct message was sent.

- A successfully transmitted Direct message displays the confirmation message ‘Direct Message Sent’ in the signed Letter or Referral.





## **Receiving Direct messages**

To receive Direct messages in Elation:

| | |
| --- | --- |
| **1** | Share your Elation Direct Address with the sending provider or facility. |
| **2** | Check the **Provider Letters** inbox of your Practice Home page and/or the **Requiring Action** section of a patient’s chart for any incoming Direct messages. |
| **3** | Click on the name of any attachment to view it as needed.   - If a patient summary (CCD or CCDA file) is attached to the message, it will appear above the Direct message in the **Requiring Action** section.   1. If a Direct message is received for a patient **without** an existing chart, Elation will automatically import data from the CCD/CCDA file to the Clinical Profile of the newly created chart.   2. If a Direct message is received for a patient **with** an existing chart, Elation will not automatically import data from the CCD/CCDA file. You can open the patient summary and choose which sections to import. |
| **4** | Click **Sign** to sign off on the Direct message to file it into the Chronological Record. If the Direct message includes attachments, you will be prompted to sign off on them as well. |

![]()

# **Frequently Asked Questions**

#### **What information is sent in the CCDA file that is automatically` included in a Direct message?**

#### [Click here to learn more about what information is included in Elation’s CCDA files](https://help.elationemr.com/s/article/Supported-Elation-CCDA-types).

####

#### **How are Direct messages routed if I work in multiple Elation accounts?**

If you work in multiple Elation accounts, the Direct message is routed to the first Provider Level User account you registered with Elation.

####

#### **Can Staff Level Users send or receive Direct messages in Elation?**

For Standard EHR subscribers, Staff-Level Users cannot send or receive Direct messages in Elation for Standard EHR Users. However, for [Premium EHR subscribers](https://help.elationemr.com/s/article/Premium-EHR-Features-Guide), Staff-Level Users can be delegated to send Direct messages.

#### **How do I update a Direct Address for a contact when I work in multiple Elation instances?**

If you work in multiple Elation instances, update the Direct Address of a contact in each instance separately, as changes in one instance do not automatically apply to others.


**How do I stop receiving Direct messages?**

It is not possible to block specific Direct messages from reaching your inbox. You must either receive all Direct messages that are sent to you or remove the Direct message feature completely to stop receiving Direct messages. Removing the Direct message feature will also prevent you from sending Direct messages.

Click **I need help** -> **Contact Elation Support** if you want Elation to disable all Direct message functionalities within your account.

# **Related Articles**

- [Letter & Referral Introduction](https://help.elationemr.com/s/article/letter-and-referral-introduction)
- [Letter & Referral Guide - Auto-drafting letters and referrals with Wordsmith](https://help.elationemr.com/s/article/Auto-drafting-letters-and-referrals-with-Wordsmith)
- [Letter & Referral Guide - Sending correspondences to other Elation EHR Users](https://help.elationemr.com/s/article/share-documents-between-other-elationemr-users)
- [Letter & Referral Guide - Sending a fax](https://help.elationemr.com/s/article/how-to-send-a-letter-on-elation)
- [Letter & Referral Guide - Sending correspondences via a secure Provider Portal](https://help.elationemr.com/s/article/accessing-interactive-charts-online)
- [Letter & Referral Guide - Managing & searching the provider directory](https://help.elationemr.com/s/article/Using-the-Provider-Directory)
- [Support Guide - Whitelisting Elation's web domain for email communications](Support-Guide-Whitelisting-Elation.md)