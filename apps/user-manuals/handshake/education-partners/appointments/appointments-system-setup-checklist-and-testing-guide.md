# Appointments System Setup Checklist and Testing Guide

Source: https://support.joinhandshake.com/hc/en-us/articles/360007478833-Appointments-System-Setup-Checklist-and-Testing-Guide

---

This guide will help your office configure appointments in Handshake, then test the workflows involved in everything from scheduling to managing appointments. Use the Help Center links within this article for detailed guidance!

**Note:** If you'd like to create a group appointment, you can create an event and set the event type to *Group Appointment*. Set the event to invite-only and invite students that will be attending the group appointment. Learn more about creating events in [Events: Creating an Event](https://support.joinhandshake.com/hc/en-us/articles/222774407).

**Step 1: Configure Appointment Settings in Handshake**

**![](https://support.joinhandshake.com/hc/article_attachments/25991264516375)**Create Your Appointment Types

- Appointment types are the kinds of appointments that can be scheduled for your office, i.e resume checks, mock interviews, career planning, etc. You can define which groups of students can select certain appointment types by setting qualifications. *Learn more on how to* [*Set Appointment Qualifications*](https://support.joinhandshake.com/hc/en-us/articles/218693528)*.*

To access your appointment types in Handshake, navigate to "School Settings" > "Appointment Types".

For more information on creating and managing types, refer to [School Settings: Appointment Types](https://support.joinhandshake.com/hc/en-us/articles/224601047). 

**Best Practice**: *If you have multiple career centers, add the location in the name of the appointment type. This way the location is included in student reminder emails. It may make sense to duplicate appointment types for this purpose - that’s ok!*

**Best Practice**: *If you want standardized information when students are scheduling or staff members are running appointments, configure your pre-appointment, post-appointment, and staff member survey in your appointment type set-up. If you'd like to learn more about setting up surveys, please refer to* [*Creating and Testing Surveys*](https://support.joinhandshake.com/hc/en-us/articles/218693548)*.*

***Best Practice**: If each advisor in your office works with a different group of students, and you would like to make sure that students can only select appointments relevant to them, then we recommend to create appointment types for each of those groups. This particular setup works best if each advisor creates appointment types with the same naming conventions.*

**![](https://support.joinhandshake.com/hc/article_attachments/25991264516375)**Create your Appointment Categories

- Appointment Categories provide first-level appointment type organization for students to choose from, making it easier for the student to choose the appropriate appointment.

To access your appointment categories in Handshake, navigate to "School Settings" > "Appointment Categories".

For more information on creating and managing categories, refer to [School Settings: Appointment Categories](https://support.joinhandshake.com/hc/en-us/articles/218693018). 

***Best Practice**: Categorize appointments by college, career center, or subject area and standardize your categories. We highly recommend having a standard naming convention across campus to reduce confusion.*

**![](https://support.joinhandshake.com/hc/article_attachments/25991264516375)**Create Your Appointment Mediums

- Appointment Mediums are the methods you will use to conduct your appointments. These may include: Face to face, phone call, video call, etc.
- You can activate the Handshake provided medium "Virtual on Handshake" to use integrated video for your appointments, providing a seamless experience while generating useful reporting data! Read more about [Virtual Appointments on Handshake](virtual-appointments-on-handshake.md).

To access your appointment mediums in Handshake, navigate to "School Settings" > "Appointment Mediums".

For more information on creating and managing mediums, refer to [School Settings: Appointment Mediums](https://support.joinhandshake.com/hc/en-us/articles/4406019952279). 

***Best Practice**: As an alternative to adding the location to the appointment type, consider adding the location in the medium if you are having an in person appointment, for example: “In person - Career Center, Fisher Hall”. The appointment medium is included in the reminder emails that are sent 24 hours and 1 hour prior to the appointment.*

**![](https://support.joinhandshake.com/hc/article_attachments/25991264516375)**Configure Your Appointment Preferences

- Configure different appointment related settings like auto-approval, request timeframe and permission labels.  For more details on how to configure these settings, please see the article linked out above.

To access your appointment preferences in Handshake, navigate to "School Settings" > "Appointment Preferences".

For more information on creating and managing preferences, refer to [School Settings: Appointment Preferences](https://support.joinhandshake.com/hc/en-us/articles/219132837). 

***Best Practice:** If you need to exclude a subset of students from accessing appointments altogether, talk to your IT team about importing a label called “no appointments” (or something similar) onto those student profiles. You can then use that label to set a restriction on the Appointment Preferences page. Read more on* [*Importing Labels*](https://support.joinhandshake.com/hc/en-us/articles/229507687)*.*

**![](https://support.joinhandshake.com/hc/article_attachments/25991264516375)**Set your maximum open appointments & Appointment Cancellation Timeframe

- The maximum open appointment setting is the maximum number of concurrent appointment requests a student may have at once.  
  - This setting includes all future appointments (approved, pending, etc), based on the appointment start date. Until the start date has passed, the system won't allow the student to schedule any new appointments beyond the limit set.
- The appointment cancellation time frame allows your to specify the period of time in which a student can cancel their appointment prior to the appointment start time.

To manage these settings in Handshake, navigate to "School Settings" > "Details". For more information, refer to [School Settings: Details](../handshakes-school-settings/school-settings-details.md).

**Step 2: Have each Career Center Staff Member Configure their own Appointment User Settings**

**![](https://support.joinhandshake.com/hc/article_attachments/25991264516375)**Add Appointment Types

- Choose the types of appointments that students will be able to schedule with you by clicking the green “Add” button.  Students will only be able to schedule these types of appointment with you.

**![](https://support.joinhandshake.com/hc/article_attachments/25991264516375)**Add Appointment Blocks

- Designate blocks of time that students will be able to schedule appointments with you. Within each block, you can designate specific appointment types that you will conduct, as well as specific mediums available during that time. 
  - Students will not be able to schedule an appointment with you until you set up available appointment blocks.

**Note**: If a block is made available for drop-ins, the appointment block will not be available for scheduled appointments.

[Configure Your Personal Appointment Availability (Appointment Blocks & Types)](https://support.joinhandshake.com/hc/en-us/articles/218693168-How-to-Configure-Your-Personal-Appointment-Availability-Appointment-Blocks-Types-) for more information and guidance on adding appointment blocks.

***Best Practice**:* [*Sync your calendar with two-way calendar sync.*](https://support.joinhandshake.com/hc/en-us/articles/115011864208) *Keep in mind this will impact your availability. Events in your external calendar that are “busy” will pull into Handshake, and your scheduled Handshake appointments will pull into your external calendar. Check with your IT team to find out what server you are on.*

**Step: 3 Think you’re ready? Run through these tests to make sure!**

**![](https://support.joinhandshake.com/hc/article_attachments/25991264516375)**Ensure the correct appointment categories and types are visible to students

1. Navigate to a student’s profile and click “View As This User” in the actions section.
2. Go to Career Center > Appointments and click “Schedule a New Appointment”.
3. Verify that the correct categories, types, dates/times, and mediums are visible to that student.

**Best Practice**: *If you have qualifications set on your appointment types, repeat this process with multiple students of varying qualifications and for each impacted appointment type.*

**![](https://support.joinhandshake.com/hc/article_attachments/25991264516375)**Sign up for an appointment as a student and approve it as a career services user

1. Request an appointment with your test student account. **Note:** As of May 2023, staff member names will be randomized when selecting an appointment. Previously, staff names were listed alphabetically. This change increases the likelihood that students will schedule appointments with a variety of different staff members.
2. Switch users back to your career services view.
3. Navigate to the appointments page and approve the appointment.

**![](https://support.joinhandshake.com/hc/article_attachments/25991264516375)**Launch the check-in kiosk and check-in for your appointment as a student

1. For in-person appointments, navigate to Appointments and click the “Check-in Kiosk” tab.
2. Select your office location, career center, and if you will allow drop in appointments.

**Note**: if you do not click “allow drop-in appointment”, students will only be able to check in for scheduled appointments.

**Important**: choosing "Keep me logged in" will allow students checking in to have access to your account. For testing, this is fine, but proceed with caution if you decide to choose this option outside of testing.

     3. Enter the email address or username of the student you are testing with.

     4. Select the scheduled appointment.

**![](https://support.joinhandshake.com/hc/article_attachments/25991264516375)**Start and complete the scheduled appointment

1. Click “Appointments” > “Manage” > Click on the row pertaining to the appointment that you want to start.
2. To start the appointment, click “Appointment Started”. If you're testing a Virtual on Handshake appointment, joining video will trigger the appointment start.
3. To complete the appointment, click “Complete Appointment”.

**Note**: marking the appointment complete is critical to ensure post-appointment surveys are sent as well as reporting accuracy.

![complete.png](https://support.joinhandshake.com/hc/article_attachments/25991264518295)

**![](https://support.joinhandshake.com/hc/article_attachments/25991264516375)**Check-in for a drop-in appointment as a student

1. Launch your check-in kiosk and select “Allow Drop-In Appointments”.
2. Check-in as a student and select the drop-in option.

**Tip**: If you aren't able to select a drop-in option, make sure there is at least one appointment block available at that time with "drop-in" selected.

**![](https://support.joinhandshake.com/hc/article_attachments/25991264516375)**Start a drop-in appointment from the waiting room

1. Viewing from your career services user, navigate to the waiting room via “Appointments” > “Waiting Room”.
2. Click “Start Appointment”.
3. Verify information about the appointment and click “Create”. *(If you're planning to send a post-appointment survey, remember to only mark the appointment as 'started' on this screen, then click 'Complete Appointment' to trigger the email!)*

![waiting_room.png](https://support.joinhandshake.com/hc/article_attachments/25991264519447)

## **Additional Resources**

- [Appointments Troubleshooting Guide](appointments-troubleshooting-guide.md)
- [Handshake Community - Appointments](https://support.joinhandshake.com/hc/en-us/community/topics/115000555148-Appointments)
- Appointments Help Center:
  - [Operations > Setup & Configuration](https://support.joinhandshake.com/hc/en-us/sections/204176117-Handshake-s-School-Settings)
  - [Student Engagement & Usage](https://support.joinhandshake.com/hc/en-us/sections/1500000983581-Appointments)