# Calendar Guide - How to set up the provider calendar

Source: https://help.elationhealth.com/s/article/calendar-and-booking-settings

---

📖 **RECOMMENDED READING**

This article provides a quick guide on how providers can set up their calendar to manage patient appointments in their Elation EHR. If you plan to use the Booking Site feature with Elation, we recommend reading the [Patient Booking Site Guide](Patient-Booking-Site.md) first.

# **Contents**

- [Overview](#overview)
 - [Understanding scheduling privileges for Providers and Staff](#Scheduling_Privileges)
    - [Calendar ownership and default views](#ownership_and_defaults)
    - [Telehealth visit privileges](#telehealth)
 - [Premium EHR considerations](#premium_EHR)
    - [How chart access controls affect appointment access](#Chart_Access)
    - [Workspaces and scheduling visibility](#Workspaces_Scheduling)
- [Workflow Instructions](#workflow-instructions)
 - [Accessing the Calendar Settings](#CalendarSettings)
 - [Managing Appointment Types](#Appointment_Types)
    - [Creating a new appointment type](#AddingAppointmentTypes)
    - [Editing an existing appointment type](#EditAppointmentType)
    - [Removing an existing appointment type](#RemoveAppointmentType)
    - [Sorting appointment types](#SortAppointmentType)
 - [Managing the Calendar View](#Calendar_View)
 - [Managing Exam Rooms](#Exam_Rooms)
    - [Creating a new exam room](#CreateRoom)
    - [Editing an existing exam room](#EditRoom)
    - [Removing an existing exam room](#RemoveRoom)
 - [Automated Appointment Reminders](#Appointment_Reminders)
- [Frequently Asked Questions (FAQ)](#FAQ)

# **Overview**

## **Understanding Scheduling Privileges for Providers and Staff**

Before setting up your calendar, it's helpful to understand how scheduling-related privileges differ between Provider Level Users and Staff Level Users.

### **Calendar ownership and default views**

- Only Provider Level Users have their own Calendar in Elation.
- If you are a Provider Level User, the Calendar will always default to showing your own Calendar.
- If you are a Staff Level User in a multi-provider practice, the Calendar will default to showing the Calendar for the provider you set as your **Default physician** under **Settings** >> **User Settings**. If you have not set a Default physician, the Calendar will default to the first provider alphabetically by first name.
- If the practice has only one Provider Level User, the Calendar will always default to showing that provider's Calendar for all users.
- If your practice uses Workspaces, you may not see certain provider calendars depending on your Workspace configuration. See the [Workspaces and scheduling visibility](#Workspaces_Scheduling) section below for details.

### **Telehealth visit privileges**

- Regular Providers, Non-Prescribing Providers, and Limited Use Providers can activate and use the telehealth [Zoom](https://help.elationemr.com/s/article/Elation-Telehealth-powered-by-Zoom) feature.
- On Call Providers cannot activate the telehealth [Zoom](https://help.elationemr.com/s/article/Elation-Telehealth-powered-by-Zoom) feature themselves, but they can start virtual visits from a Regular or Non-Prescribing Provider's calendar.
- Staff Level Users can start virtual visits from a Regular or Non-Prescribing Provider's calendar but cannot activate the telehealth feature independently.

## **Premium EHR considerations**

[Premium EHR Users](https://help.elationemr.com/s/article/Premium-EHR-Features-Guide) should review the sections below for more details about our specific features interact with appointments and their Calendars.

### **How chart access controls affect appointment access**

Your practice may use chart access controls that affect what users can do when viewing appointments.

- **Viewing appointments vs. opening charts:** Staff members can view appointment times and details on the Calendar. However, if chart access restrictions are in place (such as VIP Charts or Patient Cohorts), they may not be able to open certain patient charts even if they can see the scheduled appointment. If your practice uses Workspaces, users may also be unable to see certain provider calendars. See the [Workspaces and scheduling visibility](#Workspaces_Scheduling) section below for more information.
- **VIP Charts:** When a chart is marked as VIP, only the Provider assigned in practice can access it without restriction. Other users may see a warning or be blocked entirely, even if you can see their appointment on the Calendar.
- **Patient Cohorts:** Patient Cohorts allow practices to automatically restrict chart access based on patient criteria. If a patient is assigned to a cohort and you are not a member of that cohort, you may be unable to open the patient's chart even if you can see their appointment on the Calendar.
- **Block All Chart Access:** Admin Level Users can revoke a user's access to all patient charts. Users without chart access will see an "Unauthorized access" page when attempting to open any patient chart, but they will still be able to see the appointment on the Calendar.

For more information, see the [User Accounts Guide- Chart access permission control options](/s/article/chart-access-permission-control-options) article.

### **Workspaces and scheduling visibility**

If your practice uses the Workspaces feature, scheduling visibility may vary based on your Workspace configuration.

###

#### **People List and Calendar visibility**

- The **People List** resource in Workspaces controls which Provider Level Users appear for selection when viewing Provider Calendars and scheduling appointments.
- By default, all Provider Level Users appear in the Calendar and appointments unless a specific User Group is selected in the People List settings.
- Providers will always have access to their own Calendars, regardless of Workspace settings.

###

#### **Time zone display**

- If you are using Workspaces, the availability displayed on your Calendar will reflect the time zone configured for your Workspace.

###

#### **Switching between Workspaces to see related Calendars**

- If you belong to multiple Workspaces, you can switch between them to see the related Calendars by clicking the Workspace dropdown next to your email in the blue navigation bar at the top of Elation.
- Admin Level Users can use the **Return to practice view** option to see all resources within the EHR regardless of Workspace membership.

Non-Admin User View

Admin User View

For more details, see the [Workspaces Introduction](/s/article/workspaces-introduction) article.

# **Workflow Instructions**

## **Accessing the Calendar Settings**

The Elation Calendar settings is in **Settings** >> **Calendar & Booking**. The main calendar related sections here are **Appointments**, **Calendar view**, **Reminders**, and **Rooms**.

## **Managing Appointment Types**

Appointment types are the different appointment options you can utilize in the Elation Calendar. By default, Elation will load the following Appointment Types to new Elation accounts to start you off:

- Follow-Up
- Office Visit
- Physical Exam
- Walk-in
- New Patient
- Procedure

### **Creating a new appointment type**

| | |
| --- | --- |
| **1** | Navigate to **Settings**. |
| **2** | Click **Calendar and Booking** in the Settings options. |
| **3** | Click **Add Appointment Type**. |
| **4** | Fill out all of the sections as described in the images below. |
| **5** | Click **Save**. |
| **6** | Reload your Practice Home to allow your updates to display. |

**💡** **USER TIPS**

- Learn more about the [auto-created visit note feature here](visit-note-automation.md).
- You can add multiple visit note templates to a single appointment type. This means that, for telehealth visits, you only need to have one "Telehealth" visit note template that can be layered on top of any other visit note template relevant to the appointment type (e.g. Annual Wellness for Women).

### **Editing an existing appointment type**

| | |
| --- | --- |
| **1** | Click **Edit** on the appointment type that you wish to edit. |
| **2** | Enter the changes to the appointment type. |
| **3** | Click **Save**. |
| **4** | Reload your Practice Home to allow your updates to display. |

### **Removing an existing appointment type**

| | |
| --- | --- |
| **1** | Click **Delete** on the appointment type you wish to remove. |
| **2** | Reload your Practice Home to allow your updates to display. |

**💡** **USER TIP**

If there are any past or currently scheduled appointments that are assigned the type that you remove, those appointments will continue to keep that appointment type. Removing an appointment type means that you will no longer be able to create new appointments with that type.

### **Sorting appointment types**

Click and drag the handle ![]() on the left hand side of the appointment type to re-order it. The order of your appointment types in Settings will be reflected in the **Appointment type** drop-down menu in the **Create an Event** window in the Elation calendar.

## **Managing the Calendar View**

To edit the way your calendar displays information, go to the **Calendar view** tab under the **Calendar & Booking** settings page.

- **Appointment Time Block Intervals:** Set the duration of the appointment time block intervals in the Calendar for everyone in your practice. For example, if you set the block interval at 15 minutes, the scheduler will display times throughout the day in 15-minute increments.
- **Hide the durations under the patients name on appointments and on events:** If you wish to hide durations that show up on appointment and events, move the toggle to appear green.
- **Show Canceled Appointments:** If you wish to see canceled appointments in the calendar, move the toggle to appear green.

**💡** **USER TIPS**

- If there is only one provider in the practice, the Calendar will always default to showing that provider's Calendar.
- If you are provider viewing the Calendar in a multi-provider practice, the Calendar will always default to showing your Calendar.
- If you are a staff viewing the Calendar in a multi-provider practice, the Calendar will default to showing the Calendar for the provider you set as your **Default physician** under **Settings** -> **User Settings**.

## **Managing Exam Rooms**

To add, edit, and delete exam room names that you can use from the Elation Calendar, go to the **Rooms** section in the **Calendar & Booking** settings page. You will be able to select from your list of exam rooms after you select one of the "In Room" options for the appointment's status.

### **Creating a new exam room**

| | |
| --- | --- |
| **1** | Click **+ Add room**. |
| **2** | Fill out the room name. |
| **3** | Click **Save**. |

###

### **Editing an existing exam room**

| | |
| --- | --- |
| **1** | Click **Edit** on the room that you wish to edit. |
| **2** | Change the room name. |
| **3** | Click **Save**. |

###

### **Removing an existing exam room**

Click **Delete** on the room that you wish to remove.

## **Using automated Appointment Reminders**

Your practice can choose to send up to 3 appointment reminders to patients ahead of a scheduled patient visit. Elation's automated appointment reminders help ensure that your patients have the information they need to attend their visit and will decrease the number of no shows on your schedule.

Our system uses the following logic to determine which notification to send:

1. Preferred contact method. If not, then:
2. SMS Text to the mobile phone number. If not, then:
3. Email notification to the email address. If not, then:
4. Phone call to a home or main phone number.

ℹ️ **NOTE**

Appointment reminder notifications cannot be sent to work, night, fax or other phone numbers.

To turn on appointment reminders, go to the **Reminders** tab and follow the instructions in the [Automated Appointment Reminders](appointment-reminders.md) article.

# **Frequently Asked Questions**

#### **Can I add additional time block intervals to the settings?**

The time block intervals options cannot be adjusted at this time. Elation will notify you if this changes in the future.

#### **Can I add additional colors for appointment types?**

The appointment type color options cannot be adjusted at this time. Elation will notify you if this changes in the future.

**Next Step**

Review the [Elation Integrated Video feature](Elation-Telehealth-powered-by-Zoom.md) to see if you want to utilize it for your patients.

# **Related Articles**

- [How to use Elation Calendar](how-to-use-elation-calendar.md)
- [Patient Booking Site Guide](Patient-Booking-Site.md)
- [Automated Appointment Reminders](appointment-reminders.md)
- [Introduction to Google Calendar Sync](introduction-to-google-calendar-sync.md)
- [Elation Integrated Video- Connecting with patients using video](Elation-Telehealth-powered-by-Zoom.md)
- [User Accounts Guide- Chart access permission control options (Premium)](/s/article/chart-access-permission-control-options)
- [Workspaces Introduction (Premium)](/s/article/workspaces-introduction)