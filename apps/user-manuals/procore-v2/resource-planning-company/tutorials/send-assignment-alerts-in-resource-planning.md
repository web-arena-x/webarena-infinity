# Send Assignment Alerts in Resource Planning

Source: https://v2.support.procore.com/product-manuals/resource-planning-company/tutorials/send-assignment-alerts-in-resource-planning

---

## Background

Assignments allow you to manage your resources by assigning them to projects.

You can send assignment alerts to notify the assignees and share key information about their assignment such as when they have a new assignment or when there are updates to dates, times, projects or locations.

## Things to Consider

- [Required User](/product-manuals/resource-planning-company/permissions) [Permissions](/product-manuals/resource-planning-company/permissions)
- Assignment alerts can be sent to individuals or multiple assignees.
- If custom assignment alerts are enabled for projects, they are sent instead of the default assignment alert.
- Only default assignment alerts can request a response.

  - Depending on their settings, people can respond to alerts by SMS or email.
- Assignment alerts are not automatically sent when bulk editing or bulk deleting resource assignments.
- From the Assignments List, you can send alerts for individual assignments, or multiple assignments.
- From the Assignments Boards or Assignments Gantt, you can send assignment alerts for all assignments for project on a certain date, or within a certain date range.

## Steps

You can send resource assignment alerts from the following places in Resource Planning:

