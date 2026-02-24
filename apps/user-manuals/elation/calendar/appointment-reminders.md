# Calendar Guide - Using automated appointment reminders

Source: https://help.elationhealth.com/s/article/appointment-reminders

---

# **Contents**

- [Overview](#overview)
 - [What are automated appointment reminders?](#description)
 - [Why are appointment reminders valuable?](#value)
    - [Reducing no-shows with reminders](#reducing_noshows)
 - How will my patients receive reminders?
 - What will appointment reminders look like to patients?
    - [SMS (Text Message) reminders](#sms)
    - [Email reminders](#email)
    - [Phone call reminders](#phone_call)
- [Workflow Instructions](#workflow)
 - [Setting up appointment reminders](#set_up)
 - [Adding place and location details to appointment reminders](#location)
 - [Adding visit instructions to appointment reminders](#instructions)
 - [Allowing patients to cancel appointments via reminders](#cancel)
    - [How patients can cancel from a reminder](#cancel_methods)
    - [After a patient cancels](#after_cancel)
 - [Checking if a patient received their appointment reminders](#reminder_audit)
 - [Using appointment reminders when your practice has multiple practice locations](#multiple_practice_locations)
- [Frequently Asked Questions (FAQ)](#faq)

# **Overview**

## **What are automated appointment reminders?**

In Elation, sending automated appointment reminders to patients is easy. You can send up to 3 reminders to patients ahead of a scheduled appointment. Each appointment reminder will contain the following details:

- Date and time of appointment
- Type of appointment (Appointment Type)
- Name of provider
- Address and phone number of practice (for ['In person' appointments](#location) only)
- A button to confirm the appointment
- (Optional) A button to [cancel](#cancel) the appointment
- (Optional) [Instructions](#instructions) for their appointment; including a link to join the video visit for virtual appointments

## **Why are appointment reminders valuable?**

Elation's automated appointment reminders help ensure that your patients have the information they need to attend their visit and will decrease the number of no-shows on your schedule. All of the information and actions needed to follow up on a scheduled appointment will be immediately available in each appointment reminder.

- For text and email appointment reminders, patients will be able to confirm and, if enabled, cancel their appointments directly through the reminder to give your practice more insight into the accuracy of each provider's Calendar
- Details or instructions entered into the **Visit Instructions** field within an appointment, for both in-person and virtual visits, will be automatically sent to your patients

### **Reducing no-shows with reminders**

Appointment reminders are one of the most effective tools for reducing patient no-shows. To maximize their impact:

- **Send multiple reminders.** Configure up to 3 reminders per appointment. A common approach is to send reminders 7 days prior, 1–2 days prior, and 1 hour before the appointment.
- **Combine reminders with clear visit instructions.** Patients are more likely to attend when they know exactly what to expect—where to go, what to bring, and how to prepare. Use the **Visit instructions for patient** field to provide this information.
- **Enable appointment confirmation and cancellation.** When patients can confirm or cancel directly from the reminder, your practice gains real-time visibility into schedule accuracy and can fill open slots sooner.

## **How will my patients receive reminders?**

Patients will receive appointment reminders based on the patient's preferred contact method. You can set-up your patient's preferred method in the **Contact Information**section of the patient's demographic window in each patient's chart.

If the patient does not have a preferred contact method selected, then Elation will use the following hierarchy to determine how the reminder will be sent based on what information that is available within the **Contact Information** section of the patient's demographics:

1. Patient's Passport account contact preference (the default setting is email). If the patient does not have a Patient Passport account, then:
2. SMS (Text Message) to the **Mobile** phone number type stored in the patient's **Contact Information**(if the patient [opted in to receiving SMS (Text Messages)](SMS-Text-Message-Opt-In-Guide.md). If a **Mobile** phone type is not available or the patient did not opt in to receiving SMS, then:
3. Email notification to the email address stored in the patient's **Contact Information**. If no email address is available, then:
4. Phone call to a **Home** or **Main** phone number (or the **Mobile** phone number if patient opted out of SMS)stored in the patient's **Contact Information***.*
5. If none of the above details are available in the patient's **Contact Information***,* then the patient will not receive any automated appointment reminders from Elation.

ℹ️  **NOTE**

- The patient must have a **Mobile** phone listed as a one of the phone types in their demographics window and be [opted in to receiving SMS (Text Messages)](SMS-Text-Message-Opt-In-Guide.md) in order to receive text appointment reminders. If the patient did not opt in to receive SMS (Text Message), then the **Mobile** phone will receive a phone call reminder instead.
- If the patient only has **Work**, **Night**, **Fax**, or **Other** phone number types available in their demographics window, then Elation will not send any reminders to the patient.

## **What will appointment reminders look like to patients?**

Below are examples of what the appointment reminders will look like to your patients.

### **SMS (Text Message) reminders**

SMS (Text Message) reminders will go to the patient's SMS-enabled cellular phone (if they [opted in to receiving SMS (Text Messages)](SMS-Text-Message-Opt-In-Guide.md) and will come from the number *36331*. The text message will contain a URL for the patient to click on to:

- see additional details about their appointment, including:
 - Date and time of appointment
 - Type of appointment (Appointment Type)
 - Name of provider
 - Address and phone number of practice (for ['In person' appointments](#location) only)
    - See the *'[Appointment reminders for practices with multiple practice locations' section](#multiple_practice_locations)* below for additional details about practices with multiple practice locations.
- confirm their appointment
- (optional) [cancel](#cancel) their appointment
- (optional) view [instructions](#instructions) about their appointment; including a link to join the video visit for virtual appointments

**💡 USER TIP** Elation will continue to send reminders to patients even after a patient confirms their appointment until all reminders are sent.

### **Email reminders**

Email reminders will come from the email address *[reminders@elationemr.com](mailto:reminders@elationemr.com)* and will contain the following details:

- Date and time of appointment
- Type of appointment (Appointment Type)
- Name of provider
- Address and phone number of practice (for ['In person' appointments](#location) only)
 - See the *'[Appointment reminders for practices with multiple practice locations' section](#multiple_practice_locations)* below for additional details about practices with multiple practice locations.
- A button to confirm the appointment
- (Optional) A button to [cancel](#cancel) the appointment
- (Optional) [Instructions](#instructions) for their appointment; including a link to join the video visit for virtual appointments

**💡 USER TIP** Elation will continue to send reminders to patients even after a patient confirms their appointment until all reminders are sent.

### **Phone call reminders**

Phone call reminders will be sent as an automated voice call to the **Home** or **Main** phone types (or the **Mobile** phone type if patient opted out of SMS)stored in the patient's **Contact Information***.* The call with come from a California area code phone number and will have the following message:

*Hello. This is a courtesy reminder that you have an appointment with [Provider's full name] at [Date & Time of appointment]. If you have any questions or need to change your appointment, then please contact the office by calling [Practice's phone number]. Once again, you have an appointment with [Provider's full name] at [Date & Time of appointment]. If you have any questions or need to change your appointment, then please contact the office by calling [Practice's phone number].*

See the *'[Appointment reminders for practices with multiple practice locations' section](#multiple_practice_locations)* below for additional details about practices with multiple practice locations.

# **Workflow Instructions**

## **Setting up appointment reminders for my practice**

To turn on appointment reminders for your practice,

1. Go to **Settings** -> **Calendar & Booking** -> **Reminders**.
2. Choose the number of reminders you would like patients to receive and the time frame you want each reminder to be sent.
   - You can insert any number between 1 and 365 into the text fields provided.
   - The most recent option is **1 hour in advance***.*
3. Data entered in the reminders will automatically be saved on the page.

In the example below, patients will receive the appointment reminders 7 days prior, 3 days prior and 1 hour prior to their scheduled appointment:

![]()

## **Adding place and location details to appointment reminders**

Appointment reminders will vary based on the appointment **Location** specified (if applicable) and the appointment **place** selected ('In person' vs. 'Virtual').

1. To add additional Practice Locations, view our [Practice Locations Guide](adding-a-second-practice-location.md)
   - See the *'[Appointment reminders for practices with multiple practice locations' section](#multiple_practice_locations)* below for additional details about practices with multiple practice locations.
2. To set a place, choose **In Person** or **Virtual** in the appointment details window
   - If the **Visit instructions for patient** field is filled out, the appointment reminder will include those instructions. For **Virtual** visits, you can set [default Virtual Visit Instructions](https://app.elationemr.com/settings/telehealth/).
   - If you select **Virtual**, the reminders will also include references to the appointment being conducted virtually.

## **Adding visit instructions to appointment reminders**

You can use the **Visit instructions for patient** field to send additional instructions to patients for their visit. For **Virtual** visits, you can set [default Virtual Visit Instructions](https://app.elationemr.com/settings/telehealth/). Some common use cases of the instructions include:

- safety guidelines for visiting the office during the COVID-19 public health emergency
- how to locate the office
- where to find parking
- how to prepare for the visit
- what to bring to the visit

**VIRTUAL VISITS**When an appointment is set to **Virtual**, your default virtual visit instructions—including the video link—are automatically included in appointment reminders. Patients receive everything they need to join the video visit directly from the reminder.

To set or update your default virtual visit instructions, go to **Settings** -> **Virtual Visit** -> **Virtual visit Preferences**.

For more information on conducting virtual visits, see [Elation Integrated Video - Connecting with patients using video](Elation-Telehealth-powered-by-Zoom.md)

You can add visit instructions at the time of creating the appointment or after the appointment has been created by clicking **Edit** in the top right of the appointment window

ℹ️  **NOTE**

- If you edit the visit instructions after appointment reminders are sent, then you will need to click the **Send** button next to the visit instructions to manually send updated visit instructions to patients.
- The Zoom link generated by Elation (when you first sign up for Virtual Visits) must be included in the visit instructions for virtual visits. If the Zoom link is not included, the patient will not have a link to join the virtual visit.


![]()

After adding visit instructions to the appointment, you can send the instructions to the patient right away by clicking **Send**/**Resend**. The instructions will automatically be included in the next reminder that will be sent to the patient.

Email Reminder:
![]()

SMS (text message) Reminder:
![]()

## **Allowing patients to cancel appointments via reminders**

To allow patients to cancel their appointment from appointment reminders:

1. Go to **Settings** -> **Calendar & Booking** -> **Reminders**.
2. Click the button next to **Allow patients to cancel their appointments online** to turn it on (green).

![]()

This will cause appointment reminders to include the option for patients to cancel their appointment. If the patient cancels their appointment from the appointment reminder, the patient will receive a follow-up text or email. If you are using the [Patient Booking Site](Patient-Booking-Site.md), then the patient will be able to book a new appointment with you.

### **How patients can cancel from a reminder**

Patients can cancel an appointment directly from their reminder in two ways:

- **From the reminder link:** If you enable the **Allow patients to cancel their appointments online** setting, patients can cancel directly from their SMS or email reminder.
- **By phone:** Patients can call your practice using the phone number included in the reminder.

### **After a patient cancels**

When a patient cancels an appointment from a reminder, they receive a follow-up text or email confirming the cancellation.

If your practice uses the [Patient Booking Site](Patient-Booking-Site.md), patients who cancel via the reminder will be prompted to reschedule online.

Patients with a [Patient Passport](what-patient-passport-messaging-looks-like-to-a-patient.md) account can also access your Booking Site link directly from their Passport to reschedule at any time.

## **Checking if a patient received their appointment reminders**

The appointment activity log will show you when and how appointment reminders were sent to your patients.

To view the appointment activity log:

1. Click in the shaded area of the appointment in the Elation Calendar.
2. Select **Edit**.
3. Review the appointment reminder details in the Activity Log section at the bottom of the appointment box.

## **Using appointment reminders when your practice has multiple practice locations**

For practices with multiple [Practice Locations](adding-a-second-practice-location.md), remember to select the appropriate **Location** when adding patient appointments to the Calendar to ensure the correct practice address and phone number are shared with patients in their appointment reminders. If no **Location** is selected then the address and phone number of the 'Primary Location' for your practice (as designated in your Practice Location Settings) will be shared with patients in their appointment reminders.

**💡USER TIP** If preferred, you can ask Elation to turn on a feature for you so that practice phone numbers are never shared with patients in their appointment reminders when no **Location** is selected. Have an Admin Level User in the practice click the **I need help** -> **I need help from an Elation Team Member** button to submit a request and a member of the Support Team will assist you with turning this feature on.

# **Frequently Asked Questions (FAQ)**

#### **Can I customize the language for appointment reminders?**

Appointment reminder language cannot be customized at this time. Due to the various capabilities and features tied to appointment reminders, Elation has standardized the details disclosed via the various appointment reminders to make sure patients have the most important information needed to show up correctly and on time for their appointment. Use the [instructions](#instructions) field to disclose additional instructions or details to the patient as needed.

#### **A patient said they never received their appointment reminder. What should I do?**

1. The [appointment activity log](#reminder_audit) will show you when and how appointment reminders were sent to your patients. To view the appointment activity log:
   1. Click in the shaded area of the appointment in the Elation Calendar.
   2. Select **Edit**.
   3. Review the appointment reminder details in the **Activity Log** section at the bottom of the appointment box.
2. If the activity log says the patient received a reminder via email
   1. verify the patient's email address is spelled correctly.
   2. ask the patient to search their email inbox for any emails from *[reminders@elatiomemr.com](mailto:reminders@elatiomemr.com)* (especially their Spam/Junk) folders.
3. If the activity log says the patient received a reminder via SMS (Text Message)
   1. verify the patient's **Mobile**phone number is accurate.
   2. verify the patient's **Mobile**phone number can receive SMS (Text Message).
   3. have the patient check with their mobile service provider to see if the mobile service provider might have blocked the *36331* phone number used to send SMS reminders.
4. If the activity log says the patient received a phone call
   1. verify the patient's **Home**or**Main**phone number is accurate.
   2. ask the patient if they received any missed calls from a California area code phone number during the reminder timeframe you specified.
   3. ask the patient if they received any voicemails from a California area code phone number during the reminder timeframe you specified.

ℹ️ **NOTE** If appointments are added to the Calendar after the timeframe specified for appointment reminder frequencies, then the patient will not receive that reminder. For example:

- Today is March 1, 2022. You have your appointment reminder preference set for **2 days in advance**. You add an appointment to the calendar dated March 2, 2022. The patient will not receive any appointment reminders because it falls out of the specified **2 days in advance** timeframe.

#### **My patient has a Mobile phone number on file but they received a phone call instead. Why did this happen?**

Patients will only receive a SMS (Text Message) to the **Mobile** phone number type stored in the patient's **Contact Information**if the patient [opted in to receiving SMS (Text Messages)](SMS-Text-Message-Opt-In-Guide.md). If the patient did not opt in to receiving SMS then they will receive a phone call to **Mobile** phone number.

#### **A patient said they received an appointment reminder but the details of the reminder was incorrect. What should I do?**

Ask the patient to show you the exact reminder they received if possible and compare it with the details of their appointment. If the reminder does not match the appointment, take a picture of the reminder the patient received. Afterwards, notify the Support Team via the **I need help** button or [fill out this form](https://help.elationhealth.com/s/contactsupport) and our Support Team will investigate the cause behind the incorrect reminder details. The Support Team may also ask you to email them a copy of the picture of the reminder.

#### **Why is a reminder not sent if the patient only has *Work*, *Night*, *Fax*, or *Other* phone number types available in their demographics window?**

Information within appointment reminders are considered Protected Health Information (PHI). In order to ensure only the patient has access to their own PHI, we can only send appointment reminders to **Contact Information** that is normally only tied to the patient themselves.

#### **My patient received another reminder even after they confirmed their appointment. Why?**

Each customer can set up to 3 automated reminders for patient appointments. The timeframe of reminders vary and patients may forget about an appointment even after they confirmed their appointment. Elation will send out all scheduled appointment reminders, even to patients who have confirmed their appointment, to ensure patients show up for their appointment.

#### **When is the *1 day in advance* appointment reminder sent?**

The **1 day in advance** appointment reminder is sent more than 24 hours before the scheduled appointment. For example, if the appointment is on May 4th at 3pm Pacific then the appointment reminder is sent sometime before 3pm Pacific on May 3rd. The same rule applies to all "days in advance" options.

#### **When is the *1 hour in advance* appointment reminder sent?**

The **1 hour in advance** appointment reminder is sent the hour before the scheduled appointment. For example, if the appointment is at 3pm then the appointment reminder is sent between 1pm and 2pm.

**Next Step

Set up automated appointment reminders for your practice to ensure your patients never miss their appointment.**

# **Related Articles**

- [SMS (Text message) Opt-In Guide](SMS-Text-Message-Opt-In-Guide.md)
- [Practice Locations Guide- Listing your service locations](adding-a-second-practice-location.md)
- [Patient Booking Site Guide](Patient-Booking-Site.md)