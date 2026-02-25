# Configure Advanced Settings: Project Schedule

Source: https://v2.support.procore.com/product-manuals/schedule-project/tutorials/configure-advanced-settings-project-level-schedule

---

## Things to Consider

- **Required User Permissions:**

  - 'Admin' level permissions on the project's Schedule tool.  
    *Note:* To view or edit information on the User Permissions page for the Schedule tool, 'Admin' permission to the project's Directory tool is also required.
- **Additional Information:**

  - The latest date and time that a schedule was uploaded or updated will be displayed in the header of every page in the Schedule tool's settings page next to 'Last Modified'.

## Steps

1. Navigate to the project's **Schedule** tool.
2. Click the **Configure Settings**icon.
3. Click one of the following pages:

   - General
   - File Management
   - Email Distribution
   - User Permissions  
     *Note*: This page is only available to users with 'Admin' permission to the project's Directory tool.

### General

#### Functionality

- **Enable Calendar Item Creation**: Mark the checkbox if you would like users with 'Standard' level permissions or above to create calendar items in addition to the integrated schedule. These calendar items can be published and visible to everyone on the team or personal and only visible to the person creating them.   
  See [Create a Calendar Item](/product-manuals/schedule-project/tutorials/create-a-calendar-item).

#### Project Tasks

- **Display task names with their summary task names**: Mark or remove the mark from this checkbox to change how each schedule task is displayed in the Schedule tool.
- **Allow schedule tasks to be updated via the Procore mobile app**: Mark the checkbox to enable schedule tasks to be updated from a mobile device using the Procore mobile app.

### File Management

- See [Upload a Project Schedule File to Procore's Web Application](/product-manuals/schedule-project/tutorials/upload-a-project-schedule-file-to-procores-web-application).
- See [Clear an Integrated Schedule](/product-manuals/schedule-project/tutorials/clear-an-integrated-current-schedule).

### Email Distribution

#### Project Schedule E-mail

1. Use the toggle onicon to send weekly emails to specific users showing all upcoming schedule tasks on the project schedule.
2. Select the **Day** and **Time** that data will be sent each week.   
   Timezone is based on project location.
3. Select the **Coverage** amount.  
   Coverage determines the number of upcoming weeks of schedule data to include within your email.
4. *Optional*: If you want to send the weekly project schedule immediately, click **Send Now**.

#### Resource Schedule E-mail

1. Use the toggle onicon to send weekly emails to specific users showing all upcoming schedule tasks on the resource schedule.
2. Choose the **Day** and **Time** data that will be sent each week.  
   Timezone is based on project location.
3. Select the **Coverage** amount.  
   Coverage determines the number of upcoming weeks of schedule data to include within your email.
4. *Optional*: If you want to send the Weekly Resource Schedule email immediately, click **Send Now**.

#### Lookahead Schedule E-mail

1. Use the toggle onicon to send weekly emails to specific users showing all upcoming schedule tasks on the lookahead schedule.
2. Choose the **Day** and **Time** data that will be sent each week.  
   *Note*: Timezone is based on project location.
3. *Optional*: If you want to send the Weekly Lookahead Email immediately, click **Send Now**.

### User Permissions

***Important!*** The following action requires 'Admin' permission to the project's Directory tool.

1. Click **User Permissions**.
2. Choose each user's permission for the Schedule tool from the **Permissions** menu.  
   *Note*: You cannot modify the permissions for users with a permission template applied.
3. Choose which resource the user is associated with from the **Resource** menu.
4. Select which, if any, weekly emails they will receive from the **Email Permissions** menu.   
   *Note*: Edit when and how often these emails are sent from the **Email Distribution** page.
5. For a list of what users can do at each permission level in the Schedule, see the Permissions Matrix.
6. Use the **table filter**and the **ellipsis**icon for table configuration and column adjustments.