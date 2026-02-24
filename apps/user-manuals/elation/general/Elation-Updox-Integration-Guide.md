# Elation-Updox Integration Guide- Using Updox alongside Elation to manage documents and patient engagement

Source: https://help.elationhealth.com/s/article/Elation-Updox-Integration-Guide

---

## **Contents**

- [What is Updox?](#updox)
- [What is the Elation-Updox Integration?](#updox_integration)
- [How do I get started?](#getting_started)
- [What information is synchronized between Elation and Updox?](#synced_info)
 - [Provider Information](#provider_info)
 - [Practice Locations](#practice_locations)
 - [Patient Charts](#patient_charts)
    - [Creating Charts](#creating_charts)
    - [Merging Charts](#merging_charts)
    - [Deleting Charts](#deleting_charts)
 - [Patient Demographics](#deleting_charts)
 - [Documents (Reports)](#documents)
 - [Appointments](#appointments)
- [Sending documents from Updox to Elation](#send_documents_to_Elation)
- [Managing appointments](#managing_appointments)
- [Managing contacts](#managing_contacts)
- [Getting Support](#support)
- [Frequently Asked Questions (FAQ)](#FAQ)




## **What is Updox?**

[Updox](https://www.updox.com/)© is a communications platform that centralizes communications for EHRs and patients through a single system. Updox’s features and functionalities include:

- Electronic fax
- Internal messenger
- Telehealth video chat
- Secure Text/SMS
- Patient mass communication
- Automated appointment reminders




## **What is the Elation-Updox Integration?**

With the Elation-Updox integration, you can:

- send all documents and communication records from Updox to Elation to keep a single source of truth for all patient data
- utilize the appointments and demographics data in Elation to power Updox’s appointment reminders
- utilize the demographics data in Elation to power Updox’s patient communication features




## **How do I get started?**

To request an Updox account and/or begin the integration process between Elation and Updox, [click here to fill out a form](https://info.updox.com/elation-updox-integration) which notifies the Updox Sales Team of your interest. Updox will assign an Onboarding Success Manager to your account to assist you with setting up your Updox account and turning on the Elation-Updox Integration.



## **What information is synchronized between Elation and Updox?**

| Data | Sync Direction |
| --- | --- |
| Provider Information | Elation → Updox |
| Practice Locations | Elation → Updox |
| Patient Charts | Elation → Updox |
| Demographics | Elation → Updox |
| Appointments\*    \*Only the 'Scheduled', 'Confirmed' and 'Canceled' **Appointment Status** will sync from Updox to Elation. | Elation → Updox |
| Documents (Reports) | Updox → Elation |





## **Provider Information**

The synchronization of Provider Level User accounts is unidirectional from Elation to Updox. When a Provider Level Account is activated in Elation, that Provider’s name will automatically be pushed to Updox within a few minutes.



## **Practice Locations**

The synchronization of Practice Location information is unidirectional from Elation to Updox. Additions to your Practice Locations list and edits to Practice Location information must be made in Elation and then the information will automatically be pushed to Updox within a few minutes upon save. The following table shows a mapping of the Patient Demographics fields that are sent from Elation to Updox and their matching field names. Fields that are not listed are not sent from Elation to Updox.

| Elation Field Name | Updox Field Name |
| --- | --- |
| Name | Name |
| Address | Address 1 |
| Suite | Address 2 |
| City | City |
| State | State/Province |
| Zip | Postal Code |
| Phone | Appointment Phone |
| Fax | Fax Phone |





## **Patient Charts**

### **Creating Charts**

The synchronization of patient charts is unidirectional from Elation to Updox. This means patient charts can only be created in Elation. Afterwards, only patients with the 'Active' [Patient Status](Patient-Status.md) will appear in the Address Book in Updox. Chart additions and updates will take only a few minutes to sync to Updox upon save.


### **Merging Charts**

Each chart can only have a one to one connection between Elation and Updox and this connection is established upon chart creation. If you happen to see a duplicate chart for the same patient in Elation, please make sure you find the chart that is connected between the two systems and keep the connected chart when performing a merge.

- For example, patient John Smith has two charts in Elation but one Patient record in your Updox Address Book. The best way to find out which of the two charts in Elation is connected to the Patient record in Updox is by updating one of the connected demographics fields in Elation for each chart with something unique to see which version is sent to the Patient record in Updox. (For example, update the Ste or apt # field in Elation to 5th floor for one chart and 6th floor for the other chart and see what floor appears in Updox. Afterwards revert the Ste or apt # field back to the original information). The Elation chart that has the data you see in Updox must be the chart that you keep in Elation when performing a chart merge.


Here are the proper merge steps for Elation charts:

1. Open the duplicate chart that is not connected to the integration
2. Click on the patient's name to open their Demographics
3. Click on the "Merge Chart" button
4. Find & select the chart you want to keep (the one that is connected to the integration)
5. Click "Merge Chart"
6. Confirm you understand the transfer of data and then click "Yes, merge charts"

### **Deleting Charts**

Deleting a chart in Elation will not delete the Patient record in Updox; it will only mark the patient as inactive. Please take caution when deleting charts in Elation while using the Updox integration as charts have a one to one connection via the integration. If the patient is still active in your practice, the deleted chart must be restored in order for the patient's information to sync properly across the two systems. Contact Elation using the "I need help" button if you need to restore a deleted chart in Elation.




## **Patient Demographics**

The synchronization of Patient Demographics is unidirectional from Elation to Updox. All edits must be made in Elation and the information will automatically be pushed to Updox within a few minutes upon save. The following table shows a mapping of the Patient Demographics fields that are sent from Elation to Updox and their matching field names. Fields that are not listed are not sent from Elation to Updox.

| Elation Field Name | Updox Field Name |
| --- | --- |
| Legal First Name | First Name |
| Legal Last Name | Last Name |
| Middle Name | Middle Name |
| Date of birth | Date of Birth |
| Sex at birth | Sex |
| Home Phone | Home Phone |
| Mobile Phone | Cell Phone |
| Email | Email |
| Address | Address 1 |
| Ste or apt # | Address 2 |
| City | City |
| State | State |
| Zip | Zip |
| Elation Patient ID | EHR Patient ID |
| Preferred Language | Patient Communication Language\*    \*Only 'English' and 'Spanish' will be synchronized as these are the only two languages Updox supports. |
| Patient Status = Active | **Active** checkbox is checked |
| Patient Status = Prospect | *Not synchronized* |
| Patient Status = Inactive | **Active** checkbox is NOT checked |
| Patient Status = Deceased | **Active** checkbox is NOT checked |





## **Documents (Reports)**

The synchronization of documents is unidirectional from Updox to Elation and will appear in Elation as Reports in the patient’s chart. The Reports will appear in Elation within a few minutes upon send.

The following table lists the Reports fields that are pushed from Updox to Elation and show how the Updox fields map to the Elation fields. Fields that are not listed are not sent Updox to Elation:

| Updox Field Name | Elation Field Name |
| --- | --- |
| Document Name | Report Title |
| Document Type | Report Category |
| Provider | Assigned Provider |
| Date of item | Document Date |
| Date & Time Sent from Updox | File Received Date & Time |
| Notes\* | For customers with the metadata setting turned on, Notes will appear in the metadata page at the end of the Report |

**Important Note**: The Document Types options you see in Updox use the [Report Categories](report-types.md) you choose to use in Elation. Once a day, each morning, Updox will sync the most up to date list of Report Categories as it is configured in your Elation account. If you edited your Report Categories today, you will not see the changes until tomorrow.






## **Appointments**

The synchronization of appointments is unidirectional from Elation to Updox. Practices must create and update appointments in Elation for the appointment to push to the corresponding Provider calendar in Updox. Appointment additions and edits will take only a few minutes to sync to Updox upon save.

The following table lists the Appointment fields that are pushed from Elation to Updox and show how the Elation fields map to the Updox fields. Fields that are not listed are not sent from Elation to Updox:

| Elation Field Name | Updox Field Name |
| --- | --- |
| Patient Name | Patient Chart # |
| Date | Appointment Date |
| Start Time | Appointment Time |
| Duration | Appointment Duration |
| Appointment Type | Appointment Type |
| In Person/Virtual | 'In Person' or 'Virtual' designation next to the Appointment Type |
| Provider | Calendar Name |
| Status | Status\*    \*Only the 'Scheduled', 'Confirmed' and 'Canceled' **Appointment Status** will sync from Updox to Elation. |
| Location | Location |





## **Sending documents from Updox to Elation**

1. Select the pages you want to send from you Updox Inbox by checking off the box under each page
2. Click the “Send… selected page” button in the sidebar
3. Search for and select the name of the patient the documents belong to
4. Check off the “Send to EHR” box & click “OK”
5. Fill out the following fields:
   1. Document Name
   2. Document Type
   3. Provider
   4. Date of item
      - If you leave this field blank, Updox will default the date of the item to ‘today’s’ date
      - The time of the Report will always appear as 12am in Elation
   5. Notes
      - Notes entered will only appear in the metadata page that is included at the end of each document that is sent to Elation as long as you have this Setting turned on in Updox.
        - If you wish to turn off the metadata page in Updox, go to Menu -> Admin -> Practice Settings -> and check off the **Do not add last page of metadata on PDFs or imported documents** box.
6. Click “Send”
7. The report will be sent to Elation within a few minutes. The report will appear in the Requiring Actions section of the patient’s chart. If you are already in the chart you may need to refresh the chart to see the report.




## **Managing appointments**

Updox allows you to customize appointment reminder text and preferences based on Provider Calendars, Practice Locations and Appointment Types. If you use Updox for advanced appointment reminders, the appointment data shared by Elation will power the appointment reminder configurations in Updox.

- **Important Note**: Turn off your Elation appointment reminders if you are using Updox’s appointment reminders and vice versa. If appointment reminders are on in both systems then patients will receive both sets of appointment reminders.


When patients confirm and cancel their appointment in either system, Elation or Updox, that updated appointment status will appear in both Elation and Updox.

- **Important Notes**:
 - Only the Scheduled, Confirmed and Canceled statuses sync between Elation and Updox
 - If you need to see canceled appointments in the calendar, make sure that Setting is turned on in both systems:
    - In Elation go to “Settings” -> “Calendar & Booking” -> “Calendar view” and toggle the **Show canceled appointments in the calendar** setting to green.
    - In Updox, check off the **Show Cancelled** box at the top of the Calendar

- The Activity Log under each appointment in Elation will display an appointment that was canceled by Updox as Canceled.



## **Managing contacts**

Contacts in Elation are defined as providers that can be used for Letters or Referrals. Contacts can be self-created or can be pulled in from the main Elation Directory. The synchronization of contacts is unidirectional from Elation to Updox and happens once every evening.

The following table lists the Contacts fields that are pushed from Elation to Updox and show how the Elation fields map to the Updox fields. Fields that are not listed are not sent from Elation to Updox:

| **Elation Field Name** | Updox Field Name |
| --- | --- |
| Type | Category |
| First Name | First Name |
| Middle Name | Middle Name |
| Last Name | Last Name |
| Address - Street | Address 1 |
| Address - City | Address 2 |
| Address - State | State |
| Address - Zip | Zip |
| Phone | Work Phone\*     \*If **Cell Phone**is not available then the **Phone** field in Elation will map to **Work Phone**in Updox instead. |
| Fax | Fax Number |
| Email | Email |
| Cell Phone | Cell Phone |




## **Getting Support**

#### **Updox**

If you need assistance with Updox or the Elation-Updox integration, contact Updox using one of the following methods:

- Go to <https://www.updox.com/support/>
- Email [support@updox.com](mailto:support@updox.com)

#### **Elation**

If you need assistance with Elation, contact Elation using one of the following methods:

- Click the “I need help” -> “I need help from Elation Team Member” button at the of your Elation account
- Fill out our [Support Contact Form](https://help.elationhealth.com/s/contactsupport)





## **Frequently Asked Questions (FAQ)**

#### **I added a new Report Category to Elation but I do not see it in Updox. Why is this happening and what should I do?**

The Document Types options you see in Updox use the [Report Categories](report-types.md) you choose to use in Elation. Updox will only sync this information once every morning. If you edited your Report Categories today, you will not see the changes until tomorrow.

In the meantime, you can select any Document Category that is visible in Updox, send the document over to Elation and then change the Report Category by clicking “Actions” -> “Edit Details”.

#### **I sent a document from Updox to Elation and the time on the report says 12am in Elation. Can I change this?**

It is not possible to change the time of the report at this time. All reports sent from Updox will be time stamped at 12am.


**I see an appointment on the calendar in Updox but I don't see that appointment in Elation. Why?** We recommend checking if the appointment is marked as Canceled in Updox. If it is, check your Elation Settings (under “Settings” -> “Calendar & Booking” -> “Calendar view”) to see if canceled appointments are visible in your Elation calendar. If it is not a canceled appointment, reach out to [Updox Support](#updox_support) for further assistance.

#### **There’s an extra page of details at the end of every Report sent from Updox. How do I turn this off?**

If you wish to turn off the metadata page that is sent from Updox, go to Updox -> Menu -> Admin -> Practice Settings -> and check off the **Do not add last page of metadata on PDFs or imported documents** box.


#### **If I add a new patient to my Updox Address Book, will that create a chart for them in Elation?**

Adding a new patient to the Updox Address Book will not create a chart for them in Elation. Patient Charts only synchronize from Elation to Updox.


*Copyright © Updox. All rights reserved.*



## **Additional Resources**

- [Elation + Updox Information Page](https://info.updox.com/elation-updox-integration)