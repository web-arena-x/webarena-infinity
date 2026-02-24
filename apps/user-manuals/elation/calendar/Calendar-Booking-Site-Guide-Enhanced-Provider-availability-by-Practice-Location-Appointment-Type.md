# Calendar & Booking Site Guide - Specifying Provider availability by Practice Location & Appointment Type

Source: https://help.elationhealth.com/s/article/Calendar-Booking-Site-Guide-Enhanced-Provider-availability-by-Practice-Location-Appointment-Type

---

# Contents

- [Overview](#overview)
 - [What is Provider Availability?](#what-is-provider-availability)
 - [Why is Provider Availability important?](#why-is-provider-availability-important)
 - [How Availability, Events, and Booking work together](#how-availability-events-and-booking-work-together)
 - [What actually blocks the Booking Site?](#what-actually-blocks-the-booking-site)
 - [Current Limitations of Enhanced Availability](#current-limitations-of-enhanced-availability)
- [Workflow Instructions](#workflow-instructions)
 - [Configuring availability preferences for a Provider](#configuring-availability-preferences-for-a-provider)
    - [Verifying each Practice Location has the correct time zone](#verify_time_zone)
    - [Configuring availability for a Practice Location](#configure_availability_by_location)
    - [Removing availability for an entire Practice Location](#remove_entire_location)
    - [Removing availability within a Practice Location](#remove_availability_within_location)
 - [Viewing a Provider's availability on the EHR Calendar](#viewing-a-providers-availability-on-the-ehr-calendar)
    - [Adding appointments to the calendar when availability is configured](#adding_appointments)
 - [Displaying a Provider's availability on the Booking Site](#displaying-a-providers-availability-on-the-booking-site)
    - [Viewing a Provider’s availability on the Patient Booking Site as a patient](#view_availability_as_patient)
 - [Configuring Rotating or Irregular Schedules](#configuring-rotating-or-irregular-schedules)
 - [Storing & utilizing a patient's time zone preferences](#storing--utilizing-a-patients-time-zone-preferences)
- [Frequently Asked Questions (FAQ)](#frequently-asked-questions-faq)

ℹ️ **NOTE** This article only describes the ability to set Provider scheduling availability by Practice Location and Appointment Type on the Elation Calendar and Patient Booking Site. Please reference the [Calendar Guide - How to set up the provider calendar](calendar-and-booking-settings.md) and [Patient Booking Site Guide](Patient-Booking-Site.md) for more information about other Calendar and Booking Site related features.

# Overview

## What is Provider Availability?

The Provider availability and scheduling features allow Practices to:

- Define the availability of each Provider Level User for any Practice Location and Appointment Type within the EHR. (This is sometimes called setting availability templates, schedule templates, or office hours by location.) This availability will be visible on both the Practice Home calendar and the Booking Site calendar for each Provider Level User.
- Specify overlapping availability for different Practice Locations and Appointment Types.
- Assign a specific time zone to each Practice Location to ensure accurate configuration and patient communication regarding appointments.

## Why is Provider Availability important?

The Provider availability and scheduling features:

- Provide scheduling control and accuracy because:
 - Staff can now visually discern on the Calendar both the availability of each Provider and the specific appointment types they are available for.
 - Patients using the Booking Site can only select appointments based on the Provider's chosen Practice Locations and Appointment Types.
- Help practices with multiple Practice Locations segment their patients according to each Provider's availability
- Ensure that practices operating across different time zones:
 - Provide clear time zone details to patients on the booking site.
 - Accurately send appointment details to patients in their respective time zones.

## How Availability, Events, and Booking Work together

Provider availability, calendar events, and the Booking Site all use the same scheduling feature. Understanding how these elements interact helps you configure your calendar accurately.

### **Key scheduling elements**

- **Provider Availability (by location and appointment type):** Weekly recurring time rules that define when a provider can see patients at each Practice Location for specific appointment types. Also referred to as availability templates, schedule templates, or office hours by location.
- **Appointments:** Booked patient visits that occupy calendar time and block additional bookings in that slot.
- **Calendar Events:** Events on the calendar that occupy time slots. By default, calendar events block patient self-scheduling via the Booking Site. However, staff and providers can still manually book appointments over these times if needed. These include:

 - Events you create directly in Elation (such as lunch blocks, meetings, or personal time)
 - Events synced from Google Calendar
- **Non-Blocking Placeholders:** Internal preference cues that do not block booking. Patients can still book appointments during these times via the Booking Site if the provider's main availability allows it. Non-Blocking Placeholders are internal-only and will not appear on your Booking Site.

### **Booking Site and Quick Reschedule evaluation order**

When patients view the Booking Site or staff use Quick Reschedule, the system checks availability in this order:

1. Is the provider's availability configured for this location and appointment type?
2. Is the time slot already occupied by an appointment or a calendar event (including synced Google Calendar events)?
3. Does the appointment type meet the minimum notice requirement?

## What actually blocks the Booking Site?

Use this quick reference to understand which calendar elements prevent patients from booking appointments online.

| Calendar Element | Blocks Patient Self-Booking? | Can Staff/Providers Still Book Manually? | Notes |
| --- | --- | --- | --- |
| Appointments | Yes | Yes | Booked slots are unavailable. |
| Calendar Events (including synced Google Calendar events) | Yes | Yes | Events block patient self-booking by default, but staff can manually book over them if needed. |
| Non-Blocking Placeholders | No | Yes | Internal-only; patients can still book during these times via the Booking Site. |

ℹ️ **NOTE** Non-Blocking Placeholders are meant only as internal preference cues for staff. They do not appear on your Booking Site and do not prevent patients from booking.

## Current limitations of Enhanced Availability

Keep these limitations in mind when configuring provider schedules:

- **Weekly patterns only:** Availability is configured as weekly recurring patterns. You cannot set availability for a single specific date (e.g., "this one Wednesday only") without making manual adjustments.
- **No automatic rotating schedules:** There is no native "every other week" rule. Rotating or irregular schedules must be modeled using weekly patterns plus manual overrides.
- **Manual updates for varying hours:** Providers who want varying monthly hours on the Booking Site must manually adjust their availability as their schedule changes.

# Workflow Instructions

## Configuring availability preferences for a Provider

ℹ️ **NOTE** The ability to adjust Provider availability preferences can be limited to [Admin Level Users](https://help.elationemr.com/s/article/administrative-privileges) if the Admin Only toggle located in the top right corner of the Calendar & Booking settings page is toggled on (green).

### Verifying each Practice Location has the correct time zone

To ensure the Booking Site displays the correct time zone for each Practice Location, make sure the time zone for each Practice Location is accurate when setting availability.

If you attempt to add availability for a Practice Location that does not have a time zone set, you will see the following Location needs a time zone alert. You must click Update location time zone and set a time zone before you can add availability to the location.

### Configuring availability for a Practice Location

To define the availability for a specific Practice Location for Provider Level User:

| | |
| --- | --- |
| 1 | Go to Settings → Calendar & Booking and then click into the Availability section. |
| 2 | Find the Provider whose availability settings you want to update and click on the arrow to expand their availability preferences. |
| 3 | Existing Booking Site users will see the Provider's pre-existing availability preferences linked to the primary Practice Location for the practice. By default, all **Appointment Types** will be associated with the pre-existing specified time frames.    - To edit their availability for the primary Practice Location, jump to step 5 below. |
| 4 | To define availability for a new Practice Location for that Provider, click + Add Location.   💡 **USER TIP** [Click here for more information on how to add additional practice locations to your practice settings](adding-a-second-practice-location.md#AddLocation). |
| 5 | To edit the availability for any Practice Location, click Edit Availability. |
| 5a | Select the Start Time and End Time for any day of the week as needed. The selected time will correspond to the time zone configured for that Practice Location. If you need to update the time zone for that Practice Location, click the Update button next to the time zone displayed for that Practice Location. 💡 **USER TIP** If the chosen time frame overlaps with the availability of another Practice Location, you will notice an alert icon next to the time frame indicating this overlap. Place your mouse cursor over the alert icon to see which Practice Location it overlaps with. ℹ️ **NOTE** If a time frame does not have both a Start Time and End Time, Elation will not allow you to save the time frame. |
| 5b | By default, all Appointment Types will be associated with that day of the week. To change the Appointment Types available, click on the Appointment Types dropdown and then unselect the Appointment Types that you want to remove for that timeframe. The selected Appointment Types will appear on the main Settings page, as space allows. Click Show all… if you want to see the expanded list of the selected Appointment Types. |
| 5c | To delete an availability time frame, click the trash can icon. To add a new availability time frame for that day of the week, click the + icon. |
| 6 | Once you are done defining the availability for that Practice Location, click Save Availability to save your changes.    - To discard your changes, click Cancel. - To remove all of the availability for that Practice Location, click Remove Availability. |
| 7 | **Repeat for other locations** - To define availability for the same Provider for another Practice Location, repeat steps 4 through 7. |
| 8 | **Repeat for other providers** - To define availability for another Provider in your practice, repeat steps 2 through 7. |

### Removing availability for an entire Practice Location

To completely remove a location and all of its availability for a Provider Level User:

| | |
| --- | --- |
| 1 | Go to Settings → Calendar & Booking and then click into the Availability section. |
| 2 | Find the Provider whose availability settings you want to update and click on the arrow to expand their availability preferences. |
| 3 | Click Edit Availability for the Practice Location you want to remove. |
| 4 | Click Remove Availability. |

ℹ️ **CAUTION** Take caution when removing availability because it cannot be restored.

### Removing availability within a Practice Location

To completely remove availability for a specific day of the week or a specific Appointment Type for a Provider Level User:

| | |
| --- | --- |
| 1 | Go to Settings → Calendar & Booking and then click into the Availability section. |
| 2 | Find the Provider whose availability settings you want to update and click on the arrow to expand their availability preferences. |
| 3 | Click Edit Availability for the Practice Location you want to edit. |
| 4 | To delete an availability time frame, click the trash can icon. |
| 5 | To remove an Appointment Type from a time frame, click on the Appointment Types dropdown and unselect the Appointment Types that you want to remove for that timeframe. |
| 6 | Once you are done editing the availability for the Practice Location, click Save Availability to save your changes. |

ℹ️ **CAUTION** Take caution when removing availability because it cannot be restored.

## Viewing a Provider's availability on the EHR Calendar

A Provider Level User's availability is marked using gray vertical bars in their EHR Calendar. Place your cursor over an availability bar to see the availability details. Each availability bar indicates when the provider is available, which location they are working at, and which Appointment Type(s) you can book. If there is overlapping availability then you will see multiple appointment bars in parallel.

In periods when the Provider is unavailable, the Calendar will display diagonal stripes. Your office can still schedule appointments during these time frames if necessary.

### Adding appointments to the calendar when availability is configured

To schedule appointments on the calendar for a Practice Location where the Provider is available:

| | |
| --- | --- |
| 1 | Click on the gray vertical bar for the corresponding Practice Location at the time the appointment starts. |
| 2 | The Location field will automatically populate the Practice Location you clicked on. |
| 3 | Fill in the remaining appointment details and then click Create Appointment. |

💡 **USER TIP** You can click in the white space of the Calendar to schedule appointments. However, this will set the Location field to "No location specified" by default. You can schedule appointments during any unavailable timeframes by clicking a time in the timeframe or click + Appointment.

## Displaying a Provider's availability on the Booking Site

ℹ️ **NOTE** Two steps are required for a provider to appear on the Booking Site:

1. The appointment type must be marked as available on the Booking Site using the Show this appointment type on the booking site checkbox.
2. The provider must be listed under Providers in that appointment type's Booking Site section.

Setting availability alone is not enough. If either step is missing, patients will not see that provider for that appointment type on the Booking Site.

To ensure that the available appointments are displayed correctly on the [Patient Booking Site](Patient-Booking-Site.md):

| | |
| --- | --- |
| 1 | Go to the Appointment Type Settings. |
| 2 | Click Edit for the Appointment Type you want to make available on your Booking Site. |
| 3 | Check off the Show this appointment type on the booking site box. |
| 4 | Select the name of any Provider you want visible for that Appointment Type under Providers. |

To share a direct URL for each Appointment Type with patients:

| | |
| --- | --- |
| 1 | Go to the Appointment Type Settings. |
| 2 | Go to the summary box of the Appointment Type you want to share. |
| 3 | Look for the **Direct URL** under the Booking Site section and click Copy. |
| 4 | Share the **Direct URL** with the patient using any method of your choice (e.g. link it to your business website). |

### Viewing a Provider's availability on the Patient Booking Site as a patient

The [Patient Booking Site](Patient-Booking-Site.md) will only display the Provider availability configured in the Calendar & Booking settings. When patients first navigate to your practice booking site, they will see a list of all available Practice Locations. Patients can narrow down the availability displayed by selecting a Practice Location, and/or filtering by Provider, Appointment Type, or Time zone.

**Default Booking Site display:**

**Booking Site display after a Practice Location is selected:**

- If the patient selects a Practice Location, the page will display available providers and appointments for that Practice Location and the appointment times will display in the Practice Location's default time zone unless the patient changes the time zone selection at the top of the Booking Site.

## Configuring rotating or irregular schedules

If a provider works a rotating schedule (e.g., Mondays & Wednesdays one week, Tuesdays  & Thursdays the next), you can still manage their availability using weekly patterns and manual overrides.

**Supported behavior:**

- Availability is configured as weekly recurring patterns by location and appointment type.
- You can define multiple availability blocks per day and remove availability for specific days or locations.
- There is no native "every other week" rule. Rotating schedules must be modeled using recurring weekly patterns plus manual overrides.

### **Example Scenario**

Provider works Mondays and Wednesdays one week and Tuesdays and Thursdays the next:

| | |
| --- | --- |
| 1 | Set a pattern that covers all potential work days. For example, set availability for Mondays through Thursdays, 9:00 AM-5:00 PM. |
| 2 | **For weeks when the provider does not work on certain days,** add a calendar event on those specific days to prevent patient self-booking. |
| 3 | **For one-off days when the provider is working outside their usual pattern,** remove any calendar events that would prevent booking. |

💡 **USER TIP** For complex patterns over a limited window (e.g., 2-3 months), set a baseline weekly template and then use one-off overrides on specific days as needed.

## Storing & utilizing a patient's time zone preferences

To ensure that appointment confirmation and reminder notifications display the appointment date and time according to the patient's preference, save each patient's preferred time zone in their [Patient Demographics](https://help.elationemr.com/s/article/Patient-Demographics-Guide). The Time zone field is in the **Contact Information** section of Patient Demographics.

Any patient communications sent by the EHR will follow these time zone rules:

1. If a patient’s preferred time zone is saved for the patient then appointment confirmation and appointment reminder notifications will use the preferred time zone.
2. If a patient's preferred time zone is not saved, but their Patient Demographics include a valid zip code, appointment confirmation and reminder notifications will calculate the appropriate time zone based on the patient's zip code and use it for sending notifications.
3. For practices with a single Practice Location:
   1. If a patient's preferred time zone is not saved AND the patient does not have a valid zip code in the Patient demographics, then appointment confirmation and appointment reminder notifications will use the time zone of your practice’s primary Practice Location.
4. For practice’s with multiple Practice Locations:
   1. If a patient's preferred time zone is not saved AND the patient does not have a valid zip code in the Patient demographics, then the appointment confirmation and reminder notifications will be based on the time zone associated with the Practice Location of the appointment.
      - If the Practice Location of the appointment does not have a defined time zone, then we will use the time zone of your practice’s primary Practice Location.
      - Go to your Practice Location Settings to define a time zone for each Practice Location. Contact Elation Support if you need to update the time zone of your practice’s primary Practice Location.
   2. If a patient's preferred time zone is not saved AND the patient does not have a valid zip code in the Patient demographics, AND the Practice Location for the appointment does not have a time zone set, then appointment confirmation and appointment reminder notifications will use the time zone of your practice’s primary Practice Location.

# Frequently Asked Questions (FAQ)

#### Why are changes to availability not saving?

If a time frame does not have both a Start Time and End Time, Elation will not allow you to save that time frame. Add both a Start Time and End Time to save availability preferences.

#### I work in multiple time zones. How should I indicate my Practice Hours on my Booking Site?

Currently, you are unable to designate a time zone for your Booking Site Practice Hours. We recommend leaving the Practice Hours blank if you have Practice Locations in different time zones.

#### Can I specify which locations appear on the booking site?

Currently all locations configured on the Practice Locations Settings page will appear on the Booking Site.

#### I sometimes see patients virtually or I run a fully virtual practice, how should I set up my availability?

To set your practice up to use the Booking Site for virtual appointments, we recommend taking the following two actions:

| | |
| --- | --- |
| 1 | Adjust the Practice Location of any provider offering virtual appointments to match the provider's time zone. 💡 **USER TIP** If the Practice Location offers both in-person and virtual appointments, set up two versions of the Practice Location - one for each. |
| 2 | Save each patient's preferred time zone in their Patient Demographics. |

This ensures that Providers see their calendar in the Provider's own time zone and patients receive communications in the patient's preferred time zone.

#### Can I enter availability that changes week to week?

Yes, but not with an automatic "every other week" rule. You can configure a recurring weekly template and then adjust specific dates on the calendar.

For a detailed example, see the [Configuring Rotating or Irregular Schedules](#configuring-rotating-or-irregular-schedules) section above.

#### If I am also using Elation's Workspaces feature, what Time Zone will the Availability on my Calendar display in?

If you are using Elation's [Workspaces](https://help.elationemr.com/s/article/workspaces-guide) feature, the Availability will display based off of the Time Zone your Workspace is configured for.

## **Related Articles**

- [Calendar Guide- How to set up the provider calendar](calendar-and-booking-settings.md)
- [Patient Booking Site Guide](Patient-Booking-Site.md)
- [Practice Locations Guide- Listing your service locations](adding-a-second-practice-location.md)