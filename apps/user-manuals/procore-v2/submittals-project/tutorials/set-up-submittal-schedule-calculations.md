# Set Up Submittal Schedule Calculations

Source: https://v2.support.procore.com/product-manuals/submittals-project/tutorials/set-up-submittal-schedule-calculations

---

## Background

*Submittal Schedule Calculations* is an optional configuration feature that can be enabled for use with the Project level Submittals tool. When enabled on a Procore project, this option analyzes these key dates, which are entered by the creator under Submittal Schedule Information in a submittal package or a submittal item:

- Required On-Site Date
- Lead Time
- Design Team Review Time
- Internal Review Time

After analyzing the date entries, Procore automatically populates the calculated date values for the end user in the following fields:

- Planned Return Date
- Planned Internal Review Completed Date
- Planned Submit By Date

Based on the calculated date values above, Procore also suggests dates for the following fields:

- Submitter Due Date
- Approver Due Date

This helps the submittal creator ensure that submittal packages and items submitted to the review team are approved on schedule.

## Things to Consider

- **Required User Permissions**:

  - *To create a submittal that uses these calculations,* 'Standard' level permissions to the Submittals tool.
  - *To define the calculations used on the project*, 'Admin' level permissions to the Submittals tool.
- **Prerequisite**:

  - ***IMPORTANT! This feature must enabled in the Configure Settings page***. See [Enable Submittal Schedule Calculations](/product-manuals/submittals-project/tutorials/enable-submittal-schedule-calculations).
- **Additional Information**:

  - Schedule calculations do NOT automatically populate due dates in the submittal workflow.

## Steps

1. Follow the steps in [Create a Submittal](/product-manuals/submittals-project/tutorials/create-a-submittal).   
    This reveals the New Submittal page.
2. Scroll down to the **Submittal Schedule Information** area.
3. Set the following information:

   1. **Schedule Task.** The schedule task associated with the submittal being created. A schedule must be uploaded to the project first. See [Upload a Project Schedule File to Procore's Web Application](/product-manuals/schedule-project/tutorials/upload-a-project-schedule-file-to-procores-web-application).
   2. **Design Team Review Time**. The number of days allotted for the design team's review on the submittal.

      Design Team Review Time *Note*: If you enter 7, the system subtracts '7' calendar days from the **Planned Return Date** to automatically populate the date entry for the **Planned Internal Review Completed Date**.
   3. **Lead Time**. The expected number of calendar days that will be required for the material/services for the submittal to arrive.

      Lead Time*Note*: If you enter 10, the system subtracts '10' calendar days from the **Required On-Site Date** to automatically populate the date entry for the **Planned Return Date**.
   4. **Required On-Site Date**. The date by which materials related to the work detailed on the submittal must be delivered and available at the construction site.

      Required On-Site Date
   5. **Internal Review Time.** The number of calendar days that your project's design team requires to ensure the submittal is properly reviewed.

      Internal Review Time*N ote*: If you enter 5, the system subtracts '5' calendar days from the **Planned Internal Review Completed Date** to automatically populate the date entry for the **Planned Submit by Date**.

Example: