# Calendar Guide - Scheduling recurring patient appointments

Source: https://help.elationhealth.com/s/article/recurring-patient-appointments

---

# **Contents**

- [Overview](#overview)
 - [What is the Recurring Appointments feature?](#description)
 - [Why should I use Recurring Appointments?](#benefits)
- [Setup](#setup)
 - [Pre-requisite Configurations](#configurations)
- [Workflow Instructions](#workflows)
 - [Creating a recurring appointment for a patient](#create)
 - [Editing a recurring appointment](#edit)
 - [Deleting a recurring appointment](#delete)
 - [Sending appointment reminders for recurring appointments](#reminders)
 - [Sending Patient Forms for recurring appointments](#forms)
- [Frequently Asked Questions (FAQ)](#FAQ)

# **Overview**

## **What is the Recurring Appointments feature?**

The Recurring Appointments feature lets you schedule a series of ongoing patient visits—such as for behavioral health, chronic care management, or multi-visit treatment plans—in just a few steps. Rather than creating each appointment manually, you can set up a repeating schedule using customizable weekly or monthly intervals and define when the series of appointments should end. A recurring icon will appear next to Recurring Appointments for easy identification.

## **Why should I use Recurring Appointments?**

If you need to schedule recurring appointments for certain patients, the Recurring Appointments feature minimizes manual data entry and streamlines the scheduling process, helping reduce errors, omissions, and missed appointment slots. It also eases the administrative burden on scheduling staff.

Common use cases include:

- Scheduling biweekly injections for chronic care management.
- Setting up recurring lab draws.
- Reserving a consistent weekly appointment slot for patients receiving ongoing therapy.

# **Setup**

The Recurring Appointments feature is available for all users.

## **Pre-requisite Configurations**

To ensure the Recurring Appointments feature works smoothly, ensure [Provider Availability](https://help.elationemr.com/s/article/Calendar-Booking-Site-Guide-Enhanced-Provider-availability-by-Practice-Location-Appointment-Type) is set up for providers to ensure conflicts are taken into account.

# **Workflow Instructions**

## **Creating a recurring appointment for a patient**

| | |
| --- | --- |
| **1** | Create a new appointment using one of the following methods from the Calendar:   1. Click **+ Appointment**. 2. Click on an appointment slot. |
| **2** | Enter appointment details such as **Patient name**, **Appointment type**, **Start time**, and **Duration**. ℹ️  **CAUTION** Information added to the **Patient Payment** and **Billing Note** fields will only apply to the first appointment. |
| **3** | Verify the **Provider** and **Location** information is accurate. |
| **4** | Choose recurrence by clicking **Recurrence** -> **Custom…**.   1. Specify the repeat interval by entering a number and selecting **week** or **month**.    1. If **week** is selected, pick the day(s) of the week you want the appointment to repeat on.    2. If **month** is selected, choose when you want the appointment to repeat each month. The available options are based on the date and day of the week of the first appointment. 2. Select the end condition    1. Select **On** if you want the series to end by a specific date and then enter the Date.    2. Select **After** if you want the series to end after a certain number of recurrences and then enter the number of recurrences. 3. Click **Save**.   ℹ️   **SCHEDULING LIMITS** - **Maximum scheduling horizon**: The latest possible end date for a recurring appointment series is **18 months** from the date it is created. - **Maximum appointments per series**: Each recurring series can include up to **52 recurrences**. |
| **5** | Review scheduling conflicts.   - If any conflicting appointments are detected while creating a recurring appointment, the conflicting dates will be listed at the top of the create appointment dialog. You can find each overlapping appointment in the patient appointment search after the series is created and then solve each conflict separately.   ℹ️  **NOTE** If the **Appointment Type**, **Start Time**, or **Duration** falls outside the provider's availability, a note will appear at the bottom of the appointment details to indicate the conflict, just like it does with regular appointments. |
| **6** | Click **Create Appointment** to save all appointments to the Calendar. |

## **Editing a recurring appointment**

| | |
| --- | --- |
| **1** | Click into the white space of the recurring appointment to show the appointment popover. |
| **2** | Click **Edit**. |
| **3** | Edit the appointment details as needed.   1. Edits to the following fields will only apply to the specific appointment that is being edited, even if you choose to apply the edits to following appointments:    - **Appointment Status**    - **Patient Payment**    - **Billing Note** |
| **4** | Click **Save**.   1. If you did not edit the recurrence information and the appointment is not the last appointment in the series, choose whether you want the changes to apply to **This appointment** or **This and following appointments**.    1. When you apply changes to **This and following appointments** in a recurring series:       - The changes you make will be applied to the appointment you're currently editing and every appointment after it in that series. All previous appointments in the series will remain unchanged.       - The original series is essentially "split" into two separate series. The appointments from the date you made the change forward become their own distinct series. If you edit an appointment *before* the date you made the change, it will **not** affect the new series. 2. If you’ve edited the recurrence information then the changes will automatically be applied to this and following appointments. |
| **5** | Click **Save** to save your changes. |

**💡**  **USER TIP**

Before editing a recurring appointment, you should always click on the appointment to open the pop-up. This will show you when the series ends, so you know exactly how many appointments you're editing.

## **Deleting a recurring appointment**

| | |
| --- | --- |
| **1** | Click into the white space of the recurring appointment to show the appointment popover. |
| **2** | Click **Delete**. |
| **3** | If the appointment is not the last appointment in the series, choose whether you want the changes to apply to **This event** or **This and following events**. |
| **4** | Click **Delete** to delete the associated appointment(s). |

## **Sending appointment reminders for recurring appointments**

Appointment reminders will be sent for each appointment in the series, following the cadence specified in your Settings.

## **Sending Patient Forms for recurring appointments**

Patient Forms will be sent based on your existing Settings.

- If forms are set to send a certain number of days before the appointment, they will be sent for each appointment in the series.
- If forms are set to send immediately upon booking, they will only be sent for the first appointment in the recurring series.

# **Frequently Asked Questions**

#### **Can patients book recurring appointments themselves?**

No, patients cannot book recurring appointments through the Booking Site.

#### **Can I book recurring appointments for multiple patients at once?**

You can only book recurring appointments for one patient at a time.

**How far in advance can I schedule recurring appointments?**

The latest possible end date for a recurring appointment series is **18 months** from the date it is created or a maximum of **52** **recurrences**.

#### **Can I change the “Repeats On” selection when editing a recurring appointment?**

Yes, the **Repeats On** selection can be changed once the recurring appointment series has been created.

#### **How are conflicting appointments handled when creating recurring appointments?**

If any conflicts are detected while creating a recurring appointment, the conflicting dates will be listed at the top of the create appointment dialog. These conflicts must be resolved separately. You can find each overlapping appointment in the patient appointment search after the series is created and then solve each conflict separately.

#### Can I use Quick Reschedule on a recurring appointment?

Quick Reschedule is designed for individual appointments. You can use it on any single appointment within a recurring series, but it only reschedules that specific appointment—not the entire series.

To use Quick Reschedule on an appointment in a recurring series:

| | |
| --- | --- |
| 1 | Click in the shaded area of the appointment to open the appointment popover. |
| 2 | Click **Show suggested times** next to **Quick Reschedule**. |
| 3 | Select a new time from the list of the next six available options, based on the appointment's **Location**, **Duration**, and the provider's **Availability**. |
| 4 | Click **Save new time**. |

ℹ️   **NOTE** The appointment must have a **Location** (Practice Location) assigned to use Quick Reschedule. Other appointments in the recurring series remain unchanged.

# **Related Articles**

- [Calendar Guide- Using the Calendar for appointments & events](https://help.elationemr.com/s/article/how-to-use-elation-calendar)