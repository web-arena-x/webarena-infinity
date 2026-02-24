# Google Sheets

Use the Google Sheets integration to create custom analytics and dashboards for your company.

![Linear and Google Sheets logos](https://webassets.linear.app/images/ornj730p/production/e72a17743d75cacf18542c1c95122ca4bf4bc5da-2880x1620.png?q=95&auto=format&dpr=2)

## Overview 

The Google Sheets integration creates a Google Sheet for your workspace's issue data, project data, or both, allowing you to build out custom analytics among other uses. The data in these sheets refreshes hourly when changes have been made in your workspace.

All issues in public teams in a workspace will be shared to the issues sheet, and all projects belonging to at least one public team will sync to the projects sheet. We do not export data contained only in private teams.

There isn't a way to select what data is shared to the Google Sheet beyond configuring whether you wish to sync issues, projects, and/or initiatives.

## Configure

Go to the [Google Sheets integration settings](https://linear.app/settings/integrations/google-sheets) and connect Linear to a Google account. This will automatically create a Google Sheet called _Linear Issues_ in your Google Drive. Optionally, also choose to enable new sheets for projects and initiatives.

As this is a workspace setting, you can only connect one account per team. To share the data with teammates, update permissions directly on the sheet. If you're looking for a one-time download, workspace Admins can [export](https://linear.app/settings/import-export) a CSV instead.

## Synced data

### Issues

* ID
* Team
* Title
* Description
* Status
* Estimate
* Priority
* Project ID
* Project
* Creator
* Assignee
* Labels
* Cycle Number
* Cycle Name
* Cycle Start
* Cycle End
* Due Date
* Parent issue
* Initiatives
* Project Milestone ID
* Project Milestone
* SLA Status
* Roadmaps
* Created
* Updated
* Started
* Triaged
* Completed
* Canceled
* Archived

### Projects

* ID
* Name
* URL
* Summary
* Description
* Status
* Priority
* Milestones
* Creator
* Lead
* Members
* Start Date (Start)
* Start Date (End)
* Target Date (Start)
* Target Date (End)
* Created At
* Started At
* Updated At
* Completed At
* Canceled At
* Archived At
* Teams
* Initiatives
* Health
* Latest Update
* Latest Update Date
* Customer Count
* Customer Revenue

### Initiatives

* ID
* Parent ID
* Name
* URL
* Description
* Details
* Status
* Creator
* Owner
* Target Date (Start)
* Target Date (End)
* Created At
* Started At
* Updated At
* Completed At
* Archived At
* Teams
* Health
* Latest Update
* Latest Update Date

## Updating data

The Sheets data refreshes every hour if there is an update to be made, otherwise it won't refresh.

To run an immediate update, Admins can open the `Cmd`/`Ctrl` + `K` menu and select `Sync to Google Sheets` action. Alternatively, go to the integration's page and click _Update now_. 

You can rename the sheet or move it to shared drives without affecting the data or uploads.

> [!NOTE]
> Avoid updating cells in the source sheet as any changes will be overridden. If you want to run analytics, do so in a separate sheet.

## Custom project analytics

By using the projects sheet, you have more flexibility to build custom analyses in support of planning decisions. You can see an example of a project prioritization analysis [here](https://docs.google.com/spreadsheets/d/1qi3lV5d22ZGx-9mkHaDS_tT-Y1fT-BEKd7Ik87wkxSw/edit?usp=sharing).

## Custom issue analytics

To build analytics from issue data, import or reference data from the sheet Linear created using IMPORTRANGE, VLOOKUP or similar functions. 

Linear users have used the Google integration to build analytics that:

* Track velocity per team member.
* Combine with Linear's cycle statistics to get a deeper view into individual and team velocity.
* Track the types of work completed and planned. To do this, create custom labels and issue statuses in Linear. A common way to do this is to name labels with a prefix or key:value pair for easier filtering (e.g. _comp: feature_name_ or _type: feature/bug/etc_.)
* Build a Gantt chart for planning or other charts and graphs to show issue progress over time.
* Track bugs more granularly. What percent of open issues are bugs? How many bugs were worked on in a cycle compared to features?
* Track time: Use the timestamp data to measure how long issues remain open or how long it takes an issue to go from start to completion.

For more advanced queries, consider using the API or Zapier. 

## Timestamp FAQs

* Multiple issue statuses can exist in a single category (e.g. _In Progress_ and _In Review_ fall under _Started._ The timestamp exported reflects the latest timestamp at which an issue was moved to that status category from another category -- not between statuses of the same category.
* Null fields on timestamps mean the issue or project was never in that status, or the timestamp was cleared (an issue moving from Backlog -> Done -> In Progress will clear the completed timestamp.)
* All times in this integration are displayed in GMT.
