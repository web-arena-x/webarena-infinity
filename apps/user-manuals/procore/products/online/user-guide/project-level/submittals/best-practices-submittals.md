# Best Practices: Submittals - Procore

Source: https://support.procore.com/products/online/user-guide/project-level/submittals/best-practices-submittals

---

Table of Contents

**Table of Contents**

- [Overview](https://support.procore.com/#)
- [Company Level Settings](https://support.procore.com/#)
- [Project Configurations](https://support.procore.com/#)
- [Imports](https://support.procore.com/#)
- [Submittal Builder](https://support.procore.com/#)
- Submittal Packages 
 - [Overview](https://support.procore.com/#)
 - [Itemization](https://support.procore.com/#)
 - [Creation and Review](https://support.procore.com/#)
 - [Distribution and Revision](https://support.procore.com/#)
- [Workflow Management](https://support.procore.com/#)

## Overview

| | |
| --- | --- |
| submittals-illustration.jpg | Introducing Procore's best practices guides for the project's Submittals tool! In these guides, you will find our general recommendations for utilizing Procore's functionality to its greatest extent and maximizing your company's insights and productivity. These best practices guides are intended to explain the benefits of implementing certain features and are supplemented by Support Center tutorials that provide step-by-step instructions for performing the related actions. While the recommendations in these guides are generic and may not match your company's existing processes exactly, we encourage you to take a look and see what suggestions you can consider adopting |

## Company Level Settings

##### Note

This page describes recommended best practices for setting up the project's Submittals tool. Click [here](https://support.procore.com/products/online/user-guide/project-level/submittals "Submittals") to view tutorials, videos, and more about the project's Submittals tool.

## Introduction

Before your team starts creating submittals, you will want to make sure that you have all of your company level configurations in place. This will help prevent problems and re-work later on. Are you ready?

### Why should I do this now?

You should define these configurations now to standardize the data entered by your project teams from the start. This will help save you from needing to edit existing submittals to change or add missing information later. Although you can edit submittals in bulk, you can only bulk edit specific fields in a single project.

## Custom Submittal Types

With Procore's Submittals tool, you can route any type of document that might require an approval workflow on your project. Submittal Types allow you to organize those documents by creating separate categories of submittals. See [Create Custom Submittal Types](https://support.procore.com/products/online/user-guide/company-level/admin/tutorials/create-custom-submittal-types "Create Custom Submittal Types"). Your project team can filter and report on submittals based on their type to easily find the data they need.

### Best Practice

We encourage you to create additional types for your project teams to use. Here are some popular types that we recommend:

| | |
| --- | --- |
| - Attic Stock/Extra Material - Concrete Mix Design - Construction Schedule - Control Plan - Coordination Drawing - Design Calculations - Installation Instructions - Mill Certificate - Safety Data Sheet (SDS) - Operation & Maintenance Manuals (O&Ms) - Other | - Procedures/SOP - Product Data - Product Warranty - Qualifications/Certifications - Record Document - Record Drawing - Sample - Shop Drawing - Tests & Inspections - Training Verification - Workmanship Warranty |

### Why should I do this now?

Custom submittal types allow you to organize your submittals more efficiently. You should create custom submittal types at the beginning of your project so that your project team can use them as soon as they start creating submittals. Best practice is to create separate submittals for each type as needed instead of combining submittals together under one type that isn't applicable to all of the items. This helps ensure that you are meeting your project's submittal requirements and makes it easier for your project teams to find specific submittal information quickly.

Custom submittals types allow you to define the categories and naming conventions based on your company's preferences. Since different design teams might use different terminology, we recommend defining these early so that you don't end up with multiple versions of "Product Information", for example.

### Additional Considerations: Submittal Builder

If you are planning to use [Submittal Builder](https://support.procore.com/products/online/user-guide/project-level/specifications/tutorials/generate-submittal-log "Generate Submittals from Specifications (Submittal Builder)") to create your submittal registry from specifications, the submittal type only automatically populates if there is an exact match for the type in your Procore account. Plurals are considered an exact match. For example, "Shop Drawing" matches with "Shop Drawings." If an exact match is not found, Submittal Builder selects "Other" as the submittal type. If you add custom submittal types *after* using Submittal Builder, you must manually update any existing submittals with the new types if necessary.

See [Best Practices: Submittal Builder](#s187102 "Best Practices: Submittal Builder") for more considerations and recommendations.

## Custom Submittal Statuses

Procore provides 3 default statuses for submittals: Open, Closed, and Draft. However, you might want to add more statuses to show exactly where a submittal is in its submission and approval process.

An "Open" submittal can be:

- A submittal that has been requested, but not yet received
- A submittal that has been received and is being reviewed( either internally or externally)

A "Closed" submittal can be:

- A submittal that has been approved, with or without exceptions
- A submittal that has been rejected or marked as "Revise & Resubmit"

### Best Practice

We recommend adding custom submittal statuses to fit with your company's processes. See [Create Custom Submittal Log Statuses](https://support.procore.com/products/online/user-guide/company-level/admin/tutorials/create-custom-submittal-log-statuses "Create Custom Submittal Log Statuses"). Here are some common recommendations:

- **Awaiting Submission** (considered 'Open')
- **Pending Review** (considered 'Open')
- **Approved / No Exceptions** (considered 'Closed')
- **Approved w/ Comments / Exceptions Taken** (considered 'Closed')
- **Revise & Resubmit** (considered 'Closed')
- **Rejected** (considered 'Closed')
- **Void** (considered 'Closed')
- **For Record Only** (considered 'Closed')

### Why should I do this now?

You should add custom submittal statuses at the beginning of a project so that the options are available for the project teams to use right away. With clear statuses, teams can see if a submittal is at risk of being delayed and confirm whether its the most current and approved version. Without custom statuses like "Approved / No Exceptions" or "Rejected", it could be difficult for users to find the final version of a submittal if all of its revisions had "Closed" as their status.

## Configurable Fieldsets

Use Configurable Fieldsets to help make sure that your project team only sees and completes the fields that are applicable to your company's processes. See [Create New Configurable Fieldsets](https://support.procore.com/products/online/user-guide/company-level/admin/tutorials/create-new-configurable-fieldsets "Create New Configurable Fieldsets").

### Why should I do this now?

You should define your project's Submittals fieldset at the beginning of your project to simplify your submittal process and make sure your teams enter the correct information in Procore according to your business needs from the start. This increases the adoption of Procore and limits the need to manually edit submittals later on. Although you can edit more than one submittal at a time, you can only bulk edit certain fields in a single project.

## Custom Fields

Custom Fields allow your teams to capture data unique to your company and/or project. See [Create New Custom Fields](https://support.procore.com/products/online/user-guide/company-level/admin/tutorials/create-new-custom-fields "Create New Custom Fields").

### Why should I do this now?

Much like fieldsets, defining custom fields at the beginning of a project helps ensure that project teams are capturing the data important to your business processes. Although custom fields can be added at any point during a project, Procore does not support adding data to custom fields in bulk for existing submittals.

### Common Examples

Custom Fields

- **LEED Submittal?** (using the 'Checkbox' custom field type)
- **Priority** (using the 'Multi Select' custom field type)

## Project Configurations

##### Note

This page describes recommended best practices for setting up submittal configurations. Click [here](https://support.procore.com/products/online/user-guide/project-level/submittals "Submittals") to view tutorials, videos, and more about the project's Submittals tool.

## Introduction

In order to get the most out of the Submittals tool, you will want to make sure that you have all of your project-level configurations in place before creating submittals. This article will go over the best practices for the most notable settings. Are you ready?

### Why should I do this now?

Enabling certain configurations provides additional functionality to help ensure your submittals are processed as efficiently as possible.

##### Tip

If you want to set these configurations as default for all new projects, most of these settings will carry over in a project template. See [What is a Project Template?](https://support.procore.com/faq/what-is-a-project-template "What is a Project Template?") and [What gets copied over to a new project when applying a project template?](https://support.procore.com/faq/what-gets-copied-over-to-a-new-project-when-applying-a-project-template "What gets copied over to a new project when applying a project template?")

## Number Submittals by Spec Section

This setting enables an option to prefix the submittal number and revision with the linked spec section. For example, if a spec section #03 30 00 is identified in the Specification Section field of a submittal, then the submittal number (such as #007) and revision number (such as #01) will be formatted as #03 30 00-007.01 when the setting is enabled. If the setting is not enabled, the submittal number and revision number will be formatted as #007.01.

Also, submittals in each spec section will be numbered sequentially and independently from submittals in another spec section when this setting is enabled. For example:

- Spec Section: 03 30 00
 - #03 30 00-001: Concrete Mix Design
 - #03 30 00-002: Product Data
 - #03 30 00-003: Expansion Joint Layout
- Spec Section: 07 45 00
 - #07 45 00-001: Product Data
 - #07 45 00-002: Samples

### Considerations

After this setting is enabled and submittals are created, we do not recommend disabling the setting. Doing so will likely cause duplicate submittal numbers.

## Dynamic Due Dates

Dynamic Due Dates are an optional but recommended configuration that defines workflow step durations instead of fixed due dates. This ensures each workflow step and role has its contractually obligated time frame to review and respond to each submittal item. As workflow steps are completed, the next step's due date automatically adjusts forward (if the previous step was late) or backward (if the previous step was early) to always comply with the defined durations. Overdue rules still apply if the workflow steps do not respond by their due date. See [What are dynamic approver due dates?](https://support.procore.com/faq/what-are-dynamic-approver-due-dates "What are dynamic approver due dates?")

### Considerations

- We recommend enabling the 'Dynamic Approver Due Dates' configuration before creating and using submittal workflow templates.
- Submittals workflow due dates comply with the project's Working Days settings. See [Set Project Working Days](https://support.procore.com/products/online/user-guide/project-level/admin/tutorials/set-project-working-days "Set Project Working Days").
- Overdue submittal email reminders will not be sent once the submittal is 45 days past due.

## Submittal Schedule Calculations

Submittal schedule calculations are an optional but highly recommended feature that displays relevant milestone dates for a submittal item. These fields consist of the following:

- **Required On-Site Date:** A user entry field for the date the submittal is to be installed or used on-site.
- **Lead Time:** A user entry field for the number of calendar days the submittal requires for processing, manufacturing, and shipping.
- **Design Team Review Time:** A user entry field for the calendar days allocated for external teams to review and approve the submittal.
- **Internal Review Time:** A user entry field for the calendar days allocated for internal teams to review the submittal.
- **Planned Return Date:** A system-generated field to display the milestone date of when you require an approved submittal from your external reviewers to meet the Required On-site date milestone, also commonly known as the "drop dead date."
 - The calculation used to determine this is: Required On-site Date - Lead Time
- **Planned Internal Review Completed Date:** A system-generated field to display the milestone date of when you require a reviewed submittal from your internal reviewers to meet the Required On-site date milestone.
 - The calculation used to determine this is: Required On-site Date - Lead Time - Design Team Review Time
- **Planned Submit By Date:** A system-generated field to display the milestone date of when you require a submittal to be submitted from your Submitter role to meet the Required On-site date milestone.
 - The calculation used to determine this is: Required On-site Date - Lead Time - Design Team Review Time - Internal Review Time

These fields support the ability to back-calculate planned due dates for each member of  the workflow process based on specific required on-site dates, lead times, and allotted review times. This setting makes it easier to report on the progress of a submittal to determine if it's on track.

When the 'Submittal Schedule Calculations' option is turned ON:

- First enter a date in the **Required On-Site Date** field.
- Next, enter the days in the **Lead Time** field. For example, if you enter **10** days, the system will automatically add the **Planned Return Date** by subtracting the 10-day lead time from the **Required On-Site Date**.
- The same is true for dates entered in the **Design Team Review Time** field. For example, if you enter **7** days, the system subtracts 7 days from the **Planned Return Date** to calculate the automatic entry for the **Planned Internal Review Completed Date**.
- Finally, enter the days in the **Internal Review Time** field. For example, if you enter **5** days, the system will subtract 5 days from the **Internal Review Time** date to automatically calculate the **Planned Submit By Date**.

### Considerations

- These fields are purely for reference only. They do not impact or sync with other fields, including workflow due dates.
- To avoid confusion and eliminate duplicate data, consider hiding the standard ‘Submit By’ date field in the Submittal tool fieldset. See [Which fields in the Submittals tool can be configured as required, optional, or hidden?](https://support.procore.com/faq/which-fields-in-the-submittals-tool-can-be-configured-as-required-optional-or-hidden "Which fields in the Submittals tool can be configured as required, optional, or hidden?")
- These calculations assume a perfect scenario with no submittal revisions. Be sure to consider the number of potential revisions when determining the actual workflow due dates.

### Why should I enable Submittal Schedule Calculations?

Displaying this information allows you to add and reference these important dates when building your workflow to ensure that your submittal is approved by the required on-site date. See [Enable Submittal Schedule Calculations](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/enable-submittal-schedule-calculations "Enable Submittal Schedule Calculations") and [Set Up Submittal Schedule Calculations](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/set-up-submittal-schedule-calculations "Set Up Submittal Schedule Calculations").

## Enable Reject Workflows

This setting is highly recommended. When enabled, submittal responses of either 'Reject' or 'Revise and Resubmit' from a workflow approver automatically route the Ball in Court to the Submittal Manager to determine the next step.

- The Submittal Manager will be notified by email that they are now the Ball in Court user due to a 'Reject' or 'Revise and Resubmit' response. When the Ball in Court is routed to the Submittal Manager, they can choose to:
 - Close the submittal, and create a revision if desired.
 - Return the Ball in Court to the previous step in the workflow.
 - Resume the workflow.
    - When a workflow is resumed, it will pick up where it left off. For example:
      - If the 'Reject' or 'Revise and Resubmit' response was entered on a step with no other approvers, the workflow moves to the next step. If there is no next step, the workflow completes.
      - If the 'Reject' or 'Revise and Resubmit' response was entered on a step with with more required approvers who haven't responded yet, the workflow will resume at the same step so the other required approvers can respond.

### Considerations

- This feature also applies to any custom responses mapped to 'Reject' or 'Revise and Resubmit' response types.
- When the Submittal Manager chooses to set the Ball in Court back to a previous workflow step, none of the step's information (Attachments, Response, Comments Sent/Returned Dates) is removed. These items can be edited, but the original information is not stored within the submittal. The edit actions will be recorded in the change history, but are not reportable in reporting tools.  If maintaining the historical data is important to you, we recommend closing and distributing the submittal and creating a new revision instead of returning Ball in Court to a previous step.

### Why should I enable Reject Workflow?

This setting simplifies workflows and eliminates unnecessary revisions. For interactions between the Submitter and Approver, it provides an opportunity for the Submittal Manager to address an incorrect submission from the Submitter before it can advance to the next Approver.

For workflows with multiple Approver steps, it eliminates the need to insert an extra step dedicated to the Submittal Manager between Approver steps to ensure that a 'Reject' or 'Revise and Resubmit' response does not advance to the next step.

## Submittal Emails

These settings regulate which Submittal roles will be copied on email notifications resulting from a specific submittal action. These notifications can be configured as needed to change the number of notifications being sent. See [Who receives an email when a submittal is created or updated?](https://support.procore.com/faq/who-receives-an-email-when-a-submittal-is-created-or-updated "Who receives an email when a submittal is created or updated?")

##### Important

These settings do not control any 'Action Required' emails sent to Ball-in-Court users.

## Defining Submitter, Approver, and Reviewer Roles

These roles identify the specific actions required of the Assignee on a submittal item. The roles and their specific actions include:

- **Submitter:** As an optional but recommended first step in the workflow, the submitter role is responsible for submitting the requested documentation. Multiple users can be added to the "Submitter" role, but there can only be one Submitter step in a workflow.
- **Approver:** These users are responsible for responding to the submittal item. The response options can be configured within the project's Submittals tool configurations. See [Manage Custom Submittal Responses](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/manage-custom-submittal-responses "Manage Custom Submittal Responses").
- **Reviewer:** This role is commonly used to provide the Approver role flexibility to send an item for review to another user not previously added to the same workflow step. An Approver can only do this when the item is in their ball-in-court. Once the item is forwarded to them, the Reviewer can take similar response actions as an Approver. The ball-in-court returns back to the Approver for their final response. See [Forward a Submittal for Review](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/forward-a-submittal-for-review "Forward a Submittal for Review").

##### Note

To effectively build submittal workflows, ensure the submitters, approvers, and reviewers have all been added to the project's directory. See [Add a User Account to the Project Directory](https://support.procore.com/products/online/user-guide/project-level/directory/tutorials/add-user-account-to-project-directory "Add a User Account to the Project Directory").

See [Submittals - Workflow Diagrams](https://support.procore.com/products/online/user-guide/project-level/submittals/workflow "Submittals - Workflow Diagrams") for a visual of how these roles work together in a submittal's lifecycle.

## Submittal Responses

These settings allow you to customize the responses that can be used by Reviewers and Approvers. For example, you can add "Reviewed" as your project’s preferred response instead of "Approved". Submittal Admins can create up to 12 custom responses for each default response, except for "Pending" and "Submitted" which each allow one custom response. Custom responses cannot be deleted if they are being used on a submittal. They can be edited, but note that the edited response will replace the previous response in all of the places the previous response was used. See [Manage Custom Submittal Responses](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/manage-custom-submittal-responses "Manage Custom Submittal Responses").

## Workflow Templates

Throughout the course of a project, teams constantly reuse the same workflow across multiple Submittals. Teams need to be able to define these workflows as templates and apply them when necessary, rather than having to recreate the same workflow for multiple submittals manually. If a Project Engineer is going to build the same workflow across 10 different items, that is a lot of extra time spent performing a repetitive action. With this feature, templates can be created and reused as needed.

### Considerations

- Since submittal workflow steps are assigned to specific users, and no step can be “unassigned”, it is likely that you will create new templates as you buy out scopes of work.
- If you prefer to avoid creating multiple workflow templates for each unique routing, you can create partial workflow templates containing only core workflow roles. Once workflow templates are applied, the remaining steps can be added, and any existing ones can be modified. We typically suggest building workflow templates with no Submitter role, so you don't need to create a template for each Responsible Contractor. This works especially well if all submittal workflows are otherwise the same.
- Once a submittal’s workflow is complete, the ball-in-court automatically returns back to the Submittal Manager. However, no due date is associated with this ball-in-court, and no overdue notifications are sent. If you prefer to ensure the Submittal Manager distributes the submittal according to a due date, add that user as a final step to the workflow.

### Why should I create workflow templates?

Creating workflow templates saves you time and ensures the required teams are reviewing the submittal items in the proper order. See [Manage Submittal Workflow Templates](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/manage-submittal-workflow-templates "Manage Submittal Workflow Templates").

## Next Steps

Now that your project's submittal configurations are in place, you can start creating submittals. The fastest methods to create a submittal registry are using Procore's Submittal Builder or Submittal Imports. See [Best Practices: Submittal Builder](#s187102 "Best Practices: Submittal Builder") and [Best Practices: Submittal Imports](#s197287 "Best Practices: Submittal Imports") for more information and recommendations for using these methods.

## Imports

##### Note

This page describes recommended best practices for importing submittals to Procore. Click [here](https://support.procore.com/products/online/user-guide/project-level/submittals "Submittals") to view tutorials, videos, and more about the project's Submittals tool.

## Introduction

Submittal Imports is the most efficient method to bulk generate a submittal registry with detailed data for your project’s submittals and packages. This guide will show you the best practices to help you maximize efficiency when using Submittal Imports. Are you ready?

### Why should I use Submittal Imports?

You can add many details to the submittal items at the creation time by utilizing an XLSX or CSV spreadsheet and the Procore Imports application. Duplicating data across multiple items is much more efficient to do within a spreadsheet compared to adding the data individually for each submittal item.

##### Tip

Submittal Imports are done using Procore Imports, which is only available for computers running Windows 10 or higher. See [Import Submittals into your Project Level Submittals Tool (Procore Imports)](https://support.procore.com/products/procore-imports/submittals/tutorials/import-submittals-into-your-project-level-submittals-tool-procore-imports "Import Submittals into your Project Level Submittals Tool (Procore Imports)"). For Mac users, our Customer Support team is available to assist with these imports. See [Send a Completed Submittals Import Template to Procore](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/send-a-completed-submittals-import-template-to-procore "Send a Completed Submittals Import Template to Procore").

### Before you Begin

- Ensure the user or users assigned as Submittal Manager have been added to the project's Directory tool. See [Add a User Account to the Project Directory](https://support.procore.com/products/online/user-guide/project-level/directory/tutorials/add-user-account-to-project-directory "Add a User Account to the Project Directory").
- If you will be assigning another company as the 'Responsible Contractor' for one or more submittals, ensure that each company has been added to the project's Directory tool. See [Add a Company to the Project Directory](https://support.procore.com/products/online/user-guide/project-level/directory/tutorials/add-a-company-to-the-project-directory "Add a Company to the Project Directory").
- If your project is using locations and you want to add location information to your submittals, the location tiers must already exist in Procore. See [Add Tiered Locations to a Project](https://support.procore.com/products/online/user-guide/project-level/admin/tutorials/add-multi-tiered-locations-to-a-project "Add Tiered Locations to a Project").
- If your company is using the project's Specifications tool to manage specs, upload the project specs to Procore (see [Upload Specifications](https://support.procore.com/products/online/user-guide/project-level/specifications/tutorials/upload-specifications "Upload Specifications")) or manually add them to Procore.
- If you will be using the Submittal Schedule Calculations feature, be sure to enable it within the project's Submittals configuration settings prior to import. See [Enable Submittal Schedule Calculations](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/enable-submittal-schedule-calculations "Enable Submittal Schedule Calculations").

## Using the Import Template

First, download the submittals import template directly from the Procore Imports app or from our Support site here: [Download the Submittals Import Template](https://support.procore.com/products/procore-imports/submittals/tutorials/prepare-submittals-for-import-to-the-procore-imports-app#Download_the_Submittals_Import_Template "Prepare Submittals for Import to the Procore Imports App").

### Best Practices

- Do not delete or move any columns in the template. Doing so will cause the import to fail. You can, however, hide any unused columns.
- Submittal Imports can only be used to create new submittals, not to update existing ones.
- All date formats must be entered using the date format MM/DD/YYYY, regardless of the project’s settings. Other fields, such as Spec Section Number, can be formatted as needed.
- For most fields referencing existing data in Procore, the data entered on the import must match exactly what is in Procore. Otherwise, the import will display an error message or create unwanted new records.
- If you prefer to number submittals as you receive them, you can leave the Submittal Number cells blank or add the number **0** to all of them.
- Completed import templates do not need to be unique for each project. If you consistently create the same or similar submittal items for each project, you can create a master template to duplicate and edit as needed for each new project. This can act as a template submittal registry and will save you considerable time on future projects.
- There are no limits to the number of submittal imports you can perform on a project. It might be useful to separate the imports by priority for large projects.
- Submittal Packages (Columns A-D in the template) are not required but highly recommended. See [Best Practices: Submittal Packages - Introduction](#s187104 "Best Practices: Submittal Packages - Introduction") for more information.
- Submittal Schedule Calculation fields (Columns R-U in the template) are highly recommended to help you understand whether your submittals are on target. See [Best Practices: Submittal Project Configurations](#s194924 "Best Practices: Submittal Project Configurations") for more information.

See [Prepare Submittals for Import to the Procore Imports App](https://support.procore.com/products/procore-imports/submittals/tutorials/prepare-submittals-for-import-to-the-procore-imports-app "Prepare Submittals for Import to the Procore Imports App") for additional information.

### Submittal Imports Compared to Submittal Builder

Procore's Submittal Imports and Submittal Builder are the two most efficient methods to create a Submittal Registry, but they should not be used in tandem. The lists below show advantages and disadvantages for each option to help you determine which is the best choice for your projects.

| | |
| --- | --- |
| Submittal Builder Advantages - Submittal Builder can drastically minimize the time to generate a Submittal registry. - Submittal Builder uses OCR to identify and add  the Submittal text from the Spec Section into the Submittal Description. Disadvantages - Submittal Builder creates submittals with very limited details, so  there will likely be more work required to add missing data (either manually or via bulk edit) - Submittal Builder can only be run once per Spec Section revision - Submittal Builder is only available in English for the United States, Canada, and Australia. - There are strict requirements regarding Spec Book formatting in order to use Submittal Builder effectively. Consider Use If: - You require a simple and quick submittal registry without a lot of detailed information. | Submittal Imports Advantages - Imports are significantly more detailed in the amount of data that can be included on the initial creation. - Imported submittals require less manual or bulk editing for their data such as:   - Submittal Packages   - Material Procurement Milestone dates   - Locations - You can import as many completed templates as needed Disadvantages - Creating the registry on the import template is manual and does not automatically pull in any data from within Procore (such as Spec Sections or other text) - Imports require a third-party program to edit an XLSX or CSV file, such as Excel or Google Sheets Consider Use If: - You decide to use Submittal Packages - You want to utilize Procore's [Submittal Schedule Calculation](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/set-up-submittal-schedule-calculations "Set Up Submittal Schedule Calculations") fields to determine "Planned Submit By" dates. - You  have a complex project, such as multiple phases, where you require separate submittals for each phase |

##### Tip

For more information and recommendations about creating a Submittal Registry using Submittal Builder, see [Best Practices: Submittal Builder](#s187102 "Best Practices: Submittal Builder").

## Next Steps

Now that your submittal registry has been created from the import, we recommend using Procore's Submittal Packages feature to initiate a workflow for multiple submittal items. See [Best Practices: Submittal Packages - Creation and Review](#s187108 "Best Practices: Submittal Packages - Creation and Review").

Alternatively, Procore's bulk actions feature can add a workflow to multiple submittal items from the list view. See [Best Practices: Submittal Project Configurations](#s194924 "Best Practices: Submittal Project Configurations").

## Submittal Builder

##### Note

This page describes recommended best practices for using Submittal Builder. Click [here](https://support.procore.com/products/online/user-guide/project-level/submittals "Submittals") to view tutorials, videos, and more about the project's Submittals tool.

## Introduction

Procore's Submittal Builder is likely one of the fastest methods to create a Submittal Registry if your project has a published specification book. Submittal Builder can find submittals based on specific formatting in a spec book and create a basic submittal register. This guide will show you best practices to help you maximize efficiency when using Submittal Builder. Are you ready?

## Why should I use Submittal Builder?

Generating a submittal register at the beginning of a project helps prevent critical submittals from being forgotten. What would take someone weeks to do manually can be completed with significantly less time and effort using Submittal Builder.

##### Note

Submittal Builder is only available in English for the United States, Canada, and Australia.

## Ideal Specification Formatting for Submittal Builder

Submittal Builder looks for specific components when it processes a spec book. If these components are missing, few or no submittal items will be detected. Please review the information below and review your spec book to ensure these rules are being followed:

1. OCR technology is heavily reliant on the quality of the PDF document. For this reason, we highly recommend using Vector-based PDFs whenever possible. See [What is the difference between raster and vector content in PDFs?](https://support.procore.com/faq/what-is-the-difference-between-raster-and-vector-content-in-pdfs "What is the difference between raster and vector content in PDFs?") for more information.
2. Submittal Builder only looks for submittal information within section headings that have the English word "submittals" in it.
3. Within the "submittals" subsections, items need to be indented to be captured properly as individual submittal items.
4. On each item's name, Submittal Builder looks for any exact matches to your company's submittal types (default or custom) before a colon (:). If no exact match is detected, the submittal type will be selected as "Other" by default.

##### Example

Here is an example of optimal formatting:

![best-practices-submittal-builder-spec-formatting.png](https://support.procore.com/@api/deki/files/390658/best-practices-submittal-builder-spec-formatting.png?revision=1)

Click [here](https://support.procore.com/@api/deki/files/390270/Submittal_Builder_Example.docx?revision=1 "Submittal Builder Example.docx") to download a Microsoft Word template with specifications optimized for Submittal Builder usage.

##### Important

Since you can only run Submittal Builder once for each spec section revision on a project, ensuring the spec book has optimal formatting is an important first step so that the system can capture all of the possible submittals. Otherwise, you may need to fo the following:

- Manually create submittal items later.
- Delete the spec section from the project and re-upload it to run Submittal Builder again.
- Upload the spec section as a revision.

## Submittal Item Creation from Submittal Builder

Before confirming submittals in the Submittal Builder's review process, you should know how you want your project's submittals organized in Procore. To better understand submittal organization in Procore, please see [Best Practices: Submittal Packages - Introduction](#s187104 "Best Practices: Submittal Packages - Introduction").

Submittal Builder creates submittal items with the following user-confirmed fields populated:

- Title
 - *Note:* Since the Title usually contains text related to the submittal type, verify the "Submittal Type" field is accurate before you configure and apply the Title. Applying the configured title will automatically update any existing titles on submittals waiting to be confirmed. Changing the 'Type' of a submittal manually after configuring the titles won't automatically update the submittal's 'Title'.
- Type
- Description
- Submittal Manager

Submittal Builder creates submittal items with the following fields pre-populated by the system:

- Spec Section Number & Description
- Status (All submittals created will be in Draft status.)
- Submittal Number
 - *Note:*
    - If the project has the "Number Submittals by Spec Section" setting enabled, then the submittals will be numbered accordingly within their spec section. For example:
      - 06 25 09 - **001**
      - 06 25 09 - **002**
      - 06 25 09 - **003**
    - If the project has the "Number Submittals by Spec Section" setting disabled, then the entire list of reviewed submittals will be numbered sequentially, regardless of the spec section number.

## Next Steps

Now that your submittal registry has been created with the above mentioned fields, there are many more fields that should be updated for additional context. To add this remaining information on your submittals, we recommend using Procore's bulk actions feature to edit multiple submittal items within packages. See [Bulk Edit Submittals in a Package](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/bulk-edit-submittals "Bulk Edit Submittals in a Package"). Procore's bulk actions feature can also be used to edit multiple submittal items outside of packages. See [Use Bulk Actions > Edit in the Submittals Tool](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/use-bulk-actions-edit-in-the-submittals-tool "Use Bulk Actions > Edit in the Submittals Tool").

## See Also

[Best Practices: Submittal Packages - Creation and Review](#s187108 "Best Practices: Submittal Packages - Creation and Review")

## Overview

##### Note

This page describes recommended best practices for using submittal packages. Click [here](https://support.procore.com/products/online/user-guide/project-level/submittals "Submittals") to view tutorials, videos, and more about the project's Submittals tool.

## Introduction

Understanding how you want to organize your submittals within your project before you start creating and sending them will lead to a lot less problems later on. Consider not only what works best for your design teams, but also be sure to take into account your field teams. Often, field teams are not considered enough at this stage, which can lead them to struggle finding approved documents later on. Also, changing your submittal organization plans is much more difficult after some submittals have already been sent for approval due to potentially mismatched submittal numbering between you and your design teams.

## Problems Around Document Packaging and Approvals

A submittal is typically considered any document submitted by the contractor to the design team for the purpose of receiving approval for usage on a project (equipment, materials, etc). Historically, most construction professionals think of a *submittal package* as a single PDF that includes a cover sheet and all of their submittal items. When a package like this is sent to the design team, they may provide comments on the individual items, but generally provide a single response such as "Approved" or "Revise and Resubmit" for the entire package.  When approvals relate to an entire package, it can create difficulties depending upon your company's submittal revisioning process.

### Option 1: Only resubmit the rejected items under a package revision

![best-practices-submittal-package-problems-resubmit-option-1.png](https://support.procore.com/@api/deki/files/390660/best-practices-submittal-package-problems-resubmit-option-1.png?revision=1)

In the image above, you can see the original submittal package was partially approved, with the rejected items getting approved on subsequent revisions. This is the most common revisioning method since it's typically the fastest. However, as shown in this example, there are three versions of approved documents related to the same submittal package. This forces field teams to waste time searching through multiple submittal revisions for a single piece of data. Also, because the items are not listed in a submittal register individually, it is easy for items to get lost or forgotten.

### Option 2: Resubmit the entire package under a package revision

![best-practices-submittal-package-problems-resubmit-option-2.png](https://support.procore.com/@api/deki/files/390661/best-practices-submittal-package-problems-resubmit-option-2.png?revision=1)

This is not as common as Option 1, but this is the best method from a document control perspective. However, this method can cause delays for already approved items and lead to design teams wasting time on nearly duplicate reviews. There is also potential for "Approved" items changing between revisions since reviewers tend to not pay as close attention to approved items on the later revisions.

Similar to the previous option, because items are not listed individually, items can easily get lost between package revisions, especially if previously approved items are changed later. Additionally, field staff need to read through much larger documents when they are likely looking for specific data.

Both of these submittal document revision options were developed well before digital files became commonplace and managing submittals was still a paper process. Neither option is the most efficient way to provide data access to the **entire** project team. As a result, Procore developed a new concept for Packages.

## Submittal Packages in Procore

In Procore, individual items in a Submittal Package have their own workflows and approvals, instead of the package as a whole. Within Procore, individual items are more comparable to the familiar packages described above and submittal packages are more similar to a flexible grouping of related items.

The major difference with using submittal packages in Procore is how resubmittals are managed. In Procore, when resubmitting a package, only the rejected items are resubmitted but all items remain in the same package, eliminating the need to search through multiple document versions. Procore shows the most current versions of submittal items within packages.

![best-practices-submittal-package-resubmit-recommendation.png](https://support.procore.com/@api/deki/files/390662/best-practices-submittal-package-resubmit-recommendation.png?revision=1)

If this feels a bit too unfamiliar, revisions can also be moved to a different package (acting as a package revision) if the design team prefers to keep them separate from previous submissions (example below). However, keep in mind that we don't recommend this option as it can be inefficient for field staff who would need to look through multiple packages to find item approvals.

![best-practices-submittal-package-resubmit-as-different-package.png](https://support.procore.com/@api/deki/files/390663/best-practices-submittal-package-resubmit-as-different-package.png?revision=1)

Procore's unique submittal package concept addresses many of the document management difficulties experienced by project teams, especially field staff.

- Because items are recommended to be listed individually, the likelihood that a critical submittal is overlooked is significantly reduced.
- Individual item organization allows for specific submittals to be expedited at any point, yet remain connected  under their associated package.
- Individual items can be revised as many times as needed but only the most current version is shown at any point in time. This reduces the risk that project teams will reference a previous version.
- When items are listed individually, field staff spend less time searching through separate packages and large PDFs containing multiple items.

### How should Submittal Packages be organized in Procore?

Most contractors use one of three options to organize their packages: Trade/Responsible Contractor, Specification Division, or Specification Section. We recommend organizing your packages by Spec Section since packaging by Spec Division or Trade/Responsible Contractor can be too broad and lead to large packages that are harder to manage. Also, packaging by Spec Section is typically more accommodating and less challenging  for multiple trades involved in  similar scopes of work.

#### Example 1: Package by Spec Division

| #23 Mechanical Package | | | | | |
| --- | --- | --- | --- | --- | --- |
| Spec Section | Submittal # | Revision # | Title | Type | Status |
| 23 21 13 Hydronic Piping | 1 | 0 | Hydronic Piping Product Data | Product Data | Open |
| 23 21 13 Hydronic Piping | 2 | 0 | Hydronic Pumps Product Data | Product Data | Open |
| 23 23 00 Refrigerant Piping | 3 | 0 | Refrigerant Piping Product Data | Product Data | Open |
| 23 25 00 HVAC Water Treatment | 4 | 0 | HVAC Water Treatment Product Data | Product Data | Open |
| 23 31 13 Metal Ducts | 5 | 0 | Metal Ducts Product Data | Product Data | Open |

#### Example 2: Package by Spec Section, Combined by Submittal Type

| #23 HVAC Water Treatment Package | | | | | |
| --- | --- | --- | --- | --- | --- |
| Spec Section | Submittal # | Revision # | Title | Type | Status |
| 23 25 00 HVAC Water Treatment | 1 | 0 | Bypass Feeders Product Data | Product Data | Open |
| 23 25 00 HVAC Water Treatment | 2 | 0 | pH Controllers Product Data | Product Data | Open |
| 23 25 00 HVAC Water Treatment | 3 | 0 | Injection Pumps Product Data | Product Data | Open |
| 23 25 00 HVAC Water Treatment | 4 | 0 | Centrifugal Separators Product Data | Product Data | Open |
| 23 25 00 HVAC Water Treatment | 5 | 0 | Multimedia Filters Product Data | Product Data | Open |

If you choose to organize your packages by specification section (Example 2), there still might be instances where you have multiple responsible contractors involved with a single package. Fireproofing is a good example and, in these cases, there are two main options to ensure each company is receiving the appropriate information.

1. Create a separate package for each responsible contractor using the same spec section. For example, create the packages "Fireproofing Package for Mechanical" and "Fireproofing Package for Electrical"
2. Create a separate submittal item in the same package for each different responsible contractor and process the individual items separately. For example, create a "Fireproofing Package" with "Firestopping Product Data - Electrical" and "Firestopping Product Data - Mechanical" as the submittals within the package.

## Next in this Series

[Best Practices: Submittal Packages - Submittal Itemization](#s187107 "Best Practices: Submittal Packages - Submittal Itemization")

## See Also

- [Best Practices: Submittal Packages - Creation and Review](#s187108 "Best Practices: Submittal Packages - Creation and Review")
- [Best Practices: Submittal Packages - Distribution and Revision](#s187105 "Best Practices: Submittal Packages - Distribution and Revision")
- [Best Practices: Company Level Submittal Settings](#s181271 "Best Practices: Company Level Submittal Settings")

## Itemization

##### Note

This page describes recommended best practices for using submittal packages. Click [here](https://support.procore.com/products/online/user-guide/project-level/submittals "Submittals") to view tutorials, videos, and more about the project's Submittals tool.

## Introduction

Once you have determined how you will organize your submittal packages, the next step is deciding how to itemize the submittal items within each package (typically called the Submittal Registry). There is no right or wrong way to set up your submittal registry, but there are certainly pros and cons for each option.

A submittal registry traditionally begins with the specification, so let's start there. Here is a typical spec book sub-section for lighting fixture submittals:

![best-practices-submittals-spec-book-example.png](https://support.procore.com/@api/deki/files/390667/best-practices-submittals-spec-book-example.png?revision=1)

We recommend that you start building your submittal registry by creating an individual line item for each of the items identified as requirements in the specification. In our example specification section above, these items are: Product Data, Shop Drawings, Qualification Data, Product Certificates, Field Quality Control Reports, O&Ms, and Warranty.

## Itemization Options

### Option 1: Broad Itemizations

Since the project might have 50 separate lighting fixtures, so each of these submittal lines in this example could potentially contain 50 separate documents for each fixture to be reviewed and approved. You might choose to stop here when organizing your registry, but this option has both advantages and disadvantages.

| #165000-1.0: Lighting Fixture Package | | | | | |
| --- | --- | --- | --- | --- | --- |
| Spec Section | Submittal # | Revision # | Title | Type | Status |
| 16 50 00 Lighting | 16 50 00-1 | 0 | Light Fixture Product Data | Product Data | Open |
| 16 50 00 Lighting | 16 50 00-2 | 0 | Light Fixture Shop Drawings | Shop Drawing | Open |
| 16 50 00 Lighting | 16 50 00-3 | 0 | Light Fixture Qualification Data | Qualifications/Certifications | Open |
| 16 50 00 Lighting | 16 50 00-4 | 0 | Light Fixture Product Certificates | Qualifications/Certifications | Open |
| 16 50 00 Lighting | 16 50 00-5 | 0 | Light Fixture Quality Control Reports | Other | Open |
| 16 50 00 Lighting | 16 50 00-6 | 0 | Light Fixture O&M Data | Operation & Maintenance Manuals (O&Ms) | Open |
| 16 50 00 Lighting | 16 50 00-7 | 0 | Light Fixture Warranty Data | Product Warranty | Open |

#### Advantages

- It's easier to upload all documents for product data into a single submittal instead of creating separate submittals for each fixture.
- It's faster to review all documents for product data in one submittal, instead of reviewing separate submittals for each fixture.

#### Disadvantages

- Because items are grouped together and listed broadly, there is a higher likelihood that a critical submittal item is overlooked. If not a reviewer is not paying close attention, they might miss that they only received submittal data for 40 out of the 50 fixtures on the project.
- When revisions are needed, it can lead to multiple partially approved "Light Fixture Product Data" submittals and confusion about which revision is  the most current version.
- Field staff spend more time searching through large documents that may have multiple revisions.

### Option 2: Specific Itemizations

Instead of stopping with broad itemizations, you can continue to build the registry out further and get very specific with your itemizations. Using the same specification section example above, you could create as many individual submittal lines as your project needs for each fixture's product data, shop drawings, etc.

| #165000-1.0: Lighting Fixture Package | | | | | |
| --- | --- | --- | --- | --- | --- |
| Spec Section | Submittal # | Revision # | Title | Type | Status |
| 16 50 00 Lighting | 16 50 00-1 | 0 | Peerless BRM9-1-28T5-SPR-20/80 Light Fixture Product Data | Product Data | Open |
| 16 50 00 Lighting | 16 50 00-2 | 0 | Pinnacle E4A-35-28-G9G Light Fixture Product Data | Product Data | Open |
| 16 50 00 Lighting | 16 50 00-3 | 0 | Gotham EVO-SQ-30-10-4AR Light Fixture Product Data | Product Data | Open |
| 16 50 00 Lighting | 16 50 00-4 | 0 | Pinnacle F36-A-35-G-120 Light Fixture Product Data | Product Data | Open |
| 16 50 00 Lighting | 16 50 00-5 | 0 | Pinnacle EV3WG-35-28-SFS Light Fixture Product Data | Product Data | Open |
| 16 50 00 Lighting | 16 50 00-6 | 0 | Pinnacle F48-CL-35-S-120 Light Fixture Product Data | Product Data | Open |
| 16 50 00 Lighting | 16 50 00-7 | 0 | Gotham EVO-CYL-30-10-6AR Light Fixture Product Data | Product Data | Open |

Depending on how many items are in a package and on your project, you might find that you want to separate  your submittal packages even further. For example, instead of just creating one "Lighting Fixtures" package, you can create packages based on your project's locations, phases, submittal types, or even separate packages for each fixture with all of the corresponding submittal items (product data, warranty, O&M, etc).

#### Advantages

- Because items are listed individually, the likelihood that a critical submittal or component gets overlooked is significantly reduced.
- Individual items allow for submittals to be more easily expedited at any point.
- Individual items can be revised as many times as needed and can be displayed to only show the most current version at any point in time. This reduces the risk of field teams referencing a previous version.
- Because items are listed individually, field staff can find what they need faster and spend less time searching through large documents containing multiple items.

#### Disadvantages

- Requires more time and effort during submittal registry creation.
- Design Teams might feel overwhelmed by the number of items requiring review and approval.
- Submittal distribution can be tedious because distribution from Procore is only available at the item level.

### Which option is recommended?

The simple answer is both options are recommended for different purposes. The best choice really comes down to the project and team needs, but you can use both within the same project. For items such as drywall accessories that rarely get rejected or referenced, grouping them all together makes sense for simplicity. However, with commonly revised items such as lighting fixtures, separating  that data into packages for individual fixtures is likely the better option.

Procore allows for the flexibility to support many different use cases and projects so you're always able to organize your submittals in the way that best supports the project team. If you are still not certain which option to choose, we ultimately recommend spending a little more time at the start by creating more specific submittal itemizations.

## Next in this Series

[Best Practices: Submittal Packages - Creation and Review](#s187108 "Best Practices: Submittal Packages - Creation and Review")

## See Also

- [Best Practices: Submittal Packages - Introduction](#s187104 "Best Practices: Submittal Packages - Introduction")
- [Best Practices: Submittal Packages - Distribution and Revision](#s187105 "Best Practices: Submittal Packages - Distribution and Revision")
- [Best Practices: Company Level Submittal Settings](#s181271 "Best Practices: Company Level Submittal Settings")

## Creation and Review

##### Note

This page describes recommended best practices for using submittal packages. Click [here](https://support.procore.com/products/online/user-guide/project-level/submittals "Submittals") to view tutorials, videos, and more about the project's Submittals tool.

## Introduction

In this article, you'll find the recommended sequence of events to maximize the use of submittal packages.

## Step 1: Create Submittal Packages and Items

### Option 1: Submittal Import

The submittal import option via CSV is the quickest way to create Submittal items and packages at the same time. The first four columns in the import are specific to package information. The fields are not required to process the import, but you will save time by completing them on the import.

![best-practices-submittal-package-submittal-import.png](https://support.procore.com/@api/deki/files/390671/best-practices-submittal-package-submittal-import.png?revision=1)

"Package Title" (Column A) and "Package Number" (Column B) can use  whatever format works best for your organization. For recommendations on package titles, refer to the previous article [Best Practices: Submittal Packages - Submittal Itemization](#s187107 "Best Practices: Submittal Packages - Submittal Itemization"). Keep in mind that a package's number is a user-defined field when you import, create, or edit the package. Procore does not currently allow multiple spec sections to be selected on a package, so "Package Spec Section Number" and "Package Spec Section Description" (Columns C & D) can only reference a single spec section.

### Option 2: Manually Create Packages

If you used Submittal Builder or just created submittal items manually, you can always add them into packages as a follow-up step. There isn't a way to bulk add submittals to a submittal package, so we recommend Option 1 above whenever possible. If you choose to manually create packages, you can filter by a specific spec section to narrow down the available selections.

![best-practices-submittal-package-add-submittals-filter.png](https://support.procore.com/@api/deki/files/390672/best-practices-submittal-package-add-submittals-filter.png?revision=1)

## Step 2: (Optional) Manage Submittal Item Numbering in a Package

We recommend that you use 0 as a temporary placeholder for your submittals' numbers when you create them because it can be difficult to know the order in which you'll receive and send them. As you receive the submittal items but before you send  them for review, click the "Edit" button on the package. In this edit mode, you can inline edit the submittal numbers. Once the submittal numbers are set, continue to the next step to bulk edit the package and send the items for review.

## Step 3: Bulk Edit Submittal Items in a Package

When a submittal registry is created early (before buyout, for example), the known details within submittal items are generally limited. Via the "Bulk Edit" button within a submittal package, you can quickly add the missing data to multiple submittal items within a package as the information becomes known. You can also apply a workflow from the same screen. Without using packages, this would be two separate steps for each group of submittals if you did the same thing via the list view bulk edit option.

![best-practices-submittal-package-bulk-edit-submittals.png](https://support.procore.com/@api/deki/files/390674/best-practices-submittal-package-bulk-edit-submittals.png?revision=1)

## Step 4: Initiate Workflows and Digest Email Notifications

Once workflows have been added to the items within the submittal package, you are now ready to send the "Action Required" emails to the first person in the workflow. Unlike creating submittals individually where multiple notification emails go out once you click "Create and Send Email", packages take a different approach that results in a single email sent to each user.

After a workflow has been added to at least one submittal in a package, a new alert banner will appear on the package view page. This banner allows for an Admin user to initiate a single "Action Required" email to the first person in the workflow. Fewer submittal emails is a major benefit for using the package functionality.

![best-practices-submittal-package-send-now-banner.png](https://support.procore.com/@api/deki/files/390675/best-practices-submittal-package-send-now-banner.png?revision=1)

##### Note

The workflows don't need to be exactly the same for all submittals within a package. The Submitters, Approvers, and Due Dates can all be different and each user will receive their own digest email based on their involvement in the workflow.

We recommended that you send emails for all the submittal items within a package at the same time. You can add new items to a package at any point, but clicking "Send Now" in the package alert banner will also resend any previously sent email(s), which could cause confusion for your Submitters/Approvers.

## Step 5: Submitter Role - Package Review and Response

Once you click the "Send Now" button, the "Action Required" email shows the recipient all submittals that now require their response (4 items in this example). They can click the "Review in Procore" link to go directly to the page in Procore where they can submit their requested response and documents.

![best-practices-submittal-package-action-required-email.png](https://support.procore.com/@api/deki/files/390676/best-practices-submittal-package-action-required-email.png?revision=1)

In the example review page below, you can see all four items have the Door Contractor listed as the 'Ball in Court'. This view is where users can see and respond to all of their items from a single page and is another major benefit to using packages. Clicking "Review" for each item shows its Due Date and includes the fields for users to enter their response, comments, and attachments.

![best-practices-submittal-package-review-page-submitter.png](https://support.procore.com/@api/deki/files/390677/best-practices-submittal-package-review-page-submitter.png?revision=1)

Because the workflows exist on the individual submittal items, due dates do not need to be the same for each submittal in a package. In the example above, we included a submittal item for a Closeout Warranty that is not due for several months. If the Door Contractor is not ready to submit this item right now, they can submit the other three items without getting delayed by this one closeout item. The Door Contractor will stay listed as the 'Ball in Court' for the warranty until it is submitted. Overdue email notifications will also be sent to the Door Contractor if they do not submit by the due date. This is a great way to keep on track for closeout deliverables. If your project's design teams prefer to receive "complete" packages, you can easily move any closeout item to a separate package.

## Step 6: Approver Role - Package Review and Response

The Approver's process is similar to the Submitter's process described above. The Approver receives a single "Action Required" email with the three items in that package that they need to review. Following the "Review in Procore" link in the email, the review screen is nearly identical to the Submitter role. The only differences are the selections available under the "Response" dropdown and the "Previous Response" section.

![best-practices-submittal-package-review-page-approver.png](https://support.procore.com/@api/deki/files/390678/best-practices-submittal-package-review-page-approver.png?revision=1)

Again, because the workflows exist on the individual submittal items, they can each be forwarded to another user or approved separately. Regardless of how the submittal items proceed, each user remains listed as the 'Ball in Court' until they post their response.

## Next in this Series

[Best Practices: Submittal Packages - Distribution and Revision](#s187105 "Best Practices: Submittal Packages - Distribution and Revision")

## See Also

- [Best Practices: Submittal Packages - Introduction](#s187104 "Best Practices: Submittal Packages - Introduction")
- [Best Practices: Submittal Packages - Submittal Itemization](#s187107 "Best Practices: Submittal Packages - Submittal Itemization")

## Distribution and Revision

##### Note

This page describes recommended best practices for using submittal packages. Click [here](https://support.procore.com/products/online/user-guide/project-level/submittals "Submittals") to view tutorials, videos, and more about the project's Submittals tool.

## Introduction

In this final submittal package article, we'll talk about closing a submittal, issuing it back to the creator, creating revisions, and other helpful information.

## Package Distribution

Once submittal workflows have completed, the Submittal Manager typically sends individual items back to the Responsible Contractor/Submitter. Since each submittal item has its own workflow and approvals, all submittal items are distributed through separate emails as described in [Distribute a Submittal](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/distribute-a-submittal "Distribute a Submittal").

## Package Revisioning

Like distribution, there are no package level revisions since submittal items are approved individually via separate workflows. Referring back to [Best Practices: Submittal Packages - Introduction](#s187104 "Best Practices: Submittal Packages - Introduction"), this prevents needing to choose between the two options identified under the "Industry" package. Only the items that need to be resubmitted are processed, which speeds up the overall time for approvals. Revisions for items in a package can be managed in multiple ways, but here are the two most common:

### Option 1: Resubmit items within the same package

When a revision is created on a submittal item, all of the previous data carries forward automatically, including the package. This assumes that you want all submittal revisions to be contained within the same package. This option is the most commonly recommended method since it keeps everything bundled together for faster referencing, especially when combined with the "Current Revision" filter.

#### 'Current Revision' Filter

Once applied on the Packages view, this filter will remain in place for your user account on a project until you remove it. This filter is especially helpful for field teams because it only displays the most current version of any submittal, regardless of the submittal's status (similar to "current set" in drawings). Below are screenshots of the filter:

**Filter Off:**

![best-practices-submittal-package-current-revision-filter-off.png](https://support.procore.com/@api/deki/files/390679/best-practices-submittal-package-current-revision-filter-off.png?revision=1)

**Filter On:**

![best-practices-submittal-package-current-revision-filter-on.png](https://support.procore.com/@api/deki/files/390680/best-practices-submittal-package-current-revision-filter-on.png?revision=1)

##### Note

This filter is one of the main reasons we recommend creating the revision immediately after the original rejected item is distributed. By doing so, you create a new line item right away that clearly indicates the item is still awaiting submission. This makes it much less likely that a field member will click on and build from an unapproved item.

### Option 2: Resubmit rejected items in a new package

Using this option, you add a revised submittal into a newly created package. This can be helpful when your project's design team requires very stringent package controls and numbering. However, the downside is that you will have multiple packages to search through when trying to find a specific item.

In order to prevent items from getting forgotten, we recommend creating revisions immediately after the original rejected item is distributed, especially if you are using the "Submitter" role (see [Create a Submittal Revision](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/create-a-submittal-revision "Create a Submittal Revision")). The due dates assigned during this process and overdue notifications will help ensure nothing gets missed.

## Conclusion

We hope these articles have clarified the purpose and benefits of Procore's submittal package functionality. While we realize this functionality may not be the best fit for every project or team, please consider these closing thoughts as you think about how to organize submittals on your next project.

1. Submittal packages can be utilized as simply an organizational tool without sending workflow notifications from the packages. Think of it as just another way to view and group submittal items.
2. If you are still unsure how you can use submittal packages, we encourage you to give them a try using broad itemizations. This option may look closer to how you've processed items before. If you decide it's not for you, you won't have a ton of submittal items to manage.
3. While using submittal packages may not be the right choice for your project currently, the functionality will continue to evolve over time and may work for you better later or on another project. To stay informed about new releases, we encourage you to register for our [New Release Webinar](https://www.procore.com/virtual-training/monthly-new-release-webinar "https://www.procore.com/virtual-training/monthly-new-release-webinar").

## See Also

- [Best Practices: Submittal Packages - Introduction](#s187104 "Best Practices: Submittal Packages - Introduction")
- [Best Practices: Submittal Packages - Submittal Itemization](#s187107 "Best Practices: Submittal Packages - Submittal Itemization")
- [Best Practices: Submittal Packages - Creation and Review](#s187108 "Best Practices: Submittal Packages - Creation and Review")

## Workflow Management

##### Note

This page describes recommended best practices for editing submittal workflows. Click [here](https://support.procore.com/products/online/user-guide/project-level/submittals "Submittals") to view tutorials, videos, and more about the project's Submittals tool.

## Introduction

The workflow section enables the Submittals tool's notification and ball-in-court tracking components. Workflows provide the benefit of automated workflow progression and action/overdue notifications. This article will discuss best practices for editing Submittal workflows. Are you ready?

## Bulk Actions > Apply Workflow

This feature allows Admin users to select multiple submittal items in bulk and apply a new workflow or pre-created workflow template. To apply a workflow in bulk, all submittal items must be in draft status AND have no previously applied workflow. The two options for bulk-adding workflows to submittals are described below.

### Why should I use bulk actions?

Bulk-applying workflows saves time by adding the same workflow to multiple submittals simultaneously. This feature can be used with Workflow templates to save even more time.

### Option 1: Bulk Actions from Submittal Packages

We recommend using Submittal Packages (see [Best Practices: Submittal Packages - Introduction](#s187104 "Best Practices: Submittal Packages - Introduction")) since you can also bulk apply workflows via Submittal Package Bulk Edit. The main benefit of this option is that you can also initiate workflow emails in bulk as part of the process instead of requiring separate actions to send each submittal item separately. See [Bulk Edit Submittals in a Package](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/bulk-edit-submittals "Bulk Edit Submittals in a Package").

### Option 2: Bulk Actions from List View

This will likely be the more time-consuming option, but you can also bulk-apply workflows from the list view if you opt not to use Submittal Packages. See [Use Bulk Actions > Apply Workflow in the Submittals Tool](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/use-bulk-actions-apply-workflow-in-the-submittals-tool "Use Bulk Actions > Apply Workflow in the Submittals Tool"). However, unlike bulk-apply workflows via Submittal Package, this option will require you to send emails for each item individually.

#### Considerations

No notifications are sent when the workflow is applied since the items are still in *Draft* status. To complete this process, you must edit each submittal item, update the status, and click **Update & Send Emails**. If you click **Update**instead, no emails (besides overdue notifications when any due dates pass) are sent.

## Bulk Replace a User

People regularly move in and out of projects, so there needs to be a way to replace a workflow user with another user easily. If you need to replace an approver, submitter, or reviewer on a large number submittals, a user with 'Admin' level permissions on the project's Submittals tool can do so in the Submittals Tool Configuration Settings. See [Configure Settings: Submittals Tool](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/configure-settings-submittals-tool "Configure Settings: Submittals Tool").

## Reject Workflow & Reverting Ball-in-Court to a Previous Step

In many scenarios, an Admin might need to revert ball-in-court on a submittal back to a previous workflow step. Some example scenarios include:

- A workflow user forgets to upload an attachment or uploads the incorrect attachment to their response
- A workflow user provided the incorrect response
- The submittal was routed to incorrect approvers

At any point in time, a Submittal Manager can revert ball-in-court to a previous step. For a more automated experience based on specific responses, we recommend enabling the 'Reject Workflow' setting. See [Configure Settings: Enable Reject Workflows](tutorials/configure-settings-submittals-tool.md#Enable+Reject+Workflows "Configure Settings: Submittals Tool").

### Considerations

Using this functionality to manage submittal revisions is not recommended. When you revert to a previous workflow step and new data is entered, previously recorded data - dates (Sent, Returned, and Due dates), comments, responses, and attachments - are overwritten. The changes are still documented in the item’s change history but are not immediately obvious. Additionally, reporting in Procore only displays the most current data, so you cannot get a true sense of actual ball-in-court durations if you shift the workflow back instead of creating submittal revisions.

See [Change the Ball in Court on a Submittal](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/change-the-ball-in-court-on-a-submittal "Change the Ball in Court on a Submittal") for additional information and instructions.

## Submittal Revisioning

The 'Create Revision' functionality creates a copy of the original item's details (under a revision number), excluding any previously entered data within the workflow. The workflow steps will be copied but the order will restart from step one so you can request a new submission from the Submitter role. This functionality ensures all historical data is maintained within the original submittal item while allowing new data to be added to the revision.

### Best Practice

The recommended process is to immediately create a revision when necessary after you close and distribute the original submittal item. This communicates the rejected information to the Submitter on the original submittal and provides a new item for them to submit under. See [Create a Submittal Revision](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/create-a-submittal-revision "Create a Submittal Revision").