- [Assignments Boards](#send-assignment-alerts-from-the-assignments-boards)

  - Send alerts to all assignees for a project for a certain date or within a date range.
- [Assignments Gantt](#send-assignment-alerts-from-the-assignments-gantt)

  - Send alerts to all assignees for a project for a certain date or within a date range.
- [Assignments Gantt (Beta)](#send-assignment-alerts-from-the-assignments-gantt-beta)

  - Send alerts to all assignees for a project for a certain date or within a date range.
- - Send alerts to individual or multiple assignees.
- [Assignments List (Beta)](#send-assignment-alerts-from-the-assignment-gantt)

  - Send alerts to individual or multiple assignees.

## Send Assignment Alerts from the Assignments Boards

From the Assignments Boards, you can send assignment alerts for all assignments for project on a certain date, or within a certain date range.

1. Navigate to the Company level **Resource Planning** tool.
2. Click **Assignments** and select **Assignments Boards**.
3. Click the ellipsis  for the project for which you want to send the assignment alert.
4. Select **Send Assignment Alerts**.
5. Select the date range for the alert.

   - **Current Viewing Day** to send the alert to all assignees with an assignment on the date selected
   - Select **Date Range** to send the alert to all assignees with an assignment within the date range selected.

     1. **Start Date.** Select the start date of the date range.
     2. **End.** Select the end date for the date range.

        - Select **Date** and select the **End Date** to choose a specific end date for the range.
        - Select **Weeks** and enter the **Number of Weeks** for the date range.
6. Select when to send the alert:

   - **Send Immediately.** Select this to send the alert immediately, then click **Send**.
   - **Schedule.** Select this to schedule the alert to be sent in the future.

     1. Select the **Date** and **Time** to send the alert.
     2. Click **Save**.
   - **Save Draft.** Select this to save the alert as a draft. Then click **Save**.
7. Click **Edit Alert Template**.
8. Enter the **Subject**.
9. Enter the **Alert Content** or **Message**. You can select dynamic tokens to display data relevant to the recipient and their assignment. **Show/Hide Fields**

   - **Assignee's Name.** The assignee's first and last name.
   - **Assignee's Email.** The assignee's email address.
   - **Assignee's Phone.** The assignee's phone number.
   - **Assignee's Job Title.** The assignee's job title.
   - **Assignment Start Date.** The assignment's start date.
   - **Assignment End Date.** The assignment's end date.
   - **Assignment Start Time.** The assignment's start time.
   - **Assignment End Time.** The assignment's end time.
   - **Assignment Work Days.** The assignment's work days.
   - **Project Name.** The project's name.
   - **Project Address.** The project's address.
   - **Project City.** The project's city.
   - **Project State.** The project's state.
   - **Project Postal Code.** The project's postal code.
   - **Project Country.** The project's country.
   - **Project Number.** The project number.
   - **Project Status.** The project's status.
10. Select the 'Message Type'.
11. Click **Review Recipients**.
12. Click **Send**.

## Send Assignment Alerts from the Assignments Gantt

From the Assignments Gantt, you can send alerts for all assignments for project on a certain date, or within a certain date range.

1. Navigate to the Company level **Resource Planning** tool.
2. Click **Assignments** and select **Assignments Gantt**.
3. Select **Projects**.
4. Click the ellipsis  for the project for which you want to send the assignment alert.
5. Select **Send Assignment Alerts**.
6. Select the dates for the assignments.

   - Select **Current Viewing Day** to send the alert to all assignees with an assignment on the date selected.
   - Select **Date Range** to send the alert to all assignees with an assignment within the date range selected.

     1. **Start Date.** Select the start date of the date range.
     2. **End.** Select the end date for the date range.

        - Select **Date** and select the **End Date** to choose a specific end date for the range.
        - Select **Weeks** and enter the **Number of Weeks** for the date range.
7. Select when to send the alert:

   - **Send Immediately.** Select this to send the alert immediately, then click **Send**.
   - **Schedule.** Select this to schedule the alert to be sent in the future.

     1. Select the **Date** and **Time** to send the alert.
     2. Click **Save**.
   - **Save Draft.** Select this to save the alert as a draft. Then click **Save**.
8. Click **Edit Alert Template** to edit the assignment alert.

   1. Enter the **Subject**.
   2. Enter the **Alert Content** or **Message**. You can select dynamic tokens to display data relevant to the recipient and their assignment. **Show/Hide Fields**

      - **Assignee's Name.** The assignee's first and last name.
      - **Assignee's Email.** The assignee's email address.
      - **Assignee's Phone.** The assignee's phone number.
      - **Assignee's Job Title.** The assignee's job title.
      - **Assignment Start Date.** The assignment's start date.
      - **Assignment End Date.** The assignment's end date.
      - **Assignment Start Time.** The assignment's start time.
      - **Assignment End Time.** The assignment's end time.
      - **Assignment Work Days.** The assignment's work days.
      - **Project Name.** The project's name.
      - **Project Address.** The project's address.
      - **Project City.** The project's city.
      - **Project State.** The project's state.
      - **Project Postal Code.** The project's postal code.
      - **Project Country.** The project's country.
      - **Project Number.** The project number.
      - **Project Status.** The project's status.
9. Select the 'Message Type'.
10. Click **Review Recipients**.
11. Click **Send**.

## Send Assignment Alerts from the Assignments Gantt (Beta)

##### Beta

This feature is in beta and available for customers using the Resource Planning tool.

1. Navigate to the Company level **Resource Planning** tool.
2. Click **Assignments** and selectÂ **Gantt (Beta).**
3. Right click the project and select **Send Assignment Alerts.**
4. Select who to send the alert to.

   - Select to send to **people assigned on the current viewing day.**
   - Select to send to **people assigned within a date range.**

     1. Select the **start** and **end dates**.
5. Optional: Schedule delivery

   1. Move the **Schedule Delivery** toggle to the ON position.
   2. Enter the **date** to send the alert.
   3. Select the **time** to send the alert.
6. Enter the **Subject**.
7. Enter the **Alert Content** or **Message**. You can select dynamic tokens to display data relevant to the recipient and their assignment. **Show/Hide Fields**

   - **Assignee's Name.** The assignee's first and last name.
   - **Assignee's Email.** The assignee's email address.
   - **Assignee's Phone.** The assignee's phone number.
   - **Assignee's Job Title.** The assignee's job title.
   - **Assignment Start Date.** The assignment's start date.
   - **Assignment End Date.** The assignment's end date.
   - **Assignment Start Time.** The assignment's start time.
   - **Assignment End Time.** The assignment's end time.
   - **Assignment Work Days.** The assignment's work days.
   - **Project Name.** The project's name.
   - **Project Address.** The project's address.
   - **Project City.** The project's city.
   - **Project State.** The project's state.
   - **Project Postal Code.** The project's postal code.
   - **Project Country.** The project's country.
   - **Project Number.** The project number.
   - **Project Status.** The project's status.
8. Save or send the alert.

   - Click **Save Draft** to save the alert as a draft.
   - Click **Send** to schedule or immediately sendÂ the alerts.

## Send Assignment Alerts from the Assignment Gantt

1. Navigate to the Company level **Resource Planning** tool.
2. ClickÂ AssignmentsÂ and selectÂ **Assignments List**.
3. Mark the checkbox for each assignment you want to send an alert for.
4. Click the **send**  icon and select when to send the alert:

   - **Send Immediately.** Select this to send the alert immediately, then click **Send Alerts**.  
     *Note:* This will send the alert immediately based on the default or project assignment alert settings.
   - **Schedule.** Select this to schedule the alert to be sent in the future.  
     *Note:* You can edit or send the scheduled alert at a later time. See [Manage Scheduled Assignment Alerts](/product-manuals/resource-planning-company/tutorials/manage-scheduled-assignment-alerts-for-resource-planning).

     1. Select the **Date** and **Time** to send the alert.
     2. Click **Schedule Send**.
   - **Save Draft.** Select this to save the alert as a draft. Then click **Save Draft Alerts**.  
     *Note:* You can edit or send the draft at a later time. See [Manage Draft Assignment Alerts](/product-manuals/resource-planning-company/tutorials/manage-draft-assignment-alerts-for-resource-planning).