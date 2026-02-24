# Patient Forms Guide - Frequently Asked Questions

Source: https://help.elationhealth.com/s/article/Patient-Forms-Frequently-Asked-Questions

---

# **Contents**

- [Setting Up Patient Forms](#set)
- [Sending Patient Forms](#send)
- [Filling Out Patient Forms](#fill)
- [Reviewing Completed Patient Forms](#review)
- [Patient Forms and the Booking Site](#booking)

# **Frequently Asked Questions**

## **Setting Up Forms**

| | |
| --- | --- |
| Can I upload a PDF as my Elation medical history form? | Yes, you can upload the PDF file to the Patient Form builder and have it create a draft form for you to edit and customize. [Click here for more instructions](https://help.elationemr.com/s/article/Patient-Forms-Guide#upload_form). |
| Can patients electronically sign forms? | Yes, patients can electronically sign forms if you use the **Patient Signature** question in your form. |
| Are there any sample forms in the system for us to use? | Our team has added a few form templates that you can further customize. These are found under the **Create new form** button on the Patient Forms settings page. |
| Can we create forms in other languages? | You can modify the question prompt and helper text of our canned and **Other** question to be in another language. |
| Can we create forms with conditional questions (i.e. questions that only appear based on gender or age)? | Questions are not conditional in nature right now. We'd recommend adding phrases like 'if applicable' in the question prompt to indicate that it is not required for all patients. |
| Are any questions on the form mandatory? | Only the **Patient Signature** question has requirements. Other questions cannot be set as mandatory/required. If you'd like your patients to fill in all questions, please include those instructions in the Form Description. |
| Can I add more than one patient signature question to a single Patient Form? | Yes, you can add  multiple **Patient Signature** questions a form. |
| What is the character limit for the **Question Text** field? | The character limit for the **Question Text** field is 5,000 characters with the exception of the **Patient Signature** question which has a character limit of 50,000 characters. |

## **Sending Patient Forms**

| | |
| --- | --- |
| Does the patient need to have a Patient Passport account in order to receive and fill out forms? | The patient doesn't need to have a Patient Passport to receive forms. They only need to have their email address saved in Elation. |
| Will the patient be invited to Patient Passport when we send them their forms? | The patient will not be invited to Patient Passport when Elation sends them the forms. |
| Do I need to enable the booking site to send forms? | The Booking Site does not need to be enabled. |
| Can you send forms without scheduling a visit for the patient? | Currently, an appointment must be created to send forms to a patient. |
| Can I change the timing of when forms are automatically sent to the patient? | Yes, under **Calendar and Booking** -> **Appointment Types**, click **Edit** for the Appointment Type you'd like to customize. In the edit panel, you'll be able to configure forms to be sent to the patient upon creating their appointment, or X number of days prior to the appointment. |
| Can the same form be sent to the patient more than once? | Yes, patients can receive the same form multiple times via different appointments. Patients will be able to fill out patient forms each time they receive them. |
| If two patients have the same email, will they both be able to receive patient forms? | Yes, if multiple patient charts share the same email, each 'chart' will receive a copy of any patient forms attached to corresponding appointments they are scheduled for. |
| If we schedule patients through our Practice Management System (PMS), can we still send forms to patients? | As long as the appointment created in your PMS synchronizes to the Elation calendar, the patient will receive the forms that are linked to the appointment type. Please check that any Elation appointment types with forms are mapped to the appointment types in your PMS. |
| Can the forms link be sent to the patient via SMS? | Not at this time - forms are only delivered via email. |
| Can you send a form to a patient if the form hasn't been added to the appointment type of their scheduled appointment? | Right now, only the forms that are associated with the appointment type can be delivered to the patient. |
| If an appointment is canceled, will the forms link become invalid? | Yes, if an appointment is canceled/deleted from Elation, the patient will no longer be able to fill out forms for that encounter. |

## **Filling Out Patient Forms**

| | |
| --- | --- |
| Are the forms mobile friendly? | Yes, medical history forms are mobile friendly and will work on any device with an internet connection. |
| Can I use Elation as a kiosk? | Elation does not currently provide a dedicated kiosk user interface. However, you can use **Patient Forms** on a clinic-owned tablet in your waiting area to collect demographics, questionnaires, and consents from patients upon arrival. Combine this with staff-driven check-in in the **Calendar** and **Patient Payments** for copay collection to create a streamlined intake workflow. For a more robust intake experience with patient self-identification, consider a third-party intake partner such as Updox or IntakeQ. See the [Patient Intake & Check-In Options](https://help.elationemr.com/s/article/Patient-Intake-Check-In-Options) article for recommended patterns and partner integrations. |
| Besides free-text, can patients answer questions in more structured ways? (e.g. use dropdown list, radio buttons) | Most questions are built as free-text answers. Certain questions will support different types of responses. For example the **Smoking Status** and **Depression (PHQ-9)** questions have a drop down selection, and **Medical History** and **Family History** have checkboxes. |
| Can patients search a database to enter their preferred pharmacy? | Currently, patients can only enter a preferred pharmacy with free text. |
| Can patients save partially completed forms or edit responses that they've already submitted? | Once the form is submitted, the patient cannot go back and edit their responses to that form. If they have not submitted the form yet, they can use the same link that will bring them to a blank version of the form. Partially completed forms will not be saved. |
| Are patient signatures saved so the patient can re-use them on other forms? | No, a patient will need to individually sign each form where a signature is requested. |
| Can patients add/upload any attachments when they are submitting their forms? | Patients cannot currently add or upload any attachments when submitting a form. We recommend using Patient Passport if a patient needs to send an attachment to the practice. |
| Can a staff/nurse fill out the form on behalf of the patient? | A Provider or Staff member can fill out the form on behalf of the patient by accessing the form from the individual's appointment in the Calendar. Click **Copy URL** and paste it into a new browser tab to open the form. |

## **Reviewing Completed Patient Forms**

| | |
| --- | --- |
| Can we change where the patient's response exports to in the Clinical Profile? | Yes! For the **Other**question topic, you can customize where in the Clinical Profile you'd like to export the patient's response. First add the **Other** question topic to your form. Then click the **Export to** dropdown and select the section. |
| Can the answers submitted for one patient be shared across multiple patient charts? | Currently, answers will only be exported to the chart of the patient who filled it out. For example, the family history from one form that may apply to multiple children cannot be exported across multiple charts. |
| Can a staff user sign off on forms in the patient's chart? | Admin Level Users can turn on a setting for specific Patient Forms to allow Staff Level Users to sign off on forms responses. This feature is ideal for forms that generally do not require provider oversight such as forms for demographics or insurance collection. [Click here for information about this setting](https://help.elationemr.com/s/article/Patient-Forms-Guide#sign_permissions). |
| I can't select the insurance card images from the completed forms to export, why? | You must update the Insurance **Carrier Name**, **Plan Name**, **Group ID** or **Member ID** information on file by clicking **Edit** before you can export the images to the patient's demographics. This is to make sure your patients always have the correct insurance data stored in their chart. |

## **Patient Forms and the Booking Site**

| | |
| --- | --- |
| Can we list just the URL for the Telehealth appointment scheduling on our websites? | Yes, you can use the direct URL for the telemedicine appointment type and your patients will be directed right to this appointment type. |
| Does the patient information have to match when booking the appointment? Email/Phone? What if they input another email not on file? | The information goes through a matching algorithm to identify whether or not the patient exists in our system or is a new patient. If the information entered passes our checks as existing patient, we’ll add the appointment to that chart. If the patient information does not pass our check, but looks like it could be a duplicate, we’ll create a new chart and notify you that it could be a duplicate. If the patient information entered does not match, we’ll create a new chart. |
| Can you tell if an appointment was self-scheduled or scheduled by the practice? | The appointments will appear identical on your Elation Calendar, but you can turn on a setting that will send you an email each time an appointment is booked through the Booking Site. Please find this under **Settings** -> **Calendar & Booking** -> **Booking Site**, and scroll down to **Preferences**. |

**Related Articles**

- [Patient Forms Introduction](https://help.elationemr.com/s/article/Patient-Forms-Guide)
- [Patient Forms Guide - Creating and managing Patient Forms](https://help.elationemr.com/s/article/Patient-Forms-Guide)
- [Patient Forms Guide - Sending forms to patients](https://help.elationemr.com/s/article/Sending-forms-to-patients)
- [Patient Forms Guide - Managing forms responses](https://help.elationemr.com/s/article/Managing-forms-responses)
- [Patient Forms Guide - Receiving and filling out forms as a patient](https://help.elationemr.com/s/article/Receiving-and-filling-out-forms-as-a-patient)
- [Patient Forms Guide - Sample Forms & Uses Cases](https://help.elationemr.com/s/article/Patient-Forms-Sample-Forms-and-Use-Cases)
- [Patient Intake & Check-In Options](https://help.elationemr.com/s/article/Patient-Intake-Check-In-Options)