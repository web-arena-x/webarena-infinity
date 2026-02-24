# Scheduling Capabilities Overview

Source: https://help.elationhealth.com/s/article/Scheduling-capabilities

---

# Contents

- [Overview](#overview)
 - [What are Elation's scheduling capabilities?](#what-are-elations-scheduling-capabilities)
 - [Why are scheduling capabilities important?](#why-are-scheduling-capabilities-important)
- [Key Scheduling Features](#key-scheduling-features)
 - [Calendar](#calendar)
 - [Patient Booking Site](#patient-booking-site)
 - [Provider Availability](#provider-availability)
 - [Appointment Types](#appointment-types)
 - [Recurring Appointments](#recurring-appointments)
 - [Quick Reschedule](#quick-reschedule)
 - [Calendar Blocks and Non-Blocking Events](#calendar-blocks-and-non-blocking-events)
 - [Automated Appointment Reminders](#automated-appointment-reminders)
- [Feature Comparison](#feature-comparison)
- [Getting Started](#getting-started)
- [Frequently Asked Questions (FAQ)](#faq)

# Overview

## What are Elation's scheduling capabilities?

Elation offers a comprehensive suite of scheduling tools designed to help practices efficiently manage patient appointments, provider availability, and patient self-scheduling. These tools work together to streamline scheduling workflows, reduce administrative burden, and improve patient access to care.

## Why are scheduling capabilities important?

Effective scheduling capabilities help practices:

- **Reduce administrative workload** - Automate appointment booking and reminders to free up staff time.
- **Improve patient access** - Allow patients to self-schedule appointments online at their convenience.
- **Optimize provider time** - Manage availability across multiple locations and appointment types.
- **Minimize no-shows** - Send automated reminders to confirm appointments.
- **Support care continuity** - Schedule recurring appointments for patients who need ongoing care.

# Key Scheduling Features

## Calendar

The Calendar is the central scheduling tool in Elation, used to manage provider availability and patient appointments.

| | |
| --- | --- |
| **Feature** | **Description** |
| **Standard View** | View a single provider's daily schedule. |
| **Expanded View** | View multiple days or multiple providers side by side. |
| **Appointment Management** | Create, edit, and delete appointments. |
| **Patient Check-in** | Update appointment status as patients arrive. |
| **Virtual Visit Support** | Distinguish virtual from in-person appointments with a video icon. |

For detailed instructions, see the [Calendar Guide - Using the Calendar for appointments & events](https://help.elationemr.com/s/article/how-to-use-elation-calendar) article.

## Patient Booking Site

The Patient Booking Site is a personalized web page where patients can self-schedule appointments based on provider availability.

| | |
| --- | --- |
| **Feature** | **Description** |
| **Online Self-Scheduling** | Patients can book appointments 24/7 from any device. |
| **Real-Time Availability** | Shows only available time slots based on provider settings. |
| **Customizable URL** | Personalize your booking site link for your practice. |
| **Multi-Location Support** | Patients can select their preferred practice location. |
| **Patient Forms Integration** | Automatically send intake forms when patients book. |

ℹ️ **NOTE** To enable the Booking Site, each provider must configure their availability in the **Calendar & Booking** settings.

For setup instructions, see the [Patient Booking Site Guide](https://help.elationemr.com/s/article/Patient-Booking-Site) article.

## Provider Availability

The Provider Availability settings allow you to define when each provider is available for appointments, by practice location and appointment type.

| | |
| --- | --- |
| **Feature** | **Description** |
| **Location-Specific Availability** | Set different hours for each practice location. |
| **Appointment Type Filtering** | Specify which appointment types are available during each time block. |
| **Time Zone Management** | Assign time zones to each location for accurate patient communication. |
| **Visual Indicators** | Gray vertical bars on the calendar show availability; diagonal stripes show unavailable times. |

For configuration instructions, see the [Calendar & Booking Site Guide - Enhanced Provider availability by Practice Location & Appointment Type](https://help.elationemr.com/s/article/Calendar-Booking-Site-Guide-Enhanced-Provider-availability-by-Practice-Location-Appointment-Type) article.

## Appointment Types

Appointment Types define the different kinds of appointments your practice offers, such as office visits, physicals, or telehealth consultations.

| Setting | Description |
| --- | --- |
| **Name & Color** | Customize the name and color for easy identification on the calendar. |
| **Default Duration** | Set how long each appointment type typically lasts. |
| **Visit Note Template** | Automatically apply templates when starting a visit note. |
| **Patient Forms** | Link forms to send to patients when they book. |
| **Booking Site Visibility** | Choose which appointment types appear on your Patient Booking Site. |

For setup instructions, see the [Calendar Guide - How to set up the provider calendar](https://help.elationemr.com/s/article/calendar-and-booking-settings) article.

## Recurring Appointments

The Recurring Appointments feature lets you schedule a series of ongoing patient visits in a few steps, ideal for patients who need regular care.

| | |
| --- | --- |
| **Feature** | **Description** |
| **Flexible Intervals** | Schedule weekly or monthly recurring appointments. |
| **Up to 52 Recurrences** | Create a series up to 18 months in advance. |
| **Conflict Detection** | Review scheduling conflict alerts when creating a series of recurring appointments. |
| **Individual Editing** | Edit or delete individual appointments without affecting the entire series of recurring appointments. |

ℹ️ **NOTE** Patients cannot book recurring appointments through the Booking Site. Only staff can create recurring appointments.

For detailed instructions, see the [Calendar Guide - Scheduling recurring patient appointments](https://help.elationemr.com/s/article/recurring-patient-appointments) article.

## Quick Reschedule

Quick Reschedule lets you instantly move an appointment to a new time slot based on provider availability.

| | |
| --- | --- |
| **Feature** | **Description** |
| **Suggested Times** | Displays the next six available slots based on location, duration, and availability. |
| **One-Click Rescheduling** | Select a new time and save without leaving your workflow. |
| **Single Appointments Only** | Works on individual appointments, not a series of recurring appointments as a whole. |

ℹ️   **EXCEPTIONS** The appointment must have a **Location** assigned to use Quick Reschedule.

For instructions, see the [Calendar Guide - Using the Calendar for appointments & events](https://help.elationemr.com/s/article/how-to-use-elation-calendar#quick-reschedule) article.

## Calendar Blocks and Non-Blocking Events

Elation offers two types of events to help manage your schedule:

| | | | |
| --- | --- | --- | --- |
| **Event Type** | **Blocks Calendar?** | **Blocks Booking Site?** | **Use Case** |
| **Calendar Block** | Yes | Yes | Lunch breaks, meetings, time off |
| **Non-Blocking Calendar Event** | No | No | Scheduling preferences, internal notes |

Calendar Blocks prevent appointments from being scheduled during that time, both in the EHR and on the Booking Site. Non-Blocking Calendar Events (also called non-blocking placeholders) display preferences on the calendar without restricting scheduling.

For detailed instructions, see the [Calendar Guide - Using the Calendar for appointments & events](https://help.elationemr.com/s/article/how-to-use-elation-calendar#blocks-vs-nonblocking) article.

## Automated Appointment Reminders

Automated Appointment Reminders help reduce no-shows by notifying patients about their upcoming appointments.

| | |
| --- | --- |
| **Feature** | **Description** |
| **Up to 3 Reminders** | Send multiple reminders before each appointment. |
| **Multi-Channel Delivery** | Send via text, email, or phone call based on patient preferences. |
| **Patient Confirmation** | Patients can confirm or cancel directly from the reminder. |
| **Virtual Visit Instructions** | Include video visit details for virtual/telehealth appointments. |

For setup instructions, see the [Calendar Guide - Using automated appointment reminders](https://help.elationemr.com/s/article/appointment-reminders) article.

# Feature Comparison

| | | | |
| --- | --- | --- | --- |
| **Feature** | **Staff Can Use** | **Patients Can Use** | **Requires Setup** |
| Calendar | Yes | No | Appointment Types, Display Settings |
| Patient Booking Site | Yes | Yes | Provider Availability, Booking Site Settings |
| Recurring Appointments | Yes | No | Provider Availability (recommended) |
| Quick Reschedule | Yes | No | Location assigned to appointment |
| Calendar Blocks | Yes | No | None |
| Non-Blocking Events | Yes | No | None |
| Appointment Reminders | Automatic | Receives | Reminder Settings |

# Getting Started

To set up scheduling for your practice, follow these steps:

| | |
| --- | --- |
| 1 | **Configure Practice Locations** - Add your practice locations and assign time zones. See the [Practice Locations Guide](https://help.elationemr.com/s/article/adding-a-second-practice-location) article. |
| 2 | **Set Up Appointment Types** - Create the appointment types your practice offers. See the [Calendar Guide - How to set up the provider calendar](https://help.elationemr.com/s/article/calendar-and-booking-settings) article. |
| 3 | **Configure Provider Availability** - Define when each provider is available for appointments. See the [Calendar & Booking Site Guide - Enhanced Provider availability](https://help.elationemr.com/s/article/Calendar-Booking-Site-Guide-Enhanced-Provider-availability-by-Practice-Location-Appointment-Type) article. |
| 4 | **Enable the Patient Booking Site** (optional) - Allow patients to self-schedule appointments online. See the [Patient Booking Site Guide](https://help.elationemr.com/s/article/Patient-Booking-Site) article. |
| 5 | **Set Up Appointment Reminders** - Configure automated reminders to reduce no-shows. See the [Automated Appointment Reminders Guide](https://help.elationemr.com/s/article/appointment-reminders) article. |

# Frequently Asked Questions (FAQ)

#### Can patients book recurring appointments online?

No, patients cannot book recurring appointments through the Booking Site. Only staff can create a series of recurring appointment in Elation.

#### Can I double-book appointments?

Yes, staff can book multiple appointments in the same time slot when needed. However, the Booking Site does not allow patients to double-book the same time slot.

#### How do Calendar Blocks differ from Non-Blocking Events?

Calendar Blocks remove time from availability on both the calendar and the Booking Site. Non-Blocking Calendar Events display scheduling preferences without blocking availability—patients can still book during those times via the Booking Site if provider availability allows. [Click here for more information about these two features](https://help.elationemr.com/s/article/how-to-use-elation-calendar#calendar_block_vs_placeholder).

#### Can I use the Calendar without the Patient Booking Site?

Yes, you can use the Elation Calendar without enabling the Patient Booking Site. The Calendar functions independently for internal scheduling.

#### How far in advance can I schedule recurring appointments?

The latest possible end date for a recurring appointment series is **18 months** from the date it is created, or a maximum of **52 recurrences**.

#### Do appointment reminders work for all appointments?

Yes, appointment reminders are sent for all scheduled appointments, whether booked through the Booking Site or manually by staff.

# Related Articles

- [Calendar Guide - Using the Calendar for appointments & events](https://help.elationemr.com/s/article/how-to-use-elation-calendar)
- [Calendar Guide - How to set up the provider calendar](https://help.elationemr.com/s/article/calendar-and-booking-settings)
- [Calendar Guide - Scheduling recurring patient appointments](https://help.elationemr.com/s/article/recurring-patient-appointments)
- [Patient Booking Site Guide](https://help.elationemr.com/s/article/Patient-Booking-Site)
- [Calendar & Booking Site Guide - Enhanced Provider availability by Practice Location & Appointment Type](https://help.elationemr.com/s/article/Calendar-Booking-Site-Guide-Enhanced-Provider-availability-by-Practice-Location-Appointment-Type)
- [Calendar Guide - Using automated appointment reminders](https://help.elationemr.com/s/article/appointment-reminders)
- [Practice Locations Guide - Listing your service locations](https://help.elationemr.com/s/article/adding-a-second-practice-location)
- [Calendar Guide - Setting practice location for appointment reminders](https://help.elationemr.com/s/article/using-multi-location-scheduling)