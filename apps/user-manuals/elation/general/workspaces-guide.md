# Workspaces Introduction (Premium)

Source: https://help.elationhealth.com/s/article/workspaces-guide

---

## **Contents**

- [What is the Workspaces feature?](#description)
- [Why is the Workspaces feature valuable?](#value)
- [How to start using Workspaces](#start)
- [Admins for Workspaces](#admin)
- [How to configure a Workspace](#configure)
 - [Creating a Workspace](#creating_a_workspace)
    - [Time Zone](#Time_Zone)
    - [User Access](#User_Access)
    - [People List](#People_List)
    - [Locations](#Locations)
    - [Print Headers](#Print_Headers)
    - [Lab Accounts](#Lab_Accounts)
    - [Fax Lines](#fax_lines)
    - [Templates](#Templates)
 - [Adding new users to a Workspace](#adding_users)
 - [Modifying a Workspace](#modifying_a_workspace)
 - [Removing users from a Workspace](#removing_users)
 - [Deleting a Workspace](#deleting_a_workspace)
- [What does the user see after being added to a Workspace?](#workspace_view)
 - [Switching between Workspaces](#switching_between_workspaces)
- [Recommended Use Cases for Workspaces](#recommended_use_cases)
- [Frequently Asked Questions (FAQ)](#faq)






## **What is the Workspaces feature?**

**Important Note**: The Workspaces feature is a product for Premium EHR customers only. If you are interested in upgrading to the Premium EHR subscription to use this feature, click the "I need help" button to notify Elation and a member of the Elation Team will reach out to assist you.


The Workspace feature allows a single Elation practice/organization to utilize a single Elation instance (login) to house specific teams and/or relevant resources across the organization. Customers within a single practice can add a flexible organizational layer (known as Workspaces in Elation) to the Elation ‘practice’ concept enabling them to deploy specific settings, resources, and configurations to different members of their organization based on different operational scenarios such as practice locations, clinical focus or role-specific responsibilities.

With the Workspaces feature, customers can create a Workspace and utilize Elation’s [User Group](https://help.elationemr.com/s/article/user-groups) functionality to segment users by designated operational scenarios. Afterwards you can specify which User Groups can access which Workspace and customize the following settings & resources for each Workspace:

- Settings
 - Time Zone
 - User Access
- Resources
 - People List
 - Practice Locations
 - Print Headers
 - Lab Accounts
 - Fax Lines
 - Templates
    - Physical Exam (PE)
    - Review of Systems (ROS)
    - Letter & Referral
    - Visit Note

## **Why is the Workspaces feature valuable?**

The Workspaces feature is valuable for practices that:

- have multiple practice locations (or time zones) where patients, clinical providers and staff are shared
- have various clinical focuses that involve different resources such as Lab Accounts and Templates
- have segmented responsibilities across different teams

With the Workspaces feature, each user is allocated the resources and configurations that are relevant to their day to day needs. As your organization continues to grow and scale, you can easily add new individuals to existing Workspaces and individuals can continue to keep their focus centered on the relevant needs for their role.

**Important Notes**:

- Providers will always have access to their Calendars
- Users will always have access to their preferred Print Header if one is selected




## **How to start using Workspaces**

The Workspaces feature is a product for Premium EHR customers only. If you are interested in upgrading to the Premium EHR subscription to use this feature, click the "I need help" button to notify Elation and a member of the Elation Team will reach out to assist you.

Once the Workspaces feature is enabled, the feature will be available for configuration for [Admin Level Users](https://help.elationemr.com/s/article/administrative-privileges) in the Elation Settings under “Workspaces”.

## **Admins for Workspaces**

Only [Admin Level Users](https://help.elationemr.com/s/article/administrative-privileges) in Elation can configure Workspaces and User Groups (another essential feature for Workspaces). Admin level users do not need to be a member of any Workspace in order to configure its settings and resources.



## **How to configure a Workspace**

Follow the instructions in the different sections below to configure your Workspace.

### **Creating a Workspace**

To create a Workspace, Admin level users can

1. Go to “Settings” -> “Workspaces”
2. Click the “+ Add Workspace” button
3. Enter a name for the “Workspace”
4. Click “Save”

Once a workspace has been created, you can configure the following settings & resources below.

#### **Time Zone**

Each Workspace can have its time stamps displayed based on one specific Time Zone. Select the Time Zone for a Workspace by clicking on the Time Zone dropdown. The selected time stamp displays on the Elation Calendar and on all records in the Workspace, such as visit notes, lab orders, provider letters, and more.

#### **User Access**

Each Workspace must be allocated towards specific members of the practice. The Workspace feature uses Elation’s existing User Group feature to allow you to separate specific members of your practices into groups and assign specific groups to specific Workspaces. Only members of the User Group(s) selected will see the allocated resources as assigned to that Workspace. To create additional User Groups, follow the instructions in [this article](https://help.elationemr.com/s/article/user-groups).

To add a User Group to a Workspace:

1. Click the “+ Add User Group” button
2. Search for and select the User Group(s) you want to add to the Workspace

**Important Note**: To add new users to an existing Workspace, all you have to do is add them to one of the User Groups that is already assigned to the Workspace.

#### **People List**

The People List resource uses Elation’s [User Group](https://help.elationemr.com/s/article/user-groups) feature to separate users into groups. The People List resource allows you to select which Provider Level Users will appear for selection when Workspace users view Provider Calendars and schedule appointments or select Provider Level Users in demographics or visit notes. The People List resource allows you to configure which User Groups and associated individual users (both Provider Level and Staff Level) would be available as contacts for Office Messages within the Workspace. By default, all Provider Level Users will appear in the Calendar, appointments, demographics, visit notes and Office Messages and all users will appear for Office Messages unless a User Group is selected.

- **Important Notes**:
 - Certain Workspace users may only have access to a Provider List setting in this section. This was the initial form of this feature when the Workspace feature was first created. The Provider List setting only controls which Provider Level Users appear in the Provider menu in the Calendar and in appointments. If you do not see the People List setting, click the "I need help" button to notify us and a member of the Support team will enable the People List setting for you.
 - Once the People List setting is enabled for you, please review your User Groups and People List settings to ensure the correct users appear for selection for Calendars, and appointments, demographics, visit notes and Office Messages.
    - If you are using [the newest Office Messages features](https://help.elationemr.com/s/article/Office-Message-Feature-Guide), it is especially important to make sure the correct users appear in your Workspace User Groups so that the appropriate recipients appear for selection when writing Office Messages.

To allocate specific users:

1. Click the “Only show 0 of…” option
2. Click the “+ Add User Group” button
3. Search for and select the User Group(s) you want to add to the People List resource

#### **Locations**

The Locations resource allows you to set which [Practice Locations](https://help.elationemr.com/s/article/adding-a-second-practice-location) will be visible within the Workspace. By default, all Practice Locations will be allocated to a Workspace.

To allocate specific Practice Locations:

1. Click the “Only show 0 of…” option
2. Click “ + Add Service Location”
3. Search for and select the Practice Location(s) you want to add to the Workspace

#### **Print Headers**

The Print Headers resource allows you to set which [Print Headers](https://help.elationemr.com/s/article/print-headers) are visible within the Workspace. If you have selected a default Print Header prior to being added to a Workspace, that default Print Header will appear for selection along with the Workspace allocated Print Headers. By default, all Print Headers are allocated to a Workspace.

To allocate specific Print Headers:

1. Click the “Only show 0 of…” option
2. Click “+ Print Headers”
3. Search for and select the Print Header(s) you want to add to the Workspace

**Important Note**: Users will always have access to their preferred Print Header if one is selected, even if the Print Header is not allocated to the Workspace they are in.





#### **Lab Accounts**

The Lab Accounts resource allows you to specify which [Lab Accounts](https://help.elationemr.com/s/article/labs-settings) can be selected when creating Lab Orders. By default, all Lab Accounts are allocated to a Workspace.

To allocate specific Lab Accounts:

1. Click the “Only show 0 of…” option
2. Click “+ Lab Account”
3. Search for and select the Lab Account(s) you want to add to the Workspace



**Fax Lines**

The Fax Lines resource allows you specify which Fax Inboxes (tied to fax lines) are allocated to a Workspace. By default, all Fax Inboxes are allocated to a Workspace. To allocate specific Fax Inboxes,

1. Click the “Only show 0 of…” option
2. Click “+ Fax Line”
3. Search for and select the Fax Line you want to add to the Workspace

#### **Templates**

You can allocate the following [templates](https://help.elationemr.com/s/article/templates-settings) to Workspaces:

- Letter & Referral
- Visit Note
- Physical Exam (PE)
- Review of Systems (ROS)

By default, all templates in each category are allocated to a Workspace. To allocate specific templates:

1. Click the “Only show:” option next to the category you want to limit
2. Click the “+ Add” button next to the template name to allocate it the Workspace




### **Adding new users to a Workspace**

To add new users to an existing Workspace, all you have to do is add them to one of the User Groups assigned to the Workspace. To add new users to a User Group:

1. Have an Admin level user go to “Settings” -> “User Groups”
2. Click the “edit” button next to the User Group
3. Search for the name of the new user & select their name from the dropdown to add them to the User Group
4. Click “Save” to save your changes

### **Modifying a Workspace**

**Important Note**: Take caution when modifying active Workspaces. If you make any adjustments to [resources](#description) within a Workspace,  the change will take effect the next time any user in the Workspace reloads the Practice Home, reloads a patient chart or prints any records.

To modify a Workspace:

1. Have an Admin level user go to “Settings” -> “Workspaces”
2. Click the “pencil” icon next to the name of the Workspace
   - Click the “X” button next to resources to remove them from the Workspace
   - Click the “+ Add” buttons to add resources to Workspaces

### **Removing users from a Workspace**

**Important Note**: Take caution when removing users from a Workspace, especially if the user is logged in to Elation. When you remove a user from a Workspace, the change will take effect the next time the user reloads the Practice Home, reloads a patient chart or prints any records.

To remove users from an existing Workspace, all you have to do is remove the user from the User Group they are in that is assigned to the Workspace or remove the entire User Group from the Workspace.

To remove users from a User Group:

1. Have an Admin level user go to “Settings” -> “User Groups”
2. Click the “edit” button next to the User Group
3. Click the “X” button next to the user’s name
4. Click “Save” to save your changes

To remove a User Group from a Workspace:

1. Have an Admin level user go to “Settings” -> “Workspaces”
2. Click the “pencil” icon next to the name of the Workspace
3. Go to the User Access resource setting
4. Click the “X” button next to the User Group you want to remove




### **Deleting a Workspace**

**Important Note**: Take caution when deleting a Workspace. When you remove a Workspace, the change will take effect the next time the user reloads the Practice Home, reloads a patient chart or prints any records.

To delete a Workspace

1. Have an Admin level user go to “Settings” -> “Workspaces”
2. Click the “delete” icon next to the name of the Workspace you want to delete
3. Click “Yes” once you are ready to delete the Workspace

## **What does the user see after being added to a Workspace?**

When a user is added to a workspace, they will immediately be brought into the Workspace, whenever they reload their Practice Home page or a Patient Chart, and will be able to see all Workspace specific settings & resources.

### **Switching between Workspaces**

If a user is in multiple Workspaces, they can click on the Workspace dropdown next to their email in the blue navigation bar at the top of Elation to switch between Workspaces.

- **Important Note**: The "Return to practice view" option allows users to see all resources within their EHR regardless of which Workspace(s) they belong to. The "Return to practice view" option is only available for [Admin Level Users](https://help.elationemr.com/s/article/administrative-privileges).




## **Recommended Use Cases for Workspaces**

The following article lists a few common use cases for Workspaces and guides you on how to set up your Workspaces based on the use case: [Workspaces Guide- Common Use Cases](Workspaces-Use-Cases.md)

## **Frequently Asked Questions (FAQ)**

#### **Will I see all patients after being added to a Workspace or only a subset of patients?**

Patients are not tied to the Workspaces feature. This means that all users in all Workspaces will see the entire patient panel.

#### **I am not seeing the correct resources in my Elation account after being added to a Workspace. What should I do?**

If you are not seeing the correct resources in your Elation account after being added to a Workspace, this usually means one of two things:

1. The correct resources were not allocated to the Workspace you are in. If you are an Admin for the Workspace (or you can ask the Admin for assistance), adjust the resources for the Workspace by following these steps:
   1. Go to “Settings” -> “Workspaces”
   2. Click the “pencil” icon next to the name of the Workspace
      - Click the “X” button next to resources to remove them from the Workspace
      - Click the “+ Add” buttons to add resources to Workspaces
2. You were added to the wrong Workspace. If you are an Admin (or you can ask the Admin for assistance), adjust the User Group(s) you belong to that is tied to the Workspace you should be in by following these steps:
   1. Go to “Settings” -> “User Groups”
   2. Click the “edit” button next to the User Group you do not belong to
   3. Click the “X” button next to your name to remove yourself from the User Group
   4. Click “Save” to save your changes
   5. Click the “edit” button next to the User Group you should belong to
   6. Search for your name and select your name from the dropdown to add yourself to the User Group
   7. Click “Save” to save your changes

#### **Will I be able to allocate other resources to Workspaces in the future (i.e. Rx Templates, Lab Order Sets, etc)?**

Yes, Elation plans to continuously add additional resources to Workspaces as we expand on the feature. Elation will notify you as additional settings or resources become available.

#### **I want my staff to have access to all items available within a resource. What is the difference between using "Allow all" versus select "Only show" and I select everything?**

When using "Allow all", any items added to the resource in the future will also automatically be shared with members of the Workspace.

If you choose "Only show", new items added to the resource in the future will not be shared with members of the Workspace.

## **Related Articles**

- [Workspaces Guide- Common Use Cases](Workspaces-Use-Cases.md)
- [User Accounts Guide- Administrative privileges](administrative-privileges.md)
- [User Groups Guide- Simplifying office messages & expanded calendar view](user-groups.md)
- [Print Headers Guide- Managing practice letterheads](print-headers.md)
- [Practice Locations Guide- Listing your service locations](adding-a-second-practice-location.md)
- [Labs Settings Guide](labs-settings.md)
- [Visit Note Templates Guide](elation-visit-note-templates.md)