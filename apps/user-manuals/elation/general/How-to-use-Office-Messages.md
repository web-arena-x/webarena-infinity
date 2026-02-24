# Office Message Feature Guide- The enhanced inter-office communications tool

Source: https://help.elationhealth.com/s/article/How-to-use-Office-Messages

---

## **Contents**

- [​​​​​What is the Office Message feature?](#description)
- [Why is the Office Message feature valuable?](#value)
- [Sending Office Messages](#send_office_message)
 - [Initiating a new Office Message](#initiate_new_message)
 - [Composing a new Office Message](#compose_new_message)
    - [Additional Office Message configuration options](#office_message_configurations)
 - [Sending new Office Messages](#send_office_message)
- [Viewing & replying to active Office Message threads](#view_active_messages)
 - [Viewing active Office Messages from the Practice Home Requiring Action Queue](#view_active_messages_in_Practice_Home)
 - [Viewing active Office Messages from the patient’s chart](#view_active_messages_in_patient_chart)
 - [Replying to Office Message threads](#reply_to_messages)
 - [Viewing Office Message threads with multiple replies](#view_messages_with_multiple_replies)
- [Managing recipients in active Office Message threads](#managing_recipients)
 - [Adding or removing recipients](#edit_recipients)
- [Using the "Keep Requiring Action" checkbox](#keep_requiring_action)
- [Closing Office Message threads](#close_message)
 - [“Sign Off”](#sign_office_message)
    - [“Acknowledge”](#acknowledge_office_message)
 - ["Mark Complete"](#mark_complete_message)
- [Viewing closed Office Messages in the Chronological Record](#view_closed_messages)
- [Removing or deleting an Office Message thread](#delete_office_message)
- [Premium EHR features](#premium_EHR)
 - [Sending Office Messages to User Groups only](#send_to_user_groups_only)
 - [Allowing Staff Level Users to sign off messages on behalf of Provider Level Users](#delegates)
 - [Workspaces](#Workspaces)
- [Frequently Asked Questions (FAQ)](#faq)

## **​​​​​What is the Office Message feature?**

Elation’s Office Message feature allows you to send messages about specific patients to anyone who has a user account for your EHR. Recipients of Office Messages can easily track and reply to messages on their Elation Practice Home page, and closed threads become archived in the patient’s chart for future reference.

## **Why is the Office Message feature valuable?**

The Office Message feature facilitates internal communication, allowing you to keep track of conversations and tasks that need to be completed by anyone in your office. You can also set reminders for yourself, your colleagues and your staff to follow up on action items. Since Office Messages are visible to everyone in the practice, this feature fosters transparency to ensure that nothing falls through the cracks.

## **Sending Office Messages**

### **Initiating a new Office Message**

You can initiate an Office Message from 3 different locations in the EHR:

1. From the Practice Home page by clicking "Message":

![]()

1. From the gray navigation bar at the top of a patient's chart by clicking “Msg”:

![]()

1. From any Order, Report, Letter, Visit Note, or Note by clicking "Actions" -> "Office Message":

![]()

- **User Tip**: With this third method, the Order, Report, Letter, Visit Note or Note will be attached to the Office Message so that it can be referenced.

### **Composing a new Office Message**

To compose a new Office Message:

1. Enter the patient's name in the **Pt** box to indicate who the message is about.
   - If you need to correct the name, click the “Actions” button next to the patient’s name followed by “Remove”.
   - If you initiated the Office Message from the patient's chart, the patient’s name will be automatically populated
2. Search for and select recipients from the dropdown menu in the **To** box- choose individuals or try adding a [User Group](https://help.elationemr.com/s/article/user-groups).
   - **Important Note**: If you are Premium EHR user, reference the [*Premium EHR features* section](#premium_EHR) below for important details and additional features tied to selecting recipients.
3. Compose your message in the **Msg** box.

#### **Additional Office Message configuration options**

- The "Keep Requiring Action" checkbox allows you to pin Office Message threads to your ‘Office Messages’ inbox in your Practice Home Requiring Action Queue, even after you’ve sent your message. Doing so allows you to quickly locate and reference high priority threads. For more information on this feature, please see the *[Using the "Keep Requiring Action" checkbox](#keep_requiring_action)* section of this article.
 - Recipients will continue to see the Office Message in their own ‘Office Messages’ inbox.
- The "Urgent" checkbox will add the office message to the recipient's ‘Urgent’ inbox in their Practice Home Requiring Action Queue in addition to their ‘Office Messages’ inbox.

### **Sending new Office Messages**

You have two timing options when sending a new Office Message:

1. Clicking “Send” will send the new Office Message immediately to all selected recipients.
2. Entering a date in the Pd box will allow you to send the message at a later date. The message will be sent at 12:00am local time on the date selected. This option can be used to create a [reminder for yourself or recipients](Office-Messages-Feature-Guide-Using-office-messages-for-reminders.md) to follow up on a specific task at a future date or time.
   - **User Tip**: You can enter a relative date, for example '1 week' or '1 month' into the **Pd** field and Elation will automatically calculate the date for you.

## **Viewing and replying to active Office Message threads**

You can view active (unsigned) Office Message threads on Elation’s Practice Home page as well as in the patient’s chart.

### **Viewing active Office Messages from the Practice Home Requiring Action Queue**

You can find all active (unsigned) Office Messages that require your attention in the ‘Office Messages’ inbox of your Practice Home Requiring Action Queue.
![]()

The Requiring Action Queue in the Practice Home comes with a "View Queue For:" menu that will allow you to look at other Providers'/staff members’ Requiring Action items.

- **User Tip**: The "View Queue For:" option comes in handy when you need to assist colleagues or other staff members with open items while they are unavailable. Administrative users can also use this feature to keep track of responsibilities and productivity.

### **Viewing active Office Messages from the patient’s chart**

Active (unsigned) Office Messages may appear in two different sections at the top of the patient's chart:

- Any Office Messages that have been delivered to you, and presumably required your attention as a next step, will appear in the ‘Requiring Action’ section of the patient's chart.
- Any Office Messages that are waiting on a response from other members of your practice will be located in the ‘Outstanding Items’ section of the patient’s chart.

### **Replying to Office Message threads**

- Click the "Reply" box at the bottom of any active (unsigned) Office Message threads to write a custom reply.
 - Your reply will be delivered to the individuals whose specific names are listed as recipients.
 - If there are any User Groups listed as recipients, only the members of the User Group who have already responded to the thread will receive your reply.
- Optionally, click “Quick Reply” to select from a list of standardized reply templates:
 - “Recall patient” = ‘Please call patient in for appointment.’
 - “Get patient on phone” = ‘Please get patient on phone.’
 - “Information patient of results” = ‘Please call and inform patient of results.’
 - “Should have appointment already book” = ‘Patient should have appointment already booked.’

### **Viewing Office Message threads with multiple replies**

When an Office Message thread already has a history of replies, you will see the buttons “Show # reply” or “Hide # reply” in the Office Message thread. Click on these prompts to reveal or collapse all previous replies in the Office Message thread.

- By default, active (unsigned) Office Message threads will be expanded so you can optionally click “Hide # reply” to collapse.
- By default, closed Office Messages threads will be collapsed so you can optionally click “Show # reply” to expand.

## **Managing recipients in active Office Message threads**

![]()
When replying to active Office Message threads, any user can click the “Edit” button next to the recipients list to add or remove recipients from the Office Message thread. This feature comes in handy when you:

- have multiple team members with similar responsibilities so they should all be notified
- have team members rotating in and out of the office
- need to redirect attention to the correct team member

### **Adding or removing recipients**

Any user can add or remove recipients from active Office Message threads to adjust the team members who need to receive the message. To add or remove recipients:

1. Click the “Edit” button next to the recipient’s list at the top of the Office Message
2. Type in names of individuals or User Groups to add them to the Office Message thread
   - **Important Note**: If you are a Premium EHR user, reference the [*Premium EHR features* section](#premium_EHR) below for important details and additional features tied to selecting recipients.
3. Click the “X” button at the end of an individual or User Group’s name to remove them from the Office Message thread
4. Click the “Save” button to save your changes
   - If any recipients were added or removed, a note will appear in the Office Message thread to indicate this change.

![]()

**Important Notes**:

- If at least one Provider Level User is on an Office Message thread, a Provider Level User will be required to sign the thread in order to close it.
- Removing all Provider Level Users from an Office Message thread means that any user will be able to close the Office Message thread.
- Removing any recipient from an Office Message means they will no longer be notified of subsequent replies to the thread. Take caution when removing recipients.

## **Using the "Keep Requiring Action" checkbox**

![]()
When sending an office message, you can optionally select the "Keep Requiring Action" checkbox if you’d like to keep a copy of the Office Message thread in your own Practice Home Requiring Action Queue. If this checkbox is not selected, the Office Message thread will not appear on your Practice Home until someone replies to you within the thread. Use this feature when there are Office Message threads that you want to keep an eye on from your Practice Home page.

**User Tip**: If the Office Message thread that you’re writing to includes a User Group in the “To” field, the "Keep Requiring Action" checkbox has the added effect of sending  the Office Message to the Practice Home Requiring Action Queues of everyone in the User Group. If “Keep Requiring Action” is not selected in this scenario, after the initial message is sent, replies to the message thread will only be displayed on the Practice Home of User Group members who at some point personally replied to the thread.

## **Closing Office Message threads**

To close an Office Message thread, your user type and the user type of other recipients in the thread, will determine what type of button you’ll see:

- Provider Level Users will always see “Sign off”
- Staff Level Users will see “Mark Complete” if there are only Staff Level Users in the Office Message thread

Although labeled differently, these two buttons serve the same purpose - to close the message thread and archive it into the Chronological Record of the patient’s chart.

### **“Sign Off”**

Provider Level Users are allowed to sign any Office Message thread - regardless of whether they are part of the thread’s recipient list.
![]()
The “Sign” action can be taken from 2 areas of the message thread:

1. If no written reply from the Provider Level User is necessary, they should click the upper “Sign Off” button.
2. If the Provider Level User wishes to type a response before closing the thread, they should click the “Send & Sign Off” button beneath the reply box.

If the Provider Level User typed a response before signing the thread, everyone on the recipient list will receive the written response in their ‘Office Messages’ inbox of their Practice Home Requiring Action Queue. and will need to click an “Acknowledge” button to dismiss the thread.

#### **“Acknowledge”**

![]()
This feature ensures that all recipients (in any Office Message thread containing Provider Level Users) view the final reply of the Office Message thread after it has been signed off by the Provider Level User. When a Provider Level User clicks “Send & Sign Off”, recipients must click "Acknowledge" after reading the latest replies to dismiss the Office Message thread from their Requiring Action Queue and only store the completed Office Message thread in the patient’s chart.

**Important Note**: If there are multiple Provider Level Users in the Office Message thread, all Provider Level Users who did not sign the Office Message thread must click “Acknowledge” to dismiss the Office Message thread from their own Requiring Action Queue.

### **“Mark Complete”**

![]()
Office Messages threads that only contain Staff Level Users on the recipient list can be closed out by any of those Staff Level Users. By clicking the “Mark Complete” button, the Office Message will be dismissed from everyone’s Practice Home Requiring Action  Queue and become filed into the Chronological Record of the patient’s chart.

**Important Note**: This button was previously named “Acknowledge for Group”.

## **Viewing closed Office Messages in the Chronological Record**

 Closed Office Messages, after they are signed off or marked complete, will be stored in the patient’s Chronological Record as shown below. To reveal the history of replies on the thread, click “Show # replies”.

## **Removing or deleting an Office Message thread**

You can remove an Office Message by going into the patient's chart and clicking "Actions" -> "Remove" at the top right corner of any Office Message thread. This action will delete the thread from the patient’s record.
![]()

## **Premium EHR features**

**Important Note**: The features listed in this section are part of Elation's Premium EHR offering.

- If you are already a Premium EHR user and you are interested in using any of these features, click the "I need help" button to notify Elation and a member of the Elation Team will activate the feature for you.
- If you are interested in upgrading to Premium EHR to use any of these feature, click the "I need help" -> "Contract Elation Support" button and a member of the Elation team will assist you.

### **Sending Office Messages to User Groups only**

Premium EHR users can request a feature that customizes how Office Messages are sent. When the feature is activated, you can only select [User Groups](user-groups.md) in the **To:** field when selecting recipients and you will not be able to select individual user's names. This feature makes it easier to route communications and tasks to the appropriate team by sending messages to users according to their function or responsibilities.

### **Allowing Staff Level Users to sign off messages on behalf of Provider Level Users**

Premium EHR users can assign specific User Groups as office message delegates, allowing all Staff Level Users in the group to sign Office Messages on behalf of all Provider Level Users in the EHR. These Staff Level Users will have the same sign off workflows as a Provider Level User. [Click here to learn more about Office Message Delegates](https://help.elationemr.com/s/article/staff-permissions--staff-delegates#practice-office-message-delegates).

### **Workspaces**

If you are using Elation's Workspaces feature for Premium EHR users, [reference this guide](workspaces-guide.md#People_List) to ensure the correct users appear in your Workspace User Groups so that the appropriate recipients appear for selection when writing Office Messages. If you only see the Provider List Setting and you do not see the People List Setting in your Workspaces Settings, please use the "I need help" button at the top of your account to notify us and a member of the Support Team will assist you with enabling the People List Setting.

## **Frequently Asked Questions**

#### **Can I send an Office Message that’s NOT affiliated with a specific patient?**

Office Messages must be affiliated with a patient chart, but you can create a chart with a generic name (ex. First Name: Internal, Last Name: Office Messages), and then use that generic patient chart to send Office Messages that are not patient-specific.

#### **Can I send an Office Message to multiple team members?**

Yes, you can send an Office Message to any combination of individuals by selecting their names from the drop down in the “To” field and/or you can use the [User Groups feature](https://help.elationemr.com/s/article/user-groups) to group specific office members together. For example, I may send an Office Message to all 5 medical assistants in my office by adding the 5 medical assistants to a user group called "Medical Assistants" and then selecting "Medical Assistants (Group)" from the "To" drop down.

- **Important Note**: If you are a Premium EHR user, reference the [*Premium EHR features* section](#premium_EHR) above for important details and additional features tied to selecting recipients.

#### **What’s the difference between inputting individual user names versus User Groups?**

You should input individual user names if each person needs to be equally informed and involved in the message thread. When individual names are listed as recipients, each person will always be notified of subsequent replies to the thread on their Practice Home.

You should use a User Group when only 1 (or a few) of the members of the group needs to take action (for example, among a team of Schedulers, once one Scheduler takes ownership of a request, the rest of the Schedulers can disregard the thread). When a User Group is listed as the recipient, every member of the User Group will receive the initial message on their Practice Home, but only people who have personally written at least one message on the thread will see subsequent replies on their Practice Home.

#### **How do I add a new recipient to an active Office Message thread?**

To add recipients to active Office Message threads:

1. Click the “Edit” button next to the recipient’s list at the top of the Office Message
2. Type in names of additional recipients or User Groups to add them to the Office Message thread
   - **Important Note**: If you are a Premium EHR user, reference the [*Premium EHR features* section](#premium_EHR) above for important details and additional features tied to selecting recipients.
3. Click the “Save” button to save your changes
   - A note will appear in the Office Message thread to indicate this change.
4. Afterwards you can type a reply if needed.
   - **User Tip**: You can add a recipient to an Office Message thread without writing a reply if you simply wish to grant them visibility into the existing information in the Office Message thread.

All individuals whose specific names are listed as recipients will be notified that you added a new recipient from their ‘Office Messages’ inbox of their Practice Home Requiring Action Queue. If there are any User Groups listed as recipients, only the members of the User Group who have already responded to the thread will be notified that you added a new recipient in their ‘Office Messages’ inbox of their Practice Home Requiring Action Queue.

**Important Note**: If a Provider Level User is added to the Office Message thread, a Provider Level User will be required to sign the thread in order to close it.

#### **How do I add myself to an active Office Message?**

Anyone can add themselves to an active Office Message thread by replying to the Office Message. When this happens, all individuals whose specific names are listed as recipients will be able to see your reply from the ‘Office Messages’ inbox of their Practice Home Requiring Action Queue. If there are any User Groups listed as recipients, only the members of the User Group who have already responded to the thread will see your reply in the ‘Office Messages’ inbox of their Practice Home Requiring Action Queue.

**Important Note**: If a Provider Level User is added to the Office Message thread, a Provider Level User will be required to sign the thread in order to close it.

#### **How do I remove a recipient from an active Office Message?**

To remove a recipient from an active Office Message thread:

1. Click the “Edit” button next to the recipient’s list at the top of the Office Message
2. Click the “X” button at the end of the recipient’s or User Group’s name to remove them from the Office Message thread
3. Click the “Save” button to save your changes
   - A note will appear in the Office Message thread to indicate this change.

Take caution when removing recipients. Removing all Provider Level Users from an Office Message thread means that any user will be able to close the Office Message thread. Removing any recipient from an Office Message means they will no longer be notified of subsequent replies to the thread.

#### **How can I tell who removed me from an Office Message thread I was once part of?**

To see who removed you from an Office Message thread you were once part of, find the Office Message thread in the patient’s chart and then find the note about who removed you along with the date and time of the action. The note will look like this:
![]()

#### **How do I reopen a closed Office Message thread?**

Once an Office Message thread is signed or marked complete, it cannot be reopened. You will need to start a new Office Message thread to continue the conversation.

#### **How do I edit recipients of a closed Office Message thread?**

Once an Office Message thread is signed or marked completed you can no longer edit its recipients.

#### **I no longer see the “Acknowledge for Group” button in the Office Message thread. What happened?**

The “Acknowledge for Group” button has been renamed “Mark Complete”. When a Staff Level User clicks the “Mark Complete” button, the Office Message will be dismissed from everyone’s Practice Home Requiring Action Queue and become filed into the Chronological Record of the patient’s chart.

#### **I am a Staff Level User but I cannot see the “Mark Complete” button in the Office Message thread. What happened?**

The “Mark Complete” button is only available for Staff Level Users if there are only Staff Level Users in the Office Message thread. If there are any Provider Level Users in the Office Message thread then Staff Level Users will need to wait for a Provider Level User to sign the Office Message thread in order to complete it. If a Provider Level User was accidentally added to the Office Message thread, you can follow these steps to remove them from an active Office Message thread:

1. Click the “Edit” button next to the recipient’s list at the top of the Office Message
2. Click the “X” button at the end of the Provider Level User’s name to remove them from the Office Message thread
3. Click the “Save” button to save your changes
   - A note will appear in the Office Message thread to indicate this change.

#### **Why am I seeing a message in my Requiring Action Queue if I already acknowledged it?**

If you are viewing group queues (such as "Everyone", "All Provider" or "All Staff") from the Practice Home page, you may sometimes see that a closed Office Message thread that you have acknowledged is still visible in the ‘Office Messages’ inbox. This is because ALL recipients of an Office Message thread containing Provider Level Users must acknowledge the message for it to be dismissed from their Requiring Action Queue.

Check with the other recipients of the message to make sure they have clicked the "Acknowledge" button.

#### **Can I add my own Quick Reply messages to Elation?**

We currently do not have a feature for users to customize and/or add their own quick reply messages​. ​​​​​​You can [use Templating Softwares alongside Elation](using-templating-softwares-with-elation.md) if you want to add any custom text templates in the EHR.

#### **I am unable to find a specific user in the recipients list. What happened?**

If you are using Elation's Workspaces feature for Premium EHR users, you must make sure the correct users appear in your Workspace User Groups so that the appropriate recipients appear for selection when writing Office Messages. If you only see the Provider List Setting and you do not see the People List Setting in your Workspaces Settings, please use the "I need help" button at the top of your account to notify us and a member of the Support Team will assist you with enabling the People List Setting. [Click here to learn more about using the Office Message feature with Workspaces](workspaces-guide.md#People_List).

**Next Step** **Send a message to yourself or a staff member to start coordinating on tasks!**

## **Related Articles**

- [User Groups Guide- Simplifying office messages & expanded calendar view](https://help.elationemr.com/s/article/user-groups)
- [Office Messages Feature Guide- Using office messages for reminders and task follow-up](Office-Messages-Feature-Guide-Using-office-messages-for-reminders.md)
- [Practice Home Guide- Checking for requiring action items](https://help.elationemr.com/s/article/check-for-your-offices-daily-to-do-list)
- [Templates Guide- Using templating softwares with Elation](https://help.elationemr.com/s/article/using-templating-softwares-with-elation)