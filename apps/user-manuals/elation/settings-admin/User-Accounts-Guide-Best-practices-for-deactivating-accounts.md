# User Accounts Guide - Best practices for disabling accounts

Source: https://help.elationhealth.com/s/article/User-Accounts-Guide-Best-practices-for-deactivating-accounts

---

# **Contents**

- [Overview](#overview)
 - [What happens when an Elation user account is disabled?](#description)
 - [Why is this guide important?](#value)
- [Workflow Instructions](#workflow-instructions)
 - [Notifying Elation](#notifying-elation)
 - [Action items for Provider/Physician Accounts](#provider-accounts)
 - [Action items for Staff Accounts](#staff-accounts)
 - [How to disable an Elation Account](#how-to-disable)

**💡** **Closing Your Practice or Transitioning EHRs?** If you are closing your entire practice or transitioning to a different EHR system, see our [Offboarding & Data Export Checklist](https://help.elationemr.com/s/article/Offboarding-Data-Export-Checklist) for a comprehensive guide to exporting patient data and notifying patients.

# **Overview**

## **What happens when an Elation user account is disabled?**

When an Elation user account is disabled, the user will no longer have access to the account and its data. This guide walks practices through recommended action items that should be taken before provider/physician or staff level users leave your practice and before their Elation account is disabled.

## **Why is this guide important?**

Following these best practices ensures a smooth transition when team members leave your practice. This will ensure:

- No action items are misfiled or overlooked
- Patients are properly reassigned and notified
- Pending prescriptions and messages are handled appropriately
- Administrative reports are preserved before account deactivation

# **Workflow Instructions**

## **Notifying Elation**

Before disabling any Provider Level User, reach out to our Support Team via the **I need help** button or [fill out this form](https://app.elationemr.com/support/) to let us know that these changes will occur. Include the following information:

- Which provider level user is leaving your practice
- The date that this provider level user will no longer need their account active
- Is a new provider/physician taking their place?
 - If so, how many hours will the new provider work per week and will they need an account with prescribing privileges?
 - New provider/physician's start date

With notification of this change and the information above provided, our teams can ensure that your Elation information, like billing, is properly updated.

## **Action items for Provider/Physician Accounts**

The following changes will occur immediately once provider/physician level accounts are disabled:

- The provider will not be able to log in to Elation
- Your practice will no longer be able to view their schedule on the calendar
- The provider's Practice Home queue will be hidden
 - Any office messages that are left in their queue will need to be acknowledged by another provider/physician in the practice
 - Any other open items in their queue will need to be signed or completed by another provider/physician in the practice
- Patients who are assigned to the disabled provider/physician will need to be re-assigned to another provider/physician in the practice
- The provider/physician will be removed from all administrative reports

ℹ️ **NOTE** Please read through each section below to make sure the proper actions are taken to ensure a smooth transition.

### **Practice Home Queues**

Please have the departing provider address and/or complete all items in their [Practice Home Queues](the-requiring-actions-queue-follow-up-on-action-items.md) (e.g., Reports, Rx Request, Office Messages, etc.) before they leave your practice. If there are any open items remaining after their departure, make sure another provider in the practice addresses the open items before disabling the departing provider/physician's account.

### **Lab/Imaging/Hospital Reports**

Please notify the different facilities from which you receive electronic results and let them know of the provider's departure from your practice. Specifically, we recommend sharing the provider's last day and asking them to forward any of the reports they ordered to a different provider at your practice (provide the new provider's NPI number) after that date if possible.

If the facilities are unable to forward the electronic results to a different provider at your practice, the results will not automatically arrive in Elation. Your practice will need to retrieve these reports directly from the facilities via their own websites or have the reports sent to your practice via fax or paper mail.

### **Refill Requests**

Please reach out to our Support team through [this form](https://app.elationemr.com/support/), or through the **I need help** → **Contact Elation Support** option within Elation, to notify us of the date to turn off the Refill Request feature for the provider who is leaving.

After this date, pharmacies will see that the provider's electronic prescribing functionalities are disabled and will send refill requests to your office via fax instead. The new attending provider at the practice should respond to these faxed refill requests via Elation by sending a prescription electronically back to the pharmacy so that the next time the same patient needs a refill, the refill request will come directly to the new attending provider through an electronic request in Elation.

### **Post-dated Office Messages**

If the departing provider ever sent [post-dated messages](post-date-a-message-to-yourself-or-a-colleague.md) to themselves or other members of the practice, those messages will be automatically signed off and stored in the patient's chart once the leaving provider's account is disabled.

If needed, our Technical Team can generate a report of these messages and share them with you so that the remaining staff and provider(s) can follow up on them. Please reach out to our Support team through [this form](https://app.elationemr.com/support/) with the following information:

- Name of the provider leaving
- Date range of the post-dated messages (you can also say "Any message after a specific date")

### **Patient Passport Messages**

Before disabling the departing provider's account, we recommend you pull a [Patient List Report](find-patients-with-elations-patient-list.md) of all the patients assigned to the leaving provider using the **Reports** → **Patient List** report tool and reassign those patients to a different provider at the practice. If there are many patients, our Technical Team can assist with reassigning multiple patients at once.

This way, after the departing provider's account is disabled, all new patient Passport messages will be routed to the new provider instead of the departing provider.

### **Appointments with the departing Provider**

Any appointments scheduled on the departing provider's calendar for any date after they have left will need to be manually transferred to a different provider's calendar because the departing provider's calendar will be hidden from the practice once their account is disabled.

You can move appointments by editing each appointment and changing the provider it is assigned to, as shown in the image below.

You can also download an appointment report by selecting **Reports** → **Appointment Report** from the top blue bar of your account to find and reference appointments scheduled with the departing provider in the future.

**💡** **USER TIP**

- If you need to view an appointment report that is longer than 2 weeks, please manually type in the "From:" and "To:" dates and click the **Download List of Appointments as CSV** button to download the report and view in a spreadsheet software on your computer.
- If you need to view an appointment report that is longer than 6 months, you will need to break up the time frame into multiple reports, download the reports to your computer as a CSV file and then combine the data in a spreadsheet software application. For example, if you would like to see all appointments from 2020, you will need to run 3 reports; each with the following time frames:
 - 01/01/2020 to 05/31/2020
 - 06/01/2020 to 10/31/2020
 - 11/01/2020 to 12/31/2020

### **Access Controls for EPCS**

If the departing provider is an [Access Control Manager](how-to-set-up-epcs-access-controls.md) for EPCS set up and configuration, please ensure there is another Access Control Manager at your practice before the provider leaves. Reference the [EPCS Access Controls Guide](how-to-set-up-epcs-access-controls.md) to update access control settings if needed.

### **Administrative Reports**

If you need to retain a copy of any administrative reports for the departing provider, you must download the reports prior to disabling the departing provider's account. Please reference the following articles for each administrative report you might need:

- [Patient List Report Guide](find-patients-with-elations-patient-list.md)
- [Billing Report Guide](https://help.elationhealth.com/s/article/billing-report)
- [Appointment Report Guide](Calendar-Guide-Searching-for-appointments-with-the-Appointments.md)

### **Recommended: Notify Patients Using Bulk Letters**

When a provider is leaving your practice, follow these steps to notify affected patients via a Bulk Letter:

| | |
| --- | --- |
| **1** | **Run a Patient List** - Go to **Reports** → **Patient List** and filter by the departing provider to identify their patient panel. |
| **2** | **Send a Bulk Letter** - Select all patients from the list and click **Send Bulk Letter** to notify them about: - The provider's departure date - Who will be taking over their care - How to request copies of their medical records if needed |
| **3** | **Reassign patients** - Update patient assignments to ensure Passport messages route to the correct provider going forward. |

See the [Bulk Letter Guide](introduction-to-bulk-letters.md) for detailed instructions on creating and sending bulk letters.

ℹ️ **NOTE** After a departing provider's account is disabled, if a patient sends the departing provider a message from an existing Patient Letter, those messages will not appear in the newly assigned provider's inbox. We recommend that the "Everyone" Practice Home queue is checked periodically to check for these kinds of Passport messages.

## **Action items for Staff Accounts**

While it is not necessary to alert our Teams when staff level accounts are disabled, we still recommend the following workflows occur before disabling a staff level account.

### **Practice Home Queues**

Please have the departing staff address all items in their [Practice Home Queues](the-requiring-actions-queue-follow-up-on-action-items.md) (e.g., Office Messages, Patient Letters, etc.) before they leave your practice. If there are any open items remaining after their departure, make sure another member in the practice addresses the open items before disabling the departing staff's account.

### **Post-dated Office Messages**

If the departing staff ever sent [post-dated messages](post-date-a-message-to-yourself-or-a-colleague.md) to themselves or other members of the practice, those messages will be automatically signed off and stored in the patient's chart once the departing staff's account is disabled.

If needed, our Technical Team can generate a report of these messages and share them with you so that the remaining staff and provider(s) can follow up on them. Please reach out to our Support team through [this form](https://app.elationemr.com/support/) with the following information:

- Name of the staff leaving
- Date range of the post-dated messages (you can also say "Any message after a specific date")

### **Access Controls for EPCS**

If the departing staff is an [Access Control Manager](how-to-set-up-epcs-access-controls.md) for EPCS set up and configuration, please ensure there is another Access Control Manager at your practice before the staff leaves. Reference the [EPCS Access Controls Guide](how-to-set-up-epcs-access-controls.md) to update access control settings if needed.

## **How to disable an Elation Account**

ℹ️ **NOTE** To disable Elation accounts, you must have administrator (Admin) level privileges. If you do not see **Manage Accounts** in your Settings page, then you are not an Admin. To become an Admin, you must ask an existing Admin level user in your practice (most likely a primary provider level account holder) to grant you privileges via the **Manage Accounts** settings page.

Once you have addressed the action items listed above, you are ready to disable the departing user's Elation account. To deactivate or disable a provider or staff level Elation account within your practice, Admin Users in your practice can follow these steps:

| | |
| --- | --- |
| **1** | Select your email address from the blue bar at the top right of your Elation page and select **Settings** from the drop down. |
| **2** | Scroll to the bottom and click into the **Manage Accounts** settings section under **Admin Users Only**. |
| **3** | Select the down arrow to the left of **Active Users** to expand the list of active Provider or Staff users at your practice. |
| **4** | Click the **Disable** button next to the name of the user that you want to disable. |
| **5** | Read through the confirmation prompt and then click **Disable Account** to disable the user's account. |

**Related Articles**

- [User Accounts Guide - Onboarding & Data Export Checklist](https://help.elationemr.com/s/article/Offboarding-Data-Export-Checklist)
- [User Accounts Guide- Managing Elation accounts for providers and staff](managing-user-accounts.md)
- [Practice Home Guide- Checking for requiring action items](check-for-your-offices-daily-to-do-list.md)
- [Post Date a Message Guide- Reminders & Task Follow Up](post-date-a-message-to-yourself-or-a-colleague.md)
- [Patient List Report Guide- Searching your patient panel](find-patients-with-elations-patient-list.md)
- [Billing Guide- Billing Report](/s/article/billing-report)
- [Calendar Guide- Searching for appointments using the Appointment Report](Calendar-Guide-Searching-for-appointments-with-the-Appointments.md)
- [Bulk Letter Guide- Mass communication with Patients](introduction-to-bulk-letters.md)
- [Elation Patient Passport Guide](elation-patient-passport-an-introduction.md)
- [EPCS Access Controls Guide](how-to-set-up-epcs-access-controls.md)