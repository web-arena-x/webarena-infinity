# Configure Advanced Settings: Project Level Timesheets

Source: https://v2.support.procore.com/product-manuals/timesheets-project/tutorials/configure-advanced-settings-project-level-timesheets

---

## Background

When you set up your timesheet settings, you can choose how employees track their time.

Additionally, you can choose to track your employees' field location when they clock in and out using a *geofence,* a virtual boundary you can set up around your job site. Users can be prompted to clock in or clock out when entering or exiting a geofence.

## Things to Consider

- [Required User Permissions](/product-manuals/timesheets-project/permissions)
- In the Company Admin tool, you can configure what fields are [required, optional, or hidden](/faq-which-fields-in-the-timesheets-tool-can-be-configured-as-required-optional-or-hidden) on a project. See [Create New Configurable Fieldsets](/product-manuals/admin-company/tutorials/create-new-configurable-fieldsets).
- Changes to a project's 'Time Entry Settings' only apply to new timesheets, not existing ones.

## Prerequisites

- Add the Timesheets tool to the project. See [Add and Remove Project Tools](/product-manuals/admin-project/tutorials/add-and-remove-project-tools).
- To enable employee location tracking, the address must be set for the 'Project Location' in the Project level Admin tool. See [Update General Project Information](/product-manuals/admin-project/tutorials/update-general-project-information).

## Steps

1. Navigate to the project's **Timesheets** tool.
2. Click the **Configure Settings**  icon.
3. Select the Time Entry Settings for the project.

   1. Select the format for **Time Entry** on timecards:

      - **Total Hours** allows users to enter the total number of hours worked.
      - **Start Time and Stop Time** allows users to enter the exact hour and minute that they started and stopped work, and account for lunch times.

        1. Select the default start and stop times that display on timecards.
   2. Mark whether 'Employees Can Select Non-Budgeted Items' when filling entering their time in Timesheets or My Time.

      - Move the toggle to the **ON**  position to allow employees to track time to non-budgeted items.
      - Move the toggle to the **OFF**  position to require employees track time only to budgeted items.
   3. Mark what overtime rules to apply to timecards.
4. Select the Lunch Tracking Settings for the project.

   1. Select the format for Lunch Tracking on timecards:

      - **Total Time** tracks the total number of minutes a break was taken.
      - **Start and Stop Time** tracks the exact times that a person took their break.
      - **None** does not track breaks in Timesheets.
   2. If tracking lunch breaks, select the default lunch time to display on timecards.
5. Select the Employee Location Tracking Settings for the project.

   1. Move the toggle to the **ON**  position to **Enable Employee Location Tracking**.
   2. Set the **Geofence Distance** from the project's address by clicking and moving the slider to the desired geofence perimeter.
6. Click **Update**.