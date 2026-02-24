# User Accounts Guide- Viewing activity logs for users in your practice

Source: https://help.elationhealth.com/s/article/User-Accounts-Guide-Viewing-activity-logs-for-users-in-your-practice

---

## **Contents**

- [What is the User Activity Log?](#description)
- [What are the benefits of using the User Activity Log?](#value)
- [Using the User Activity Log](#using_activity_log)
 - [Accessing the User Activity Log](#accessing_activity_log)
 - [Viewing data in the User Activity Log](#viewing_activity_log_data)
- [Frequently Asked Questions (FAQ)](#faq)

## **What is the User Activity Log?**

The User Activity Log allows [Admin Level Users](https://help.elationemr.com/s/article/administrative-privileges) to see and monitor actions performed by all users in the EHR from January 1, 2023 to present. Non-Admin Level Users will be able to see and monitor their own activity. The activity in the User Activity Log includes, but is not limited to:

- Accessing, deleting or merging patient charts
- Creating certain content in the patient’s demographics including:
 - Address
 - Phone
 - Email
 - Contact preference
 - Insurance (including deleting)
- Creating certain content in the Clinical Profile including:
 - Patient’s profile picture
 - Patient allergies
 - Patient drug intolerances
 - Problems
 - Medical History
 - Family history
 - Patient’s provider list
 - Immunization history
- Creating, deleting or printing visit notes (including vitals and certain bullets)
- Creating and updating bills (including CPT Codes and Diagnosis Codes)
- Creating, signing and deleting orders
- Deleting discontinued medications
- Deleting medication history reports
- Approving and denying prescription refill requests
- Creating and deleting letters
- Creating, signing, acknowledging, and deleting Office Message threads
- Creating and deleting non-visit notes
- Reassigning and deleting reports
- Creating and deleting appointments

## **What are the benefits of using the User Activity Log?**

The User Activity Log provides a convenient way to review activity performed by various users within the EHR. Through the use of powerful filters, you can quickly review all actions performed for a given patient and/or by a specific user. This new functionality will simplify and expedite the process of understanding when actions were performed and by whom and allow you to access the relevant patient chart to take next steps if needed. You will also be able to undo certain actions such as deleting certain records or merging charts.

Use cases for the User Activity Log include:

- *Which chart did I update?*
 - In the busyness of a typical day, sometimes someone in the practice makes a change to a chart only to forget which chart they modified. This can make it difficult to continue making necessary changes, or to revert changes that have been made by mistake. With the User Activity Log, you can easily see all the charts recently viewed.
- *Who has viewed or taken action on a particular chart?*
 - Sometimes certain charts are sensitive and your practice may want to ensure only authorized practice users are accessing the chart. With the User Activity Log, you can search for a specific patient and view all the users who have viewed or taken action on that patient's chart.
- *What actions has this user performed?*
 - In some scenarios, a practice may have concerns that a particular user might be attempting to view or do more than they should. With the User Activity Log, you can search for a particular practice user and review all the actions performed by that user across charts to ensure it is aligned with what they are authorized to do.

## **Using the User Activity Log**

### **Accessing the User Activity Log**

To access the User Activity Log, go to “Reports” -> “User Activity Log”.
![]()

### **Viewing data in the User Activity Log**

By default, we will list user activity from January 1, 2023 to present. The activity log will list up to 20 activities per page. Use the page navigation buttons to move between different pages of the activity log.

- [Admin Level Users](https://help.elationemr.com/s/article/administrative-privileges) can see and monitor actions performed by all users in the Practice.
- Non-Admin Level Users can only see and monitor their own activity.

You can use the following filters to narrow down the activity log data. Click the “Search” button after applying filters to see the results that match your filter(s).
![]()

| |
| --- |
| **User Activity Log Filters** |
| **Filter** | **Use Case** |
| User | Select the User in your practice you wish to monitor.   - This filter will not be available for non-Admin Level Users. Non-Admin Level Users can only see their own activity. - You can only filter for one user at a time. - You will not be able to filter for disabled users but you will be able to see their activity listed in the User Activity Log. To filter for the activity of a disabled user, you must temporarily enable their account, view their activity log and then disable their account again.   - **User Tip**: To prevent a disabled user from accessing their account while it is temporarily enabled for this purpose, you can adjust their email. (Ex. If their email is [john.smith@email.com](mailto:john.smith@email.com) you can update it to [john.smith+disabled@email.com](mailto:john.smith+disabled@email.com). |
| Patient | Enter the **Patient ID** into this filter if you want to look at the activity log for a specific patient.   - You can only filter for one patient at a time.   To locate a patient’s **Patient ID**:   1. Open the patient’s chart 2. Click on the patient’s name to open their Demographics 3. Click the “Copy” button next to **Elation Patient ID** at the top of their demographics. |
| Record Type | Select the type of record you wish to look at.   - You can select multiple records at a time.      - For example, select "Visit Note" if you want to see all activity related to visit notes. |
| Action | Select the type of action you wish to look at.   - You can select multiple actions at a time. - For example, select "Delete" if you want to look at all delete activity. |
| Start Date | Select the date you wish to start filtering the activity by. The date cannot be before January 1, 2023. |
| End Date | Select the date you wish to stop filtering the activity by. |

The activity log will list the following details:

| |
| --- |
| **User Activity Log Data Columns** |
| **Column** | **Description** |
| Date | Lists the Date and Time of the activity in your practice’s timezone. |
| User | Lists the full name of the User that performed the activity.   - You will also see activity for disabled users. However, you will not be able to filter for disabled users unless you temporarily activate their account.   - **User Tip**: To prevent a disabled user from accessing their account while it is temporarily enabled for this purpose, you can adjust their email. (Ex. If their email is [john.smith@email.com](mailto:john.smith@email.com) you can update it to [john.smith+disabled@email.com](mailto:john.smith+disabled@email.com). - If your practice uses any API integrations with Elation, you will see ‘API User’ listed for activity performed via the integration. |
| Patient | Lists the full name of the Patient tied to the activity.   - You can click on the patient’s name to open their chart if needed.   - You will not be able to click on the patient’s name to open their chart if their chart was deleted or merged away. You must first restore or unmerge the chart first to access the chart again. |
| Patient DOB | Lists the date of birth of the Patient   - Useful when multiple patients have the same exact name. |
| Action | Lists the action performed on the Patient. Note: The 'Update' action may be recorded if a user accesses a record but does not modify it. This can occur because a draft of the record is automatically saved when it is accessed, even if no changes are made. |
| Record Type | Lists the type of record the action was performed on. |
| Record ID | Lists the Record ID of the record in Elation’s database.   - This is often used by Elation’s Support Team for troubleshooting. |
| Restore (only available for certain Record Types) | Allows you to click a “Restore” button to restore certain deleted records. Restored records can be accessed immediately.   - After a record is restored, the “Restore” button will be replaced with the designation ‘Restored’ for reference.   The following records can be restored from the User Activity Log:   - Patient Charts   - Both restoring deleted charts and unmerging merged charts - Visit Notes - Non-visit Notes - Reports - Medications (including discontinued medications) - Medication History Download Reports |

## **Frequently Asked Questions (FAQ)**

#### **How is the User Activity Log different from the Audit Log?**

The activity data in the [Audit Log](https://help.elationemr.com/s/article/Patient-Chart-Guide-Audit-Logs) is specific to each patient’s chart whereas the User Activity Log lists activity within all patient charts (unless you choose to filter the data by a specific Patient ID). You will not be able to undo any actions within the Audit Log but you can undo certain actions, such as deleting certain records or merging charts, within the User Activity Log.

#### **How often does the User Activity Log update with new (recent) data?**

Recent actions may take up to 30 minutes to appear.

#### **When will I be able to see activity prior to January 1, 2023?**

The User Activity Log will only list actions performed on or after January 1, 2023. If you need information about actions performed prior to this date, please click the “I need help” -> “Contact Elation Support” button at the top of your Elation account and the Elation Support Team will be able to assist you with this request.

#### **Is there a way to download a report of the data in the User Activity Log?**

A download option is currently unavailable at this time but it is something under consideration for future development. If you need help obtaining a download of activity, please click the “I need help” -> “Contact Elation Support” button at the top of your Elation account and the Elation Support Team will be able to assist you with this request.

#### **Is there a way to download a report of the data in the User Activity Log? Why does a record show the action of 'Update' if I viewed it but did not make changes to it?**

When performing certain actions, such as viewing a medical order, a draft of the content being viewed will be saved, regardless of whether a change was made. As a result of this draft being saved, the record is considered to be modified and will thus be categorized as an 'Update' action.

## **Related Articles**

- [User Accounts Guide- Administrative privileges](https://help.elationemr.com/s/article/administrative-privileges)
- [Patient Chart Guide- Audit Logs](https://help.elationemr.com/s/article/Patient-Chart-Guide-Audit-Logs)
- [User Accounts Guide- Managing Elation accounts for providers and staff](https://help.elationemr.com/s/article/managing-user-accounts)