# Exporting Data

Export your workspace data using built-in tools, integrations, or the API

![Export issues as CSV option displayed after clicking on the overflow menu on a custom view](https://webassets.linear.app/images/ornj730p/production/8467997bef5508113d3245730f68905602daebc2-1186x687.png?q=95&auto=format&dpr=2)

## Overview

Export data from your workspace to build custom reports, keep records, or input into LLMs. 

### Workspace CSV exports

Admins (Owners, on Enterprise plans) can export a workspace's issue data in CSV format from [Settings > Administration > Import Export](https://linear.app/settings/import-export) and click **Export data** at the bottom. There is a toggle option to include private teams, if any. This export action is recorded in the audit log.

This export contains the following fields for each issue: _ID, Team, Title, Description, Status, Estimate, Priority, Project ID, Project, Creator, Assignee, Labels, Cycle Number, Cycle Name, Cycle Start, Cycle End, Created, Updated, Started, Triaged, Completed, Canceled, Archived, Due Date, Parent issue, Initiatives, Project Milestone ID, Project Milestone, SLA Status_

## Member list CSV exports

Admins (Owners, on Enterprise plans) can export the list of members in CSV format from your [Settings > Administration > Members](https://linear.app/settings/members) and click **Export CSV** button.

## Issue view CSV exports

Export a CSV of issues from any issue view, project or issue list using the `Ctrl`/`CMD` + `K `menu. In projects and custom views, this action is also accessible through the dropdown menu pictured.

> [!NOTE]
> Members can export up to 250 issues at a time while Admins (Owners, on Enterprise plans) can export views with up to 2,000 issues. 
> 
> Guest users cannot export issues from a Linear workspace.

### Command menu

![Export issues as CSV on the command menu](https://webassets.linear.app/images/ornj730p/production/8464b391e1fac11411e5269b47710611af695c60-1476x786.png?q=95&auto=format&dpr=2)

### Mouse

* When in projects or custom views, click the the project/view name and choose "Export issues as CSV…" from the dropdown 

![Export issues as a CSV option selected on overflow menu of a project](https://webassets.linear.app/images/ornj730p/production/24537d04edd782a6d2ccc69516ee9c1dc522a815-1106x1586.png?q=95&auto=format&dpr=2)

This export contains the following fields for each issue: _ID, Team, Title, Description, Status, Estimate, Priority, Project ID, Project, Creator, Assignee, Labels, Cycle Number, Cycle Name, Cycle Start, Cycle End, Created, Updated, Started, Triaged, Completed, Canceled, Archived, Due Date, Parent issue, Initiatives, Project Milestone ID, Project Milestone, SLA Status_

## Copy issues as markdown for LLMs

Copy issues and documents as Markdown with `Cmd Opt C`, or from the command menu. When copying an issue, this command captures its full context — including title, description, comments, and customer requests — in a structured format for use in AI chat tools.

Copy multiple issues at once by selecting them on a list or a board and using the same command.

## Export individual issues as PDFs

If you need to save individual issues as PDFs, use the Print dialog (`Cmd`/`Ctrl` + `P`) while looking at an individual issue to save an file in that format. On doing this, we'll automatically change the timestamps on each issue event from relative to absolute, which can be helpful if your auditors require seeing precise timestamps for each event on an issue.

## Project and Initiative list CSV exports

Export a project or an initiative view as a CSV. This export type is available to members and admins. Please note if you attempt to export from the issues page of a project you will be exporting issues, not the project itself.

### Command menu

To export only one project or initiative, select just that single project before opening the `Cmd` + `K` menu.

![Export projects as CSV through the command menu](https://webassets.linear.app/images/ornj730p/production/2fb7d05534506c42b04b097f7ccd2923fbf9dcfa-1158x556.png?q=95&auto=format&dpr=2)

### Mouse

![dropdown menu on a project view showing export projects as csv](https://webassets.linear.app/images/ornj730p/production/bace1f1cbbfd97b043e57d17ccf95074468e3ed9-884x562.png?q=95&auto=format&dpr=2)

For projects, CSV exports contain: _Name, Summary, Status, Milestones, Creator, Lead, Members, Created At, Started At, Target Date, Completed At, Canceled At, Teams, Initiatives_

For initiatives, CSV exports contain: _Name, Description, Details, Status, Creator, Owner, Target Date, Created At, Started At, Completed At, Projects, Teams, Health, Latest Update, Latest Update Date_

## Integrations

Our [Airbyte](https://linear.app/docs/airbyte) and [Google sheets](https://linear.app/docs/google-sheets) integrations offer ways to export and sync your workspace data to those platforms so you can build your own custom reports. If you're interested in exporting data for analysis, consider using [Insights](https://linear.app/docs/insights) as well for in-product reporting.

## API

You can also export data from issues, projects and more using our [API](https://studio.apollographql.com/public/Linear-API/variant/current/schema/reference), or work with Linear data using [webhooks](https://developers.linear.app/docs/graphql/webhooks).

## FAQ

<details>
<summary>Can I export teams?</summary>
Teams can be imported from one Linear workspace to another. Please find steps to accomplish this [here](https://linear.app/docs/import-issues#linear).
</details>
