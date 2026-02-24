# Calendar Guide - Managing cancellations, no-shows, overbooking, and recalls

Source: https://help.elationhealth.com/s/article/Calendar-Guide-Managing-special-appointment-use-cases

---

# Contents

- [Overview](#overview)
 - [How do I manage special appointment use cases?](#description)
 - [Why is managing appointment statuses important?](#why-is-managing-appointment-statuses-important)
 - [Why is using appointment reminders important?](#reminders_value)
- [Workflow Instructions](#workflow-instructions)
 - [Handling appointment cancellations](#handling-planned-cancellations)
    - [Canceling from the Calendar](#canceling-from-the-calendar)
    - [Using Quick Reschedule](#using-quick-reschedule)
    - [When patients cancel via appointment reminders](#when-patients-cancel-via-appointment-reminders)
 - [Handling unplanned no-shows](#handling-unplanned-no-shows)
    - [Setting the status to No Show](#setting-the-status-to-no-show)
    - [Tracking no-shows with reports](#tracking-no-shows-with-reports)
    - [Following up with no-show patients using Patient List](#following-up-with-no-show-patients-using-patient-list)
    - [Using Office Messages for recall workflows](#using-office-messages-for-recall-workflows)
 - [Overbooking and double-booking procedures](#overbooking-and-double-booking-procedures)
    - [Double-booking appointments](#how-to-double-book-appointments)
    - [Booking Site limitation for double-booking](#booking-site-limitation)
    - [Maintaining a manual waitlist](#no-native-waitlist)
 - [Using reminders and Booking Site configurations](#using-reminders-and-booking-site-configurations)
    - [Using appointment reminders to reduce no-shows](#how-reminders-reduce-no-shows)
    - [Booking Site cancellation and rescheduling behavior](#booking-site-cancellation-and-rescheduling-behavior)
    - [Checking reminder status for an appointment](#checking-reminder-status-for-an-appointment)
- [Frequently Asked Questions (FAQ)](#faq)

# Overview

## How do I manage special appointment use cases?

You can use appointment statuses and appointment reminders to keep your schedule accurate, reduce no-shows, and make it easier for your team to handle cancellations, overbooking, and follow-up work.

## Why is managing appointment statuses important?

Appointment statuses track where a patient is in their visit journey. Accurate status tracking helps your practice:

- Identify patients who need follow-up after missed appointments.
- Generate reports to analyze cancellation and no-show trends.
- Ensure billing workflows proceed correctly.
- Maintain visibility into provider schedules for the entire care team.

Elation supports the following appointment statuses:

| Appointment status | Meaning |
| --- | --- |
| Scheduled | Appointment is booked but the patient has not arrived. |
| Confirmed | Patient has confirmed the appointment via a reminder. |
| Checked In | Patient has arrived and demographics were verified |
| In Room / In Room - Vitals Taken | Patient is in an exam room. |
| With Doctor | Patient is with the provider. |
| Checked Out | Visit is complete. |
| Canceled | Appointment was canceled. |
| No Show (Not Seen) | Patient did not attend. |
| Billed | Billing has been processed. |

## **Why is using appointment reminders important?**

Automated appointment reminders ensure patients have the information they need to attend their visit. Reminders can also allow patients to confirm, reschedule, or cancel appointments directly—updating your calendar in real time.

For complete setup instructions, delivery options, and troubleshooting, see the [Calendar Guide - Using automated appointment reminders](https://help.elationemr.com/s/article/appointment-reminders) article.

# Workflow Instructions

## Handling appointment cancellations

When a patient notifies you in advance that they need to cancel, you can update the appointment status and optionally reschedule using [Quick Reschedule](#quick_reschedule).

### Canceling from the Calendar

| | |
| --- | --- |
| 1 | Click in the shaded area of the appointment to open the appointment popover box. |
| 2 | Update the Status to Canceled. |
| 3 | If the patient prefers to reschedule, use the Quick Reschedule workflow below. |

### Using Quick Reschedule

Quick Reschedule streamlines moving appointments by letting you instantly select a new date and time without leaving your current workflow.

| | |
| --- | --- |
| 1 | Click in the shaded area of the appointment to open the appointment popover box. |
| 2 | Click Show suggested times next to Quick Reschedule. |
| 3 | Select a new appointment time from the list of the next six available options, based on the appointment's Location, Duration, and the provider's Availability. |
| 4 | Click Save new time. |

ℹ️ **NOTE** The Location field must be filled in to use Quick Reschedule.

### When patients cancel via appointment reminders

If you have enabled the Allow patients to cancel their appointments online setting, patients can cancel directly from their appointment reminder.

When a patient cancels through a reminder:

- The appointment status updates to Canceled
- The patient receives a follow-up text or email
- If you use the Patient Booking Site, the patient will be prompted to book a new appointment
- The time slot becomes available for other patients to book

For complete setup instructions and configuration options, see the [Calendar Guide - Using automated appointment reminders](https://help.elationemr.com/s/article/appointment-reminders) article.

## Handling unplanned no-shows

When a patient misses their appointment without prior notice, update the status and use reports to track patterns and follow up.

### Setting the status to No Show

| | |
| --- | --- |
| 1 | Click in the shaded area of the appointment to open the appointment popover box. |
| 2 | Update the Status to No Show. |

ℹ️ **NOTE** The **No Show** status may appear as **Not Seen** in some reports.

### Tracking no-shows with reports

Use the Appointment Report or Appointment Dashboard to identify no-show patterns.

#### **Appointment Report**

| | |
| --- | --- |
| 1 | Click Reports → Appointment Report at the top of any page in Elation. |
| 2 | Select the provider and date range. |
| 3 | Click Update List. |
| 4 | Download as CSV to sort by appointment status and group all no-show appointments together. |

[Click here for more information about the Appointment Report](https://help.elationemr.com/s/article/Calendar-Guide-Searching-for-appointments-with-the-Appointments).

#### **Appointment Dashboard (Premium EHR Only)**

The dashboard displays a graph of **Appointments by Status** with quick-view counts for:

- Total Appointments
- Canceled Appointments
- No Show Appointments
- Canceled Ratio
- No-Show Ratio

[Click here for more information about the Appointment Dashboard](https://help.elationemr.com/s/article/Reporting-Guide-Built-in-appointment-and-visit-note-productivity-reporting#appointment_dashboard).

### Following up with no-show patients using Patient List

Use the Patient List Report to generate contact lists for appointment recalls.

| | |
| --- | --- |
| 1 | Click Reports → Patient List in the blue bar at the top of Elation. |
| 2 | Apply filters such as:    - Last Appointment – to find patients who haven't been seen recently - Next Appointment – to identify patients without upcoming visits - Patient Status – to filter for active patients |
| 3 | Click Generate List. |
| 4 | Use the results to contact patients and schedule follow-up appointments. |

💡 **USER TIP** The Patient List Report is useful for patient outreach—generate contact lists for preventive care reminders or appointment recalls.

For more details, see the [Patient List Report Guide - Searching your patient panel](https://help.elationemr.com/s/article/find-patients-with-elations-patient-list) article.

### Using Office Messages for recall workflows

You can use Office Messages to create internal reminders for patient follow-up.

| | |
| --- | --- |
| 1 | Send an Office Message about the patient to the appropriate staff member. |
| 2 | Use the Pd (post-date) field to schedule the message for a future date as a reminder. |
| 3 | Use the Recall patient Quick Reply option, which sends the message: "Please call the patient in for appointment." For more information, see the [Office Message Feature Guide - The enhanced inter-office communications tool](https://help.elationemr.com/s/article/Office-Message-Feature-Guide) article. |

## Overbooking and double-booking procedures

### Double-booking appointments

Elation allows you to book multiple appointments in the same time slot when scheduling manually.

To book multiple appointments in the same time slot, click on the white space to the right of the time slot. The most recently booked appointment will appear on top.

### Booking Site limitation for double-booking

Each appointment slot on the Patient Booking Site can only be booked by one patient. Elation does not allow double-booking the same time slot through the Booking Site.

If a provider is already booked for another appointment or event, the availability for that provider will be automatically updated on the Booking Site to avoid double-booking.

### Maintaining a manual waitlist

ℹ️ **NOTE** Elation does not currently have a native waitlist feature.

To manage patients waiting for earlier appointments, consider:

- Maintaining a manual list (spreadsheet or Office Message thread)
- Using the Patient List Report to identify patients who need rescheduling
- Contacting patients directly when cancellations occur

## Using appointment reminders and Booking Site configurations

Appointment reminders and Booking Site settings directly impact how your practice handles cancellations, no-shows, and rescheduling. Understanding these configurations helps you optimize your workflows.

### Using appointment reminders to reduce no-shows

Automated appointment reminders ensure patients are notified of their upcoming appointment in a timely manner.

For complete setup instructions, delivery options, and troubleshooting, see the [Calendar Guide - Using automated appointment reminders](https://help.elationemr.com/s/article/appointment-reminders) article.

### Booking Site cancellation and rescheduling behavior

When patients cancel through an appointment reminder:

- The appointment status updates to Canceled
- The time slot becomes available for other patients to book
- If Booking Site is enabled, patients are prompted to reschedule immediately

You can also share a cancellation policy message in your Booking Site settings.

ℹ️ **NOTE** Elation displays the cancellation policy but does not enforce it.

For full configuration options, see the [Patient Booking Site Guide](https://help.elationemr.com/s/article/Patient-Booking-Site) article.

### Checking reminder status for an appointment

To verify whether a patient received their reminders:

| | |
| --- | --- |
| 1 | Click in the shaded area of the appointment in the Calendar. |
| 2 | Select Edit. |
| 3 | Review the Activity Log section at the bottom of the appointment box. |

# Frequently Asked Questions

#### How do I see all no-show appointments for a time period?

Download the Appointment Report as a CSV file and sort by the **Status** column to group all no-show appointments together.

#### Can patients reschedule their own appointments?

Patients can confirm or cancel appointments via the appointment reminder and can then reschedule through the Booking Site, if the Booking Site is enabled. If they need to reschedule before receiving a reminder, they must call the office.

#### What happens when a patient cancels through the Booking Site or reminder?

The time slot becomes available for other patients to book.

#### Can I create a waitlist for patients who want earlier appointments?

Elation does not have a native waitlist feature. You will need to manage this manually and contact patients when openings occur.

#### Why didn't my patient receive an appointment reminder?

If the patient only has **Work**, **Night**, **Fax**, or **Other** phone number types in their demographics, Elation will not send reminders. Ensure patients have a **Mobile** phone (opted in to SMS), email address, or **Home**/**Main** phone number on file.

#### How do I track patients who are overdue for follow-up visits?

Use the Patient List Report with filters like Last Seen and Patient Status to identify patients who haven't been seen recently and need to schedule appointments.

# Related Articles

- [Calendar Guide - Using the Calendar for appointments & events](https://help.elationemr.com/s/article/how-to-use-elation-calendar)
- [Calendar Guide - Using automated appointment reminders](https://help.elationemr.com/s/article/appointment-reminders)
- [Patient Booking Site Guide](https://help.elationemr.com/s/article/Patient-Booking-Site)
- [Patient List Report Guide - Searching your patient panel](https://help.elationemr.com/s/article/find-patients-with-elations-patient-list)
- [Calendar Guide - Searching for appointments using the Appointment Report](https://help.elationemr.com/s/article/Calendar-Guide-Searching-for-appointments-with-the-Appointments)
- [Office Message Feature Guide - The enhanced inter-office communications tool](https://help.elationemr.com/s/article/Office-Message-Feature-Guide)