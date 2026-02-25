# Configure Integration Settings for Resource Planning

Source: https://v2.support.procore.com/product-manuals/resource-planning-company/tutorials/configure-integration-settings-for-resource-planning

---

## Background

Some customers choose to integrate Resource Planning with an existing system of record, where they create and manage construction projects. If your company has an integration, you can manage that data externally so that your projects stay in sync between the two systems.

If you have a new start date for your project, the Shift Project feature automatically updates the dates of any associated assignments and requests, shifting them in the same direction and for the same duration as the new start date. See [Shift Project Dates](/product-manuals/resource-planning-company/tutorials/shift-project-dates).

When Shift Project is enabled for your integration, associated assignments and requests are shifted in Resource Planning if the start date of the project is updated in your system of record. If Shift Project is disabled, you need to manually update all requests and assignment dates according to the new start date.

##### Â Note

If you have an integration, you can also shift projects if your integration ignores the 'Start Date' field, or if the project was created in Resource Planning instead of your system of record. In both of these cases, you can ignore this toggle as Shift Project is automatically enabled.

## Things to Consider

- [Required User](/product-manuals/resource-planning-company/permissions) [Permissions](/product-manuals/resource-planning-company/permissions)

## Steps

1. Navigate to the Company level **Resource Planning** tool.
2. Click the **Configure Settings**  icon.
3. Click **Integration Settings.**
4. Move the **toggles**  ON or  OFF to enable and disable functionality.

   - **Shift Project.** When enabled, assignments and requests can be shifted when a future project date changes. See [Shift Project Dates](/product-manuals/resource-planning-company/tutorials/shift-project-dates).
   - **End Assignments for Inactive Users.** When enabled, any current assignments for an inactive user are truncated to the date that the user was marked as inactive. All future assignments for that user are canceled.