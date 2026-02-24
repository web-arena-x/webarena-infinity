# Event Mediums in Handshake

Source: https://support.joinhandshake.com/hc/en-us/articles/6330606403735-Event-Mediums-in-Handshake

---

Handshake has incorporated Event Mediums and revitalized the event creation form! 

The updates to the event creation form and the addition of mediums provide Career Services users with:

- A cleaner UI
- A new event “Medium” field allowing you to mark an event as virtual only, in-person, or in-person with a virtual link
- New “Add Employers” and “Add Schools” options on the form itself that’ll allow you to add participating employers and schools (these flows will still exist on the event page)
- New help language and embedded help center articles to assist with user flow

## Using Event Mediums

The introduction of Event Mediums enables:

- Career Services users to create virtual, in-person, and hybrid events.
- Employers to choose from in-person, virtual, or hybrid mediums when requesting on-campus events.
- Reporting on in-person, virtual, and hybrid events, available in Analytics via the Events report type.

Previous events (created prior to this feature release) have been backfilled for mediums since this is now a required field for all events.

- Any events that had the “virtual session” type have been backfilled with a “virtual” medium.
- Events that did not have the virtual session type have been backfilled with an “in-person” medium.

### Student usage considerations

When searching or browsing for events, events are displayed based on the selected medium:

- **In-person events *without* the option to join virtually** will show up for students who filter for “on-site” events. Career services team members can add a Room (pulled from School Settings) or a specific event location address that will be displayed on the event for students.
- **In-person events *with* the option to join virtually** will show up for students who filter for “on-site” events OR “virtual” events. The physical location AND a “Join Video” button are displayed on the student event page.
  - Like other virtual events, the join video button will go live 5 min before the event and will lead to whichever virtual event link you included in the event form.
- **Virtual only events** will show up for students who filter for “virtual” events. The “Join Video” button is displayed on the student event page.
  - The “Join Video” button will go live 5 min before the event and will lead to whichever virtual event link you included in the event form.

Student registration for hybrid events looks the same as it does for in-person or virtual only. Because of this, there is not an automated way to report on how a student checked-in (virtually or in-person).

- **Tip**: if you'd like to track how students plan to attend the event, we recommend adding a custom attendee survey question–ask if they plan to attend virtually or in-person!

When a waitlist is enabled, the registration limit applies to all registrants, since virtual and in-person registrants are not tracked separately. 

## Creating a new event

Click **Events** from the left navigation bar in Handshake, then click the **New Event** tab in the upper-right corner of the page.

The new form will load, where you will enter event information. The form is broken down into three sections, as described below:

### Event details:

- Name
- Type (dropdown menu)
  - Workshop
  - Info Session
  - Group Appointment
  - Networking
  - Speaker/Panel
  - Employer On-site
  - Virtual Session
  - Mock Interview
  - Classroom Presentation
  - Other
- \*Career Center (dropdown menu, if more than one Career Center is configured in School Settings)
- Contacts
- Date and Time
  - Start Date *(select from date and time in calendar)*
  - End Date *(select from date and time in calendar)*
  - Timezone
- Event Location
  - **In person**
    - Select a room from the dropdown menu.
    - Enter the physical location of the event (n/a if a room is selected - the room's address will be used).
    - This in-person event can also be attended virtually. Check this box if you'd like to allow virtual attendance, then enter the **Virtual attendance link** in the text box.
  - Virtual only
    - Enter the **Virtual attendance link** in the text box.

Click the blue button **Next Step: Visibility and branding**.

### Visibility and branding

- Description
- Image (Your institution's logo will appear by default. If you change the event image, a 400 x 400 pixel image is recommended.)
  - Change image
  - Delete image

Click the blue button **Next step: Attendance**.

### Attendance

- Coordinating with employers for this event?
  - Add employers here to help Handshake recommend the event to your students and to display the employer’s logo on the event page. Employers you add will see this event appear in their events list. Learn more.
    - **Search for employers name**
- Participating institutions
  - Students from other participating institutions will be able to register for this event.
    - **Select from other Handshake-partnered institutions on Handshake in the text field.**
- Admission
  - Will there be a cost for this event?
    - **Click on Free or Paid as appropriate. If Paid is selected, enter the appropriate dollar amount for Students and/or Employers.**
- Is there a maximum number of students that can attend?
  - Once maximum is reached, students can join a waitlist. If there isn't a maximum, leave at 0. Learn more.
    - **Enter the maximum students that can attend, if applicable.**
- Invite only (checkbox)
  - Restrict event visibility to the students you invite through Handshake. Learn more.
    - **Check the box to restrict event visibility to only invited students.**
- Student Registration
  - Set a registration window. If fields are left blank, registration will open when you publish the event.
    - **Set the Start date and End date and time.**
- External registration (checkbox)
  - Students will be redirected to the external registration link (like Eventbrite) when they click "Register" in Handshake.
    - **Check the box to have students register on an external site.**
- Attendee survey (dropdown menu)
  - A survey that students complete when registering. The questions come from a survey that you or a staff member can create in Handshake.
    - **Select a survey from the dropdown menu.**
      - **Note**: surveys must be configured prior to  attaching to the event.
- Student welcome message (optional)
  - toggled off by default–toggle on to include a custom message in the email students get after registering for your event.
- Name tag (optional)
  - toggled off by default–toggle on to sync a printer to Handshake to print out name tags for your in-person event upon student check-in.
  - **When enabled, add your XML in the text field.**

Click the blue button **Publish Event** to save the new event.