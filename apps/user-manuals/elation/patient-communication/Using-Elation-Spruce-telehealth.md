# Telehealth Guide- Using Spruce alongside Elation for patient encounters

Source: https://help.elationhealth.com/s/article/Using-Elation-Spruce-telehealth

---

## **Contents**

- [What is Spruce?](#intro)
- [What is the Elation-Spruce integration?](#integration)
- [Quick tips for using Spruce with Elation](#tips)
- [Inviting your patients to communicate via Spruce](#invite)
 - [Contacts in Spruce](#Contacts)
 - [Inviting your patients from](#invite_from_inbox)
    - [The inbox](#invite_from_inbox)
    - [A new message](#invite_from_message)
    - [Contacts](#invite_from_contacts)
- [Composing messages in Spruce](#message)
 - [Starting messages](#starting_message)
 - [Adding attachments](#attachments)
 - [Using Saved Messages](#saved_messages)
 - [Schedule a message](#scheduling_message)
- [Having a video call with your patient](#call)
 - [Before the Video Call](#before_video)
 - [Starting a Video Call](#starting_video)
 - [After the Video Call](#after_video)
- [Transferring your conversations into Elation without an integration](#transfer)
 - [Formatted Copy & Paste](#copy_paste)
 - [Conversation Links](#conversation_links)
- [Elation-Spruce integration- How syncing works](#syncing)
 - [Creating Contacts in Spruce from Elation](#contact_creation)
 - [Linking patients](#linking_patients)
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
- automatically transfer your messages (especially telehealth related) from Spruce into Elation so that all of the patient's clinical data is easily stored in one place for billing purposes.

See the [Elation-Spruce- Message Sync Integration Guide](Elation-Spruce-Integration-Guide.md) for more detailed information about the integration features.

## **Quick tips for using Spruce with Elation**

#### **Do I need to sign up for the “integrated” Spruce option to be able to provide and bill for telehealth?**

No, you do not! The benefit of using the integrated experience with Spruce is that you will not need to individually create patients in Spruce and you can more easily sync copies of conversations from Spruce to Elation. However, you can still use Spruce for telehealth visits alongside Elation without using the integration. Please see the [Transferring your conversations into Elation without an integration](#transfer) section for more information.


#### **What virtual services can I bill for by using Spruce?**

There are 3 main types of virtual services recognized by Medicare and commercial payers. The following table covers which services you can deliver with Spruce.

| | | |
| --- | --- | --- |
| **Virtual Service** | **Description** | **Spruce Workflow** |
| Telehealth | Full patient visits performed in real time with video and audio | Hold a visit with your patient with a video call |
| Virtual Check-ins | Patient initiated brief communication via phone or review of patient-submitted images that mitigates the need for an in-person visit | Phone: have a phone call with your patient through Spruce (or with your regular phone) Review of patient-submitted images: Review images sent to you by the patient. Respond via phone, email, or message. |
| eVisit | Patient-initiated communication via an online patient portal | Cannot be completed in Spruce as a certified patient portal must be used. Please use Elation’s Patient Passport instead. |

Please refer to this [help center article](Telehealth-Coding-and-Workflows-Recommendations.md) for more information about virtual services.

#### **What workflow would you recommend for Telehealth visits?**

1. In Elation, schedule the patient for a virtual visit. Remind them to install and set-up their Spruce account prior to the visit date.
2. When you are ready to start the virtual visit, message your patient with Spruce to check if they are ready. Next, initiate your video call in Spruce.
3. Create your visit note in Elation. Update the visit note category to *Telehealth*.
   - **User Tip**: Learn how to create a *Telehealth* category using the [Visit Note Categories Guide](visit-note-categories.md)
4. Apply the *Telehealth* visit note template to document the details of the video call.
   - **User Tip**: Elation pre-loaded a simple *Telehealth* Visit Note Template to your own during your Account Set Up. Learn how to create your own Telehealthvisit note template using the [Visit Note Templates Guide](elation-visit-note-templates.md)
5. Bill for the E/M code that you would have used for an equivalent in-office visit. Depending on the patient’s insurance, make sure you add any necessary modifiers and Place of Service. (See Elation's Telehealth Billing Guidelines [here](Telehealth-Coding-and-Workflows-Recommendations.md) to understand the latest Telehealth billing requirements.)

**How do I bill for a Virtual Check-in?**

Since billing codes can only be added to Visit Notes in Elation, click on "Visit Note" in the patient’s chart followed by "Simple Note". Change the visit note category to *Telehealth* and document a description of the virtual check-in. Add the billing codes to this visit note and then sign the visit note.

**User Tip**: Learn how to create a *Telehealth* category using the [Visit Note Categories Guide](visit-note-categories.md)

## **Inviting your patients to communicate via Spruce**

Spruce allows providers to communicate with their patients via SMS and/or Secure Messaging directly within Spruce. SMS communications will be sent to patients mobile phone as text messages, while Secure Messaging will take place in the Spruce application and requires the patient to install the Spruce application on their mobile device.

#### **Contacts in Spruce**

Patients must have a Contact in Spruce in order to be invited to communicate. To add a new contact:

1. Click on the ![]() Contacts icon
2. Click "New Contact"
3. Enter the patient's name, date of birth, contact information and another other demographics details
4. Click "Save"


See the [Elation-Spruce Integration- How syncing works](#syncing) section to learn more about how Elation can help you create Spruce Contacts and what information is synchronized.

#### **Inviting your patients from the Inbox**

1. Click the ![]() Inbox icon in the menu bar
2. When the Inbox opens, click the ![]() Compose icon.
3. Click "Invite Patient" from the dropdown
4. Select the type of invitation method you need to use
   1. Use the search box to search for an existing patient
   2. Click the "Invite a new patient" button to invite a new patient
      - Enter the patient’s name, phone number, and/or email address
5. Click "Send Invite"
6. A new conversation window will open for you and the patient

#### **Inviting your patients from a new message**

1. Click the ![]() Inbox icon in the menu bar
2. When the Inbox opens, click the ![]() Compose icon.
3. Click "Secure Message" or "SMS" depending on the conversation method you want to use.
   - SMS communications will be sent to patients mobile phone as text messages, while Secure Messaging will take place in the Spruce application and requires the patient to install the Spruce application on their mobile device.
4. Search for the patient in the "to:" field.
   - Patient who have already been invited to a conversation will display in Blue. Patients who need an invite will display in Gray.
5. Select the patient you want to invite
6. Spruce will automatically send the patient an invite.

**Inviting your patients from your contacts**

1. Click on the ![]() Contacts icon
2. Click "Invite Patient"
3. Select the type of invitation method you need to use
   1. Use the search box to search for an existing patient
   2. Click the "Invite a new patient" button to invite a new patient
      - Enter the patient’s name, phone number, and/or email address
4. Click "Send Invite"
5. A new conversation window will open for you and the patient

![]()


## **Composing messages in Spruce**

#### **Starting messages**

1. Click the ![]() Inbox icon in the menu bar
2. When the Inbox opens, click the ![]() Compose icon.
3. Click "Secure Message" or "SMS" depending on the conversation method you want to use.
   - SMS communications will be sent to patients mobile phone as text messages, while Secure Messaging will take place in the Spruce application and requires the patient to install the Spruce application on their mobile device.
4. Search for the patient in the "to:" field.
   - Patient who have already been invited to a conversation will display in Blue. Patients who need an invite will display in Gray and an invitation will automatically be sent to them if they need one.
5. Start typing your message in the *Type a message...*box
6. Click "Send >" to send your message

#### **Adding attachments**

- For both SMS and Secure Message, you are able to attach files like photos, videos, and PDFs. ![]()
- For Secure Messages, you are able to attach additional items, such as a Spruce Visit or a Payment Request (if you are using Spruce's integrated payments) ![]()

#### **Using Saved Messages**

- Use your Saved Messages for quick actions or responses
- You can be creative with these, but common uses are for booking an appointment, reminding patients about an appointment, quick check-ins, and sharing contact information.

#### **Scheduling a message**

- If you’d like to send out a message at a specific date or time, simply compose your message and schedule the preferred date/time and press the “Schedule” button. You will see the message queued in the patient conversation dialog box.

**Please Note**: While Spruce's app to app conversations are HIPAA compliant, SMS communications that go outside of the Spruce platform will require patient consent. You can read more about Spruce’s White Paper on HIPAA compliance [here](https://spruce.docsend.com/view/nur46mb). There is a template for obtaining patient consent for SMS/email messaging on page 12.




## **Having a video call with your patient**

#### **Before the Video Call**

To initiate a video call with the patient, the patient must be invited to Secure Message and have the Spruce mobile app downloaded on their phone.

For best practices, we recommend recording the appointment or scheduled video call in Elation and then sending a message to the patient a few minutes prior to the start of the video call to ensure the patient is prepared and the video call is not missed.

#### **Starting the Video Call**

Once ready, the provider can begin a video call by clicking on the patient's name from the Secure Message and then click the *Video*icon.

![]()

#### **After the Video Call**

Once the call has ended, Spruce will automatically log the date and duration of the video call.

Providers can then use the *Internal* notes section to document the visit from the video call directly in Spruce and use either the [manual transfer method](#transfer) or [Elation-Spruce integration](#syncing) to transfer the information to Elation to begin billing.

**User Tips**:

- Only providers are able to initiate a video call.
- Spruce video calls are not recorded.




## **Transferring conversations into Elation without an integration**

Using Spruce without the Elation-Spruce integration, providers and staff can transfer Telehealth visit documentation from Spruce to Elation using the following methods: Formatted Copy & Paste and Conversation Links.

#### **Formatted Copy & Paste**

To make the transfer for patient communications easy, Spruce has a conveniently formatted copy and paste feature. To copy specific messages from Spruce to Elation:

1. Open the patient’s conversation in Spruce.
2. Highlight the relevant messages and copy, or click the three dots icon next to a specific message, then click “Select Message” >> "Copy Messages"
3. In Elation, open a visit note or the desired location, and paste the message content. The formatted text will include the timestamp of the message, the sender of the message, and the channel in which it was sent.

#### **Conversation links**

Spruce also has conversation links, which are unique links that allow providers and staff to seamlessly access the conversation that took place.

To copy the conversation link from Spruce to Elation:

1. Open the patient conversation in Spruce.
2. Press the ![]() Conversation Link icon at the top of the Spruce conversation

![]()

1. Paste the Conversation Link into Elation using your preferred note format.
   - **Please Note**: You must be logged into Spruce to access this link in the future.




## **Elation-Spruce Integration- How syncing works**

Integrating Spruce to Elation offers additional benefits, such as Spruce Contact creation from Elation, contact information sync between systems, and correspondence syncing. If you are interested in these additional benefits, please [click here to notify Elation](https://help.elationhealth.com/s/contactsupport).

| | | | |
| --- | --- | --- | --- |
| **Elation** | | **Spruce** | **Notes** |
| Chart Creation | → | Contact Creation | Charts must be created in Elation to sync over to Spruce. Once the chart is created in Elation, the Contact will be created in Spruce instantaneously. |
| Demographic Edits | ↔ | Demographic Edits | Demographic edits can be made either in Elation or Spruce. Each time a change is made to a patient’s demographics in one platform, these changes will be reflected in the other platform. Only the following demographic information will sync:   - Patient first and last name - Phone numbers (up tp 2 different phone number types) - Email address - Date of birth - Gender |
| Visit Note or Report created\* | ← | Conversations | Conversations can be synced from Spruce to Elation through either manual syncing (Selective Sync) or Automatic Sync    \*Select Sync will create a Simple Note and Automatic Sync will create a *Miscellaneous*Report |



### **Creating Contacts in Spruce from Elation**

Patients must have a Contact in Spruce in order to be invited to communicate via SMS, Secure Message or Video. When you create a new chart in Elation, a new Contact for the patient will be created in Spruce immediately and this will also create the patient link. You will receive a message in your Spruce Inbox with a note describing this automation for record keeping purposes.

**Important Note**: Creating a new Contact in Spruce does not automatically create a new chart Elation chart. Patient/Contact creation only occurs from Elation to Spruce.

###

### **Linking patients**

1. Select the patient's contact in Spruce to open the contact card.
2. Scroll down to Integrations and click "Link Contact to EHR".
3. Select *Elation* from the drop down menu.
4. Search for the patient by the name or the Chart ID numberused for that patient in Elation.
   - This search must have the full first or last name in order to pull up the patient. It is not case sensitive.
5. Once the correct chart appears, select it and verify that the information from Elation matches the information you have in Spruce.
6. Click**Link** to connect the Elation chart with the Spruce contact.

To remove a link follow the above instructions and when under Integrations hover over the integration you want to unlink and you will see it will say "Remove Link" when you are hovered over.

To see Spruce's demonstration of this workflow, please click [here](https://www.loom.com/share/9a83b4ae4501408ca52c889f789abcc3).

### **Message Syncing**

There are two ways messages from Spruce can sync into Elation: Selective or Automatic.

#### **Selective Sync (Recommended)**

Selective sync allows you to choose one or more messages you would like to sync into Elation. This option allows you to control which messages you would like to copy to Elation. When using this option, you can select which patient chart in Elation the messages are filed under. The patient you are currently viewing in Spruce will be the default.

The message(s) chosen for syncing will populate into Elation as a Simple visit note and you will be able to [add Telehealth billing information directly](Telehealth-Coding-and-Workflows-Recommendations.md) to the Simple visit note directly.

To use Selective Sync:

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

Automatic sync will sync all new SMS and Secure Messages in Spruce automatically to Elation every 24 hours. With automatic sync, the messages from Spruce will populate into Elation as *Miscellaneous (MISC)* Reports. This option can be used to attach supporting documentations when [billing for Virtual Check-Ins.](Telehealth-Coding-and-Workflows-Recommendations.md)

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

- [Elation-Spruce- Message Sync Integration Guide](Elation-Spruce-Integration-Guide.md)