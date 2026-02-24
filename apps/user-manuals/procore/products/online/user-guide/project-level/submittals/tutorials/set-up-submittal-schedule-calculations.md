# Set Up Submittal Schedule Calculations - Procore

Source: https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/set-up-submittal-schedule-calculations

---

## Objective

To set up and use submittal schedule calculations to automatically calculate date suggestions for approvers' responses.

## Background

**Submittal Schedule Calculations** is an optional configuration feature that can be enabled for use with the Project level Submittals tool.  When enabled on a Procore project, this option analyzes these key dates, which are entered by the creator under Submittal Schedule Information in a submittal package or a submittal item:

- Required On-Site Date
- Lead Time
- Design Team Review Time
- Internal Review Time

After analyzing the date entries, Procore automatically populates the calculated date values for the end user in the following fields:

- Planned Return Date
- Planned Internal Review Completed Date
- Planned Submit By Date

Based on the calculated date values above, Procore also suggests dates for the following fields:

- Submitter Due Date
- Approver Due Date

This helps the submittal creator ensure that submittal packages and items submitted to the review team are approved on schedule.

## Things to Consider

- **Required User Permissions**:
  - *To create a submittal that uses these calculations,* 'Standard' level permissions to the Submittals tool.
  - *To define the calculations used on the project*, 'Admin' level permissions to the Submittals tool.
- **Prerequisite**:
  - ***IMPORTANT! This feature must enabled in the Configure Settings page***. See [Enable Submittal Schedule Calculations](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/enable-submittal-schedule-calculations "Enable Submittal Schedule Calculations").
- **Additional Information**:
  - Schedule calculations do NOT automatically populate due dates in the submittal workflow.

## Steps

1. Follow the steps in [Create a Submittal](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/create-a-submittal "Create a Submittal").   
   This reveals the New Submittal page.
2. Scroll down to the **Submittal Schedule Information** area.
3. Set the following information:
   1. **Schedule Task.**The schedule task associated with the submittal being created. A schedule must be uploaded to the project first. See [Upload a Project Schedule File to Procore's Web Application](https://support.procore.com/products/online/user-guide/project-level/schedule/tutorials/upload-a-project-schedule-file-to-procores-web-application "Upload a Project Schedule File to Procore's Web Application").
   2. **Design Team Review Time**. The number of days allotted for the design team's review on the submittal.

      *Note*: If you enter 7, the system subtracts '7' calendar days from the **Planned Return Date** to automatically populate the date entry for the **Planned Internal Review Completed Date**.
   3. **Lead Time**. The expected number of calendar days that will be required for the material/services for the submittal to arrive.

      *Note*: If you enter 10, the system subtracts '10' calendar days from the **Required On-Site Date** to automatically populate the date entry for the **Planned Return Date**.
   4. **Required On-Site Date**. The date by which materials related to the work detailed on the submittal must be delivered and available at the construction site.
   5. **Internal Review Time.**The number of calendar days that your project's design team requires to ensure the submittal is properly reviewed.

      *Note*: If you enter 5, the system subtracts '5' calendar days from the **Planned Internal Review Completed Date** to automatically populate the date entry for the **Planned Submit by Date**.  
      This illustration shows you an example of these entries and calculations.  
        
      ![create-submittal-schedule-info.png](https://support.procore.com/@api/deki/files/338157/create-submittal-schedule-info.png?revision=1&size=bestfit&width=729&height=444)

## See Also

- [Create a Submittal](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/create-a-submittal "Create a Submittal")
- [Enable Submittal Schedule Calculations](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/enable-submittal-schedule-calculations "Enable Submittal Schedule Calculations")

## 

If you would like to learn more about Procore's submittals management software and how it can help your business, please visit our [construction submittals software product page ![icon-external-link.png](https://support.procore.com/@api/deki/files/186764/icon-external-link.png?revision=2&size=bestfit&width=14&height=14)](https://www.procore.com/project-management/submittals "https://www.procore.com/project-management/submittals").