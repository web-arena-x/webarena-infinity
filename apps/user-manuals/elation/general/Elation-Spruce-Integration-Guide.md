# Elation-Spruce- Message Sync Integration Guide

Source: https://help.elationhealth.com/s/article/Elation-Spruce-Integration-Guide

---

## **Contents**

- [What is Spruce?](#intro)
- [What is the Elation-Spruce integration?](#integration)
- [How do I get started?](#getting_started)
- [What information is synchronized?](#syncing)
- [Creating Contacts in Spruce from Elation](#contact_creation)
- [Linking Patients](#linking_patients)
- [Demographics Updates](#demographics_updates)
- [Message Syncing](#message_syncing)
 - [Selective Sync](#selective_sync)
 - [Automatic Sync](#automatic_sync)
- [Helpful Videos and Links About Using Elation and Spruce](#links)




## **What is Spruce?**

Spruce is a secure, HIPAA compliant communication platform that enables patients and their providers to readily connect. With Spruce, patients and providers can seamlessly discuss symptoms over messages, then have a phone call or virtual video appointment with their provider - all in one space. Both patients and providers can have peace of mind knowing that they can receive and give care in a secure, simple and adaptable way.

## **What is the Elation-Spruce integration?**

The Elation-Spruce integration allows you to

- automatically create charts for patients in Spruce when you create their chart in Elation
- easily keep patient contact information up to date in both systems
- automatically transfer your conversations from Spruce into Elation so that all of the patient's clinical data is easily stored in one place, your Elation EHR.

Read our [Telehealth Guide- Using Spruce alongside Elation for patient encounters](Using-Elation-Spruce-telehealth.md) article for more detailed information on how to utilize the different features in Spruce to complete Telehealth visits for documentation in Elation.

## **How do I get started?**

If you are interested in using the Elation-Spruce integration please [click here to notify Elation](https://help.elationhealth.com/s/contactsupport) and a member of the Implementation Team contact you about next steps.



## **What information is synchronized?**

Integrating Spruce to Elation offers additional benefits, such as Spruce Contact creation from Elation, contact information sync between systems, and correspondence syncing.

| | | | |
| --- | --- | --- | --- |
| **Elation** | | **Spruce** | **Notes** |
| Chart Creation | → | Contact Creation | Charts must be created in Elation to sync over to Spruce. Once the chart is created in Elation, the Contact will be created in Spruce instantaneously. |
| Demographic Edits | ↔ | Demographic Edits | Demographic edits can be made either in Elation or Spruce. Each time a change is made to a patient’s demographics in one platform, these changes will be reflected in the other platform. Only the following demographic information will sync:   - Patient first and last name - Phone numbers (up tp 2 different phone number types) - Email address - Date of birth - Gender |
| Visit Note or Report created\* | ← | Conversations | Conversations can be synced from Spruce to Elation through either manual syncing (Selective Sync) or Automatic Sync    \*Select Sync will create a Simple Note and Automatic Sync will create a *Miscellaneous*Report |






## **Creating Contacts in Spruce from Elation**

Patients must have a Contact in Spruce in order to be invited to communicate via SMS, Secure Message or Video. When you create a new chart in Elation, a new Contact for the patient will be created in Spruce immediately and this will also create the patient link. You will receive a message in your Spruce *Inbox* with a note describing this automation for record keeping purposes.

**Important Note:** Creating a new Contact in Spruce does not automatically create a new chart Elation chart. Patient/Contact creation only occurs from Elation to Spruce.



![]()




## **Linking patients**

If you have a Contact in Spruce for a patient that already has a chart in Elation, link these two together by following the steps below. This will ensure the Spruce messages for the patient will sync to the correct Elation Chart.

1. Select the patient's Contact in Spruce to open the contact card.
2. Scroll down to *Integrations* and click "Link Contact to EHR".
3. Select *Elation* from the drop down menu.
4. Search for the patient by the name or the Chart ID numberused for that patient in Elation.
   - This search must have the full first or last name in order to pull up the patient. It is not case sensitive.
5. Once the correct chart appears, select it and verify that the information from Elation matches the information you have in Spruce.
6. Click**"**Link" to connect the Elation chart with the Spruce contact.

To remove a link follow the above instructions and when under Integrations hover over the integration you want to unlink and you will see it will say "Remove Link" when you are hovered over.

To see Spruce's demonstration of this workflow, please click [here](https://www.loom.com/share/9a83b4ae4501408ca52c889f789abcc3).

## **Demographics Updates**

Once the patient is linked between Elation and Spruce, any updates in either system for the following demographics fields will be pushed to the other system immediately:

- Patient first and last name
- Phone numbers (up tp 2 different phone number types)
- Email address
- Date of birth
- Gender

## **Message Syncing**

There are two ways messages from Spruce can sync into Elation: Selective or Automatic.

#### **Selective Sync (Recommended)**

Selective sync allows you to choose one or more messages you would like to sync into Elation. This option allows you to control which messages you would like to copy to Elation. The message(s) chosen for syncing will populate into Elation as a Simple visit note. When using this option, you can select which patient chart in Elation the messages are filed under. The patient you are currently viewing in Spruce will be the default. To use Selective Sync:

1. Open the conversation in Spruce
2. Hover over any messages until three small vertical dotsappear to the right of the message and click on them.
3. Select the "Select Message" option from the menu.
4. Squares will appear to the left of each message that you can click to select the individual messages you would like to copy to Elation, they are selected when blue.
5. Click "Sync to Elation" at the top of the conversation, below the patient name
6. A box will pop up and if this patient is already linked to their patient chart in Elation it will be populated under patient
   - If the patient name is blank, search for the patient by full first and/or last name.
   - You can also edit to a different patient than what was prefilled
7. Enter a *Note Subject* if desired.
8. Click "Done" in Spruce to exit the select message view
9. Open or refresh the patient’s chart in Elation and sign off on the visit note in the Requiring Actions queue.
   - **Please Note**: If your practice utilizes Patient Passport, signing off on visit notes will automatically send the visit summary to the patient.

To see Spruce's demonstration of this workflow, please click [here](https://www.loom.com/share/ae02d980185e41a684cbafb225c94195).



![]()

#### **Automatic Sync**

Automatic sync will sync all new SMS and Secure Messages in Spruce automatically to Elation every 24 hours. With automatic sync, the messages from Spruce will populate into Elation as *Miscellaneous (MISC)* Reports.

To access in Elation, click on the "Reports" tab, then the MISC category to access all Spruce conversation reports for a patient.

**Please Note**: Whether using Selective Sync or Automatic Sync, the visit note or miscellaneous report will appear in the “Requiring Action” queue of the patient’s chart, and will require provider sign off to file in the patient’s chronological record.




## **Helpful Videos and Links About Using Elation and Spruce**

- Spruce Integration Help Center article: <https://help.sprucehealth.com/article/470-elation-integration>
- Elation-Spruce Link Charts Video: <https://www.loom.com/share/9a83b4ae4501408ca52c889f789abcc3>
- Elation-Spruce Selective Sync Video: <https://www.loom.com/share/ae02d980185e41a684cbafb225c94195>
- Spruce Help Site: <https://help.sprucehealth.com/>
- Elation Support: [Click here to contact Support](https://help.elationhealth.com/s/contactsupport)
- Spruce Support: [support@sprucehealth.com](mailto:support@sprucehealth.com)
- In-App Spruce Support: Search for *Spruce Support*

*© Spruce Health*

## **Related Articles**

- [Telehealth Guide- Using Spruce alongside Elation for patient encounters](Using-Elation-Spruce-telehealth.md)