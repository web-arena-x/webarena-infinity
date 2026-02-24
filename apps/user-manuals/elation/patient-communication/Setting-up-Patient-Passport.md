# Elation Patient Passport Guide - Setting up Patient Passport

Source: https://help.elationhealth.com/s/article/Setting-up-Patient-Passport

---

# **Contents**

- [Setup](#setup)
- [Basic Configurations](#basic-configurations)
 - [Customizing default sharing preferences for your assigned patients](#customize_preferences_for_all)
 - [Specifying messaging preferences](#specify_message_preferences)
 - [Educating patients about Patient Passport](#educating_patients)
- [Advanced Configurations](#advanced-configurations)
 - [Customizing Clinical Profile default sharing settings for individual patients](#customize_preferences_for_individuals)
 - [Enabling notifications about unopened Patient Letters](#enable_notifications)
 - [Training staff - Best practice workflows](#best_practices)
 - [Setting up the Patient Booking Site](#Booking_Site)




# **Setup**

Prior to using Patient Passport, make sure the correct Settings and workflows are in place by following the setup instructions below.

# **Basic Configurations**

## **Customizing default sharing preferences for your assigned patients**

As a Provider Level User, you can control what Clinical Profile information is automatically shared with your patients through their Passport accounts. The following Clinical Profile information is **always** shared automatically with patients. This is known as the **Objective Data Only** category:

- **Allergies**
- **Drug Intolerances**
- **Medications**
- **Vaccines**

Other Clinical Profile data points that can be shared automatically are categorized into three additional levels. Use the table below to determine which level you want to set as your default and then review and adjust your preferences under **Settings** → **User Settings** → **Patient Sharing Defaults** → **Sections of the clinical profile to share through Passport**. These defaults apply to patients who have you listed as their Provider Assigned in Practice under their demographics.

ℹ️ **NOTE** Changes to your sharing defaults only apply to patients who register for Passport **after** the update. For patients already registered, adjust sharing settings individually in their chart under **Passport Sharing Options**.

| | | | | |
| --- | --- | --- | --- | --- |
| | **Objective Data Only** | **Objective Data & Problem List** | **Clinical Profile, excludes Confidential** | **Clinical Profile, Expanded Summary** |
| Satisfies MIPS requirements | **X** | ✅ | ✅ | ✅ |
| Allergies | ✅ | ✅ | ✅ | ✅ |
| Drug Intolerances | ✅ | ✅ | ✅ | ✅ |
| Medications | ✅ | ✅ | ✅ | ✅ |
| Vaccines | ✅ | ✅ | ✅ | ✅ |
| Problem List | **X** | ✅ | ✅ | ✅ |
| History | **X** | **X** | ✅ | ✅ |
| Legal Reports | **X** | **X** | ✅ | ✅ |
| Provider List | **X** | **X** | ✅ | ✅ |
| Confidential | **X** | **X** | **X** | **X** |
| Expanded Summary, Implantable Devices (CCDA) | **X** | **X** | **X** | ✅ |

## **Specifying messaging preferences**

By default, patients cannot initiate messages to you from their Passport account. To allow patients to send messages to your practice:

| | |
| --- | --- |
| **1** | Go to **Settings** → **Admin Users Only** → **Patient Passport Messages**. |
| **2** | Change the **Allow patients to send messages to the practice** toggle to Yes to enable patient-initiated messages. |

Afterwards, scroll down the page to review your routing preferences to ensure patients’ messages are routed to the correct person/team in your practice. Adjust as needed:

| | |
| --- | --- |
| **1** | Adjust routing preferences   - **For all providers at the same time** in the **Routing for All Providers** section by clicking **Update Routing for all Providers**. - **For individual providers** under the **Routing per Provider** section by clicking **Change Routing for …**. |
| **2** | Type the name of the recipient(s) or User Group(s) in the **Route To:** fields next to each Message Category.   1. To add a recipient, type the recipient’s name in the **Add provider, staff or group in practice…** field and then select a match from the search results. 2. To remove specific recipients, hover over their name and click **X**. 3. To remove all users click **Clear All**. |
| **3** | Click **Update Provider's Routes** to save your changes. |
| **4** | All newly received patient messages will follow the updated routing preferences. |

## **Educating patients about Patient Passport**

Educating patients (and/or their caretakers) on the benefits and usage of the Patient Passport can help boost adoption, especially as different use cases will require different ways of setting up their Passport account.

[Click here for a patient facing article about Passport setup and features](what-patient-passport-messaging-looks-like-to-a-patient.md). Feel free to include it in your communications with them.

# **Advanced Configurations**

## **Customizing Clinical Profile sharing settings for individual patients**

As needed, adjust what’s shared for each patient to override the default.

| | |
| --- | --- |
| **1** | In the patient’s chart, click the passport button (a globe) at the corner of the patient’s profile picture. |
| **2** | Go to the **Passport Sharing Options** section and choose the level of sharing you want. |
| **3** | Save your changes by clicking the appropriate button based on the patient’s account status:   1. If the patient hasn’t been invited yet or they haven’t registered yet, click **Send Invitation & Close**. This will also send the patient an invitation, even if they’ve already received one. 2. If the patient is a registered user, click **Save Settings Changes & Close**. |
| **4** | The changes will take effect the next time the patient signs in to their Passport account. |

## **Enabling notifications about unopened Patient Letters**

As a Provider Level User, you can specify a default notification preference for when patients don’t open/read the Patient Letters you send them. This includes [Patient Passport invitations of any kind](https://docs.google.com/document/d/1Nk38K6UkfP-cCdKrWoGvhRj6hWYk7Mhb4odGpP1ByqU/edit?tab=t.99ih9hgc9jlk#heading=h.9xw2jed7wz7f).

| | |
| --- | --- |
| **1** | Go to **Settings** → **User Settings** → **Patient Sharing Defaults** → **Notifications**. |
| **2** | Use the dropdown to choose how long to wait before receiving a notification. |

[Click here for more information about receiving notifications](Passport--Communicating-with-patients.md#reviewing-notifications-about-unread-messages).

## **Training staff - Best practice workflows**

To maximize Patient Passport adoption:

1. Train your staff on the common scenarios they may encounter when inviting patients to create a Passport account (see the table below to find the scenarios most relevant to your patient base). The correct invite process is different for each scenario, and following the right workflow will ensure a smoother experience for the patient.
   1. **Collecting a patient’s email address:**
      1. **Before you collect a patient's email address**, here are some important questions to ask. The table below shows why each question is significant in different scenarios.
         1. *Do you have a Patient Passport account with other practices, whether it be for yourself or someone else? If so, what is the email address associated with that account?*
         2. *Do you plan to use this email address for multiple Passport accounts? (E.g. for your child or someone else in your care).*
         3. *Does anyone else have access to this email address?*
   2. **Collecting a patient’s cell phone number:**
      1. For security purposes, an Invitation Code, sent in the form of an SMS Text message to the patient’s cell phone number on file, is used to verify that the Passport invitation is being sent to the correct person.
         1. If the patient does not have a cell phone:
            1. Temporarily store their landline phone number as their mobile number so that an invite can be sent to them.
            2. Send the Passport invite to the patient.
            3. Change the phone type back to the correct designation.
            4. Verbally give the patient their Invitation Code - [see instructions](Managing-Passport-invitations.md#looking-up-the-patients-passport-invitation-code).
2. Have staff [educate patients](#educating_patients) (and/or their caretakers) on the benefits of using Patient Passport.
3. Have the front office:
   - Collect & store an **email address** and **cell phone number** for each patient in their Patient Demographics for Patient Passport account invitation.
   - Invite all patients to Patient Passport.

| | | | |
| --- | --- | --- | --- |
| **Scenario**   *\*Regardless of who the Passport account belongs to and which provider the account is with.* | **Staff Actions** | **Patient Actions**   [Click here for a complete walkthrough on the various ways patients can register for a Passport account](what-patient-passport-messaging-looks-like-to-a-patient.md). | **Additional considerations** |
| The **patient’s** email address is not tied to any active Passport accounts yet. | 1. Collect the patient’s email address & cell phone and store it in their chart. 2. Follow the instructions for [inviting patients to Patient Passport for the first time](Managing-Passport-invitations.md#inviting-patients-one-by-one-to-patient-passport-for-the-first-time). | 1. The patient will provide their email address and cell phone number for you to save in their demographics. 2. Then they will register for their account by finding the invitation in their email, entering a unique **Invitation Code** texted to their cell phone, and creating a password. | If the email address that the patient wants to use is shared with other people, advise them to create  a new private email address first before inviting them to Passport to protect their Protected Health Information (PHI). |
| The **patient’s** email address is linked to another active Passport account and they wish to reuse it. | 1. Collect the patient’s email address **(must be the exact email address as their existing Passport account)** & cell phone and store it in their chart. 2. Follow the instructions for [inviting patients to link their Patient Passport accounts](Managing-Passport-invitations.md#inviting-patients-to-link-their-passport-accounts). | 1. The patient will provide their email address **(must be the exact email address as their existing Passport account)** and cell phone number for you to save in their demographics. 2. Then, they will link your practice's account to their existing one by finding the "claim chart" link in their email. They'll log in to their existing Passport account and follow the prompts to link both accounts together. | If a patient's email is already being used for a **family member's** **Passport** account and they **don't** want to link their personal Passport to that person's account, they have two options:   1. Update the email address in the family member’s Passport account to the family member’s own email address **OR** 2. Provide you with a different email address. |
| The **legal representative** is trying to register and their email address is **not** tied to any active Passport accounts. | 1. Collect the legal representative’s email address and cell phone and store it in the patient’s chart. 2. Follow the instructions for [inviting patients to Patient Passport for the first time](Managing-Passport-invitations.md#inviting-patients-one-by-one-to-patient-passport-for-the-first-time). | 1. The legal representative will provide their email address and cell phone number for you to save in the patient’s chart. 2. Then the legal representative will register for an account on the patient’s behalf by finding the invitation in their email, entering a unique **Invitation Code** texted to their cell phone and creating a password. | - If the legal representative is also a patient and wants their own Passport account, have the legal representative create their personal account first and then link the patient’s account to theirs.    - If the legal representative’s email address is shared with other people, advise them to use a private email address for their Passport account to protect their Protected Health Information (PHI). - If a legal representative is creating accounts for multiple patients, have the representative complete registration fully for one patient first before you send an invite for the next patient. - Multiple legal representatives can't access a single Passport account with different email addresses. |
| The **legal representative’s** email address is tied to another active Passport account. | 1. Collect the legal representative’s email address **(must be the exact email address as their existing Passport account)** & cell phone and store it in the patient’s chart. 2. Follow the instructions for [inviting patients to link their Patient Passport accounts](Managing-Passport-invitations.md#inviting-patients-to-link-their-passport-accounts). | 1. The legal representative will provide their email address **(must be the exact email address as their existing Passport account)** and cell phone number for you to save in the patient’s chart. 2. Then the legal representative will link the patient’s account to their Passport account by finding the "claim chart" link in their email. They'll log in to their Passport account and follow the prompts to link the patient’s account to their own account. | - If a legal representative is creating accounts for multiple patients, have the representative complete registration fully for one patient first before you send an invite for the next patient. - Multiple legal representatives can't access a single Passport account with different email addresses. |

## **Setting up the Patient Booking Site**

If you allow patients to book appointments through your [Elation Booking Site](https://help.elationemr.com/s/article/Patient-Booking-Site), you can enable a setting to automatically send them a Patient Passport invitation after they book an appointment if they don’t already have an account.



To turn this on, go to **Settings** → **Calendar and Booking** → **Booking Site** → **Preferences** →**Automatically send patients an email invitation to join Elation Patient Passport after they book online (if they don't already have a Passport account)**.

ℹ️  **NOTE** If many of your patients plan to use one Patient Passport account to access multiple charts—such as parents managing children’s records or caregivers managing relatives’ charts—we recommend leaving this setting off so that your staff can confirm the use case for the account with the patients before sending an invitation.

# **Related Articles**

- [Elation Patient Passport Introduction](elation-patient-passport-an-introduction.md)
- [Elation Patient Passport Guide - Managing Passport invitations](Managing-Passport-invitations.md)
- [Elation Patient Passport Guide - Communicating with patients & sharing records](Passport--Communicating-with-patients.md)
- [Elation Patient Passport Guide - Helping patients troubleshoot Passport issues](troubleshooting-passport-with-patients.md)
- [Elation Patient Passport Guide - Patient's Point of View](what-patient-passport-messaging-looks-like-to-a-patient.md)