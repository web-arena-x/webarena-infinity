# Configure Notification Profiles for Resource Planning

Source: https://v2.support.procore.com/product-manuals/resource-planning-company/tutorials/configure-notification-profiles-for-resource-planning

---

## Background

Automatic notifications can be sent to users in Resource Planning when information changes about project, people, assignments, or requests. To configure what notifications are sent, you first configure notification profiles, and then assign those profiles to users in the People tool. See [Edit People in Resource Planning](/product-manuals/resource-planning-company/tutorials/edit-people-information-for-resource-planning).

## Things to Consider

- [Required User](/product-manuals/resource-planning-company/permissions) [Permissions](/product-manuals/resource-planning-company/permissions)
- People can only be assigned one notification profile at a time.
- You can create an unlimited number of notification profiles.
- Only people who are 'Users' or 'Both' can receive notifications.
- Users cannot respond to notifications. See [What messages and alerts can people respond to in Resource Planning?](/faq-what-messages-and-alerts-can-people-respond-to-in-resource-planning)
- Notifications about people and projects are sent at the time those changes occur.
- Notifications about resource assignments and requests are sent based on their configured 'Notification Thresholds'.
- Notifications can be viewed on the Resource Planning homepage, by email, or in the Resource Planning/LaborChart mobile app. See [What is the Resource Planning/LaborChart App?](/faq-what-is-the-laborchart-app)

## Steps

1. Navigate to the Company level **Resource Planning** tool.
2. Click the **Configure Settings**  icon.
3. Select **Notification Profiles**.
4. Click **New.**
5. Enter the **Name** of the notification profile.
6. Select the notifications users will receive when they are assigned this notification profile:

   - **People in User's Groups.** To send notifications to members of the user's groups for the following actions, move the toggle to the **ON** position:

     - **Person Created / Deleted.** Send notifications when a new person is created or deleted.
     - **Person's Groups Changed.** Send notifications when a person's group changes.
     - **Person's Status Changed.** Send notifications when a person's status changes.
     - **Applied Tag Warning.** Send notifications when a person's tag is within the warning range of expiring. See [Configure Tags for Resource Planning](/product-manuals/resource-planning-company/tutorials/configure-tags-for-resource-planning).
     - **Applied Tag Expiring.** Send notifications the day that a person's tag expires. See [Manage Resource Planning Tags for People](/product-manuals/resource-planning-company/tutorials/add-or-edit-tags-for-people-in-resource-planning).
   - **Projects in User's Groups.** To send notifications when the following actions are taken on a project in the user's groups, move the toggle to the **ON** position:

     - **Project Created / Deleted.** Send notifications when a project is created or deleted.
     - **Project's Groups Changed.** Send notifications when a project's group changes.
     - **Project's Status Changed.** Send notifications when a project's status changes.
     - **Selected as Project Role.** Send notifications to the User when they are added as a project role on a project. See [Assign Project Roles for Resource Planning](/product-manuals/resource-planning-company/tutorials/assign-project-roles-for-resource-planning).
   - **Assignments.** For the following actions, mark the scope of the action that would trigger the notification.

     - **Assignment Created.**  
       *Note:* Notifications for this action are not sent to the assignment's creator.

       - **None**. Notifications are not sent for this action.
       - **User's Projects**. Send notifications when assignments are created in Projects where the user is assigned or has a Project Role.
       - **User's Groups**. Send notifications when assignments are created in groups the user belongs to.
     - **Assignment Edited.**

       - **None**. Notifications are not sent for this action.
       - **User Created/Edited**. Send notifications to users when assignments they created or edited are edited.
       - **User's Projects**. Send notifications when assignments are edited in Projects where the user is assigned or has a Project Role.
       - **User's Groups**. Send notifications when assignments are edited in groups the user belong to.
     - **Assignment Deleted.**

       - **None**. Notifications are not sent for this action.
       - **User Created/Edited**. Send notifications to users when assignments they created or edited are deleted.
       - **User's Projects**. Send notifications when assignments are deleted in Projects where the user is assigned or has a Project Role.
       - **User's Groups**. Send notifications when assignments are deleted in groups the user belong to.
     - **Assignment Starting.**

       - **None**. Notifications are not sent for this action.
       - **User Created/Edited**. Send notifications to users when assignments they created or edited are starting.
       - **User's Projects**. Send notifications when assignments are starting in Projects where the user is assigned or has a Project Role.
       - **User's Groups**. Send notifications when assignments are starting in groups the user belong to.
     - **Assignment Ending.**

       - **None**. Notifications are not sent for this action.
       - **User Created/Edited**. Send notifications to users when assignments they created or edited are ending.
       - **User's Projects**. Send notifications when assignments are ending in Projects where the user is assigned or has a Project Role.
       - **User's Groups**. Send notifications when assignments are ending in groups the user belong to.
   - **Requests.** For the following actions, mark the scope of the action that would trigger the notification.

     - **Request Created.**  
       *Note:* Notifications for this action are not sent to the request's creator.

       - **None**. Notifications are not sent for this action.
       - **User's Projects**. Send notifications when requests are created in Projects where the user is assigned or has a Project Role.
       - **User's Groups**. Send notifications when requests are created in groups the user belongs to.
     - **Request Edited.**

       - **None**. Notifications are not sent for this action.
       - **User Created/Edited**. Send notifications to users when requests they created or edited are edited.
       - **User's Projects**. Send notifications when requests are edited in Projects where the user is assigned or has a Project Role.
       - **User's Groups**. Send notifications when requests are edited in groups the user belong to.
     - **Request Filled.**

       - **None**. Notifications are not sent for this action.
       - **User Created/Edited**. Send notifications to users when requests they created or edited are filled.
       - **User's Projects**. Send notifications when requests are filled in Projects where the user is assigned or has a Project Role.
       - **User's Groups**. Send notifications when requests are filled in groups the user belong to.
     - **Request Deleted.**

       - **None**. Notifications are not sent for this action.
       - **User Created/Edited**. Send notifications to users when requests they created or edited are deleted.
       - **User's Projects**. Send notifications when requests are deleted in Projects where the user is assigned or has a Project Role.
       - **User's Groups**. Send notifications when requests are deleted in groups the user belong to.
     - **Request Starting.**

       - **None**. Notifications are not sent for this action.
       - **User Created/Edited**. Send notifications to users when requests they created or edited are starting.
       - **User's Projects**. Send notifications when requests are starting in Projects where the user is assigned or has a Project Role.
       - **User's Groups**. Send notifications when requests are starting in groups the user belong to.
     - **Request Ending.**

       - **None**. Notifications are not sent for this action.
       - **User Created/Edited**. Send notifications to users when requests they created or edited are ending.
       - **User's Projects**. Send notifications when requests are ending in Projects where the user is assigned or has a Project Role.
       - **User's Groups**. Send notifications when requests are ending in groups the user belong to.
7. Click **Save**.
8. *Optional:* Set Notification Thresholds. Notification thresholds dictate when notifications are sent based on assignment and request dates.

   - **Assignments.** Enter a number in one of these fields to:

     - Enter the number of **Days Before the Start** date for the notification to be sent.
     - Enter the number of **Days Before the End** date for the notification to be sent.
   - **Requests.**

     - Enter the number of **Days Before the Start** date for the notification to be sent.
     - Enter the number of **Days Before the End** date for the notification to be sent.
9. Click **Save**.

## Next Steps

- Assign or Edit a User's Notification Profile. See [Edit People in Resource Planning](/product-manuals/resource-planning-company/tutorials/edit-people-information-for-resource-planning)
- [View Notifications in Resource Planning](/product-manuals/resource-planning-company/tutorials/view-notifications-in-resource-planning)